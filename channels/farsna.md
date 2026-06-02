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
<img src="https://cdn4.telesco.pe/file/sl5UpMLm81y6kv7AHq9QHlox1CpkEfJF524PG54iSc0KvhQ5gDcRx6I7fGHureZQxprnrsRXv3I_mhIfwwdP5HlxS1dWaWeALB8DQ6i4FPvwKpN0hX0w8IkuLhIvm4uK-oqZYsDow_8uuInZmsjb_0lK6Tf8Ka34BVeK9XtH74hS2SC5f2IGbEJ8DWEF5alqKw7F_1WzOKEStowPm26w1uZ-FkflL9NNVBzBaKFBT04j5FNkmFHL0PZnbiNwqio3ZDDLvlTOFuqhVvxvGYiBORDJku4yWwyuMmFFX2aheM4c2OVvfBMJZm-t3O_gNxrx_j7sKOQ8RN46FE11q0Wq0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 03:37:39</div>
<hr>

<div class="tg-post" id="msg-439360">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx9_IOFf1URuxRQEGZvackqba8bUSnNDuk1k4tleDJGIA89nMO6TLEDna481wlODBdyjLctRhd7MCeFt6HJifo-CDX2K2PziIb1XFNy2vk97Pr-5aHPLI_seNyYNui1mmZ7IVdttjZqI_3NwvivmHa8rxLoawojahkSPh1jqMn8ka5b4GW15L3SoX04unGo12BKGUJw_1YlbbhiVD2T9cbrWKVyNHSqAl3pmZse7MsIlmaQaVfer3Tz18bqTyy_zHt8xPjmu27XjQ7Rtb8i_DItiCk5GkfsPqWSwn1UAXlIDyzF5-ph9Lt_kDDRM6aAK79eTD9uRUMjobycI3tLeQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین: اسرائیل باید فوراً از خاک لبنان خارج شود
🎥
نمایندۀ چین در جلسۀ شورای امنیت: حاکمیت، امنیت و تمامیت‌ارضی لبنان باید محترم شمرده شود و رژیم‌صهیونیستی فوراً عملیات نظامی را متوقف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/farsna/439360" target="_blank">📅 03:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439359">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJvxHm9iYJAnmYbCC0P31JetfaljH8vrbW08wcb3eWrFd_elbkRZ4f3Omw9vgADyfqJ--G20kxgsZvLGo4Mf4P_7D3OVODhVmWbr16OC9Tgh8nRq0SGIP0IXYP01fSOryuvndrLYLF2xkaGZrpW4hx1yhQT6Hkj1hTD6SasHskmJM962I7s3cwLWzcj4Gw3iSImkn0Vlii2s-fZX7Ue5Evg5lU6rgDCZe5IoYBz8BgANblJGxj4ffDNO3yl50CT_STYJx_1YdTJ19A9kJsInLjMqU03Grp344xwkmmRybJFCA2Dfw8UBkUdiWwqt8gi1ScZCIoiOWoPwoTDkjQm-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشارکت استارلینک در کشتار مردم ایران
🔹
رویترز به‌تازگی افشا کرد که ارتش آمریکا برای هدایت پهپادهای انتحاری لوکاس به شبکۀ استارلینک متکی بوده است. این درحالیست که آمریکا و رسانه‌های مختلف، مدت‌هاست بر روی ارائۀ استارلینک به مردم به‌عنوان ابزاری برای ارائه دسترسی به اینترنت آزاد تبلیغات کرده‌اند.
🔹
وابستگی عملیات‌های ارتش آمریکا به این شبکه به‌اندازه‌ای بوده که وزارت جنگ ایالات متحده حتی افزایش چشمگیر هزینه‌های این سرویس نظامی را هم پذیرفته است.
🔹
در میانۀ همین تحولات، وزارت جنگ آمریکا نیز قراردادهای چند میلیارد دلاری جدیدی با اسپیس‌ایکس امضا کرد تا این شرکت در توسعۀ شبکه ارتباطی ماهواره‌ای جنگی نسل بعدی آمریکا مشارکت کند؛ شبکه‌ای که قرار است سامانه‌های تسلیحاتی، سنسورها و زیرساخت‌های جنگی را به‌صورت لحظه‌ای به هم متصل کند.
🔸
در جنگ ۱۲ روزه بین ۱۰,۰۰۰ تا ۲۰,۰۰۰ ترمینال استارلینک به‌صورت مخفیانه در داخل ایران فعال بودند. این ترمینال‌ها از طریق قاچاق وارد شده بودند.
🔸
این پرتوها توسط عوامل اسرائیلی برای هماهنگی عملیات پهپادی و حملات هوایی استفاده شدند.
🔗
جزئیات بیشتر این همکاری را از
اینجا
ببینید.
@FarsnaTech</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/farsna/439359" target="_blank">📅 02:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439358">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1dmzCAG66pirtjg6yhYITWPHcAf6sTJLKTX6IYt0odPcUP1D7o5HqzJzoEUWCZKoePTKd099tr2qBooF6efQaJuepBG5U3TfHS5dXv7srQd_BOU9VgDZCW-uet9dS2JdqSL08sMWPn3l09WBvw1wDCTtYVgTy70eNTcmfoAWYXVjx3-qHJneESxhl-dfrG0olll7l-33oQZyGXIShmlEAHdZ17AoYwTF3WQPPB50yqUPs3Hp7STDrH2niNkjHkyW4tAoCsBm1RY7mxc4NS6RhkUIeBpzhoW-K6fvCofFWxLT4vOhKazz3xoeAA4CbbJX7lebgYDd3rncvpooOPY5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه: وقایع لبنان شبیه سناریوی غزه است
🔹
نمایندۀ روسیه در شورای امنیت: توافق آتش‌بس حاصل‌شده بین اسرائیل و لبنان که با میانجی‌گری آمریکا حاصل شد، متأسفانه به پوششی برای گسترش تجاوز علیه لبنان تبدیل شده است.
🔹
آنچه در لبنان اتفاق می‌افتد، بسیار شبیه به سناریوی غزه است که مبتنی بر اشغال گسترده و آوارگی اجباری جمعیت است.
🔹
وضعیت وخیم لبنان نتیجۀ مستقیم تجاوز ناموجه آمریکا و رژیم‌صهیونیستی علیه ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/farsna/439358" target="_blank">📅 02:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439357">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5aab5a2c3.mp4?token=alX86yWfa0Eh_iymUnRsb_1TyunqDAa6rab6GZtFH_fEb7IicZ8uhCjPN7ZUrNeFzm9vvSjJm7WhZxs1wCVq9QzynRhYsQ6y-SwClC4-BT2oNwSyagtOvrHmnHG_mASoH6OVb7ktpX4IzqdzAbuKA1cs3wWsQiB_dOThvDxedHkUVbDayL1IvoW_njVBBIgfuYT_ZE9r-15NeGOWmICgPGGd_KuSD66WEHszDFwYAFEyARIlJr6czk3ulQk_ZvcJZBd7j8Vo9kPAudDt91e7EnpaXziV8PA1X3k4B0GAH6liFwDgjpO-BpjojSwsDT7dry2-f5u8C9LBkYDnXqCDhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5aab5a2c3.mp4?token=alX86yWfa0Eh_iymUnRsb_1TyunqDAa6rab6GZtFH_fEb7IicZ8uhCjPN7ZUrNeFzm9vvSjJm7WhZxs1wCVq9QzynRhYsQ6y-SwClC4-BT2oNwSyagtOvrHmnHG_mASoH6OVb7ktpX4IzqdzAbuKA1cs3wWsQiB_dOThvDxedHkUVbDayL1IvoW_njVBBIgfuYT_ZE9r-15NeGOWmICgPGGd_KuSD66WEHszDFwYAFEyARIlJr6czk3ulQk_ZvcJZBd7j8Vo9kPAudDt91e7EnpaXziV8PA1X3k4B0GAH6liFwDgjpO-BpjojSwsDT7dry2-f5u8C9LBkYDnXqCDhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ‌جهانی دوم همچنان قربانی می‌گیرد؛ این‌بار در اندونزی
🔹
با گذشت حدود ۸۰ سال از پایان جنگ‌جهانی دوم، در پی انفجار بمب برجای مانده از این جنگ در شرق اندونزی، پنج نفر کشته و سه اندونزیایی مفقود شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/439357" target="_blank">📅 02:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439349">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPutlb8iNd_FCrzwNoMvRyCakk-ME9qxEHd7--oqyrr96VA4XEsQZE8DweL7EbeUIb19-y6xmeHCb4RSgwZjY89dvNVhQirD_f9Nofll4pAo4O3zfa0j1kI4e19HMjT1FqzK_WBvXB_xs8EUEdohN1ntGqM0UBLy1bAvfZ4wDkdEiGJeEJO9TOqvQMVUBnrvM54AKvcASdpyjLDnakkPf2mLti2CLrRQUGnMFK6lK7UaE3wtj8Jb1uvRr56YJ0is0e0sIg1qA3cY1G8n3UUu2bH3yBqip7QVTAQrOplFJR9tiufEelZv3UN6YQGETs8hZOH8KNIneNBtTngTytyjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه: ادامۀ حملات اسرائیل به لبنان توجیهی ندارد
🔹
نمایندۀ فرانسه در شورای امنیت: هیچ‌چیز نمی‌تواند ادامۀ عملیات نظامی اسرائیل در لبنان را توجیه کند. تهاجم فزایندۀ اسرائیل به خاک لبنان یک اشتباه راهبردی بزرگ است.
🔹
فرانسه کاملاً از مذاکرات مستقیم بین لبنان و اسرائیل، تحت نظارت آمریکا حمایت می‌کند؛ امیدواریم که مذاکرات منجر به خروج اسرائیل از خاک لبنان و تضمین احترام به تمامیت ارضی لبنان شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/439349" target="_blank">📅 01:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiKJJaP_5IJfYHhiFqMKkbcmsTrznj4SkF-Nm-QGbI4aU4mMDnbzTOsFlGCGygD1neTvsOLKQKG4Ls1LD7dwrTNoTGzLr2pfBlu9wsQlRgtpd79eOCwAtYvK51TGeeHnEeZ_a7nev4fCHi8kyzYCZ6_2x8g6LD8sWY8frOOzevrwQ8lOHG2pTb3YB-cabsxzhnejJnlRpDauqyuV5tm5XJfG77Yzrzz9Qp1UdRuRkVlUmH650MCmFBa1FO5QK8L7wg3CS9B6i3xyq1rdov0WcNQPEJCI7Xf-e904TjsEtd4-BlwzmcSlYWKy3ZY1cJ8Z__6WuH8ihr1liffx2PR-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بعد از عقب‌نشینی از حمایتش از حملات اسرائیل به لبنان مدعی شد که مذاکرات با ایران با سرعت بالایی ادامه دارد.  @Farsna</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/439348" target="_blank">📅 01:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439342">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCdvia-t6ytyIfnCyuf7lJOuF1S-qPNatUYduKvvULJ9VysXAFQ2AgauoRCjAveSgSf0mSZcqCyIm3d8psEqVgLMKJgjf9aKDFSTkoPwscdPAY26uJ9eHt56hKuMP8HfDaTvCy1sxuWjMZN3eqwXP1Pi-1WgRvRb5BE53nC150tch-xc4xtGM5ow9ppl5HQiqRBUfOhcA5-IT96uyEFUvCpQo1-wH7dlSc9eOPUwhCDBkH-r8fha820tin9dj85yuXr2Q4D8AlKo8y69J1EN06e-pldt-nKvH9ILBBST-MHZVfsmOv4FzArsf95DFxoxyycLz-HH70mWsHj5UZ85jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cfwNDHdoY3OY-HgYE1sK5sLm9liq2K7wEOVrOn3XSkIrnjW68ansGI-6dJtp40R_YxqjvAwFYaluUd04GjzUVg2yeQdDKCf8fdxywVhDAdln0GeG35s3hk3YVvHanWID9FMvLGFSKGcvL4IzYbHdab2k8qk3DOZsgJk9W572xHEaQ3LHdHjTelet5MCk35btEJGgV1-zxDLqZkb2xh6uZVzEndGQPHX8AsFFzzZP5SnBDGn-KDVG_BwDK2qjkDqNyAY3h-RtERGIVHpfYftuWmwCvgb9xPppUBhhVx0oLUrxPmxThxnOKQRNtkUjvQ137fpXIm3gCV7g54U9LuFwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXseDT6GyIkD3JNs6AT3ayuZS0ifE7C6kPT4AetILZN2C-Gqat7sAmkYRPNjRYt76JPK2CSNbDok5c3ZROhv32LpA0QOrQfUVJx9Hfaaybm25i1JgTnYVBTtBf6whfPqN0JIjBNzi9jIM5obidzubVfyxe-8qyhRHyOM4gHJfpQy-EYqg8K5PNd8dlvnCAgrwrVoK9HWTpz08FUeWFDkblxph4M8CvZ3dio1wTSjJEbMztNnsRUjyjoV36aIP54RqrRKvHQyLqWWZHrtNTPl3vwHk1TYUcG2xcAfPv618l_3isoJnAoe30DdHZlfnauYjI56JzYPGZAMBRNRRXZlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pO-c7CMpcnTVjbPWtaEqXTLCCGw8Ex_yZOVOEBH5qlcRTxlIv8amF3_onvlAFc_Qku9uZLr2zeDFOP_0F7yqaiJcKDSRpBNNZPhoSRrQrgcUE5_3XYMhI_ksHEwQ3wz5oJDa-At3mfG02CyRgOcv6wtNgh682B0ATcPBYPM7Kbbj2czp1jeg84NYO5DkgXOc7Qshhhg2eZdMXpen5y32csS5IAvXFXf9HDuGmV6B72p8nBCMtMTswnZYEFXB1cefUsQ-_Mt1euU79BX0nE7Pg22FJiXuBWGMKrkGjADUIP8Ee66ud0WRnXPy3leBsw-cuKdGkW95FrYxlnqx4VCvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7SbN29wu99RtfdStXVwcvhD2MhpR7CFMhKgen9VamtsXwYUd91pueQpbNxRy9ch_Vk9Eqbj0uryZp0cdv9xKanRAALlPaMkyMDCbbekXlbW60oxPaWkvvuAN8rLmWGVnpV7WDZPjIuIQecNLb0V3sRndQs7z32y22k3VjHmOpupw72BMFFpY7cxfOUvr4KYEYf0BwW53E_YM5V42zwFSowebnLrdOV5iQjDCTtDASFCA4bT200dPaGrUiLJ2cK3JwVXm8pNNhjK_mvtYTHcB7D-u0O0-S6zz9jtaDJBPPPmjRkrev0Mkr4hO4i7JND0m1ozyhp7miB-2xC4J52MxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdXi-s24y0ll3RdNvzOjX2HzQ-RJORH_r7G9mHJBQIJOYyJzQxX02UNiA9a3tyFDkZXYIDDxirXMRmTsdERIEmZY7Ypl69pXikhygimfWO32LsxaOo8JoL8xJjJaa8sLAcKwrafYoy9jclK8Fcnk4MqmoZd2BxIqdGY2sq7MZyEmpFhVnytOl-B27MAPtN0IBZcpZOFG-MFNu--mfPPCtV9I8xguB-7bxwO6OfAnKhxX-a93GhELLZUSYE1vyW-th_7YPTF8Qe33NrqgDRfJF8Z0dE0mvFoBUD6zm0wIyUSWqgd-l-HfW8rG-PrDmy-TK8pV8duA8fGLj-QMMAV5oA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۱۲ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/439342" target="_blank">📅 01:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439332">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcPxzCDASEgdng_5qIz1kHIp1WqDPSk3_Z4hrLvsZZXIRN0HCEc8P0G5BzZZqO_ypUM07va9AsIbkfGU8BnprXkXCvW4nuBvioHXcaFKY05Ao11XiGqwsRZWXKHrHMtLufArMQgE3fc9kdbE2ETAwL1knuIp1C9HwF6Xarrzfzd-lQrtfiYgNMHqZdHlAkzR7MawXBMojZ-v2edfcDvDuYrik4gF4XOot4FF7UE9jQIMiQmlU50LCNTUg8LfPnVhS6TfzQACmEEBSgEKrvuEj1YSe2o0XmkDXFzDrWlCmixVqo_dY5vTOKGJTBdkWf5hGfGC26PNyJ-B3WrD4KdcmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U65K-28rVUtu4nZtPVruyoy_YuRNYlBkKxJSbxReSXPDD97DHTrDy3wCeyifD9TgeEiIxRxs1YbF4vs-VTFSe86jxUF1JCcugxGpNLauTPKvchbBV-Zwtd5RbpAun9w4kIqfRKc_K4_qHuyw5euJQs1O_QDUMyER3uHXZJ-81KsVUTj0igMSbC0ruXYYWXVxE0iGcR4a4sagWKZsGrV0ZeJ7znlKs9qLkSxRCshggCr4REpVPbguWU-RQEvwQK60DY-Ys6ksoNT7pwGqRD-MRG3yFsRIBiaUNqmcKVN1NRui-SAw_p0-rSUUsUUDHnmH56ehbod6kSXSRxQGmx0KKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbaAvbvfwrovzcDK1nmfjPhwMVNvbLGt3ATPlO_YkAcEXx09ValqAx-5NTMKyzqtkmLZcv-wzlROrzTSTzdqa0xW3x8Mprm9yhCgtapTE3LPrT8wIxX5RedPALdr_s6s9lU5-4wnqUwx885kUXVm-0Ye9RIfJWDWnTdo94JpVyfrPSb70XQEfSCsOlj2A4DMMirZgFdZM_4iuZmIFYCGGedbC8jihuvU7Hw5bfGN4Widn_iLpW3ZiRKy5gkWeGH7oYigUAQH3_AnePCsEOp6nthQAGDL74T4UopTuneYzX_0JassQnEDDfXL24GQzM5aM7YUbfd8evdAh-2dB3LFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EsN8FvucAyY1GYU90fbYCzrUEtG9btRKRoeEFSznyM5l4mgDavGAKCXw8zQM6FHpB-x_0RgavePaLe8LPwxmM2SjwiZmARVl-tvwGKTTodSr9zsQeyaa5XrGMx75GQvyYCiDpPnFX8mhIsOmS3AZgPb_kCM9_magC1dXHQ4PpBQL6YvDl2rzVVevEvBgRzB67hBosTf4P0nGKaeWp_9aSh4Qp6QXAEOG5_ixNOxfwW7y-rudY4EiDQY9DiKdZBzFM-XUQYyRSbXKAM2Gh92MVbpe0Izr57C4Gu3Eeh0ZdOyowzsPCkOk7J1BgR6DgFIqiUJZAdxdvtDDR9Sj-wIK3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4gqJr9YwYEAtYerDETu9aqgC1fnJWA65GFY4GCIYxEvbXE299rQWvbNw31zVqcWQ8mrru5iRWvaGDBZteVgZnv42FtlhDw--24muQ5IVSuycFcwLqOtNkyO_3Ul6z0GIMAtN8B7BC8YH-kcY16zpJrU6vObCCkayZS3-6fjI2hSjUHldewY6ynMh2XgYx2m2EIJUSLvXbxOmBE1VJ7G-WH3p3FwkGjoGJ4ZAoglQ5rTIRwv1L0Ywdl6_tpPqk7Khs02CXSWUqxwjfgx9jhcOvaEg-ZemlJMmaEYy5QGJveUP5ZIzQBKUNPfcm-5mIxJTOxbKZaQC4hGk5ql7AhMsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rC_cFlFCZoWVOh65bKv3jnOgJtxHLKsxR3aLgQPk5JD-dKlnjwBWwWRWMxffUDmSUpkHvhNi4ydZV_wl6unefDtt-xG9-uFXYX9azd1wrX3Ne05ogkA6aPZarg4Hb1m3NOcmiylJ2JHjapJovY0Wt8DrxmYIdu9_O2EAWGOYriTS4kCJWuLr2eMz6pVK2x_UKsNkzV2NVwDcVwt_AZ3yTCqprgu0_F3wkh4YVtyn9Mj2dZFYTxany3fqP0CgmYM1S4o3yzL11D5jN0w6ddJr3LsZZlLJRtFK5KehXXuTyOnfoQoddP6aCLPK6vfV39dShTp3_wahiXeGnX_L-gIw4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VyyqL581Aty_JgRsbp8kkyM-sU6PY3WaobhkpUdE0N-tcynpXev09uDHTRCFz0tQmANWymqGCrU36Zc93BgiXuAJaMI3HjoFk4e0u5DvNNAVBsCX_xV5CCe_Ci3EbsyX4jrLuW6UOQ_ylvY0GESKDQclztag8hVEj9fW-i0hGkGLUGoWe4mrU-Cft01HwFgBjr4j8Rx5Q3S6k3Wh9S1DCE_pAlLVA4jXLHOu3aPcdZ8Skxl1tPUZR50QGdEAICAfwb0ifTZhNGaD9V9gtrc_8bX9iWMR9XLdnU_5nfsvnwRImDmNDtgD0DIT2fRFeFxLeu7PJ1VF4kQV4VQaxgzg_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdOVUma9tDukgV-F_ImBR8EtyBob5IhNCSZSNM2sWJPtbGE-47BaWNzKsxD9SHaxejVoJzFCHARKlgmNh9fc4THRwp0GIuXvwKvNci4qkApXU7QFkwaA1m_yqSNLHV33RQtMg4diJiKMAuGsOOb3ZgJMLJDIRHUvWmHv4jCuwG2yZQ_V2Dqu79xR8xBTNVVqglvR_4qm8f7FgjxZp5fTY52gJXELBq_wDW52viXJuTAuSH-x6moJFpxLDvutQDKg4_KY5Xx3Fi8ynAuqAi7RtnqPXINzH0GMOtsTuUOjwa35johOIphRGvCuNxD4bzwEKvh7eFu7kkynvtVUwHv-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWKSYy178qQevGYpN-nJ4Gakrjv6DJIxVNrfoQnEpxDXXiUTgHMJCLt9ttjxLRIhfsIST-9HzKubugoEnemspmOwJcuaC4i-7c-XiYbYAnvPkH6Loi27S1ucPmX9oO6yV_HUsT-etoTP9SKnT52Bp-obWbkKPBTInruy5aq7-2AgedVAuTcrc1n7l6oeb8OdDBHrHp82zleRda7FwDX0bRhMwAHjyn5iH7INfjq2cLH26zXEU4iKsgeV-BaD9Nh7Ci62Vpw0lObqii-K2znqbxq1r9vx1UZeFztt4o1FrQ5M33-gyNCymWC_IvIs6KZU6EoqZYvoiZc3zxtaDmIz9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IQh5-H4CcumHOSvHG-3PGvLRJkgZA3lB4De0tJCKkfjr3CBmDnrDjA8f6jeSNdlHNqlROOOGnygWl4eviuukwWc13sbKXq7CjIicgO8oXgC9fktIJa0Z5hV465Dohciu3PkVykCAcpDGmTqfsAbu9fqQJ9X7Ya1j0fUbyG95xmn4S5_LXXjhngVdHeVOBNJ5EjPlnPFlMkJtOy5jCWi_4Nqpo7RMaYysXorwv2YV96kY708bZCOyovx4ZLS9j8YFT68xTj5_HiJ-N5Uyo56JIDHeet1Tcz7wXyBOwv0XixwDx6KMyXdRopgShYOpBmuCQfvIfwlPMRVOP4oMVcuaIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/439332" target="_blank">📅 01:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439331">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqySJgzKs5voSITEacTGTc15JjijWggnAf88oUgw_z4rolYHut9V19KAo7lJEOtSyHHWYGONLdEtYgeNXiVFCBTCUjfuuOh37LE6RHlq_sStngYPsYYpr7rAGjNNxHB4eeKS6RJyk4zrQXA4u3wwCvtuwkeXXkbekWTzkqvRIl47k0stGBR_UG8eqX5zU-a-HXzDuV406GMQwQ3IEASrvLZScJ4tJ0HXCb0bgOTmCReLJPGsy5_7PwQ7E7b_otImicdNoC0XkHt94IqAyOaTVA2nbiGSmD5ryxp6ucFd5am0_ei0n8LcL_cyObAc5FJXNZcT8CwMXGy2T3DNC_aeKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف در گفت‌وگو با رئیس مجلس لبنان: با ادامۀ جنایت، ضمن توقف گفتگو، جلوی صهیونیست‌ها می‌ایستیم
🔹
حزب‌الله و امل امروز هم از سرزمین مادری‌شان و هم از امت اسلامی دفاع می‌کنند. از این جهت پیوند ایران و لبنان ناگسستنی است و جان ما و شما یکی است.
🔹
در ۲ روز…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/439331" target="_blank">📅 00:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439327">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SK5G2JIpMCGkwHT5Rgnm_KKm_JLR5LykwrsbmhrVc_HM6-u-yzCND77xh1Mxi2UQ8bVqu7nLur9iltdC99tvAPT4Ph2LLrFYACgYWwbqkuRPaoo6OAsvlqCzoM_8uZHy2EizL4Gr7W8hoA9VZbXrCuh6mems49rAVcMHy0hFJnF8idhgIJkygzn_cOXuHLCbplxctFmHTRI3zxV-fIuEhnoLbfUdBbbw_T1tjKOdI-ZSwfrBT7WbOwBYnc_fRsvtmwBtkB7QXDg0_WIkCaZ9YYJwfa8qILDyDI-DQg6yubDspST0R6WDwlahJYLhMsoaMxcyAlTzCetR4W0sj0a4wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5hz6ussUAzMptZRBa57RbJAed-MvRG6lwADdcW_6b1RXgT7V22RlgmljlgBYhYgW_-_Xwtrq8t3xHE8Nw71D-kGS1Do4CKlYr_wLEN1kQCKyNSAtpUK30KfIVsCetq3DECLZkcjApCXoNuT3XSq0Nc7zy0kK5yXSYRaR5gmJ6U3QgnSBDf86HtqL_UTP6qpZVJf5g5FQMXyqGr-XQTvcTk5nbrl6mrETQs3nFLfEQNmQY1S7HgVhsIjFfigWCYogvIyWR5aBtGdrIGMXdokkSqMuM835JFv_n3crwSMOKFEEZWivB9cWOAxtktF8sRbWMOz1n44xXIm23XRU2Sz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aAEQ7w37krS0HZ22OHc3GTx29n85j-GJv8bqEToxHZ6V0YPMzoJ_xEDWXbHyRn6Il0wVKVUwj2i0VvZgVioFLbvzLN7XJA5KYaT5xpLnFjqpzuz0koa8TZUV45GANG8RPDDrrYvk6s2kWbXpG74pKLGY2sx5SzND_gBrNWk1ZEpMSVd8QkdAT5jdt1hvhOUQu5G-dmCUx4etjCKB1JkL8tuNCj--FvvYK2oTWZvwtBcN7iAyAtbNcE0g469Oi4u_-d1HM1o9NaAjyhXa37lzWpF4OXZbWlueuBiNzkrf18PGj2m4S-nlMGwhdadjvzujvLHxCoXcN1rsOd30xEEw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZ8QoKc067Nn3QWV5RlXOYDch1zZR8SFupgqwK6YeSh5DjXdv_UaPSpyRBCZiJ8-ytzj_pqpPmPybK3rlT4GgzMGw8Fo7T-wrNUKmt7iwsb84xe7yMKjzu6zV4eKZJIBV3wrnCbn0rlTWalG8F92688FljWP0m1Z2Y9IWkwNXi7SMV08eHhxTY2trWqPUVUvFlSnZ97IQ6fTcE7gBBJ_BLiPpEu4MgaRKNlUU-DNjYUAKhSjGJJPItzygsOI3hgV_kbbUHb2jCZPxoIz41aNTIg1yhLS5K1B20ZKhm02huHcXnOuqwXbTuq5mCXfZ53FHb8gHgwYh-qsA1YfCBPP7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
گزارشی از نخستین‌ماه فعالیت نهاد مدیریت آب‌راه خلیج فارس
@Farsna</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/439327" target="_blank">📅 00:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439323">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be983ed74b.mp4?token=sQ1fa1ScV77Ps8YdLNaq4yKXF2RQK1np4gUCApuP1UgXSaheKNkUxHoRzqx4AjpI1Tz3YoxqSDOYgFhW_Nc7FNzE-gR6n3gqEfVOgHzr_Bs1MMDeuJegbWd1gOLr0QkAVtPmGmJHnDWP80oHQf1t0QgB9x7XM7Fe7NhZTw1MEVY4H6QaodrXd3Sk_6xdhlnHn6Jn3OwzuB8v_O__mnE0TUwmFswz5RclQN59qn06zTWFQH_KPM2Uh3YTjF6efYC12Xy2d8kA39z9TUPi5LPIT8dSSHQW4gszK3ewSkz9fAIeS6EapzGGPDZlP05xaJ_AIs0nJVg0ZrRv0zRzG_4uLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be983ed74b.mp4?token=sQ1fa1ScV77Ps8YdLNaq4yKXF2RQK1np4gUCApuP1UgXSaheKNkUxHoRzqx4AjpI1Tz3YoxqSDOYgFhW_Nc7FNzE-gR6n3gqEfVOgHzr_Bs1MMDeuJegbWd1gOLr0QkAVtPmGmJHnDWP80oHQf1t0QgB9x7XM7Fe7NhZTw1MEVY4H6QaodrXd3Sk_6xdhlnHn6Jn3OwzuB8v_O__mnE0TUwmFswz5RclQN59qn06zTWFQH_KPM2Uh3YTjF6efYC12Xy2d8kA39z9TUPi5LPIT8dSSHQW4gszK3ewSkz9fAIeS6EapzGGPDZlP05xaJ_AIs0nJVg0ZrRv0zRzG_4uLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اقدام ویژۀ فیفا برای کاروان ایران در مکزیک
🔹
درحالی‌که کاروان ایران برای انتقال به شهر تیخوانا برای برگزاری کمپ خود در جام جهانی آماده می‌شود، نشریۀ اکیپ فرانسه از امنیتی‌شدن فضای شهر مرزی مکزیک به‌خاطر میزبانی از این تیم خبر داد.
🔹
طبق گزارش اکیپ، ٣٠٠ نیروی…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/439323" target="_blank">📅 00:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439322">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">قالیباف در گفت‌وگو با رئیس مجلس لبنان: با ادامۀ جنایت، ضمن توقف گفتگو، جلوی صهیونیست‌ها می‌ایستیم
🔹
حزب‌الله و امل امروز هم از سرزمین مادری‌شان و هم از امت اسلامی دفاع می‌کنند. از این جهت پیوند ایران و لبنان ناگسستنی است و جان ما و شما یکی است.
🔹
در ۲ روز گذشته با جدیت توقف حملات اسرائیل را دنبال کرده‌ایم و اگر جنایت‌ها ادامه پیدا کند نه‌تنها روند گفت‌وگوها را متوقف می‌کنیم بلکه جلوی رژیم‌صهیونیستی خواهیم ایستاد.
🔹
ما مصمم هستیم که آتش‌بس در همه‌جای لبنان و به‌ویژه در جنوب این کشور برقرار شود.
🔹
چنانچه توافقی برای پایان جنگ بین ایران و آمریکا شکل بگیرد شامل توقف حملات در همه جبهه‌ها به‌ویژه لبنان خواهد بود.
🔸
رئیس مجلس لبنان ضمن تقدیر از تلاش‌های جمهوری اسلامی ایران برای توقف جنایت‌های رژیم صهیونیستی گفت:
لبنان هرگز مواضع مثبت ایران در این مرحلۀ حساس را فراموش نمی‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/439322" target="_blank">📅 00:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439321">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVKPJ8I_X0xGuL61p5KZJ8YuOC5RZW40Py_nAFqKgLEbUivd-3Y0bEMxA6hzPxM5XK8yv12Z2APAVl4D4XXrvAnMYT40hdTyKK-ZSt7ipjH4u_qniPeVs0bERj_v68LZKk5n6T2Ai3ThnxUXyzzeylpgso8ROUwofNlb1UHaMwqPNetsxs-wYD1XJhiNpylB8C3nfexiS8voXUveenNuhnPBSs6QYbxZCATO-_wUcfNzMSfV-y5hVUuaWDOMbQUQHkGxxrI-HdMgeac9z2xtT3gmCNecxDkk0vq7gX0b-KG6bwkWJhtLOTbz7AdCF86KUv4E08rSVi0YV0A6NBbInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله پیشنهاد آتش‌بس جزئی را رد کرد
🔹
نمایندۀ حزب‌الله در پارلمان لبنان: آمریکایی‌ها پیشنهاد دادند که حزب‌الله تمامی عملیات خود را متوقف کند تا اسرائیل هم به ضاحیۀ‌جنوبی و بیروت حمله نکند، این پذیرفتنی نبود.
🔹
مقاومت پیشنهاد آتش‌بس جزئی یعنی خودداری اسرائیل از حمله به بیروت در مقابل توقف حملات به شمال اراضی‌اشغالی را رد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/439321" target="_blank">📅 00:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439319">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4E1gwSkCntUWBHq32gnOIsaP48mKwg0qcdTrMc1JZdL-OdxBSFT2_T0wE32fNknBOVDE8XHIoYjWZ32uxPXfs6BHwnebCtgDQznaVh6-q-cIAbkXVNWHA4a3NlWXWAJDlhbmipVn8Lh2_FRQ9hscTtmoL3uOOrXjdHRTX4_OATomoXyF6mlnfng9eaV1cxL853yXLjHN_ZVwan0064cp_2xp-T0XKlZC_w-C0IVr0Yvo1CWmPlhFMm81iqOSjdL5bHZ4WrEESmxVREMsW-hA3MErsjjyshJw5AvhZKXbHjCDTu4uG4c6sKU-YjjEhma2JTLlOkVqJiQOdiQeURMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادتِ درخت
🔹
مردی پیش قاضی رفت و ادعا کرد: «من صد دینار طلا به یک شخص قرض داده‌ام و اکنون او منکر می‌شود و پولم را پس نمی‌دهد.»
🔹
قاضی از متهم پرسید: «آیا این سخن راست است؟»
🔹
متهم با خونسردی گفت: «خیر ای قاضی! من اصلاً این مرد را نمی‌شناسم و هیچ پولی هم از او نگرفته‌ام. اگر ادعایی دارد، باید شاهد بیاورد.»
🔹
قاضی رو به شاکی کرد و گفت: «شاهدی داری؟»
شاکی پاسخ داد: «خیر، ما تنها بودیم. اما در آن لحظه که پول را به او دادم، زیر درختِ بزرگی در بیابان بودیم. آن درخت شاهد ماست!»
🔹
قاضی لبخندی زد و گفت: «بسیار خب! برو پیش آن درخت و بگو قاضی تو را می‌خواند تا بیایی و شهادت بدهی.»
🔹
متهم که در دل به سادگیِ قاضی می‌خندید، آنجا نشست تا شاکی برود و برگردد.
🔹
مدتی گذشت. قاضی درحالی‌که مشغول رسیدگی به پرونده‌های دیگر بود، ناگهان رو به متهم کرد و پرسید: «فلانی، به نظرت آن مرد اکنون به آن درخت رسیده است یا هنوز در راه است؟»
🔹
متهم بی‌درنگ پاسخ داد: «خیر ای قاضی! هنوز نرسیده؛ درخت خیلی دور است!»
🔹
قاضی با خشم بر میز کوفت و گفت: «ای مرد! تو که گفتی اصلاً او را نمی‌شناسی و پولی نگرفته‌ای، از کجا می‌دانی که آن درخت کجاست و چقدر راه است؟ معلوم شد که تو در آن مکان بوده‌ای و آن درخت را دیده‌ای!»
🔹
متهم که غافلگیر شده بود و زبانش بند آمده بود، چاره‌ای جز اعتراف ندید. او اقرار کرد که پول را گرفته و بدین ترتیب، دانشِ متهم از موقعیتِ درخت، بر علیه او شهادت داد.
@Farsna
-
#حکایت</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/439319" target="_blank">📅 00:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439318">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎥
برخورد مسلمانان با حجاج ایرانی چگونه بود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/439318" target="_blank">📅 23:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439317">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9ac54a9a.mp4?token=m4ZVL0Juvprxm2CktyGvZbniIuyMxx39rznJB6Uq6jOxN9vNgYoFgHt8Ey31OMlEKHTFniZg3u_T1adXXUHIuV3QSaWXaKL3E1qh7CQgQGmFAEvyopVfsLbNNq0ZqLupX7CnOIzWUNPwIyIApHEIV-k6L0uvofFV_rL2lxd5UAMh2LM4DLsqXHxqMxkbLN51Az3u2cZ6jNYt8UXRJocAmF4cGdzE9n3rWRZu2BtXlgSprbqsEerBYZDoXq3ehBHtW6IzQVzlIHvuHA-GD7ZyTHlrgF_jL_V34EzKeH2p-YOt_ALqpKwC_qOtLHCemclGguo_9X0OFBfZAL8hEY6SkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9ac54a9a.mp4?token=m4ZVL0Juvprxm2CktyGvZbniIuyMxx39rznJB6Uq6jOxN9vNgYoFgHt8Ey31OMlEKHTFniZg3u_T1adXXUHIuV3QSaWXaKL3E1qh7CQgQGmFAEvyopVfsLbNNq0ZqLupX7CnOIzWUNPwIyIApHEIV-k6L0uvofFV_rL2lxd5UAMh2LM4DLsqXHxqMxkbLN51Az3u2cZ6jNYt8UXRJocAmF4cGdzE9n3rWRZu2BtXlgSprbqsEerBYZDoXq3ehBHtW6IzQVzlIHvuHA-GD7ZyTHlrgF_jL_V34EzKeH2p-YOt_ALqpKwC_qOtLHCemclGguo_9X0OFBfZAL8hEY6SkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یک
کشتی با مالکیت آمریکایی-صهیونی هدف قرار گرفت
🔹
نیروی دریایی سپاه: درپی حملهٔ متجاوزانه ارتش تروریستی آمریکا به کشتی ایرانی «لیان استار» در محدودهٔ دریای عمان، در یک عملیات مقابله‌به‌مثل، کشتی MSC Sariska متعلق به دشمن آمریکایی-صهیونیستی هدف موشک کروز قرار گرفت.
🔹
​هرگونه تجاوز ارتش آمریکا در منطقه با پاسخ قاطع روبه‌رو خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/439317" target="_blank">📅 23:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439316">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a212e1b27.mp4?token=VibRy12maL4AapjNSSBMwJivzlFe-UQqzKs4HTh3EL44D2_qV8LrXDPvYEnLKvUf4-jVjiw_IrRRm9JFrFqhNYE05nK62io8Wo9I0BgvxukoGEBEky_4f06N7ifKzi9sqJzSSOmSFaELXCMkwI3_-1LeEB7w6OMOgSTfAonU_7NA7wGQnapCZBEgAdS0Km7AXzCsb1Ubo6pvzDe-VCFGlDTg_s5mes7rUTlAGwpliFKEs48OfliiwAqCnwVzbcdJgCpxvGWko_TBDAYCRfUU6tzWAjvdQ9y0PO-lCBqOj2Nnn-q18DUu_zUOlbKKcHNH-9km29U-yRmNAYq0AhU3upj6G7K18MjKJSFCavEqAiLpMEU4sHqIvHkxrPPND-iNDjbx5t9H12nvxaRBSQsaqj32zK0icYiHgnI_jnbMQYQrwzuY2q8QpXd5WiC5OunHcM9P5qMqgFlvhN1HdIl8xAV4lnwdskH_LxfVvtkoJvVj_KKRDOcK4HhDrJvhcAXhtf5NBvkIj11vSC4TdhjA_khAndYN1cf2n3KCmE7yNka5uXmAkjbfPF_JU-9W4Q9HSRJx0n2srj6B9EtxuzJxQB2L0eCkwP8t6PLWOzHcqS5qf6lrsano1lo952tW7A86qhtH0z8uV29q4oQMOIOXBg8AQJRgwMDMlys29Rk9Fmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a212e1b27.mp4?token=VibRy12maL4AapjNSSBMwJivzlFe-UQqzKs4HTh3EL44D2_qV8LrXDPvYEnLKvUf4-jVjiw_IrRRm9JFrFqhNYE05nK62io8Wo9I0BgvxukoGEBEky_4f06N7ifKzi9sqJzSSOmSFaELXCMkwI3_-1LeEB7w6OMOgSTfAonU_7NA7wGQnapCZBEgAdS0Km7AXzCsb1Ubo6pvzDe-VCFGlDTg_s5mes7rUTlAGwpliFKEs48OfliiwAqCnwVzbcdJgCpxvGWko_TBDAYCRfUU6tzWAjvdQ9y0PO-lCBqOj2Nnn-q18DUu_zUOlbKKcHNH-9km29U-yRmNAYq0AhU3upj6G7K18MjKJSFCavEqAiLpMEU4sHqIvHkxrPPND-iNDjbx5t9H12nvxaRBSQsaqj32zK0icYiHgnI_jnbMQYQrwzuY2q8QpXd5WiC5OunHcM9P5qMqgFlvhN1HdIl8xAV4lnwdskH_LxfVvtkoJvVj_KKRDOcK4HhDrJvhcAXhtf5NBvkIj11vSC4TdhjA_khAndYN1cf2n3KCmE7yNka5uXmAkjbfPF_JU-9W4Q9HSRJx0n2srj6B9EtxuzJxQB2L0eCkwP8t6PLWOzHcqS5qf6lrsano1lo952tW7A86qhtH0z8uV29q4oQMOIOXBg8AQJRgwMDMlys29Rk9Fmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ر
وایتی از وقایع ۱۳ و ۱۴ خرداد ۱۳۶۸ و اعلام خبر رحلت امام خمینی(ره) در رادیو
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/439316" target="_blank">📅 23:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439315">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMMDvX9gTXHQz9fMNL_cXKLDKjFr9Q-bHtJ3ubNKYepX2rL1sLIDpDkak-LBc2QQCWMyTA47B_XxoJp1fgVALMuDWLotn2clA4hSRErsY4Y_fsUM_gHYVOeWiwMoztH4cnUHdrTAnj27j1NyjGE7mGjaAR_MvEwgTejz5_kfX20A0Zyp1uGPnwgAY6jMDLjerc9yfVtgIqmKVjlFp1Ens7cSqQyWtHBkgKq5C5HONfYm8dwMyp2p3DsBgTT-ddkRWDiseEWvz_na7OLq3VABkVrit4zys7sApK3Jdbaj3eO3BVESnOUCzylqZGTHQBBgtzVgNMHfGgxnhSs6HF6F1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مردم ایران در مورد جنگ و توافق چه نظراتی دارند؟
🔗
جزئیات نظرسنجی دانشگاه جامع انقلاب اسلامی را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/439315" target="_blank">📅 23:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439314">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99966d935e.mp4?token=fNGMhA1awVgM53nR_lbed77cSQ9lMOebvgUwglXg3aGnMyKU3LEqAi287O1IUgKEtX_7m1XSRRzeyzbBplqkN0iWWIa5KnstH46djlHsmK5uhKujeJInVmWFHYXkk9IjHn7gclsnpW5hjZw83uvnA9N1TLdYKEeIKZOeK2Yd36UQEoc_62FgvrNf5yTZB9XX77GOTyXrxNZ0MgHSdmy90gRWKg3BMq_Nq_JMQ_Dihcjupt961QbHXyvJC2-Rg2r5_uzZXO8bUIDh8c5HH5QtSFfas2zLpRpBRX0qHwR8ovp03qz47fzvubnxeKWmVJueZpA5DesBpGDvgLhhgc-8Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99966d935e.mp4?token=fNGMhA1awVgM53nR_lbed77cSQ9lMOebvgUwglXg3aGnMyKU3LEqAi287O1IUgKEtX_7m1XSRRzeyzbBplqkN0iWWIa5KnstH46djlHsmK5uhKujeJInVmWFHYXkk9IjHn7gclsnpW5hjZw83uvnA9N1TLdYKEeIKZOeK2Yd36UQEoc_62FgvrNf5yTZB9XX77GOTyXrxNZ0MgHSdmy90gRWKg3BMq_Nq_JMQ_Dihcjupt961QbHXyvJC2-Rg2r5_uzZXO8bUIDh8c5HH5QtSFfas2zLpRpBRX0qHwR8ovp03qz47fzvubnxeKWmVJueZpA5DesBpGDvgLhhgc-8Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیخ حسین انصاریان مهمونی کیلومتری غدیر امسال را متفاوت خواند
@Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/439314" target="_blank">📅 23:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439306">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/luM9NhFzHbUonnpYMOpo2i4hU9uFusz7DRJhkM85eDfbONV_j-quR5lYd4-L-IJNJtebLjhqS5uzq3ANNVrt5EtuuH6FDAf6_8Kbk3tgMdVUyS28x6UT0txW-2GzGosUgA-lpfDP00fMQE_0upAxamDbIKq5RMY2yDf5gEr5oYMwsvGfJvKuda0YlPub0u0xUDWZg1t7WFmpAKAgtJeZFC47tYIJQB2yjigf5LrNm-TlKrib-3hpF-aFZlK0bsTl8lkGmUcUroMgqLL3BCk85plY5PjvEu7RZ06t4DgDeKIE0yC3sqGfeKh-vEFQiKE4J613EFlE8GNqHMlmpGSXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swwt_xSnj_ezidXn5T-GAeR9pAYqxM_RaRZuZF2N3Nc4v64syyChE2eqjq02rXrBpdz5DWxlf3L94gsxz2tj0NUObdUiNXnQysH2dzXSuNXczEDVrCZ0ZqrACeCWcTzIymUdh357Nn_8D3rbIJxhwkPDpCq_dxHy-JjDccLMup1Rt-LgOw0qMfgHqvL5vEbvC2r6oaCSwKypFCELsrn3AkTE8K73PglLsGVdstZI881hnz1rrknM8QzD3HrdhT-YPS1D9pQUqYj3798GLvHr_Fv9WFofjMisyib33VLzf52kNlrloxfWn-ik5mGRNSKF5Isspp2kPVdpS_WWlOP4sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KHyKGT18JuknWhwjPB978_QAQJmkmlbDxTz_6nTncS23JDj_SygFopiJfVDc_30IDvl_8lTQsUYlg9XWPtONmH30-92vArqkNQncaQmgIf8z8LXTXCwTxF41On8OBShVcx_pgsOEXNNRJCUecVirqkiIccKZ-CGoGHjwl1bRHydlk-q3p3WFUo3rr6MXelQd5vpFs_Wgdn2XSz7JjTXFqp8xkvb0s7GzO9oRm17_ttuQEp-_dQccCxgWzjS00xSQDUL-BIEDNutuWt7jdwWTOtQ8FKxOpn931sMI70Pp0lftLFzZC0aXCX_mKvsVoXItLwgL7pzDhuCn-rlULZMBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ner1PV2X1XME2_TsdU_CYwWqaLCkX-nQGzqGZ_eIO345Hc4mCWk5mI3Tm_QrdnrMEMJSMmS69tYgFyaCh1alUVPfCT0c6JUcZiys47VQfYZN2ZsThjN7qF8Lfk0Qd3EbT90P8bL00hMbWdI0uvTFXLn3_KfZuFbbUOJMM-nqhHKzvOO1Onpto9WakW1zZvkDu5V6qaI_KWIrbJghtYDhDa45Q923Px_-lREDsMQC0w7aYIs67Fxw2CYfywrjY44UOxxAV3he8dNh2qIdW4YGPz5AzwAhweRz7nbC3_ySOR5e7YdKW3kr_m0451W6P8Aho3fGN7faQCvIoi3mvvlEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTmKpoX5IhP7zU2ueEzqHhAyBg-2Owm9ap0CT93LPCaSRKE0GYnEavTnxSXn6Q6FgV4ajRj-iSJ4mHOpsuihNb9yl3vhxkP-jftsg48isyI7Q4-Xgf2qNhCHLAFL4abJVgvtGmKaTAMO5x-ako7uqKGeXunWWRWog4rtlltzYGZYfZ28g0L3uW7-ovMlzqXyKIoNplhjT_2p7vI2DwW_171FQE5ODfGSX9sCjTFdZdTdNso7zugiUQhpU2Sxa_ooVLJm_EKujUvgNLSygolOqOrL0Z-NysLAgOBOXHHEes6cLbvOk1OuZAcQtIzBxBLyOVEBp_tWSzPt0ptw1Zhxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4aPeUQBQmJ8hjVZ_gQQpL70d5f-L-gPt_IasDyvxqmQXaXPM1Z5bC1S0t-w55c1-4nmq3VJU_qITJSu8gHhtVFQ_w3qfPQ-T6u6DrPPrVYImBY3c44TAuIb6RY-reJ-c2R-ibac-qA57KNHR_J2D145WkjQ77Mj4KW1d5strtltqRrqpXRwfP_aoV8PxoXr1hUsnaJebXfK9le5uk7_w5TlV6gtm_17GVyuB3puCeKJl3wYPPinv7vcRIfTgR8ZMwOGl4jJD3MQcwMWejWlXoFLpYKDzwmdagxqwIDZuGtydQTBb11l5rpNNyBzVxMM6NMDYo4enmj5dsgSTMmyzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jJWHAy7PiEcpWHeuudV6CbmA_RPsMqY9tFIxyHq8KabxsQy1lhWhEnJ1IwDjnp168xZhNyVH9nkCHclP37Utw46Q5a4Rao4TumElu3r8UuKLluX1il1rKjdEeitvf7a4YCVKKSJZ2iThc61nK1H7ceSD_jqirukVUMES8uYuDki-fQny80uKA7vD4xn4_EIdOA0ShrwbdwJh5Fw9RvTorZj-ZDZhHA6Yq0tw6MgyfiqJY4cpvWMSw1jqIHSjzK7eqlvTd3qBFZATkG0bBNQDse95_r_x4LQpzKNoQ-K39WoTivYVPh4AhpjAsgzcsqJg4EmI21Meg3WTYg9TXq9wFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نخستین پرواز بازگشت حجاج به کشور
عکس:
هادی هیربدوش
@farsimages</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/439306" target="_blank">📅 23:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439305">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/095eba5046.mp4?token=um1VYB28rntby1kA3MA1rj8oOS7OwHdOJ8ih0L21YO_E13Cf9-yUVDb-phjekzuWMjX9Y1bO3S5mGsH-TLOqgy9wwg7osMHVeDF0TZPlZHY2X98PFxoB4eP59We7hLGCbu6UBsegUcn4H7QadAVWe8EdNn3f9WxdM66n2AEgRT5AoSksmdvrgzVrrMSPBocjahps05ho23aSelWCGoBR9XZmqH9hHa2es--e2DCdui01R9lrX7cazFQIzsh7CpN-Tplmw_360IKLOrLeD1pqpQFK9fT0eiz65MThTgrGgFMl7jn8nD7MG-CFlTzTfSArGKQPz83ey13p8Mojil_2nG2faY5ZF7mtxPlgn1WZBiTn9zBZwVquOCpDvPQWQ92HGRi9Cznh9LDHVvhOyI840WAsAFZ7igs2XKTcMcofvC65A1GHMCYKZVNswUEjmFaYF24OfUCtH4WxJmsdkUVXaXSRDYliX17-uPfhaWOPXsAtdR6JODC3tLFChzznOkMWFBRXhJqqqb1FQe-Ds-orOuckFAu9c1gncO8q0Yt4Ve0Ige7Fk-t7lzs36gRcbry-5mGZqORwY0IeYQb5bET8thXHXMEblKcU5B4pYKD-o1R4y_A-C4AH3tQFij87M7t_o2dU0xqEI0Fxktqdricn7R4sRA5LKkW7FUVfsXmmeic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/095eba5046.mp4?token=um1VYB28rntby1kA3MA1rj8oOS7OwHdOJ8ih0L21YO_E13Cf9-yUVDb-phjekzuWMjX9Y1bO3S5mGsH-TLOqgy9wwg7osMHVeDF0TZPlZHY2X98PFxoB4eP59We7hLGCbu6UBsegUcn4H7QadAVWe8EdNn3f9WxdM66n2AEgRT5AoSksmdvrgzVrrMSPBocjahps05ho23aSelWCGoBR9XZmqH9hHa2es--e2DCdui01R9lrX7cazFQIzsh7CpN-Tplmw_360IKLOrLeD1pqpQFK9fT0eiz65MThTgrGgFMl7jn8nD7MG-CFlTzTfSArGKQPz83ey13p8Mojil_2nG2faY5ZF7mtxPlgn1WZBiTn9zBZwVquOCpDvPQWQ92HGRi9Cznh9LDHVvhOyI840WAsAFZ7igs2XKTcMcofvC65A1GHMCYKZVNswUEjmFaYF24OfUCtH4WxJmsdkUVXaXSRDYliX17-uPfhaWOPXsAtdR6JODC3tLFChzznOkMWFBRXhJqqqb1FQe-Ds-orOuckFAu9c1gncO8q0Yt4Ve0Ige7Fk-t7lzs36gRcbry-5mGZqORwY0IeYQb5bET8thXHXMEblKcU5B4pYKD-o1R4y_A-C4AH3tQFij87M7t_o2dU0xqEI0Fxktqdricn7R4sRA5LKkW7FUVfsXmmeic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام مردم قم به بیروت: مقاومت تنها نیست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/439305" target="_blank">📅 23:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439304">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d2391a616.mp4?token=hQCg7JPJ4_ynDTFoUwrtxjBWFnRQE8TdGdoa3SmJquyRfPmaV7qnD0po_jpEkML4VNIUUcOK4-mERCGm-IW72Ti7SQFA99ImZ86qluBgKVEoZibp7j_kUCkT_-nA197S2OCvCrSEFXy-qOmKGpG6edNCU1vqmJjz5dT2QyjQYbnUt9pF-dhLdjkJKIRqEY_ErrMmYBGzNI2YSqNZj8EXwgt2OCdMyFQsUecndNMfavrbss_1TdKO1v03aUvS8jRDab3ZNh92s-gtuXHoSoO244XDXzNHUB1LTAWdhLY4tp9C3l5oG044NLCkgXT5VWP4BUFauR_BGLMCVmUyae5Ojw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d2391a616.mp4?token=hQCg7JPJ4_ynDTFoUwrtxjBWFnRQE8TdGdoa3SmJquyRfPmaV7qnD0po_jpEkML4VNIUUcOK4-mERCGm-IW72Ti7SQFA99ImZ86qluBgKVEoZibp7j_kUCkT_-nA197S2OCvCrSEFXy-qOmKGpG6edNCU1vqmJjz5dT2QyjQYbnUt9pF-dhLdjkJKIRqEY_ErrMmYBGzNI2YSqNZj8EXwgt2OCdMyFQsUecndNMfavrbss_1TdKO1v03aUvS8jRDab3ZNh92s-gtuXHoSoO244XDXzNHUB1LTAWdhLY4tp9C3l5oG044NLCkgXT5VWP4BUFauR_BGLMCVmUyae5Ojw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی کودکان پاوه از تماشای دستاوردهای پهپادی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/439304" target="_blank">📅 22:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439302">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-OLH4Nc1OpgRV2c8kGb8HWDqVRxY28x-d1QMPVZn4D8rsDtchPa5DEgCGK-kP4QICU3A31SMYLq5H911xiwP9tBb79N3Buq_3CikUwRLbzWyc6F3c0QCJJcsMlVaxiIRNpULjET9J-GlQZv-R6mvL0P3Ok7g_iCCpUNvhuF3fGZgEChxukUyoQ2vmOZQ7VHW0HRq5aymCw-kD8w0JUfiLFdusxeNoejy_oLnugQDD5J_0lmY_VO-vz4Ps64xmaEAKZ_tPX1PVr1VhrMmUuuvNPpJYnuwvJdd1VExEtZLhJxrCgY15ZAeJfZKMhT-jOF0X6j4bVqkCwrQdxu30aszg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: شرارت جدید صهیونیست‌ها باب‌المندب را مثل تنگهٔ هرمز خواهد کرد
🔹
شرارت صهیونیست‌ها در لبنان و غزه در سایه حمایت‌های وقیحانه آمریکا، عزم محور مقاومت را برای توسعه پشتیبانی‌ها از هر دو جبهه، اقدام برای فعالسازی سایر جبهه‌ها و همسان‌سازی وضعیت ترافیکی تنگهٔ باب‌المندب با تنگهٔ هرمز رقم خواهد زد.
🔹
رژیم مفلوک صهیونی بداند جنایت توامان در جنوب لبنان و غزه، او را در گرداب عملیات‌های حزب‌الله و طوفان دوباره جوانمردان فلسطینی گرفتار خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/439302" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439301">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhKxrOpfh02KOor7aE8sI_LeyIogpl6SJ_D167f0Qwx7n-65oAUHXd8fFew8mTZqs3SNpylDIRZl3s42Dj8zgQ9uNx8m7_XSNxfJWBouQCQ6Up5TKVgqw9heqTQNOADqxsw3nsIhAMGGG-AlVmd-ddddHl_iL_eTXKvy6NvhjqN_vQgYtyL7Qmk2PqC5jOF_bO1f1ogoYNRmO0reFBZv6lIqrdcToFWfsZKkAvLuqE6f_t0Lm-y9byDotOh3VB5T2EgTkM21sptVmJsMPJuT0grHFC9cA7-w1VEc14VfnzwDvaKIr1-vBDeRJ9SKRLE0Nf_zZIPgzCzm6g2Tne3kZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به ناتو: بیایید و به ما درباره ایران کمک کنید
🔹
رئيس‌جمهور آمریکا در شرایطی که گزارش‌ها از مواجه شدنش با وضعیتی سخت در قبال ایران بعد از آغاز جنگ حکایت دارد بار دیگر خواستار کمک اعضای ائتلاف ناتو برای کمک به بازگشایی تنگه هرمز شد.
🔹
او در مصاحبه با سی‌ان‌بی‌سی گفت که متحدان ناتو «باید وارد شده و به ما برای خروج از این معضل کمک کنند چون آنها بیشتر از آمریکا به نفتی که از تنگه هرمز می‌گذرد وابستگی دارند.
🔹
ترامپ در پاسخ به سوالی درباره اینکه آیا از متحدان ناتو خواسته در عملیات بازگشایی تنگه هرمز مشارکت کنند گفت: «اگر از آنها بخواهم این کار را انجام می‌دهند ولی اطمینان ندارم که چنین چیزی بخواهم.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/439301" target="_blank">📅 22:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439300">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658cf46d1c.mp4?token=rVL6HkSSSG5jJn3v5jaomZbnBTWMf0qo9FUZWTlFwu_CfConWZ4eYF0lvbkeOicRTAqGaDagHV8G2E_1xS2HB6VJ95FnQ9xIq33Y4TEh3Wy2SBLiF-t2fHfnRg4A4dnZPlVPD_iXIwsIAqWlqxcstJBkIe_uQeeRVulcL7sHLmuw9ddZLOP-byGpxpQiwsC_Hey3r5Tk8EUiMi97dgGN3PawnSXYCOpN-KFV6kk80mXc4bwpVX_9SXdLQjuhgubtIfnwdNE3zsVfL1elO4YUZAkeElSm-E4YhuQqcb-820QBuX6uq52NeYaGfXnHsHfBy5jeWas5Cthysjb2D4SWz6X_9J3ngYPPEQpsiEMAWM2sKmeE5OLtxO2GRWpsLsP6mDCCSx8xpdh-wDx6QJj5YNxi87PiaT8W8FVu3Tq4BGHnpms3hHU2oG5d4W7TNkMoaE7N1GFGYXw-Xl7pSKUEks806lm-VcF30xwmeOmuWQgGnmoJL-7fCaOt_Pw27A5sr1natZodgmofiMigmO6HxL5TNqAPtfXOqvMrOCiOmq2HtsLSF3h2GogguBl3_xJwPzio38pK6Ov9PWlHAKxj0UUb1o5U_awr6Sz2ESiZ5n6JdpvdvzfKr-mbqmJjIqpWLYpWj8ogCIskLUp24VNQnijeHi505mfs5jZJBMmxZPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658cf46d1c.mp4?token=rVL6HkSSSG5jJn3v5jaomZbnBTWMf0qo9FUZWTlFwu_CfConWZ4eYF0lvbkeOicRTAqGaDagHV8G2E_1xS2HB6VJ95FnQ9xIq33Y4TEh3Wy2SBLiF-t2fHfnRg4A4dnZPlVPD_iXIwsIAqWlqxcstJBkIe_uQeeRVulcL7sHLmuw9ddZLOP-byGpxpQiwsC_Hey3r5Tk8EUiMi97dgGN3PawnSXYCOpN-KFV6kk80mXc4bwpVX_9SXdLQjuhgubtIfnwdNE3zsVfL1elO4YUZAkeElSm-E4YhuQqcb-820QBuX6uq52NeYaGfXnHsHfBy5jeWas5Cthysjb2D4SWz6X_9J3ngYPPEQpsiEMAWM2sKmeE5OLtxO2GRWpsLsP6mDCCSx8xpdh-wDx6QJj5YNxi87PiaT8W8FVu3Tq4BGHnpms3hHU2oG5d4W7TNkMoaE7N1GFGYXw-Xl7pSKUEks806lm-VcF30xwmeOmuWQgGnmoJL-7fCaOt_Pw27A5sr1natZodgmofiMigmO6HxL5TNqAPtfXOqvMrOCiOmq2HtsLSF3h2GogguBl3_xJwPzio38pK6Ov9PWlHAKxj0UUb1o5U_awr6Sz2ESiZ5n6JdpvdvzfKr-mbqmJjIqpWLYpWj8ogCIskLUp24VNQnijeHi505mfs5jZJBMmxZPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده ولی‌‌فقیه در سپاه: از مسئولان خواهش می‌کنم شفاف و روشن مسائل را به مردم گزارش دهند؛ این سبب می‌شود دشمن نتواند سوءاستفاده کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/439300" target="_blank">📅 22:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439299">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e045d91e9b.mp4?token=cJYilgktkqAaiPOhxpZvBT7EEdQZY2-29kl8r7NW5F7GR9FdfWSA5cnu9Croak_hzDjyXDCmfGz68j8tGRm8-parpNgALTvmB1uR1KA1RE7XVcg3f3seOpufjrE0mEWOSGkVPGxhAvMssvsp-GmLo2-ux3hlbHqNrDbJfGaGR-WEkRBI4vnCWXYV1T2S4T1jqN9_Wt24Hi_Vae6rPEEgrKa8bhESrxuH9yFAFmdBwWhCF--9qTmWnxc-zPVPMXV6AN-tqRZe9vwyD-HyfNC7HquOlDFjGwMfFShoHjcNLWMF2b-KY5CW85Ubo09iqvi95HpukOvWqAVPgHzQoJqRVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e045d91e9b.mp4?token=cJYilgktkqAaiPOhxpZvBT7EEdQZY2-29kl8r7NW5F7GR9FdfWSA5cnu9Croak_hzDjyXDCmfGz68j8tGRm8-parpNgALTvmB1uR1KA1RE7XVcg3f3seOpufjrE0mEWOSGkVPGxhAvMssvsp-GmLo2-ux3hlbHqNrDbJfGaGR-WEkRBI4vnCWXYV1T2S4T1jqN9_Wt24Hi_Vae6rPEEgrKa8bhESrxuH9yFAFmdBwWhCF--9qTmWnxc-zPVPMXV6AN-tqRZe9vwyD-HyfNC7HquOlDFjGwMfFShoHjcNLWMF2b-KY5CW85Ubo09iqvi95HpukOvWqAVPgHzQoJqRVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: روند را با قدرت و با صلابت تا جایی که جان در بدن داریم ادامه خواهیم داد
🔹
یا با قدرت مدیریت را ادامه می‌دهیم یا شهید می‌شویم؛ جان ما که از رهبر شهیدمان بالاتر نیست. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/439299" target="_blank">📅 22:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439298">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07a3f0b51.mp4?token=OBYSxieWH0_dcqaTndp7F_Hx9yp7ineFIs72lEFFFA5PQ0ZUbzVmktK5ba766RT4Q7IQOCniT-VWgVFAYS1ZsNLv1E2hRZs3Bs1i58dPqkCL7dgzTQrJ8m0j5XcciV9-M3iYfRrkMjNTc6oVjIsJPt7jYGvD-IAAWnuNb7EOztI9gyMRU7b3KqhnuJgvh6lFYhW2WC0wVU0x6figro3zWzQ9cLv4Dv-KopBHRQ4I6AvJlSH45jDigLlt5RkLZWZvLgFv28smGhRPyozAXay1CIboc8kUEd-m7ew0nPTlDNQ4tsciWXF-qdUSoEShy4n8NDknc7Y4LnGRSNunsT4fDyBTtHK2Fjh5kdlCOnRTusxCSm8EtnidXgnUq8sn7HOruSuY2_ey8Xjihh27WDjAwnz9R5seeDk0RA2TRyqN2fNjO8OvxQ9awuX7mEZTHJXRdBdBvkUmk9Kk7E89iXXcQWsrqCG71Os4BePSmCMKcITa1F0yArWjOmmG3BR3k6rXawY3U9IeuC7TMymduxgIiApDCIjdXUqs10pnpEnfEtesaEre6IxxSwK9SUr0cJ06Eif3R7BEg1Mg3Da88aRxA7u0_II3k0g-YNOzjfS_dDDJqfIodbTcQ0pp7GvxG1lj4zOiqXAjFB8k_xZBQX0KWoEdCokiVCnt7jz2mcgnLrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07a3f0b51.mp4?token=OBYSxieWH0_dcqaTndp7F_Hx9yp7ineFIs72lEFFFA5PQ0ZUbzVmktK5ba766RT4Q7IQOCniT-VWgVFAYS1ZsNLv1E2hRZs3Bs1i58dPqkCL7dgzTQrJ8m0j5XcciV9-M3iYfRrkMjNTc6oVjIsJPt7jYGvD-IAAWnuNb7EOztI9gyMRU7b3KqhnuJgvh6lFYhW2WC0wVU0x6figro3zWzQ9cLv4Dv-KopBHRQ4I6AvJlSH45jDigLlt5RkLZWZvLgFv28smGhRPyozAXay1CIboc8kUEd-m7ew0nPTlDNQ4tsciWXF-qdUSoEShy4n8NDknc7Y4LnGRSNunsT4fDyBTtHK2Fjh5kdlCOnRTusxCSm8EtnidXgnUq8sn7HOruSuY2_ey8Xjihh27WDjAwnz9R5seeDk0RA2TRyqN2fNjO8OvxQ9awuX7mEZTHJXRdBdBvkUmk9Kk7E89iXXcQWsrqCG71Os4BePSmCMKcITa1F0yArWjOmmG3BR3k6rXawY3U9IeuC7TMymduxgIiApDCIjdXUqs10pnpEnfEtesaEre6IxxSwK9SUr0cJ06Eif3R7BEg1Mg3Da88aRxA7u0_II3k0g-YNOzjfS_dDDJqfIodbTcQ0pp7GvxG1lj4zOiqXAjFB8k_xZBQX0KWoEdCokiVCnt7jz2mcgnLrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش علوی کودکان یزدی در میدان مبارزه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/439298" target="_blank">📅 22:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439297">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbf88be443.mp4?token=PHnz96Sn5GiCnzxh3Ljlm59uqW1l6LeoXUuW_IRRTVpOKS1fyeSwwOtgTz9S5c_Hq3vuKuoLj4WlnDyLqXGQWWlpjJsZlXIQjQp_O8W01Nn_4GhpTV8DftRF42Jhf3IpPNv9-2j0JIIHt6Hsc0-f2YgunigcWtXqvFcqRjGC7hERPCMZn2K3iWTo9lieMy29WBpO2NYyfSnp7jAnppma002nElLth4aJSOkES8rpR6mcHmLOAq7Ex9VWKkcSH1PdxRyz1dGx3YccRl4l6Cj6wPzW3E5IKRuTq-HXVZbDxcuUWRMPH_2N4vxjEDr2EUHeAPXInoQaA4s56dFz-PZqRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbf88be443.mp4?token=PHnz96Sn5GiCnzxh3Ljlm59uqW1l6LeoXUuW_IRRTVpOKS1fyeSwwOtgTz9S5c_Hq3vuKuoLj4WlnDyLqXGQWWlpjJsZlXIQjQp_O8W01Nn_4GhpTV8DftRF42Jhf3IpPNv9-2j0JIIHt6Hsc0-f2YgunigcWtXqvFcqRjGC7hERPCMZn2K3iWTo9lieMy29WBpO2NYyfSnp7jAnppma002nElLth4aJSOkES8rpR6mcHmLOAq7Ex9VWKkcSH1PdxRyz1dGx3YccRl4l6Cj6wPzW3E5IKRuTq-HXVZbDxcuUWRMPH_2N4vxjEDr2EUHeAPXInoQaA4s56dFz-PZqRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پلی که دشمن در محور تبریز-میانه ویران کرد، دوباره ایستاد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/439297" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439296">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSIz5bs8OzptIoNF_l7QJUhpMlYzuIwuHMCrCiiD7gq9BGNluI_hGK3VGNo6hIQw7w3J-YLizi8O68bL1EO5JDjwFNLhbcA6dBD97HniE3o-lOPjhYxHXnM9pdI-R4UsafaCtaKpy0Nih84BCAqofEIkf5EL6q4W0xiQCdUZEj03cVcypKmTUiGw-4vLr-HuwHe9QR51Z5ZnSP9LoXGYD1_LYW-naLejaYx71omEjdJu-2kHzyJDz6MkAk6_yT2FW5mz2WdNCrnAhZGX8VKH762EqkjdhAE3R8_XhUBaVPuiEJWYsD5SxgCJZDgwwPC-c_kdGhwzg-HBsVJpX8agvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
موساد چگونه با حساب‌های جعلی به
‌
جای هزاران ایرانی حرف می‌زند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/439296" target="_blank">📅 21:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439295">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f935ebf7ef.mp4?token=NQkYN21ztNJRsXmMDa0O9TXCkje-2lypHpoRmjuTeMX7LOimN__qI6sM6-Dutx7JJomIJJF8_oFT7H65CjadhX8Lsu5meixTV5MKR4r1xudfUsxMX8KzN0GK1_c4oUDT9abxrMpTm9kGGXNInbpSEIIsDhZEVaEs91tamZJTZmVv3LPM9K_d9pscW5ps2b_Iwq1BMpcX2PdzPO387MW5sfUEBAuRgdIXCpJJsqNw2RAwLSrGHCBwl-8wzwjQht-vLBZBXuMHhxJRIYuqSZlVTYJXJLV7c4hDTLNQ1nFbhY87fhIJiU_2oNrcOmioi3vGUsw3Do9rjxasNB8iNHEBcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f935ebf7ef.mp4?token=NQkYN21ztNJRsXmMDa0O9TXCkje-2lypHpoRmjuTeMX7LOimN__qI6sM6-Dutx7JJomIJJF8_oFT7H65CjadhX8Lsu5meixTV5MKR4r1xudfUsxMX8KzN0GK1_c4oUDT9abxrMpTm9kGGXNInbpSEIIsDhZEVaEs91tamZJTZmVv3LPM9K_d9pscW5ps2b_Iwq1BMpcX2PdzPO387MW5sfUEBAuRgdIXCpJJsqNw2RAwLSrGHCBwl-8wzwjQht-vLBZBXuMHhxJRIYuqSZlVTYJXJLV7c4hDTLNQ1nFbhY87fhIJiU_2oNrcOmioi3vGUsw3Do9rjxasNB8iNHEBcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار تانک مرکاوا توسط پهپادهای حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/439295" target="_blank">📅 21:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439293">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCcWUzxypIjJJdDoCxsRu4vE7e9xcwlG-Ca86J99ezZ-1X-oF8OroqxMiJclEErTpVxnoF9wIi_dpPG4l3c0qicq0mkjiDikgiID5DdjrcyxO4qLIrQEPu2xMZRNVZnI9OY6grQXxdf60UTgDzQmOsXpxOWwiASQezEUCpxFfm0QXiK2DVz1NjcXoa7bQX2GVjm9rupjAlA41IVhNcS8W0WIatmVGtSmQKKdPS4l10KWOPPEfJZISleBKUwtqSm835U_IILADYWzrqQdqHDmwmTkl83QEDQShgTi8ffOa6wUCv9QqdIlo4ZDEJQj3H7fe69qemCZRcMsPLXW9l-pyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ درباره توقف حملات اسرائیل به لبنان پس از هشدار ایران
🔹
رئیس‌جمهور آمریکا اعلام کرد پس از گفت‌وگوی تلفنی با نتانیاهو حمله به بیروت متوقف شده و نیروهای درحال اعزام نیز بازگردانده شده‌اند.
🔸
ایران ساعاتی پیش هشدار داده بود در صورت حمله اسرائیل به…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/439293" target="_blank">📅 21:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439292">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBrO6aHZJ5zM8_e2SlcWhPJYeI5L02oESbaHgxZJPF50b3FN4y80LiUZslkvwPHXt3MApkKMHyL4rJozjpqVfMor1LBgVaqvRu52q4sY3IIpAe5ujBguWtr5KaT3f55lcTXZ3HmdVjwlON95e5OrHVGbS0Gtxx7lDmJaG-NiTLtUx43kIB4CqPbGKx8TnRkupmYRmPl0npFUm4JVm7JclOMT_c-DESDUA9FurPNjF6qKjZAz_qsSUdbfBAm1Izu2Z6RDycGcUeR7XY68RiRf7XcbLY_fKW2m120kbb_jcSzwLbh6t4lYFKrQKsjuZiVnsY_8O9sjK_T_kx60ZhgQIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشت پردهٔ پیام امنیتی «اسرائیل هیوم»
🔹
روزنامهٔ اسرائیلی «اسرائیل هیوم» روز ۲۸ مه در گزارشی از تشکیل یک شاخهٔ محرمانه در موساد برای مقابله با ایران خبر داد؛ خبری که باید آن را در چارچوب جنگ شناختی، عملیات روانی و ارتباطات راهبردی تحلیل کرد. چون هدف اصلی آن شکل‌دهی به ادراک، محاسبات و برداشت‌های طرف مقابل است.
🔹
دکتر اردشیر زابلی‌زاده، عضو هیئت علمی دانشگاه صداوسیما معتقد است «این گزارش و این گزاره که "کار با ایران تمام نشده و تازه شروع شده"، بیش از آنکه صرفاً یک خبر اطلاعاتی باشد، باید در چارچوب ارتباطات راهبردی و جنگ شناختی تحلیل شود.»
🔹
این تحلیلگر با اشاره به سناریوهای احتمالی کنش اسرائیل علیه ایران می‌گوید اگر از سطح تحلیل رسانه‌ای عبور کنیم و خبر را مبنای سناریونویسی قرار دهیم، مهم‌ترین مسیر پیش‌رو در حوزهٔ جنگ شناختی و رسانه‌ای قرار دارد.
🔹
در این چارچوب، هدف اصلی تغییر ادراک و اثرگذاری بر محاسبات ذهنی جامعه و نخبگان است؛ بدون آنکه نیازی به اقدام نظامی مستقیم وجود داشته باشد.
🔗
ادامه را
اینجا
بخوانید.
@Farsnart</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/439292" target="_blank">📅 21:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439291">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌ ‌‎‌
🔴
حزب‌الله: یک سکوی گنبد آهنین در شهر المطله در شمال فلسطین اشغالی با پهپاد انتحاری هدف قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/439291" target="_blank">📅 21:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439290">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWVu8BmQUxvGOJHFgsrvHXSwhkwk9IDKom7l1uiw-L4SSEaA-lLIktoLWwSNYhuHzjJ2nGcL9I2aehNUWcyM1RVJNP8hYyO1eJWZRluXVKYMDh8lmjWQg9vJyxGhfdcXH2FEVCG_cQdZ0M_vKIZKJhvAYi_yhdgvAy6Qj7lLbUxCR9G3-ei5csUrlZiIE2SLt7bXSqL6q59i4ZhvfR-LojR3-IwTPEj-PFirmzee-eSacM1iKnaxSPAvjrvNdv4gP-WFi9mJIBQCGCdncFLYXJnl4HFLh2PUAtLmsqBQBsxmbYyJ73SPvZRRhaW5oI--TrWom1d3oW8HQYIX2X4G7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رژیم صهیونیستی حمله به ضاحیه بیروت را به تعویق انداخت
🔹
سازمان رادیو و تلویزیون رژیم صهیونیستی: اسرائیل برای حمله بزرگ به ضاحیه جنوبی بیروت برنامه‌ریزی کرده بود، اما در آخرین لحظه و درپی مداخله آمریکا، آن را به تعویق انداخت.‌ @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/439290" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439289">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgzWlcorpwxB_YFv_Kad3HZuB_UgE4UWm8VxRY-GqZJyI-ADWZvSw48SJH6S4LPJHf2Gf3H53Sau5qizjPyun80afcvYn2vKjGzSjzgflR1L0BEvOG5XakPKLBrrK1aMqQrdibyKj3ji_0rAlP1jPyVdx_nFxjTj9VhP5U8DNTiPdzQpL7QQ0iWPn2xlKUAZyBZnSFweaG5U6Swr9sU9kTsPYe0BXYxuoWr2-2qaAjpx0VvAZV_qSqffiVQtRFZSbiibGFQjJMOxn9u7WxwIuOUNMopHgNk7ilvfai7g4jggkKuOVAPEWxyYj86rxKDvhg_6YGyiWExftzgce5ERmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز امتحانات دانش‌آموزان از امروز؛ اکثر امتحانات مجازی است
🔹
رئیس مرکز ارزشیابی آموزش‌وپرورش: سال تحصیلی امسال به‌جای ۲۹ اردیبهشت، تا ۷ خرداد ادامه یافت و از امروز ۹ خرداد، امتحانات پایه‌های اول تا دهم آغاز می‌شود.
🔹
امتحانات دورۀ ابتدایی غیرحضوری است و بر…</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/439289" target="_blank">📅 21:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439288">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
هلاکت یک فرمانده تیپ «گیواتی» اسرائیل در حمله حزب‌الله
🔹
برخی منابع اسرائیلی اذعان کردند که یک پهپاد انتحاری حزب الله به مقر گردان «شاکید» از تیپ «گیواتی» اصابت کرده و یک افسر و یکی از فرماندهان تیپ گیواتی را هلاکت رسانده.
🔸
صهیونیست‌ها تیپ گیواتی را «پر افتخارترین» یگان نیروی زمینی اسرائیل می‌دانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/439288" target="_blank">📅 21:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439285">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پیکر بی‌جان «سلنا» پیدا شد
🔹
دادستانی اردبیل اعلام کرد پیکر بی‌جان سلنا، کودک ۳ ساله روستای چهل‌گز سردابه، پس از چند روز جست‌وجوی گسترده پیدا شده است.
🔹
به‌دنبال اعلام مفقودی این کودک و بی‌نتیجه ماندن تلاش‌های اولیه، با دستور دادستان اردبیل تیمی متشکل از بیش از ۱۰۰ نفر از نیروهای انتظامی، اطلاعاتی و امدادی عملیات جست‌وجوی گسترده‌ای را در منطقه آغاز کردند.
🔹
براساس اعلام دادستانی، پیکر این کودک عصر امروز کشف شده و پرونده برای بررسی ابعاد و علل وقوع حادثه در شعبه ویژه دادسرای عمومی و انقلاب اردبیل در دست بررسی است.
🔹
همچنین معاون امدادونجات جمعیت هلال احمر استان اردبیل اعلام کرد پیکر سلنا در یک برکه خارج از روستا پیدا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/439285" target="_blank">📅 21:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439284">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837f3b72fd.mp4?token=MamsvBW1OMO-ndLOwvpROvKnZM9nN7sCHQhMU0uOkNpz7_U9eYiJxX1Ingh6TaMDKpKwE7PiSceY29zdsMzQRkkdRWjXRXgZTSuTuZ0YuQoReOA2qpjXNsxqrlWuiJi9YG-Pb98VvAQkA8FSRUxN6I1t-TGcDTNrfbEO81eYDWEG-EUHWUWyVGtQo46O2QuOcvLUGxwvqa0JXypu0Tsn_PpY3nzwt3iPfBH66QBs1ek4U8UA-PBblYIuE-lMwHVwFJz4dYZcVpMEPiZdy41iNJHBEgKYAmqGJhyZnEKHYnHcDz8DI9OFUq76jTyT_k8f90NBC2GluzMyuipoJaKo0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837f3b72fd.mp4?token=MamsvBW1OMO-ndLOwvpROvKnZM9nN7sCHQhMU0uOkNpz7_U9eYiJxX1Ingh6TaMDKpKwE7PiSceY29zdsMzQRkkdRWjXRXgZTSuTuZ0YuQoReOA2qpjXNsxqrlWuiJi9YG-Pb98VvAQkA8FSRUxN6I1t-TGcDTNrfbEO81eYDWEG-EUHWUWyVGtQo46O2QuOcvLUGxwvqa0JXypu0Tsn_PpY3nzwt3iPfBH66QBs1ek4U8UA-PBblYIuE-lMwHVwFJz4dYZcVpMEPiZdy41iNJHBEgKYAmqGJhyZnEKHYnHcDz8DI9OFUq76jTyT_k8f90NBC2GluzMyuipoJaKo0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از آرزو در محفل تا برآورده شدن در منزل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/439284" target="_blank">📅 21:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439283">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pItz8uNPgpJwos7bInNBwa9tVdugQxFgEiOc1R6j-to080hocW024m7LW0TIMxqHH0rPoS6snb3wocsBpdQf4qo2OFXM0ozN6xxQy-CMlvW73Ccuf_GAyTLlyUhjCTThsS--Oqp1usJCJXegHDJ1WCW8j4uUpSUP_Q4PuLYOU_Mydhmwz6R0DYDuGa3BSIiQxxMVmAMGpG1lZWY3Z6H4guAV-6r8vb49iWGR8kldfRNlnkH80gQEJKNU_yQahu0hUV4meOSmruZpVe-gu7Hy6hwW9DBp4aZ0HkJTVJxK3NOoXqzkeeCzLkcFMS0wAJ4nbKHqRQ1xsxMoRYBtfAC92g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی: بمباران ضاحیه و نقض آتش‌بس عجلۀ رژیم جعلی برای پایان دادن به تاریخ نحس خویش است.
🔹
شما آغاز کردید، اما برخلاف انفعال تماشاچیان منطقه، ایران و جبهه مقاومت تا آخر کنار مردم عزیز لبنان، از مسلمان تا مارونی ایستاده است.
🔹
تاریخ تکرار میشود و پاسخی از جنس «ذات‌السلاسل» در راه است تا زنجیرهای اسارت را بگسلد. «نقطۀ پایان این کتاب باماست».
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/439283" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439282">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4KiUWGpammtQ7e6Yfn5g4BFryUe5Is7D4EEXcAMJRPor_BQlX9xLkl03uu0MzaP18uc5kcDG78Is6gVfy2zZMFRCGxxNhc_PygZtqFpZqh5YGu8_ND3wvTWGQudCpVTQB2VcX1nRcyV02bDLeMb_mV9SM4HVmI2oZYPJJafZex5ETMf32uwyKaaZZy0Pjzz_t7aND_kkPpONdZKEb5zTwDrL52zjdePSEJdULFT9U0E3hVJqS0P5W6AOxpCKxST_uT5M219PLetGn7R9NgPdnsXQ_fsWRmXoAR4CndaTv935AVBE5lDm8lW8zOuacNzG20pBeYfy4oWvkj-RE_G1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش ترامپ به گزارش‌ها درباره توقف مذاکرات
🔹
رئیس‌جمهور آمریکا: در مورد تعلیق مذاکرات از سوی ایران چیزی نشنیدم اما اگر این درست باشد، اشکالی ندارد.
🔹
به نظر من اگر راستش را بخواهید، ما بیش از حد صحبت کرده‌ایم. فکر می‌کنم سکوت کردن خیلی خوب باشد، و این سکوت…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/439282" target="_blank">📅 20:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439281">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
هشدار قرارگاه مرکزی خاتم‌الانبیا به ساکنان سرزمین‌های اشغالی
🔹
نتانیاهو در ادامۀ شرارت‌های خود در منطقه، ضاحیه و بیروت را تهدید به بمباران نموده و برای ساکنان آن هشدار تخلیه اعلام کرده است.
🔹
با توجه به نقض مکرر آتش‌بس توسط رژیم، در صورت عملی‌شدن این تهدید…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/439281" target="_blank">📅 20:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439280">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY6vUdKaiAIdsoIKHS8aUyqTnmZ_i7oVS4hkuHbFbaeVZce-Uuzt9qHgIjLp8AeQ-BjUGtiK9jv9JdYijZ2Y2smTXuBvuHEgKw1QlCN5zDQRTA-nvpMYWGZEWE8NcB3TEB24HCmEy0S9cZdlkrp7WdNZLPbFlxLDKydQfrD6t9xQCskIyEC6kum9udJ_nPA16-kO7-WVbdhn2UhDY8bfAOBCkY6MVOK-nikrcMyRLn0zY6xDC6ZW3vphUyts6AKzpzeur2jI40DngScxK8eUL8rHrAzf6JD0VlhErczXh5rugyu355aMu-agZcggoyCbvMlXfzUwe1dMFAL45ijZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بیانیهٔ وزارت خارجه در خصوص نقض مستمر آتش‌بس توسط رژیم صهیونیستی و آمریکا
🔹
مسئولیت مستقیم آمریکا، چه در نقض آتش‌بس علیه ایران و چه در نقض آتش‌بس از سوی رژیم اسرائیل علیه لبنان، محرز است و مسئولیت آثار و پیامدهای این وضعیت برعهده آمریکاست.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/439280" target="_blank">📅 20:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439279">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e094781ca.mp4?token=Fld3475-n9-M8NDJeiwLkPoH2gVTZ_JquMXwMwlTEorreZiAOQx2aCW7fMTJ2MlGPU2DP49sz4tYfGWZ5PPZ74BHMZMLJrRXSWv1Obv0g-0i2r9FheQIBvyCs-xSIZjFghED5zYgmipx3FvrrOEewQjtJoGy6FxR3d38iKNKmX9LYWoH5E2bqda7EPDIQBGtSV-S0gkEldNv8R1JCcE-apbUDRFHU2eAsLomTElSKySyVJU4ApdBQrMBiwUfwF0-962FVnGLTrFTbMQk25g5rcPi0vCoHhBqyHNYgqnFvjp5nyl48ALji5t0ZyHEArC_b9dvrhJPsR9Umkc6JnSNEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e094781ca.mp4?token=Fld3475-n9-M8NDJeiwLkPoH2gVTZ_JquMXwMwlTEorreZiAOQx2aCW7fMTJ2MlGPU2DP49sz4tYfGWZ5PPZ74BHMZMLJrRXSWv1Obv0g-0i2r9FheQIBvyCs-xSIZjFghED5zYgmipx3FvrrOEewQjtJoGy6FxR3d38iKNKmX9LYWoH5E2bqda7EPDIQBGtSV-S0gkEldNv8R1JCcE-apbUDRFHU2eAsLomTElSKySyVJU4ApdBQrMBiwUfwF0-962FVnGLTrFTbMQk25g5rcPi0vCoHhBqyHNYgqnFvjp5nyl48ALji5t0ZyHEArC_b9dvrhJPsR9Umkc6JnSNEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان در قم مدرسه شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/439279" target="_blank">📅 20:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439278">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Smn5ycEmSndjMEuS6H-Buil4Y3v2FwdUIzQ2OIUKYyktQpVgv8WnyuCNdNdozsq2knZhtMmlRWNi2aFxXDkRXigOgpd2__p35pVhJygOxIqA8720nfI3-VmIEWCDVK27qMlwT6fLAjqtVyDRMy6BbqKFBZ5Pzxp9CrzQxkknf_ox0PPZswfiVpxjyUxc_o9CipIHpGapHBY4lEeJ6cP_A_SBbC_WpwDg3VPvk8IxfkN9N1v2TL9ErVCm87Md7OgjP_OyrzF06T1mnB066muBA_fqLxHt6BIuHBGEzS0AGT6-Tn3xCE_spiMUAe4jFSos8S_YSp_7qYeRL0Szpu64QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد جانبدارانهٔ آمریکا به اسرائیل برای آتش‌بس در لبنان
🔹
مشاور رئیس پارلمان لبنان: «پیشنهادی دریافت کردیم مبنی بر اینکه حزب‌الله هیچ حمله‌ای به شمال فلسطین اشغالی انجام ندهد و در مقابل اسرائیل بیروت را بمباران نکند.»
🔹
روزنامهٔ یدیعوت آحارونوت نیز به‌نقل از یک مقام اسرائیلی خبر داد که تصمیم برای حمله به ضاحیهٔ بیروت با هماهنگی با واشنگتن گرفته شده است.
🔸
رژیم صهیونیستی که در روزهای اخیر در جنوب لبنان متحمل تلفات و خسارات زیادی شده و نتوانسته حملات حزب‌الله را متوقف کند، از صبح امروز مناطق مسکونی و بیمارستان جبل عامل در شهر صور را هدف قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/439278" target="_blank">📅 20:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439277">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🔴
حملات حزب الله به شهرک صهیونیستی «کریات شمونه»
🔹
مقاومت لبنان خبر داد این شهرک اسرائیلی را با چند فروند موشک هدف قرار داده است. @Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/439277" target="_blank">📅 20:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439276">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miEWBGqRQh5nwryvMKXOSny3cZWThCq1WJdAGCf2e831D_fOEyFUQkZGoB8SrX-nSRkUQs7b_cgRA4lXMybJPYqehckQPrh2gMNU0fJqAGqyl2Sf8ExJvSaFzon-sSVdOE-87eyHMjB3kKW4phU5jOPvbjAG-F8Xg2EqqGuJIokhL9AJouWymYOPE2OSeGV1aaG3oT31lK87wpVgn7gpRKTwKtdfmeG4qZUYcOJ_fNHgBO9gDVp6n0FYSjR9MAEaJB15OaLCNlX9wjZzmpBW_KQp8N-CDx9T8XM4qkaLwN71qtG1wZdHL2CI9l1RUYjLujD2-dA9b3fwBEvLhas57A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: نقض آتش‌بس عمدتا از سوی اسرائیل است
🔹
معاون وزیر خارجهٔ روسیه: گزارش‌های میدانی همچنان از نقض آتش‌بس خبر می‌دهند و این نقض‌ها عمدتاً از سوی طرف اسرائیلی صورت می‌گیرد.
🔹
عمیقاً نگران گسترش تنش‌های زنجیره‌ای به لبنان هستیم و اقدامات ارتش اسرائیل علیه حزب‌الله، دور جدید و خطرناکی از درگیری مسلحانه را رقم زده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/439276" target="_blank">📅 20:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439275">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Biug3gve-rtLH_DQ0otPhSoXVhIAI-bmbYZWi_3yEEtMUz-vcXNr3x0aiCNZsaUefDD_q9Z2vP_WKNoiOy5uOOhL6pl5knV5LNIS7jysxvnYWuNQuAbvx4MMc9hrobHdnT0XCF9e-ug6AQYjoePHyzDW7FzdSMzrSCthx5q5PpqRWNPK-hpZGnmJAdgrbE6cWwCht-dsrHDiMt6L6O5KODxzoo723DYVPyPC2yDTkGbSr4FQM9wKUKyWtdKUVwU0IhJDHeXv0zEXozWhYAalmdzespPJoiBFHBSdDHA74zZn99SNB8zt0EJ6EYRZIiETH38DLo0Ez3QxcOkmULLaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش ترامپ به گزارش‌ها درباره توقف مذاکرات
🔹
رئیس‌جمهور آمریکا: در مورد تعلیق مذاکرات از سوی ایران چیزی نشنیدم اما اگر این درست باشد، اشکالی ندارد.
🔹
به نظر من اگر راستش را بخواهید، ما بیش از حد صحبت کرده‌ایم. فکر می‌کنم سکوت کردن خیلی خوب باشد، و این سکوت می‌تواند برای مدت طولانی ادامه پیدا کند.
🔹
این به این معنا نیست که ما برویم و هر جایی بمب پرت کنیم. فقط سکوت می‌کنیم. محاصره را حفظ می‌کنیم. محاصره مثل یک قطعه فولاد است.
🔹
فکر می‌کنم به هر اندازه که آنها بخواهند می‌توانم صبر کنم. آنها دارند یک ثروت را از دست می‌دهند.
🔸
ادعاهای ترامپ درحالی است که کارشناسان درباره تبعات تداوم وضعیت کنونی در تنگه هرمز ابراز نگرانی کرده و از احتمال جهش قیمت سوخت و کالا در آمریکا سخن گفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/439275" target="_blank">📅 20:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439274">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
مادری که حسرت دیدن پیکر شهیدش بر دلش ماند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/439274" target="_blank">📅 19:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439273">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-byhn_mbAryVpXEVnFftwdH73_4pbBNuPqyZcgsMhLUIkQjG8vlFA-1s7dw-4yHLsnKWgvR_a5BvaXVwPdC862LGmcdfNJd8lrpunrefeLXWFAIjQ_SaBWxE1wUPMltcUtSfXHzStMjA8M-gA8zq876abw0iO2SUUphnAd6vhNG9YNL4koJiGrvO1fFi1Geyw7lYsWDxG8H0sStRF21gUy2ZhDV0Pexttzn-tgxfcAlYD03H-xvNqNrolKimUtW3rg1d3XV8a7oGoZSSdeCh5B92CGwe23lRbxPx5V_noP5GAQlCaa7DwqsfOTYmfjavc18wLW9MKYmJyLVshne9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج هنرمندان از جشن ترامپ، او را وادار به لغو برنامه کرد
🔹
بحران پیرامون جشن ۲۵۰ سالگی آمریکا وارد مرحله تازه‌ای شد؛ دونالد ترامپ پس از انصراف پیاپی چندین هنرمند از فستیوال مورد حمایت کاخ سفید، خواستار لغو کامل برنامه شد.
🔹
چندین خواننده و گروه موسیقی که قرار بود در این فستیوال در واشنگتن دی‌سی به مناسبت دویست‌وپنجاهمین سالگرد استقلال آمریکا روی صحنه بروند، در روزهای اخیر از حضور در این رویداد انصراف داده‌اند.
🔹
ترامپ که از کناره‌گیری خوانندگان و گروه‌های موسیقی خشمگین به نظر می‌رسد، هنرمندان انصراف‌داده را «بیش از حد گران‌قیمت» و «خسته‌کننده» توصیف کرد و نوشت: لغوش کنید.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/439273" target="_blank">📅 19:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439272">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeAq9mf6vmspqzK2FeypXKkdxOuphL-Zh-5Uwdoe_vK_tUCJi970jCAPPOH4b3OehFi2orX3i0r7z5EkCTh9w5zHXatoAR0CIHEkubBg7EwWMBJUpwxCTYkndEvhMwsIaDvakfyUdgmsZLqx00U3iM_0x_b0uTL2Hli8doVo8ccnZA08k9jzw1JARAViQIeDN9tm1jvyrXrkhX4nZRAbEKAIq6RJZT2YgXRVKP4xEmBgemX8E6_syt0Gl_HX8LwfI4spkKXU3xJrXSUbCN48ZcvVKuyMsXCjLAfK2qVn5TO74KlRPQQdQweOTzVig8QckvSyefIZfea1rDi6xSNCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: نقض آتش بس در یک جبهه، نقض آتش‌بس در تمام جبهه‌هاست
🔹
آتش‌بس میان ایران و  آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.
🔹
نقض این آتش‌بس در هر یک از جبهه‌ها، به منزلۀ نقض آن در تمامی جبهه‌هاست.
🔹
آمریکا و اسرائیل…</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/439272" target="_blank">📅 19:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439271">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2a767fed.mp4?token=q4fLGqNHqPFWcpmZ9d-4TeFl4mkMFi2t1Hehy6Z9nTPV3OmxAWeLiHHCruGzQzvtEZVeDSxudrtPD2lcpsODC6xpofX_uPDsaiFc4SdB4nNKHpj-RelNplsSmkERU2kYhk0DESwvNMjn2-i9K_KZ95Z7VMh-eO3S74CfRxCfRHUhaENpYuKMhl5z11PNufO4pRgMQ2cc1f6Bv2k_hOZipX65hbw7nDPsg2lvsOqJg92yZOYFWP0vGWbhz0Zo7sHuXDyZkA0ZBarty8DwriXt9d5YqPwTnzogjEYzycLE5edVDMKoGLpdarfrNEH_aNrorwYoP2rsyTDtCrx6TAUuLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2a767fed.mp4?token=q4fLGqNHqPFWcpmZ9d-4TeFl4mkMFi2t1Hehy6Z9nTPV3OmxAWeLiHHCruGzQzvtEZVeDSxudrtPD2lcpsODC6xpofX_uPDsaiFc4SdB4nNKHpj-RelNplsSmkERU2kYhk0DESwvNMjn2-i9K_KZ95Z7VMh-eO3S74CfRxCfRHUhaENpYuKMhl5z11PNufO4pRgMQ2cc1f6Bv2k_hOZipX65hbw7nDPsg2lvsOqJg92yZOYFWP0vGWbhz0Zo7sHuXDyZkA0ZBarty8DwriXt9d5YqPwTnzogjEYzycLE5edVDMKoGLpdarfrNEH_aNrorwYoP2rsyTDtCrx6TAUuLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چگونه در برگزاری مهمانی کیلومتری غدیر مشارکت کنیم؟
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/439271" target="_blank">📅 19:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439269">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dbcc1692e.mp4?token=BQelO0ekxScIIARBSanx7OHXTZha7MnSzjRfLhc5DjID_MI1_AxWY4b90fdrc3UEhYbi9fqq7RWYk3Z_d9qKxq3NhVdnhAJIsH7vyYtl_y-Ut6nb29kDkD1uxu_5f-bAU32cx1eY6-WiqrWDw5RtZ23lvoYRkEveWyhwbcM5HDdRLiJxJDV_vBJMQi5zSkBPaD7de8wRPseqZq39zqlm5TDg6a9GuxMR4ryUjaW9rE_JMuo3yg9QALpdceiO9Uqd_5AnZOMZzTTVKTiI5QwrF9Da3q8PDKt9Bv2X1AzcoKiUCJT-sshRwnUQtzduFxvIC5sPo8RwB4YnlBnbqf_IEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dbcc1692e.mp4?token=BQelO0ekxScIIARBSanx7OHXTZha7MnSzjRfLhc5DjID_MI1_AxWY4b90fdrc3UEhYbi9fqq7RWYk3Z_d9qKxq3NhVdnhAJIsH7vyYtl_y-Ut6nb29kDkD1uxu_5f-bAU32cx1eY6-WiqrWDw5RtZ23lvoYRkEveWyhwbcM5HDdRLiJxJDV_vBJMQi5zSkBPaD7de8wRPseqZq39zqlm5TDg6a9GuxMR4ryUjaW9rE_JMuo3yg9QALpdceiO9Uqd_5AnZOMZzTTVKTiI5QwrF9Da3q8PDKt9Bv2X1AzcoKiUCJT-sshRwnUQtzduFxvIC5sPo8RwB4YnlBnbqf_IEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد مردمی برگزاری مهمانی کیلومتری غدیر: ۲۵۰۰ موکب مردمی در روز عید غدیر در تهران میزبان مردم خواهند بود
🔹
در ۳ سال گذشته ۱.۲ میلیون نفر بانی مردمی مراسم غدیر در تهران داشتیم. @Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/439269" target="_blank">📅 19:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439268">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-53.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/439268" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-52.pdf</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/439268" target="_blank">📅 19:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439267">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qa-JAlfT0pawKoWGmEF-exv0BMJ3UKcGQbnP_GZqFgTGeVboXj2lPounF4NAZb7nZ3R6Q6BayF3bw7AX_jEL23RSzdswH_VFf9dpGoIOXtm7dOV9mqdir-pabRQY0a_wJerkaOqGpsgoFpneQo6LnRrARqJvnQl6RhXUgy6KfNuebltac7g9pnYtRKVAh6Lw3MM6_SKf9OwpWAiGXpYQAFisdmgb3yxFe_kHQw38JR_dEIJ2R8bfdYYTCNGF77OgfygqsNrRfpPfVViL1rcgh7lPpp_8W6w66ZmKFAKCx_nAh1PDT46KKbTwob54nixdi4xW35QpcykDOfWOsfzkhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار قرارگاه مرکزی خاتم‌الانبیا به ساکنان سرزمین‌های اشغالی
🔹
نتانیاهو در ادامۀ شرارت‌های خود در منطقه، ضاحیه و بیروت را تهدید به بمباران نموده و برای ساکنان آن هشدار تخلیه اعلام کرده است.
🔹
با توجه به نقض مکرر آتش‌بس توسط رژیم، در صورت عملی‌شدن این تهدید…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/439267" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439266">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJSfEF0yjgJsoyoQxe-ObfncQsQ0HZXHn-DcxQI4juIjLe_o8ftgm61QDHzGjZAjbgcYnj2vFh5LvtyJWouMYZKAX-Ual6Ad-DNWv0YlHkqDeFU0PDiTMKcypYidyEjS1Aql7sQ4o6gQdHs7BPXNog67RM-ZkGMnlE4hkKMu4vIUxRyMMQBZc6wdXfoQcwP2-BLXs1BQ9zbWvqE-_KcTPZo7HVKvy2blPOTsAZZ-2Q7D1N-WP3oTe2TQnh0GIJX4Pd0RIuS2BfW05z3rmH7IzvkrYs48x8-FWmbifajzfLgEhKG4hdMz6QtqBlxhrMULYNXAGcsZ4bbcPRSPxNoKQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار قرارگاه مرکزی خاتم‌الانبیا به ساکنان سرزمین‌های اشغالی
🔹
نتانیاهو در ادامۀ شرارت‌های خود در منطقه، ضاحیه و بیروت را تهدید به بمباران نموده و برای ساکنان آن هشدار تخلیه اعلام کرده است.
🔹
با توجه به نقض مکرر آتش‌بس توسط رژیم، در صورت عملی‌شدن این تهدید…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/439266" target="_blank">📅 19:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439263">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
هشدار قرارگاه مرکزی خاتم‌الانبیا به ساکنان سرزمین‌های اشغالی
🔹
نتانیاهو در ادامۀ شرارت‌های خود در منطقه، ضاحیه و بیروت را تهدید به بمباران نموده و برای ساکنان آن هشدار تخلیه اعلام کرده است.
🔹
با توجه به نقض مکرر آتش‌بس توسط رژیم، در صورت عملی‌شدن این تهدید به ساکنان بخش های شمالی و شهرک‌های نظامی در سرزمین‌های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک نمایند.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/439263" target="_blank">📅 19:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439259">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHHMYPULRsri3Sk5gA0TouwK_JrzBG9jbaiuwxiOU2WY4YkQyaXSi7xMMcqIu_3X7XvUQXxZdDYoRb1blYnaKkvTJpxwzxDYsl3fqQO_Qia5NUSixAhK_ZtsVqB0eRVoBVYPZTGFgwDLS6L-WCnHx94K4onQW89Sb60IaSW61w7ljYJYIx9sMMwjxdDPSav0knm997c_9jdTNZWl6IOY0AmF6yfens191oWyh1ozfpgk7eLVBj6_L7P5TwKmerSW9Nu01jn5OCXabL0V7i4GmFzn0pL8E4TYKA3tUY6tfVgr_KI_Xti1-sK3WN5OLRfeWlLsdLjjhXrvm-M4CKTHFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFMZr_OwcK1r48RqTjVmVSVfNOGd2ZK2gs-FRJVHbhRFdAmaeudfnqcVT4hhiZKFEbuQ6Mx0WcuGP3bTRJbJUsMp57DFxh4KGiK1cS8RKPtUAMsZgZKtY5UOV9q1E-Nqy2yo8dBiAWFex6fcq7cTMcCDpClTzQ9D3bzcQuHNxy1bzjihER-TxqMUTduIykqnfzrcCXp6msDtB9P9tYt9U4rRqcrQmqX8m4IryMM6XgbQ67EcvIxc4kj-oorhDbhqkzG7fWdvDfy5cKYKI2H3QDCxb8gkDVqtHhyjRaJDEBi_GFRe7wLTmM_Qvo7ZOLxruFARPWIGPNme4xbXqOASDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_qGB6fzrWSTs8hABDdSRIGoaM8_pRiywjBxpceMegJzj5odkGEq6oDzO2O5DxmiXkAK6MFV5XjMaO94DWiD4xYQURRFDyHaMQoVVAK5IYvJ2fOIf1CzkKNEjf-GXbr28Xs5bi4u9UefpYldd8sWGPyMdaVa8K-2mDIvVFW7e19y_e4l7q4isqPljR8vUs9SQc1jlV1K1CMzwntdKvgyo5xHAdHXywXVI_zCB4d-iJE_m2XdfKBxiAq1HSlMSpvvfRRsSAgv67XXSdT5t5thg11e9KKsyp_9Iu1OX-Xjf7kapvz_A0oIIhE8SbZ27bLxv8bhNUTRwjxIlwG8oiiNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXHvMC59fGb_34BLCXhXFfFT6v5Hv4egKuKH2Nml9y2A3U9cNCJ85uL8tnZ0RDiKQbriCF1v3AOLDTckBOnowgAf1Yaap6LekPX0_KHLpiZVhGnHy4upkiXudRC8fHcCShNjNqLrhYu90igxl2RQzja-n7rifpsj6RU2kmJVXGWpbYwXVcDpZL5KDHMECY4kDGRkpzZIZDURiBOyrPgADMBFBLH2Je-YXc9zibD3oGYBb618L-WakX4aNOL6dxflQNtGt7wBbU0Zqpt7l6A28X2DkPhBR2llkmAKgyJ6gDEXpeN8WW0iitLEOtd_Ze-R3vtxxMxGjYANZrp04R12tA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مصوبه منع شکایت دانشجویان و اساتید ابطال شد
🔹
مصوبۀ شورای‌عالی انقلاب فرهنگی که امکان شکایت دانشجویان و اعضای هیئت علمی از برخی تصمیمات دانشگاهی در مراجع قضایی را محدود می‌کرد، با رأی قطعی ابطال شد.
🔹
سعید فدایی، وکیل پرونده، گفت این مصوبه مانع رسیدگی دیوان عدالت اداری به اعتراضات مربوط به پذیرش دانشگاهی، بورسیه، نقل‌وانتقالات و آرای کمیته‌های انضباطی می‌شد.
🔹
با ابطال این مصوبه، مسیر پیگیری قضایی اعتراضات دانشگاهی در دیوان عدالت اداری و سایر مراجع قضایی دوباره باز خواهد شد.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/439259" target="_blank">📅 19:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439258">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHYJYLGIkVENeZVaJu3cKcYbC2nU5kq4oLtgZUZGTgYf5f15YpeoF2VqppXy27vcJJUqynWmeQkFX1PT-kB39Ws_ERqBGZwVNV27u42gfedyQsk96hgn-7lmRGwSSkHgPeLgchhkt3QdVLE03E1UuCn3-uf48CnxY8aTvuNSWQF0Hp5jZtp1DTNXX_UVZbwFAPskmao_oHBhdJbQAo-e0qGr6Vei_02yJSQL5aLw7zR83Pke96Y4zJUFmzoLENjn6ySUdK3XbPc1B1N5oNsCInqTwFFKE3NHYdIIO6ylpOdv5llyIPssorV_wXLUvHCDBcT_HiRRvnVOeViPaAcpBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اول رئیس‌جمهور: فرماندهی رهبر معظم انقلاب و وفاداری دکتر پزشکیان به نظام بی‌نظیر است
🔹
فرماندهی مقتدرانه و حکیمانه آیت‌الله سید مجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در شرایط جنگی، ضامن اقتدار، امنیت و آیندۀ روشن ایران است.
🔹
رئیس‌جمهور نگاه خالصانه،…</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/439258" target="_blank">📅 19:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439257">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1i46lu851RkIjENphYpHwf9KgPCFNw5hjKOVyRX_rcnqz9Ijh7S5_8Ew_Ps_bMaM9AARfyN2DZMpUkJmW3abnw2bvAlP31HKlJy03PdEMuXt5IRULDYTulG1W1bW6JwvdXpANRidZWHY58rBOUaOZGNlDektHIKXYjBYAxzf2se2tzWV04VdKbmNh_BdqM2bz5H-F904tPu9XDqqdKCxr1H-7p6_5WgyY3jZt7aCuuShXQy_pzflkm14Cji2TR7wKPj2xZ0Q4sW6vCflAaM7ttCu65bgKj025o7eVsoudNS0s8zzBPXZ8R_UgIXkMBCjVbcgyv8_2KGgGktUnFpTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محیط‌زیست بخشی از منطقۀ حفاظت‌شدۀ بهرام گور را به یک معدن واگذار کرد
🔹
شورای‌عالی محیط‌زیست محدوده‌ای در ضلع شرقی و جنوبی منطقه حفاظت‌شدۀ بهرام‌گور در استان فارس را به‌دلیل آن‌چه رفع مشکلات شرکت گوهر‌زمین عنوان شده به این معدن واگذار کرد.
🔸
منطقۀ حفاظت‌شدۀ بهرام گور معروف‌ترین محل زندگی گورهای ایرانی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/439257" target="_blank">📅 18:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439256">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac10398c9c.mp4?token=kMXnmKQW4Z-4-qLdtOFGF6AA2h0XIXwWcR1gLgqRfcuPJa-i67w7ONugBtkChNNkk1IflvZWazyAULVE72E8P3B3sUItqpeG0nrS1ffjRXRCWd-61qahtNEp2AW7ulX89aV9iJlnheZYT9PaAllN3673OOcroi3xjAdFZ2tR3D6wSYQxdWafvBiUGtW6DleYRkOb_r-5tzq4_wlo56ZLuh75ctkd47Fq0ciEsQQoSTmmnOv-mtV4uKehvYHAH-e_bd00lJbWCGYZjxigVFuWUWmbxdg3aYpWlF7ogh-9pmJsikkrY2D-NUrDCy0SyW_yF67oRUgehgVOk43MrrIb8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac10398c9c.mp4?token=kMXnmKQW4Z-4-qLdtOFGF6AA2h0XIXwWcR1gLgqRfcuPJa-i67w7ONugBtkChNNkk1IflvZWazyAULVE72E8P3B3sUItqpeG0nrS1ffjRXRCWd-61qahtNEp2AW7ulX89aV9iJlnheZYT9PaAllN3673OOcroi3xjAdFZ2tR3D6wSYQxdWafvBiUGtW6DleYRkOb_r-5tzq4_wlo56ZLuh75ctkd47Fq0ciEsQQoSTmmnOv-mtV4uKehvYHAH-e_bd00lJbWCGYZjxigVFuWUWmbxdg3aYpWlF7ogh-9pmJsikkrY2D-NUrDCy0SyW_yF67oRUgehgVOk43MrrIb8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶ فرودگاه کشور میزبان حاجیان می‌شوند
🔹
در عملیات بازگشت حجاج بیت‌الله‌الحرام به کشور، نزدیک به ۳۱ هزار زائر ایرانی طی ۱۱ روز و با بهره‌گیری از ۹ فروند هواپیما به کشور بازگردانده می‌شوند.
🔹
براساس برنامه‌ریزی‌های انجام‌شده، حجاج ایرانی از فرودگاه جده به شش…</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/439256" target="_blank">📅 18:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439255">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bornmohEY4Qa5HbG7KEsgAHN-0eZcIEyLFf_4xgjpnhsR8rlLL3qwi0WHfCd6Do5I1VcXfVbOWHFobJoDoe0w77LQNP3EJtXgfOsiNF-enXuMGWXL-ayHwvk9-ta2PIt1AVOE5DjmxdMkgVDm3mOYAqhfQqNAMLW2xa_cwNaG9cVXUnS2hM9OY_B-vXrBmqvoupnV_7-7VT3NWWGTtpBl-h9cZIkARuSvVYJrsPBA4t9tJ0IoLzmndPtA94CzBm_lGINzr3TvbXWV7wXU4qqoVJ-DBPqujuXyNF0drwsWOhzN-jQjlFkZn2sLYJ-W41CRgj7zynIOP9UgQkqzJol7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل از حضور در نمایشگاه تسلیحات اروپا محروم شد
🔹
دولت فرانسه به وزارت جنگ رژیم اسرائیل ابلاغ کرده که این رژیم نمی‌تواند هیچ مشارکت رسمی در بزرگترین نمایشگاه بین‌المللی تسلیحات اروپا داشته باشد.
🔸
فرانسه پارسال هم غرفه‌های ۴ شرکت بزرگ اسرائیلی فعال در نمایشگاه هوایی پاریس را به‌دلیل عرضۀ بمب‌ها و تسلیحات هجومی بسته بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/439255" target="_blank">📅 18:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439254">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ep6z6GcMxorz6AqfoLKGuKdIKBNnRT6Y45LWzNv9hrt7OHjOX8lTYYhGorIfucLOmVLR8FGSxKlu-tRYxc5UlOyyt2Lb5-9XVMNEJ0xIGzfT1MujH3_bFbXvYC1yUC_cZuFyC0P6j95xe2V5E0U4BE9LyjPmiPSVC-XNDG2Sy6Il-lkZ7ZqaZlUAly1qwzVwtG5w6cpBp1XGlq_qmHKkXEZf_sDEa0V9_-wWJftMgMd6st9iEPx3kMUJYLjHap4Ecb4PYX5Plr3nY6yQW-Zfs8ePlzbCNDTG25JOzVOeEKpJvGWFAfBUKQGQRNVcHDKztw7jnDKEEQWXPZBgP5xFYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو هیات‌مدیره و معاون فناوری اطلاعات تاکید کرد:
✅
«ردبانک» محصول نوآورانه بانک شهر برای ورود به نسل جدید خدمات مالی و هواداری
🔀
حسام حبیب‌اله، عضو هیات‌مدیره و معاون فناوری اطلاعات بانک شهر، از ورود رسمی «ردبانک» به بازار خدمات مالی دیجیتال خبر داد و این محصول را گامی نوآورانه در مسیر توسعه بانکداری هوشمند، یکپارچه و متناسب با سبک زندگی کاربران توصیف کرد.
🔀
به گزارش روابط عمومی بانک شهر، به گفته حبیب‌اله، صنعت بانکداری در سال‌های اخیر با تحولی جدی در انتظارات کاربران مواجه شده است؛ به‌گونه‌ای که دیگر نمی‌توان بانکداری دیجیتال را صرفاً به ارائه نسخه الکترونیکی خدمات سنتی محدود کرد. آنچه امروز اهمیت دارد، طراحی تجربه‌هایی است که در عین برخورداری از دقت، امنیت و کارآمدی، با نیازهای واقعی، الگوهای رفتاری و حتی علایق کاربران نیز هم‌راستا باشد. در همین چارچوب، بانک شهر با تکیه بر ظرفیت‌های فناورانه خود، «ردبانک» را به‌عنوان یک نئوبانک هواداری با رویکردی متفاوت طراحی و به بازار عرضه کرده است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/439254" target="_blank">📅 18:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439253">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng9S9WkXTuyyV2Yg-swi9f8dokMJVGg0WNo8i5rFpKwioelkYl1so2G2fWyZS9NPPZQCALtyjtIO6roaQy29LOp0pDOpbZMfNE5aD57Wre6p3zKr9aDq9Goche2T5rf-wcIR0YOvZn8c3VCJAy-96H_BB5iexxnaeI3jZ1Thx60D8hTpIRTXy8mb_OS584Pl1y5W2TcsUAGddbR0JbZeP0g074PzIKouL4Mvxd9Vsx0umPixCaa7X45_EYjggOL0k_VB-zGfteO7wmPZodBADd8JvsQZuQb9mITaIZUgJ_MieyJjrbWn_vGTdcWnnrv1kQVvE51RkOu2xbPBRo2hpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
با پیگیری استاندار آذربایجان شرقی؛ محدوده تردد خودروهای ارس‌پلاک گسترش یافت
🔹
با امضای تفاهم‌نامه مشترک میان استانداران آذربایجان شرقی، اردبیل، گیلان و مازندران، خودروهای دارای پلاک دائم و موقت منطقه آزاد ارس از این پس علاوه بر آذربایجان شرقی، در استان‌های اردبیل، گیلان و مازندران نیز امکان تردد خواهند داشت.
🔸
همچنین با توافق استانداران آذربایجان غربی و گلستان برای پیوستن به این تفاهم‌نامه، محدوده تردد خودروهای ارس‌پلاک به ۶ استان آذربایجان شرقی، آذربایجان غربی، اردبیل، گیلان، مازندران و گلستان گسترش می‌یابد.</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/439253" target="_blank">📅 18:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439252">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/439252" target="_blank">📅 18:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439251">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0I2ozWJd4gs2GjAzlpdwd44tp7_AWRwYjyQcCk7nkUiX20yejpjSoyAPre1PJfeqWpBbQrqfqiT_kqouknpNRrtmr2yFt3g0xt-1EOW6yTtYgPgP8BjeuGrVQwnuuXNs6rYelsY25BQRH3GRUQijnvCNDYkY-CBKnHH_4TKKaTO98Mke9hQVd-KFBjASWkPKAY5449fjTVUpxCv70m0CCCEYW1QoNUJC9C56b4csRML9VjAZjlVOdJvbeJXrf6e6rCXzqF4Zt4fDMWxoFJic4_cL0lBsH-MA1aN3n4vW2DQF8QAWJxInbcxLHVDRrwafSspWaZ2QDGPcZZtpqMwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۲ تعرض تجزیه‌طلبان به مرزهای کشور ناکام ماند
🔹
فرمانده مرزبانی فراجا: گروه‌های تکفیری و تجزیه‌طلب امسال ۸۲ بار قصد تعرض به مرزهای کشور را داشتند که همۀ این اقدامات با اقدام به موقع و قاطع مرزبانان ناکام ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/439251" target="_blank">📅 18:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439250">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTfHZ35eVfuYchYgjuj_7FW_Se2kkfW-kJa07gmyK3w8UbXVk5BrxFFFqEHmOWmwM-b2gTElzHpGSf87mPdPVerVen3WjeXCRsnpW1w6J1gy60GepkvN8Yi12fi4qYdf7qUiw9uzz-T470V3GNe-rmfpMh-oSlFD2-LkwXyaZFaTOFm9aczN_Vz1hi4Pr3Bup-mUqdVQs6CborTWptbRW3RgsDR_RUDvyIc-E_KSPPV-3mak32lTUHwfX--q9uvj6nLh7dtDnYwmEXgTnB2W8-9I1Vi30oeHrPyZh0FlHfkpmVXgTpaSCZ5B9r0U4VDNf3rj4WUI9rN9bjoPIs5NvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اول رئیس‌جمهور: فرماندهی رهبر معظم انقلاب و وفاداری دکتر پزشکیان به نظام بی‌نظیر است
🔹
فرماندهی مقتدرانه و حکیمانه آیت‌الله سید مجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در شرایط جنگی، ضامن اقتدار، امنیت و آیندۀ روشن ایران است.
🔹
رئیس‌جمهور نگاه خالصانه، وفادارانه و بسیار قوی نسبت به انقلاب، نظام و کشور دارد که انصافا این نگاه بی‌نظیر است. مواضع صریح و عملکرد او در دفاع از کشور مایه افتخار است.
@Farsna</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/439250" target="_blank">📅 18:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439249">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pK7tKLcvReU2Cz6TG1AW6F_8iXpomTwyDhrbuwzDZpuH7klTr4KnlQKmz9oPk9sZoZQrLbSrDbEQgDSi3wUZ4sUobW6lYiu02tKmtsWNPXBTzoiY9-dFsXKTb0V1aY5VDeJyQJiugvYgySu-5iAPGjmda4thaNJaWv0QzViszGMBW5uzyfEYonVC0hQuvxm1aDIaIJHnaM8aIBnMul-8NyTlATe4i850u8MuLTrvYu0lEdCLfyTcptBY9hY6R4mtc_C0_072UBYfbEFyw1lI8HiSKO6dpr_n7Btj1JNuRtVv5vrWdf6s5QQy_ZUqaueuw6-GEnt9hy3PyfZUBE0euQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان حملات اسرائیل به خاک لبنان را محکوم کرد
🔹
وزارت خارجهٔ عربستان ضمن محکوم‌کردن نفوذ نظامیان صهیونیست در خاک لبنان، خواهان مسئولیت‌پذیری جامعهٔ جهانی برای توقف این تجاوزات شد.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/439249" target="_blank">📅 18:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439248">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88863fe00.mp4?token=trQYJ52CLBahLZcl-ro2WexRg6doZGxCRgE0cfJavqJ3cpgRXrZsiA3qihU9yLJ7ob55LSMtFQ2MT_NahyYMI4tBg_OX1Zx9uVnndhxPNKjbhO8s9e9pYoZPAr65TaizqPEg-xVzVSKIAzrsQ78kMjLNCrIkCyNTYj2-0B5VVjPAijL1GhnT3Lvme4iP2EMgIgzyliZyoz9a3ArBmLB-geJaTbrVCHoY2Zj0XtFBv-2ABAUUpWqrCY-Y0-50dwbC7ZjE-8cYvuAZBH_zeuzvT5wbMLLenot1kTNbyw4_U8vwjLo8zvkOvoFf7KNwpAraTQ1bn85cTM8caVskK0qFVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88863fe00.mp4?token=trQYJ52CLBahLZcl-ro2WexRg6doZGxCRgE0cfJavqJ3cpgRXrZsiA3qihU9yLJ7ob55LSMtFQ2MT_NahyYMI4tBg_OX1Zx9uVnndhxPNKjbhO8s9e9pYoZPAr65TaizqPEg-xVzVSKIAzrsQ78kMjLNCrIkCyNTYj2-0B5VVjPAijL1GhnT3Lvme4iP2EMgIgzyliZyoz9a3ArBmLB-geJaTbrVCHoY2Zj0XtFBv-2ABAUUpWqrCY-Y0-50dwbC7ZjE-8cYvuAZBH_zeuzvT5wbMLLenot1kTNbyw4_U8vwjLo8zvkOvoFf7KNwpAraTQ1bn85cTM8caVskK0qFVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد مردمی برگزاری مهمانی کیلومتری غدیر: مراسم تشییع پیکر رهبر شهید انقلاب در بازۀ عید غدیر نیست.  @Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/439248" target="_blank">📅 18:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439243">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کشته‌شدن یک نظامی ارتش انگلیس در شمال عراق
🔹
وزارت دفاع انگلیس مدعی شد که یک نظامی این کشور روز گذشته در یک حادثهٔ آموزشی در شمال عراق جان خود را از دست داده است.
🔸
وزارت دفاع انگلیس جزئیات بیشتری از دلایل حضور نظامیان این کشور در منطقهٔ کردستان عراق و دلیل کشته‌شدن وی در این منطقه ارائه نکرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/439243" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439242">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363a2fe1bc.mp4?token=N7fI2HOGmQ2AG4AgNpP__529_G03LT1EU-qJGGSXt1Kn9axHx7FtJ7frZC2zQ2MCkjoXgfvz54SuwFJKRvk4eZZ4LEGlc47WFTzviOALd5A8v3ieBl7xRM_ykaqb2Xk31UEpNiAby9h5YGkeOvJ65sgttYpSxG_VdXjv4UpigAYHVmhbwHrpgg76a7lVqRsSmzM5q4klAGOdC-g_NYIKiDLnTRw0aEAd89mkLZQdNwViHCwRpuMYMBqdz8orDBsTxUKmhPwIOC1relpg1hi_VAMjrKm_nTfo2CoXd8CMzVd23JkHGGnrOD2IE7Z4AxhqXL3-YhSXMiXSI0F6D-Hhbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363a2fe1bc.mp4?token=N7fI2HOGmQ2AG4AgNpP__529_G03LT1EU-qJGGSXt1Kn9axHx7FtJ7frZC2zQ2MCkjoXgfvz54SuwFJKRvk4eZZ4LEGlc47WFTzviOALd5A8v3ieBl7xRM_ykaqb2Xk31UEpNiAby9h5YGkeOvJ65sgttYpSxG_VdXjv4UpigAYHVmhbwHrpgg76a7lVqRsSmzM5q4klAGOdC-g_NYIKiDLnTRw0aEAd89mkLZQdNwViHCwRpuMYMBqdz8orDBsTxUKmhPwIOC1relpg1hi_VAMjrKm_nTfo2CoXd8CMzVd23JkHGGnrOD2IE7Z4AxhqXL3-YhSXMiXSI0F6D-Hhbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد مردمی برگزاری مهمانی کیلومتری غدیر: رهبر شهید چندین‌بار در سال پیگیر برگزاری مهمانی غدیر بودند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/439242" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439241">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rm8Bn_olzDrKXX6PZPaV70jDxGYwTSdhZG-guUy1kNVBKvx01iwI9Wr3cvkNCN3UA2rKYDPtDNCWRVysAmw6hUj9griDpDEne7tBEv4Qxa1_Lq_6yCDljXKPpV_sUoMFUyHEI1jVM7mnPrw2VjBFYR4h0fNoUDs14m6EJ-2DmXHCqz4mypRi2wADBL8GmJXoMXqJEit4VhplekJyqkm1wPvI6mNKjya_I7poPFX1Zk5yi427S5OD3nsXPht7WY0_ABFim-S4fQiAtEYEpn0BMaqLMYj-F16hFQwkST8VwRK4zS6mx8arLFMLpi_yxvhwVJuwahDx2G2pjqDl0tnSVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل برای ضاحیه بیروت هشدار تخلیه صادر کرد
🔹
ارتش رژیم صهیونیستی در فرار رو به جلو، مدعی شده اگر حزب‌الله به حملات خود ادامه دهد، صهیونیست‌ها هم ضاحیه بیروت را بمباران خواهند کرد.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/439241" target="_blank">📅 18:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439240">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46161d95d5.mp4?token=N7k2ptVZXWfWemYNjmxycJwiIKIdOrx8YCCYkGnitnvxjw9KsJCz6yPomY-uIXVZSUDSSOWNJcYRKanZS82ebZD_xFv2WtvVm1mG797X1taRBUWDAfIBOnQ1Q5AEsG7twqnmEBmDlHPn2u0V_njKuiYkvsFVMVPTTv9vn2Fn6bvewYPcm2HgsHHhefDcnIDmSt-0069_7wP3V2vCgoxfljV4zvGIk6gSn78Or-82lPWyFSMO4aIoT-mjw40AVgWvl9waiaMn64pizQSE4Pn4OhVNGQA7rs5pr1OYz8CuaJ508LF2REu8Nbk_6bkxvYoomU6yd8G7jMeAz49kSOBaBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46161d95d5.mp4?token=N7k2ptVZXWfWemYNjmxycJwiIKIdOrx8YCCYkGnitnvxjw9KsJCz6yPomY-uIXVZSUDSSOWNJcYRKanZS82ebZD_xFv2WtvVm1mG797X1taRBUWDAfIBOnQ1Q5AEsG7twqnmEBmDlHPn2u0V_njKuiYkvsFVMVPTTv9vn2Fn6bvewYPcm2HgsHHhefDcnIDmSt-0069_7wP3V2vCgoxfljV4zvGIk6gSn78Or-82lPWyFSMO4aIoT-mjw40AVgWvl9waiaMn64pizQSE4Pn4OhVNGQA7rs5pr1OYz8CuaJ508LF2REu8Nbk_6bkxvYoomU6yd8G7jMeAz49kSOBaBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای تذکر رهبر شهید به تیم حفاظت دربارۀ رعایت بیت‌المال
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/439240" target="_blank">📅 17:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439239">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ارتش اسرائیل برای ضاحیه بیروت هشدار تخلیه صادر کرد
🔹
ارتش رژیم صهیونیستی در فرار رو به جلو، مدعی شده اگر حزب‌الله به حملات خود ادامه دهد، صهیونیست‌ها هم ضاحیه بیروت را بمباران خواهند کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/439239" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439238">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1383d6bb26.mp4?token=ADCpq8dITsxp02Ns9vJO0kYba3K2ZQ4tW2d3foEI9ZIj6mtne9ckjKPumRMZ7Zd1Td4AMXp2c3_OjkUt6BHz4Up1Sb9XwBNZFiDLmhemBtht02cnwC1oaChf374YMlAco2lELb8WWJHYN0Ha1wu3F2z-bW3wcxIUuxfBjh_xlGQ6kcQt9-doqIwgoANAliEFS6Als6ZKQnjkcZbbeDRiLcf5qcuKKROVHM_Iqs0KyZt0FpCIPklOenfs0TOta8zCZ4R_S6z0LSrwQYT4_2U3Rg4aOpacJwo8DDB7OP0hTmMHVkHbwgGZ9-VvNdTcDKvsuXbSDAKFFew9GNvzRBzfgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1383d6bb26.mp4?token=ADCpq8dITsxp02Ns9vJO0kYba3K2ZQ4tW2d3foEI9ZIj6mtne9ckjKPumRMZ7Zd1Td4AMXp2c3_OjkUt6BHz4Up1Sb9XwBNZFiDLmhemBtht02cnwC1oaChf374YMlAco2lELb8WWJHYN0Ha1wu3F2z-bW3wcxIUuxfBjh_xlGQ6kcQt9-doqIwgoANAliEFS6Als6ZKQnjkcZbbeDRiLcf5qcuKKROVHM_Iqs0KyZt0FpCIPklOenfs0TOta8zCZ4R_S6z0LSrwQYT4_2U3Rg4aOpacJwo8DDB7OP0hTmMHVkHbwgGZ9-VvNdTcDKvsuXbSDAKFFew9GNvzRBzfgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد مردمی برگزاری مهمانی کیلومتری غدیر: رهبر شهید چندین‌بار در سال پیگیر برگزاری مهمانی غدیر بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/439238" target="_blank">📅 17:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439237">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07cc6e033.mp4?token=PwCwpAEGpFXEx49xvWGvdHiGheUDDZuqZ9tJkU4jklFcW_6aA7Rl3w6M51rOaTZ8fJFT6NrMU8OFC6uKn80m14jHV_EbdImAOmtEAFXqAxIs7FxpnQ5dAuykRaD_0YvG5jj-ZRX1WlkVyobxacxTYGHbB6ZULFOdNcxLyJMeVXsndUXZCkPCsklQHi0E5A-QAfbkslcLZ9UQeXQ53JwWmsPpWj3GSwe-ILtlN-0ZM5_8TO0cJBj3jxuqv67nhNhyQuPoYWS2hUwhIwiY-pkP-Z9I0LbCWutCowVDdYpVjNO-r0YoWBG-25A1aOg1h3spQ-ES54O6SqJxJOH5H8z1fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07cc6e033.mp4?token=PwCwpAEGpFXEx49xvWGvdHiGheUDDZuqZ9tJkU4jklFcW_6aA7Rl3w6M51rOaTZ8fJFT6NrMU8OFC6uKn80m14jHV_EbdImAOmtEAFXqAxIs7FxpnQ5dAuykRaD_0YvG5jj-ZRX1WlkVyobxacxTYGHbB6ZULFOdNcxLyJMeVXsndUXZCkPCsklQHi0E5A-QAfbkslcLZ9UQeXQ53JwWmsPpWj3GSwe-ILtlN-0ZM5_8TO0cJBj3jxuqv67nhNhyQuPoYWS2hUwhIwiY-pkP-Z9I0LbCWutCowVDdYpVjNO-r0YoWBG-25A1aOg1h3spQ-ES54O6SqJxJOH5H8z1fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرود پهپاد حزب‌الله روی سر سربازان صهیونیست
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/439237" target="_blank">📅 17:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439236">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e10313c68.mp4?token=uNCYamk7y1ojwJRZdi1E35d5bXJ75MhdlclUzmwN9pqHcpFX0Yk8TwMZi8-V-FmanbSU_ZNE77FX7ToI_7QSXlm6OYXcosl-oX36vnCcu7OmhNXtvKFC9AI7kzwWX4ZBgjA7r9PNU7EPM8mbjYfOAggZs8b-azaMrPJyGs2K8u6lP1may60r0BDESFTV_lj0WhNLbL3KsC7nzHlO5xqLZY2D6CvDRFEEu4RLxuewzE_Om7SXU9nRPlg8fmyL3r0JeGISpJsUSi5E1r6yCKn48dFYLcmLwusDrJsCGMsTPziKne_IEJY3nEhqb1Zhsh2OvluwJJt1aMaLlwYiEpf_pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e10313c68.mp4?token=uNCYamk7y1ojwJRZdi1E35d5bXJ75MhdlclUzmwN9pqHcpFX0Yk8TwMZi8-V-FmanbSU_ZNE77FX7ToI_7QSXlm6OYXcosl-oX36vnCcu7OmhNXtvKFC9AI7kzwWX4ZBgjA7r9PNU7EPM8mbjYfOAggZs8b-azaMrPJyGs2K8u6lP1may60r0BDESFTV_lj0WhNLbL3KsC7nzHlO5xqLZY2D6CvDRFEEu4RLxuewzE_Om7SXU9nRPlg8fmyL3r0JeGISpJsUSi5E1r6yCKn48dFYLcmLwusDrJsCGMsTPziKne_IEJY3nEhqb1Zhsh2OvluwJJt1aMaLlwYiEpf_pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارخانه تولید مواد آتش‌بازی، صحنۀ آتش‌بازی شد
🔹
منطقۀ ساحلی سالینا در کشور اروپایی مالت امروز صبح بر اثر انفجاری مهیب در یک کارخانه تولید مواد آتش‌بازی لرزید؛ انفجاری که ستون‌های متراکم دود را به آسمان فرستاد و به املاک،‌ ساختمان‌های اطراف و خودروها خسارت وارد کرد.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/439236" target="_blank">📅 17:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439233">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sm1IC4yLg8tyjVL7Y8XZTbVW8kW8ETWw6RAL9fvajq6EKX4MSBYg9cRfXgR37W5rCl9xx68t88seDv9FVTwACTAZwZVLMlWCjb-TQfYayp9iAbEALPe-sR7MmaCTJQzFUCKHCsx6VMUFVWEKlCN1zt1zQKOCzckeATzdtKui4gvquQJDbKbdtjVvaNDDdN8ngP77qQC7v6RKl2m8xiOkKKGlAY3q1uIR9iB8Hsm_A-t4Nh_cvDLGimC8yW5y8cNW_6HzQzIXWKAfVwWKG64lIxCft7WhULfugTteIB_bmTeBQPR4FP40c6QMCZxQfMgAP0Op_-xOxdfR1NZQpVWYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRrVPql7Zrqdwcx4SDdz5DzgFNEsxnJ4pQUhe6bSrVpljnPYXkVZ4ZS4vaRhzSkMYtlsnrtb0ESgY1KhXWUkTSZkgugTG5nMNW6Mm0AnR3vO0lTbjSccdIzg9VUwz14dAqUb1XbUYRtAhCESEu2HTdNRPCrsNqETYUrZyFkLrZL3nA3mMOcoHxtljHkKeATQoYzkO4vXUL8z7XbOYqMbwUt-H1AOMWjnf7eOlwJMtH5Pr4tEtHgHKK-5gTINZLWj6UwA8LupVDzL05tKTJbwdCTNGoMh9W6yTEc8HXH-TGnnwNYnpqCqieGVLcnIv9okkUcf63mY568AGo6UkESa4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvHysmqLbnMZ2xpNMISLTg5HPmZ44zqYLZ9gRF3buQ_P-lla6unLXPOziFsEpHKgWGL9iAnuGpWWnUkNR0HIfn32D-WZ3b3icD_dZc7I655nCO8ZY03i3a4ub6NwPSLwIDMuCqdoJFqGvkgzX5Zy3LRytMldTSG9-YckkPTmkwPArEPNk17B9kiAemEI8CzjwbFsptpcTnqoe07HwS5l2FJlytgVHbzezEVoB78ll3OJFSDAKolrJoZRM1Ofudyub1oi5pUCwl8sv8vMmqjdo5ZMg1wd4bv8caWf6n5a1HMLN0fCorVLeVhrqoEAXMUl81Hyf_kR26pK-IhtfaUGVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
ابلاغ پیام رهبر انقلاب به خانوادۀ شهدای مدرسۀ میناب
🔹
حجت‌الاسلام وکیل‌پور، نمایندۀ ویژه رهبر معظم انقلاب، در سفر به شرق هرمزگان با خانواده‌های شهدای مدرسۀ شجرۀ طیبه میناب دیدار و گفت‌وگو کرد.
🔹
در این دیدار، پیام و سلام رهبر انقلاب به خانواده‌های معظم شهدا…</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/439233" target="_blank">📅 17:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439232">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8251471bb7.mp4?token=ak7wLGix58YS6fzTS7fqV8citgpcNpJfflgiztVJlRoxy91oCbcy_EgfLCHqxN8ARrOmHX_eizjyHHtod_KUzYH4WmNiqDreooGaZyi20wjkBHa2M3J4pW3swbUVtBWGvA4ia1jU2-H92DvZgjTZC6Xn2vn3fj-Ht0wru29-KJkB3abtUg-_Q8HniPPvPUWLs3cOpXk2gP6AO-HBSWcJeFoi18w6MDao6R52to_WTWw3D0BLPOqx5L3NKxdcf5i-ZWczyEpUuGrV-NBs3E2N9-ijOjyGB6Eo5CK7DjUhS8tysNZg2mdENrtJNFVgFx-tnMfW4byxuss-j4YjIQFw9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8251471bb7.mp4?token=ak7wLGix58YS6fzTS7fqV8citgpcNpJfflgiztVJlRoxy91oCbcy_EgfLCHqxN8ARrOmHX_eizjyHHtod_KUzYH4WmNiqDreooGaZyi20wjkBHa2M3J4pW3swbUVtBWGvA4ia1jU2-H92DvZgjTZC6Xn2vn3fj-Ht0wru29-KJkB3abtUg-_Q8HniPPvPUWLs3cOpXk2gP6AO-HBSWcJeFoi18w6MDao6R52to_WTWw3D0BLPOqx5L3NKxdcf5i-ZWczyEpUuGrV-NBs3E2N9-ijOjyGB6Eo5CK7DjUhS8tysNZg2mdENrtJNFVgFx-tnMfW4byxuss-j4YjIQFw9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقوع انفجار در نفتکشی در آب‌های عراق
🔹
العربیه نوشته که یک نفتکش غول‌پیکر با پرچم پاناما در آب‌های سرزمینی عراق دچار انفجار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/439232" target="_blank">📅 17:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439231">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7422b8693.mp4?token=NVVk17TaTnq0Mh2xIAlH2VKUIlnA9r2jb0t_Fq2WgHm6knFWbsSVwlsfYgaogCol87qt7Z9CG7ZZqY81s-E5KEs6_6kEO8tBjvppZUetqSj2z2twSze-HHfVg6GGgyoacnBOZvdMDS72MOiKFGKM_AiycnYuy6TJ6cY1hsaoii4WS0jkIqQjfe40rO3n_iUowZhatndJwtMPyUAJn7v06dxKuQz-7s6SdJMgq8oyP4U14qUG_RwEIqZTys5bytJ1HZvHzvNbCdMUFeTVHun79YRTPAtrDpuob-9WOHBgo7RaWj5DCaGg0sf9nhca27vVCf-vezDJnQOCSwvrJdYMgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7422b8693.mp4?token=NVVk17TaTnq0Mh2xIAlH2VKUIlnA9r2jb0t_Fq2WgHm6knFWbsSVwlsfYgaogCol87qt7Z9CG7ZZqY81s-E5KEs6_6kEO8tBjvppZUetqSj2z2twSze-HHfVg6GGgyoacnBOZvdMDS72MOiKFGKM_AiycnYuy6TJ6cY1hsaoii4WS0jkIqQjfe40rO3n_iUowZhatndJwtMPyUAJn7v06dxKuQz-7s6SdJMgq8oyP4U14qUG_RwEIqZTys5bytJ1HZvHzvNbCdMUFeTVHun79YRTPAtrDpuob-9WOHBgo7RaWj5DCaGg0sf9nhca27vVCf-vezDJnQOCSwvrJdYMgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تسلیم اعتبارنامهٔ هماهنگ‌کنندهٔ مقیم سازمان ملل به عراقچی
🔹
کریستین وی‌گاند، هماهنگ‌کنندهٔ مقیم سازمان ملل متحد در ایران عصر امروز و در آغاز ماموریت خود، با وزیر خارجه دیدار و اعتبارنامهٔ خود را تسلیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/439231" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439230">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5242d357.mp4?token=o0XK9cl7457f4UsztaJtxXM6tALq6nOyop72s18B7twY5Oertyw-PkP5L8fDw-VAutTYDLLBRspgQVNLdCpWKwtM_B4W5krNsl6cC-nGpWrexTyosmLwb72hqCB89XLLWEZZwSTFiLzg2wUNqBdpD0oGmqpGz62MxWLhKBg0xO6XkJ3cOFgmZDEDSCBWqUIHoOzu9TuV-LnRFfO-3bcZB4d_xNQ-C98nyIEysUnO61CjruZ7gPlnQ-BG0bPoJ_1nRROyUXN9m81lOl8Dp_-efbuxLx-iA2hrybxkF-TqWU1j96NHkxVLAolUgiQRwyH0XMZf6fVNhzTg3VotNbJusg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5242d357.mp4?token=o0XK9cl7457f4UsztaJtxXM6tALq6nOyop72s18B7twY5Oertyw-PkP5L8fDw-VAutTYDLLBRspgQVNLdCpWKwtM_B4W5krNsl6cC-nGpWrexTyosmLwb72hqCB89XLLWEZZwSTFiLzg2wUNqBdpD0oGmqpGz62MxWLhKBg0xO6XkJ3cOFgmZDEDSCBWqUIHoOzu9TuV-LnRFfO-3bcZB4d_xNQ-C98nyIEysUnO61CjruZ7gPlnQ-BG0bPoJ_1nRROyUXN9m81lOl8Dp_-efbuxLx-iA2hrybxkF-TqWU1j96NHkxVLAolUgiQRwyH0XMZf6fVNhzTg3VotNbJusg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میراث عظیمی که امام هادی(ع) به ما دادند
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/439230" target="_blank">📅 17:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439229">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
هشدارهای حملهٔ هوایی در چند منطقهٔ شمال فلسطین اشغالی فعال شد  @Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/439229" target="_blank">📅 16:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439228">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d738f7e192.mp4?token=QT3czoN0XB1JpOD99ix9n6rRSN31V0ydF5q2oG1hp7Nf10jHmTNnaeNzufvH7Yo29G8aHZZNgx7kXyhos5LOUBl1ITf1O_PGOrbiu33B4pp5ErCyVovzOUqNEJ6SDPcLBhh0G48P5xJhfUYa4zT-Vu2BbXKez-46y1h_dyPQEhZLdYIFPOWHihm88pIr0AXM0NE_KUhLkUtoBD8lc7zZ57AfxoK_Q8s20tyYlGFEf_Hu4K1gnnIV3M9M-4fQdXE734YDL5l4rXA4SyX06JGydl0ZJD3dzWBlATgu35igvxMBvNZC2Loj2lvUQG998U_8lm9YsVdRTODf24exLHoAJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d738f7e192.mp4?token=QT3czoN0XB1JpOD99ix9n6rRSN31V0ydF5q2oG1hp7Nf10jHmTNnaeNzufvH7Yo29G8aHZZNgx7kXyhos5LOUBl1ITf1O_PGOrbiu33B4pp5ErCyVovzOUqNEJ6SDPcLBhh0G48P5xJhfUYa4zT-Vu2BbXKez-46y1h_dyPQEhZLdYIFPOWHihm88pIr0AXM0NE_KUhLkUtoBD8lc7zZ57AfxoK_Q8s20tyYlGFEf_Hu4K1gnnIV3M9M-4fQdXE734YDL5l4rXA4SyX06JGydl0ZJD3dzWBlATgu35igvxMBvNZC2Loj2lvUQG998U_8lm9YsVdRTODf24exLHoAJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات آخرین پیشنهاد ارسالی آمریکا به ایران
🔹
آجرلو عضو تیم رسانه‌ای هیئت مذاکره‌کننده: در مرحلۀ نخست مذاکرات، آمریکایی‌ها خواستار انتقال مواد هسته‌ای ایران به آمریکا بودند که این درخواست پذیرفته نشد.
🔹
در آخرین ویرایش‌ متنی که آمریکا ارسال کرده، دیگر بحث…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/439228" target="_blank">📅 16:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439227">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTK4qxi5ZsNcw7vUYxX9-d1b2DZK1VO4TYwNT3vW5HmhKiDVuWARjMKMHYlRQTirG1jrPWJMAwytaCIHGe2bVjJmr9sQfyF7B2kHKS0yUaViaqrEjIUGBSgAo2w0fNK1BbZpzF_wtQKAAk_sUxsqNiCB1NL1GsfGduNt6Jy9IsyAqLR4dfgWA4h-TaakAftJDZdwRqCM3ANAlMXdEEsjVUO2MOWvMaDiG6O6hnXhrnD-4ZDCSy_07kd8ypLmGX_CECYYlL6IwPv7IeCxDvADEj9vzKr1vRc9IqWsX02cwL5kUlVufoqQda38q31NxLKEc1bf9PPsdOyZI7wXRU9uRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدارهای حملهٔ هوایی در چند منطقهٔ شمال فلسطین اشغالی فعال شد
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/439227" target="_blank">📅 16:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439226">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59508e038.mp4?token=QYSsNNY2njZRWdPZ4EzC9JDTTDbViWu5ZmjdHO0RWiT6Yuoko0q2ErqbMf29MDDVDSdWVhRncV7ZVNj9jZxQrMguRnsUkEeIfB6ErwbkQnsclFP6kWVzQ64pTMctDHjNTiAJheao622-NpJ3cA85jum1UY8oGuJpAFVIXmAQtk4ktNFOrtYuale2pbMyyPQfU4dHYZJ1NAQY6DHN5RnDeJjhz9gZW5O5QVkVKM8bMvjJ7iIBup_WQg9glWLPQmVmT6Vxq-W1GLLljyBAITJ3J0eevtPajf6Mf7mCafWabGh3c2BZJURE94BcBZ-rm-sxsdMfuhg9GRfZl0LzFtmCRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59508e038.mp4?token=QYSsNNY2njZRWdPZ4EzC9JDTTDbViWu5ZmjdHO0RWiT6Yuoko0q2ErqbMf29MDDVDSdWVhRncV7ZVNj9jZxQrMguRnsUkEeIfB6ErwbkQnsclFP6kWVzQ64pTMctDHjNTiAJheao622-NpJ3cA85jum1UY8oGuJpAFVIXmAQtk4ktNFOrtYuale2pbMyyPQfU4dHYZJ1NAQY6DHN5RnDeJjhz9gZW5O5QVkVKM8bMvjJ7iIBup_WQg9glWLPQmVmT6Vxq-W1GLLljyBAITJ3J0eevtPajf6Mf7mCafWabGh3c2BZJURE94BcBZ-rm-sxsdMfuhg9GRfZl0LzFtmCRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور نمایندهٔ رهبر معظم انقلاب در جمع رزمندگان در سیریک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/439226" target="_blank">📅 16:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439225">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پزشکیان: تلاش می‌کنیم عبور کشتی‌های ژاپنی با سهولت انجام شود
🔹
رئیس‌جمهور در گفت‌وگو تلفنی با نخست‌وزیر ژاپن: ایران همواره دیپلماسی را مؤثرترین راهکار برای حل مسائل موجود دانسته، اما متأسفانه برخی طرف‌ها از جمله آمریکا با عدول از تعهدات خود و همچنین اقدامات…</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/439225" target="_blank">📅 16:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439224">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پزشکیان: تلاش می‌کنیم عبور کشتی‌های ژاپنی با سهولت انجام شود
🔹
رئیس‌جمهور در گفت‌وگو تلفنی با نخست‌وزیر ژاپن: ایران همواره دیپلماسی را مؤثرترین راهکار برای حل مسائل موجود دانسته، اما متأسفانه برخی طرف‌ها از جمله آمریکا با عدول از تعهدات خود و همچنین اقدامات بی‌ثبات‌کننده رژیم صهیونیستی، روندهای دیپلماتیک را با چالش مواجه کرده‌اند.
🔹
جمهوری اسلامی ایران آمادگی کامل برای تسهیل عبور و مرور دریایی را دارد. مشکل اصلی ناشی از محدودیت‌ها و موانعی است که از سوی آمریکا علیه کشتیرانی و تجارت ایران اعمال شده است.
🔹
تلاش خواهیم کرد مسیر عبور کشتی‌های ژاپنی بدون مشکل و با سهولت بیشتری فراهم شود.
🔹
ایران هر اقدامی را که در توان داشته باشد برای عادی‌سازی روند تردد دریایی در تنگه هرمز و حفظ ثبات و امنیت این گذرگاه راهبردی انجام خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/439224" target="_blank">📅 16:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439223">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1023c192.mp4?token=sVYH4UmHHTRXZFNh57sRjQt_U8mcNl1NG_Tb1echRv4NOSUq0Y9i6_gxqm9sMYxm2JHpxvKp1x_WufXbAWY7CEvPwi2mLw39_GFnG-g-DDOGC5Y_uD1tn373SI2UdAbyG_aC4KnoGrGKm1d0GLPyN2t-Xm-xDiiH_-HhqdK6PMxvMAETEDQ4-C8pkPqJbjOCANbhpIcuVKNJq4EDD2y2uUa7VPk1sm_O42_s5bpTw8YwLA_dPHjzuc7_2Sj6Ttkm9I7cjJfPETqEd1ihXwgHG2KvObmgJHHeg4OF06jgyQhTx6VXvxhFoW7haRSF5RTUy7CVhcq4S05px5Z5bdUAYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1023c192.mp4?token=sVYH4UmHHTRXZFNh57sRjQt_U8mcNl1NG_Tb1echRv4NOSUq0Y9i6_gxqm9sMYxm2JHpxvKp1x_WufXbAWY7CEvPwi2mLw39_GFnG-g-DDOGC5Y_uD1tn373SI2UdAbyG_aC4KnoGrGKm1d0GLPyN2t-Xm-xDiiH_-HhqdK6PMxvMAETEDQ4-C8pkPqJbjOCANbhpIcuVKNJq4EDD2y2uUa7VPk1sm_O42_s5bpTw8YwLA_dPHjzuc7_2Sj6Ttkm9I7cjJfPETqEd1ihXwgHG2KvObmgJHHeg4OF06jgyQhTx6VXvxhFoW7haRSF5RTUy7CVhcq4S05px5Z5bdUAYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف علی یونسی به هواداری منافقین؛ روایت‌سازی رسانه‌های معاند فروریخت
🔹
علی یونسی در نامه‌ای که از زندان نوشته و در کانال گروهک تروریستی منافقین نیز منتشر شده، صراحتاً خود را «هوادار سازمان مجاهدین» معرفی کرد.
🔹
این درحالی است که رسانه‌های معاند طی سال‌های…</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/439223" target="_blank">📅 16:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439222">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNBMm-_n3R1wC0zlCQGnOWBvDzlI5Ne3Q-taJbwq2VTnGr5TQcjOIUmwUQQV-GQTx_AVTe7JrUBjN-CyDQCRorarUsU0hIh2litTu9kV4nsBjKT7KL_bl_XjUmH3hjjQFkmXV3Ng8T52wA6VpC4mYsBHVufRxDnY739pgPAM91lIbPC3fh-p0lrzyhH1juiBekMQRe8bNHnWUjv1leZOfCVeycsNd6TiavojvseR9M1AOgH-NKjYgTKcFQpLAUZfdIL3c63hF46Bh6nqJrV0bywz1PDslHM5pIF6JVvzprtCxyPJu68gxLk1Ch02aVFDn97YNx_9XLQBty5OCJR2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: ایران پایگاه آمریکا در کویت را هدف قرار داد
🔹
بعد از آن که سپاه پاسداران انقلاب اسلامی از پاسخ موشکی موفق امروز به تجاوز جدید نیروهای آمریکایی در جنوب ایران خبر داد، فرماندهی مرکزی ارتش آمریکا در بیانیه‌ای اعلام کرد: شب گذشته در ساعت ۱۱ شب به وقت شرق آمریکا (صبح به وقت تهران)، نیروهای ایالات متحده با موفقیت دو موشک بالستیک ایرانی را که نیروهای آمریکایی مستقر در کویت را هدف قرار داده بودند، رهگیری و منهدم کردند.
🔹
سنتکام همچنین ادعا کرد که هیچ‌یک از نیروهای آمریکایی در جریان این حمله آسیب ندیدند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/439222" target="_blank">📅 16:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439221">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c55155dbee.mp4?token=bu1jXnwRyvuubA51tR7p32EFI0a7hMCJhTf5vmeoq8o8CaOuZfB5V3QmeblUHZJpjKB4xCtSTVyAgJocMc36n4k8mwhpxQQtP0o_VomeDk_jsiuZ6v-sOWGx9EnqwgtzJaYNlEgWf3Fy6A4IfFwBXUTnm8CtVfWFePYqWefZVKUaQ5Yjc9kfeuZpLXDS9WaUmU6emVd9y2vvjTpDHFsa7LCGh5SHoNkZNsw3Bsy4x63UH8OAfh0f6IFqrv2_uClP93t7G42G3r3-OflBcmYtJaEEvTxYievyQCfct78H-LUvgJ1LfgK7UUNnyqAF2zuL4tHyvZfSTgr6YSUyeAFXxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c55155dbee.mp4?token=bu1jXnwRyvuubA51tR7p32EFI0a7hMCJhTf5vmeoq8o8CaOuZfB5V3QmeblUHZJpjKB4xCtSTVyAgJocMc36n4k8mwhpxQQtP0o_VomeDk_jsiuZ6v-sOWGx9EnqwgtzJaYNlEgWf3Fy6A4IfFwBXUTnm8CtVfWFePYqWefZVKUaQ5Yjc9kfeuZpLXDS9WaUmU6emVd9y2vvjTpDHFsa7LCGh5SHoNkZNsw3Bsy4x63UH8OAfh0f6IFqrv2_uClP93t7G42G3r3-OflBcmYtJaEEvTxYievyQCfct78H-LUvgJ1LfgK7UUNnyqAF2zuL4tHyvZfSTgr6YSUyeAFXxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌
🔴
حزب‌الله: یک پایگاه زیرزمینی متعلق به ارتش رژیم صهیونیستی در شهر طبریه اشغالی با شلیک راکت هدف قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/439221" target="_blank">📅 16:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439220">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42ebba9900.mp4?token=l-UNo08mbYf8mWU_c5jeei7Umj-lWnEkwaoyBT1E32vqcob0wqmyBvhmPckMXCKkfJ9AIsu2KhwvBiFL3MHkDYyAbZ66cMH8bF-EymdLAx9uXxEGIaAny36z7z_AxIlSg0667OfupqZkhvZYtKSXBNQM7AD0gnbICZvTbL2e1pYgCwacLYX2IjfWZYhrUQc6O0mrMZKv9HeLKUfNx0FoLdV678XkaSHAZXkPH5krBU_hDljZtRFoDTLXybPmIqhZXWE8DAGDOcHqXpzqpqrB1kyxaY3qC7cDS2MdK7LxwTdzdT4s7aBEUakhM_XDvPFADomi36Caof_KcOcIyi5tcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42ebba9900.mp4?token=l-UNo08mbYf8mWU_c5jeei7Umj-lWnEkwaoyBT1E32vqcob0wqmyBvhmPckMXCKkfJ9AIsu2KhwvBiFL3MHkDYyAbZ66cMH8bF-EymdLAx9uXxEGIaAny36z7z_AxIlSg0667OfupqZkhvZYtKSXBNQM7AD0gnbICZvTbL2e1pYgCwacLYX2IjfWZYhrUQc6O0mrMZKv9HeLKUfNx0FoLdV678XkaSHAZXkPH5krBU_hDljZtRFoDTLXybPmIqhZXWE8DAGDOcHqXpzqpqrB1kyxaY3qC7cDS2MdK7LxwTdzdT4s7aBEUakhM_XDvPFADomi36Caof_KcOcIyi5tcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگو با کوچک‌ترین عضو گروهِ سرود میدان ولیعصر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/439220" target="_blank">📅 16:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439213">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flM0A3OhcvHva8WXKh9uSHSXLftBrZdzBU07Vlsk5zWBDhKwV-DqwoiQoEVCleO78tgpJ7mR2iRoJjTw0PEbbg1rNwZIT0FO3OWOJ0L_Uo9F5HBLZB6XmZqybpWL9Lp5y3L0QNkV42toalat1CJ_a1dKAtDbuOZ4RW8SRC0FPWxyEAQtCqmvVKofotkg5ZfCPbMGAkYUvugqHnGpYr5uw7ZCWNmwv48ICO_plOVvqyD2FkX33ssVIY-h3HpVtBEY8g3dJtDjiUsFfi-GCVCq54P_ZIS4Hxo6yas8rBD9jFrFruv-vU5lZvhoTEGA-8wVcSQG5V04ssJ2L8ZGX4yfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfqIZUp3_ttrz1iJEqV8i4sXwEECyWyMD8UYmOPeC_uT8usFrHfDNVr70jxqpNH7g43TL2IX7P32Ro3pTVrm-Xb8MHI4wcFbS6i-hAAD9kTN3GktYnZQWofpbMBYr9Vp868dgRYO6ON4yBCXaN3DnGWz_tOL3QwQGlHBBAKy83avKSgIqlOLcbHypLqKjGp5uKN04y6R0BQVS73VblI_-Zrx1r_f4u2cR-sNlhTa6O9zIHW5-WqcH9M-YXVF7s89VDii8XUKQC3UcOg1AQ6bfsJGAcHrGq1BRnrm6_w-qU_mFBzYMPvu7F4QwQJDKOetDLP_K8ULAZbydE2bdPIN-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p8fqXiZGzqJLNTKRSXcpi71FCndnZ35LmQfDruthCyuK8CHH_DTisBAqwp8O9N9zF69tzKWz3aq6gbODYkqAIQOpqhv1v0BoZG5gNBuA3gFufN2e52dOCTLv5EJAULBdZuWpO_7ZM2ivobnPfwv6Q9KDR_Uet_YvhWUEOaky4tpo1s9Ce6-fDqCWzhUv3jeWNctgQFUDkq7WDCDVF4R7Xw04JHDGO2oXsUhVsuqN4PElDtQOsYouIYdttKiT42wlyCkeekpem0VKErYq3X3qZf79AEH9zWh-stBi7OfEUQk50TvJpk-BT1DWB6o5XcEVqdinkpbeYDyMqYJGUyhtrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNyNOWGznv1GJf3Q61Sc3WcJ650bYzRS-rDOOVG9ZZUPaVXCWnjUURaw_r2a7AnhSCIMb25K8vnKDE2UehpvgisAJoO0M2wcR-NYWRcqhQKQ9yz_96QvsMY1dcUKM_ENaHyfzJuYp3Nqu9hEyaMdZwhnA8U78oDOQyZdgJ5FoMosvfaqBvihG24Q1jYo-Nix0tReAbpjnmDKdR5iK9RK8zrmr18K1Dqfa0o47tWkU9x9H1bJwYa6nhov0Zqt1j_HTBMbmk94jPpVgzn6j6Xiw999UpKNWsVCEoPx2puMlPTJfqAcMOFOOqwgVwHaZDYngzI8ZWExMRwJG_22tbH90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DfS-CuUYKQe1A7E5VHTI2sPo7aXkT0qUk16L7Vt_r25g33cPyMXHV9ctfP-3iBolTtOPKVPzkb3jmUT7PIbt3UoRLrhfeqgEB05MmnFVksJhNj9Nl1nBrOp-z7i7YTz-v4k1W8MbVUtDgwMDAdEB0uszeS8hbKwDJoK1Yd1oI9zOwl5zhNvJo0_v57KAiADYEfzY3tCJGBgpxImwCp_MbhKZH55l256n3UCB1xXElnTYob-vKO-OV_J6dIGwGu0lHucSFEHeOX-Uzg6p7C5MSWr6jg22T8nao2z0qkMMOR2qrETqJWQRPKsCHuzHWvOh5ZbU1cNEPOHFn6InrTfUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCQUxfypID4QQJ_TzObXBu5soZ8hDRPK69tmYLpdYmGY_urTZQYG6DKEHVdZiuukjrtGjxQS4YiO9VmnvQS8uLirevRtssqkoXKUtvYB9vdk0RMesdiDZOlcs6qkDMtYLsCyy3HIxcYZLWDG_vkwWtA5z65AKMRxw9Bas6wnhQCzh0pMZoPsfmvjxeCNqHEWPaZBT5cd5_aXR0V9MikAuO0PaN8vGldC2BW4oo3HS1eRoYAbxNbS1HVTZteymTGPvtVT_sjG4umsTSNkWlA2_5tu9E4u_pk-lgSjhNI-9HO1hbwbn6H_-m9GNCIVB0ptv3JwxGo_hZiFPLlbM3A3JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohHirKb8B7AU4eC9BHIAyTwUgpKWYNTLVxXP-33IJhdYNXnAkqKepR5aszc24pjpr-KIO6pHrTObh5N0R_9nMc7BICxTjtJOgyyCFZ7Og5447jY-fad3WcsL_NfajTl5EAwncqwCKAZU4xoWX6_Qhxj7fGTSVOozQKmjHcN8y8nY30ixDV4EZacJNEcSrB4nSiqSKN54AUCLfuvq3VCCFE_mayMC_-LBfn7wef_P9B__BrDDIQBiH4Qw45m12bU3xOFO7_tPi2oIkCNz49Kpul6ZE0ya2qYEnLoF8uK15kRRH4syAsFLQ_BGlfE9UfilVata4xEeg0hcSPHDtUxoeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آخرین وضعیت تفاهم پایان جنگ این است که تبادل پیام ادامه دارد و به جمع‌بندی نرسیده‌ایم.  @Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/439213" target="_blank">📅 15:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439212">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34a7935398.mp4?token=IzFBzEOSK4KPG203PrjA7WFhDTZ_XWvvEDrVfIGRIXR18TedMOadYhzPqIcuA-ekPMPul6GmnQe0Irh5rXqfLf0_SJDgj6VTEbBMNv4eoxtD-00LBQt3r7dsHHAMXWu-WWPjXpZvuApM-3Ryoi7iNUE2vS3Lw4FlAdziT3RRIBTwxosuFsbz1jVvNkM3T0ivwBCQIJB7x6X6xEp5w34UDee7V2VWvz-tSslPATgC9PbJBOXiXRYih9uo7_eRcmZytAh3fZnY7LYRv_tzD_mvh2eTM-OfjqTySe02o8VuCP3R2r4E4NOYHQbrsOw1qbcuAaBlyWNSbDet-07yQW2kEGlt7nQIuoDt7rxml0Q7a6YlK-8gbbKIHyKZtGOhpMs-PqyPLg2lINRskD11aBlOskG0TOLL1M3nQ-hmTLR5JmYT19CxgFwD-Wpxwk3GE67znsZel0KoZk0FXklq_V4pyQtTlUKNejrLMCHVRtGz5CXULnDT268dfWU0ifHPSTSjSG6HeZDg2ed2B9JzkuBCGZRc7-u6N0Nvbisjxf03Hyvd5N4jZwa5DGgVZUnsNzm6QhgBLnocioo1lIDEEtnr5jxgWrhMWDI9lmBV8a44rNPE6t4CNfzgFHPyWnbgft-Wy40-TlhD0DfJFIcX1C_9XXlrpyDs_sKHhubLxXM1YHU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34a7935398.mp4?token=IzFBzEOSK4KPG203PrjA7WFhDTZ_XWvvEDrVfIGRIXR18TedMOadYhzPqIcuA-ekPMPul6GmnQe0Irh5rXqfLf0_SJDgj6VTEbBMNv4eoxtD-00LBQt3r7dsHHAMXWu-WWPjXpZvuApM-3Ryoi7iNUE2vS3Lw4FlAdziT3RRIBTwxosuFsbz1jVvNkM3T0ivwBCQIJB7x6X6xEp5w34UDee7V2VWvz-tSslPATgC9PbJBOXiXRYih9uo7_eRcmZytAh3fZnY7LYRv_tzD_mvh2eTM-OfjqTySe02o8VuCP3R2r4E4NOYHQbrsOw1qbcuAaBlyWNSbDet-07yQW2kEGlt7nQIuoDt7rxml0Q7a6YlK-8gbbKIHyKZtGOhpMs-PqyPLg2lINRskD11aBlOskG0TOLL1M3nQ-hmTLR5JmYT19CxgFwD-Wpxwk3GE67znsZel0KoZk0FXklq_V4pyQtTlUKNejrLMCHVRtGz5CXULnDT268dfWU0ifHPSTSjSG6HeZDg2ed2B9JzkuBCGZRc7-u6N0Nvbisjxf03Hyvd5N4jZwa5DGgVZUnsNzm6QhgBLnocioo1lIDEEtnr5jxgWrhMWDI9lmBV8a44rNPE6t4CNfzgFHPyWnbgft-Wy40-TlhD0DfJFIcX1C_9XXlrpyDs_sKHhubLxXM1YHU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گشت‌وگذار پلنگ پارک ملی گلستان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/439212" target="_blank">📅 15:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439211">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frhrPTxMmwu2IPVFgcwbWze2UBIeFt_OGQSyboK3G72HRs24jqO6FylgPrmK0f0KCg1vOqNrpMhmBGdW2UIHoPQZ0Cw9yFPDH0wF5bmyWTF1g_ZUWWJQcMQXZqG8acUVCgmFglIXdqun-JmREdu9J1GMC1OIwHpHHvGuVjACX7lAFlTy3-XniUfXwzD0G00cx3HN5Z94TyPqG9ZcMRMRDEeiqeXpyqRWhZ8oZyjViTlyofRHPvvOTA70pCa4QYGgiw1h71oIXd-qi1sa0Dn8WVU24tkQdS0nO9n_0TdFQrMP8I0D82jZhaOJmbbPOeqQT9jcxRRvRHE_GbL4G6U9DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آملی لاریجانی:
مردم ایران در کنار مردم لبنان در جبهه مقاومت ایستاده‌اند
🔹
حزب‌الله لبنان نماد مقاومت مردمی است که در سخت‌ترین میدان‌ها، شانه به شانه ملت سرافراز ایران ایستادگی نمود و با وفاداری و فداکاری، تاریخ را رهین عظمت خود کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/439211" target="_blank">📅 15:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439210">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxBT9mk8MWW3qYX0PZYorNUJV8HrkgadS-nqFusykyQkqt46EPz6wcSUfhlUzg3nLoO6Y5t_J9q4KM1QSH-FvKfvp2tZ-e37Z-za_U69c5KQTmOAokKvSYNEPnsB-HZWRCYb84AfcbRY3F9taQe2sM1GDOtRgV1J3gUOzMixfh_MFizqD--OSnN8gJ0g_F2hTnqvUfc1qlmCSsbGLanUiWC_rIlVfm2rthRuMBfkZ26MIZXYxEyzvMS2277AccQe9AeFMQIYef6iLh8VqykKkgdhIsF2hGadkdlie-0lhZTqWrueO1kBGBXuf_dtEzUbVHV1ulkD3qA-dDkdpVvdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
۲۶ مسافر ایران در جام جهانی ۲۰۲۶ مشخص شدند
@Sportfars</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/439210" target="_blank">📅 15:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439208">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e235c0d4.mp4?token=fF4OeOqwV9nJ1DQRNoyuRyabGxit6lrY_aiHkeWSckcMO8-D8ojmG-Zlhzhc0vmbMQiRyeh6LLwTXGpicTZCP3q3vkJJehQks5kC-xijrAcbI_Hql0hxg2R0izhQZ0W9Ru58s8pltCkLalphJ2P7-PGaFTjxQCSRm2Lk6p7IP8iwEF2qtjjyWumEfZF1IZt-H4T1JX2xfThPdwA8zs5kd3fSPo5xjc59raXb5on4P4_NrxyEeXkqHc0dLy1gSKXsbt9qWQvfwhwAmMulZkvZgzEPuA_p5Wpu9_ijcyPXuglEnUS3hBltP6yIV5a8p9QbyGhtdCAZCTo1esVTg2wuLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e235c0d4.mp4?token=fF4OeOqwV9nJ1DQRNoyuRyabGxit6lrY_aiHkeWSckcMO8-D8ojmG-Zlhzhc0vmbMQiRyeh6LLwTXGpicTZCP3q3vkJJehQks5kC-xijrAcbI_Hql0hxg2R0izhQZ0W9Ru58s8pltCkLalphJ2P7-PGaFTjxQCSRm2Lk6p7IP8iwEF2qtjjyWumEfZF1IZt-H4T1JX2xfThPdwA8zs5kd3fSPo5xjc59raXb5on4P4_NrxyEeXkqHc0dLy1gSKXsbt9qWQvfwhwAmMulZkvZgzEPuA_p5Wpu9_ijcyPXuglEnUS3hBltP6yIV5a8p9QbyGhtdCAZCTo1esVTg2wuLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رهگیری و انهدام یک فروند پهپاد دشمن در آب‌های سرزمینی ایران
🔹
سپاه پاسداران: بامداد امروز یک فروند پهپاد MQ1 ارتش متجاوز آمریکا که با ورود به آب‌های سرزمینی ایران قصد انجام عملیات خصمانه داشت، بلافاصله در رصد و هدف موشک‌های پدافند سپاه قرار گرفت و سرنگون…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/439208" target="_blank">📅 15:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439207">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nW_wJMzuHSkHFicZIzP9RkEP3uG3iEDiI6VyP1XHZ1NVPV-agNfAGszfJybrNsyoEwQf0v7gDF_JJM_KNSEemSJLdqquM_4Yjwl8u3lXluBlc5tE_cJpxBe0ivVuDUcpNT57YtmxYklxxlh_VcaXc_uZYNVN18-_fRLqj5OPWSOEgNDA8pT-lvtK7oLrNFZTjR5BKAkm847UtjLHIsvw_oKBkfMYVnBTOEombz_cgONYeGOCQc79fTnNKwRf6QyPmXjQc0rdhiADiwvS2DHLJh3VEZjBC1SgK8kZ1v4Dn8fdvOJivUWSUwWai-Oa6ADPKO7LBJRr4FvGyFNv8IQUyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جنوب لبنان این روزها چه می‌گذرد؟
🔹
جنوب لبنان این روزها صحنۀ تحولات سرنوشت‌سازی است. ارتش اسرائیل با گسترش حضور خود در مناطق مرزی، ده‌ها روستا و شهرک را به اشغال درآورده و موج جدیدی از آوارگی را رقم زده است.
🔹
منابع صهیونیستی از استقرار ۵ لشکر نظامی در مناطق اشغالی و کنترل حدود ۵۷۰ کیلومتر مربع از خاک لبنان خبر می‌دهند؛ منطقه‌ای که در برخی نقاط تا رود لیتانی و قلعۀ راهبردی شقیف امتداد یافته است.
🔹
همزمان با تشدید حملات و صدور دستور تخلیۀ مناطق گسترده‌ای در جنوب لبنان، نگرانی‌ها نسبت به تکرار سناریوی غزه و حتی اشغال کامل جنوب لبنان افزایش یافته است.
🔹
با این حال، حملات حزب‌الله متوقف نشده است. عملیات موشکی، پهپادی و کمین‌های میدانی مقاومت همچنان ادامه دارد و حتی تحلیلگران صهیونیست نیز اذعان می‌کنند که گسترش عملیات زمینی نتوانسته از حجم آتش مقاومت بکاهد.
🔹
در کنار نبرد میدانی، حزب‌الله در جبهۀ سیاسی نیز با فشار جریان‌های غرب‌گرا و حامی خلع سلاح مقاومت مواجه است؛ موضوعی که برخی ناظران آن را عامل افزایش خطر تنش‌های داخلی در لبنان می‌دانند.
🔹
لبنان امروز در نقطه‌ای حساس قرار گرفته است؛ از یک سو اشغالگری و بمباران، و از سوی دیگر مقاومت و نبردی که همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/439207" target="_blank">📅 15:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439206">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmClIBDM1v_uiCJhhw0CnJo35T6Ct0oisQ-4VjMm-MQO1qRCT45aZ1UpEYLO6prZpqW5bczYLuZqPPFOmWfR1dH8UxvYvZynkzRafSrKtZZjmVU4fgDVp2FPbkZZ-R8QZm1qf96MizhGl10TttPKCxRlQEsgyAMhMMQ9cd87vGC6jkC0VIUcTWuEFuGiydi1Mg46F9cdPGR-GY2G2DkG7nYcTrfjqZ8TKf9xyEuw8CrNSq1xgSAATvmsiY9LtcsvbbyId-q8l-HgnP6yKgETqRUJOwxUnjciZvUIeu3kGGwkGEid0YuInb8RsxzTYjXu2JombtSqmltRxRWbLNH2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مجروحیت ۱۳۷ نظامی صهیونیستی در ۲ هفته
🔹
ارتش رژیم صهیونیستی: در ۲ هفتهٔ گذشته درپی درگیری‌ها در جنوب لبنان، ۱۳۷ نیرو اعم از افسر و سرباز مجروح شده‌اند.
🔸
ارتش رژیم به آمار کشته‌شدگان خود اشاره نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/439206" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439205">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c7b1bdb6.mp4?token=dRqrSOUgTPfvgXqX1UTJs0L16a_XxkUsWMZTuV9622syhuuiFuRUQIKl8AWkuF7XVYlO6jrWpS2Abk5S2h4A7M9LG1_VGJHac4XL3oC-PvRWMzA1ZKzkDK_K5Hg4n9D8RGncLKxQ_p8vsCENB2WonUuq9ylgkdzQVVsNds_a0ptnRJURKndZrPb3Km1OdyR5gZJuRFYqU2xinSrF_OCBh-azZSx0hlDDq74ezTXpg0z1v4-u4TdBHacG3HKFUwn0ldpgr9_Pj5Rri8QzOcAFGgS0jhlJUWCbf6t-3l-Xb1n6y_7auArdidvxT6h0KQZBtQF4jhHZnp2LjDoKrkZkgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c7b1bdb6.mp4?token=dRqrSOUgTPfvgXqX1UTJs0L16a_XxkUsWMZTuV9622syhuuiFuRUQIKl8AWkuF7XVYlO6jrWpS2Abk5S2h4A7M9LG1_VGJHac4XL3oC-PvRWMzA1ZKzkDK_K5Hg4n9D8RGncLKxQ_p8vsCENB2WonUuq9ylgkdzQVVsNds_a0ptnRJURKndZrPb3Km1OdyR5gZJuRFYqU2xinSrF_OCBh-azZSx0hlDDq74ezTXpg0z1v4-u4TdBHacG3HKFUwn0ldpgr9_Pj5Rri8QzOcAFGgS0jhlJUWCbf6t-3l-Xb1n6y_7auArdidvxT6h0KQZBtQF4jhHZnp2LjDoKrkZkgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار صداوسیما: با وجود اعلام آتش‌بس، به‌دلیل تهدیدات رژیم صهیونیستی، مردم درحال ترک ضاحیهٔ لبنان هستند
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/439205" target="_blank">📅 15:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439204">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
سازمان پخش اسرائیل: حزب‌الله از بامداد به شلیک موشک‌ها و پهپادها به‌سمت شمال اراضی اشغالی ادامه می‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/439204" target="_blank">📅 14:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439203">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIBDmQqGMnyPMyGu3WD7LDA_z5mbgj9FbpK_WZ97QIW8rpCGITweeIzPS9X4LVVfEOqUejumyG4Sm4SGMmKcqTMG1EIUAaLFU6y7pXQN7fib0CG9AGp273jwWLIUQ6-aWQwtU_FgWeU8uHNByXylknWGC7WRYzQQYzWJG-IQBIsuFfDfdBZ-NSXU383j8yX6kbfOgFc4O7Fk1NxQ60qZsUxjr9rexTyK7AMJvI3LlYswSmht8NaYFEQjqLkUbYo56ij62ulGm3utpRW8g83HXThHkvlJtCdhViIR4NNCf9A6eEFuStZZiy2fP4RCZ2nXsRPd-nvCl1Knu84V_bucQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سردار شکارچی: تداوم جنایات در لبنان برای نیروهای مسلح ایران قابل تحمل نخواهد بود
🔹
سخنگوی ارشد نیروهای مسلح: رژیم متجاوز و کودک‌کش صهیونیستی با سوءاستفاده از فرصت آتش‌بس و تجاوز آشکار به خاک لبنان، بیش از ۳ هزار نفر از مردم بی‌گناه، از جمله زنان و کودکان…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/439203" target="_blank">📅 14:39 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
