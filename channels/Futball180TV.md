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
<img src="https://cdn5.telesco.pe/file/lqfnATbmRtCiMl6RavzFZ4ffRXFUOPzN98sckN0Wh96DUrpH70Xfcieq6G0qYroBBf8IHti4GUDH0Xjj4rx27zRjkBaEwbrid7FM34JRYFrgrzllY_L8iHuu20UPux02ijM4wOw28U8rGojtZ4QidRUFHxN2HXIPSOmvi19Smi1koMM5jhIjDalsKJ212qshhP975QyuwZBFNZQ7tx4KAdlsu5x2sPLIIXaSUEfpSMWLeYw4JWFdI5C5N011vWPphvNPbEpFZFUYUZI2fkfhmQ1mpTgqE-r1KD2xrXOuQ48jVSrKVDLWaC_UN1EZAHNXg8RTSdCnO6pY8NTu5n8GUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 410K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 13:03:18</div>
<hr>

<div class="tg-post" id="msg-106752">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3wPLSzp3L64qqsfsiMlXxVtOGIUEVfIjKJvf2b-dXai4bfPAB9JCyb6KKGNoBNJMsT1WaHGMiAkL7MEyw2D4nVrurxzTY0SPSpoLn6GPeH8zgaiMdlC8mCEdJjLyJumY-zI-d6fqIPMqeHKLFJ065iKqbOKJsgGn3dLQpC6vkle9GAz7wnm1G37jp9sW0Q3wDPdP6aDV2rQBIb-x2g6bUvGAla_xDIbY4bOv3ypOd8UlDPdcoMvz0syMLXKyo0IFmKliPlfHoSW5S6iVMDvAK8LkEkNbztBQP2sLnxibvNAv0vvsQl2Hs3k9sKxcPrA6CL4LV3LDsihISShTNXfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/106752" target="_blank">📅 13:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106751">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDOCYIT1gd-q2RV9TY3S_FF-uZJrDJiOG1CO5M6rK4zrsi8Q_J1rLLXCDTYtacek-UBr-DfHmshJtmN-PgSssXTPPXXWgmpWkEPQpJI6T2rdiqkTb3h6wsTeM-6Z1cOmxXF19Eo3Z_CxYfW6sz6x8fN5miLK4XM0kV6wTo5Egi5bv9DOcMkhszodBaYHJ3qNkv6YobjzxL-5lawiv-lvNYGfqmSV4vZ9WDix8UIHUjjEIjSaRCQyJy3f38Trej-Ol89b2qJHlZAGlEnfETenyoBi-NMFdVcNcuWrueUhycxpscstjY_tzPJbPlQSgRi2Bwyd_ivNoHoHCQhdLkVGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/106751" target="_blank">📅 12:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106750">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddepDEHH8_baNh0ur-ypsPOMKnKOM_7EidLr51yAeQrPugN1wz4fUbreDaBv8Yjdw1HkrX5Y7jSeCE86pbsDLGT0tp-nxMitDT3j4iZDytj6E7xNiNhiRMPypbNs28KzC49Vdtb2FI24YjSLak7Zsl51qMZoDLTQsJSNr73QvgTA9TJoo2O3OvIw6qYeC9K6GdsNyekOt6MDFaMZrkNRPzJxmJ6RipXR-nbeCJXUH6TDJiJnWZEpuxpV82Lyzv4gnOpsI6zRJxX1SvjMrM36WgajRk6eGMLnPjbn4rhap2_MnyVzqfOQV3Sx7xHrCnoObQ_SqPYcQNXs3NAlB07Lbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🫣
بالاخره روز پسر شد
😁
👍
‏در تقویم هخامنشی روز ۲۶ شهریور روز تولد کمبوجیه پسر كوروش بزرگ می باشد و این روز را در ایران روز پسر نامیدند. برای پسران عزیز زندگیتون بفرستید که حداقل تو این وضعیت کمی خوشحال بشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/106750" target="_blank">📅 12:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106749">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEi7vDRY9PiSnCw4WcnCbRdWrbAksjTruKbb1TW-x-RDp35qxbq2hTV1WIfTAAHf53kgDCLK6wXChECvs-FGiP55q4nW5-D2uofcs7Q59QYRzGtPsDhrAGG_u8U55zloLVDqV0AwIvOcJwhVX-qg_xcVgzaeJcFT7YrHY9sYGfaRiOy2Fy5JbFdST_gX2YollzFUX932UTNtQFJd7sRWZOZ5TIfL4CW98JzyzB9OFc86pkSveh9OY7BAg7enZjZ2nlxnRwqQz2NMRWZIsXGAmUNtV2m5zD8cmz5FvCPFwqV69SL_aAs1stYsdoVCZ9f5OK8r3HTMM_8drvnjdv7OTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
💵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بهداد اقبالی میلیاردر ایرانی به طور کامل سهام باشگاه چلسی انگلیس رو خرید و الان تیم کامل برای این آدمه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/106749" target="_blank">📅 12:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106748">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎙
🐐
🟣
دیوید بکام بعد قهرمانی دیشب تیمش:
🔺
هنوز باورم نمی‌شه مسی اینجاست و برای اینتر میامی بازی می‌کنه؛ برای همین هر وقت بتونم می‌رم سر تمرین تا ببینمش. به نظر من، با وجود بازیکنای بزرگی مثل هری کین، کیلیان امباپه، جود بلینگام و سایر نامزدهای توپ طلا، مسی باید این جایزه رو ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/Futball180TV/106748" target="_blank">📅 12:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106747">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb69509038.mp4?token=Lzol4gm1kbJHTnln-PrQUuTKHesxyJYIieoziyUPN-vewQZKECiCW3q1jmhwGhvAXOKvHYwaq8x5rOsoMaFndvyDxy1-pF9BJiFmw-42nnu3szp76JVwdcS_j39MuKuZNR1hBpJ22PXg1L1slbZdDcx2Bue8liKFNJep31Wyq8844DI1TiXUwSfWu2wWBM1yIP4r72P1xIQnqzea6Ou2MmGDPpyTnYgcAupOX2lv274TDKBL4Oo5YYIjTpRHadWuQxrDu2AeibvrJ8LjZWD694aEAJkuGr5_9fvSrT4qVkCkT4RXTFLSyPYywiC7VIRvU4zfDYk3PqcEe36zjpR7lkXXfMsYF8Pq7YgwzyxP0OST6ccycA5udOD2aM4GLNNCQNHINEs-mYbejygLW54Li3te0OPAMuq3-s5FRKXW0wPz8vx70syt0eaQOeFi0hQHv7e3pGWzBjAYt8R9u1ldHJl1Pnsel-dTcu8RCZgr144-U21mA36P5kD9JOlcvG03xoGYJq06aJIyXSRCLPS7RS2ty7x_TJaZjROBwK0TCnxBXrMl7XICwdFLi6nxIm727wf4fduAETGkJZuYbiJMkkDUWK3VwgAtByWmJ9sCwY9k4qjQdX5-gx7onoeyUv8iGIBDu7AfNNVt1sCMHMXs-AsU24Pz7t2Gj7DTvQSUOIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb69509038.mp4?token=Lzol4gm1kbJHTnln-PrQUuTKHesxyJYIieoziyUPN-vewQZKECiCW3q1jmhwGhvAXOKvHYwaq8x5rOsoMaFndvyDxy1-pF9BJiFmw-42nnu3szp76JVwdcS_j39MuKuZNR1hBpJ22PXg1L1slbZdDcx2Bue8liKFNJep31Wyq8844DI1TiXUwSfWu2wWBM1yIP4r72P1xIQnqzea6Ou2MmGDPpyTnYgcAupOX2lv274TDKBL4Oo5YYIjTpRHadWuQxrDu2AeibvrJ8LjZWD694aEAJkuGr5_9fvSrT4qVkCkT4RXTFLSyPYywiC7VIRvU4zfDYk3PqcEe36zjpR7lkXXfMsYF8Pq7YgwzyxP0OST6ccycA5udOD2aM4GLNNCQNHINEs-mYbejygLW54Li3te0OPAMuq3-s5FRKXW0wPz8vx70syt0eaQOeFi0hQHv7e3pGWzBjAYt8R9u1ldHJl1Pnsel-dTcu8RCZgr144-U21mA36P5kD9JOlcvG03xoGYJq06aJIyXSRCLPS7RS2ty7x_TJaZjROBwK0TCnxBXrMl7XICwdFLi6nxIm727wf4fduAETGkJZuYbiJMkkDUWK3VwgAtByWmJ9sCwY9k4qjQdX5-gx7onoeyUv8iGIBDu7AfNNVt1sCMHMXs-AsU24Pz7t2Gj7DTvQSUOIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت دیشب نیوکمپ که هروقت بارندگی بشه اینجوری استادیوم به گوه‌خوردن میفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/106747" target="_blank">📅 11:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106746">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
✔️
اعلام فهرست بازیکنان لیگ برتری تیم ملی
🔵
علیرضا بیرانوند، سیدحسین حسینی، پیام نیازمند، محمد نادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی‌عیدی، امید نورافکن،…</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/Futball180TV/106746" target="_blank">📅 11:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106745">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC352ZpuV3S-29NFMASH21OCxf-i33N3rCAFrPDjdd0GQ8vXy1MvoT-0PdRdzXvaN4y68oUOQ6-CPjbQU-xuVtKxsTxA6RDEy04GQwXGlhSgGDyMMtv482GERdQYF10OGLAGgixQC_hdy0AXki-PmFHo73c2iILo19LDH4DaobL_bL4UCV-ZPHtCL0F_QlQw8trv72jgCKMhOCaMGm45AEtWIxsSEau01oR8yQlY8lVtwtCfCzMOVP5MIyqJ3aS7odvID-0Y31QRglJyu2CVKu_P16e6JIOM3nFsi9LpUuXW-QB1mg8zNpJ0g3Uljy_BpuSb_PTQwIdzwTqfVQP9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
اعلام فهرست بازیکنان لیگ برتری تیم ملی
🔵
علیرضا بیرانوند، سیدحسین حسینی، پیام نیازمند، محمد نادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی‌عیدی، امید نورافکن، مهدی لیموچی، مهدی محبی و امیرحسین محمودی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/106745" target="_blank">📅 11:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106744">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b540a014a.mp4?token=FeItlOhyP38T5FdNiXWVOg_BxkbzwlrqXaWGGoPOo2xqJCONEa4mq3oapIkEgMaVMy5rHbtx5TAdZJKf3Jocv2YEYhfsDq2KhhoKW9qYv0uJXbxMUQJXdyAPOor-Lfm2ijpuMn6y87OjxBlw1xs8hzd9aLwP7A7aUcprc-JDLgu4Sm4vPS1VilT8A8wI1vp2Pk897BHHCj-fYq-0SZNNCZpfP5mN3e94NvDyZIHfHnfu1lL0uBEpfQP2Rv23u8J7rsZ7f-eb-G3e4W56MYlse7uUY0fluwVsqA_SH6rS1MUzGSA74kesHAw9sOmH19p2r5OITWwQ6jfYbVNGeNkSBIAbcaVZyGTc4kLunGgdN74mMgVUgreuRV3Aho7T5fUENxj9WAmeQ5DF7frD3TX4FR8SV0ZU4g8lfZlkepIrW_BGWvkzRG_10IDWE_jzEsJd85nqMI1uEwcGvvfUAQ3QhkceE8l45g1-_lh-bV2Uug6y5T1hb-rYK0hPzQSwRgGPQh4tikO3wdAEfsSYf4DBSfRxbI9lCF5VTVh6gLx-2B9UQ1vu8fNf6v1k-QgSCT1XH8hiSexBjVEwDcdFZUx8yJCHCfLnpDSk-QsjVbznRurxEsKuLKB8Zgw5fSg4JtZXHwFyHOAv2qD4wJPvvEW8fg8q_OWjsLPWL_9DrS0-kmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b540a014a.mp4?token=FeItlOhyP38T5FdNiXWVOg_BxkbzwlrqXaWGGoPOo2xqJCONEa4mq3oapIkEgMaVMy5rHbtx5TAdZJKf3Jocv2YEYhfsDq2KhhoKW9qYv0uJXbxMUQJXdyAPOor-Lfm2ijpuMn6y87OjxBlw1xs8hzd9aLwP7A7aUcprc-JDLgu4Sm4vPS1VilT8A8wI1vp2Pk897BHHCj-fYq-0SZNNCZpfP5mN3e94NvDyZIHfHnfu1lL0uBEpfQP2Rv23u8J7rsZ7f-eb-G3e4W56MYlse7uUY0fluwVsqA_SH6rS1MUzGSA74kesHAw9sOmH19p2r5OITWwQ6jfYbVNGeNkSBIAbcaVZyGTc4kLunGgdN74mMgVUgreuRV3Aho7T5fUENxj9WAmeQ5DF7frD3TX4FR8SV0ZU4g8lfZlkepIrW_BGWvkzRG_10IDWE_jzEsJd85nqMI1uEwcGvvfUAQ3QhkceE8l45g1-_lh-bV2Uug6y5T1hb-rYK0hPzQSwRgGPQh4tikO3wdAEfsSYf4DBSfRxbI9lCF5VTVh6gLx-2B9UQ1vu8fNf6v1k-QgSCT1XH8hiSexBjVEwDcdFZUx8yJCHCfLnpDSk-QsjVbznRurxEsKuLKB8Zgw5fSg4JtZXHwFyHOAv2qD4wJPvvEW8fg8q_OWjsLPWL_9DrS0-kmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
آنچه در بازی دیشب بارسلونا رخ داد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/Futball180TV/106744" target="_blank">📅 11:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106743">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-Eht22afIexjk_2-ViajeFB2mbyDX1y-fV4kzGsi-MiL57oMwd-TscsECtyVmcTTzsOEobIah6eBro3MYFcbg4aRCtNjY2SOlxPAPICZXoX4TlBQHU5IuGk8bS6RcgmvGk57bDvWoXcoK1sHic0U-8d28tZTAaHxQIjzG1MTAeSG3lhHLSzePWm13EnlHgODWOGYJwlrh1e94lBtIGzGH3MTz8n4sREFNQqLT19CAqrk9_nLT6a2UQfIQKDGeCA3O689MIF3PpChs3N0HdwapGS-TxeWNywCm2yaZ1TlJq3OFqrdmhF0MyJ-5sfc5qDxHNLH4eFL0VT0LV8CQjajw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📱
علی‌ضیا هم رسما با انتشار این عکس اعلام کرد که زید زده و دیگه سینگل و این‌چیزا نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/106743" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106742">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106742" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/Futball180TV/106742" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106741">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MD_yEX2LSvcXmh0V3rtCzF10-x02lMczFy8f9yNOcGe_MDvLIfhyqO9UQ9e954TvyhzGEBICDuJIru1YfTwjfMfPI9fEoFUzJ_aiuk2ZCRyrOi5xtLmj7DKKs-q8CSUVqC5aC7_reNOzSppnibqPMnyLtuWqMMral4qmtfMgrI5i5fm0sv5Rnnbo0wG3VE4uErcjv1VogJvIFx2sFzyq9Ov6roIajm8aHWP7PDXuBWLizKPup1SUmn7X22SEybWAiNrl84I_H5OCS-bULJMqTCQd7O49EqQoNstm6JdTZBqrDVCqi7jXJavgW3eUi_IvEjaZk3qiUKdbscujuFqCiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ان‌ئی‌سی نیمیخن
🆚
یونتوس
نوریچ
🆚
منچستر سیتی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/Futball180TV/106741" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106740">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee3ee373ec.mp4?token=uVIBMUZKFOAzTMFtdZnxHr7zAq6xEll_os6vvr9NvblHG02dRFiezlJjDxPfkYLcnBgPJH32TuhBLgVGNpuM0bYwXpD_E9JrgdcLQvqtIK5WNJz7dhLXN_m92D-H3ILS2tna3_Tjz8B-hu3rY35KTZk9G_mGGWgS9XykQAw1oOl9taoJ1ITUJUr2hkd-P7NTaw7Z8xu05Ka0GK4ZGyMFMVLAl5zwDxu7KyPuHkEUhef8pq-6CpJsUxfZ7UKEzBgElZPeb8hwFmOpcJvwWliRAL35iNvcu2V36sxymPb6CarwPd_Pj5Gys1_QKDWK26ZTlg7O2iPrOfIWtdJXIVC8WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee3ee373ec.mp4?token=uVIBMUZKFOAzTMFtdZnxHr7zAq6xEll_os6vvr9NvblHG02dRFiezlJjDxPfkYLcnBgPJH32TuhBLgVGNpuM0bYwXpD_E9JrgdcLQvqtIK5WNJz7dhLXN_m92D-H3ILS2tna3_Tjz8B-hu3rY35KTZk9G_mGGWgS9XykQAw1oOl9taoJ1ITUJUr2hkd-P7NTaw7Z8xu05Ka0GK4ZGyMFMVLAl5zwDxu7KyPuHkEUhef8pq-6CpJsUxfZ7UKEzBgElZPeb8hwFmOpcJvwWliRAL35iNvcu2V36sxymPb6CarwPd_Pj5Gys1_QKDWK26ZTlg7O2iPrOfIWtdJXIVC8WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
از عجایب فوتبال ایران؛ دیروز حین بازی تیم بعثت کرمانشاه و نفت‌وگاز گچساران یه نفر درب اتاق داوران رو شکسته و تمام وسایل قیمتی تیم داوری رو دزدیده
😐
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/106740" target="_blank">📅 10:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106739">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebaf856a1.mp4?token=T15vaTsUkWwht5ZaAza3gDrt5DlJB0fTU5a2DGRWuLZWAgwXX6J5Pu8r25z3YM6052FM-MEePIXQisWANcxS71luUWs5o0L73CNjfIk1Ifw4mrhEGBXLuQRszAfWoqUL5TVJEQycF7awx1Vf-d3OhFJptA1xJq7zih8sAKMvSvuNwAir1Zyseoc1WnY2RQHT_8vtLUaG0fpVnPZDCjuMEZ3DwF3JDHG64cBAlT6cFfzEJ7l-ym2XS5dw89_fuelI2_kIpx_gY4S1FbLWFnyDl2WfCqFOj7LFSoRrouTj_6iUaN1n6pFCrz_K6XLlmD7cGIfhC-Fv11sC9I34aozAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebaf856a1.mp4?token=T15vaTsUkWwht5ZaAza3gDrt5DlJB0fTU5a2DGRWuLZWAgwXX6J5Pu8r25z3YM6052FM-MEePIXQisWANcxS71luUWs5o0L73CNjfIk1Ifw4mrhEGBXLuQRszAfWoqUL5TVJEQycF7awx1Vf-d3OhFJptA1xJq7zih8sAKMvSvuNwAir1Zyseoc1WnY2RQHT_8vtLUaG0fpVnPZDCjuMEZ3DwF3JDHG64cBAlT6cFfzEJ7l-ym2XS5dw89_fuelI2_kIpx_gY4S1FbLWFnyDl2WfCqFOj7LFSoRrouTj_6iUaN1n6pFCrz_K6XLlmD7cGIfhC-Fv11sC9I34aozAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
🙂
آرزوی هوادارای رئال مادرید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/106739" target="_blank">📅 10:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106738">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
⚠️
خودکشی سرباز روس با استفاده از نارنجک پس از زخمی شدن توسط کواد اوکراینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106738" target="_blank">📅 09:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106737">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/704ad943ef.mp4?token=F497xBLfKLUrsrQVYVuqBiXJouMEhmIHpUCatYn-479TRYVrRi8j5UAUXUHiPLJxMrKEcCIyaYTTW1FDLmM-q8z1o2R3E-rN_V7aAdT5BWr0KTZ68bbHPyblkSPG-pGTOdjUxG4Wf5O8EIoVbQg3FY_O95PqH5HZV3h1zhg2oOImaW_67ADUwOTIEOZ_BgqNYQLKpUTwVsSTiqGpP4CNHvcmkqX9_dUnNPdyq9fsO4bDTpR0fFlhGG8s-88toLG1SjBfO7__nMpsovXHLbFOuSDpGUH_o3JCAvEvyJPGBgojHhYiSfPMoTv46QKySxnIsKCKANP00codJxNOGrla6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/704ad943ef.mp4?token=F497xBLfKLUrsrQVYVuqBiXJouMEhmIHpUCatYn-479TRYVrRi8j5UAUXUHiPLJxMrKEcCIyaYTTW1FDLmM-q8z1o2R3E-rN_V7aAdT5BWr0KTZ68bbHPyblkSPG-pGTOdjUxG4Wf5O8EIoVbQg3FY_O95PqH5HZV3h1zhg2oOImaW_67ADUwOTIEOZ_BgqNYQLKpUTwVsSTiqGpP4CNHvcmkqX9_dUnNPdyq9fsO4bDTpR0fFlhGG8s-88toLG1SjBfO7__nMpsovXHLbFOuSDpGUH_o3JCAvEvyJPGBgojHhYiSfPMoTv46QKySxnIsKCKANP00codJxNOGrla6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کادو ولنتاین سمی مسعود شصتچی برا زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106737" target="_blank">📅 09:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106736">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546d8bc40e.mp4?token=f8szgZIsRJEaFijR_7r-TbQJix2sPUX3bjFC6nj-ua3UNU-WpzekZC_w4bHQq6IflVe5Vwr4bXP03Je3AMLXTlrdHq05AvLIFGgXjhEcT9V8G-lyXqB2fZineyh6IwTvL3AWvR35DhEAHPM-fe45mx_Z0KR_yclgh2V6BTWyvYFwy17zaWrxTjjtbHzb9Z4Bxjxi5x6PNZJ5G7Cq0M9Bro0V45lfysJ4xVLIgrqG4z6AM2n1njcHBrb8ZshJTImBDP0tIhH0CXoCb2D2IcUbv0ysiFzp8DZ0udiXxRat9roM5dfFRE2KAbxtdYfPbVuvrcWBj4fJQIXrGzZMsup8MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546d8bc40e.mp4?token=f8szgZIsRJEaFijR_7r-TbQJix2sPUX3bjFC6nj-ua3UNU-WpzekZC_w4bHQq6IflVe5Vwr4bXP03Je3AMLXTlrdHq05AvLIFGgXjhEcT9V8G-lyXqB2fZineyh6IwTvL3AWvR35DhEAHPM-fe45mx_Z0KR_yclgh2V6BTWyvYFwy17zaWrxTjjtbHzb9Z4Bxjxi5x6PNZJ5G7Cq0M9Bro0V45lfysJ4xVLIgrqG4z6AM2n1njcHBrb8ZshJTImBDP0tIhH0CXoCb2D2IcUbv0ysiFzp8DZ0udiXxRat9roM5dfFRE2KAbxtdYfPbVuvrcWBj4fJQIXrGzZMsup8MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
یه زمانی نوکیا به تمام ایده‌های ممکن ساخت مدل جدید، نه نمی‌ گفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106736" target="_blank">📅 09:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106735">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3Ast5JPNJPsL3mXb9c_dcHDh5s68sYgsWPbofGieHpZHC-JleGXBYPlVggowE6kt56u64w1cnAdVJoZoxXnqtfVrXVsO65uYlxj49TQGCDOrdHUqSuCv0PFhxVjRrojlfHm2V9x9kvqTm4J8dQ6kYRmRg-YDgAw6xaHb9Wgyxpn7Z19IyGs1JWJ6sI_H3JegKQ_-IzkCzJzXPCQJBzUYxfXBimRO7Tca8MKFojkBayq8qmHpDZvvQdKrRxOgO2smLDeUp9K8ae4G2uziKV8WFTHRxBwddt05dEHMOGYjyD6WCW6wSUdaI9r7SACm1JU7oeYAPrFsaaaGMmvMM6hBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🐐
با قهرمانی بامداد امروز‌ در جام قهرمانان آمریکا، لیونل‌مسی به ۴۹‌مین قهرمان تاریخ فوتبال خودش دست‌یافت و رکورد خود را بهبود بخشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106735" target="_blank">📅 08:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106734">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106734" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106733">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qpBzNDTltf4RzCvf2mkfDAMM-TxMj43EZksMn2s0xZGuLtNNViPcJdhnMHKduwFF8dpVDjduUR_aNro6x3zr_IG9e6DyIdCMO3WACw5jD1Ru-Tb-uXDlaB3Ia9VypsxuC-rsd-aeAD_sTj3EOG9aqYoz8jBII94VuhbcbUS2Y4f7TB50CTAmjYbiiYBZcqKZYlljlHvwGk5sViE-Ivl3rDvmeVPz2F50umUBEd4PFh0UiBzhfw_OMwC63y7qxVJTSNSjiWGZjEi0lea6vG1kbw9XcuxbcbO-h_GAXsCoGlbQKGY0pFBmaKQUJfGFfuu8HKoz88qk7V5u3LHF5rKhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106733" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106732">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0WhiJMG6vE7RIivrQMvMhV9elaB5nD0JgkNMSgsRO2lih1oVmuw1pH_xrKY0d6kLwWHYfiEJw4s-vTdDwQFS3XldyMb8pVc8ZMaRHyy00HK9aMGlUbY4FkTkkhf1imyxyrLo7HyOALYS3ULRap2_Hm0FOYUYqMANjVaRkzUUtgBa7S1gn_Y0Yb0PyahszMUCepfZ7RNHlcRUThO0cwtJ8-m6YK49vHuLNxuKDIIE15UYaAggTrq2mnalG5f2UZNVO9Z5sBC9DXzxbbpcdvouiMhzP_M0HG5KwgYVbS9uNxMWObPiQUyJkCbVqLT4tDjlWSGKKQg36IwgKJveOvBqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
تواضع و فروتنی رافینیا کاپیتان بارسا:
🔻
من میخوام به لامین ، کریم و گوردون کمک کنم تا گل بزنن ، میدونم مهاجم نیاز به گل داره. ما خانواده هستیم ، توی خانواده باید مراقب هم باشیم و به هم کمک کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106732" target="_blank">📅 01:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106731">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8hh15YjvQT_DTH89JUcqfnNkYLZhbNBsmTQHvFb5_mgw1-ILp9J2KwF8V3d6fuYLOIEhClf7R6oARG9GpAmJuthGU9MOxAXRPJoJKF8vYxsO-uZEKbybtjE620Xmr73rOb6nsZAqiNFjwOckiVhst3XOMhly6jz-Bu36s6k-oHHmxsbmY38e2_32frt2QHXhqzXg5-jfsyTw0N0uhWlOv1ukLbNL0HrNv4n1sadWEsjlyeD0Q7rRqmHbUJ7HOOLQsUrUUPu8PEoGuC6i1GH7Vc8wbSFk_nju7DV-0S0jIuCD3K4TuScFd8AtGGvmWJ5JOJNewj5v14ghH91JB5DWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
تواضع و فروتنی رافینیا کاپیتان بارسا:
🔻
من میخوام به لامین ، کریم و گوردون کمک کنم تا گل بزنن ، میدونم مهاجم نیاز به گل داره. ما خانواده هستیم ، توی خانواده باید مراقب هم باشیم و به هم کمک کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106731" target="_blank">📅 01:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106730">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OruG5Z5-NvGhTtE23GvPSeIpSNodngndruvpCloegsWaUOF1cfa6E3nM27ckrgv3fxcr7T6igsnb4JQcgOLR5bOBLeXmy-3Rv0id8tZshW7GTWflo1uVPtqAHattrcQwsGeg8EK3ygErbKq923x4mJVri_iPH8j0iUiJmkdskasBhu_3k8njwPGtiv-AwObt7Y-cBZl4x4JxhN0nHKQkur85UmNOsuSF63WGlt4CpBzIlzJA6ci_WF2WpTYuo9tWShL0x2G70zaSl4jFC-69cBtYYJWAiFLnOoku7kGr-98ap-b3OFrHnKX2nTIhTHTFqclhGAZfWpyM1Pwu1M9-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
شاهکار این‌فصل فوتبال اروپا بدون‌تردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106730" target="_blank">📅 01:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106729">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1vtGlGvIldsanIz0rTnZtpSbMBsJa6Ogs1SRKPTeQyN8lPCqP7zstLq3fu0CXo6HzH3NWteEgAJBMJbKxVAvCz6txxQbvqCCOzVEZHUshjXUHky2YrCmUdSoTnzrc4Ow7GM6RMo-xjZWbMrxIJqCtrVkWIkEj0N9mC8IyCjUCibw25QT5Mg2udRiLJyp3N7cal8Sjn1RC5m1Yl51eLwY5zvk4waQdqSQaIna0eZ3asxE5jFoV9aXEzPDWx9pJtlcnoqnSEuRrpok1PmC8KoDdc9yjC1wcAuGrL3wfHVzSxNA6MgM4jOAhWgttoQuxacl6qXuLUU8vSQrHvn3gtQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
وضعیت جدول لالیگا در پایان هفته‌ششم
⚔️
برنامه بازی‌های هفته‌هفتم:
🇪🇸
رئال‌مادرید - اتلتیکومادرید
🇪🇸
🇪🇸
بارسلونا - سویا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106729" target="_blank">📅 01:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106728">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnMS-_w4WksUEjysUE_snxcIeqd6XYO2fUju-Gz4sSnL6E3RFvVIkQe02XTC3n9qVROV28OcplLJrKG335cROGgZXa9sJ83aA1T71Pzg1CRk3pyENNtRN6RrZY7TnZYagagg6YfmZ9B71p3pCkcKDBPrPRiNi3LQs-_71a6Yq-8mP81FKQniJNbyRioX9-VDMzLgx26JbfIPgj8CNTbxmtCma05ikBZwUSCTAf9Iw7xwEE-7PdaIOL45hgJJZHm_-1zraynjaxpLOWx38hU51wylr3Qc9Cnxh5L3-7pdFNviHoZvrYfZRBK6xx2eyf2YDg-9AUpUZbcLjAlC11qtLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بارسلونا بهترین شروع فصل تاریخ خودش را رقم زد؛ 7 پیروزی متوالی(لالیگا و UCL)
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106728" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106727">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLRbLcwLqQ3v-oj4kgMKTr6BtIX1XHzTS6ZRzdxachTFNN0ZQi1-B93bSwUetEgvPSLgQY3NghRv_97wiZPMAwZ7zHjryhpUw9ABoIaFq_BWtMC3iAnO0PVJk-58Ho4iznWOOm8qnewlOdwrkUu_GLuxyETfGR8zROnX2Xj5uJx0RK4Df-q7jDu-ojpZvmECoDLUYcjTrBdsCHI40rTbbZWuNQPUPjPtJhOAViJSQNZkq-qsJS7q6bUhDLu27sgYguhHgVvRTwBKcCsEuLdquEU3JpVSOwCYVO71QfRa7Hll0-ER9ZRdEABsh-WBBYkJMMUDuPUDEWcppp5Wa0Or9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لالیگا| بارسلونا به لالیگا رحم نمی‌کند؛ همه را گلباران می‌کنند و یک سؤال: بعدی چندتا؟
🇪🇸
بارسلونا هفت - سانتاندر دو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106727" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106726">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">لامین‌یامال
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106726" target="_blank">📅 00:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106725">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هفتمیییییییی</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106725" target="_blank">📅 00:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106724">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گگگگگگگگگگگگل</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106724" target="_blank">📅 00:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106723">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fd0c97753f.mp4?token=ANmBG4L08jm3Xacagfdy9AU9ilUjtT3FbRXnbp1-ZdXEshJTfT91D35xdTWIDvipmzzeslTy4Fi6eocGYeZdmjsCFAaKusaZPXKq5pB9zMFjDHh2NnFKEYPcWwKzr5bfV8E875TP02hMa8mqF0Ws4C4duTBJIH4C8-Lq5mt6AYb_HKfyXSx9NPj-InREcaTaArFAk5bMtfu5yh2f180mPG9BxlWXazUFSFqIjQ383PCBPoBybRY7_4GYjjWJtqKM7cOxU9SqahnJeHxpXlfxQL_vNzEb5f9vbYrUsN4uJx3PI-D2wLDFnc1yyg4mx4doEwUrnK464s7nvPyhcSmrpA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fd0c97753f.mp4?token=ANmBG4L08jm3Xacagfdy9AU9ilUjtT3FbRXnbp1-ZdXEshJTfT91D35xdTWIDvipmzzeslTy4Fi6eocGYeZdmjsCFAaKusaZPXKq5pB9zMFjDHh2NnFKEYPcWwKzr5bfV8E875TP02hMa8mqF0Ws4C4duTBJIH4C8-Lq5mt6AYb_HKfyXSx9NPj-InREcaTaArFAk5bMtfu5yh2f180mPG9BxlWXazUFSFqIjQ383PCBPoBybRY7_4GYjjWJtqKM7cOxU9SqahnJeHxpXlfxQL_vNzEb5f9vbYrUsN4uJx3PI-D2wLDFnc1yyg4mx4doEwUrnK464s7nvPyhcSmrpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا حضرت عبااااااس چه گلییییی زد
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106723" target="_blank">📅 00:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106722">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پاس گل هم لامین‌یامال دااااااد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106722" target="_blank">📅 00:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106721">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">چه شوت محشرررررررری
😳
😳
😳
😳
🔥</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106721" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106720">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گابریلللللل ژسووووووووووووووس</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106720" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106719">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چه سوپرگلییییییییییی</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106719" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106718">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یا مولا</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106718" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106717">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b622b454a4.mp4?token=Ojwq7WYWF4b_AUBRInht1wdufFm6O5ndJ_N0ohdfbYGZT8DHfjYc0ZIZfXfNwWHAWX0EbAnLtIKBZF9yjvvPLBSDxmsygFC370u8G7Ok94yd5ataLPTX-oaQ38Hkarwnfj_hye5cK1q8cRQ8-Tut7nEDMrSlny742lhyvf9c9wvUO87UN2hntSUS8AA2Cu-Vh2atb4N4gfJ3VEvavVA3jx_CIbB2dPY3wznDh_Qptj4e82gI2c0jdOpp8C9dMZ71cOvfnN01rh6w_Pjr5ZCj6eTFAzHgvM7C_GKtPlmn2a9o6d3a0Cqpnis4MWMO73SbYcfqPsO4tmmcm7iiSjEtuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b622b454a4.mp4?token=Ojwq7WYWF4b_AUBRInht1wdufFm6O5ndJ_N0ohdfbYGZT8DHfjYc0ZIZfXfNwWHAWX0EbAnLtIKBZF9yjvvPLBSDxmsygFC370u8G7Ok94yd5ataLPTX-oaQ38Hkarwnfj_hye5cK1q8cRQ8-Tut7nEDMrSlny742lhyvf9c9wvUO87UN2hntSUS8AA2Cu-Vh2atb4N4gfJ3VEvavVA3jx_CIbB2dPY3wznDh_Qptj4e82gI2c0jdOpp8C9dMZ71cOvfnN01rh6w_Pjr5ZCj6eTFAzHgvM7C_GKtPlmn2a9o6d3a0Cqpnis4MWMO73SbYcfqPsO4tmmcm7iiSjEtuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇪🇸
گل‌پنجم بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106717" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106716">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گلگلگلگلگگلگلگل یامال زددددد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106716" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106715">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلگلگلگلگگلگلگل یامال زددددد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106715" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106714">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a4e9698bbc.mp4?token=eHni_bfBaM20KDW12q0Ah_8tUPljOFdEFzhQdoewN0dkaAHjpGkBAuZD1Die2rKKrx6yfpvdh8dt4qFYeIjS1c40STg2pk3jX-GWEvzQ5piKHNfmwRgjUUipDfoMl1ZSmYWnK9JvUCzJj9gB0gA1kMvHPJdFqJB4FzfiySTjbrj_KHgCEtmM18M4DdTKYG0BfMbJB0OmOlm5ToKmV53l-j9V-FrA5Ksu8rx3HrPRJ7AUQKUZ-lF_zdzAZBbFhPmfKRE4Z4IZ42H2eKu8Q2nZ0Dnwpr7e-UGHDe4fxIXJo7gM_ykkz2t6FOzjC9Ohott_kygNW1NcnCqYOhIB4jo2SIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a4e9698bbc.mp4?token=eHni_bfBaM20KDW12q0Ah_8tUPljOFdEFzhQdoewN0dkaAHjpGkBAuZD1Die2rKKrx6yfpvdh8dt4qFYeIjS1c40STg2pk3jX-GWEvzQ5piKHNfmwRgjUUipDfoMl1ZSmYWnK9JvUCzJj9gB0gA1kMvHPJdFqJB4FzfiySTjbrj_KHgCEtmM18M4DdTKYG0BfMbJB0OmOlm5ToKmV53l-j9V-FrA5Ksu8rx3HrPRJ7AUQKUZ-lF_zdzAZBbFhPmfKRE4Z4IZ42H2eKu8Q2nZ0Dnwpr7e-UGHDe4fxIXJo7gM_ykkz2t6FOzjC9Ohott_kygNW1NcnCqYOhIB4jo2SIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ریدمان محشر شزنی معتاد
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106714" target="_blank">📅 00:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106713">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رافینیا هتریک کرددددددددد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106713" target="_blank">📅 00:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106712">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگللگلگل</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106712" target="_blank">📅 00:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106711">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رافینیا پشت توپ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106711" target="_blank">📅 00:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106710">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سومین پنالتی بارسلونا
😂
😂
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106710" target="_blank">📅 00:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106709">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پنالتییییی</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106709" target="_blank">📅 00:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106708">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وااای عجب ریدمانی کرد مرتیکه معتاد
😂
😂
😳</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106708" target="_blank">📅 00:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106707">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شزنی ریددددددددد
😂
😂
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106707" target="_blank">📅 00:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106706">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-9HAqRr9DPjd8Nc6rpAnYCbtoBREkIKnMPCvHzik-fUxPpzJ2ZsWAnPsx2stwHLAPl36ZaZQ6tcM-_AKCwdBwZVpnF-mFyFwuvnbKQgzVUivmnPvTo9g_wIYVyrnod_24m1tPj9tdH9TLjXw_VyXanWOMACEdQ80N9XU7ALtl8gYm9bHUXg_A3ZCJ729gqCm66zvXqst5V6dzoeWuY9YaRFKYTWLSRIF6LvmppqjAuTKF0OXcR0xPDFa5Z6nP2eXsFDtB7_I23CwFSqnHW9n6RAfM1NZZ5NaNp6yVkO3AbyBA4mEqDiq4BpeXViG0LKhLDRIM2J_hS92-jXCdBPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل‌سوم بارسلونا توسط ژائو کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106706" target="_blank">📅 00:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106705">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یامال دلقک کارت هم گرفت
😂
😂
🤣</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106705" target="_blank">📅 23:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106704">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33d7bb9281.mp4?token=E2dnzJ8rA6Oss4pLLCPlRVVf9eSc_kHvTtzl8C3iAGpnuGyHq2SkuvLG4-gk5dOT2tzWI15aMWo987w3ghFdATkukvD8RNuqPawZx-pAaNAF7R3K5PU-IQUNj96knNBeygAozIOZNdEM0YZg0w11QZmV-lgP6FcKkSmUUixn1i_9Q_6pPkIA6ZQi4vOQJ--8U2YwLcqm8USFK8ED8oydeDmBRZRfmA1Sxec3yaOdvQ2Pq48aOJYfLJtWdYTpzgunIA9YMyhOsUFpjlsGIZkLER4l8GN9XpV9CUQZ62ZJnWjP8bWnaOiNTiIVBmpwXvrkvAXFjBT5WmDc7Njt4LEsJoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33d7bb9281.mp4?token=E2dnzJ8rA6Oss4pLLCPlRVVf9eSc_kHvTtzl8C3iAGpnuGyHq2SkuvLG4-gk5dOT2tzWI15aMWo987w3ghFdATkukvD8RNuqPawZx-pAaNAF7R3K5PU-IQUNj96knNBeygAozIOZNdEM0YZg0w11QZmV-lgP6FcKkSmUUixn1i_9Q_6pPkIA6ZQi4vOQJ--8U2YwLcqm8USFK8ED8oydeDmBRZRfmA1Sxec3yaOdvQ2Pq48aOJYfLJtWdYTpzgunIA9YMyhOsUFpjlsGIZkLER4l8GN9XpV9CUQZ62ZJnWjP8bWnaOiNTiIVBmpwXvrkvAXFjBT5WmDc7Njt4LEsJoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌چهارم بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106704" target="_blank">📅 23:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106703">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9b1574719c.mp4?token=s5I9Ix-McvzU2mL0V4B6RORVm1OZDdcUNQ1ryi6xMU4kikAiqjw9ofX9d2D5yXeCMF2MiU2dR9IOtjMpna43lp3QUsIdgpjKP5SpKoIwvlr3HLz1fdv0t1Fi4HkBBJaIL4JZN1RrvKytjnbnxmBc42_y0ifdsXGAa59UwoLKPk_o4mMFXwws79P2epYmi4hT-TyOLtW_mYLuku1YidVmhL2XeecJnXDpntVh1ZtFSBLhyzj-BCfuK_33TvjwBLF1fX6Y56tiomakQVtV3obPD8zRrlYfw5voF7zp_pS4cP1BAuXMd4oKrVW4ojjVEUzxuTA9IQQPe4y4eZXwO5YoRlmpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9b1574719c.mp4?token=s5I9Ix-McvzU2mL0V4B6RORVm1OZDdcUNQ1ryi6xMU4kikAiqjw9ofX9d2D5yXeCMF2MiU2dR9IOtjMpna43lp3QUsIdgpjKP5SpKoIwvlr3HLz1fdv0t1Fi4HkBBJaIL4JZN1RrvKytjnbnxmBc42_y0ifdsXGAa59UwoLKPk_o4mMFXwws79P2epYmi4hT-TyOLtW_mYLuku1YidVmhL2XeecJnXDpntVh1ZtFSBLhyzj-BCfuK_33TvjwBLF1fX6Y56tiomakQVtV3obPD8zRrlYfw5voF7zp_pS4cP1BAuXMd4oKrVW4ojjVEUzxuTA9IQQPe4y4eZXwO5YoRlmpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بارسلونا توسط ژائو کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106703" target="_blank">📅 23:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106702">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ae99f7d7c3.mp4?token=opToq2kTZLFCMEnPICKq8hz6k-VEseUo-KXMv64SLvd7CrXk0Kzr4ljtN9RtJQjkEieQ4Rfhju4ieLXAchcSpUBREL0C2oDioOeu77qoSxaUAjNZ4J0bHZO2jZIVgR_Q8im0XZzoF0WBOcd2rzhBae6Jqh-aSepWs2U5KJ0ZTWGJ90QtdyXePG3GKN7O8F9QTpAgZzCORdBDWHt4GBvNx-LrdVNYluXVavjxH97h-whsHfLH26crbpE01-goQ5UMSf7eA1s1L185cvPC2sjz3pyrfRJlXgiV2Q4JaMK1oLYWfbcW2xm2fI0jOk6KMzEKg9i35ebfAkpg1ez-AKmP5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ae99f7d7c3.mp4?token=opToq2kTZLFCMEnPICKq8hz6k-VEseUo-KXMv64SLvd7CrXk0Kzr4ljtN9RtJQjkEieQ4Rfhju4ieLXAchcSpUBREL0C2oDioOeu77qoSxaUAjNZ4J0bHZO2jZIVgR_Q8im0XZzoF0WBOcd2rzhBae6Jqh-aSepWs2U5KJ0ZTWGJ90QtdyXePG3GKN7O8F9QTpAgZzCORdBDWHt4GBvNx-LrdVNYluXVavjxH97h-whsHfLH26crbpE01-goQ5UMSf7eA1s1L185cvPC2sjz3pyrfRJlXgiV2Q4JaMK1oLYWfbcW2xm2fI0jOk6KMzEKg9i35ebfAkpg1ez-AKmP5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106702" target="_blank">📅 23:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106701">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این دلقک توپ‌طلا میخواد
😂
😂
😂
😂
😳</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106701" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106700">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یامال ریددددددددد
😂
😂
😂
😂
🤣</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106700" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106699">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پنالتی دوممممم برای بارسااااا
😐</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106699" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106698">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل سوم بارسلونا ژائو کانسلو</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106698" target="_blank">📅 23:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106697">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بارسااااا خوردذدذد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106697" target="_blank">📅 23:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106696">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106696" target="_blank">📅 23:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106695">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رافینیاااااااا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106695" target="_blank">📅 23:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106694">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بارسلونا ۲۲۲۲۲۲۲۲۲</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106694" target="_blank">📅 23:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106693">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106693" target="_blank">📅 23:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106692">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پنالتی برای بارسلونااااا</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106692" target="_blank">📅 23:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106691">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2a96773e1c.mp4?token=PoolVByt5jD9WoOocaA0vM5jSou6XEsKiVEZvEhRkpO0AlQPH8SjxXyr6TCsC2rV5ZiVCgk4296ZP39EWK8MiR7G6UbIAiRg-VUKoGByGHBJHTXfDj4et-1fH6WuMNe4s8wdkJBgFflHezmQbgDsX7DetWn6Ebn-pQa_BUDPo3qGIvkG-K0GQ2GQWU3KfBHcnyWDivmEFSY_1T-2TKwa6thVRqAGYYAHrUpdnq92W1lRWEBMubjOkqVhSClyoP5Eal9V74TZ9Ms-1WcxjV3ABchKyou2lF0SFTstRkg8BNtnNjp6YCuDqNJiwad_DmGrvv_ZDDtPCKWa4u497rJLqTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2a96773e1c.mp4?token=PoolVByt5jD9WoOocaA0vM5jSou6XEsKiVEZvEhRkpO0AlQPH8SjxXyr6TCsC2rV5ZiVCgk4296ZP39EWK8MiR7G6UbIAiRg-VUKoGByGHBJHTXfDj4et-1fH6WuMNe4s8wdkJBgFflHezmQbgDsX7DetWn6Ebn-pQa_BUDPo3qGIvkG-K0GQ2GQWU3KfBHcnyWDivmEFSY_1T-2TKwa6thVRqAGYYAHrUpdnq92W1lRWEBMubjOkqVhSClyoP5Eal9V74TZ9Ms-1WcxjV3ABchKyou2lF0SFTstRkg8BNtnNjp6YCuDqNJiwad_DmGrvv_ZDDtPCKWa4u497rJLqTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
سوپرگل اول بارسلونا به ریسینگ توسط کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106691" target="_blank">📅 23:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106690">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayR4LEAySbhDXZWryVolP13Xs41Gv6xxyigOUZi6c8ge1TMwMdy4vgg8H0RzXBLSj-t0l_pP26kg5YXL1pZZnA53VGNEuVMGyQs3fOz_DM9PiVHy-ozs4wp7ponQKkxpywbb7KoOjAYK4GwBLOz-YR6fmm3GD4BRQ3mxMdv8H58T3a9AbKUEx02vRR8GlVp8RK1_gjcxTNk3q2RmB8TyqbpntQLu6LVFhr_S8R7cCE1l4hFOpDy2Zs3w59yTJQhlf1gsDMf8t8muTmPq0aWV6ThZLDvFg1rqw80BOAjJxdsIphkFxjQgrZQSR6kt8gSnEqLd3Q41zH77rypjkvhGjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شماتیک ترکیب بارسلونا مقابل ریسنیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106690" target="_blank">📅 22:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106689">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCEaKuNMDWcWIQToRvBHLSdg7GICsSN0pS6Y5AJ2o1w_pq3odeWjWMQ5Ohy6goigOTaeSlYuAOp-D2TBOz_mgDOKWkR9lqsHqmDNeCh2Gl3AoJsOWWEyMZaOSFJM7qeU-Gatl3CCVLdBa9RRFG051ywuQvzefB3jnPLv-67rCqubAFYaDgZl7U708FgEE261LmHqMBqMXd4s2tyJ5zN89sKBsLqkx3xh12fhcmJPJNAOqgkdbABcgWGag1HWXOaCcH7RHNg8rEd9LJiL9g-gXVINkFVfT5pqNyuTuu3BtbhDgoGphLlDWM3zbw_OVdoPb3QuX57-FHduLC9U8G4bRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇮🇹
🇵🇹
لیگ‌اروپا؛ ترکیب میلان و بنفیکا
⏰
ساعت 22:30 شبکه ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106689" target="_blank">📅 21:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106688">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e46b13203.mp4?token=gmtRbKlWLDSsZolzNVnr_cjA6SZfN4BpWKpz6awm4qnvbvw4pzSwZk_qoAHZEHA6XUD-kbAv3GPEb8N3jM6caZrGUxZ9A4BHS3Ng9Qpwf5mbhzeol6g2MLgWOXbqDMc4nlUeLW288WEC6vbzFFEdBpYI3QTRM67SJ-GEJoypn-SunaTeTzFR1ycftFOynuLMaecXYoJY7TR3x7mgNJ9oMc1VV39Z-pIIWLqydzcXYPE_atqus-MelmWSQvsufb3Uihb5T1ZL2daKFTPlJgy9lp_rOe_NPuxe00T96BMRMWpr0S6piSazVeP5IqOEgayKqboaxJ-qmGZivuXqmfeBag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e46b13203.mp4?token=gmtRbKlWLDSsZolzNVnr_cjA6SZfN4BpWKpz6awm4qnvbvw4pzSwZk_qoAHZEHA6XUD-kbAv3GPEb8N3jM6caZrGUxZ9A4BHS3Ng9Qpwf5mbhzeol6g2MLgWOXbqDMc4nlUeLW288WEC6vbzFFEdBpYI3QTRM67SJ-GEJoypn-SunaTeTzFR1ycftFOynuLMaecXYoJY7TR3x7mgNJ9oMc1VV39Z-pIIWLqydzcXYPE_atqus-MelmWSQvsufb3Uihb5T1ZL2daKFTPlJgy9lp_rOe_NPuxe00T96BMRMWpr0S6piSazVeP5IqOEgayKqboaxJ-qmGZivuXqmfeBag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
همین حرکت دیشب رونالدو که
کیرشو
میگیره، تو ایران خیلی وقته توسط بازیکنان انجام میشه
‼️
پ‌ن: واکنش رونالدو به شعار دیشب العینی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106688" target="_blank">📅 21:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106687">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2943ca3183.mp4?token=XcYzOE5owmskFVgRKd3cVDCOwOCo7kwr4b0Mj9q7qK3aF-BChPfwjGizRT8neIxtlt6vB7Oktxl5eGdRjYgkwzFAph-pb1HvUbo8OBmRkm9WfIyVrIcBXgkIKiBSFTUOSoTsX16gqvJ_1GD8SfozYnszGdWKgJlh9TstmvsrBnowtlDbozlMYIJOftp4bTu-x7zOt9daMKLqb37TCjvJ3ZV3qpV8Xn8OlG-38sCLwCXldkwaKEtg4ZO66aF0hU6O6_lQMeQW7mRVv_xgRTxbIllqjpZm2w01PH7VKJ9MM84w2TqLhm3BXyQ8j84kLwNf9ErM9KOvkPskMSTkQABM_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2943ca3183.mp4?token=XcYzOE5owmskFVgRKd3cVDCOwOCo7kwr4b0Mj9q7qK3aF-BChPfwjGizRT8neIxtlt6vB7Oktxl5eGdRjYgkwzFAph-pb1HvUbo8OBmRkm9WfIyVrIcBXgkIKiBSFTUOSoTsX16gqvJ_1GD8SfozYnszGdWKgJlh9TstmvsrBnowtlDbozlMYIJOftp4bTu-x7zOt9daMKLqb37TCjvJ3ZV3qpV8Xn8OlG-38sCLwCXldkwaKEtg4ZO66aF0hU6O6_lQMeQW7mRVv_xgRTxbIllqjpZm2w01PH7VKJ9MM84w2TqLhm3BXyQ8j84kLwNf9ErM9KOvkPskMSTkQABM_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول اتلتیکومادرید به اوساسونا(جاناتان دیوید)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106687" target="_blank">📅 21:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106686">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f3f55505.mp4?token=cK9XfjnXHRxz3az8rPPVm6WfxmvYRBn1JhWdeC4ocrCkPVEeMPIsXHhYlf75lZLYTqZtxiGfj7Oi4xUTZsxVca5i0xDSpDXEaSPkKrtUtRt42yzyDyY883-f8qG5grM0xWxqR6MdoZvV2ma32pWw_c4H4d3D63WqXHs2m-J3Ic28z0N4LqKOh5fwm6hV3j3lsD8nBb12FEbeUvOPE8dsuUTuPOoEIa-GLjF5zMZzxpnGZpPpSZ_zRXPHrfHAFWsTtvMeoJWyfCRypgbHv1BDQ3xlqdtpZCivvJXiHP-cY5dzPouUWYKgl3JdLhR8dJe-zGnVSomnAXWY_e7kh8SZ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f3f55505.mp4?token=cK9XfjnXHRxz3az8rPPVm6WfxmvYRBn1JhWdeC4ocrCkPVEeMPIsXHhYlf75lZLYTqZtxiGfj7Oi4xUTZsxVca5i0xDSpDXEaSPkKrtUtRt42yzyDyY883-f8qG5grM0xWxqR6MdoZvV2ma32pWw_c4H4d3D63WqXHs2m-J3Ic28z0N4LqKOh5fwm6hV3j3lsD8nBb12FEbeUvOPE8dsuUTuPOoEIa-GLjF5zMZzxpnGZpPpSZ_zRXPHrfHAFWsTtvMeoJWyfCRypgbHv1BDQ3xlqdtpZCivvJXiHP-cY5dzPouUWYKgl3JdLhR8dJe-zGnVSomnAXWY_e7kh8SZ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شنیدنی و جالب علیرضا مرزبان درباره زنده‌یاد سحر خدایاری یا همان دختر آبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106686" target="_blank">📅 20:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106685">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f63c731d.mp4?token=MQToTnjHsir4meya3mlVB_GH1HU5_DOvi3sM7i8ab8ARzK8FbtVo2OCLcfOSW1kpO6tP05sxQs0P88A6BkqIGcBHw4fv1VYvuUDFd4zLXFI-_e7L1ZocGNgceXoc1ntWyMeQnLjMlbh_XxW1MmpoeO6VytdctcmLaG1zsTYu5u3YF8xpJwSgOuD-551vK0dHB0cHmyUB8lHw69HgzF2SAfWW3zEIWFgWTq45VmJlt84qO0adxWHE5zXYkFKYV4nM32_auTmv8vXuJ4KhpdMaOYt_eUBUeaIAzPo9ZPjTa5cBUOPZPhbB8gBxQxnAoWAs-_mRQ0Ip7dLrLxcefasP3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f63c731d.mp4?token=MQToTnjHsir4meya3mlVB_GH1HU5_DOvi3sM7i8ab8ARzK8FbtVo2OCLcfOSW1kpO6tP05sxQs0P88A6BkqIGcBHw4fv1VYvuUDFd4zLXFI-_e7L1ZocGNgceXoc1ntWyMeQnLjMlbh_XxW1MmpoeO6VytdctcmLaG1zsTYu5u3YF8xpJwSgOuD-551vK0dHB0cHmyUB8lHw69HgzF2SAfWW3zEIWFgWTq45VmJlt84qO0adxWHE5zXYkFKYV4nM32_auTmv8vXuJ4KhpdMaOYt_eUBUeaIAzPo9ZPjTa5cBUOPZPhbB8gBxQxnAoWAs-_mRQ0Ip7dLrLxcefasP3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📊
ترکیب‌رویایی قلیچ پیشکسوت فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106685" target="_blank">📅 19:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106684">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bac1a39777.mp4?token=lVKCIjQ97k_aOZR4Ldux6rkIM1jPlM3Kp8frjH0Bq0bPyGpt2p7yV_SfWqhBJ0z0MGTuJRQk6rea3y4Qts6Cm_SRx31qfBeydN0QMbQmWaUtrDMS2QuRGo5stfez8OyYGCoy70D_6xZDJI9GWtU-CRjGWSSG6Hsd8IAYTaW8mTaLr1cnlGS6i7uAeZlGOYdfIWLqejcaw3InczQlcvmtTqqfEs1Sgh8YmYlu_C6Uu3ic_GlYdANUkoEYAwy8_oSog5MI2DUpQCwDa4uoqmUASZ-LMjNLh879_mfr0qk2CjXkDKNrUHnV9FJu0Huy9LAEQFeJF63MCMd0zISuSKfyRivUTWwNTAbNBCDgUlg9Z8A9ybMeuj6QGkS9lmFj_2q54Uzv3Yqx2gaZCGrKlbFbxysW4oQyWjw5AZBNTHrzFVs5jPB62nP-V9Hhvr7yOUe_fUjvqnZTUP31KYWLA2GS0IK8SxI4iEftIEYTHg2CXg7yjnK7-LIdNtHZIZe_p6jnnkoyCUBpq2nu0Bk6W4i7G-KEwRhsy5g6a8x4airz6HfCEvUA8GUw12P_RPOWNL_c2ZTILVM2GZvwkjGchq_D22Vaqx2AoDhCSiVRkFWK2jE4Qrh2xEh5-OBBYNMgd6HGev4y5U1DMLEiD79ImWM6jLtDytkU5qHfeOHRskepj1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bac1a39777.mp4?token=lVKCIjQ97k_aOZR4Ldux6rkIM1jPlM3Kp8frjH0Bq0bPyGpt2p7yV_SfWqhBJ0z0MGTuJRQk6rea3y4Qts6Cm_SRx31qfBeydN0QMbQmWaUtrDMS2QuRGo5stfez8OyYGCoy70D_6xZDJI9GWtU-CRjGWSSG6Hsd8IAYTaW8mTaLr1cnlGS6i7uAeZlGOYdfIWLqejcaw3InczQlcvmtTqqfEs1Sgh8YmYlu_C6Uu3ic_GlYdANUkoEYAwy8_oSog5MI2DUpQCwDa4uoqmUASZ-LMjNLh879_mfr0qk2CjXkDKNrUHnV9FJu0Huy9LAEQFeJF63MCMd0zISuSKfyRivUTWwNTAbNBCDgUlg9Z8A9ybMeuj6QGkS9lmFj_2q54Uzv3Yqx2gaZCGrKlbFbxysW4oQyWjw5AZBNTHrzFVs5jPB62nP-V9Hhvr7yOUe_fUjvqnZTUP31KYWLA2GS0IK8SxI4iEftIEYTHg2CXg7yjnK7-LIdNtHZIZe_p6jnnkoyCUBpq2nu0Bk6W4i7G-KEwRhsy5g6a8x4airz6HfCEvUA8GUw12P_RPOWNL_c2ZTILVM2GZvwkjGchq_D22Vaqx2AoDhCSiVRkFWK2jE4Qrh2xEh5-OBBYNMgd6HGev4y5U1DMLEiD79ImWM6jLtDytkU5qHfeOHRskepj1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
🇮🇷
سورپرایز تاکتیکی سهراب بختیاری‌زاده؛ استقلال چطور السد را زمین‌گیر کرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106684" target="_blank">📅 19:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106683">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be6891deda.mp4?token=kVUIYD2Sfozh4uAf1Gg09wQVRnQFYN7gV1zzwarKvQ01RVeU17XGjhvQoXJaZsay69jZRKNrrfR1zg-3e3HwMho5w8qVYmfXb_M49LSc3mX330VGVn8rhy6Yrv_KGQfZHSRhiGAd-3EVwkjUHM6iJrGi9CRKf-kFIWlXy99jarLaqIGgdoHy9kcXaoHgCPyy7lnG1zkNC7FoyQS78DvD_FDPGpcAeio51n5yDKmubST6xQOtxA_ZuTT2Vx2BsrSH80zmunLMT8oy9ZSRBK66YiMrkZdWwpWre0yNR9DutnhocjOQ5nmtAY36mIFNL2dac-_zCAlR5UUPVUTTR98VfrezeebFio7UXa2WCqX0bjv0BrMp1Mc2uuK9gtCdhvq-GmBtzbcQiA3XIfcrulsjoWgM3jpttgWGEzcBOQv2_QS32pQEmCHj4yFiCdPgZL72O93isV8WL140kOIyqqQVrsb5TiFMKmgCR8T8LHBKa3Fz9r7qenVxpUXY2RaJOmO81x-4w6klLh45M9Y0_EUPQhLLXL4S8OPgHKMI9wYfczE8Fsapl_xUjKQo9ujqAIVN142tBWHbxbyrttcy9WZY_Za9_IhskdtPpChJhR6mmQfoexvn8EXdQ-rVxuEq-vUOpCHLjONupyq0DxOXmRLVkGY4kzQfcupeCX032RW5DkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be6891deda.mp4?token=kVUIYD2Sfozh4uAf1Gg09wQVRnQFYN7gV1zzwarKvQ01RVeU17XGjhvQoXJaZsay69jZRKNrrfR1zg-3e3HwMho5w8qVYmfXb_M49LSc3mX330VGVn8rhy6Yrv_KGQfZHSRhiGAd-3EVwkjUHM6iJrGi9CRKf-kFIWlXy99jarLaqIGgdoHy9kcXaoHgCPyy7lnG1zkNC7FoyQS78DvD_FDPGpcAeio51n5yDKmubST6xQOtxA_ZuTT2Vx2BsrSH80zmunLMT8oy9ZSRBK66YiMrkZdWwpWre0yNR9DutnhocjOQ5nmtAY36mIFNL2dac-_zCAlR5UUPVUTTR98VfrezeebFio7UXa2WCqX0bjv0BrMp1Mc2uuK9gtCdhvq-GmBtzbcQiA3XIfcrulsjoWgM3jpttgWGEzcBOQv2_QS32pQEmCHj4yFiCdPgZL72O93isV8WL140kOIyqqQVrsb5TiFMKmgCR8T8LHBKa3Fz9r7qenVxpUXY2RaJOmO81x-4w6klLh45M9Y0_EUPQhLLXL4S8OPgHKMI9wYfczE8Fsapl_xUjKQo9ujqAIVN142tBWHbxbyrttcy9WZY_Za9_IhskdtPpChJhR6mmQfoexvn8EXdQ-rVxuEq-vUOpCHLjONupyq0DxOXmRLVkGY4kzQfcupeCX032RW5DkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚪️
توضیحات مجتبی‌پوربخش درباره فساد ۶ عضو ارشد فدراسیون فوتبال جمهوری اسلامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106683" target="_blank">📅 18:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106682">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83fb9dbe46.mp4?token=Fr6pRAGcF1D0okJ7YQqHoK3DxV70bAv8sCGpFTtd6JoCQYxvSYl0afquZ9MPoRfDYWe7BbZBlexNB1Yi2F1924485ICFFNqE9ZIFUUO5AAuSbZ0rr1EashpexbJS4cCVVWnKuOAX7zcjX9h032xYEWD58FIrvKW6Kt04xEgqOdubV3W0TiluW5iM6rNEHXCLpm1qavqTVczcOMOmjQC50JhnW0kToF3M6Gniu8nBKXiw2c1HR16XPtXj3NKbhotXRv_ddPA7vszls-b3Ajas4DU1ajlgNE01mQz7zbj2Wt4rgrp1lmBaUuHTsI5DTVa1phuVU7UAXadDPF1Mpa2Z0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83fb9dbe46.mp4?token=Fr6pRAGcF1D0okJ7YQqHoK3DxV70bAv8sCGpFTtd6JoCQYxvSYl0afquZ9MPoRfDYWe7BbZBlexNB1Yi2F1924485ICFFNqE9ZIFUUO5AAuSbZ0rr1EashpexbJS4cCVVWnKuOAX7zcjX9h032xYEWD58FIrvKW6Kt04xEgqOdubV3W0TiluW5iM6rNEHXCLpm1qavqTVczcOMOmjQC50JhnW0kToF3M6Gniu8nBKXiw2c1HR16XPtXj3NKbhotXRv_ddPA7vszls-b3Ajas4DU1ajlgNE01mQz7zbj2Wt4rgrp1lmBaUuHTsI5DTVa1phuVU7UAXadDPF1Mpa2Z0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
قائم‌پناه، معاون پزشکیان: اگر بنزین را ۸۰ هزار تومان کنیم، می‌توانیم به هر نفر ۷ میلیون یارانه بدهیم!
❌
پ‌ن: ۳۰۰ تومن یارانه دادید، از ۳۰۰ جای ما دراومد، برای ۷ میلیون چه بلایی سر ما میاد ...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106682" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106681">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106681" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106681" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106680">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqCc7aX29mdBWpCFswGSJNy6SuZegjbpCG23n897y9lgvwXvndmccDANszfBZMPbjRgLdx-d9M_iSY-b6coWrMEF3llVULvSkrJb8raHiIjbNrM_W-mqnnc6xSc5t2HfTGGh-vxeupUcIWt-IVb_rJGLYZ-42y5AVQQCD33rMBHFX51uRfAGhtgKd_EB-pPJKU7hh285NeDOvH5vZt7-O8IUBN942F6nubsgtYzO9PCseYv3irkMZqAx4OSUDBY2Yo32186w6O7ZvxuWaXUZmCiIxuLZAP29l35088sW9qyO5ldKKSkVcSsjkd461cw0JfO7Ix6NHm87h-ab5T0PBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
راسینگ سانتاندر
🆚
بارسلونا
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
راسینگ سانتاندر: ۲ برد، ۲ تساوی، ۲ شکست و ۹ گل زده
⚽️
بارسلونا: ۵ برد و ۲۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106680" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106679">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKaZlNDLcx9k17CYJvPi7i38_YEbIYgnrsoPIWKC62aSOnWNbAkdJOaIi69mH2AdJlZxgoMaPspH_3W1ordrFTtJNTbNX9lihOO6OrLDC3ZcjzRX1KUgSCxyk1F1ObUbCjbHtQnIfyPurrfbF0ISuHVtL0mI1ZiExi-4F8vFIJ2TKemQEFs2w_PmUsfs7m3JKya4zP53k-sk1fq8AMceXA0suV-jWZrZEHt_4QxqvVf-_DKr7WdnO7Oaxm0v-Wq33zFsOUpAYW91rrC8pSF3DmgHflGj7G0tQkHfKex_VTLDvw2OixdPnfj7EdPLOrCHdMx9aDroNC03uY9lZE1R0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اعلام زمان‌برگزاری سوپرکاپ اسپانیا
نیمه‌نهایی: ۱۳ و ۱۴ بهمن(۲ و ۳ فوریه)
فینال: شنبه ۱۷ بهمن(۶ فوریه) در استانبول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106679" target="_blank">📅 17:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106678">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVlBGFpNGAZ5pEs5WSruH6lCcEFrD5Oxkw1GyWHfcHcUGalqKgcP0RV_vHx3vtQN0uzpGXMCw5XSaHsZOgZEvdGe4R_B8ShL3i6RLjdNoJmRSf4HuVVAJjXPefS9KeBGx72Ikuf5uZY7lqAwUCCrMIFlUXxEWIWwzPRhn4RxtmheviKuy_VY2pLH_Uirs66cwdXdhxrUW3cfWwhRRk-zLKLcqnRvai6V29ytjtF1RoDdyhD4lW0C7qgh6M-bXnpdVhugMUPQGMq485JtkFRWW0VOJISAe9jEoFTANH6q0roYNsoGQ0cK8f_TPAein3XvANKcMbXnT6D5vmHFPkhAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مقایسه افتخارات ۵ نامزد اصلی توپ‌طلا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106678" target="_blank">📅 17:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106677">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15009e843d.mp4?token=YFKZhqQnosnzmQQBXg2O5CLXgJR665R9zayYfyomvrQxQWFV8P4HAxHFOa-bGeEjDjD5XoMo3_pwIltM-1lmercv2D_DWp519UhHhGppe9BjC-lkiPdI0yKVw38l6x--jenubqriEc2FmmJqRR8KEHiIOuGpM7ylI2sdAota3b2mWtNaqbM5TXKdxFm46oXjbncicWsN_CAxdfiQzc0CUQ8v2XqP54czFMOmSkSD_0TOiEns3nDwuyX76_tNRU-FSHhG3iUcSMukX1RI_b4JdgJY0tM_7ulVF0ShowIrXBrDnoAC_aqegLeSGpGBjJ0WArkca6tAqeDD--1i0jzeMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15009e843d.mp4?token=YFKZhqQnosnzmQQBXg2O5CLXgJR665R9zayYfyomvrQxQWFV8P4HAxHFOa-bGeEjDjD5XoMo3_pwIltM-1lmercv2D_DWp519UhHhGppe9BjC-lkiPdI0yKVw38l6x--jenubqriEc2FmmJqRR8KEHiIOuGpM7ylI2sdAota3b2mWtNaqbM5TXKdxFm46oXjbncicWsN_CAxdfiQzc0CUQ8v2XqP54czFMOmSkSD_0TOiEns3nDwuyX76_tNRU-FSHhG3iUcSMukX1RI_b4JdgJY0tM_7ulVF0ShowIrXBrDnoAC_aqegLeSGpGBjJ0WArkca6tAqeDD--1i0jzeMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
واکنش دیشب رونالدو به تشویق لیونل‌مسی در ورزشگاه العین امارات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106677" target="_blank">📅 17:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106676">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268cfcdc63.mp4?token=nyWVofO6FROmDg6tpYLsLMF3GKhqYY6SYK6R79mC0K9h_opBPNecCj5wrHYkqHUzxFP8S5PsYoxmYEwwP43a2D2FKL2mFRMWU1-7RbM0LCPq6t_cmOZaPneOIsjEY-FUHGylrncja4qdVjJN4TwT9r9IQ44PmaIE72x0rEalI5bt0wpYRnDIuBgl6rFeDp1UEpDG_N2YW5BmOhWC2SmjGcmBemGHCZgacj8SN1pdltZ4Qy3JCDKLgI0lQGqwZloaTLdQzVH6xWkhHRsAKqiHSBSHH6LN6yZITfR28omc95BV4qnZ7e3Fe3rg-ZrrzQ2WO8r27IysowC_QAHQjr2Clw96SWPh2adfwUtre9YjVlaCwRMoqkdVAozDUB4UOAOZxN9P3ZI6ZM7Ckd81EBIeo_obH-RykQbRrt2NGGSbaDvJnjKtaZ2iuOouYL2LJfdGjVi0MNFE2rAGM5A5Qs275r8po8_shBN3khCGQwJnHJ2Nmx08tktMN-Ve7tw1aHP2GKggMnyEDWbKVEZnHU4RZJw1mNVxTE5nLdGRRWnc1EUdmO9smhicZRoxYbVCbtTTgG1n1k67z2wjXM_cxb6XHp1osMpXUeERjnvDSmLKwYyqFyWUip_j1tbzd1raYZEfNnBJaXQI0hQfFed-xACUG_39T4QDcKyH_1ceAiYEkIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268cfcdc63.mp4?token=nyWVofO6FROmDg6tpYLsLMF3GKhqYY6SYK6R79mC0K9h_opBPNecCj5wrHYkqHUzxFP8S5PsYoxmYEwwP43a2D2FKL2mFRMWU1-7RbM0LCPq6t_cmOZaPneOIsjEY-FUHGylrncja4qdVjJN4TwT9r9IQ44PmaIE72x0rEalI5bt0wpYRnDIuBgl6rFeDp1UEpDG_N2YW5BmOhWC2SmjGcmBemGHCZgacj8SN1pdltZ4Qy3JCDKLgI0lQGqwZloaTLdQzVH6xWkhHRsAKqiHSBSHH6LN6yZITfR28omc95BV4qnZ7e3Fe3rg-ZrrzQ2WO8r27IysowC_QAHQjr2Clw96SWPh2adfwUtre9YjVlaCwRMoqkdVAozDUB4UOAOZxN9P3ZI6ZM7Ckd81EBIeo_obH-RykQbRrt2NGGSbaDvJnjKtaZ2iuOouYL2LJfdGjVi0MNFE2rAGM5A5Qs275r8po8_shBN3khCGQwJnHJ2Nmx08tktMN-Ve7tw1aHP2GKggMnyEDWbKVEZnHU4RZJw1mNVxTE5nLdGRRWnc1EUdmO9smhicZRoxYbVCbtTTgG1n1k67z2wjXM_cxb6XHp1osMpXUeERjnvDSmLKwYyqFyWUip_j1tbzd1raYZEfNnBJaXQI0hQfFed-xACUG_39T4QDcKyH_1ceAiYEkIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
روایت مجتبی‌پوربخش از اعطای مجوز فوق‌العاده عجیب کشف معدن توسط فدراسیون کشتی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106676" target="_blank">📅 16:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106675">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d14f705b.mp4?token=jmvLv435hyuFicjTOisctJVym63_3LWgikVk_kkPJq2j9FhegL5eUy0zdtpkbDcTSDr8FPI1RwTUglPY-Nu5cMnWrZPPPILujcqHrt-d6oR3diFnejGio-lUvlMb4_tYRJ3AP7jziObIrRswUJ4hsFF4S3rVPFRg5zAjk1M1ixqgLsBtVyfXpIG8opZB-bcXv54i0KpzR-KKjb82je6CR1JoZBnVvEDJ1JQJoo5amN8A6g3r56Sk0ecbz4cL5QBbG3dRIPOQ3IXHjFR-cUPj7_g2BCAe_MwunzGHjO1rnW89xlWq0zbt_HO39OKqlnCvm3nKp4GGTEZ1Zu_A7b--rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d14f705b.mp4?token=jmvLv435hyuFicjTOisctJVym63_3LWgikVk_kkPJq2j9FhegL5eUy0zdtpkbDcTSDr8FPI1RwTUglPY-Nu5cMnWrZPPPILujcqHrt-d6oR3diFnejGio-lUvlMb4_tYRJ3AP7jziObIrRswUJ4hsFF4S3rVPFRg5zAjk1M1ixqgLsBtVyfXpIG8opZB-bcXv54i0KpzR-KKjb82je6CR1JoZBnVvEDJ1JQJoo5amN8A6g3r56Sk0ecbz4cL5QBbG3dRIPOQ3IXHjFR-cUPj7_g2BCAe_MwunzGHjO1rnW89xlWq0zbt_HO39OKqlnCvm3nKp4GGTEZ1Zu_A7b--rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل توتی در یک‌دیدار دوستانه در ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106675" target="_blank">📅 16:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106674">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE4e40ZMlzF-ae5C587XXWH_YT6Avmwfq1_1QiEuj6HvC_Tvd3IbzNj0JTG_UbWhc2VU1C_o9eO6pUtVfZ-bE016nAlQEp-xACxS5eSJtVJwY90vNw58GMbRfDAfZgeQ7SxHGVLeh2jFyllSQOTKCn-4MBCKsXRtr914-OAx76LZWaF6R1aZVME-ao0kpUWRdNvj-0hW0rgR9Iuf4buEVqUZg8PxzzreRSpu4m1MyznNtUKz_fTFpbTnN4IaMQBOXjhbSugZvV4_RO1QUgrLzSXgvAG5jBqHLVFq2qpdIkgFfvV_JIj2pC5RhaRbojGgl4EHniBSTZzGNNa_WuoOuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
مصدومیت حبیب فرعباسی سنگربان استقلال جدی نیست و این بازیکن به دیدار روز ۱۶ مهر مقابل تراکتور تبریز خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106674" target="_blank">📅 16:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106673">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bbacd491.mp4?token=VddpEtq94Xc70fjqQ1ubr8JMs5HFe2SWGfiOiaDtTr9pbCIRqytd57g_qJ61JJYAqPIc26X0mviTbBuwA09nPnAk6CVocriBHj28zI4Uitfm24Jbk6IxXikQZkQ2H-2fULiZqYdzs5BzT4D3chwjJskfWBCW7IrsXzWdnsyDb19bxi8Yevig5CrcMdsqn16XXL5Zz8QgTybX2-bpUNhni4JK7fM-d1LHfY7bo9MsdwGsY91OVuN7wNJkOmH_P0aKc7BVOKGf7kiBiM0SX4Az7Y6XoJv204_lf9UOwMjsSqDoUQxMsFUhtDlIw2aDWMRlXTh6OoeN_N-qSujxZCdsDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bbacd491.mp4?token=VddpEtq94Xc70fjqQ1ubr8JMs5HFe2SWGfiOiaDtTr9pbCIRqytd57g_qJ61JJYAqPIc26X0mviTbBuwA09nPnAk6CVocriBHj28zI4Uitfm24Jbk6IxXikQZkQ2H-2fULiZqYdzs5BzT4D3chwjJskfWBCW7IrsXzWdnsyDb19bxi8Yevig5CrcMdsqn16XXL5Zz8QgTybX2-bpUNhni4JK7fM-d1LHfY7bo9MsdwGsY91OVuN7wNJkOmH_P0aKc7BVOKGf7kiBiM0SX4Az7Y6XoJv204_lf9UOwMjsSqDoUQxMsFUhtDlIw2aDWMRlXTh6OoeN_N-qSujxZCdsDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
👀
صحبت‌های عجیب و بامزه پارتنر مهران مدیری در سریال مرد سه‌هزارچهره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106673" target="_blank">📅 16:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106672">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6760fc381b.mp4?token=FcqwL663wYBrYcWuY3s6cVVw3gznNolO8IViwuWCZc5so_vJkSwIUF2GK_tKZmmS70bJJDhULJXYjC216wbkPEMl6iQBxZLpFiER3xuO5U501aiMwsBeWIUqHc0hhSCoO8Co51fr3zx6y6m3HLY4fCjlqzuMb-xl-Qio36iMqIl3rEZ_z_7FekzGudoiW0HG9efNhPNifhVn1WVLpvb2ftu63dvaQWfiyLY0VMvGJzSwqzJq_N0GCl1N5JQ6ZcQ9dQcM8tzGw-RmsvH-fPz04cRrNQRjeHudUCW5CAiF1nF5LJpKyLbSy1ZiDCZERZC-Ye6AR8FapN51w1tzcKOeww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6760fc381b.mp4?token=FcqwL663wYBrYcWuY3s6cVVw3gznNolO8IViwuWCZc5so_vJkSwIUF2GK_tKZmmS70bJJDhULJXYjC216wbkPEMl6iQBxZLpFiER3xuO5U501aiMwsBeWIUqHc0hhSCoO8Co51fr3zx6y6m3HLY4fCjlqzuMb-xl-Qio36iMqIl3rEZ_z_7FekzGudoiW0HG9efNhPNifhVn1WVLpvb2ftu63dvaQWfiyLY0VMvGJzSwqzJq_N0GCl1N5JQ6ZcQ9dQcM8tzGw-RmsvH-fPz04cRrNQRjeHudUCW5CAiF1nF5LJpKyLbSy1ZiDCZERZC-Ye6AR8FapN51w1tzcKOeww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از استاد آریا بام رفیع دبیر زیست کنکور تو چند ساعت میلیونی ویو خورده و خیلی وایرال شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106672" target="_blank">📅 15:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106671">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4e1abcd1.mp4?token=bvlmcf5CphRrUq8SxZLjiqPOU5qck4_0PHqzlZnoZzyafCq24yZLcWnDAFMDS0SqnIdbRkE1kfTSbL6Nmj2sWP83ie1KRUss5wXiQulumWk_vqC5WkzQtC1wSRG8MMt5vfpmrO5T6K1fKt3yHJE0Q74MpgMQFg7-VvSYaaTVls3os6BDCluoCGWcvwcF0JV4i4bzcCKN1PhfBxlwISrG1Cdm3yvU2j4pfiCB6u5dLrSaOi1FdFtU3Fh01odEocS6WBx69lBQKqLvb-UXYRyi9GTG3Wgo-bKH9JujEMxNEKhNxYcBq6y7E4blBJTgIxB_UcOJIPrfGMGOw_bOupYDUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4e1abcd1.mp4?token=bvlmcf5CphRrUq8SxZLjiqPOU5qck4_0PHqzlZnoZzyafCq24yZLcWnDAFMDS0SqnIdbRkE1kfTSbL6Nmj2sWP83ie1KRUss5wXiQulumWk_vqC5WkzQtC1wSRG8MMt5vfpmrO5T6K1fKt3yHJE0Q74MpgMQFg7-VvSYaaTVls3os6BDCluoCGWcvwcF0JV4i4bzcCKN1PhfBxlwISrG1Cdm3yvU2j4pfiCB6u5dLrSaOi1FdFtU3Fh01odEocS6WBx69lBQKqLvb-UXYRyi9GTG3Wgo-bKH9JujEMxNEKhNxYcBq6y7E4blBJTgIxB_UcOJIPrfGMGOw_bOupYDUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
هانسی فلیک: چه به عنوان مربی، چه به عنوان هوادار بارسا، در فینال چمپیونزلیک ۲۰۲۹ که در نیوکمپ برگزار خواهد شد، حضور خواهم داشت.⁣
❗️
خبرنگار: لطفا به عنوان مربی ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106671" target="_blank">📅 15:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106670">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a617f5cf34.mp4?token=UMRkY8e4lyLe75mbKN_ESGgPsMzXPRSIfS4HI-MLBooRXBOVGCF44KAsD0ukM6qxaJuh4vLqdhHXEc-GYoUHgwf2iVHg3qK7AuvKI5RL4Bl4hB90bSLmtgQIm-rG4dsVPA75O30Y7t_PVKRamlJ9DkRsOJwGKq0oJCbgfRuqFfK3hj-cR4vS7IXv5tFggxf1f7r9R34WiJ_-ft2ZexXS9bduv_O7BsObuxuPm9RQH-3C5l-iau8K0jIMALCfk3Sqau3fWAALZ4dH5nz3siqnL9R79iv4SvPQBVX7UZPcuy6OXQPCA6jBz6JjOUadr2tqk8z7V7Gr25bFQm2NiXN-4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a617f5cf34.mp4?token=UMRkY8e4lyLe75mbKN_ESGgPsMzXPRSIfS4HI-MLBooRXBOVGCF44KAsD0ukM6qxaJuh4vLqdhHXEc-GYoUHgwf2iVHg3qK7AuvKI5RL4Bl4hB90bSLmtgQIm-rG4dsVPA75O30Y7t_PVKRamlJ9DkRsOJwGKq0oJCbgfRuqFfK3hj-cR4vS7IXv5tFggxf1f7r9R34WiJ_-ft2ZexXS9bduv_O7BsObuxuPm9RQH-3C5l-iau8K0jIMALCfk3Sqau3fWAALZ4dH5nz3siqnL9R79iv4SvPQBVX7UZPcuy6OXQPCA6jBz6JjOUadr2tqk8z7V7Gr25bFQm2NiXN-4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صحبت‌های هانی‌رامبد درباره ضررهای مصرف سیگار روی بدنسازی و عضله‌سازی؛ حتما تماشا کنید بسیار مفید و کاربردیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106670" target="_blank">📅 14:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106669">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4b40a7a1.mp4?token=e3Gd3WXFNFCtAGLcWA0KOJ6mI5prKxclQ_WpjNHQ2kQG6QK8B_Tru-hSeM5VzOf9wv7IgmjD9nMs7gcvWF2uM5Y_PYOQHWLWSjAI-GY8dIl93FE-LyZ74jyjUwmcJKCnIWllUT8Iua9QKDuQ8PLaZdTfvfsDZxJVZXeqAMbqIkCA6T6kAsYNjk5cN7tCQsX7VfkpYLtjAtL2o-CVWyMleSQ8777qpWwS-Fd356NKLCbNW-SHtiFUHWfzAlcKe_fpPgg5LeFdL0arJbFTQp7QUoG2ozBkkGJrifTE-2MrSZJpN_H94DPqKIVKGXfgmnXFtfrawYyAFR2EX9vn2txWujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4b40a7a1.mp4?token=e3Gd3WXFNFCtAGLcWA0KOJ6mI5prKxclQ_WpjNHQ2kQG6QK8B_Tru-hSeM5VzOf9wv7IgmjD9nMs7gcvWF2uM5Y_PYOQHWLWSjAI-GY8dIl93FE-LyZ74jyjUwmcJKCnIWllUT8Iua9QKDuQ8PLaZdTfvfsDZxJVZXeqAMbqIkCA6T6kAsYNjk5cN7tCQsX7VfkpYLtjAtL2o-CVWyMleSQ8777qpWwS-Fd356NKLCbNW-SHtiFUHWfzAlcKe_fpPgg5LeFdL0arJbFTQp7QUoG2ozBkkGJrifTE-2MrSZJpN_H94DPqKIVKGXfgmnXFtfrawYyAFR2EX9vn2txWujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇪🇺
🇪🇸
رودری: قهرمانی برای بارسا دست‌یافتنیه اما بارسلونا مدعی اصلی قهرمانی چمپیونزلیگ نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106669" target="_blank">📅 14:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106668">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8dcfc377.mp4?token=GL-ZgV-ssGnp8nJ_g1xr3TeqUWkgkUA0qdIqMhEtYhoCNUCMmyhBsRcVDpXdnouqnT9Hpdsu_M0eHtJHJZOEsgMrFy7psY09e4BRg6MHv-xlRjfLTTAZyF3mJE9vqlsOsQWxvS_1FFEs-4pqfUfZW-Ry1MJB1DpY5SJpu9hCg_FKDe1MWKM2qYpfecWDwRVTNfoGu9dby6RUR0EOQbCiDBTIwrcCle4ZDldht-UEND2OIIM947t_Uikdy8qn2Pl7L4bIPdcbZi7hGl9LzpUMbYFEX5qsLBBD5caFI5CKEmZzyW7Nn3FxBE14f8axMEvfE4w8dOw8tGb_Bxho49lARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8dcfc377.mp4?token=GL-ZgV-ssGnp8nJ_g1xr3TeqUWkgkUA0qdIqMhEtYhoCNUCMmyhBsRcVDpXdnouqnT9Hpdsu_M0eHtJHJZOEsgMrFy7psY09e4BRg6MHv-xlRjfLTTAZyF3mJE9vqlsOsQWxvS_1FFEs-4pqfUfZW-Ry1MJB1DpY5SJpu9hCg_FKDe1MWKM2qYpfecWDwRVTNfoGu9dby6RUR0EOQbCiDBTIwrcCle4ZDldht-UEND2OIIM947t_Uikdy8qn2Pl7L4bIPdcbZi7hGl9LzpUMbYFEX5qsLBBD5caFI5CKEmZzyW7Nn3FxBE14f8axMEvfE4w8dOw8tGb_Bxho49lARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
شوخی‌سمی رودیگر با تدارکات رئال‌مادرید در بازی دیشب مقابل الچه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106668" target="_blank">📅 14:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106667">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrVGw4mWFHqLvRJ6CGXiwil_MIQkTACs3545HiNCAaX_gp1FpJS1oW9blDHfTC0w90QZ-MHZxgHhqh01atlf1ysin3qIQoz6AspP1Rvw8geWSLtvtfAd_g3YMO1hk9YL5eeAnY0fBokSknn0XhocA8QcdpBid0rqCSYm2PR3o-xjXSM1fNG8RxvNT1RhlVEouDUSsLsrF9-Afm6aGqBHJI0PGzpj6Oxx765dYTRZpCCAYy_FgYC_JMX6oGllinYRNkC41GWO-wbkNT9d9UActGMYvMs5BOCcWjqoPnJk_a4UgP0x50yLigAwAJMKcL_fgJMn07NLasZa5Jf8TIOEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
لیدز یونایتد تنها تیمی بود که در میان تیم‌های میزبان هفته‌گذشته پریمیرلیگ، به پیروزی رسید. تیم‌هایی مانند لیورپول، تاتنهام، چلسی، منچستریونایتد و استون ویلا، و دیگر تیم‌ها، نتوانستند در خانه خود به پیروزی برسند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106667" target="_blank">📅 13:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106666">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d150b918d.mp4?token=o-k9cas1ZRgHXzcQajH1WjA-OW2nRbRPid2uryAbcYXfDpRDiNixpyfmwaCyHoQ-0WqQMTZky_kQBXtlkg3foUbBsULHvtgcF9reh8oL3hTwmG9nPDUcPR3IZmaWvBjPK8OK7YMMkY4ln41CVSXJfhr_SK_Btd47dxF4w0rvftLBIpcnoPwAsIocvz1DzRKvlBir41cOLbHEXxfXDDkw09KHGYfpeWniduUSNGHeCiQmdh1YSZlIILd58pqNYQ0JHQWmRM_ZFLQsm3gJE9ZdKijQ9Mb2BakMRyEYhd8fsyI8qUMZIp3GDUSfMt6d1CkCRBqJyj-IpFZLA-SaekEpFxuMIYJdRtm8k3BaUSz8T7iWsa8Bsu2tLrDiNAI79lJdp3pLux6LLxvjvslAd6WH1_Nl0lBI_Wiw6CP4b3iU5xR5ngBW7A-K853td9MIE8DTUefKjX8Q6vLMCt_96YVeWIBj6Eu5aFVAnqkOSoQJpwN7SwINVskEHZqtbVWHFD889YVFAsvK92rSFavGvxFNvvlbsn-dDzU5MZKqL8TO5X2jCajkXQ2znEnkW5X06HLKZHLQCwSz4IDCGNV7PSo5BmkQiVP1KfnfaqBXVcIHAlisUNMoM783VIRY_w1cWuUQstRDhpNDRjG5AamGBRq0fU-rLdnKkHx9naozLRRiAz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d150b918d.mp4?token=o-k9cas1ZRgHXzcQajH1WjA-OW2nRbRPid2uryAbcYXfDpRDiNixpyfmwaCyHoQ-0WqQMTZky_kQBXtlkg3foUbBsULHvtgcF9reh8oL3hTwmG9nPDUcPR3IZmaWvBjPK8OK7YMMkY4ln41CVSXJfhr_SK_Btd47dxF4w0rvftLBIpcnoPwAsIocvz1DzRKvlBir41cOLbHEXxfXDDkw09KHGYfpeWniduUSNGHeCiQmdh1YSZlIILd58pqNYQ0JHQWmRM_ZFLQsm3gJE9ZdKijQ9Mb2BakMRyEYhd8fsyI8qUMZIp3GDUSfMt6d1CkCRBqJyj-IpFZLA-SaekEpFxuMIYJdRtm8k3BaUSz8T7iWsa8Bsu2tLrDiNAI79lJdp3pLux6LLxvjvslAd6WH1_Nl0lBI_Wiw6CP4b3iU5xR5ngBW7A-K853td9MIE8DTUefKjX8Q6vLMCt_96YVeWIBj6Eu5aFVAnqkOSoQJpwN7SwINVskEHZqtbVWHFD889YVFAsvK92rSFavGvxFNvvlbsn-dDzU5MZKqL8TO5X2jCajkXQ2znEnkW5X06HLKZHLQCwSz4IDCGNV7PSo5BmkQiVP1KfnfaqBXVcIHAlisUNMoM783VIRY_w1cWuUQstRDhpNDRjG5AamGBRq0fU-rLdnKkHx9naozLRRiAz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇵🇹
عملکرد ضعیف اسطوره رونالدو جلو العین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106666" target="_blank">📅 13:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106665">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a01bac8019.mp4?token=rMTyxDnT9bAEmyyiDAKfJkixJhIsbUdkfZRAAoXxMX-4BIk92HzLVPDAZc7WY2aAaQcDv93rCxFRh5loQmiM0baG0qIVy2YCdgXYjU8_2iJjo0fr0K_DiwoEpPdpWWyW8fPlIyezx0m8023xa-CvNzf524ouVFey5h7jyLZVkm-oYbrjNyY6IXusmMBaqPFklOb22-WZIL77JHNcAYdRZFFdLD0GvzIhh5K49vaZ725O8r-9i0UruvaTjnqX5rWA_2ek55tiGO_y94PhghMbl6KzBlnnHyJvyTmyF8B6nVugEzgNTLVfcFSBoyxdVa2BXDW_KyMHGBPT5Y8J0ARb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a01bac8019.mp4?token=rMTyxDnT9bAEmyyiDAKfJkixJhIsbUdkfZRAAoXxMX-4BIk92HzLVPDAZc7WY2aAaQcDv93rCxFRh5loQmiM0baG0qIVy2YCdgXYjU8_2iJjo0fr0K_DiwoEpPdpWWyW8fPlIyezx0m8023xa-CvNzf524ouVFey5h7jyLZVkm-oYbrjNyY6IXusmMBaqPFklOb22-WZIL77JHNcAYdRZFFdLD0GvzIhh5K49vaZ725O8r-9i0UruvaTjnqX5rWA_2ek55tiGO_y94PhghMbl6KzBlnnHyJvyTmyF8B6nVugEzgNTLVfcFSBoyxdVa2BXDW_KyMHGBPT5Y8J0ARb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار از علیرضا منصوریان میپرسه چون الطلبه مشکلات مالی داره این باشگاه رو ترک میکنی؟ اونم در جواب میگه: اگه تو این روز سخت تیم رو تنها بزارم کم لطفیه و امید هوادارا به منه و نا امیدشون نمیکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106665" target="_blank">📅 13:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106664">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfbc375b35.mp4?token=mwEMnvbC5wid038tJv6U9CMJH8K_F9m7lu2xP1vrIOXGfKW739UqRp_Lfcx_2VWZ6pM5yDhlDYsbpjroZhnYLRiTKCl9M3laCjlinwFGBIRACevANyZ0xKkv3D5fnDdNsHFBWAi17z4R4a7VuQYmQblyA1xADiFFqL_SZl21uy3asX8a25sxIvhRxF0WxTFNGi0QVBqAXAx9vhMhsSgReuT_RcqH2sp0jW-yGyqCGDdgGpsa4lyno4qOZnQ_IJjVZD96zsNZVNfEIWpeqcg9NM3eAWENp40GBmYDYGphjWck_2WU5nAHLnfBkhATo9y2zBN7xd2RO_a03sc1YQlAAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfbc375b35.mp4?token=mwEMnvbC5wid038tJv6U9CMJH8K_F9m7lu2xP1vrIOXGfKW739UqRp_Lfcx_2VWZ6pM5yDhlDYsbpjroZhnYLRiTKCl9M3laCjlinwFGBIRACevANyZ0xKkv3D5fnDdNsHFBWAi17z4R4a7VuQYmQblyA1xADiFFqL_SZl21uy3asX8a25sxIvhRxF0WxTFNGi0QVBqAXAx9vhMhsSgReuT_RcqH2sp0jW-yGyqCGDdgGpsa4lyno4qOZnQ_IJjVZD96zsNZVNfEIWpeqcg9NM3eAWENp40GBmYDYGphjWck_2WU5nAHLnfBkhATo9y2zBN7xd2RO_a03sc1YQlAAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇪
🇸🇦
هیجان‌بالای گزارشگر خانوم استادیوم هزا‌بن‌زاید العین امارات در بازی دیشب مقابل النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106664" target="_blank">📅 12:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106663">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e050d24ce.mp4?token=cu39ckg12F7WUS2Q1BcikBMlzO_n4R3vDnW_Pw2XWaBjLB27jxEUG_3yJNuhm9uyrSSTrEo7u7XiCFTjYHFxkrl9BJpq0kxW2ktHZ8R7rnFfvyubxNM2qEgM81Eh7Smf8pvYYY9Y3RbxIf3MA8D1lfSYPEb8WIE34agkmEnHnnL95sc77r65xA6LBJwrwE0UBkU7Es0LHLjWM5SJW0GS8-2q1TYRbdSpuDmisnZdL44Htj_NZ7fMtY4wYaESSXUmjWxtTe0tC3dDLHW1r3g5adc44zhArfS8mJCil9JwLZhho53Wi5k8PB1ehKncEtq0totFgTEQF16a_JtAKh8j7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e050d24ce.mp4?token=cu39ckg12F7WUS2Q1BcikBMlzO_n4R3vDnW_Pw2XWaBjLB27jxEUG_3yJNuhm9uyrSSTrEo7u7XiCFTjYHFxkrl9BJpq0kxW2ktHZ8R7rnFfvyubxNM2qEgM81Eh7Smf8pvYYY9Y3RbxIf3MA8D1lfSYPEb8WIE34agkmEnHnnL95sc77r65xA6LBJwrwE0UBkU7Es0LHLjWM5SJW0GS8-2q1TYRbdSpuDmisnZdL44Htj_NZ7fMtY4wYaESSXUmjWxtTe0tC3dDLHW1r3g5adc44zhArfS8mJCil9JwLZhho53Wi5k8PB1ehKncEtq0totFgTEQF16a_JtAKh8j7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
✅
قبل از ترک باشگاه چه‌کاری مهمه که انجام بدیم؟ برای دوستان بدنساز‌تون حتما بفرستید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106663" target="_blank">📅 12:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106661">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZz9yEZvlMB3WW_OH244nuBfohlxZS5opO9x2T62qOFfr0y_W94HhFyFwycnMok9ycDk4jmh6lPYsBLbwBY7xK6_loxQXtM6_jP06QMh_oFsKWm6gaWrJWT0Ndr9tU6EhyTfq2lf-wFWEpVpYCY1j0bB49A55aQOjAlZ6Pionov2goND2av4gKPLsZo31OeJLLoK5IoomqvwzKVAncN4J7konO9mJI41MVjDsE5yd7aUTg880DzxK7l27w8Bsv8HEPToxVuVu7gaqX-jMiwn8_M1ul6r1v7qtNFJpEWlf1kzHv3-un8FmfP6P2MPcAEYusYwTHRiIop3QNVd7vPVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyiyiQ5qp3c4y7VSvMg03qXAHr1YqyORDrQG1XbwlSJfo5uJeSWa76QBhjyqbduxIINUJl0o1PuJxGsyDv9kVztkA23lZfOyagArzcavpaDw0Iu6XPbgSUxM8lFgR5OT5qd7wnXtgIgUvOgXNZ5J_XZ2at4-YW9q6v0ScJMaCR7HKsRJzqut2UwlpMK50TfqkxC5GsJypc-ntw4XdLVO50fyW8TrRdFTQ4aRQM5EKtKIrMlNu_USfNw5yyWY9NvywIogOKJQpYMnVcdzIW5BglmUo6_s7Q88xaXGmxcQrQt2W1PWtu-2EjPJIPNP3hbGoDPyeUNYY-W-NItH-uuJKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
عکس‌های جدید شکیرا در ششمین دهه زندگیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106661" target="_blank">📅 11:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106660">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
🇸🇦
🇶🇦
درگیری شدید دیشب بازی الهلال و الغرافه از این زاویه؛ بن‌ناصر بخاطر کشیدن موهای سامرویل کارت قرمز گرفت و جلو استقلال غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106660" target="_blank">📅 11:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106659">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106659" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106659" target="_blank">📅 11:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106658">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYvR3L2RWvhm2aoNmx1yYKg54tY3Qum7u_FpslK-IO6fZ4HNG0XWmEpDHvX8r2x0soFigYPowm0hf4AnAzb4FCZppIB1wrfvyAl0Rpos1SmkkcdoSW3_YbtSNkxO5ju4STUh20OKyip0lZIJjVUBCdiaVViR41gmePQdFp4aOG80OZCCaa-MVpcaKNXLb-0_C1kbaO8J2uYxEXZcT526xM7EdYboRJCKC-UHA7K0YnvO8ijCwTzt88x7SLQ9ZxmxdxHnp8sjdwNXCT6YWopcpIn_5jADyOCLWUMvYqzWgfDiuy61x1e1g4QPAH6mwkqD-JUJ54mTXoWebRlGvrGO2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
جدال جذاب لیگ اروپا!
نبرد هیجان انگیز
⚽️
بنفیکا
🆚
میلان
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل اخیر دو تیم:
⚽️
بنفیکا: ۵ برد و ۱۵ گل زده
⚽️
میلان: ۳ برد، ۲ تساوی و ۱۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106658" target="_blank">📅 11:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106657">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJKPo-9flcJkXSJ6VyGkJgBkTIAUc3msELOCDSYQc92brLRdQgr3seGu6pWaE9EMZ8T6i16pGUxbVweH5TOilEuLHmvbhkkbihHaF5kzxVf2VNFDE3DVKzFQzOflSNweSDqC-9nOK01rWQ-9bLTNRN1w6LS170afO1TJa0ALR4mTCpO_NNtHSHYXuwmOEt0fBXNeDNxTrTnQYDhmN_TEfTf5xgOLNC3yu0_HWAQ1rO-hHx1suM6zNrGDMVzRaiq3kbR57WhB6Wcu9L4RnBquaQNDisq0Lj2mVmpGgIPIEDT23fVAAyzTCoQJEYrPvUPvjxfcVMiV_lsnYQsQgdsCKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
📱
استوری اسماعیل قلی‌زاده بازیکن استقلال: من هازارد فوتبال آسیا هستم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106657" target="_blank">📅 11:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106656">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796caa8457.mp4?token=rLsiLqFV9EPI3C32xiVmQCdyh24fsmLvc3NPs0r95yhA2ukrPuep952sTgYuhBe-uXF8zSXyPgtmIQHkFhN7ELrLWm6rm9E6jRzMgLAbYw4x4a66Vmk204epxhV08sLxvanoLwt8a8pEkKQiszubsFRjmr1r0SNwEMwujYV2YNL4AznWfTvg6aVA86XGJCK-gUJREUQ41OcK6dctu72U89W76Z2GZYKT5DKf_tDU3WVe3ME-P626Od4sXBJdLj7yc9931UM6GE2fmGp5K6WPJcySPmaD9U-uzARc2GryWzMOGD3yeyRrDk-lMR6FMNEK3_yE_375unHtBPnWmWM-eLVxOy7rBEw0OrBsWUhCpHLDkZxSF7h-Ywah-_Tz8TbpPrTdYrEHjhFAXQyfVT6o03Fto3Pn31ofXSxvbxWnHeYnId9N0EZryKWRHVKEr9Jhdt3hLAhROqLcmFWsxhrtx043NeredUCTuUyTM8HIaPfrz3d-waOmzlTe2xeKkMUMhXb3M5isbPttwzI1WZQKjZF4OAMPGVHcdiVL5P95P87E9G6wMmzV7QgmqVuvKLZ-zpzLKQ1ZFDVrBp9y2zG889ISe3Thf2bpKYU02KfdUQ9ADV_KuqKbW4Q53-5SAtShKkVfaqWTKP0GAcyiherJktNqWd-84SlWVIGOO-O5mNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796caa8457.mp4?token=rLsiLqFV9EPI3C32xiVmQCdyh24fsmLvc3NPs0r95yhA2ukrPuep952sTgYuhBe-uXF8zSXyPgtmIQHkFhN7ELrLWm6rm9E6jRzMgLAbYw4x4a66Vmk204epxhV08sLxvanoLwt8a8pEkKQiszubsFRjmr1r0SNwEMwujYV2YNL4AznWfTvg6aVA86XGJCK-gUJREUQ41OcK6dctu72U89W76Z2GZYKT5DKf_tDU3WVe3ME-P626Od4sXBJdLj7yc9931UM6GE2fmGp5K6WPJcySPmaD9U-uzARc2GryWzMOGD3yeyRrDk-lMR6FMNEK3_yE_375unHtBPnWmWM-eLVxOy7rBEw0OrBsWUhCpHLDkZxSF7h-Ywah-_Tz8TbpPrTdYrEHjhFAXQyfVT6o03Fto3Pn31ofXSxvbxWnHeYnId9N0EZryKWRHVKEr9Jhdt3hLAhROqLcmFWsxhrtx043NeredUCTuUyTM8HIaPfrz3d-waOmzlTe2xeKkMUMhXb3M5isbPttwzI1WZQKjZF4OAMPGVHcdiVL5P95P87E9G6wMmzV7QgmqVuvKLZ-zpzLKQ1ZFDVrBp9y2zG889ISe3Thf2bpKYU02KfdUQ9ADV_KuqKbW4Q53-5SAtShKkVfaqWTKP0GAcyiherJktNqWd-84SlWVIGOO-O5mNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
برخی از زیباترین پاس‌گل‌های اسطوره CR7
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106656" target="_blank">📅 11:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106655">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc02fbddb0.mp4?token=myYIMUbw-O-ZT23Y3GVISzytydC67TUdvAMv2K6VowhTzbT-SxNtfa1PjN9xpVI__LekacZrPSdbEsXwOOBNNjLO4YUALNYZhCUC3TKwEcjPGci78IDoUP0nx_DedvKLh39nEiLyMiYnhDPrY5QZLgwNYWbgG1IHRJj0YAu0SCKgCMc-IStdAX4TNDzUdXOZV0S_KC-ehtY6Glu0YzD5w5EraHQVHFzud8h8m6S1hVw7rvVCWw4Ax98qnWFgJ1Y9ON81ihvB2vWGwQ9JswTidhu0mfbxIqMfI82xMvo8wI37uE-33ZqBpOWQ2TrijPfHpPneWAOLvU4r4v7lomYj3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc02fbddb0.mp4?token=myYIMUbw-O-ZT23Y3GVISzytydC67TUdvAMv2K6VowhTzbT-SxNtfa1PjN9xpVI__LekacZrPSdbEsXwOOBNNjLO4YUALNYZhCUC3TKwEcjPGci78IDoUP0nx_DedvKLh39nEiLyMiYnhDPrY5QZLgwNYWbgG1IHRJj0YAu0SCKgCMc-IStdAX4TNDzUdXOZV0S_KC-ehtY6Glu0YzD5w5EraHQVHFzud8h8m6S1hVw7rvVCWw4Ax98qnWFgJ1Y9ON81ihvB2vWGwQ9JswTidhu0mfbxIqMfI82xMvo8wI37uE-33ZqBpOWQ2TrijPfHpPneWAOLvU4r4v7lomYj3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
یهو هم دیدی سر توپ‌طلا غافلگیر شدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106655" target="_blank">📅 10:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106654">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=CFDW1-vfgwG16RichFW_Z1NWiLq6frVEvNPXXmln28DoDAscVBfFqphRxmxBMIGpJ8DBiukWDyfXWAjPykhSxD8cWteJ6drmERZ-g4cot5Huf2L_8kpvcgOrNdPvL0Oq6yvd3v3muKWDk0nLTtpP1b4aFw188FzZUJV5F6LrQ50GjI9SU7bs0BZamKmdCaeiWQr8SmDOv78hevqZRPsVYq4rfZOuOeij9Vg1vZ0B801JsBowSkryv4K-BCmpM--akQktjx-HGUrmFgzdbKpHZQec_aprLFT10euUsna2JgnL6OIEwFbDETGGDL5ODbpEEv9w3hprOd6LX5eBguneMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=CFDW1-vfgwG16RichFW_Z1NWiLq6frVEvNPXXmln28DoDAscVBfFqphRxmxBMIGpJ8DBiukWDyfXWAjPykhSxD8cWteJ6drmERZ-g4cot5Huf2L_8kpvcgOrNdPvL0Oq6yvd3v3muKWDk0nLTtpP1b4aFw188FzZUJV5F6LrQ50GjI9SU7bs0BZamKmdCaeiWQr8SmDOv78hevqZRPsVYq4rfZOuOeij9Vg1vZ0B801JsBowSkryv4K-BCmpM--akQktjx-HGUrmFgzdbKpHZQec_aprLFT10euUsna2JgnL6OIEwFbDETGGDL5ODbpEEv9w3hprOd6LX5eBguneMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل سوم ایران به امارات توسط مزرعه(89)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106654" target="_blank">📅 10:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106653">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679dc80276.mp4?token=LLwyPpbdLB34uCQJy654lyoUb4BO_gM-N8XXDlwjUIsJzBu_P4t5U680dAa-EvJ5A_Sp3swU7IUom4KKlXQb7iA6t7uLlIBHm7UPz0L9lfqfwKv0Hnd3bkXj1YZLzD9tY4CDes7S6b7G-1Q2uzRr_V3CXwHmAgHmCZMTHp5NoRvVdGX0gmdUdmslmF0L_Ibc1flevXUAdc_5-pHyJ3zotw2vDUPOCQ13mvEtG59iO9KHpEQDJmShTHSnxPjC2tiP_JrDcEAgA5eoGqVRr7IXgQLTQucMHeHxTkxY_YNXvhHKVQ9d6pASsOv3Qz9AzY2_NLZatPeqm0EoeQJR93AjLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679dc80276.mp4?token=LLwyPpbdLB34uCQJy654lyoUb4BO_gM-N8XXDlwjUIsJzBu_P4t5U680dAa-EvJ5A_Sp3swU7IUom4KKlXQb7iA6t7uLlIBHm7UPz0L9lfqfwKv0Hnd3bkXj1YZLzD9tY4CDes7S6b7G-1Q2uzRr_V3CXwHmAgHmCZMTHp5NoRvVdGX0gmdUdmslmF0L_Ibc1flevXUAdc_5-pHyJ3zotw2vDUPOCQ13mvEtG59iO9KHpEQDJmShTHSnxPjC2tiP_JrDcEAgA5eoGqVRr7IXgQLTQucMHeHxTkxY_YNXvhHKVQ9d6pASsOv3Qz9AzY2_NLZatPeqm0EoeQJR93AjLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🎙
انتقاد طرفدار همیشگی هادی چوپان از رفتار وی: درس خیابان با ساندو فرق دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106653" target="_blank">📅 10:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106652">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH5_GszFtDIbhZbJN0kJH0m7G_hopU2Lr0jdaHx1bYvtiIfqvnf7FF5VT1KeT_9z_MV67LB6oif5YkLms-YJpg22M6o_3NVTRDlNdQSFSTtJdxRFujG6SChRHiphoVOGGXcgU5bjbtOkKV3PbvZp0i5FRZaJ8b43scsfUiK-zRMO3yTO8JDgOLsiTq_hRu37G00Mh-9vVdh--kMcxXiGmCF8tS8XA59XEpBmlBGrhXUV0xiTGuzWC5Q1yc8QVZD6QhcSRnFliZ4-OsTiQowS8HoqAkUlCbQSnZsBl6oGuvXifhZCE3d6o3tsNVx4JRE68MLIRSfDuO7v7MwhRuTRGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
تفکیک گل های لامین در فصل های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106652" target="_blank">📅 10:03 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
