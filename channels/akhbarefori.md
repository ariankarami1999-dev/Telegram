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
<img src="https://cdn4.telesco.pe/file/jG8lb3WrLKFdL9tZMulcP6Pi6-_bKDPMzqvTsBq4TLAj2tALaDJCEtYI27Fpln92udpfY-TVzldOw3twUQWFH6TEQyiMYGtGyvOvsalMrk9Schd5m8AF8o2BD2HjwViiRHoZlsfKIyTA5CymoHdTL6D8vPam_a4Yow9fffSYuyjoIuaW3BZT0wcld-mOOy14uSvCkyNQjWKGFGXK5q6ZctdloOFqwk77motg4-cqnvAzHDYswGtk3OtSOSPhTsxx-kxni0weC4ZCph3j_Ob8GEE-npklHVOeCzC2uYqrr8pFLtkgQDBBWwjfrIeggQq027KdTYCtQr6qI427q48nDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 09:50:01</div>
<hr>

<div class="tg-post" id="msg-678268">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
امکان نوبت گیری «سنجش سلامت نوآموزان» در روزهای دوشنبه و چهارشنبه هر هفته
رئیس سازمان آموزش و پرورش استثنایی کشور:
🔹
اولیاء که به هر دلیلی تاکنون موفق به نوبت گیری سنجش سلامت نوآموزان نشده‌اند  می‌توانند هر هفته با مراجعه حضوری به مراکز جامع طی روزهای دوشنبه و چهارشنبه، نسبت به نوبت گیری و غربالگری اقدام کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/678268" target="_blank">📅 09:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678267">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1e9ea989.mp4?token=KkMkQWWfE0cMYDDs8H7JXxO5sILmcyB2iraPtbydXyY7ao7Fs_xDTneJZ_TMPk_NnqbDtlQEeXJXTOjIfJ-Y9jf9mQnikMzyKyy1XAaXbkxIYYSNCHQ1OaTq1WpCTtEWWUGPfztvlVzFOIauOrkWATuDfycT3v0EWrlwH4UEoeNBihj3c2AvsCUcXmdgx2Y5HeAUVLY1x0gIkv6WeRRWtuT99JU6PqO9OjmLz6vo8FNURzZ-UIvYDhtTod_cBhwnpkkNudwMaBGfy2UCIXalPbvd2kCUyjgkmZCYmlPgoPH8PlnuQXl9fkoCXHvPP6blfTjmJM9Xim_Yp3N2qTHRxjYe2N5XVVZPxVIHWMTzaPGr49BAVxKrcst1RSXh7p-k-WakDhc5TtdpraaEbzqSYOCO-gtdODCj3OIRIqGl6M-akHDs1UNpkkJFoppQqpH1pw7sQBDKxk58F-PAAArVXdV7smUcAxs1FFS-RHG1vTDN_TFX454MkXIZbIsbXtA9yqo73wdPS9ziwE6KnzUKJlphiwweIboQHZ3EWNum4BA28UsQd97NC_3lOXSmKi0bdTz190cuSE8dbW8SSmgbSRFDQInGujYJKKGgQwJn9oPwII4TB98BCsYyYDfZpa3KrSN-RS7W6XZuujJw-12luAa-6IeR-YvjgG2_NzSx3mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1e9ea989.mp4?token=KkMkQWWfE0cMYDDs8H7JXxO5sILmcyB2iraPtbydXyY7ao7Fs_xDTneJZ_TMPk_NnqbDtlQEeXJXTOjIfJ-Y9jf9mQnikMzyKyy1XAaXbkxIYYSNCHQ1OaTq1WpCTtEWWUGPfztvlVzFOIauOrkWATuDfycT3v0EWrlwH4UEoeNBihj3c2AvsCUcXmdgx2Y5HeAUVLY1x0gIkv6WeRRWtuT99JU6PqO9OjmLz6vo8FNURzZ-UIvYDhtTod_cBhwnpkkNudwMaBGfy2UCIXalPbvd2kCUyjgkmZCYmlPgoPH8PlnuQXl9fkoCXHvPP6blfTjmJM9Xim_Yp3N2qTHRxjYe2N5XVVZPxVIHWMTzaPGr49BAVxKrcst1RSXh7p-k-WakDhc5TtdpraaEbzqSYOCO-gtdODCj3OIRIqGl6M-akHDs1UNpkkJFoppQqpH1pw7sQBDKxk58F-PAAArVXdV7smUcAxs1FFS-RHG1vTDN_TFX454MkXIZbIsbXtA9yqo73wdPS9ziwE6KnzUKJlphiwweIboQHZ3EWNum4BA28UsQd97NC_3lOXSmKi0bdTz190cuSE8dbW8SSmgbSRFDQInGujYJKKGgQwJn9oPwII4TB98BCsYyYDfZpa3KrSN-RS7W6XZuujJw-12luAa-6IeR-YvjgG2_NzSx3mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ما از حد و حدود خودمان دفاع می‌کنیم، اما به‌دنبال گسترش جنگ نیستیم
🔹
باید تلاش کنیم در این اوضاع و احوال، جامعه‌ای بسازیم که دشمن در آن طمع نکند، وارد آن نشود و نتواند این مجموعه اجتماعی را تکه‌تکه کرده و از بین ببرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/678267" target="_blank">📅 09:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678266">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtodMYEH92orJaclrieSoxoPCnAL0JwhJCMXSMc14X871htPCzw8tNgD39uGSUGE4fdCIkrO-9kHjg4076BZsEg06NmIoVIFKN0BtpgECRXR1KqBn4IxSDUqj_8g7kSctTmoLpxWHWMpE2sjHxL1-blLmvGK04JnEfGzDU6sWglKLWVvMldD1cxfdNaFNr5LW5swCE9ie1cXlphUsiRssSLoXatX_hhwuZPm8hhf0IVIX22M79hO0eN-fb1nqmf6xuT1VJ4OdE93wbzP_mnu4knSLaSEFtfz5m09p51W_qmC0AR16g3FfQsPo7RAZsOiLNIGwcP56btq4grdHHSUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرگ عجیب و باورنکردنی مربی کراسفیت ایران
🔹
مریم سبزه‌کار، مربی کراسفیت و نایب‌رئیس بانوان کراسفیت تهران، هنگام کوهنوردی در ارتفاعات لواسان بر اثر مارگزیدگی جان باخت.
🔹
او که به‌تنهایی راهی کوه شده بود، پس از حادثه حدود دو روز مفقود بود تا اینکه نیروهای امدادی پیکر او را پیدا کردند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/678266" target="_blank">📅 09:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678265">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6d0e66e3.mp4?token=MPrb3jLlpmrU2zJsUcfcORQOnQ0YAm4hqujSM5FwUAP4s4vmEzWejFDQQudN0PLeN_pVN-LmHo4q2mtCawAXBoD0F4xBR0TzX2byaDGygq3fghD5-BH7Z6VblMMci9B3PMndpWPbfKxOyPQjhoqKZJ3acqvrN2Q5IZUTBsDyADhAnik2XBpQdxy2luohc0Hb7x4w_iePAMrHrOVDyGEYQAWO1PYZSFDHEa5v6KyZVmVZxWhlyy_9LyGWNcx40JzaRYWqWgkzBpHxEut269tgd_ez2dS55cCtnFaLJ9phRT997zCQj0mcp7Lm-P4a1ALqKhhOa3OvY4ND0iqJz2t4yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6d0e66e3.mp4?token=MPrb3jLlpmrU2zJsUcfcORQOnQ0YAm4hqujSM5FwUAP4s4vmEzWejFDQQudN0PLeN_pVN-LmHo4q2mtCawAXBoD0F4xBR0TzX2byaDGygq3fghD5-BH7Z6VblMMci9B3PMndpWPbfKxOyPQjhoqKZJ3acqvrN2Q5IZUTBsDyADhAnik2XBpQdxy2luohc0Hb7x4w_iePAMrHrOVDyGEYQAWO1PYZSFDHEa5v6KyZVmVZxWhlyy_9LyGWNcx40JzaRYWqWgkzBpHxEut269tgd_ez2dS55cCtnFaLJ9phRT997zCQj0mcp7Lm-P4a1ALqKhhOa3OvY4ND0iqJz2t4yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله یک طوطی عصبانی به یک بازیکن فوتبال در لیگ جوانان برزیل
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/678265" target="_blank">📅 09:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678264">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ace8c9e57.mp4?token=TPCupmfpeAZaQT6-IXwxxaCEXCVbVI_HI0v1kR0hvRiXGIzTPBSfFJxtixNwOTJCfFv-kqZAynQRIIvIKV-QEVCv3Sx1rEuo6sUd761jgDI4qA6Oygp9WNPQIWBirAN2Odb5GocYFxUMhNmcb-AeUXH-pHIW18KWJH_blXE2QC0tT3tUN8zOfwOg1VEhyXuRDlyWJ1_1eVee85a2-0lTGzWBioNAA_gvx7NMB1R6mxi1NboFjdWQiH0mK50K5-wUlWVFcRqnwrVDZQAYfS284Q6NCOWmg5QhzW7ZoICQ-UvxKAwA8BaBZc4ucpDK5oHPJwpKI7ZHazWyMRNp8zrpxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ace8c9e57.mp4?token=TPCupmfpeAZaQT6-IXwxxaCEXCVbVI_HI0v1kR0hvRiXGIzTPBSfFJxtixNwOTJCfFv-kqZAynQRIIvIKV-QEVCv3Sx1rEuo6sUd761jgDI4qA6Oygp9WNPQIWBirAN2Odb5GocYFxUMhNmcb-AeUXH-pHIW18KWJH_blXE2QC0tT3tUN8zOfwOg1VEhyXuRDlyWJ1_1eVee85a2-0lTGzWBioNAA_gvx7NMB1R6mxi1NboFjdWQiH0mK50K5-wUlWVFcRqnwrVDZQAYfS284Q6NCOWmg5QhzW7ZoICQ-UvxKAwA8BaBZc4ucpDK5oHPJwpKI7ZHazWyMRNp8zrpxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم بزرگ خونخواهی در مراسم راهپیمایی جاماندگان اربعین حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/678264" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678263">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7db3633281.mp4?token=qz9n3-L_64lD1CEzaJ1ukCZi0VcumKYeWM6dx18-Uxb92PpFrcInqkYx9WUoFfWEb2eLmPMaWyoQOn2rvFxRYUWRB0AfTkkncFoq60uJurkfPTA-Bs0hriDcVIp14dNtebI8sXqfpcGDgBprBSskQZwEKB307st7-bYZMeMeBCQ6ss5BWTgkYEGVAS0uPVRZE4hi62XkEKwZThBsOeldMwerAYVQmqWWmC11OTS253X3EVaXmiyXGsbcE8L6aSfzVCGMhGCkaTWIQ2KkcddFXz6woXgYhRuaqFY6ORKpMLzgQ9IPRlxF792Gqmzy2QkK95voHQmiJY8Fh0zdFYACyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7db3633281.mp4?token=qz9n3-L_64lD1CEzaJ1ukCZi0VcumKYeWM6dx18-Uxb92PpFrcInqkYx9WUoFfWEb2eLmPMaWyoQOn2rvFxRYUWRB0AfTkkncFoq60uJurkfPTA-Bs0hriDcVIp14dNtebI8sXqfpcGDgBprBSskQZwEKB307st7-bYZMeMeBCQ6ss5BWTgkYEGVAS0uPVRZE4hi62XkEKwZThBsOeldMwerAYVQmqWWmC11OTS253X3EVaXmiyXGsbcE8L6aSfzVCGMhGCkaTWIQ2KkcddFXz6woXgYhRuaqFY6ORKpMLzgQ9IPRlxF792Gqmzy2QkK95voHQmiJY8Fh0zdFYACyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا اباعبدالله
اِنّی سِلْمٌ لِمَنْ سالَمَکُمْ
وَ حَرْبٌ لِمَنْ حارَبَکُمْ اِلی یَوْمِ الْقِیامَةِ‌...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/678263" target="_blank">📅 09:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678262">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tj9VaP6bkXC2P1llEhgh_n3kWsjsyXp-kUhwLMkgLeQ8xGkBDpNHf8T2ZSRV7Y_o2YWrcTtHSGxKjqXtD5VhlGeJ5nu7DYDkvDmX3XUwZIfxeMPhc-uxmrMFGFGudcHV6PEH5zgjnfSF0QjJmKNcOEva0r5ahH_BhSJjYGtpysgtluw_wr7JeUPA5XJ_1HIE-VJrh75Gx13RNkXB2SOitGXpDLBDIRtSCviPe28dU_EaIclG4j5BE-hEG6mVwQvFXVc9cP8rV0k0cMfHi24HI73TiA1lfHrCoefgkKIY6D-31qdfOnmTzf6UgejkYZdfyLkeBiV6Z4GXa_F1b5oJ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش مهران غفوریان به فرارسیدن اربعین حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/678262" target="_blank">📅 09:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678261">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QliMxFXDAQU7EO4-ZASKOgT5v19FeYmlbcZTfMwk_QdzmaNNBqP8l9IQfXruqF-1V36EYn9n4BdW3cjVZnlzDsPtjipl87C46_hT2hOD70tCUlD0NO1AbjxCXn_CzbYdH-U5DdDoT9bQ6YZRDw_wJXGQdHBufv03D3s1V-TIXdsa89OGRO1qoH3NUqWpBEhwoQD-BWg4vY9gdA6b28EZzJnItrFiUFXZX_J5kCUjFuUuWlvpwcH0uynceh0tW1qBE1iPxRhsHNgrsrReTH12-9VnmKRFJ9nPe1YVGTL_scgMDLTPX9HBfbn_uf872aqGbxh2UwgFMYiC89Q_MsUwKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استیو راتنر، ستون‌نویس سرشناس نیویورک تایمز: در حالی که آمریکایی‌ها با افزایش قیمت بنزین و تورم دست‌وپنجه نرم می‌کنند، شرکت‌های بزرگ نفتی از جنگ ایران میلیاردها دلار سود به دست می‌آورند
🔹
سودهای صنعت نفت تنها در یک سال، بیش از دو برابر شده و به سومین سطح بالای خود در تاریخ رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/678261" target="_blank">📅 09:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678260">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
نیویورک‌تایمز: توافق در حال ظهور ایران و عمان بر سر تنگه هرمز، می‌تواند کنترل تهران بر این آبراه را تثبیت کند
🔹
این توافق به ایران اهرم استراتژیکی خواهد داد که پیش از جنگ وجود نداشت و شامل دریافت «هزینه‌های خدماتی» از کشتی‌ها از سوی این کشور نیز می‌شود.
🔹
مقامات آمریکایی می‌گویند «در مسیر آب‌های عمان در تنگه، هنوز مین‌های زیادی وجود دارد و کشتی‌ها برای عبور ایمن از آن‌ها، نیاز به هماهنگی با ایران دارند»/ انتخاب
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/678260" target="_blank">📅 08:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678259">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
به آتش کشیدن خانه‌ها و خودروها در نابلس توسط شهرک‌نشینان صهیونیست
🔹
خبرگزاری الجزیره اعلام کرد که شهرک‌نشینان صهیونیست پس از یورش به روستاهای «تلفیت» و «جالود» در جنوب نابلس، تعدادی از خانه‌ها و خودروها را به آتش کشیدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/678259" target="_blank">📅 08:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678258">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
پزشکیان: ما از هیچ‌یک از مردم دنیا پایین‌تر، کم‌هوش‌تر یا بی‌انگیزه‌تر نیستیم
🔹
قابل قبول نیست که نتوانیم به مردم کشورمان خدمت کنیم، مشکلات آنان را حل کنیم یا از دیگران عقب بمانیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/678258" target="_blank">📅 08:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678257">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
اپل تلگرام را به‌دلیل محتوای ناقض قوانین سوءاستفاده جنسی از کودکان، موقتاً از اپ‌استور حذف کرد
🔹
پس از حذف محتوای موردنظر و مسدود شدن حساب منتشرکننده توسط تلگرام، این اپ دوباره به اپ‌استور بازگشت./ بلومبرگ
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/678257" target="_blank">📅 08:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678255">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A7Sybg_XEknq_08Y9CsPfOqBbpgKTnzSVQEer2chMpKwhgpK2S9DIj_q_XhlX8cXpry28DaB08ggzWeZbFy3FNSPeRrb9OkNPhmPa6DqqG-bcQIm8lpc_YhJKnkCDnHJ1IVFbII0KStHL-7kHimu2ZKRf71f4zrEpEB5l1Xml1k2LYWU5AcShV8-y9-wWoDKsQCA0-_rXeTgzRyzt7h13bLIcLoDjD0g8XeXv2H1PKWbsz_tzoVOAike1AB03P4D20R6c4YtYp4cbiX4WsAeWgpH8pQpFzDgBgkGEtGB7BlHOrdH_FPxl7RORrn6pVc_aJo3dfJsvpndes7HSz2R9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GS8Mxd5pSqz7UBxunm2bTwk_x4DRVnpBeOzRw2t0tgia9ER4vUY2ZnOtfun_hsrlP-rhDVhcBNZPg9SNzt3qhc--5O08Eco-65wbit0wGJ13F986OgCsb05VAJOtRhReyPBWJHlzNQS3OoR2vfa9UiXMcmIVrBNhGNysqZe99DeAnTaEDaRjZ-N6I5hC2p9w_-qyJU1lTQVR6_IE-6hNN8poMRJEcyHS8BA2RyExvHJpXuGfuFC-90syvQwybMmcSWPMV1tE7RYu7J85KpJbNYMsUC0djMcawjBRDamTz12ILrUzJSFT5yPzLVgPZ6oqFJrIjzEBpgXKygQMjyUxrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طرز تهیه ذرت مکزیکی خیابونی خوشمزه
😕
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/678255" target="_blank">📅 08:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678254">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
کنسولگری آمریکا در ژاپن، کانادا و اندونزی تعطیل می‌شود
رویترز:
🔹
وزارت خارجه آمریکا تصمیم دارد دفاتر خود در «سنت جورج» (گرانادا)، «ناگویا» (ژاپن)، «مدان» (اندونزی)، «دوالا» (کامرون) و «وینیپگ» (کانادا) را ببندد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/678254" target="_blank">📅 08:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678253">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e739b2af.mp4?token=chNe21q3QE4a7C1LXyt01paCaBNyNYn0fRzZhWZwNRWE2qeTrulkHDAB7euNAxuezbFJThE2ggYK4IUgCrFWHeAI_Jt_wkjRwA4_ilZV4w2jIGjFauo_7ksRiR26ZUrNHmJJCX5YZFxLyxLki1ub9nG9sleM1eJ44DZHUiuglFrcqb43E-ufUGLfdl21PVyhotjE3VmRi_x99rOkAoAMPXIriQh2Yu7IVlYOuIJckkPsJ4dDTIAry_z-HDloyiMIBEV9UOF9p_bq-TNyDCUejs1RZbIZs0tnlF2eXCHcHcN-b1dhSKZOcA9fn7QHw6NVI9dHz9jIvua1628LIFnXrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e739b2af.mp4?token=chNe21q3QE4a7C1LXyt01paCaBNyNYn0fRzZhWZwNRWE2qeTrulkHDAB7euNAxuezbFJThE2ggYK4IUgCrFWHeAI_Jt_wkjRwA4_ilZV4w2jIGjFauo_7ksRiR26ZUrNHmJJCX5YZFxLyxLki1ub9nG9sleM1eJ44DZHUiuglFrcqb43E-ufUGLfdl21PVyhotjE3VmRi_x99rOkAoAMPXIriQh2Yu7IVlYOuIJckkPsJ4dDTIAry_z-HDloyiMIBEV9UOF9p_bq-TNyDCUejs1RZbIZs0tnlF2eXCHcHcN-b1dhSKZOcA9fn7QHw6NVI9dHz9jIvua1628LIFnXrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل زائران اربعین در کربلای معلی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/678253" target="_blank">📅 08:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678252">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
بانک ملی: مغایرت‌ باقیمانده حساب‌های مشتریان تا ۱۷ مرداد برطرف می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/678252" target="_blank">📅 08:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678251">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12137677b1.mp4?token=l113wtOet8Oyw3hEmoYlqGiM_Yn1BIJH8zAIvmubTGAvey_nIv4W0Afmy6ILx7wvB82_fbY0CykRyNbN_tU7bHjwcf02oePaVCcoI4E8ohBQeiH-iNcnnl87DlIB561XCiuV4KpXXNd9-ZokCAJn4CeUmFhJwOSKWrTtl8mNWYRx_2ES1NHg9eCzautrvIyy18eWzFuAGeIQTv_Xxy06pOTm0skSI-019wqnfzdaYZXbMHqsLSJ4FMbY5ei4TtzhsyubP5dA8qP2leFrSF3rkw7YeB7RSvddiYO7wsX6BB6vv5KY0gu_GCdgNgD-mvPfjEmjNy-hMFEtixAcr4EuH32xZ8PEAQLYd-fNUVxzMJkYmGJApRugGF7uN31k0_fMPzc-8YrFvoQuWwLBx4o9f68dXm_UGrwabZHwXp5vKkr72aNI2vl2YqNTyC6hCPofYrBEEMOeEmBTBtVUbqkqxYFzcS6RKOsE1HKB1xS8yV894cyIJrsGKr8fUfLi35m4_t9lKeUKbEbFF1LZIhFaxuycIdpt8BVPOsUgLsnkhsW-w9ApCX2VQblycGLuen5t-Tsk4LRRzGQ8gzt_-d6KurepekZn1QCFfdPPaqF6vrfL37zyVuuLAmuwrS17r0Dp_VJtKYDDYzqZz6Dzyq14OIO264_vJfJBkXhLDVVEyAk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12137677b1.mp4?token=l113wtOet8Oyw3hEmoYlqGiM_Yn1BIJH8zAIvmubTGAvey_nIv4W0Afmy6ILx7wvB82_fbY0CykRyNbN_tU7bHjwcf02oePaVCcoI4E8ohBQeiH-iNcnnl87DlIB561XCiuV4KpXXNd9-ZokCAJn4CeUmFhJwOSKWrTtl8mNWYRx_2ES1NHg9eCzautrvIyy18eWzFuAGeIQTv_Xxy06pOTm0skSI-019wqnfzdaYZXbMHqsLSJ4FMbY5ei4TtzhsyubP5dA8qP2leFrSF3rkw7YeB7RSvddiYO7wsX6BB6vv5KY0gu_GCdgNgD-mvPfjEmjNy-hMFEtixAcr4EuH32xZ8PEAQLYd-fNUVxzMJkYmGJApRugGF7uN31k0_fMPzc-8YrFvoQuWwLBx4o9f68dXm_UGrwabZHwXp5vKkr72aNI2vl2YqNTyC6hCPofYrBEEMOeEmBTBtVUbqkqxYFzcS6RKOsE1HKB1xS8yV894cyIJrsGKr8fUfLi35m4_t9lKeUKbEbFF1LZIhFaxuycIdpt8BVPOsUgLsnkhsW-w9ApCX2VQblycGLuen5t-Tsk4LRRzGQ8gzt_-d6KurepekZn1QCFfdPPaqF6vrfL37zyVuuLAmuwrS17r0Dp_VJtKYDDYzqZz6Dzyq14OIO264_vJfJBkXhLDVVEyAk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ما از هیچ‌یک از مردم دنیا پایین‌تر، کم‌هوش‌تر یا بی‌انگیزه‌تر نیستیم
🔹
قابل قبول نیست که نتوانیم به مردم کشورمان خدمت کنیم، مشکلات آنان را حل کنیم یا از دیگران عقب بمانیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/678251" target="_blank">📅 08:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678250">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed46a57cc.mp4?token=U4pxDJXk6_7XURj5IU2yYWXv-CG5I9iT38qMcblc8gNNRLvLFNLF_MQZO9pxdT5_hcjalZwA4NgX_ao38uUfB_biGdvu-g2oqC-C0m-MTFlc5KZUjy8Dg75QX-ZzHyN2GO2iS7-3Y6nXU63sSb8uz8SxohFNgo_GIOYgv7ZqrrF71fPOnfVYtEcteZZ-LZNlaJ3Toky1d7OhA_zh6TbMA4A7fH54qZFECVTBarH8rYHG9zYDJ3Jf3x_Zc0Y52S7QCt1UZarnLaSjs8TkU8RD4Pe2AaywCL5Xj7JEKDY4YwFLXnPOwdOz3oTIzXcR5azXjSlX3Yh4-rh49wONpRQ_xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed46a57cc.mp4?token=U4pxDJXk6_7XURj5IU2yYWXv-CG5I9iT38qMcblc8gNNRLvLFNLF_MQZO9pxdT5_hcjalZwA4NgX_ao38uUfB_biGdvu-g2oqC-C0m-MTFlc5KZUjy8Dg75QX-ZzHyN2GO2iS7-3Y6nXU63sSb8uz8SxohFNgo_GIOYgv7ZqrrF71fPOnfVYtEcteZZ-LZNlaJ3Toky1d7OhA_zh6TbMA4A7fH54qZFECVTBarH8rYHG9zYDJ3Jf3x_Zc0Y52S7QCt1UZarnLaSjs8TkU8RD4Pe2AaywCL5Xj7JEKDY4YwFLXnPOwdOz3oTIzXcR5azXjSlX3Yh4-rh49wONpRQ_xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از سیلاب در شهرستان راز خراسان شمالی که موجب قطع کامل دسترسی مسیر ورودی و خسارت به زیرساخت‌ها شده است
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/678250" target="_blank">📅 08:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678249">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bblh9H2wxaJYYd_f3eXHb5Dyk3iugyqvKg7CsBOiUSvp9vW_70mUj0_LOQhICYK9o1QQ9Q2qeRivo85XjqMUBF8By74uwneIIahvZflW4E0IId53f9pDN_S16-kf2TwzxnKi_K5UVc8oyW_-7Ij1hoD215FUbcV0R66ckeX4ZuT9QqcO5udfehTGuFK4oRPX6q6KfSXbQiVjhVCr2Xk_iPcQiomdZkmIP-KM4rkdQ0liaa9Si7YgORfLih2eI3ck-SVNmkTRz1mR1aAdEXY1lDIJijeg96uHnDP-FBfjOcQMdkciSDLP1A3DvI4ldQQ9Du1xbV8K0dGm66YXBGIW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت سدهای تهران اعلام شد
🔹
درحال حاضر به‌طور متوسط حدود ۵۸ درصد ظرفیت آنها پر است اما حدود ۲۵ تا ۳۰ درصد سدهای کشور بیش از ۲۵ درصد کسری نسبت به شرایط معمول دارند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/678249" target="_blank">📅 08:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678248">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoOj-4gaiCeTOnPUIl3MOUuJHK99Imx34mqKSz_a-dgTqbIUlnwlcrQPcWFdNa-chBmRSuomhpHTNEsJN8Z1FoQ_JUDjlDjT8csDAbev11OGZSq5yvJtI-Kj-I1E16kqZrwjFjNsT5VMVGkxqv0HOOdl2GtNe1rj4eL7bDr9tmNLHCLx5FsxHGNGxZ4NR4-aj_jLo0e7LCIT7kA7HWlnAyjKhB1oUib1ZMLfDJYpxR27INRTnxgBjlXhN6VhJYnAtj2fxsnuIeCJXCOh6YpjPuZIfudCPAypw1EhqDrrty4MBlisJmXwSeBhUWCKjR6bPBnjl_rnQUAFggx_SP_QSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لری جانسون تحلیلگر آمریکایی: راننده و محافظان شخصی نیکولاس مادورو در ازای پاداش میلیون دلاری با ایالات متحده آمریکا همکاری کردن اما بعد از پایان عملیات دستگیری مادورو، دونالد ترامپ از دادن پاداش نقدی به آنها خودداری کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/678248" target="_blank">📅 08:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678247">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سی‌ان‌ان: ایران آسیب‌پذیری مراکز داده و هوش مصنوعی آمریکا در منطقه را آشکار کرد.
🔹
فرماندار مسکو: حمله اوکراین به حومه مسکو ۵ کشته و ۶ زخمی برجا گذاشت.
🔹
تعطیلی تمامی میادین و بازارهای میوه و تره‌بار در روز اربعین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/678247" target="_blank">📅 08:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678246">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09f4012e43.mov?token=LrwkL0xYFxC4ngF_IsfNXlAYg5wStaTEYYaTi_dK7GPkGlJhtLPfhSLe5YZD_TN5RqnVqiVtfQFqdVQC3cQl8NY9HGCssSEwRqbDoaI2x_NK8B-JerDqxCwKzx_etMqgY9rRH7fVvAHK_t7bYVUdOeRwamz-XGUVv8dWBhm7jbnxyMAQPLIW4yxwU6Dzy5EPWeLXMmY1kUmUB8FLh-Yn6JS5maWTs7oyk4cg0JBmsKhp5ZhD0jxQ42jgpdMJYjNIuPsZJRWZjR8Wh9u3bcN8K2GCnm5UyGbzTO8O4awrLn6cShsHTIqEGplZhsX4KI-mK_FNZpMXAOTAydtAqZborw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09f4012e43.mov?token=LrwkL0xYFxC4ngF_IsfNXlAYg5wStaTEYYaTi_dK7GPkGlJhtLPfhSLe5YZD_TN5RqnVqiVtfQFqdVQC3cQl8NY9HGCssSEwRqbDoaI2x_NK8B-JerDqxCwKzx_etMqgY9rRH7fVvAHK_t7bYVUdOeRwamz-XGUVv8dWBhm7jbnxyMAQPLIW4yxwU6Dzy5EPWeLXMmY1kUmUB8FLh-Yn6JS5maWTs7oyk4cg0JBmsKhp5ZhD0jxQ42jgpdMJYjNIuPsZJRWZjR8Wh9u3bcN8K2GCnm5UyGbzTO8O4awrLn6cShsHTIqEGplZhsX4KI-mK_FNZpMXAOTAydtAqZborw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلدادگان حسینی در مراسم پیاده‌روی جاماندگان اربعین در تهران در ساعات ابتدایی آغاز مراسم
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/678246" target="_blank">📅 08:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678245">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
رئیس فیفا دست به دامن سگ زرد شد  بن جیکوبز، خبرنگار انگلیسی:
🔹
جیانی اینفانتینو قرار است با مقامات ارشد دولت ترامپ دیدار کند.
🔹
او به دنبال جلب حمایت برای ادامه فعالیت خود در فیفا است.
🔹
اینفانتینو در حالی که فشارهای فزاینده برای استعفای او شدت گرفته، با فدراسیون‌ها…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/678245" target="_blank">📅 08:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678244">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8625f597ec.mp4?token=Tntkn4vk9qNkO7aSnInU9-W2i9MuXA1-ha7WDQV_1Pzdlh7PBDoWzet-87ZyS5KtSzrgSYviBdYT3o1z5dozI1SYFKBfVuqE3WnG0DkUTr2jVUxgMDT_JtBZ9mnK1DrlxhuFi5JKSlKmqARQu0gv_L-OAynzGsN4rpoFc86PlH8pnIgfu9DaUKLAH0rVV6ca3LRe9C0gkVFytck3aIflV67QlF-eTYqRFgzMnTlVcEejeCwyNtqZ6mcLUQTUJZsRLXIeWY4vTVx_Ifu6c_CiPNuiB5CMFMmDoEanvA_4a0pNRqa14vz_85ZL41m26vFJP-lu7s0btG_KJuft4Eu1kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8625f597ec.mp4?token=Tntkn4vk9qNkO7aSnInU9-W2i9MuXA1-ha7WDQV_1Pzdlh7PBDoWzet-87ZyS5KtSzrgSYviBdYT3o1z5dozI1SYFKBfVuqE3WnG0DkUTr2jVUxgMDT_JtBZ9mnK1DrlxhuFi5JKSlKmqARQu0gv_L-OAynzGsN4rpoFc86PlH8pnIgfu9DaUKLAH0rVV6ca3LRe9C0gkVFytck3aIflV67QlF-eTYqRFgzMnTlVcEejeCwyNtqZ6mcLUQTUJZsRLXIeWY4vTVx_Ifu6c_CiPNuiB5CMFMmDoEanvA_4a0pNRqa14vz_85ZL41m26vFJP-lu7s0btG_KJuft4Eu1kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز مراسم راهپیمایی جاماندگان اربعین در سراسر کشور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/678244" target="_blank">📅 07:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678243">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ادعای ماسک؛ از بازگرداندن بینایی تا دید فراانسانی
ایلان ماسک:
🔹
نورالینک طی ۶ تا ۱۲ ماه آینده تراشۀ بازگرداندن بینایی را روی انسان آزمایش می‌کند؛ تراشه‌ای که تصاویر را مستقیماً به مغز می‌فرستد و به گفته او حتی می‌تواند به نابینایان مادرزادی کمک کند.
🔹
همچنین امکان «دید فراانسانی» مانند مشاهده نور مادون‌قرمز و فرابنفش وجود دارد.
🔹
تاکنون هیچ شواهد بالینی معتبری برای تحقق این قابلیت وجود ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/678243" target="_blank">📅 07:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678242">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
فاجعۀ امنیتی در لندن؛ اطلاعات ۱۱۴ هزار افسر پلیس لو رفت
روزنامۀ تایمز:
🔹
در پی یک حمله سایبری گسترده، نام کامل و اطلاعات تماس بیش از ۱۱۴ هزار نفر از کارکنان نهادهای امنیتی و پلیس انگلیس در بازار سیاه دیجیتال منتشر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/678242" target="_blank">📅 07:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678241">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d0e881a9f.mp4?token=LqaLCY1nkhAKtANT_82L1N2TNFoPpLOo29gfoNRwu6E5q1HuqxyDnD1OdpHcwObf3GPH_5zxBR7ArA-LSXGx1gOCowNeZwUhCJ8rfOi5tPgHeTaby4Ncp3RM1B5IE7vlPsLNAyStQe6kd_DUUEvfnjTqAZcgEb1eiNA9zhAjlXnGwv7NjZCqQ1Aa17V-q2Tp8CTIpUJ8XOPBJyH3ba378KVKvndg38dQEgIMt5pbQx9K_BS3QuRlEU_J4A1_f9JjOTvHiPM28294DnEiIsWz82bhY-pOqz4guKaXhA-8RoadPDOgc4T5-9YF2UkPJ8mSgJzY9UQwHZng1yibSVMMTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d0e881a9f.mp4?token=LqaLCY1nkhAKtANT_82L1N2TNFoPpLOo29gfoNRwu6E5q1HuqxyDnD1OdpHcwObf3GPH_5zxBR7ArA-LSXGx1gOCowNeZwUhCJ8rfOi5tPgHeTaby4Ncp3RM1B5IE7vlPsLNAyStQe6kd_DUUEvfnjTqAZcgEb1eiNA9zhAjlXnGwv7NjZCqQ1Aa17V-q2Tp8CTIpUJ8XOPBJyH3ba378KVKvndg38dQEgIMt5pbQx9K_BS3QuRlEU_J4A1_f9JjOTvHiPM28294DnEiIsWz82bhY-pOqz4guKaXhA-8RoadPDOgc4T5-9YF2UkPJ8mSgJzY9UQwHZng1yibSVMMTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بین‌الحرمین در روز اربعین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/678241" target="_blank">📅 07:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678240">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jahEtPzxX_IaWcFFG-LrrUWRK3GXIP8wSxLup2Hn8RgdKfXfsdDSTPKc7PvtSmGvzau5RpYQoVyvhPCoUwE2XLeJ-R30yTi5eeF4Z8v6jys8F-7f7hoK6E0SWoY6J0i5yRyX9SO64g3NFZhIymDQsM9oUfpakjDSqK9GelaHNi97EtxcRWQ-EK4i4WHJW7N-3fgP6qQcxxknNhCRmRk8Qe-UIvPfjmoaESoPNduQ3IBmUyEMHV1NU6AB9ZW8u2dB5M9kkzSTC6FI35e04ks5Yzf2JIHGA_nmE3pW7nKwY3I49OgDedW08TatIzs-Ze9POCQ7eSs6lCreRcEHWvhuZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۱۳ مرداد ماه
۲۰ صفر ‌۱۴۴۸
۴ آگوست ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/678240" target="_blank">📅 07:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678239">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiWpodYm3NbdDIp8BVBXLVMZIlzdgSm1jx1vAXMpcEwI-pYr6w0GU2jDTrKO9sQWJIH0A1RfG-Dcrm-0uUaJwvEz0vMEFjeyJ0ZtBsaHcdFnM6sEVwTPaxc0cCO3rrBzqf7qagrPM1tQXUj8n8WQU-_Pw3LbYHGYZRUFrlwYl8wTFX1C7ZU2JBSgjXhT2DHVXtadRXIE5qqPauD47vkQohkOcaiSZ5ckMMVF4BansBR578K7lffJBoNp9N6k11qAE0k33njOrxH8w8MiAMtntbVF1DlXqRvi4MPqle2kbkeFDvkfiFzHA0eiZtTkisG-mvBvLtIl8Yw6M5np_THpow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصابت پرتابه ناشناس به یک کشتی باری در سواحل عمان
سازمان تجارت دریایی بریتانیا:
🔹
یک کشتی باری در ۲۰ مایلی شمال شرقی بندر «خصب» عمان هدف پرتابه‌ای ناشناس قرار گرفته است؛ مقامات در حال بررسی حادثه هستند و به سایر کشتی‌ها هشدار داده شده با احتیاط تردد کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/678239" target="_blank">📅 03:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678238">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
رسانه‌های عربی: صدای انفجار در کویت به گوش می‌رسد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/678238" target="_blank">📅 02:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678237">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e81c4a381.mp4?token=KoTmwnEj7g-lVgEPIelqR50UMKcxKu_L3l7CusVfPB4zS8b9I5hNkpm_SFXmg2PNuWCzDKFhflUdOYDJ_lJl_Fo_tXosDIMocZQN5s785oubfT9Z_Dk7RPPt2eYQhGaljrCjNiFNEwwLXaejCv5HOZF2NIWMVgKXwj4pjW_0sGJGxA4CQ9_tkPkOsz-D7sCaX3BN3C8Xf0vg-TeZrk8OH1JHq18CVYRb8Dw69OfS43aNgGBFxXVVXweoKqOHC5XVAdsNzsemvWtgmyaRxyHNWoT5UJl_ZWKT7tdUhuMA7UpR-0dTDqBnESzgKT7KY6XE0Xj2kkCwdmxPUJPe1lKZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e81c4a381.mp4?token=KoTmwnEj7g-lVgEPIelqR50UMKcxKu_L3l7CusVfPB4zS8b9I5hNkpm_SFXmg2PNuWCzDKFhflUdOYDJ_lJl_Fo_tXosDIMocZQN5s785oubfT9Z_Dk7RPPt2eYQhGaljrCjNiFNEwwLXaejCv5HOZF2NIWMVgKXwj4pjW_0sGJGxA4CQ9_tkPkOsz-D7sCaX3BN3C8Xf0vg-TeZrk8OH1JHq18CVYRb8Dw69OfS43aNgGBFxXVVXweoKqOHC5XVAdsNzsemvWtgmyaRxyHNWoT5UJl_ZWKT7tdUhuMA7UpR-0dTDqBnESzgKT7KY6XE0Xj2kkCwdmxPUJPe1lKZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی: صدای انفجار در کویت به گوش می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/678237" target="_blank">📅 02:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678236">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3Hz4oBjrt53vtpCFX8460OrJ0vl3ROX67_RTJZPpnhWbaNN_JGUU48TFMFnkPqayd2q5oH0hJk_FjS9_ZYFhj9cUv50f18cgaOMXK-6RmSmjRnV3eDrNJAnoPoUoX6bSGHOOoqs7v3fIfJn1etViAzARntFMVKw21kvV5k1PmXUMcacntxzKhaRv_5LsGbXyECsfK5uHfpG0FwPGCrhWYRqQLnY-_e4XVuGrsgKuZ035YKzbr3saqmjB8G4vyhIUIxciobZjnTuwqBoZhrobqUjreszZyXJObWm4dba-t0N63Um49RLji_MLIh8AnlGIWk5MssIgRlFHiEL8Y70LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین‌لرزه‌ای به بزرگی ۴.۱ ریشتر، ساعت ۱:۴۵ بامداد حوالی فارغان در استان هرمزگان را لرزاند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/678236" target="_blank">📅 02:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678235">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
تشییع پیکر بیش از ۱۰۰ فلسطینی پس از سه سال
🔹
پیکر بیش از ۱۰۰ نفر از اعضای دو خانواده فلسطینی که سه سال زیر آوار مانده بود، در منطقه الصبره غزه تشییع شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/678235" target="_blank">📅 01:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678234">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
زنده بیرون کشیدن یک مرد ۴۳ ساله از زیر آوار،  ۸ روز پس از زلزله ونزوئلا
🔹
تیم‌هایی از هفت کشور - ونزوئلا، شیلی، آمریکا، پرتغال، کاستاریکا، السالوادور و مکزیک - به مدت سه روز به صورت شبانه‌روزی برای رسیدن به این مرد تلاش کردند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/678234" target="_blank">📅 01:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678233">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35651a1e7.mp4?token=BpWAqYpp9Fg-A3OnMPHCzRNdYtjzmIQC_t7-zPapDOTkPd6q8wRrM0vAOE1no8AI-Imjl0EbmlnrMwYj-COmkIAa4ND7KYrvGw2mrUUj2Qwth-dNpv9VEv6z9uw1i2fbkYH63vgNF24jylAjy0Xzmx_wKqDE3R9lkNB19Oh9yMY-7ExyamlELHUHn5NYCt8_DPByhH4_uDV07tKtcPF1KcGWnfn3M1giaCvqy_Oy2gQrcCXNgHBwNUnrr23BQqbXDQ5Ac951pGpif7sxzXvfJu3BzxjxLQUwENG0HKUPVyZRPW0zywSCKsnPnon6mho3rwVAa2YPUMbC49H5eZMAjYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35651a1e7.mp4?token=BpWAqYpp9Fg-A3OnMPHCzRNdYtjzmIQC_t7-zPapDOTkPd6q8wRrM0vAOE1no8AI-Imjl0EbmlnrMwYj-COmkIAa4ND7KYrvGw2mrUUj2Qwth-dNpv9VEv6z9uw1i2fbkYH63vgNF24jylAjy0Xzmx_wKqDE3R9lkNB19Oh9yMY-7ExyamlELHUHn5NYCt8_DPByhH4_uDV07tKtcPF1KcGWnfn3M1giaCvqy_Oy2gQrcCXNgHBwNUnrr23BQqbXDQ5Ac951pGpif7sxzXvfJu3BzxjxLQUwENG0HKUPVyZRPW0zywSCKsnPnon6mho3rwVAa2YPUMbC49H5eZMAjYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری لفظی بن‌گویر و وکیل آنروا در جلسه دیوان عالی اسرائیل
🔹
همزمان با برگزاری جلسه دیوان عالی رژیم اسرائیل برای بررسی دادخواست‌های ارائه‌شده علیه قانون ممنوعیت فعالیت آژانس امدادرسانی و کاریابی سازمان ملل برای آوارگان فلسطینی (آنروا)، میان ایتامار بن‌گویر، وزیر افراطی امنیت داخلی رژیم صهیونیستی و وکیل این نهاد سازمان ملل درگیری لفظی شدیدی رخ داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/678233" target="_blank">📅 01:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678232">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixPeWd8uLTGIGkriOZGomrQ7SfvTAqg96HHOBOkRD74aVJY4GuLv32MdPLuUXkr8co62vHmUAXoynbmTwCCH-9P4GbctNd4YWrCQ8dIxomFi-iAi0Gvep3ryFT-K2jf4P5qIgkdQ2Yqomvr0trFK-r8eIZ619PDlke4EXwANJSYyuAXnoZoVgWgnsQAt6n_cq6emSk6sGSOX4QacUqGkWdVHS8_F6eBnEb2Ju-Ik5kQR8FcWnhLKOOO55MO-uI90OOc24H09TNK_PAO9JNO9MWk0kgHJwY5EiM-R7CAzg_uX6he_YC4ZFcrX960k49OgkFAqoAGX7-hvjf9o8Mo0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویل شرایور: ایران ترامپ را در گوشه رینگ قرار داده و تنها دو گزینه تلخ برایش باقی گذاشته است
🔹
وارد جنگی شود که ایران می‌خواهد.
🔹
شکست را بپذیرد و منطقه را ترک کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/678232" target="_blank">📅 00:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678231">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سرلشکر رضایی: به‌هیچ‌وجه اجازۀ بازشدن کریدور دوم را در تنگۀ هرمز نمی‌دهیم
🔹
اگر ناو و نیروی نظامی هم به تنگۀ هرمز بیاورند آن‌ها را هدف قرار می‌دهیم.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/678231" target="_blank">📅 00:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678230">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
تمدید تعلیق پروازهای شرکت آمریکایی به اراضی اشغالی
🔹
شرکت هواپیمایی «امریکن ایرلاینز» آمریکا تصمیم گرفت تعلیق پروازهای خود به سرزمین‌های اشغالی را برای سه ماه دیگر تمدید کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/678230" target="_blank">📅 00:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678222">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I5G-NsNYzf0Qla9OngXNKfAQErBWTtR9_MRn4fIROaPrZp_b9TpbK-MBzD8PBexci96WwW0Oey305wg0Zvxd6iBPywGcAsVasUOnvgRJ5JRQbOK3R6wGGjYN8A1M92c6kVd8wTpw2qEBNJ4L_y93gDb8n0kCAzZkDtkULxiA9vkzQsLWKfoH7GGW7bgJJ_0yeYBrI14rIRXiabyyiHl__zHoh8F4-VYohh635sUC1E_g3G3UC7Z0xZiCXeEKl9ln4soWwJfBR8XLjJJxH9YKKa4rPLYwHP6Zf20aIjSKP3ac1H5ExPhsOxmPVHIAk35lU9PbR0RJWzCUkhWh0SAOOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FE-8qJAVENfhUOusg-Sc7yL4ZONEFGsx8rZeD8uqCTltfHaqS6q0woabSSlllRlgTPz0Czc3bdBS958_JXo5UAdgamKNCuTNwnCWCXwFbCpAeIdMxNxzJ-IWLKIVvuNdMI2H4uSVLVAyG0rBIcVqq16ky95OcPtRXIVaN6ReYGQ0KQaYcOClhYhHzCzC_16DE4B0lJX6rajvXSvd7Rjo914BQ6Y-_yVuyHGlCEAdnULhbGz20aZLZpyDr7xGx81Y6LJNI6DUAwAzE8YbSEM26rekhzkzECg_8PCFNnGoYDqR54yrXDwXCFiNiMHwOZdHtM9qeRRVPrH8F8BebyIvfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IANH7PBdnaYurEBPELhO7OkSG1BHrBADkYl3xqhEWCW4AHZRxZJWLGd7dgHXcLlz5WzqO9-yCAbU88Iaz173kJ8TYBsHs5vcyf9_aJrAQVBx64cDAtzHjQaMygZYeqs0peSfq8Z82QKa-JYR90feeLvdVqDePsBQZiveEPym-sRaNG8kKnGA8uRq3GXw1gqtQZ5luSV-ZAgaiBs8xNxaNvhJvD5BGzouft2UjebRHnWwB9N_JAErgRvyK3oNc0CccwAbBossQ5IntlUf8WbVO4gRhv1VqLvFqkPhln-nRkMS9Xu7dqrVITY-q7RWest7066U9uMccjVNAt0h2iwcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmLXMYoP0dNFUX4UhXk96eMaoN4qU81IBLrvGSwM25EEc1zljpQciaTuK9qlT24cU05I057eg5ST0EgNwTgGB9uc4Cq4ICR1vLTzTl-fqD1qRszv0s1uWZkPXkBwuTznB5-zUtJv5vB82Sg1BNd2zer454LWzPecSjzvvOdy5dEkGG0NKypw5jGChXIAM3nj2dnC0841zGQDk79dO7dRSFrJ2lz9tSgQMSBKF4gIizkRDijuQA7oUrPITpc4KF0NZM5_UlZCJYrsHIfYaQe_XhpePz7nnPwljCMCrfMJjec1JYjMs_wmhfTiKVfTmGQdiOBmg33Ume86HJ8JSFPHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhC2eU9yvq9jbenYm786An0-Q0pRzpMZHPgYnv-mxqmuggbD00OZ_THqmtaNWbMYQ2FGXpn_wOvMQCs7wG9zWgKoKmXgfhTNIKQeXB1RKHI0EBRuaqiqcxiLqUb3Sctlj2BqVGzFPrVS3YxJpfsSYOuaTNISHKhlytbz3riuLaKkha6WGcTpNzSwLKuVYFKbAdVm3sfqTz85PgA7zCMfA9SvyGGLBUySHsWd57XDfQmDLTvGTp1rnRhbry0rx3Ir0bmk8Qc7SR5VMor0Cyged34Zq1OA6NLR7R08CF_2lzPDp1L_IBXpONrcYKsck-6zOiSc9v6hcXMP_fBRZe6zKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eii4MjWcxVc1BovOJXKTdm3s9J-7UoTYKB38blTD3Oj_VK58Vk9uvXrxD5MJmZ7JEht6dU_j_-6VM115B9b73CsVlwBpxzIM45kyMSwfWsZ3PVRVxUxXeaeHLtUNKSx-rmQcAxMDmPSUwsgfWlyMhZbV8vsW4PA-CXIURVU2D-xJx6O9GHUyoqp1OEP6-e5Ke9OUKeGIxFNNMMsDXM0HJAyzwkLJggl4VJyTZcOOpj58huZgjIRIJFkQb3-rekd-asv20lnGvClwJBBITHVw2wWPGIwGlyy3bwZXQn4tzgXRUytmjMAXpwEjNfbOpWvu852l-_dV_8AnRW3ozfGcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gh36pNXqAjaWcbMifKUOumFgElKhv6kmLQUCAzswjDLUH0b5D7B70vlIH-210l9sBsYxanrj3n_wS1v3UEGW004yii6k2JapLaddokfNt6GSS3cfL8WC_H-KDhXNoz9nT4GeNL_XmQGlFHgjw1UIQJTFXDx0JGhqT-p3D_AQfcxrKssmX2mbt43cXfYliT9nPCnUUYO1oFmZf_oW0T6xlWI2iyYmqP78FvzF5RsycbxQVQd8v4aizkViHLS91s3l2c5CPE3szXyVo53mV44BAd0mkIKXuw_IIyDN8-U37phdIxbNK0osvcyav1iEX1Yn9bsBIGHOXxnTQHl0Wlp_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOIZx9X6fu-ogyqklgCg6ZVvV5oO5CL6LbBK8vkemVyZjjiqWYQW0eH9WeFwyVv4Ww9KRdoee9Raew1-Rv9Huhep1HL204mc09E-7qajUhplG7c2hzT3QKKHCiiNQHwzTkeHPs3xZs7jIgdJkHI95lDOdM0C1kOhVF6v_npP6KZ0cGNGKueyIKDzy6qn_snqCNHK99fQEgHfdY1PZZp-SuLvIjme7EG68BMNjZpZjGC_KW1kequ1kulUdW5nZvyvB-7KJ2Xs6qbLZgqoDIkdtzzsaEk8dl-gYMS92iSb-GzhHGXdm3mHPZeLIcwE7-2aWqUJ-GD9MpuZKQC4eaTH2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت یک فرهنگ ماندگار
💫
✨
آنچه از نهضت حسینی در دل‌ها ماندگار می‌شود، تنها یک خاطره نیست؛ فرهنگی‌ست که انسان را به مهربانی، ایثار و خدمت فرا می‌خواند.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با توزیع گوشت قربانی، این فرهنگ را در حمایت از خانواده‌های حائز صلاحیت به تصویر می‌کشد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/678222" target="_blank">📅 00:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678220">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYQFgktcsYsN0lmf8TvGxCFvW-tVeIDgK93jyyQ3fCL5CzL73uV6eFjKJX4DMe4JXrWXhqcyjiN7gK3VIofqPUeBKObOGiYQw_vfXpzMwUwMxbowykava7u15U-NXT1rpDLGPFpUMcC8eND805j23WLhuTN23XYRdyqgrisArjtgHu4WRi7_YeF0xFCajJFXIEQIl0dr2n_9x6WBp9kwI7KSNeI6-5Yggug3tHzrPAcsZmJQkOEgtGRbI0a5uIMKMCZc9QPYaWEsMAId4l_pNQGFztj-f_CzxkIBdi9yXhHrcWAOEeDzsRCOiBq6ejQLx3gSHReURV0L9Io0IWjXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ جنایتکار بار دیگر از شرکت‌های نفتی خواست تا قیمت بنزین را برای مصرف‌کنندگان آمریکایی کاهش دهند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/678220" target="_blank">📅 00:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678218">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwYdSh-v9jKspQW1v68-wRePX9GW4LDyHSRrIN_NelK8FGhJffc5TxkFkukHnDeHE2nRzcxeX4_G02pYPUtJSKS_A8gaZ1xpb0KiZ94lV6fQKken1zcO0rtzZSTLW4U9oMfgM6Mrz-7l5Sco7BKCPb5VpKgETQ2IV4tMP_UEhZi5IvlZGC-JMqi6JgXQ2yzLUCrgxFW0anpPOzdacu8XLMv7BvNPWQbN52ycGoO8CgFVT2u35p_RAcWLfsDFtUtmJlj5JOHCUzIQZu2NaiqL2EjQXFNrdoIQZxp7mCRQU7i5MhDpZ_OYBfKJCZGRar_P_1JVLzwYE1-DfLevlnJNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZgsPI89TyGw1VsR2TKOm37dgAWu2EoUlP0YdN7LmbPg7IlKiN0OeBePn9698CW2XfQE9L8zSCehxlCaKgPkBc13vC2Nu7mF0NE-0Xpe3S4f-L8BjF7Z4yNBzwSZomudD3sYqINaFJ8TIf5qq6tszU0MRFTg9SZow4SQVPdRI8L1l2x9HDx8XlhH6GxbxR3UHWtbK3Ap7cC5uSs3jTYSZpNsjdWeIGULLI7pj8GwqXTPw59eH5p3vjTo5A4JVMTxhVZ653XGIEIRIUQyQkw_Y7VT62YRQa39OTzsemBWyaWfUQgRdi3L1TXbBtVW8_7wmsywO83OjNTfRZV7QieKlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فکت عجیب: اگر دو، سه و چهار انگلیسی را بنویسید، زیرشان یک خط افقی بکشید و صفحه را ۹۰ درجه بچرخانید، دو، سه و چهار فارسی می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/678218" target="_blank">📅 00:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678217">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP2rI9EAA4y3H8kkccDEtb4ZhzNhdQHbtR8VWfFE6J0lAN7870Mj4mOeNMHIb7fCyzPFMO5RbiWI6ZElZb5CJWfXBs2YkLeVt_k7pjB_lb6jFYzZTvYrSyObkEeZCDUDPUeeQI-XyznoreBPeiJi8oGk9TmC1-NEPwuIzbw1qX--KWokroN3P3tL1RKTkBP_Qhy1AKscu5gzWtwtYkFIbb4gfTP_EeuA-Pa2zeuLyhOO3JhrTcnGzkgpYw5ebskywml3yBo9md1dqRiSLDS6gGjZGlQU3V3nMaxGLQ2puCqq2xE8FUqplTyJUaQNGs4fUR_H_eJKVPR7KKxLLj9hqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران و العراق لایمکن الفراق
🔹
اربعین امسال، در سایه تهدیدها و حملات نظامی آمریکا، جلوه‌ای کم‌نظیر از همبستگی و وفاق ملت‌های ایران و عراق را به نمایش گذاشت. این راهپیمایی عظیم، بار دیگر ثابت کرد که پیوند دو ملت فراتر از معادلات سیاسی و فشارهای خارجی است. در آوردگاهی که روایتگر ایمان، ایثار و مجاهدت است، میلیون‌ها زائر ایرانی و عراقی، دوشادوش یکدیگر، مسیر عشق و معرفت حسینی را پیمودند و با حضوری پرشکوه، پیام وحدت، مقاومت و همدلی را به جهانیان مخابره کردند؛ پیامی که ریشه در فرهنگ عاشورا و مکتب سیدالشهدا(ع) دارد.
🔹
هشتصدوبیست‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/678217" target="_blank">📅 00:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678216">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
الجزیره: ایران تعیین می‌کند چه کشتی‌هایی وارد یا خارج از خلیج فارس شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/678216" target="_blank">📅 00:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678215">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLWxoZP8fv_whts633eZ3jVfH45N6duJomHODVkgrenyHUPqIbtQS3cjL9eyBPEU97nELEbIXXTAeiymcKMiD7tNB3h6_PqmvAOEt1d-vCX1WnNrBpAuyABWjrhWxriprH1CU--714UuKz-Jhkl1aCY-H9MDI5QwiMLzTHpG1w6gZJp5TJ2yXR5ZM0Y9ygAdois8lc0Vz72tX_O52lt21DaxN87PoUR9LA3y323GSXhmDbU9dbI6VefpBMeCjpZsaLmiIhIim7A51-aOKerdyNYbDQNyFg5c27NqXCXgty16kBr8MaNCWd8DBN9tEpsfv_ydIbvjy0K-2KgUjbvZZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری اینستاگرامی علیرضا بیرانوند در انتقاد از بدون تماشاگر بودن
دروازه‌بان تیم ملی و باشگاه تراکتور:
🔹
فوتبال بدون تماشاگر اصلا فوتبال نیست، آقایان تصمیم ساز حالا نوبت شماست که خودی نشان بدهید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/678215" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678214">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQTGa8mb_x9-Emv9k_yQD0PBQ16S_22MecA9qiHwoFxJF0SePHYkrmN8615bc7U7w-4Usd4yJF6ost4XNE5a_dgOUyuMC9jNTJ4Ai05yaOW6q-vvqbn5I3qJW3BDRI8NiMCmygx0lqURba_S6frWGtBdBeJF1OGDiQzJo5TTgkPBxO95OShA5Frgj_ehaQU0ibA5RAoWNRUAH21b3uE82aXsLjB3y2kTUR6tjxI_AdthjD-free9JeX3PJaZKlpXOGCyno9YviIQ05AqbRQK4rStB-DoUfRh_YnthckUvr-GIP2WbBlY4sKHDrD7RtTH6TlXX3BkDrmH7Q0sKjDClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر پزشکیان: ادعای استعفای رئیس‌جمهور واهی و کذب محض است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/678214" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678213">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuCbXT0UkMaEEf9J09OqShLquEraaoz04XSgqfc3un8as8QVDMHPsDRKxFGmp-AdcOA6kKLAi181F6hj7oUzPkZXlRWNdq9b2NgEBe-I5fmouf3CX6jz7XfJTGha-b5JTjw3Osk01NjNrBkGVo1KuNNSQ1ucvssFYGq9CAxjVuD_IJSdq-axHLetJkZCkdA0UC7z1x0dsKq-H0nRGB5U4Y2CL8c3Eb9vODS1EX_P8fQrRjHQS9RlyID_JgbKa-nX_Vv_kBbN4fwleGeiILIsunQtcV-SJKdWkGPF979siQkraTgQnk7SAbJqS7t8yt1KPL5pG_XVf2rI2N9TCfM0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/678213" target="_blank">📅 00:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678212">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhZFJn3sZ8mBDMJyXav-jBVmTbLZz7J0XljSbsRFBcWaxmoP_dEADsfXGro2OzM339o8F_nxaSFLvhzfwA1BAljISMqxkkvdRCCHLSfhZ48a2-5zFEmJb03OuXjiFYEfdnZ5OMK2qQDanZ-vmACTu0cS9EU2PdC4unQC8mScMAJxnITpcGqoDD1g4mls_xoIyt7xWaJH8NDX92Y_M5TiLMHiXEpSGvNm5ZX3eTlMeGZfXoIYxBo0gRJYumMxMch9e-ewncA87XDDXItJ31hriZdIFWqZi3rbHfFepASxumj3s8vj3noOgLBL0kU4YLFnb-W07pQtLTOMa-ZcDOWTwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الایجا مگنیر، تحلیلگر بلژیکی: به نظر من، سنتکام متوجه نیست که وقتی می‌نویسد «۵۰ هزار نیروی آمریکایی در خاورمیانه حضور دارند»، این ادعا تا چه اندازه مضحک به نظر می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/678212" target="_blank">📅 23:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678211">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75331f2505.mp4?token=iARbxPeyiQUA7lVsaflvuYimh_cKVL-8J3y7yrCAtwVyNs7RU-ke6tvfpqz2zkmgw2ssnRtnAVYDABDkorNJqh6SGny44kCA9x_y09z6a-I-Kpvzf7rNj7Q0j2gNENJb6ILUhq09uH0ga8rgO8mBAgkGSyZxOD9NzRMKWprxo-ooqplUaa_yaPCD4DIsjV61LmBiYLBlF3pSvcv3SSkaxk4y3c4I0601wl5ik56WIHgBM4PiBwCrvG05h2uPb9eYVfuuIiJh-_r2JpTECdfCqSU78N2V-ZAkD0sZ6q75xhPSPqg0Pnp75SQg_eZE0SSctNjnDwRw9kVCXCrnYTsdWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75331f2505.mp4?token=iARbxPeyiQUA7lVsaflvuYimh_cKVL-8J3y7yrCAtwVyNs7RU-ke6tvfpqz2zkmgw2ssnRtnAVYDABDkorNJqh6SGny44kCA9x_y09z6a-I-Kpvzf7rNj7Q0j2gNENJb6ILUhq09uH0ga8rgO8mBAgkGSyZxOD9NzRMKWprxo-ooqplUaa_yaPCD4DIsjV61LmBiYLBlF3pSvcv3SSkaxk4y3c4I0601wl5ik56WIHgBM4PiBwCrvG05h2uPb9eYVfuuIiJh-_r2JpTECdfCqSU78N2V-ZAkD0sZ6q75xhPSPqg0Pnp75SQg_eZE0SSctNjnDwRw9kVCXCrnYTsdWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت معترضان به جنگ علیه ایران در مقابل کنگره آمریکا
🔹
تعدادی از روحانیون مسیحی و فعالان حقوق بشر در جریان اعتراض نسبت به جنگ علیه ایران و ابراز نگرانی درباره حقوق رأی‌دهندگان بازداشت شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/678211" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678210">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
محسن رضایی: شرایط کنونی ما شرایط گذر به قدرت چهارم جهانی است
🔹
وحدت‌مان را حفظ کنیم و اختلافات بین نیروهای انقلاب را پایان دهید؛ نباید نقد را به سمت تخریب و اهانت بکشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/678210" target="_blank">📅 23:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678209">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d92958e1f.mp4?token=QHYQHoNxFtOIKCotlRuIMX-zOOBUSjB1-T2LP_IBVlhA-90NtnR-4_xTeLn4b2qOzZMaxf1MfDUlQxXIVdhTtKx10N5ruG8L4l6GpkkL_XqPaQCCdrZ-J5vgo8UN-r24yDJSTDzIxjN_AKH6SewGEf1GK3XUZPayHRoHb87Y2xlnZIX0rxFpMvLTC9uNuddtNqYbxv504NWGIwl81QMDMV24adsX6GbbJn6khbcQBALPRSugUIXW5F8MOKUX2wyb8kX2zBYAMHvxzgoq6mrQy11DNqrtMYjiLzADKe01Io1v4pVD0WDGdKYJ3mhfCw037Kzo9lL8bU5OECOAFmAcKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d92958e1f.mp4?token=QHYQHoNxFtOIKCotlRuIMX-zOOBUSjB1-T2LP_IBVlhA-90NtnR-4_xTeLn4b2qOzZMaxf1MfDUlQxXIVdhTtKx10N5ruG8L4l6GpkkL_XqPaQCCdrZ-J5vgo8UN-r24yDJSTDzIxjN_AKH6SewGEf1GK3XUZPayHRoHb87Y2xlnZIX0rxFpMvLTC9uNuddtNqYbxv504NWGIwl81QMDMV24adsX6GbbJn6khbcQBALPRSugUIXW5F8MOKUX2wyb8kX2zBYAMHvxzgoq6mrQy11DNqrtMYjiLzADKe01Io1v4pVD0WDGdKYJ3mhfCw037Kzo9lL8bU5OECOAFmAcKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سید عباس عراقچی در حرم مطهر امام حسین
(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/678209" target="_blank">📅 23:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678208">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8017aa4184.mp4?token=gWuTjZx8twpQOrtounSut6r0-mjBr2LtRRCRSSHQACUh4hOttrfoQo3N6unYQ4t-iSLSrIoFGWr_Mki1u2eUIofYQgl9fkbr_g-atSLgh1RJgAVzARC62dY7uMjPV6RbX6BJaviM0GJTSUE1N_-1c7XkfD7HR_TMzeCUjgHiKdDHfuHhRZIQoHszS49SR80REa9tIOBlsocjSR8RZ3zE4qjEU_8qjSlh_faD0Fe9z9wr-a9DjPlsHb_BKuUu8n7cbUEa8VbcxyNNpreoLCIeaCTlma3tyzuLNRgQwkceJlA2fc809rvZ-R6yk74e8JOJedXNWBrnJw0-KQv669hPcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8017aa4184.mp4?token=gWuTjZx8twpQOrtounSut6r0-mjBr2LtRRCRSSHQACUh4hOttrfoQo3N6unYQ4t-iSLSrIoFGWr_Mki1u2eUIofYQgl9fkbr_g-atSLgh1RJgAVzARC62dY7uMjPV6RbX6BJaviM0GJTSUE1N_-1c7XkfD7HR_TMzeCUjgHiKdDHfuHhRZIQoHszS49SR80REa9tIOBlsocjSR8RZ3zE4qjEU_8qjSlh_faD0Fe9z9wr-a9DjPlsHb_BKuUu8n7cbUEa8VbcxyNNpreoLCIeaCTlma3tyzuLNRgQwkceJlA2fc809rvZ-R6yk74e8JOJedXNWBrnJw0-KQv669hPcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از حرم سیدالشهدا (ع) و حضور باشکوه زائران در شب اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/678208" target="_blank">📅 23:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678207">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f8294db6.mp4?token=JuwG81yY5bYAQeepzXflnCONUz-eheJY9dUggw_ua7cEqbZWZ37kRyjLClpx4xO99Vz6JE_UPjPkPM5yFzpQskB7vBVtKWmZ4atRYF2IDxIS6XVDz3_kunhOiPOXoVlxeigUr9Dc7CEKwT1NViZElN1-_FydiCNHOOHaCJmmqpvYvzB_eZ9M2bN1WlrYydHzPBMDtSKB0q9QzY1kfy0W2bH2-hDVx0serq25G6ybLLYbXEF9RCdp_40wOcavgF-yUezpYEOVH6i1xcoPmi6lia01ooZ6qWWDjpRr9RSElMfyYzDOfeYq-RxJI47OdumDj9njHQuUJpQuYLwwEJtxs1kfESmKa19OYvP8bPPrFzkKLktVKcjdjOuCh6uANdAky-Eat33AdUGgFq6gpMk1_sgDU28zDvQkNEl259Dt3X0Mnjbhrdz5bJqLdW4v_gYmgKQ5F2RWSCB8AZsdsIwRd2trCzIN5irwc-9ExwBqsewmpz8pJD-uPnPZ_F2gBy8LE1G7rX1pkeaRlK3V8dFFUr3PrSmsUBthTyiftyyKyXRZ1l3Vx3RRcJXnV2FQ0EV8b3EaFlyCgI-nGODOXijW82CSB3vHhrfBqrU-rFxyW2JqZRxd2Bm909KNGtLu01b1qls93yiT9uWfmLQG-78YTkLwiDgvM7VUTIT_oa_T6iY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f8294db6.mp4?token=JuwG81yY5bYAQeepzXflnCONUz-eheJY9dUggw_ua7cEqbZWZ37kRyjLClpx4xO99Vz6JE_UPjPkPM5yFzpQskB7vBVtKWmZ4atRYF2IDxIS6XVDz3_kunhOiPOXoVlxeigUr9Dc7CEKwT1NViZElN1-_FydiCNHOOHaCJmmqpvYvzB_eZ9M2bN1WlrYydHzPBMDtSKB0q9QzY1kfy0W2bH2-hDVx0serq25G6ybLLYbXEF9RCdp_40wOcavgF-yUezpYEOVH6i1xcoPmi6lia01ooZ6qWWDjpRr9RSElMfyYzDOfeYq-RxJI47OdumDj9njHQuUJpQuYLwwEJtxs1kfESmKa19OYvP8bPPrFzkKLktVKcjdjOuCh6uANdAky-Eat33AdUGgFq6gpMk1_sgDU28zDvQkNEl259Dt3X0Mnjbhrdz5bJqLdW4v_gYmgKQ5F2RWSCB8AZsdsIwRd2trCzIN5irwc-9ExwBqsewmpz8pJD-uPnPZ_F2gBy8LE1G7rX1pkeaRlK3V8dFFUr3PrSmsUBthTyiftyyKyXRZ1l3Vx3RRcJXnV2FQ0EV8b3EaFlyCgI-nGODOXijW82CSB3vHhrfBqrU-rFxyW2JqZRxd2Bm909KNGtLu01b1qls93yiT9uWfmLQG-78YTkLwiDgvM7VUTIT_oa_T6iY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری ایرانیان با پرچم‌های سرخ خون‌خواهی در شب اربعین حسینی در کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/678207" target="_blank">📅 23:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678205">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
حماس: منتظر پاسخ رسمی و روشن میانجی‌گران درباره توافق هستیم
🔹
یک منبع مسئول در جنبش حماس اعلام کرد این جنبش و گروه‌های فلسطینی همچنان به توافق‌های انجام‌شده درباره اجرای مرحله دوم آتش‌بس پایبند هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/678205" target="_blank">📅 23:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678204">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f726e8cb.mp4?token=DQluHcuOiC_6leRffmWTpxFxskbuK9fCzX1Ue4AZjN2DtRwxLFoUvtC5cEsB2ov7lhCmCmQokz6e9Joj3jW_gR_d0RVU1UQHnSd20aPbrqq3AUaoiHInO1MyKGB0TaNXgPz0n7zf7RAnvR6ZaPjpTP1JwVZvtJE5qa06bFPxZh_5pQ5oVqRQAngJ05pyrdgrctfECveT4LdGaclgI1_cDCxczch53JWk_Ezo0Zsn3-MmnvwFyVfQUf9QAMZCKRlE6ZBtjMF9RgNEZNOk8lsp8XTcGPk1FV4RymsxN6tww0RlhkPTAZQ_2YSniVoBSvPSiFn1uhjA4DpkeaIv_IhNh0Lp7onWw-rMYSh7kstidkWxPD4wrfhdWz2TnENT8U6wDoKssDruBGNykQBS-bBPG48sdc_Q3ikL_0d6raphuU1TEu6uWJYDM3W893tIfaNHqguvoZUb0RQ1TpfmsFWXNRy_ZnDcNn_-rNqDWFcf-cb9JoI5-zAvudLeAPN_b9t7mctTEOFhAElSJS2-1JmJIrHBCe65Em1lm_w-K9NmqTJVf8THAcb718dnRVfezUiBjmb6wNBoZdXdzQcPAXJICTFL5bn4civxjI4wOdd1PYBcY1wAgffQqHEW7Dn4IbJHaIZrQ1CKXbdW19ZLsIPjSHSFcKSOx9_TLTpMeSt_qU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f726e8cb.mp4?token=DQluHcuOiC_6leRffmWTpxFxskbuK9fCzX1Ue4AZjN2DtRwxLFoUvtC5cEsB2ov7lhCmCmQokz6e9Joj3jW_gR_d0RVU1UQHnSd20aPbrqq3AUaoiHInO1MyKGB0TaNXgPz0n7zf7RAnvR6ZaPjpTP1JwVZvtJE5qa06bFPxZh_5pQ5oVqRQAngJ05pyrdgrctfECveT4LdGaclgI1_cDCxczch53JWk_Ezo0Zsn3-MmnvwFyVfQUf9QAMZCKRlE6ZBtjMF9RgNEZNOk8lsp8XTcGPk1FV4RymsxN6tww0RlhkPTAZQ_2YSniVoBSvPSiFn1uhjA4DpkeaIv_IhNh0Lp7onWw-rMYSh7kstidkWxPD4wrfhdWz2TnENT8U6wDoKssDruBGNykQBS-bBPG48sdc_Q3ikL_0d6raphuU1TEu6uWJYDM3W893tIfaNHqguvoZUb0RQ1TpfmsFWXNRy_ZnDcNn_-rNqDWFcf-cb9JoI5-zAvudLeAPN_b9t7mctTEOFhAElSJS2-1JmJIrHBCe65Em1lm_w-K9NmqTJVf8THAcb718dnRVfezUiBjmb6wNBoZdXdzQcPAXJICTFL5bn4civxjI4wOdd1PYBcY1wAgffQqHEW7Dn4IbJHaIZrQ1CKXbdW19ZLsIPjSHSFcKSOx9_TLTpMeSt_qU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان مرشایمر: ایران برندۀ جنگ شده اما ترامپ از پذیرش این واقعیت سر باز می‌زند و در وضعیت فاجعه‌باری گرفتار شده؛ او هیچ راهبرد نظامی معقولی ندارد و فاقد هرگونه دکترین پیروزی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/678204" target="_blank">📅 23:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678203">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
وقوع انفجار مهیب در حماه سوریه
🔹
هنوز علت این انفجار مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/678203" target="_blank">📅 23:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678201">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVup0fv5IYrQgx_n0SWUvSleToy8kX3t5QaRgZIT84--RdJKmcoQjKZUVxinssRkj3GAeK4ZpLViqwodvKsUsb0AJRTkmdw2Sgqq44kfoTBcd2YhEQh7TPxNFUIaxM6z4zfBox4aHrMyNoj9M58E3Sg7HGc_LYXGcwCuP94hJgNLtureBP58Cyd9sjyxtpF4nE5kcAacUyWNgm7KwWaUD1atHEZvLT0uQdDVz8xKJ5nq5PUW1GI9rOzmaMZQq0n8cJGxbOYz-246gGVRlOByxXvkzSrB8pdkPdnTuVKbkMOTX0Mg1apGoM_GQU4wiDJKgo-1Ih5clbzSWxqcGTcxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز یک برنج قدکشیده؛ این اشتباهات را تکرار نکنید
🍚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/678201" target="_blank">📅 23:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678200">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یک منبع ارشد سیاسی در تهران به خبرنگار المیادین گفت:
🔹
ایران مذاکره ای با آمریکا نداشته است و رییس جمهور دروغگوی این کشور به جای پذیرش مسئولیت خود در به هم زدن تفاهم نامه، همچنان در حال فرافکنی است.
🔹
مذاکرات ما با طرف عمانی است؛ عمان یک همسایه ابدی با ایران است و تنگه هرمز هم صرفا در محدوده آبهای سرزمینی این دو کشور قرار دارد و آمریکا که تاکنون بعنوان یک نیروی شر و ناامن‌ساز عمل کرده است نمی تواند خود را به عنوان منجی منطقه جا بزند.
🔹
باز یا بسته بودن تنگه هرمز تابعی از وضعیت کلان منطقه است و قطعا در وضعیتی که اقدامات تجاوزکارانه آمریکا و محاصره دریایی و دیگر اقدامات ایذایی آمریکا علیه ایران ادامه داشته باشد، این تنگه باز نخواهد شد
🔹
مشکل منطقه ما، حضور آمریکایی هاست وگرنه هیچ کدام از کشورهای منطقه طالب جنگ نیستند و همه می دانند که خسارات دیوانگی های نتانیاهو و ترامپ، برای شان بسیار پر هزینه شده است
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/678200" target="_blank">📅 23:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678199">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
آمار دقیق از میزان خسارت جنگ در تهران؛ کدام مناطق بیشترین آسیب را دیدند؟
👇
khabarfoori.com/fa/tiny/news-3235347
🔹
کالابرگ مرداد برای این افراد واریز نمی‌شود
👇
khabarfoori.com/fa/tiny/news-3235308
🔹
چه کسی در جلسه شورای دفاع در نهم اسفندماه ۱۴۰۴ به جای سردار رادان حاضر شد و به شهادت رسید؟
👇
khabarfoori.com/fa/tiny/news-3235132
🔹
تصویری از تغییر چهره ضرغامی؛ او دچار سکته مغزی شده بود؟
👇
khabarfoori.com/fa/tiny/news-3235351
🔹
تعطیلی ادارات در این استانها در روز چهارشنبه (14 مرداد 1405)
👇
khabarfoori.com/fa/tiny/news-3235258
🔹
با نصب اپلیکیشن خبرفوری، از خبرها جانمانید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/678199" target="_blank">📅 23:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678198">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
سرلشکر رضایی: ما در تنگه هرمز مسئولانه عمل می‌کنیم و ضمن امنیت خودمان امنیت دنیا هم برایمان مهم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/678198" target="_blank">📅 23:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678197">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecccd3a4fe.mp4?token=b1KZ-49fYBvCI2l67MxtiQGbS_a5ET1-4sB7Rno_jFmgvWAHVNQDc62YBMUFYNymX8i5XNkBwFVLLCkY8-hbxMvIhCzo8K9rj0Qq-GV7EHr1rxU13KXon5Il9l7QT3RtM-8K-AAXPrla3E5enh8P4OJEujTlvSsATPEocFGMFPKq7lzCCuk7tXxdCeUNx4OiBV7ZMD-f8RrO37wrJx98czCKYf_ZoVwAvk3KpgR61ByOZFO6BlfbldhzE3t0wThVYBaHA5kL8TnX4LcnbhsPzpFvIUxOmw3NXoX3WDxlcucE0URQaRWYwFBopUHc_mLW70SooErCZU3v1JiKgML4IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecccd3a4fe.mp4?token=b1KZ-49fYBvCI2l67MxtiQGbS_a5ET1-4sB7Rno_jFmgvWAHVNQDc62YBMUFYNymX8i5XNkBwFVLLCkY8-hbxMvIhCzo8K9rj0Qq-GV7EHr1rxU13KXon5Il9l7QT3RtM-8K-AAXPrla3E5enh8P4OJEujTlvSsATPEocFGMFPKq7lzCCuk7tXxdCeUNx4OiBV7ZMD-f8RrO37wrJx98czCKYf_ZoVwAvk3KpgR61ByOZFO6BlfbldhzE3t0wThVYBaHA5kL8TnX4LcnbhsPzpFvIUxOmw3NXoX3WDxlcucE0URQaRWYwFBopUHc_mLW70SooErCZU3v1JiKgML4IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سید عباس عراقچی وزیر امور خارجه در راهپیمایی اربعین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/678197" target="_blank">📅 23:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678196">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
سرلشکر رضایی: اگر محاصره ادامه پیدا کند برای ناوهای آمریکا خطرات جدی به‌وجود خواهد آمد
🔹
آمریکایی‌ها باید رفتار خود را تغییر دهند وگرنه ما این شرایط را تحمل نخواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/678196" target="_blank">📅 23:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678195">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
گاردین به نقل از یک مقام ارشد پاکستانی: عاصم منیر برای جلوگیری از تشدید بیشتر تنش در منطقه، با ونس و ویتکاف در تماس نزدیک بوده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/678195" target="_blank">📅 23:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678194">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
سرلشکر رضایی: دست‌وپازدن ترامپ ممکن است جرقۀ آغاز جنگ جهانی سوم را بزند
🔹
خلیج فارس و تنگۀ هرمز چاشنی بسیار خطرناکی برای جنگ جهانی سوم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/678194" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678193">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
محسن رضایی: آمریکا باید رفتارش را عوض کند؛ اگر آمریکا به شروط تفاهم‌نامه عمل کند می‌تواند نشان از تغییر رفتار باشد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/678193" target="_blank">📅 22:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678192">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
یک منبع بلندپایه ایرانی به المیادین: رئیس‌جمهور آمریکا که به دروغگویی عادت دارد، همچنان دیگران را سرزنش می‌کند به جای آنکه مسئولیت ناکامی خود در به شکست کشاندن تفاهم را بپذیرد
🔹
مذاکرات ما با همسایه همیشگی‌مان، سلطنت عمان، در جریان است، به ویژه آنکه تنگه…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/678192" target="_blank">📅 22:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678191">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
محسن رضایی: آقای ترامپ شما در خواب و رویا عملیات بزرگ‌تر از جنگ جهانی دوم داشتید، پس چرا پای نیروهای شما در خاک ایران نیامد؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/678191" target="_blank">📅 22:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678190">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
یک منبع بلندپایه ایرانی به المیادین: رئیس‌جمهور آمریکا که به دروغگویی عادت دارد، همچنان دیگران را سرزنش می‌کند به جای آنکه مسئولیت ناکامی خود در به شکست کشاندن تفاهم را بپذیرد
🔹
مذاکرات ما با همسایه همیشگی‌مان، سلطنت عمان، در جریان است، به ویژه آنکه تنگه هرمز منحصراً در آب‌های سرزمینی دو کشور قرار دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/678190" target="_blank">📅 22:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678189">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e83ea2b385.mp4?token=iHEYJwuxHM_1Mshg4DgnrZcv_3zjo_Zon1HQVO20QfSC9cG-J60jdXU3QWMWgbWFkTBiH0XGaJfDLAqCat0kpD6LMgti_LqvY-2wG7ofFpQipIx6s1XI5qgBqeN3gACIxKebXUWLif9nLLFVf27c0V0Umr4F-j7-9wGMefE6zNsZhAk6nhSp0wtpmL6cRvJipBZkm_-HY0J0gz67WnB0x9ojw0-MsdHm3CISx2-9T4YkvUEbKRT27OcCc3_UVq2HRkUIg8tC3Nyb18BNfA-xNHeSew0qZXe-bxT1JXsszbowhQEODw-JXDu2pV-GGM80cKJmYHzQechggmxnwOHhvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e83ea2b385.mp4?token=iHEYJwuxHM_1Mshg4DgnrZcv_3zjo_Zon1HQVO20QfSC9cG-J60jdXU3QWMWgbWFkTBiH0XGaJfDLAqCat0kpD6LMgti_LqvY-2wG7ofFpQipIx6s1XI5qgBqeN3gACIxKebXUWLif9nLLFVf27c0V0Umr4F-j7-9wGMefE6zNsZhAk6nhSp0wtpmL6cRvJipBZkm_-HY0J0gz67WnB0x9ojw0-MsdHm3CISx2-9T4YkvUEbKRT27OcCc3_UVq2HRkUIg8tC3Nyb18BNfA-xNHeSew0qZXe-bxT1JXsszbowhQEODw-JXDu2pV-GGM80cKJmYHzQechggmxnwOHhvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این اپلیکیشن‌ها حرفه‌ای‌تر، سریع‌تر و هوشمندتر کار کنید
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/678189" target="_blank">📅 22:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678188">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
چرا آمریکا در حملات اخیر اسرائیل را دخالت نداده است؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/678188" target="_blank">📅 22:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678187">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f4a2d6b2.mp4?token=oAwnvG8kxoZHhvjaCukJNdP2N7-0l3ne0TwqyCt5a8LLnutTgeFgheB8V6-hzZfGqk76hAl4-nXFMSTCMOPLwArQ7ulKVwwFv8YLmwm_L1QV-Ud1YjX1OreJ1R2uRnj3P-nBDknvJCxNUd-I7-41XStFZlRXEOx2RpWNjE8CqmGfYtsLB3AZ6hRP5bxPHOro6MlxyPgHfio5dSpSvnBay-2EBr0bRxNIybm6aca1SKO_RXt-pCn59laV0ZdgMkRc6iNMlsuOh4DcZogcLBbB6AaDr9Bij877bQB3Q5ItSnrXN1gfKw9hao7IjwzGZF3y0T9IMUpCE7G_oBgsnZQhRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f4a2d6b2.mp4?token=oAwnvG8kxoZHhvjaCukJNdP2N7-0l3ne0TwqyCt5a8LLnutTgeFgheB8V6-hzZfGqk76hAl4-nXFMSTCMOPLwArQ7ulKVwwFv8YLmwm_L1QV-Ud1YjX1OreJ1R2uRnj3P-nBDknvJCxNUd-I7-41XStFZlRXEOx2RpWNjE8CqmGfYtsLB3AZ6hRP5bxPHOro6MlxyPgHfio5dSpSvnBay-2EBr0bRxNIybm6aca1SKO_RXt-pCn59laV0ZdgMkRc6iNMlsuOh4DcZogcLBbB6AaDr9Bij877bQB3Q5ItSnrXN1gfKw9hao7IjwzGZF3y0T9IMUpCE7G_oBgsnZQhRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: انگلیس کشور ورشکسته است
رئیس دولت تروریستی آمریکا که بوی نفت در دریای شمال به مشامش رسیده است در ادامه اراجیف خود:
🔹
انگلیس یک کشور ورشکسته است. اگر نفت دریای شمال را آزاد کند، به کشوری ثروتمند تبدیل خواهد شد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/678187" target="_blank">📅 22:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678186">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=oEKWvh4iAI5eRo-n9mIFmQpm8tTfmcnFZXtekJCmxnTvIKVw7esEYzsmle9kCgXc4tNAPuTR9nX71kIP71OQigOMArs-pupC7W1IjcrSa0T-Ty1RQc1CtUOfviDB-dt4_6wklvuD7OcV_u_aC-lkxj1lwhffnvZ1MHygaAQP-Zq2J4G_9Un1jxfLOmWfk9pD-LuKVmRJZ9BNbhG9D6suvewrsX2UAyzkZ5FOHhpz0_24SZf2iWpG1SI7BIq_VSNzDcrpUROyJVTEYKEs5Ydt8PkW4V49ah1H9rGiVtaxv3SN5uldHgCXOKWRH_qUZbUFy7g0W0cNZS84ITTds1R2MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=oEKWvh4iAI5eRo-n9mIFmQpm8tTfmcnFZXtekJCmxnTvIKVw7esEYzsmle9kCgXc4tNAPuTR9nX71kIP71OQigOMArs-pupC7W1IjcrSa0T-Ty1RQc1CtUOfviDB-dt4_6wklvuD7OcV_u_aC-lkxj1lwhffnvZ1MHygaAQP-Zq2J4G_9Un1jxfLOmWfk9pD-LuKVmRJZ9BNbhG9D6suvewrsX2UAyzkZ5FOHhpz0_24SZf2iWpG1SI7BIq_VSNzDcrpUROyJVTEYKEs5Ydt8PkW4V49ah1H9rGiVtaxv3SN5uldHgCXOKWRH_qUZbUFy7g0W0cNZS84ITTds1R2MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا آمریکا در حملات اخیر اسرائیل را دخالت نداده است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/678186" target="_blank">📅 22:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678185">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003c87529a.mp4?token=eBaW3doIybFFdiBMgqZIWeS5VpBGQpiQy1VPyWAiHCXpdnhhjpWSB7b3_qqbCkZH2fClI_iHXB8spkxMP7m0ucj0Cm9bjz9zCvfUyGNuAXwN5a2mvEAe7SNXIyCv83bgXWwGttnbPbu4uPV1Av64ear2CZQDRdxhn38hPA3NeZxCLePYQ2dnNd2VGBk3KGUeuU52N4u0khARX_VRt_tUnm2Yws6JYXvC8PXZfL9LTNuoNPRI9QVaD-WvWPSjhVYuzKKabE9me5DXVcg3ATsfxLUHmnTNEDo-oP8Z97Y6tHQv9ZuEpDwvGBwc0VI8aupr5WeCGoDtZimGE2YZNFLyaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003c87529a.mp4?token=eBaW3doIybFFdiBMgqZIWeS5VpBGQpiQy1VPyWAiHCXpdnhhjpWSB7b3_qqbCkZH2fClI_iHXB8spkxMP7m0ucj0Cm9bjz9zCvfUyGNuAXwN5a2mvEAe7SNXIyCv83bgXWwGttnbPbu4uPV1Av64ear2CZQDRdxhn38hPA3NeZxCLePYQ2dnNd2VGBk3KGUeuU52N4u0khARX_VRt_tUnm2Yws6JYXvC8PXZfL9LTNuoNPRI9QVaD-WvWPSjhVYuzKKabE9me5DXVcg3ATsfxLUHmnTNEDo-oP8Z97Y6tHQv9ZuEpDwvGBwc0VI8aupr5WeCGoDtZimGE2YZNFLyaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: دشمن برای باز کردن تنگه هرمز میخواست یک کار زمینی انجام دهد/ میخواست ارتباط استان‌های جنوبی و شمالی را قطع کند و پل‌ها را زد
🔹
طرح ناپخته فرمانده‌های ارتش آمریکا باعث شد حمله زمینی و هوایی متوقف شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/678185" target="_blank">📅 22:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678184">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
محسن رضایی: مقام معظم رهبری اجازه امضای تفاهم‌نامه را دادند و رئیس‌جمهور محترم هم امضا کردند/ ترامپ در کنار آقای مکرون یک شوی جهانی درست کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/678184" target="_blank">📅 22:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678183">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
محسن رضایی: با پاسخ شدید موشکی - پهپادی ایران در آن ۱۷ روز آرزوی ترامپ برای فتح‌الفتوح به در بسته خورد
🔹
به آمریکا فهماندیم هم موشک داریم و هم توان دفاع.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/678183" target="_blank">📅 22:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678181">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
محسن رضایی: با پاسخ شدید موشکی - پهپادی ایران در آن ۱۷ روز آرزوی ترامپ برای فتح‌الفتوح به در بسته خورد
🔹
به آمریکا فهماندیم هم موشک داریم و هم توان دفاع.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/678181" target="_blank">📅 22:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678180">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b694f704fb.mp4?token=enwF_IHaFdki5U5h9xhqHiJ2gaGbzqjjXkM7OmKCShyzkXs4LWwGGedtXQKViRFQdzF7eSg1RVFjN26l8E_opQ_94wX-0dmavjV3dA9Ty5oieQ9X7EEx1Tq2cbBIjpWPpA-LK_J4Z8fj2DQWh6qtmjyRYnQSOxWoVJ8cGz9FG2A0wcEKUtzd2A_TH6quJRhJj_yf1NfWzqujdNHoiy5kunnlu7c8C_sZsu1RJe6FefQenHzsHJRfkc2ZpIo7gXVqRrUkN-d-mJqQJsD0NUI_mEdrvTLJut0sDpFcsvyw653xcUPkFkXT_68ia0Xe4IivQKN0jcUAMSfyxFAkOHs0JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b694f704fb.mp4?token=enwF_IHaFdki5U5h9xhqHiJ2gaGbzqjjXkM7OmKCShyzkXs4LWwGGedtXQKViRFQdzF7eSg1RVFjN26l8E_opQ_94wX-0dmavjV3dA9Ty5oieQ9X7EEx1Tq2cbBIjpWPpA-LK_J4Z8fj2DQWh6qtmjyRYnQSOxWoVJ8cGz9FG2A0wcEKUtzd2A_TH6quJRhJj_yf1NfWzqujdNHoiy5kunnlu7c8C_sZsu1RJe6FefQenHzsHJRfkc2ZpIo7gXVqRrUkN-d-mJqQJsD0NUI_mEdrvTLJut0sDpFcsvyw653xcUPkFkXT_68ia0Xe4IivQKN0jcUAMSfyxFAkOHs0JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای خصمانه و گستاخی خوک زرد درباره ایرانی‌ها: قبل از بین بردن و کشتن ایرانی‌ها فرصت بدهید؛ اجرای برنامه ریزی هایمان بسیار دشوار است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/678180" target="_blank">📅 22:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678179">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcFAoyOOri4xJkbJVYMcpx0OXz7zG3v3S6apAG0IWNsRykERLNGTC5BWYmmT5t7aEhpcD9hS7ShKRtuEeWrEfOf5olSlKw9jc0YsM1fj_nNOB_yKRCnhOOIR6KDNEheRwpjcVGwC-DIHbUO89k94qUhsgneoACIi3Nnapv_vYQt5MCftlyF4tbPL2n0aAZakf1tjqRbGM0_kKkGnUbmCZqbSz2pa6KCyQWLUotnvoLK5vOGB2om7gqzsUfBU-LF-0MPCSSaI92uD1VFUUIDXjPogMGStwBKv89C3_SHYfxG4HXuNfRteJnxkgf-mitUwmNCDk8xywXPd8V5WjIwKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرصت‌ها مثل ابر می‌گذرند؛ آرام، سریع و بی‌خبر
🔹
در حکمت ۲۱ نهج‌البلاغه، امام علی(ع) یادآوری می‌کند که فرصت‌ها ماندگار نیستند. بعضی لحظه‌ها فقط یک‌بار از راه می‌رسند و اگر قدرشان را ندانیم، شاید دیگر تکرار نشوند.گاهی یک تصمیم به‌موقع، می‌تواند مسیر زندگی…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/678179" target="_blank">📅 22:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678178">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeef354708.mp4?token=V2Pt6GySOmACanIRJUTzCPaUqBFUSG48eSr8Drl2j0nAz66QhS4lpY0KM8vwgZOXwpk7ICdEVcj4lB8V81yqHjNSAKje5xDnt-oalCK7_UW0roS8OZuis0z0YwNLjX7qHSLh3eKm_PqSWeAw0H_wPwlWoU4WB49s9SgTjSecn_FTSGuc8cB0QDjg1SqAjqmOt-439XQ8qmcxGLOKS8WJ5KTOAeAS6S3NopmEU9UZNMAVqGh9DcI2BYklDmWyE7cji4R2JYA1KtbkboH75ROp4qbH3HjQyE1a8EhmVWFVHYCNhhhXdzQvR0s60K_EBFT3P4S63Bp10jPvGiIRLCVoMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeef354708.mp4?token=V2Pt6GySOmACanIRJUTzCPaUqBFUSG48eSr8Drl2j0nAz66QhS4lpY0KM8vwgZOXwpk7ICdEVcj4lB8V81yqHjNSAKje5xDnt-oalCK7_UW0roS8OZuis0z0YwNLjX7qHSLh3eKm_PqSWeAw0H_wPwlWoU4WB49s9SgTjSecn_FTSGuc8cB0QDjg1SqAjqmOt-439XQ8qmcxGLOKS8WJ5KTOAeAS6S3NopmEU9UZNMAVqGh9DcI2BYklDmWyE7cji4R2JYA1KtbkboH75ROp4qbH3HjQyE1a8EhmVWFVHYCNhhhXdzQvR0s60K_EBFT3P4S63Bp10jPvGiIRLCVoMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک کثیف درباره ایران: به من زنگ می زنند و می گویند: لطفا حمله نکنید، معامله می کنیم
🔹
این حقیقت مطلق است و همه آن را می دانند.
🔹
چه کسی تماس نمی گیرد؟
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/678178" target="_blank">📅 22:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678177">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65010e1c6b.mp4?token=J9TjtN6Q4Yv57OH0NQ3cb0wxe-bKkdo12937rfeW9YrLVGaY3sJnWbQRI4DteOSxieBdS84eyPsA6E8oeRykjXUKkA0wq2TylPBxKh6c38PQViLKk0hXq6avgN9WsQyzfkRfqIJiq4aOC4FB8ErumV65CyqNs--JGSjGAHERSx4xS5iy8gY9pRtZUVCq53bo0WsmEkOfjQwS0o_G0ZV3JBFkR4Htzkdavsd6bgp0Q_3RF-IUL1_np7h-sJqNf_XiBd65nnzgxM2GtIHHFOrnQn4XmrfRAF_rfwiexmqb9eFCdfSrCyQ33I2DDqdnSCYO4aakBGVxAQfJGNM6GCTjuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65010e1c6b.mp4?token=J9TjtN6Q4Yv57OH0NQ3cb0wxe-bKkdo12937rfeW9YrLVGaY3sJnWbQRI4DteOSxieBdS84eyPsA6E8oeRykjXUKkA0wq2TylPBxKh6c38PQViLKk0hXq6avgN9WsQyzfkRfqIJiq4aOC4FB8ErumV65CyqNs--JGSjGAHERSx4xS5iy8gY9pRtZUVCq53bo0WsmEkOfjQwS0o_G0ZV3JBFkR4Htzkdavsd6bgp0Q_3RF-IUL1_np7h-sJqNf_XiBd65nnzgxM2GtIHHFOrnQn4XmrfRAF_rfwiexmqb9eFCdfSrCyQ33I2DDqdnSCYO4aakBGVxAQfJGNM6GCTjuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: من می خواهم قبل از اتخاذ اقدامات شدید، هر فرصتی را که می توانم به ایران بدهم
🔹
امیدوارم به خود بیایند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/678177" target="_blank">📅 22:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678176">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isAqfNhZEddtR09UML9mY3nwhlx1cLY7KODtg3jNMCXwNW6wIWYyapstboQY_uDEzK2kwfwnaX5RCVmnrY6tXA2slKpEh4vGbmWJTCvz6X7xqUwTw2Dn_rNlTpoQ23zpEvLhBRjOJqXNeHNFhfguQAUy6bb2D1apeTEDLszbcwqBkABclyVuo1Xy9D-CfmuqBKIN1GSe--CVBkG7FX12ne-hBejLLDyYVU4FtDyEtIhFJXMqJL0UP6dNsIPJIdIDKPuwb6bRH7L7sRJsJwjaZ3BZeHSBfAcLIitSmF3kwYbyQEb0B67rJrVYYUMGdbieAOwTo64WV0dPDEp17_ZwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نوبت به بیمه ثالث موتور رسید!
یک موتورسوار حرفه‌ای همیشه برای مسیرش برنامه‌ریزی می‌کنه. خرید بیمه شخص ثالث هم بخشی از این برنامه‌ ریزیه که امنیت خاطر شما رو در هر تردد تضمین می‌کنه.
✅
برای اینکه با خیال راحت تردد کنید،
بیمه‌بازار
خرید بیمه ثالث موتور رو براتون ساده کرده:
•
مقایسه سریع
قیمت شرکت‌های مختلف
•
خرید اقساطی
•
صدور فوری و آنلاین
👈
خرید قسطی بیمه
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/678176" target="_blank">📅 22:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678173">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a224327602.mp4?token=pKZz-yjhE-1_-HckiqFpcD24__1uWYbGzq5Hex9u5aktwGAGRWtUBOrC08AoowPEFyc_1aw2hyR-6muAy3L5q_HflCrBKQ42RoFn13ZDrctrYd4yL2T1KjAMWLt85c4jgOPA7OEw1O_cbcRJWCMiWnjCcNvSwnkDgNFEoNsL0-4WrdwjeCKEBmyBNKvWMYVgxEpk7IkLtfeojb1a-BEZrbpA3W6mzz8vQR-WXbUTDQSNXlSd6ZJjGu8WZpqZPIbCgnNrZzCmRbYQrZMQO5ztdroBUSe3Ci7nh_RvkKmsNT8NXhzQObMusEbONP_0uXj6ugLe7Ii9FcNzR_v32j-lsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a224327602.mp4?token=pKZz-yjhE-1_-HckiqFpcD24__1uWYbGzq5Hex9u5aktwGAGRWtUBOrC08AoowPEFyc_1aw2hyR-6muAy3L5q_HflCrBKQ42RoFn13ZDrctrYd4yL2T1KjAMWLt85c4jgOPA7OEw1O_cbcRJWCMiWnjCcNvSwnkDgNFEoNsL0-4WrdwjeCKEBmyBNKvWMYVgxEpk7IkLtfeojb1a-BEZrbpA3W6mzz8vQR-WXbUTDQSNXlSd6ZJjGu8WZpqZPIbCgnNrZzCmRbYQrZMQO5ztdroBUSe3Ci7nh_RvkKmsNT8NXhzQObMusEbONP_0uXj6ugLe7Ii9FcNzR_v32j-lsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از آسیب‌دیدگی برخی ایستگاه‌ها و پالایشگاه‌های شهر ینبع عربستان پس از حملات اخیر انصارالله یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/678173" target="_blank">📅 21:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678172">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moL1Sk-T4bRRZdfsfdMAXpE3Hc_1QezkgqQpVMqtscNICaWXmQ0A-T08de4z3Sf-UTp9AU1K-ThrWJV8Lphhm7pgPCb0s4s33yhXrnDo9DQVtsXXLNkWZg3rcatfwwPpwXHJ6DiQiKz2MtagcPo9ZVLi7P-SqzOiQNAitxt3Xrer_xigLYTGRqBF5c3euHgfyS1ngwK5yy1lxo4y2zg8TIu1wGK3rr7-4JQRikbZ0c9854hGFskGzv0qhRPuu8SVG6w_jSx9S2O9IeiAaJeQdtzdy8h5Yin9v4m0ysfY31F99Bn2WMyeAdvKfhd1CpwkH1KSpYyILVNkt3alXJH5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زهرا، نوه خردسال آقای شهید ما هم اربعین امسال این‌گونه زائر حرم سیدالشهدا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/678172" target="_blank">📅 21:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678170">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75a71f2f93.mp4?token=XYukc3qgeil8ByitIM6fuGnyZiLAkRF7HAdHMyGfuTbpj2u3ipCJ2TZ9-_t01iw9_Kd_qCmzzD6hHf6yWql9J5U_CmNUk_V8GBukw2XLjprpd_KOtbCWLNms_bPAY-LBquQe1SlvQElz5jOnNVEVCev0n5DzcCKAUExxBNk8Umy3lbxLijGeculZpGAst2JpTcr_3AI9KZv5CUXryNJb3mGY3xIlYXbyaon81y5Yoqlt2xRgWDz5ehFT39JIubjXnUfLGJUa1T3VARYmP9S0AP2w4tDFBSVhhL5r1DCZB-TRdIsEFpSvMKPxIU9CazRLOCBlCsBNvcjyqxtx7PcykA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75a71f2f93.mp4?token=XYukc3qgeil8ByitIM6fuGnyZiLAkRF7HAdHMyGfuTbpj2u3ipCJ2TZ9-_t01iw9_Kd_qCmzzD6hHf6yWql9J5U_CmNUk_V8GBukw2XLjprpd_KOtbCWLNms_bPAY-LBquQe1SlvQElz5jOnNVEVCev0n5DzcCKAUExxBNk8Umy3lbxLijGeculZpGAst2JpTcr_3AI9KZv5CUXryNJb3mGY3xIlYXbyaon81y5Yoqlt2xRgWDz5ehFT39JIubjXnUfLGJUa1T3VARYmP9S0AP2w4tDFBSVhhL5r1DCZB-TRdIsEFpSvMKPxIU9CazRLOCBlCsBNvcjyqxtx7PcykA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک کودک کش: من به ایران اجازه نمی‌دهم هزینه‌ای دریافت کند
🔹
اگر قرار است کسی شارژ کند، این ما هستیم.
🔹
ما کنترل کامل داریم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/678170" target="_blank">📅 21:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678169">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21c4ec7f1.mp4?token=VdgpN52-IzIxOSOznOnuFiaxAbA9poDNrn-ILtU-x1WVs043RQ-u79IiUZGTcnYN6bpBxZuvTjONgwbpAAYuQw3-ojg6kql0oisugKg3lmRVA9Z5e9FUheXMC5xpZDNRl7vicvdg5dFio9pmRbQbcTuW2AuKXEmvnRZRGQRHT7LqQ2x7Jb2gAcwrpYMC-REfOS6ic3e6LDSLeL6CV9jN5vmg3rGRKGEFUzs_GEu4KzfAM_jmYA6TOUGo9dd4Iah5C4r24voANAlENiUuKTHZOQsjB0VD5-3KM95-0t0-T87H3O19JQWeT7w5HW-ENABTMib3X6AExATnqjHKLQ1wyZDc7S_LZbxKOb_OsANSR3LAa5iIWATdnKADWJK2ZMexRJ5xoSofK1CXKR9U_ul7zxiSA3PHORTLh9snUIxTDpNcOK-CVJqoanSRe6Xm-BezyD7erhtPUmLAgZ9DAYXW6moJh6byMKCtaqw0PyCIMZVhKzEhusetxJRnAv5nGxDDlFHxI_8ILEs2YxQbMznLT-Ej8Pexxis3CsdzXP95ELcpBw1rn57OPLkxjScSUbYQ8KkSPLCCZebIh3eNXOTHLnmzaWZgoeAmDwdja3Arlaxw1iqp7hZZvTlv5ocD-PU8RxVaNfzddKaNEHaI5iqFBdjKlWu6Aji5YogW42M48TY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21c4ec7f1.mp4?token=VdgpN52-IzIxOSOznOnuFiaxAbA9poDNrn-ILtU-x1WVs043RQ-u79IiUZGTcnYN6bpBxZuvTjONgwbpAAYuQw3-ojg6kql0oisugKg3lmRVA9Z5e9FUheXMC5xpZDNRl7vicvdg5dFio9pmRbQbcTuW2AuKXEmvnRZRGQRHT7LqQ2x7Jb2gAcwrpYMC-REfOS6ic3e6LDSLeL6CV9jN5vmg3rGRKGEFUzs_GEu4KzfAM_jmYA6TOUGo9dd4Iah5C4r24voANAlENiUuKTHZOQsjB0VD5-3KM95-0t0-T87H3O19JQWeT7w5HW-ENABTMib3X6AExATnqjHKLQ1wyZDc7S_LZbxKOb_OsANSR3LAa5iIWATdnKADWJK2ZMexRJ5xoSofK1CXKR9U_ul7zxiSA3PHORTLh9snUIxTDpNcOK-CVJqoanSRe6Xm-BezyD7erhtPUmLAgZ9DAYXW6moJh6byMKCtaqw0PyCIMZVhKzEhusetxJRnAv5nGxDDlFHxI_8ILEs2YxQbMznLT-Ej8Pexxis3CsdzXP95ELcpBw1rn57OPLkxjScSUbYQ8KkSPLCCZebIh3eNXOTHLnmzaWZgoeAmDwdja3Arlaxw1iqp7hZZvTlv5ocD-PU8RxVaNfzddKaNEHaI5iqFBdjKlWu6Aji5YogW42M48TY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: فردا آخرین فرصت ایران است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/678169" target="_blank">📅 21:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678168">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9041bec7.mp4?token=BY79VNZtkbqSV0OV99yfDSaG7t1R_MaIb5QcNdCa-xBsiLYv82X3YScHE_j503EUnGe7wkO9Z71IIuWF_pWomVgDP5-MvISPIZ-ZZjVlCALWMDuFCO9l8O4ducPG5n8Uk50EOvYyrexWbDdYmtUDwr2fk1Luc20hMvAgu0XxLqe24HqEbuEcvlVUH4UL0gMpPfowAU4MQW-EJ_o1q7Q5uu86bvyPMpLsaQ2b_f-D-GLL3XsZVBnV3MYL4n36ZkvFjQhHTB8tUs1QU0fgbmmLQA_EF03sV4wF9QhAvSmCeSKniOKgKcFMK9UM4nN6XOHel8XwR2XdKLc_Tdp3d4KIyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9041bec7.mp4?token=BY79VNZtkbqSV0OV99yfDSaG7t1R_MaIb5QcNdCa-xBsiLYv82X3YScHE_j503EUnGe7wkO9Z71IIuWF_pWomVgDP5-MvISPIZ-ZZjVlCALWMDuFCO9l8O4ducPG5n8Uk50EOvYyrexWbDdYmtUDwr2fk1Luc20hMvAgu0XxLqe24HqEbuEcvlVUH4UL0gMpPfowAU4MQW-EJ_o1q7Q5uu86bvyPMpLsaQ2b_f-D-GLL3XsZVBnV3MYL4n36ZkvFjQhHTB8tUs1QU0fgbmmLQA_EF03sV4wF9QhAvSmCeSKniOKgKcFMK9UM4nN6XOHel8XwR2XdKLc_Tdp3d4KIyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک پلید: مذاکرات به سرعت پیش خواهد رفت، این یا آن صورت. خیلی هم پیچیده نیست
🔹
ما در مورد باز کردن کامل تنگه هرمز فردا صحبت می کنیم.
🔹
سپس در مورد توانمندی های هسته ای ایران صحبت خواهیم کرد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/678168" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678167">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c6a2a1f36.mp4?token=V_pOxFL4IX4VednRZDkZyD1Agxw8E8N2EFu8sRFrEuwWjgF-xhOfc0Ij7plRkB-SJfcyBuGBiTDjN2FmyTfr5V6udmU39dWMU5Vrqkq_ljVhvvVZNOy38nfq8ffzuCxjKyA4aNLCUW7XP-Y4SAsIUGsWvy45kPKF4_FA04Jf5dXlxjxVMZWXaTURWdN8GJvvVu2vo9DrOKipiIHfrA03PSWktesYwAmIeG4betNHMXnoKbaHfd7wvMXMI2lidETau_N_h41UL7dNbyRFMUxraKr-ve_OGTT3WCfjD0AeywIupwbWxYUuRfo3I_g5-is9QPV7ySXDEmqAPnwTKXO3pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c6a2a1f36.mp4?token=V_pOxFL4IX4VednRZDkZyD1Agxw8E8N2EFu8sRFrEuwWjgF-xhOfc0Ij7plRkB-SJfcyBuGBiTDjN2FmyTfr5V6udmU39dWMU5Vrqkq_ljVhvvVZNOy38nfq8ffzuCxjKyA4aNLCUW7XP-Y4SAsIUGsWvy45kPKF4_FA04Jf5dXlxjxVMZWXaTURWdN8GJvvVu2vo9DrOKipiIHfrA03PSWktesYwAmIeG4betNHMXnoKbaHfd7wvMXMI2lidETau_N_h41UL7dNbyRFMUxraKr-ve_OGTT3WCfjD0AeywIupwbWxYUuRfo3I_g5-is9QPV7ySXDEmqAPnwTKXO3pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان پلید درباره ایران: این آخرین فرصت آنها برای امضای یک توافق خوب است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/678167" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678166">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7424851c8f.mp4?token=SD_90XmD_5CZddQdYPoOcaKTz6NOruvZPpyNONEXKcxukPezoPrkUm9v4eshBMxdk-A3XnXS9BIy7gSaSRQfM64iQxJRv1NsqkeHNzjqRTMtUE5HBrBs-d6CPt3hn_paJJN-JIkTJNF_4XF61Sb6YFvNJtB1oD0dDfGjFlAE5GyfRhdCaWGFvLE62LQeoN5cSpvMIcPtyVizwlkz-Ya51hnuWf2n0qB9hoH0cbHI3oj5s66uNMdtB3uUWYa-bprjLahuCF2tGVU2kF-9IoCGNQJrY8WpqXRrm-fhd9xY8t0uulKWlr8Nu_ZPLtwwCnp2WmByoGF0rxV2tLL4dkjiGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7424851c8f.mp4?token=SD_90XmD_5CZddQdYPoOcaKTz6NOruvZPpyNONEXKcxukPezoPrkUm9v4eshBMxdk-A3XnXS9BIy7gSaSRQfM64iQxJRv1NsqkeHNzjqRTMtUE5HBrBs-d6CPt3hn_paJJN-JIkTJNF_4XF61Sb6YFvNJtB1oD0dDfGjFlAE5GyfRhdCaWGFvLE62LQeoN5cSpvMIcPtyVizwlkz-Ya51hnuWf2n0qB9hoH0cbHI3oj5s66uNMdtB3uUWYa-bprjLahuCF2tGVU2kF-9IoCGNQJrY8WpqXRrm-fhd9xY8t0uulKWlr8Nu_ZPLtwwCnp2WmByoGF0rxV2tLL4dkjiGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: ما اکنون به درخواست ایران و با حمایت عربستان سعودی، امارات، قطر و دیگران صحبت می کنیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/678166" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678165">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e13546124.mp4?token=o_Jh6afnLUgeS8LUwso2pioiBmEaWtirjBgmkylWDxeUalx1N6JgBvVbPKXNOA8jV3uZytsndh1rq78NIJ2Z9rApwEE3nA-6H28m3z0gs_qKQ_73XLLuioXk8DN7Prnbqv3bj214tePqGv6GUaHM7w3AzJcun77NudeFyfMCoK3KQjthiwT_XWE9_JCCizUxv3zRR8OODxpKHwgoUCGfu_6lgmgjvhRMk4Hb36kTngnfYRlT-W43cHkbaUjrz4wxdTfvGZidmZn9ETWZu_TfbLOtqj1XNO5oe2zjGeY3FcvDaPm66E_ND4dgZ2_Fu1O2Eotg1vO0JWSxeXOZDPDqXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e13546124.mp4?token=o_Jh6afnLUgeS8LUwso2pioiBmEaWtirjBgmkylWDxeUalx1N6JgBvVbPKXNOA8jV3uZytsndh1rq78NIJ2Z9rApwEE3nA-6H28m3z0gs_qKQ_73XLLuioXk8DN7Prnbqv3bj214tePqGv6GUaHM7w3AzJcun77NudeFyfMCoK3KQjthiwT_XWE9_JCCizUxv3zRR8OODxpKHwgoUCGfu_6lgmgjvhRMk4Hb36kTngnfYRlT-W43cHkbaUjrz4wxdTfvGZidmZn9ETWZu_TfbLOtqj1XNO5oe2zjGeY3FcvDaPm66E_ND4dgZ2_Fu1O2Eotg1vO0JWSxeXOZDPDqXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک کثیف: دیروز قرار بود ضربه محکمی به آنها بزنیم. خیلی قوی قدرتمندتر از هر حمله ای از زمان جنگ جهانی دوم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/678165" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678164">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735f9b35d6.mp4?token=C202C4xQvSHZEXEexic_ltDRKHqMcXut0kF9-iiVOLDivWPWDAxiz0wlyTSvxXHvgcUAEP0mBmbSJYR7kCLS6XdDOtbu5OH9YXvXx9In0YG5vcmY4YZCcEcMf5d4Tw5Ul60xT12UAundDy9RUIi3IuJApC7be66-PXeKh93fiFaYGsOtVbIgq5P_E8MfsOH6MLjjMsysVlJtibkwaB7o2kT2xOJuErZVpeKsXJtiL9y4sKl5cv1p0XcLvQwUZwiNSP1FC3jLYxVPUlySMbQNeput4IzdNjuzb19DbuUgMZw2CNqbVdhtfnX9PDYVaK5Xw5PeG3tp-1vG344r-QCnzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735f9b35d6.mp4?token=C202C4xQvSHZEXEexic_ltDRKHqMcXut0kF9-iiVOLDivWPWDAxiz0wlyTSvxXHvgcUAEP0mBmbSJYR7kCLS6XdDOtbu5OH9YXvXx9In0YG5vcmY4YZCcEcMf5d4Tw5Ul60xT12UAundDy9RUIi3IuJApC7be66-PXeKh93fiFaYGsOtVbIgq5P_E8MfsOH6MLjjMsysVlJtibkwaB7o2kT2xOJuErZVpeKsXJtiL9y4sKl5cv1p0XcLvQwUZwiNSP1FC3jLYxVPUlySMbQNeput4IzdNjuzb19DbuUgMZw2CNqbVdhtfnX9PDYVaK5Xw5PeG3tp-1vG344r-QCnzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: ما با ونزوئلا اختلاف نظر داشتیم و خیلی خوب تمام شد
🔹
ما با ایران اختلاف نظر داریم و این اختلافات خیلی خیلی خوب پیش می رود.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/678164" target="_blank">📅 21:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678163">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e26ecf0d2.mp4?token=MQeMT95AmKrH8LQBUtQKMN6rgpEPlzOGMK-AA6QeC6mmt_CGkPvyX-zR-uM4iStSuvJH-pP6c8ml9pPe2iT1c3EWKDE1gzsUsoThkWNWue1gFpxmneUK5vyCGslGDls_Zu13FcHIX0nXymYZN0z5ktAyNlbz5TmWIEjJq4BYQJ9DyrR0rOn6Z5CtiPzDmPzxwpYCUcMVEhTqix52iijbcxVvnak_6Pdo5YO0YZy4R-AQGgtU2lFlPiB-yl29yrJXIWPIqfqTDvNZkoiML3E8OON-zCnqrm_hbIVmLqSleU1Waj8sL30CAyLn1ca0UMVOEg06uYnsnB53a-S1Qy64Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e26ecf0d2.mp4?token=MQeMT95AmKrH8LQBUtQKMN6rgpEPlzOGMK-AA6QeC6mmt_CGkPvyX-zR-uM4iStSuvJH-pP6c8ml9pPe2iT1c3EWKDE1gzsUsoThkWNWue1gFpxmneUK5vyCGslGDls_Zu13FcHIX0nXymYZN0z5ktAyNlbz5TmWIEjJq4BYQJ9DyrR0rOn6Z5CtiPzDmPzxwpYCUcMVEhTqix52iijbcxVvnak_6Pdo5YO0YZy4R-AQGgtU2lFlPiB-yl29yrJXIWPIqfqTDvNZkoiML3E8OON-zCnqrm_hbIVmLqSleU1Waj8sL30CAyLn1ca0UMVOEg06uYnsnB53a-S1Qy64Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک کثیف خطاب به وزیر جنگ آمریکا: شما کار بزرگی انجام می‌دهید
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/678163" target="_blank">📅 21:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678162">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46daf284a1.mp4?token=K_hQSM3IYpBZkYOSaYDubHNFXjb_OFHyYdEJbbK0yKdhWAe-1lLT6w1j10K3YqqP9VEi7N4yMqzjNV33JwBVD3mt0FHO4M6bcwGpgRoQ7DR-IVLVwsIWnA4zfuZIqt-Rba3KeOOp7YA4-Tooas-YWGZR132cmKxo3XnBKu9M-W9pJyBy-z0ByKeQnfp_BMm11UfgkzIRMxhTi7GPJ9Xecd0qIej8yg9FoBsjb-gIOeO2uIwONaAi4b7kwcuSLG8bFqYgi5CP59-ExNlCODkGIju0z9YsaGcJ0lqKD3khx5a-Dd2UTSa_UIgT-pqfj9luy4S5ZpNVUC64T8Np6JfvAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46daf284a1.mp4?token=K_hQSM3IYpBZkYOSaYDubHNFXjb_OFHyYdEJbbK0yKdhWAe-1lLT6w1j10K3YqqP9VEi7N4yMqzjNV33JwBVD3mt0FHO4M6bcwGpgRoQ7DR-IVLVwsIWnA4zfuZIqt-Rba3KeOOp7YA4-Tooas-YWGZR132cmKxo3XnBKu9M-W9pJyBy-z0ByKeQnfp_BMm11UfgkzIRMxhTi7GPJ9Xecd0qIej8yg9FoBsjb-gIOeO2uIwONaAi4b7kwcuSLG8bFqYgi5CP59-ExNlCODkGIju0z9YsaGcJ0lqKD3khx5a-Dd2UTSa_UIgT-pqfj9luy4S5ZpNVUC64T8Np6JfvAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: مذاکرات با ایران در حال حاضر در جریان است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/678162" target="_blank">📅 21:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678161">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/678161" target="_blank">📅 21:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678160">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2240c9d4af.mp4?token=lld6OTuqxD6L_A5rRb8gCQOWQMEgouLz4GHrw76fnkkNjyBTS0TDrdbMRXZziKv3TUbHZaaZc_Jn7pQ9Pu6Z5Q47jxotGIXrunFNjBC-OZVJ6lUpR80SlPJP2xBZfn6MPaeYGpyNkg7XyO7MDFBqW11ye4HtWaeQOviZaQwBN5iJQ5LwEpK4JHk-I_u5n6fJMkvlmqd4eGvqYA8z0G2aKcWMNg41iubMxpY2blg92WZCnByB-mYWz3qVw3eB1vYeRUEzMQIXLLSqYGJJLC13pdVaJkTN7iVdNpNJ1p08BtDcx2ZDI6-i_JA3ZsxKQXJ11bfst_lozhV1CiZZC06dgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2240c9d4af.mp4?token=lld6OTuqxD6L_A5rRb8gCQOWQMEgouLz4GHrw76fnkkNjyBTS0TDrdbMRXZziKv3TUbHZaaZc_Jn7pQ9Pu6Z5Q47jxotGIXrunFNjBC-OZVJ6lUpR80SlPJP2xBZfn6MPaeYGpyNkg7XyO7MDFBqW11ye4HtWaeQOviZaQwBN5iJQ5LwEpK4JHk-I_u5n6fJMkvlmqd4eGvqYA8z0G2aKcWMNg41iubMxpY2blg92WZCnByB-mYWz3qVw3eB1vYeRUEzMQIXLLSqYGJJLC13pdVaJkTN7iVdNpNJ1p08BtDcx2ZDI6-i_JA3ZsxKQXJ11bfst_lozhV1CiZZC06dgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز
کارواشی که روزانه به ۱۲۰ خودرو سرویس می‌ده؛ فقط با یک کارمند
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/678160" target="_blank">📅 21:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678159">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/678159" target="_blank">📅 21:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678156">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryTrV467Jq30TH6x0lLD5TXm6UyZ8mH1-QMrmuNOgMMH_S64ynhpxqS65RwpaCNCAgtkHx8p3R5lUULwII6NzFTTYvCvpJveIyUHjDcFUlazt8g-AE6b29DCnKo_uz6pnVkgIZbKWaHibkCh0S813d09MKhCyhLfFPxJrnP4Ri_7ZIkchaCu2GoM0AfzclNsFp3DisoDa1zbwEbfNXdMcIpXShmezutWUpo2scYcbj3TlqafPhN8VmT7fb0BsYtPVt30IaXg_rRuwaUFK8x63gize4Ex3f5NSiVAbsuVAQBrva9j5M_ypWY9muk4vIudyBRGLWdTveDaCQcl26vVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خورشید
🔹
کارگردان: مجید مجیدی
🔹
ژانر: درام، اجتماعی
🔹
بازیگران: علی نصیریان، جواد عزتی، طناز طباطبایی، روح‌الله زمانی، شمیلا شیرزاد و…
🔹
خلاصه داستان: علی، پسری ۱۲ ساله، همراه دوستانش برای تأمین مخارج خانواده کار می‌کند. روزی مردی از او می‌خواهد گنجی پنهان‌شده…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/678156" target="_blank">📅 21:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678154">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b4a4714e5.mp4?token=Km4cEehB1awTOEwAjdJfPtxAGpzJ0G0g-7nwFQA9zNBQGDz5fBoCusvUH7kN8LJ93eWVZYPZkud8lOzan3JaaiAmSwQYmjnbABC4yFkO8lX_poY-RpoPPjiVEhIocRrP_KdVyqay33a1EO6iloby0wTL2fQyqDW8JHoF7h6x6E31HxsbA--r4lXrBnkGB-P6uAZl1naT1NXCaMTYzWyLbjfxltiK9-yTcwFxmimrfTW5Qmva0Xa6i1sjNW5pwCTkFutKc31_U9hEstrZc0EzekAs6cCdrWpP1qkLNg9fJPsvbss_gA19QtbjdX8X7Ri4a6MMwogOo9Ani8eLf6hIgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b4a4714e5.mp4?token=Km4cEehB1awTOEwAjdJfPtxAGpzJ0G0g-7nwFQA9zNBQGDz5fBoCusvUH7kN8LJ93eWVZYPZkud8lOzan3JaaiAmSwQYmjnbABC4yFkO8lX_poY-RpoPPjiVEhIocRrP_KdVyqay33a1EO6iloby0wTL2fQyqDW8JHoF7h6x6E31HxsbA--r4lXrBnkGB-P6uAZl1naT1NXCaMTYzWyLbjfxltiK9-yTcwFxmimrfTW5Qmva0Xa6i1sjNW5pwCTkFutKc31_U9hEstrZc0EzekAs6cCdrWpP1qkLNg9fJPsvbss_gA19QtbjdX8X7Ri4a6MMwogOo9Ani8eLf6hIgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این کلیپ از حضور قهرمان مسابقات مردان آهنین در اربعین و خدمت به زائرین، میلیون‌ها بار در رسانه‌های عربی دیده شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/678154" target="_blank">📅 20:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678153">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRJ068uBOUsiYyIYB08-nWEfW27yYLqU0g1cUTNDVrR4QffeyaxVKFPjSOyMhI7nhXKZW0A0a6VlQrKJbGhp1TLZbnIT0l10zw4jeHO70tRvVylYfESSSux8sMRui-Z5zwjOaqBjvwKzf3SN3BYYEAjh9BNDHI_0EmurK4lN2vwG1QClzTzOnZfLq2Er6UHlcioWn4ghsSIJJftPg_cBMBAGB3ILh8emDHBiIyRpySFAvdVAglvdgSVNWIgP2N0QnTmnQ5FFUipsOxBJ31PvQvRH_9yPf47haq7mz7Anwbrv6hFpg2XF-_iXUuTuMT63yTno3XV5nOS6-ex3s9i3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جالبه بدانید چه گیاهانی حشرات رو فراری میدن
!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/678153" target="_blank">📅 20:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678151">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxhzzU3N_MrXs1SWwYoC30RMMRyAYuuu3bd0SczfKjmhexaqMKSlP6R81phDfQATygnDr53CIGd6RwC6K_2hECNO6Cm4AVWGo_XWXQdM0NbfCgN064S5IGECA9EaFeU2J-LCdgmDE0EewFoehtQZNJxLB5a8ioxmZ2w1dNgJhauaLek-UrOb2SvCRobLmwslxRwB8l8w7x7A5MULMemIlLk5uq3dV8mJQ1etORxuwkPCc8x50WLjiMYjbU_mbYKYqHk3eP4qy1-wZoqEtWfjESCA30tWs6pHq5LLXJk4DppSRye78cmxlMrTPtf3sQ2O89zX-qXmFdwikwLqeNQiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHLpk0qsd-1wuPxLUelyBEs60rlo6mLbp7pEBFkYGbD6l-0tI_p3Z8VNSKxF0fkPX9AvT7Y_nLK6KfIMDRslEcEJaW-gBWdkqA_DWKkY1J9x9NDhri7cN5Y2d0CdKQd2pM9PJI2ANSYpOOvSGcSar534uW5tuj-elfkM91TdCycMRKjiPUEHCffAuh6MwT7Bfc1twCbN3KeBGycuNzPBwad5mP84YPBwiFCcb-C0osv3uC2BAEdq6yPXrkFE5OScVLLdxLIc6AvUckhIDjiE4eetcWXxa3_UQp9VxQBWtWUGK8NflPMcpnRymFWDFKQ2Q2aBsiqgbyvUnO13-NorEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پست جدید خوک زرد درباره ونزوئلا: حق با ترامپ بود
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/678151" target="_blank">📅 20:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678148">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKD-cbSk20FLNSXWsF9Gjc2Mj-Via3sFy9deeNkHWRkewvktWjers8jNOWHvN1s46G5R_Oki_Nu6eJ_Gf8tETrk45N_Q268ib6NqtkL6DSJRAokbNmQDXnLyAdH4h2GDVVUA8RfkiPm8zclzWJ9VPHZ7emOIxRYLHqI7zzLrx3Zto7qMzQHGqHCmp1QFewJgdmNVA_-tHmpEKVMpviq_OIR_KvVjvbo9UXG-H1c2QNp3BKIoGsl6vmjfziOdSg7Axzo9hZRZs-N0d6Z9mXAHwMZPvce7TRHJYdLXKelVolN-7t-JgyPDIFZkKOpObs_MUMmQKl8x9_PcWjVB5kLk6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
اعمال روز اربعین
▪️
فردا سه شنبه ۱۳ مرداد مصادف با ۲۰ صفر روز اربعین است.
#طریق_الحسین
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/678148" target="_blank">📅 20:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678147">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
از مسمومیت تا برزخ؛ روایت مردی که بازگشت تا حقیقت را بگوید
🔹
00:08:30 هیبتی مقتدر، با خشمی لبریز از مهر، مرا به اوج آسمان برد
🔹
00:28:15 مادر با قسم به اهل‌بیت، جان خودش را پیش‌مرگ من می‌کرد
🔹
00:36:05 چگونگی پاک شدن تن از پلیدی‌ها در آسمان
🔹
00:41:30 طواف معابد تمامی ادیان گرد کعبه و تأکید فرشته مرگ بر اهمیت آدمیت
🔹
00:51:30 ماجرای شنیدنی از مددرسانی امام رضا(ع) هنگام صدا زدنشان
🔹
01:00:30 آزمون الهی برای خانواده‌ای با مرگ فرزندانشان
🔹
01:15:30 علت تبدیل انسان‌های مسلمان و شیعه به حیوان در برزخ
🔹
قسمت بیستم (یک آزمون، سه برنده)، فصل پنجم
🔹
#تجربه‌گر
: علی لعل یوسف
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/678147" target="_blank">📅 20:32 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
