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
<img src="https://cdn5.telesco.pe/file/PR7HEnNfexSLnQAMZvN-2xy4IoABrpSMe3yAJY7tPm6wdlkTDWODgbJBa4-SYabZKT-vqnG1VXcTsYht7YCunyJ5ZOPq-BKGBKqflXqH8LqgbxoXayHnio_JTKaVV_08xBUvl8lyKmNI_5zt8qB510MdyIC2rWIhEwK8D_ftUFBhpUnB7l1-VeGDN369_TnfX4zZRHmbT4ve5gv3fOtLfnBmc4Cpr6OL5_0Dsqb6iuzGychrdCrMibk2Om6E8eE4UTR32BFDqmQ1PMLMA705dluSU37PYNmK8VxNOoO8Waf_WTOir4-82tmoMAGGQ9io_B30UBmqz_zpCa69chAZFQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 496K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 17:19:42</div>
<hr>

<div class="tg-post" id="msg-102688">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEcQH_1kIMaWcXts35wp1Nonx1l4RF_QnTn_AK23G9V7-E45vEebyMm0QvaJkZCZ9f_7ZfFODJ2gMLS7Z_X4Ivb19QeVYZhHgChYiOKWYlcSOpRxcfDfJc0YzzbERX48mrtTELsVhIZiNVmm_O542OQznhSApkE6p0dJkVe3crKJi2MzIxXy5XM_R6WSjCCYYikDMtiMSqY0_bog8dKJUc0_4v1kWwQijBJTLYzYl9z-HS6BTz-59SvUZBUMHh0bK2kEDmAHyNKuHRmt_Zi2x4AOxPTHARSqDq3sHdn0ENLQ0x8AWaPuvTah2X94hs4g1Pk4wxXA2jEJZ8g3Clz9cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
چلسی صدر جدول تیم های با بیشترین خریدهای بالای 100 میلیون یورو در تاریخ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 612 · <a href="https://t.me/Futball180TV/102688" target="_blank">📅 17:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102686">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAIedibtgAfqpuFnhbmI40DgrjsSPYU2XdI3QiUTYVDtZyc_IjUscdTXDh4HFVJhcWC8y5zCG49FZTRRvOAZ4kYwCP1HC8fsl0zv8d6vT1G5wvKqL84-bP7z8yeCYogrH7wsULPWAYVDfL12SjJhBjGpG46K2ndT0FN2GMj-7NuQEy0YhvmizHMOV50dUNFiqp7V39s6NCvkBNbW6z6nmuVjtbYe-q15KcS4YUq0Zvx2UrhYN8-3kF_Ol-t94sZ4q7zkh_zqakePlhLlV_Ntzl4FVRSRY-vJFNKX7N02Z2K86KSE723gzuEx2Oa1gMeKFQcb-yksofvyBuz0WcppwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7APQ9i1SCYeoLwn5uFJofVylrKUHAhDFKlcZ-9m00DDwljJiEVMkUmHUq0Rv8Nt8t_ej6YzHg4C9h5yJJSRfsJvoW-RldWOvgbpLo5Gesya_uN4UyR_ZFNJjAQ6IjlkXD3tAJpPsFVs2nlHaHSLeOWZaXqwb7gc2QntRA0JiIfZqHfRnvvaTgq6S02nKp973Wpszz1zRP2sSyAOmfHRMMVlLZPoPQ9MG8tbBlpss88puZVhcQkveAiZc_k4GDHhqnrFGTXAb_SfHNstOnmWRoOASvvz8znRt7gXA442x9tbOwSvJ9C5HsKzUVSsx8788oPTXsmx1485JrOfmlTnhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تغییرات رودریگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/102686" target="_blank">📅 17:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102685">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AceDAJz9KevIt_jqG7J5qMyC4bkHzsrPhPJp5-zBLv-DhbPLY8PwL2pUs04bD_1G0mTm40w26hsrBHdo6_1eN72_rplBaoK1dPhFs_x4Vsv8kqamQ3P06RM5DImNQZ_W8weli0fCw5SA7P1pDioxA35Bd9PsCIJiUX8MWu5DeJxyqatQ-VIpBUVsOREHzGCDBNxCwd6uhfEC25BgBT55NiOGMzLYEARBQBAXypCRcuFr4MZk1ATFJAAitTyKuz75IS2_y36M7UXgaqvRax5xfaFu6JSm0qO2xlPhHEQhOnrpu8dTmasBD6tGMSgH5pbVdJlHXhPpBJKzlth6SWyaZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
14 سال پیش همچین روزی؛ باشگاه یوونتوس پل پوگبا رو به صورت رایگان به خدمت گرفت.
🟣
پیرلو: روز اولی که پل پوگبا با ما تمرین کرد، همه خندیدیم چطور منچستریونایتد می‌تونست اجازه بده بازیکنی مثل پوگبا رایگان به تیم ما ملحق بشه؟
🟣
بوفون با خنده به سمتم اومد گفت: واقعاً پوگبا الان مجانی به اینجا اومده و منچستر اجازه داده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/Futball180TV/102685" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102684">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78b336809.mp4?token=D_dBb6o-tWyYaIP-PySxBC2tcXLcCm93yFh7TjCIpXxelhdThwM2RoH3nArvX_zWxHZiIVKMltTPIZRe2LQaM7V67T0auLDx6f5xht8BgxaUiyLIdzmzQVdD1tm9FLfqzOAmx8wiIChMxgDIdv1AiqE_PuB5uHvZLJ8A-vTnvMYmd_5R2yfxV_NnEHUzrOnINNbzoU586Q5DqnKcFjIjDaUo8HxEslZgY6Rz_-PJh3zLekMofxDkvZavJW6ggQKxAERaxnQT6EIVsx2rKXavUDIiTdeCjNR7mFFbNCnEkZVA7zyVKBdNvdOJr6NVOexZDKYxxrzgSGQUhWKvH3Y62Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78b336809.mp4?token=D_dBb6o-tWyYaIP-PySxBC2tcXLcCm93yFh7TjCIpXxelhdThwM2RoH3nArvX_zWxHZiIVKMltTPIZRe2LQaM7V67T0auLDx6f5xht8BgxaUiyLIdzmzQVdD1tm9FLfqzOAmx8wiIChMxgDIdv1AiqE_PuB5uHvZLJ8A-vTnvMYmd_5R2yfxV_NnEHUzrOnINNbzoU586Q5DqnKcFjIjDaUo8HxEslZgY6Rz_-PJh3zLekMofxDkvZavJW6ggQKxAERaxnQT6EIVsx2rKXavUDIiTdeCjNR7mFFbNCnEkZVA7zyVKBdNvdOJr6NVOexZDKYxxrzgSGQUhWKvH3Y62Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
امشب، سالروز تولد پهلوان مسعود ذات‌پرور است؛ مردی که از باورهایش عقب‌نشینی نکرد، شرافتش را با هیچ چیز معامله نکرد و در کنار مردمش ایستاد.
🔹
نام او برای بسیاری، یادآور ایستادگی، غیرت و وفاداری به اصولی است که به آن‌ها ایمان داشت.
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/Futball180TV/102684" target="_blank">📅 17:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102683">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTz4h5Y6YdUbIj2XoqCzx5TDNGP9KFWrjy_9uwrN-wAZFCDFOf1T5rnFYhVgfPVfnb84olORucEsboAPjpyqZoRYqLw4rzGXLeU__ov1db_5_QPaGPCx7XYtrLXIV9yRafXhozbN3k9INIDhmFX4PCiqMk7Fqk0SBEo0wpv_c_pfpFl5uGoceBICjiaYyPH52JcGZu4SS_WqtYJYo8FZMDMYv0srkT4DZ19U6KbfWz9nPBqaeNFJsLBeplzYHd1IXGh6AFJZlcEu9NVAFTXT12Qo4bwdO3cOStXNT6z33Za1gSyk3VSufzWZkfEa1cDK6g4enkljd7iSf73OgW1igg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پست جدید بیژن مرتضوی درباره مصاحبه همسرش با مجید واشقانی و شایعات بازگشت به ایران: تا وقتی جمهوری اسلامی حاکمه به حرمت خون‌های ریخته شده در ۱۸ و ۱۹ دی‌ماه به ایران نمیام
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/102683" target="_blank">📅 16:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102682">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3348f33cc.mp4?token=SQmPiVXL73T664RxaMMuSjFod2hKqN6uZq0R8kUDcn2t_phpcT2IghUx1b6AdewgktXSbZ5kP3phgLMj5m42ajcSwrVb1Caf2rADwlJl_xWs3CxotHh0yUQzPjkh1oQz3qT8NDCr1BvgS4OKW0lwRz8juXMioLVCMKK0LybpDwbKt8BlwfEKa9RJ5InIaoGDwO0XgGD5Xpq9sQU30Y2CFHzgb4z7iwwtVbNrPpntcIIs2fFC89cviXUctx40CvI7r_-zSj9j0PqnMAmsVHGB6nYL09sm95cU9V-n7lhvTWEAapG822yGEs_LdPz0a5p1loHRVBrShEm6yFUJb_s11g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3348f33cc.mp4?token=SQmPiVXL73T664RxaMMuSjFod2hKqN6uZq0R8kUDcn2t_phpcT2IghUx1b6AdewgktXSbZ5kP3phgLMj5m42ajcSwrVb1Caf2rADwlJl_xWs3CxotHh0yUQzPjkh1oQz3qT8NDCr1BvgS4OKW0lwRz8juXMioLVCMKK0LybpDwbKt8BlwfEKa9RJ5InIaoGDwO0XgGD5Xpq9sQU30Y2CFHzgb4z7iwwtVbNrPpntcIIs2fFC89cviXUctx40CvI7r_-zSj9j0PqnMAmsVHGB6nYL09sm95cU9V-n7lhvTWEAapG822yGEs_LdPz0a5p1loHRVBrShEm6yFUJb_s11g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#نوستالژی
؛ هتریک رویایی علی کریمی جلو کره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/Futball180TV/102682" target="_blank">📅 16:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102681">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018847c7b0.mp4?token=MkvA7fZmT6vUnUIBA-ghHRQ-2Fs8F6yZxlRT98vJR5STqoLdmtALTLczMUEWPGqPMUNaol7q-XGPCVV-skSJnJM8hooacRlzEOrj-XGH9EQHj1J9wR4sDA2CpskF6y3HfelgdwElXqXOqP1NQhrj6bUswmBNL6WN3dfBjdmz19RGVRd1QwDpsGxekpaho1ZX0E6tqt4hw4RdiquBb9H0SN95uRP0hF8akHRkkenPuyuTfO5tGOb45BQht39EhhNAL4anJ1Sq3GcnbP23LX1vnDhRDZqFqqRfpEoaez3Qh-kfXLtiSR6eDtF0hAM2G-p9Ri2TW0YdgWw3njENiwaQzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018847c7b0.mp4?token=MkvA7fZmT6vUnUIBA-ghHRQ-2Fs8F6yZxlRT98vJR5STqoLdmtALTLczMUEWPGqPMUNaol7q-XGPCVV-skSJnJM8hooacRlzEOrj-XGH9EQHj1J9wR4sDA2CpskF6y3HfelgdwElXqXOqP1NQhrj6bUswmBNL6WN3dfBjdmz19RGVRd1QwDpsGxekpaho1ZX0E6tqt4hw4RdiquBb9H0SN95uRP0hF8akHRkkenPuyuTfO5tGOb45BQht39EhhNAL4anJ1Sq3GcnbP23LX1vnDhRDZqFqqRfpEoaez3Qh-kfXLtiSR6eDtF0hAM2G-p9Ri2TW0YdgWw3njENiwaQzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
عشق‌وحال یامال و زیدی همچنان ادامه داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/Futball180TV/102681" target="_blank">📅 16:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102680">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrWjXDhj3RmJdWdCrEWdF6dsWSDPdZT1xEapHjz9XJKjQDZvkOEOu3AlZBhoDuSaSGaLtj92oWeE1FcJRH-GIF0_bcyjvqSIyqUZetkpafNPyH8GoZuPEOUEJjABt50rCTkWfoLuk_SKWsEVYQ4sv_jf_dyGp63U6-wtM03AEMWVo3m_tKDpIVWfsv0JRlsTcxn5xUdzlzuY1M7zhQA4FkCPHMAD-ujSAv_T_mjrqm_DviJwc7b06Oq6rR3zv1vYhzhc9fh8b7dXF-qV8-L7Mfw3LH-pvhaqSvaz5f_3X-_K7kvvBNBbbpVlQAjrHULwU2DwIvI4_F0pzk-NdtSySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
🇪🇸
آمار جاودانه کریس‌رونالدو با رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/Futball180TV/102680" target="_blank">📅 16:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102679">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5903f6c3b.mp4?token=EXJwwX7dvhboKSAWNPMl2IFDk0lW06Q6jbXfn_ojuwU_M5jkZ1nzCGhgp4rxXYTCbjmXjzzQai237ajSY9isj5Rh1muXjJx5NEbczVdqmqVX-Ee0NZut7oDVugiDqepjgf0t9Mwujt2DdvdwDhhFtYQ1DuDVIE2R788TDNZ2XywP9YMPADeE7fkyZ-OyUBaYEaGfwNI9ZJGCumNydJc1QkB2TE5Rc-lmov9PMd_PVwgCDQVJYRj3JoaINCRof_oVlrmGViCQeZ5Hm3YJPfAFhSxZHEEjfqKNCuxz-q0n53wErq18zn3QEo6iiFadNfWu7Apo0Stmmvr5n4XKML9YDXsDMtcFpO4BgzwwQc2GrcOboNT5brjrIQ7KL46JVlW48wfQgHjEWxgjetvHxErKt0__BYoJ-xuvV8IKRV_ZpXPFc6EQXa3xcILzbMQreiF-t8fiDZSfdIUI6rnsvkJvMHqIyFaextqY3BghnpFoVhTPdU0L47vYNNv1wqEO8oE39kv4liFpfF2BTBe825NCiejcJsWCuIpnW4WvPDCnjJyzIMipGrJqLa0ObhcFkP3IXsTLmG0bUdhGc8IuC-IJ7BC1HKQT8VoWhmnQBwPHiay_-wSJkyUxgxWh0-O3ogiXRFPNPar9eAhRYqynFuVhBmWmpd6QwUhHFyqQm2m6_GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5903f6c3b.mp4?token=EXJwwX7dvhboKSAWNPMl2IFDk0lW06Q6jbXfn_ojuwU_M5jkZ1nzCGhgp4rxXYTCbjmXjzzQai237ajSY9isj5Rh1muXjJx5NEbczVdqmqVX-Ee0NZut7oDVugiDqepjgf0t9Mwujt2DdvdwDhhFtYQ1DuDVIE2R788TDNZ2XywP9YMPADeE7fkyZ-OyUBaYEaGfwNI9ZJGCumNydJc1QkB2TE5Rc-lmov9PMd_PVwgCDQVJYRj3JoaINCRof_oVlrmGViCQeZ5Hm3YJPfAFhSxZHEEjfqKNCuxz-q0n53wErq18zn3QEo6iiFadNfWu7Apo0Stmmvr5n4XKML9YDXsDMtcFpO4BgzwwQc2GrcOboNT5brjrIQ7KL46JVlW48wfQgHjEWxgjetvHxErKt0__BYoJ-xuvV8IKRV_ZpXPFc6EQXa3xcILzbMQreiF-t8fiDZSfdIUI6rnsvkJvMHqIyFaextqY3BghnpFoVhTPdU0L47vYNNv1wqEO8oE39kv4liFpfF2BTBe825NCiejcJsWCuIpnW4WvPDCnjJyzIMipGrJqLa0ObhcFkP3IXsTLmG0bUdhGc8IuC-IJ7BC1HKQT8VoWhmnQBwPHiay_-wSJkyUxgxWh0-O3ogiXRFPNPar9eAhRYqynFuVhBmWmpd6QwUhHFyqQm2m6_GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
هفت کارت قرمز عجیب دروازه‌بانان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102679" target="_blank">📅 15:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102678">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVmDimc6ONs0QyupNy4AbB2BUTAH-OWp1nPYXVtQdqGbydwHth8KbZ0quTteSRXGKpiZV_C2oN5KeOIQeA-OBKZKREGkomlzMDQjUqAmFpDTepdrGNIpjcm50fpa9O9cg4WiIZkA5jzfe_-ODefyA0QUdEA7vwMw4OzoDVxs29nbdqz_PyPWVEm6SnTbFTEgwNzp7mvsO2MQNEfT4-B4M2QHGFV847-dF_RLO2YHknzap5ntY7FhlfKOq23D4zqvgffB34sfOIjzPJNeCk5hJpptJbeCwro4rseOPs1M6ptRjCX5w8nFbkL2UlPpkZrcmHQUxlxo-WpYIXLEmuCmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
💥
عملکرد ۴ مهاجم برتر دهه‌اخیر اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102678" target="_blank">📅 15:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102677">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PodPkMOONQRiKN1ZULP-VEZMy2SFnTLRmoH7jjJrGDoW3ga2lDWDpm5TRWl1oIGA66BTyGG--RqIn9FTWMCyw7N1m6aCePdNCNDu6Bpscgf1gOSDbszP5iuZfRUgUH6gfUSNaDWncK7TBcxCy0lDjWeailgHwV50-1lwKIeZ8P7Fdlg4-OTYJp-roPwlPRd7FZ7ekZHyTEoeOE8py2Cg6vwfA9Y7e72AhInL7WN1Du4uMJojOkMAfC3tNAttsM9jNnu_HtJ4aeCnpMVr-PwuCTzfaxwpT3eu4ok4BykD8ejJrXRFvhmuBF02Xv8f-d1qopyva_LKLXwg4XbUmekQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پاریس؟
🎙
فران تورس: خیلی خوبه که باشگاه هایی مثل پاریس بهت علاقه داشته باشن! هواداران بارسا باید احترام خودشونو به من نشون بدن تا بمونم، فقط باید بهم ثابت کنن که دوسم دارن و بیان باهام برای تمدید قرارداد مذاکره کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/102677" target="_blank">📅 14:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102676">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b59000aa4.mp4?token=QXbwQiuvacNU7BdnMOm9EsAl07-d5q2eZYc5S9eByDR_wR9NjC987oc2GKsZ5NJOStI_mJjRCN-ALXDc7pVBqCVt3fgf3ubvfP1Au9FgDvnWjIooQE4A2FIxOmQN-TgBsRGCj7A4yEQU90ODseEAP2gvIg9UfKNk9WAUYRzG7ZOaaeBW56unCHFfqPRsD7H-93vX9RkMxUu2MhrEpGGVYwmLTUUWbhZYIvYXNjmYfwKiKZMSojd8upOAcWdBaIB7JNN82k0ydrrFtcWF6p_ne4RB4aQyrGl0IvgCQcaSIhKjEd6jIDqhLcySrIE2LVRErBFofAaK7C9Ma2yH6eooJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b59000aa4.mp4?token=QXbwQiuvacNU7BdnMOm9EsAl07-d5q2eZYc5S9eByDR_wR9NjC987oc2GKsZ5NJOStI_mJjRCN-ALXDc7pVBqCVt3fgf3ubvfP1Au9FgDvnWjIooQE4A2FIxOmQN-TgBsRGCj7A4yEQU90ODseEAP2gvIg9UfKNk9WAUYRzG7ZOaaeBW56unCHFfqPRsD7H-93vX9RkMxUu2MhrEpGGVYwmLTUUWbhZYIvYXNjmYfwKiKZMSojd8upOAcWdBaIB7JNN82k0ydrrFtcWF6p_ne4RB4aQyrGl0IvgCQcaSIhKjEd6jIDqhLcySrIE2LVRErBFofAaK7C9Ma2yH6eooJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
برخی از ریدمان‌های اساطیر‌فوتبال :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/102676" target="_blank">📅 14:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102675">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzKC0kCw8M3MLwgJiIDuVtxxEvZlTXtFlN5kyfOONxsUapZuSg7zQ5FXmktbgNKCKs9u3hZJPtZ4-gPJAw7BtkRzcb9eszxtJB5M_cmoKTYNw0y4IGm4zz7PMLlF1aags6Hm1_kJM1xDoEMgNLhtFSOobC3pMtknfQdV6vjkdy0IH5MEK_-WAJ5tsQRuhAUZrbG-CXPhnSQPIOWaIsAsNgCW8OQMoBFU37ReMb55rtpFtXTgucRwXy6Jzu_ls11dNRBaMWBr-B3hAMyluH5CBA7aWqpCUZkhPH-mOKC0Flo9KZEeconFcvrF_xBTEvpxcL53zxK1IziRZwMquagUKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اولین جلسه تمرینی ژابی آلونسو با تیم اصلی چلسی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/102675" target="_blank">📅 14:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102674">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb25fb54e6.mp4?token=ajQoKc_cK5smMuIohkkDcFl74wpN_UfTERjGTr3ngZtNiFOTr0Nb-Om5_bwjJxQ10a8vBjyaNvQ4dDl6m8iHwJ2HqysVvOoee9U7g5zMxncL7El4jx_IQFAeXqvo6EcJ9iFi_GA8T1Cy8AMX6Hwxhj357BSRPAHHbCNzZUNudx1o1_OU5jox5BKqdoU3_Z6VewP5V7dk1_iK1xq-BDIvI8b9HziBHtmFq44sAgbzpD48hxLe_FoVsl6NNfyBx5AHDx-z0EGo0-xCAtZMiMdpmjB0X9mqd06JrXqNHTIJAc4cSx6vIDQD1RoMqg9mZ8mr6ZlZcCzV3Ye5rrwqgSVV4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb25fb54e6.mp4?token=ajQoKc_cK5smMuIohkkDcFl74wpN_UfTERjGTr3ngZtNiFOTr0Nb-Om5_bwjJxQ10a8vBjyaNvQ4dDl6m8iHwJ2HqysVvOoee9U7g5zMxncL7El4jx_IQFAeXqvo6EcJ9iFi_GA8T1Cy8AMX6Hwxhj357BSRPAHHbCNzZUNudx1o1_OU5jox5BKqdoU3_Z6VewP5V7dk1_iK1xq-BDIvI8b9HziBHtmFq44sAgbzpD48hxLe_FoVsl6NNfyBx5AHDx-z0EGo0-xCAtZMiMdpmjB0X9mqd06JrXqNHTIJAc4cSx6vIDQD1RoMqg9mZ8mr6ZlZcCzV3Ye5rrwqgSVV4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
مثلث آلبا، سوارز و مسی که بارسلونا رویایی فصل ۲۰۱۸/۲۰۱۹ رو رهبری می‌کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102674" target="_blank">📅 14:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102673">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLxrj9DLn6b53SYXriQ_wpMCA8tfbUhoZV2xq2XK7kHAYiZbR1b2U6Vv0mbEZOHNupT31pLXhNzv8T5A5w8ZE7f6Nk9Wj4KzvHZ7UDb8mNTZUImLW8R4AYbKro7uOHm9NSFQqI2jO3l39inV3bYZZIyqLL6amnygqYBTkTHKbDiugS_5rQ67ET3lVbzQV8VN2eV52KbrXRlHuJuc9C2vYIBV1705Ee1oJQfC2KOCFQ82anKIyCFvnu8mIxaum_QJKPxOm4hmMYPPBpQBd8TGw2fH0tjW0z__4QeXul9wNErmSYE9hGepErQuRRzn3ORxErdpmkqOVzxr4B78wDfNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس سنگین ایکاردی به وندا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102673" target="_blank">📅 14:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102672">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
شهرک صنعتی شمس آباد انفجار رخ داد که عضو هیات مدیره شهرک اومد مصاحبه کرد و گفت یه مخزن ترکیده و چیز خاصی نیست نگران نباشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102672" target="_blank">📅 13:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102671">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4x-U81f_lSDeeM9ZoNKq5TIuV-8NXVvPMJun7LUG_jl-LnKX_Xym99-6s2sCHtld-AWdLG5IaeUyWQJhQJ7CLp0nm9rBOGlvHbtuYmql_dTqshK7kg1v878y4tO6lYuE_d_UJNO8doR_gmilkja4uWjc471ceLU7U65bkCrHba1qtDu7Zqd3EkGMq70LUHMFQ1ZpVHG0_PE8I0wsDyPrvqjA8l3RvLzsJESjYPjHE5_VMAQIy5U3CWGuJ9XHdsucdfgRrEvs_f5jrKrpjBu2yBwozDxcM7Qx9IHjKxlq-uFjNscGBp6Og7tFcoW5TnzG64gbbN8uym4TDJxo33eyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تو سبزوار یه مرد بخاطر اینکه زنش پیراهن امضا شده پرسپولیس رو به اشتباه شسته و امضای بازیکنان پرسپولیس پاک شده، درخواست طلاق داده و به زنش گفته که کل مهریه‌ت رو یکجا میدم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102671" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102670">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627a83e0e2.mp4?token=nGeXavpoYdw5PaU6D2ipuRptnLly4gJmeq4Y73A1nH3uXJjf5Nobm3E4xlzinvcUg4Za-RR6EmRy36ywlmDRVjOfLBABllpLW_1Oa0N7DnjOegHJ-JysNJ5v98b6Ge5w8GXe5DQqouOIoqKQclj42PbCruHyHZZhdJbqPaaCBkVgVdrrCX7NtgrFwHS0Way2aFlNgwxItZsnvfrfqfnqRXWNEHnaIAyZLNEWmAznca1fQieKOpF3VOsHAxHjgiJwpSRjkN-cvhvMXFFDbqnEgpQZluNxI5iF3zKAhctv9T3HlEaYgRbYHcvr_I_yzd5vxMEJOl-Qxv87H_sZbGxbvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627a83e0e2.mp4?token=nGeXavpoYdw5PaU6D2ipuRptnLly4gJmeq4Y73A1nH3uXJjf5Nobm3E4xlzinvcUg4Za-RR6EmRy36ywlmDRVjOfLBABllpLW_1Oa0N7DnjOegHJ-JysNJ5v98b6Ge5w8GXe5DQqouOIoqKQclj42PbCruHyHZZhdJbqPaaCBkVgVdrrCX7NtgrFwHS0Way2aFlNgwxItZsnvfrfqfnqRXWNEHnaIAyZLNEWmAznca1fQieKOpF3VOsHAxHjgiJwpSRjkN-cvhvMXFFDbqnEgpQZluNxI5iF3zKAhctv9T3HlEaYgRbYHcvr_I_yzd5vxMEJOl-Qxv87H_sZbGxbvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
روایت‌ایووبی بازیکن سابق آرسنال از تقابل با مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102670" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102669">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv-_oqse4mW7qxnzQvS-9fkcuQfe5XJ5rRyJfOSqg9Kqi-q5xYH2JF543WQ6MgB4IFh1004yTgY4ZKa07GaqqRDXBXa5Oq10kRKmMtmWQpNvFrDEAz5lW3KG-_rsY0M6yZ2eqxKRPcXl74YxKQ0PLZoN46yJxPgooyg-snYTe7sBIWJpVz-CjlUTbuuaQ4p2KBHVr17abpaZGdaq8n2t59maT06Y-PEJYT7oaqkRwbnKqBpCQonwsZ857y0lBRDKUyHFk_l-bQ0lSdLviyctylfTpBei_b2SMQa88sOoJsnJ44lXfrHacZQ8BVzFrzIqIRGi9Sh1aifxbDjF_ZwXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
متئو مورتو: باشگاه استون‌ویلا درحال مذاکره فشرده با اتلتیکومادرید برای جذب متئو روجری است و احتمالا تا ساعات‌آتی این معامله نهایی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102669" target="_blank">📅 13:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102668">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e611ac196.mp4?token=nI0knLKhFDc1vsMBkQBZB88lA8uz9QVSxQVtlUNfUh_sjo_beGQR1BEABEIuHm7XaxBhJ86MXsYa_LFD3DUukmMRkthNQoEgo3Bd2lJhSQEcnRn72YpQMgB7L30x8Jkcu4Zyv7JKRQ4uxLWLkK9aT_A2dzDp43XKTgObBaRgp_u2lkhs5jMc09L_QC8eqhTFmrzthY3r-sQKIugLKJC8oZVohfR7A47eaNK85VMPKaQLAaGe4FgMVN_HYoGgQ5V80jstY9Im51NzzJ9f4aNq_IgO0WB3SmeWLGAiIsCN3a_aTvO8jA2K-f-mITDe85uuwlpSiA17hpiWJ9h4aO3S5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e611ac196.mp4?token=nI0knLKhFDc1vsMBkQBZB88lA8uz9QVSxQVtlUNfUh_sjo_beGQR1BEABEIuHm7XaxBhJ86MXsYa_LFD3DUukmMRkthNQoEgo3Bd2lJhSQEcnRn72YpQMgB7L30x8Jkcu4Zyv7JKRQ4uxLWLkK9aT_A2dzDp43XKTgObBaRgp_u2lkhs5jMc09L_QC8eqhTFmrzthY3r-sQKIugLKJC8oZVohfR7A47eaNK85VMPKaQLAaGe4FgMVN_HYoGgQ5V80jstY9Im51NzzJ9f4aNq_IgO0WB3SmeWLGAiIsCN3a_aTvO8jA2K-f-mITDe85uuwlpSiA17hpiWJ9h4aO3S5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
اوکراین دیروز کسخل شده و با پهپاد یه ساحل تو روسیه رو هدف گرفته که چنتا مردم عادی کشته و خیلیا مجروح شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102668" target="_blank">📅 13:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102667">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937fee7ba7.mp4?token=A2f-YeZmwIIYIzRlhjpuxeHyGCoeXjKZCzohmRumNoYbps420g4Osl1H7ZLZyrDZOkzGYoAIHL50J0ScSLwWj6Q0erjCMOsag1CPTnZiab_z2fxIb4rb-r0TIPWaeV8jmth7bAnAyovPQMQWwAh-dNmn7pFE-v2FWzjp7f5fYMy5FOdgFBjgz2p0lsoSjtNhXhLLBC3qCHqD8qb8XFRNdSR_jM3u51EJe2aVxZxzKhHQmakZbH8g04XvgFNbdmAjPSJ8VIp71HNhrQ1vqOyQ31OXTnPyB3HvjASCM37NoVMVMWPmN_sDj8TFN5Nk6i3-6oiOISjcy4ZeTdTRupgkdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937fee7ba7.mp4?token=A2f-YeZmwIIYIzRlhjpuxeHyGCoeXjKZCzohmRumNoYbps420g4Osl1H7ZLZyrDZOkzGYoAIHL50J0ScSLwWj6Q0erjCMOsag1CPTnZiab_z2fxIb4rb-r0TIPWaeV8jmth7bAnAyovPQMQWwAh-dNmn7pFE-v2FWzjp7f5fYMy5FOdgFBjgz2p0lsoSjtNhXhLLBC3qCHqD8qb8XFRNdSR_jM3u51EJe2aVxZxzKhHQmakZbH8g04XvgFNbdmAjPSJ8VIp71HNhrQ1vqOyQ31OXTnPyB3HvjASCM37NoVMVMWPmN_sDj8TFN5Nk6i3-6oiOISjcy4ZeTdTRupgkdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
دلیل اینکه چرا کورتوا یک‌دهه جزو برترین دروازه‌بان فوتبال اروپا قرار داره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102667" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102666">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=uQyf5Lmm3Sbg320is1xfasuJKjNGsy-i1mNCZfq0vTscJe9SMDeMMnMVBU5SRYAq7U1My4XyUcNzpiCvlb8q8dMT0mbQ2d2Kw93iyUtju_JXg6rKzOtgcEPrrcoWu6EepvffGtt9J1F33AfHhDSYMzlI-ja8xvxbUKRa-wdr6troi3VTBESLm2MiHq517YMvNihoTD4R2OKsOXqUuWcD7wFJCUOKA3_tT-LAHj2crNvPukK14Y2CWxKZdfhUUi4byjHYtn_0Nk1zaSoEc7bbfHOMF2scpC0R6amBuC6GyXURsAql-WyBgetk3JDCZFu037WpbcdNx6aajz4DeCFc6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=uQyf5Lmm3Sbg320is1xfasuJKjNGsy-i1mNCZfq0vTscJe9SMDeMMnMVBU5SRYAq7U1My4XyUcNzpiCvlb8q8dMT0mbQ2d2Kw93iyUtju_JXg6rKzOtgcEPrrcoWu6EepvffGtt9J1F33AfHhDSYMzlI-ja8xvxbUKRa-wdr6troi3VTBESLm2MiHq517YMvNihoTD4R2OKsOXqUuWcD7wFJCUOKA3_tT-LAHj2crNvPukK14Y2CWxKZdfhUUi4byjHYtn_0Nk1zaSoEc7bbfHOMF2scpC0R6amBuC6GyXURsAql-WyBgetk3JDCZFu037WpbcdNx6aajz4DeCFc6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇰🇷
هونگ میونگ-بو، سرمربی کره جنوبی در جام جهانی ۲۰۲۶ مجبور شد در برابر مجلس ملی کره حاضر شود!
‼️
او توسط نمایندگان مجلس درباره تک‌تک تصمیمات تاکتیکی‌اش بازخواست شد. از تعویض‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت.
هونگ در ابتدای جلسه از مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102666" target="_blank">📅 12:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102665">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9e48b7ed.mp4?token=P4yWSJxVBBbwagXbFCi_OzsSCPJUjCc0gfgHkI64nkhHFLYOnqdHhMDxNdkuzJfuBJOi2sGIGWHGLM7dzffjimuwd0seD4cwHSWW8VncT_m47K0obTtmmLZ7JbiS1yImaJurT_UNg2u96MNheh6RJKcubxs91mZyhuqdi6M7vgYzvFP6FsksyUo1RDNNqgRVwW_J088am6uhTZjmfWe3TWu6xnbgyth5KBmZ-YZLjgkOxoPKDTkkw3Ez0UA1sl9XAF7omkvdDv6R7Z6AxgMILznPKGa_aXWlU3jKm9wQZ_YF2pUwG2IILLlUI3UD7SYppwN0dO_RUK21nHX15bAxFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9e48b7ed.mp4?token=P4yWSJxVBBbwagXbFCi_OzsSCPJUjCc0gfgHkI64nkhHFLYOnqdHhMDxNdkuzJfuBJOi2sGIGWHGLM7dzffjimuwd0seD4cwHSWW8VncT_m47K0obTtmmLZ7JbiS1yImaJurT_UNg2u96MNheh6RJKcubxs91mZyhuqdi6M7vgYzvFP6FsksyUo1RDNNqgRVwW_J088am6uhTZjmfWe3TWu6xnbgyth5KBmZ-YZLjgkOxoPKDTkkw3Ez0UA1sl9XAF7omkvdDv6R7Z6AxgMILznPKGa_aXWlU3jKm9wQZ_YF2pUwG2IILLlUI3UD7SYppwN0dO_RUK21nHX15bAxFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
گشت‌وگذار امباپه و اکسپوزیتو کف بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102665" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102664">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOfEYMUW9kYYpgEIuA5FWmqnYV-4dHJT7WB92ssAmQZg1njsJpi4Z7fwbmve796miXcN7HlY6-2-lbzF7rujeBGkUBxOqV11rb9fVK85yIL1tIt61J7IQZIV5O2BE8cjp2jHYQdQ5rMoTzVzt-Ls9W38UgiCDjUZ3hXP0hyi6V-VFcfSY-CRvSRwP0aQrER9iO9G5Xr3uJMhMaF3JpKg6WAINodyZ8J3duwsiQrjwDcA7yh8xiqerCajGN0tLKoWK0vRKbNsFsnTWnvmzwAYgssIcJq8ZkpnTvZuRNnuL3AY0WFj_I8lgidrHrBnRsjOnlyOBLeUuxfyTevx63MYdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🟡
فلوریان‌پلتنبرگ: بایرلورکوزن درحال مذاکره با الاتحاد برای جذب موسی‌دیابی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102664" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102663">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnFlWr6Cxgbwu6L06W8J5PaLzEFuKb-mDaI3Dhpu824y0GHoFSk_aBWA1PUMhy8PFqYzm5Q4NQJaM8jybwy9FFBCxpdnDMiL9F3PDrhNFgdjifMXbrP6mZITv8-S9Vld5LB7fIAtxS5dCJD2h6fw29VAtmXwkfCk6ljhJkGD4Vpb3yElZbumZpguiK4E7-N8BMBxIajBgJ-ZVFgb7UHnHn64hPktZ10GRDMzECjETzoYMKbkAdwFp2JJrpbzfM1dKEirs1cuGVnyB-ztwy5GXZE2Ic6p0v3uzQ9A5Jbz4qD_bOutIQ7HMeJKvqwh9o8h2tUvXBbDr7cNHdDErf8Dzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚽️
فیفا با انتشار بیانیه‌ای خبر حمایت دونالد ترامپ از اینفانتینو را تکذیب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102663" target="_blank">📅 11:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102662">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UITp43Tu7Z3xq3KL78biQer--Ck-bMO4HJyZCtGZdRQslMKnQryuV_zwUXGRUHWfg2r7CCaN2gP22E-DCuENVDHOS3ShtTNABntWMJ2JGQkoBQj21BagPf1rv56x8v49f2yuBLicM6AXJNxZLOsPg-LscPqljpIqFQpYFGKThrmIt6JVkJUptkf8imJB3L0Co8bSIQsGBRZ1fVoxQEHpnEsiQ6-CoSSQRi8t_PMC8HDjsZOjrHAk3Ub5SZop0OaIIEVBXZ3wMGwdM7wxS53cIUkjOHT7yTlxASwYW7lNREJzZjYAx-OZkJfipWyVL1ZLaBe7aq1UqyosM1e3wKg6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
⚽️
#فوووووری
از مارکا: رودری دست رد به سینه سایر باشگاه‌ها زده و گفته که فقط به رئال‌مادرید میرم. قراره بزودی این معامله تکمیل بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102662" target="_blank">📅 11:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102661">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uQbn6QAtRi62l8XWh8BE1MgwsMQwrnirNBM0uGYYXhPJvtmfN_6RCgv2kqo43bhWUOwRkV4NLevuP8UdJ0gmXPE4p_LI4weOWkvKmorfPEQp7yaps_VL3-0B0O1eTQRcqLWTV83gTXPUxSiDQvcll1tfiD7q4raktdq7bzpGGQ-vzbjPjNRuyeyR1J0T4Vvn160MKPKNAtQ6MqPJ5ILh0h3ms8AemO-35fw7fn80EUNeyuna6K0Hytrdvb9oWg1f3nq6jWsaMqLxOviSkyV50vtHLuxqcl5S6Qu22lhd9q7l3S6qygqp1wBOP6a0_Zg2636rVAOsKB9El3gwcvUAsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#رسمیییییی
؛ نی‌لاند دروازه‌بان تیم‌ملی نروژ با عقد قراردادی به لایپزیگ آلمان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102661" target="_blank">📅 11:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102660">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
‼️
😆
😆
🎙
ساکت الهامی: 55 میلیون تومان دادم کت شلوار آنچلوتی را خریدم تهش ۶ تا از استقلال خوردیم و باختم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102660" target="_blank">📅 11:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102659">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yao6cydMPDDf_6O5SveyjH3qjr_zvpZG21uLpWBQmWS1VYqyoW1zt_J3MuoEkXq6lidt7eOsuHuQOgo4D3q7dzYpfBpGv-SMZ9z2ZyYeV3lm4E2jbdOyy2uZXPfwYF0Oqq7E2eGqR4hHZ3XBVRhzqAPjW-MMvdrn6H71JAUOkAmeivDHto_dmNpEAn7jxx97jlkHxu7WRdzGhk_HHkhphNeEwyGLcWyY9ySCRKp-lCacK8RK_dFHzQAXHcl46Dr7tLyC62wR9cbDv86934V30tuvtwe0e7EDzry8YMTqKBYJP1WOsENpABI-PecFjemNRYg4UoneIi7roT0PFgJBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژاکس آمستردام از جذب مارک آندره تراشتگن به صورت قرضی تا پایان فصل از بارسلونا خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102659" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102658">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf1a57969.mp4?token=MmK2CnVJFUHfICvOtUyd8E8brqLznec6Dka4K_VoGYX_nNL0KpelVE0nPymbjSveuaGlwqkvTAN5r93Eah5aIsO5fnVTmidnjAMkIvEdQgk--NGjlEZuj9RFfY4WWScjPpb3dEOQiM3go_NKq0ZnHSNWthCVLGu_lID4fhejdMWBxb6SStDZK8v_ayV6pOlNPRR7PmGP1cYq10SwyaI71Gke5eMrISAtVfih1AuVIttdgQyo5xrCbbaOO1OrJNIOEi9nxCEQAwN4AGaRYqQgBZWyYGxioZTJNkQGGRsjHvz72EuXGyriG6s7y3Mr187EoscFD8Q4SlayZNTS-p8H5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf1a57969.mp4?token=MmK2CnVJFUHfICvOtUyd8E8brqLznec6Dka4K_VoGYX_nNL0KpelVE0nPymbjSveuaGlwqkvTAN5r93Eah5aIsO5fnVTmidnjAMkIvEdQgk--NGjlEZuj9RFfY4WWScjPpb3dEOQiM3go_NKq0ZnHSNWthCVLGu_lID4fhejdMWBxb6SStDZK8v_ayV6pOlNPRR7PmGP1cYq10SwyaI71Gke5eMrISAtVfih1AuVIttdgQyo5xrCbbaOO1OrJNIOEi9nxCEQAwN4AGaRYqQgBZWyYGxioZTJNkQGGRsjHvz72EuXGyriG6s7y3Mr187EoscFD8Q4SlayZNTS-p8H5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
پدر تشریفات ایران آداب استفاده از آسانسور و پله برقی رو بهمون یاد میده که بنظر هیچوقت نمیتونیم رعایت کنیم
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102658" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102657">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0e4679b6.mp4?token=EI_6HTaKTj012GwVCeMwVP0Eh0ojgqsiat9sT1CxRvyCwiy6va_h-7Ssu4W7hKddRIU8sTwQNufDvIdCSa8ZvhFmiWpgPrm5epcejSqcHUIfIAicJn_5YlwXcEj37w0tvusXVW48ReQZ8UjEiAalmFfV1wrieOhnlV6wVshrWitxkiSjmKoPN9MEIArCzITmEVywIpQQoSq47yHJ6PhK5tOLh5VbmYGqbhCLBQATV3XqReOmTQb-UVVPvND-0tbL_Evhp56i9U1fRMDhMjl4MZLycKesr9I40zM9pjbnYIotnWZnPkGx3Lyaay74x_gotu1diJZjcDt6muQxyP6MBzyfhZhytttqU8ZfdJLEBSLTEQdi_GgKs_Uw6zTzAWjeOaMyVKBpZbwBwHWkE4QJSg_f8cgIYAzkSE8fZTCNz5iSFFgZeDGFyl-NunYIAtGY50me_C1qyv09Jc8vZ-zi4Jjx2BMHFx-bBYCdtL1Y0Ao83IxPMH7QeE8Toiy0cOzCO_HppND_3llX3Tz6m5aITUfoe8RtT0MCsJUvmchgXqEwHH32eAjP3UHmo--RT8EchIjwJN5koWvEvKCOYcGsMNeUYZGTJ8_m60BTodFbp2KRgdGnKyozgJbD06SL3pmYM2BFX2orYfVIYl6AuHzARpXx0Mz0-c-LmCjQzZHcn10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0e4679b6.mp4?token=EI_6HTaKTj012GwVCeMwVP0Eh0ojgqsiat9sT1CxRvyCwiy6va_h-7Ssu4W7hKddRIU8sTwQNufDvIdCSa8ZvhFmiWpgPrm5epcejSqcHUIfIAicJn_5YlwXcEj37w0tvusXVW48ReQZ8UjEiAalmFfV1wrieOhnlV6wVshrWitxkiSjmKoPN9MEIArCzITmEVywIpQQoSq47yHJ6PhK5tOLh5VbmYGqbhCLBQATV3XqReOmTQb-UVVPvND-0tbL_Evhp56i9U1fRMDhMjl4MZLycKesr9I40zM9pjbnYIotnWZnPkGx3Lyaay74x_gotu1diJZjcDt6muQxyP6MBzyfhZhytttqU8ZfdJLEBSLTEQdi_GgKs_Uw6zTzAWjeOaMyVKBpZbwBwHWkE4QJSg_f8cgIYAzkSE8fZTCNz5iSFFgZeDGFyl-NunYIAtGY50me_C1qyv09Jc8vZ-zi4Jjx2BMHFx-bBYCdtL1Y0Ao83IxPMH7QeE8Toiy0cOzCO_HppND_3llX3Tz6m5aITUfoe8RtT0MCsJUvmchgXqEwHH32eAjP3UHmo--RT8EchIjwJN5koWvEvKCOYcGsMNeUYZGTJ8_m60BTodFbp2KRgdGnKyozgJbD06SL3pmYM2BFX2orYfVIYl6AuHzARpXx0Mz0-c-LmCjQzZHcn10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
▶️
آخرین فصل‌ لیونل‌مسی در بارسلونا
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102657" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102656">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برترین گل‌های محمد صلاح در تاریخ لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102656" target="_blank">📅 10:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102655">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzEIEP1EFY1we2j6I9Z9GxlL2t-mpIVEC9PoM7z3zwmG9sBxXHsyddIWPkVxzqSiZdNMWrZIVOVKYk-ujJ93sYHu-_5LYROHMA0zmcfr8P_l5OeSHlsY5cq9Fh-A0jcLp36Hy8lzGQrfywqyPgubZPWl6eosgIiIkcGvqzlRVHs5ySUsYaAR0PGbGJ0075RxBI6xmIRJwM0HNZPcUoa2-ePrZXgGAi4j4k9BKyeT_jUCqKz-rp0BKM8UjItra5-dA6AWk5d55oHaysqRHqId76FCiB67u5QCkHP2Sh_eudSjHZcXqxsJZBzM1QTtysVj8saDdodjK1Rfk-FrdxJi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
مدیرورزشی لایپزیگ: دیومانده به محض بهبود بیماری خود به اردوی تیم در اتریش ملحق میشه. دیومانده بازیکن تیم ماست و به قراردادش پایبنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102655" target="_blank">📅 10:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102654">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👀
🇪🇸
🇪🇸
یادی‌کنیم از بازی دو سال قبل و پیش‌فصل الکلاسیکو که حسابی جنجالی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102654" target="_blank">📅 09:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102653">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
‼️
😔
🇮🇷
پرزیدنت مسعود پزشکیان در واکنش به جنجال‌های ۲۴ ساعت اخیر: استعفا نخواهم داد و خواهم ایستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102653" target="_blank">📅 09:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102652">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f47080196.mp4?token=bk-kFDh_fbuRyO6bxHl7N1lSJv3tjIXBkq1VYO-JVf8aTOFyuRsJX8-DV3pDBLSmqz7H56uBpER3k1V5L7KHqctVZUj8UjQt6ZtgV9Jq58wZHBa6M6uJqssp7Nz1ovOstSyG6YluLPSB1RvgL3RQ_mToBuUpLMeyvNWrvh0gXcw7e930GI7D1yBJme1tUabFFMfeF_dv2_xjPGorllaRUTHdO3Ilj8f-ICWhMf8BOLGgyk7kVCyIxUAejBE6vxN-ysWKbwip719RI3wOc8WBwfQe-a1MNRLqHKjplwa7m7bExBwj3gxVHRFomPcSdHu3S9TqgzQNE24KKeycTlmPag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f47080196.mp4?token=bk-kFDh_fbuRyO6bxHl7N1lSJv3tjIXBkq1VYO-JVf8aTOFyuRsJX8-DV3pDBLSmqz7H56uBpER3k1V5L7KHqctVZUj8UjQt6ZtgV9Jq58wZHBa6M6uJqssp7Nz1ovOstSyG6YluLPSB1RvgL3RQ_mToBuUpLMeyvNWrvh0gXcw7e930GI7D1yBJme1tUabFFMfeF_dv2_xjPGorllaRUTHdO3Ilj8f-ICWhMf8BOLGgyk7kVCyIxUAejBE6vxN-ysWKbwip719RI3wOc8WBwfQe-a1MNRLqHKjplwa7m7bExBwj3gxVHRFomPcSdHu3S9TqgzQNE24KKeycTlmPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
روایت دیوید بکهام از میراث فرگوسن در یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102652" target="_blank">📅 09:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102651">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TttQfYtL06AB0GWuzd7LypBbWOM76yhCzoKJNK_wcF4OlK1Tev6AphSysA0P-U7SwDGlU7Qf7aOv8vQ_9G1NPdVkaamB1R3PNnZgwgCwuS9Mp26dIKYgWmU9VoQGCA86nistSelRr4n2MQiNqYKlp8iW3kzs6ghlNfKxqOZR5rc8bj74a3J0gNqGCUadh3pd1F_Ut50KOmfI3VwtODDZuHHqrS2Qb69Fiucbp5nbGe30VkCUUxAIi6ss3RlR0nYHBp31NxLZ--QAuvHCIkvePPLShTTixazyANAMt2lywvo0NGEVjVH4JgGnTpNabexmcfqmdV5gzzuZz_hirvMJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
کشور عربستان سعودی در حال ساخت بزرگترین شهر ورزشی جهان با بودجه ۱۰ میلیارد دلار است.
🤯
این پول معادل هزینه خرید ۸ بمب افکن B2 یا ساخت ۱۰ تا برج خلیفه ست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102651" target="_blank">📅 09:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102650">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeIecWXv7za6JA807m-ERhRffFF8KUbFcTfk0D7Osmmv-4rhuSLT71Da6R7r_6H41SDPhsDaRbQbs8xpkkZzckFx-i76xNe_ss0GhVNHEMAvgwXdPPLN4fizxtmUxCxLfHrFhFAx9rxDezpPfm8jXRXYLggLClO-bJobxX5whbfvCvMzzS4U-dZeQcAWiPoM6uiVH5WFJWn-Zpe3Ovh4fwz871Wn-dW9JBd24b1XWe2iCabpAbHYeF85RbSrSxGOoM2Y7f3nr457fglDvJ3mK4tCFhof50BCDbEXaFskrcwFMLZWd7d0W8JdaStqcuos_8wvKGVZU7ziAFRG6W3qAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه سان‌انگلیس: باشگاه استون‌ویلا بدنبال جذب مارک‌برنال ستاره بارسلونا است و قصد دارد رقم ۳۰ میلیون یورو برای جذب این ستاره جوان پرداخت کند. هرچند که بارسایی‌ها این بازیکن را غیرقابل‌فروش اعلام کرده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102650" target="_blank">📅 02:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102649">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d8f16631.mp4?token=ZgpLizEHSb1VRZXL13OK-JhPE3guoLxL50T2rSkjT8VdmQXrrfZIVD3j32JEuzXYJocqLLVWKnmuVH4ZYwOLA0e6ABaAomPDFOXXi9Nl7M_-JjTTzIbmL-74mRJGwCGCek-aFzOF-0CL89SHK6xY6luUN3ZsdtWq8MammAtiHJW8KzBanjTs00ldyLV3T1HuyTw09ZQKzSzhrU_NDyoojN28-xfaoKT-gH4Dole0hQmbHghIhSmsFLeZHunxyJoBvLbhYVzF0xwisXoRnwXpo2QRBTgyEvGV02vUtqSxicU6eNxttC9r5gUhCP6I2iUXqOrEJ30izKZHC1Ni1cymzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d8f16631.mp4?token=ZgpLizEHSb1VRZXL13OK-JhPE3guoLxL50T2rSkjT8VdmQXrrfZIVD3j32JEuzXYJocqLLVWKnmuVH4ZYwOLA0e6ABaAomPDFOXXi9Nl7M_-JjTTzIbmL-74mRJGwCGCek-aFzOF-0CL89SHK6xY6luUN3ZsdtWq8MammAtiHJW8KzBanjTs00ldyLV3T1HuyTw09ZQKzSzhrU_NDyoojN28-xfaoKT-gH4Dole0hQmbHghIhSmsFLeZHunxyJoBvLbhYVzF0xwisXoRnwXpo2QRBTgyEvGV02vUtqSxicU6eNxttC9r5gUhCP6I2iUXqOrEJ30izKZHC1Ni1cymzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا سپاه به پایگاه آمریکا در کویت حمله کرده و آتش‌سوزی رخ داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102649" target="_blank">📅 02:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102648">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇪🇸
#فوووووری از ESPN: رئال‌مادرید پیشنهاد دستمزد ۲۲ میلیون یورویی در سال به وینیسیوس ارائه کرده و قصد افزایش این رقم را ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102648" target="_blank">📅 02:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102647">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuOH_Yp4V5-jDDnDcA8btBUP2sY6-5V0sQ_TGmKFAUAb4iOuf73-9hjO5AZhqNDQvjwxQDBAGOVoVtF7Vt-3cal-zZi0qwNNie3jyoOf9JDfu5E6babyOISpcTimWNWvhnWAZt0gphhPAcbGNDQepwiM5BT-JavpTAreyDhfqmihzP2Q18TblSn6cTmSkU8bNrBp4tVQKbkEcnUBfpVDo6-FsWbJYLezJVLqQyHnEEChvlzThfsf_iJtO-1AuiMTTBs8SksGI0LbhYTU6DpI5B7KCAkHm0SodArywt11LTT47Wafb1-1vNq6BwUuZTBTUjEwg5eU8G_5i0JTabpiAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از ESPN: رئال‌مادرید پیشنهاد دستمزد ۲۲ میلیون یورویی در سال به وینیسیوس ارائه کرده و قصد افزایش این رقم را ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102647" target="_blank">📅 02:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102646">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obcSzdhUA0nGrDOwQ9N6RDb0Aq1scTLFANmXh-W2ytRDZICMHzV5yhNQOkTGbaaVwtCxVidsICqA9tq1vZtBU2tDd-GyOueIg536VV2ORtUcLsWSPBkzaHOxEfxMtr8MErcxHo92Cgh7_T9QooSNt3IXEPLCoSDSYsgS2FE1ygVR3OC7_XV7zuNNcv6ciUQAWHUq45dwyY6ISM6QZmT5SK8ri0B_YwGPCFm6z86Q3RrDch4dDOgTrD_-Xd8sXGUdkyokU5sHVZyL0ZMamzxfP2dLkqAlYD-YhYpK7ZU_YRNOsCket_KA3ieK3BveHOegLgj2rxPYUbAW0rzbyVwf7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
بن جیکوبز:
چفرین و ناصر الخلیفی در سالزبورگ دیدار میکنن تا درباره تحریم جام باشگاه‌های جهان در صورتی که اینفانتینو همچنان رئیس فیفا بمونه تصمیم بگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102646" target="_blank">📅 00:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102645">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDyZ2VMnL_sKkGYfSa1ovh9Qlb86MC6V-T9N17LjIVkEd6NjWvgPqBJUAIHdJ8cpMBH-_TzwEClEme6dCcePO2ONW7HCD0Kb2qdjxFoCJvRCz6QM5WCCOQ1uf_2Z2KSHtyPBIt3HIl1NvDYeNWyIVFCO2TNAbkzbWmdgZ7RTHTDWUDnXIvKdKTYxBE9i7bdK1XdDDCCCPlIzP2EuqNbzNG6lNB5dUoj_pVDS4hVrJvZ2QrvVoppniep1b3XXnBPBCzneNGUPewkXqQ516hSgxLupsLVCkJ5UwFdrOVbI-kPc5NZuBfCKfM4OuKOrbF-czElViuBHTeCJUhxgZrPTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پاریس؟
🎙
فران تورس:
خیلی خوبه که باشگاه هایی مثل پاریس بهت علاقه داشته باشن! هواداران بارسا باید احترام خودشونو به من نشون بدن تا بمونم، فقط باید بهم ثابت کنن که دوسم دارن و بیان باهام برای تمدید قرارداد مذاکره کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102645" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102644">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
با تایید تار تار و اعلام رسمی ایجنت بازیکن قرارداد نهایی شد
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102644" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102643">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kZlxLj-srXeOdjonwpmkp9dL65bqFME80BHcihJ0I68kGfcaX2L2Zfj4jVeBYyi2Pj0ZgUc8DlCOKKAd1WjggOUUdYWBIt1R0YclF2kj3lTb_IGKn8vXBWBmI5tK9FXbLAn54sqgprjzBCi1QHto4cuv7cJWy04HNhxMVMBm2nxRMI6s3gqx3irko0tuoZJyZ-zy4OsoLzQPC36tYJqEpSm6kjWQD1rkKs8poPS_Pib51mOEi88JMam3XwMKupqsDo9rAkcERc2vCKyDD9g_mTfmYssXA68SLYySWnhGkshIJp58VouAVzQi_VSjGL_msHAXw90uQdsIY74Oy0PvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
🔴
تارتار تایید داد؛ پرسپولیس بار دیگر خواهان جذب</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102643" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102642">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-HdpzVlCQ6A1k4ckeIS2JT8H2Y1DDGvBLH-veY2bdCiO68Wo1CKcuWhgECDNdMO1ev3vzD8rMPMc32272zMFh7GVZzW2TwW26JBl0E_KupmjBrGZYLbFV07OoszqwPdbDGGHNj-TuoOZT8Lv-eoBfE2Ymm3rbDBP9mQU9SKluaQE3Fypcyju2mS5hNIiLVE-RHAJPBWT0kIRDR4tBGzd1zSuv5Qlx619GiiaTrSthsUl2xg6dm1EUeJNB-4623hwOV57iHD3dIqIFXbIzde7tLTOYsJipRKQoBoqDX2QouXjQmKz-BX1Wu1QsAV4LE-6qRnsVSi0a98N-s0-U6kvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
برناردو سیلوا:
بی صبرانه منتظر کار کردن با مورینیو هستم، اون کسیه که برای فوتبال پرتغال خیلی مهمه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102642" target="_blank">📅 00:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102641">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b215f0831.mp4?token=i2pKnuFEYWbzylQEMKhSLNd5Kd1uspyZD5LB58rxkQ9Xwb4lbANjhVag7p7wfojCqxIg_xn78tcyatLswYH6knPpmzHcqwgsODIZhLM0EePVZlNXBcRfmUGENUarp__XiFGeGI38Y8Q1upCqmiH-1_nNPY7Ee_gA495pqHwLZzS_ljBCemghkqluw-SkRw_zfA_1Ug2rZtG2OWj7OOfF_gJkHpzEvWsLOJNrHb9X8fBmRlhzJbZZGVVT_B4mCAqE2WDrbKEWd_D0AMEK2LqD-rXd8mvd3O8PgVjgDpM1KyDwvLy21D2ThDmdLRmNjMkD5Dm_ihN-5llVjkiThUubAh_8Hpeb0X3yw_gb_2LxmbD7tM0XndE5Wh3VW57Mf3C6ihWEjwH09OheRRaYgSo3-ZQiI6iv48p9Yppq-Ze2KrKc_FGe-w6_bmHDeuw-VIcRenAaDrR795kl2ZpD8wnZK-K4PVUHOX1FqKZQdiD_XDZLkQ0Cyv92haMqquTdEP9TcD3wPw7KJIgQFv1MP0QtzgdMrCpT13vzKTgiqZ6sTXbED9yJeu3-NaABBiV-edHUfNy2ZfhfOYXUk2J7-YYL8GOS3nlRliGhArjrQ9zgx7Vme0HLEu1783IDPB1DJNEuwx2BQ4DhuzxUs6aLF_92x4uNw19wbrd2zX_Jz7aahiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b215f0831.mp4?token=i2pKnuFEYWbzylQEMKhSLNd5Kd1uspyZD5LB58rxkQ9Xwb4lbANjhVag7p7wfojCqxIg_xn78tcyatLswYH6knPpmzHcqwgsODIZhLM0EePVZlNXBcRfmUGENUarp__XiFGeGI38Y8Q1upCqmiH-1_nNPY7Ee_gA495pqHwLZzS_ljBCemghkqluw-SkRw_zfA_1Ug2rZtG2OWj7OOfF_gJkHpzEvWsLOJNrHb9X8fBmRlhzJbZZGVVT_B4mCAqE2WDrbKEWd_D0AMEK2LqD-rXd8mvd3O8PgVjgDpM1KyDwvLy21D2ThDmdLRmNjMkD5Dm_ihN-5llVjkiThUubAh_8Hpeb0X3yw_gb_2LxmbD7tM0XndE5Wh3VW57Mf3C6ihWEjwH09OheRRaYgSo3-ZQiI6iv48p9Yppq-Ze2KrKc_FGe-w6_bmHDeuw-VIcRenAaDrR795kl2ZpD8wnZK-K4PVUHOX1FqKZQdiD_XDZLkQ0Cyv92haMqquTdEP9TcD3wPw7KJIgQFv1MP0QtzgdMrCpT13vzKTgiqZ6sTXbED9yJeu3-NaABBiV-edHUfNy2ZfhfOYXUk2J7-YYL8GOS3nlRliGhArjrQ9zgx7Vme0HLEu1783IDPB1DJNEuwx2BQ4DhuzxUs6aLF_92x4uNw19wbrd2zX_Jz7aahiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
برخی از بهترین گل‌های کاشته تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102641" target="_blank">📅 23:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102640">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290de4f011.mp4?token=RcpGfHRmeQ02nc4HshxFIG92GjANJNMK-rID186IWpkGm9gzneU9nriGomQ73KMJRKgG3f8X0vI7gOOjYZknb8vBcEZmR00fuwpA2vNvsHINhRmkFUttoIn3z5vU8zxvgDRlY7ovkHyf-Dz1zpf336criFlAr-l-W53NQLmBdCNDjHc_xO8bpj5-6K5yYEJeG7aMrTnyE8dIhRu1bcRD7IpDYvRncGc-bXqErLuhL3Fi793udkZCEluAhC1D47THnK8t-aEI8i-vXpdiy3J4NI3kEdEFpydjojFC4WZaY5mMFkfxh8mAZbDwDg-gKfAvAv9E9Nf3kfPweW55BauFhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290de4f011.mp4?token=RcpGfHRmeQ02nc4HshxFIG92GjANJNMK-rID186IWpkGm9gzneU9nriGomQ73KMJRKgG3f8X0vI7gOOjYZknb8vBcEZmR00fuwpA2vNvsHINhRmkFUttoIn3z5vU8zxvgDRlY7ovkHyf-Dz1zpf336criFlAr-l-W53NQLmBdCNDjHc_xO8bpj5-6K5yYEJeG7aMrTnyE8dIhRu1bcRD7IpDYvRncGc-bXqErLuhL3Fi793udkZCEluAhC1D47THnK8t-aEI8i-vXpdiy3J4NI3kEdEFpydjojFC4WZaY5mMFkfxh8mAZbDwDg-gKfAvAv9E9Nf3kfPweW55BauFhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮‍💨
چرا بزرگ شدیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102640" target="_blank">📅 23:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102639">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTIZAy9ZTRakw1YxTvOYD3GSfikl64AOyC9XrWeMinDws7OVhHEiCyKgxoOj3GezBlyouUc9_Pe3wnwj6kfJSFLYOxo4-ja6sluA-T-ogmvIv4agNEvxdgwpzmDMizoSDHgVIbqbCmcCzt12vhQqOJxhgb48N_le3mG_gAdgZ2WbIKESqEUSwqJBi96a0NKLZMy5JJbJKiFm6IlTblyDDju0dvFOoNmup7SUdaxzH7snlAm1j-4Iw-Wk8mp0Rc4DVjgNGBhJNVy3Oq9qNHUlCvfzjujYGWOaO_qlPelt18nC-qyX6NWM-SwYAqmIKi3dfna7UlX8OUjgmgW0GR-jBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا : رئال مادرید بهترین باشگاه تاریخ فوتباله، نه گفتن به پیشنهاد این تیم غیرممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102639" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102638">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC4pYrDWA4Ifo-DAdwlVvQRgcQiorzAHrgh3DyA0LQktav4yrooy_LKRCsctSPdCU5NlJxyPmOaDjO-7wRV0aOflfeJgOPtzKsFDDAylgtj95rBxvx3O6RVr2X8c3Fo1KLQ0kDwfwG72miHYoB9gy9uSCIQ7m5blWkz5UTDP_Kl5HkBAwj0jqngea-p97GaarsuaKoueWbnAVjbQfEuAY6gvb5f-hCUK3_LwoYUQ09bZTgdFjKW-I4z9UQf2qQUu0E4Nn2pRNEtt9PtclKXcmEX1_u4qRAhhaUW2A56RzkEBJsGcDFlRcjUr5BPiZ8jFRxp1IiledudYoVFe_vqjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتونی
ویتنامی و اروپا
رو از شهر مرزی
بانــه قسطی
💳
بدون ضـامن
بخر
👇
👩‍💻
https://t.me/doniakalacom
کانال تلگرام مجموعـــه بزرگ دنیاکالا
📱
https://tlgrm.in/doniakala
بزرگترین
واردکننده
🚚
کتونی در ایران با
سـ۳ـه شعبه فعال
💊
کاملاٰ
طبــی
ضـد زانودرد
🦵
کمردرد
🩻
اینستــاگرام
مجموعـــه دنیاکالا
📱
instagram.com/doniakala
✅
ضمانت
کیفیت
💸
قیمت
مناسب</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102638" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102637">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac45ed94d.mp4?token=i4c9krYUGlryEiQlz8WBm2PNnl-rh0ZnwmJspHdiSge3jjfPGiMAc8W9AsIOopvi86CKDQAZ6fuIDbFzXtuyxkPUcFexvt3XhmB4q6zaC7fre-VCf8Q1DODIcNyRhOEy9bTLG7osloD-CWLTnl4RpIOCVifHPOfEn4e_yiwKhYE4gP2gQcMHionbgmZZffYUgX3X-AcJsCkb8tPVky94x6Qyzsbh0wlcvLv_u-kEK1WGZ9pS1PahIynA_GNLJRaxxTFLuWY_yXOCPGwL83ic1fnJhtomTJieWzQDuQ58n8nTTkBemPGK_iGz7vbPcPDZjfk9ClaDmwMyOEc2R_AX432RxXVjXYx9UA3i3mJseiU9xNKX46ReIYbWCMuMYtBWm2DikoWFIn73VEc6BbH8ObXhQ4TceZeBudUQNk0yRxkLV9NPJyqLOkultPIu7zWYliBOjubo85p49yTEH9NvF0PJJzzQvVHBCs045LNTk1SELDDmlZLda_lL4-ON5EnDYfZgGYdIuXjey6pWHtArsHWL_gxvnCByziDA4CRCO59vJsKobuqnIzVrt2ucNDtuzulSS_bcxCexKUhihXk_IIVP4HfLUsHNxxj5-x4d22FKnBk7h1j0rainFfxEgNE8SL2d53wiHyRsJghrx7eYUAduFi0HT1DubPNG56LRoW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac45ed94d.mp4?token=i4c9krYUGlryEiQlz8WBm2PNnl-rh0ZnwmJspHdiSge3jjfPGiMAc8W9AsIOopvi86CKDQAZ6fuIDbFzXtuyxkPUcFexvt3XhmB4q6zaC7fre-VCf8Q1DODIcNyRhOEy9bTLG7osloD-CWLTnl4RpIOCVifHPOfEn4e_yiwKhYE4gP2gQcMHionbgmZZffYUgX3X-AcJsCkb8tPVky94x6Qyzsbh0wlcvLv_u-kEK1WGZ9pS1PahIynA_GNLJRaxxTFLuWY_yXOCPGwL83ic1fnJhtomTJieWzQDuQ58n8nTTkBemPGK_iGz7vbPcPDZjfk9ClaDmwMyOEc2R_AX432RxXVjXYx9UA3i3mJseiU9xNKX46ReIYbWCMuMYtBWm2DikoWFIn73VEc6BbH8ObXhQ4TceZeBudUQNk0yRxkLV9NPJyqLOkultPIu7zWYliBOjubo85p49yTEH9NvF0PJJzzQvVHBCs045LNTk1SELDDmlZLda_lL4-ON5EnDYfZgGYdIuXjey6pWHtArsHWL_gxvnCByziDA4CRCO59vJsKobuqnIzVrt2ucNDtuzulSS_bcxCexKUhihXk_IIVP4HfLUsHNxxj5-x4d22FKnBk7h1j0rainFfxEgNE8SL2d53wiHyRsJghrx7eYUAduFi0HT1DubPNG56LRoW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دوران پرایم‌اسطوره مانوئل نویر در بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102637" target="_blank">📅 22:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102635">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P47N3pcoQi3JL2smPMryCfz3gq6FFhI2Nogf00nZnojyomk4Jdc8TUmrRnCy5kj91qhAZrCvFmDOcqLZULQBj1buX8pwlVJyx32dR0T2i4cIun5loXScoyvD3Dn3XZWu6BiqSSShEYu7j1QtvaWr6gF0IaH1RrzfIV5xezwGCGtYGov8PJKkuQ7ClVx9Gm6wOFyJp6lLGu4vE4bWM1NKbtlDr9282K_V0CMiIIuEnrYHE1bRkXX3Cvj0Hf9etljldIGqlmEKdOrIq8DKObRudvFIPDqKZ3j4TJJ5P7OMo1Yog6YTD1kwANjhuWdObJ33rRuRep-NDZ1LFQHb1e5OAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCzkR67UHqgrSmXWZHTz7rBTmLrtIcQS7EJZa5Z2RxLfpku5FwzC_oguXv6r60nwdeHFJBnTiwDMnsSmGKosorrV620FxYD7VefDdEsOK2uFFl5jhBinWbUIg98RrvhkwazWUB7b-mUOTI9tIHcUTm6nGQ7_LpzYLMACVTzcK9iMuGe-lPukuUZbhHsuOIGWGAOpb6OSaTeL9-44XuvGFqbtGz2NojEodRc4SOEvoNy7_LhENNpW-kCVhGmqEd-tOjVUJZiX0N7efKKBrErCEuAvGZ2NViAyiyc7Behx59qbkCauKzb6_121Vy84-cz076NfM3hUsbUl8VHROmNitg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وندا چقدر چاق شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102635" target="_blank">📅 21:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102634">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=LkzpuNqKiSEPnPy8WjyZsO3RPBYfRr74GMZWwHBS-vFAEWrtjATkgctxuldnPDFNMq8pBQwc3Z6BuasmnmOv_rVV4P_uMdrgF7RUBOPKiXdP_gJwU2aaD1ic6SrQAHCy9DSBd8ysOjxj-hSUnyJMf5Hcj1q6fnq1rHnB4VOPmj_-RdlKRO29DLkyirObDkOpSKDPLvYv2vuZSAeXJtarf0DNvo2wX3tr_fKPxSlvkkzEt17LqWfKL0s-eNMH64lsqNRTYsN-8f7OX90mDAOsub5Ed8fVCZ9eFG9LyXXL6NHvzjyyFEccMZcTIQ2HaJC0xQfbQGBf4XtiPM_dWi0rkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=LkzpuNqKiSEPnPy8WjyZsO3RPBYfRr74GMZWwHBS-vFAEWrtjATkgctxuldnPDFNMq8pBQwc3Z6BuasmnmOv_rVV4P_uMdrgF7RUBOPKiXdP_gJwU2aaD1ic6SrQAHCy9DSBd8ysOjxj-hSUnyJMf5Hcj1q6fnq1rHnB4VOPmj_-RdlKRO29DLkyirObDkOpSKDPLvYv2vuZSAeXJtarf0DNvo2wX3tr_fKPxSlvkkzEt17LqWfKL0s-eNMH64lsqNRTYsN-8f7OX90mDAOsub5Ed8fVCZ9eFG9LyXXL6NHvzjyyFEccMZcTIQ2HaJC0xQfbQGBf4XtiPM_dWi0rkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوانین به ظاهر ساده فوتبال که نکات کوچک ولی مهمی دارد و در لیگ برتر گاها داستان ایجاد می کتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102634" target="_blank">📅 21:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102633">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=C1jhHPjHQS3aYH1z0i5npNRnADtuXF9wPT0Ngk4Ro1vzdtLy3Z-sUYLOlg9uGWRfycdpyM2M7asdW_45FdZJvk9oPzSN7B62JmchYeKGU7VBpy7Y0ONL2HUqxT1EEbZTLeDTRI-dj5JOhQZwjjePU5ev8DwVmnwNnR0DiMqFHtjfwnCCU2-t6rRSB_uuWHjHiWKRVInWZn57q1pVsz24-hVJEJvwSOI16VjC572QPhQtNgW2V6wD7mMdf0DjekHjxamymE0LfNKxkSa2MaOrefZ5mbSZ2_OZnwdoFsYzhe5TqlOcgHf76MDm5b5FmThXSje_jsV263E1eWKPW69UUBQOQPie37wBSX6uaCOCj5sMsELyDxngiYNzV4pTNtjKy3rnSM-9SfDkZxrsbo_A7qIxPZ2OFcxOZs_dnNmXTmtS-U_hFGA4oTTyC_lZcfh13fiOb_PVZcIRZ_tIIqL9tK9pmZNO0YT9eXna6vKcSIDj8t-JqPQqCpOANRYxCDNtyDktm8L_LH531IMuOBpKnvhJKOS7Ba6I90pcs-ofmwrkLjFgaoWRoimdJOKFg2dlJxMio_1_US8-qkeMjdkpvOAbmcUaqdwgbG9uzRuZzIjKl1kX5zOrvNh-NJVJuHnv6qkPiSGcqD-epIbXb4tylgEWK-ZDwxQMX_GFbBiVc84" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=C1jhHPjHQS3aYH1z0i5npNRnADtuXF9wPT0Ngk4Ro1vzdtLy3Z-sUYLOlg9uGWRfycdpyM2M7asdW_45FdZJvk9oPzSN7B62JmchYeKGU7VBpy7Y0ONL2HUqxT1EEbZTLeDTRI-dj5JOhQZwjjePU5ev8DwVmnwNnR0DiMqFHtjfwnCCU2-t6rRSB_uuWHjHiWKRVInWZn57q1pVsz24-hVJEJvwSOI16VjC572QPhQtNgW2V6wD7mMdf0DjekHjxamymE0LfNKxkSa2MaOrefZ5mbSZ2_OZnwdoFsYzhe5TqlOcgHf76MDm5b5FmThXSje_jsV263E1eWKPW69UUBQOQPie37wBSX6uaCOCj5sMsELyDxngiYNzV4pTNtjKy3rnSM-9SfDkZxrsbo_A7qIxPZ2OFcxOZs_dnNmXTmtS-U_hFGA4oTTyC_lZcfh13fiOb_PVZcIRZ_tIIqL9tK9pmZNO0YT9eXna6vKcSIDj8t-JqPQqCpOANRYxCDNtyDktm8L_LH531IMuOBpKnvhJKOS7Ba6I90pcs-ofmwrkLjFgaoWRoimdJOKFg2dlJxMio_1_US8-qkeMjdkpvOAbmcUaqdwgbG9uzRuZzIjKl1kX5zOrvNh-NJVJuHnv6qkPiSGcqD-epIbXb4tylgEWK-ZDwxQMX_GFbBiVc84" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاس‌گل‌هایی که ارزشش اندازه یک‌گل بوده
👀
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102633" target="_blank">📅 21:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102632">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=vRU554IqIuraZ3s6R1ZghHL4i0mR9PIM017-e3Z2bfrWnFq9gRp9RFBZOWtUt_5IJaP94oljIYYGp-zGFkDnhMWdBISMVNJoau3c8yleqZfHQSaaWbROpzvs9pLJeafbiOnh3pOkVo6qqjgIT8oLUUYQZoPmPzXJM_0ADNtd0ps6XzUTeDyaqPibxBn3zuL-AIXVLjTDix8JGH1dp-SkRkWje7zEX_l71oniJcBFQqFfSuj7qTafvxdno4Y-6okFXo9ucnnpabl6Z7WyDoua84bQs3eMcUXwpRWCwSm1SVItsGeTFAc2ptDyR0L2ktpGwBWBFbjUn4jO6-s27r2sIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=vRU554IqIuraZ3s6R1ZghHL4i0mR9PIM017-e3Z2bfrWnFq9gRp9RFBZOWtUt_5IJaP94oljIYYGp-zGFkDnhMWdBISMVNJoau3c8yleqZfHQSaaWbROpzvs9pLJeafbiOnh3pOkVo6qqjgIT8oLUUYQZoPmPzXJM_0ADNtd0ps6XzUTeDyaqPibxBn3zuL-AIXVLjTDix8JGH1dp-SkRkWje7zEX_l71oniJcBFQqFfSuj7qTafvxdno4Y-6okFXo9ucnnpabl6Z7WyDoua84bQs3eMcUXwpRWCwSm1SVItsGeTFAc2ptDyR0L2ktpGwBWBFbjUn4jO6-s27r2sIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فران تورس درباره آینده و باشگاه رویاییش: "میخوام خوشحال باشم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102632" target="_blank">📅 20:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102631">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRn9Zwurded4par3QENiQODDuEBbdTPBt6N5MN-WyYGz5si9tgoOOLTfvHtavxvRX1cLUKqz4vRVoUbwjIncxcla2iXPSvaPdKSProFb6r0UDfl3nzVUuwfRNke_t6hsAJ_-iQlttzOi2Ddd3J4IoJFETOQY6xJkQizN9PhSe4SxK8MYSofXWdzckU-qREh59rjE_Z7yrZl5YjHz-ysAFQ78MnbLWFNn_ZT8MqfuhygRgBKGFMKxc22xkkKdUGNxrhyoj5tD5atc4iNszR7BO824sxF-v3Ixcd6v5esM-7T0ngMYz0WA_Fd5s5ZM8920RD6glJPn_tMrBszYk4plSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
تلگراف|ترامپ تمام تلاشش رو میکنه تا جیانی اینفانتینو همچنان به عنوان رئیس فیفا به کارش ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102631" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102629">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3MSHLdEA93RxTZRq0k0OwRw64pmHCfntfS_cB8GzQdllWsHAxsfIgqsydAvqMb4WtuEp-38JZGOLVAe9HzsgYSyczClys2HF6W8Gztewc25_OBuWg9zRL-Tt_BMXLyhjWmrMJxULbav35C50gChw_LaXs5xez9xBjD4M1HQoR_gD-aUFToRgtBPLbZ76Se6CgJgDgq_79mgqoBTnWT3UAeTFUTzgi4wYhFXhsyoHbOrpqyeoSGy5BeivgJWp0Y7bbQLzePUcAaL6qQe2QmOFswaQAlMcRW-AvBhryqkuV5ILHwvT9qym042MmfDVmc2xT7HXGKwF51fRx2DMFsDsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQT9816BZr-y___1Zcl1Nv8owJg4TgzTJdm_12YJ1zOSzxMT3aq0eAdFn9r6DgOBug7d42XJE8e6Q1HQYyEf0h-4wBEsbOUBqxd4AXl-KMmhpo-I9RJMQBHmw0bC5KQ1eGaFLtXSBpm6-WmpMgEHGT75ac0smzcIQsIRWmqa5aEDISqucZdxjjMU6F55mfFXF7039BHFSjipsDMvuYB9C2Aog28KGoPQZQy0QroFmLTUvREw0pnydtjxtUwM_QLMj2ppNCK0hRxRo57NJdgOHK3rb44exNsr_y2TLyrKXR-M8yZ0yOmPXdW1tClkLnFOyFyJXUExMCnfdvUmShKeGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
حضور مودریک در تمرینات چلسی بعد از ۲۰ ماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102629" target="_blank">📅 20:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102628">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owx5XO6NMefhBIwQT-6zEs4rLexupecnmfet_0JqDODeyGwu_n-zZnEiWgTeYg5Z8FXCK1gKvE6mJbQatc0OtHi4CqJH_Tvk1nc49h_OPNL3xpwDpK8mAvN7PbGA2zXmNQcGcs6tVCP7y7Z_RHs9lOscypbcYhzizgtGSz_QT47DbRdtz548brvqfvrNOS72D9WRRwgGk3AS0HJilJE0iL0qMPI_WtbjIT_J-i3j8eLV5MnsbnRaQxd3vGIIRr-zBcYiAnEkYu2LQ1INeRGe_FYxrkz71r5Ljy2bBC-zKPBcjpWWM0PvGHCdwqDEhryH_OmBBWdkbecOVyUr54FBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فران تورس:
در حال حاضر با بارسا قرارداد دارم ولی تو دنیای فوتبال شما هیچوقت نمیدونید چه اتفاقی قراره رخ بده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102628" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102627">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590393501c.mp4?token=O8-GA1En4CCXxcxPsYa6OU9jwNXZ3yEpLuE-lvl2hcMjXmG_QqKiKhSVJyQspJtkaXpibNJV8y0fYdRI3ziVRUPmvMPAPjX5SZfBwfLoXyovfeIpAYRIGuheMsQu9E9r-3PT2OVfPoQLobJg4k9uouERaI0ovIHYJDqouzrRPy540KnwfyV7j_1IU-OdhYAAAWxG7vaxOrxeNSvcgOdHfSR_ph1Hhv5ucD0LEet3w3FO3Kaj4sg-XHVWCpG3F41WVhuvjTUsIrjyYJfVK6gRrm3yJpf2E7mDx8tmGAiHh5SiYncIIxCL5MyuIfjxfeBcCFCX4MWuzUp5jIKjMB-qag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590393501c.mp4?token=O8-GA1En4CCXxcxPsYa6OU9jwNXZ3yEpLuE-lvl2hcMjXmG_QqKiKhSVJyQspJtkaXpibNJV8y0fYdRI3ziVRUPmvMPAPjX5SZfBwfLoXyovfeIpAYRIGuheMsQu9E9r-3PT2OVfPoQLobJg4k9uouERaI0ovIHYJDqouzrRPy540KnwfyV7j_1IU-OdhYAAAWxG7vaxOrxeNSvcgOdHfSR_ph1Hhv5ucD0LEet3w3FO3Kaj4sg-XHVWCpG3F41WVhuvjTUsIrjyYJfVK6gRrm3yJpf2E7mDx8tmGAiHh5SiYncIIxCL5MyuIfjxfeBcCFCX4MWuzUp5jIKjMB-qag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلیچ: علی دایی مردمی هست، من مردمی نیستم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102627" target="_blank">📅 19:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102626">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pXyRH4BvmWjGQB_0vBf3MFFW9OJo4AVDnG0UgRZDjkicT2de07iSyh2Npec8j-DW9-xdv-WvwlFajkgKgprOAhqlIogOhQgUbKmAlqtFyC6SK4XRE_vpr7IlVHb8my5tl9Wkqdrad77Jz488EgLF_MU2d_PZRK8GkDga5z0SfY3Wo721oQ5MDu1PY7GfEgGCosSO99kO3nWBMXjD3QOzVqCISGPH-0DVVHX2f3tUQbutZWFZa4nfVQNwAzhtsXJAzdAe1Ex3ycZP1abvMIuFtWPqlteIJriiwwWBCw_bghrUISDfk_IYGIeoaYlKoIKb6kb44kW623LOvehA3iWC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
باشگاه لایپزیگ اعلام کرد که پیتر گولاشی، یکی از اسطوره‌های این تیم، به ویارئال پیوست.
این دروازه‌بان در 11 فصل با لایپزیگ حضور داشت:
- 362 بازی
- 117 مسابقه کلین‌شیت
• در سال 2016 با این تیم به بوندسلیگا صعود کرد.
• 2 بار قهرمان جام حذفی آلمان شد.
• 1 بار قهرمان سوپرجام آلمان شد.
• 3 بار بهترین دروازه‌بان بوندسلیگا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102626" target="_blank">📅 19:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102625">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQcQLUGi-Sr88dgpO_s0h2dNKiVzoM-SFk0tcZ8wqnup8yBYjlrMb89N5DMtlA6-5UVLVS31Tzz3yqfQpsNPTZ7N_S4i1psIlfTYeaVJx7PRWcs1nYpETrn92NVBb0_6yrrLDwNswSOGnZykAJlESpr59yiuH4druKRpQXm2m2Y-LxMNdCJOQTeqM8nWdWiCUOx8ww_2h-724GPh5T-5Su3vqjWhkY163KAKG6opujPqDdoGOe2ID-hEBE_uK2srS1JEP8x8-bmxXlfuoXeD-3vx8k_ZNM2tQsvYCBesRwq5CPY35ocnDdP4TQloGVMzVOGFXg6hN5M-8ygw7VPzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رونمایی رسمی چلسی از جردن هندرسون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102625" target="_blank">📅 19:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102624">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCAz7t4jTYD4buu1vpnvFphl5OYcOzqjZPgvcDFQoO7AZAn_mYSuSRnXJW40c8v9usD05q8C3ufdbZBkZDsjAnnG0WV0IDE1UCb-NzaeVPwUKUdFWCSNNMNnQeus2z_zkzz1LkLzBzgVjNEfFTBi_D4n8luokoxcMempvTrwnnbcFSIlKD3zc-DLGFvH6egYEkbCCy-Eu8Z7gR6T5d4zzzmbKx85SOzYDBDvLq-jfSr7OK-ePMBg_W5AVdMDGzCRGHOpZthcpdmc3FTDgy91HudEX-ddWhvI0ql3MMIfx8hYrdlY-Hzfzd-SImwEc0PIZq4UYpzsbnCCiiZtzt9UKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیاس یایسله به کمپ نیوکاسل رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102624" target="_blank">📅 18:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102623">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16357a3407.mp4?token=C37C8vCJSzt90cIP71pcsU8ap444z_GWXgCMftYz2XTVLXxk1bYHhypayyyeizrLJk6vuXcZge2IVumuB3TmnUuXIQUCYRNfY1aVBAwoTjlmIvSP4FQAycu9TYC0pkJKt9A3yh0klt4VzsQl_nNo6_wRcRGLKcOfi9M5LI3bYAj0XSHWKUBYJlyC5qIyw2mEDJo2MkREI-UIzpZrqm5KZJdhCuF_-r6odzq1vCwCLxLR6AyCYQW3OQxE7J6SOGyCWP3UeCoSdxWbr8eDGSbZeUdIWMerMuhtJAOMxguJdOhsQ2VAOlQN1RVRUJbhpYVA4Wtw-javw0xTAPbcgbSwRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16357a3407.mp4?token=C37C8vCJSzt90cIP71pcsU8ap444z_GWXgCMftYz2XTVLXxk1bYHhypayyyeizrLJk6vuXcZge2IVumuB3TmnUuXIQUCYRNfY1aVBAwoTjlmIvSP4FQAycu9TYC0pkJKt9A3yh0klt4VzsQl_nNo6_wRcRGLKcOfi9M5LI3bYAj0XSHWKUBYJlyC5qIyw2mEDJo2MkREI-UIzpZrqm5KZJdhCuF_-r6odzq1vCwCLxLR6AyCYQW3OQxE7J6SOGyCWP3UeCoSdxWbr8eDGSbZeUdIWMerMuhtJAOMxguJdOhsQ2VAOlQN1RVRUJbhpYVA4Wtw-javw0xTAPbcgbSwRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا فوتبال ایران بهمون یه ممد مایلی دیگه بدهکاره.
😂
یادش بخیر...
واقعا فاز عجیبی داشت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102623" target="_blank">📅 18:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102622">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ویدیویی از شعرخوانی یک جوان بلوچ در باب جنگ که حسابی در ایران ترکونده
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102622" target="_blank">📅 18:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102621">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkNiinbcPYZ_rOaFito8TLbXsr46DDfCRGwgT9m2rz0Ht4-9FHoA667EyVLbZKWaon-98DEpLFqg8uchfk_tkYJAXS6wNov8HBB9_qcCGYHU8QXZFYV2NpSAEwApK4MxSNG-gkkphfnRgNPd3iCAzsn4G-QtTAvWm7U8XAlWh8xXXhXbDRQ7spCohEHINOSYw9Jo28RgflFE_SejtQ8rjPeeDj4V0cqjA-DUAdChA26P7z6JM1gqPVUhVdFeDz3RD4_NNxZNN4qU4CpPeB4hccIXJZ5JJngeBGlQkUbjq4laVGzgDVjtBKYQ6VCSSE_i-lHJZcYQipsSFLlyxCgUCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مسابقات سوپر جام در ماه آگوست، پیش از آغاز فصل جدید لیگ‌های اروپایی:
🔥
🏆
• سوپر جام اروپا:
• [
⚽️
] پاریس‌سن ژرمن
🆚
استون ویلا [
⚽️
]
🏆
• جام خیریه انگلیس:
• [
⚽️
] آرسنال
🆚
منچستر سیتی [
⚽️
]
🏆
• سوپر جام فرانسه:
• [
⚽️
] پاریس‌سن ژرمن
🆚
لانس [
⚽️
]
🏆
• سوپر جام آلمان:
[
⚽️
] بایرن مونیخ
🆚
دورتموند [
⚽️
]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102621" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102620">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGpX75b1NzVo2kp34mjAh4poYnyiYlqE8M5LOiQ8o_LsD1zmm5Tbywz6lg3K7FYL2B5mGhlrORKgQqW8Iq64bfkGnRfr_9c9blEWlvzvcY5cQcm9PVVW7H5T2Za9AQSfq7gqPelgmjpcJjgL44GFk1JW5YmE1cCWeWymDMt2ADElBhHZWyvDvykmEDg1trnaDJeL6duN-C0yifADf1hC2YYl0YdxFVp6yD63xuxHE6P0DQwMZhrGj-jhTK1WFQuGp7CWKQ84yI2yRLAiUX7IHMPuB1epOj-QLggG14mG_m7aJzxUu-JLrNMOaqNcGljm1E0PiYS42ranMdxDQeAdNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
#فوووووری
از رومانو: چالوباه از چلسی به کومو با مبلغ ۳۰ میلیون یورو
HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102620" target="_blank">📅 17:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102619">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsNnekZguDNwxOevxp_tipOprIfRlXwM7E6vUkozKl_6gOGYGfF6rsSxPjVSiIqQ1SrH8srQEtjTWPnCEFVF0uPEIgHzWpqEE6HokrDyPCrCFlyVdXem0BJ4DTqB7ZDN4AAJvwk5HAfFm-XaNWEXt6xv3ewV-4qB5Y1i1JGqyLDcPnCTeJSy_J4MArZ0lpv6qXPT9vqAzMew5ua3ofSVv2NlM5-4KzKYBkIdSLhg1AJ-nIlhoQanH0Q0uS1ScD1JX7ijPpMPBcRphMk4uiE8eIeZN1eFAYn-NtvhyCZIR4Zkyxn-hy3czDEZEat-pviml8dbz-fyq6CeFWJbUjK_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پوچتینو تا پایان سال 2030 با تیم ملی آمریکا تمدید کرد و به کار خودش ادامه میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102619" target="_blank">📅 16:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102618">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سیوهای تاریخی گلر‌ها در دهه اخیر؛ پشماممم حقیقتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102618" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102617">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWtgpPjnxOJz7WnWoPCcxz9yKxwSwx3jZxq9WmNcl11yiRsUfRFuOYm8oQMKS75Jw8MkV3GPCEb8foVbiXGFOzUydTWTgONkUbCoiBTwWxxw0Xv7bvuMG59tFSL8oWzE8QuQGL4XZPdDvpx_o22TA9bLFP581bIWGadJ65IzJymj3lKG8Sw_1meAE6_eIS7qBXbRPtMM9h7WxPrlS4_l5AtMPhpjGCatqqLSVtDpwUKVXLyjcf_k3HtQspN0V8jBzNryDbnvXnFhE1WhHuaBTVF55oCC7le_8XLACe0K9CXFDHI10yJXXbYdmC4lzNXkDufesteN3-ZyVURRe1C9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیماریا:
بنظرم مسی تا هر وقت بخواد میتونه فوتبال بازی کنه، اون تو 39 سالگی نشون داد یکی از بهترین هاست و هیچ محدودیتی براش وجود نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102617" target="_blank">📅 16:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102616">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=V8GQXZ8G8zYrZ6TZZ5taPA41womLRuKpHojSsPAU7NKb7wU1LI5kCvWdkphcDLFMwQu32kjYBoh2hQie1T7MBIjXkAFOvO2HTe2PEcBU-4llgJZacpMtRdBj3aGWFU5XJwzVPwy_WKM0fDXO5bjzaA0IUY-_JNmQYaIS8ONpJ4Q0d6wEqRY3vILWJaNQ5XhlcvXFnxrwIMBpaYBCMEKX9NRlBhIsdk7D7C4J_w41RAO0UDU98vyxG-fMxcJVkIUhxQBGWg6bQfpjxbxFArg1fQQiNcGUbxyg8iV6AXVeUwRktVLnjCclG3e84IxBhFTVDfc_oXewBqu4ZsmpVu1-MIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=V8GQXZ8G8zYrZ6TZZ5taPA41womLRuKpHojSsPAU7NKb7wU1LI5kCvWdkphcDLFMwQu32kjYBoh2hQie1T7MBIjXkAFOvO2HTe2PEcBU-4llgJZacpMtRdBj3aGWFU5XJwzVPwy_WKM0fDXO5bjzaA0IUY-_JNmQYaIS8ONpJ4Q0d6wEqRY3vILWJaNQ5XhlcvXFnxrwIMBpaYBCMEKX9NRlBhIsdk7D7C4J_w41RAO0UDU98vyxG-fMxcJVkIUhxQBGWg6bQfpjxbxFArg1fQQiNcGUbxyg8iV6AXVeUwRktVLnjCclG3e84IxBhFTVDfc_oXewBqu4ZsmpVu1-MIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
بعد اینکه رونالدو و جورجینا با هم ازدواج کردن، ملت شروع کردن به ساخت مراسم عروسی با هوش مصنوعی ؛ از حق نگذریم این یکی خوب درومده
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102616" target="_blank">📅 15:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102615">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=lXToN1w69heKeSh5s5F0tD3zS6YHkpkci6Lg3v4K3nwciDbfYXWvUumXOvmyhE8ACTmfsvjBL4XpozOC5iCdzxsEDNYU1CpeOnrwy44i5fhoWArG-VWaMHMz32ez2KO6P3fT6zF3hr7dxAoYcXzCaJN-Ac7ZdoZcDs0sHqL14Oo7_ur5RLqTielgUz0m1RyrZVj11ox83y-SYak9pQDUQ6hg0PRGF_w-joxUUFIy2a-dabs7CTgjeWEQ-n1OX4A61f0_5TGpP0kIWUaBxTc_BAvBodMRkZviVu2bogn5ObdDKG4XobYTuf3oH5JAeiPuRZIqw0jzmW-96jvtGXTUHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=lXToN1w69heKeSh5s5F0tD3zS6YHkpkci6Lg3v4K3nwciDbfYXWvUumXOvmyhE8ACTmfsvjBL4XpozOC5iCdzxsEDNYU1CpeOnrwy44i5fhoWArG-VWaMHMz32ez2KO6P3fT6zF3hr7dxAoYcXzCaJN-Ac7ZdoZcDs0sHqL14Oo7_ur5RLqTielgUz0m1RyrZVj11ox83y-SYak9pQDUQ6hg0PRGF_w-joxUUFIy2a-dabs7CTgjeWEQ-n1OX4A61f0_5TGpP0kIWUaBxTc_BAvBodMRkZviVu2bogn5ObdDKG4XobYTuf3oH5JAeiPuRZIqw0jzmW-96jvtGXTUHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
یه قانون خیلی جالب فیزیکی تو فوتبال هست به اسم «اثر مگنوس»!
وقتی بازیکن به توپ چرخشی میزنه (مثلاً یه ضربه کات‌دار)، توپ تو هوا یه مسیر منحنی رو طی می‌کنه.
ماجرا از این قراره که چرخش توپ باعث می‌شه هوا دورش نامتقارن حرکت کنه. یه طرف توپ، هوا سریع‌تر می‌ره و فشار کمتر می‌شه، سمت دیگه هوا کندتره و فشار بیشتره. نتیجه؟ توپ به سمت فشار کمتر منحرف می‌شه و اون حرکت پیچ‌دار قشنگ رو می‌بینیم!
برای همینه که تو ضربات آزاد خوش‌گل (مثل شوتای دیوید بکام یا روبرتو کارلوس) توپ یه دفعه زاویه می‌گیره و دروازه‌بان رو غافلگیر می‌کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102615" target="_blank">📅 15:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102614">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=SF7pagt5BjfUKIpYn-JVLvxC7K5I1mimatc8OZuCA_p6j7AYCpAsv9W35Nd3H7uuKKlbT2pSXNhTULva8GoQuIUACvF10ep19a2F4e1N8Ahtv5ox-0vgbiEEkoOykictzpfeCZ-7Qy_MiF5whyTZNeFaO7os9CUjIoapkZRPzMEEatTL3K-HTZTnBM8W4KUCNv8lvVgQcvrtCSXO7vhhZGfv5ga6NE-C6u31iXFw6HW7OLdX7Y2tL-HFE7stNZMx75zoAwv3J_sytZ-1D5W15iwZ8mDk5xcoHuRJ8p0j1fuW5RbdhGLCJ9qGH8qDvWZ9k4TNsc6YUdRacPQ5I9eg2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=SF7pagt5BjfUKIpYn-JVLvxC7K5I1mimatc8OZuCA_p6j7AYCpAsv9W35Nd3H7uuKKlbT2pSXNhTULva8GoQuIUACvF10ep19a2F4e1N8Ahtv5ox-0vgbiEEkoOykictzpfeCZ-7Qy_MiF5whyTZNeFaO7os9CUjIoapkZRPzMEEatTL3K-HTZTnBM8W4KUCNv8lvVgQcvrtCSXO7vhhZGfv5ga6NE-C6u31iXFw6HW7OLdX7Y2tL-HFE7stNZMx75zoAwv3J_sytZ-1D5W15iwZ8mDk5xcoHuRJ8p0j1fuW5RbdhGLCJ9qGH8qDvWZ9k4TNsc6YUdRacPQ5I9eg2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خولیان آلوارز همچنان در رویای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102614" target="_blank">📅 15:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102613">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2HUmLEpa42nFAZXnqSWrg9veYelRaFAEACvL5q17K-EIcNDbJ5i_Kmyf-P01fFyG9xkPMtIb4gWSS0pB4GYdLrDbIptaRBTzuMNKYxVasn954nDDQhJc7Kn_djX-JuQqWFdkDwGB45dffPcPPPzl-aWh-UVUnBO_0yCd581_-E7-CQtGrbIZX5MhixVNhtmFXGAN4lkf3E2VeOEC_NanJIctPv2GKRkdBInd9oUNNlgo8Kq-1vIlgZab5muVUb1Orn3i93EH0gOxOJXh-UaMSyPQy5l0abEmkU2u5xbSlc8XLdN-kM_ffjWerbcnZdzk2CYbgJXsxgsCvy4Ujcw6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
استقبال هوادارای کولو کولو از ووزینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102613" target="_blank">📅 14:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102612">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJFGQr5G7Y69U4f27ezGfP3V-xnfjAIcEOuWsn2NJp9I1TWhE59jwqkYJARe1LA2txU9Ah7Fqssq0S5vJixKk-7Cwg9LksWHAnqlmLM9Dpr8DwiwqCWr0DhLtWiRlXl83hwbuMZWZgCWAp3cGHpRmv98kgJ3UcGJhUMv-lcSQ4R16b38YMSqTCvCGjAG6iYrod5d5-9i-3v1VblFdAcQ2y5kbckQL2E22LH_8Y17tOhpvN-EEkuqtf78rY3lDx6D81k29DplbqIHMvRl7HinwIwMjx2Y4stXvSrBL_qzoV7mzL47Fj3RrIX4OnvXwy6-J42wzjmpNIZc9bG3gMPMdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
مودریک رسید به هنگ کنگ تا تو تمرینات چلسی برای فصل جدید شرکت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102612" target="_blank">📅 14:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102610">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVjmKYzYiCSc2zbByE-NZ8NJo3iPOqpb_UgG-VVX1A4QmAyXJVkASSz-KlJH3hajH7LAP5j2NXnikE9vW8IH10SQ5k4ZL2nrB8qIohKel7UfQp9H-gAS1CU7KcpLFoMbNEz8yhjCg3F4CZwe1seLNY-TsDClU4KUBVNUoRGJ1N3hDyRxY54QxHPna2tg29SEe7PWuaB6QEwvLpcdVW9KbAJdOcl10eWuJLMwKNNwxwbgsLD03KEFyi1YwMdHTi2btx9o--ox_P_ux2cjh0DCRVWGo3OWv63eIFK1-aViYA-8J_OBxJibAXomyM8AtzgrmOcAZy4a9vWKOT2jOCjqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ATlefXd6nFHm7kEKpXB2iJF-XLDJfSfvWjjVCyPMZQ81ey-rPTT34ZpnoPRYOAxVCJpWhx0CztxcQ-2baphQhCbj5_WvsH35fiOmBtI8xG6C_jZwK8FRqmvvrer-crWoQb7aZxCLpUi3ayHOMiz_WRnH1oIhKrFD4kPdW2BQF0hKdc6feDhQcI_vsObWC4vaKIaLYgSu8XBiirOhVdUdhpSu20dpb5B1n_sotv6IA8eHlvJTYXZKTFA2TNJY0es9QmRpFmCPTof57rHeMQrrMjEqLHtONxvp2d70S6LQwbIqFwx65MGRreIYDqvZgc95qEq9OBgyiGC-uDDr8fZf9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینا کامنتای زیر پست بنز و پورشه نیست؛ کامنتا برای خرید پلی استیشنه‌
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102610" target="_blank">📅 13:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102609">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=O_q4ttACCYacqjYtNv0g4mwqzWxdxDR81xZoXEP0AWgXIuQnsgDIRj92WKxbyj0v17kW35VvldFtl7JmTpuLDlOfxEjTMAshw83KWOMf0doN4BvlkZwSqrFvZ6Lu9F8hzMVfBp489odha5Ok7qK_-jnrryS2sHI_Gz_CVACo9CfaZuyaH-7FPFdrmNdpg9X6jNAiLa3qVvA7QO1uanb8LN9irHZgwmD6MQ-QEAVMbfJCYWJcyts2o7WR4MQovrfZ0VFAeoUKY9zyuFAOvPfaIcANcGQr6HZRCeScfL8nZ40dyOggvsqtUZqu0HP_UfMySsCiNGcMWmenmUaon-4EKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=O_q4ttACCYacqjYtNv0g4mwqzWxdxDR81xZoXEP0AWgXIuQnsgDIRj92WKxbyj0v17kW35VvldFtl7JmTpuLDlOfxEjTMAshw83KWOMf0doN4BvlkZwSqrFvZ6Lu9F8hzMVfBp489odha5Ok7qK_-jnrryS2sHI_Gz_CVACo9CfaZuyaH-7FPFdrmNdpg9X6jNAiLa3qVvA7QO1uanb8LN9irHZgwmD6MQ-QEAVMbfJCYWJcyts2o7WR4MQovrfZ0VFAeoUKY9zyuFAOvPfaIcANcGQr6HZRCeScfL8nZ40dyOggvsqtUZqu0HP_UfMySsCiNGcMWmenmUaon-4EKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد ریدمان دومفریس در بازی اول با رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102609" target="_blank">📅 13:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102608">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvfjuC8twTjV38BjXKrHcltd4mNjGDeHA_rs_s2zfa_E6Q_VbAfU4aFIdpnQ_mUIskNSP3IVmdg4X4CVM0afB7vngxnlOP85x1cjKjBdK_qmxJMdKlY8fA05hQ2bFavh7QkIjIjMv5HPxhSOD3lTf-2cMFt55aEje9gmRNOCZsgHmcnTvF5PKnC2dnYg3JhLkSPoKOuh6J5VBpN_6jsQlahwF200JuieEqxRDMp1uZrfaVj1RSMnsuWYJ4VJzPdaVNaxe_tMVMeTTkHDLSUIS2lMxLHcmDJd6jTR5lS8XswutwiFLmKe5-vPtRqxCDK8XCFOLso7MvW7xcr7VPfqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس بعد از کلی خوشگذرونی تو تستهای پزشکی رئال شرکت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102608" target="_blank">📅 12:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102607">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=KlvKyzfkQHjorCVz1C9l5EsecH2xWFPGIt-zHJYALixPFiGZG-WmETuuDbUu0pYQP2z1rMgZRHmLzFikK7OI87sYp8df4pDyPPfTP_Ufg0h73WSHPOHcK0QwCWzbPOjUP5FrUDwBrlsmyOvQNmdjLQ-IN1BpgsPIjGw_rAtv3WP2b-kTb-Rm900XK5ycA330hMx7oK-jn4cuHTfVhCgybEYtiwhuq6-d5_70XFvcQWuNRHcDgmQ612NM3fjeTa3bcjyIXhcE0u4PV2NtXi2z9dKNEwFBa0l1TUCVP1ee7F7RVfzllSQGg3OMWEJqGSlp6_hIYx7p3N2S3ABlv-Mr7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=KlvKyzfkQHjorCVz1C9l5EsecH2xWFPGIt-zHJYALixPFiGZG-WmETuuDbUu0pYQP2z1rMgZRHmLzFikK7OI87sYp8df4pDyPPfTP_Ufg0h73WSHPOHcK0QwCWzbPOjUP5FrUDwBrlsmyOvQNmdjLQ-IN1BpgsPIjGw_rAtv3WP2b-kTb-Rm900XK5ycA330hMx7oK-jn4cuHTfVhCgybEYtiwhuq6-d5_70XFvcQWuNRHcDgmQ612NM3fjeTa3bcjyIXhcE0u4PV2NtXi2z9dKNEwFBa0l1TUCVP1ee7F7RVfzllSQGg3OMWEJqGSlp6_hIYx7p3N2S3ABlv-Mr7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
انتقادات شدید و عجیب وحید قلیچ: چرا تارتار منو دستیار خودش نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102607" target="_blank">📅 12:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102606">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzL95mPPGzYhLsfWQFuHe1ZWnRAm7-RrIpbjJqgP1rZkkX-eZAz4jvmT6bn7KBqULl1pXB0wU3xp4vgSYR6HQPbWsyBihp_Qtt76Y6iglD5N5pDaF4p305j-V6a2LPtih6oLqCj2HcCoZcNkTi8DbmpPUx-4f8acr2-IeN1hNOOcsWk5sKTaMoTdw6xvFylqjzoVhqB2kG5GVxKEfQzAVy4b7JUSMKeFZjqkW3en03VDXqAMj489Y823zApbmbKz0VvS4kFeEddhxZXmgZhxt-RlfESxdJgj5_NBd0C5c0C297q0T2YP1C0MqyeHmgVJJgBlue6WKgiIqh7SgJ_rUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⭕️
باشگاه‌استقلال اعلام کرد که فیفا در نامه‌ای تاکید کرده که یاسر‌آسانی فسخ قرارداد خود را در پرتال فیفا ثبت‌نکرده و این بازیکن مشکلی برای همراهی استقلال در فصل‌جدید ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102606" target="_blank">📅 12:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102605">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=Kh1IjmGfEkem9-7cczdJMX590I6LL9WlNmlWT5cj1NAq5v1-kHhGN9VefWoissq_ANGjs5PXo3vEZGp-vADWR6xK6TyIkbTaHigv35SYq4rwrFooffJcxIakpySNA8Qj2fbZTrZ7PDRG-h0slfSeHZpAOXP97VoBfT5GH6H1D5amoeKX_79kVOD1RnAIhjFSHHUC0jrL1Egk0SbXUSOnkgKKa7ajRgcT1UfXlDz-HdUcbStCJOHYMNwwiq_wOisx0HoCV8RVQS5RvfwGw9zDw6lcDJLE27Y6dq1oHP1iva5vUBM2nHWDCbR9iCFvyZF7UaEef_l7925m1xWCaj52lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=Kh1IjmGfEkem9-7cczdJMX590I6LL9WlNmlWT5cj1NAq5v1-kHhGN9VefWoissq_ANGjs5PXo3vEZGp-vADWR6xK6TyIkbTaHigv35SYq4rwrFooffJcxIakpySNA8Qj2fbZTrZ7PDRG-h0slfSeHZpAOXP97VoBfT5GH6H1D5amoeKX_79kVOD1RnAIhjFSHHUC0jrL1Egk0SbXUSOnkgKKa7ajRgcT1UfXlDz-HdUcbStCJOHYMNwwiq_wOisx0HoCV8RVQS5RvfwGw9zDw6lcDJLE27Y6dq1oHP1iva5vUBM2nHWDCbR9iCFvyZF7UaEef_l7925m1xWCaj52lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این عالیه از دستش ندید
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102605" target="_blank">📅 12:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102604">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=ERJHavC8LZ4nFm-HwCkzrITiKfzg2Z2C66swBqIowKPcX9i6Y9i8PE3v5u4-iPl-vAvsVt5chcPYGzsB9tXCbbojxQB8gdQ05kS1y2hKb6L6xhez-VcJyP3XQ8R47HLcNVFCl6m94OpmBSN_wMM8faxqyP0A2zmW5vIKUUWWejqJnjcECz2IsiLE5_utJ7TLGfPOESMDdrR83Ebi-SazuCPDldrBzAkWqejKEy_HTN0bCPCfdLj2awFsV466HcOegxO8RRydKOnPv87gxgjWPh9XuquINZc1vI5z7hfvBzpJMZB2Y7-_d2bqWLvGvoDtyPVrG3UAVONLQhf3A2CnVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=ERJHavC8LZ4nFm-HwCkzrITiKfzg2Z2C66swBqIowKPcX9i6Y9i8PE3v5u4-iPl-vAvsVt5chcPYGzsB9tXCbbojxQB8gdQ05kS1y2hKb6L6xhez-VcJyP3XQ8R47HLcNVFCl6m94OpmBSN_wMM8faxqyP0A2zmW5vIKUUWWejqJnjcECz2IsiLE5_utJ7TLGfPOESMDdrR83Ebi-SazuCPDldrBzAkWqejKEy_HTN0bCPCfdLj2awFsV466HcOegxO8RRydKOnPv87gxgjWPh9XuquINZc1vI5z7hfvBzpJMZB2Y7-_d2bqWLvGvoDtyPVrG3UAVONLQhf3A2CnVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
مورینیو رئال امسال رو نجات خواهد داد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102604" target="_blank">📅 12:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102603">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyyzfG7_7fSr21I2BytNQvfMmputyodIEyAbRQ9m3USJNMTIDmPcI58p7tb7oKkukmVnvvEFG4lEx0S24Z5swS8x0_zFlyWkTYY5_cMytJmV84JLcTNmAdmnPjOgVqhch42H_iZFtMANHRGAA_PuJ_WQHneIAG7iUixRbxAd8Gj836oCoz7dYOFTTTbPPojma4LTwB5VjsBYJhpuaxlIUrQHT1_j4RApX7U8FJb9gVNgC06O9nfZBIDrwflNWB5ETL9jzbfJW_ZaxJeJr4gxZ36PCWrHSlUU_fJAtf5IQ4RDYdocA01K1_oGzzcYsSDC3VH-SlvGI9yKTG-zk9FXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معجزه فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102603" target="_blank">📅 11:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102600">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVP3qBhEuFHJw1tmdWfo3-BAtC-v749G-ICVtdnMTqWN2Mhk3rU4unRu1NO2gS5Z-3woWk3Szq5_IqqcU5tcViG_cBVcmpEhWunaNOxNf6-74SUXjXKbeeFhNDUOwkdFT32IeKXgKCbvmKG5NfLB1y9LTB0OmTI6oo5cSb8S1PgwbFXfQAFXZefOALIpahW6S1hE1yruAz0x9tiXNqXf8TX1JRxRCS8v1rTTVkvguPWBBWBJn69X94oHhMncJECenqSLvEt6kmqZ2rh8-GPN50z5JNpviRJBEhdWcDQGo3P4JkwLwNR9Xgnet-A_5fPc6CaBlPavQ99cXjpGDdD2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1qleVV503zF17NHg923UcW0ovoGAvNOkG_hnEQCOdl43EgQzUJCrO3F-UvwAaDt9VOfwq9iUBma4CKPCK1vojFPDHDKRHWMO1WMtlbWGO8_Va6qn6owweIhI1fxWouePtbX2GhQr2nF_NpozdEDQM-c-wjluURQ96PQwZx5Gt3CUJjdBnyv1EBCd0P6lCtNvyhwixEfFRQu_-8PPmJEO-TBhkKWbKm5MxmBNRlltEZ7aJ9tbnogQJ782PustDjQWJfwwaOkb68ExkuUXKucWqkiHrN0PRLCZe9EifwydHXovA1R9nlE6e0fu8FH3c_qb-l0aBZ2lWOr9nJfhTpBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLbK_0reQ--LuyWF94OvXfc9xLX6QpMkzJaEhXoj1OL9tyKNs7nDoUIkBob5sAPOozwIylc2cd0bPnvryoZmcR_z2-7HhGvrB8vXV6YSilndNsECvx1nFqJxjyJ3bY0RJCOAD7FysqV57SsWv5X6iQo3WTxEVvW4__2QeJ9QKTH97u2jGuXbHDTjnpc7rfoPqSIfoVgyE9zHmWj4i5JG9s2Vqt1k3ICXV4GralrJSKIbkYK4ZlrEXEte6gE_W_dsKUcQexzuZ2kfyrdmUag6uCdc-rG-rAg0BefNFXKo2gjFdiIAjoK6qTCPSxP-URSZj76Qg0Ie1QStCiAsJeWYBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⚽️
کیت
‌سوم فصل‌آینده آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102600" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102599">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv9ciCdr35efEW4EAKKXywPxu5VXDi_q2E5VIT0htDgfMhdcTLqLmy0tV7dhyxiW-6UaceAwd-8gJtlEFDWjDfERkoPDbg5gWE-dKic2VCgMZgaucIJX493_8jge3-PHUyUUw8glteo8s5fHrxtuDgunX9RZo7n0sThBuRidEOe4ZCJpMmic4CSgFCz92vdFlBwOQdO7DSj1C-CdXvRZ3v-LFDfmEkSrRbUITRTmYwHWX66CUZOAVX1l2GHaNrIanMhXkycJ4D-icE8AjhcrhYFVYaHUzH5t64u2hvyW13A1AlBEkWyA3ICNtI9JTpHKG0CZ8GLgLy1H6uLrklCEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی منچسترسیتی از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102599" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102598">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkQcb5rJdg7Dwewc33xnsqWxhUwzoCZ2DhPVJQDgheenRU3A-L9viHsyn2H0Eiw-3ld4XiAuEIVJYG15FtNnku4Dez0NQSwPoMF7mp_ccU3rajiX8rvje6iKDJ6ccphY6y5CCqRXwafSgh5il5VPO9kvWAKveIN4lpOBoETpBhhkVDddf7-yzMALmHPiY8-0jhQxZmBWYaz32UslYAwLOv1JpRMgNq1wyhGMwoymVsm20OcYVvxx-Aw_X4p91OG0kMa1DJ2UA4b1KbriPZlxPb4KGM8o6dD3OasgtFYOFpDnXHHasYlS0PX0DFPXxpW3AjsE4VvCBw0ERK_JEUVN7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
لاپورتا از جذب گوردون و آدیمی کاملا راضیه و اگه آلوارزو جذب نکنن، عجله ای برای خرید نداره و ممکنه بازیکنی نخره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102598" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102597">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=oF5mY-CuNVVE725DLcp3VGaIwrkv0vHJR6m9QjVQ42_UwbLE2YyJ8gBBzcLqZEvjBrl1dBiqFoKBbBGTfrRKhMQtz7Q1VxBoy-ktbpGYzbmgaB3GAqOkDiW2ugwIs2OjF7nduePkxjX3MpVH1zFx7act3wUED00OmTZykJeTQAE1ZWA8rSxrnRhgfwSW4wZ9O_TUXoGI_l7oaPiDFEwjo5hNCMjH9WF3NvYShgz3FjzmUpwmGwsP8S4DjpQY4hse2RdLLNFqFn5uld5pAJiGIaVDaPFCqzFN7Ljqu_L3XfqN9eeoIuES3OwSWbw1rDgyVA4cNlnMkjs56bR-kjEf0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=oF5mY-CuNVVE725DLcp3VGaIwrkv0vHJR6m9QjVQ42_UwbLE2YyJ8gBBzcLqZEvjBrl1dBiqFoKBbBGTfrRKhMQtz7Q1VxBoy-ktbpGYzbmgaB3GAqOkDiW2ugwIs2OjF7nduePkxjX3MpVH1zFx7act3wUED00OmTZykJeTQAE1ZWA8rSxrnRhgfwSW4wZ9O_TUXoGI_l7oaPiDFEwjo5hNCMjH9WF3NvYShgz3FjzmUpwmGwsP8S4DjpQY4hse2RdLLNFqFn5uld5pAJiGIaVDaPFCqzFN7Ljqu_L3XfqN9eeoIuES3OwSWbw1rDgyVA4cNlnMkjs56bR-kjEf0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از رالی‌های جذاب و تاریخی در مسابقات امسال لیگ‌ملت‌های والیبال ببینیم
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102597" target="_blank">📅 10:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102596">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=RdJBwMyhVPdx6MOSJUIjwCZtEXWFykrj0kQljnssVL5i_CGq3Rl_YIof__elUguLtPEfi9nHjLealg5m6_LaHfS44sDfM6sGrRVUTje-xS0avw4CPX5ZuICfvrSUDFGablZDWZsUBqwPot8KqI0c2OlC__C8fmvyiqUWhuFv2Nu9os9XPT-C9rlEPzz_-LM-kxDDMiOFwrNa12y-aTAEAx8ZUV5z1HVzn0JFmv7YHNgpVbGl4kg8egLIaBgVLjUn6Toc1B3uWlwFQLCDn_VIXIkfmG5U-8wZ3leiekb06EcGKIVFD4AWQuA0E6XB6aru_iQfs2WuJIkG5BF-4V_RTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=RdJBwMyhVPdx6MOSJUIjwCZtEXWFykrj0kQljnssVL5i_CGq3Rl_YIof__elUguLtPEfi9nHjLealg5m6_LaHfS44sDfM6sGrRVUTje-xS0avw4CPX5ZuICfvrSUDFGablZDWZsUBqwPot8KqI0c2OlC__C8fmvyiqUWhuFv2Nu9os9XPT-C9rlEPzz_-LM-kxDDMiOFwrNa12y-aTAEAx8ZUV5z1HVzn0JFmv7YHNgpVbGl4kg8egLIaBgVLjUn6Toc1B3uWlwFQLCDn_VIXIkfmG5U-8wZ3leiekb06EcGKIVFD4AWQuA0E6XB6aru_iQfs2WuJIkG5BF-4V_RTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به‌بهانه مراسم عروسی اسطوره رونالدو
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102596" target="_blank">📅 09:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102595">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=njpmUyKvPKWiAKdv1jF90Qie56-9QmuneFbx-vYvgdBl97XOsx3csUj2G-xragUnnIYYdyKz4DbTPc5gCbYGeeoBsebM5o32MYh0QXHnkJ2Ix0DWY-sJeA7J04q1FXpbWBFYcDgpveke7Nic5I_zpBPnpFu0zV_6gVOpARTaHsfvR9BiLtPL0-TtcZyYgIAt8F6_UkdhUEuVWwnEHAlK9deeJ5QbmRY7HRwlCsDOiH5P80O-n3NHXkmPEQJ5GokQvA6A90AU0gzklQ4fDWNJlDTEDbX101qzVA-7o7GI_FbbTJARMwLrKp_tT3MFmNxoIg3YgjJLaDU9nYdfB1_BsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=njpmUyKvPKWiAKdv1jF90Qie56-9QmuneFbx-vYvgdBl97XOsx3csUj2G-xragUnnIYYdyKz4DbTPc5gCbYGeeoBsebM5o32MYh0QXHnkJ2Ix0DWY-sJeA7J04q1FXpbWBFYcDgpveke7Nic5I_zpBPnpFu0zV_6gVOpARTaHsfvR9BiLtPL0-TtcZyYgIAt8F6_UkdhUEuVWwnEHAlK9deeJ5QbmRY7HRwlCsDOiH5P80O-n3NHXkmPEQJ5GokQvA6A90AU0gzklQ4fDWNJlDTEDbX101qzVA-7o7GI_FbbTJARMwLrKp_tT3MFmNxoIg3YgjJLaDU9nYdfB1_BsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیزا بنظرم از معدود بازیکن‌های این نسل نه‌ چندان درخشان ایتالیا بود که توان رد کردن یک در برابر یک رو خیلی خوب داشت و حتی به جرات میشه گفت قهرمانی آتزوری در یورو ۲۰۲۰ هم بیشتر بخاطر عملکرد درخشان اون تو خط حمله آتزوری بود تا چیزهای دیگه!
خلاصه که واقعاً حیف شد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102595" target="_blank">📅 09:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102594">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=iom4TKoOCXR44HzwO1YmLHddw6dD0b3yLwMHBjhaXisfuosRU_Xd6DXeMukILm1miPzNyqAog_wfB4v041J3JwrY1I-lSORUVgX4p5p7JInGuFCe6ZDziEFzmi1HTNsfdKElB8lBoypTu7WanBS_xqUqAPxnHuMMa11RYZTYGvDj62gW_Vj3-fTitOugXNPJZr_CkJFHR4Z86nbflANWL9TOQVwX9JYigdJSKIisEE6L-5hTENAA2X_C0PyAbKszqdN1S5T5cKF0p9JcFxW6x7Vq_IF0HiU51vA5Ls1Ly-9fL-_ewyLU7fbLwZAqjeTJXhht5ByeEM2VfoQJzjDd-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=iom4TKoOCXR44HzwO1YmLHddw6dD0b3yLwMHBjhaXisfuosRU_Xd6DXeMukILm1miPzNyqAog_wfB4v041J3JwrY1I-lSORUVgX4p5p7JInGuFCe6ZDziEFzmi1HTNsfdKElB8lBoypTu7WanBS_xqUqAPxnHuMMa11RYZTYGvDj62gW_Vj3-fTitOugXNPJZr_CkJFHR4Z86nbflANWL9TOQVwX9JYigdJSKIisEE6L-5hTENAA2X_C0PyAbKszqdN1S5T5cKF0p9JcFxW6x7Vq_IF0HiU51vA5Ls1Ly-9fL-_ewyLU7fbLwZAqjeTJXhht5ByeEM2VfoQJzjDd-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
👍
نوستالژی از رقابت مردان آهنین سال ۱۳۹۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102594" target="_blank">📅 09:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102593">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGNaiNHjSCpeDh-8hT3senb31FYo9CN11rqE6WG24nDQPgOA_qndAuwtDYO0kJvf5L01JhEk41A5KS-Mc2hETWTBni4kylPgQOOJb2qhL88Kp0QyWT6Vi34cRWs6fM3RXa35gFNHDUdn-j9PJfgiXiWFDRudAcW76lC69nHkcCMH1AWq4KG9y8zySaShVmAB6BNwdFgexMSDJnwJw-1PUE2rX9jfGUZt7dZp58fG4sVLOkSGESWmpUMrIsFuX4LM_Cy7-Ux-6vG0RTbHm7_TlxfX_VXNsMcxZQFT8Z03sDfasN2kiTFcfCYCspBuWmSO3xXPPA33AG80hjtIi-wpKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏آمار تولد در سال ۱۴۰۴ با ثبت ۸۹۲ هزار تولد
به کمترین مقدار در ۷۰ سال اخیر رسید
، ۱۰ درصد کمتر از پارسالی که توش رکورد جدید کاهش ثبت شده بود، ازدواج هم به نسبت سال ۱۴۰۱ حدود ۳۰٪ کاهش داشته، به نظر خرد جمعی ایرانیان داره تصمیم درستی تو این اقلیم و شرایط میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102593" target="_blank">📅 03:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102592">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-Lziz_YhlgNhiMRDJLZjYCTSxHOV2v9zDY9E0r4jAEBpaQAnL8s1_CXmqLFhg2B34s5FpDrPN0192FIEi2NNDXoHItxm4S8MeyWiPYTuE5MeGNstF8zXatMItfkYOJ0CXW35Gb8PWzt9oM320W281cpzb7gTeSBuZ-IJBNBOGOemJt9aYGhFnRMquj_2tZXExzmcovd7LNE5Mbl6xdXjX_CYY95C9dJwpagvBT67a17i9XI9Xgw6G7tcbABVF6fx2F3oimwur0kb-46NmDOTCn6rt1OfE3p621WVMGF3pzguBkOv_0Y0we4L2QsotEQcZFGiumXzw1gVTW0f1gPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
نشریه SER: باشگاه بارسلونا پیگیر جذب رودری ستاره منچسترسیتی شده و اگر این بازیکن تمایل نشون بده، اولین پیشنهاد رسمی قراره بزودی ارسال بشه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102592" target="_blank">📅 02:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102591">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی لیورپول 2-4 لیدز یونایتد با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102591" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102590">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش جنجالی پرسپولیسی میشود؟؟؟ خرید جدید پرسپولیس درحال نهایی شدن Tic Tac
⌛️
⌛️
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102590" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102589">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGx48l-5hKgylptRaDYF8pELwZrOqNFHGw7KcuX7KJ066OgCYKL_h-4TtpkuKlur_ldZgWIybrQzIjBPcSr-1ptM6fhXCZ_HTPv9ELDEovBzkGBqhSgf1UYUbymWFJI4peHBTmAUYGq3_OlLlvKdM4Ooq9cuCMtm4rCoHgRhBBZvCp7UJxb-xWZ9PMVH5ONZXM_Eoc4q6lfCgXiQxX-6zqeguoEByA3yedfGZNFD3ihHvQVTgcO3P-DE3Uodi7RsKgm3Gl5pDzt6BkvfeQzHR9JiuNo9oa36t-6WTF2JIcc49kSr6YomLDDkYnZa1QKGaI0DLF3jMo4wpF4M1fLtiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
۹ سال پیش در چنین روزی؛
🔼
💸
گران‌ترین خرید تاریخ نقل و انتقالات رقم خورد!
👀
🇫🇷
نیمار با مبلغ خیره‌کننده ۲۲۲ میلیون یورو
از بارسلونا به پاری‌سن‌ژرمن پیوست
؛ انتقالی که تا به الان گران‌ترین خرید تاریخ فوتبال به شمار می‌رود!
📈
عملکرد ستاره برزیلی در پاری‌سن‌ژرمن:
۱۷۳ بازی
🎁
۱۱۸ گل
🅰️
۷۰ پاس گل
🏆
۱۳ جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102589" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102588">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=XAwZQ1in_579KPywC3aOMQSuzMGj5x4vMkWgAAfbvfcMq6jbME71B7wr-sh9-WTAXbxp5KwNtlr2mstIggRfdJYCozFQ6Xta1cPTEVaWD8JQhBgKgxwtHBnpXt4mpBF_qATRN__JyGFdJoy1BACJHBr378h4SOF3KAhImb6jEg9lWMvZE6K93OhCVitI1OPKiz4wmE0hFA0ojb96RKn23vHdrM6ouAaUykHEJPgaU2htMNtuweMkI7wrbDEMxf5TgxSqm9rHi3r-0SU13wuWai2Ho3EkGxX3Z6yUsQVy4B7fwhosttbGa3dFKttvbfLlfgedEl1Ogdq8jfspnh5pKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=XAwZQ1in_579KPywC3aOMQSuzMGj5x4vMkWgAAfbvfcMq6jbME71B7wr-sh9-WTAXbxp5KwNtlr2mstIggRfdJYCozFQ6Xta1cPTEVaWD8JQhBgKgxwtHBnpXt4mpBF_qATRN__JyGFdJoy1BACJHBr378h4SOF3KAhImb6jEg9lWMvZE6K93OhCVitI1OPKiz4wmE0hFA0ojb96RKn23vHdrM6ouAaUykHEJPgaU2htMNtuweMkI7wrbDEMxf5TgxSqm9rHi3r-0SU13wuWai2Ho3EkGxX3Z6yUsQVy4B7fwhosttbGa3dFKttvbfLlfgedEl1Ogdq8jfspnh5pKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای انجام شود که بزرگ‌ترین حمله از زمان جنگ جهانی دوم بود.
این حمله برای آن‌ها فاجعه‌بار می‌شد و به همین دلیل نمی‌خواستند ما آن را انجام دهیم.صادقانه بگویم، عربستان سعودی هم چنین حمله‌ای را نمی‌خواست؛ زیرا معتقد بود توافق بسیار نزدیک است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102588" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102587">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=QuMFTaW3FPuOHmdiZqEjrYiV3mYsJu_uJ2kFUvZIteINGZequ3SnUYXck7yH8zCFOri9xbQN2_pP9oLZukpuhFo6YB5r89SSkypNX53dWXXe67z12c_wvgN-19T54b0FCAUlktXtIohl7_0g7anlPmhZXMCgAFDnak5xQ7mxSqqmZoXV5XSBhwv6g1Rx1iaHBcIokIBqaEcxM09iDryBCz7p2nQaf0NESE4MriKhAq6wA8VkuAoHUAUzhdrJEO68WG1HWyyHn8BAseJgNOvyC6fTqLMk7jTpqE6__LE8rigtGF7JQ28fOhpHPQYNx6WqgA9C_9cDZCO_LqahqjPOqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=QuMFTaW3FPuOHmdiZqEjrYiV3mYsJu_uJ2kFUvZIteINGZequ3SnUYXck7yH8zCFOri9xbQN2_pP9oLZukpuhFo6YB5r89SSkypNX53dWXXe67z12c_wvgN-19T54b0FCAUlktXtIohl7_0g7anlPmhZXMCgAFDnak5xQ7mxSqqmZoXV5XSBhwv6g1Rx1iaHBcIokIBqaEcxM09iDryBCz7p2nQaf0NESE4MriKhAq6wA8VkuAoHUAUzhdrJEO68WG1HWyyHn8BAseJgNOvyC6fTqLMk7jTpqE6__LE8rigtGF7JQ28fOhpHPQYNx6WqgA9C_9cDZCO_LqahqjPOqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌خوشکل لیورپول در بازی امشب با لیدز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102587" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102586">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bh41hFE4fjLh_U5BlgHCDFe9Wiw2fvCLYDe9u5N15ykxR20QYTu_-pJ_G7q5cAY5ZD03muNKFKyUt4SKAC0I9LNIwmm5S3PX9R1aezFe5UMO2z-W9xhffGSzaEsJ9GdZ2ebsArhuPT6RXkJaWT7Y2i-Is6WUY9nG_30snqGyo-ODhGqaIgONM6zG1P0e64EW3aXJmHbt-aqyVW7nd-9BqzlGcWuDvjho4U02R2Y4UMZQVrXQkjsv_8JYjZeIG4x1VRtxRGXung3KZpe8sMSw5MLrS_1-frMoYBgXbW1QHnltcI6Q4FV0JKUFEpzo8e5Y7luX_w3XVSH_DE6NmiOYeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است بزودی مذاکرات نهایی باشگاه پرسپولیس با باشگاه</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102586" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102585">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBirXHJQmL_ljqnm6CwkrlRSIuAwRCUPOxgsyKFkQcNv0QM2y_9JP3y0pNqS4yIcYtuJ3If1J3_9WE-CMvhpuY1Ze55xHYbI40WKi_RtcMjSR_JSdt3wfxZ9i0erEp_DZrtyCrUKISf4h_pFKnn60pdeBUsVEe4MQk-QYIFmZXYnnL006-D-u2RhVkKBczO1_6XYdK2PKkDSw-foqJmCAmenkL-olGF08m5NS-Nl2QUjvtIYMy0mMfxPwkKqO1krA4fvCMCp1B7q37JkIhQXcYyiWh21r3AJc5M9VBknPPDNl5mZSJQYszsOoA6zLJ0xavpoohuaP3fBPMOHmfGmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خط حمله احتمالی پاریس برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102585" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102584">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=GmowMxr7EcO00IGd4GVT7AJZx0efrvh0D1SuzbnwNKQhZnUz8GlZjGFsdDJ3E5DxF9r_GHXvPdrvl64RJp5H3s8ZM6oWWZbkRAoUwn4660C8AQr301xeJCxtPzgKyLZyUWz4kLdF99fW-aA1oi8TwCU28qPAJvffJd-KjmBuicdwDxYcWzP_d2AyhjcSqGHa7OQqR7M9w4KdM8YzZpc3L_9xvgDEZ8HZkAXdif9BacsBkKh_dH-ZNKA25pmwkAC6BmTxGWZoGom6IF9zBeKpJjado7CHamNZXZdojdBV9E8SesT-QELMW0EtMkzFSULp0kiH1yXcZ4HNmDsPRvD7YlSYrWvibw8XskNWa6rKUpZA_a2n4Rs2ANgM8jpIUnKuiVK4qftHJ4A6zMKevRjpszzp-yy7C35vyrDAX5UcO-sjs8ktnouh-UO-KFFhGDQ49QVlDnGUhHwKReHTB3Y983lzQsn7jTPPCspFOPNxkSYlovKBmy3_S33J7iFLv5FO2L-jivorekOgWwmEL98deh15GgJa8azUoaJNRaNutILnIBSr50hDaAUrV0bkBXheYYwB-3QA9y2Gdh_T2HEHdtGMewUoyJyfvJ2jdVuN2v-CmN68en4YDXQJSrbxZbeS8yujh9L4eVexC6-OXfYMk7YS_vaJidcGBIg5cHpCha8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=GmowMxr7EcO00IGd4GVT7AJZx0efrvh0D1SuzbnwNKQhZnUz8GlZjGFsdDJ3E5DxF9r_GHXvPdrvl64RJp5H3s8ZM6oWWZbkRAoUwn4660C8AQr301xeJCxtPzgKyLZyUWz4kLdF99fW-aA1oi8TwCU28qPAJvffJd-KjmBuicdwDxYcWzP_d2AyhjcSqGHa7OQqR7M9w4KdM8YzZpc3L_9xvgDEZ8HZkAXdif9BacsBkKh_dH-ZNKA25pmwkAC6BmTxGWZoGom6IF9zBeKpJjado7CHamNZXZdojdBV9E8SesT-QELMW0EtMkzFSULp0kiH1yXcZ4HNmDsPRvD7YlSYrWvibw8XskNWa6rKUpZA_a2n4Rs2ANgM8jpIUnKuiVK4qftHJ4A6zMKevRjpszzp-yy7C35vyrDAX5UcO-sjs8ktnouh-UO-KFFhGDQ49QVlDnGUhHwKReHTB3Y983lzQsn7jTPPCspFOPNxkSYlovKBmy3_S33J7iFLv5FO2L-jivorekOgWwmEL98deh15GgJa8azUoaJNRaNutILnIBSr50hDaAUrV0bkBXheYYwB-3QA9y2Gdh_T2HEHdtGMewUoyJyfvJ2jdVuN2v-CmN68en4YDXQJSrbxZbeS8yujh9L4eVexC6-OXfYMk7YS_vaJidcGBIg5cHpCha8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف داشت از ماشین فیلم میگرفت که عجب ماشینیه یهو میبینه راننده بارکولاست
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102584" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102583">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=I-qS6Pa_OuUcWy7TS_c5J4D15yMnqxux2zWi2BGMMvBiBOwgi7HD-IW65glHL2XrjuY1ZPy6JmIaVL41zpAyK9iYqKUjxFsZ6V7C5hFcUPSlPlyzxhfvjCh3FrNFHKbrVZUAR8bmIFHvFyAXyRNb-1VSz_KWRZ7fX7G8WsNzVZZswvcOV7CN_51yXN10KFM6J61ZGnYu1pTWX4oeOa83fm-L6wnVjh3st1LMpht1kHanE8ga3B5im0OZUbe6dsO6WzdimCjJc22vnvpjlzoYexgS_QqoWS3vQliEZ3IzyFSIY3p3wocd-yFhIH8G8fjBqi6YBaJMqbu8b5anr-2VLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=I-qS6Pa_OuUcWy7TS_c5J4D15yMnqxux2zWi2BGMMvBiBOwgi7HD-IW65glHL2XrjuY1ZPy6JmIaVL41zpAyK9iYqKUjxFsZ6V7C5hFcUPSlPlyzxhfvjCh3FrNFHKbrVZUAR8bmIFHvFyAXyRNb-1VSz_KWRZ7fX7G8WsNzVZZswvcOV7CN_51yXN10KFM6J61ZGnYu1pTWX4oeOa83fm-L6wnVjh3st1LMpht1kHanE8ga3B5im0OZUbe6dsO6WzdimCjJc22vnvpjlzoYexgS_QqoWS3vQliEZ3IzyFSIY3p3wocd-yFhIH8G8fjBqi6YBaJMqbu8b5anr-2VLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت زیدان و بکام در برابر استرس و فشار بازی‌های بزرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102583" target="_blank">📅 23:55 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
