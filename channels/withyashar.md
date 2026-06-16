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
<img src="https://cdn4.telesco.pe/file/bEiDHH-8iQI9KCUJeW3glFQxnGg2Wfgu71d4xPcJa19CSCtgAQwVcrSfciJL7bbmq2e2dezjtafjh9qrnjmPXLhVhQk2P4cXVOf_h8uJ8bnzlzQ3vg5PyF2xv-xc_OE4vf_bdwOVOlv2LbdPI4flKC6oG2xdYULSeZu-vf2WFMTF1kZNKYC1Sk-Yifhbj4TBlfuVxHjeQ5SMAxlXOSXSkcoUSJQvvFYmPttnbtDvOZP2wxKvrHb_Fbf8RjQBTfX6HeScnHt6jem9zgrnQHAqq4tbztiMtoOint3srtpjF-k-z-4sGH4Ux-IKcP2lIU6ahTQzNsqMmux3oQfDS38d7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 21:43:22</div>
<hr>

<div class="tg-post" id="msg-15087">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/withyashar/15087" target="_blank">📅 21:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15086">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شبکه ۱۳ اسرائیل: امروز یه نشست اضطراری تو دفتر بنیامین نتانیاهو برگزار میشه تا بررسی کنن چطور میشه بین جبهه ایران و لبنان تفکیک ایجاد کرد و با این شاهکار ترامپ کنار اومد.
@withyashar</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/withyashar/15086" target="_blank">📅 21:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15085">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/withyashar/15085" target="_blank">📅 21:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15084">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">@withyashar
استادیوم</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/withyashar/15084" target="_blank">📅 21:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15083">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMona</strong></div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/withyashar/15083" target="_blank">📅 21:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15082">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">@withyashar
بی‌بی و ترامپ
mma رو  گفتم wwf</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/withyashar/15082" target="_blank">📅 20:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15081">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=fxCFdm7CjfaMEDv-3S0qI2IN-nU6YxQ5Ik54MT-DhOUVrQhYHuAkZDNQAMDAjD7afd3m-d6OflO6viY61cZikkP-RY0AuZPo8DxqVsFLHI405p8yJ9ktzZd3rDqU9ZPymvWUs51vqCntJyDG-Ij0RbszHFBbh20-vHF6wmsQPxYlL4kyyECf5lG2-LFqCWqBxnqAPq9LKi5ExictsNKhszJ080dNV2bRi5PKlNr-PZPRm1x-__uR6_yvfvlkYMXx6-tTS6PWc1HsYjbzkSE7Cm6ZeXFuvx3WO8Lij5KfltR5Z4jF-1hFfGBIshA17yFoXwAjQEt32u3-_Gwqz32hxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=fxCFdm7CjfaMEDv-3S0qI2IN-nU6YxQ5Ik54MT-DhOUVrQhYHuAkZDNQAMDAjD7afd3m-d6OflO6viY61cZikkP-RY0AuZPo8DxqVsFLHI405p8yJ9ktzZd3rDqU9ZPymvWUs51vqCntJyDG-Ij0RbszHFBbh20-vHF6wmsQPxYlL4kyyECf5lG2-LFqCWqBxnqAPq9LKi5ExictsNKhszJ080dNV2bRi5PKlNr-PZPRm1x-__uR6_yvfvlkYMXx6-tTS6PWc1HsYjbzkSE7Cm6ZeXFuvx3WO8Lij5KfltR5Z4jF-1hFfGBIshA17yFoXwAjQEt32u3-_Gwqz32hxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/withyashar/15081" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15080">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from자</strong></div>
<div class="tg-text">یاشار اخبار خیلی دارن میگن که شکاف به شدت زیاد شده بین بی بی و ترامپ
به نظرت زرگریه یا واقعا ترامپ پشت اسرائیل رو خالی کرده ؟</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/withyashar/15080" target="_blank">📅 20:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15079">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شبکه ۱۲ اسرائیلی به نقل از یک منبع امنیتی:
کاهش محسوس در عملیات‌های ارتش اسرائیل در لبنان
@withyashar</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/withyashar/15079" target="_blank">📅 20:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15078">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دلار ۱۵۲،۹۰۰
@withyashar</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/withyashar/15078" target="_blank">📅 20:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15077">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/15077" target="_blank">📅 19:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15076">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJAj7Y-uZPzdiOS2O4l8fKf-gT5EVwvpwE8oq9ZPoMYtNWD8XYBiDDfye8bUo3wv0lDaO75Fhbnc7LBY0W9ud6wMopSMRetLtHJekit9p2O3XAGD2c3KSmC-X3-w4cURZ_7jvzW9ndpPHKhS4ofBeqFi5BL8yYAzRrNu5CDKurlmvbpZFZdO2hx-gwgwon5vYHtJ2i9WA9eQZVlkQNNnfMVRFA416CB5seD9liC6jVvq11syN6HQQkrqYmlboPv03UvF3lwqbFpmG6ci9InaCvnfH3B2RZQivsm4QslJm39vDY6eZVumMHtb5TaHsS6CRjWpuhel2ecF7PGMls710A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقتصاددان سابق ترامپ می‌گوید توافق ایران به معنای رونق اقتصادی بزرگ برای ایالات متحده است
@withyashar</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/15076" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15075">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUiN9yWZWeFatUDccTrH8Hby2HEE9aunJJcNlrDBFEzrnaI9fjjVrb4nVY7n2k_htvXWSfRfOCqbAHh3ABttgxvM52X21iY75wSbFvffnG2FG4I0XHSja6gAhduoA4ferQmii19spu_47VPtr3VU80ZWGkA4sJrwS2KSUSbfuD7uqLnKwHpFIaLmSfk4yjcxddGNHL4wy8EIzQ6gwzQDkdQpzE2DrLSVg0S1BAMsBceBEeV9ouWj-CY8AV8b0qMr9cuNv9NtymECy7FWZ7OITWcfLtlKKw4IY2syae3uontrbhpg1C8Kq7OtYEZRzzS3kdQC2fUF7I-ws_EElomX5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته ایلان ماسک ۱۶۵ میلیارد دلار سود کرد و ثروتش به ۱.۳ تریلیون دلار رسید
@withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/15075" target="_blank">📅 19:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15074">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نفتالی بنت، نخست وزیر سابق اسرائیل:
توافق فعلی بین جمهوری اسلامی و آمریکا فقط یک توافق موقته.
@withyashar</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/15074" target="_blank">📅 19:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15073">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ادعای وال استریت ژورنال: واشنگتن به تهران اجازه خواهد داد تا بلافاصله فروش نفت و سوخت را طبق توافق پایان جنگ آغاز کند
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/15073" target="_blank">📅 19:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15072">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دلار ۱۵۳،۵۰۰
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/15072" target="_blank">📅 19:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15071">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf74c8a754.mp4?token=U5XLBKhwsXxVyTVqNLBYHz_l-nhSZ76qmNUhJMihyboEjl3N0ZxqDgwTH3HBLoc1tr2-zdxwSMW-Xjb062-5ThKyLpP9-n-36gKVFS0ouQ6R2GrdrOTUNNBZEHbe_7E8m9YZSPotBtCQckmwGhHEHzOS5OrOPqJyjtanqfuC4p7BPdClLCRhoqE0590RliG1LsZlCwu1wvBzIA7GQYNf0gEhBHWUYJdzDkqD3rmfA0AdogiNOCuq8Yd4NtU1-o6Vfdi3sTKPjCDeqYkbuXPdnRrrQz0W9lWfzWbuE3Rf0Eqy5zw6B_1vP8Byvk3c3Uyqg0DoQ-1kOcaFoSeQ-Uz0NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf74c8a754.mp4?token=U5XLBKhwsXxVyTVqNLBYHz_l-nhSZ76qmNUhJMihyboEjl3N0ZxqDgwTH3HBLoc1tr2-zdxwSMW-Xjb062-5ThKyLpP9-n-36gKVFS0ouQ6R2GrdrOTUNNBZEHbe_7E8m9YZSPotBtCQckmwGhHEHzOS5OrOPqJyjtanqfuC4p7BPdClLCRhoqE0590RliG1LsZlCwu1wvBzIA7GQYNf0gEhBHWUYJdzDkqD3rmfA0AdogiNOCuq8Yd4NtU1-o6Vfdi3sTKPjCDeqYkbuXPdnRrrQz0W9lWfzWbuE3Rf0Eqy5zw6B_1vP8Byvk3c3Uyqg0DoQ-1kOcaFoSeQ-Uz0NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس فدرال آمریکا (FBI) در جشن تولد ترامپ، پهپادی که قصد ترور وی را در کاخ سفید داشت شناسایی و خنثی کرد!!
@withyashar</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/15071" target="_blank">📅 19:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15070">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبرگزاری وابسته به سپاه:
اسرائیل آتش‌بس در لبنان را نقض کرد.
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/15070" target="_blank">📅 19:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15069">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618d127639.mp4?token=uMLc9WCsQeuYwx2cMY3E6z6rkZnA6Dn8WbDH_jRQS5kiPdPA6iDnJNBoJDwFiy-FQODss1N6B_DcPsohmTmUQKm1cGnJCJL3tXqJM9CgWIIWTDsxxrsfHECcTKAVaG1BMQDsEi1LWi4hShprdFIMRHRj6lidZNhEI22u_BBjHbSvFkXgzVycZRDoFdRIvcfp3CYhCGMVCmTiFCZdxPUDtmU1NHLbjrYOMXLEkcCnvmQIp7RXq5XiGa_AQqZzwH3s1LDPuO4QDSUZs4jJdu_WAhLBcALVTYQW7173b0Y531u3Esk9ksJfF8nxjQ546r0GOky_TNT-x8cEj1JoRwFo-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618d127639.mp4?token=uMLc9WCsQeuYwx2cMY3E6z6rkZnA6Dn8WbDH_jRQS5kiPdPA6iDnJNBoJDwFiy-FQODss1N6B_DcPsohmTmUQKm1cGnJCJL3tXqJM9CgWIIWTDsxxrsfHECcTKAVaG1BMQDsEi1LWi4hShprdFIMRHRj6lidZNhEI22u_BBjHbSvFkXgzVycZRDoFdRIvcfp3CYhCGMVCmTiFCZdxPUDtmU1NHLbjrYOMXLEkcCnvmQIp7RXq5XiGa_AQqZzwH3s1LDPuO4QDSUZs4jJdu_WAhLBcALVTYQW7173b0Y531u3Esk9ksJfF8nxjQ546r0GOky_TNT-x8cEj1JoRwFo-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند عرزشی هم صداش در اومد
@withyashar
اینو پیدا کنین استخدام کنم اتاق جنگ سبک منو داره میره
🤣</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/15069" target="_blank">📅 18:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15068">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWwbNHii6jCndfFJLeD0ghn7SuayGxyac9SbWvsdgJ3x9qDoSOj7WivkizN1ZM4kW8Kt5uMkuu1lc2FdWDj7M-FcytQrTmMsjfJxE_ut5phcxb-p5SB4hIjKIRNC7QC-SQzSSyKOyWYOjuLNN0I8ScDYPdmc4PtzUEk94Xc6RTzO0CdIu5C96nkZ2xD1_UMUz7LUdTOroQFHCK_h6spZM4wBXgSOurFksQFLlH0MQPLGSaGksbZ0Qh_JwsBW0VbO6Tq8UlD688RgVnxKkO2KbkqOF85sovLdZwJV488S0xG37xLb7GuFH20QrNhQe553bC3eCGaW7ioL0WH07g7QKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دراپ سایت: ایران برای تحلیل رفتار ترامپ، دوتا روانشناس به تیم مذاکره کننده اضافه کرده
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/15068" target="_blank">📅 18:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15067">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/15067" target="_blank">📅 18:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15066">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">صداوسیما : همین که اول بازی پرچم ایران توی خاک آمریکا به اهتزاز در اومد یعنی ما بردیم. دیگه نتیجه بازیا خیلی مهم نیست
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/15066" target="_blank">📅 18:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15065">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4feef4c4.mp4?token=tuLMCmhwdPuxgu1tS_sOhRpFZLVWlogoOnMXPIAVaZA5K1Lxtld2Xs53JmwKaPffUeHGYBfOxNx6qMrhm0vhqvxLdx5KQeIAX38Zgg9SGiqyM2wC47N7id3Z1opZ3BUfNDs_Z29Dw9s_7x0m3gFEyiUBztmZsqLb3spT8N91roE8Ce9RhasiYS4w4p1gRANhZsF7JJzLVUKugCydkDMvnxr6EjkfVHyZ-EZv3lod9S9T-9LTk74hq0gHH8OF6otrun4bUWxVE6gxIH3j5tqHVrYj_LwXy5AWNYGS5Eladytc80fOJQATYfUMeUoXa0f8z_rtEZ7WOCSoRIw6C01RBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4feef4c4.mp4?token=tuLMCmhwdPuxgu1tS_sOhRpFZLVWlogoOnMXPIAVaZA5K1Lxtld2Xs53JmwKaPffUeHGYBfOxNx6qMrhm0vhqvxLdx5KQeIAX38Zgg9SGiqyM2wC47N7id3Z1opZ3BUfNDs_Z29Dw9s_7x0m3gFEyiUBztmZsqLb3spT8N91roE8Ce9RhasiYS4w4p1gRANhZsF7JJzLVUKugCydkDMvnxr6EjkfVHyZ-EZv3lod9S9T-9LTk74hq0gHH8OF6otrun4bUWxVE6gxIH3j5tqHVrYj_LwXy5AWNYGS5Eladytc80fOJQATYfUMeUoXa0f8z_rtEZ7WOCSoRIw6C01RBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس:
اگر مردم ایران خواهان رفاه بیشتر هستند، رهبرانشان باید پیشقدم شوند و رفتار خود را تغییر دهند.
اگر این کار را بکنند، عالی است. اگر نکنند، ایالات متحده قبلاً چیزهای زیادی به دست آورده است.
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/15065" target="_blank">📅 18:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15064">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ونس به فاکس نیوز:
ما پیروز شدیم، چه ایران روش خود را تغییر دهد و چه تصمیم بگیرد به توافق پایبند نباشد
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/15064" target="_blank">📅 18:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15063">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کانال 12 اسرائیل: اسرائیل درخواست دیدن یادداشت تفاهم بین آمریکا و ایران رو داشت اما این درخواست رد شد.
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15063" target="_blank">📅 17:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15062">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: ممکنه یه کنفرانس خبری برگزار کنم و متن یادداشت تفاهم آمریکا و ایران رو با صدای بلند و کلمه به کلمه بخونم تا رسانه‌ها اونو به درستی پوشش بدن.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15062" target="_blank">📅 17:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15061">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ: اگه لیندسی گراهام بیاد و به این توافق با ایران شک کنه و حرفی بزنه، واقعاً براش دردسر درست می‌شه و حسابی به مشکل می‌خوره.
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/15061" target="_blank">📅 16:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15060">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آکسیوس: جان رتکلیف، مدیر سیا، به دونالد ترامپ و مقام‌های ارشد آمریکا گفته ارزیابی‌های اطلاعاتی نشان می‌ده ایران احتمالا تمایل واقعی به اجرای تعهدات هسته‌ای خودش نداره.
گفته می‌شه تفاوت میان حرف‌های داخلی مقام‌های ایرانی و آنچه به مذاکره‌کنندگان آمریکایی گفتن، باعث این نگرانی شده.
مارکو روبیو، وزیر خارجه آمریکا، و پیت هگست، وزیر دفاع آمریکا، هم نگرانی مشابهی دارن.
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/15060" target="_blank">📅 15:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15059">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، سه‌شنبه 26 خرداد از اجرای حکم اعدام جواد زمانی و ابوالفضل ساعدی، دو زندانی سیاسی بازداشت‌شده در اعتراضات دی‌ماه در استان سمنان خبر داد. میزان اتهام آن‌ها را «افساد فی‌الارض از طریق کشیدن سلاح گرم و سرد در شهرستان…</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/15059" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6041510c69.mp4?token=gx6vB5WMqLYlxTxN_aCefr7jwisvOmDKTva2qh4WJV1BKe1PwCk99kyC_J9PvcaIu20nW1hIOKaftccnBxmIIjJLGrPQYq1o-ZSIZrvboE9FBOsT47mFQrBJVDTTALWAmMsVEBSk5Gu7dv7MRn3V9G960ZO1TI7zhiY5j_sUvHz7DmdnV86iUY58FQ9i2WAeXDPPCjlBfhDcClSNFlZH8vWifC7l3kJjgYSys8djy8RiNUs7q1_ZeYi4CY6-t34AAm7Ex1LH_AqxHDtoiL69yAe7jYXGagr2peo86cGb0jl2nyvMhAnkK1cFipKWl5mwc_rhmv168BErwSejNoz0Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6041510c69.mp4?token=gx6vB5WMqLYlxTxN_aCefr7jwisvOmDKTva2qh4WJV1BKe1PwCk99kyC_J9PvcaIu20nW1hIOKaftccnBxmIIjJLGrPQYq1o-ZSIZrvboE9FBOsT47mFQrBJVDTTALWAmMsVEBSk5Gu7dv7MRn3V9G960ZO1TI7zhiY5j_sUvHz7DmdnV86iUY58FQ9i2WAeXDPPCjlBfhDcClSNFlZH8vWifC7l3kJjgYSys8djy8RiNUs7q1_ZeYi4CY6-t34AAm7Ex1LH_AqxHDtoiL69yAe7jYXGagr2peo86cGb0jl2nyvMhAnkK1cFipKWl5mwc_rhmv168BErwSejNoz0Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با پراید رفته دم لانچر در حال شلیک
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/15058" target="_blank">📅 15:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15057">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خبرگزاری دولتی ایسنا:
محاصره دریایی آمریکا در حال لغو شدن است
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/15057" target="_blank">📅 15:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/563a3a2554.mp4?token=QQciIbSi7cB2xZ9Si8vqZaQZ9Pdc7JUN_yeoGVOVYUzRkn0k2ZG35h6orRuGdoWlAaeeicnvgRjTbU1eCOM36if8F_nck6C92p4t8luB5RYAg1tc1bMx26OByzZLmzqhu1x_MtIkkawS2qQI1VYfWKZFm5alv2f2QlT4oXhSDdXZs-E93MIWsqvN7dOAHDidmbKMCbSFu3f6XqOLM-yhr1TnAY6vGZFNP2FIF9Qm2VYIA26zxNS7xISj56AN6FqZ9QojOpnK3Hl18DTdb4f3AK6CfxQopTRDvFX-R0zUEnSphUDozkpPgWO4Ck_diEhSVnqyP62ybW-5PmkYNvZqUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/563a3a2554.mp4?token=QQciIbSi7cB2xZ9Si8vqZaQZ9Pdc7JUN_yeoGVOVYUzRkn0k2ZG35h6orRuGdoWlAaeeicnvgRjTbU1eCOM36if8F_nck6C92p4t8luB5RYAg1tc1bMx26OByzZLmzqhu1x_MtIkkawS2qQI1VYfWKZFm5alv2f2QlT4oXhSDdXZs-E93MIWsqvN7dOAHDidmbKMCbSFu3f6XqOLM-yhr1TnAY6vGZFNP2FIF9Qm2VYIA26zxNS7xISj56AN6FqZ9QojOpnK3Hl18DTdb4f3AK6CfxQopTRDvFX-R0zUEnSphUDozkpPgWO4Ck_diEhSVnqyP62ybW-5PmkYNvZqUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران حتی یک بار به ترکیه حمله کرد، من هرگز این را درک نکردم، هیچ‌کس آن را درک نخواهد کرد
این مشکل است، آن‌ها کاملاً غیرمنطقی هستند و اکنون آن افراد رفته‌اند، فکر می‌کنم ایران اکنون رهبری منطقی دارد!
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/15056" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش روزنامه New York Post می‌گوید که پلیس فدرال آمریکا (FBI) پنج نفر را به اتهام طراحی یک حمله به رویداد «UFC Freedom 250» در روز تولد ترامپ که در محوطه چمن جنوبی کاخ سفید برگزار شد، بازداشت کرده است. گفته می‌شود این طرح شامل استفاده از پهپادهای انفجاری، تک‌تیراندازها و همچنین تلاش برای نفوذ و شکستن دروازه‌های محل بوده است.
بر اساس این گزارش، FBI در تاریخ ۱۰ ژوئن از وجود این توطئه مطلع شده و سپس طی یک عملیات چندایالتی اقدام به بازداشت افراد کرده است. مقام‌ها می‌گویند در جریان تحقیقات، چت‌های رمزگذاری‌شده در اپلیکیشن Signal کشف شده که بیش از ۲۰ کاربر در آن‌ها حضور داشته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/15055" target="_blank">📅 15:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15054">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf2f513ca.mp4?token=bxdyI30zQsLJuygINkjT65BpaRHQru3-gjOcVg9u1n-P7jHZ3lY7JJ9LF8cmTcemli2oPr_UvSxj5BF5bGjY2jHvs9NFF6pU7hCWhNJp-GGQeKP1_F0ptExgLVsvyOOPnUbYRZEoKFc9osA6IprlWIUVaKkvIOdZZD0XMQJ2raMH8Af1eeHEfUFTfpOyzuhd6CmS5okThVRj_wKYUf0kq9QRBVHnKT7GTfJULaMh-IE-f3_NwjWKBt8gD18cxgNGchQqZFJtDc9NnFYU8BcX0DkybLfwzLVoQKo87RERXXyk2xR2OOzaFgxCjJYcdhNwxTsjGc9V61g3EvzggbTcoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf2f513ca.mp4?token=bxdyI30zQsLJuygINkjT65BpaRHQru3-gjOcVg9u1n-P7jHZ3lY7JJ9LF8cmTcemli2oPr_UvSxj5BF5bGjY2jHvs9NFF6pU7hCWhNJp-GGQeKP1_F0ptExgLVsvyOOPnUbYRZEoKFc9osA6IprlWIUVaKkvIOdZZD0XMQJ2raMH8Af1eeHEfUFTfpOyzuhd6CmS5okThVRj_wKYUf0kq9QRBVHnKT7GTfJULaMh-IE-f3_NwjWKBt8gD18cxgNGchQqZFJtDc9NnFYU8BcX0DkybLfwzLVoQKo87RERXXyk2xR2OOzaFgxCjJYcdhNwxTsjGc9V61g3EvzggbTcoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدراعظم آلمان در جی۷ پیراهن «ترامپ ۴۷» را به رئیس‌جمهور آمریکا اهدا کرد
@withyashar
خانواده دونالد ترامپ ریشه آلمانی دارند. پدربزرگ او، فریدریش ترامپ، در شهر کالشتات آلمان به دنیا آمد. او در سال ۱۸۸۵ و در شانزده سالگی از آلمان به ایالات متحده آمریکا مهاجرت کرد. پدر ترامپ، فرد ترامپ، در آمریکا متولد شده بود و شهروند آمریکا محسوب می‌شد، اما از طرف پدری کاملاً تبار آلمانی داشت. از سوی مادر نیز ترامپ ریشه اسکاتلندی دارد. مادرش، مری آن مک‌لئود ترامپ، در جزیره لوئیس در اسکاتلند به دنیا آمد و بعدها به آمریکا مهاجرت کرد</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/15054" target="_blank">📅 15:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15053">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ با انتقاد از نتانیاهو  :
لازم نیست هر بار که دنبال کسی می‌گردی، یک ساختمون آپارتمانی  خراب کنی.
تو اون خونه ها ادم های زیادی زندگی میکنن و همه عضو حزب الله نیستن
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/15053" target="_blank">📅 14:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15052">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7693c44486.mp4?token=hM9xswnAQpS6Up2A3p_9iCKZrdtPyTCbm-oXPLPmDBH8U4u14Vaz1USH6yVC0NixBlS54gW8E4cNTqzHED8S182dUuCxF56ilM3eh_JSTjgqUIwAfZAKdbYrTtiaTivtRiNjdRRhdYCGpGQLC1kEPqKJwyJtNQuQmyhId1MfL1mdMNc4o-D7PIVYr2piVHmIWkCxAWBQop5ut3hdOP4-R59qiw9e02zvUh2BF6641H8gW6eKDN4JWJYr9yAkrKWIv-tGd0sBI5jhApLpGoWVTT82tTM0d2qH5ymTE4Scpjt7euyUltYAz6wdURwRz8pVzIqWGziobadoQ4rZt6pXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7693c44486.mp4?token=hM9xswnAQpS6Up2A3p_9iCKZrdtPyTCbm-oXPLPmDBH8U4u14Vaz1USH6yVC0NixBlS54gW8E4cNTqzHED8S182dUuCxF56ilM3eh_JSTjgqUIwAfZAKdbYrTtiaTivtRiNjdRRhdYCGpGQLC1kEPqKJwyJtNQuQmyhId1MfL1mdMNc4o-D7PIVYr2piVHmIWkCxAWBQop5ut3hdOP4-R59qiw9e02zvUh2BF6641H8gW6eKDN4JWJYr9yAkrKWIv-tGd0sBI5jhApLpGoWVTT82tTM0d2qH5ymTE4Scpjt7euyUltYAz6wdURwRz8pVzIqWGziobadoQ4rZt6pXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : اگر رژیم ایران به کشتن مردم خودش ادامه دهد، آیا شما همچنان این معامله را پیش خواهید برد؟
ترامپ: ما با آنها در این باره صحبت کردیم. بیشتر این اتفاقات در دوران رژیم اول و دوم رخ داده است، بسیار بیشتر از الان.
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/15052" target="_blank">📅 14:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15051">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرگزاری msn
: ترامپ و کنگره به هگسث و روبیو اعلام کرده‌اند اگر با توافق با ایران مخالفت کنند ، از سمت خود برکنار خواهند ‌شد
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15051" target="_blank">📅 14:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15050">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ: جنگ لبنان مسئله فرعی است و توافق هسته‌ای با ایران می‌تواند پابرجا بماند.
به اسرائیل گفتم که از حمله آنها به بیروت خوشم نیامد
من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد
من از نتانیاهو ناامید نیستم. ما رابطه بسیار خوبی داریم
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/15050" target="_blank">📅 13:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15049">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: من به تغییر رژیم اعتقاد ندارم. سال‌هاست که تغییر رژیم‌ها را دیده‌ام و هیچ‌وقت نتیجه نمی‌دهند!
فکر می‌کنم توافق با ایران عادلانه است
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/15049" target="_blank">📅 13:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15048">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ:
می‌خواهیم اورانیوم غنی‌شده را از ایران بگیریم
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/15048" target="_blank">📅 13:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15047">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ: ما می‌خواستیم برای دریافت اورانیوم غنی‌شده به ایران برویم، اما این اتفاق نیفتاد.
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/15047" target="_blank">📅 13:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15046">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ: تلاش‌هایی برای تغییر رژیم در ایران صورت گرفت، اما موفق نشدند.
چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، اطمینان از این بود که ایران سلاح هسته‌ای نداشته باشد.
اگر ایران به دنبال دستیابی به سلاح هسته‌ای باشد، جهنمی به پا خواهد شد.
ما از نحوه مدیریت امور توسط قطر در طول بحران اخیر، احساس خوشحالی و احترام می‌کنیم.
توافق با ایران به مرحله دوم منتقل می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/15046" target="_blank">📅 13:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15045">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5d35b80d.mp4?token=Tu10q_-lS09FowF0CLQl8n5b0i4GvoUL3J4lj3K2_MkwSyewcVCMDKM5TOEug3hhEQYtSnjSAorYVqbwXLKCmZkARDoes_07FVUzGpoPTcGKq09uqbC7c0O_yW5P4Hy-LPuuZAFlmBz-XcEIyGAM4HftOb_xjSsY10_0lX4n6p0-CBWEYZZazoLrPWjxLSxn79L1gOum6U47AZvHUG7ahufOGJubcjjPMheWxEcUipixvFsNZEBgFf00i4udBQwS59vY69g9R2eI_xTG3WIoLBWrKddY0C1XT-Zz1IIEVkz8kY5LfF1fg6nLcbsX0VfFR6M9JOlPq-g53d_PwH3pBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5d35b80d.mp4?token=Tu10q_-lS09FowF0CLQl8n5b0i4GvoUL3J4lj3K2_MkwSyewcVCMDKM5TOEug3hhEQYtSnjSAorYVqbwXLKCmZkARDoes_07FVUzGpoPTcGKq09uqbC7c0O_yW5P4Hy-LPuuZAFlmBz-XcEIyGAM4HftOb_xjSsY10_0lX4n6p0-CBWEYZZazoLrPWjxLSxn79L1gOum6U47AZvHUG7ahufOGJubcjjPMheWxEcUipixvFsNZEBgFf00i4udBQwS59vY69g9R2eI_xTG3WIoLBWrKddY0C1XT-Zz1IIEVkz8kY5LfF1fg6nLcbsX0VfFR6M9JOlPq-g53d_PwH3pBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ما هیچ پولی در ایران سرمایه‌گذاری نمی‌کنیم، راستی. دیروز شایعه‌ای پخش شد. مضحک بود.
ما حق داریم روزی وارد شویم و اگر من بخواهم کاری انجام دهم یا کسی بخواهد کاری انجام دهد، اما ما هیچ پولی سرمایه‌گذاری نمی‌کنیم.
ما هیچ تعهدی برای سرمایه‌گذاری پول در ایران نداریم.
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15045" target="_blank">📅 13:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15044">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ: ما هیچ پولی در ایران سرمایه‌گذاری نخواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/15044" target="_blank">📅 13:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15043">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، سه‌شنبه 26 خرداد از اجرای حکم اعدام جواد زمانی و ابوالفضل ساعدی، دو زندانی سیاسی بازداشت‌شده در اعتراضات دی‌ماه در استان سمنان خبر داد. میزان اتهام آن‌ها را «افساد فی‌الارض از طریق کشیدن سلاح گرم و سرد در شهرستان شاهرود» اعلام کرد
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15043" target="_blank">📅 13:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ویس میلیارد دلاری ۲
💰
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/15042" target="_blank">📅 13:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15041">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ویس میلیارد دلاری
💰
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15041" target="_blank">📅 12:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15040">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/15040" target="_blank">📅 12:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15039">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/15039" target="_blank">📅 12:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15038">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3Z_ehBNzKylUTxFEd2fq3iTrbNwRkIQdh5PLaoa0H_u0CUcZJeGQMk__GcRsCuB7wQ9BoyYhdPbrfk4a11gbLlfg0Rro8tD_RZxUrbfRvSi8Foo2UPL8u07Da8Lq5SOvNw8PTkC3G6rV8-nWaNp-AvHHi0ig9hJ3BVr_U_HphLB9qeW_dF8VtREq9fIGbMrx_fiAOUBzKci3WEHD8qzVMO90h9y4WD2h2bGkCjo_9K6Q4R1GKBhvQ1DaLVrrnZuVf9DeahJbr7lKWtLtCHSlcxVaFMHmyzEIu8GqIe2_mNsZL9tPaZiNGCDuZ3hIOEAxJD39faJ70nWRbzmNFEu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی پیش اهواز چیزی نیست کباب‌میزنند
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/15038" target="_blank">📅 12:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15037">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/15037" target="_blank">📅 12:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15036">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ارسالی</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/15036" target="_blank">📅 12:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15035">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/15035" target="_blank">📅 12:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15034">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چپقچی: در سوییس پس از اینکه مسئله امضا ( تفاهمنامه پاکستان) انجام شد، مذاکرات شروع خواهد.
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/15034" target="_blank">📅 12:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15033">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcV5sNWzq6YQURNmRIZr2SJZlyLz3YCqc8ouHZU-oAfVRAzHCt5eVV8jpwxoGE_Oyy9V3O1jxQrdZcKS71Vt2a3NhenX8r6KWEYAElPEkg3XgdJWxUhccoTobLvuNkUAtLbehOEn4_kCPkqHL_zI2zIKTqfQ1yuDsZW4gIo03Xhy_MrNxR2TyQDLm90-Qoiu_2WwAUapCSqXtVKtc4KHNzY0_Xej944kFMeSXXvBcem7_GZTbauRvpe8NT5YtZQQzAt0hPG_Z_pvzFL5pulUgX97TE5v2RmVg9hI9lIjBhV8KZbnbzOu448YYXjsYODBfb-kyU12wYWwlCMpEOpXww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای روزنامه همشهری از متن و مفاد توافق
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/15033" target="_blank">📅 12:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15032">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">عراقچی: هرگونه حمله نظامی اسرائیل به لبنان ، نقض یادداشت تفاهم محسوب می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/15032" target="_blank">📅 12:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15031">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کیهان: معنای سکوت رهبری درباره هسته‌ای این است که دیگر مذاکره‌ای در کار نیست
@withyashar
روزنامه کیهان وابسته به اصولگرایان تندرو نزدیک به بیت رهبری است و مدیر مسئول آن مستقیماً توسط علی خامنه‌ای انتخاب شده .</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/15031" target="_blank">📅 11:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15030">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3bf6e0591.mp4?token=StC0Hx2BWqZfs6Ezbldg6hw3ydWD2xUu10ha0c9dd8udgSZyuK4WZtV8jP759r354axpFTXoX6SNUBbXRnIyryn9KwXJu8COzy6_2vCqKqu-sfM2_zdOp1OqUkM-Gh5gueJU-VFxD2N96h5ZhfIJGxLuq2FztWvWS2Palq-fC4xf2tlQqcvHEJw2VSbtMk1DMptdFLnmYhk-Rywav3ZoKqGgQKQT-ctRPDbg3tCxnjCgx_nNnbU9Ah4ddNSpcg7CoHO6cN6t5jnlkxAGx_eRVCJjdnZDx2IjBAOyfz60rPIur-qyL2T_R4zNYM96tG8mmRbTVOzGrIMvqOiKwFX8pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3bf6e0591.mp4?token=StC0Hx2BWqZfs6Ezbldg6hw3ydWD2xUu10ha0c9dd8udgSZyuK4WZtV8jP759r354axpFTXoX6SNUBbXRnIyryn9KwXJu8COzy6_2vCqKqu-sfM2_zdOp1OqUkM-Gh5gueJU-VFxD2N96h5ZhfIJGxLuq2FztWvWS2Palq-fC4xf2tlQqcvHEJw2VSbtMk1DMptdFLnmYhk-Rywav3ZoKqGgQKQT-ctRPDbg3tCxnjCgx_nNnbU9Ah4ddNSpcg7CoHO6cN6t5jnlkxAGx_eRVCJjdnZDx2IjBAOyfz60rPIur-qyL2T_R4zNYM96tG8mmRbTVOzGrIMvqOiKwFX8pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبی بعد از  زدن گل دوم، با نشان دادن اسلحه و شلیک نمادین به تماشاگران نشون داد این تیم مزدوران حکومتیه نه مردم ایران
این نفهمی او واکنشمنفی‌ در‌
رسانه های جهان داشته
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/15030" target="_blank">📅 11:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15029">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دونالد ترامپ در گفتگو با CBS در واکنش به سفر کاروان تیم فوتبال ایران به آمریکا گفت:
"افتخار میزبانی کاروان تیم فوتبال ایران را داریم. آنها تیمی بزرگ هستند.
به قلعه نوعی گفتم اگر اینجا جایی نداری شب بمانی به منزل ما بیا. شاید قبول کرد. شاید هم نکرد. باید ببینیم چه می‌شود"
@withyashar
.
😂
شوخیه</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/15029" target="_blank">📅 10:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15028">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ویزای مهدی ترابی باطل شد
در حالی که برای بازیکنان تیم ملی برای سفر به آمریکا روادید «چند بار ورود» صادر شده است اما ویزای مهدی ترابی تنها برای یک بار ورود اعتبار داشت و پس از سفر تیم ملی به لس آنجلس جهت دیدار برابر نیوزیلند و پایان این بازی، اکنون ویزای این بازیکن منقضی شده است.
فدراسیون فوتبال ایران برای اخذ مجدد ویزای ترابی اقدام کرده تا این بازیکن بتواند در دیدارهای آتی تیم ملی را همراهی کند.
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/15028" target="_blank">📅 10:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15027">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یک بمب‌افکن B-52 استراتوفورتراس نیروی هوایی ایالات متحده بلافاصله پس از برخاستن در پایگاه نیروی هوایی ادواردز سقوط کرد.    جزئیات تلفات هنوز گزارش نشده است. @withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/15027" target="_blank">📅 10:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15026">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ونس: ترامپ ممکن است که پیش از روز جمعه، جزئیات توافق با ایران را فاش کند
جی‌دی ونس، معاون رئیس‌جمهور آمریکا اظهار داشت که رئیس‌جمهور دونالد ترامپ ممکن است تصمیم بگیرد پیش از روز جمعه جزئیات توافق با ایران را منتشر کند
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/15026" target="_blank">📅 09:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15025">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">امکان پلاک‌گذاری خودروهای بالای ۲۵۰۰ سی‌سی در مناطق آزاد فراهم شد
معاونت حقوقی ریاست‌جمهوری در نامه‌ای به دبیر شورای عالی مناطق آزاد از امکان شماره‌گذاری ملی خودروهای وارداتی بالای ۲۵۰۰ سی‌سی موجود از قبل در این مناطق خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/15025" target="_blank">📅 09:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15024">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Feb-BcFQr3mdZNT8KDJQtj_WuR8ILus-L9BA_r8CUCC3CIEUm_JrR8-lEGiH2ie9PRhKGwCh6ypMoF7pmdWDtRSIlSTxJR4RmuNqCtxfRsDB_rlxgJ3UDXeULm38MWfXoROinhj2k7stOtPC_3DpyWL5fEQuZNXMXGqRSF4IMuAZGcM1gRw66jqyfOL7W9Zi9TIbzUU1jbh2K6eBCn3g4KnP4S82YKG12RL9BMgUeAWAMRxdQmpXL5JuVJ7wDmB0wKRUlh1jtK5z8An2aYMyoxJfyuV5S5cHwOsJwLMFdUS6o2k8PDdkPysbAlk5eYLQtp2AGJj-14e-2Smt9qhSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندین بار در جریان بازی مسابقه امروز تیم نیوزلند و تیم ملی در صدا و سیما پرچم شیر و خورشید به نمایش درآمد.
کارگردان فیفا تا حد ممکن در حال سانسور صدا و تصویر (شامل هو کردن و پرچم شیر و خورشید) بود. از طرفی تعدادی از پرچم‌ها هم با نزدیک شدن به پایان بازی توسط نیروهای امنیتی جمع‌‌آوری شدند.
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/15024" target="_blank">📅 09:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15023">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a672a698ff.mp4?token=hjD703acTkkVC2kQuNz5_OeZoAb17EaaKfvku16z2RYbGkJRBaPSoM1cf8Vv4f_KwrnH-WMP4bMW7zomWaLn3aTfnWrxG8zi2nEoBIKZ-2IOapLNFLA_pxbXe0z314PtalQFKppxWJl5uJ_cedMSLqLIimp9kOzvypu1Di05Zi3qCADIusLPIa-zqyOdBhPbDom4jCxCrXDlTbgU_u6QFh6MI7G__Lduo-JabGvBbKiUmOGTJoru3cNM08LfvYoW9EYYNKtRu6lqWcm2gedfdBMtCB5vJwP0nIh-D9MKxOqrgl-34HcfFxkuXgbwCjkC9_-yQ-p7BRyOUanVPitmIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a672a698ff.mp4?token=hjD703acTkkVC2kQuNz5_OeZoAb17EaaKfvku16z2RYbGkJRBaPSoM1cf8Vv4f_KwrnH-WMP4bMW7zomWaLn3aTfnWrxG8zi2nEoBIKZ-2IOapLNFLA_pxbXe0z314PtalQFKppxWJl5uJ_cedMSLqLIimp9kOzvypu1Di05Zi3qCADIusLPIa-zqyOdBhPbDom4jCxCrXDlTbgU_u6QFh6MI7G__Lduo-JabGvBbKiUmOGTJoru3cNM08LfvYoW9EYYNKtRu6lqWcm2gedfdBMtCB5vJwP0nIh-D9MKxOqrgl-34HcfFxkuXgbwCjkC9_-yQ-p7BRyOUanVPitmIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">7’—Iran 0-1 New Zealand
32’—Iran 1-1 New Zealand
54’—Iran 1-2 New Zealand
64’—Iran 2-2 New Zealand
گلهای بازی و تساوی ۲-۲
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/15023" target="_blank">📅 09:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15022">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ecb9fedcf.mp4?token=K4zJKQcxgR2qyWclwm1z4oKXeRPmXzrst5XseNSZUzlZcKzHIuvAMspfDwDHdYWVubGHBnHPeb20TMr6PLzH1GbdxSBeCSpAOvBnRUvVUEwT6qhrvDVIpQVkErvVefh5YeYnQjsH_R-e0k8YmpR45KQ1SELIq_bxNJWlLZ84yDjsItPVOajNY4sT3BHKWwxQsQc_oQENTl69BhmTR44Rbfx1mATuilmMoXFKjAqzHJj-4Ph25b37XpMegRd17Gm-t6rxLI1EQZ0rbZBN7o36YCGnt7JI1LE2HCWc_jSMwy6gMiK89FiubSVRf-bRAnFSlWgXh9zLH1lx8ZGfgOYu5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ecb9fedcf.mp4?token=K4zJKQcxgR2qyWclwm1z4oKXeRPmXzrst5XseNSZUzlZcKzHIuvAMspfDwDHdYWVubGHBnHPeb20TMr6PLzH1GbdxSBeCSpAOvBnRUvVUEwT6qhrvDVIpQVkErvVefh5YeYnQjsH_R-e0k8YmpR45KQ1SELIq_bxNJWlLZ84yDjsItPVOajNY4sT3BHKWwxQsQc_oQENTl69BhmTR44Rbfx1mATuilmMoXFKjAqzHJj-4Ph25b37XpMegRd17Gm-t6rxLI1EQZ0rbZBN7o36YCGnt7JI1LE2HCWc_jSMwy6gMiK89FiubSVRf-bRAnFSlWgXh9zLH1lx8ZGfgOYu5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج مکزیکی بازی ایران نیوزلند
@withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/15022" target="_blank">📅 09:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15020">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SM9YLyDW7U3NhXL615RTC8kLWphOVwaWDqALe8UAtEFxnLK39ZjytTRAvWV-PoV6KBL0SvrZaVU4kg7xX6Wy_xz73XrSUAwK6ZhbijysDj4BXvKCo9mMGIK75Nd_a9xykSa2WVjq3lHdDNGxeyFPUGoqUFwg05zwifNgDFcZCAgHnxjNYjhol_c_xCA5rFQFd8S4ydlUPuemzDuvLPGhWSfQWfd-Ygp2jVCCOFog4SHbHM0Qe8JqxUU2LMqWOxdUREISGmevtEoMjaF2xkfJHc0c1juSaL_ziXWJ1fdWT3k7bO0Xdaijxfwe7Vjgp559hiyh6Az5XxOIVBTz1nhHyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :ایران موافقت کرده است که هرگز سلاح هسته‌ای نداشته باشد! همچنین داستان اینکه آمریکا به ایران ۳۰۰ میلیون دلار می‌پردازد، خبری جعلی است که توسط دموکرات‌ها منتشر می‌شود!!! رئیس‌جمهور دونالد ج. ترامپ
@withyashar
فقط این ۳۰۰ میلیارد بود که میلیون نوشته</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/15020" target="_blank">📅 09:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15019">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769eece9da.mp4?token=erwP53sAI_HVnNNcqdGHh7WmwKxGJmYBcEpiculCXjffdkomySFay3Ev03ItJ30Nh_JvXwZ-uBn5PnDQbWid6lLpvPjkboBkN5pqngKO7LG4CAAfkbZkWJ0S-PLHeDB_MOdP0tRrFsz5aksw1YzC3RKDeS1CE5zo8BedTp8q-LGTAltqEjdGjRSNkgpQZViDSLELWTd3WPkL0ADBjmdcQUe1rkuQ3hqxgYK-1bGFazaS-bePCzM5L6ugtIrqiEHDsFIR7_Fhwb6K8vYswIxbPshKn6xLc5JZZg9URyCDu8uBPfcBcITCMGkKuLxbc4q6YhZWmn1i3S8jNQ1AwjbosQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769eece9da.mp4?token=erwP53sAI_HVnNNcqdGHh7WmwKxGJmYBcEpiculCXjffdkomySFay3Ev03ItJ30Nh_JvXwZ-uBn5PnDQbWid6lLpvPjkboBkN5pqngKO7LG4CAAfkbZkWJ0S-PLHeDB_MOdP0tRrFsz5aksw1YzC3RKDeS1CE5zo8BedTp8q-LGTAltqEjdGjRSNkgpQZViDSLELWTd3WPkL0ADBjmdcQUe1rkuQ3hqxgYK-1bGFazaS-bePCzM5L6ugtIrqiEHDsFIR7_Fhwb6K8vYswIxbPshKn6xLc5JZZg9URyCDu8uBPfcBcITCMGkKuLxbc4q6YhZWmn1i3S8jNQ1AwjbosQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس : هیچ دلار تخفیف تحریمی یا پول بلوکه‌شده‌ای، نه از آمریکا و نه از هیچ‌کدوم از متحدای ما تو خلیج، آزاد نشده
این امتیاز فقط وقتی بهشون داده میشه که به تعهداتشون تو توافق عمل کنن
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/15019" target="_blank">📅 01:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15018">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پرس تی وی: ۳ نفتکش و ۲ کشتی با کالای ایران از محاصره دریایی عبور کرد
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/15018" target="_blank">📅 00:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15017">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">@withyashar
تحلیل وضعیت</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/15017" target="_blank">📅 00:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15016">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU0ZaKiMKKZ4hDVtW8nyrW2JJl7eyit2z953nBrL9o5CXNOKpD8Y5n13GDRI8eMA3xYpiKmDV5Innp2vLiloE07ycR1Y1Pt76E6y5J7wQ81XMRpyi-BgmFxhP_gKnetUnJE4lbm7gO-dz0ErFfRrMwgsduAfB3KvRXlFCU2RxrsVDyrhilyX1QGrZWV2fKGDAfmmcD7ied2x05Q2fO-Mqv9GuiEVuaB-nbiApLzooqpPbsQ9xXyjo1K2SgMK1WcsM9lVJABd6x71wnErohw8Z8xF1893Gu9jSd7oFmcbEtsabzT_B4l-HuENmSWJOSLpxgrr8cfSmxHPPA36NzpV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قشم  سمت سوزا همین الان خیابون اصلی
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/15016" target="_blank">📅 00:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15015">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">صدای توافق از قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/15015" target="_blank">📅 00:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15014">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEPsLkFq5GYwYA4J1VILKz339kTklRw_9CFLl92NiyLg7O8sGlkOlPqk1DEK22IdHGZ-PiHgK-VHSg62D-bQleqlLj5AsSeExJWxfNaJPktaA0CcYyGG_Eo55mAh6E1jFGYiQR6Vn19eRRKAl4omyoaKjvipriZ4onL_wMq9dqBbKlBUTHJNIgF4osWniE94VYeeLK-X1ebsROPnW-71EMZg2HfVkcTyjDF1dhOi7TKA4nZ91ZHwcct-JSeAMpY_QCAwU2E0d9OvvTqq15dw9LdG7fe999X6an9vIwgBu7aprRevyfitef_i4uS1olv00vLsN6yvIimXAP-WUl3Uxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
توافق یا عملیات فریب برای حمله وحشتناک امریکا و اسرائیل!
⭕️
مشاهده تحلیل
🇮🇱
🇺🇸
🇮🇷
👇
https://t.me/+hLt81qXCGTQzOWQ0
https://t.me/+hLt81qXCGTQzOWQ0</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/15014" target="_blank">📅 00:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15013">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/15013" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15012">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کانال ۱۴ اسرائیل: تعجب جامعه اسرائیل از این بود که مقامات ایران قبل از دفن علی خامنه‌ای با قاتلینش توافق کردند
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/15012" target="_blank">📅 23:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15011">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/15011" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15010">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عراقچی: جمعه در سوئیس تفاهم امضا می‌شود و پس از آن اولین دور مذاکرات بعدی را خواهیم داشت
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/15010" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15009">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نیویورک تایمز گزارش داد که ممنوعیت ورود پرچم‌های شیروخورشید ایران به جام جهانی که از سوی فیفا اعمال شده بود، پس از برگزاری یک جلسه اضطراری دادگاه در لس‌آنجلس در روز دوشنبه تایید شد و قاضی کرتیس ای. کین حکم داد که این ممنوعیت به قوت خود باقی بماند.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/15009" target="_blank">📅 23:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15008">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76cd0f1e71.mp4?token=qUuj-NvhGyu8wjZyGEqZpUsO8KVeR-0vjA6WPr8zRGESMeDpXqJY2AZgK0xJ5gB04Pd9vXuznNVoZIahPZYgBCSXVLu4p_F1TwMNBVV-j0yywoY6oq0PvAigVxyxGWDJhHtSAHsORu5-keEAKpML2aNJxaASQ0yfePnoMr8VQtTgzL0b4n_4AD2UZcDed0R39cy6Mw0KS4TEkdxYijB3wy8h3Gdvw_Cn2tewmMQm5fz-9axOrK7qS-bOKhqm5wvt-13Pd84Jd8T293yK8l5qf3x26n21Ef_TYC5ifsBT588g9PzO-Rp3mdF-pj_Q8NsOpfwkcSRQ30h6ordKuV9ipA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76cd0f1e71.mp4?token=qUuj-NvhGyu8wjZyGEqZpUsO8KVeR-0vjA6WPr8zRGESMeDpXqJY2AZgK0xJ5gB04Pd9vXuznNVoZIahPZYgBCSXVLu4p_F1TwMNBVV-j0yywoY6oq0PvAigVxyxGWDJhHtSAHsORu5-keEAKpML2aNJxaASQ0yfePnoMr8VQtTgzL0b4n_4AD2UZcDed0R39cy6Mw0KS4TEkdxYijB3wy8h3Gdvw_Cn2tewmMQm5fz-9axOrK7qS-bOKhqm5wvt-13Pd84Jd8T293yK8l5qf3x26n21Ef_TYC5ifsBT588g9PzO-Rp3mdF-pj_Q8NsOpfwkcSRQ30h6ordKuV9ipA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از محل سقوط بمب‌افکن استراتژیک B-۵۲ آمریکا در کالیفرنیا
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/15008" target="_blank">📅 23:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15007">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bk3oYZOeetM-pGcvf8OJzUlFKzdbK69scCIRiT1v6giAaxCWuzw7TdlVyHDcLb23ZCROpVAAmJLpPvSpfDIVMl514i2uom5uS-rnM7xoKKInegJ9iqAkygI2W8bnRn1d3Jkefvx07T1KK9ie_cq4QsbZ0WfT5ZDYEV-VwYUrvVpftnvpFIAKC7S687QM0pCVEPTshX5eBbVZzuA3WUOurMrBcGmxoZumDMPUzv5pzBeTW6idvlxjGyl5aj256ji9P_NYopU4CMagunfEB3J-DCqBzmRNuIdX68n2Mja5tHOe19ISTwqOEUKlwTq1ajxelO-TXp-5a6-mr0EtGhcETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک بمب‌افکن B-52 استراتوفورتراس نیروی هوایی ایالات متحده بلافاصله پس از برخاستن در پایگاه نیروی هوایی ادواردز سقوط کرد.
جزئیات تلفات هنوز گزارش نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/15007" target="_blank">📅 22:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15006">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoji pers</strong></div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/15006" target="_blank">📅 22:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15005">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به ارتفاعات علی‌الطاهر در نبطیه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/15005" target="_blank">📅 22:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15004">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/15004" target="_blank">📅 22:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15003">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پست جدید که در اون هنرنمایی هم کردم براتون کلیک کنید و حتماً کارهای اداریش رو انجام بدید.
https://www.instagram.com/reel/DZngOTKRtYt/?igsh=MWwzcTZmaW9oZndxcQ==
⁨ اتاق جنگ با یاشار : سفر قاهره «ملودیک»⁩</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/15003" target="_blank">📅 22:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15002">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نتانیاهو: از موارد مورد توافق بین ایران و آمریکا مطمئن نیستم ولی قطعا در انتخابات پیروز خواهم شد
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/15002" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15001">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6-x-O7vApb0d4RED4XBpTKQ56eRupP1AiJgHVgs2kwVb7HBJKOd3x42cdADDuVu75shY8OGpp9yGgpTaLuJ8tTA6pWeqh89SjObsJCIZJgXU9rHnMuD1tAbgLMaEJORqu0wA-OTvcC631yyzxukTk4V1dumW1OHbvpX4qjaYlwZbgWbiGVJTyJNxs7GJOYk57QPRL2opiSDUbzptum0O6BNsRWpjBFg1b2qKPrpnwGgn9mcncSL4loIgqvyzF3aX7JhZ4nJwjeIFT_FLpMf4jDaZSdy6fGp9_yel-62Lng8h-x6aIG2RYe7FkrhOxSzCXV6QqsS5uKXtKENCxff7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15001" target="_blank">📅 22:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15000">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نتانیاهو: تا خلع سلاح حزب‌الله، اسرائیل از منطقه امنیتی جنوب لبنان خارج نخواهد شد.
همون کاری با غزه کردیم، با جنوب لبنان هم خواهیم کرد؛ همونطور که غزه دیگر تهدید جدی‌ای برای اسرائیل نیست، حزب‌الله هم در آینده نخواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/15000" target="_blank">📅 22:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14999">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتانیاهو: توافق با ایران توسط ترامپ منعقد شد، این تصمیم اوست و ما منافع خود را داریم‌‌
ترامپ رئیس‌جمهور آمریکاست و من نخست‌وزیر اسرائیل؛ من از منافع کشور خودم دفاع می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14999" target="_blank">📅 21:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14998">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نتانیاهو: من نگفتم هدف ما سرنگونی رژیم ایرانه، گفتم میخواهیم به مردم ایران برای انجام این کار کمک کنیم
@withyashar
یاشار : توجه کن این جمله بار حقوقی داره با این حال بنیامین نتانیاهو بارها این حرف رو زده</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/14998" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14997">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نتانیاهو
: مبارزه تمام نشده است. ما باید همچنان هوشیار، قوی و مصمم باشیم تا از خود تا حد امکان دفاع کنیم. این نه تنها در مورد ایران، بلکه در مورد بازوهای تروریستی ایران نیز صادق است. ما به شیوه‌ای بی‌سابقه به آنها ضربه زدیم. ما این کار را در غزه، لبنان، سوریه، یمن، اردوگاه‌های پناهندگان در یهودا و سامره و همه جا انجام دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/14997" target="_blank">📅 21:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14996">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نتانیاهو: من با ترامپ موافق نیستم،
بنابراین، اسرائیل هر کاری که لازم باشد در برابر ایران انجام خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14996" target="_blank">📅 21:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14995">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شبکه ۱۳ اسرائیل به نقل از یک منبع:
تل‌آویو و واشینگتن بر سر عدم عقب‌نشینی کامل اسرائیل از لبنان به توافق رسیده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/14995" target="_blank">📅 21:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14994">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecbac886c1.mp4?token=uY94aszmMdPXrMDVjXVXGfYfx1r9U6vS7Cfrw9ZSKo2KkBExXfSQyRQzYG9C0wFAXNeUxiiDxFjSY1-Ddklvwh7p4a-dQcFdZ2mff4ACFSK5u5Zv6PPpo837oZSntRWhdnItdLhhy7ctTHXSqh5nJXrC31l_MbUh9-9dYtRGUmzDjBHGrw3RAHndePVqEx_K-l9OQIMiNRDJJVl8yIhRMNA6HSVSezYEFBrwUh2PKL6YRft53ObPWebsli3k64-GPGkh_t2B32VusHac3J-cIn67c4lecx8RB1xbu7taX1RKf120QM3VPgJKs45-Vn8SJqjr7V0I7BJ3snG5gH7CoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecbac886c1.mp4?token=uY94aszmMdPXrMDVjXVXGfYfx1r9U6vS7Cfrw9ZSKo2KkBExXfSQyRQzYG9C0wFAXNeUxiiDxFjSY1-Ddklvwh7p4a-dQcFdZ2mff4ACFSK5u5Zv6PPpo837oZSntRWhdnItdLhhy7ctTHXSqh5nJXrC31l_MbUh9-9dYtRGUmzDjBHGrw3RAHndePVqEx_K-l9OQIMiNRDJJVl8yIhRMNA6HSVSezYEFBrwUh2PKL6YRft53ObPWebsli3k64-GPGkh_t2B32VusHac3J-cIn67c4lecx8RB1xbu7taX1RKf120QM3VPgJKs45-Vn8SJqjr7V0I7BJ3snG5gH7CoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:  ما در لبنان خواهیم ماند. کار با ایران ممکن است همچنان تمام نشده باشد
ماموریت زندگی من مبارزه با برنامه هسته ای ایران است.
با توافق یا بدون توافق، ایران سلاح هسته ای نخواهد داشت.
اگر برای حمله به ایران عجله نکرده بودیم، به بمب هسته ای دست می یافت.
ما رهبران ایران را کشتیم، به سرویس‌های امنیتی آن آسیب شدیدی زدیم و اسرائیل را از تهدید هسته‌ای ایران نجات دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/14994" target="_blank">📅 21:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14993">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نتانیاهو: ما خسارات عظیمی به ایرانی‌ها وارد کردیم و اسرائیل را از خطر نابودی هسته‌ای نجات دادیم.
اگر ما به سرعت برای حمله به ایران اقدام نمی‌کردیم، این کشور به بمب هسته‌ای دست پیدا می‌کرد.
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/14993" target="_blank">📅 21:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14992">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتانیاهو: «اسرائیل تا هر زمان که لازم باشد در “مناطق امنیتی” باقی خواهد ماند.»
«ما شراکت‌های جدیدی را در سراسر منطقه و فراتر از آن شکل خواهیم داد، در حالی که توانایی اسرائیل برای تولید و تأمین مستقل تسلیحات خود را تضمین می‌کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/14992" target="_blank">📅 21:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14991">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/14991" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14989">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مقامات آمریکایی اعلام کردن حتی با وجود توافق قصد عقب نشینی از منطقه را نخواهیم داشت و نیروهای آمریکایی در منطقه خواهند ماند.
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/14989" target="_blank">📅 21:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14988">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14988" target="_blank">📅 21:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14987">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کانال ۱۳ به نقل از یک مقام اسرائیلی:
ما از لبنان عقب‌نشینی نخواهیم کرد، اما از این پس هر عملیات نظامی قابل بررسی خواهد بود.
ما برای دستیابی به توافق بین واشنگتن و تهران قربانی شدیم.
معاون رئیس جمهور آمریکا از نتانیاهو خواسته است تا حضور اسرائیل در لبنان را کاهش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14987" target="_blank">📅 21:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14986">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نتانیاهو: می‌توانید طناب را با آمریکایی‌ها بکشید، اما نباید آن را پاره کنید.
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/14986" target="_blank">📅 21:01 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
