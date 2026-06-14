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
<img src="https://cdn5.telesco.pe/file/S2f7k9OsDcygU_UauoYw1PX4vlFWtnpEMQtq4FfE0Yu-3TW5Fb3-DVkN1IFkiDmzsztmSm6EKU0P9ry49aUoNw1tQDeNtTTL5FeKCcRMJFSBCyqvDLtdERLXjQA7IGjjWQge9bKWR2hqgeC_ht4DSrQsf6Y0omcJahcaEyej2lVtHfe-lgopqTipeMqb_G_kQj8saRuMv6rgLHJUc-8IrmoUQ3EumCxYBealmC7a7wR05mEqKC44vJ0rHpssifKf-HFnxBx89hFXtuIqOO8kgMNgle23fVzYP3vuSziNodsriWFRTh8N6kb4TI1hufTfuPwebWicsDDAxYy5HlUYIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 546K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 00:14:42</div>
<hr>

<div class="tg-post" id="msg-93071">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ژاپن دو تا موقعیت عالی رو از دست داده</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/Futball180TV/93071" target="_blank">📅 00:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93068">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvvgwFkzaGsP2BXNCJ4j-zaB_Tn3rvTE-Vi1ZyyFtKjUQ2oX1v8v7ZAOXConlRxpz4sIJ2b05J-fAaPDpoeki4IDplvaMysJiQcD78a8s2A5Ujagl850fTxLyqnitLl5ojqpU3TMKPVRmeu7vSWhgv3kcsn653jLe0KupK0tvNP99CXYWYseROZ0Ex8FyTO8BC8YR-xHzwOzHhBsABonTcPDfThjShcdxEVHssDn5VUx0p33Ys77FNHzZmcDj6DZni4ecbTxUsk6QKYu4FSlmiqGjQUJ8ezCPqQ48RKNWgaa2llegV-Q_CqUTG2Lmj9U-924yS6tVaky8Hjy8zyu4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ay2LZg7jwJYGLsa_EXNwKIzmc6J3l18PdgKBRmBaPJtKWn6Cm25-_v0ejOPMT_f6oGhLZCA8YEFoGOnWXsMeMqNMKtiRAFoOtZJBJvwfJeRFbobV1Oy4yIOe19jYK3iNbo3aBF9Gky_QdZVHVH3QybSbnHJ7dHT1xBQKxiCKsuDEKM3AXQ4R9ekkiZjX6BqVuvA_-YnyQQk_a0ehwnYTIACipgxeW-VOErQ7muj85-wKE3fsZAU02sQGYHa8lVNCqyX6T-zC9kdDphNn_lVmWp8REfIXH5MXwKQjIhVCNZTjwEVnn-LZb1DSMoiMnmBtCYRcickn3Mu49jC8iqgfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GomSLF8zzk76vDkle8mzq3jXkL2BvmUBEJg2NSK8ArJqWHOe9MunNypv7qhrSdOQSgqUVYbiyLIRX3tmd1XKtHaQME6PG_mvlVsDfR3A5uuZ0-qstiUxfmpaxlUaRcmwblQkuyixB9iDqyqcyXDJ5Ki79kTtKaX6NM2-cNe7QKUl0h9V_kOWEzSWVWY2ukwH7-K-lujs6b6ciwcbr_vTdMhLSoSqR9mUx7vPCdMRGNjgjl3K53V45iaSzeC8D22vQGQ4MdBqX7BzWW_nuwkkLg7zKaCXkw2d9N3bRsuja7cTnYxzhLodFEt5eaRj8GtdDYJg2xMPaj2qPo6Y5l8_oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های رسمی رونالدو برای جام‌جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/93068" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93067">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سوپر سیو گلر ژاپن</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/93067" target="_blank">📅 00:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93066">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">۲۵ دقیقه از بازی گذشت کلا یه شوت از دو تا تیم دیدیم</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/93066" target="_blank">📅 23:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93065">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Plgio1EnWOe5sv0EUqaLou5wMbtmt3hAnr0868wVroeTkQaBulVaDI4hxULtM2l7-6eJocXyo884dAugnOKB6_ljwICNl2MYxvAbqHZCu5TTzJIVqhXcVlQ70COP-o1KH3ROw4dUg-vfPLfO6vkVQZfSFvrWaIvq4D-me496mj5BLO5k9i_jj03WdKSleOfovUEjtwaQ-BSNE8PW8AjF_9s2EFLN8ZxN2KMd6L70PHIWPvZedsVEhqJVICJ2rnh_h2JmWgX3_-oyIu_C-Tm_VZYqFYnX3Dxjl_HFrPAFeTWhh34e1rWCWsKZnPRpxiHFXOl627yid-arLYGgOSf0DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لوئیس دلافوئنته سرمربی اسپانیا آمادگی یامال را برای دیدار با کیپ ورد تایید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93065" target="_blank">📅 23:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93064">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سوپر سیو گلر ژاپن</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/93064" target="_blank">📅 23:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93063">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شروع بازی هلند و ژاپن</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/93063" target="_blank">📅 23:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93062">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCOtNg94PLIGwRMyhAtpykWtva_JZcYBILy1s5ztDDAcrr9yUKuZTMJpzNLbPzEhE-Itxuo8tLER6qytF_PeFkbe1hnYv1WmFS6rJ5mdZbw0oJGxI3sRelLsEM9LHhVsIMjpnjY9QC_yMd4ME5Gp7wIMf9Eb20-SKSRlOTxzz6RcA1yru-oBNySXaS4va9Fu9waZjwab8JGoeUA_8Yq1yS5-yADc9KawD80iBp5WVmHG9Yzin5f5yn2PjF4sq465jOOntwEAccb7cURsL9e_OofAzbZ6qDcayBI-1jdOjrXSVWYsmy8I5QN7QC2CBOViiybpUVqejGpiiHha1CbDCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
ناتانیل براون به بایرن مونیخ :
HERE WE GO SOON
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93062" target="_blank">📅 23:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93061">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gffHd1oWXQPloG_-KFJFCKLgAWPVq05QRFgueCXYASrjxUVoLRN3Nc7UnkIi5uKEm9nEzYg_TbKlANHXDBM0Gzpaz5xEr6rXhHnYDldSbt3Ezz7tpbRm_I5wjG5hNF1_paw5wO3Uwz-TmCLnEVkQCXazvFoIP4XETovyR8tRVwXXGvMMkPRUJF9iA-8gr_pG9OM3FEVP6EvBd8PTcPxfn5CyJSHr92pNT9X5cS6Jcx9OXuIQXzmlHYR-dhE81MExff6SxlDykx58OGIpn6brZ4-KCJft-nvgQ50caxhbW92-SuBOeJnn6UabrdlOZBRdh-I_eZEl-2iGeuMAuqZuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کای هاورتز به عنوان بهترین بازیکن دیدار آلمان و کوراسائو انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/93061" target="_blank">📅 23:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93060">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بشتابیدددد که فاک بت آنالیز از بازی ژاپن و هلند گذاشته سریععع بیایید و ازش استفاده کنید
💸
@FutballFuckBet
💸
@FutballFuckBet</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/93060" target="_blank">📅 23:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93059">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mni-1W0eUr4Q9bsly7ezma8dvk5lzNIbCYiWhEPYU2Zuuh-LADsUoMcUF9il5Fpe46r3722twhJytGgmqCoQWSJr0Z4suFiPA8qIZh40ehaS0JID8m_tsEe53aQsPJOHphZAuWMQHh_trXZYdrUzi8cYi1EboDBG1eOXsXAs0a1Nux7nnbYD2DxWjXyh0GU5mHaMXhPRRWzoNpn33prXSnAzwjsabTq6Oo4o43BF64GzeZgbh8iAIUmnHsu4AIfgBOmaeb5UMMoj7hWJSvgX_q3eqxgjtHYZNLOMbIvvERVPKIf7beE9neFxZ29ju_bqIEd19fS7foZVQ_9QzZ5awQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇾
مولینا خبرنگار اروگوئه: آمریکا بدلایل نامشخص اجازه فرود هواپیما و حضور اروگوئه رو در کشورش نداده. این درحالیه که کمتر از ۳۰ ساعت دیگه با کشور عربستان بازی دارن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93059" target="_blank">📅 23:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93058">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXSpYgV4_Iavv1cyvRxxndVJt8lXxwnfqDOkMfoFStxdV9NiKqmThEvMESHeIZ-AC1xT5fFhaE9ao114ZgEH3PMkuj1WyG85ZX8A-OtiWj77wCsWH66jiQxhbgnEK1Pay-OCigGTq9xFW7kB8Dws2eh5IAoC35kBPZCVEyBgYOLqsCVeO204Xc0M7JCcDqkLi1uRHg5ZK1dIBlPiCdqw0ivDkdMPBgeITuFrYiNhBuuMpJIfWwLGN7YOoRUMjcf45dgW2JkqMzuaxtZvqGjXfI-wHPfkMOfhxzoqguCJvmm0W2q_repmwr_cQMknd1jykTmNdHVcjUQaxRVi02r84w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوش و بش یورگن کلوپ و توماس مولر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93058" target="_blank">📅 23:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93057">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0240278273.mp4?token=oEs1KKjoLUKWyg5OqlejSpdF4eBiNUIOQ9MYT-D_B6BA3D5OliH4EQWxOjlFg7UGmMxMlVDsfq9pF9BRVwFsFa2m8zFzU6zKcLU8BvQlFTlNB7DKsQNhMBvTcLbb4MnhgaNeXYIZVFudihz961rbeDd9de1JRAwPWxKmgvFfikRHgUnLkX0yvJjlMFVjpA58qSYEReuXZ0UcKI20kjV3n-uUPoeYy2bKvtGKSchuCNjHuqNybg8w3pr3gtyE7KjyzwowRKZPByi2JxqxxFHymCHeoYlm8Jcojpad2MJB6jasENJUFcDLyIPUBXGkFkAbZnmSzL-TY91u-YJQMDtvBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0240278273.mp4?token=oEs1KKjoLUKWyg5OqlejSpdF4eBiNUIOQ9MYT-D_B6BA3D5OliH4EQWxOjlFg7UGmMxMlVDsfq9pF9BRVwFsFa2m8zFzU6zKcLU8BvQlFTlNB7DKsQNhMBvTcLbb4MnhgaNeXYIZVFudihz961rbeDd9de1JRAwPWxKmgvFfikRHgUnLkX0yvJjlMFVjpA58qSYEReuXZ0UcKI20kjV3n-uUPoeYy2bKvtGKSchuCNjHuqNybg8w3pr3gtyE7KjyzwowRKZPByi2JxqxxFHymCHeoYlm8Jcojpad2MJB6jasENJUFcDLyIPUBXGkFkAbZnmSzL-TY91u-YJQMDtvBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کار جدید حمیدسحری با کپشن:
آلمان 7-1 کوراسائو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93057" target="_blank">📅 22:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93056">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLvQAiR3HfgNN9BJvUUKS_WYilGEscoL7jwRs-vYxASUPbOd2QbCr8AVmNKOkViwbwct_02Z2lXgPoeFeNm6Dg3aOLON0Cso6MXiXfCM_qdydD7PNafcDdSYxrLVeXRA7-mJYZDAi2h7900AUZKkHpEkwxJZEQ-IfFP2iSlUvYKM9H-HTI2w68lQ3T6gsxR0mKoy-t1vLj3U5T_Ob_3Pq_LwUGc9wMKysUoQEq7a5M0nK_vRb1QnxflWEMbhRZAgB1bzqHg6volIO_cqyNcekAG0YdR6Jae8u4X3XLDDQwzPUFLPMsBQPoVAxFIO3k_H3jg5AkjgqTkTVASdsx_ZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلمان عزیز امشب ثابت کرد با این حجم از قدرت شایسته قهرمانیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93056" target="_blank">📅 22:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93055">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">➡️
فصل قبل:
❗️
یک مدافع چپ جلوی یامال بازی خوبی ارائه داد: کارراس در بنفیکا، که پرز جذبش کرد.
⬅️
این فصل:
❗️
یک مدافع چپ جلوی یامال بازی خوبی ارائه داد: کوکوریا در چلسی، که پرز جذبش کرد.
⚠️
پرداخت بیش از 100 میلیون یورو برای جذب دو مدافع چپ، تنها در طول یک سال!!!!
﻿
وقتی فکر و ذهنت به جای تقویت تیم خودت، فقط روی متوقف کردن رقیبت باشه، شایسته موفقیت نیستی
😉
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93055" target="_blank">📅 22:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93054">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0jQjAeWtYs5dItrru4dRuCfIpJCSjh7Nm4roOU2sOEAu0MPm8bx5EewS03pJ8QVnOxoxQjhHNWAfF883-7bVDhTadWby9RnGOm2sI-MCBX4t1WIWvNCQVUV4c2Snt0zGaT87Hc7RUuQGbGJdFPyjHFhl15MFT7Ea5LoPf5qRNYfEawdSu-j-QIE08rHZo4TvBK9tjULNsFI89iJS8KNVuo3ecULKkXiib7ZNeIz6xX_HMctinDC1-4CCQZdX_Oq95Muo6mIlXNotCj--GKq20qUmZl2Fgu80DRZGbJdGbzpp0j3kVNQoXlVwE9cYp7uHWtb1ILS0E1l61wnAAHQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از خامس رودریگز مقابل ژاپن در سال 2014، دنیز اونداو دومین بازیکنی شد که در یک بازی جام جهانی یک گل به ثمر رساند و دو پاس گل داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93054" target="_blank">📅 22:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93053">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbQ4p9kd6yl9xHrABiszmni1bDh2DzrcryG1cE_DJ18FuNT9ThRNpPmdZYx8rJzeYTKkkGuQgW0AKRqt2FGoopUxLGgQDnAjduOo60eehW2l9vvgiYgssBjnAOeKFdmQolT1RPamEpvQVS7OwZ7TbWSlyBhE3e3nWqivqhlFmPmMfrzz4GrT0PaxU8T1tqVFuoADm6ho91HzEGYIajqa10Xm_KFi75TVD9sWt1IIbAPZZfLwMfydOw9KTfdu1ZeDxPFL5XeTjk0yJJl5jmUQTwb8npGs3g7_-wQg8mwBJHnT-ZXrBm856AJK6c_dmdJoqK1tQtXew5j71gKrdttrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تیم ملی آلمان در 10 بازی اخیر خود در تمامی رقابت ها پیروز شده است
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93053" target="_blank">📅 22:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93052">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پایان بازی | شاگردان ناگلزمن اولین گام را با تحقیر حریف شروع کردند
🇩🇪
آلمان 7 -
🇨🇼
کوراسائو 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93052" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93051">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icSj4IH4GQPoqtx0KZoWHOUazunxpbdUlh2HMibHTaBPv0s_4BZ4NjPlcBzqRJzeopyLrQvc1kEvHRKKEK_biU1EAkjMYo4O0MidY5UiPGixpSsYyKqkikTVYpBFZHuWxckPpJGc6DDKjafw2m3jqcup1pW9OQ7Taz3g3kYOqW9FLtji2TpHNHoAj2u7bxOmZ9nKyDQ1QLO99zMleOJXyaTyT3ilbmrA2n3zfj5QOcw7hLzdFtC4AilM-aMUbeUwC3evGwqCnUBNqSd4l2mL2rpTTKkHaqi_9J-Xs2r3T2wg5-YjBBXnFUdFuIeU8z-9XyQwJJ1Pkg48btdbEVpJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آلمان جلوی کوراسائو ۲۷ تا شوت زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93051" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93050">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
#اختصاصی_آبی_تاج_اسپورت
🚨
Coming Soon
🔵
🔺
💣
💣
💣
✅
بعد از محمد خلیفه و بهرام گودرزی، سومین بازیکن جوان و ستاره هم در حال نهایی شدن قراردادش با شخص یکی از اعضای هیئت مدیره استقلال است.
🔵
مذاکرات فشرده با ایجنت این بازیکن از چندین روز قبل به درخواست شخص تاجرنیا آغاز…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93050" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93040">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D29-yxYNJuCOqV3CVzWnyJDE4ycgmrQk2wtJb8xdIfosUSNin6UQfBmV34d72dxkWyv7Y2qdAWMNLMqGlcyTKzAtzvpY-67gQbJMM1EUUGQmD7TAIKCcpuvzS02V7oNczLLix-df9yQ5tGza_O83B0oEp79F4_3dxccqlgi0LsvYKZQ6KQC2dQP7Quwwhm6P1WvN6VuZGKwOFAyrKjWP25HZ2IIpi0jju0AxI3sWX-lv2bM5Kg-xZNJCKGEUuBH0E6gB_nhalInDTm_LRamMm8kdudftEGaMHy8v14rstzTLJhBXsoKouwopjJ3Sh-VWe61LXzsAoIDs_JyKfg_H7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAL2vkfTX_cXXXulVTvC0DnZ-PHyjkY9NrPHugyjSX8Sbtwt8U55P-oje7W8Y9Blu7oJedd04EHnQS93naAeT8tl3zevWHmo3Fo-dkg5ynREa3BwjEwWxcfcdsRfE87NgaAbIcM8arE8Ji44P1nvP3-DAIB9xC4B2v78V7T3ACRWm4hem9IvSjnhgFa37YjbfU9nyL3D_nqJ0Jhm1XRBH6bHeE3BuzDCj-h28P85DEkZRc5gWmh-p4Cp-SEaFettJF6NF5tFl8lA2d2hN6wLbiLYXvr7mybumBHssDU1xveL5jWcrRNI8Z-kvNPzDgn4-nf-62s6SsIa8a4ShYviow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dtmaB_1MUnEZjdvbGOBQK1hKe3vqy9RzUaPfe3X6-GIKhqsMpcZleaCAXL_gipELK4FDVDEp45bpFhoGxFQHZZZEsfOV_FDqBYL-dQ87tN8rUJP8jbTHuB2Eiz59psM_V6Zm59Gw_3VZHzEKT_0TMkDDgiQh8w-bA1aSSrgx6fZIXLmKj1CE7s7xwT3jJw7SJoJvMAIXMIawrSa55fK8lFrPgWvG5MOlhg68Yt0EPOQnhX6OAJDKwGZXH_AHCKeXnrggZ5yd1ICdSjfZ5qKIBRjORDZut6-hbuPuAqZ7lZnNmHZQ3WNm5Oqj6rcVT_sIFa9tBNL3KnuCCc_mhEIDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3MXbFCtzS0AWm-3ZQaaXmdFXf7_uND378E0KqCIhhqjS0hi5BmODiz5t7gHbn3eILD11ToZ7pHMYrYv1Z0aFWjkwjuLl9xQ4fosnncMH_sQq4yMHuq8RwZ_Sq4M78bKmchelHay-5JYACvqVxDR9GwspjU2W4tVDqE1S1flHcrpTW3eX-Prn6xt78vHznqtfaxioYcrczOTonPU17H3Huyf3JNQMuCR6aEbeD_I1fj7KyyNizDsUBHrdyPWiFcbskNWd8prMrn1zULsxB9bSdLm5jbz2kWe7jlQJz9VxqHv0RZ5Tlns2maFJ2Dg-a46pGzvBZtE578lSBLazAURew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kE8HsH7fEOGjpUoDsVozz_U3SiZCucqsJ8xwelqNFrncmtLPajyz-xazaBwKpHfMf9vJiRxEC4WgpQpuqb5dMMaU4lHHEG1jn6nXRod_WKmdxBP4ndr9GMwA06c7MrUkgOv6FPhE5Bfy4odvBaHxXz395vingLRIPzPKr60dvXc0Ou8kiNKREEva6z2nxYRz9TC0ZBU7t9vPdSvHZ29b7ObFl42uVD6yIxEeo5CIMIVRgaZSpz-5dWnA6_kjXu8uqTzGZ3kyJ3Pfu930nQOP3KLN9p5BEqrJBUZAnvR3mp6PKvioHIztF_x0ggIdg9lKXnoXsa28wL6__LlnjC1nIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ja1BDJkwcvRELHNkbGoK4z5yMfKX0vOjQwrPJ8MyvQd87QF5CiXypqJkxAIUPkJbumOp1ZeLYhh5K0ImQdj7SOOn2L0oMmqpwCDwiyZuJInTuOKG4fbYc9pl_WjG6YbIdnOMxvvZcn6PIoPktbrxgznaJbANcxhXIdBqVm6knltHlXtTjCPqXlid0rFHoNtHlZsNhlFrD3E9U75F_ugby2-Hxgd7QO3pu2PnU0zh-Tm14Z_mt1U-pSbDmzUvlCVCNyglyNUV2nuM6DuxM8GA3fHQHMcPxCGcGAMUhT_lSwS4z5goKElQxLC0dm61IkumJzSOZIOgGDKsyqOZ_kON-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qy3eSRsLYc0nTHok3gSGAAK-N6wh3VHkjqjKon46yEPz3EoeGWx3pTAZM6eb7Cu9Asjo2EHxrCQYEIDk0SM3BpBOXkjJNnhJm4iO_3_n0j5eoa7kRz_04VOKt7Q3ku6q3h2aiBraYj2Z897N3YHeLi4eoJbES7xBj7GGuYbKYNtTrnwMVS63mJc6GcOiVheWjcFmOcjATseflpmrYIavcu0KCWWuGl25BOjPwmA0gdjIritvM_3syJ4N3B756J2LJn9jM4DmFfX940u25GuVrLm8Kh6YqL2r53_b9D-KM8Cz2zZ7yQ4c3t3h7iaTl_DyZ3P1CJDhm_dV1WnUVd6DXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJmJElSvNHI_YG5eWDZy4SqZCpST3bEga8a2DAB96NDLqaZ7Q6YWtWJhSIiLXLx2QnoCTev7DzgFbA5FanIyswCtVbgE9DvTpXcnuqcpPA6cIQr7WSeCSsXJDEINrJVUMHQNtjyuVKOw59dQpf5KJp7PLTkJzbqrZLzNJzwxCnfDjQsczjez177iYm3Z9NrjMVzFKmyno9_32hm4ipe_ZsDhZbompS8SIQvosanqOLPMScEbEO9gMGDJFDRYVhy7OWMG924f634G5QflpC2OxaLf-90Aojaon5T0WFoand-wU3zkYK5zfvQGLhW4qSK43QoRko6iprTNH4CbFefZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vbmq7OXWv60-8WLbDutJ02J7OOqmljqZQgT1qboQc3cC3EtChjHV2UuR_SLrSaZeYkqOtu35GvBHIQPwVRPXToLGDzP4FGnkyMzhN276sQOxwViRDDsACt8eFpmQP6OeqxTdc7aoYEzcHhJoD6p2EzcsDT_cGe3v7MGlsqxq8pWGa-hmwe5a7XsblD4gEoPLXnmCsheBpjmOn1g7EnZhvCpar9ed5vyrVraOTVmOXlYoKzjz5VP81ZnQ-Gj1A37KuO_YKi9PTWU58a8nIPxUwE2LMaaiWwBwPoxq-MlamhLyMfdUZIiUAx9c6qZ45mRUopPy8AG5vOsPhBzUs6BQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jk-Isi5aRSQaGPN0UXpj7hsM5eDzI-dQJJDyzWcbM7xBwM9sMFJUnIbkgU1O_2pU1daCBoPAHidedLWHXLi5a40L7H_q8J-iDHJJn05zuPW5OkuynBhxGAK5ebS1uC-uGHr3DOJFtyInTa6ZAQsPe8R3kpps9fQRewMeHi0oura4ix50YuZvYnH6yarfkzQMGo3_evaUbn7qaQ2K7LHCB_xG6CNBOAB4sO7pVChTI8_cWvNlIH2-z5yhKN3Cj1kzdvtoLv-9zMpu-bGKO14kegd_lkGL9LCAQ9_EjWVLoQFD7RjoJLq-9DITXdMn1EvmX_6bFM-b4Wu7opck65tIhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جذاب برای نیمار فنا
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/93040" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93039">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArEezXPnAUO4fo6kTlr0V4cEggscbQ5JEtWqYm2gPcRhvFg4z21YIiDmAx25f1_VUVteCiw6_rukcfriTgQAhSez8Lg579rlZdeTxYv6ihLeCoW_QfsOzVBKJsXkAw93VZzK912CVOg_tI6pIjHVbmi6Gjd8HNg33LWauRYhxldkSPDNbDZH2hH9MmOXoqSK6jcAvh5EKJ7nil6wxtqRNqOAnzmpJ4FfK3JS2TqY7PBLk0ok77oMwqU3A9XEmo8UsKFkXcy8fRqhyCgwAa5ii8chpfn_IsrBkLSX8wczxpAOlGyx1IUrQxDkbY-I6nL9_1prN2rxF5j6a6i1cWAdiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان بازی | شاگردان ناگلزمن اولین گام را با تحقیر حریف شروع کردند
🇩🇪
آلمان 7 -
🇨🇼
کوراسائو 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93039" target="_blank">📅 22:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93038">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVCU_WlA4K6iX7rnAI5w76qNdmPjCij3robI4hAqestbQXmIb4G9q1BNJs21eFhZSbfCPEAyzqdwyvJ-48KUtJP6mew3Gu8uFTUq_PsK5EY2Ifh9NBAPHGsan5mgs4Q-gTBF8bA0hN3ZBuODN_fqMkvoNIwpwIbvBOGGHwQKkyNkP5-InBCgMKCvkIcrQ3_jAMX8xNXzifKh68fk32byfz9m_h6zcZcnP51eGKiPA_4Um2NAAc2vSNKrCBN3pdK-dZW35m0vfKWhYXmEU-mlqk8Ca_26jiH7mvJQ3Tp619BDQDXJs_yvNCnDbYIQawvBE982wVlAxaYUlBwJ31oYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🔥
🔥
تیم ملی آلمان تبدیل به تیمی با بیشترین گل زده در جام جهانی شد:
۲۳۹ گل —
🇩🇪
آلمان
۲۳۸ گل —
😀
برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93038" target="_blank">📅 22:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93037">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هوادارای کوراسائو دعا میکنن این پنج دقیقه هم بگذره</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93037" target="_blank">📅 22:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93036">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f0490e11b.mp4?token=Y4lRxVEOfhKCBmug7NblYaHFv_QWkwelXkPbW2jz0Dj8XcoXkWQtHATItSDRHc_-aJMSafYjHJmKoQr891fT9fj_8syGAbVsqWv4ymv0VOjTgm91t30auaB1hN40N_zX_-fx3QBi0kqTfcsJ1qwMKpOE3jDGBNuz8nFBpWWwwv6ybiMKUZJTRFXU-3CJqIRDkG14hRDO_qFIqLVGS1YDv49SmraNk1PfjxIxnIZEWUVbFs8BJRWjSEizRy6C1D7QJn6SdsJaC7YUX53es-HFgEQKELPEAk903CDWt0yseeEBUFdtkR1y5EPRwX-MG2XO3E7cOc7Z1xHdTrgrwv1fAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f0490e11b.mp4?token=Y4lRxVEOfhKCBmug7NblYaHFv_QWkwelXkPbW2jz0Dj8XcoXkWQtHATItSDRHc_-aJMSafYjHJmKoQr891fT9fj_8syGAbVsqWv4ymv0VOjTgm91t30auaB1hN40N_zX_-fx3QBi0kqTfcsJ1qwMKpOE3jDGBNuz8nFBpWWwwv6ybiMKUZJTRFXU-3CJqIRDkG14hRDO_qFIqLVGS1YDv49SmraNk1PfjxIxnIZEWUVbFs8BJRWjSEizRy6C1D7QJn6SdsJaC7YUX53es-HFgEQKELPEAk903CDWt0yseeEBUFdtkR1y5EPRwX-MG2XO3E7cOc7Z1xHdTrgrwv1fAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل هفتم آلمان توسط هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93036" target="_blank">📅 22:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93035">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هاورتز دبل کرد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93035" target="_blank">📅 22:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93034">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آلمان هفتمی هم زد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93034" target="_blank">📅 22:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93033">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6OTy9zDZKxodWNoxqmImZusRfvev3YlGWhxpqS9Qa7HiUTghl8gqNpP_cZPET2zwl1zJEmcI3FaH6LUwzOdTf7HrP6v2Ejc1xeoieBVKSiMZdoB5pbf0ZWDY3eG3YX716w_faItKaDpRQG-2kj-uurlObEYFRTYav-f5idJOaIyvEVHpEv91wfUuNlGgimZ3uMNtsYPelV94ug0d9Hhh-85aIbxGwlZhhbj7AeOCHW-7NGv4C_8nnWkXvlVvVTXSBht8l3KEUiLXiIrdbCa5twcKlKLvehTzyFI02FPujsFOcZ2CGWlFig9Vq_NO9sOXwyq_go6sf-la9Ga_a8BHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
ترکیب رسمی هلند مقابل ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93033" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93032">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3dc1080cfb.mp4?token=CYqJQers1cu0AOlk7FgeCnVxBcxDUBAswD9dQvWsIkk8-e4BoTbVkH1OvmVYtcCD_qmP9tJtiln8dB7lK-hnDaGrde_LAWcxrc68sNuuH59cNMYdzXbzm9DDppvfKfO5IBCUaNwI2Ftr7nZFRUy1DwcFPkFT2G34rY_G_2Qa9wJisjTh0bO4v6-grlMrY-ZDjBYyKYJDpNmkj5QBgxUV9ybnzljOgp7ulFu-L3Gt6CO9HDZrPscD8JNEAEXzGCFRgtmaZEcWLpUawWfxZYpLCmIR69fI445CSAKWIQ4nNNy78z1KPZVxouh72Rvohuwd9eSA4-NVTk25W6RwfqXt4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3dc1080cfb.mp4?token=CYqJQers1cu0AOlk7FgeCnVxBcxDUBAswD9dQvWsIkk8-e4BoTbVkH1OvmVYtcCD_qmP9tJtiln8dB7lK-hnDaGrde_LAWcxrc68sNuuH59cNMYdzXbzm9DDppvfKfO5IBCUaNwI2Ftr7nZFRUy1DwcFPkFT2G34rY_G_2Qa9wJisjTh0bO4v6-grlMrY-ZDjBYyKYJDpNmkj5QBgxUV9ybnzljOgp7ulFu-L3Gt6CO9HDZrPscD8JNEAEXzGCFRgtmaZEcWLpUawWfxZYpLCmIR69fI445CSAKWIQ4nNNy78z1KPZVxouh72Rvohuwd9eSA4-NVTk25W6RwfqXt4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل ششم آلمان توسط اونداو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93032" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93031">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آلمان شیشمی هم زد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93031" target="_blank">📅 22:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93030">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQIUYvvCSejeE7UgEE8WsyLugg-Bpbn5U5YQIL2ze_T8JcNlDWr8IAXFTtsuSJfguud_CQNpkU9FwRgw2e51GKnpStHAZ29J1dtMNwpxB6a-a5Ou5ENcyd65YywtGyaZGYHoz9LBIaJZIreC_sPNrvvaT_9wauIPcLX37s3rQTyqMgcrzI20PFetr9hSxKxy7jHLP_2n1yTERvKUMjYZq_MkJdIb89wdsjBGwa4j6xjRFn1R1IAT1So04bRep26gfbe_kcu9UEuH0Jw4SnjZyhq2szgrET7YEFKMcrpi_96QEmansxQCWbar0tiBVey6fEVjxgbEq4ZApz_QJfv6Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
ترکیب رسمی هلند مقابل ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93030" target="_blank">📅 22:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93029">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0rZEm68Jjzm92CnKBxDwA1vPg3u5h0E6XaH2AUmCttEjAjIWtw2e1tWZPX2sxA5eiY7RM3c6kdLiCknNndb8o2XmKQawKx7DxlYr-GHdeGKwtPo8DwnoGixk0dgrBWokXSAMDT5jgcd2Oeqc9SVG4R1q2vZkQnJK0YNEIAEt88JEWYOL97HuyuaZJiwDTSF70-eit_v4lV0iIZTzMOneHSogqhxZzfeXs9KGXz3Kj_vlV8XT7YEZ3HlMXT9cpQ9-b7WNuvPFJnYGH6_XkeYd42-v-94S_GcXyXQPuNWskkKCvGIM6kfUF2a7-W62QEp23Fjyt28rrJ8l10tFTZyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل عجیب هوادار کوراسائو
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93029" target="_blank">📅 22:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93028">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5399ab6b00.mp4?token=bNGrZVxMbxe1Pkkwk75TVXLiqGn3i7EXu8ZhzICiKYVeMgdl9zJKZo4-M-o9HqLm8fO5fx_IY8gAD0BMaXToYaZjE3loURRLSbOoJQ0vAj5PkFZT_cILJnezFaaPqFXF1PacfoGz_CaQYPpkWPBelS8WWXtFcrsr5uBj75H2FTBCAmeCSD3GiWiAVlV0pv9UY7HKx-1aacKgDfmdQfclv1jtRLc_GKq2ux7nPkM19txE9ijnEKVJsVdgJ3LTMfAhZpdL80Yfn-4Na3vRefzPnK4kJmkfkcFxO9GLzBffJucICX8brVdi-r_jd4i56sNMFLidfB4UhWMifbWyjzDY4J1zWxXiuDpjGGlXIOpsKA46tFVG-brGD54ntng1z-PiFUl-AnHTfBkKOQLoPn6S1L6O6hagtRU203EtJK0tAhghDlAZxICHqjy9gOTPtNrQANYYTKqwuSnEX-MPzE3TsYHsQ0jA1dVoBHsyP7xXzFvRqnSmcjFGOr5RLXOcXQihPyYgNYJqtm10PuzXQz5_7-wI2pK2jd-cBJ6BArjJQhjkIukPE-4ZCtD7uU5PygXmQX_x4sU4466qKCLWilj4BcIeyG3JzUEjyvxCbFeHu6IxL8hqTatWEu6Hj3iDzN3uIDnlxN4Zoboa9MyZvdXXe0zV57PuvO05maGqdrIQXrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5399ab6b00.mp4?token=bNGrZVxMbxe1Pkkwk75TVXLiqGn3i7EXu8ZhzICiKYVeMgdl9zJKZo4-M-o9HqLm8fO5fx_IY8gAD0BMaXToYaZjE3loURRLSbOoJQ0vAj5PkFZT_cILJnezFaaPqFXF1PacfoGz_CaQYPpkWPBelS8WWXtFcrsr5uBj75H2FTBCAmeCSD3GiWiAVlV0pv9UY7HKx-1aacKgDfmdQfclv1jtRLc_GKq2ux7nPkM19txE9ijnEKVJsVdgJ3LTMfAhZpdL80Yfn-4Na3vRefzPnK4kJmkfkcFxO9GLzBffJucICX8brVdi-r_jd4i56sNMFLidfB4UhWMifbWyjzDY4J1zWxXiuDpjGGlXIOpsKA46tFVG-brGD54ntng1z-PiFUl-AnHTfBkKOQLoPn6S1L6O6hagtRU203EtJK0tAhghDlAZxICHqjy9gOTPtNrQANYYTKqwuSnEX-MPzE3TsYHsQ0jA1dVoBHsyP7xXzFvRqnSmcjFGOr5RLXOcXQihPyYgNYJqtm10PuzXQz5_7-wI2pK2jd-cBJ6BArjJQhjkIukPE-4ZCtD7uU5PygXmQX_x4sU4466qKCLWilj4BcIeyG3JzUEjyvxCbFeHu6IxL8hqTatWEu6Hj3iDzN3uIDnlxN4Zoboa9MyZvdXXe0zV57PuvO05maGqdrIQXrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
پشماممم از جو فنای هلند
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93028" target="_blank">📅 22:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93026">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ae46c9a9ea.mp4?token=sH4JV5HIt2d5z4x1VbCnyi4fCFr84tJOLiT1C-QuqV-GVDk3TVl3A5JPyza3DUhGVLxX-j7V3Qj2zKQzD-zThzy58oEskoAIjRULjH28AHfoNxp7gBgOtxBAa_M6obW_LHGcFdCoj5W-M2skz11WhpoFXLpiAUCcLB-a2n95GpLqAWl-HMaeu6UG6T-UurW-MH-mEdSjR6k9aS2ElQSR_hTDn2rHw1qQDqNdfeB0td3zDe12YRty3Nbqi33kj2uSiKbL9mpZ-OuHmRhqEyYEnwKZ6FyEdVBIiBH-Hg2bWWbYKARzh1iDDvUYqSSDqXFsA1ymIgMSBu0tlX3bCZZh1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ae46c9a9ea.mp4?token=sH4JV5HIt2d5z4x1VbCnyi4fCFr84tJOLiT1C-QuqV-GVDk3TVl3A5JPyza3DUhGVLxX-j7V3Qj2zKQzD-zThzy58oEskoAIjRULjH28AHfoNxp7gBgOtxBAa_M6obW_LHGcFdCoj5W-M2skz11WhpoFXLpiAUCcLB-a2n95GpLqAWl-HMaeu6UG6T-UurW-MH-mEdSjR6k9aS2ElQSR_hTDn2rHw1qQDqNdfeB0td3zDe12YRty3Nbqi33kj2uSiKbL9mpZ-OuHmRhqEyYEnwKZ6FyEdVBIiBH-Hg2bWWbYKARzh1iDDvUYqSSDqXFsA1ymIgMSBu0tlX3bCZZh1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل پنجم آلمان توسط براون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93026" target="_blank">📅 22:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93025">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ناتانیل براون گل پنجمو زد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93025" target="_blank">📅 22:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93024">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلگلگلگلگل پنجم آلمانننن</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93024" target="_blank">📅 22:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93023">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">📊
بایرن مونیخ باشگاهی است که بازیکنانش بیشترین گل را در تاریخ جام جهانی به ثمر رسانده اند.
80 گل - بایرن مونیخ
79 گل - رئال مادرید‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93023" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93022">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کوراسائو گل زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93022" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93021">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg60JmXiCx6RFjTwI5nYzfRWcKXPTG02u12Vzw_OArQYP6KyGWklXBIAt5JHiNMBzELmQvO5lTzPS-2qrlSeTZd3vditTwua7xLN5P_fZakqPW0lMNq9gV8_24K-CQPEb7ENBwTFr9ovSwuxyjlBL9DuVeQX-N6XkInJZAlGrr-I3KHcO3ToY5KJoKQNWxSFfSs2Ya-ay5pLCra07_pNGfAoJMnDRGtgRfJEDprGJMvImZC7pe9-BstH6YOoHRKtdNcrWEc_zh3_P1t6tgg3pkkTnWK63LBPkYajwqNUqwxE-RenXsnvyIYRSNBuQ1woXGnEaAIKCKsBy1vPVGpIVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار کای هاورتز در جام‌جهانی:
4 بازی
4 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93021" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93020">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kujou88A9MidY0OrtF1IftEoTcOqnoI6TO0dEeld7TC-fxqHW7CMbEMlIQ_0dopDycRRPcRBYotbBiYkeow8DWK6r19F2zgbMkxGn7VyoMRK3QSlxrkrS_u-DJLT9ViNyH6ANpEER-2DVKkrWMEdZZ9XqfttHjBgzHhHSpxOdty5J3sfWLay-efL8BanH_kayDX7AkCcqXTDm-hyGmuHSQc12HhSybBmYcoi-9-FaFBhHlj-EkN5zMmV3FJvQjvAoiJOBUG4XJg9H3f85JTYNt6THnIAAGX2_PzVm5dqBwawQBr7QIq-yL1O3Uocz1bIEinrMxgYxEl64KFbKj3bEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اوه اوه
😈
🇧🇷
دیشب موقع گل وینی یکی از هواداری برزیل کنترل خودشو از دست داد و یه لحظه ...
⚠️
👀
🔖
کلیپ کاملش رو داخل ربات زیر گذاشتم
💥
🫦
🖥
🔞
https://t.me/FoootyHub_Bot?start=HyU5AoEy
💦
⚠️</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/93020" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93019">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سانه چجوری این توپو از دست داد
😐</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/93019" target="_blank">📅 21:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93018">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سانه چجوری این توپو از دست داد
😐</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/93018" target="_blank">📅 21:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93017">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBkCPE0n_HkkH0bGgcsjbOrCRTgeaLGHhcd4fUOpx5tBYP55CgOrfeufZ6Sx4gNnVpGI3oUDaujHmn17GaxwR_TseAm2SoUQwJrdln15PwMUvtxeE1MdEBcbICLoBczUffZ2XNyCWt1e1Kq4BMp8pAyrFnYW9y3TOmonLmOpd000sEtvbQBqkvEyT2fbdk4qlYF3BaBuYKAZhh7CPN9GD9LrCXIL7XhjgnHhIzvb-flo6yPNMzSw0ThJl9sGuPnIUA37N9h_0gt49XvRzl2vcmFXl61pN5PABIMMiz8e2wvWdcvLNXVUVPHooz8Lg21Y5d0YaIhRk2e0OtHi-RiQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور هیتلر در ورزشگاه برای تماشای بازی آلمان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93017" target="_blank">📅 21:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93016">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/theusWaZ_TYax9nJ5XCfYaCsnNYlVznz5UmBObslk8unS-9KINphI9ibRGeezyNo6gtAQNMAN-Bo1gBriBLd1ub7oEH2sateb_a62ze8sRfOKDknDbZrbnHnLKl7uQiME23Y0QlXEb-SKCspwWNBoetzmNCo0vuOhzB6oTzuBPaHAZMZVY5NAQztjp9SzXfP40kHiPL6-DX0b2D3ffOoo5HPnAPUkVLe300f-cN9_Jrl-2SXIuJR6QnAuDv_AoiQBjKNJXu6CFsJwqMDoNtkUYoHzTInqgsunpENjZL9FJz5Y5Lrjawr141OpmOgzYxvGLqW9tkOMXHptvQELnZc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
🇳🇱
نمایی از ورزشگاه دالاس قبل بازی ژاپن و هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93016" target="_blank">📅 21:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93015">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b7e8323f65.mp4?token=TFtEQ5gSQ2CssaqMsg0uEzrucd9BJ-qk1zp4bM3qv2M8SThCXFvO2k0rdcUKuYx79qLLsg2Ggg5lkfZgjtNxP5wc-Yvv3_g2ipLsKX7WifLRVhNAzhCLpO_VI4lbwevd7NX7oWh7WA87KyOsIsoYUiyP1pQFQnxyLn6TluFlVaI3xUlViKZIkO91wZBTs8BrdAjmNtHc6PLyR0TZgHO7uis_5BlE7KqEQHaIAdLBuhtzYi9Re0gj_8T2k2inm-ATVTFltyFNVuQtJWlhlR3YWdajYx4nR-ANcHdOF1Ndr3mvkhVWDuBmb_-Fjc6ZCJTd2LQUpgfbuc89ncAkwg69Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b7e8323f65.mp4?token=TFtEQ5gSQ2CssaqMsg0uEzrucd9BJ-qk1zp4bM3qv2M8SThCXFvO2k0rdcUKuYx79qLLsg2Ggg5lkfZgjtNxP5wc-Yvv3_g2ipLsKX7WifLRVhNAzhCLpO_VI4lbwevd7NX7oWh7WA87KyOsIsoYUiyP1pQFQnxyLn6TluFlVaI3xUlViKZIkO91wZBTs8BrdAjmNtHc6PLyR0TZgHO7uis_5BlE7KqEQHaIAdLBuhtzYi9Re0gj_8T2k2inm-ATVTFltyFNVuQtJWlhlR3YWdajYx4nR-ANcHdOF1Ndr3mvkhVWDuBmb_-Fjc6ZCJTd2LQUpgfbuc89ncAkwg69Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل چهارم آلمان توسط موسیالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93015" target="_blank">📅 21:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93014">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلللل آلمان چهارمی رو زد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93014" target="_blank">📅 21:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93013">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گللللل چهارم</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93013" target="_blank">📅 21:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93012">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بریم واسه شروع نیمه دوم</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93012" target="_blank">📅 21:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93011">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENa3Wtk6jwnSJPOGmSdDDlc7wqEaANghrLwUSyEFt3Y-VRnhwULun9HR8qIeamHfDEXh6rDZwcxbKjU6AAkBAOfTB02Al_5Sx2GVeG1WDfFWotKxj0yE74Yi8R-mJQqhDleVB4uOZzDBAiB4eCpL0iEl8fvCGEtj0xTunnQHYPOsINmvLt7wIPwxnV7M1QttjkLBlg73TqgpOfeN0SthZNyNA147S6cl_6pHgb_nP-O98jhog7Hdvf8MpZTP8JPy8xAFh1If7d6g_rAHVg5le0Rl0n2PfmxoDdlhgDyxhUWjgsdRFCbubL8075zGX1wcQ-04y2M0JIMrDepdrVuC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
آلمان برای اولین بار از 1 ژوئن 2002 مقابل عربستان [4 گل] در بازی افتتاحیه جام جهانی، 3 گل در نیمه اول به ثمر رساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93011" target="_blank">📅 21:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93010">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfF3x6-8yYvyqbpBsSEuwT31NtBthbXDBhBd7f3oV2RQWS-JtsJVwMJgQEaYWDLJlc44KNzxdaI4CSZpxonI_Fw9_SnzD038iCgsCh5yg9VySwvFHjxezPDHB5Wh_bGcZqON2zV4yMN_YcEZ91ktkauNMlPVtSMRtD_Kwqwx4LMeAwT0l32-8LrdsymlUCcQGAhX6su2IY4pacdvWZLH7CVcYkdEMGPcor53nO9nxkf8uelvE-TmI1SI4VcCUGf4ltVjGHbyfbbxE0XxgMk4Y8q09WMeBMkoUvKvA_lh6DtPhzWcI-Nbnyd31U3uTehoc3b5A3-cU-kbns4t0VCk1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیک ادووکات سرمربی کوراسائو با 78 سال و 260 روز مسن ترین مربی در جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93010" target="_blank">📅 21:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93009">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پایان نیمه اول
آلمان 3 - کوراسائو 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93009" target="_blank">📅 21:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93008">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f6788069f0.mp4?token=NaoRSvIoxqnDpDriLInitMdv496bCmU5rd0gFaGIhohd75t8GK3lSr-zq7BLv3pkAUu4lDnWt2jfy2U0O28bLmQ92z5CNzzQdWgHlxCH1oDqkn4v1O3Rct6VX2q-foB3rh3xDXWLt92CtZ5lt66Iw5G6Fk3qdKwXlp_ocm13hsAHV4V_PdrL4cHH1btyO0dmzpMGVg7Wb5tOFpnGHlMw0S3owuqoUzEZsy9y1UCJgJKAe5qdI2v4XKxOPnumxrrNQuKgqlzYIGzPRquCuY9SXMTGH9WUxPz4c0NPDlYCwIqjD4u0HiI-2rM4T-tLqk589-Laf08Zo7sFTVVv9LavIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f6788069f0.mp4?token=NaoRSvIoxqnDpDriLInitMdv496bCmU5rd0gFaGIhohd75t8GK3lSr-zq7BLv3pkAUu4lDnWt2jfy2U0O28bLmQ92z5CNzzQdWgHlxCH1oDqkn4v1O3Rct6VX2q-foB3rh3xDXWLt92CtZ5lt66Iw5G6Fk3qdKwXlp_ocm13hsAHV4V_PdrL4cHH1btyO0dmzpMGVg7Wb5tOFpnGHlMw0S3owuqoUzEZsy9y1UCJgJKAe5qdI2v4XKxOPnumxrrNQuKgqlzYIGzPRquCuY9SXMTGH9WUxPz4c0NPDlYCwIqjD4u0HiI-2rM4T-tLqk589-Laf08Zo7sFTVVv9LavIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم آلمان توسط هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93008" target="_blank">📅 21:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93007">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گلللل سوم برای آلمان</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93007" target="_blank">📅 21:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93006">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پنالتی برای آلمان</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93006" target="_blank">📅 21:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93005">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqm59a4aYC7VHPyZP4THkRs8k3-MoXwb-BugWK8GG0llOyJdaXULS3q1ML-VpmwwvntuponDE80f3NUBOuR4JvPrSkm-XEwyCuQH3OZeHQdzvf5o3Se5-fuwscq9dEp_RAx-aDScIC3uMWRG3m62RXDu1yVbVZo4JGskL2AAjpfRhF_RVgezp83WltmICNUpdH13vRCSJKBDNk1Om0-79O_zAkrPwmUu50jSm5QGkUtwNMHWwGzJZdMbncKUP7Tq9t9s7sK6Fv5NSYlJy_UqwBDEkgtszy5VPi9MjsMdj9YNPFyyqy38orpSX4EZTacB6VJpteu523YF30KbC_05hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس رودریگر خوراک میمه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93005" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93004">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9MafFC4eeL7IcIfQpTbVzp9PYNGWScnAuWzCjcbFAYM1DHvgIXRPqswtym8-sv4DUIkJO-MJtaKti_jxh9a6m0oNQcPa2jyZNI7rSihWFhr2wnXTowAZ3yjY9Z9hANjWkr8Ukxr-bM65gk4lI__tmKDlrwNoWxcDJ-sLFi9OtNPc_YDUMusjmxdyHybvFI3zz-QxXOuN7taWJquu1Cpzwl4MqYML16ezBiAUYaiS2AjKIdFxXRXXXgLMrhRv_4Y6EW9yBrXC9q8F74IR-KGF-Bl8eqUmYtmWBlRyHH_N7RD9djX36nF2R4v9F9WBB_BY_hATa_6lAX6FErYWqWRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سریع ترین گل جام جهانی 2026 تا این لحظه توسط فلیکس انمچا به ثمر رسیده است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93004" target="_blank">📅 21:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93002">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/66b9fc33af.mp4?token=QSaoPFjMzTPznNWblH-iesprZLMfVttU8VHy-2-7FscCIWD9CrU62OzCY7xNZa2vUcObMMkIJpxF7Jz2ICYi_xifs2SpC_HnOsAretIxO8mFKmsq8TqAURyChn6W3hfVL87WFJJZBMzm_GonNVhdpVSsSrnhyTLSgUdBp9GrdkHgpB7_Y6DO0JCov923CPY-ENsElA6hwiwFWaaIN_bHppM5HIt-NV7iKusa9e5cztDESsia0aXb4J4r-LhWk_iy53pjqPz9vCLnGtxdAufuTNiDSVKZpkaLsfweHY-JkT8R-YHosfzFMzlucZ_unmM59CczLvJek3aFODKs902HEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/66b9fc33af.mp4?token=QSaoPFjMzTPznNWblH-iesprZLMfVttU8VHy-2-7FscCIWD9CrU62OzCY7xNZa2vUcObMMkIJpxF7Jz2ICYi_xifs2SpC_HnOsAretIxO8mFKmsq8TqAURyChn6W3hfVL87WFJJZBMzm_GonNVhdpVSsSrnhyTLSgUdBp9GrdkHgpB7_Y6DO0JCov923CPY-ENsElA6hwiwFWaaIN_bHppM5HIt-NV7iKusa9e5cztDESsia0aXb4J4r-LhWk_iy53pjqPz9vCLnGtxdAufuTNiDSVKZpkaLsfweHY-JkT8R-YHosfzFMzlucZ_unmM59CczLvJek3aFODKs902HEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل دوم آلمان به کوراسائو توسط اشلوتربرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93002" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93001">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmcYnpJI2zouUPX5xpmUtiaM7o-B5uv-TeDco5hW0woTOEve0thT7T1Tm6nIs2986j4jZCc71Laalo8A5y-jAyrO2w6QoOtqVFZK7ZowM2T1jiQX1q_xEVmIA2zuxjfsh6QuqN9MrHQZXumvWS7ZqhuRFmt7s3rDtoXmxfYmSyMLtowYsBzC2_VL7PbJrox0BGaV8z_SuEMAAwmO0QjLbnBGio9C1OFQ540Jxu7jsQOlqzW1a40cK1RWNi82U3sr0YPw-OE2t7VMcCqDA4yMhycXA38j-IEJOyeuYeBa2smDmC2duqA_VDZtcHQl_2m5YBDkYI4iO7lRZrB1jSYQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی: ‏پاسخ رزمندگان اسلام در پیش است.
وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93001" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93000">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاو‌ام‌پی فینکس | صرافی ارز دیجیتال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkpu9GRfqFE-cetrgvuwSZkFMgfgj3AYWEUTBlRJEL5sM_EpuwBAJ4AddNGOiuFZTcW52mkNWrFApb0QxA09ZtgPiw_f9BwItHMA98LIa0wFJSGzFxBiTNXw86L3-kyghNIwCXgP9paYdP--vVubs39IZPTFM6islIiz4fjji4dLhodHd60ZIjm4615c0TszTYp6tB7ZUSpBJruVS992nOUoTJ49Nc78SRi70HVCxZ7R0-jw6m0bQ9b9EFbkyl_7buFMmMjy1r6bxd6z8vNBfBHCFOpAwFOLmBMQNQJK9XuaSNBvWePu09ieIPjYwpvmo-hQnQU2dQMNHI0IU8Yx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
تو اوام‌پی فینکسPOOL پول میاره
❗️
🔔
فقط ۱۳ روز دیگه فرصت داری که توی استخرهای تتر، طلا و بیت‌کوین مشارکت کنی و تا سقف ۱۹.۴٪ سود روزشمار ببری!
📣
به صورت نامحدود واریز و برداشت ارز دیجیتال انجام بده و تا سقف ۳۵ میلیون تومان هدیه بازگشت وجه از ما دریافت کن!
💥
وقت رو از دست نده؛ POOL منتظرته
🔗
کسب سود و دریافت هدیه واریز
شبکه‌های اجتماعی دیگه او‌ام‌پی‌ فینکس رو هم دنبال کنید.
💬
اینستاگرام
📹
یوتیوب
💬
ایکس
💬
بله
❤️
@ompfinex</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93000" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92998">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWNKf1OTVCUzMIdDN7aQuf9YEjd3In2XbgjfaQkXHM1sNvnjQiIQChxKwYv--ArGtynKWYHDA7JQgF8OU2cWhNMn0sKgE7ENcjlpfiL_1KDcF-o9MHBvhUynnxaX-GEwy4eSk2BY0nZ2CdRFcFF-xTkkMMXz3evQZXfftcytelhtlXgDRXhevdpXJkoZWOZGwnLFR17MPqOqPsjJy4C2hHzp_p5efUw_YtXt-R2ckqL6W8E5rG44dQ9aijvvbAhG10lCINgtba6RH6P4W6US5yNNJh44CHSQZ1i1Mnk_9ZnBK3AJFR-zh4sfUyItLJJJ82tn-7n-15WJmGTn6OZlRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92998" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92997">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گللللل آلمان دومی رو زد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92997" target="_blank">📅 21:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92996">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آلمان بدجور فشار آورده</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92996" target="_blank">📅 21:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92995">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">چه سوپر سیوی داشت گلر کوراسائو</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92995" target="_blank">📅 20:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92994">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWijlNi_kGiBH4RRnXRSlP6HpYZXZlScapf3QH0iK7UwrJHMKn_6K_niAWlSeQ3pk4yOHawMqAcaT6hzq4G5_OkaGb9DFO11h0T8JFozMBPv-qjHNV9SWQeoBVft2FbPkB0ATfWAM--EwiKO3sh413nUU4JGCIjJiDBoApwrxYNt21jgCY9xiHWCjZhMsJ92o1hLITTZYTKGEKVXp3DniwN0Uu26XnpueVlTZxoDsgzXsV9ei_UibSJpxZl-jNDNwcnFrbXIH4O2rl1pEVSR2h4d0FcM_PQWaTOJ-BoGXj19YVQR0wO75TeReR_5pZhF8vYz1bXEyIHVu3GX3O825w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوشحالی دیوانه وار بازیکنای کوراسائو بعد از اولین گل تاریخشون تو جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92994" target="_blank">📅 20:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92993">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کولینگ بریک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92993" target="_blank">📅 20:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92991">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ff3f955717.mp4?token=AXUBV7hwpa-mahAPSub08IIO4xPsWc6UkHGUpXzS38wpCLzDC8jGSY0G0RTLu0KvWFIJZbbPPdslnBna-pH1z-yMs0AmLIZs8dCix-vaq0tQzeNttxPcl0Dz_32m0OPoRegqCWXHtsr7YdcW7meb828_RumdNYH0fU02sLmTSer5j53BPwRYBpqigWzmPHD2gsLJPFmVms8InizlF74MO99fXqSAe1WzV1aBGij2NJhuej-mh-myfic5slNPyGZF3McPt2w8nkNUkAzZn7fMXO8YVQGodkOlgUKHxShF_EVtg6mbzaCG23_ONyXHKU47jh8BjxGnRp94EwHlgWzhG6Bg1go9MQjoUbivBfo_XE1PPNfLD0pc7mb706YvbfBah0E9V6TVKuaPjHuVdZrA0omhnjWquboxBtwuqXxJjreW2xNQN99rvGTlWC2ROFuXIlqJo21kndlVSdEpLYqMdFuWKKGsp3UK_aWBjvJS6DZjz9lLj0hV03m_GFBK1HLjrGHt1zrWDkejf5d6NvZTM3dKTgq7J3f72m2A2zmDUan-3sjb1C4hKz5cYpLowezORodbw95Z6H0PZyhTe5wjWNLA71CNTpKif5n-VvmedALlOg7RcHiEUvBc_iqKuu_7rXNyWUXFk-3xMnB7n0y-iiiTvkwqt0lp_lum-xKBOug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ff3f955717.mp4?token=AXUBV7hwpa-mahAPSub08IIO4xPsWc6UkHGUpXzS38wpCLzDC8jGSY0G0RTLu0KvWFIJZbbPPdslnBna-pH1z-yMs0AmLIZs8dCix-vaq0tQzeNttxPcl0Dz_32m0OPoRegqCWXHtsr7YdcW7meb828_RumdNYH0fU02sLmTSer5j53BPwRYBpqigWzmPHD2gsLJPFmVms8InizlF74MO99fXqSAe1WzV1aBGij2NJhuej-mh-myfic5slNPyGZF3McPt2w8nkNUkAzZn7fMXO8YVQGodkOlgUKHxShF_EVtg6mbzaCG23_ONyXHKU47jh8BjxGnRp94EwHlgWzhG6Bg1go9MQjoUbivBfo_XE1PPNfLD0pc7mb706YvbfBah0E9V6TVKuaPjHuVdZrA0omhnjWquboxBtwuqXxJjreW2xNQN99rvGTlWC2ROFuXIlqJo21kndlVSdEpLYqMdFuWKKGsp3UK_aWBjvJS6DZjz9lLj0hV03m_GFBK1HLjrGHt1zrWDkejf5d6NvZTM3dKTgq7J3f72m2A2zmDUan-3sjb1C4hKz5cYpLowezORodbw95Z6H0PZyhTe5wjWNLA71CNTpKif5n-VvmedALlOg7RcHiEUvBc_iqKuu_7rXNyWUXFk-3xMnB7n0y-iiiTvkwqt0lp_lum-xKBOug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل اول کوراسائو به آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92991" target="_blank">📅 20:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92990">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پشمام کوراسائو گل مساوی رو زد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92990" target="_blank">📅 20:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92989">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISCD4qMKtLUfZIIW6T24xtS_2SB9sDt4LI2nXbXVptbKk7Qkm74vZgjwSjQWIrgyzNeyyQgb01Ak1bzdCGbrRTGxsa6W9qaomqDzTt06BzqOF3TjfVSdXcown8yvw_dtwfOuasYmKR-BaRTxjf2u4Xbaf7KWuIl8TzXe1ujKNN0Olbem3H9B09_FChDwM5bdc1ZE1kAj2xFecMinTrSvE6j7bHQy-P94EQn6d7CCw0DAuZ6ZRyi_aSClTAbNN8csW0HNOGjnNwRIliqIEWZFGlSPCWI4861yNEbUoiZrOm_ioU7TH2r-mZzTc6CR2c6a0dGFjeW9pSq6reMaPhmb4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت گرم کردن آلمان چه خوشگله
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92989" target="_blank">📅 20:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92988">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/043736f33a.mp4?token=kuxfPVnFoqRvFyXQ5aKdD9ZbBCib2BZ-CO5Rs2WmRaG6yBej3Ry9h1oBBJdZtPGTNoCyM7wNIcI86rbOz3uSxVja7eytSrlG5rmF7B-gAFQlYKusrvlMBJj51bG2lTKIA-L4FshU1adxnu7rD5lFqydFiNdbhSAlaLvV8YlzEN5OKSF8geDHBYqatMEfEc5xMWIrLfdcGhotluwV7LSPpSLhLCSdsuUKdWz54M1LFiG5s0JsP_FI2uAuMVBq6l1z0pkVi4Pye8EIqFlpbPBtwEr61keVpDIknbYFKB7WpowEybSG53Uxj0rWN-0i2QTiRsUyVp7g48gt9VXvNYP5gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/043736f33a.mp4?token=kuxfPVnFoqRvFyXQ5aKdD9ZbBCib2BZ-CO5Rs2WmRaG6yBej3Ry9h1oBBJdZtPGTNoCyM7wNIcI86rbOz3uSxVja7eytSrlG5rmF7B-gAFQlYKusrvlMBJj51bG2lTKIA-L4FshU1adxnu7rD5lFqydFiNdbhSAlaLvV8YlzEN5OKSF8geDHBYqatMEfEc5xMWIrLfdcGhotluwV7LSPpSLhLCSdsuUKdWz54M1LFiG5s0JsP_FI2uAuMVBq6l1z0pkVi4Pye8EIqFlpbPBtwEr61keVpDIknbYFKB7WpowEybSG53Uxj0rWN-0i2QTiRsUyVp7g48gt9VXvNYP5gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید : میخوام تو جام جهانی 2030 بازی کنم
نازاریو : 50 سال تمرین نیاز داری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92988" target="_blank">📅 20:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92987">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34ec3a9b4.mp4?token=B0SGwh7fmpS6-dTkx8QcxlGkom6lKNY99qmioptzSHD0fd4QVpA4AnMbtOSmmkJ3fgtDwdx3LbrTn0MeIYQSUbqrHKwNd8ZMaEJv_ANDilAmG0EkPDP7jENoE4SRVHpoXv7Jc0BVHpcerkP6woPOXKTF1bBILDeZNEpd9EeMnNLrOUFKwAC4UwUYVGG-FQBfy1JbD6zM6L3m3VvtIpv5leyxHIYRnVDm6TsrrQjWEuT-J2QPjI1hK6PmUoi54mDX0ZJQy8h4wBR9xzdTEaBBf7H_RP0x5EYfvPUJB2qsZj-MefbTfm3ViSccLoWxULR_fqg4jnNf4GEFgNdvjQeAVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34ec3a9b4.mp4?token=B0SGwh7fmpS6-dTkx8QcxlGkom6lKNY99qmioptzSHD0fd4QVpA4AnMbtOSmmkJ3fgtDwdx3LbrTn0MeIYQSUbqrHKwNd8ZMaEJv_ANDilAmG0EkPDP7jENoE4SRVHpoXv7Jc0BVHpcerkP6woPOXKTF1bBILDeZNEpd9EeMnNLrOUFKwAC4UwUYVGG-FQBfy1JbD6zM6L3m3VvtIpv5leyxHIYRnVDm6TsrrQjWEuT-J2QPjI1hK6PmUoi54mDX0ZJQy8h4wBR9xzdTEaBBf7H_RP0x5EYfvPUJB2qsZj-MefbTfm3ViSccLoWxULR_fqg4jnNf4GEFgNdvjQeAVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترند این روز های اینستاگرام از اعلام ترکیب تیم های جام جهانی و حالا ورژن ایرانیش
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92987" target="_blank">📅 20:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92986">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPBeM_nRVHjZC41xPATJ186D0lh_EJA8voHE49FBia3fxLtcFTrKuX_3VtMgW9X7zlxPS9iocpYQSCE3ZNRWn117npqfwEq0I3uvobyR94my4DV1F2Be-tEh2q8-Ns4anwgCRPzofQICfI3jM5f6KoOZPAmWGm2ScC7vn_NhBJPamT8j6C48S47VS4DmOcigSNw4vUNIMo2_KvSnmEtalzn0hZYFjCzy5R0lzQYeW5mRICyLYI1cYlQMXLYMZAVRca3YYV9rrvg1DfxB7EbZiWBhVfwj2BlJ4wV16Jx9w6epKF3MGlcgGj9DM7m8yQYHtEVzBLNj2NY2uFYnyasCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
برو ثبت‌نام کن، تو مسابقه شرکت کن و ۲۰۰ میلیون تومان ببر!
⏰
هر شب ساعت ۲۱
🎁
جایزه ۲۰۰ میلیون تومان بدون قرعه‌کشی
🔴
ویژه هواداران پرسپولیس
شاید امشب نوبت تو باشه!
اینجا شرکت کن:
📍
zaya.link/p4irm
#پرسپولیس
#ردکیو
#۲۰۰میلیون
#جایزه_نقدی
#RedQ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92986" target="_blank">📅 20:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92985">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کوراسائو کلا تحت جو جام‌جهانی قرار گرفته و همش توپ لو میده</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92985" target="_blank">📅 20:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92984">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsgQ2ZtwsF65_83wHc43lYKASyhF1V2wExY4DIpHE4XIw9uB9hNHa9ei1GkUnuqCPgdUpw70ssnUGvbfVdlniNfUVEDC_AJ2CdZb7H8HraODuQsGlREb666fVvJMDTB3JXihl_kD6Qcdb23V-1drmnHGGGGzbDoSitqCw0ZqvdbU56mPkrvSCml62EsutZWzKFKzckmKfNDKDlbXEJhPPgBDAFcxpr1SYmSdB3NR_BXfUpm7CaOyspBdooOp7Ue8CRKfhlO2ua54hfgLVgOK9D5Fgg4jOuBm_ckiU3IjfMMBw-vlAEd3mU9yfP8gE69Ma3JZP5BpBb2x3IKuV4TfNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غنا؟
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92984" target="_blank">📅 20:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92983">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آلمان می‌رفت گل دوم رو بزنه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92983" target="_blank">📅 20:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92982">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfe1e6844f.mp4?token=BzSN3dC9a5JgNV3-go6IchwfNi3tpLHqjVZnG8ersCchyKptUpWmfdzIo-FIvKK_cimVJSM34KrF4Mu7KNE9E4Io-1GbYVdrXHAVqEKfk2i5Y79mejdIkEAx7tQFTzEccTmGboXutQat5rQWXg5EPX0VdcVZX04HN1fAwWU5az6k39YJKCJioDIljAUDcSSh0oKDwhk7wCVebSP4shlAmq5RTSaJdyikjI1kTmvasQQ7MxHHqmiaoKY6lllDMjui04F0A2YS2qCOkIEP4cki20f9RCPyyOJsbq11xnkXNhPwDVYkuapZvsx-e3DLrWAGR4RSI5dCDlTF4ILLY6wmlg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfe1e6844f.mp4?token=BzSN3dC9a5JgNV3-go6IchwfNi3tpLHqjVZnG8ersCchyKptUpWmfdzIo-FIvKK_cimVJSM34KrF4Mu7KNE9E4Io-1GbYVdrXHAVqEKfk2i5Y79mejdIkEAx7tQFTzEccTmGboXutQat5rQWXg5EPX0VdcVZX04HN1fAwWU5az6k39YJKCJioDIljAUDcSSh0oKDwhk7wCVebSP4shlAmq5RTSaJdyikjI1kTmvasQQ7MxHHqmiaoKY6lllDMjui04F0A2YS2qCOkIEP4cki20f9RCPyyOJsbq11xnkXNhPwDVYkuapZvsx-e3DLrWAGR4RSI5dCDlTF4ILLY6wmlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول آلمان به کوراسائو توسط انمچا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92982" target="_blank">📅 20:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92981">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گللللل آلمان اولی رو زد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92981" target="_blank">📅 20:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92980">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آلمانننننن دقیقهههههه ۵ زدددددد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92980" target="_blank">📅 20:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92979">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گگگگگگلگل</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92979" target="_blank">📅 20:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92976">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGr73jSB2sPk1Z6LCVIZtpy5rVVJI4Ql0nRgYEPolN_9wInD9fQ4PigHrXurun90cPCQQ03A1mp7V5QLZi6W52MI6rZ-YpZs0zUGuwiz3lOHWw6MLNOea-Wo31PUP8pEzyqRh_7iQLK7CTUSaqCNy_uDYd7W4JLqtcdXbjMJuaTC1oP1XP8_65AqJUhu3dumFg7AOYkCLUqVOMWzaWor2ypweXFHGQ0ebbVcoF7SjVC_M7choQptcabCzelpgr1RBy9uFSMR0SO5ujw2yJgzxNJPiR1GniDSs2ugw14D0lJvj2e87huVb6ezouSmmgOOcQauCgJTFnfqSLxLDi0Alg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
: شبکه ESPN آرژانتین: مذاکرات وکلای انزو با رئال‌مادرید از یکماه پیش تا الان درحال پیگیریه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92976" target="_blank">📅 20:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92975">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کم‌کم بریم سراغ بازی آلماننننن و کوراسائو</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92975" target="_blank">📅 20:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92974">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhmUb18fPtfQ-o8eGP9gIS89TuKlXFRceofZgW0netxROP4SPO6EBTNJUPpTJgwJBlPNHVwwuTlV9hRheUokk_DUcdpzGwgKkni2OJmYza7fP5t0RLOP2BG12I2JYZEdaXTP9deyTvJ3q7uUfjhj3vnyaKcAVYSBqpDleLHqUNdI5zuP-p0vKW5sLRmRPqz1LYRHndrCVG_kqUd7lRQk2pLgONJ-0DC0yAPdXUuVOs4bbtbLr_0BisOk_2R235_Xpi7bivAJk3qJyIIsZJ1vZzwRqfJQrkM9GKD6OpUZ0jKyGWu1EQ9TxMd0IAgOaGiNF-7LTHLjfAVZ2fkO3X6ltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید یاسین چوکو محافظ مسی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92974" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92973">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpoY9_Msf9cS7oU2HkRRWuVJVEnDaiOoFcDE1wXwFMta2_te-jy5Giknoigu0nnk9uBcqjtkPS4UXqzGdc-tklbMAF5MVTMaAf0fDS1bcd23bYE_X4WNSTpj7VthiVynvml1ifEBDCKdIzaumAKzrSKaCF0RO79JGfI3FOziGuZA4DqoBoa19Vm2Z1q3W_U7QT4kE3WP78GIqa0S2n3bfVuiVzg4Q0humfAVMQHumddar4nDv-gh7upNd780scprTNNsjgiVsyNnY_6L0uLXowtdm_4a6HN-dmriIj3qI3_B1C7e-TU1UF48WvcXy3W9YphtsLq4CGqR47Q-U8oY0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین تعداد فینالیست شدن تیم های ملی
🇳🇱
هلند ۳ بار فینال رفته ولی قهرمان نشده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92973" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92971">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ek7mRf9qP79NdP4P-o1BcgCanIWn-RaKQoCER5TWfHnEnFnC9QxtrkV-dZDGhAgsC8Tnnr_KxIo0cV0WSZgrKZL5P3h1xJK3fzWbbg6IPSEDlFBH1Vbe2xXGeMkAOuRojSvKXabjUPNGp-ubNtzYX7mL0uW-vCo5Nl4Sig1U9XLnAsYmg38e3dwX2uvB6SZnLJzOdnZxYBOEFoZRmDTVHrhoApfkTurIc7i4qCQ5NjHg58cYEZuSAoMWX87BHvVMugsnTySggbjDt9hay-8olvjbTviYRuqh8SauuHNR_G4AEneG075AwKC5lp7LKgByypzxXPIaD2sOEsNRUXJXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد پدرو پورو ستاره اسپانیایی با تاتنهام به مدت طولانی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92971" target="_blank">📅 20:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92970">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZWya_hfWfk5OX3pwnSPQdFoCOKcHwVnAQ5r_85vLcf3wS9dpqRkLiMw6h-IxtRpSsu0dLHY3I9XXiBf6NxSkx2zOabu7fijVrlBeGYZe_1tFpmbcj3Ke4Htcm2_6tnXcI8xUTnkcCY5VfBzdYI-3SqbLuGH7u5F1dbm5HQKPALTIgFanJ0hr3GbNN85r4QgfrMBFYkdTKsVu--Hx9Wweq4lnVSER4p_17L43yWLsHcDtfs2ZC8eLjfh6hb-YoZMDC4BzU5wVwmH2NgBhPYRgCK8pxRvcuX-2TDfWM8X8dpngHVdRPU3rng_eSn3GbUoNM2bx3rqWmleVXZVNEGBYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
ویژه جام جهانی ۲۰۲۶
هیجان بزرگ‌ترین تورنمنت فوتبال دنیا فقط داخل زمین نیست… بیرون زمین هم جریان داره
⚽
به مناسبت جام جهانی ۲۰۲۶، یک پیشنهاد ویژه برای همراهان فعال در نظر گرفته شده:
📌
از ۲۱ خرداد تا ۲۸ تیر
📌
هر روز ۲۶٪ بونوس روی بالاترین واریزی روزانه
یعنی در تمام مدت جام جهانی، هر روز می‌تونی با یک شرط کاملا رایگان  وارد فضای پیش‌بینی و هیجان مسابقات بشی
🔥
🌍
از روز شروع بازی ها  تا فینال
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92970" target="_blank">📅 20:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92969">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7D3RvOGhqKN4UMZddOz7rtu3NNrLYrX5CPyEezmPEhp52z3hcMQw9iPYLFvsGGoR16KsyyOEd04VMI3ns93Ozqduxn44LY5e22UN2y2vIlhvlrMmPCmQZYKS4Bh4Xen_BRp4myHgUWnhtpmpPWqQFMGJoEw74iq5tdr0-Nm6O56M8K2UhNeFpmSdCuo2vGLeHyaK_PR1QSybcjqgGt5c-vfBOfumFDzSkhUfUJm-bUcmzcIoncOs7n1pIpoXIb15l4_sz_0RoRUzSMqkggkC2wUfaXAUb_0yVsjR_Swtk5o_8wIvof5LEyq4YzYdWrb41oikmIK3xNinPc31x-QiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو: نقل‌وانتقالات رئال‌مادرید هنوز ادامه داره. منتظر اخبار جذاب باشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92969" target="_blank">📅 20:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92968">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDj0jDVGICqcw5FIhhPY_MXDxS_KBtQJlnkAcqVed0qyCF6ijapFADUN7W80X5yEI4t06q_SEcHEHrEUiItH45ePvmEjhSxFhbKE9Lnp7G5gl10SQncaQtDDXnUUIWxRX3zlyl91chD_RHWVl5puPsNHf3vIz6kYepT9llS-LVoSlUo5sgo2hRnP3xUgKFl5ZzsJZ7_5KLEovzNeO6L-yxLiI5qDynrS8ATolpTDG1Yj9M0qRHD8Ws1PsgGqekE3rNhYdZ5RLAB-FJHaucNboUVK5EoOMVaAhLAMitLFsWExZPKfHaZW--F-n41N3XwiASln66JP3dRwczvqGMF7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
خوزه فلیکس دیاز:
سامی خدیرا دستیار ژوزه مورینیو در رئال مادرید خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92968" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92966">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLiboN6NmXzYAoq_IPhtfBwLYA8gAJqm78-7ZOZxkz3j_xtbOYb8AQIOV33voB3ZgeHHbdxH4u6_NHsePqKEBqvq4HR2r1Tr0oAIjwR6RfRL0f7VJtn1o-8S53xoRzfvxG8__fapqoELuUzkpFC2WCuhuTO9g4_E6eR8bC752sw5lt4ndy4qxiFC0hbyY8mcP2X_UvQ9rlXyO86MN8OtCtMn08vzL9F5fJlvQLf3pjd7QjKlRVa8cNupiSej4VB54jromFs_FZdIRN9zRlU2sxctzId7LBL1H0rfeB7X85Yve5hg3TaI6RqmQoDvJdhPNJ1F9WFfy6V0bIBjHJ-nqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3qs-OszE-u7IbN8Tnj9joha_dBb_EkOeBkh-DctY6wjhHkXMpi4-NzkaYNzXM9nBQMVdLzAgTqq1CTQ7-Zye374pQfv6rKEOy2NJ2gnB8IsMJZbQIDONx5VOFJ85sEfs0msQ0sydxVdvHfcIujevmVC2XNcoJy280OEMIezdWISP1iSMctKUNKPm7igOZ4IynmXXE_8f8BUEZLcQNFyuOrW8aPsP_4pwApMcYrSJLmWYnhLPWue1UW0aI5Po0iSP69eEcvMeiZ_2aiQqJlcLXUToNd7_OhZ2tYq33DRoFleID8aBvsuH9HRVSTsD5amLFliYbON5kYJqzFY_1BY7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
حضور توماس مولر و شواین اشتایگر در ورزشگاه قبل از شروع بازی آلمان و کوراسائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92966" target="_blank">📅 20:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92965">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:   کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92965" target="_blank">📅 20:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92964">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4NZPc2cHtCVXWPK2r_73YNQSXLNEaoHgaRA6prnWxyvy6meedqCT9mF3ied9AuWiYzRdIpjI4e2jGpiCvXtZb-EZDtH9UK2spngg5yEfYFTcinHo_rl8LwDMFNkGJXLWLJSjNNbjRDXfVe5kwsLWjWNXZJ1CE9hmQQzaXhRT6TfInUSzNaL5cnm3BC-VoVXZ5YVgpSPC3q1FG4q3wtUhApSN9Atjvlh321YHjB1yxwKA16fJNBl3wtHvnyBrxkzrnSdi3EwXFU-bC47rUgVvX-WkJpNRAdLkr_ZgOdLsVNb0H67O_NKJeWBSo3fPOh4dlO846MCk1NHtUbaMqJ2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
❌
رومانو: بعد حضور کوناته و داشتن رودیگر‌ و هویسن، رئال‌مادرید علاقه‌مند به کالافیوری نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92964" target="_blank">📅 20:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92963">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBxsxbL6DYm761ecwv46_EF9vCIf5TDAJIsCWJzvSLPNLbtbLQLVUlNjZBo3vNuQj3-FSI6_HNAiFyVEM5rRHgVQZSE57ZDjqXdLQGmMQhRJTcACQk7yimKnCUufDGjp_7NghLDWh4UAC-yw6QYhk1bChXM5DzJstgx8TYnfAdmmJwXz2mNNK0gqXyD5P8AJHM0vZ_Mg04N5cx1hTL52P3eT4LjYOen68NjAcBDhifTPoT26fUfJnAvl6PHdrpUllrXl9X9KlCup-mr1CYAoJCGphISunDUsdaoWayvFzH3IFHYKwDGSZGiW9ySj9bbco2S4K5cKIay_Nm4PiOH63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاحیه جام جهانی رو کامل و 4K ببین!
🏆
⚽️
خرید مستقیم اشتراک ESPN ، BEINsport و...
برای داشتن بهترین کیفیت و گزارشگر اصلی
🔥
با اکانت پی‌پل کایا
✅
✅
✅
میتونی با این اکانت چی داشته باشی
⁉️
🔹
اشتراک شبکه‌های ورزشی
🔹
اکانت‌های PRO اپ‌های مختلف
🔹
خرید از تمام سایت‌های خارجی
🔹
و هر پرداخت ارزی که فکرشو بکنی
چرا اکانت PayPal کایا
⁉️
چون این ویژگی‌ها رو داره:
💰
حساب بانکی متصل
💰
هویت شخصی
💰
متصل به ویزا کارت و مستر کارت
💰
ساخت کشورهای برتر
اطلاعات بیشتر و فعالسازی اکانت
👇🏻
🔥
doo.st/FIFApay
doo.st/FIFApay
doo.st/FIFApay</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92963" target="_blank">📅 20:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92961">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8a8a00bb.mp4?token=hCzb3sulk-DxlTWy5WvdshP2a-jUvjz5hqjbxlB13sjbLb8kzROUaikH99mKNktjY8koq4tN-i7EexMlQ21AIlhmkV2PC7ZNbCwk2bKY4xxvqpeXTQpi1y7nyBl5i1IB-hxY5SbHuwmdc5n_FfzdS1W-xop0uEFqf7CF15dHkbssi2H_pf3bowcP5P4Xg5Z7U1Xovp9jqDTePnNm8ENU-0ENeNPmhK96wFPBd3odQ9qfhDqQkD0hKaBo9sV7oxRoKcIAMQGSi4lYFU-j0rZN7taPdlSnQxVmznpM1YeuN1I0u236ysq_kUGW_QFYXUUdQEvRf_5pfjzLNAU2BmikmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8a8a00bb.mp4?token=hCzb3sulk-DxlTWy5WvdshP2a-jUvjz5hqjbxlB13sjbLb8kzROUaikH99mKNktjY8koq4tN-i7EexMlQ21AIlhmkV2PC7ZNbCwk2bKY4xxvqpeXTQpi1y7nyBl5i1IB-hxY5SbHuwmdc5n_FfzdS1W-xop0uEFqf7CF15dHkbssi2H_pf3bowcP5P4Xg5Z7U1Xovp9jqDTePnNm8ENU-0ENeNPmhK96wFPBd3odQ9qfhDqQkD0hKaBo9sV7oxRoKcIAMQGSi4lYFU-j0rZN7taPdlSnQxVmznpM1YeuN1I0u236ysq_kUGW_QFYXUUdQEvRf_5pfjzLNAU2BmikmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
ترکیب احتمالی فصل‌آینده رئال‌مادرید؛ بالاخره زورشون به تیم مدرسه‌ای هانسی‌فلیک میرسه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92961" target="_blank">📅 20:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92959">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJALvAw8cXb5qU4DiC3vrAG2DB4f-dXzqljFSJ0TcO0tIKUvtZmAKBasyZftHmOYxYvJ_erZkz3QGqWOM47x2WgaJKJgTs5LCKCJm9JkITK-tsiXBljd2jup51WNO_uy12qIaUGcpUrhCKXQWKhlckc_GWpbFiP6Uimj1cVIgo-6ZYqPFu9SsgmWMHxpW6T9xivYYQszGPcEJvWSMtuwFu2lP1c_M7hx8VIu1Iyr6xCZWJ58ElXyYlrOGi07HlOUNEos3Tts5X_YCobr1SYvcAUacL07KOihhOAZUywko5CyAVr9Z553o6RZrYQ2kYLvohmkvwp2uLoZu22rNsMMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب احتمالی فصل‌آینده رئال‌مادرید؛ بالاخره زورشون به تیم مدرسه‌ای هانسی‌فلیک میرسه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92959" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92958">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خریدای رئال بجا اینکه سر و صدا کنن کاملا کاربردی و متناسب با سبک نسبتا دفاعی مورینیو هست. پرز ظاهرا سر عقل اومده و نمیخواد پولاشو به کص گاو بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92958" target="_blank">📅 19:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92957">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پایان ست چهارم والیبال با برتری ایران
🇧🇪
بلژیک 2 | 17
🇮🇷
ایران 2 | 25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/92957" target="_blank">📅 19:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92956">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">كوناته ۲۷ ساله است. کوکوریا ۲۷ ساله است. دومفریس ۳۰ ساله است. سیلوا ۳۲ ساله است.
❌
خبری از جوانگرایی برای مورینیو نبود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/92956" target="_blank">📅 19:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92954">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🔥
🇪🇸
بازیکنای جدید رئال مادرید تا کنون:  • ابراهیما کوناته. • دینزل دومفریس. • برناردو سیلوا. • مارک کوکوریا.  پرز سیگار به دست داره رقباشو میگاد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92954" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92953">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🔥
🇪🇸
بازیکنای جدید رئال مادرید تا کنون:  • ابراهیما کوناته. • دینزل دومفریس. • برناردو سیلوا. • مارک کوکوریا.  پرز سیگار به دست داره رقباشو میگاد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92953" target="_blank">📅 19:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92952">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpudDa08_U-KTuuzU5dK9hU8tcUYSJhNDE8w9S0aqPYUqUaXnUwaGQdfP3WHAtDjkC_ieMfbwZybnSwYtAKAf9FawIiCx7cWE1ztBcp9zB7hF5y-xHHpgD3fCYYx8yeWQhkKlnQKjc24KuBAlotQ84ssVFtuCd47qSocoiUgyYYqpR-XI0XnPqTjcLZ0z8KS2Sn9adT7_Lmm2l9JC3Mh8r0yEFjTIgpw4zzxHeCRUuz9YJJkqtJ73CDdEOgAub5OnIbnTl_UXoJciXN6Y8j3MQFU038xhhxwBoEnbZ6eeEx82DamEs9m4ED-jrlSROKGH3bT_jTGtnxLrjZvDPJeUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇪🇸
بازیکنای جدید رئال مادرید تا کنون:
• ابراهیما کوناته.
• دینزل دومفریس.
• برناردو سیلوا.
• مارک کوکوریا.
پرز سیگار به دست داره رقباشو میگاد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/92952" target="_blank">📅 19:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92951">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
فورییییی فابریتزیو رومانو:   کوکورلا به رئال مادرید، HERE WE GOOOO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/92951" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92950">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGAaizBB3KRLEaBHyaDg1jPI809sVmAE3r3d-a1UJNnSPsVoS4S-UHIgYcSSJPei1V9D-EJt439b6J9YF0bAU-H5DlICWmSvzE3jZlyrY23n1kbwmIb1AmTvve5oi1wi42e48AGFHwV8APehTFMCbqcMdDWLHurK8RLH0h9b9bAijl2YuwBWjvNX3I8EkefWGApOg2kLrbEbURjok46xODEL7ly63x7JwKjrpNzD25zgSYJ-N5G8bNZzWHIzBijkvrQofeOoZxsG5stpsXIVRpLxE52BsFabDGe6aNwUQ-7F1stvyI9LJBJKwMItPNo6Tdfg0w7evKyNP5mBrBP4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک کوکوریا، بازیکن جدید رئال مادرید، یکی از پرورش یافته های لاماسیا است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/92950" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
