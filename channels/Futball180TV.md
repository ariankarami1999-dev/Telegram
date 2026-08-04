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
<p>@Futball180TV • 👥 495K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 23:36:34</div>
<hr>

<div class="tg-post" id="msg-102716">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NTHnxdxM5M-huQtcVp809YTbWQ6kB1C0HilXnsSshgFE5fgssC-0VZMqE2LgHiaPjEHFw-Q5RbVqSJeuemhdegJG_KfbVsrxkzEAeKKS1rLohyS4rQftuULAdw6q-xZEQ9xvg7k671-i5EbWchJr3UPqUZ79sUv5UpWxvLvudchHECkxXKQp757ELAzu2rEqCSRFSPayLg8vtp3-d5PEvRVvHQ_a-oULqVRfZ7Nv-WjNxO3S7k2D2wBcBt6hYkuD3pDUiSV4WlHCYHAgF04Rv3YypYw_UShFsXMhQ3YHkPTyE2Q8UhjH9LDZ1SKGpWDhE7zEPitSe5GiF58D1jlEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
جرارد رومرو خبرنگار نزدیک به بارسلونا: امروز تو مادرید دکو با ایجنت آلوارز دیدار داشته. طرفین میخوان هرکاری برای نهایی شدن این قرارداد انجام بدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/102716" target="_blank">📅 23:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102715">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5UP0zJBsVhzhz1rvsLhaif0yXTvndCI01nd_n1ZuqRrlqhy33-eK-qq8uPHObNG8wHpVZw2i0KXN15DxAv-juTRQHXSYOshw9UYVXT0CbvZzJJiESsTLgU9Lu0RPDz_5HEUEhxLnpoX3Iky1paHvPqB91e-atji6Zwq1aik5PxWYcdiaW4-cgGpug0xXOjbocYy_H6w8Rw-XzG8QofYBGEYDQYpFi9ETchgGZeYo2wWa4Rs213UTB3INB2Cr8DDznetiLZWxwtluH4A42ahgYSMF4WCAbT7_BOL225FdVdmZQ2158va3KAMZOsZ7qrQdG2H4lvdybDTPyqHbXXvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو و پوستکوگلو تو تمرینات النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/102715" target="_blank">📅 22:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102714">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hge0yQmggCcbhCBCydkdrx_dRg5IaEyciZgGKwobSeNuYC6pbTP5UQ95vfDtLdxzuOi9d8fE_KZJ4Pay9yXN3Dm8H2RHogQZt9QcfwXVNX1Xkbir4hBMa6vrwncpnALFaQIfPT26tTIarJbzKWiIYloivh1DjrXFA88myZ8b2y1o-qqNPe-TQC4XhF0O16_pANSr-lHboHJfiXt5LSMjvU7WSTdC0JZtJPebEl7Ro_D5rgfE6iYdeHsj-YuLO87N9gf0pzJWozVmrKH6XALR0VTMobRrf0F1E7D2hIlXdepRymflr7mZgzRV7tlkUcXOuMpTQ19q3A-4qEqviSWz_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/Futball180TV/102714" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102713">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=hcv9ZNzKKEYGx3fQ1mEsPRuO4IebKZA7-9dwGeTBWNugq1vazLpo5NjBaMFeb-Vi3uy8KHXfF2df7ZJVrU8u3dQJZiGY8JA63UueMXhBU9DZ2-EA4-oT5fCtz-XatOqbbFog9fO_kxmQqnUcF67DvD8wj975NLjs1Pw3S-J8gjG8X7BacfddJIYkobRV-l1JD0X3K39BPRSS-tLVzvzyARAuWibE9q9TvR59jzPZ459SajXG8cBbIKyJekAoI6Dl0I9xdsYRWHx9on_M7KjasH0OrcX_-UwvZgoklHSgjaDLxCrVCsgJWmtde34BbU7a5DwFNOXBlRyfA1sOIO3igA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=hcv9ZNzKKEYGx3fQ1mEsPRuO4IebKZA7-9dwGeTBWNugq1vazLpo5NjBaMFeb-Vi3uy8KHXfF2df7ZJVrU8u3dQJZiGY8JA63UueMXhBU9DZ2-EA4-oT5fCtz-XatOqbbFog9fO_kxmQqnUcF67DvD8wj975NLjs1Pw3S-J8gjG8X7BacfddJIYkobRV-l1JD0X3K39BPRSS-tLVzvzyARAuWibE9q9TvR59jzPZ459SajXG8cBbIKyJekAoI6Dl0I9xdsYRWHx9on_M7KjasH0OrcX_-UwvZgoklHSgjaDLxCrVCsgJWmtde34BbU7a5DwFNOXBlRyfA1sOIO3igA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…..
❌
تصاویر مناسب دیدن برای همه نیست.....
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102713" target="_blank">📅 21:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102712">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIHMkWJ2vBmylzIS-Xlvo5D7p9svGngx2OEn72UtQ1JclTUL2_fOozf7iyIRB6Th_R82lk-_m_nPe7r9qXY7n5Qe0rhoUxfwRzGL6wFOKMNFMHWrTJDUpJ_pQvjXburYMeRjBLKZVXwlRD2Iad-JPV1kZZJ3k70Cm0-f6UjRegAiVhqhfBDVxN79EbTe-fBQ-HAJOsLIBlfuZZ36VomZ6gCQNJ0dwrQQV5qM2fD-oALEuyw_f2GnP9e0Znyyp2rU8IMwB2zs7O91xl2OS9MH03YGQxfNYJnpMIB3y1SCieaeHI9PVv5egfgdaCwrfUmreU-mlfNt64uQ0x5m7F4SiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدری از پسر تبدیل به مرد شد
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102712" target="_blank">📅 21:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102711">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrjYYzzm4Nojd3rztrjdBYfJnNfvme-4nxML7MRHOl2wqZfDUjHgSgnHoq2IHKmtSHQF6jiLXmb8IdelnaacpsmeQLphBBKdsLAzhXwE6_5labmj8hF7BuwTPUf0v8ytOgm7AxEGAzcUELlzAvhD4a-raebtZ0vNGUSA9cMwDmwbc1acOsFny3pox-cMUn5gXJkru_HyCidIRxzOgfR1OPmwf2HkOz06apYyvGNMMVmpc3rYDCsEZyAcnzWrlk3ViYyb4IQfX8tOFQsDXf-NEJbolmhhrslqY-HybN5bWRtLZCqamOQpGYSNOQsqa4Kg_QQWC236qTy-FxSWA9Yzyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل زده در 10 فصل اخیر 5 لیگ معتبر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102711" target="_blank">📅 21:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102710">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at9g2xbaGzqwp3pA95rm4JHP3PUxNMk5BA9tpjOtdtHECQ62WvfhXNi3tH2CZs3mpwWIchcvKAdfUYx7YC4Xr0pxghzWrgtEo_MP1ekXPw8RDIEAJqaTh7t1bhPvX6e4cK9PhEjvZeDatsJpfaAn2h7_gzJ4a28tAcXWKzQgOxLc89p4AeU7Z-LvMVcA4Of6j-ukvLLLuQ7XwdTMwQtMaqXR7u_0ywNQpfSaMLFIzpsSQ9Z6VTCMiZ30Wd_Kk4wsfAil6QOkQ4nGD4Tozqy-QdFCfwyac8QpFokTIamZTm_DxHn69GSpXxWEjzPiqQKtWTePak8BClW0cXdA96UxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
رامین‌رضاییان خطاب به مدیران استقلال: دست از اینکه منو بذارید جلو هوادار بردارید. من حرفامو تو زمین میزنم نه فضای مجازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102710" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102709">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMayle_26TOtK7J_9IA7TDW_pnTwA_r0cnnzeZI_q5Eg5ZXeHkEr1B4gx_mJyZBe_xddbKQ8td-07HiRl-uQDGpyiIRNX5-KXefQnvQM7OVIBdMrOYJd_1ah0WwVaQ4Y0OEZCT5CRB-fhSlZP01cezGX9Xo1uwYsPSWi_PtZ0KTDiBVdIROezLaCS_SaFTze_msYlU3QrHkirRg_vh_11zi85xTvo-80MS93MphVOSkqpVnDmEkfeEACERtQS5KoUYHi6DK_cXVTTdXO-nygk3Hr6sJrvAsn-Rv1ciRhnZWDVLXX-G0ouTgYIpjmSyq0efKBONUYZCeJoD2m23saiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری
؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102709" target="_blank">📅 20:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102707">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVndqOc5tM-lc1bpiJVz2fkk3_j6d72rJAeqNJWZwrPGf0JR6aw6MAdxqhAhoEgLbWJ71tb2WLSeSXCyv5znKaaRnf3EoPtKulsTFjE-rES-BwrRErsJmSmPYY9q3kBgLjBMTYtdc0w4OmJVbtxJb8VihOYRwNT6vIu3BviIx0s6M_l24iAuYVRxgDswHO2UhadCJQtOsH_gvndxcmaRsydYePvZgkzqWAhmtkV8buUZh0IzmOK1Mp-hhfWom0HcbvxgKZfoyjjJU_MF03p4GLpuKL348B4nG8HP0gpuUFQY344dNGM0fM8zA-9DdM4IT2qpeFOOW3RInnnPzCX0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tGJG8gxBc8UhysTcR_LEgrXKpz9qDc3g5q66ADYBHn1VfBoV-jXE5AaJbOHTY8bCNkUQj6FgdvZTjRAZiOI73k0i_rjA2iREuhzFzvGzhJ3Z8_88rWvySzGDt_bJ4YJWnJf7uRhdpkW9RvMtCgZulrtst4imTR3A2powATfkN7MgeMztg-6mBjiN16vujjUmHzVZdjN8f7j0hlqLPiuEMMv-QlSJXzzLLcaBJhulYliaD8LKDhJcIxifrJ51pgygGK2Up_9Egy9Lvdo2gfgjMCvdwLQWAvYpDCmWI3QXms8gl5qyItm1EBhZOdQS4KfDrU8iZRxoQts_PyXZ0C4iEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
ویریجینیا:
من اصلا حسودی نمی‌کنم. به نظرم وینی جونیور خیلی هات و سکسیه؛ اتفاقا باید همین‌جوری عکسای بدون پیرهنش رو بذاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102707" target="_blank">📅 20:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102706">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW7_qQzPAOvHv6eiVHq6vhkD8R77o12bHAQbNxY1uSL_UUsBZk6cZnnT9lEr0OBWA2E1KQQxzo7Om8xOsuIK8ID2hiG_Iz2alqM4xkURMfNoEfKd6q9hjhmjzapjN8LuTTc9TePwagW4sdK4dX_KgCaGOL1FKfrWW52TyOxoDmjC1cfJkqzHC3hukCrAsC4fSoEIOAU7TWacAguJOr2eN7CXEcTPz2KbBi966oOc6vvVS9e-07Nj-NuzO4whSR57iWPs6-48VN03VKcY_7Gmm3xYH0Ys6VRFhJ7jClJbYBuQOsl_D4d-L3S9xUlz5O2W2i6OU1OwG_cGBMIuA3RBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
فووووری از فابریزیو رومانو؛ سیتی به دنبال جذب پدرو نتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102706" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102705">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b139a17c.mp4?token=Yc31eviIVhlxLTqxJyRiYyAUMjWy8l9vjgHviaPXX_NKYevmBdpM8QY-SxbwW-ln6q7_195SBCh-dkKolddXegl1NnavRzDmbQ4W1DgSf_GV1qi8UVemT3cGYs29ulUSkUc1CTzh9mTy_ougGVCpyTEBDZBaPlvWqWRQXZXnFODIDyXqeQpf2bH9Z0GOf7MT1tjGTjO7w4R-jBG2wUlwxUPwR-7BHrrCd53GxzBSVMVllyoeG2NIzEf1KUlO_rAJhQje22YXQrnqjTGGgv7sfd6JF0Y8cv4tXB8hbKca-bpVCCE-k5jygLjY3urfzltbf8uzL3clE7b_kabjtrlF2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b139a17c.mp4?token=Yc31eviIVhlxLTqxJyRiYyAUMjWy8l9vjgHviaPXX_NKYevmBdpM8QY-SxbwW-ln6q7_195SBCh-dkKolddXegl1NnavRzDmbQ4W1DgSf_GV1qi8UVemT3cGYs29ulUSkUc1CTzh9mTy_ougGVCpyTEBDZBaPlvWqWRQXZXnFODIDyXqeQpf2bH9Z0GOf7MT1tjGTjO7w4R-jBG2wUlwxUPwR-7BHrrCd53GxzBSVMVllyoeG2NIzEf1KUlO_rAJhQje22YXQrnqjTGGgv7sfd6JF0Y8cv4tXB8hbKca-bpVCCE-k5jygLjY3urfzltbf8uzL3clE7b_kabjtrlF2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⚽️
#فوووووری
و
#رسمیییییی
: تریلر جهانباز FC 27 منتشششششر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102705" target="_blank">📅 19:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102704">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISxYPZRyLEnyjoegFslWzIXUmbgdmZhyjS0NU54cj-Q3oTVtFW440Ovl9gSQeqCdJvEvc4RmMXKbPTPrqhOJnb-VunjPrEbxKXsjuVsRz_qsIoqYAUoCJZo69aYDE-6d6Em0xYXFKmEpp0jAv5sCaTJu-rh_5qHv72rNzQkRBGo_XXaku7jjEDShBB44ShT8gWGt-t2XjVZ64NDZ_8U8i5UlLSL921f3GiyY2On6YDVv-veRJ9_bSkyOjGbRZ2SCkTwDF5H121p5CGaKNvcn0vAwxApR1h9o_sLHXg375D2RNqWzLDZshWnB8uPquI-4t3Iby_4DJ_eGVXiVrH1KKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👤
پست جدید خاله جورجینا در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102704" target="_blank">📅 19:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102702">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rc4YbGMVcNPeLSzeRaspAHQHIsez-55Zylyjl-3fEFmo2-qN_FZRYRVHoLaAgpYxFiodpx291KbBGpfX3gOcKfec0hxFzqU7wLmI7Yywds1F9VPVp7PUVdiu7nG6ATHGZapqTdb5hVn0pafdreId7UIF71nYXjIfSfA_28b_jRI2OQx5r09YCdnl5czAVe1zBYf6BfDvkTHrYhMd1lGjSkhFyHyj0abZCFabO99qOqt8Gxmk_joHBvhStYxARdMPRiVmUY1FAzMnCPd-d2DN5Q6I6dI6nRlQFWclO1TEx_vWfZkidEL0hz9cyGsj9PdX0ujfylSuADQtNidSBd8r6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8lxRnwBA5QHIglGFVopTlnKNKI1jZOsaLYYDD9OPK_a7qXGuaEH6i26K-b6LKHtgRackHu3yWqfg9iSoR1tQc8mkuuZQGIBSQXrk6yIHCQW48uE4kyR0hzCxzCbarAdb8RcuUjLANYO5Zut0EHZvAh8KnvhgCW2pQA0mz3hbOB89PFDve3u92_iAXwnd7t0IsayFAm8EwHRKfiliCrvcgU9E3NvgmPwg3o1eOmrJoC9S_1t-OsUPhf2gbTKwK4r3k52yUST7TylzYR2OWK4zQs6YSwZ2OgTk_gtc7x2WOmiAN9_ftPNQdDCx6ZTkMneFhzTcIX4SuVZWt1YR894vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
رونمایی موناکو از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102702" target="_blank">📅 19:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102700">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=h9V90l693rzxXz3iPx2QvHOFDU7_7hbHCwC1dTADCa-ybQROC0JHPbxX7x94Ew9T5v_4gmWjYyJxytH4gnrq67skWzqdllK8oegwJj6bZMXQoxe7oUaIMOM6ptr51_EtgYmpci3FzOWeLnnqWv_cPcUSIIFLJdFCcOm-WiIF6u0kLUYmEUHyTJwG0oBvCDGVXRcTvaZzdynHOrExtFRGLuwL5XV0gOoKLjTaKxP5N_0XFQdPr9IhZ83TwQptxtyv-wzMDHHfhCAsS1iOhAetQEOxFIp4TLJalQ_bq_ohSUFcnUl8sCAigAwvb7TPY50mySoyU5xfcJmCfBUBeNxqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=h9V90l693rzxXz3iPx2QvHOFDU7_7hbHCwC1dTADCa-ybQROC0JHPbxX7x94Ew9T5v_4gmWjYyJxytH4gnrq67skWzqdllK8oegwJj6bZMXQoxe7oUaIMOM6ptr51_EtgYmpci3FzOWeLnnqWv_cPcUSIIFLJdFCcOm-WiIF6u0kLUYmEUHyTJwG0oBvCDGVXRcTvaZzdynHOrExtFRGLuwL5XV0gOoKLjTaKxP5N_0XFQdPr9IhZ83TwQptxtyv-wzMDHHfhCAsS1iOhAetQEOxFIp4TLJalQ_bq_ohSUFcnUl8sCAigAwvb7TPY50mySoyU5xfcJmCfBUBeNxqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
مطمئنم شکیرا ومپایره مگه میشه آخه تو 50 سالگی اینجوری باشی و با 30 سالگیت فرقی نکنی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102700" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102699">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=pyqH_vA2Dacvponh4AHC-E35Cyhn7BlpsgIYxczEN-i70bkalXjar6G2cEF0DG6oWEufq8dDIrDzlnWoeO-aszDDEEJZenjv2XAIZnsh2X8ifdChD42fMGpsqxhl0FWe5l7q8QpH4Y0U7DEdsmRlDSzlUlLa77dPzUPmvJ4Yda8Ji2J7ciZP_Stam0yqSBS5ZM5mWthq7a7bqpL-K5jwKCdGRGqgwAVCMLN2jFgMVRgfLJvePfivTHE_TYer9UVuNeahBgUxTqWWYQx6a-S5hDu7dg3d78qpeYLGjYgRmNAWWvbwZ-BIXJNCUdE-DhkG0ALOUAw66X8iBHEpsifssw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=pyqH_vA2Dacvponh4AHC-E35Cyhn7BlpsgIYxczEN-i70bkalXjar6G2cEF0DG6oWEufq8dDIrDzlnWoeO-aszDDEEJZenjv2XAIZnsh2X8ifdChD42fMGpsqxhl0FWe5l7q8QpH4Y0U7DEdsmRlDSzlUlLa77dPzUPmvJ4Yda8Ji2J7ciZP_Stam0yqSBS5ZM5mWthq7a7bqpL-K5jwKCdGRGqgwAVCMLN2jFgMVRgfLJvePfivTHE_TYer9UVuNeahBgUxTqWWYQx6a-S5hDu7dg3d78qpeYLGjYgRmNAWWvbwZ-BIXJNCUdE-DhkG0ALOUAw66X8iBHEpsifssw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره خنده دار پیمان حسینی از عکس گرفتن با دخترهای بلاروسی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102699" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102698">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJNwkAi0zu2F_lxeGtaUozy_FqKZcJhe8t8X8j7w0MK9CteAMvrbNAy0upBcogla085h3gSy_N7HAV6txCtcpSs9_0Co3R-G8FVibJiqTeYGYKCZF9L5PN-V-B3PS4UcuMIOwGaCgSHD-VZMJW0Ya7v75G-oaMc0tObIbbmjseG7cSARlfy3FM6SAQvmTqudlPjq8ZgQ2zet-RTKC5ngo3GlH8WEviax3QjSWOKTGlfr9naFie5GH6rzL3v63Hl3I05CroSWXV1G30AM1etJtQh60_SurSPguLZoEZ1xrgYgKRexAqDGqAikxdpgn2XqMuiMwejZtQGBovXpAbWKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/102698" target="_blank">📅 19:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102697">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8Xi0zXGUFmevZ_CjQb0Cx8h9XRYnRoQAcnoRLXK8bThD4f7XV-kM9U6YVZzd8leuKCPUBMKEc3iq4KG_a4bWvb3iu0--ok6ICvYPNRYA-Ouh0HsASGGjOksaSHJSaNBoO-mOLnmdYLZ3twKg56ThBT-aHdTHatznxS2h_FHII7CWjoLkhZaC54YwDMoIy6d8IQ-Bp46OrvRydQyKEbotYxqd55CKypJP_jgIv6D67uUCd7FgI278fe8cHmec3O8Q4LbjLLrr1FDBKouGYm8lkg4tl5lb1_bGnI3jLXx0VKP-6HymrVhr-2n70yPuNmgD9Se4t54ORpP9bURDdYR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
#فوووووری
از رومانو: ترابوزان‌اسپور ترکیه اولین پیشنهاد رسمی خود به مدت دو فصل را به محمد صلاح ارائه کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/102697" target="_blank">📅 19:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102696">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlKJXyCjAw5gDNEDNhN283lGTQb1yobskak4nj8EgcKbsA3w1pDUn-N802y6MRfEudehSjyHeoqZWxDdHMjs6OnsouYxkasZ7_QbwOWlcEGuQulwz_pSbjI4Fwyl7idTu9cCPuNb3sm60x7PX-RkP4N6w7Tb6UAMH0bc9-I8VARQBK-B_ErDCwwkeBKhMkNx6BPnBlg2T1YFA03QM20ZszXlIF4k-ezPgWOQufC1SHml-r3prpMYWqAwBiYCK-ZbHiR2YclGRDbiWt1edsEopU8w2Tcm9Agfmc0TcDx2K1P3ZLAK1GuNT2wiC2BrcdQ4e8J7M9CFvqSqsNfIajoQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#رسمیییییی
؛ علی‌نعمتی با عقد قراردادی به تیم لوسیل قطر پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102696" target="_blank">📅 19:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102695">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b46370582.mp4?token=kBdLpk91-pesx0hC5jPeD3z6VI6sXkpwu_Dv0Pw0JvX7iWBPqRSuq6pq-eGPirTb1xeKIKOOKJntvl2hwirpV4nvOu-yVWm4nSTD6qZReUtg4scx1bcokwrBkXp87TXibmXnK6kT-1JLL-1pEaKmOvkPSy_9qEP9MpIAJLa4qY2Whsq33Xn8MDV8z8sV_uF63QvzFdx3TAutapI4CD380jKn4ZCnY54X-osskn2jTRo4RmssrjD2p0HZceXCt5PH9EC5uPfVOSUCUus0mPOUj8e2nSd6411XazNWvUjAPum3odb8p-2YsixRmMKE-zDfGM72thAwvJDNWYzKmGF1ool8GVvjSfp-eht75bvy7Jyn_XxG112d4NOglppPwQBKftw3OUMB2hCDiklQwDzkQVD9614XmhPMQfHNqdFFJwueh1CZj9KqCyqaJcLtfrsjIRS9NWUSqD-IGvj30Gqm6sJbI9h4kYj9Fm5nqPJ64U67Bca9XjHyxHsb2yLrL229_mdxyWSigrZt7bKwb1EwEgO1oedY0GgTc9UejhyjNKVwILg5DIhPCxIP1LNHctdS7bbKm3pLy0tIGMaON92TA92OVoYyoJTVvtv68pjDoYRArC1D5MDqFzlbT4Z5uTr0AFd2Os9hx2DpTlVULwI1GzG0DeKbHZjiRBmOCPIdnBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b46370582.mp4?token=kBdLpk91-pesx0hC5jPeD3z6VI6sXkpwu_Dv0Pw0JvX7iWBPqRSuq6pq-eGPirTb1xeKIKOOKJntvl2hwirpV4nvOu-yVWm4nSTD6qZReUtg4scx1bcokwrBkXp87TXibmXnK6kT-1JLL-1pEaKmOvkPSy_9qEP9MpIAJLa4qY2Whsq33Xn8MDV8z8sV_uF63QvzFdx3TAutapI4CD380jKn4ZCnY54X-osskn2jTRo4RmssrjD2p0HZceXCt5PH9EC5uPfVOSUCUus0mPOUj8e2nSd6411XazNWvUjAPum3odb8p-2YsixRmMKE-zDfGM72thAwvJDNWYzKmGF1ool8GVvjSfp-eht75bvy7Jyn_XxG112d4NOglppPwQBKftw3OUMB2hCDiklQwDzkQVD9614XmhPMQfHNqdFFJwueh1CZj9KqCyqaJcLtfrsjIRS9NWUSqD-IGvj30Gqm6sJbI9h4kYj9Fm5nqPJ64U67Bca9XjHyxHsb2yLrL229_mdxyWSigrZt7bKwb1EwEgO1oedY0GgTc9UejhyjNKVwILg5DIhPCxIP1LNHctdS7bbKm3pLy0tIGMaON92TA92OVoYyoJTVvtv68pjDoYRArC1D5MDqFzlbT4Z5uTr0AFd2Os9hx2DpTlVULwI1GzG0DeKbHZjiRBmOCPIdnBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این خانم باتجربه نکات خوبی رو در مورد دفاع شخصی به خانم ها میگه، حتما ببینید :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102695" target="_blank">📅 19:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102694">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsfl2lj2JMIgSlmrMCInOqgfkAxdevHeVQAZAUGEq6HZC5hJCTTlozZTxvGgZaNAyerMeVLL3uA0ctvav5EMNIyGYv0hLk1X9mmQjXDg25En-nDUdwUv7d6Jv0R-ddp_oo81a1139sd6F3gMN7XjpVKvNkmAKJs7pfU9FYN_DJp9n9rbjwA-WG9xwil_chHzbXFymUi-LUTmay79LMlBk3MMtnxpZCQmeU-z5NtGIPWZsHSqs_eeAQx6E7wpUWuB8dWXxuhwwwKa-nqWKDPaCwop5tlfuvWw3yfT1Dy7eGSX-YTmV-hm606RPA6dMgiMC-NNdo4s0QTWQhf0y01NaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی برای حمایت از بازسازی مناطق آسیب‌ دیده در سیرا اوئیسته مادرید، 80 هزار یورو کمک کرد.
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102694" target="_blank">📅 18:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102693">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD2jUiZh0l6DghX-Ln8C7uA8c8ARl2q6jAz7vx_QaMm3XmUfqu3paDqlaDX_bMl1sGxsQAplXnFxgjvhzUcI4NQew8BC2Pvqg3r7Z2DW2Luxd2O5R_jjfWjaqSdRJcIhx1U5AoydVfABhlWedCct4d0EAaUjYj5kfONmIY4o3cTf6fLZYmMEHl7HurE8QEitKQlfLVD8kaqLe9i9bhPOvJtDz40BQC5c_kdSKupb9AhDN1ANam4Nl-pTceupbLf4IPlT3KCkDgZ2FeoGqFhV8g75Gh4S4LC4VTQsEeWNrYxPMxHFkHkJ5s1taCrGLlYouc1I2JPt09do8xr1gaNKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
هروه‌رنار سرمربی تیم‌ملی ساحل‌عاج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102693" target="_blank">📅 18:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102692">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f0d298b0.mp4?token=urZhn5loDbJ3_szNlt9pE6JbmrprSkCWSkV_H3JxZRuz7Mi_fy8EyRUrIYbfAY_YlrRu9G6MiJd8ZwssF9DVdvuMlOhF4Eh13CWaDMOMLPBwshcqP7Gw7X8CjxP9AAIWqof3IXHtUL6iO__7chkTzkM25MD1rRkyv8JMgeLZ8aE9NdWmO92Lr8thtloy_iQfZudZWG08oWAsNytB2-oiADyXmMzMoSOHllDF0hwbmep-ia5CxnZx8_ygecU4AXr7SrTpHEP9aaNTfGlzYTbuCqNpESh4fJUS42qSQtY5QjKYU5z8b9w6suG4Hjo7S62UOXFtsyR47Peh3TumQsjhAzhvSeqx8YE2QDwDc9KvctTDESf2n3lcKlsthNPoxjylcLQfXmdX-GuAX0i2rFIq8tWjrQidvPquhfatsCOJ8zjko_ekrJnjwqVYcfxZNVfhw7Jqny4a1Y9nN37gMlwo7txgTgDGmOQLXi7UrqP7uHI8MM-5FsHX3VIgz-689hYvHOuKoTRqcmRsGOx_EJZVFq0Vc-KZx9iGejS8sYPunhv5NT-GJorKndm4nfp82dA7L1f-v5Gw7-glM1ugwdHJmgpUACIAGorPJ1Q7pJNQyVmmQ_Qe01Zo1qn0KxHG_tvkkcCspM-GasaQ-hv85JoGS4PG3YtXLFaLh_5t3UHOziM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f0d298b0.mp4?token=urZhn5loDbJ3_szNlt9pE6JbmrprSkCWSkV_H3JxZRuz7Mi_fy8EyRUrIYbfAY_YlrRu9G6MiJd8ZwssF9DVdvuMlOhF4Eh13CWaDMOMLPBwshcqP7Gw7X8CjxP9AAIWqof3IXHtUL6iO__7chkTzkM25MD1rRkyv8JMgeLZ8aE9NdWmO92Lr8thtloy_iQfZudZWG08oWAsNytB2-oiADyXmMzMoSOHllDF0hwbmep-ia5CxnZx8_ygecU4AXr7SrTpHEP9aaNTfGlzYTbuCqNpESh4fJUS42qSQtY5QjKYU5z8b9w6suG4Hjo7S62UOXFtsyR47Peh3TumQsjhAzhvSeqx8YE2QDwDc9KvctTDESf2n3lcKlsthNPoxjylcLQfXmdX-GuAX0i2rFIq8tWjrQidvPquhfatsCOJ8zjko_ekrJnjwqVYcfxZNVfhw7Jqny4a1Y9nN37gMlwo7txgTgDGmOQLXi7UrqP7uHI8MM-5FsHX3VIgz-689hYvHOuKoTRqcmRsGOx_EJZVFq0Vc-KZx9iGejS8sYPunhv5NT-GJorKndm4nfp82dA7L1f-v5Gw7-glM1ugwdHJmgpUACIAGorPJ1Q7pJNQyVmmQ_Qe01Zo1qn0KxHG_tvkkcCspM-GasaQ-hv85JoGS4PG3YtXLFaLh_5t3UHOziM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📅
شش سال پیش در همچین روزی ایکر کاسیاس از فوتبال حرفه‌ای خداحافظی کرد.
"عده ای برای پر کردن زمین می‌آیند٬ عده ای برای تاریخ"
⚪️
🔺
ایکر کاسیاس از دسته ی دومی هاست٬ خیابان ها هرگز ایکر مقدس٬ یکی از بهترین گلر های تمام دوران رو فراموش نخواهند کرد :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102692" target="_blank">📅 18:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102691">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5e14ddfd.mp4?token=vk7eTBLQgkUS2mhzR1LGgbvOHLFipo0gvjGzLi3luDCQkZcbYVCl9EYroS2C1TpQd1jKAaEGgM58JGLUrzG8Mm5cpUrCEYbBttM9m6JloNqIsuLrblwjmbbbuqZXk5ZdO7iGup_MS56x24Wovre-MafwfpO5SVqrYDBJCz_uubE2P1mXAwVoawPyb2nhpJWVo2-0UyDxW7RDuBeWwvsJIOOjVjaEj65kOGF_6MMKiYUt9SUSTq8x5qIjLUJLQxBZ3UurMUaPznXMWSOLGf4Fl0dUTQ0w7-Ft-JrE9z2rj3Y4LZYO4t0F05YImAfqyOX_NxxP3HJdlHObFPKRSzP5EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5e14ddfd.mp4?token=vk7eTBLQgkUS2mhzR1LGgbvOHLFipo0gvjGzLi3luDCQkZcbYVCl9EYroS2C1TpQd1jKAaEGgM58JGLUrzG8Mm5cpUrCEYbBttM9m6JloNqIsuLrblwjmbbbuqZXk5ZdO7iGup_MS56x24Wovre-MafwfpO5SVqrYDBJCz_uubE2P1mXAwVoawPyb2nhpJWVo2-0UyDxW7RDuBeWwvsJIOOjVjaEj65kOGF_6MMKiYUt9SUSTq8x5qIjLUJLQxBZ3UurMUaPznXMWSOLGf4Fl0dUTQ0w7-Ft-JrE9z2rj3Y4LZYO4t0F05YImAfqyOX_NxxP3HJdlHObFPKRSzP5EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
#نوستالژی
؛ دیدار فرزند رونالدو با مسی فوق ستاره فوتبال جهان در حاشیه مراسم توپ‌طلا سال ۲۰۱۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102691" target="_blank">📅 18:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102690">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxylJGOYH8HFsHwOwwLSx1vKSsnZDZ9bxckDkNc7ewtGjlwV22D1Jfjqk6IitF1BhK_6G1yIH80Llr7bO-FsqoD6NPu19zIP6prUy7XBuupm8CIEZP6-gyggDzPX7_MlWPyrHY-Lq1hZKsNaomTwhAhPdqGvQyIwu-8xTTBTRfrBupbFPQChIEnjUopDHIcH_itVNtu8q3Cmw644-0wUNAGapNbNsSaBaQJRqAtt2nZcaEt8MTPXrhtQuukgonFCY7XQpHU9ok4igYOGZFHb7HMkwfo-OZXd25U8qqErGwGiVzrAVLQ7jnWkfkdR8CzDgNxERs4mIpl68lYJNNPy8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بازیکن سال 2003 آفریقا: ساموئل اتوئو
🟢
بازیکن سال 2004 آفریقا: ساموئل اتوئو
🟢
بازیکن سال 2005 آفریقا: ساموئلاتوئو
🟠
بازیکن سال 2006 آفریقا: دیدیه دروگبا
🟠
بازیکن سال 2009 آفریقا: دیدیه دروگبا
🟢
بازیکن سال 2010 آفریقا: ساموئل اتوئو
🟢
بهترین گلزن ساحل عاج: دیدیه دروگبا.
🟠
بهترین گلزن کامرون: ساموئل اتوئو.
✨
بزرگترین مهاجمان تاریخ آفریقا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102690" target="_blank">📅 17:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102689">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
⭕️
🇺🇸
روبیو وزیر خارجه آمریکا: مذاکرات بسیار خوبی برای بازگشایی تنگه هرمز در جریان است و احتمالا امشب یا فردا یک بیانیه مشترک صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102689" target="_blank">📅 17:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102688">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRaaU0Ee2Q_ia-1DEAERHkMMB1NG36pHwElJZM_Mg_vyA_71ugd8sNBnf6xAmHddxjnAE3oGyFHuvXFg2zj9EDoRaE0PIwXCq7KR6fLMtPza4hsEkW0AkP2q4WMeZ7KvEiiZKwD4X68aKfHlAOIek8rweScXncYitekfd1f3hREKnYIp7IpWJu_p86uzuM1fPnZaJNx3_omUgJC6T4S0o20ewLPyqWvNeorpHEd3qHoRrq8_Y2O2Xqlw1ffUPLUNk7Weje2p_idbPiNXAReFI7zMMotUZ2z3Ww1F4EppJTaO53lQOrHiWjJRSP3AKAFjqCoMLex3rSOcnUZWEJMEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
چلسی صدر جدول تیم های با بیشترین خریدهای بالای 100 میلیون یورو در تاریخ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102688" target="_blank">📅 17:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102686">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAIedibtgAfqpuFnhbmI40DgrjsSPYU2XdI3QiUTYVDtZyc_IjUscdTXDh4HFVJhcWC8y5zCG49FZTRRvOAZ4kYwCP1HC8fsl0zv8d6vT1G5wvKqL84-bP7z8yeCYogrH7wsULPWAYVDfL12SjJhBjGpG46K2ndT0FN2GMj-7NuQEy0YhvmizHMOV50dUNFiqp7V39s6NCvkBNbW6z6nmuVjtbYe-q15KcS4YUq0Zvx2UrhYN8-3kF_Ol-t94sZ4q7zkh_zqakePlhLlV_Ntzl4FVRSRY-vJFNKX7N02Z2K86KSE723gzuEx2Oa1gMeKFQcb-yksofvyBuz0WcppwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7APQ9i1SCYeoLwn5uFJofVylrKUHAhDFKlcZ-9m00DDwljJiEVMkUmHUq0Rv8Nt8t_ej6YzHg4C9h5yJJSRfsJvoW-RldWOvgbpLo5Gesya_uN4UyR_ZFNJjAQ6IjlkXD3tAJpPsFVs2nlHaHSLeOWZaXqwb7gc2QntRA0JiIfZqHfRnvvaTgq6S02nKp973Wpszz1zRP2sSyAOmfHRMMVlLZPoPQ9MG8tbBlpss88puZVhcQkveAiZc_k4GDHhqnrFGTXAb_SfHNstOnmWRoOASvvz8znRt7gXA442x9tbOwSvJ9C5HsKzUVSsx8788oPTXsmx1485JrOfmlTnhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تغییرات رودریگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102686" target="_blank">📅 17:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102685">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AceDAJz9KevIt_jqG7J5qMyC4bkHzsrPhPJp5-zBLv-DhbPLY8PwL2pUs04bD_1G0mTm40w26hsrBHdo6_1eN72_rplBaoK1dPhFs_x4Vsv8kqamQ3P06RM5DImNQZ_W8weli0fCw5SA7P1pDioxA35Bd9PsCIJiUX8MWu5DeJxyqatQ-VIpBUVsOREHzGCDBNxCwd6uhfEC25BgBT55NiOGMzLYEARBQBAXypCRcuFr4MZk1ATFJAAitTyKuz75IS2_y36M7UXgaqvRax5xfaFu6JSm0qO2xlPhHEQhOnrpu8dTmasBD6tGMSgH5pbVdJlHXhPpBJKzlth6SWyaZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
14 سال پیش همچین روزی؛ باشگاه یوونتوس پل پوگبا رو به صورت رایگان به خدمت گرفت.
🟣
پیرلو: روز اولی که پل پوگبا با ما تمرین کرد، همه خندیدیم چطور منچستریونایتد می‌تونست اجازه بده بازیکنی مثل پوگبا رایگان به تیم ما ملحق بشه؟
🟣
بوفون با خنده به سمتم اومد گفت: واقعاً پوگبا الان مجانی به اینجا اومده و منچستر اجازه داده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102685" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102684">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102684" target="_blank">📅 17:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102683">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTz4h5Y6YdUbIj2XoqCzx5TDNGP9KFWrjy_9uwrN-wAZFCDFOf1T5rnFYhVgfPVfnb84olORucEsboAPjpyqZoRYqLw4rzGXLeU__ov1db_5_QPaGPCx7XYtrLXIV9yRafXhozbN3k9INIDhmFX4PCiqMk7Fqk0SBEo0wpv_c_pfpFl5uGoceBICjiaYyPH52JcGZu4SS_WqtYJYo8FZMDMYv0srkT4DZ19U6KbfWz9nPBqaeNFJsLBeplzYHd1IXGh6AFJZlcEu9NVAFTXT12Qo4bwdO3cOStXNT6z33Za1gSyk3VSufzWZkfEa1cDK6g4enkljd7iSf73OgW1igg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پست جدید بیژن مرتضوی درباره مصاحبه همسرش با مجید واشقانی و شایعات بازگشت به ایران: تا وقتی جمهوری اسلامی حاکمه به حرمت خون‌های ریخته شده در ۱۸ و ۱۹ دی‌ماه به ایران نمیام
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102683" target="_blank">📅 16:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102682">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3348f33cc.mp4?token=duOYeyf7E6Sn6c-P73vvY5K4EC2CaWah3XM0Pf3Kdgu33zSa3i7wvRDCEdWYjyIoD2G6-JB9BalytHHsa-Qre7RyEF6AIADocf3wG85bqd94qv1GDcVVROEofMPu-8slgBQFlpI5uwChdAN0stHFh0Oxxztp5YS2tXZeDmYBbSSNH7ij1rlBCAiSOaIPD0llrPFgbtGJJJEj4hGo5qX17vIYPRnSY03YkA4i-OqU05gHrW1YC_k_V0TxD4zK3wHd8hQ_cHMWJRICCeIJ-3Ef4vtl0BuACG-0r_wetHbb5rxwYHkRE2ht4lbuJ2qmHXovISVAJjIpOxL1-JYIO9qmgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3348f33cc.mp4?token=duOYeyf7E6Sn6c-P73vvY5K4EC2CaWah3XM0Pf3Kdgu33zSa3i7wvRDCEdWYjyIoD2G6-JB9BalytHHsa-Qre7RyEF6AIADocf3wG85bqd94qv1GDcVVROEofMPu-8slgBQFlpI5uwChdAN0stHFh0Oxxztp5YS2tXZeDmYBbSSNH7ij1rlBCAiSOaIPD0llrPFgbtGJJJEj4hGo5qX17vIYPRnSY03YkA4i-OqU05gHrW1YC_k_V0TxD4zK3wHd8hQ_cHMWJRICCeIJ-3Ef4vtl0BuACG-0r_wetHbb5rxwYHkRE2ht4lbuJ2qmHXovISVAJjIpOxL1-JYIO9qmgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#نوستالژی
؛ هتریک رویایی علی کریمی جلو کره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102682" target="_blank">📅 16:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102681">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102681" target="_blank">📅 16:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102680">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmhAxLhU0z5G196wG4GSEPRI2rxIZUDufWIxB6RnLP0H4Wombqmb_2D5EAwUEqrGmaScH2t_xjB6VYCb82TqRNpXiTZ16UqR-4ox8K9ltgIU-OKdbWLvhbs2RgkTaquA9HrQegZ-s-0P6i1rXOqnioHTRSurQZFzxGoojmgyRTMKguivSLnPUB5tr4xBNFzq6RUsVZZ5X3DJ0fY-Q68oS8YMvTzlksIiHEHW_6b2N7NUWUe8j2XvyIs7tomcLF-bGH1AI5gNc3QEBpQ1a1uF3cm7n_JAAQ3xmOKiKKjORKeerpFb64j9Muhwr87Sqgs5nItAZmjq9dAhP3FKaqWkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
🇪🇸
آمار جاودانه کریس‌رونالدو با رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102680" target="_blank">📅 16:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102679">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102679" target="_blank">📅 15:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102678">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_gAsO4fwokhWg73phhtb0Hzyxx1nimNG3gVv5-vG6_f7FEBJOugILEfGFY5GN2iDmNoUxyeFYYtaPFz03SB4_1P3qpwJHaDlvpqKcYTjmGQ-Zi_YT4iKZmCMpa_GLhQXqfSwylNjNcMDPPiNM6nrb3GpUUUZWI-k4TweGW7L2_ZUVhU3k7ZQrhTYmZi1EOgN114ml4Q6JjVLX6F6Jm0YRN9awcbO21b8a5PGJZqCTFamiaqgz7w2W3M4B1_qKCIhWv6eY-FQZy6TXP8T93z9Jr91PAuXACqmgbGEVi6Ntq2vDoMiAKSgbMRHC7cAvPD-zSechzfHZck4GdSCGlT6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
💥
عملکرد ۴ مهاجم برتر دهه‌اخیر اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102678" target="_blank">📅 15:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102677">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PodPkMOONQRiKN1ZULP-VEZMy2SFnTLRmoH7jjJrGDoW3ga2lDWDpm5TRWl1oIGA66BTyGG--RqIn9FTWMCyw7N1m6aCePdNCNDu6Bpscgf1gOSDbszP5iuZfRUgUH6gfUSNaDWncK7TBcxCy0lDjWeailgHwV50-1lwKIeZ8P7Fdlg4-OTYJp-roPwlPRd7FZ7ekZHyTEoeOE8py2Cg6vwfA9Y7e72AhInL7WN1Du4uMJojOkMAfC3tNAttsM9jNnu_HtJ4aeCnpMVr-PwuCTzfaxwpT3eu4ok4BykD8ejJrXRFvhmuBF02Xv8f-d1qopyva_LKLXwg4XbUmekQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پاریس؟
🎙
فران تورس: خیلی خوبه که باشگاه هایی مثل پاریس بهت علاقه داشته باشن! هواداران بارسا باید احترام خودشونو به من نشون بدن تا بمونم، فقط باید بهم ثابت کنن که دوسم دارن و بیان باهام برای تمدید قرارداد مذاکره کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102677" target="_blank">📅 14:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102676">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b59000aa4.mp4?token=vwd_j7NI6bxEj5kynlSpV7GAjKlpYCoq1JXQo97c-tuaXFvEQpe-jxJkporhasONJNFyqihMAwZpvOI9ccYEvciFTqHj77xHirgtOYbpY1wgI0PYUAMQu0TIFguCnCh66e3QUCJOdRlUtX2LAgGTXAaPyAATEyIKAX2whZ5hgZo-pZzFzebhJmFY6egIS5XWkIX9hRku-BCykM3LuDhNZhqeCG2MxQ8-iGV7c5vqSnZR7Y2ZVt7PdInQQtqxqsS1epnmJZxDwhMYg4H6nMD5IMZeF29WJkrZHRRRV1mUVrdmCez4ERIKYUdDSB5sP29AmOdSBlZpYQ-qVkleDTqOig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b59000aa4.mp4?token=vwd_j7NI6bxEj5kynlSpV7GAjKlpYCoq1JXQo97c-tuaXFvEQpe-jxJkporhasONJNFyqihMAwZpvOI9ccYEvciFTqHj77xHirgtOYbpY1wgI0PYUAMQu0TIFguCnCh66e3QUCJOdRlUtX2LAgGTXAaPyAATEyIKAX2whZ5hgZo-pZzFzebhJmFY6egIS5XWkIX9hRku-BCykM3LuDhNZhqeCG2MxQ8-iGV7c5vqSnZR7Y2ZVt7PdInQQtqxqsS1epnmJZxDwhMYg4H6nMD5IMZeF29WJkrZHRRRV1mUVrdmCez4ERIKYUdDSB5sP29AmOdSBlZpYQ-qVkleDTqOig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
برخی از ریدمان‌های اساطیر‌فوتبال :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102676" target="_blank">📅 14:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102675">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsCq9nrrBZc7lB_j5-JFDT8toDoZu_ex3bjytn_I9VQ-YpL42TCxUhL2dWrSaZGR3QXJbv68jDWOJvCEnMvWLYsPokfY4KBRYINNChlSG1WruvIe-aI8J-trKvxo-636Y9UW0P0R8Mlr5WfoZkwIk0K_8Vp-StbxLzFidSNoYnd9QQeA-hx8uAPIkGGrwDZldjKl0gSTVO7EZ0KdVi8xIMv793vqTZ2ZWdLuj7mDuztRyR_rzv7--MgTnTjuIayZ-BAO2smm22CZYAJ4m1AXZGZg5khm0GDM02TJ30g1V6fAUbOjMr5IyBXuIHDP7OpCjxfSqetmVX1tAFrQiNVlNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اولین جلسه تمرینی ژابی آلونسو با تیم اصلی چلسی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102675" target="_blank">📅 14:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102674">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102674" target="_blank">📅 14:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uddSkdMqVbiVvHvKEFA2YBT3yqdXttXqOU4inZe0TFYpFy3Hs_et4i_Ti8IcV80RMTCM4lqr5_ayiA_ApwWRKC6OyVFFcymFCRv6Ctd1gpKfOQTzfq91GF_dvJHeEpObgpxnKhld-55DSL5LEJ-FYrNU7h-y0MbFgJnaWTsuA5HHjPHugPiTd0KthgrH4STTVCoi5MNIfMmjiC-2MDoR_0ErNxyDh0rKehZNlqJicgQla79PBv4mDJ7mqMIi2KdpoaZtJRlkpmD59s6bKqu52y2gbMmgQeQxmxdY1RNZqD3QH4jUpt3kcRA4cSvmQKMNbhmk740ZGunGRgwv8qKDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس سنگین ایکاردی به وندا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102673" target="_blank">📅 14:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102672">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
شهرک صنعتی شمس آباد انفجار رخ داد که عضو هیات مدیره شهرک اومد مصاحبه کرد و گفت یه مخزن ترکیده و چیز خاصی نیست نگران نباشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102672" target="_blank">📅 13:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102671">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYneKf2wQNk7SU92LdR1uNwUFprIhxhB-vEHjivezSFNOWWgleCXKmnFzLC8ghjXz5ptvu9Ca5BFJ5aUmiJAgCnGg2avmmM24W2ia71VnJppefOgv06F0eMvn-sTGskRwuVBg8NRVugWVB1YzUYcyBtoQ1Mul_KqUBRY0HTTC57EXiDreToO_4Pcl57mVdorpBiWJr1yCjWOozOhqwy4yLm7AGwfwekRnC7hjAexl0jI4uTFt5kdoo3e1ftgdr2lStS-1pI9NxgoVcV0iiMkgriKsBFPTqO6MLMgB9c81fHPtdn9_Mqm5od4gYhe45Tq07vA4GewEctrNN75aO-DZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تو سبزوار یه مرد بخاطر اینکه زنش پیراهن امضا شده پرسپولیس رو به اشتباه شسته و امضای بازیکنان پرسپولیس پاک شده، درخواست طلاق داده و به زنش گفته که کل مهریه‌ت رو یکجا میدم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102671" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102670">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627a83e0e2.mp4?token=rAvlGOb1ifLYVlnAMuIXqmkcKnZUZDW6ZGuaLePr9zS3FSHXXYpHYVLaKuKIaQJ68yA4KM_nz9BwHOnniyP5kobMPMoXInqaM8e4yGaGL6cDORiHYVoDyzDnUzuNE4yoqM_0tK3Mlu7qJneo9OnpY0LV-T1B6YdPvzaX9-xPCqhppitQz1x4COoIyc0mWTVeHTtJpTCQa_yyyj6HeHk1kfOGakrQ-lw9GN7cmQBVOhB6Cq5s6n-6nZkWhiIdImbZIafCH9IdGhPnUiJRM-30PUGtA50udmCx2jgFrmVnQJy8d08yBI3FPKqiCVRHIX97RLzQhHNW1rOuVODPXRU0_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627a83e0e2.mp4?token=rAvlGOb1ifLYVlnAMuIXqmkcKnZUZDW6ZGuaLePr9zS3FSHXXYpHYVLaKuKIaQJ68yA4KM_nz9BwHOnniyP5kobMPMoXInqaM8e4yGaGL6cDORiHYVoDyzDnUzuNE4yoqM_0tK3Mlu7qJneo9OnpY0LV-T1B6YdPvzaX9-xPCqhppitQz1x4COoIyc0mWTVeHTtJpTCQa_yyyj6HeHk1kfOGakrQ-lw9GN7cmQBVOhB6Cq5s6n-6nZkWhiIdImbZIafCH9IdGhPnUiJRM-30PUGtA50udmCx2jgFrmVnQJy8d08yBI3FPKqiCVRHIX97RLzQhHNW1rOuVODPXRU0_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
روایت‌ایووبی بازیکن سابق آرسنال از تقابل با مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102670" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102669">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0lnW2zh2935B3zBXcON8noJY6Fe7cw57oJn9Rk0gVBFagS_G8nbHKuw2K3aTAV5IWnmD4x6vsd1mfQ_mAIXKiJao2v6SiSy9t3c2BH4LyZ3GSq9YsIx-pbiMGGI5vv19bVv0p3IJY_NQ6KMKcNiSL7iwuheTFUTCffIhWPOde4qOyv_AIecVYz5SugwJ5CiPk4QHCDkwbWFl3begoeiYWMpeR-8DlWCrIdLca4wdiYb3FSXi33-9F15SgLT_tsBI3-cV4asnlCFGCAOT2teBKpLpLQ-rPJCCJYn2fpvjTzh92jO17nSqjIPny58neJvwVvYS543vq3legOjLsvSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
متئو مورتو: باشگاه استون‌ویلا درحال مذاکره فشرده با اتلتیکومادرید برای جذب متئو روجری است و احتمالا تا ساعات‌آتی این معامله نهایی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102669" target="_blank">📅 13:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102668">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e611ac196.mp4?token=je4TKnCHKyRcVC73VvkyiAtdHZvsa050wK6LqSXgJWux5qRnfTuY979xRPNzjboz2GhbDK6ORohgNRbBtpyqYeJGXP4_FqeKZfTCxKED201uYNKnRvNKtXBnjWx8sBQeYrrySSgCpoIheGMb4GD2_VIkY-Kr4m85ZlM5R7xPiU4snUG0-WjBysigFNv2GtpzlBMJoq9jqo0HNSyFjrxi78xt5lBjasmI2E9-gFN3JeSDZhufto30Qs11Xw9zJHeP7NmcDQDhV8xmbIMuctnwohjb5uO7q3Lp6lI3Y8x8AmQkBx--6EXjc0Tptpjbsoufkm1s24baiq_ZwUZGTYWQ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e611ac196.mp4?token=je4TKnCHKyRcVC73VvkyiAtdHZvsa050wK6LqSXgJWux5qRnfTuY979xRPNzjboz2GhbDK6ORohgNRbBtpyqYeJGXP4_FqeKZfTCxKED201uYNKnRvNKtXBnjWx8sBQeYrrySSgCpoIheGMb4GD2_VIkY-Kr4m85ZlM5R7xPiU4snUG0-WjBysigFNv2GtpzlBMJoq9jqo0HNSyFjrxi78xt5lBjasmI2E9-gFN3JeSDZhufto30Qs11Xw9zJHeP7NmcDQDhV8xmbIMuctnwohjb5uO7q3Lp6lI3Y8x8AmQkBx--6EXjc0Tptpjbsoufkm1s24baiq_ZwUZGTYWQ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
اوکراین دیروز کسخل شده و با پهپاد یه ساحل تو روسیه رو هدف گرفته که چنتا مردم عادی کشته و خیلیا مجروح شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102668" target="_blank">📅 13:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937fee7ba7.mp4?token=L86nNkaTxxbkgnsxYpPZZuPY4BQ8hvOrbEoDPFaoDd6SfqessfKGAcl7bcSeqRD4YlH_wjgrp9kfbl8CbNr-bVKTV-C6lQFdNQBwBERyOC4MXRAX141T8mnaelfYBtwWqZKRSSghgFNcbY59HeUBQ4ZOvaJL4PoTr1vsJibDyhWI68Ra38E9_B6ecoAiYL8EInkY4XBUVpoutR4QlXhF-eFnCCZoSd7atNasmKTMDWaA7pvL4XRp6n5AhuOKsOpsN7mQ7ZTvM9Hw6QdDPUcqw-HRx2cSKR4WfSS266XvOjiiCJ-5PjdoBB2tgZILoaCIlqyz9jgfEIMYhrfm7PqoWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937fee7ba7.mp4?token=L86nNkaTxxbkgnsxYpPZZuPY4BQ8hvOrbEoDPFaoDd6SfqessfKGAcl7bcSeqRD4YlH_wjgrp9kfbl8CbNr-bVKTV-C6lQFdNQBwBERyOC4MXRAX141T8mnaelfYBtwWqZKRSSghgFNcbY59HeUBQ4ZOvaJL4PoTr1vsJibDyhWI68Ra38E9_B6ecoAiYL8EInkY4XBUVpoutR4QlXhF-eFnCCZoSd7atNasmKTMDWaA7pvL4XRp6n5AhuOKsOpsN7mQ7ZTvM9Hw6QdDPUcqw-HRx2cSKR4WfSS266XvOjiiCJ-5PjdoBB2tgZILoaCIlqyz9jgfEIMYhrfm7PqoWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
دلیل اینکه چرا کورتوا یک‌دهه جزو برترین دروازه‌بان فوتبال اروپا قرار داره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102667" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102666">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=lauvV2FFJVHo2MTIth5cE0mBsD32ROsHo2wg1p4PPbZhK2KMbrI7ucU8M8cmy42hDJ6TUCNV6tjs830uTbbM9TAyxVHCbxSUGMqIEmf6mdpmN3cbLPkZMqgd5br-gS8UGd4BizJsJJlfM9CrEedLCQkptYxnILDTsJiHltB8me8j5DzSVQa9eno0aLoYej9A38SKOggMtMv5kNKdt1DeEgMf0tox0YV9cB-Lx5dA6RSP3CVwaWOxKIC72dHLQqggPRnZzA4ROxdtJyXPjWGfes3o900gB1pRURZRR_IcvID-5acpKw4eNzwed84rW1tCIl78GsMC9n4Y7aoFw8WA-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=lauvV2FFJVHo2MTIth5cE0mBsD32ROsHo2wg1p4PPbZhK2KMbrI7ucU8M8cmy42hDJ6TUCNV6tjs830uTbbM9TAyxVHCbxSUGMqIEmf6mdpmN3cbLPkZMqgd5br-gS8UGd4BizJsJJlfM9CrEedLCQkptYxnILDTsJiHltB8me8j5DzSVQa9eno0aLoYej9A38SKOggMtMv5kNKdt1DeEgMf0tox0YV9cB-Lx5dA6RSP3CVwaWOxKIC72dHLQqggPRnZzA4ROxdtJyXPjWGfes3o900gB1pRURZRR_IcvID-5acpKw4eNzwed84rW1tCIl78GsMC9n4Y7aoFw8WA-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇰🇷
هونگ میونگ-بو، سرمربی کره جنوبی در جام جهانی ۲۰۲۶ مجبور شد در برابر مجلس ملی کره حاضر شود!
‼️
او توسط نمایندگان مجلس درباره تک‌تک تصمیمات تاکتیکی‌اش بازخواست شد. از تعویض‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت.
هونگ در ابتدای جلسه از مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102666" target="_blank">📅 12:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102665">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9e48b7ed.mp4?token=LiHI1698vRAuNF-RNJVRRIGueS_TRUfxbLrbfuRxklJOvAy8sVnyjn948gUPJqnSUEUrKi93pv0q4oKgTennv3mSEbv2GlLDORhR2Qp-rKKUeocQwzuU7ax0o41C2IwiaaNdCIe5yCnLC4WvpIFwnt96mNbXqcH8mjP88kb8pjvPqvi59jwl5_IzVeOTFYoXATV9RXkqRVu2pcpcFNxPEzHj-HIAyUiVJ1IIyqmDqQs__DWT4x2b-MpLQBqHVNRvaCYqQ5Mc_wK1v8S9zLb1x06ItKTu0qCOMdx1NcDyDYUyRfCsAnm0cC-SIdF62SjNp_w5S2KTyJiUINOEtRSAbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9e48b7ed.mp4?token=LiHI1698vRAuNF-RNJVRRIGueS_TRUfxbLrbfuRxklJOvAy8sVnyjn948gUPJqnSUEUrKi93pv0q4oKgTennv3mSEbv2GlLDORhR2Qp-rKKUeocQwzuU7ax0o41C2IwiaaNdCIe5yCnLC4WvpIFwnt96mNbXqcH8mjP88kb8pjvPqvi59jwl5_IzVeOTFYoXATV9RXkqRVu2pcpcFNxPEzHj-HIAyUiVJ1IIyqmDqQs__DWT4x2b-MpLQBqHVNRvaCYqQ5Mc_wK1v8S9zLb1x06ItKTu0qCOMdx1NcDyDYUyRfCsAnm0cC-SIdF62SjNp_w5S2KTyJiUINOEtRSAbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
گشت‌وگذار امباپه و اکسپوزیتو کف بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102665" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102664">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmcbSASf6ahmdruyUaRKsgcUXVL14JQ-qbN6Hj7Tkwxa5Djlrg8hK_rYPSCg20newivWtSf9qqPmPBqDY9zmJ0dznP0i9ZdnCx5v5mz8wAfAdO9wxhXaNmTPYVDe0XMfFF8oTNJdzEtv3anVxl3P7z2qjzfT4jVhnr75w8TuvN01Gif3EyW1Cv-W3hd-YG6e7s2nNLkW-uL9cQl-i_eAurDBPxuAjjm58761YqvPsUI5IDUd83-63yheed9slqaapdAu6EoALg2m3RdRY6BlITnsTlu1r7trD8gnDPYwIC6KdXx63Q6a0SKb6rXCLxBB2JV9nzuR_8t_Gml2XBBRzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🟡
فلوریان‌پلتنبرگ: بایرلورکوزن درحال مذاکره با الاتحاد برای جذب موسی‌دیابی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102664" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102663">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnX9hYdJfHUcpFrxrmy1N4lU-9IgLf0-ea-s3OPI7fDCXBnVnrvBp15inhnBuWGK1sXbDjIqJwctk6cEHcDzeeB0tnBSLzR72qGqfUmjBCFVw6cTw5pqrSMAxRPwL5JIe2lWZWY5GKrH8JvHvR_EMEZP1qpivGko8Q0psYBVPQJa4SVf9VY36xF07UQw1TpvugZe-xOv6uWzJsljH8R8CLVs7MwVVro8S8Mz6AbstU3GQAgrP4xQzzMZBUUylwFB1JXMXg5f1vBusRnrxdhhZ9JmOyGv1LS0PBsrtAs0RZzJWpprrRS-uyta8s4xMvxHyN8GoLaig_CRToQBVRJPnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚽️
فیفا با انتشار بیانیه‌ای خبر حمایت دونالد ترامپ از اینفانتینو را تکذیب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102663" target="_blank">📅 11:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102662">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbXjX9KmSLLxNgUrMt0ha5tXY0j9ORg298_EFKNRMlpos2iFdXCcYausWGNKGBcFC1vyBNBt0JmGyg9_fzif5nKOSgr_rUcuQzpm3qR_Gqekz0G5GAyxowEmD_YJED7xT2ao5VDnXB5NelSBcWAXfNTomXm90PG700PziUviuqdiUzdtJoqeS1kHzTbDq-4_BpWRueWhB-7vfYg7eroK-aVhWtkTSFKkSczroLZ_lWCT90iDRtIVO7eRi4yhfL4i8NO4NRRx6Cxh4uHPkV3PTvBO-JqQRiEUq7_hbRBvOlhjufs43tp9Vymk-D-N4kZN1GMi8fB_dNoW101Ox4GwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
⚽️
#فوووووری
از مارکا: رودری دست رد به سینه سایر باشگاه‌ها زده و گفته که فقط به رئال‌مادرید میرم. قراره بزودی این معامله تکمیل بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102662" target="_blank">📅 11:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102661">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u5DjSSrdO-Nz6VOhVRAgYzAhiz8SktEqAuj3rKmJ9yCTAZK6nSNEItJzIdARcEMNKlZGXx4EedIsLWYd-l2Pf7eazxrEZbIl47mkXbLwIFokdxDRslrsfIaGYeclfquWLwrz8XSQbWZHBuXzarOLID4J9I6CKgxOFxXEiu6u2lesihOqWO90T65w8K-3gFGeLuglklLcGIIqJXz80clAYDzKldXga7Y3bhyLfcThZz4fUro1vNjlircbQrX5TsDISn8oOQnqned-XkCDgQECuSyA6SVgpJxISzyE-ca-j5CegfxdDI7fD_XAMMJ30l7GJiSeJltgVu_Hz1Wc62JT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#رسمیییییی
؛ نی‌لاند دروازه‌بان تیم‌ملی نروژ با عقد قراردادی به لایپزیگ آلمان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102661" target="_blank">📅 11:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102660">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
‼️
😆
😆
🎙
ساکت الهامی: 55 میلیون تومان دادم کت شلوار آنچلوتی را خریدم تهش ۶ تا از استقلال خوردیم و باختم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102660" target="_blank">📅 11:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102659">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFozIT92OyDsZvmGbDL6pdiRZoA0ORcwwVnuT-E_Tamg5bB3WD1qhUxtOwlfyMRAZIgrd3dX6-JIqjfX_517SHXTO7yk56WJ0jV-Mgwm9KrBd6QP6L_cPx9nzYPZuz3qDOX0v5Y332uuuWrGaOgCM6Vb2Ge24Hi45HR6zCRJnhCtZ5XJixGhMRCPkwF1cH-Q5quLO0y-iyBUMhOL4lGeHFUntjgMVmdM3iHxG04mPrPx2jvG5r0sqolgHHcrLhR7xyzhZvQ8yLmlPBFig6-CQrolCMS7Ik6JQi3qf7mUgW9efq_bjXQKZEEIQXUs0YomKd69u052UH7n1Q6QTVMUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژاکس آمستردام از جذب مارک آندره تراشتگن به صورت قرضی تا پایان فصل از بارسلونا خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102659" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102658">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf1a57969.mp4?token=eg84m10_wD9NHsYz0BnWq-_uJhn-RbuWcj3FukbrlI7s3lqwVaZ3O3ELyD0IVUUFE8lT1xqtGJBI3X3l_wtjTnVAi9yO6Dq-C2F23TrCHJx-cO8-uTmZ5sCB-kNmdKKAGvb5QAxVvqWsSYmGNd3kApE_l1YI46jEukRBJsD6OcofLkekHRhLVbR86BHUJ7UowkpLw5mXIBkEdu8Q8Q7BIr0fsZPK-gAxa4wXxBGRmVj7uhQpo_lm9s92u7egMXRSB1YaqljY7DRc-w62pYKGGiEzZIvn0ljRu9MdSyAkF494APrll7cNrlpTlsgI1wA6bA2c8ZbNjhBDLtI3u0uCPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf1a57969.mp4?token=eg84m10_wD9NHsYz0BnWq-_uJhn-RbuWcj3FukbrlI7s3lqwVaZ3O3ELyD0IVUUFE8lT1xqtGJBI3X3l_wtjTnVAi9yO6Dq-C2F23TrCHJx-cO8-uTmZ5sCB-kNmdKKAGvb5QAxVvqWsSYmGNd3kApE_l1YI46jEukRBJsD6OcofLkekHRhLVbR86BHUJ7UowkpLw5mXIBkEdu8Q8Q7BIr0fsZPK-gAxa4wXxBGRmVj7uhQpo_lm9s92u7egMXRSB1YaqljY7DRc-w62pYKGGiEzZIvn0ljRu9MdSyAkF494APrll7cNrlpTlsgI1wA6bA2c8ZbNjhBDLtI3u0uCPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
پدر تشریفات ایران آداب استفاده از آسانسور و پله برقی رو بهمون یاد میده که بنظر هیچوقت نمیتونیم رعایت کنیم
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102658" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102657">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0e4679b6.mp4?token=EI_6HTaKTj012GwVCeMwVP0Eh0ojgqsiat9sT1CxRvyCwiy6va_h-7Ssu4W7hKddRIU8sTwQNufDvIdCSa8ZvhFmiWpgPrm5epcejSqcHUIfIAicJn_5YlwXcEj37w0tvusXVW48ReQZ8UjEiAalmFfV1wrieOhnlV6wVshrWitxkiSjmKoPN9MEIArCzITmEVywIpQQoSq47yHJ6PhK5tOLh5VbmYGqbhCLBQATV3XqReOmTQb-UVVPvND-0tbL_Evhp56i9U1fRMDhMjl4MZLycKesr9I40zM9pjbnYIotnWZnPkGx3Lyaay74x_gotu1diJZjcDt6muQxyP6MB1-JWggCERjU_Ro0h3n6E-8bheVDA7izotvnjY6YEfTCk0gQqUrTT09JiYpseOTFphKTP-tjKBM1sv3YAgZU10pn73hSZiiNZPPRgdJLb46Beukej-wGCQhSpC4UMTfl6C6t9V2NySNBBVKn3NzE3gkqOLIgaURklB19cunfeg23QRPb5dr4bzhmTd95MxeFb2AswLH8cE12jNdNVDilRcdUJj_BezNfqhyeI6LmvV-dul5FB5vBQltdDumOlWpFKQHvkXwJqf7ToCEm2HjF9CEFoB4QTDPf-mC8LGIB2WNLnSNzDfVKcg22ggmP0EwAnkdZvdSjfiY4JPNf1YAf3VU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0e4679b6.mp4?token=EI_6HTaKTj012GwVCeMwVP0Eh0ojgqsiat9sT1CxRvyCwiy6va_h-7Ssu4W7hKddRIU8sTwQNufDvIdCSa8ZvhFmiWpgPrm5epcejSqcHUIfIAicJn_5YlwXcEj37w0tvusXVW48ReQZ8UjEiAalmFfV1wrieOhnlV6wVshrWitxkiSjmKoPN9MEIArCzITmEVywIpQQoSq47yHJ6PhK5tOLh5VbmYGqbhCLBQATV3XqReOmTQb-UVVPvND-0tbL_Evhp56i9U1fRMDhMjl4MZLycKesr9I40zM9pjbnYIotnWZnPkGx3Lyaay74x_gotu1diJZjcDt6muQxyP6MB1-JWggCERjU_Ro0h3n6E-8bheVDA7izotvnjY6YEfTCk0gQqUrTT09JiYpseOTFphKTP-tjKBM1sv3YAgZU10pn73hSZiiNZPPRgdJLb46Beukej-wGCQhSpC4UMTfl6C6t9V2NySNBBVKn3NzE3gkqOLIgaURklB19cunfeg23QRPb5dr4bzhmTd95MxeFb2AswLH8cE12jNdNVDilRcdUJj_BezNfqhyeI6LmvV-dul5FB5vBQltdDumOlWpFKQHvkXwJqf7ToCEm2HjF9CEFoB4QTDPf-mC8LGIB2WNLnSNzDfVKcg22ggmP0EwAnkdZvdSjfiY4JPNf1YAf3VU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
▶️
آخرین فصل‌ لیونل‌مسی در بارسلونا
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102657" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102656">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برترین گل‌های محمد صلاح در تاریخ لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102656" target="_blank">📅 10:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102655">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLy-K1gQSRpLSfXxggP1BKGS9gbenzrsmajyCH9arlnuxOHLv90prclfFIV63Iuq5C3ltXei3lP7ESnev46yvBALtBokdRdSef0iBz0AC3IcygdXl0Hn0V5cRMofeBWVgepkRD6WgJBQMmrFMPDWV9bS8bFRmr8ktC6zSsT3ByVO2CeJSGZ4SGoSo78DbfaIvovcNwF4_N83t6-xxXI45ET4uectC0-0S8vI0q3eG_B_tjpTlTabFsdTS_mqKnQkI2zZXIwjgMGx9CA35rRrfUzH4Ql6Gh3nmdFhKU0izYjIhbic2__mkq8UHK3NM8bTc2ZeLVgxjhS_woZd6GaHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
مدیرورزشی لایپزیگ: دیومانده به محض بهبود بیماری خود به اردوی تیم در اتریش ملحق میشه. دیومانده بازیکن تیم ماست و به قراردادش پایبنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102655" target="_blank">📅 10:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102654">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👀
🇪🇸
🇪🇸
یادی‌کنیم از بازی دو سال قبل و پیش‌فصل الکلاسیکو که حسابی جنجالی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102654" target="_blank">📅 09:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102653">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
‼️
😔
🇮🇷
پرزیدنت مسعود پزشکیان در واکنش به جنجال‌های ۲۴ ساعت اخیر: استعفا نخواهم داد و خواهم ایستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102653" target="_blank">📅 09:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102652">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f47080196.mp4?token=UT3UwgGsRhivqQgAc7dD7wSlaZXCAIZXhrqtrQrqIXkJ29FCEdRWDm6bDNV4A633GW492YdTFSGptd9-UVc-1FqwuzZMnbUMkIrcviKpuZhIF5LQzvzlJkQ40zLeyk7rzUDKk1aBXhnXluuQC_TnD2UEV1O-j6LQsU8KS5GzYEJYFbDdmxJkM8CDHe9ixusgR85gjKQBJsySfFxJxOTM_FB8nc4HQlnHCy8Fjv8M6hDaYMlzURQjvNxGc04xid4Poz75DCvH7qxUy6Wv7e-OXxsR6Rf2XdhhWJuRYReqXn7vN_Yc4AvnWzi7ryFxoor_XIO3rsGPxy2aG6Uv9KaQ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f47080196.mp4?token=UT3UwgGsRhivqQgAc7dD7wSlaZXCAIZXhrqtrQrqIXkJ29FCEdRWDm6bDNV4A633GW492YdTFSGptd9-UVc-1FqwuzZMnbUMkIrcviKpuZhIF5LQzvzlJkQ40zLeyk7rzUDKk1aBXhnXluuQC_TnD2UEV1O-j6LQsU8KS5GzYEJYFbDdmxJkM8CDHe9ixusgR85gjKQBJsySfFxJxOTM_FB8nc4HQlnHCy8Fjv8M6hDaYMlzURQjvNxGc04xid4Poz75DCvH7qxUy6Wv7e-OXxsR6Rf2XdhhWJuRYReqXn7vN_Yc4AvnWzi7ryFxoor_XIO3rsGPxy2aG6Uv9KaQ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
روایت دیوید بکهام از میراث فرگوسن در یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102652" target="_blank">📅 09:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102651">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5Edg6He4eU0mPjQnbCSQME3Id8RrgvgHxnxqkxXfONGzz0Mzra7fVKo6L0UY035ES9Fp8ldxYCysknKL0nexwKrDRGXHboTkud3Vn7q5M6plGUAYdt5zuXC8RmPltjbFZJRbvnvoKAliHw3VlfVhzOCJ7JcmDBy0gcNCjgzV6jXvcHDGzxly2qROP0JcLhPM5A_l00KumblD9wzono1mnyBpCtnQDyQRVNdGIxn7dex9t-Ma58NZCAlrWgR_9qjwsPYikNjOw6XyxP-KrPHOvYEBFMYXqXwuOuzWGwyWmxFv7husoPgEII6x3Fm-YtnEo_pK1-cR5puSxidVDablA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
کشور عربستان سعودی در حال ساخت بزرگترین شهر ورزشی جهان با بودجه ۱۰ میلیارد دلار است.
🤯
این پول معادل هزینه خرید ۸ بمب افکن B2 یا ساخت ۱۰ تا برج خلیفه ست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102651" target="_blank">📅 09:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102650">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZ34jsUdGzecSSiGob8D0OFw9rKxUndYHQPgEFop8tqyMSfoozDu3H5wHCi6-ZQPoivYC_VihsQHQOLlMPdTGvjCaQNcXBzguwK2M-N83E9HnrZRwbNQpD-__JkOAw4t856CMSSBYCKao956Gi9J4NWUHANBj9cU2NGMf230XoaSCyDkBkJmNerSCb_NF8PZ-xA3nALpXm7F3DsBETfKedvN5VxgXmYozWzAGEjbO_IZhdf3XJiOE4Pz14ypYZ2DEYOICwuAVjfoIe_C5zlhXYEGuu51AfWSwLcl2xGPCWrPwOU_N5MlicS2T3BpUVyEd8eaWd0XHkHJ4Y5F7qxt7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه سان‌انگلیس: باشگاه استون‌ویلا بدنبال جذب مارک‌برنال ستاره بارسلونا است و قصد دارد رقم ۳۰ میلیون یورو برای جذب این ستاره جوان پرداخت کند. هرچند که بارسایی‌ها این بازیکن را غیرقابل‌فروش اعلام کرده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102650" target="_blank">📅 02:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102649">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d8f16631.mp4?token=QLQcd9B68au28NbGqZHqILxTSsZzoh2icVAhjsV4WUi53N2WvB4cvSsetCTUxKC28lMYq2v1TMk5ND2SwENqxDvq1Yld6hUnS81swrndxJqN3vEZ57a_YZ2wqzMWRKpjI3Z7guM8hDPGyKNQu68YrVesA8_YvrSCULeU9wK3dmABA8mNLEp6Yc9nEtWnRexnVH2mYnOly5QyXB3AEzIMPO2wVbZBuirF9hklADXjzXkUCy4niQwfZ1PCDo-dO2mCfGL3rEkGbgHWdphu8EXD47Z-hokxwCwMUkOLxruGSFTJkI7A_i4gTJtaSQ2L3DLIhXhXCw-LSZoPip-Llp2UNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d8f16631.mp4?token=QLQcd9B68au28NbGqZHqILxTSsZzoh2icVAhjsV4WUi53N2WvB4cvSsetCTUxKC28lMYq2v1TMk5ND2SwENqxDvq1Yld6hUnS81swrndxJqN3vEZ57a_YZ2wqzMWRKpjI3Z7guM8hDPGyKNQu68YrVesA8_YvrSCULeU9wK3dmABA8mNLEp6Yc9nEtWnRexnVH2mYnOly5QyXB3AEzIMPO2wVbZBuirF9hklADXjzXkUCy4niQwfZ1PCDo-dO2mCfGL3rEkGbgHWdphu8EXD47Z-hokxwCwMUkOLxruGSFTJkI7A_i4gTJtaSQ2L3DLIhXhXCw-LSZoPip-Llp2UNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا سپاه به پایگاه آمریکا در کویت حمله کرده و آتش‌سوزی رخ داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/102649" target="_blank">📅 02:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102648">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇪🇸
#فوووووری از ESPN: رئال‌مادرید پیشنهاد دستمزد ۲۲ میلیون یورویی در سال به وینیسیوس ارائه کرده و قصد افزایش این رقم را ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102648" target="_blank">📅 02:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102647">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPd7VA5pG2KChRratn4hFfJvP31Ck8x0dYUwXRPdBkp8w7M5QcVt8Nx9GUS4_1wJOjs1duNq93akkd5TB-cUW_t5_JinrHr2Xp5FowZ2v98SXuIotOnxI8wy2XJXiuLkz_DE_D98dUzZzbdUfHzM0aJABSJZ1dV7sKYZ13014KVf7mYoGtA6HuOC2hhi63ekmPRASNFypigZuBRzbKka5Y_sFnjgs-93UAK5Xh4b6yZR-8yVYyR3RF--9-VYEsJoz-FQyChiZ-hJbJKraGPdjcMYP8HYaC4gZh4bNCuGn36FwZuxKmp60Sno1OwHlXnaZIpS4zOPqV-cVPblVl67hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از ESPN: رئال‌مادرید پیشنهاد دستمزد ۲۲ میلیون یورویی در سال به وینیسیوس ارائه کرده و قصد افزایش این رقم را ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102647" target="_blank">📅 02:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102646">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtY7odiUD6aU554gaIlBqmkNI--IbEAblph5Gh-6akL8BtQxHHchy1eIU7IjRjGOihOYZ6iwd_tKHfKaGa8Yf2p3U6dXNBMyjM7nr6jO38izWk9mflPJAAPwzns_H9gaAYW51AbCQZVVw474r2RQi8fVP-Copb9eYzxrLzHnZTwRUYmBoygagH67cBIBcvmzlGpb1V-6QqyTxjIK35dph5tqStlKl-Id4jKE-duKlV11g9mJOvSvdkixvf2Ic-y-YxF9H2QwLyGmPHNtYQ-FyRlkTjcOloZpZleeXpQqkWEdT7RpfmKAnk0hl2_FtjQKk6WvA8NIa6h6-ZXC90j_0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
بن جیکوبز:
چفرین و ناصر الخلیفی در سالزبورگ دیدار میکنن تا درباره تحریم جام باشگاه‌های جهان در صورتی که اینفانتینو همچنان رئیس فیفا بمونه تصمیم بگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/102646" target="_blank">📅 00:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102645">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMth9PJgLVsIt1BGqQQcT-9_N_SOVwomEfH_JcBMBUJWM5AN3psa90oASGCsXSh4sF3MXxpYbhZ61L8rZj2lEUaiodkEemlz60_QX5azS8Py7mkrdEQv3hgF26N5uVJnjPWNbAsLTxRVYHcho_6k7bri-JzizgVgRKe4o7a26PC3MCX0702wELKOxQk5gQAJckkp3mvTbgrOspmhvPzCw7DQ5iV5p8AS-WUTIUTamzJ1iqSdQcUCsischOHKOy7BZvN2pwY56jnN6Sco_r0pQYgd2UktilnNbYwplCCMlm4p-QMJtRK68EZORi3uN6T5pHPDur8_9mcOb0R2Qy4GxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پاریس؟
🎙
فران تورس:
خیلی خوبه که باشگاه هایی مثل پاریس بهت علاقه داشته باشن! هواداران بارسا باید احترام خودشونو به من نشون بدن تا بمونم، فقط باید بهم ثابت کنن که دوسم دارن و بیان باهام برای تمدید قرارداد مذاکره کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102645" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102644">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102644" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102643">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Re__ic78wZ-1TC5fwhYaWLnMTnHls0pE9B7g1NAP66sFf714eBlYo0ZUdr1KOiZtldpjrqZiEnOeKWR4plwiOYCviaz96SXd8514zCeDZ8rUMBNU8T5iRsEh_TuoH-99C6BLVuIxeQ6aJXBqVjc5Gw6yG8QR-CssjeKNpWdiMC1MmLMY61S01YcBS5C1WgDwijnR1mHsAEFB8fRqk0kZvMpc7Pmh9NO5Z1VtpWZUzsEn4G69WIbLdDTyu5JxcIC0LlBTHQQTnNmX6oEnMg61ZocvhC7zXTOWJrZSJ8EClCkkIUeYFhT9yCZy_J_hxrXIXvkj_gjHvY79u608Dm0VOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
🔴
تارتار تایید داد؛ پرسپولیس بار دیگر خواهان جذب</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102643" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102642">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbnGQO_2NHln70X6sVXk8eC0Fl07T4YeE6hDWcYIiqa5FAqPAsW07NvENanMvtDcxsyh-rEPTDnwD-zyYbmnayq0Dmx3xrtx4_z7H_bRcJRy125uIeykG8JPEcDWW4BIxKyTVdzvA2jmD0cf87Nxh49D09bDm2h8Nht970U9TFBG6praeM1BKJrqo4xP0-mE6cieycVP6VNJURSuMs2jaLJUE6gT6S6Of67eMmSJGu84gCKJUk7wql7fqnQay-UqUrSS0WCGiEoczme9aIvMpwerV4UMfnCICcCMnbB52lbD1RbiK3izLmTRP9xGeEnrfaCMZeKVpvBu3qjc0_ya4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
برناردو سیلوا:
بی صبرانه منتظر کار کردن با مورینیو هستم، اون کسیه که برای فوتبال پرتغال خیلی مهمه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102642" target="_blank">📅 00:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102641">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b215f0831.mp4?token=C90ruGdrcRslubcCRlZzO1_Zz4YArlLdVk6QXRUpHUnx9cgWHbJ9KyDVuvGFr4pEOR4dxn_nxsdP-zUGRbAJJsBVFJv5kkwmiiGMjli0oTsZOkFSecxvUbBY9vsQabPgapN8_55jK6uhKUupbQC2BQeiPzki7WDBtdKmEoKcSx-TJfHeB2rUwGJwtqrWcW5DYOlb-LAr822AtB7ibNtOUsk4IV7lw8a04a4HwItb0dzrvYIYODfrgDvAp0nEziLG1T_KQ6oecKcXeaAp17CW5aeplEdRWExV_BpfSWJ0JcwMMjHRepolz_NV34h1lT0NHJ62OHdNjMB7kEcigTXrfjj75G9Va3x5h7cxdP-GnWBp9gGbQaZk28Cmqv47hDf8IsKbfzXVtK0IrM_gg9pn4ZzukA4cg4NRO_43FAbbFSp9e2uBLogDCvvKr3brzhHfl0RxLZzFvrg9j2_PCuOMnQmzT2IrFcnnEM8bFZQUTaKj-RnY1-PRIN9oipcmCNL_RV1bHyOEtaSsc7lJikWIQdtIbNs5nI2nwNhJB6wWMHlcOaQv4Q_UhZ2JzShKC5N9EosNYZ2HY593YSjBxKEmOS9G7y_uumcmbm3JR34Dv6JaoXpiNifCKK2RNJdPIQn9Y2swv7pbRtShvo6V3xgswRWlbigoEa2GXq3OxXsf0_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b215f0831.mp4?token=C90ruGdrcRslubcCRlZzO1_Zz4YArlLdVk6QXRUpHUnx9cgWHbJ9KyDVuvGFr4pEOR4dxn_nxsdP-zUGRbAJJsBVFJv5kkwmiiGMjli0oTsZOkFSecxvUbBY9vsQabPgapN8_55jK6uhKUupbQC2BQeiPzki7WDBtdKmEoKcSx-TJfHeB2rUwGJwtqrWcW5DYOlb-LAr822AtB7ibNtOUsk4IV7lw8a04a4HwItb0dzrvYIYODfrgDvAp0nEziLG1T_KQ6oecKcXeaAp17CW5aeplEdRWExV_BpfSWJ0JcwMMjHRepolz_NV34h1lT0NHJ62OHdNjMB7kEcigTXrfjj75G9Va3x5h7cxdP-GnWBp9gGbQaZk28Cmqv47hDf8IsKbfzXVtK0IrM_gg9pn4ZzukA4cg4NRO_43FAbbFSp9e2uBLogDCvvKr3brzhHfl0RxLZzFvrg9j2_PCuOMnQmzT2IrFcnnEM8bFZQUTaKj-RnY1-PRIN9oipcmCNL_RV1bHyOEtaSsc7lJikWIQdtIbNs5nI2nwNhJB6wWMHlcOaQv4Q_UhZ2JzShKC5N9EosNYZ2HY593YSjBxKEmOS9G7y_uumcmbm3JR34Dv6JaoXpiNifCKK2RNJdPIQn9Y2swv7pbRtShvo6V3xgswRWlbigoEa2GXq3OxXsf0_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
برخی از بهترین گل‌های کاشته تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102641" target="_blank">📅 23:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102640">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290de4f011.mp4?token=jK_2SljjOUMvaEKQsjNoBgRo37u0hxOseDV3lwOByBog3gEpM2NNKru4lsALic0ubUqqY6J1KGdZJKLwSSXWp-5_dljFnLgxA4w4pqAHr0NLAYZJ0wxyGwyismUNvsa4Z1oYHq6InzOsb5W6h9v1cywxCpnyE8FnNxOUDvUginnKmhdACnAaPkyFsn3Z77eftWyDKnXvFwlUIk3cLmM1d0d8NXeyiy9xkfvqm5oFjGxVVZz5PY-6nmAmaG5sk3dBwI88RkVlWxhcgDHiI09e8cD1Jy1jDiJJRfm2kJjMNiDdG8XF-3U0tV8FRQzBPE7VjHOIqaRgRmewGT2XXG_Kcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290de4f011.mp4?token=jK_2SljjOUMvaEKQsjNoBgRo37u0hxOseDV3lwOByBog3gEpM2NNKru4lsALic0ubUqqY6J1KGdZJKLwSSXWp-5_dljFnLgxA4w4pqAHr0NLAYZJ0wxyGwyismUNvsa4Z1oYHq6InzOsb5W6h9v1cywxCpnyE8FnNxOUDvUginnKmhdACnAaPkyFsn3Z77eftWyDKnXvFwlUIk3cLmM1d0d8NXeyiy9xkfvqm5oFjGxVVZz5PY-6nmAmaG5sk3dBwI88RkVlWxhcgDHiI09e8cD1Jy1jDiJJRfm2kJjMNiDdG8XF-3U0tV8FRQzBPE7VjHOIqaRgRmewGT2XXG_Kcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮‍💨
چرا بزرگ شدیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102640" target="_blank">📅 23:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102639">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9rNiGhA2c2mUApXToPWefFbNVBznLHs3bRJiVm1VzjkdbFnLoQoZ8ebszsWyIQDcnogZ2RfxbiskeWeL837drL601Bp3KMg96MfSMy1TE9mkQkC_ponaVpsxcA-symmgIpkoizUucScsIZcubBi98JSPODd8kkzP_1F_Ho50dnpSPEOq8OHd-s_mztPhOVddIFraRegcwTuxBi8x7Xp2TrAFsp-nKERAspxdpHlQwJzIcYdL5U3F3QEmlQ9K8hX6hCwks_HklyfLFR4Kq4UySAUbKyOWKjyKytyKiCcZHjbJxm86Avb9YghqX7Z6Se1sOB81-umn_uvaFGOCozSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا : رئال مادرید بهترین باشگاه تاریخ فوتباله، نه گفتن به پیشنهاد این تیم غیرممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102639" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102638">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZAmiTq2SwXlY-joN_ueTvDwGlLSYPp5cxe46-kmP83cu_FP1hAAc8txUA6gPuEoHhMAjhy6BghL1FUG8bnOB1RrdjyBlSCgmxc7eJNFepW_ECYsQux4PyfF4NhOL2dykMA4y2UDmO327AsITzZK_P9lBQj3IrVZjPUVDlJnEYmADiI3q16okvP5FjEWlYNAswij-t7_4mcPsNn7JHEko3rkoQA8k86LD5na_z3RoOQYr3RU7aZ9w2F8VJl43N0dcdj-q-yM35cG-V0kJ4E5cr7-LdRP4XvWmUe5b7KR1NRofBG9gcTJxcokuPLfQnKY_Y0McUKKi_-N-4qBHOUtbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102638" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102637">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac45ed94d.mp4?token=MlWnZ9QVmnvqhVpVHn_wZj8lhJJ0ki3VZVwrCrQLoUfQrhPXgD7AJFabYRVgBs2oJOL3LI1Tcpni4zgHgWok2p8aWP4KM5Vethx6jsViBm6rdonrNvjU6fPemXAkVA6Iq0-CVwuKvPZ15hR_m9biUKZ3bIrqJVyw9nkCYea424dYlm1OuL-X-3KJd19vYJxvTY4fafooLcuqTVp85ceChbQxP2hVFUDg0-W2kbcEebuKfE2bw8dZGlLcSju667jq_rI9v1EDfC0JAXkYv4IMCK_NX2a4gZ3Hzv3Zot71fRQLxcBMQfACVBC-6YT6kmRrkcF1LBegydYfvPZV9LanvCiwQgr8xx6WpUUZj8RcEDplLja87pGPbGZ_flJpjZL2Afnzhv2uyrYKX2rYeG6nqdInj68TMuTYG6GAJR2nhD7JiMJF5z8g49sQvVIWK1Hp-1yG57Bmezy1DTSg-cesrztLogrjIANGg5NMNESnDczw2BwxcVuN34djR5l-ObWRWEqtteresyn7J88DvD0xBU06CH8PZpix-iZpTFOBLcm2SL5ExGV9QIB05iZ47UN1KSJNJ-4SU5JbLsXMfpHK6BlyK2Wg5Tk1REvagy5hCYYDrx9_DIDormmAMT_o7IIbXogE33VqdZyB58xOxkVRRKyx8zkU9yZQHdi70Ntz_ic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac45ed94d.mp4?token=MlWnZ9QVmnvqhVpVHn_wZj8lhJJ0ki3VZVwrCrQLoUfQrhPXgD7AJFabYRVgBs2oJOL3LI1Tcpni4zgHgWok2p8aWP4KM5Vethx6jsViBm6rdonrNvjU6fPemXAkVA6Iq0-CVwuKvPZ15hR_m9biUKZ3bIrqJVyw9nkCYea424dYlm1OuL-X-3KJd19vYJxvTY4fafooLcuqTVp85ceChbQxP2hVFUDg0-W2kbcEebuKfE2bw8dZGlLcSju667jq_rI9v1EDfC0JAXkYv4IMCK_NX2a4gZ3Hzv3Zot71fRQLxcBMQfACVBC-6YT6kmRrkcF1LBegydYfvPZV9LanvCiwQgr8xx6WpUUZj8RcEDplLja87pGPbGZ_flJpjZL2Afnzhv2uyrYKX2rYeG6nqdInj68TMuTYG6GAJR2nhD7JiMJF5z8g49sQvVIWK1Hp-1yG57Bmezy1DTSg-cesrztLogrjIANGg5NMNESnDczw2BwxcVuN34djR5l-ObWRWEqtteresyn7J88DvD0xBU06CH8PZpix-iZpTFOBLcm2SL5ExGV9QIB05iZ47UN1KSJNJ-4SU5JbLsXMfpHK6BlyK2Wg5Tk1REvagy5hCYYDrx9_DIDormmAMT_o7IIbXogE33VqdZyB58xOxkVRRKyx8zkU9yZQHdi70Ntz_ic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دوران پرایم‌اسطوره مانوئل نویر در بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102637" target="_blank">📅 22:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102635">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JciwrHGL9hzjBednBHSOu_yZgPR5X9QEhIyojkFPs-bMv2obpC3IR0NfAK5-hs-sw4eUyR8HqF6pbSMux9LTdDXWLSVh4y1E_UZRfDtsDkQrXkeWFxlgCl0OP2CzCvHTzq5vFief3obhs8qvwsSytOCkswWs0PvryW-NRt0ZEGH23jIIzkdoQtjca1_ZzfJ3wCBj12N2XploMhAgvrc9AqTKbCPlh2Z6bCG8LjgSA4L9QX5u_0InLxVcYNecGJJc48SXIs6BrpDaxHY5PMBSD51Xml9NCJtTfdFXy9XO9Ba93FGe_J4euF77l9iZvU8zu8yq8g9ABD0koEbbiFTCZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLDvEhw4reiXIN29D3zwxTQ3PjFNaGHBsm0_09alCX-e_j7xuCMHPUTFHHpZ4Y8BY95itPxDN45q4uANpukLAmpQIgpAAaEoMzqEmQXkFcK7zeWFxKh36a4_eJs-f_uoDvLDskes-8fCHQq0P9zZy5z72hLKf10y02Bbuwd5pL1kDA63gls9GmxOevdbqnGToKBpsoz1YrOyzWvfzE9w6L28orPTldlbkAv5BZnVL3UtP2d0mS2vqzlbNnpht2ERkwJSBXBCOB6uMLKs0t7cIkVapw46Q8JuYCM8obam3HrN1g55S0SCNdL3_3Y1Qo4t8NIRdQpRVtclFrh1ZkDIIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وندا چقدر چاق شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102635" target="_blank">📅 21:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102634">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=aklLiaywkZLyzxbfWeHEU_kZHKK03TPZLyfVyopN8F9nfhi9h_FOxO9rvqqJLvvDRLG-6gGfbRLP1LJQwbKrYiKfDYofkJgQFHKY7NypP4xtqIU8NPUpTHPdqe8ZdT1V6zRNKM9211xJdd7KJF3pJUPJrCreuxdlIcAKPS6Zq-C0IgP622KFrYIenEaGmP5zwIt53hS2SEcQnIl-1pEFHYQYtRw6z4DCUkOq8sC-uqdgh4aM_NRuGOVmqvu0e2R12jno6fjwrqFCnFixuaySJ_fxf9eUaekfVXFd0_Io7mmiK1ylczonKnaHRbw0gbqDq6PjZ9aKmwtLBmbVxA6hsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=aklLiaywkZLyzxbfWeHEU_kZHKK03TPZLyfVyopN8F9nfhi9h_FOxO9rvqqJLvvDRLG-6gGfbRLP1LJQwbKrYiKfDYofkJgQFHKY7NypP4xtqIU8NPUpTHPdqe8ZdT1V6zRNKM9211xJdd7KJF3pJUPJrCreuxdlIcAKPS6Zq-C0IgP622KFrYIenEaGmP5zwIt53hS2SEcQnIl-1pEFHYQYtRw6z4DCUkOq8sC-uqdgh4aM_NRuGOVmqvu0e2R12jno6fjwrqFCnFixuaySJ_fxf9eUaekfVXFd0_Io7mmiK1ylczonKnaHRbw0gbqDq6PjZ9aKmwtLBmbVxA6hsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوانین به ظاهر ساده فوتبال که نکات کوچک ولی مهمی دارد و در لیگ برتر گاها داستان ایجاد می کتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102634" target="_blank">📅 21:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102633">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=enWo_7qWJsbMmMwn493pA4LTDS-uSdwn1ckRBgtoOY23trxXepLSimU8mz5FM1nwU2tl-GNw7Yf4d3ocyTV8WBVdAknClPFQ5RJdLw6e5uRDrUvfB0KH2-anQpvkbccWtl_3Livgp5E3EMm37cVLhlFJczN1Z7X-6Hb51GOB3h80FCI14rdUSDjFcRkANuCs6_q96UME02v7sayZWpMypbY5Ay6YmxrelHj9RRbdBfRJOFudsMEmB2u6GIYFvrLuWXEFMvvrDu-PZfbUViMVSXMIFk0Qq_f88O_qm68ToN4498ak-XdFfuULD4-hgCStHMvq2hOwD0S9wmOXgEYp6KxrCH8-IBEk5rSNTRDeThFHMcjLZAGzc4ecFqMspBSgTsvN0joIodOVcGfRVYQrtCgsWPMm1FYQeM4d8hqr-sfVkWygj1IiTMedTZz6JjKqffGn1mx_sPw0Qx02SGgoHeWp88CiGoZpCSpzAj1LlZMsdRQC_oHizuAhZY8AIEkalX8jr7R_E0u4dQGn96RJRvUQbyyb6YMcAqqmHksrgbKyDOspwkJvioElDcXzq5S72HV6dlvFm0T65yfGtY7zWST0JbYz44fTUzVAfwnw0bFMXSfRgMpbUxCx0VejirbrmuNeBqd7lQG-tHNyqphCWw62KrfZ5QY2Ca0wj_ILvTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=enWo_7qWJsbMmMwn493pA4LTDS-uSdwn1ckRBgtoOY23trxXepLSimU8mz5FM1nwU2tl-GNw7Yf4d3ocyTV8WBVdAknClPFQ5RJdLw6e5uRDrUvfB0KH2-anQpvkbccWtl_3Livgp5E3EMm37cVLhlFJczN1Z7X-6Hb51GOB3h80FCI14rdUSDjFcRkANuCs6_q96UME02v7sayZWpMypbY5Ay6YmxrelHj9RRbdBfRJOFudsMEmB2u6GIYFvrLuWXEFMvvrDu-PZfbUViMVSXMIFk0Qq_f88O_qm68ToN4498ak-XdFfuULD4-hgCStHMvq2hOwD0S9wmOXgEYp6KxrCH8-IBEk5rSNTRDeThFHMcjLZAGzc4ecFqMspBSgTsvN0joIodOVcGfRVYQrtCgsWPMm1FYQeM4d8hqr-sfVkWygj1IiTMedTZz6JjKqffGn1mx_sPw0Qx02SGgoHeWp88CiGoZpCSpzAj1LlZMsdRQC_oHizuAhZY8AIEkalX8jr7R_E0u4dQGn96RJRvUQbyyb6YMcAqqmHksrgbKyDOspwkJvioElDcXzq5S72HV6dlvFm0T65yfGtY7zWST0JbYz44fTUzVAfwnw0bFMXSfRgMpbUxCx0VejirbrmuNeBqd7lQG-tHNyqphCWw62KrfZ5QY2Ca0wj_ILvTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاس‌گل‌هایی که ارزشش اندازه یک‌گل بوده
👀
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102633" target="_blank">📅 21:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102632">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=t5xe844Jech8V5fclSSxOX7woTkmA8doQSzHx7Q0oj0fAdKJnVT4p4k2Fsw1TcvoxKq9_LGOV74h8owk05kRaPc5HAv8uk1jwHX42ZaW4WGc9x4dHXPCUcMbU0W4bc9ea0A_1ojZmBiKjLoreqoETP8ZJqUJdb2lA_qrFN43VfGqP-b01XXp-0HWFoHuX-Xcibx4j2cxu4qovCvMEwQe-BxZyTZURdArxCLO4md1YY9ieF21jBveQadf6-EyuZkNagqFq_lSRAZvaROJYK3PK_8lGByoaOW1GYjTdW5Qnb2fjAGsU_ggd6lBkIJxT-He_OPNtBP1QLI7tHv8sIcguw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=t5xe844Jech8V5fclSSxOX7woTkmA8doQSzHx7Q0oj0fAdKJnVT4p4k2Fsw1TcvoxKq9_LGOV74h8owk05kRaPc5HAv8uk1jwHX42ZaW4WGc9x4dHXPCUcMbU0W4bc9ea0A_1ojZmBiKjLoreqoETP8ZJqUJdb2lA_qrFN43VfGqP-b01XXp-0HWFoHuX-Xcibx4j2cxu4qovCvMEwQe-BxZyTZURdArxCLO4md1YY9ieF21jBveQadf6-EyuZkNagqFq_lSRAZvaROJYK3PK_8lGByoaOW1GYjTdW5Qnb2fjAGsU_ggd6lBkIJxT-He_OPNtBP1QLI7tHv8sIcguw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فران تورس درباره آینده و باشگاه رویاییش: "میخوام خوشحال باشم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102632" target="_blank">📅 20:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102631">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Plro3r8mhIT6KQOyjdMs5fZQ6mMVvmiIhVqwS6CdlSGkqIbzEuUfysXqT0adSR52A4j_OcXW6VHLw8rgcBw61KqcSjNQ1KH364yi8iNJOcn_AC_jdUI4-czAT8GyyFOIM0lHDtMQ_LLDtvz7OiWfxZvHk347nrX_-8ILHrpKOibXYpynSspdIn4FLfojs5nSV6ySgK5_UTvE5wkWacLGYzxY55J2rNumYsyrZMhzduXuBpAf2JZJL3RjoQ8iy68LMO4kPkrUB3irtFep0bptQjSFDgkn_VbuSVHVBtf_-R4zaLNaJRnV_MF_zFJYheT9by9Scp3VihribNhPKD8BZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
تلگراف|ترامپ تمام تلاشش رو میکنه تا جیانی اینفانتینو همچنان به عنوان رئیس فیفا به کارش ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102631" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102629">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d16BqUwejkzI70VPwNd9pI0qcs0ViLCVxhQSb-7czjT-gumZNGkpho_tj_u9uTVS_kCsgNMEzT2VIvsLL-jNq6c2atG6xmjg3aLFwkhtdDAtDAznTmelOlMIee8xq_KcGY2552xHqoTpjkZgKejiGKMnd7BM_OUoj5iifwb6kDi3JYjtN7LYfWayNrVZbuPSZ7aMzuT9X8r8etn8UfjBOsBOVb3uT1HnBW0Mw8BNcXY3pInVbOArmWGRiJ_hoAr7XbNcYcF_5RWC0S4L3mF5HwR-JY7bdjSBAiI_xxI_eEoUnWUGoqcxIg_rwOOQmgvX3AI8HSo5EOkrYoc13RjpeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCw2PipnPVFJH-dftK-1bRiAZUa-ZmXcxqODqghElK8tQyCQAOExyKxwqmQ06hxjUzgpjwWIlxcsYSuZZt94NS4ljat7ekGXJw72ORVARM4FtRIpkiVibXT8S5gJye3WLfEya5xfGHQFN_fVK-Lwt3j0ECEtS-FbeIDj2ZRwnRucQ8OKOvexvRA9eYHzpaWo8E2xYlB2-zoQJdl65pNpf4QIMz_kz5BgnO2eOVmyyV5DiACz5hpModoR8AU2xd-SKgicQ3gB_iiFDP_2kCl72thy0vglOi6-VIX_5SbtHlgEw3mJbC_uVTDlmofpOOZ0zHXB3O58h4WABGKLsXYHZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
حضور مودریک در تمرینات چلسی بعد از ۲۰ ماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102629" target="_blank">📅 20:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102628">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ucdlhxld-O2R9b8THYfGuJPMAHSdLvr6cKSlW49k8XuHrd_n6QdkRy0n2GW6NqP0O0FrAcijgGayQZp8_PefsNIwHP0pD2S-CwrIN8HZQWZz46rbRWdB_VjjRW80uv4Ahl1mx93tbPVr_jbLXGBFqPEz7EoOTu0cjlM2aMWZN1nbHTAVVJ-PGF6WOPfA7CALYpjaQier5sdXqiWaH-_1ix0idU6PTsEa9PqhFHovOP-NFRx5JfE3pZfItQKCCyqoYd5Ke4SXGpuzxtB2fllRj4hP1CTZf5vbQT8OKhw6DIdQVQjoUCqDVVgRBJfgBEwzzAwdYaQKM1OAl3AqBCnKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فران تورس:
در حال حاضر با بارسا قرارداد دارم ولی تو دنیای فوتبال شما هیچوقت نمیدونید چه اتفاقی قراره رخ بده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102628" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102627">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590393501c.mp4?token=gsBU8gqaT5OBJS2v0s07K3gDUbh7RD7hU6c2m9lLeyIRHFvGHv2881EshnJdlchvj6nIp08_kHhjf8iGBlMEcvvdm98j2huqegfF8JQkzz1OsDK43oNaP_3P3QoD0DDUX4NKRPQ_abhiN6UYtWCzFeIeyQtIiL2MMs1R94hvd0D8DFmgqt8Kk16uZi2VdNde8bE-JFmUI2Lv87YDLN6Xs6dSibOgQnH5rEbUCZQZRcKJ1f0oeqGaR8SgQtROfitu4ZUjQiSXQP9iqXLNwCen_7zonfnpC-bOr58q9WzDfOr3jaKQbimkpGTTD16ozWUvv3p-JZzpo01_fs3r_NLfzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590393501c.mp4?token=gsBU8gqaT5OBJS2v0s07K3gDUbh7RD7hU6c2m9lLeyIRHFvGHv2881EshnJdlchvj6nIp08_kHhjf8iGBlMEcvvdm98j2huqegfF8JQkzz1OsDK43oNaP_3P3QoD0DDUX4NKRPQ_abhiN6UYtWCzFeIeyQtIiL2MMs1R94hvd0D8DFmgqt8Kk16uZi2VdNde8bE-JFmUI2Lv87YDLN6Xs6dSibOgQnH5rEbUCZQZRcKJ1f0oeqGaR8SgQtROfitu4ZUjQiSXQP9iqXLNwCen_7zonfnpC-bOr58q9WzDfOr3jaKQbimkpGTTD16ozWUvv3p-JZzpo01_fs3r_NLfzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلیچ: علی دایی مردمی هست، من مردمی نیستم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102627" target="_blank">📅 19:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102626">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IZNC37n8rGYVu595FrBIijr82hY7jJE7jTkCyRg3qfNEOTscbmh2tcU8j4fERGNXODNpSoHWjLqDxnWtFUK3aDggvdiWLu348qqG8IiFsYVrfCD_0EO3neuEcf_o8jwQjP8bEyPGBnsr-b-IyIjsXXyJQL7GC13aqi5Cs_w2NBe03izDXhgI8SwJCFSwrqiS48fq8zJi53J0eUjSMSgyhIT5yAkN9I3KmcsZeUPhDmhg8gCdGZqOumbM23fT0eGV8o7lxXk3vUkx2K5QSgYnyXAutHWRwt45wflYFYv6SXtJrp2AV7YKguhZQ6PCdvldvj9ExICm4PsD5IPijYoKsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102626" target="_blank">📅 19:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102625">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8zedU7t2qMX1bG2GTozs7T3DBPEWThN4QkIGt-Mh7PHvku7DruOlZLMxGuTulpd3XDH_VTwGfQ5owxknaUvheN9KvVB6CQbDybCVbhl5UEKnndyVF6OlviXbXJg6l7yNYb7_Q864d9dsHda6eq8uC8CAFpnCUtdeBeqRZ9_3PG-9s4exjiCxLSBtvXIMUJi5rLS1FdzZ8JuMRUjyBo0im2AoIfuTNl5FGylWyiu5cB8hfNL11g__rxlBwmu1h9qJeWFqYFTQdshfcjMW7Zv14u1JpzAx-Q3VaRU0nuls0GHwoJhonWUd4ayis769Fc4HrVkSz8uZri7prHTLdqcOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رونمایی رسمی چلسی از جردن هندرسون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102625" target="_blank">📅 19:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102624">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qE_tSJNem7xRHy19A6DlQeBOgbU1I_jg76DfMMwnNf-YCtlynvBOwFai32ubEqBf_sWc8hi6IMSMAOk53OZkB3QB6OYnrxEgr0lbybcWh8xfjH14CNlQydq1M3VkFQmA59G4OBx0Kl1i7EzfUJ99RcF9AGHhyFhCRO8LLnZlBMKdH5lYx5_UO3z7mO4gETM3efCgaM3fe0_08uqlMio-o8o7o5ukoEUhUyGuW80bqpHWNRDH7WttPg_SsDbA2RLQN1Kt1jTdUyKO3Ni9No2rzbu6SoJ7DztlXEcG67uRGHjOJkPS2Lc1uukoGOCZN3D2OakmKbdzneJSRUTZT8QpTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیاس یایسله به کمپ نیوکاسل رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102624" target="_blank">📅 18:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102623">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16357a3407.mp4?token=QS3-ymGWkszkZznNQ6vEu8OY_Hv-axunA8LoUvrWDZpIFc4Ey94U1Ch4vClOruYDq-K2HXCPe-2dm3EV7Uq_IbFdoOCuDxwHGXhcyNCv0YFeMFro6oZRnvQ2PZVA37otM-OxRQbo5pY64dsJtZbniGtvV8A4oDhjYvuBtiL9_5AfJWCwolroVI6dFuQfvick5_9NrQnpdEUa9ndxDV8H65wXu9C6Dom0KAYiAL5ycNAy6XxBCA3Pd34Co4eqCp3ogy0EhkcOo5pzmj4bFszyTJiaBzxbJkr9O8qwoAgVzvAGBEBLpcwLlEcsZy3UsoUVw1jak_TAYEZtcUQ2sFJUqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16357a3407.mp4?token=QS3-ymGWkszkZznNQ6vEu8OY_Hv-axunA8LoUvrWDZpIFc4Ey94U1Ch4vClOruYDq-K2HXCPe-2dm3EV7Uq_IbFdoOCuDxwHGXhcyNCv0YFeMFro6oZRnvQ2PZVA37otM-OxRQbo5pY64dsJtZbniGtvV8A4oDhjYvuBtiL9_5AfJWCwolroVI6dFuQfvick5_9NrQnpdEUa9ndxDV8H65wXu9C6Dom0KAYiAL5ycNAy6XxBCA3Pd34Co4eqCp3ogy0EhkcOo5pzmj4bFszyTJiaBzxbJkr9O8qwoAgVzvAGBEBLpcwLlEcsZy3UsoUVw1jak_TAYEZtcUQ2sFJUqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا فوتبال ایران بهمون یه ممد مایلی دیگه بدهکاره.
😂
یادش بخیر...
واقعا فاز عجیبی داشت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102623" target="_blank">📅 18:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102622">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ویدیویی از شعرخوانی یک جوان بلوچ در باب جنگ که حسابی در ایران ترکونده
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102622" target="_blank">📅 18:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102621">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNwiLkfBdacCfOFL8osKrwoPyT9FIEKps3ryTz9HGDIBp0YQTDK3S4u4v3ejfz1D7G3ctzT7HvwLXgaIsUzHUqkZIwKOsNgguPW9bbGHfqCzc7khBnqnn9lU94uH0D2_0jgeV42tTnEjN7lGOb51-uZ6G3cBjTYtzMKLsQ14MaWjzxkshLWufrx8QMW-X4zjtF4fe_Xl7Dn34z7DAQuy1PTBQ6JHvL8er7b1wSF_G1eKxv-SxUW-zaq3GVOABRGIc3-sGSnvTzdxg2eb7DfnSFg-gr1Zonkuhk5v7gA4STBWVSk2evmh-UzO-W0xNxd7azhk19jgsn0alW46I19oPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102621" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102620">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwjRx9j7cgp-RoFd_UVow7NWRbR89PF5aLBneQ-WX4zqKK5rLpjdVlTg7-5lkQyeeOCop9arUfQcbQsfiKijkvAou3INOzrpCtjsF2pRZfmUwAhVVp8H1RdCUKufjjuPygmIvR3ytQ6I52j_jJvPUkQYrqpIMrUkcbG_iGwj1CooT9ohIbVe11ODD3MQE37JO8YmfkO7EAaciSrlcUxcRjI5T2WAxLkP3QRkQXsA73wYFpoc9eJNjH5LlhhMms3nvgfKX7S3W8f6uuDtY9Ci_Wzc6EIAND63cnIqi-veZyBPWQ5PmtUamjF8wyaUf_OJZII-ZgoQCI60495TQa-L1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102620" target="_blank">📅 17:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102619">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np1LwlZvgMhWSPEbr6VW-iBkDDUgGu7ZUbH0bNZzBTYsQSUsDiz-e-_kCDW3PLyf9wkd3uKZUz4F5bvSMgA4QkbGk_46ZW_IZmsZFlh1o0S4D3bAP-TVjdl06WoWr4gUqlAMcdckhJhxC4r6VDaLNBr79v3vBxMcVSQ_srneqd4HxWGt9wiFa98J7zb7I5HlHYuLORqy52ckrP7Buwzb-NBEbvVhHO5uXEaOF53zZYGt7zjMhM0nJWVjw4EzVzCJNuGaSgUv1S4QOTtnX22rPAiPFlEkoE1W2NfnzR56KsU-R6mxDhQ5H_hd67Jh1gZsa7CIKYZemK_ZLV2b51d_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پوچتینو تا پایان سال 2030 با تیم ملی آمریکا تمدید کرد و به کار خودش ادامه میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102619" target="_blank">📅 16:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102618">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سیوهای تاریخی گلر‌ها در دهه اخیر؛ پشماممم حقیقتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102618" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102617">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6yd9JVeImYvyq187mOXwdXp_IVxorc56PYIYdZhszVUUSeTrq_SJoE-aAnZK19WXvGhIg623VoWXFn0JxqURM6vw2oiTmDoenI9rpVkkPPgI83x5Qnzcuy_y3u_ykpcHmNwMgdA4DRHgXKxwNZnz0dCXP1QGb2PkXmxCUkZZUtxsOrdEXaMeniqyJTE7BwZoTymkVH-rUv8PTIXtLRRV18M1pOyWhGIUOJ8QylWU7tm5_h_2_u_HcFQ8IX9UXRyqXftlkpfgop0PKFxnIRucEw6m0syuTdXW9ynqpDlEi09r4xX-tE7ok6-CiUyVgTYFpnTtbR_SWqJoB7WK6u6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیماریا:
بنظرم مسی تا هر وقت بخواد میتونه فوتبال بازی کنه، اون تو 39 سالگی نشون داد یکی از بهترین هاست و هیچ محدودیتی براش وجود نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102617" target="_blank">📅 16:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102616">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=Vp5qJzfPya338hh81V2-bJApxlN-X5-b9HuuD6j4jGcsAvXLLZf1Jqk1rpjxQ4CbX2UHd2TLN6TBbP_-wprELRZ5XP-BuK7rN2fGusgIxsegmClxoJ4LIrsIpdfVs3LeM4qoauVOv7h2f1-9ThVTyjiSBLNBNQN2D4yHLJKFnn_ckzkdDjwmXxVHOLh8HjElAkdDzGgvhyqE5vnsXa_2Nr4wAV0lBJXttCpr2Pv7hQNUJDZNX648s-XAVySC-2QNVjHnVwXZPG4gFx43aL2sxiIbwc1Zq6vVnIbmc5Gz1VsKY_etxl4v9BtLTbvZYuehWVVfU753QXYGGjaK4CGR6DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=Vp5qJzfPya338hh81V2-bJApxlN-X5-b9HuuD6j4jGcsAvXLLZf1Jqk1rpjxQ4CbX2UHd2TLN6TBbP_-wprELRZ5XP-BuK7rN2fGusgIxsegmClxoJ4LIrsIpdfVs3LeM4qoauVOv7h2f1-9ThVTyjiSBLNBNQN2D4yHLJKFnn_ckzkdDjwmXxVHOLh8HjElAkdDzGgvhyqE5vnsXa_2Nr4wAV0lBJXttCpr2Pv7hQNUJDZNX648s-XAVySC-2QNVjHnVwXZPG4gFx43aL2sxiIbwc1Zq6vVnIbmc5Gz1VsKY_etxl4v9BtLTbvZYuehWVVfU753QXYGGjaK4CGR6DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
بعد اینکه رونالدو و جورجینا با هم ازدواج کردن، ملت شروع کردن به ساخت مراسم عروسی با هوش مصنوعی ؛ از حق نگذریم این یکی خوب درومده
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102616" target="_blank">📅 15:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102615">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=WjxFQMwAubgRdj_sv4OVraXG47NK1VnWZ58uW3NiOOza6t2oWrl6hc4RAIgMpblggTqURIz6wd8sYp0j3CBvQ1z-xKZaOdYEsL6I1xXJpYJidoaI_4Ox64hZbOb5PdsrBRl5doPOMQC4Fu9esN-k6VGqREdlqvYfMcvHwOfqhsgRJ0Qfa_Mlc9Ie4G437-wOGkFrqvJ1DYd0zRV3vBQ-o2NwwbjO8pG9eSalOYel4u2qD3q_VVy3-1EowTKU6Ht356Nla0dUak3W-YQN8kWfKUOOAf1qWUv3C4oiRmPlbhryhwimi4Y_psAYt4KR9UBAKARkZZ9qpkraZwEwikB9Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=WjxFQMwAubgRdj_sv4OVraXG47NK1VnWZ58uW3NiOOza6t2oWrl6hc4RAIgMpblggTqURIz6wd8sYp0j3CBvQ1z-xKZaOdYEsL6I1xXJpYJidoaI_4Ox64hZbOb5PdsrBRl5doPOMQC4Fu9esN-k6VGqREdlqvYfMcvHwOfqhsgRJ0Qfa_Mlc9Ie4G437-wOGkFrqvJ1DYd0zRV3vBQ-o2NwwbjO8pG9eSalOYel4u2qD3q_VVy3-1EowTKU6Ht356Nla0dUak3W-YQN8kWfKUOOAf1qWUv3C4oiRmPlbhryhwimi4Y_psAYt4KR9UBAKARkZZ9qpkraZwEwikB9Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
یه قانون خیلی جالب فیزیکی تو فوتبال هست به اسم «اثر مگنوس»!
وقتی بازیکن به توپ چرخشی میزنه (مثلاً یه ضربه کات‌دار)، توپ تو هوا یه مسیر منحنی رو طی می‌کنه.
ماجرا از این قراره که چرخش توپ باعث می‌شه هوا دورش نامتقارن حرکت کنه. یه طرف توپ، هوا سریع‌تر می‌ره و فشار کمتر می‌شه، سمت دیگه هوا کندتره و فشار بیشتره. نتیجه؟ توپ به سمت فشار کمتر منحرف می‌شه و اون حرکت پیچ‌دار قشنگ رو می‌بینیم!
برای همینه که تو ضربات آزاد خوش‌گل (مثل شوتای دیوید بکام یا روبرتو کارلوس) توپ یه دفعه زاویه می‌گیره و دروازه‌بان رو غافلگیر می‌کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102615" target="_blank">📅 15:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102614">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=BHUFU5njSLi5HyA1VSABSM91OLFM0XLGqlzPidLu9LNc8GZjobY9IYNCqwvsKpV9VZAdV2QTD3pqxSbU8t_w3iabAnMS5pZr7uSYfPNduUUgX-JSDs-2MU80unrZdaYfe-rZDKzcNwrkHexmRMlvNRCehZ4p7zuAg3vxkmKt2vuF5YCjpbs3RrByT3elBSmV34LSGYGEIjupovY_3UnUwhp1297JFIB6WoUo3PgjKMSwYqxHqKSyW8jFpIVK2F9VzMI2dYbodkyJDy6W2QvRcfmo-ZeNIGXIgnWeQClr0ssrAXXwb2r2mO29Nn2csBMmrkJ0E0f3wiIwHw3lBNlvtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=BHUFU5njSLi5HyA1VSABSM91OLFM0XLGqlzPidLu9LNc8GZjobY9IYNCqwvsKpV9VZAdV2QTD3pqxSbU8t_w3iabAnMS5pZr7uSYfPNduUUgX-JSDs-2MU80unrZdaYfe-rZDKzcNwrkHexmRMlvNRCehZ4p7zuAg3vxkmKt2vuF5YCjpbs3RrByT3elBSmV34LSGYGEIjupovY_3UnUwhp1297JFIB6WoUo3PgjKMSwYqxHqKSyW8jFpIVK2F9VzMI2dYbodkyJDy6W2QvRcfmo-ZeNIGXIgnWeQClr0ssrAXXwb2r2mO29Nn2csBMmrkJ0E0f3wiIwHw3lBNlvtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خولیان آلوارز همچنان در رویای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102614" target="_blank">📅 15:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102613">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N72TtOzGzmroaXTnXqNnmGqoMCm5xEi2FYk22PMS7tZSo87pSjVZQJRSFiijk8MKRmcjWkZnP-E4qm7vLbRICf16v2ICf4t_44vlC4m7oqvAAO5PYzjMdcu5YSGITzaGsB-9HzEzCuiTjN_zuo7aM6H7qPt-Elc91IaGXrpvdpOPdW5fGBwrhBThHQ6xIpa4_pnQFpYBh7h_mwj4PAHwtjg_UQbjhEbWcf5q7fRPFLl9DGr2b5ZEw678w5vM1OHZKXbDz9aTeLtyCCpDSbeCqoaFcM6fq7HFCouRP1baQqV_1mlp_oW-UmfFqP5RVPyyt7AudabGZI6cZMTWB8j1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
استقبال هوادارای کولو کولو از ووزینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102613" target="_blank">📅 14:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102612">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LU9g62ymU_HYA0yXKNQB8dcYXxOfF4eNwk-G6ZP04lti1dB108VdMd_rDJDS5G3qZdZCgCoVGLDhGuBzmWfzUsAyBixo9NyuxJ5gnLSLfI6IU_p0HM552v5WG3KD1Ol1vXA97BwsxHRjujHcWNRYSlALnSq7ZAyMJJuZWw6wR2W6Jsbc3GkIeF6OGOpq5nbTG_xXwkgjtxHI1ziHTK-Jo20qJF0BH5AEd3LjPJKLi2179g7zGTaGqcWt1m2MgUIDghtTJPw43f3Ij22sNcIqChvPJ02DtLpyGlnp-kZbTMZV8Dl13GFw2UDfMoQXOjOazympNtXyBzy3f1sI5UHyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
مودریک رسید به هنگ کنگ تا تو تمرینات چلسی برای فصل جدید شرکت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102612" target="_blank">📅 14:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102610">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIOaU71wc-9R0qzq8hYelV-3noMNuBlp4N0WbUKCS6Vgi1MX0GuZrTp4SkN152uuD3Ea7RqDQPVN1xLpx7CmVko0FYA-JHfCyqtgwx60RAJseVOgYunapcSd7xCsRLYn20U7fAHGlcSXqlMhd4emZ8Od1dyQtdcvDYT19ybWNkBscDpMzGooRRiyKzEqO6HoTVCsGHD9_gjvfotwiLAFFMB0MJhxkXPwSGkFV8-zaXS5p16qNZh9Kqls-TtW91u_OL2FkqQD460Wh_-9r4xw9Hzo8UkQjAAyjIzNnMo1HEeYK-e1x3rAjazsDsNN2PANsAQJKi6vbIAG59SnYyvoTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fnQtaIcOYaIce9AtWuCN8-_79CNcQv2PoKfG-RRQIC3cZJIgakgtPCIPGyFYLV9lBjYIOXO9j5zR9COYXGb_PkzqDa-HicGaL0ICAuWEhFghARHRfR7EzSS6p9O-3Bn-BWKo6xYtKElgmE-WoeP7UQ1UVa5pxMLrG264nvhx3sbP2VHdPgURbEPP3vzP6ireyvyq5y1Xbi8OyWMRKT792Zc06oV8ZDwDVgqlNGcOI1YilG4zjISPjVbyeM9FjsYknqJUeHIEWWuU9khfUBEbp6HYUeueosPC3Tk3OuqSDLPpiSt_1_4-DuBZ05pkhSDz6awa54xLtQrKqc74_jeVew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینا کامنتای زیر پست بنز و پورشه نیست؛ کامنتا برای خرید پلی استیشنه‌
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102610" target="_blank">📅 13:40 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
