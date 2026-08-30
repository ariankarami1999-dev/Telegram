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
<img src="https://cdn4.telesco.pe/file/SgUfEcR3shLhuSwninn-34iOUl9mK5wKS_vUSoWP2bc_L2sa8XUuUN2fVWx4Tw1wylhm1s4xRWB1NrwpBSNubVYjyffUklrr9Uh62Gr2HX2Jz0Y4Xff2PT6pR4TJIizSSpV7HD3PsEIEiZkz2qfcIpFf-UZwlmI1xYjz-3RAIVD_paqDFWYxFzz1r9shUowHePLg4mYIHcSbhbnSXZo6AQhRjCVhRTMhs71g3ppbV6q5XHAPrUKRd9DW5J5_ts1t8FX7ycmHnTnk-hbkHJw7IaqIo7m270fgCHz2Syq-GrRout5zbrzgEKw2uNkBaVYIsDRGXuERh36N_s1bI2TYhw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 631K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 06:08:05</div>
<hr>

<div class="tg-post" id="msg-28712">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFEd9JZNugjNz0N3SwCjEkxoyso8SLYSHXAyRxygAsTNixgcLUgtJP_fuaHFUSsYqeQpZTt_M6vdKrWVaoOrWCWEF2UZ13usWhbu7IjXA9LFe7gf6XXw_vQzB8-PVLXbPLhEUTOq3Xy1v3FMwS9iweURNYFB2tgMVtBtkDFHc1p3t2x3OtqVelKg10qT-4EZNUujaeOp2cMVL8YjdQvRNmsJRV2y3h9Losr36OXnqljHZKqKLcWaGydAs9JYB30va2FXdYUYX5pIa6qLCZHchveGz1gZxWysxiVVXJ0qrwQJEo5YAAqvyN20gIY1rbcvBJ24HMvdDZceyMP-c1FYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛اسپورت: دو تیم اینترمیلان و بارسا در حال مذاکره هستند تا برسر معاوضه فدریکو دیمارکو و الخاندرو بالده در روزهای پایانی نقل و انتقالات به توافق نهایی برسند و این جابجایی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/28712" target="_blank">📅 01:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28710">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1-St23F9VOy-7mVh6G94EmqPM1xDNn7df4K05dXN025ZpaHz7eToYV4j-HeKkEvlkBQjYT5RokyGCQAxJbKo1LEjM1llXXrLQVvlsjxO6IVHB0fSL4y1lMH7xazsrGJx1VZpJKnttj-q6LEButYLuxsf2Xa2cy6ebI5_2Aa66HABh_EOVtib-5mH_6wmxI-BCYYpW6EmvxX5OJKtKpdJZaeszdNyQX-M3yLCRb-UrDLq41HnjuU25Z01ZVeVcd2Z2aJteKLBFAB0wXG9WUzrvt5XXOiIahFvV-1jqpkwfV-OuXij5u_sp16GZQ9q4jrc2epfvOwB7U5ieh4gM6KzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ نبرد رئالی ها با تیم سابق ایسکو و مصاف شاگردان کریک برابر ایپسویچ‌تاون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/28710" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28709">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db6agi1DZEaE8C77NxGbj9veI4v6tNJmQ14nNlw2srkLXTo0W5175CVZbg4_AeKGJCt1210JCUxhRtRkCGytPVxNAAoGlebRYJlnwlL73R9dqBsWuRHlY76yZR0-4cJP6SVNOz0g8X6pjH7GLmF8siQlXzo5dyWyH8DA4ceXi94xx_e8GPwT0ulpbPOKPjk-ltR420qsZ2L4WyI-FGoVuYFS1h5L3Nc9hy7XYQbDQUsoLg-DUgQrkuZUIufVhQ1W5DzGZjP9zLqS709LgCzIiolV1v041qJTufGUjknHvZ2ya_6A4g2AB-T4u72-UrH0VT56m9R2BGirXgjIQizOCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
برتری قاطع پرسپولیس و استارت فاجعه‌بار شاگردان دی‌زربی در پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/28709" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28708">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeOxvz_rTyjrjI17vvEseTl-i5RnuxMDFQJWTJF6IAG_TCCJ7EJS_mTiqqEqj13J5xbyeE-UJavq7eOtoqMu5LtBjjwqZJ-B2g4FfBwiT0Ly7DxZJ8uGva0QV6sB3p1hpnEbwlvGFcjKqrTcO2IDfIBu9O10gZuboqcbnm0eDxj-LxjGhzoy00ywDXyLfoyG1wB9XyIG6_o0BWCMlfRI91pD-HAGDW3FuMZFukQJ-dRsb2cFsrHL-qYBzWPOzEztEj8HbGqqNzA-_Y2Fc6NhcRWDQ-kE7ItZUxVwl5tY4wD0F9bjTkubfeBjW1dBzFbDKuR3ytvuelItvK28-VelsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@HUNTTER_BET
@HUNTTER_BET
@HUNTTER_BET</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/28708" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28707">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqXKs1joiX01RC3vQjhzFmVSgrYWaMdcasJMa3yfP2yDe9fscipYcEe9A6Q3BI3c_0TP4QUY1dqA9Bx9A79e0V0PGItlGWePnixUbct3Z_tFeHJGoRtTBFmyiCg1dmm4-lTJ-wEKPTMD3bcaIst2eOe657MHz1bLkvYSXQD3vIDVK9dOxkljhoqAdXU55t4lVfzWhYntcVohAFV7Tku6DK7Ch5iUnDPKH9qJt7mT0husHZfe3bkwMp9EC3h8nS-ka0NYHJlpUh48HbCDtJOnl-poE3FcG0DBrh31rBGGLIGnxOL8fZD7dqg5WXZtVWqlBcKMhqlaF8QBs9wYSycNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍁
پاییزِ زیبا، پاییز خوش آب و هوا، پاییزِ دلپذیر و جذاب‌از رگ‌گردن‌به‌شما نزدیک تره. این گرمای لعنتی بره که برنگرده. با قطعی برق دهنمون سرویس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/28707" target="_blank">📅 00:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28705">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GILjbqgErOLZ7AccQqNPRDjvQUaFd4Sw4RBSj10raWsBmTrgiQ7PVFrnMiDQ2figUZzudGLo-yCOKlljsN2btBUnOHGPdI91u4QE_48IEKBPJEINSV8hz0Cl81F2Uykd_fNDCh1LGdD7KqxVV_hjwbJY8rX6f2zQBHXwc9TaE6ygu66FD43rnoong0yRj1tviJju1IKsHC7T-svPyFxA5eL0_D-g4OcEXCt5IXOj_bJUufsVFEiejM_kobwqq2z3Xxr8KBhWg54jtiuhPSLI3fqMWDb5Sxk6TzSi73dEo1aZdePFcypcHn5Np6-SSS001N9y-YAfQreUxjdKxx5heA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنهایی‌دیداردوتیم‌پرسپولیس
🆚
ملوان از نگاه متریکا؛ ثبت‌امیدگل خارق العاه 4.02 و انتخاب علی علیپور بعنوان بهترین بازیکن این مسابقه یک طرفه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/28705" target="_blank">📅 00:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28704">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-LAKuDNzxmA9P08jpROi8ZUJDtHw8JdCZymPMlxveX0PJlWW-mewb4Bwm6XgNP4VCc8NIcsZgeswnpJN6c0HZTIBSlDOteM1nEOA3TDoDWYQ5-kdkxmwGrLfMAlfzNDVC1H87eP8d-_jiWBc7c7JoxURe4bNJNHxa3hf_UthEWwnE5k2kPg5Lluxoek_BtES5qEX-6LihyoHUNYdVlx9d3NxiYuF-PF6rITQ8drnn-zy6mKr8-PBqd9lOJzBkbUahmGjYaGMJ8b5xEqxfjzA0eMmC0nDM0gsHNhWqaO6ECoveUvB2YMNQ3shgUtmZybgXDIqP466YIbjHsvw0whdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزنامه«Novi list»کرواسی‌گزارش‌داد که محمد محبی برای‌انجام‌کارهای‌نهایی‌لازم در راستای پیوستن به‌تیم فوتبال رییکا وارد شهر رییکای کرواسی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/28704" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28703">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXT9yoUGRhxyVnrUM0iV0Uxb77LDdrguXtT32ckkFUGttCwUh_PYmE6CYxgHoEY4PzfLUIKRhkvdj1ddjDMNJdI3ptofb3nLVAZV0HM-13VFcAfHpIht1ilt8gUbb_4XmpsBoUujhJlMriWLQnfDOuYAoYTEN13hdiz2scGULea6NdJPH-0-oQE6I4vE6uHyfDP_a3cQur3_sJabJGC8QeRk6AxUFro3F8WLnGKrt3NJWZYoER8wPyEzUYLanEgHA6rukEAjhIzI-K4ILJlb9aO-f_4dMMZ0aqvX96SKnAo9I9M4qCzHU03Ggb68_LNzPBJSLGecy4P_1d5Ufv4NNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28703" target="_blank">📅 00:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28702">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-wbx31YbpHLfZPAZ3havhgDYueCSiROYY3rQOQ8MhX9G45Ptk7zwPH_Vhnn-oVmhW79xn1tuLXCGGbtDPoyFAwncaeph9L0LHCICyurBeXjZXtJ77tDsTKFAh7_3pLEU5zX6KxwCPdXASlkMUODKPihBjKEK8RjYCzhWNP8XUXglEJhhHgYwLcu1U-EwkHSUxU65by_jM60BTfkKOiaGtorfZ_IbRHTTgN0pNLLnxIB8KaIEWT-5MKJwNwIUeHIT4ZDw_uRrI5t5IKNlPJb2YApurS-opcecQPT_reV3upp3ln-NIluRhPU6ejKgMdhKJL1_aOE7cLdkJMwB3f3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ اهداف‌ باشگاه‌استقلال درنقل‌وانتقالات نیم فصل: مسعود محبی یا مجید حسینی، ماهان بهشتی وینگر راست‌ ملوان، مهدی گودرزی هافبک تهاجمی گلگهر سیرجان یا فرهان جعفری، محمد محبی وینگر چپ تیم ملی، محمدجواد حسین‌نژاد هافبک تهاجمی ریوآوه. جذب…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28702" target="_blank">📅 23:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28701">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcYvn6W7xoI4EYnkMO2yUFEjoZrgs2VFwAVeeyiLBE354jo-KFvb4iDBj0Dl027OlO-pGGgBRtqRMNaa4_HVHFY_zgUs6Ax6-mXLWbvEeqy5F-BvnypOoSurSx2RyLRxnyEMylAT1iXZsqTfmOyMJNdggUFciLm_YqJNSghepbEpO5JjDHoTQRwFF4HNAcEWwGMQTBUkOE2HAG_5fYVJUPGT4Mu0-ndmQ4lEBl4bqkmy3Pj_kpFaVAYc7E3GtWY1--yVy0e6ZHIVGBdJtm4syt89MyBSgbueFdiFzZFyCmFrMqrzyfHHmuSUZQzYwMs4i8WX9Iepq74NLMo1GBgaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام جرارد رومرو؛ الخاندرو بالده مدافع چپ اسپانیایی بارسلونا تصمیم نهایی خود را برای جدایی از بارسا گرفته و بزودی از این تیم جدا میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28701" target="_blank">📅 23:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28700">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKBbK9cEamUOvexRuqdxgMUgemyIADcVXKNUe4c9Eoz1NC4ugBFwpK2oLAmzI3qSnWpH1wIQVLC2ZeIwutsAJyYS1n4ecPrgvtPdRxNcGv9dvzpv69xXneOO-zElwFytKKfKtFZ_OKOsgSXw1Ld-pYy_K-0wjpaxRtI27YHZqWguZlWVRTXdWHMdHVcuwZmRkNRshoIAkFQW3kQWggUt5Mxhjhf5IgEXg27_dgQPpQMVB-eFURseCEnfND5BIANwf7K-8dsraBE3ldc32N2-GrSdLMTR9F9PIYgMjug8BVhkbNT37CH6xK71EcTD9vqHnDE1a5rqC4Oro_lDBu4haQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/28700" target="_blank">📅 23:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28698">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpaokd3jlqkU_BWZhvGMNyiHYTAsjE-5MHv9nM3JkeTfRKEo8CIN11zJtxJ7mooVAH3G1MQwSTRvH54RJsMo82udHn_of4-JcBFpkk4McGTovns-mXTB765Ry0xKbB-UEx0MnZZiPX3c-S1RkWwBk6ST8mkvBswL_9EIFi6NLlKUBvEnqnPjO8vI46TkF7hAuau6KI7o_zb7S9pUwyfNDHzTo7PZO8YquRg80teVA6kqJmeCr4ey3ssVUFKk-G0G9aFngLledekY3cycFlZWUqno-EIffFKH_MNg_5oPGqts_4jtcdXOu6WAJj3vs-En2JpONEb7LgkxS_kEgLPWoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/28698" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28697">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f3cfd1b0.mp4?token=u4-1qbB1IPMNMpHZK4mAZq_ps-X475_wdX-Zfsx8tawfA_-lsSx6m4Yoe4ANCmdkvFZR4co-P3wrkSxNJabupfVB9ISKyGx65UhZYjZsqQ-7X4wXjXXxvePqI2_ACIbhcRu2S02r4WxTCPf-FapnWi740e_-Li5Wqt7WaLYO-5H0SGiF7xVAzVd5SyRMu7n4Aawwx3xLMWzcrAMM--dGySXSshQqXYdeznnltYSzX7mgysb18Fvz2-cU4c-aEi6B4aG8xKRWhGzjLyrwoh5xznnV-df5-Rk9Y42weibs7a1LwmKwFBWAP7JKUt2A2VFQlpHMwLQNxTrxmE_fmsFdyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f3cfd1b0.mp4?token=u4-1qbB1IPMNMpHZK4mAZq_ps-X475_wdX-Zfsx8tawfA_-lsSx6m4Yoe4ANCmdkvFZR4co-P3wrkSxNJabupfVB9ISKyGx65UhZYjZsqQ-7X4wXjXXxvePqI2_ACIbhcRu2S02r4WxTCPf-FapnWi740e_-Li5Wqt7WaLYO-5H0SGiF7xVAzVd5SyRMu7n4Aawwx3xLMWzcrAMM--dGySXSshQqXYdeznnltYSzX7mgysb18Fvz2-cU4c-aEi6B4aG8xKRWhGzjLyrwoh5xznnV-df5-Rk9Y42weibs7a1LwmKwFBWAP7JKUt2A2VFQlpHMwLQNxTrxmE_fmsFdyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
فرصت‌سوزی‌عجیب‌وغریب و دور از انتظار طارمی 34 ساله در اولین بازی خود برای الوصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/28697" target="_blank">📅 23:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28696">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCcrklYym_XJXZ-FvQsQ4cb7Tlpk_a_qIRpA-K4k7MSUxmdFeRwqFcjgbffWDWgb9t0xyvUGNtSjsdVkVbhMlYdXucqmnTU6AP2QIgYl3fFbGOtxvBDVLYYNlqJ96C0rZqoIQtAsDzbN9n_OQoGcgNcXT2locDlgEWEGAScbur5ZAhTaOsJhL1mVanf54pSNcp3KE5ud3v2_AzXD7DW4Hj51_X_pDIe_xIP8oDHUCw7dcaEum1X4cgWddudfvWk-mOIVL0v2rN2nN-Zow0D-Vd8QxbUQhE8-Ig9zTpjf09wC3Y81tcXt3V3IbBAu3KLnFs9RElO0l4UbexXC2XQO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری
؛دیویداورنشتاین:
کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/28696" target="_blank">📅 22:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28695">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6xRxFN01fZqAEiAMAnzas2hSpq5jYp-v9ObVRl0-OzxGGWJHGTbnz7CK-7kTEScJ8Wnzrf1c49beaC74Kjs0fSrYFKHyFcRAIc79LqmFYjC829KFse6V3mPLLYCugGgtLE6xwN1CqwuQVBGZNHl8Pfo5BBUBj8NLx3KEv_kJ0txW3BDR7C2kE3WyZaKYhxf9POVtQfNNoCRmCKs8YL2mlQk1Hc_cM7dcl5ktdron7V7q2MhvVlj0_AX28DAHdVP0fFEuiaOD6r6p7kkaRLOwbQpXN04eEwa0CrREH8oaabfBrUxiDjvUP4WpOzoI7OAImbeSNkEEStKmAb9R0f2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های محبی قصدداره بعد از بردن حسین‌نژاد به‌پرتغال، محمدمحبی هم به پرتغال ببره و نیم فصل با رقم سنگینی به ایران برگردونه. فعلاسر انتقال حسین نژاد به ریو آوه 250 هزار دلار به‌جیب زده قطعا سر انتقال‌محبی‌هم 300 به جیب میزنه بعد نیم فصل‌ 1…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/28695" target="_blank">📅 22:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28694">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b98c0d9b2.mp4?token=TlW6PA27Dr0PHidUHwktNO2UWW8A9GzZGeEIbI-VbeJshm-UXRcyFBHKANF5q31lgQTOj7saD61CJQlY6u8HvjdTyHar7cDhkVGPujY8Xc6GxVz6J0NkZEFbdVCdVBkfVQLUe-JMDlKi2Fo8-uux5xIYj5EUyhE7cbvbTVnBroIFr5Zon2jHAwATc9cXWhf1OS1cWrLNi_Q2hpOVtGdOoBB_J5RWkQPjEO85oZoDLBluLD2VcayFy-y_nGuI7wvwW4QlExWCMrGC5d7OfA5EXx6CWqcDwzU5_EQUgxG4ynZg_fCXhU5IQV8VfO65Vp7Q6vYA6tJv_fJk7wgzpF8m2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b98c0d9b2.mp4?token=TlW6PA27Dr0PHidUHwktNO2UWW8A9GzZGeEIbI-VbeJshm-UXRcyFBHKANF5q31lgQTOj7saD61CJQlY6u8HvjdTyHar7cDhkVGPujY8Xc6GxVz6J0NkZEFbdVCdVBkfVQLUe-JMDlKi2Fo8-uux5xIYj5EUyhE7cbvbTVnBroIFr5Zon2jHAwATc9cXWhf1OS1cWrLNi_Q2hpOVtGdOoBB_J5RWkQPjEO85oZoDLBluLD2VcayFy-y_nGuI7wvwW4QlExWCMrGC5d7OfA5EXx6CWqcDwzU5_EQUgxG4ynZg_fCXhU5IQV8VfO65Vp7Q6vYA6tJv_fJk7wgzpF8m2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس‌جالب‌ازسریال قدیمی فصل دوم ساختن ایران و رفاقت باحال امین حیایی و محسن کیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/28694" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28693">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e895367e.mp4?token=FNiEiOkIMcaakbQJ7w1DEATB44CzGd0khEbaBLl-642FKMcJgsaspLLWNBjtQwhjdTHATMVcciYamXt7dQElXh_qXRsb4wB_9z-1_wQUSgIOQqU_kqligW9hpPWQrjZtcnAMQPu4hajEPlC3jqYOCrXhruooUSQp8goUOftMw48JyLz7BegqWQ1vItzN1NJUYOz2sB3Mb8K5WxJSHZQrL7UaxnQg1Z2lAfiYlr43M8jOwI9zPreQnXQyDfCt_K2jMiq7SXJ62rv4YHiervCcG3p6E2DMOhM26sSZ6QVCWTW_1MQjo7NwlHYrcskCXHkklpouUMEPKj8cHjEUWSk66Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e895367e.mp4?token=FNiEiOkIMcaakbQJ7w1DEATB44CzGd0khEbaBLl-642FKMcJgsaspLLWNBjtQwhjdTHATMVcciYamXt7dQElXh_qXRsb4wB_9z-1_wQUSgIOQqU_kqligW9hpPWQrjZtcnAMQPu4hajEPlC3jqYOCrXhruooUSQp8goUOftMw48JyLz7BegqWQ1vItzN1NJUYOz2sB3Mb8K5WxJSHZQrL7UaxnQg1Z2lAfiYlr43M8jOwI9zPreQnXQyDfCt_K2jMiq7SXJ62rv4YHiervCcG3p6E2DMOhM26sSZ6QVCWTW_1MQjo7NwlHYrcskCXHkklpouUMEPKj8cHjEUWSk66Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تاریخ سازی دختران ایران برای اولین با قرار گرفتن در بین چهار تیم برتر آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/28693" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28692">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe8rXpSFObkAe_8SFkzFU2JVNtf-0ISEB0Vbk1_N181OMiOoNLYnHENKsiw_XfWvgdMqCt1sgLMOcjNH5Jz2BiL2JlU8IlQ6Wv0CWlW4WVjKEbkeFnQjlLoGVEcXxYshmxMOnncQ3OTplXDtPwz-fpXhgMm932j8bYc9-ifDtKGFr4EMdBSosvE1QIzGHauhvZgMnEjrSyvtO-OepVXDbRXoCPureJqcqowSuWBNOFA_1Xu0X70nVIuhaRpXwTvqFWbAY66tGKyM0kHP_o687jt54QbOGMiun3H_QtrCmuF1ZEHEKZ4Xnl1ZArCxMxRvV4kfxM6n7lrKqPFxYh1puA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌دونستی‌امکان پرداخت قسطی می‌تونه تصمیم خرید رو برای مشتری راحت‌تر کنه؟
با درگاه‌امن اسنپ‌پی،
حتی بدون داشتن سایت
هم می‌تونی پرداخت ۴ قسطه رو به فروشگاهت اضافه کنی. این‌جوری علاوه بر اعتمادسازی، خرید رو برای مشتری‌هات ساده‌تر می‌کنی و فروش و درآمدت بالاتر میره. برای اطلاعات بیشتر و شروع همکاری با اسنپ‌پی، روی لینک زیر بزن
👇🏻
https://l.snpy.ir/hw5zl
https://l.snpy.ir/hw5zl
https://l.snpy.ir/hw5zl</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/28692" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28691">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=jT6Fj1Z51CNnfc4z8R-sq6gPAm4gUpZM1Dq2AWKWUJZPylFH6vCLKDP3lI1DDdsl0b1rtTc9osZOYFhcRXmtVmHWH5ivD7qCfX05KpbcVCCWASpd76h4E6-MamgMAcuVtoIAQcDdngMSQCqwFzpDjnRLZ0kRoLJ3WIaQUe2afJ76sVnZM2ywKHSYVdlgOIDY8uocFhUL_lhitKM5pS_FH1Mh2awKqzhKS93_45LUllD7qdXgNbxFg9VbT-AoGxIv-SqZHQxrO4Cm8Cb-ZsWa3XdASgd_3HR8N8FelfZL3KXXp-bvBDNFN5g9QX89uNx42u7Lg95fwK0M9qiBNSq8kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=jT6Fj1Z51CNnfc4z8R-sq6gPAm4gUpZM1Dq2AWKWUJZPylFH6vCLKDP3lI1DDdsl0b1rtTc9osZOYFhcRXmtVmHWH5ivD7qCfX05KpbcVCCWASpd76h4E6-MamgMAcuVtoIAQcDdngMSQCqwFzpDjnRLZ0kRoLJ3WIaQUe2afJ76sVnZM2ywKHSYVdlgOIDY8uocFhUL_lhitKM5pS_FH1Mh2awKqzhKS93_45LUllD7qdXgNbxFg9VbT-AoGxIv-SqZHQxrO4Cm8Cb-ZsWa3XdASgd_3HR8N8FelfZL3KXXp-bvBDNFN5g9QX89uNx42u7Lg95fwK0M9qiBNSq8kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
👤
مازیار زارع سرمربی‌جوان‌تیم‌ملوان با تریلی از روی برنامه فوتبال برتر ممد میثاقی رد شد و گفت تا دوربین خودتون رو از سالن بیرون نبرید، مصاحبه نمی‌کنم. دوست ندارم تصویر من رو پخش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/28691" target="_blank">📅 22:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28690">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9zwb81LZt2mGw5IYggqPewwgYeaWu6MfxXwAQcZRbaZyFc84zkNPSAMcB0nCsP5UmIIjnoGQ-2if-cEOQRosEbIzxwQw1gs6oYJO9qbdH1VTziUDUt5-9hpC5omFNNfRkzeYYH5CS9UvXMtGDUr50M_A0QDFHerzeb3ZwCXu0kUjLLf7_P7ukxBtg2VORJTvXvpjgLnvsxnyLjKV96NXEstwOWAHQod9RBUkWhP66kWfkOydbFIc9rE2HW67HQzHkCP5fpX3AfiBUuzKtc95W9hDZHt-VF8IBfz3e2UldEBFld-kJNcQAPx8DSPh5_zBNmAtl_ykfLKMc_eY5APpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28690" target="_blank">📅 21:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28689">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwiTpQZHSGQ9LRqdW9HdvhUKpNUPixIed26KMnmL94ASySifVgsKetHIhMzpk2SGVXVjAZirWfkG3VoXtKtLrRLrqJygKWQwEQUYsDdH1luWseJV0XIhAZBW1caqUtHjbhnGIvH7-t51Lg-Rqamzkzr1W09yHTNVP5Bd1SyfSv69vZmGRPmixqaUFCMu_TJsh6XxWAOVzv_-_mDV-vIM6L67jPJCRPdtY5ueOQt1I-OCpsmm7-LS-ae7mT1Qu7IwJXzGVaNmLRjgU_oNyRIhBBx74Rmr-wlYzX-XuNtakmNwGWEkr4UQKqa2UpMbFEMX8EBKJsA6CiXEfKuvslRODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌ونتایج‌کامل‌‌بازی‌های هفته چهارم لیگ برتر؛ تراکتور با جواد نکونام همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/28689" target="_blank">📅 21:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28687">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CW2RzCML7Qt5yaS09fFL-r8aJJGXwXSArUMa1q3P4ESMWrNwHs9TI2a2uVEYy7eK4lIJ-25YRD-hLkf4I4PZ7bKEpCJ1ENzs3aC9fNJAAeajUQg9UE4jzpyi9LSfCajqY-NdGD0uboxiDI-gh8GZyd3BwvYUSVl2kao54lcLIXIq53PnGVdzdn70D3ns1v_ckSIEl0j70d4OvwF2RNHhJ3MCvW4OsIGUnb7wPLrZGKCR1_bwCcVcf6lRzonfG1BRDIGpAMMmfJzDvwuMqc19YeNxUEkqdvqD9NeRKgY3geCQ-XEV70eIfXGH5BlI6BOxN-B08IBl9C2RbPZ9skgTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwIFvQz_uMg8nbJbeD9YWqwQ6oRlYg462Aer--v_4CXQK4QzkBGW2mQgsDmG_g6KTMjRodZAfQgUxDzIBu4mTLtbGFtLaNL7SDqi6QAFTjGgYYKVk3fiFM0aPUW4uJyBxDqOWqNJU3gswXAYmjlCQ23H9eADciuqbMEvepz_SNEA9FeqKZEHaoAEpEsOhnckZeQ0d0PsrT7LXSnXz5j1xq2fZHWXW8uaDnAARl9gSk4IKuOQOlb-60YeKNljBDbvDzdDHo01x4cUvI9FSD6ZGu3Kxkv9lbumoFvvFG3BfYzbTNN9Vj1Vbl8A00UAyMVAlTu7V4KTPYX_1Ti3k8MdPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28687" target="_blank">📅 21:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28686">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urHvuG8BG7TNyXEs8ryfywTIMsw16NDWxLQfKu2YdDv66GQrbn4Y2mS_jporUznSH_76AbEjA0s6rPDd2mdKEayomDypKhANZymMR0M5NBSm6-ZGUYo50_f_eL9UICh0s3k-g0f-UeUGIYXqpxqQe3ibkzhMzcaIQJzcqOHpXNZbufU0vIjAqphI0oRxMOG798B9zN1_Bf3P5w56WT4SOO2_hDemxRiO2TsKsRyQNMysnPxonVTj4vgYH2NJJLHqXGZC69NMYRYGODvEjIoOVTk7nKGFfr2KOklhNG4qVj7nGzMk5ligVi1K3mUajygK_J9-ZnuntD7ThDb6hQp5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/28686" target="_blank">📅 21:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28685">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY8vJzw_x7ISsSPFguY-gbPcPFLAKy2BmgDju4UCkUhTi58j1JqldmNAjc9BIeBUCybryO4s0xpMF8z8E4AFhIkDMlrtogTm237ENxyKflLUIm3KTAvkD5aKwXGI6H6CizMBobyUHnE_QhVAwChenFYOfdTH85yYMvlZeGTUhyWb8UBG3bSMdSBzwt6N0KpFoRFemqaJRwN1msAcdJwGgT76Qru5hPFWnxlI9MAGa_TkZEKTyubmMU4fm-diEUPZxvYG9oWTngzWDG5bT4mmGwRl-m6_tBQRELUiEDsLD7ifFnQE5DlR3qWOTs9jgbG5d94cxLDMFF9WgnMCrxO-BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آتش‌بازی‌سرخ‌ها روسوتی‌های عجیب انزالی‌چی‌ها؛ گل سوم پرسپولیس به ملوان توسط علی علیپور '56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/28685" target="_blank">📅 21:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28684">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0430b06fb1.mp4?token=Nsy_1_fYeJjGHZCX4ZEqTgZWgMtcKgXTLlr3AI0I386g6qd1SCtawU5Az1pZNfi5Bud--iDpzTvsT9Q9exrKouOLRmYNkEL2jKyyR1zGOIwKFBTX91c2HmrW_tUXga-4cI6EAy6176PSD9AQE7TvQtlIERJhxmLdlVB2kdpDaNIERrkiI8hgQ7kfmD8Cd9kbzEdbJCYvj0HLXdyhzJQ0kpomp6qMZp1O_JMZ1XpbqAtfm0MCe9YNIYGR2t8yucxMYTKYkLMTuuv-x4abwGfexJUUe2E3ZwcLbDPxQ498YJF5jqKEpxMSmJuE9d2Io_Ks6IX75hmmqLSm6UAFLfXOKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0430b06fb1.mp4?token=Nsy_1_fYeJjGHZCX4ZEqTgZWgMtcKgXTLlr3AI0I386g6qd1SCtawU5Az1pZNfi5Bud--iDpzTvsT9Q9exrKouOLRmYNkEL2jKyyR1zGOIwKFBTX91c2HmrW_tUXga-4cI6EAy6176PSD9AQE7TvQtlIERJhxmLdlVB2kdpDaNIERrkiI8hgQ7kfmD8Cd9kbzEdbJCYvj0HLXdyhzJQ0kpomp6qMZp1O_JMZ1XpbqAtfm0MCe9YNIYGR2t8yucxMYTKYkLMTuuv-x4abwGfexJUUe2E3ZwcLbDPxQ498YJF5jqKEpxMSmJuE9d2Io_Ks6IX75hmmqLSm6UAFLfXOKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های علیرضا منصوریان سرمربی الطلبه عراق باخبرنگان‌عراقی بعداز دیدار این هفته این تیم در لیگ‌ برتر عراق که با پیروزی تیمش همراه شد: 8 ماهه که هیچ دستمزدی از الطلبه دریافت نکرده‌ام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/28684" target="_blank">📅 21:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28683">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ebe211786.mp4?token=ldc4xux3C1tP_8S0Qase95tQF4lrzwEOy3gmlOCmDvhTfn_Xz0IKyXnul6mT8iHI5KoIVSxF1_uJHMyhpJGzwFQRHIqgRPBrmK6K_G8_TsLzBUqfgDveRxdGwY7Je1T37SgJM2EWgGimB8KvRhJDb2JOqcTKW1RdxomXDooDA11kT1nCdB4L1VEReFqmX6kf8cZY2mm3Uv6aTg6pK6ycLGwzYc6vSxOwtSFn9QXbbfuDIg0T1t3dvgRm4XgorQgrAi_xcFczvf0mjVdgG-tKNor3m3qIy4ZJrf5sC6L1kM0EGOdqFgGpZI4JNBP6DJaW5xjpvwvyTyjMD4jwr5ej3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ebe211786.mp4?token=ldc4xux3C1tP_8S0Qase95tQF4lrzwEOy3gmlOCmDvhTfn_Xz0IKyXnul6mT8iHI5KoIVSxF1_uJHMyhpJGzwFQRHIqgRPBrmK6K_G8_TsLzBUqfgDveRxdGwY7Je1T37SgJM2EWgGimB8KvRhJDb2JOqcTKW1RdxomXDooDA11kT1nCdB4L1VEReFqmX6kf8cZY2mm3Uv6aTg6pK6ycLGwzYc6vSxOwtSFn9QXbbfuDIg0T1t3dvgRm4XgorQgrAi_xcFczvf0mjVdgG-tKNor3m3qIy4ZJrf5sC6L1kM0EGOdqFgGpZI4JNBP6DJaW5xjpvwvyTyjMD4jwr5ej3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول و دوم پرسپولیس به ملوان با گل بخودی مدافع حریف و تیوی بیفوما در نیمه اول مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/28683" target="_blank">📅 20:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28682">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b26514a40.mp4?token=UwOdjRk4KtiRHealZ4N-6os4WYE86l3P7bXCsUa1oqDq91iVR8lKGOPPLbJwYuLo8-SnKj5fAOwERm4xVlKm6eH1UkygiC7fcS70B_F_Fypu5Dy4IEEiUAH-9CoM6eDfRU7rP6N_QO7jbFoIJMWN5Pj_nbYR_AbSeYIV1mmXYazH8LUeadcWbz1uPW24pNAy6CYen6aUwRo74QMbqna175wmtj_pICIRyMcY97Gq_Py4XCYgUVSHM0yjPChIr-J02vkN_LCiDUikS2Ha74Wgfm7fGzWrJGUMOY6w2l9vvIHk7TWH1Q8VB90paVMK6yDawFGoKKFFmlOF_QJN1r9Ztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b26514a40.mp4?token=UwOdjRk4KtiRHealZ4N-6os4WYE86l3P7bXCsUa1oqDq91iVR8lKGOPPLbJwYuLo8-SnKj5fAOwERm4xVlKm6eH1UkygiC7fcS70B_F_Fypu5Dy4IEEiUAH-9CoM6eDfRU7rP6N_QO7jbFoIJMWN5Pj_nbYR_AbSeYIV1mmXYazH8LUeadcWbz1uPW24pNAy6CYen6aUwRo74QMbqna175wmtj_pICIRyMcY97Gq_Py4XCYgUVSHM0yjPChIr-J02vkN_LCiDUikS2Ha74Wgfm7fGzWrJGUMOY6w2l9vvIHk7TWH1Q8VB90paVMK6yDawFGoKKFFmlOF_QJN1r9Ztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریس رونالدو کاپیتان النصر پس از برد دیشب النصر، پسر سامو کاستا را هم در شادی اش شریک کرد؛ قاب زیبایی که حسابی‌مورد توجه‌قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/28682" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28681">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVxdF22F_sB8xbDBMYFiIKEdeDXknzxHEiLeTYCINA_WXNMqmh5DTRmkejWCgWNk8F6KKbAdmNQcPoXnpoT_eDb4U_ofpAAUbCgxi4aScgfqKxPG_aI-fgDWEy0voBqpcAzsMVvZ1IzZYZ2ISVn0E4Ua3dpCkjrcziZZySOLMDOTSOvkkmfq9htsEAoENp8HQPCg3v7yyNYBuh_SGfmfb5lKYnEVK5jOTeHwpw2Vd_4Qa_ObW-XLPNgcQKQvA93Xck71PRY2A3o7R7Iz2oom_aRJao2Nwdo4wLLAY3lwdJSYgOMPiohsQV-X18BEub0DpTBWboWELq3Ug6Tb-WV3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دوخبرنگارمعروف و محبوب شبکه DAZN ایتالیا برای پوشش رقابت‌های فصل جدید سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/28681" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28680">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QGY2cQQoym6Mbv5IVD1Z4RVVr36DFOqdllDrPAQvM8L9wkIW_V7ctDTl0FPvdpg1_eM5e71F8T77Mz6CX2XYStAR2Ns_tOom463qKLACTh9ZOtqkpj7tAon2AScuGMTAXcTzmyp4d7ju4zuVvrGTEvAzaB8i_oiharzK-0-ldIFraMdqAw6kGW1HIdSJ_oA3pWNGdQvG5f9NVrBLi1GgZ1fbWSzrbGN_zUpTFKZ7DRfVTEO4UPMbte3no-u6rUnjL5gk4abApR10p1pXbzzY1GbllOobmpGZXKB4_9Kc7pfLNdk6_7wasdqF178FP79dhLhw_u9JIJ44tCCrN0cFSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب با ۱۰۰ هزارتومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/28680" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28679">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qh9EnJFhhR_8MVGqrqkuP5zqI0rdRPrntEvNj7q2S3pak8dymgSxQmb_5OEyMgjxUCtUwy1GTJez6llcHHSkmjaWAGl7bL23IV-fneozBSn-kQ1jdztxp0saAA5vaf_qv2vPf1x1Q--GfI4uYAqKSrsBoPWyaggdFTSMmKPYXqmT2YVmEB3Wy8VdXEAu7J6m1eX6jwElMHurH8oiPE91nBstViUlEWIfwBjVZyC7tqxKx9GAB4M6cycUlnig4bQHX5mApVy0E0k-7lE71bcDL-4PjqAM4n_7qhbdXGYN9scrdHvCR8-aTl22owOB3Q7BedJJGFoByCN7edPpkKxGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گل اول و دوم پرسپولیس به ملوان با گل بخودی مدافع حریف و تیوی بیفوما در نیمه اول مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/28679" target="_blank">📅 20:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28678">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/28678" target="_blank">📅 20:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28677">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6uzsJ1SzPR1QcIzvJHRUHeS9s3EetlGwV838oqL0HE9Jyb1nFnRrCgKUu-CuSlGiObbICIZECZK7Ya_wJxvD0ZxS0KSUhKubvk100JGq30aHioRcvo4U1Y7YYhy7kSkIibi3zDPbLHrNWEs9EooCkGVgfmiSx5HzYU1DDfCv-3YlMDkmUZG3esKw0ar4bsDToz4WjNq-NnhBjd3EU6XOx92_5RladdxUqu9sOERXljkMCkTObIaCMu8ePxX6_KgsII5mVsc5UBsKstGf3nV9GR9KaVpuzBCBYCGm1jyLvZx6obP_pwhrfQUB-_Cm6vpO3lk2w-4WjHiq80h5pKAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر
؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/28677" target="_blank">📅 18:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28676">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=ge22Sf9gh14J0ltPSfBww2FKM2SGxCxlMM_a8ANvMTX9gG-AOmJDAIsHYS4qWQGr3FbRe5Rf9JK4-ow0rgdfd5vRJI0u9o7AAiejM9-se2TQctypnk6hYiCrTMXaIoTUVRvJuy-UPAVSPMXA2Jj3FZjNJ2XWIyZf5FjAokYsHqTCPBj8CYzU95sZ133gX_-WDeJSdOPUDnGMnVA-2UtlsLWe5rb6nkaCNL1cPEWDAnMUQk_sYF5Vn8odDdyuyzgfPfQ_KH8-SClzMIV-sfg3JrN6Bi9zmbipqH2bEORmoy980vS6VmvOxI2Z53ebNOLWn5IM999buKhoiMMqFihlyEYERASHmNE74Xb0JVOeCzNhisAGxSwUy_hs-DvvTwaBvwfQLVVuJUwknrMISoy87XUgEw5mDBD__qQflvkQTTnVjftWXarfuYhkNkvt_h-I8oYw9-l7vai31Xkm9DU8Jrl7MeDgNYeOnk97CqS8E8TjVRnvM-UhlhOFrcc7cjHRE2Zbs1svjTBbnF2Xzso2Jxu1mdt7vj7JhfUyCNrg2sl1GqLtPKeGqubtax9nN3MOXO3vzz9B628RlUX8Su_luFwhAp1XSEM8xLHluHWeSLjKgyc9It1TdgiVCC6i-_HzaB0_3-qWyQ8RsmddGnHgRdDmMISAt3atAjBOxrYtxgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=ge22Sf9gh14J0ltPSfBww2FKM2SGxCxlMM_a8ANvMTX9gG-AOmJDAIsHYS4qWQGr3FbRe5Rf9JK4-ow0rgdfd5vRJI0u9o7AAiejM9-se2TQctypnk6hYiCrTMXaIoTUVRvJuy-UPAVSPMXA2Jj3FZjNJ2XWIyZf5FjAokYsHqTCPBj8CYzU95sZ133gX_-WDeJSdOPUDnGMnVA-2UtlsLWe5rb6nkaCNL1cPEWDAnMUQk_sYF5Vn8odDdyuyzgfPfQ_KH8-SClzMIV-sfg3JrN6Bi9zmbipqH2bEORmoy980vS6VmvOxI2Z53ebNOLWn5IM999buKhoiMMqFihlyEYERASHmNE74Xb0JVOeCzNhisAGxSwUy_hs-DvvTwaBvwfQLVVuJUwknrMISoy87XUgEw5mDBD__qQflvkQTTnVjftWXarfuYhkNkvt_h-I8oYw9-l7vai31Xkm9DU8Jrl7MeDgNYeOnk97CqS8E8TjVRnvM-UhlhOFrcc7cjHRE2Zbs1svjTBbnF2Xzso2Jxu1mdt7vj7JhfUyCNrg2sl1GqLtPKeGqubtax9nN3MOXO3vzz9B628RlUX8Su_luFwhAp1XSEM8xLHluHWeSLjKgyc9It1TdgiVCC6i-_HzaB0_3-qWyQ8RsmddGnHgRdDmMISAt3atAjBOxrYtxgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بجای‌مانده‌از دیدار روز گذشته فولاد و استقلال؛ دوئل علیرضاکوشکی و رامین رضاییان درکنار زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/28676" target="_blank">📅 18:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28675">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHlDvNK0UDuqtR6g3Q2c77Y7rtBn43LJcpVb7I1CBIaD1kYSfeTERFUKZHwqTezu0YMc2mN1p4y5TvVhjbp0SnUZEEK0opEmP8JzBnrUPax1iB-fMFujUNH0zQcUFUQxV2ywOJoH0GXkvphdlLjL9stRf1Px4AgzQPzRURYjEMwTF_HtYgCbFxqCCSYToo03NfqfX0nJhpKTFrhlD61UkGETZPk6rRJIP-pMKkvQ89v8o8Plc2Q5YoBXLk5oLpoU8LzbFAW-kn9T81eA3ubKBgswghtSEbomryP6zbB3JN1YzmP1LXdPBlqfMx3Cof-_XlethZcOo8EDouPcYLL4PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دوخبرنگارمعروف و محبوب شبکه DAZN ایتالیا برای پوشش رقابت‌های فصل جدید سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28675" target="_blank">📅 17:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28674">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b03755e8.mp4?token=s8tDLlGmNbU47r7rbQdMsFubLb5psATFqTaIDHlbln7BgrKfUFJILasLNFgp-r5u3xqrMsQGs8ehyu_cf05-hcFRZYDVhNvEbN2rFgMNiUaIRjc5XQvffLhyatiNlBPOHUZQUQLqydIFdWDsbIzo0Jjd__2pH48Lc_2p2biCUaWWDID9iYgv4_t49oNOocF_1fenoB-aN8-jDEN3rb4hUpVqdkvB3MRk6pNm8XysNay7jiUfKYYmsUOlxcJ1nQSq12_tRZrKDRxhe27igLZHS2lrASzvp8YnTbL7MFQTDy4Fn9IxcfWcC_cvlF70IlvEydgklF_G32HEIet0KDFbXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b03755e8.mp4?token=s8tDLlGmNbU47r7rbQdMsFubLb5psATFqTaIDHlbln7BgrKfUFJILasLNFgp-r5u3xqrMsQGs8ehyu_cf05-hcFRZYDVhNvEbN2rFgMNiUaIRjc5XQvffLhyatiNlBPOHUZQUQLqydIFdWDsbIzo0Jjd__2pH48Lc_2p2biCUaWWDID9iYgv4_t49oNOocF_1fenoB-aN8-jDEN3rb4hUpVqdkvB3MRk6pNm8XysNay7jiUfKYYmsUOlxcJ1nQSq12_tRZrKDRxhe27igLZHS2lrASzvp8YnTbL7MFQTDy4Fn9IxcfWcC_cvlF70IlvEydgklF_G32HEIet0KDFbXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
صحبت‌‌های‌خوزه‌مورینیو سرمربی جدید تیم رئال مادرید درخصوص جایزه ارزشمند توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/28674" target="_blank">📅 17:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28673">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mavqbls4e3vJT1k8j_rplps3T9OjzEIUX-jLsrV8V3ycRXD9VjoU3L7tpTpzHgsmv_gdS-dDREQQ6rU0yeBNpE-O27DZj0AtO5AYRxiSw2VtHRgRUfsJyI6zq-AapP2E4uMyj8B7GM4pu7w4TRjj4FsUF5c3Ia0SkbmRFzYofLka2sE__kudg2DMu-v7m9UskUG3FKj6CQHH1yvnWhjhgQ2_NemFVpGSOyNAxGLR9AJHX5xJvrvDae5FcboY3VD3JquTjzZUv1XxZdc1zibQKyWSqZYdJ7NaYMfJfsGUesgRL9L0x6FK6TFFbZtFfdp_9fNnJnjOgMdrNitkySEWVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به احتمال فراوان تیم پرسپولیس در بازی مهم امشب مقابل  ملوان با این ترکیب به میدان خواهد رفت،ستاره ازبک دور از ترکیب فیکس سرخ ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28673" target="_blank">📅 16:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28672">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873c1f0eb1.mp4?token=Wsn2_bnuEJl8sg2i4EV9x9BqVPiN6JNL-fSYxaWJuz8v3Wp2LVII9wJ3K_rX_q9xq_kfdEd918e8wZaSDLT_lxs2TwRZkAJQn-_gkOrw9sZfMaWpLRfu5WvPf2e3HhkChvIJYgWCmKfkX2Yh216yBSpfghKYqn-qrM9yp-OrELnGg5c9mT-GikkduxktMHw8hcw-O80TQ39zeSdWn1i_FNZPbWXKOQ_IeCANM9guAum1ppsagUdd4KDrWEVIVYtbhrqgoTS2Rmvx5fKF3ffwI-9NVVsQJa3AVj4DkIZgEVN870LepfwCZpe--OIiBNqS3z12knuNEKTF4zGDRLJPiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873c1f0eb1.mp4?token=Wsn2_bnuEJl8sg2i4EV9x9BqVPiN6JNL-fSYxaWJuz8v3Wp2LVII9wJ3K_rX_q9xq_kfdEd918e8wZaSDLT_lxs2TwRZkAJQn-_gkOrw9sZfMaWpLRfu5WvPf2e3HhkChvIJYgWCmKfkX2Yh216yBSpfghKYqn-qrM9yp-OrELnGg5c9mT-GikkduxktMHw8hcw-O80TQ39zeSdWn1i_FNZPbWXKOQ_IeCANM9guAum1ppsagUdd4KDrWEVIVYtbhrqgoTS2Rmvx5fKF3ffwI-9NVVsQJa3AVj4DkIZgEVN870LepfwCZpe--OIiBNqS3z12knuNEKTF4zGDRLJPiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇵🇹
باشگاه گالاتاسرای با پیشنهادی 50 میلیون یورویی درآستانه به‌خدمت‌گرفتن رافائل لیائو ستاره پرتغالی‌آث‌میلانه. لیائو ازمنچستریونایتد و الهلال نیز آفر مالی بالایی دریافت کرده بود اما به طرز عجیبی تصمیم گرفت راهی سوپرلیگ ترکیه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28672" target="_blank">📅 16:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28671">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq-zt1RVJGBiy9M8N_VNfWEUfYTkpVqySqVrKrBs9MRYb1hBeLT-tCF9CXrUZsDv4UXXcuoCJnT1lzVnBNdJ3kGnMX7BEXfdjzHCizL-GjEWKnMVFszlTK5Y7tpRkZ-QGXoUQg4VBlBdlaDYd6IMscCUA92Dui1T2-E_VdAvNr1snvjfRflMejbleYT8Mt9HF92CFHfQFbe28kkdJ9QmTFS5lIy8pBczIKFKmCqkgis0m6CPRE5B3m7Z1kw3SE7YXNJ8IkET8edWReW-Qf1pBLFBAksYB6vXjSHw7QPwgSBB8N9EQAATJSm0P3GSWQs9WIo822rMVSDu5KyUThVRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امروز مقابل ملوان انزلی در هفته چهارم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28671" target="_blank">📅 15:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28670">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e418389c.mp4?token=QeCv3OOua9RLshwJ4qZqy6No7b4LMdBntECrd_-vJa3hZbwcJvjq2kqijtebEHosN6QE_i-Wmptvlw0ndMGd6y2MDOSSlIc2ekbXm7yqrnd6rUiS5rybtK_Bi61MiRiDEaVJCMEALjvZwpicQvsaDu0RVX4Nue0YNnf2W5NU3nRepF3mUKhErclfKTZJt07uD2UzpRUHOe-k6BRs19ID5zF4fDKgs8Zb5WT_jpzGLA-dzaMIKAXxXUNgd7ZRilkyZy6_52McVpz-MP9a4_3vdnfNd9ikMeRHgYJW4KaGQr8xU7HPdG-zyvhg1skZ3Yb2XCeVjjNS0p3P0pK4k5uTHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e418389c.mp4?token=QeCv3OOua9RLshwJ4qZqy6No7b4LMdBntECrd_-vJa3hZbwcJvjq2kqijtebEHosN6QE_i-Wmptvlw0ndMGd6y2MDOSSlIc2ekbXm7yqrnd6rUiS5rybtK_Bi61MiRiDEaVJCMEALjvZwpicQvsaDu0RVX4Nue0YNnf2W5NU3nRepF3mUKhErclfKTZJt07uD2UzpRUHOe-k6BRs19ID5zF4fDKgs8Zb5WT_jpzGLA-dzaMIKAXxXUNgd7ZRilkyZy6_52McVpz-MP9a4_3vdnfNd9ikMeRHgYJW4KaGQr8xU7HPdG-zyvhg1skZ3Yb2XCeVjjNS0p3P0pK4k5uTHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالدو بعداینکه‌دیشب‌گل978دوران حرفه ایش رو زد یادش رفت خوشحالی گل معروفش رو انجام بده که مانه میاد یادش میندازه اونم انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28670" target="_blank">📅 14:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28668">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqzjjsHhnnCzsstLwpRTVAMdRe5g2n7CA0g9bwOQ9lHzPBr7s5Y4VR1Tb5Dl__fzWFsqmVmNsKy8sJIHLYNOJqfzWrCiVD-CHE7kRhWSW3K7Pixsgx4P8_WaPFhUel-FF_G8uMUdimHRLI_deK8cE5NkRQkpo8JwmKynjJyblNjpXM1LrUp8f7oGw_sFZJWqXpIgbV_fJaIdnrREPsmg4k3Sl3FhUG_29zcChV2bE4de9UohpNSzZoyDL6JCk8rzf_SAEK-BtMohkS10mZlEjbUCjzeSsXZ8DMXTyb_Qnrdyjygs_2ll66osLWHlJRI_aEmoXTBzD-v8DtEsVRIvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCsQ8MHwbJrTt7XP1wLl59QAXOnRHL0NAm2Swc0Ggx5gO7jJb1uw9G_L24Mp2FnCSLp2iAKfCgxtI36S-hBMb6ujzJuRyT8bAPasrIaBlSh24JTOmHX8gDQKy2KT-WVsWyfTgopTQL91RWMF9TRUVwnXiJ7uvr2KlHmKnlI4kMHFRFlT_LkOkd1I2N9-ANPW7y-FbqusG08YRLoadE8QqodF9aMDZQONPA0nuHSgKfsu7F7dtcdnTd0RDGOE2OYVafwAw8ZY-Gw3ZKVsJxnyBRVNb5zZ1qnctiQMilmCNcHrHfWrom90DQabDf9_WuJefb4dIPJCigpwo4RAtYHnqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب دو تیم فولاد و استقلال درهفته چهارم لیگ برتر؛ بازی در حالی بدون گل به پایان رسید که آبی ها امید گل 1.4 ثبت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28668" target="_blank">📅 14:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28667">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evpvrIKjbzyLCHI-IwIMBU5vgthZeBsxENf3qPUD3MobTPCK0x4A2SdrEDJosclhsflpYaGbRM6x6uj9nITOH2GF8wPI2Zrv4lrG5umuCKNd5FpcNy8Q-qtk5aJ6Rok98oQZUwdHEMaX4mTT9F-vIASAh1-2FgNUpy2-O_r2y1x1QgKiBvvCYEu3QxqzWyjVqaPJICulY3X4XCCMR1Wz6ysMtLqszK-00DnVWQvBGLndqcS6pJRJMEvawN03RqwsgLWxXxT8s2NN6Sq4vlVMLa9iOAlyle6yQuB1uCQNKOA6yx48nsYvlMZ8xyschRL--J0aOwp0apVfEOhn1ia3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28667" target="_blank">📅 13:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28666">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08aa642e2.mp4?token=L3b8NBNb8IYJWO8lzvXXhKmsUhCZdO3BG_faxyrH8Z8S0Ugu1UczHtpCRRhgf6OyS8YFfZLtyExfamnxO8mvddDLl2uzSrauB22XHFysHzFTb0z07f12072ZmUbPQR3KMai7mwcNeXKklNKs70XImlLPYuhQO1-qte8TVKD0MTdZRhoT-9O1JVoO3xAXgcAqwBSJcDaf7Sc_tBOTFtqx4SI-ybtVSANMpXOP0JIzymlNa7vfkZcOt68wuE7Ii1mWrH47pqwL0slSlDcLmudShkk-To1bbSMlpGHoryezaAqm7Nw4OiXoD9hnmNs62T1ObmktQ7b8fBVtvGdI3cb_Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08aa642e2.mp4?token=L3b8NBNb8IYJWO8lzvXXhKmsUhCZdO3BG_faxyrH8Z8S0Ugu1UczHtpCRRhgf6OyS8YFfZLtyExfamnxO8mvddDLl2uzSrauB22XHFysHzFTb0z07f12072ZmUbPQR3KMai7mwcNeXKklNKs70XImlLPYuhQO1-qte8TVKD0MTdZRhoT-9O1JVoO3xAXgcAqwBSJcDaf7Sc_tBOTFtqx4SI-ybtVSANMpXOP0JIzymlNa7vfkZcOt68wuE7Ii1mWrH47pqwL0slSlDcLmudShkk-To1bbSMlpGHoryezaAqm7Nw4OiXoD9hnmNs62T1ObmktQ7b8fBVtvGdI3cb_Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پوسترباشگاه‌لیگ‌دویی لگانس‌اسپانیا برای آلوارو مورتا مهاجم جدید این‌باشگاه؛ مورتا سابق درخشانی در تیم های رئال مادرید و یوونتوس در کارنامه داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28666" target="_blank">📅 13:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28665">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTyK6QmftGFWt1HlbX2KlAszpzS1z7_VSD83NHI-oMCKGRBzjarBPjV4zlw6-h5pKo9IlfQBrWQytQyRtsTF3b09QWaLZRI9Y5cEHMUSI5RjWdXTw3z9-lTy44ZKWjiCB9pIdRXT2nOsjl3LROJrhGN-oduevkDIrnNu6M8j4pg75_1xDGPsZg_VIQ2FBWpks2-OYz2Wjb3bF2UcIrI2tIP6EW3jIh33IoF-jfWVSY0WpMQ5ptB53sKW_p2FgcbS2s_VhZ5ld7_djmhUBe588s7D8BDGLiVicZ_XTmTn72W_ErUuy35y1NuwmllehEbjfnNzPpGOfcyDnaDQuJczlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28665" target="_blank">📅 13:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28664">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28664" target="_blank">📅 12:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28663">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzVE0vahYMfuPgJqznV8oNFfPI6212gXTI-cZ-aXl2MWq9D08Yk1sZO2fGOaeiCV-18GnvGGexEGeniPunPd7zBsviFRbAYdivJxWmgvljKiz2T4eF_0ygTwGlCeulaW6u4GuIojneGEP49IhahJ7U4nn487bkay66i4cazknWogn5I8ae59v5P_WNsbuKNucClfSuAXpXzH61D5Q4O0-elaCWDdu47mduvBVgGoyuotDfBZDsi3FJ929KfF82dpMcdDb8CbpUKc-0yoOWnIHMz8P7yzkhQXlE5sqJQ_X9OeDCbCtCcc6yw_KqCVWqMqkuL9xcUS9zJJu36zXxbCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوسترباشگاه‌لیگ‌دویی لگانس‌اسپانیا برای آلوارو مورتا مهاجم جدید این‌باشگاه؛ مورتا سابق درخشانی در تیم های رئال مادرید و یوونتوس در کارنامه داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28663" target="_blank">📅 12:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28662">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5mdntFpKMTSl8fHes8r-T4lCPmHFhoiiGHIbbEC8FXCWMXhZIP_N46zlcOqFsxoc6J9RB2EQDYunRRTSVtYHVOCOdPZ8x_VgyVtdXDblnLH_oBfnfc0Xymv6RG3RX0jT5q6Awm3RDMc1xwZ1MXagcwQU92qw6gLJJAk46AxRoT6qtwZxFsi8gV0PoHvQxK-BMvBB2g3Gz88WgZvm5d0JcHf7NOlyNSOgmZYZYQ3nc53PQYHtWWYlMfcj5IyPnxjxfWbi6625yZt-zgh5SfqXj32kEAbtDsy89xhhrb4fJKdXZZG-FKeVXvlA3mi17O2i5LUdOaFEuNexnAPNyz-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ شماره 9 الوصل به مهدی طارمی مهاجم جدیداین‌تیم رسید؛ طبق اخبار دریافتی رسانه پرشیانا مدیریت‌پرسپولیس بعد از اینکه متوجه شدند که طارمی دراروپا نمیمونه قصد داشتن برای جذب او مذاکره کنند که مهدی تارتار اعلام کرده بود که سن او بالاست و فعلا نیازی به…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28662" target="_blank">📅 12:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28661">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2IHbGsfYfgY42W2VzLGwldlRh-0BTCAq8cDAfCXJHDYuYAgLaJUZbOirk0MdI4qw9DK4v-rOSRTYyR7f2Wa5XWn-rto43pkl8k-Gwje2Y7g0oFBS9T4Qtwp2UkSz4FPkDamDILywaNPafyEOUkdd-HAyoPHldHZwAfAXq1QApvWPbAbEQeMTnuuFArjvVY5gqYmnBnfDurLh-VB_AfAzmEfQd2o2PR6eSYKFjkAenI33DGO8YZZbcNr8-Ky4w2vpm-s-CN2F_vI984PIj3ifOSDBtIOVPCiQbkiF31EiZcGx_GX35p0aJvKTOFjBrzzWwBhqs7pmEFuAIt7jNih8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
کادرپزشکی‌باشگاه پرسپولیس و استقلال در تلاش هستند که ابوالفضل جلالی و مهران احمدی به مسابقه شهرآوردپایتخت برسونند. 48 ساعت قبل از بازی مشخص خواهد شد به‌بازی‌رسیده‌اند یا که خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28661" target="_blank">📅 11:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28660">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bj7lAmyRxd35v_T8V9dAn7ugAmw2AIkH6jkImXKrv_tEfMkikgxUQfJ4EpjWiIiM9WG14IsrkxIsF6Muz_b08adtiC_2-ogNEMt0ZvpJQeQx4-RpqVirt32fS7wQwNSXgPVgXyQOAepTjtMHAd4L68_roUuUfap_TpVDv4kUtppw8ogZ4mpMCAGSdKusGJrvLb1Mo_YvzuDKZe2K6THzRIuWUvgy6JtGYJeDzFzgzfFRqn09vK63gPvw1HIbxzGHEs28i4nbpVJksC7imjIkdYigGfWX7H_E4i_adtd7tP8gzfKvm04ZzaG8o4lWEXERyOfX7xrqFQ3n-s2U7LT2Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهریه دانشگاه آزاد رسما اعلام شد
؛ پزشکی و داروسازی سالانه 137.5 میلیون تومان ناقابل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28660" target="_blank">📅 11:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28658">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhMfbwt7GHyHooPYANjybepy5mqeyMx66ErgLvnwJCqnEuLi3suVScWREX1Mzc_MYGdz8yNXSleogTudEjTMMj8LwKkXdCOda9puq1nghVszYnifW_CE_0gfDPbq_6OqC4ESNZqMu76nYmZPB-HkShpCMlqmO4rQp9lyoan3iCRHeQxGy6o888V_6jKOnJlQnKlFG6qyAiv2QaRUAeElyck1DCX6YZOhomR4Ho9vKQ37E-Uk5QycraB-sr-dvoeiWJW_87c2v_I5BeLq8FrOI-pRgPrm-R-52RcQej-BQIAtYL6Jpt5I8tha4jPdxP1JI6aneJTe_ctqF4uLEiew1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSTTzgSWljDqPyMMbLnbcH2Kwv18fbZJ1TXD1NVYzNkWDBVYyTTWL4Okh8GN6SLr6kGtBV-36v-phx0BjCuqIh1L05H6jYzj-or6ko5HP92bF0h_wYamylx8oCJZ09_ZeXloUauiACLyyAaK-Qc79aHqqiaC3cSPEEXqhxQTNIAS0J2EadWJxBBwkWPM-1fcF6FrF4LOP8IouMVbvEbj0Krt0bFpmveLAnd4MxHdV_OlvGmAU8ATGWlB9LZ1IXXebWoaHcy4lviILtwlZ-MtuYlsbzEaGWbJLf5SnxiHzEHq7wIoG8T808VWJzNx3H3eTdBAAI1YWATcbIeV5rtM8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوست دختر بلینگهام ستاره انگلیسی رئال مادرید و یکی از دلایل اوج گرفتن این ستاره در بازی‌های اخیر در مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28658" target="_blank">📅 11:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28657">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjDUbadaSD7pqeNBJVJwdrsjOKnjnq5i5LWN1xhHV2W1akAmwQ8HWgYWRSwMZhJ_XKBO7e9Dy_IulaA_KCGALIQCpOv_oplNTHvAUILfaQsHFuEk3nfVRkxRnl2l5AVtFHxZ6uG5JMZsa7K9zLyDYF4DSuU4igTMZdaL2c7ZOeJ0AiG99xHv6QvbQpIz-9OjYydcRezpUMMwJkQy-oE5Q-Swth5m-mf2lYvfIgYDFNbRj5DnZcUKBdFgoZXgFrwYqIXlIqFWEh5GH3mbz1pB9PFg-6t1KhtTee8QtECpJIFFOkyEbsC0CsiMDrk6xB87JbLKUICOBLoC4GvbHidDrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه گل گهر بابت استفاده باشگاه سپاهان از کسری‌طاهری خریدجدید‌طلایی پوشان شکایت کرد. باشگاه سپاهان هم میگه ما از فیفا استعلام داریم و فیفا گفته که کسری هیچ مشکلی برای بازی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28657" target="_blank">📅 10:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28656">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9fc8311f.mp4?token=qlUWIu-1N0UJdWAwY1eXBLR9ie24HNUFSkYnFPMY8jjieQq_ZtGvQ284fvPeZPDtQFrXKWzkf8mbkUlVpc781ii8oCqCVi75Mrj7gmOd-KaA1s9E2GlplW27anylzgbih1kTdfTmjBEf517Gw7y_7zkOEVlS8R5rTXg32o61sfp3-NS_IVTn_7c_iqMzXFGjnMp0QlmemubfD0fFXc7lKeFGJklrn0Qj41foFyheQNGSvp_5AGOpchaaDqvNoFyLFyXuvvimwKlo7k_-fm2Ffl8-03ldhwJI15Sqe74SiWvrTGHBp_bPMf7kSfaurAuedaakSKHUB7UOsKlyTz05MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9fc8311f.mp4?token=qlUWIu-1N0UJdWAwY1eXBLR9ie24HNUFSkYnFPMY8jjieQq_ZtGvQ284fvPeZPDtQFrXKWzkf8mbkUlVpc781ii8oCqCVi75Mrj7gmOd-KaA1s9E2GlplW27anylzgbih1kTdfTmjBEf517Gw7y_7zkOEVlS8R5rTXg32o61sfp3-NS_IVTn_7c_iqMzXFGjnMp0QlmemubfD0fFXc7lKeFGJklrn0Qj41foFyheQNGSvp_5AGOpchaaDqvNoFyLFyXuvvimwKlo7k_-fm2Ffl8-03ldhwJI15Sqe74SiWvrTGHBp_bPMf7kSfaurAuedaakSKHUB7UOsKlyTz05MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوپرسیوهای‌دیدنی‌حامدلک‌دربازی‌با استقلال؛
تقدیر رامین‌رضاییان از حامدلک در رختکن بعد بازی بااستقلال: حامد نمیبود این‌بازی رو 3-0 میباختیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28656" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28655">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de192f8f44.mp4?token=cJOHLpk7cbKN2zUs0TnrE_AG-nzBdsuQjb-Fw6V9YMHsM38MRMnJPJkfoGfTvDySvxB4F6NFrOogkUPSie0aClYBRIXmRWtR8CuDVN5AYyk_B_-9L0LyMoomnompjrrTWn9zbzfTQrusCxfIwHBqbBpxiP1E6QoMenrS0CafbhMNFcuFOptd8teCannvOlE63JJEQ_Cy2DVa39kKx-Vsz5bbuaAd9SdKiBPw8cID618rCmmfdvrZ3QtqKivNvnQDM8lzvQWzWkyzEKzRRwHe8FZuGgyg8DBw4drwO9v-HTIysZ3bYJny6IeqRrLo1LZIb2wOSvQi-AgWidc9QuXynGn33toq7J-7eYSQU6a3bwHNes2aIhfvxNZX_FQ8Sa_dODtPkZrDPC5FGCgw08JpFHDgGjqAkuC5heGiupZ6WTsdE7xYXW8CafBA55XtcyyV2K4iyCK-2_5ULSmJDARSiJ9bsGqdEJ0ftPuU1A3eXCPkbIPNnQszSjGkSVYo0FOQBfmxHcAyc_28Kq8AoZd1bLme_r-xtvJVZyHp8aPpczNRQxf9rJGnOvVBSmF6I3EAd3Qi1FcClGY9KO0thFA21SxyjLTthulDdniH9z05BAN9qNlu8NIBh1bd50pseomK2xgJp6CRJxAsNSseW9ii3OiDxdSwwBRnWOvQ0aZRMB8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de192f8f44.mp4?token=cJOHLpk7cbKN2zUs0TnrE_AG-nzBdsuQjb-Fw6V9YMHsM38MRMnJPJkfoGfTvDySvxB4F6NFrOogkUPSie0aClYBRIXmRWtR8CuDVN5AYyk_B_-9L0LyMoomnompjrrTWn9zbzfTQrusCxfIwHBqbBpxiP1E6QoMenrS0CafbhMNFcuFOptd8teCannvOlE63JJEQ_Cy2DVa39kKx-Vsz5bbuaAd9SdKiBPw8cID618rCmmfdvrZ3QtqKivNvnQDM8lzvQWzWkyzEKzRRwHe8FZuGgyg8DBw4drwO9v-HTIysZ3bYJny6IeqRrLo1LZIb2wOSvQi-AgWidc9QuXynGn33toq7J-7eYSQU6a3bwHNes2aIhfvxNZX_FQ8Sa_dODtPkZrDPC5FGCgw08JpFHDgGjqAkuC5heGiupZ6WTsdE7xYXW8CafBA55XtcyyV2K4iyCK-2_5ULSmJDARSiJ9bsGqdEJ0ftPuU1A3eXCPkbIPNnQszSjGkSVYo0FOQBfmxHcAyc_28Kq8AoZd1bLme_r-xtvJVZyHp8aPpczNRQxf9rJGnOvVBSmF6I3EAd3Qi1FcClGY9KO0thFA21SxyjLTthulDdniH9z05BAN9qNlu8NIBh1bd50pseomK2xgJp6CRJxAsNSseW9ii3OiDxdSwwBRnWOvQ0aZRMB8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریس‌رونالدو با۱۰۴گل در ۱۱۰ بازی به بهترین گلزن تاریخ‌النصردرلیگ‌حرفه‌ای عربستان تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28655" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28654">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1PN3BwWcwWwMtH0b7QhyH6f9QD_cgrJtO3jR05UyrobHFJKr6_6LM3pH7a9eF_4nNBsQFPBDxNAOA6n3zMZHl6nwp8hfysm-OLTSmooFoqilNG8k0Sb-mXzN0b67Q4rUVz3jdoyESE1uBaHYQIfd4BWyA0981tcyjBRnyNjPEcqqiMoXSESaPbwD3wqG6Pf9Mx0WuTE2BN67cIhOLSJielPU3DCi0-7LS24NuW5koUIWfOTjoQ-r-LWUgAHesJ3EGh8RRzw3S9ED-jtKvG-Q1FvMD8zm7II0-AO19Mbk00cRnqE4m_svbWZ9LvHN_OcQ26vdXwzB9vv-kynnlFecg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28654" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28653">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41bc6c0a53.mp4?token=D7DlwMoqbo4BKZ-ITvQqzFcC7OJXIRs7Sg4oICtMP15ia4IgKWzz8mGQ-MTkofcwdM2Go88QSmiggPk8v7I31Eec4P_TSlORCIn-_k1S-BNF08lKWQRMDVySAx2--3i5XyK-MErWFq1Iv8EFxOFypG6bl1H5nKUSBLNVNw_iLvypDC-8eIJLmHxjl9KCVc_WikyJzAHuBguBXTXBSLCkRtqFWzmUijcztp_dqBL2qd94Xip2otf4weW1eNkwEIOPHIeLuLjPNhWuKL7R9c5Ssa96qzPXuDd1RvN9P8_Sw3NA2iS3igysdDrjquJkVibzG3puiIPgBcVu5sOXO0Fd1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41bc6c0a53.mp4?token=D7DlwMoqbo4BKZ-ITvQqzFcC7OJXIRs7Sg4oICtMP15ia4IgKWzz8mGQ-MTkofcwdM2Go88QSmiggPk8v7I31Eec4P_TSlORCIn-_k1S-BNF08lKWQRMDVySAx2--3i5XyK-MErWFq1Iv8EFxOFypG6bl1H5nKUSBLNVNw_iLvypDC-8eIJLmHxjl9KCVc_WikyJzAHuBguBXTXBSLCkRtqFWzmUijcztp_dqBL2qd94Xip2otf4weW1eNkwEIOPHIeLuLjPNhWuKL7R9c5Ssa96qzPXuDd1RvN9P8_Sw3NA2iS3igysdDrjquJkVibzG3puiIPgBcVu5sOXO0Fd1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇵🇹
سوپرگل تماشایی روبن توس ستاره پرتغالی الهلال در بازی این هفته این تیم در لیگ عربستان؛ نوس این گل رو تقدیم دیگو زوتا فقید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28653" target="_blank">📅 10:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28652">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeHUcSyCh-cPIphf5_geC8155R2IoVKbx7Pe_fztwo1-x73zrs-wiw3hgIktZn99MWJ2zCIvEM4IpF_SmH5zhL0GbVTzy6xvm5dNQSHpXP4nH3kkDkzi4akxgjeqxBHHYngm7x6AA2Q_wOexyqqI8Fh7E4VEYlSh3dqiVX_9b5SiZ_Z05m-8UAo7-zAlu3Ie2Sy-NClLo4TCHZmWTQV9JLzwOJEjH_tBDuoMzus_wWG6bHTUI_G_CbGU2s49u4E1uUu3yiml6KLhJq9IaD2BgAI66ACHBMPew-tziwi6Ic9yjo-Fmbky01xPD6-rNHsSiwklN1Ps_YlICAF_hhA64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ دشت یک امتیازی شاگردان سهراب بختیاری‌زاده در گرمای شدید اهواز؛ آبی‌ها بی تلفات به استقبال شهرآورد پایتخت رفتند.
🟠
فولاد خوزستان
0️⃣
-
0️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28652" target="_blank">📅 09:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28651">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7ef945d2.mp4?token=YVgz_to4lSh2E2h6HpRn5Yqj1XE-0mhORZ73BjwyPd9AAVp26lerJl1qdfaRkDIyzIMLJQAKbqzF3oph8h4W-6O-REZ8ufiud6psSHauuN_4gZcskK5A3FYeH8IAnxi9OZXP9-J_i4FOy9R6X1YjYskOMwUlUmedUGSKdoPCeThHyiDigV9XrHFYBm10d9YmEDzUZH9SUUMzYjID-TrGZZe-wcuLHCQ0yc8-Is2OvGnfVVF8MXhkbaF5po4HtEYR9OlHvNzRoMyqvmddpg5Z8ZHy8oUE7z7axZzaBSUUDxqAkN_4zsFV86XsQ61KHxZzGDSxXCwxPGfctGLocDqikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7ef945d2.mp4?token=YVgz_to4lSh2E2h6HpRn5Yqj1XE-0mhORZ73BjwyPd9AAVp26lerJl1qdfaRkDIyzIMLJQAKbqzF3oph8h4W-6O-REZ8ufiud6psSHauuN_4gZcskK5A3FYeH8IAnxi9OZXP9-J_i4FOy9R6X1YjYskOMwUlUmedUGSKdoPCeThHyiDigV9XrHFYBm10d9YmEDzUZH9SUUMzYjID-TrGZZe-wcuLHCQ0yc8-Is2OvGnfVVF8MXhkbaF5po4HtEYR9OlHvNzRoMyqvmddpg5Z8ZHy8oUE7z7axZzaBSUUDxqAkN_4zsFV86XsQ61KHxZzGDSxXCwxPGfctGLocDqikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده الولید بن‌طلال‌مالک تیم الهلال در حال دوچرخه‌سواری‌درریاض‌درکنارجوانان‌عربستانی. او با بیش از ۱۹۰ میلیون یورو سه خرید بزرگ برای الهلال انجام داد. سامرویل؛ ۶۴ میلیون یورو؛ واتکینز؛ ۵۸ میلیون یورو؛ مارتینلی؛ ۶۰/۶۵ میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28651" target="_blank">📅 09:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28650">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLjVvj9UUia33sgxvm6I1N7IBrok7MRlFK0oAZ_wJsNPquhnUwK_rboymaWDP6Xyh6xk6kFCod9KNzrXfNK-aCQ-bRJnCs5sfp819jf4g8Bf7uR2YwW9NAgaFXMjj013vm_Yzs-TlqNp3Ruw_VKjoKhKpMU1FmygORKSX3FMU8i2HafxtY6muZdU3Lbwn644xrv4ZgYI0p1LY749n2RCAkCrSuh9oArBSffu0GyoaOA2aV4iEMk3E56g5aYGmc3zg-9nSozpE0RPJS1HyqbFZqnyFxuE6lULI-e9sHC959SSotFx0FxqFgU1e3PBZGWoz19dYJhtdH-tJR233soWXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تارتار گفته به اورونوف بازی ندادم چون دیر به تمرینات اضافه شده درحالی‌ایری و محبی هم دیر به تمرینات اضافه شدن اما فیکس بازی کردند. واقعیت اینه تارتار هیییچ اعتقادی به اورونوف نداره و داره کاری میکنه اورونوف خودش فرار کنه بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28650" target="_blank">📅 09:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28649">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6abfbbf23d.mp4?token=nqgikrizUOQ-J-0DJ6mQTpfmi8_25dlB87syblwhRyWKHwBs9nKyKeJ0U4iPY3FeBVpCPgYifIXE6Ls-gElZkYjUOMZzo5sGo9FqW9pSXSNG8h50aV2dEwF66AXooAE7XHgAXKEfOkmhbX6VUzsqCV5rSUBLFlYB-Pojwefn9Hbx9O0m5-YyZIISqAYAUkOvZ4m_bCxy1QuQqYIevfqYYz512gYjQbLiLXO0540jgDl1c0-B9rLmDN8hpSnvS0pcYxEWyiquXVRGy_ehWN67RChc1QCwLT9begVccRfg27tIHVyFdqfQOr30pRG3jQH0jzETt9fDufMXuw6bKDSsyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6abfbbf23d.mp4?token=nqgikrizUOQ-J-0DJ6mQTpfmi8_25dlB87syblwhRyWKHwBs9nKyKeJ0U4iPY3FeBVpCPgYifIXE6Ls-gElZkYjUOMZzo5sGo9FqW9pSXSNG8h50aV2dEwF66AXooAE7XHgAXKEfOkmhbX6VUzsqCV5rSUBLFlYB-Pojwefn9Hbx9O0m5-YyZIISqAYAUkOvZ4m_bCxy1QuQqYIevfqYYz512gYjQbLiLXO0540jgDl1c0-B9rLmDN8hpSnvS0pcYxEWyiquXVRGy_ehWN67RChc1QCwLT9begVccRfg27tIHVyFdqfQOr30pRG3jQH0jzETt9fDufMXuw6bKDSsyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بجامانده از دیدار شب‌گذشته فولاد
🆚
استقلال؛ برخورد سرد رامین با یاسر آسانی و صالح حردانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28649" target="_blank">📅 09:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28648">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZCYaLXw0_VoZZue91u0y6bvpIJ6cC8qVtjpGhLyILdS0vAZaiLTx2AjouWAR0Ya1ofFM4mfAFi7i1ltVRB_72Ttcvmhq5tXp4TGaw-nrK-CuipuG7wdX5T4JqLly64FGZ_1kmicMaytljes_0nf-yTdh5p6KoRAWJ7Wg2EtuhsDGfUw6sGjDMJYfsKV7zTvrir7qafywSIqy9XQUt4QOg-NqKOG9Ip83k3qXUZACiZeRxiE-6igY7dg235oaOGXEIb0jZDoOwD66CVNmm1BXKruVGEUEGcfZqJ4OySG8_Ywy-srwL6Gi96GQCaemX8ifGvJIcbqaS83BrvEobVosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امروز مقابل ملوان انزلی در هفته چهارم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28648" target="_blank">📅 01:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28646">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT4-PYCL77_exBmhhujx3ZMAtqTiTgVLfUROnh8JgUBIDoQ3EKf-zeBnnACfqGCXgZc-MpU4vcPBV0ukWZ4DW4GJg6eUruNz9vJseoMW0eRGC8FrWNnxCz4SzlPSrJTcX46C_VCtRo_RJRVlrnzSuYTMXJEH-K8ZRufB-ef59GmnVxqnLW7l5UmdOP4iZ2W_4GweTFfEqvN7485F_0T4-x5tvoky-2_a2YOB8W7_FheD1w_M5sKovCrlzrrALUEK_QbNUWKqa6Nw93HJVPbW5nEPYtZMKfMVrJ3Mbf0j1rvZyU4INAI9gFnSPgWaXN6MWlindC09foEeAS_HQRZeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌‌‌ امروز؛
مصاف پرسپولیس برابر انزلی‌چی‌ها و دوئل تاتنهام با شاگردان ماتیاس یایسله
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28646" target="_blank">📅 00:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28645">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNW2fjoodZMIKDQaaqjfnNIlzTin9tBfTWSDF-cR2yy-TTi262iC_SHPIlsA4HgsFs0v59a7jJJAJVresJnuZHkOEUE_8neIVTA_sBtX67Bgtw9od1q-i-O4-dRv5rc9Gtlo9Qpf6EKFjymqGXyAM9FUnKCLmKXSHKZAgBHFghlrBFZOEv2veVoaV5EqKKJ0DYDCpBMWteIKjpMmmAP_GtwaCC6IOM7M4Wm001ahJ5YxJ_t-jiuLWLdwfp_VVAYuV7opMyDFNxESg0L0zkppiWCx7pZX-44u_Zt_Dkkx2VCnmvfiaQh_qwkLMK07YuQ7JPEVC96a8zH-5ck1VkImtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
ازتساوی‌بدون‌گل استقلال و فولاد تا برد پرگل‌بایرن‌مونیخ و من‌سیتی مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28645" target="_blank">📅 00:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28644">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EORjeolOlSguaESEW2-6s6KowAQ2c8x4YMauXxs2a9Fpjp1nUTImd9LKT-7EZH3XLSV4UIHa3Of4xmhkDrYuuT_tCMMz4Kzelpd-Sef3tvYH6MwLYcBvS06Q0wuQUMya_bsvtxd4FrCFTZrjnBe3IIbr23LYDa1aUn43qEcJDXPIxVHyxDNU9spT-fiAaQbf2H-RYkGKLdd9YJKBbjYNdJsBDGCGZn7-r8HOFXxEfUdPFJkzDG7SCHuNJEFwlSF2QsnFITnQ1hZq6MSBFm5ZLH4tD5rhkIlOLnmF82fBof7OMoHGFmhw1YVAijp8x4UzHLFlVJZp1SnttDb46MjWTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28644" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28642">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJO_980BfloZm2RCUk3IQB_gECiOQaOAO5HZha26mbAvsRns2Mc7nnyPtrA2TJupCFd0sjZmGR3ttD-TFWK-5BFORsEVeNP2afC-tSY7wmrbGALXGzBLwVZSiSMJldU2nSYHHy9eJQM8HUO-umRBtF5Gsh2ymcf201zJiw72qQd85mRtREofDLI8B80ziNBjAnnwcpnt-L2VKTKFeCU9ueaV_Pr8FxIPOCHa_rOjCuB6nkTIOpUXsiubJRTwKmzQ6-Xoc3SRTJB4vogeexuQXf1EieraKd2OtKmb3tKhe4kT6Z8IXFxnUiFY0hUagsOxml-YyYRL5q5ymwMGEK8d2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6-gkF20n9r4G9ILgEWP7AnG4hY5ans0U8te9mzGUAOl8f0jkOTfXCJ7o94m-O4gI6umMkqqtDfit2hD7T58jR-X2sR5Yn4kVn6fDlVGTtZ_9z0NswsoZCAUlDpOxZAenc6bZ9vmyNFQBTKwwnxnB5i64sMo0KXZFuvnwKj06I4Jx-n7wCB8t11MgvqaqDOtd1Vtyhqi6Wg3jI9m8aH5_Ty9Lvs53v91I6YgvP_a-hSxTGrgY6JHVfXAuU-YOMswHMwoXoY5KT_m8lgOxBPBFnjG-cbnarSWseDYwyfg1y7LMWiyjbKNsT3a3ri6eL9F-1Oxht-KVLPZe9-BexWHzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ دشت یک امتیازی شاگردان سهراب بختیاری‌زاده در گرمای شدید اهواز؛ آبی‌ها بی تلفات به استقبال شهرآورد پایتخت رفتند.
🟠
فولاد خوزستان
0️⃣
-
0️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28642" target="_blank">📅 23:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28641">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISpmRaq9gw11x5ugynxAzMrc9zoLOlXHXwQ9nC9onwSPPT5LtoAntJjkK5Sgu218XRaTrWPgf0IOKpScrkEJ6WdvEQhLZsA1IKQy8vZiC_455qbhTKwNUwyml77VKIKcH3xH0tOhOb9QFbUHU22Hrv0UXwu7pQpFiNj_upRbvoUbwJsoosw1PtQHol_wPc0X11DsW1D6w1Rc065R_-RvgbJeNCAhgKAH2Qq-LcioaB7Ug006WH9x_jwlskY-teksd8IyEdV35FINpm2fP1ErI19nJq-YZO6EdjXb77qQVlkg8zs4OrzJD5dNVk1YBIH7IvgYQ7mYKHA0HdIC4-t5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول دیدار امشب‌دوتیم‌استقلال
🆚
فولاد خوزستان در هفته چهارم رقابت های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28641" target="_blank">📅 23:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffc6c7296.mp4?token=AG6UAsk7x66jyNs4b06rec4Pdp5xtB-MjFDl5vXP_xLYGz7quJNAVeYvoL8WChZj_tdfokA_SPGWIH6dpp9pwCfyQeabk-fHWVV1X0PZ7enr2UCHC98YZkHxTv-QlQICCV6-zLGutQQG2SeVM6V5tT3XwZdP2KUGi6ATci73P_fq2RkVIgKWLLZ89THdwhgvOwo7hDbu38GAGAiBPU6tiZ1cdt3FiMmoROC5QQsDGbTzLPw9qWXs7h5sort9Ylj47WZ0QGR_uw_Ey3wvKX0YxfCCzANAVsQHgpPdY5I7jAK2bV_CZOK7B81JZKCK8TA4JBSDY6igyLH1hZWLFvAFeFBv-CIYQFusIkm4DuLnuxOLjRYDzb-AzQN96VrRZHJKP5wYOPOtE6zyz1DfLWHGrH6NKSFMgNT8IvM5TaXCgHOW3wrFleH0jjvlb3loCk3JnMTXPfWmi2uhrxm11glI5vsvIlJ_c07vaPdmmkhC1qF7haofuAAXGAptcvAU1ZxUxSbqkoctTHayXLH8PHZFYkRRy_H_0trlJcBdIamQ2AUBOYcIY6-EUPKHQ8tWosJvJVNZMDrpA7Sbf32uCTZrO4E9FKOlAE1mqQyga3dA3uZL8i15M14imNQeqzco6Q6TjjMgVXX8lt7SRkwhS2YjoyFdaKNj6Mw2N7LDWA67u4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffc6c7296.mp4?token=AG6UAsk7x66jyNs4b06rec4Pdp5xtB-MjFDl5vXP_xLYGz7quJNAVeYvoL8WChZj_tdfokA_SPGWIH6dpp9pwCfyQeabk-fHWVV1X0PZ7enr2UCHC98YZkHxTv-QlQICCV6-zLGutQQG2SeVM6V5tT3XwZdP2KUGi6ATci73P_fq2RkVIgKWLLZ89THdwhgvOwo7hDbu38GAGAiBPU6tiZ1cdt3FiMmoROC5QQsDGbTzLPw9qWXs7h5sort9Ylj47WZ0QGR_uw_Ey3wvKX0YxfCCzANAVsQHgpPdY5I7jAK2bV_CZOK7B81JZKCK8TA4JBSDY6igyLH1hZWLFvAFeFBv-CIYQFusIkm4DuLnuxOLjRYDzb-AzQN96VrRZHJKP5wYOPOtE6zyz1DfLWHGrH6NKSFMgNT8IvM5TaXCgHOW3wrFleH0jjvlb3loCk3JnMTXPfWmi2uhrxm11glI5vsvIlJ_c07vaPdmmkhC1qF7haofuAAXGAptcvAU1ZxUxSbqkoctTHayXLH8PHZFYkRRy_H_0trlJcBdIamQ2AUBOYcIY6-EUPKHQ8tWosJvJVNZMDrpA7Sbf32uCTZrO4E9FKOlAE1mqQyga3dA3uZL8i15M14imNQeqzco6Q6TjjMgVXX8lt7SRkwhS2YjoyFdaKNj6Mw2N7LDWA67u4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
گلزنی رونالدو در بازی امشب النصر با التعاون؛
این 978امین‌گل CR7 در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28640" target="_blank">📅 22:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28639">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feNn8qadvYTcWTCsMUUPrHrDsfql_kASI07T0zvjqUSHDk7Ml5qSqUS0xj0l8Mm0ZhirZP_JjvuIaXLv8rHSZSfbUTw_s6hBAp3lUA95TvJTvt7dzNriFW4gQ-k8-HUSdomkTUEf78cqLx-rqaeHD2MddllK69C3lk18H-aR_48MDzTTO_nUdNWHPQJAk91IRlQvHM-GeypGlT76e6FRAUcuansTNfS5pa_uIaNbNZKP4EoPlvqAqS8tG0fgUdWbxnDg1Q7ZDvFcSB4r68zoMPN78WP3NIZ72YBfZeL4T1cTbmEnx8Val8rovSQw6Q48en3_FYb9QPup-gnQ7amorg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شماتیک‌ترکیب‌استقلال برای دیدار حساس امشب مقابل فولاد خوزستان؛ ساعت 21:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28639" target="_blank">📅 21:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28637">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EK_PIVrPBfcRtG4qIRCI3bvlQ_XT4YyLdFDTrrLTXuYNh0yYLGzk3smDo5KGEH4jah8_KQ_F6oSODQ-OambriKtUJ0Ua6tgSDJj8KuU9m5w_Yitp8mT2ligZocYwTsUi2FNf8mPY8PkoybpW2zZMO_PFjY3dd5I7ImVqVx0V31hwXfu8iyIvF7yx9_iGJEfVCkAjniSbTHAUBBWCmeT4eZ8alRUqgZXXwQJZtW4fU2wi0hyabDgsTYoKv9uLR7D2Z5HVeac3KlH-amHlq2YHtJE6OMQedlMgM00A3urGcxG36sjDtDwlNSE6ilCuoJq1vriR1qqu2v5Q-Ogd7IqMWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28637" target="_blank">📅 21:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28636">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17182aab77.mp4?token=v1uJD9abdO9Eq0I1A_rPx6nqaV9si-n0r-HR0Ji4LlK_GpcrkcNW51aJ9YGYhe_QSV7TODBUvo_c0WXau4cyb0rQ_pypFuhWmzLlIOCLoN91kmkwGHFh8DcErta4UALPOBx07OfpN0_-lo39oE11TBYCMEP8noC4i_r5xZ7g82nRMJM1b8nfM-38k0EinzYjzGqe3_2PGjdDh915acxTiBKEuZSnT4dnCbDkonLp1UUiC_bDcPVAOBN7DYv3cjOms04kJ9X_Jk3Uvs5s_zOIyGhIrzlSn7-Gko75i9P-KnnVNFvY5Nisz3LmPEWoKWBhFPXMDgffY-b9Q_4W6Q4iiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17182aab77.mp4?token=v1uJD9abdO9Eq0I1A_rPx6nqaV9si-n0r-HR0Ji4LlK_GpcrkcNW51aJ9YGYhe_QSV7TODBUvo_c0WXau4cyb0rQ_pypFuhWmzLlIOCLoN91kmkwGHFh8DcErta4UALPOBx07OfpN0_-lo39oE11TBYCMEP8noC4i_r5xZ7g82nRMJM1b8nfM-38k0EinzYjzGqe3_2PGjdDh915acxTiBKEuZSnT4dnCbDkonLp1UUiC_bDcPVAOBN7DYv3cjOms04kJ9X_Jk3Uvs5s_zOIyGhIrzlSn7-Gko75i9P-KnnVNFvY5Nisz3LmPEWoKWBhFPXMDgffY-b9Q_4W6Q4iiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته چهارم لیگ برتر؛ شماتیک ترکیب تراکتور برای دیدار مقابل چادرملو اردکان؛ ساعت 19:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28636" target="_blank">📅 20:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28635">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28930c27fc.mp4?token=n6-AU-4uSClrn3MSRkJ8uwOu8CEOSgJdeATEU7B1wRZtWmEo49mxAkBQ2rvVYLWV0y__y0IunneWn9eRDr_wBRw_ISy5p68_vk-ZlzjToZRKcgiv6PhrKZPvEWWJNn401ZiHYyFfwfipqEATKKYth22DuFIhuXm7HDr9cz8RBxsKMj2yk6-KepQSsROWyetQ_Z0rwrlMNXrdPt6IxopkeDy-xdzygH7Bskh1tGqfZW6ex7CyN09cpp8agDvx--Hj9HeonG_t_hMaHJH0BTaDEE71EYdDM0rtGGNe_HERO0Y3tU_gA5fCnSk7yxr3Mx4gA8yU86r1h6gTZ4x5DqVpxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28930c27fc.mp4?token=n6-AU-4uSClrn3MSRkJ8uwOu8CEOSgJdeATEU7B1wRZtWmEo49mxAkBQ2rvVYLWV0y__y0IunneWn9eRDr_wBRw_ISy5p68_vk-ZlzjToZRKcgiv6PhrKZPvEWWJNn401ZiHYyFfwfipqEATKKYth22DuFIhuXm7HDr9cz8RBxsKMj2yk6-KepQSsROWyetQ_Z0rwrlMNXrdPt6IxopkeDy-xdzygH7Bskh1tGqfZW6ex7CyN09cpp8agDvx--Hj9HeonG_t_hMaHJH0BTaDEE71EYdDM0rtGGNe_HERO0Y3tU_gA5fCnSk7yxr3Mx4gA8yU86r1h6gTZ4x5DqVpxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
ستاره جدید نیومده گلزنی کرد؛ گل اول تیم سپاهان به گل‌گهر توسط کسری طاهری در دقیقه 6
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28635" target="_blank">📅 20:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28634">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bD6fmoGMgOsRpt4HXpup0bQKbvvNnh8yx9l3mw1gKHutxmFidUxhiO0E8ppr5lTWIEyB2qrAdDtEgRXmR4sJNd-XZssb00kPwcwIxXmb_EJ0iscFUgiqEb51vPUgaX0pwDYZcWP-3DZIlVriUlnbi0FJqs3j93UHVENICuiYtPyxDoKX6BpXaXjy6D6ZiTrkb6v6dxhC4rCB0MQHaMl1gMiO2dRwln4avDlkEvxK678_R-IfyxR68zPAqGJqj_8OMFnErAJZGNq84nV4_AY2dUDneImfXrbIe1xUQIwihMRQq7hl3sh3WRMDagkvopIBw8blVXwtxOjmvKyahy0Xlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفته چهارم لیگ برتر؛ ترکیب دو تیم فولاد - استقلال برای دیدار امشب؛ ساعت 21:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28634" target="_blank">📅 20:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28632">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mM_8PCjfJ_n-aKUxxjwzHQyjdSUlthKP5KnceOhPUT3cSnV9rbVOytC8N33Xysbm8ooj_9XiRLcrls09qjkM8POuM6WY23_Vcx4n8rQiwr0TRrvsvp9ni3gQZtQFy1lAnSLl_InP0Una3PrrhDH772ccLXj8Blqq-RPxXh3eT3wCMUKj6RW2ZzT4TJWiiZVVBef-8AIpknh17QhDK1Bu6xJbiD-hDd-4MGtTEPB93Czj0V9pYLKxHFMelmIZMt4EypgGYKpdK8Vl818N-257hTxVlN5PFB4wA5bkjPJwEU6X7yFjyckfcA40b_w4c1aamB01XsnNYQnSNxdaUa4kMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PwC0OmB31zZCF-A50ZLxisquvMmlSzzK_6h2n3vJBX9vVKoaycAipAPDmxcUQrNDTJoEK6uYDRiL0xdIKwkbSXRqEGFXRGDlNLyCA3gANbjHLju8hxE5DM-r1u6r9WulgRSL5PhbqyIHL4crVZiBFgiiKTrZyQrJ2kBsvWU--A0Qf-PsJK0CuU16swUFXk7ctndtEFmeU2U2C8gEgghIRa8qXcxxdsl97k-fQHJZ3Jgn1jBRiy4u-0HyzkxmCs5G_lg-Jm29kpHXvkM2YABoioxvy0MJ5m1nMHWZtT7f9rgL9VtsbCF42jEGnn_cajtY76LL03ZZJws46djUw3JE1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هفته چهارم لیگ برتر؛ ترکیب دو تیم فولاد - استقلال برای دیدار امشب؛ ساعت 21:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28632" target="_blank">📅 20:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28631">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b6a569c2.mp4?token=b1hYLZRnDUI6m-KdS_hD3M2f1ZDJtrPQ9kQwy8ttIsOXTzI6uE-agh3v7skHlp8QCpmZmX6Ol9rrF83K-OTKr2NvrDHkT6ATvhCU3uvGQSGi8LYlf7ixEX-guHM8uZ8t7udU3YktFlC064j4WGZoMClhStvRj2SBslDwzIyqBGPJj6POZF04jEJnzscqv_JnN4nQquSK1xTfIC8bPMvw4tvrpu_G9A4lGSvSvZyq4KzZYNkw_3ScHQwPw9PsxQB6cUvm2LivO2tiYBXV8-6Hp_lm8RDRHbtxQkElJRKkeMOhyK1zxNJ1zwqJekNJUz7FZrAnBRApsOS68iCPRW_1UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b6a569c2.mp4?token=b1hYLZRnDUI6m-KdS_hD3M2f1ZDJtrPQ9kQwy8ttIsOXTzI6uE-agh3v7skHlp8QCpmZmX6Ol9rrF83K-OTKr2NvrDHkT6ATvhCU3uvGQSGi8LYlf7ixEX-guHM8uZ8t7udU3YktFlC064j4WGZoMClhStvRj2SBslDwzIyqBGPJj6POZF04jEJnzscqv_JnN4nQquSK1xTfIC8bPMvw4tvrpu_G9A4lGSvSvZyq4KzZYNkw_3ScHQwPw9PsxQB6cUvm2LivO2tiYBXV8-6Hp_lm8RDRHbtxQkElJRKkeMOhyK1zxNJ1zwqJekNJUz7FZrAnBRApsOS68iCPRW_1UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌چهارم لیگ برتر؛ ترکیب سپاهان برای دیدار با گل گهر سیرجان؛ ساعت 19:30 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28631" target="_blank">📅 19:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28630">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1bdc45bb6.mp4?token=fNgQ1Muog3RlwHfNiWhyroNZvgggA_C3GRfEsKk_JhqVVkNpV4MlKd4kVUErMWRNv6DhqU1KX6G6GzG4lpqq8O3hIPpXO126UlaVNijbEx87jCYuVMQKw0st-4cNj024kGtcwwZUfsvGpXK-npVJiVyvvJbXYvqikSypzmGEVdw3EuR12zJv1O8VBsd7lSutk108ZFWn1UmSbVuPXvzsEQz97bH2c1c34e65shRcN8eUqv6qnDLS1gD5PGUQcBHLwRxXr_2bJHLQyGj-L2WUoCiFGzGHeKs6D4qMJzVEuwEKkYApfvBJfIEvKE9x6L1TrbfbDzFo7FcwKbmbgpckwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1bdc45bb6.mp4?token=fNgQ1Muog3RlwHfNiWhyroNZvgggA_C3GRfEsKk_JhqVVkNpV4MlKd4kVUErMWRNv6DhqU1KX6G6GzG4lpqq8O3hIPpXO126UlaVNijbEx87jCYuVMQKw0st-4cNj024kGtcwwZUfsvGpXK-npVJiVyvvJbXYvqikSypzmGEVdw3EuR12zJv1O8VBsd7lSutk108ZFWn1UmSbVuPXvzsEQz97bH2c1c34e65shRcN8eUqv6qnDLS1gD5PGUQcBHLwRxXr_2bJHLQyGj-L2WUoCiFGzGHeKs6D4qMJzVEuwEKkYApfvBJfIEvKE9x6L1TrbfbDzFo7FcwKbmbgpckwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی احمد نوراللهی برای اتحاد کلبا در دیدار امشب مقابل اف سی یونایتد دبی در لیگ امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28630" target="_blank">📅 19:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28629">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pribZ6sD0dS5iKXprjebNJR0aEBGJvZAw22gffqIoVls6mD9KYBI3gyAxJvyoXELfz_VOF1yBM2iJIMlSss70f1B5MSrYmJKrWuhEb4RH83-KarHJA-NlojFPyRPmul8NnnCsKysHHRUFq7FwyY1B7ypBuoPb52lKa5JOMfgR0E672_Pc0L00CYORbO-key1_Gamj-4JP2VA6Lk6IgaMTD62igrQHDw_nFPeIuBb4R_Ln2uUX0P_CkITrXqyIrSsl54gU-EgZF-E4yWZkls0zDIpaUIf5MibckbWhG6h0C-X-IXUwMNBLtMxDV0zcVzmxPQRWR2g1iH7EvrwoLUSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم لیگ برتر
؛ ترکیب سپاهان برای دیدار با گل گهر سیرجان؛ ساعت 19:30 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28629" target="_blank">📅 18:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28628">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKjnEVwxYaV6hA8g2e5pRkmoyesVD3IDo9s-o4mFGzYu0-lF8Z9uZWrkeerY85CLS2yz3dGBGJH0aHDXgj-enGEQHyBKk7Mh5Ss4qqZgzgFA5JtHdGBkXNDCqkarZlRNHdK9B4IwljcTcnxcRzaABzVv6dTuDgHLhSmZemWMjNrbjTg6O2PTov62h0Gn8mXUvBrIfn_vQc0AoQ4AfssY3P3-yzTGZDtPK0QTFDXBolBNl1wxElCPT0ZhkM0HKq311GajKX6r4hui7Hlza5kEUel8SiGg8kvw2tTvfo5Ef40liCS7DegUfn0vvoFVME8s4obg072nJx91Pd-yAxrJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لیگ برتر؛
شماتیک ترکیب تراکتور برای دیدار مقابل چادرملو اردکان؛ ساعت 19:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28628" target="_blank">📅 18:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28627">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cug5RPA2q257mDL1fBFiV4Va70FK3-hsZMxgg556riDtJFGH_tPOjxrsQErJQuuSLiYEeRCzqfm7D0--RGVCSoU4U3hbg7Ab6gX8fJze9d7r9jCX6iJN8dMl8B_WjmZdJz3GS0tTVfFpzjGXtxk27bQrTabL6-GCNUKDzGu5_yZwuUJhIi87a-xCl1vRFeS8ZiBwhVfmNSOgDBHI7ThflJCPIolDGnkQRJkF2um2ZrYENgoDx4MmwRUz2z_a_Zt0S4m_E0m2q7KI7Tk1kILKtmiB3-fH3QsZ_ZbFhvnVMCut1LHLOnLY7Vsuu7utRB94G4QlEY8zmL5gx06PSKjN0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لخ پوزنان لهستان با الهیار صیادمنش و علی قلی‌ زاده در لیگ اروپا مقابل تیم‌های مطرحی مثل لورکوزن، بنفیکا، ساندرلند و کریستال پالاس بازی میکنه. فرصت بزرگ برای الهیار صیادمنش که کریر فوتبالیش رو یه قدم ببره جلوتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28627" target="_blank">📅 17:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28626">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFz0AvGuiCJylXIgWqAv1WlLQ5rzhA4URztt32nqHF7RVG2XOSsfcDnhq5aGsivt1v4FoinpGoBTIlLbGaZa74uWsWKxzsuMJiTEN5KJWur-b7ZLNHPsO1hFeg2ZtwBGmESB8l4UGtsuTsDClSGggNyMKtjaaNLc92J3AiXf9J2SQOUXDUucZ0C0GkF-ktxX9WKNl6GSsIhQY082jPit1whfMGVSWUwqkfPn-77qdOSGBEHLLfJgBvuaOBNAzrmmrWNyf9EsAzE_jFnIsbZqcTO3uixXLlEd3iw1xZIv2QRvmgcQWgBfk82x_KxucrkJn34xvXtxqXyNqjaOG4fiyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل فولاد خوزستان در هفته چهارم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28626" target="_blank">📅 17:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28625">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwxtVDDJ2uVBu532gaYRXbx_DqQIwaGZpPXO0-5KnfcNOmQr60NSNVnkrXym1XPK4-ZTCmtG7NCbtHw1sAwrGEGXTzJs1uqOE7-605Icef09rP54riF0LE1cZ5Rr7vaZTb6h5LrztO7cTSH_u5wbh1hjis332qJ5ImHND4uC-z-BzYXoWWzMnKe6z17Oku0bDd6cIWUgv95l3LbHStwOVTLVgMaGEWuA-IS75my-6F-lPdKMy92VjbY1tWzxnT-Jiu-gSveFrGLI4vqCr95gW3wh9-WwrnexIuBH_ag-ndfX0T8wV9IS0tgvmBQy4xkbCKs4M_DoYBr-2IW3XX1pZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارمعروف‌شبکه SPORT اسپانیا که معتقده که امسال بارسای هانسی فلیک قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28625" target="_blank">📅 16:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28624">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO5jNhKP-0bXLPC6Qza9avbIFvXK7NyyY7TtmXE9qqee63EHvaEroPFtbXuKrZK6yOuZFOrsRBFb_k5ig4VHeZACUf3d06C70eXD1HvdsEIYjFx0hfEDXfZSoeSnVwzhLX80K7M0teNnCQSczN35jR752kRcKvRns7VG2UkOZodJZBvXamon7ih5p5H2l3ngNx7hmP-LsWhtO2Ms5y3bkTeI0p58RtwKkc3isTewBpavoMjlR-tfzEcnGRh4fVlLEZZii-mt0sueYVE6-9hHNlKoM-YFfP9x4U4YRd0iYrVUfldyuNb8jWaM0m9g0ddqW2l6nncfO6FJyj_KybNnfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگاره از تارتار پرسید و گفت چرا اورونوف و سرگیف بازی‌نکردند؟ تارتار برگشت‌گفت به دلایل فنی بوده و حتما یچیزی‌ میدونستم‌که بهشون بازی ندادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28624" target="_blank">📅 16:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28622">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ic8axqmlYrwlExGVxrJDtmTOqCb6XQu4WhJnVW2ahs1wkenWQUttkCQzyb4M78W3qgDo1FReCup-WOv8Fm0Ogo_zWawKDrcPwrt39IS3jAN5gT7Vk1nae3TaBfPwvLEYSMLuCyTklUFCTP6FCqCtUS3YPJhiipIzVB-AdpR0eua4VhAY8TXauTwymUIZUhhQi50s0Npie0k_ww6iZ6NnxXGa-SygQZtdpO6hicxZzLle_pm2LekhMuul-iaE9W6pZ15XTDvBp-qPECOfK4AOIndjJKU9l2yS-nWk_Z8NsLnWDIW92iJdemsbOe-H-fUczw4EJVfEMNt1EQY5LNTmMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guqywj2tjMPkvX-uVYOUv74W0HevSXz9QhPt5gbUSlJM-aDFOApNwRDxFGsOxWP6lzuxVioxdG8VXKVvm4tpKg6LCSD9GeCa1U7Vh8SoHKf66Kuv1WlQvZpf_VDCfaqb9wX4CqQTvm9Ber56cbNdl4A7-cZqCgIl4L_-rV50usUSu6GxIPv5G2Xbn9pdb29_DyAtRT4dp5b-7GE4oo_j1AF0kTYd5MTiRDd5XU_dx7ubo48q_OYAyBp3eo-jKwBV0hf0ZsII7l420q-IT__EXF7iiuaQNch2ZYfS5Ni0nd3-D8xycLoabpdZCUpdwXDSXNpwAqHGgyQJWPM2_XiZoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
خبرنگارباشگاه‌الوصل:ازپیوستن‌مهدی طارمی به الوصل خوشحالم. او میتونه به خط حمله تیممون در این فصل کمک کنه. بزودی با او مصاحبه میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28622" target="_blank">📅 15:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28620">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQeZBLOTiKl6RFE7QTW80FTyMEs8tUvhiZ5rYIviF2WiD2pZKqplA6v-v5UvdpV4tGcsZJEfUmuGkZIJQPHJxeEHALOYyyAkfdYgtjTOVAu1msVU3JNo39EB60mnx6rtbVuNE6RRND98ze1l9KZpRvs6MN6PGxqDdzNuufpt_eQ8z98BUCer2et0kS3enrb65hosfotm2BLR6xSR3HFlao0aLlOrmviKkSIAbVXjBEzXiQmj-AkD8nTWbMM4vmICQUsytvYPbQL5SZYeProLnBxONVEXIpncKC9DMBITBUPp-75MMMRRaGJew4jN-7AdLIVs8MKbO5isoR47P7gwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره کننده کیلیان امباپه، وینیسیوس جونیور و جود بلینگهام درکل دوران حرفه ایشون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28620" target="_blank">📅 15:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28619">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dojPIYoNJT2CeE6bYqdouNqze2povjY50BouFpXDSc11UOvIxf5YQBATvvNQLqD5BcRpfKMErM8tS9enA7GLNm3mXULzoxCe2VFNCX08yCm2P2kMObFyNEurLvzF9GGrw1lJbUdwpUF7u-Em4BfzpmtIu17guUqS6Mh7bLVpcYenBdQV5ohcNxj-NuHcIvTWBG2IacSsVTtob2jIuT4EEtwNWYkOEJyRi15owaA2p_9TlJr8bEmnQd_uqLbjzLqRSr1A1jJrcb1_l6gWsFW9QcCh1ZuY5nScg441iML3tyzxTPQ8lpyQxN7rzu8Oz2on5XiONyTcgj6a4bzbizPu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامبک دیوانه‌وار تیم ساپینتو در مقدماتی لیگ اروپا؛ پافوس باهدایت‌ریکاردو ساپینتو شکست 2-0 دیدار رفت مقابل هایدوک اشپلیت را جبران کرد و با پیروزی 4-0 در مسابقه برگشت، به دور سوم مرحله مقدماتی رقابت‌های فصل‌آتی لیگ‌اروپا صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28619" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28618">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_TR1MfQQcR-eqJa67jDnSmE8TT3HnNopKaTLEk1bdm5ECPm0m8t38MkCRht2qbuwIEUge3QTvPU1hbnKHrVd62jyMEVrpZg-rcK9pjXkCBzxzxVjaZGp3UDRJwIuBT8otiYNtJUILZS1UFGQb8GcsAE9CKjn0x16F2cNg1sn4WrZEAzrlB8TTd0820-hyJtOx0gKBK2J2eHD9_XsQ-vkqWtlZkLZVVCHqchf7w1P_BlsYuRIgWnnAhm96M1oo0ofd56iuTExPGZ3hCp7cL_Fp_Vk4pTZHpJXmLyxvQCYEOCIvt3stQ-9DafXV4iFtUc2z7ir2phlvzfFIkUXj8S-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
کادرپزشکی‌باشگاه پرسپولیس و استقلال در تلاش هستند که ابوالفضل جلالی و مهران احمدی به مسابقه شهرآوردپایتخت برسونند. 48 ساعت قبل از بازی مشخص خواهد شد به‌بازی‌رسیده‌اند یا که خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28618" target="_blank">📅 14:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28617">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNbQs17xDWgXQEOOh-1oKsoEwG4Eox2z_vDtECRce8nRP_QAQxPRGOvpmDxOP30B50NM5nUmvqlGQeNecOncTD_jZH-2Q_HglrncXqXm67qy2JRCl_Pig1hIcbppon77Z_bSs-dreLyDquxKQO0VV9LvNguUbYNTOh0U1ZnPpj-syHjXwUBjTOGqqOfRjX9Y6O5PB4p27Kc1CUhIEQA7byKS5jCN-TNa-xu--X3_mLNsFGunA83h-RukFF5uJ93lphuMxqcI0atFd7nANUucl2EUQ8wFMPpykDE7a1WuE1yDFVCkLWcs_Tjvm3Khm4kJe9EQY_e7504lL9wIC0AKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛ آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28617" target="_blank">📅 13:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28616">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADgt43dE2H9IbOzAD210Cj2csvJMiokIYvIUKMAj5WrO5-UzNKxvSy9nev8M6ioMd9g18R4Kdm6aNNW5W3JCQKhC5OViybELkMRT01e9yT0HbHcxNmU0RUUaIXqiCKzuBUv7YaJFRv4AT_txkfdrUqCtHnAL3VnM_eZC4a4dx9K0xiCmf5PW15gtSXfW5A4_K3OfTNVM1ZqYmMrBToW3Qy4hq4811K7QnWeE2gju-P5PR3hkJVX_EnLrNc7LQO9aeHV1Fl_4RcV1sARrsLLmWlC-ND3nVagQ4tVvLq-TkX6NuOvOVa7D4f8x5ePXFSw_iSyakLCWyHrr7nuDR3Ar8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
واکنش خولیان‌آلوارز به بیانیه اتلتیکو: حتی اگه بدون‌تیم هم بمونم در تمرینات اتلتیکو شرکت نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28616" target="_blank">📅 13:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28615">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dubHdjXBGUZDnRVbUnbkGGlKaKahAvzp4jSrzcPjp30qPfFIUKufl6VOFIPo8HN4r5x0FQYHsXauSih1P2ti9KLAO_vNLRtabB-qxZgrSYkggaNUK5TND_JILL2BLJ0uidRFUcFSQe_xIZfGmF3WmF527UFJ1YeUeeyBfB-rUxID52m-I_3_gzBhc7qG6sxKrRp2HkC-GOHdSz6lvcMgRsSTMK1VfPKsIFhkoBgS9TeLjFui5stdR1RVdoQuluDNCI2_oXK77NAXjWFl9viLMUtyBnA4zlJBIflS9dPHYGeMc8PHfeMHcfKW8bK-pgidYdkIFiSvYPXs09oFDrk3mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه‌تراکتوربدرخواست نکونام با عزیز گانیف هافبک دفاعی ملی پوش سابق البطائح امارات وارد مذاکره شده تا درصورت توافق نهایی با او قرار داد امضا کرد‌. گانیف در حال حاضر بازیکن آزاد بشمار می‌اید و مشکلی برای پیوستن به تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28615" target="_blank">📅 12:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28614">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9HrrU-s9wa4SfndOMWV7j2_KvsN9H0AesiS3A7Ceh5g_p7MeBUfAEEg2zM2VwKxp-dT0ScVNPyfodgafsXlhI9uCQY6q7TvT45L0WLu1n3EIpSAvRhpjJgQT9U8jw8t9wgchCBWkzF0LcgSSVlfsESt7u_f6Ao7Zw5myN1UrNbfvO4NQaO2InmH7qHa7MAYKbj5Yaa7H9qanuYNE017xUGgPYRbfYfBGna3PDQKHyoh42QPBBLfE_0KhmbiL3XCxQMClTcjkQQ9-Ainlud29bwJqh78kyndeSlPaZe6UsAxGTZENLotzhiij71xVj78a0Sul-L7Jjl8yTO1zHQluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پیمان‌حدادی‌مدیرعامل پرسپولیس؛ پرونده نقل و انتقالات سرخپوشان در این پنجره بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28614" target="_blank">📅 12:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28613">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhMDVdkAv88xJyVMUPxWGlflFdLhWAKTt9zGQl700BBLWMEWMPuyFisBGXlYX5s3h_r456PA-0ki3RFjK6tvMMYZgDCZa2THbiKjwuyYHkk4lhXDiYPO5E_vBR1zUpHfa-A0KkZG4y3tODVqaaAmaNRfuk8QEVTzKHJTUEY344JMgd1oCfoq4TmHcS8cGIVs8gCzXOfDQejkl-o6lge-bP7s2TYhtwHem6DbpRXdGIxNRaIaLluiKy8QMEv6n0hw6kl-TByRU1MNZGsoQfnY8ZQP2yl4zvFnsbf9MAt_Qw2XQ7zCTcKXtI5wOXj27OpkiKVKFgoQIqcT_66iFflDNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران: دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/28613" target="_blank">📅 11:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28612">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVodDbjlACJpBvTzeaiDiW-XSH3xByaUvUBK-4XXznI7lmswU20jNyt9Y_3QIFmy5_oAu5AQ8GBtNcTjXAyEf-yj3t4oJ1ogWpVB84LRTSw438iMss0VnQcmYxj3aob7lrWrGwhnYWmVRgEHhBe4prw0ps8CXSq0CaObFVDi0sWUcfmLw5790AjHelcvym8qUlaDfbWDjwqxEL35H2E_fnce21MJ2TPCSduk-_ZZe4kvoHTungbUB8CoNM2MT9d57QZnxHLnfvbd-7wAwo1Xz7PZGl6f9-yrihjnWdxewM7mP7CYpzuxSkXJMqp5x_rSKLZEe8ca6KyjPjxdX0MAWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28612" target="_blank">📅 11:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28611">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5mACEJSPCxTlK68Jh2blw_ShWHJkq7IAyjX5S1dGXZ_bljhBnn8tJLJJKEY1PjPeq3_PWYa-3q0OMZuObXO4pmnrU7Bra_nvYF8vqVpWvWgc63PDHwEWHoFgZqpZJyMmqHY3kSSQ31gBFH2sCfNmjzApTVdutWrp3Q-61jb2Jw1C5bAR1VTbbaHkZnS4wR-RVdZmzMnhalse9ofrF3JA1cPYuOr4_Api3VCAoTZlIMTJP0yM-ECTMKX4FThYar-sEerhESv9iMPVuZQeOqcDbNvDALkz1igRn8Zu_oI5EnxmKJ2PStxdalJ780b_IJqw2s5UNChVwEhS6sRH-ipIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/28611" target="_blank">📅 10:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28610">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra2DXv0ZmHV3ePe2VffYDxxKXJTbMYm9mT97pvr7rFnDA1ZE5-dFwzPT_iABBsRR24EEC287UsTnVeRPEGn41bnE5DgxX5Px31BDyP67Xw0HwQNw8Yfv2bbIQYpYyBB8OkguHzOXG2D3hcd8qKE_U2Kwk_5YyOZLNiGSyLSHWvPFJzMAn1ZAoBGC6w02dozRLY9u-8nkwL-I06992Sth-pv115HClFNA7W3RObuGr5EpIrbrhMLdCcro8WNgXKQzJc3IbWUuWEdGcgXmmUPGROpcRFaDvgNlS24rfgkqszQ1tmkoA_gdD-wuZJOXVJI6WlDMpHgESe9veorZ2QT-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇩🇪
‌اسپورت‌ امارات: باشگاه الوصل بعداز جذب مهدی طارمی و ریاض محرز در آستانه عقد قراردادی دوساله با مارکو رویس ستاره 37 ساله سابق‌ بورسیا دورتموند قرارگرفته و پیشنهادی دوساله به‌ارزش 10 میلیون یور به اسطوره دورتموندی ها داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28610" target="_blank">📅 10:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28608">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph9Immez2x1_9s0ng99O5oux_Bcm1UT8gN5mSvK2_XjDfIWGPnBa6dPkNSr4ESxrRp8Kl9TlzQyVA52KrYu8DEggdY0o3MBl3rec0dgTir2D-NGuJ1GDg6dNizygtWM8MqA1u5KWreIonoWrY4xzL3jm9JIHbLOI02S20ZmWKRgBnwRbR1MBABOs0hdwB-byTliHJ_AohVMnAh_u-KBK6NFr_HUun3gBPNlBypAEv8P5rs51fPozLMmd8l0dO2rDC9hqPwFdZwG9iwuG9b6cvUZiY1WAPGoNX6J_5ELXTWxg0zQV7l2E4nASBFRbsnC3ekMP_dzD_v_FIGghsh3eNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ با اعلام باشگاه تاتنهام؛ عمر مرموش ستاره مصری منچسترسیتی با عقد قراردادی قرضی تا پایان فصل همراه با بند خرید دائمی به ارزش 50 میلیون‌یورو به‌این تیم پیوست و شاگرد دزربی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28608" target="_blank">📅 10:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28607">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcWnLrD6s3FjFSnv5iGHcUFugpdb3l0qTC3DCAh7jKHxyo-DqtOOngZRz7QDG-8grxG3uGzTPq8HJm4DXa4RkNMhubWN3rxiGxam7_xXa-J0u-cEN2Een8Gp9hayL0uuVFRFF-aoTJWcQ0rtlO6llHIeDgwTw5Y61OUYsybKtYAEuDwyL4-fmmtit0fZ1gbnjFkLEnFowIthySKNoN5UMSnq7x2plRX-BTy983uwQ58dkVszvhyjPxF6pC6ZYAJiDb-D31517LtrsQ8hsHkuT1NcwABGJ47HmNeCcobSLIQzvx46HBqzqRevkgBwxTEJkf0I03TekY4loUB-nknIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
واکنش خولیان‌آلوارز به بیانیه اتلتیکو: حتی اگه بدون‌تیم هم بمونم در تمرینات اتلتیکو شرکت نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28607" target="_blank">📅 09:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28606">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daviKGJVQ1ZouB71G4xUyvik0ZIr77mRTCbLnKm1Ud1UKKDphyeOhjbfyL2bdXYAHEsk6DKX1MtEVJSCwVW9Cvpa68EDoBW2CcWolYoATbOtkZ_78NjTfKL35ZHpeYPW1tWF8rCpltuX8DWnUV3Q9D2wB0kiMfkHmVPybBQu9oFASg5RgbmcfB0fvBW2phaSpOWyv_BklX9wgpakm0dbquSgHK9TgQLGCkBdy18iUUFJ42cIlF9EW4R9_eaj-EZVClEf8JC3o0F9PFWHXFGvLyn2kbzVBV8YSr0TZDuQYPVOR2GOL153dyBFtr9POZ3-juAZ0G0lQbNbxqZMa7NyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب گندوزی بازیکنی که قبلا مارسی بود در جریان بازی‌فنرباغچه و لیون‌حسابی رومخ هوادارای لیون رفت از زمان گرم کردن که فاک نشون میداد تا بعدازسوت‌پایان که اونجوری خوشحالی کرد و دیگه کار به دو سه پارت دعوای سفت و سخت رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28606" target="_blank">📅 09:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28604">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcmIvmMXxUNOMMFLaKKKzDejEI0ZAdxyTCxYpQPqstKbOkoGcvTE1QfiUXw1GQp8VWtt-mwWYUnTQUEz6NAuK4Yx2E_44ys31tXPMtL8Tq8Q1Ryxoc0fu1JNhx181x4xmZIbCb9AXlxyHAFExVaOnJRVnNef9oTx0OGs2_15lPFkAb9VEq-e_mybheeDT8bI0FOR19DOpoBfx9HS3_a3aJl4VMY-Wh_jr2zhnUpJcWz7gjTg-h_TRVyjoUI2lQEYZ67UccrX-WSWEpYhYEUh9RDy4y7o9zrVv1c_Kgbwv29HTWRHJZjMTsvvw702dPYgcTfXO9GN2SGcuBB3TcutzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل مرحله گروهی لیگ قهرمانان اروپا در یک نگاه؛ چه بازی‌های جذابی قراره ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28604" target="_blank">📅 09:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28603">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b440142175.mp4?token=VHptzlYWBZpGEgOZT9ZWLeS1EROAglfi3HnbeMwrdLh2Hxfp5trKaAZhj2duxjMy298g-0kthQku_gUCBUP8sAc9y4dwl-QAoh7PgdtAK_c2d6RXcQ_i_Q4INOBh3Oi5rDvB9Ut6-ttrKuaho4ZiJ6VYzEeB-J-Euv4icinhoqZ1ejwOqSEO2QaVhoqwdMtTHPkNkjGWUg6TrRp2F8uxuJuXYLkSE81-o59Nn9uvDOqCDZdRiGV-lcYCyY-gA44DC5tJYTMzC1icfReKPh0_5cJVsfswojs1PIjQaAOv8RpdYEvN-42R7rl7M5CLy-lyE4dpEOyRuV9nJ1_92ttqrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b440142175.mp4?token=VHptzlYWBZpGEgOZT9ZWLeS1EROAglfi3HnbeMwrdLh2Hxfp5trKaAZhj2duxjMy298g-0kthQku_gUCBUP8sAc9y4dwl-QAoh7PgdtAK_c2d6RXcQ_i_Q4INOBh3Oi5rDvB9Ut6-ttrKuaho4ZiJ6VYzEeB-J-Euv4icinhoqZ1ejwOqSEO2QaVhoqwdMtTHPkNkjGWUg6TrRp2F8uxuJuXYLkSE81-o59Nn9uvDOqCDZdRiGV-lcYCyY-gA44DC5tJYTMzC1icfReKPh0_5cJVsfswojs1PIjQaAOv8RpdYEvN-42R7rl7M5CLy-lyE4dpEOyRuV9nJ1_92ttqrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی جالب دیدارهای هفته‌چهارم رقابت‌های لیگ برتر؛ سیوش‌کنیدببینیم چندتاش درست در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28603" target="_blank">📅 09:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28602">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🗓
🔴
🔴
#تقویم
؛
15 سال پیش درچنین روزی؛
شاگردان سر الکس فرگوسن در اولترافورد با نتیجه‌ تحقیر آمیز 8 بر 2 تیم آرسنال رو شکست‌ دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28602" target="_blank">📅 08:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28601">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcFvrG6sLo68vVvDtALf8KOm2415-56s6dHlWtUbev9e0-Qo2JgWZcCc_71_VLeb7JvoN9MdqI72ZDZUd1a0CbxOG9tWXObTdNORA8LY_eOtxeYh9s_JMyKSD9bKikCroI7OkYNo6nOKXuXHj9P-zLkzRwf5AORBA5ohHxOkfLYPzREVu4ksj4a_M7iSqNUA27DglzV6H04tf0wQmYhwSp8XrvrBzM3hPsYaVUqETPWNxLG5PnWnIe24oWM6J7YOGIaMy1VEeJS1MD9zLBBKebyNQBrlUtXej4TeAzSB9TFtWynFI29p7jctr62evDckI2NYf-n3PK7xaCbNouAypA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌‌امروز؛
جدال شاگردان سهراب با فولادی‌ها در هفته چهارم و دیدار افتتاحیه فصل جدید بوندسلیگا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28601" target="_blank">📅 01:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28600">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTmpjRe3OuqIGmdI112dxS0IR1GZuuRbylLlwra8L-PeVFeRkTuqCIYtYtV4ERrSn9mF6H-UA2nC4xDpAqF2HhNZZbIbgeUeAhIHacN0y1A27nm0tfI5z1MQdECtYp2AUz4lu5WvdI6Zd24RzWKkCV4EVL8kzChlLK52y0XVaQ7iPjsL4gt7GNjSqWtrfrNNznMWn9BbSKK3WqJU8VYMT8OBHNBDXk8mK_U2Nm6NOf_gwXMx9106jHgZnE31prZz6olOnoPikiHnm3Vsq_kX3NhfLGjY9enjitHoWmFbmLlC8ewxfWyKHQHvq8_0k6UNTFyqtYmfhFSX5uDfYJ-_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
برد آبی‌اناری‌ها در اولین تجربه حضور رودری و صعود چلسی با گلزنی ولبک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28600" target="_blank">📅 01:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28599">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdggwxsbjscN1rDt2Iy6ZMP_mWE6mJuFX9sCS3Pyu1S23SYs_uZCO5aYBldAwGl_NRdJWClM5VZmCq2NB0R4gvQ45NpmQ2e3XipkNv74ubOskVae2rkrgA2qvFwfqZK1CdWyfFUEI1b_VL27-1WvknYKHAoXx0Q2DKjXcJutw7dYGDyt7IxLdmETwfR9d3yqkN3FuMe1Jhv_VasFdGa0Vrw3oeZEa5GojyGhyDAsCQ9UDInH0Y2W71YfmPLhwGnY52CUlNqokFGKf7Rn2igoT2iSswL5Vvrlx8EZGnufsgqNKCSosuksAmi18SCUgc7nkuH11jJVkk2npAXfLx-ieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا|شماتیک‌ترکیب‌بارسلونابرای دیدار حساس امشب مقابل اتلتیک بیلبائو؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28599" target="_blank">📅 00:42 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
