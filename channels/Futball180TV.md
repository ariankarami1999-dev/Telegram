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
<img src="https://cdn5.telesco.pe/file/gykUWV9XQUAdp5Fx016ugoCslTVVqdkFyOXxBLquj_Viia63rMxXvTnjrMv9ljaeEOmcuJUn8JbWb9ZfFO_YTFiD5q6TQocY4hy5QHS7x3srDT_tDN3Mh_Vv4wWh2KY3ev0HKy06nJuQ3f-93v4vMaX7h1Qb67crqMVNMpBduw8UzFMm0UDOzI8Nn8juyXGB797GlFwlkABSk0xHpWxXdsP9JwfwVPBK6YC9nLMHkoUOFc3xJGzcH1ZMshbCJMsm1VacUf0R5qDT4hNaksgXUPYdszyi-Usddt9gbG_4kDF_StvhSibv6DNP48i6ToN5Dzq_W28j7yzOec6UXpQdDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 383K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 05:31:08</div>
<hr>

<div class="tg-post" id="msg-108650">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/Futball180TV/108650" target="_blank">📅 01:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108649">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q9Xp9ZCFkMMFSyjNT1snvDM76XMThrv0bz9EEOnnq6jRkgL8V_2OhkmKDDdJPZd5mGcSVlrMfkg47TMnY6MUFlMpd48cPuSPFcxZd2P0HkqVUxFvBhELXYgBqiwyyL6P1AMqyqMsMpiufUQfJqhKHH6OoIDzmYR671rV_nLz2mgyPtHKlui3cQyn4_SEO0jbWHBvkApAsNtBLqNkv4NBswO0tkcPhEv2FpnhSK8pGtBVvJ1SeIKd1NlDCc3AGqqf7DEPbXmm2Dx5DIOiJe8NRd-0_Mv9YFHbVK5OyNuq9jLD5tGzXw417OGUFtM0Mzkfam9HBPs7L2LlInKzKKdBYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/Futball180TV/108649" target="_blank">📅 01:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108648">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/Futball180TV/108648" target="_blank">📅 01:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108647">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umsottd_yq9PLsI2BmyNIcj_dwqu8GQOL7Sp_Z1uhWRRRJBpaQVlKZ5eVCHI_82ziszezUHot4eENmt6n1IK0U2l3uSSkqSizVKLvq_gyQBcl2ykN0QnlQookB6Msy7jTVWy-pFlDI9qLXFoZniu_i9A1KXOq9RvekzV5ewU291fS-QSSGuIX4W7xGsNGpxgEExvmjD7TUUTe6g8uK_G3hjNiw9M6fDVQLuxaNHk-Zy3ncB8Hts6_yf4uV_ivJqTFINLXMHjDdB49h1B97h7cCn0J0PxZuKh5pyYSF4vKKYoACXhBl6zvzILPZklCBT4-y6fCZNH52GNzHMJxgVwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🏆
هفته‌دوم لیگ‌قهرمانان اروپا؛ دهمین برد در دهمین بازی فصل؛ جهنم استانبول هم مانع پیروزی پرگل شاگردان فلیک نشد
🇪🇸
بارسلونا
😀
-
😃
گالاتاسرای
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/Futball180TV/108647" target="_blank">📅 00:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108646">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDhyz7jYl0odsp3u_Bl_U3h4p9AhtOgRSsk25Iw-E4kzh508EB1DPyg0YnvT3q3uIDbMgebbX9-bhKE5rGqOtsxNcIydK9P-o6aW7-bVwRoDfzYfWv-ZzkfZ_Q9xCHB-yPZmMmKLZuE_XKc8bA0d6Tl3hOoRxjF2uEfxMBhdKf9bXhdn8FGlFoHN-5oAp14JpL-FqTRqYFmtD_DHtutNrxy3O7GcsZyBFVS7uwYTz14WDpP-r7CdoA6mOz_CtNgRmADlnRJJPq_64NtjADLqWk8qPcIM9A5wxeJPGNKbYt-7jbQbL2H4AIoiAnHkdLmsMv-CznggoNRI-IkiYG6SMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/Futball180TV/108646" target="_blank">📅 00:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108645">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOEDo-mtGJSux_gGu1mY6UsQsZw6JwAkNQYjtgqss52y1pRKosPWQPZL1Qtg51JsH2LSNSN6FO5-QVcqLBWDEiJphjE_mpH_qYqhYz3knoHCwClrATSmOxHqRabl9qk8a0ELNTFc9LoygwNJw4rNxZEYzv8s2C-gLvWrvCBl1Ip_EegGWrm9C6Yvs7wHUUzClnYaNQ5XT7KRFoC3G827upBCFe3PoXZKh_mC72hrrM5hudC_kaShel2-4Q-pIg7wxTamzAkT9eWkIjozEdkP-sU7DsHXNOJqED8y0qBQ3-4g0QWB8hrbGSi1EcN3-UFsTMR_L0Vafmuk793GYDPFWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
لیگ قهرمانان اروپا | در همان ثانیه‌های ابتدایی غافلگیر شدند؛ وضعیت کریک در منچستریونایتد بحرانی شد
🇪🇸
اتلتیکومادرید
😀
-
😏
منچستریونایتد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/Futball180TV/108645" target="_blank">📅 00:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108644">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk72JtSFBnmotXM4RxiqNO71kmhhyMiQBM3hsgAEv0syWEvGOSqu_OUtQev7aK_ABmrV0x6G2JOgCSpwkyOlfzWfIA71YPlAJXxgoKhCXnmN6K4idWywRnDnvFTE1vUbz-tnfy9c_9G0rWuZbnbPHhXeEU9MxJ5nkRqwKWhcbZvzeAIVmSlzJH0R_qv2zPpefUJcy7ViOoX41-ceYvXmRUejfd7Ym3pGcaNR7GOmuQGECzXmEy_rzuWABQPkbGtddy59uBXMJnfh-gzemp_h0JU1_YYCXAbTsZ1kaEKuoCe2-uPjjfACaKuH_T2yfYtEE4GOTxxipiTspqObnfEJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
لیگ قهرمانان اروپا | تساوی دور از انتظار بایرن‌مونیخ مقابل نماینده نروژ؛ توقف شاگردان کمپانی در دیداری جذاب
🇳🇴
وایکینگ
😆
-
😆
بایرن‌مونیخ
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/Futball180TV/108644" target="_blank">📅 00:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108643">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKwDeJ77CXYpFwzmH7NCv53ytCmruglOQyQHATOcelMzlElhlBLBfGQczbJ8qAE5fSaI_ivBt5wpG4hpkapKnm4Tw8lqLns6HV6GpJ_sNw4ASAGBJxoQBc80RnUP99GcxKT9EdKsSV-UpkoHPiOIoeLzbMq3cH27VKcFM0uNOM6JrbnflNIPJYn7b92NZ00JB20WtHeFZK-Z12EbvAvxF_hk-HHhvWVLo7R4sReqAOjGvKof3_7wzaTFlZI1IZ0tgSSjAm5PH0awiW4-Edu7Fg4XQM4WXcBxdtywY2veqeL3AA3PC93IJ4I1_rBAjqu0e2AVtIsec-hqyRi_Qbu7Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🏆
هفته‌دوم لیگ‌قهرمانان اروپا؛ دهمین برد در دهمین بازی فصل؛ جهنم استانبول هم مانع پیروزی پرگل شاگردان فلیک نشد
🇪🇸
بارسلونا
😀
-
😃
گالاتاسرای
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/108643" target="_blank">📅 00:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108642">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/def4417737.mp4?token=oPkUa_DQt-FlPRzp8p9ZioCEgKUez70GReE0XUUTQJgyFJ_xQelSdH_FHeD3-Cr19bouL0A2k-KGoyZEUSeTWR8mrINrkmAlazKH_UwpTfvu4EVNgJUjfv7FDWSmmheimNXffoslhs43nIYIMixBlFyJWN-B0ANk_ogFvbS7-cpbJOFvgKCQJlB77neYIY8boIOEryrze7xJgObNS8qQK-wdzQ_q24v-t-TpheL8QT_chyEQYRQUzOt_44oVxKMT7u_znVjUgxV-u7NHNYJ0Sjmtm0uMH4mLnZZ4KswZ-qt3hCF6kwNA1EooYTi_aCWSlVSpNHrkT9IXg_4BYvE7KLXP1oABE24ImzQedoktiVxIt0ua4TN9TlzyYDijuB_gpTaaceLD4Sf8HRkFFXiOxdIn6WFQfy4Mz1tTvKz4J1yKnFcZShFMeha_BTGGcp4nLoeufUXNSZhV69a7Is-XefBX4Y_rz1XrHXww46lXXsaEcHaONu98y4yK1ehJ_uLmz8SWc58QhvF8TNxAbUuPYeiL1fS9hO8vSeNMBNYctU96OJEj08sLFcez9mMEaAnt9TCAMY9HM3P5UjlVVgGrdJCvSZcXs_ly3AWTv0xXVk-h9qLCuEAWgK2qEsqW1w8chuo8Ogjx1XFd7yROCFftT6K8YwZ6UGNUepdHH8W0Gw4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/def4417737.mp4?token=oPkUa_DQt-FlPRzp8p9ZioCEgKUez70GReE0XUUTQJgyFJ_xQelSdH_FHeD3-Cr19bouL0A2k-KGoyZEUSeTWR8mrINrkmAlazKH_UwpTfvu4EVNgJUjfv7FDWSmmheimNXffoslhs43nIYIMixBlFyJWN-B0ANk_ogFvbS7-cpbJOFvgKCQJlB77neYIY8boIOEryrze7xJgObNS8qQK-wdzQ_q24v-t-TpheL8QT_chyEQYRQUzOt_44oVxKMT7u_znVjUgxV-u7NHNYJ0Sjmtm0uMH4mLnZZ4KswZ-qt3hCF6kwNA1EooYTi_aCWSlVSpNHrkT9IXg_4BYvE7KLXP1oABE24ImzQedoktiVxIt0ua4TN9TlzyYDijuB_gpTaaceLD4Sf8HRkFFXiOxdIn6WFQfy4Mz1tTvKz4J1yKnFcZShFMeha_BTGGcp4nLoeufUXNSZhV69a7Is-XefBX4Y_rz1XrHXww46lXXsaEcHaONu98y4yK1ehJ_uLmz8SWc58QhvF8TNxAbUuPYeiL1fS9hO8vSeNMBNYctU96OJEj08sLFcez9mMEaAnt9TCAMY9HM3P5UjlVVgGrdJCvSZcXs_ly3AWTv0xXVk-h9qLCuEAWgK2qEsqW1w8chuo8Ogjx1XFd7yROCFftT6K8YwZ6UGNUepdHH8W0Gw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بایرن‌مونیخ به وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/Futball180TV/108642" target="_blank">📅 00:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108641">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گلگلگل سوم وایکینگ‌ها به بایرن‌مونیخ</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/108641" target="_blank">📅 00:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108640">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdfe06f9c.mp4?token=TXBLzMOoE3jdWlPwbhSJz1ED_FSZ_c3FeOsdItl92gEEvNYXYDHCFNiq_S9_pe7UDRYlOSxAG2qKX4P3zYzmc1mJ7ZImPV29hPb5rjote-TDW2iV2n1xOUo_5f5kCz0pSICkK914l0Fd9mTW6byEr_DmXaeSHcLhIHZFWgdOdn-EzZMOnG_OtfikYHqN3bPuxKbqppa_arCv427Rw6F5U1CSZm2rO_zrH7VRuBBR0oNj09BWGGZGZ5NSBcpe7Vxv0w-EjOl2XKDRKFCMKj-RIdx6DMZ7BCmCJkvYqgVa6sVjngvVL-ht1OBNPHT-Vz1g8H3je2bR0z9IFveHuYqRFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdfe06f9c.mp4?token=TXBLzMOoE3jdWlPwbhSJz1ED_FSZ_c3FeOsdItl92gEEvNYXYDHCFNiq_S9_pe7UDRYlOSxAG2qKX4P3zYzmc1mJ7ZImPV29hPb5rjote-TDW2iV2n1xOUo_5f5kCz0pSICkK914l0Fd9mTW6byEr_DmXaeSHcLhIHZFWgdOdn-EzZMOnG_OtfikYHqN3bPuxKbqppa_arCv427Rw6F5U1CSZm2rO_zrH7VRuBBR0oNj09BWGGZGZ5NSBcpe7Vxv0w-EjOl2XKDRKFCMKj-RIdx6DMZ7BCmCJkvYqgVa6sVjngvVL-ht1OBNPHT-Vz1g8H3je2bR0z9IFveHuYqRFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم اتلتیکو مادرید به منچستر توسط لوکمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/Futball180TV/108640" target="_blank">📅 00:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108639">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گلگلگگلگلگلگلگ اتلتیکومادرید دومیو زددددد</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/Futball180TV/108639" target="_blank">📅 00:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108638">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d76e2a5b60.mp4?token=MzHsEGS4MkDqSPF76hr1GMaP-_sFxx0XwVlH9hAYoKSQtlKl13MxruUfihUNM0zApKnxnfWqT-QyTa2cnrs0y6uwKL0GQiZXvc4fxkDypeUAUbWmTdt2IVaV5FxcTFeVF5S61bAe6mnKbtbWjPW7kmWVBZEnkVvdwbaRedRCZP_tujvC8QBZU2ggcoQ9ZIXujUdZ5JS6L0OJrgDMqJKFJB_WMG5r3Xnry0FyfdN-c28rXNGqFZXiyIVzX0s-4pirFc6U-WqiD58-xu2MB7VmL15zmp1Y8kD5R36wFbhUV4_jWepvr7A9_SWBMD172yy1e0pX6AK3MnWqomoZMDOLwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d76e2a5b60.mp4?token=MzHsEGS4MkDqSPF76hr1GMaP-_sFxx0XwVlH9hAYoKSQtlKl13MxruUfihUNM0zApKnxnfWqT-QyTa2cnrs0y6uwKL0GQiZXvc4fxkDypeUAUbWmTdt2IVaV5FxcTFeVF5S61bAe6mnKbtbWjPW7kmWVBZEnkVvdwbaRedRCZP_tujvC8QBZU2ggcoQ9ZIXujUdZ5JS6L0OJrgDMqJKFJB_WMG5r3Xnry0FyfdN-c28rXNGqFZXiyIVzX0s-4pirFc6U-WqiD58-xu2MB7VmL15zmp1Y8kD5R36wFbhUV4_jWepvr7A9_SWBMD172yy1e0pX6AK3MnWqomoZMDOLwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بایرن‌مونیخ توسط لوئیز دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/Futball180TV/108638" target="_blank">📅 00:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108637">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🟥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لنی‌یورو جلو اتلتیکومادرید اخراج شد</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/Futball180TV/108637" target="_blank">📅 00:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108636">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🟥
🇩🇪
مایکل اولیسه بدلیل دریافت کارت قرمز بازی هفته بعدی مقابل آرسنال رو از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/Futball180TV/108636" target="_blank">📅 00:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108635">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گلگلگلگلگگلگلگل سوم بایرن مونیخ به وایکینگ‌ها</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/108635" target="_blank">📅 00:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108634">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b2a48903.mp4?token=o3HcMvOgCAaxhCuibBPndT4r-nOzVWm7buwshPpUhX96JVv_IFhDjV9BFJsY_536Cc5ERIoIfQOR29wCqcFpTWVZQ6nmm5u1jiUpZ7pk-lE9ZoRu5_0ASZdYI3e_Xksi7kNqLkuj4_K_VGKzL7iJnrZG0iezQYqUsJUf9bPVZNA8vIYh9u8xGVPPzwOy1R6b2auhTV7RZVi58CVnY8SfwxaILJs2QtIC_bajBW4Qe-gk1NpRG0gMLQeMu9CVNKnJp4UH8r6LqWCi6h5_zrYuWh5T_ugORi1pve70lff68xw-OY0tUNvYFDuDlMwnsBnppcysik-YV-wtAbBSBe8s-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b2a48903.mp4?token=o3HcMvOgCAaxhCuibBPndT4r-nOzVWm7buwshPpUhX96JVv_IFhDjV9BFJsY_536Cc5ERIoIfQOR29wCqcFpTWVZQ6nmm5u1jiUpZ7pk-lE9ZoRu5_0ASZdYI3e_Xksi7kNqLkuj4_K_VGKzL7iJnrZG0iezQYqUsJUf9bPVZNA8vIYh9u8xGVPPzwOy1R6b2auhTV7RZVi58CVnY8SfwxaILJs2QtIC_bajBW4Qe-gk1NpRG0gMLQeMu9CVNKnJp4UH8r6LqWCi6h5_zrYuWh5T_ugORi1pve70lff68xw-OY0tUNvYFDuDlMwnsBnppcysik-YV-wtAbBSBe8s-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌چهارم بارسلونا به گالاتاسرای توسط آدیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/Futball180TV/108634" target="_blank">📅 23:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108633">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگلگگلگل سوم آرسنال به لیل</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/Futball180TV/108633" target="_blank">📅 23:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108632">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پاس گل از گابریل ژسوس
🔥
🔥
🔥
😂</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/Futball180TV/108632" target="_blank">📅 23:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108631">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گل زیبای کریم آدیمیییییییییییی</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/Futball180TV/108631" target="_blank">📅 23:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108630">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گلگگلگلگلگلگگلگلگل چهارم بارساااااا</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/Futball180TV/108630" target="_blank">📅 23:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108629">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگگلگلگل دوم آرسنال به لیل</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/108629" target="_blank">📅 23:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108628">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHfDk9wu3NhTwLv4lDwZ7zDMvqqg_kT9KT--nOMBjpFgJ-4ERmyC0FESSFCGcpnpwjHfGu-EOoNHN-SwuoyDQI5gGGkc8tj4Gu-LmY2MiSKDCU5uFR6JuYaKYdmy1kOOjoWBjfI2U_vpV46iZffezYB8d2SKbv-D_3zt5Ixk2gUVGDSvAHDAni_wxRreTReqL1GWORCPdYgQ4cWNX2R10Ytc3G8mK6H65Qhswpeq0nEn_6sJwL8Hd0x_vGE_ISWzbohQDjvakdVxr5YOBPvHUGwLYJiFodPLFvrbASv8XgSGPejVTnLbmk9li8h4RxNwvgjnMERcx06hmhY31Pizhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
▶️
🇪🇺
نتایج بازی‌های تا این لحظه</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/Futball180TV/108628" target="_blank">📅 23:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108627">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگگلگلگل آرسنال یکی به لیل زددددد</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/108627" target="_blank">📅 23:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108626">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf53f669cc.mp4?token=DEpXi532pjSlesqTsmxhyhUlZEQ6655KFqljxNlg4Mj7Xc55fxBgsjIW1ZuDqhGrtAohhqfPHvXhXxvGUgPzim082HKTlcvjccLUDk2zD2mu3h5NtLl5FH4PPsorpb9yVIB91kvDFPn4-zjZIVaRhu1QTuTu6EvW4_SzDqnVnOYnphm0x7g9lbZ90Z2VoD5ZB1_VWPjzO_I14XHXrSKBh_qbwJ3I4hyjcsmmRVDn76t5_w3bIX_ToxKwVU4xKnA2fa37JxvisLLm7JVZd29J3rLBDIe4Z5ZNK4w8p3kNvMrVqUZA05e36RSPKDz81aYuHfS0mDUsRqn-H-R2rUZOg3bJ1DfPnLcYCHwAxdP8CVr7o2Un8B9UGG-AwHCK1Bo8cEzo-nrgDMf7s1PYwX9FfJCXpPZwloe4FctLZXPArF2uQRDvLVuVFXh5jNZ9e5BhtS2I0UCdvdLcqJR5OKhehXPEbdifcBWPUIxTcuWnQg6tUPwuyGJdqXjDI5MSVYjW5YojMdFwwqsdWoMY8UCaMkC6KzmeTYfIk9uztbAtdTA0EwleVy0NVeHdRQ6Xyt4RgxB1p0n3anrRngujsSLwH-gNk4hCgc2I6hK0k1qV2yfkAP84sPoeQdixaZhtRRJQLAWh6QSw6vV3xbEmxMLp0P-ZLB0SiTmY82zTHP7kRJU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf53f669cc.mp4?token=DEpXi532pjSlesqTsmxhyhUlZEQ6655KFqljxNlg4Mj7Xc55fxBgsjIW1ZuDqhGrtAohhqfPHvXhXxvGUgPzim082HKTlcvjccLUDk2zD2mu3h5NtLl5FH4PPsorpb9yVIB91kvDFPn4-zjZIVaRhu1QTuTu6EvW4_SzDqnVnOYnphm0x7g9lbZ90Z2VoD5ZB1_VWPjzO_I14XHXrSKBh_qbwJ3I4hyjcsmmRVDn76t5_w3bIX_ToxKwVU4xKnA2fa37JxvisLLm7JVZd29J3rLBDIe4Z5ZNK4w8p3kNvMrVqUZA05e36RSPKDz81aYuHfS0mDUsRqn-H-R2rUZOg3bJ1DfPnLcYCHwAxdP8CVr7o2Un8B9UGG-AwHCK1Bo8cEzo-nrgDMf7s1PYwX9FfJCXpPZwloe4FctLZXPArF2uQRDvLVuVFXh5jNZ9e5BhtS2I0UCdvdLcqJR5OKhehXPEbdifcBWPUIxTcuWnQg6tUPwuyGJdqXjDI5MSVYjW5YojMdFwwqsdWoMY8UCaMkC6KzmeTYfIk9uztbAtdTA0EwleVy0NVeHdRQ6Xyt4RgxB1p0n3anrRngujsSLwH-gNk4hCgc2I6hK0k1qV2yfkAP84sPoeQdixaZhtRRJQLAWh6QSw6vV3xbEmxMLp0P-ZLB0SiTmY82zTHP7kRJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی بایرن‌مونیخ به وایکینگ‌ها هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/Futball180TV/108626" target="_blank">📅 23:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108625">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">لوووووویز دیازززززززز</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/108625" target="_blank">📅 23:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108624">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">لوووووویز دیازززززززز</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/108624" target="_blank">📅 23:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108623">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گلگلگگلگلگلگلگلگ سوم بایرن‌مونیخ</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/108623" target="_blank">📅 23:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108622">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هری کین دبل کرددددددد</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/Futball180TV/108622" target="_blank">📅 23:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108621">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بایرن‌مونیخ مساویووووو زددددددد</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/Futball180TV/108621" target="_blank">📅 23:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108620">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گلگلگلگگلگلگلگلگگل</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/Futball180TV/108620" target="_blank">📅 23:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108619">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/93ba7eabbb.mp4?token=jzi8ZMA0-cVCVrHswgu35PWwC-B1lM0BgltlL4ulpmepDzOjzJ-TPhw9gsI0ej98CCR1qpML_qXT9BQsh0_RwiJYynnF63k0RZfJkEMzjAev47iyG8eUG62lsCW2s-QqkrmYfLLa3uD1a7qQTTkQIoQB6Uke967DmULCmxaCipbhpp463DJyqSCgZBML-Lw3ri-OGBiiiqmWlxpm_Q8kNHa4eCMcVTV7pQQ8K6KG3ycudOziFZRqHpnEl11k2IAaUEg0bJ0BpebwfFFG4RXmDah4d-jTHv48Wch347MWR-QbnjZQwlfGFlZFsb9GWf2pska9-m-mNjWtiG463k-Uj45Xo0YMGDQZjALIWeJShb3Y3jTxUzRs4PnsF08w9XnuaCf6dzPdnW8IpfI73kJqP92yagarCGTWN_fIlFHevQ8XLGC3SZq7lSLNsffNP3faqItIu59eJixsGL3GHjrDmKh3kCvo9gq8za8Fr1TCM2fAh_h2UeDCpLR09JcBSlqWsHC0gSaPsjpqw8gVclMtkzpebolCADyBGJh8dLSDbLWF1WkyGmBST-65aZiPRhYhqgV8wQt-CYKjPLH1L77c0lGfVZsvuMHKbam3vOoKa-vIgJbUrcML_RssGmLgM4Kr9bhoTVFQvt2KbCIXYzUCDNhOPKP5Atnq6SmEkEDZGnU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/93ba7eabbb.mp4?token=jzi8ZMA0-cVCVrHswgu35PWwC-B1lM0BgltlL4ulpmepDzOjzJ-TPhw9gsI0ej98CCR1qpML_qXT9BQsh0_RwiJYynnF63k0RZfJkEMzjAev47iyG8eUG62lsCW2s-QqkrmYfLLa3uD1a7qQTTkQIoQB6Uke967DmULCmxaCipbhpp463DJyqSCgZBML-Lw3ri-OGBiiiqmWlxpm_Q8kNHa4eCMcVTV7pQQ8K6KG3ycudOziFZRqHpnEl11k2IAaUEg0bJ0BpebwfFFG4RXmDah4d-jTHv48Wch347MWR-QbnjZQwlfGFlZFsb9GWf2pska9-m-mNjWtiG463k-Uj45Xo0YMGDQZjALIWeJShb3Y3jTxUzRs4PnsF08w9XnuaCf6dzPdnW8IpfI73kJqP92yagarCGTWN_fIlFHevQ8XLGC3SZq7lSLNsffNP3faqItIu59eJixsGL3GHjrDmKh3kCvo9gq8za8Fr1TCM2fAh_h2UeDCpLR09JcBSlqWsHC0gSaPsjpqw8gVclMtkzpebolCADyBGJh8dLSDbLWF1WkyGmBST-65aZiPRhYhqgV8wQt-CYKjPLH1L77c0lGfVZsvuMHKbam3vOoKa-vIgJbUrcML_RssGmLgM4Kr9bhoTVFQvt2KbCIXYzUCDNhOPKP5Atnq6SmEkEDZGnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول بایرن‌مونیخ به وایکینگ‌ها توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/Futball180TV/108619" target="_blank">📅 23:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108618">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c86178bbb0.mp4?token=bs6uJ4WNEGSUI7OPcie2Rqr2vAvDjGb-mHIozxTIErCVwPH3vON5gfSxTzyBgu_IpbnHGe6XxQ7qC-gEcYryYPSpeJZlESo_hrYDMtVeB-wawczW3I1Q52M6vzGqZMnmjuLUEmb-lx_U4dbVQwifksopkzWE_caN0FMDAwzfpuP5bNNKYWdhBJ1bgSn_OZCGnJKo9L6DkqQ0N13qAnQj9oECstKkRDpzWI6I5O4Czy78MKUwdduJracgsN6ZnIE5meMgUDtyR6nAlcSXQSg2gTZTv4TX3JAlJ7Rc0OfHzyUdRoDEMFAG02h-sxG2Gh8SwGpuoj84wt-vLKQEhVfT-Sqvn_SSqzzBZZBxTDi5LreroUiPaeWFIN1ytgzFofwADFiTr-Zmx4KunxZe7pEwrwGHNCZ31Trcw2aduZmWyECLSiuXd7YAsCIMPQiS_D_gLqEPOVadeUO4J9sA9NPMcMlCGCiSc3yNnRFhPD_bJ_zdZKu8cGj7tfIOcej1U-Lg_2rThQOzyzmhkPvBCs3X_lqv8Cqw5Umq7fY6MMlUfL9B8AjVb97f8zY5jNjAdmVTsRACc4fUaZ1M7xU8itl57Ebi80KaAKbW9C9i1ZmHWFz7v4YbUN5AQ3hxN9istD7WoZ7ETCl-FtMqUglV-IWIqf9MkaXqt726LmcEJEujg48" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c86178bbb0.mp4?token=bs6uJ4WNEGSUI7OPcie2Rqr2vAvDjGb-mHIozxTIErCVwPH3vON5gfSxTzyBgu_IpbnHGe6XxQ7qC-gEcYryYPSpeJZlESo_hrYDMtVeB-wawczW3I1Q52M6vzGqZMnmjuLUEmb-lx_U4dbVQwifksopkzWE_caN0FMDAwzfpuP5bNNKYWdhBJ1bgSn_OZCGnJKo9L6DkqQ0N13qAnQj9oECstKkRDpzWI6I5O4Czy78MKUwdduJracgsN6ZnIE5meMgUDtyR6nAlcSXQSg2gTZTv4TX3JAlJ7Rc0OfHzyUdRoDEMFAG02h-sxG2Gh8SwGpuoj84wt-vLKQEhVfT-Sqvn_SSqzzBZZBxTDi5LreroUiPaeWFIN1ytgzFofwADFiTr-Zmx4KunxZe7pEwrwGHNCZ31Trcw2aduZmWyECLSiuXd7YAsCIMPQiS_D_gLqEPOVadeUO4J9sA9NPMcMlCGCiSc3yNnRFhPD_bJ_zdZKu8cGj7tfIOcej1U-Lg_2rThQOzyzmhkPvBCs3X_lqv8Cqw5Umq7fY6MMlUfL9B8AjVb97f8zY5jNjAdmVTsRACc4fUaZ1M7xU8itl57Ebi80KaAKbW9C9i1ZmHWFz7v4YbUN5AQ3hxN9istD7WoZ7ETCl-FtMqUglV-IWIqf9MkaXqt726LmcEJEujg48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌سوم بارسلونا به گالاتاسرای توسط گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/Futball180TV/108618" target="_blank">📅 23:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108617">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c2159385.mp4?token=kzJDp11S8lTGILVIei4WUaH9fZmZz_Y_KrKAAHSDW1qtx0DzDPGUmUwjXoIKBKBIa154wfnLJfRWuvm6MhvDLJcR8DHJLUkCKLcgHIHAU43Ba7Ni37Lb70yiMtUsKSWf74iqeBQjSygniXl4gPW76TnltpF0QC8UaWjt5O6Aslt-o4yqAiNrB5BRbzKsRhjm8cLouSs1lyfNSQgjC7JpqLallaG2DrS76ngwZLqH0B6mB_zf6_HT4_aswL5zk4P_fNAGyhq_YYhGxFZkr8lM6pXpB40AMSXc7ASqguDb78iutmgXIYmVsiHWAaxQ65Ybll0u-YQ2MP3tPtQ7o4Krzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c2159385.mp4?token=kzJDp11S8lTGILVIei4WUaH9fZmZz_Y_KrKAAHSDW1qtx0DzDPGUmUwjXoIKBKBIa154wfnLJfRWuvm6MhvDLJcR8DHJLUkCKLcgHIHAU43Ba7Ni37Lb70yiMtUsKSWf74iqeBQjSygniXl4gPW76TnltpF0QC8UaWjt5O6Aslt-o4yqAiNrB5BRbzKsRhjm8cLouSs1lyfNSQgjC7JpqLallaG2DrS76ngwZLqH0B6mB_zf6_HT4_aswL5zk4P_fNAGyhq_YYhGxFZkr8lM6pXpB40AMSXc7ASqguDb78iutmgXIYmVsiHWAaxQ65Ybll0u-YQ2MP3tPtQ7o4Krzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم بارسلونا به گالاتاسرای توسط لوپز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/Futball180TV/108617" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108616">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سوپر دریبل و حرکت فوق‌العاده یامال فقط
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/Futball180TV/108616" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108615">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آنتونی گوردون</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/Futball180TV/108615" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108614">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بارسلوناااااااا</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/108614" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108613">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگ سوووووووم</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/Futball180TV/108613" target="_blank">📅 23:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108612">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گلگلگگلگلگگگل بایرن‌مونیخ یکی زد هری کین</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/Futball180TV/108612" target="_blank">📅 23:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108610">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سوپر پاس گل لامین‌یامال
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/Futball180TV/108610" target="_blank">📅 23:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108609">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فرمین لوووووپزززززز</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/Futball180TV/108609" target="_blank">📅 23:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108608">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/Futball180TV/108608" target="_blank">📅 23:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108607">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گوردون دروازه خالی زد بیرون
😂
😂
😂
😂
😳</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/Futball180TV/108607" target="_blank">📅 23:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108606">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSuQO8bpxeoPbyVEY26dy4ec3XjW2duChquyk954lseqRuMWsYTZmLgp3nu2AqVqFBzhAGfGcZTDFSRAX7MDn56UdgxZA90eIBFvdgqjTU4NbGL1oua43WJkUz_QhxeD6Gxlu8MGnVXrp5HVXVaqBRfAme2voJYUx6cDwoITVWhM_BCI9LMrPBlQJy_DQWgnHU6HdpR5h8ZW01VHr7hLzZYs3fApiyaA5ZrOVzs3-8czpsgpDFAxGPcc9HX39pcL6Kz2KETUTriMfk1yMK9m_o_K_X1oT-yLowv7LT2t4SuLpEwuo6eRRdh6V03pDdxk_xwFOYm73h_gD3KOPTs-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج کامل نیمه‌اول مسابقات امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/Futball180TV/108606" target="_blank">📅 23:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108605">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گلر گالاتاسرای ۵ تا گل خریده برا تیمش</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/108605" target="_blank">📅 23:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108604">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78ba46272.mp4?token=hpC2RqokiX0kZcFxnDVQ3pzzK2UhXLzCLbzE9FZmEFlLk1P7-1KbvkYzeeqVXGbHw7okimxkmACQ5UNSkLA4FDgdHa8FPmVD3BavSDaGaqoxrRp9d-WmNNKgb2E27Bt1cEmElZ9iLDaSU7S0L1ujB3L8DYG5an0SPwyxHGyTP6RwtKqbWfbwRwy5qERV1eOM69V5YNyrGBiVWiqTbA_EC926L8rfbXftVyb1Q51qt7CAWAAKM7-JjbUf_jBnNt7DggR8o4aPAFiac18bq_dsRFjZtaEFxjdR2fO5XViZ-EqOGE4AiKG_-OsX5RcIJLoCjQ18AECMYpF6Bq6OxGoWSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78ba46272.mp4?token=hpC2RqokiX0kZcFxnDVQ3pzzK2UhXLzCLbzE9FZmEFlLk1P7-1KbvkYzeeqVXGbHw7okimxkmACQ5UNSkLA4FDgdHa8FPmVD3BavSDaGaqoxrRp9d-WmNNKgb2E27Bt1cEmElZ9iLDaSU7S0L1ujB3L8DYG5an0SPwyxHGyTP6RwtKqbWfbwRwy5qERV1eOM69V5YNyrGBiVWiqTbA_EC926L8rfbXftVyb1Q51qt7CAWAAKM7-JjbUf_jBnNt7DggR8o4aPAFiac18bq_dsRFjZtaEFxjdR2fO5XViZ-EqOGE4AiKG_-OsX5RcIJLoCjQ18AECMYpF6Bq6OxGoWSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول بارسلونا به گالاتاسرای توسط کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/108604" target="_blank">📅 23:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108603">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اتلتیکومادرید دومیوووووو به یونایتد زدددددد که رد شد</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/Futball180TV/108603" target="_blank">📅 23:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108602">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گلگلگگلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/108602" target="_blank">📅 23:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108601">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رفته وار داره بررسی میشه</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/Futball180TV/108601" target="_blank">📅 23:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108600">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رفته وار داره بررسی میشه</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/Futball180TV/108600" target="_blank">📅 23:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108599">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اسطوره ژائو کانسلوووووووووو
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/Futball180TV/108599" target="_blank">📅 23:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108598">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بارساااااااا</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/108598" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108597">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/Futball180TV/108597" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108596">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d28a95756e.mp4?token=gKOptxnmLS-iKfFPHdsRTRndo14lVgzXsadrEU9Bgl9Hh4BaddemOpdk4QER0uRu2FEkt-NyNU86uCRJ-JdlnWIw0elIe9W7QQIf8uFb8BvSvc6aWh__GDIVrpQCSWSOn25Bxr6oldquNVGYyyDcI1ItVa9P6eCDJHS1sRB9XCJyaQ6QSIrabuGVDm64iZHCQTKqstYyP5Ek5N_I4lohE7ow33ocWh6sqs769LqNBzkj_3ZKQlE3UumwZVvL1DYk527e60FKkkHQqEtHBopfn5UvoRsf-H8RtjwmmusDx8dglYA8VSSDz9L18HobKochCGKL4QaeZfE4R1sORYnRfx4DdZgALfj_2dPJ2GDMjE5rWxIwG3KY9CF8k0Jnd-yJBp7vIj7qshM5KeWaowaIwqSKJhJS3GICgzY8nRbYSnkEXMWsPdTBOjJvlbFSO_8EoAoK0b0skPdkGta3BEb2WiPXqsxYOL32wJtaZBB1cIuB52HwwQoYKgaAHCvP08zLtdbHyshcMla6MjN_NB5HVeNOFGKZ0f_pCuN6aIExExYvttEdwTjM8wsNw_Qdf3f5TVPcDyly_Kx7kg4zZ5mVcCIWFP0ikyyGJAx87kurjXu0wZqew5Vxswc4PYt3CRcny98IRBQSGHilqHZ7OK0q-SFhBCUgtNt8LnSLx80PDp4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d28a95756e.mp4?token=gKOptxnmLS-iKfFPHdsRTRndo14lVgzXsadrEU9Bgl9Hh4BaddemOpdk4QER0uRu2FEkt-NyNU86uCRJ-JdlnWIw0elIe9W7QQIf8uFb8BvSvc6aWh__GDIVrpQCSWSOn25Bxr6oldquNVGYyyDcI1ItVa9P6eCDJHS1sRB9XCJyaQ6QSIrabuGVDm64iZHCQTKqstYyP5Ek5N_I4lohE7ow33ocWh6sqs769LqNBzkj_3ZKQlE3UumwZVvL1DYk527e60FKkkHQqEtHBopfn5UvoRsf-H8RtjwmmusDx8dglYA8VSSDz9L18HobKochCGKL4QaeZfE4R1sORYnRfx4DdZgALfj_2dPJ2GDMjE5rWxIwG3KY9CF8k0Jnd-yJBp7vIj7qshM5KeWaowaIwqSKJhJS3GICgzY8nRbYSnkEXMWsPdTBOjJvlbFSO_8EoAoK0b0skPdkGta3BEb2WiPXqsxYOL32wJtaZBB1cIuB52HwwQoYKgaAHCvP08zLtdbHyshcMla6MjN_NB5HVeNOFGKZ0f_pCuN6aIExExYvttEdwTjM8wsNw_Qdf3f5TVPcDyly_Kx7kg4zZ5mVcCIWFP0ikyyGJAx87kurjXu0wZqew5Vxswc4PYt3CRcny98IRBQSGHilqHZ7OK0q-SFhBCUgtNt8LnSLx80PDp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم وایکینگ‌ها به بایرن‌مونیخ
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/Futball180TV/108596" target="_blank">📅 23:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108595">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بایرن‌مونیخ دومیوووووو خورد از وایکینگ
😐
😳</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/108595" target="_blank">📅 23:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108594">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/Futball180TV/108594" target="_blank">📅 23:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108593">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
گل دوم مردودددددد شدددددددد</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/108593" target="_blank">📅 23:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108592">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صحنه رفته وار بررسی بشه</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/108592" target="_blank">📅 23:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108591">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کوووووون فلیک داره پاره میشههههههههه</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/108591" target="_blank">📅 23:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108590">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گالاتاسرای دومیوووووووو زددددددددد</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/108590" target="_blank">📅 23:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108589">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/Futball180TV/108589" target="_blank">📅 23:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108588">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a56bd8725.mp4?token=Xz7yZs7s5c9DcfrcrLDqlNn9-0NiyW59SDpyz9y1YTXNWxnGaHnDXlGqSyDykoKhORlY9YiVGiGXLPUn2jcR9rLjMDLtMUp_mjsjd6CxFJ9QEoY8haAvxGzl5-R62Mt4wzfL-k5jmfUO0e8JXVU3O0J0PTVHBkrQo3bTFQNgf4wikx_x0lbXNQANs4UhvjGtOgb-kLwMYZatFqPESPzd3gX4X5QNNC9zSmTyYvnUayjCiicj5xgKDS-dUakqCQeTLVh0Pd_kEry9cZSm8QgbZzqG1bd2XojSiZYnGWLi9aHzQ-zh6yZiIiRdFBHZPjQIL37I7rlkOJboa2uIem9xsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a56bd8725.mp4?token=Xz7yZs7s5c9DcfrcrLDqlNn9-0NiyW59SDpyz9y1YTXNWxnGaHnDXlGqSyDykoKhORlY9YiVGiGXLPUn2jcR9rLjMDLtMUp_mjsjd6CxFJ9QEoY8haAvxGzl5-R62Mt4wzfL-k5jmfUO0e8JXVU3O0J0PTVHBkrQo3bTFQNgf4wikx_x0lbXNQANs4UhvjGtOgb-kLwMYZatFqPESPzd3gX4X5QNNC9zSmTyYvnUayjCiicj5xgKDS-dUakqCQeTLVh0Pd_kEry9cZSm8QgbZzqG1bd2XojSiZYnGWLi9aHzQ-zh6yZiIiRdFBHZPjQIL37I7rlkOJboa2uIem9xsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇹🇷
گل اول گالاتاسرای به بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108588" target="_blank">📅 23:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108587">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گالاتاسرای زددددددددد</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/108587" target="_blank">📅 22:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108586">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گلگلگگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/Futball180TV/108586" target="_blank">📅 22:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108585">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">لیل یکی به آرسنال زد</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/108585" target="_blank">📅 22:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108584">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">لیل یکی به آرسنال زد</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/108584" target="_blank">📅 22:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108583">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گل‌اول وایکینگ به بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/108583" target="_blank">📅 22:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108582">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee25b8b605.mp4?token=V7Pplt24joZwCtUDBtZCh5YnGq4NeY_Fk5aQlWkGZPRed8WFD-d-nXS8o2Dx9EpwCHEhyPnSCEEFlolGzv4Ufr19VNi8sH5uDPE0XLGquKZ5N7JPo6iwsgJDK7OLzTksZVZzP72xKlieDMLtby0ZorAGrguZebP9wKsth4OvjsP12FZM9cQirFX8v74ioDSGAEeJm-6DPWQI6oC87Rqp0_erRixq9oj2s7Gf3Lfpn4ExKKhk16THjaGYBETfH-cRvLL2TOETD2vlLpcDRBCB7qOW8Avmr4IPUGjVO-TlPRpGGj7XkpNz66Q-ZRhsNhn0Dm1_swCrClQxAMhflW1RgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee25b8b605.mp4?token=V7Pplt24joZwCtUDBtZCh5YnGq4NeY_Fk5aQlWkGZPRed8WFD-d-nXS8o2Dx9EpwCHEhyPnSCEEFlolGzv4Ufr19VNi8sH5uDPE0XLGquKZ5N7JPo6iwsgJDK7OLzTksZVZzP72xKlieDMLtby0ZorAGrguZebP9wKsth4OvjsP12FZM9cQirFX8v74ioDSGAEeJm-6DPWQI6oC87Rqp0_erRixq9oj2s7Gf3Lfpn4ExKKhk16THjaGYBETfH-cRvLL2TOETD2vlLpcDRBCB7qOW8Avmr4IPUGjVO-TlPRpGGj7XkpNz66Q-ZRhsNhn0Dm1_swCrClQxAMhflW1RgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
به نام خدا و گل؛ گل اول اتلتیکو مادرید به منچستر یونایتد توسط باریوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108582" target="_blank">📅 22:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108581">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گلگلگلگگلگلگل اتلتیکو یکی به یونایتد زدددد</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/108581" target="_blank">📅 22:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108580">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بایرن‌مونیخ یکی از وایکینگ خورد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/108580" target="_blank">📅 22:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108579">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/108579" target="_blank">📅 22:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108578">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">برررریم سراغ بازی‌های امشب لیگ‌قهرمانان اروپا</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108578" target="_blank">📅 22:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108577">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
خداداد عزیزی سرپرست تراکتور به مدت ۴ ماه محروم شد
‼️
امید عالیشاه نیز ۴ بازی محروم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/108577" target="_blank">📅 22:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108576">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnaksNmSrqLUMKVrbinHkRWami6w77umYZ1MGDl7nul5bv0aLpJCq_zb27_1_biwIRd9qEQk6BgzJy73AZ7AN323FbSUbIqTFc6ET5wAIQGCgj1SGN0oVvhnJQcqvc_O0jUO8uz6Xg0rLE694TUxRMiBeAWSTN1dn2yS5HVRstJPFwrFKOKUi17ylTJJxbalPDDoJSvPB2x5axaQqU3PRmPlJqn9hQtyZgC-TPpAnbtEj4UcYUxjhRiAbdPi6AFysrSIguMniHs1UM_PrBKwHEfRgiGdxGDa_fTo8aafVLPBMLII794l2YJJc5rwAvLIjeFl67dM8L5peotSq-lZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب آرسنال مقابل لیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108576" target="_blank">📅 21:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108575">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaJ0DGBh2SvFYNh_gXdzenrzuVXBQM1luQHOoFLv86cfEzmFT_R3gbBDcCwyLMxrzdkxhNTwgiS8Dk87EHlIBP9dF1aTjwXlSxKVVaphUwvaBbGwecXxCQSNl87htBInFTN35YkPN5Wecbfo9UjD4_Jkv8pI0gvPFID8Fl2hw89XFkFSfhkOb4V001GsxgRcpWkvW0weYSPd-Zf-KoWRT-VFAz0nbl-kQhOpmUA4FO-vHJkE5NhcOYpb4l5wV2rx3P0ia7wRuqRfwfas8BXMAFPjmTBDrrtw9iAW0ZTEE2Ck3aovz-Run4AuXNa4Lcy3-8GVkGDb9x00z7t_yEgmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇺
ترکیب بارسلونا مقابل گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108575" target="_blank">📅 21:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108574">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13c928814.mp4?token=FxWwu65w3CqnStdJ_zEaCYTqhSGEcdnTbOMLlan42jb6Iwf39XuB4ayi-YiQVAZ9yKNwQvkbXT1cbrOES-TLzXfH9w3tjhC6IWS1dC_5pAC3cMZX2Q3pfYcEedM4ybimKAqUhqArK2iKTr8V-F7FjaLkbZ2vaC-AqlsvOtC-25bKwLSWzdaxlyruvzMqXrqZk6A-C6mbYXVTqADsXnEgQ_xJ0UagL5Qk391HLMkoUj0-2n23oErufjN_I9vw_T16XQ5g0_InAAQg06ep8gzZRw4hKttPxUnb0mWIssEr1J3BmLuCT7iUVa68iGdZUe2XAjY1SjHNeD5LrfA9Y90clw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13c928814.mp4?token=FxWwu65w3CqnStdJ_zEaCYTqhSGEcdnTbOMLlan42jb6Iwf39XuB4ayi-YiQVAZ9yKNwQvkbXT1cbrOES-TLzXfH9w3tjhC6IWS1dC_5pAC3cMZX2Q3pfYcEedM4ybimKAqUhqArK2iKTr8V-F7FjaLkbZ2vaC-AqlsvOtC-25bKwLSWzdaxlyruvzMqXrqZk6A-C6mbYXVTqADsXnEgQ_xJ0UagL5Qk391HLMkoUj0-2n23oErufjN_I9vw_T16XQ5g0_InAAQg06ep8gzZRw4hKttPxUnb0mWIssEr1J3BmLuCT7iUVa68iGdZUe2XAjY1SjHNeD5LrfA9Y90clw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇮🇷
آسیا محو تماشای یاسر آسانی، سوپراستارِ آلبانیاییِ استقلال.
😧
🔥
☠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108574" target="_blank">📅 20:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108573">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kg7t--2paRONAHuAgPMaWN8cIqX3OYT4g_4CduievUEQm6R_yu8xj4d7-Vy-eUKK3eyd28QKj2ZZgI-ODQOAQWrsUslUpGm8eVD63qIFaQrdQD6hiCHmzY8CAjjAsyxJGtRwssQAylQUyAVPtPNiLe0oDCYc77NLz_E5Nrh8q6-rDNDqXgxm5U5vELec2oLQz31Cy9JxZDHXD9l-x6bJ30e0tdmMrqiWOySwyHzt06mjUb2ekoQtKZlchBkiFXUmZgRxGPgUTIQYmyVhRKpeZ6ZrY0zJ45xImwqDxXXg4hLx_jC1REI7auGQ0lbsjFTiwuSpH6Z_Gq2wzCuukzdGsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اسپورت: دنی‌اولمو امشب مهاجم نوک بارساست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/108573" target="_blank">📅 20:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108572">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94fdeb1527.mp4?token=TuDEBfZpyl-iUFZlxoiy4z06WH2JVbJYHXRbUt89s-HFerzDaFWtDx2UiB8J577CZYblRbMHaUwbEu0RGpci8dZJE2iTntKBRojFHHsaNqJLkD723_EjIU7XLDU95f-ldDvU-UZKX-s24H8l5rFjPDyst09AtfQ2D-sdCJ-TZrZ7-qg1ujRBP-CEYVcL5HoM-bj1Xo9Ut4rFiLyy9iEDKbxnSvzep0jzdNqR05f_Pkyel1CEn8yxYe2WFmq05aG5V94XYKeKkrCJMZqMMBLsYjO1Z7wgHW0msEpHnPdpsvkV6LBXGrrfu26d3WcCffPEJwpnPqUVFNwceHHd4YeB0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94fdeb1527.mp4?token=TuDEBfZpyl-iUFZlxoiy4z06WH2JVbJYHXRbUt89s-HFerzDaFWtDx2UiB8J577CZYblRbMHaUwbEu0RGpci8dZJE2iTntKBRojFHHsaNqJLkD723_EjIU7XLDU95f-ldDvU-UZKX-s24H8l5rFjPDyst09AtfQ2D-sdCJ-TZrZ7-qg1ujRBP-CEYVcL5HoM-bj1Xo9Ut4rFiLyy9iEDKbxnSvzep0jzdNqR05f_Pkyel1CEn8yxYe2WFmq05aG5V94XYKeKkrCJMZqMMBLsYjO1Z7wgHW0msEpHnPdpsvkV6LBXGrrfu26d3WcCffPEJwpnPqUVFNwceHHd4YeB0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوبه که فرد ذلیلی نباشیم
😨
😨
مثل مسی اسرائیلی نباشیم
😳
😳
دوشنبه؛ ۲۰ مهر ۱۴۰۵
📍
میدان انقلاب تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108572" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108571">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7ec7a32c.mp4?token=R81tn_YQMLDRd_roYppTc20vGpDWcQ-Gr9OfUk1VHBcQIjPZfvoRhN_N2RN4GzdqNMq2h-TBo3hcR0QubTRqd_OzTTqenui94ISg1pQqSqBF_rbQXh06x-y-KFZxGVz4ZCuEkUiR-VrtKvs0OmBBfq8ECDGFEA2NKRVJ8Xr_pj_mVwCTUu5DErfkRWq6CoUbBI1718u2APw0FW1IOLYTQtTNRPqfpnu186cmnf3oBBKHV4jX1lF04-p1JuvRKvSrEotLowHO8I5wxGgJgSSqv2tAioeSwKh8HEc3tN9hjCzhLaqS8gUyL57gjdutxoEix1K2ahe5cQ8a6BfllFYIWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7ec7a32c.mp4?token=R81tn_YQMLDRd_roYppTc20vGpDWcQ-Gr9OfUk1VHBcQIjPZfvoRhN_N2RN4GzdqNMq2h-TBo3hcR0QubTRqd_OzTTqenui94ISg1pQqSqBF_rbQXh06x-y-KFZxGVz4ZCuEkUiR-VrtKvs0OmBBfq8ECDGFEA2NKRVJ8Xr_pj_mVwCTUu5DErfkRWq6CoUbBI1718u2APw0FW1IOLYTQtTNRPqfpnu186cmnf3oBBKHV4jX1lF04-p1JuvRKvSrEotLowHO8I5wxGgJgSSqv2tAioeSwKh8HEc3tN9hjCzhLaqS8gUyL57gjdutxoEix1K2ahe5cQ8a6BfllFYIWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوبه که فرد ذلیلی نباشیم
😨
😨
مثل مسی اسرائیلی نباشیم
😳
😳
دوشنبه؛ ۲۰ مهر ۱۴۰۵
📍
میدان انقلاب تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108571" target="_blank">📅 19:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108570">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75009e0b9.mp4?token=I-s4r8MYDXDVCXOdkjcmzD8n-51WKmQuJb2fbeN9xN6ZdmOgKcuzTXO0cnwTCfyn1v74Gzm4ZEj0HuUNrG5InqBxnurd8SL1KgIRiaweHFgm6h7GvdCacvQV4tr0r_PVlwJb0xXQEIYs1BTFl-uiKWKCLJ-9LDh06q0loihIiyUxZ4zNu6BmJD_MB90jzT5TDLW6KyTBylcFYCXv10bxronQT3qq2fZNa7PzmWq0A97uxD5--_rMj79I0f9oSVO7D9lI7OXe4YpzriXAYJ9uuYpiaWjYNllN4ULJ00fMLsMbaqX64_2sTdoMFVWNWBJ1NOhyixJzlKXw_1i_tX3kMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75009e0b9.mp4?token=I-s4r8MYDXDVCXOdkjcmzD8n-51WKmQuJb2fbeN9xN6ZdmOgKcuzTXO0cnwTCfyn1v74Gzm4ZEj0HuUNrG5InqBxnurd8SL1KgIRiaweHFgm6h7GvdCacvQV4tr0r_PVlwJb0xXQEIYs1BTFl-uiKWKCLJ-9LDh06q0loihIiyUxZ4zNu6BmJD_MB90jzT5TDLW6KyTBylcFYCXv10bxronQT3qq2fZNa7PzmWq0A97uxD5--_rMj79I0f9oSVO7D9lI7OXe4YpzriXAYJ9uuYpiaWjYNllN4ULJ00fMLsMbaqX64_2sTdoMFVWNWBJ1NOhyixJzlKXw_1i_tX3kMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باند سفت‌های استقلال از یک فلافل شکل گرفت:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108570" target="_blank">📅 19:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108569">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9aa2627f.mp4?token=v1eUnFfTpEJTIHBMfGTmsjlaLuG20Qwyhwi_BBC-DzjLn9yisYBEVbMMdn3Pm69KfJZbQ8C2Hd4eIkHsZTvKnCoXY9Ywumuy9HuK4D683upePImno8qivmuYUh8WupKQnlP-7erNXwb72fQrp2vAVQ28q1FuWInm6NSauob0ukj73jgMIfmiV53jtqZwhsBhc6M9T0oo_Zp6MIVH8YELZAyBYiVLnXDrkKyQHGhfKdGdUZF013UrnpOne-smhmzrZms7eAmLnwuTp9NJm5_DTHvIYTiR7dZdaO2VLEkzaIEfur76pvzhZGDn41Spu-osPPO2zwYd3MEX9aG7vtoJyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9aa2627f.mp4?token=v1eUnFfTpEJTIHBMfGTmsjlaLuG20Qwyhwi_BBC-DzjLn9yisYBEVbMMdn3Pm69KfJZbQ8C2Hd4eIkHsZTvKnCoXY9Ywumuy9HuK4D683upePImno8qivmuYUh8WupKQnlP-7erNXwb72fQrp2vAVQ28q1FuWInm6NSauob0ukj73jgMIfmiV53jtqZwhsBhc6M9T0oo_Zp6MIVH8YELZAyBYiVLnXDrkKyQHGhfKdGdUZF013UrnpOne-smhmzrZms7eAmLnwuTp9NJm5_DTHvIYTiR7dZdaO2VLEkzaIEfur76pvzhZGDn41Spu-osPPO2zwYd3MEX9aG7vtoJyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
روایت خوبان‌عالم از بخور بخور در فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108569" target="_blank">📅 19:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108568">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce5d2d95eb.mp4?token=KctGP-oH5tySVrysqL9569QYbNZcoHVs5oWo3kzcv0uY1TNIUnk6Bvu0mZxlI-KJGI-kSz-i1Uqqv59KpLVcWAaN2SNmDNFnPX0QIYECxlXKujxq1WGBErXKo4orEHqlk_3ui37k-Sl3t339ahy069yU5NJXyWY8ebvwUhMuQuLSYljQCf7W6o-qutT3ImTZVmsHWlK2W8gTsJMhp5wdQREiao37EtIi21DvUE7c7r34jchfuBR2wSRFU30ZgZQwtqh6j9MU58I3dR4fzIhgMTNM8H35yhoC1nflXsp70lT6a6xCQ_OBhaHgnZt0mvpmyMQJ6uqS6C4HbSYEfi03BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce5d2d95eb.mp4?token=KctGP-oH5tySVrysqL9569QYbNZcoHVs5oWo3kzcv0uY1TNIUnk6Bvu0mZxlI-KJGI-kSz-i1Uqqv59KpLVcWAaN2SNmDNFnPX0QIYECxlXKujxq1WGBErXKo4orEHqlk_3ui37k-Sl3t339ahy069yU5NJXyWY8ebvwUhMuQuLSYljQCf7W6o-qutT3ImTZVmsHWlK2W8gTsJMhp5wdQREiao37EtIi21DvUE7c7r34jchfuBR2wSRFU30ZgZQwtqh6j9MU58I3dR4fzIhgMTNM8H35yhoC1nflXsp70lT6a6xCQ_OBhaHgnZt0mvpmyMQJ6uqS6C4HbSYEfi03BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
⚠️
شوخی سمی ابو‌طالب با کات‌کردن آسانی و زنش و احتمال کامبک: واسه خودم اومدی یا چون که یاس شدم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108568" target="_blank">📅 18:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108567">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ds83LbkT-jb-N6U3Ru6dP9Gq1W6TtAkjjIn0i8FHv16vNbuHVfWsC_cFH0tkY46ZQdrW9sFQ7LqY6c7IqEZhD0wWymPaW9qJB2-1dLxQJAciNKz4ZOe4qyPt7ZXNYblctF1A35v14vKPZ4xyBzVEF9SGhgglPUwTgIXQU043x3MwbzpK8bwXapGVgXM3NxjRfjCyqcRGpfNlKC4jdbUg22HhxTHHAIZFXVQxGTk7eqTdIWjJiH_BawGGv6yJ6knzEnQsDlxdcUus8NNt0DknSfl93JjzBUERCGzlku_3Knvz7Ju-CZl5qs81tq75vBWYTOkYrj9Ak--A3j2FYx39Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
❌
لیونل مسی قرار نیست در مراسم توپ طلا جامی را به هیچ‌کدام از برندگان اهدا کند؛ چرا که برای این کار از او دعوت نشده است.
❌
حضور مسی در مراسم توپ طلا هنوز قطعی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108567" target="_blank">📅 18:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108566">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa1WngsGmgnCl5xVRCH8yF99Qv9AKRP4TbiQX-x9e9PTqDW5ZMF9cGfHx8NB_34JrRRXWEdYW6O7pxC4KeJtWuxE3Ng-At8yJGxsJxYgWtvfcMcwjWYN5RWu5-T3QCLu4VjLrp6UZV-ORmD5LWz4XhgMGqZQhtpQTrUpkfQxNBZxhGKz59cJe72ogklqKj5ans6FzhsmFlQ9Y2nsBgK6YUu1mDXPVbAxVu3FvFAdj-RGkQznTQ_2YNxXYca--EZn_rivUrdUG-5znx1S7k_xHc05scPMytsyjcTE0dzye0nC1t6t6AVdlky-yvSoTLGib9_YzxPIYBNABo8MA95pQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیگ برتر ایران|سپاهان فاتح دربی اصفهان شد
🔸
ذوب‌آهن یک - سپاهان دو
⚽️
گل سپاهان: محمدمهدی لطفی و کاوه رضایی
⚽️
گل ذوب‌آهن: امید لطیفی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108566" target="_blank">📅 18:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108565">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108565" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108565" target="_blank">📅 18:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108564">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiRZGOmv9awIUDk2F5kBNFcxLaNNFMXYFD90XnJckoEYCDFWw6wm9LSdfD1Wi9sHPHX4vpmx_uLm7juN8Dd3UXWpNdvCrp9QS5d-DE7kcKODJdmSMK_NScWuq60jjSB5AGJPXJ381Ezuf7kON7yYgfPn3U8K-3FLxTH-m3JcafbNQ0WVDu3fhw0YJtq93jlFZ01hIJVi4-h5_QQKJaaN11Z4wDRq0lQbm8jmQeCyWqvF-YpCTzWCVDr6_5ScSJz9grQOd5E9doGMzwNA8cBzdNMaPoe25VMUX9yYlPMlm5flLoM9YDPM37xdYBQJRNTLJH654s5iPP29km9MQ5I6oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منچستر یونایتد
🆚
اتلتیکو مادرید
🦖
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۲ تیم
در ۵ رویارویی اخیر :
منچستر یونایتد : ۱ برد، ۲ تساوی، ۲ شکست و ۷ گل زده
اتلتیکو مادرید : ۴ برد، ۱ شکست و ۱۲ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108564" target="_blank">📅 18:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108563">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19588c007.mp4?token=K-Jf4TAP6eKUVNIEiJMl_096k1MoxlakbpwddShKwsHbPunmIeiKGdwreaWHcsbE5J0NkTSbsT_6V1X3dmRMmvbNa15WAZp2AAAikyoq-DkG3i9KHf16s-rAm8a11Fz2C-pAKvwTxvDReUIqH3RZCQzRbVAgxHp-YvW7BX02mnc5gjA-8mygMh-DJO4qlSqckeCC216GXOVDluiSWKH-A4K6peCYYcg4fhn9hJjOHlwdTA3XH8NX7LPm9ql9XTa5QQygxR1KDc--_O1EuX-hQS89nzVZJw13BqUanVarokIuV0ZU4Rmb7I1JRP0w3ijwbyfYjqKsdVQuj_Z966u51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19588c007.mp4?token=K-Jf4TAP6eKUVNIEiJMl_096k1MoxlakbpwddShKwsHbPunmIeiKGdwreaWHcsbE5J0NkTSbsT_6V1X3dmRMmvbNa15WAZp2AAAikyoq-DkG3i9KHf16s-rAm8a11Fz2C-pAKvwTxvDReUIqH3RZCQzRbVAgxHp-YvW7BX02mnc5gjA-8mygMh-DJO4qlSqckeCC216GXOVDluiSWKH-A4K6peCYYcg4fhn9hJjOHlwdTA3XH8NX7LPm9ql9XTa5QQygxR1KDc--_O1EuX-hQS89nzVZJw13BqUanVarokIuV0ZU4Rmb7I1JRP0w3ijwbyfYjqKsdVQuj_Z966u51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
هالند و یک آمار عجیب؛ او بر خلاف امباپه، در تله آفساید گیر نمی‌افتد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108563" target="_blank">📅 18:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108562">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a34457cfa.mp4?token=Po730qki8KyrxjkulZF19U5Q-IfXpQqGCVyvVsZT08ow8uFheO94TGoKd41rETaNWZZEBjNKCmno3sw6-rYAViN_6WhLzfWS18kZRGiih5UqjkYJ3IpvIqHGsc5xy4GoC4c0-HecujtwLeExVoRARlh2LFj0i0N9uIzcQWucyUc-E_VEH_2zcA6fd5H4TbmNGMcb6C9Z9rRhB9xEkL-7sKfQ2SmMaljvfKkcjCVCjm4OrAUrpU9upt2Hk2nknymptfMCzRYEwxq6URrGpykBfHv4IOjE4J5aZF4sWcpU9j6wV6oVcX1RQ8MvwV_un3pBT9jJYJpfCHMEwEW8jJdTzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a34457cfa.mp4?token=Po730qki8KyrxjkulZF19U5Q-IfXpQqGCVyvVsZT08ow8uFheO94TGoKd41rETaNWZZEBjNKCmno3sw6-rYAViN_6WhLzfWS18kZRGiih5UqjkYJ3IpvIqHGsc5xy4GoC4c0-HecujtwLeExVoRARlh2LFj0i0N9uIzcQWucyUc-E_VEH_2zcA6fd5H4TbmNGMcb6C9Z9rRhB9xEkL-7sKfQ2SmMaljvfKkcjCVCjm4OrAUrpU9upt2Hk2nknymptfMCzRYEwxq6URrGpykBfHv4IOjE4J5aZF4sWcpU9j6wV6oVcX1RQ8MvwV_un3pBT9jJYJpfCHMEwEW8jJdTzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ده نفره گل زدند
⚽️
لطیفی دقیقه ۸۴
ذوب‌آهن ۱ - ۲ سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108562" target="_blank">📅 17:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108561">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGL0VqNZgrHHUk8852gmn7LsOUgie41o6rqE3xn2QEYwXJZwo6bcNKf4RZg_jlef4y_QbcBUchXzzw3zRFbr5-0arcSA0V-oloSc22dpY6Vj_uektFN34EphY5iF-6AfZjpc-98if5uV8b5kewW3QHrGLR4HQKVuNNDGVOBHKCgj4TX7e0-vP39erDhlV_-mAN1MdLzZaJcp3TOg4ep-Fq5PqKi2vntF-eNm3nRCdbRvNMuyIWzNIyJmtNKfhFKIWL6DQocI5-UfoiT-pf9cGvKDU3S6cmqCq6rJLIEmYd2HqS0K5IZ5rWBJc-De-yiaaIodDqBctN5_W8BYklnPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نسل جدید خط هافبک منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108561" target="_blank">📅 17:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108560">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57b850047.mp4?token=RBhCfFZmo_OoUTeF-4-j7iZ9W3sggslI8Y8Pk0BnjwGp4qqo582XovWrQLdUR9dSFrZkJbiK12FvkasMA9HKrRKUevgycjJjqYdJ5Q4UYcwI8q0iIZIdy5lhy_ZDWlc7_WMBk1goW39boAx2aVQPplhTRo3GfYyyiy1m1lgM3SS2_AKxp2aQbwHyL7RZhbDbMAhA4BHrlZbfkHxpU1J-us7vyAgAFMaNB2c1Vnh7jMdBcwumg-jUOvzxYV_cHxkBtD4tbJ6r3LqDnYPMidTtXSBhxgsEhveMUSItRQCykvN8OofhNMZvejkoXa1NdKJa1ndg0x7UWoOfCd3C_9gF2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57b850047.mp4?token=RBhCfFZmo_OoUTeF-4-j7iZ9W3sggslI8Y8Pk0BnjwGp4qqo582XovWrQLdUR9dSFrZkJbiK12FvkasMA9HKrRKUevgycjJjqYdJ5Q4UYcwI8q0iIZIdy5lhy_ZDWlc7_WMBk1goW39boAx2aVQPplhTRo3GfYyyiy1m1lgM3SS2_AKxp2aQbwHyL7RZhbDbMAhA4BHrlZbfkHxpU1J-us7vyAgAFMaNB2c1Vnh7jMdBcwumg-jUOvzxYV_cHxkBtD4tbJ6r3LqDnYPMidTtXSBhxgsEhveMUSItRQCykvN8OofhNMZvejkoXa1NdKJa1ndg0x7UWoOfCd3C_9gF2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
صعود تضمینی برای تیم اسپانسر داوران
ماجرای عجیب صعود آرمان آفرینان به لیگ دسته اول نوجوانان با حضور در رده هفتم؛ دلایل فرافوتبالی برای ۱۹تیمی کردن لیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108560" target="_blank">📅 16:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108559">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ca58a516d.mp4?token=D2_SoYZG9Q6WIOWTlcBoadjSVPMgip-MfNjbISbQnvl7tgbzbHfPK1xyXyjyKHCG151ZyjQHZaahaJiIPFzcEjNc71lyRcB0MNBG-HNoeZB9wsSh3fOCq1bH0ZchIQLdb2xtErc2tsrmJUC2Ln-ZWhwzZCiW6lq94QosxPWajoqMLpw80YuZRBSnzlmvcFZKdFtGRLOCjnl-Nk28w3JukbbNms9zi6_Uf9NimZtDJHhxg9HTaNzytHWeB3_IZKQcGQzrMR1fWmsPMJ4dOh1FQy4eD49uXTqgcLKYxSpQaRbG85TG_ASF9iKGu180btchLII3_bpiseOx5ulxZvvHaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ca58a516d.mp4?token=D2_SoYZG9Q6WIOWTlcBoadjSVPMgip-MfNjbISbQnvl7tgbzbHfPK1xyXyjyKHCG151ZyjQHZaahaJiIPFzcEjNc71lyRcB0MNBG-HNoeZB9wsSh3fOCq1bH0ZchIQLdb2xtErc2tsrmJUC2Ln-ZWhwzZCiW6lq94QosxPWajoqMLpw80YuZRBSnzlmvcFZKdFtGRLOCjnl-Nk28w3JukbbNms9zi6_Uf9NimZtDJHhxg9HTaNzytHWeB3_IZKQcGQzrMR1fWmsPMJ4dOh1FQy4eD49uXTqgcLKYxSpQaRbG85TG_ASF9iKGu180btchLII3_bpiseOx5ulxZvvHaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
اخراج محمد حسینی و 10 نفره شدن ذوب آهن مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108559" target="_blank">📅 16:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108558">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54bb3822ea.mp4?token=mV6ROKB6EWe-MQTe86fxj6T867rZCRU-ORxTBp9wW7_0O6IKYL0veChcBDM-eRoFBCl1RDu80S4PUSslQ9piAnL0tJxan_T9mg_FxWYlsxZqbWRGtvEsj0lPTN-LqFTU1cgF91JlAjavWDklocM9Ms1nlZJCfaDCJ36n6ST23AQjVobMG0Q0dzC9SgwIsUIc7WqxUirP4CMp9YHkcaDTcq-F99mm4vgFJm8NQTPZcK11Uidt8rlCAgKN2Aj6W6VPxex_cQaKsleEpl6v8cFY4uqi7-2Skr4oaG-0YzbNxU2jncoS59yTGzIu76WKpFre9USubg07FKYr8Lj6K3AmyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54bb3822ea.mp4?token=mV6ROKB6EWe-MQTe86fxj6T867rZCRU-ORxTBp9wW7_0O6IKYL0veChcBDM-eRoFBCl1RDu80S4PUSslQ9piAnL0tJxan_T9mg_FxWYlsxZqbWRGtvEsj0lPTN-LqFTU1cgF91JlAjavWDklocM9Ms1nlZJCfaDCJ36n6ST23AQjVobMG0Q0dzC9SgwIsUIc7WqxUirP4CMp9YHkcaDTcq-F99mm4vgFJm8NQTPZcK11Uidt8rlCAgKN2Aj6W6VPxex_cQaKsleEpl6v8cFY4uqi7-2Skr4oaG-0YzbNxU2jncoS59yTGzIu76WKpFre9USubg07FKYr8Lj6K3AmyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🟡
گل دوم سپاهان | کاوه رضایی '23
ذوب‌آهن 0 - سپاهان 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108558" target="_blank">📅 16:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108557">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108557" target="_blank">📅 16:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108556">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WxUUGEQTnfE105jB7F7EfcQDNEFPqdjMgPUQq8v0BdJv8ZYMtTNpVX6lNAV1ZJULDQoVOIdHlQz_jpIbAVtrOb00ubb2IFX4Py5bTB0oOvM0EElII1G9L9nS3Dj3jm9VtOeejFb4q9pnYQldeJS9xdnrbx9xg3WqJ14QrxEUl6agh8zAUAHSuTrQ70AUgULZAtB3Nq7Yyym3OyBv8i8xsupwYGrl2uf5bk2m3CgLkF9hi_CpQ9QGpm2Dfp1aDiQZif_lZwViIFTkuUdhH9E4PdQ5a-38HiDaoa2mcl8v5ZGIF0d0RM8xEJHsCZa9EbMP15mWQRqmxalZRpXuUQJ8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108556" target="_blank">📅 16:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108555">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5299108b84.mp4?token=g85IZXUOP8Xh-nOdTSK4JMSOq6qWjuTN-i-jZMJn1poaKGzpUWdIPFXaiCk2C8YPQXxbDeOfHOuxmlvRavhkmyXZq0k8Qu48pR3WreWgEc6XYHJwfOHIGvPNbTZpBREo15Qjqmnr4_w1ZVXGSpIhG_1LIoxZqkPiBwCxqrAlxuQAUsEefJx3arlaeVxbBP2jixE4LN7j1S_9JhsPArfF18jEu4ThfBXo2sb6TQ979jYcmocSVVKYhYrWlIlvIFTsAC2MQABFU9UoKeLmgDrc16JQ8Cu6MTMuZUexp5InmSIihHNBO9UpBd8QpTvXdJuX35FzxwkWfGsC0HzIYpHsdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5299108b84.mp4?token=g85IZXUOP8Xh-nOdTSK4JMSOq6qWjuTN-i-jZMJn1poaKGzpUWdIPFXaiCk2C8YPQXxbDeOfHOuxmlvRavhkmyXZq0k8Qu48pR3WreWgEc6XYHJwfOHIGvPNbTZpBREo15Qjqmnr4_w1ZVXGSpIhG_1LIoxZqkPiBwCxqrAlxuQAUsEefJx3arlaeVxbBP2jixE4LN7j1S_9JhsPArfF18jEu4ThfBXo2sb6TQ979jYcmocSVVKYhYrWlIlvIFTsAC2MQABFU9UoKeLmgDrc16JQ8Cu6MTMuZUexp5InmSIihHNBO9UpBd8QpTvXdJuX35FzxwkWfGsC0HzIYpHsdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سپاهان خیلی زود به گل رسید؛ لطفی در دقیقه ۲ گلزنی کرد!
⚽️
ذوب‌آهن ۰ - سپاهان ۱
گل: محمدمهدی لطفی '۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108555" target="_blank">📅 16:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108554">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263d796f58.mp4?token=nlGJIPDQYm7Gqb0TI1QxW9CjhXe2x6_UhThmBwgutRHyiyBFQ8JUKJPLZo0iDCIey43Dl9NzoD1C-E4-PH7HmfGSyArG_-a4Z7vqX-Ud7AyYgY_z4xzCb8wDEf4fUZJWBWUZzBzaqH6K1rkEu9GLnQUXY6S-tPqR7Ztc7rsRyMES61b3ObBGmX8w_U_xIMD27qgK4M2rY0TY9gEtQCPc_o2EsoJEAiqC57QFwUuwzEEmR7ZANLbsz1v-GR38c2z3z6JlO_v9MUWJ9HVfncbVAfpgGrFOLo184t0vwUv4X5UF_Npcw8MccrB4HW_S_xiRISedeFhsilzY7MuSZFG4Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263d796f58.mp4?token=nlGJIPDQYm7Gqb0TI1QxW9CjhXe2x6_UhThmBwgutRHyiyBFQ8JUKJPLZo0iDCIey43Dl9NzoD1C-E4-PH7HmfGSyArG_-a4Z7vqX-Ud7AyYgY_z4xzCb8wDEf4fUZJWBWUZzBzaqH6K1rkEu9GLnQUXY6S-tPqR7Ztc7rsRyMES61b3ObBGmX8w_U_xIMD27qgK4M2rY0TY9gEtQCPc_o2EsoJEAiqC57QFwUuwzEEmR7ZANLbsz1v-GR38c2z3z6JlO_v9MUWJ9HVfncbVAfpgGrFOLo184t0vwUv4X5UF_Npcw8MccrB4HW_S_xiRISedeFhsilzY7MuSZFG4Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🇮🇷
مقایسه سوپرگل آرین‌روبن و یاسر‌آسانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108554" target="_blank">📅 16:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108553">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ac4b09ba.mp4?token=vAotoERhI7dQiF3yUqmZY4VQN_QXiXrHYllnx2uOe6dDimuolK4zzlxeHPqiNzlbkDVezhUfZwML7um4epyrl1kxZkzSRSb-RODvN-duGM9itMnw4D9Yl5qcI_EXdFKhvSWaQNfj8EerHu-w557LWTgd0UVfeVfY7bnZ0oB22xH2JOX1x94ZtM-g3A1jRqCAS12uMDygqfFIVXmLPPEMa4fONENB5s2xMZVrlXnowQjyFJH9ohuGy0qU62EL3bYACNYp6BgBzPACWplbPB7zuO2UacJn5DqCcXd7F8xkE_hxMCfQc3QSNNM_WmVX6xB70xcyWO2Scw-dmVB1LZOXqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ac4b09ba.mp4?token=vAotoERhI7dQiF3yUqmZY4VQN_QXiXrHYllnx2uOe6dDimuolK4zzlxeHPqiNzlbkDVezhUfZwML7um4epyrl1kxZkzSRSb-RODvN-duGM9itMnw4D9Yl5qcI_EXdFKhvSWaQNfj8EerHu-w557LWTgd0UVfeVfY7bnZ0oB22xH2JOX1x94ZtM-g3A1jRqCAS12uMDygqfFIVXmLPPEMa4fONENB5s2xMZVrlXnowQjyFJH9ohuGy0qU62EL3bYACNYp6BgBzPACWplbPB7zuO2UacJn5DqCcXd7F8xkE_hxMCfQc3QSNNM_WmVX6xB70xcyWO2Scw-dmVB1LZOXqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حمله مجری صداوسیما به سرپرست تراکتور تبریز: خداداد عزیزی توروخدا بس کن!
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108553" target="_blank">📅 15:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108552">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIVWS6n35Rx7C-je7fWjEmXK0cK45CpKiGZCPgdOqhmYB_9elU5OORdGaDIdoyxbG9hJcRptSQonAjiGsf7khh7WRcBF6f_liGulFk9xZCYJl9C8X3JhvAD2p14YldDK78PPlTAvj2Sh_HK80FiN5JzxCk9-CJdvLDBsmimGbATfBxOGxd0YPycGWzqF4TtnzADzmcwea-H8SU1Wnnr1AyOXbixjAwNU3DSFAECC5gOngrS2nDMst5Cgy4ylLpbKDiKarD80kYe-lkQi7O5dlvgMv3shyWLLrv-TTgdyMmbUsp00a2eLrfCZqmVljfcnRDYbkCTikgaGppXwW00wow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دانیال‌ایری مدافع پرسپولیس پس از طی کردن دوران مصدومیت به تمرینات این تیم بازگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108552" target="_blank">📅 15:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108551">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23eaea7cdd.mp4?token=c9kpVxJqL9T-MSECAlpRmEwUTYwaDiB6cnvLNVxd9yrnG8Pnt3wc-XS2-i6-SvMd19WrjS4F1VgHN4Kz8CcsWzBoGqdOZQoii5dNK9XeGqXLO-49XUomR7vdmgdJkDPst45sa8xKUlZwLpKkeW6VpZJEvL4t4Rx5rBXdY2eysAR-yklCuhUPD_V1wk_QE2ODQe_duaZrhRY4GedWwmpOKg0cvGNhc8Ik_fu3CQY2aF2goUvZ8ikBoJ74vCwDUHlfNajgFUOfZBL7ISM-eFffIWTjwT-4OKx-DLGZkyB-7IW_H6BH_HHTGGup_MNW1YtNyrWGPUoAp7n6CHtpYB-xGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23eaea7cdd.mp4?token=c9kpVxJqL9T-MSECAlpRmEwUTYwaDiB6cnvLNVxd9yrnG8Pnt3wc-XS2-i6-SvMd19WrjS4F1VgHN4Kz8CcsWzBoGqdOZQoii5dNK9XeGqXLO-49XUomR7vdmgdJkDPst45sa8xKUlZwLpKkeW6VpZJEvL4t4Rx5rBXdY2eysAR-yklCuhUPD_V1wk_QE2ODQe_duaZrhRY4GedWwmpOKg0cvGNhc8Ik_fu3CQY2aF2goUvZ8ikBoJ74vCwDUHlfNajgFUOfZBL7ISM-eFffIWTjwT-4OKx-DLGZkyB-7IW_H6BH_HHTGGup_MNW1YtNyrWGPUoAp7n6CHtpYB-xGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سمی‌ترین ویدیو از حرکت زشت وینیسیوس
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108551" target="_blank">📅 15:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108550">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cea75d776.mp4?token=rIuPd1e-X80Cn8OSmybCk7liFPiS6vBLgR4Y9B_GqcoV-WGQ7WtMdKqAKGqHkvGvGRBY8_DtxLtdEhKS8XmBC1GDmAULytyRg8KoKXi6iXHZpHdIpjA5VGu4eQXXWnXiwpfEVNhn-efxiJU-9FAcc7giRiVVpAjSvvgdutcPegw1d7EDJPPEaKaNcMC27Td0Js6GWY52zEUhBEDzNMr_-f7gkjkGcffjXq6aP4m0AZFRLjGBkw4-Ewr0qE8su8x7V4CQRPUzsGcaKk5NC1ajPliWnVC5xyRHOwyhsYDakXKm_gQtODRC0iS59k4Q90UhnFLiz4mkxbf3BlI2HqdGOQ8ZsJfR3XEBSE4Fji1Fd6UDVooDD87ZQvFFl0ociRirWfpxtddXAv2d-uVV-0i96FXg7UZRjGGuoHEM2rJorj_IlSIxeDb2O8MiVrpGMSpq7Gt7Qv5laH5mkHYWu3fFtkFk5B3QALXwnuswaxHfuyUuKLDVMJztYs8TffvB9cwecQLpaM_elKYBM0TP-x1rJD9VWhtpj8KyWzAVfrKZE8UGebWqs2aIHF7O1o0eo3KrV3XxeTjst9pdX1bFkfrK-Zy7_okZCar-GGOszF4FVnKCArfKSuVIJaJdVWR4NehXwv7KOrLGlA_Y1-Zu9d0teQ9ARgwiT_8jJlYfJoSPXec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cea75d776.mp4?token=rIuPd1e-X80Cn8OSmybCk7liFPiS6vBLgR4Y9B_GqcoV-WGQ7WtMdKqAKGqHkvGvGRBY8_DtxLtdEhKS8XmBC1GDmAULytyRg8KoKXi6iXHZpHdIpjA5VGu4eQXXWnXiwpfEVNhn-efxiJU-9FAcc7giRiVVpAjSvvgdutcPegw1d7EDJPPEaKaNcMC27Td0Js6GWY52zEUhBEDzNMr_-f7gkjkGcffjXq6aP4m0AZFRLjGBkw4-Ewr0qE8su8x7V4CQRPUzsGcaKk5NC1ajPliWnVC5xyRHOwyhsYDakXKm_gQtODRC0iS59k4Q90UhnFLiz4mkxbf3BlI2HqdGOQ8ZsJfR3XEBSE4Fji1Fd6UDVooDD87ZQvFFl0ociRirWfpxtddXAv2d-uVV-0i96FXg7UZRjGGuoHEM2rJorj_IlSIxeDb2O8MiVrpGMSpq7Gt7Qv5laH5mkHYWu3fFtkFk5B3QALXwnuswaxHfuyUuKLDVMJztYs8TffvB9cwecQLpaM_elKYBM0TP-x1rJD9VWhtpj8KyWzAVfrKZE8UGebWqs2aIHF7O1o0eo3KrV3XxeTjst9pdX1bFkfrK-Zy7_okZCar-GGOszF4FVnKCArfKSuVIJaJdVWR4NehXwv7KOrLGlA_Y1-Zu9d0teQ9ARgwiT_8jJlYfJoSPXec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی رامین‌رضاییان خودش رو چشم میزنه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108550" target="_blank">📅 14:50 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
