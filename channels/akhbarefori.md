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
<img src="https://cdn4.telesco.pe/file/jUs1LVE8IrJ08hliFzORbwkUEW7yzJMtJ5DnHfnOhMJowumlQS_p9Uc4QxDNoCSXAuOkrjXFNP--C0H6keMTcpJExkCFOmxop1iNx8NR4zrfz39Wf8SQITGZk5QOyXmZ3agjfW-z5WkKly8stk9vAeodqgIyDXgjuuJC_Gyb3aZgQhPUHUMjZJPcBiFEIsRfHDtvFvU99cu-Z0aJ0X_hniGXxJxChUvWNQZ9hCVMb0GRqie8iBFUQHPfQb9K3EMSGyynsFFO5W3HWBOIU69AckEKi9GStCyYsqbFskAyLbynPV8WGQo7hD-_yRQLx-xsYcj1SQydfrt9QscliLtuQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.17M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 18:37:23</div>
<hr>

<div class="tg-post" id="msg-689847">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
مدیرکل دفتر واردات گمرک: به مالکان خودروهای مناطق آزاد اجازه داده می‌شود با ۲۰ درصد تخفیف، خودروهای خود را به پلاک ملی تبدیل کنند
🔹
این فرصت فقط تا پایان سال ۱۴۰۵ اعتبار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/akhbarefori/689847" target="_blank">📅 18:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689846">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiIckyAhHrVLGB-0l7EI4vJdbVSzizNO7V8dwW7CYfvNwcJMIxeHIhi9bBZThQ3uvclZs6sKFxzznPPhQscanhsly8QIqBdooXqdIahieLlmoy4gMWNiX3sMn_80rXgrOZIw2Av_LiQEcvX0irE2x3EwGEmRBFO9rMAvWX48OL3Ccn9mCr-Bsf5KTDibgzIQUnr-sEiei4rQmKSV-qfhI5Az6jeXW9Fs8Q1ae8XE9EMo0xhpYOBlyFceDF3vtUXi4Mn1qPmDvcLzJ4aW2r6-XsZAkxIdDNVGWtL9X3Pp0obzf_ajoTfhzyOMwY289FHTUJPrgGikRmfZwJV0Jvp4SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر قانونی استثنائاتی داره، درست مثل قوانین تلفظ کلمات در زبان انگلیسی #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/689846" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689845">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2kuc21LAV-ThFnFLqrwpc30dUtkuoIQGMkcEqK5URq4vU2cWL-bQA_P6KwT8tebZ9w5aUhlzUchPOLzmdbxcpg_Cmm9gChEHsH0kU-48r-BXt5vAoYHAsQgAJhrgTUvC3lEPFIjWxL_6PIOVx0ut8q3FlcQnS-tSrom4_E82IEuqlHqEpoBKGob64o_YyJiChwTOHdIdbtmK8Be3O7ZXw1F62eAqP3NxE1ohq4mYgDatn7GL6NHW5Q36BLgSDMW0JobibD2ImiR-d8a9BwHS8Z0kfoAvm1Mdlqube-z1oQtZgQpLtQaiwCQJAXOF-1qKg-BAnLecvdfoZb8P_Aq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط میزان ذخایر استراتژیک نفت ایالات متحده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/689845" target="_blank">📅 18:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689844">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44cef5b2b5.mp4?token=qE4crzcw5H4bXzrI9Gf8CGfWw_0wuBrguylqTYdCMGIzNPUdvfOLR6t4sb22Ha2XlB_-rqcEZu9DdMjboO8902QHfUURnGPYw6aiRYM5VxJn-V9MpPBmgf3wG5Yui-e1RlDFUQuJ50WIkbW8Atv65qvFuwFaLQni_jvKdDISAbQMnFNXO5RiA-ifSP4a-vNprh2LwaBt_tGyuk4pSsbd9OBy4mOwWGpIybzxj9RxXSZaUCyzw-EzdPUYK-7VHpLr9xIVM07LgY5gEeu87uFkcUdBpXhOJrd8RvVF3Jm0icXkHw_9WsFT-s5AOquEBXH0Ok0yL-AgI5PWQkyan5WtGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44cef5b2b5.mp4?token=qE4crzcw5H4bXzrI9Gf8CGfWw_0wuBrguylqTYdCMGIzNPUdvfOLR6t4sb22Ha2XlB_-rqcEZu9DdMjboO8902QHfUURnGPYw6aiRYM5VxJn-V9MpPBmgf3wG5Yui-e1RlDFUQuJ50WIkbW8Atv65qvFuwFaLQni_jvKdDISAbQMnFNXO5RiA-ifSP4a-vNprh2LwaBt_tGyuk4pSsbd9OBy4mOwWGpIybzxj9RxXSZaUCyzw-EzdPUYK-7VHpLr9xIVM07LgY5gEeu87uFkcUdBpXhOJrd8RvVF3Jm0icXkHw_9WsFT-s5AOquEBXH0Ok0yL-AgI5PWQkyan5WtGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش رسانه‌ای وزیر انرژی آمریکا برای آرامش‌بخشی به بازارهای جهانی: خط لوله نفت شرق به غرب عربستان سعودی «خیلی زود» دوباره عملیاتی خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/689844" target="_blank">📅 18:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689842">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kz6pbTOxGIEuiZl1V0L9GH6pk05kNSXmEFA2Gf0Xt-HQNm2A6AvOGXwEUDWAmdtbG4b6H18zhLQTMPF9qPBC3R3s0b_T0z-mKUSwpKLLKWp8fTlSZmGoixH4wc6ds-8ha6ya_YjZQ0YgR56dVb0bUDdcxKnCuGv5YD0yLdTBFZXqwTcbzh7KpEWNNftYdRz_D-dSVDkYXD3eqQF5JplEoTG7xviwm4bKIJLfXvaH_uZAoquXB2CsGWn6AzyIEJovvMCWhciFO-MbQH0jUnxBUbqtmIUvRUoRRCmXjpQ5Eo0spT4wAynNPl_f9v_Te9k7IwF_MAQ1kl6ZaD4VTGe67Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_qFNF54j2J23ffy4dAg9ahm8wnFS-a7Xd2Wa59ytQK1g5VmklW-_yxyAVSbC_Ls_N5NrPA705v_NIa-36DwOCnIesT2ogwqwWEfM_2sQ0DoUMgBN61tbeTtKc67v96kdMoxgXtylzQ8xAFQOdwLgCTuuxDiSK5zEuBEM87IFCbbGltxF0MOltFrjR6zFkNc-NEWeKSdI85C0JgpA_ZYVedWpE0uxeFapeVMwGzSPc4LZUA7mJ2s99Da-xd30KsxDQae6QQV5qXMqFHesxbeHum5iNX9AwucbbeCAKe2f_-vMB6-pc7A3fZe_KLhEOWmvewISH1zZ9_TanK9vZsfdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حذف شیر و خورشید؛ وزیر خارجه عمان اشتباهش را اصلاح کرد
🔹
بدر البوسعیدی پیام اصلاح‌شده‌ای درباره لغو نشست اعراب با ایران منتشر کرد، او پیش‌تر از پرچم شیر و خورشید استفاده کرده بود که واکنش منفی برانگیخت.
🔹
در پیام جدید، تمامی پرچم‌ها حذف شده است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/689842" target="_blank">📅 18:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689841">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trcsz1dCVqSprCkANHBOXVBOd9UJYYLNMSl6_8ArZ1SblmsZuTU-2xJPjwqjUDiK0IBBdIEOujVLC8YepkNQj2uPB_UlTKUAPJ8EylHL52A6m0k7ndaPA9iX1ppQQHJRqvUxJBRgKSte7sfzZLPKN8Kfs9CYYcJTJCc_BQpEkOMAkuUZT-Ct1YgsCLViJ5fX-AAZLAn6paQUvJgXKIOXMdwHXmDMQDN-GXpj83b0bbggRfWHn5Mb5x5Tr4BCk-ijjoam_ZcE2rqfzHw31XVqKkwt5ErV4Q1nr9BiOO73KVnsut84QzuYqy7d6imQbyyRlOJRTn2ld1GfigxDbnxi1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترور عالم اهل سنت در زاهدان
🔹
مولوی یوسف گرگیج، از علمای انقلابی اهل سنت و بلوچ زاهدان، توسط مزدوران صهیونیست مقابل درب منزلش، به شهادت رسید.
🔹
اخبار تکمیلی متعاقبا منتشر خواهد شد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/689841" target="_blank">📅 18:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689840">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🤌
کلی ویلا با قیمت کل توو کانالم هست عضو شو ببین
👇
👇
📱
[کانال تلگرام من]
(
https://t.me/fafamelk_68
)
❌
مالک به خاطر نیاز به نقدینگی و انجام یک معامله فوری فقط تا پایان هفته حاضر شده 8 تومن زیرقیمت واگذارش کنه
❌
همین امروز برای بازدید تا پایان هفته آینده زنگ بزن تا ساعت بازدیدت رو هماهنگ کنیم.
⏳
📌
#جاده
جنگلی ایزدشهر(بین چمستان و ایزدشهر)
🔹
زمین: 350متر
🔹
بنا:450متربنا،جکوزی و سونا واستخردار با روف گاردن،4 خواب،دارای سند تکبرگ
💰
قیمت: 10میلیارد کلیدتحویل  (قابل معاوضه با طلا،دلار)پرداخت اقساطی بی بهره
📶
خانم رضوی
09194565022</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/689840" target="_blank">📅 17:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689839">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-ceqh7fsQClxKaFGs0yG5b6qka3JETGA7-QhjLm_inzLXUHkkbAKQy319jP6p5mqndaPCPeVJEoLHp8tcgCZoHwv8PsygQggxmwSS6H0RFDuJcq4CUb9envKAQ8Z61cXDfymAKXDqmtUu3NtYDjgGR0zDQQKA60njZG61LX_PGYyap9QvNXLG_m5R6kVkwoxKc1hSyVhv5vOCgnKSZt12tDPGhvP9YwmAWw9Wr4eWd7W8J59JKmQlfp585hDHHIex0PXYrwY2Ox2B0zHWWaYJXmLKXXPbqWGb9SlczekrIJ7fkCunOx3CAAszXDu5yVjAD0QABLoaYAUsRvC_obFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انواع سیستم های فروشگاهی تا آخر شهریور ماه شامل تخفیف ویژه و شرایط پرداخت شد !!!
فروش فوق العاده انواع تجهیزات فروشگاهی مخصوص هایپر مارکت،مجموعه فروشگاه و رستوران ها با نرم افزار باران
🌧
همین حالا با کارشناسان ما تماس بگیرید.
09024293322
09158207400
05136142212
آدرس سایت جهت سفارش
hivasys.com</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/689839" target="_blank">📅 17:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689838">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e2a43377.mp4?token=tZK6h8FAASiksII-7lZ2JoPdm22TmhZX1-x0QjmxRmZKyu7B2XK_TUtfmlgoeCCyzHwpHjcx6UGi1w-_J_z7VdRD2CTZuIsAqb6vdW8xNQ_-7zx9ObbLMPLSD9U3Yv85M6Zf452QgwHbTp1LfUb3ViUhxRkPEPd8GfPZ8lPTkX6FXYq79zK2WWIcfUf1-e5xwaShT2Gryb09Ylt3kd1Pk9XTuQIGeHIJfaufwlTPbPWA_83H6Q3h7c-qJgkMcUAN1pEKhVe9mof5yAsHQzac3AEXRv3x6gDMcwGgK_GWzHg_f9QUc8D9nj9dplrISWoXrCe6flOlPZxbHq2w_08QFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e2a43377.mp4?token=tZK6h8FAASiksII-7lZ2JoPdm22TmhZX1-x0QjmxRmZKyu7B2XK_TUtfmlgoeCCyzHwpHjcx6UGi1w-_J_z7VdRD2CTZuIsAqb6vdW8xNQ_-7zx9ObbLMPLSD9U3Yv85M6Zf452QgwHbTp1LfUb3ViUhxRkPEPd8GfPZ8lPTkX6FXYq79zK2WWIcfUf1-e5xwaShT2Gryb09Ylt3kd1Pk9XTuQIGeHIJfaufwlTPbPWA_83H6Q3h7c-qJgkMcUAN1pEKhVe9mof5yAsHQzac3AEXRv3x6gDMcwGgK_GWzHg_f9QUc8D9nj9dplrISWoXrCe6flOlPZxbHq2w_08QFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‏
ماجرای شناخت رهبر انقلاب از فیلم‌های کریستوفر نولان
روایت فرید حداد برادر همسر شهید رهبرانقلاب:
🔹
آیت‌الله سیدمجتبی خامنه‌ای با همسرشان برخی سریال‌ها را می‌دیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/689838" target="_blank">📅 17:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689837">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-ClYyJsiQZ5JZZFOtK0fr25mNhwPyNkYaOBckWWJnn8Rlf7dbYWVpdUDPZLJJHckHMLi2rkGW_BW-22v422KwUFI_12w_uj-dEzB-yQn9nTiSW7RS2WoIHnDfFP9oGITEMuatcJQdSHnaciZ9ATp4reLh9PH47RH8DJc1KVD_7Ay2fzHqUoHjsmdINEBp9_iaGEs3W09RpS6Kq88WBnaLJaAQxKNiCu9SenXYMrFx7OqrlpxKm3aaxCqp1eAZDmCUwVUcajTl4YOzR9SF6uO824Febc1IyCLHKUm2928C2kigaLaD0sbpDL9WZ11be4LE2QGJlVxzXS3Iv0z7BgHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین تولیدکنندگان سوخت در جهان کدام کشورها هستند؟
🔸
چین با تولید حدود ۴.۸ میلیارد تن سوخت، در صدر بزرگ‌ترین تولیدکنندگان سوخت جهان شامل زغال‌سنگ، نفت و گاز طبیعی قرار دارد؛ پس از آن آمریکا با ۲.۳ و روسیه با ۱.۵ میلیارد تن در رتبه‌های بعدی جای گرفته‌اند.
🔸
ایران نیز با مجموع تولید ۴۵۷ میلیون تن سوخت در سال، در جایگاه نهم بزرگ‌ترین تولیدکنندگان سوخت در جهان قرار دارد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/689837" target="_blank">📅 17:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689836">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
المسیره به نقل از منابع نظامی یمن: تجمعات و نیروهای پشتیبانی مزدوران سعودی در صحرای الجوف هدف قرار گرفت و چندین نفر کشته و زخمی و تجهیزات آنان از کار افتاد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/689836" target="_blank">📅 17:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689835">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5809fdeff4.mp4?token=vfc-NaBHXvB7fWJJLSXTHdmmLKh_yiV4Kc4F-BkNAsJYJ9EcqhfDmCa7xSZBQ1yfkiVTbLp9kMO2jE2gr9UR_YMHay8oiUXSmVUFYCjsVLuFzZ8RVNCxVmk1koIlBYKj58GJW2B2oIGmQlv6f9aLMOUjGMhS-2WQR2XnWmITaj-Mu2DETAgh9jeWk8q9YzYq9nj0JFaMsldNmgzB_IfVK_AxCSJlZSHeKgyDU8Q1eSbfF5KSZV11dYptYdPXKXyOWPSUhdv2kSGOgAwvyl6skl_3cMjXThEMPe_wAzuvSOFDa_q5S1fHvkrDYTZKgWi2tNE77K0M3Uey0XmxernbDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5809fdeff4.mp4?token=vfc-NaBHXvB7fWJJLSXTHdmmLKh_yiV4Kc4F-BkNAsJYJ9EcqhfDmCa7xSZBQ1yfkiVTbLp9kMO2jE2gr9UR_YMHay8oiUXSmVUFYCjsVLuFzZ8RVNCxVmk1koIlBYKj58GJW2B2oIGmQlv6f9aLMOUjGMhS-2WQR2XnWmITaj-Mu2DETAgh9jeWk8q9YzYq9nj0JFaMsldNmgzB_IfVK_AxCSJlZSHeKgyDU8Q1eSbfF5KSZV11dYptYdPXKXyOWPSUhdv2kSGOgAwvyl6skl_3cMjXThEMPe_wAzuvSOFDa_q5S1fHvkrDYTZKgWi2tNE77K0M3Uey0XmxernbDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر یکی‌از شهدای دوران دفاع مقدس در طلاییه کشف شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/689835" target="_blank">📅 17:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689834">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d2895480.mp4?token=cPpQffGpqSxYE8d2PMwfICXlfnD_1thvBroMDcG2ltdROfEJylNVeYFEm6Fx8igtDxnR7jhq9dmaIiqee5KqbvOX0tUh8Y47hLr9S6OTfl5htBnD_9GMYdkViPJSNo5TSBheeua6UE4kTurlLmJoQ3UeOwdHEGzK3wIqyZlYdEL6mpjJnfrkJKVXs8luEyFxjov575VVEbK5fqh5doT3uSfhO2z0G291kgv0YDFAS8GA7ie5V6fb_6cc5DZubNRu6iClu4_6FusqhGCGl8wn8I4yjGCoOUyzEH2TLYmENArYXUYOjRF62p5y3CTU2cTsdZwlYm-90E0gEVBtFLGeZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d2895480.mp4?token=cPpQffGpqSxYE8d2PMwfICXlfnD_1thvBroMDcG2ltdROfEJylNVeYFEm6Fx8igtDxnR7jhq9dmaIiqee5KqbvOX0tUh8Y47hLr9S6OTfl5htBnD_9GMYdkViPJSNo5TSBheeua6UE4kTurlLmJoQ3UeOwdHEGzK3wIqyZlYdEL6mpjJnfrkJKVXs8luEyFxjov575VVEbK5fqh5doT3uSfhO2z0G291kgv0YDFAS8GA7ie5V6fb_6cc5DZubNRu6iClu4_6FusqhGCGl8wn8I4yjGCoOUyzEH2TLYmENArYXUYOjRF62p5y3CTU2cTsdZwlYm-90E0gEVBtFLGeZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون سیاسی رئیس جمهور: هنوز نمی‌دانیم آمریکا برای سفر به نیویورک به چند نفر از تیم ریاست جمهوری ویزا خواهد داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/689834" target="_blank">📅 17:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689833">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
تلاش رسانه‌ای وزیر انرژی آمریکا برای آرامش‌بخشی به بازارهای جهانی: خط لوله نفت شرق به غرب عربستان سعودی «خیلی زود» دوباره عملیاتی خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/689833" target="_blank">📅 17:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689832">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cbe87ded4.mp4?token=t_jAF83LzDB13xfwBPfoYfLn1CDZd9G7ixxwB2K3LmL_M7pVQX4HC8pL8GtTwD6GWEydDENopPOUGDyaU2C0Ps5SxtsYtsbOSaWdCzPmhYLUMTCoiTLPY6zshI0jAcIEEvY4HkGW177e2Ko48D1hHCYH3Hgd0W9dBsHrM4FZcAJqIE_J0XeqQZ5FujvgZmo-uTdKV7Phu5TcQ73Jff_gU_83gblXsJITue_K-Mrg6sZAVaCRlrPj07F7T9igGvSRfJJsiR-cXzXj2GWv345zeNExLFdb6csNwwNqlHm7Nvgbv6R_nbPuBws6gm59kpdNcDaEqcyYVyVSLcEXCUAjbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cbe87ded4.mp4?token=t_jAF83LzDB13xfwBPfoYfLn1CDZd9G7ixxwB2K3LmL_M7pVQX4HC8pL8GtTwD6GWEydDENopPOUGDyaU2C0Ps5SxtsYtsbOSaWdCzPmhYLUMTCoiTLPY6zshI0jAcIEEvY4HkGW177e2Ko48D1hHCYH3Hgd0W9dBsHrM4FZcAJqIE_J0XeqQZ5FujvgZmo-uTdKV7Phu5TcQ73Jff_gU_83gblXsJITue_K-Mrg6sZAVaCRlrPj07F7T9igGvSRfJJsiR-cXzXj2GWv345zeNExLFdb6csNwwNqlHm7Nvgbv6R_nbPuBws6gm59kpdNcDaEqcyYVyVSLcEXCUAjbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از خسارات وارده به عربستان در پی حملات ارتش یمن
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/689832" target="_blank">📅 17:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689831">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400d87aa86.mp4?token=PrOs81SxyzrXpQd5t2mBGZtfV4Of2SMw2Aq-xiDk_kezSKmr6rWPF3Rh7KTn-G-_7KD4C6QWEXfPIPVUcbdOx4XgdF_n3fwwArobbg4y3uZPXD-9jOkVdKIIDwcdnLKU3hXuY6AR47i9b2KVoFiRH0U_CM-PGkZrEhjcaT7-lDtaXng1CEB5qAw8Up2JhtTygN1OuUspk6xZslGV8hgKSGI8gdEF2nmSO5lHHekIc_CDYsX9TzMf-lQSRi2sk6R2PiM3UBa0hlv7qQGKVy_a-QUhw5c16CcgbVNTYOt_VOqoq0dOvkBUYiC-PjuQQ30294pVX4_mBve0l4tfjiXLxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400d87aa86.mp4?token=PrOs81SxyzrXpQd5t2mBGZtfV4Of2SMw2Aq-xiDk_kezSKmr6rWPF3Rh7KTn-G-_7KD4C6QWEXfPIPVUcbdOx4XgdF_n3fwwArobbg4y3uZPXD-9jOkVdKIIDwcdnLKU3hXuY6AR47i9b2KVoFiRH0U_CM-PGkZrEhjcaT7-lDtaXng1CEB5qAw8Up2JhtTygN1OuUspk6xZslGV8hgKSGI8gdEF2nmSO5lHHekIc_CDYsX9TzMf-lQSRi2sk6R2PiM3UBa0hlv7qQGKVy_a-QUhw5c16CcgbVNTYOt_VOqoq0dOvkBUYiC-PjuQQ30294pVX4_mBve0l4tfjiXLxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرریز شدن سد خمینی‌شهر بشاگرد پس از بارش‌های تابستانه
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/689831" target="_blank">📅 17:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689830">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای وزیر انرژی آمریکا درباره وضعیت تردد نفتکش‌ها از تنگه هرمز
وزیر انرژی آمریکا:
🔹
نفتکش‌ها شبانه از تنگه هرمز عبور می‌کنند و تحت اسکورت نیروی دریایی آمریکا هستند.
🔹
اهرم فشار را از ایران سلب کرده‌ایم و داده‌هایمان دقیق است./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/689830" target="_blank">📅 17:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689829">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ایران ۷۷ کشتی را تحریم کرد
🔹
طبق گزارش نهاد آبراه خلیج فارس، ایران تاکنون ۷۷ کشتی را به دلیل تخلف در تنگه هرمز در لیست سیاه یا فهرست تحریمی خود قرار داد. هر کشتی که با این فهرست همکاری کند، خودش هم تحریم می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/689829" target="_blank">📅 17:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689828">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a68c3e958.mp4?token=QwjzNpByZTnj1CmlPl5rGC5Z78EgK0gOzsrAMNhfnosYJdcGuSYdjU_tiVcSS7uP9zbNZLywHCf_6dToXEzImb-OcGI3clw_DGpTteD-nyxddGM4O6AT9dpm_eSgt1aZn6uFgoOKR9uth-k3LPJ7G0UsO79qymptpvB_2N1DP3M4xG9j3A0tkZ6NwSeUZ3_0NGxbWgux1yxiPxMUE4bperDqYDmvRBiVRlNmzh04TZda26zDQ2wM0knozC2dEqdrY9t2JS4lTO39SjHeus60QTX77AM9orBjA73AdzCiicrKZKREYUIYWuN0CW-gtn25DxntOdhQfUzJVcntJelaEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a68c3e958.mp4?token=QwjzNpByZTnj1CmlPl5rGC5Z78EgK0gOzsrAMNhfnosYJdcGuSYdjU_tiVcSS7uP9zbNZLywHCf_6dToXEzImb-OcGI3clw_DGpTteD-nyxddGM4O6AT9dpm_eSgt1aZn6uFgoOKR9uth-k3LPJ7G0UsO79qymptpvB_2N1DP3M4xG9j3A0tkZ6NwSeUZ3_0NGxbWgux1yxiPxMUE4bperDqYDmvRBiVRlNmzh04TZda26zDQ2wM0knozC2dEqdrY9t2JS4lTO39SjHeus60QTX77AM9orBjA73AdzCiicrKZKREYUIYWuN0CW-gtn25DxntOdhQfUzJVcntJelaEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی‌هایی با بدنه‌ ضخیم، نمایشگر کوچک و دکمه‌های فیزیکی که بخشی از هویت روزمره‌ صاحبان‌شان را شکل می‌داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/689828" target="_blank">📅 17:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689826">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mvEXEFufCAO2ZMGOdkfRkoro9bMoJgD_z56ZpVrG6ToSq7B9pn3cEWuWmVDR-VvQfFv9bGh2sTItJ9WW3sQwb_5-xAnXZ2_dGr4_hghz33cRI-AXnA9zq1cod7IABmT1eBqAHSqbxZk0ZcXrhrVc5CWSw9qf1XkVa2h4yJ015McEzktNv7WKP7a0sQXeFPaCWHeU6hnqUXRgKGkrzl2JcZu9EMZ2Q6JSwpoYwzhG1S3GZFljB-ztvHsjqIj8E2JEvOzG95Ust-Nz_8XeGbuYCTB1PMNYVLcFZC8DI-YL_EuIVVq6naVV1YBA4Cywi4RQSIXz8csoEgynXCL_VtoYbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cWCiV7IQRs3S1rBqgmGTo4ZnsnjHsMeEr_Ubzou1ctUtWl-bwAcMlJTVeun5oTxvK_SJ4rLJxbnwlb-I7NvQtqTvDbMOCf4XXBqCGTBuL8Hd_zWqMTzzFgemEdBBmmPtUgtWqvBmHSKLrPjc_5_mEvVjy89VBawWLVQU-NV-bSkPkK4kNh85dhISHa6Z0qSk69OPXTwrgjDqbiIKfyJ65YUC73wCCdKsFVGutbgxwnVbyjwodzx96yyp5xKbwIv6C0eNYTm5bWqf15TMsOsC1LYxL_lDAVRqyl-PFJW5VYnOGb14wjc3cI5Qv32jyuid1k9cou51M6f32-nUVxj4Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آذر پربرفی در راه است؟
طبق تصاویر مدل‌های اروپایی:
🔹
نیمه اول پاییز، باران زودتر از نرمال در شمال کشور
🔹
نیمه دوم پاییز، شدت بارش در زاگرس از ارومیه تا زاهدان؛ شواهد آذرماه پربرفی را نوید می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/689826" target="_blank">📅 17:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689825">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7faa8111f7.mp4?token=pVnZd6FxtuYP13TGHKZVqrL2gmrqazWHIC_ZAVsGjtwR3y1em8PEY5byR6dHtZo7SK_xrA2C0pioMfU9h_rviyk7srMNVudISj9xbKa1sSvko_z0z1ZeQYm8Bc7xfwcju1TYl2x4SVSDcnbZnup1IzV8P6De_8M-68X2cCF8m7OwhmNhZKtnoILmOmG6pHS154f9LrA5Go0jBuqeRJA7gqAeoVsx1xDttO8v5HQTLrQPlW88xPbk4R93otnxL0AmtlEmtnzPMKYvS1TVS5YsvCzZkRboMKsXPwDPgAS-VqwrJ_ekDcnj9jtdT16weNtyMzAabv_Ky46o7ET2STKtag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7faa8111f7.mp4?token=pVnZd6FxtuYP13TGHKZVqrL2gmrqazWHIC_ZAVsGjtwR3y1em8PEY5byR6dHtZo7SK_xrA2C0pioMfU9h_rviyk7srMNVudISj9xbKa1sSvko_z0z1ZeQYm8Bc7xfwcju1TYl2x4SVSDcnbZnup1IzV8P6De_8M-68X2cCF8m7OwhmNhZKtnoILmOmG6pHS154f9LrA5Go0jBuqeRJA7gqAeoVsx1xDttO8v5HQTLrQPlW88xPbk4R93otnxL0AmtlEmtnzPMKYvS1TVS5YsvCzZkRboMKsXPwDPgAS-VqwrJ_ekDcnj9jtdT16weNtyMzAabv_Ky46o7ET2STKtag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این اشتباه باعث می‌شود پول بیشتری از دست بدهی!
🔹
خطای هزینه هدر رفته، یکی از جذاب‌ترین مفاهیم اقتصاد رفتاری است. اگر می‌خواهید این خطا را دوباره تکرار نکنید، این گزارش را از دست ندهید.
#چرخ_زندگی
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/689825" target="_blank">📅 16:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689824">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
نتانیاهو عازم نیویورک می‌شود؛ دیدار با ترامپ هنوز قطعی نیست
🔹
نتانیاهو هفته بعد برای مجمع عمومی سازمان ملل به نیویورک می‌رود و پنجشنبه سخنرانی می‌کند، دیپلمات‌های اسرائیلی انتظار اعتراضات گسترده دارند./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/689824" target="_blank">📅 16:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689823">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgtC7H_0tTcyv7PJ-qTLZACtyuFlsQEJhyTwmDDNGPt5eJxD-vzXfRW4lsRrFJ6HvEY4Ts9_jvm3H-8JW5m6421i7RUTx9lN_mLEDvpbWpACvb6fPE2RjMoGrISV5OFOnvH5lTQtIHVL7iRpTIhMZRPMdLtEvCg75QZjQGSKFr9R1ZvHzgPpNpTRBSk1FueUEKmRlr1p5DhsN26JpWqJrmnokuAm28UNrRDFRpsIKOROgrXR4lKXVNYjcKEC0AZWIAF1zOPLxMoaor922IthdGtUF6H7SQbxMqolHOjRR1eI1dws7hpDQKI28vI5dCRk88cILFgyLh3MyjFqVKWXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قات چیست و چرا یمنی‌ها این‌قدر قات می‌زنند؟ | مخدری که در یمن عادی شده است
🔹
در بازارهای یمن، دسته‌های کوچک و سبزرنگی از برگ‌های تازه چیزی فراتر از یک محصول کشاورزی هستند؛ بخشی از زندگی روزمره میلیون‌ها نفرند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3245206</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/689823" target="_blank">📅 16:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689822">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzK1Js_q1L-fvD-pua0JCvshgvZmVSmqCSlh2oAzriuHe1E5z4VSy70D3bjH7n2hi81xkMMEHDf08Bd1-M5MRp7sFbxQFNzryxhzB8KgxqnVRo3eHzMZ2D-Qk9I5cLY2p-2BqIjW3SzqDRetTd3LdWGxvPAqOJJieX_q8lz51CtJC5JZQYivuOE8bMKjhwVjqqDozLGLYW9DA3aBjyUdEerToGXXB3OZIy71I1lcTSnjNLdmjgXZ1QMQuGDtNXdC4XDkVUrdIN8AKffY0eWPL93DiX2YCb8sMjIO93RxE2fZ6O_0MQj0wXSfmP5KIGdfhMa9fWPp5FmQpYpy53s9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش قیمت طلا ادامه دارد/ طلا وارد کانال ۴۲۰۰ دلار شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/689822" target="_blank">📅 16:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689821">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7RocByM6OAixQ4g3ULHeTWiyTySDb-VOGqQep9QrmavwBcjm3OmKVxGQyXA1JbMx3fmTzfA4Pn2HllmFEekuExPcYg7b29hPGJdgMmIEhsKGUzr4mjcbDVr2MkB_n4DD3Ns3ttXlOBy68u3MOGBmgU4QK2X3n9YDoWZglWtjbRUhV8WYLchFICQowIirgVyHFGeYgj43-rmy1-t8dQnM14RMouM7lTEgSTkrNcHfFDdiIGv0WvVESfPHK5dBSsPNRTmHolkLQytb6eIM9ooD7YvNqDGvvJrbPc6cFDp6qs0pqT2njqo2qpXjHZs3rBtzyVMo_tsK5UkMTtibGqrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
طاق نور
یادمانی از روشنایی ایمان؛
ترکیبی از آرامش، معماری معنوی و نور گرم که می‌تواند حال‌وهوای خاصی به خانه یا محل کار شما ببخشد.
✨
📐
ابعاد:
۱۶.۵ × ۷ × ۹.۷ سانتی‌متر
💸
قیمت اصلی:
۲,۳۳۳,۰۰۰ تومان
🔥
قیمت ویژه:
۲,۱۳۳,۰۰۰ تومان
⏳
موجودی محدود | تا پایان موجودی
🛍
سفارش:
@gharar_order
👀
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/689821" target="_blank">📅 16:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689820">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
۵۰ درصد ترافیک مصرفی دنیا در بستر 5G است، اما در ایران این میزان نزدیک به صفر است
پاسخ معاون وزیر و مدیرعامل شرکت ارتباطات زیرساخت به سوال خبرنگار
#خبرفوری
:
🔹
فیلترینگ بر کیفیت سرویس اثر منفی دارد و انکارش غیرکارشناسی است.
🔹
مصرف ترافیک موبایل ایران با میانگین جهانی تفاوت زیادی ندارد، تفاوت اصلی، سهم بالای شبکه موبایل نسبت به استارلینک در ایران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/689820" target="_blank">📅 16:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689819">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/000802efa0.mp4?token=FAt3t46XF8vMHd_S1dd-Da6ToKEVxMSTBS8W-hMzCtgngPzrwzoQ-aQ5kSSWj8PSFuAGPBkIGpc6YiUVX65GgyOhz89y5PDV2UhOWRHo-076ULgAlH4wSRD-aNtIwSQrWQdkuiHZ3jVDxMFHcezHAfQKSXemIsAzW3LzTDUs3PFnILuwuM4Oa7NcxXPSW9GhwlC9EuxP13DBzQLnTEDE5I8pDtqg_7JYADQqGRkuIa5-2L8SwLw9ki19vLAx3UjVlJEg-SqMneXoHz9fr-H65RNX6Yrsims6dnF7c4NlQv5_WDjuGac1kFS5KVttQs57qlOI0YrKLZr3xxFTNmUKyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/000802efa0.mp4?token=FAt3t46XF8vMHd_S1dd-Da6ToKEVxMSTBS8W-hMzCtgngPzrwzoQ-aQ5kSSWj8PSFuAGPBkIGpc6YiUVX65GgyOhz89y5PDV2UhOWRHo-076ULgAlH4wSRD-aNtIwSQrWQdkuiHZ3jVDxMFHcezHAfQKSXemIsAzW3LzTDUs3PFnILuwuM4Oa7NcxXPSW9GhwlC9EuxP13DBzQLnTEDE5I8pDtqg_7JYADQqGRkuIa5-2L8SwLw9ki19vLAx3UjVlJEg-SqMneXoHz9fr-H65RNX6Yrsims6dnF7c4NlQv5_WDjuGac1kFS5KVttQs57qlOI0YrKLZr3xxFTNmUKyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رودخانه گنگ یکی از آلوده‌ترین رودخانه‌های جهان است که همه فاضلاب‌ها به آن ختم می‌شود و اجساد سوخته هم در آن ریخته می‌شود اما مردم هند آن را مقدس می‌دانند و از آب آن می‌خورند
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/689819" target="_blank">📅 16:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689818">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
خاندوزی رئیس گروه اقتصادی دفتر رهبر انقلاب شد
🔹
احسان خاندوزی، وزیر امور اقتصادی و دارایی در دولت سیزدهم، جایگزین علی آقامحمدی به‌عنوان رئیس گروه اقتصادی دفتر رهبر انقلاب شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/689818" target="_blank">📅 16:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689817">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
عده ای همین الان می‌گویند در شرایط فعلی نباید اینترنت باز باشد/ در زمینه حکمرانی فضای مجازی باید نگاهمان را تغییر دهیم
پاسخ معاون وزیر و مدیرعامل شرکت ارتباطات زیرساخت به سوال خبرنگار
#خبرفوری
:
🔹
اقدامات وزارت برای رفع فیلترینگ همیشه در دستور کار بوده است، اما نهادهای تصمیم گیرنده در این حوزه متعدد هستند.
🔹
این حجم از اعمال سیاست‌ها کارآمد نبوده و به ضد خودش تبدیل شده است.
🔹
همانطور که می‌بینید همه در این پلتفرم‌ها حضور داریم. در نتیجه پیامد فیلترینگ اضافه شدن هزینه، نارضایتی بیشتر و‌‌‌‌....بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/689817" target="_blank">📅 16:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689816">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
پاداش جام جهانی برای هیئت‌رئیسه فدراسیون فوتبال گران تمام شد
🔹
سازمان بازرسی بابت پاداش ۲۰ هزار دلاری اعضای هیئت‌رئیسه پس از برد مقابل ولز شکایت کرده و ظاهراً برای برخی مدیران کیفرخواست صادر شده است.
🔹
مهدی تاج، منصور قنبرزاده، احمدرضا براتی، بهرام رضاییان…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/689816" target="_blank">📅 16:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689815">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
نفت به قیمت ۱۱۰ دلار رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/689815" target="_blank">📅 16:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689813">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f91e2a63e.mp4?token=GdJVKkVsN7YS-sMCE879Vnfzry_p2x-m-EAiwLlLapsNhQ_ZQo0WoFzvukM8W8OkSOAXVGwcGmFI-uGnvQrV4g_9PJPNw3Pn_Duo5U-aRYHqAyI3-g_U16wO5GdpphnmKepnzG6plYyXng2rZzJywqGryAEGXivVdiOdijqJ-OWJ6gKlPL_tJJRIxmsnSnWb3mPn1JAhLcH3PITbQQ7qqBstzVKmor8GD3UNtUqwVqWRsctCqclHlXSU_AySbFpHURAKJ63Bb_3JlOjDA6whO5OlSx2Yit0m-9w7I9xT3Sw0A4NkWT3U0U9PAAH04V23K4xVsQsHWd-nx6QCRBsNzhdnffHhPF96GMWwV9OMbWzWnac6oZi6TD30N7woCbgF_oGnm2cD5GR4SkZQ5d_UUk8Ar_2cRxGjbsjpmp4nNGxmO-zypWM8IZKdlkPlvFOiDPCOV4cif_meVlzOS2AGTfVVe4NSDmbYuZDyPi8qXa5TpqUN7_ZTMiPwevGP2F5QhYyOr-48RgFItFPPHH1LXKxf8TnDGXotVH53Bq-8Q6vF1CfqEKAsmzJtlQe8UEvNee18TsdNUSC5cCOTLlbnHI5y6XvLI_kM5hg8AyJzyBrc9pglvFdRfTLtsFS3pg99p8f_5yt0cqcgkh-rrf9lLIoq3vepk0sYfPzE_MaNt_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f91e2a63e.mp4?token=GdJVKkVsN7YS-sMCE879Vnfzry_p2x-m-EAiwLlLapsNhQ_ZQo0WoFzvukM8W8OkSOAXVGwcGmFI-uGnvQrV4g_9PJPNw3Pn_Duo5U-aRYHqAyI3-g_U16wO5GdpphnmKepnzG6plYyXng2rZzJywqGryAEGXivVdiOdijqJ-OWJ6gKlPL_tJJRIxmsnSnWb3mPn1JAhLcH3PITbQQ7qqBstzVKmor8GD3UNtUqwVqWRsctCqclHlXSU_AySbFpHURAKJ63Bb_3JlOjDA6whO5OlSx2Yit0m-9w7I9xT3Sw0A4NkWT3U0U9PAAH04V23K4xVsQsHWd-nx6QCRBsNzhdnffHhPF96GMWwV9OMbWzWnac6oZi6TD30N7woCbgF_oGnm2cD5GR4SkZQ5d_UUk8Ar_2cRxGjbsjpmp4nNGxmO-zypWM8IZKdlkPlvFOiDPCOV4cif_meVlzOS2AGTfVVe4NSDmbYuZDyPi8qXa5TpqUN7_ZTMiPwevGP2F5QhYyOr-48RgFItFPPHH1LXKxf8TnDGXotVH53Bq-8Q6vF1CfqEKAsmzJtlQe8UEvNee18TsdNUSC5cCOTLlbnHI5y6XvLI_kM5hg8AyJzyBrc9pglvFdRfTLtsFS3pg99p8f_5yt0cqcgkh-rrf9lLIoq3vepk0sYfPzE_MaNt_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۷۰ درصد ترافیک پهنای باند کشور مربوط به فیلترشکن‌ها است
بهزاد اکبری، معاون وزیر، مدیرعامل شرکت ارتباطات زیرساخت در گفتگوی اختصاصی با
#خبرفوری
:
🔹
فیلترشکن‌ها بیش از ۷۰ درصد پهنای باند درخصوص ترافیک کشور را به خود اختصاص می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/689813" target="_blank">📅 16:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689812">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjfkKxgW_cinkpN697pb3A4A68ZxzmZTgbj8U08-0Ou8v2zDruupWRhonWEtWPenSjIqhfvZOzTaqLE-ZhcFNILTjn-Q7QVcxjsMSLDpMNqKwsTXyCkWarYPuqV1v9xLGo3TRnXo7E7Zuk2Sbnj1nCKwB8sdu0-IS9Pw1_Re-9IiYCvMgARaKoJS1Vwgte9y8l7OUD5KdTqm3VmUjgsSibYFyiaHpsDoKm2e51MSXpGGyFshGF4CzojfMmkdK7AnkXTuKgJZKI_0L-gnmRBbvSVwtRsvMB7SqT0_taCoiSMFtw2Z6OhUjuqEllN6l1LXkIFTZRIdjXlg8YTQ1RkIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شرکت صنایع پتروشیمی خلیج فارس پیشگام تولید سوخت پاک شد
در میانه جنگ و تحریم؛ تولید گازوئیل یورو۶ برای اولین بار در کشور
🔹
با تکمیل و ورود به تولید پروژه گازوئیل یورو۶، شرکت صنایع پتروشیمی خلیج فارس پیشگام تولید سوخت پاک در کشور شد.
🔹
در پی برنامه‌ریزی‌های صورت گرفته برای تکمیل زنجیره ارزش و خلق ارزش افزوده بیشتر در گروه صنایع پتروشیمی خلیج فارس، این پروژه که از سال ۱۳۹۹ آغاز شده بود، به پیشرفت ۱۰۰ درصدی رسید.
🔹
با نهایی شدن این پروژه میزان گوگرد برش سنگین از حدود ۲۵۰۰ ppm به کمتر از ۱۰ ppm رسید؛ دستاوردی که می‌تواند مسیر حضور این محصول در بازارهای بین‌المللی و به‌ویژه بازار سوخت‌رسانی دریایی را هموار کند.
🔹
اکنون پتروشیمی نوری ظرفیت تولید گازوئیل یورو۶ را به میزان میانگین حدود ۲ میلیون تن در سال دارد و بسته به شرایط خوراک و ترکیب برش سنگین، امکان افزایش ظرفیت تولید نیز وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/689812" target="_blank">📅 16:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689811">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
عارف: قانون ملی توسعه هوش مصنوعی سریعاً اجرایی می‌شود/ هدف ایران، رتبه تک‌رقمی جهان است/ جنگ‌های آینده، جنگ فناوری است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/689811" target="_blank">📅 16:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689810">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اعتبار ۵ تا ۳۰ میلیون تومانی خرید ویژه پدرمادرها
لوازم مدرسه فرزندان را با اعتبار بدون سود و ۴ قسطی بلوجونیور بخرید.
برای دریافت این اعتبار
👇
1️⃣
ابتدا برای خود حساب بلو و برای فرزندتان حساب بلوجونیور باز کنید
2️⃣
یک قلک «مدرسه» در اپلیکیشن بلوجونیور بسازید
3️⃣
بعد از حداکثر دو روز کاری، یک باکس اعتباری مدرسه در اپلیکیشن بلو به شما نمایش داده می‌شود
4️⃣
روی گزینه «فعال‌سازی» بزنید
5️⃣
با مبلغ این اعتبار از دیجی‌کالا خرید کنید و موقع پرداخت گزینه «اعتبار بلوبانک» را انتخاب کنید
سایر جزئیات طرح را از اینجا ببینید:
https://jr.blubank.com/campaign/back-to-school/</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/689810" target="_blank">📅 16:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689805">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qK1sYV-Rbnd2GaZMFJd79rGEOkVErNXE-0hfOZGfiY_det6b7q2QS5gcPcfLE-yP87rUfCM4JRogoWupRh1GsmtXywelA3ba6rc7_ZNBXkko4DAeCA8T7rwAHsV0XXK7Sw-7rt7Hy41XTz3IXLYXnu1v1PhAwJmQ18MPlCD3STWhNqP6uItG0nOS_Nx7SY_NiuFo1KNm5SJ2-Tqr4tOg_nJjsO_gYMVetBFMRkam0XIfVY-fZ9oee6AMoepn1TMHAAACy_jpbeRBwyTjbikdhOKxDv2wlgMyY7bzqcSARODJrtSKnF3fctiJ99b6DZDEEqBBDU1VaJVeK7zrTGxT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3Ahy_ZLpc9FOfWetHxstVM7YH_zMPCYnhwwXoN2zK9gCPpj0ifYeGXDtxGjX4fHEUL0jRaLPSKVwdG53yEMYCooTcGpQfYB_yhjoAIyd-NYKWMyllyxXLh7HDCxzfs6A9O-7GCwCAWXRLsuTHyYegfNQ7lfYN7VDuivSS16X3nXedo0d7xenhgAuyYwzL1n6F0rJRYVwet6GnpJYYRgpcSRRWAG4gWsevPfnMLA6MZ-4R-mEuy5TM4zVULU7RyJ4mAL9yStMZJXVTBt1zpugGTgGKAEvCJg32LmAvW8a8Zu1XzM6TjKf-kV3zmKsh1FK2QsIn1EAeUT2UTz-Nyd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijxf1AVigyzv1xfakndSTbPDNsMaztkxZ_T_GP7E7yYB1XRkjfOdsvuT_2Pr6cHwj2onDWZ0oiONAN8a28RK6l1W5IJjpZblePgQdNZR0PBNKlp97PCcPu9qteodfmsRh4ynSNohyalTwNpWUQMk8J0N58FLOCNuHwXURD7OWy377JnhBrUTeXBDkv1IL_VTRHG3-LcfED6cHd6RW48xxOqKhtjewhTQhZGrrR10c2YzEgtQ0x0nILqd8VC9MO-5rWxPTGfwHH1JBwgLL3yQ2E1laUXaa5h61C9Opouk-Esw9x5ZeKHr7xnYcO6TEbJRKX38zjQjCnNM1o9AeszjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YgjkzeziAKYnk1rvJ2iI3GFxD9DqdWSIDcZJkBENWIDJ-jmqvigNxNO7Z0tNTM37HziOE6u16pYHs0ywwPXFrxUqwr6KRQV7K1nK49tdY0RDgOnNrGYLhwxpexdVJGlFcGULmzhjVBdE3vc8huqTJ1Ci3ZzIy2MGnarWS_bkHner_YLgrovH48vesEAh5J4gff6GtKXIdQJJIRdRoAAMxKx1tDtDzfNC47ZgYFTWO5I0KplAw9xRVGbe0PrIp393PdCwag0zlXehjX9u7PK4f6Wu474E2A7FU7dvbDUNn-_eKFRC6jSNYSPv780Ul33oD2qN9cqVAP-8vfd_citJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vR0LeKXsSY2sAXfeb4j1eNvYAPTt54Zx6n7EYbN6qF_hM7ei80TGBWgrQvvJ530rKfW2bk7YFQjuBmKLNKSq8iFBCMHkmVG2cEX-vVvwESuVBxP8m-xOJAMtm1TXqUbTtdHEW2S4FcwxwBO-MHoV506XmedOVVrPjkSLwC2bJIp7oslFsRInWTMKiwD1GnYeGQZi3Z8wiUPCrL-2Fpzjqt32NVw2f7aAIxnrQFKKCH71M7z2BS78_9Zv3Ox_OqfbpALoaXWbSv8O78t-EBrl9jWIBrLMWRrLfr3sNpiPsUUXUyGH5C84sFP7_urgC_2kkEt3lhwxx5YcGU6J0Xboiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بیت‌کوین یا طلا؟ کدوم برای سرمایه‌گذاری بهتره؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/689805" target="_blank">📅 16:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689803">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
وزیر آموزش و پرورش: با تصمیم دولت ، وزارت آموزش و پرورش مرجع تصمیم گیری درباره تعطیلی مدارس شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/689803" target="_blank">📅 16:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689802">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11a15cf91.mp4?token=u0pB4Y_nzxCnf8NHuCCN3UjGF8RoHNUmEjao3J9xUknuU5Mp88TnncQRLJmWHyul3R3XRGWgrEpNx1QuauTPHxPwxSzT_kFp_f3mRJB1hEaoOLD6QdBTYX-eH1Xg8hvkKDBvNRbx10Itbyoq_W3l1jSOVtsPxDWsqDqPGtTEnpe7gx8B9ZZM1WFxbKzGWH-7mxUXX0Om_xelXpWTK0dxI-M0PmmcZ--hImEVIHTO-M3GpeHiP0ztV0IPPrC1R6SJ72nnn7T_FA2ccurBVsVDi3RYR8ec8LfUf3noPZbXncrtehOF7p7Yt7mp1Dxancdi_apMhgUYEZHab0SBc9boHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11a15cf91.mp4?token=u0pB4Y_nzxCnf8NHuCCN3UjGF8RoHNUmEjao3J9xUknuU5Mp88TnncQRLJmWHyul3R3XRGWgrEpNx1QuauTPHxPwxSzT_kFp_f3mRJB1hEaoOLD6QdBTYX-eH1Xg8hvkKDBvNRbx10Itbyoq_W3l1jSOVtsPxDWsqDqPGtTEnpe7gx8B9ZZM1WFxbKzGWH-7mxUXX0Om_xelXpWTK0dxI-M0PmmcZ--hImEVIHTO-M3GpeHiP0ztV0IPPrC1R6SJ72nnn7T_FA2ccurBVsVDi3RYR8ec8LfUf3noPZbXncrtehOF7p7Yt7mp1Dxancdi_apMhgUYEZHab0SBc9boHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لپ‌تاپ هم اجاره‌ای شد
🔹
تازه داشتیم با ماشین و گوشی اجاره‌ای کنار می‌امدیم که به یک آگهی عجیب در فضای مجازی برخورد کردیم.
🔹
در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/689802" target="_blank">📅 15:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689801">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb5e17aa56.mp4?token=WJilEzhQLrGSeswjYQHHMcCrZh-Pgc6s4yg94b2I9AqiyAdq9gaZiY_m7aycif6h9tI_IO8J7IB4B47fjJH0Vb7oj4pqx_9ebQdel8yOT7Ha2nMFLQLZok6P4dF8LNPA0VNESpNfvQwv7yifEZ3kUYcGNK046g212FNRHZ_9XGHGe4hhXSke7UjYiAYas1RiabiEt0iGRRnmhW-01XzW1zmRoriAID_Bfq5YedJuX6z5HcAJP7tJRNnxK8bvmZQAPiJwcYpysL9rzvxcBXD1n2SAhbDxHlzSeoi6gQg0ncT6AS10JRMTcmH6H8iYL6hLt_tKTDoEB_A4cJ5e_9Vqqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb5e17aa56.mp4?token=WJilEzhQLrGSeswjYQHHMcCrZh-Pgc6s4yg94b2I9AqiyAdq9gaZiY_m7aycif6h9tI_IO8J7IB4B47fjJH0Vb7oj4pqx_9ebQdel8yOT7Ha2nMFLQLZok6P4dF8LNPA0VNESpNfvQwv7yifEZ3kUYcGNK046g212FNRHZ_9XGHGe4hhXSke7UjYiAYas1RiabiEt0iGRRnmhW-01XzW1zmRoriAID_Bfq5YedJuX6z5HcAJP7tJRNnxK8bvmZQAPiJwcYpysL9rzvxcBXD1n2SAhbDxHlzSeoi6gQg0ncT6AS10JRMTcmH6H8iYL6hLt_tKTDoEB_A4cJ5e_9Vqqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج یک هواپیمای خصوصی از باند فرودگاه مصراته لیبی؛ این حادثه تلفات جانی نداشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/689801" target="_blank">📅 15:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689800">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57561ebec.mp4?token=NeXqsuf2fAcKzX43cF2ZhlEy4-mNbHRTsaW8gs73LU9xHMHfsh9hmq2_CkYcxHJfiLu8VHbgl0-tLyiFTTqzqkWczb6xKBBN1mqt8gdXkczbHrk5wVB19jYnVpsnzqqASQc_fTe5V4aaU6Ig_FuHr3b6yjhM07LOQSPWklax1ldZCUBTf-ipp4_5Ymalbsl9Ll2MsXEeTq4qUtuCT9wf0uRAuRqZxCmSGVqBM3x5dfU98Lo-4HrcSvMAzv08unaNJtMdCrjJfgGOaxdD1Kt7k3CxISFY3z00Sxv3ebpNgu8bn17_MXY9mVQn5UQ1hq4CzEjzOJHK5qCtA_Hw_qCAN1e9QKkkL3LwURJERchyphqsWvHygvojTq_rf5Y_qGabE8Y8-T8-9iZHthz1_b6KT6SZkNa8w8qB_dCA6nBFN84knWDLf4r-jG-XNvoIRAqGQDbI93ZJTRsCBy1G2KfyLY4yQPD7-ZCux9cFvDXXiQSZV2fwnHz63-tnkpKsfm82wnfpxzm63sjKpXmCaq0CMI9VAdmJIEvMTivMb3XA5mK8CeDKQAWFDqkDVHL6beCKpS71xSBpysG1SktSkiait8EhqhfJEEvtkekv9Uh7xELiQws-zLstvg4JZJvnE7X6CHpHHe0v16Th0d4auLNVDjJgKNmN4mwEuelMtbZM-78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57561ebec.mp4?token=NeXqsuf2fAcKzX43cF2ZhlEy4-mNbHRTsaW8gs73LU9xHMHfsh9hmq2_CkYcxHJfiLu8VHbgl0-tLyiFTTqzqkWczb6xKBBN1mqt8gdXkczbHrk5wVB19jYnVpsnzqqASQc_fTe5V4aaU6Ig_FuHr3b6yjhM07LOQSPWklax1ldZCUBTf-ipp4_5Ymalbsl9Ll2MsXEeTq4qUtuCT9wf0uRAuRqZxCmSGVqBM3x5dfU98Lo-4HrcSvMAzv08unaNJtMdCrjJfgGOaxdD1Kt7k3CxISFY3z00Sxv3ebpNgu8bn17_MXY9mVQn5UQ1hq4CzEjzOJHK5qCtA_Hw_qCAN1e9QKkkL3LwURJERchyphqsWvHygvojTq_rf5Y_qGabE8Y8-T8-9iZHthz1_b6KT6SZkNa8w8qB_dCA6nBFN84knWDLf4r-jG-XNvoIRAqGQDbI93ZJTRsCBy1G2KfyLY4yQPD7-ZCux9cFvDXXiQSZV2fwnHz63-tnkpKsfm82wnfpxzm63sjKpXmCaq0CMI9VAdmJIEvMTivMb3XA5mK8CeDKQAWFDqkDVHL6beCKpS71xSBpysG1SktSkiait8EhqhfJEEvtkekv9Uh7xELiQws-zLstvg4JZJvnE7X6CHpHHe0v16Th0d4auLNVDjJgKNmN4mwEuelMtbZM-78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای دیپورت دانشجوی ایرانی از آمریکا؛ FBI من را از خانه خودم بیرون کرد/ دولت ترامپ حتی به قانون اساسی هم احترام نمی‌گذارد!/
تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/689800" target="_blank">📅 15:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689799">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfoFpR0VfP0-pTUARqdoqiM1tKqbvKE0LZtaiQEyOjOolgsy1VdqSnborkZ7ZtEQft2ztpDOfH5ow3zwbw1pJgoHE0w1ndT4C9sU46dni2grBgeAB1uyV9S9oVsh6stUeZaEvLGzKN8p52ApmGaD2sr8xFsIHARj7ohJ56Ja06TdckGZoJEU92QPgriOvK2Imz29eP2qEdcGb4FsToo1cT650QX9vXlpj2NG8h381VxkkfsUcbkOSz_La4xMjZYy5rsdKKinS9AfcclEulOzd_jyR-QB9FOQ3DStdgiCTz-YsTe0EHkghJ8CgQRyjCtBg-hVMH10KnRHE7ds4t4GYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام گروه‌ها مناطق مختلف یمن را کنترل می‌کنند؟
🔹
در پی افزایش تنش‌ها در یمن؛ انصارالله با پیشروی در سواحل دریای سرخ، بندر مهم «مُخا» و جزیره «میون» در نزدیکی باب‌المندب را تصرف کرده و نیروهای دولت یمنِ مورد حمایت عربستان را عقب رانده است و این درگیری‌ها هنوز ادامه دارد.
🔹
در سال ۲۰۲۵، روزانه ۴.۲ میلیون بشکه نفت خام و مایعات نفتی از مسیر باب‌المندب عبور کرده است.
🔹
نکته جالب توجه این‌جا است که حدود ۷۵ درصد جمعیت یمن در مناطق تحت کنترل انصارالله زندگی می‌کنند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/689799" target="_blank">📅 15:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689798">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
وزارت دفاع امارات از کشته‌شدن ۲ نظامی خود در یک «مأموریت آموزشی» خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/689798" target="_blank">📅 15:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689797">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
خلبان آمریکایی: کل امیدم برای بقا این جمله بود: «هرگز اجازه ندهید کمبود انگیزه باعث شود که شما را در تلویزیون ایران ببینند»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/689797" target="_blank">📅 15:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689796">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW155gazoYumL23zBI3nbBvntxDjmZLiHeEhM_SGyXH7KjTOyCgeVYOrMMMsxtSExBW3WcD0jQAo72kKXPvwm1V-GQVmV5UyYhc619U9lefZQbO_SuJfUtEI4J5-ugUjRFXvXt7Oiyf4lVvTcJEImaPF1UZtqNzJnB_7KpovVFaBCtx8gXs65Kp0w4KZpJG1RI94CEwhJxlW3GbnkAyN51WqS0F_zfvuOMGlIUEKX6khja1yktbi3CxbChSiFJg_TNXmFZEkRPZta76y3LpyV46ZDO4Gh1NtehozFpNyZceexm7AkPWMSnjaHbNOUCDGj7o4NjOuYVcZxxdZe2z1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
می‌دانید سهم شما از ارث چقدر است؟ این جدول را از دست ندهید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/689796" target="_blank">📅 15:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689786">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BckogcjGDlLIfSuc3swoBZ_qpdN6wc3nedcX1gD5akCbJQBYj4qKwZUffeKlUWbKKTKBsUj3iYjY9e16qF5Dl0rg1BXyEgJTLB5vMX5qV0PCJ3ObJIAxWw-P0UwmN-cq41ZjiUAlPwcjLN8i7uBsxx8eWX4f1sgJoFfKs6c_laGNnKZfXtdjLOHPAs5gRJCnXnsFq4TSpN7V6nv-pM7FzznTrIZET9vzxa9W5AbTgzOaczryjSFyyhWB-SccYmMWqzx7IxaimCV6G0SPQ4ApCjXgBYt7f_mJWwytDZy09gZpaN-QUTwcLfjFsKZ8rSm5XILbR6ghmyGZWHk_L3YHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3cBSgx5_2BPuTlUhKEbkKV-PFNw7rSfdwqakxidINnJuLZm-E-mbpxI-zqjB5IEA7veSwZFvD7t2h4qCpAOCEgIyxV9MpUPZ5sn8KVTK-_xFcT9xThAjoX6X3UelLgIGEbonNiPseSdGV-7hvHtPR3HdTE0aLXG45xMiptraK8TU8yHERZuGkLKvUUj_1OenNLR-gy4jiZUKKA32QsHXaRGLcuPLsybEyZXRmpH1rIT-kDn9GPuHdPhqXkJgwuwB9k-bWcvA3F0gYBPBvM92CySTh0tNjfowiBCZcvywZCAni43_CKD-9nNLj8dmR3at23F_95mUR40MHG6ojMMeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXuuHlT4SOzkzWerrfCprNRp9QNkO7GhtNcsPz0QITiXFHIh30rKuCjxrqEes6Gzbg-1GwqGCKV5HG_fxaEsuq2d_eNdg3snokJ33TcLX_W0zhLZjvcG34zY8PqCGElmHLzs1g-t_wYvdd24HPhbI6lIscAhBxvSR-0vchILBjw-Uc4jHyLPPdEWI-kh8yaZykw0QUtHEVK3Oip2pmWtPXA8E5I4QBpK3omn8SzOANVRCobAvKhP1TH6v7v1QuGMWaS-_8zeurSqPNgZfvUMFNQCeQOsbt1_pO5AwWOVdOjRVY1wj7aXpso7YhRAM6IXjvYKKsaU77QkShOavpiuRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KX5Bg6pbNp-PEPtqimDTHIsNmUaFJbgi96EmS5sLGXG2AWIN5CXV76MBLbkJcDtUBRsYYfhE7fL_V5gVEJtyxw3tGI0RPL-Hk8vM5GVbmPW_F8ksiWiKL0pNtaw_RmxNFgJzU-xYvBi5zRNLf5qF6KSoMvPxJSuMEQIVy_5ForXUXjeGfmf7BduX4cj5xjod5mXGp6U8MQIteH9h3PotQKC4XfEYjmehD7XjLNIrAV38n_TzdksTWZc72BwUyflbC3dq4paHNSwbK3k0Guwm7hr18i7fhuNOTI9Md7CPjB2SjEQiGRwuAmJ9iBHsjJizitYS3ad2uvX_O_OJD5zfZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STKcBd_UXG4WUtZz7uRIlJ0e5AHvXOixTO-4xOkRUga7siEk35in_7wvbu22BIULpjTq_uk2EfTs4APWP7OANWbgC-G_J4z8ZxJPqLE2uo9sxEmA--W6wwtzcfjsgP1AEJF8ncEfe0Xuc_Mv5si4vYb_Vl9pjWEKh09Z-dM7u95GqGZhbo8DfYrK8lH4b8fZquiejKO_dSeOcxfLGbpoJ730ZuUgXGbfPKMX3NcTpq6Nns2zM1htLQjDrAx3mgyblMLh6_ZLubeLe0nUNVOzmEaCJ9NkMh53xAsBy2B8vvKbJO5KoQ8v-Z9OfFjof8WjCHpMK9AjPmh4eNA2MsSP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgPm3-u1pvfZj9gNtf8IJ4ilguPlmcWMPVKl9wfa1p7hQt-hutsaZR10xCX5OzEpSnlImu6Vd7WMFt-fDdxSSXG4XTQAVCE5ZiDFdNsX9gsWwz4yDHTamJqBEMBIZis84vOyp_jTojPNLRGRUZ1ZOZ8SN40xxXN02gPKkpeWJXmZ9-Ozq2bohPuSdj75nsYZ82h9wNm9HAUfK7RMV8Tk6jnAZQSEgT5V5anIjeWodGM7avnl3YlacLUIDv8DXGNf6nhBhUAYKUXDnPAzG0h3Ne5ZUp2YOKH0eGT0Qb1pgcwFPv17KZ62-mL11M187tzQmrW4nY6K90ESYbdVDMeD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWTbVkl7yGDUz-azdFiCpD1epV_UiF76O79QpYkTkaLWmSp2xvhpVFLfbKmQqMihOXfsQ4hsNi9U5efC6VZd8S5VW4c1b5vl4-PCRI2qiaJt-z-Z4KvDVjO0VCEbDNdIYUsNqA3Rnr-VJqkg0v2Mo3oxIplcheUtAOjUPmLf2frKeJO-sAGuZ1c9DDw-cCDm86qgkI6__QozAEd0yN2KUtbu6fFoLDaBGDKIwF7eJycUgYU2aqa8-Bj6tAZBww1UWBI-vtTSSgPZx0eN1JyJI7L3koE609ZXfZQrXa1vusq1ZiGeM7u6-Bu7FMg_i_f0YkC9fsrfgGuvRYWXsmWnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GK-xo4Zhuh94tzO9WySrckJpfDvUUZgqF7yybJKfiz1sgEPkr3pdorSiXEsJUXXpsBGnR7C5LUPkG1BPkrpO4RxktWg4OFtb4yi43APcM8EqKfMyzE3YE7uloM7c8Vr5h5274SvoOz6U7H1oh7YVouj39IMA2nhvJ7nYeoD53v1TfG8bBEqQueCz7dGFTzh1SNEBslVmEuxsnFtU9ppyKQloQhj8Kg0eTKLeTYqLkCjGCndJIh0exmJwVxFD5soDI464izRc75QQ3zfnMve4cCQx7j8V1Dd2lw0mgY_i9mrRlZT62zL_vYuVf-UatXkOTn6lfawR1y1bqKwO1qmcHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qlJ9v_NkGeFrNJmSDk413lguIHL6XtG5HQq_VTQsH6DUaMQhUZ1wvGJuvFVZuY3A_vlXuNE5yJUBbfpsZjkRTmTfqYEhQ30z13pEbfIBjjZ4gX_SxlhJfaU2vN6Nb5PvCJ4w9vbgerVQmheHtTdwwXT3pRWTSxf6SuPMi0DeICOFC7m9rKo9vTL7qFQ8h1oZn7f4vofoz9xAfRbXKS9hT8CrxYhK8Lh0_n-C6boclSsbiSdYs46FXhvm_XJcNrlNVN8iM7OfAfUOuriTFYTXnuSYZq_NyleqfVxkdqhy7FaCkCQO5RNq2fjbqit7S7PJclc1cwWDUIk8rzDsnLLvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AusI7iaMfm319mVdbF1sK4GxHDhWGb6oqax9jLj015Y4Rosxjl3wXQ_IJ1kAqg4ApbQMRxvW__wVmq-UyWoZ0-atf3oNDqR4zEyVJn0skBA9mWLgqm0bk2f9gYlochjcwUeNjSvyQuaxWxDrj9pUYfMQ0FfSOyKANvCbvs3qqne1h9gRthItb7sf1rCKdVyHxBM-JsZUB1HIpUXOD5EXf8ejmafG4tdg098OAK4UrOnfDORyU-VjX86UPOvjv97wFdK5S1VHPSosWqBYmrb-OCYNgxIZH37Iw9YAttpFGJXg-gQq-AGXc_eiLo7kY-aNTapAKnuvWq1m56TqdzlhDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
دغدغه‌های والدین و دانش‌آموزان پیرامون ثبت‌نام و هزینه‌های سال تحصیلی جدید
🔸
روایت خود را در قالب متن کوتاه ، همراه با نام و شهر به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/689786" target="_blank">📅 15:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689785">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4903cea3.mp4?token=WOSXczC4TNibcb059WIM7D8GofWu1z0NrlzJCqxLlmg0MTAUbfcmxRrsDnpc5scweVvJI40upF6eJdttiZkZ9jy7CGZuYHPXZHyOON95-ZKvcqIp_QgpnB6BRW_daLpKJD9t2pDMUxM5TjTWwYCX86JCf-e5Fp9A5lOxUCfvQET3qPlkD97Adb_JTv81oIjTnGaOT70cKsy1rDI-DC0KamUiy-Lvc0oy_xgZ1fUF3YlYjLlDXPRjX5_cd-jA3Xs2ZRtG0KH035QNQffiznE4fy4hn0xwInF5ze3XcwDiWrtvjeSxp2J1iwtbVtKkuRme1spzuVqqdkHo0KDy_64jeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4903cea3.mp4?token=WOSXczC4TNibcb059WIM7D8GofWu1z0NrlzJCqxLlmg0MTAUbfcmxRrsDnpc5scweVvJI40upF6eJdttiZkZ9jy7CGZuYHPXZHyOON95-ZKvcqIp_QgpnB6BRW_daLpKJD9t2pDMUxM5TjTWwYCX86JCf-e5Fp9A5lOxUCfvQET3qPlkD97Adb_JTv81oIjTnGaOT70cKsy1rDI-DC0KamUiy-Lvc0oy_xgZ1fUF3YlYjLlDXPRjX5_cd-jA3Xs2ZRtG0KH035QNQffiznE4fy4hn0xwInF5ze3XcwDiWrtvjeSxp2J1iwtbVtKkuRme1spzuVqqdkHo0KDy_64jeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواشناسی: از پنجشنبه سامانهٔ بارشی جدید وارد کشور خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/689785" target="_blank">📅 15:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689784">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331f7fd9e5.mp4?token=pCntFkXubgGzIOqhWYG5QxUp7fz9YwyfE1R6Ixzn4jXRg5kpVWau8ZSuY1z_OBF9gU3-4kAVIYbvzC27TqXHEivFGWvjk1zM5VHwCn2ndMaCND21o9BQemzTO2yQ9k0Vk1sJyDDrYqOK7XDZySYaLVQau8D-32mp1YkZNQAjZg_QAQ9AaXanep-gHtAyDZRe3GPdnW8jjLE1woSApFe9e8oeXk2uv6j7n-bavDJwCMWXS2UXnxJe-0eGsi8x2AhMXum1vgi8Tb9x1EpqH-tSYUoEPJ9J2_trYnfldYDXflWYt9sGCfpn65ak-P-7Zk4KjqFRktb5zTg9-TUEqnjuOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331f7fd9e5.mp4?token=pCntFkXubgGzIOqhWYG5QxUp7fz9YwyfE1R6Ixzn4jXRg5kpVWau8ZSuY1z_OBF9gU3-4kAVIYbvzC27TqXHEivFGWvjk1zM5VHwCn2ndMaCND21o9BQemzTO2yQ9k0Vk1sJyDDrYqOK7XDZySYaLVQau8D-32mp1YkZNQAjZg_QAQ9AaXanep-gHtAyDZRe3GPdnW8jjLE1woSApFe9e8oeXk2uv6j7n-bavDJwCMWXS2UXnxJe-0eGsi8x2AhMXum1vgi8Tb9x1EpqH-tSYUoEPJ9J2_trYnfldYDXflWYt9sGCfpn65ak-P-7Zk4KjqFRktb5zTg9-TUEqnjuOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر نوع جنس و پارچه‌ برای ماندگاری بیشتر باید با دمای مناسب اتو بشه #فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/689784" target="_blank">📅 15:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689783">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yi2hnhFIgg11dNPXGwtZl5Xtf3DU9OakE5LsL5oCbWw1FV-Xbg5PZ91OtxbmYW2imu4N-UQdRHHYA5oodjb760WSEyFTMD8oJoBukYSpIM3oLtWlHTuEU3YM73Fj3GE9ap6vO1avPqYRpNgiLwNTOCEBtTTchbNJtNLVdBr7v66qYvExZtKqSNfTB11Vh81B8EH5rBUN39Dafg-8BF9Cy_dyDmLjM_wBNL2Ne4PAHAYun9EdSbjOtHnDx-My-Cqp79QhzU7qv0Quj5b2b6o0mLePf457pU3uBz_oTkTw_osTE5xoprqXlf9yI7OgUf798_EUJfj87Jx-U9qqsHD8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
♦️
۸۰ میلیون بشکه نفت؛ ۴ تراستی و ۴ ابهام
🔹
حدود ۸۰ میلیون بشکه نفت پس از توافق اسلام‌آباد در اختیار چهار تراستی قرار گرفته و نحوه این واگذاری با ابهام‌هایی روبه‌روست.
🔹
مهم‌ترین پرسش‌ها درباره سازوکار انتخاب این چهار تراستی، سابقه بدهی آنها، چرایی فروش اعتباری و حساب‌باز و همچنین مبنای تخفیف حدود ۸ درصدی مطرح شده است.
🔹
گزارش‌ها حاکی از آن است که نهادهای نظارتی نیز درباره نحوه واگذاری، شرایط فروش و تضامین، خواستار ارائه توضیح و مستندات شده‌اند.
🔹
با توجه به حجم بالای معامله، پاسخ دقیق به این چهار محور می‌تواند ابعاد مالی این واگذاری را روشن کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/689783" target="_blank">📅 15:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689782">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ab367382.mp4?token=GiujzVxuHhfe7Zpj67PeC-WjFsz2z_TLQ5yt7XJ60aHRe86Auh5LJl1ZQ_SNGFGpVScOAaVOdRg9sZH1cOlfEnDqs3ZY_6vy0qQLLvF8lf0yNHbwZekgInBuH5G6Q2BqpdDqul0-xxJ2uZBd_Ury-7kY0x1I8YXx_5sEIP19Ri2BJAB4qXwOwcWWaUT9klXS2qIj3gxFJrxTLrxiNfnBfBoqntEX3IdwDj34zUHM-Myyc9jcknku-FJh8AfyTdQpEymvYRRBKFgxcIW8jbn6ddCE_b5oOgrJz6KzNLmsJI9nkhFjTckTlrl0zNnL_FtaoCRWnpGehBtHTmVow1xVHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ab367382.mp4?token=GiujzVxuHhfe7Zpj67PeC-WjFsz2z_TLQ5yt7XJ60aHRe86Auh5LJl1ZQ_SNGFGpVScOAaVOdRg9sZH1cOlfEnDqs3ZY_6vy0qQLLvF8lf0yNHbwZekgInBuH5G6Q2BqpdDqul0-xxJ2uZBd_Ury-7kY0x1I8YXx_5sEIP19Ri2BJAB4qXwOwcWWaUT9klXS2qIj3gxFJrxTLrxiNfnBfBoqntEX3IdwDj34zUHM-Myyc9jcknku-FJh8AfyTdQpEymvYRRBKFgxcIW8jbn6ddCE_b5oOgrJz6KzNLmsJI9nkhFjTckTlrl0zNnL_FtaoCRWnpGehBtHTmVow1xVHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا فرشتگان معصوم‌ هستند؟
🔹
راز مجازات «فطرس ملک» و تفاوت خطای ملائکه با انسان./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/689782" target="_blank">📅 14:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689781">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8iIKq2RMQKqPSxzQXctNkvPscE0-72sAJx6flD390mGGnUwzOVSbazO1q_VhOmo9eJW0xu0nXWT6-fjzwZR-JM76026QvvZ15QJVc_J3nG7palBBkZV029OpxXmpZivc6M9vtpCWlpf2NurKcjl2f04R6qb51jGTpkAAG-TPApwoPm1bUBTaSgPcekbTVumcxgOepy-TIG89X4FzBSHQrEd5Vs9XIWt0q8xygWqsNO9KaeE3XKyBYieLLBs4m1fdY7Sgd0viPW8VlKzQjuRzURgqVa7uz_LSnhIYN7mVLhxSIAaNQLOdkIKALLgUoCjkV_HpvcFxLahKjvH_ek3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در دقایق اخیر؛ قیمت جهانی اونس طلا ۵۰ دلار کاهش یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/689781" target="_blank">📅 14:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689779">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtbvMHSl1fEp9Q56bhJn9THapUORrMKyZhuUx4yrlyNDRF2oKuWaZqOS3_N-coeWgd2WfE4xCk-f4wz3f10BQJgrnLd8HrU3V82HQFQk9gAgFXcltzfOWbPf8oW92lLDTC8ioeQUPP_gOT3IqINS3VRZWRL4E441Uayw2Qobjb3PZ2KO-PFEMfvL3K77JI8heKPEWq7FdDsNZ1QO8S7E9htP_ycbjY1XVgaVtUh0e4YsOwJXYIoOzd9sEX3DaQ4vlbhucCgyAbZMQdd1WP4mOCnlCnhmi_s9TSAGr1kQF7zfxaoB2u6vGdApGw9_-PUveXAvmj4FM8RMgsNMm7lT6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیین افتتاح کلینیک تخصصی و فوق تخصصی استاد محمدکریم فضلی برگزار  شد؛
جلوه‌ای از پیوند کارآفرینی، مسئولیت اجتماعی و توسعه سلامت
🔹
«کلینیک تخصصی و فوق تخصصی استاد محمدکریم فضلی» در راستای ایفای نقش مسئولیت اجتماعی به نام و یاد بنیانگذار گروه صنعتی گلرنگ و با هدف توسعه زیرساخت‌های سلامت کشور با سرمایه‌گذاری بخش خصوصی ۲۲ شهریور در بیمارستان بازرگانان تهران افتتاح شد.
🔹
این مراسم با حضور وزیر بهداشت، مدیرعامل گروه صنعتی گلرنگ و جمعی از مدیران و اعضای هیئت ‌مدیره اتاق‌های بازرگانی ایران و تهران و شماری از مدیران و فعالان حوزه سلامت و بخش خصوصی برگزار شد.
🔹
مهدی فضلی، رئیس هیئت‌مدیره و مدیرعامل گروه صنعتی گلرنگ در این مراسم به پیشینه فکری بنیانگذار آن مجموعه اشاره کرد و یکی از دغدغه‌های اصلی ایشان را خدمت به هم‌وطنان و ایجاد شرایط بهتر برای زندگی آنان برشمرد.
🔹
وی با اشاره به اهمیت اشتغال‌زایی بیان داشت: به لطف خداوند رحمان امروز توانسته‌ایم با تکیه بر اندیشه‌های ناب استاد، زمینه اشتغال و فعالیت حدود ۷۰ هزار نفر همکار را در مجموعه گروه صنعتی گلرنگ فراهم کنیم و این برای ما افتخار بزرگی است.
🔹
متن کامل خبر:
سایت گروه گلرنگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/689779" target="_blank">📅 14:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689778">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/450093983c.mp4?token=QGad7J12TUKD932g4gFu1FWG-RJzXPNtA-YspQUDP6zBCLF8I0Ousd9wWyo8xW9UqxZyRyc3iJ0IEs_xttMik7p7yo0cD6nSF0PkUPPQztStRCCcdyOvfX5ZiEHrSj6RdUj2EF0jxE6jpQkcUG1sHykaRbBXGwO8fEgCl9d1hjFCwmi_-GAWxS6m7I1pzuIt-cpvU5I_ONEHCeF9pQRK7A09yO7xfDujGNiz1UVEoxLM6LtRwQ0K_ru64Z-YNrMn5odtFtrItswX1tsov-8PM5yGvvwAXcp4YlSbqGjmLcAQGUSLewdwhKh-L5iR3e0ty-Go98ydR7qHORbg44xuTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/450093983c.mp4?token=QGad7J12TUKD932g4gFu1FWG-RJzXPNtA-YspQUDP6zBCLF8I0Ousd9wWyo8xW9UqxZyRyc3iJ0IEs_xttMik7p7yo0cD6nSF0PkUPPQztStRCCcdyOvfX5ZiEHrSj6RdUj2EF0jxE6jpQkcUG1sHykaRbBXGwO8fEgCl9d1hjFCwmi_-GAWxS6m7I1pzuIt-cpvU5I_ONEHCeF9pQRK7A09yO7xfDujGNiz1UVEoxLM6LtRwQ0K_ru64Z-YNrMn5odtFtrItswX1tsov-8PM5yGvvwAXcp4YlSbqGjmLcAQGUSLewdwhKh-L5iR3e0ty-Go98ydR7qHORbg44xuTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون مسکن وزارت شهرسازی: به دهک‌های کم‌درآمد تسهیلات قرض‌الحسنهٔ مسکن داده می‌شود/ بازپرداخت اقساط ۱۰ تا ۱۵ ساله
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/689778" target="_blank">📅 14:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689777">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89f8206d5.mp4?token=Z9pe0QGWoB4XTX3QMlds4r-oAXKpU75RNx9E0F3ZfyQc7vGqCs-QA6EIUE7xuDjxNdEba-tl37Hzgy7sDCUr82r0vEltcVIAIXMVC7_xZuqLC805WoGOyn1IONkC-1CuwCU2JQc90ePhst1bJQxmqcQF82ceFC2jLJqkzThknnIvjC6cw6QXOi47YoZAxwO0cPN69-f8s8LC5bhm70C9yvOUIejJ5ZautzrIF8XcHAu8ZTyf-SA3AUb-2Xf6BqzJ1ZMKf_jOsWZCqpyPOW2j4tee7_KXS7hCEiRoFotCo5JS5LxwdXe_md6zQoRcVDgPcn8PoIA_rsHkEdcGg5LLrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89f8206d5.mp4?token=Z9pe0QGWoB4XTX3QMlds4r-oAXKpU75RNx9E0F3ZfyQc7vGqCs-QA6EIUE7xuDjxNdEba-tl37Hzgy7sDCUr82r0vEltcVIAIXMVC7_xZuqLC805WoGOyn1IONkC-1CuwCU2JQc90ePhst1bJQxmqcQF82ceFC2jLJqkzThknnIvjC6cw6QXOi47YoZAxwO0cPN69-f8s8LC5bhm70C9yvOUIejJ5ZautzrIF8XcHAu8ZTyf-SA3AUb-2Xf6BqzJ1ZMKf_jOsWZCqpyPOW2j4tee7_KXS7hCEiRoFotCo5JS5LxwdXe_md6zQoRcVDgPcn8PoIA_rsHkEdcGg5LLrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطعات موشک به‌جا مانده از جنایت آمریکا در عروسی سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/689777" target="_blank">📅 14:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689776">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DntY9kwJ8NZ845RyKg-xTb5HP4IhRuobefzBN-KfkNtKtvLBU8AvEWiy8ONxiqpW56zhugTHjTcH5G5OM12k3tWWni2dn4p5ZcquwnYAwsyrmNdBUjeu01aMFPa5vv414v277sRjdezqcNyMVRYbzx9AipNCtWAEW7XkkfnE6Y0-KAEqLCSXriUOBQ9OYlmnL5R1RFAyvyLhz17QZymh6nEpi1Wsr-Yh0DnuJPF5XbKF-keIo_RL3I0oyj9iAOQQCIKqD9zMoPKoXYBkHZK5F-13RjICebam0mVygzkMgoiCbzxaznWwym3yGoxRB_WH2T7u3CgUumKjj9y6jD8WEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خارج کردن تومور غول‌پیکر ۲۰ کیلویی از شکم بیمار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/689776" target="_blank">📅 14:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689775">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86eef3fec6.mp4?token=pu2Aj47VJxOPRqh80ddKmzWG1N5n531NjWIh227e9McxywT1thQJbUkBjzFCuLFYi6MtDzugChCWIRc36zy8sABQ5fWJTiDsid4z1N_28W4gwj68UpCJegE_GMu0zbsXSqoVWrNXGkYMI_IUgGJbVaKLLaWBr5KytptxqDAHaOuOb33Xj9JumuR86RnKCdptSHVOC4V2UFrpEZ1q5z3ORKCincMMpBNO9KBT4VoIalE9CVmA1zIItel5orYINyLKiHP14amBJL_Mfs7LSekMOQlQRLv_ofuxAFq0otcrPxN4xS3NJCYas9af8sxBQ13vPnKExWJO84fzEHDbrLJNow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86eef3fec6.mp4?token=pu2Aj47VJxOPRqh80ddKmzWG1N5n531NjWIh227e9McxywT1thQJbUkBjzFCuLFYi6MtDzugChCWIRc36zy8sABQ5fWJTiDsid4z1N_28W4gwj68UpCJegE_GMu0zbsXSqoVWrNXGkYMI_IUgGJbVaKLLaWBr5KytptxqDAHaOuOb33Xj9JumuR86RnKCdptSHVOC4V2UFrpEZ1q5z3ORKCincMMpBNO9KBT4VoIalE9CVmA1zIItel5orYINyLKiHP14amBJL_Mfs7LSekMOQlQRLv_ofuxAFq0otcrPxN4xS3NJCYas9af8sxBQ13vPnKExWJO84fzEHDbrLJNow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه دو پرچم‌دار گوشی‌های تاشو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/689775" target="_blank">📅 14:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689773">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123e295506.mp4?token=ZYRRRd5mQx7oDwfX6bA2_0s8FQMqPW1-uhKTXkrSvHq1x9RVlutPqlQsWrt9G0KrVpfMWuCWyFencouTqPc_6j5CKuw3W5wAnRtDjf8ROFwzBl43UmSIRwQCryN3rtQb0Qzv2UKKoYk7tVQe2LIsIfCsqPLvTRS5pUhpm6cKmoHEyvxudKJ32LcX7227es3PZXwElXFu5txGlNMTfzvxmMYtOw_nfj6wHRMvvrZzrBwUMzKkPiGqNffgwDTqhhuUFhRrhc11JvdqGphZUh7a0OTD6nWaL3VWYUNuvTFLziZwWB4j9SsmfA-GXhpghbqgKEDwyOFItq2nex_XBMIxFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123e295506.mp4?token=ZYRRRd5mQx7oDwfX6bA2_0s8FQMqPW1-uhKTXkrSvHq1x9RVlutPqlQsWrt9G0KrVpfMWuCWyFencouTqPc_6j5CKuw3W5wAnRtDjf8ROFwzBl43UmSIRwQCryN3rtQb0Qzv2UKKoYk7tVQe2LIsIfCsqPLvTRS5pUhpm6cKmoHEyvxudKJ32LcX7227es3PZXwElXFu5txGlNMTfzvxmMYtOw_nfj6wHRMvvrZzrBwUMzKkPiGqNffgwDTqhhuUFhRrhc11JvdqGphZUh7a0OTD6nWaL3VWYUNuvTFLziZwWB4j9SsmfA-GXhpghbqgKEDwyOFItq2nex_XBMIxFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باب‌المندب؛ نقطه شکست عربستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/689773" target="_blank">📅 14:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689772">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
حضور ۲۸ میلیون ایرانی در دهک‌های پایین/ ۱۳.۶ میلیون نفر در طبقه ثروتمندان
بر اساس اعلام مرکز آمار:
🔹
جمعیت کشور: ۸۷,۰۰۰,۰۵۴ نفر
🔹
۲۸,۲۱۳,۱۴۳ نفر در دهک‌های اول تا سوم (دهک‌های پایین)
🔹
کل یارانه‌بگیران: حدود ۷۳.۴ میلیون نفر
🔹
۱۳,۶۳۵,۸۴۲ نفر از لیست یارانه‌بگیران حذف شده‌اند
🔹
جمعیت مشمول یارانه در دهک‌های چهارم تا نهم در مرداد افزایش یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/689772" target="_blank">📅 14:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689771">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0724111aa9.mp4?token=WMPw16Lik-H18XcBUzJYQ_kOCeFYESUGcCQ66FP3Ir9BgvFtPXQ8kMI2l31120NxGyg3ke5S4G9grbT4arV2GUCpcX0eRnkGZT69f8ePJyMD3VWyi0lDgEbdOS9k2qhe5n928LRbN56zhsPgwjfl8GGy1UIn-p7_1hX8liGk_ZAkhfIB1aZK7ov15iEmFFC5eJjR4wWiNzVb_FVwzzUTEOo6ApqR3G-lnOfb-vm6YoxwaJIuuASnsdKKueyQFaBUzUZsp06f7iCTN_2jPlUWSaHBeUCLThXIWcNdlEpV8CoZpQKTVo60-Umo-kAEVmSrfibwJM_ekqvp8gYrOXZ5zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0724111aa9.mp4?token=WMPw16Lik-H18XcBUzJYQ_kOCeFYESUGcCQ66FP3Ir9BgvFtPXQ8kMI2l31120NxGyg3ke5S4G9grbT4arV2GUCpcX0eRnkGZT69f8ePJyMD3VWyi0lDgEbdOS9k2qhe5n928LRbN56zhsPgwjfl8GGy1UIn-p7_1hX8liGk_ZAkhfIB1aZK7ov15iEmFFC5eJjR4wWiNzVb_FVwzzUTEOo6ApqR3G-lnOfb-vm6YoxwaJIuuASnsdKKueyQFaBUzUZsp06f7iCTN_2jPlUWSaHBeUCLThXIWcNdlEpV8CoZpQKTVo60-Umo-kAEVmSrfibwJM_ekqvp8gYrOXZ5zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: رقم کالابرگ افزایش می‌یابد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/689771" target="_blank">📅 14:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689770">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b37b3f03c9.mp4?token=SSxlZ4JXVqdycHkbr3bcodb07U0K_LA3M71nCmI5eCYjE9wXGdvhj9wgkZv3hFzq-v5iWWYZy3eRNtwD9qelJ7PdUSFnzL4DPE7oQINDscvv-YSTOh0Ef-Im4UnjM9ywefRX2skLgs_9c1gGPgEiw_01gZjceVCPejz9nR8VfUU9TFF5BeflaDXdjosa2kOem_OSMir0E8zVHH5-T3K15QDUNSgy-StVxUAkso4ctsfoDKW2qOPEpwA1c96Zo86ZMNn-aZWgKdZfnRgtM6vvUZm45naBwyHtxyed1n17djGf--cBYbUlmVRu3BYE1Oq22yRnRfnrGwQgtZpjsWdoMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b37b3f03c9.mp4?token=SSxlZ4JXVqdycHkbr3bcodb07U0K_LA3M71nCmI5eCYjE9wXGdvhj9wgkZv3hFzq-v5iWWYZy3eRNtwD9qelJ7PdUSFnzL4DPE7oQINDscvv-YSTOh0Ef-Im4UnjM9ywefRX2skLgs_9c1gGPgEiw_01gZjceVCPejz9nR8VfUU9TFF5BeflaDXdjosa2kOem_OSMir0E8zVHH5-T3K15QDUNSgy-StVxUAkso4ctsfoDKW2qOPEpwA1c96Zo86ZMNn-aZWgKdZfnRgtM6vvUZm45naBwyHtxyed1n17djGf--cBYbUlmVRu3BYE1Oq22yRnRfnrGwQgtZpjsWdoMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازنشر تصاویری از بقایای جنگنده اف۱۵ منهدم شده آمریکا توسط پدافند هوایی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/689770" target="_blank">📅 14:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689769">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMED8mKlEqXlMHMWLwfG3pqVUJ6jNPZkPABDifHXdMxam_QI7KLrSN2NDU48KiTo9KisXam5e9nk9PKFR6kLhwrvoL8mj3_Ixbjgj7EA4y2ja6csnJ1-vYH0CKjGmXDNBIjGZgdRdkoOFvzWTKmyQ4f508LBIljysRdupS6PVns47Hre5T6GqkWAAKTq7dvY_VE66U_QqUYnKYyALy4BCqWmGi0hOsIf2oxD2btJ95rtF0rDlVJuKgwydR-f1G6u3M-YMueBJKGDCd_AQrIIZyFPz70kuCgs2JzE_gDdvSbm2gKBjWmOUn2gpAVIlEatY8kSKbrPiad93CXoBu4Qng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_خودرو
| قیمت روز خودرو های بازار کشور؛ امروز ۲۳ شهریور ۱۴۰۵
🔹
بازار خودرو امروز، چرخشی محسوس را تجربه کرد و تمام مدل‌های داخلی و مونتاژی یکپارچه وارد فاز ریزش شدند.
🔹
عامل اصلی این عقب‌نشینی سراسری، افت هم‌زمان در بازارهای موازی بود که انتظارات تورمی را تعدیل کرد و زمینه را برای ریزش قیمت‌ها در بازار خودرو هموار ساخت./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/689769" target="_blank">📅 14:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689768">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b058f41b7.mp4?token=Xp4EiV8DmtHFD7WAYIQ0iqshb9NpeunXmCvb074wqChXSzKoUNJGA7M1Gvz4t5MpjL5R64bkYI15IY7Yf1jU4KPThwp7M0MjofPa8MrHljvHGxhVjDoaVLuYw4F4oi_YgWU0jBIyOfZ9MKSUNBLdj2qB2FziOJvY7La7NP4gi7wShaUDsOsFq_eDNVrb3cbrS8bQTbdGA-PqTm9i4GEp5zB7yDBXPVhLB2qf35rsbGePGibEKg1BCtSiTtKrhFsm7Y2JesoUeTaXxNM2BeXkwmhQqsHeTPHhXJFLEQTbv1WQeB9mqtsrWP_0QqXfVZ27NnjAe-Z6sL4Wf038SJhYUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b058f41b7.mp4?token=Xp4EiV8DmtHFD7WAYIQ0iqshb9NpeunXmCvb074wqChXSzKoUNJGA7M1Gvz4t5MpjL5R64bkYI15IY7Yf1jU4KPThwp7M0MjofPa8MrHljvHGxhVjDoaVLuYw4F4oi_YgWU0jBIyOfZ9MKSUNBLdj2qB2FziOJvY7La7NP4gi7wShaUDsOsFq_eDNVrb3cbrS8bQTbdGA-PqTm9i4GEp5zB7yDBXPVhLB2qf35rsbGePGibEKg1BCtSiTtKrhFsm7Y2JesoUeTaXxNM2BeXkwmhQqsHeTPHhXJFLEQTbv1WQeB9mqtsrWP_0QqXfVZ27NnjAe-Z6sL4Wf038SJhYUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آشنایی با شگفتی‌های درون آناتومی بدن انسان که شما را متحیر می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/689768" target="_blank">📅 13:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689766">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
گروسی پس از گزارش‌های یک‌سویه علیه ایران: بار دیگر دست خود را به سوی ایران دراز می‌کنیم تا برای روشن شدن مسائل مربوط به برنامه هسته‌ای با آژانس همکاری کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/689766" target="_blank">📅 13:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689763">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: آمریکا خواستار مذاکرات آتی با ایران با تمرکز بر برنامه هسته‌ای و نه تنگه هرمز است
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/689763" target="_blank">📅 13:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689762">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/db2acec3ea.mp4?token=IGwQOKOteQAvmeISguA54Ib3kQrOzr6aslsNVEtoys07TiGNBrWjc59EC7GL5ZJ75pA3h8EXHICTbG0TITLqcx7em3H9wHVI3vKKMYMPtJxOGVJs8SsSKgLQMnzzv04O_6eaepon3HzgiIo3IOxE_ReI9zwmKbATibt7ZTRC5nag1JB3VSm0YxPJvUVD8FP0tuHzq48cggzywRx4AWT7YvEjYArQ4yM9JQv93MYzba3tSK2feqs00LTdNw3PwzxbCSJtOFNq3ci5BjzzsV6YdhXqggrLC9NS99LZlhtFRAWXB78yBbRTKt4c5Ejk84EBvLzN_qcEu2KzHg6WjVZbKA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/db2acec3ea.mp4?token=IGwQOKOteQAvmeISguA54Ib3kQrOzr6aslsNVEtoys07TiGNBrWjc59EC7GL5ZJ75pA3h8EXHICTbG0TITLqcx7em3H9wHVI3vKKMYMPtJxOGVJs8SsSKgLQMnzzv04O_6eaepon3HzgiIo3IOxE_ReI9zwmKbATibt7ZTRC5nag1JB3VSm0YxPJvUVD8FP0tuHzq48cggzywRx4AWT7YvEjYArQ4yM9JQv93MYzba3tSK2feqs00LTdNw3PwzxbCSJtOFNq3ci5BjzzsV6YdhXqggrLC9NS99LZlhtFRAWXB78yBbRTKt4c5Ejk84EBvLzN_qcEu2KzHg6WjVZbKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پسر خردسال یمنی با رقص خنجر در صنعا توجه‌ها را به خود جلب کرد و لحظاتی زیبا و دیدنی را رقم زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/689762" target="_blank">📅 13:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689761">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0gBRQH7xUx2ZjV91iXoY0aIw1uxzk3x5okKHqFKq_fnKQr82-EyK9AyBaW3Oe7Br8GsgAPXDuxrIP_2-K_5zxwwE7Hwh2-TQKOBIPI_qaD1AttL2cVQwBeJVfaa2bc6PsuQ1L9lKM-sV4yDkRXg8fXOSp3YsZ97HaNminHlK2cEwAAm_oxe8lN5tfYMVzc5DQCTAo1DBy-WN_lcAccr-OV19vGr4rWlsUJwNl_W840qMmgYgfovof8vh55-cLQMcq05F0Ai65o8-jdQGtlH-lPph3Vn_Fe9OrzQDcjbqAofEYEbWiwkskzqdmX6icXMqwfS9fVfGT2J6uLYcW3R6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت آیفون‌ها در ایران؛ یک گوشی یک میلیارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/689761" target="_blank">📅 13:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689760">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6rDj0DVFPnRx3GlleUiiZk9RUnbu7YdoL7LE7TlH7pgMphHA2J2zpA0BSxFo5RHkOWyiPs-HciktkB10CzLihb51fFicZATITgX3LEOLOLpWkbiBlwP6Va2nphYdsk_x0nC_30nCXhGA6h78J2Cs6SIxSSZH967JnYUf2VizCyy9E0HvGgPt-4BYGO_OmP-kclkTFs6xcNrdcHhBMlVEh8huoo747jzwPd5u29KvV_jD1SNtgPCcNcC6nnRIrvnEZUJ5UvZ_OxEUcCx0un11IXe80fL7f3lfmpwzrVt2ioKkUAelETIgoK6Cup8GWf9l41Z05lns03rIz62NjRsnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۳ شهریور ۱۴۰۵؛ ساعت ۱۳:۱۰
🔹
دلار آزاد پس از اصلاح مقطعی، در معاملات امروز دوشنبه ۲۳ شهریور بار دیگر در مسیر صعودی قرار گرفت.
🔹
اسکناس آمریکایی با رشد قیمت نسبت به دیروز، تا رقم ۲۳۳ هزار تومان بالا آمد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/689760" target="_blank">📅 13:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689758">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
رئیس پلیس امنیت اقتصادی کشور: پلیس هزاران میلیارد تومان ارز صادراتی که در چرخه اقتصادی کشور بلوکه شده بود، را به خزانه بازگرداند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/689758" target="_blank">📅 13:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689757">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
معاون هماهنگی توزیع شرکت توانیر: در صورت رفع ناترازی برق؛ از ابتدای هفته آینده قطعی برق نخواهیم داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/689757" target="_blank">📅 13:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689756">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای بلومبرگ: دولت ترامپ از ورود رئیس سازمان انرژی اتمی ایران به کنفرانس آژانس بین‌المللی انرژی اتمی در وین جلوگیری کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/689756" target="_blank">📅 13:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689755">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkqmcZ8ayB6DNCa2-rlse9CV7Hh0FhJdRES-CdBJkRz9G-YSVE6auO3j2Uq6uOiJjg0pPbSlKgm312mm5aPJt4uykaH_uat0XsSPEI7NKltgBqArWPyTucHLc7LIKL_P4KdUyh1km9HF_gu4E8LX0iW19jUqs6CJC3zpYGFinHxKi_5MxQ7dgOIwk4l75q5aRSChAoLrcDLRUOeCLvj41x1Klqy6e8RqavBrLAc5Q973GJdT07PG4WFUtIYrNHadPsO6I7-IBNZvEhacGny3qKKDQ6bxMotdUcdLdUW5sBbgCbJb5UVxRk6XVASugmSLZWAT4wE8_thonYCHHhUtDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه در تصویر جدیدی که منتشر کرده، بقایای جنگنده F_15 را در دو فرغون ریخته است
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/689755" target="_blank">📅 13:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689751">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUQgV2vte-Kv6uICy9jcSLICENw8CfhQIKgUYLm99m-r4CtTE60hfEz3qrJ5mV8tyvrny2G7F1fvXgJzoent_J5iibnvll8WmTF-V3LkO-odMsp6ozxIgTKZry1CgtCopV2i91nnqCJVWRjxaRLAhuwLq8_63KGUZh2b_yXcpUTjg9FPhhO4Difm_pcOJ9VEsVSZ7oq65dRb2GI1ZI8tO2yPEfFCRVsNPm7eq5BqlTBBpMMledgFGEes69yrllWeiQ7FxOOiE4YmErYRmR_Rq4CHZl0OtYYhg88Yehegj_E25TX5qHuYjaLou17QjtoTxTbXshy3UIIY_oy4gnpp1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvPS0_JMj_F4PfdSIOvBP9jvh-SsgINsshJjoMWfHgSsv1w0sAXj5O95xJ1MQy_Z7CUTlWNdaVMffICBKHTTtz9Y0NuI0o4Itd0fqfRTlVCZ66HTm19mGqZV4pG1LkzimPDjkif9YeB2HGqupqUa53mwWM9DEli6gg6Sqg-V8fvMTbq8Ykk66qxyxrwal1WM8Qc_M1HtoRK5_N4IalCzel04j3sjxtn3LSSZ7_dsQLqCTuLCWyK8Qu84cNk9giMXkt29r9WFloisna5tHBn9nTyGlZ4xM1gJitY6ndePA1TWiC1-JHqsyiXYHmufkWx0Bg6nEOao9uL_AT7rcVIpuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNAIaxeY7MuVw_MLmhIClfInBFYORCRdhi1Hc5MLvRZ3YcMhQhUVi900jCevoBjIVc9UXWlg1ybcRh5kTu4RH2b1XE96rYc1ATlnIXx-8wGJDE0K1VLU701JbAk_cKXwGFviEd1OfYf2ubxwHk92cnjct0vWxYr2a-HI4wBp6MlnNJ1ztyuW5fcxYvlDn6Jnn5siUPlQtHwX-vVuY78nGyaG26LjDC0mwivf7OC2b0ECj480P3slREa2CwxoSW1sQKzH9D3vP1CPXEsRMfXcuR2A-yOTiL8ZwquqD2jHby5XF-54uf5_myNWaUWY9yUNtgcpr6ax3CCHPFkgSs2RMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_OGJQ-UdqeTwRitxhoQUDNw4jatrAsD8W3EwXN6lcS5qraTIQAB3H289wud7n2z4i00AA0XC-vODFc4A2844zZXKPU0p67P2C5UdIejRcgrelLhBrcBE4orh-u7TP0pXqYOjVEHjsh9mLqmy9kbIRc9WpYOIAmRw4hHnlgChQT0uPrFWOxPN_m3QZNGuXI6v0TJBRcOejvwVE3lFv--hh1RnUhuSSRE-SQO4piyLXP8jlB_CYdRBxSoMmK6Fq2KqafHh6fBMJ4zv1joDmWGsYRSOmb0MaPYwnb8jOGYouKDAe_5NBITERmLp6XRv7NV9TqCH0ToAL-9KaciQHW_eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بهترین زمان برای خوردن مغزیجات که شاید تا حالا نمی‌دونستی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/689751" target="_blank">📅 13:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689750">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromblu Junior</strong></div>
<div class="tg-text">🔔
الان وقت خریده
🛍
تا ۱۵ مهر اگر در بلوجونیور یک قلک به اسم
مدرسه
بسازی، حداکثر تا ۲ روز کاری بعد از ساخت قلک، اعتبار برای خرید از دیجی‌کالا برای حساب پدر یا مادرت در بلو ایجاد می‌شه.
🏧
وقتی این اعتبار رو فعال کنی می‌تونی همه‌چیز مدرسه رو
۴ قسطه
و با اعتبار بلوجونیور از دیجی‌کالا بخری.
🧡
خرید مدرسه خوش بگذره
😎
🛍
🔗
اطلاعات بیشتر</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/689750" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689749">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bad67a27.mp4?token=hsljZDUjxGS8Az4qrEIFdMPFlVe3iCtglJJz4SVt6FBdpBcJXI8H7mkAe6znRl0v2vfIdYcYp9LM7wbEZaroddyhZ7ecdaE6Mlw-Uil8dQrWFfrOEqt6UgMR98TmCu8ViEpju5FjhSZQnX4uxm7JzeAJnUajOYqDbs0C51Xfno5RubmNpuYwo01uc5FYV5Lt88pRBbDR0ooPnSqbwgeebulH2-u0nJJVLKpvEXuxgzhDeVl1HPJjCQsqAHQh62i3mQoDE5tL7r-yCeSNwTMGg6LANmo8LuUrT2AexCH263wVtrk78zoDP5ltH9WiCcWIKmBYR02DoAPGZ1bYYIYa1jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bad67a27.mp4?token=hsljZDUjxGS8Az4qrEIFdMPFlVe3iCtglJJz4SVt6FBdpBcJXI8H7mkAe6znRl0v2vfIdYcYp9LM7wbEZaroddyhZ7ecdaE6Mlw-Uil8dQrWFfrOEqt6UgMR98TmCu8ViEpju5FjhSZQnX4uxm7JzeAJnUajOYqDbs0C51Xfno5RubmNpuYwo01uc5FYV5Lt88pRBbDR0ooPnSqbwgeebulH2-u0nJJVLKpvEXuxgzhDeVl1HPJjCQsqAHQh62i3mQoDE5tL7r-yCeSNwTMGg6LANmo8LuUrT2AexCH263wVtrk78zoDP5ltH9WiCcWIKmBYR02DoAPGZ1bYYIYa1jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظی با غبارِ صنعتی؛ فولاد خوزستان چه تغییری کرد؟
🔹
یکی از چالش‌های همیشگی اهواز، نزدیکی واحدهای صنعتی به شهر بود؛ چالشی که در بادهای تند، گرد و غبار را راهی خانه‌های مردم می‌کرد. اما حالا ورق برگشته است.
🔹
پروژه «وین‌فنسینگ» فولاد خوزستان، مثل یک دیوار حفاظتی عظیم عمل می‌کند. دیواری که نه تنها ذرات معلق را مهار کرده، بلکه نمایی مدرن و فناورانه به این مجموعه داده است.
🔹
حالا دیگر تکنولوژی‌های روز دنیا، هوای شهر را بهتر از قبل نگه می‌دارند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/689749" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689748">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
وزارت امور خارجه چین ادعای ترامپ را درباره دستیابی ایران به تصاویر ماهواره‌ای از پایگاهی در اردن از طریق منابع چینی را رد کرد و آن را اتهاماتی بی‌پایه و اساس خواند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/689748" target="_blank">📅 13:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689746">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8b214b43.mp4?token=RBofX3DkHYau8jRRpwfpUtrku2J1KlnMc3e94y3ys1OvG6oNxCojWS9Idz9RzS4rVUrIPn3XAij1fZXHeJX4wrtl_bGO1OsuBtqDMOqzm3nJzoK6DmlpwqzBpoZEjuyOu_fBhoabqX8ozlOlqJvYEM2PrMctCG-e3W_K476498-lzh1ZokGq0QXK_halepP0e-TKTJ2T1RyptoiqN_CbdF7CmMi1m7Wn_qZcM4q8_Fw2hyHcrfGoKSeJAA5FhQUVADl5Zly1LpbJS4JxQ5tpU6wR0x5FomwvBdSGth4Vl-0bdJU7TMZfBu1o1ijxYu4jMGJb0ZHZ68jN5H1LotyaFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8b214b43.mp4?token=RBofX3DkHYau8jRRpwfpUtrku2J1KlnMc3e94y3ys1OvG6oNxCojWS9Idz9RzS4rVUrIPn3XAij1fZXHeJX4wrtl_bGO1OsuBtqDMOqzm3nJzoK6DmlpwqzBpoZEjuyOu_fBhoabqX8ozlOlqJvYEM2PrMctCG-e3W_K476498-lzh1ZokGq0QXK_halepP0e-TKTJ2T1RyptoiqN_CbdF7CmMi1m7Wn_qZcM4q8_Fw2hyHcrfGoKSeJAA5FhQUVADl5Zly1LpbJS4JxQ5tpU6wR0x5FomwvBdSGth4Vl-0bdJU7TMZfBu1o1ijxYu4jMGJb0ZHZ68jN5H1LotyaFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باورش سخته! واقعا چطوری یک دانشجو مشکل به اون بزرگی رو بدون هزینه حل کرد؟!
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/689746" target="_blank">📅 12:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689744">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv6-GWelQbRlYk9u3IJj3lgryNI7v61ijNnKUgPAsqvRImEROYH90l9TW_CzLbcdeJqtU-hjmNXKifX1nLlAIyMqugXbiwQFpc0HJkSsl8HQvbi1gusl1YngkG6gb1p7Agg_6uMDmkBH1XCu2FOiTSckCZNXOlRIjXmzYYpXv88HBk3oQc5WSBv-Xyh2JkhH1XI99JbhY3ihNDe84__W7nVzZObPWyHJ5oihq-oXNKD75R7X5i_RX3lT54LBLiC9jtiekbT0FjOvyNPhlygTq1G58H-MNINgosASWory4mB2aIBuODoU207EaKkMEsAVWHAFUWzEm2T441epZCMheQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو کمیسیون اقتصادی مجلس:
ممنوعیت واردات لوازم خانگی در آستانه لغو قرار دارد
حاکم ممکان، عضو کمیسیون اقتصادی مجلس:
🔹
ممنوعیت واردات چهار قلم لوازم خانگی نباید به افزایش قیمت‌ها و حذف اقشار کم‌درآمد و زوج‌های جوان از بازار این کالاها منجر شود.
🔹
در کارگروه ماده ۴ مقرر شد تولیدکنندگان بتوانند یک میلیارد و ۲۰۰ میلیون دلار قطعات مورد نیاز خود را از مسیرهای کولبری و ملوانی وارد کنند تا از تولید داخلی حمایت شود.
🔹
سالانه حدود ۵۰۰ تا ۶۰۰ میلیون دلار از چهار قلم لوازم خانگی وارد می‌شد و مقرر شد کولبران و ملوانان بتوانند معادل دو برابر این رقم کالا وارد کنند.
🔹
اگر مشخص شود تولیدکنندگان یک میلیارد و ۲۰۰ میلیون دلار قطعات مورد نیاز را از مسیرهای ملوانی و کولبری وارد نمی‌کنند، در تصمیم اتخاذشده تجدیدنظر خواهیم کرد.
🔹
در این صورت، احتمال لغو ممنوعیت واردات چهار قلم کالا و صدور مجوز واردات تا سقف ۵۰۰ تا ۶۰۰ میلیون دلار از طریق رویه‌های کولبری و ملوانی وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/689744" target="_blank">📅 12:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689743">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfGJfxUxf7e2RCwWn0DkArKFr8U1M-pg2pln7PB1asGkxsz36eUHugmfbUbYB3pIJVdahufd9O07xqlItaZ9q7gZxb3FcuxznZkwJX2nqf9Ac7fG3oQTDB6-weKT75xckSkawbnXdaT7k1uGHH-mBk2M9q0E0KT2tQEc8KFPR_UUujZfmkPaVrvAlaNUAc8_S3dlnM56WdNFITnrS19UFZr7vWHjE7lNI7qCCeZ0nOBWlbEM1AEE_NGRDOJOrUIQpwUFaZ59Dv3MW4Bggnbuccwl9Wh2a7Tvd4jD59dSFfOu7VkGdhUy4HHzzozdcbIC9wZ7uREMGCw4fPOu1Sj01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار رادان: بیرانوند شامل قانون سرباز قهرمان نمی‌شود
🔹
دروازه‌بان تراکتور از اول مهر سرباز است و باید یکی از تیم‌های ملوان یا فجرسپاسی را برای بازی انتخاب کند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/689743" target="_blank">📅 12:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689742">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8568eedd54.mp4?token=tIlR28M-C9rVkcXogZVvwhrDcgFmlM-t8lv6Q8moKYjWmIXJzzbfyDEr1FOjStCJ3Es1712T46fohuOIdMKc8hWnnmEwGPwvo5o2x5TUMbjSycCA4Uw5wxJlO5lRAaWi-C5CsC64Z-3Q7V2vlyLlOhWbcPBc95RTjNh2u25o1lLuoG6rHeqgaYIIyJRgso04FPTFnfWz2cDkJXCpKE-1LhfZPzq-3KVLVSAm25eZG5W32dS-GYHGuf0omhkStQGd3glHUkT_g62esuEnnMIiGHwfQg0kSHb-xWocIen-cYVHazQv27jh4soEu_HOGHLeQfoyHy3xPum2-as-UJDhsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8568eedd54.mp4?token=tIlR28M-C9rVkcXogZVvwhrDcgFmlM-t8lv6Q8moKYjWmIXJzzbfyDEr1FOjStCJ3Es1712T46fohuOIdMKc8hWnnmEwGPwvo5o2x5TUMbjSycCA4Uw5wxJlO5lRAaWi-C5CsC64Z-3Q7V2vlyLlOhWbcPBc95RTjNh2u25o1lLuoG6rHeqgaYIIyJRgso04FPTFnfWz2cDkJXCpKE-1LhfZPzq-3KVLVSAm25eZG5W32dS-GYHGuf0omhkStQGd3glHUkT_g62esuEnnMIiGHwfQg0kSHb-xWocIen-cYVHazQv27jh4soEu_HOGHLeQfoyHy3xPum2-as-UJDhsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهروند آمريکايی به یک نظامی این کشور: آهای، قیمت بنزین چطوره؟!
🔹
نظامی امریکایی: خیلی وحشتناکه
🔹
خب امیدوارم توی ایران کشته بشی، اونجا بدجوری قراره به حسابت برسن.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/689742" target="_blank">📅 12:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689741">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7030eb849c.mp4?token=EFAfuHnGcqZOZD5fFcvNhtu_0aDpM0aH16fM67Desb3_B8fd1wfJ-K39vYc3Q9KNWqOq5w7xlN-k8GPu6_QfOvfa14P0NU1VyXYFh9JXDuPakUerQYDKQ6YCFDyVoeO5QjycjfgpjFSPFyECxRLf6V_8yCh1De1p3dBdixmJm_VUr-ujoTNOpfzh4cTzzW1FCesvOz5kxoxRoSeG6mgrsHhJ12fvrLhYIRpuss4p2kjPxxBbZ7fPlLbA0mgoZYiV5ZP_7KTFtDNg64h1lhL8mA648QR5OyFw14an2BghRJltdAozsJLmyiIK79X5-5Sr-EuurFXwd2Eh3BxktZbiEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7030eb849c.mp4?token=EFAfuHnGcqZOZD5fFcvNhtu_0aDpM0aH16fM67Desb3_B8fd1wfJ-K39vYc3Q9KNWqOq5w7xlN-k8GPu6_QfOvfa14P0NU1VyXYFh9JXDuPakUerQYDKQ6YCFDyVoeO5QjycjfgpjFSPFyECxRLf6V_8yCh1De1p3dBdixmJm_VUr-ujoTNOpfzh4cTzzW1FCesvOz5kxoxRoSeG6mgrsHhJ12fvrLhYIRpuss4p2kjPxxBbZ7fPlLbA0mgoZYiV5ZP_7KTFtDNg64h1lhL8mA648QR5OyFw14an2BghRJltdAozsJLmyiIK79X5-5Sr-EuurFXwd2Eh3BxktZbiEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نامی عبداللهی (فرزند ناصر عبداللهی) ترانه‌ای از پدرش را بازخوانی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/689741" target="_blank">📅 12:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689740">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz0ZqQ5aiynrE0urRyvGc7CkoWfVTXAavVKlof3IoY0-We9IiT2Rw5olJGaeTgzTOAw4Zk9c9pXFSHJBdWLv62F11ljRqmQdtXQvBydtff6b0AFletuCkvaHxJHCajmndd4zJNrYl5RTU2iIDMUX8EwuLBue6H5irZtY64o7S58wb3MoRML8cjG5zvOhLxpt3Xz94cl5Mc1ZOiSvhQKyteaHPcb3LD2UKDWYhqGZgp1Jk63ZzRotzIpYAJSOpoIUpg-BK_xVKPoxNcZFXr-XG8dGT6nBclDXXFEV0osZ-8e6tSYHW6Kn6eyocX1PWC2dq0X2rkHclfQG3dAJG4dLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار نهاد مدیریت آبراه خلیج فارس به مجموعه‌های مرتبط با شناورهای متخلف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/689740" target="_blank">📅 12:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689738">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfGAhdRG1yjLJpcO_sQDfaOdvJYYCXc-3M506db8furK9NxsLzWnr1Vyj0irz9vsavLYg_TjxLamuyjBiNlShZgeKSlskogeuD4MJ_kqYh6hIP0JVefFbjxjHCyQot-RX1HwnXKCrGVAmdZYt7BH323OL81DsNEXdE9ryDA7eXfTO_F3f5LVUuMJRBQTIOm6nErR3yEuiCZy58x8wz_SGBHXwyWFefPg6jnzYpMPCLkzH-paPQWaB5fX2SSaw8jEmrHt4SNrFeOzKoBqlbJSF4wptEriQGTaWD1Uvt-X_YN9CE3sz_OnRKOhDqvnBrTqSn6KqzRVb5rShBHM5w47ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییر پنهانی مدیریت شفا دارو در آستانه واگذاری؛ چه کسی پاسخگوست؟
🔹
در اقدامی بحث‌برانگیز، سه عضو هیئت‌ مدیره شفا دارو، بدون هماهنگی با سهامدار بالادستی و ارکان بانک ملی، اقدام به برکناری مدیرعامل و تعیین سرپرست جدید کرده‌اند؛ تصمیمی که در آستانه تعیین تکلیف واگذاری شفا دارو و در شرایطی که بانک‌ها مکلف به خروج از بنگاهداری هستند، پرسش‌های جدی درباره مبنای این اقدام و انگیزه‌های پشت آن ایجاد کرده است.
🔹
این ابهامات زمانی جدی‌تر می‌شود که تصمیم‌گیرندگان این تغییر، حسب اطلاعات موجود، فاقد سابقه تخصصی و مدیریتی قابل توجه در صنعت دارو هستند و خود را به دروغ به یکی از مقامات منتصب می‌کنند. موضوعی که ضرورت ورود و شفاف‌سازی فوری سهامدار اصلی را دوچندان می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/689738" target="_blank">📅 12:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689733">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_KqgWT9mFjw0BIzzfH08odKLmulQG6Pq7pdTOLz2C6tXpEHahoD9TKKmL3JLi4SR5rsv5lUQQ9SiLt-pGPSTVg847UTo143MHdaS4N8f9FxKnYQ-acqBJ633rvHLRy9qJ85aOUGIPVVZB8AdzorzGxCeSfezVuJVPLKvEQ8gwJQW1yGisD2JDBMrQI5LGAXhYDkWuWCiRlKIcPrPe2SsRmzQ-RMy3eIJAWqnrkOo3nIl8RprPa7D-mYWnqDfOmHUIFzzJuIWdjccp0q2__d4oBIavWbgUjACt03eqUl5dwVijw8q26fRXpaA9XzEPVqDcpXzr8c2bumsmzzrl1-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtjDs7dOMjRi3PIU5pxmw1Sxy84am0Vtd2t4mlWM6-b70KGNNB40KFApGsCTo0z3JYLcJNfh32DV9_Z45RDppxsZt0KpVBF1D9vKUu446OAyE-iGA22V3rN0u3eMjxgQXnGuZJNyAi4a_X76GQjtHK6B0mCe6G7greXbIVHozAQXHc3acQum0UWjEfK8XxY0t9Z0bijer8K786HF6hOZSqJJBoBUD9DYf2aRlejerqlI6ecVPuaNZeIIngzYueftnm0WHiw-7iSSC4DnDpIB-Y_Hb9SCtKKn1RHpaHrMJJFmIORltMV4Ofm5sEafnvYCrG191JF9sXXY7QmHUSkCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZj5RuHZfanC3WXLvQPUztWXteQlc_Q6Z6RxMQK8E9qnekPQFxiVT_P2gJGkPK1GqI0u6b0xWRkRmh5vs4vWWayKiS6fJ0FFtGAqqhmlhHGLFJHL99zeD4cVXjfccPEbuRVmHmrOeULDrgAbelXCqrCUiOtmv9qj8JrgdMLjUOcnUGobmcD_tuJSoxAPYCHej41qllYuJQY2m0FhxU_SjRe_TLH0GxPpDWXUG8ZE20iNUXtDgbfJ88vB6K2Ov8sIdqXSP4oM1ljyu-ZIvEzgNxXoNESQXZlSgPF3DfwvkgL0o71bjnIJ1pO9YcIbxmpI__5wV-_HL3Je4tY0ycwRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIEQFXbqhV5gC2sj6D0eFPVvNyys5MKIGDlAllYCT3e53zfOXLm5rmz93YhJt6O4zco9-EKNhYwmIHuKcA4QK66ZGOdsTvbr4w0FBEbDIoaMVqAkqDHyp5sfGRmSVlbBWNNePok6vo1O7TRRnDHniFeGLFF-Oe9HFCG-t73I82FC9hx0Lpo6wRzqlQSBbf1P_i1jK6r5s-9vFts4WHbKzno_q3Z9cGbyNRBZNZ38jayaPzn1GFHScBGY5Aj_WWm5geJNV6gjkyerNvW9N0g8a4m_hqkumjxFy4C6eeDLJMknld1mHnHxuMdTNIPKKP1ujUcl9Wt_WSgZatkCKwanbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گزارش تفصیلی خبرگزاری قوه قضاییه درباره مجرمیت فاطمی امین و ساداتی‌نژاد وزرای دولت سیزدهم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/689733" target="_blank">📅 12:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689732">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886581420f.mp4?token=HmvFL-qThe0HCS4a5kljNyiX9WHcGhWzCgcKucPEpVXphg-7BRuMqcKIhcxjQBO4H1B1CsR7Th7UPWmx6-jA15PbN3TyLqUhiZ3y5wYpiO9X_KUZqyoAwrUuMXcZpilI1Dh4dZzva0M9vNzCiTggvJL1Q6ejq_fYflL2-Y0eQkyrwnoYN5381WF8OhSf2gLtptUIP_TFTDviLzcD7d-pUaDDIGMV_lNiieFrZG51UGB5_t1W_0scSpSWrcBlD9yIuIBgEJX9wA1H_JJIsE1CHyzn1WeojIzvy7ZBtX1W8bWhLCJ0OuKVO7wURmMGyuKMQYQWLsHXPGouWbP138il-BYzySx0LXRmf6eq77e8AUpVdFz6d9qQ56P3Ai9NXYMybaG8RkN--UM9CSfl7-O5TI2ih4ZDQAkr6MP60vDr5Y5vu6ycxr3gajDncPrIzDXQoVBNK3ndaV_JfePWe9f2hqhMePL18wvZrKnSdmF4YZCMWQyrR6nVC2wjGwHK_e8bN9azG04GzuUDEJKeWqVLfqTmYoagsooAri7-WdmI42f0QpKtPK69g3Kk77LrgJ-3VF0aLDQdtB-iXvJEoQJUuYJfBjxOdqjWjbnoF5z6KGZ3a-1MMaywWxc3cSGev1J_sTUAQwwhTNfcXs_ZiOetPZh5ZxIDV_O4VNiDUBP13aU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886581420f.mp4?token=HmvFL-qThe0HCS4a5kljNyiX9WHcGhWzCgcKucPEpVXphg-7BRuMqcKIhcxjQBO4H1B1CsR7Th7UPWmx6-jA15PbN3TyLqUhiZ3y5wYpiO9X_KUZqyoAwrUuMXcZpilI1Dh4dZzva0M9vNzCiTggvJL1Q6ejq_fYflL2-Y0eQkyrwnoYN5381WF8OhSf2gLtptUIP_TFTDviLzcD7d-pUaDDIGMV_lNiieFrZG51UGB5_t1W_0scSpSWrcBlD9yIuIBgEJX9wA1H_JJIsE1CHyzn1WeojIzvy7ZBtX1W8bWhLCJ0OuKVO7wURmMGyuKMQYQWLsHXPGouWbP138il-BYzySx0LXRmf6eq77e8AUpVdFz6d9qQ56P3Ai9NXYMybaG8RkN--UM9CSfl7-O5TI2ih4ZDQAkr6MP60vDr5Y5vu6ycxr3gajDncPrIzDXQoVBNK3ndaV_JfePWe9f2hqhMePL18wvZrKnSdmF4YZCMWQyrR6nVC2wjGwHK_e8bN9azG04GzuUDEJKeWqVLfqTmYoagsooAri7-WdmI42f0QpKtPK69g3Kk77LrgJ-3VF0aLDQdtB-iXvJEoQJUuYJfBjxOdqjWjbnoF5z6KGZ3a-1MMaywWxc3cSGev1J_sTUAQwwhTNfcXs_ZiOetPZh5ZxIDV_O4VNiDUBP13aU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا چین می‌تواند گره‌گشای تنش میان ایران و آمریکا باشد؟
مهدی خورسند، کارشناس مسائل بین‌الملل:
🔹
تنها بازیگری که در شرایط کنونی امکان میانجی‌گری مؤثر میان ایران و آمریکا را دارد، چین است.
🔹
تا زمانی که چین پای کار نیاید و این توافق را ضمانت نکند، صلحی میان ایران و آمریکا شکل نخواهد گرفت؛ چرا که هرگونه توافق بدون پشتوانه پکن پایداری لازم را ندارد./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/689732" target="_blank">📅 12:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689731">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9a835086b.mp4?token=YoLISAmlNBVCt-0TYk67E_GK4y45tESsVzo8j44laukejqV3iR38V9UdUqdmidjLgKS6pKJTZ-3KQjh2qvnGyuDGnZEi7ByS_erTlNvpDiu1E09q4nGB_Pyq-rgqyIP8KEB3H1jzksTzRiANF9zfFDL-HfrPJBdh8s8eop1U87TfeHa6uCg3mDW5wDZzSFp5W4nAIq-ESiHIl35xSoln8Gzu60PO4ybfomLLNK2i4W1e-IcrcJHICILUd0cpLn7qV-DO8Vqv9UMhGyK0QtSr3PnVs2xlVhym6QwaecGvY1ybbDIJH_LgRWdTex9ioxYYq5yo_BNthIqGpwDuEWPXQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9a835086b.mp4?token=YoLISAmlNBVCt-0TYk67E_GK4y45tESsVzo8j44laukejqV3iR38V9UdUqdmidjLgKS6pKJTZ-3KQjh2qvnGyuDGnZEi7ByS_erTlNvpDiu1E09q4nGB_Pyq-rgqyIP8KEB3H1jzksTzRiANF9zfFDL-HfrPJBdh8s8eop1U87TfeHa6uCg3mDW5wDZzSFp5W4nAIq-ESiHIl35xSoln8Gzu60PO4ybfomLLNK2i4W1e-IcrcJHICILUd0cpLn7qV-DO8Vqv9UMhGyK0QtSr3PnVs2xlVhym6QwaecGvY1ybbDIJH_LgRWdTex9ioxYYq5yo_BNthIqGpwDuEWPXQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر سرترالین مصرف کنم، بهش وابسته می‌شم؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/689731" target="_blank">📅 12:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689730">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
رسول جلیلی، عضو شورای عالی فضای مجازی: بازگشایی اینستاگرام «برخلاف عقل» است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/689730" target="_blank">📅 12:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689729">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromطلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bra5zF1ZpJYQQcLUp7bHpisPvqoBFOHiW0nPQgu-3JHehU9E4JXtMy_v9iOGbDEwQQyPK3likNojVeoblD-2gAarxijieIwXx_zQNNnCtLA8S898D7B94juSLvThtHTQ6EROcnmnoqnVNmErdqF36-mOlXnPZORRrr2Iy4gt-t0WRQFMXe6owvDZEJnPRcqFGn4N3rfba5jy1AvV-mYWHgb9KrRZeKx1FlscHR7UVae1oZS9Ffoo6FedY2kVUK4HE1veD4q7Jmc3AsUzNJzQOHM-zBX_wQnTZkPGohQsvxjFAN52WEVQNC309XNdEoEc50Wc7w6UajSfMdY-FNtxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط به طلا فکر نکن؛ این بار ممکنه خریدت تو رو به یک تویوتا کرولا برسونه.
🚗
✨
با شرکت در رقابت طلاین، شانس بردن جوایز طلایی و تویوتا رو داری.
پس ماموریتهارو انجام بده، گردونه رو بچرخون، این فرصت رو از دست نده!
وارد رقابت شو
.
👇
🆔
@taline</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/689729" target="_blank">📅 12:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689728">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_I_l3tR0i3u1hRLLudS677A4_Cf6Xm_SVHxngGmq4jhu1Afzka18_LjeuMfRO8L-ReFomrJ4mNzSIPq6rrqjMyQ02dEJlB41jzS8yWWURtwRGRZo9G9Aex5Yma_fuoaXSYpJGTwuLFKk314gv8r-LMgFb8kaXmFGDCi8ItI3fbEksyiYZhj2bIGAPAVQtApqHH7quFzRDg0G0MBiurWtmSOqA7vqhQ3T3gutbnRd_vmYzxiK9sv3p3kX2b12tVeA1N4OEQ7o2jw_qJA2vQZ8G8fqBqAiXWyc5cXrXZfAUc9DXXqm_VHe6yFrnp_pgzao1IUrHY-L-KfIzVMcamI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رویای تحصیل در خارج از کشور رو داری؟
🔻
قبولی دانشگاه، بورسیه و ویزای تحصیلی شاید پیچیده به نظر برسه؛ اما با انتخاب مسیر درست، می‌تونه خیلی ساده‌تر بشه.
🎓
🔘
در انتخاب همراهت هستیم برای:
✅
اخذ پذیرش از بهترین دانشگاه های خارج
✅
بورسیه‌های تحصیلی
✅
ویزای تحصیلی
✅
پذیرش در مقاطع کارشناسی، ارشد، رشته‌های پزشکی و دوره های زبان
✅
دوره جامع آمادگی آزمون پزشکی ایتالیا
🎯
نمی‌دونی از کجا شروع کنی؟
✉️
فرم درخواست مشاوره تخصصی رایگان رو تکمیل کن تا شرایطت رو بررسی کنیم.
🌐
فرم درخواست مشاوره:
https://ezam.entekhabafarin.com/consultant
⁠
یا با شماره های زیر با ما در ارتباط باش:
📞
۰۲۱۷۹۴۱۲
📞
۰۹۹۸۱۲۵۱۲۵۴
✅
@entekhabafarin
موسسه انتخاب | انتخاب درست، شروع یک آینده بهتر
🎓
✈️</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/689728" target="_blank">📅 12:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689723">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACrK97uVGx0fyctlyhE4WN_XThT2oY4ppnNHBHbmx3QBs14F3pbrzjPFgHALzR-Fs6OaG1lNi_XXsHoCklC_YI4KJjVwI_BgeOlBT7AT9O8WGWWnfoenDRULd4B1OuIOS-yQChYs-UqflOc4dCo7wGkjRBqLeElpk49uKKXQhn9VPmvrzK4utdC9RuSMHLb_uWBU63eIYRtUEciMuJL9paUikjialoiKy1XfNEhiH7xF8Ei1ywsO4wfnRAFA6YZ7_6mEN7ZV5wUDWUvlm5VKmur3RPozXXIwl6S34Wa608d4XDr5ECL_TWiACp5wlgXzdunCCFGVNJaTAjpwqkSP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyxHq4COUg9E4zYAG4_yauKTiTOgf89XjzFdJCXuhR9Ol8mzHkEpQkPlhKQmCngs8izf1D3p3uU6agAawXAkKK4zkknwZZxJi5k2E_o1EuZKaa-FFGPlnE-SfGerA01-RyrrLEMkLWm3KBT2Ai4CcBlAH-L4KFCnsciKLUruaeYK2OxyUEUza4BWU9NR8lAnQW4gd2XRZGtCsXy9HIswf-8fbbDaz1UlcUqRPCE8_6JSPrqV-a5_ub4kKSQyBhwTQRpaM7jdxPQTRiVtGOx76j6zSxvzMdhPioH9nrKQzPGm2OlFdYEXT_Hd9z9Z69N_jXEd_dSv28jP5u5mtR-AFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IqoyH630OUgnp5F1cSc9wFUF2CLOGOQvIFScBg15nYEdBs_BmvAfOajXn4eraOLdEPr_9F6TfFkmNPvFJo3BXPkpNv-fvoQ3vVjjRgsWpygaXtHa1eLHtVrG7rrmZgcL2Nw6SNpGo1ZGRTsINUWU6TcsT0EEozjG7kKIr4-VAI327bu1350ka3rqOnvvnxphB9ouN2o27M_reJYSFQD-DfmLVViNWWpSVJsK_sBRZax8TXaPMOicELNSX_-nRCUEx5H7InlOLbkHI0UcLUOqa2Xf7N3p_y1-vAhDPmSYxbL5GJAIg89KHJ3rhfJuWS88uRQMLB3IlLCvHu9mpBGOGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vnBumJiRVXhLapJnv0WJ0JXoVYy27M7OGXSOvdfAxk9GlmrpjCSmz1YW2570bhcl4AsSkHJQumptN_6ZxW08dXsgkajUJn6EGTHvEUKxdjtYC26F20aHLhQJeJ1sJPURDxexP6VuML2o5C_BT4QSApnU_vqp0Hh3uaSeZcjFA_6Rpc_lc0SnJeHFpEpgOD8ecGCAMdf1j4GBYp2ZYf1zBg99rOsKP6OAHTlPt77sbhSdXNb-19mfI7TyadkBojlmpx2ldf5Nui16rZxGKpxYe7x-Ko4ERW-agi2ZTArVlkEGbHbaLlRIuRIXQusXiJXrZWzLYlCWDAw5lTQEyuLr3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وقتشه که برای صبحانه، پنیر برشته اصیل گیلانی که خیلی هم خوشمزست درست کنیم  مواد لازم:
🔹
کره: به میزان لازم
🔹
پنیر لیقوان، یا تبریزی یا سیاه‌مزگی: سه قاشق غذاخوری
🔹
زردچوبه: به مقدار لازم
🔹
شوید خشک: یک قاشق غذاخوری سرخالی
🔹
تخم مرغ: ۳ الی ۴ عدد #آشپزی
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/689723" target="_blank">📅 11:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689722">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
انتصاب مخبر به‌عنوان نماینده ایران در امور چین صحت ندارد
/ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/689722" target="_blank">📅 11:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689721">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
یمن: به پایگاه هوایی ملک خالد عربستان حمله کردیم
سخنگوی نیروهای مسلح یمن:
🔹
با ده‌ها موشک و پهپاد، انبارهای هواپیما، رادارها، باندها و انبارهای مهمات را در پایگاه خمیس‌مشیط هدف قرار دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/689721" target="_blank">📅 11:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689719">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
سپاه اصفهان: احتمال شنیده‌ شدن صدای انفجار کنترل‌شده در جنوب اصفهان تا ساعت ۱۴ امروز
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/689719" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689718">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e27a9a496c.mp4?token=n8ttmOrxdtsC_mhlgvjeMpgqhIBTmkhNZAct9-tR7zp7vTqL8W5jwRvG_0p2Ido1incexMs3JVBeMUv1eTVIh-TtaL5vv84k10XhecxQRccieF8L0VISaX8pk0eRiqMp06InvFvyPz1WV0SVxDDJ-FdlIxAJeRAsj0iFsMxwGIREUvzflZfqzVZJKaBFQp4LjRlg31XiW7tgFmJ2oY6YtFrSAR5YNZjWspVNj8mhRFEKtiQ3lwBsZp_ki14AO469KKAg5v6PouT8dTHwmrP51QAjKNHT5ol6y0EuYqZQXE_nmzv_cXDEZvhkkAb1m1aNlGtjIb6HyfGaIgSaVLeA-hvCDbt7uMYtaQ4xS7gMWPXwvc_KH1eZ4HcNXSy3-Yr5PB0iIKvOovf-rugTfbovXSBnZtewIiNjPxWR2E-JMX-1A10WH1afe8MZlmAl6j9COypo8PdsPAUH_Dks0jUdsgF4fU_X735M0HzqOtR1UUE9MvGEcbK6X2ErYWlvuCoicv6xmBzc9Sq8-5Mbue2T3eBYAd-R5l4Nqvxxh1rMwofuwgvMoTFbxCCyGe1KKE4smypnFlXlagjltO5BQ9kezJC1fqohKO7rZxkln1_o0xx3g3-aMjh2H0R0ziOjwVVA9hah90ChGR6RdwHahn2FXFH_3fEiYvlH3tsDjWG5SzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e27a9a496c.mp4?token=n8ttmOrxdtsC_mhlgvjeMpgqhIBTmkhNZAct9-tR7zp7vTqL8W5jwRvG_0p2Ido1incexMs3JVBeMUv1eTVIh-TtaL5vv84k10XhecxQRccieF8L0VISaX8pk0eRiqMp06InvFvyPz1WV0SVxDDJ-FdlIxAJeRAsj0iFsMxwGIREUvzflZfqzVZJKaBFQp4LjRlg31XiW7tgFmJ2oY6YtFrSAR5YNZjWspVNj8mhRFEKtiQ3lwBsZp_ki14AO469KKAg5v6PouT8dTHwmrP51QAjKNHT5ol6y0EuYqZQXE_nmzv_cXDEZvhkkAb1m1aNlGtjIb6HyfGaIgSaVLeA-hvCDbt7uMYtaQ4xS7gMWPXwvc_KH1eZ4HcNXSy3-Yr5PB0iIKvOovf-rugTfbovXSBnZtewIiNjPxWR2E-JMX-1A10WH1afe8MZlmAl6j9COypo8PdsPAUH_Dks0jUdsgF4fU_X735M0HzqOtR1UUE9MvGEcbK6X2ErYWlvuCoicv6xmBzc9Sq8-5Mbue2T3eBYAd-R5l4Nqvxxh1rMwofuwgvMoTFbxCCyGe1KKE4smypnFlXlagjltO5BQ9kezJC1fqohKO7rZxkln1_o0xx3g3-aMjh2H0R0ziOjwVVA9hah90ChGR6RdwHahn2FXFH_3fEiYvlH3tsDjWG5SzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: عدم صدور روادید توسط اتریش نقض صریح تعهدات دولت میزبان است
🔹
سخنگوی وزارت خارجه: دیدار پزشکیان با ولی‌عهد امارات به‌ درخواست هیئت اماراتی انجام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/689718" target="_blank">📅 11:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689717">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610f6a4bcc.mp4?token=I6IiM574psYegVkFQNLblus-MKRo4KaI4wysF49YMaRZ1jKaOodpFkgnuf-9Hqkv9eFEF7cQ1KdY0oaqu1dwVoF9txLad7Y66oIh6IhZVYzsXdDnlN-1iNF5RBlQydsuywZFheSSeU6lrFrSqPGHjnXXKPqbZd5yFoCX7XanEhEAMYePM65TXTeieJqJquvHMKxd0QIJZxISSW5dZ4boUqmioAW85p5DhwPr3GMk9epGNgMolujmg3DyzAZC77_PV1lz4XQdTIeTjeT-ULS_CVXgT6rDcZSRiZISFjyQZU2Ecw0SPe_kiiB9ooO71f1p8YBrhsXZgA2-LJOO3wbnow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610f6a4bcc.mp4?token=I6IiM574psYegVkFQNLblus-MKRo4KaI4wysF49YMaRZ1jKaOodpFkgnuf-9Hqkv9eFEF7cQ1KdY0oaqu1dwVoF9txLad7Y66oIh6IhZVYzsXdDnlN-1iNF5RBlQydsuywZFheSSeU6lrFrSqPGHjnXXKPqbZd5yFoCX7XanEhEAMYePM65TXTeieJqJquvHMKxd0QIJZxISSW5dZ4boUqmioAW85p5DhwPr3GMk9epGNgMolujmg3DyzAZC77_PV1lz4XQdTIeTjeT-ULS_CVXgT6rDcZSRiZISFjyQZU2Ecw0SPe_kiiB9ooO71f1p8YBrhsXZgA2-LJOO3wbnow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: زیردریایی توقیف نشده، غنیمت گرفته شده و غنیمت هم حلال است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/689717" target="_blank">📅 11:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689714">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc9088d61.mp4?token=byWJ8gOvjVbJ6bBOk8aS4HWP9jsB4TpuVnukbd1zk1MB0TR1awy089M0gtcw_YV1RBajYzLpYvrspyoEqujiotEBQ1bUrrgjabHw9LO0JBHfvUZ2MurfCklmMz_jUmVQ7AFq9X-yXffHHychqk9zD3vI2mRFb4ceiMDJG71t1SeQzuSUQvsWo5gTA5mdxYgTCU4TF6kDOs1SJqLX93WQxa2hC4E7lqpseupHD81TityTSsRRGb41J8KsFem1eLfc0-EW0SjpNy0tRgIq0_RvWZ1jEzUYdg8RWqcYO2TTBaacO3fqoAZuobCv73qtzX98ly-AQhSIfXVVZvg1Y1W99w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc9088d61.mp4?token=byWJ8gOvjVbJ6bBOk8aS4HWP9jsB4TpuVnukbd1zk1MB0TR1awy089M0gtcw_YV1RBajYzLpYvrspyoEqujiotEBQ1bUrrgjabHw9LO0JBHfvUZ2MurfCklmMz_jUmVQ7AFq9X-yXffHHychqk9zD3vI2mRFb4ceiMDJG71t1SeQzuSUQvsWo5gTA5mdxYgTCU4TF6kDOs1SJqLX93WQxa2hC4E7lqpseupHD81TityTSsRRGb41J8KsFem1eLfc0-EW0SjpNy0tRgIq0_RvWZ1jEzUYdg8RWqcYO2TTBaacO3fqoAZuobCv73qtzX98ly-AQhSIfXVVZvg1Y1W99w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: گروسی طوری دربارهٔ تأسیسات کوه کلنگ صحبت می‌کند که انگار پروندهٔ محرمانه و جدیدی را کشف کرده!
🔹
۷ سال قبل هم مسئلهٔ بازرسی از کوه کلنگ مطرح شده بود و ما هرچقدر لازم بوده، به آژانس اطلاع‌ٰرسانی کرده‌ایم. این مکان حتی در معنای پادمانی «تأسیسات هسته‌ای» به‌حساب نمی‌آید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/689714" target="_blank">📅 11:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689713">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8b20fea9.mp4?token=nUWhbeXmVpBML0d5H8wt223cio3WKJm0ctfWqeA7rrPvfV6IkmJpMVKkDXyqypraKfbp1NgPGpKyQcHIGDXYbL9wuZ7dme_xrxc58rfKU9yZRxN_xgB9qUmkt-FrlDuW1O-XYsmcSJGsMX1LK6WGzzqXOhLRauAlN9tD4pWh-khy-cwPw7iPIY_Fzn0ZNR6vjo6nJX2LY-md2FIISY0ixoqwXNKcHh_b4ASFHH5yMD6GJvZLKYnVtHS6NkbCxhh-m6BaSKUrBDYt5yseeix6kjlSULO0op0UJDgaPVxIaspmbux00JgoNH1rUWnCj7PsJoP2z7I3FDOKm5PG6VpAoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8b20fea9.mp4?token=nUWhbeXmVpBML0d5H8wt223cio3WKJm0ctfWqeA7rrPvfV6IkmJpMVKkDXyqypraKfbp1NgPGpKyQcHIGDXYbL9wuZ7dme_xrxc58rfKU9yZRxN_xgB9qUmkt-FrlDuW1O-XYsmcSJGsMX1LK6WGzzqXOhLRauAlN9tD4pWh-khy-cwPw7iPIY_Fzn0ZNR6vjo6nJX2LY-md2FIISY0ixoqwXNKcHh_b4ASFHH5yMD6GJvZLKYnVtHS6NkbCxhh-m6BaSKUrBDYt5yseeix6kjlSULO0op0UJDgaPVxIaspmbux00JgoNH1rUWnCj7PsJoP2z7I3FDOKm5PG6VpAoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: ایران هیچ مداخله‌ای در مباحث مرتبط با یمن ندارد/ یمنی‌ها خودشان برای خودشان تصمیم می‌گیرند
🔹
بقایی: دخالت ایران در این حملات به لوله‌های نفتی عربستان را کاملا تکذیب می‌کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/689713" target="_blank">📅 11:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689712">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukRnQLoNU8oe4OK8QAyjGDf9vmw1zI1QogpmZyKi-zJrttpB5jBP698pzBBvlAoBMgjSH8bGmLq3g0BTNFbpuD2YILbRfJ7-eeuZ_vyVFW0VwuH776gGdw3vy1JkgYd5KuNvtBUcE9yeFJmG3hz_9ob1N6BSYEWpgbBZ0imlqsYvf_OxPg28kbikvUPuZGyNJOc8i7OPIwIteRyKezVHlD8ECL6RefXJhv1t2uCLKqrLHTdj-ZX8KJAK2aXwQaup_TpJBhMMspKU0SxKZwLNu1mGjuKWJvEAozaqvrdKfg24IKcKdiME1Q7cXaCuL11ivU8xzEEoCay5Xc6nEXr93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گام آخر برای احیای پل‌های محور بندرعباس - لار؛ پیشرفت ۹۳ درصدی بازسازی پل‌های کهورستان
🔹
مدیرکل راهداری و حمل‌ونقل جاده‌ای استان هرمزگان از پیشرفت ۹۳ درصدی عملیات بازسازی پل‌های کهورستان در مسیرهای رفت و برگشت محور بندرعباس - لار که در جریان حملات آمریکای جنایتکار آسیب دیده بودند، خبر داد.
🔹
عباس شرفی گفت: بازسازی این پل‌ها با بسیج ظرفیت‌های اجرایی و فعالیت بی‌وقفه ۱۴ اکیپ عملیاتی در حال انجام است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/689712" target="_blank">📅 11:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689711">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
کنترل ارتفاعات راهبردی باب المندب به دست انصارالله یمن افتاد
⁣
🔹
در ادامه پیشروی‌های منحصربه فرد نیروهای مسلح یمن، کنترل ارتفاعات مهم و راهبردی مشرف بر تنگه باب‌المندب به دست این نیروها افتاد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/689711" target="_blank">📅 11:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689710">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: عربستان درخواست کرد نشست عمان برگزار نشود/ انتظار می‌رفت کشورهای منطقه قدر این فرصت را می‌دانستند/ با دادن آدرس غلط مشکلات یمن حل نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/689710" target="_blank">📅 11:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689709">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
بقائی: تبدیل مناطق غیرنظامی به میدان آزمایش سلاح، جنایت جنگی است  سخنگوی وزارت امور خارجه:
🔹
این اقدام، با هیچ معیار انسانی سازگار نیست؛ استفاده از چنین تسلیحاتی در مناطق غیرنظامی و هدف قرار دادن ورزشگاه، منازل مردم و مراکز آموزشی، مصداق روشن جنایت جنگی است.…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/689709" target="_blank">📅 10:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689708">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3819f38b38.mp4?token=NLj5sOtpinFAqdjDQYPBHkg23_RVoPftdFdfu-wEEfm1p5uMZNqmcXXYdz2_iqBVjbWDfFVZyTlAbr9WYRlkPF6XX9GC1ASlNfz3_gsslR06TUUV-5rztMdt3nhTQmW-MaXoqGbPdz1_NUdYOhYoGD3ptAX5AibU6tD73-o-PXHT_cTqs8b4-bK2XN-fCxuwzCc5vEgi9oiFUOYoYK_ymbrxo4P3f1RbEtg9anOHROvIZx-GseIGnjq081v5WKrrXa9SbsynFIos6cK9SxM5XQ97PaE-BJgsL2JJEboY1Ll_402OYrV1OrT2qZfu49eAZuj_q6_B5HihBHJ__iB13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3819f38b38.mp4?token=NLj5sOtpinFAqdjDQYPBHkg23_RVoPftdFdfu-wEEfm1p5uMZNqmcXXYdz2_iqBVjbWDfFVZyTlAbr9WYRlkPF6XX9GC1ASlNfz3_gsslR06TUUV-5rztMdt3nhTQmW-MaXoqGbPdz1_NUdYOhYoGD3ptAX5AibU6tD73-o-PXHT_cTqs8b4-bK2XN-fCxuwzCc5vEgi9oiFUOYoYK_ymbrxo4P3f1RbEtg9anOHROvIZx-GseIGnjq081v5WKrrXa9SbsynFIos6cK9SxM5XQ97PaE-BJgsL2JJEboY1Ll_402OYrV1OrT2qZfu49eAZuj_q6_B5HihBHJ__iB13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: تبدیل مناطق غیرنظامی به میدان آزمایش سلاح، جنایت جنگی است
سخنگوی وزارت امور خارجه:
🔹
این اقدام، با هیچ معیار انسانی سازگار نیست؛ استفاده از چنین تسلیحاتی در مناطق غیرنظامی و هدف قرار دادن ورزشگاه، منازل مردم و مراکز آموزشی، مصداق روشن جنایت جنگی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/689708" target="_blank">📅 10:54 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
