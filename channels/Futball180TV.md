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
<img src="https://cdn5.telesco.pe/file/Uo1KV1i3JQ99jogJx65kuC8P7tIK5U3iCG10r0xX-QB0oaC7QHtPQ6zw6THi-ra7gZIlEKFDK7DsbD1YJGzlcd64BZPVzNqNuzZkO44OdYSyZyKn-cbC0bBjUb4tUIBRiob9r411c-AsYJ_bQpQ5dbEr0ygtLULoAYPAz7EHxCKqCqc-mkQmRLx-h0A9Aa4EoQoTYnZsKnXU71WiygkawXfwTpFF5tZJ6zc9GRk42XJWpuFSkrGrYBnVaLU6w566eGPKZpi3KcFsuWa0XkTJULeAZF55dUU5fcFakpdlU8cgdV-8GvzDy-kxo1JdMadfCduQJgXvGoLvd7CrFPctOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 686K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 20:58:30</div>
<hr>

<div class="tg-post" id="msg-96834">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">برگاااااام</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/Futball180TV/96834" target="_blank">📅 20:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96833">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گلللللللللللل ژاپنننن</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/96833" target="_blank">📅 20:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96832">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دول موشیا چه بازی ای میکنن</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/96832" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96831">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTV99gUSWCtStfGf1Wp9SL2yBWLClrfPEWG4WmafghU-GfiCU6uyLLjYnh_CsWYS4yHOS8JCs2hBFbscyS2GTc4PoNdmE0oZ53SCADVAb9TDfyeEWsh1v6SeJyjPUI417Ua3yVbjU6dwXbjOu48LW5-4IyocMeOCbSCIAb8YzsFtaZQ4R6N777lW0tiK-1BV_G1J7fDR1cLXlZeSE60vYOi-yqDQQz17sBamLNGAUY4W3-jca_hqtUBf-pRhc661sLE-4AUITpND3DOuKcRC0RcpB1HFIlfj73y8YSMvacQYxfGsB1VHFMNz3IoVWb-ljEqy54zMSEz4feT2UxNk7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرشیووار: بازیکن ژاپن باید تو این صحنه اخراج میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/96831" target="_blank">📅 20:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96830">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سوزوکی چه سوپریه امشب</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/Futball180TV/96830" target="_blank">📅 20:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">برزیل داره فشار میاره</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/Futball180TV/96829" target="_blank">📅 20:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96828">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZIyfmOUekOHx_rzI-5aRQdeZ4T4v8n0A6sQ9Epl8XysioqdRnZsS2cl3PK43ZFFP2PlQgaUjmty0JhW26w8gcmNKxSJNVlkg7Y_Gb6IefbszvpacO7gy9B2eRJCNt-tEc1OlARJnWRmzXr2q2fG_doDIk8rq6BcHhsU1ERidVSZX3VJr8X4BnLg8ieLCtR9wjd6cNu55aKz3ezykxX-1OcTbQxdJKDQw402yEB-O1zXHn4rXT2BSTD8I6CETeXr6QKVDNam9Itf5fBaNCohpa8jkDC9yA5uP4psr47ML208dxoOo8t5BSK9539Q7SQsWosjdtulm0dnXTqJ8BznCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عشقتون رو نیمکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/96828" target="_blank">📅 20:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96827">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">موریاسو همچنان درحال یادداشت تو دفترچش</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/Futball180TV/96827" target="_blank">📅 20:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96826">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شروع بازی جذاب برزیل و ژاپن
🔥
🔥</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/96826" target="_blank">📅 20:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96825">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPHNLhGOLAtFTv10IT1fLpKbnb84yT1C_mQ1IqniGpuzf_sSgL6b1Gj0JRm6lQ_yK0bjrNc49eA3wVvJRVxPec9u1Y_i9aN6H5uAHswf1S1Oc5CoNyUKELlyAWzgCQs_ekLaf47C7lY_IgaagCACOv8185xIdPbFgnsw619Fhaz6QsnYYMuWp903dGhjDn11Z3nh-dWpP-o0r8bLtDJPjOjjoREXSN-Mmb8NKyELfD4eFv7Fh-oLwmG8UI0qUjtk0NFyQDVWwY-fVo3JOfB5mAB0KW1aV2ygXYg8ocT6Sbpu8PoDQTQOfDAnAzmGfsCDx4C7EJM01Wb3djrNizOYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور رونالدینیو تو ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/Futball180TV/96825" target="_blank">📅 20:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96824">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e1e888ed.mp4?token=b0fYNpTqZ3071DGUEI54P0jj2r-0MGTUAcIZJZhaQs85IDGZ2AjfwhepqSMP6Qya1Z81ry-eBFi2uqMKC35VQ0tXZBARt7Jue4_FRaJvOvBe5p_SHmX0_7CU9w8YrEjkxW8nt8qprnlSmdhNosS3PQJU-GOgcv1Q0reqQEC064dou5p-WTXpNBw223E1chREf4RDRo4DsEjeacaCeZCdmxcC_j2xbGcG8jCweN2QABTOg_K5idRhBlpcH5za1FgU1BSdrQK__t425Yr2gFJ-1dbUe4JhD4p9BBiVw4kcfCYESvTNjibkHxBbRDJp509_1Ua-FY-5E6oCjcs9HizhCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e1e888ed.mp4?token=b0fYNpTqZ3071DGUEI54P0jj2r-0MGTUAcIZJZhaQs85IDGZ2AjfwhepqSMP6Qya1Z81ry-eBFi2uqMKC35VQ0tXZBARt7Jue4_FRaJvOvBe5p_SHmX0_7CU9w8YrEjkxW8nt8qprnlSmdhNosS3PQJU-GOgcv1Q0reqQEC064dou5p-WTXpNBw223E1chREf4RDRo4DsEjeacaCeZCdmxcC_j2xbGcG8jCweN2QABTOg_K5idRhBlpcH5za1FgU1BSdrQK__t425Yr2gFJ-1dbUe4JhD4p9BBiVw4kcfCYESvTNjibkHxBbRDJp509_1Ua-FY-5E6oCjcs9HizhCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امباپه تو جام جهانی وقتی هر چی گل میزنه میبینه مسی یدونه بیشتر زده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/Futball180TV/96824" target="_blank">📅 20:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96823">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🔵
🔴
اسپورت: بارسلونا قصد جذب هری کین رو داشته ولی طی روزهای گذشته پس از پرس و جو متوجه شده که این بازیکن از موندن تو بایرن راضیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/96823" target="_blank">📅 20:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96822">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/750ace79b0.mp4?token=ULZqFfULDYNDebxO8PDhOgfT0ju1x7HptfK7-ySyPxDo2LrUjIbZIr7XNK2_Fofx2PCulcyocMG9_9vVyszP7Sy9TcLWMKEkres-p_Y2Q_TvmoByRZAKac7gCloTIeVZSIAUm8MqHLC1u_nsWaz6adyPRR0DUMn9CA84LzWKIB2gxnYIdfBCk1jr5BCD8ZhsKH-JRmXZ0RS6doMIdUpPmvxCEUcHkIiQA5Rw-isqaqvFUMPkPxx7wpJbULcLj8GXtGjBWGsJN3hrsWnXj-cQdRXFdk6_G7Jash_AsyxlPl3wRrOuoC0RnjlaQkR0Le-n6jn5Amn1VGx1SbRXlEZYrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/750ace79b0.mp4?token=ULZqFfULDYNDebxO8PDhOgfT0ju1x7HptfK7-ySyPxDo2LrUjIbZIr7XNK2_Fofx2PCulcyocMG9_9vVyszP7Sy9TcLWMKEkres-p_Y2Q_TvmoByRZAKac7gCloTIeVZSIAUm8MqHLC1u_nsWaz6adyPRR0DUMn9CA84LzWKIB2gxnYIdfBCk1jr5BCD8ZhsKH-JRmXZ0RS6doMIdUpPmvxCEUcHkIiQA5Rw-isqaqvFUMPkPxx7wpJbULcLj8GXtGjBWGsJN3hrsWnXj-cQdRXFdk6_G7Jash_AsyxlPl3wRrOuoC0RnjlaQkR0Le-n6jn5Amn1VGx1SbRXlEZYrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😂
پشمامممم اینو ببینید امشب جمشید خیابانی دوباره سوژه درست کرده و روی
آرناتوویچ و خداداد عزیزی
صداگذاری سمی راه انداخته
خداداد عزیزی رو ببینید فقط
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/96822" target="_blank">📅 19:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96821">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDateOpiE8fXZFLMB4d1JWJ5YgPVqQHsV0CsbenbqYvfJCmEkuevGaMTfbD3D8nTyrHA1MboXi81SEpaPAUSPTYjjlMwJLzIuINwjGwR3qWAm7cuxZlP7jZi-8e-SepI0maLWXAPWqscLkz7oj9qjAlHvvJUi6DwF4djxn4Xk8YNImKBCWWlu4fjAcB1k80WZyV9zHSOJpaWXBm-k_kit-zzZmnqYhVcrDgF3Qgx75LK7oZ9bwFpKmuIKfGIg5SBkCGvW9GDEVTSobqfi8YIZG-Ncc7wXDLdVvEsdJ72oTlomxsszM6RlQNx42gid2uwvNNXA1bFXIF6LBo6cwa2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🇧🇷
نام‌های فرزندان نیمار روی کفشش.
⚽
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/96821" target="_blank">📅 19:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96820">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLOSW3ovr77yviiIWgYwkSNAUMfwTJMdBJE9-rb0ABIP6b4RGWN7zgRtaNo0KHc0GCOQkTnXiJRGdcG5qUjAhkhfTZW2ExiCSd9S8pqCBFwW5SDEoQCpmfcs7uGEkQYlq40TcSM8MZFnGJ8Dzh6RjvJb5wlm2ZNzj8wRzXT1j4talNSzqgVtCUtNVyl3MoBblj-rWm45GZ-ilmXLDf_m4tz9jS27dnV7cSFyLs7lZ4Vh_FHMCEaP5x63-yWntm9nt5gXwqvlEC5-MpTZd4BSfz2F1_vXyYUoZiJZQ6OMTZ7ZVB-nIKaXYTLzm6Y95ueVfrdjdG_DsnpLB5QIvRKMvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
پرتغالِ قبل از رونالدو: 0 فینال در 75 سال
🔻
پرتغال بعد از حضور رونالدو: 4 فینال در 21 سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/96820" target="_blank">📅 19:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96819">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/em7esDFFcrest7UO5jL4h8ThMyoB1lIVZZSqBAy6bHlvOxoruObVZ5l5WoLjy-xGWu1IgOzEQ0MHzndgvG-c-R_geLO-u_oCk9jZvctbQMyfj240nQ5nSKO4edCuFejPhSUv75j35gWkmmUlJ_c3ntPkrbjJRw7qxFgxRvptqX2lpoU7GJC1lN9GzQPbUMVAR-hYNTWE8YRHfjg-RdRtcoPymQkS5BNSgYc70faxwOtuLnqlCy_yrxHhNVilJ6sZOGN_8VnKV5g8lGq6i63kAH1ZNmh0jkhla6u0dOC2ngWqdftovFLVfmNR8DHKAFlVr8thPvrf-dIQIc28zENr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برنامه فصل ۲۷-۲۰۲۶ فوتبال اسپانیا
:
🏆
قرعه‌کشی مسابقات لالیگا، فردا ساعت ۲۱:۳۰ به وقت ایران برگزار می‌شود.
🌐
فصل جدید لالیگا از شنبه ۲۴ مرداد ۱۴۰۵ آغاز می‌شود و یکشنبه ۹ خرداد ۱۴۰۶ به پایان می‌رسد.
🏆
سوپرجام اسپانیا از ۱۱ تا ۱۶ بهمن ۱۴۰۵ برگزار خواهد شد؛ دیدارهای نیمه‌نهایی در روزهای ۱۱ و ۱۲ بهمن و فینال در ۱۶ بهمن برگزار می‌شود. محل برگزاری این مسابقات هنوز مشخص نشده است
🏆
فینال جام حذفی اسپانیا هم روز ۴ اردیبهشت ۱۴۰۶ در ورزشگاه لاکارتوخا برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/96819" target="_blank">📅 19:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96818">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDPHuElBlsP6GrDxlzcJzRiFzmMwDI3mRddZhOQhfs1J_-CT4F-LqweuMq1klsNhA8KcHclUc6synkfJDFN0L-mrrKUGSnGJAxAHR3dvXY8uweyNL2QTeo8cKSq1EmGvzyWR7vjGdTz8ITUp8o5XFPUMoKNjSy9vG0nnkUvZcSiZP1hFlqtCCLgSCepM1Q61aRKNt6bt7aesKCq3dfRFXuIeBNRYcykqENeYW49z6NB-PuSoILH3YAslA-YCuuPriow4GPRs3Q0pKsqQ0wOy6vYExaDlrqWzASaJ7fOJtrQn84WDAkE7p_0Hq_A7D2oSTG72cbWSjUBMGO-A-q5Rbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
برزیلیا در یک حرکت فوق لاشیانه پوستر قبل بازیشون رو ناموسی کردن؛ این شخصی که میبینید دوست پسر مادر سوباسا هستش:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/96818" target="_blank">📅 19:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96817">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4223b69552.mp4?token=IJ-okd0587bEmZbO_WV2nJZ7NVV_zHO3mvi3vqyorxxnb1EPagdrsAXuIvOBVvyVNUxA2pliE7u0vCOUi5oWMkOB4j__47hTk27a-GyHGOnnpN-Tf5Px4cfjQqsinl1ssSp_y5zDPXwabs4566wqMESd-rYZ07_biL_aSn2HN7c1LiR3jskTNRcRJg3_1lO2x4J8Y86Wqndf082jIFXyGPoAqsLHcDiZpOq9PRzUYk-pUXQnTrODUlpGxOHbgqrePE2-GPArMnEo7bXmdesxQZjfy4yFuebSDOl9kdALwhy6UXP2BIbtBtkwiuYugbYBEM-hyNp0Bui27t8hQ0yFFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4223b69552.mp4?token=IJ-okd0587bEmZbO_WV2nJZ7NVV_zHO3mvi3vqyorxxnb1EPagdrsAXuIvOBVvyVNUxA2pliE7u0vCOUi5oWMkOB4j__47hTk27a-GyHGOnnpN-Tf5Px4cfjQqsinl1ssSp_y5zDPXwabs4566wqMESd-rYZ07_biL_aSn2HN7c1LiR3jskTNRcRJg3_1lO2x4J8Y86Wqndf082jIFXyGPoAqsLHcDiZpOq9PRzUYk-pUXQnTrODUlpGxOHbgqrePE2-GPArMnEo7bXmdesxQZjfy4yFuebSDOl9kdALwhy6UXP2BIbtBtkwiuYugbYBEM-hyNp0Bui27t8hQ0yFFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای خار جبر جغرافیایی رو
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/96817" target="_blank">📅 19:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96816">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN6-T4hVCmMW7rB7L9pvzWL6PMEaZCwg6-dXLSquudv-ECbkbphzoimyEO30lXXRNm4yPEDGmmsHs98AMrVN6Gb4Zidxyo-Y_XWysJjoma8ISFpMLNKgmdpr3ryyqHTKDtrngVdMP6oicfa-ToXhHdC4K8N57cBVyBMk5HyPAi26zEuSp5ebESkHr-0ddU4XtedykAnlBL082hbsGD28Ql-2A6394iGA1jpjVjWb-uVlQRy830jbPifC8DH4PyzbMJoJ1PmFGrW0IHqUg0TrWobY9kmz2e5pX2wYSd-VrkOC8cw0bECXfEP47sSQOsHQElPG7tiD2IGD6mo0j0L60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو نازاریو: وقتی به امباپه و بازیش نگاه میکنم یاد دوران اوج خودم میافتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/96816" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96815">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekE6QTNxYJLIaIwzkXw-vpeRG4SKyK3F8DS9XYkG2E0vKFslA6vgrHgWqwS9AJsQ3QVPnRL7HG9i0tITN1igefa5VRXBvnySID5KofpnTfW3PGhLwoRnV6I_dWAlDmZv1m3RuGiVRrS2n5Vf-FTwBdew0Gg4s_qYyknDRiGZCaJSThfUuB1VPtGK8Wrx8fv7rzuDF7I-qEjRRnAY2m-8WY_VmUgcnp1TooI6wEteyWp90tQFXC2BvvGxWaJlcM2IjwkUOHbrUJ2-1I_e4pK0umuzf58MUz_BsZdJvazppFn26rL7mYRKGqA65WGAdLVe5WK_j1n7JW806h0oY1J_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ترکیببببب رسمی برزیل؛ نیمار نیمکت
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/96815" target="_blank">📅 19:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96813">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OE976JbBl9R2m95Vx1LA0_6aCFlhUQvYskEs6IbfMl2F8F86X7QwibZOYNu9SwPgo8fCww5ZZICNMJqKDvPWATxioVe0E68emWguQU1MbV45wQIx82w_uxESzkaI5b5NwgQnMK0mxGs_ygZl-fOb9cH0Yfq5gEsXnHU87xm4MdThvIIDpUk_rdMTbv8r46dqQe5Vs9sILM4SIZYuMZqqM8aLpBLi3xFKy02WitW_x0KiHcGnucTP6eQ19TCXLjA4fmiFQZOZY4Q5OlXwp2b1Y1IQFJje0NaJq7qoq6sbVnqNY8acOHZAxtl6fsuKWfTPBrijLGZumYwH_RPoS01eAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4oOp7OVRdnS_BJz8Px71k_S0BiuUI_REf3Qr1AkRwmbr-YnshIpvu9coqz81AJ0Z17F5vU_b8AlAk3NgqApnLZiMMtenqtXezv5juqMuApCpNn4gSgwOF-6IQLbJuZn7j2xswrexdxtTHhs-0K9L_2EuwGG6XJLdre6BY_YNRaoYg7UiLbhLcwsfBiFzHS4Tse27uBcdqPom0v6Y-te2cUSQXMVe4LGExH-xBg79ThOPDa-En6kt_8f5YklND1QqAIKc4jV0bxukFDewwyf3LsOtSEXawbESfkowCbS31ikGquyivLsDKa1gVvlFAyLrzapWbkIplFYpt15Fzn3Yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور بانو ویرجینیا در استادیوم
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/96813" target="_blank">📅 19:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96812">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmXMgrZnSeE_5gsc6dBVfWiq2zWmBfubxLx184EMn02LaH3QcQDZ1wNgP-eFJVqJXKbW92fnUJB-Oto1v-2ukPy0UJGxcheEIXBb36nAH3EwGNB8-yFPD64uczPkYesgvgyTVLtfyh0ARhWYtaSy7O_5cuQcMTOLZ5ow3LYVgtrxvZgwwuGAuH8nctovPM4cRszMP_t9PLKIFigY2l2lA3IJMj7Ko9Us6UXK4NZztcpFLVkBP9_5Uz3uMBthnniaR0ypGeHCxvkFw2MWwlRZ5uOcW2S0Z6HfsgxrKgKvCINYhtkFVekOMUMiYP7qOa-iWea515tZNx1RMSWrcamWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ترکیببببب رسمی برزیل؛ نیمار نیمکت
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/96812" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96808">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEy22kuX3IXWnYnG8iCdNAc4X7e6BrtYcdZ4r292AUJOuTXYvzsFsieXkRAO9UQAoQ7dQdvy_6Z4neBvaONjRMoKYS4r0VeOPg-maUQNofj9cYrjQXZZxFnYWcTV1CcMU2tUzVmnNPq1EkGdG1C3FjhrJljKqrhjO9DOAq09nevTIh1r3WhCJUkxHAz6s4Pm7rXjlqXriPdJjDK_1FBBaIIUF8P3PZO7G7rMs1q2FIatmkscJ3YJHqEVYCw-xfBTrsYUnOSN91BD0n9lcdXsvaHcZsFQcWw7WRfKjSzSwc9suU25uT2ztIqZ-J3_20UyaBvJUI51WRdcmW7O5F1jCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKbdgH6Hxi9M7t7X6TpXhhVQX-nnDvnoJsL7P2IEGKVo0oM5M21MKdg3dgtmSceh8WLJG97vtmR7b6Wbv6_QUWFCQMIrF0vdEUvt3UO27NSRzbvLgNARyMMMdM0-gjVttw5a8aMlUXCyD449dDLI96S52h8EBSt2gpSTdlDX96wnCOGf0xNTGMkMasaadkysr2XcXVMXD5dgfRldFnnZm4JzeaZq0tIcMnTgpD39p39Vz2zK3MSbVQaxIr_tr571-FOXSKk4bJazVYaY3LqEhUgfRko8I8YkYKfoE158GD53prPRiLQXRfJsWYYGSdjr3AgNEDaiTMBf7_hyMYMiXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LFArsZOQTb8rifXAwBburXCao6WcMUkZ7rUXgmrbm4jRyQoJlYmYI4Y_JoF-EEnTMWCIWpOa6MHHkwlMhbJ3arXFIBHyT6JPnhMO8oEsZngynJ03g9KRQ-PW1tvtx5Ccp_C9OGPRJME-CJO24Otxjr2-OQR3au_EiiTkOcwLYSa_MiaZpfeZvPTyAtsXZE0miyV9_70dUDcUQm6TLQwdpsD1N_cSNyeTF5aRQDBYRte0Fnu-mLknKBr5-irlPf1MrqJQ4NTpSvbwAvBViB6Zkgba6uMmW5S1QSzdMt_7_zuYc12cchI1OfdY3tAVzmXFISvDk5I0RT-VxeBmy2HNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwCBhDWNNp1Qy_zPKA7k8z1Te6wZBaZXxf2WbvsvNYNdsE4w_aNlKtZfdCN-1vIdfzORxarCJJ7t-2ZoY3Dl_Z14UG9coMDf9V1FVWsYJ-4zdEoyQfANw94rLZ0QYacJedUVYKVk5ucA_f3Ljnc4U17GGmdEWia6yDmpfqXXlWAVQ9zfDbYyZtPC5B1oVOo96RklUeCBOu4JzvzEUoa2iEjl6sHq_nX4XjuouRup90caAWXFWRLxL7T1OmrpLV8RNbugUyN4GatvpRqYS8RzhWnehjqPEDHqmJpWzFIyjMy6A7t7d19daHX_bGAHOYIUlVrQMKeUr0O7GFOxBbQ8ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇨🇭
خانم‌آلیشا لمن بازیکن تیم‌ملی سوئیس هم رفت قاطی‌مرغا
👍
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/96808" target="_blank">📅 18:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96807">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fymN9I0Fsi5T0jB67zyGDp95c5RNI_OYTHvGIIgE7CElPhIdMWGE3x9Z2c3xLuy-6tKeYSOzlIbb8CRkPiDsWscDDg3QMu2t43rpTSGT9u6-o7Q1hSVTV6oYZZbAqYmukap--o9Xj1uuDsHfL4DJrPNyBGeBSBDJbmUgst0lXdnOXEfKxtiBQfGFss7blFfhxTuxZCQpzEj9FpZcBw-qaxh0KtgAJnVn8yTtDrpJ9OfgnZ49Pd-cLvy0aOGYmvRGiZeHbqtZC2OAaepvElAC4mBkatil2DyyP1DIbFo7TzZ9XQSd4beSK7KQJAu_Nrn6afS1nrMXXvkErPnAoRO5Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار دو تیم پرتغال و کرواسی همزمان با اولین سالگرد درگذشت ژوتا خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/96807" target="_blank">📅 18:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96806">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c36f5ccc71.mp4?token=eFRsNyLkuzfG8F-MhtZ7TIvY6WxWZ46Pq_5V2YEO4bBmIPLkVObADyoWyPGgN_EYyaWdxiYDNLLEUIYe-GxA0ZcyAOR0LlxauoKYs4aTzrGdK74fnZRsdpEzC1ywY0rFJtJJLvLIeMrG3m0h1krQ-6tle--7_n_YqnSiielB2z5tlNVtWS0q8-ITeVL2qeZxu0K7ebc5miGOdKyZKM8gsuh64GH5W_1-u7ti4QQTI-YiPZOE3J_kJvUAv5kLvqmLsvXLCRZVmM89VtYYoPeyW0FojgpiM2Bay3LhJkZBbiHeA4ZnICPXltP7S9wix1mhVB-3iWHhumPdwPI-x2WH4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c36f5ccc71.mp4?token=eFRsNyLkuzfG8F-MhtZ7TIvY6WxWZ46Pq_5V2YEO4bBmIPLkVObADyoWyPGgN_EYyaWdxiYDNLLEUIYe-GxA0ZcyAOR0LlxauoKYs4aTzrGdK74fnZRsdpEzC1ywY0rFJtJJLvLIeMrG3m0h1krQ-6tle--7_n_YqnSiielB2z5tlNVtWS0q8-ITeVL2qeZxu0K7ebc5miGOdKyZKM8gsuh64GH5W_1-u7ti4QQTI-YiPZOE3J_kJvUAv5kLvqmLsvXLCRZVmM89VtYYoPeyW0FojgpiM2Bay3LhJkZBbiHeA4ZnICPXltP7S9wix1mhVB-3iWHhumPdwPI-x2WH4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
💥
خواب دیشب مردم برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/96806" target="_blank">📅 18:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96805">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX6ua-OKxXxUD9BBh3ZP9kkGgDFTboZjJFHdEUf5N8SN69NlKo0onsX-HMRD4ncxUM1UqVe_deCxo-id-A7HCWgPt6mhxxLi8f0OU_SsH0Qa4PfvZhLQBHpuq_4S5q1q3MSckpyq4AML049bTYQ2p_S1F5CQaG39ICN_YGFTUB325sOU7y4husv-5YEPbbSFf0VyRDCp0_o63_VN8eJnZtxGe_wjDU-F8yJab_1nzhdJ81jxqYzuFginZ5WeQed8Y_54etWYXzjEfjP7LKyDAtv1Q_GlnasM0KrMHmR9pBdqiymFZcnqKscYmZXA61h-jpXZbAlt-qkJ8joKFiJBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
68 سال پیش تو چنین روزی، برزیل برای اولین بار با پله 17 ساله قهرمان جام جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/96805" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96804">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دیس ابوطالب به جواد خیابانی در برنامه جیمی جام
والگلد قراره یک کیلوطلا به شرکت کننده های بازی جایزه بده
و اگه میخوای برنده باشی کافیه توی بازی های پیش بینی جام جهانی پامپ بازی کنی
تا فرصت هست ثبت نام کن و بدون قرعه کشی طلا ببر
اینم لینک :
👇
👇
👇
ثبت نام و دریافت رایگان طلا
کانال تلگرام
@pump_vod</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/96804" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96803">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpWxzLAY8KktZvWa4mhw9Bt5SLM4Qo25Sevv_xfEpF1DK9DdCRME0tvxPgzAfT5YMiJCtZTh3ZeGZiDsJhhbC5eHbOtyQFjB6QvvfdjQJ-u7473v12tykeG2ClDGi7OCRoe9N3GmUR7E9S26sLYpLFkNTZi30c0mF0DEGExxT4DV1onX55NQyDXg9tjHn5AVB4MuXrBIgj-tBR98XytUmzf1LpY56XkG7iXN_gI5wiGpCZwd1ZAqTAjn0TkivPuZA0uLTzfNKoCpyhjqqAeFKU8QMx11bWF0uMHktI2vqidHXFAwv0qEC7sorYoakg2piuraiKiJ5JOEGXeFD4rEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت هر قاره‌ تو جام جهانی 2026
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/96803" target="_blank">📅 17:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96802">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyB2wyzb4H6OTcaMKEN2FpySKZ0QS7jtDEJv7zvrOQXwZXlvgZFb-YH6Xyl8c216oA4sE1uJybytglmcXt8eeOk6TzHISQJmI37wRkkNQkTI28T3a3L3MBCAJX6Zj5A7UdQ13gdapJA-zSvUdzTfKajIUdus7A9u4SuKieQWjntkPaYBDFsu9FANlErs94y82moBV-nNE6H260qvko28dwUkpeInQHVc0uM31uu7Mtggx2Eg0-RjNIPnexU_tvRiQXLQ2hM4avmQD_QPJZixjXArHFMox19xsk5ZRWutoWdT0uCjQzVJ0rif8bm-U75oUBMSdrwXw-qVGq2RKXOwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فهرست بازی چادرملو و گل‌گهر برای تورنمنت سه جانبه آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/96802" target="_blank">📅 17:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96800">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsHiG6oVIKIDboJjDIgW5vIFEy5G-2dk8pF2hsTQQ5mfdqRlqeK-cc3b0ong8PrQQRUUvUIYI061mEc2B4VOKcT63LllGgfMu_C8qdWmTt14v3LJAMGOQi_LPDUqWY6Z4iYPQu7x4cZ3IR1gV7m3anaRtF6qjEtCpMEdQ0jUuOYNNUek24_A4Qc8imO6aEbEL98I7oZTg_SM_dYwwBEhjgV6QL-tORIKqRZATfMIg1mi8k_c4SlndPmpIF7guyMtObqj-f6odxsDEv-v1SMg5d-QOkR7dGM2NeO9BtaACpxPZKfMGtnO2BXAtGbMCbJmROeSSqwZGHfNRh47W-yDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RR0eDdW14EmNxQ4u4dq3h9x6bNICu0S0pNmDZQ2bygVRQi6oE-lJAdLOlRk94GRNSZjhSibLTsDvPZoJoa0jIGlEm-BplGirAcSmAsHjRbYzVQJlnK4F4rdZsoyMjwtM2Ozg2T4bmUf-tqjhGkQzjBCZ_cUzexrIBMIwlu8szkKFL7jlYSfaq-2dvfbiOnypsoJSEP_6c9Yf3vdt_hLd5RRi0VLKgmnA2REXA599uosjUItt0D6I8Lqi1GmgfO-6TrcoLcrdCsRGmQmUPKbSBS11-gYOYmsfSk3YTLzg0PJB0PankXurP3ld1cNozmw3tUvdMP9Khb1x2VBbLGjg1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🆚
🇯🇵
🗓️
۸ تیر
⏰
۲۰:۳۰
برزیل
🆚
ژاپن
📌
برزیل مدعی قهرمانی یا شگفتی سامورایی‌ها؟
⚽
🔥
برزیلِ صدرنشین برای ادامه مسیر قهرمانی به میدان می‌آید، اما ژاپنِ جنگنده با امید خلق یک شگفتی بزرگ وارد این جدال شده است.
👀
🚀
⚡️
آیا برزیل مقتدرانه صعود می‌کند یا ژاپن همه را غافلگیر خواهد کرد؟
🔝
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
🚀
پوشش کامل بازی را در بتگرام دنبال کنید.
👉
🌐
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/96800" target="_blank">📅 17:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96799">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvoCPz2mFKgq-f09_CwXhKTOcJyXKtY34dnC9iREzqi4cC9Iy2nKEyn1WKb3Narnqci6GTajncO1DoPZ_o4K9HxxF4jHB_hP_vcNc-JOf7QP1WDyvEqZL4Qc8hAXS0wAE8LYbdpySPmRKQmzhWQql494M0KXAKjd6C180x1CsqE0TJQvuH9a_rkQ6Awza0qFpVV603DrOPeRgz75WwM7UKcGAXpz6F4dsWYfwbZwuF8z2uVQ1NVLFDKHvWlBqj4Ao9b-wq_qFlWpIf2Wd2rRPBDap-8W6ys9z70KZWwQzPBlvoalvudut-wgqv41qorGgTnAvSSO18M6kLgIAIXC-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
فکت؛
فقط مسی، وینیسیوس و صیباری موفق به گلزنی تو تمام بازی های گروهی شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/96799" target="_blank">📅 17:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96798">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🔵
با اعلام رسمی باشگاه منچسترسیتی انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی این تیم انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/96798" target="_blank">📅 17:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96797">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tssNhQdO_uKNeH3pFWXpxN-fvPjhP0u73-MRzIyx0Kh2nvvY01YGbHcnM6AnUbM7LvKNn_XG1JEEkCaTEDPHIB3v4K_BsBgdOJaA_-6K6sBLzwAhqxbQ5l5wUFgXqcBhDXjnLE7Kp7GyOuhfeNIBptXTrDBvzm-i9RVacT1DzEaXNDC7rvJMqrok-xcLZcu4dcVC1mw4-XCtqQBQsLUzfsTkKM6hBY0PBIcBeeGfI86oe0F6idRSmqPbmN7SJZb-8609goR2ZlNYnoVsqSKgTiOIpTxvu6FPVn1L-KQD10kCnc_LNJoA45EkkkR-OktEP8RzDehxoyDdhlc6t0r9rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
🤯
پشمامممممممممم
🇪🇸
‼️
رسوایی بزرگی درباره بازیکن اتلتیکو مادرید، متئو روجرری، امروز صبح فاش شد، پس از آنکه زنی پیام‌های خصوصی که او از طریق اینستاگرام برایش فرستاده بود را منتشر کرد.  طبق آنچه منتشر شده، متئو روجری به ازای هر پیام صوتی با محتوای جنسی که…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/96797" target="_blank">📅 17:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96796">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6c4d178e.mp4?token=BTRpaAYfmkQVgQsNk4z8rAX0BgDRpl0TKrk7-BeiRZxCJMgQU4rkbpKVj10OliDdgWUfJbEfdj5U_v3t3vxnFEih2MVLnTA7AdL3RyxO5gbb5ivd_agcQ2gb_TfJRwX4oUDaXNQszw_oPjt9b24d9Giu3eCZ7d8Dx-xiaOzGnPHSBBIkeQM9Vpa0P8AEL3rNL46-XfQnwpafj2KrlYG0sIAKoS4BIv2_jyiPn75ssQfLiYw4oeF3QhlkqdLBNXxbtAACnN5jX4FmtKkz_5jXVwRhOGvVVCtmRK3sLKXmUHFJOz1Q6M_3qbh83qgkDfOMN2h5sAc02HoY6ZET-jZiwmS8VJcSOHrEWFbq8ephrCHLk6_tTPK-0hnmRGmxFIwulzT6cEYs_TuNltgSHmuE-vDMVxBDMO6JRGCSRQmZ7peCQ4yLObaSsb_FZV1TL6e7wZbEaI8sjMZiM5Ehl1GW653u0MuxrKp7KAFC0ZLgBmvey1MP7kJaSjPr6i75dNzPqhNhTgzpatJll9NMvabdAv84YajdpyalhTSoNb0wRvUn5GeyaqoXznXJZgO0OyUfv4xHXBgXQzOFC1BeaRMt4T7G9MrU5pTS7NGUinsmAYvhXSxwtHVg1lBFVy0_2Td9Ndu7gRoOk15wD9xT3SuudhK8qRCC-s_T8jm6ppuPajY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6c4d178e.mp4?token=BTRpaAYfmkQVgQsNk4z8rAX0BgDRpl0TKrk7-BeiRZxCJMgQU4rkbpKVj10OliDdgWUfJbEfdj5U_v3t3vxnFEih2MVLnTA7AdL3RyxO5gbb5ivd_agcQ2gb_TfJRwX4oUDaXNQszw_oPjt9b24d9Giu3eCZ7d8Dx-xiaOzGnPHSBBIkeQM9Vpa0P8AEL3rNL46-XfQnwpafj2KrlYG0sIAKoS4BIv2_jyiPn75ssQfLiYw4oeF3QhlkqdLBNXxbtAACnN5jX4FmtKkz_5jXVwRhOGvVVCtmRK3sLKXmUHFJOz1Q6M_3qbh83qgkDfOMN2h5sAc02HoY6ZET-jZiwmS8VJcSOHrEWFbq8ephrCHLk6_tTPK-0hnmRGmxFIwulzT6cEYs_TuNltgSHmuE-vDMVxBDMO6JRGCSRQmZ7peCQ4yLObaSsb_FZV1TL6e7wZbEaI8sjMZiM5Ehl1GW653u0MuxrKp7KAFC0ZLgBmvey1MP7kJaSjPr6i75dNzPqhNhTgzpatJll9NMvabdAv84YajdpyalhTSoNb0wRvUn5GeyaqoXznXJZgO0OyUfv4xHXBgXQzOFC1BeaRMt4T7G9MrU5pTS7NGUinsmAYvhXSxwtHVg1lBFVy0_2Td9Ndu7gRoOk15wD9xT3SuudhK8qRCC-s_T8jm6ppuPajY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
😁
ایران صعود میکرد اگه اینجوری میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/96796" target="_blank">📅 16:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96795">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1AhL37Ytk2Vaf9P6804uPsgZeOxEbzEa0OFzgf0gdWAd0Kd49oIFB-J0Vbgf4oGEjQim0PdFCBPCteafriFvohYzBMQH8OWCa88EPx8aEOyHsFGFOEgIoQEx9X5GzKdPGKplARP8Xcg0Dy2E9pg8oKcs7yJ9UwmDnAlCFejEISqZh7ZccZGojIaz2ar7FsbXEBxojD8aoFZYRghlN8OXjpVt5gicVu94Sy2-aXf3xQ0C_Bb30imF7LgoLgyb9yqm5Yxu9OK5O9PRBrNF20Q6ytg2txfgmy1h9JP7Ci9jVqsom5sy1M_Oewd6hZPTb4GrISpKZezwXTUI5g4sW5uXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
با اعلام رسمی باشگاه منچسترسیتی انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی این تیم انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/96795" target="_blank">📅 16:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96794">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJaSARYekr9dHpU7Cj_yesCIB6vgIcUfuwYBLEWuAfXrEIxSjMSNRAy2R52IO5nGxYCY3FhED692nxQedc3OyHU-qgS9_iabOmXXaODj44aqTUD0rFmPh8SQ1GQtBc_Wa8Hw0TIriqn0IsWpIOzg58uD0wX2HQWA-E99LIvi-akGQmXRNyopacvxlZM1Jrnlu704ZaRhnoEwdhhH7z9Th8H_SAnD9Sh6xQzJ9DfNiVwptkBZ0qHdUWsLwSCe7DES3jdhURXRq5NmRL5Va65AGwVxWVlbxPpwQwUPCgGr_EdDR5q68Ttrn2g7FFrLI7cAcQNhsJ1p4r4sc_C_gxANcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇦🇷
لئاندرو پاردس و همسرش در بازی با اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/96794" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96793">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09f8bd84ff.mp4?token=HSKKo7oA5LUDtksbog5lpAnwzZwymq__eDRLyCg79xByYyL-KSXnDeMy4MovTzGWIxoLFH79IjdqkIpFh8Tiup89-KtDsCC8wtQCwyHakpZ5w0lUFicNW79R5Sm3ioFe_kYU3XpG1PztAO9Dpvpw7oxen_NOqDs1kS1gRErEPjwzKPvKTrHtuazCxrS29hZv4wv9e-skF2dsOZPxHCA9lOdBfIiuHBL3PGItTxuwtAKiGHLm9k7tbI4ZNUWFyLp4WK3W93rYTjiUWg5Pa2c9mlndP7fmaTmqE2OswZjUMz8tKtJeashSoC8DM7589H3w6srKin-XqXmi8zDgU9PvxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09f8bd84ff.mp4?token=HSKKo7oA5LUDtksbog5lpAnwzZwymq__eDRLyCg79xByYyL-KSXnDeMy4MovTzGWIxoLFH79IjdqkIpFh8Tiup89-KtDsCC8wtQCwyHakpZ5w0lUFicNW79R5Sm3ioFe_kYU3XpG1PztAO9Dpvpw7oxen_NOqDs1kS1gRErEPjwzKPvKTrHtuazCxrS29hZv4wv9e-skF2dsOZPxHCA9lOdBfIiuHBL3PGItTxuwtAKiGHLm9k7tbI4ZNUWFyLp4WK3W93rYTjiUWg5Pa2c9mlndP7fmaTmqE2OswZjUMz8tKtJeashSoC8DM7589H3w6srKin-XqXmi8zDgU9PvxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
🙂
این‌خانم نروژی بدلیل شباهت زیاد هالند سوژه محافل ورزشی اروپایی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/96793" target="_blank">📅 16:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96792">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29b044b968.mp4?token=TimtS37Y_VoijhKwR-dI9iuyxIF8zd3gMc9iwPacTtMkYjj5YdTwqqGg2U-q4MLbISd7ecsVjt7rAGINzSKDpAY0H8VD6l5RnVA5UE1JXD1EuUahkitZRwmvyLJP4GGJ3PZbeCOayVE_n6_1YpfRO1jNCE9HIKLUwsPFJPUWW9xk2xzRB-TN-Ov_WfuQE-GhByVP_onYIIiilONlAmxe135MyOD0UWcBB1gy5SLMRQ_42ofxUDSZ2rAARrSGRv34xhEnh42OUbRZiRwAuHnl1-mLEK5-WpHYB8LsbvWBayUxbyGHrsP1c1RUBguPJZ5uUo1uFY-cY6GQForYiGvZFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29b044b968.mp4?token=TimtS37Y_VoijhKwR-dI9iuyxIF8zd3gMc9iwPacTtMkYjj5YdTwqqGg2U-q4MLbISd7ecsVjt7rAGINzSKDpAY0H8VD6l5RnVA5UE1JXD1EuUahkitZRwmvyLJP4GGJ3PZbeCOayVE_n6_1YpfRO1jNCE9HIKLUwsPFJPUWW9xk2xzRB-TN-Ov_WfuQE-GhByVP_onYIIiilONlAmxe135MyOD0UWcBB1gy5SLMRQ_42ofxUDSZ2rAARrSGRv34xhEnh42OUbRZiRwAuHnl1-mLEK5-WpHYB8LsbvWBayUxbyGHrsP1c1RUBguPJZ5uUo1uFY-cY6GQForYiGvZFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مود پسرها در آخرین روز مدرسه، بعد از اینکه کل سال از اون متنفر بودند:
🔺
دقیقه‌های آخر زنگ آخر؛ زل میزنی به تخته، به نیمکت‌ها، به همون دیوارهایی که کل سال آرزوی فرار ازشون رو داشتی. یهو یه موج عجیبی از نوستالژی و دلتنگی میاد سراغت، با خودت میگی: «یعنی واقعا دلم واسه این روزا تنگ میشه؟»
🔺
اما این فاز سنگین و کلاسیک فقط تا دم در خروجی دوام داره! به محض اینکه زنگ می‌خوره و پات می‌رسه به بیرون مدرسه، انگار یه آدم دیگه میشی. کل اون غم الکی جاتو میده به جنون و آزادی مطلق! دیگه نه بیدار باشی هست و نه امتحانی..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/96792" target="_blank">📅 16:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96790">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYOIK2tUNdXxIOtoCuCpKvoqt7QzvPwXGqAZGhjNY-4p0Y2wIdi-zKJz4kJbo27mceJkVe-96zuvLmB-CDFMlpWvBksh9URHtRwaqVR2lXz1h7sdQrA3Bmy9e8BsQsldsb-wIWE-rm90FuTfZUSzc5gUHDr4FAw2SEdgozsP3rvKaWxqX1D3HmU5WHAFZHbVgCe2sYgPIvo6Z3U2bw4KDV6gTQWGfGHlqurmG7BahLrYNQmwCbas3dBL5OiIYgOscc07Ko7m4CIbmGD-v8QQdrV4XR6kLu9fm-Ox8X7g8kK8076NYHwwHoVBjTCzMude7YMODqToPWbilFocebkIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_lzqPqO_bdk712b1XooLX_SBYIlEiNeMYeqXX0OV5W0yiOJbvPXALhwg6O8wG_XWJ3IHnfFZZdVnJZmElbXuZfgyXALdbr7p3sAYW7Bkk-Mf-FgpW3j6BzX4SZwZN9GN8AyBSNe543eYloAokJejZcvYPLxv3dZsd2BJorbv3bCiXcWcx7rAtS_FmIN5SUuRlWCjcigXYDUEJRAYhQiv1U1KKYy2OMRSnr_2OJxGEoXF80gS70KFzpfJvTveQZL_tZ6V_Y00I7fWhBqwSRawgomAyhR2EHMYR5Us1t-ZL79ffVahfiAsHEYUNsO9FEcZwbRwLdPBCr29X88_kULOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🚨
⚪️
میگل سرانو:
مورینیو به کاماوینگا خواهد گفت که نقش بزرگی در تیم نخواهد داشت، و این مقدمه‌ای برای جدایی اوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/96790" target="_blank">📅 15:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96789">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SL4nwGnZ6Py6lECgbCSAq1Qrd6jg3vehnoHlnHaGiT1iY7hHliDRqmY4ejFAuf-ndE0c7Q0OGNRW7veDCyHGwVJTo3Kp7VcuMywdBrV7naxPKTQ8clh5zLIFw1EWC1LIYIuUpP_KPBjgNpOh3EuX2gKRs6HRN79ZnjLbZ_h4jKk2CGomIKv8U6u5uttsLcrxKKvdYF_gC-peqOvozWjThu-TVnMQsIlYyZW8KqvIfD4dwLOMHDRMpl0cwutrRBCehjFondEyw3HlKq3cD9KBDoBUZFrFGN68AFDqSgzvAsUbBNAWWzVonZOfdj80mejkcb779pwvfRg4uSg5wcPXMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اینستاگرام بازیکن های کلمبیا بعد بازی جلو پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96789" target="_blank">📅 15:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96787">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiU19C44Wdljgp9QLo25YNFCucPWZHthmVfI80n_q8OaI927nVroP-SaAkyOZe6RW-UCeQL8bXlnFdO878eCUQb7gxo8nPh8cymRjzZdxEtWun0uStCHjuBVgDM-vibZkSFcvgfYmW1-20C0OnRxTP3VaNgXjJ_6Uw7zRlC_ws14yp46xRFOVj6sToiwI-Mid9Q0imteQ_y-48UGjgrwEUJB-Noj_LcP4GWYJtY62_dam_g3BoNzPquVs6ONjU9sp2akQrsHd9ebPzgY4y5gQbIJ0Z-uYgOYFNY5-eWXt5Y6njjAj8qQIaxfq4DAbfk3Qy_5kF7xzohQlvqoUCvi7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
🇪🇬
سرمربی و بازیکنان مصر بعد بازی با ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/96787" target="_blank">📅 15:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96786">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c49365cc36.mp4?token=OdzqNjNO9Rpsr99tGvF2vUkN9Owkmdn_uKuPnqZZe8noK9eU_RmZTKUXRoGSWXcxHgP7s8ofUc9BxnjEuiA0_3PciWaxo2iwqPb-6rwL5XbjDDoxC4ik1lcLrbsInSctOx8qZqqGLnGEWBS-sqcpZf7TtQu5CCx6r_Ka5wBJS8ol7WUx75nHi4VUvpMk3MAbyL30KGFocBTMZHOUY7XX1fN3jyj3XYU7cMW4GwIO9NtaYMVC0hOrPjVie6IqDN6Bddo7JoBDLgmLMI4bOMJiOVWTyXSeZ_6ZcWnkn-mC43mr1YbLg3NOmNUeH9AFd3QxbfwzSnKYVy-A6qttZzC3GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c49365cc36.mp4?token=OdzqNjNO9Rpsr99tGvF2vUkN9Owkmdn_uKuPnqZZe8noK9eU_RmZTKUXRoGSWXcxHgP7s8ofUc9BxnjEuiA0_3PciWaxo2iwqPb-6rwL5XbjDDoxC4ik1lcLrbsInSctOx8qZqqGLnGEWBS-sqcpZf7TtQu5CCx6r_Ka5wBJS8ol7WUx75nHi4VUvpMk3MAbyL30KGFocBTMZHOUY7XX1fN3jyj3XYU7cMW4GwIO9NtaYMVC0hOrPjVie6IqDN6Bddo7JoBDLgmLMI4bOMJiOVWTyXSeZ_6ZcWnkn-mC43mr1YbLg3NOmNUeH9AFd3QxbfwzSnKYVy-A6qttZzC3GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی برزیل و ژاپن اگه به ضربات پنالتی کشیده بشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/96786" target="_blank">📅 15:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96785">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b94bb0e26.mp4?token=ICME5E6y0FLHB4tvjw39srW3jQxPlBerEvowdyAbp9iN3NWy7iTwuvbNtWteHtSbKFYUh8YfBZN_WB8px68apG4bOpmKPley61uLbVuv-j54Ugoll9F6ZjAfwS8nYKnHYq6w3x9B4OmXrDWWUwD15_0j-L0ngArPg4dGblrkkc1M0uH79OiXApqD3MVSTWMz7albrfHd0drnrgMGg-rIHEkwAZQToclAEIQdyxc0uWMHtXO_7PXoLee878WVm1Iw_mvT6F6zoWeQNgWeIku2JBAZtlu6pe3GShNUOn-AjTpFnEokkoifCTJhST4MRkow_vbAUHX-nqcomCWPSx-Mqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b94bb0e26.mp4?token=ICME5E6y0FLHB4tvjw39srW3jQxPlBerEvowdyAbp9iN3NWy7iTwuvbNtWteHtSbKFYUh8YfBZN_WB8px68apG4bOpmKPley61uLbVuv-j54Ugoll9F6ZjAfwS8nYKnHYq6w3x9B4OmXrDWWUwD15_0j-L0ngArPg4dGblrkkc1M0uH79OiXApqD3MVSTWMz7albrfHd0drnrgMGg-rIHEkwAZQToclAEIQdyxc0uWMHtXO_7PXoLee878WVm1Iw_mvT6F6zoWeQNgWeIku2JBAZtlu6pe3GShNUOn-AjTpFnEokkoifCTJhST4MRkow_vbAUHX-nqcomCWPSx-Mqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
واکنش ابوطالب‌حسینی به حذف از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/96785" target="_blank">📅 15:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96784">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0ATM-EVRQqIHhJxmvKw-qlitdvK7A2huwdtx5bCkuLZniwRV-TOqsaykC1hg7d6YgEQlCB86eGLhdgXdZapEqfcY4rij7O8HujJQ6yJ9umIb0T0BhJRWOsVYGfqNWdxrjPn3rtd-2qKtwq0hwEKaPnFuxXcG4fEqEKITnL1dHbqZ3VVR5gMj_5tmmhsuYjLqHMmj8LOJVSgKv1WLf9Xu_gLCo9CYlN_KxW4pp9-aS6bZSD2nX6mv3PenTOE3bc5pyDJTcicVTm8z89i-SyRgndPMal0k3DC274rvCgiP4EgWCI357RGQyd8Hn98acZfJ4CJxk8LtIpEXyDCpGg4bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بارسلونا فردا پیراهن خانگی خود برای فصل 2026/27 را معرفی خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/96784" target="_blank">📅 15:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96783">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuoQyXxUNzlWVSptVbfmWFHNevG9IhQPuCtRtwGA0fjRJQINbYghDZ1EhNRO4q8QN3fG9LU65sWxYMImoufaZZDJgNp4yUfRHFaQOsnir0VW6sFIgSP6sb_AJDBMW36zp23-fNN5gQmUQQse2yWR1KsZwsF6iIeefxsaKmCa4wN5LRvbDGJBx8feaIFbzz0NsaiTsF1ITtuAJr_baeHeHKxveSGFsBRtHH57n-dXOBy4RMXXqwjauwJqyOA1ss4fePJr4IeZtayqZAYGBIzZDwLdiM6uvFYXSb6lpQtkSfpV-MAeyz-ohNDhp-aW8cajXDCxzQ0Ulbbpyf-g89bCJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
الگوی فوتبالیت کیه؟
🎙
گاوی:
ایسکو و وراتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96783" target="_blank">📅 15:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96782">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96782" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96782" target="_blank">📅 15:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96781">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=dmnSkhkaTtIUCCZ021SvCUKWKUgzfNl5kMPr-h2J_KvhO7-M2mwjO017OKLsKe7qy63_KIUDibQ_nJLkNuzJu7HQChyWwCPStCzXy_t6gBnQb2wVtKBr1EuFE8yBhKEY_OtqPOXl805CJDScYNgTWm0jR4GDv8ndk-BWclgyocIQW6ySDumV443ss0bAnLHylmSBjOn1EFhVOEuLd9-8kCipipWUAhrWbueqoQwF0CmNXiSasJQGTcMQu9rW8tl-mb-gwSugKZcgtSHOYtAPNPye9z1aqvnoY8BJC70I4vOm6ZkMu9TEZZAC7AFnRDPpt2IceunudX45aXNb_YUwnp_YvSwH7QsSDkj_C6EJ339Sw-EYrh9iNhv2tIwM36Y8oriWKOAy9SqgQoHtWR5I9d-y305-ZpSGYeQ6iy1PaVRnOwRuYA2WBU6zzm1XrOlulMLae_5WHs3P8eCn_stugC1wsgjyB3dLKVbRIy4KJbfSOYsuEVgVzEvRHFmiuAnclfTolkTsCEb5jud2NVzv3AYV0xJa0EnnWHEM4NEanBd0iiQGWCx37AxqDjjN-hnUK4PlbAcONb9djX0bUzRgW7PmyvTrNai4k8dplJpdIzJmH5ldVe4iJmrv_g8esyAQpukuNfh-oZwrNxUBbls1Qr7lWz6VuAvghPku0UF4U-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=dmnSkhkaTtIUCCZ021SvCUKWKUgzfNl5kMPr-h2J_KvhO7-M2mwjO017OKLsKe7qy63_KIUDibQ_nJLkNuzJu7HQChyWwCPStCzXy_t6gBnQb2wVtKBr1EuFE8yBhKEY_OtqPOXl805CJDScYNgTWm0jR4GDv8ndk-BWclgyocIQW6ySDumV443ss0bAnLHylmSBjOn1EFhVOEuLd9-8kCipipWUAhrWbueqoQwF0CmNXiSasJQGTcMQu9rW8tl-mb-gwSugKZcgtSHOYtAPNPye9z1aqvnoY8BJC70I4vOm6ZkMu9TEZZAC7AFnRDPpt2IceunudX45aXNb_YUwnp_YvSwH7QsSDkj_C6EJ339Sw-EYrh9iNhv2tIwM36Y8oriWKOAy9SqgQoHtWR5I9d-y305-ZpSGYeQ6iy1PaVRnOwRuYA2WBU6zzm1XrOlulMLae_5WHs3P8eCn_stugC1wsgjyB3dLKVbRIy4KJbfSOYsuEVgVzEvRHFmiuAnclfTolkTsCEb5jud2NVzv3AYV0xJa0EnnWHEM4NEanBd0iiQGWCx37AxqDjjN-hnUK4PlbAcONb9djX0bUzRgW7PmyvTrNai4k8dplJpdIzJmH5ldVe4iJmrv_g8esyAQpukuNfh-oZwrNxUBbls1Qr7lWz6VuAvghPku0UF4U-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/96781" target="_blank">📅 15:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96780">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b31d932a.mp4?token=o3VNBc6lH7mt5M8nbk1YPjSxq9hwzYzGNDdBsfEt6CPlDuRKaplwkWgnXnPYww7ewSLCAaVH9lE-KCHZTl9jMlGOja0LGae66QhQLZRcuuteWX2WiRE15DDruaWnznObPlEMrsslLNO-m3FkF3VyRsqKiTlACNuGZoam1plxq3uZo9_rKIXJUiuz3A7rcRe5YDaFRPsENSWvovE86nq1FlpWd9Ro7iY_veCinbV_4JCxwq61cvWIA3k7YM3NoXNSdmiYRxXiBagGdS2NYNeALTHnsmsk1SwmEZcal1mQsv_kuw9490qrNPBFAOxZRXfd_VA5EM4v-yn0uWCIMHFLVYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b31d932a.mp4?token=o3VNBc6lH7mt5M8nbk1YPjSxq9hwzYzGNDdBsfEt6CPlDuRKaplwkWgnXnPYww7ewSLCAaVH9lE-KCHZTl9jMlGOja0LGae66QhQLZRcuuteWX2WiRE15DDruaWnznObPlEMrsslLNO-m3FkF3VyRsqKiTlACNuGZoam1plxq3uZo9_rKIXJUiuz3A7rcRe5YDaFRPsENSWvovE86nq1FlpWd9Ro7iY_veCinbV_4JCxwq61cvWIA3k7YM3NoXNSdmiYRxXiBagGdS2NYNeALTHnsmsk1SwmEZcal1mQsv_kuw9490qrNPBFAOxZRXfd_VA5EM4v-yn0uWCIMHFLVYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
مجریان تراز صداوسیما و ورزش ایران که هرچقدر از بی‌عقلی و عقب‌ماندگیشان صحبت شود، کم و کم و کم است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/96780" target="_blank">📅 14:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96779">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEFBKV-oepJWc1XGLe91-HBD-28nNWJ4qMr2Xe19LHkUkXLI-tDLv0QzpRAvaXYGen5jyhU2ZC3igj04XI5F2QfjwW3PP_plQpQgaJ6Op0S5TxNr8SGnluZAJ_1l-5K0bKPsbyuOWsX-XXaOOQWJF6FVcYEWI62ap7YR8kFXQ3avtNGDlY13J7anGJ1JkTc_kE5QZGX0yTJi4UcUPyzmhouuO-ZT06ZCwSG7DncUsCDSCD-BsW9TIbYBflYC6YcF7PQvwWl0YWa7dwqTyaKSdSM_LNgKVwt45drESDaRymHQSkJZRuXHfd0gBeB7HdzOt40bWl5S4t6IPbIb3aw61g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇯🇵
هاجیمه موریاسو سرمربی ژاپن:
رویای ما قهرمانی در جام جهانیه و ما اومدیم که دنیا رو شگفت زده کنیم، درسته که برزیل تیم قدرتمندیه اما ما هم تیم کوچکی نیستیم و برای پیروزی به زمین میریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/96779" target="_blank">📅 14:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96778">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gflA5UmF6TNmBnoWrPf4vGoWOik9vV49jtjuRJ8LmW7DUaIOBbVd_a5PdqZyCDT1skXmwhX1mWv25fAXM6YNKmE6J7qNCfhBL7MBcXa1t6O5Di9ZB5u_-xH641C72tOuYlgF9yqogIzT3B5xWqWMsbNYPIeYGvs0Syp8e1pug5TX-c4tJReJf7uBGnW3-HGN9exaPhTMk70es_MZyFTL5zllqXCbxTQc65LH-OgzLeW--MuFxitqt18TaEZGHAKCtu8cRPasKN8-OnOZ81_J58sNceGqIQe7SZsbHD7LRwfJyqIIBaZ2ZyGkcteP2qMvW38MIy2lq3p3PmLDjMeAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
اسپورت:
بارسلونا قصد جذب هری کین رو داشته ولی طی روزهای گذشته پس از پرس و جو متوجه شده که این بازیکن از موندن تو بایرن راضیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/96778" target="_blank">📅 14:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96777">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_KS1ZyoFTJ0B-Zqj2q1hFpt9x4tSxe-BIn4A_fFto07HZDWbtLIG_1BKXndjce0c3uoqgik69IHVyMZUyZ_HT3MEa3OcqqhVjkvSvEW7SPWZFzlo7bgMZ-XdZVIj7-8WKkU56Ssbo9LmMUzZ-VdA8ctPhrNWdcHIjbvfrDoPJ-avKLB1JicKLEKVAMjPCvx2mee1YK4g-ADpTJHFF2v8fO_fq_B7yNr4lgFJPR4wIsJmYXCDXjJZV88Vyel0mZgc4qJTgNhNhJkkoqI9k7DlOEt4qIz6bZZF12pkHbJGr6bluASFqAmMVCNu8MYDVqqnqJLi194B3ll7doP-L1NWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
اسکالونی و فدراسیون فوتبال آرژانتین به توافق شفاهی برای تمدید قرارداد تا سال ۲۰۳۱ رسیدن.
🤝
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/96777" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96776">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61f63773e9.mp4?token=DG840Bv_vzn6SEwVMQ7McT_FSMZipIm7DCgcTMPa0Ot_CbHDfMlt32hbu3k06vqalHYLKbP8AMNCop_xQ2UIWjAXFz8zDIaeL0Jbb0RGN1cWKqdojHbxmLcS5MhEYf7cIfudpbShPRTd9O92wBFSIutJWd_80W7X_b1fxV-AU2Wz7eKTzI2004FsdoWoMKSdbDBcQUwpt4ha_f5xq0Pk2DuxgTogIBeDdzslwz_dYvu6ysByApGa2Eu6J-OJtlWr_Z4iIurNLxJWUMyaoxVcsLO9ssNtg4JrbhctGab33wF1Bg9BeLzvaxJKyldgQmeKNE3quIC538HIXCfAoPE3-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61f63773e9.mp4?token=DG840Bv_vzn6SEwVMQ7McT_FSMZipIm7DCgcTMPa0Ot_CbHDfMlt32hbu3k06vqalHYLKbP8AMNCop_xQ2UIWjAXFz8zDIaeL0Jbb0RGN1cWKqdojHbxmLcS5MhEYf7cIfudpbShPRTd9O92wBFSIutJWd_80W7X_b1fxV-AU2Wz7eKTzI2004FsdoWoMKSdbDBcQUwpt4ha_f5xq0Pk2DuxgTogIBeDdzslwz_dYvu6ysByApGa2Eu6J-OJtlWr_Z4iIurNLxJWUMyaoxVcsLO9ssNtg4JrbhctGab33wF1Bg9BeLzvaxJKyldgQmeKNE3quIC538HIXCfAoPE3-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🏆
ایران کی حذف شدیم؟ دیروز یا مدت‌ها قبل؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/96776" target="_blank">📅 14:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96775">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNFJ5F4sah400o1xy5hpZIuJoKEa_-oNF6Z90iGhNytZ77sXhkaHIsDu0gSdymfXL86l6lo3iwztC4I6jCyPt-TRxBsdg53vvliHAlBk1I19w95X-ekjbgPr_QfTLPM4Zu04NObqXh6TU9qN3r3u5qQGCTlYUzAdcna_sRz1ouhgliiB97dYfd07AT7p_IuweQv23JlNhxG-3QgpYw2jlgZirWOMX2ZHP21TFpO4Uy3pJkvt8cxNa0MX3Tc_GdQKRAQWFbNXX-rxJuDVuGX8QxcyRqo_rVKhNiydEGwElArCN94KFJbHpIf5EdLsb-p7XTaxDJv5z0ZAR4Nag9Cxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وینیسیوس جونیور:
من به تلاش خود برای مبارزه با نژادپرستی ادامه خواهم داد، تا نسل آینده مجبور به تحمل آن نباشد. من به دفاع از همه افراد سیاه‌پوستی که صحنه یا صدایی مانند من ندارند، ادامه خواهم داد.
✊🏿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/96775" target="_blank">📅 14:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96774">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🎙
🏆
صحبت‌های تند مرزبان مربی سابق سپاهان خطاب به امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/96774" target="_blank">📅 14:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96773">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc903827da.mp4?token=alB16T0SkyD4ehMMQP3c4CEm0wcrhFtxxdKTqa-08WUf10qL1r7QYd49kcgNvXNx4Ol23wzeQRKZyB6BQQTN3ktxKx-t-oYh4MzO56gnG-TB3wK_V_VeKSxFeeVuscXEQNkQeWKWlH-oXjqXgqXdwxReWuc7ul9VnoBLMyNNdWYA0ynBkdIgotO6XcnxwZYqpIILaedTiLjB7JvtMXa87bo81R28db-1e3mOaD4vJtg0yEGneVwgmp97G3act25T9fSXAWGHUSJJXr66QqNveKVv93-IEbqyNZw-JCLIQ3TIE4ztrVKkJkw0e2AiyZb1fo-Lkb89QvqR7ElraJw11Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc903827da.mp4?token=alB16T0SkyD4ehMMQP3c4CEm0wcrhFtxxdKTqa-08WUf10qL1r7QYd49kcgNvXNx4Ol23wzeQRKZyB6BQQTN3ktxKx-t-oYh4MzO56gnG-TB3wK_V_VeKSxFeeVuscXEQNkQeWKWlH-oXjqXgqXdwxReWuc7ul9VnoBLMyNNdWYA0ynBkdIgotO6XcnxwZYqpIILaedTiLjB7JvtMXa87bo81R28db-1e3mOaD4vJtg0yEGneVwgmp97G3act25T9fSXAWGHUSJJXr66QqNveKVv93-IEbqyNZw-JCLIQ3TIE4ztrVKkJkw0e2AiyZb1fo-Lkb89QvqR7ElraJw11Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمشید خیابانی: الکی از قلعه‌نویی حمایت نکنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/96773" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96772">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d99a4b228.mp4?token=Y0e3vaUXtiYozwJ2qoH5vHKpBSZ9AA-ZWGVFqM0bX4S2p74WG05NH68zt7GUfDFJziQKHS0wHVoxhofbOZxu9QC32nPImea0Y3HUbcOnSlhJxQRryXM-zPfE2DJkcQw5UojsnnuO69C52-KIfQhWrgIykYqP5a9F4NuEYltPfhzuFVBtPPp3SsnzZUCaDDnV0BiRrm_i_7w03p7AZuGEBH85g0yrMNjAdgEhCPA-ElSzov45A8NkBbN3bnw8K44-42N6uWhvPs4J0yi2AV7ClLGdqQYw9gx7oAvbVbrqhRjGG5sCN6iv2ozwWXVZqaBYEpDdDerTfvtNziC75i2cKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d99a4b228.mp4?token=Y0e3vaUXtiYozwJ2qoH5vHKpBSZ9AA-ZWGVFqM0bX4S2p74WG05NH68zt7GUfDFJziQKHS0wHVoxhofbOZxu9QC32nPImea0Y3HUbcOnSlhJxQRryXM-zPfE2DJkcQw5UojsnnuO69C52-KIfQhWrgIykYqP5a9F4NuEYltPfhzuFVBtPPp3SsnzZUCaDDnV0BiRrm_i_7w03p7AZuGEBH85g0yrMNjAdgEhCPA-ElSzov45A8NkBbN3bnw8K44-42N6uWhvPs4J0yi2AV7ClLGdqQYw9gx7oAvbVbrqhRjGG5sCN6iv2ozwWXVZqaBYEpDdDerTfvtNziC75i2cKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
آخرین تصاویر از سد کرج که سال قبل همین موقع ۴۰ درصد ظرفیت‌ش پر شده بود اما امروز نزدیک به ۹۰ درصد از این سد پر شده تا اندکی از مشکلات قطعی آب تابستون مردم این مناطق کمتر بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/96772" target="_blank">📅 13:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96771">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb782b722.mp4?token=ZMpYFrnqNITHGuRuol_Y9rjTEZZYudDM1-u0WvbSuf2Nxg_pelZKhNcVmpliI1gY6AgyB6NJS4jTWVCwNeMmiS_OaecQAnWN-8dhuMfhEtbqh3CdDxFxhnTO7QyXadctWU8Si7oeoJjSX5D-xnEAbDaADRWBOpbRWH1SK8C49wTsZQwrSCSQ5MttoWV1r5wO8a65OgGLe7q96yUqnltZjlbaKEFFY7JnnPcBFQB2PpJ-d9WsMPuk7hwZxnA7gLNdpaVRY6OVNzJWKoOTXFhn6PkQvQuQnuw0UYaqZV2rCJDCAT52pmXjoxUfDzB2XRF-inFJ8Bq-eL24hQvGiQ3I6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb782b722.mp4?token=ZMpYFrnqNITHGuRuol_Y9rjTEZZYudDM1-u0WvbSuf2Nxg_pelZKhNcVmpliI1gY6AgyB6NJS4jTWVCwNeMmiS_OaecQAnWN-8dhuMfhEtbqh3CdDxFxhnTO7QyXadctWU8Si7oeoJjSX5D-xnEAbDaADRWBOpbRWH1SK8C49wTsZQwrSCSQ5MttoWV1r5wO8a65OgGLe7q96yUqnltZjlbaKEFFY7JnnPcBFQB2PpJ-d9WsMPuk7hwZxnA7gLNdpaVRY6OVNzJWKoOTXFhn6PkQvQuQnuw0UYaqZV2rCJDCAT52pmXjoxUfDzB2XRF-inFJ8Bq-eL24hQvGiQ3I6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏆
وعده‌هایی که عملی نشد؛ از تعطیلی یک هفته ای کشور تا گرفتن بیش از ۴ امتیاز در جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/96771" target="_blank">📅 13:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96770">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWMIaBfGowNcvDV8NM3k6SAs_jOSIELAxKjI5JeFah3WNj41I7_fyXDEIfGq1jSze8KsLcOyuE4vTaOd4d3SUqMBuUDlXOAMjyodieQ11BIEbaozk34lol1AcJlS3zlB4jjM67LEui6fMKm99YV5hj8NC_vZvNV3GWyBMgHTD6m6Buq0WQu-RwPJT68SYuvMd5Xe8Uf_FsI5Y-oE11J2euL4TSxUT6VGKqQbYiOhBleImP2_sHebmNC81wCxYcvL7VfQlPa8CdEXOgP6A-aJpEBApsjmx0znkGBVhgDNqL96mOHaGgODkI7k2RrNB1nqom7bJv1s7y5_mN2B0z3Hxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری | آاس:
مورینیو از مدیران رئال مادرید خواسته یک مهاجم نوک کلاسیک شبیه خوسلو که در محوطه جریمه تمام‌کننده باشد جذب کنند، هرچند این انتقال فعلا اولویت باشگاه نیست. این موضوع می‌تواند شانس گونزالو را برای ماندن در رئال و ایفای همین نقش بیشتر کند؛ در حالی که پیش از این به جدایی نزدیک بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/96770" target="_blank">📅 13:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96769">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzkDfCD2DG0ZFOzF0tVqHlyFNncHexs-tiFXEnUkQeixMSue8-nNbRX45cKIv4qISgWntC3HqDLYKOhuQleYSt_DOpci_3rBQkMYeJd7JmYgo50HVLqANio8RwV8c8FdE5ozzgvfT0pB3pv0v525TUNBZCuLfM0KfgBaQaj7YdPGelWpYT1vHCIz_pmWa9vhmKNCJUrNJgzjDXPDO0g64HG634G7HCah9W-ygu9RB-1MtU1fceJR4ywsmY4p1jHZfRqvKpY0AvTWvqfGsA2zzsFOu8hJfsajy6mGdZazdf_CbNIWpzFgpjtVEcuxjeydLrcMdFcw3WU9DzzlCEKVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
آمار دنیس اکرت درگاهی در جام جهانی:
💥
نیم ساعت دویدن نرم کنار زمین
💥
حرکات کششی
💥
تشویق دادن و روحیه به بازیکنان داخل زمین
💥
یادگیری دست‌کم ۱۰۰ لغت فارسی
🔥
🔥
💥
نوشیدن حداقل ۱۵ آب معدنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/96769" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96768">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKgNfosT1sbtdPfuJIHRjRfoDnIe3BTsqXvnx6oL9LHTS0I4znh4bY3U2wczfjg8oX7egixZan1efzH6NZ9D_tAMbgYvMUMtqQ2faOigUjUT4iyDn4SxQYj_C-R8anpzlmI50MQo6pOuno3LZsC8kYWdYcWyn_g9S3dm0m1wMx3ufdhHw6AjJC_Nq5r0WwgGcU3p6W-ZATCieyeqVv3HeES_TCAbf61zPWLSKOj-nb1LU_vrHJ5ry28UWFOQdiN_9CJbScYvXm_BRFydt3muPgtdTPfWJDeb1pRILOqA1PyepK4T3pT3QuEycQDxXJnnkABUBtlo09iTaBGo5B29vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛
موندو دپورتیوو: لیورپول به کاماوینگا علاقه‌مند است و با رئال مادرید تماس گرفته است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/96768" target="_blank">📅 13:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96767">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
‼️
🇰🇷
پرتاب تخم مرغ به سمت بازیکنان کره جنوبی بعد از بازگشت از جام جهانی
روسیه در سال ۲۰۱۸؛ ظاهرا در سئول مردم تدارک دیدن که طی روزهای آینده و با بازگشت از مکزیک، رفتاری مشابه هشت سال قبل با کشور خود بدلیل عملکرد ضعیف در جام‌جهانی داشته باشند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96767" target="_blank">📅 13:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96766">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e142b950f.mp4?token=aGsU7ySlNtUj8ia7l1iVfFoooegaWKdUIXze8OIbwJ8qVs-fbCKz_eNm506vhy4OCetRNgJ0eUv1CLIASK14KQdx19btN5WydO1ybZkRWT5ZByl5NiIdmCPFdBeWoqvIbM9wzE7pGbWX-WlJE7TFOF86ybnNd1ZwyRKwo5G1pw_QnezIPcclMYAf4h6-V7tIIu9ZKcOqtWwPmMyKLHw2Gi04jmEIihtwrK913IkCEFpNdWNAB7M4ETkDxH6ZzcubcYPxKYymXZhla2rJYOTv7IOic3FSc1jPTdaXAgho-lF5J5ffT_h6X08H1HoCvzeG_bl0EoFcjpVKmq0CPpgkxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e142b950f.mp4?token=aGsU7ySlNtUj8ia7l1iVfFoooegaWKdUIXze8OIbwJ8qVs-fbCKz_eNm506vhy4OCetRNgJ0eUv1CLIASK14KQdx19btN5WydO1ybZkRWT5ZByl5NiIdmCPFdBeWoqvIbM9wzE7pGbWX-WlJE7TFOF86ybnNd1ZwyRKwo5G1pw_QnezIPcclMYAf4h6-V7tIIu9ZKcOqtWwPmMyKLHw2Gi04jmEIihtwrK913IkCEFpNdWNAB7M4ETkDxH6ZzcubcYPxKYymXZhla2rJYOTv7IOic3FSc1jPTdaXAgho-lF5J5ffT_h6X08H1HoCvzeG_bl0EoFcjpVKmq0CPpgkxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظاتی از بازی ایران و مصر و وقت‌تلفی گلر تراز تیم‌ملی آقای علیرضا بیرانوند؛ بابت حذف شدن اینا اصلا ناراحت نباشید چون میخواستن حذف بشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/96766" target="_blank">📅 13:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96765">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/az1ISDSH6uX2IKpGlultECGXXSynhhQSnjLQgdoEEd2Fvp9acBgdeU1RPWO7Avbne9vZZxtWyo5KRfYrRb4X6CFL9cpsAzCHYBQ3S65c4FHuM0aD5i4kUmZO6GyLt2-tbfe0xKEgWJjXg8HYlQyqhMTbPf3OYRXA67AL2tkAz0gYgNUEAifGmt-a3uVE64TiIJej7LM_-VOPs0ngo_i9uqRXgvqpRY3Zro8KWntk14eOt_qqDztkF-oIY8i6q8RPFGmThI1kZuT4CKKqjp3yyrgQZdiyHdHmHUViqsRAye5_oCPBQ2oelc3iw1YmWSa-GX8TkEglWAPuRALTQ7kMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
فابریتزیو رومانو
:
ترشتگن با انتقال به آژاکس مخالفتی نداره و حتی مذاکراتش با این باشگاه هم به مراحل خوبی رسیده.
بارسلونا و آژاکس هم در حال مذاکره‌ان تا این انتقال فعلاً به صورت قرضی انجام بشه.
تنها چیزی که هنوز روش توافق نکردن، اینه که چه مقدار از حقوق ترشتگن رو آژاکس بده و چه مقدارش رو بارسلونا پرداخت کنه. فعلاً گره اصلیه انتقال همین مسئله حقوق بازیکنه.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96765" target="_blank">📅 12:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96764">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a762bac2b9.mp4?token=hE1fQtY1wPfUqBdLeCvWB1ieJSruxt8b4zDLvrQC7Elq7MUn-9lclLqsJOnuCjRO7B_Skl7pAlwFNqyrN9ZudhlhxaW8V-CFO8R06EKGC9Xr3_B_g2EYf4u-3Q6MISzCmQ5gEQjAd6DC6OHKmoKiqwvUIcnnQ9pqyuH7ipPLRNY0bG3PJwhe9H-IFYYj4qG8Nu0Cle1cvzIgO8A1lV1eVFSqQDLqJmqN4F8rSEJAEurIPpiQpakpXDegHp1VI8Ok8XyVyNKHYzbK_VI3n4k5uvOCJFwxDbaxQy8833S5I9Wy3OWMZxewX9iTdzj73J1PH9eQ8gCvRebnTpz2AdV8vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a762bac2b9.mp4?token=hE1fQtY1wPfUqBdLeCvWB1ieJSruxt8b4zDLvrQC7Elq7MUn-9lclLqsJOnuCjRO7B_Skl7pAlwFNqyrN9ZudhlhxaW8V-CFO8R06EKGC9Xr3_B_g2EYf4u-3Q6MISzCmQ5gEQjAd6DC6OHKmoKiqwvUIcnnQ9pqyuH7ipPLRNY0bG3PJwhe9H-IFYYj4qG8Nu0Cle1cvzIgO8A1lV1eVFSqQDLqJmqN4F8rSEJAEurIPpiQpakpXDegHp1VI8Ok8XyVyNKHYzbK_VI3n4k5uvOCJFwxDbaxQy8833S5I9Wy3OWMZxewX9iTdzj73J1PH9eQ8gCvRebnTpz2AdV8vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
انتقاد شدید خداداد عزیزی و جمشید خیابانی از حمایت محمد ربیعی از تیم‌ملی و سبک بازی ایران در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/96764" target="_blank">📅 12:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96763">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293cb5ce55.mp4?token=SKzlVDXIV0KTRqw5mnIsmp08Njwmgp5ywBVGc9BYxcq1XpV4t5x-mazDKkoo8OYdp9EhU8RQy1SyxmjHKbGOPhK3aYEXQ6Il9xPjnt5E1rCFqm0fLRSnqjPkj1XqteMXd48WtEk1SEPz6uTC6KcnOv0Oj1DnrSsvXULyR_2z67t1B2B2nhnkoRqkegbuViQlT7ixlC2ijB38_FVwo1dfdjYSVcac0EQD_ftvIFdWDM9VIbY6v9L6ipHKuHy2NgfIebmoUkdZBg9SqZZjMHGhTeouvyhry4cy3fGHDIvRd8zV_VuSTtu9z_ypvk7LANHCj_eIGTkq72dBagrpg8nnsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293cb5ce55.mp4?token=SKzlVDXIV0KTRqw5mnIsmp08Njwmgp5ywBVGc9BYxcq1XpV4t5x-mazDKkoo8OYdp9EhU8RQy1SyxmjHKbGOPhK3aYEXQ6Il9xPjnt5E1rCFqm0fLRSnqjPkj1XqteMXd48WtEk1SEPz6uTC6KcnOv0Oj1DnrSsvXULyR_2z67t1B2B2nhnkoRqkegbuViQlT7ixlC2ijB38_FVwo1dfdjYSVcac0EQD_ftvIFdWDM9VIbY6v9L6ipHKuHy2NgfIebmoUkdZBg9SqZZjMHGhTeouvyhry4cy3fGHDIvRd8zV_VuSTtu9z_ypvk7LANHCj_eIGTkq72dBagrpg8nnsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
کنایه‌های تند جواد نکونام به قلعه‌نویی: فرصت داده شده، حتما یک‌جای کار ایراد دارد!
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/96763" target="_blank">📅 12:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96762">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e14e005e.mp4?token=ta3aQhYD65fudkycMXb4W4SSKBmyLQdzqEygwzKyUflpWcGK-Rft3XsDrTELAoUtK6r1E_FxlZ6-b6Aiz3uhB5r2GvY7sUKMUsbNTqi8XwFktNhtCr8JpKpI5VkxQgptWZrshDw3apLASAXG1B7lDvgWW0Z6GvGBCLNwaeKW5h-Ykvics7GLeQFut9rBRuQTVXpU-tCpCZ_WfMlxFtoe_yv3mdgaWtG7PX22XeRc8BFno0vcqlGt8fJ4K2AzE3Qo6O-__3PA4JADgIZHhykM3GneAFxjAmf1z3f3gRTmiCC5fAFO9Jki4QIAob4v_-Ye8v5gLorDhbSbGBTzDwWO1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e14e005e.mp4?token=ta3aQhYD65fudkycMXb4W4SSKBmyLQdzqEygwzKyUflpWcGK-Rft3XsDrTELAoUtK6r1E_FxlZ6-b6Aiz3uhB5r2GvY7sUKMUsbNTqi8XwFktNhtCr8JpKpI5VkxQgptWZrshDw3apLASAXG1B7lDvgWW0Z6GvGBCLNwaeKW5h-Ykvics7GLeQFut9rBRuQTVXpU-tCpCZ_WfMlxFtoe_yv3mdgaWtG7PX22XeRc8BFno0vcqlGt8fJ4K2AzE3Qo6O-__3PA4JADgIZHhykM3GneAFxjAmf1z3f3gRTmiCC5fAFO9Jki4QIAob4v_-Ye8v5gLorDhbSbGBTzDwWO1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
فیروز کریمی: طارمی در‌ جام‌جهانی حتی پخ هم نکرد. طارمی پول بلیت برگشت هواپیما را حساب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/96762" target="_blank">📅 12:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96761">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fdec54ce.mp4?token=SDPpFyuZRlLUAZkIRa61JDwdl_kx4nNr_fl587uZMMwBSwfpwYyCTeVi3ac-Ir-X4A1I_SprcJkBhJv3ozLL6o2iCaPQ0gE4k1S4hjmd-cRNWtQHjuaP3oEMmwSG7OyAqgZSZGXRMIh1P5-gSxjTrMsxh8rbrbgZ5hSEsaaB4FMfWNqSeHDQD0ELopCtfhNvtnk11l4aYHSJryBYSv5iEzY4LKUZKV3aZwpCY1ODQl8eOvWhrPZ_XjW414RJApUyHS5BmDHcARtupw7KUe-to70XEfgNZgxoyKC658Y2Wn7tXEHMvzfx_sP4JDYtgLB0_QYGn_3vjO0m3nyDp5C4wBCX_X42-UqpNBbd2HEAnbFDi8InfjiCJhILeYRQJYMi_zzWKDkIi9RSXLn7e07vxurReeQsHd5RvCUCDRchkXLz2wm6qJyrs18zQ1MuultC252v6PjBFMpsBlTQ--EWulch2opqWXJVHJ3n6Mn9oWbwClzDrC5Fx-Zd8UvXbZxOUPXpy7xnKVLco74XFQIvoR5vDiHLNbae15-15Bq7ETE9xLCgQkcUQTxobp1uvmk6BOJEkfvnJjISjzKse0dRU2w0iM4Ew1QWBp2Q3EP8veU98vbfV46O_VavTPWHOF-PtZPuUX3gVCHlvmbnZaQL4stkGXsbvoLlGQekBbOYGHE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fdec54ce.mp4?token=SDPpFyuZRlLUAZkIRa61JDwdl_kx4nNr_fl587uZMMwBSwfpwYyCTeVi3ac-Ir-X4A1I_SprcJkBhJv3ozLL6o2iCaPQ0gE4k1S4hjmd-cRNWtQHjuaP3oEMmwSG7OyAqgZSZGXRMIh1P5-gSxjTrMsxh8rbrbgZ5hSEsaaB4FMfWNqSeHDQD0ELopCtfhNvtnk11l4aYHSJryBYSv5iEzY4LKUZKV3aZwpCY1ODQl8eOvWhrPZ_XjW414RJApUyHS5BmDHcARtupw7KUe-to70XEfgNZgxoyKC658Y2Wn7tXEHMvzfx_sP4JDYtgLB0_QYGn_3vjO0m3nyDp5C4wBCX_X42-UqpNBbd2HEAnbFDi8InfjiCJhILeYRQJYMi_zzWKDkIi9RSXLn7e07vxurReeQsHd5RvCUCDRchkXLz2wm6qJyrs18zQ1MuultC252v6PjBFMpsBlTQ--EWulch2opqWXJVHJ3n6Mn9oWbwClzDrC5Fx-Zd8UvXbZxOUPXpy7xnKVLco74XFQIvoR5vDiHLNbae15-15Bq7ETE9xLCgQkcUQTxobp1uvmk6BOJEkfvnJjISjzKse0dRU2w0iM4Ew1QWBp2Q3EP8veU98vbfV46O_VavTPWHOF-PtZPuUX3gVCHlvmbnZaQL4stkGXsbvoLlGQekBbOYGHE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
نگاهی متفاوت به یک قانون جنجالی
⁉️
چرا محرم نویدکیا، موافق هایدریشن بریک است؟ مرور مزیت‌ها، و تنها عیب این قانون با سرمربی سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/96761" target="_blank">📅 11:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96760">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38e9d0491.mp4?token=j4r8bSSj2btd0VJaJjPqoeGr6TuKeUCR8q6QkPsrJR9wdMDMo1_UADIvdrgAXO7qeStyWJl4e1kcUzn8XSWW6hvNzz_hO3C9ajRE0CxvCyqz43ryWXGRIapMsfkY22A3CnB7_KuSZttjig4e242nU3MXY2hoPwNp5Win63ihQh9IYidxP763CLVGFuY97ayn5iZOEhioTBL0oKnwljCQiYzWfgLd_ryjhXwKDXJr-mJ_eV7nA-8WsPkYLU88EbE1cY2sgaxCrwcr2a_UQ9p29kQ8Axl7xGas27KylV4cQZxurfdyqUp6AZD3h-w-sAAuSIB-ZeXsazO_W564w1ZD-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38e9d0491.mp4?token=j4r8bSSj2btd0VJaJjPqoeGr6TuKeUCR8q6QkPsrJR9wdMDMo1_UADIvdrgAXO7qeStyWJl4e1kcUzn8XSWW6hvNzz_hO3C9ajRE0CxvCyqz43ryWXGRIapMsfkY22A3CnB7_KuSZttjig4e242nU3MXY2hoPwNp5Win63ihQh9IYidxP763CLVGFuY97ayn5iZOEhioTBL0oKnwljCQiYzWfgLd_ryjhXwKDXJr-mJ_eV7nA-8WsPkYLU88EbE1cY2sgaxCrwcr2a_UQ9p29kQ8Axl7xGas27KylV4cQZxurfdyqUp6AZD3h-w-sAAuSIB-ZeXsazO_W564w1ZD-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میزان سگ‌حشر بودن دخترای مکزیکی پشم‌ریزونه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/96760" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96759">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
فوری؛ رئیس جمهور پزشکیان: ۶ میلیارد دلار از منابع ایران در قطر آزاد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/96759" target="_blank">📅 11:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96754">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItQTvOjMaY72hFnp33Uu5i171b_GecWCiC_yWxbvvIKG03rYIl0bwmBhGnbhf6NC6jy_qk1y6D3irt44hcavgGspYAjnbRXAdrNsiNi9tw8uD04tvKFN9Aeq9EvDL8aX_P-w29T68yMigcuBfpgEP3NVqlSxuPA1iWKwF4K2Oju9mwJ_9ktM9ekb8EabNaPUo011qpsvkbluVzYdTd0GiYvRDeWOZyduT5DrTml9CUpXrgQxEZNyvuEhB5CdlgnbrhB6ursfhZ6EXanYsQWTPjB_zhZYjXTZNRmt137mjFFHSfX3wsKTs_cJmTpdVR0daKsFJWFh0DnFMNzxz1RviA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vuVAdiawpJgqJnsuw2DFg9xz7_gkd16Fe441d-kZRaE73B6Ll1Gw2amPmcp4eDAFBCQDiAcnlyDJPUjmPyV7gnwKtNX4mX0M0sgQMpS6B3KWhOHfYyCfsHyjMp3jpeAJuTlSdu8EucH_wfuh-mnOwQp-XAk-BdPz_nTTJMTDchK4KVGrPkPCUtnjNQRTztTX_s2NuAhNVkofhzTSnXKt1tFudUvFEse4LE7N_lkh05wySF5agqBldIA1lERDWArvRngXd3HER34h8vwksRJEbbjjvQnKXPzskO39hlXoEoLYM-FxCBh78KCBVE4SR2IAs1pwT97TOrdbygvfVvYqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfFB3CggZKZ6DnLSjDAmwCONi-xKRYJ00T9bHUwrgqiKFev8ERAK4YiYUh6CLbBZ1qgWYmGJ0jU3GrWb106nBWKQih5xSoiHJr-R1N8FzsxWwqbQEpNNM5NrW9r20uVIpBkBJ-deojl_JOzgekgjC589kNWGtYrvmvXbfy_QXYutDZ2MR_ufPV8DbTmL5BHt8siAr6iRhy-KpnsOBjQOFOr1XrflxTTBu2UW5QIaR5rvrpek8ruZuNgUmIQcUqSJRMMU3oKoVJ4zyRl6B2b3miU8WekkKzqpOhmuAiAjm8aJnEqCpxDk5XOJyuWPVBJDkmvn897JJq29N_-35h3f3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZISKfezz-Sfg8MW_ypPXyqj8kflHmlitJuFt_kFJD1ZHBH4-CDgkGpcC_uNrPPHIByEk4G8dHt5s3G7W-D9SpuwPySxAZZduTyOgEtZQmrUFfuEm9NbNoddukI2LTQ4MxSL8QR1t6rxDBkwmJBTERyP9S_4ldUM2UCNHkCERv9DGklcvNw7Vi1Ge8Oel2seJi9D_sOcifqScELhw0bRkC66J69vXBiBOTPa0xaygTONzntSeZT50QxaeLwTivTQ4oJla0eYTE1RGTHa7e_AM48wnEek4oCBfBr8yzRVW1CCeT6-aYSrGLWLjr9aFrB8k6_EF116Zya_bAnZ8-xDn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CT2c52bCFeKzVBI98FaDrfdLwLkHoHa_OUbY4sryK4swK8QjN5wF8dwHJEQRYKZZnin5Az0Q0lT3OPrYSiIUwj1LXNk25HzWEl2dnE-zh_NzqN2vxupJE7Z6iaBQD9-KbD1PlVMRVsjAaP4l3QMM0I1pdnROfByk0ZvyRZiqRElW0FZSRba0tTTcur_VAeVTzD3cMjGiz2EHl_NWORB6qSoOSLJIwEtgGNA9HJFtxe8k4RMkx82vbudezvEWxAyNuHdZz_jEaIVkCaapQqydWJTYxfqKeP1L6dv5QgARJyfXqM_7MvsshIe3aEc66_BJxdvNXFQIfjfZB799Xx1kYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
🇬🇭
همسر جرمی اکاپو بازیکن تیم‌ملی غنا در ورزشگاه بازی با انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/96754" target="_blank">📅 11:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96753">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBrVsTfPOBa6v2wuOA-7QD9O9v8AA9GpLlgnHlQ--9z6XdV3sewFz3FsfdCllARf29dfDDLnClZ9JigpvJGQcyQom0jt3CrcjBPAFmt88CgUVPtmBbw6KEkx3Vt4snqR3KsaOe5jnsvxLuZvnr3d-Ta8m-ki2zAIA1w7jfJscd642Fw2-HWY-KCIJ-xmHVBR0wAsnUgQPDE3t5ILek0mdvTPZdMQsxkJrsipaQBj7l2jP8egcfXgFpvUAZC0HkLkDLERHL2G9K5O1binJksMPaCWjacWp_N-T1eq_Y17OIG9y-MnlHpsJuB7YXTtRDAtxG8bWwBe9NeA-FAl6dQnyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسبت‌ها و احتمالات قهرمانی ۱۰ تیم برتر در جام جهانی ۲۰۲۶
📊
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/96753" target="_blank">📅 11:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96752">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lK7bXk9mm5hY1IObaRKmWYW0BvqC9JenmVRyswkiApYEohLuW3AtDAK8ktQWwKSvVmqWGkpObfK3BPqo9QKc_f2h8Ppi9mIxpW9eFQDqTKXNre5smeGjUCUL9NjSSnTyxhttaqyhaFC06jLALPVZI5VxWIWUp857GaHFJUuLB0LKts01myf3ch1JbGC2nJLOWNFb_W23TTOEYmLpNjarwxfPO8F4-m1AGMETa8NB-0jcypxL2V3t0M2-wNwbfww_uUm34jjboi2zFDRtgeb74g9Wp1LV13zlTUmQjYsG-v7IQsjKd0l3_RV5jqDLaB4m3QDZxcCr8EIWjOw7vTAAAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تنها بازیکنانی که در هر سه بازی مرحله گروهی جام جهانی، عنوان بهترین بازیکن زمین را کسب کرده‌اند:
🇵🇹
کریستیانو رونالدو (۲۰۱۰)
🇦🇷
لیونل مسی (۲۰۱۴)
🇧🇷
وینی جونیور (۲۰۲۶)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/96752" target="_blank">📅 10:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96751">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxtHXBn6uOkh_TXGBTjroToNh8UtoV1MhkCZqBUkoJj-0HbwxYWAV3gChTJUbJ0DhVYud1Qy2ZRgewWYuhTDF2KoV3XWj7FSEle_cabbcJuXbGyVdve0OIUxzDWLgLpNUJs4cJtIW4dMRMoaGxm2bqo2OhDfC0V22rWtkMkf-exzLuEz33r19jxZZUatgvAcr420OITrF-hK5arht9QLEg-vTCNxFCp8u7mpG3nW_PR6dQCPdFt67v_xkDdn3ZrrbIhRgB5exXw59UG5HOWogxwP0adsvSmJ8FOdhBeVTIY0dEpf12vevj1fKt4ziDkJ2rxVyAUXt8cg40x0W56Lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
مقایسه عملکرد کی‌روش در گروه مرگ و قلعه‌نویی در گروه زندگی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/96751" target="_blank">📅 10:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96750">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe_A0RhFCP_IPiSSUipxgFFy9DgkFWG1ESx2FqG-MNyNSF6gkTwlGjwJME01KjAQNTGDXCdo--f27FeyVg_mOq6JWScvu-BEg6SccgucceNIGwVGX4-QLs3gol3w6nHQ2wcNjui_yHiFldpGt-784jRYsFSmenkkE27tfmb-f_-3aavxuZqaPhpNyYnvT3MOnd7AqDf5hDYdagxDE3I3Dlhq8otadxVMheejXwr7s6eBnnjU5L8Mn6lQ6bU-yBgnb819gRsb34tvV13gG7Qt9zFhkK3eoCG7aH-n7X5rl6IJEhR-hHEM7Oha2s8CIPhl5jpY_YIoFEOkstZEfzjsbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
🤯
پشمامممممممممم
🇪🇸
‼️
رسوایی بزرگی درباره بازیکن اتلتیکو مادرید، متئو روجرری، امروز صبح فاش شد، پس از آنکه زنی پیام‌های خصوصی که او از طریق اینستاگرام برایش فرستاده بود را منتشر کرد.
طبق آنچه منتشر شده، متئو روجری به ازای هر پیام صوتی با محتوای جنسی که برایش می‌فرستاد، ۱۵۰ یورو پرداخت می‌کرد.
او همچنین از او خواسته بود عباراتی را تکرار کند که شامل توهین به مقدسات، عبارات نژادپرستانه و اهانت به خدا بود و نحوه تلفظ آن‌ها را به او آموزش می‌داد، به طوری که می‌گفت:
> «آن را با حرف دال قوی بگو»، «خیلی واضح تلفظ کن»، «اینطوری».
و همچنین از او پرسید:
> «اگر هنگام گوش دادن به ضبط‌های صوتی‌ات خودارضایی کنم، آزارت می‌دهد؟»
روجری پیام صوتی دیگری نیز فرستاد که گفته می‌شود صدای آن نشان می‌دهد او در حال خودارضایی بوده است.
زن افزود که او پیام صوتی دیگری فرستاد و در آن گفت:
> «به من هم بگو که به سیاه‌پوستان توهین می‌کنی و نژادپرست هستی.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/96750" target="_blank">📅 10:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96749">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6WnfsLoeoFc8cBkPfyQVWgrFC40p96Dn0HBrX4bYK3Nr15UUlcFgwffm01GjbD2LawKitxVANDdRz9OJIZJACscy1l9TMlYjRW6Tjh7hwystFFYE2NuFRUD617h2hymnzQ8iDwWI09821FgrCucCY7tFlj6L92Tc4heUrrETK3hsoIZwcgojS1Kv-j0t2M3M3GE2sgV2rIH3FA-LprgxT609dAcNKwc2CBzQ2EX1DnB0JbUeUchY4S7geGxTYOuG6fYahSmLsjDB7yWQv27U3VFoztRNqJZBcPvHe7c6MSxSqyvk5R0PcM5X4fxAnlwTQWMYf_SH4SiknqSEGoyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از اسپورت: دیگو سیمئونه از سران اتلتیکومادرید درخواست کرده که خولیان آلوارز را هرچه سریعتر به فروش برسانند. سرمربی تیم معتقد است که این بازیکن بعد از اظهارات اخیرش به تیم پایبند نخواهد بود و مشکل‌ساز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/96749" target="_blank">📅 10:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96748">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f669d874d.mp4?token=GXqi2Z5ZHKlaTDNf3k2Rlp6c9K1-Ns0hhyzUnBINXZoFZ2M0WPTq3p0ANOQRbVZKYZ1RI1M4DphzBHVda73XseQ7vJDAOIKHgGvqatdHgbKIy2rtOQ_EmMXq5GfaYtG-SnCDEN0_hOn4ISjc92yMO9shCr-oR3EHIBtpS-qPfvfQET0G8aifkymRKET5SpxjfBDzwBn_Pi97Te_VX5aDczGKX13FFip993YnuzMrxPtxPo7ggn8HJGuVCA3D2Qs9rBHCBz6plGXFi4HZiwD9doK8sbW-67SFGe1XI7tX95nXFSrGiX0Q5q7y453vN7Aro_KZj3SjlLB8CTR-c4VLJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f669d874d.mp4?token=GXqi2Z5ZHKlaTDNf3k2Rlp6c9K1-Ns0hhyzUnBINXZoFZ2M0WPTq3p0ANOQRbVZKYZ1RI1M4DphzBHVda73XseQ7vJDAOIKHgGvqatdHgbKIy2rtOQ_EmMXq5GfaYtG-SnCDEN0_hOn4ISjc92yMO9shCr-oR3EHIBtpS-qPfvfQET0G8aifkymRKET5SpxjfBDzwBn_Pi97Te_VX5aDczGKX13FFip993YnuzMrxPtxPo7ggn8HJGuVCA3D2Qs9rBHCBz6plGXFi4HZiwD9doK8sbW-67SFGe1XI7tX95nXFSrGiX0Q5q7y453vN7Aro_KZj3SjlLB8CTR-c4VLJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
😁
😁
مصری‌ها سال‌ها میتونن با این شاهکار شجاع خلیل‌زاده میم درست کنن و بخندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/96748" target="_blank">📅 10:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96747">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🏆
برنامه مسابقات مرحله‌یک‌شانزدهم
🇨🇦
کانادا
😃
-
😏
آفریقای جنوبی
🇿🇦
🇧🇷
برزیل
🆚
ژاپن
🇯🇵
دوشنبه ۸ تیر ساعت ۲۰:۳۰
🇩🇪
آلمان
🆚
پاراگوئه
🇵🇾
سه‌شنبه ۹ تیر ساعت 00:00 بامداد
🇲🇦
مراکش
🆚
هلند
🇳🇱
سه‌شنبه ۹ تیر ساعت 04:30 بامداد
🇳🇴
نروژ
🆚
ساحل‌عاج
🇨🇮
سه‌شنبه ۹ تیر ساعت 20:30…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/96747" target="_blank">📅 10:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96746">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5a653813.mp4?token=NcTMgww2EwZfRvZhR60Y1VKd9ayJ59e29GTvFfxzLvRJdls8I22ppVRlYifDdHVdWzrxBPRCpf_mae7FCna-bF6skbJDqONYD6_7hssa8vHENx7eQ4hGhfforPGSlnwbfv0pvMbO60ZYf8EGAp2oRmmqlEb8G_m9cD0ySx7fOSeUfItpS_X1c0W6_XFrbaGaGcMo75xxWSeuPLLk3FCjO16hwwyu1KkoCSV2DSfEdsqOUj01J-6Pg_FINqMARiLhov7GaGfDSJ_HN9F5gP-MZeyuwGd60ZTVHN9pnggiOlxzAHY2ux3tcmmAYxjGljAiMYoR25XD0fzTONQNLTgMOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5a653813.mp4?token=NcTMgww2EwZfRvZhR60Y1VKd9ayJ59e29GTvFfxzLvRJdls8I22ppVRlYifDdHVdWzrxBPRCpf_mae7FCna-bF6skbJDqONYD6_7hssa8vHENx7eQ4hGhfforPGSlnwbfv0pvMbO60ZYf8EGAp2oRmmqlEb8G_m9cD0ySx7fOSeUfItpS_X1c0W6_XFrbaGaGcMo75xxWSeuPLLk3FCjO16hwwyu1KkoCSV2DSfEdsqOUj01J-6Pg_FINqMARiLhov7GaGfDSJ_HN9F5gP-MZeyuwGd60ZTVHN9pnggiOlxzAHY2ux3tcmmAYxjGljAiMYoR25XD0fzTONQNLTgMOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
🇮🇷
بهترین نسل تاریخ ایران به روایت ویدیو:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/96746" target="_blank">📅 10:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96745">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6df7bd6.mp4?token=Infx-WR31X1zhreLOFPOCHoVUId98b_gDKmhVkqvivnaDU6A8L6svldhsJ6DHYicz5kMfGEPCZmuDEaHrJ50_e7gXORXjselXw_o6ZKDYEKKoQl1BOVt3rjns6QhLzAeAhfR0tC0z0YTSbIGAqf3qaT2CqNsMoAYKy9XZoL-s7i6BOZpP5RD7K1ETo7nIbY9FzClH8sGTzwoqlsqMNRmYk5uVTiO8AmxrMK3FP3f-RhH6NBIuJkfICGAzlVbCRbBuIBhMLZuFLOYoeyqzZfS3-TxeiW4XN3bEgaE0VukGp_hV_jNK8O8D8hwd893JfOntGRWgQetD1AgtN-Yaly9PiyjzhyXVtjMI41N6EIBNZ6GdFy2PS_UTLO90s9b7aQTNEwfIAWrgSpsuMlg79L0P1ulFcgnkHDl4ibAPMHXSCR0oKsKfYP2ZWiIvxgrgSWpdxWYHMM5ibwYpuQhbfFpty-naOHcTEHk5qIAcCMD_hty4moVVcSY3yq80EyWit-U21ZITNJuCbNmp4DRJYHqI5kI9o9SGqqbQ4LUxP8RGjI_81wrowiO_5BDYitsaMx4RTHxYJY7uOdAW3t_1hgzLa6iSCAgkwqknmisu3ONFL_gWi_1pq73VfaneOwW0n3p5A7VaB1GC6QoPNMYQ_dyIfROtmokK7VfWUyzY8bnUUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6df7bd6.mp4?token=Infx-WR31X1zhreLOFPOCHoVUId98b_gDKmhVkqvivnaDU6A8L6svldhsJ6DHYicz5kMfGEPCZmuDEaHrJ50_e7gXORXjselXw_o6ZKDYEKKoQl1BOVt3rjns6QhLzAeAhfR0tC0z0YTSbIGAqf3qaT2CqNsMoAYKy9XZoL-s7i6BOZpP5RD7K1ETo7nIbY9FzClH8sGTzwoqlsqMNRmYk5uVTiO8AmxrMK3FP3f-RhH6NBIuJkfICGAzlVbCRbBuIBhMLZuFLOYoeyqzZfS3-TxeiW4XN3bEgaE0VukGp_hV_jNK8O8D8hwd893JfOntGRWgQetD1AgtN-Yaly9PiyjzhyXVtjMI41N6EIBNZ6GdFy2PS_UTLO90s9b7aQTNEwfIAWrgSpsuMlg79L0P1ulFcgnkHDl4ibAPMHXSCR0oKsKfYP2ZWiIvxgrgSWpdxWYHMM5ibwYpuQhbfFpty-naOHcTEHk5qIAcCMD_hty4moVVcSY3yq80EyWit-U21ZITNJuCbNmp4DRJYHqI5kI9o9SGqqbQ4LUxP8RGjI_81wrowiO_5BDYitsaMx4RTHxYJY7uOdAW3t_1hgzLa6iSCAgkwqknmisu3ONFL_gWi_1pq73VfaneOwW0n3p5A7VaB1GC6QoPNMYQ_dyIfROtmokK7VfWUyzY8bnUUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
گنده‌گویی مجدد سجاد غریبی با غول انگلیسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/96745" target="_blank">📅 09:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96744">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cdcdf95c9.mp4?token=M16rMcA5LN6Vx23An5u4EI3siAUfmiH75GYRxcIYOXEZ5BHLpJXbnKis55lrEl9Cvdl-4mSghfshhXl_Y4SUrHUIN4VN5WQ_2Krzfd7EU50daxVxy1gtmJU5HxIaBXVKoAwGyy_l7qeylSgjS8-B7UBnaLvxc9xtewoyNYdQrW4kgq0fHpkxOQM6AtsShcDu4N1005SuPdnSh-4JqnZAaU5K4CSR2zcjUb6dMeGA6X51lyRBG5GI-mtSeeyIMPshFpew1l1FS51S8hASG6sfB_Hwo1tuzqM8tNSfAIjx4OuB4k9Cfp6V6wfEREZUBPIsgsmt-45p5p_V5VrFr4qLcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cdcdf95c9.mp4?token=M16rMcA5LN6Vx23An5u4EI3siAUfmiH75GYRxcIYOXEZ5BHLpJXbnKis55lrEl9Cvdl-4mSghfshhXl_Y4SUrHUIN4VN5WQ_2Krzfd7EU50daxVxy1gtmJU5HxIaBXVKoAwGyy_l7qeylSgjS8-B7UBnaLvxc9xtewoyNYdQrW4kgq0fHpkxOQM6AtsShcDu4N1005SuPdnSh-4JqnZAaU5K4CSR2zcjUb6dMeGA6X51lyRBG5GI-mtSeeyIMPshFpew1l1FS51S8hASG6sfB_Hwo1tuzqM8tNSfAIjx4OuB4k9Cfp6V6wfEREZUBPIsgsmt-45p5p_V5VrFr4qLcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کواراتسخلیا - بارکولا - دوئه و دمبله کم بود، ناصر قراره این شاهکار (دیومانده) رو هم به خط حمله پاریس اضافه کنه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/96744" target="_blank">📅 09:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96743">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMqzMqgcYQ-9GiLH4wVdpiLm-oesgKLBBQbWno927x0zel_zEzjj50L7R9Kqo6ZWSIcl0CfmKexf-B8uTlZQdExwxOdauc7SCkfFdegUT9GP_nhGIlp7YgRuPLWZ9sJ8vf4R9P79nd7rXtjiFNKbu6jEETQkMYWoq79brGVi_Hm5_azMMikt3NbvD-cb7Q58fWRZvCojlcqLJZc0HY94nVMy2nn5GxXLyHJMecmfpKYI_j3_bZ4Y6SGiTSN99I3sJ20QiidoDP1Ba8YXCFMgGM2V6l4WBVoz870c_x5FKgN-ScjCt9BN399UlUhpInmvzs_IAuMGDGpJtLzuxBlXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
توماس مولر: «در آلمان، ما به سوپر‌استار بودن اعتقاد نداریم. از سنین پایین به ما آموختند که به عنوان یک تیم بازی بازی کنیم، نه اینکه تنهایی بدرخشیم.
🔺
به همین دلیل است که بازیکنان آلمانی زیادی را نمی‌بینید که توپ طلا ببرند، اما می‌توانید ۴ ستاره را روی پیراهن ما ببینید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/96743" target="_blank">📅 09:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96742">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owE8ckADb2MsSvOTb4pkcjCYwO3qynN29gxKV31ZWdm-EMxxNrL_LnV4NW0t1TfSzCeCzGgOs8pHx4matEFYJjvNb19aKGpoy-8T_wHKjT52vi4UFaSp_P864kk_qc5nsP3HjL88scBmbXUjh1nnrqWt6w1l1QPJhthfBiU0JV6HxHYHQ_1kWwaigfteFn6eMpQAm2wFQuo-qXHn-mUZbOG5KNggOc250X9H5P7qW5xEWnU4ubZR7rvQ9yWbx212r6Td0Pj3ye6yYxPD4Z9Lzu6YS7VFNv0W0jiUkT_OrLbqYE0D5jewy_Eqgqvy6zoBs1xWiWxcBcDPHKBHIHmgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
در مسابقه‌ای که هافبک‌هایی مانند:
🔹
ویتینیا: بهترین بازیکن فینال لیگ قهرمانان اروپا و حضور در تیم منتخب فصل چمپیونز‌لیگ
🔹
برونو فرناندز: بهترین بازیکن فصل گذشته پرمیر لیگ
🔹
ژائو نوس: یکی از بهترین هافبک‌های فعلی جهان
‼️
حضور داشتند، بهترین هافبک زمین در بازی کلمبیا مقابل پرتغال، خامس رودریگز ۳۴ ساله بود...
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/96742" target="_blank">📅 08:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96741">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9609549bad.mp4?token=IQT4A2SFw_GLP9dL8R_6YwAcigPZky-0hVowY4EnrQCEo2m2KRHDKqB80_GCNByl4Ics5Lz-FjqbOTz1coJRja14ynwgjBMhJHqHLEdsKSuR8I1Pa4Qxl1u_D3WcHUkru1B8yR132cHc3bWgh_QmXBHgbu8KZd_nbZfabxSQX7kswcdp2L9TesA4uw25kR7obeUxhv-x_jWKbNtWwCVh0YqdkEQxeiI3B0UDW6diE1eHl4Alos0-aGlPi3rrR0OrIqxSBsoju7rfu1KPblQ8bXMY7s-FPnIqyTgxOupm2ZztECS18Eh2Ky1nGQOwqDw8YmRUoLJ2nLx_g6ERSbXZ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9609549bad.mp4?token=IQT4A2SFw_GLP9dL8R_6YwAcigPZky-0hVowY4EnrQCEo2m2KRHDKqB80_GCNByl4Ics5Lz-FjqbOTz1coJRja14ynwgjBMhJHqHLEdsKSuR8I1Pa4Qxl1u_D3WcHUkru1B8yR132cHc3bWgh_QmXBHgbu8KZd_nbZfabxSQX7kswcdp2L9TesA4uw25kR7obeUxhv-x_jWKbNtWwCVh0YqdkEQxeiI3B0UDW6diE1eHl4Alos0-aGlPi3rrR0OrIqxSBsoju7rfu1KPblQ8bXMY7s-FPnIqyTgxOupm2ZztECS18Eh2Ky1nGQOwqDw8YmRUoLJ2nLx_g6ERSbXZ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تناقض‌عجیب صحبت‌های میثاقی راجب شجاع خلیل‌زاده؛ رنگ‌عوض کردن این اراذل خیلی جالبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/Futball180TV/96741" target="_blank">📅 04:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96740">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7323fbe34.mp4?token=Bt5m_nQI2HGaIRblxruevZKjL0f7M689mk5HSfTR137U4r5ZC5xf2RP4Hs7WK4gXailkdXVcf2IjYmn-aO37B1hyUqzs7Ssrj6KeFEJ78mFM3gOulCWj0i1RjJqDWY_T-DF9s-uZfp_NXinhQ8urEGnqq-pZyuqphxoBks548VbwCyHi-7wWYfdCw3zQlDANPBIbAGNdTQ68GA8KK8J5fR88o5jpxrMVzkQhgUipsMwQdBOSfZ6WKp23zNx7-w4sLvjFNvsPWqmLl5pjOGLxaksaE7lD0T-_-UraBClyZeeCseuFkGLknhtwwUYQaTsYeBnEPSMlnG8Jb5g7YpdZaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7323fbe34.mp4?token=Bt5m_nQI2HGaIRblxruevZKjL0f7M689mk5HSfTR137U4r5ZC5xf2RP4Hs7WK4gXailkdXVcf2IjYmn-aO37B1hyUqzs7Ssrj6KeFEJ78mFM3gOulCWj0i1RjJqDWY_T-DF9s-uZfp_NXinhQ8urEGnqq-pZyuqphxoBks548VbwCyHi-7wWYfdCw3zQlDANPBIbAGNdTQ68GA8KK8J5fR88o5jpxrMVzkQhgUipsMwQdBOSfZ6WKp23zNx7-w4sLvjFNvsPWqmLl5pjOGLxaksaE7lD0T-_-UraBClyZeeCseuFkGLknhtwwUYQaTsYeBnEPSMlnG8Jb5g7YpdZaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
عذرخواهی پیروز قربانی از امیر قلعه‌نویی بابت مصاحبه اخیرش بعد بازی با نیوزیلند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/Futball180TV/96740" target="_blank">📅 04:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96739">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/96739" target="_blank">📅 04:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96738">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8cda33a18.mp4?token=oO2N3-KZjYsUM3crWbjEcCPgRIJnJ6AL_QxzhMqiVwE0PZcl184D9A6AeIaB9aMZIn3ZIFBcVSJ4irFSTbmWg1QFSRxGWbw7ZkUl_JNZibCnVb6ipdMPwvvQJeOHKajogJ2j6dPaNtGhORrrSpN_qLzn25-cf-GEJ7EQVM5_WNOv119u7JhMRLh_-oMWWMkjoWUKbDrg6tXtK360qlxUs2oJbfnsphDz6PlTvM7oug_FFkG8I5yZLhdTsbk5genyg2iJ2CNY2prenQr94gNUv4aoCx3NGhMir1Bl4fDFay2_ejKYHrUrjZUyAg3eoxI6qVwrZdAMF41ZRwq1EAKt4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8cda33a18.mp4?token=oO2N3-KZjYsUM3crWbjEcCPgRIJnJ6AL_QxzhMqiVwE0PZcl184D9A6AeIaB9aMZIn3ZIFBcVSJ4irFSTbmWg1QFSRxGWbw7ZkUl_JNZibCnVb6ipdMPwvvQJeOHKajogJ2j6dPaNtGhORrrSpN_qLzn25-cf-GEJ7EQVM5_WNOv119u7JhMRLh_-oMWWMkjoWUKbDrg6tXtK360qlxUs2oJbfnsphDz6PlTvM7oug_FFkG8I5yZLhdTsbk5genyg2iJ2CNY2prenQr94gNUv4aoCx3NGhMir1Bl4fDFay2_ejKYHrUrjZUyAg3eoxI6qVwrZdAMF41ZRwq1EAKt4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلیل نتایج خوب آرژانتین همین هواداراشونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/Futball180TV/96738" target="_blank">📅 04:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96737">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43e217c61.mp4?token=T82qmXB0oqGbR8y4Epz9hDN06Dvx5H_QbQ6tuzmcVJgT9_wbStViEkPB32Z6yDJ1FTneZ69r3LYLFblOSrjvr73dHMPJMkENP23MpL7XXe8oqpWISS4c1sE9ljIZkeWX8GyQWVP0SS5nRysLkY8lnuQSKM3MXLT2Q9_KSlVY-hbT2UzaW9koMF4AUZWKax_XUiqX7QTR6_yq3f7lfohQFb8kB_rQZkOkd7ICKrtlCFxc46z4P6KNEQ4OLiu1WkfMf67_C_NhwMAFUer5P_UhqVg6hYkeT3VPhdc5nhBxJ6SEVOkaDHVUbLvv1G7B3tPzYMtfFXYc2CoEoc6BGGi_Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43e217c61.mp4?token=T82qmXB0oqGbR8y4Epz9hDN06Dvx5H_QbQ6tuzmcVJgT9_wbStViEkPB32Z6yDJ1FTneZ69r3LYLFblOSrjvr73dHMPJMkENP23MpL7XXe8oqpWISS4c1sE9ljIZkeWX8GyQWVP0SS5nRysLkY8lnuQSKM3MXLT2Q9_KSlVY-hbT2UzaW9koMF4AUZWKax_XUiqX7QTR6_yq3f7lfohQFb8kB_rQZkOkd7ICKrtlCFxc46z4P6KNEQ4OLiu1WkfMf67_C_NhwMAFUer5P_UhqVg6hYkeT3VPhdc5nhBxJ6SEVOkaDHVUbLvv1G7B3tPzYMtfFXYc2CoEoc6BGGi_Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
12 سال پیش تو همچین روزی، خامس این شاهکار هنری رو مقابل اروگوئه خلق کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/Futball180TV/96737" target="_blank">📅 03:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96736">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4RCse3f4k7lYSQXvKQgcAC4rZRux7M0kOiiYL73ANkNvF1M35iYtw-chXdYUFBy3sdVHuii6H0YkMeOctv0XTgJdLRI0gVjYdgI5o2TUBqvrT3mM-7tnTTRUujCDbxkmtWA8jf6vjbkr94cxZoldrNIjyj08vc3PS3oB2QSWZKI_keouZwU1RvpuaiuIzyGVPBc9LWmunjdBIP7fF_NHyB_Iwhad1PORK_22XCthGJ6IfnrZB3jLmMbknDfh9HBLJZAVxephMV5C0MPPceFzef0gcKr_c3M8-DUTA4OWlmCPMGtsRrC0jx2z66ews5YTUMD6uUnRSuC12B3j3XFXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوریییییی
از کریگ هوپ:
🔺
بارسلونا در حال بررسی امکان جذب هری کین از بایرن مونیخه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/Futball180TV/96736" target="_blank">📅 02:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96735">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb77bafea0.mp4?token=C48YnaAIgy1uFOJv_sZT_J47jLwHoQ_n1MN_pOj0XbYdoT5eNUU9i1w7rrGADNyyW3R8W3DFcNc0_K3eBQmmyxw6D01wIiPvX3wftoNL-1xfXaDBVwIc2IJDGSTpANCxcK7wW-gVfvab_ZJkWNTsjZxKVlAsgDZxws69YDM_Wjl-eu5mm_tO5xGFNvTXtyo2v0dkc5JDlDyf3wTGPwY-TMs2dfIo-bi7coRnRTnVpU_87S1S9JVzZd7JMzPUrRTiwXxb33PZS6PvXKTxcLV8nS9KqWS0CPEmIf-VZDXYZYrSlh4EjacmLDWcD2JnliIAELm3HXIyCokfpbLRcx5urw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb77bafea0.mp4?token=C48YnaAIgy1uFOJv_sZT_J47jLwHoQ_n1MN_pOj0XbYdoT5eNUU9i1w7rrGADNyyW3R8W3DFcNc0_K3eBQmmyxw6D01wIiPvX3wftoNL-1xfXaDBVwIc2IJDGSTpANCxcK7wW-gVfvab_ZJkWNTsjZxKVlAsgDZxws69YDM_Wjl-eu5mm_tO5xGFNvTXtyo2v0dkc5JDlDyf3wTGPwY-TMs2dfIo-bi7coRnRTnVpU_87S1S9JVzZd7JMzPUrRTiwXxb33PZS6PvXKTxcLV8nS9KqWS0CPEmIf-VZDXYZYrSlh4EjacmLDWcD2JnliIAELm3HXIyCokfpbLRcx5urw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇵🇹
تو حاشیه جام‌جهانی یه خبرنگار میخواست با ژائو نوس مصاحبه بگیره که ستاره پرتغال با دادن به تیکه پیتزا به خبرنگار، سرگرمش کرد و تا از مصاحبه فرار کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/96735" target="_blank">📅 02:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96734">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fee527586.mp4?token=cI2ssMH8J8ClooE5nRQZCq_wsr8Lv_2tuzyMssAyAJKuP_peguR_Udyp9V6vjfnnjG-BCCRPbzYvzti0uThAMp0Fo79eY-YbQGIg-Z7g41Rfh4rXII4_3LCxW8P_ZIvYXx74RkOvlNiphrRY5YPIYjXRDDbYz1Ko_oo3RqUxDZQKPI4c2VeNH1SZWjpi6LLCgPUPa19KD6efhxYdNLxBjPmiZ-4UWzeLT3BzOvxfsoqRm_c5kjhOwfsAQkCZekpYAqxPIm5FSOYmOxDTAEXmspxFDSPBvxfKjRQlQwVWW6JFBwyfU6Vyl9ctlSFXCc0SuTfQK87ATVn-JoPQPe9sTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fee527586.mp4?token=cI2ssMH8J8ClooE5nRQZCq_wsr8Lv_2tuzyMssAyAJKuP_peguR_Udyp9V6vjfnnjG-BCCRPbzYvzti0uThAMp0Fo79eY-YbQGIg-Z7g41Rfh4rXII4_3LCxW8P_ZIvYXx74RkOvlNiphrRY5YPIYjXRDDbYz1Ko_oo3RqUxDZQKPI4c2VeNH1SZWjpi6LLCgPUPa19KD6efhxYdNLxBjPmiZ-4UWzeLT3BzOvxfsoqRm_c5kjhOwfsAQkCZekpYAqxPIm5FSOYmOxDTAEXmspxFDSPBvxfKjRQlQwVWW6JFBwyfU6Vyl9ctlSFXCc0SuTfQK87ATVn-JoPQPe9sTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توصیه رونالدو به رودریگو: «باید صبور باشی، همه چیز خوب پیش میره...»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/96734" target="_blank">📅 02:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96733">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqLdcJ0ilfwm5BYIo47l085WWEisOPc_KXRU0NkrK6a34ixERUpydnydIcXo42tnZ1swg7uFyzc0J9_u6sJ5yfjwNMkX67GuAfyKq8fbh3PflBC6egnSL5KBMCFpzZl4epKym5hhBpj-bgyNEnYeJ9wuqs1XUoW-pv6XPySJBks13foRcTJOCH4blG1QBKB1zKmrW95ztrr5v3kuYr1GmTTXzJbLkOioX1rgmuSpUftJNjGOSW4y80aAJwkIus3me6M8T8zsw5CzCClbcvG2gmSrB2INm7UkOR5-aptZ25jHWVQLNVctxTZ-XzkaHV1k3GUb0o8tabK4RIBEidc6Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند و ترویس اسکات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/96733" target="_blank">📅 02:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96732">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt81Bnihe6rqD9J1kRj26SIiqatUVhszBn1KCGylp1VVcKXHiu8lkuEoPoI16kqMawO-ssjmyH3Fix8rSNEsq4wPGOBSb2au45bSKvModOpq5LX0nQ1dcDcQkQQUBRaE9XAuz5YSEC6aP_H7rF0OYHY8yR1JI9UuEB9WL0fyWe5e_LzI_KEZPrpxuGpJh-C8IjNnI6nIFbOePW7Hn9gqxb4uSzgpPkvuPbz014fPuA7fugV1ANBXHO6iDgJicV2eHlE9ZPwmQ7YS50kCW1RXTTiBH2FRPYC4haYPI3k2ODfbbEyQLtSZujQmXA5cWQ6suYKPxZ3KwCGuF8keZQLmZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک 230 هزار دلار رو صعود کانادا سود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/96732" target="_blank">📅 02:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96730">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/agPBIeIxzVx1tKMLCAcb3S-6x7sZSPAR1Gk0IPM9DREaJ9XMGPB9MSnCUxNJAu916i84tKv_z_6I8XTGvUMJYvuvQDsC30RIU8jHxyGj3oVWlZovlV4jXS5j2FlqzBa1KucCwTi7KvSQnR9w5uvYr9ajNVBB5xLDaqz8gJR7ZDHNq7XTKx6HI0EJKSXYu8GYJOYQVPvUkEF-TdymGAdf3_0w215pNvULnMDDXVH2cOX1B3tgpQGaXif54H2sCHWpYCFS42Q4MyER1KhyGz6BP2R8KLtW7MKF7g_LNpQ3XWIzYubzTnm2Ben7iBgzdowQgBfh3Tzt9YKaDYGCag5sjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/96730" target="_blank">📅 02:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96729">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3A8KafQTYDojmgurzMqlcIH5fkrzEmN2_fofxMPkJUhQbcuWAcrQx3RYsc35IXN3zrTE1nQ6If6nWxOnH82uOd77-gjrr_zoJ28cc-4PNLyD327e259s81szj90dh1K5LG63p1u7uPTe0Ya8HKBpE1_aI5Tvh47gGIOX_B8pfcJeycUvGcwMMhl8FB9EUuTiR66EnrvTtKg8xLCK_0z5Ws3j1GOSv51eO-3NuzizFNh3-fc50HSXy21U1rVmkLvRsJcFd4bdDJo-BZQpEyZejRMfzgIZiSP0rPHhD0ydu0qUaKAps9Xu7Spd_Bz0-vEvoxwLOnRYONVA6MvEqukPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
ماتئو مورتو:
بارسلونا قصد دارد با بردلی بارکولا مذاکره کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/96729" target="_blank">📅 02:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96728">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FvYI4QxJEzwxLQeN2CeZ7egzSZxcF3-X03kjOVkHiXiAhm0NPRODnitwtyPxNCne1g-y5DvplMLzFmvOrY7YYcRmP5PeiXE5N2kzZEBasvw0tqbKOEchcIXFvDM0-Mazjd2D8pU4ieQEq6vYTbIvEQ7pMPzASwo2IcEzl_ylVSEsrj-m7OcApi9SoqPc_XCelwvGYwtCj0WMSLKLsr1SuYZcJQDbP4BGXAmC5ZTYavEY87_0I7DAvNkvR4MZcCuEnhEEsEPZvbm_iWrqGznbCYpuiD2jaOANhr-MI67YTkarxKNHog8ZlNxpUnzRQiEVK5Z2ZWOCmDch_UeDrGDItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
موریاسو سرمربی ژاپن:
ما می‌خواهیم برزیل را حذف کنیم، توانایی رسیدن به آن را داریم و فلسفه بازی‌مان را تغییر نمی‌دهم، اما برای این دیدار برنامه خاصی دارم و برزیل را به چالش خواهیم کشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/Futball180TV/96728" target="_blank">📅 01:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96727">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKDZ2_gZGNEkML5fR6_pm9Bafc_oSJNNHoUqsIs2fUsrE2r-Lk-r4GRVVoTuTgjtZVXVbU1tL8kkM5tzinZRQT9W56NwBnaUW9Et4dEnE2FBDBd951OQc68sZgrEAOQywVnY12mF7VaYFkV8hSPDCx9hEhQMD1KlY_Y3bCrASOvKJ3vanqkmDClIGL-ANy0--NHBcvSpB1TIXXVKwZe5WNAheCeA1FIcqSo_lee5W0NosD0-J--cGTbo1KWLSogc33HtMPHJLBCi1TeE37bIVCh7sCDnTJJyvmbYWLscwJfjcJMepYSbW31XDoUIJVpGvOMSJCzZXxCCakKmXxTPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو
: پاریسن ژرمن در تابستان امسال روی جدایی سه بازیکن حساب میکند، معاملاتی که تقریباً یک معامله تمام شده به حساب می آیند.
گونزالو راموس به میلان با 74 میلیون یورو
کانگ این لی در حال مذاکره پیشرفته با اتلتیکو مادرید است.
کولو موانی با یوونتوس به توافق رسیده است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/96727" target="_blank">📅 01:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96726">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf096ac36.mp4?token=b6c5UMJ7ZlmRRsY46_c7CgyGq-AM0Y3J_RuMlqdi5fdUW_e389-glA8BJdgby4eoEqjTWRR3k0Drn6VEBmYHDOydtwbjo1HlpUFXa18_flc8s2rlwQ7acfgWRsSHJgbvpoYURFnXLJPZnVEwfuBZcDVBg_Cc4HLHkmhmz8_VwqqT5e2SBEh7bagevgAp8jN9vRGUeknyALGf5ZrTBD2WPspSToe5hstxCdIPALQESBLBok72tdcRIYCNSmxrY478LT8vw8BjBDvACiGl0JcY2eH3zEi6pVMa6ea1kO1-o9t5Cgxeu8sVr2OrTJ60NJOUMRSHozFmYGFdo5NpVCZZ73mWFoRJe2Wi8OE9tj56kgfdnFOOAGC0JmzFUVSEnveeStpWd0kRqo5YdSLENmZ86jSWPRgUJPYOOmfX7SXd7WeNoe5B15XC0CjjCouaqj60zf4YtuMqfuxTDVaerRAjZ0PLvfdjd6xbfBZrOs039hEiifPQpen64Z6wH8gPtoOKj2EKszK1oNojCAvt31IJscEL_5rJ6A0eQv9FO1aQqXASIKglrI6xEtncCgx1Vngx-HOKH9vGy_d6FWFebNEafLQ0ts8XChINbk7jl-SAcn8IiYZfqhNcP8b-EWOPFwcNERJ3MVHyB-gpaH6VtBuXPg2p_tGZuDHGYlLVb1iBNMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf096ac36.mp4?token=b6c5UMJ7ZlmRRsY46_c7CgyGq-AM0Y3J_RuMlqdi5fdUW_e389-glA8BJdgby4eoEqjTWRR3k0Drn6VEBmYHDOydtwbjo1HlpUFXa18_flc8s2rlwQ7acfgWRsSHJgbvpoYURFnXLJPZnVEwfuBZcDVBg_Cc4HLHkmhmz8_VwqqT5e2SBEh7bagevgAp8jN9vRGUeknyALGf5ZrTBD2WPspSToe5hstxCdIPALQESBLBok72tdcRIYCNSmxrY478LT8vw8BjBDvACiGl0JcY2eH3zEi6pVMa6ea1kO1-o9t5Cgxeu8sVr2OrTJ60NJOUMRSHozFmYGFdo5NpVCZZ73mWFoRJe2Wi8OE9tj56kgfdnFOOAGC0JmzFUVSEnveeStpWd0kRqo5YdSLENmZ86jSWPRgUJPYOOmfX7SXd7WeNoe5B15XC0CjjCouaqj60zf4YtuMqfuxTDVaerRAjZ0PLvfdjd6xbfBZrOs039hEiifPQpen64Z6wH8gPtoOKj2EKszK1oNojCAvt31IJscEL_5rJ6A0eQv9FO1aQqXASIKglrI6xEtncCgx1Vngx-HOKH9vGy_d6FWFebNEafLQ0ts8XChINbk7jl-SAcn8IiYZfqhNcP8b-EWOPFwcNERJ3MVHyB-gpaH6VtBuXPg2p_tGZuDHGYlLVb1iBNMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😁
😁
صحبت‌های ابوطالب‌حسینی درباره شاهکار دیشب جمشید خیابانی به زبان عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/Futball180TV/96726" target="_blank">📅 01:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96725">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jA3J_jpCizwnkhNUwoc52qrTc0jXQwzHmHNJE00M7XmcsL9A-nxPyO8V0kqCutWDFYEIwU-S7RK0Z6e0FXhQAb7SR6cN8agIJUY4KI6uN--iy7g5r_tHronV2dPmh9us4O6Rd7N78VIlEwmnX_0u1vuzn8QMzUAbMmZovGBnwLHXgLbcaX7Jx1k0yg3IoE931vSiBwjqEam13KNUg5AabW1o6KUma-LuY73BP9czfWnfeFQcRcd1rKwL0RTpyE4ccnE-cwphs7j3sfYyBckw-ZpUd8rLi9-gCViB8mIexYOZoVdeVD64H1_btKrUjKVP_6conjAUUVi9loMx6Ms8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇨🇦
کانادا در جام جهانی ۲۰۲۶:
🤝
تساوی مقابل بوسنی و هرزگوین
✅
پیروزی مقابل قطر
❌
شکست مقابل سوئیس
✅
پیروزی مقابل آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/Futball180TV/96725" target="_blank">📅 00:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96724">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdKNTizfJXI7O1vzA8WYtFey7-E_oQRXBxsKn0P538h5DznWuoNAsFXO52J3kgoL0akcfko2Ry3fzKPbfYW8I7ekDu-kFv_LnSxZO7oWIyWMT9CkNIcd8hrBFhpi_QJqwXVaktzULMepWL0Ebw36IlDvSscVYliSsAT7ApOCpyO0IF1oUH7FD8S0mrAkH6ZLXRjVc_8f1OiYRjbSiVk_ANGlRCe8TwK1m0NEJz9tDg51F9yB1iXHdJZ6_I01PxDGREnJNtREvH52WQvtJy61dvyRaELHJlpZwwY0VcIDcJ1Z5ELS6dqk_hRUe7bR4OrKK_cGJT5X1HhlBXvirYfiow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
جام جهانی تاریخی برای کانادا:
✔️
اولین امتیاز در جام جهانی
✔️
اولین پیروزی در جام جهانی
✔️
عبور از مرحله گروهی برای اولین بار
✔️
اولین صعود به مرحله یک‌هشتم نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/96724" target="_blank">📅 00:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96723">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwbFnE5igPIswM5Ct0gA_CrFxU3OKb3H95qK3j57TX4QbIHoeXQIRygpvhN6tx7nPy6KBNjwMMmrrH-ui963_GVLzrjR_jRXxisNRZYj2Gw44vkMrisCR0ZYmVVuZcd0C1iXqRkp7tajDVG6cAAoNqrY6H8YzqMZeu0chga-iCRTP0qJLLyYCBVBVxzkIG4Iuh2JaTOIznBRvNdWuY6sgKeC5rHTip1bXTCyneekVfZXMGNIj7-fYDct01Pnv1PILTE2_KM5pizsDw2e9XAgMjEtLS9sc9LV0iZu87aqqWYbZE3_CXP3rHFQbhnGe6zK7TGRJR-iA3gbyPCtWkDf2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
بازیکنانی که در وقت‌های تلف شده نیمه دوم گل زدند تا از رفتن به وقت‌های اضافه در یک بازی حذفی در تاریخ جام جهانی جلوگیری کنند:
‏
🇳🇱
ادگار داویدز (۱۹۹۸ مقابل یوگسلاوی).
‏
🇮🇹
فرانچسکو توتی (۲۰۰۶ مقابل استرالیا).
‏
🇳🇱
کلاس یان هانتلار (۲۰۱۴ مقابل مکزیک).
‏
🇧🇪
ناصر الشاذلی (۲۰۱۸ مقابل ژاپن).
🇨🇦
استفن (۲۰۲۶ مقابل آفریقای جنوبی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/96723" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
