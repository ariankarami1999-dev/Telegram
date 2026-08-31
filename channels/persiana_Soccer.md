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
<img src="https://cdn4.telesco.pe/file/Ei2kjxsPx73bAWGtPL7ObjXUjndd30NzswBKv_fF3Ey88Z3SRHpF7V_QUtSNZvufbiAMwW7zizIXOtdtQqfSdvf7wqJgaM2IaGQwQJDm2aajJBZXZ7Nq3Y1suLJaomKSIa-mz5ruunCVQZ4CslCDMVwNg2MAVTMd3AN0rxdoGfUhHrl7Qsxybe5hK12J2gYCReJjt_UlSV6i15H2TSKWW8n9NIu-LPnwKUsarwoUCBc9wiYQ1WIhVqSpokPOQXCNoK2xU7Pus1EJYIu9k484xAwc-Tg695wGR5J9aoOE-U3cDe8X6mAefvkWppzdHZmsZOGPhUAPx_H54sOJKVs5-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 614K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 01:27:09</div>
<hr>

<div class="tg-post" id="msg-28830">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jib6kRr6GDZShsHdd_8keR7XITVQKsT_WCNbBXuKFUecfoMQpsOb1nyZ_JpsiGZiSLI3cDlKq_1eFKb7cNneBaBjFgmXgrQEvBErdFG0WH7i31Ajwj9cM4Y1caX4v-C1_hmvFsiiqLI0mRTyRV5mEGKd1twjd3GCcfUpei8cdfMDKHxG8w-kPSx4fwO-yTmGhLVG4rRODQHAhhifZ8m28-KkwruEi17YUFYVRTuLOPQfQ8amhw7e6ynj4aCzgvRq_k-6VFR8yXNfcizBwxnTAFBuW75YtdW_DfPN5yuWd9PjGAsEGGIsIWtdtrwlAokg5fGhKrzho5gKXn6gEz8Vsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لالیگا|شروع طوفانی بارسا هانسی فلیک در فصل جدید با زدن 12 گل در 3 مسابقه؛ پیروزی پرگل آبی‌اناری‌ها با درخشش یامال.
🔵
بارسلونا
5️⃣
-
2️⃣
رایووایکانو
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/28830" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28829">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3AaF3QcOIWgoJKlO2TpiBUlHrxQ22sU7DgCFh-ujy2-W6aeJMkZMe-A8FPk1DS9DZN4Z3dhj1MRrnliAkcJsFRcUKxOCFSr_9nOHNW-t-rVyfsvJpjiPlnh4md8moaQ2i0dNDYzH15fn3J8E1JHiRZmxQqdPl6jwQmc2O8FxqQQej1D3DSRYdQSfi1UV1iVdN9X3-oT91n7PwUL7DxUigUhz6cYP0XzH4Taw97FSUGZ-DYu2fHGzSbcU5JyAU6GAEZsveOmrKLLy0XgiQzUMOm1cmmMfgo9pH6Qxaafj4Ulg2rDPJTt4d3tWGuwz6iOYzbVaJOgPJfe3C_xSKep8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/28829" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28828">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=g3AM8GOx5PwOs-8qPHj-ewYmQF07El_nZRkseIXRPNuaHRz2cWe7pZ2OSJTgU1G8V5UssCFZzUTSR7PXiSlZ7nKqJ-5-SOXur_dT947RL2meIk1kuA0wh4S4ueQHvzgp588-4hIHDIyVl7jZ4O5KKr0SFJ-I5cXc3ETnKN21iSgaBJcPrvXwEyEOlnMm7f6AqRFzlRtdqZrsYP3fBkioedwxmp0cmpCzE0T4Xot7g7WWV9C52gCTlr2qBsShBaQoAwbvfiq0oogmIOPWd1oLLj_tBEIj7Apvmf6PF0iFIOlsxid0q2yANnpUKHZwRvYzclqx2s5pshBsA2ciRnopqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=g3AM8GOx5PwOs-8qPHj-ewYmQF07El_nZRkseIXRPNuaHRz2cWe7pZ2OSJTgU1G8V5UssCFZzUTSR7PXiSlZ7nKqJ-5-SOXur_dT947RL2meIk1kuA0wh4S4ueQHvzgp588-4hIHDIyVl7jZ4O5KKr0SFJ-I5cXc3ETnKN21iSgaBJcPrvXwEyEOlnMm7f6AqRFzlRtdqZrsYP3fBkioedwxmp0cmpCzE0T4Xot7g7WWV9C52gCTlr2qBsShBaQoAwbvfiq0oogmIOPWd1oLLj_tBEIj7Apvmf6PF0iFIOlsxid0q2yANnpUKHZwRvYzclqx2s5pshBsA2ciRnopqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه سپاهان از باشگاه‌استقلال و هواداران این تیم‌بابت‌حرکت‌زشت و زننده عارف حاجی عیدی عذر خواهی کرد؛ این باشگاه همچنیین موافقت خود را با قهرمانی باشگاه استقلال در فصل گذشته رقابت های لیگ به فدراسیون فوتبال و سازمان لیگ اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/28828" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28827">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0zOpSE5M6aaDpt1V7H4l0YQiX9WzMzARqMcFJcJoSJNG7wOqM4dZDPrimolu6MGJtXzb1qHVib-JjBOhsUgEF3VmF9BRUa-kxb5wQzJUlCaauneIUk2LJSYQMSk3sGz48kTixlEMdjcXYqe6-XfJWY7KYQ3mEDcBL8F0nz5SxPi7KCaoivpGtvJSUTV8_ve3G9ZQ6co4X4OSp74N-IXcENLz1-gLrArSXaeB9Xn0QNFw6gMGKopFmEvZA8_fRckbf40160gq3R1ssOVvgtOQ2FG7xIzAZLa1NHFtZl32bl9Iveq6jOclCvEvctBI00ysHx40KBdDLAC8yooRZZbIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کجامیتونی‌همچین‌آماری ببینی؟فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@HUNTTER_BET
@HUNTTER_BET
@HUNTTER_BET
@HUNTTER_BET
@HUNTTER_BET
@HUNTTER_BET</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/persiana_Soccer/28827" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28825">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFpGLog-T938Klzm8OXXEVDMdaRz8vA469MI23T3B6B_KVIA6uL79pp6L8U4WVfZgBc1HZyxFXdyfihhhRdLzB6RedE6TRk19NWPjIkYLg8Kgt70uBxu3-ez5KFJ2Ug_slLt5zkzFMExrvCBTiMOwH224iritsYp-H6e397hPazR6zVIT7K6WWeAfNt5GxDqeqloQk0fQ2uI1xZFZyaj-jMSo0k3phAFR4WIxQf4r5t-WRkneMBUJRtT7z5TnXJHNeUGTWK5WNW6L0ojSxT_v140v71fKBVuBpJSkwn63zWL-kW9lsX-8XZzVZEDLHYApFqe8jwpfUPCLrRrQKTu_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت رسیدن شهرآورد پایتخت؛ مقایسه ارزشمند ترین بازیکن دو تیم استقلال
🆚
پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/28825" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28824">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=cUdwX-FrD7mi_EPgPDksyJrGuUhS05hx24-hjQgl8yHzAemzKWIjo_UUf12ryWUvw0Pcz360g8wEv2nm2nx54r7NOwAzfGRwACFNQpq-yCmppMjRvKdtiD7-f-u3aY13CU-vKgrdxyROkcmlgRgczHw7mkzYNum_oZ8urIQfyxoQ4-lGtmZzYS7AEomXOSEXcqVV54VpXWZubqrzDUlk8qGndfrhOVijIrWqBMzwpihFIaVdokezn66UgPYjJmTxdgttEi9GZFxuIcjb06HICcO9SlrNkC95zQ5obvyd8DzNNaX0Vvj-J9lbJCYqirt_dxItb8BYe3QTC_hzO2f1nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=cUdwX-FrD7mi_EPgPDksyJrGuUhS05hx24-hjQgl8yHzAemzKWIjo_UUf12ryWUvw0Pcz360g8wEv2nm2nx54r7NOwAzfGRwACFNQpq-yCmppMjRvKdtiD7-f-u3aY13CU-vKgrdxyROkcmlgRgczHw7mkzYNum_oZ8urIQfyxoQ4-lGtmZzYS7AEomXOSEXcqVV54VpXWZubqrzDUlk8qGndfrhOVijIrWqBMzwpihFIaVdokezn66UgPYjJmTxdgttEi9GZFxuIcjb06HICcO9SlrNkC95zQ5obvyd8DzNNaX0Vvj-J9lbJCYqirt_dxItb8BYe3QTC_hzO2f1nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/28824" target="_blank">📅 00:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28823">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWLFJakt-SW1oux1dtT2Brdd1GaJSekGePaHHqkJwY2XuYHs22mRXbkYdmBSqCkdjn-ryOjeiT0-BE4KbAaLGDAysSbzsk4ZKsFAWWf2g0WdWNuPBZiok4-T3TMW87lAWls1VVdCfe1T9bzw_mXhKrywWaPExwYNTGqfWFu7FE14XXIlkuxwgSj15JqcYXNTRyT_shjMLeCkmK6FA5EaLwLApi64MhfZcsbiwadyzkcs2SQHwteIfLky0RkSVM9cDFFaGle54nn4_aUkSWG3klkidldMfoECJbyG8AjyaVzqEpxzk-TLYDC9Pd-PEYJ8WNClzahvao1tELuRNHRxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت‌رسیدن شهرآورد 107 نگاهی بیندازیم به افتخارات دو باشگاه استقلال
🆚
پرسپولیس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/28823" target="_blank">📅 23:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28822">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F16ULvQtNLg_dmxy5vZX1uLSU5ErYJh3SdiS3lg1rnuTSFtQ8KI0jf4BtzgPOP_XfHm9UVG8vZioZ6qV5TWoi4PW1A3JRRjhDoYeVYQiOP14nm1oguR1p2cdBfW14vSbg_4i5KOdUxsq_LCE1p1sNRHAERnWJAg3-b3TkyxOd36DyvKhK4Ie2W9fLmiG9KEwC51rbjNz5oH_cMQFWNRGWSZNaAWWTcAjo1pMiyGLPLY7W4I9HuU4swCzfG3jS3DDY79Wpt59Inq3AiS1LQ5LMBDGZag2LaXU31dkUpb7BGU7QecUMRjT91eqUlyvJsxo3BfrEropG6jVlb6J8nOTCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی؛ از کوچه‌های‌روزاریو تا قهرمان ملی آرژانتین در جام جهانی  دیگر لئو‌ را با لباس آلبی‌سلسته نخواهیم دید. "خداحافظی‌ام را در تاریخ ۲۱ ژوئیه ، ۲ روز پس از فینال جام جهانی نوشتم. امروز ، پس از فوت پدرم بیش از پیش به درستی این تصمیم اطمینان دارم"
⚪️
…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/28822" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28821">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rab4EWM-tanhytoMLb8IqSYb4_l0B6TtD12GYGEstxeJ7f1l2KHQYMEPQwWDC9lCGLilQ_RE0TTh9OBRYV0SwYHhZA6maPnxt3_OamYHVICEMqd7tkHP0K4xVyVaCS5-REuoGhMPGmgqc-oo7QfSicXl0uR3_9GKEaWo8cdG2w5MEyvTyT5-5E54O2jo1Eu_uujLPWQu4aHTNFvSYNTCNQjy330S8xfBRFRIoGGaWG6_6072x3guJrrnLUEBDDhs-66JzlU2MYju0r07YzW5Vb8FmjSfnk9IQ5cs2fbbdzAPou-8CIeozxBR2z69OH8s1pxpih8QIV8uA2QZ0JgywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/28821" target="_blank">📅 23:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28820">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=fptYgem_sqFIlU7slgqPL9EStUkoxqMoePrbtO6gNQCHVhexUsCAu-OXsFi-qXjujVUm3r42cktruhZnesjorcjb3eepyP_P0tnkVcTXLL0RdZXwHUZGf7M6cppgIYFq0-9AQDLlkWKUTVjb6CCZ01DpHVWGGlD-pGo0WocU3Njm0i1sFdocUIyJD21Xa2ajRiTMHVEs4no8sK64FsvXaPMiyQ9XKvj2sSJA6p5hUvHr-fL7UZ2XUIqQXSz0no1Ffk9KHy_fwdoxO6pDdrverUd4sfh3zSHDE3J0evRFgy_xXwVJrlpoL8Tv3cCId1VjiseHVC1WRguSN5N-71vK-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=fptYgem_sqFIlU7slgqPL9EStUkoxqMoePrbtO6gNQCHVhexUsCAu-OXsFi-qXjujVUm3r42cktruhZnesjorcjb3eepyP_P0tnkVcTXLL0RdZXwHUZGf7M6cppgIYFq0-9AQDLlkWKUTVjb6CCZ01DpHVWGGlD-pGo0WocU3Njm0i1sFdocUIyJD21Xa2ajRiTMHVEs4no8sK64FsvXaPMiyQ9XKvj2sSJA6p5hUvHr-fL7UZ2XUIqQXSz0no1Ffk9KHy_fwdoxO6pDdrverUd4sfh3zSHDE3J0evRFgy_xXwVJrlpoL8Tv3cCId1VjiseHVC1WRguSN5N-71vK-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/28820" target="_blank">📅 22:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28819">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7g6t1_psYj8uPFRPLG1MA0vOxgc9h8RnbCOGWoArWcQOlqkLMCnrNWBrwsRNjyysqEoBgA_MW2cVbVJHIHT7odRctOkxMOM7pg722E0sdcTL6byZu6eCd4ghQcW-sfV8WyWBEh55xaFPkYD4TBLwRTWU5WYfdldrVtC_InTdiwj-5kUElZXuMN9hXcChnwDucYAYWbc8kYMk9CzhdtIiyUzlEB5RW-Kx8IVfNff-Eegy20aVpDc4T2gRmPDSSuGPkLBiCkZr6r0q75C2nKmBheZYg02LrGsYD3VKzxeoC0RmBYNzGOhL718LBp6sHdusZ2cXx41NlKYY8ctUXu4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/28819" target="_blank">📅 22:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28818">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PID26wGtTtVjIDhRbPfiH26aXeytkKF3HErlNUeBsgm0XE_O8dhsDe21RDJaO9iLxgLi748JLqHiVygb-qht5TqKG0jrRvdCKJ7IAWBiv2L0WfT5Q8hSBwlS06z8UVycwm2x-VVq5hSN2Ebp2YmvlMbHXhKtmAoYE4FBElFqYTLbr-BrpqrljQfC1OZMB4Mh_4BiR5HDzK5Zvt0rsGuCu6GyLzgQUFzQzhZagJ1jwscmQ5_RMTXSirwQ7txwGIxIiGgvcAW56xcDfUowqrOcMSqFUuJ8YEv9nwqRBZcYOTbzL292rKIRi85_mGm5XkRh_VqXWhpJnjwrBMVxmW8Nxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
ایلیمان اندیایه وینگر راست 26 ساله سنگالی اورتون باقراردادی 5 ساله به منچسترسیتی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/28818" target="_blank">📅 21:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28817">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aa9U1tfgY_PeIwyevoXUoLIapfeGLwHLBWOuQ0c0dMAXRB5LcpqFX8H2TQcOIoxBj1gtDIM8Fqc3VCcJxUVdsjVqtGfeFS7rqlNpdAtqrWYjn5tCHWwsBnEk9UXymSk2EH8uC0vq41Pf7oIkJBIEXke5-0ldZb3WFlbbNtUSrrLHy7D_l0stApK5CxbSM7v1BaNSDD_nOslPhdRQ7tRNWzp3_SRrN52d1ur0CYzvVrPGcLkTOWDXtlzw6KL8SsTX-15Gwq5e7NlAIurwJfZZI9sG6vsGHKgbf890EFbIvNAN_oXQKwC6xowIFBXTKNxMjGQYewFNmgbUsO5wNdP-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/28817" target="_blank">📅 21:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28816">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQaRiiFc4VfLf0GoKSg4RQXJWk_nv66Guy9I9hCm9xDdNI5-fkXdYRdOwmWjs-DoHyZO8Cu5xPAWo4Y-0Q-mZ6zi-MSDzStN_7ug5vIEMzDT6bYLJZiDPtP0HkuABliwWDroBG4yeedRiBBq100o5Tz7k1820qdgub0pmD8HVX9cuJm8TL0IzcVpwXA8z1V3QoxcDsxfMx3Lg4X-IDn-f7XwZWAgRvn0abPb7-eyzVY_zGcaaTezozKCJs-e2rSj6C72j4EWD6GCPeKlG9J0MiFudrSZgwnGeNHstajjFhlxa9pRz33Yp8y56CXQFf2n73qGkQcsA-NShX63ZqzH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/28816" target="_blank">📅 21:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28815">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/28815" target="_blank">📅 21:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28814">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMz09ju51dynKcg9cRskpinO6XD7X_4mvcI8PlinurCiukaBQ34V_qrl27-P5g3tWzcnVmewBSw5_5TKeXT0LsYoBEW2-OCv5G_obD19_CY0ibzmdL2tX7fMaKRwV9_sfELpBGT-C6jN5EsrKGT6v7X7Z5PRb3f6kYcKdPNjwX0cdsecWMBoKg4KG5d_0uFD4igr3uG8-57qo6LR3sRcqoJa_y6wRJTU2YH0fnIOkljUWzuhCTqkr_SG_7jmpSaMTKFObMO8xdYTl3OYe9I7Et4XwaV8mSS08KnpfxRqM7FqGETroNexKQ5ryga3cOCmg5A_n6jRgt4-VIl9q_X41A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌اسامی داوران هفته پنجم لیگ برتر؛ موعود بنیادی فرد رسما داور شهرآورد 107 پایتخت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/28814" target="_blank">📅 20:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28813">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIVZ44xKGIFXsRO1ChLVrCS58ZvldZlUWD0-l6qiqMhGMq3WQB-D1q82cwshbeZB7qCCG4sCVTGa4GL5PrZUMdYkL8HnBix5fcM4pm5T8k49UW8x15WZTzqSlJV04VD3JKJHdiS6S9S0pdLlK_uUcytGm8BCkMeWJimx9bLdHOybPQ76MEOh6zZoXF5qPlx2GuQ2I6BCDVPNncED7yYG9kDi3uDCwsivmjFcLjnHfeNLBz9o4wfpD8jgfTQhyVp96-0_MS3dqeniQWuFRI48omf2dfoIcsgd542cGXBiOsQPmQ_1gskJQfU5ntZPfR2Hl0yC8ubnJPij1GfZ_t88XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
جای‌داوروسط و داوراتاق VAR شهرآورد پایتخت عوض شد؛ موعود بنیای‌فر بعنوان داور وسط دیدار روز چهار شنبه استقلال
🆚
پرسپولیس انتخاب شده و سازمان لیگ فردا این خبر رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/28813" target="_blank">📅 20:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28812">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg57VC2dl6MDdldvXFnUME54tg5EPOCjAcPXiSa903HPfqYmKNdVrusgyeVz5wBFrvEKuasSfL42Iqy_OstvKHPQZ1-DgVLjTAPEDskmisGyGz4BtgkNlrQuSrahMU2pmWtpM0sn54aJSdL-IdcxcJDbB9gM1HPuXJ9BG1-v4fWKKSOfyFXjZpK08KBMgkyYCBpxxEYDgoBJvM873Ar_8NdyDCwyv9bH3efUr-g4H-ILNJvbBzKivAkji_btzL6isMVuxdeUfTQQMnyFTd7ubdQ4HIJYzhAxT723uXjaGX627RxEkr_y0GewZf7ZE9iek2hjIRA6kBd6K7Rb093oEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
آنتونیوآدان دروازه‌بان‌فصل‌قبل استقلال رسما اعلام کرد که بخاطرشرایط‌جنگی به ایران باز نخواهد گشت و مطالبات فصل گذشته اش رو نیز بخشیده و هیچ شکایتی از آبی پوشان به فیفا نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/28812" target="_blank">📅 20:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28811">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYbAmjL4sNKBornsB6Fh5S_Gwp7qnwMRSLtzuaZv2LsrlncxzF_ety4gFFeUdHYBaaroLKCZdABp0J2BQbHfgDi-j9ZPfThXCj1RLf21ioOyEz3-HJzvLdX_5dFjP502fjCBLTs4cG48XakK7tFoSehsOSuClGw27j6Iv5N8FOPHITl2jLuymYRvgUHjP3qHFbVT3SuMoXhxCoszTC-LpBcTir9AJIaoAd43dH0wVvwK-c33pQE-LlPINEe1p_d6p1dP-Dk04jGJ5O_EaR4OpQv9pQi8nWmCkc5EYcCOjbFzfZZPNSfQ_HX32G53pzz0gtLARKce8H1CT7emdBaKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: اتفاقات‌مثبتی برای اهدای جام قهرمانی فصل گذشته لیگ برتر به باشگاه استقلال رخ داده و به زودی اخبار رسمی دراین باره منتشر خواهدشد. در تلاش هستیم که‌زودتر آنتونیو آدان و نازون رو به تیم اضافه کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/28811" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28810">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOmYQLjhilLCFm6eghSEkm-I_970Ah4LNnMs_Hsn39bbQcQyHhwrU7wcxglVJ9mxUcAiyiiljL_lqmZ4DtHvBicvqZ8SxnIRmo22xNuAt2zPRT-VzebVo25P_fbbiZm30qvQBVqG1W_wIX31LM4tOOilDbdRy22S24j8EI49wlweNrjvlV5YGTZKuU92JvaVDtIz1oW6YCQ84ggMhj-PH65ALRvhWwAEVkbeBnLhM19Vjnqu7rkKIc6bl1Y9uyP7EplCicB9hSHdnNlihm_I-CIUhatuxJxqFHe8tW9Jg9M8-V7-UfjgaVNurKihRtnThLu4DpN8bsEFAVvuaP2nFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی چهارساله به منچسترسیتی پیوست. فابریزیو رومانو بزودی هیر وی گو رو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/28810" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28809">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYIRMWM_kHJcRZJ1Z88sriSTGIp0UMWE9gq7ji47Q_TzdxWZBa8YIniYKsF_XFZypJu_G6qlluhtjzmp-V3aoXKZq9J8Ev8fKMdJgnnBFALpxFOALd-NqzAnqkJ3vyczJtWp8LHn21yKgXn4mP1jpgM8j3s3BZUO7ev6qbp8cy0Yeot_jMR5RhLlhphM5Yl168mFQ8vIlEkfswD8FgH2p2-EBopBC0n7vBGkr7w8QV3jlUEKByut9sW9xHm07tjEteRVhFy0-pS5VsgfBJrZ11DJZzq_wjF5imNVyY_JDqUg2T_YDNKVatNLMMt5-y_kxibewsGkwEZolDdiOhbkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال‌سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت‌استفاده‌از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/28809" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28808">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JW8VcLzZCFpHKb-HSLIkR_y3a-q3OQ0LRNg6plybqBOalU-wdR5n-GAcNkCf9xxGGIslomlVaTmF1EEnt4aogaQMYzqgKIXYbqTekvDpdiKaVV8Dp20NMktPNUgzFsUFWx9VGXfqwVOoF0DCE8Adt9FVLfWZYv33ql-Rjh0ZMSNDcizMbP7Tq2zD4cIIcBPOB8ilD2kRlDktuVmPDPsn-cf7sxqgzS-KOVmcYuO81cJKdFMxGgTtXxH1ZDiMXyMQcQpmM8xf1u2qz0pPAKoccIMxbpOJBwv39GcGCyEQ3lhk94pMnVFuKl1tAFsPu8Yh2ju1No9bQSapZKSNLUlshA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/28808" target="_blank">📅 19:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28807">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=ki1JU2urNp_N1AZ_JDNFx981sauce2SxkBQ-n6lJWQLoQeAoEhdz7l-dbfeO9ZGBgkmZF6mYP2p8zH7wDIQ0FWsXgOf0K-XxzSYm_FLFzeWHSTkwAzAURkvSRCE9l-GEEfyLQs7nc1frI46MZxBPmlGxoehePeA6fOeKqrg8-xJ2bofGleGXxD4IceVIVnIh4QkecWCaKBHWCeLLxZ-uciwW7XY4LjSpDKCNHL7fGqMW7qBCmLKPINSwpC7gwb7eWKSC-LLFTmqVKRGmRISLvr_1T1v9RIhtBFYGx42PXcv1LHyLi_BHYlUW7NKLDDPe15vUR_YeeMiS5kKwFgDMTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=ki1JU2urNp_N1AZ_JDNFx981sauce2SxkBQ-n6lJWQLoQeAoEhdz7l-dbfeO9ZGBgkmZF6mYP2p8zH7wDIQ0FWsXgOf0K-XxzSYm_FLFzeWHSTkwAzAURkvSRCE9l-GEEfyLQs7nc1frI46MZxBPmlGxoehePeA6fOeKqrg8-xJ2bofGleGXxD4IceVIVnIh4QkecWCaKBHWCeLLxZ-uciwW7XY4LjSpDKCNHL7fGqMW7qBCmLKPINSwpC7gwb7eWKSC-LLFTmqVKRGmRISLvr_1T1v9RIhtBFYGx42PXcv1LHyLi_BHYlUW7NKLDDPe15vUR_YeeMiS5kKwFgDMTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/28807" target="_blank">📅 19:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28805">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXFexPfyszIisonRZmTB5grUmmM4V3LaUXYgFbBJZ8C8cDIfkttQuXqULf67QOqnp6QIN-vKngQoXqdk5yRRddJ20l72hfNJ4PtkD_q5DVkTpEGLU4l9is-xDE0ANsIENlMvqCWFmUZSJj8pdI3TS_HFdM4ncKoe6vY6bQ9AmVcK1uszRaS7KGlnKR83RpmSoaLZOSg-ZbcFfr0J7ParAFSqAnXHw4DdUvgoyy2nGeYinz1k_ks6eB1nMGXcFXvRBAHyzfdVqDxBOYUlEpMaHuoiHW0ltjYoI7HfS2Os-Z3Dmwczp6x5drWcgHWhGGuta-ItYNN8-RGDzp7xpMjKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTDdB5Dc-w1-X3eMGHS_mSVBEzwdOyj70FJAMEaf6csCz8tmNoqhcVARbNgxLDjdXORaotlIxphe1IM8-dPcSUo8cvK9ppnxjTiI_iKE0ZxSY-xgkqdmFwH6GXXZ1HQVHxK5XbhANvbYCI5pe2yobE7_KnKtCdm3kfucCKZkLF_C3FdSGtoNQhW1-5wgo_YmYOW6Jv-Cu8So6ncgIB-3tcj-WI6Z3AASbcTwsodoJbbdJyHpabFy6ZTbeUHwxlaAdjqWmQmVPyJGjcO-OZmep6vpvUhKYO9QKkIeqDKk-hXMBlUiTZ8q_RGHwHnMuIfxq8nTCN7Kll6D4suk7m8Szw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/28805" target="_blank">📅 18:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28804">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5joGjoYFkE-vO8cK_WLYvSDarCKqD7THQ9UM_iGOzTTrCAiibK08kLbkwQJcEbDi_30G7iUvv6sNTYkfP4rOyMU2q6SEDi6glQLeKtXijnJ1gkhqZJtNjAeyyWpi2Glat23IPHpCVuXn9nOPYVRGeZ79-TillczDWye6db_UGHHQ0tkEBGSPUn902n_ejMAqe34YIyp9K5e3Bh0Dc7i_M65OpOB5nYotnRR3M8jLNcZMygxDyUGl3KALNX4Or1XLAD-e7LFWeR1LvqLuf78VlNmlm1lOXBZdbSklRAZzE9XBYMQwForMp3f97eUZhwJoLhVxFdZWWTwtYhN8F399g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/28804" target="_blank">📅 18:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28803">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6Zrem8i5oBQrfsP52HTY1BX3hL3VWcIv8SbcTLVADiY8tbBrNnwHdinxgJ_DhZcoEHzM0o99UFbMGOn28YTkqxvkVfGjdK2PtKCOtUi_SrhKkMJ5ZnCWCtjKD3Ss3snvGZnpTfIQP0avXrUX4RN_fhFOn-wPV95bxzIllXekq7NCRVo6hVEfVRv0Yz4D8G3qjRPiipIBb8ccUmY1cHqluvDTzzN0xBUiEoPcjkaXlBzQy81htSZUe_dSg6IV1dHYCVZx5L4tNGIFCefIGGKj998p96EgwsJXFALp3cb46GfHsDFuN6qpQwwpJOuSz_s5JPA3SiPNEmOAGpseWu5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
عملکرد فوق العاده لیونل مسی 39 ساله با پیراهن اینترمیامی: 98 گل‌زده درتنها 111 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/28803" target="_blank">📅 17:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28802">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiE_CleKzn93ZChQXjAW3DYoKCnt0poB_GV7vs9AOHl3wRiD1FurBVilS0fXCtvBLNZi8smYtnyKV4avwCNbCXMhOhP_dOhITMTIPp927kzY-gkmzV6rZV8VxVRNCBqRBnVFsLaRh4eD4PiTqr7mR-5UiqUTbEC1BCcELdpJQJ5TRpYDkg983mNvNSgLImwMOha3guqfJbMNdjmgz11T2c9NZipq-ibQH-e157P8ob7bISYhy11wK3cPYxk7WxXMlaM8jv_9y_BZZ8u3zgje6eVfltpnYimnM6HUXzg1utkLUslfE1NAWJqLXAtVLuSgt89c3PwxST749r9892Cw7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تکمیلی؛ سانتی‌آئونا: کریم بنزما ستاره 38 ساله فرانسوی‌قراردادش رو باباشگاه الهلال عربستان فسخ کرد و رسما از جمع آبی‌های عربستان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/28802" target="_blank">📅 17:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28801">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlnvYBHV28krSJ93fF8Eo32VxGyAuJ7N3jUUu1YwWe0AfDAfOWQYeIGBJhxwcXzGqP8T7IVzWp0r3SiqOGFlB1cGW9hpwc6eu-btL1HXlPuAFaSk6-pWMKqjD4-MwPmoXqEsWg8lokYaLu80fhlRa7DR0uf7W9nhVicmAK23gng_m2mUHLoWSaCBGRu5PFscInTZoSE-W0KFQcSHG4zdMVh-hBzX13igaRPR2ru4KGjNrIxPzP6iIRBtt_U7L6J9OmL6ErxdKw88A3X4q__OLdCANQmj3l9b2HeNseMyze8Tm6uAr8UkiXPvI52fHkVj_DY6QGWXoZmixmIyACwTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/28801" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28800">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEVnewy415aCTKgIuNy4kKYVqYT4VjQKe_RvVDoNNRaJOQ1qwAb_9RGmutOT0gKTU0zmybgcGiTq-l-9XYEtFfBJsI6o3ATlBPK_6nxNaXB1u5lqJiijMtHkEhkw7WPjWg6YZmbauu5hLsDmhn0gsR9JdmGGDyql2E110VVbIKNNX1m1ZqYjgaE0JfR6MieBd_NztgC8xNMG6y1zNSicNzPN_ry1iRUV6JXjd9qgjIOkWTIurDr4YVsOh2I_DmwtLXApT_wmQjXiWyp-QD6xxtc-A92lBqa1EuIf_yQum2xt7JIL_o0ZZFD4S5TmeC_q7ukKW7Ng_SzdJ8PlxF-MFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونمایی رسمی باشگاه لیورپول از بردلی بارکولا ستاره فرانسوی جدید لک لک‌ها. لیورپول برای این انتقال 106+ 17 میلیون پوند هزینه کرده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28800" target="_blank">📅 16:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28799">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=OxxyRO6qg5kG-S52gj5c7ja3gX5g3twdzjVFb5BO1WR5Z-lrvwXCkw7VxTusZQ-4818GOl6GRi-xRKmjZjsBCvjXcvANPjwLRk0vEimQ8ahYnlNXFIdxrv41VxruTDE4TNriWL8cJ-win7mC53u5f3WdxeXgTRUjaDBpmb6Cqxd_b4R4n7fEC6R-4_qqN07bmfLlfcJpBrfhuJWyBo3Pw6px5H5tkkl5E-ZsnOPNBj4C8wA-slu5ISkuSot7OzKJI8T6na0fgOYoj9uLqR0XZxDbeNRd9WiPrjHtYOzQoSRJRqs7D32M1p-yQbGgiMnmQ1ACA4pWcCy8JuZ1h416vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=OxxyRO6qg5kG-S52gj5c7ja3gX5g3twdzjVFb5BO1WR5Z-lrvwXCkw7VxTusZQ-4818GOl6GRi-xRKmjZjsBCvjXcvANPjwLRk0vEimQ8ahYnlNXFIdxrv41VxruTDE4TNriWL8cJ-win7mC53u5f3WdxeXgTRUjaDBpmb6Cqxd_b4R4n7fEC6R-4_qqN07bmfLlfcJpBrfhuJWyBo3Pw6px5H5tkkl5E-ZsnOPNBj4C8wA-slu5ISkuSot7OzKJI8T6na0fgOYoj9uLqR0XZxDbeNRd9WiPrjHtYOzQoSRJRqs7D32M1p-yQbGgiMnmQ1ACA4pWcCy8JuZ1h416vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌جالب‌از استادیومی‌که.دولت تاجیکستان در عرض دو سال ساخته. اینجا هم ماشالله با وجود حدود سه سال هنوز ورزشگاه ازادی بازسازی نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28799" target="_blank">📅 16:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28798">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVQwx11pTBpaeJ1g8TTQ61Ni_nAt_-XETeXaGOSJwNli4siORYW6lxOEjk2D3-E6YBEOwteFYtQaMXkzaDv2FruO3QJyxMvsV_-VwEhKrIGwk06y0h6HM8bm3SP0VxW71JBTIta-xb_hi1fKIFpZ98MLxynuZ5guKIPVST-S1WeAAucIKBweQopu9juEXSjl8D0DDEFDeZIs5RKXYy8v-WLWT_jYLcUEC_FQnwQhF1G0uwiuYpg7O4EKhHcj_k09gsJg0RSciGBzEyCzLndGPILyudcTBisg__fl9yyskx9n2O5v1XCFtJ46GjDlb7DglUOqMHcJ0U1sgZnCUhP0jdW8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVQwx11pTBpaeJ1g8TTQ61Ni_nAt_-XETeXaGOSJwNli4siORYW6lxOEjk2D3-E6YBEOwteFYtQaMXkzaDv2FruO3QJyxMvsV_-VwEhKrIGwk06y0h6HM8bm3SP0VxW71JBTIta-xb_hi1fKIFpZ98MLxynuZ5guKIPVST-S1WeAAucIKBweQopu9juEXSjl8D0DDEFDeZIs5RKXYy8v-WLWT_jYLcUEC_FQnwQhF1G0uwiuYpg7O4EKhHcj_k09gsJg0RSciGBzEyCzLndGPILyudcTBisg__fl9yyskx9n2O5v1XCFtJ46GjDlb7DglUOqMHcJ0U1sgZnCUhP0jdW8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه پاریسن ژرمن در این پنجره با فروش پنج‌ستاره‌خود 335 میلیون یورو درامد کسب کرده‌. البته انتقال بردلی بارکولا هنوز رسمی نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/28798" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28797">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGpSWvtq5KXFNdhysuERKVPzQg1Qvx4GJpxB6jZx7LpCQnSCT7UVQG9cN9wf3EfDq7aor00MbPYfujffOCZ1PiIUEECT_9MD-XtF3pWn_unknfldC5xjQ8QCg-Riq-fru7MmrlbFid7f7TiNuID0xoyyfDK_FMlhbqBQzxYxlS61EqGgZYHXrjCmJOdXUXsOZhFVSxru_bM0pIWL8OOupPkjBGXc1MYJvmHqGEjT7jFnD2xnXbSRYU5Me9vbZ0edK0Luv9cZnYldY-4gyFctsPoGkrtLfGOxWDF8O-e_MaDiSEDLjMgOWu8Adv-OcEO8kELxLOLh3LyMmwYYvBzi7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28797" target="_blank">📅 15:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28796">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKrRO8S-gDsLpiVYn3fXhKAZjOg89GZXgv8uqCBJbZjGTlSrBRNQc4CD0000KW01BEX4vQf7iNXDst9m9WRLuRuReCuqg256PhpvkNnj9_CfyK5yqTG7CexMnMO2jhLE6xcE4WCSPgwfCMYjlP6MRVPwcwHxT052tBNLEiOoqc_rVF-tyri7lgqZcdRUHe5rGQdVi_bnn4OaiUs9XE78J2p5vDdwwcgHU4WtI8OtX13xJ1u65MUDJfyz6IqIXYKttzFW8K96gS1NC32Rk3Rucr-e8mefdE3dhsvHq2nGWyvLr7ez77Yc0wa_t5W3zID5vSsvPsiU7kCrMgmLk0WajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28796" target="_blank">📅 14:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28795">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdCe0164fl6WAJsvmB5FcUNofWzAAwFBWCyzLSdsE0JMt60_Q_qGMRfVEHM8tnAUHDMuq2R0mQlNPXm5IuEKX0VP41YHbpXpW2v-QD1k__OCioosnxlx_ULMnFObjURAdVcNW5P2jfp7kiz2e1KttcRTgjbBcqwq-taBs0XwfpuI2PmeEIiUDD1wbd_lhFQSbvtk0nE3f3JQB2ki9cajWYCUtWt0lrMVV8mW-7L9Fv-BGM1pMbd2YYCHXDh_D7g_e2Ci7CkmU2tM9aF7IpdC9Ec2cA9kg4AbED3B8a5XYZWNyEiKfDxc_wJBZ7-YxabpWmZkm4L2sybPdpQtqFBIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28795" target="_blank">📅 14:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28794">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔵
🔴
درفاصله 48 ساعت تاشهراورد 107 پایتخت؛ ویدیویی ببینیم از زیباترین گل‌های تاریخ این مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28794" target="_blank">📅 14:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28793">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8HT2LaGlrYPbAwcGB9G5TjqFyR93dWLJ10z6uPQclaTFFEVg8gdyl_dfkGGUXwy1Gu66eS4mQa1gCjOI0ppui7sjcPl_lP2dYU9NC6uGiD_97vfXqlVZGkxDoiDoVxLB0B5d-Tdxrvy_5TYltGF4I84E4LZP8n881GOxkMLW8BVBAHmLv12OliPK0c_MnBvQp1L4GnZO80m_KiK-cLoeQMAGrNJmCUihVBOHvIFW_2C0YbifCqMT2T-e_Y97GwDAMcpirE9H3bAWZ_80jIL04Ww6z9pMhNJPlrPrHqHv0ZuXvtZ8XbyPpP0ftvDE1kGb2F47d6rXaAPm8dR3t6nNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های کرواسی: آفر باشگاه رییکا به محمد محبی دو ساله به ارزش 1.6 میلیون دلار بوده. یعنی سالی 800 هزار دلار بود. پیشنهاد استقلال به محبی برای پیوستن‌درنیم‌فصل سالانه 1.2 میلیون‌دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28793" target="_blank">📅 13:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28792">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTlJXjyiIcnSxcNzdx1c_3kOoZhRI9CBc_RJRGTYg8stGH4trQF9tZfMQwLPwQ9g8c5Vz8mhWn9Q5QZiZVJWDdV6rd2oO33XFdSE0VQjo-2EovW9B5o_vDJ-4lKNwLP9ooTB8BuWAl_14TV4v9K_4HPSvhM9_syPjJT24LfrfDOBPfrHe90uHr4YtQezHUeU0s0hUSkRLiEpTgbu0s82Y5X2gQUK0od9Y2T6oa60RtV0rVp7z66MS9zwzPoR9S3gL_scCeazrje7FQirwufnEoOL1aZD5h5FC7_hmqxgLBltXZvZvZZFYXNb68qWj0G-gqz1mdj9GRrE36OTdRGvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28792" target="_blank">📅 13:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28791">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627b425286.mp4?token=e_LU3pecPzGbXjR0_3fxVvJlyWcpesotzkmsxWgw4RwdexBZamWMCuqfYaaNVa-PzJKpoBX1C9huMHxI1n5WPnlf51-llR5KvYrCi0eEptRIVrA1akOOEqZ3LdlDnOVZUiKHafXS8FzwoRMVZN90GUn8pdThGN147duupBArtBGw_Pxh9MRdJlU9BsrLctyivH9YaI8GQgZokHyYJgY6XJeeftBGbsh2nozz1SYWGsZZysbmc2IWJF-SPTr3SXOJ1-_T6-7YCH-KhqAI40DvTM7ygm-d9IzcjYNl5ljT9ZIp17-HCuR2km3v95HO0_23qBb20IklKREwbkZQM5MJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627b425286.mp4?token=e_LU3pecPzGbXjR0_3fxVvJlyWcpesotzkmsxWgw4RwdexBZamWMCuqfYaaNVa-PzJKpoBX1C9huMHxI1n5WPnlf51-llR5KvYrCi0eEptRIVrA1akOOEqZ3LdlDnOVZUiKHafXS8FzwoRMVZN90GUn8pdThGN147duupBArtBGw_Pxh9MRdJlU9BsrLctyivH9YaI8GQgZokHyYJgY6XJeeftBGbsh2nozz1SYWGsZZysbmc2IWJF-SPTr3SXOJ1-_T6-7YCH-KhqAI40DvTM7ygm-d9IzcjYNl5ljT9ZIp17-HCuR2km3v95HO0_23qBb20IklKREwbkZQM5MJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
بااعلام فلورین‌پلتنبرگ: میکل بازا پسر خاله شانزده ساله یوناتان تاه مدافع آلمانی بایرن مونیخ با عقد قراردادی تا سال 2029 به بارسلونا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28791" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28790">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZb6Eeq8-M6vlzK1p6g_GEk5hwYkZ0Z9Yz2Cv_diBwiEcWOn_ljMxI_WMsfTd8_Cfy32YQtPzH6gAueNJE7qLNNSL-ZaxWWWK3HgpixdGrU2EZOcI-lqaS2iAWw7-TYHsDPPHIR56d5eFXyJ9XjaqvaVT2Tdap2OEozO_zKsxh4WViERvOglW3p0xKYL16Bptkj5YD4l-MRg3aqhgxBO56zZ5O7ngEjuedbWbfQjkni6NxXcOXi794TvBGSJgIQ_asBVUmPE8RKXbsW6NTbt3nFN_fyXEWFISPWXzr_ny06Yi0gHVVkiQNz6FApBoX7mYstbZFA47MHnMlgLlazUKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت فوتبال تیکت اعلام کرد که بلیت فروشی دربی از این‌سایت انجام نمیشود: بلیت فروشی رو از طریق باشگاه استقلال و سازمان لیگ پیگیری کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28790" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28789">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXJSoBrsmszdoVzI8ZT7Lo5sLGGHKvKL0XqqGgQNoHbbAZdfFIvY1-GT07rR_eIQQ7os6VdfReHXFVKZsQnoPdBbAVfpiLhp1-sMXkTUfiEZrxHt0Q-1btKQDZCJiCJXp0hDYd_Gdt5a6q8SIsE37dPemh9zW9_GF_bS4Us2mArrCTZPCsV7W_B-BKKbNaJfSRGvCMHbTbovHjis171gqe_Lz1E2sdYl4668LEhxLzeQBcGxv4j6B88LcX5Ke1FOy4PKakIfZ1nQdBHgq2EMyPxUl2mozij60C1KZikQrKnuJ9axEybkk6gsFtbiKkX0spnsV_dnQL4QL-IgkfabxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفت خرید بارسلونا دراین پنجره که بابت جذب شون مبالغی بعنوان رضایت نامه پرداخت کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28789" target="_blank">📅 12:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28788">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtqxZWBc8W2PPBYv1r_RD2PQ0O4FRQinjcSOtw5uCREeG-ZO4cg7Htuakw2dh8IeTZViRWvTCQ0GUgHrXniDs7HW6ut_9a6aJir9jBgzD7Ik0A2InFvUB3gcEYfaH6_yIv8vG1UV0sas0ep35CcejXcs9OHhWcYQAFLVf13AefZEmwtJee6ASXlH_924a4qE9Bg73JcgfCOjSuHrJIdZm2suDWb30W0FUTNbkUp-jaB8HDAzM2m2AQ-yHAfWKL0UAVdpvTDReeWH3h03WKs0itBPgAiAyfhEGnEIgt--cImbZ1VbjQmCPYn9jz_661CvKdFVUyGvli9ZFub7v5rLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28788" target="_blank">📅 12:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28787">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-sODR8ETopMqa89Aqz5SCDWAko1_ezVjrbln30TFayQuM3A1-KiUFy2P1WN30bkXfwdLR2ueYModry33sY0xNqgJ9QBnbBDYFjHVw9cDgDPJAEtiRWypB47HtVAfPGzR88DzJB6hoWaqkXHOSKCs-rcFY3fiF0Lkx-2wzctXP2QFuIvuCjz8wxtl0epNcUImEESGYcOAULckacKNi_NyHWC89ZjnYc-Bwux-TAn0UWriZu-XQ9G-2tKXKUsIAkqoY6GdKZezrX6GKk_sr2XpE3_KQD5z_6stqzTIR51sHThJWsAc77CFIve1UJWUXwAmyl64cAL3Occ-zeNu-8o1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
🔵
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ درصورتیکه‌هلدینگ‌خلیج‌فارس‌تاپایان این هفته 400 هزاردلارپیش‌پرداختی به عزیز گانیف ستاره تیم ملی ازبکستان پرداخت کنه این بازیکن قید حضور در تیم تراکتور تبریز رو خواهد زد و آبی پوش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28787" target="_blank">📅 11:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28786">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqYycztowjz-UV5T3EUQmg08CkDKAtNwuFP78fyxQdK_4qtAzwuGQeZXCUhiGQRoOawmhKD4h1J0CYS-PaLERNZZCYunEJnXkjGeSvwDZSjmoTxgI3C9Nk13bfY4h00zQSGWpPYrzqfVv6v72ReJuNoBwJP-wRwp5cEInuR6PDOMUu96Eynic759zfTe9_eyYnm130YH5nRM9R6uDdoHUslnsLeIsojHoAZnjFeHEGapFwwZ4z_9oieojFFLxcdjxWKnw76SIrMBL_cv0YimyTPbHrE2aY8NnSZPqIyM9FbratVzN4QNeHXC5MRnbkMco_cuNCNUlf5sLX5TXP-7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28786" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28785">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRXVna7QKwHekkX3uumDSr-b8vmo7U90nWAdgD51AlnHbdwn1tP_wMxBUQ2OlfO0IlNEDSc7IQUAwzUfB1kO0uYVKy4Pq8at6rT0q36oUVqGCVLnlZAQPQvQlAhmJFGkZDClatWulEiosK-HZtEH78Kp0XkauuTin7DWgvoZlR9nVdAZX81FFKXMyB1pmyxGiMrllaQ4fgoS5XARr0yuq7cFCCYgYqNSTkmvnV2VDOTDRFIV6iViSou1CSDKdS9QJFJ3twDBMYIUnnNNnBzPgsqXUksrK1BsGED841RtUwKIR8Rj0BvvXYgAqs4I6zoXq99GAS5EGxXxVJA6kqLynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28785" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28784">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXlukjuRF-yIGZ06wsBXwjlclqE_gvuJOI-g3_S54YkfwvKir9LSKf5vHLUo37qkzqeupXGg6yOQaxja4YXZvHRhB5f0fc-Zhxb5ZI16BHTxfzkIOSCgrrxAylY9VTtZIoUAkgHRy176k4mR0Ikn3grsbikcblkwZF5MdK3okhNUyOY-cg2BmMMDvptg5ICE4nbDU71ulHQ1ekl2gZF3yeI4xdqvxXl626f8OH8fj4ZsCKrW2MqKm14R08-bbCSmOPgfdtkBhnLo49sHrSYxNOO2xBUCwnmke8dlqT2SYBc8UNK-i95aQYuMZq0We1Wpo5VRx9mvvpYoON7I_5sTxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28784" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28783">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZNOi11T1lvhnrZwFV5sqeg8Rwkjsncjb_1TMb5aaJwOBb92A5g29eJ1Kx3O-T_hn6vUuJgHomL9luedIA33pFLMeyZGmrPYaIad4XcTJ2N5TM3DRfZ_V83Nh017kDguRLFjeOk9JE13th21Ur-vzGUwdeKvB2pPGu_toeDE3YN_S_H8Q-4bldenMpcfgmoF5F6F_xbAoIyjdITegPZeXTB1q6sTLP7SER-BF_ZLexT7yTjFu6L0TU18hBv5NGR0iNSSyLF8LNeR1XCAwZpw4ZUdo9R09qLAx1iNfwZD-Xgib59UDb5SBwdJLEgW7dizDuP-2JuzFfXcSA-H-1bgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28783" target="_blank">📅 11:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28782">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf70d43b37.mp4?token=P0g0x3ULGmm9N4s-DG9WDxVinc-hTbGR-o4da5shObdKFRI9Lo1mEnoy-wnp36-HBKzB5SnLRHG_WYzAV34sTl_LUOJSeoJeoHhrgpuGMxXIcmRBFA6z2HXMrA5kfVb78FLLmvfFcVTrGJEDtrhCO8x7fxBs0wYbfdx1GenMMLUMWPwuR4VQNGswjwlkEOu-SsNeNc9JYf9hV7wITcukN43djRkf960ns2r6STiUAuRk5HHxxzYvb4rZ6kwWnCtp-mbeepu9SoiliD-qicDgKA5NvwK-M9Pm_3e4u8FlwbIubw52PzH0GcWkjz0WZrUqHCFdPM3xdVs0gz6MXelgLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf70d43b37.mp4?token=P0g0x3ULGmm9N4s-DG9WDxVinc-hTbGR-o4da5shObdKFRI9Lo1mEnoy-wnp36-HBKzB5SnLRHG_WYzAV34sTl_LUOJSeoJeoHhrgpuGMxXIcmRBFA6z2HXMrA5kfVb78FLLmvfFcVTrGJEDtrhCO8x7fxBs0wYbfdx1GenMMLUMWPwuR4VQNGswjwlkEOu-SsNeNc9JYf9hV7wITcukN43djRkf960ns2r6STiUAuRk5HHxxzYvb4rZ6kwWnCtp-mbeepu9SoiliD-qicDgKA5NvwK-M9Pm_3e4u8FlwbIubw52PzH0GcWkjz0WZrUqHCFdPM3xdVs0gz6MXelgLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی‌جالب‌از سبک بازی خارج مستطیل سبز کول پالمر ستاره انگلیسی 23 ساله چلسی انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28782" target="_blank">📅 10:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28781">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇿
🇺🇿
هایلایتی‌کامل‌از عملکرد درخشان عزیز گانیف ستاره‌ازبکستانی مدنظر دوباشگاه تراکتور و استقلال؛ همانطور که شب‌گذشته‌گفتیم درصورتیکه آبی ها این هفته‌پیش پرداختی رو به او بدهند آبی پوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28781" target="_blank">📅 10:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28779">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28779" target="_blank">📅 10:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28778">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqsSC_omjWOJ2PcAqQvmyslfj2hNdHY_scfVyQzztjK1GHYHvDLB-sI6-Qx9HOginHhEfnyrtByrXJkkq77BIGx0j2_fpeILoGnPb-Kfu8J0Vjhf35WeX91zJHFZ0gotPS_2SlgMwlp1b9ZIEjoKBx5xx_iUoyY1qC585_dM7SOyjNYQ0MnV7vBVmon6WViG30cF4ljK_2sLQkYjpd9WKrpxx-UeSt-5-sCQQjT7XjJrnfmJLA9lyb-0cZnrdgQmFgffBg7jdnaI2AbG22cY3vBl2A3OrvtkaTLLU-zTcPecYLLIHAV7sQOBnlVTahjyBFSIkkLjvBoYH0d3WRgzQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مصدومیت‌جدید مهدی ترابی ستاره 32 ساله تراکتور مشکوک به پارگی رباط صلیبیه و به احتمال زیاد ترابی 8 الی 10 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28778" target="_blank">📅 09:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28777">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edcdd5b47.mp4?token=ZDJz8jaCN6KhiBhiuGFZ01gnL4oBR89kPD9k0-Hno1NVSXlD_zb-wkoHyIHwFHvJPL-oGY8WJ-XqjeZS2qYQGQ-MyiRtEwPNiNmLHIvj0YAO9uR2U65rD6kOA8u1RRgQkqHE3yy-oa07bpsdonygcnSkzlBPFafrgyUPp43lz55UloZeepXXgBdI90FHB8A0MRNfke8YNyVkE3M5wFD6GOZYf5NHqk9SAEWgp-_k61KlQ7tACbGsyfYi7kY3Gg834PYS23QsWxSlPlM--ADmK9FwgK69iVXxXzyI5EXmnQWw2a8bljB3wqjgBzo0GvewsLJAf2SEBAjtQ0F3kleLmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edcdd5b47.mp4?token=ZDJz8jaCN6KhiBhiuGFZ01gnL4oBR89kPD9k0-Hno1NVSXlD_zb-wkoHyIHwFHvJPL-oGY8WJ-XqjeZS2qYQGQ-MyiRtEwPNiNmLHIvj0YAO9uR2U65rD6kOA8u1RRgQkqHE3yy-oa07bpsdonygcnSkzlBPFafrgyUPp43lz55UloZeepXXgBdI90FHB8A0MRNfke8YNyVkE3M5wFD6GOZYf5NHqk9SAEWgp-_k61KlQ7tACbGsyfYi7kY3Gg834PYS23QsWxSlPlM--ADmK9FwgK69iVXxXzyI5EXmnQWw2a8bljB3wqjgBzo0GvewsLJAf2SEBAjtQ0F3kleLmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت گل کیلیان امیاپه به مالاگا در بازی روز گذشته به گل دیدنی CR7 به یووه در سال 2017
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28777" target="_blank">📅 08:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28776">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=LFj4lZwTpKuEZx-u7gCC1CYCvQu4jvGNPSgO7xlOCUb0isqmnbPemgduULidS6luym2-6QzryIb9CUORvgW1reCZZi0QMDNDouG-uyP9dHgvZLxDrTIShOrgz72YoeMEy9AklqvOMgd-5v0JXtdVuRDBQOLgkONelc_138YvITzlvwRfnCYHz0KET1Uv6LNhtmyD1eILI2LkzNjfNExcsvoxos-l0zwys3GNEX_oVqO1gjQnDF8XS9Y4xjTuucDje80kjUNB9rO9jvlOuIKYYvulq4O_jSHXVIviQENnfls1GkQg_Z4WvXxSqrGLDU78athLHRTg_nLalQOjc1C20A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=LFj4lZwTpKuEZx-u7gCC1CYCvQu4jvGNPSgO7xlOCUb0isqmnbPemgduULidS6luym2-6QzryIb9CUORvgW1reCZZi0QMDNDouG-uyP9dHgvZLxDrTIShOrgz72YoeMEy9AklqvOMgd-5v0JXtdVuRDBQOLgkONelc_138YvITzlvwRfnCYHz0KET1Uv6LNhtmyD1eILI2LkzNjfNExcsvoxos-l0zwys3GNEX_oVqO1gjQnDF8XS9Y4xjTuucDje80kjUNB9rO9jvlOuIKYYvulq4O_jSHXVIviQENnfls1GkQg_Z4WvXxSqrGLDU78athLHRTg_nLalQOjc1C20A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌بسیارزیباوارزشمند ازهیجان و استرس مادر برای پسرش حین کشتی گرفتن او در جشنواره کشتی امید سازان المپیک 2032. عالی بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28776" target="_blank">📅 01:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28774">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5sC7aS2LDyBfLFMu_YuKxtk_cdwMAFHxhOcKXT1huKtqGR7vJAMjbt1OdfYVHcC4h-YPICY6f9jajBUwOOqXhhA5yunaMZrRKBOEYnxMit5tl-2yJF66yPDQq_K3Pnf6IgfTOX_MgVG8yFc3KCN8GeE0xAa6yrBANXqzu2C_ntsiEXsUry8Zne26fi-ApSE8JZO7zwvhDjXLm2WbMkTT0HUGhzWLw1Any4G55EuIZo3mLfNXleLEFdojmUDxPQlHivbgj9DdPD89gAbEe3TUKRZ56uXGcLhIi0y-jNEozlZOCApkcpQOJbBCw7B8ss32ZB1Hj68-79kbJUZhEra4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28774" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28773">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJf-KnV_a8GiI82ZKYcrgPxtUReqZMRi0MrvIiK6X9rEIW_isxUiKjV99iymvTuxc9ldRyYjqT6BP4vXTt67VW6GjIAUXp-PEhMLlk-TLWsoXMXJ6R2x_ecRphWwvjTfJSjcLsWy07ngQPrDMSzdKSTSjtUj0dMubEYJ_c1OAd1zXoWVWyTgBzjFiZ8Oer8y7hYprWcHfukqqySdkD3VUGLiOPRDdzUBCXObD0iOCQoLByTq_vm2Wr5YUY1zPS8nuFRHee1E234s-0oMjnmWYPYmNa7WFJWR2dvpS6qj0YdZPVM2YMHhOFW8NUZ51cnwzbIbrlGs9VshpIb1qdRWYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛دوئل‌شاگردان آرتتا و امری در ویلاپارک و جدال کاتالان‌ها مقابل رایو وایکانو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28773" target="_blank">📅 00:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28772">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdGCbEreU7dzSnATM90JJAP4m9dLd1ikPWKIpSgpFgY_bSq_O-BXGyndBfJuZ-bJiuvT-MixCT93q1mub2VYJ43oFgpHCkKquxS6jOnMRSmmRikF75rAH9CEJoQFCbShPpFYrb4-4QxTzGIYLopYzSQuwUNDk6ddBCz20am98nssqPaPLrhpkVpXYiQMlT2BcKg9FtsExgI9p-AozWQOPR1O_mudIJn1j1p4BKOx5teq3txgFoSr6ipz2hidQlRccRBmtabg1l_sjw077TCeMUAcApnZkAC2NWEym_ypDLt6l9hSzFFpe2hdPySXdkZbSmm-Ov0zegHI6VyROVCZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
از آتش‌بازی لئو مسی در MLS تا برد دلچسب یونایتدی‌ها مقابل ایپسویچ با هتریک برونو و ورژن آماده کهکشانی‌ها با ژوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28772" target="_blank">📅 00:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28771">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOiZvKMgMXltertVmkqiLX-ZDS8X-Ld2qQEItvSBJkj18vrNMZL8Ci3c1_9UzL4Rj9bc7kywkW9ovZ5bJZtzYbcsZD0GoLTX8mb70acJoLJrV_CroCRqGJMUaGdlrlNRSHvJtz5-pPE2urXWZuTv9wRFGggE8XiAx-2-j8kJbb9vGU96djs2gn97AgavdwP5ZIAUAWdAqf9inb5Afb7l9bGcLwFJGm74PI2iVPc0GWCgeussMjulL2oj-hzCuKxVji4gQ-T6Pf0P6jUrIeZkxTXf76RUnJuZFlZnVHOjoz5s8VhW_HKh1DI6iTJDBDTfJdwRC0wOS8Zue_AEL1TXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28771" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28769">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM7U-yK15UvpHNh4AKCw2A2002iN9uHBPRIVTe9FJ9ly8Daxjax8ert01NWYLOX_UVep0AEuhMHzwbQpP6Fj1rGBcBPrdIIpt0nMvPpcJ9Lio7zjavMdvVKfEAFI9l9JbnajJX8CXPvZefnCFVL2x132564KXNlzMVyKttg2Z2q4z8qLgef02jzXUTFLXgUUSSvm35_cMArMWFTs_1EgOyEe07VOAhFUCM_sNAynOGCw3J7mHAG03u7JKaNtaSVVQbxt1Oh6LrsDK1dS-JWg5T72df34j74bw40hNUimz2hnyaRXPw6HQ17co34lBN0nQGIlnErO9sd7z98vKt5DTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔵
سوپرگل‌استثنایی و برگ‌ریزون هاکان چالهان اوغلو در بازی امشب اینترمیلان در هفته اول سری‌‌آ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28769" target="_blank">📅 00:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28768">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKz90Y91NL4PLvibcMqf0MZlDU-BXm8zVu4mJbs_HE-PlujfmduFUaw8EcONMWpn896BnIUymfugDJeOEctfqG0vmfEc_1E4ICtbv0JDK3e38zDPjthI3MQtOJIaO1lPZpZPKHMqyX2E5yxAPwrv4GXrJNDN7Fo9Sn12RT_oXYCwDhI37ohTROEjLYUn7Yu6qnQfFIKQjAzhkaxd60Sk8CE3cRZ2CX4V-1HD8OJ2I86_je-c3tbA8HUHlVNr8qzTEZ9CLJgY0gI9SgLyj6At2jk0jVO71fwc-IN9dWIf8ulNwrl_XIdRzwjDROFlgJ7S-ui0PqEV7VnxmerA3kEpEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مصدومیت‌جدید مهدی ترابی ستاره 32 ساله تراکتور مشکوک به پارگی رباط صلیبیه و به احتمال زیاد ترابی 8 الی 10 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28768" target="_blank">📅 00:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28767">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyawyOc9z5fTGaWvRsgYv7-4dhzeNQYVKUgXVQljKmvF9-4Nz9zb1xSpVMxDb_62yb7JsM9C0_3z-oEMBKI0ZM4rQWs7X5cqeWQKY1Ca6_FskiFCcr_bCJuEMclWEP46Q3pUaWm4hSzae3WnPWhFJ3n4BuyvAmH5xox7oYhCZgAXmJrSCahBW50VYJYgX9J-OCF8rNStpmtnU_l06tvRXBIMIjvnChwtpAbdHSUEcBK9Rbh1niJfntqAAbdwkJ3nn3IL7A_ZXttwx6HsA4uYewUhxsdXuzD_kw5IjA5t08mU-FhuYxSxHijU0CyWcIg1UEmvslWb34amI-McZmedmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هلدینگ‌خلیج‌فارس و بانک شهر پاداش ویژه و میلیارد برای بازیکنان دو تیم درصورت پیروزی در شهراورد حساس و حیاتی پیش‌رو تعیین کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28767" target="_blank">📅 23:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28766">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-Tk2c_nMJFKforT4LZFsgqb7iDYhMNWbeLlDNVr_4ljrWJ8_KzZfg6V4s-5oSvm0pqhKdTOHdERI3wtk8J26dFBcDjQ_GZkSSZJaUnXqO258gKnaUDCn11GsDsLZr1Ywjy3KGGTeYQXKH_CgWoNITKMUVL5LCx6asDfVQvUw95LmW55DJoIcT3x1zMCQdDZhLdEpat84mfhGZPB-3eEZ6FgYrl81xD2G01stLca1fVrUpQCHsZ0CDi0afiVEu2FWui_O0uUWw4KRlTELLRWQ1cN1sV8VDyAR_7qCdR9iif59ODf7LbfHwmDhhmA3vKSJqO0ncDJXBXi0-osLcO9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
گل‌ های دیدار دیدنی و فوق العاده امشب دو تیم منچستریونایتد
🆚
ایپسویچ درهفته دوم لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28766" target="_blank">📅 23:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28765">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-7QgCh0puwaODKWcMbte45vtARJwMhGfNlHIbnwxmM6UbH_sOHQp21TQcXMmPTuNiFlUa9ann533zf3ANCDSO52_PXCsxEzSaaaObNFR3RFxQ_uSTN4F6v-47_m2KG2-0W-fJpKFZLpgVNEmmGWHZ54Aj6gTPGVxGHmlRdCdA8wvk-ffnIDgo1AHq-t-2-BIzfC5pWtiNdmDxO0T8OA2dh3ZaeRJFq1gDhYZ2voIMFnoNQCKhHm-o5FEcwjmR2HzJZ9_KbjGRkxafWmPVrrnCvqZAukydAzs7tgITfWXUEK8QVarnhv1okplzpwdrt6G0j3ULyGOgunEoqXAdt9zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ امیر عابدزاده دروازه‌بان33ساله سابق تیم‌ملی به نزدیکان‌ خود در تراکتور گفته درصورتیکه جواد نکونام سرمربی پرشورها از او بخواهد حاضره درصورت‌جدایی‌علیرضا بیرانوند راهی تراکتور شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28765" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28764">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwz9IQqDPFrqLuvFL585slubPFVlHQJzXItyBnvdQap2weCe8fDgrYfsxuJ1V2uDE2jzcw-afWHHwXtmJJjeIhLLvrUv1wLEdQoQF3py3ytZEIwwqWml3XR9eSC1vHVZxrXKmrP6tk4MdUSnQnxLs7oMzCXAom5syi2EkKRGstI85ikzrsX_lFcyyyRmum3B9jaW4UiKfpg4zG-6m34eUtygSfz13jwibkSSNB5ppeDYG6OxUjOV2B1dLl8a9kR46uWyX9FiQq2l2oWg_gl9ut02hV_a89cLj9Yl5Df7lwzMsIXP4hwycNLmhuXyI8vgxwiG3st9mNPWkQIomk4Qtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28764" target="_blank">📅 23:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28763">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c007350.mp4?token=FXKWGHUj9zZnHdquqzwhG-IFX5pziWRRp_91iqh3ACkgRQ3q4wZaGF-QcMoWyi8QYKhkX8IqkhHISXJaRymzSLPqt1lSki1mZnPqlJQDgIGesd0BwBJwPl9vkCzRNAG6LhVKGK25AVYxxwLaS0b6hqeP1BySt1RNdprfHSFLvMa1hr6YY3BVX7-R2-32H3rniReuwZz8oBLFWnXq77PYAcdME5hxXPQZr7viKVPg4XXHeapiLjs4C8iLF9BrwPcbdw3c9NFn5rtoeUVTbSeo7vMqysxDFthP1S8V6QildpNdp73wtPG2mObyb8CuSvzb2Y_t9JRTJ_P6wjgeyVaH8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c007350.mp4?token=FXKWGHUj9zZnHdquqzwhG-IFX5pziWRRp_91iqh3ACkgRQ3q4wZaGF-QcMoWyi8QYKhkX8IqkhHISXJaRymzSLPqt1lSki1mZnPqlJQDgIGesd0BwBJwPl9vkCzRNAG6LhVKGK25AVYxxwLaS0b6hqeP1BySt1RNdprfHSFLvMa1hr6YY3BVX7-R2-32H3rniReuwZz8oBLFWnXq77PYAcdME5hxXPQZr7viKVPg4XXHeapiLjs4C8iLF9BrwPcbdw3c9NFn5rtoeUVTbSeo7vMqysxDFthP1S8V6QildpNdp73wtPG2mObyb8CuSvzb2Y_t9JRTJ_P6wjgeyVaH8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گلزنی‌دوباره اللهیار صیادمنش برای لخ پوزنان این بار در بازی امشب این تیم مقابل تیم کلاکسویک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28763" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28762">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZozekD2U_nOdtsuXxScf7Nq9Sl2AWtlXXFFe4w59eqlOhaPGmU6HAP5t9aiB4itTS-rYTLDh6lyAJKNjqW1wt186WP_ZBMPPSPRsAEcdneKRzqP_INcRaxXbIWtf6AlPGReCZGcW3Qpi25r4FLqrX_t_M7drXgNo6BCJg58YxiqE2Wg2SqGg9_2f6-G5BUkNVrmwCuUXCh9tgmm-FXW-CwAkaFGSE5wT0X-XCz_B-RLMlFVZk79cmerrxqxaHejsspV1rXvoZdVWJ1AOJG-SxQXI9BZpFdngCp02VEksEMVTFDSiyek4Rojr8ceZQty2_de7y84LVblibF0gKov1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
درفاصله سه روز تا شهرآورد؛ کوپال ناظمی اصلی‌ ترین‌ گزینه قضاوت تقابل حساس و مهم یازده شهریور ماه استقلال
🆚
پرسپولیس است و اگراتفاق خاصی‌رخ‌ندهد ناظمی این دیدار روسوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28762" target="_blank">📅 22:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28761">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEvc-vK_0yXzEhMkMHJ5gkp9rlehOeG3aB88bNI-aDH0Clf_yMaIPmGBWEYZQYoEK2VTp2OzDeFyCglx-WhXlvYzuw-foziaveJqZqBnfUJjPvLOHikm6SwUZWmUGVdrC64zyZdotCJDlRi6wfUDUaAwlUlV2IgRi-SNG75bxaxfWl6_j9UG6ZEubny8GuDvGQKRRo2whY_4JPksWTocHuqNRBK5sEBEm_Pez12-puf6NNmysYLvDae83-NX2UtlEaXPX3yQh5L_f47Gtq-7vytBRWqdt0h5wxZAQa01xQQHVpLxwsP-P9iwg-Q9BoJVbcRjkevOuviG1us11DJXAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28761" target="_blank">📅 22:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28760">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b5db2489.mp4?token=Yx1Tj-RBXxShWOQJm0sSAUdE2biG8VdHr0hRiGGUwsHgZme9JKshK33KJfriEsDQNb1xmMEsaBbwyaFwavkrk4AC4m_7dzVTL_OVSy_zabDndV1sRuLon2g5VC4KVGuV6NA4ukJdiltbTZT6dVQXg65QMfczWEz_EOv0RnjEAWJiOcnOiJdThNrdEMELvNv1ihwcP-rEuKiIiBn1baBY3TCi0AKeP7RKiiF7X68B79G6st1-b9aQngkN38NYjuOzEXxTxAVcafzjTMviJ2JX5h-sBZ2mdW7Qv4sXERsVgBE7YjQAfVdHDXlMXpVLAhUAYn58PTxa8Ht4_ARca6KQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b5db2489.mp4?token=Yx1Tj-RBXxShWOQJm0sSAUdE2biG8VdHr0hRiGGUwsHgZme9JKshK33KJfriEsDQNb1xmMEsaBbwyaFwavkrk4AC4m_7dzVTL_OVSy_zabDndV1sRuLon2g5VC4KVGuV6NA4ukJdiltbTZT6dVQXg65QMfczWEz_EOv0RnjEAWJiOcnOiJdThNrdEMELvNv1ihwcP-rEuKiIiBn1baBY3TCi0AKeP7RKiiF7X68B79G6st1-b9aQngkN38NYjuOzEXxTxAVcafzjTMviJ2JX5h-sBZ2mdW7Qv4sXERsVgBE7YjQAfVdHDXlMXpVLAhUAYn58PTxa8Ht4_ARca6KQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
هواداران چلسی یه ویدیو دو دیقه از عملکرد سانچز در فصل اخیر لیگ‌جزیره ساختن فقط آهنگش رو از ثانیه ۳۰ به بعد گوش بدیم. این چه سمی بود:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28760" target="_blank">📅 22:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28759">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzR94-pLFAPbDJru2jS0KzudidfrYQox37B1Ti6YRLupvt5yNRSpFENpfCa_obZp1kdF3gMP29l11CWgyzFkhoS4BZxAZuLV-QwTU_aps3tW3p_4Uh4AyXCAwUoyIp6JcfaGOqV_6E2VYwXzCwpDYf9TGNY2V5YgvfOh48E0pYEkfbS4OXB4a1Zed9HPJIvk4peX3tyJgwl-rE3IXu86MUQOkx6Tc-tRwaYxxrt8R8V7vZHTvRPfbke4JZV2gzJLUBELzo4LjIQiJvfCnhhp-Dd-f6MLB_dmZHrhxNv9NncVx8GElP7OTqVo0DZzA27jrgWpFDTEtO1lnxH6Ko1tNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های دیدار امشب دو تیم رئال مادرید - مالاگا درهفته‌سوم‌لالیگا؛درخشش فوق العاده جود بلینگهام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28759" target="_blank">📅 21:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28758">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUmvdivHkyQ5V0PkOOVojiPgv7ecc-YSDmUmMtuYyxTGrrnVWKX_DpJoAJ_4PeBj6Q3NmIHl3y5SU9BZjzwB9JaeJR_nbtRTXtccaGb-GjEAO330773FlOP77hemOQadk_Wzx_8U0zCIwvDC2W-z2ll9jvU7r8YExZ7NWSSKe6qJlGoEyWe6xQ1KcrbF3XqxxNJnnOtVriqO2YV15Fg7Sd7TIU7p8nFtemhVpDTdA029IAwhHf1_8dQyIJRmNyRbjNn7rUuPKhcg3vBLdCuE5v5zGqL4muLHPNOtKui3YRfxmOfyUsElnVWvzdJCLYq3JZX8AJ63uCXENBT8eSI91A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28758" target="_blank">📅 21:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28757">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3f6e0903.mp4?token=dEcmmQNPaqYXrkeq1zgr4MqNTS2O5L9zKGqcptxWcZluxMLlJZ7g5hq37OXULMtSYxCW_J2UL7HEPQsYLrZXhq6OcYDrW1mKYCsq5km0auQI3Ht3FfuRYMncL-tA89osVq2wuTqej50jyuMmebME7T4kK0arayJCIHekg8w7Dqi6eROFZByjDIvg3GSJCQTrxITSv1tatS14epAt6dZdjYTLdA8BxtdktUEZIBAeKDsoeIbAmsC78aU1D-8lTuKr8pRDAYsdO7lq2aWgKJysfQvx-eW7pLxe5xkUPJMgNrpCj3bdS9pjIgcauX5NZUDG6UAh_oqc05aO95liVR339kWU8BzwiMauOhavATDi42CY7mrN7MnJJZidmmLqEhm2znfldPi-Ri4185OTpF3JKyzM5Bl0gfzcdSzV4yz6-JIMCNbezZQTh2dARxtlCmoEHm9HRr5J_94o01FT0m8hh6kv2i3RduLKOFBotd40ESFBXCAzPItsU1psmrWQyUi_cvIjNAZFXoitDFOC5KrplZHo7QbbidXsJOhEMJSaHlTJeLf-xFfpBRsXxUoSL8mueVCZCkkGrJi3GaoDHki2ASAlfVNXmX2d2RcjlzUsSmvujn9DuMl0thYjJplvCqXyHJbYyxy74Q2I1_JXxe5JMZxMTLxkOepjRxDZbPi3vGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3f6e0903.mp4?token=dEcmmQNPaqYXrkeq1zgr4MqNTS2O5L9zKGqcptxWcZluxMLlJZ7g5hq37OXULMtSYxCW_J2UL7HEPQsYLrZXhq6OcYDrW1mKYCsq5km0auQI3Ht3FfuRYMncL-tA89osVq2wuTqej50jyuMmebME7T4kK0arayJCIHekg8w7Dqi6eROFZByjDIvg3GSJCQTrxITSv1tatS14epAt6dZdjYTLdA8BxtdktUEZIBAeKDsoeIbAmsC78aU1D-8lTuKr8pRDAYsdO7lq2aWgKJysfQvx-eW7pLxe5xkUPJMgNrpCj3bdS9pjIgcauX5NZUDG6UAh_oqc05aO95liVR339kWU8BzwiMauOhavATDi42CY7mrN7MnJJZidmmLqEhm2znfldPi-Ri4185OTpF3JKyzM5Bl0gfzcdSzV4yz6-JIMCNbezZQTh2dARxtlCmoEHm9HRr5J_94o01FT0m8hh6kv2i3RduLKOFBotd40ESFBXCAzPItsU1psmrWQyUi_cvIjNAZFXoitDFOC5KrplZHo7QbbidXsJOhEMJSaHlTJeLf-xFfpBRsXxUoSL8mueVCZCkkGrJi3GaoDHki2ASAlfVNXmX2d2RcjlzUsSmvujn9DuMl0thYjJplvCqXyHJbYyxy74Q2I1_JXxe5JMZxMTLxkOepjRxDZbPi3vGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌دوم‌لیگ‌جزیره؛ من یونایتد در اولترافورد با درخشش خیره کننده برونو فرناندز ستاره پرتغالی شیاطین سرخ پنج بر دو از سد ایپسویچ گذشت. فرناندز سه گل و یک پاس گل به ثبت رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28757" target="_blank">📅 21:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28756">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHXcgso9k2JMwPk6Ta9m6YACMSsxJ9exVaBdUeLrp0Z7BAI74qDBqdcVx3nz-WovHXTFkrdQRByIfbLp9JLOAlQq4MRKAdL0fuNQHFybAdUxVEmVBfTv8vXYexIjWNq8yWyhkn8hRAgShzbsWkS0FXZBymWDH7PZamEciQQ7hlB5eUubOIGTsceHzSJJK22RnaYwsCKk5IK4XtoiC6RObWua74-eUn4-e1rsOCbsJPmDDL9b-fzrzhN0WqQCMRhRwzJX6RJolhyGyZVkzcBGl06I6HmRawouz0ePqd4tPRvEEemOmqGvhW6LXW4ErZLrFcjXAuRyAFW8bQTyXBTndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌دوم‌لیگ‌جزیره؛
من یونایتد در اولترافورد با درخشش خیره کننده برونو فرناندز ستاره پرتغالی شیاطین سرخ پنج بر دو از سد ایپسویچ گذشت. فرناندز سه گل و یک پاس گل به ثبت رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28756" target="_blank">📅 20:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28755">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd133737.mp4?token=mn4rl0_yeIwOHupYZ3FVW7w-0ytwmbegYLxOst_iMJ41gp6e42_x4H30WoltXN4NQzbUW2ovfmIsK_OkF1mWz5OIYB8mqjDyFpff8T-W5qZU7_kPyYIbZsyZoDczvIETidoJ2DM07_JVL9LFuHhoqvVj6QfdNwzxekCfW2-4xhJC7zDO7DFSJvYPdzrMCEu-L1rJAbIwcdtuqYYnwnu8EeKTYqqgtNU6-S809aTyTw9mdwLocXtEVW87pILHWpeOEgNc_nTlqU-UdRDbFZn5rHbnPMXACtfSgMuAhoLpYPnf_l7rNoR0ZR41J_ibLrpzqr_oM7scIzWXFzmQUh11bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd133737.mp4?token=mn4rl0_yeIwOHupYZ3FVW7w-0ytwmbegYLxOst_iMJ41gp6e42_x4H30WoltXN4NQzbUW2ovfmIsK_OkF1mWz5OIYB8mqjDyFpff8T-W5qZU7_kPyYIbZsyZoDczvIETidoJ2DM07_JVL9LFuHhoqvVj6QfdNwzxekCfW2-4xhJC7zDO7DFSJvYPdzrMCEu-L1rJAbIwcdtuqYYnwnu8EeKTYqqgtNU6-S809aTyTw9mdwLocXtEVW87pILHWpeOEgNc_nTlqU-UdRDbFZn5rHbnPMXACtfSgMuAhoLpYPnf_l7rNoR0ZR41J_ibLrpzqr_oM7scIzWXFzmQUh11bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته سوم لالیگا؛ سومین پیروزی ارزشمند و پر گل شاگردان مورینیو درفصل‌جدید با درخشش جود بلینگهام و امباپه.
🇪🇸
رئال مادرید
4️⃣
-
0️⃣
مالاگا
🇪🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28755" target="_blank">📅 20:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28754">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8G0c-wWEPoRlMcz1sLe1iUYtzwNwxhWxGsThuDhOkP1pTtDXV1-1ARdguJSu1mqJC14F-391fnrRIwiru7yscnzbTrMwNA3V7-hb3EN-7BJmAPSaL0Ev4BzC_rKF5UlFGmD9KEUBDicaOGUvN947ezJxYbVDz_NId1hytYGpQ5-bSwHtuv_TtZkCRx0mLnc00s0VELXerpi_umUteitqgX8-CyVvXeuf_oOiNKdAKo0GY2XA-VP8ZDffr0xkhy5hTb3Z-7UafjZQxSZV6AnGadZyCV5yiq_7PFBBeJRxmbhJfTkDMl0NJ8PfYkQBgsK6iWa-Xl5TMsYu4_1kveedw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ دوست دختر جود بلینگهام ستاره رئالی‌ها تو ورزشگاه برنابئوعه و قراره بعد بازی دست جود روبگیره اون روآماده مسابقه بعدی کنه. جالبه از وقتی بلینگهام باایشون وارد رابطه شده جود عملکرد درخشانی درجام‌جهانی و باشگاه رئال مادرید داشته. امشب هم مقابل…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28754" target="_blank">📅 20:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28753">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGajTRUYExNGViGs-_kYRTBur18YOM2Y_n555S75kieGxZfMhv5rCDNR8iT4YM2oHYAMIW682AFV3Sorg5vhu7KTMLC8g6SeT3rq8gNLRfwdL0f-AvKXZLQKxd7T5560VwhbXmC0YRjQkFjpKJ8N6GiOXNLmIcRQcSY3YQr36D-gi5tidUUN32IFAonq-kfCMGqBL3LdchiXZ-B3T8n98HgcFM8Hp_H_vn1GVJJAd6Kqz5JPWtcMDMelj2wlSkSHdXf3ZBXsYhcPUHcVKUylrkcS6s7Ygk5fxNfzreTfdyk_gg7beTo0Akifc5PpMtEe3ft3YkjyxXrzpM_nuT-AVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوست دختر بلینگهام ستاره انگلیسی رئال مادرید و یکی از دلایل اوج گرفتن این ستاره در بازی‌های اخیر در مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28753" target="_blank">📅 20:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28752">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogJqN-imIax7xhnsEQUGDTjVr-nN5OP7I5Fs0-uMSs-eGJtzhLoIACH92u248uOYVArgtBwHfAWdAw1EvR0w3UJNtoxWw5juNjdctx0U9YfN-lVn_5PteLf6KTqcgwMA6OSjgaq9KNRJLRBFt-oV8lEFbgXqxslf0rlW1ZCJ24KGHJEYWVDpm9VqWeco5DIM8s6iciOstG3IIMcjo_W5QPosYcdsusNeawrG7mIr1F8aqHsfKU4enB71VmIN1mdnTJ_TQoPs3ImF9e1H9w1CRr2kno3BqFStHeJU9iFlren_edBQq2BV3k1RpBqZypp_V8MiQ2cf_mljvg7_PmlV5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ اولی واتکینز ستاره آستون ویلا با عقد قراردادی سه ساله به الهلال پیوست. عربستانی ها برای این انتقال 60 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28752" target="_blank">📅 20:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28751">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2zBjdpVabS1m-9Y-O4ciXmhW2UUwROg7YgtapX9uclM_wN-y8AwxoSNijD1jcCXQ5aKoF_c01xy3_UHy2T6NCzFQDsDQs29xwyQoycXENqmydZH91c2t3WFnhA-Me7abssqjrFanqQ8OJ-PfXOyMgPoH3PrbWL_Zt6jojKljhAbLiiQhPMB9_1qYJ9fDi0d8aeSWSukGkFwpkgvBuCPMNO5T0PnzDkLvR3foHpQRzRg-4YU9zXyAh_wNASMgg5UeJnhRnCa39hHDdNToQxRJyG4bkKzO9cVzfdpqhzwwveET6P-SmjMqDnL_2NwhwBc6hvSxAAkd6GpvPODrotjuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28751" target="_blank">📅 19:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28750">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3859b36e.mp4?token=P0cVhohO3q08IISBjseK6Pzw0bFznIwOV36Q3d9Z6Qnn6xBTgbxT7BxlEPz1uQYUPY85NLALHz5BzVQ1rR86V2W0s95AO5lUMyrxHg60WRBIasvr307mUYEwnMULDf8-A4FJhFBIQzlkuswra5DauN8Aut7KdfRVtU1AUf4qHjNpaczoWYYglo0yT8aN7KBPb42iOeMmvAUi6U70ohEewyWNvvR27cGqMqXOJpNk90BlIL_cDhp9lKDeWYAZoXUTfQhhLe7NGOKqnu-MGscybFMaNFQYwQCd-L9qa5jAmGm9rmnsNlYgA83GaCU_Qv9Cw3gfinDNt2bAGujhvS0iK7z2Sp6PA9fmV0RMs85MnAuW59KqOi6YejelXO3m_maHjHPiBwC-7qoiObfpY-wmalC7Y2tCi66qZDsBNF5jYZ12DziHs2h4hhzpkm2140M3JQA1gqQmII9ESDr13B69JI0UDzvSxnVJs-f3Uk9oUKInnME2GawUFlaoGUkMIUE3zTf3F-qOZV3OsRVBOA2CdtAUv6qBdIW28hHFcEgtVBhL8YJNxxXEaHTwdHvo6-GqXhYbUFcdUua02uQxj9d8E9uLtgmJU2qMByZkRO0IpE81oA3SovqMns43lRII543-HbTXac5rVM2SWvqAM8rJuQHQQULByhXU9mnkUvRLtH0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3859b36e.mp4?token=P0cVhohO3q08IISBjseK6Pzw0bFznIwOV36Q3d9Z6Qnn6xBTgbxT7BxlEPz1uQYUPY85NLALHz5BzVQ1rR86V2W0s95AO5lUMyrxHg60WRBIasvr307mUYEwnMULDf8-A4FJhFBIQzlkuswra5DauN8Aut7KdfRVtU1AUf4qHjNpaczoWYYglo0yT8aN7KBPb42iOeMmvAUi6U70ohEewyWNvvR27cGqMqXOJpNk90BlIL_cDhp9lKDeWYAZoXUTfQhhLe7NGOKqnu-MGscybFMaNFQYwQCd-L9qa5jAmGm9rmnsNlYgA83GaCU_Qv9Cw3gfinDNt2bAGujhvS0iK7z2Sp6PA9fmV0RMs85MnAuW59KqOi6YejelXO3m_maHjHPiBwC-7qoiObfpY-wmalC7Y2tCi66qZDsBNF5jYZ12DziHs2h4hhzpkm2140M3JQA1gqQmII9ESDr13B69JI0UDzvSxnVJs-f3Uk9oUKInnME2GawUFlaoGUkMIUE3zTf3F-qOZV3OsRVBOA2CdtAUv6qBdIW28hHFcEgtVBhL8YJNxxXEaHTwdHvo6-GqXhYbUFcdUua02uQxj9d8E9uLtgmJU2qMByZkRO0IpE81oA3SovqMns43lRII543-HbTXac5rVM2SWvqAM8rJuQHQQULByhXU9mnkUvRLtH0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم لیگ‌جزیره؛ برد ارزشمند شاگردان ژابی آلونسو در استمفوردبریچ در دیداری پرگل و تماشایی مقابل برایتون؛ چلسی بامالکیت‌توپ 25 درصدی این مسابقه خانگی رو از برایتون برد و رفت‌صدر جدول.
🔵
چلسی
4️⃣
-
3️⃣
برایتون
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28750" target="_blank">📅 19:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28749">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA3Quy4no9RKGD-wv2Ug5U2tIuH40gDsn5hThBUmT2uXbiGyGuZp0wac6JmTnLOghWij75JXQzqIc8Y5rhM37uug49XLfzamTCE1MMnM3LdT211P-_f9XmcrTFaHnmNK-jwKMb9K24aUdg06fVlt27rQC28WHziU7oEO5EusfFyLjeega-XT50Qdm0Ma8irJ9xNWJeOymT7b4JnAwW_0DI4-BiFBK5TArfQFS0qdra1DXiaBRSFFP1l196-qZFfCl7i6KbhpvYcYvUd6gi2pfpIC_STLBJPWGUN9pO8U_uv4A6l14fKuOSio8ThLMERv8fwm-1SR9878PwCJFrROVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب هفته سوم رقابت‌ های لیگ برتر بر اساس نمرات گرفته شده بازیکنان از سایت متریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28749" target="_blank">📅 19:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28748">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rh0cIdZwkZikCxLZtKVhsmx3DIWiVdk0Xqzqt29L6h4LWEM0gVRqWcDe8bxTajBK29Vddgr_WkPlRgsBroTFhHHA-5VLxXAgdwgrxgn0yR0mUElPyX7PzEKARDzsvluuT5pySsfOudQo1u4sUwzChs9OFTJrH_ngezFqKcbfzCqIcEMEB9_NL44wpjv2LycZvSlKcMqX9MVWNoLy3k2V7CvY9hQYzaWq90Ly_9ke3nWBhHKwPlhphz24HrUJ3KxZDa4sXWF0dWy0zpcmeCNLc6pvKzb0dF3jPFUkG0GqAL1buskkaDkovltkisRYZBgyA0CeD-82sVGo5GT9fnXSpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی: کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28748" target="_blank">📅 18:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28747">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCH28w2hs5SrXq43xMORPCt3KIc-urcWZbBCovjdz2Vv-EKe4WlzEC29A5Sl4LjqZPZjr9FCWP2tLfb1rVVyWlB-9KS--XF9F7rmY_Tps5qLPVMxAzm0AWeV28u5Zpe1Yh5N7lAL9FVmVe3u5CbyfJjo-fT0jbawqx2l4N-xHYfafwiIb7dLIAZn1MDTYl0PrVDfmkAzIxta07IZ9USw8_DX-1IjYW3ICjL3fwku_wTP-3KkqLFe1H0WUj8PR2HmLk0_ULB-aeVVi-zrVfV3FKCopnVPZB2P6ujdgpb1k6D9B2xVOQDsRbq06qw74rCf6wWa_StT0DaX_UVz8XoGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌جزیره؛
برد ارزشمند شاگردان ژابی آلونسو در استمفوردبریچ در دیداری پرگل و تماشایی مقابل برایتون؛ چلسی بامالکیت‌توپ 25 درصدی این مسابقه خانگی رو از برایتون برد و رفت‌صدر جدول.
🔵
چلسی
4️⃣
-
3️⃣
برایتون
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28747" target="_blank">📅 18:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28746">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad7e62a7d.mp4?token=jprW5aGDtzUBCbi9Low-OZ_TQgOHLGb4p9vZpXpCD3zWn8dRjoudzX3XhV6n5sT6D2XgpHpVspmLD5Fc7z6MxEwmpSmQ4kKn3gBOJpyfq3R7x2rXIjx8v0trL9zKaPMcNCM2A4jrx_rk_p0NeljQjWNdw_WmlcWGaxv7sPMTPry9escrJBx9v2CH77hRXi3ulivSLRuAEQLPKv2XK3JCrzQk5aH4epz29l5ChWqb7BKXV9SMEsRa5AuP4NuR-4N8bq3Yw2Q4bw6HyOVf-K837vfaZFk-B2TWk1PzeLRbSQps1KY9fB58kP8dE7CPPCbZTUSiTgwCXObcYypQESbJRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad7e62a7d.mp4?token=jprW5aGDtzUBCbi9Low-OZ_TQgOHLGb4p9vZpXpCD3zWn8dRjoudzX3XhV6n5sT6D2XgpHpVspmLD5Fc7z6MxEwmpSmQ4kKn3gBOJpyfq3R7x2rXIjx8v0trL9zKaPMcNCM2A4jrx_rk_p0NeljQjWNdw_WmlcWGaxv7sPMTPry9escrJBx9v2CH77hRXi3ulivSLRuAEQLPKv2XK3JCrzQk5aH4epz29l5ChWqb7BKXV9SMEsRa5AuP4NuR-4N8bq3Yw2Q4bw6HyOVf-K837vfaZFk-B2TWk1PzeLRbSQps1KY9fB58kP8dE7CPPCbZTUSiTgwCXObcYypQESbJRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28746" target="_blank">📅 18:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28745">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVBjYTQCWdLN_a-5LrYAO8N1yspqHyHlMYnbeEHXDRndwY9PS47cjSASXN1hX2JUmLwmAgSy8K1hGyos2i-p3y2o9T_KDiu9vdQVnipptQsf3aBpxSxCGe2PPvfiHMeT9YJWQquAmHRj9xy-QljC8s6ti47MRi2Qd5VpXH2DgRh3_YSEIx8db8TxH_AHWZxuojwvKfvhQvuyRhP-S1RwUtDG1H-6Pdt28-FM_v9Rylje_r6L-T3lQYHgFN5FsVzl1Q9pa__hVP072AJZZggI0-TtILZ-GPXMIfYUw1AzsM1NbKUqdIXgKO7P4qajV3UsOWh67MiXvrl30VyuDi3jVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باگلزنی دربازی امشب با ملوان؛ علیپور با گلزنی در بازی ملوان به رکورد تاریخی علی پروین رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28745" target="_blank">📅 18:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28744">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUrvvTAtPyYy6pzTzNrdZYyXPBciVWhPGn2HxuDX7D9BUteGcejhBzJsKAYhbkb-MeXoIiHl1nD6fKvgZwRjVHc1MjVmABOud71Fis22bxWJXb9P9zELzMJBEiqZiZ1xAgSdPWnzc-egpkzokjBKItATkCql_yxKTD1tTQUgVmGqlF_Vwp-TEFK7BNlmf32iasZ6aKKG-gku0d-l-I2DKroIhVVUO-WvIK4l9jMIB2-czr4aIWrzoPVOb3_3MbX5ZQBKAWmMLZa2rvqQWMOJ4OYlKXGtFFBLDDMJc6tQpsalXVVZJyu4t0xLrp6bJZjMQSbNzvAR-0Jac9mi31jfJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه‌تراکتوربدرخواست نکونام با عزیز گانیف هافبک دفاعی ملی پوش سابق البطائح امارات وارد مذاکره شده تا درصورت توافق نهایی با او قرار داد امضا کرد‌. گانیف در حال حاضر بازیکن آزاد بشمار می‌اید و مشکلی برای پیوستن به تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28744" target="_blank">📅 18:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28743">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Do58Sw5mQfHvm7IKAUSxzRHA81HClXffVTrCbWnYoGMSqJ56yq-FRznbQfLPDEskp8n4JFyQI123c89kY7PVz_8Zsk9d1AgS26G35zrZPAtKmJ9g2p7oPlj7GEy1ABrOvPkNk5b_tXMeWxW5y10bHpUNytN5Q0e-oPFNXDi7qQLuA2ot2SCn7R1tad-XaVjNlN5hADUcXZODLmkfHEi9ROIlac7R-3rlT3Eszs8YOyUWMhBo1ZkVnJk_CS03d9_7AiTyQ19gQxBprDnb5wWzxijStmgBqOEVeVo8Eo4BFyienlcQOf_gMZhYVw8_rJ5VXqWmoYz2OgesxH97QoWQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
مریم یکتایی دروازه‌بان‌شماره‌یک‌تیم‌ملی بانوان و گلر سابق باشگاه بشیکتاش با عقد قراردادی به مدت سه‌فصل رسما به تیم بانوان استقلال تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28743" target="_blank">📅 18:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28741">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o27DCE-2F_C119jkvi6NjG-ntYooK9lYOxrs2iqXOQISxMOobTr65AqD2VK9pM46EMosc_vI-5fC7oTU3r8nhKU2X8LMt2tuc2oDiTn8c7V26wSheZTZjDxq_9w6KPa3-GT_pbPYnOgmRcSRa-FrXduLhnsWjYMHbzAXZaHQUTZvSkienxWIX7zzQ5aSEkOMTS2jgNbcxU0SwVsKoP3uVFIWIHPE0d412Y_hxY-C1Yltcuo79Pp7O1BJ334bPaI_wOIjxOGDQu2Ws-Snvroc2zAdcRvjR4fss97cvmBgObdt02Lj69ereOEfqr6KGPWJGr0l4VqkYb61LpJLmUtrhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
؛شماتیک‌ترکیب رئال مادرید برای دیدار حساس‌مقابل مالاگا؛ ساعت 18:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28741" target="_blank">📅 17:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28740">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8lMpETPGdPrwM_mMtZ7lrn79sN09thzfGgJjVS8Z6zec-ilAezr-Yi2cQngKegkHFNu7p9tumWMqHuMDN_OPkAD-as6QkqAQUHqwwWRQG9DCv1NYHVs3Jk0bpvMhtsRvFE_9gGDNuiyMg56X-VGGZy1CWirFhmjUj9lXqIOwKwAeM-uJWlOYK8q2JHRAJdQjQUL9jYBLBRc6f_qvSbeROp7xb13F8009tV_Q2LfrxDQRsOP2cEfYCKzMpfCtPaig5-Y_fEpscxruTiG0k4NBRwga0xirAEO53E9JU0an24HsmeVVnc1McM5kE9RMZJd8ZyKCuNW3fYhbzJb216Ukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه حبیب‌فرعباسی درمسابقه این هفته مقابل پرسپولیس موفق به‌ثبت‌کلین‌شیت شود رکورد وحید طالبلو رو خواهد شکوند و به اولین دروازه بان تاریخ باشگاه استقلال تبدیل میشه که در پنج بازی ابتدایی فصل موفق به ثبت کلین شیت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28740" target="_blank">📅 17:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28739">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqIn5hiyfArkgCB5Vsxejpi3U40yng5FRCCUKgEfQo288kTR98yxhC8Vt222WW61Hk0ntanFjTuEs1VHcch6ankfomUIewOm9PHBD6mwN6y0ylW8p05Z9aAjBSvw-3tuOixBmHnFiy1fR26elbrXggoSw7YdGX1yClBSUmrJAbZhh1-6lvj1W9YGWNNM_6hM36xxDRHCNHFzPGgDGRIILWLFJ9hD9cCfQEQJ0V-3MjT-8APOuZ1Eq2LaJ2_FmnX8i1rsOkYZJ9Asvo2_qDykPWlTtv4kOVEP9-cXog92ixzO8JhXMMNqGOxOjV1umdJiO9unb5YTb6ZDZpJnmHiISA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردحبیب‌فرعباسی‌دروازه 28 ساله استقلال دراین فصل: 4 مسابقه، 4 کلین شیت، 0 گل خورده، 14 سیو در 4 مسابقه، نمره 7.7 از سایت متریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28739" target="_blank">📅 17:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28738">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgwsk8SyLDrUiJKFL-5_Gfaeuc3x07IuU41AY_d0ZYZdJTC2YEa_RMPDS9-IHHSK4fmVAJmEOkcoHI169chnA3m4aKRP1e-eHAohAiCzpccDbF6y_aiicTbB0YN769pHbSjtapK3ZuNnN6hUlM7FJwonFqYuBkML5OqozPaJmJr8LezRo0XpQW-TH1Qac-6WlJxcO8WBbQ2Otx0a0AR4QK7GWDyHmubJN65CcFdH7cGuUnAiVGfmcnKH-LrpUUPQfLC1_OOinH3lC5989ifkWg25E92zyNE5As6Ur18AN5xEGu4hPmvhV1ChVKA-IX6IXN1IuGJYEy0t8vvC0-rjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28738" target="_blank">📅 16:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28737">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkclXaU6VXoi2F0pL9Q8uLdl03BrfJMQL8Huo4PbzhXARuxGqxKC8RJfJk0h2Uf2FpBZW0KFxrGT_HUpqxdMvcpgc3jQFdPUFBmaVbRXYxbHdXauy_ef90lmEzmt1XRL6vMETl84WsTkIDUniXXD9x8P0LGK-L-doQ8oMQwZuf5T4_70sSPwR7lAlGUdoQahP_9xf5z5iRF6wzryTFY3yeLBwt1G6-LppSdjwn1YJHBUZEr24lnqDvHFHrC_zw-G7EZZ_ilkn7GFc20J0nHER_-7U7-l8wQu6EDj2rgPiymP4ONoRwBE-gNjpyGr0ylWtmgAq10rqhkMEF6qYVuBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#فوری؛ با اعلام فابریزیو رومانو؛ گابریل ژسوس مهاجم 29 ساله آرسنال با عقد قراردادی به بارسا پیوست. آرسنال موافقت خود را اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28737" target="_blank">📅 16:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28736">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksp27cvfiIhNzJ-Poq3vJxOIUVSBhuXgMrIoXQjzS82CXM1mxrb5dCOVIDEwBgBHWwHi6x44ZFps2jqgp3Cscn4TuIZNBG_iCfMPeE73ytchOtMHIhQyzFsx_t3lzGR9SILWp7EM38h8ihbZ2twLcq59IxbRBmXuTnX9URiBYpUBrbHftvs3SDCU8DaJkTO5bIDwTaNf7bOvXO_B7R3z8AGnon_-4ML5qFAdidgAdBQwcQMHCorkrHcXULN2B1DcXOHU0sQVUPG1Kpdh0vB1GyiSaDMoWIIK7yuegZWr-iBohlpybKENqfY8R-MruT25EC-OlRd925YGjIsF922ruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
فرناندو پولو خبرنگار اسپانیایی: بارسلونا مذاکرات خودرا با گابریل ژسوس مهاجم برزیلی تیم آرسنال آغاز کرده و میخواد درصورتیکه آلوارز جذب نشه گابریل ژسوس توپچی‌ها رو در واپسین ساعات نقل‌وانتقالات جذب کنه و شماره 9 آبی اناری‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28736" target="_blank">📅 16:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28735">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flndDPeuUbAD320OxgYz2ns6ag-ZUCZQvkucfnP_k5BsOqQckxnBrKYO5gvWE15IhbVx9-0PEVidbMmPP5-VEbjdg7nPAig59SwsbMyRjP0Bb4QaDGi1cUb1zfyyu4rhOg3aScfYbi3U-Sqs2zz_1wcwky27aDMcyoCYfio7PKKTF7pneEu76cqudUBz6-qrX6l1QMuLFcB0JEAPmoERb2l8zmIdH3ABMc5UrrTGBF5szG1k_nK79oXylkHK19mnRJt9et7eRPTy_p6ZoPcupkx6QgbNpQTipEEEvfgN8REcdxGU1U5U3EhI9tmhCco29cXyTQsxRPZHivmpb6pAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
فرناندو پولو خبرنگار اسپانیایی:
بارسلونا مذاکرات خودرا با گابریل ژسوس مهاجم برزیلی تیم آرسنال آغاز کرده و میخواد درصورتیکه آلوارز جذب نشه گابریل ژسوس توپچی‌ها رو در واپسین ساعات نقل‌وانتقالات جذب کنه و شماره 9 آبی اناری‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28735" target="_blank">📅 15:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28734">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwOk0UCWEEFSNZz3oxL1I2F4qwb-RdXAyC2gZgrlGdf8JC-ViKmXX6obOdzanfPujo5c6UNp5Ak5sQ6Fj-dNplUr3pgAZnB4olmtVjnfrWDxm59KrSecix8ZD7mKqQCDHsSu7qR67WkQsDt9LpKqFblZ5ERqguSQaeIvKhf4pQfjBU6B_C5bz7Mt3-RcoRDgyjIodWVOlZGiiepBxHWQpzGsb-_b1cnlWdc8RDtL-yqCUEBrHdpSvuIgT0d415FM0DNrTPf9F2F8IonfEHEra401EuhFMWLghNl68-0sdGzYArleMSyk6z6HNbhyYgcPtRkbbCdP_pTpWHUFRurOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی پرسپولیس در استانه دیدار با تراکتور: به جز تایم فیفادی به هیییچ عنوان بازیکنی به تیم ملی بزرگسالان و تیم امید نمیدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28734" target="_blank">📅 15:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28732">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jbe0Y_wkMhvE1QkJD3kwrx732KM22oDkNRy5-PLEOZqA1T3ImjgVt7mdHZff4GHaPCuQDFE9UuZ_mdXNC-_6WG4_Je3bBlUbV8h-yiyQZGta-WQ3XyY77elUNt7FWF2U5zbybxKRdwnhA0c8temBrY1S1hIBeBiRbjRMDKA6lDfBtoXK7qkBWA-80L6s8RYxhsVKypdYTX7jDV0K-ZWALk4_su92J7NpRPcAQeMzr2VN5X8TVDcI3LWhnjwd6G20-LJdOJhkxKaHDw_F_D0RIqlPqfEplDASHrnwjdvHc8T28ZBUYQZ7BN1UDprmFS6qzWNX-cP9hOxmUUSNHZGjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XkLA09WDwgQWQxgSVlkwVIqtl6g5Y0XmimarX4XrDFS1brPMCy43Xiyo44IAeGrrBozTbQHsce0IInU7mQTyhwDgJkIqBA2dxy1znS73POLnBaOZY5bDRvcgMjNmAnNM4UxkuPL96w9SxycDR-URfvmDZ-NcJdk6TS_oMGr4ynsSOfZzKizrbMFneRrJCNuT1Lb8S4gooXB1q7O_MxbBsGP9-zgJmrWSNMUV3EQ_43626_rvIXzeYcHPjzAyVz4tWJRl8uVnJBYuw7WrtOpqLibvDDtJAyoA4hivsRzbyjgc8X3Pwi5zf00WtWw7ZSR87d_YUfEhmbkVYde26KNF2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
بانوان هوادار حامی باشگاه ملوان انزلی که در تمام بازی ها برای حمایت به استادیوم میان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28732" target="_blank">📅 14:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28731">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eueq5HJ1Un0ORLx8u4_F4sdXadV9iPZEtg8LIBk8Hn2JMmUc40emrXHvQfioWE17ZTiqo3jr0zuFRnJla1S5X8CdpHi44HkEiC9bC93ZUSVK3unIHvTFTXv8mQT060vyyKMEh_U5c0EeL7mBilzgLMVn6wz-11Vj55tJ8Q7Z7nsRmh8ahwm4R0Zc1ULttP9KrJx0Se2ykoPp7T1JTsq6912r4T9ilaD4Z43EggCl2fKWURAFIuj4i-a8Dh5_1u3wLXJJs_oGDT1nFWVBT_MGQV3DZZbRF1jwPELxxv9bu-Nd6F0X4ntHOEDIuVXRx6Xdgo9ukAzUqAqSJBBymqxbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌انواع‌کنسول PS5 درایران؛
PS5 PRO که بهمن ماه 40 میلیون بود شده 251 میلیون تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28731" target="_blank">📅 14:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28730">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayBWrCvzqaRRfFAsAg2CUTSe-3SYhPqmpPIQsYT4divPkvaWNjKInQt38hwxJHUxGxEUoBxKbAYjYtLse4vl3xvoH8kODmYz7TjC-WTN5-_VEwdiqCVvSv4qT95cMCfBrCUlJdyqGJMWMlF2LOsR3z9TyYsjL_cB_rh44hPikhTUBpSGACeob4UA8ctYrqyS4cu75NvXPwT81NmEumfgKuaY4TU7j21HmySU1KORNqKFGvH2YmOxvECn5MOqS5QyfK7YOImW_ZggJ9HIbL5ogXXpNXNCywrsECGw2ULmVfzKvwOIrViMcd6etCz-lxjacSd_qR4c_fcm3m34K1DECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
مریم یکتایی دروازه‌بان‌شماره‌یک‌تیم‌ملی بانوان و گلر سابق باشگاه بشیکتاش با عقد قراردادی به مدت سه‌فصل رسما به تیم بانوان استقلال تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28730" target="_blank">📅 14:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28729">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9bmql5f-uztczo13DAvfaLM92j1fckVYTH-vt_dPzLaeR7IomPIXOsxs1hl0xZJEbH-HqEm13AJOzGs0ES-1YIvs76sZ9BeSYu6D_c_Ywx5qRKbx17Nu8dEsz5wP79Cf2hsDE3TCm48p6bwWZoMiTAATNQGJcjyzimWtGcfNLuYGUKWx9dVAI1WhwtHd1kSrIHS_PgThkJ8tZUuzqgNl-bPBuHgRdcvVGEWRPok6pwc6IZwsvbvLIuii3eyx8YGk9O08LQUNHfcRKH69lCasml6f8ng616kMFnkJUoNAjaQFdKMHXinKsiNhGizPD5AR28ApGwsvqUkRpbB09NujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از همسر عثمان‌دمبله درخصوص پوشش که هرجا میره ماسک میزنه‌پرسیدن برگشته گفته این یه عقیده مذهبیه و دوست‌‌ندارم‌‌چهره زیبایم رو جز عثمان کس دیگه‌ای ببینه. حتی کنار فامیلامون هم ماسک میزنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28729" target="_blank">📅 13:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28728">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520eadae82.mp4?token=YmYoEcklpUJW2Pe85aAIBZ314E-HwQk1OmQLNHrwXNMKId_iL4XD84qfaiZ1csL_4_3qToWUnDc7eb4xR7oVZ1fkLwm37nsPrFtymE-58Tqcv92NvatPF2OoHFBWh0DrqGvq8yL8JBqwOkJkPbGEWx39BKJ0JExolV0L9IlBx9SSfGXMzugZ1JUxMku7j5BhFcLp1M_oCeHNdt1M3Q1bw8KQbYnnN9_ndrSqVTbnMfhX2AE9bmUs0GJ-T8RTmtgeNacYx4yYpmLnqnQl2LWMFecG2aZ5cP8WDPch9rG7pvvODAclCMpPyx2tnVwOn10TS6gMr6NWjefR-pPafHE8TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520eadae82.mp4?token=YmYoEcklpUJW2Pe85aAIBZ314E-HwQk1OmQLNHrwXNMKId_iL4XD84qfaiZ1csL_4_3qToWUnDc7eb4xR7oVZ1fkLwm37nsPrFtymE-58Tqcv92NvatPF2OoHFBWh0DrqGvq8yL8JBqwOkJkPbGEWx39BKJ0JExolV0L9IlBx9SSfGXMzugZ1JUxMku7j5BhFcLp1M_oCeHNdt1M3Q1bw8KQbYnnN9_ndrSqVTbnMfhX2AE9bmUs0GJ-T8RTmtgeNacYx4yYpmLnqnQl2LWMFecG2aZ5cP8WDPch9rG7pvvODAclCMpPyx2tnVwOn10TS6gMr6NWjefR-pPafHE8TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعودپزشکیان‌درحضورجبلی‌رئیس صداوسیما:
دیگر تلویزیون نگاه نمیکنم وقتی من این نگاه را پیدا می‌کنم. ببین مردم چه نگاهی پیدا می‌کنند. هروقت تلویزیون رو میبینم اعصابم خورد می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28728" target="_blank">📅 13:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28726">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQu_q7g4PqXPT5BgIwjxO5EvpEQr8pUh0e4hJMfK0OxlD4_5cPPpYACfDcHLaiuHVU4EDtu5kdDxTINUjirNHGpPG8Ekp0ksM9PkAOP8shFjLLcf-ZpsHVIuRG7VPOgVaYUqU7GWu0s6y1xRef-VslTeM2lq8uqPO6OANOXtQC7ODVJ0vM9szFjFVFZjUvve_Pz_fKeADDd5GUjCWEQYQJRUlsU53e9KAr3JYSd9CFwKXtk4UXofJkOM_vtMDBju5_VymaASQTv1_Kfg2SJbGNWH9Af4N7CMfolfHBgtE2kicMZPMcecgxv-GrC4AdjOtJZcWrlL0GzgLRCLtFTFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
جوسکوهای ورزشگاه فولاد آرنا دربخش بانوان؛ هواداران بانوی فولاد بعد از سال‌ها بالاخره از فصل گذشته مجوز حضور در استادیوم‌ها رو گرفتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28726" target="_blank">📅 13:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28725">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📊
تمام گل‌های هفته چهارم رقابت‌های لیگ برتر جام خلیج فارس؛ سیزده‌گل‌زده در 9 مسابقه هفته چهارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28725" target="_blank">📅 12:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28724">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeBRLdXroUBwyyLYtvrOfD9BiAIrKd7lbnYdbamIxTRK3lB6Bub8iEuOrluoYPhM6ykIMqtx4VF8aT_rNpyNFAX4o-ARQVm9_nuUd3YWb-A6oRdsGmlpZ_C551yBkQuCHrXHNhPAuvC2o8A9ILXZSgyTsBoj2thWiqE2ppmF3jK6jVgX3IyENzM8ngDle6UzAcpXVi0z3qSryL67vq6Bh7Db3nfRiK6p5H3MyZIgc0KB1Jm3MNxOUxU194-eQpYsI2XdguBexOtGaT0JioAOt6x1yYd8ewusgyhxk7TYmVcN0-NiH8lNkY6o5iGP9OY6hO6gOcfezjSM_4Mc2_WM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
درفاصله سه روز تا شهرآورد؛
کوپال ناظمی اصلی‌ ترین‌ گزینه قضاوت تقابل حساس و مهم یازده شهریور ماه استقلال
🆚
پرسپولیس است و اگراتفاق خاصی‌رخ‌ندهد ناظمی این دیدار روسوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28724" target="_blank">📅 12:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28723">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc627927f.mp4?token=QahsLb3v5vHyB5_PdkuS19sw3ulMItxTpAOATX-XUF64K7KsGiwwRrPxTKXIksQjzPKJDFIR27u32D50zLnRZjqfYhaqEVjLVY2xAdQsSLS3sf7CTqivEElAp-ObpVgEHOvjLjLQ2yCjO52iLIQR3IA9qQdc6CZSUgwFmcyA3_7kXK6xvfrQhqwCP5oNoAfEu-YcpYx05jrmaPVSsj_WV0TBS4_derB_vSs-33A_iczA6bSgDsC-BF7I4hMZC9ciIEeeXkoUgE5_jGlTkUpTCsxdG6sqER-0pauvJPWLmSTYVtCTBVty0Min_rCnx3H9ORS6gV8hSDj6miVryMOa1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc627927f.mp4?token=QahsLb3v5vHyB5_PdkuS19sw3ulMItxTpAOATX-XUF64K7KsGiwwRrPxTKXIksQjzPKJDFIR27u32D50zLnRZjqfYhaqEVjLVY2xAdQsSLS3sf7CTqivEElAp-ObpVgEHOvjLjLQ2yCjO52iLIQR3IA9qQdc6CZSUgwFmcyA3_7kXK6xvfrQhqwCP5oNoAfEu-YcpYx05jrmaPVSsj_WV0TBS4_derB_vSs-33A_iczA6bSgDsC-BF7I4hMZC9ciIEeeXkoUgE5_jGlTkUpTCsxdG6sqER-0pauvJPWLmSTYVtCTBVty0Min_rCnx3H9ORS6gV8hSDj6miVryMOa1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس‌جالب‌ازسریال قدیمی فصل دوم ساختن ایران و رفاقت باحال امین حیایی و محسن کیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28723" target="_blank">📅 12:03 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
