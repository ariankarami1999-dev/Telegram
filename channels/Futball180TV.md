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
<img src="https://cdn5.telesco.pe/file/gNNVh2833jllNBAAH0LtGceiQcALpzka1QtHFEjyV2-vEJydTmamlHEyCM4cWvCzGzfPZROuz29eXgqDhzrBDAt_EeGVWUFJ8Za8-uBiExI8_oaAaS-DnjZaOIzumN-DCI8oi03mS2fymuFA_itAzKqDNGDXc_gqKbPNJ97heZ03tq4NhSQeSIbiTVDDfY5zFnA0rCiu1rxZWfvx4R58G-ntJbB02j5ev6sxDuG4UWiOAGa14KOcQ_U6cd5ywP5eugl11OuUwU-1Gou5u1SU1lMuids4XdZz5x1tlNWe9XIVGe72ueAJz3MotP7TDt1YyIjtK3o6D3hrIgu5Mr0OiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 520K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 09:56:35</div>
<hr>

<div class="tg-post" id="msg-92856">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLiKem_Re2e3xpOso6LSHjq0YyundC76WTniucoXZTkw2NeD31sYTdeBkCiJgen5TNcORZBu8l8i0BRdr3MSTIqCZEgbt2-w5kEEJVY2s1kj3KDtmALIz1oH6-Cahq1-MdVmC04tt2xPHgrtIOkOz-ApuswE4F_Slv58ZkZUCc4fNEfjYiDRw9thODArs95X603kpq-SurX-xcZmNU1jN3gpRPIU-t1MbdjWhP_0xlYPdPnAwJzwYf2i3DJDypZdl4J7XeU5-DafHICr4oWgYQ1eUPRCcVKlmPrLLYZjDtd4y6M09yfcZTj6zI4p7_tBx_dO5fg-AAuPciZLE30Lxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|تیم‌های آسیایی به دومین برد خود در این جام رسیدند، ترکیه بعد از 8 بازی شکست ناپذیری بالاخره باخت
🇦🇺
استرالیا 2 -
🇹🇷
ترکیه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/Futball180TV/92856" target="_blank">📅 09:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92854">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohI8Y4t75G4PMepFWY8gvIwCt5-pqWmYmg13el9BhfbyElAFsJpxOEwjuO8uSYHqhpw0PQX8sZoANvKlxr6F0RMxFIUiOjt63RYKRyLtaj1WJ93wUzh-ZoAiHA1w77oPjOKT7-cMSHwSzAu11fDYY7gW5Qu324xy7rC-xoywj4xHWoyJB08t1bngGNxfopCUFTQ6qgFnWsKEvUrKdrXXVFgeNgWbu29S67cAXiXmHDmm9TLbIN_PXjZLIGQtZgjUw_zR7xKoJX9Uy2VekhugDILG2QjPpmI0eqxF1DPmvy_0M5afYsuk8BknW5SvcO4O8ND_hAn5fmV3qycn3jefrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رومانو:
روبن آموریم آماده پذیرش تمامی شرایط میلان برای هدایت این تیم است و تنها منتظر چراغ سبز مدیریت است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/92854" target="_blank">📅 09:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92853">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzaCo0AEswec8wNvmpsGkeqi4ufXyrfB2uS_OoMTX1TzgzAk7-vuuHJ85e5nJnL-XUvEXHuzR3_90VZFfL-Ym87xd3oOTdi1QTnq2R6aSjOHzgUZuPUhfQAQOokP-6l98bduQY9uUJlTxreOfTdxxPUqxgoRLaevmYfokqF7lviif45rjgBDHp1xeCeyTBFKziL_ODO5rp18mZqYLkIu2j9_QVyU5XI6zXqF0UJ0yL2Yhlqw5RN0GmABbUh54FYrxpxs9O7g7-LL6dXrS49kbDHE9ip1_9uGv4tvnm6hkxhHgGYfwoMomAqiRYGe_DZbv0BZ0wc0T_vJCw0f-ZIkIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین تعداد پیروزی تیم‌های آسیایی در جام جهانی:
۸ پیروزی —
🇰🇷
کره جنوبی
۷ پیروزی —
🇯🇵
ژاپن
۵ پیروزی —
🇦🇺
استرالیا
۴ پیروزی —
🇸🇦
عربستان سعودی
۳ پیروزی —
🇮🇷
ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/92853" target="_blank">📅 09:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92852">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKw1y6P4rmXuqZSOnYjfsQ6LdlsU0YEqjPdhiqOyOOezRQfdApu_bvf8abXUE83XHI_hgQleA6jhrzJXAAIiCukSiteh0fX-WrOj9aGeF0Co4u7w_bnt8qlZ0qxSvc5rl5NRaPrGLl-N04cbcSr-dBOkGEVtw5Z1DxYndeIRWH6BkTgfiYAVokGqdwyOukb5h5DN4NCy_ycIPhCflR24CgNfQIvW26GMkZe-gPkjaSeRktQ2RgFLxYS72uzQkj8voRzng2vH7ZmwlJafowvzEfIzrp8EbGtUJZ27bugprbJGu07SgLJLCyB1lZzudP_D9qesquBu-beOsEVFJwTNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پاتریک بیچ گلر استرالیا تو بازی امروز با 8 سیو بهترین بازیکن تیمش بود
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/92852" target="_blank">📅 09:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92851">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgbKJaGOQqVy9lpSUBMh916NnXUMdHYRCtGhE7f4i9ErcYRsM_sF9z6CzqeONzbp5Uvrcqay98oFD2XrKbGJ2x3lTCNqo0ve2krb7O8QOEEMeIWD87bOU7nMTR_25PEe6OiV3-2ek0EAOOYdW_TpgYMgJHZZgxbLyCH-Ya3jbN_Ch3x0tBayTxeN3VCxLsA1Edc1Xxcf6_RATs6A1G3gwwTqu5KHEKqae4CJWxH3Z2K1LUn8EQChU9mhp-4mQ5F0bJvRm2g1Ix9gqMn8DSTI2_YSWCXhHeR2KGUriHEomJ9FQHhE5lRIG3jIAZVf5h9eO7kyAlKo_jWsLOzFLEuCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه D جام‌جهانی پس از پایان هفته اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/92851" target="_blank">📅 09:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92850">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frVC3GNbpFmBWMrl6nLvdOkyG2ZIk21C9ulaStyy5u3t9G_xW_93JQ9lLrkH4aToXHKPNli3HUuwdwX8ctfdyC6SobJf0Je1rZRl9lhD_8zfRWwL5zhWnRWaLhzZ_eaZHukvonfwj9m-J9yhDe31t00ELGnNdogF7MxDCqAitOv2h5poqGhGkuOZH183AkADmZYL_uTZaeCErbjEXFXfuoQ3OFswpeTFlYofn5pILX0eZoKV-0DpW7QUBrxh_AlHH63tuVX1nWtUqcjzovubr94eLh1_7SZ6WDJ5Hu7gTiHTL_OVO1V4vFX2Naf4BlFEQ6hd1c0WYpS-oCR3ISA5hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|تیم‌های آسیایی به دومین برد خود در این جام رسیدند، ترکیه بعد از 8 بازی شکست ناپذیری بالاخره باخت
🇦🇺
استرالیا 2 -
🇹🇷
ترکیه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/Futball180TV/92850" target="_blank">📅 09:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92844">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7kEu28YwfrZXY4BIqy4npoDYP8aUBqND4sp73BktMQ2rl1dbhusciIy8oOvrr3YicEzcO1hlnJXJ3fyfh4qKyOgTnIX-lgUl6uVI6eQLAs2r8X6AyabCzXpPAZjYLugm3jeJDk_1hA0nrIBDjYmEu5PJCNLc-wR_XQOu_5FIZFvVOBOJWbir2QaW66XC7GcU8sAiOnakB7L3zite45MgBvzQmwSP8Vh6bdlVST9Ve6EI_KAw3RmdqTtOTBb6pyj9txPgIFklXS6OjaRwIiA_k76TxOiq-0TQ4DDtfd511FCULUE2npDVZGPe8sr0JNjyAOpgGLBv0RkPJZ2nIXuTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIwpyLNVxjDesfdnL_jSLpW-2DdwHInrs55qT84BOfpPfipKca83T4SWorSR1Bs9swidDbnzOAGwEVbllFhVUr9s_cWgd_kdM86Vt4N4FIOLItm1RfkgPWJPUxmNjscb6DSraOfH4ONolz_5TBAsKJiitKmYzVph9QKd_IDWyt3EhTjFroEQn2rRd0Un-62zPT0sC9HgnoDUdHxL4qxp8oZmctDdOz9r7dfCwiI7NEXy0UD8kj0Gvc6hs_n5QMjYjDucazi1xhxr5HpV7pnR3DZQcTzXppmLyRDZhpSfoaFYHVZnokPPbirVPFjflfKcGRx3KIAav2spP8i9Rh2JRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eO-fdgxjE9CPTyx1CXUEmGhOm0CXUhTGytgq8goldn07kPufzSjjskuvQwHJ7oHY14MBde8VNvVB1Rik03rC03L-Ywfgs_zphU3118Am7E07O9lUOqJMR_0BthlxmrdjgPV8xt3xjVYI7ep37-VJUZMNhh3nt6JNSSesZpehjGm3c75M5r6ttGY63iGU8BQ3r53RMW2KZ--LkxLgJ1COo-pTUhPrQY_VUH8qeQL8AVQKXBPLS7I8TrWfTWWHkJwbUOmdi23CTZWpSDSj9UGpiijsalKD_ZsWRRNA4FZ-fTGBNTAHAGkymyRodl7Jr1bb-ea9h4eZDajOuyVTD6atgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZuBNez2VEt7Ig8EoC3MXYR6DNUyekI8Vy-ftduHTyFv7k0L4Ki8su6SJlA2hCVxAzbMH_HSVIJEorPam9Peni3f4HIAM6KvIkWS1zmqtVBqBoa7gqsQ3U-8YBLxpdDSNCzwqLlpdlV3qoEjayZl7dbLrVKTdXHS-fkAJa2Ds9h7fY1TvZfHa9eQmQLcivNMJynxrWr-JWzq9KmpUHaWOUrgdM25qT8XQEQRBGPDWeDOnHBmGrnVAmVpASsyyxZnoDdPEg-dNHNDXKnY8zYjPkheyJzt1XCPwCLZ8ShPIxdHE_jXdrqOKitdP-2caq5IWPiEPtQ6c4NRzoKJwFyjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uk81fqV-tY0q7osEalQPGayScPxtB0y0HSDOsWMlMTM3IzajDhkK7r96GUD5_9Q94CYLGfLyCH5_90YZOIBVVui6bolET7u9v9lHRbiBiPAGzYUHXdzhKAQugtf5IDpQf0pVPEwEVthNb7AQR4OuiIPIpAXlLbOkacfcbjzndjywvVV5C9jmQQ9qnBqZg5mt5hSiQvbhL01LpgVkpp2tDumv7MH7L2lFpaboZDUiL5lmt-t5ClKTKRQ0peb7xGAYNZhtNp8Lu2ruOrPL5-zFKQErhQ9zyi6dRVxkYS1uktF-mceprkuOxduVmZ9qbmcbaq-AEAD_sqzcs75YOTORzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzQ2onVLo3tZHK7ZiVSoES7CYlAeRMu_KThDouAd0VlzyEERPYlCpNjaLzZKdrg5g73wa1CT-duul1zFuIxB2_21_-XUmKR_1mzffDdhod31Zdw45M0iNU5DdwxIYo-cyxFyqZvfTpGv8PpnJdyAWxA_Q5VogPc1fa2TJOfKKC9veGMw2gHC0ffatRKtI_SYYsMIQU9X9Yn1pJHWNwZPYgSV_iH2ADsP4d96X60IJHC2xaqyNWh8y5H5DyT4qU2W_5nIA3x135QKHWfzPR2qnUPX4zh63zlgipQULj7t4nNpTYyIKpH0euJeU3v6dWHbDko-pe4MQ-P8aS9NLeiEng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
استایل جذاب همسران برخی از ستاره‌های برزیل به مناسبت جام‌جهانی
💚
💛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/Futball180TV/92844" target="_blank">📅 09:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92843">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دفاع تیمی استرالیا واقعا شاهکاره</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/Futball180TV/92843" target="_blank">📅 09:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92842">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6857d54a.mp4?token=AAB-FU8zs5OeqB0JH6ym6tUcIEHO_ggkgPoDC1AQrbHvhrY9WE_r_UVXOB6EicxOagxNgXAr4j9s0QpRRzVvkvqE2Zz_Olrj3bQMw1xmGQ-mAPCrPOz0J73om5z1D0z5EZz7-pOGku_G0XNac6k1vnVHn7d3F8x6NZHlI0pyY1YVXBFfOm4SeWhP_VYMZlo01ngM5iO-0v4V8eVuJ3DKlHH10j0mRgMp2BavxCzd5BVr6imQN3-XF-g5_AKoOOULPbbftDn5lykSoi-9g0HjdONmkBw66F0v_0TYQctrrBrP-_xq02a9xOVsIcQi7pZMeRU6btw8ZBzLAEsD20_lrC8n3Fy_1e6L41hJYqYE7Wq0gw7NZeeV20ZcnO_VGaUd2KP4UcbV1BNevUFzIbg_S8oK4dlR2seD3X35gGgI8N0L1AMgdI2qsycom4w_IL5ifhDAnzShO1V8efIA8stHOo-UbAPIjRrjVZz0RJCYOzgq7509VrLaLWCgxcFsV6Uo2JvCJpFwcqh8Tf2803KZYJco_Iqjs6Ounk_1CEDNZ08AxwkE0uGH8_8itDdWiwj-8ZgbdWDCaSJ1soM51Ym0BLJkkIwoHXrybsderQ0mfCboMOui6WMuImCjHnrEj7m_8qpAAiIoIKO6sPNxe3PKAW6rbaSz1POx-BPBpDDmk-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6857d54a.mp4?token=AAB-FU8zs5OeqB0JH6ym6tUcIEHO_ggkgPoDC1AQrbHvhrY9WE_r_UVXOB6EicxOagxNgXAr4j9s0QpRRzVvkvqE2Zz_Olrj3bQMw1xmGQ-mAPCrPOz0J73om5z1D0z5EZz7-pOGku_G0XNac6k1vnVHn7d3F8x6NZHlI0pyY1YVXBFfOm4SeWhP_VYMZlo01ngM5iO-0v4V8eVuJ3DKlHH10j0mRgMp2BavxCzd5BVr6imQN3-XF-g5_AKoOOULPbbftDn5lykSoi-9g0HjdONmkBw66F0v_0TYQctrrBrP-_xq02a9xOVsIcQi7pZMeRU6btw8ZBzLAEsD20_lrC8n3Fy_1e6L41hJYqYE7Wq0gw7NZeeV20ZcnO_VGaUd2KP4UcbV1BNevUFzIbg_S8oK4dlR2seD3X35gGgI8N0L1AMgdI2qsycom4w_IL5ifhDAnzShO1V8efIA8stHOo-UbAPIjRrjVZz0RJCYOzgq7509VrLaLWCgxcFsV6Uo2JvCJpFwcqh8Tf2803KZYJco_Iqjs6Ounk_1CEDNZ08AxwkE0uGH8_8itDdWiwj-8ZgbdWDCaSJ1soM51Ym0BLJkkIwoHXrybsderQ0mfCboMOui6WMuImCjHnrEj7m_8qpAAiIoIKO6sPNxe3PKAW6rbaSz1POx-BPBpDDmk-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇺
گل دوم استرالیا به ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/Futball180TV/92842" target="_blank">📅 09:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92841">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پشمام استرالیا دومی هم زد</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/Futball180TV/92841" target="_blank">📅 09:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92840">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
پشماتون بریزه؛ یه پسره ۳۰ ساله تو یمن که بهش میگفتن مرد عنکبوتی و شهرت خاصی تو صخره نوردی بدون تجهیزات ایمنی داشت، چند روز‌ پیش موقع انجام کسخل بازیاش تو دهانه یه آتشفشان اینجوری سقوط کرد و بعد حدود ۳ روز تونستن جنازه‌ تیکه‌پارش رو از اعماق آتشفشان بیرون بیارن
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/Futball180TV/92840" target="_blank">📅 09:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92839">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">استرالیا عجب اتوبوسی چیده</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/Futball180TV/92839" target="_blank">📅 08:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92837">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWDKehOBvV6AMqRhrrag78R_qa0JXfF9JQkL2TdKBtGx_PE0SgA8K2tzRiqLVvs5ov_kl3QF5SPhccBSUSrrXH_67lPglouXEBM-f1W-9PmnKiVQjb-FfouSDaRhad4JbwjwteRIC1gTNS-UYxWQbKg0DU3RvSSMYrlkNjd3EyfHAmppTfH-WalTKCd6niclNWv0B8kAZfa_pzYrS-oIEDHsorjh5XabjfIYpu73GtzAyr5New2X1KGbgl8gVc0Bvc7wml_rYHIanrs-Cpe5sBAFdLeD_7UkQxXYLz7tVOIIzEqNzXSDe9sTQQr_kmPzYz5RIqnyra4-uyHGHVPoPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه ای جالب از بازی ترکیه و استرالیا:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92837" target="_blank">📅 08:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92836">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترکیه تو نیمه دوم فشار آورده تا گل مساوی رو بزنه</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/92836" target="_blank">📅 08:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92834">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شروع نیمه دوم</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92834" target="_blank">📅 08:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92833">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwdTvqEQIi1z7pcbXrd8QSZKco-Nr-hl9eBnlJzL-mbi0Whl-gUPA0kjh0v1mSazn_tPR8rlaUDUwnL9GuEa_rcO7o_gJUU08M8NbEZPocDiTUQqSY6aPchy9RWExQEYJziTRhvu-ZLWnFSoeC83OpxLTNL7af_-OOaH6r6y_d0164RgS2OwyFsY4OOaDeLrS-kYxuv-e7jRrkVEnUMc7y8MYLCO4nmTgWW6KyAOzXvaPVqLvL4wChu9vYriHF-gcRPw8N2QcJnhnlg0svZTsaHjmZMGXCjCGSn_LDfslusNpmT1xe2NdJDrSAe38M0yq7Y72gnNOqE3Afvpp605wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نستوری ایرانکوندا با 20 سال و 4 ماه به جوان ترین گلزن تاریخ جام جهانی برای یک تیم آسیایی تبدیل شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/92833" target="_blank">📅 08:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92832">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پایان نیمه اول
🇦🇺
استرالیا 1 -
🇹🇷
ترکیه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92832" target="_blank">📅 08:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92831">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEansV1xBFivaht1xi-AWbU3CR4PR6EuWDt1ADprsajsE0nFqv8Miz0y8OV1zJ8vlze6Q6HIMXTbppJLGTvrPkBbRvOR3cCah5o7Tb4gtuevcTUhu7FuxBMbJ4TwDLlNK0yW6rSm3y7_whS_0IbSLEv9vaGAIdHDwGHRPqYf00MR47RNyWijgKFQUecg6zzeCicy5NcUXYrM158wkWc0RIHsYMntI9uiKIqg8az2IFL_QTojpM5ZPo6703g2-qP61zs3g_dKHq5Ql81n9pF7iBqG2_eRBI6IWcHEpLJO0Ke_A-FDvrCOSn5It8VIZnkQ4w7I6QCdWQZm-R0L_BkAXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇺
خوشحالی ایرانکوندا به سبک تیم کیهیل اسطوره استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/92831" target="_blank">📅 08:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92830">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29527446d1.mp4?token=HFRJwGMagOG53OYiodAHqhBjkd-Dm9mTLTVNUQwx0QCeyXnehOoAy4W2HnEcmrqBTtTjaRWVBa10HdXR7Sek-90sr3skvJ2_M8hh-C2s5gwDKZFX7sLRd2yNc-5x9Q6XYWWwhBhfXw40VObjS75rwtli5GhDC4fxmnaIWyCBtXoAzH7Rp-lpTs_M2vTFGQ6srUdCsrikiXT21KRONXkuxxmSUCcstHZSFj0UZpodLNcExqgxui3cKgIUlvl4ekFVb2z49QDs-CxwpD1WEd3GQxjc3x2GLS1IazdKYlBZG48bTBAbSMunjM3mh1Eejt3kph30LA2Z0nxmtXm1qLmG0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29527446d1.mp4?token=HFRJwGMagOG53OYiodAHqhBjkd-Dm9mTLTVNUQwx0QCeyXnehOoAy4W2HnEcmrqBTtTjaRWVBa10HdXR7Sek-90sr3skvJ2_M8hh-C2s5gwDKZFX7sLRd2yNc-5x9Q6XYWWwhBhfXw40VObjS75rwtli5GhDC4fxmnaIWyCBtXoAzH7Rp-lpTs_M2vTFGQ6srUdCsrikiXT21KRONXkuxxmSUCcstHZSFj0UZpodLNcExqgxui3cKgIUlvl4ekFVb2z49QDs-CxwpD1WEd3GQxjc3x2GLS1IazdKYlBZG48bTBAbSMunjM3mh1Eejt3kph30LA2Z0nxmtXm1qLmG0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇿
گل اول استرالیا به ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/92830" target="_blank">📅 08:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92829">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">زننده گل استرالیا اسمش ایران‌کوندا هستش
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/92829" target="_blank">📅 08:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92828">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بازی اونقدر جذابه خوابمون گرفت</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/92828" target="_blank">📅 08:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92827">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گللگلگلگگل استرالیا زددد</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/92827" target="_blank">📅 08:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92826">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شروع بازی ترکیه و استرالیا</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/92826" target="_blank">📅 07:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92825">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bvp5kySwPbOHHTt19kUcSKyvLBgL9OeuN_gMByynZqnqlTtDLukZT2EpZe5D05r58Bo-5maZaiobJsafaFxi_2f2EYjKNsSuF6AYwkttYuWT6YrPAhmiZlDgplRr8doy5Czhk8fuopeEZyOpVKkoFsdur2swVm-MzZ1oMSHsVqICBSNw7b9X4XAq1juVbhicPpe-FUYUmQJu2ambTWVm0yTFDvq2RpXr30JXPScjmnzorOA1wLCRqzvzbvkXtSjdX9odfOm9IQz1xZnyIaqXut1ecZnjl0FRDwoygnCfYVMZwRSbWlu-60MlI43UTI9X5iRUtsxjEaYGEySnnyJm_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل عجیب هوادار ترکیه ای
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/92825" target="_blank">📅 07:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92824">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شروع بازی ترکیه و استرالیا</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92824" target="_blank">📅 07:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92823">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIYU6ZpQdKMa8TBg7W65T06a8LzUWz4NqKewFhGZbcKf6B6Z-yUHinrc6-C65a-vxKvPisojfy3suiyuqhI9U55m_pt46aqYKbCOsO-t1lF-Ytj6lIzYgAjAGNM4J4hirVtTjQN3K4YjiBBq7V9ueqvEbhgNnMdFbkmRP4T2SrjLspQvrb3XbS4F6Wk1AgwtQCkXhsfHH8mAoMSr9vQ43KmV4sf8RvCAhxa_AG-EqK20Loo9Y0epRaT5HVNKHd2BzTzjWiJ5YBnL-yWzmkrxLBKvQQ94HAKfnL0YpmAsCiB1JsQpfjz2Z8sFqbZfPXy423yVJoaCETXaFjE804c5ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇺
🇹🇷
نمایی از استادیوم 54 هزار نفری BC Place ونکوور پیش از شروع بازی استرالیا و ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92823" target="_blank">📅 07:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92822">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhRiWEgYsBmH2FFW5M0-LGp4oTZCvGYpNsDqZEiEgPz_G1A_5XxHNBlJN0-9dDbe3R-CJ-elZn7PGn8nv3a1eqyOv6hjtivpBgSQER-kCvcn-JyJZ4kGgFIP3mT0695YZWz8kzGD_CshqZ-mABJ0mLECrH2QqAzn8j_iD5gPHEKTGl0KCFfxMeJqF9HQi-6HlZ05ilNef_tYtYhbpj1CNpoBtHVFoi4VJetQWvtNf4VdDhHEw2dNvNCDNdGZ71zoiIopkMNax7an1746TN_ac7ITratDCjouJ_eR6o1vWh3gFV5Tf8V2BhfT6MOWA9Fb6h3vFpiCtIHN4r-wGM81Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
گل‌اول اسکاتلند به هائیتی توسط جان‌مک‌گین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/92822" target="_blank">📅 07:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92820">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Epvw1MmRO327R1yN-_xGmY9SbSW-mWybYc5a5CMvBmDiGwx3VpSY0A2pnAfNDQf3o6cDrqu8AB_kvtQlyMIQGNOp4Sq_7Ilg_XBb3ucK0cWVJqkt-tyVnc2rsnPNgmFWsNnJ0NRsp7ld72aOcmXrtIt9pYOsmVRZeeb6E081Rra3xGPzWDNZxYspZhiIQacarYRKPzwOfp6ThG2wCK9pLSv8BHZQn-eF9tOloNQin4g2LEtvWFpwb6WyWpdsh-GTQYVUdZ5CpGrBFyXxV-TfHcY5YDLvW9lGvENyW3-NhQ4J6SPFrxhV4yw8Y5MDcGH7FHk7o8tkVbN7hkJog6hJCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Arg_iyujsM0jwFlYQMqFW9J3hKvTCgQjN5X0D3CAY372ndeIHatzaO86E-C3tTN4L49uF8E1u0R04NBUMr42QqVUDlJtT9zpLhUPPsroUTkxXBiy78aCVgvydVM_PSh4eJk_BkCpN3pw3ZnNuaZ3phiNWN3PtrngNTaSljxGg0gRauya5a_mYhfHMNMnXEkggYwlSOuqPjqISQbosos_wHu90MveJGil43fhNfYnEP-iV2ueYpawHFMKf4r3Pp9vfB3ZCzWg1kdaDGmiD-hwkxln5aKB5Vrm1cEQvgu5Ty6mCQWPj6iaLiX-6r-jWTd5qsggR2liG8ln5AkFYo0S3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🏆
ترکیب دو تیم ترکیه و استرالیا
/ساعت ۰۷:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/92820" target="_blank">📅 06:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92819">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این بازی کصشر خالص بوده تا اینجا</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/92819" target="_blank">📅 06:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92818">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJ7TNNvfIPvM5i06TQ_sT2pXpFTa8lBkYKl2USlrrj1E-MAH861P9QnmoESkWphDK8EZG9hp-KLS9KQgQIX5hNQnQxUrpYZj33DKYgQHqUSIrSTIMZk2c2G24vqukfNUGBBzo8d4SACXloMd3ZCsI0FQnPaWm6U3f7lKblkwWGwleFTtoPXF4O3baMHp04BJKkls1sZ5thSLUv0Y8LuqqBdeZ5bbt_UWoYlihAkhBIlaqPlcqAQ1xJ6lQGu-CcOOoOQER4IflRU4WIBiE8Vwf0RLyA8bPIRmglCLtMctmXNucAyHDFnmbYf5whXVgOoGo5TudebUpTco3KLKyurhfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دوست دختر رودریگو دی‌پائول:  «بعد از جشن قهرمانی آرژانتین در جام جهانی، رودریگو مست به خانه آمد. من مجبور شدم مثل یک بچه از او مراقبت کنم چون نمی‌توانست جشن گرفتن را متوقف کند. به او گفتم که دوستش دارم تا آرام شود. سپس او پاسخ داد: «من هم تو را دوست دارم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/92818" target="_blank">📅 06:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92817">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-pYTTi210vygWzZwCBjmRqz0_0Ie9hvL91CUUFk2jRbA2Ef1VQ94dBL9yaTmwaaM7lfj2SW1T3QkKwg1O9v9Kwz9_KhmCdIqKR9hX8YO2CJQms0e_pRSAzcibQKxisZ6UDRP-r1lVeGaZu3imey2xJMs7ZCYlTdgfB_rRgPwmXLRIwN_HFc6tvw7bJZ-vdOCGeHjH7ppO0gxAUnSo9FhVmrscI-O2gPXhYKJUSjI2QlF4Gle23lWAdFnLv0NU7BXXHe2TuSnQJZT9M7ozCLW5yGtSRj_g6R4ROjDp8locWoIkxEggMT38taNWz4yQBvsr7g9v1hgTnTIyuG9dEZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادارای برزیل دیگه خیلی جوگیر شدن و اندریک رو پله جدید میدونن
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/92817" target="_blank">📅 05:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92816">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcdOTswMXmgUzWAKAKslXHIPPJ3EDCuI4VIpw7U-69KWIUcNT5Tqdwn5vjtWqMzoPbFi1pkjl4dedtmcg3YNk4PZQm9oLxCTsIRb379GXWVtTw7FqKKTvLNU4idYb30SA_QNwkghy-jdx7oM2NyEcAHCp4MjFtaRzpkkxItmo8e85MmiU4qDYJ5-f06SNzWmwKHsnLJIW4Gp77IbwaAf9l_0PBBJm2lCAoli-bl8wCOs8fx48YDcvxRaxvVx4zVVcRwQ8eB9pujkncQtCrj6CFxkQxWZve96kvy5PrKTmjp5w3N5QGevgLQoVKrBX9WhWQgeTLZB2WmDvgfxeSFzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴
جان مک‌گین اولین گل اسکاتلند در جام جهانی از سال 1998 را مقابل هائیتی به ثمر رساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92816" target="_blank">📅 05:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92815">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏆
🔥
پایان نیمه اول بازی
⬛️
🏴󠁧󠁢󠁳󠁣󠁴󠁿
1️⃣
🏆
0️⃣
🇭🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/92815" target="_blank">📅 05:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92814">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0-XR2TYaOx-bmnT01ZlORYXA37NPw2-XLQCoets5trbSDbWt43mzZ6GNwtgSIEIsGjJ45qb6BjbE5BOLAMlDad-nWmvG6RET3jioqtIxO4XjoYEiVXFMCf_cu5DY3IC45E3TLqJXp0-29y6x-_zq215KNFYVi4npejPk6hG52s6zjLSyheIQ7WdcftDOZdbpFWo2fepgJQpRxzeRgdCh9ZftEMnQ1z7RfBHogMU1spc22v48BGApHObiyZCYVm7kChrCATuISB8EoKg8oTndEEyJrhbmQkvS-P37Fus27dlRyZEFDBdmTZlF1XZYPRC4EYyb_k1qDxHJTXbPXUqJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازیکن متولد ۲۰۰۷ و ۱۹ ساله خط هافبک مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92814" target="_blank">📅 05:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92813">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bcbb2b8e.mp4?token=fFSQIOkatVOGT4Pt88kcT940qDF1y0V7ViumPoXhn7CqC3jbsPINyP-wRpw5Ylkia-MFx0fckqZpzTnH_9SJGXDJ6iRbt1UWd7Lgd9Hc3sZ97Rk0Fy45DKASs-AudRTxZ3Gc5olvtawryLceJkC66Ak7OX9qCIDw0JV_J7Mj3QM2HsU_UX4fFr2-P7mTS_lvLf4pwiTPA3NUs_mHJYiJaHCM_PGugCpAMA07PkIckL4j_Ta6S3yIkcdMAnVvGaXVaXcTo0j7rkvfh2jlJVavzlQE1kkEFaN9dF3eW5Oq-SxznX8C3IetLjk5viQJPb0bAZY2D_CZkbAHOO5HDAejCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bcbb2b8e.mp4?token=fFSQIOkatVOGT4Pt88kcT940qDF1y0V7ViumPoXhn7CqC3jbsPINyP-wRpw5Ylkia-MFx0fckqZpzTnH_9SJGXDJ6iRbt1UWd7Lgd9Hc3sZ97Rk0Fy45DKASs-AudRTxZ3Gc5olvtawryLceJkC66Ak7OX9qCIDw0JV_J7Mj3QM2HsU_UX4fFr2-P7mTS_lvLf4pwiTPA3NUs_mHJYiJaHCM_PGugCpAMA07PkIckL4j_Ta6S3yIkcdMAnVvGaXVaXcTo0j7rkvfh2jlJVavzlQE1kkEFaN9dF3eW5Oq-SxznX8C3IetLjk5viQJPb0bAZY2D_CZkbAHOO5HDAejCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
گل‌اول اسکاتلند به هائیتی توسط جان‌مک‌گین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/92813" target="_blank">📅 05:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92812">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلللللللل اول اسکاتلندددد</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/92812" target="_blank">📅 05:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92810">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n22HBSgvYmlAmbHVSZH5H4RuQ7LPZEY28wIZD2-wgchQy22Pdzo9fs6PDuciUE7xOsQ3FSbj00-ulT_ph6t6PB9Iwse5Lb5ALTgKail9WqEcjwrwmksyZOFA-0FlLxF7JZJe9KQWpSdOFoIErdf40Wwf5tLCTdnDZJZ-pq5po2j9VU3pHYMXRfRoL8VlOBs_G8Qu7ZHvRh0sKIkp8vc5UnEN6c8mOauKy3oixVxF4HlThxfJZ8B2_mhkN7MOXuKqXAjPSpoQH5jj06U6qfQhS0yZIr4yDIa9VDmI8bb3wqAJnlHzdtC92_hH1uVBuQfuJmonOEKs51tVJfFXfYbTfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRkgOtT5XTHDjI4oJhYTfDkpyTG9W-2iz2FUXf0b0CdZ7EH2wjILuDUDs-_EqLLSVZ1A1n0K2Yuz8daU9mT6rFd4aBJLyS2pGw9mtu-152t5SMktULSQuSUoOm-W363rsWlTm9I1UVIQyOn1lCtlBgZgTz2j8_p8hdn3DlTO85XsLVJSdijSJzot4ZFMYdvwDRJh8Tw0o-t-ygwI9_YorfEn6kzUGKUmR4HR-lLUUCDZxKpPBH7TAM4OOynGRr-N-vBCQNqLU8QCl2wvLTolJ63JGiZ7cRJDiLbkKV-BL_Wn2ZWq5xabw5G4kSDgTYBjnYZsCXuJJ7x_sMZ2PDheHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇶🇦
صندوق سرمایه‌گذاری قطر اعلام کرده که بوعلام خوخی پس از گلزنی مقابل سوئیس در جام جهانی، 3 میلیون دلار و جدیدترین رولز رویس فانتوم به ارزش 550.000 هزار دلار رو دریافت خواهد کرد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/92810" target="_blank">📅 05:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92808">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IrGGGnkYYd3psCY0YqXEpkVcKL3O5e3i-7nl8MFnDsKxgCmh_gqTSGhbMQh0JKfwzLzNgLbe3_vhEqYdJftp34-x59QlYGgfJGABbpeYe1Za1SaoHBz5WWQ-I4wKzqLZ6FdUrLUwiz5OjBTXE5DrgBhbqLcgBt2eg7l-j9C8zeV4_35xOfwXYIczruHwmKBh9zo0qJuBeKE7oszF05LsZj89Qsv_MJM14-WUeoTDMp4IzDFT1ujb6lMHuXurTVKdDYKh6I3FMSSSwdtsbYMixlmVjouOcAuUtWKnea3XyLRtnAqH7OTNq3-cb_enP1SrQ7bDIWifpmB88CWBGWA6-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2o81fftn4IS-H4hMtBS9OVWULixNIUAYMGIJlQnr2mZNhqP-Ih6DR_lyCdJ69kN8nzDb4P8ytSNCdVBrwzvhaB1U-1kWUmLU5F5oU10P5TSWHEp28jpuG-CWFFPMkKbldQz_EYyqtr1AFxmJEUN3iLwT2MCSk-ck_Tc19qPZ8cWgGkr91c8COolmaKohAYiudUb7aIc8hpOrEtw9qNcdeA8zo2ne3dLPaVkunNTK0viupnpyYijw7_Q06gZkel7eOz3bD22ZqybZ9M5IOfJAArjyK8Vm4J4oKkploXJKoqb46fkD8LFHQbW39SFOIlW2M-B5kVUH25yD5ArW_WA4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جو ورزشگاه قبل شروع بازی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/92808" target="_blank">📅 04:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92807">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بریم سراغ بازی اسکاتلند - هائیتی</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/92807" target="_blank">📅 04:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92806">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqHLT1Tw_hN7IUgkWo7FPPa_ArCnvxy-Sudg429ySBtgRPU9VXyVMyHOPwwweUYSMAyWePpK-IpZMtZOWaJcGbepawK424jQq0vLPsqa5lcQocNDq08ur1_e1uMVnqRuPQGDXDoM4HtTgU2OBzg_aPEca2z3oTGzL1OYArKwbEwa8G7GQV6bmhqsEC_vUSKUoNFxVUeVUPrX4C_KMINwOUiiJ3Qc1nrVOGiVblENPrWiwLcopjYAuCDff0_hLV_kzIFQNgPiKdRXtlLpTon6D0jnyosp02ejB6V7LMH395hfmxG51FfMd17iia72RVb8B6vmdIaKYQu6R-ZGupHrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین باری که برزیل در بازی ابتدایی خودش در مرحله گروهی جام جهانی شکست خورد به سال ۱۹۳۰ برمیگرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/92806" target="_blank">📅 04:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92804">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oyUjeYv3i54sLuJrUJ2ts5wAqAcclrwxR8HaE0i2uLi8xPqppqK2Skq5IRRhYxYkSzByI1ejhBcPuXl8z1R7_xStvGUGwABXs4yPtQ9mUuZ1gycKeoQb2KWlZV-Dsa8NcZekrXJb82lQD32Lm0IbFfc1Ohy0PTAE09FqQYm2y-aiuoP1zigBo4Ina1dMyAF8yDBq-PZWUL0ioqPPv3LK_x_YCZzV3KyQFuz5MCaL-8nsVswMaQlCdWFY5nadpO0xZdfep2PAgnlu4YANVrBtqWrgb8QuoWVifRly1NaiWpfGBmSIpo4wE9T7gQXyPgVLczEA7NbzgA8X1mcQmerMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aI3mLAr0NGh11ZZuw8uItQ6gPKdAqMbHQ-RAsTgIdstglZwYfAHs4ILvoVWLH1x5xTwQlQdYtl2FydNZqf-kHxMKq6kP-XjIFu5gOKt34I47s95NfqG1Lb1FgdNn5Z5cGDBYOdbfu3gbuUBL8PFV_de8ycZBa7Qlel3LrC_IAFmDJ-1B3vjMwMDxJunq70zqCvQ136L8RjWcaG0jXnOJ_QPzpyY-JtiPO1heczCXY3Q8hw_cK2Fl6efNbSr1CfuSNxkBHKWsFaANSu-FgigZoP6m8BRr0n0PA_im9n3pNQrfQbOLTrDkOdOiJYiO5MAH9GDCTTAFCwW5rhdvvl4eWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
خلاصه کریر اندریک زیر نظر کارلتو:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/92804" target="_blank">📅 04:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92803">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPt-f6wRACkKOLVA3w3i8og35fG8LMDlhDHDfS48sabiBSY1zg1trcCsJJbejf59yJMjQKxk4PgnmQzXLvy5kV6kjsEgDaUaj9KGrAb6ZcSNV3oR0u1zqOlx_ucFs-XAuij2MWy9ysmbZNJvPsiwtcckxpUTUjETqpNg0ozGHvyLRqz4hjBAylS9aZFIistOP-irqmT1nRPRNtLm9uS6vCJh5ROIAUFwZ-xZL7G9oCr1wBIAdlDaZyvvDJFzMz_YbzgoHXJ2Mx_s_hKMlabTK_wDfr5TouP6-NaMMD9jrxX0_Gpl7R2jH64nLx4FxQz2utC_T56jnxRFPwVfCy1Osw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
🇧🇷
🇲🇦
آمار تقابل برزیل و مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/92803" target="_blank">📅 03:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92802">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojp1D8paeEifEzGxNljAVIpqLhBHK0DUidjc1CgI4hTaCpQP1DOZPD2oEt8Bv5xTrtCf1PAHmCfxcq6NbCF7v4lJNYA09OvS_mFadRMEFZby7WLRu57NKDDI_lZUkzQ0JvWPw1QOIipi9pxnr79KLP3cEwygdhOw2tw64hXNNW3G8ihAjdAdP-l42FiGyM8rJFMeet7PJcVUetZPe5XzcDsVSP88hBYsAq20KAHGXAdOqOKEEgWFtvX1HK04TeXGV4bDAjqPvSfO5IuX8hXBbwuXiZOmgZYNKS7Mj01JLdAHgtPAlO-DCLtMZkWgSKAdFsXMB-4vlH7cCThbBDWsnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وینیسیوس بهترین بازیکن دیدار امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92802" target="_blank">📅 03:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92801">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD5f2jWebVv9G5A1pVF-EIkpm-NHnPrcBAiuxG3O4I6K5tjo6T6oaIejrtPtm08NgnWNH4UMrmcCDexKenz1aKL-Z-Sq1BGxyVKm2Fj8rS_Qoq6F-0Q3ZgfP8YNs7Y8EHKgIAGkIQW8__SUFaQxHBHG2zGJINVysD3ZyO_3K3LN-CuefMvG4_sAhS7K2-yH_hKS7MpgjXO1iS6IsuWRpcIx3SU73l-rg0453gxpjPK8DW_cMcdDBdnfD_Jn6Sb-i2I1t5brRVbDZgepwqlZm_AUst_NslRTK3dP3MBD8h20Oteat2takSGAXwOOE0obsYQI3RwQKiTLJSYJBZpWr0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمرات بازیکنان برزیل و مراکش در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/92801" target="_blank">📅 03:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92800">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شب خوش کونم از ته ته داره میسوزه
ولی بر میگردم
😭</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/92800" target="_blank">📅 03:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92799">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwjBNWCsPWhnhcOsXdJDS_VUnmX15eY5JqVt7uyEgT6QFeksKJyhO_jTTvG5NHfIhr8RjoZdDroXSqsk-4PQ0AE07yLw5p8ZwNG9XQRKtp3ew-AKllll7hEaB_xydhdtKikh6TpR8Sakw0GwmHI4gQQ8nk7zUdFdbpyay0tFwOiCfZa22e2b8Ros8Bz_IyKH6ogGGE2kLZ7GhXZ5m3URnLsDOwz_jQUS1JZnWx9ZKMQGdPrDUYVCQ0Qf_NUgapTrTC4likIkHkF2yQ0v04cNZfh-hfQ9goW_9ZwyJyM8wU8lLbBVoA-qYfQUflefw-Wkr4tkq3jrfyFnbOlYDdWwfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
وینیسیوس با تعداد گل‌های رونالدینیو برای برزیل در جام‌جهانی برابر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92799" target="_blank">📅 03:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92798">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcNf3b1b8B22qyEu19D_t2TLkDSxK_X8Q8IKN8DA-sXWXrWeQRF67Tsv4xKUiHiLB3K6GkP0wrDj0gr6224GRdRS3E7r-sPln_8ozhsRDKj0CBJ66mF61WX1O3P4SFYq2J7sMIO1uhcEbIJ_B0JMvgua_xDe_cEqWon2rYaGVeDdWIP--fdiWEtTWSULXUGnhMskrY3TCZnNFVWGWVFewMdbHvXjzHjiNVyGu1rKsn9SeNGMj-JGP_hnA9DpQeuJFVcXIV8ijFe4CeK8R-GAJfUGZirlB-20MQzQ8bnDu_yvBR4srQyWdl7rTfOtOF6V_5TDcv10u1Ue2q7TJm2f-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|نبرد هیجان‌انگیز نایب قهرمان آفریقا با مدعی جام در روز سوم بدون برنده شد؛ برزیل برای قهرمانی در جهان نیاز به تحول اساسی دارد!
🇧🇷
برزیل
❗
-
❗
مراکش
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/92798" target="_blank">📅 03:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92796">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqExGHnfvF5P0UrJ36Ot_Wd7RJFNbc56c-PF9eBaoyPVhDlGMZK66C5tniuEXubjLswmk0b_Q-9FoxhGwycVK24YG4I1-vLE-gFsPhj22GPjV0ogGd6YMMfiyOyzoJb9XYaFi7znbUESgLAx0U72p4hmVH5gtuXkLaMw9RQ10lHsfnY8KsTne8zd0PbUhNGe6IOuMtAD4_AoEAkqKgtDE9iPGzO4B1RTqZAzqDgvVVU6YhgTgU3sTwKhj3ZAqhyTJabl3aPlHQzY7xjK4PLOizPiLU3KVqoRGDQ1FYrZyGAR9iDIGy3qp8dPcz-3RFXCryCj60M7w1YCHziwPobU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iIGxK0gFmgLAiGfeIy_ZEMBaFWIyECnzqrx8ZEMjuvAUroZ8Kgxua7JDybgQTSV2oEAoV1Lniu20zywtU3jyLLF3Lbj36I9A1oqPFmZPHq2O8QGo2WOPsd4ZcF9z6wh_-u-38qCoyk3AlF_6cxnZJ77LZ9HxkQTRKMXZoQuPC1qB-BjocTuWDB-KIq4vGBFH4xlHXe_9T_E5pOaLguMmo0zL1hW5qK3pcfi9VfR9JFyC8LdZ3PSnEMI1gc3hUFYS5iFiK2rlPxD7oSvzxujV_Ja4y97mTyvaPJoh9dBfo0ITl6JHRHTHAJA-a4PadP-nzOglp45lh1MR6qLzVFKh3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🏆
ترکیب دو تیم هائیتی و اسکاتلند
/ساعت ۰۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/92796" target="_blank">📅 03:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92795">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بابا بزنید دیگه
🥺
🥺
🥺
🥺</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92795" target="_blank">📅 03:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92794">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ee5b8e61.mp4?token=tzIWDlavAuuaVuJbs14nyryn-fkZXMbfSFPyeBBctViJ3feAQt6BSs3-mEcsgfdTKF1oRcATGov_os64YXQJEMpgQTX7HLEd93W3ct25Gfhp9OTlKXIU0C9CtCf1CeQg5wUm3hEPvG9qbOuxRYPd0Ola1QqxS8MvhgQ5_wCN6i2XHV2BYUslTkXVibsS0v441EJVMHbXKIXr_b0_lArNSnxz_UDlKTfGpGbZpevkwkuAtIxD1h8mk1E84jCN4F9RMqsps-pVDBlEGOtSRJIf2u6C7ReqvEOfh41RY0tWhWjrl3vmMznh7oDO4Sunu-yjjJCtB8tQe3OftHsgGKxw8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ee5b8e61.mp4?token=tzIWDlavAuuaVuJbs14nyryn-fkZXMbfSFPyeBBctViJ3feAQt6BSs3-mEcsgfdTKF1oRcATGov_os64YXQJEMpgQTX7HLEd93W3ct25Gfhp9OTlKXIU0C9CtCf1CeQg5wUm3hEPvG9qbOuxRYPd0Ola1QqxS8MvhgQ5_wCN6i2XHV2BYUslTkXVibsS0v441EJVMHbXKIXr_b0_lArNSnxz_UDlKTfGpGbZpevkwkuAtIxD1h8mk1E84jCN4F9RMqsps-pVDBlEGOtSRJIf2u6C7ReqvEOfh41RY0tWhWjrl3vmMznh7oDO4Sunu-yjjJCtB8tQe3OftHsgGKxw8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی برزیلی‌ها از گل وینیسیوس کف سائوپائولو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/92794" target="_blank">📅 03:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92793">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Du_L2ww82aHz7K4vl9GK5SIisVRkV4hAbJ_bkWntYhniSkadi97r6Fvn4qQN1uowx506O2z2o2_P0w4kXmZEy759ZW8faFKNmHHJM48_87zC8lDKTdy2JMGT6b2eLuLbSHVwioUkkyHByIovr95KG3UcKkiBOx4pz3b0fvzlNdMJ2EznGefBvVGigl4DiEa_S-t6OOFDmWrMHb3Wttu_FXwyln9NIj6EBGjdsvD5b2pII3jpvRFG9oa8pCl6a5BJYFs7vEJ3T5LGiLMcM_DaAi_K0IFeGqoIa8R-wSNkRtgeZqoD8XuAeC3-arVIaz2UwifkEAy_14K9UviTTSO5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازیکن متولد ۲۰۰۷ و ۱۹ ساله خط هافبک مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92793" target="_blank">📅 02:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92792">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d20b3cd9.mp4?token=vp7Dmg0hRi6WjYKTSXcYKB74fbrjni3jiWvIIE3Bu1R1v7bDkm7smNToVn90f2ksHvqh1An_1i49prYgDcNRKQfixUIRluHrDNiLpBg4gdzTQgiwsshbWwI0srOvzjh7QsBMnkGuoJVHsVYqndDSwLy2gbg56Qc39IgXr0RaUi9oT-QTf_r4pj4_eg-UY0GquiZPcuhoJczXYjK7sfEcHerTTB0om5x7qftDfrk0coRenRkz8pyiTDFK1oM4ypkVWSBTMON9GvKzDriz__L3VIwn8kHE-TmvRgXJ1PC_lSRgl9owsPj7kilxhAJuqn5XCGrU--JPE6PDw_N2fSI51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d20b3cd9.mp4?token=vp7Dmg0hRi6WjYKTSXcYKB74fbrjni3jiWvIIE3Bu1R1v7bDkm7smNToVn90f2ksHvqh1An_1i49prYgDcNRKQfixUIRluHrDNiLpBg4gdzTQgiwsshbWwI0srOvzjh7QsBMnkGuoJVHsVYqndDSwLy2gbg56Qc39IgXr0RaUi9oT-QTf_r4pj4_eg-UY0GquiZPcuhoJczXYjK7sfEcHerTTB0om5x7qftDfrk0coRenRkz8pyiTDFK1oM4ypkVWSBTMON9GvKzDriz__L3VIwn8kHE-TmvRgXJ1PC_lSRgl9owsPj7kilxhAJuqn5XCGrU--JPE6PDw_N2fSI51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
صحنه مشکوک نیمه‌اول بازی که اشرف اخراج نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/92792" target="_blank">📅 02:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92791">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/92791" target="_blank">📅 02:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92790">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lG3OK_8iBe4x39wWpEu3KQ0NhPdjOhW7aHgomWDgntsEWSrKSUT2ul-msZ_rbYERE2ekQdguYK4XzK2wJqA2RY1NLfSqcfqSLH40yGipHA2dQRFhhQgqPmxPfEyz6THPAemdGV2ImQPdbBDQg7b3KOSdGldpFzcxvEdID1jyUjG0ZuzH7w_YhRXpbvhCP_R3xcanbfIhejE61lMS2cEXv30iL5E3SM2HlKHujXYpme6rNHF20zuDqw4Qb284K8A3tZK19qj9v6cvDYfhH3NIbxdpvjK5L_2DtYxKUD9d2K5uTUqW_XhmDzuhyi9vVTS82J2h6wn_jgleadxGPvxP7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/92790" target="_blank">📅 02:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92789">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KABpb6EQFAr-XwHzmSXW8nKXdzJIy8ONANpBd9USwIIKWrOvabNnX-5A9kGyqarHjKlgmA73bwG6JG5EgQX3ZZWypJRampugOApbUlpUXmKGskAfEnySJ4rBtx2gpbxxnTzes6ge7QUh_qZwGM3NZ5ivXprMY5VPaVPRaGQD4nVpamGQ1s1P3NVDU6R_FJ8Bii3K-dCqrr9KCos_G1VH9Gw_EZi8to12tshdwHjIBHpQl_nfeL4ZeZ0m5pcOOQuvnxwqNx7hjSrRb5lnuit6O6phpgOZXGWnTYJ79V7IR0bDZnBvZ355VBgnwdlb1c63xV6ac2t-arod28thgMSfyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
آرشیو‌وار: اشرف‌حکیمی بخاطر این تکل باید از زمین مسابقه اخراج می‌شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/92789" target="_blank">📅 02:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92788">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آغاز نیمه‌دوم</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/92788" target="_blank">📅 02:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92787">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5kApusIini9AFxlr3L5RTznIvOh4eEonb_jpGMLAh2toHzRuO35Usuk1N8QWkcuT2CAT89y9rxPoK_XnwXqrP1zuX53jS9DWMnVytMQnQvFaxC9HXvhdWrf5b6QljjxBiZOn_rf3IgTi7q7kntyUhglExObYYuhSSwtE3kfh2FbaTv_s6LnVwFpmRv9YmjxmxfVj1uM1T87950l68jbCTpuGXE3ClO1bjUE-_wRV9QfyAHauyPXqcuccqDZJ_8V1SvD9D0rAs0w9rZ7UW95D7dsfnm8rRSRThxLiYzFSHIfFQQU6iWg7tWiK0KJWSaN2-EflzevYmw9BsRrowl7lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
آرشیو‌وار: اشرف‌حکیمی بخاطر این تکل باید از زمین مسابقه اخراج می‌شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/92787" target="_blank">📅 02:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92786">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3tTDv5HAAmZtYr8SLUnorpXO1ZIlxLi2ZRnz6eGzpyrotwz1BmXTMqFYos-WWXnt7OVEySzirrTaFgMkHxqLPfcKWHWXM9cOeh0AcDWrF0VoyVD6dOMEtkTTU4mpgyJXNP2U2CzjbW0-qsMWmtTOBjRdiNc8PgJVEi-QgkvyhmtV2xMqfB1-ntOFCG0-gxw4fGSc99idq2q7htFNN-qo8L1Q3ctmM2z3uFMAmY5vRWZjpFfUM15V_kMBpFTx9Vi0LRmTzGicJK6kU3cgMg9v7_O8z27dgMAPkyPhRZ7XnEL_S7DFW6arspY7mdNwP2X4qbfnrpW3kWg_pBdJcuD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/92786" target="_blank">📅 02:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92785">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh1kez6hGCrUV49gWjUmX8yv5z3jWU9qKEVnZABKI--N11wOllQfWiiuitV0Qy-MWBsVyQeAg4FY0EN0D3E041Zug4dancliY9e2PqYRzwekGWC_4i9CQfCxNcUrdI7nDogiCle6JWb684UENApCcjM5_xvzMeRx-THWdjADkGSqq_ZYfTHAnWNzJUOS8Gvbo2ACrvjsX5vE-G5Yrruzze6_UnpN0CuAri6FY1PtDegKkZ4dNZOfdmmWyP6qAMq9U9CwxratfTD6Uq2zYqWFeoGvrMSVjWU5lI7FBzE-np2aVtezWw-j99Zu3xNiCmMktsRUR8qtE_q3L8tSwr8qrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار وینیسیوس در جام های جهانی :
5 بازی
2 گل
2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/92785" target="_blank">📅 02:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92784">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🏆
پایان نیمه‌اول؛ برزیل
😃
-
😃
مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/92784" target="_blank">📅 02:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92783">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سوپر سیو بونو نزاشت برزیل دومی رو بزنه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92783" target="_blank">📅 02:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92782">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">برزیل داشتتتت میزدددددد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/92782" target="_blank">📅 02:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92781">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/92781" target="_blank">📅 02:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92780">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ایبانیز هم کارت گرفت از اون بازیهاس که احتمالا اخراجی بده</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92780" target="_blank">📅 02:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92778">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwGEtrgBI178E9xFjo5Csls_q3Du1vFo_oWANyQTllkp5ZtDdLLHKCLyoCzpKW126kybU_RHj2A58W6zIrsg_yhBJCbt_ZAUM-FFQf2agV4U_rgLyuV-5M-6FenKmhss8IwOUjwNm3unQnhNi_t5pPoLBEDSA4UJdYY3ai-DiaMhcBZU3DHGb0AI9E2R9T5pmulXwJpuDS_sYrebXYq7I2jrNeoaS5VuPSbS684FYUty9PzlBZBPZCoeQcejSs0xk9TammlX3044LYSVLDh6bsRdDNyVY_93-Ea3lL3BYtJH6Z9YPjWRGpUO-XQrYKwOyTMXqh7DErKSljmaYBY3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گل‌اول برزیل به مراکش توسط وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/92778" target="_blank">📅 02:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92777">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کاسمیرو کارت گرفت</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/92777" target="_blank">📅 02:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92776">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f79c357bf.mp4?token=YQaw2FZ5IwRnK5s5riVJkwvbZX6eSEiV_JZpSggLxCVsI4feyYDt3Wg4uqpybXqeIGYJ_sReKj7dDIEqIfiZWi-rI-1LeCYQMuxJ-ey9pjREtlKqzKKC26gb-h8twCBMkm_rnEJykMwHV7hMGjThsxEeqEkkYb26TYgKChAys3w55ngD-tNHtahH0eUvKO9rZqtBR4CfzJcReGA-fF2C3TI_hHPCwpaoC8iRzduL65TFSa0djbroY5mh4LjM7DybaHE1N2hWqcHyddpjNdE94g8IILEnETgOnQ0bQnWQ-tfr_fXrju65jxLn2Yhq4cuzKCenOxEgQJcUtZ1s5e4xKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f79c357bf.mp4?token=YQaw2FZ5IwRnK5s5riVJkwvbZX6eSEiV_JZpSggLxCVsI4feyYDt3Wg4uqpybXqeIGYJ_sReKj7dDIEqIfiZWi-rI-1LeCYQMuxJ-ey9pjREtlKqzKKC26gb-h8twCBMkm_rnEJykMwHV7hMGjThsxEeqEkkYb26TYgKChAys3w55ngD-tNHtahH0eUvKO9rZqtBR4CfzJcReGA-fF2C3TI_hHPCwpaoC8iRzduL65TFSa0djbroY5mh4LjM7DybaHE1N2hWqcHyddpjNdE94g8IILEnETgOnQ0bQnWQ-tfr_fXrju65jxLn2Yhq4cuzKCenOxEgQJcUtZ1s5e4xKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌اول برزیل به مراکش توسط وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92776" target="_blank">📅 02:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92775">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">لبم به لبااااات وینینینننننییییییییی</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92775" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92774">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">چه گلییییییی زددددددد
😐
🔥
🔥
🔥
😐</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/92774" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92773">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رحمت تو کونش عروسیه
🤣
🤣</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/92773" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92770">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وینیسیوس
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/92770" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92769">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گلللللل برزیل بازی رو مساوی کرد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/92769" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92768">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">برزیللللللللل</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/92768" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92766">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oYekJ7lZW1nGAFn9mkR1sCjWPKvWc3c2kXTDgjWjQ991t_OoEDcSjnxjUCMWGnQRjinKpVoEDSO5vAYY8WPW0UVQ5DGCw6rufhf0zkrnIFLo_mF3c_dCwkatV2kuE5QT-Moell0rRaFUMPHu8bqs-y4KNCTb8AgLMBuOfXLnADoUlqulpq6XNE-q2hzLToKvv0qua6YsBuY9CzMCTZViKCQ5QBIbYSFu3WlMXo3lbnkFJ0JEtY9vY5yLeC-PnUe6dTZdlRQ7sxf8zk1bVl1gY4oqzcdzWImP5BLIU612jImctObHacF7E0sS-Z_ijWACwMtDvJrH1fT-TKz_y4JBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتشه که آنچلوتی ابروهاشو بده بالا</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/92766" target="_blank">📅 02:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92765">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وقت استراحت یا همون کولینگ بریک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/92765" target="_blank">📅 02:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92764">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇩🇪
#نقل‌وانتقالات|بایرن‌مونیخ بدنبال جذب اسماعیل سیباری ستاره فصل آیندهوون هلند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92764" target="_blank">📅 01:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92763">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
گل اول مراکش به برزیل توسط اسی سایبری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/92763" target="_blank">📅 01:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92762">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وقت استراحت یا همون کولینگ بریک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/92762" target="_blank">📅 01:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92760">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/81f3af91f3.mp4?token=Hrd7Jr6yR3dZnbUkBMzGhPpAB0EVxg6rDc4hHW7yvcGSBtQnoBxIfuCdVoWDunzZp9tYhuco02oL_dOcqcuGmlR9GQLu86uNRFb287C_Nvqa7e0j_CmO35hXmdlr043Xe-OXMpGCQLqxpxQakQbYlWqfeYp9bjA6Nji5tSoVD7_L9P21xVDXVZRfhNQiZGHGwGmzHR3PBshI14jJqvEkovNuTcAveCLqeACh0MVl0pX9-gQGgIQH-Qg0ntBLR6d8LSHcANdoUEtCh10KRhNLihVJM9CWNQoWGWjntOeT0w8eoPSbvrbxhPx_LwIE3HZR01DqOsk3ZoKuYUgjKzLR1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/81f3af91f3.mp4?token=Hrd7Jr6yR3dZnbUkBMzGhPpAB0EVxg6rDc4hHW7yvcGSBtQnoBxIfuCdVoWDunzZp9tYhuco02oL_dOcqcuGmlR9GQLu86uNRFb287C_Nvqa7e0j_CmO35hXmdlr043Xe-OXMpGCQLqxpxQakQbYlWqfeYp9bjA6Nji5tSoVD7_L9P21xVDXVZRfhNQiZGHGwGmzHR3PBshI14jJqvEkovNuTcAveCLqeACh0MVl0pX9-gQGgIQH-Qg0ntBLR6d8LSHcANdoUEtCh10KRhNLihVJM9CWNQoWGWjntOeT0w8eoPSbvrbxhPx_LwIE3HZR01DqOsk3ZoKuYUgjKzLR1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل اول مراکش به برزیل توسط اسی سایبری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/92760" target="_blank">📅 01:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92759">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">😡
😡
😡
😡</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/92759" target="_blank">📅 01:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92754">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اقاااااا کیرم تو ابروهاااااتتتتتتتتتتت</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92754" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92753">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اسماعیللللللللل</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/92753" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92752">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/92752" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92751">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ضربه پاکتاااا گلللل نشددددد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/92751" target="_blank">📅 01:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92750">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/92750" target="_blank">📅 01:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92749">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">برزیل بازیو‌ دستش گرفته</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/92749" target="_blank">📅 01:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92748">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این تیاگو مهاجم برزیل شاید فک کنید نزدیک ۴۰ سالگی باشه ولی ۲۴ سالشه فقط
😐</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/92748" target="_blank">📅 01:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92747">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وقتشه که آنچلوتی ابروهاشو بده بالا</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/92747" target="_blank">📅 01:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92746">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کیرم تو کله کچلششششش
😐
😐
😐</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/92746" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92745">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مهاجم جقی برزیل چرا نزددددد
😐
😐
😐</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92745" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92744">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/92744" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92743">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تا الان مراکش ۶ شوت
برزیل ۱ شوت
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/92743" target="_blank">📅 01:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92742">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کیرممممم دهنت آنجلوتی این چه تیمیه
😐</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/92742" target="_blank">📅 01:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92741">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کیرممممم دهنت آنجلوتی این چه تیمیه
😐</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/92741" target="_blank">📅 01:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92740">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">این چه بازییه اقای انجلوتی اخه
😑</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/92740" target="_blank">📅 01:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92739">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بازی خیلی پر سرعتهههههه</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/92739" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92738">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رافینیا داشت میزددددد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/92738" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92737">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92737" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92736">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">۲۰۰۰ دلار روی برد برزیل بت زدم پس اگر گل خورد و اینجا بی ادبی کردم ببخشید ، از الان بگم
😐
استرسسسس
گاییده
منو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/92736" target="_blank">📅 01:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92730">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کم‌کم بریم سراغ بازی حساس امشببببب</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92730" target="_blank">📅 01:33 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
