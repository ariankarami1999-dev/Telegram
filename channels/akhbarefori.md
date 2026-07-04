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
<img src="https://cdn4.telesco.pe/file/D_LKKWV7a9LL7VQdBcI-CRi0Xpl6zVcC4pni9CbKcYhlQtc3IGbh0uYZuUcKvASv-GwqjZvsD0GYeBiWPmu8bunj-a-AMZykpLbSbb3kzsM6KIylkTwVZ2lVt84gyC5setlLn3IJLqhFbad0PhyjHQcRlqjjhXvq4RCnEYVRPv7UInQ6MWHmqklUtalB0wnvX70FVI9_-QTcLCsRcihMpf-lt72bV8_6YjOWb9_CtTSMEVL6mw8-LbN-8FnXzoM9eUCi8KkfSvE2OVM1nEjRmlEwCrgt-KrDkKhrS6VLViS4fklY5Cy2GL-sPRy75Lj6MX8cAU3EV_hxFWLsflyk3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 22:37:13</div>
<hr>

<div class="tg-post" id="msg-666600">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f415f88f0.mp4?token=sVhpXXBLvXZtkxJWYDp71q5N6gZHewjzSxmkcsB1Y7jvirF9HW0YupYH_UCpaKEpzY56hvKE6JQ9KxZn8hZSJexO9T6hkgo22vdsigMh_6VYLVkrIvFwYsbCeFwpPW6z0jsaKWjHeVEyDRQI8-EGKMlkiQJUhMA0OlGlGgrxGT2yL95suxpG8pVajNKGf7ntbLszPpR8xmdwy6RgrbqKmz9t-orxEpvlZxLkp5aRLhmUyg4G1ClkwgDgxwGeFTvdquqUSIbDISVFowALnhwUVdhvSIXYzuoN_sLXa1L4PYXxyHVmSxf5-pDzZJfolLgyYtjqA1rmLl9NuuWY1-_crw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f415f88f0.mp4?token=sVhpXXBLvXZtkxJWYDp71q5N6gZHewjzSxmkcsB1Y7jvirF9HW0YupYH_UCpaKEpzY56hvKE6JQ9KxZn8hZSJexO9T6hkgo22vdsigMh_6VYLVkrIvFwYsbCeFwpPW6z0jsaKWjHeVEyDRQI8-EGKMlkiQJUhMA0OlGlGgrxGT2yL95suxpG8pVajNKGf7ntbLszPpR8xmdwy6RgrbqKmz9t-orxEpvlZxLkp5aRLhmUyg4G1ClkwgDgxwGeFTvdquqUSIbDISVFowALnhwUVdhvSIXYzuoN_sLXa1L4PYXxyHVmSxf5-pDzZJfolLgyYtjqA1rmLl9NuuWY1-_crw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراکش مقتدرانه نسخه کانادای میزبان را پیچید؛ گل سوم مراکش توسط سوفیان رحیمی در دقیقه ۸+۹۰
🇨🇦
0️⃣
🏆
3️⃣
🇲🇦
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
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/666600" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666599">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bl6k_n7vA0mLG05QUPBm4YeqEe0KUwavFYlZhmAtX4z5WKyI4nHcpyDesPmRF8gEvNAE1XtdMhUoPMJU6MpecUdc7Onp7JHENgCkHLeuy-v19EBtKvuSfDRnTNuYOtB2u2AtQEXytizZYK4BrOcO35SP2zYqS3uNd8d2JEY-jeNyObrheFKKu23q5bVf_iIc5Ags9qnBjwysOfX8n5BFSdG6DEsGwH2sDxp3vLlp8_mP2CRFQq_Rbq2ZXBiWpdim7yGivCG8EhsDNbro4N7waWS_TcIa4TLdIiLnDzCOvnDPBlefZq8QiTzdWUAsuPdm0xo0lLI74EbOQRLBcHn72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه‌حل امام برای خلاصی یافتن از ترس‌ها
🔹
امام عليه السلام مى‌فرمايد: «هنگامى كه از چيزى مى‌ترسى خود را در آن بيفكن؛ زیرا سختى پرهيز از آن از آنچه مى‌ترسى بيشتر است». ترس اغلب زاییدهٔ خیال است. انسان تا وقتی از چیزی فرار می‌کند در اضطراب می‌ماند؛ اما وقتی…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/666599" target="_blank">📅 22:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666598">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
یدیعوت آحارونوت به نقل از منابع اسرائیلی: تاکنون هیچ‌گونه ترتیبی برای برگزاری دیدار میان نتانیاهو و ترامپ انجام نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/666598" target="_blank">📅 22:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666597">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2-m97smM8CmAll730-yXQzspZyPvH-7h2ILaFDvSGQ95ZYt2A4kWk2xeLvncTtk3TVjlwsjTOLXaYp3cw1Uw0lzN8ooXxJ4_I4qLm_iub-lHN7BA6YhCJRuSrhOumdEjvy_oc4ftKPTfzwcYMqYg6yjonxTHEKyKBiXfCbTWdY5Zj6dJR9TGtj1LgU28scYWtRep0cl8aHNOo-QUQEQoyEhFOSCogVmmouzGD4ZtL8Fg4F91tJUo1l9kVRlDPXimI7H4nObdXM0TYQgLa_V_wXQCR1e3xPlPU5qF4rD6-YefdAa9cSUyof48rma2zmqKMu2Vd3wJ6kzmaOY4Z-IVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدردانی عراقچی از نمایندگان کشورهای شرکت‌کننده در مراسم بزرگداشت رهبر شهید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/666597" target="_blank">📅 22:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666596">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
سخنگوی ستاد بدرقه: مراسم وداع با پیکر رهبر شهید انقلاب امشب تا نماز صبح ادامه پیدا خواهد کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/666596" target="_blank">📅 22:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666594">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
شب نورانی مصلای در هنگام مداحی حسین طاهری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/akhbarefori/666594" target="_blank">📅 22:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666593">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c52c1e47d.mp4?token=QLSjloMXPyZ4gyuFX5myHr_JJbUNuwTMJxRt5uFGawEhUY_qN7XIKCO1YuRY9JXdPYd4Puw-dv7Xm4M4U8jj2r3po67uGHdsH1hkM8qlzDP0M_Yf1J60b3RRahaE9kgG7g_fxj5TouOwpmjfrTZ6_arC8f2wsJMKtcR9SkjadRB4WE5lGPOssQK7SqebAmnXd8CJ3BPk0e9J7e9_CbDA7xn9Cld2awyvwOzhDXr11YAH0_m1SzNjJU3NAGxVR7eJELZ-q_Et3iuTvJVnrIqp6olrWYd6hv0GnMhnBNcpFiZqMrBjYb1Ag8lAZ94t9zfBR4XQgjFEMBPPabiui2F3SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c52c1e47d.mp4?token=QLSjloMXPyZ4gyuFX5myHr_JJbUNuwTMJxRt5uFGawEhUY_qN7XIKCO1YuRY9JXdPYd4Puw-dv7Xm4M4U8jj2r3po67uGHdsH1hkM8qlzDP0M_Yf1J60b3RRahaE9kgG7g_fxj5TouOwpmjfrTZ6_arC8f2wsJMKtcR9SkjadRB4WE5lGPOssQK7SqebAmnXd8CJ3BPk0e9J7e9_CbDA7xn9Cld2awyvwOzhDXr11YAH0_m1SzNjJU3NAGxVR7eJELZ-q_Et3iuTvJVnrIqp6olrWYd6hv0GnMhnBNcpFiZqMrBjYb1Ag8lAZ94t9zfBR4XQgjFEMBPPabiui2F3SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضد حملۀ برق‌آسا
،
گل دوم مراکش به کانادا توسط اوناحی
🇨🇦
0️⃣
🏆
2️⃣
🇲🇦
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
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/akhbarefori/666593" target="_blank">📅 22:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666592">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca5Y5b10rQWGIG2rPbt2hTgotktq5RWPozw8Huk6wwyYuepimphsz1LZjEu-9UlTRXT2W0VHm9-mb5HqEtf7N9LaSOY6Cfc9kl5nFx0EPxIOR6Ect0fKBC7w1Sfqp_VtJnQm6moFQ9TchMDQawYOlQuKwF3tMd3S680ePjxjwaM6sCpKlty8i4NhAfd5-03KKqXSJg-P7Jxz5SwS8J7pSS_BLUX7HlJdFgrTiF1qVHXMLq4F-0323Ezt8VWLFjmDQHXCOuzf5LMTp_M5zv_GhLu_rKdZz1fqD9Oc8T5wG4a0oPWfemTYlNc4cfzVkhigAARGCF4zt0NcWYG-4BF7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/666592" target="_blank">📅 22:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666591">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36cc42a03c.mp4?token=KWRGteJBvAw2GaFDWR80ZxQnEI8I_B9qPeIEz0yLpCrTmQnVPxiHJovei-UlVgNLauB1yDo-1zdC4FVj48a7vUbPtWdFoSaLcUyB9qGAvQJzd25d0DYXjQ8hlCabwLGjcFS-1WIqyVEqNRdOHZrMQnAWHeuUz_dkm-PEDGg3EUGdoNcuFNEeQNq8p1zBQ88iJMpQ22LCt64yBcqpw2-F2VlppbLkB-F9a81J6gnE3p0P8Y2NnbiKAApenGD3sf4H_8a_z1-Gp0-SB5OfwBDJXOmsHC3icogKhpmjkt8U18aFCxBqLC6TfGgH7AzRmA15XcN8pcAyjWfyCxhu7aczjHMmGnL7EbvVv_YR6H90M9hIs9VgVvnNs8x_UY6bO_zdKoMYdWiy_qyIkFfQ1jIHNCq98c8n8-hEH_2w8LmGsgiyBbac96qBmxkeNxNKR56J_IogWQD5Qchh6zXFo9falCb6Bnltknm0Dfj4cFdip509JJtCTvYaywTNE7bMDOXORoIufVvG9TR4Hl7ng3R8DYK1x_GrPY9gXFIZugKCxdRGRngUH82qF5QHA6znInjh3ixviwPW6nT4UBdq-soKyZWoJYd69JTfy5-QjfHM5REnQVCbby5CgEKxoC_LnwlIPYmjPYmMX3SjD53ddhDaOWeej_H33uel5NLPBZ_cApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36cc42a03c.mp4?token=KWRGteJBvAw2GaFDWR80ZxQnEI8I_B9qPeIEz0yLpCrTmQnVPxiHJovei-UlVgNLauB1yDo-1zdC4FVj48a7vUbPtWdFoSaLcUyB9qGAvQJzd25d0DYXjQ8hlCabwLGjcFS-1WIqyVEqNRdOHZrMQnAWHeuUz_dkm-PEDGg3EUGdoNcuFNEeQNq8p1zBQ88iJMpQ22LCt64yBcqpw2-F2VlppbLkB-F9a81J6gnE3p0P8Y2NnbiKAApenGD3sf4H_8a_z1-Gp0-SB5OfwBDJXOmsHC3icogKhpmjkt8U18aFCxBqLC6TfGgH7AzRmA15XcN8pcAyjWfyCxhu7aczjHMmGnL7EbvVv_YR6H90M9hIs9VgVvnNs8x_UY6bO_zdKoMYdWiy_qyIkFfQ1jIHNCq98c8n8-hEH_2w8LmGsgiyBbac96qBmxkeNxNKR56J_IogWQD5Qchh6zXFo9falCb6Bnltknm0Dfj4cFdip509JJtCTvYaywTNE7bMDOXORoIufVvG9TR4Hl7ng3R8DYK1x_GrPY9gXFIZugKCxdRGRngUH82qF5QHA6znInjh3ixviwPW6nT4UBdq-soKyZWoJYd69JTfy5-QjfHM5REnQVCbby5CgEKxoC_LnwlIPYmjPYmMX3SjD53ddhDaOWeej_H33uel5NLPBZ_cApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به رهبر شهید ایران سلام / سایه سیدمجتبی مستدام
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/akhbarefori/666591" target="_blank">📅 22:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666590">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0764895667.mp4?token=GXh5oguN4VB61HgPXbMnKe2FGv9jg9wAxL1kIwO_ISz5A5nJJrVRy_V9SUAIJ1Y0A8q5uVyZ6t-jQUsDLM4C8rrA1ib37ayX-Vpez70xhXizmBYl7suEziiiGTOZIsH6PyzfRoAnKyZdJIhLbmAaLsc2_AB1ifNM7GZZb7v3Iq9hW5FkptzJLdHIcKKn5PEABLRF-dJTDSUlvDKJgUEYZGAdRXcDmQ-ikiHSfBp6Th_fyoGGWOnZUsenQbf9Al_7R7hpIO9Fho4TIUUHzEOd-e2cMbnzF-0agu3FJy47VaQBfezZhfE6IkcQZKJ1b4r4NeTCgj2Whf5FUKjIHdTksw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0764895667.mp4?token=GXh5oguN4VB61HgPXbMnKe2FGv9jg9wAxL1kIwO_ISz5A5nJJrVRy_V9SUAIJ1Y0A8q5uVyZ6t-jQUsDLM4C8rrA1ib37ayX-Vpez70xhXizmBYl7suEziiiGTOZIsH6PyzfRoAnKyZdJIhLbmAaLsc2_AB1ifNM7GZZb7v3Iq9hW5FkptzJLdHIcKKn5PEABLRF-dJTDSUlvDKJgUEYZGAdRXcDmQ-ikiHSfBp6Th_fyoGGWOnZUsenQbf9Al_7R7hpIO9Fho4TIUUHzEOd-e2cMbnzF-0agu3FJy47VaQBfezZhfE6IkcQZKJ1b4r4NeTCgj2Whf5FUKjIHdTksw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار تانکر سوخت در آمریکا
🔹
این انفجار حوالی ظهر به وقت محلی رخ داده و علت آن نقض فنی اعلام شده است.
🔹
این حادثه منجر به قطع برق چندین خانه در منطقه شد. پلیس از مردم خواست تا از ورود به این منطقه خودداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/666590" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666586">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UluqC2xGBrY9GmqIGeK2umximGchPreCgYgVc6NuTs2muz2oFHcYIbjrefD6gefLwsLz1cNuCGA-K9HLtS0nXirdk9nWKXIeZKmwwzqvmTDmy5kJ6dClTk5M85IhJLyBkBeISozT6OJY6GZfbCHiAHkACJ0UVH2_-WpfNsTJ9Ii31N1Ry-JGnlKnxnmQok0u-J5X3M-oZlhL6o7FbGRhbnXGTSe1sIJzKKfPo2OIaLhfTQ0lTgL-dGGb3gwKcd49BX9f8ujSxDhaqQam4k93ysPdF6WbcsZYxHoFllVH4ymviQx9fJaVG2I21D8xb9QlNuOkGICEzSYS-qYptgvEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lm2ud66OhaZlcPTB7cqR17Lmd9St0Z8HUYhJjFUhubJhS1cn_1S_mKVmFkznyrASCj656UBbmRXT0kJZWSAjwIGV6jr_hIvFZ8YGZy6e-fmcnHGOXPvXJnyhyABVJ33nXAOZmqwwOu6fTUU1tLCfsR_AMjsrNl34lxOIV2mGIt-lrA8mPSt4TmYaQBAH8ViJe6dVKhCV65BPYMTMhJvmhZUxgXo53JY1Ee_6W_rVLBQqICAjLU7YFYCtQwg2tf8CdQUqWosojLHOVopq5OTRYmjlNH2zdklphRKIQLAX4jLARkq6ScXREFLitniQdKo1JFhTo3e7SZW72G4x2jDRsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2XuSozGut7Xyb3v7ajrls7qs8VfMWOz8IucLL6yoPQqQA_Nl9jCUQft2238-lq6L60jh3MXZ6UWtRXB0MxenTPXe7hW2XkxObu2b7HN1komFwz0WPlE5fuCcqY6QiIUO2OiTITkzQLZwWBHKIJCWrZ9x970qNcdSK4u9uaTrtEuynwc4Pes9WXJmVUrbPzpbK0upR6aw56qfCtFAqxx0CQV6gVklXYHpE6tDsw6H5sP6INNBJmdUFaoL6OcDCKSr0l4Uyt5PBzbB19VDowl2dnGeI3BGjMcWK14dTXv014pydKN-o0LYUbG0YI4IFkpIW75pmwI0otW39zfb-Y9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D61d7ASC9n5WH6eX_Ccw9lVMIR-y1B7HHRvGX_bQLKbh6tCR6YVjXM6LZROJrcbf6B55CcY4x1iuPykmDf7DC01TdllTHwt9NXbTR-MVW5T8ROj-yW3pXDpb34Mj__tAlWbwcgaZo1Z_0bvguP0nYb9szA-6aGDe8qivoUxuuFqbFh2XPmbvylF0VwJB_4ITP1e_1t17vp10JlX-qeLY-AW6UaZWPLQh7wOEFwKOf1VrR24wMEQbH5B9---CR2S1SxsCOkj3hNLRdVLPwtzKzpfQHQKqYeXLpnHM6pjAeedRxaVKg7Jz6JQ1NoVKj7cDhFi1hQlAEfp5LJf5N5ISJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طرح‌هایی در راستای راه اندازی موج خونخواهی رهبر شهید
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/akhbarefori/666586" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666585">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4722481f4.mp4?token=NHH8c_u0NBfWch8ctqmyj0tdD8zc9bkoDb5NGKgaZWbAZyW3M-vJs7x8GVeGcwJd9B9WyqZ7ddT_VMY9IHOHDz_DFjOy4GBv2UDPWiGSvJ8wVB4lbXrZewKi4IJPPbnOScPhiBRUwh_n5sftVZRLJWnu6gKVe3cNmWy_-F983-G8UYN4OGFNryRTiRAtQJe0gogcfbtt8ds6wwxwTFutOUaiePnvcpf4S4-v5XXrN1nBykokg0YgpWGWiOnG18RZX0DvEqBtjOJrMBcl0nqjm3HJpJy0YU6QpG_doJbWl0CkImPnaiFEB5WAQVgs8M6cQBvqa8uRPKIWnQF03zv_xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4722481f4.mp4?token=NHH8c_u0NBfWch8ctqmyj0tdD8zc9bkoDb5NGKgaZWbAZyW3M-vJs7x8GVeGcwJd9B9WyqZ7ddT_VMY9IHOHDz_DFjOy4GBv2UDPWiGSvJ8wVB4lbXrZewKi4IJPPbnOScPhiBRUwh_n5sftVZRLJWnu6gKVe3cNmWy_-F983-G8UYN4OGFNryRTiRAtQJe0gogcfbtt8ds6wwxwTFutOUaiePnvcpf4S4-v5XXrN1nBykokg0YgpWGWiOnG18RZX0DvEqBtjOJrMBcl0nqjm3HJpJy0YU6QpG_doJbWl0CkImPnaiFEB5WAQVgs8M6cQBvqa8uRPKIWnQF03zv_xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جکسون هینکل، فعال رسانه‌ای مطرح آمریکایی: سید علی خامنه‌ای در مقابل هیولایی به نام آمریکا ایستاد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/666585" target="_blank">📅 22:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666584">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815c9ff5ee.mp4?token=nNyVOxqrVmI4oEwFvPQuSrvkJdWRZJI8QdEnW38PuGnXsNz5vyvo7ReuBOhDbPwjq52Q1WP9GApfR5foOw-oGDKLWfIYlTGcE58TDPWyXdzuIq6R6do6BjtgUFRIv-aKvUwqr_q6BT6c-VChSCwYEfkJSyfbJ0xzNXV34zjAnwewjfGhxkFRokGiOCtTbCbzmY8Lopb6wXSNhxSsEo149w_qADX0UROiaLBGk0n-yad4LK-2MtBm2IXfGknhJhQQQd11XIanr3dGfCzAMEVByCXQkKxPuSSO-shyAr-c6f_Grj0LzGOpzfWa9BVTjp-lVnEy76564Gk1Cs0K9NTqrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815c9ff5ee.mp4?token=nNyVOxqrVmI4oEwFvPQuSrvkJdWRZJI8QdEnW38PuGnXsNz5vyvo7ReuBOhDbPwjq52Q1WP9GApfR5foOw-oGDKLWfIYlTGcE58TDPWyXdzuIq6R6do6BjtgUFRIv-aKvUwqr_q6BT6c-VChSCwYEfkJSyfbJ0xzNXV34zjAnwewjfGhxkFRokGiOCtTbCbzmY8Lopb6wXSNhxSsEo149w_qADX0UROiaLBGk0n-yad4LK-2MtBm2IXfGknhJhQQQd11XIanr3dGfCzAMEVByCXQkKxPuSSO-shyAr-c6f_Grj0LzGOpzfWa9BVTjp-lVnEy76564Gk1Cs0K9NTqrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار مردم در مصلای تهران: ما همه خون‌خواه پدر، گوش به فرمان پسر
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/666584" target="_blank">📅 22:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666583">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
استان میسان عراق چهارشنبه و پنجشنبه را تعطیل اعلام کرد
🔹
استاندار استان میسان عراق روز شنبه اعلام کرد که روزهای چهارشنبه و پنجشنبه آینده به مناسبت تشییع پیکر حضرت آیت‌الله خامنه‌ای در عراق تعطیل خواهد بود.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/666583" target="_blank">📅 22:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666582">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
تأکید عراقچی بر ضرورت خروج کامل صهیونیست‌ها از لبنان
🔹
وزیر امور خارجه امروز در دیدار عضو هیأت رئیسه جنبش امل با تمجید از پایداری و استقامت مردم لبنان در برابر تجاوز نظامی و تهدیدهای رژیم صهیونیستی، بر موضع قاطع ایران مبنی بر ضرورت پایان قطعی تجاوزات این رژیم و خروج کامل اشغالگران از لبنان تأکید کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/666582" target="_blank">📅 22:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666581">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/splcktFa8bjGSb6xchVx_-IB-n9CHQNTe_Bymc_DrZBPKgDt0Lp3NdKSZs73V1MQdnHEvfk0niW-K9RIf6gBo5DNx0ajRW_CVWF_mPAlotkUDpAjC0HG2vZlpSrV6kMs0171yfzus4-NaZtyB85SFX9bekSObJqgsjqg42WrhWfLtqXYg20yIkdBL4VAJjMm5TW8YtHUytcm8XZsNvsI4umMTZhofkaLYio6shlfJ4UPUWJeidOty2w44BBrHRUrtGgwbJCFqkd5GxVwBogy6ujRBGyCWyjVpBwG0cF0UUp4ymt2W7kOM1PpTR9VReFbMyZEpuLZJ8B9H2GY9WoKFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
هموطن گرامی در صورت
سرقت یا گم شدن
تلفن همراه،
امکان ثبت و پیگیری آن از طریق سامانه کشوری
همیاب24
در دسترس است.
اعلام سرقت از طریق لینک زیر
⤵️
https://hamyab24.ir/l/kbi
https://hamyab24.ir/l/kbi
سریعتر اقدام کنید؛ سرعت عمل در ا
علام مفقودی، 50 درصد احتمال بازگشت گوشی را افزایش می‌دهد.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666581" target="_blank">📅 22:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666580">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqbJYzzKRoikUmJH-iYrb6ikZzlklRHYg9XZHYGIC0JuLOJOWI46tFBvclmSU9o3i_eFqrJVOGEgYFDM8rpJPvjUluqtK6RQzHzfsuGMKbNfjJeEpyd8MR5ro6Ji2tt4YeqLMb0WyoI78iIfvQ_Cn8P5pq7XW8dZ7rTYGt-V-Gzq2kKrvhqW55eqSCmhZcPH_eIG1Jd01PIFYKvUgFokpmE7sDUFXRLon3WvWYoD4Zc5OJcnwJm2gYW9nFN9b0baT3spvualpfNNXh8anDU6NfxPdMY1q5mkke6b_fsTkhl5tofDsZJNnbTuSp320ypT7MePRwLtT6Nmy77ZesxKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر شبکه خبری الجزیره از مراسم وداع با رهبر شهید انقلاب در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666580" target="_blank">📅 21:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666579">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
محاکمه یک ایرانی‌تبار در لهستان به خاطر انکار هلوکاست
رسانه لهستانی Notes from Poland:
🔹
دادستان‌ها در لهستان، یک شهروند آلمانی متولد ایران را به دلیل اظهارات انکارآمیز درباره هولوکاست تحت پیگرد قانونی قرار دادند.
🔹
او سپس این اظهارات را در یک ویدیوی آنلاین منتشر کرد. در صورت محکومیت، او تا سه سال زندان محکوم خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666579" target="_blank">📅 21:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666578">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حضور رهبران تاریخی مقاومت در مراسم وداع قائد شهید امت
🔹
از امام موسی‌ صدر تا نلسون ماندلا و.....
آزادگان عالم در خیمه حسین‌اند
@Tv_Fori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666578" target="_blank">📅 21:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666577">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f8803cf1b.mp4?token=nSrqFcXr8gQ-9YTpIZiz0bjZwjT8BXf3qprR5XUkYESAF_JjPOkpR_tMzYtQyvSRmEPTjMZJNLLAideKZmCVAQmp7Wa_3UEoOGxczkd9_VnCS6BYPnFMQTf4wyVdf9bArjUm1oWQ0jQh53Fu5LqaGHaIARQVP_mTiJ_UWQ2BV_jnAa0Vy9xeYpF8pD4cLqch46sSUgQ_sGt2OEzPIjRuZinAc31Iwt67JdWz8__F0UfYtzbzNo0aUAQFfHA0pKNewvBfkZgvHzcC6QiEEP7ev3gnkSzn248q6OHINybL9z3cGSnsxQk8hINtRpSn20cRNX5tzDb7PVDkxeLIh5319w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f8803cf1b.mp4?token=nSrqFcXr8gQ-9YTpIZiz0bjZwjT8BXf3qprR5XUkYESAF_JjPOkpR_tMzYtQyvSRmEPTjMZJNLLAideKZmCVAQmp7Wa_3UEoOGxczkd9_VnCS6BYPnFMQTf4wyVdf9bArjUm1oWQ0jQh53Fu5LqaGHaIARQVP_mTiJ_UWQ2BV_jnAa0Vy9xeYpF8pD4cLqch46sSUgQ_sGt2OEzPIjRuZinAc31Iwt67JdWz8__F0UfYtzbzNo0aUAQFfHA0pKNewvBfkZgvHzcC6QiEEP7ev3gnkSzn248q6OHINybL9z3cGSnsxQk8hINtRpSn20cRNX5tzDb7PVDkxeLIh5319w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول مراکش به کانادا توسط اوناحی
🇨🇦
0️⃣
🏆
1️⃣
🇲🇦
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666577" target="_blank">📅 21:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666576">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5762c89eb4.mp4?token=KBUdz4Z0BMtXGF918y24OCDgtkOAGbHAsGYFHru6SIC9sfIYOZQJrR8spZGau2v9jsRZhsp8vj0JI2uGtq3HQdjJkeMIVUoHG6IuppXH-Je_AdKToRNVWdORA9eOt0FK33HQH9dniXloSZBtpn-86a6USR7OLolFL2Flz7hZ8bkq7dFJHCBFG-GBQRYkwVFFJchZTGuZ73QSjX5fv_Yi5AFQmobRgdpYASI_rUgXswKew2rUEp76Bltr-YGy5UJEw41sMhZW8VIT7l_ZbT62YZ4XMZJkGqMcewrVw8PxP45q2pHUjmJR4gvg6dMmwJC47R-1DU-5Xp9hOcH4-7LfaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5762c89eb4.mp4?token=KBUdz4Z0BMtXGF918y24OCDgtkOAGbHAsGYFHru6SIC9sfIYOZQJrR8spZGau2v9jsRZhsp8vj0JI2uGtq3HQdjJkeMIVUoHG6IuppXH-Je_AdKToRNVWdORA9eOt0FK33HQH9dniXloSZBtpn-86a6USR7OLolFL2Flz7hZ8bkq7dFJHCBFG-GBQRYkwVFFJchZTGuZ73QSjX5fv_Yi5AFQmobRgdpYASI_rUgXswKew2rUEp76Bltr-YGy5UJEw41sMhZW8VIT7l_ZbT62YZ4XMZJkGqMcewrVw8PxP45q2pHUjmJR4gvg6dMmwJC47R-1DU-5Xp9hOcH4-7LfaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر حسن ابوالقاسمی: بمباران بیمارستان‌ها و کودک‌کشی‌ها و افتخار به آن توسط نتانیاهو نشان می‌دهد که دشمنان رهبر انقلاب چه کسانی هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666576" target="_blank">📅 21:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666575">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2869806eb4.mp4?token=eYSs-GfVb0rza8uvVQM5TR92_7TQ9HSzCCf3JmEV-gk9eMNboI1aV8podfrjQnCuGbecWTedDHYagohiDayxPhnsPyppcBjMJWRmuWDdCOFyeKcX2kBRu4J9Pkg6ugbYMBtSyNHyRwrPmIwX-rlM1rRIY2Fud_GmgC4gd7FHDMbj30rbZ64ccEJCz_ZNOa7F5X76ZjaBCixig3J6vFkRCY5klvU6pF767EhR5fIeiGwh2N8GGgS_ljSxlHqyCbKPMDdbDXEOVU1g6yTggdwdYGsGhPg3l6dRSm388nw_-2R5PyBDKrgmq7V_xFXlVeiaN3tNSEoT3ZxV2mPSAmCL9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2869806eb4.mp4?token=eYSs-GfVb0rza8uvVQM5TR92_7TQ9HSzCCf3JmEV-gk9eMNboI1aV8podfrjQnCuGbecWTedDHYagohiDayxPhnsPyppcBjMJWRmuWDdCOFyeKcX2kBRu4J9Pkg6ugbYMBtSyNHyRwrPmIwX-rlM1rRIY2Fud_GmgC4gd7FHDMbj30rbZ64ccEJCz_ZNOa7F5X76ZjaBCixig3J6vFkRCY5klvU6pF767EhR5fIeiGwh2N8GGgS_ljSxlHqyCbKPMDdbDXEOVU1g6yTggdwdYGsGhPg3l6dRSm388nw_-2R5PyBDKrgmq7V_xFXlVeiaN3tNSEoT3ZxV2mPSAmCL9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: ملت ایران عاشق رهبر و میهن خود است؛ مردم ایران خواهان انتقام بوده و خونخواه اصلی رهبر خود هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666575" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666574">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ممنوعیت پیش‌فروش خودروهای وارداتی در مناطق آزاد
🔹
دبیرخانه شورای‌عالی مناطق آزاد تجاری ـ صنعتی و ویژه اقتصادی، هرگونه پیش‌فروش خودروهای وارداتی در مناطق آزاد را ممنوع اعلام کرد و نسبت به فعالیت افراد و مجموعه‌هایی که با عنوان پیش‌فروش خودرو اقدام به جذب مشتری می‌کنند، هشدار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666574" target="_blank">📅 21:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666573">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b7c265df.mp4?token=tc0FKoxOdE4r9D1DRx7eW1AeEBTrXn_mGXl_Bp80nw_onZPxpvbOdYaI7bi9Zk_jEPD9F8VvleOfpmpS_xwCoV2JtPh7GesivK3TE5YG5m2hfgg97kyDjPUj2OholOZDtgm6sNlO4aNL1JQvjOtOh43yiYom58ITmxYiUact0X5a-uqMBSgeHlRzs7SmcX68yeCoVwIZZtyvLYBGuBT3Ml44Y_mfQKJJbl9w52VnsUYFH0na2ibWRo_CzS65_3zeJsl2ZykbiR7tQF5EwmeEQeFKfR7dH0aEc_uAawo0aiGea5UlVhj15lj6MKr4K7jTxJxtf_ItH4jEeEE9bWDikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b7c265df.mp4?token=tc0FKoxOdE4r9D1DRx7eW1AeEBTrXn_mGXl_Bp80nw_onZPxpvbOdYaI7bi9Zk_jEPD9F8VvleOfpmpS_xwCoV2JtPh7GesivK3TE5YG5m2hfgg97kyDjPUj2OholOZDtgm6sNlO4aNL1JQvjOtOh43yiYom58ITmxYiUact0X5a-uqMBSgeHlRzs7SmcX68yeCoVwIZZtyvLYBGuBT3Ml44Y_mfQKJJbl9w52VnsUYFH0na2ibWRo_CzS65_3zeJsl2ZykbiR7tQF5EwmeEQeFKfR7dH0aEc_uAawo0aiGea5UlVhj15lj6MKr4K7jTxJxtf_ItH4jEeEE9bWDikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی ستاد بدرقه «آقای شهید ایران»: مراسم وداع با پیکر رهبر شهید انقلاب تا ساعت ۸ شب فردا در مصلی امام خمینی (ره) برگزار می‌شود
🔹
بدرقه آقای شهید ایران در خیابان دماوند بعنوان مسیر اصلی تا میدان امام حسین، میدان انقلاب، میدان آزادی و به سمت بزرگراه شهید لشکری صورت می‌گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666573" target="_blank">📅 21:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666572">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55afbb1663.mp4?token=T2TBlwLXzWCfT7nOAjsJJeRI3jTwh8l7QMrxGNZKhSROc19bxsrEiLzq3YVSsPBDTHCF2OhWFM208l4vC6Zp-U8_O5fUuPcuDhb4xx__GF2thr9lZLXZ28yVlRiPOBP3hS9xdi1IER78NG6pAsZD9Dj8oqTAq64HrgITtGXnkvzNIeJrScC9cv6mRsrLsoxeFJgBppVkEgq50gf5k2ttmjILJ3NUx90CYmTQCuIRIl2T7f0jr0YlVyqYhT-N5JLgPYKSRUKOqFqG8hkXzPO2bGfZnaUkv1bPEtJnMDrVrURqdixtLRVvAQvdQehXIvO_KknHKiyUA6CvU-vsSwOyKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55afbb1663.mp4?token=T2TBlwLXzWCfT7nOAjsJJeRI3jTwh8l7QMrxGNZKhSROc19bxsrEiLzq3YVSsPBDTHCF2OhWFM208l4vC6Zp-U8_O5fUuPcuDhb4xx__GF2thr9lZLXZ28yVlRiPOBP3hS9xdi1IER78NG6pAsZD9Dj8oqTAq64HrgITtGXnkvzNIeJrScC9cv6mRsrLsoxeFJgBppVkEgq50gf5k2ttmjILJ3NUx90CYmTQCuIRIl2T7f0jr0YlVyqYhT-N5JLgPYKSRUKOqFqG8hkXzPO2bGfZnaUkv1bPEtJnMDrVrURqdixtLRVvAQvdQehXIvO_KknHKiyUA6CvU-vsSwOyKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی رفتن‌ها، فقط نبودن یک نفر نیست؛ انگار بخشی از وجودت را با خود می‌برند. بعد از تو دنیا همان دنیاست، اما دیگر هیچ‌وقت برای ما مثل قبل نمی‌شود. دلتنگیِ تو پایانی ندارد
🥀
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666572" target="_blank">📅 21:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666568">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9160db867.mp4?token=b-IkF9ji8PGkqZ9GRptU6S9b3dw9GTg8YS7z94GVRZBupJeZ_Jq_jIyBivoV1T_4ykIJQTffa2OWAP2zyDLUzvp4IR4szsVU7JHDz4eTnl3f6Bp1YFKwkBnNl-UHKxsK3DSGRaDpVZyfZltPagLwmnTzGlEvT9Gohh7whEPRQVj3qSFQNo-rxvwWH0MXC2wVRhL3ZNQ9NjxphpKFfwurSeKoKFSIvVzqFmDrLrCFqi626EwW7H3b_tRRYOtPicUY2hXnyk_xHw21--xrpTXWVnu_eVEbOSyXvOSHS9L3asFoXAuNlbUnoEDPrPCR6CjvI1e6u-QM5buLJ6MTtRF6SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9160db867.mp4?token=b-IkF9ji8PGkqZ9GRptU6S9b3dw9GTg8YS7z94GVRZBupJeZ_Jq_jIyBivoV1T_4ykIJQTffa2OWAP2zyDLUzvp4IR4szsVU7JHDz4eTnl3f6Bp1YFKwkBnNl-UHKxsK3DSGRaDpVZyfZltPagLwmnTzGlEvT9Gohh7whEPRQVj3qSFQNo-rxvwWH0MXC2wVRhL3ZNQ9NjxphpKFfwurSeKoKFSIvVzqFmDrLrCFqi626EwW7H3b_tRRYOtPicUY2hXnyk_xHw21--xrpTXWVnu_eVEbOSyXvOSHS9L3asFoXAuNlbUnoEDPrPCR6CjvI1e6u-QM5buLJ6MTtRF6SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
کلیپ های رهبر شهید حضرت آیت الله سید علی حسینی خامنه ای
همونی که براش نمردیم
آخر سر فدای ما شد ...
#رهبر_شهید
#استوری
@Heyate_gharar</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666568" target="_blank">📅 21:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666567">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d6d4fa62.mp4?token=LQEk7VBvd6Niym8yJSWrgPJxH3DCBaOlhC3JsSKD50bDh6UkExq5sLL1kicSG0yyxhjp8hHjHnEWlZro4N1qQ-RUglVytES20pY0xI6KaqcEjx2XYlnswnJL06PaeJvJqVzlq9dob2gaMnbMoIxlGDt1r_civZ0Ay_gKhE-YQlz1ToYqkRv8v9BrohWcdF87qZbTgtvMNANqdMu3gXV59IGSOc1mNMniqNnwwSvuWDH4DPmIjL4vbxPo6klnSuvWW2ZEvyfGshgNQsmwZsXPGflYwMTXeBPaSrvUs9FMDAAUNYA0K1HKiFkuvfve2zwvEibA460X-J0gKqi10zpFwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d6d4fa62.mp4?token=LQEk7VBvd6Niym8yJSWrgPJxH3DCBaOlhC3JsSKD50bDh6UkExq5sLL1kicSG0yyxhjp8hHjHnEWlZro4N1qQ-RUglVytES20pY0xI6KaqcEjx2XYlnswnJL06PaeJvJqVzlq9dob2gaMnbMoIxlGDt1r_civZ0Ay_gKhE-YQlz1ToYqkRv8v9BrohWcdF87qZbTgtvMNANqdMu3gXV59IGSOc1mNMniqNnwwSvuWDH4DPmIjL4vbxPo6klnSuvWW2ZEvyfGshgNQsmwZsXPGflYwMTXeBPaSrvUs9FMDAAUNYA0K1HKiFkuvfve2zwvEibA460X-J0gKqi10zpFwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقامیری: مردم با حضور در مراسم تشییع، غیرت و شرافت و هویتشان را سر دست می‌گیرند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666567" target="_blank">📅 21:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666565">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
حرکت دسته خانواده شهدای میناب به سمت مصلی تهران برای وداع با آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/666565" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666564">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0cc9eb971.mp4?token=V1NUqLvVZoPzXFZwjHccrXuQ3XbIId6JLzDmRNz7S0vG9Q2s22Xr1r2yQTJcSv3v4GvgMkRaIxxr_7IZ-xi5If0DIscplkoA6M4Gq8sa4bcV_e9dpurzTUYvWgZUmjCo8hXdWWRy1PqLT3B8Zg4_zD1KT63U-M-rzNU4Wm-GLfzi4bHybjQAdzbXTeHnlAj-VmnLtW9FVt2vmKZAM92StHjdKwH8SWWqzsgR63pR57PQfPzg4SaUS_aVJ6ouiq-I94jBpTcgIQ4LeY399Ugn6tFuLeqWKcF6NCxS0wnv-KEOzsUX-VyTbbkfTSswfVTT0h-xcl_wZacHd2NJ7XjByA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0cc9eb971.mp4?token=V1NUqLvVZoPzXFZwjHccrXuQ3XbIId6JLzDmRNz7S0vG9Q2s22Xr1r2yQTJcSv3v4GvgMkRaIxxr_7IZ-xi5If0DIscplkoA6M4Gq8sa4bcV_e9dpurzTUYvWgZUmjCo8hXdWWRy1PqLT3B8Zg4_zD1KT63U-M-rzNU4Wm-GLfzi4bHybjQAdzbXTeHnlAj-VmnLtW9FVt2vmKZAM92StHjdKwH8SWWqzsgR63pR57PQfPzg4SaUS_aVJ6ouiq-I94jBpTcgIQ4LeY399Ugn6tFuLeqWKcF6NCxS0wnv-KEOzsUX-VyTbbkfTSswfVTT0h-xcl_wZacHd2NJ7XjByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عباس موزون: رهبر شهید انقلاب تجربه نزدیک به مرگ داشتند و یک بار روح ایشان از بدن جدا شده بود/ بعید نیست اسرائیل از نیروهای شیطانی کمک گرفته باشد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/666564" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666563">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای رسانه عبری:  نتانیاهو انجام حملات در جنوب لبنان را به تعویق انداخت
🔹
رسانه‌های صهیونیستی گزارش دادند که بنیامین نتانیاهو،  اجرای عملیات نظامی در منطقه «علی الطاهر» در جنوب لبنان را متوقف کرده است.
🔹
بر اساس گزارش‌ها، این تصمیم پس از درخواست دونالد ترامپ و در سایه هراس از پاسخ تلافی‌جویانه ایران اتخاذ شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/666563" target="_blank">📅 21:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666562">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
این سلاح ایرانی لرزه بر تن دشمنان می انداخت
🔹
سلاح بومی که در اواخر دوره صفویه و دوره نادرشاه افشار و کریم خان زند به کار گرفته شد، سبب پیروزی ایران در جنگ های بی شمار گردید و توانست ضربات سختی به دشمنان شرقی و غربی ایران وارد کند؛ این سلاح بومی که در جنگ با دشمنان داخلی و خارجی به کار آمد، «زنبورک» است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3227867</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/666562" target="_blank">📅 21:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666561">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e8c0f03e5.mp4?token=NV7pKstA0w3gGDXxL8udutGk79c2L22ny72NBCZ1ISFE_1M3Ru8Pl1-ZLgpaVU3VehqnLnvD4HF_HZw5ij-S_sauYicQZJtOtdEx8aaj3gAK6DubTEF1KAWDW2CHnJqEkAEcDXWveTh74PoHvg_RHVPb6Y5yy1OzP26hdDgrgvozgiQ98mEMyyo6aw0aeiVq_WE-XqLgFnCcwQVCYUH4VPcBKBvJOebMHMBLKG-58ERdOWU0wYd_gTEpvOFAUiDrgXu1HmJMOv7zPXy4CHMw4BX2shnmr-EMl3nG9JXTs66Ms35x9MfsrYWh-CKSk-RvNEYhmghm_-PXMj-1fTb0CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e8c0f03e5.mp4?token=NV7pKstA0w3gGDXxL8udutGk79c2L22ny72NBCZ1ISFE_1M3Ru8Pl1-ZLgpaVU3VehqnLnvD4HF_HZw5ij-S_sauYicQZJtOtdEx8aaj3gAK6DubTEF1KAWDW2CHnJqEkAEcDXWveTh74PoHvg_RHVPb6Y5yy1OzP26hdDgrgvozgiQ98mEMyyo6aw0aeiVq_WE-XqLgFnCcwQVCYUH4VPcBKBvJOebMHMBLKG-58ERdOWU0wYd_gTEpvOFAUiDrgXu1HmJMOv7zPXy4CHMw4BX2shnmr-EMl3nG9JXTs66Ms35x9MfsrYWh-CKSk-RvNEYhmghm_-PXMj-1fTb0CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخش صدای دل‌نشین قائد امت
و گریهٔ مردم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/666561" target="_blank">📅 21:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666560">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfef33bb16.mp4?token=sTLcOOhXOxjRi2a14BLz3TdWUIsIUH9PO0264ebRqDChsebAqQ1a5rUh97W7_Y6tEurdreVUW9-h4px78CsrxMWl7jLZPGzhlc7Yh5GRiEsSMFInXPjvPF52ImYqeWd331Z3Z3nAgSnfCOT1qxLOHksCiHr-wPCJckSu8Dj6naT2dtPU8xTL_6ccTc0N_OuS2YzlMvDcGROdDl5rAqJvkSHPRGDsf3UOnj1sI9Rvb8Fj5rnLtW-yy5oqMeUEDbBvXcl25I2lIyFiRdWaRgsMWGs3dZCxgZr3Hb3wv6TiMZtw1V_Eu6sGGx9aGjB9OgXxFpjIcYhPEIYv3uu6j2mI4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfef33bb16.mp4?token=sTLcOOhXOxjRi2a14BLz3TdWUIsIUH9PO0264ebRqDChsebAqQ1a5rUh97W7_Y6tEurdreVUW9-h4px78CsrxMWl7jLZPGzhlc7Yh5GRiEsSMFInXPjvPF52ImYqeWd331Z3Z3nAgSnfCOT1qxLOHksCiHr-wPCJckSu8Dj6naT2dtPU8xTL_6ccTc0N_OuS2YzlMvDcGROdDl5rAqJvkSHPRGDsf3UOnj1sI9Rvb8Fj5rnLtW-yy5oqMeUEDbBvXcl25I2lIyFiRdWaRgsMWGs3dZCxgZr3Hb3wv6TiMZtw1V_Eu6sGGx9aGjB9OgXxFpjIcYhPEIYv3uu6j2mI4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقامیری: مردم با حضور در مراسم تشییع، غیرت و شرافت و هویتشان را سر دست می‌گیرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666560" target="_blank">📅 21:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666559">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
روایت الجزیره از مراسم تشییع رهبر شهید انقلاب
الجزیره:
🔹
پرچم‌های قرمز، که معمولاً با شهادت مرتبط هستند در تشیع به عنوان نمادی از انتقام تلقی می‌شوند.
🔹
این پرچم‌ها در سراسر محل یادبود مصلی بزرگ تهران و دیگر تجمعات مردمی دیده می‌شوند.
🔹
«ما باید برخیزیم»، شعار رسمی مورد استفاده برای مراسم بود که با تصویری از مشت گره کرده رهبر شهید ایران بر روی زمینه قرمز و سیاه همراه است. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666559" target="_blank">📅 21:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666558">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e0a6909fd.mp4?token=NVrVyoZxy4UdE0cfI-Ol_KE6QzgNfkW1Y61s0uemsBzNEviE5ZZLyZaeskJsiwDuPEHM4DvS5V4WTiV9fzlNEsFAPzo5KpLs70QcaoyLHq9TdU30bQNzVWFMWObTMdt8kXcByk5y1Fj3WMg4RQggWKstXplMXsLSMN1Z9ZLYI6faJgyicN-HpUP1aGDcibvqpjsq7yveVZugfaIJggE9_ax6OjtaJv7LlT-hdR1dmGqFd5Ee341MK_bpphZGBZgEDTzs2CAuNna_h6WcjvXVFaBu7n2j5dU5K4da903YV-GSrPfHtxNBW9mCPuKeyeU5moIWrKQ5DikLUfAP8i479A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e0a6909fd.mp4?token=NVrVyoZxy4UdE0cfI-Ol_KE6QzgNfkW1Y61s0uemsBzNEviE5ZZLyZaeskJsiwDuPEHM4DvS5V4WTiV9fzlNEsFAPzo5KpLs70QcaoyLHq9TdU30bQNzVWFMWObTMdt8kXcByk5y1Fj3WMg4RQggWKstXplMXsLSMN1Z9ZLYI6faJgyicN-HpUP1aGDcibvqpjsq7yveVZugfaIJggE9_ax6OjtaJv7LlT-hdR1dmGqFd5Ee341MK_bpphZGBZgEDTzs2CAuNna_h6WcjvXVFaBu7n2j5dU5K4da903YV-GSrPfHtxNBW9mCPuKeyeU5moIWrKQ5DikLUfAP8i479A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصلی امام خمینی (ره) میزبان نخستین شب وداع با پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666558" target="_blank">📅 21:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666557">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای ترامپ: ایران و آمریکا تصمیم گرفته‌اند تا  یک هفته به مذاکرات وقفه بدهند
🔹
در این فاصله، هیچ‌یک از دو طرف به سوی دیگری شلیک نخواهد کرد./انتخاب
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666557" target="_blank">📅 21:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666555">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gY9U5x-9Vpa9FLLQKXpI6TnnQku_e-y0SVDlW3k8pMePdZizOuKB68z8Zy_wleewSPg1IzlDxqn1njKP2GbSCblpF09IsmE15jyaI_aE8Zi2r3BotRnTOp1_cEDEquFMnj3mvlnjHgKywKCDR0zoZMX1HpTjNs1keHMKsuKUGrDoOUUspgM5_L-f8mt92UYpFVbaazL6OI8Pau92_fsovQKaNYjVbzhRj21QyBoC9EmYMo0jXZEfe0AmukSIaTmH00ltDM3OOtlHimkpSJ5CxYp9aLj47LSvGiVOTplumqoVV3BBp2YHynZc8c9yq-YQfokEDYa0jiAmiBgEarfYOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی سریال: چرخ زمان | (The Wheel of Time)
🔹
ژانر: فانتزی، ماجراجویی، درام
🔹
امتیاز (IMDb): ۷.۲
🔹
خلاصه: پنج جوان از روستایی دورافتاده، ناگهان وارد سفری می‌شوند که سرنوشت جهان به آن گره خورده است. زنی مرموز از فرقه «آیس سدای» باور دارد یکی از آن‌ها همان…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666555" target="_blank">📅 21:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666550">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0K6UHy0TLJGJwmJH0atGDRxXtdIC6HTVjx5UITjcf0kmKHjx2_slC8d2PDDImM6hZ8tvMra_-WpnYppaB7oFqlHHTVyktbqTUrBmRRQ92oHHAU95uyhmRCS4DlrPwWalVTRgjef8MTpaaxaBh1GPg-tVQra6ijvl0BxH1TjLNz6dzugGwHCZShl8j75eKrYni3zaQ-RcM0aoyQXzDD5Jkl1km1LUFjwfxXyVky9XqnLJgbzrLG8XhWCRacZ-RASYwoDKiPL90UhLcU6PvNqkr0nX3Be_ssOGyzpMU0n_SvdMmrqRzbAwqKJnCmAdo2jpP5je1aObGoj0EJE9tEj1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7YPhor4gX5G-9MGK3ltMiRbqfdSpPzAgjSY21W_DrfWSsZsnRXq_maPordx3MnLACbWTwivKkxyrRd4n0MNx86k8MurbXrckjV1LzkiozDI4kqcvx5yPuW4AgiK2yktVj5MApgtDCZSL88mmsmIXrOH3j8BRrX7GZwgKT0Xcg2kNU7j2eLXMQy34ExTrcEePhfihEd8iJD8G2tpKeTTJPjPlJt1hr8C0MArV09OFfHxE9hhjnXwjqD3zanvNt8QHUJjiwkTQRy_s8dPvQsz4ZRF9yPhDDHqT1d6I2zMlgErBmeu4EiYD6-K_E5pPOh0hqKEc9-3OoefGI30dkgnEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaAgYSRkxelAw1p7zXrQvyGaMQt0ZNq40fLPp0cTvzxgOozZ7JCeVTTGOVy5WVZ16QsIOcHRhs2f-hufeMfpPSi-D7OV-nw3MutU4ht6UG30rFzqib4_i0aeAgo1moQdrbDwMewmGKw4NZnx2s3f9VCValzDs6eGL1swU2C1-tdhNhE7NFTbQC1_icviUEVhPHaGhpyQDCXIBGsKgr6gVSgXXPaUUBaQe6V7fjMpB_Ykoyb-VedggVfTCG93vVZZL6fgLRawoXQk4isab-3yXGDdm0afzDk2ltfpKJVtMqvppzPJlgdfysu0Osly0-4lHwH2RfKRxB1pbq1LDQbQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbpLvZFYuox2QyNiRqNA9YadY-YoVStBN9cwLZ5GzPYwlzxZzj6vP9EqWUfVWk84Y8xdH9GMRWLujm5ntUEV2ycaO6aviXRInBMKjMFXsE3PjQGrJaLPux_1fVa8p4D6-2fJjay8XYyC-iIFkLyKuc3gEZeRv5K2YFi6zrfWB1L-oJwbMSHRIcUyx42hmf9mIkNkl2D1Q-EXwTouGxg1vz9JbxPMB2aB3Iz4JMkR-i6pSqnskndynFixnvnz5CvUEgBuK4CnonWEU3we4ltYSPwDrqsHlEZSGSgLuz2xe_MhSxE1_7LJA15pjureHsCMVmo1qqavWMk0Gv5o2qRsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmVDNYHgd_8g4EHnfeuEVZYQvylcpjOuNsWt9YdGPT_GuPC6pEujIYeOilunSsmV-xeIzTj1tOhAUgAzLMQnhc3rVgN6bC1gWQZln5QvoUj9Sfk4ZlgFlX3-0sQvG5mmAZyVgJzyG0ZfFLL7SlIkJ7qQLX5TMs2wkKQiBHsbkVHgaIwDfOHkoV3e8WocMFQi66MwNHtHLzfa0beEFZEdiQ46EGdVNxGOjjwujQp0iKEur2X77L4F5A94Pf7_uahJ_Mboicd6HkYAfe_14btLDwyLrjR65euRYjXjBxU67ryQ3SmWmCGCxqb4yVwI--sz7hMr1PSYVJ5ImKci7YT-wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرگزاری الجزیره از روز اول مراسم وداع با رهبر شهید در تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666550" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666549">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
بانک مرکزی شایعه نیویورک‌تایمز را تکذیب کرد
🔹
بانک مرکزی ادعای مطرح شده از سوی روزنامه آمریکایی نیویورک تایمز درباره نامه عبدالناصر همتی به رهبر انقلاب در خصوص ذخایر مواد غذایی را تکذیب کرد.
🔹
یک منبع آگاه در بانک مرکزی: چنین نامه‌ای درباره کمبود ذخایر غذایی به هیچ وجه صحت ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666549" target="_blank">📅 21:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666548">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
پنجره‌ای به مراسم وداع با معلم شهید خانم زهرا حداد عادل، عروس رهبر شهید انقلاب و همسر شهید رهبر معظم انقلاب در مدرسه فرهنگ تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666548" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666547">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70caf986c.mp4?token=NcYhWtNvpZt7mZR4-VuRtWfvEE_zL5QZw736At8S1_D-xfRvdGd2wgbycABsFFkZYHAULbJ4NbZ9Re1XoLQgEGKMs72DSwUoHO5SU1u_JXw2zHUDmp82WJzRSmhstLqC5fLht7lEV7Tnhbnf5LhR70cVK-ATagdIW4ui1mdWyeQWf82ZrX_7McfF1PoZmhRseSEjnLCCqWpUTGNMpmUATBzKma2IDflGdhVkVlbBfX_vD5EGKwBNOMiW2j-gotjOys-KlbKhvzMPsnqa85No3EnUkYRLGpIW4Ox22LabVl8u5vT6v6XuJITNh_QoWywLKCsjI7t0KA90kugSaDpGYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70caf986c.mp4?token=NcYhWtNvpZt7mZR4-VuRtWfvEE_zL5QZw736At8S1_D-xfRvdGd2wgbycABsFFkZYHAULbJ4NbZ9Re1XoLQgEGKMs72DSwUoHO5SU1u_JXw2zHUDmp82WJzRSmhstLqC5fLht7lEV7Tnhbnf5LhR70cVK-ATagdIW4ui1mdWyeQWf82ZrX_7McfF1PoZmhRseSEjnLCCqWpUTGNMpmUATBzKma2IDflGdhVkVlbBfX_vD5EGKwBNOMiW2j-gotjOys-KlbKhvzMPsnqa85No3EnUkYRLGpIW4Ox22LabVl8u5vT6v6XuJITNh_QoWywLKCsjI7t0KA90kugSaDpGYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی شورای نگهبان: رهبر شهید می‌گفتند در تایید و ردصلاحیت‌ها قانون‌مداری و رعایت حقوق مردم حفظ شود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666547" target="_blank">📅 20:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666546">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmNGxJykqBfYf5SWed1VcJmS1gdTc1071Ghz3i9rwy5Xh_f_Gf46O1gxXlH81-mXdBFtJ9-5NQxtMqsRsvBL_JhDtgB5omSSepzgGLm22QZnqfEiAbB2amoy100crSf6HBISAB5FP54U9e0jIoEHWi3yBosJwymQES-tEWjJP-iBehzOjOWDIsS1GAn1hmtlM0ZBohvr-J2JqfijUJNp-5KFmjKFXEW0Fb1mA1H7RjY1Y-XqlEqeUSpM_1BacRKYIcVJtovNKjSCpPk-Rcb8nZr8OdtdsjH1j889yEOiGvSD4zNUgsKUjXvsEeTi1IaudDHNfTa2VBhFzpEKIBF6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فردا؛ مراسم اقامه نماز بر پیکر امام مجاهد شهید و شهدای خانواده ایشان
🔹
یک‌شنبه ۱۴ تیرماه ۱۴۰۵؛ مصلای امام خمینی(ره)
🔹
شروع مراسم از ساعت ۶ صبح
🔹
اقامه نماز، حوالی ساعت ۸ صبح
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666546" target="_blank">📅 20:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666545">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ترامپ: از دیدن گریه مردم ایران در تشییع آیت‌الله خامنه‌ای غافلگیر شدم؛ چراکه فکر می‌کردم مردم از او متنفر هستند
/فارس
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666545" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666540">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOjh4MDo8OZdB_ZwkGAG_Gk0wdOCHSM7TN9qlesudk_4I5XKQWDwXKUADmDpz6OyyQBqTjZd2EEMB-gnBKuZzLP5SMlDE-_yZJjnbdi9hW6GfHmn9R0q7no46gz6RlD3a4RtHw4RiBjJ5CJtrDBY4WkKYpUG5yTng1SJx8_P4cyHHdL3jSyRgi__JcNpSU459Wq6U-R4nsRyiCzCd-nrnm2v3OvZRw6F9AI4mg0-sJoQncoM8mh95pALPL9ikYDu9WH317UuVf6T6NeLIJyYS16EjVG-FA3-G-O-Su4JSX47ESUJgO6swtZQtCjq3mSom99q171DK8mFjNo7hx72MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pS9VSuos69j6G5OguHl-gdifXDVPjYbN3tAx4XrCM77pKhqKudDpfC_sirun57_76oJ1iKZ3GqQ37LDLS1NMJNhoE0WCJ3A_5TjUu0Y09MpsssppVNOKwHHrgT_TVKl0Mw5aFkguTdJdRMn6ewOlywMT48SADknCUIaWflSs75StrXRtlLLy_gqIcJYmqbpCwqua-l-wlvfv-NPlF6jt6fjxRr1FHSHUE_ThvMnSZ72EX3lKYgGUV8XL0wGGK3yvRMzGGpogjwhu7JkmSdTLW7okl2ygL-iRyuOPZniWba8V7wMJPsvf4ZBNmUPxOONGfQCxS8iBplGkqyFEwzt_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sk4v--PhwA_urdOnFuz6_DKp3rvxxJlZgUY7cDbHaTrI-LmYHy78xuWChu3WcGKjZvhdEO5T8Xp_PuoDI5u3-No0ihrmaQX7MBBCwaTDwGV7YcpSVx3E1nXV1Grj6eytNsyEJ0jCNNxqbpSzaUmv2Bdmzh-l8qb6S8G0aopkX2lKTYZTntRFbgwTmcYxwszArcCYM2v3vWiRM_-OSUjD9xXcg8KVkxmtlrBymVTf9qGjAb4iShPmHq8QOmVFQWo9Thgrt2M10PQWtfsMP8qYqcUY7pkSakFk5NbahJY4eU8atAN5rqyNq7lOoZBoUmYF2H4IfCxGkaQUSaxlKtLeuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuwKowWpAsMPKaQx8MCIyjzPNkwIFFZjryqnIc20hvPs3lbXyzjmUCeXBFIjlz8MsmuQWlQ0UyM5PElQYMWVKQYzsiGr2ufZo-T37UDdGFJgU0HQVBBq5chmXgePfxFn95byqQeZU5F62skFYYB6PtkcsQLgZWvxvkpt2nu8IPWwRMUwW5yGb9rlqz3_cGq_EZYxViLbykuv_mPyQ1rJENIH-TA2xn_OUyVRxA0Dz4AWBE89huR3OyEK4qm_Pu7GukQVSB_ZLwNjXs_Mo2j-weZUSz9PjllvYVNCyAuQosBsZWC1S57XEjRqrts--bJkQ8OgZyooWLseeGKjxTdCqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PPHqK3pjjwSQJZQhng_wxyqBTJ4dABnIet6mvbhb_aXrSnN2u9_paJPKby1HlTjk0a6DVwXKEJ6FAZPEI__cCMaOBv7tyx_kxnJoBXITRongsWMxrg2K9C0SN7HBQFRq0OH83iTMpn2CQbVYnStDRhoYSJWJB3Raxy1B0XCCOBmhaPoWy1C_nF6jrW7Hj0iAauQfeC-lJaeNNXcyKZjSUFHco0L5AiUoc3Ci5-_zRWIz0Qk9os_S8Q_W2oz3C0nCSWBurcPdaJmyZwnaI_QSKBc1o-Rq3lAYFHAZGe2Xo8YTrvgHClYGpKuP4yE7HJeFn5kIdF885wLKHSzU-erw2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور شامگاهی انبوه زائران برای وداع با آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666540" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666539">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
الجزیره: ایرانی‌ها خواستار انتقام شهادت آیت‌الله خامنه‌ای هستند
🔹
احساسات مردم در اینجا رنگ و بوی سیاسی نیز به خود گرفته است و فریادهای «مرگ بر آمریکا و مرگ بر اسرائیل» در میان جمعیت طنین‌انداز است.
🔹
بسیاری از سوگواران حاضر در این مکان، خواستار انتقام برای کشته شدن آیت‌الله خامنه‌ای هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666539" target="_blank">📅 20:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666538">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
مراکز شماره‌گذاری وتعویض پلاک کشور فردا تعطیل شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666538" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666537">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
کرملین: شاید زلنسکی به مسکو سفر کند
دیمیتری پسکوف:
🔹
رئیس‌جمهور اوکراین ممکن است به محض اینکه آماده تصمیم‌گیری‌های مهم و مسئولانه باشد، برای مذاکره به مسکو بیاید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666537" target="_blank">📅 20:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666536">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4003ac89b3.mp4?token=ZdFqTnuSdEziUoRV_9XH-sZTsHCS_-e1FV2OxNGgcX4BiJ_G4FPsxjtDXL1ORKqg5M23C4NCs4a35HGlYW5udlUBo-AaY-_JWmTuV7AophHF0nrDGyETl2BhWX9eMpEfRMCZfJ-7uUSVBcZdmvL_jl1pxAN2TXc3SPQd-50iKsBf3nTlvpm9n809NtEa3ThP9s7IIi6KbtfdyyfKmjhBb393-COoRsnES7qG6HgERvbKpIcYtkWyqG_Z5lI3HB_eMQLBhjnCaUB8oIVEDIy6C7mqfwZXKn2oK9G0UJ7i2NXmKZKjeU1ZCL4y8-C_rwHflxjZU1Hl_ZSyO2RVEe41GYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4003ac89b3.mp4?token=ZdFqTnuSdEziUoRV_9XH-sZTsHCS_-e1FV2OxNGgcX4BiJ_G4FPsxjtDXL1ORKqg5M23C4NCs4a35HGlYW5udlUBo-AaY-_JWmTuV7AophHF0nrDGyETl2BhWX9eMpEfRMCZfJ-7uUSVBcZdmvL_jl1pxAN2TXc3SPQd-50iKsBf3nTlvpm9n809NtEa3ThP9s7IIi6KbtfdyyfKmjhBb393-COoRsnES7qG6HgERvbKpIcYtkWyqG_Z5lI3HB_eMQLBhjnCaUB8oIVEDIy6C7mqfwZXKn2oK9G0UJ7i2NXmKZKjeU1ZCL4y8-C_rwHflxjZU1Hl_ZSyO2RVEe41GYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از اقامه نماز جماعت مغرب و عشا در مصلی امام خمینی (ره)
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666536" target="_blank">📅 20:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666535">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ترامپ به آکسیوس گفته است که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از او درخواست دیدار در کاخ سفید کرده و این دیدار ممکن است به محض بازگشت ترامپ از نشست ناتو، حتی از هفته آینده برگزار شود
ترامپ:
🔹
ما خیلی خوب با هم کنار می‌آییم.
نتانیاهو می‌داند رئیس چه کسی است
.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666535" target="_blank">📅 20:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666534">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU8lVvxB-OT48q2TJFGHUgkFLfKj5oFLawIx-5wgPGhqZEaoi7B3FeN-YbKkQgHHoEiLzoepTAmdug7dJejfep0yHdQjqDTsdV6tjTaiNjZ9WpnSlY0-7DLTIGJWkoiuC7QONgr6IcvRUtnQi7Qtk8EL2MOm3sfWQbwFiC3kNTfLs5C9k1iE7W1yZGD4tXSQtEcVsrYYyG09bz1ljg6xWoZ30QpmQ719OpdXw5VjHwRxiV_EOEMcdklBDUy4p56QyO9elsybwzy42ibqdlT6ie3_44kFqssGNU7zSZfETte7e0iYsfX9RSc87QJt0OQqjL29w-INKRtD7eiV0D_7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقش شما در بدرقه (۴)
🔹
اگر نتوانستید به تهران، قم یا مشهد بروید با اکانت خود در شبکه های اجتماعی و انتشار ویدیوها، متن‌ها و تصاویر مرتبط از شهرتان در این بدرقه همراه شوید. در انتشار عکس و ویدیو از استفاده از هشتگ های این روزها و کپشن انگلیسی و عربی هم فراموش نکنید.
🔹
از الان شروع کنید و راویِ حال و هوای شهر خود در بدرقه رهبر شهید انقلاب باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666534" target="_blank">📅 20:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666533">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
تعویق برگزاری امتحانات نهایی پایه یازدهم به دلیل تسهیل در تردد زائران مشهد
🔹
به دلیل تسهیل در بازگشت زائرانی که به مشهد مقدس مراجعه کرده‌اند، امتحان نهایی پایه یازدهم که برای روز شنبه برنامه‌ریزی شده بود، به تعویق افتاد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666533" target="_blank">📅 20:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666532">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
توصیه کارشناسان فوریت‌های پزشکی
🔹
اگر در مراسم پیاده‌روی وداع با رهبر شهید شرکت می‌کنید، حتماً یک بسته پودر ORS (او آر اس) همراه داشته باشید. پودر را در یک بطری آب حل کنید و در طول مسیر، آن را به‌صورت جرعه‌جرعه بنوشید.
🔹
نوشیدن محلول ORS به جبران آب و املاح از دست‌رفته بدن در اثر گرما و تعریق کمک می‌کند و می‌تواند از بروز کم‌آبی و خستگی ناشی از گرما پیشگیری کند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666532" target="_blank">📅 20:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666530">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vwglro26Nn3eGq8wZevggNV60WqSxVUrMzKOuGoU7kcy4RVjxmLNR9igvi7kFfRjMSPbyVoHXxUhAly3tqJu10I5YZPYkeHoJ74WcYQO9LvffLG_mOjUk_I0E2o6sNn2kUx1C6gZttRsjilAuN4SPQkR16siN0yHWBuDrx9o6XChXbdfkc9NTjNnmFRde88m3ALYyKSn-nf2sddFGxspIXR563YcD3dNLOFIkoFFQwe2DPsLX0F17Xs9hZTpaju9CCsF_bOkvJkr3Mn9ahzfPTutoUn5Qrevn3x2N7LWVdRtXZqNvwHhJgcb2LPYNgFUP4pn7iGKIYy2TsTPVImxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G88AsN8dEmsUIOloCt1JEp8fNAhkbO6FGIygrqFsCubAUHMtHbFaI3RtWFTSla9ZGJDLqWp0cIRO8TPawVeZzuF1cjS7SwReV1y8wmkq6yn7m46CACLz9V3PdWrA_QXraaaOA72hRC5bMq54HR8ocUU_j-sdfxKR6DDwkNHTjWD-aAHKS4Uajm3iqlSrvuIj3cEhW9yzOHnmKqjXHqjfKdd3VK9rtvsZ-cgoYHl4SfEx3SyiYKSiCZsf-dlESf3uI23OpFha_ut9_5WD7T6hWqvR_A5e90K6g4i-WGp2pobVfKW0_O8481dyrxLMW74zDQWJoCllVyJsfs_JIPnNuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برگزاری نشست قرارگاه مرکزی حمل‌ونقل جاده‌ای وداع و تشییع رهبر شهید انقلاب با حضور وزیر راه و شهرسازی
🔹
نشست قرارگاه مرکزی حمل‌ونقل جاده‌ای وداع و تشییع پیکر رهبر شهید انقلاب اسلامی به ریاست وزیر راه و شهرسازی و با هدف برنامه‌ریزی برقراری سفرها در حوزه حمل‌ونقل عمومی و جابه‌جایی عزاداران شرکت‌کننده در مراسم تشییع به میزبانی سازمان راهداری و حمل‌ونقل جاده‌ای برگزار شد.
🔹
وزیر راه و شهرسازی از انجام هماهنگی‌های لازم در خصوص تأمین سوخت تنخواه ناوگان اتوبوسی خبر داد و بر ضرورت برنامه‌ریزی دقیق برای تأمین ناوگان حمل‌ونقل عمومی جاده‌ای در سفرهای بازگشت تأکید کرد.
🔹
در ادامه این نشست، رئیس سازمان راهداری و حمل‌ونقل جاده‌ای به ارائه گزارشی از روند سفرهای هموطنان به شهرهای تهران و قم طی روزهای اخیر و بررسی ظرفیت ناوگان حمل‌ونقل عمومی جاده‌ای برای استمرار سفرها و بازگشت از مشهد مقدس پرداخت.
🔹
معاون وزیر کشور و دبیر ستاد ملی مراسم وداع و تشییع قائد شهید امت، معاون حمل‌ونقل وزیر راه و شهرسازی، معاون نظارت و بازرسی امور تولیدی سازمان بازرسی کل کشور، رئیس سازمان هواپیمایی کشور، مدیرعامل شرکت فرودگاه‌ها، مدیرعامل فرودگاه امام خمینی(ره) و اعضای هیأت عامل و معاونین سازمان راهداری و حمل‌ونقل جاده‌ای در این نشست حضور داشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666530" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666529">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
خونخواهی، میراث کهن ایران؛ مسئولیتی بر دوش مسئولان
🔹
طلب تقاص خونی که به جور ریخته شد صرفا مطالبه‌ای ملی نیست؛ بلکه ریشه در فرهنگ تاریخی این ملت دارد.
🔹
سیاوش در فرهنگ ایرانی با مظلومیت خود به نماد جاودان عدالت بدل می‌شود و کیخسرو با برپایی داد، نه تنها خون پدر را پاس می‌دارد، بلکه نظم اخلاقی جهان را از نو استوار می‌کند.
🔹
ملتی که سیاوش را در حافظه خود زنده نگه داشته است، ظلم را با سکوت همراهی نمی‌کند و نمی‌گذارد گذر زمان، حق را به فراموشی بسپارد.
🔹
مسئولان این نظام به عنوان وارثان مکتب رهبر شهید و وکیلان این مردم در قدرت وظیفه دارند این مطالبه تاریخی و ملی را پیگیری کنند
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666529" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666528">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_FaLJ9l34sZmX9DNyta3O9CiOJpmmfzrzlSxWzOG5vCJNf-w2LL_--V0m4mdmWvab6troTuErQck6mgHGUKA7cFZX1tIRaLNDZVGVx1jsy8Srydmd_Q9LeCDTsemetXC8yUIGtxu_TmvJ6AtJZgBmMgzkBLMBawxUe-yFvvA0a139FQcXI6UwNHYn-Ce9avZtGhRiKR1BaFxwLlK8vIEAzcXiLRWshpoUsDgU6JZ9iq4J8lzXgvEN1wVU96z1BWttZWqDHZlrel7nLTaNMg3s_OV9oOcELIZIjPCitpGt1AM3EZSmO8dYYSJaiw_L0RwP9rbp7c9hFBpIT4mOP8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهان در نبودت دگر زیبایی خاصی ندارد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666528" target="_blank">📅 20:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666527">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
رئیس‌جمهور: وحدت و انسجام را در عمل نشان دهیم نه در حرف
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666527" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666526">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e948877e53.mp4?token=ZGJ-I-RyGq-ku0zCTDMwn-mX7cvwiiOQ8AeNjc4gp7utrLzB3vRRMbDTVnbher93J8FAsmX0oIGyUBerHk7p0RDdwuLvNf_de8n3I9Iox0gOzWjcOtdeD9QWAFnknjZh2PzY6zsfnhqPwM1my3hlBmuh5ewuwd1XgbA4WK7qktf7qnk1JZYlVucnfqZSJ_i_e6K1sn4DsHeNzOe0pw1irRVnAdX6NXwPL4vIJAtEa0y6OZU0RZ1fyNEUIFV1YDER78Uu5BNqHQy3IrArx9GmUESLHZfdBswA5oFJfBxAyc8LHCrdm9jPs2dbLuGAaujMJBR5qtIA3pTqQuq2moMoXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e948877e53.mp4?token=ZGJ-I-RyGq-ku0zCTDMwn-mX7cvwiiOQ8AeNjc4gp7utrLzB3vRRMbDTVnbher93J8FAsmX0oIGyUBerHk7p0RDdwuLvNf_de8n3I9Iox0gOzWjcOtdeD9QWAFnknjZh2PzY6zsfnhqPwM1my3hlBmuh5ewuwd1XgbA4WK7qktf7qnk1JZYlVucnfqZSJ_i_e6K1sn4DsHeNzOe0pw1irRVnAdX6NXwPL4vIJAtEa0y6OZU0RZ1fyNEUIFV1YDER78Uu5BNqHQy3IrArx9GmUESLHZfdBswA5oFJfBxAyc8LHCrdm9jPs2dbLuGAaujMJBR5qtIA3pTqQuq2moMoXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ازدحام جمعیت در مترو شهید بهشتی برای رسیدن به مصلی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666526" target="_blank">📅 20:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666525">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
نحوه فعالیت بانک های کشور در روزهای  یکشنبه و دوشنبه، ۱۴ و ۱۵ تیرماه ۱۴۰۵
شورای هماهنگی بانک‌ها:
🔹
حسب تصمیم هیئت دولت مبنی بر تعطیلی روز یکشنبه، واحدهای فنی و پشتیبان ستادی و شعب منتخب بانک های عضو شورای هماهنگی بانک ها در روز یکشنبه ۱۴ تیرماه ۱۴۰۵ در تمام کشور به صورت کشیک از ساعت ۸ الی ۱۲ فعالیت خواهند داشت.
🔹
اسامی شعب منتخب در وبسایت اطلاع رسانی بانک ها منتشر خواهد شد.
🔹
تمامی واحدهای ستادی و شعب بانک ها در کل کشور در روز دوشنبه ۱۵ تیرماه ۱۴۰۵ تعطیل می باشند.
🔹
نحوه فعالیت بانک ها در روزهای سه شنبه و پنجشنبه در استان های قم و خراسان رضوی بنا به تشخیص و اعلام استانداری های متبوع است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666525" target="_blank">📅 20:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666524">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنیرو آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdsXUyE7ZzJcKxDP1uBvlZMJeV1foYRVguo6mOWALRR77jp_nSgzoZBnr9xxVJuT0KHroEEzqY2Z9QituORO5D9ywmyaNMMLLSgPBpDfWW9amwIR6cMHAN7hRzYaZs5htnq-nrP7pLcH16_VKSSbYys_SxdA4W_4qTvXSEdxixGHL7PB64D82g3jze2d61pTtFHXUkDn87kGTkv6VgQnEf9WZGz5dchbUK-Q8p9auhgm31JiVX6Nc-U55-aX1DqrPY0JE4tYz8KemmZS5_tvJpS9gEt44F6ZUcMvyzhIy0eDHcGoS0O2e5QkB1oRbit37Ug3P7D1O_jT2pcrRVQjCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئول ستاد وزارت نیرو در امور اربعین و مناسبت‌های مذهبی:
⚡️
💧
توسعه فنی و زیرساختی صنعت آب و برق، با رهنمودهای رهبر شهیدمان ممکن شد / تامین موفق آب و برق  مورد نیاز آئین وداع با رهبر شهید انقلاب
🔹
مسئول ستاد وزارت نیرو در امور اربعین و مناسبت‌های مذهبی و‌ معاون پارلمانی صدا و سیما گفت: نگاه حضرت آقا همواره بر مصرف صحیح و به‌اندازه آب و برق بوده است.
🔸
احمد حیدری در حاشیه مراسم تشییع پیکر مطهر رهبر شهید، ضمن عرض تسلیت به مناسبت مراسم بدرقه و تشییع پیکر مبارک امام شهید و خانواده بزرگ ایشان، تاکید کرد: مسئولیت تأمین آب و برق مراسم در ستادهای کشوری به وزارت نیرو واگذار شد. این مسئولیت در شهرهای تهران، قم و مشهد دنبال می‌شود. در شهر تهران، در دو مقطع شامل روزهای جمعه، شنبه و یکشنبه برای مراسم وداع، و همچنین روز دوشنبه در مسیر تشییع از خیابان دماوند تا خیابان لشکری، برنامه‌ریزی‌های لازم انجام شده است. حداقل جمعیت ۱۴ تا ۱۵ میلیون نفر و حداکثر تا ۳۰ میلیون نفر برای حضور در این مراسم پیش‌بینی شده است.
🌐
[
مشروح خبر
]
#باید_برخاست
#عزیز_ایران
#صنعت_آب
#صنعت_برق
@niroonline</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666524" target="_blank">📅 20:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666523">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c500e8796d.mp4?token=p_2ZThcX73pEqzle1cDb2NlP3hD2Q26N1z51U20dI4VrU7vDmA2WveG0M1MEGo7wYDYbXbGlNTO5Gb8ulCqjk-Xn3xtGQ3jaXsrdo1FrOGHexUVTzTIsXNBY9yd0WLwCtOzwLU4NoVM1M21LFX7HGk6vX77evNEi9T9PzYHlYgKfCTXp6FuDdbB0uDhpST2jpgoTr5VBlsGd4ndh8bDKJm9YhFa4nxC98omI6bEfzFBj_OrkCWRoVnjqHajCwIullS3XrzZ_E0gWMYxChqb-BRLI7HLXglM1heA0EoYMGzTFdNtyfQ5tomCACwkEFabLyS7RUXa_LMflgm1_Sf4HlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c500e8796d.mp4?token=p_2ZThcX73pEqzle1cDb2NlP3hD2Q26N1z51U20dI4VrU7vDmA2WveG0M1MEGo7wYDYbXbGlNTO5Gb8ulCqjk-Xn3xtGQ3jaXsrdo1FrOGHexUVTzTIsXNBY9yd0WLwCtOzwLU4NoVM1M21LFX7HGk6vX77evNEi9T9PzYHlYgKfCTXp6FuDdbB0uDhpST2jpgoTr5VBlsGd4ndh8bDKJm9YhFa4nxC98omI6bEfzFBj_OrkCWRoVnjqHajCwIullS3XrzZ_E0gWMYxChqb-BRLI7HLXglM1heA0EoYMGzTFdNtyfQ5tomCACwkEFabLyS7RUXa_LMflgm1_Sf4HlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار مرگ بر آمریکا و اسرائیل مردم در مترو تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666523" target="_blank">📅 20:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666521">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NpXlgE_vLleSVszpj107nnKpS789RQRDiPZspvo09o8NqFLoQxUE9Sy2YTZ1dqAcf-KjSt48ZwExypMWH3DOn4IGSFc2_Y1US2HCtICIYevW0EhdMSsG3CmJGBBTNZDENma9PlYptaVuNwkuBtouDdXOFA44UW9TtF0SH8vQy-N8RLT8F3ylyrk5447f_zhVLJGtquaU2wwKgZn_fmklgAiUkxDC52q5qhB04JhYh67y2g-8XgC14nhKOGmPXZ1IY8RIDhqE6S3V_R6llk9DhgnBbX3bzgd5McTtd_vKzNouM69AuG8UUa5CmNltphDHvmQpoacCTtvL-1Tu-PJbaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSMNclHKCRvc0b5KG3GF3pOLrn3YTh3-Kz-9T5XhNhHOAW-mbEt53KvYlXN0I8Om60sETVvSCFy-fDNA7YuG_qzcTKIpSMLw_Cqyriis5961lO6H5-mEspk-6kGYKc3b_k9WDY8XPbK4z1wPIaQpA-B2cD6RmYnCpmxNEJmevyhSIlddMdutXbC5S4NB9I8JQjNxPYMrhE7jW4_I-_PlzCPetyN_dafaB-G4WTqPv6jcpVzPW509mXsNsYiukjSL76L-bnZZjy9y3Uapvt4BKP71rK0K1KHzrdmNUwL-f_Gnovq--sdLbaCli_-r1bB2FEyyG_pbzgIMP0n9oWOQ1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خون دلی که لعل شد؛ روایت رهبر شهید انقلاب از مجاهدات ایشان
🔹
«خون دلی که لعل شد» فقط یک کتاب خاطرات نیست؛ روایت دست‌ اول رهبر انقلاب از سال‌های مبارزه، زندان و تبعید است. نویسنده با نثری روان و بی‌پیرایه، از کودکی تا روزهای سخت مبارزه را با جزئیاتی کمتر شنیده‌ شده روایت می‌کند؛ روایتی صمیمی که خواننده را تا آخرین صفحه همراه خود نگه می‌دارد.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666521" target="_blank">📅 20:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666520">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
اسرائیل در پی چراغ سبز شورای صلح ترامپ برای جنگ علیه غزه
🔹
شبکه‌ای عبری گزارش داد که ارزیابی‌های رایج در این رژیم حاکی از جنگ مجدد علیه نوار غزه ظرف دو تا سه ماه آینده است و این امر منوط به چراغ سبز شورای به اصطلاح صلح ترامپ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666520" target="_blank">📅 19:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666519">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5608cabb7.mp4?token=Fgt-CkGkTHfryXOoHIC2_W_rikqVrT_iAOO4RpdPjelD0XJH9zFfSkOB14479M_2KF8JK4zb9WyMG2qQHW1fVCGq0bQggYobTDk-BHhssccsm7vJBnPDZU3LZOSzZKcpnw_01J8Du0SjXIsMdS7a5IE5FUara4KiUIIZI4Gd_lB8R0Y-AK-LOUDsXS4t84ySIiV1SrXyNdW9cqmRiTSVzFrCS7JnNJAatnShJLAJKjgGMVo7OqlvlGUZ8-pRBEQslPCMqpnwOTGd19HhFcIYUShwD4yz9G8D7awnrsl0gIfxPDJvclmhUmSwL2P3YWD53MlPuXNgengdc2JrvvB3fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5608cabb7.mp4?token=Fgt-CkGkTHfryXOoHIC2_W_rikqVrT_iAOO4RpdPjelD0XJH9zFfSkOB14479M_2KF8JK4zb9WyMG2qQHW1fVCGq0bQggYobTDk-BHhssccsm7vJBnPDZU3LZOSzZKcpnw_01J8Du0SjXIsMdS7a5IE5FUara4KiUIIZI4Gd_lB8R0Y-AK-LOUDsXS4t84ySIiV1SrXyNdW9cqmRiTSVzFrCS7JnNJAatnShJLAJKjgGMVo7OqlvlGUZ8-pRBEQslPCMqpnwOTGd19HhFcIYUShwD4yz9G8D7awnrsl0gIfxPDJvclmhUmSwL2P3YWD53MlPuXNgengdc2JrvvB3fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: من با رهبری شهید وداع نکردم و نخواهم کرد
🔹
رهبری شهید برای من همیشه زنده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666519" target="_blank">📅 19:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666512">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Du5AqvF7-f7zcofVSdA2p3kpTVh7vya4LA50HGCME-xe70XjsnNl_X1TogyundQky-P2RF1tbeqRxw7vojh82xq7pFwiV_FjvR7yWY9eHvFm5379HXsKieHHrZzbpAWc3bhADidinGvbgk5RbcRIHlETD3MCDgS_ikCkFjTnasxj19M-uEoz2UV6_mHrAiaLtQODPpexGNWDEO8lxMNon7QCA_kO-JZU9uUUNDNIDrOQXy2MmOUVTRVTEbJuvVzcW9ehD6vu8AZW2IKxPsahE_uJOaO04OirIjwYf9kLTYmmEWH1QLtLaFRxSG3glxT_hzmMuMSKMwgPuMNUbmEClg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOlpnPcjRTfW3gBpVtM061XPA58vojrRiUvQbiiRUWIofzNFPweXdg5oV83OI7FtoIlNpBd5F8kF6KBu8e9gN2WBYuWzLOkB-smD_SIamrCDKEnRNpSDtXXR7zVOfR4fw9YLjge17PyIrKlQk7FIosT_SZfwlTSIyJds-MGy64aR12DQK9DZcUfQopHSMHBNaWlZ7WDTaBB9gIo_t1AOmQmAj8_34s67drDs8_JrhQ1lP-LktnEpOX5wEMEGuWYwVNxzSlnVuOGAAVCtN8L-MVGtijFXQTS24ZoecdpEmcGFaxROI0goYc6wDYujkN_6YhXJzBdyYXDisgKXBg-esw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XbFsO7quRS2dEoo7_KIXz7mUpnPUT94TEKCHNmeOp4wiJT6uVdrzp_Me-FCZE0mnwyhaN1o7Q-m7zeqzcdX2Q0lalpRkJvXa7V0mWCWvBAqagdk6Uhymdszkb5EFCBCtXEJCU0hnG2N0BNehkTmhQ_om1YLINlKK8wTn7O1GRxRHH6e71diAAM7qGLjJLZV7lZZTDVlGcw5DCw1UTE2WNGhC4YzwTRF2KqFq9oUQBx6PG3zbTTeOoKtew3joiCXoi4MC9FlbqEsbh-QyaqVpbjFq5_UWCOaMnGh7OJy7vol4_OCIVqQy0yJeAkuuirrI-Kpk7BdELu9MYJbcZeNL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GRWjgGWZ9kCH70Rcoc0lYREAjYc7dQwJVOzalY5alVZqoyfF5B5AlfkZXTNzu8rH_odVzPtcncJgYlQVVVjD_v5WeYnLul69PbQypTlynhgWu-YaAqV707hdhUeJXJPslkK1xHo9dW45cno6nIkNaa1xtBbj3BKU3XzoB7xCotsc2BlU8GblSzWq-2wViZDy4qHfos42Y7it2rCeLZhIGmgIaQ_t0_QtKu9FVMl47YQSZt6hvoRHmTip5yJZcv_aPzxYglyQb3mS4Q5VgQzyKGVJJ_eYEndVy9YwQI98GGfJsFMNjlE-yv_JAWWpe4VPYCNvNEsqXje1mLSevkX-mA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cac4c39e7.mp4?token=NE5IYmHHuhinZRpL_m9xMOw0P3YkXJl0JQsY6IJ-nPKVHWEjeuGValVe1s4lpVo1HrQhPodw4o-voMUY4Ye8Dmm0I1WqeNXNFdW7FnW5CoJcRq5dXVDhHRILTG14AbKC3qWZ3JjrAkKP450d57af-oAAAHC2IAId9MRG0neeMY84QAgnzmcEYfr8E217L7Qd0Egr1QZtPIY2N5oP88YmcbniU1nIjgwbHl0I0vmAxmpJkSxfRdnQ3tWAy9au-6bZIusRhFXb2ZwJ6N5q11vmCfXlUfn9D9uQvHf9gA5BIZI91KrqwgYgEnz7PY4lWTJMjmTcNqt83bklbAMPUHHGAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cac4c39e7.mp4?token=NE5IYmHHuhinZRpL_m9xMOw0P3YkXJl0JQsY6IJ-nPKVHWEjeuGValVe1s4lpVo1HrQhPodw4o-voMUY4Ye8Dmm0I1WqeNXNFdW7FnW5CoJcRq5dXVDhHRILTG14AbKC3qWZ3JjrAkKP450d57af-oAAAHC2IAId9MRG0neeMY84QAgnzmcEYfr8E217L7Qd0Egr1QZtPIY2N5oP88YmcbniU1nIjgwbHl0I0vmAxmpJkSxfRdnQ3tWAy9au-6bZIusRhFXb2ZwJ6N5q11vmCfXlUfn9D9uQvHf9gA5BIZI91KrqwgYgEnz7PY4lWTJMjmTcNqt83bklbAMPUHHGAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ویدیوها تصاویر مردمی است که پدر از دست دادند...
🔹
عکاس خبرفوری: سمانه صالحی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666512" target="_blank">📅 19:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666511">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
اردوغان: جهان پس از توافق ایران-آمریکا نفس راحتی کشید
🔹
رئیس جمهور ترکیه امروز شنبه در سخنانی اعلام کرد: هر راه حلی که از سوی کشورهای منطقه اتخاذ نشود، پایدار نخواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666511" target="_blank">📅 19:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666510">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW34zeaLBP_Eiiijko85p-LOmQbLF2K3G66zMWYsX3vSAk2X9Q6r5GxR2flC7rsIzuOkoQasmn4fctDxl9XHmQB0Vg1EGM_Bt4vuqoLkggytQUB6mVnTYALdAJBEXX4QpFBX9S1w_he-cgmJL2jFwlB-oRHoKruVA0MjlToCsdqJMzedsZEiiwepeGAaUMkkj282KEAqCuHADRU7lqxXTVevBpltenfUP8CJ0smliISkjkOhZAN-MjP7IN2p4oSrOTAm7vhbBHj1GNtWFLf_6U837Ulufoxj5Pxwfta7SXUwTqZwBQZBArA0zd6po1ngghE98luiXilFQawHa38ByQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای روس: میزان محبوبیت یک انسان در آخرین سفرش آشکار می‌شود
🔹
میلیون‌ها نفر آیت‌الله علی خامنه‌ای را در آخرین سفرش تنها نگذاشتند و مردم جمهوری اسلامی ایران در کنار میهن و رهبر خود ایستادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666510" target="_blank">📅 19:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666508">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0145dd6a7b.mp4?token=BRISsvmYGOiz84Jknut6bhLuFiLD-o7mexPjz_0I-YNSWWotjPxbyM_vQyxM0D3OhYNr-AcQdvSep5KJCBNhxSKrGi2fMeOqpD4j7vAqqk7z0T6UTN2fnyfUcSUn2oDI-q3_fwk5rF116XOiZ7i8XCf-Tum-fqCrFM1J6R_TP7ukDw_0pBz_ER7kKS819T-xCi6tWvmNASal66mavJF8HNER7_xJ8ayLQwPTML8IoBmit-O41csFgOgcf-NDbv83tpfp8WBA49QzxsDSnBcG2P-6vY_7Lt-6sdo6F0leo0PbW2bU5do6GbHFZE7hb7PEAYyYXPxOHIAWZOM2KhmlnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0145dd6a7b.mp4?token=BRISsvmYGOiz84Jknut6bhLuFiLD-o7mexPjz_0I-YNSWWotjPxbyM_vQyxM0D3OhYNr-AcQdvSep5KJCBNhxSKrGi2fMeOqpD4j7vAqqk7z0T6UTN2fnyfUcSUn2oDI-q3_fwk5rF116XOiZ7i8XCf-Tum-fqCrFM1J6R_TP7ukDw_0pBz_ER7kKS819T-xCi6tWvmNASal66mavJF8HNER7_xJ8ayLQwPTML8IoBmit-O41csFgOgcf-NDbv83tpfp8WBA49QzxsDSnBcG2P-6vY_7Lt-6sdo6F0leo0PbW2bU5do6GbHFZE7hb7PEAYyYXPxOHIAWZOM2KhmlnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: من با رهبری شهید وداع نکردم و نخواهم کرد
🔹
رهبری شهید برای من همیشه زنده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666508" target="_blank">📅 19:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666507">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c315ef6a62.mp4?token=SRajLSA77hhxHe701oqCJVacT38Xmzf9uzXRekTgqIzZWKvBNxz5b5e3NBVA4bbCVWr7vm1ud3OKXbHBfozKd-b70gdAibOhufAJqt_E36ioD6-3lzui9kuY1rb1DKb05QQfcz5b798dgn687U5BaQ7a6k12ywdlA_lAmrCJuVEkfsOs5yZPuMOTwUKTKDJkBc-KyyxlUdSFftSd1aKEW1ONbgp3dQd9_98sZCAGTAWa8jWFRhD2L9Q4DkvF-ejjPBweAx1PLBIsaa5oKlFZYI-Xs7ogeX8iW7YNvVb3N_H2kMw9Le1sMmsvup7dXIokCVAbvllSg-WDuthrhD_fcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c315ef6a62.mp4?token=SRajLSA77hhxHe701oqCJVacT38Xmzf9uzXRekTgqIzZWKvBNxz5b5e3NBVA4bbCVWr7vm1ud3OKXbHBfozKd-b70gdAibOhufAJqt_E36ioD6-3lzui9kuY1rb1DKb05QQfcz5b798dgn687U5BaQ7a6k12ywdlA_lAmrCJuVEkfsOs5yZPuMOTwUKTKDJkBc-KyyxlUdSFftSd1aKEW1ONbgp3dQd9_98sZCAGTAWa8jWFRhD2L9Q4DkvF-ejjPBweAx1PLBIsaa5oKlFZYI-Xs7ogeX8iW7YNvVb3N_H2kMw9Le1sMmsvup7dXIokCVAbvllSg-WDuthrhD_fcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حیرت عکاس سرشناس آمریکایی گتی ایمیج از حضور حماسی مردم در مراسم وداع با رهبر انقلاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/666507" target="_blank">📅 19:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666506">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5700bf5c0e.mp4?token=vAvDgM204aBBJIGXrlCnytEs2Yq9ibr8qouc5LPyfVQKXLAVc-psopk0KWlotbRVJs-1tKTsxSeqRUSx6K0jfNrCrNEGBQWX_O24OJfK1vFq-vIedEH-kXZFJEHJrSRbID5qqTC-6PIbc_iUQO2RCdavr_TOzdPDtRPlKSJPjss7BjYM4w7BdXpjxgwR5KA4CM1m4VAgUFEEAgvyiKEP_UOPzQUap-WrHmytu_019OuyXJYqmlT_sXZFPOQf6l8Tr-lwGh0jir_ak2nPO8doLCzeA4gPYTjhIIfOlvgYozEhghWCECDjIb8crlbuz2wIHBrpazibAEK8aiTqcYT1_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5700bf5c0e.mp4?token=vAvDgM204aBBJIGXrlCnytEs2Yq9ibr8qouc5LPyfVQKXLAVc-psopk0KWlotbRVJs-1tKTsxSeqRUSx6K0jfNrCrNEGBQWX_O24OJfK1vFq-vIedEH-kXZFJEHJrSRbID5qqTC-6PIbc_iUQO2RCdavr_TOzdPDtRPlKSJPjss7BjYM4w7BdXpjxgwR5KA4CM1m4VAgUFEEAgvyiKEP_UOPzQUap-WrHmytu_019OuyXJYqmlT_sXZFPOQf6l8Tr-lwGh0jir_ak2nPO8doLCzeA4gPYTjhIIfOlvgYozEhghWCECDjIb8crlbuz2wIHBrpazibAEK8aiTqcYT1_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: رژیم صهیونیستی به همه کشورهای منطقه حمله کرده است، آن‌ها عامل بی‌ثباتی منطقه‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666506" target="_blank">📅 19:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666505">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
پناهیان: ما حاضریم تمام منافع ملی خودمون رو در راه انتقام امام شهیدمان بدهیم؛ ولی انتقام را بگیریم
🔹
ما همه هستی‌مان را می‌دهیم اما انتقام آقامون رو می‌گیریم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666505" target="_blank">📅 19:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666504">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b194b778db.mov?token=aqbNdJAhrDmkm_a8YiodfVhk5q1wqoue_Td2d_oP7YAkVaVA8zvyKuyYu0rjqbTp83UWmN10PJrqYKFdPunoPhmRFr6BFvXJEUx20oK9WBR48O8myZsVUn_8h6tCA7tdlKYPqkk7nafZd1iviIL2I_QthWKopg_-0wSVOFMvF1ge33F9OGdOJeiPDCfZeNQEUGMaTGVKT80kX6H0HoOnd7Bq0JSvZZh2w6Z7iAz8jxo86L5DWazPA0zj7SkmReDLfblDDfrywJyxTUY4RpLXcGO4IJE5Lq9o21MVH4Mhj4gHIS0MTS6TI7LETmWVL84BBLDjF9TVHY_5e3cKxI_DHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b194b778db.mov?token=aqbNdJAhrDmkm_a8YiodfVhk5q1wqoue_Td2d_oP7YAkVaVA8zvyKuyYu0rjqbTp83UWmN10PJrqYKFdPunoPhmRFr6BFvXJEUx20oK9WBR48O8myZsVUn_8h6tCA7tdlKYPqkk7nafZd1iviIL2I_QthWKopg_-0wSVOFMvF1ge33F9OGdOJeiPDCfZeNQEUGMaTGVKT80kX6H0HoOnd7Bq0JSvZZh2w6Z7iAz8jxo86L5DWazPA0zj7SkmReDLfblDDfrywJyxTUY4RpLXcGO4IJE5Lq9o21MVH4Mhj4gHIS0MTS6TI7LETmWVL84BBLDjF9TVHY_5e3cKxI_DHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقبال مردم از مراسم وداع توقف مترو در ایستگاه مصلی را لغو کرد
🔹
به‌دلیل افزایش ازدحام جمعیت، از ساعاتی پیش قطارهای مترو در ایستگاه مصلی توقف نمی‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666504" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666503">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df790d290.mp4?token=bBVyNvj3JDXLegXL7e3InDUwF_suh1SnwB67AIHn5v33j8UudokfC2z8oM5sdUu-_3z4lIf3hzlPvbyZmRTJFvjLM0pwFTmY8Wb58ynQ1pshFdT_hvk6AeGnLIc0OfQn9NrwCQ3-sq1RIMaVWjkqRjuVRysFMbBNcfjiiKX94Rl6mHmX3631TEAEdOwbV297I8A69l9psowVj-3JmBSkyt5KErZu0UK6sAPgsYRDKEo6gQNRbMk8XuH83LkN8t2-Ez8hzIc_rSz6QALMCxYnKdaDON1qrk-u9rahHKkaaBK3glQ5TAtHxheeCFF7FkFqKfv16Fcdej-vVVTmVNEkMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df790d290.mp4?token=bBVyNvj3JDXLegXL7e3InDUwF_suh1SnwB67AIHn5v33j8UudokfC2z8oM5sdUu-_3z4lIf3hzlPvbyZmRTJFvjLM0pwFTmY8Wb58ynQ1pshFdT_hvk6AeGnLIc0OfQn9NrwCQ3-sq1RIMaVWjkqRjuVRysFMbBNcfjiiKX94Rl6mHmX3631TEAEdOwbV297I8A69l9psowVj-3JmBSkyt5KErZu0UK6sAPgsYRDKEo6gQNRbMk8XuH83LkN8t2-Ez8hzIc_rSz6QALMCxYnKdaDON1qrk-u9rahHKkaaBK3glQ5TAtHxheeCFF7FkFqKfv16Fcdej-vVVTmVNEkMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: برای چی باید با هم اختلاف کنیم، برای چی باید بر سر جزئی باید زاویه درست کنیم
🔹
این علمای بزرگ‌اند که وقتی یک زاویه درست می‌کنند، در پایین مردم عادی به جان هم می‌افتند و مسلمانان مسلمانان را می‌کشند و دشمن از این موضوع سواستفاده می‌کند و ما را در مقابل همدیگر قرار می‌دهد. دشمن آدم‌های آگاه و توانمند را به شهادت می‌رساند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/666503" target="_blank">📅 19:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666502">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-YVsHtHSXxZmw65QU3AvZu8tBUhdnc2ufSlCVC1rtiWB2nNfnRZ6fHlFSQy7-xg4WjkacoLs7gGzR8C1XvlXvho9iaMopXUzfj8jREkJY9loj8zP7GPaXs7jo_Aj8gW6YJe8Fueyefy9Cqs0CcTAs5a284CQzClNj0e5FPkr8HG64c2KArjN5njgSiHevzbKKvLr7vHxM8K1npSqvWBD-P914Sh6LFC-Wmf170Eyc-k52PB4omotikV2eVY4DosHzgCA4byil7iXaz9O3ND6gMK57BPcY34EeCr0wEh0EqCMF0KL0vPqaWA2muzNVqYKvxYBsLyUd0B8mGYO47mcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان نتوانست حضور گسترده مردم در مراسم وداع با آقای شهید ایران را کتمان کند و اعلام کرد که جمعیت عظیمی برای تشییع و گرامیداشت حضرت آیت‌الله خامنه‌ای در مصلی تهران گرد هم آمده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666502" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666501">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
گریه بی‌امان دخترکی که با ویلچر خودش را به وداع رهبر شهید رساند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666501" target="_blank">📅 19:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666500">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfaf30c6.mp4?token=MKY9W1rD-0W5qRGVcQzuhD0ViT2EYzcmnahdiv-wL3oFRIMqqkQf6XOx7u81SPymy-GNafsbrcCfY49kFtQwlyD6MwuxgKla59QZj8xyJo_Sa6LJe3oxNjrU9pGuglKyW17ZfI4lmfpjaIBD2vBE2s-RPrk5AFxDSziAIGCq4rK9eTIBy1lOdRSQ5UkUSaE0UOsT1Z_Pcou_kgpE9VhK_bnPaWUFKpPfrit2-ZpbIKzxAuvwvWaFdz4mFzYxIOYeJhJjt5k8dKAlhrLRcl2Ar5uB1iKK8oewCwJ-3lt5bLGjchhJVW7b7361Sa8lhhT9nirLxwEFqj6y7wD37_OgTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfaf30c6.mp4?token=MKY9W1rD-0W5qRGVcQzuhD0ViT2EYzcmnahdiv-wL3oFRIMqqkQf6XOx7u81SPymy-GNafsbrcCfY49kFtQwlyD6MwuxgKla59QZj8xyJo_Sa6LJe3oxNjrU9pGuglKyW17ZfI4lmfpjaIBD2vBE2s-RPrk5AFxDSziAIGCq4rK9eTIBy1lOdRSQ5UkUSaE0UOsT1Z_Pcou_kgpE9VhK_bnPaWUFKpPfrit2-ZpbIKzxAuvwvWaFdz4mFzYxIOYeJhJjt5k8dKAlhrLRcl2Ar5uB1iKK8oewCwJ-3lt5bLGjchhJVW7b7361Sa8lhhT9nirLxwEFqj6y7wD37_OgTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رجزخوانی متفاوت یک جوان در مراسم وداع: از امروز موشک‌های ما با بغض این مردم پر می‌شوند نه با سوخت جامد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666500" target="_blank">📅 19:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666499">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKwby9bP_4dsWj1z13vTKvoWUBWFWguYkzZNuT6b2Coz1iMW6Ynfp1M2AZDTDBHsuN7F6K5IeuYN3s5eBVeC92EQJ5BcFCwJLWlATjrkaQ6F1tf3nZW6bdQrXswZl-CuSxnEAEVi9V0xhruesEMEubUqLs89rWwszJY4bluZ36lnhwIKXponUbR1PTiRbvTf3S-xu2CkQ8z7MeAfMr8ERkG3xtan__EHYi-zmHw4FoNOXsxF5Et1JRoioffte8YwcDrZxFRhDG4mEQThLQD-_R3gg7vw4EvxNcixCwsEhqNwbDg3TIGb3KMxpDdVTfuTNw3ShpcTkEtR6hHWz3mdmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی: خون رهبر شهید باعث بعثت همۀ آزادی‌خواهان جهان شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666499" target="_blank">📅 19:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666498">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
واشنگتن‌پست: مراسم بدرقه، نمایشی از مقاومت جمهوری اسلامی ایران است
🔹
رسانه آمریکایی روز شنبه با اشاره به حضور گسترده مردم ایران در مراسم بدرقه پیکر رهبر شهید انقلاب اسلامی نوشت که جمعیت حاضر در این برنامه، «نشانه‌ای غیررسمی» از حمایت مردم ایران از حکومتشان است.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666498" target="_blank">📅 19:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666497">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ملاحظات ویژه ایران برای چین در هزینه‌های تنگه هرمز
سفیر جمهوری اسلامی ایران در چین:
🔹
تهران با توجه به تحولات امنیت ملی پس از جنگ اخیر، برای کشورهای دوست از جمله چین، در تعیین هزینه‌های خدمات تنگه هرمز ملاحظات ویژه‌ای در نظر خواهد گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666497" target="_blank">📅 19:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666496">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVzn5PPLvTFHjWCO1WvGFywXMkimokELWpyyPvSOf6fy1AOy1aRKW_4UhBPU8AzGe3V46Z7Qr_OBe9sZs-9e1y2hcvDkCtsaDZD_SzNO5nqYH6JXzkjJOxx5aACLW8s_Llz_KSe6BJdWje1S7IGpXWnWui9HCiLBYE2NLiwnJMY7fkwHqj5RurSk3R3YRS8pB07TH0jCfYgYbNbDN9aG0jNoXQnQGq3u1WiRhhwP_XMFPdqNLSCe45LTcQCC4xNP0XICMyulQLsZFsgXGsNSlFAWPwAOIcZJVIUXAmYnJnk7KMYvirxY1hGjR3POvmEYXq76Uu171RpFwr-mFqkm-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666496" target="_blank">📅 19:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666493">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbksYADpSpQe15jxd_IH_iCbLrHZ300ceo__kpKIL5dQQZju-Cg_rUzt2BuGu6YBQ-ld7Udqc8QeGTeW2atmgUQorJTlCtzHbWGxuBdcyt6WcsRI3R4u9OSuPD9Agnc2kssOPO6bZhRDCBXWgvjDn5Onkhw-743cG309wwMvqUnMu_aIyNvAKbNPfENb_kWp3YGWl6zIs0utOfSi2BPV54T7aiPXh7Flde67-m3W9I-q5k_lDyimY9eMeS0Tdf6yhWI-kFHv3gHLhcgb35T6GnmZZNpbIiHgErZDPxaKTuDEbpfd7k_XRs46CCqe2mUM8PNp0Mygh3yVMknPfrfnUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfLRnyOStcJAEuvhRIds045MOue4sxfN1-NS4rklG7NnuCI9ixYdfr611nVYh0hAgicsAh2qBThwQ6ZT_LALg0QurNtIu6oNPWvWYLUNThXFQeANAJnmxQx3Um0KgmrcV-qF0YfEddJ0z1rczDCBpwpVNx4HXF1N4HrfTpQ7kUyX6xs695Oi5ptUqPhgzT-4YSvblbVRY2bsp1MBQVaXpkx7HLB6LefCYDz_kNPnLGn7wSRSFGpoVwHAu1jRWOzTtN5FzKKef0rbqsWBcgQnRgFNSCm4FkpjXWLFp_qXwiLeuJOzBzPMKtLKG3d7ATBdFMQY__d3UNPIgO9bMlRrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fiWYQNoJoh8iAa5BUAUNw89KWenwGx7cXFhgAs7oCkkL96w1eY8ttrzCKGNqNqO4ns9hvOjba9LEGyvYnnYI1sL6xbxpbjAQAWlfIx7KV0h_uzYDzuQjnnKme7hOgWZsL7Iiu70sHrTk9a_-wfWFquy1Khz7ck0CyRY2zExLIVDhyllOpwJ4EZaz1l00Dcq2qBWFF9dlKyOFS1eETbIZssnXWaOx1-m9h_JadzDK_WqXj4mtrLt1jlpdPnFSEh3LgCJzpcH5p2Q5oFBOtptuHgBiSakmDan3U2cFAzehjyUQeYAduKiZUo00UyxfW-IYDGZ5CshObeJcqppm4VNzrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حرکت مشترک سه پلتفرم نمایش خانگی همزمان با مراسم تشییع رهبر شهید انقلاب
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666493" target="_blank">📅 19:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666492">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry9ENv6F1eB9dBiI1Tvhm4vlObdyaOSULG6ETvLacJcmeP1NzwRfksqshv-kpA-stUaWt0eHjHZUKs5grkwdlEUNegRe-L5plvzdAUlodkH4WeZlexTpE8Zn7b0EMw45NmwJ3YS-g2G-e4OZWDdT6x8r4tYOTenOgVMT9WjGZLyMa3oqjBo8QXpm3q0nUYmosjG_t4hVaJcDDRiAVs0VIP0hEED5RWFtTUV2tIZkwotsjWHSrtZP7KetoLvfJ5dLS7FnfQ2P2CCiSANGItw9qVzb6ahxWzUOYOkru-TkpQ2FlJe6Oj4PwBvNry_8TokKuM3d5X_c1JrtDLxgiKQnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میرمهنا؛ نماد مقاومت در خلیج فارس، الهام‌بخش امروز
🔹
میرمهنا؛ دریادلِ شکست‌ناپذیر خلیج فارس. زمانی که قدرت‌های اروپایی برای تسلط بر آب‌های جنوب ایران رقابت می‌کردند، او با ناوگانش در برابر آنان ایستاد. با بیرون راندن هلندی‌ها از جزیره خارک، یکی از بزرگ‌ترین…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666492" target="_blank">📅 19:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666491">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d664908bc4.mp4?token=o1Y7z2ZHWFEo-kq0xJK4Z41Zkp1zEqrUbHZrilVWxUYdwlGhl48i9irEenKSkKUT4VvYnQYgrXkblyQoE-9015u88rfwQIB8LaVuE1OQNvGwT5Rv6WBvuh9wgiz8tQD7lrPPc1hg6VomDssmazgaftd7AavB9AsfwDdoZvNtjCI5L_cgJMk0WI_tlRyCn9dSnitAueQe5FwbAhgKWYGmKaPPcPbnb2og6xwfpJw9JPK-8yVx-kmLvKy8urdJjDQIb4ds58wkqXOMjBEjYYC82I5nQDD7gQ4POEPNz4ScQBGHc6MpOa_ri5974RjQvrHShrAovMFHHY5A5NdCak8rpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d664908bc4.mp4?token=o1Y7z2ZHWFEo-kq0xJK4Z41Zkp1zEqrUbHZrilVWxUYdwlGhl48i9irEenKSkKUT4VvYnQYgrXkblyQoE-9015u88rfwQIB8LaVuE1OQNvGwT5Rv6WBvuh9wgiz8tQD7lrPPc1hg6VomDssmazgaftd7AavB9AsfwDdoZvNtjCI5L_cgJMk0WI_tlRyCn9dSnitAueQe5FwbAhgKWYGmKaPPcPbnb2og6xwfpJw9JPK-8yVx-kmLvKy8urdJjDQIb4ds58wkqXOMjBEjYYC82I5nQDD7gQ4POEPNz4ScQBGHc6MpOa_ri5974RjQvrHShrAovMFHHY5A5NdCak8rpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احمد نجفی، بازیگر: کدام رهبر یا مسئولی در جهان، مثل رهبر شهید ما با علاقه و دقت با اهل سینما و هنر تعامل داشتند؟/ هدف ایشان ترویج فرهنگ و هنر در جامعه ایران بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666491" target="_blank">📅 19:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666490">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
حمله بالگردهای رژیم صهیونیستی به جنوب لبنان
شبکه المنار:
🔹
بالگردهای ارتش رژیم صهیونیستی در اقدامی تجاوزکارانه، مناطق مسکونی شهرک «مجدل زون» در جنوب لبنان را هدف تیراندازی قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666490" target="_blank">📅 18:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666489">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
تهران؛ کانون وداع با رهبر شهید
الجزیره:
🔹
تهران به مرکز وداع با آیت‌الله خامنه‌ای تبدیل شده و جمعیت بسیاری در خیابان‌ها و مصلای امام خمینی (ره) حضور یافته‌اند.
🔹
این رسانه همزمانی این مراسم با دهه اول محرم و روز استقلال آمریکا را نمادی از تداوم رویکرد مقابله‌جویانه ایران در منطقه توصیف کرد.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666489" target="_blank">📅 18:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666488">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ایران یکشنبه تعطیل شد
🔹
هیئت دولت پس از درخواستهای متعدد از استانهای مختلف کشور برای فراهم شدن امکان حضور مردم در مراسم وداع و تشییع قائد عظیم الشان انقلاب اسلامی و با هدف تسهیل و امکان حضور گسترده اقشار مختلف مردم در آیینهای سوگواری، روز یکشنبه ۱۴ تیرماه…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666488" target="_blank">📅 18:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666487">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-A9SLbrT3M1BZPFM6HsEw9-NxgSy_6c0_zWD_6bCriqlQcMRlDpqFw8Wg2B-VpPq0N0c989Qpk_ThsNV2FUhKq8aC4gF0Cfr-jBSkNVXRxaCnaCmO3p_fL5UezfaoCn0oI9NUX4R3eDuI5DjTSd6t_IWMYfr9OafdArDCTWXGAWzNfx9T5N7kKuhpmMLlo05x3dPR_zioKqWkb5PRGi2vrHwMHxJBI3ozK-36lnJf3OC7ZG_2uZO2xFxV9u1DZtFQXPbkLYf7DwxxtjmMQn_a5501Znecn7tR5L-L5IXPLQTdua8AqvGJYMcYY9uN36zQBsYgx7eBcXhrsyltWswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/666487" target="_blank">📅 18:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666486">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqV1hwhtpxDH0KY_Tsnkt6iFW0wlgEAWE5y42ALugAPd7ug9dUFGo4jZFhvif5yuymbL3bn97QqSZGfvDocBgC_OPJZkNE2wIIunGbb1fvm9RuPKdVG-5HKiLEgBwqsJsWWu16yV29AS4k4HuMDEh9SGdffXfBb8Zfiszmd6l8ACcQ9nHsABXD65yA7KTmfHJHvKID96GEib3CSDXJ2kuTAd4xDqbQcASXCd2zJ-bDLql2_T0ApmQhl1B9y5k6l7GI4kq_T0peiWfN2PTDgrl8rfrxUZxyRiZip9XbiCeonyYMzN_0QNpOYLyf9od2HKp7G2N9S3lJmegeXcAXyE1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر خبرگزاری فرانسه از مراسم وداع با رهبر شهید در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/666486" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666485">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
شمار شهدای لبنان به ۴۳۰۳ نفر افزایش یافت
وزارت بهداشت لبنان:
🔹
شمار شهدای تجاوز رژیم صهیونیستی به لبنان از دوم مارس (۱۱ اسفند) تاکنون به ۴۳۰۳ نفر و تعداد زخمی‌ها نیز به ۱۲۲۰۲ نفر رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/666485" target="_blank">📅 18:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666484">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15bb4eea1.mp4?token=taxlt6Y1wtiZRAt0igRHaYOXqMoWzA3pDCdL5t21E6Wkg2q_fPcC_10Zd3ygajZeD3DvTTNx9D91UNA-WpjV8UmByxnUxmQb7bQKZb3Nv4pRASzFn6TFKQy_I3KynLyZsm1gvcHAQBUpNR4Gv00-WYaderiO3fQUfiRXJiCMImfL_HQlKhJG4C9ZLkY0BfsDPpoFA0_oJ7H01Q0JZyLGpadgDlu0verF-O9remR_a-07g8UXT6aKbgTKLIAqM2DSMRRQ2rEuLDH-twO1zf78DVf8hSQvghidTFJt0sxC-kO4_-gTtIwKozv9CYOLsyQUI7zZmMgHXwsReyyxc8TT3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15bb4eea1.mp4?token=taxlt6Y1wtiZRAt0igRHaYOXqMoWzA3pDCdL5t21E6Wkg2q_fPcC_10Zd3ygajZeD3DvTTNx9D91UNA-WpjV8UmByxnUxmQb7bQKZb3Nv4pRASzFn6TFKQy_I3KynLyZsm1gvcHAQBUpNR4Gv00-WYaderiO3fQUfiRXJiCMImfL_HQlKhJG4C9ZLkY0BfsDPpoFA0_oJ7H01Q0JZyLGpadgDlu0verF-O9remR_a-07g8UXT6aKbgTKLIAqM2DSMRRQ2rEuLDH-twO1zf78DVf8hSQvghidTFJt0sxC-kO4_-gTtIwKozv9CYOLsyQUI7zZmMgHXwsReyyxc8TT3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر حسن ابوالقاسمی: زندگی رهبر شهید به قدری بدون تشریفات بود که می‌توانستید تمام وسایل خانه ایشان را با یک وانت جا‌به‌جا کنید/ رهبر شهید اجازه کوچک‌ترین فعالیت اقتصادی را به فرزندان خود ندادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/666484" target="_blank">📅 18:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666483">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
مشارکت ۳۰ میلیون نفر در مراسم تشییع رهبر شهید ایران
نشریه بین‌المللی کرَدِل:
🔹
پیش‌بینی می‌شود طی شش روز برگزاری مراسم بزرگداشت و تشییع پیکر رهبر شهید ایران در دو کشور ایران و عراق، دست‌کم ۳۰ میلیون نفر در این مراسم شرکت کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666483" target="_blank">📅 18:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666482">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUl0-RMfxFtqkwfurUwSgDJSxQA3cqnxV9azdnwq80_mb8YUMJzXcD6_qcFU7CMvEbLEgFI6_Z93LDosImUYLWlMiH5QeLLxkDjMLqtHI6oRS93ZdgUkrh_ycMyd4_E2iZq5HjpKIHpocA-kHUdIpzIP7Kr_DprNUA3aeHJ09daeQwo4sVd1sAHHnsHOYpHyM1NMRUyMxHIPH5PSbdOt9SQitKGQto2POFHJG-RhXh8wnR2hsdNwiHfo5txVBiUWROqRoS8xF1FOxRunFTWrgifPcHNhhNInwXABK043xQAExLu_o0cd_Zm7u8JEopjKS3-4hR4HfGHNq1WC2QLO_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط بالگرد نیروی دریایی آمریکا در شمال اقیانوس هند
🔹
یک فروند بالگرد MH-60S Seahawk متعلق به ناو هواپیمابر «جورج اچ. دبلیو. بوش» در شمال اقیانوس هند سقوط کرد؛ از چهار خدمه این بالگرد، وضعیت سه نفر مشخص و یک نفر همچنان مفقود است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666482" target="_blank">📅 18:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666481">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCxEI0PR3HTF4Ot8-u2twVyIgJNggFtHQXWOJFUE8USsDZey-4Wx8-KJRfulDyZusgh_jCqLUgbPPHqc0zzslQLouKE5mHwq3S61cL63ufiCiod-e3lwbulyo39u80JNbOUE8gWH-iJh51W-KMhgUEsb4OVWacQ0MX7IEsLLWaoprUUqpQXKlLUq8pe8TEkseK0a4krC6dpa6NpQDKUuJyO9p00B9hTCRxydQSNXgB2X7vdBNZWJmxIgwRlR3BQt11cofGbHKKrvTY-YtRdwczPielaewl_G9Xf51kieqG8ZxlicLnQ70Q2vkEc6n36DbNqMdUk3zK_Sox4WY6_XGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچم خونخواهی امام شهید توسط عشیره عطاشنه استان خوزستان در مصلای امام خمینی به اهتزاز درآمد
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666481" target="_blank">📅 18:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666480">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a0f3176.mp4?token=QPLJ4X2-YIoqMX-Dic7oHy6lPZyIApVG5w5r8vsSEV3xYtvarWvoKjbsJrnxgVGGWcbm5qpFm-MZf-mvoLB5XagCKdjqRaJz7LzwnUXy4_0-jvn2kxHtaZbqp6igZAaYyKiug_8ctyUJEQopRa9dAhEovU6xiHBUKMxkN0Htp0OoqUI5b1WGxxDdJEIfBp2qmnN4kaGm6YYa5XkTIE9vY_yGLEWgpvCvPtjUmUx3edq3u7JT92-WhVNPljBScqaYayuUOIPqlkzvnz7jmkwhCUc61apKchltwY2clDOIiEB03IQLFRQAQKCunVLxbQRiwCSXebBXB9rZ_3r08TWJXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a0f3176.mp4?token=QPLJ4X2-YIoqMX-Dic7oHy6lPZyIApVG5w5r8vsSEV3xYtvarWvoKjbsJrnxgVGGWcbm5qpFm-MZf-mvoLB5XagCKdjqRaJz7LzwnUXy4_0-jvn2kxHtaZbqp6igZAaYyKiug_8ctyUJEQopRa9dAhEovU6xiHBUKMxkN0Htp0OoqUI5b1WGxxDdJEIfBp2qmnN4kaGm6YYa5XkTIE9vY_yGLEWgpvCvPtjUmUx3edq3u7JT92-WhVNPljBScqaYayuUOIPqlkzvnz7jmkwhCUc61apKchltwY2clDOIiEB03IQLFRQAQKCunVLxbQRiwCSXebBXB9rZ_3r08TWJXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احمد نجفی، بازیگر سینما: سکوت در مقابل شهادت رهبر انقلاب مایۀ ننگ است/ همۀ ما مدیون رهبر شهید انقلاب هستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666480" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666479">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تشییع زمینی پیکر رهبر شهید؛ پایان مراسم وداع در ساعت ۲۰ یکشنبه
فرمانده سپاه تهران با تأکید بر اینکه مراسم تشییع پیکر رهبر شهید به‌صورت زمینی برگزار خواهد شد:
🔹
مراسم وداع تا ساعت ۲۰ روز یکشنبه ۱۴ تیر ادامه دارد و پس از آن پیکرها برای تدارکات مراسم تشییع منتقل می‌شوند.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/666479" target="_blank">📅 18:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666478">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
جزئیات مراسم تشییع رهبر شهید در قم
🔹
طبق اعلام کمیته برگزاری، مراسم تشییع پیکر رهبر شهید روز سه‌شنبه ۱۶ تیر، از ساعت ۵ صبح با اقامه نماز در مسجد مقدس جمکران آغاز می‌شود؛ سپس پیکر مطهر از مسیر بلوار پیامبر اعظم(ص) به سمت حرم حضرت معصومه(س) تشییع خواهد شد.
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666478" target="_blank">📅 18:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666476">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f42a2a3e.mp4?token=v6OpjekV5E6srNF3RvqnPwGK4q9x3P0gH3QE-O_elbZ-MNxl83FJ9pTYcATsp8T_ykpFxllIVOBgQDUJaZLFlAELNt_WruLl9nIeOfoyMYYbDUfZCMhoVPvU6jBFaj6CIC45DaZ6neLMrHLuEhJq6ByUD3qE_mSLkXVYxaADX8TSO5G4GoGsO2Yc_mldGS3jNHRqEp_yTVl_zcN0FvfKQOOdvZgSr7ir1U9Cr4DQm541QzlefqkLSxPO0CbrYO7iPyS3WSt323NAlIb-o95DsptHK4BQmZ2fK7Tc0kUPh06Cjxv303sNCv29R_uhHQ4-yaKWezOu0Yqphzx2KkCq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f42a2a3e.mp4?token=v6OpjekV5E6srNF3RvqnPwGK4q9x3P0gH3QE-O_elbZ-MNxl83FJ9pTYcATsp8T_ykpFxllIVOBgQDUJaZLFlAELNt_WruLl9nIeOfoyMYYbDUfZCMhoVPvU6jBFaj6CIC45DaZ6neLMrHLuEhJq6ByUD3qE_mSLkXVYxaADX8TSO5G4GoGsO2Yc_mldGS3jNHRqEp_yTVl_zcN0FvfKQOOdvZgSr7ir1U9Cr4DQm541QzlefqkLSxPO0CbrYO7iPyS3WSt323NAlIb-o95DsptHK4BQmZ2fK7Tc0kUPh06Cjxv303sNCv29R_uhHQ4-yaKWezOu0Yqphzx2KkCq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن محمدی‌پناه، مداح نماهنگ «باید برخاست»: مردم در تشییع فریاد می‌زنند که باید برای خون‌خواهی و انتقام رهبر شهید برخاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666476" target="_blank">📅 18:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666470">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5wqaaImoYNyO9JCeqLK_914ZwqcbDj-NGJVxHYXLGrC1LTG38yZuW1oj5XRxfsQ6pmAioFCGFk3lQJ94Ruk-AHMnfnvc58YFZ7GrfxzM9cp8mCRhHzznzKrEIpzHxl5koHCV6hh38gaGU-ws03NkgWTQBj-5v7Zq32A20WTqOSr4S58LhSEI_jm5KsJuAy2lhSqPqDQNOYsB2_XIt1mJT-6lrBuFx-YmPuOI8aDoGVlkEIP9OiHRO5SUz89YfOLFerqwyaj957cNRjnmVNinZ3aFDFJ8IRVFWBh7EFEwf4GCvQwBl1qMmpYCNFVnpdyKpzoSCsR15_h30lfPr97Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPTA_7m68Vz4DDc8c7to6VBnQLmi65uEiohDzEex4nFLUkRv1DxDL6FJDrnuHIvqX6RVXeE9I7XuADFKv-SsUcl6yhTewdNmg72H2XaA6bMvcSLN8Vnip_dLlrW9aMnqi2yM1ckrgtlj9SoIV9i66ZaXkjjKVjqmDRYSsBMnOBvPFglGOlqEqhlPfzrpFUeIcAw0oHjXTOEPr5118gutv2vFbApPdVSkLc3Z5VU9nVvuiKcSxRLfEU-BSXJK1s6T7wenPqDw7-lODoJvGgPvn209jDdVWjZex4CuJaygmX09JMK7hkdZnPfqp10WAhGc1K6KP8fFlhZWzDLS_tuqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PqoOVaUZBQwW1SmNH1UFbQgOf8Qi5K-GUs40roftxBw-GspMYZfDiWUDv2iowIeZW03UZUcR55mS1CY-YuGFMqSrfoWENtIUIbxBrCh-keE4Na204GWLW-MQWZ35pf5ax5gUPwurJCX96hWyPEv78gPxUD9tX0z-0Q6THilSiw-EQTP0ZEV7zbN4tLOMfrE7DnwwNz1SBUF7dcWfU-VM6l9dakNYvRGBdYcxATDf2Entn7BaOa0ztzOxYz_rvNVfM9MdsdQEY60THAyfkSW6FQX2ffTYPj2rZqfe3L1cg5uN2telQ_JDyOgtUCYrRLRWAvUJGQEK-YY7-oargjmKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQzxZTXjLMVmJJD6sgqFQPuf0Pf54ZL42AMhh_80TrnLwr-ljFOu1hCOJ__6XZkqKGPSCJg-ung1-BEhU_itqTwPxIUOo3RBNGunxom11CNrZ4MjqAOnU-uy1rRcNnSkwbBDQJ3TFxfaqcnZwDJLeHm5NwhoAX5inlg0Rv0hKuTrDrKQPf9qaxceHo1PktTNgNDm0_vJXhqDBHFzvkU_iAtnxXhsUzjGX-ZI9_xysnlTmOoL01O81GprWVD3neaOMe3dnxwu2jAWWGNwiQSpseBcYWcPjn5KLYEngbVeizTwJjj4IsrjKwP21MxpyuNRAwl4L2hJh2-3KEEQ2WaxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQqrwSm34bcg1PBs6p1hrujwEuH1OhQQ_gJuEXjLPCGQorbgKSHhutQMUaj6VBAGhUN8l3kGOLIvF1P9lZVOLyT3O0eIyVsrdWwmUkd-8n6Efh9mZA0miqBSWfh6D3IUqVGsAMWL-Xz3ie66DEjA28WfL0x5FBxueAwitIp5RkoICd99f0ruNHA6p5ES-jmocp8CwcnxdtUTfsFe4CdqK56AabKMTXWNbtIfjoGkIJvDtGdOOP3xiKLMHL1Dfs5ml-bzsr_UPyCsdM-VQ84S2JMFZxy420yJCRMcnqmDeOFb6z3CYp9rmsZtBVkeiNV_Wj9Clk-gCkHzqfI7moKepQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFb501NoJzy088qDPI0f-LLzp8wT11e1lMuwEW-jH0Y-GK6aal-iAH_BwIHvGO9sxcoM_0BkWjqM2Yqajt-sCF4ZBYo_-dGeLCIzbZcduZ--8UURPQE-iHZtePD72G4axBlKGTiEvVprVcTlXAeGPkYeWzLE7sS6jhcjNn2KnF7yi6K8uTk1Ck0RYKhyLAfKForv4t7QEL4JrfVYq5NYxAVMn2gJrKAEo-xEUyH3Ey7evoCOhvN3jz7fODGLkA5QA7F5RFaHCgr36PaUivI4Q4onRsIg3pG7VsIIcGJOZd3dZY-vw67NsESeCeluNVLH2R2GjH8WF-WSky-Rk8aL6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از مراسم وداع با رهبر شهید در مصلای تهران
🔹
عکاس: زینب سادات اسماعیلی طبا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666470" target="_blank">📅 18:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666469">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvaedDSaNQnlO-MoRLc2LhzeIerOcbiQVJUazVu63vC6uDIZYFxONdPL4lYv2d9WMQmmxLfqQW3unqZivePFpk2ftRE8cKjK8sEwWfLZxwku2PwZDURVYoicZtD48kHCRR_inGBE_Ftmnbh5L0fFG2e8DOXL50tqbrXA6p0FSyaraakUDFAusnebkrDKqQQaFOSgXtnWAoKraXH5cbTuB9oWyVIX7v5enkIWNCJVD2Q6IM3kOsQHMllHgGOtjltwXrMQuQ_hKP65bCtfLygvOqINFuiPH6NE-jvQLODwicTut62NfTvqokNOuV5-6As0sLDDStPvXcXZmE91Q4o71Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوچک‌ترین وداع‌کننده با رهبر شهید انقلاب؛ نوزاد ۴۴ روزه‌ در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666469" target="_blank">📅 18:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666468">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CveiMGm7P7ZTNvwSKZ8_qxIyP874zBDAWCxLHJYOnSmZjExnWFv8rjvnr88l9yRlGTzsNLahtcSRsWLDQiVJIcqE8CzjRqjjQJpPoqOjluWqAJzcN44wlZFVdk_VeVDmZhu0ZCNgAWQ77P61E-O-_f0kYBj51gCm3VAfn8YglqYCFpYr3rrjsAMQV5JvZyM_100bNXK4uvNAJj-8-aDBXxdvEuaVeYLL2o0dWLfB-0N8_HprTH_1IZ2X3p48GLLttGT96PLv70vrwEcWQ6k5u0n4Ytp0YcLvk4JrmjXBo6ju0Dqh6aam6_stglIKZutI_5q9Gjngxm2aF6CWhhtuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی ستاد تشییع رهبر شهید ایران: دولت عراق برای هماهنگی مراسم تشییع ستاد ویژه تشکیل داده و گفته شده به خاطر محبوبیت گسترده، کشورهای مختلف خواستار میزبانی مراسم بودند، اما به دلیل محدودیت زمانی امکان‌پذیر نشد و در چند کشور هم مراسم عزاداری برگزار شده است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666468" target="_blank">📅 18:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666467">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مقام ارشد چین: به توسعه و تقویت روابط با ایران ادامه خواهیم داد‌.
🔹
اوکراین ادعا کرد بیش از ۴۰ درصد از ظرفیت پالایش نفت روسیه را غیرفعال کرده است
🔹
قطعی گسترده برق در کوبا ناشی از تحریم های ظالمانه آمریکا ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666467" target="_blank">📅 18:07 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
