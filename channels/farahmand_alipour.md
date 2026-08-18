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
<img src="https://cdn4.telesco.pe/file/Qod_bS7doGSPh2lfpiMd0k7LrSIz_mkwuL019Ct6bH6o7DR2Ffvq7O1lh9o8cXwMdWeW7NChZCISAkOuWLUXx8ycVE0oktDPBMGpqAz1CZJ0gReCQAmdvNFc4LNDojqsdWS-Ll6TnDxJJtKxCQQeFTcD7UNME0e_GBRNNfdzosFA143iXGn22QpErjCKnN-S-NVjGT1lvKLFgjh-rSRQblFkvIfoDWURkZRpWVxg0feXm6cDRgQpMBbJ1-YFYGyEdKg4b8A4C5hUW2FAoxT4tgUQVk7rvBd7oP1EN0G0oJogXkZti-JK3NMka0UQcZmR5tLYCk_YlwfM2_r9z7F-6Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 19:03:10</div>
<hr>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTa3smGv5aP9_vJ2GqQDm5Ms6iwvSCtVBUeXkkKSV-Lk_TEfvaiaWa3LHyZUr8vQxiP5jFuOmdBgl0I3pZlTuI1Vwvoqwlh7cS5y202vLU9QTS1xy9NXBZ4TJ77uYu3dOdRQCXGQIriY3gswbLlWnsjoyB2QE4QI3ulENEG58fEYwGDiqV_RHvtKr-U_vPSvcdXao8H66ycbWA-1OQl-0k4dEv6Hah7jK4YNjJEPN835GFP9QOmY4vwzyY7iRqvIAmWsElz7Z5-nACMiU6u0mJrTDpakaF65Pe3drFAtX-A8CIBLp911jf6VeK4nuPDBGa1Qv2l6zAcWw0v2iCPlQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHS-fyMoAv3AITT3WpY3hgOjnkHk_wmX20wPykt-S9PB874v5ZKqYYXLL4gmhfXZHbhMQxxtCQHulnU7gdnmoFjBVKLEGohsTnEiQ2MBborOhdQq_0vyOgSCWeoNayqCWxVlRS65wt3QSx-feoWbQIgkCXmeMeUIQQbH7GwMssczA1gAM9J8rxE-TTysnMFVNu-c6VYcOohWESnt7ydcC7oChcPXP9D5tUq7owlJSxO0IbEhnHuXud1OmoIPsyvrE_RCkL-AkeWbkiYEU-ovVzXTcqjxYc9S4bzfxhoz9hrbGmhC1eqdNCF2Pydu_rlnVMbResjipF4rLGxDb8zHzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUZq6NeLqBt8GfP3PyI-u4zo1ky0lHw_TGl7Sa0IMHqCQDB-yV-uq4cZ6M5p73ev47gq7dMKx4mXPFu50Mo1qvuynjYpVw-JkX9Iq1PczxUisNYuiuYGwnxIys2kvBNbV_RkKpHTOm4x04u7I5LEa81CIafFvGmIPS3JXeIgUMwa4qXxLyCk4NDdtmsMjLjj6vwDHxWz_TP2W5-rXciF8RoxCsVKMYyLnl3i_fD7AxU5PHC6PCF_oAx175M0huqhckdqxX0jNGwuUemc7auo8HNdVoQMUIl0okgCKxciZrwfv9GrYRlQT71GeBKmNyoyk9bzQFIVLE6XMRB5_GvBZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY3yW0v-Pgks9oDGstGbQPlsJ9eB-iPb1emBmNWvgedDtAo8MzkERO1lgP8UXm-kTEHCDQ4LscafKoxBAF31XA-Sgq45rOWYx-rEPOD4yVZvVq-R9Hwloyyrc2-Qo7y6nC6EpA7LtUq2dXSryYn26on-J59eETatBrJCJ9E9I-4kSabHhMVXJkKOg2lICzEd3K62AlxEB__YKTITq6eWhVPgzIVevJZNsBqqeqESUUF6T3a7-2e9ixcM63cVvHU4YOzfvvTlvoMqxaRRtxOEE7nPXXgJ3iqOrz5yxGehx4McgbIc6qtQAehmxpaVGgtKSVkSVPjBwjdvEGSlA4LF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pG988_vDqkJSFgzh23yDgTYGDA-WQ2QDpXJOvDmaDxEDQwOZ_O-w04Bwa8gaDcpYjVukcF5fBn9ccYC7rwcT-LbWh_i_zBcAGHZNWOvvaOwyhnKeHnG8P0QP5wQHRiie3yJDTvKeE4x0HNMztdYqraRif1_Dzbj5raIPzh8z2vuRfsI676-RmH3VorWYSMI0lIP2eOG5p7PqYpVstx96nTafNKP1BbO31hVKtkhbpKJ9VgMqGYBuNtMSSMVbLLjwhQYgWUgAeyiyugboHMdH57fbSSni6D9whvhnyrwYj7EC66ataQDgXr7BESdvWpreFN05gix1_SYbPfCVRNPKpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQnuvEqO9_M6NSgPhNn2pGS1r4V7liV6zVWhmWBSBywZiGyPF_K1MD5Fv7W_0MmQHWhJqTssX3NFC_-rguKeEzdgxZn3DCMqC6_-o6G6aMemtWq2n1AiTyBqzmkq1tyvPoqzrrX0t8onXzWZJUqJspF9afz5NoPFPUgxAFzJ-8xqnGu4u62F5jR5DI-X1OV9XptvoK5kVYd9eOOXKGUsmlt3ejtjd62n0trHOBaspQ0w1fVpkqs1F0kVRfzFKRFJHGKVuUZDfjZsBKvYriOG4N4WlwyKNlM_kfEjFiBlrHQM2wiCP6CZOto3HYJg_ou23esVk5fk8I67IiefIjSBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4pBZ94kA2NkKwKlwNNxkHHuYvMqJasnpHUEhA4wqDTo7rRxPdRxEXh1pBOK8JGEAa4IwYgoSHAR4jD6gGZHNxe3GPsz8Flg8R8GDRAn658CL5gNZlYubV5NiV5-kPQrknfpwc43WC2D6Xn24vl6jsfIFkHmVCkWiEBq6JjdXlCLNRmS2Ly72BQ5cPZ7Nap7IVMGwtyEg9xN89R_WfrDQY5Uz7ImIYZIh4upag6hZXgXTg9g3CjG4vZmf1YqRZkulBON9FYphW0f21WaicS6FaofOs513nrVB0Zw-BLEjGUPdwGaDFTr2mQ29n5DJQqTtcAsIi9KdklCfZeFf9C-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY0SgegUIrXJ7wWYUr3oh3FZajoN0CKbNgjrsdU5sR9dwUmBUPQionOi_Ap0RoOksm3Gc_emf4DDplTPWLmXft66pFbytNuBaWM96VxvtjOJo_gdCDw984E8l8666qLQkTnn8d9KIbha3T9pPoPZ620VoUSB40dn_ZbZp1Fj7pxE9T-rSrqC98CiTjaR87CDR_hfPJAVv-tndvRRpjJorhA9srfRSVUm_SQBbO77RbnP3Ak0D1dH24K3uBByZ8CyaRGhN4AOPwqXfUv_62eWgYG0oW4HvUhvjCd3Q_-jScSa_j7R2EJdqHDKvihMj05GdK_XBKCm4MSQII0API0Mpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVHtMuLQRyeUvBf0p8_wMNPs02uCaYrukIZ2S3-b64rXrzfEFvK0S8Ij0TpYpRkQkj-pJycOnlKIhUObTnMXC137rQPI2EJFCca4qjdNKPdS7hwH6V01FEgPLw9vBhpZbGOgICip9dkRhPBsrFYUCxv1hZQfNqQgkEO-0xQtd6VEdanwUZfUrUY_EV98pCCPIIIniFrEXAiswRpktPbW5BabSLP08Gb4uJP0NI1JkmQhxwq0UwvWhWCHJRYPwdEMtxDQCFIBAdj50bk3Vx9dUmSVB7Q-micoAscyJmqDbPayNe1UAxkhUM98db-cSVo3g1Qud0NHL4EwcQsKc2HWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FT2KKyX5jbpPPsP5kENhpEzY51O0tfYcEFKspWmYkdT7KJ3102jPxtpd2Rv5djVUvJr3jjBV66vMyHXNNHXsd5TMfKNC9ymHvBWrkWo79AQS4m_6ffMSvwi2HTC6nHWOyg0psHeQUM0ZUm49bkF0GCzfnfnUYFFeQlZcomoo5fei-Jw8MLm2fuGXYkW5omuaOZ5VeTYTLPllT27GNrdI7OJM9fzxUldTUDQnqRaemH3h_6oU4u7RJWz7PWgEki_Ih8tc6YaDngwqwMJ9N8s7_usR0Euj5GrqR6ApRk_2lhTfFlZQAtQ069kkIXjTHATxzfqOZFE8oB4ofAha01Rpgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZ7DQDTQ8jIkQku3LuFiZF7kwJVXVqgX2EH8Q2SduMy_ytOtua34SjHgivXvPtb_qpGmFpFycFFxahMnpojIbI3YuKeDEgbqI6Q6RozwtwUySYRxr8kgVbtYtSuqiRiKeZzmL1BooYt8Kz_dHO19ZxbbO-KvQ-6n3BaquKIBqF9Fof7R2WQljWcxdjD6SunonZ-iNHUoXuFaDNkPauNxJfIBCNUqr7TlbeDPNFqJ4GC1raSJrl9GtgkW55ALRXASD5P4PNnPtFo7sFt-Pdtehl3uoT660N_R-WFdZfXPfRcXRYtUSvbRNBB3MMPzeDH9WQM0SzWWzvEBPhJs7L34hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW-7nmpeRx6wwP5p3vXk8EVWDmd2kqBTxTBfXooRtICddMpMh-G7WSC5JyDl03yEiLi3vacFerh2AOMwLgyPnuQWRSgPuXOaDl-wM386iDJeIsODd3AePdjfDxEph2W78G5N0UWdMRyUqx-d_GVJJ72GsHFKLAU2KonAg_B8RoRxSejd5_WdtVqNxmybimaHzisQuSOMVwYzhfuuGWxK4oodG1LTT6K6XyaV9uOvvNXi_IvGtUtyGrb3AvxPXrejZSrWFy2gZvTn1n2dppRMS4XXGZKy7Mg20y5AvlNKfDfEGPX8gsqCfyZUSA2Apz8o1kYl6Rbw2hUq4rKhbZaL_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Whoddz3aDTksKRjFNULYyHQ_W9IOelnUazusfxtUZtrRf9_IEQNkphsm-bKK9dNkt56p6UYFP2HOZDa2twXPUYCaKWJu3tbNycI1E8WVQ877il5DL-IGrYN3uaW3KCzleSAiRT3Wh8vQYh6jTRQwRYsjHAwngcDLVMBWQ0yoyulEHgqP-y8E2CGzohuCTVyIvmzICpcaJPPoN6xXy4mspRwhjBo5QGB9HSNku5AuViygcdSurRs-tHbQIJdVg6JBt2A5FrYNHXyDnJ9SY8m308Ir25uNQiOLhA9d0NGX6L6e4jsJjGD879u8NqFtAUiF3rkQret4laDR8DxbNgAMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqUpOTChbpkKVW198y5yBrBjTKcMmaOtvxTiLX4olUAB1SuQwnEhRz7YM1h5V90rxsO5gnOgj1biTsUmglQohFilWWKW_sYgVYyuiFLQApgWjc1RHlnG3sraXTuUNiOi5zQjC_nA4qoUPmwqc0PKtwl9ZRXB2a0WdSBWDUwVEgZOj83s5ftbLO0AX0s1dpvpyiPub8bHP7KP1f1QNLdolsryY0UDyYS8OherbXSvVEb7rv6vuEIDcDwmAO2BOOLljIgZj2SLu0ZixxKFgV-BzspGRhl3BOEG_jXsozEBlCbHUCzVSdjeMpyegnQm5y1tD6jRk4fpPR54ZeJi7KrYuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdjeQ4upo_bdFeTk6OhAXjrZJfYle3CavKJzSC6ZBn8qRH0wvJDD6SgEj4pxYpIzDmnWlmM8W_SBoK0Dv6sBczXLIzt8nSfHFxN6chsuOqMMfGzst2qeGJYvdRXFbubUR9oQiX9Lc8NBMipW3BDzCfarixE2qfD6rB4r_WuqGDjJkWtaABzuaWbZToeFvdnoweCWhuJo5CLvKXYsM59L4dT7DAslhQvUJlxtHveGux1UwkSGrrG_waPLdnSRhJXWcQNYdjQZ9Zv__AvNxleS82m2iEx-Gp4_nO9pGMClLtH3cCYPRl_XkwSjp3HmkxG59SXj3Kxcj_cAC75eUvW3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbsU_ttp8hwV0xu_c9t9VtMvz71lXc78Q94EQ9TvQ17J74o4h6RQ2zT3J-QFwV_F3u65RAU07oQuoBqEfmeQ-R1EUNAGjyK933_p4508iWKlrvzYtNXnPkUevrx6bozyTXO7zoLpAIininvuh1mSrYEBmpLApS0llKqkRKGwG2kbHN_GQlfgfwLK2scRDC-CPa12wXPqh6S8qe5Stn6WnjcRdlOoALTSVbPTvFwb_n7DUrS0CRa6Eyga7qN5-vjDBPi9v3O05IR6i7635c7QmqW5byGuQPuarFLkl8L0RRd81rWYGJ61E-x15hseRB2S0B_pSKgyoI7b2-L1aHXP5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0nF5R-1J3EtsdHItKsCYNiDsismHEYPuLpwXxmEeOYeJ328wFgrRsoyygwW1KXRvP54K7PL9e5O4WEIn16_OXJhFYqzeGPQ22l8JwwbBlQDUg6Z_F8HtED5jZa376iGv7UcY8FRzAjsUX3ojtOVDKSeuVvraK8K9zwPuQ5d89V0MgDXsuc8h-isvICLHZ1_tgaGuHKeenD-3vtxOBZOhe3P8lGWXVA5bisbM9Q39dQw2i-6xBIfl9yP2VRM0wJCTV4EyCy1yv5Mk05TkBpGHYiYBqkBtvMvdy-VirtxvsuurpeFCO4C7_UOlmM9q-hIOGYr6slR6PuPYsv034HsHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa7R0ukvkhKS6re4AdRFR7LmLp-APE24pQ0YFHEN9-FHWd0dke21HssCs0GQ0CObWri0N_GdVSQbqi8u88KN3OK-IycWvoToNayjsnM3TH1_yZSvaGO6xCRqKq0vTiic1KDOvzjzHk6LKOpCvFfzxKv5jc3L5URGm1QrnvaStyfP_vMzzg5lYLzNpmgHPMY_JiZowSvZojvh1uYHdZYwVs4PW-zte3ARopyAJXX0HZ1Tf_EKG9Fd8nNWHJHMrxvG7Ragak-kJHMOAYmg-JOEina4vc2YIJXHuYLVqfLiCV0osVqjwQVnel7nRwNlF9ImmzWwQViHrFSYc_dT8ii80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=DZXTSIWMHTBlFob5pVOJq_5cncHrZWZ-VtrkgRjTZDHEBVmEWAGQoQe7hoD6hTuLU-WwonJimojiM2S62hpDEM4jS_zJ4d_J84mJrazsqLeK6XYkcHBF0mopkbf-2RYawMzOjr-jW9N7sgR8kAkg8UbGCzlgm4sSKMa-6YnYUH7WQ5-Ng_exTqbm5le8bwRUBXG_E6TJuySHs8Ki-2PVUi0jIhFEmsNh2nXgO5xffuVyJtj1Js1icIdjDXsJOZ8hPI8U21eMznIovD4_Pz8YiaTotaGMakQsCPOOiCk5Q4SpEG-czWpzRkogxjJEXbejY1pxKuBIFv2-gcgrpbQVIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=DZXTSIWMHTBlFob5pVOJq_5cncHrZWZ-VtrkgRjTZDHEBVmEWAGQoQe7hoD6hTuLU-WwonJimojiM2S62hpDEM4jS_zJ4d_J84mJrazsqLeK6XYkcHBF0mopkbf-2RYawMzOjr-jW9N7sgR8kAkg8UbGCzlgm4sSKMa-6YnYUH7WQ5-Ng_exTqbm5le8bwRUBXG_E6TJuySHs8Ki-2PVUi0jIhFEmsNh2nXgO5xffuVyJtj1Js1icIdjDXsJOZ8hPI8U21eMznIovD4_Pz8YiaTotaGMakQsCPOOiCk5Q4SpEG-czWpzRkogxjJEXbejY1pxKuBIFv2-gcgrpbQVIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuWxjldwN2vQDsjZ_FkGEZJ9RBquZm7XqcImVnLFI2HhQ9t30UmI93jHNtmW7VFUKJf8qdmb9TPPOk5H6v_ltF0M6loZxbYYlpq1TGGtOO1Ilo1JESqeRMtIR45HRLku8aCmD5O_SH2PQo-vVesv7nsN-zIISvHfdC6sQ4mdvBrZdO4oylLv6F9QJfozBKltrgbJLbSs31pdGbuz58xWUK9TtL58PiBVCsEqRqu1gJ3uwH_0Vd1EshvTth6t5Zpqk5bHxQVBl75Qo64PfTmw6XDloq3AUk8N-e741GQN4ADvbPxIIkW2qLClXl0AZXVwP3wgKBLZuH90IuTAg3pl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=WzCulOzMAa3M__sFde1yW6jOkKbkcM_FQcQQ9CUmEBBG1JKqBz4TNuDPfp7ecVjFtCr-8Z7li0Rkq9Nu1ofd6OAJaYpqrQV3cSJd5KNRvVDW3byVbl2fMn8soPqVeSbaIKE4C7AZNmuLqe8nUzdeXQGjlqwBVaD62lzcMCuRyafwohN9qBcLFw0qHiHMvokrqcZrFC2fpxxMzL7tKsJqjC0n-yQWb-IhbYFMRVkjotGiN56O0U0J0nc9UqsnKGoarePHqHU09BxQ-oCj5ehzfz1HBYzphemMxJSQ0v953UGpmIEpQiegio2Nuu8Xr3YucTm9VxLSEv-rA03am-wzcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=WzCulOzMAa3M__sFde1yW6jOkKbkcM_FQcQQ9CUmEBBG1JKqBz4TNuDPfp7ecVjFtCr-8Z7li0Rkq9Nu1ofd6OAJaYpqrQV3cSJd5KNRvVDW3byVbl2fMn8soPqVeSbaIKE4C7AZNmuLqe8nUzdeXQGjlqwBVaD62lzcMCuRyafwohN9qBcLFw0qHiHMvokrqcZrFC2fpxxMzL7tKsJqjC0n-yQWb-IhbYFMRVkjotGiN56O0U0J0nc9UqsnKGoarePHqHU09BxQ-oCj5ehzfz1HBYzphemMxJSQ0v953UGpmIEpQiegio2Nuu8Xr3YucTm9VxLSEv-rA03am-wzcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jv0PF3LjKYuaABG23TKJF75LWshkpdssp6Gj--djNFovgT3DH-x9YtxBtehYE3ZfiCU2RB6oJ6tbij20OKMYvq8ikw7eAN6pkYlRk--gEvbPssnjhGvOLidhB42JvADpDzIiByyLMxM8JYIoJoJXFAeu929YnrsVZhMIZKuKqa-iFDK1duEE9B5-oANlWhh6i0DgwYaTfUwtHlvCs8g5MwSWO166iY36uAEphHrQirJsmQiGDWpExeSqgRqjLBA6kzzy7K47mJvNbZ-jE6aCifAsiHWV8zL0YpNH_TDPW5EJkJ7m2xrfMA_jj8eIaU1yo0m5Q9xAj3in8naz-XRakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWs8BsnnudvYzLrmxUIl4Xcue3N99LStJJUzzF2noOraca0TzKjCXFVK57dRMex5YVeZ9Eb-IIcVEXLtieCQzM5IAyk89UnT4yva68s1OuoOTlDQULavOyw-uFcVEWEym9uePEqF6VrP4yib9IBD4dESKP49AdEMjD4VwsMh6_DDIAsM_V6xkzBM77eNIM09id1MCetdmUVtP2aGXdz6lFrNaZxNDxOPIQDOYeAD2weiHWw_F1nxSQzqWyIPmpTmZ_SBN5XGxFM-mqHB9FlMxFbTrdt24ChiQRQtJqq3Fr4nCoYCvIJiUdC454wy1PSmrZ3lq5U1zhIaEUm4tFpg0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=kSRRaVfoLsmMf9zQ-3_HtORzTljRS_rL4E-IcOWAYh8Ei1SrKxmV11Yj0VzANcNBoMWJr17EeJfwbrGdC0AYcwK5diuFwtI_1WbxWUzpaXbso9bYYDLOimbi6V_Ph-9e8SiV1ws5VgaL0FSnUY55GeR2z9_r18NmWDRaKHk0XWWaASjGxxgyRHDo6Z8RVKOLXRAsH-zAZB-TcDJL20-Lq_FZ264DhSTM2CC2-2rQeGNhnaJsO7Px69jnvNwg4V5YHsYnByDnlaWObiFoGczgGagchxekTi4YJpe8D0Jdj-8w-XJuM7amv3HAXWAacirs08OJvstjc61yi5PcJ-Z0Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=kSRRaVfoLsmMf9zQ-3_HtORzTljRS_rL4E-IcOWAYh8Ei1SrKxmV11Yj0VzANcNBoMWJr17EeJfwbrGdC0AYcwK5diuFwtI_1WbxWUzpaXbso9bYYDLOimbi6V_Ph-9e8SiV1ws5VgaL0FSnUY55GeR2z9_r18NmWDRaKHk0XWWaASjGxxgyRHDo6Z8RVKOLXRAsH-zAZB-TcDJL20-Lq_FZ264DhSTM2CC2-2rQeGNhnaJsO7Px69jnvNwg4V5YHsYnByDnlaWObiFoGczgGagchxekTi4YJpe8D0Jdj-8w-XJuM7amv3HAXWAacirs08OJvstjc61yi5PcJ-Z0Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngkEJTWaRPOjnPTQqpcAuUlgb0UuBYC6zN_4TQ5vJZL3Wk2bxjxMrsfv6k5tWqT84sJ_ztRsVSMLMWLZmz2-0fECiVumOFOPRihIniqUiaZMUtQW02HBrkcdr_ZkMkgalMGfaMhXYus9iC7qkcD8Sa3VqP2dpHn7nWESqJPt568fSk88KIr4anxBfC6JeCC9wfYMsZE9aAflcpaaIh3kGBQ47LsHD29IMoM0u-FzZAhsBQwHzFoyqgSle_5u2ql9sr4sWlWC5uGNzrIAPISKkOTUO9XF0ZPawMZUVsKgXmSic4MxXX4MOZL8ZbUUNG5yJng-SqFj834zjCEcJYB_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3-cwl0e6ljJt6ZZ9i6muM5CgEvZ2mqMBsP9iIFwXl4o9G_dtrGCLCrWz6CrjvtVEKWo_xi1D5IrRikg0bV2745Hz90WBtUB8cwWMwDx5wOb3knwzAVFgywBc0DUirrcczEOZ0NWV2Di27oexxRf64LLr2iMIq0L9ujtcij_usA0o9lTOrKbwdB6Jx7pSct6W5fvXlVlMr_Pi-X4pELlWblVWW9aEZ-v5Fqg3fGpJV5c6xKHGC8OYy3tQ4d9SSKwHA_futr9k0eULd-x6HEfpbS_aYyJMOUd9WH1t09NjbUcCP3sLlUGOc86-k4fWSxpGDnV17RNJLrKnqbeYV6a2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKGEHFGsFfoVdymqKNaJCG-dIBPPQQ4Hh_c8Umg0_WEZMXNW8PRGVHwtr_YLUkmgjgkcvRF0-_AB7fsjnQuErk2U_XfLYhIpmoYLvNRmh_2JjdqGQ_b79ZNbyKbqguAcCn-Y694mBoSYA9TADt2EO5rCJSMVkDUF-69I4PffBKC1AhW8Kx53ufkZBrfGF2zIGK4a4LAVPhjHQo-e0nGMXUyyu-u5DynEvnmkTdwJtObP8nSSpczvbfZDlTMlyDLFyNZj547bWYUee_39XhLq3XZMtvONtfOunyN51g0L3d1LapnBJ7l9R6aIQQhAyv4rD2auoxLXNklNg8QpJ-W9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=iAxOxBCWExqmK-a-vsHM0ZnsutQXu_eOwUOZWijEQOXaNC-WdenlIDvbiPSq9F3lSyKA5UNXVd2p0JkDmrqpBWmVVv6h1gjrQjaKlnoVgpDJtIOM31ad-2rjR4xvxLdavlWiz39sJrm2rVQuuFgrithvvQMSqOmm3g6d2LLCG7M3Um88g2NM8J-qWyBNvtXxHZe6fMtMmReN22Sy-BhmaMuIdtA3F814Oddm_r6SXc1BawjRRSuY9bRy8jvjQKHE3TKMvHvyZSX2McrBRCAeS-7d8FHB_RRW2HV1NP149Cam_heGKSWUpRr3empWFy6O0cZ9uViCyIj-YUSkaM2TCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=iAxOxBCWExqmK-a-vsHM0ZnsutQXu_eOwUOZWijEQOXaNC-WdenlIDvbiPSq9F3lSyKA5UNXVd2p0JkDmrqpBWmVVv6h1gjrQjaKlnoVgpDJtIOM31ad-2rjR4xvxLdavlWiz39sJrm2rVQuuFgrithvvQMSqOmm3g6d2LLCG7M3Um88g2NM8J-qWyBNvtXxHZe6fMtMmReN22Sy-BhmaMuIdtA3F814Oddm_r6SXc1BawjRRSuY9bRy8jvjQKHE3TKMvHvyZSX2McrBRCAeS-7d8FHB_RRW2HV1NP149Cam_heGKSWUpRr3empWFy6O0cZ9uViCyIj-YUSkaM2TCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=QWKa-EvFsUWynlfGeIDmHiiqM4R-KHLmdltEP48EmVpwH9s74HB6aHco2ldf2VFK81RZh1T3FmJCK2WEMO7Rzt6hpW5d0QxF61rRBd59rRz3MaCG2Zbbzx91213zNssVPNTIkyoS-FXkzF1cUsdMNfjVngjYRLAV3yQG2E-lVlSJGtvAadTPe2ceOj_xe1OHy04E-4eXocUUpLQQie1PU9Xu72VPKS4En5Fw14UsFk5vl1IFF8Ps16ryvEe6DboQ4cBktbyLZmyMwA-vl-nVYQK0TcMjU6NIIy0o0tAVmUBRmA3kpRtTSE5pvHn7RL0447_jVf44BMc96oyRDfRk9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=QWKa-EvFsUWynlfGeIDmHiiqM4R-KHLmdltEP48EmVpwH9s74HB6aHco2ldf2VFK81RZh1T3FmJCK2WEMO7Rzt6hpW5d0QxF61rRBd59rRz3MaCG2Zbbzx91213zNssVPNTIkyoS-FXkzF1cUsdMNfjVngjYRLAV3yQG2E-lVlSJGtvAadTPe2ceOj_xe1OHy04E-4eXocUUpLQQie1PU9Xu72VPKS4En5Fw14UsFk5vl1IFF8Ps16ryvEe6DboQ4cBktbyLZmyMwA-vl-nVYQK0TcMjU6NIIy0o0tAVmUBRmA3kpRtTSE5pvHn7RL0447_jVf44BMc96oyRDfRk9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKnTRlhy_MRniwfWolugw-KzNHHlOyclWGU203hHMz9yoXufTGlETGm1ot_ROvZezE9zSHJBlB281qf346c41nq_2z2kMCIH3rOjQlzMz8EaK-k7PwAa5AzGeMoZLpcSeJBx5mYJqWV4v8Zw0WceEIhsOPB4Dz5RReUgajPFTAHC-OQs4hbQ0L6OD-b0AON01VGWlCfv_5Tg3H6b5kvNi4pX4VckV0HPD0JkdIA9K6vbBgD3yXe-wS_dSh2QI6xxg6dQyxn8MnKuQXmiplhKBSprqExGwdQdeL8DWZEcCYo2i3a4aIuNSGhytRVRNzzOLukj2AGQETFpxCn-NcGWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n72DEC24smR5L5KPgZ9_8NtKGhxMunZZJNwoJIAgV0jwT3VyxHqbbeYxm9AymIBnOSgaTdZgj-dobGv_cDQDCHsgAW7TXXCo71sgdFYLCVf2fINp9Py9V95A7Oyfij0nML1gabHC735eC70KftgfedykyFMn6ota-d2O47Umiv_djGR3SAwpuAlcsCRUzXQzPBcNvWckVjbBDtSH7_je6i6-PrJDyxg3BBKV0WT4RD4c--ApzzOekoEAGkUPh_x-_3ExyFuR7JC6Xgw9dbbz8qGb2TPKFl70Tyi9Re0YhLPTI5xYHAunD72nmvfjD7OLTS_B0PZZFpHC54cm7aSgyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5sx2mEwmjMdEHYB0EgdgQFWmae03U0vyPptJE0CktwW-xFBnm26-aLIYYFZmkqawlFDkcAI_zY3hshecK3Ks8gfT3VTB6438shUXgkFK2tsBKhCJk7Zd0TTYQ5oHJ0FfEYd8hveb0vRY8BBlXnBxPMDT0uonXA0Hk0C-R91P5tvcHGyDIuBHyP9TK7AVFQJjigxFs6VReCz64iQdIODNUegw2bQhkLjMOswHUHlRBogeNXvyTq3EQHF_sihDbrW3Np71m11puKX2em4oXNZd6UknH97F3AmsyvcYS7yayg_4oGpZPbuTWznmQGCegsVA-RRAVL89YAUmPTFvpgcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkNcasvXf8Qn-EhMW-ISjUZKppQHP7ES5srUwXB2iFOGatqmx1rgNLcWwbgA6-oSQy8RIfFM_nHrHeAixSYaH50M4hPLDXCMLoR-NCI1qwit_wm3-nTQ5VivN2j1NwaPCZPb-YKdYqPRmQknvvp_fXFyAs1FFWhryRQlddQgFT7YIWzz2lZV4ODNxEG6uVCCQuOV0ePLgfJWbh81K545f45nFCgnrRQq19izORhtCh7VcTmCu6LO3KYfohquof3afvPNM1OmCvh7TeUOsgNVubn9_vDZLW8OXr1P7sk39k1lHy26hQ4WB4Jo3TsN5AR2r93xn-6VC87_JTP2TF4bvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3OJ8XgxBvC9TRDbg2veZdjBJC6N3Yt8Em0mzhyOl5INqHQtFvTpHhfYhc6Y9MCQJJ3ROmb_GzKUGF8jQIg70DlQdXvM-YBJzc_af5d3rV0OlL-tk9RU3N1TFMz2g19PIKgE6RzauDO49Pl9s3bRl7TzdNDpgrjNEYxlMzAPAJQrKIBOOlL2QJaKcScGvCeDicMGfnUsWVanOv3GJw4zxIynAxJWYWM_4cmzYjqrg9WoA21BXPbvbsf9ayabIjyNdot_96Ghgtz8yok6Kvr8LFyy8teoo5--zCGu9tzUTjJjbHkprXfxJqz5jSxS4k-bH3iLNBYrmhyg0P2lWBAKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOSSvfP5drQ4eF67kZAcdTneyW9QkGmxH-UxPcbnVoFxJeWFptItrVGRcIMKHNHXC1ejWyV-VeH5sZOWTY99120vSkpfusC5b_XZR4bimdIB6YfgABuPhnFigpaojRRGQ7HRzW78ZeMhZACVFWp1srp2pHdpJNQroznGEf8F5qoLo5LmTytp93-j7gDg0FxSZUaNtY9TNsvUdpfhHpiaHFkvRkD-raWOUFKCXmzGAC7q_upOjw1pgAmGgrbmNL-aXr5eLMwpzx8paH_tNaQT0ZaX6BIsXA_R_s--eYSOFS_wkOPnT5BrIfaNaW1TOLQJlB8Uhhmd-4e98yNCp2PqRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RitQuVj7GQyECAx8a0crmHYofj0RPaTnAnbIUkwZSISX7Exw5H3RoUKrxmYtBdyu4rB3BTpziu0g_i-W28gUny1DJirbzf20tbpETcxZDzcwSS40MMiWMXcaexi68DmUmda4V1VEYIBxsKrntPiRVWc8XsQIxOEjAUARj8-wI634gCnd9PxSIfcfaUYadMQuqjWEtGbQKYBps_3kUpw6l-ydrxNlxKdZNhF9n84ZqwnWxAwnjg7z00D5qR9-sZKCpCbfeIbqvxkHrqnJKbyYzqDZT1FE3Xz4CEceOR5xZQbeLrgVa1liooRbp8KY6q3ecZeHzjTnKSJk9-0CgX8Tkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=KreG3oiOgV0ZqsMITjP3HFuQYLt2ZaytNy-qsIdNXpL81oJXqgXwW9rKcyz54gSuic46gOe5vRW2e78ASzEAICzq0XN8Puk6yBwKQ3GlUWbPaa9OQNyarQYenvrLb4EcgUlc0u1QSm-N38pOgsg-3uH0QOJlp9d_f1RvWl3GIDaY3F1doaqJ3Eozxne8ld6M_4wn6mPcBGm_VgVw9VbrpLpZLGaManu-tVswELvKk90QeCPj38rSeRdnu6pkL-TK8HfyOQLT1HJKYXNJJJcz27d0SkUEl2e6fXW5dNgI5yvhGao2ZaM_90l67QrSQs1kSXv6FJduIi2KhdIlGjJ6Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=KreG3oiOgV0ZqsMITjP3HFuQYLt2ZaytNy-qsIdNXpL81oJXqgXwW9rKcyz54gSuic46gOe5vRW2e78ASzEAICzq0XN8Puk6yBwKQ3GlUWbPaa9OQNyarQYenvrLb4EcgUlc0u1QSm-N38pOgsg-3uH0QOJlp9d_f1RvWl3GIDaY3F1doaqJ3Eozxne8ld6M_4wn6mPcBGm_VgVw9VbrpLpZLGaManu-tVswELvKk90QeCPj38rSeRdnu6pkL-TK8HfyOQLT1HJKYXNJJJcz27d0SkUEl2e6fXW5dNgI5yvhGao2ZaM_90l67QrSQs1kSXv6FJduIi2KhdIlGjJ6Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=Lle8E4Z7cpYfaNPqslJ7eYVi7SE3qwBUnRCpvOY4r5r2IzFovzDHcYM11DxHS74ac-9akQaa8vTi7aC0EBDTb-1793QVRd-a8i4YI3zAsM1TTi_lerY-rubs4k_tyxLRl2Inm1VzT0cAa5eBNPE7WoByRUBS6AC1_NkzHuPc8Ky2sCokPxD16KYphHTtQ1E-U_XRAa7TI33SvT1Vp0n77IyaiVvf-1buB7AlGcCSGGbvWPTEJH7JhdD9WEfTiS8jGuYT2xFBFy8XZPpvtYMXgDCa1UVMRofO1mGbf_uAMcTg1utxVDmAuv7yE-QhOVdWfVUjcJoLlONDWWe6nKQdoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=Lle8E4Z7cpYfaNPqslJ7eYVi7SE3qwBUnRCpvOY4r5r2IzFovzDHcYM11DxHS74ac-9akQaa8vTi7aC0EBDTb-1793QVRd-a8i4YI3zAsM1TTi_lerY-rubs4k_tyxLRl2Inm1VzT0cAa5eBNPE7WoByRUBS6AC1_NkzHuPc8Ky2sCokPxD16KYphHTtQ1E-U_XRAa7TI33SvT1Vp0n77IyaiVvf-1buB7AlGcCSGGbvWPTEJH7JhdD9WEfTiS8jGuYT2xFBFy8XZPpvtYMXgDCa1UVMRofO1mGbf_uAMcTg1utxVDmAuv7yE-QhOVdWfVUjcJoLlONDWWe6nKQdoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=gwEHCZKj69Vj-bLaWFza4ZxxtXghX_ApinsDhfJemwSLxwwmg6qYuLYoV_3lTaA8rnabeDZnPQcs1Y9b-BNX6Jo7yzB_h9EK4hXrqSkle3zy5WATZ1D8Cgcv-zxQNa8f8bQYFmrhVsPTGF11II5pb2Sr3qKLhFFi1t5XQayfZRflxckMPtCEu1rLpXpW1k4KLX5Ho0vhsBefNJVW-5KvGNutBZVOxrwY2VL3-F1868NzG-oOwafCUNjatYCNqz5fZc87k9WMkYxwkBQvlnAdpvIWNTebos4PlUwcHISDE9EKqfM6vDUvY2OxWjyiQ-TKgK3hWlKG1KJHoThbXCkNhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=gwEHCZKj69Vj-bLaWFza4ZxxtXghX_ApinsDhfJemwSLxwwmg6qYuLYoV_3lTaA8rnabeDZnPQcs1Y9b-BNX6Jo7yzB_h9EK4hXrqSkle3zy5WATZ1D8Cgcv-zxQNa8f8bQYFmrhVsPTGF11II5pb2Sr3qKLhFFi1t5XQayfZRflxckMPtCEu1rLpXpW1k4KLX5Ho0vhsBefNJVW-5KvGNutBZVOxrwY2VL3-F1868NzG-oOwafCUNjatYCNqz5fZc87k9WMkYxwkBQvlnAdpvIWNTebos4PlUwcHISDE9EKqfM6vDUvY2OxWjyiQ-TKgK3hWlKG1KJHoThbXCkNhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=T943xBd7hegLZ7-htJjVMc4ysUcxJT8Gzzc7Ct6anr2BabcxWOx915LuDF7hu7wqRbiQ5pIZufgiqHIuf0wB-QIlyu6UoOJ3T06e3ncZzN6-zmT7g-MJ4rI7B_Ozh0oJ0vZjUkU5eVyImQ_bAh6liWJspxCitqilXjSFVsJYxOe9-z6fVdvhjuyup4Enj4PLwh-RLiEiBojZlzLmVct9GwwvOrU-exrBNUoMDz4fxgZ_cYQ54sweVctfiqirpGINY-j6O5zNvLwLBAeV84nOwGUwZFPCJPDUgEbr4OiEuj5_E-otGrAGFl5TLYwp66PCXcrJfcsmNOE_JmoXrYQrxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=T943xBd7hegLZ7-htJjVMc4ysUcxJT8Gzzc7Ct6anr2BabcxWOx915LuDF7hu7wqRbiQ5pIZufgiqHIuf0wB-QIlyu6UoOJ3T06e3ncZzN6-zmT7g-MJ4rI7B_Ozh0oJ0vZjUkU5eVyImQ_bAh6liWJspxCitqilXjSFVsJYxOe9-z6fVdvhjuyup4Enj4PLwh-RLiEiBojZlzLmVct9GwwvOrU-exrBNUoMDz4fxgZ_cYQ54sweVctfiqirpGINY-j6O5zNvLwLBAeV84nOwGUwZFPCJPDUgEbr4OiEuj5_E-otGrAGFl5TLYwp66PCXcrJfcsmNOE_JmoXrYQrxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=fAzxT9pI4oJmmM3jeHMbTum1PPM8vpWmp-4KigPjdNeTY42goV8nnlubwucIWl3b0idrZjwoyjChErGbe_T4JW2SNokhxLr8UgO0ZOUxlP6JcafpwXgyV3AtNt63vMZ8LAySUXfZ8JQxHwVzr4XqUGtyaFc1bgFd9v6AQwfwJQ175M2NaOZR9Ir2iGoHB1ayU97C-PojE8Nln_I4mcP1MILWcjjAV1IbCZskD4W5sfY0gDY46VeLmOyJDRvjEgVW1-UlIXUiiu4AtZCpw9WcXBNwGfIvGcNi2G82LwADTPy-kwIFKEMpPFTW9rThM2_1ZpiMnkWWEb9WuCNORN7vDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=fAzxT9pI4oJmmM3jeHMbTum1PPM8vpWmp-4KigPjdNeTY42goV8nnlubwucIWl3b0idrZjwoyjChErGbe_T4JW2SNokhxLr8UgO0ZOUxlP6JcafpwXgyV3AtNt63vMZ8LAySUXfZ8JQxHwVzr4XqUGtyaFc1bgFd9v6AQwfwJQ175M2NaOZR9Ir2iGoHB1ayU97C-PojE8Nln_I4mcP1MILWcjjAV1IbCZskD4W5sfY0gDY46VeLmOyJDRvjEgVW1-UlIXUiiu4AtZCpw9WcXBNwGfIvGcNi2G82LwADTPy-kwIFKEMpPFTW9rThM2_1ZpiMnkWWEb9WuCNORN7vDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=WSutM6FVWw_P6J3JmBrUtlyoR0uGagPv6R-LKKM7ibuN473k99VGiKbh6ul0DsKQZrQlDPQme7ZlXB9BmTRw6Afdq0zj9NQcOzMb71_UO1CFCOnKBMiS_hwPhebAo0dNexABQEGeNvOvG3kcuc8yPAhs23UxFVmfdtu4-770P__0blgP0yiRc0Tt1sUs_Ubs_-XKeVPSuCmmQ8m-D2UNorswwi7XUutCaj5fOtcKWCbAOtkHrx2aoI51EptNbIaPRPCazSaj5BQIu18uvchjyVdkCK-lY6xQsZ6prapcAHvlwD59TVHZazKP-HDWjBgO2chxdyHNBupiCRru-bgjVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=WSutM6FVWw_P6J3JmBrUtlyoR0uGagPv6R-LKKM7ibuN473k99VGiKbh6ul0DsKQZrQlDPQme7ZlXB9BmTRw6Afdq0zj9NQcOzMb71_UO1CFCOnKBMiS_hwPhebAo0dNexABQEGeNvOvG3kcuc8yPAhs23UxFVmfdtu4-770P__0blgP0yiRc0Tt1sUs_Ubs_-XKeVPSuCmmQ8m-D2UNorswwi7XUutCaj5fOtcKWCbAOtkHrx2aoI51EptNbIaPRPCazSaj5BQIu18uvchjyVdkCK-lY6xQsZ6prapcAHvlwD59TVHZazKP-HDWjBgO2chxdyHNBupiCRru-bgjVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=UwR6rHn6Coud2uh4UxaQ-Xs4XQVlByf-9e1nace2ljd3T5BBN5L7Y2DgDeq-UOz356XDxWgG2WxzKIwZo3LeGW3nz3JEY7T3l3Cmj_OhihVBRWYqe6fHpSlbx1AUUZraR7kz3Wd6jJIFbr45_BrT9zF-T07XEI1Jk2oSgu_-PgcUX-FVcqTGbeaWYGnpA5v29XpKFhXB3YOIFUlDNj0mTWk7umJ4Q_IrkKF5Tfr49L3bE1npK7LwrQrEm8WSkqXDn8o5KqrPSJ2N8B35q9AVXGnR1yMlplO_WO6XOAS-yuhO7VzqP2waKgl_u-Vp8V-WvqqM4AWz0iMBtzpfRgOAFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=UwR6rHn6Coud2uh4UxaQ-Xs4XQVlByf-9e1nace2ljd3T5BBN5L7Y2DgDeq-UOz356XDxWgG2WxzKIwZo3LeGW3nz3JEY7T3l3Cmj_OhihVBRWYqe6fHpSlbx1AUUZraR7kz3Wd6jJIFbr45_BrT9zF-T07XEI1Jk2oSgu_-PgcUX-FVcqTGbeaWYGnpA5v29XpKFhXB3YOIFUlDNj0mTWk7umJ4Q_IrkKF5Tfr49L3bE1npK7LwrQrEm8WSkqXDn8o5KqrPSJ2N8B35q9AVXGnR1yMlplO_WO6XOAS-yuhO7VzqP2waKgl_u-Vp8V-WvqqM4AWz0iMBtzpfRgOAFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvVLSGLvKdaEn3wsBvQj-U2Qw8g4a417ItVRWs0fPKxEjmN70y_vp1WfAQPaS8-Go4DvA8ODd5EDWVj15rBNd1FuF9-lxq4JmbQwYrz9E6MYgzeAF0cQ9U7Xy-JTVsv8VbM6g5bOKIwUcLPSzNZ3EDfm_gpDx5x1t0FdJNLuh_8XvQ7SvB-1DYR6OOyfG0CYx7xidyno0wtn1F-KOLiUoSPhQn8nzqWI0K5Ha18nPCHthXjLeli0vm-1ev2ZCIYEg8q-ad27jEv4die0uLuifJC49JYNDDhVwvz85nmqM7k2ymF7lV95egnP0H5Mx7TG_-qVZ0F0bwRp2Fa9Go8FAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=id32hgkvqQXyOYMNduHDw_IBFwa6n4KgbgyTSYcFFL4_p73rBfhcYTaRGFzJTSatyph8Cn3UJxZCOCFwyzxTkJLvozgV5wel1zqb-9-RJwpzOsWoZ7eESLxlzhMSoVMXXxKls0uoMAVDUyFLhAlKSgwD7crm60_L_3xzH8yqtfpaKtIADMgQQoHPNQ83xrVOfPXfy76Qzqfb0L8bQwmFrKA8gp8YClUJ_ZIXlaSpFKRe4Jt58_xbGxmEuvQ7SJg4MSnP_lKUfQ30qHGVmuySDjnVjjOHEfk7-xmCTdydnOj5bqsTqDfJY2p9jPH7WqE5cHco6u-IZ93OdEtyzcHvtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=id32hgkvqQXyOYMNduHDw_IBFwa6n4KgbgyTSYcFFL4_p73rBfhcYTaRGFzJTSatyph8Cn3UJxZCOCFwyzxTkJLvozgV5wel1zqb-9-RJwpzOsWoZ7eESLxlzhMSoVMXXxKls0uoMAVDUyFLhAlKSgwD7crm60_L_3xzH8yqtfpaKtIADMgQQoHPNQ83xrVOfPXfy76Qzqfb0L8bQwmFrKA8gp8YClUJ_ZIXlaSpFKRe4Jt58_xbGxmEuvQ7SJg4MSnP_lKUfQ30qHGVmuySDjnVjjOHEfk7-xmCTdydnOj5bqsTqDfJY2p9jPH7WqE5cHco6u-IZ93OdEtyzcHvtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVdf18VHZo257uk8CgfWqsfiB54YaAu0tlkczCk6Cx2NhIHw4sM9qxHP09pvhgnUF6ShZ5s5rMULL-eUXP6lXcATAjWrDKa2AyidLgqDnL_gYZZu2P67ORPAsHejAs5VW0OkNX6aYLt82J2JERExBvh8HQne7gc8VczPTtBX-j2CP_e5XGpSkCI5e-c1ZN5M554XjDJL1x9UvSYN93waNeD4-Jdnny-oXPLrisCIou41GbRgZXYio2GreBFbNddf5Ow7jR3GG6mcEcJnNPFm0ODG-5M0IoyM1PsprFOPK8DbFeNIMbnHHmQdr7OV1_0WDeR2hWsd-D7jNKTFdvIkJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NofLIuA26lsdEU1j7_3N-4CTmKbwskHbLQZ0m8a8umgFex0msjLXdp2emPykaQOa8nHhY-zg9AyOZNgDrSlT3fIQuPHtZUb9baVTA2wB5ffpQheP7Y0heWHXwDHdmY4TxHT3N_Y6wZimjiKGtvw9l6e47E0Ly_HJC-CxeAI2mRRoYZ4leXRhroieGQatVZP02PWF5v1ASkBW2QBYEtCSV4uzoOO9qp3Fhiz7wlCPqby3tnvHgN57ChaliZbhPUAzHsDxsI4JqpAYoDy2gCKr9kI5E7INOl3s-a00P7zMuC0GX74HnsB8uRnm-yPmXzPBGFrZGjRcygd7aliMC4Jvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP8xXI5oO4U9Api2m4tLguuYICCuke1YW-txNG8CfOHgt2JugyJJIi4-ZiyRzYYwQYZ8cNiA_AxHFwouHdzdpXF9R1ENbwYBdRL8014eaknTfxIiK2q_GmFROy1m0qw3RM2OUueKozBlOduRN5pQvNYykGGnCDXCbrQCdp4DO2sc2M1BdLw5t_4Zy2y08wReFwIrt9djC1XDAk93Sy-rVoAGnYjHYN8LfltkrInJ7in130XmOTeYQi7xaYsWA3MpsestR4xj31JJ_OZkt4r7fQwSKKWCJiwIRuWEHO2OD6yJ0xnEFMu7JgibKqNWI59BoA4Z7O7rNkUZ0ifwbITU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vg4STIqGdh3RUfLzFnOlLNHPKYsLhYTFz6Njsjwq1casLRa9klpFU9O84-rxlVHnWlEC164ZqimOCG1g40vdqVJz9odEZIbHslbUV4UY4I96ik70kH28r4uMEluZt9hyljEEYUTz6FON_Y5wSn-kitFoiYSSUlMP0feiFyKUTH0f34MfvEDT4iWOzuZpfai_OmYxgsQGyDmBx7r40YYp-ru_yx_nPWrxeWosfXpQI6pgIgGEdzLDiuQwcNPzNlW_bNGvV4MF1br7jcPzaTrlRjYGcuCvWVCoAr-f-ODYVdMWFQPSoVXJbpC3ZxewcOFBSAvcY0XKdKL7Ixdz9QWljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=W1kJlBYJD6I1SYhvlkAh33qvCUekeBjkf6ZGIJLbRfkN8uA758JQYqXwtkXjRM3YBpS2kzEGTK-rZrC-RN8v9giVIngYR17QVbrrlN4PmaIF03iUh2vPgsAUv81KH4DEHHMMt1GBw68S2bBebYi0WtA9jd0RoYC3SKGJX6hARWeWG7kxkzi-Mpl3M8CP9ro9v1upiUS_cLpOnsVE-8wonr5kbNruvXhEJ2Uupi4AZTQiyv9jD-5cw9H1gFaVgkZOXV8irFwd9EsZ4ZeJzIO_kDmhEO5CaT_YZDoreAqjLDouKYlDwcGkYNjMrFV5GIvux1sfMBLdsnWGMfpwoi1Jiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=W1kJlBYJD6I1SYhvlkAh33qvCUekeBjkf6ZGIJLbRfkN8uA758JQYqXwtkXjRM3YBpS2kzEGTK-rZrC-RN8v9giVIngYR17QVbrrlN4PmaIF03iUh2vPgsAUv81KH4DEHHMMt1GBw68S2bBebYi0WtA9jd0RoYC3SKGJX6hARWeWG7kxkzi-Mpl3M8CP9ro9v1upiUS_cLpOnsVE-8wonr5kbNruvXhEJ2Uupi4AZTQiyv9jD-5cw9H1gFaVgkZOXV8irFwd9EsZ4ZeJzIO_kDmhEO5CaT_YZDoreAqjLDouKYlDwcGkYNjMrFV5GIvux1sfMBLdsnWGMfpwoi1Jiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBQfhQhCDU7g9U8lTRinAn2MR1BrKEWMgR5dib7-RS4LdW0_iTg6cvl8Uu0cjVqYn2Lg_LP8hac6e4-t7eKHG79fqQUe3Dor1b4YbPFhnCS4ovzfJSiQA1KyqMyUYWRqmIGDi9FPkvpAASaIO5S0j_nfYPu4-B62WtOq-adzCB4uIbaj74BtUBC7dOLLLGw2r2ZzncnzJmg-gdeTFxt21TF727oTKf1nAqYZ0NNzX9STfH1M8v3JJh8ktbAR8gaWbCD-lbHdoqWkclodEhEyvf96I-2nqLcvEChud8RgQDSPxlRwHakmesFmWinFZFo8MGbKkTGHxsVXifPTuhs1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=WHG91zK3K4QlJ7xtrkMr3NGltrMD2wv3iI6UonExFwQZGcVZtngYw3k7p1I1WNbvURIdZxvfo0RL8mtcwqd3iFXxxcnBdrwFYLYp4W3WezQ4r7Ud-JeovHRkHHjHk4MV1O-C3LzPjNO4fSZjeyK3SLIVrGJrPqi_DQujoI_PjHkCnfgUn5lRqe-rCzEj6DGeRBotgZFLSqYoqVB_O0isr4RRyHXexPbAqSZubqQa7Iyq8hrocSHSXlnQhF-FqzvzXgMI01hj27r0nsGN8K-IkWok9q_3Ncn39aYaJJHNq2Giu_muf7wWGby05AO2n3GVFI_WKX8JBQ1UKcDuTkoL8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=WHG91zK3K4QlJ7xtrkMr3NGltrMD2wv3iI6UonExFwQZGcVZtngYw3k7p1I1WNbvURIdZxvfo0RL8mtcwqd3iFXxxcnBdrwFYLYp4W3WezQ4r7Ud-JeovHRkHHjHk4MV1O-C3LzPjNO4fSZjeyK3SLIVrGJrPqi_DQujoI_PjHkCnfgUn5lRqe-rCzEj6DGeRBotgZFLSqYoqVB_O0isr4RRyHXexPbAqSZubqQa7Iyq8hrocSHSXlnQhF-FqzvzXgMI01hj27r0nsGN8K-IkWok9q_3Ncn39aYaJJHNq2Giu_muf7wWGby05AO2n3GVFI_WKX8JBQ1UKcDuTkoL8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=KeJUV96FtrzLRCbwqtcy26ieWqzPivtahU6he48ME_hivhRlLbjrYAbN5djhgIfN6BBhFzonXsx9LsdgehA-2zuVOorMx9pA8duNOV_gdIOr6tBWly8CafidtYnsg4xgEpUlHkKwibSkUehMY4wh1ZLpRFh-E0VKiETcL7sQEIRlF4lcvKOFkixQbwIMpuhsORK4_0zw2O16nbBu-wkwwrPY_K1L5AeEb1NYJMFcNHuU-gvx5l9k_3DPFK-Rj5bDJ0G9qb_OxmZL4ayjXuHEfI27COd8tENkb6E1k9j9lEl0Cvog_VjaeGEApHeZT1TevVf3fisJFriS3ofqQpWprg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=KeJUV96FtrzLRCbwqtcy26ieWqzPivtahU6he48ME_hivhRlLbjrYAbN5djhgIfN6BBhFzonXsx9LsdgehA-2zuVOorMx9pA8duNOV_gdIOr6tBWly8CafidtYnsg4xgEpUlHkKwibSkUehMY4wh1ZLpRFh-E0VKiETcL7sQEIRlF4lcvKOFkixQbwIMpuhsORK4_0zw2O16nbBu-wkwwrPY_K1L5AeEb1NYJMFcNHuU-gvx5l9k_3DPFK-Rj5bDJ0G9qb_OxmZL4ayjXuHEfI27COd8tENkb6E1k9j9lEl0Cvog_VjaeGEApHeZT1TevVf3fisJFriS3ofqQpWprg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jid9BYVPsfg-yD51qHSKGdsB0SfzJbGUzFaxkvii7D-qXYdLkLYm6zHn1r4PN9gHmEJRYY1YD8rk-OIx52jufutSwOJRvmVjYZ6Xev-FjJhSvB9UAZPy1Nolv9LL5bFNcaRHRhw__PpWSrYzhKexlgBdkpP63c2CRELA74O8InV_UD4WR2YQ7PLbLoH-3MA09s0boq73D-RpeuMTQdFGOMZxhl3Y77_XKE5Mj4j1TGogE0FSDwUMmb6kMKTsaKUR1YPMDR3m9xFyHi9DtpxBnSnP-NlIiv_oHRZaTAbgNF3gAy59__ejRCrPX8nlrSbDBlTZF-gZB_ku1vFXsRl8mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9LOm4EQrkcEZZNnXlRUZNX3MJdjT5j1ck7JPvLaAvSALDn1jmSCvazjElIpEIe68ILyjYx06XWSdW7o-fSeSPrQ6fsq4U9AXelRjqTxjxEFFnuTlvSsc2LR6curXCXn5zhgSL1BwgMEq47GhpIUOHpZHAX0Df4ZKzMsQFBrkPl_V1BftpQW5nI6OrTA9AP0kxaI_n2VCBGSwZyfZ9Ogvsx1ZUEnidC67sRTHZGL4uuYVZmxOrqDjoHt1uoY0tmT05X5K-pPJTP6WOl-1cXyF7ocK67bWFTqgJ_XRGHmbARJ6SxhbI5aQ3vjNxb7awAPGvpcelDY3VODwiRt_O2zdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8GONHC0detXysA0bMVJftkZ7fTWXEAM5h2624CUhUxmhJ4jUdSYhKF2bhgeaE-Wly5XJ7mPd0wT2XsDpxB1CE4pUAFxmav-rliibaoJ_ceA_mkbGzciyxHO_eSsihasVsY7KORCqyEUNY_FJJ22BZyxzPpuxllC5A4WT7Ni7t850981ex5x7GNi3JijqmFmwReNwyHqOVK1XxKZZxaWeAfD-Zshn9wf70W1wP0Mk-MWuVBjH8p0fiCwCpLDBIQQtOQxXb7OxpneGVlrQkfZ--RERiu4ivbBL9T2ueFuumhQuXgHq-p2183I31of5cNVXIJ0o_3m6GoUHDej0MjnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=g_v9QAt464pgRF8slKKo99VNRSMQxXrucSW8_HavzQIyKkR5eja-O4tza6pJyWKhUpC-W1y9NsguhIkmbIzT_5RvZdiHZbxS0X8okxkZyBugpb-EHwFHexzyrust5JnbizfpRxeXGTCyAyRg0HnOge9F44bQanrD1lKV0TM6LwrAW30-GJd0-iwy0FdmJI_TuT2tORhfvajhG1Ef_VrueTzAOpW4zgC_KjM26tjzBBz5u0YiHGlCSE9FJ1LvV-fV70RXF58_Qkj5_8MQajcLyQB3JGt4SaK8XvQeJ2NpEldH_VEv5bCBfxkScen61gtP8UCkR2180VlHohxo01IHyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=g_v9QAt464pgRF8slKKo99VNRSMQxXrucSW8_HavzQIyKkR5eja-O4tza6pJyWKhUpC-W1y9NsguhIkmbIzT_5RvZdiHZbxS0X8okxkZyBugpb-EHwFHexzyrust5JnbizfpRxeXGTCyAyRg0HnOge9F44bQanrD1lKV0TM6LwrAW30-GJd0-iwy0FdmJI_TuT2tORhfvajhG1Ef_VrueTzAOpW4zgC_KjM26tjzBBz5u0YiHGlCSE9FJ1LvV-fV70RXF58_Qkj5_8MQajcLyQB3JGt4SaK8XvQeJ2NpEldH_VEv5bCBfxkScen61gtP8UCkR2180VlHohxo01IHyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=WcqWWxnjjQhKtmJwyo2BmMy8w_Cv3sekAGk8OG5ZcDfF2x-fc6nzUdie-ixUSTRCoG_LokIjmj9lpw_tnInCRRdYFeMQf0A1xf90FW8nVGGM1kRNGCLqhiQYRQtIKd9B14uGfTbemJErhTn4mSMhc-75jbq7n8dM5ZixrQe5ligK84DsFXD8ioYXN37og_xrXgEXzQYch_pUYfClFru3aUMR4R2UEvbeODMu3hFZT-LVSNjAv9hMKS2IBTBNDtrbfmfBXxvLJ_jez2ycNQ-oqMHBQeGiQEvWLi5IN1j0fmdt_DdiyI004XEOEGjQRBqVBtTpzXrgyuYQnEqygJ5V4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=WcqWWxnjjQhKtmJwyo2BmMy8w_Cv3sekAGk8OG5ZcDfF2x-fc6nzUdie-ixUSTRCoG_LokIjmj9lpw_tnInCRRdYFeMQf0A1xf90FW8nVGGM1kRNGCLqhiQYRQtIKd9B14uGfTbemJErhTn4mSMhc-75jbq7n8dM5ZixrQe5ligK84DsFXD8ioYXN37og_xrXgEXzQYch_pUYfClFru3aUMR4R2UEvbeODMu3hFZT-LVSNjAv9hMKS2IBTBNDtrbfmfBXxvLJ_jez2ycNQ-oqMHBQeGiQEvWLi5IN1j0fmdt_DdiyI004XEOEGjQRBqVBtTpzXrgyuYQnEqygJ5V4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GV3LoHI5L8oP0898H63wqHKFgYuFKs-iaX7umwxiPhWLyRp4G1Av1mrSJ93hH0BttOGa76v-cbR3knAnwiZgYoVWgdUF1iUsmzemAa0Ti_DXtud9TSHoeV88ByjDe9VOBoCaZ4Rv1PODb1f8YozF7EsN6nfZ6xxBVf2lurG6Bl7JMxMfUdwxdu9mbYbMZmQs95vXnN3F9hWn1Y9Ygoa-w6SH6Dc-JFM0xNWNfWMfkncB8VsaBL0uiHxcw8F8JF_vdVtwKIXxZmTxy2vMP-v4IfjsltS-wz1rwbjOYIv2PTJvTblY0BtQFsMVVT1rAEhFWh6ghxHOGmBeibZcXjXu-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGT56e6yLxxzVJ3fzq7PiT7AJOnnbH4HRUkDrTSNP3LvwayhC_6J_DUQgQgy5Jx5m1vUAnAxpLgRVvNpo2q3F10Hj_ajiFXYRRJ1-k0CfHAdYh6gt4ki5mQXJmNWKFVehjRfO92vtzkBhNxPY34ulEsq7KK1U5y2ia4tfXCcU8Q9MtLdrGB0KujwzKg8_QrrGdp1Gy9raN3w5kZCydOpq1Jy1W9xtpA99KAqwaXcKmWeAequCZS_pVrx4ydMh5XxCSY1xT7RS92Kn-LMLVnmagzry7Gzscjdx_nL3GKU6sK2On_gQaRaPvGBpQkIPNsxWnES1lvFb8jpDc9zWFj_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM7ynBdu-v7uo9rM_Stx2dW33Ovb2ERB6vCjVozq89jNwcl-CfIuR-2XNXcaE4eCWZ8ZwsJSggesytkv-IKW2RqiyJsN90uX08B_d5tY6kmrPgFLm3N9sGLgLVRrwvP5S93llXj_tYqytACky7mvkyi--jLWx29XBhrJeFFNqq01cGKxHjRH8upOL0kTLx7wjbKT5vOEYDHVcNOMSF-bWLdUAvzhRimaacm6Mc-25xZNX3lR2-62FIG9pIBEiZ6A7SVdjick1nKR8sgUkbuEFbEx6oYZyVXOLCDpnZ6yg8SUfcYHKpzK6f1m-DZBnU1NKYyakudf1AlYvS0frSM1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uu38p7FIyRF03mJotpEKQQO7zQJ7osdc6yc-sHXc4bWkccRouvNDB0irbdctMl7HxTLfHb2NezQBbtB8bxxK9Ley3gm8KSaRe5F68oQAMoaeGMkc0Yb4Cvli2goL68IDqv8EBrduWKbaszKaX6BuanTE0aEt0wH3t9IZrKCVgjdLL8x2vQBJ4DkiRB8TjvbFHhZy8CaYonGDf9SQpHPYW_d5UKwlx7QbQAJ20g4L-3Y0jlLlm4ws7088s97hFcI5Sw8l0K9ZXi9xGLF9JTUYPefKX_z9SiYVrIlykkACqjWXlLpRAMmEZ4uU1PId2hHadnuBWqOrxqpIpIV3M2C8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceQVe9sdYtyVKNxGmHWmCNRLEsms1kOeWfgfhWo92qZChyBdhG4VTLx_vx0Z1avKSlHav7UzEgFoRTgcGPALg62y80XASdK_lTYQKN3y-v-RrS7rNpjk1WI0NHGn3_0T9C886U_8Pz829xDEQwvPe3-QASmE9Fhh8RobsrpUYKEj4t_8OWHT4hcGpb0Re7FPWS90GPXTKBkZLQKkzkwtAgTcquui6XvKzItpyMQ4to4CRoRVKT0_xkVzAmuCUMiE3KgVohj5bhljWrmGCI7e61xyiX6WB-tykiB8GdxKokAM8RfrNvO5cESXF5JxHd5DKqtmqpiUE0dZI-VDKmCyww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGNIb8_7d1RIox6NOddt0yEBugE7-5lWsJWuWD0zK6NaSioySSfJygL15XQt5MgGa3L8PN5HuuHZAtTMtnGU2X-EQcjdFS9wmQqxqKNb4_4NIVwZGuxqXQ28hms5Ip7P_lWuFEeyyTFyLAHR8SNIr4Pd1jc7ajHHdqijdG3s4ozBZb2NHL7x3HtJmiVYx-tZrPWyNZd-XsrtzZzZSfvP0PbY6Tqf9zzBhtl5SWNyNUfXq0maFY8qJy3NSpimuhk7oAALLbOmXCpZcqz7rDQ43kOmsjFfRfSyi9MUgWmSE4omnik2dhwaSMQZtgGDCJZZj-qhKDpfbQt9tWl-G71o2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d94ESS0YmzBwaw06FjrrndBEU2v4YxtrPBE9gTnvuNWFjBIWFteYktqDIFwnsaV8lJJ-NaPwvoDlFJLR6pWHql0R2sPATCUZiV_ivJO_bl5QaJxzTGoOckwELVkEN0awBl6ITg8kzY59RtlD6T0Yg6h53sGhjKfuWx5ecLbiGIsE0K9gGw_P862IEH0R2ZhE609o2fj7_3ObWYxM-wnFrbeMkIe-syyKlAnoM_2AIJjQzolM_lUvPPgv_ReQ-dJPKwkFsA5nKj4uPt2-h1lSJBaKg4S9Pgcg7Go9xqFWqBXGFKbJDEYT1H0DJzwGbcP6lZTQLSGDfERCsVR_37l9-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZc_BShmZm76v7P0svWzVGu_kidaJFpohOtiaDK9xQqCeisCeDq_PP-qn8sMVqgx1ohf64vxDdcddQXsBXy4JEj5C6jCEJ4natbsDLASjASGuYRijPZc25KG04y1o1dRKm2Lw_--U0_fQoe-BGPakPiw4YmfaeXtZJhcqrTuV_ff42-UgulMqmH8H7y1P6RAauyufDoIxmsf4_W813ruK0m9qXgj6GxL5SR-gAF7h734AuQED_xdJxtL6pbquaHIvtH-5d7y39RFV09p-xpUldSqiJ7H7FIRMAw7GnAviYUbm4KzzuK_MZQ1zWqftdxPU0jVG327a1qy-FgoPGNcBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHiYe1HiKHsMMVb114IqyDeqENPGurUfoyTCRw7jvGK7uyDj2ybuWuN8jhbatEAEUyE4-z9vuEXOR2n_UZ25o1vqsAk-VYdYGTYph6nGoMPGqUgn3bucneadnRg-kNC9nJMERnPms81BSkqnR3HFy-edxMbn9Dp6bVOiWFFX_qIlz8MVe-Kp8z2dQyoOmp_t_p5t1ECELKrYqIK7qT-creUffPK-gT81WWnI1AJ5AiHLCqU5Mgg-8UwMk0AYGy2mF3rjvrKkD5b4j0K85z-P6qhXPIM0TpO5Yksl2XsjeNvFKdoAaGlhLkVMQvbrcLvlp9fb2HqRGmDT_RU_GNmzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">لطفا این متن با دقت بخونید
و قضاوت کنید:
پدر یک خانواده،
نیمی از درآمدش رو صرف مواد مخدر میکنه،
موضوعی که باعث فشار
و فقر در داخل خونه شده.
مادر خانواده ، چون بعد از اجاره و….
پولی براش نمی‌مونه،
معمولا از بقیه کمک میگیره
که پول پیاز و سیب زمینی و قبض آب و برق رو بده  برای سیر کردم شکم بچه‌ها و…..
هر روز هم دعواست که اگه پدر اعتیاد رو ترک کنه، هم پول بیشتری در خونه می‌مونه، هم کار آبرودارتری پیدا میکنه و پول بیشتری در میاره،
هم خانواده از این فشار و تلخی.
🔺
حالا سوال : به نظر شما افرادی
که به این خانم کمک می‌کنند، دارند کار خیر می‌کنند در سیر کردن شکم این بچه‌ها، یا دارند مسئولیت رو از دوش پدر بر میدارن،
و اون هم با فراغ بال بیشتر، با شنیدن غرهای کمتر، پول خرج اعتیادش میکنه
و در واقع کمک هست به پدر ناشایست؟</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=Tg9aqAUbofrZw0KNL_JnxG-BhgFAR4Vc5CvkTtfx7rijwjMkfI4rH_RGw05miZR9GU1-Y8Kz0ZYDUG9WvAtgL6RoySToiaGr-B6URLgMuRdEEz7KerBV0YCeugv5fhPTApqcQAtsSq5vfyRdUCw-w2sTfMKXXJeTNdUKCZi8nXws1pj09NPf6SQBwFKwduVGXoyNn6b8qv1MXy8kNEM4XIL7xkyFW9PD9nwcNDuAlRipg9CftylL3coD8R7ML-iH0WTTOKFOV3LWA4bZ4OS6aWz6Gqo2b_cdGbojlquZCG8veqUZ9QINsBJ3-hmrelM6GKpW8QF5KI28FyblYPrh8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=Tg9aqAUbofrZw0KNL_JnxG-BhgFAR4Vc5CvkTtfx7rijwjMkfI4rH_RGw05miZR9GU1-Y8Kz0ZYDUG9WvAtgL6RoySToiaGr-B6URLgMuRdEEz7KerBV0YCeugv5fhPTApqcQAtsSq5vfyRdUCw-w2sTfMKXXJeTNdUKCZi8nXws1pj09NPf6SQBwFKwduVGXoyNn6b8qv1MXy8kNEM4XIL7xkyFW9PD9nwcNDuAlRipg9CftylL3coD8R7ML-iH0WTTOKFOV3LWA4bZ4OS6aWz6Gqo2b_cdGbojlquZCG8veqUZ9QINsBJ3-hmrelM6GKpW8QF5KI28FyblYPrh8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVkF8QigaBnSe6ONFOflD7_dLBunUQTpf7MvTiZcegIy8hUQyYmkxyn95F5P4tQjTPG9hB_7vFev1DyySO8B0AMd15qHvC1X94H2Y_uyKR5LdTVzNtuVwa4cSWnhUibW8BE0lSQl6oIktznMybVSk_YWahurXgvDCFw_pJx_Yu8fLlqrnJEgKmZgVTRx0HzLwt2efqhkZUANNjRdtHEYM7KcPZqlaI7vQYC0tAQPpqqljN-vkA8Arag0dDvGCFYptVHj0hyBSun2BKmK_L-_kngJYpFxrifVk4N_K1jo6MEp6wQBPtyK4D_LNPyZgH7JX7kXTFT85ULvW8j0W9_-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh4fxYncMrBXRJTu4Bt4aXhaB1YQ5D_yANEBRcLt4fb9Uvnnz2XvjwWN-egWPBzn1x1aL6aG90dnPXUiLx7YjlF40ACHAjpmq33aqa39-hvemlFzZII4QUJul2dFjVAsfgapTqD-mgh0PVsuY-umOgQ2kjCL7igY7FnFCcyQsi85RhZre2r0y7UuuaCag503l6kuBDn5QfViZQf7ktwc8FNKhrf4N40WRslBQfnyeUX79NK0mVFSVSfFOl-Sk9RqkoKpQCvp-3XbpXKowTfr3zxmqGYLLd82fMasYDuUiGnrd7n-Jl9QRpjdRVf875p99Y8knjE-JlqrSmq--Xypmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9n_H9w9dgrDCe-DR_XdxkfmPjuGHIPEtVV4umpsZ-nlVV1K2ZMvUuzz34TzfcvnBo4QiHYu5tBAQLRbg7x3VGMMd-2O0-xO6w9f6UXKppWGXgbEvWBSqfclPh43ksl0OzigrVOG_zeZEPtswVOoJI1a_wusXB0V63T7QAAd05I9JFL8w6Vnbec1jBRvYy756efd8HJA0XS_xi1263PayEAnuLIA_9NZGFVwGxTBowd3xfNFdvIiipR0NHP1biCRZZ5Dr5AhYHZ1lEWhoaek3UfwnFmHBJsW1dTqfYatgBydddzMHNKlIDpiss9nQMXSQML9lCvSedZE7kKDgS7vHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RupNtz_NQWb2dcaR6nxe9eCt2Gw7P1Vmm5H9nQOj0YxmAD6TSgPM7-ssZvu6eIGEsryK1KKUeBE1JDuZbL_bmiwH_bfCM-s5ACJMKVIVNOov-lWab7JoEXiihBsqnpGpL01UXTjMl7szAz-46tyzMFJeLrIz9WiSaqiLtEhzHMAxSnz2NpwTepiBRSUp24kQIJakN9qtuKKD0KchlEqOIJTAwRBlIIG-v7sBpj6Rj7qsWRDdjhtqj_rI4GNvbQgsVUIwac5cYwbfRpungtsAh1L-kVTK5HsILvLpECOxxrC7fAFMdjeKpzDQ4HMejLbs4tJhHMKHwxvep7raiwGTaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4fgzz6AuEK9C6MK531xVAVZ2sXiw-kVYX3RcpKs02wZiy4mSSX21gnUiJxKsg0H971pdBp5EsYLTOpgZoGJ7sW00nqWA0r8wXudocav1_aXPOiaOoG_rvvAgdyOiAAp7DtusQDjh5vTZHW6HULrOMfC8hwQ39Zv02sdeCU85Ts7VvH6Ukr14aLimyF5_t8ba9HQIrDLHyoq859ILEzRIvVYt1PgAnycUcdFJX0BCZBV1p1zx6Yyr3XYGfxrRpeJap9mKcxXr7REFRCbL1i7VSAMQY2O7SpYHX0HN1UquDjIgnQLghwkOKsPnEwyV8PGZa5YT3UbZ57ts_YMsPlJBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BeYaxqpmh7Q5Zutpecu43tsvd-iRpFNeZCDJFAC1E6KAUH41gqn2fB0QkzZwJCKIxf8YcpxXwLEeO7bUlNy_xOyuyzA4Y0FqeDeY4vRDPFuOUllwCRG38df6AWmQJ4yCou6nYo4wttNyOW165t0gdNfWIKM5Y4hXCUMQ7_VQtNmfXva4KlVoCnKU6hEmRBVXExOsqzGz3HF_zfojJinElSH4MNvsNA9AZGAioWAGTb1fl3621puVgSRF_Aib8vBRfhr3fczR95EzBn9qZcahpoOIEtDr1BbJ76nCh8AoGi8bueyyxL25ldY06R9ZbJue68eSnVgJp-m8CQ6BMwwiQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cCDjfKETdvKvqF2NW_socXIw1kteEhzrKQyJCYI_PMqIgoniLKIm3J6C_RV35JMsq71_F9F_1hhun9bPFYfywG6GllXC_bwf4SOXe0wxQA08tA61tuL9_jV8YYrH4E3qanGtnUAGrOmuxFA_TzZ70o-E90emG8an2KD1MnRoCbW27stNLoA5_FyvohmOiSvTXzEBCDuuPqYFq5glS2IjX8h894_fELzI_GlysBowaE41AZ_nH6c3SXgbXoo13s4vBGWSCrWSURhMNVed43PxXb_SjbERrRnf55LS3rZ_Qm64KRHaYqmlwdJ9aYxVcup6T9hjJ3s6N7aEmsEBG-3lJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=EIpWwN4JfV7iraX4UjLX10ujYYKc4fjSbKaSQHP9ud9mfQ4OiuLk-UbrL6JfuSqBV_LqBu3499SvSzVUyENwRgh248IqepMAssxdJ90leYkGH6QOpdU_vd51PCusP7ucu7SGpmSLRZ1_RB8m_EQDNWW45ucEKTzpWu7Ljaf6A9lTtb19cdnnJhpG4a1ovziFpfdP4jCh9nmxIT3Ld9e8JGoY-0dmWiLtHg7Ni-EQcwDCqBI-eG2MBr8pq4GUdLX3G1rAWW9j1wOdGjaPUkniiJrmeS8rfR1nHFkjUG1ubsTqiVV7XkWOUnf7-TyUza7awN8gyFb_VV-e3W-MDppfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=EIpWwN4JfV7iraX4UjLX10ujYYKc4fjSbKaSQHP9ud9mfQ4OiuLk-UbrL6JfuSqBV_LqBu3499SvSzVUyENwRgh248IqepMAssxdJ90leYkGH6QOpdU_vd51PCusP7ucu7SGpmSLRZ1_RB8m_EQDNWW45ucEKTzpWu7Ljaf6A9lTtb19cdnnJhpG4a1ovziFpfdP4jCh9nmxIT3Ld9e8JGoY-0dmWiLtHg7Ni-EQcwDCqBI-eG2MBr8pq4GUdLX3G1rAWW9j1wOdGjaPUkniiJrmeS8rfR1nHFkjUG1ubsTqiVV7XkWOUnf7-TyUza7awN8gyFb_VV-e3W-MDppfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=gxmee-IDGJfqzVZnPg1s_hnwKee55V0RbDFRFoch6edsJDoR_A34RZH_y2UQzkeHBKkiUI5z5IdXT9L7UxUyUjeMsqGPJLqoS6VBnk1f2Sn2Y_5IuMSNSJKA-TpxhgQU0kz896E1qBCMpS3qDBqSD0q7JFq9Qgt14RUJ1rqfP06-1BJBme-_F-O1ts2wy0_-X7ZcV9cnZzoC84Ak71GQjwxi4emFoSHgYm7l8IFYG10xT0gCkkgb3FeeSYncR8N8CUpkwmJsKZZj01Vf94FHg-xu8bvS9R5TZUPRz6Geul8rsOl_UT4QOsqGwzKg7ds5cJaR7e1WmzF9FDrK77pzww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=gxmee-IDGJfqzVZnPg1s_hnwKee55V0RbDFRFoch6edsJDoR_A34RZH_y2UQzkeHBKkiUI5z5IdXT9L7UxUyUjeMsqGPJLqoS6VBnk1f2Sn2Y_5IuMSNSJKA-TpxhgQU0kz896E1qBCMpS3qDBqSD0q7JFq9Qgt14RUJ1rqfP06-1BJBme-_F-O1ts2wy0_-X7ZcV9cnZzoC84Ak71GQjwxi4emFoSHgYm7l8IFYG10xT0gCkkgb3FeeSYncR8N8CUpkwmJsKZZj01Vf94FHg-xu8bvS9R5TZUPRz6Geul8rsOl_UT4QOsqGwzKg7ds5cJaR7e1WmzF9FDrK77pzww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHw-3ofC0QBxfebUtajdZ7azgzptnE4G35K-7mkvDV4LKwP3yNq7NHbd29YZE0d-ey5iHkiOsKKnehEn-UvRieUg_g3x0ZkogWt_8qsrYpKMidtfO44LKtP-Ff0Zt6FC4gziJlYAtraD1z72WHdWxLQuT6DCJ_v_2hnUmOvGIjCteh0I_9qUcYDU1s4_5qVCoaIL1pm3ez2dwu_rBQWrJichQPtG2PufPTzCvSDjPRPuenE-cWJyXl6ny3-379ZZdLUnngKElAu8-hinf5yMBafPT0CMgA_zSYrcXbIN4Ig_HqNHJ_sSV4qXZL3PVgDgVPVHFdZWTE7Fpt76osu8HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRB1f5LylCPdC0jm3dGGjboy4zmjwGtFL1-JskqK3ukkWUr9AicsJYix-RJdDRWi3BWc9v1H6ZmlU9PPq51P39jTeAZXEwr9vwVOHZe_tgMVUoLrzPkKD3Aoz55zp6Bb8UnwhIGr4VSkW7JrYPslNB-3y-gvKH_ROxyYBcOn6ILJ3E6tRm8dwLPFAPp8h0lcaS-fJyxZlyMg1rWMmodxTIHoOXKLcTZmA6i5RibBGdC6EgKFTDo9B2dKAbKRt4xN_OzDFAV4oSEcLdquYrqHKvbV3xs7Tc-c16hF3udkuDAydW4z6XNa2BJM3naMdZxArEmmL-lzYquCy-figfTOuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=aQ7THrjYYo4FMAdSYF0kH_V4bBPwZrXMhIm3Qiqda8yG6-5D3IXAY3t95kgG_Yadv9NvntFzDVOT-8nEXO3RbvIo7K4ZcUHs7MvptvFjaki4oLcX_htqo8jslR-mGAobHI5HPDhospbB4hwNq1FOdXKUJvv-FQem5y6f95hqGoRhQ2ia4uZ8X_yh0dqxooFBJ4kUtRp3Rnj6XSbrU9wya86_VzBDMbMLb4AGQ5R1npVR_BOglpImAxn_6HVIDnDZLpruLWocG6LyRfEhzDZ1STyLasy9_wyNj4LaZpQnGeWMI3UTtcR1TtALELUwVcWcBYkRuhLQ08hQjzt-mL1htw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=aQ7THrjYYo4FMAdSYF0kH_V4bBPwZrXMhIm3Qiqda8yG6-5D3IXAY3t95kgG_Yadv9NvntFzDVOT-8nEXO3RbvIo7K4ZcUHs7MvptvFjaki4oLcX_htqo8jslR-mGAobHI5HPDhospbB4hwNq1FOdXKUJvv-FQem5y6f95hqGoRhQ2ia4uZ8X_yh0dqxooFBJ4kUtRp3Rnj6XSbrU9wya86_VzBDMbMLb4AGQ5R1npVR_BOglpImAxn_6HVIDnDZLpruLWocG6LyRfEhzDZ1STyLasy9_wyNj4LaZpQnGeWMI3UTtcR1TtALELUwVcWcBYkRuhLQ08hQjzt-mL1htw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohVOzvIei69O4ukxkGcubjiv8HxnqfRB1uqO--jFW0MwXQP6KjGx9iHvGwNq7TdC6h1GP6n17PZio-NqrSyG-Qd1IBxu9IlIF482MBZbSMbaJQ-BhCycW1hr3fdBD2iaTZizvcTY0wGh56gvcNmYhqG3zoQSRRJBoxd0oY7YyYjuem4W7ewqVLG9fgIUkhM_AQVo6Dnssrd2SCVv5Jr1pw6P1LVPItpzG0fGklACGLTUDAR3i3sv2_3UKNZ92mUGRFpLEEQhIoCEdJnfgQzWBmYzvOmJkvQB2xsjyKZGyN-euSHDKP_-wPP1rP_xhwnNzT2kD72x-REPavIOJVxhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
