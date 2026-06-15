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
<img src="https://cdn4.telesco.pe/file/gF2A3lKwkaisNQhpP8hTq1fpplwJXLaZw-Fcv2GG6qOMrov4rvWb9o_Cbk4OGVomY_RL3OrgIx6DsqGlOOvT_vsyzVfRk0Jg_QDNG7RfKZZzTeTnH48X6QHN44a4Wt3SE238iKinUvP6HbeV4IuOUQqaBPcnc3vL0CEhY-4hfjSVwRpopcwmjkgo5qeuP237ikeas8PH-wnA-c9KyGmZkY5HG7qUtwtCv2ePWudgX2Cnw7-QCgoeKs7SesHJnp8I2QBr6JW25APCZvvMdeQg7UYdFwDBPY9TiVkAATqCIagdh9vQcQXiIf2HAOpj5kbmBlR2_ZdnynX_76yFPuv-rg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 22:33:11</div>
<hr>

<div class="tg-post" id="msg-442376">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">منبع آگاه: ادعای الجزیره در خصوص عدم شمول لبنان در تفاهم‌نامه کذب است
🔹
پیگیری خبرنگار سیاسی از منابع نزدیک به تیم مذاکره‌کننده از اعمال برخی تغییرات در متن یادداشت تفاهم طی ساعات پایانی گفت‌وگوها خبر دادند.
🔹
براساس اطلاعات دریافتی، یکی از مهم‌ترین اصلاحات انجام‌شده در متن نهایی، اضافه‌شدن عبارتی با مضمون «احترام به تمامیت ارضی و حاکمیت لبنان» است که شامگاه گذشته و در جریان آخرین مراحل جمع‌بندی متن مورد توافق قرار گرفته است.
🔹
پیگیری خبرنگار سیاسی از منبع آگاه نزدیک به تیم مذاکره‌کننده همچنین نشان می‌دهد در یکی دیگر از بندهای مهم یادداشت تفاهم بر «خاتمه فوری و دائمی جنگ بین ایران و آمریکا و متحدان» تأکید شده است.
🔹
به‌گفته این منبع نزدیک به تیم مذاکره‌کننده، همزمانی تأکید بر پایان تنش‌ها و اضافه‌شدن بند مرتبط با لبنان، از نگاه برخی ناظران سیاسی واجد پیام‌های فرامنطقه‌ای است و نمی‌توان آن را صرفاً یک ملاحظه دیپلماتیک یا حقوقی تلقی کرد.
🔸
پیشتر رسانه قطری الجزیره به‌نقل از یک مقام رسمی آمریکایی ادعا کرده بود که «عقب نشینی از لبنان جزو توافق ایران و آمریکا نیست».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/442376" target="_blank">📅 22:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442375">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02aeee65d3.mp4?token=OUCIS8m5LHrD6YZvtSmvh-VAbvIuIyIyWs1V_PdSRdxvLmJceypRzztrQRacqtzDHRl7k_rM11IkIS3SB6bRr9kiQzffowMFk2XHsGcW2XisW19s7D9CoGpfuxpCfF6Y6UBLUsWbZtXb4UMecuHzfg-lIgFE3sP0HsxYvMVhBG43XN5T_MF9fVrTlBhec3JvLeXEQPw1uhXcNtySaFO3-6r3AfknUWHl3j7UEy5161uqdtF8hZ37I8vARle2MMwO8yx8xcfp9vL_9oSh5ODgjC_8mzNOB0m14mjdhhcYCmXBmUqZrGNczxCXA18Y2V0quuGHyycvG6YAPt3Un2MDhFHuEMRKGlB-FWhnp7iEur8kHUX4XPsX0CmlLbtLxnRgWRmR2GXRxafhN2W6ozCQnHeUbDJ7I50UYG7nfSNSZy-EqT9Ny3lfqCq09XSKK6NHRpPCg2XBpeq90O4q89pf-E53KPrdpY8sf8ElG38TIRp2lKIlyVs17eWyDcboaUhLnAA5nY9_fddFPqea2MgxU8-oqQRDiVOGCyRKHdXiIrXYcCAt93j7m2EFNEL-Pqgjck58A0LP_sCHxQLvLcy2nqKcffnvzZ6di6vMX-elp1lz2aGIO-tVhs1ifQfiJX61grWYj6Y7gV5KBGpBTCrI2NlTN_PE-laRh38YZ3CEveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02aeee65d3.mp4?token=OUCIS8m5LHrD6YZvtSmvh-VAbvIuIyIyWs1V_PdSRdxvLmJceypRzztrQRacqtzDHRl7k_rM11IkIS3SB6bRr9kiQzffowMFk2XHsGcW2XisW19s7D9CoGpfuxpCfF6Y6UBLUsWbZtXb4UMecuHzfg-lIgFE3sP0HsxYvMVhBG43XN5T_MF9fVrTlBhec3JvLeXEQPw1uhXcNtySaFO3-6r3AfknUWHl3j7UEy5161uqdtF8hZ37I8vARle2MMwO8yx8xcfp9vL_9oSh5ODgjC_8mzNOB0m14mjdhhcYCmXBmUqZrGNczxCXA18Y2V0quuGHyycvG6YAPt3Un2MDhFHuEMRKGlB-FWhnp7iEur8kHUX4XPsX0CmlLbtLxnRgWRmR2GXRxafhN2W6ozCQnHeUbDJ7I50UYG7nfSNSZy-EqT9Ny3lfqCq09XSKK6NHRpPCg2XBpeq90O4q89pf-E53KPrdpY8sf8ElG38TIRp2lKIlyVs17eWyDcboaUhLnAA5nY9_fddFPqea2MgxU8-oqQRDiVOGCyRKHdXiIrXYcCAt93j7m2EFNEL-Pqgjck58A0LP_sCHxQLvLcy2nqKcffnvzZ6di6vMX-elp1lz2aGIO-tVhs1ifQfiJX61grWYj6Y7gV5KBGpBTCrI2NlTN_PE-laRh38YZ3CEveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بوی محرم در شب ۱۰۷ شهرکرد پیچید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farsna/442375" target="_blank">📅 22:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442368">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NaTC_HabmPnM8LJIyIF_T5ngfqyagUrPmvdJ6ekpurrYx1LKNJVrfGBcMjauSHIcZXCGrXU8oJfnLaTnUC_ghNVlToDLAWx7ysKoo4rGEInRbEwOAnf-MUi56b_yZz035_J3YENLHZRk7V2_7LsGRpBaz44luWl6iXk8EI9XqKMJ3OIZyNM30t-wQUKKxKyJKNHGopD1E9NvtFOEWv7wcGnz8AyGJ4qKR_EmWGo5kKGjNAjqwVs81N3qdfDFIwsftepqhdvNaatKjzynl01ObnESCioNqWdzPE-eZgCnzA2M_n7IJ-lmjrxnIiUplePuGmC53FvuZ0Yzo1cq3jh4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kpe-_8OJJ2IfCwvOO6eH0fwSCYX_QWYU46eWI-ZyCF4ag-DYhyR1J4YFIKlIhmUow7L581oyHoqFLi20J12fgjH6znnl-Aq1o6Ec2Y3fII26RexXJ_K-o-X3c-RXXpsRd9RGFKP_X8-za5Oe6uDussfM-loCKqyPiNp1ydze1C2xGEVfHqNQxxirj4VJ3GNqBJDq903QkkOsjUaYZ4rGsAbpazeT0zaa0slx2wObJtF6fDvtAz5WENkPumVhqmZw23x3rF55xZjauhbBRxHJsfKrwOggYk4n_8thBMPQ92Oad3OND59IhvPq-LqfIQcBS1JdzSwOrlapS0eYRTAdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/re_C0Qa8uJ-Dy7dcWu5lrtHWfJWYWjK0cFV4YYR3gNsJDwzY3Aw9azz-e61ApqYqFS2cvZfh2-HMoKamX3tawv_RQwsCPG4nTu6MdQQ0uCGlWvXbIFBFDr_5fWnSlDuxiDW_iKd-VsaHCIGN_HvqYSCGqYPPEjQjkz44wyvpcqzFrgJNS0agEiPx0VtChGeO50GemDwu1r25GLlTqrvFXKvQaOgV0Ghz5yDrSU6eM57L7TwqCZaX7epXHjmHHPiKDL26y7KRnO4fdcJ9V1n9niM_58gUhaj0xKmXy1G3R6x_NWdV_N90RvlHym5Tdxko-yiDvylvmSgWPN5plaKWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWPPVgIkutJhKHYp0iQJGOdjAQVeZDxBQnWq7fL0hH_kRuQEEKTHP1fnFouqPsQ3ryBx_zIrRdxzt4IpDnBE2Dk_Qw3yz5rXxoMiucn0ymCVnzsmEkquzRO1y0___2p_c89U5Py_UT_TePfTIlECp_oBsUNVpoHflk5rmsZV4rHaQBMtgC-TkvFXDmyOTh9y3Bw7t1vVAv3U0A5t-VT4k6rtbcCiCKL4sstBTorzieoBnAplnsOTvz8-3zyO7EpbgdUGMiNt_Ecb_it6Q8jcSzS1C4qXz3jHMYbILjG9mPnUnz8cnIKAP8RZNiM5ZW78a6zHzxs1lTFniboMu84qWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byia2wdJVO3De295pYGc7xKXA41dHta3QWoCIKMiL9we-3BrhyXcYbco8J6FFIDPL5hLRs5ODzuIwCizTvc8aICJnpGVO8nkWODZy2ZrZOAjUXKnnPc2ez9NSjSJD5qEEp7lo7zuYrnZZnUfxjSa8PkhSf1cgwZIOupEi0N6xGDoH-556S4hp4IyFU_K9zGSVGJI_i300WMFmxvItjIH5fjt-Dr0eByInOdra-UCsLwkGDZwmqqyi9JZlBcxQpfazxgVmnIUGjMb19hr8Uv7Jt0hZ7Z9VQX0xVbkXHEvyfe_Cw-dh-WGzarlP3eYDWYkiypFfJWXmKpCwBhN6Ui6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpeZfsYieWjyv5nPHd4Y5bB8Ef0xY4qNOlLPQdY_7CV6KN3QeGjkcNKQDB09rcrZ5oA1YfjKnHNlqwxlSMm0BMjCaVbHCZyNLB58-UVr057j2BZp7TY5qO3kk2fvIcLSmw3G3SENaJCoiT6GHveNhBeQdkiqgaWD1qpIqjfOczqNcDyaVQmXq2y-JN4GZC5fQ_UibXgxygFTDcL5dVBXXQkYzzxt4h4NPSoV_7ivQCde5xNV9uv5sn0pIrgXN78k_WfDf613uI1zSSeT7taa87RUGyfoOA16KTgvtuD1lFFS-P8hronfdwDg5qB2xG7QGrlIv4b9_-6X6BhK6PXHFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQZ7YSjYwai5JH-Ua_ddhiFlsrtCw8IX83-PHsck8k7sYNfbSz9m4Wh2Pf045Yv0UxxJ9jGJEIqWoYA-OVTfJmUcMIJC7CFQa48sNAWrE_O3zkHARP7XE249XDDvkFjQxuElES2Ls_U7m5DV-qlBBLd2D_LxnRvj5KIdkz8DgSMylhPEHOi2i6P9Xdf1jDxIWCCc4k5WOTJinwBeOh_ozB2xCh-1q4V5WbZ3L4HG5ZeVRt5htGvAK1es1OcsKMWJyzc_YsZ40KG_4pCbXgrtpmQ_ftvUSBP_svzQVu7wOjX74EMHijGvJZsRzRThiBOXhGyQTFmG3UprnyqY9uKT4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اذن عزای ماه محرم از امام رضا(ع)
عکس:
امیرمهدی آقاجانی
@Farsna</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/farsna/442368" target="_blank">📅 22:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442367">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843c083ba2.mp4?token=iuLf1Zbrvp8iSsLi6J9qNElCmVF9MFjZFzhCrfTtUGaPzYTNsKduEFyzWb4Mz5LCDqICEmdH8mabo0hT2l6rFQ5d1qXHONj2LwaxZwcOj3i2xAeFOlCpHC2h_edFHQ1EyT9Mjqzx8Y1amJXOQYzmIUwYjG3546hCigdUxJ52ujBBmqhLm3ACPomKVmksgA8Z7rF91XpbZZzqAt4QiNv_Pd39vExqU8k5GhnAv-hqdE1ap0sYY8eviwyg5dcymi4wzaqu577RENxkAl8GX95Ok9UHoH2PyLkudHfjtYDrEmkGcHkSWzCRydZ6ty3M9K1LWEM9zv4xc2VSlZ1HZtKT-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843c083ba2.mp4?token=iuLf1Zbrvp8iSsLi6J9qNElCmVF9MFjZFzhCrfTtUGaPzYTNsKduEFyzWb4Mz5LCDqICEmdH8mabo0hT2l6rFQ5d1qXHONj2LwaxZwcOj3i2xAeFOlCpHC2h_edFHQ1EyT9Mjqzx8Y1amJXOQYzmIUwYjG3546hCigdUxJ52ujBBmqhLm3ACPomKVmksgA8Z7rF91XpbZZzqAt4QiNv_Pd39vExqU8k5GhnAv-hqdE1ap0sYY8eviwyg5dcymi4wzaqu577RENxkAl8GX95Ok9UHoH2PyLkudHfjtYDrEmkGcHkSWzCRydZ6ty3M9K1LWEM9zv4xc2VSlZ1HZtKT-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیین سنتی علم‌بندی آستانه‌اشرفیه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/farsna/442367" target="_blank">📅 22:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442366">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49ee9477bc.mp4?token=H2a69lYhbDHQsnFvLqCfXy6VuSh-l6U4z-jNefTdSt0475Db_gHlkf_Vv-IKBpqRnIS62zV1y50mzvKHNGq9_Rms1WPuZyTnb6nl6EOWcotnJXCeoSwonB1W0TPMAwuVLxn7yBEZ8mS9LYjPNED6vp2wkMZisnWJ_zelt6BZXvHTCBkyauE_eCOGC-N1haeCS93BOIMfQToscI4CZy96QBuD-iq40jyFxll5CwvmJjBeQaZuPK-9fbyHlZHjGBG595D_ZQdh9CNzoFt9D3zCeDBSU5jmR62RdpMKbX25kKDu_AhI99SLQXZ0iwBvqVJLTZDpmUbS_NaEP0f7aZyRnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49ee9477bc.mp4?token=H2a69lYhbDHQsnFvLqCfXy6VuSh-l6U4z-jNefTdSt0475Db_gHlkf_Vv-IKBpqRnIS62zV1y50mzvKHNGq9_Rms1WPuZyTnb6nl6EOWcotnJXCeoSwonB1W0TPMAwuVLxn7yBEZ8mS9LYjPNED6vp2wkMZisnWJ_zelt6BZXvHTCBkyauE_eCOGC-N1haeCS93BOIMfQToscI4CZy96QBuD-iq40jyFxll5CwvmJjBeQaZuPK-9fbyHlZHjGBG595D_ZQdh9CNzoFt9D3zCeDBSU5jmR62RdpMKbX25kKDu_AhI99SLQXZ0iwBvqVJLTZDpmUbS_NaEP0f7aZyRnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماتم ما امسال دوچندان است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/farsna/442366" target="_blank">📅 22:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442365">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
ما لشکر ۹۰ میلیونی حیدریم
@Farsna</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/442365" target="_blank">📅 21:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442360">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی</div>
  <div class="tg-doc-extra">حجت‌الاسلام کاشانی</div>
