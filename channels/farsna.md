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
<img src="https://cdn4.telesco.pe/file/NLRxiNNJBocQNzHtAzunIrEE9LkykRZvy2Sl_ZdG-VO4V0edKexSBP7ls4IWFEuEKtCMUTYMHZZuvJoWOke0OSaiXDKRRTdF386sTuZS6qN4DeWWdkpQGm5UuZozkXd7AuFTvHXt3d6sVqHKzBSlIwryPoBW-Ni6I3iXlEkZl6DQGyzAx4Pe0VfxLplOrInh9Z1b8gMjHEMEc0cYBLpoLk7ivneQg-AmazSElzDYbFd0b05trXfhbybkNl3HpZ2K1ffIZvo0knLt11C4LXniCcA_cOs4u6jKaBU6fQUeEH1sVzb7ntoU7MMMWwWyzx3X6cBS_SjfUCnpS9c0X7unhw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.86M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 17:38:33</div>
<hr>

<div class="tg-post" id="msg-460923">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-uaceRCmEQbxHAWUAVBrqMrY9fcGeVnal7Up3L-7sldb1xzNJHLNgkqyOpE_7tlP5J-9O0DOFznNyWZ7ZxqmMjQzVryCRvVe-i9u6G4fo4BxrDjrN6uaikrVEF3sMK2RPy5e_dZOX6qpOzUdo287ihW1X8CpdrDyrEAjETi7hOQsHJtG56EYV6Gr9BWrZUvppwU4R69hOO8dXs3Yp4zsLWax3XFlwKVs9S5u52_eM53pudG3G4Y3UTUjuMrmA-alUGXg1jP5jRNGB5dxIwgcyBXG1AuzOXNsPShjPuX6FIf13mm-DDDXO2crp6mb1lXYo7_CCsVZ2mvQkWMxW1wPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاور عالی فرمانده هوافضای سپاه: در شرایط پایدار تولید موشک و پهپاد هستیم
🔹
سردار بلالی: امروز قدرت نظام جمهوری اسلامی از لحاظ موشکی و پهپادی پایدار و دائمی است.
🔹
اگر دور کشور ما را دیوار بتنی و سیم‌خاردار بکشند، نمی‌توانند جلوی تولید موشک و پهپاد ما را  بگیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 327 · <a href="https://t.me/farsna/460923" target="_blank">📅 17:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460922">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_3esF4yjNwsa4oFEr2zlQUm_jpBesKva4PDL6VRIzUAWyLdvfhwWJPpIWTl6ZISgTDh3E0aScNu2Zx-x2_LmSdTRWefybXIC35jvsRDWc2lc6SL8-bQMDCAWkmmWFsjbmVC5wz23De7AdG2tVnHqVUDQ6cSfB2k8_SNTMralDl39_nuWvCNR_HqZcTVz4uVQh4z69MHDcIxFyJlOIETWYZ2Md-ZC74Cmk_9_iheLvW3-SBx4ujewwvCkd--BM-9qATTUWMN28UDuf2S13mzYHI30KmeayMz3YM3_WDdyjKHCbtgskWclBEBlOGqIoGWAUn1Dgmmn5K4hC2FCuF5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرداخت خسارت اثاثیۀ منزل به آسیب‌دیدگان جنگ از شنبه
🔹
رئیس کل بیمه مرکزی: با توجه به اتمام کارشناسی و ارزیابی خسارت حادثه‌دیدگان جنگ ۱۲ روزه و جنگ رمضان، پرداخت خسارت از شنبه توسط شرکت بیمه ایران آغاز خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/farsna/460922" target="_blank">📅 17:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460921">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPUgo_5tbQ_NqqU7G6aEsSZa5Xak163UTJlx7Y3vkUOL4RysYv7FtyYwXRyZGZPgNVAXrOhMIkRBdZxoJvJrTYaSIydsF1e2arZWnHvMb2kZRur3PwgJh03YLtLMReJ4_qu71FVnxoiN4oqA0JGRuMtUvWiSwCFydTQMAUi5Fv039uP6iCZpaqsf3bz_w0pY-IknZMe6K0kR2Ww61_d8ZfClPfwG67K67Cn3soq0RWhXlh97StevG8vKf5vx1uVIvxreW1ftfJXbZbUkxIzHnruCKGC6AVn3Soxy6D3I_sy1er3mpF24HVqVjjgpKDFHqmZYPqeKiR_SqWJLv2FcUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: با ساخت‌وسازهای غیرمجاز در عرصه‌های طبیعی قاطعانه برخورد شود
🔹
با قاطعیت با هر اقدام فراقانونی که به محیط‌زیست و منابع طبیعی آسیب می‌زند، برخورد شود تا بستر برای بارگذاری‌های جمعیتی غیرضروری فراهم نشود.
🔹
تملک اراضی و مشخص شدن حریم، پیش از اقدام اجرایی برای احداث جاده و خطوط ریلی انجام شود و هیچ‌گونه مجوز ساخت‌وسازی تا محدودۀ حریم مشخص، صادر نشود.
@Farsna</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/farsna/460921" target="_blank">📅 17:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460919">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7708c5f418.mp4?token=ooVfRwL53v56SIdv9kamx-MWbRwTntz2dco0f-5Ilv1598lkTtx1KEmU_pHQ6YxQ93vUc2vkPfYbKuBR6LVd5Ld9M8XYMeLbRXb_wuE3KzYUG8S0fsE4BFd84d7_Nc76i9pg3kCy2ZLtaJ4mKFJKXS_SPBMhyaXUcXYggv4rKxU64VVsF2rNsPdw7o5bvObOBkvuhrqCIUH_nyK6rx7dShprKPhA1O3x43F0HGKLLw9PzPdTahvXIi4ahYLZ7C4uwgKuCVyUA5DBHG39UUYndHLYr6G5fonYv0WZ1PTZfhDx7uZvVT8mTVQ2xK6Sleu4bgBLESdTMulfIsgqZf9BAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7708c5f418.mp4?token=ooVfRwL53v56SIdv9kamx-MWbRwTntz2dco0f-5Ilv1598lkTtx1KEmU_pHQ6YxQ93vUc2vkPfYbKuBR6LVd5Ld9M8XYMeLbRXb_wuE3KzYUG8S0fsE4BFd84d7_Nc76i9pg3kCy2ZLtaJ4mKFJKXS_SPBMhyaXUcXYggv4rKxU64VVsF2rNsPdw7o5bvObOBkvuhrqCIUH_nyK6rx7dShprKPhA1O3x43F0HGKLLw9PzPdTahvXIi4ahYLZ7C4uwgKuCVyUA5DBHG39UUYndHLYr6G5fonYv0WZ1PTZfhDx7uZvVT8mTVQ2xK6Sleu4bgBLESdTMulfIsgqZf9BAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب‌گرفتگی منازل در پی بارش و طوفان شدید در مازندران @Farsna - Link</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/farsna/460919" target="_blank">📅 17:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460914">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihPNWc-za5ydUvfwO6gx-ocNxuTY_Ym0tIm_jmFVchpJIcFu2j5vhAy_q2uHc24RhKAA6PcJyhHYFZHocCv4qnxkR2MIve5IkXk89tEvL8tBtEHvvKeSnyCVs_s89cTsR7FpYPYFI1K7nVs7qDKeXNPbUgNuO4GrJsIAocCmgtTE6lBN2_Qv3Phbc6QVSrXVTlCriSF2ksx7uIe7dMKHp4Zt2gJM4HPjeqgilhqU78PxfhP9IYXD7_ARHULo8ssPsF-PqEXi_5ng0sEz19ybSsJFZRWyLLfoK7KT7DifBf2T04tf1uJ8px3iowSs4_9Q5nuGdVb5ZWp2xssPfTOiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjyIz20rk5QjQTJ0EuQhyR5C9wQMmZLjwxYD5dztfouWPPX9MX5JDnmce-jAR8jI9I4-vAIAKHM6N5yAdOrnlv_dtUoNMWphfqLpeHuxiEjnUutMrwe4XtwH8668aEvODTeDOR9vxt7F5tZJk8jwcpQJVbd2OxYz278cfKXO-AatMQX2mjw9tRL43pwxNozgQoa2rf1Ed5EmnL6RCPrKSs9hWuclqwobPI0ZkTE6Z8Y_TuYHlgICV_FR2pX6kHmExGvIMIKs0YlW7bK94KZFTrBgG9B-8bWuUcVHVDjOiSJ6Jwfqb9v_0XVJ5hO8hin4ZveAAqKGjaK2WkhwQ-afYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffP7YPlSiHmP_8Um6WrKIuClngSYLmrGbecG7LwDJD0-2Ps-XG04mE9zhF8H_m_EBVE2BAeuT0tocoYsmYYAZNH2yIYCit3xEX7KIpxUVrd16f7pCXDt9e8KVbu5lfHpyltI9UZeHDZ1g96d0dL8HT3NQiocmBCqnAXndrLmJT7pElZcknadN5kQhTBBpqwP0tSBjI-HrVb64UEM_GbiaJ3PWT9jzV2tA8aZtSTJuL5OGwMYfCaWRYb9kdcJB9N2fLcAKgsYGkrP3iGFAbnUph-9I9PMVi5GNcicM5ptNRPcPr2hszOqczq6-6_dj_C0B0dGLt97kLeQYbNbLk3EIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XlN3DqpbY_A19861LI79rNXlrV22sGkDkDLfce2URYw_mqn7dea5p-9EgwZAAb26dXX5UL-mFDU2zOr2TuApARAxNuMWTf4jOd3DqUcbbusNVkwVay6etGHGzILgMmOCh8IKninLNRbb0NrwhYPNmje-sXYhBccHc878epUJe7Jg6aUpkYpw-E97tjD_RepneivjGwGQZVwRlealtbpDNq24nmLzFYk69Sj4iuxy4MgbqYwCwOkJvN0yMUw2XTVN8z6vdK6AFw5YkiWHSM_Ew4Mxb9a3P80QDwv9jXQQEb-IeW0UHSiSQtimNWbK6n7VJAxOqx4ExNqluZciSMIDvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j78lKUa7wSDCBLWvuwzXR0FThP4F0BIFkvzywp6zt1_C3T2-7uhMd7vd_kTZdDkRCWyKIeRKXchAd0rl5kn2DSN4OCneeqqBhc14bCJbGaz8EfFZcd4j8lvHPvhcwtpYXfiAd5UwxopjX0ObGNip0J3hXAC5jRGrB8qKdKZXE_gPwWTQisT3xo54pBdLf-f0H5c86EdHNCqP-h2-Gt1NsU_TCZjcVZk-dOAQb9JYZlBQw8wIfrw_h_LiFiRbxwdKFRoyf8x07dl7a8n9ZHXEBllNWJ2npmbSp7w9mRJT3ydhDN3kywSFLDgMAbFfzQUcunTAS3of23qKlgvfPSgGqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس بسیج اساتید: از ما نخواهید که بسیج ساکت باشد
🔹
هر مسئول اجرایی که در راستای اهداف انقلاب حرکت کند، باید بسیج را «نِعمَ‌العَون» بداند؛ ما حاضریم برای مسئولی که در راستای اهداف نظام حرکت می‌کند، پادویی کنیم و به او کمک کنیم، اما اگر مسئولی در این مسیر حرکت…</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/farsna/460914" target="_blank">📅 17:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460913">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFTsIf8uFWZWC9OE-13Iwppq9L6xgf82wxbPAbRwvqLh9PaPvdh5Q0CXOpQfiyF3_H1Qo3s5ceD2iLS118bgleASeLR0sx-gP1CGpK4P-CZZ-vnJE3d3kevuU6HqsNqvVdjExw_FcKbqzMVbTUm2PC2V0exqveL7mLF_-yu3VJZco4xovnQr8zQNTSh2TIPLrnLwsmwT3rHiIeXUJhjchBK79XDvvUlPma1VRb37ikVcc6GX4yzLn9xLsZexgEN8-GovWhfY23c9nPL1PwO0dHaYfMjrE13euihiJvMw8kohkE1S8ml_yurBEoAe_7dD0ZqdU0gOZvMlKk-nFBcgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قالیباف: دولت و مجلس مصمم به افزایش کالابرگ، مخصوصاً برای دهک‌های ضعیف جامعه هستیم و در اولین فرصت اجرایی می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/460913" target="_blank">📅 16:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460912">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMiBIOpJbapHviAgiFfEnyj-8Jc9Tvqds5rOk37R5Lyc3s8L1hnhmTcvv0mGeUsmZkKpWCutGmW-g1isMBNb72W2a1Qc4tUJpinVA1128D4qnDGt3aSve53IbnBs7qG1rPDT2DXknX9gxxM8d73Lejv1xpVw4rSAI1UfPKjIkhtuHcBJdKh-fHRS1mJJIyCBTsH_Nw_DE85n8KfmZVmrNiKL4YkAtIKVu1rQRp8IX3uOcj4BO0Wi6IPbhymK2YT59huaPsVISk84_tqNMqIQ2wybx2qhpZbsmLyOHGg_Sw7Ak510QgOUvl5iorWKdBBrSdMrUAwgZLh7MJmtc4ln3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب، حردانی را از استقلال کنار گذاشت
⚽️
بختیاری‌زاده: تا زمانی که من سرمربی باشم حردانی دیگر در استقلال جایی نخواهد داشت.
⚽️
او  فقط به خاطر صحنه ضربه ایستگاهی در دربی کنار گذاشته نشده و از اول فصل ۳ بار به خاطر بی‌نظمی به او تذکر دادم. @Farsna</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/460912" target="_blank">📅 16:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460911">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کندوان مسدود
می‌شود
🔹
پلیس‌راه مازندران: از ساعت ۱۳:۴۵ مسیر شمال به جنوب جادهٔ کندوان مسدود شده و از ساعت ۱۷ به‌دلیل وقوع بارش سیل‌آسا و احتمال ریزش تخته‌سنگ‌ها به‌طور کامل بسته خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/460911" target="_blank">📅 16:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460909">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEk16Re6GjVwf05d8DycFYg3QleHpPR0LAoPPs-fRGDEyGFul-0ALjXiMq_L2YO_yjGnTfwXiVlnOGZD0fTLV15-A1mZu0Q_4GfOWszOdZ1HT5dlCwJ79Dt5tchHyVKCBkOcsW37o-Xu2sHG2f9DiACP2QuLWVvbPL5KJOhibIXLlWjWURNL1MExrHJnZ5xDgqqXgjsVgMrE3PFDjUU2AwnJIaTBfcEhT3Uo9yS0hqZvMrEYC5hBStY-rck5r75EjXhr6Sja9ELGSGWWihCzEyNut4DePNJxm15HMkxRxf7D4LHc9ANjzytw9fW_-LobRvbgR10OTEznv7YVlrWAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2LU5_9OSeCZt4e7vPF-ZkDtzl02S15AFSCaX5Y2rUPIhoZ1g6sg-q58cLsQAui9vCyuN_vYaxLwd86s356rkH82Eq_ffTh--oEWO8NB9rBMmtFaVBTSz-U1omdBjtNttdGQ__4sH2dVAUSLZKBvth3ewggCpyc1QeZ0ybZ5CX-pmXLUUgnUpCRub8W0rwEU-D1sacQdLsfrrTIUgz4xJxLtOFDjnMRkqbkIbE1OrEIRbHssNxdKzLiVunsdprfgs2EspiZaHgIWzuQsAfbtFfGta7QFER6Ua0iQgwFQxsH91FydmNYs8lRExLgdG0SZ2SaUvPqZvvATluF1AWDMJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پایگاه هوایی خمیس‌مشیط</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/460909" target="_blank">📅 16:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460908">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hV5oZBwtFUtH4GTJMg5zF8ZeyylKXFNEaG5g8O32hS5xVN2Li9WGVWg6oGLpbZf8y8t9NgzvYx__151S9DCcCgN4vp703D-dckSvPG4P9fxwh5ENsmHkyU-4GmScaRP1lRGV_LErckdrFXzgw0SjRYN6a8QbqiwaiYqBslthkUT1FlgarnIl1tOjS_YaIAANkm0usiKF8bdlVf9izxeTEuJ1m5T69ieb5PwgER6dB-mebb30j0b7b5H_xRChJD3fWuWEfnipa7NJJownC6cTQ63LyLDoYc5F60vY0ea5E5nDKEMCCxcetAiAghYtVJVhKmouykjnnQF3qUIppAJG2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۶۷۰ کارت سوخت غیرمجاز در مریوان
🔹
فرمانده انتظامی مریوان: در بازرسی از چند جایگاه سوخت، ۶۷۰ کارت سوخت غیرمجاز کشف شد؛ از این کارت‌ها ۱۶۴ هزار لیتر سوخت غیرمجاز عرضه شد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/460908" target="_blank">📅 16:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460907">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
۴ حملهٔ هوایی رژیم سعودی به مرکز یمن
🔹
شبکه المسیره از ۴ حمله هوایی جنگنده‌های سعودی به شهرستان «الجوبه» در استان مأرب خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/460907" target="_blank">📅 16:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460906">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
شکار
یک پهپاد آمریکایی بر فراز تنگهٔ هرمز
🔹
یک پهپاد MQ-1 بر فراز منطقه راهبردی تنگه هرمز با هوشیاری نیروهای پدافند هوایی جنوب شرق کشور شناسایی شد و هدف قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/460906" target="_blank">📅 16:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460905">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎥
شاه کسی را نکشت؟
🔹
مردم پاسخ این سوال را می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/460905" target="_blank">📅 15:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460904">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy0dv2neVxwbuwu3hnbyJPLpN8VjKc9p7H-CPlrrHYel7ALQg6G2DMslX9Adz8Ma_ZJQbS3VkMAZuXnfLmtB8CRGhuuHzLWeRWRaaMNwvgDdK2IKjmWFd439e-rKGYHoPqDEIB4saM_HXIJy7BfkmJU3WlsM6OLYLWz_0S_iUAkOjbwFGrx1-vbQbCrGiWYSM2AxrC3pR4Z0aRhldhGowylV9vG_MbTCTOBra5xdhh72a1XDaCvHQUDmHtwquHQu4Fy-SkJFUktSogaVAG-SI22uVySq4qo5hp6rXUy7PXwU7wn2-dHAm27gyk1nM6g2XCb3rB9hD0zmX_Oe8_ln7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: روز بدون خودرو برای دستگاه‌های دولتی اجرا می‌شود
🔹
با توجه به ضرورت مدیریت مصرف بنزین و اصلاح الگوی مصرف سوخت، تمامی دستگاه‌های دولتی یک روز در هفته را به‌عنوان «روز بدون خودرو» برای کارکنان در دستور کار قرار دهند.
🔹
توسعۀ دورکاری و کاهش سفر‌های غیرضروری…</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/460904" target="_blank">📅 15:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460903">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bezWsNBMoeOP3GH4BqwleEsu8xHqRuy_9nJfGh3FfIdP1VNmIx7pLFq6caPHlg-fqq6Iq6ch2Sy_FkB8CIKPRnIXb8U2y1Jp0vukBzQO-xNMKLtFZEVrIChdewYaJlD9MW8doVog2_Ecu4iQZXRToYazPahIzearVC1TN3eWknAnxKK_0FxUdsVSvvr8QjOBuK_jdGHot2yRuKQcSnnQnfInUuCsNm5sHRrdHtw2gOS_82QU1ZKj1dsYr0GozlS8bpci_p6QAtjehayQceCh4wFG5Up7Ql4xvBraM2TfqxMxvnDEf-G5QSBqUcP-LMcY2t9PIuEGAnNxYDA76CsEQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فرمانده بسیج در راسک به‌شهادت رسید
🔹
پاسدار عبدالرئوف اسحاقی، ساکن پراهین گواش راسک و فرماندهٔ حوزهٔ شهید فدایی پارود، امروز درپی تیراندازی افراد ناشناس به‌شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/460903" target="_blank">📅 15:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460902">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a1d0866b8.mp4?token=J2QZ32BCeeUC67FKulq7Ml_6V6nUDE_Ezh8Qtn9Q3D0Cb-JmxKeKqUajt6lbRpHRJmnvbvMmfud7gZjQ5MRJBTR20eXV-RwfSRpKGH2dAbMk3FMjnXAhM3U5AFWNH4gU90Rd1KVZK77VATfPASlV2iTDSYgLWHymvwhkU9LorQBtoQDT2Lk-vrnY2AxuMdIgtLNNpxssroEMG0jYzAqQ7mToFB3JA9b4VAV3VpnzakJbao0KTTQ_Zf1nVPSwLLSsxKCiq8YYcCuU8Ok3ht9gzKx44rJ_wnbr3Y9u1JbqZCxiInuxJL4veNBJWPr-AuSpI8C4ymOuNLy65p72vDfUuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a1d0866b8.mp4?token=J2QZ32BCeeUC67FKulq7Ml_6V6nUDE_Ezh8Qtn9Q3D0Cb-JmxKeKqUajt6lbRpHRJmnvbvMmfud7gZjQ5MRJBTR20eXV-RwfSRpKGH2dAbMk3FMjnXAhM3U5AFWNH4gU90Rd1KVZK77VATfPASlV2iTDSYgLWHymvwhkU9LorQBtoQDT2Lk-vrnY2AxuMdIgtLNNpxssroEMG0jYzAqQ7mToFB3JA9b4VAV3VpnzakJbao0KTTQ_Zf1nVPSwLLSsxKCiq8YYcCuU8Ok3ht9gzKx44rJ_wnbr3Y9u1JbqZCxiInuxJL4veNBJWPr-AuSpI8C4ymOuNLy65p72vDfUuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرمیتا بابا، این همونه که بهت میگفتم؛ این آمریکاست!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/460902" target="_blank">📅 15:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460901">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm-dmjefWug_ZdzT0reh3bdU_xQFzmA1S3R2n5GRod5-ZpJu6kHHPzzMrCzA14Z-4P0yNfQC9dr1xhGiWnFx6FBtlpPeTthsEURUwweL2NbgvJhOn97zRn9DHJ_DZG_vzolL8asbfCC0uf9_MqN7vFhdyuFRcAFPhqPrIg-T0O_JitOHmkzI9KvgfCfBqjVtyHMRgataBr59Uii4_tsuDSDbsbocDQAQxOp5vS6TvJqNBpAUqYOT_pIiw9F91iSjykj8oHOe6ghVEVvZ9lBG0OmjVC2I_GNlzZf8a9pIHJhyE-HtFqaDQQqwahbmT4dMV7Zb8nfYRiyzk7nlliRSjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری
همزمان با تثبیت کنترل تاپیکو بر پالایشگاه نفت ستاره صورت گرفت
✅
قانعی‌فرد با حکم شهیدی‌پور مدیرعامل شرکت نفت ستاره خلیج فارس شد
🔸
همزمان با تثبیت کنترل شرکت سرمایه‌گذاری نفت، گاز و پتروشیمی تأمین (تاپیکو) بر پالایشگاه نفت ستاره خلیج فارس، وحید قانعی‌فرد با حکم روح‌الله شهیدی‌پور، مدیرعامل تاپیکو به عنوان مدیرعامل شرکت نفت ستاره خلیج فارس منصوب شد.
🔸
قانعی‌فرد در یکسال گذشته نیز مدیرعامل این شرکت بوده و در ۱۰ سال‌ فعالیت خود در این مجموعه پالایشگاهی، مسئولیت‌های مدیریتی متعددی از جمله قائم‌مقام مدیرعامل، معاون برنامه‌ریزی و توسعه و مدیر مهندسی را بر عهده داشته است.
🔸
وی دارای مدرک کارشناسی مهندسی نفت از دانشگاه صنعت نفت و کارشناسی ارشد مهندسی شیمی از دانشگاه شهید باهنر کرمان است.
🔸
انتصاب مدیرعامل جدید نفت ستاره خلیج فارس در حالی انجام شده  که این پالایشگاه به عنوان مهم‌ترین مجموعه‌ پالایشی کشور، نقشی راهبردی در زنجیره تأمین و تولید فرآورده‌های نفتی کشور دارد.
🔶
صلاحیت‌های علمی، تخصصی و مدیریتی  قانعی‌فرد در فرآیندهای ارزیابی و شایسته‌گزینی تاپیکو در بالاترین سطح مورد تأیید قرار گرفته است.
@tappico1381</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/460901" target="_blank">📅 15:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460900">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Minab - LV - Eslah3-1080 (2).mp4</div>
  <div class="tg-doc-extra">118.6 MB</div>
