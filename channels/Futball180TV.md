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
<img src="https://cdn5.telesco.pe/file/jlSAiZedoNi25chbWgZLm-dhx9nW6ZejrJPs3XaReOyfP9XbswbV6NhO6fQGe-wfkuu8FdnK0z_ib7SfEl25laCTWEZTMfOIhCI4FThEQbNEbEPMFmp8Rr612zK8GovQtDZmwfZX5oW5VUaW-I7xMJ1_omsLCqZBxuD9ytLnC5jfMpJFgOQEO6aBioytcJkqRwaXwr75pjA5PJ5PGTRYOXCTJB5RHK2607W6qFuJzfY2KbzjeO_XqRMP5kaUA_0Nss_Ns6DmBjESl3PCaDeLxGf6PvLQrC_RdGsbwuY2aa7gFaJoDH_H5ykp9-ZYY1mIx6sWrADex6Eeg732zb_gLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 387K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 03:38:05</div>
<hr>

<div class="tg-post" id="msg-108220">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/Futball180TV/108220" target="_blank">📅 01:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108219">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rQMY9uPfymkBqRw_iN7VxAXYggjqCqleCqmq6wfgm0v_DsVgzx8kDKHYrwJ-c2FHzngCWYyQoZJ_f1txtn99t_Xij22-YAG0f5MJLUq6gUxstFXTf0uyE3Ya6295MxlymDxUHU815QT4jya9HczpyIyfuu97CZKZ0OsqhUDtqewXfhpeIGaQhstIrDswrPp41H5y362DgLKFAflzBIytwYe9kqGn2BmyU6NIRAIEbOTQhFyCiB6m-UPE2j2yW2psL8_bDFO5QuldnaBVnfZ2lvbMNnPtJ0nKIS_YD35Q2qBpDbocvtzXqNGPqe1RRnWTMrznvzkiFFRck6CasRA74A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/108219" target="_blank">📅 01:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108218">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTFnB1puOvGcVzqbbT2T-BAy1Rck3WyA3UlOLRhPwZ7s78nq8vcLsluQwxBIrfHGhotRE6FqDwL_8TOvnaU68EUnwwBUr_WNwPnTPolYNX9D_9eiKza8dyDIwXoPL4KjuOkndJN6AJSrAABfGSNLY2c0oz_25W3j4nqH1OOC52dnqI6GaLrf0jd7nZVC_CGFEj2rsul7DkOsMf8VkHLLFaBuSzuMOsSRIrr7IMHLnvdIWNe0EAvj3JAXToKwkaNXhFVe4nSsOMNNBl9ili8mJU69JQRxdRnD9klLAuOzY5k_e2Zf8FH1skRdonzWpTK48w2VQZaJmoKUEQsjK5z90Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
❌
#اختصاصی_فوتبال‌180
؛
🔴
در گفتگویی کوتاه با مدیران پرسپولیس این باشگاه اعلام کرد که در نیم‌فصل هیچ قصدی برای مذاکره و جذب بشار رسن یا بازیکن خارجی دیگر ندارد چون ظرفیت بازیکنان خارجی این تیم پر است و محدودیت‌های نقل‌وانتقالاتی فصل‌جدید مانع از جذب نفرات دیگر خارجی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/Futball180TV/108218" target="_blank">📅 01:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108217">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tg0DxvcgnB7wIwmOGuyhtjQTvRhthfqFiPoR08r3axTqstwpwRUVGf6C3WkAcRaHgfgvUbpDyDAS2snhwMM4e7Jj-tN34ellDZzHKOCFB1Vz1td-pNlREgtxGv3n7AfGQXo9SO3NhIjDblxKt28XDXcTcs3qNrAwE-yo-uVvU446OWGuBfO343Pu2sSAjUw-mweSUjku19v1Nqltw4nTu-OG6lClVuqCNEpYqHjxvKfs_luJrrOrnTZ8H0bNewC_xttsurHuK9wveCXQ06I5KgBFjPzw3K-SXnKsKA6697IGFU4KGFuctPe9wOP_Rt_qIutA8KhzvrKrMbhq4IXWfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
❌
🚨
وزارت امور خارجه آمریکا در توییتر: به هیچ دلیلی به ایران سفر نکنید. شهروندان آمریکایی باید همین حالا ایران را ترک کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/108217" target="_blank">📅 00:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108216">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrdXeEkVxcrGPVhLARZkRbmi3Zm-kxvn5E6pppkkidd5euFvEnVZAeWaVSK1qebeavn6M2mKeBfv35cSPYgKSJjfeQvde7Z9zSxZU1SXoNccalDg1hJt_EIxca4gX4Wo1XYalPbabLjqBaM0SpMrZrxG6YZwemg1UlgGykg8wt2nac_UTUS3mSmdzEcLctCw3SS3NCcH6Xn2XJ00fFLu3rfNqwn2OxZGvNY6E2R85IPemQNVLbUNvWAKVzanFj3WjimsA9-_sxcrDKrVZgEOir70DFxBSaJXAHNu8NExm19u2sP8R-cbHOZOdsDHjO8Isuxxq_VqI2Ql8dUxlBvz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🚨
ظاهراً سازمان نظام وظیفه به بیرانوند اعلام کرده تا زمان مشخص شدن وضعیت کمیسیون پزشکیش حق خروج از کشور رو نداره و حتی اگه بیرو با مدیران باشگاه به این اختلاف نمی‌خورد هم نمی‌تونست شاگردان نکونام رو در سفر به مسقط برای بازی با الشمال همراهی کنه مگه اینکه مشکل خروج از کشورش رو حل کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/108216" target="_blank">📅 00:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108215">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab16b6ba1.mp4?token=pJKpu_pG6qlUNC8ss04hHmp3ArmS66OTO6ZVQVGZwWIIEBzVKU20EBrP243CitJeSHKK-dmDEYF5JD34XwPeWvy3Py2ckxEYVe-DrDVx2J0y618qaUINNk5KoC_WiMJhRw4Bgp-ZLRDi8IOxIH0uneLt7fHbhDlymKF7v9wjfL2StLVjf2c2MZ7Xv19fXSKk7c-tq_wu-eaO-wvR8WJ7Abt32Y5PMkBTIJmwd6pIsDIv-qXv3NHrLqecqwnLTlGv59eVFZ-4DnMR1wdC926VbQr6iC89jyYYS1Px43242PAns4y24CYcCR7T1ZvLy_MwZDrOXOnY-cK87PPN6OJNXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab16b6ba1.mp4?token=pJKpu_pG6qlUNC8ss04hHmp3ArmS66OTO6ZVQVGZwWIIEBzVKU20EBrP243CitJeSHKK-dmDEYF5JD34XwPeWvy3Py2ckxEYVe-DrDVx2J0y618qaUINNk5KoC_WiMJhRw4Bgp-ZLRDi8IOxIH0uneLt7fHbhDlymKF7v9wjfL2StLVjf2c2MZ7Xv19fXSKk7c-tq_wu-eaO-wvR8WJ7Abt32Y5PMkBTIJmwd6pIsDIv-qXv3NHrLqecqwnLTlGv59eVFZ-4DnMR1wdC926VbQr6iC89jyYYS1Px43242PAns4y24CYcCR7T1ZvLy_MwZDrOXOnY-cK87PPN6OJNXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
آخرین وضعیت شکایت باشگاه ها از آسانی از زبان رئیس فدراسیون فوتبال: هر تیمی دلش میخواد میتونه به CAS شکایت کنه و مانعی نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108215" target="_blank">📅 23:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108214">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MicHYqf_TP5yzcqu0F5rZoGkKDZYWE-WOHd7Lp6IUQlaURzxlbLGjC-yxzJFmDftkMAfRaDb7H4wcV3FCWK-R5-hL-zE8vE0xcuM5FoMxW4A2WS_z2tNp6ZtX9ud_SE-GUeM8ETQVzQgkgwHHoqR5_r6JNMKLJhLUwcH2fGOUY71BOILpNQUeyLdnWSf1RsaRRwTYF6hTEnrGYoi-Fk148Pq0DajqXoKuk8PsRnlfwSbOa6OO_jKZ5TKNJwgV3TWyQTULOxf3tCc3rFY1tZNoCiG2peuXCUyG8_RJrdjfTOwfF8EjFlq-FynxOH_QChgCmquYXWWSookVxMUNjUX3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
فوری؛ بیرانوند از هتل اخراج شد!
علیرضا بیرانوند پس از درگیری لفظی با مدیران تراکتور و در آستانه سفر آسیایی این تیم، از حضور در اردوی تراکتور منع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108214" target="_blank">📅 22:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108213">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPAXHYKD7osi6Live77YF1H2G4028apG3QkVasMGtWV3Ue9uVZISwQP4MO80zySw6UuY9MPGp50h-rluAQYdncKJEIWS7yqFbun5oVk7o2tial4_XoQ4OfrCqwG8uBOhWHfwoagQDNktY1U9hYSVafx9E7CVRaxzcEErQYd4OZZ31Miwz5afRA6X5_7xXbNy2xBAQRJDWtvlDhCUMQkSHezemBa_Yct6a9oOJQagct2SbLEYaDbxIyjVaSuWbds_AO9lq55_kWPxNIJt5mMrvbsuhmTt5Rk61evMWFv2ah6tMst5cpNxPfa9rIlzvbYOLPWFFRAAgMwlWNHdz3TDKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
❌
محمد نوری پس از شکست مقابل پرسپولیس از هدایت نفت‌آبادان اخراج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/108213" target="_blank">📅 22:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108212">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b78fb174d.mp4?token=ALhSJ4ZrGycj4QZghXELD2mnTaDyiaYhjRtXWJoH7Cw9hvxMT5ZBjjbWM_etuYANsa0JLWUJ2qqJWpt2oFvYYI27wNNPlT3RcLVc5L-_saAA7gtJZULzMtJCPt5fKIeAczB4WVduiD2WhjqjakKB58jM0lpdL84zPkVm-5KrYk3bR_575CN0pPAdG0qTkmjMZGAAWX5iIv9_mR5wJ9BTmjG5Rry8wZ5H3x_MtwQmOBIL4jhGnOWIioitlamQ0fIOufTZO0umSSlCauktB04Mb8kNamSJ6UukjdtDyqt1njBMp-X_-KMXJTFW3CeNW0KajTSRirEVBDtNa1In9YBmqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b78fb174d.mp4?token=ALhSJ4ZrGycj4QZghXELD2mnTaDyiaYhjRtXWJoH7Cw9hvxMT5ZBjjbWM_etuYANsa0JLWUJ2qqJWpt2oFvYYI27wNNPlT3RcLVc5L-_saAA7gtJZULzMtJCPt5fKIeAczB4WVduiD2WhjqjakKB58jM0lpdL84zPkVm-5KrYk3bR_575CN0pPAdG0qTkmjMZGAAWX5iIv9_mR5wJ9BTmjG5Rry8wZ5H3x_MtwQmOBIL4jhGnOWIioitlamQ0fIOufTZO0umSSlCauktB04Mb8kNamSJ6UukjdtDyqt1njBMp-X_-KMXJTFW3CeNW0KajTSRirEVBDtNa1In9YBmqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل‌شماره ۹۸۰ کریس‌رونالدو در بازی امشب النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108212" target="_blank">📅 22:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108211">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🔴
طبق شنیده‌ها؛ باشگاه پرسپولیس مذاکرات خود را با مدیربرنامه‌های بشار رسن عراقی آغاز کرده تابرای جذب این بازیکن در نیم فصل به توافق برسد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108211" target="_blank">📅 22:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108210">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
⭕️
🇮🇷
مهدی تاج: هیئت‌رئیسه مخالف دادن جام قهرمانی به استقلال بود، ولی این مورد مجدداً در حال بررسی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/108210" target="_blank">📅 21:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108209">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
‼️
🇮🇷
محسن خلیلی، سرپرست پرسپولیس:
یاسر آسانی؟ باشگاه تمام مسائل را از صفر تا صد پیگیری می کند. داخل کشور به نتیجه نرسیم صددرصد در دادگاه عالی ورزش دنبال می کنیم. ما نگفتیم این پرونده پایان یافته است. مندیت آسانی به پرسپولیس؟ بله او مندیت را داشت اما زمان همه چیز را در این زمینه نشان می دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/108209" target="_blank">📅 20:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108208">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VF1m8kwzlpUDTlItW2b4TuSg2pSAxlmMjMukpFXXK0h1Obsb_K0O0WaOzSph5FWyV9rvKZmJ7qZ6N5gsrNBeg6CGlzpQ6X03t-qa0xp6YsHHUIAKlBWm3Ths6EURtLvgcyjKUQ4YvohUApiyhuxjM3MIpJBJ_V1n8CeaULoYYt5t7yhWEraNCg7LCHJWQHWFvB-nW_eVyPOgTbA9pqDyzW34BRsfw5XD334ZPJIAmHLpP7lg6xCAp0Xr4z6bgUVck4ZgHxhdOvwFRjeAk4Wdm_X-jiLFDifSf_2t-HVE6VPdtgBPIMV3Gfnm_LtoU2msrlBgtEYCG_KOetbTJOe5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو در ترکیب فیکس النصر بازی بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/108208" target="_blank">📅 19:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108207">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e597b9b54.mp4?token=Kp3YMEYdAQWfLwdMgL2TSnVVeieIvD8cwwC1tI0dJAAIaFcbPh2Em32ySsl1xk7OoiHc7yh_JCks3rrxj0BXV1P4GCt7RfPiMbpNPpEHwnVM9VYOIp8Jq7Fhmj6M1OEzMuOR-qgpxagoDVzNHvUvQ_k4ukPbPSbJk8nwD5DrQ6WJnXdyd9bruvSd32BqRwwabuot-j535mM1VqVtnBz8j8KN__RMBlIcBM4r7DSWWPOfN3YaDu0C0ctkSoxIQljsU1eHp6T4cTPj0nv55At27rDVt5aYIKjj-3yDijmn_2dDvCxkTvLSXW_M-_tdlKe9Rlq6anakgpbuklMAF3Ud3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e597b9b54.mp4?token=Kp3YMEYdAQWfLwdMgL2TSnVVeieIvD8cwwC1tI0dJAAIaFcbPh2Em32ySsl1xk7OoiHc7yh_JCks3rrxj0BXV1P4GCt7RfPiMbpNPpEHwnVM9VYOIp8Jq7Fhmj6M1OEzMuOR-qgpxagoDVzNHvUvQ_k4ukPbPSbJk8nwD5DrQ6WJnXdyd9bruvSd32BqRwwabuot-j535mM1VqVtnBz8j8KN__RMBlIcBM4r7DSWWPOfN3YaDu0C0ctkSoxIQljsU1eHp6T4cTPj0nv55At27rDVt5aYIKjj-3yDijmn_2dDvCxkTvLSXW_M-_tdlKe9Rlq6anakgpbuklMAF3Ud3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‼️
🎙
پیام نیازمند: گل صنعت نفت؟ من را ساندویچ کردند و گل زدند؛ مثل روش آرسنال/ از گلزنی اورونوف خوشحال شدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/108207" target="_blank">📅 19:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108206">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1c0466c5f.mp4?token=HDyv30okK-6saBV5nouO6FfAOQ8sYWcEIpOL72MeG-0lbU_ywsdaCYx55M4thhFR_bQoBmfsMOrjZZWp9Fhm6iZPM89nN3n0D08JygE6mGcBxHyVH3mRbLcFNS2dVAY22NWkHJVEQyb5b_YVCkHDBQBjRDqtC2DG4Km2jAG1S6HxkYe7-1Ypr14FvkM4KPbmk2qAn6MGKrmiVZUhBYYdUBSbyUH865UiDyu_qZ_sR4Y2rBVq9drGXO12X-UEKb97hvdlpczGBfLqfzTH0oB3U2_uuDtHHIQ4iUO66E5mgpH0lC0vPveQ2kCwe5fPXiym39ZHmEiKlpD1any5rXMAdDeQaOUTpNY3F8sRrYIpUw7KUOeKMUCPK6E10sXxTg39ObJQjJThgGheIaolGWyUDADitQEgLSabFQ_Lf3T9be7tYl6Wfl3M_XqgcV4wqmzLg4AD7litpbSNAvrTr2feX5K79CKceOJ25uaQNprVEBuu4vmKLuauBiEh5UhqWj_7uT3PXppPg4t6_FzERtUAUkBJjNFUHN-1wt-e7h8dlwf9ydyAVFJXPO2HsOg1kmqt8BwVlLdGcNHrtIpNinxKduqV4eo6xY1lYLIbbK3H2ig7lXsnuh_AUX-IvUR3-M8dh7cgcWTYdYaftKx0CKOqsG0TP53-VR3JiTHwMB2lqbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1c0466c5f.mp4?token=HDyv30okK-6saBV5nouO6FfAOQ8sYWcEIpOL72MeG-0lbU_ywsdaCYx55M4thhFR_bQoBmfsMOrjZZWp9Fhm6iZPM89nN3n0D08JygE6mGcBxHyVH3mRbLcFNS2dVAY22NWkHJVEQyb5b_YVCkHDBQBjRDqtC2DG4Km2jAG1S6HxkYe7-1Ypr14FvkM4KPbmk2qAn6MGKrmiVZUhBYYdUBSbyUH865UiDyu_qZ_sR4Y2rBVq9drGXO12X-UEKb97hvdlpczGBfLqfzTH0oB3U2_uuDtHHIQ4iUO66E5mgpH0lC0vPveQ2kCwe5fPXiym39ZHmEiKlpD1any5rXMAdDeQaOUTpNY3F8sRrYIpUw7KUOeKMUCPK6E10sXxTg39ObJQjJThgGheIaolGWyUDADitQEgLSabFQ_Lf3T9be7tYl6Wfl3M_XqgcV4wqmzLg4AD7litpbSNAvrTr2feX5K79CKceOJ25uaQNprVEBuu4vmKLuauBiEh5UhqWj_7uT3PXppPg4t6_FzERtUAUkBJjNFUHN-1wt-e7h8dlwf9ydyAVFJXPO2HsOg1kmqt8BwVlLdGcNHrtIpNinxKduqV4eo6xY1lYLIbbK3H2ig7lXsnuh_AUX-IvUR3-M8dh7cgcWTYdYaftKx0CKOqsG0TP53-VR3JiTHwMB2lqbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
واکنش جنجالی گوهری به جدایی از پیکان: تیم می‌باخت، سرمربی می‌گفت ما جادو شدیم و فقط دنبال این مسائل بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/108206" target="_blank">📅 19:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108205">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4ed7f5cfd.mp4?token=CYT9C5Nh7g7fZY6CcjqAi150wf7DlpFDkxKD-5tLT6YUK4Qc1W3zJbI8fz-gva524dkKUi-lCQ7B4cmXf8tN2npf3lu3D7tT_e2Xiqrn5bqKL-GbKmqnK1RsmfzoPFzQXxBDVs_fwa82soZDjA3Ji0TXg5R8ONunJepK2PKXyNA8ja5h3FQIVDn5ScmkhgjNRzl5SYEGZTc1BmyTCxYvOMnGYCxRX0o9m3dbFk03QidgO5iTkD_VwwJcw-sEc4Xhm2k_eUUkL18rPVIpcYNo0xhy8RF3_gnoIDLAmarVrF2xtV9ACaQWiIWX54mAghzzJXRr6uX5-I232u3YlKuN5m_k1EQds5IMyGR80V8p8EESIe1Lup5tX8Y8OFRB82nfZUjbBXP-ZPuUWkhN652QeGJThG2gz1P7I9-Pnif90199vv2HfmAAID0eWscXOEyMbPrm-xZ2OYf2fQJFwVfAeXHyKx6yW7W0jZ4x1USn3FcHC1hp5t4rbI1I9e71kL14Z7kUkYDrfrJXyaoSXrhuZ9Ovav73aC26yJuKhmmqbpKdPYMc7qzWE-aKvQys4577fdTIlr2hi9FapH1e9KiGde1IdLbG0_51LaGs80SNSLGppVyiy3DMHXKOrzoAbaxvBqbGAUPepjQm_hSxJ1u-X_RXkusbPOKtKKzGT5CKh7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4ed7f5cfd.mp4?token=CYT9C5Nh7g7fZY6CcjqAi150wf7DlpFDkxKD-5tLT6YUK4Qc1W3zJbI8fz-gva524dkKUi-lCQ7B4cmXf8tN2npf3lu3D7tT_e2Xiqrn5bqKL-GbKmqnK1RsmfzoPFzQXxBDVs_fwa82soZDjA3Ji0TXg5R8ONunJepK2PKXyNA8ja5h3FQIVDn5ScmkhgjNRzl5SYEGZTc1BmyTCxYvOMnGYCxRX0o9m3dbFk03QidgO5iTkD_VwwJcw-sEc4Xhm2k_eUUkL18rPVIpcYNo0xhy8RF3_gnoIDLAmarVrF2xtV9ACaQWiIWX54mAghzzJXRr6uX5-I232u3YlKuN5m_k1EQds5IMyGR80V8p8EESIe1Lup5tX8Y8OFRB82nfZUjbBXP-ZPuUWkhN652QeGJThG2gz1P7I9-Pnif90199vv2HfmAAID0eWscXOEyMbPrm-xZ2OYf2fQJFwVfAeXHyKx6yW7W0jZ4x1USn3FcHC1hp5t4rbI1I9e71kL14Z7kUkYDrfrJXyaoSXrhuZ9Ovav73aC26yJuKhmmqbpKdPYMc7qzWE-aKvQys4577fdTIlr2hi9FapH1e9KiGde1IdLbG0_51LaGs80SNSLGppVyiy3DMHXKOrzoAbaxvBqbGAUPepjQm_hSxJ1u-X_RXkusbPOKtKKzGT5CKh7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
🇮🇷
بازگشا، سخنگوی باشگاه پرسپولیس: مدارک کامل و جدید خود را در مورد آسانی به کمیته استیناف ارائه کردیم
🔴
همه تلاشمان این است که موضوع در داخل کشور حل شود. حل شدن در داخل کشور احترام به ارکان قضایی کشور خودمان است. درخواست از پرسپولیس برای پیگیری نکردن شکایت؟ ما دیروز نامه ای به فدراسیون زدیم که قانون محل مصلحت نباشد. یک بازیکن می تواند نظم جدول را به دلیل تاثیرگذاری اش بهم بزند. فدراسیون درخواستی برای عدم پیگیری به ما نداشته است. تا آخرین مسیر از حق باشگاه دفاع می کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/108205" target="_blank">📅 19:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108204">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad5142fc9.mp4?token=Nbvs-y-woMvOSe2qLonMSRmMKYb5B6DNc_MqnAnSBt9guogtejS7VcoClCfuYTVnJk5M-g8lV3GWQVU3pyksl-Rb1OS-p3_ZwUZ0joffPHRArG1IxeWsNuuLB-isdLapN1rfTd657IzFIypGScxP3zgj2n86FQUA2QdVvQyMyvTytYkaEw99mBaNeOJJXVBJhuu6Qv3LIyVCtnWEHdcshdyNSqUFhgCXX-Dpsv-7Aqt7I3gfgtoPU0I3W3cHUVkpiacZrc3inlQGk-OUg4obAGL6j6Z-w20TJZCv1XtLMYcDMYzYunmH2eWrwSB8cOtMeQM1XYWqC6YaoC4a3LC2rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad5142fc9.mp4?token=Nbvs-y-woMvOSe2qLonMSRmMKYb5B6DNc_MqnAnSBt9guogtejS7VcoClCfuYTVnJk5M-g8lV3GWQVU3pyksl-Rb1OS-p3_ZwUZ0joffPHRArG1IxeWsNuuLB-isdLapN1rfTd657IzFIypGScxP3zgj2n86FQUA2QdVvQyMyvTytYkaEw99mBaNeOJJXVBJhuu6Qv3LIyVCtnWEHdcshdyNSqUFhgCXX-Dpsv-7Aqt7I3gfgtoPU0I3W3cHUVkpiacZrc3inlQGk-OUg4obAGL6j6Z-w20TJZCv1XtLMYcDMYzYunmH2eWrwSB8cOtMeQM1XYWqC6YaoC4a3LC2rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🚨
‼️
🇮🇷
هوادار پرسپولیس: کامنت در پیج السد؟ ماجرای آل کثیر را یادتان رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/108204" target="_blank">📅 19:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108203">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLJGYBGQmruHrx4jtIY_bP-JoP5sG3l10UpvnfCA2YAtvOoZVh-TgTFiBOi0BrZiWnw3efoarj2R9JtRsuHssmwbbbZmsRzftmH1NgBT2N-cCTvBhrjm9_GIthFT4BKgXS9UlL_MaEbZ8uoHOx3h6GVCn18lqy1GMgeu9pczX8m4zgjvpT8lCRD-4BtiGo7yvNiQXCfnzAPtzYwI8qzOpcFwIsxLS7wWGu7IoK3eU6tQ7Sgjcd20s-V6BoW3c9qIb5p8npHceKM9L20lSNAhH9UNbyt6008QVYbpD_lgYYWiyrTRK73k_8ARPAx0IA_6pFneeknwqauL9Ia3s-DYeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌هشتم لیگ‌برتر؛ بهتر از این نمیشد؛ برتری خانگی با گلزنی اورونوف و بیفوما؛ علیپور هم طبق معمول گلزنی کرد؛ پرسپولیس در آستانه گرفتن صدرجدول از تراکتور
🇮🇷
پرسپولیس
3️⃣
-
1️⃣
نفت‌آبادان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/108203" target="_blank">📅 19:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108202">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4l235WvijDpbN9b6S80djwCVBxzW_c9rl7PO7SJX2jU7_AQtolGdtqxpRfAi78QS84H_V16lF-Rnj7WGKHslKDBu0HUFb_XWL_gjR-TaflOI_gCUM_XJXZPn7VgzThpkh1wJQs0APCk-q5sY-HRSehGvIb90mknw1iS5UiTv9caeyXk0etKpDCOIJOVXpTLlV6ns8anmkDnqNyhpD1L9WacvM9J0YgxNODxOQB34pCR25LQUmAuK04lAcz5tK-qNoHivg9wNijdnfYG2Ksm53YVEtYTOWPpu8n4M1O47Ll1rO6cRvwIVZAmiO_FQK5oeKDmQCgU9nXU1VbUz7wEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌هشتم لیگ‌برتر؛ بهتر از این نمیشد؛ برتری خانگی با گلزنی اورونوف و بیفوما؛ علیپور هم طبق معمول گلزنی کرد؛ پرسپولیس در آستانه گرفتن صدرجدول از تراکتور
🇮🇷
پرسپولیس
3️⃣
-
1️⃣
نفت‌آبادان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/108202" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108201">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9ae46fc.mp4?token=OeIq1KElmNnLha0ixUBg1UiPJrbiK0kT8Nx8DnsBCVgar1nF1pGmZjdTn60zUTq27YwewnxUo6n_W_tajQW07yHvtEGOO2oR9wIheUAQuxY6ZJVG7ITsaXLIDNeMtPhpeWpQPtWXo2mbMof1NrjHHktL7vXFSYa1pCvCcWJsVoDRawXGHGDmghgFVXOQ1qNBd3fljWhKpg4SgUWqCdEv_2rN0kLjcJGv2NM-CA4ATcO__Fz3Yy7lVo6qSEGxv-wToKwDR1wVzrgZhayNxA-3Xj-hWhRb5YODTI2-BT0r2cyPppWeZgQuhjwiexGkaKbK8VIMuenrnvD9UMlV_5HtJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9ae46fc.mp4?token=OeIq1KElmNnLha0ixUBg1UiPJrbiK0kT8Nx8DnsBCVgar1nF1pGmZjdTn60zUTq27YwewnxUo6n_W_tajQW07yHvtEGOO2oR9wIheUAQuxY6ZJVG7ITsaXLIDNeMtPhpeWpQPtWXo2mbMof1NrjHHktL7vXFSYa1pCvCcWJsVoDRawXGHGDmghgFVXOQ1qNBd3fljWhKpg4SgUWqCdEv_2rN0kLjcJGv2NM-CA4ATcO__Fz3Yy7lVo6qSEGxv-wToKwDR1wVzrgZhayNxA-3Xj-hWhRb5YODTI2-BT0r2cyPppWeZgQuhjwiexGkaKbK8VIMuenrnvD9UMlV_5HtJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل سوم پرسپولیس به نفت آبادان توسط اورنوف (84)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108201" target="_blank">📅 18:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108200">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4da4e50a3.mp4?token=dkA3upDnE-93uQAjaOG5SQIQ7zv6ybC6ibGrk8IVPFHOLFcdG2edjixEuJqKGY941nak8atxnu8rYDLVbeatj-qoLoas1IX2rXahJDtf63qhmVzELLHH9RVyuhFJoERwyVl67zCrT0D_d7DpdjGu9Jm1MmJinT5Z9OySwdJYqROBT-ZMEeMBRgxRzU0CtUvkRftlhTo7emH59ynV1Ybhs5OFZxwU4qgHFx-DJsRhbMHBzPzIyFeuh8yL0AkjXhgbz4BHcXzN_AW-YubqK2sPb_KwVna2rNedXO4VTELenNX7yw4mbYKc8Uh5maknM9KRfgn6T-qsgH7ioGMN28G4Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4da4e50a3.mp4?token=dkA3upDnE-93uQAjaOG5SQIQ7zv6ybC6ibGrk8IVPFHOLFcdG2edjixEuJqKGY941nak8atxnu8rYDLVbeatj-qoLoas1IX2rXahJDtf63qhmVzELLHH9RVyuhFJoERwyVl67zCrT0D_d7DpdjGu9Jm1MmJinT5Z9OySwdJYqROBT-ZMEeMBRgxRzU0CtUvkRftlhTo7emH59ynV1Ybhs5OFZxwU4qgHFx-DJsRhbMHBzPzIyFeuh8yL0AkjXhgbz4BHcXzN_AW-YubqK2sPb_KwVna2rNedXO4VTELenNX7yw4mbYKc8Uh5maknM9KRfgn6T-qsgH7ioGMN28G4Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول صنعت نفت به پرشپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/108200" target="_blank">📅 18:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108199">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa65c912b.mp4?token=oERyq1ANngM6q34uPV-FaCX9eyaLZAiFW3aLlDu2okkEIQxG9gIobYIZiWc02KDV_oMmbVB7bcy2RVa8nIPPO3_ST-yb0GZ2LqLP0uH0D-Hk6N4VKyQk23ORDmxuja93kA5kMPrs2VM3MQ5gov-FkDfOno-RXmqqb7xX_93dPLQ5cZ72shzsBC3mORh2mIBRnWetaXptZnrNJ4wY868eUSllF1BrfNEcLjOvoIB7GEKHI5FPuk_GHiH9Z3IudjKzInYOc0wcEHBn-EZrohcynJt9FwEQkYaL7Vw_yDqgq9ge-vYEEvANJDnZ4fUym2YClcDHRiKUQss9BwC_rXnx0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa65c912b.mp4?token=oERyq1ANngM6q34uPV-FaCX9eyaLZAiFW3aLlDu2okkEIQxG9gIobYIZiWc02KDV_oMmbVB7bcy2RVa8nIPPO3_ST-yb0GZ2LqLP0uH0D-Hk6N4VKyQk23ORDmxuja93kA5kMPrs2VM3MQ5gov-FkDfOno-RXmqqb7xX_93dPLQ5cZ72shzsBC3mORh2mIBRnWetaXptZnrNJ4wY868eUSllF1BrfNEcLjOvoIB7GEKHI5FPuk_GHiH9Z3IudjKzInYOc0wcEHBn-EZrohcynJt9FwEQkYaL7Vw_yDqgq9ge-vYEEvANJDnZ4fUym2YClcDHRiKUQss9BwC_rXnx0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل دوم پرسپولیس به صنعت نفت توسط علی علیپور
P53
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/108199" target="_blank">📅 18:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108198">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4b20c129.mp4?token=PNI7LROcijfkFRwvSy4ngu2w2vpbfehHOXKnq2PdTbIcZZ6G8N7JqmCK26B_e4TlWyM65u7eAAMRUrpd4_StkWPq92fD6dlFYAw5eG0qiyrr5cekgxZ3nRNc2ibTxJisEavqfuAzD9PnW56QSW3ErMOkfJQ-wnzRoK2e7ikuTtFTru3Asx7EW8hIoXp-bO9A6ga3Q57zsP8H5aQccP3wllOwL2lYJp4jyobYq-QcxahFkVvobQw-gNcjvu4aeZN4IzHV25SWRsgHgOa9SVOtVt_6h_2ykJ-y64ekmqn3aoIEYmgpad3vLBICf73nuSOFddDHY3GWkypFg1W2grNH4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4b20c129.mp4?token=PNI7LROcijfkFRwvSy4ngu2w2vpbfehHOXKnq2PdTbIcZZ6G8N7JqmCK26B_e4TlWyM65u7eAAMRUrpd4_StkWPq92fD6dlFYAw5eG0qiyrr5cekgxZ3nRNc2ibTxJisEavqfuAzD9PnW56QSW3ErMOkfJQ-wnzRoK2e7ikuTtFTru3Asx7EW8hIoXp-bO9A6ga3Q57zsP8H5aQccP3wllOwL2lYJp4jyobYq-QcxahFkVvobQw-gNcjvu4aeZN4IzHV25SWRsgHgOa9SVOtVt_6h_2ykJ-y64ekmqn3aoIEYmgpad3vLBICf73nuSOFddDHY3GWkypFg1W2grNH4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اعتراض شدید تارتار به پنالتی مشکوک صنعت نفت
🔴
@Perspolis
@RedStarFc</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/108198" target="_blank">📅 17:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108197">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3013266bc8.mp4?token=l_fxWCnSGAN_pMLsqJWoDTZ1KN4Bs2d1GKnHiUm4AYX7rXx6UMfTMFNeKV1R9dSN2AztGZ_6LA_3ltemesV8wdKDivYEfnIYrXzfIQNsNSIsX18zadbUpDA6iyjrRNcLO_g8EZoJI3DY_0qIQQnHd2fiKsaGt0_nDdRXy8oNgKv70nn4d5BfHuFnxUSaStP2AmSakrfRahBKun8mZxr17cd4AvCOXTy1WHGmXt99UzTcduapf6JDxAjmry3EvMruqc1O_8eQ1Ci2Q4xlo0uoI-ds31WZSe2_HTWgwpLX4LlDPl-hTuvbroNTJfJROxc4u-aNbdILtlGaPhMqm9AeiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3013266bc8.mp4?token=l_fxWCnSGAN_pMLsqJWoDTZ1KN4Bs2d1GKnHiUm4AYX7rXx6UMfTMFNeKV1R9dSN2AztGZ_6LA_3ltemesV8wdKDivYEfnIYrXzfIQNsNSIsX18zadbUpDA6iyjrRNcLO_g8EZoJI3DY_0qIQQnHd2fiKsaGt0_nDdRXy8oNgKv70nn4d5BfHuFnxUSaStP2AmSakrfRahBKun8mZxr17cd4AvCOXTy1WHGmXt99UzTcduapf6JDxAjmry3EvMruqc1O_8eQ1Ci2Q4xlo0uoI-ds31WZSe2_HTWgwpLX4LlDPl-hTuvbroNTJfJROxc4u-aNbdILtlGaPhMqm9AeiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباه عجیب سیروس صادقیان!
⚽️
⚪️
گل اول خیبر | امیرحسین فارسی '35
چادرملو 0 - خیبر 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/108197" target="_blank">📅 17:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108196">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108196" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108196" target="_blank">📅 17:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108195">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xeh2yRUmyov_62oYHFEX60OsWIL8rsgmEUIigr7NeA1FgFU1k4wwi-ER-_9EtKD6APwlMQIk4HpVbgJcneYmbtt9k4GqtWR4vOxVlsBfuNj-D-Fj9TzGXU9UA9DAZuRzSPt3F455oocVRncRUah4vfkCvr08idCeGXUpiMpxE4Z0-rN7tclAXvBwY5VuzY5O_E3njpLfkD7CBf_7WoN7yqH0q6KoivfAkJgvPpNa51kcewcXbdkcNepTbTHtXszN85IFiajYe3R-A3sqBih_VWMI9TMR-LjnUBRIhHGY5lk_s46sTqJUgVEDo_RMZBNLQ4exR4CWgCWyf1cO3qDeiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108195" target="_blank">📅 17:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108194">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
اعلام پنالتی به سود صنعت نفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108194" target="_blank">📅 17:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108193">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef96e5b249.mp4?token=aATxPaMJyKf6TK5ul4OAoOhXAEtguAxN-QskwWyr8dAExYwTvAER21pX8wgNbkjVrfc6LqMhG7dOw_s1_9D8xmg3YwpRSWmDDaphpdj_h_iWNhEXZqQrh5RgR0zu2qTkSjGleqFpS8VaBUYIvK_La4P6tXgPzCwjA-iepXcFiGXJZ2XB6ZdV1tZXtB_XX-PzjurZMbq7n-8Ro0IXz_d6BuoTY8-Pn3bCWY6ZIkk6LmXVyk6z5ohC1g0PqycTBugcOMYdLdTlSvk0H9-iGHCb5_xG5s1uK-d9PHVF87JDiAJo3PR3Rn8tin2jeSLGxRmnpc9hTxTtezytkImZlc58fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef96e5b249.mp4?token=aATxPaMJyKf6TK5ul4OAoOhXAEtguAxN-QskwWyr8dAExYwTvAER21pX8wgNbkjVrfc6LqMhG7dOw_s1_9D8xmg3YwpRSWmDDaphpdj_h_iWNhEXZqQrh5RgR0zu2qTkSjGleqFpS8VaBUYIvK_La4P6tXgPzCwjA-iepXcFiGXJZ2XB6ZdV1tZXtB_XX-PzjurZMbq7n-8Ro0IXz_d6BuoTY8-Pn3bCWY6ZIkk6LmXVyk6z5ohC1g0PqycTBugcOMYdLdTlSvk0H9-iGHCb5_xG5s1uK-d9PHVF87JDiAJo3PR3Rn8tin2jeSLGxRmnpc9hTxTtezytkImZlc58fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعلام پنالتی به سود صنعت نفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108193" target="_blank">📅 17:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108192">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60684bf96a.mp4?token=dXi8PjzfCSExgmJE07GxHrfk3xXyxhOW3dXA8l7CT_cOH5NcjvZNWYWAysfUO0OkiAuCObpPonscLrPZGa9NikrmhGYlf9RCkeKfPOp5APDJyiOrCT1fJQy9nmwWYqnBls1cDMLZEE0gpKdvPw9lCFFDEThsm9aBUXPYWzBLV9YIPSZB75h-Vcd9oGiFs7EDpa-DVS6XFZwaq_DG61sXeBA2iFgbXdgHPNo4lSp4C50nLegg9CCOZyc2iN9P1CXEYQcHalrqi9MVJ6DmMh5SAVqYn7Wi_r4tTJboMj2g3-BmhsIwk04HCSJUWaWBrXiSepQZUgdPGRLoGvGIZoNfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60684bf96a.mp4?token=dXi8PjzfCSExgmJE07GxHrfk3xXyxhOW3dXA8l7CT_cOH5NcjvZNWYWAysfUO0OkiAuCObpPonscLrPZGa9NikrmhGYlf9RCkeKfPOp5APDJyiOrCT1fJQy9nmwWYqnBls1cDMLZEE0gpKdvPw9lCFFDEThsm9aBUXPYWzBLV9YIPSZB75h-Vcd9oGiFs7EDpa-DVS6XFZwaq_DG61sXeBA2iFgbXdgHPNo4lSp4C50nLegg9CCOZyc2iN9P1CXEYQcHalrqi9MVJ6DmMh5SAVqYn7Wi_r4tTJboMj2g3-BmhsIwk04HCSJUWaWBrXiSepQZUgdPGRLoGvGIZoNfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل اول پرسپولیس به صنعت نفت توسط تیوی بیفوما در دقیقه 5
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108192" target="_blank">📅 17:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108191">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b705c5cdea.mp4?token=AVGFUxyJfqIkiLh556AiaC9jirQbpaVpVmnF-h0ohhQRnf4YlUxl4oBza3vePR8EDVDxMDqzJKtaNJ0tsP_w4mro18i9bc_FXzp7mzSG4aHHzA2RHRgeMqdTall4vy5fbd_j-Tzx3LYhsjdlPrGhx878EB7qaDtk_ZKEx7Fb57VlbqE4Isu-AKFEFukRxgAKLogFD86Jzp_oq4PcXC7481GoHdEHaC9ZAFLwy9sq5FlfwKy8acNQNFKTjqIFJI6EXKKErpLtg7KxjP3rNgrc0rUhx3l6dXgO_6cN4ZN6-tbU_Hm4zqSdDNnXPwV7HG9Ehj-NN-zSTFFvD4DyW4LgXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b705c5cdea.mp4?token=AVGFUxyJfqIkiLh556AiaC9jirQbpaVpVmnF-h0ohhQRnf4YlUxl4oBza3vePR8EDVDxMDqzJKtaNJ0tsP_w4mro18i9bc_FXzp7mzSG4aHHzA2RHRgeMqdTall4vy5fbd_j-Tzx3LYhsjdlPrGhx878EB7qaDtk_ZKEx7Fb57VlbqE4Isu-AKFEFukRxgAKLogFD86Jzp_oq4PcXC7481GoHdEHaC9ZAFLwy9sq5FlfwKy8acNQNFKTjqIFJI6EXKKErpLtg7KxjP3rNgrc0rUhx3l6dXgO_6cN4ZN6-tbU_Hm4zqSdDNnXPwV7HG9Ehj-NN-zSTFFvD4DyW4LgXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
هوادار پرسپولیس: به عنوان یک لر بختیاری از بیرانوند متنفرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108191" target="_blank">📅 16:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108190">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fffee2ce.mp4?token=vqgQVNXFR8ILDvWzMASM68_wUitO1GwMjsv6nUlIUt70x_NXrvlpcUgu92xPRmH2LGrn26UrUzSspsM7ix8RPOJEeukmNrhvWMepT0XsCd46pEcSHzMO_iZjdUjQu_Ams53d6GlsBx49fHertkbSCTXcigrg8ndT61uyom7BnWsIvC3fVwk0zO1vyWHakRf9AHbOxAZC1YLmZxwWFfv5W6bSzlDT1mYI0t7y1rSN6OE1vZY37ub-YfNa6CoFT-7LcwEqt6ei28gN5kSNSOCCVDYVcwpEnyEAD-_C1xzqnlUGJ0DIfs2hH2cfdlUwJJ5uqzsje6h-J0xvQaYqyJGmvwgr9vRtrbgHH3CBUQ0COGfhbLIpOm4srTYgN807sb6jZu3PWnakudkocbeLGIYefKK-m3-XNkO_cVuxYPG3iaXzwnILBwEQJGt3bFWV9_mDQEPqhqfLVr18b6u1bw-9XtvzpZfiHYU0zrC8U5THTY0PvT9Xqx2dfIrkqxsgmLwFWzcwJIzY2lz66AeEX6voLVoZX3u-s7Z_hThfSXLTjLPZ94eJGdUHJNW6vbr5Wko5Nj0A4YzBCBNCLqlorLetKNGDaPQ6lIQZfZ3gddovz6ssacL4h6QN9Xmga7jr7td7iVUKp5z-J6Guem9XuglagkuqgCRQBvkQThO7_ZtEaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fffee2ce.mp4?token=vqgQVNXFR8ILDvWzMASM68_wUitO1GwMjsv6nUlIUt70x_NXrvlpcUgu92xPRmH2LGrn26UrUzSspsM7ix8RPOJEeukmNrhvWMepT0XsCd46pEcSHzMO_iZjdUjQu_Ams53d6GlsBx49fHertkbSCTXcigrg8ndT61uyom7BnWsIvC3fVwk0zO1vyWHakRf9AHbOxAZC1YLmZxwWFfv5W6bSzlDT1mYI0t7y1rSN6OE1vZY37ub-YfNa6CoFT-7LcwEqt6ei28gN5kSNSOCCVDYVcwpEnyEAD-_C1xzqnlUGJ0DIfs2hH2cfdlUwJJ5uqzsje6h-J0xvQaYqyJGmvwgr9vRtrbgHH3CBUQ0COGfhbLIpOm4srTYgN807sb6jZu3PWnakudkocbeLGIYefKK-m3-XNkO_cVuxYPG3iaXzwnILBwEQJGt3bFWV9_mDQEPqhqfLVr18b6u1bw-9XtvzpZfiHYU0zrC8U5THTY0PvT9Xqx2dfIrkqxsgmLwFWzcwJIzY2lz66AeEX6voLVoZX3u-s7Z_hThfSXLTjLPZ94eJGdUHJNW6vbr5Wko5Nj0A4YzBCBNCLqlorLetKNGDaPQ6lIQZfZ3gddovz6ssacL4h6QN9Xmga7jr7td7iVUKp5z-J6Guem9XuglagkuqgCRQBvkQThO7_ZtEaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
صحبت‌های هوادار خردسال پرسپولیس: اگر یک بلیت داشتم که یک بازیکن را پرسپولیس برگردانم، آن کریم باقری بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108190" target="_blank">📅 16:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108189">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0df85fa87.mp4?token=cuPLTPxC0C3KEamDc6EDOYuwZDvt0KOWga6IIt_e8OZooWtVubNb3A2rnl82s73KXsO1QvSrsFdKDCh0Wp1JA2TLmwllx5w0DntQYuFf2PSOktHvK43INgwcYS0Um21K6hKe7KGFCBcs-5fm4FgjyDIQXKw0jVCsgxO86g3KkIO2C1GxoKExkajSzOFe6B0PTsbT0QGLSTYv_bubzAxxenxwDcf6NjodJ1XnXypR-YyR9XPCpfV94lkMiVevKIuf49fZ50g1IupNt524Erp9qjQlrHNW7-ZTkQwx1R0xJ9blIY6y1Oca7B4TFlM9tPVNJqlU342EAucDVTxWVCVb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0df85fa87.mp4?token=cuPLTPxC0C3KEamDc6EDOYuwZDvt0KOWga6IIt_e8OZooWtVubNb3A2rnl82s73KXsO1QvSrsFdKDCh0Wp1JA2TLmwllx5w0DntQYuFf2PSOktHvK43INgwcYS0Um21K6hKe7KGFCBcs-5fm4FgjyDIQXKw0jVCsgxO86g3KkIO2C1GxoKExkajSzOFe6B0PTsbT0QGLSTYv_bubzAxxenxwDcf6NjodJ1XnXypR-YyR9XPCpfV94lkMiVevKIuf49fZ50g1IupNt524Erp9qjQlrHNW7-ZTkQwx1R0xJ9blIY6y1Oca7B4TFlM9tPVNJqlU342EAucDVTxWVCVb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بانوی پرسپولیسی: به خاطر پدرم استقلالی بودم اما زود متوجه بزرگی‌ پرسپولیس شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108189" target="_blank">📅 16:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108188">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtrT4V4hVXIEP4SGsp1nYwis_qGoUDStsPGpRo3VuMcy_ieRNkBUJ_iwopY1Izn_dLjh4cvI9qqDigv5bW5zJuHFnQutotaPpRtElg59Up73w--v4A6YC5_uzNXIOizw3VXeOq8MAOsobAS4jzwGMOYaZazFWuxr8OWZ2732lKh68VD-OSsadtCefbgeI_kzDxZoXDR9aLpGJdnHIIaXP3tShG2MUDB4hyVgMEpk-PEa0DbA9uEWCcoiHyZsYDTBsqQQnGbwQegugrHlivTqjMbEbAzrf0hrYu4vtm11awpzW-GxthHU4HUzSppwZfDyUn1FJ-HiVAB92o-Yy6pDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با ویارئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108188" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108187">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c488f1154.mp4?token=YzgS22Ypq5z8vK4-hEdwMFzkK7_yhALjAMo3OyAvhi2FBRXTT5Wq9wipPInydhAyGR_0DgYG_VZa0vn4k3BmOL31XsWhX1U8qzoV7PwM-cZhk464hn65vmlw9CIdR8Wcb8tzfrgBCSQLPqVA-qzyqbqcBBy2Qwcq7Tl0BkYoppZQ3ahMyaZWGsjQkHHhdQUzkvfIDVeqgSlVk0d3yg1CrshpEIP4HOAapn3mjPtLigWi3Z7CWIBJRzTJgi4BIfJlUaQNue8SmvrxhzaJxIAfXQI90wfsP_Cfn-J_hSYG5_wO1FBnxAHsG218QLwn5ryczZZHwXalUQSCN46mkgJfIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c488f1154.mp4?token=YzgS22Ypq5z8vK4-hEdwMFzkK7_yhALjAMo3OyAvhi2FBRXTT5Wq9wipPInydhAyGR_0DgYG_VZa0vn4k3BmOL31XsWhX1U8qzoV7PwM-cZhk464hn65vmlw9CIdR8Wcb8tzfrgBCSQLPqVA-qzyqbqcBBy2Qwcq7Tl0BkYoppZQ3ahMyaZWGsjQkHHhdQUzkvfIDVeqgSlVk0d3yg1CrshpEIP4HOAapn3mjPtLigWi3Z7CWIBJRzTJgi4BIfJlUaQNue8SmvrxhzaJxIAfXQI90wfsP_Cfn-J_hSYG5_wO1FBnxAHsG218QLwn5ryczZZHwXalUQSCN46mkgJfIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
هوادار اصفهانی پرسپولیس: تیم دسته سومی هم پول زیاد بدهد، بیرانوند قبول می کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108187" target="_blank">📅 16:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108186">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f38bccfd90.mp4?token=dvIOFYhbLqMKGhRjARnvQvhN_BSV93YjpD5sy811uIa0E9gCNrfvlqWpFxZ5RzQ3bZIF3spNNbV1O9C6A4U9zRVhVD3kck6c5VvYeBy8QOe0igiLDAfzqFGkCnHVH02wKdj6ZF6dNuft63ghM8A8WPip8Cumllnds8eGBRX6IAaXTkrd4mKooydNNI7nIjb53IE3SNVThg-OgLEtJJyPf3FO0_BiRNbMf1y7zuQZSMBxJ5ANmuxhuAao2pB_tEyIMSpu97xrr2d4E9AhrygGlQoyCYfNkzXoASjdMsvj0WEYvaHQNQXSAGyBKKgZEYPvROBbtTlXQ5NO9Gu-_G1Y-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f38bccfd90.mp4?token=dvIOFYhbLqMKGhRjARnvQvhN_BSV93YjpD5sy811uIa0E9gCNrfvlqWpFxZ5RzQ3bZIF3spNNbV1O9C6A4U9zRVhVD3kck6c5VvYeBy8QOe0igiLDAfzqFGkCnHVH02wKdj6ZF6dNuft63ghM8A8WPip8Cumllnds8eGBRX6IAaXTkrd4mKooydNNI7nIjb53IE3SNVThg-OgLEtJJyPf3FO0_BiRNbMf1y7zuQZSMBxJ5ANmuxhuAao2pB_tEyIMSpu97xrr2d4E9AhrygGlQoyCYfNkzXoASjdMsvj0WEYvaHQNQXSAGyBKKgZEYPvROBbtTlXQ5NO9Gu-_G1Y-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
هوادار پرسپولیس: جام فصل قبل؟ هیچ کدام لیاقتش را ندارند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108186" target="_blank">📅 16:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108185">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
⭕️
🇮🇷
براساس گزارشات اولیه، مصدومیت یاسر‌آسانی جدی نیست با این حال سهراب بختیاری‌زاده هیچ ریسکی روی این بازیکن نخواهد کرد و زمان بازگشت این بازیکن حداقل مقابل گل‌گهر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108185" target="_blank">📅 16:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108184">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f4416442e.mp4?token=resPGo94keWsj5-ySqJICJPTLTY78QKgyOFH8ZRvU4o4oupIJ01bOaXhvkcEfLZMnzptWJ1tMvLR5oSSZk7tcAJ0bXQ3xKJXKeB8-RM5G78Kv85tv9_3cl081eA06irf2rhGEYqHAsVqXkfz_qXASf6qah7PRtZTKAFOmDMWtVx3_26nV9MwCdPgov89w0ebfBK_FBjzs5IfxtKJDYJ0UmS4lKJDnGGPcBwwLHqRiH1jxHDwWXkb0FX0JTgSPLC_TLAxtprjt608j8Y03Rty3ata9j44696waQbv-oCOqBKUkLK7onRcB7sa_Gov2gTBmjxGeSZkggeXzkdlI5mqaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f4416442e.mp4?token=resPGo94keWsj5-ySqJICJPTLTY78QKgyOFH8ZRvU4o4oupIJ01bOaXhvkcEfLZMnzptWJ1tMvLR5oSSZk7tcAJ0bXQ3xKJXKeB8-RM5G78Kv85tv9_3cl081eA06irf2rhGEYqHAsVqXkfz_qXASf6qah7PRtZTKAFOmDMWtVx3_26nV9MwCdPgov89w0ebfBK_FBjzs5IfxtKJDYJ0UmS4lKJDnGGPcBwwLHqRiH1jxHDwWXkb0FX0JTgSPLC_TLAxtprjt608j8Y03Rty3ata9j44696waQbv-oCOqBKUkLK7onRcB7sa_Gov2gTBmjxGeSZkggeXzkdlI5mqaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
کنایه هوادار پرسپولیس به گلر سابق: وجه اشتراک ما با تراکتوری‌ها اینه که بعد از 3 سال می‌فهمن بیرانوند چه کاره بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108184" target="_blank">📅 16:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108183">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-W1UIM2lPeWcxfV1k4nTOO9mZub_-tuzxhugUqXqNP68n4zbjlBQqB4pPmh_j21azhUzlBDMkzREjg3HfqPnnYk3HTPvjSFEdGsiYhsbBvp2IHBF5XBsvEgYu-LZ3s3iYnJhFYOWwYSF5Sc_dXqlH1aFgD5N6G-tfDGMbjIes-sIEA28QuoWkJv7ZbfQJmqtGG4c-D0uFZX0sEA7WMBX0b_LSSevRqG3k3as4jraz0vLwXT0cKXanWIC94Hkzw-UQH_rhe3Kryo2_cKl-ImHVy6kQRDohBy5DOmzFhCfjpBlC1sQqWORdsclSryZtQYCyYAK7yN0BDtoRDrSWs6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اعلام ترکیب پرسپولیس مقابل صنعت‌نفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108183" target="_blank">📅 16:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108182">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8dae1c8a.mp4?token=nlcLVpKwbNAL1D8OuyVuxPeXb6fQFTHRApfrdIUSUFFtKhPwf9Ea_w5D8_5OjqUZPU-joncRp44e9Io6cwK_7_TS1e0UKzmxawGU-BICWI2Jx7pp8haMSvgSekvuf3QB2fGwvEq7lG2DQ_d2-NhQl5duTqaiSQPvdod203dDPEaaHLzCON8k7VbV83GMFSXK4z0cgLUbmhD0gZ6BGS1cc6AGmhzHciWxOiiRYZZYo0cP-xvR7HHjcqvt5lk65V9WbxZfafF9ZJcvrFPA1wXSt5E9AFc8p4cQeq8AQDxP8WK_jHhWYVfkUP2__upSpSYEpn_rD27gbV3v93gIZXexJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8dae1c8a.mp4?token=nlcLVpKwbNAL1D8OuyVuxPeXb6fQFTHRApfrdIUSUFFtKhPwf9Ea_w5D8_5OjqUZPU-joncRp44e9Io6cwK_7_TS1e0UKzmxawGU-BICWI2Jx7pp8haMSvgSekvuf3QB2fGwvEq7lG2DQ_d2-NhQl5duTqaiSQPvdod203dDPEaaHLzCON8k7VbV83GMFSXK4z0cgLUbmhD0gZ6BGS1cc6AGmhzHciWxOiiRYZZYo0cP-xvR7HHjcqvt5lk65V9WbxZfafF9ZJcvrFPA1wXSt5E9AFc8p4cQeq8AQDxP8WK_jHhWYVfkUP2__upSpSYEpn_rD27gbV3v93gIZXexJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
کنایه تند پهلوان پنبه هادی‌چوپان به منتقدان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108182" target="_blank">📅 15:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108181">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa24f6046.mp4?token=aPdMEM97qNT-bf2Uplrhi0tpQOxYNLhiRu0zNZnZXQtxSd9cAyfDASp1MSVt97pMRG4yao5VslP6eDSR_13tGokMrX3QuAsQmgmjdOsDFdoQTYnwaHFKuBGsK1HhHn6wMZKRIlHYOE8V4Z6U2YaFMaCCYZYHYyIZ5nqvM8H0J5uyrwVepfqsLEeIwqB2p4CIJjQd1BmbAot2OjcMRzTRJVaiFG68BDCBG2ch5CvAJrmuBvhOso9fAtDQg2R2HKOh16CoF2qyjr28-BWEHF80GohfNDTUYEBnRFAZyHAx4_4bBNkS0XcehzBzDFyeYkX4KHsYEejCD1ChZ2YjTcGKjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa24f6046.mp4?token=aPdMEM97qNT-bf2Uplrhi0tpQOxYNLhiRu0zNZnZXQtxSd9cAyfDASp1MSVt97pMRG4yao5VslP6eDSR_13tGokMrX3QuAsQmgmjdOsDFdoQTYnwaHFKuBGsK1HhHn6wMZKRIlHYOE8V4Z6U2YaFMaCCYZYHYyIZ5nqvM8H0J5uyrwVepfqsLEeIwqB2p4CIJjQd1BmbAot2OjcMRzTRJVaiFG68BDCBG2ch5CvAJrmuBvhOso9fAtDQg2R2HKOh16CoF2qyjr28-BWEHF80GohfNDTUYEBnRFAZyHAx4_4bBNkS0XcehzBzDFyeYkX4KHsYEejCD1ChZ2YjTcGKjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
همچین ذهنیتی برای همه آرزومندم...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108181" target="_blank">📅 15:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108180">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e35d4b3b4.mp4?token=foZ029XD_BWIsJ-Q3kVVy5Z89OYf4MgJFj4eAvhed6-xpkOo3us_XaYn2JEIDexEi8uCtDIwPGnoKFksQzY8dxCiwy1EcURPpSJra25DM3PJM031tfSqRrPdUitFHkSN-YozO4gGqsXzG1pJjBAMFY-WDA2LJPcJdUjVDzp-s7nboHsb0YZYoTArWqrDg5WVy1mJuCELgaIAjSMSYTD4fwAWpixznhy8q7QGmfqn1qFrH8qEjyT9lxbXLfeZqRWjmgWEL__H9fohsC5cpzr4oQ4hs03cdLSUXPhlEV7NY8btDO_eCTFP9twdY3VvJSgGXI0wMuDYZO_qhZ3fVOckrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e35d4b3b4.mp4?token=foZ029XD_BWIsJ-Q3kVVy5Z89OYf4MgJFj4eAvhed6-xpkOo3us_XaYn2JEIDexEi8uCtDIwPGnoKFksQzY8dxCiwy1EcURPpSJra25DM3PJM031tfSqRrPdUitFHkSN-YozO4gGqsXzG1pJjBAMFY-WDA2LJPcJdUjVDzp-s7nboHsb0YZYoTArWqrDg5WVy1mJuCELgaIAjSMSYTD4fwAWpixznhy8q7QGmfqn1qFrH8qEjyT9lxbXLfeZqRWjmgWEL__H9fohsC5cpzr4oQ4hs03cdLSUXPhlEV7NY8btDO_eCTFP9twdY3VvJSgGXI0wMuDYZO_qhZ3fVOckrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ صفر زندگی یک
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108180" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108179">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUyGg-YWKe3gAnDhYv2e4mDsrmBQTRgBZw0dKdaaES8J3Db7QycoKtBdtoWiqJnNfeyP1SBdHi8_0jEStcinpY4jrx9eroPsoUe4hYIJ2f997kEknM1mtWuG2YCdV4ZF9d2XZ6T4tfXESFH75NmBC8Q7z_C-bQFvXn0ve-MRKg4R8tFaoZ0h9llrbtiSygOR4vXjhGEof_Bl2sZcDjT1VeUs2VFhX3XwlrbEs0jqDfCetS0cmBSyYNaMpt1MNnOWtxa1yqBk5Oq8d7Eit3fTyHMdScBcfa8UsACmRTGsBMDXW20ie1DKh44dqSBBY8KFHQjtZb3UVpepL1oaCgDoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇶🇦
با اعلام پزشکان باشگاه استقلال، یاسر‌آسانی به طور قطع بازی روز دوشنبه استقلال مقابل الغرافه را از دست خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108179" target="_blank">📅 14:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108178">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEYK6w_2E9ykz0zNtsMO3AZ4OdXj3Kq0CUYLqXDu9H5Gx2qxfG3yz6P3jkQig97_qxOX-26ElIiGi27FfiZRfHZZFneByg1ihTQIwLSDt89_Cp7wOKX3qZqPf667wgN-k4N3yIGbX8gIePaV133o2ol-Gsg6ojlcbk8nHmsc76Fgd0fgzdsuk64dr6QHq6aRD4B5yjGP0BtjtlqHtZCmUXJEEDzgx75R04lvTSf8E8oxOzm8s525jP9ctebmaAtNheupWzhPxmkn7DEckWZPIWDNyVwv1tASKtVxJUp1y3CSBWEj2VE9xJbJnTUohXAuTrd9wATAAF5BNit3TF6TZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
هانسی‌فلیک: مشکل رافینیا جدی نیست اما محض احتیاط بازی جلو ختافه و گالاتاسرای قرار نیست به میدان بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108178" target="_blank">📅 14:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108177">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">توصیف وضعیت اقتصادی ایران به زیباترین شکل ممکن..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108177" target="_blank">📅 14:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108176">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gABo4B2NdLiV5AtRcmGOYkCd6WZorLzByJ_E6Te6BT6m3-6F0vCqR-4LSjxEpmUrmLX4iAuYgb0kvwhvo0OPqkVdTR5KpXz6r3ev0i6i6YJhFKL2NzLoCE3Sx55VGUT6TJ8WmCPGgItM64e-uCnMB29VALhOlnH73RgjoSnnvG9KYx7lMjqZh80ddkRB0nGRHzaHrW0f4pDeL18zFDSCwG3GJTZiI-WbR-Y27q7h0J2Ot6mDaAPYyBErx9wVMC3oco2pS34MC_n-MT_cUKzy9WEUHxQrZecwCDC22ZQI7mjpUvxcjq3JQkfskH9DnBNS5lgJ1Fv1gMNUCvW-1rgbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
🇮🇷
استوری علیرضا بیرانوند خطاب به هواداران تراکتور: حرف‌های دیشبم از سر دلسوزی بود؛ الان زمان مناسبی برای صحبت‌های بیشتر نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108176" target="_blank">📅 14:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108175">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrIqzbleJotZpacUUiOPMpuCrLxP3c7LEuvipl80bgHDtEgiVIKVLzpKAkv3z1UiEvnkm-wuOo3oVLw-WUYAdoO3irjtDD5VcicesxlfyJ4GSKciZ8pnFSzt52-uX5UbGNAkyQMXjK0KNeCuTGB-PH1ez9dW4NI5585rfWEKlxn8iZpafvxZNb2EBRBjxemo-uRm0OBuu6Xs628-a8Z2M6w2pC4jphs_gTg5IVmyKTC_JswGIJvGGOYk4gyClQUtcFSxkAtBQeS8O-2VFcGLhbB2Kks2AuyvXRLZYIb37b_bgYg0bvda_4C_7plzifNzSQiUi25WeWQdwtmsPSWvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
ترنسفر مارکت: ارزشمندترین بازیکنان لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108175" target="_blank">📅 14:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108174">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601dba4230.mp4?token=SuMHYqU0doJSGwv05IYJ74PrCwoTN3YnkyXxlBBud0A_7RupNTyqIlSvv-aDkQeStbTzW6VUVNVqzHVAmuxlHGisJKgnaztaEQliTNOmMLhW2mFcA8pi1_I-Z1WAdhyFO4jTPdLA0W_jsKHk6Gf1v0Er2d9PwrNepdrEp7amNm7JjXTNJfPus6p4OJbL-cB93QCBlk2BTPKSixJX1v5PoqlmA9ca_f09iwmQKAq4l0DrrM6pEEVFEPgSvVpxmpkRqxQMCJlVsm5VnZ7CBmm9sxoLsfe4fhmh4PyQYNUMulWzCLjCY6pXpCTY10WOAvMRqyo7ALs9ibSqWlGpoat0Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601dba4230.mp4?token=SuMHYqU0doJSGwv05IYJ74PrCwoTN3YnkyXxlBBud0A_7RupNTyqIlSvv-aDkQeStbTzW6VUVNVqzHVAmuxlHGisJKgnaztaEQliTNOmMLhW2mFcA8pi1_I-Z1WAdhyFO4jTPdLA0W_jsKHk6Gf1v0Er2d9PwrNepdrEp7amNm7JjXTNJfPus6p4OJbL-cB93QCBlk2BTPKSixJX1v5PoqlmA9ca_f09iwmQKAq4l0DrrM6pEEVFEPgSvVpxmpkRqxQMCJlVsm5VnZ7CBmm9sxoLsfe4fhmh4PyQYNUMulWzCLjCY6pXpCTY10WOAvMRqyo7ALs9ibSqWlGpoat0Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
وقتی فساد سیستماتیک می‌شود، بعضی رفتارها آن‌قدر تکرار می‌شوند که دیگر حتی عجیب و غیرعادی هم به نظر نمی‌رسند؛ گاهی آنچه باید غیرطبیعی باشد، تبدیل به بخشی از زندگی روزمره می‌شود و کارهای عادی جامعه دیگر به چشم نمی‌آیند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108174" target="_blank">📅 13:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108173">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuK2JHMZiWCbYkSAoY08zsrTWVt9qKx_tZj9xsxXRTPYscwLEE_dq_6GTba0Tzl8lAf_HKBro4qr0MlAafoFqNQ16nQt7tBuq1IrVjd0TtzAfz-eZOLAe9OyaaSzH6ox3orvE6x7XAJXoqu_P66MWtR5oUUEzDfaE_KDuyM7X3l7uilmNZgVh5QkP4GtFXa5usFAcAXeLYCs-yrXJKnHVMLKElxW0hEnoZGBST0zBJFW5YsPe1Q6ITuIKGb2DwVNppQ7w8KU_WN8xcoJH3FQ__Yb7xoKAXdQlHaMr3aLczbah9hMONiiQRAt_LTqItntHlc_VtnqNqJhkFJCzumKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
📊
آمار بازی روز گذشته استقلال
🆚
تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108173" target="_blank">📅 13:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108172">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
⚠️
انگار ۱۰۰ سال پیشه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108172" target="_blank">📅 13:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108171">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghQ3u3gs_Em62GsOsQQ1yPvbqBatWFsmTDR2Gs6U4K0btTj-eZ3uReLMQ2zw0uLSqJ5wlrf5JxN_-2hMOI1w-SMb0zfLP4lrstAOX0mcS9g-gZz1QJCHeFANTdj8q8R9pCeJqqdOkXYNtJTmlK4u03XvZjmykbsF5pRlHqc-rHywL_AjAeYmN9aF6PjYPBxYAxu9jjO9YnmG_OQAW5X8_aeD-nQBxTQYtSIXeaqFtn-N5cyFCC22CryOTVQzRX3MQNNPVoxDeVa0FthDAVG4NWahaKsb6Kt1YQ9SkAuZLTN_Xi6sqMw3WkCzBe_EB9lNmoFUgCfByaDVABVAa8TF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇳🇱
عملکرد ژاوی در اولین‌فیفادی خود با هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108171" target="_blank">📅 12:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108170">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
‼️
⭕️
🇮🇷
با اعلام باشگاه تراکتور و با تصمیم جواد نکونام، علیرضا بیرانوند تا اطلاع ثانوی از این تیم کنار گذاشته شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108170" target="_blank">📅 12:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108169">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRaTR83299OKuTiN9ErS-Ikso4zDBtUnhJdHdDHTd9YeWjsd0uH23bldWf0gnPRwtKKSIMLzWpgRP4_35WHpKH--Qk-FKTn5Ikp6A1xc9qCi0I0SKvpSynPxHDe6fH_FY1q8Uqjzw2z3vznNuJTqXDj31ykHom3sTH_g7RFItD8d37U8nlLNKhfU6ON65SCsqh-Q6HkzSPQYxk6TJp8VPpr8bH1ac3ePi0W0Ssp6XHYBDP6pga05T2TggPHBlxGVVnWvbWNUmyDDBeQ75g-DaDal8oFdqmyhm7uRzrk6RDP2Y1rpC5fuik8_z2kh5QO-eDwNXaGa2bP_o7nWWyBRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
استوری جدید یاسر‌آسانی از مراحل درمانش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108169" target="_blank">📅 12:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108167">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kj3xM7dh5LzJEuIzv9w0i7topYCqR-250GtKyug9gIE6LXiNtPZFsK_r8i-9TXnhh_YeRZAlpXt5CyJKxcQDMY90rIraB_VIHb6wPiJ9oHh5WPHZURFr8OB3ZCQay5hxYtN9_o2J1w8kl9HzGUCE9i7kA6fu7eEdatM2W0_Ga1D85cy3n61dp3RHBULCOqHlpsSDOhrftX_6csqgZ4TplbQSjsXjrShckgAuQcvEU6O9LrE-7ZhyKz0jnBRFJT5kxmFlsLBNiq1NyVEtym5n94Ok3k6yY0Zcu3l_HNylfpLRuSnN3q0CEFDbiaN7rSbXwxfWY0WwS4cb85aCHdADRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pImRdtjAXFsOAfDEkHNLFLqa4UKe37KkcUKi_XUSgYN2Xj6Z1GaibRZTwL3Ulai72zASlz4Ee8LvXnZqBHsa-IJ5TiIXWtlwtpTeRI4brjdPyGkW6VDeSSyfNriA-SvqGfu1Il-p_BdLwmjottautHEgEpaQXBjGM34khaAjCq2y5n6ZlxKT-izGcwGPTw_MX1aJ8Gj7lSefAH4rQJC9Ja9_nSK0MPvyrQOxGcThLtZYiUbKqm5LDCsiqRvTqQP_W5ZNfoy6jXixtV4smiivXUCgY8EiuDjP-fewMznuzMK35eYVry2WEM51GOcbnPaq4MHw3mExvopDTExeOv8nSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇶🇦
با اعلام پزشکان باشگاه استقلال، یاسر‌آسانی به طور قطع بازی روز دوشنبه استقلال مقابل الغرافه را از دست خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108167" target="_blank">📅 12:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108166">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65716e5170.mp4?token=jjf0qBLUhmphQM8Eu4Zmo8mGoBbHy4-nPK1KoXRdqlAQ1H3prFXcNyhHpUBliXlOz0v-GqbtJz4lVIybjGD9yqWfUb3teTKHEIrPlNMdMjXlVBzht5nV9OBeLDBH94ZWKEIWw7msKxnCqzhX3kP6TYpZJQRqFMMmKoNvwCVnqN9HlEUJpHqxQzp-tMN3zyWbFKJ69u5EZo-dXfJRgn1XbdVIaZkUT6AKcO6k8imRQqLGejwGWhIzDsN2gvuqZYu9QbXDs6sbf6WAc9mSYplkPfeaNscU4lcsWkgS4TjUxNamxx8owZP3tHwQj3zUT_4xvNOd8dWC79DHtyaoYPmvrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65716e5170.mp4?token=jjf0qBLUhmphQM8Eu4Zmo8mGoBbHy4-nPK1KoXRdqlAQ1H3prFXcNyhHpUBliXlOz0v-GqbtJz4lVIybjGD9yqWfUb3teTKHEIrPlNMdMjXlVBzht5nV9OBeLDBH94ZWKEIWw7msKxnCqzhX3kP6TYpZJQRqFMMmKoNvwCVnqN9HlEUJpHqxQzp-tMN3zyWbFKJ69u5EZo-dXfJRgn1XbdVIaZkUT6AKcO6k8imRQqLGejwGWhIzDsN2gvuqZYu9QbXDs6sbf6WAc9mSYplkPfeaNscU4lcsWkgS4TjUxNamxx8owZP3tHwQj3zUT_4xvNOd8dWC79DHtyaoYPmvrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اشک‌های نیروی امنیتی آرژانتینی برای لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108166" target="_blank">📅 11:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108165">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97652f0e6.mp4?token=imeJUifcxXpuqcmyTphJV71LfXzd0tRlcpOD16hmlcRnNvQtrPvaRStYccSjCyI0kl9CTKfjBblyr8Lk-2ZTBd-V_9IzdZRiRvInNapgyN9De8_SvZKFzzOfFJg0beic_5ri79sA4gYXvAghrFOs2CvaclmvRAWuKdf03zpAjm7shHzpRTjk7ccHqvQVM8iOZQod7GhJCzKn2Sdt6GGi6RlsiabszHcRXhKoh5so8nyRj00KuB1vEslPEWSDxM9iHEaaUAtHV2A-gH9zd3Z6Bn89-dVuvkjYkUfCgQGdq__bxprfXZMOSFJ_utqcLZzcuMjk9OVKwE-bBxdJUDyG1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97652f0e6.mp4?token=imeJUifcxXpuqcmyTphJV71LfXzd0tRlcpOD16hmlcRnNvQtrPvaRStYccSjCyI0kl9CTKfjBblyr8Lk-2ZTBd-V_9IzdZRiRvInNapgyN9De8_SvZKFzzOfFJg0beic_5ri79sA4gYXvAghrFOs2CvaclmvRAWuKdf03zpAjm7shHzpRTjk7ccHqvQVM8iOZQod7GhJCzKn2Sdt6GGi6RlsiabszHcRXhKoh5so8nyRj00KuB1vEslPEWSDxM9iHEaaUAtHV2A-gH9zd3Z6Bn89-dVuvkjYkUfCgQGdq__bxprfXZMOSFJ_utqcLZzcuMjk9OVKwE-bBxdJUDyG1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
صحنه‌گل دیروز ذوب‌آهن به نساجی که به شکل بسیار عجیب و نامشخصی توسط وار مردود و باعث اعتراض شدید شاگردان حدادی‌فر شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108165" target="_blank">📅 11:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108164">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41de558131.mp4?token=GIePQk37hwWpRRNUwJCzxJpt7OMvzxoKW1NJFqMtIYg7NG86gPG-oSr199CA9AC-7EHwJS67F2kXAclHR73KjSAAFLM0tJ3fNfAh88VbHXzEiIJ0Ek4zSr8l5EWQRgF1AiEKzprqVrDqfeDViJ0nuWNely6rogggmhBGCun9yDR9jOYwzw5p6zoHCXMlTc2zysbOqpC4J1Xa7PZiXWvKtLD7QLDgm29ADNI1It8us3Wfii9VXY_LVThDnDFwzuyMDjnZVvrCWMfY4NZfBcPaGQV8170yYuWIOBbil020vboNtg4cZnDEdRPH4nG2o15sLGCxVyEpU4aUhOgpQiNGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41de558131.mp4?token=GIePQk37hwWpRRNUwJCzxJpt7OMvzxoKW1NJFqMtIYg7NG86gPG-oSr199CA9AC-7EHwJS67F2kXAclHR73KjSAAFLM0tJ3fNfAh88VbHXzEiIJ0Ek4zSr8l5EWQRgF1AiEKzprqVrDqfeDViJ0nuWNely6rogggmhBGCun9yDR9jOYwzw5p6zoHCXMlTc2zysbOqpC4J1Xa7PZiXWvKtLD7QLDgm29ADNI1It8us3Wfii9VXY_LVThDnDFwzuyMDjnZVvrCWMfY4NZfBcPaGQV8170yYuWIOBbil020vboNtg4cZnDEdRPH4nG2o15sLGCxVyEpU4aUhOgpQiNGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
هاشم بیک‌زاده: در تایلند اتاقمان کنار استخر مختلط بود. دستیار قلعه‌نویی نیمه‌شب رفته بود لب استخر و دخترا را دید میزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108164" target="_blank">📅 11:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108163">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndafn9U-6kO-zFBNbau6RAizj8V0gdYE5brpAtTa1QyyJL8rgObyLhiiqLho_BAZesEwiC9lrbJBWfBiteIfHJKTPxWuS6El3URVc5NXexdbCbcBjTnqn2wWx7D9sT7lhZ1Jnec5THi31zGqxtuvrdc07iR7MrUdNEUt3SlxDqQdkT8J5nQbGIHu9Wp-2qCBTmZ33vHECpxxbsvuVW_HGag72uI0JGC2v2wOEvalM731i5SMvyZHZPUOP4JEqBQwF0kauoW2xzr_IvqtW3o_Q_8x-Cx51PnEXtixySNoXSH2HND97_YtJ9jln5gxgPyCu5YsWJSn-rO60P4xu3gHFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
علیرضا بیرانوند اعلام کرد که از کریمی مدیرعامل تراکتور بدلیل اتهام تبانی شکایت می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108163" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108162">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b39729529.mp4?token=dmZjCv8IgMd7oTlT3F3-s6Y5ymsSO3Ft8cIiVL5qtleWjPEk3b8EWSWPV8U7LB1BshH7FBJOmqcEtjdOY1PYyEFjvJoh7CU9HQWOh9WlrQfrV3cy4C7lvtPVoamovOU3_pNv0F4CEc8nOs4tuv37lh7Sjj84l-OksIYZ6quhFYW5QWgBt8yH2l3d2bgBGXgGTnBnV4uSDfF7aYgOGrXxSuJTQDymFnnUDzGtGgJMx6RQP0pw0pYSiLQn0nTaHxkXSBaBSBGHokIUARZZq4JYbPkuayBf3KeyfIZuqEAJ43v4N5ZRu0SJzsaaxJinr461AYgiXY6tgcUmIJDXgYCHUjmoFUwiKnQj7eURebSr_sHpf-KD-MJiPGXzXrvWB0CsJhv1U68oWLG3N41vUHVqTMOQr8jGogUdEWaP5EIVWZLzfYXiEeLJ6a21hW_zEI_4TbtnsixFXWvdr-aZbiCgEoaDVNYb6hTo7h7ZlXzweho4XFCVH44qU5M2ndnWoccNGCvvIHUjhWJKc1E9tbidSlgNFC4kWnfxJ3NEltTT7-6CbtFCK1yFai58kahACVFUBDd-t24tx9BlhWQXhZWNkTr2tY7zWNj5DRBooa5m7WJdDDT2pQmTowzF5mmrYYgvy22ZClRAwk2azyNj8dkdhuKrWdLcK2Kp0JPDbNin_qs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b39729529.mp4?token=dmZjCv8IgMd7oTlT3F3-s6Y5ymsSO3Ft8cIiVL5qtleWjPEk3b8EWSWPV8U7LB1BshH7FBJOmqcEtjdOY1PYyEFjvJoh7CU9HQWOh9WlrQfrV3cy4C7lvtPVoamovOU3_pNv0F4CEc8nOs4tuv37lh7Sjj84l-OksIYZ6quhFYW5QWgBt8yH2l3d2bgBGXgGTnBnV4uSDfF7aYgOGrXxSuJTQDymFnnUDzGtGgJMx6RQP0pw0pYSiLQn0nTaHxkXSBaBSBGHokIUARZZq4JYbPkuayBf3KeyfIZuqEAJ43v4N5ZRu0SJzsaaxJinr461AYgiXY6tgcUmIJDXgYCHUjmoFUwiKnQj7eURebSr_sHpf-KD-MJiPGXzXrvWB0CsJhv1U68oWLG3N41vUHVqTMOQr8jGogUdEWaP5EIVWZLzfYXiEeLJ6a21hW_zEI_4TbtnsixFXWvdr-aZbiCgEoaDVNYb6hTo7h7ZlXzweho4XFCVH44qU5M2ndnWoccNGCvvIHUjhWJKc1E9tbidSlgNFC4kWnfxJ3NEltTT7-6CbtFCK1yFai58kahACVFUBDd-t24tx9BlhWQXhZWNkTr2tY7zWNj5DRBooa5m7WJdDDT2pQmTowzF5mmrYYgvy22ZClRAwk2azyNj8dkdhuKrWdLcK2Kp0JPDbNin_qs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
صحبت‌های تامل‌برانگیز مجتبی پوربخش درباره میزبان دوره بعدی مسابقات آسیایی سال ۲۰۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108162" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108161">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108161" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108161" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108160">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4sIT8QqfkIfay3fYcRkV5xJv-YE7qU0M-1RbUbvh75lCL4LN8G5ewqW2jlucksrUYs9VtuezPmKvwnOr97Q2VNPpa77OKyEdkzyB0z4kOg8IL2Oo3_mu-3mxQsRF8VEvqXNuALMoWlYEQPJIb7jgQf7ZJbxYvXTHqrDncAjaZZhyS-SeAdpBD6_XyaxSxSyVef2YsOY0Y9OEzyNyu-Q4b1s_WOsi2h9NhrXInQFsBl98f7esTsGf6nNKvsv-PI1VeC14LXtdu9FRbK6sOjYidvAU6fYC1j5d5aUELQu3lTcJk4BKaAQLcIQTZRW7HhRg3IhamzE4Vd9uTne-tDtzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیول
🆚
مالاگا
وردربرمن
🆚
دورتموند
لیون
🆚
لنس
صنعت نفت
🆚
پرسپولیس
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108160" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108159">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27270d1b9.mp4?token=sCUUddHwoead6fmcz94X_H3Q5Hj2QD8AXFjYpVNVvG-QpguKeLKujZTQ8scjKWrsBEx7MWMOASHMScAPloUq-x26QQfG3sjkPR7S215Y8AkvQC64A88N44ssweRkIRzYqywQ9lGtNowmehpWmyCSk3ozwzYaRYH4uYbhAT6nQ01LXRNKHZax4QwXOfW3NEvDwS2ADR7c4kNTUtAY694KtMBhsP_UcLdwjgz0zUDMp9rSr1iC-yNP3PlMiAhz6iQZtFmJeS9EBPPqDyGDpVoCo_PKY7snEKog-RIu_ucuAlQ0fA2GbtgoQe45_X_4MeYocjj-eOetlxlfQz0i6mzZjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27270d1b9.mp4?token=sCUUddHwoead6fmcz94X_H3Q5Hj2QD8AXFjYpVNVvG-QpguKeLKujZTQ8scjKWrsBEx7MWMOASHMScAPloUq-x26QQfG3sjkPR7S215Y8AkvQC64A88N44ssweRkIRzYqywQ9lGtNowmehpWmyCSk3ozwzYaRYH4uYbhAT6nQ01LXRNKHZax4QwXOfW3NEvDwS2ADR7c4kNTUtAY694KtMBhsP_UcLdwjgz0zUDMp9rSr1iC-yNP3PlMiAhz6iQZtFmJeS9EBPPqDyGDpVoCo_PKY7snEKog-RIu_ucuAlQ0fA2GbtgoQe45_X_4MeYocjj-eOetlxlfQz0i6mzZjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✔️
🇮🇷
فاطمه‌احمدی ملی‌پوش تکواندو که در ناگویا مدال گرفت: شدیدا طرفدار استقلال هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108159" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108158">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23161a114d.mp4?token=hfrgZxbbvwlBQXkejHqx9AkeohU3B5DLF2QyOINSbQHkrOrYw7qYOdyU9KY4N4K2AVN2-KHp2CWxDUKmISTza5Wyk6jasDzFjZ4L2dh7Hva9tHk9wzlbzDiFlH6Uz8VAsTQJoSxRUQeanS6cGZakLaBhNYQO53BPN0DiyzkVCN8kgHQCeD7WblctrGVodQTktebNk6EXMkJ6lTEOR9iC1iKL40RaDchAlVdYwEq20ALeN0pailrooNdUs5LtUB_a7yDjyTI_VUkRWdeouEsyvxwtNY5ycehtyyNfncOaHryYHbVOSkpmcM1P8NCX1nondyKclWWdQqT-veKAgHzEuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23161a114d.mp4?token=hfrgZxbbvwlBQXkejHqx9AkeohU3B5DLF2QyOINSbQHkrOrYw7qYOdyU9KY4N4K2AVN2-KHp2CWxDUKmISTza5Wyk6jasDzFjZ4L2dh7Hva9tHk9wzlbzDiFlH6Uz8VAsTQJoSxRUQeanS6cGZakLaBhNYQO53BPN0DiyzkVCN8kgHQCeD7WblctrGVodQTktebNk6EXMkJ6lTEOR9iC1iKL40RaDchAlVdYwEq20ALeN0pailrooNdUs5LtUB_a7yDjyTI_VUkRWdeouEsyvxwtNY5ycehtyyNfncOaHryYHbVOSkpmcM1P8NCX1nondyKclWWdQqT-veKAgHzEuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
فلسفه جالب نام فرزندان لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108158" target="_blank">📅 10:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108157">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50646a3df.mp4?token=YRhNyXCwSE5bfbb9CuEl8Aw2UNwoVF4zYfA82LBgAAaIOYociBJ1r8-qzieP4agRLtBXl5IUjX1pYrfnot28dhL-BoDg3ajcsENJknYxCoIwoNti0r4__RkZqKErVBNYSffAITgmHunMQfL68z6oimutGI640z7_6-tH0cBCx77J_6VbDjRL15Hhw2P750jCjsO2DicLWzgMKlZ27BUjglMGeik4K5A_6BeZxvk96fLN9mJQwpya-ibQ3icJ4G8OJh8CpRo4w7W1dWrNCW7a-5xYLcz2uEl235nxZJCw9hh7EKiDxj1hFsJ9G1Qfpx-Kirp_mfZkTc8CwfEvrlxHRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50646a3df.mp4?token=YRhNyXCwSE5bfbb9CuEl8Aw2UNwoVF4zYfA82LBgAAaIOYociBJ1r8-qzieP4agRLtBXl5IUjX1pYrfnot28dhL-BoDg3ajcsENJknYxCoIwoNti0r4__RkZqKErVBNYSffAITgmHunMQfL68z6oimutGI640z7_6-tH0cBCx77J_6VbDjRL15Hhw2P750jCjsO2DicLWzgMKlZ27BUjglMGeik4K5A_6BeZxvk96fLN9mJQwpya-ibQ3icJ4G8OJh8CpRo4w7W1dWrNCW7a-5xYLcz2uEl235nxZJCw9hh7EKiDxj1hFsJ9G1Qfpx-Kirp_mfZkTc8CwfEvrlxHRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
کنایه ابوطالب به نحوه برخورد بازیکنان آرژانتین و پرتغال با لیونل‌مسی و رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108157" target="_blank">📅 09:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108156">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9a44b2ebc.mp4?token=fqEw68ck8BKRBJnxoGhk6YUsaq5SGJmo5KftXf75cDjfuiInkmQTvXAnBu1f2hFg3Riz6d2E4AfK2cI2o-wKwj9oD5opdfd_-JWA_u_N7zRBERDwAu0HTd2V7F7lBG06E-6moA0BWeojjq-Y-wKkSxb_gO3T9CAzfVJdz9iJpk7ulDN7DXZ4ndLjRS1_Mq3X6CHoFA5m1B9nxL1PfyCELgeraoR83-sPu0yvRJbM4gWpnp1WcU8lZjLSFjzLWxvlBxDXiIRXU4a1GJYTXsHNbN3TkELAubTviOpHU_2IdBSf7eYRyh0v72O9F7GtQJUH6Ddq1gsnODtv22Xr6wsxWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9a44b2ebc.mp4?token=fqEw68ck8BKRBJnxoGhk6YUsaq5SGJmo5KftXf75cDjfuiInkmQTvXAnBu1f2hFg3Riz6d2E4AfK2cI2o-wKwj9oD5opdfd_-JWA_u_N7zRBERDwAu0HTd2V7F7lBG06E-6moA0BWeojjq-Y-wKkSxb_gO3T9CAzfVJdz9iJpk7ulDN7DXZ4ndLjRS1_Mq3X6CHoFA5m1B9nxL1PfyCELgeraoR83-sPu0yvRJbM4gWpnp1WcU8lZjLSFjzLWxvlBxDXiIRXU4a1GJYTXsHNbN3TkELAubTviOpHU_2IdBSf7eYRyh0v72O9F7GtQJUH6Ddq1gsnODtv22Xr6wsxWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معلوم نیست داستان چیه هرچقدر هم ببازه بازم از فدراسیون پاداش میگیره
😂
😂
☠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108156" target="_blank">📅 09:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108155">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
🙂
سرمربی فولاد مطهری: داریوش؟ گرشا گوش می کنم، وسعت صدای ابی را دوست دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/108155" target="_blank">📅 09:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108154">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77201b62ab.mp4?token=Ap71JGZG19asnHw4plO0iPp9R1KiFIgCQ5xK-n6QS1GaHkoSC_h6rFA3u2qoSoMfUkYZufFK2fA1SwgyfvCDChpAKWiIHpgGqIdZpmsaLzaxam--49BhpSzcZRCuIUphXox72dFV-uI5O-P-knnSDR7WIC68i5qrW9baTaV8Ygiv7gEgOvszEdglqo0TFRvlLEzHN9dIid69MxxY476Koj8RfYxRflRowND5DpndL2AGIyo1fuDIuXeQx8jEVWzna5EIhO5RituicxWuBx92ywziDfj_S1bAkoCmIq63tqDtTEJowRwCUVFyv8aBeORgIBdqJI5YRp1Pj6bEeg9cPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77201b62ab.mp4?token=Ap71JGZG19asnHw4plO0iPp9R1KiFIgCQ5xK-n6QS1GaHkoSC_h6rFA3u2qoSoMfUkYZufFK2fA1SwgyfvCDChpAKWiIHpgGqIdZpmsaLzaxam--49BhpSzcZRCuIUphXox72dFV-uI5O-P-knnSDR7WIC68i5qrW9baTaV8Ygiv7gEgOvszEdglqo0TFRvlLEzHN9dIid69MxxY476Koj8RfYxRflRowND5DpndL2AGIyo1fuDIuXeQx8jEVWzna5EIhO5RituicxWuBx92ywziDfj_S1bAkoCmIq63tqDtTEJowRwCUVFyv8aBeORgIBdqJI5YRp1Pj6bEeg9cPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
عاقبت تیم‌گرفتن با رانت و فشار بالادستی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/108154" target="_blank">📅 08:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108153">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108153" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/108153" target="_blank">📅 01:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108152">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB97J7T9tlC0jRGoRDHXr-x_ELuDBnt5UArnoMaEskZci_3eAgWiucXLt33AbjYvRtGciFSJ0T1uatW1AMbyrrscjjsXsukCI1LJbuYllPscFaOaZy2XHJbgzvqWnr2C-bGQnSorh_Q2gRj40BL2tI0ZOputls3VHuvCj81IHfuYAJ8w48Zc1qYBfGNriSfr27TtaBqE9vv3dyHT2AwG9K9uaQvShNtunfkarBYbhbN6cJEzDmjjIsaqwyCsoD5350CwXvXT4Uzl9PuXubvQwOsu9ENEzIghF9zilkYsP-ZtPbS1SzP6d2C28pCx8G-B-4fPSSvN_uKZIynAFzoSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/108152" target="_blank">📅 01:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108151">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7_1eUs4BYhL5tKAPtebQgAV8w-b31C9P2y8BVBWTdQTRLunF0yz5lDBkO9ThDxfFptoJuezhG_Chscz3WSthXZun_BCnXxLVdoiiXLhLdyAubCUC29HP1tAMyAVZCAih-cMBshFmZuclRCCMGHjSiEgT3Xc0kWrYRXqaVli1HZoukPcmteB8loTbGQNpsX4c3pXREE6mfOkkOUCe-kC1PcecluchuudaWZ8M9AsKhqVu9nN-8vWszMB8z0rUTmEy-nReXgLkcITkns55bQSpiTmKM0m3oZVrQ0SgL9vQcQ8OQsK-gvzmQabN6ACjCyv5GVG-IvQppfn74PkT9RWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇶🇦
نتایج ۷ بازی اخیر الغرافه حریف استقلال؛ 5 باخت - 1 مساوی - 1 برد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/108151" target="_blank">📅 00:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108150">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa5d1caab6.mp4?token=RM2ltJj0-qRBcD9Ov1M4FApNzFj8Ey3167m329E3lY8SiZ4OQlKAzOhjOOrFkOeLDyNPXAXZQW7slp9l8hdOkjrOC53969_BU_iF90_cq3eBL4v-KfiagF7yt3ZYkneR0XM_l4u0OKITsdp_IEiyfad9ezCilTIRDGOkdRXEUT5ttutNUCnFnD78UkN6P026aeuZu8pPzy7eq3zjDV6rfy0irkCH4IxpnOfMt31HEgBgDniHuLbN4OthtGioIJ-Nzer64Wv3w78J5kyc2yq7Yf0nElxsV0yJIIf4A99FFvaj3V7NtnJEE_oF1WTrUgQqT8vjk-V5G2MaP-lH8cAXAHHFQY3dhmydMVjCP0mAUpC9LKs2Ys5BOOszoie2Z1rwmyZO5z9t8HrBLa3_1OMXNjn2xfJC28UY6fcGJFzyUA8POdamPtkei66NJZlP3VM25KAVb_On7jl-8CkTS9rF6buN4vrCLTSxztbXrfGf6BXGLN9JKhPyS1S_fSpa2a5QCpo4v994_5SxhjxOWqCslmhl_6YITq00hfYS40Gs9v7SCG1KZFCMWPYHZe-BtOHNz34D-E5nQsoArgPcFUZb3-y0O7GCmCFPk1pjwecFSl71RpYRkFbhXli4nlCOGyvZpcYZTkT7fNYgHKOfQg2qLyp9okiBPRq8wNfgP4QBc2c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa5d1caab6.mp4?token=RM2ltJj0-qRBcD9Ov1M4FApNzFj8Ey3167m329E3lY8SiZ4OQlKAzOhjOOrFkOeLDyNPXAXZQW7slp9l8hdOkjrOC53969_BU_iF90_cq3eBL4v-KfiagF7yt3ZYkneR0XM_l4u0OKITsdp_IEiyfad9ezCilTIRDGOkdRXEUT5ttutNUCnFnD78UkN6P026aeuZu8pPzy7eq3zjDV6rfy0irkCH4IxpnOfMt31HEgBgDniHuLbN4OthtGioIJ-Nzer64Wv3w78J5kyc2yq7Yf0nElxsV0yJIIf4A99FFvaj3V7NtnJEE_oF1WTrUgQqT8vjk-V5G2MaP-lH8cAXAHHFQY3dhmydMVjCP0mAUpC9LKs2Ys5BOOszoie2Z1rwmyZO5z9t8HrBLa3_1OMXNjn2xfJC28UY6fcGJFzyUA8POdamPtkei66NJZlP3VM25KAVb_On7jl-8CkTS9rF6buN4vrCLTSxztbXrfGf6BXGLN9JKhPyS1S_fSpa2a5QCpo4v994_5SxhjxOWqCslmhl_6YITq00hfYS40Gs9v7SCG1KZFCMWPYHZe-BtOHNz34D-E5nQsoArgPcFUZb3-y0O7GCmCFPk1pjwecFSl71RpYRkFbhXli4nlCOGyvZpcYZTkT7fNYgHKOfQg2qLyp9okiBPRq8wNfgP4QBc2c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
مارک‌کلاتنبرگ کارشناس داوری: هیچ پنالتی روی یاسر‌آسانی اتفاق نیفتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/108150" target="_blank">📅 00:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108149">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/108149" target="_blank">📅 23:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108148">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czT0qKEUFKA1hQ7VexIVsAUL-88PwTWfmHrb91UQi3ugV8HhbS14kEfIBVlzGhqMh1TZvWInlKeSGP9lMDHHD7Wz439mLVDd5j_-18WBRDoFjxPqv7MndkUPLpG0XqpfE8oMbQNxIiB4hdWVLpKxI9wfUlXFU7e7fe7ZqxesJWReEl1wfiovGqJDUm-b59f8FNY8M49IWo2djmZXOH_7r6517f5aUyvRaLuGZFgtHGwKpooETREQoYeL_uUEQ00Axer9M2H0F8QnZFuhstangJ13CfstOGgqwFKC3EGPf-PtJkiJpE_oFwK3DF1ToKMs99g-usf56UIkbYBESq673Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
اسکای اسپورت؛ مایکل اولیسه تنها در صورتی از بایرن جدا میشه که به رئال بره. اگر مادرید پیشنهاد جدی ارائه نده، او احتمالاً با بایرن قراردادش رو تمدید خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/108148" target="_blank">📅 23:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108147">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAJ4aH6AcbcEeFNLNvKx-jAw8s-rqMVyZK6MmLx4ciMnXjgaXTg9lFZkuOl0JuOfQOvbAugHQtRIVFNn5pCuDn6t-7KRryHxFZgX202l8HVYYRETQJAo1XPAOzdYZ3tmpqz_ngCVILKAdNSc0nGybGLQ3rQNbAtqCvsNJuZFKb2aae-gcOTXpvJPGReFZKECg5GXOTozJw_3A7gBjRVZ-vZ2FVh0BNIgzIwHs5f4DdUBGxHIJKNm4TnCgSGHNpIKBXYOlSnvrleSJRJOQdeNAAi0a-pDIyYPntWOfB_xouSFEH2mPM5cUu5l4UTpGbnmwmyFokN8B1JiANy3nngLQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
⭕️
بیرانوند: استقلال تیم بزرگیه. فصل بعد بازیکن آزادم و یه تصمیم خیلی بزرگ میگیرم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/108147" target="_blank">📅 23:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108146">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQwFd6rpwOVaaZ_RBDoLzTCIAOnZ2h6-Gvq1qPwCKUgoBe243uS89t1c8SAtrdmEZP5GFlP7_FgOfo36iSVUMKl7qi0EiDFRgFKGn7-QkJdEYY_obVvzG5kCPJ4HcdL2uD_lbjm-tRuFmrKqBatzkroZ3XmRC9wwFMYh3g-GY1GHuQNn3C3cmaiSlikYvnDkPtKKRos2E9VmHsHrpQm00uwjPEAd8CWQCy8xRXT_MljNjQQnd_RVguTVVm5qV8YSX9g-lbnaZSkVlQ7DzbMuEthLp8aEh2DZitGbPo89H1qOUNZibYZfJCZUn-PEjiswmK0jQRtr9shyDGP6qPBakA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
👤
کنایه خداداد عزیزی به بیرانوند: اجازه هیچ حاشیه‌سازی را نخواهیم داد و از زنوزی بابت انضباط مالی قدردانی میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/108146" target="_blank">📅 23:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108145">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109c5cc92a.mp4?token=E8zCF8H8Et9QWbkMLIGFcCpACss-0aouJHKQUZfYIw3UrLUydsUY1f7L42cOQPbgnDnUslZU3SqysCy-d_yKNwCWiul9E7lfALXhmAn_wy1_JiQfmSHIWfCQHkkF5eh-3aefnoJPzu7mayIZRj6dnorCO_WKJ4CeSvlG88-7l77Se9NWKQJt0xOUIjvUS18Xtkg8MtDWmtDIFVOtGtcVtNU6JPGv9G8P8Ve3u6d7nueOjiWGd-2BIRwKLSAT3wePTlzn7L1rFwK4jQ95yieeBjgKmzVvsEyX5WogqfcHS6dJ-VfcRGmGtoK0z8IcT1X1T5lYk0lrfZYXcbEbysENOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109c5cc92a.mp4?token=E8zCF8H8Et9QWbkMLIGFcCpACss-0aouJHKQUZfYIw3UrLUydsUY1f7L42cOQPbgnDnUslZU3SqysCy-d_yKNwCWiul9E7lfALXhmAn_wy1_JiQfmSHIWfCQHkkF5eh-3aefnoJPzu7mayIZRj6dnorCO_WKJ4CeSvlG88-7l77Se9NWKQJt0xOUIjvUS18Xtkg8MtDWmtDIFVOtGtcVtNU6JPGv9G8P8Ve3u6d7nueOjiWGd-2BIRwKLSAT3wePTlzn7L1rFwK4jQ95yieeBjgKmzVvsEyX5WogqfcHS6dJ-VfcRGmGtoK0z8IcT1X1T5lYk0lrfZYXcbEbysENOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
🇮🇷
در اتفاقی جالب و زیبا جایگاه هواداران استقلال در ورزشگاه یادگار امام به صورت مختلط درآمد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/108145" target="_blank">📅 23:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108144">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBEKsftN_5LPmW2mnEtBkr49p4xqVrlb30Cxik24HARyL_CFMXEui9KqEAcAHJed7opnjNwVUY8kN-PceZE7TNI64NZFvSAF9o33ofHzRYYZ0lebM6QX6ETGzgfJ3N-ylyg9rBTqraHeBcwdfVDsYCR5CgHNJm80rl8JoxKlnEc_NaX-GUVilyHbADnho_itqmo6-rAowwMgosyk5P5b0SV-rbqmaRrMhF27DxpXPBzkfAAEhRnxLnaBWe1FsAzy2b1iibL0D7TzHxe1K3ghcvRcDqbHfxzPV0qQZa9v6nYMAqQEKkgd0oDO68L35lBhEoxov2UKAfRPSeV3T-nQMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
مورینیو در پاسخ به سوال درباره رابطه‌اش با داوران: فکر نمی‌کنم مشکل از من باشد. فکر می‌کنم مشکل، بدشانسی و حضور در باشگاه‌های خاص در مقاطع زمانی خاص بوده است. من در اوج دوران نگریرا به رئال مادرید آمدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/108144" target="_blank">📅 23:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108143">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRD8XVFdF-BUGsq153O3yX5XiMDWzpJyqHJIOpYueriB3dHjKhABvg2OSIlgHK4odNUnufUgDsIbhzwAI6V4jK-7-J6TS-k-MVSRvIvd0xixP7Os_cLzUGfMm7j1omJTCguha_A9nteOXqp7VP-Mo2ZQyhKie5Q3QTLzE3P7VdR54NDczccUs1urSzbmU1sGboilO54wxDb2BYjEZVETOviQEwcfdiKsUniRlkOWc6w_Nhbtva55TU9qlgmkTMHDwt8cko92BAOnnSg0xaaPC-cDJZfTlaJDhRj19sCh_G78KPqdIRRiTU3oSaAC8ETMqbo_qM1Twpuaj5Yip3qYMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/108143" target="_blank">📅 22:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108142">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVFkFRSTOXpD00PnYrl1yTc6XnxkxaFhu6CUd5fWZ4p_0NXhlaaCdHjJ_FiIPQsWfEj7mmGKvaFeajbcGw9cpHGc1e1Px1qXJS3g3K6uLbXqZ03GOA362z1VDlitNtH0KfEjnXIgIp6CCgyC2MRYe___LqXN2b_sIbfTpfo9_X3kmW7_C2RtHTfX0d90hqcYn1hJsMQlZ1osKgyFzV0vu8jungZCiBAjmSEX-OO-zuNq6CNhi_8pFkvrOo-e6r725gK8v9iRIOI2EDvWfQziFykzwOgB160mx_9KsxXye0kicoQcH2Ll9RHE-z_H_BBLfNMWESLnoUU-M0_6Zv3AOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد ژاوی اسپارت ستاره جوان بارسلونا با این تیم تا سال ۲۰۳۰ تمدید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/108142" target="_blank">📅 21:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108141">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jl30M9Ue7VnkXy-m8PeBBWIU6NzhRqyCC9Ihhp5BVORaKJBAjO7FNBaXLWga-r3KpuVe4i7L5GiUDnnQT7Gvq6ZBMZeERIFF2XoOz5MQht7nL2xJs3WGmduvHJqu7I7Ef8EGKHJzwVvODUkpLC6LALDKpXkUvvQ_gXJi655DjGC_q8e-xGZ3q0IFDboTc9jwwU1DpGx05cskg0zJbnKY2FSh0xjEoEiqhOT5FQw9VunfmsuINFHyN41YpBHxpK-xNO8YlukYcBF8_RrYAIlZwMVcv0D3-iT1XmdJHxIOwhb-PB_9_aiR6SCGLgwJKvxRcKSsZgV05qtba90k9LGerg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/108141" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108140">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMMoujYT6QtALRuATZbKVpMg_3BfoZvFb8GcInoiR1dBaPDQan0802mWMWe7D4cY2XJqI-4DQFmFZM01oxc81F-cTt84l7-81Hi_F138c0y9qNb11U_dn5a5HHcAfqw4SWYEyKUiHt7YXS7YAj0-LmY3GuQlCDJO9HGAQXT4yO1oZi0hmJm75-im_Pr_qdKMBCaFgk9HulxX9WcmivMsEO_JKuGY-jdkUbEnFoai3r_7Hc5Ne1UGcOz0jCGzeEGRSRsCKGn4mqli3p2W_EkLFrnlMAkv0UjpFmXnxyiDPeY6XPsNf8CF6u9zsIUiIHYAhQ9svylwq09EhSoVQKdBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/108140" target="_blank">📅 21:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108139">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14105f8264.mp4?token=SBPdIZJcgglvO5b5-B08Kl-PPPC7FP9qlxUgzs_nNOMhzRsZBGjvQHRgSrD1mvKC-YtCEwKgB_QcSp2dWdK_eVToYan0maGWLpBLVkqKbu1M_LsNp7lb-3-bbMEuQ-fMPgIA7T7LzKFJRMf9y0Z2wp2WUBWLRXlMl7z7N2KJxd9m4lb4K44sIKS5reVQizXKXMIS8RuSxJyEwDficqZHcSefaEcaluZPdxZkHF7ozXWguxAKE8po850mkGJT4ImevVKXvtsyTOm2hJLN4ZHm73YJIcNPm3zdAyzc-D_hUKOc-qjMBXe6xO6EpIrCtfV8BMBJe81L4UMWYWYgbS6P4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14105f8264.mp4?token=SBPdIZJcgglvO5b5-B08Kl-PPPC7FP9qlxUgzs_nNOMhzRsZBGjvQHRgSrD1mvKC-YtCEwKgB_QcSp2dWdK_eVToYan0maGWLpBLVkqKbu1M_LsNp7lb-3-bbMEuQ-fMPgIA7T7LzKFJRMf9y0Z2wp2WUBWLRXlMl7z7N2KJxd9m4lb4K44sIKS5reVQizXKXMIS8RuSxJyEwDficqZHcSefaEcaluZPdxZkHF7ozXWguxAKE8po850mkGJT4ImevVKXvtsyTOm2hJLN4ZHm73YJIcNPm3zdAyzc-D_hUKOc-qjMBXe6xO6EpIrCtfV8BMBJe81L4UMWYWYgbS6P4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/108139" target="_blank">📅 21:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108138">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApyxbfCYfh3wOr5iyA3q8FgIDSnPRRNvczvhh3hcBo1fwM_eCzJHVK6wQFOgLrkzFllYeNa7mb2kJ86bsNhZ23xq8ztCr90M-rf7muEmXfSl0GaFBIB6Rpd3-uYLqFxaZvDAcd33cO_kFQV7-NNUpbUyvCFwFyoLUiUclTQW0dGgQTalZPZ21wtyLUbHv5mrNG60uuaFdCtdPJ4zvE47za8KqNQ3IAhMr5pkNuGsweUb9_8PIJQHHE49KUZN7y2G2ZXnI9MvE_NzQTfcNIVoJeg2g10J2M2NZ__hIEDo9cKALxsnmc_FDCvBC9jmYQhqdp2jFOBKclml28VDlxZGAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
پایان‌بازی؛ گلباران شیرازی‌ها در اصفهان؛ نویدکیا پرگل به استقبال بازی بعدی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/108138" target="_blank">📅 21:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108137">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/846f23996a.mp4?token=P_gKjzJBPcOmCsYr4q792Rd18dqK_6SkuZPmmCpfGbRm_NmoImAsw4zTXIyvbmH6ySVHRGXyBZARmBOVGopch6r0Xhy_tHouW81_I6QSVfYM0ZfcKZ0_iAC4iFgxc6ddlrXt23NE8dpQrA7JS-w_ZzoHCJ99AznteKF1-beuZTrO0zUIWIn14h_6c4AlU_4vEC1Dqp11jd-Y2vVILFxyDJCO_HclA1hb__lgySPrhpIoUWTGlQ91v6E9R37mHE0VsGu0mEz9jA0hSdJg7HuAF3aY7U9CU2ZwgTbw3gRuN112UN2sLyS-EhNZXH4xCzZwk9AYT7BZmgJclrsM6R74LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/846f23996a.mp4?token=P_gKjzJBPcOmCsYr4q792Rd18dqK_6SkuZPmmCpfGbRm_NmoImAsw4zTXIyvbmH6ySVHRGXyBZARmBOVGopch6r0Xhy_tHouW81_I6QSVfYM0ZfcKZ0_iAC4iFgxc6ddlrXt23NE8dpQrA7JS-w_ZzoHCJ99AznteKF1-beuZTrO0zUIWIn14h_6c4AlU_4vEC1Dqp11jd-Y2vVILFxyDJCO_HclA1hb__lgySPrhpIoUWTGlQ91v6E9R37mHE0VsGu0mEz9jA0hSdJg7HuAF3aY7U9CU2ZwgTbw3gRuN112UN2sLyS-EhNZXH4xCzZwk9AYT7BZmgJclrsM6R74LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
⭕️
بیرانوند: استقلال تیم بزرگیه. فصل بعد بازیکن آزادم و یه تصمیم خیلی بزرگ میگیرم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/108137" target="_blank">📅 21:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108136">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d21db945.mp4?token=gFR9T7bN_dXhuyuVS2uygsbuRznrkvfTVgZEucCm_g3ti9N4loONru42HtNEFWs-Bl8NWniAl6_inPVI1c-eAr-wKJCCxVAimEliNFFDQHoUVMhFNUyLaXyzwVRQssL_tYIVh1R-OJNiUIwmdk5EPaLqhSo6DQTWlKJOaK-LlqPcAdUHKqSo2n2uK6_AuftkHCU9TcyL_Np6sLMoPqNyeR4JIt7NT21puzDhFTNVA4RZlPT34FtHkJliUql1F4Cbs_qgAGb0N9_qcOFOy82J5-3pSWNjaXBU62l8hvChfGAFpQz45QIGS8kstmApoR6LyH0RVMClPJOde-eY_eXRfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d21db945.mp4?token=gFR9T7bN_dXhuyuVS2uygsbuRznrkvfTVgZEucCm_g3ti9N4loONru42HtNEFWs-Bl8NWniAl6_inPVI1c-eAr-wKJCCxVAimEliNFFDQHoUVMhFNUyLaXyzwVRQssL_tYIVh1R-OJNiUIwmdk5EPaLqhSo6DQTWlKJOaK-LlqPcAdUHKqSo2n2uK6_AuftkHCU9TcyL_Np6sLMoPqNyeR4JIt7NT21puzDhFTNVA4RZlPT34FtHkJliUql1F4Cbs_qgAGb0N9_qcOFOy82J5-3pSWNjaXBU62l8hvChfGAFpQz45QIGS8kstmApoR6LyH0RVMClPJOde-eY_eXRfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‼️
🇮🇷
واکنش نکونام به مقایسه خودش و اسکوچیچ از نظر هواداران تراکتور!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/108136" target="_blank">📅 20:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108135">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGmh-ybJZ1GY0yV91ShK3hI0ddExIZ7JojGE06JMm27-ilqeXqdAA5DRqD2PLSLCxF1Ex0-kCz4brBnkLqev-uNz2rmwqIeUb5vM60ZkG6BLS7pUex-no8NRmv2j27Gl26DJS46pfcGnlc7jn3BDtLv98yb7JMHcLLq_ocpspw3X35x1A7hHNlzguvkVmQyLo9x0SxVeNWgEis6oSb8aecel8i5IjXQmHKkV0fymClPtJv50Jk1yetcGAX645d2ae0Bxh082LDJezjdnwqfTLAxuql0VeiQ5hvXGiYE3XgT8aVRNSNG5tdAA8iKhY3Xz4ppF6wpQc_-Kb4kvAvpZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
گل‌ششم سپاهان به فجرسپاسی توسط شفیع‌دوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/108135" target="_blank">📅 20:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108134">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a8cc7873.mp4?token=iXe1qdJL-Vbppe3uPH04PzMg2Ju5dSP8T0zJFfv_S1xo5cnPRwi2v90sO5PNU9MLvs2g1vs4VExdU3tZ-viswlu5GibQ1xZBOLfRn54V1NOZD3sxTIaNsafYPfA_yJ53pGcVAOrH44KGb1yOZes618eQs1W3Dy2WRgAPT-pCsKUfMjQTQbXmTNZLwsqohiop7Pum7cALQxTiK5lSKZ2fxaVdrdu8xlLyhUpcoylBjoehrh2OyUMZDxwySkH0EE1ZnLGaE_ygaDXqxsDkT0uvfV3GkNEvSH8AfJ6wQPl2306nYm2Te1_aASfl5aYXtnyuaNW8hnxjW5YUS2rS8lbK9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a8cc7873.mp4?token=iXe1qdJL-Vbppe3uPH04PzMg2Ju5dSP8T0zJFfv_S1xo5cnPRwi2v90sO5PNU9MLvs2g1vs4VExdU3tZ-viswlu5GibQ1xZBOLfRn54V1NOZD3sxTIaNsafYPfA_yJ53pGcVAOrH44KGb1yOZes618eQs1W3Dy2WRgAPT-pCsKUfMjQTQbXmTNZLwsqohiop7Pum7cALQxTiK5lSKZ2fxaVdrdu8xlLyhUpcoylBjoehrh2OyUMZDxwySkH0EE1ZnLGaE_ygaDXqxsDkT0uvfV3GkNEvSH8AfJ6wQPl2306nYm2Te1_aASfl5aYXtnyuaNW8hnxjW5YUS2rS8lbK9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌ششم سپاهان به فجرسپاسی توسط شفیع‌دوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/108134" target="_blank">📅 20:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108133">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded4443f3f.mp4?token=gu66U0jR0Md40QY7-ixccC6VB88lbvMtjwuI2C_V7l6BbsOrBMDaFP0Mz4wAJs3hYuxCzfs40VNE6dVyD-2acW8celUWZRu_kMWVJqH5lVtheUeLhQxX6n3zCHHHK6eYIBEqUklXx4d27XpCPjCwIZkeSjiRxkz3gv5Hv7LEgh-3XfrufGfdk4mp5uJXZ8UlF5O1S8jqMXnDBSt6qkl2DPNMnVhg2vgyu1CMV2MvOPnM32YYpzhgfUr12J2ZEBtwnZ7RJcwIQFvXsZvoQlCrT_--LkDlD5mESZpymCpU6OrXz_pnrFyuaGmi2lHi5AWTva2gKmFm_oZDfRwqo3vr3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded4443f3f.mp4?token=gu66U0jR0Md40QY7-ixccC6VB88lbvMtjwuI2C_V7l6BbsOrBMDaFP0Mz4wAJs3hYuxCzfs40VNE6dVyD-2acW8celUWZRu_kMWVJqH5lVtheUeLhQxX6n3zCHHHK6eYIBEqUklXx4d27XpCPjCwIZkeSjiRxkz3gv5Hv7LEgh-3XfrufGfdk4mp5uJXZ8UlF5O1S8jqMXnDBSt6qkl2DPNMnVhg2vgyu1CMV2MvOPnM32YYpzhgfUr12J2ZEBtwnZ7RJcwIQFvXsZvoQlCrT_--LkDlD5mESZpymCpU6OrXz_pnrFyuaGmi2lHi5AWTva2gKmFm_oZDfRwqo3vr3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌کاشته مس‌شهربابک مقابل فولاد خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/108133" target="_blank">📅 20:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108132">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
📊
🇮🇷
جدول لیگ‌برتر پس از تساوی امروز استقلال و تراکتور؛ پرسپولیس در صورت برتری در دو بازی پیش‌رو خودش به صدر جدول خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/108132" target="_blank">📅 20:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108131">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cf998598.mp4?token=rn31RFtpclNaXcupTv7JLRo4WaTUQWlKycWtr_YFS36YLCRGLuRT7f3l5OnrS5axzy63EVyVKYTG5fSVKwRd_6R3jZHglIvnG-HS4ebLUGEfwdbkV07EyxutiK3qDoJCbEb1tJk0nldYHCeWGYfu52IROrNfb8dr-eMn_wwCmNu2SXVUagI_6y4zKmV6tCRSu4K_GEHwNNSKUDo2ug7lWfnvxRtuCJNFk2DDJP2CNQpIyasteyAeJPXV5SUrYz9CMNGwvoz9fSlWUnhx-vbNXxL7pRf_1yro2KgwpQcmlvWnIboFxcxj1SQMzKck92Ox17jGdzm4U6U3VODA-Fpw5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cf998598.mp4?token=rn31RFtpclNaXcupTv7JLRo4WaTUQWlKycWtr_YFS36YLCRGLuRT7f3l5OnrS5axzy63EVyVKYTG5fSVKwRd_6R3jZHglIvnG-HS4ebLUGEfwdbkV07EyxutiK3qDoJCbEb1tJk0nldYHCeWGYfu52IROrNfb8dr-eMn_wwCmNu2SXVUagI_6y4zKmV6tCRSu4K_GEHwNNSKUDo2ug7lWfnvxRtuCJNFk2DDJP2CNQpIyasteyAeJPXV5SUrYz9CMNGwvoz9fSlWUnhx-vbNXxL7pRf_1yro2KgwpQcmlvWnIboFxcxj1SQMzKck92Ox17jGdzm4U6U3VODA-Fpw5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
💙
سعید فتاحی رئیس سازمان فوتبال باشگاه استقلال: پیشنهاد داده ایم تیم‌هایی که جزو 8 تیم برتر جام حذفی در سال گذشته بودند امسال جام حذفی را برگزار کنند. پیشنهاد خوبی هم هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/108131" target="_blank">📅 20:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108130">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/251e2a3878.mp4?token=gJxvVFCLGZF4eFsFor8eFqpEcaWSW5fx2P3l9SDdIXjJw22gdi0bp_Ph01Ky-CAuAM_LtS0RLw2tQvo9E5B7B2cv1fIvXUoRw4_1F3M7jAMFzyXhrh3nuYGa9uJMqvkaA0MfzDuSl7NdNyohV-XygsGtMwhRRCYNgw8PUS_eVlDdQveTPO0B79FdE6bHOpT4zotj5IqhcI4Ebia1S6HDSHB6Oimu3Wuci6QUB6EeVBo8txqiq9LWYL3JeoWFmUim9yQZXM2HoHEkiDo4C5TVcRrGtoAhmcBxRqux8E5Q6mWi4Ijsif1CBxNnZBM57fFfSsFAyhR4uMaL-eqI0HjgDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/251e2a3878.mp4?token=gJxvVFCLGZF4eFsFor8eFqpEcaWSW5fx2P3l9SDdIXjJw22gdi0bp_Ph01Ky-CAuAM_LtS0RLw2tQvo9E5B7B2cv1fIvXUoRw4_1F3M7jAMFzyXhrh3nuYGa9uJMqvkaA0MfzDuSl7NdNyohV-XygsGtMwhRRCYNgw8PUS_eVlDdQveTPO0B79FdE6bHOpT4zotj5IqhcI4Ebia1S6HDSHB6Oimu3Wuci6QUB6EeVBo8txqiq9LWYL3JeoWFmUim9yQZXM2HoHEkiDo4C5TVcRrGtoAhmcBxRqux8E5Q6mWi4Ijsif1CBxNnZBM57fFfSsFAyhR4uMaL-eqI0HjgDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌پنجم سپاهان به فجرسپاسی توسط لیموچی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/108130" target="_blank">📅 20:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108129">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f44126980.mp4?token=jbSKionjVlQAFdR877P5hgAxFopcq6lNQpW21729KXAMj-c1W9YbEgX-FFGJA2jHBgEdk41CfXR9ga_kvUT4mbdJA-bpn2G5dzxi2QzNzNaJPLA-5WgFGSnZACLd2ZRCBR_NF5jBgqbQGdBVHWni42L2CFTdBAFxndvu2255x-pTZPZxU7y-oPj_93Am8sePIUtvxX_GLtuUp2BKGqpw12enR79X4tPHP0jN_JhvubH22yVJNEHiiVne8ZqaDQdO2u7P13rASKVqyPdsfNzbecua0tJHeUIuPdGtoS5dl79tN7DtISjE3z6B6-QPnkHKFP15YajAaH9hS6zmBBPEx2fePDM7SaIdY07f2IFlJ5b57ZEpqwBVDVQcy0zRsDmZlo098ptXSCV-M5tzdzZ2lk0BDUwB1dqE7oILiB9oc8XU1pdQLdU_hiJ9Mv4tZ4eSyl036r-NHGIE2oXeo7ZpbTOj3HoM7HpHlKxpI00E5Czn34yUMYBk4ov0R4a89tShcmUPokIpx1DBRfm8ltjbzW7N8rR4jStE98_8MHtqViZy4FylTEeUd_RSRI0xJOpD5vduJA1FhuF34Q2uHvTTzdGy_aD3_0NINcr8r1B67Gwxe2IVixofPV5Ymwln1LOc0G4s0yrTWA1uCHRhhWYQOWZw9cvypc-aRblGU6dHHW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f44126980.mp4?token=jbSKionjVlQAFdR877P5hgAxFopcq6lNQpW21729KXAMj-c1W9YbEgX-FFGJA2jHBgEdk41CfXR9ga_kvUT4mbdJA-bpn2G5dzxi2QzNzNaJPLA-5WgFGSnZACLd2ZRCBR_NF5jBgqbQGdBVHWni42L2CFTdBAFxndvu2255x-pTZPZxU7y-oPj_93Am8sePIUtvxX_GLtuUp2BKGqpw12enR79X4tPHP0jN_JhvubH22yVJNEHiiVne8ZqaDQdO2u7P13rASKVqyPdsfNzbecua0tJHeUIuPdGtoS5dl79tN7DtISjE3z6B6-QPnkHKFP15YajAaH9hS6zmBBPEx2fePDM7SaIdY07f2IFlJ5b57ZEpqwBVDVQcy0zRsDmZlo098ptXSCV-M5tzdzZ2lk0BDUwB1dqE7oILiB9oc8XU1pdQLdU_hiJ9Mv4tZ4eSyl036r-NHGIE2oXeo7ZpbTOj3HoM7HpHlKxpI00E5Czn34yUMYBk4ov0R4a89tShcmUPokIpx1DBRfm8ltjbzW7N8rR4jStE98_8MHtqViZy4FylTEeUd_RSRI0xJOpD5vduJA1FhuF34Q2uHvTTzdGy_aD3_0NINcr8r1B67Gwxe2IVixofPV5Ymwln1LOc0G4s0yrTWA1uCHRhhWYQOWZw9cvypc-aRblGU6dHHW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🇮🇷
سوپرگل امیرحسین جولانی بازیکن فولاد خوزستان از وسط زمین به مس‌شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/108129" target="_blank">📅 20:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108128">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRvBmvp0iVMqsKTasIKSbxvjdE4X6dFdWRGGqKS9ABPO3ZWVcchxK4z7mr036USUh0uXn5AhEx0aEU1VfD63uCqhU5Q5lh5xSLDC43EmB7nqVK6aI6uzba_tgiebqMFklLdlmoGiqQ2HUDwlAwXlWB1nLMvr07YdWuewga-1VGjpVJHoQBlIuADLmxqFssnWDv7tSU-Poavts9FheAHCz2jzzFaVDlsTnrZFGTD7XC02Bh_jWCHKSqzAsfQmV5ZqNoXUojFDZSMDncwdz9fz5TyNzhChVg5-SNqSSpPLiYBxfsIPehUD7sZyt6q5r3z9UKO6ktbe6-LipLk-0zyC6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
❌
مدیران پرسپولیس صبح امروز با حجت‌ کریمی مدیرعامل تراکتور تماس گرفته و اعلام داشته‌اند که اگر در بازی امروز مقابل استقلال موفق به برتری نشدند، می‌توانند با همکاری و تعامل با استناد به این نامه(صحت یا عدم صحت آن مورد تأیید رسانه‌ما…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/108128" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108127">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36afca847.mp4?token=FPGHh42_WwmKSWA5cRwBZU2F0YmmXW0EeXjZlRRMRJt-60yxdhTgYbpdckb1je6VQ0JpaaiFZ9I7AeNLT-gXfwxP2jOb1-TxLYDT69sZnHq6kEQcjniLyf6W8lBA7KgLN5muhIcI6iUMVFqgIO6dC6Dm6610xveUyNtAPa62z0s9R6WQsm80U0A1ReXojowj1leMJi1wqfTY2T7ztb6LdbdCHl6aOqQCNxmfi7q7-spUo7TiclQq2s-4WKcaJhForyeyfHz21Ddee6iFKBE6PrYMXf5Guk3WcUFwlBmdMcpVgGQRGqz2UEBKnhRNM3B4TK6TMnVpKUJuVdgNynBnCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36afca847.mp4?token=FPGHh42_WwmKSWA5cRwBZU2F0YmmXW0EeXjZlRRMRJt-60yxdhTgYbpdckb1je6VQ0JpaaiFZ9I7AeNLT-gXfwxP2jOb1-TxLYDT69sZnHq6kEQcjniLyf6W8lBA7KgLN5muhIcI6iUMVFqgIO6dC6Dm6610xveUyNtAPa62z0s9R6WQsm80U0A1ReXojowj1leMJi1wqfTY2T7ztb6LdbdCHl6aOqQCNxmfi7q7-spUo7TiclQq2s-4WKcaJhForyeyfHz21Ddee6iFKBE6PrYMXf5Guk3WcUFwlBmdMcpVgGQRGqz2UEBKnhRNM3B4TK6TMnVpKUJuVdgNynBnCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل چهارم سپاهان به فجرسپاسی
آریا یوسفی در دقیقه 54 دبل کرد و گل چهارم سپاهان را به ثمر رساند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/108127" target="_blank">📅 20:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108126">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb8c7cf69.mp4?token=oZs7UaQma3mtXz6tyYAKOXxQY9HSvHrYKBHAaz3TJOTe2iJzPI2FDJgd22cJDKbB94XHbiEpB8zlBuNridH5mcm5wf-aovWFcU65T2kG29wdWsF59bnCNgKP6VHJs3mfas4v0BeQRNI-bsbMBtTKwxHplpyvxWUZnmpUYr1-PYYct1m2JfTIi6kTRRNpszxuV-trXq-Wv_ffG40QLZnMrnk0_ULqzX2aUFZ6rWjkuKf-PNpeKBoddlem5WIaUAHyoMtli3Kd7z0jqkRsz32Mdp5tnSFiGbPx-2QkfZRb5E4vuzFojWJg7O71i6G4vTUpr5cUnNkrsxKFkSJOvviylg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb8c7cf69.mp4?token=oZs7UaQma3mtXz6tyYAKOXxQY9HSvHrYKBHAaz3TJOTe2iJzPI2FDJgd22cJDKbB94XHbiEpB8zlBuNridH5mcm5wf-aovWFcU65T2kG29wdWsF59bnCNgKP6VHJs3mfas4v0BeQRNI-bsbMBtTKwxHplpyvxWUZnmpUYr1-PYYct1m2JfTIi6kTRRNpszxuV-trXq-Wv_ffG40QLZnMrnk0_ULqzX2aUFZ6rWjkuKf-PNpeKBoddlem5WIaUAHyoMtli3Kd7z0jqkRsz32Mdp5tnSFiGbPx-2QkfZRb5E4vuzFojWJg7O71i6G4vTUpr5cUnNkrsxKFkSJOvviylg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🟡
گل سوم سپاهان | احسان حاج‌صفی '47
سپاهان 3 - فجر 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/108126" target="_blank">📅 19:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108125">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da3e24c2e3.mp4?token=O9i0wP0EzQOGQKgcdBEfTw88A3qCRUrcHPT3RekNIHje5NnO8TMv-ij19X3kdvtD8Ry4L6feAzsN5XzEbUl2MMD6F3Rf--1AMUO8-nCGeVcYCJ-y6twZx093jB6qFY-6kMEZGlaueKU5_m-BEZPE6RkolB2n2XbNMksPjpL4NEJWLpHZwuiiz6MRXBhsaQ4fmC1QqCPchST9ayt07FI-zxRiAafOJnGzgazbAMmvyKiJoo4XqfmG9sNBwAGSVnFOZngK5NEhTuyngARW05JjjhIi6rJikpLn62sKkdRDZD9r3Er5VaN3CdQHrB4tP1F-I5Qy3jMH-PklnPFYTeYNaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da3e24c2e3.mp4?token=O9i0wP0EzQOGQKgcdBEfTw88A3qCRUrcHPT3RekNIHje5NnO8TMv-ij19X3kdvtD8Ry4L6feAzsN5XzEbUl2MMD6F3Rf--1AMUO8-nCGeVcYCJ-y6twZx093jB6qFY-6kMEZGlaueKU5_m-BEZPE6RkolB2n2XbNMksPjpL4NEJWLpHZwuiiz6MRXBhsaQ4fmC1QqCPchST9ayt07FI-zxRiAafOJnGzgazbAMmvyKiJoo4XqfmG9sNBwAGSVnFOZngK5NEhTuyngARW05JjjhIi6rJikpLn62sKkdRDZD9r3Er5VaN3CdQHrB4tP1F-I5Qy3jMH-PklnPFYTeYNaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سهراب بختیاری‌زاده : یاسر آسانی بازیکن تاثیرگذاری است/ بازیکنان تعویضی تلاش خود را کردند.
🔵
کادر پزشکی تلاش می‌کنند تا او را به الغرافه برسانند.
🔵
امیدوارم مصدومیت او جدی نباشد ولی احساس می‌کنم کارمان یک مقدار سخت است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/108125" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108124">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbd7f5f47.mp4?token=NvQNm1pkB97qCvcK5HoeIradanOjN3LOt-xORKnvCEQ4ZHvnE6reBR0AC3WCA5J620qsQPtkRCtQrGaTRHrwozZhwO4t0oJ3XReDCvuVXADVeTSEmO_g1FxOW3cd00GOZMQoAzzZzs4oc75c1-v8OcVp3cfZeRZqlkdC2_7V3LKc0286TOw88NbjiucJu1Ch2jVFvjyM3OTWnNs8BsXExnpTRMiDbMvLy7Q0Z-F_v9WvMyoAcyFL6YLcY3mhg6eHpYL4053o59hLldSQscdyiI4NHZpMp4AUWpSKjkLH6U93NWXbkU8NYbADAGUFsjp0RA2lxapANqgi4Pc-u_aoLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbd7f5f47.mp4?token=NvQNm1pkB97qCvcK5HoeIradanOjN3LOt-xORKnvCEQ4ZHvnE6reBR0AC3WCA5J620qsQPtkRCtQrGaTRHrwozZhwO4t0oJ3XReDCvuVXADVeTSEmO_g1FxOW3cd00GOZMQoAzzZzs4oc75c1-v8OcVp3cfZeRZqlkdC2_7V3LKc0286TOw88NbjiucJu1Ch2jVFvjyM3OTWnNs8BsXExnpTRMiDbMvLy7Q0Z-F_v9WvMyoAcyFL6YLcY3mhg6eHpYL4053o59hLldSQscdyiI4NHZpMp4AUWpSKjkLH6U93NWXbkU8NYbADAGUFsjp0RA2lxapANqgi4Pc-u_aoLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🟡
گل دوم سپاهان | احسان حاج‌صفی '38
سپاهان 2 - فجر 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/108124" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108123">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8faa668d.mp4?token=LIMIJ8PSQgTkF5-ubLixTgpSzSKZJ0Jjzwe27Y_PUi4uz-FktO6Ftmdo3TRphiMWszvMXtXjJCLD_XSmS5PxiBQ3xMuQyNoI9Xs1SD5empTKWXjYCHMQJPuKXTzrBOvEOYs5aRVaUVMuQLNaMji_KetgificFZH4-dOmiUu63RiIXt5wD8gdSuIjH24wiW4A4YnJ2MiaNX83Kl47hiIsLKp-XLooQlEKEYfmDSDkqGGYFQXZbmyeuZKoU-08bbe_xJs_9SvE9DH8Lry3lt30V6op2zwkxthEwBEipNPpRFkyjQPQBzwOEKBO-MrCVZy81VS5n_unjZmZvHWCObI2XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8faa668d.mp4?token=LIMIJ8PSQgTkF5-ubLixTgpSzSKZJ0Jjzwe27Y_PUi4uz-FktO6Ftmdo3TRphiMWszvMXtXjJCLD_XSmS5PxiBQ3xMuQyNoI9Xs1SD5empTKWXjYCHMQJPuKXTzrBOvEOYs5aRVaUVMuQLNaMji_KetgificFZH4-dOmiUu63RiIXt5wD8gdSuIjH24wiW4A4YnJ2MiaNX83Kl47hiIsLKp-XLooQlEKEYfmDSDkqGGYFQXZbmyeuZKoU-08bbe_xJs_9SvE9DH8Lry3lt30V6op2zwkxthEwBEipNPpRFkyjQPQBzwOEKBO-MrCVZy81VS5n_unjZmZvHWCObI2XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/108123" target="_blank">📅 19:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108122">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f54d246b.mp4?token=hA8EHLlXpFPjyW9OloldkBVRuhfFHSAS86zwXfsq6mpNOFzwPL9UOj6a1ua9VlukpVGOPAduHnw9QJeczyALEsZ7bX5hxhKBDh4b7xSsAbnLRrgESYVCYL0LWTARr723RjZiiMb1SeNZ1vhk6H8clEA6ERR4HmowT4RN0NJeZ6RgxIr8M3ThsR-T3WcqkTv7jx-trqtW9obIwAQwj6PB3UG0j0x1HLyp6Sk0EXyQtxixOiea14t15Ga3UYex2QWqTbL0G-qb59h5tIJyuVa5WS1zuKFPsc-P3gxHr5rHxcoURVZZS-59MaFNxzHaRoVrYwyLZnwrfDCwfkbsgUyfqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f54d246b.mp4?token=hA8EHLlXpFPjyW9OloldkBVRuhfFHSAS86zwXfsq6mpNOFzwPL9UOj6a1ua9VlukpVGOPAduHnw9QJeczyALEsZ7bX5hxhKBDh4b7xSsAbnLRrgESYVCYL0LWTARr723RjZiiMb1SeNZ1vhk6H8clEA6ERR4HmowT4RN0NJeZ6RgxIr8M3ThsR-T3WcqkTv7jx-trqtW9obIwAQwj6PB3UG0j0x1HLyp6Sk0EXyQtxixOiea14t15Ga3UYex2QWqTbL0G-qb59h5tIJyuVa5WS1zuKFPsc-P3gxHr5rHxcoURVZZS-59MaFNxzHaRoVrYwyLZnwrfDCwfkbsgUyfqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
شجاع خلیل زاده بعد از پایان بازی با عصبانیت بخاطر تصمیمات داور، راهی رختکن شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108122" target="_blank">📅 19:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108121">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238e05c12f.mp4?token=QjroO2EH2iYBgU-WoTDjJZsqD3_M8hLjGLrPC5uIFNxGwn6Wb_y7XKm0Kne9nWZ2dfYDCbL3ZsvC44_AJo9Qg8KLH_5wQJn2i7LjWUs1UjKaiWg4aMDvyrdGUbrh0DjQobDBNMeNkRet6LwDu3V5SmEHxAYoaGm3GZCIJB7BTN5s0Qsy1fkV3VmqvsS7K-mD84oHpcqCI4vMA3SckPkUG8z-e0ZyysM6Ipf6cAPwlwyJJTrNF2fVpA6-5sMfR9iPIqXNPbnlWkPZY3jtiFfLPdjpAAxYx6IHEwGxRKWP4dI66j9lGwOw6xKGd5_M5OmsNctcBMSZusL54ycADu7m9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238e05c12f.mp4?token=QjroO2EH2iYBgU-WoTDjJZsqD3_M8hLjGLrPC5uIFNxGwn6Wb_y7XKm0Kne9nWZ2dfYDCbL3ZsvC44_AJo9Qg8KLH_5wQJn2i7LjWUs1UjKaiWg4aMDvyrdGUbrh0DjQobDBNMeNkRet6LwDu3V5SmEHxAYoaGm3GZCIJB7BTN5s0Qsy1fkV3VmqvsS7K-mD84oHpcqCI4vMA3SckPkUG8z-e0ZyysM6Ipf6cAPwlwyJJTrNF2fVpA6-5sMfR9iPIqXNPbnlWkPZY3jtiFfLPdjpAAxYx6IHEwGxRKWP4dI66j9lGwOw6xKGd5_M5OmsNctcBMSZusL54ycADu7m9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
گل‌اول سپاهان به فجرسپاسی توسط آریا یوسفی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/108121" target="_blank">📅 19:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108120">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RURXecaUsa6GfCWAOfaz5P4NJcrdzpuQQ7rRXPJe_YvKtNTDhtKp3Chnbc93AX89YDgH0VSJ8e4jT3UjTb2fxWhqlh6jokMh_DnXM8rZjthMzHSi3fEgYxC3ZsXgdNK8_IHQAv3BLrpHEUB8MoNLaYF5fA802m1wE9cStr4L1W2pmxjUO0y78eT-WJ2KBiJpEPv4Lv9Axao4_Um2Y-Dr7yJxYM4UIq6FT3FOYlykomUk70d-BZbXOfawDb43fKLk9UYqVDrBN4sVpqpUjEb5QbkoVZqR6WIen_pSr3ODg4yTCL9K8xMqWo_s9HngbHZjpoYc-dq4ng1mYnNKxkN1Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/108120" target="_blank">📅 19:03 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