</div>
<a href="https://t.me/farsna/442360" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#حسینیه_فارس
| شب اول محرم
سایر مداحی‌های امشب را
اینجا
گوش کنید.
@Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/442360" target="_blank">📅 21:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442359">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/442359" target="_blank">📅 21:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442358">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcfRUSnBcGwW8Xa-HRVX8fkDiF3HawZzuIo0--42HJlEjFlleJUTqROWlmgLYK7cnhHwtiB3R38X8QQKUXJNgDmmLEmPCq_plInO2dGN14Eqey5NE8p-xhrvef7x5KJ-bnsoutHYvrW4yfn8UXt-_aOkRaYrDCmvcvu5fJeM3yQzcH3cLCicmJawq3hnPXeOZc7sMIFwAkpijveJpL2cz2zVOrUVhuTFc5n2OvLLT5mQrDCG3oYJISQlUkkmXPoP07fACPSSpcG1FOGuTwK05u0KTEOjnh6SgmL1CyXvpUIwMHbFJgooaog6yN-eC_di4p0y2t8SBeZ8nRrHwcsq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین شگفتی جام جهانی
🔹
اسپانیا از پس کیپ‌ورد برنیامد.
⚽️
اسپانیا ۰ - ۰ کیپ‌ورد
@Farsna</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/442358" target="_blank">📅 21:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442357">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e7bf7ca.mp4?token=g6wbEBIT4YnK_YKoy1XTMpkmYslflj_0F2COoU99cIXvasO89h6KMtuF-TAiXyfjGU07wrncPoiaLdgXUGbhaer1KQICxWwuqkHJw2gcJ9gJqVkV_YBDjBeOnTAGP-vJesQgaU6xWHDMlnkdpuE1ZbQsDoo5ggnJ9RvVvPODCoTedHEUe0ryt1ZHjnQuMZElRV8RJEuiMvDzDUVusGUJWutiL00hTcyPunPUs1yk4tiAEuh1FWH-0AxieORQVEs2NXRkJhT5cTup-zebB1x4QiLbjFBFPL5Cduw5_z1ZHyidi385UTP-5a-9nyrBYj-jrZLdhAjTrvR9ca31h3d8_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e7bf7ca.mp4?token=g6wbEBIT4YnK_YKoy1XTMpkmYslflj_0F2COoU99cIXvasO89h6KMtuF-TAiXyfjGU07wrncPoiaLdgXUGbhaer1KQICxWwuqkHJw2gcJ9gJqVkV_YBDjBeOnTAGP-vJesQgaU6xWHDMlnkdpuE1ZbQsDoo5ggnJ9RvVvPODCoTedHEUe0ryt1ZHjnQuMZElRV8RJEuiMvDzDUVusGUJWutiL00hTcyPunPUs1yk4tiAEuh1FWH-0AxieORQVEs2NXRkJhT5cTup-zebB1x4QiLbjFBFPL5Cduw5_z1ZHyidi385UTP-5a-9nyrBYj-jrZLdhAjTrvR9ca31h3d8_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶۸ دلیل علیه فراموشی
@Farsna</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/442357" target="_blank">📅 21:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442356">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d37089622.mp4?token=ARoovH2n71afOoPdt2i5wwYdR8Tg4I3NQoZl7Eiaw9AcsdhMA6xXnENbpQ3YUXAgk7LjN-UDl-WzC9OHdH_2DcwcmLnfYDdMb8x6FwuBaTEi_mbRdPs5dOZ0lNW8eTEf4F0sihkebSD7aleZzg1eAFJOAZqhuO_gt_Oo9HGTgD7XaOe9p4-O7ict-vNnmsLJFf5WA0hOQVq0ldwanLvP07129c2uPMyTMy3-A-Aa8Hl5pbWL8KN1uJBuCmj-XBslBpEkdinVYXhYHbgPbNKk50TTdvKcwqToh1kFjOtIpWCqscRtLoTzR_Li06QeWbXwthHmbuyvYxN1MFw50ZKFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d37089622.mp4?token=ARoovH2n71afOoPdt2i5wwYdR8Tg4I3NQoZl7Eiaw9AcsdhMA6xXnENbpQ3YUXAgk7LjN-UDl-WzC9OHdH_2DcwcmLnfYDdMb8x6FwuBaTEi_mbRdPs5dOZ0lNW8eTEf4F0sihkebSD7aleZzg1eAFJOAZqhuO_gt_Oo9HGTgD7XaOe9p4-O7ict-vNnmsLJFf5WA0hOQVq0ldwanLvP07129c2uPMyTMy3-A-Aa8Hl5pbWL8KN1uJBuCmj-XBslBpEkdinVYXhYHbgPbNKk50TTdvKcwqToh1kFjOtIpWCqscRtLoTzR_Li06QeWbXwthHmbuyvYxN1MFw50ZKFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه هدف قراردادن تجمع سربازان صهیونیست توسط حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/442356" target="_blank">📅 21:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442354">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت باب القبله طهران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WN_WEUC7S2lZKaK0za-8cy6Rjnph1yn-5CSbYfCuDSYQxCBHIXl838u_3EjmNvpGtUIgcgk7SpYC4YRJzsPZ5Q-lCKY4ulZXHU7OBtyw-iiR3spSAGrrigAaluXQwkVFwGXuGsYSscnMieiXGC9qBzw0aIYfQdbADRx39tld6Ay4HsEXu4-jRzuvsI4Hu8MyZn8GWJjkGflmJtIYFYv6TMggCrFPplKQq_rFxK8EjHHjKSTQZc2Cd7Sgl0Vpk4-hqnvx43YLiSbO9AAu-ZvjwtgYaEjKnIT-teSr6oacDJW60xEz0eQ4R_YoUpfPoe0ZGqi11JHvBXlDU0v9j-Scxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TghB90IRTLn17_SZD6lcChi7s7KTSf9EZXdKD9hGUEvtjxbV5SoTpL_iuxP5nwpkCZ3cyL3OcGl4D2eMMm4Gr2rm1uyJ1_3TxjmQYBNwvDcrKlLVFQs2uq1lyRrt1LHM8yVdvjvWPebDGpzDIc8ULVSfVyNA2zZN-WvCJZLcSSLSFFMO4E7ItX2xwKN61qapVmERnxjPiY0zLfFzDICIbAuPF3LL-zHnLBHnCIVpGVoMW9LKFI0nEwZk7NTYBgLDBQvpiE1LZxcgeyOiGi6mL3ODiK_QvxpUTd9NOUH_3JQVKJmBEAzUuQB-OrjlkK5OMIOSNSFIRWDLal_3ITny1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بـسـم‌ربِّ‌الـحـسـیـن
🏴
اقـامه‌عـزای دهه‌ی‌اوّل محرم الحرام ۱۴۴۸هـ.قـ
به‌اِذن‌الله‌وحضرات‌آل‌الله ﷺ ودرضلِّ‌توجهات‌حضرت ‌صاحب‌الزمان‌ارواحنا‌فداه  وبه‌یادقائدعظیم‌الشان‌امام‌خامنه‌ای‌
و شـ ‌هــ‌ دای عزیزمان
🗓️
دوشـنـبـه۲۵‌خرداد‌به‌مدت‌ده‌شب
🕰️
ساعت۲۳
سـخـنـران:
🎙️
استادمعظم‌حاج‌آقاسیدرضـاجـعفـری
مداحان:
🎤
حـاج‌عـلـی‌عـلـیـان
🎤
کـربـلائـی‌سـیـدجـوادپـرئـی
‌
📍
لوکیشن حسینیه باب القبله
‌‌خیابان‌سعدی‌خیابان‌جمهوری‌کوچه‌درختی
🔺
ویـژه‌برادران
‌
#محرم۱۴۰۵
#محفل_اشک
#هیئت_باب_القبله_طهران
‌    ━━━◈❖✿❖◈━━━
اینستاگرام
|
تلگرام
|
واتساپ
|
بـله
|
روبیکا
╭━━⊰•═
🍃
═•⊱━━╮
@babolghebleh_ir
╰━━⊰•═
🍃
═•⊱━━╯</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/442354" target="_blank">📅 21:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442353">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/442353" target="_blank">📅 21:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442352">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7373d222.mp4?token=F0TEB3vH2070iU_uSl0J_RFO-7oaapOdvay8NszO4Yn2IGcvrD1wz2haWc96rw_Jk3IrByWVn3uV2agalRyzCL5OZIiVI2N19Gf_UJ69PKM1csCIfHQWEw2-AeWZjIg7E_PfpJ4Wu5or_2kJnIiL4LpIZTbpEpxWAP19dVNdi7qsOfJx4zxeajxICo9G6PpcOKgmaHWgH8nYhHxyDNgc_Y34Qe6YplOElaiS-CckphIMgG4ycdkjA4U5tXz2IJzmlEZBkBUMz0D3_tGilFeo0cLw-JxrNFvLlyX6EMEnGu6L9COpVk3ETSApgStHGoSY3YSCXhezjzN2hvRAwmk9rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7373d222.mp4?token=F0TEB3vH2070iU_uSl0J_RFO-7oaapOdvay8NszO4Yn2IGcvrD1wz2haWc96rw_Jk3IrByWVn3uV2agalRyzCL5OZIiVI2N19Gf_UJ69PKM1csCIfHQWEw2-AeWZjIg7E_PfpJ4Wu5or_2kJnIiL4LpIZTbpEpxWAP19dVNdi7qsOfJx4zxeajxICo9G6PpcOKgmaHWgH8nYhHxyDNgc_Y34Qe6YplOElaiS-CckphIMgG4ycdkjA4U5tXz2IJzmlEZBkBUMz0D3_tGilFeo0cLw-JxrNFvLlyX6EMEnGu6L9COpVk3ETSApgStHGoSY3YSCXhezjzN2hvRAwmk9rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرنوشت «تنگهٔ هرمز» چه خواهد شد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/442352" target="_blank">📅 21:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442351">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_1ElsQw_ODqEuSo_bPy1Uc1uHwM67c1MKJteGoOrUgLSkRKPJNWsFGsEDCoqKxKiJB13nBHg5D3hqoQrJhYuXnilz0NL9wUhn23lEW4POJp5TvvbvtVtCtTCKobYmlc_ReLd-KNad7gfpIcF3Q7t5GGg_5_UMPoTie5I92MiukkCL1Q1mQXPUl7yG-Q6J8clYswzas9cABDSCTZ7ZyeelLZUzmCv04VUHsIhq3IUHt4HrFsh0GlIOHq8U3xClC8cSD-XqBGDo7PC7xtLTif9wGD71pXU6oJY1hIKoQP8Nawr-eia22VPCHl5P52USeYi43GJTK6xjSIWPBOhYMZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: تمرکز ما با یا بدون توافق خدمت به مردم است
🔹
آن‌چه تفاهم شده، گامی مهم برای توقف جنگ و شروع مذاکره است و هنوز توافق نهایی شکل نگرفته است.
🔹
جمهوری اسلامی ایران خود را برای همه گزینه‌ها آماده کرده و تمرکز دولت با یا بدون توافق خدمت صادقانه به مردم است؛ ملت ایران از امام شهیدش آموخته که زیر بار ذلت نرود.
@Farsna</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/442351" target="_blank">📅 21:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442350">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5rxRGBQpFohTvRaakA3Zy_Z3M2sWIJoxUEUcaa3IqNmxMcAXsz6xkelnKWuIZZeEWQNaL3cX-B6Ku38CMEbXoHITKIDLS0QWL0TDgmtEn9XejN4kNSY6laZU4PBis93hkYIKvW0imyp2cbmPugYQ4HP1DfgKvzzwMj0GnEHxjYFnQQ83xDa3AkCbTp6mDqHhv5Sb1rhlTChAhaPd1b6zGMA6V4hW-Y4Z7jAgCFr5M16B2-ZGWUW4mY7DJwF5d3b0sPtkKAn8VOXDCPYxoxZR19cr6gmZCv3idsREDOp21efH3kY37Zpd1brlcF_dKjknFw-uN-Acb32Ssp1WA34QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: در دورۀ توافق توان دفاعی خود را افزایش می‌دهیم
🔹
ما از هرگونه تفاهم و توافقی که منافع ملت ایران را تأمین کند حمایت خواهیم کرد، اما معتقدیم اجرای تعهدات از سوی دشمن نیازمند اعمال قدرت است.
🔹
اگر دشمن در اجرای مفاد توافق یا تفاهم‌نامه مرتکب نقض عهد شود، با سرعت و قدرت وضعیت نظامی منطقه را به شرایط پیش از توافق بازمی‌گردانیم.
🔹
سطح آمادگی نیروهای مسلح را بیش از گذشته حفظ خواهیم کرد تا دشمن ناچار به اجرای مفاد توافق و پایبندی به تعهدات خود شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/442350" target="_blank">📅 21:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442349">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ac2f8c5d.mp4?token=oC3VqLm7pcY8NJiVHSOglS43aV4Z5L4EX-ZtlhQxDCFAlZNMGvLnRwzvZb4Gnq7Yh2S_Ty5wGlO-ORsA_mtegL9G0M5tP8eo9B-Qlh5Fe8cJY1Bq4Y0FfYxv9Ap63RUrmk7I9uWVZw5U4wogEtvh9tbGxuZ8Go0_356tVaUH8HZkZV_NO0a1HdEO5g2CepVG2TME-ONAH__YIus2WYnYPY5YfwZb9P10JUoTvZMpGIXdxCAETCqzWMJ-2UcnyBgInSPu-qIWMIZ8lNDQ2xwfO2gRs0vsVJ1qMNJr-elTOTrUStN5Nmwk9hzXYCyfUbp9z7Un_NRFXxr9o0FDbJGqXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ac2f8c5d.mp4?token=oC3VqLm7pcY8NJiVHSOglS43aV4Z5L4EX-ZtlhQxDCFAlZNMGvLnRwzvZb4Gnq7Yh2S_Ty5wGlO-ORsA_mtegL9G0M5tP8eo9B-Qlh5Fe8cJY1Bq4Y0FfYxv9Ap63RUrmk7I9uWVZw5U4wogEtvh9tbGxuZ8Go0_356tVaUH8HZkZV_NO0a1HdEO5g2CepVG2TME-ONAH__YIus2WYnYPY5YfwZb9P10JUoTvZMpGIXdxCAETCqzWMJ-2UcnyBgInSPu-qIWMIZ8lNDQ2xwfO2gRs0vsVJ1qMNJr-elTOTrUStN5Nmwk9hzXYCyfUbp9z7Un_NRFXxr9o0FDbJGqXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تا پایان خرداد فرصت دارید از بخشودگی جریمه دیرکرد بیمه شخص ثالث استفاده کنید
@Farsna</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/442349" target="_blank">📅 21:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442348">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/763b20fcc8.mp4?token=DplhGVZqPLIyxh0wgw3f6TK2x0-1A5EESsRSp5fvmiab2uSqArFXQ8h8Xix3B9Adau-rxtrGHc6llIwGDUzE7EWG8UmpJdjecQL3aGa_R2m66A8-n5EIwh0GHxNi226qrafnNrpoGACMaT32wy-CwAM4PDhpuPvhDoWqKGNsPKU4BFptPoyhxq3MVlqOY9b3TfCiWXggDzv_Jq-V_Ia3ipgdmQZnnfHtshqSpLiVMuHUXSIfQm083IBXxCNMLyP0oJcHcvJoR6frrGahENvb3M0PrfpBdnTb2TQAaD1ohxrsx-HIcVKJkuskxLND2OTI2i9XWwjDu0oI0QcFllb_kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/763b20fcc8.mp4?token=DplhGVZqPLIyxh0wgw3f6TK2x0-1A5EESsRSp5fvmiab2uSqArFXQ8h8Xix3B9Adau-rxtrGHc6llIwGDUzE7EWG8UmpJdjecQL3aGa_R2m66A8-n5EIwh0GHxNi226qrafnNrpoGACMaT32wy-CwAM4PDhpuPvhDoWqKGNsPKU4BFptPoyhxq3MVlqOY9b3TfCiWXggDzv_Jq-V_Ia3ipgdmQZnnfHtshqSpLiVMuHUXSIfQm083IBXxCNMLyP0oJcHcvJoR6frrGahENvb3M0PrfpBdnTb2TQAaD1ohxrsx-HIcVKJkuskxLND2OTI2i9XWwjDu0oI0QcFllb_kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: ما برنامه مذاکرات و اجرای تفاهم را براساس بی‌اعتمادی به طرف مقابل تنظیم می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/442348" target="_blank">📅 21:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442347">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1fc1dce5c.mp4?token=hkhk0SC-3qzkmxngOwaCC9t3gPzVZMB8DLjb_3moMk8vHG9M8nXNkD5wU63s8E5zePjRLDhlERzx1fpGpbvoGS6lRI8itAW8Ltry72eo7IosZ3gjrAfKXnA1niNcSqIV0Yg8vmgntMFBIYK0bYkYOpYpmzXBOy_HEvz_0FQ7ulL54EKYPHKv79Sl9vhKP_rjg6l7NQpVzZGd1bgs0M_Z9plyeNJbHxIcqpKfQVgP-pGG_gJDveilZljdEpQi-W9sTl56glhgdziwa6joVqRG0Uk43lvcPcWe4Ffl56zB4otG45o0ofQ8DyndpEbxZQhWeL0RodEm-fP3fLhEu5pllA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1fc1dce5c.mp4?token=hkhk0SC-3qzkmxngOwaCC9t3gPzVZMB8DLjb_3moMk8vHG9M8nXNkD5wU63s8E5zePjRLDhlERzx1fpGpbvoGS6lRI8itAW8Ltry72eo7IosZ3gjrAfKXnA1niNcSqIV0Yg8vmgntMFBIYK0bYkYOpYpmzXBOy_HEvz_0FQ7ulL54EKYPHKv79Sl9vhKP_rjg6l7NQpVzZGd1bgs0M_Z9plyeNJbHxIcqpKfQVgP-pGG_gJDveilZljdEpQi-W9sTl56glhgdziwa6joVqRG0Uk43lvcPcWe4Ffl56zB4otG45o0ofQ8DyndpEbxZQhWeL0RodEm-fP3fLhEu5pllA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم حرم حضرت معصومه(س) به رنگ عزا درآمد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/442347" target="_blank">📅 21:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442346">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حمله پهپادی رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری گزارش دادند پهپاد انتحاری صهیونیست‌ها به شهرک «مجدل زون» در جنوب لبنان اصابت کرده و یک نفر هم زخمی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/442346" target="_blank">📅 20:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442345">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزیر اقتصاد: مبلغ کالابرگ دهک‌های پایین به‌زودی افزایش می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/442345" target="_blank">📅 20:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442344">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69117795d.mp4?token=hTRyPhE50wCk_C-Goz5nGq-N5aWPNEW8x0QZWA2TsUok3WLo169EuxhL7J6lYF5k-ZwTbIWMoVP5D9zJeFiwC3OxPfACBoLNStUNLmbxn1k6E3oZk3sGDKm5kdFNwpBiS59GsrSqI9pVlEbfezLx4auWXWeh8eVWC2CcYj4FbIKwlBNZh6MbjqBa1ttZ9NFSfft9PYI8XQ_i96M6rhgJpNcf3y8vmZlZwM2-xv6J-9Z1Jd7UoS4atXddagW1mvfDpPrj401dcLMCZ6s9KPtUm4VDnzG4KuQMqWmrwedplhmZsst72eiQ-XSd8t0jpCR4njYoQpVZ2l2Llbr07G5_uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69117795d.mp4?token=hTRyPhE50wCk_C-Goz5nGq-N5aWPNEW8x0QZWA2TsUok3WLo169EuxhL7J6lYF5k-ZwTbIWMoVP5D9zJeFiwC3OxPfACBoLNStUNLmbxn1k6E3oZk3sGDKm5kdFNwpBiS59GsrSqI9pVlEbfezLx4auWXWeh8eVWC2CcYj4FbIKwlBNZh6MbjqBa1ttZ9NFSfft9PYI8XQ_i96M6rhgJpNcf3y8vmZlZwM2-xv6J-9Z1Jd7UoS4atXddagW1mvfDpPrj401dcLMCZ6s9KPtUm4VDnzG4KuQMqWmrwedplhmZsst72eiQ-XSd8t0jpCR4njYoQpVZ2l2Llbr07G5_uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار: آیا توافق با ایران شامل رفع تحریم خواهد بود؟
🔹
ترامپ: خیر، شامل رفع تحریم نمی‌شود. این یک چیز وابسته به رفتار است.
🔹
معاون ترامپ هم پیش از این در اظهاراتی که گمان می‌رود بخشی از تاکتیک‌های همیشگی واشنگتن برای بدعهدی باشد گفته بود که هرگونه رفع تحریم…</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/442344" target="_blank">📅 20:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442343">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI-b1JxkZ-zUKnOLesNn7KyceHRBeNg-VmZm7TGzrNSFupuRxsSOtkMvGyBUssT4qwWDD8b698hom9nbeHs1HyOzDxwUMHdBObQVjLHVD8AqNnW19sucpxoSbZYO-ioZ5xIdEltkdDTjLtWTv__gTYRGDgFk-YQox6pkAwr4Y2zO4c2tb_1PrSpHPfkgK5W6qsjcT-XE88pMJS_VNlzDlU6sqpOsmBDLQjNeaylcC_QRm5ARh_A5sJGRVb37DnK8uHkGXrIg5yWCMYWjL6EfKP_0lfYaLq6vXZ8fDgdFpIEEeIVGv5PkhJqmP4g1ae0wIElB1y5k10zMWo3bA6VyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سرآشپز»؛ کپی موفقی که از اصل عقب نماند
🔹
برنامه «سرآشپز» با وجود اقتباس از نمونه خارجی، توانسته با بومی‌سازی مناسب، استفاده از غذاهای ساده و آشنا، طراحی جذاب مسابقه و ریتمی روان، به اثری سرگرم‌کننده و قابل‌قبول برای مخاطب ایرانی تبدیل شود.
🔹
سناریوی برنامه چیز تازه‌ای به نظر نمی‌رسد و آشکارا از نمونه‌ خارجی الهام گرفته است؛( نسخه جهانی «Next Level Chef») اما نکته مثبت اینجاست که سازندگان توانسته‌اند آن را تا حد زیادی با فضای ایرانی تطبیق دهند.
🔹
این «ایرانیزه شدن» را می‌توان در انتخاب غذاها دید. همین موضوع باعث می‌شود مخاطب راحت‌تر با برنامه ارتباط برقرار کند و آن را از فضای تجملی و دست‌نیافتنی برخی برنامه‌های آشپزی دور نگه می‌دارد.
🔗
ادامه را
اینجا
بخوانید.
@Farsnart</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/442343" target="_blank">📅 20:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442342">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2769169015.mp4?token=Y5KlGvhkV_-wH3VYBOt0OqLo7ubzdWBOFtGFMuVTJH_2VSu6h5W3dP8HDT-dxW9pJBT0LZID16_BGfmagcSH4X-8VxsCh20BzEz0-h08JaeE1Ej4FlxkHfrx4ShhaRbQ8U-pmabU9JPGugCQEFgctOiiRyX-d932XB1rP05im4F0rBrDJ6q7Af-3jxwe4rS0ufcm4GinkezpiOyW4FFOY36bfSvkahw5dJrQnkXBAxKhIyTNLOVGxBCJPjO9UuojpdjzeP74Lvuw149V-O8xCLGfBOhz2nUaZXaV1eJpqUI-PB-7cRjyJOIG66iO_pF6fwqlNfYulEZV-Q4HlNpq8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2769169015.mp4?token=Y5KlGvhkV_-wH3VYBOt0OqLo7ubzdWBOFtGFMuVTJH_2VSu6h5W3dP8HDT-dxW9pJBT0LZID16_BGfmagcSH4X-8VxsCh20BzEz0-h08JaeE1Ej4FlxkHfrx4ShhaRbQ8U-pmabU9JPGugCQEFgctOiiRyX-d932XB1rP05im4F0rBrDJ6q7Af-3jxwe4rS0ufcm4GinkezpiOyW4FFOY36bfSvkahw5dJrQnkXBAxKhIyTNLOVGxBCJPjO9UuojpdjzeP74Lvuw149V-O8xCLGfBOhz2nUaZXaV1eJpqUI-PB-7cRjyJOIG66iO_pF6fwqlNfYulEZV-Q4HlNpq8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار: آیا توافق با ایران شامل رفع تحریم خواهد بود؟
🔹
ترامپ: خیر، شامل رفع تحریم نمی‌شود. این یک چیز وابسته به رفتار است.
🔹
معاون ترامپ هم پیش از این در اظهاراتی که گمان می‌رود بخشی از تاکتیک‌های همیشگی واشنگتن برای بدعهدی باشد گفته بود که هرگونه رفع تحریم علیه ایران تنها در صورت پایبندی ایران به تعهداتش صورت خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/442342" target="_blank">📅 20:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442340">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-poll">
<h4>📊 نتیجۀ بازی ایران-نیوزیلند را شما پیش‌بینی کنید</h4>
<ul>
<li>✓ برد ایران</li>
<li>✓ مساوی</li>
<li>✓ برد نیوزیلند</li>
</ul>
</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/442340" target="_blank">📅 20:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442333">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hG_bF05fsAruZsGCl_TZfc-Es-pf4zrNJQ0jfjEJk28bx7KkH3yo0BLsxdAhG9p5egxRJ2zvxa6PXdW8ZCIx-npAFeJOEPl0Z8ykJQMgogHxDyFWlBnx3AGqtX2UW3w0l6k9z6h7cMzq-Dxb0vZ1_s3zifTZ69lc2O1QNEQNvmT2GNxmPf8U9f68rMXwFPogH6bBPwoMmBNEv6aN8TFoN6lmWGET4UTfHCJZv3JKiVtfkZUq3w8olsaERNP2TtRbUVNHDBPmZc6xKesr29k6j4IJYV_KUFDgt53nBX3gScsrsHvTTvD9Pe_mRbXKwFJJVWX9kVKD4cML753VSJRRiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwRCnO_m6EGrKVdMXbOHqyBTr0KNMiEkQ9IPndKDwgI_jM7n-02ZQrPqUQsXPeDpu7fMwsJ3vxaBh2cEtUOpyOm6HSulEQoYbbNVXVchmFWiJw5NWcl9f1wNfD3H_HEVs0s4WXovTokN7SS2UkAQiD_AqY7-KXGRHecw3hiMzLV4-pICRfkKpv3rsI2IvE-YNyI9eCyLS_JVkBA5upU3N7KLuIKzDLRVjR2m4G6voPz1t86H2uuKcMtNMUqzQEJYBJmTm2oL9v6LPpY-ukZWEC5zF6VGgUymSCLe9pX91qXw503f1aJUtzh-dV2p3MxJdoqpZDUiuy4v4b3BPO3Qdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fv8geIdFVDw062wxdGDMSmlf-XLBS5PDsQf_F2ZgFZckwr5AklMpqPubruWvAnfxMH-xVxMGdJd106JeAJ63EMEsX9VS3QfbheaNWcWpUsDjSKZcqVwlnBlcJYMbME9amvUxh37nf9fNgUi16jirXDzAXpbFzhe4jscUHvcMB7MFGFyT9Sq1nPBUJxbISOp926nJ2Iu3GFOnLf-7aiM4cgV4TBsSiNf7EDYs4TRf1qAiAkdl5UtgS6hMHuN-VkSj-CVtqAqFk4weqIupTbvSrO4uKVgfJIYegCBBmF5sxtXvpT11I7mb-vYJG8MAh8phhCxNrBOU99V7rH92LQqgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bppNjiOxRKi2pk6zvDMSr-HD7mB0zS807WtoVwVao-RpuDIkWntMNzjSIFhaj5wC06QYzPA3_vul_rBSicCx5eD4_sIjhSGsGdVYugkgPIGt8LDbng5WGKv23J1nGEFraoSObJpCRFXLbwGv3fGZnntrbUu_4ekd87cjbRkVms8o8JmuAwcrp56ZgCw-8F9tbfrnwbaTvlRzOnhemmXxukPpKJP5vkJQ0WwnKSmfC272IeggMa3Nbm92MQNYe3neQuB3RCYc-8u06zLipRIVIdtAr4GvIIrLFfedjSczp_bKNM7Ro4g-KntKIMPnokPvQhrN44WarW1ztIrIYIlXgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NYqBVyUyzguedUUh8jfNOuZn7cwGSkw7bIB9f7OC0KpjFVoknZoYCp6mawIuf5VQ9QYpgBWJM8HycyJN_rH5gqVb7u3U29Ga4438R3ChtY7yaAMLay-VDpw0x_BPgLAv3g5OwtvdhW3Ie3FgbVuqKgaW_ubE_W2MdgJQDSvLG_ygMqxwuwY-rFeq2iuILzvEtYbHmZwbg0u2IG_4eIci-ewwdUAnLrPoSqZyn6yjgiZ-rxplbaqbkZh8C3fWKJgIrg6r6oPseUJri45hte5OPkV5y3rG35Z8X8BEW178BEUzlWqws3K3c3hAKTkNZ2WdJk13fWhI7v5wDZt-alYbhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7QqO7sqv1AI1LSfNAhDPBtLp0QkTyldemjEDT_U2PgkLApBN6OGh4l1TITGJyecbT3QJ4zKJtQq_UaT3CQ04vUIRSUgZR18451ewVnoUe1EFeGQ3ijZ48fhwtk-lfhbBrT5J29Bg-tC2xO1guMWBRA-MIvb7LA6XXMPtfIX4whq2beqVi1f1VvEgm4KviJH9n20L2bFqVPXBo8-vUcKp0B-JR4RgEgpZ1XdX01GnXv8_CU9WcGK6g_VmwQNXr1OLHqEBhineU0i65FuMjeuT_qyMBpH-NJ6b9d_mOkCKyWUCryCllAXFcqMV5oFyzvPi7V9Pmh39knvuzhwH5k78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J6n_ALNflPVO3TW27CiNGZH4K_UXuMK7HBaE3ikme_R7e0xseb5EYMNyMaGW30k3npSKeCZzfeN7ukmalHNBE06Rv1wvThHIdRpzUb1R1-iWnIb_tWgvJiroJ1E56Z1Cn09Nw24a3a85c3ulb_dU14n-F5StPSeykQ-tchsTIZ_QlyXgHYE2S2IY749yyoA_cyP8ngv4tHtdmGQueZ0u0LcQ4ZERo8Fteazsc-rOzRl_DrQWcvWb21yD3HoM5kUpg0p5JwNU0yuUZsYJLxjeJM6B0SQCuF-Oej-ruhkoK0Uj5dK4hNaRb2Y1eJV0WDGgzuCFYSdY6UEXPliOxW7ugg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سلام بر محرم
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/442333" target="_blank">📅 19:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442332">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30b30da167.mp4?token=rP8II9E7mCFREXtEvGo3rMqrtdx_cFnCXH7vyPzNQp088rSM3iQA3rpmHUBa97iJPyf6KoSJQHKfxluVZc_mBgAexUnze9T9CZ44LrrmjTpf7CrbVIQHTKuu1nRl_1WsBgPZoxwYYpR-qyREmyC9fBDSh_-KXb1kpbCRZ8kLRg6dVpZMWlFc0vR9xaFlh-WH7bmLkK7TwS-B-TlKmXMYA5gX5sxFY76B6nO7-IhLLanQ5UcLOdxU9e-67XEqtqf81OvkmbmRItni7JW_NlV0g3VxQtNlhYwEbhGuTmjerl4VvRg2JCSgBPfpk3GaOK7MxaemzPLL-t7JaYcxYrRIdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30b30da167.mp4?token=rP8II9E7mCFREXtEvGo3rMqrtdx_cFnCXH7vyPzNQp088rSM3iQA3rpmHUBa97iJPyf6KoSJQHKfxluVZc_mBgAexUnze9T9CZ44LrrmjTpf7CrbVIQHTKuu1nRl_1WsBgPZoxwYYpR-qyREmyC9fBDSh_-KXb1kpbCRZ8kLRg6dVpZMWlFc0vR9xaFlh-WH7bmLkK7TwS-B-TlKmXMYA5gX5sxFY76B6nO7-IhLLanQ5UcLOdxU9e-67XEqtqf81OvkmbmRItni7JW_NlV0g3VxQtNlhYwEbhGuTmjerl4VvRg2JCSgBPfpk3GaOK7MxaemzPLL-t7JaYcxYrRIdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از آسمان منادی ماتم رسیده است
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/442332" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442331">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7DDD7qxezOsfjS-t9ytMkFXwj8f8z0Vn-FF848tF8aaVP_2wqVzzKAW0_GjW9l_ayxV3uIfkPCQH-xpuxMsHa3N4fhrqLHvx9Wchp_VvYiHkM-4_DMdlVstC22uamngj3dWyUB33rqfuTKjHTs2rlyu2KcSWbpPkUtgH4pJ6jQwF1ZnfN88tULPuRzmAebWdsin-gAlXKUP4xPc-EPo9NKnqc91cy_W9Y--YUbdLLE9qDeynEhbNynbfn_8xQ6se3urtVyGuocVjZH-2xHcr4mjCsT9oGMlnhrsRL303oj7l8gZaUVqhKrmr9iomwZDnozBqOelUuortcIHwiREdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برق ۲۲۸ ادارهٔ پرمصرف در آذربایجان غربی قطع شد
🔹
شرکت برق آذربایجان‌غربی: برق ۲۲۸ مشترک اداری متخلف در شبانه‌روز گذشته قطع و موجب کاهش ۱.۲ مگاواتی مصرف برق استان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/442331" target="_blank">📅 19:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442330">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDm70728H_HN_ZAo6YWiy4nil_fSVq1ikUypdkjxFPRFW51hColcm5W1DuBUqn-oIGnokjHLJKDNTTItho9g37O9F5zv917swzuYsHfaMxvsHFUd3qXBwptGio6euCC81Rhjy9TB8AkeKuKAh0pGbsJpfq9AAJc4hWDxZkCMwncumJPuLy5WUpQ6A41CbElbm0ZpXuUmYN6sYXMP8TgbsmtZq17l0Llt3CzGDfw6A2tJ2pn1jbUOUyUSB0AmqxUMBokHw9jxx_CJnlh3HBMa1EOGY9oo6qvBobbQvkCCwQqoauMeHLNgghICtFa2fzuwadiYE35DmJrxoTCRwj5oJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از دیدار شهید طهرانچی با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/442330" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442329">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bc485bd8.mp4?token=Tz8F7nKCc4i1dWJr-s36niZve4L77QjJpbZBfFc-NFShgQZWA8R-zJDiFoY6O-58u6TMkLCv21dHzAXfXlx-8EfhQf6ZE7WojIv7UpcatURnfPtW4OXSdZ9m0EdRnub9w6Sxma5DefuPR0-OwEXbsgdbSOy0HHPt_z8eUtMnDqunxC9ZO_z203jCRqYnOPXG-oBD2EXOO-hZB4F7eL6GzEkNBtgDLScL4oN5lrNS1ujmcd8bKMlS9O_IjbzuhMlaxwS1A1nbw_5zj3-VOguVXkQ9dOLkPsvTHeI46CNiI-kR-sjlCU6Ort3Npru4rGpbkp_C2p5IBMFIIdpD6V2Ygw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bc485bd8.mp4?token=Tz8F7nKCc4i1dWJr-s36niZve4L77QjJpbZBfFc-NFShgQZWA8R-zJDiFoY6O-58u6TMkLCv21dHzAXfXlx-8EfhQf6ZE7WojIv7UpcatURnfPtW4OXSdZ9m0EdRnub9w6Sxma5DefuPR0-OwEXbsgdbSOy0HHPt_z8eUtMnDqunxC9ZO_z203jCRqYnOPXG-oBD2EXOO-hZB4F7eL6GzEkNBtgDLScL4oN5lrNS1ujmcd8bKMlS9O_IjbzuhMlaxwS1A1nbw_5zj3-VOguVXkQ9dOLkPsvTHeI46CNiI-kR-sjlCU6Ort3Npru4rGpbkp_C2p5IBMFIIdpD6V2Ygw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسم «خاورمیانه» از کجا آمده است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/442329" target="_blank">📅 19:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442327">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/064ed5ee18.mp4?token=mXPGoNG7gJZpFVayCL7_zIxZ9rit2U49Z1Tgi2zwmSGLnQBq7cueR7r5T3nm5CO9jPMw6sKCxCxZ8Cb8xPG1AKUkBdq7Ef0t-YjEaL4QFnKs9_hZcjawXJigKcEPUOG3zVciSNmwI4Ko7sEkE-mR-0G8mQOBqVnNNRG_VXgVRF1kZtRjs9xUw63dVLvuEHIS6a8AT_s5MXgEp_vdAzQ2Muq15-yKJv805PhGiF4ICH3VD0vwmKKk8FkVMy94Wtd9Iay8KmEjw9uRgQdbrPMY8A681oBF729fcF4dpDmPte5naktBYfpQ1ODczhqXRIR74KGnTwaDwkPfgoGNbV1-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/064ed5ee18.mp4?token=mXPGoNG7gJZpFVayCL7_zIxZ9rit2U49Z1Tgi2zwmSGLnQBq7cueR7r5T3nm5CO9jPMw6sKCxCxZ8Cb8xPG1AKUkBdq7Ef0t-YjEaL4QFnKs9_hZcjawXJigKcEPUOG3zVciSNmwI4Ko7sEkE-mR-0G8mQOBqVnNNRG_VXgVRF1kZtRjs9xUw63dVLvuEHIS6a8AT_s5MXgEp_vdAzQ2Muq15-yKJv805PhGiF4ICH3VD0vwmKKk8FkVMy94Wtd9Iay8KmEjw9uRgQdbrPMY8A681oBF729fcF4dpDmPte5naktBYfpQ1ODczhqXRIR74KGnTwaDwkPfgoGNbV1-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امشب از عرش خدا بوی محرم می‌رسد
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/442327" target="_blank">📅 19:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442326">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595a7e8117.mp4?token=LQVPwsQvuAfV6NABnxqbGFztVRVcW-83BmPKaADzO2snOMnHEzT-_Nvg-JoweafcZWqT1DslTXbugfk-i_cOMwdEV4JujJrZw9ahlimiFlw0wSWOZRhPshJMATZF5YqN6tcOIC2eUR575bEA9JGUPozyW-JZP6HOX68gH_TpTzXdwBsbnHaosbf37U7DZkpuhKG05-gya598v75j4NVjdHOWjZMHLzkbkSbdXbrer162Sq1HjHafQPaZEsgyN4FBlod511COvomivHbCglyzzjXUuVGiHzLIEJUs2C0HHJ9E2VLLoxkpKzThY5FPWPYhgOmW9VmAf0F8VCCZ31g8aYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595a7e8117.mp4?token=LQVPwsQvuAfV6NABnxqbGFztVRVcW-83BmPKaADzO2snOMnHEzT-_Nvg-JoweafcZWqT1DslTXbugfk-i_cOMwdEV4JujJrZw9ahlimiFlw0wSWOZRhPshJMATZF5YqN6tcOIC2eUR575bEA9JGUPozyW-JZP6HOX68gH_TpTzXdwBsbnHaosbf37U7DZkpuhKG05-gya598v75j4NVjdHOWjZMHLzkbkSbdXbrer162Sq1HjHafQPaZEsgyN4FBlod511COvomivHbCglyzzjXUuVGiHzLIEJUs2C0HHJ9E2VLLoxkpKzThY5FPWPYhgOmW9VmAf0F8VCCZ31g8aYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تقابل طارمی با نسخۀ خشن رقص بندری
#جیمی‌جامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/442326" target="_blank">📅 19:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442325">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXZjw9WmhKN-qMRG5UvSREEQ9q1qsAZp_qx5BqvC_55bnJLHrEPd7GGzKXJ0xet5Gy7bWDNt3Ib6una1gA0dzn95c-0pdtlXIgcrWNRA5uQtVSaEAHyAgJvkj9xrJLDaoAG71sj5sBOnGaprGwPOmm6_5ews97QPB9CQlQVQRSq3MnL8mpakeoDqT7rQ4Drsmsg7sVay6Mj65Rd5ofvlwnpwvETVV3s4BUOx0V7fAGsu-m9cw9kP2rcuK_evaw1aGuFf-L8U7y5MN-evdIosVVFNYKgwo1LGh9VDa4qt2a7NqJHxWmBVP0od0Md81x58Yh_WitZ4JeD120pGx4ZWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: با مقاومت تاریخی ملت و رشادت نیروهای مسلح، ایران گامی بلند به سوی پیروزی نهایی برداشت.
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/442325" target="_blank">📅 19:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442318">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzC-YDQ7v3JFsigMBpi7qs9EbOF_QhznKH0siKkUWLyOxhr0Lu-pzLxOyACnAEhr3YQvPmNGZCx3SDQv3ldxASiSdFXA-pK2WUDSfRGhspYCB66vMS3B_wsPBuN2C72ELugDig29dV8jHkLMOWbiOgPOXe2wOw2RciDiNkym9EmCK47WXGLkwDeVNA0nGqAUeMXEhsUiaE1Di_a7fmHWp5b13o8vsZRvCvAo_PfIcmO5e_JqQdBxQ4v2esM9gpk1DkbHVYYti0uS5RxV-0_R5xcMLszibVeD0sl4shyt0fsSwy_iYopO-AZdka5lJi9vAhH9wi-vWD0HM9ibFdk3gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVW0eVEWuf2XjjP6SJi25fP3B99w_MemvqaAziJeAiyJf0pUffHO8VMLUbYOO9FDQ-2IvB8Yuu__Py3Ms9wdPM543UHyeJdZ683bOLf_ThHVi_FMAdvxJfwg33E97rse4AWJpClGA_gGTJDKTQcAa_CEeJKznYTlKBvzxmzLBi7Di55NTwPC-YbAnf-mcqUKQfihjF_oq7YWR-xKokcSIp6PpYlQs4gpG6HNwv088KjejOdYekHFQ8f1Wmc3OLVZB_-kUi2710bGgqJG2Rgc_5mcoRA-JgZxBLthzXo7Vf6yRx3NKc4c9T8XeHtz7M4DdQ9XfvqS000TsLqXGN9Ebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfwxM0_ZfFp5-S22x-a03ORqQmslUxSQS_5xi57BqhHH9LIlCgwS3MV-SbTepXrds9qv9fLkIP9dT6zXvBZhdY6uKrX9BGlQsKEI_U1cG4_OfTRjQpiHxWNuwSqBiCi6VsViECu61IuKgjyJEJyWdJjsOjFvQcLca9sQK8rWx6Z054rc2SIc6tWQKGolluFzZ0vjpIKEJoPbqQhdXSy85Vq-Z1k1AtCj1vEBuZdZq_IcAMLHPissYD393WkfXWmPeHza9pRQhWxxGKxjTVRL3j02mtpbzzdCxajCC4WJNdCrAlS4t8ICG8WpvPbAqOGWfSTKG356pangrlV-czzPWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGSkVrz6YEMZZ7e_9n38PfsYEM0f__jGSnwWDj14q4lN8alHRnBKIfct4mv6xXon0rIY-ypVcr7mWkQt-rDRhfQ1v3g0v63Sv0sJmBGxep09BvQgmMkXe4RUWyPo5fUFf-fEgZ522ocG8GnvsdVVwMrMb2bng-CBQtXBHPBcDDHJNtNtFUCeckiC-mnM32Lziq6uRMwPALzRHLv7PwXWvvmLPueZSqXvQ3nUxW2V2ecZqa_4pUOwoyj_0ZMyWE1Rnkpbuyy5y8eleZ9UKnGk6w06WjcZTQ5ewt0OOWINuiQfERs9fccw3bvR-r7PMySMnJTKA8b0RT3HPAgbdaa5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUCLZ8RBm_NQV5c7n0yMfB4hPRgcsDYBR13LhmW4UTRo9ONHBtogpKLWvxKgrK-DzNr8dJmMyhvtuGf_g8B5cRnkZHdYUJ_TmyDUVqpF79hmjl3BAcB5n4nZSndFu8SCp-eMhcxBdTY_De6TjZEapYTe8YNCwFOtXJuBPmnBKVsEC4wsURGGrDN1j5bvwa5--ptDjEf3dE0BMHwtx4PnaOqa7EVp277GZZ-PKZDjXTOqr20oMzH0WJZczx3i89vqeBMyN_yLnFbD-X3xxiWQuoKzfU2ZyMFXeGQwAIjz4Onl9AtfACIRVESwTeUhQytPmKCYp3MsCJ351y3VeAjSmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zjm4YT7ODKR99VkrVBZoauf1cblYlQq447fEb5024GNsNmfis1gkKm0uaG0J0xfNrZLRLxoHIpQYc--sstfcqes0YqNGWlKEnoqs2Hs-D36PQzjALlZuotOe_AWb6PamdXlh206frkrRe16iBYiErDry2bhypUb1WuvtrHUfDcG79WgfUHRdYfE4iFPqgdFtbfog8l7_w3i7YjsSLOXPLrgm6jKS6FATgu5aOjxRpc739qfJ2XHBZai8gxp6fjcW0TBvziRduBvFCcdo7zmGekFBwLmeFmoRF1dIOMCkoKIkGzpwK5KSGCVeoHioGZMC8JCaEpOsSIvOPUtKXnA8Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxK-Hivg9xv5oVBw-yOlTNe_mwO3xIMcjpu_1nHCVDPl1mvuuHYGcUyp3YaGrwlDvfwvuR_Y8vIC5XtF40tjgxbCXAVOlyjHv9oOds-fwbQY10t87TaYmE0mo7qizryQNwKQ7vG1ROtiJ1ZpxN4jBiCcXX6pyBMvqPL044c9zm99qKkTXKIebiFVNVnWvwl0-Ju_JWSwFHKHau5vOoRpgQnkFOaV7lJz99OD5z8uJGnVC25f6goDGMlyy0zENcGotPu2BxI-K0KYJ9JLaECrIp52SR-uPRGmAPSDlqohIrY13yBmNtr1RFvgoi1vKl1BiSlyICRmh5xl-r8cCHfilg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سفره‌داری ۱۰۰ روزهٔ مردم یزد از مدافعان امنیت
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/442318" target="_blank">📅 19:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442317">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3a877e1a.mp4?token=UyTInMFl1PtBjgGolNsZK2TrTm0tHFQ2MXbrzWU2zJlVsTFpVygdQEAxFtcXSr0uFVf36TsKJjhfoIg-bMu1tWHTsQIzWUjOBoJ5542t0G_5LhLEmM6n6sr99Wtk-mz2Jv_2RHoxDrGWA16Al2qYoTkf9pnIv8YKj1eb2KHZwivpzUr8vdABA0TUVEkr_KjyQCQvUW2E8osObacQiDSOWbZo0wKQuHsGkZANguGbbAyZy2VjKcQhMSFhGBoUPtA0Fa0Vj5mjTQQbdUsixB14t6ZZ0xbVjBDam09DSfaJfOQmfWJNtmXXKevJWuffrTbmYtDt3nimzOdRwhEr_n9c1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3a877e1a.mp4?token=UyTInMFl1PtBjgGolNsZK2TrTm0tHFQ2MXbrzWU2zJlVsTFpVygdQEAxFtcXSr0uFVf36TsKJjhfoIg-bMu1tWHTsQIzWUjOBoJ5542t0G_5LhLEmM6n6sr99Wtk-mz2Jv_2RHoxDrGWA16Al2qYoTkf9pnIv8YKj1eb2KHZwivpzUr8vdABA0TUVEkr_KjyQCQvUW2E8osObacQiDSOWbZo0wKQuHsGkZANguGbbAyZy2VjKcQhMSFhGBoUPtA0Fa0Vj5mjTQQbdUsixB14t6ZZ0xbVjBDam09DSfaJfOQmfWJNtmXXKevJWuffrTbmYtDt3nimzOdRwhEr_n9c1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم گنبد حرم امام رضا(ع) به رنگ عزا درآمد
@Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/442317" target="_blank">📅 19:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442316">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4qi24URBn6-NsFSTWa80WN8hWwI8rlcsuRP91Lbs_uOBqCqOw3QPMoTmcjW1YUR7Phw4Z1LV5_-fuHyZXm_KAbnCrHTB-J85GYV5YpmFLgbj3ceVbhY1LgnuZpjpRCWwzHpC4zUP3E7OEcCIzIN7e5oLRckUuI76GnI2n550137KQZBRO4QXve3oXSMtLyZQGn3S_qdyNVunFxXqgQkR_a9Yf8DxLr3n4JfrYK7YyC3qU0_IgZhT0bm73LK-q5OclbDn4ffklDi089iMvd_kDOV1aXBirXLD7aLKIizEyiEEqHFi8_lBdAkY7qQGHIIKXM0JULiyCpaS4AVBbel-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: اگر همۀ مفاد تفاهم‌نامه به‌درستی عملیاتی شود، به‌عنوان سندی افتخارآمیز برای کشور تلقی می‌شود
🔹
اجرای کامل این تفاهم‌نامه می‌تواند بسیاری از مسائل را برطرف کند و شرایط تازه‌ای را در ایران و منطقه رقم بزند. این تفاهم‌نامه نه‌تنها برای داخل کشور، بلکه…</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/442316" target="_blank">📅 18:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442315">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57edac52d2.mp4?token=Lyv0pUhticy9aVM6kDYk3aq_LSCPYpuIH6YktVHtfK9WyF-bwMtZrdHuPPHMkv5fCDmjIVsEv_42d5XYlqJAj8pEFQ8Cvz6bfpJMxBaFfCNIcVNPCcnjHdC9ozWl2wYx5TY1ravV3WZfyWASFvxDjfRQ4VVgvfy2dAD280BkiuHKHJzKe17x7VuPFx7sPnHPAFNAx9gW-HJTeEdOU2mrfhlkHougBR5QIxOs4pFYuvr0OheLT7J9vHawuPDlDP7fSVpioBpNVOPadHmCLi-qc2s0EP98xBKYTl5LcTo8xJYweIxfhPD8aIpECoxSrE0pPl4ky2wglk_EKIR-QkTBbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57edac52d2.mp4?token=Lyv0pUhticy9aVM6kDYk3aq_LSCPYpuIH6YktVHtfK9WyF-bwMtZrdHuPPHMkv5fCDmjIVsEv_42d5XYlqJAj8pEFQ8Cvz6bfpJMxBaFfCNIcVNPCcnjHdC9ozWl2wYx5TY1ravV3WZfyWASFvxDjfRQ4VVgvfy2dAD280BkiuHKHJzKe17x7VuPFx7sPnHPAFNAx9gW-HJTeEdOU2mrfhlkHougBR5QIxOs4pFYuvr0OheLT7J9vHawuPDlDP7fSVpioBpNVOPadHmCLi-qc2s0EP98xBKYTl5LcTo8xJYweIxfhPD8aIpECoxSrE0pPl4ky2wglk_EKIR-QkTBbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای اولین گویندگی مرحوم رضوی  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442315" target="_blank">📅 18:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442314">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش‌ها از وقوع یک حادثۀ امنیتی در سواحل یمن
🔹
براساس گزارش‌های اولیه، یک نفتکش در آب‌های ساحلی یمن هدف قرار گرفته اما تاکنون جزئیات بیشتری منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/442314" target="_blank">📅 18:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442313">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خداحافظی با رفت‌وآمد بین سایت‌های دولتی
🔹
وزیر ارتباطات اعلام کرد اجرای طرح «زیست‌بوم‌های دیجیتال دولت» از ماه آینده آغاز می‌شود؛ طرحی که قرار است خدمات پراکندۀ دستگاه‌های اجرایی را در یک بستر واحد تجمیع کند.
🔹
با اجرای مرحلۀ نخست این طرح، هفت زیست‌بوم شامل مالی، مالیاتی، انرژی، سلامت، تجارت فرامرزی، زنجیرۀ تأمین و مهاجرین و اتباع به‌صورت یکپارچه در دسترس قرار می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442313" target="_blank">📅 18:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442312">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8535b8b7f8.mp4?token=EjxpZ2Y95T2k-4lfD-5siJUV11pJi_IBdkx_ea21tYrE8lc9MJGf2yRy6VErqZ-4zXXqyMbq1owp-tp5zTG3PoK3Ay5Wo_eIoDHm7_QmPTQIA6Fwpzit6nE57yYXe0EtJLaM69c36FKEEfFNd6NRMKiOM6wamje5vD-JS3e-fGt8kdvR0t8OMUoXE5ULb04RAbhe499gAVeNYZ-uM6rOcpk4J4JdJoEUBN6Yd4__JzkhnOzwksOV_OYtXNKTVmlCIL0pcWiaU-2hlSmGP3ONolLJLEfY-__J2wL4vXgnNzpiIKr4aLhdm97BglBgreMFYEAESwbpzJaGwy7ffE7S4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8535b8b7f8.mp4?token=EjxpZ2Y95T2k-4lfD-5siJUV11pJi_IBdkx_ea21tYrE8lc9MJGf2yRy6VErqZ-4zXXqyMbq1owp-tp5zTG3PoK3Ay5Wo_eIoDHm7_QmPTQIA6Fwpzit6nE57yYXe0EtJLaM69c36FKEEfFNd6NRMKiOM6wamje5vD-JS3e-fGt8kdvR0t8OMUoXE5ULb04RAbhe499gAVeNYZ-uM6rOcpk4J4JdJoEUBN6Yd4__JzkhnOzwksOV_OYtXNKTVmlCIL0pcWiaU-2hlSmGP3ONolLJLEfY-__J2wL4vXgnNzpiIKr4aLhdm97BglBgreMFYEAESwbpzJaGwy7ffE7S4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امام رضا(ع) با آئین اذن عزا به استقبال محرم رفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442312" target="_blank">📅 18:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442311">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5HdhaFTfG1tSTyBNFJEgR9mtJ6CZ0_P-MKy1yCF0D2dcP7jxBYhNA_JlYhWkSw8ULjHQ7SisypAy_g1MXfSqnln-0innFSeL5z9sQrnv18_17OlyvNtUW97Or-q7QHp6KuiGFMzbyEuBDO24aXuIwjRlO7s3t0MEqPuZrGKc6jA22JPtdq2PgE0l27mCbBbK3tasc9eLo4NIK32m53ri6c9zLYc4Xk8NlUHN2F-1y5vnT0aeLfhIryr4EI2eSA1cQnMk4hd9jqC9SHKQ59167G-LfVSJiRKc8WFAI4h7JaJxROzTzR0ZZ0gW76Oc6KlMS0qSffzdAJHF2oVYbXLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اینفوگرافیک | روایت نقش‌آفرینی بانک صنعت و معدن در توسعه زیرساخت‌های انرژی
⚡️
۴۱ طرح نیروگاهی، ۸ هزار مگاوات ظرفیت و سهم ۱۰ درصدی در تولید برق کشور
🔹
بانک صنعت و معدن با ایفای نقشی مؤثر در تأمین مالی پروژه‌های نیروگاهی کشور، از اجرای ۴۱ طرح در حوزه تولید برق حمایت کرده است؛ طرح‌هایی که با ظرفیت ۸ هزار مگاوات، سهمی ۱۰ درصدی در برق تولیدی کشور داشته و گامی مهم در تقویت امنیت انرژی و توسعه زیرساخت‌های صنعت برق به شمار می‌روند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/442311" target="_blank">📅 18:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442310">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt5IAQ6unVBTTVEcM6tymEaCbwCdhHfmoXxvJ55cLxMkTRKjLdtzDlhgU1-mxcKS6TIDXaS1DYot44ibtY4ShPz104mEB3Umoae8qZmgSx2uH4qIjvN56SXDQQSLkK73-Fepc8QdaJ3FLGbEGw3oOZTJ_9R5vl8pYJfTKSXFeSEPM0PxbcBt-5XnfbWuEW3Ii8OohWD228gVKbCdQMIgusoCBlONPDX_O8ZueN6zirfRWN3UuwhAtihMvABF3Y1AUJsvb0VDQzj9jkVYIoZPKmChleHQRh1wuqv31ic5YiCzelI6v9FMOS57NcWZGJK8nZq4SNDYsyb4aW4igVphXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
در مدارِ آینده؛
🔰
دومین شماره مجله «عصر مس» منتشر شد
🔻
دومین شماره از دوره تازه مجله الکترونیک «عصر مس»، روایت صنعت مس ایران، منتشر شد.
🔹
به گزارش پایگاه خبری مس‌پرس
، این شماره با یادداشت دکتر سیدمصطفی فیض، مدیرعامل شرکت ملی صنایع مس ایران، با عنوانِ «مس؛ روایتی که باید گفته شود» آغاز می‌شود؛ یادداشتی که بر ضرورت روایت‌گری ملی از صنعت مس و نقش آن در توسعه و آینده ایران تأکید دارد.
🔹
در این مجله، با بهره‌گیری از روایت‌گری، رویکرد چندرسانه‌ای و طراحی تعاملی، موضوعاتی همچون تولید، طرح‌های توسعه‌ای، بومی‌سازی، مسئولیت اجتماعی، ورزش و روایت‌های انسانی از زندگی و کار در صنعت مس مورد توجه قرار دارد.
🔸
دومین شماره این مجله به تاریخ خردادماه ۱۴۰۵ را ازطریق لینک زیر دریافت کنید:
👇
https://media.mespress.ir/d/2026/06/14/0/15451.pdf?ts=1781420523000
#عصر_مس
#روایت_مس_ایران
#StoryMag
@mespress_ir</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/442310" target="_blank">📅 18:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442309">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/442309" target="_blank">📅 18:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442308">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۶۶.pdf</div>
  <div class="tg-doc-extra">3.9 MB</div>
