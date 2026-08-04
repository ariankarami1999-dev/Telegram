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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 21:39:20</div>
<hr>

<div class="tg-post" id="msg-102711">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrjYYzzm4Nojd3rztrjdBYfJnNfvme-4nxML7MRHOl2wqZfDUjHgSgnHoq2IHKmtSHQF6jiLXmb8IdelnaacpsmeQLphBBKdsLAzhXwE6_5labmj8hF7BuwTPUf0v8ytOgm7AxEGAzcUELlzAvhD4a-raebtZ0vNGUSA9cMwDmwbc1acOsFny3pox-cMUn5gXJkru_HyCidIRxzOgfR1OPmwf2HkOz06apYyvGNMMVmpc3rYDCsEZyAcnzWrlk3ViYyb4IQfX8tOFQsDXf-NEJbolmhhrslqY-HybN5bWRtLZCqamOQpGYSNOQsqa4Kg_QQWC236qTy-FxSWA9Yzyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل زده در 10 فصل اخیر 5 لیگ معتبر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/Futball180TV/102711" target="_blank">📅 21:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102710">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at9g2xbaGzqwp3pA95rm4JHP3PUxNMk5BA9tpjOtdtHECQ62WvfhXNi3tH2CZs3mpwWIchcvKAdfUYx7YC4Xr0pxghzWrgtEo_MP1ekXPw8RDIEAJqaTh7t1bhPvX6e4cK9PhEjvZeDatsJpfaAn2h7_gzJ4a28tAcXWKzQgOxLc89p4AeU7Z-LvMVcA4Of6j-ukvLLLuQ7XwdTMwQtMaqXR7u_0ywNQpfSaMLFIzpsSQ9Z6VTCMiZ30Wd_Kk4wsfAil6QOkQ4nGD4Tozqy-QdFCfwyac8QpFokTIamZTm_DxHn69GSpXxWEjzPiqQKtWTePak8BClW0cXdA96UxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
رامین‌رضاییان خطاب به مدیران استقلال: دست از اینکه منو بذارید جلو هوادار بردارید. من حرفامو تو زمین میزنم نه فضای مجازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/Futball180TV/102710" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102709">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMayle_26TOtK7J_9IA7TDW_pnTwA_r0cnnzeZI_q5Eg5ZXeHkEr1B4gx_mJyZBe_xddbKQ8td-07HiRl-uQDGpyiIRNX5-KXefQnvQM7OVIBdMrOYJd_1ah0WwVaQ4Y0OEZCT5CRB-fhSlZP01cezGX9Xo1uwYsPSWi_PtZ0KTDiBVdIROezLaCS_SaFTze_msYlU3QrHkirRg_vh_11zi85xTvo-80MS93MphVOSkqpVnDmEkfeEACERtQS5KoUYHi6DK_cXVTTdXO-nygk3Hr6sJrvAsn-Rv1ciRhnZWDVLXX-G0ouTgYIpjmSyq0efKBONUYZCeJoD2m23saiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری
؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102709" target="_blank">📅 20:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102707">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVndqOc5tM-lc1bpiJVz2fkk3_j6d72rJAeqNJWZwrPGf0JR6aw6MAdxqhAhoEgLbWJ71tb2WLSeSXCyv5znKaaRnf3EoPtKulsTFjE-rES-BwrRErsJmSmPYY9q3kBgLjBMTYtdc0w4OmJVbtxJb8VihOYRwNT6vIu3BviIx0s6M_l24iAuYVRxgDswHO2UhadCJQtOsH_gvndxcmaRsydYePvZgkzqWAhmtkV8buUZh0IzmOK1Mp-hhfWom0HcbvxgKZfoyjjJU_MF03p4GLpuKL348B4nG8HP0gpuUFQY344dNGM0fM8zA-9DdM4IT2qpeFOOW3RInnnPzCX0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tGJG8gxBc8UhysTcR_LEgrXKpz9qDc3g5q66ADYBHn1VfBoV-jXE5AaJbOHTY8bCNkUQj6FgdvZTjRAZiOI73k0i_rjA2iREuhzFzvGzhJ3Z8_88rWvySzGDt_bJ4YJWnJf7uRhdpkW9RvMtCgZulrtst4imTR3A2powATfkN7MgeMztg-6mBjiN16vujjUmHzVZdjN8f7j0hlqLPiuEMMv-QlSJXzzLLcaBJhulYliaD8LKDhJcIxifrJ51pgygGK2Up_9Egy9Lvdo2gfgjMCvdwLQWAvYpDCmWI3QXms8gl5qyItm1EBhZOdQS4KfDrU8iZRxoQts_PyXZ0C4iEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
ویریجینیا:
من اصلا حسودی نمی‌کنم. به نظرم وینی جونیور خیلی هات و سکسیه؛ اتفاقا باید همین‌جوری عکسای بدون پیرهنش رو بذاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102707" target="_blank">📅 20:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102706">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW7_qQzPAOvHv6eiVHq6vhkD8R77o12bHAQbNxY1uSL_UUsBZk6cZnnT9lEr0OBWA2E1KQQxzo7Om8xOsuIK8ID2hiG_Iz2alqM4xkURMfNoEfKd6q9hjhmjzapjN8LuTTc9TePwagW4sdK4dX_KgCaGOL1FKfrWW52TyOxoDmjC1cfJkqzHC3hukCrAsC4fSoEIOAU7TWacAguJOr2eN7CXEcTPz2KbBi966oOc6vvVS9e-07Nj-NuzO4whSR57iWPs6-48VN03VKcY_7Gmm3xYH0Ys6VRFhJ7jClJbYBuQOsl_D4d-L3S9xUlz5O2W2i6OU1OwG_cGBMIuA3RBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
فووووری از فابریزیو رومانو؛ سیتی به دنبال جذب پدرو نتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102706" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102705">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102705" target="_blank">📅 19:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102704">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISxYPZRyLEnyjoegFslWzIXUmbgdmZhyjS0NU54cj-Q3oTVtFW440Ovl9gSQeqCdJvEvc4RmMXKbPTPrqhOJnb-VunjPrEbxKXsjuVsRz_qsIoqYAUoCJZo69aYDE-6d6Em0xYXFKmEpp0jAv5sCaTJu-rh_5qHv72rNzQkRBGo_XXaku7jjEDShBB44ShT8gWGt-t2XjVZ64NDZ_8U8i5UlLSL921f3GiyY2On6YDVv-veRJ9_bSkyOjGbRZ2SCkTwDF5H121p5CGaKNvcn0vAwxApR1h9o_sLHXg375D2RNqWzLDZshWnB8uPquI-4t3Iby_4DJ_eGVXiVrH1KKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👤
پست جدید خاله جورجینا در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102704" target="_blank">📅 19:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102702">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rc4YbGMVcNPeLSzeRaspAHQHIsez-55Zylyjl-3fEFmo2-qN_FZRYRVHoLaAgpYxFiodpx291KbBGpfX3gOcKfec0hxFzqU7wLmI7Yywds1F9VPVp7PUVdiu7nG6ATHGZapqTdb5hVn0pafdreId7UIF71nYXjIfSfA_28b_jRI2OQx5r09YCdnl5czAVe1zBYf6BfDvkTHrYhMd1lGjSkhFyHyj0abZCFabO99qOqt8Gxmk_joHBvhStYxARdMPRiVmUY1FAzMnCPd-d2DN5Q6I6dI6nRlQFWclO1TEx_vWfZkidEL0hz9cyGsj9PdX0ujfylSuADQtNidSBd8r6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8lxRnwBA5QHIglGFVopTlnKNKI1jZOsaLYYDD9OPK_a7qXGuaEH6i26K-b6LKHtgRackHu3yWqfg9iSoR1tQc8mkuuZQGIBSQXrk6yIHCQW48uE4kyR0hzCxzCbarAdb8RcuUjLANYO5Zut0EHZvAh8KnvhgCW2pQA0mz3hbOB89PFDve3u92_iAXwnd7t0IsayFAm8EwHRKfiliCrvcgU9E3NvgmPwg3o1eOmrJoC9S_1t-OsUPhf2gbTKwK4r3k52yUST7TylzYR2OWK4zQs6YSwZ2OgTk_gtc7x2WOmiAN9_ftPNQdDCx6ZTkMneFhzTcIX4SuVZWt1YR894vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
رونمایی موناکو از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102702" target="_blank">📅 19:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102700">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/102700" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102699">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102699" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102698">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/102698" target="_blank">📅 19:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102697">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8Xi0zXGUFmevZ_CjQb0Cx8h9XRYnRoQAcnoRLXK8bThD4f7XV-kM9U6YVZzd8leuKCPUBMKEc3iq4KG_a4bWvb3iu0--ok6ICvYPNRYA-Ouh0HsASGGjOksaSHJSaNBoO-mOLnmdYLZ3twKg56ThBT-aHdTHatznxS2h_FHII7CWjoLkhZaC54YwDMoIy6d8IQ-Bp46OrvRydQyKEbotYxqd55CKypJP_jgIv6D67uUCd7FgI278fe8cHmec3O8Q4LbjLLrr1FDBKouGYm8lkg4tl5lb1_bGnI3jLXx0VKP-6HymrVhr-2n70yPuNmgD9Se4t54ORpP9bURDdYR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
#فوووووری
از رومانو: ترابوزان‌اسپور ترکیه اولین پیشنهاد رسمی خود به مدت دو فصل را به محمد صلاح ارائه کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102697" target="_blank">📅 19:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102696">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlKJXyCjAw5gDNEDNhN283lGTQb1yobskak4nj8EgcKbsA3w1pDUn-N802y6MRfEudehSjyHeoqZWxDdHMjs6OnsouYxkasZ7_QbwOWlcEGuQulwz_pSbjI4Fwyl7idTu9cCPuNb3sm60x7PX-RkP4N6w7Tb6UAMH0bc9-I8VARQBK-B_ErDCwwkeBKhMkNx6BPnBlg2T1YFA03QM20ZszXlIF4k-ezPgWOQufC1SHml-r3prpMYWqAwBiYCK-ZbHiR2YclGRDbiWt1edsEopU8w2Tcm9Agfmc0TcDx2K1P3ZLAK1GuNT2wiC2BrcdQ4e8J7M9CFvqSqsNfIajoQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#رسمیییییی
؛ علی‌نعمتی با عقد قراردادی به تیم لوسیل قطر پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102696" target="_blank">📅 19:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102695">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/102695" target="_blank">📅 19:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102694">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsfl2lj2JMIgSlmrMCInOqgfkAxdevHeVQAZAUGEq6HZC5hJCTTlozZTxvGgZaNAyerMeVLL3uA0ctvav5EMNIyGYv0hLk1X9mmQjXDg25En-nDUdwUv7d6Jv0R-ddp_oo81a1139sd6F3gMN7XjpVKvNkmAKJs7pfU9FYN_DJp9n9rbjwA-WG9xwil_chHzbXFymUi-LUTmay79LMlBk3MMtnxpZCQmeU-z5NtGIPWZsHSqs_eeAQx6E7wpUWuB8dWXxuhwwwKa-nqWKDPaCwop5tlfuvWw3yfT1Dy7eGSX-YTmV-hm606RPA6dMgiMC-NNdo4s0QTWQhf0y01NaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی برای حمایت از بازسازی مناطق آسیب‌ دیده در سیرا اوئیسته مادرید، 80 هزار یورو کمک کرد.
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102694" target="_blank">📅 18:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102693">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD2jUiZh0l6DghX-Ln8C7uA8c8ARl2q6jAz7vx_QaMm3XmUfqu3paDqlaDX_bMl1sGxsQAplXnFxgjvhzUcI4NQew8BC2Pvqg3r7Z2DW2Luxd2O5R_jjfWjaqSdRJcIhx1U5AoydVfABhlWedCct4d0EAaUjYj5kfONmIY4o3cTf6fLZYmMEHl7HurE8QEitKQlfLVD8kaqLe9i9bhPOvJtDz40BQC5c_kdSKupb9AhDN1ANam4Nl-pTceupbLf4IPlT3KCkDgZ2FeoGqFhV8g75Gh4S4LC4VTQsEeWNrYxPMxHFkHkJ5s1taCrGLlYouc1I2JPt09do8xr1gaNKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
هروه‌رنار سرمربی تیم‌ملی ساحل‌عاج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102693" target="_blank">📅 18:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102692">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f0d298b0.mp4?token=urZhn5loDbJ3_szNlt9pE6JbmrprSkCWSkV_H3JxZRuz7Mi_fy8EyRUrIYbfAY_YlrRu9G6MiJd8ZwssF9DVdvuMlOhF4Eh13CWaDMOMLPBwshcqP7Gw7X8CjxP9AAIWqof3IXHtUL6iO__7chkTzkM25MD1rRkyv8JMgeLZ8aE9NdWmO92Lr8thtloy_iQfZudZWG08oWAsNytB2-oiADyXmMzMoSOHllDF0hwbmep-ia5CxnZx8_ygecU4AXr7SrTpHEP9aaNTfGlzYTbuCqNpESh4fJUS42qSQtY5QjKYU5z8b9w6suG4Hjo7S62UOXFtsyR47Peh3TumQsjhAxkeCmsJm_g5zh8Lvvt0NIb58_YA7SnRhTWRVaN9XY74WKyqLi3uPXL089_FpY2ahKvvISI8vNObRro4s_R_Njn58UnEMxqHNUmI6Iy7Qb3XgNZZp2GhJKOHRB63uYfoJTqDE9aHXIcyIprK9NhxTOj9tL34sLXaSrC9AGAscCJQBko_owV5rON-5kFJBqq0El96ZhCO0rJ5Z8fkETvM9Ni9XL1EOsLzfWDpeIpQoY-2y0y1c7patXXCm68AnCil7Jj1rxxauUYtR4Y50MZyHMT6LgXPWm4Cid652cC8DeWsYY2ofqNZVl6f1TXY0C7uWLLtW8wIDyB6LLoadIFHa-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f0d298b0.mp4?token=urZhn5loDbJ3_szNlt9pE6JbmrprSkCWSkV_H3JxZRuz7Mi_fy8EyRUrIYbfAY_YlrRu9G6MiJd8ZwssF9DVdvuMlOhF4Eh13CWaDMOMLPBwshcqP7Gw7X8CjxP9AAIWqof3IXHtUL6iO__7chkTzkM25MD1rRkyv8JMgeLZ8aE9NdWmO92Lr8thtloy_iQfZudZWG08oWAsNytB2-oiADyXmMzMoSOHllDF0hwbmep-ia5CxnZx8_ygecU4AXr7SrTpHEP9aaNTfGlzYTbuCqNpESh4fJUS42qSQtY5QjKYU5z8b9w6suG4Hjo7S62UOXFtsyR47Peh3TumQsjhAxkeCmsJm_g5zh8Lvvt0NIb58_YA7SnRhTWRVaN9XY74WKyqLi3uPXL089_FpY2ahKvvISI8vNObRro4s_R_Njn58UnEMxqHNUmI6Iy7Qb3XgNZZp2GhJKOHRB63uYfoJTqDE9aHXIcyIprK9NhxTOj9tL34sLXaSrC9AGAscCJQBko_owV5rON-5kFJBqq0El96ZhCO0rJ5Z8fkETvM9Ni9XL1EOsLzfWDpeIpQoY-2y0y1c7patXXCm68AnCil7Jj1rxxauUYtR4Y50MZyHMT6LgXPWm4Cid652cC8DeWsYY2ofqNZVl6f1TXY0C7uWLLtW8wIDyB6LLoadIFHa-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📅
شش سال پیش در همچین روزی ایکر کاسیاس از فوتبال حرفه‌ای خداحافظی کرد.
"عده ای برای پر کردن زمین می‌آیند٬ عده ای برای تاریخ"
⚪️
🔺
ایکر کاسیاس از دسته ی دومی هاست٬ خیابان ها هرگز ایکر مقدس٬ یکی از بهترین گلر های تمام دوران رو فراموش نخواهند کرد :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102692" target="_blank">📅 18:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102691">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102691" target="_blank">📅 18:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102690">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102690" target="_blank">📅 17:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102689">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
⭕️
🇺🇸
روبیو وزیر خارجه آمریکا: مذاکرات بسیار خوبی برای بازگشایی تنگه هرمز در جریان است و احتمالا امشب یا فردا یک بیانیه مشترک صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102689" target="_blank">📅 17:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102688">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEcQH_1kIMaWcXts35wp1Nonx1l4RF_QnTn_AK23G9V7-E45vEebyMm0QvaJkZCZ9f_7ZfFODJ2gMLS7Z_X4Ivb19QeVYZhHgChYiOKWYlcSOpRxcfDfJc0YzzbERX48mrtTELsVhIZiNVmm_O542OQznhSApkE6p0dJkVe3crKJi2MzIxXy5XM_R6WSjCCYYikDMtiMSqY0_bog8dKJUc0_4v1kWwQijBJTLYzYl9z-HS6BTz-59SvUZBUMHh0bK2kEDmAHyNKuHRmt_Zi2x4AOxPTHARSqDq3sHdn0ENLQ0x8AWaPuvTah2X94hs4g1Pk4wxXA2jEJZ8g3Clz9cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
چلسی صدر جدول تیم های با بیشترین خریدهای بالای 100 میلیون یورو در تاریخ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102688" target="_blank">📅 17:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102686">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAIedibtgAfqpuFnhbmI40DgrjsSPYU2XdI3QiUTYVDtZyc_IjUscdTXDh4HFVJhcWC8y5zCG49FZTRRvOAZ4kYwCP1HC8fsl0zv8d6vT1G5wvKqL84-bP7z8yeCYogrH7wsULPWAYVDfL12SjJhBjGpG46K2ndT0FN2GMj-7NuQEy0YhvmizHMOV50dUNFiqp7V39s6NCvkBNbW6z6nmuVjtbYe-q15KcS4YUq0Zvx2UrhYN8-3kF_Ol-t94sZ4q7zkh_zqakePlhLlV_Ntzl4FVRSRY-vJFNKX7N02Z2K86KSE723gzuEx2Oa1gMeKFQcb-yksofvyBuz0WcppwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7APQ9i1SCYeoLwn5uFJofVylrKUHAhDFKlcZ-9m00DDwljJiEVMkUmHUq0Rv8Nt8t_ej6YzHg4C9h5yJJSRfsJvoW-RldWOvgbpLo5Gesya_uN4UyR_ZFNJjAQ6IjlkXD3tAJpPsFVs2nlHaHSLeOWZaXqwb7gc2QntRA0JiIfZqHfRnvvaTgq6S02nKp973Wpszz1zRP2sSyAOmfHRMMVlLZPoPQ9MG8tbBlpss88puZVhcQkveAiZc_k4GDHhqnrFGTXAb_SfHNstOnmWRoOASvvz8znRt7gXA442x9tbOwSvJ9C5HsKzUVSsx8788oPTXsmx1485JrOfmlTnhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تغییرات رودریگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102686" target="_blank">📅 17:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102685">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AceDAJz9KevIt_jqG7J5qMyC4bkHzsrPhPJp5-zBLv-DhbPLY8PwL2pUs04bD_1G0mTm40w26hsrBHdo6_1eN72_rplBaoK1dPhFs_x4Vsv8kqamQ3P06RM5DImNQZ_W8weli0fCw5SA7P1pDioxA35Bd9PsCIJiUX8MWu5DeJxyqatQ-VIpBUVsOREHzGCDBNxCwd6uhfEC25BgBT55NiOGMzLYEARBQBAXypCRcuFr4MZk1ATFJAAitTyKuz75IS2_y36M7UXgaqvRax5xfaFu6JSm0qO2xlPhHEQhOnrpu8dTmasBD6tGMSgH5pbVdJlHXhPpBJKzlth6SWyaZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
14 سال پیش همچین روزی؛ باشگاه یوونتوس پل پوگبا رو به صورت رایگان به خدمت گرفت.
🟣
پیرلو: روز اولی که پل پوگبا با ما تمرین کرد، همه خندیدیم چطور منچستریونایتد می‌تونست اجازه بده بازیکنی مثل پوگبا رایگان به تیم ما ملحق بشه؟
🟣
بوفون با خنده به سمتم اومد گفت: واقعاً پوگبا الان مجانی به اینجا اومده و منچستر اجازه داده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102685" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102684">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102684" target="_blank">📅 17:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102683">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTz4h5Y6YdUbIj2XoqCzx5TDNGP9KFWrjy_9uwrN-wAZFCDFOf1T5rnFYhVgfPVfnb84olORucEsboAPjpyqZoRYqLw4rzGXLeU__ov1db_5_QPaGPCx7XYtrLXIV9yRafXhozbN3k9INIDhmFX4PCiqMk7Fqk0SBEo0wpv_c_pfpFl5uGoceBICjiaYyPH52JcGZu4SS_WqtYJYo8FZMDMYv0srkT4DZ19U6KbfWz9nPBqaeNFJsLBeplzYHd1IXGh6AFJZlcEu9NVAFTXT12Qo4bwdO3cOStXNT6z33Za1gSyk3VSufzWZkfEa1cDK6g4enkljd7iSf73OgW1igg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پست جدید بیژن مرتضوی درباره مصاحبه همسرش با مجید واشقانی و شایعات بازگشت به ایران: تا وقتی جمهوری اسلامی حاکمه به حرمت خون‌های ریخته شده در ۱۸ و ۱۹ دی‌ماه به ایران نمیام
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/102683" target="_blank">📅 16:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102682">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102682" target="_blank">📅 16:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102681">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102681" target="_blank">📅 16:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102680">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrWjXDhj3RmJdWdCrEWdF6dsWSDPdZT1xEapHjz9XJKjQDZvkOEOu3AlZBhoDuSaSGaLtj92oWeE1FcJRH-GIF0_bcyjvqSIyqUZetkpafNPyH8GoZuPEOUEJjABt50rCTkWfoLuk_SKWsEVYQ4sv_jf_dyGp63U6-wtM03AEMWVo3m_tKDpIVWfsv0JRlsTcxn5xUdzlzuY1M7zhQA4FkCPHMAD-ujSAv_T_mjrqm_DviJwc7b06Oq6rR3zv1vYhzhc9fh8b7dXF-qV8-L7Mfw3LH-pvhaqSvaz5f_3X-_K7kvvBNBbbpVlQAjrHULwU2DwIvI4_F0pzk-NdtSySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
🇪🇸
آمار جاودانه کریس‌رونالدو با رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102680" target="_blank">📅 16:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102679">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102679" target="_blank">📅 15:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102678">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVmDimc6ONs0QyupNy4AbB2BUTAH-OWp1nPYXVtQdqGbydwHth8KbZ0quTteSRXGKpiZV_C2oN5KeOIQeA-OBKZKREGkomlzMDQjUqAmFpDTepdrGNIpjcm50fpa9O9cg4WiIZkA5jzfe_-ODefyA0QUdEA7vwMw4OzoDVxs29nbdqz_PyPWVEm6SnTbFTEgwNzp7mvsO2MQNEfT4-B4M2QHGFV847-dF_RLO2YHknzap5ntY7FhlfKOq23D4zqvgffB34sfOIjzPJNeCk5hJpptJbeCwro4rseOPs1M6ptRjCX5w8nFbkL2UlPpkZrcmHQUxlxo-WpYIXLEmuCmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
💥
عملکرد ۴ مهاجم برتر دهه‌اخیر اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102678" target="_blank">📅 15:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102677">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PodPkMOONQRiKN1ZULP-VEZMy2SFnTLRmoH7jjJrGDoW3ga2lDWDpm5TRWl1oIGA66BTyGG--RqIn9FTWMCyw7N1m6aCePdNCNDu6Bpscgf1gOSDbszP5iuZfRUgUH6gfUSNaDWncK7TBcxCy0lDjWeailgHwV50-1lwKIeZ8P7Fdlg4-OTYJp-roPwlPRd7FZ7ekZHyTEoeOE8py2Cg6vwfA9Y7e72AhInL7WN1Du4uMJojOkMAfC3tNAttsM9jNnu_HtJ4aeCnpMVr-PwuCTzfaxwpT3eu4ok4BykD8ejJrXRFvhmuBF02Xv8f-d1qopyva_LKLXwg4XbUmekQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پاریس؟
🎙
فران تورس: خیلی خوبه که باشگاه هایی مثل پاریس بهت علاقه داشته باشن! هواداران بارسا باید احترام خودشونو به من نشون بدن تا بمونم، فقط باید بهم ثابت کنن که دوسم دارن و بیان باهام برای تمدید قرارداد مذاکره کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102677" target="_blank">📅 14:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102676">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102676" target="_blank">📅 14:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102675">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzKC0kCw8M3MLwgJiIDuVtxxEvZlTXtFlN5kyfOONxsUapZuSg7zQ5FXmktbgNKCKs9u3hZJPtZ4-gPJAw7BtkRzcb9eszxtJB5M_cmoKTYNw0y4IGm4zz7PMLlF1aags6Hm1_kJM1xDoEMgNLhtFSOobC3pMtknfQdV6vjkdy0IH5MEK_-WAJ5tsQRuhAUZrbG-CXPhnSQPIOWaIsAsNgCW8OQMoBFU37ReMb55rtpFtXTgucRwXy6Jzu_ls11dNRBaMWBr-B3hAMyluH5CBA7aWqpCUZkhPH-mOKC0Flo9KZEeconFcvrF_xBTEvpxcL53zxK1IziRZwMquagUKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اولین جلسه تمرینی ژابی آلونسو با تیم اصلی چلسی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102675" target="_blank">📅 14:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102674">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102674" target="_blank">📅 14:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102673">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLxrj9DLn6b53SYXriQ_wpMCA8tfbUhoZV2xq2XK7kHAYiZbR1b2U6Vv0mbEZOHNupT31pLXhNzv8T5A5w8ZE7f6Nk9Wj4KzvHZ7UDb8mNTZUImLW8R4AYbKro7uOHm9NSFQqI2jO3l39inV3bYZZIyqLL6amnygqYBTkTHKbDiugS_5rQ67ET3lVbzQV8VN2eV52KbrXRlHuJuc9C2vYIBV1705Ee1oJQfC2KOCFQ82anKIyCFvnu8mIxaum_QJKPxOm4hmMYPPBpQBd8TGw2fH0tjW0z__4QeXul9wNErmSYE9hGepErQuRRzn3ORxErdpmkqOVzxr4B78wDfNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس سنگین ایکاردی به وندا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102673" target="_blank">📅 14:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102672">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
شهرک صنعتی شمس آباد انفجار رخ داد که عضو هیات مدیره شهرک اومد مصاحبه کرد و گفت یه مخزن ترکیده و چیز خاصی نیست نگران نباشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102672" target="_blank">📅 13:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102671">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4x-U81f_lSDeeM9ZoNKq5TIuV-8NXVvPMJun7LUG_jl-LnKX_Xym99-6s2sCHtld-AWdLG5IaeUyWQJhQJ7CLp0nm9rBOGlvHbtuYmql_dTqshK7kg1v878y4tO6lYuE_d_UJNO8doR_gmilkja4uWjc471ceLU7U65bkCrHba1qtDu7Zqd3EkGMq70LUHMFQ1ZpVHG0_PE8I0wsDyPrvqjA8l3RvLzsJESjYPjHE5_VMAQIy5U3CWGuJ9XHdsucdfgRrEvs_f5jrKrpjBu2yBwozDxcM7Qx9IHjKxlq-uFjNscGBp6Og7tFcoW5TnzG64gbbN8uym4TDJxo33eyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تو سبزوار یه مرد بخاطر اینکه زنش پیراهن امضا شده پرسپولیس رو به اشتباه شسته و امضای بازیکنان پرسپولیس پاک شده، درخواست طلاق داده و به زنش گفته که کل مهریه‌ت رو یکجا میدم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102671" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102670">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102670" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102669">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv-_oqse4mW7qxnzQvS-9fkcuQfe5XJ5rRyJfOSqg9Kqi-q5xYH2JF543WQ6MgB4IFh1004yTgY4ZKa07GaqqRDXBXa5Oq10kRKmMtmWQpNvFrDEAz5lW3KG-_rsY0M6yZ2eqxKRPcXl74YxKQ0PLZoN46yJxPgooyg-snYTe7sBIWJpVz-CjlUTbuuaQ4p2KBHVr17abpaZGdaq8n2t59maT06Y-PEJYT7oaqkRwbnKqBpCQonwsZ857y0lBRDKUyHFk_l-bQ0lSdLviyctylfTpBei_b2SMQa88sOoJsnJ44lXfrHacZQ8BVzFrzIqIRGi9Sh1aifxbDjF_ZwXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
متئو مورتو: باشگاه استون‌ویلا درحال مذاکره فشرده با اتلتیکومادرید برای جذب متئو روجری است و احتمالا تا ساعات‌آتی این معامله نهایی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102669" target="_blank">📅 13:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102668">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102668" target="_blank">📅 13:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102667">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102667" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102666">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102666" target="_blank">📅 12:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102665">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102665" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102664">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOfEYMUW9kYYpgEIuA5FWmqnYV-4dHJT7WB92ssAmQZg1njsJpi4Z7fwbmve796miXcN7HlY6-2-lbzF7rujeBGkUBxOqV11rb9fVK85yIL1tIt61J7IQZIV5O2BE8cjp2jHYQdQ5rMoTzVzt-Ls9W38UgiCDjUZ3hXP0hyi6V-VFcfSY-CRvSRwP0aQrER9iO9G5Xr3uJMhMaF3JpKg6WAINodyZ8J3duwsiQrjwDcA7yh8xiqerCajGN0tLKoWK0vRKbNsFsnTWnvmzwAYgssIcJq8ZkpnTvZuRNnuL3AY0WFj_I8lgidrHrBnRsjOnlyOBLeUuxfyTevx63MYdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🟡
فلوریان‌پلتنبرگ: بایرلورکوزن درحال مذاکره با الاتحاد برای جذب موسی‌دیابی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102664" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102663">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnFlWr6Cxgbwu6L06W8J5PaLzEFuKb-mDaI3Dhpu824y0GHoFSk_aBWA1PUMhy8PFqYzm5Q4NQJaM8jybwy9FFBCxpdnDMiL9F3PDrhNFgdjifMXbrP6mZITv8-S9Vld5LB7fIAtxS5dCJD2h6fw29VAtmXwkfCk6ljhJkGD4Vpb3yElZbumZpguiK4E7-N8BMBxIajBgJ-ZVFgb7UHnHn64hPktZ10GRDMzECjETzoYMKbkAdwFp2JJrpbzfM1dKEirs1cuGVnyB-ztwy5GXZE2Ic6p0v3uzQ9A5Jbz4qD_bOutIQ7HMeJKvqwh9o8h2tUvXBbDr7cNHdDErf8Dzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚽️
فیفا با انتشار بیانیه‌ای خبر حمایت دونالد ترامپ از اینفانتینو را تکذیب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102663" target="_blank">📅 11:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102662">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UITp43Tu7Z3xq3KL78biQer--Ck-bMO4HJyZCtGZdRQslMKnQryuV_zwUXGRUHWfg2r7CCaN2gP22E-DCuENVDHOS3ShtTNABntWMJ2JGQkoBQj21BagPf1rv56x8v49f2yuBLicM6AXJNxZLOsPg-LscPqljpIqFQpYFGKThrmIt6JVkJUptkf8imJB3L0Co8bSIQsGBRZ1fVoxQEHpnEsiQ6-CoSSQRi8t_PMC8HDjsZOjrHAk3Ub5SZop0OaIIEVBXZ3wMGwdM7wxS53cIUkjOHT7yTlxASwYW7lNREJzZjYAx-OZkJfipWyVL1ZLaBe7aq1UqyosM1e3wKg6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
⚽️
#فوووووری
از مارکا: رودری دست رد به سینه سایر باشگاه‌ها زده و گفته که فقط به رئال‌مادرید میرم. قراره بزودی این معامله تکمیل بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102662" target="_blank">📅 11:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102661">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uQbn6QAtRi62l8XWh8BE1MgwsMQwrnirNBM0uGYYXhPJvtmfN_6RCgv2kqo43bhWUOwRkV4NLevuP8UdJ0gmXPE4p_LI4weOWkvKmorfPEQp7yaps_VL3-0B0O1eTQRcqLWTV83gTXPUxSiDQvcll1tfiD7q4raktdq7bzpGGQ-vzbjPjNRuyeyR1J0T4Vvn160MKPKNAtQ6MqPJ5ILh0h3ms8AemO-35fw7fn80EUNeyuna6K0Hytrdvb9oWg1f3nq6jWsaMqLxOviSkyV50vtHLuxqcl5S6Qu22lhd9q7l3S6qygqp1wBOP6a0_Zg2636rVAOsKB9El3gwcvUAsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#رسمیییییی
؛ نی‌لاند دروازه‌بان تیم‌ملی نروژ با عقد قراردادی به لایپزیگ آلمان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102661" target="_blank">📅 11:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102660">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
‼️
😆
😆
🎙
ساکت الهامی: 55 میلیون تومان دادم کت شلوار آنچلوتی را خریدم تهش ۶ تا از استقلال خوردیم و باختم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102660" target="_blank">📅 11:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102659">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yao6cydMPDDf_6O5SveyjH3qjr_zvpZG21uLpWBQmWS1VYqyoW1zt_J3MuoEkXq6lidt7eOsuHuQOgo4D3q7dzYpfBpGv-SMZ9z2ZyYeV3lm4E2jbdOyy2uZXPfwYF0Oqq7E2eGqR4hHZ3XBVRhzqAPjW-MMvdrn6H71JAUOkAmeivDHto_dmNpEAn7jxx97jlkHxu7WRdzGhk_HHkhphNeEwyGLcWyY9ySCRKp-lCacK8RK_dFHzQAXHcl46Dr7tLyC62wR9cbDv86934V30tuvtwe0e7EDzry8YMTqKBYJP1WOsENpABI-PecFjemNRYg4UoneIi7roT0PFgJBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژاکس آمستردام از جذب مارک آندره تراشتگن به صورت قرضی تا پایان فصل از بارسلونا خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102659" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102658">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102658" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102657">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0e4679b6.mp4?token=EI_6HTaKTj012GwVCeMwVP0Eh0ojgqsiat9sT1CxRvyCwiy6va_h-7Ssu4W7hKddRIU8sTwQNufDvIdCSa8ZvhFmiWpgPrm5epcejSqcHUIfIAicJn_5YlwXcEj37w0tvusXVW48ReQZ8UjEiAalmFfV1wrieOhnlV6wVshrWitxkiSjmKoPN9MEIArCzITmEVywIpQQoSq47yHJ6PhK5tOLh5VbmYGqbhCLBQATV3XqReOmTQb-UVVPvND-0tbL_Evhp56i9U1fRMDhMjl4MZLycKesr9I40zM9pjbnYIotnWZnPkGx3Lyaay74x_gotu1diJZjcDt6muQxyP6MByc4anFiwA8xR0McSEqY6sheIVoEz87fWW_n1CzdQVziaXE3V1lk_I4kjN4DSL1GUn-UbWdrZKDVq0vs-q6VrUgX-yxxZ6yMl8YC7SOtUbo2K4toGKF-_zDSVqDOV5TDAmgb0rooI0NjkfXrL4gwF4wLi7Q2i2LiE6NyaeFOWt4E3eQVG-iQ0HBGl1M_mshUk7EHcRDsUW4jKddyPDNbb44Tgm-k17TgOPBDheeFKuiDt_GYYIlqd0mBSQxpIbUZ95noxL0SvdBikyNct4hg2Lu8bgjnHsSt8FNagiAGIUyt-GQML2aGXl2gqAh1aW110hFflG-8x8wGELAU9YqKNSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0e4679b6.mp4?token=EI_6HTaKTj012GwVCeMwVP0Eh0ojgqsiat9sT1CxRvyCwiy6va_h-7Ssu4W7hKddRIU8sTwQNufDvIdCSa8ZvhFmiWpgPrm5epcejSqcHUIfIAicJn_5YlwXcEj37w0tvusXVW48ReQZ8UjEiAalmFfV1wrieOhnlV6wVshrWitxkiSjmKoPN9MEIArCzITmEVywIpQQoSq47yHJ6PhK5tOLh5VbmYGqbhCLBQATV3XqReOmTQb-UVVPvND-0tbL_Evhp56i9U1fRMDhMjl4MZLycKesr9I40zM9pjbnYIotnWZnPkGx3Lyaay74x_gotu1diJZjcDt6muQxyP6MByc4anFiwA8xR0McSEqY6sheIVoEz87fWW_n1CzdQVziaXE3V1lk_I4kjN4DSL1GUn-UbWdrZKDVq0vs-q6VrUgX-yxxZ6yMl8YC7SOtUbo2K4toGKF-_zDSVqDOV5TDAmgb0rooI0NjkfXrL4gwF4wLi7Q2i2LiE6NyaeFOWt4E3eQVG-iQ0HBGl1M_mshUk7EHcRDsUW4jKddyPDNbb44Tgm-k17TgOPBDheeFKuiDt_GYYIlqd0mBSQxpIbUZ95noxL0SvdBikyNct4hg2Lu8bgjnHsSt8FNagiAGIUyt-GQML2aGXl2gqAh1aW110hFflG-8x8wGELAU9YqKNSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
▶️
آخرین فصل‌ لیونل‌مسی در بارسلونا
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102657" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102656">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برترین گل‌های محمد صلاح در تاریخ لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102656" target="_blank">📅 10:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102655">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzEIEP1EFY1we2j6I9Z9GxlL2t-mpIVEC9PoM7z3zwmG9sBxXHsyddIWPkVxzqSiZdNMWrZIVOVKYk-ujJ93sYHu-_5LYROHMA0zmcfr8P_l5OeSHlsY5cq9Fh-A0jcLp36Hy8lzGQrfywqyPgubZPWl6eosgIiIkcGvqzlRVHs5ySUsYaAR0PGbGJ0075RxBI6xmIRJwM0HNZPcUoa2-ePrZXgGAi4j4k9BKyeT_jUCqKz-rp0BKM8UjItra5-dA6AWk5d55oHaysqRHqId76FCiB67u5QCkHP2Sh_eudSjHZcXqxsJZBzM1QTtysVj8saDdodjK1Rfk-FrdxJi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
مدیرورزشی لایپزیگ: دیومانده به محض بهبود بیماری خود به اردوی تیم در اتریش ملحق میشه. دیومانده بازیکن تیم ماست و به قراردادش پایبنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102655" target="_blank">📅 10:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102654">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👀
🇪🇸
🇪🇸
یادی‌کنیم از بازی دو سال قبل و پیش‌فصل الکلاسیکو که حسابی جنجالی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102654" target="_blank">📅 09:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102653">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
‼️
😔
🇮🇷
پرزیدنت مسعود پزشکیان در واکنش به جنجال‌های ۲۴ ساعت اخیر: استعفا نخواهم داد و خواهم ایستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102653" target="_blank">📅 09:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102652">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102652" target="_blank">📅 09:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102651">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TttQfYtL06AB0GWuzd7LypBbWOM76yhCzoKJNK_wcF4OlK1Tev6AphSysA0P-U7SwDGlU7Qf7aOv8vQ_9G1NPdVkaamB1R3PNnZgwgCwuS9Mp26dIKYgWmU9VoQGCA86nistSelRr4n2MQiNqYKlp8iW3kzs6ghlNfKxqOZR5rc8bj74a3J0gNqGCUadh3pd1F_Ut50KOmfI3VwtODDZuHHqrS2Qb69Fiucbp5nbGe30VkCUUxAIi6ss3RlR0nYHBp31NxLZ--QAuvHCIkvePPLShTTixazyANAMt2lywvo0NGEVjVH4JgGnTpNabexmcfqmdV5gzzuZz_hirvMJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
کشور عربستان سعودی در حال ساخت بزرگترین شهر ورزشی جهان با بودجه ۱۰ میلیارد دلار است.
🤯
این پول معادل هزینه خرید ۸ بمب افکن B2 یا ساخت ۱۰ تا برج خلیفه ست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102651" target="_blank">📅 09:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102650">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeIecWXv7za6JA807m-ERhRffFF8KUbFcTfk0D7Osmmv-4rhuSLT71Da6R7r_6H41SDPhsDaRbQbs8xpkkZzckFx-i76xNe_ss0GhVNHEMAvgwXdPPLN4fizxtmUxCxLfHrFhFAx9rxDezpPfm8jXRXYLggLClO-bJobxX5whbfvCvMzzS4U-dZeQcAWiPoM6uiVH5WFJWn-Zpe3Ovh4fwz871Wn-dW9JBd24b1XWe2iCabpAbHYeF85RbSrSxGOoM2Y7f3nr457fglDvJ3mK4tCFhof50BCDbEXaFskrcwFMLZWd7d0W8JdaStqcuos_8wvKGVZU7ziAFRG6W3qAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه سان‌انگلیس: باشگاه استون‌ویلا بدنبال جذب مارک‌برنال ستاره بارسلونا است و قصد دارد رقم ۳۰ میلیون یورو برای جذب این ستاره جوان پرداخت کند. هرچند که بارسایی‌ها این بازیکن را غیرقابل‌فروش اعلام کرده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102650" target="_blank">📅 02:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102649">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d8f16631.mp4?token=SwhURhE_l4YjNgnkU0WUp72b8rKqY9k-2oGsFO-N-DNdjCq1x5TeMj0_Xmg7NlHLY2wP0oOLEx0JzPNrLAD_4Y_tpfZmva8PAx82xundAtk7-scUw6WG2s3UpbzZqXoUANKQBDZuAQLsxCLTlFAoJMAt7YxnY63LdlOcoRl-AX9_byTr1ZHG_OXIN7BwuL-B5_OssUfdsWHN95AbqEL7s0M90KxxCD-CA2WXi3fMJ1qkbl6gss2RNiMB69fjaq0w8dwSThYtJ_Ku3RVZW_noF6XtRXbWF14y53E5sHXKtkTGbTop0vOZrl9SCODFrbysA7EfdvpwYV1twPRLbWwGaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d8f16631.mp4?token=SwhURhE_l4YjNgnkU0WUp72b8rKqY9k-2oGsFO-N-DNdjCq1x5TeMj0_Xmg7NlHLY2wP0oOLEx0JzPNrLAD_4Y_tpfZmva8PAx82xundAtk7-scUw6WG2s3UpbzZqXoUANKQBDZuAQLsxCLTlFAoJMAt7YxnY63LdlOcoRl-AX9_byTr1ZHG_OXIN7BwuL-B5_OssUfdsWHN95AbqEL7s0M90KxxCD-CA2WXi3fMJ1qkbl6gss2RNiMB69fjaq0w8dwSThYtJ_Ku3RVZW_noF6XtRXbWF14y53E5sHXKtkTGbTop0vOZrl9SCODFrbysA7EfdvpwYV1twPRLbWwGaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا سپاه به پایگاه آمریکا در کویت حمله کرده و آتش‌سوزی رخ داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/102649" target="_blank">📅 02:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102648">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇪🇸
#فوووووری از ESPN: رئال‌مادرید پیشنهاد دستمزد ۲۲ میلیون یورویی در سال به وینیسیوس ارائه کرده و قصد افزایش این رقم را ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102648" target="_blank">📅 02:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102647">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJXeKj8nNC7o_a35meRC--s-VWYytc-_3OgGLZ4_z-UP5ug-7NAAgbxLkYTRo0wIHbAPuwJ9gqGJ7VeqU1mFbv9FGpO5obxkJ_4BYPmfpmYjrzeJUZ1S2HRg5npN0FiZ-RwFOgMdju-jlx9RYu9eMH0Nry9mwqDwW2JOeYjXTdalHrCeZYEhtq61f0H7uOljTUTlB3_-nlVp4LtgNhP9II_vNps2s0r-ApqI7AngbxTPcMxpwXoG5ot1ujDt1zAnHwvyT1wmFt_pDlwr3GmT5i0wYMc4tTcdPuc5Ojvnk9s7BAsALyunWd4KhBxYUpKF_KMtWqSEMhelLjhECo5Ksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از ESPN: رئال‌مادرید پیشنهاد دستمزد ۲۲ میلیون یورویی در سال به وینیسیوس ارائه کرده و قصد افزایش این رقم را ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102647" target="_blank">📅 02:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102646">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_j3H4OmCuKW0YM0JnmR8VzYzJDOecIm2vmwD4aqWJnSBB6sua-kFzbpZM0FrO4Y_nJBjqZqL2PexL9Ms-viZxtHVxOQQfz7pa2vHSRtYeCGsHTBMHr919gxlPtrdHw_ogX3TSUHUodjrC-UbdbQEMfRuBMOvIVBN9np9m33aTr7X8fDIVIUF6Owc3Vzx3onhBMfN58jwi353VofK7NYqSIOFBPlDEM0Eneh2Y7ePsBnGTl88sox_nx3tKWnOYvV-jTf0qHlxw41T7DgyMeZZUpENvAjPu2PErd2eggjbIIAFrGqMOJzURZZCofp8y-VdPSCjCkTe1LuVJnUD5rO9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
بن جیکوبز:
چفرین و ناصر الخلیفی در سالزبورگ دیدار میکنن تا درباره تحریم جام باشگاه‌های جهان در صورتی که اینفانتینو همچنان رئیس فیفا بمونه تصمیم بگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102646" target="_blank">📅 00:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102645">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmJGEHEvZ7HCjnHFWfRKOWRQPWE-CSet2_nFrybp8o0mEpKcbl6YSnHZSNKaNpczb2RLR55FIz87ebjjaYhJLqOEY_74Yp0BMB0371xUSCSZniXZlrZcjLx82rgETTwk61t2TZUD82HdvM4Of3vN5JR6mFH_f7PFCewzxGPDgO2aMZlAndfWr5b4iwRTzB4V2ZNImN7UTFea-V4nt2DJ3mI0SAuZu3wqTV2jBjLZO0pwsstc0uMqlDhsjgQRgu0H6ec4BywzMk8LHg6yWc4BpHdOHrIDFiI0b8KvKPcP0ab1eM3Cz0JM0jvureJ4yX_wl1iwzIDVzqh1PcgTkpQgQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پاریس؟
🎙
فران تورس:
خیلی خوبه که باشگاه هایی مثل پاریس بهت علاقه داشته باشن! هواداران بارسا باید احترام خودشونو به من نشون بدن تا بمونم، فقط باید بهم ثابت کنن که دوسم دارن و بیان باهام برای تمدید قرارداد مذاکره کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102645" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102644">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102644" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102643">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HOZ_qyGugqpdKwmopU3rmlqs4WBGJ7ByJnXgLpeqOT88dHtFs5EYiZypdmQVJwe2AQEcpT9Mlx032obIKGD5nxB-2o7v4HsoNpNQBi2khuL-iuEVLDD0X_FLKln20ZEu3EJYbx9I2oCzjKoMFrW3vrzUSZD9Jk-oM_Oe9vzNvT7ASfGtuGFfIP_BbKDQEkIRs8fXWrFcO37jZEv7wVOEMVhhHEv03Hzb8aryOUZnEL02A8OZsQ4MSXE-SyJ5CF_ESQYg7WecbuQoBuZfxZR9iNCJpvElnu-v4QGdEof9xaXVcQ0e2IDh23Sdhxmp5GLQpz8gUBLbmmKgqNmkrM9VFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
🔴
تارتار تایید داد؛ پرسپولیس بار دیگر خواهان جذب</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102643" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102642">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Inm1DC68Ry_f8nOvMH2AnMNLMkxk1Eb3sxJAp84qApsVp6j6ER2DhfXuz08o090odLX-0YrcCfI9jqLFfmWob9llm_xurQ4KhEV_eLe3O1fYNDISMVfqymnb1t7jRgTOM6-X4m_wJPa8wNbyjmW64qAihzy6mPUvt9gUldkynMa0sv9T0C05jocJk41bQbejLJAHspT_Sr9a1eFyW99wSBZtOC4WrqQ5sbzcCVIQ2GHrFbC8eY4F21DUTfl3u_BB6g8z_75XKewhzfmzjFZQADtWCCoUjrguJJm9pNYZ7xkAeviDdn6e9Mj_Yia1GIyKbdepYtrQhLkof3gUW4faxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
برناردو سیلوا:
بی صبرانه منتظر کار کردن با مورینیو هستم، اون کسیه که برای فوتبال پرتغال خیلی مهمه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102642" target="_blank">📅 00:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102641">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b215f0831.mp4?token=Eb3C0sPgRx3KyD-8Y8yhsjqX9YT930_eH8e5wZwtWI7Srbgt1EizT1iUJr7NZ1JDs9du4l4lxxa5belYhmxtgvAYmF70Xnpr22gXYpFB73BxN5eoEy-7nGN6FrSRJmq-CZx7p0BP52KBA0oOEyUo4V-uC-dkciE-2EWbSepyVeixWkjnG4EoU9mmMc2vZjBc2UOVE51Jxbc6LK0syzkSqj09wFd5x_ZXujnszC16nB2S7XPnLY7vY1zXfyK93IV6_rpqcSd4BuRbjrlnzAFjxvimsExX15O8_dHhs1_tF9epIjStcVlMiLZhXPwVSCV0WO_4vktaB_cuzpeq-ozvib99y8osURi1DoWxdMBYyO4EqsfuP4dLk1mtuXaCIydWgPEXJl5dFSeUcukZEDp3VSfyQLl9MB59qv04F724lmJWlxxptYe8LLSgvokzW5wZtXczWViPBsrNIVI_WkP4H2h3Q1nrWt4EMzUnrUViVsAzJYUrw9Yo3NSuB0HwcB0Lr25NBUdw9d43RE70jpZ1Xag-7n4mG9oLHNcDJhjPbQKTtezS6MDLDUKa1CCAr-KvhbBCwLrZFvX-4rGDijD7178dNgN0Tqja9RiraaKvnJJqtTFEIBla1fEFWD49Pnnm7CfC91p2Kert4U5Q5yZQBshuYYdbgM20VvOjf8Ze-Tc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b215f0831.mp4?token=Eb3C0sPgRx3KyD-8Y8yhsjqX9YT930_eH8e5wZwtWI7Srbgt1EizT1iUJr7NZ1JDs9du4l4lxxa5belYhmxtgvAYmF70Xnpr22gXYpFB73BxN5eoEy-7nGN6FrSRJmq-CZx7p0BP52KBA0oOEyUo4V-uC-dkciE-2EWbSepyVeixWkjnG4EoU9mmMc2vZjBc2UOVE51Jxbc6LK0syzkSqj09wFd5x_ZXujnszC16nB2S7XPnLY7vY1zXfyK93IV6_rpqcSd4BuRbjrlnzAFjxvimsExX15O8_dHhs1_tF9epIjStcVlMiLZhXPwVSCV0WO_4vktaB_cuzpeq-ozvib99y8osURi1DoWxdMBYyO4EqsfuP4dLk1mtuXaCIydWgPEXJl5dFSeUcukZEDp3VSfyQLl9MB59qv04F724lmJWlxxptYe8LLSgvokzW5wZtXczWViPBsrNIVI_WkP4H2h3Q1nrWt4EMzUnrUViVsAzJYUrw9Yo3NSuB0HwcB0Lr25NBUdw9d43RE70jpZ1Xag-7n4mG9oLHNcDJhjPbQKTtezS6MDLDUKa1CCAr-KvhbBCwLrZFvX-4rGDijD7178dNgN0Tqja9RiraaKvnJJqtTFEIBla1fEFWD49Pnnm7CfC91p2Kert4U5Q5yZQBshuYYdbgM20VvOjf8Ze-Tc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
برخی از بهترین گل‌های کاشته تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102641" target="_blank">📅 23:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102640">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290de4f011.mp4?token=d8I3uCclWiGs9MOu8T1GTfvRpp0SHvhjuh_Ll2Cf3d7SRI7MGWHNuvxedLky9Qq6hdlI--M5J5eWIp8xopenZeQgy3QjCR2qvcugNIFNnlOjXSDGykgl9QI9TUWNlJHSbbSXj2FINo612caxQrCP0KCXSEOz3sswcF76aDM_NI3N_Kfw5lgWrZAkAWFTv0-Ii0JOYPY2u3ph3QTspHqChg7PQRNt_p8cSjWSUDDGSAn65se7a04ZRlrLBz5QVhKPZXP4xBl6LckKIQwbbhEKeOyVWkVfQ2iCYiYlhZ8T9pkqSyrdhX18j1xwcXU5bavtCEtLbak9iP1io5jcyXP50Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290de4f011.mp4?token=d8I3uCclWiGs9MOu8T1GTfvRpp0SHvhjuh_Ll2Cf3d7SRI7MGWHNuvxedLky9Qq6hdlI--M5J5eWIp8xopenZeQgy3QjCR2qvcugNIFNnlOjXSDGykgl9QI9TUWNlJHSbbSXj2FINo612caxQrCP0KCXSEOz3sswcF76aDM_NI3N_Kfw5lgWrZAkAWFTv0-Ii0JOYPY2u3ph3QTspHqChg7PQRNt_p8cSjWSUDDGSAn65se7a04ZRlrLBz5QVhKPZXP4xBl6LckKIQwbbhEKeOyVWkVfQ2iCYiYlhZ8T9pkqSyrdhX18j1xwcXU5bavtCEtLbak9iP1io5jcyXP50Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮‍💨
چرا بزرگ شدیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102640" target="_blank">📅 23:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102639">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dX7pbpZ9um31x__mKgyLnPsRGImeO3RehkEg3reNXRTHBIaKvKxVoDYZtNgkDCyJ07YsP2RtaRCqVuCa7l2Lw_A0bauB68pcELVjMGY_wVjV4zf5Du4M00ONfzbtA6UrUVUwShC5A9J3rZRellDHLzNgnoXhR6GrwPgYazrprmtWXo9NH1vInhAi-w1WKo-qsi81MW8jIrypxAmC_zFHvOuwVtD0fGSwjOHEb8YnGyQg7nR8HELD2X-JDO6Wv_wgoMynqoyZ5BH3EJ7eqpdnmr4PniEdxr8gQ98gljutkhtSYTFjjexReEVRcmHDdm0nw4PljLp6_CG9usVKsc9qQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا : رئال مادرید بهترین باشگاه تاریخ فوتباله، نه گفتن به پیشنهاد این تیم غیرممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102639" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102638">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0rRRdcxYs0vI98qcYQREEYoyY5RbltelnSYzn6U_CFGL8gFrPId38m-uR08IYJIkC4-tLoh86dAF4n2d1wR3ZC3rFqGK0_l1KJA8iMhTRkLVTUD_ohgS5d30DDN1G4dW8txeN-XfRdG9otDlP2BqY7CPLj9GPquqYg8J6FQFvypyYylYQgpdkE6lZk5eR5tRKSp6XWcLIKFeKhn6a0KBifKbaGhyG6VwWTmRhFszG6dABdrijNxDr2TPwdhvA80UzIJMC4-uJwJ3ZlhR-lRU7_xprSzCc9DV99g_zGFWnk-ODQKV7JXlx6CxL6mIbXMq1dwZjnq2EW8wU9HZgVTOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102638" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102637">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac45ed94d.mp4?token=CLYed5lzUNS39JcOQ67HNf7p40oCopq5KAVCC5h8AUspxcD4_xafyVuanpZ0ggwVW4r0OHGujZbA9nd6scQAR7p0LLpaO3bujL0u0V8YB9XvLsj-WZv_Z8dfCxoxoUvs5wfaAH-BTH657A_IZlbJFUjUeS91fYF2aCUcASEhi9XFwzeYAxZ70E5ARgazM6Dz6RF-qmgJnF-32P-H3jLBFLjWrDpDUMEik-WaH7DnxPy3dK1UwwPRqHoZNZSWFXoZDXwW686L4U8vAjHN1E35prb7_i6-wi5YGpWa2ZxXePyanxDcVcLj5hAOCD14tL0wRWxVFAsKAE4yMd5BYy5Ejy7BhBeKJc7CR5dc56zXduL-UE9jY8PJdd2Ptx9R4dH9WAVw5-obLHq2UKMyZ0VPLgR4rFgRMxXiKicC218DpQvqYhVBcEp6skw_5HCWiW1Ho2QoeY9d1GJa4-ujngkGNU7E-FZhjNlkkUhOJ3OQhfuZ6x7_v8M7r_u19rIsYbiMYHNeHagcIRHVffpdlikZpzYXtd6gglY7YA0S3qzz_1Imzo9RTXnFEndBXcSpIxYC6o771cZ354rLkrJD9UriE9tR_8OHCQeqY0tvDtfCULHQG-tov6GguUOHatGkxlC6BUyEIAnBC7OaAAhDqMZxXQki62GSTD6udK8KMBC6oMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac45ed94d.mp4?token=CLYed5lzUNS39JcOQ67HNf7p40oCopq5KAVCC5h8AUspxcD4_xafyVuanpZ0ggwVW4r0OHGujZbA9nd6scQAR7p0LLpaO3bujL0u0V8YB9XvLsj-WZv_Z8dfCxoxoUvs5wfaAH-BTH657A_IZlbJFUjUeS91fYF2aCUcASEhi9XFwzeYAxZ70E5ARgazM6Dz6RF-qmgJnF-32P-H3jLBFLjWrDpDUMEik-WaH7DnxPy3dK1UwwPRqHoZNZSWFXoZDXwW686L4U8vAjHN1E35prb7_i6-wi5YGpWa2ZxXePyanxDcVcLj5hAOCD14tL0wRWxVFAsKAE4yMd5BYy5Ejy7BhBeKJc7CR5dc56zXduL-UE9jY8PJdd2Ptx9R4dH9WAVw5-obLHq2UKMyZ0VPLgR4rFgRMxXiKicC218DpQvqYhVBcEp6skw_5HCWiW1Ho2QoeY9d1GJa4-ujngkGNU7E-FZhjNlkkUhOJ3OQhfuZ6x7_v8M7r_u19rIsYbiMYHNeHagcIRHVffpdlikZpzYXtd6gglY7YA0S3qzz_1Imzo9RTXnFEndBXcSpIxYC6o771cZ354rLkrJD9UriE9tR_8OHCQeqY0tvDtfCULHQG-tov6GguUOHatGkxlC6BUyEIAnBC7OaAAhDqMZxXQki62GSTD6udK8KMBC6oMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دوران پرایم‌اسطوره مانوئل نویر در بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102637" target="_blank">📅 22:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmBul4slOJJR2-iS_46R4IZM8v3QK2_PStQdukpxE_W_lm8GxRPV4-MdzE3BrDRJYhOYy8pl_CfTjR6-zmmMDYLEma_e4N6b-JSE5X47Zn4DNlhjRL2-LXmo0N1MWceNB6KTKAlDbpTsElykxeEhNKjs1ORZLK8uXSO-VQ-rQj1qV0w7rXIKF3GXu9eeAVSFC6rdmgG94oYwaP5xXvps1yl7FWD1uv-TT7pofVY42NLlOOzGe2k6VxgyzGm4FhsjEQUvlR6uZYqXUBhPr7_jdvAmfj--l0nnn-zOMwz51NCk7NzLeiAUkCN0s7zXGUCEmmISg7yjrzMtmayoWLbUxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXs7hvxCAu3Jy-bAJUtTNM-8Hlg-TTlJ3aLeLD_TFkxs1eHroE6HX6lYaFgl_LNWevVInWxLctkuxz5FfD-FX-mKDmxIHMw5eGCwr2o-0caAbnwmLpuAXMaQooz9aipC7nPIAjzmWRSrUWTiwK5O2Kl7qeVskXMS_gDI7hVNcISC369vLho7YDeC7xASRFOilMgKgCiwG1U2akAEe_uBiiLYfmHU5fg22mp_B3Ke0ZpCenmVycpyzlxlwFSC9SsEgtgdPOspiS4_LKNh1IJSdVdXTjFLSwXcBFfqj2TRI7N9TE1HuU4Lk1WwncyxvBu_htNHGTvt7pVqQlCvBTwPKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وندا چقدر چاق شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102635" target="_blank">📅 21:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102634">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=qqGDcseVbryylUosfOz9flXvmM0S3WdZ4uaTAbdgiVcbPx6xbfbxvxzvIAAAjqgJrvrmiQqVdIfm3Eee2aOO2467wwsA8kmZMZKY2Xxn9HYjOpfGhQeUjgMQ3lA4scAh24wunZLRQtEUyT-XZrATxzEZcZEDW5cSpu6MoHuURZgjxl0h0nZJCxSaUA9zehOmCk7xQnDzCkWTdRUwuy1t1K65pYIzz0aXgwQVz6zzeqyXb8cec0mpTwbAYaN_cqAjOm4MIO9NXSPwSBavNTstFM13-yieEjeEcVODBCSZ3WANIXnM2dh9KShs83g5rZPU5759yaBxvb-vtGDr2UYp6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=qqGDcseVbryylUosfOz9flXvmM0S3WdZ4uaTAbdgiVcbPx6xbfbxvxzvIAAAjqgJrvrmiQqVdIfm3Eee2aOO2467wwsA8kmZMZKY2Xxn9HYjOpfGhQeUjgMQ3lA4scAh24wunZLRQtEUyT-XZrATxzEZcZEDW5cSpu6MoHuURZgjxl0h0nZJCxSaUA9zehOmCk7xQnDzCkWTdRUwuy1t1K65pYIzz0aXgwQVz6zzeqyXb8cec0mpTwbAYaN_cqAjOm4MIO9NXSPwSBavNTstFM13-yieEjeEcVODBCSZ3WANIXnM2dh9KShs83g5rZPU5759yaBxvb-vtGDr2UYp6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوانین به ظاهر ساده فوتبال که نکات کوچک ولی مهمی دارد و در لیگ برتر گاها داستان ایجاد می کتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102634" target="_blank">📅 21:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102633">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=Uz8nR4Qtz7EcVeetzi7cPXQmYDLPJhS0nym3sJ5nK_niVwYtM5kaL4VPQYX87y0cOIfxHwEu7ZU8rw1tuAw6wjN830KH3j0P9YQWDnV66fj-zhYfDUYn68Bg6qHDzk876MgJWRD9Z0fE5GM1wuRui0Z1Pp-XNja3VquylPsqDTd-1xZnPOpZaKr6xuwoZOoTk6EICaCYibymyyf0jlmkOyA-ueUUy3QEczxeD520UUtZn4fQKFeY-Pn8_VweCvW2-pOqFuMYgJ01ALVW-W8hJJyPJ3kE6Bo0-Wy3W08tVfsp6rmwWJQAGACwbSL1bUqX6N5Aaw9X4VNaT9peU8OMVSE8KWcBTzTOPAblPQcDnukJmxD-qDuMGkPe7Yuln8b1qCTovz5V-cWU1iQ-cNMX3D144Z2jnAotnzt5cimCGD_RRmiUj6WEtUfUI7DOTE2WznR828YrI54Ijd-ubqx6Gx40EGr0xqHtF_kosks5CD1-PSQcE7VbKKMlqIDs58DxAEjrijHhqfU4_M4Rfv6HXd1-2ZKxtSRZcIqoA2bx85FNgKYr_h7OnrMe6QrbbdmzcBvigok8xWGSftKaQomMvGB6YsE3jN3ECT_furO8AycNxK-3qZCyYiNg9vmT_LFBvg3NWvazHfwriEE71eRAwZQwyZNnwrBQc87oPVxXcEU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=Uz8nR4Qtz7EcVeetzi7cPXQmYDLPJhS0nym3sJ5nK_niVwYtM5kaL4VPQYX87y0cOIfxHwEu7ZU8rw1tuAw6wjN830KH3j0P9YQWDnV66fj-zhYfDUYn68Bg6qHDzk876MgJWRD9Z0fE5GM1wuRui0Z1Pp-XNja3VquylPsqDTd-1xZnPOpZaKr6xuwoZOoTk6EICaCYibymyyf0jlmkOyA-ueUUy3QEczxeD520UUtZn4fQKFeY-Pn8_VweCvW2-pOqFuMYgJ01ALVW-W8hJJyPJ3kE6Bo0-Wy3W08tVfsp6rmwWJQAGACwbSL1bUqX6N5Aaw9X4VNaT9peU8OMVSE8KWcBTzTOPAblPQcDnukJmxD-qDuMGkPe7Yuln8b1qCTovz5V-cWU1iQ-cNMX3D144Z2jnAotnzt5cimCGD_RRmiUj6WEtUfUI7DOTE2WznR828YrI54Ijd-ubqx6Gx40EGr0xqHtF_kosks5CD1-PSQcE7VbKKMlqIDs58DxAEjrijHhqfU4_M4Rfv6HXd1-2ZKxtSRZcIqoA2bx85FNgKYr_h7OnrMe6QrbbdmzcBvigok8xWGSftKaQomMvGB6YsE3jN3ECT_furO8AycNxK-3qZCyYiNg9vmT_LFBvg3NWvazHfwriEE71eRAwZQwyZNnwrBQc87oPVxXcEU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاس‌گل‌هایی که ارزشش اندازه یک‌گل بوده
👀
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102633" target="_blank">📅 21:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=bY_yo1TzStuSuaec69lowkl0pM1aktBTItnoJMg6NMImdkGZrgX-lX3thYktLJ-c6VXAxMb2eRKaG5RnmW3qRdHNvrr1jClcfzuRELTKtplzFYd09dohVDo-cqMsWggHKNI2LURD9Jzywe0JclhPnF5PfRkgzHBtsAFQqRFA6POKTsFikGNSMcez0x0DKyt27qIFEHTqJ5Z7oz5pFDk2xMyI_E_hdnsWQ_i74L-4nUuAU_BB6by_kd8E_XvbcTW3KxaxT54s1YuQZeTogBdfNYaIonNCsmckCglykz8HSP_glwxEK88A7n0Y3ycZ9pTdC4AWX-IqMM69xmVSnMaHqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=bY_yo1TzStuSuaec69lowkl0pM1aktBTItnoJMg6NMImdkGZrgX-lX3thYktLJ-c6VXAxMb2eRKaG5RnmW3qRdHNvrr1jClcfzuRELTKtplzFYd09dohVDo-cqMsWggHKNI2LURD9Jzywe0JclhPnF5PfRkgzHBtsAFQqRFA6POKTsFikGNSMcez0x0DKyt27qIFEHTqJ5Z7oz5pFDk2xMyI_E_hdnsWQ_i74L-4nUuAU_BB6by_kd8E_XvbcTW3KxaxT54s1YuQZeTogBdfNYaIonNCsmckCglykz8HSP_glwxEK88A7n0Y3ycZ9pTdC4AWX-IqMM69xmVSnMaHqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فران تورس درباره آینده و باشگاه رویاییش: "میخوام خوشحال باشم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102632" target="_blank">📅 20:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102631">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoSOVf3rfm0TdZ-QQOD0jC8SYWEozyeQ4s3h0DO99GJ4cqdfKL09kjXfg8QJwW91cZKpsPaD_yxcQdz5iBInRBskx6z-oZnt3alBnpOReeA74--SzzBapXMchX7S55gqXUWBIPGID6DlEBexHxrWtcvG1r2o6oxf-hDLrST1u81KmU-UT3NtFBboVDEZzhGqAgW_hK9UZmnLEzl3LPVCEk99EMF8a0QttUqaB8i69T4933f_eqiLSCES8RCjQX4edO1HPm_2UWjztRngcGPqMf9futT1s9o3l6P6rHX29Fo7uAz6XSIl_wNr8ig_N-sAW-4aiXySE-cRCscKyWMXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
تلگراف|ترامپ تمام تلاشش رو میکنه تا جیانی اینفانتینو همچنان به عنوان رئیس فیفا به کارش ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102631" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102629">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0jOBAzVRtWdwSTVPYz7OWPVIbJjkZmGW6HrLbc30X2Q6MZSVIFnrq11Izan3_9YnZuUYCM60HCXS_Q51tQVRau_A-nno1jDRFfR1IMGdoa2inSMmpssJR_dqUMnPhjrpxzVJxloPt1xO27O0mztRRV0g0ioAAQ91ofW_gF2LhAF1E01LiwzuZ-XnhO1AAI04Eq0rvPgRXii_k0HjWWT-qPkvX-ZmkOfP-haTh34ESzZ_nsB-3yySgV6JrYTs3VMMrwS-w1szhmsPTg8SGvNksIm4WenyH3RFgfzUtdq8vsFv9zc63EnuLn3n7FlZqW8aeUlXT41IpuIu2i57nT7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNvbCxkhbfEIDVnfLESD8Nx6CRlsS8xiFKzhoGi07zO7bUhOONXh4cfLInnBYwWSzIY7wrwLK9ZvOcFWcSmUJ_q2O9mzVGxQk0LWdRxmes7TMQ6b_o0Z0HRwfGjBa2r3BlP8g74NmSnd4MUiT39z5kz4jYf0t3jYxC1J0eLDlO7WYVDS_6SRMBhCAiSsS29wsgbZBqRZ_tGoM9nloUnxUsrhdsiP1BA0cyDtVVfsiTDyu_Py5LLcuAX_QFrf41AWgIaUVyB9Reapczj40S5ald9YAwqEwdHgoNMOoAnl_rN0cKHAAaW3d0E1eh3Z-dc5RmMlSseJIZwKbUhctn95-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
حضور مودریک در تمرینات چلسی بعد از ۲۰ ماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102629" target="_blank">📅 20:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102628">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H96j_aVkt37FP-NoBqs93SoPStVQL9kjOzQ8zULwLufHJSvYqJyqdPFKeijZZmso8Y5Wrt4XKS1Dqkit8TF_d1B2bg8WQnKDUQTgvu87Z9H4F7DDHjXiHijybX6j5EBXA--3Z9_eLOVmfi3btE2emCeGaY6ePk7kR0n9ce_lMttUIWewvxGKTf87sb5EofvL7VblVRxiSOYMVzvRShhZY-7tyq0GmZfuQoDNCM992xLhPVTEJuNiAMKOC5p5rBE0PrZlf3ixPbTDCv4U_mnhsODZjV6f3kj1v19EcSn22DdTsfYWdMlJvt4foRYc_sunr7kaLSYHWqaf9x33sb_5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فران تورس:
در حال حاضر با بارسا قرارداد دارم ولی تو دنیای فوتبال شما هیچوقت نمیدونید چه اتفاقی قراره رخ بده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102628" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102627">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590393501c.mp4?token=bPEjwasCFXPhloaUPshHz2yOL6lOiCqIdodSb7u5iI2SaJcWI59VdjuFQXxFt7R1MXLd_qQwQdOJGXLrCmvtzIse824DoizCmVLVdy3rcRwxiG4AjwVQHpbpLvRnv9wTFelf3E-WfIevIHCqZWKP3BsvO6vdAfcT866MQwsHeBbVKK10ekjN7tqQ9eZBBsKcyo9VLTJtEwkKIX6viMihtI5O7DXwFaEre6YAESS02jAwVJEQCeSXmceA6ngk9b6pqxz9P-j-hQcU5FbusCDBYiNOtr7eyWdGQEI499d5eR_9rVTXzi_9S98tdnZRVgr_Ksrtb82wfZCawsJ5QgwIOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590393501c.mp4?token=bPEjwasCFXPhloaUPshHz2yOL6lOiCqIdodSb7u5iI2SaJcWI59VdjuFQXxFt7R1MXLd_qQwQdOJGXLrCmvtzIse824DoizCmVLVdy3rcRwxiG4AjwVQHpbpLvRnv9wTFelf3E-WfIevIHCqZWKP3BsvO6vdAfcT866MQwsHeBbVKK10ekjN7tqQ9eZBBsKcyo9VLTJtEwkKIX6viMihtI5O7DXwFaEre6YAESS02jAwVJEQCeSXmceA6ngk9b6pqxz9P-j-hQcU5FbusCDBYiNOtr7eyWdGQEI499d5eR_9rVTXzi_9S98tdnZRVgr_Ksrtb82wfZCawsJ5QgwIOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلیچ: علی دایی مردمی هست، من مردمی نیستم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102627" target="_blank">📅 19:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102626">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/sGlW6lFOuI8nEHNbS6Gsxle29JP20Rs3cH7VXvKWh3pNwSvdUtZa7AOWqzZdtGY0r1lVecy86yWnHt7yMRtdFgvF_UbhHOa-URPQ6PJkzW5QYhpU1AWZtjFo6CliS-RW0y88kKbbN0AO2khAmUffekj2nMrNnVI_1WHawY3FSyMJEOAaAuLHu_s93p7AZbE5yohBktwJ3jekVKKiUaXv336tnviSckEcI9QpvEx8wkXfmEOVLBQr1XGPU28qxZQpVw925dPiflrTofLdimfw6Bm6SR5l09_M3k0slWgcgOY3zTp0jdr-E8x8F0Cey9XFDnnZ9X7QvEnTyOdgnvYFHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102626" target="_blank">📅 19:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102625">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcWIrjEzBQGVmATrfeko0b4YY3iQ8iN2oguji9E2h4vemi3rWPaa1EWGX-oDbqAHPEE8EcopNfyMnyndO_XGYkjyg_AqECErpIvQpUyr0PYlTRWsE_AHJtlOxMoKxNxrDwhAxhYoy0dBN_N5pp6E1NNjT4BuCHSAPlwC2JRoWWOlNPckySdPEOtN57aQ4iKPB579IvoUO6J-ODajUIjHd1NViAYSJheHvKP8dU-beeadGEVVsxIX5Y6h2mVaIZWHID0g215lfaW3bC-vzDa4aVvuifsRP5DjOKPbSORoxO46TBZBNzDDA1Psaa0mazafZaYmDNreA2i0yRHCsUTC9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رونمایی رسمی چلسی از جردن هندرسون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102625" target="_blank">📅 19:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102624">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQUwHSUGTyDsB71CX9nej6YPTKVC80YC0ThE-1VFy_9KMlOzpwMIfwTUoAhhZzV7W2BtWpL0YVl3OyKRwMz5kar9whnG_VpbmoXYFOK3f9T61JpYd56bydswVpygMrPdsI6XlIKx4_F-PZfgOUe8J-etyLszIksdfM7637ZkHpexdbgVCxVQK9CBEWGfdOxddnZapDww5fD0mxdA1S4CdMrDYw-MgnpheHp8BtM8QU-9FeN1qy4lMJ40P0_tP3aZqeHiAes73PaQpBhsadydjKmrqw10asTTNR_RmdZB_ezUPeXNFueg8FpsQ7c71WirJ8s3TlnedCXaZeBrgeawEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیاس یایسله به کمپ نیوکاسل رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102624" target="_blank">📅 18:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102623">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16357a3407.mp4?token=fQj3LhQ3wtf7R0tAXJfw3_WwyYV7HnuLpq0tmB9_YWzxyN5PLsqA-dN-Ycju_Ebypz2Q_p7PSniCMOcam-IpTVsXZIIzGEmQEuiyVHl95RZSw1ZWMvQvx5lzYanbLStmUTKRW83QvDMERskCJWOGD4lgpW7Y1ekbbf35JaiPEhrOD-O5_spZet3gzx9cT156ia0x6iPhwrWiM3RckepqwUMrqMAkIZcTQfj_1Xb6LM1k-Up8s5J3uEOd6E5bmWlShajzxOkr9op4sb7drPxXZuO008N9xOQgosiRwSQYq4_0uaOqqZQqy_r8NJ7wqYa4R0qdcH8-szf-C0uhLd-zlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16357a3407.mp4?token=fQj3LhQ3wtf7R0tAXJfw3_WwyYV7HnuLpq0tmB9_YWzxyN5PLsqA-dN-Ycju_Ebypz2Q_p7PSniCMOcam-IpTVsXZIIzGEmQEuiyVHl95RZSw1ZWMvQvx5lzYanbLStmUTKRW83QvDMERskCJWOGD4lgpW7Y1ekbbf35JaiPEhrOD-O5_spZet3gzx9cT156ia0x6iPhwrWiM3RckepqwUMrqMAkIZcTQfj_1Xb6LM1k-Up8s5J3uEOd6E5bmWlShajzxOkr9op4sb7drPxXZuO008N9xOQgosiRwSQYq4_0uaOqqZQqy_r8NJ7wqYa4R0qdcH8-szf-C0uhLd-zlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ویدیویی از شعرخوانی یک جوان بلوچ در باب جنگ که حسابی در ایران ترکونده
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102622" target="_blank">📅 18:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102621">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml94SydZYVzUkz45PzChrRa1GsnRYhKU2Bs4wtW1GmPYCB9s8SQxaMrxPwaCdLOJg14gNh9gySn9ss1j6H0F9RNF14iHDntEm9yMS2ENzD1ibtApafaKaK--tdUiPmL11lC3Oaf4_jokmpgle1L-urQ5jk9h46ai32mNZdyDDTvGYLLekrq8ONlrdZQmKM8pMnfZZJhp79HUL0GTXjWOM04gYHmgKwvMOu3eCU44sOe9Dpx9EoAHRAj6_4vNE3SGNrkiffTHKu2w20TUBtKufmDKqDY65maL9sjqUx_v8a155sSVPpA5Wei9Knk5sazBmHLLhv1TfTb58H9hmugxiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102621" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102620">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzqzqebZ-dAMMORpgGBEx-CgiYUoDAK_jxySfm_GijCN5fffwCVGLMBTuZYURmrcDnClreoObmozwW3J2k97PcBRqviBYCvlD618FRPKIoDCqor29lJydxtaDG8ThL-yolxI2KKziM1SKgk_sBviSjA2jzjGj7uisJyGOED9sjtSuprNTYoVaXZ8AZ-1SzPOPOdu0IN56aZ_wKkkIrQZVcaTshRK-lqKJjq8a3pOjIu0Ih5KQj_zrSlMayzTBLaIDAP-_dkG9z-y4DjOwwwpV167v9bt8az2z92ejRaIzh_NwEbdQzg2lXBLI6HJZRLtfZhNQpCAAsYimgK-8WciOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKBfT2sem6tpPP-R0kLW5WEFzxWHhqwyIONHG5PfKEzd10TzMkBJmqCClf42MlM1mL9rLqSCyte6yqcL0yX_II9NR5l9iK5M-geuwgtPB1Yo8gnOl1GYXUEBtxBI5EClUld6tmNqm3WFmsNAU9yZEvYe3ZZdOoXv6IpqNnRaP0LhodI-4F5aD8ajtvqys-eKr7Bbo1H4rCwpo12ibpHKMj0R8Xydjyk1-kJ64AkszBTJZdY0tSqk7C_n83qRwDXhcl5wCLFv2fqRT-0FHvMqNRUODdpkMUSs0XDkn59oKtKxCpFmq6s1ATpZHKmn5WVZ_W6UI9hX24pkMH5ycRYW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پوچتینو تا پایان سال 2030 با تیم ملی آمریکا تمدید کرد و به کار خودش ادامه میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102619" target="_blank">📅 16:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102618">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سیوهای تاریخی گلر‌ها در دهه اخیر؛ پشماممم حقیقتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102618" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102617">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEHte9UL5aKjLAQfzfteGX7ePKf4qYwLx5cNHkob_VRS9FaXwGGY1fqtkiBjk1BeCkHD5JJ4QTooUal6QvKfimUyw6I7CF747fVvpDYAJXxsF2AXplw1-RJNAWMQc3LBqXdlqaLh_36zDmIz_gH44zgrdkHvab57lBxyMz6jKOhTCZU7zCIO5ITu0lGwkh83z2WrQzEd4uHspEghB9diD1qmY92ZkxWk561Ns1jUHgnX4zwn-9lzgg7EXw2Y3dhPo9UH8EimFPfH0KhDIuIdSB0y6jMoaP_Wp5pe-oSxAUZj3P0-omDP2B92ZvIyCsDZz1knQUQHyR1SoqSDOmp7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیماریا:
بنظرم مسی تا هر وقت بخواد میتونه فوتبال بازی کنه، اون تو 39 سالگی نشون داد یکی از بهترین هاست و هیچ محدودیتی براش وجود نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102617" target="_blank">📅 16:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102616">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=X8lr0b2NIhrH6L1dJ4f7HsksNm_80lBxOZ89h11o5_VArd0V0BSJ35Vwk6fFTMvgPdNYTwHVWGjWLIDOByPneKpUx8H2vnasK0gK_-f0TSCeO4j10LRg5WiNROzp4Fl4DOzr3sTZ3g_YjkUY-xflB3Aorj_YLKI69gn6Cjc1balZBwkdrRFgYjDwr9Mk94nx8-lafGEqBLGu08dVboMIC8g1FY115IJ_IK1paqgGGBX504bxzApJbhho8Y5mWJ7CX-eYwrGPjaNRWP6VhvMB-vJI-oW1RQpPXlP4RocJ7ePDvhF6S_nVa9cYlA3j3VtlJAvqEUhSeUxBl8_lXC92vIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=X8lr0b2NIhrH6L1dJ4f7HsksNm_80lBxOZ89h11o5_VArd0V0BSJ35Vwk6fFTMvgPdNYTwHVWGjWLIDOByPneKpUx8H2vnasK0gK_-f0TSCeO4j10LRg5WiNROzp4Fl4DOzr3sTZ3g_YjkUY-xflB3Aorj_YLKI69gn6Cjc1balZBwkdrRFgYjDwr9Mk94nx8-lafGEqBLGu08dVboMIC8g1FY115IJ_IK1paqgGGBX504bxzApJbhho8Y5mWJ7CX-eYwrGPjaNRWP6VhvMB-vJI-oW1RQpPXlP4RocJ7ePDvhF6S_nVa9cYlA3j3VtlJAvqEUhSeUxBl8_lXC92vIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
بعد اینکه رونالدو و جورجینا با هم ازدواج کردن، ملت شروع کردن به ساخت مراسم عروسی با هوش مصنوعی ؛ از حق نگذریم این یکی خوب درومده
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102616" target="_blank">📅 15:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102615">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=ZjflSytn0HPccR3alKORrGSp_x8LHyVplh439leGigIunhf9DvAUSnH6xry6nb2tc4L2i8s9vxUv6JmIxmm3dSIXoWmyhnl3OXA0dzbWCs2lip89eT6MaeKzgAKwPXxQdfqYR6RfACi-o3uWISjHKweA-9mKCQ3Npsn7KU-5B53w_KGyWYuJ8U9f3XljG37kYiN-2FDyOOCcPv2fxhgkXRleqxmgWA7_eX2x83GOSg2a3C0MB79NhKHG3JXlzYwZwNHNosKBSxJYdqQBp63jrqjNkjmrYk2iqhcKIxUDQRBCMeauIr9WsiZgc_MJbWpJdbduZle5bvwfLMYmcr9WYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=ZjflSytn0HPccR3alKORrGSp_x8LHyVplh439leGigIunhf9DvAUSnH6xry6nb2tc4L2i8s9vxUv6JmIxmm3dSIXoWmyhnl3OXA0dzbWCs2lip89eT6MaeKzgAKwPXxQdfqYR6RfACi-o3uWISjHKweA-9mKCQ3Npsn7KU-5B53w_KGyWYuJ8U9f3XljG37kYiN-2FDyOOCcPv2fxhgkXRleqxmgWA7_eX2x83GOSg2a3C0MB79NhKHG3JXlzYwZwNHNosKBSxJYdqQBp63jrqjNkjmrYk2iqhcKIxUDQRBCMeauIr9WsiZgc_MJbWpJdbduZle5bvwfLMYmcr9WYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=iobg3tcTsAI6g47M-FMDb8pvBZ_dy-VuP78CTPpzXr7bTYpdtUC1wjmL7ATiq9o4JkXHsdWm8Vii98noGxR8TAI6wPRdzGGZRKtXoUCgAQGncLyNANniAsJ32F24qkwSsXx553K6sWOYjz5H9djy5f7f0TZqYZi74Kh6Mo1BW7HmhXwW3rq9QNznUj_axyQViXU7UW5PF6ZL54KdHZ6MLHrwNYSZemRHS1u4NS8s2q_hwT6OU0xLZeAXM6HVJlYPso49nKoIIpDC6WqUGpZivRK-02gf0lJtA4Rgg6tRjPGiRkc_mMnb5-DNLZaZ0f0BhqRJfwZyEz-uFHJVoxldDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=iobg3tcTsAI6g47M-FMDb8pvBZ_dy-VuP78CTPpzXr7bTYpdtUC1wjmL7ATiq9o4JkXHsdWm8Vii98noGxR8TAI6wPRdzGGZRKtXoUCgAQGncLyNANniAsJ32F24qkwSsXx553K6sWOYjz5H9djy5f7f0TZqYZi74Kh6Mo1BW7HmhXwW3rq9QNznUj_axyQViXU7UW5PF6ZL54KdHZ6MLHrwNYSZemRHS1u4NS8s2q_hwT6OU0xLZeAXM6HVJlYPso49nKoIIpDC6WqUGpZivRK-02gf0lJtA4Rgg6tRjPGiRkc_mMnb5-DNLZaZ0f0BhqRJfwZyEz-uFHJVoxldDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خولیان آلوارز همچنان در رویای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102614" target="_blank">📅 15:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102613">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AW_B4jR-8R-g9TI0M1adJQMdWQWX7jkW7tQhuQE5sPmhCfC1dnGGrxCT-88xTboVvv1x2ub0VH8GkE2YYB32TrrjamyTzMgfyDkiXppNAPa6qyOAxz1wda3o_TJN3K_w1TNLQ6Nvk_6VqokuaHbOXnYl58C349_YN35QVVmpquKoqEg0V5PBW9XUlR0vGf5suFern4yaTfHLngsfA01SM_s-8wF9vZx6ukiEBpRjr7n-gh1h2rGjKwCSy06ccBTSNA9jhtEOkwEvTfgMePSQmos7R-DiZoobky3ZQNfUhZpBFvItZIH6MxR61nEX2QParx3BuV3p_vyIXPFymPmaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
استقبال هوادارای کولو کولو از ووزینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102613" target="_blank">📅 14:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102612">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYd8_Sj1NXe0tldawuH_MkRVMZQF1GMmpok7kZeFJlbfcYidBLdT4r0WD_jiPyTXJ2jf0JtzUjHdeTmUqbrvFE3_Z_XKU_42CpvXSNrTih4u7m_6LaDoEgMyQ90WPF8TYmYSgxLix0Ahgi8b-TaNG4qz32-fJxeUvskSl1OpVxHJ6JhU6aiCnjLrtmop0XqemXj2XA8ubQUOmM34WePsxaN4Gxo6b59WtXQ2SZQXK1KiedF43eowbgiVrllvN807PfpaUFVOwS94Ma2QJPlsIcuRO_5vHEwJTQHKN8UaT5UlY49fKdaWS-Ok2AUzB5sm_-GMrOAsoJHknzZzqTFZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
مودریک رسید به هنگ کنگ تا تو تمرینات چلسی برای فصل جدید شرکت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102612" target="_blank">📅 14:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102610">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i0XDLNwOOwqFPIpUOQ7S1c0h7waa__Oip8f4DNL03bc-aECWMox-ASg16huMPnM2jGHGx6pF7btNvGatpgP3YPzYSQ1UOZbBn7hN_c9j8RikimnXMduBST6uGPHrktFfebgriYdm2amlLgMKXVAzz6NTJOorJa2g7qbUnsUGW-X01B4UTG6roPsxTcTKHGgDCHzN5FCltmHS3t0yc2rODI945hjNxH9z5M5QnvjA8VT2nnB2sX2q2kx0CZ88RLYXQ3hXw-nlMdf6fuVwbSY_PMcvYZsV2it0o_n6oQ9SMQgdpC6CxyWhgZ44qX0q1kEO9onzpppc4YN-ChsjgXB1eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRaCud8ND0KJ16Qt3UwCBj0P8Gjf5YiJXrST613e20Yx8glZHRAULA2r4XJ2JA3I8_sBRaol010fGqSxnyu-nE3KvCkW592OH4j0Av6XdXAXqSgvzForIWnyl16X2JGUyiFrM_07oT-xYEJAzOqWn972LXkWiNm99IO2UqJC9jLIhDjMgCDfsP1FlfA0EnXWXDbXSMXzXa7Gqv0tQQwjJ70Izn0JEJ_yE6nmk5jd_Qfxuxsn-l2FfcdZHR4z8SUnh7kR23ZZqwncp59fYODc7JkVKvgKcF3Cb-BWyJjYr_grrfR4QOprEeUk2n2q4ccMuInNBiuMkWpZS2BsFO3oMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینا کامنتای زیر پست بنز و پورشه نیست؛ کامنتا برای خرید پلی استیشنه‌
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102610" target="_blank">📅 13:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102609">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=b7qIesBcUTRnzOoZ1w_7hfaBVDDOBWRepk41X_8Q3TbwWykCZCtrRdeKhd03xRFZqDPHyqJixJQfCHXWFwY4pkTnzmEQXefs2gVjluikpqYWihdr7jmRFgd4FGUNyI38Posu-3T4e_5SvvXecRY_J0bcG_Cte1jMsj1GCBZ5yjPPHNXK4SSdnKvZaadobcFxvTCOeNX_2urmhYO5C5pgowiFR9tH74B3fkw472rb0PuBOPLLtJxqhTPDaZxH7CQjCXPiqMVwW_qfcs3b4AcR7qkkT412DTsnvTIFeKYVGBbWebVC7nas3wvo7D9N-BkaXXxN0Fp_ixwhfWalawmHbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=b7qIesBcUTRnzOoZ1w_7hfaBVDDOBWRepk41X_8Q3TbwWykCZCtrRdeKhd03xRFZqDPHyqJixJQfCHXWFwY4pkTnzmEQXefs2gVjluikpqYWihdr7jmRFgd4FGUNyI38Posu-3T4e_5SvvXecRY_J0bcG_Cte1jMsj1GCBZ5yjPPHNXK4SSdnKvZaadobcFxvTCOeNX_2urmhYO5C5pgowiFR9tH74B3fkw472rb0PuBOPLLtJxqhTPDaZxH7CQjCXPiqMVwW_qfcs3b4AcR7qkkT412DTsnvTIFeKYVGBbWebVC7nas3wvo7D9N-BkaXXxN0Fp_ixwhfWalawmHbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد ریدمان دومفریس در بازی اول با رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102609" target="_blank">📅 13:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102608">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXyAWU6PvCouNlJN1YJ8rNKQcrn1Xuq5B4HrUDzMOZRGyYo900Xvks0odvIEd34ryXebH3OIPLzpx-oxDEbBp6LMIXmFXBGEoUBwxe8flQ9hWO9KFdTqw0WZEJ_6uwo_YMlMIcHefcBZd0OdJRxMUNl1eCNJS4H-YW1xXW9QqOCnJviMpVF2ab1EHf6PBUEPz5ZMnjWJ6eN7Rz1ZvJ2MXQ7r4I9r--mtyejOLU9uULz0LyAR-6jqly4DYbuvlVpPQa6tBX_PEdGtbXSWY_FwAPl9cZ9s5z8vRnJgzIac8ujFjxfnBdMLBr_WMyh2NhomOEGH8kvRFXbRVG2EyASgmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس بعد از کلی خوشگذرونی تو تستهای پزشکی رئال شرکت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102608" target="_blank">📅 12:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102607">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=XNG_e9AXPo6y0xZN6Ug_2FNUdSImmFe-Am94AxTmUyC-gDK5pNkCkKDWPTWT3hzjNKND9dFvI_-PFVL_N6H76O4L6loKJR7xaoB2uhpewSZH7p_3TPOByz_Zdq6spVDE6kpWYtilnHEqRa6RO3SMX4_2xLIkoklfrUsSRnWiP6VOXPWJFvGKdJaZO0nznrxiS9KVgF-_pUurN62v-hinD9QaxjbTxe29xsM5a2_wtXTWF7KtqOpUg4QGqJWTlzJ1DZz_SRJD7NwfLx_i022DuUCF9BZOHkesqA1BQLMkIAfaKcGNgkNF7B6sD6INENWP_YcxT6Loj-ihVuhTIlAsHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=XNG_e9AXPo6y0xZN6Ug_2FNUdSImmFe-Am94AxTmUyC-gDK5pNkCkKDWPTWT3hzjNKND9dFvI_-PFVL_N6H76O4L6loKJR7xaoB2uhpewSZH7p_3TPOByz_Zdq6spVDE6kpWYtilnHEqRa6RO3SMX4_2xLIkoklfrUsSRnWiP6VOXPWJFvGKdJaZO0nznrxiS9KVgF-_pUurN62v-hinD9QaxjbTxe29xsM5a2_wtXTWF7KtqOpUg4QGqJWTlzJ1DZz_SRJD7NwfLx_i022DuUCF9BZOHkesqA1BQLMkIAfaKcGNgkNF7B6sD6INENWP_YcxT6Loj-ihVuhTIlAsHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
انتقادات شدید و عجیب وحید قلیچ: چرا تارتار منو دستیار خودش نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102607" target="_blank">📅 12:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102606">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWkRrnnjX8uylYuyD4dC6AwbLl8wYimECoa_AIzd3IjHp05thkWWeMyiuiB5qMUxmhzpdB_4qyVwvc-KSUVLiu7NrNSIBukEpqkWb7GD0UAOcu6EUXLb_CmpW3DQWIrrFBaEB7p_d511TwG3MU6oNj-mL_NTDSGqGpXhdxGRgWTv5LOdMMVveRu4QFJFdQ2LSULTDURTfnkiQD8dNKW-1YDNtGkN9AEddWn8nxxvcqi_EuHQzOtPM5hn4zmc00XkpZsXiV4QZf_JI72qz0z6ml4EnVhZhGR8r6Gogu7ZIw_x61_SbDlNJ50x3HrM_VP8KEGI12kdQHgG7X6Hnx0gWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⭕️
باشگاه‌استقلال اعلام کرد که فیفا در نامه‌ای تاکید کرده که یاسر‌آسانی فسخ قرارداد خود را در پرتال فیفا ثبت‌نکرده و این بازیکن مشکلی برای همراهی استقلال در فصل‌جدید ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102606" target="_blank">📅 12:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102605">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=GOOTW0yqKs3-4jfdNGR8JDaGtu5PyG2M3QcGQRWCqu__UrOVeM7HASPGJuU7kitGm_t8SPQPL6iJQTtwp-lIEb2DIFLq-BDtfntAjcs1py6C0Wo9Ht__k66elGcRNNgdopI_ca6ZBcR7w8mvOzLLQ6e-bO5M_-gw1m7vXSwh0_yAavlKR9_NPTuWxat20UBOOr9QOuGRgjXWuPigXCSiS-T_Wop0FyhdO86sjmcm9cJnlT65NtGJWJty9zeODYJfCCG57QJX0VqYOz3gpjaEpzUqpi_mcvTCToUVDeNOq0BWZcDCHYRlrCtvcfHuxIMZNHObd7wp69VZv8_rz7SUDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=GOOTW0yqKs3-4jfdNGR8JDaGtu5PyG2M3QcGQRWCqu__UrOVeM7HASPGJuU7kitGm_t8SPQPL6iJQTtwp-lIEb2DIFLq-BDtfntAjcs1py6C0Wo9Ht__k66elGcRNNgdopI_ca6ZBcR7w8mvOzLLQ6e-bO5M_-gw1m7vXSwh0_yAavlKR9_NPTuWxat20UBOOr9QOuGRgjXWuPigXCSiS-T_Wop0FyhdO86sjmcm9cJnlT65NtGJWJty9zeODYJfCCG57QJX0VqYOz3gpjaEpzUqpi_mcvTCToUVDeNOq0BWZcDCHYRlrCtvcfHuxIMZNHObd7wp69VZv8_rz7SUDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این عالیه از دستش ندید
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102605" target="_blank">📅 12:25 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