</div>
<a href="https://t.me/farsna/460900" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📣
میناب؛ در قاب روایتی جامع
▫️
«بانک جامع اطلاعات میناب» راه‌اندازی شده است؛ این پایگاه مرجعی برای گردآوری اسناد، اخبار، روایت‌ها و آثار مرتبط با واقعه مدرسه میناب است؛ جایی برای جمع‌آوری خبرها، گزارش‌ها، تصاویر، فیلم‌ها، روایت‌ها و آثار فرهنگی و هنری مرتبط با این واقعه.
▫️
اگر خبرنگارید و گزارشی از میناب منتشر کرده‌اید، هنرمندید و اثری خلق کرده‌اید، از خانواده شهدا هستید یا روایتی از میناب و آنچه بر آن گذشته دارید، آن را با دیگران به اشتراک بگذارید.
بیایید با هم این آرشیو را کامل کنیم و بخشی از حافظه میناب را برای امروز و آینده ثبت کنیم.
🌐
www.minabmemory.ir</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/460900" target="_blank">📅 15:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460899">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه سرمد sarmad Insurance</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awr9BQ-k_SqNQIsVPOq2l9Q3i21ic1N0oRl0tBiwi_X-D7Ux1p7xpb6fxi8foQADny-Au8MCVV40XbcOcQUVmzeut8Hi9r6JiCpy05h6xLuPIdp6LBZX7oQNyT0G8SgkiDuJjlhKm3YmCN1BQYVYeTYWf0pBH7IVgK4zHfjNErhbk9cFfSQkjoE2ZJ9NsMTUrRgvg0aiupAxMMvm_D0eYPZ40G1YY_Doqztp3S9u1DrBxKf-U1McI125bYaB9Xm8tR9zKEtWwVhw0ZkoZZu3jWq8EseQZ-nFne4y2mxn5CZaVLgupSn3biVfQgeVGuCAckeNim24TwdXHyjqvioUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ثبت افزایش سرمایه ۴۰ درصدی بیمه سرمد در مراجع قانونی
✅
به گزارش روابط عمومی بیمه سرمد، در راستای برنامه‌های راهبردی شرکت و با هدف تقویت ساختار مالی، افزایش سرمایه بیمه سرمد از مبلغ ۱۰ هزار میلیارد ریال با ۴۰ درصد افزایش به ۱۴ هزار میلیارد ریال از محل آورده نقدی سهامداران، با موفقیت در مراجع قانونی به ثبت رسید.
⬅️
این افزایش سرمایه ۴ هزار میلیارد ریالی که نتیجه پیگیری‌های مستمر هیئت مدیره شرکت و همدلی سهامداران است، بیمه سرمد را وارد فصل تازه‌ای از فعالیت در بازار بیمه کشور کرد. این اقدام، با هدف حفظ و ارتقای نسبت توانگری مالی، افزایش ظرفیت نگهداری مجاز و ارتقای توان شرکت در قبولی ریسک‌های کلان صورت گرفته است.
⬅️
این افزایش سرمایه، نه تنها پشتوانه‌ای محکم برای ایفای تعهدات در قبال بیمه‌گزاران است، بلکه امکان توسعه پرتفوی شرکت و ورود به بازارهای جدید را بیش از پیش فراهم می‌کند. با افزایش توان مالی، بیمه سرمد قادر خواهد بود ریسک‌های بزرگ‌تر و متنوع‌تری را پوشش دهد که نتیجه مستقیم آن، افزایش قدرت چانه‌زنی در بازار و ارتقای سودآوری در بلندمدت خواهد بود.
🔗
افزایش سرمایه ۴۰ درصدی بیمه سرمد
🆔
بیمه سرمد، تکیه‌گاه مطمئن
🆔
✅
@Sarmad_insco
☎️
1516</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/460899" target="_blank">📅 15:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460898">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/460898" target="_blank">📅 15:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460897">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3EztrAioN778H8tkHRnHcVxeVjbodgexp-5l5VadRXO8FLQ5Bg8bVECbJEUy2NbjtjlJNEaWkITOzaIqwF2PG39khykmihHN_nvUfG6-vO0i_OoEFNIFkad9MCPhEAQCBCgXYYjuHK64jhgljXqXgxrSgb_U2wZWX14pT0Fm7P4-3Tjap6XBxyxcLtO6ZEf46JwfWr9cD2z1UA6_ngz1EX0xanFlHBSZImFtQZpCDGFPBF8LvsajCZ7a6MDiPBNW4dlTxY47SmY86DU4XePPTPXIN0DHaz_OiZC-erU9QAlzXjltiiyKLPPtmR52tZ7D-F_e1SJ46YBMRhH0ykz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عزیزی ادعاهای ترامپ را با هوش مصنوعی به سخره گرفت
🔹
رئیس کمیسیون امنیت ملی مجلس با بازنشر تروث ترامپ که در آن ادعای پیروزی در جنگ با ایران کرده بود از هوش مصنوعی پرسید: ترامپ تاکنون چندبار رسماً مدعی پیروزی در جنگ با ایران شده است؟
@Farsna</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/460897" target="_blank">📅 15:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460892">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fdcuFhcnZdqoNnEGKAVhJIUrwxJtCvRksCo3eRDetHkGiGbvxRnkZDYTGWG0UKTfGDDYjKp_Zke_myhl7fB-39vhs5m23ZsefSX3qKsCNWRXxR-rKwZAioprqUb5e61VyR4AlNqMTqeb9hmkUyD91yXroynnuowM3RbY00y89FHQgQ2T83w2B2d03q64Fu5I9bF-BKmU3Un8lNWigot_HzBaUr7NO1C59JVoN7jrRrpgZwiSNXvv-Gj0s38IcEZ3KcotXVzNkRyIT0iMhsjLyHUUIufp-rsqwF8oxpe0xyMUub-nuvW6zVYO8iK93xHWtK1j-STJDPwah3xSVsgI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1yeLNhprImx9QPV5zMTgdU-ZUNUDz6ciMz6CBytyv-XB4SrS1uxgJ068lJflumExgo4tM3b791qUqUbqOJeGtzaD-aq--OTnGdZPIMYrL-4LA0H7uNfWC2w8VcHFJQCqcL7L8K3JPdlBXLer-Ny6S0pEyU5oH6wLwyHtjWs6ZJGWAqNF8hscJzhTXOxCWdWD7blCkpHPD37RTyhcbCaXjZj7Hlos216V2iNeVfUKRkr4xKHLJ9kiOZiHqYYG1mCQQTImcTnn5kVsYpNJtPufdjCKcIUhd34IyrV08QQK7EOeuS1-z_8BscfjbPRFu7G_1d-z_EM7xIUQo5jdxcSEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwOacFj4mAMef5CArKHaPi9V8qbcukzgmPTdqM-goXnyFzQTBh6XuzU3rUjelJ483sT9mNk0_mwFWiaus48s7GW-9PtLZTzZKKQSf-zrEAfqzodm-0neqI0U4huppvIPIGGTVaMtXyxB1Gt8GjzPZD-qMkCeaRqoCetNE1w-cMbgjhH4YzPVSnBApIqy6kL7yEK0c4HR5zOPdkFTzZSQzyP3p7GAx5ugHoL8QSSQj4ux8vXxUXfTn2pxg86ToGhSimWdK_nxiU7QVTp-lWg7YmVKLSBq0Bf15d86ZJkXW8BOo-08310rn7OisWMCQHlqTlpk8kpoo5lRzYFCQBemgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFecXrIHeIlEtsmETE8bYe1W4JhPt_DAHClhQP_EqMQadgB7lZfr2PJ2n9udo347xo582Z7o5E_DqRRqh6sbXi5pAVrU-90bHZ3S7cx1_yYQR90pMihmMoqu92oRRcvcRM9Zz2pITELgdJgMp_cRPlCsBRBALHlz2O8_4kHUYCY1cihYaYlGAu6q_WPNbzXg2vjGYvi-RYGQoC_qPHC1zHk9iv54-cPCGmqmDQaUR1nDZKLIhZNvJU0S1_2ESXs0OB6-yiXGL_8q3a1wFrVVhdW8rcS2_51MMKpWyC4BuWvybf2AW8hX_L-ntuK0ocmMUCITOHLTKcU2xrg0uET6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLQvMzXUnya479336VNUnR4SQ9s5Hib4mIQ17MaL-hin-lWuV7L8QjJABIW9RGZo1dP_SzK1n4nFWZMkp-8IRzYdYSmZ9kvpMTIPL67AnSOfPb1bI4v5pxeuN_IN2AN5E2RelTiC94OHLjl0RnfMbV8uRKKP-WeHenbVBG3XNboIFHmpe7_bB676AzVifAV1jOosvRGOq_H1ftJ4QQrIelhJ4eU21e4SgXQkTzXYdMVwoJ0U9OSRl-T7odO_uH8nBaLVCg7Ls0Yq_eOJFBEr02rnVWJYOxK6YAiOuOsRHoFVgvExUFWd1SSK6E3uZmd1bt1raRJ-txw8U88HMbAN6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: تعداد زیادی از تراستی‌ها کارشان را درست انجام داده‌اند و فقط برخی از آن‌ها تخلف انجام داده‌اند
🔹
کاظمی: بدهی ارزی تراستی‌ها حدود ۱۱ میلیارد یورو است که ۶۸ پرونده برای آن‌ها تشکیل و برای ۴۹ نفر قرار جلب به دادرسی صادر شده است. ۲۲ نفر بازداشت…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/460892" target="_blank">📅 15:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460891">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/211a9d8eca.mp4?token=rSclPNoCpSqcBnnnszWpcVy4on5QfdDzbKJKVHJcxllUhKNVKesQYeR7g36_aZ-5uXiYZ2UPWEgrY436Lx0-c-QSQ5-XsBOLCKE_cRgxlaCEg1t40l9dMNEHc42RaXxZw-ZrcRxg6cm4eu3Lq-YjWbkgtpbdq3fLSf8D3m0ZPKjfwJbNl11hqVjzQFcREmhJ77vZ0xNS8k7b2ZkU_eVxcJkUPrt3bQ39i59qGmkaXof_673KY-GUckxT3scaEAIejgTxZ84YnBujE9OAbOK95hxOp-L0VwBi-uDOD1rsHbtO-rOSXR-YPtNxBOm3cj4sqFdVXfvmThKXY0oBiZcXyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/211a9d8eca.mp4?token=rSclPNoCpSqcBnnnszWpcVy4on5QfdDzbKJKVHJcxllUhKNVKesQYeR7g36_aZ-5uXiYZ2UPWEgrY436Lx0-c-QSQ5-XsBOLCKE_cRgxlaCEg1t40l9dMNEHc42RaXxZw-ZrcRxg6cm4eu3Lq-YjWbkgtpbdq3fLSf8D3m0ZPKjfwJbNl11hqVjzQFcREmhJ77vZ0xNS8k7b2ZkU_eVxcJkUPrt3bQ39i59qGmkaXof_673KY-GUckxT3scaEAIejgTxZ84YnBujE9OAbOK95hxOp-L0VwBi-uDOD1rsHbtO-rOSXR-YPtNxBOm3cj4sqFdVXfvmThKXY0oBiZcXyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستادگی ایران، آمریکا را دچار سردرگمی راهبردی کرده است
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/460891" target="_blank">📅 15:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460890">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3569284e9.mp4?token=snYDusVtYGUFz2uo-UEOYUX7ooP5hSelad-LgvwwZKZ6W8Yr8HnqtuU2qssibE-Poh6XT2uOflTmfXGm7LNFUsVZheJmna6F8oMdmAN7A4Z1fOr6HxqH6jzHRcydKFctX7dGr5zAqNMfBpe8LWbMXj8m9p8fbG_rpm74RqDct6xo7nWrBjeGWTw_M4bEaQaiIEw8sHBbiaSoeT2X46IibpRcvkclfEMlGKHAdQIw1kcHv4p3LdTF3vs9eClm7rpkQzUCy3w_DkllfSH9KVHhyXB6Av7DKBZqdHS7WCoUx3pKRkUYtRgJa4WIsLnY6U_U6oB9JAsG72JfvcsrOCXxoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3569284e9.mp4?token=snYDusVtYGUFz2uo-UEOYUX7ooP5hSelad-LgvwwZKZ6W8Yr8HnqtuU2qssibE-Poh6XT2uOflTmfXGm7LNFUsVZheJmna6F8oMdmAN7A4Z1fOr6HxqH6jzHRcydKFctX7dGr5zAqNMfBpe8LWbMXj8m9p8fbG_rpm74RqDct6xo7nWrBjeGWTw_M4bEaQaiIEw8sHBbiaSoeT2X46IibpRcvkclfEMlGKHAdQIw1kcHv4p3LdTF3vs9eClm7rpkQzUCy3w_DkllfSH9KVHhyXB6Av7DKBZqdHS7WCoUx3pKRkUYtRgJa4WIsLnY6U_U6oB9JAsG72JfvcsrOCXxoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جهش قیمت نفت بازارهای جهانی را به‌لرزه درآورد
@Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/460890" target="_blank">📅 15:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460889">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a98160603.mp4?token=nIA9YJ1liWO_1hBpm3QxsWEZ_LgMcOKK7sv8sT_606Mzx4j2x6Z-DyvVblix9k90wmS0UXr21Mjp_RwZOVkqp28olJGs1mZjUBUK1k7YDo0wgKacCg8ZsDLVOM-3X1QVNbygYxepJqyMhuEWICk3HlzQG9QVqOdz4HgJWo3qXiw-bvpCzByigVikhc25nvOcsNveI04kVmYkOlgNyHTORLYBSZCnTmWh0P-4XGnLzVwbonu66s-lOmzGLo2onoUeiRieTGvVJ676BFiiHfB_nK4_SP6V9dEvz5-6h-Ji-zEzjN7BiflKQF-ac3MCsJ9suMiRBajYz-DBXV9rJCyMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a98160603.mp4?token=nIA9YJ1liWO_1hBpm3QxsWEZ_LgMcOKK7sv8sT_606Mzx4j2x6Z-DyvVblix9k90wmS0UXr21Mjp_RwZOVkqp28olJGs1mZjUBUK1k7YDo0wgKacCg8ZsDLVOM-3X1QVNbygYxepJqyMhuEWICk3HlzQG9QVqOdz4HgJWo3qXiw-bvpCzByigVikhc25nvOcsNveI04kVmYkOlgNyHTORLYBSZCnTmWh0P-4XGnLzVwbonu66s-lOmzGLo2onoUeiRieTGvVJ676BFiiHfB_nK4_SP6V9dEvz5-6h-Ji-zEzjN7BiflKQF-ac3MCsJ9suMiRBajYz-DBXV9rJCyMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون‌اول رئیس‌جمهور با مراجع تقلید در قم دیدار کرد
@Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/460889" target="_blank">📅 14:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460888">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e68b576c33.mp4?token=B6ZYUre728czCKkCaX2N0VuJxsasn8MXhgk-Au1MhO72R3-f6Xp9y5-26HDVrVKbLGd4asyZrlMBU2yto1yRf954BMY1drE2DGLedHg1mD-o0lBFjCC9iGxzuhtBQIMDnsPocP5V3LV06Sv3yQx42jBftcY70ZcxmmB4iNJGedDjpRXA--xRE7Kg67RMlEm0BDIzw_vuoKfur2VIFfAf9BLet72LmAA5NqC05C1e2FC1hcXIdwwTOnYvw_wYbZNnp5abhz6Bdt0cGdFZH6j0SLv-TgOlP1yZKUb7lQxsPEg5HY8Bv5hV-i8YBOZXOOodQErzdxOSLXVlP9S0mVJFfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e68b576c33.mp4?token=B6ZYUre728czCKkCaX2N0VuJxsasn8MXhgk-Au1MhO72R3-f6Xp9y5-26HDVrVKbLGd4asyZrlMBU2yto1yRf954BMY1drE2DGLedHg1mD-o0lBFjCC9iGxzuhtBQIMDnsPocP5V3LV06Sv3yQx42jBftcY70ZcxmmB4iNJGedDjpRXA--xRE7Kg67RMlEm0BDIzw_vuoKfur2VIFfAf9BLet72LmAA5NqC05C1e2FC1hcXIdwwTOnYvw_wYbZNnp5abhz6Bdt0cGdFZH6j0SLv-TgOlP1yZKUb7lQxsPEg5HY8Bv5hV-i8YBOZXOOodQErzdxOSLXVlP9S0mVJFfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افتتاح کارخانهٔ ریسندگی با سرمایه‌گذاری ۴ همت در
قم
🔹
این مجموعه که با حضور معاون‌اول رئیس‌جمهور افتتاح شد، با مساحت ۹ هکتار زمینهٔ اشتغال ۲۵۰ نفر را فراهم کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/460888" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460887">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d48a6aa307.mp4?token=TADKoWE73rWTCDihSv3mpqwzR6-sx90vvAUGN6KCt5-FOJouiDIYv3IFxMBOdqeiIccoQ0Ya20oZFoTkKo-ejtUK3eBb1QP9hGQo2C34OI_77b0CaIlOmFAgAOV7fJN06jZk6c0AjNCmFI5fKPwiNDpwuOyKTHZVvzt8E5OLSADAAgE8YoII_4Nyn6ctbRd5L59lyX3OTJGDerB8LxKRYV8uMn3jkrdDb1_IGJyRlCsMqAFwgQc3vQ8iETlgr8QKXwiTivNkTI2jnWHVi1q3xXQPEkZu-VWNRTkrdaqtbG9sEfPJi561q4Bkn7SzGOOa8WeNmDr47BlxLF-irpfiNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d48a6aa307.mp4?token=TADKoWE73rWTCDihSv3mpqwzR6-sx90vvAUGN6KCt5-FOJouiDIYv3IFxMBOdqeiIccoQ0Ya20oZFoTkKo-ejtUK3eBb1QP9hGQo2C34OI_77b0CaIlOmFAgAOV7fJN06jZk6c0AjNCmFI5fKPwiNDpwuOyKTHZVvzt8E5OLSADAAgE8YoII_4Nyn6ctbRd5L59lyX3OTJGDerB8LxKRYV8uMn3jkrdDb1_IGJyRlCsMqAFwgQc3vQ8iETlgr8QKXwiTivNkTI2jnWHVi1q3xXQPEkZu-VWNRTkrdaqtbG9sEfPJi561q4Bkn7SzGOOa8WeNmDr47BlxLF-irpfiNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: ساخت قطعهٔ ۱۱ پارس جنوبی برای تولید گاز شدت گرفته است
@Farsna</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/460887" target="_blank">📅 14:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460886">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">موافقت نخست‌وزیر جدید انگلیس با تداوم همکاری‌های نظامی با آمریکا در جنگ علیه ایران
🔹
بلومبرگ: نخست‌وزیر جدید انگلیس، استفاده از پایگاه‌های نظامی این کشور توسط آمریکا برای آن‌چه لندن «حملات دفاعی» علیه ایران می‌نامد را تأیید کرده است.
🔹
این اقدام ادامهٔ سیاست…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/460886" target="_blank">📅 14:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460885">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0eb975e0e.mp4?token=BwhYHUy0S6lgihzqB_8DR29SdTjxCo8RQ2Yy_n6ckB4owpKr9rGiGvPQnX0Q7Kdi--xmp30pE_FAUrI3tybVP460tBjYnJOoCMcRvN_YalQKdi2U_1UO4oP5C7l3UcsRL9X98y_KGfRul_I5aDTmC6NhrRaY0a9fEs1N5Pzu42fbxWqteIiGCf8xu1x_xfKen4LOs9V3rwK1FhbIIAanqib79OB3we9ncIgTMlAXAve68OqaPQ6-JXnf9jiQky3mosfuWtVUwYcEOXpTqHMDUPiHry9gDWP9YSH3ne78KKj8-x950DQa5_7dZ-WoHbEE5spVR5hHkEzvb3qp56TCGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0eb975e0e.mp4?token=BwhYHUy0S6lgihzqB_8DR29SdTjxCo8RQ2Yy_n6ckB4owpKr9rGiGvPQnX0Q7Kdi--xmp30pE_FAUrI3tybVP460tBjYnJOoCMcRvN_YalQKdi2U_1UO4oP5C7l3UcsRL9X98y_KGfRul_I5aDTmC6NhrRaY0a9fEs1N5Pzu42fbxWqteIiGCf8xu1x_xfKen4LOs9V3rwK1FhbIIAanqib79OB3we9ncIgTMlAXAve68OqaPQ6-JXnf9jiQky3mosfuWtVUwYcEOXpTqHMDUPiHry9gDWP9YSH3ne78KKj8-x950DQa5_7dZ-WoHbEE5spVR5hHkEzvb3qp56TCGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رایزنی‌های وزیر اقتصاد در روسیه برای
توسعهٔ
روابط تجاری
🔹
وزیر اقتصاد: توافق‌هایی با روس‌ها انجام شده که می‌تواند گشایش‌های تازه‌ای ایجاد کرده و تاب‌آوری ایران در برابر تحریم و فشار را افزایش دهد.
@Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/460885" target="_blank">📅 14:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460884">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ed4cZj2WxypHq31znxMWFVTudyrNBkoxarMI5pz9_OWYdN9V8mtVg2jzwqj_sEdfhbPhSnGMSbhDM-qenNDl_vOy6N8FSTbFHHNi2i6L4MfOIbbLmXdG_AL-dxb0Pwy2SImBOO78RBrmCZQinNlM6XQe8Ud7fLWpIVV4jK93nvrbAxoMCDN38i_vb_mVLEcjL2Zm8jVf3t2uBPXl-WCB12b8JaUNSRL8ypXYvAW7d_tf3avjVRKOU_v6CyU0oYexPE_4a5y1qtF9IP6JhmfLBuOyFF5znoRzdcUVjtvEgE-vrVNbAoGwtNiXH4hlUZIW7eZcam2cqLlgmC2brB65vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان غذا و دارو: واکسن آنفلوآنزا هنوز توزیع نشده؛ واکسن چمدانی نخرید!
🔹
سازمان غذا و دارو اعلام کرد: واکسن‌های استاندارد آنفلوآنزا از مهرماه وارد کشور و توزیع می‌شود؛ با این حال، در حال حاضر برخی دلالان اقدام به توزیع واکسن‌های چمدانی در میان مردم می‌کنند که بدون رعایت زنجیره سرد و نظارت‌های کیفی، در بازار سیاه با قیمت‌های گزاف عرضه می‌شود.
🔹
قائم‌مقام رئیس هیئت‌مدیرهٔ نظام‌پزشکی تهران هم دراین‌باره گفته: واکسن یک فرآوردهٔ بسیار حساس است و برای حفظ اثربخشی آن، رعایت کامل زنجیرهٔ سرد از زمان تولید تا زمان مصرف ضروری است. در صورتی که شرایط نگهداری و دمای مناسب واکسن در طول مسیر رعایت نشود، نمی‌توان از اثربخشی آن اطمینان داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/460884" target="_blank">📅 14:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460883">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f6d0bb2e.mp4?token=J2A5BILV4jbc6P91Ye5IlP3HkMxiIguRjiZ0XSxc2yI77avzT6pbJIBGRTgo7feDeR_mDJIW_4DLKMt5-N_xPiZp5hk55xyuHsSipykUIvyVq6036YPaAT8jbgXOZ5RUzQJLGC9JarghTl-us-RPNPqdZPxylRhKu5AN9hnAMmEuSbtlPePK6rEy0D-kJT_LH5VTxMEtyivQNHLvYQ7Fda9OMvBiu5YIhAzQc9U2HUlScrB2JLGJQ_hSco9Y-AHD4oNDjMNjZKgcYrm6Pzg97mEIdssj6i66moplJnXw5y_PKibqkT0aCGn5CRw15EOaEXvX594q4P95LCmAMlZgDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f6d0bb2e.mp4?token=J2A5BILV4jbc6P91Ye5IlP3HkMxiIguRjiZ0XSxc2yI77avzT6pbJIBGRTgo7feDeR_mDJIW_4DLKMt5-N_xPiZp5hk55xyuHsSipykUIvyVq6036YPaAT8jbgXOZ5RUzQJLGC9JarghTl-us-RPNPqdZPxylRhKu5AN9hnAMmEuSbtlPePK6rEy0D-kJT_LH5VTxMEtyivQNHLvYQ7Fda9OMvBiu5YIhAzQc9U2HUlScrB2JLGJQ_hSco9Y-AHD4oNDjMNjZKgcYrm6Pzg97mEIdssj6i66moplJnXw5y_PKibqkT0aCGn5CRw15EOaEXvX594q4P95LCmAMlZgDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جانشین فرمانده سپاه: نیروهای مسلح ایران کاملا بر تنگهٔ هرمز مسلط هستند
🔹
رزمندگان اسلام با آمادگی کامل در مناطق جنوبی و جزایر خلیج فارس مستقر بوده و اقتدار جمهوری اسلامی ایران را بر آبراه حیاتی تنگهٔ هرمز اعمال می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/460883" target="_blank">📅 14:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460882">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1XoXMHAN1gVZv_BN9XeZ3vq1Cw91vK5-t9MzplOVca_Zx6UIoaelA4DvqtauoOy4wffD5VdSjNGK_76PSbp-nfY93IVa54e-2CID6K982T8LknzACUzw0PukUQSqTp26Ki3Gkv2t5FcUGLcRj8qXIg_BeYMQhF9h8BlmxPSfW6BftLDbaj8Pwf4WaZlfCbTnmfbLJwOPH-ixyUl74EZ0HYQhBsRu6cL1O7ZRBMEioITsgWj4tkXqW3LgEYsIUbz7cFcHEH8EWHviLrFVwdZ6L1vk5UGCRV1R4aY6DKK9zb693lCzmjrtEor9saNOl03HRv_8yMziU5y86xUpmDM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلمب ۴ تالار عروسی در لرستان به‌دلیل تیراندازی
🔹
دادستان لرستان: درپی تیراندازی‌های غیرمجاز در برخی تالارهای پذیرایی، ضمن پلمب ۴ واحد متخلف، عاملان اصلی این تیراندازی‌ها بازداشت شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/460882" target="_blank">📅 14:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460881">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb104c959.mp4?token=Qfjw-EGfYmioNK39n_UV-EaD1EqyllLytdPZwvsPCwEelSNgzM7M9NKYsdC8Z5yzcyX08LSihrweEe42RlKvKWBtxOerYfBFKqokvCg0PCHRNbj7q3o7Dczu3rmj4UbExKYNm5zWVOARXLgKgP1HkuepivM_UAMaXywM1svdU9vC8WrqWcXmfQqlp9i99ijjY-geOgMlLA3UW3y7veOZcMgbNIEnQUYCqmQK-y5nL6qnHR6tgGmyvtbtMGePWYJP_4vYMN1ozLGEJq_ViRlL5wvE_Irh7N0mfzxp7gsYDAv1fDaErKRemVS4hw4em6j1Ui2nhej9hOIeQF6A5LOtbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb104c959.mp4?token=Qfjw-EGfYmioNK39n_UV-EaD1EqyllLytdPZwvsPCwEelSNgzM7M9NKYsdC8Z5yzcyX08LSihrweEe42RlKvKWBtxOerYfBFKqokvCg0PCHRNbj7q3o7Dczu3rmj4UbExKYNm5zWVOARXLgKgP1HkuepivM_UAMaXywM1svdU9vC8WrqWcXmfQqlp9i99ijjY-geOgMlLA3UW3y7veOZcMgbNIEnQUYCqmQK-y5nL6qnHR6tgGmyvtbtMGePWYJP_4vYMN1ozLGEJq_ViRlL5wvE_Irh7N0mfzxp7gsYDAv1fDaErKRemVS4hw4em6j1Ui2nhej9hOIeQF6A5LOtbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارتباطات: تعداد مشترکان متصل به فیبر نوری به ۲ میلیون نفر رسیده
🔹
توسعۀ فیبر نوری در کشور با سرعت خوبی درحال انجام است. مصداق آن هم آنجایی است که در ابتدای دولت چهاردهم تعداد مشترکینی که متصل به فیبر نوری بودند زیر ۴۰۰ هزار نفر بوده، اما  امروز بالای…</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/460881" target="_blank">📅 14:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460880">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
۴ حملهٔ هوایی رژیم سعودی به مرکز یمن
🔹
شبکه المسیره از ۴ حمله هوایی جنگنده‌های سعودی به شهرستان «الجوبه» در استان مأرب خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/460880" target="_blank">📅 14:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460879">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54be1ec368.mp4?token=txEfUmSEz9SOGQKWwfsD8Sf761imu4YspgcjgEvBEsQUJ2iJJh4QzMafkCqoD1hFxXGd1TKNRvhGhOcoBDtiPohd4I3g9vORXvj7mVYYb5OcIRcKM4FZCnItK-2SndYK1YaEqv_mwJK3CWfF2qhAMJHMVG4QuuZBqOr-PC2oZ7LVJUWujKaT2D1PkA029y-f6dnBEBA3vafMidhGx3UEz32sHctAx0qD21FPsCsImFTIjepk-KUKvh2Xm-wT8H9-ERS4mgtPvouoPxQ_Vks8dEP6QvDc6Llxa7Qrb50kRAHAuQF_PGhIL4aq8KVnC3KvFIoLFSzQf7wu1PnphX1XBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54be1ec368.mp4?token=txEfUmSEz9SOGQKWwfsD8Sf761imu4YspgcjgEvBEsQUJ2iJJh4QzMafkCqoD1hFxXGd1TKNRvhGhOcoBDtiPohd4I3g9vORXvj7mVYYb5OcIRcKM4FZCnItK-2SndYK1YaEqv_mwJK3CWfF2qhAMJHMVG4QuuZBqOr-PC2oZ7LVJUWujKaT2D1PkA029y-f6dnBEBA3vafMidhGx3UEz32sHctAx0qD21FPsCsImFTIjepk-KUKvh2Xm-wT8H9-ERS4mgtPvouoPxQ_Vks8dEP6QvDc6Llxa7Qrb50kRAHAuQF_PGhIL4aq8KVnC3KvFIoLFSzQf7wu1PnphX1XBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارت زرد مجلس به وزیر ارتباطات
🔹
در جلسۀ امروز صحن علنی، سوال علی جعفری‌آذر از وزیر ارتباطات و فناوری اطلاعات با موضوع پوشش‌دهی ضعیف تلفن در جاده‌ها و روستاها، بسته‌های اینترنتی بی‌کیفیت، بلاتکلیفی بازنشستگان مخابرات، رهاشدگی فضای مجازی و بحران تلفن ثابت مطرح…</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/460879" target="_blank">📅 14:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460878">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1KaO-AD2UanqTwhmvZMpSaRSPUI3BnE_iKrfUmDH4idwuaTJmeeywmGxe8K7Dnx5NCoSVAMhx4q19Q72wv_Tmb3nQ3goARXaFwRB2qNfO8Q5K-kUGzIWjIrH1VrGGJh1FsVaIDUCqxwQvjK9Vq2QdLCL_SI0wrDeiTxoAx54ZpG6Bs2ZHRLsKfzdrObP3PjODkilYH-1fYr5BI4nIhU3-bJMBDEWKSAzhFUhOEcmHr1b5autS9-tJ6SU4HBwwxaXhUvXZ0-RBRYZwR2MnDxR6i36efuR5NoWVijwOaJc0jUwQGxdQ5CquXfBEFjlPg9rTtUxEXqj2ET6ZTrP_Q3jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار هواشناسی برای ۱۵ استان ایران
🔹
هواشناسی: برای ۱۵ استان کشور هشدار هواشناسی صادره شده است؛ در برخی مناطق رگبار، رعدوبرق، وزش باد شدید و گردوخاک پیش‌بینی می‌شود.
🔹
همچنین برای بخش‌هایی از گیلان، مازندران، غرب گلستان، کرمان، جنوب سیستان‌وبلوچستان و ارتفاعات هرمزگان هشدار نارنجی صادر شده و احتمال سیلابی‌شدن مسیل‌ها و طغیان رودخانه‌ها وجود دارد.
🔹
در نیمهٔ شمالی کشور کاهش دما پیش‌بینی شده و دریای خزر در ۳ روز آینده مواج خواهد بود.
🔹
در تهران نیز امروز آسمان نیمه‌ابری است و در برخی ساعات رگبار، رعدوبرق، وزش باد شدید و گردوخاک پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/460878" target="_blank">📅 13:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460871">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HC_TWc2bwt7JDA1th-uLf7xEY3YBesRi5UPvMwx79UpzHjABWP_bYK_zC9KfWzhfbEHg33x6lOnZh9CRWpGf1Z-P7MzpOvwJ1egd1nZoofkCuIzZdzwd6TPS5T2dedSoU2LcM82ts8v_3h68eu8OkJ-EiQnPjWa-R7kZ4X__K5JtwCQHqQq9W1xyUQcaU9yTlbheAtb1Qu-nkD5vevPo9kPeLkZmPPEKkLfgbwzzisE4veFElShbq3N4XC0mDDQ-Gzye_wEOktAO9baNLjvJFHY5-coZkPvN8PruZTIcreEI9dSrAJcoEXzy481lM_adRIdVoaqkO9132CWEomkHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N5Wa4lNq68FFlIywuBD0nwvwlqX9K3LD_a3d2oQE713HSx7SSllsOhBVPot0uWY_sC_LgMrM5r3DCIFMJ2scKU8XPItBxY18l9KVXySg6JnWJAyaLNiD2fMWIHLJd2xtKTH4YUDyhMcAcAqmt0aYzn4iUNnAuxvM9-21aeC0dqi6CE0rzS7FgkpGk1JUSEG5l7FaHB7Lu52r6Dq5lcrYrA2F5pGmI7vYYzYFGNASypa8YYS-j9AAiDCvh8xyENNyWp5otQLZ8-FEgU12UqlTtnPTVS621IRHCtwBjVb0zqQmWAoZGGC1V-LVPkUa2wK_ZFHFwd8LfnkMdnCxoQ-qsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J03rUds65wOOVATD26Ta0IXzzxrsq3qvhFHyU5Sirw8H_FQ0Fpl-D1qV8obIHV0lfnNm-jqbRUhJjp43Sy2lgx3GzdRuKbXv19LsPUy6XAC5O0ttyC6map3Q8SCDTpmAY6oOJ7xwDBCZRBnhHc0zvDZxWjk21_4bAwmH1seeLfgfC8WplXA-tGZhM8X54tgwHuz3-1Qa4h4ZZWKwEA-4f6o--UqStJevRyMrggU-biulvWCjUYEEVxpLxHCEbB_RLcn2GnW0nwozkvWzebB37kWyZmmRgP_2aGQuJpcrVzHwL5SjfuL6QgPgfbTXgc5p8vUqcIvvOlx6dhatrXup-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anVU1CLdwiptaoH1_uMzi5GDFUqO7mqOiplQ5MRHk0vyGaSyVNBN4h7STT67uIcsCLCuhWOfWmaxsydRAbBPXUQLVDL4z3kiaiEaahsTb5m2wfLOgFofkDFXNe815pSA2X3eiWrlvtDWTO9g_EEPjot0RHQ54aLi23oA42uiQhXF7m3CbQPCxad8z7jmyaL6pkddN0Pwmpw2eZWxSE_2eT7yZ1lMkbQyVftbVZvwviHzNU-UILdp0zc6LHZb-psZdJPuIMX3kW3G44P7O3MuCH9RcbQsz1z-Izu4hxWHodh4PJsmrhOGvXdmosYDYMnWVJ78LXD21r_Fl_cm9iDHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCYduqncxAZ3yl8GCQ6mu4o0cYZoHbVfR0SAkWdyL3BsWCdd-DpUHG0qR3S-EoA2TvfEW3I_PjT9jXhK9LM6CyQ34YOFgl7_UOl2XroLJ-NxVIYZGfyNZEugLAcm4NItv9-SjxWv6Rz-3cycSsow4qOg_in2Xndgy3xNn4NmFxrT75bKszQIRj_vyy-hUThaiL6avjqqyCn6R-YE6FVElEcBOhbprHVgeYuRH4KoDlg5sqh3-BSJ1lvKtHLeWCrzXpxQQLbOq0RasctPs7W5yOhCBw0n2y6Uw3rBZ8cZ3L18sdrmmHd7JakzDkk0aE-v0__0pcNX6QHoUSYP31LMKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQXfilMSBJ51EIzTnsz0UGyaNeE57WJALmvrRL_lsSkh-pPblC67ce3YxFbrhNJ9Z2ZLdKVHEyNoKDNM1WPE2zSjJX7jZQyoiiJO2AhO4-rliMl0y8GqV2cIT5M25sGjgS0XLm5EiCCgRkbtqvOYDbu1w1ztcBbr5K84HafZY7Hqk15oSbchNEgb2gPZ2jn_KTcC-aSUujk0c0-GHVXF0LhHF7F3qLY05lStulJ2HU4BFCMholrcAQ8l6swFmVpTeyzjLxDjdaE8aYelrmolyMWpxWnMNQkttBJRQweFq8-ozTc89tZHpiWJeQuL006IhHbOy-lLyDoYVSpTJ5PGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6LQqSEBf-KXbpv8hGe0b-TsXk5AIWAe9Fm7l8EIHjxxq6SEwDQBER39XT01S5e2V5dBBx2UUSe0hdaHMNEgVcUcr7TO9paM-AxTkukLlfl_VDTnrl8ilzuMhHWsD0QwIw9xg45Ctp3j8XzLhGCvC7mEDq7jNJ9_-sSfrw3oeC44icjrmZrZkzxaiPhJ0eKKX9Z_MhVaJ6-in8qta2txk8e8bqCGOWnI6Ell2F4HzCtuhSZVgWrhQhrE6XDIHlyAqBzDsU3SLdhyWkese9wLHGskivAtciXDU5yJldravDVnlEaORDhTBbdrxZ_ShaqfH5XBJ95vTeWJ9Ugs1VdNcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: ظرفیت حوزه‌های علمیۀ بانوان باید در خدمت حل مسائل فرهنگی و اجتماعی قرار گیرد
🔹
در بررسی ناهنجاری‌ها و نارسایی‌های امروز جامعه، باید سهم و مسئولیت خود را نیز مورد توجه قرار دهیم؛ چرا که مسجد، مدرسه و دانشگاه در اختیار ما بوده است، اما نتوانسته‌ایم از این ظرفیت‌ها برای انتقال صحیح و مؤثر مفاهیم و معارف دینی بهره بگیریم.
🔹
باید ظرفیت‌های موجود در جامعه، به‌ویژه ظرفیت بانوان و نهادهای دینی و اجتماعی، به شکلی هدفمند و مسئله‌محور در خدمت حل مشکلات مردم قرار گیرد و از این سرمایه اجتماعی برای ارتقای کیفیت حکمرانی و تقویت انسجام اجتماعی بهره گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/460871" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460870">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4_N0PAZGUDtC4yUPN-DLSO17Sqd5UBMG1X2w75mYPuV4GbsHQmzPf8sxWt2uLIZF3CwJV8U-1Q_pM_tAFdAdQeWfUyXzmP5LLp3UFEGeYKyDWcn6hl_uh40ekoCVu1uHQmJo8ZunMunN0DYm66KAsKHWZfqsxMtqQEQO-fdrKUCq-iB4XyVIEV2YjNoC8UnbC7VTCYBitfHV4Pv2d9k71xccCUNcqYZjhCqcR7qcssm0hWlX5fSwiofN565gAeQ__FJFLfQaInbjiAMNt6XE8iZRK_xsYxA81tK_nr9hj5RAIOlYD7K6pKyucsT4uukT9B_rx869ugIxe9bk2Y5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بسیج اساتید: علاج کشور در هتل‌های وین و اتریش نیست
🔹
میرسامان پیشوایی: دروازه‌های نظامی و اقتصادی کشور از طریق علم و فناوری گشوده می‌شود و علاج کشور در هتل‌های وین و اتریش و این موارد نیست؛ بنابراین نباید علاج کشور را آنجا جست‌وجو کنیم.
🔹
علاج کشور در…</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/460870" target="_blank">📅 13:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460869">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQnlbzr_4JCGGPQVM0VNIw1sucuuezPirnreg4L9io9qLLgGoo3S_zF_AcZy5LGIpT4L0KXHyAme1F0oGjAaWKBzTLksuTGjLasw1caf3A2gbSi1SiszkvfDg0FlU6J_tHCOl8Fp1aYI0gkEcPrBCSufSbyUHh6KS8HxWi-4zGdVK9RBLdpzqWTVvkgOTViKoa7VYEGKTojdXRsRr7Q17PpKe8gpoY59Qq4nvB8fAg6BVgzjxTXXekLzr-OTxX5IEy9GP3CYH9dEfw967kAzolSD7eUlCXimR5Zo5eu9YO1iU2SyFBK8WFdBStRg9KRH9LgkbzMnM9maHic3sV9mRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رئیس سازمان بسیج: ان‌شاء‌الله امسال ورود ما به دانشگاه با جشن پیروزی مقابل آمریکا و اسرائیل باشد.  @Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/460869" target="_blank">📅 13:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460868">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4zxCszgeCTTHUPmNVnAMPegqKcueElLLj00MIRvOGjGvbpGOM73Pk_LXOnNGFDiHLP99pLbwjz83bSuxHHbThz1I7o1dDvRFyCHqmh7jg0SecwuJ0tYSzcdZGSXyjuSgAWUMx6NUOcgHOHEKB7j2sdZnv73oiQoN449Dv9nlVuOYxlHFXCSGHuZ2JVFBU_9959FqVz4LpjNGhzatMTseqXhyeXQubguAbTPJhpoMxYP72H2cXthB_EmohemUReiNv5xEMk1MYi0JS9nUH3dfAXEvNxhTz2Hg-KFnfJkJx4sCE-mNWLcHQiKzOGn4hHX2I5Zflm8o25bUejerAy57w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی در تماس با همتای ژاپنی: وضعیت منطقه به‌دلیل نقض‌عهد آمریکاست
🔹
وزیر خارجهٔ ایران در تماس با وزیر خارجهٔ ژاپن مسئولیت وضعیت تنش کنونی در منطقه را متوجه نقض تأسف‌بار تعهدات آمریکا در چهارچوب تفاهم‌نامهٔ اسلام‌آباد دانست و گفت: «راه‌حل ساده است؛ بازگشت و پایبندی طرف آمریکایی به تعهدات و امضای خود در تفاهم‌نامه زمینه را برای بازگشت به وضعیت عادی فراهم خواهد کرد».
🔹
عراقچی همچنین با تشریح آخرین وضعیت مذاکرات ایران و عمان دربارهٔ تنگهٔ هرمز از پیشرفت قابل‌توجه گفت‌وگوهای دو کشور برای تعیین یک مسیر موقت تردد در تنگه خبر داد.
🔹
موتگی، وزیر خارجهٔ ژاپن هم با ابراز نگرانی از تشدید تنش‌ها در منطقه، بر ضرورت تداوم رایزنی‌ها و هماهنگی‌های دیپلماتیک میان کشورهای منطقه و کشورهای ذی‌نفع با هدف برقراری امنیت در منطقه و تردد آزاد و ایمن در تنگهٔ هرمز تأکید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/460868" target="_blank">📅 13:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460867">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b40c83147e.mp4?token=lcX2-93C2sd8kmP62UpwDr78UyApZN2P8DrHH_va2HgACDDa-NBhvxACN-7T967EZfH5_lUa2x8by1RwqHi1eea1zrd1Qb4zjenh6-Q-l6DZeYC0tR4A5PAweKWSRFx52V7W82LB1ZeifEsDDNkKaRVx8rnBmglqYLlgZnhvDlddxdTNsk6EexIUMr1HdV760d-F5Llh2NZvPxbUKMMPipa22w81nAvWYs0AmZrslsHsnqau50rEFHIxRJThtDmrFZe-UtHF-_NqcWJXX6pMZfN85XoyWsiMA8juwp20iMQ0wjNZfpACuqs2Hg96s2nzGS5-XW4CSXS7ub31qY_ivg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b40c83147e.mp4?token=lcX2-93C2sd8kmP62UpwDr78UyApZN2P8DrHH_va2HgACDDa-NBhvxACN-7T967EZfH5_lUa2x8by1RwqHi1eea1zrd1Qb4zjenh6-Q-l6DZeYC0tR4A5PAweKWSRFx52V7W82LB1ZeifEsDDNkKaRVx8rnBmglqYLlgZnhvDlddxdTNsk6EexIUMr1HdV760d-F5Llh2NZvPxbUKMMPipa22w81nAvWYs0AmZrslsHsnqau50rEFHIxRJThtDmrFZe-UtHF-_NqcWJXX6pMZfN85XoyWsiMA8juwp20iMQ0wjNZfpACuqs2Hg96s2nzGS5-XW4CSXS7ub31qY_ivg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طائب: هر استاد یک بسیجی و هر کارمند یک بسیجی را باید شکل بدهیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/460867" target="_blank">📅 13:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460866">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVQxFBL5a6TxBSAVVW81bdDAauzWXGOjA2suJXnv7w5nfUAK4cRFhn_8cX3A5yjD9u_tuPtcxonYeZKbTi5WmoMi3NxjY3jfXS6BPcnbbjrkhWo7DSusUbIqV7tXqIAJxgNL8Z6PCh2-P-kBqDdJe-y4u_y_4hDHdsijbSHDhP48QCgzOLjCOBz76jFj8n2fetymqpfnA7gby0vIEpukW85X8e7ZNDI6ogFpw4IjK0Dp2wpRFTm45Zgyb--uET6BUADIEmsVAlser9vpUPDum_m2aAeZ7y98pyZvnCKWI7_UFEToSjTKMzGLJcOoVjC439IzBIwpKsdY5RpfBlwB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: ایران تا پشیمانی کامل متجاوزان، با قوت به مقاومت ادامه خواهد داد
.
@Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/460866" target="_blank">📅 13:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460865">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31884a3da2.mp4?token=N87CvP-GTTYxDl7BRG_mm-utGonxEsKWvw0JhNu7-vkxBMMjgSCqlwfxQQja_4ePRhORA-bz0XuWH9hvp8eJfX_bAxSxSJimcw1Xp7d4rTzFug6J2AcCibd9YS9fmGhV_RlVPnBTQRc16VTNlycHpuJAZpYclONiqKXtlwBn4LF4oO-EbRRzYsjzZQsGaMnqkhFWKDpa_qpndfxPKHe8SUrpiZqqrJhHuxwXd0gYTZgwkrq_HtcSpkrKiwfGFLQAQNZH2vwM-k_PaaqY2yvtC36e8QVQabzGtfvd8iTI6MyUYjn9jNkRuTE3civP8DId4Uc0dju-zJI6bw4BrM1vMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31884a3da2.mp4?token=N87CvP-GTTYxDl7BRG_mm-utGonxEsKWvw0JhNu7-vkxBMMjgSCqlwfxQQja_4ePRhORA-bz0XuWH9hvp8eJfX_bAxSxSJimcw1Xp7d4rTzFug6J2AcCibd9YS9fmGhV_RlVPnBTQRc16VTNlycHpuJAZpYclONiqKXtlwBn4LF4oO-EbRRzYsjzZQsGaMnqkhFWKDpa_qpndfxPKHe8SUrpiZqqrJhHuxwXd0gYTZgwkrq_HtcSpkrKiwfGFLQAQNZH2vwM-k_PaaqY2yvtC36e8QVQabzGtfvd8iTI6MyUYjn9jNkRuTE3civP8DId4Uc0dju-zJI6bw4BrM1vMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بسیج خطاب به ترامپ: اگر نیروی دریایی ایران را از بین بردی، چرا هنوز در تنگۀ هرمز می‌جنگی؟
🔹
طائب: دولت آمریکا باید به مردم خود بابت راه‌اندازی جنگ با ایران پاسخ دهد.
🔹
طبق نظرسنجی‌های صورت‌گرفته در آمریکا، ۶۰ درصد مردم معتقدند راه‌اندازی این…</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/460865" target="_blank">📅 12:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460864">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7010c9344f.mp4?token=gqP71Xj1HZHKrxI63lqxyH2erZ6jwb9IxinLj1qEO5fhgvNTTYQ_pYv1caG4dRkYjB-MZuFz6-Er7Hn26PzAAK-1jZzlQQZ-530heJ84Vyg0x2w_eULZtIqan0qBTEk5ACHIjHzL2Ik5v-Hprs6Gx8cZK6wjHMvaAiheSyzO6dZpNyP8d1yR_Zv3d68X7krDcYrRzTqIFNDN0qTWPZZSdYkZ14porPPcm_7Gu_EfAjn68YUdS9IG_rpQMpj9e9WJ0VcsdWGVSYQAoXvNM3vumWFeLFvaXuiZhdfKIAcrdYPXyiXxtJW0jKPkM8kBYSgIdeCj-yWfBr25uEV_petWEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7010c9344f.mp4?token=gqP71Xj1HZHKrxI63lqxyH2erZ6jwb9IxinLj1qEO5fhgvNTTYQ_pYv1caG4dRkYjB-MZuFz6-Er7Hn26PzAAK-1jZzlQQZ-530heJ84Vyg0x2w_eULZtIqan0qBTEk5ACHIjHzL2Ik5v-Hprs6Gx8cZK6wjHMvaAiheSyzO6dZpNyP8d1yR_Zv3d68X7krDcYrRzTqIFNDN0qTWPZZSdYkZ14porPPcm_7Gu_EfAjn68YUdS9IG_rpQMpj9e9WJ0VcsdWGVSYQAoXvNM3vumWFeLFvaXuiZhdfKIAcrdYPXyiXxtJW0jKPkM8kBYSgIdeCj-yWfBr25uEV_petWEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بسیج خطاب به ترامپ: اگر نیروی دریایی ایران را از بین بردی، چرا هنوز در تنگۀ هرمز می‌جنگی؟
🔹
طائب: دولت آمریکا باید به مردم خود بابت راه‌اندازی جنگ با ایران پاسخ دهد.
🔹
طبق نظرسنجی‌های صورت‌گرفته در آمریکا، ۶۰ درصد مردم معتقدند راه‌اندازی این جنگ ارزشی نداشت.
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/460864" target="_blank">📅 12:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460863">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8ZFWDX2boJP4I6mGwEvLz-VpA9xR9OvUJ6IXOdswuGQk66lr_e_hLKcVctdR32jGioDaUz8sTSNXQLPtryUao-1qAOKKb5kqCr4dvX9dbFxpb2iIxxsUdXiMf54h7w8pJY-Hf5hevCxtNmpTalL2pzrK-QNne3jYFo3xvp97bBdHq5fxjcbBq5BRytSMSWU-rHCJVRMq4K1uPWoV8l-29F5pBX0KfrlVvs3pTlfumAK_qCe3sjlLLpIVmdYNbgNgARUGSxo5ewD5Y7LF2A3cYIfc9LsZB6HxGqsV48K4WgQiB44yN2jfkgV-tLuuhaXvOIx-X6Kt5aZ-tKSQsrCbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس امروز را ۷ میلیونی تمام کرد
🔹
شاخص کل بورس در پایان معاملات امروز با افزایش ۱۶۷ هزار واحدی به ۷ میلیون و ۷۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/460863" target="_blank">📅 12:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460861">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc7b914dd.mp4?token=ecu86_GkuzxAV_yax-OgX3tGT7MelLZI1RbSwCB-Z_XQFGQsZnbhe1A7knurV1nddJ27oDAGN6FZNMWOpLbAwrNHv_363hE9lrBg7s9etJ0B_0JAx_DGfp0ezHP9cipV2uR3aOFOMrDlsPSUWbteewrDV7SzCPT15vgZAl8crZYJli6DMXPY7R_uLgU0ZlcUKH0pErz7gZ5WofpxaXWtgoPNu8DkTwIznx-lgrkhf5fZDrG9KNuBnSdo5xGUtiO9zevMqd6D_p1ujB1YtfShmWfHn9OeS3ZuZ-fyeECFvZYgWuYgD75CWXfegHXrrnEWEROxv0JF82OipDxklc5Isg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc7b914dd.mp4?token=ecu86_GkuzxAV_yax-OgX3tGT7MelLZI1RbSwCB-Z_XQFGQsZnbhe1A7knurV1nddJ27oDAGN6FZNMWOpLbAwrNHv_363hE9lrBg7s9etJ0B_0JAx_DGfp0ezHP9cipV2uR3aOFOMrDlsPSUWbteewrDV7SzCPT15vgZAl8crZYJli6DMXPY7R_uLgU0ZlcUKH0pErz7gZ5WofpxaXWtgoPNu8DkTwIznx-lgrkhf5fZDrG9KNuBnSdo5xGUtiO9zevMqd6D_p1ujB1YtfShmWfHn9OeS3ZuZ-fyeECFvZYgWuYgD75CWXfegHXrrnEWEROxv0JF82OipDxklc5Isg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جاده هراز پس از ریزش سنگین کوه در محدودۀ آب‌اسک بازگشایی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/460861" target="_blank">📅 12:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460860">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291f3357ba.mp4?token=F3ghmF-NkVmsYvt_ulkl1u8fGJ7u2nSjGlRglXF0rfWxfLJ27y7CUum2YJT102_ArIJzjV-ny157zE43x3QG2bX6bG6pA0PTVMskzbutME7GySc9hkhk2sdX_9fqwweASdD4UEGvxg46LZgi2dKxhajGIbuU0TW09Cu_Ad9wk5ztYWKfxooV-2sirbWd_i211EGRYLQYQsG4mk6fQ5G6UNPSWF4AGMGdXhV_nMj3DoR7Ut3jkp0J1NMqcPR5Y3phPioalzwaz8Zz1jSdhGtyLJiyq7zhNeTndEha7jNKy433vhyMemC4di8GL0t2UmHFc1b4ntjungEKkgmKHFB79w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291f3357ba.mp4?token=F3ghmF-NkVmsYvt_ulkl1u8fGJ7u2nSjGlRglXF0rfWxfLJ27y7CUum2YJT102_ArIJzjV-ny157zE43x3QG2bX6bG6pA0PTVMskzbutME7GySc9hkhk2sdX_9fqwweASdD4UEGvxg46LZgi2dKxhajGIbuU0TW09Cu_Ad9wk5ztYWKfxooV-2sirbWd_i211EGRYLQYQsG4mk6fQ5G6UNPSWF4AGMGdXhV_nMj3DoR7Ut3jkp0J1NMqcPR5Y3phPioalzwaz8Zz1jSdhGtyLJiyq7zhNeTndEha7jNKy433vhyMemC4di8GL0t2UmHFc1b4ntjungEKkgmKHFB79w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای اولین بار قرارگاه مشترک مبارزه با گران‌فروشی و احتکار در سطح ملی و استان‌ها شکل گرفته و با این موارد قاطعانه برخورد می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/460860" target="_blank">📅 11:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460859">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cfb970427.mp4?token=najBNT0rANKxuDfHUZPDZL3XqXiXLUCksjjhVtRneb5CC5cudQHIlN6Ylhql2BFRhRV_zU0QUoRGxL7KfBnLYmznofzKMmUAo_aWz4r6-ID59UOtWtK5sS48Su-ciAFO52FZMVQ5x0QF8xTvoRpKPZOWHxqIvg4bQXO1sBx53rd2PT91xmlfa7bM1bKuou_8iOGPyUuRdcVUbu_j4i0ikzPQ9t0eQXrty2UF4iSQYAPnEBabhscUTxwbW4G_4vpb8dZMW6LDTUkz3XOJgAvFG_mGY3rmT67b63k5M3BE17QG_19ulwy8PlOtW0nN546zqCiZ_S7LTklBPeTmo1DSlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cfb970427.mp4?token=najBNT0rANKxuDfHUZPDZL3XqXiXLUCksjjhVtRneb5CC5cudQHIlN6Ylhql2BFRhRV_zU0QUoRGxL7KfBnLYmznofzKMmUAo_aWz4r6-ID59UOtWtK5sS48Su-ciAFO52FZMVQ5x0QF8xTvoRpKPZOWHxqIvg4bQXO1sBx53rd2PT91xmlfa7bM1bKuou_8iOGPyUuRdcVUbu_j4i0ikzPQ9t0eQXrty2UF4iSQYAPnEBabhscUTxwbW4G_4vpb8dZMW6LDTUkz3XOJgAvFG_mGY3rmT67b63k5M3BE17QG_19ulwy8PlOtW0nN546zqCiZ_S7LTklBPeTmo1DSlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: در رسیدگی به پرونده‌های دی‌ماه تمام حقوق متهم رعایت می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/460859" target="_blank">📅 11:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460858">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee10be90c9.mp4?token=ezwtflkqY7wz8EF98ZK8BARcMsxksUtL0u0oIECeYoyc-mnMo4IqB6k03BRc6arS1m86fTl_-jpmllX0iCCwiKDAmMrvb_oVwa80FybOHYjaFcWnsce5Bx1221wiMpz2aS7aNWXE3RMGcVo1Ikzl8k1aZ0X9vBRDhoXMpSmLRMLX-Nlldw7Htzqv0bbXo2BvjTpf13Y3IAJ6B6cvP4aQKB12_N9o5Hv9WHLalsqoqk3WCL5s0hHeg4Zb8-zMfVnPlwlJEewtLzyIUU58AkdL4akszBBWHTL_98rSJuAYPclfIDdtcPfStDSoKaZxW5hFbBOpfSnbJZ_-JBKJKvT7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee10be90c9.mp4?token=ezwtflkqY7wz8EF98ZK8BARcMsxksUtL0u0oIECeYoyc-mnMo4IqB6k03BRc6arS1m86fTl_-jpmllX0iCCwiKDAmMrvb_oVwa80FybOHYjaFcWnsce5Bx1221wiMpz2aS7aNWXE3RMGcVo1Ikzl8k1aZ0X9vBRDhoXMpSmLRMLX-Nlldw7Htzqv0bbXo2BvjTpf13Y3IAJ6B6cvP4aQKB12_N9o5Hv9WHLalsqoqk3WCL5s0hHeg4Zb8-zMfVnPlwlJEewtLzyIUU58AkdL4akszBBWHTL_98rSJuAYPclfIDdtcPfStDSoKaZxW5hFbBOpfSnbJZ_-JBKJKvT7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: پروندهٔ فرداموتور ۹ هزار خودروی تحویل‌نشده دارد که بخشی از آن در حال ترخیص است.  @Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/460858" target="_blank">📅 11:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460857">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c66a69a8.mp4?token=I_Jslu0LKyGyopSuNLlHsAilIdYMMka0YQ-YV5oVSmagzQ-qF3ubfmcpF5h8F95pNTk9ppIWgEKHHO075_ZqDD_iglE7u1KuzNNes0NGrhwMrh3nXldi4thbOWLVZFdyFIpMM928WfDinVMlTGjFOdLR8yxp4eo3j3A1Zqf1istysfgbnhQnW1Tr_4ID2yvCo6-h9F9-GZZocT2EvvkPx9bSEcv1sQSRmsXokHwIBZGAfaDMvn5uLvnBGG1gfDXIIvMIluhG0ZNBvi6JuYkd7Q_mf70Gz4q6QEGxJwzuBkOUjYL-UcVu2yNTfIk0JW509QMHr_t95p-2W-ZK-XHSBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c66a69a8.mp4?token=I_Jslu0LKyGyopSuNLlHsAilIdYMMka0YQ-YV5oVSmagzQ-qF3ubfmcpF5h8F95pNTk9ppIWgEKHHO075_ZqDD_iglE7u1KuzNNes0NGrhwMrh3nXldi4thbOWLVZFdyFIpMM928WfDinVMlTGjFOdLR8yxp4eo3j3A1Zqf1istysfgbnhQnW1Tr_4ID2yvCo6-h9F9-GZZocT2EvvkPx9bSEcv1sQSRmsXokHwIBZGAfaDMvn5uLvnBGG1gfDXIIvMIluhG0ZNBvi6JuYkd7Q_mf70Gz4q6QEGxJwzuBkOUjYL-UcVu2yNTfIk0JW509QMHr_t95p-2W-ZK-XHSBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: محمدباقر خرازی در بازداشت است و پرونده‌اش هنوز به مرحلهٔ صدور کیفرخواست و حکم نرسیده است.  @Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/460857" target="_blank">📅 11:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460856">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf6253d754.mp4?token=baL-u5c-a9bk36oskyLgvj7HXg9-TQRIwdec2q-bbiEsacriUWRFELCrM5SW2mVIcTpkXzcecWyrRLbcPqq56wH34ncLRLf2CVxFqCKS4A4s2xMWGYHKCeyU0c3zj339jm9Y9ZQCqUtyLuOvQHD1v2YynaqmBJqiuJcRTx1Cu1pm01UFILoD_LPXA-vMh5BnGHQmFT7WURn4Nx7OGDHQM7QAECFgmMOZEcO6rTalvREDwtmng37EfowWPjNsWbaVf6tez8i9PYvw-7J-4kVSOgBJYTojnsB0DBXRai825aTqDOEF5X1pqeYMC-SbDzB8Qnv1VVy0tfcH8Sr7RnAS1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf6253d754.mp4?token=baL-u5c-a9bk36oskyLgvj7HXg9-TQRIwdec2q-bbiEsacriUWRFELCrM5SW2mVIcTpkXzcecWyrRLbcPqq56wH34ncLRLf2CVxFqCKS4A4s2xMWGYHKCeyU0c3zj339jm9Y9ZQCqUtyLuOvQHD1v2YynaqmBJqiuJcRTx1Cu1pm01UFILoD_LPXA-vMh5BnGHQmFT7WURn4Nx7OGDHQM7QAECFgmMOZEcO6rTalvREDwtmng37EfowWPjNsWbaVf6tez8i9PYvw-7J-4kVSOgBJYTojnsB0DBXRai825aTqDOEF5X1pqeYMC-SbDzB8Qnv1VVy0tfcH8Sr7RnAS1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای مقابلهٔ هوشمند با فرار از دِین، سامانهٔ سهام طراحی شده و تاریخچهٔ نقل‌وانتقالات مشخص است.  @Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/460856" target="_blank">📅 11:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460855">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8e3d77ad5.mp4?token=dWR1OgO07btQSwf6EbE0B4AW7sOkUoFAh42qpgB3ZCIPoWd7PQH4ISnl26WfQwFo8AtOczHJiabjZPlDZsRQ1l3LcbxgWrZi8YqGn9iUM-mpVFoj-bBxCB9sQ3i-j5MsnFJpiz6eS5ZGBlV-_t2J_NTOgMe1YgtqolzBU2RXE45zsnM-yqJpDvdBUHjsjY6RyVKwH4hAOvUGxbutmgeT8j_ouKyeZfF2PsVtXTebDVJE093qUbCI3ml1p862U8scCMfZ-AqS9XU24j94Y5HyWITZ1XJ04S9zgktNtF85muIJqPcjeD7VHLQwMdXQgwCrn72wvscQQc2JzELqJLNfoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8e3d77ad5.mp4?token=dWR1OgO07btQSwf6EbE0B4AW7sOkUoFAh42qpgB3ZCIPoWd7PQH4ISnl26WfQwFo8AtOczHJiabjZPlDZsRQ1l3LcbxgWrZi8YqGn9iUM-mpVFoj-bBxCB9sQ3i-j5MsnFJpiz6eS5ZGBlV-_t2J_NTOgMe1YgtqolzBU2RXE45zsnM-yqJpDvdBUHjsjY6RyVKwH4hAOvUGxbutmgeT8j_ouKyeZfF2PsVtXTebDVJE093qUbCI3ml1p862U8scCMfZ-AqS9XU24j94Y5HyWITZ1XJ04S9zgktNtF85muIJqPcjeD7VHLQwMdXQgwCrn72wvscQQc2JzELqJLNfoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: تلاش می‌کنیم با رویکرد صلح و نگاه مددکاری به حل‌وفصل پرونده‌های مالی کمک کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/460855" target="_blank">📅 11:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460854">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a6d40fc.mp4?token=LsY8bdTQqJZsBzS6YYbuIUNufixnUw1xpN6kyOI2S3SPZGEjRV9ZH_EFVhM9Kd4W9MO7ET7eZGremYxmo5edR2XxBuAyUaeYBxUt_oSStnQB7kkza3a9gIXHjfUwaqlNWUNTXk9lhvIFqqQms7QrJOFM39OU5VzRFWbctkMpiNIs1F0rEVUJrjBqUn-lfmBgGnWwVj0E7Cfwbh9YrZ_aDKn4n54X9ohk9DyUCR96BjXHvk3CGdqMKlVE62dznj_-XgWVzUMrDml2wPp4eSrUrNuP49zx_6ecaHSJC9MwDKIs2aNWLAfjGX4j0zVS4fVtBkRUaXySYc-3jBANlBnK8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a6d40fc.mp4?token=LsY8bdTQqJZsBzS6YYbuIUNufixnUw1xpN6kyOI2S3SPZGEjRV9ZH_EFVhM9Kd4W9MO7ET7eZGremYxmo5edR2XxBuAyUaeYBxUt_oSStnQB7kkza3a9gIXHjfUwaqlNWUNTXk9lhvIFqqQms7QrJOFM39OU5VzRFWbctkMpiNIs1F0rEVUJrjBqUn-lfmBgGnWwVj0E7Cfwbh9YrZ_aDKn4n54X9ohk9DyUCR96BjXHvk3CGdqMKlVE62dznj_-XgWVzUMrDml2wPp4eSrUrNuP49zx_6ecaHSJC9MwDKIs2aNWLAfjGX4j0zVS4fVtBkRUaXySYc-3jBANlBnK8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: در قانون آیین دادرسی کیفری ماده‌ای پیشنهاد شده که رؤسای دادگستری‌ها هم بتوانند بر وضعیت زندانی‌ها نظارت کنند.  @Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/460854" target="_blank">📅 11:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460853">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSz8PKA-XqdG5-ESsTJCl3SFG72Rz5kj9RiAqSlWEenjLOU1Ikz1U5rSvxZSAPgs6xXHJVLsRQqtYCNd_8851lVrZIOiHhytas9PVkvNK3a3RRVN3ZBB6eP3O92GNL2r5KZV8Wa3YKwRVjXx2M4rQFoWqV1purb6V3YxGulI9OfU7GxNRJtt6fHsrTopDQePiUyY6hDEUlY1w5MIzj7jxFjBZ4QzncNkJMbpC5Txt9MWzDmn7wbPQ1DbpnuAnfvUEZTIuk_VuRbD5zD1PQvh31QrwQwFo4oPr91rDgNYB-TS79tuprgvQ4XZsHFvBuRU7XUMQvGgjOsZh82uReJSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حملات یمن آرامکو را به تعطیلی کشاند
🔹
وزارت انرژی عربستان اعلام کرد حملات بامداد امروز یمن به تأسیسات انرژی در جنوب این کشور، موجب آتش‌سوزی و توقف موقت فعالیت برخی تأسیسات شده است.
🔹
در این حملات، پالایشگاه آرامکو در ابها هدف قرار گرفت و همزمان گزارش‌هایی…</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/460853" target="_blank">📅 11:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460852">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fcfb4550f.mp4?token=bkAVV_EM7MHh1F-Ec_W0Bfk53QlR7eXmURhkfgt1Bp8h7ar0TUvRGYWZzr_dmQlmSnZtCCZiWuc7Udpom66vsAIzUKzdS871yJgWbR95WQTmIbzyAqp_s4Weu4LThvodcP6-KZ5O69hXzJMwiEBGG2m_V68fPtkhEcqUTxELj1EUTx9bMOKmnPAEo0J7uDXT1L1l_lLMOAHbm7D7tXhcIOV1RH8dry7XJ8PQlEmsp82Rn-nXu0S9aVQhalNB0kEddrffLMGWPpmI2OM56-vl44Vv5bD6ZiWQ7CYU1k1ORKYbk6zmRHi5zmqybAfRIeS0MJiyGXDFKaOPS6GxJVTB5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fcfb4550f.mp4?token=bkAVV_EM7MHh1F-Ec_W0Bfk53QlR7eXmURhkfgt1Bp8h7ar0TUvRGYWZzr_dmQlmSnZtCCZiWuc7Udpom66vsAIzUKzdS871yJgWbR95WQTmIbzyAqp_s4Weu4LThvodcP6-KZ5O69hXzJMwiEBGG2m_V68fPtkhEcqUTxELj1EUTx9bMOKmnPAEo0J7uDXT1L1l_lLMOAHbm7D7tXhcIOV1RH8dry7XJ8PQlEmsp82Rn-nXu0S9aVQhalNB0kEddrffLMGWPpmI2OM56-vl44Vv5bD6ZiWQ7CYU1k1ORKYbk6zmRHi5zmqybAfRIeS0MJiyGXDFKaOPS6GxJVTB5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای وطن‌فروشان پروندهٔ قضایی تشکیل شده و برای بعضی کیفرخواست و حکم هم صادر شده
🔹
حجم اموال این حوزه بسیار زیاد است و تجمیع آن طول می‌کشد. @Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/460852" target="_blank">📅 11:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460851">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1738a6d5.mp4?token=HMwJuVUp43G4xpxmpbRCrO9wgW2sJWPIrmmeQSMcSnUPmT_CFvI_R8NDHTaXzFldTljejth7QW8iXDah2Sojsu-5wBouQKRquh4fMOJIXD_IJ9dXjK_xBnZn91HetxuGv7HP0evS4Qve_to-PsY8YukVPDdQK0swh7pr1NqLIGdZ8Phez9bEGjPHLM_NYC7nJjQ_So7uRQQxaBiqWeKH2e25pJ-8UGOFS5jXPkazwFOUhht4Y9d1xmkOaP_h5T8PDCcrnL38C7__FLTMtlHWEMbmyDOuzwhifAzBHZLBs-QP6QzxIAa7GMyFzdPsO0AZB2GwSMjG4WIyr7oqnO1yBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1738a6d5.mp4?token=HMwJuVUp43G4xpxmpbRCrO9wgW2sJWPIrmmeQSMcSnUPmT_CFvI_R8NDHTaXzFldTljejth7QW8iXDah2Sojsu-5wBouQKRquh4fMOJIXD_IJ9dXjK_xBnZn91HetxuGv7HP0evS4Qve_to-PsY8YukVPDdQK0swh7pr1NqLIGdZ8Phez9bEGjPHLM_NYC7nJjQ_So7uRQQxaBiqWeKH2e25pJ-8UGOFS5jXPkazwFOUhht4Y9d1xmkOaP_h5T8PDCcrnL38C7__FLTMtlHWEMbmyDOuzwhifAzBHZLBs-QP6QzxIAa7GMyFzdPsO0AZB2GwSMjG4WIyr7oqnO1yBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای وطن‌فروشان پروندهٔ قضایی تشکیل شده و برای بعضی کیفرخواست و حکم هم صادر شده
🔹
حجم اموال این حوزه بسیار زیاد است و تجمیع آن طول می‌کشد.
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/460851" target="_blank">📅 10:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460850">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf30da4a1.mp4?token=f5u3-vCAwJbVQTBmuzXKw7nqc8otYjnKSHu1WWk_VEKo57n-XuC7yt_qRgvqUzyVR__9zfEpcf6gDSimFcgOjxVyhRKc-nHU4LBYQeXse1cGpgcHZUYZbBlOLdw9yEv1RLxXU_c1SF5iKv6t0DfX2wNkytBzmAsMJktxvpDy5gIkolPrwpnQntSQx5BslO5REf-n6MnU_uw1cL9mpm-9bQMGWcgVW49nKA5RsvOnzSYo3karK6XEsinHdGKXr1ud7dTXGKrcd6Qjk3KQXAPBP6O7n_oEQPQF817HLBOGpMrdiL15mjK7Ci9nlPhHHuuPGeZ-C6qEbXA1-M46YdcdAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf30da4a1.mp4?token=f5u3-vCAwJbVQTBmuzXKw7nqc8otYjnKSHu1WWk_VEKo57n-XuC7yt_qRgvqUzyVR__9zfEpcf6gDSimFcgOjxVyhRKc-nHU4LBYQeXse1cGpgcHZUYZbBlOLdw9yEv1RLxXU_c1SF5iKv6t0DfX2wNkytBzmAsMJktxvpDy5gIkolPrwpnQntSQx5BslO5REf-n6MnU_uw1cL9mpm-9bQMGWcgVW49nKA5RsvOnzSYo3karK6XEsinHdGKXr1ud7dTXGKrcd6Qjk3KQXAPBP6O7n_oEQPQF817HLBOGpMrdiL15mjK7Ci9nlPhHHuuPGeZ-C6qEbXA1-M46YdcdAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای راهبردی روابط خارجی: مذاکره گره‌گشای همۀ مشکلات نیست
🔹
فیروزآبادی: دیدگاه و نظریۀ بعضی از دوستان این است که ظاهراً همۀ مشکلات را می‌شود با گفت‌وگو و مذاکره حل کرد.
🔹
اینکه همیشه فکر کنیم همه‌چیز در هر حالی می‌تواند این‌گونه حل شود و با این روش عمل کرد، از قدیم در روابط بین‌الملل مورد نقد بوده و الان هم مورد نقد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/460850" target="_blank">📅 10:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460849">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyM7KQDVeE-_DlC9ReyDlFA6doCfo9HxaMm0oATApRuGvQwJLOtJcD8ZlnQ9jEu2qBNt2VlR8zisjjbQ5uqpem0jPMxr2N-bG2AwSdobrx1fCh6dH3ijzy3V6w6A3EcdTI8aNC1J7toVEnCYexijirw1lKybWFO6SR2WMdRjW-BcQ6dnbEnA6tbjWXtF_AzvwYEtyp5TSNQHDfY9dr53T2PhbVIa1I2-69kpnWwfgw52s_onG0cjKfKwS2yHm8Q6Sh55ax1T60gT7Kv20f700dY7eah3M_Kh7ZuGvCWZYiSiMuIRkKWB7q_eDjp4bM6tgiqgTMEx58RHYeOyUxK5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده به مجلس بازگشت
🔹
در نشست صبح امروز مجلس به ریاست نیکزاد، برای نخستین‌بار پس از جنگ رمضان، جلسه به‌صورت زنده از رادیو فرهنگ پخش ‌شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/460849" target="_blank">📅 10:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460848">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b357690a.mp4?token=Qw2MoYN3e7A89aopzySRD6tn7-2EalcDMACB5L1TMRmYr0HYqAOyg8Xf9_Ft3RnZBtQW8eN6aeys7yv_mjWe9bcRMTR9KTiqmOQe2oryoTi-WYhPrivWedL8PllyeZR9iABDXQONaiUkJIYSab2liPsSB8Q8ONN_K-cXe84YemKARk_7KYNvzKh0NZBIKJdUCluUj9BkESylqwHWiM2AxW5BZqrlp_tR8RhC865kNnMF-nhNe5KLpxbWZo34OJTuMxE0n3_QRQJX0DFplxRjnA-BMU9AYgMxqKUvs3CpJiZCkIBDn58vEDqtRKUjLQRN-_M0YMyi4jTLozkCToYgRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b357690a.mp4?token=Qw2MoYN3e7A89aopzySRD6tn7-2EalcDMACB5L1TMRmYr0HYqAOyg8Xf9_Ft3RnZBtQW8eN6aeys7yv_mjWe9bcRMTR9KTiqmOQe2oryoTi-WYhPrivWedL8PllyeZR9iABDXQONaiUkJIYSab2liPsSB8Q8ONN_K-cXe84YemKARk_7KYNvzKh0NZBIKJdUCluUj9BkESylqwHWiM2AxW5BZqrlp_tR8RhC865kNnMF-nhNe5KLpxbWZo34OJTuMxE0n3_QRQJX0DFplxRjnA-BMU9AYgMxqKUvs3CpJiZCkIBDn58vEDqtRKUjLQRN-_M0YMyi4jTLozkCToYgRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رویکرد جدید نفت ایران در برابر دولت ترامپ
🔹
معاون تلفیقی شرکت ملی نفت: در مواجهه با رویکرد خصمانۀ دولت آمریکا و شرایط خاص حاکم بر کشور، افزایش تاب‌آوری در بخش‌های تولید، توزیع داخلی و صادرات به اولویت نخست شرکت ملی نفت تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/460848" target="_blank">📅 10:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460847">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/544e56f81f.mp4?token=KaUDauG_QfD7lP3m83HjbBBstk18Mhe_qspJBqKgM6QDRg6wSer6lDYDRERQ5FdCglmWYI9L69ck5FtjNw1tDRxC36lsygnbrHlQ_xM-3NZn5DKfduYSKmv3XON_ob4ThUrVDFEA4fG5XJEoQp1sLBk911P2mSwKIVfLA3_gCIFMSdn3pDkaaqFXvIzGScIB4l_2cx2baB9p7kN-QcrvRnHLEEKziMV8XdrAFMohIRGmNWmmvNEG9lmxL5XthHzn9fKEsIF8_5GXw-bL7agHbS_srIaLcvtdczZ9mBFVXORaBCJuxe5BFhMUZ_v6lh1lh4RloehILReUwCqRR6A9aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/544e56f81f.mp4?token=KaUDauG_QfD7lP3m83HjbBBstk18Mhe_qspJBqKgM6QDRg6wSer6lDYDRERQ5FdCglmWYI9L69ck5FtjNw1tDRxC36lsygnbrHlQ_xM-3NZn5DKfduYSKmv3XON_ob4ThUrVDFEA4fG5XJEoQp1sLBk911P2mSwKIVfLA3_gCIFMSdn3pDkaaqFXvIzGScIB4l_2cx2baB9p7kN-QcrvRnHLEEKziMV8XdrAFMohIRGmNWmmvNEG9lmxL5XthHzn9fKEsIF8_5GXw-bL7agHbS_srIaLcvtdczZ9mBFVXORaBCJuxe5BFhMUZ_v6lh1lh4RloehILReUwCqRR6A9aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارت زرد مجلس به وزیر ارتباطات
🔹
در جلسۀ امروز صحن علنی، سوال علی جعفری‌آذر از وزیر ارتباطات و فناوری اطلاعات با موضوع پوشش‌دهی ضعیف تلفن در جاده‌ها و روستاها، بسته‌های اینترنتی بی‌کیفیت، بلاتکلیفی بازنشستگان مخابرات، رهاشدگی فضای مجازی و بحران تلفن ثابت مطرح شد که نمایندگان از پاسخ ستار هاشمی قانع نشدند و به او کارت زرد دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/460847" target="_blank">📅 10:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460845">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/251a5a71b3.mp4?token=FWGSv_5Fs5RMJA1Usa58f7yw6849JQhLS8wBngGxMWISm-oTHyDzROnyUaVFsSAvJze9oCL45VzU8D9Q_qplqKIPjh538Vg50YkqCL4ohV8nffPt4hZoSWuSGG8fD-QEKxGWcefgb-_WzuDU2BIO0Fy9i-IeLJvFTZ7kvnySHgYVNKqZeo7sJUrtR2Qkqb1iSv2G98mt9rUykEI_Xp3dKLSjJcLin4r71HZgXUVljju0rQ1m3TBa2ukw6VycVP7N2u_t7LUvQBNZpXmGSaQ1fGALAAP8MeDNySc3uM3a-ejfWGdv1ZjbV40qk1jy_1it9kpBApEgl9W0ZNp6OIC27g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/251a5a71b3.mp4?token=FWGSv_5Fs5RMJA1Usa58f7yw6849JQhLS8wBngGxMWISm-oTHyDzROnyUaVFsSAvJze9oCL45VzU8D9Q_qplqKIPjh538Vg50YkqCL4ohV8nffPt4hZoSWuSGG8fD-QEKxGWcefgb-_WzuDU2BIO0Fy9i-IeLJvFTZ7kvnySHgYVNKqZeo7sJUrtR2Qkqb1iSv2G98mt9rUykEI_Xp3dKLSjJcLin4r71HZgXUVljju0rQ1m3TBa2ukw6VycVP7N2u_t7LUvQBNZpXmGSaQ1fGALAAP8MeDNySc3uM3a-ejfWGdv1ZjbV40qk1jy_1it9kpBApEgl9W0ZNp6OIC27g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات یمن آرامکو را به تعطیلی کشاند
🔹
وزارت انرژی عربستان اعلام کرد حملات بامداد امروز یمن به تأسیسات انرژی در جنوب این کشور، موجب آتش‌سوزی و توقف موقت فعالیت برخی تأسیسات شده است.
🔹
در این حملات، پالایشگاه آرامکو در ابها هدف قرار گرفت و همزمان گزارش‌هایی از اصابت به فرودگاه ابها و شنیده‌شدن انفجار در مناطق جنوبی عربستان منتشر شد.
🔸
این حمله سومین حمله به تأسیسات نفتی عربستان در کمتر از ۴۸ ساعت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/460845" target="_blank">📅 10:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460844">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/efa5317854.mp4?token=R5AaikFeSJVByyQutVfAOcfIVe0J8F7uS3Ni1PL4b6R-cq-rcXSNt55wUzd46gLT6L8_4KUUV2uMaRs8FEQTQq3zYKJgZ9uvJUhJaXvS79AxLT9zQgcmCY9II2YWJ1tf4lmJaO9y_LoQvnpZtan556np8FzaPUe13ylu02hFARn_7m33mXnPzUVE8wYFIsYBuLIZVUGf13L8uoH5kAJrJ3V1Y6717CKKV2ilO0O-NsZxPvl-Bc37IigmHtmjvwR2tzI_EGF719IoTn1WHI3GBJjSz4PbhecgwbTB7HYiYVorTw7ZwRVpoQi0wzd4c7oB2ixIjzcttwfLK7pb0tMqWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/efa5317854.mp4?token=R5AaikFeSJVByyQutVfAOcfIVe0J8F7uS3Ni1PL4b6R-cq-rcXSNt55wUzd46gLT6L8_4KUUV2uMaRs8FEQTQq3zYKJgZ9uvJUhJaXvS79AxLT9zQgcmCY9II2YWJ1tf4lmJaO9y_LoQvnpZtan556np8FzaPUe13ylu02hFARn_7m33mXnPzUVE8wYFIsYBuLIZVUGf13L8uoH5kAJrJ3V1Y6717CKKV2ilO0O-NsZxPvl-Bc37IigmHtmjvwR2tzI_EGF719IoTn1WHI3GBJjSz4PbhecgwbTB7HYiYVorTw7ZwRVpoQi0wzd4c7oB2ixIjzcttwfLK7pb0tMqWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست جالب بهروز رهبری‌فرد از همسرش در «پانتولیگ»؛ «می‌خوای بری خرید، کارت منو با خودت نبر!»
@Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/460844" target="_blank">📅 10:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460843">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-text">📊
🙏
یکه‌تازی «وتجارت» در بازار کارمزدها ادامه دارد
✅
بانک تجارت در پنج‌ماهه نخست سال ۱۴۰۵ با عبور هوشمندانه از الگوی سنتی درآمدزایی و ثبت جهش‌های معنادار آماری نسبت به مدت مشابه سال قبل، فصل نوینی از استقرار بانکداری مدرن را رقم زد:
🟢
رشد ۵۷ درصدی درآمدهای عملیاتی
🟢
افزایش ۷۰ درصدی درآمدهای کارمزدی
🟢
رشد ۶۰ درصدی خالص درآمد عملیاتی
🟢
افزایش ۶۴ درصدی منابع
🟢
رشد ۶۱ درصدی تسهیلات
🟢
جهش ۱۹۸ درصدی سپرده‌های ارزی
🟢
افزایش ۱۴۲ درصدی تسهیلات ارزی
رشد درآمدهای کارمزدی، توسعه فعالیت‌های ارزی، افزایش منابع جاری و تنوع‌بخشی به سبد درآمدی، نشان می‌دهد بانک تجارت در حال حرکت از الگوی سنتی درآمدزایی به سمت بانکداری خدمات‌محور و مدرن است؛ مدلی که در آن، رابطه مؤثر با مشتری و ارائه خدمات متنوع، به موتور جدید خلق ارزش و سودآوری تبدیل می‌شود.
📌
بانکداری به نفع همه؛ به سبک تجارت
🌐
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/460843" target="_blank">📅 10:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460842">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/460842" target="_blank">📅 10:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460841">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8Q3feZVWYeb2_gcsowhXuIIexKglc4AqngKB244fTepcU5zBLnbnUnNp-N9hl0Myf-Y_4v6SEgihCxVGOrxYUotLWtStVV5YLHDNfSUbuDJh7I7WIGXMD__fjoqKqvY-4EY-m5b7P0HOSrENcDsR_YXLxdbDHwvQAyIZiyNuW-tKDhAKGrmIcSkhw1zS2BG3ED9wx7rdclMnYYyI-WY15kWM1D2HpgfS4rE0P3CiLYrTRp3izOnBTHBcSM_ki5gau_x28AHid0pBjUuv2U_q5kC03BZbEfoyPD_KEa5CUEqKQ9AlpBJmg1a11_kN0EwjCAKL4t27KhLxHmwXBY0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تصویب یک فوریت بررسی لایحهٔ تداوم حمل‌ونقل عمومی رایگان در تهران
🔹
یک فوریت لایحهٔ تداوم رایگان‌بودن حمل‌ونقل عمومی در تهران، امروز با حداکثر آرای موافق اعضای شورای شهر تصویب شد.
🔹
رئیس شورای شهر با اشاره به اینکه «تصویب یک فوریت لایحه می‌تواند زمینهٔ ادامهٔ…</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/460841" target="_blank">📅 09:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460840">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMwRneig66eTA2QJZPQbzZTYcQgrmZSq0cLmR9ALEruUqfmkkKxX6vHd5dIrkjZ4mx14AZ_YuHlAFTEQU0qsiGREdPdTBdInoegwnOBPisTqKq80m7ufmrVwjKA0ZaV8UN-b-XFzW9X4w60HiYHqnlQRmjUzKD0YhWirll693Gocx5UujjTVJFI_C40CHBYu4IuHHCIPqn0QTrdLgncQVVaijIRCI7RXsDrk_GyRUD6PJfYrcmOqP9_EM7KyKLHL-wMPhZoMMo9Ner8sfpLCJNDdV1Yex4xVGQ3rd9RXNHD8FosA1HONtzPM6xgyOyESzeGSYqOdARIinhdwp1oMNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/460840" target="_blank">📅 09:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460839">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LInDRTKVGDDP1jFtVD-GUC3JMoEmpCQrjfYceunghI5XBGDAu6jZ36dXG5k3PwcPSdRdd6oyJsAZXoSoudxPQE6Mq7MPhvVl8UQXilCEoNsUpTwm5p4hVRP7mKMGFvSWj0W0zPsZIB_gThU6jEtjBoMLnZCBY_7qCz7iQzisrp-D3vPD7O5i_BDicMiiNXKXbPgIPUiOOOWsG_K0_DSDhHz-6aySKCxH1oBv8-WeRHYheE2KkMt3NcOd89UoUTsn10etkuANwXXwSx2JPyr3YFqydMdgR1VQXMryKpXkgxUe-vehpYJhKQ4lmPgHiEYoZmK2m23FSBS1UANxK8pMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای «بانک» مخصوص جنگنده‌ها
🔹
«بانک زدن» یعنی
خواباندن جنگنده روی یک بال برای تغییر مسیر و گردش
؛ مانوری که در پرواز ارتفاع پایین، مهارت و دقت بالایی می‌طلبد.
🔹
«بانک زدن» یعنی
خواباندن جنگنده روی یک بال برای تغییر مسیر و گردش
؛ مانوری که اجرای آن در ارتفاع پایین به مهارت و دقت بالای خلبان نیاز دارد.
🔹
در
جنگ ۴۰ روزه
خلبانان ایرانی نیز در مأموریت‌های رزمی از این تکنیک استفاده کردند؛ از جمله خلبانان F-5 که در عملیات حمله به کمپ بوهرینگ، بخش‌هایی از مسیر را در ارتفاع بسیار پایین طی کردند.
🔹
اهمیت «بانک» زمانی بیشتر می‌شود که جنگنده در ارتفاع پایین پرواز می‌کند؛ جایی که خلبان باید در زمانی کوتاه مسیر جنگنده را تغییر دهد و همزمان فاصله خود با زمین را کنترل کند.
«بانک زدن» چگونه انجام می‌شود و چه نقشی در پرواز رزمی دارد؟
🔗
اینجا
بخوانید
@Farspolitics</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/460839" target="_blank">📅 09:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460838">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPJRCB3wH4EcdFnkzkkoYlAxpjgUqE6ZEU1dQ37Y3Q_UghhLEvMliXPpck9wgx82tXLwIidumj3FrKG808hHHRn4wX3Et-7N5nGxXxFd_xtKopSk1evGlWHj2wr8Jb8J6rMpvzV2mohbddY4S3JQXDwSyL7smJM2USakcktMg3FMgX1mW7_ancBlj3iQ4KUok6wjazdaJl9oE8bKr4FPNsb0sXzD0Oyyi8ybSkU8SDsXrgOL5BZrOKHouq3lBMJgeBv3d177UMdm63yM9ghK1rs3HfhIShcoKhGRm4j6P4BNKSkztWo8oDExmQ7Q6D-fRT6LSsdmSEyeuS5x--sAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۷ میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با جهش ۱۷۶ هزار واحدی به رکورد تاریخی ۷ میلیون و ۸۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/460838" target="_blank">📅 09:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460837">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5QI90z2s92eRFvcuNjyHv3UgEX1mAqRQzcdjCzOeoAuyv7rHmApF9bSXzNdja9tQ5zLjzunwKv0A1TET8R2gVA_t7AA4oe9YdSpKDz8Zry1zH95GOddSYAx_DTKJdi5c2w9XCII3D2VXzmofsOdQoO0i1610YUTEcNQIw4nqtAC5SYbad9wohn_L6OsifBSohyN6O-nk1gfQVfzvlQL0QxTGG2qSj2Y9iAcyypmqxeLHNntIWG7_rsSZJYs4EfK1JtbmZU6O44DUCUzPLNHOLNM8Vhvj7pOaoeyRSzko28zsB3bM-liTRQNMSxOWa9f5Z1t9H6Bh4ZgnuVUGnWRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکزیک به ترامپ: مستعمره کسی نیستیم
🔹
اقدام رئیس‌جمهور آمریکا در انتشار یک تصویر جعلی با موضوع تعلق بخش‌ زیادی از مکزیک به ایالات متحده، پاسخ رئیس‌جمهور مکزیک را درپی داشت.
🔹
شینباوم در رد این تصویر منتشر شده توسط دونالد ترامپ گفت که مکزیک، مستعمره هیچ کشور خارجی نیست.
🔹
رئیس‌جمهور مکزیک در شبکه ایکس نوشت: «در ماه سرزمین مادری‌مان، بار دیگر تأکید می‌کنیم که مکزیک مستعمره یا تحت‌الحمایۀ هیچ کشور خارجی نیست و نخواهد بود. با افتخار، ما یک کشور آزاد، مستقل و مستقل هستیم.»
🔸
در تصویر ترامپ، آمریکا، مکزیک و کانادا را با رنگ‌ پرچم آمریکا نشان می‌داد، در حالی که سایر سرزمین‌ها نیز زیر پرچم ایالات متحده به تصویر کشیده شده بودند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/460837" target="_blank">📅 09:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460836">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e49b3dc7c6.mp4?token=OBlmn4O1EqemWQM0NAiurnOzGCL-pM0vfkcu8OIKcNXqY3D_OkY59-pSvOCYT2_5m35HKtbYZcl23dAdacObRS3b5aSly76wHcwANsOwPU317VWRiuuZpvpA7RVKEGOBLZDeIFwFkv4gQb1Rlk2mpio2fl28V2MbKQQ6q_-5TZ5QwsvKSxuAd1-Ref2W2GpPUyI_vBgYJFmG5paO2M0MC7DIiGWkKgWJbhbE_UCRYBVsRZzOG23l2peuz9SQyQ8ODvAH7HdEYft4TbaLzjDE-vorf3AszRubf01TmrY0WgaWB3sOBTSggKyU5uUeqt30UXmVmFMirUKI5Ecz4K1AAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e49b3dc7c6.mp4?token=OBlmn4O1EqemWQM0NAiurnOzGCL-pM0vfkcu8OIKcNXqY3D_OkY59-pSvOCYT2_5m35HKtbYZcl23dAdacObRS3b5aSly76wHcwANsOwPU317VWRiuuZpvpA7RVKEGOBLZDeIFwFkv4gQb1Rlk2mpio2fl28V2MbKQQ6q_-5TZ5QwsvKSxuAd1-Ref2W2GpPUyI_vBgYJFmG5paO2M0MC7DIiGWkKgWJbhbE_UCRYBVsRZzOG23l2peuz9SQyQ8ODvAH7HdEYft4TbaLzjDE-vorf3AszRubf01TmrY0WgaWB3sOBTSggKyU5uUeqt30UXmVmFMirUKI5Ecz4K1AAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ بانک‌های مازندران هم امروز تعطیل شدند
🔹
معاون استانداری مازندران: با توجه به آب‌گرفتگی شدید در اکثر شعب بانک‌ها، تمامی بانک‌های استان امروز تعطیل هستند. @Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/460836" target="_blank">📅 08:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460829">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TsWCm1NLZUaMMJ6YpCyQ3mSe6P0CiRQiS2a3KLnxO8g4_m3VQOdKawgMTqGovssl6J9eNrDOlDyeEQuFvGpg_1eymkifIvrl7RayRo8KXWV6lN5lFfcBgscOvp8VhBjKjfhn6kd1q_7i6yJU_XjTgJ-3mw-K2sf2GrPcnjjdx0q13CaMneg5bKdlBfNoaHq3dID8TQuOBsds-vXWc0q9JzfjT03fr59iuMQygIk-LA7MG2MpJcxAOJOcQ4se5KIkDXjEAuErjI8c_VXDL4t6L61IVJPlVoU0nbw697fOovbjLr-Le3zTF8zCwGRPzyIu61WlyedfMknUmS30FFqa_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jaKMpNbAPIIgqV01vVASUXYM8nQB6ODoNLMXcGsLc02OnlWj8AHv010_uZi4N7fUbzpMsApUIi6tpDNMjOS2u71nJqLJVmDjD7MK1W-QVAlUuXoJ4tn4NgbQNF1PIc_VcTDij2dvTYZqb_fRKuWt-Dz0cxBPThYPaUlRGxQoar0qAXl4uYDps-Evrwh2zkaSFrHZMaFtN8q0gPoYCHSofGcAgdkG28kmWAVgPCxP1APLZLDpsH0HHlSuThRzvZiyKbG_RHIL7wwX57W7yiZyIDKJcHTrHHnK7C6OXL2hAVA6lr_qothxlIXJyhCKiGpsQOHRoTletoed88f1LcI9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6bqnUdP-A6auXYaDJNiyVE-gnakIrbJOSSRNvhKHbCcumi40QPnEQ7Tc5pkboD4y96ZXXC-f-VvtginQvEcsgiaqNyUviW_H8-KzWk-EPGDsnp7LcfE2jxxZRiO1rPAoKEYpMu6Wm9aN7TnTVjE6UbwPdvEQLWPy70LGGQLOs6yewxEWZNUB3xzMoMqcVuowxnTQdQwMw0bPKpLtH0-361UQL8MOOgNclSxalDP9hdxmVMFa5-jtev3_P6iTuEdnEuQVmkwBrIlIuocFdMPah5Y182vtOeb4nl_h-IWZG_0AYZbEr3l1d94wP5yq6tMqFDH85f9ll6zhTa1UEYGqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9NTG4I3F59E-0JxADFL4yY7I6U-BBYMUnO4UzFQJYx58rcS5oqvvhJu3tUtyvxyzuD9uAHL9ctzBPwYraGls_qEqwWvJ2hhy1lFxyv-tAcqTCTRzOOfTFLEq9dn-NX6w3pfybX0BJn0AtQtgjF5y_x0oy_FEfVI8dVVZTpkIqv3M2v0QnGyD16JoPmsTHzYQzkwK6CpD2-5FgtJZe6jBRgnfiksRGOqDEyuqGgEg2Lnls4-7_T4ipUncMhpjHwnCk9tZoBpOYCVFwOvKolE4slS0ZdRkXa10u40my8wyJYgrjraDF4mOjrtJq_L7h4Z7qsw7iXgB-6QzmY632pF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pL8ToRKaI49zizr8HG3W0BHAiEbblFmBtfCQx5qCGyY5OGltlAKSZJgn6O7dYuizPVazLR2RNiPIulU0BMW700hFGPBlJE2MMbzEKQE5SAtDn2UI9QozI0UKrBXlXKyG-BSscfWaBH8CmlEeRjJGRkiox2n4ctZmRoH7xebbraPbqKBLzKVzk2_hhwjlP-Rvrej0TCJEwzu22yRds8j2jgcI7kzZYPJXZ5KGzE3g4Z6g-YiVsFbRLHnvVzWb2Z8Vke6CM74aAOAEpUeCnRNJ5JvVogewNqVJrnnNCaHGng6xnqNTd3g2QtEo_m90dhvJ6V_jpUR7ZxSAL3kQw8P2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxr-tDmYZ70ZdJLSvjBc7KubXbTA_epTYneKeHP48FE0gzh3VKkTtH9KbJ93NWYLTDT5FnTX-0jY6sG8QPL4othPJrwQWeu-ZxpnjYAhXVP3z80h0M7XL7nh9yhTT3NNlthZKKwkgJfMZf0KTaqFFMK0vO2zzDNWPhO6_sSv0YBLjFpM3sf4PEFZptQkEILbLcOkyyZjDK_jqwCxxLX62QDxOhAldc9qbOc4uKSD9rsOiyncusjQgiJzgBKY4wddSE7XtpNuEK1NtL_GE8hPVakrpl3sloBCmSur82lu8lohg-I54QL8VxxpKtWxHyzgNPD9tLX-TNeXo8c1KG10LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b8PDWcAXVTRgU5R-X-h0fdzPzrYzhqMxaXWWHMKTOqIIpvfPZNg_IueE0o28MVQXvNBcZLDZs3SBtLubrPrnrkudScvQKoAdypJDGO33D7Tn1kCKGZJMuKepQV7gCUCdNMeXTLMwFB_8o5Z6htSaT-N_66-D8thlW0REthcDzvMLlBaKO96UMreNxXWWXWHZu9FWAD9JeJxqFJdEVvHngchq9_BywMRYqnXMDNzTLZmx83QBG42H-G7hu0yjMnglD9shRIXfp9XJtGuttqeKYI4nQy-Q02fzAu9rblFirk-A-zeXEPx3jBVvEbLc-ZBCDnGgVX4hp5kbOcePltRXCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور قالیباف در حرم عبدالعظیم حسنی (ع)
🔹
رئیس‌مجلس شامگاه دیشب با حضور در حرم عبدالعظیم حسنی (ع) ضمن زیارت این مضجع شریف، با تعدادی از زائران دیدار و گفت‌وگو کرد.
🔹
او همچنین با حضور بر سر مزار شهید سلامی، شهید امیرعبداللهیان، شهید علیرضا بیات، شهید طهرانچی به مقام رفیع این شهیدان ادای احترام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/460829" target="_blank">📅 08:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460828">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MibG0KNANJeVfhrRHmNajw6ZR5X26mCEkgVLWbJo1uXjfB2-ql_U8sJBYMRLZde5CfKpPYh687ZT1RRQEsbvbO2s7MmxXG6Y0gAKGkY6vvXRthWxgIspfvGWuQzVT54Jw-U6I2fKjWmGFDwsotLbWfrb8BjhYuJBl1j0wmCF5LzEsSeDhmNe5tjoCYG5V4AuLp4_jfD7pKUOuZFIUJ_yYxagbseLWHB1IYAW400I8unMiH8WTibNgm9Wf5FajWdgPEMERlSA8T6DHkfcmqZypzvRJUcEjd9rvrjvzhMWFKNEiHiUWmADzowzRVIlcu8QNPS9S3E0xfKuGRpgq1ESZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نرخ سوم بنزین رسما ۱۰ هزار تومان شد
🔸
از راس ساعت ۰۰:۰۰ بامداد ۱۷ شهریور، نرخ سوخت سهمیۀ جایگاه‌ها از ۵ هزار تومان به ۱۰ هزار تومان افزایش یافت.
🔹
نرخ ۱۵۰۰ تومانی سهمیۀ اول و ۳۰۰۰ تومانی سهمیۀ دوم تغییر نکرده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/460828" target="_blank">📅 08:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460827">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dzpz9eMdOa1GCwz0kkS6bsXRcfLsgOTUlkDC2RU0UAbon_E3ZQnZflBzHBMQNbQh90P0iY6wwgSGDGjFJ1ds2pw0Bogx1r4YBT7RKCVOfK5PxiGQVLgdjZRC6kgjpNlMi1_8OjfCKK0FwIWJRdt4RU3VLaYtyKv62eUZ_iGYNfK2c-nsln4q6rmnb4DjTz1QMalqLIQOI8aTCg6mZPMP9XIzMD69YMmrXr83lyULgaOd_NucGnN-dAc2dTJoVUe8fW5NT8KSBzntspwxMpZUNA2cn_oxH03rtKFgxGidhGmsr8z7bcwNfClYZMfKDyURGCsrM99qCvjhBf8JrJLF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط سنگین گرا برای جدایی از پرسپولیس
🔹
شنیده‌ها حاکی از آن است که تارتار نگاه مثبتی به استفاده از دنیل گرا در ترکیب تیمش ندارد و همین مسئله بار دیگر بحث جدایی گرا از پرسپولیس را مطرح کرده است.
🔹
در این‌ بین، گرا برای جدایی از پرسپولیس خواهان دریافت ۶۰ درصد از مبلغ قرارداد خود شده که پرداخت این رقم برای باشگاه پرسپولیس، سنگین است. به‌همین دلیل و باوجود مطرح‌شدن بحث جدایی این بازیکن، فعلاً تصمیم نهایی دربارۀ آیندۀ او گرفته نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/460827" target="_blank">📅 08:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460826">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
تعطیلی ادارات مازندران در پی بارندگی شدید و طوفان
🔹
در پی تشدید بارندگی، وزش‌باد شدید و طوفان، و با توجه به آبگرفتگی معابر و اختلال در تردد، فعالیت کلیۀ ادارات استان مازندران امروز ۱۷ شهریورماه تعطیل اعلام شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460826" target="_blank">📅 08:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460825">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌ هشدار پلیس‌راه مازندران دربارۀ تردد در محورهای استان
🔹
با توجه به فعالیت سامانۀ بارشی شدید و احتمال آبگرفتگی، سیلاب، ریزش سنگ و رانش زمین، از رانندگان درخواست می‌شود از سفرهای غیرضروری خودداری، و هنگام تردد در محورهای استان احتیاط کنند. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/460825" target="_blank">📅 07:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460824">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91e27328e6.mp4?token=tWNNygP4XuYQtsBCV4bvp4PNPy6wetaBEBUNEz9xYTmkOHfXsYmT1ygMKXh8SrmDooh-I9uljN7ZC1IUgjWfZn4SAzMiWqwGs9ZDKhRDfrvG6Jp34_YHw734kQ9QMq6bWhjD2zlc1fekOXMhO4t6XQsuujwun553n3pHh9_zAawTVKbF5qqHUTV1LWGQx4lLpoxLJbrfid8e3gbRJ_FSP71hZE8vb3a97AIAwl70yX3wG1QoMh-BeOyJ8r9bVx11b9ZCO8-V1jNwRk_KqheoMgCsTFD4jEciXtVbYu8FcKLBycDZj_yMoGRyg9uxsZPv4uMqfbQ9OUtXi2D2MNDpcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91e27328e6.mp4?token=tWNNygP4XuYQtsBCV4bvp4PNPy6wetaBEBUNEz9xYTmkOHfXsYmT1ygMKXh8SrmDooh-I9uljN7ZC1IUgjWfZn4SAzMiWqwGs9ZDKhRDfrvG6Jp34_YHw734kQ9QMq6bWhjD2zlc1fekOXMhO4t6XQsuujwun553n3pHh9_zAawTVKbF5qqHUTV1LWGQx4lLpoxLJbrfid8e3gbRJ_FSP71hZE8vb3a97AIAwl70yX3wG1QoMh-BeOyJ8r9bVx11b9ZCO8-V1jNwRk_KqheoMgCsTFD4jEciXtVbYu8FcKLBycDZj_yMoGRyg9uxsZPv4uMqfbQ9OUtXi2D2MNDpcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش‌های سیل‌آسا در شهرهای شمالی کشور  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460824" target="_blank">📅 07:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460823">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b236108324.mp4?token=royfZsmEXJFK8Ch6NyI-XFzTwn4io1JtUUWaKD0Y33N_FC5x4tzj62xcOXAzbiRch6bfmLUS0odTDAF8L9OCXDj9p-SbYmK1BMstO9dSp7LArNrcWTJT-vVaeJlqOWBIusj270PQhaBXlld8Ibya_uzwd9UP8cAkWZt60W94pN6WtflWHsML1caRFH5TT0R2QClefhO6A3jvtGthh4koylc-SaRDW4Gec5_RrMnMnwZCYa9751bmvQCNgt7SHlzzBrastoaGWz3GH3SolnAiH8FTITZr8czMwcZxTL4vwMUbW4hBYzM57HS631sYtOJVoJOI422eJkE8NYzbYASA8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b236108324.mp4?token=royfZsmEXJFK8Ch6NyI-XFzTwn4io1JtUUWaKD0Y33N_FC5x4tzj62xcOXAzbiRch6bfmLUS0odTDAF8L9OCXDj9p-SbYmK1BMstO9dSp7LArNrcWTJT-vVaeJlqOWBIusj270PQhaBXlld8Ibya_uzwd9UP8cAkWZt60W94pN6WtflWHsML1caRFH5TT0R2QClefhO6A3jvtGthh4koylc-SaRDW4Gec5_RrMnMnwZCYa9751bmvQCNgt7SHlzzBrastoaGWz3GH3SolnAiH8FTITZr8czMwcZxTL4vwMUbW4hBYzM57HS631sYtOJVoJOI422eJkE8NYzbYASA8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب‌گرفتگی منازل در پی بارش و طوفان شدید در مازندران @Farsna - Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/460823" target="_blank">📅 07:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460822">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_z25Z6fyWrn9tEULHVxcgjQd2ND2y-4Femd4NNyInIvoNIGR02FZJktMB_TlAa2p5NTcHw61JcPgBA-2tgvSs0NCs6bHvIhuBynYRkJPuOhigXSjJ2-eEWVKN6zPpfMIx-GWOX2bHHgjI7WCeICamfBZxNB7cfKeJVbLy4Zg2oBsxZxWfyXDWhmKgpTUaV9Ngc5j3kB7CPrzbBkIy3rakqFk-HGL6GpBvJPR_JPrpmIQQD_eZrsmjlDjc5OwWeudmM-_UEHELlPOVMVdgqchfD69OKCQUz3fnRq74YDmfelE9NN1CB3xzG3cTIpk93v0fv6Ycs-YI9ZMjV3wwFNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارهای مهیب کی‌یف را لرزاند
🔹
رسانه‌های اوکراینی می‌گویند که ارتش روسیه با ترکیبی از موشک‌های بالستیک «اسکندر-ام»، ابرفراصوت «زیرکان» و کروز، پایتخت این کشور را هدف قرار داده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/460822" target="_blank">📅 07:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460821">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70365c549f.mp4?token=vLB_vWqQchN3kxNk1BZFWkmI9Rs3W8YAIyUv0vFQ0WZHMy7ei0Hs9IAnfQDGV67dqLbSrzxgrfTAqmlbEBjSVwZYCMCuu1K2nat3PJr4HCMIdoGNJq0AJMNBTt7lww1_LTunkjzLKWR3UMbYXqTcijd6pSzn2clRZoOSovs4GI1z01PxV_iTvI8DyBwtvr9ZERiL_AVxuNZitVA3sC-wc02ZgqRyMBP5o3TlKkyqTQM72bdeaVL-um2d9Ez1OsbbhIv7VlfhPkFbkVN4mHiNfy6sUOi6CC65vGtl67mrodnlyUNkow5gkh7kI6KiKtVL_b71ndc7txPOk5NPq7Vjvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70365c549f.mp4?token=vLB_vWqQchN3kxNk1BZFWkmI9Rs3W8YAIyUv0vFQ0WZHMy7ei0Hs9IAnfQDGV67dqLbSrzxgrfTAqmlbEBjSVwZYCMCuu1K2nat3PJr4HCMIdoGNJq0AJMNBTt7lww1_LTunkjzLKWR3UMbYXqTcijd6pSzn2clRZoOSovs4GI1z01PxV_iTvI8DyBwtvr9ZERiL_AVxuNZitVA3sC-wc02ZgqRyMBP5o3TlKkyqTQM72bdeaVL-um2d9Ez1OsbbhIv7VlfhPkFbkVN4mHiNfy6sUOi6CC65vGtl67mrodnlyUNkow5gkh7kI6KiKtVL_b71ndc7txPOk5NPq7Vjvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ هشدار پلیس‌راه مازندران دربارۀ تردد در محورهای استان
🔹
با توجه به فعالیت سامانۀ بارشی شدید و احتمال آبگرفتگی، سیلاب، ریزش سنگ و رانش زمین، از رانندگان درخواست می‌شود از سفرهای غیرضروری خودداری، و هنگام تردد در محورهای استان احتیاط کنند. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/460821" target="_blank">📅 07:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460820">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌ برق برخی مناطق مازندران به‌دلیل آب‌گرفتگی قطع شد
🔹
بارش شدید و سیل‌آسای باران که از شب گذشته آغاز شده، علاوه بر آب‌گرفتگی معابر و اختلال در تردد، موجب قطع برق در برخی شهرهای استان و بروز خسارت در نقاط مختلف شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/460820" target="_blank">📅 07:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460819">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
بارش سیل‌آسای باران، طوفان و رعدوبرق در مازندران، در بامداد امروز
🔸
در پی بارندگی شدید و طوفان، کلیۀ ادارات استان مازندران امروز تعطیل هستند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/460819" target="_blank">📅 07:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460818">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c763e8ae68.mp4?token=i4qNiJhxJvK_X-WEQ5_u1UWE9MIk2Zn-1T6T512rYS2jtQfKVcQnamYbfHc4BTf31kgHBMzdxPPZ8hmHhAG1_3Wi51prOTiC5MGvUD9O2kDBLPFdH0i8Ep92uFyT3LINrMTgxUu1RwBO-Xa_uZZ_EKeRrOuxln82x6ywOIMYDA04IFHwILfpj0y_MXFA6c95NRUtwNARsPSu05vKutP4yvAzJx9bdEBGFXiLZgI-XMgnugEOyLsrkYb0MzaFzByVokKB1ACvNoIrrWnACNXMdl7AWZI6YYKrmudYCKa5QS8C32rN4WDX68bt81AMMHfCTcnC043atpe4TtYY_C_BBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c763e8ae68.mp4?token=i4qNiJhxJvK_X-WEQ5_u1UWE9MIk2Zn-1T6T512rYS2jtQfKVcQnamYbfHc4BTf31kgHBMzdxPPZ8hmHhAG1_3Wi51prOTiC5MGvUD9O2kDBLPFdH0i8Ep92uFyT3LINrMTgxUu1RwBO-Xa_uZZ_EKeRrOuxln82x6ywOIMYDA04IFHwILfpj0y_MXFA6c95NRUtwNARsPSu05vKutP4yvAzJx9bdEBGFXiLZgI-XMgnugEOyLsrkYb0MzaFzByVokKB1ACvNoIrrWnACNXMdl7AWZI6YYKrmudYCKa5QS8C32rN4WDX68bt81AMMHfCTcnC043atpe4TtYY_C_BBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعطیلی ادارات مازندران در پی بارندگی شدید و طوفان
🔹
در پی تشدید بارندگی، وزش‌باد شدید و طوفان، و با توجه به آبگرفتگی معابر و اختلال در تردد، فعالیت کلیۀ ادارات استان مازندران امروز ۱۷ شهریورماه تعطیل اعلام شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460818" target="_blank">📅 07:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460816">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253c13e9c9.mp4?token=IHdYnmV_6RaD4TDgwDc9OQaIZWYl_6hR8U4ZstsrFZFf5-7WEWfcvKeJAZTX5DHFb3T9c1gIP00ED-Dt3Hb4Hj9TifbSf79S_wn1e1_af0YAu3w9x9S78_fbRIQr0xotcyJQ-g_C2O4WOgE3sxyayQxYav97cQjjX1MCnO1lbHwRkuBV-d1Pz2iDRkm93VBvB_WigYo2hEnfDR2CBkJz2tmg_WEh_o458ceibzb2EIQrNGRUxsAD4nSlQlL7PJuoa4x2qopsLkCY5zUvS7NwGIK9Q9GsUKfyheWQwt_hCnYOd-EO38_cut05zo1cXL-JRneYhUqXMR204IzC19hp6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253c13e9c9.mp4?token=IHdYnmV_6RaD4TDgwDc9OQaIZWYl_6hR8U4ZstsrFZFf5-7WEWfcvKeJAZTX5DHFb3T9c1gIP00ED-Dt3Hb4Hj9TifbSf79S_wn1e1_af0YAu3w9x9S78_fbRIQr0xotcyJQ-g_C2O4WOgE3sxyayQxYav97cQjjX1MCnO1lbHwRkuBV-d1Pz2iDRkm93VBvB_WigYo2hEnfDR2CBkJz2tmg_WEh_o458ceibzb2EIQrNGRUxsAD4nSlQlL7PJuoa4x2qopsLkCY5zUvS7NwGIK9Q9GsUKfyheWQwt_hCnYOd-EO38_cut05zo1cXL-JRneYhUqXMR204IzC19hp6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعطیلی ادارات مازندران در پی بارندگی شدید و طوفان
🔹
در پی تشدید بارندگی، وزش‌باد شدید و طوفان، و با توجه به آبگرفتگی معابر و اختلال در تردد، فعالیت کلیۀ ادارات استان مازندران امروز ۱۷ شهریورماه تعطیل اعلام شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460816" target="_blank">📅 07:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460815">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
تعطیلی ادارات مازندران در پی بارندگی شدید و طوفان
🔹
در پی تشدید بارندگی، وزش‌باد شدید و طوفان، و با توجه به آبگرفتگی معابر و اختلال در تردد، فعالیت کلیۀ ادارات استان مازندران امروز ۱۷ شهریورماه تعطیل اعلام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460815" target="_blank">📅 06:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460812">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5qtKI8iobiSPhtA_l35vr6DawiKMv7FHoQ8kHk3qa1uprp41WdG61lEdPF3PBAtAKC-sqwuW_OekjMNoq_MYbOYAH5TZi0hS04B520smO5jY2y3t6-mxz-iwy0o-Gzz4QlPflLQnodsn_1MKDc9-iaiW8ILeS49MvzRx00E8xJ1AyFoWfib0SDdaFc2kWSK4zStHsuKmdtCF3iXYQ7nBSRKTiCbackCySAItmp4m3FF6QaFF_Qs6BsD8gtgFtrTPzc8nfLgQBlbdFHo22U-3syud4_MZdeaXyXAOaOWU1LQOaH5uDcvoeXxsPKpfLF-PbfNgC9EAlC7tRvtqVCnrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ct2LyK0886BowicFtxLDrgMtJMQHOZ2-HkFMUGQNWJP7HRWFypxFGPxZeQFM2AMiaQrZw2J7h6dZamVZk2V1gfQx6_sxgSGAuOpr8FvQdVI6_wFRs0IMLJ4MwZH4iyiI5I4KF8WbuvQPa-0TzmbQTijlvK2SfKqdes_8lMAo_nlpTcJJFOvYzS8BjzkPk9ExV21ROjeK3KZN9yVrOBbcYLKK2e2FBFhMTBzE11fRjtj4RrYsYss5Tpw6kMroCv2_3YPBki2yF4Sgd16zYulOmDOUVpG0pLWvz7SwADir_Tmc2QmtiQRyTuPZmJ476RbMzb7GCkefKrTYzWboLHDkhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUnwNExslssZufYD1b8PKteRVjxrvamnOvzChVlTKejL0CmMozejO_UsQv000U0grN5sZHR7le9xKw0o7oCgzLWzjTgPMBEmtQDcEd_-uUKDcqhzSSea4J1kCdWytc5R1dLL5QcToL0Ne2_s92jga_dtEYs3146m6QQM7jnBGg0xVbH7xRp455a3ALEF-pWv6Vv1CahzRPUMtQX2YFfYjYBUaoh8yz7XS7w9bqpMVkJVuiBW_5fKmzRQfy6au6nmVRURxrKDmm-z-l13av8FGEwBpGfheINOsj62PYSwId1_rcIHnBNh-icdChwYAHfn4yud7Ei-3v52T6C-dw7qDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست کمیسیون امنیت ملی و سیاست خارجی مجلس، عصر دیروز با حضور سید عباس عراقچی وزیر امور خارجۀ کشورمان برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460812" target="_blank">📅 06:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460811">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اروپا برای اوکراین موشک پاتریوت می‌خرد
🔹
باوجود هشدارهای مکرر روسیه دربارۀ ارسال تسلیحات توسط کشورهای غربی به اوکراین و مشارکت مستقیم در جنگ، اروپا تصمیم دارد برای اوکراین موشک پاتریوت خریداری کند.
🔹
منابع مطلع اعلام کردند کمیسیون اروپا درخواست اوکراین برای دریافت موشک‌های رهگیر سامانۀ پدافندی پاتریوت با استفاده از وام ۹۰ میلیارد یورویی اتحادیۀ اروپا را تأیید کرده است.
🔹
بر اساس گزارش‌ها، کی‌یف باید قبل از تصمیم‌گیری درمورد پرداخت‌های واقعی، قراردادهای خرید را برای بررسی به نهاد اجرایی اتحادیۀ اروپا ارائه دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460811" target="_blank">📅 06:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460810">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حملات رژیم صهیونیستی به نوار غزه
🔹
المیادین: تانک‌ها و خودروهای زرهی رژیم صهیونیستی به سمت مرکز و جنوب نوار غزه، و شناورهای جنگی این رژیم نیز به سمت غرب این باریکه آتش گشودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460810" target="_blank">📅 06:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460809">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7FxBxbNygtJDcN2BCxUvOkAbG3_u4fKzl27_BZqGKXc0UvznJorvRw0-5D1074XDT19ciBXuTYJvUcSRxMrobZW8HXvuwlVuEDdMmLHjgH43nZgvgijvXJcD4yO5LK0UaHKyj4TX7g0w3UL-t0ScPSjKRgS6rfQqcF_F-3R-bgKVOnlvVLD6pFHtx-nMyyf7D71RCZ7x0_76vU4OweagBZ1ucbnBIex__rhKDLgbIToQqJ7rPZ0Wli2jxreIeLY9sJ9_hldbGl1U_YbwuZGBy_5rHevvoajiaPXsxTOE_GIVsghM4tDcoPG3UVdDPTtr6I--ZPobXWWwXx6dAZlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارهای مهیب کی‌یف را لرزاند
🔹
رسانه‌های اوکراینی می‌گویند که ارتش روسیه با ترکیبی از موشک‌های بالستیک «اسکندر-ام»، ابرفراصوت «زیرکان» و کروز، پایتخت این کشور را هدف قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460809" target="_blank">📅 05:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460808">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bff62194.mp4?token=PUMkzMJO4-hTLnWKN1qhLAPKGL-TrGFrw-jcqh2nNSVyFTruWbwppfyzCI4J5FqjBiy-5PsUIxAvp0AmsHhZD9zFY-mzfLFmD2jR0M0GDj59UIhZJ-AJ9pZnDUbZPYT3u1cjvSc91sgDt5wRGzyclQPGrszzDNM7Gb_QybZGL1Yd8UPONNuMO_DCRh2AcsQQ8zBNvz-RRC3MxviPQpm_1kGlfC3Gr9St91nFoxJny6KKeMkNHT3Lt7XLK_0giqJEmZbIw3X8_HJuiCfFdvsMuHXQS2U6oz72KiTsxYju6v-VooiuizBgTcNVkGt9pcl2bCzSnkanVNwt4F8msVhgvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bff62194.mp4?token=PUMkzMJO4-hTLnWKN1qhLAPKGL-TrGFrw-jcqh2nNSVyFTruWbwppfyzCI4J5FqjBiy-5PsUIxAvp0AmsHhZD9zFY-mzfLFmD2jR0M0GDj59UIhZJ-AJ9pZnDUbZPYT3u1cjvSc91sgDt5wRGzyclQPGrszzDNM7Gb_QybZGL1Yd8UPONNuMO_DCRh2AcsQQ8zBNvz-RRC3MxviPQpm_1kGlfC3Gr9St91nFoxJny6KKeMkNHT3Lt7XLK_0giqJEmZbIw3X8_HJuiCfFdvsMuHXQS2U6oz72KiTsxYju6v-VooiuizBgTcNVkGt9pcl2bCzSnkanVNwt4F8msVhgvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازار سنتی ماهی و میگو محلۀ پاشهر بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460808" target="_blank">📅 05:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460807">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFQFt-LatKsPSxpjzyJQYyPAQ4q2OmksSI-HapcE0QkHxKXAQ7Rj4acD9XmHJIvZzLS_XzBU7Wl-B-mhb9YakyYnInQaySdp-9wIcNpzTZ5wFu7k63F7Y8Qz4lUREcqcK3oqopfRe61Mxm9YhpTUxE0XxrudP1acEx8EKy60vgXISPoyuf61FJMiJc-eHJJRfrKE37ClLj8PxltJVNP1YLiUBTdLjeWioWJOFxDL9nOdlZD8fyAjbfceVUeIVZnCJ5C5aLcTpYXldjDiGpn9u7D5H4kPxfQtBboBLyoz6XmfWn-ZRZTFe_JX0Paequ0g03qkz-gPlLE4YZRhsR7orw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش ماکرون برای ممنوعیت شبکه‌های اجتماعی برای کودکان از طریق اتحادیۀ اروپا
🔹
رئیس‌جمهور فرانسه در نامه‌ای به رئیس کمیسیون اروپا خواست که دسترسی افراد زیر ۱۵ سال به شبکه‌های اجتماعی در اتحادیۀ اروپا، به‌صورت قانونی ممنوع شود.
🔹
وی با بیان اینکه وضعیت کنونی نیازمند اقدام فوری است، پیشنهاد داد که در قوانین آیندۀ اروپا ویژگی‌های اعتیادآور رسانه‌های اجتماعی را تعریف و تنظیم کنند. همچنین از همان ابتدا استانداردهای ایمنی، از جمله محدودیت‌های زمانی برای استفاده از پلتفرم را معرفی کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460807" target="_blank">📅 05:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460806">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127c8d7ef0.mp4?token=Cr1CHcZHrQG9bkxGnA0RoaFsPlTmmpvra-rjGzk45NoCqwNJbibAU6yAVWGCvA84TDiA2eILtU7ceYJ7NNLjg3mVxhaptg7JPMvzbCEEgOsgRNhiV9bYSy2oXRo2L_NcOFtIFvzHToZTbUwrcEWj2x2jg7lvPe3x0VuJ631hUfzS5wKZY8ay7yhsHGZbmZ_bL_AwLJHapRNQAasjeZatlemOKHdPWKbbJPHF-wSmHtY5k_l-8xuELWsph4p9kLY17FvynjDyUGs_THaMuUknpQfcLPVkesTt2jLEgPAJ-tuBPc8Mjt-zVwBdBEYmgdADJKUW1FpxjYws0v8WUuDCgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127c8d7ef0.mp4?token=Cr1CHcZHrQG9bkxGnA0RoaFsPlTmmpvra-rjGzk45NoCqwNJbibAU6yAVWGCvA84TDiA2eILtU7ceYJ7NNLjg3mVxhaptg7JPMvzbCEEgOsgRNhiV9bYSy2oXRo2L_NcOFtIFvzHToZTbUwrcEWj2x2jg7lvPe3x0VuJ631hUfzS5wKZY8ay7yhsHGZbmZ_bL_AwLJHapRNQAasjeZatlemOKHdPWKbbJPHF-wSmHtY5k_l-8xuELWsph4p9kLY17FvynjDyUGs_THaMuUknpQfcLPVkesTt2jLEgPAJ-tuBPc8Mjt-zVwBdBEYmgdADJKUW1FpxjYws0v8WUuDCgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افکارت را کنترل کن
🎙
حجت‌الاسلام رمضانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460806" target="_blank">📅 04:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460805">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">مسکو: ایران، اولویت دستورکار سیاسی بریکس است
🔹
«سرگئی ریابکوف» معاون وزیر خارجه روسیه در مصاحبه با خبرگزاری «تاس» گفت که تنش‌زایی‌های آمریکا علیه ایران، مبرم‌ترین مسئله در دستورکار سیاسی سازمان «بریکس» در اجلاس دهلی‌نو است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460805" target="_blank">📅 04:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460803">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSIrsVmAuj2u_RIwsUqs7bZt5aNApyGCKsKj-LGPGsUC2NDXaymuFf9gDlzjcwOA_8UhNnEQjsij50wCtQ1rpUNd8BGVgiQ1xl6Nv0hngAqZIw_E2mOdzNnLclXBtk03nE1itJqfkuDSWp2COEyACadzFIqGo9HPDrKSsHsTAukyusfn3F9MMoND0INN_ha9oC8JYEaFqfkSR8p8KDkC-eWebntvFXRPc7J14cTe_n9pzN51Qgisb6myEEuJ8X2k_bKau3pd-ZmRtfMD30aIjHJ6yYQI7huAKvCK_UM1zZzT4e-C4MDxWLhUNbDrgRLwDLDbUBh7gYUzXJoc-JHP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bu_0FhsBO3wZS-zecPovFbddXFXAcEz0U4RoztxGe347HKSCrD00h7HHAZT9YJcMFpP-AYQvCPNKjXk0PIIiLwtofQ5pvN5eT-j9oBrdDrz_Sx1nIeb1gMpcp-yYYMTfr4amJW_HS1W39YmCIIgTOCXnVnMa9J7Dyo-Z6Nj2f8FEosLR7RGGuQlMUR-OOKjdhx1TZEDrPg9fM6KE0UnPQNv0Q55AK_XKYfmdDq2o7VW3DxZje2L00jEgmAMcG6c6Q6hfYZkkjrfSnmWtyJzWvhiSFyysVJbtrTACpg3H7JLdFUegDxkEpvKXEhsoUAdGT_ktpc1sndgablo1rqNXKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ گزارش‌های تاییدنشده از حمله به پالایشگاه «جیزان»
🔹
رسانۀ عربی «صابرین نیوز» نوشت گزارش‌هایی مبنی بر برخاستن دود از پالایشگاه نفت جیزان در جنوب غربی سعودی دریافت کرده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460803" target="_blank">📅 03:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460802">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Starp4piAGNpbZFmn379_X70LuiXkzJo8LPfEnaSReKP5ypd4GZgNLXWb89xxD9b2DyeK038xb9zLj1DgLUvHlORfiL_DRmO80Cjj3vIw5zfiSod6r9OED_6fwEOeqsl6ackLbnqmMMN2nAlRpwzDnxEnwizKIedBi3SLstTODq9GvOwH-fb0p3x5qLvFj8aPvbeHdgchMkCyx7Q7F-0oOy73Hi2GT6wCTP9ZB6XhMs8d8qWLwfANdUamroCuwTrYEARum8h2Lvm_IAeUaSMtE3-v_B1YVG5bv-bvmMFpSWKQdTeMVb_XqBIo_OHLupnUDrkGLf1btoyAnXQLC6fQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش دوبارۀ ترامپ برای گفتاردرمانی قیمت نفت
🔹
همزمان با نزدیک‌شدن بهای جهانی نفت به بشکه‌ای ۱۰۰ دلار، رئیس‌جمهور تروریست آمریکا بار دیگر به گفتاردرمانی برای پایین آوردن قیمت آن روی آورد.
🔹
ترامپ مدعی شد وقتی در جنگ با ایران پیروز شویم، قیمت نفت به سرعت کاهش خواهد یافت، همانطور که هر چیز دیگری در حال کاهش است (اما بیشتر!).
🔹
وی با نوشتن آرزوهای خود، ادعا کرد: سه دلار برای هر گالن، اما در نهایت، زیر دو دلار برای هر گالن خواهد شد. همۀ این‌ها به سرعت اتفاق خواهد افتاد و ایران هرگز سلاح هسته‌ای نخواهد داشت.
🔸
عصر دوشنبه بود که خبرگزاری رویترز نوشت قیمت نفت برنت به بیش از ۹۷ دلار برای هر بشکه افزایش یافته است.
🔸
بلومبرگ نیز هشدار داد که در صورت تشدید حملات به کشتی‌ها در تنگۀ هرمز، قیمت نفت ممکن است به ۱۲۰ دلار در هر بشکه برسد و اختلال در عرضۀ جهانی نفت را به‌دنبال داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460802" target="_blank">📅 03:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460801">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎥
پرواز موشک یمنی در آسمان سعودی
🔹
گفته می‌شود که در حملۀ هوایی ارتش یمن به خمیس مشیط، پایگاه هوایی «ملک خالد» هدف قرار گرفته است. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460801" target="_blank">📅 03:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460800">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb721b9567.mp4?token=tvHsQb8uAuX54Gst79Si2zDvYmI9sSUnz88px5-CdJXZbHhvzTZ0TVp3Dqe524QYEUsbN5_TKiSwEmMgZzDwmIJZ8hUuSwJUrlqhW4_0nISekrLLNHwQVDWfKXSiQChH8ToA1tiWGeZn6g2yAUsd-iFxMlGn86zS0U7jNVaz4GqPn7AnVe4LUg_YKV6xLK99CMD3v6HHt8ox0gQomeVJmO2uGMJFStSkMkWwBj5vYiooIUP1pFFb158jV-c31FRPuU27tdjTKH5_5sa4Di8NzU7zxEb_T86Cb4tycj4Zws0GvuPvTrgKhlips9Bh-yD0Gc3oo3EQP9kWgRXvvExMTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb721b9567.mp4?token=tvHsQb8uAuX54Gst79Si2zDvYmI9sSUnz88px5-CdJXZbHhvzTZ0TVp3Dqe524QYEUsbN5_TKiSwEmMgZzDwmIJZ8hUuSwJUrlqhW4_0nISekrLLNHwQVDWfKXSiQChH8ToA1tiWGeZn6g2yAUsd-iFxMlGn86zS0U7jNVaz4GqPn7AnVe4LUg_YKV6xLK99CMD3v6HHt8ox0gQomeVJmO2uGMJFStSkMkWwBj5vYiooIUP1pFFb158jV-c31FRPuU27tdjTKH5_5sa4Di8NzU7zxEb_T86Cb4tycj4Zws0GvuPvTrgKhlips9Bh-yD0Gc3oo3EQP9kWgRXvvExMTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادامۀ حملات یمن به سعودی
🔹
رسانه‌های عربی: با تداوم حملات موشکی و پهپادی نیروهای مسلح یمن، صدای انفجارها به شهرهای مختلفی در جنوب سعودی گسترش یافته است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460800" target="_blank">📅 02:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460798">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e0682df0b.mp4?token=D39qmd_dLq1K5_Rzb-BNtZQOqoSNClVqWXGLb8FT2UeZNk-75lvOFHkB3WoG-8T4QHRFZIYhClIaCUK2S_e4Fmo6_oAVUVeQPGqghwS7xqsX8AJWCMLa7hYQODwBzPD2AjTMZsq7W8_R6zelUjqBMlF2oUtteMS770FUTXCY7IQvOUV2kP_QKVfakOnzGGTYyfQRrYrJBbDbquc9HygR39gpVZkdf4oHDMqNXm0WLbNLLbFMu6Tyw5tyLF-0JLqVNPcJq9o75DMF7WTGzS6QwvCpwtj74qcmzuvarcuJfpMEU6am6OO3V1kGiRw3qAEZ6tBoofJ1Yz1ggZH5b2KdXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e0682df0b.mp4?token=D39qmd_dLq1K5_Rzb-BNtZQOqoSNClVqWXGLb8FT2UeZNk-75lvOFHkB3WoG-8T4QHRFZIYhClIaCUK2S_e4Fmo6_oAVUVeQPGqghwS7xqsX8AJWCMLa7hYQODwBzPD2AjTMZsq7W8_R6zelUjqBMlF2oUtteMS770FUTXCY7IQvOUV2kP_QKVfakOnzGGTYyfQRrYrJBbDbquc9HygR39gpVZkdf4oHDMqNXm0WLbNLLbFMu6Tyw5tyLF-0JLqVNPcJq9o75DMF7WTGzS6QwvCpwtj74qcmzuvarcuJfpMEU6am6OO3V1kGiRw3qAEZ6tBoofJ1Yz1ggZH5b2KdXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش‌ها از وقوع چند انفجار در جنوب غربی سعودی
🔹
منابع محلی از شلیک چندین موشک بالستیک یمنی به شهر «خميس مشيط» در استان «عسیر» خبر دادند.
🔹
صابرین‌نیوز هم نوشت که در پی حملات پهپادی یمن،‌ انفجارهایی در فرودگاه «أبها» در استان عسیر رخ داده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460798" target="_blank">📅 02:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460792">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_nQ_Kafdngh6Sw17perPOV6aRv82OJlasiJ7LR5wL_qEATKVJ8Z8fYg_tjCNmZVjCEu7sHUYXI2zM3RWoxkdcyZo809uunRz_KAQCdwK0PijFQJYwek104lyHIWFt7cLCNtcgflbGfHyRRBB6hz8ik_WmPmjSa8gC8GPEqUI5GbJHZ2KzUda-3yY0DLX2jIl_4LjfSxnEZP7jmMX6d9UBBuDQ2litKd3DNjkJFKXL46Ot3F8LbbgIhAhQS8pFwyoO4zh75fmYKrR83873MfeXpON7A-agtS7cvSaPbE-2OzgLysuibr3OUFpX5tBOSJi6Z1E1x0EArEHNetak7E2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQ8vzfioO7fNfFwe-1h-71kdXvsRzzqg-BXC89DWAAkutjgP8xTrHV9y1ueUomiL1_jefbVlUPK-plsxItyzcT4efJWbt4rAkLbzmT6i_a8sWIWQGZZ8ISrVtfAYJw5mLiqVnKNEOGaYxNu8saLNmKR-uArKE2a4VBnlyzZGUGqEueQK2ZkHbOvv3pi7vh-by1tpvZo8DfCGNBK38otEqVvAHXrNI-PDHXPa4gNf67M6y496IpMOzvswRPbTBfyqL2QQizW5RxNu7hZpJjOrH0jnChQb1xG_7m8embDRyzEgtHRk1IJpIbsqKBWbTBhqQCFs8L9w0bjx1-WkUjdfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhPJqW-MxWSGs74SY_YU305gXBJ3xM9pAvacANaCvmne1sMtoUrjVwFvUpGe6lHw5bmvant5IXVk14iBw97wJrx15V-Qkh93l9kXV39s372MZIcO7hWA08qs-Mu7PjjVkKGzwYosQj_JOMWDKCBteubyszJpjoyWHMtDpdMWGx0QJkER0LC2oSuf0uf00NPFL2DCDaXyvYdSoHHlFqSpkN7g1SV8ugtMy_5UrNp1OVwT6CuK5vvjTByleuPJThV6KCxHV0VHD4BFdvMM130Zy-JLMguFE8mVEJq0jhdfiBICMPNaTkIlSNAhPTaEb461SrSNHoyUYuFp4Y-OHtGFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpkZd6vvJBfuOin2kbkKE_7fmiT0flKYuh3nOHMFXgt5-98ZtNNE3MZPJSIFyaibexUq9ZDvgIx8tQxCoh0kfI6PAhzXHJNImM3tU3nYVLZfYn6MOsIXA4JNRinw3RKBoHbKr8Pl18lOyH-Faw4EHR_ZSIi9hTvTxzXRirPEQJ2Kd-0qIGxUIZzgxHqAgsd89yLi-OZO3agQU34Hk2cu-X-7j2YtkDWXR8LzsuWVaGCokD80IEMHulPnUwhQJFMoLq8qLhLqYI3Ah7J0zjmHNXTooRCyh87wPd8qG-BwIqngFd6o6OR-KhqZ_aQ8aVkov4P7mLziUJsG8fqnQTnaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nywRlr55aG9v41ZbmF6726Iv5ukkI3YcBmIOzKiA9hY_5yuWkiDnOkPjXY-7jIfV5nW8LPVoEyXjZRlcsFV4l4eATm3OM8UZA9WZUbGz5aConUWt7u_sLOWx_GiyrPPQW3iXHg_XdfogA0imk6_VuwWvq5ROfJvX3epfx1YoDP2T5XSwOQVynLZ0_jsB2yotx3pxNcI2hg3l8qLZossC-KLdowQpP466sbhY2kJ5Q3bNUNc38BvYBUZVzEnitaJhg8WvHx2avjB4gm0wr1vOc9jefWvX8I-vqZZ7CnSuh7hxh7MLIFCW32eXM-4AU-u1s5WMDQOoIJU8EcC9AwbXvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYW27jlO-swUfBFUCPORIogYVs4Bp3Le1AMp9-WRIGD8Sk2SVKg01WdYxPiOJ8HVgmBCsUR0uVMgMsvlKQU3hqm8LXPWRswk2sMMloI_lAH0FlZExT3HOwLCVPj-yS_UTVYFHGz0e3Ivk00V7zp0ZWquWGTuMRjBRReERTCJxe_sy612P2Aq5sUFrb0StLeyzfJ-qpuQsom-cfKUcqiVo5Q_ZrPQdBnAOMmc8whT15tNW1BwMTC1Ztovq_8-Ig3fR845jIXrd7YdouSwc-0CHSjS-BFWHeRz96XwdHFebXBSdhxfq-h67XiohIXxFHYPQdbU1pgPuntxxBugvpjA4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۱۷ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460792" target="_blank">📅 02:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460782">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Evry_tCKFhOUbkD1x6Zl8xnHxKhex2-Pe7A-boC2Q7jI52JGMJVG4EzfWQ5wbWg5sD0V_qlzdxEfTT0tCnw7oUv2dEKmowXbzkCbiNBKihyoAXLPuiDYY999kmO5OrfkbHOsbXelvJ5EjXW9oXcRcshRguVr1s4TpQVxhaHZ2H1GjCDUHuMgvIYeRN-zsf7VsjOgLgwNa6P_5GrypsNnqBCgJ4iecgjBkoqsOt0_Y_DzQTrmfuR0Au3zABaHyI1_2QLuuvxkIKS-JifnV_qWRO3kbhrLFWUVmNlVdOeFvkQ-vkdzvx0dhzXSUtcJ2CSXwMGOpF3PqouPI9mA-VLYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uH_UvHkeL9zBKiib9orLZMq-3gu0L50v4Y0il7grVpZjl9IqH7XR-gVOgydcbEoyc6PRygiUUV_EHKosCe7aaVvSFJkSTy1U-YZAp7sPQGbjYLtDm17mHg8HGS0PnmR9Wz6haiPMiVz3F_OTZV99ixPO_uwF-3cYy529JXfJRdZ0xz2wKg2XLl0g7ICYsxDyNLg8dvj2Lt_8pT9phZnPLM2vPh_g1wSeNA0Yl5GrBmBhya_iEnBraOcY2wgJGbET0QWkzvMZRfKnFTynSxp5g7ht3FBKZWKVAtFoS3gSVTo3MLbqlIXNbdFIjH0eGN8wE1wKdLNgBJiDmsn3e59TXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSaRW8fu6NOnXqpLM-FgsqVdbGHWfGFqQmDqJBwPW0f8C933VG14aB0w0RdwXnzdJ16rya0nF5V7iACizrs2x_9L4D-yNE0BCz3Ec4dqGs0-BHxVgWd7vqGgyLepcy1VRTjsmBQnIzz1Wt7RWZPuOQ4CDGTIbuIlEoynYO6_APDjgmrLmzT2hg4OGp4IzXCquAu-gEJ2ArEjAwa_CQlRoHUFVrSVOxG2fstKgMmv8bw88XuxI2J30eW2s1tfCQimKC-PKaLwKgM3553s4xlVC_5X4JOsJJbmsgy5dLzW-7UAVr0NRB9ww0HRmFmWFaYKukNNwcinRC9GmTSsBqGlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdsbqvl0bHqCGh74MRqJ4bm2W7GRHjdQAhmX8NHjqe8REeFyarTBghZq8hoTpBYRVCZrJEFjdIbNQX-XNS_QavuGkr_nO7uE7n6gBS0vKGcz3BsgeGaDrRRdlTcVt-Tuhb6o_s-a4_iKZGk3Erhpgsz7olXmI67lqNe3CoQ_us-iwRh41ReNU0nTHGT9vEnTav5YztiZ_a3XgiBNP9KIQomUrzXoWI3F7ZQCua0ON62vxpVGkYNtEUUY2Hq0iKlVwXxLiDP64TpXo49nyVc-vWHM1x7NceOp1v05aKlpTk6cREQaJ904bHqJfF2OlEZk7jpQA38tzHIPd_b9ED3bQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SesZeH3sJ_P76yFcDd0TJfOhYZ0DDSR_M3IkHj9Ik-DDTSoV2K9he_wgJXPHKsezGqfriMUQi-FUqlh31Z7s9ut-yXPypNwQYS3jyOl7y75uwmzfSR3ugLzhxHelEx8_Hh7n7NaNGQ0fj9oR-y2YMBWtJfFibzab33_-HhlfXt09KBdWsnws9vV7Ar7TKEC2oPFxU78ZlHP9JvESB72JdNqYxrbw4Q4GlLRhUsOq8Ms0v8FEuI0UBbl6c1jLwcdSIrOffBP9mZndnVouDcE-_Tp0GbazD5BtX3Tes0Egp-U50iajRUsuufxXi56Lj6-FBEeLGB87TSTtxjvVdXsHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWtyBxDYE6i7YLhCDfGEzqTkGmexl_SiRyeb6OVFoVJEtPMiHVKXcwpFEEqFl-nBiZRIFGPAftgRnaf3f5z2AKBCLEjl0BNT6GXBfbbVYVvkDlky9zZ7bPXBs83oxduTNnUUK3yAuQl07fSkcNHQFOXaGG_GuDo5EG3VqU-bCFZx_Ka04BnTnxGuIyaqfGeqh6siDUqAwdmPH9yMiD_bmnUId7Bhbzb4B0egR3Thi63eOatFXB6TTvDgdyOxtSeBuZl-M5VUopAAzaLBZ7t1ZAZOfDUETlFaP7KfN1P1kePwEagt4SLdtMBn9GBd7snglmWU8W0o1uaok4n8i0QhRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txjesPwApvU5fKAx5-SeHZiW3TPcp27hLBoHRQkXiDatbIgekdqLDh1kUgUkCHGAOjaPWI1odeYNWGwdWQYUx2eL94VbwHF3nA9OeUv7umioUjY2_oQl6QqXbpEAz6S00TQmqDxGiBaFATqtlBTaMkx7OZETQbuwbTGGG6vZec9D_PafseRZ1UdesLEqgAXrXD84rEn--Lj8soOW2qXFF6ODF1eNwX1lamkbFrlJhzuZ9BWq_yh81HUzFfXK6gOsqI4X4vTYrA5Rf3JpE_C8u8-REstRC2rASkTBhCx2vaYdgHSl8kecxx-S5SOlcHzbjWbXVhlD21CQxA34Y-fy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4IR2oq19w6_MN2aD1nPd7DqXnu4NhdvBeQca4LT-SDlEmmSMgKt0ABhrrlLHNMpk1Y5Zu86UCX_YIUiHSeS0KejCVyRqQq5MQ06Zm23Z9l40GYE-0DQ4dA23ZAA8RT6tDjyfMO9MWYAkRxb78ZJ8YfafbWZ6zy8IEasKVFz0pn77Hk1W6mUtw0Wget60JCd1xIyTnnPh83rY7W-4XI0txBPY63djUL_Bwq46FXSHqTdTjFo9x3DtP5Ef_oZuYYiV3Cmc-yUlHFK2wluotmlssiUY0MHZRUU3hqCsORvpdvG2j8qW7driNo0Yqo6k-VPHPq5OIuLbe-Vr_sKvQxcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUgT5tu7mnxPG1hjOO6lSzw_VKC9M5b7xZ4qmc3Chydjk1RNbamZhg8NZcdmva7Vxxudi0lLzqYRrAaVTPqOOhTEi0YSPzwsE1TGsuJPsNq1sSnedRs1yhY8vTDwZs9CJ8evpTY51S-zw3SUf1zSxGFRDrHP5j4Cu6_ru7auf9FqX9THZzztQPzud3Lel_z1SfEdVZkgxyNDwYFEq0xN91gX5lHqudDwFendtrbiQrtnhraiAJhmPpu2_QslAoGGtI0__cw5XVo_uwalReQQ-r5-4Vj-t1z_Q4srldIdou0JHbRrw5vHAaWTIkeYy4mpES68WXX638RMrqFQxMWJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRbqBkAAvdOFiK1mbFNxSxzQAVDYnWIPKKub9b--h-Y9Dy6lnioTblgRe4U9cbwO9bC5uDp7hTr0ki5t-WT15SS6hzc2hkGHPe-MBGxEasD5UA5ulk38y7qb_7UWem9Q5YA3Y3X99DgyxLiK0dbnj5dseIcMZfc5sUXHngt_Ns24tz-HtCozG0dmmdkEzqydjNuw-SLVSI5k4ZT5bAIswuW8yXwmcBZI5fLu-AfwUbULGQalokRtrgbJ5hdga-8Sje4VuwntYPEWOlrkUKOB3n8xxZknOW7B2AiXEY9T2aBg3GrG0J0ySAnsxxkltSapwu3mBydIa68oQujBVk_j7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460782" target="_blank">📅 02:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460781">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش‌ها از وقوع چند انفجار در جنوب غربی سعودی
🔹
منابع محلی از شلیک چندین موشک بالستیک یمنی به شهر «خميس مشيط» در استان «عسیر» خبر دادند.
🔹
صابرین‌نیوز هم نوشت که در پی حملات پهپادی یمن،‌ انفجارهایی در فرودگاه «أبها» در استان عسیر رخ داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460781" target="_blank">📅 01:51 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