</div>
<a href="https://t.me/farsna/442308" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۶۵.pdf</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/442308" target="_blank">📅 18:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442306">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGM5FrAzG_Opho9VhPXEyiOUdgxuYx6UBIdsbavAlkbRAPXOA2ijv5WdUeTFFuuj93oqhco1qTMAt572ZNHBY6Dt8B0H_A1YbPLDA84HXfBbhGuNgw4WEydVtUpAdVkG4Ezt7rwtwL-TKfl0IFFwfGfJz7RLY4eqnC7jc4KjNmZdwrbrVEVHAl7MHfFqt8ALhz6oGWaptD8l628V2Ouw9JtCiUHWAWCs8lyfst8XuzS8yipvaVBHs34JzFokBzW5yB4WVxuQSKzl-x6u6DbgJXOFyCrc7Zs5-oRrDc8sVAgcW5k6LdlfbN64SXoWJ_X7zauCCX8h5QzpDdD4ERFPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام تو به یوزهای ایران در جام جهانی چیست؟
🔹
ساعاتی دیگر تیم ملی ایران نخستین دیدارش در جام جهانی را برگزار می‌کند؛ مسابقه‌ای که برای ایرانیان، فراتر از یک بازی فوتبال است.
🔹
اگر برای ملی‌پوشان پیامی دارید یا می‌خواهید حال‌وهوای خودتان هنگام تماشای بازی‌های ایران را با دیگران به اشتراک بگذارید، متن، عکس یا فیلم خود را با هشتگ
#میناب۱۶۸
در صفحۀ فارس تعاملی منتشر کنید.
🔹
همچنین می‌توانید پیام خود را از طریق پیام‌رسان‌ها به نشانی‌های
@Interactive_Fars
و
@fars_ma
ارسال کنید.
🔹
در پایان نیز به قید قرعه به ۱۲ نفر از شرکت‌کنندگان هدایایی اهدا خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/442306" target="_blank">📅 17:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442305">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3d4695485.mp4?token=FOZLBY08gZBqZ8oHZ7qCgSPFkURlxeNy_Fdn3xsLV2TuyhPZ_qT7pDxAn6ntOsxrLLbxCIneWsP-ptwZB5YtC-UFzEea97fjkIGwu5LB8_rgo8MbqwYDg7JBpaClrN8FqceE6FsRfm6BXFbaEak9Pqgho2KTUkCo0T3jHlmMUCsnNxP0tiwsdiiIgxlNUKbgaLdmTrJ9wWfiyJ78g9DMjhpxA08pkefUGgAGRfECLuvFpYJjNFaZFRwA6UWR8XEPX2GlnhioNkRZJcfa-pgIg6P8UygDpxfC-yI7hcFCVDCP4BjfmNXlEDErlvJEjI6up8q5MAj4rtayajO0HRy4Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3d4695485.mp4?token=FOZLBY08gZBqZ8oHZ7qCgSPFkURlxeNy_Fdn3xsLV2TuyhPZ_qT7pDxAn6ntOsxrLLbxCIneWsP-ptwZB5YtC-UFzEea97fjkIGwu5LB8_rgo8MbqwYDg7JBpaClrN8FqceE6FsRfm6BXFbaEak9Pqgho2KTUkCo0T3jHlmMUCsnNxP0tiwsdiiIgxlNUKbgaLdmTrJ9wWfiyJ78g9DMjhpxA08pkefUGgAGRfECLuvFpYJjNFaZFRwA6UWR8XEPX2GlnhioNkRZJcfa-pgIg6P8UygDpxfC-yI7hcFCVDCP4BjfmNXlEDErlvJEjI6up8q5MAj4rtayajO0HRy4Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم مطهر امام رضا(ع) آمادهٔ‌ عزاداری سالار شهیدان شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/442305" target="_blank">📅 17:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442304">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd29612d12.mp4?token=aUNHqTKnk4roQREnzYd5wqfQgeB9XyEttXwmCYK-544keT6_Pc3aZGgKhIXQX44B3tYOfxobvwbVfbNBaOtmquZJq0-RWR8UVvRuR8uDr0iFN8CoR-sQdv-NFyS5RDDO2k0EVwj4RtxI3mVbGu-GnXHwGNUQpa0rz9wMAbrAhCHAOznZRiDc7ZdTNmM1WFjx-r0Bu6oE-vSm_3iaTct4k1z7KoLs-D9foNmkKjN1kg7O1YeMxj7uH9UU7JXZR4oFqbhh36urL5KE6Va5tUrAerb26zyuO2Fn6fllZxKDR6UVriSi80rgXVtxO1SOfxN-QpNvx4Qk45gwE4D-9yQ4OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd29612d12.mp4?token=aUNHqTKnk4roQREnzYd5wqfQgeB9XyEttXwmCYK-544keT6_Pc3aZGgKhIXQX44B3tYOfxobvwbVfbNBaOtmquZJq0-RWR8UVvRuR8uDr0iFN8CoR-sQdv-NFyS5RDDO2k0EVwj4RtxI3mVbGu-GnXHwGNUQpa0rz9wMAbrAhCHAOznZRiDc7ZdTNmM1WFjx-r0Bu6oE-vSm_3iaTct4k1z7KoLs-D9foNmkKjN1kg7O1YeMxj7uH9UU7JXZR4oFqbhh36urL5KE6Va5tUrAerb26zyuO2Fn6fllZxKDR6UVriSi80rgXVtxO1SOfxN-QpNvx4Qk45gwE4D-9yQ4OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳۰۰ خودروی جدید آتش‌نشانی‌های کشور واگذار شد
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/442304" target="_blank">📅 17:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442303">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پزشکیان: اگر همۀ مفاد تفاهم‌نامه به‌درستی عملیاتی شود، به‌عنوان سندی افتخارآمیز برای کشور تلقی می‌شود
🔹
اجرای کامل این تفاهم‌نامه می‌تواند بسیاری از مسائل را برطرف کند و شرایط تازه‌ای را در ایران و منطقه رقم بزند. این تفاهم‌نامه نه‌تنها برای داخل کشور، بلکه برای کل منطقه و نیروهای مقاومت نیز افتخاری بزرگ به شمار می‌رود. جزئیات آن نیز ان‌شاءالله در زمان مناسب ارائه خواهد شد.
🔹
لازم می‌دانم از اعضای تیم مذاکره‌کننده تشکر کنم؛ از آقای قالیباف که زحمات زیادی کشیدند، از آقای عراقچی و همچنین از اعضای شورای‌عالی امنیت ملی و همۀ کسانی که در این مسیر نقش‌آفرینی کردند.
🔹
در شورای‌عالی امنیت ملی، پس از بحث‌ها و بررسی‌های مختلف، تقریباً بیش از ۹۰ درصد اعضا با این روند همراهی کردند و رأی دادند که این اقدام باید انجام شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/442303" target="_blank">📅 17:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442302">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38f89a4ac.mp4?token=dcwgFkAgY11Nz3H7vZglrubw24HMKN7R5k8KnL786napt7qagvOsi6wDbfgVyqIjAHULUHymA0Gbxg9mKNbYA7NMieK71VJ5OshKAdpIra1CEt2_q_Aht54fMHlTYipf0LehvvJZkxAbxzJHlWRuHtHfA_IprrwdCU6S6pbuHEsHQIDbyCc7mx2koB-kamL5VrOhHp1e5r6iO-vizo6u_L-T02_2CK5qMThbZNJT5vyd_N5kOkjF1JSC6Vq-6khcThifWi5ugC5IvQ7RjvJVV6jTRWBLgQIsn_ICjLPo_f31rOnmjWn2icsToGsl6BGfOgj3MGtepZWqJyLrDJBjDhboXxP4mDi2ID5pBnEnxaIyecvxPx2fw4YP_36JRWv8W8L7xhoP4qK7mEFkbKDbJJqOK--WNCmmBt07S_-k7hgWKji6G5gAyF0uAAkBrpgYs8s4yJ4bg1g8PmXZNdxvWKUXovZftq-rlE8SFnD09L9AH2koKhh0sEPxkZ2r2kMoWK6LyOBOQEDWxA5C_KnqVoUh0IQs2oMnrmj-8ivyzxPNf62mIFrR43AP5xlv_JmiPCjbgnnF8joKc4xFb95wq23KKKzQeYvAC0RG-CAmQMPe34a6ePsLOsl1meLe850lWaeQCHuW3aZHDBVIe3KrGSilfGEJo02OAtJRvtTZeys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38f89a4ac.mp4?token=dcwgFkAgY11Nz3H7vZglrubw24HMKN7R5k8KnL786napt7qagvOsi6wDbfgVyqIjAHULUHymA0Gbxg9mKNbYA7NMieK71VJ5OshKAdpIra1CEt2_q_Aht54fMHlTYipf0LehvvJZkxAbxzJHlWRuHtHfA_IprrwdCU6S6pbuHEsHQIDbyCc7mx2koB-kamL5VrOhHp1e5r6iO-vizo6u_L-T02_2CK5qMThbZNJT5vyd_N5kOkjF1JSC6Vq-6khcThifWi5ugC5IvQ7RjvJVV6jTRWBLgQIsn_ICjLPo_f31rOnmjWn2icsToGsl6BGfOgj3MGtepZWqJyLrDJBjDhboXxP4mDi2ID5pBnEnxaIyecvxPx2fw4YP_36JRWv8W8L7xhoP4qK7mEFkbKDbJJqOK--WNCmmBt07S_-k7hgWKji6G5gAyF0uAAkBrpgYs8s4yJ4bg1g8PmXZNdxvWKUXovZftq-rlE8SFnD09L9AH2koKhh0sEPxkZ2r2kMoWK6LyOBOQEDWxA5C_KnqVoUh0IQs2oMnrmj-8ivyzxPNf62mIFrR43AP5xlv_JmiPCjbgnnF8joKc4xFb95wq23KKKzQeYvAC0RG-CAmQMPe34a6ePsLOsl1meLe850lWaeQCHuW3aZHDBVIe3KrGSilfGEJo02OAtJRvtTZeys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم‌داری سرتیم حفاظت رهبر شهید انقلاب از زبان فرزندش
🔹
فرزند سردار شهید سیدمجید طباطبائیان (از فرماندهان سپاه ولی‌امر): برخلاف برخی تصورها، امکانات ویژه‌ای برای تیم حفاظت از رهبر شهید انقلاب در کار نبود و پدرم حتی با راه‌اندازی صندوق قرض‌الحسنه تلاش می‌کرد گره‌ای از مشکلات همکارانش باز کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/442302" target="_blank">📅 17:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442301">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zt9M5OVX5wgHub44_8xhmMQYYcWEUGesfzEkVULvMMOhg7o3smJlAAPYHOOLsgtxihzmVmGm2nWtFKPYZctvoOlSkCy4GRWfvPGP-_xpKBcVZAqzzXNOp0CvQewGvfuepHVVsHo1G5WxhkFHZKd1HlAPPfq_YmR_Zbp2xpp32qqfOREmmYFiI-_CrcL5iP0LZEDu9DdUsK1cHSo5FAlSxHE4vlBdggb6WgBaZLeDjVROkh2fB-8NB1C34m_qP8BoRuFte6vJ2xgSBALFoUrqA6OUy04_yv7Rln71wXNsryVs7D88QQLb8XOUSpUcWXIzXYygeQvRaEUdbGrBghVUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقلید عادل فردوسی‌پور از ابوطالب حسینی
🔸
«فوتبال ایران با مدیر انقلابی تحقیر شد». شاید فکر کنید این تیتر رسانۀ ضدایرانی اینترنشنال است اما این‌طور نیست. در هفته‌های منتهی به حضور ایران در جام جهانی رسانۀ ۳۶۰ متعلق به عادل فردوسی‌پور از هر فرصتی برای حمله به تیم ملی استفاده کرده.
🔹
بخشی از کارکرد رسانه‌ها همواره نقد برای بهبود شرایط است. به فدراسیون فوتبال ایران و تیم ملی نقدهای بسیاری وارد است. همین حالا می‌توان رونمایی از لباس تیم ملی، کش‌دار شدن ماجرای سهمیۀ آسیایی و ناتمام‌ماندن لیگ برتر را به‌عنوان‌مثال ذکر کرد.
🔹
اما چیزی که در مورد تیم ملی نادیده گرفته شده، فشار خارجی است. تهدید جانی تیم ملی از سوی ترامپ، تلاش برای لغو بازی‌های ایران، ندادن کمپ آریزونا و صدور ناقص ویزای اعضای تیم ملی همگی بخشی از کارشکنی است. سنگ‌اندازی که در دنیای فردوسی‌پور محلی از اعراب ندارد. او ترجیح می‌دهد تا جلوتر از نوک بینی‌اش را نبیند و تصویر بزرگ‌تر را نادیده بگیرد.
🔹
نقد ساختاری به بهبود شرایط کمک می‌کند، اما تمسخر صرفاً جنبه سرگرمی دارد و ارزش‌افزوده‌ای برای پیشرفت فوتبال ایجاد نمی‌کند. مسیری که فردوسی‌پور پس از جدایی از نود آن را شدیدتر دنبال کرده. حالا همه چیز به «وایرال‌شدن» بستگی دارد.
🔹
«قلعه‌نویی حالا طوری ساعت می‌بندد که همه باید ببینند». جمله‌ای بود که «عادل» در واکنش به فتوشات‌های سرمربی تیم ملی با ساعت رولکس بر زبان آورد.
🔹
او قبل‌تر حرف‌های قلعه‌نویی درباره سخت‌تر شدن صعود به جمع ۱۶ تیم برتر جام جهانی را هم پای «خنگ» بودن خودش گذاشته بود. حالا دیگر نقد فنی قرار نیست زمان برنامه را پر کند. همه چیز به اندازۀ آیتم‌های ابوطالب فکاهی شده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/442301" target="_blank">📅 17:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442300">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ad819e65.mp4?token=Xb5O48MuTbu8ZAgpn6nqPVjCLCuAXw51eRS5c7jGBEDQoPEGeFiZWdxcgnALWEAJiHrIrDPbXP4qr5bsgg9yeutr7lQ7U_awiQ8ZLOi9W6cIMnAJ91fs-77I3ucIlnYlqi0WrSxxrP37OHdMDulHH-0JCBUdTnt3iIxzE1OVDW-rlYDkebbRTpQ9pOfoMpDNp-Rf2YB1pHKk6eQbko6YzAfdFq7fjuc2-IlqtkyesNlLOsEDgboBdOc8Ax7nyEhvsRu_xzf8ZIrNZ06-6JDihQ9RGzcfavxpzuIDhWO-5XTytsvhHqOamtdDoQQZKgu0v8rJ88hCVHSHV9RMjjtUXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ad819e65.mp4?token=Xb5O48MuTbu8ZAgpn6nqPVjCLCuAXw51eRS5c7jGBEDQoPEGeFiZWdxcgnALWEAJiHrIrDPbXP4qr5bsgg9yeutr7lQ7U_awiQ8ZLOi9W6cIMnAJ91fs-77I3ucIlnYlqi0WrSxxrP37OHdMDulHH-0JCBUdTnt3iIxzE1OVDW-rlYDkebbRTpQ9pOfoMpDNp-Rf2YB1pHKk6eQbko6YzAfdFq7fjuc2-IlqtkyesNlLOsEDgboBdOc8Ax7nyEhvsRu_xzf8ZIrNZ06-6JDihQ9RGzcfavxpzuIDhWO-5XTytsvhHqOamtdDoQQZKgu0v8rJ88hCVHSHV9RMjjtUXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماکرون: ناو فرانسه می‌تواند ظرف ۲ تا ۳ روز آینده در تنگهٔ هرمز مستقر شود؛ البته با هماهنگی
🔹
ما می‌توانیم از همین فردا یک ناو محافظ و ظرف ۲ تا ۳ روز آینده، ناو شارل دوگل، تجهیزات مین‌روبی و ناوهای محافظ شرکایمان و سایر تجهیزات را در منطقه داشته باشیم.
🔹
اما…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/442300" target="_blank">📅 17:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442299">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9cfcb123f.mp4?token=GGaxiOoti5qewyFQyn1ux6rXw1Oo-WQ0Q87y0us9K8vm4dpcLEQJTCm0YJmP3rj2IUXDA9DdlrVJMxh95nyjHsdGjr8bZ4jZcSmDCApmagmnSGlMuNggmfcLabXqsJGJ8OFHA4pNBXBXQEbuOPpCJ0v3eXSQdgaP7G9xa1liOOL4tdgU6mJxLcf3KMmhdiU9QyM_zesp0QLfCKguJj0t_5UIg4xTatQvZB0aI5TExnkWHd9gtGwcuEqtnG4lA6qNhWMfIhVGgeRO5Qh6QWlFMKMUr2Zs84Fg4VO_cDU_7_4dTdZxd68NoY-aSgU2E632f0l6fI8JUCJg3ObLW-KYAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9cfcb123f.mp4?token=GGaxiOoti5qewyFQyn1ux6rXw1Oo-WQ0Q87y0us9K8vm4dpcLEQJTCm0YJmP3rj2IUXDA9DdlrVJMxh95nyjHsdGjr8bZ4jZcSmDCApmagmnSGlMuNggmfcLabXqsJGJ8OFHA4pNBXBXQEbuOPpCJ0v3eXSQdgaP7G9xa1liOOL4tdgU6mJxLcf3KMmhdiU9QyM_zesp0QLfCKguJj0t_5UIg4xTatQvZB0aI5TExnkWHd9gtGwcuEqtnG4lA6qNhWMfIhVGgeRO5Qh6QWlFMKMUr2Zs84Fg4VO_cDU_7_4dTdZxd68NoY-aSgU2E632f0l6fI8JUCJg3ObLW-KYAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماکرون: ناو فرانسه می‌تواند ظرف ۲ تا ۳ روز آینده در تنگهٔ هرمز مستقر شود؛ البته با هماهنگی
🔹
ما می‌توانیم از همین فردا یک ناو محافظ و ظرف ۲ تا ۳ روز آینده، ناو شارل دوگل، تجهیزات مین‌روبی و ناوهای محافظ شرکایمان و سایر تجهیزات را در منطقه داشته باشیم.
🔹
اما تمام این اقدامات تنها در صورتی معنا خواهد داشت که یک توافق بین‌المللی وجود داشته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/442299" target="_blank">📅 17:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442298">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d1ca889d.mp4?token=q0_7d_FiJMnQ0DhFEI4yX60FwZz4sOZ0fA_0K0D67OV5wQdcwq5MjnKCFT0tFRaOMu4FkNTJuYOTSaWKGLxi3Y8EK1vyMQjaP6UundAXRASllnfvboVWfNZCeWqx0jPKkeO9EmBXySYaSwO4dazqLs4lYZsVOipu8tVxamOHskjqIKMIZy-P-49qvz0D4PsGe6Qij6Y0XQhfejjh6YPvkdmJfJ8KQMtuqI-vC65jLDNyZv1qDrh3C4ackIYIBmGuE0CPg-b0rziHKhPaRxiEHQxm7rv-bzHxYJqDiSJz8NFTe7kVvGm6snWPAuzK1zY5UxA5VDP6sIP077qovMyEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d1ca889d.mp4?token=q0_7d_FiJMnQ0DhFEI4yX60FwZz4sOZ0fA_0K0D67OV5wQdcwq5MjnKCFT0tFRaOMu4FkNTJuYOTSaWKGLxi3Y8EK1vyMQjaP6UundAXRASllnfvboVWfNZCeWqx0jPKkeO9EmBXySYaSwO4dazqLs4lYZsVOipu8tVxamOHskjqIKMIZy-P-49qvz0D4PsGe6Qij6Y0XQhfejjh6YPvkdmJfJ8KQMtuqI-vC65jLDNyZv1qDrh3C4ackIYIBmGuE0CPg-b0rziHKhPaRxiEHQxm7rv-bzHxYJqDiSJz8NFTe7kVvGm6snWPAuzK1zY5UxA5VDP6sIP077qovMyEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش بقائی به ادعای معاون رئیس‌جمهور آمریکا در خصوص سرازیر شدن مزایای اقتصادی به ایران: ما را به خیر تو امیدی نیست
🔹
«از آمریکایی‌ها خیلی زیاد رسیده است! من فکر می‌کنم این مزایایی را که می‌گویند، باید از مردم میناب، مردم لامرد و خیلی از نقاط ایران پرسید…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/442298" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442297">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663ecfe4e0.mp4?token=hdrv2bCwgVddjd9RToKtEWPd5-r3UQm1_fRRuzdptaa5pnPwmaHr_9xqInzsFpVEzsVmOTPmSMr-KVN967JpPosSbbTFGqastAFwYTfCBEStx45uU9OJxszSn_GnFEO2uaJcNuQvVq5-40a6ekWEVfMeGPLDe6t10p4NACsVeQkh9a6VuiX6f4UbWl0nVThTv3g-eORTEUIFqEDqxQBYS2whDXPRloZvGIMgqR3dMY3qxb-K7CqoY9ejDPmEuBWXpla2PGy9FT02CKLX28V662CYKrHjO-Axbf5TeUGKnohjVqIuOmj1CZTJkmtYip5IkUQv5dNY24M4FtuvdXe86w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663ecfe4e0.mp4?token=hdrv2bCwgVddjd9RToKtEWPd5-r3UQm1_fRRuzdptaa5pnPwmaHr_9xqInzsFpVEzsVmOTPmSMr-KVN967JpPosSbbTFGqastAFwYTfCBEStx45uU9OJxszSn_GnFEO2uaJcNuQvVq5-40a6ekWEVfMeGPLDe6t10p4NACsVeQkh9a6VuiX6f4UbWl0nVThTv3g-eORTEUIFqEDqxQBYS2whDXPRloZvGIMgqR3dMY3qxb-K7CqoY9ejDPmEuBWXpla2PGy9FT02CKLX28V662CYKrHjO-Axbf5TeUGKnohjVqIuOmj1CZTJkmtYip5IkUQv5dNY24M4FtuvdXe86w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنایۀ بقائی به حواشی امنیتی پیرامون کمپ تیم‌های ملی مختلف در آمریکا
🔹
خوشبختانه کمپ ایران در مکزیک است نه آمریکا؛ از مکزیک بابت میزبانی خوبش تشکر می‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/442297" target="_blank">📅 16:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442296">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZb6ihTZLnPuO7_uvDc1oqkuuBAvTsrwnMYOlcRl53AzweBtWWSR2qSVNt3QSusQmlzAvEau6iWw1fuXkagFcnPDw2qHHdR8GlwjAbg2DWx27OF-Xy5RmTSLelrBcTMh6ht3IH1oV_4bDOw1DMTlAhfGUBc6-2iGL4jqhoFR9qk7E-zDFblbK84KNtDhWE4yS-kNRwOfVL9boggsg0_6hZ6a0OmglfAAijG7fJWVbAwaw34k6DfyXsC2V4j4p-028yBZ8U1KCAvqr4z8NL0axpvf1jidR4-Sr-54bGcYK0H79SpnL-kdrR9xcEcwYFsqOrif0T88SyR680ertXR7yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پوستر صفحهٔ رسمی جام جهانی برای بازی ایران و نیوزیلند
⚽️
این بازی ساعت ۴:۳۰ صبح فردا در ورزشگاه لس‌آنجلس برگزار می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/442296" target="_blank">📅 16:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442295">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e51b0e9f7.mp4?token=WOD_If_ZGPdERI8ZX-SQnOt6beyxVnGrbIiyIZ_LFkGREc2pFtmjGBExJy47Ns7WuTN0D-Z53PCVNYZfbZ6mP8bSEhcHJJdYCvbtYPpMUoosuhSpuvViKzB5wYh7vToDYBBViOj2KOlC7RC4pYMgE0QG_uRAsBC3YaVxQb9Gt_ky036prY2vmsqzUFsl3X7oHMrqJr-1JlSe3DyCnY7j3rVldeOCfZc24kcZjJnYX72K_aEdsQ_rh9RJv5YPoNf9fuU7vEQ3pfyw4_CRC0f3bmmLAf-doapIRyn7960rqUfKVD07PlZRqvNKtJHXutBULxEE8yf0qnRo0-SfxUFwIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e51b0e9f7.mp4?token=WOD_If_ZGPdERI8ZX-SQnOt6beyxVnGrbIiyIZ_LFkGREc2pFtmjGBExJy47Ns7WuTN0D-Z53PCVNYZfbZ6mP8bSEhcHJJdYCvbtYPpMUoosuhSpuvViKzB5wYh7vToDYBBViOj2KOlC7RC4pYMgE0QG_uRAsBC3YaVxQb9Gt_ky036prY2vmsqzUFsl3X7oHMrqJr-1JlSe3DyCnY7j3rVldeOCfZc24kcZjJnYX72K_aEdsQ_rh9RJv5YPoNf9fuU7vEQ3pfyw4_CRC0f3bmmLAf-doapIRyn7960rqUfKVD07PlZRqvNKtJHXutBULxEE8yf0qnRo0-SfxUFwIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مردمان ما به‌عنوان صاحبان کشور حتما مراقب عملکرد مسئولان کشور هستند.
🔹
مردم ما وقتی مجاب و قانع شوند که بهترین تصمیم‌ توسط مسئولین گرفته شده است پشتیبان ما خواهند بود. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442295" target="_blank">📅 16:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442294">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318f9ae212.mp4?token=p1iddgT7-UaZxsIdhcnBjgPgvQAH3qVlL4CyFiKJ8I4DudoGRD0_cSpixs_WpJyQUqV9eTp1wFCY200j3WT7Bi40Off1ble_SaWVTwxv-0w-8ORWSFDnjKOIfojEp4Vo33aRI9J2SeoDEsSRv7VZK28lwvUjYMTcr6AJh04DktM6-WIXWeFdvVJ2nYH20jmMV7mBQlkOK3iAeA2iRiCM_jW7POkzXd1BZKY6zE-Bxs_OajULLl7An5CDnkKrkpq5OhUKaNzxHrl9xACZA2rk_DUuQNoMXUv4jBVAIhxF2l_vK22Kuy5E1Mtho1YoVICkjRCUfBtUVpgHAEY7SEvKSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318f9ae212.mp4?token=p1iddgT7-UaZxsIdhcnBjgPgvQAH3qVlL4CyFiKJ8I4DudoGRD0_cSpixs_WpJyQUqV9eTp1wFCY200j3WT7Bi40Off1ble_SaWVTwxv-0w-8ORWSFDnjKOIfojEp4Vo33aRI9J2SeoDEsSRv7VZK28lwvUjYMTcr6AJh04DktM6-WIXWeFdvVJ2nYH20jmMV7mBQlkOK3iAeA2iRiCM_jW7POkzXd1BZKY6zE-Bxs_OajULLl7An5CDnkKrkpq5OhUKaNzxHrl9xACZA2rk_DUuQNoMXUv4jBVAIhxF2l_vK22Kuy5E1Mtho1YoVICkjRCUfBtUVpgHAEY7SEvKSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما به رژیم صهیونیستی هیچ اعتمادی نداریم کما اینکه به آمریکا هم نداریم
🔹
این امر ثابت شده‌ای است که این ۲ در اجرای تعهداتشان هیچ وقت صداقت نداشتند.
🔹
در عین حال ما ابزارهای خودمان را داریم. آمریکا باید تعهداتش را انجام دهد و باید اطمینان…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/442294" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442292">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8cd6fc55e.mp4?token=fFZJz2_9lgspmvHHLb-fqVy5r3ot1C-dLjr7zbR0gxafZezrfNxMO1sZx0tEcBbDHRxgMSAnqKJW7fBbVIL0O7KWOHZxBHB2lLRoTKrDtQ9JuzmX8b-kQeJ6cKqWSTmxspJue89aZhfImfCOpylUphKSJH54MwjekipJwBIZexTMsJy0rlXVK1SGLyjMXYbCBZr5bzdTRv5-fgNmrTrZm6htM32GaWfqtPpPaCLRaFv_q3UmtXq9WAJDdRRnKVTVCsVotMSQbxuqmlZl6diPbzEit6Cpsj0GMB6ojY7GMT2IrOcUzGLrtkW-ua3Pj_V_0Hru-KhMc7g1gAAMlIFyvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8cd6fc55e.mp4?token=fFZJz2_9lgspmvHHLb-fqVy5r3ot1C-dLjr7zbR0gxafZezrfNxMO1sZx0tEcBbDHRxgMSAnqKJW7fBbVIL0O7KWOHZxBHB2lLRoTKrDtQ9JuzmX8b-kQeJ6cKqWSTmxspJue89aZhfImfCOpylUphKSJH54MwjekipJwBIZexTMsJy0rlXVK1SGLyjMXYbCBZr5bzdTRv5-fgNmrTrZm6htM32GaWfqtPpPaCLRaFv_q3UmtXq9WAJDdRRnKVTVCsVotMSQbxuqmlZl6diPbzEit6Cpsj0GMB6ojY7GMT2IrOcUzGLrtkW-ua3Pj_V_0Hru-KhMc7g1gAAMlIFyvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مذاکرات در مورد موضوع هسته‌ای و رفع تحریم‌ها ظرف ۶۰ روز انجام می‌شود
🔹
در متن یادداشت تفاهم راجع به جزییات موضوع هسته‌ای بحثی را مطرح نکردیم و به‌صورت کلی تفاهم شده که در یک بازۀ زمانی ۶۰ روزه بعد از امضای تفاهم در خصوص موضوع هسته‌ای…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/442292" target="_blank">📅 16:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442291">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حزب‌الله: انعقاد تفاهم میان ایران و واشنگتن را که به برقراری آتش‌بس در همۀ جبهه‌ها از جمله لبنان انجامید، تبریک می‌گوییم
🔹
این موفقیت بزرگ حاصل ایستادگی کم‌نظیر، پایداری استثنایی و فداکاری‌های عظیم ملت ایران و رهبری خردمند آن در مسیر حفظ کرامت، حاکمیت و استقلال ملی خود بوده است.
🔹
حزب‌الله از مواضع ثابت ایران در حمایت از لبنان، مردم و مقاومتش و نیز اصرارشان بر حضور لبنان در هر توافقی که به توقف جنگ و حفظ حقوق این کشور منجر شود، قدردانی و تأکید می‌کند جمهوری اسلامی ایران بار دیگر نشان داد که پشتیبان و متحدی قدرتمند و وفادار است.
🔹
لبنان باید از این پشتوانۀ منطقه‌ای و بین‌المللی به بهترین شکل برای تحقق حاکمیت خود در چارچوب وحدت داخلی بهره ببرد.
🔹
آنچه محقق شده، مقدمه‌ای برای تکمیل آزادسازی کامل سرزمین ماست.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/442291" target="_blank">📅 16:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442290">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfrzMyaQaQ1VbuJGOGsCMFciqK-QDp9JqIIEKhFm98JKBL8UvO_87WjXgg0xrRNZnE6OurCjTnUhar1wtFez3kDKAnK2tnYeiMDzU-FMae1ZP4IMnNB1gXV6AbfanfPavx4mY0yCfO1yUgzxlsTwMETlO48oV_8VjFOOJeBjhZ06JixByC939K8_CSFnISMaoWHMW4Rwv0TZZbwzqU6jU4BAENPpOPOE5JCHrz3ctiTeR4LBKsRfxecZHfuJReApHw5Cl9XLFJLnkrqvS3zE2sWdLNRL8hT75HTQ9b4k6VzvILxSve_lmtGVHwesjzVs6xjrOBnnU3fWC9DvbHYqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پوستر صفحهٔ رسمی جام جهانی برای بازی ایران و نیوزیلند
⚽️
این بازی ساعت ۴:۳۰ صبح فردا در ورزشگاه لس‌آنجلس برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/442290" target="_blank">📅 16:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442289">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffcd01d81.mp4?token=fYN6VbFmFecuiUrWZjXBSmCHh4Tzf8vJvpub8DJ3o4OBNLKUKr3Y3gX6GuRTw5nn7S0ara4uM1kI6CyACkWBxFpYsdUjjpkDpoGzpMFHUR3N3TZyOhRwIldC1TLWSAg84v7oN6c2I4zVtfuWTB1--eNDUkhJFrL076R-qLDZQZCmk47_5IpQkrvJx3XEpodDxmo4dB47lPpKG0Oet-hst9o5Jp8_XfF_Ysh0_E9HNKWLYmr0z5KMBp8BePR-en-N86iOyF2hez2ftswebvuQJeQzcd5JTgSKLtIFpGaMBtseSO3vnDs4bFpqtOfaZFfFbUWxotf3negNZSx2_0knLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffcd01d81.mp4?token=fYN6VbFmFecuiUrWZjXBSmCHh4Tzf8vJvpub8DJ3o4OBNLKUKr3Y3gX6GuRTw5nn7S0ara4uM1kI6CyACkWBxFpYsdUjjpkDpoGzpMFHUR3N3TZyOhRwIldC1TLWSAg84v7oN6c2I4zVtfuWTB1--eNDUkhJFrL076R-qLDZQZCmk47_5IpQkrvJx3XEpodDxmo4dB47lPpKG0Oet-hst9o5Jp8_XfF_Ysh0_E9HNKWLYmr0z5KMBp8BePR-en-N86iOyF2hez2ftswebvuQJeQzcd5JTgSKLtIFpGaMBtseSO3vnDs4bFpqtOfaZFfFbUWxotf3negNZSx2_0knLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مردم منطقهٔ‌ ما نمی‌پذیرند که رژیم صهیونیستی اقدامی بدون هماهنگی آمریکا انجام دهد.
🔹
هر نقض عهدی از سوی متحدان آمریکا صورت بگیرد، مسئولیتش با آمریکاست. @Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/442289" target="_blank">📅 15:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442288">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b78ba35a.mp4?token=n3tzi9Lc001dsDwP354tKKh3z5GW3rX1w_qIo2Q1DAmyZDFonduuejPLMzRHUwfAVoi0hqAjBVj9owz1vSDovL5_syKp1bNg7TjvuSfyumCkT3venI3_9YtFrGFATGez6TU6PIsRo0HRIpdijy9d_w9cQhc5vNkccFHOl3Zw45qElbBInSWqkd9ab8WOsDFm6YaXtkk9GmKeN5aFKJsmp68fOusDcYOHdYEt8BUNYlPsVmoLV0HJPS_lm5XNkBxswNGwEI3Xb-MTFRJjCQFaD4RzchiGCeVrxmO7wlSXzrgmGNY7zum-K2KYZ9oPAb4ZGXBpx6Q_uwVMnr_iOhfSvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b78ba35a.mp4?token=n3tzi9Lc001dsDwP354tKKh3z5GW3rX1w_qIo2Q1DAmyZDFonduuejPLMzRHUwfAVoi0hqAjBVj9owz1vSDovL5_syKp1bNg7TjvuSfyumCkT3venI3_9YtFrGFATGez6TU6PIsRo0HRIpdijy9d_w9cQhc5vNkccFHOl3Zw45qElbBInSWqkd9ab8WOsDFm6YaXtkk9GmKeN5aFKJsmp68fOusDcYOHdYEt8BUNYlPsVmoLV0HJPS_lm5XNkBxswNGwEI3Xb-MTFRJjCQFaD4RzchiGCeVrxmO7wlSXzrgmGNY7zum-K2KYZ9oPAb4ZGXBpx6Q_uwVMnr_iOhfSvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: به ازای خدمات ناوبری و بیمه در تنگۀ هرمز هزینه‌های لازم طراحی و دریافت خواهد شد
🔹
برای مدت زمان مشخص قرار است متناظر با اقدامات طرف مقابل تردد ایمن در تنگه هرمز را مدیریت بکنیم.
🔹
این موضوع به عهده دولت جمهوری اسلامی ایران به عنوان دولت…</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/442288" target="_blank">📅 15:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442287">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9122e82f3.mp4?token=Xso5Vy6knl3zBsPz7lyMoxuI9GBpNLoIBt-yNi_ewtNypNyLrluh29RzEKNRBvN4oTvo1dA-I3hIQOfrFGH2yO0MJgPilHRQm84omLG6i6752kay3ZdkwMl8rZ3Q9RjdVuSPbyzzsFLn4yZMrwqensJGVYxX1SdlyFHB1aiNsutoceems48aUzv43Tsx1WkIrmV7DVscSlNt3ZtXvFqg1DUjr8D5SWB7wf68kOS12c4F0IXbUqs_JDW4hTrJo7Yd1pQGjIjI0TLjokD0OwD2WrUW2ZlAcyl4A8diEDelFIyPBjNg_6TolavWXiaOyRpluyOEALXxCTGIv4wspe3d5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9122e82f3.mp4?token=Xso5Vy6knl3zBsPz7lyMoxuI9GBpNLoIBt-yNi_ewtNypNyLrluh29RzEKNRBvN4oTvo1dA-I3hIQOfrFGH2yO0MJgPilHRQm84omLG6i6752kay3ZdkwMl8rZ3Q9RjdVuSPbyzzsFLn4yZMrwqensJGVYxX1SdlyFHB1aiNsutoceems48aUzv43Tsx1WkIrmV7DVscSlNt3ZtXvFqg1DUjr8D5SWB7wf68kOS12c4F0IXbUqs_JDW4hTrJo7Yd1pQGjIjI0TLjokD0OwD2WrUW2ZlAcyl4A8diEDelFIyPBjNg_6TolavWXiaOyRpluyOEALXxCTGIv4wspe3d5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: طرف آمریکایی متعهد به  آزادسازی اموال مسدود شده ایران و بازسازی خسارات می‌شود.
🔹
طرف آمریکایی موظف به رفع همه‌ی تحریم‌ها می‌شود؛ ایران باید بتواند بدون هیچ مشکلی فروش نفت را انجام بدهد. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442287" target="_blank">📅 15:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442286">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d86a184db.mp4?token=WyIekvCeCDPDv_34P7pATEsRHIVBcyZ5nXcKu-xoQ9cCGXj0P_npyJ0xN9QDIN1P8O7les4ZLPPEszp8DdSu0kYspDh-w_RJGdAfwA68Rxx0bL8iCIPiL_yT7aaq6v_BNK888NsYFMB79yi4WROawGDNcWBhc_4B6JBUjnmEkvllYPv3HPgwPPUl3YQauzdJ2qC_5sTx4fGtJA_Lk-0Xz1OVT9fWidmb51FqcB-F7twiS4kF203poKiY2fwik4v_SVIvOaAvlymBlvZgVNNJQprDMncLqgaiNs_JoJDRIY1afRjZ7npZIv6MHaEOpL14m-jjKxkqbO5N21wmBjYy0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d86a184db.mp4?token=WyIekvCeCDPDv_34P7pATEsRHIVBcyZ5nXcKu-xoQ9cCGXj0P_npyJ0xN9QDIN1P8O7les4ZLPPEszp8DdSu0kYspDh-w_RJGdAfwA68Rxx0bL8iCIPiL_yT7aaq6v_BNK888NsYFMB79yi4WROawGDNcWBhc_4B6JBUjnmEkvllYPv3HPgwPPUl3YQauzdJ2qC_5sTx4fGtJA_Lk-0Xz1OVT9fWidmb51FqcB-F7twiS4kF203poKiY2fwik4v_SVIvOaAvlymBlvZgVNNJQprDMncLqgaiNs_JoJDRIY1afRjZ7npZIv6MHaEOpL14m-jjKxkqbO5N21wmBjYy0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: موضوع خون‌خواهی از همهٔ شهدایمان دائمی است و هیچ‌کس نمی‌تواند به‌هیچ‌‌عنوان از جنایت بزرگی که در حق ملت ایران شد، بگذرد.  @Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/442286" target="_blank">📅 15:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442285">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">منبع آگاه: ایران مانع ورود موضوع موشکی و منطقه به مذاکرات شد
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی در گفت‌وگو با فارس، با تشریح برخی ابعاد یادداشت تفاهم اسلام‌آباد، تأکید کرد: یکی از مهم‌ترین دستاوردهای هیئت ایرانی خارج کردن دو مطالبه راهبردی آمریکا یعنی محدودسازی توان موشکی جمهوری اسلامی و قطع حمایت از جبهه مقاومت از دستورکار مذاکرات بوده است.
🔹
او با اشاره به تلاش چندساله آمریکا برای گسترش دامنه مذاکرات فراتر از موضوع هسته‌ای گفت: طرف آمریکایی در مراحل اولیه خواستار طرح موضوعاتی از جمله برنامه موشکی، توان پهپادی و روابط منطقه‌ای جمهوری اسلامی بود، اما هیئت ایرانی از ابتدا اعلام کرد این مسائل هیچ ارتباطی با موضوع مذاکرات ندارد.
🔹
این منبع آگاه افزود: برخلاف برخی برداشت‌ها، موضوع صرفاً این نیست که ایران درباره توان موشکی خود تعهدی نداده باشد؛ واقعیت این است که پرونده موشکی اساساً از دستورکار مذاکرات خارج شده است. یعنی نه در تفاهم فعلی بندی درباره برنامه موشکی و پهپادی ایران وجود دارد و نه قرار است این موضوع در مراحل بعدی مذاکرات مطرح شود.
🔹
او ادامه داد: در جریان مذاکرات، هیئت ایرانی به صراحت اعلام کرد توان دفاعی جمهوری اسلامی ایران موضوع مذاکره نیست و طرف آمریکایی نیز در نهایت این چارچوب را پذیرفت. بنابراین بحث موشکی نه تعلیق شده، نه به آینده موکول شده و نه قرار است در قالب مذاکرات بعدی دنبال شود؛ بلکه اساساً از دستور کار خارج شده است.
🔹
این منبع آگاه همچنین درباره موضوع مقاومت منطقه‌ای گفت: در این حوزه نیز شرایط مشابهی وجود دارد. آمریکا در مراحل اولیه خواستار طرح موضوع روابط ایران با گروه‌های مقاومت بود، اما این مطالبه نیز در متن نهایی جایی ندارد و از دستور کار مذاکرات کنار گذاشته شده است.»
🔹
او تصریح کرد: بر این اساس، مذاکرات آتی صرفاً بر موضوعات هسته‌ای، رفع تحریم‌ها و مسائل اقتصادی متمرکز خواهد بود و پرونده‌های دفاعی و منطقه‌ای جمهوری اسلامی ایران خارج از حوزه گفت‌وگو باقی خواهند ماند.
🔹
این منبع آگاه در پایان تأکید کرد: حفظ کامل توان موشکی، پهپادی و ظرفیت‌های منطقه‌ای دوستان ایران  یکی از مهم‌ترین خطوط قرمز هیئت ایرانی بود که در روند مذاکرات رعایت شد و در متن نهایی نیز بازتاب یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442285" target="_blank">📅 15:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442284">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3584d1320a.mp4?token=mrgkNJpMAVw3Q_6RpiX2jxuc0kT3tceoW_B8Hv9XDJeoq-CAXTxAdyU3voYSQMAHZykDdaVbOgXfWygzdJollxvWxEghPqTZvZsFw7ieEkT1BEZsBwGy7Vs0WR0smdC2KPKD86pARoP3PyZM4wq-OlSzeogdNhbAuALFdtJi2Ydyr7SpoAkeTVUZL57sRtlHgQ2od0DxldJ0QLnK3PtNreE3MEsFM2MzGevtRO6Lr0McZUm04Vnbwxp_ugYo6cr-iw4PBsRnQtssYrQe2XFtWBQvn21aiWIHKuFap2utwyDcKqbcnHsdr-davJKVYaT6l7fAFamz0OYzacVxlU9Hnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3584d1320a.mp4?token=mrgkNJpMAVw3Q_6RpiX2jxuc0kT3tceoW_B8Hv9XDJeoq-CAXTxAdyU3voYSQMAHZykDdaVbOgXfWygzdJollxvWxEghPqTZvZsFw7ieEkT1BEZsBwGy7Vs0WR0smdC2KPKD86pARoP3PyZM4wq-OlSzeogdNhbAuALFdtJi2Ydyr7SpoAkeTVUZL57sRtlHgQ2od0DxldJ0QLnK3PtNreE3MEsFM2MzGevtRO6Lr0McZUm04Vnbwxp_ugYo6cr-iw4PBsRnQtssYrQe2XFtWBQvn21aiWIHKuFap2utwyDcKqbcnHsdr-davJKVYaT6l7fAFamz0OYzacVxlU9Hnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی: جزئیات ابعاد دیپلماتیک توافق به‌زودی رسانه‌ای خواهد شد
🔹
در خصوص نحوه و سازوکار امضای یادداشت تفاهم، تصمیم‌گیری نهایی ظرف امروز و فردا صورت می‌گیرد و نتایج آن به‌صورت رسمی اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/442284" target="_blank">📅 15:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442283">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb5948c916.mp4?token=jLVnSEsjU_28xV43vtgZ-EZP3VU2B2cn-zrgOqHDQb2cLaxkNFUknjSQ4lUvYxkFWemMEjBUZAvi7fVikr2n-ufmbKekFNOdad-InAn_fqchSZkZILPp7n1T5aAxqa5dlq-9qGVMnfqu7OuFHZI_cd3m7nAAAY7-t86jU7Pn2zdnYC0DvZcbtLe3UnM0lXgktJ5FMXr_Y7WAuU87rQOmdJSJCBcYTay56TKbI-Tb-WOxceo8SaFqN8uS6MUb3V8JqvNLE1LUljygbPXwvpMo1DlO5GxnznGJZhv_dgjn7kiSAQkYLVUFjkR1xY33AXlsAFanqp0_pxTa_xxagh8lyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb5948c916.mp4?token=jLVnSEsjU_28xV43vtgZ-EZP3VU2B2cn-zrgOqHDQb2cLaxkNFUknjSQ4lUvYxkFWemMEjBUZAvi7fVikr2n-ufmbKekFNOdad-InAn_fqchSZkZILPp7n1T5aAxqa5dlq-9qGVMnfqu7OuFHZI_cd3m7nAAAY7-t86jU7Pn2zdnYC0DvZcbtLe3UnM0lXgktJ5FMXr_Y7WAuU87rQOmdJSJCBcYTay56TKbI-Tb-WOxceo8SaFqN8uS6MUb3V8JqvNLE1LUljygbPXwvpMo1DlO5GxnznGJZhv_dgjn7kiSAQkYLVUFjkR1xY33AXlsAFanqp0_pxTa_xxagh8lyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی: در یادداشت تفاهم، ۳ بار اسم لبنان آمده و احترام به تمامیت ارضی و حاکمیت لبنان جزو تفاهم است.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/442283" target="_blank">📅 15:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442282">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c95a58607.mp4?token=UBpx_lT_IdVATUPFVHvd6TiGGdqSWBqP8_YLR18uaftTG1Oz4Y8-H0WBjFFxldjE0mArIoIwF7Fxinui_PL4bdtrkh7DE23qcrLi59ZArfgXk-MgAUAbaAGsyrdmxYDPKZYw-IVoWUtNVSTc33mItKKnflx4Xr_I6pDiryNtLtT-UotdA7GYidaT9wekIGVD-Oa-KTRtoE6wwcevX-ChxOsn7bR-6s7NDMyuFmnAQJUw6lxnnD7-0GIj_Edjytm5OpLgWpVhK_vuqRUgQdQC6mDrSePG_ke0XRkFv6-ieZ0o-qduJaEmhTWkpHFu_GRgRX_NDrgRW9cgKDX-JilUbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c95a58607.mp4?token=UBpx_lT_IdVATUPFVHvd6TiGGdqSWBqP8_YLR18uaftTG1Oz4Y8-H0WBjFFxldjE0mArIoIwF7Fxinui_PL4bdtrkh7DE23qcrLi59ZArfgXk-MgAUAbaAGsyrdmxYDPKZYw-IVoWUtNVSTc33mItKKnflx4Xr_I6pDiryNtLtT-UotdA7GYidaT9wekIGVD-Oa-KTRtoE6wwcevX-ChxOsn7bR-6s7NDMyuFmnAQJUw6lxnnD7-0GIj_Edjytm5OpLgWpVhK_vuqRUgQdQC6mDrSePG_ke0XRkFv6-ieZ0o-qduJaEmhTWkpHFu_GRgRX_NDrgRW9cgKDX-JilUbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: لبنان و خاتمۀ جنگ در لبنان بخش لاینفک تفاهم خاتمۀ جنگ است.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/442282" target="_blank">📅 15:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442281">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31afa1dfe.mp4?token=jLDyyokluubBNEBytiSKhJpC7ZY6KHGOMPFd2NSxeomPMvLCk2VDdOaYBWu5OxJfok-ClnftcEgWO-ZIo1XCBS1FPxyHQZ3x7OqQ5j8QS8gXQxFiNyo9hJ9oelY2vGvoEjwEhy5R2EWWWWEfKyKEL62hVUCatDt6baezczQV4eHNaD3dqhHuHES3qSCTdjR6w4S2W9MUfyuC-yMWuKCkdipKG4OHyXSo7AeNMZucZ3wPTxRToH6lw3bXsWwvqDM4jeyfjjvXoey1Kc8ownVKu03jNUdQMYwhnG9CHjLgdyP1LcFJduL11l5Bou8AxulmuiAFNLCu4inQi4NRjmsoiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31afa1dfe.mp4?token=jLDyyokluubBNEBytiSKhJpC7ZY6KHGOMPFd2NSxeomPMvLCk2VDdOaYBWu5OxJfok-ClnftcEgWO-ZIo1XCBS1FPxyHQZ3x7OqQ5j8QS8gXQxFiNyo9hJ9oelY2vGvoEjwEhy5R2EWWWWEfKyKEL62hVUCatDt6baezczQV4eHNaD3dqhHuHES3qSCTdjR6w4S2W9MUfyuC-yMWuKCkdipKG4OHyXSo7AeNMZucZ3wPTxRToH6lw3bXsWwvqDM4jeyfjjvXoey1Kc8ownVKu03jNUdQMYwhnG9CHjLgdyP1LcFJduL11l5Bou8AxulmuiAFNLCu4inQi4NRjmsoiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: لبنان و خاتمۀ جنگ در لبنان بخش لاینفک تفاهم خاتمۀ جنگ است.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/442281" target="_blank">📅 15:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442280">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S99uV3D06edvyx677shXD6pIPbgt7qFpxYpuRkm_B15XzMiIpeqmmksrc4c1pwHMg7dR3ntP8WtirIXaJCyquzApV7DhTe2DsWp0l-k0thpi6hN8vIO-Q8VDhKyMFKLEeHowZ2wY71HfpMk-QNytD2wKjuKIytONVgZaKZOaPzXUcgZQE4bqR8sd5n0oDq5UTD31TrcYBcuOWciZf6KjZ6uxzsdPnuv1WaNrg8abwuUQUFvQEQRkjLsQ50iD000qhVleU3nLJjvkVvGNuM346-dMmv2HFF-oIzaR8JXYat0FexoLFil4WNCytzw5XvJYgi5z5puPL22U15wNaAY6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده نیروی قدس سپاه: ملت ایران اثبات کرد خون بر شمشیر پیروز است
🔹
مقاومت متکی بر ایمان الهی یک بار دیگر از میدان انقلاب تهران تا میدان آزادی ملت‌های مظلوم به پیروزی رسید.
🔹
آفرین بر ملت امام حسینی ایران و مقاومت منطقه‌ای قهرمان که در آستانهٔ محرم حسینی اثبات کردند هیهات منا الذله یعنی چه و واقعاً خون بر شمشیر پیروز است.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/442280" target="_blank">📅 15:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442279">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d3f2d805.mp4?token=RwikXIAsE3r_GlDL7WeFLxhSrkWom62K9z0cRsTRzisAKX3z0PuRqgM3AMsQ5gi4nugAR9p384rylQC5CveDo9lyX6Aqkl1fZsFxGfwmowB14QPygg3RlbW60nmNx2jIzy80xNstQicVWgeQqa4iVRypnVi09fpsjsw1f5w8ci3E1HJJU1T6n5JFUaxFnb_UWO8PyxfS3SBqyGU3xjn26cKPtNk76XkGRGP2QZXiPJhPq3GOG38uhKlrm_tdlZhkC0ZsvZcn0CV4LDrXXoVf3497JUB14mPHFPeGTKWBFF1kcXJjig4j2k1i8ovNlZvVjDpU4OtzLrRLCvhGdg7UpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d3f2d805.mp4?token=RwikXIAsE3r_GlDL7WeFLxhSrkWom62K9z0cRsTRzisAKX3z0PuRqgM3AMsQ5gi4nugAR9p384rylQC5CveDo9lyX6Aqkl1fZsFxGfwmowB14QPygg3RlbW60nmNx2jIzy80xNstQicVWgeQqa4iVRypnVi09fpsjsw1f5w8ci3E1HJJU1T6n5JFUaxFnb_UWO8PyxfS3SBqyGU3xjn26cKPtNk76XkGRGP2QZXiPJhPq3GOG38uhKlrm_tdlZhkC0ZsvZcn0CV4LDrXXoVf3497JUB14mPHFPeGTKWBFF1kcXJjig4j2k1i8ovNlZvVjDpU4OtzLrRLCvhGdg7UpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ردپای ۲ یوز ناشناس دوباره پیدا شد
🔹
۲ یوزپلنگ آسیایی که اوایل خردادماه برای نخستین‌بار در پناهگاه حیات‌وحش میاندشت جاجرم در خراسان‌شمالی مشاهده شده بودند، پس از ۲۲ روز بار دیگر مقابل دوربین محیط‌بانان قرار گرفتند.
🔹
مسئولان محیط‌زیست احتمال می‌دهند این ۲ یوز به خانوادۀ شناخته‌شدۀ «هلیا» تعلق نداشته باشند و ممکن است این موضوع نشانه‌ای از حضور یک خانوادۀ جدید در منطقه باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/442279" target="_blank">📅 15:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442278">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nhl1ROy_Htk_uhFvfJN_7o7imEaIB7qDAf6E9SXzTQ1lDLR-OD5_2JQI_pZivT1Zt98J7BWXl9RbmdOieeNsGR9llRuD58KWoyBEQjeOGN-Ly051Kvc2C2nCd9pb_W85RYcieAUQa7KrTdw0JIoiuNOefvRtQ4DePLJkBx9F4U-XLG5dA5k6ZVTlIJib-bWkytS4lGEZeakYOpCL3QrmLvXrEn6OyUh-JVM3IDF3IHjoEJAMRC2k98dkOUoUB4WuSVX9NI7AQRuKrCN5LwLLULNRL88vrWpFHDNXoK1vdYTqtuCU_PeSKOInWWMyGlilylYb1u1rM5XUlHG37pV_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یارانۀ ۴۰۰ هزار تومانی دهک‌های ۱ تا ۳ به حساب سرپرستان خانوار واریز شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/442278" target="_blank">📅 14:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442277">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کشف یکی از بزرگ‌ترین پرونده‌های زمین‌خواری کشور در تهران
🔹
با اقدامات قضایی و پیگیری دادستانی تهران، یکی از بزرگ‌ترین و پیچیده‌ترین پرونده‌های زمین‌خواری در غرب پایتخت کشف و در دستور کار رسیدگی قضایی قرار گرفته است.
🔹
در این پرونده با جعل وقف‌نامه، اسناد رسمی و سوءاستفاده از وکالت‌نامه‌ها، منجر به تصرف غیرقانونی اراضی در منطقه فرحزاد شده که از نظر ارزش ریالی یکی از بزرگ‌ترین پرونده‌های زمین‌خواری کشور محسوب می‌شود.
🔹
اطلاعات این پرونده طی ساعات آتی منتشر می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/442277" target="_blank">📅 14:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442276">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_eapde1EO_zJa7byj-4-iPU7yEHY0xFWWH7ovM-Vs3n7YXEgy2L4hNDng0w_yd6OXNcmWOaNQfbFNYQEQpUZm2U6_YP8I5vdpv5QuoRnC3WzHgKZTy2OEnQr_dKbQE5TpQihw-BMP8GuZEx18ogUX6djNKqrC2PDrikP3NIN7Af0yVBMWrOO-wTlvzMosqZNJ25HmeZCb2vdc768ssXyalJeGndA2fGvgd2PGixWiLHOr5paTDExF4QhVjAaQPLZLndkNwFtt9YAe1zdMbplDcg3Ib1gksm9PgnAiIujYq7pGxnRucft0aj9x5eLC-bAocdOW-KfykoZHuhZxl3Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک‌میلیون عراقی خواهان حضور در تشییع رهبر شهید
🔹
عبیری، مستشار سفیر ایران در بغداد: براساس برآوردها نزدیک به یک میلیون نفر از اقشار مختلف عراق خواهان حضور در مراسم تشییع پیکر رهبر شهید انقلاب هستند.
🔹
پیش‌بینی می‌شود حدود ۵۰۰ تا ۶۰۰ هزار نفر از این زائران از طریق مرز مهران وارد ایران شوند و سپس به‌سمت شهرهای تهران، قم و مشهد حرکت کنند.
@Farsan
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/442276" target="_blank">📅 14:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442275">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e02d90ea3.mp4?token=sigRKWTj6ODJfHJ3c4dbAodbhaF93X1cI3wVp0UaOy8DnPgHLIWS4SV3QyUq6UM-on35gFUjo0cJ_t9BB1fsBrTf09wTnSwPFumaE9cddOZo_qkw9NBdGRb5X-UibqS6jjO1MlH0kH57-bP982W2x9GprYVVnu0CPlRxTzkRw4eOASyRwb0h76jpCZFCn0LIrMR64aSwiLsNrX_REq45OKWqcEfxxLN2hUxG4KNtiyjJPwTUEoZ6UYQAkySTgS1PN7XvBHQvGkrfi8X8nxyMeBP2eShZ_p59JGoqtnKAbKcfVdG3BkiVuwXleQ54O_Vqjowl4mMMEoEgmQ6XEbpRUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e02d90ea3.mp4?token=sigRKWTj6ODJfHJ3c4dbAodbhaF93X1cI3wVp0UaOy8DnPgHLIWS4SV3QyUq6UM-on35gFUjo0cJ_t9BB1fsBrTf09wTnSwPFumaE9cddOZo_qkw9NBdGRb5X-UibqS6jjO1MlH0kH57-bP982W2x9GprYVVnu0CPlRxTzkRw4eOASyRwb0h76jpCZFCn0LIrMR64aSwiLsNrX_REq45OKWqcEfxxLN2hUxG4KNtiyjJPwTUEoZ6UYQAkySTgS1PN7XvBHQvGkrfi8X8nxyMeBP2eShZ_p59JGoqtnKAbKcfVdG3BkiVuwXleQ54O_Vqjowl4mMMEoEgmQ6XEbpRUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور صفر در تنگۀ هرمز
🔹
تنگۀ هرمز تا اطلاع ثانوی بسته است و بیش از ۹۶ ساعت است نیروی دریایی سپاه اجازۀ عبور هیچ شناوری را نداده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/442275" target="_blank">📅 14:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442274">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87cd6dfe2c.mp4?token=YUqq0D6NL6e1_eJN-D9omHJEO7fTkgD5OObs1q93hKRCIPhBj8WkHccPzNA-U6LUiUqK3EhiVSgpsj9XzIUmpdfU48fpVOjxmmtZJ9fXbQCmTYYjbrBkGm-GFRyiTngBoi6RLwqIUzCNs2G5Bbc278up-Jpsdg2eHeaxhMYX9tihI6R7obRp1M5v-0_22Ayeew4yC-bhgEO1Tbrpgpv8gS-uLduQYgzxMM0s9CBjcE9dbwgLAzFLTiT0Hc-EELMKWMXLGI3cb3-RJJ7qdZFV2dEY31BcqZsVhVzMVWa_DDmk_M0-cMU9EQrwKdW0dUrEf2M4q0S-YqXq2NxB26QhVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87cd6dfe2c.mp4?token=YUqq0D6NL6e1_eJN-D9omHJEO7fTkgD5OObs1q93hKRCIPhBj8WkHccPzNA-U6LUiUqK3EhiVSgpsj9XzIUmpdfU48fpVOjxmmtZJ9fXbQCmTYYjbrBkGm-GFRyiTngBoi6RLwqIUzCNs2G5Bbc278up-Jpsdg2eHeaxhMYX9tihI6R7obRp1M5v-0_22Ayeew4yC-bhgEO1Tbrpgpv8gS-uLduQYgzxMM0s9CBjcE9dbwgLAzFLTiT0Hc-EELMKWMXLGI3cb3-RJJ7qdZFV2dEY31BcqZsVhVzMVWa_DDmk_M0-cMU9EQrwKdW0dUrEf2M4q0S-YqXq2NxB26QhVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهدی طارمی: وقتی مردم زیر موشک بودند فوتبال دیگر هیچ اهمیتی برایم نداشت. ترجیح می‌دادم در زمان جنگ در ایران می‌بودم.
@Sportfars</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/442274" target="_blank">📅 14:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442273">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba73f97814.mp4?token=W82VR4J1GFU_gVjOJSDW40_jQvyXOegxV7-g-okKH0oJq9dFpFbIRL-0I40fzFGGM_9zizmTQBZxtY7wpqpLD61DLFrKhAIwpz8wvciq6HjdHLpm507_aH5pL9NEoSKs7FTadqkGpAvjGvVieIzzLiyIZZ7uQOCRci2AMB79sJJg1SMqD2x0xXa5uUv0E-jLdZRoB0ZmpBo52qb7T8rUrUarod9d2VTiBuz33ToQkoIBLmlt-N2z4ilx6l8jTTqqR5bM1IppZlAYPa-7PEvBxoF_FNx5cdiQnzJtAEIndWZN4aItUgB9JrPr1A0Q0doESyrLAI-2RW47-glZHL4BfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba73f97814.mp4?token=W82VR4J1GFU_gVjOJSDW40_jQvyXOegxV7-g-okKH0oJq9dFpFbIRL-0I40fzFGGM_9zizmTQBZxtY7wpqpLD61DLFrKhAIwpz8wvciq6HjdHLpm507_aH5pL9NEoSKs7FTadqkGpAvjGvVieIzzLiyIZZ7uQOCRci2AMB79sJJg1SMqD2x0xXa5uUv0E-jLdZRoB0ZmpBo52qb7T8rUrUarod9d2VTiBuz33ToQkoIBLmlt-N2z4ilx6l8jTTqqR5bM1IppZlAYPa-7PEvBxoF_FNx5cdiQnzJtAEIndWZN4aItUgB9JrPr1A0Q0doESyrLAI-2RW47-glZHL4BfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار امنیتی خوش‌چشم، ‌تحلیلگر مسائل استراتژیک
🔹
کشتی‌های عبوری از تنگۀ هرمز درحال نقشه‌برداری و رصد موقعیت آبراهه جهت عملیات‌های نظامی در آینده هستند. این کشتی‌ها باید بررسی دقیق شود. @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/442273" target="_blank">📅 14:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442272">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWLqINu6iu_oVHl0J5lX5SGjA0Ba2oiSovbaePIK6vPfvAzv7sQIIySkfHieAq0gkKMPBoMiRAnbFDlAPak36kKuWTRRUqm5fMmG4npWZp480wgQ1A7JwMASzxjNrbVJmv923HaFOw1diupoKUms4ZOtVStEREDZOut2Bsd29JODrY_l51RHKzrXHrHh2XRCj2lGkhICm3nyM2ulHLAxKnw3cTijLHIVrDc-gjI9rAmFiYvrTTtefqryi74-7Kqs_XwHc5elRu4nmExzY-9ibiFob14tzf0DSEIXJlx6Crn6HAeUedQyPI_uTZpFZCzTnXQ7s2F4u01ad-WlD9uPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: رهبری آیت‌الله سید مجتبی خامنه‌ای در استمرار رهبری امام شهید انقلاب است
🔹
آیت‌الله سید مجتبی خامنه‌ای با وجود همۀ مشکلات و داغدار بودن، مدیریت بسیار مناسبی داشتند و با تدبیر دقیق خود کشور را هدایت کردند. ما نیز باید این راه را ادامه دهیم و تکلیف خود را نهایی کنیم.
🔹
پیروزی ایران در جنگ اخیر حاصل رهبری هوشمندانه، دقیق و مدبرانه آیت‌الله مجتبی خامنه‌ای و ایستادگی ملت ایران در جبهه‌های میدان، خدمت، خیابان و دیپلماسی است.
🔹
امیدواریم یادداشت تفاهم ایران و آمریکا به موافقت‌نامۀ خوبی تبدیل و تحریم‌های ظالمانه و محاصره‌ها که سند زشتی برای غرب است، برطرف شود.
🔹
مردم در ۱۰۶ شب با انسجام و وحدت ملی ایستادند و رفتاری کم‌نظیر حتی در مقایسه با مقاطع مهم تاریخ انقلاب اسلامی از خود نشان دادند.
🔹
جبهۀ خدمت نیز خوش درخشید. انصافاً دولت به‌ویژه شخص رئیس‌جمهور، در خدمت به مردم باوجود همۀ دشواری‌ها، هوشمندانه، شجاعانه و دقیق عمل کردند و دولت در این آزمون ملی خوش درخشید.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/442272" target="_blank">📅 14:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442271">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9INC-g5coZxB1l5cMgnfO67OxGZ3R0gccf6qXYR_ovn2Knjv3rZL1IP9xjvIJUDAk-Gfi-V_l65lqvi_2OAHjLxiHFQKDs7etBd5LGNMXJS8eSu1lpc8gyEdZXP6OZJ8N7OafzBXViu09_UN9aekHBuKr3n8EoI6ZPoQmvwkHDWSL01kwfliL1VBjwrGZT6Of8t9x5BZeTAnX_u6TuU5gOnCQWwsUuhllxbPMYR0Ro-RsnDKb8l0k31D6s_wgdnEKztfKUGTP-K-9Eun43nDDJEFF3DCwpRqddRdqGfKAEo_rgni91qh1eSucaeODc4YX4wyz-hS2zP8TdnoScHwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
انهدام یک هستهٔ تروریستی ۴ نفره، بازداشت یک جاسوس و ۱۲۶ عضو شبکه‌های اغتشاش خیابانی در طول جنگ تحمیلی سوم   @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/442271" target="_blank">📅 14:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442270">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eee2ec1f6.mp4?token=Uz6aHwdU_PmCDErXm__T7_Fe3qf2--3L16ocmuukOGzmEUOvvs04zlWkt-8BFkLXNEyXkgx8GEH_0HFJO-NgAhEIcj0pUfKrkzgS4VxKDMw-iwd4kgfKL95nrk1mgH3oNMpmNz3yISrX-ct3pQveZgh0kHH9QHd8KQlb2qY8AMgqQ4DPtogQpqPEClmUDpqE-2r8N5Ufs0-Nh4SQm_-JXk-fAoGZos6FwRr6hzdL4sYwPAEWBr_ruA7eJk4RilKcWXgnbWdicsF5laNjxFrX8NHqHOork_lOnPr50028zkgjaoqt5rJxbA08T7Sq2wA7qIrc-v_1-iqZJxCemU1eVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eee2ec1f6.mp4?token=Uz6aHwdU_PmCDErXm__T7_Fe3qf2--3L16ocmuukOGzmEUOvvs04zlWkt-8BFkLXNEyXkgx8GEH_0HFJO-NgAhEIcj0pUfKrkzgS4VxKDMw-iwd4kgfKL95nrk1mgH3oNMpmNz3yISrX-ct3pQveZgh0kHH9QHd8KQlb2qY8AMgqQ4DPtogQpqPEClmUDpqE-2r8N5Ufs0-Nh4SQm_-JXk-fAoGZos6FwRr6hzdL4sYwPAEWBr_ruA7eJk4RilKcWXgnbWdicsF5laNjxFrX8NHqHOork_lOnPr50028zkgjaoqt5rJxbA08T7Sq2wA7qIrc-v_1-iqZJxCemU1eVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار امنیتی خوش‌چشم، ‌تحلیلگر مسائل استراتژیک
🔹
کشتی‌های عبوری از تنگۀ هرمز درحال نقشه‌برداری و رصد موقعیت آبراهه جهت عملیات‌های نظامی در آینده هستند. این کشتی‌ها باید بررسی دقیق شود.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/442270" target="_blank">📅 14:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442269">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXKachlSsb_fo8PRakXH5PkTNdaeAftcgEV3b8F9yEAHJYOvSvmwUZSgzxetnbWAHWGsDu62-w-m1P5uCxInYkghcVmur4ZIYeSYEZDbf-k8Y6NrKxy0iDLvyRLE9Qf2cenpYD8uPYzAwozfPwCZVc-xHVR2ZyJmPHjFbFUNF7rIYk9dULhw0tSQxiC2S0y6LdvfvU_mCSPjEEzMsF2WeCnmvawyud73tlmOIxjwTeE4h37fLSy8bhYghuEhDKqRRy6QWFBuRQm6k7-DU4Si7_0rPifEcXrOMEFwFaC8Kiv51ve-x25FzYhLtxmiv84r4ygOTGhPzggOcmXaLWAc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر حاتمی: دشمن فهمید باید به ایران احترام بگذارد
🔹
فرماندۀ کل ارتش: دشمن در جنگ رمضان و جنگ ۱۲ روزه تصور می‌کرد با به شهادت رساندن فرماندهان و رهبر شهید انقلاب می‌تواند کار جمهوری اسلامی را تمام کند، اما محاسباتش اشتباه بود و ملت ایران بار دیگر در صحنه ایستاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/442269" target="_blank">📅 13:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442268">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfKQ1Nsw6vuOZAc1UUjiFhwRlWwLSvAaHv66gudlNJSe4VEEJ3eAB9XcpekrEmA88iXHEO_VaJkaJ8AUCwER0whHvBAIpZfry74Ur7SbajlaqReN9tHv2D8i3hZNvGtJPAdj6mS1YTMBnJP1otxJafZHN9acPg8PVSoZvdzift3d2zHi41saZXJVCCzBKQBl2ehg2n_H3OMQGn68Lq8a6fQsBFKqMkbxTKEMAOn8sb3QuJ4d2bL2Yrl4TLxOLW30b47oU6i_O2XekIogTZ8YS0mdW9myKEfWHaaGqXtv_apmRYzDgf2CDsNyRvfFr_fWamXAvIhSYr-rC-XVRMBPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
حمایت ایران از لبنان
🔹
کاریکاتور جدید کمال شرف، کاریکاتوریست یمنی
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/442268" target="_blank">📅 13:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442267">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پس خون رهبرم چی؟
🔹
بامداد امروز پس از ماه‌ها کشمکش، یادداشت تفاهم ایران و آمریکا نهایی شد. با این حال، در روزهای اخیر موجی از سوالات و شبهات در میان مردم چه در تجمعات خیابانی و چه در فضای رسانه‌ای شکل گرفته است؛ شبهاتی که به گفتۀ برخی ناظران، نبود اطلاع‌رسانی شفاف و به‌موقع بر دامنه آنها افزوده است. در چنین شرایطی، تحلیلگران حاضر در مذاکرات تأکید دارند که دشمنی که با ادعای «تسلیم شدن ایران» پا به مذاکره گذاشت، در تمام اهداف راهبردی خود شکست خورد.
هنوز پیروز نشدیم اما دشمن شکست خورد
🔹
محمدمهدی رضایی تحلیلگر مسائل سیاسی با اشاره به مواضع پیشین آمریکا توضیح داد: «آمریکایی‌ها آشکارا اعلام کرده بودند که ایران باید تسلیم شود، برنامه هسته‌ای و موشکی خود را برچیند و مواد هسته‌ای را بدون قید و شرط خارج کند و از حمایت جبهه مقاومت دست بردارد. هدف پشت این خواسته‌ها چیزی نبود جز براندازی نظام جمهوری اسلامی ادعایی که مقامات آمریکایی بارها به آن اعتراف کرده‌اند.» اما نتیجه نهایی مذاکرات چه بود؟ به گفته این تحلیلگر، آمریکا به هیچ یک از اهداف خود نرسید؛ ایران نه تنها تسلیم نشد، بلکه در جریان این مقاومت، قدرت بازدارندگی خود را تثبیت کرد و رسماً از سوی برخی ناظران بین‌المللی به عنوان «قدرت چهارم دنیا» نام برده شد. رسانه‌ها و چهره‌های بین‌المللی – حتی حامیان آمریکا و اسرائیل – روایت تحقیر ترامپ و ایستادگی ایران را بازتاب دادند.
🔹
وی تأکید کرد: البته این به معنای پیروزی مطلق ما نیست، اما یقیناً معنای آن شکست قطعی دشمن است. دشمنی که می‌خواست با به زانو درآوردن ایران، برای کل دنیا خط و نشان بکشد، خود مغلوب اراده مردم و نیروهای نظامی ایران شد.
هزینه‌ها بهای مقاومت، نه نشانه شکست
🔹
در این گفت‌وگو به خسارت‌های سنگین وارده نیز اشاره شد: شهادت جمعی از مردم، مسئولین و فرماندهان و بالاتر از همه، شهادت رهبرمعظم انقلاب. با این حال، این تحلیلگر تأکید کرد که هزینه‌های سنگین به معنای شکست نیست: «شکست یعنی طرفی که جنگ را آغاز کرد، به اهدافش نرسد. دشمن جنگ را شروع کرد و به هیچ هدفی نرسید، این دقیقاً تعریف شکست دشمن است.» او افزود: «ما عزاداریم و خونخواهی رهبر شهید و مردممان را فراموش نکرده‌ایم و تا قصاص ترامپ و نتانیاهوی جنایتکار آرام نخواهیم نشست. اما نباید تحمل هزینه را با شکست اشتباه بگیریم.»
چرا برخی اصرار دارند روایت شکست ایران را تبلیغ کنند؟
🔹
بخش مهمی از این مصاحبه به بررسی شبهات برخی افراد دلسوز و مومن اختصاص داشت؛ افرادی که به گفته رضایی، اصرار عجیبی بر تبلیغ روایت «شکست ایران» در افکار عمومی داخلی دارد. او با اشاره برخی مصادیق این سوال را مطرح کرد: «آیا با تحقیر ملی سودی عایدمان می‌شود؟» به باور وی، مهمترین دستاورد این جنگ و مذاکره، اراده، اعتمادبه‌نفس و باور به توانایی ملی بوده است. مردمی که در برابر ابرقدرت‌ها ایستادند، امروز با پوست و گوشت و استخوان خود درک می‌کنند که باید قوی شوند و این قدرت بالقوه را به فعلیت برسانند. اما برخی به رغم حسن نیت، می‌کوشند این دستاورد روانی و راهبردی را نادیده بگیرند و شکستی را روایت کنند که در واقعیت رخ نداده است.
هوشیاری از موضع قدرت، نه از سر ضعف
🔹
رضایی معتقد است که متن توافق نیز مبتنی‌بر بی‌اعتمادی به طرف آمریکایی تنظیم شده است. این تحلیلگر مسائل سیاسی با تأکید بر اینکه «ما هرگز به قاتلان رهبر شهیدمان اعتماد نداریم» خاطرنشان کرد: آمریکا همواره پیمان‌شکنی کرده؛ بنابراین برنامه‌ریزی باید به گونه‌ای باشد که چیزی نقد به دشمن داده نشود، منتظر «نسیه» نباشیم و گام به گام از موضع بالا و برابر حرکت کنیم. او این هوشیاری را نه از سر ضعف، که از موضع قدرت توصیف کرد.
🔹
رضایی در پایان تاکید کرد: «ما نمی‌گوییم حتماً پیروز شدیم؛ اما می‌دانیم که دشمن قطعاً شکست خورده و افکار عمومی جهان این را درک کرده است.» اصرار بر روایت شکست ایران، خواسته یا ناخواسته، خوراک تبلیغاتی برای همان دشمنی است که تحقیر شد. دلسوزان واقعی نظام که خودشان به درستی به رویه خودتحقیری برخی غربگراها انتقاد دارند، به جای تحقیر ملی، باید با تقویت نقاط قوت، خونخواهی شهیدان و مطالبه گری صحیح به تکمیل مسیر پیروزی کمک کنند و بدانیم که پیروز نهایی – تا نابودی رژیم صهیونیستی و استکبار جهانی و قصاص ترامپ و نتانیاهو – هنوز محقق نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/442267" target="_blank">📅 13:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442266">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quvEOl4EQ2VtsEMF4plAAxsUTwp9dkuA-oK36MCC37wdvj7Xkx5dZm58rD4-6u63Hx6tZ52KufqZHEiFmfrnEioqa4kv1OkbBd6gKmyLv22AxutX7Ml3bmX1LVbF6Ilm6x-qv7SxgFoDZJqSEFs3KBt441acNrT6oAdkuAWCyxyE9BUCDe2-DFE_nHRTIxGJxDPR4IJH2wmb8pOObZ18ejMcHKzoMb61K10PcdlS2jkUDggK8TQ0aeSd2NHYtJn3p6yetC3P4lyW1rr8rSDZDTlt-VvlXLMVqUts91Q5L5pDVwDSDppeATfOR_Au8sHWFG-VRsN2LwBq29SfJOGeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با رکورد جدیدش از ۴.۸ میلیون هم عبور کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۳ هزار واحدی به ۴ میلیون و ۸۱۹ هزار واحد رسید و مثل روزهای گذشته رکورد تاریخی جدیدی را ثبت کرد. @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/442266" target="_blank">📅 13:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442265">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8AsIMXqxVP-TbB8qE7cRAsw6TUt6v8H7MxPfg6cCywf0tY0TrbY4EIPXy3SBbnt_-TmZ8A0aGdqD_IY6C8TTM5VGSNBFOhsTgewkp3xQVNxsmlDhYHm7s7fG62I-hoPIocLuQLDTRYc_LVq_OgfgbyL6ejnlLKh8D9QJK0wdguzj6XJanwDdQPzuutv8Wd-D1oox9uMozcWPXQHCPBzFp08mS72R2q5kOLTMmUGgbAx4YG_16cka-LRuqIszgjQkEaLy8uSf_vgMYf0InC8HZh5jaBsuxue3TkGs3GSf8jOUbpuSdG1q9LWc0nx5P1XCadDd-1jlB_5QRsUe1MUow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زابل گرم‌ترین شهر جهان شد
🔹
داده‌های هواشناسی جهانی نشان می‌دهد زابل در ۲۴ ساعت منتهی به صبح ۲۵ خرداد با ثبت دمای ۴۷.۶ درجه، گرم‌ترین نقطۀ جهان بوده.
🔹
شهرهای الاحساء عربستان با ۴۷.۴ و سبی پاکستان و ینبع عربستان با ۴۷ درجه در رتبه‌های بعدی قرار گرفتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/442265" target="_blank">📅 12:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442264">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plnJ20pma1mOaxdQytmoqwC5m_LxI8MgilnJY99-uLbZ5MAZRLOQ6sWc6czkh6cGVMCHrt6ZX50CgI8UfCZymMJsP6L-d-ZORvrxAdzWc2NERYOTYSb5IVaQWJQgXQIOfAm5seHy6u627zCM4RFJ7NZS36HGbi-1_Q7FikMbz7zF16wAhPSRA3JmbJhlGyQjXyVb_aaFMTyQMNK_Jk7v6ydv4Ss91B0Zh6UA9iEiYd6evVMLCYoG66J678dbrph99qrWvA70iihvhFFVH2R6nqoF2IL8sjgFkO6zj9iWLX7DFXvVI0CBBFeRD6sbgD8UMzPWKOqFiDp7JDL8fkjXOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقوع حادثه برای یک کشتی در نزدیکی یمن
🔹
سازمان عملیات دریایی انگلیس: گزارش‌هایی درباره حادثه امنیتی برای یک کشتی فله‌بر در آب‌های جنوب یمن دریافت شده است.
🔹
این کشتی در ۲۶ کیلومتری جنوب عدن، گزارش داد که یک قایق تندرو حامل چندین سرنشین به آن نزدیک شده است.
🔹
سرنشینان قایق تندرو به سمت کشتی باری تیراندازی کرده و سعی کردند وارد آن شوند؛ تحقیقات درباره جزئیات این حادثه ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/442264" target="_blank">📅 12:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442263">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
ماجرای تغییرات لحظه‌آخری یادداشت تفاهم ایران و آمریکا چه بود؟
🔹
یک منبع نزدیک به تیم مذاکره‌کننده در گفت‌وگو با خبرنگار فارس جزئیاتی از کم‌وکیف اقدامات ۲۴ ساعت اخیر دربارۀ توافق با آمریکا را تشریح کرد.
🔹
به‌گفتۀ این منبع، پس از آن‌که روز شنبه کلیات یادداشت…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/442263" target="_blank">📅 12:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442260">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fnu5FzLm2iLxgDtGzrk-NwsQeI0tAs1TecixsRMtD7F0CZCqboUNNj-IFCFhIHVp2AaL1-m3oVCRCc5WKNBq-to0HAtB2HAeqiKWTNeDlLfFhh3xAcR7IMJgcxgDn1yxJNjiMePCDhzYid2Mh9aw0vC7RCpzvjAZQG2NvoHtpm-iZta6gN0AkVL4jdk2IToCsdmaFXF1qDLXs6BbzYxAHqGKP4fT3p7jXxSvMx4OiQ6C7mVkIFZVgoaF7CoenldKmLLcZYSEMNm4HGMkQgHkgAiQBlSKsKuXN1CMtcEwelghPO6I2hNTJ8KAha2hB14cvCYsvB63R27xM3uUOSiHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6eWd_TdgqmfPlz00o5nd-lttubRDXkYPqKuuLhJ4VYqKdsW86pLVgpDC7sJ5xDpTgAf2Y1JunqTmxJa74IQmmwsw0soN2W25tRIHYnlsa6dy0KWf2wivEI-FZDAAVu7wRJ43--fHBtTJ023TI-6XtWcGK81f4PkYa2qkaRyDfL6ug0A-026E-0P5rp9Nrl52fxH1Jhbv8mNZftFqVi_vaYA9QT99IUo7O9rNkmK237pf7U2MRrAopzeK2v91Zi2l358i8ZtNqm1A_Unw3AAtNkHy-cgDQAEKuGOXABFGO4pa7f_V6D44JXCH9g77S1o7AqHMI9mZgNeoWMVmSpucg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b075e3305.mp4?token=LHmGYLmJcWQfGh9w8v38SRnqXbNDUxCLn0FNbNVIjnDdejjEFJ3cD5vl97JwSAWC_xl2chVemcs3Ob7hE9LfC-gbo3Ey5ZJ-wiFfRKMFUZv3hwW3Tr7JL5AeRxvR9cIoeQjAMCvQGV7O-OSrqahlwnx2Fm8S9qSGHicXsIjO4OYSZt0386v3-YMjiOz09rJOwLpJ3iBIrp-j6VvI2Ldnr9HJAjC8D03l9AJHZNIKuktSdibEndzxGTEn8ts1h29LDaLPSPPVk9d0nXZ7dlg2Kal76KxQlTDur8BvAvd-n3pIMRf_6aWWtxY00BZf7ENvcwelgOmbA_3tMhNediDzbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b075e3305.mp4?token=LHmGYLmJcWQfGh9w8v38SRnqXbNDUxCLn0FNbNVIjnDdejjEFJ3cD5vl97JwSAWC_xl2chVemcs3Ob7hE9LfC-gbo3Ey5ZJ-wiFfRKMFUZv3hwW3Tr7JL5AeRxvR9cIoeQjAMCvQGV7O-OSrqahlwnx2Fm8S9qSGHicXsIjO4OYSZt0386v3-YMjiOz09rJOwLpJ3iBIrp-j6VvI2Ldnr9HJAjC8D03l9AJHZNIKuktSdibEndzxGTEn8ts1h29LDaLPSPPVk9d0nXZ7dlg2Kal76KxQlTDur8BvAvd-n3pIMRf_6aWWtxY00BZf7ENvcwelgOmbA_3tMhNediDzbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملات رژیم صهیونیستی به جنوب لبنان
🔹
منابع لبنانی از حملات هوایی و توپخانه‌ای رژیم صهیونیستی به شهرک زوطر، مرکبا و شهر الخیام خبر دادند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/442260" target="_blank">📅 12:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442259">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mg8qaR5Fbq12NnUS4vEwGcdjHwu8Rx7E07buIEDMkbFJmIz5TxhMMFcKENIdO-eaCVCd2aVGt3FiFMtoDvpIKZStEB4k1ZCV-23nOq7hzxNyroAc_LMfTPD8cQmkRt565s0y7J2j-tCu2p2e219PjePO9qb8Ynti_spnDTS2YeXeUB7YJ0ruiBv37AjwmgAshz1ZsSKqCOkU5ZMYkRdZowTKBZYhmgScZ0cimWksCXaG8IeKSwoITtwRO3NhWZn_HONkA4q1lv_WeiFTF_vDEAIcM0CJObsubobzvqu3gh46LLoiNdy4wgpEE_EO8HlFQvr49HgEgmgTbx0WGthDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ اسرائیل: قرار نیست از لبنان عقب‌نشینی کنیم
🔹
اسرائیل با وجود همهٔ فشارهای کنونی و آینده، با خروج ارتش از لبنان مخالفت می‌کند.
🔹
من و نتانیاهو سیاستی روشن را دنبال می‌کنیم که براساس آن ارتش اسرائیل برای مدت نامحدود در مناطق امنیتی لبنان، سوریه و غزه باقی خواهد ماند.
🔹
این سیاست شامل تخلیهٔ منطقه از ساکنان محلی و نابودی تمامی زیرساخت‌ها، چه در سطح زمین و چه در زیر زمین، از جمله خانه‌های واقع در روستاهای مرزی است.
🔹
نتانیاهو این موضع را به رئیس‌جمهور آمریکا و دیگر مقام‌های ارشد آمریکایی منتقل کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/442259" target="_blank">📅 11:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442258">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c004074d.mp4?token=UMKRjsE9GMM15T8lBfm-bbHLkqWSmhEqHBdDOYjdRqIsAdtc6VJXAcytKdA3l7fwxK9SMPuHGm3XXkGOMDU_vnZUBgwNvxiGw-HRnzO5oe11VTd_1tdGFYBRva_OEpttjaSzCJ8Htyvxgf2z6Zr78RMq3bsi2iTtknHLG2Q6fudcxdPG6Ymmdn3gU6IBmCNGOjOpllJVu4DLFdmAMzIj69yVhV3ruKn3aMQ7U03r72yIll78hzEY5lx2g6ilKVqz9GdGo-f8jPMifpYf20OlBYO6st5CPC_EM2FQTEF90bYe-4P3q4npmBB2JsnPxOLvaC1vEQOCEwwZFbCxtbNsDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c004074d.mp4?token=UMKRjsE9GMM15T8lBfm-bbHLkqWSmhEqHBdDOYjdRqIsAdtc6VJXAcytKdA3l7fwxK9SMPuHGm3XXkGOMDU_vnZUBgwNvxiGw-HRnzO5oe11VTd_1tdGFYBRva_OEpttjaSzCJ8Htyvxgf2z6Zr78RMq3bsi2iTtknHLG2Q6fudcxdPG6Ymmdn3gU6IBmCNGOjOpllJVu4DLFdmAMzIj69yVhV3ruKn3aMQ7U03r72yIll78hzEY5lx2g6ilKVqz9GdGo-f8jPMifpYf20OlBYO6st5CPC_EM2FQTEF90bYe-4P3q4npmBB2JsnPxOLvaC1vEQOCEwwZFbCxtbNsDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امیرالمومنین(ع) سیاه‌پوش عزای ماه محرم شد
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/442258" target="_blank">📅 11:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442257">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">جلسات شورای شهر تهران علنی شد
🔹
سخنگوی شورای شهر تهران: جلسۀ فردا در صحن علنی شورای شهر و با حضور مستقیم اصحاب رسانه برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/442257" target="_blank">📅 11:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442256">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e70803c3.mp4?token=chdhlfkIwZ8aaBSUe82oX_3V158SndW7F8XjtK68_oq1bTyQcBvPxKJnaI8SBA-kBnHNOgf3oace9lb2SPNDIfsaQZwTUhPqq7bXWA9l9SAY6HcK4KUVk1W5dzWPX2BRXIuGnva0eOInYfp9VcpHRsFhQPMx3PmQxcb10Sb42ECOAArRIh-NbH7PA00eCfoZeAvP3sfwbh5GSD4ONCaSFz9oyMSwATUAKT3oRwskvvM9StKypIhqDOYP_eVLQnO9PddL4gXahrHzCJr1KjivinzgpaYD7htnOy0t6i9JGV71wskCCb4ZNfQhSzTrG9dVvE9agWuDTcrz47kWCUAPQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e70803c3.mp4?token=chdhlfkIwZ8aaBSUe82oX_3V158SndW7F8XjtK68_oq1bTyQcBvPxKJnaI8SBA-kBnHNOgf3oace9lb2SPNDIfsaQZwTUhPqq7bXWA9l9SAY6HcK4KUVk1W5dzWPX2BRXIuGnva0eOInYfp9VcpHRsFhQPMx3PmQxcb10Sb42ECOAArRIh-NbH7PA00eCfoZeAvP3sfwbh5GSD4ONCaSFz9oyMSwATUAKT3oRwskvvM9StKypIhqDOYP_eVLQnO9PddL4gXahrHzCJr1KjivinzgpaYD7htnOy0t6i9JGV71wskCCb4ZNfQhSzTrG9dVvE9agWuDTcrz47kWCUAPQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: زیر بار زورگویی آمریکا نمی‌رویم
🔹
ما که تسلیم نمی‌شویم تا هر غلطی خواست بکند. آنها منتظر بودند ما در کشور با قحطی مواجه شویم.
🔹
اگر دانشگاهیان به میدان بیایند، از بحران‌ها عبور می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/442256" target="_blank">📅 11:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442255">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در مبارکهٔ اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای‌ کنترل‌شده تا ساعت ۱۳ امروز، احتمال شنیدن صدای انفجار در مبارکه و اطراف آن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/442255" target="_blank">📅 11:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442254">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXCkyM04dxnrxMVbDHtHYYiu3BLD3lmQ_-Gzc_ipsX5x3Zh6KM4uCLKK_vVl5JKOPlGYwOdNQdJcsDKXDNlSP5b2QUGpDTX8DMUFiZkZ6rUG7kvDa8Tk__sOspBfAr0fXCHXlAGWmulp1U3TMlkEJEvfi2zXX9sqrZCUcWaISy9iU-YXMj2gd09P89HU9g01P5DmyopqMjZ4sQO3sS6WBzHSeutLKjI0BfxoERM5ddhnOhJAk8s8rTYkoYayxu_dujvTNgdyWd84Gd8yYgK5uA6A4Y96lY1gPbtCL1Pkb2Rh1I9AoLvdiWmeOZSTt1mku4EGEWLCIdCDx0I_F2eVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لَا یَوْمَ‏ کَیَوْمِکَ یَا اَباعَبْدِاللهِ
🔹
به‌مناسبت فرا رسیدن ماه محرم و غم فراق رهبر شهیدمان از جدیدترین دیوارنگارهٔ میدان ولیعصر(عج) رونمایی شد.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/442254" target="_blank">📅 11:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442253">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7fHKIAF4o-dRussQUfdbvYoo6MvpOpIH8pIoUW-wJIZbdxl7H57X-G4Zu60hIJ6zVkcLhBvHjz2VQbAxB4AUXVdr5VJtMKzaJGoWFQp9Y9BC-B5XGiR7tIiV1V3zP7NM5rNGITXutmOWyDjmT9hwZ1diprh9jW7OqCb3TVohlNMxg1n83njRSiOLcQSfJ3cplogekvtxSuvgnQTDKRMA7YJGMhrfEQydABUKUCJbF_Rgpu5C54jD1e-mtt7uXenXh6-p2LcMOtBvXYxUyHeCwG_iI7BhHykMp_clGMB4Pt229i-enFxMf7iC2tKT7TYst8boLSeCK3gXHAVm1A8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی با وزرای امور خارجهٔ ترکیه، عراق و مصر
🔹
وزیر خارجهٔ ایران در تماس‌های تلفنی جداگانه صبح امروز با وزرای خارجهٔ ترکیه، عراق و مصر، با اشاره به مسئولیت آمریکا در قبال اجرای توافق، بر لزوم توقف کامل تجاوزات و حملات بی‌ثبات‌کنندهٔ رژیم صهیونیستی علیه لبنان تأکید کرد.
🔹
وزرای خارجهٔ ایران، ترکیه، عراق و مصر همچنین بر تداوم رایزنی‌ها و همکاری‌های نزدیک در خصوص تحولات منطقه‌ای و ضرورت تقویت تلاش‌های دیپلماتیک برای حفظ صلح و ثبات تأکید کردند.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/442253" target="_blank">📅 11:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442252">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حذف وثیقۀ خروج از کشور مشمولان غیرغایب در محرم و صفر
‌
🔹
سازمان وظیفه عمومی فراجا وثیقۀ خروج از کشور را برای مشمولان غیرغایب در ایام محرم و صفر حذف کرد.
🔹
متقاضیان زیارت اربعین می‌توانند از ۲۶ خرداد تا ۲۲ مرداد درخواست خود را در سامانۀ
sakha.epolice.ir
ثبت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/442252" target="_blank">📅 11:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442251">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615a222da0.mp4?token=oxgYpQXf_rCRz9nHQ_6OPCCEdF94xzekqBJUD_BY8PWiExsqVmrIiQRiXxRxDfotfNSzSmPDLEItW69tH4iR_U2BM6TaKravjtSXUOvPvfIN8k7FAmo8j_o0a1oEiIl8IRDkVdau_XG7V9Kzj0JtLF7QaNroFYs7HnQdk-V0WG9QIH9p2JfGA1AB1vICAJRPhrjOHq0uyJnbJvA51AL1mm7fzNp6rKg1Ul8sALFREUj6gJ9NvCJDJLc1Uq9eAN7i0a5jsi0wE_DGbznUluPMSgvR8ts5pcdxK-33NkHqq6P6m4nMEu0KOHof4YeXoGUqgPjJXHVRagPf_B-h_VhxTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615a222da0.mp4?token=oxgYpQXf_rCRz9nHQ_6OPCCEdF94xzekqBJUD_BY8PWiExsqVmrIiQRiXxRxDfotfNSzSmPDLEItW69tH4iR_U2BM6TaKravjtSXUOvPvfIN8k7FAmo8j_o0a1oEiIl8IRDkVdau_XG7V9Kzj0JtLF7QaNroFYs7HnQdk-V0WG9QIH9p2JfGA1AB1vICAJRPhrjOHq0uyJnbJvA51AL1mm7fzNp6rKg1Ul8sALFREUj6gJ9NvCJDJLc1Uq9eAN7i0a5jsi0wE_DGbznUluPMSgvR8ts5pcdxK-33NkHqq6P6m4nMEu0KOHof4YeXoGUqgPjJXHVRagPf_B-h_VhxTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روایت جذاب از مسئولیت‌پذیری و همدلی؛
این انیمیشن یادآوری می‌کنه که صرفه‌جویی در مصرف برق، یک انتخاب کوچک با اثری بزرگ برای همه ماست.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/442251" target="_blank">📅 11:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442250">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEQptnWAtHyd7uKOGoWSG1PvKsOBareR47kaMJFnsvs5AFKd_RwMHsmR-0jMlwUWgslgNuIrVXL7DAYSFuk9FqOc53rJR38dn7jgl1k2O9fxe-zfvA9T_HEcoArwD0RTVKl1Ufev5rsJKx-W0gCThweSugyHdivLduA763SdXNDEDWgnhr8mnNx5VQ561RFzzcurQHDx_YsG-8L3ios4Gas0r_Jnm0_MLCJHLIA7SVZZyN_Z35fjCj149Wr5dnaqQx3HWFhLHeYav5n1TYkli7bSGFopmn4yahuPpcjXhUbdGdOR6QD0XkSoOmwrou5WgSMy8800RWJQYGOfJojbiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
مبلغ تسهیلات قرض الحسنه بازنشستگان به ۶۰ میلیون تومان افزایش یافت
🔹️
مدیرعامل بانک رفاه کارگران از افزایش مبلغ و تعداد تسهیلات قرض‌الحسنه بازنشستگان خبر داد.
🔹️
دکتر اسماعیل للـه گانی با اعلام این خبر گفت:  بر اساس تفاهم نامه با سازمان تامین اجتماعی مبلغ این تسهیلات در سال جاری از ۵۰ به ۶۰ میلیون تومان افزایش یافت.
🔹️
وی افزود: برای این منظور بالغ بر ۲۰ همت اعتبار برای پرداخت ۳۴۰ هزار فقره تسهیلات از سوی بانک رفاه پیش بینی شده است.
🔹️
این تسهیلات با کارمزد ۴ درصد و بازپرداخت ۲۴ ماهه به صورت کاملا غیرحضوری به بازنشستگان واجد شرایط پرداخت می‌شود.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/442250" target="_blank">📅 10:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442249">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/442249" target="_blank">📅 10:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442248">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083b61f28f.mp4?token=gQ1v2sGIprF8iGEUEKhTMkKW1qwcbkzci11dcifAEy7kEvLVimL-5peAogA0f7b9VUBnNsvP8J2000hICLZyp_B2111PrGh2rNAsiqJF9eaL4t_EIMFpDVncR_d5tSULnIlEoac30NlDScr9-aAes2TtUy0Gd8tLc4-tZQmevPEaxS4x0yHrgJn4IHL23kke5thLpwuyvDP8plL6xgul3naDVqUK3eXia1qYnIpEEWtHYxDayPjElYfxV2t9qLajhy56KXecE8guVVTG1BsvHj-VY9ncG87IvUrO2TiCoEhMaVoOWmPaNFkMmROJ39RSFFtZOVDAzZo-Il4Qn9CScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083b61f28f.mp4?token=gQ1v2sGIprF8iGEUEKhTMkKW1qwcbkzci11dcifAEy7kEvLVimL-5peAogA0f7b9VUBnNsvP8J2000hICLZyp_B2111PrGh2rNAsiqJF9eaL4t_EIMFpDVncR_d5tSULnIlEoac30NlDScr9-aAes2TtUy0Gd8tLc4-tZQmevPEaxS4x0yHrgJn4IHL23kke5thLpwuyvDP8plL6xgul3naDVqUK3eXia1qYnIpEEWtHYxDayPjElYfxV2t9qLajhy56KXecE8guVVTG1BsvHj-VY9ncG87IvUrO2TiCoEhMaVoOWmPaNFkMmROJ39RSFFtZOVDAzZo-Il4Qn9CScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهروز رضوی، گویندهٔ پیشکسوت رادیو و از صداهای ماندگار ایران، پس‌از تحمل یک دوره بیماری درگذشت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/442248" target="_blank">📅 10:54 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
