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
<img src="https://cdn4.telesco.pe/file/f5CneY1ZmHC-EdsPeX0rWrP_ycM56U6emOhgrWJ81iyiKfpvkXhTPW5AssA0okJxzriOgEhJa8_Q9ydaKXI0Gvla0k9UZUpd4lKqf470xkmVXNJqsVCze1jlmzBfT4obc3T04OFbsEhkUFTbLbHfAD3AHLWqTqa7KbIqAbsAYaFUTcLEWqdWWElMEkT-aMKxK_QkLiP9Oq3Q_qaJCgAhZs1kMVULObJofL7djf3-N8fEEqIsbFIzrkESQhw4DhRwRVDJLvQfDcEJ2MPKFDYlFIdKNQjZFZmc2UJToGPON2biXS31jFbk48Eccy9cHsgfRXTAQiQGFwHcBz1RM9gzXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 260K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 20:37:23</div>
<hr>

<div class="tg-post" id="msg-11302">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/11302" target="_blank">📅 20:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11301">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsi</strong></div>
<div class="tg-text">یاشار بیا مثل سیاه جامگان یا حسن صباح یه فرقه راه بنداز
😅</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/withyashar/11301" target="_blank">📅 20:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11300">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اخرش مجبور به همین کار میشیم
🫤</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/withyashar/11300" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11299">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr.Moradi</strong></div>
<div class="tg-text">یاشار خودت یه فراخوان بده بزنیم کارو تموم کنیم
😂
🤦‍♂
‌ دیگه نمیکشیم</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/withyashar/11299" target="_blank">📅 20:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11297">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بیداریم مثل پلنگ
😾
💪🏾</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/withyashar/11297" target="_blank">📅 20:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11296">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParsa • PERSIAN</strong></div>
<div class="tg-text">درود فرمانده یاشار
فرمانده نظری برای امشب تا وقتی بازار های مالی باز میشه داری ؟</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/withyashar/11296" target="_blank">📅 20:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11295">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSxF2zeNbkndB8zYMP72vZKX3wf6uvSnBe1ua4ae9tGICJG-X993WlrWhwYb0SAEp27VF6A531hpamXMXyAoNw46E6Qlp0J82bu2axOKlxA3sel-CnDRgT5ZjOv_ZrjZQ6huwpFkYFACeDSEO71H8AGim7as1kF_opf0Zmp635z08lHkOYCjwOEbUOQU8TAZcHLbRNeHxzGHoqfVt6mFwtaY_2rwiMgTN_3Imh3nd1n8NM5zzMskvWSt126X9NSXOZ2dZC2EPCslIf-Ehyg2z-B6ECiGV3NT_1dA9BWYvB0c0DwRRlbdm8wvUT2RYeedDQq89uSQJnjPC9NOS1xG-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پهپاد اسرائیلی مناره مسجدی در محله المحطه در خان یونس در جنوب غزه را هدف قرار داد.
@withyashar</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/withyashar/11295" target="_blank">📅 20:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11294">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزیر خارجه چین:
رئیس‌جمهور شی جین‌پینگ طبق دعوت ترامپ در پاییز به آمریکا سفر خواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/withyashar/11294" target="_blank">📅 19:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11293">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">طبق گزارش خبرنگار همراه هیئت آمریکایی، پیش از سوار شدن به «ایرفورس وان»، کارکنان آمریکایی تمام وسایل و ههدایایی را که طرف چینی داده بود از جمله کارت‌ها، نشان‌ها، تلفن‌های موقت و اقلام هدیه جمع کردند و داخل سطل زباله انداختند و اجازه ندادند چیزی از چین وارد هواپیما شود.
@withyashar</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/withyashar/11293" target="_blank">📅 18:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11292">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وزیر نیروهای مسلح فرانسه: ناو هواپیمابر «شارل دوگل» در دریای عرب مستقر شده و ماموریت آن «دفاعی» است.
@withyashar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/11292" target="_blank">📅 18:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11291">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e37fa8adaa.mp4?token=MNkJjvAUdobrPP2sa3GSg9TWKz9EhmlKLYqeKBbJZ2-sHCdcBDvwKdfLcIxQosFzUXnHg-fmQVnHsyMVgj2fGtl2Ib6dgB6wNWJ9dunMXPHlaepSuniLq2kW1_4CvTxeSMWbRaqzLb4v1iidC_wVs-eaO5JpdNhTwS7KDGUe1YP6AWRQnDYZMVDr0ZzN_tzI1wKVWhAjlBHEXgVlcn75V8K1ZazmRpSHjQscJ8dLc0EAtFyY3yebniLz5xAEMjW2GbPdpg8bGtpwomkajF4y55vChx_OWxbpN28ISQIVUUq1U_MMnp9Cjl5h6U3GU7j56CGqD2n4R4s01ij9xKSvwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e37fa8adaa.mp4?token=MNkJjvAUdobrPP2sa3GSg9TWKz9EhmlKLYqeKBbJZ2-sHCdcBDvwKdfLcIxQosFzUXnHg-fmQVnHsyMVgj2fGtl2Ib6dgB6wNWJ9dunMXPHlaepSuniLq2kW1_4CvTxeSMWbRaqzLb4v1iidC_wVs-eaO5JpdNhTwS7KDGUe1YP6AWRQnDYZMVDr0ZzN_tzI1wKVWhAjlBHEXgVlcn75V8K1ZazmRpSHjQscJ8dLc0EAtFyY3yebniLz5xAEMjW2GbPdpg8bGtpwomkajF4y55vChx_OWxbpN28ISQIVUUq1U_MMnp9Cjl5h6U3GU7j56CGqD2n4R4s01ij9xKSvwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: دیروز از دریادار کوپر درباره حمله به مدرسه دخترانه(میناب)در روز اول جنگ سؤال شد.
ترامپ:  منظورتون همون حمله اولیه‌ست؟ اون موضوع هنوز تحت تحقیق قرار داره.
خبرنگار: می‌تونید تأیید کنید که موشک آمریکایی بوده؟
ترامپ: شما از کدوم رسانه‌ای هستید؟
خبرنگار: بی‌بی‌سی.
ترامپ: بی‌بی‌سی فیکه با من حرف نزن.
@withyashar</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/11291" target="_blank">📅 16:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11290">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc3a3a9b4.mp4?token=nwLzFS6H-Lf9MOGh_FrJ6nL0vg6Qn2mySRouTpx0NTdWXJ7Ex4Wlq4kJBxGwnddJjtSAUp_2TQ2M_bmf9yHzq9H4xCOJ7C4Sqy9eQSRtEyEXQP7kfHN21UBFn5cDzCJijj56824oX7mCl4wtzAMI8p2YGc6gJlNSgChTnvqvZMPCT92edo5re0AVRGu9Jc8lnK3vYSbMkAN7fb7ZXiBD0YDaPiWsETg31wsBTmyl--cOF2niWW53Vy20hMseWbziDekUuanuFt9IgYsDMMpgTQDe4gTysgoQI69wCun5vQ6gHCNWJfdjscB1pUrBS_M4_EpM_JB9ILpUcZx1ttI8Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc3a3a9b4.mp4?token=nwLzFS6H-Lf9MOGh_FrJ6nL0vg6Qn2mySRouTpx0NTdWXJ7Ex4Wlq4kJBxGwnddJjtSAUp_2TQ2M_bmf9yHzq9H4xCOJ7C4Sqy9eQSRtEyEXQP7kfHN21UBFn5cDzCJijj56824oX7mCl4wtzAMI8p2YGc6gJlNSgChTnvqvZMPCT92edo5re0AVRGu9Jc8lnK3vYSbMkAN7fb7ZXiBD0YDaPiWsETg31wsBTmyl--cOF2niWW53Vy20hMseWbziDekUuanuFt9IgYsDMMpgTQDe4gTysgoQI69wCun5vQ6gHCNWJfdjscB1pUrBS_M4_EpM_JB9ILpUcZx1ttI8Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
@withyashar</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/11290" target="_blank">📅 15:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11289">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238609fcd8.mp4?token=XMi7pehevpegMHZSP6wTfhAon1qrjk6n_1Ktfg-BV_uLNuD4C6GQYF93Uv571ltK4ZnFUJ3f4uAu2LbA90238Wc9R6YwAZwYf6Ox8jfNEkPmFqTuVhAGCgISF7nHDOPMbN47ZwwCVJ06T4pV5p4asO8uze63UQ3-usOc12KowbEZHUBDdWVtQy8fVUp-tZqxFAjWc-skIMe96VgGriIdqKUtJCyoqvVGLYBtRee-lyojJIsnCSnJPBmUadpGW9NXspm612ql_fFZykNl30H5eHmDtxYbKnwmcrc9xoY9ajgBoQLZtbFQgmftQ3cZzwDE4i6PRm9UCNX1tZVIFlSlnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238609fcd8.mp4?token=XMi7pehevpegMHZSP6wTfhAon1qrjk6n_1Ktfg-BV_uLNuD4C6GQYF93Uv571ltK4ZnFUJ3f4uAu2LbA90238Wc9R6YwAZwYf6Ox8jfNEkPmFqTuVhAGCgISF7nHDOPMbN47ZwwCVJ06T4pV5p4asO8uze63UQ3-usOc12KowbEZHUBDdWVtQy8fVUp-tZqxFAjWc-skIMe96VgGriIdqKUtJCyoqvVGLYBtRee-lyojJIsnCSnJPBmUadpGW9NXspm612ql_fFZykNl30H5eHmDtxYbKnwmcrc9xoY9ajgBoQLZtbFQgmftQ3cZzwDE4i6PRm9UCNX1tZVIFlSlnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 25 اردیبهشت روز پاسداشت زبان فارسی و بزرگداشت فردوسیه
@withyashar</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/11289" target="_blank">📅 15:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11288">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4486529b5a.mp4?token=uy2xKt02W_WhIxBpmPwNcrKPHjlpkTCk-x5hq8MVrmgYW-h_GguGKkVZ5v2g7i_9mV0celcgFUX6ILMSkex4EtpItTwuf_tKDT4wbIKunF6mBBKKJeXc6xHik4H-PRTyeaO7kncPSmlx86I3JCtLyeVp_fEeN7C1dW_yUvZjN3-6CXcWsHKiLFF5Dx0VTnpspeWrDosCqHX4V8IZgEZbVj8hNP20rtSJI80fCq4CAhr3fU2eDtvsGciH_am6X6GYwBzyFFq8wW9BDw5HOyKDyRewfWqu91Lwxxbbdrf6O62U9L8xDgZVJSiaVZOBZAABuFGQ21mTeaARJDCbYl-ZsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4486529b5a.mp4?token=uy2xKt02W_WhIxBpmPwNcrKPHjlpkTCk-x5hq8MVrmgYW-h_GguGKkVZ5v2g7i_9mV0celcgFUX6ILMSkex4EtpItTwuf_tKDT4wbIKunF6mBBKKJeXc6xHik4H-PRTyeaO7kncPSmlx86I3JCtLyeVp_fEeN7C1dW_yUvZjN3-6CXcWsHKiLFF5Dx0VTnpspeWrDosCqHX4V8IZgEZbVj8hNP20rtSJI80fCq4CAhr3fU2eDtvsGciH_am6X6GYwBzyFFq8wW9BDw5HOyKDyRewfWqu91Lwxxbbdrf6O62U9L8xDgZVJSiaVZOBZAABuFGQ21mTeaARJDCbYl-ZsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روانه شدن نفت در سواحل جزایر خلیج فارس جمهموری اسلامی داره نفتو تو دریا میریزه و جان موجودات دریایی و زیست بوم ها رو به خطر انداخته
@withyashar</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/withyashar/11288" target="_blank">📅 15:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11287">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27bba1486b.mp4?token=pLnDaFr-3feCYO_irtXUm_BfPj2T6Ymm1O4rAuCttedNCHqFzYY0-Qi8OgjYjNTEfHSZm1V-mXYEN_y0PPnJDGUJUcjihgIKplJiryydreIWQ5eeVqpTGqGC-dBnq7q_-6N3TK0jNcRxWiWTZujMr8DOs1Do9gWGbvzByYeM2gh1dY99KEiCw052G5l-v5xYN9c-ysF3IkLCc7Bdqsduf6zyFZdQTR2Qv4H7dg059jADLTsJwqP5Z_z3zVQPBroqDJDZWhCNinBUMsIT3dcxE8P7yIUUyxfqgLflP67fnThxhDcpNUVxxjL65O9ctdWQcy_1astjEBvWxoHnPh-SIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27bba1486b.mp4?token=pLnDaFr-3feCYO_irtXUm_BfPj2T6Ymm1O4rAuCttedNCHqFzYY0-Qi8OgjYjNTEfHSZm1V-mXYEN_y0PPnJDGUJUcjihgIKplJiryydreIWQ5eeVqpTGqGC-dBnq7q_-6N3TK0jNcRxWiWTZujMr8DOs1Do9gWGbvzByYeM2gh1dY99KEiCw052G5l-v5xYN9c-ysF3IkLCc7Bdqsduf6zyFZdQTR2Qv4H7dg059jADLTsJwqP5Z_z3zVQPBroqDJDZWhCNinBUMsIT3dcxE8P7yIUUyxfqgLflP67fnThxhDcpNUVxxjL65O9ctdWQcy_1astjEBvWxoHnPh-SIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداسیما : نتانیاهو نه خسته شده نه عقب میخواد بکشه بنظرم واقعا مَرده واقعا مَرده و میخواد ایرانو
از 100 درصد به 20 درصد برسونه
همین الانم اماده ترین عنصر برای
حمله به ایران؛ اسرائیله
نتانیاهو نه کم آورده نه علائمی از خستگی داره نه پشیمانه
@withyashar</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/11287" target="_blank">📅 14:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11286">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ به فاکس‌نیوز: ما می‌توانستیم پل‌ها و شبکه‌های برق ایران را نابود کنیم و می‌توانیم ظرف دو روز همه چیز را در آنجا از بین ببریم.
@withyashar</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/withyashar/11286" target="_blank">📅 14:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11285">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : ما ارتش ایران را نابود کرده‌ایم و شاید باید یک پاکسازی سبک انجام دهیم.
میتوانیم نیروگاه‌های ایران را تنها در دو روز از بین ببریم
اگر ایران اورانیوم های غنی شده خودش رو تحویل نده وارد ایران میشیم
@withyashar</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/withyashar/11285" target="_blank">📅 14:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11284">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/withyashar/11284" target="_blank">📅 14:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11283">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromJvd</strong></div>
<div class="tg-text">مارو به قاهره میبره؟
خب پس بذار هرچی میخواد بگه</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/withyashar/11283" target="_blank">📅 14:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11282">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ به فاکس‌نیوز:
پیشنهاد ایرانیا که برام رسید همون‌ جمله ی اول متنشونو که خوندم برام قابل قبول نبود و سریع ردش کردم
@withyashar</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/11282" target="_blank">📅 14:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11281">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df234526d.mp4?token=O_2xlkyPdLHSXgujYu1iKbtIgjz7DzMuOb-N6mir_NfdfjJbMrs8eq1EQ5LWAda963P6OJBDK_czB-Rd_fafLMYvk8HHi7tdXfRnS753Ys26FU_kivS0Yf8KsZ100atpBP-GoZia6-rjQYtP_xgjoiIiKdpzw6hLSQuIzGFJvVY_Dqh-axI6NX2r1_r8_DbEepXgfkKnGJvWnoc5G4x5THc_Yuvk-IvOpQxYm700VqqEE-BvqN_jm3mxBpObf-K1ZWBeXuoZrDpqwzz3GbdpuAvqQNwnNVj4oX_9_9E41WPrVbv7LoOw_sDLNXcXClrGPlhdTipOEH2dg_aCnHRqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df234526d.mp4?token=O_2xlkyPdLHSXgujYu1iKbtIgjz7DzMuOb-N6mir_NfdfjJbMrs8eq1EQ5LWAda963P6OJBDK_czB-Rd_fafLMYvk8HHi7tdXfRnS753Ys26FU_kivS0Yf8KsZ100atpBP-GoZia6-rjQYtP_xgjoiIiKdpzw6hLSQuIzGFJvVY_Dqh-axI6NX2r1_r8_DbEepXgfkKnGJvWnoc5G4x5THc_Yuvk-IvOpQxYm700VqqEE-BvqN_jm3mxBpObf-K1ZWBeXuoZrDpqwzz3GbdpuAvqQNwnNVj4oX_9_9E41WPrVbv7LoOw_sDLNXcXClrGPlhdTipOEH2dg_aCnHRqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز اعلام کرد که ممکن است توقف ۲۰ سالهٔ فعالیت هسته‌ای ایران را بپذیرد.
ترامپ:“بیست سال کافی است. اما میزان تضمینی که از طرف آن‌ها می‌گیریم… باید واقعاً یک بیست سالِ واقعی باشد.”»
@withyashar</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/11281" target="_blank">📅 14:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11280">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ وسط‌ پرواز به فاکس‌نیوز : «من دیگر خیلی بیشتر از این صبر نخواهم کرد. آنها باید توافق را امضا کنند.»
«مواد هسته‌ای» ایران، ممکنه به چین یا آمریکا تحویل داده شه!
@withyashar</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/withyashar/11280" target="_blank">📅 14:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11279">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز :
اما در نهایت فکر می‌کنم الان آخرین چیزی که دنیا نیاز دارد جنگ است، مخصوصاً جنگی که هزاران کیلومتر دورتر است.
شی درباره مسائل مختلفی مثل ، حملات سایبری و جاسوسی صحبت کرد. گفت هم آن‌ها جاسوسی می‌کنند و هم ما. این یک واقعیت است و همه این کار را انجام می‌دهند، اما معمولاً درباره‌اش صحبت نمی‌شود.
او گفت آمریکا در چین جاسوسی می‌کند. من گفتم ما هم همین کار را انجام می‌دهیم. این یک واقعیت است و مسئله‌ای است که همه طرف‌ها درگیر آن هستند
@withyashar</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/11279" target="_blank">📅 14:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11278">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز :
شین گفت برخورد شما قوی‌تر از قبل بوده، چون ما با انها(حکومت ایران) رابطه داریم و ما درباره این موضوع صحبت کردیم. من گفتم این مثل جنگ است و حق با من بود. موضوع قدرت بود و همه با آن درگیر شدیم. این موضوع روی رابطه ما تأثیر گذاشت، اما قبل و بعد از آن رابطه خوبی داشتیم و الان هم رابطه‌مان قوی است. حتی به جایی رفتم که او زندگی می‌کند، که اتفاق نادری است. با هم ناهار خوردیم و درک خوبی بین ما وجود دارد. فکر می‌کنم او معتقد است اتفاقات مثبتی بین دو کشور در حال رخ دادن است
@withyashar</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/withyashar/11278" target="_blank">📅 14:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11277">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز :
نیویورک تایمز هم گزارش‌هایی داده بود درباره تحریم شرکت‌های چینی که نفت ایران می‌خرند. درباره آن صحبت کردیم و بعداً هم صحبت خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/11277" target="_blank">📅 14:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11276">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ وسط پرواز به فاکس نیوز : شین گفته جنگ باید متوقف شود. من چنین حرفی نمی‌زنم. فکر می‌کنم او آدم خوبی است، اما از بعضی حرف‌هایش خوشم نیامد. مثلاً گفته کشتی‌ها باید بعد از پایان کار نفت متوقف شوند. ما هم از نظر نظامی تقریباً کار را تمام کرده‌ایم، اما هنوز کامل نشده است.
ما حدود ۷۰ تا ۷۵ درصد کار را انجام داده‌ایم، نه همه‌اش را.
برمی‌گردیم و بقیه را هم تمام می‌کنیم
. بعضی بخش‌ها هنوز باقی مانده است. توان موشکی و پرتابگرهای موشک هنوز به طور کامل از بین نرفته‌اند، هرچند گفته می‌شود حدود ۸۰ درصد آن‌ها نابود شده است. تولید موشک هم بیشتر آن از بین رفته است
@withyashar</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/11276" target="_blank">📅 14:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11275">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/withyashar/11275" target="_blank">📅 13:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11274">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبرنگار الجزیره:
تهران به‌طور رسمی پاسخ واشنگتن به پیشنهاد خود را دریافت کرده و ایالات متحده تمامی شروط ایران رو رد کرده.
@withyashar</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/withyashar/11274" target="_blank">📅 12:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11273">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">😂
😂
🙌🏾
@withyashar</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/11273" target="_blank">📅 12:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11272">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ در تروث : پژوهشگر چینی به CNN گفت که به نشست ترامپ و شی نمره «۹.۹۹ از ۱۰» می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/11272" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11271">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEONf_M-WuYrVL32B2UDArWZOalfqpKb0EAS42fXbAUbCkW9jBq07W6XoTLIR6QiTXMSDmVG9mZOp9aBJDg7RL4elZQpoz5wu4G9YT24ClwN3ycN-8hWhfY_B8hA5Pr6SBHl_anrg8RfVRx2m_QQnjtrNyEtRMXXBw28UB-A2-HTjbbyhoi9i_bIbH4Of08x0ojYMFZyo02J58zWj7y094Ovt3n2gh9wOTIEMmCid_1tyjOun7o2_GUJVfSsaCyUEFkwmNILGTXwXVAlnBf5eAsAeXDbQPNdhH9AoNrh8iW6V1qq2-F9yyfI72BKePKzjQQ3T64Mx-nsSqsLuVV0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد قنطاری، کاردار جدید سوریه در واشنگتن دی سی
😬
🍔
@withyashar</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/11271" target="_blank">📅 12:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11270">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">@withyashar
part3</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/11270" target="_blank">📅 12:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11269">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veQjoz8CJqAJQJO0lrU12Ge8qWVEheeEUhBKU3Sswi7qBt8CiRWlvcOiYrQgWB_4Z8Tbt5k97wkysAVgzs1dtLOaJ4rUwWav3nqh4KIoNTdI8zsBVFa-h4A8P1QwnJH7_tgB7ekhQei9-dFOwTrTZ0I1SSqRriH-z00SgldeHY3XVAU-eZ9gJMchW4afRtwLuGioyp5tY29iY_5_2yT5QNYB3ypVfjSVtI0IRQ05bG6iA6MTqTuXRkVO9-6AODLjd-5aBK0dj_eZevNmwUkj48_rLLRmnqgq6HaAtsN5CkhJZqexk97dTa6LrQB1Pi0m-vqsRhDcykVgvgfzUFcJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
🙌🏾
@withyashar</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/11269" target="_blank">📅 12:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11268">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هم‌اکنون حمله سنگین جمهوری اسلامی به مقر گروه های مخالف در عراق
@withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/11268" target="_blank">📅 11:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11267">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">طبق گزارش روزنامه «ساوت چاینا مورنینگ پست» و بازنشر آن توسط «بلومبرگ»، انتظار می‌رود «ولادیمیر پوتین» در حدود ۲۰ مه به «پکن» سفر کند؛ تنها حدود ۵ روز پس از دیدار «شی جین‌پینگ» و «دونالد ترامپ» در پکن.
رسانه‌ها می‌گویند این سفر احتمالاً فقط یک روز طول می‌کشد و بیشتر در قالب یک دیدار کاری و هماهنگی سیاسی انجام می‌شود. همچنین برخلاف سفر ترامپ، ظاهراً خبری از تشریفات بزرگ، رژه رسمی یا استقبال بسیار گسترده نخواهد بود و این سفر در سطحی ساده‌تر و کم‌نمایش‌تر برگزار می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/withyashar/11267" target="_blank">📅 11:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11266">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">@withyashar
part2</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/11266" target="_blank">📅 11:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11265">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ در تروث : «وقتی رئیس‌جمهور شی با بیانی بسیار سنجیده از ایالات متحده به‌عنوان کشوری که شاید در حال افول باشد یاد کرد، منظور او آسیب عظیمی بود که ما در چهار سال دوران جو بایدنِ خواب‌آلود و دولت بایدن متحمل شدیم؛ و در این مورد، او صددرصد درست می‌گفت.  کشور…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/11265" target="_blank">📅 11:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11264">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">@withyashar
part1</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/11264" target="_blank">📅 10:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11263">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76eba2226.mp4?token=Ih9AObi2nU2uZD_47cidRudDuIrfNIpoB5hoSmj-FdOxBWdtVvP0LDdqzdyueXSKgAhB0gq55kJmUPbEcY6_HZsInnkiILRPnjaVpOxTxkyw3E-CVrIfCeG3ODGiCzYFhkUDRi4q6Qkf66f_MlZaqOS2d5FQH1Bjty4zW_K_JAaz2ZpBh0TBLJNT4er2moYLizzzfGBS0LOCwsWztJ7YV0ZP74wVIRn0S7Ttn4M_OG9SxVSQzvohnKCKOhGaxyKYxsNPDDpNOnEl4ZKkCR3dwe_LnQ_EcUcZSa2H85DAMt88lp7OuHE9-Co6rHdR-kmejW5qChVjhWZTyGtmARkxcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76eba2226.mp4?token=Ih9AObi2nU2uZD_47cidRudDuIrfNIpoB5hoSmj-FdOxBWdtVvP0LDdqzdyueXSKgAhB0gq55kJmUPbEcY6_HZsInnkiILRPnjaVpOxTxkyw3E-CVrIfCeG3ODGiCzYFhkUDRi4q6Qkf66f_MlZaqOS2d5FQH1Bjty4zW_K_JAaz2ZpBh0TBLJNT4er2moYLizzzfGBS0LOCwsWztJ7YV0ZP74wVIRn0S7Ttn4M_OG9SxVSQzvohnKCKOhGaxyKYxsNPDDpNOnEl4ZKkCR3dwe_LnQ_EcUcZSa2H85DAMt88lp7OuHE9-Co6rHdR-kmejW5qChVjhWZTyGtmARkxcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
منتظر ری اکشننن</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/11263" target="_blank">📅 10:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11262">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromayoub</strong></div>
<div class="tg-text">نظرت چیه؟قبل جام جهانی میزنع یا بعد؟</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/11262" target="_blank">📅 10:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11261">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال 13 اسرائیل:اسرائیل انتظار دارد حمله احتمالی آمریکا در ایران از فردا با بازگشت ترامپ از چین آغاز شود
@withyashar</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/11261" target="_blank">📅 10:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11260">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9469892534.mp4?token=P_5M7TwDuV4n_r2zF4YUzUAkvxF2dEPJ9hd0XdG3kfhtRki3ev9TxS1z9RgOrPGtfiJSQTGLiczuRQG1rmFioWjEr66kmFGK6AvG-nEUQdno59kKgiU_E-a2GxEoIE1tt0skbAzsGkVZJSn0MxiLFuX5ZFe9kDavevBg4zSIPBz9Vb74mmZf4bcNtqhobWkX1Pj8Od5Bw7OvP05Q5SspT81uD0Xo6cwyRygbAyVE_JsDSxPe2fFj5cO0hv7mCKs8oT-Tk9AGzEKLwn8pPGofFYmNf5olah3tbpE_Jh3qqP09r87Pp0uYSK2YiCHYvnDUui24RKZYuds2R83pP0CdpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9469892534.mp4?token=P_5M7TwDuV4n_r2zF4YUzUAkvxF2dEPJ9hd0XdG3kfhtRki3ev9TxS1z9RgOrPGtfiJSQTGLiczuRQG1rmFioWjEr66kmFGK6AvG-nEUQdno59kKgiU_E-a2GxEoIE1tt0skbAzsGkVZJSn0MxiLFuX5ZFe9kDavevBg4zSIPBz9Vb74mmZf4bcNtqhobWkX1Pj8Od5Bw7OvP05Q5SspT81uD0Xo6cwyRygbAyVE_JsDSxPe2fFj5cO0hv7mCKs8oT-Tk9AGzEKLwn8pPGofFYmNf5olah3tbpE_Jh3qqP09r87Pp0uYSK2YiCHYvnDUui24RKZYuds2R83pP0CdpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان سفر ترامپ به چین
دونالد ترامپ، رئیس جمهور آمریکا، پکن را ترک کرد و سفر خود به جمهوری خلق چین را به پایان رساند.
شی جین‌پینگ، رئیس‌جمهور چین در آخرین روز سفر رئیس جمهور ایالات متحده گفت که دونالد ترامپ به دنبال بازگرداندن عظمت آمریکا است و او نیز متعهد به هدایت مردم چین برای تحقق رستاخیز ملی است.
شی جین‌پینگ همچنین تأکید کرده است که چین و آمریکا می‌توانند از طریق تقویت همکاری‌ها، روند توسعه و پیشرفت خود را تسریع کنند.
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/11260" target="_blank">📅 10:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11259">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1169f33889.mp4?token=fD4qi8aVVKJSMeXHbr0Rd79XoTxG_ngkbHtOBhXfNEH6I1KkZuFUpHolbZcRNjQlBimldOudbIgOyK9CNHEpFDk7fUH4gQQxUB9J7RcO7PCA-LLX13oMZ58TdPpXChv-RWo2ET8Qa5QkDNaxVRHm58zosqjBR6o2J9b38b3ouhUtOndhTehRXrKIhU7C17aVteHYCsoWYiRugLcqBF0wrgZBL79zY4Y-F7cUl3UwzeExjCfeS-MViOphRL5siouOkUT2SkfztpYIi0xe6pTjVf0Np3kqw3lKPvwYhlQ2B_mubXWwnot12Ms9L7JSGuWTpIfRRfzBMF90od_khHIuYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1169f33889.mp4?token=fD4qi8aVVKJSMeXHbr0Rd79XoTxG_ngkbHtOBhXfNEH6I1KkZuFUpHolbZcRNjQlBimldOudbIgOyK9CNHEpFDk7fUH4gQQxUB9J7RcO7PCA-LLX13oMZ58TdPpXChv-RWo2ET8Qa5QkDNaxVRHm58zosqjBR6o2J9b38b3ouhUtOndhTehRXrKIhU7C17aVteHYCsoWYiRugLcqBF0wrgZBL79zY4Y-F7cUl3UwzeExjCfeS-MViOphRL5siouOkUT2SkfztpYIi0xe6pTjVf0Np3kqw3lKPvwYhlQ2B_mubXWwnot12Ms9L7JSGuWTpIfRRfzBMF90od_khHIuYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیدوارم ایران تماشا کند. ما دقیقاً می‌دانیم چه چیزی را آماده کرده‌اند. می‌دانید، آن‌ها کمی استراحت داشتند، بنابراین سعی دارند چند چیز را با هم جمع کنند. آن‌ها موشک‌هایی را از زیر زمین بیرون آورده‌اند. همه این‌ها در یک روز از بین خواهند رفت. امیدوارم این رو ببینند چون همه کارهایی که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت.
@withyashar
یاشار:خوب دیگه رسمأ داره میگه جنگ میشه و هم داره میگه حمله خیلی سریع و محکم انجام میشه همانطور که گفتیم</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/11259" target="_blank">📅 10:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11258">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آمریکا پیشنهاد ۱۴ ماده‌ای ایران را رد کرد
طبق اطلاعات رسیده به تهران تایمز، دولت آمریکا پاسخ پیشنهاد مکتوب ایران درباره پایان جنگ را داده است.
گفتنی است ایران پیشنهاد خود را مبتنی بر مذاکرات دو مرحله ای ارائه کرده بود که در مرحله اول منجر به پایان جنگ در همه جبهه ها شده و در صورت تحقق شروط ایران، مرحله دوم مذاکرات که درباره موضوع هسته ای بود، آغاز می شد
@withyashar</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/11258" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11257">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مجلس نمایندگان آمریکا برای سومین بار طرح دموکرات‌ها جهت محدود کردن اختیارات نظامی ترامپ علیه جمهوری اسلامی رو رد کرد.
این طرح با نتیجه ۲۱۲ در برابر ۲۱۲ به تساوی رسید و در نهایت با اختلاف یک رای شکست خورد.
@withyashar</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/withyashar/11257" target="_blank">📅 09:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11256">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ، به شبکه فاکس نیوز: مذاکره با ایران درباره کنار گذاشتن غبار هسته‌ای به دلیل تضاد در تصمیمات ایران، رفت و برگشت دارد تأسیسات هسته‌ای ایران تحت نظارت مداوم ۹ دوربین، ۲۴ ساعته قرار دارند. هرگونه تحرک ایرانی در داخل تأسیسات هسته‌ای با واکنش مستقیم نظامی…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/11256" target="_blank">📅 09:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11255">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e641dc900e.mp4?token=W5J62XPL3MlKGEvZf-hAIFxRt_4RnnXsbppm7cVG1A6PcFFCDF219RxAuJEynNnUgJ7jh3OufvE-X4KyAEHtFOBzruLq9W0LZ_Uk3AjZ_uWrGNLkEkafs8rzeo2WaelIODSbJoFUChJWufHMOFVVGuWhKvW_CaEgXx-bXSDp78coStauOVJwsBSOMFAzs6VRAW5c9TuuPN4NyRS-VtUMEhzVMHIlv2qq6f2v9ufR4b6rtUCRXgzz7ozptjUtgck_bP1CcQN2NbFfPjKGR0i-Ub5YYGhgJUqNnh_H8-ixPBo2fKN19boFPuelSm2SYagxOkoioU44DlNdU9eu4KpcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e641dc900e.mp4?token=W5J62XPL3MlKGEvZf-hAIFxRt_4RnnXsbppm7cVG1A6PcFFCDF219RxAuJEynNnUgJ7jh3OufvE-X4KyAEHtFOBzruLq9W0LZ_Uk3AjZ_uWrGNLkEkafs8rzeo2WaelIODSbJoFUChJWufHMOFVVGuWhKvW_CaEgXx-bXSDp78coStauOVJwsBSOMFAzs6VRAW5c9TuuPN4NyRS-VtUMEhzVMHIlv2qq6f2v9ufR4b6rtUCRXgzz7ozptjUtgck_bP1CcQN2NbFfPjKGR0i-Ub5YYGhgJUqNnh_H8-ixPBo2fKN19boFPuelSm2SYagxOkoioU44DlNdU9eu4KpcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ ترامپ: ما مشکلات زیادی را حل کرده‌ایم که دیگران قادر نبودند و این رابطه یک رابطه بسیار قوی است. فکر می‌کنم در مورد ایران کارهای فوق‌العاده‌ای انجام داده‌ایم، ما هم صحبت کردیم.
‏ما در مورد ایران بسیار مشابه‌ایم، می‌خواهیم این وضعیت پایان یابد. نمی‌خواهیم آن‌ها به سلاح هسته‌ای دست پیدا کنند. می‌خواهیم تنگه‌ها باز باشند و ما آن را برایشان می‌بندیم، آن‌ها تنها تنگه را بستند و بعد ما هم روی سرشان بستیم.
@withyashar</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/11255" target="_blank">📅 09:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11254">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ، به شبکه فاکس نیوز: مذاکره با ایران درباره کنار گذاشتن غبار هسته‌ای به دلیل تضاد در تصمیمات ایران، رفت و برگشت دارد
تأسیسات هسته‌ای ایران تحت نظارت مداوم ۹ دوربین، ۲۴ ساعته قرار دارند.
هرگونه تحرک ایرانی در داخل تأسیسات هسته‌ای با واکنش مستقیم نظامی مواجه خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11254" target="_blank">📅 09:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11253">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/11253" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11252">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBehnam Kok</strong></div>
<div class="tg-text">آقا ما استیکر حامله میخوایم</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/11252" target="_blank">📅 01:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11251">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ در تروث : «وقتی رئیس‌جمهور شی با بیانی بسیار سنجیده از ایالات متحده به‌عنوان کشوری که شاید در حال افول باشد یاد کرد، منظور او آسیب عظیمی بود که ما در چهار سال دوران جو بایدنِ خواب‌آلود و دولت بایدن متحمل شدیم؛ و در این مورد، او صددرصد درست می‌گفت.
کشور ما با مرزهای باز، مالیات‌های سنگین، ترویج تغییر جنسیت برای همه، حضور مردان در ورزش زنان، سیاست‌های موسوم به تنوع و شمول، توافق‌های تجاری وحشتناک، جرم و جنایت گسترده و بسیاری مسائل دیگر، آسیب غیرقابل‌تصوری دید!
@withyashar
رئیس‌جمهور شی به هیچ‌وجه به رشد شگفت‌انگیزی اشاره نمی‌کرد که ایالات متحده در طول شانزده ماه فوق‌العاده دولت ترامپ به جهان نشان داده است؛ دورانی که شامل رکورد تاریخی بازار بورس و صندوق‌های بازنشستگی، پیروزی نظامی و روابط شکوفا با ونزوئلا، درهم‌کوبیدن نظامی ایران (ادامه دارد!)، قدرتمندترین ارتش جهان با اختلاف بسیار زیاد، تبدیل دوباره آمریکا به یک قدرت اقتصادی عظیم، جذب رکورد هجده تریلیون دلار سرمایه‌گذاری خارجی در آمریکا، بهترین بازار کار تاریخ ایالات متحده با بیشترین تعداد شاغلان تاریخ کشور، پایان دادن به سیاست‌های ویرانگر موسوم به تنوع و شمول و بسیاری موفقیت‌های دیگر بوده که فهرست کردن همه آنها ممکن نیست.
در حقیقت، رئیس‌جمهور شی بابت این همه موفقیت بزرگ در چنین مدت کوتاهی به من تبریک گفت.
دو سال پیش، ما واقعاً کشوری در حال افول بودیم. در این مورد کاملاً با رئیس‌جمهور شی موافقم! اما حالا ایالات متحده داغ‌ترین و پررونق‌ترین کشور جهان است و امیدوارم رابطه ما با چین از همیشه قوی‌تر و بهتر باشد!»
@withyashar</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/11251" target="_blank">📅 01:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11250">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فاکس نیوز : تو سفر ترامپ، بین مأموران سرویس مخفی آمریکا و پلیس چین، تنش ایجاد شده و درگیری لفظی و حتی فیزیکی هم پیش اومده.
@withyashar</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/11250" target="_blank">📅 01:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11249">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB8oJUkyrSBysRzP-M_1gQ-TT5d3knMSu1TIdnQf7KJno1nPyjHRF6Nk9UMwmiNOWOfxnZKSbsmm18zk5JDZOAOMY1k7OQZnozCeBvVRZ2HqmelGWJVOTWlXErNhCjRmefjvt2zYqMklAS4TOt7Lqs4_nxvLCDx-5TrfP5YBRvsYzzl5kHkk3V-L9d7L9GmAikt69UL2F4PJFLHLfkTZlsxVQ582t8G9_8Hu9KfzajkH1hACSIRJUAzBnYvjI-agiAl7IOCneOOdOsueNcTNewe9hgs7r2CGy02s0oyO_EcnKKZfcM9FBa8wt5PaJdkIFu-c3UAJIvLIcz5O5CTv_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کت کش ها در مراسم اربعین کتلت سرلشکر سیدعبدالرحیم موسوی در قم
@withyashar</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/11249" target="_blank">📅 00:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11248">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591abd93e.mp4?token=c62lvPJg4n5FaSYq0sRyAY7_FWcXhjMKaox2rPsMnWzGi0lhaQwWdmNlSF6at01Hn2moIMrRQcuD4iiz6vQDJUsjF3C3DbVihHvcYpQsQOexe6Mbh5lvPHKkk64lRUuGr-hAfZFL_LmRw3h3rYMWn3uQHwS94SjyJQYb3yAkIV-t_6Fayx8TMQVONYTK62As8mHdHVDEvUEKUlg1PoycG2yX0FVm1454pMgw4o7jsyfh4SQN17FDoO9MT3JdQsOyDPO_XMsBT6GUI2QSNgBRUat8-XRn7hwPDgSCUCKBOJ0vBr39BP3GduTaSjYN_7Mb6OtVK06ClqYcE-7OQSolOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591abd93e.mp4?token=c62lvPJg4n5FaSYq0sRyAY7_FWcXhjMKaox2rPsMnWzGi0lhaQwWdmNlSF6at01Hn2moIMrRQcuD4iiz6vQDJUsjF3C3DbVihHvcYpQsQOexe6Mbh5lvPHKkk64lRUuGr-hAfZFL_LmRw3h3rYMWn3uQHwS94SjyJQYb3yAkIV-t_6Fayx8TMQVONYTK62As8mHdHVDEvUEKUlg1PoycG2yX0FVm1454pMgw4o7jsyfh4SQN17FDoO9MT3JdQsOyDPO_XMsBT6GUI2QSNgBRUat8-XRn7hwPDgSCUCKBOJ0vBr39BP3GduTaSjYN_7Mb6OtVK06ClqYcE-7OQSolOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ به دلیل مرگ برادر بزرگترش که بر اثر نوشیدن الکل جانش را از دست داد ،مشروب نمیخوره ،ولی اینجا جرعه‌ای از آن را مینوشه و به نشانه احترام به رئیس جمهور شی جین پینگ
‏ولی داشت بالا می‌آورد
@withyashar</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/11248" target="_blank">📅 00:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11247">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">طبق گزارش‌های امروز، هرتزوگ رئیس جمهور اسرائیل حضور حضوری خود در نیویورک را لغو کرده و گفته به دلیل «شرایطی که مانع سفر شده» نمی‌تواند به آمریکا بیاید.
اما این سفر یک سفر رسمی سیاسی به کاخ سفید نبود،بلکه مربوط به شرکت او در مراسم فارغ‌التحصیلی «Jewish Theological Seminary» در نیویورک بود.
در عین حال، خبر جداگانه‌ای هم درباره سفر احتمالی بنیامین ناتانیاهو به آمریکا وجود داشت که دفتر او گفته بود هنوز برنامه قطعی‌ای برایش نهایی نشده است
@withyashar</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/11247" target="_blank">📅 00:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11246">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">طبق گزارش فاکس نیوز : رئیس‌جمهور ترامپ و هیئت همراهش در طول سفر به چین از تلفن‌ها و لپ‌تاپ‌های جایگزین استفاده کردند به دلیل نگرانی‌هایی که داشتند مبنی بر اینکه مقامات چینی ممکن است از آن‌ها برای نصب نرم‌افزار جاسوسی استفاده کنند
@withyashar</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/11246" target="_blank">📅 23:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11245">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">همینجور این پیغام میاد دم همتون گرم مخصوصا عزیزی که یاد کرد از من
🥹
🙌🏾
❤️‍🩹
میامممم میاممم</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/11245" target="_blank">📅 23:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11244">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmd</strong></div>
<div class="tg-text">یکی اومد رو خط برنامه کامبیز تو اینترنشنال گفتش از همه مجریای اینترنشنال تشکر میکنم ، حتی یاشار وار روم توی تلگرام ک خیلیا اخبارا رو ازونجا دنبال میکنن دمتون گرم</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/11244" target="_blank">📅 23:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11242">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دیده شده پهپاد شناسایی و صدای پدافند غرب تهران
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/11242" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11241">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اعتراضات کوبا شروع شد کشور در حال  فروپاشی
طبق گزارش‌ها، شبکه برق کوبا در بامداد امروز دچار فروپاشی شد و مناطق شرقی از جمله شهر مهم سانتیاگو دِ کوبا بدون برق ماندند. مردم به خیابان آمدند، قابلمه‌ها را به هم کوبیدند، زباله آتش زدند و شعار «برق را وصل کنید» سر دادند.
دولت کوبا علت اصلی را تحریم‌ها و فشار آمریکا بر صادرات سوخت به کوبا می‌داند. رسانه‌هایی مانند رویترز و گاردین نوشته‌اند که پس از تهدیدهای جدید دولت ترامپ علیه کشورهایی که به کوبا سوخت می‌فرستند، ارسال نفت از ونزوئلا و مکزیک کاهش یافته و کوبا عملاً ذخیره سوختش را از دست داده است. وزیر انرژی کوبا گفته:
«ما مطلقاً هیچ گازوئیل و هیچ نفت کوره‌ای نداریم.»
در بعضی مناطق مردم تا ۲۰ یا حتی ۲۲ ساعت در روز برق ندارند. این وضعیت باعث خراب شدن مواد غذایی، اختلال در بیمارستان‌ها، حمل‌ونقل و حتی تعطیلی برخی خدمات عمومی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/11241" target="_blank">📅 23:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11240">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/141998de31.mp4?token=mWjKL2syYnwh-XyrnfJBPHJ8rVi-6aZV8LWqYTdoxOToXzAtM6eyMdGUPLTLhHhn9i4PcpnklZS0g1eSAhFe19wCr4F-Ib1wIr7ho47yrZ6esNIL-apTeZymZZ6wLd2O_wDPcHFzS8R2FJKdT5tqIfQyeJ9_pFD7z8UTjlZnaB0e8bsqWAxnxNq5boTh56UnqHV0AqSLrCJNKJr-gti6kn2H0s5ttNudyjvSzSMPNF7jYd70J71HJS2Pqba2ZyWtmxD3bvhgeuJcK8CFhkYfAxAgn65GZxuCI-_0g8S6HHKDuKJf829-WZ9-1g4lzU43de0qiw7RnkkDaWGNh1MVzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/141998de31.mp4?token=mWjKL2syYnwh-XyrnfJBPHJ8rVi-6aZV8LWqYTdoxOToXzAtM6eyMdGUPLTLhHhn9i4PcpnklZS0g1eSAhFe19wCr4F-Ib1wIr7ho47yrZ6esNIL-apTeZymZZ6wLd2O_wDPcHFzS8R2FJKdT5tqIfQyeJ9_pFD7z8UTjlZnaB0e8bsqWAxnxNq5boTh56UnqHV0AqSLrCJNKJr-gti6kn2H0s5ttNudyjvSzSMPNF7jYd70J71HJS2Pqba2ZyWtmxD3bvhgeuJcK8CFhkYfAxAgn65GZxuCI-_0g8S6HHKDuKJf829-WZ9-1g4lzU43de0qiw7RnkkDaWGNh1MVzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیروزی بزرگ برای‌ ترامپ ، فاکس نیوز تایید کرد
رئیس جمهور چین، شی جین پینگ دستور داد در مورد ایران، «هر چیزی که ترامپ نیاز دارد» را به آمریکا بدهید.
از ‌آمریکا سویای بیشتری بخرید.
نفت بیشتری از آمریکا بخرید.
از آمریکا گاز مایع طبیعی بیشتری بخرید.
۲۰۰ جت بوئینگ ۷۳۷ مکس بخرید.
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/11240" target="_blank">📅 22:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11239">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبر خوب
😍</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/11239" target="_blank">📅 22:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11238">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7bad13156.mp4?token=bpCAOSuqZtLMYAYqnB-HJEb7KW_ce2oe6N-ZpHUw8Uaikh-TrI0KkCfKFYF4fmaCiHTJoNx6Tt5QGt1Pqk2DwwI8NgFbCAxeY115PaztVOHpb9444oh4WXSpF8qkFVxbZGtloHkyaxJST0EfhddYwQKHh2DJIfe7W43JKios9YgIllAm-2eFZzsBro135NHjiCtadw66QKvNz86u0xR9Y4JCs5vi37__w4FjISf4yvbPwE331Lis6yMLC-CyYznquvE8peE--8g-CnJtOrYKqgog7eOtgYUe3aeJ4gAszehZ3A1fZZv0y86szcKsHF8Po91diT2KZClqBn8PKvgldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7bad13156.mp4?token=bpCAOSuqZtLMYAYqnB-HJEb7KW_ce2oe6N-ZpHUw8Uaikh-TrI0KkCfKFYF4fmaCiHTJoNx6Tt5QGt1Pqk2DwwI8NgFbCAxeY115PaztVOHpb9444oh4WXSpF8qkFVxbZGtloHkyaxJST0EfhddYwQKHh2DJIfe7W43JKios9YgIllAm-2eFZzsBro135NHjiCtadw66QKvNz86u0xR9Y4JCs5vi37__w4FjISf4yvbPwE331Lis6yMLC-CyYznquvE8peE--8g-CnJtOrYKqgog7eOtgYUe3aeJ4gAszehZ3A1fZZv0y86szcKsHF8Po91diT2KZClqBn8PKvgldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: دشمنان ما به دنبال نابودی همه ما هستند. همه ما
آنها بین راست و چپ، سکولار و مذهبی، یهودی و عرب تفاوتی قائل نمی‌شوند.
@withyashar
نتانیاهو: اورشلیم را تحت حاکمیت اسرائیل برای همیشه حفظ خواهیم کرد</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/11238" target="_blank">📅 22:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11237">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/11237" target="_blank">📅 21:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11236">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سومین دور مذاکرات مستقیم لبنان و اسرائیل در واشنگتن آغاز شد
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/11236" target="_blank">📅 21:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11235">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ اعلام کرد که انتظار می‌رود پکن ۲۰۰ هواپیما از بوئینگ سفارش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/11235" target="_blank">📅 21:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11234">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کان نیوز : مقامات ارشد ارتش اسرائیل و سنتکام  هفته گذشته جلسه داشتن و منتظرن ببینن فردا ترامپ بعد اتمام سفرش چه تصمیمی میگیره
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/11234" target="_blank">📅 21:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11233">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016c112e90.mp4?token=r03teABsBKrMkox2wuLps3SR9pJadjcHmnr7s69PUM4qlfSLFy__falIHViuNo2CCVNYtnToGS30HHVf0U1TFI36jMe24JW5d6PXvmZjepS3VJmJbWRPOGtD_8x9Gi5AtEd72nSueRP0Zk9MtEVcDQTb7eDfyObdteCG0eqp2xM-8uIgiT4qSNsAHeCAigzniZge8aftkUB98KvMK0I5JUD4dm8qm4pao0U65UqwkzJBRgpnYpiDsrJWy7pYssrdqSrKpk7tCUFmz4EWHfSbPIv7uZ6Ct4X44J8sCmZxKCD5oNaF7T2DfkFR8q_JJkhVZ8MDue7Fd1vjfj7BHsbpq1xWv9pYRDOmc2XLLrlMU8aJ3hHTEfwEa240uq5mZUUpOYSdBxbq9IbdKPn2AGfhvD40mSKlt1I0vU5JaIMkTkykm-9YvwPgYqNctMNeD2HVOI2i3aIfg0TiAbo8XaQ5Xoc-svSy408UY_gKlFszGv987HWRg4fwRqYh-pTBpysJD735YoGahjHunL_bejeo8CfP6lmYe30bTxbJIRNBIoJ1wdE4md-bUK1DagRveeabTCj6zmEeLTTRr7wPmJDIsRgXI6pvCcD8BRK7c2SUGtFX528kW088tDcMW4l_9vgiFxTOJcjb14wCD9CK1gPRgcHaEESLsWQe6TJKZaGg2Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016c112e90.mp4?token=r03teABsBKrMkox2wuLps3SR9pJadjcHmnr7s69PUM4qlfSLFy__falIHViuNo2CCVNYtnToGS30HHVf0U1TFI36jMe24JW5d6PXvmZjepS3VJmJbWRPOGtD_8x9Gi5AtEd72nSueRP0Zk9MtEVcDQTb7eDfyObdteCG0eqp2xM-8uIgiT4qSNsAHeCAigzniZge8aftkUB98KvMK0I5JUD4dm8qm4pao0U65UqwkzJBRgpnYpiDsrJWy7pYssrdqSrKpk7tCUFmz4EWHfSbPIv7uZ6Ct4X44J8sCmZxKCD5oNaF7T2DfkFR8q_JJkhVZ8MDue7Fd1vjfj7BHsbpq1xWv9pYRDOmc2XLLrlMU8aJ3hHTEfwEa240uq5mZUUpOYSdBxbq9IbdKPn2AGfhvD40mSKlt1I0vU5JaIMkTkykm-9YvwPgYqNctMNeD2HVOI2i3aIfg0TiAbo8XaQ5Xoc-svSy408UY_gKlFszGv987HWRg4fwRqYh-pTBpysJD735YoGahjHunL_bejeo8CfP6lmYe30bTxbJIRNBIoJ1wdE4md-bUK1DagRveeabTCj6zmEeLTTRr7wPmJDIsRgXI6pvCcD8BRK7c2SUGtFX528kW088tDcMW4l_9vgiFxTOJcjb14wCD9CK1gPRgcHaEESLsWQe6TJKZaGg2Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار ، شواهد نشان دهنده حمله غافلگیر کننده برای کتلت پزون است
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/11233" target="_blank">📅 20:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11232">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30fb109482.mp4?token=ULcsiQ66nBm8YJ2z5irQFT_-B2QOkNZhQyVkCJEHd4FJlnQcA5XQV8GeCe3W5HeSj3D6ZRVtPpTtxtQDYqxR1C-vdtM5-kJQSsdPKcYqyVqWETZwBt3eOBVt66FjdTOE2R2bB8Zm6H4jr9qPoq-kV-o_QfkLV5WbO-umz8pWOAMrA5MNqc7Im0F6M78wFksTx4EgJISf5Cy24GNICRHvvF9rLzOHoP6SXOOMMRYAnUIQd6F1DE1E6vPZLqs96dy4VpbX9wCjUaqs2BP8BdL1P7yfC7_wWFkpjLCyaHrgbCM-4WeGFnMn2ycPd5cOl4s1vjFdQY1oahjRp5I0cOQwug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30fb109482.mp4?token=ULcsiQ66nBm8YJ2z5irQFT_-B2QOkNZhQyVkCJEHd4FJlnQcA5XQV8GeCe3W5HeSj3D6ZRVtPpTtxtQDYqxR1C-vdtM5-kJQSsdPKcYqyVqWETZwBt3eOBVt66FjdTOE2R2bB8Zm6H4jr9qPoq-kV-o_QfkLV5WbO-umz8pWOAMrA5MNqc7Im0F6M78wFksTx4EgJISf5Cy24GNICRHvvF9rLzOHoP6SXOOMMRYAnUIQd6F1DE1E6vPZLqs96dy4VpbX9wCjUaqs2BP8BdL1P7yfC7_wWFkpjLCyaHrgbCM-4WeGFnMn2ycPd5cOl4s1vjFdQY1oahjRp5I0cOQwug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سال ۱۹۷۲، شهبانو فرح پهلوی به دعوت رسمی دولت چین به این کشور سفر کرد؛ سفری تاریخی و بی‌سابقه که در اوج جنگ سرد، نماد دیپلماسی بی‌طرفانه ایران بود
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/11232" target="_blank">📅 20:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11231">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آیا درباره حمایت چین از ایران با رئیس جمهور چین صحبت کردید؟  ترامپ: ما در مورد این موضوع صحبت کردیم. منظورم اینه که وقتی میگید «حمایت»، آنها با ما جنگ نمی‌کنن یا چیزی شبیه این. او گفت که تجهیزات نظامی ارائه نخواهد کرد، این یک بیانیه بزرگه. اما در عین حال گفت…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/11231" target="_blank">📅 19:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11230">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/11230" target="_blank">📅 19:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11229">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">«دریادار برد کوپر»، فرمانده سنتکام:  «فرماندهی مرکزی ایالات متحده (سنتکام) مستقیماً در پاسخ به تهدیدهایی که جمهوری اسلامی ایران ایجاد می‌کرد، تأسیس شد.  رژیم ایران طی ۴۷ سال گذشته منطقه را دچار هراس و بی‌ثباتی کرده و دشمنی با آمریکا را به یکی از اصول اساسی…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/11229" target="_blank">📅 19:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11228">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11228" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11227">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗦𝗨𝗦</strong></div>
<div class="tg-text">خسته نباشی یاشار
نظرت راجب سیم‌کارت پرو چیه به مردم عادی هم دارن میدن الان</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/11227" target="_blank">📅 18:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11226">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">لطفا عکس از اس ام اس هایی که رژیم میده برام نفرستید ! خیلی خوشم میاد ! اگه قرار‌باشه هر روز اونا اس ام اس بدن شمام همتون اسکرین بفرستین که نمیشه ! به هیچ عنوان اسکرین ندید دیگه مخصوصا ‌جانفدا رو … مرسی اه</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/11226" target="_blank">📅 18:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11225">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ: رهبر چین پیشنهاد کمک در مورد مسئله ایران را داد
او قول داد که تجهیزات نظامی به آنها منتقل نکند.
او می‌خواهد تنگه هرمز باز بماند.
@withyashar</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/11225" target="_blank">📅 18:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11224">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سناتور کنگره خطاب به برد کوپر:
برجام توانایی هسته ای ایران رو محدود میکرد ولی ترامپ پاره کرد، الان وارد یه جنگ بی‌پایان شدیم، آیا ترامپ هیچ وقت به شما نگفت چرا برجام رو پاره کرد؟
کوپر فرمانده سنتکام:
خانم سناتور زمانی که این ۸ سال پیش اتفاق افتاد من یک سمت دیگه داشتم! من سیاستمدار نیستم و نمیتونم جواب این سوال رو بدم!
@withyashar</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/11224" target="_blank">📅 18:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11223">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e028b3e623.mp4?token=ftdgon4p7igksMXbA8e_HBAVQeCsaghF7rLBBxFfN7ezQ_AS-sQ4a3IK7aJwCvuj8pAIMZQNpmSH9JMMZP1CSnGkn-RfK_CrAsjB0jd76HZ3tRPGP-q9yf6fkEVkXV9i0xRVsoxK2i8OSJkj0eUTDQ1dsFGZuabQivBfa2DTvib-ThHTUnCbNplKtI4uqknDBWiEQ_gJhzRG4M6-1Vgxia1DKRNf9ej4K_2c-RCB1Q6DB6I-kLar_g6jL-Z-TCL2oJ1Hd38lhsGKfs_fv0EPLy9lAltGfZYvrWQbjGD9OtsaJw3Bj2KVruzV-7sLPG5OHFDezXiaSe8itmqKK_HvyIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e028b3e623.mp4?token=ftdgon4p7igksMXbA8e_HBAVQeCsaghF7rLBBxFfN7ezQ_AS-sQ4a3IK7aJwCvuj8pAIMZQNpmSH9JMMZP1CSnGkn-RfK_CrAsjB0jd76HZ3tRPGP-q9yf6fkEVkXV9i0xRVsoxK2i8OSJkj0eUTDQ1dsFGZuabQivBfa2DTvib-ThHTUnCbNplKtI4uqknDBWiEQ_gJhzRG4M6-1Vgxia1DKRNf9ej4K_2c-RCB1Q6DB6I-kLar_g6jL-Z-TCL2oJ1Hd38lhsGKfs_fv0EPLy9lAltGfZYvrWQbjGD9OtsaJw3Bj2KVruzV-7sLPG5OHFDezXiaSe8itmqKK_HvyIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«دریادار برد کوپر»، فرمانده سنتکام:
«فرماندهی مرکزی ایالات متحده (سنتکام) مستقیماً در پاسخ به تهدیدهایی که جمهوری اسلامی ایران ایجاد می‌کرد، تأسیس شد.
رژیم ایران طی ۴۷ سال گذشته منطقه را دچار هراس و بی‌ثباتی کرده و دشمنی با آمریکا را به یکی از اصول اساسی حاکمیت خود تبدیل کرده است.
سابقه خصمانه و مرگبار آنها علیه ایالات متحده کاملاً مستند و ثبت‌شده است
@withyashar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/11223" target="_blank">📅 18:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11222">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آیا درباره حمایت چین از ایران با رئیس جمهور چین صحبت کردید؟
ترامپ: ما در مورد این موضوع صحبت کردیم. منظورم اینه که وقتی میگید «حمایت»، آنها با ما جنگ نمی‌کنن یا چیزی شبیه این. او گفت که تجهیزات نظامی ارائه نخواهد کرد، این یک بیانیه بزرگه. اما در عین حال گفت که آنها مقدار زیادی نفت خودشون رو از ایران میخرن و دوست دارن این کار رو ادامه بدن.
@withyashar</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/11222" target="_blank">📅 18:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11221">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">برد کوپر فرمانده سنتکام مدعی شد:
توانمندی‌های موشکی، دریایی، پهپادی و صنعتی ایران 90 درصد تضعیف شده است. او افزود که نیروی دریایی ایران تا یک نسل دیگر نیز به سطحی که پیش از جنگ در اختیار داشت باز نخواهد گشت
@withyashar</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/withyashar/11221" target="_blank">📅 18:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11220">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fca974d01b.mp4?token=aZt-lKMp9Q7LYKonHTUPVIomDbMX_aATjWBGVfs4e8uhvP3wjLxiI-TEAUtT56cZYurAg8T_ailU4VqPUA7X6RSbqraY6r3TwDKTiglZmPJaKbgAZtu5ScNEZu3TXe_YzWYhHRc3eCLc-8ONPc4-C4X3Fw7soUZV6awDKe3OcCBtGPjxFn1qKu90Ws-1W97uB6XmZ3umCeAg-1rnfAdNOim-XjEf6rppyoEZhy4wu7PbViz07T4SSR84Zx_9x_Uh7lQKTkXz7Lc6btwxZ8ExmduPcQ3w50PCmv8bb7Gz89Nri8zCApzNh2NGy1bbf4ROSRTxUJbAK7A4ciz6fQFJ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fca974d01b.mp4?token=aZt-lKMp9Q7LYKonHTUPVIomDbMX_aATjWBGVfs4e8uhvP3wjLxiI-TEAUtT56cZYurAg8T_ailU4VqPUA7X6RSbqraY6r3TwDKTiglZmPJaKbgAZtu5ScNEZu3TXe_YzWYhHRc3eCLc-8ONPc4-C4X3Fw7soUZV6awDKe3OcCBtGPjxFn1qKu90Ws-1W97uB6XmZ3umCeAg-1rnfAdNOim-XjEf6rppyoEZhy4wu7PbViz07T4SSR84Zx_9x_Uh7lQKTkXz7Lc6btwxZ8ExmduPcQ3w50PCmv8bb7Gz89Nri8zCApzNh2NGy1bbf4ROSRTxUJbAK7A4ciz6fQFJ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک و پسرش  «اِکس اَش اِی-توئلو» «X Æ A-Xii» در پکن
@withyashar</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/11220" target="_blank">📅 18:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11219">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فرمانده سنت‌کام: ظرف کمتر از ۴۰ روز می‌توانیم به اهدافمان در ایران دست پیدا کنیم
@withyashar</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/11219" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11218">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نتانیاهو، نخست‌وزیر، و گیدعون سعر، وزیر خارجه، به مقامات دستور داده‌اند تا مقدمات طرح شکایت افترا علیه نیویورک تایمز را آغاز کنند.
این شکایت به دلیل انتشار یادداشتی از نیکلاس کریستوف که شامل اتهاماتی مبنی بر سوءاستفاده جنسی از فلسطینیان در زندان‌های اسرائیل بوده،
مقاله کریستف با عنوان «سکوتی که تجاوز به فلسطینیان با آن روبرو می‌شود» روز دوشنبه ۱۱ مه در نیویورک‌تایمز منتشر شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/11218" target="_blank">📅 18:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11217">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxM7v6-rDsYCS9gYvxYK6FxL5wdwMSYoIBc9zxGL4xv0rGhUYl5qn8fYDI2Ci62gD6nsXSu6z2RkDaPxiR13FI9E-QNBisPJOSFVs0KW2vT9ZtFcZvlbNstYl6csgyRumsXVyrnbSqWkZJ3uUJ_C1Y7ZnyaEWPn4DDRAoNFKYCge90veml3TlN3nNUHU-iAtt-1GSH8SvnN437JTPFmUmxf_SRJqtPoYlGgSs6ub62qJ6NctPQdB2m7fIh9vaRbzVe1dnFpQO9i38bGHBEzjsE4XnYCgNwdOUPl0dolks-StNQXsn50ubzCJRueQcacJjgUJEq-6a6-0NMyVysiBJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">INDOPACOM
، فرماندهی نظامی آمریکا برای منطقهٔ «هندو-پاسیفیک»ایندوپکام: تفنگداران دریایی ایالات متحده، واحد یازدهم اعزامی تفنگداران دریایی، در حال انجام تیراندازی رزمی بر روی ناو جنگی یو اس اس کامستاک (LSD 45) در اقیانوس هند هستند. واحد یازدهم اعزامی دریایی، که بر روی گروه آماده آبی-خاکی باکسر(USS BOXER) مستقر شده است، یک نیروی پایدار و قابل اعتماد رزمی است که به بازدارندگی و واکنش به بحران در منطقه عملیاتی ناوگان هفتم ایالات متحده کمک می‌کند.
@withyashar
یاشار: ساده بگم ناو باکسر وسط راه مونده داره تمرین میکنه و معلوم نیست کی بیاد !</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/11217" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11215">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d789d55b5d.mp4?token=MTaXTUPFvWZ-I1QvGc9XstBShpg_dg0dLXKPTSNsadvIiZjGuGbMPrg7xVDK1oejgL3guaMRJuf6aW9G3bc1Q9COYvMpK-dNJrXt5Jvidu6ZWgRdDJN6rhjKGzbf9Xsbxd0Xao6r48XLHUWZXbtI6N67b-casBRANaC361ESm8UfBhBOlXYg4qQwqBPeoTrue89Q-6ze7sWEk293XdXeRPCpsFrM-4gA-Z1prV9oK4FAiPoaFPDf4h8_vye5CzE7em43CQz-QYzVQBXGFFFq0lcsQg_R7Ld_SeXEbVYxUfPXfa_h3-LyjkUV7ycLrf8rXIMFKtcsgkXQrh2-GmqgWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d789d55b5d.mp4?token=MTaXTUPFvWZ-I1QvGc9XstBShpg_dg0dLXKPTSNsadvIiZjGuGbMPrg7xVDK1oejgL3guaMRJuf6aW9G3bc1Q9COYvMpK-dNJrXt5Jvidu6ZWgRdDJN6rhjKGzbf9Xsbxd0Xao6r48XLHUWZXbtI6N67b-casBRANaC361ESm8UfBhBOlXYg4qQwqBPeoTrue89Q-6ze7sWEk293XdXeRPCpsFrM-4gA-Z1prV9oK4FAiPoaFPDf4h8_vye5CzE7em43CQz-QYzVQBXGFFFq0lcsQg_R7Ld_SeXEbVYxUfPXfa_h3-LyjkUV7ycLrf8rXIMFKtcsgkXQrh2-GmqgWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشیT1 "ترامپ موبایل" بعد از نزدیک
یه سال تأخیر بالاخره داره عرضه میشه
یه گوشی طلایی ۴۹۹ دلاری با برند ترامپه که
چیپ اسنپدراگون سری ۷، رم ۱۲ گیگ، حافظه
۵۱۲ گیگ و دوربین سه‌گانه ۵۰ مگاپیکسلی دارهبه نظر میاد در اصل یه گوشی ساخت چین باشه که فقط مونتاژ نهاییشو تو آمریکا انجام دادن
@withyashar</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/11215" target="_blank">📅 16:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11214">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مارکو روبیو : ترامپ موضوع ایران رو با چین مطرح کرد و این خیلی مهم بود
طرف چینی گفت ما موافق نظامی‌کردن تنگه هرمز نیستیم
با سیستم عوارض‌گیری هم مخالفیم، و این موضع ما هم هست
@withyashar</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/11214" target="_blank">📅 16:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11213">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزیر خزانه داری آمریکا:ایران رو انقدر تحت فشار اقتصادی قرار دادیم که توی پرداخت حقوق نیروهاشم به مشکل خورده. دارن نفسای آخرشونو میکشن
@withyashar</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/11213" target="_blank">📅 16:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11212">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c931f479b.mp4?token=opFqMnQuT1HfufgCKUGfm0IGklG4Ct9UgaSXvJh5d8L0mgGB-CkBtkmm2oAqPCszXYLNJLGRbAbKqXwzo-4N0-lgamTGSLqao2coEZFB2o6GubClgm0T0gnkOg-Rt72yWUSVvgnp-Zh3WOlruhhV5QdUxSjctj5UAKFO-J8DP7nMuZuuatLBZb7dzelbsXkylJ8SR0nnCyR7D36nJcoQGn1q6qcWE8UVH0l6mPzaTytEMOon_1ygeID9gOeujHIH24R7y1NvtXWKToXgxEdEdvoxatvkDjrE4aVC6OGAWXw8mL1I91N8rLx5WhIC5lsBtNzpArTLOe5KzZJ0zOJQ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c931f479b.mp4?token=opFqMnQuT1HfufgCKUGfm0IGklG4Ct9UgaSXvJh5d8L0mgGB-CkBtkmm2oAqPCszXYLNJLGRbAbKqXwzo-4N0-lgamTGSLqao2coEZFB2o6GubClgm0T0gnkOg-Rt72yWUSVvgnp-Zh3WOlruhhV5QdUxSjctj5UAKFO-J8DP7nMuZuuatLBZb7dzelbsXkylJ8SR0nnCyR7D36nJcoQGn1q6qcWE8UVH0l6mPzaTytEMOon_1ygeID9gOeujHIH24R7y1NvtXWKToXgxEdEdvoxatvkDjrE4aVC6OGAWXw8mL1I91N8rLx5WhIC5lsBtNzpArTLOe5KzZJ0zOJQ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز درباره ایران:
ماموریت ما کامل نشده است.ما برای احتمال اینکه ممکن است مجبور شویم دوباره اقدام کنیم - شاید حتی به زودی - آماده‌ایم. اگر اهداف تأمین نشوند، دوباره اقدام خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/11212" target="_blank">📅 15:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11211">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqurPbhzt8m61eB5vHphZxEceLBqSID3zu4YopagzD18iDlFEYXSCGhMs2T-u5j6LRdpoEhK6XPFeqbt9RENsFRrSutFn0uvSycPFexMBY9VVtPfIp4wFgFLM5GdeTIgymCiX5i9UeBzI9ntFFXvs_QpedXZv6G61fgWJup1IPR6E2epdhSf1MzA0E0KPcV8A5FU2DgXSAi-ML-HlmdJ77moPIQdpMy5HyaSGAFVPo6XL1mfxceuBf0fFtx-HVWxIXTfXzqdCpmdF0C82wainV5ogrZjCxE4VUcBTXBqlA-Xmc0eqP5ZNf0K7_IMq30t7zUDsmKoFAmelGVJIL9DOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلفی لی جون، بنیانگذار و مدیرعامل شیائومی با ایلان ماسک
@withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/11211" target="_blank">📅 14:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11210">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الجزیره: چین با آمریکا در مورد ایران انعطاف دارد، اما در مورد تایوان نه
مسئولان چینی پیام واضحی به ایالات متحده ارسال کرده‌اند:
چین در بسیاری از مسائل مانند ایران، تجارت و فناوری آماده انعطاف و پذیرش اختلاف نظر است، اما در یک موضوع حساس، انعطاف‌پذیر نیست و آن تایوان است.
@withyashar</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/11210" target="_blank">📅 14:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11209">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda0441500.mp4?token=nkVWEka2_EQo_UFsS1JgjV9jlkEprxanXYkMFgjN5-TCipIexXjAms9RgptQvP6-zzYupuM42D6zwjW3e9V593uov6MLsQhGT0zyKDxWnnZhnxXFiSHtIOp4GuOXDT1kNx8GUuS_pm67EWCKGKEmyoXn_lgRGQx8dX6PM_c2rwy3XWU21GAwUntpaEAUddQeCszDK3jTrJxex4F59fw1hW3WxGMlKmanIo99yGmJ7WTM3aQKZVh-sEKfblyZ0gADg-85trjGNIzEe25yr-P_5vfsmVvvvNdIcXEXB8wxEdXGoFHo3AGOh3TkbRrxQAUciJ3zhI20UKZxjJvD4t-iOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda0441500.mp4?token=nkVWEka2_EQo_UFsS1JgjV9jlkEprxanXYkMFgjN5-TCipIexXjAms9RgptQvP6-zzYupuM42D6zwjW3e9V593uov6MLsQhGT0zyKDxWnnZhnxXFiSHtIOp4GuOXDT1kNx8GUuS_pm67EWCKGKEmyoXn_lgRGQx8dX6PM_c2rwy3XWU21GAwUntpaEAUddQeCszDK3jTrJxex4F59fw1hW3WxGMlKmanIo99yGmJ7WTM3aQKZVh-sEKfblyZ0gADg-85trjGNIzEe25yr-P_5vfsmVvvvNdIcXEXB8wxEdXGoFHo3AGOh3TkbRrxQAUciJ3zhI20UKZxjJvD4t-iOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان لوله لول سر میز شمام
😂
@withyashar</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/11209" target="_blank">📅 14:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11208">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
تأسیسات اصلی بارگیری نفت ایران به مدت ۳ روز است از سرویس خارج شده است
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11208" target="_blank">📅 14:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11207">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرنگار صداوسیما به نقل از نیروی دریایی سپاه: از شب گذشته تاکنون ۳۰ فروند کشتی از تنگه هرمز با مجوز ایران عبور کرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/11207" target="_blank">📅 14:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11206">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شی جین‌پینگ: چین و ایالات متحده هر دو از همکاری سود می‌برند و از تقابل زیان می‌بینند.
دو کشور ما باید شریک باشند نه رقیب.
@withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/11206" target="_blank">📅 14:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11205">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ از رئیس‌جمهور چین برای سفر به ایالات متحده در ماه سپتامبر آینده دعوت کرد
@withyashar</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/11205" target="_blank">📅 14:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11204">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آکسیوس: یکی از گزینه‌های ترامپ پس از بازگشت از چین از سر گیری پروژه آزادی در تنگه هرمز است. گزینه دیگر  ترامپ حمله به زیرساخت‌های ایرانه.
@withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11204" target="_blank">📅 14:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11203">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">طبق برنامه ای که قرار داده بودیم   ترامپ و رییس‌جمهور چین برای یک مهمانی شام با یکدیگر دیدار کردند @withyashar</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/11203" target="_blank">📅 14:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11202">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24c3a9a1e.mp4?token=EFFcF93XbKA_7FyDQ99xMZwjGHpdXKgviFlmY4j4d6SfPMvVM9qblc1QitK50X272u6lcGC6RweQItmML8zlGNtiI55OkUrrdUe6ctURa8Zfsi_ESu0nUIVrJy0Ulca80cco8jEIBraOCTDyA6JVwLhJystKl7stngXMCwQizrEQqxuxIDIqYZVlP1TYgy0Ej0E0EQD2D3zTpWgL5bwXmxOAhPSrGAm4kUfVNNlKJT1Xnj503-WV5rnFS1V-Zzhg8YReWTHEdg56RWhX3bjg3Q6NvkepkN-l8VNWxCmeTV51-OIB7gNW64vx38gqVTQYpngtvtNddeuHwIcDW2Y43g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24c3a9a1e.mp4?token=EFFcF93XbKA_7FyDQ99xMZwjGHpdXKgviFlmY4j4d6SfPMvVM9qblc1QitK50X272u6lcGC6RweQItmML8zlGNtiI55OkUrrdUe6ctURa8Zfsi_ESu0nUIVrJy0Ulca80cco8jEIBraOCTDyA6JVwLhJystKl7stngXMCwQizrEQqxuxIDIqYZVlP1TYgy0Ej0E0EQD2D3zTpWgL5bwXmxOAhPSrGAm4kUfVNNlKJT1Xnj503-WV5rnFS1V-Zzhg8YReWTHEdg56RWhX3bjg3Q6NvkepkN-l8VNWxCmeTV51-OIB7gNW64vx38gqVTQYpngtvtNddeuHwIcDW2Y43g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه های ترامپ با حاکم چین به این ترتیبه : مراسم استقبال تو تالار بزرگ خلق چهارشنبه رسیدن به پکن ، استقرار و استراحت پنج شنبه ۱۴ مه - ملاقات با شی - ضیافت دولتی با شی  جمعه تاریخ ۱۵ مه - جلسه عکس با شی- چای با شی - ناهار با شی و حرکت از پکن به آمریکا، @withyashar</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/11202" target="_blank">📅 14:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11201">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/withyashar/11201" target="_blank">📅 14:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11200">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فارس:
عبور کشتی‌های چینی از تنگۀ هرمز از شب گذشته اغاز شده
@withyashar
یک کشتی ژاپنی هم اجازه عبور گرفت</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/11200" target="_blank">📅 14:04 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
