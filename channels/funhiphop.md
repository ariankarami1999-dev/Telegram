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
<img src="https://cdn4.telesco.pe/file/ImXOoy79bOdOpAhF1nTXZMOTZXc_aitYHg8fqFdznL61eilCyYsGEESDXRpbook16VDm5dI_OPKCik5olOWkFTSiUtF0yzxDi4T84WHMWo4qRn65h0lhnuguR3i2seyBcE2UJYNSHZYRRtJ2dAFsGlSx07JK5Wd4fzoi_IovvRBRzf8OpysV36MsEadMUzpglZde3TDlkLnF3aizPEGAedb31320BmzpIuU35Dl0jE2yQDeUX5K_nPjZNI9dbPS3x_85ftF5ynwBP8L1Ht-DFVuwtKbm_M5vq6_n2oFSpwRGKzco3b5o_mdHF1Wz5EZyy2eD5XIYIhBhuQ0eg5bcVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 266K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 21:02:44</div>
<hr>

<div class="tg-post" id="msg-84672">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=otwJFC3hbnGjk72XUW1KpHu9fWKlrhfdxJLdsn50GHaj5DhtW-MumR_QCM0XOjaM0u9gTL0CDcY7TmVnPZGbKGsx0eQuWx1rsq6keM3ZoCzhT80taTMlfZZPReFqjRQm7Fozv4pC2LrBIzwlkzlsbsST4u8A491p88PvOgUeAvF4zyUVfYalkXwdwap61KGCSLC_bcK7DZU81KCEEk-wTGCgQVOAkTKcLTNrsBTHEeai_kgmWU64l09kuvbHvFHcthAse3lHwABVF2VZ5S9ChjP5vbva3gpOHeEERRhxkSrQFKfj89ms8POzmV7pyAlXNMkzBiNBG8WJZAVwhz_CGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=otwJFC3hbnGjk72XUW1KpHu9fWKlrhfdxJLdsn50GHaj5DhtW-MumR_QCM0XOjaM0u9gTL0CDcY7TmVnPZGbKGsx0eQuWx1rsq6keM3ZoCzhT80taTMlfZZPReFqjRQm7Fozv4pC2LrBIzwlkzlsbsST4u8A491p88PvOgUeAvF4zyUVfYalkXwdwap61KGCSLC_bcK7DZU81KCEEk-wTGCgQVOAkTKcLTNrsBTHEeai_kgmWU64l09kuvbHvFHcthAse3lHwABVF2VZ5S9ChjP5vbva3gpOHeEERRhxkSrQFKfj89ms8POzmV7pyAlXNMkzBiNBG8WJZAVwhz_CGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین عرفان جان میدونم ضرورتی نداره من الان این پستو بزارم، ولی تورو خدا برای یک بارم شده یچی بخون بشه گوش داد، من خیلی دوستت دارم ولی واقعا نمیشه گوشت داد، لطفا لطفا
🙏
🫀
🌱
🌹
✨
🌟
⭐️
🔥
🌈
☀️
🌨
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/funhiphop/84672" target="_blank">📅 20:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84671">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ترامپ درباره اوکراین:
«پیشنهاد می‌کنم اوکراین رهبر جدیدی انتخاب کند که بتواند به توافق برسد.
-به دلایلی، زلنسکی هیچ‌وقت به توافق نمی‌رسد.»
بابا یکی جلوی این کصکشو بگیره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/funhiphop/84671" target="_blank">📅 20:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84670">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وضعیت فرودگاه ریاض  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/funhiphop/84670" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84669">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQeHlnZgp3pOk3w-NwqK1V3UqnKsIQpJLLh7i4MEJkog_Pj_pZbCdje1d9xgLJ9Q_ye-ZY8pEuXw4moagM8qM1xbZ5c90P1khC2JM_nZ4B29O8TliKy3JL3H-yV_tkwaqVjJMNXTibf0_JlbpsTOS0Hg8Pgpiv3sf8pvHQ0n03ImZnIiOJiNuKcZyiuihi09Q0kknGYFw04RaQa9lFawz_MhgAwyTzZL4po-QneymEFOW-9WOcxTUhz7akBKvr9Q8pa5We8vLUjfTZHGvet43s2PFYddTr_bW-flOyiRW6NDZbdhEWbfs8Tconjqy0YLj308EM5KVwsL_QVS4UzRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فرودگاه ریاض
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/funhiphop/84669" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84668">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/funhiphop/84668" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84667">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4_KF_1Cpbf9ryVBPAUbm-xXkEH_ochs0rg441D6WT-F0Xe6Vjh7ugrwwkUh9f7Q6IlvZuwRbAEB8aUj1Xy8FL5De70Xq4fikRofZoVppfXSxrRAscEanYXDvDj7CkqH8DFuaY-iql7eT3fNkgxmNlq1yRBZhJtPjnBoXn2JOOHAgx3nRR4ookX3pdBjy-pr4j90GwoEMh8pZcvJEb1_bCxls1q1wKs-ffRaomSZnxP3cJby8XFpLT8zwe7xNlpg501rFdIParJKHz0sZ-pFrdODwDiFmsiF1OBpZcLrwzQMtOBEzNYALCzTuaa3KtXEyciuWGMJAPYf3gfFGAdFBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G18
🅰
🛒
ورود به سایت
👇
✅
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/funhiphop/84667" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84665">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=bwY4Q5QbPv7y-Q-lCyoyCP29qj20S3iAOM9qezuyTqUwAxSqBdnt7Zl1u0Q2WtOZhSc2sdAm05X1X3oDZ6wIHe-ws0q4SctbpAfAeHy3ML7AUsUOBRdG0UHU1XRTBUhU2bppGfaqC0CnLToMPnYOtV5RQWHXSYLJ0zt1TF0LNu857qwkWMgOAZjEhUceVK7RmULiyHUbIdzY162Tj1S1PQmQN7BL3yWNLq88pTiFAVqL7fNVIFKbtETsAAK5zOeF-rs3qUDE3WvHS7rI6jpHWfCcxzmfAkvNNcQjAAzJ2nUoVNmFWFgefdv0iy9Dphjufw6fbVmg1SSfNdgL7Om4-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=bwY4Q5QbPv7y-Q-lCyoyCP29qj20S3iAOM9qezuyTqUwAxSqBdnt7Zl1u0Q2WtOZhSc2sdAm05X1X3oDZ6wIHe-ws0q4SctbpAfAeHy3ML7AUsUOBRdG0UHU1XRTBUhU2bppGfaqC0CnLToMPnYOtV5RQWHXSYLJ0zt1TF0LNu857qwkWMgOAZjEhUceVK7RmULiyHUbIdzY162Tj1S1PQmQN7BL3yWNLq88pTiFAVqL7fNVIFKbtETsAAK5zOeF-rs3qUDE3WvHS7rI6jpHWfCcxzmfAkvNNcQjAAzJ2nUoVNmFWFgefdv0iy9Dphjufw6fbVmg1SSfNdgL7Om4-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/funhiphop/84665" target="_blank">📅 20:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84664">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">امین تیجی جن زده شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/funhiphop/84664" target="_blank">📅 19:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84663">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">چرا حس میکنم هوا دلش میخواد سرد بشه ولی روش نمیشه</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/funhiphop/84663" target="_blank">📅 19:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84661">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0auDhlBKpCSS8xMlpt8o3hXiVKqBf_lhwM0jkC-Tclx23-jbyjLwDuFL8WZ9uBKuOJwyGa8mDdO-ht6-Ij8LPig_ENUMfUurCLL986XdNlf_fBmG1KfYEjcclNzbW2yAT7BwOPG7g4mvfqh76ktqw9TPvnPZY5c13ZunZQd0g13kmji_5ssOq04EOBQEPqh3JCfdQjFdbyOVLgFzaJGWchRQo8tfYLYAD0D28MUIM5Psk5TmDgu4pkGZ-bNJHiTtcIuPqQ6s2O3DwLXhcUCV8PrMIQesCUDCKMZ0TV6S51FvJUKcazldtjD6INGMyxZ6WEFBQNCnhZ3L3-PCkO5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYWJlJvKwmdjsBeIBJHGcb4PdMtx_itttvKd95LPhQa9WixVKRwPA_S4bujl9gadi1Yc6wV0r-abNyDit8ITMRLK1gI8_qRVk20sSSRV5tLITxbKJ2IfcX6uGstJS4U1RKpMK9R2GiIF41PDhs3KtQxTR4FFq-CLZr03vGFLDzk4JVt3grpTYR5MaiYsNiM2v3roe0op-gpeCxsUUO6eEZSyYtHzcBDFCAImThPQH8pwweZ_O0-bIDw8yNE4Jcb3eGp1lid5XT-CyOut4anLy4VvwfPphh9vahwY3gTBIDCkiJkjo7MqqJJKb7Pum701LLszz4YzATXBAo7-_f656w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو رونالدو موقتاً از تیم ملی پرتغال محروم شد!
فدراسیون فوتبال پرتغال بعد از جدایی جنجالی رونالدو از اردوی تیم ملی، تصمیم گرفته فعلاً این ستاره رو محروم کنه.
کمیته انضباطی هم رسماً پرونده رونالدو رو باز کرده و قراره به‌صورت فوری به این ماجرا رسیدگی کنه.
هنوز تصمیم نهایی درباره مدت محرومیت رونالدو گرفته نشده و مشخص نیست تا چه زمانی از حضور تو تیم ملی محرومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/84661" target="_blank">📅 16:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84660">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کاش آرتا و هیچکس یه فیت بدن، هم فنای آرتا کف و خون قاطی میکنن صدای اگزوز خاوری هیچکسو بشنون هم فنای هیچکس کصخلشون در میره صدای اوب دار آرتا رو گوش بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/84660" target="_blank">📅 15:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84658">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7MMwzQz9udyJNao2ZKFoPKd8UhBpEmlRHSxRvSRMU5zAVquc79OPE3iGoNYBPJAdsP-fgZpxEglvw_8GwMyPOA9fEnfyJYuarU8p4N8IjvDzbvvcDe5cugD3yNaGe-bpLOy5s6HdgXbIgDd6H9OOK0r88IyZIHDrMXM67XS2GszcDJ2A_0a_38STYfw45_0wMuSHsmOrr30pkuMto0gfmGM4YVvxPV8gSGxAkiK-WOco5ANg3e6xvw7oJ2S2ndV_nO1pLpo7ZpQsVmZFKvxKrRsVmAvuXo2yamvYqqY_5AN182WhEO2e9mqYiGF-ZZpe3i33eA0J9cmCRyZi3zhJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-6voDmu0wQ3OTFTCE-GuWa14_9VLkRAIvMZk0LwXYfLx20SuUoM2BX0OQ3bF4j623tftSphVITssQXI86YQNnsvf-EIn-NglSiSNUpEHhoiDmBDWJP4bpr2DgJmEwEwD0lCF5fcH8q4Z8hgVOWvnQUoq0BWHUeGh8tg7nhAyIjMl9KNAkqumFx5ugWnh-7BwiUg38mVogf1wEKJ9efnT6UHZv_xOSlLimDMeKgwNBXrXUjw2x4jf4Bf299aD3T9BiuBN9rGwY43aBDS9uAGoGMpznQWz5_YS1TVkP3fjDfJV371Q_6_Mav0sZsdij89DSzBpjxKtndeJqq4W8UxWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوتیدا، ملکه تایلند برای نخستین بار پرواز انفرادی خود را با هدایت یک جنگنده گریپن در استان سورات تانی در جنوب این کشور با موفقیت انجام داد.
وی همچنین خلبان بوئینگ 737  هم می باشد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84658" target="_blank">📅 13:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84657">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حصین جان جوس ورد از اون دنیا هنوز داره آلبوم میده، این یاد کیریو بده کونکش پیر شدیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84657" target="_blank">📅 12:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84656">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در این دوره از تاریخ که ما شاهد امپراتوری آمریکا در دنیا هستیم و دیگه بریتانیای کبیر و شوروی سابقی وجود نداره، هنوز عده ای وجود دارن که کلش آف کلنز بازی میکنن، منم جزو اون عده ام، کسی کلن فعال داره؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84656" target="_blank">📅 11:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84655">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ:
ما گرینلند رو با قیمت مناسب به دست آوردیم: صفر دلار!
کصکش املاکی
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84655" target="_blank">📅 11:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84654">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFx19AZBOlm_WdDjZ-dG1tga-F2gdCEc0yQQGJf_8gEhe2bPplxZ6RmPFJ__tkpNd_8BqgLCHFKXnvw1xDlFv999nE5oDN1-cTLm8Xe6OOGUlBLkQebGqSblT1rTo0up1y9JcOpM9sv7l-D6yeyLimMGxcE5f4GZG76mE-HOMtZoPql-3Fd4BiZ4Wtkda3wZLN6zJD9TrZ49GP7Fu1xh6BoRYExKsgrlRTZY_0jE_PtLhh98w-qucQRQlt4n0fv3VKPALmaGFy6C4I4FlS_cykcsOzYIrMOIgFXiex0dzAQ-2OFwoT-CdnNpCTQU4XQIqBE0so8rW8N0jLhzfu73_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من میدونم تا مدت ها قراره اکسپلورم با این تصاویر گاییده شه، فقط بگید چقدر طول میکشه، میخوام بدونم تا کی اینستارو باز نکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84654" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84653">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84653" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84652">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4xHSNqQ1N5kHmEESexJLSaN7nXq7ok4888l9CWzXic1V_9G1vT4DZiDaV9NIrFjh5K3L1nJxoXM1YVOcfhqfUA5He144cbD4g6h6SNYr1iU6IHu93t94l9Lkj6513IuBPnQOI9vqAfJAglRpCP9-RavvdNKtejG-UfJilZow9q6RO0YoaoKQYe_Qmv4o_osW_xxk5yf43lNBIVSFZPxg1gfL6qfnbl_SMv8qrscqw20N7xW7gXs8QOJAf94khdCAGatF6sVsNfNRoIy82mTDcmqgeErnLYNpLNoOede3llnkas9ZdvENDU64CLuGxCosyhDUUh7ITedydYrjTjWiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
چلسی  - بورنموث
🌎
ساعت ۱۷:۳۰
⚽️
منچستر یونایتد  - تاتنهام
🌎
ساعت ۲۰:۰۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r18
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84652" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84651">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=EOVWF3xXB5PCQeODaxXpfSPtogcu4FmhzNwR8IBGWmhi43qUzOoVtoz2YmoiACbW57rMONxlswEPhwiGklh45Mj26pZGQ85NQMdAOUsH3AsrWg-8DhpcrSMCDL-6aL0WMiLGVBa5JCXKwBQn8n_T70zZoiNATT0LaXR9lG3YppqEMbYziOP4f6MRl3d01YLG_hVVWWN4CEfXMm6aDdvAMLrTUnMB63Q096ZtwtfHqqqNabRIs3DG6Rf2iGZ_tgF9Nt0jGhExNXwLDujBLoCKnwPxgbv44GtGsa6zi5JZNL2RBWRwaC-7kOH0mggAPGglF2jEy6p8fOhn7kTQMS5fSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=EOVWF3xXB5PCQeODaxXpfSPtogcu4FmhzNwR8IBGWmhi43qUzOoVtoz2YmoiACbW57rMONxlswEPhwiGklh45Mj26pZGQ85NQMdAOUsH3AsrWg-8DhpcrSMCDL-6aL0WMiLGVBa5JCXKwBQn8n_T70zZoiNATT0LaXR9lG3YppqEMbYziOP4f6MRl3d01YLG_hVVWWN4CEfXMm6aDdvAMLrTUnMB63Q096ZtwtfHqqqNabRIs3DG6Rf2iGZ_tgF9Nt0jGhExNXwLDujBLoCKnwPxgbv44GtGsa6zi5JZNL2RBWRwaC-7kOH0mggAPGglF2jEy6p8fOhn7kTQMS5fSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداوکیلی ۵ سال پیش به یکی میگفتی پیشرو و هیچکس رو قراره یه روز کنار تهی و ۰۲۱کید و آرتا تو یه کنسرت ببینی فکر میکرد مواد زدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84651" target="_blank">📅 09:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84650">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258be0442c.mp4?token=a64pIb-17nEt954KNNdzgt9din8p6DBcXmTY8tNwodIFAOR1OcQ1JbM3II-XZdkidjFXZkTfW7JjZNWrqUYWDE8vRSt3wptL-usQuqKl64KV8-3AoXkyDv1a_QirNx3y1RUXPFQ_QLiN0n5v9tzvmBHtzRpPrwMaH7rgBZS6mYtgYHkDndiAFbWmMU1epA8KH0nKi8yahhYzaxuT4uD1PGcehGuPreUbTscDijax9IQMh8C8nGFnC4T8qu_OvlhjOtR4DRG-5rUgxJYXhRUv5xUHDLA78BXuXXa1NMpJsv758z8Yb8jKCxUg8RDgYyJSmbkTJFOXIhsmBjdjO7wlEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258be0442c.mp4?token=a64pIb-17nEt954KNNdzgt9din8p6DBcXmTY8tNwodIFAOR1OcQ1JbM3II-XZdkidjFXZkTfW7JjZNWrqUYWDE8vRSt3wptL-usQuqKl64KV8-3AoXkyDv1a_QirNx3y1RUXPFQ_QLiN0n5v9tzvmBHtzRpPrwMaH7rgBZS6mYtgYHkDndiAFbWmMU1epA8KH0nKi8yahhYzaxuT4uD1PGcehGuPreUbTscDijax9IQMh8C8nGFnC4T8qu_OvlhjOtR4DRG-5rUgxJYXhRUv5xUHDLA78BXuXXa1NMpJsv758z8Yb8jKCxUg8RDgYyJSmbkTJFOXIhsmBjdjO7wlEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درمورد جنگ ایران:
آنها یا همه چیز را به ما خواهند داد، یا دیگر وجود نخواهند داشت، آنها این را می‌دانند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84650" target="_blank">📅 05:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84649">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تو تنگه بزن بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84649" target="_blank">📅 01:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84648">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اوه اوه
روسیه تا ۷ اوریل سال ۲۰۲۷ توسط امریکا معافیت تحریمی گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84648" target="_blank">📅 00:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84647">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7Z35vIP7RrZQXdtDNELk5LYO7kxqZl4S-o75h-UEl9_2czt3_gC4n5ANNLjXDj0550ONFvSpQz54tgqZG3id0-ePque1GtBPmyrDt251T2LisPhmRX0W9crmnAXaT31LpC1zEJivKJ3eQCOnhHJGt574iTtc6amNGF3b7nsMa4el-qZCZ7Jwi2gcNdeMZSVvk-vf5vka7h0cwbciUWlMo_MJ3b7RRlZJ3c5AgVZ0U2ASm60I2HTuWxERNt1zPwAbZb2D96ck-uydXjCbI_zjcaLJLelrDYC1ocJeuaMkZz9UG5zY7CFTmRGNLY8iz29jXUAKSVb2si28AUjuzC_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی داره یکی بهشون اضافه میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84647" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84646">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye2soeOO1qsood6_x1dJ4KdecAqY6bspBUF7x82cwloX2SSFwZFnb48Of-lOzq1sJv7QYpmu1lBW-uRbZboc7Msq0SEBNlIN9pDG0CLI58-NTdRr12ilVyb_ST3LngcdadHjCrF3yKJ8XpNNuzmgrigd-W1NntwMuXzLL6vZvMJd_NFtaeUh_EVPy17NM95b8uQ4ls6cz9xvyen22MUN23V9y0zIskcqvk8TN1yRgTxTQ0ztUjWbiLIVuLXhA-sCRY95WsO3JbigB20VVk1VDSko0zD2GNRdYdbdMv5BPX3uvA19SpyKEddKAiW3HLQeX3L9J6T41u4ZI82e3HnX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان فعلا پست ندارم اینو داشته باشید تا بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84646" target="_blank">📅 20:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84642">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ieead3r858-Dg-Dj8ovBoC4-T07DdPHgMUYwLORFdnK59P9IyHxrH-1qsUOp5DvVbb66riszonLFVoXrjJjzUZf8sCX5UHFrZyMlIhrjwEgSosdNPdqP-9FsvjaFEH8SK107nyqdViv5H_NQKoR-SLqcKg8vf8Zt2YDdY1wnVWVmIRBm-wS40zXCnAuSYYlJMeg_C-Oawvq7tGvlmevlg413Mna6OvBGv1ye5rkN4xCjNcq7696LbReEMhUqWrh0I7bThj6_RjNshhjbXz2LmeWqvi0WZ8vhS6jMr4yYsOri2dHiTJkfyf_tWHSIfGMw2DGHXFMNQ5gsVsTB_4mZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e53eLtQYSOsLKOjgDh5hnBPe6yL4qxk2puXNojIqgXA5ibz9HLcTboQlgNYEn8Gk1xdLEVV2QDAoweC3NwsPlIciqN8-JFZ28DlgKGxiHJw81cwyZqXiB6t4B6dhJiAgZG6vXpaM_01TPeGYrP5Kk6pCA-htdlG-5edmlpOROqPc1SC8KB3vwY7RlM2XzOhzbQloNEdaquzgDC65J1YWQ1YqwmU0xRm4s5jLTBRPYfRZnV94OOe2Jy8L-NEE-vRQ957v4H-YgSXeI8AOGwM3Cv7YlfDQrqx1EL7oBD6B9_rMfe3-UQ9GxhxDD3mmqEvWViIchcPS_ucRWxnL4lrnwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tPi3iS8Q_TgGGyV0__RaxPqNMkYMFcbq1O-uXPfzOkc2pAG9aamcrv015qLFpDJ9WQgtzMVGrqnfXVK0zJTEZpWWMs_4DgDL4RxkTdGvipeRJlJL2xIdc4dZO2_JdF43qZ0w15FHrpp74aH7U3Uoj9izBvNBZyG0luBA6-sn5Xd7XRTTlvNy4if62mnAfA-8CP8hc9mIzELDfCTw1Hnd1P3-GAGC0XFrdBLptsN0W5urhwmQybuGYzbh7HFLiEaYUbbEtGdiL-upqm-OXRcL4agATx0eq5cZ3bRttGyqi2lAJ3jfA80MvZAtsMfOwWLE_3sYzTYUcj5lwkJRn5RWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Yk7J9MMgtEeyOi7oWIgVVi8uBxQrzBbxXMV5QPdrQ3EXbjzntRr_WECkgn0g5EJjUkCkPJ0lN6_KH9U2WHRUkOUQdD1mkMJ5NxE9A7_YLGbx2BJ7sMgvLqH_fg37VHaouQiMBLV8Hfng4n4R65rO749AhYFeSahyzc9ZNnlo7Jejj9Hki_3ZOxrE93KG5z_oZPV2VA6qo7Cknir3FSGXKhe6EkTVwA8ZLHkkFgCZ2yodudNVnm_91kYQUEAfT37g_XZ-SUPbQQCM8uq62w26xWUqKV5gUXfOq6Gsa9RCKIOKJdt0KChry8DAs0TXBtJLEWMI-smcLGQnDGN_Rte3RQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همزمان با ماه کامل بر فراز آرامگاه کوروش بزرگ، این اثر هنری زیبا خلق شد:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84642" target="_blank">📅 20:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84641">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiWB4N9ZFysGREOL4XijXXgActNhsPaFuJ2yX1wFTny5gbLNF4W4Vi99RXclsQnq_O05OuSm7VsTuEajVZPSsswDxIa7uoWiRsIHk9PgdAccZuvedhAtMhblrX3MQ6GgBbjtazMwcn1e12kjSmky6BbLEKmkgnWSW6xxCQdJZmRPdv0AOw9DTVFZW3rSAmlP0hHQLu8qP4LuGcMkz0L2XY0eyI6-B1MK2kFOWYsZlAZk447uKokdwEx1O404t7O1Yd9EkXREoLKdeHuyOhhYxHvONnycq5Tjtd0SNVMX4Yif3u9zrXwue2Exdc-YIevMeSWiEdwkjWGFlx0mYL7_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چجوری مصرفمون از خود افغانستان بالا تره؟
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84641" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84640">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjsRkR1b5Ju_JL-gajx1dQ2zYUYona3iN_SKK-gfEHanAyeJmKj5DP2SREVOeX0hUUPSV1gzK55qyRbFdku-134RlQJrgtvPb-qG9AILIlXzcWZEh8MfPysaA095nTVvlgJ7BzR5bQGS9GksBxzzwPJXD4yUOQXupkRmBrUlWlGd0OpfAkFAD4z6n4sfaP7UDH1MTvtye6AfOa2bMXyR5pVeK0oKBMQb09KnZ7UCPJuxNHThJfY0nkBF6YgUg6ci5wKZb0LBZTNj4sYjWJLis4QVPeAK7XXLxjaEcDlxhJQzO3-yhvq9ZejmGgLgTdHO2rHDliw1hGNpOGuyZMaWUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G17
🅰
🛒
ورود به سایت
👇
✅
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84640" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84639">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iORZGs4LEiUPXR1P9qSU58c90TdmrzX4RpIHafnXxAVOj-it-AJ6OzTr8q5wiYeILJFz1OQsLM_0FJIQ-8LTQYODn75YyUsDZexOY5alxcXudM8toK9qHveZ9awTHiC43nQPGLee7HQJlXTLA2t7gFH_MSdaXYuA2eddEcGOrZIJdpji92cd5JJsJDZzK9PfApwoznb79Jfx-j4Z-rwOrFsoyGPJB8Icjh8sbm9qMwf3ypXgIZTOsc3R_kZmWk22NnsUBzhEfY3b9U4wvLZCH-yxC47-h_5sm8ZegJJl9jpFkQOoy1Aw6Jo_JU9UxPzF7xeplX20s5ceRAZ-5IJLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا خودت رحم کن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84639" target="_blank">📅 19:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84638">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvQYMgJcGDro8wu9ZBE0JgEQ9pQojvpGdtT7sfKh7oQ1sfWrAUlFfMtBk_Gh8mRllqDWTPckw9uI4XwM4vXHyufQd99SFd8WZ_7GsMbAMg0_JtPi0EcsuxZNSq8OqPpVg7EGxda7sB-KZDCScmF1bT91LV6OKB9mcIeCXjj_LdMLUY0wzIulyRYH9WbxhwiU-831v24-nt8iWETrPivxqPyMssuTxXwBLVNUsyIXP3BqSfQ3fILX5OpzKxyOYyL3PHlvfBKwdEGMYKpG2s3ihU_X6q5aqsXt7reUwWN_tMN0_6xQx3ihbxRqhlz-rTk0ItvhSOMbxm1p387fkV_jig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب ترین چیزی که امروز دیدم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84638" target="_blank">📅 19:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84637">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایرانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84637" target="_blank">📅 17:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84636">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خدابنده‌لو چقد شبیه رودری بازی میکنه</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84636" target="_blank">📅 17:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84635">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش‌های اولیه از کشته‌شدن معاون اجتماعی انتظامی استان در پی انفجار مین کنار جاده‌ای علیه خودروی نیروهای انتظامی در منطقه چشمه‌زیارت زاهدان حکایت دارد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84635" target="_blank">📅 16:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84634">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">میرسلیم، عضو مجمع تشخیص مصلحت نظام : تیبا در سطح ماشینای معروف خارجیه و به راحتی می‌تونه باهاشون رقابت کنه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84634" target="_blank">📅 16:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84633">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84633" target="_blank">📅 15:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84632">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84632" target="_blank">📅 14:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84631">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-0UpD5607WCUXB0Pwv2gubJ5WzJSsPx4ynFxS4EDzkI8rrJeuCJoxF3F4jygnmY6BecH6Z_NNqKDW5lvOOyA48m6cArWKjPspxVMrwYdcrMbzQv6GX_2Ou_fZuACpKAptTU1LL76Cx8FaRCC_3CA2HmVz-gzFrDVJgvKztQnx1m3abcwKfhkVmfFdHqBxmvXjmaKjzswaS0osa1LtYY36ykXo503VCHAtEv72m9KY-Lh1nhEduTkumv0cQuUPNtjZEVv1d3g8KHReG-zP4OIU8Uk4PB6FGS7phQi720ylBbjq1koF3_9rs_J6d5blyOY96tjHruFb89h_YvDD8bhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا حاج اقا
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84631" target="_blank">📅 13:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84630">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84630" target="_blank">📅 12:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84629">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84629" target="_blank">📅 12:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84628">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84628" target="_blank">📅 12:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84627">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromᴀᴍɪɴ.</strong></div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84627" target="_blank">📅 12:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84626">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMt16kPTvbhOlUvGh3lvCaukDZDvod8oRtsOEQqxMdK70BdekYEdOMIBnVAN-PvfSzuy-eCzzvSFR9PwtFoJqISrTbPRh519NtLsREi5iJO7aNywTHTHyg4wYt1IDzs6ztrdVUEKlqJbokidDcwVE3alMIdLsVXodjYcHvPCbJ7AO9aaOHuvFtX6QsutXp1D7euxFejNkNOETV6WAC62Gi2QwAWkU4o_CB5rmEDUA3rVcDTFo8SaDw4jgcgrrUippkOfFgyATGpOVYwHuh4X3stjsMeLGLZUVfc9GhmQ_1Ioo7DyVU8viYxCltdgiNtfD5wIxAnyxbuK1e-0veWwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا فک کن فیت بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84626" target="_blank">📅 12:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84625">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هالند و امباپه تعویض بشن بین سیتی و رئال جفتشون بهترین تیمای جهان میشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84625" target="_blank">📅 11:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84624">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8X4tDUlypycdty65BnhJbB_zVnkSJ2P_pxJx6Yh9GveQElTBdBxgCcufvupsNbSIt8o1gnduIeKpfPksjbfzVfaNy8OmK0uV9kQb3DnTuAupUyL04iqKy0VCN9Ac8E7p5gFlLRZbt5uVm3GPzVI7TVZN5aDz6qs_uZmYt7m5tYCzHQeT93qyoAVHG6T0mm4aGBmiDzB_3ae5M0Zpn2FNPqPsC18ukHVWWOg52cJ9nygphBtsUvwg5nnUKdwm10tYHPPsmJKsgJNZDHICMCy-3zD-11BM-aM2_m5xa6wvi80JZyMMRPS0VzbIeFaTix-k3CuKuOscIrdJL7TV10hRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس داستانای کیلیان دیکتاتور حقیقت داره پسر
آاس :
امباپه توی رئال هیچ رفیق صمیمی‌ای نداره و اون توی رختکن رئال احساس غریبه بودن میکنه. با بلینگهام بینشون یه جور تنش و سردی وجود داره، با وینیسیوس هم رفیق نیست و با بقیه بازیکنا هم رابطه‌شون بیشتر در حد کار و فوتبال حرفه‌ایه. حتی از بازیکنایی که قبلاً باهاشون صمیمی بود هم کم‌کم داره فاصله میگیره، کلا تو تیم کسی با امباپه حال نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84624" target="_blank">📅 11:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84623">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gud47Sg0dhK-HP0bf85s8a-JWyRCB4M1_lEgfR0Ie18RWPvIAhpTNqJf86yXVkeh3LbqupZMJxEbPaVk2r3kQgE6xXCvtkdOThbx_k5cF9uJ89f0WgzqZE1Vu1fjrz7h8OafjhHIQg8cIENrL0geF8K4_dI8W5iAGWmx2U3MG4pz_irX3oJDka5uZhNToMwVgPohpBzV8n9gtQONJdGmfGmOHZkLUBYfkw_VxQoIL2wfbyHYLNkaDzWuXh4Mf7FUhrKKJqw30csKlSUp8QjP2ESq07C9ijNMdN0DYkRW2lpT9QzlGQJPQShz3ErtVcx2_XisZo4VqG1d6j0xlUpyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستند تک قسمته ۲ دقیقه ای(یک دقیقش تبلیغاته)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84623" target="_blank">📅 11:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84622">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عراقچی پالس های مثبت از مذاکره با آمریکا داده، شیشه هاتونو ضربدری چسب بزنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84622" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84621">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ویچرت؛ تحلیلگر معروف آمریکا در توییترش: اسرائیل دقیقا قبل از‌ انتخابات آمریکا به ایران حمله میکند. این پست رو‌ ذخیره کنید.
پ.ن: این یه بارم گفته بود آمریکا لحظات آخر جنگ ۴۰ روزه میخواسته به ایران بمب اتم بزنه که ایران میفهمه و مذاکره کردن رو میپذیره، قبل از شروع جنگ ۱۲ روزه ام میگفت دیر یا زود یه جنگی بین ایران و اسرائیل اتفاق میوفته
پ.ن۲: آیزنکوت رقیب نتانیاهو در انتخابات اسرائیل هم دقیقا همچین حرفی زده دیشب
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84621" target="_blank">📅 10:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84620">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">من جای تهی بودم دیسای قدیمی پیشرو و هیچکس به هم دیگه رو جلوشون پلی میکردم و از واکنشاشون فیلم میگرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84620" target="_blank">📅 09:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84619">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6Wy3TlVmE3kUFSSaLQRP8ovanN44k6_qWkqsZCwBRroGjpbrl1PswrnYmXbYbcfb15bggc4a0MeoD8K6IErXsnoDPRtzctji5tIDZjlFW1ksapNyefK5dFeOHg5Va-kxsTVaVU8-WHTJUiu2lTyLArqVyg_QlO6j_8JWyiskU3vmmTT6DUd35kq0vk9fQQ57JqxCxhK_7QDqaWU71UO-2ZrcRxuT1QOCWrNiZyuHpqAssjioZ4l1V31ZrsEJhr_NCRKD6PJeleQDRsFtPzuP5u8YnYh5OdeoeiocL4UdhJxtq3_qFl0zuP-Mzm4FBpQvLngjLxZaDIPrp3p9KrP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی کیر تو روزی که با این تصویر شروع شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84619" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84618">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84618" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84617">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDDQr5wECJ0ZV-YzHh1uHfRg8suECEXNq0ZWj7gM0df7CdUA9NnF1JLSB5LmB02oGqpMINFpcFY1DQTllH4U4fdd2UY4p6gVfCYrENasuZbtE_AoTG3Y-JGTHYCBoS-_ENb7JW1fZnK7vywzcPy9ZAbC2pvKK0MQ6aIg0ImuS2N-7nU5oIhzsZ9yQ7WSz_3E-x8bb4F95Lwyg2CW8bTnka3DkP2oLMP6GO1r9lIh7IH-I19w5YXlN1ymTsT94FnKCQCVR2k6bsuB9mYmLS6rOOjFSZBmuJ-rIy4BpJjIf9jS7aIyTW4ErjNaPEdK_mPfCx5xmUnFJMtlLEtfnY_iOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
پرسپولیس - صنعت نفت ابادان
🌎
ساعت 17:00
⚽️
چادرملو اردکان  - خیبر خرم‌آباد
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r17
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84617" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84616">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=Z6QR_apWJUzhKvWbPHBG0mE-OU2duqlKv6e4QIxYHC01G0wJaUoDk7E3Hf26IQbhRBaDqOLO1oxQvPaBTZfxX9eLQA8k6q3Djnawje5S3G-GWYSUD9oUC1QLOnN0UAkE2mcN1OXzAsZKTMAQo7JDsDy5la-mDJ6kFYp_kNkRuZfNUzWtwFR50PnMyioQ9h76HxQJiLY0YJLDa2MtceX_eywTA4dpsl2nxdLLpC4HKbe-5XuDmMMnlkNZFd7YoOGr9TyrtctmWnzj2-2Z0QKWcnEws1MA5zPDZZQhmB5OTYSxLrQgM14ztWT3Jdx4HRb5Yd627wksD9ernMrk9PwTmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=Z6QR_apWJUzhKvWbPHBG0mE-OU2duqlKv6e4QIxYHC01G0wJaUoDk7E3Hf26IQbhRBaDqOLO1oxQvPaBTZfxX9eLQA8k6q3Djnawje5S3G-GWYSUD9oUC1QLOnN0UAkE2mcN1OXzAsZKTMAQo7JDsDy5la-mDJ6kFYp_kNkRuZfNUzWtwFR50PnMyioQ9h76HxQJiLY0YJLDa2MtceX_eywTA4dpsl2nxdLLpC4HKbe-5XuDmMMnlkNZFd7YoOGr9TyrtctmWnzj2-2Z0QKWcnEws1MA5zPDZZQhmB5OTYSxLrQgM14ztWT3Jdx4HRb5Yd627wksD9ernMrk9PwTmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و تهی رفتن لندن که سروش هیچکس رو از نزدیک زیارت کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/84616" target="_blank">📅 02:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84615">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YV1sP59TdhPRSB5-Ymc_ak4wrBtsuk0rjPxnw3SXUF6UJDdLeT9s4og-s5J2cr3qQHV0jS91guWCoQVYNRYQOWfDrdmuqLf8E1d6SHcuNTJL74-h09XxCIr9RPH_9sgRg6uc9cgOxpKFBmhjqKYEndHB-Uglcf8fF_nOw_waz9UwtnFBuqJ5U_khA1EmVMTyWVRNASQ8HrbHTrPGelK4s5sMkQF-A-Dyk0reXL4NHKfeq3csceji_JjiaNI3LQrpMNr5cknKD0NWbIQz4k9gYKz-YlceeZmkxyySI7WKektIZarOhvutxWkkzWQVbJnqY1kF2APJW7tMfYFe5JaQPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز شیوع طاعون تایید نشده؛ تو ایران شروع کردن ماسکش رو میفروشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/84615" target="_blank">📅 00:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84614">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سپاه به اربیل عراق حمله کرد، احتمالا هدف مقر کرد ها بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/84614" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84613">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/84613" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84612">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=XRFRNtMkmJ2T0AJQlKBhx1IX3RyNm8pJaQA-23vDMXgiGd_eHoKdl6VWq_-Hf3cWHrXBrRQOuZpn0fF2If2Ou4lUyn9rFDxEEbbP-d1V2vXKmkDa4sHsHH9rtrJGqKREa0HMzPGxNkDOYOdkKYMpdrVhOFtkUK18j5gkoyCoCjxBudyfjmzR52r7Naj90XQoBe0lAV4I9iZ02TqoyD1hid3Zc6IA9hqG5YwwNioEwZBe12sW9o9lAnLI9jymzOaEFdNitiSiF1XdpETHvMJS64AE7zM2p01J7ZM3RHanyaE-Q6jH7bcYy-o622WiPKVx-yhg3CwI80qn7qo9d6yJEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=XRFRNtMkmJ2T0AJQlKBhx1IX3RyNm8pJaQA-23vDMXgiGd_eHoKdl6VWq_-Hf3cWHrXBrRQOuZpn0fF2If2Ou4lUyn9rFDxEEbbP-d1V2vXKmkDa4sHsHH9rtrJGqKREa0HMzPGxNkDOYOdkKYMpdrVhOFtkUK18j5gkoyCoCjxBudyfjmzR52r7Naj90XQoBe0lAV4I9iZ02TqoyD1hid3Zc6IA9hqG5YwwNioEwZBe12sW9o9lAnLI9jymzOaEFdNitiSiF1XdpETHvMJS64AE7zM2p01J7ZM3RHanyaE-Q6jH7bcYy-o622WiPKVx-yhg3CwI80qn7qo9d6yJEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوجی انانوبی بازیکن بسکتبال+۲۱۰ سانتی نیویورک نیکس رفته دایرکت یه دختر ۱۲۰ سانتی و میگه بیا ببرمت نیویورک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84612" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84611">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=dtklyNeXDt3lr62w1C9I486HmledNviaezME800gGvNLiMYuJIvwscbMdVuboy_ixLPJ3AgpV2QooYb8PRym2nTZMPA2v7mSO65HVyrO55u3oww_14_i5_2lE8sNCeqR5OaZOQnjisMcteX2WHkxCh9NMKbnD5NILkXxveBemLInJeNR0M3Dn9XrRtZSz3-cSaZTYG5N5p61bVnkFecsp8dmngTNG-xVmmOecjlqvUamRKlyDzrWTrSBE3pzEkssUBrR3JFz6vxWvizJ_cnqQKscLJBbWlIFQi7YFUVm-b4OKf1jbInerDFc_1QJI55O0vukKz9-z9F_AvOn1-Li6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=dtklyNeXDt3lr62w1C9I486HmledNviaezME800gGvNLiMYuJIvwscbMdVuboy_ixLPJ3AgpV2QooYb8PRym2nTZMPA2v7mSO65HVyrO55u3oww_14_i5_2lE8sNCeqR5OaZOQnjisMcteX2WHkxCh9NMKbnD5NILkXxveBemLInJeNR0M3Dn9XrRtZSz3-cSaZTYG5N5p61bVnkFecsp8dmngTNG-xVmmOecjlqvUamRKlyDzrWTrSBE3pzEkssUBrR3JFz6vxWvizJ_cnqQKscLJBbWlIFQi7YFUVm-b4OKf1jbInerDFc_1QJI55O0vukKz9-z9F_AvOn1-Li6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرقت غذا تو یکی از فست فودی های کشور:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84611" target="_blank">📅 21:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84610">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=VzUtNN_TzBRIUnXprDnl-o-_Z_J4X06sg_sfJKF-P-ByZsXtzsSXvGCw0famw_KC2P7UxP3sQuhgCWdGBq30f2fBtxImmMU72xidsDBgW4x0tKwX_XgaJ_H7wrCS6r5gsMYw_Qlf_v3j1cGIF-id4LaHwCcX0WkqS_3wdyyQa94vD4_avsfMATCf1tC8ssEQCUQSCTeuGQm9ZEuRKNSL9ZwMvao0n-D6FitpXB3TMuxX5q6AQlDedF6CASyr_8TyhGwwZzarzl4isuPNJZOzA8ojRXyPvVcIzuprBBH3f8la38ny4j2hlHsI0DcndZK7mF1rZ-qzMTijpNtfQaJgRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=VzUtNN_TzBRIUnXprDnl-o-_Z_J4X06sg_sfJKF-P-ByZsXtzsSXvGCw0famw_KC2P7UxP3sQuhgCWdGBq30f2fBtxImmMU72xidsDBgW4x0tKwX_XgaJ_H7wrCS6r5gsMYw_Qlf_v3j1cGIF-id4LaHwCcX0WkqS_3wdyyQa94vD4_avsfMATCf1tC8ssEQCUQSCTeuGQm9ZEuRKNSL9ZwMvao0n-D6FitpXB3TMuxX5q6AQlDedF6CASyr_8TyhGwwZzarzl4isuPNJZOzA8ojRXyPvVcIzuprBBH3f8la38ny4j2hlHsI0DcndZK7mF1rZ-qzMTijpNtfQaJgRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچ کاری به این که رئیس بانک مرکزی ایران به وزیر خزانه داری آمریکا سه روز وقت میده و این که دقیقا برای چی وقت میده ندارم.
ولی چرا میگه ۳ روز بعد با دست ۴ نشون میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84610" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84609">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=KYNKrCzklQ26wxj4fhNA9qKexZsbK88zvQFFuzIAVjw57HuNIHMIwyfzo5Bd24rA__9JBqh2aII9spfQCNRMaITOoKtpE4yJUfcfhnrYGR44vBEYxKwluAHVMLmMMx9yocAQpgH9VmRsD4ex8E-1qZT_FK0nD60fKOk6jhZAmjpErJw7Y29_p51EWZtjIFZENrj53ByaGydshD_mBqEvj756qBnXt69iscgCVf01q2qHnwQwNFjQ2unjlzu-nKMtQMOUexr0JsqF73ZJDgLAwC9DqlygEcZsnWuyhll_Kmx79VwISLpzf5sn420iSyHooCUtSfvJYLEE2uhYQAQwUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=KYNKrCzklQ26wxj4fhNA9qKexZsbK88zvQFFuzIAVjw57HuNIHMIwyfzo5Bd24rA__9JBqh2aII9spfQCNRMaITOoKtpE4yJUfcfhnrYGR44vBEYxKwluAHVMLmMMx9yocAQpgH9VmRsD4ex8E-1qZT_FK0nD60fKOk6jhZAmjpErJw7Y29_p51EWZtjIFZENrj53ByaGydshD_mBqEvj756qBnXt69iscgCVf01q2qHnwQwNFjQ2unjlzu-nKMtQMOUexr0JsqF73ZJDgLAwC9DqlygEcZsnWuyhll_Kmx79VwISLpzf5sn420iSyHooCUtSfvJYLEE2uhYQAQwUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد.
از این به بعد در سراسر کشور، با خانم‌های بی‌حجاب برخورد و براشون جرم ثبت میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84609" target="_blank">📅 20:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84607">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6f2ajyiwCGt__iMQV3QIK07o5hk5j0hicei1SlgPEH3WQWfEBI8lQuvRc1E4X9j8WJrzZ9ooMTquQ0MDysjC47h9P7pHPIr_v9EzTVpBBI-g7nxlUqA9Ppzoe0nPZQ4ZCKDt0DyTfnjI2m-F0O70KufLEbrg5ujNsHQEnKjqZCfI2CbIt4Lc4FvCVGWFmKQ8HPlan30iP3qA2umuiEaQ-UQ38XrPMs1L8nLQd-Tc6ZTd4GpxzPRgprOqqEpUYFHcNNO89wCMD_7l3UrWWpNULSvABF_81fd7S5aGvluw6Nd5sCLSeqvjJkSWPcO_n-yUJRKNrChFHluKBIkniM9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان پاشید یه جوری شیشه‌هاتون رو چسب بزنید که ذخایر چسب کشور تموم شه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84607" target="_blank">📅 20:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84606">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBpWIQCcPMKW3QbQoVdtOZWpIMzJG_MlQslK-3W7PDSVFIBbxzq_jsmVJt34_L7hM4kIwxLa3RXDQBMp6raL52G-Q5KFkzgoZHh6oHWf6RTZFt4Zh4imoduYSCrZnB5npNKv3_6HFd7M1JgokyRpeHLti43QgdXJxEVQCvHVZOZQF1zK7v40JfhRTPUQRhCrHqTUu0cqaY9hg3klHL1q5Mbk2GfWkoyinzUpgVgyiaf-ctMCbUwuJSzUUiN_tP8god9YuXUdVEZiIQ3ZmyGoPiaTcUMBewoCc8asb1AkaM-NF2X37vO-1SkPY_Upi-afOxwO8r5FVHHhLGPpsXw99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خخخ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84606" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84604">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCqTfHtLHzsMmfYI27gx3D9zotmrcr2QTJvBq4APRL5SxbKW6NpTYX8h4HcSl-9kjNV-U9YIT0nDJGfaS4oDc6yR6k8s8tjtHhpB8g--DGpfQhvWDiEbm3uaFggnra_2WC6AkpTr0d3QIwWMR3F3w6breFK6sJIByHE6oDmppUw6kJOsOFwBoWTI5jjL4tTaAqMdjQJx_s-lKIuJBumofrY4tk4RPbK7V2LvjfvpnToHobrs2lvn8eiuZVth0wIgGLbbwT3IifHEp5Xl9ReMiXZHmlHDTBzaTdD661roOik69JvijfLBEG221yP5grdoe06qyM91tgn9ZGkBhcL3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توماج صالحی با رپر بسیجی‌ای که شبا تو تجمعات اجرا می‌کنه درگیر شده.
(به نظرم رپره داره حق پسر ایرانمون رو می‌خوره
💔
)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84604" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84603">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=J2d8aAu4zOG_DPafGGM6Rr35_izNZa6B1dGam9IHSbchiL7piJlDpGvZXMx_XoJfBq5vX7vmDgi0B3K15PLhMu1BgbN9ooxFqvXCXFd0rXRfq16gvytcfWTTBcwoGUBoLmcvpXT9T7ue9MzEvOKLxy92NPlAgSU7h_NRIJKKrZQYjYFBY3fe_NSQZL9Iq3TIAMMsQmBliLTfUP6qlgtm38HgZHvzhVE8jAoecTcx5yjIwDeh3ffzaKNh0uUsuiDlFKIhtKQ8KwASBaBy3Xwtrtu0oCerfBeJDEts-SY_lshRxqnZ9Y6m6l3WW9YrwlwBZ7AGKftWmJni9HrB7_ABmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=J2d8aAu4zOG_DPafGGM6Rr35_izNZa6B1dGam9IHSbchiL7piJlDpGvZXMx_XoJfBq5vX7vmDgi0B3K15PLhMu1BgbN9ooxFqvXCXFd0rXRfq16gvytcfWTTBcwoGUBoLmcvpXT9T7ue9MzEvOKLxy92NPlAgSU7h_NRIJKKrZQYjYFBY3fe_NSQZL9Iq3TIAMMsQmBliLTfUP6qlgtm38HgZHvzhVE8jAoecTcx5yjIwDeh3ffzaKNh0uUsuiDlFKIhtKQ8KwASBaBy3Xwtrtu0oCerfBeJDEts-SY_lshRxqnZ9Y6m6l3WW9YrwlwBZ7AGKftWmJni9HrB7_ABmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
روزهای
بلک جک فارسی
در  Berrybet
💸
بازگشت نقدی:
معادل
0️⃣
1️⃣
🔣
از خالص باخت
💎
حداکثر بازگشت نقدی:
۱۰,۰۰۰,۰۰۰ تومان
❤️
🤌
حداقل شرط واجد شرایط:
۷۵۰,۰۰۰ تومان
🩷
بازی‌های واجد شرایط:
فقط میزهای
بلک جک فارسی
از ارائه‌دهنده
Creedroomz
⏰
روزهای واجد شرایط:
دوشنبه، پنج‌شنبه و جمعه
🌐
ورود به سایت:
➡️
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
🌐
تلگرام ما:g16
🅰
➡️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84603" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84602">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=i7S-WU4v6noS5CObpktHhVKeF_X0yeBQ__qy3yS33c7YzkD4BBBuVoTI2l2BYfhGQOpnb2zKvAD8upEBGC5-bpy5u9w_zBJNo1pKoC5NAHOjrztOy1PYxwlRj5egLFU-ZJgl_TcNJ9GljgfcUB2r2tSmlv14OtH16kz_06lf3Ny68-03UQBiJczphFppkkV-oWUrPZ3tghGVOawfSDeCS1NriZQrjbEX3fIzCdUwkA2XeejrnDQGu8xj-vvbeCBoHeXsmHoRW25Agx_mVRkEnY6x1CZbantJCXYF92Qz3Unaz-XUBUTEezrQyD3g_UbcKq8cDjxqbpWF4QI72Om_nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=i7S-WU4v6noS5CObpktHhVKeF_X0yeBQ__qy3yS33c7YzkD4BBBuVoTI2l2BYfhGQOpnb2zKvAD8upEBGC5-bpy5u9w_zBJNo1pKoC5NAHOjrztOy1PYxwlRj5egLFU-ZJgl_TcNJ9GljgfcUB2r2tSmlv14OtH16kz_06lf3Ny68-03UQBiJczphFppkkV-oWUrPZ3tghGVOawfSDeCS1NriZQrjbEX3fIzCdUwkA2XeejrnDQGu8xj-vvbeCBoHeXsmHoRW25Agx_mVRkEnY6x1CZbantJCXYF92Qz3Unaz-XUBUTEezrQyD3g_UbcKq8cDjxqbpWF4QI72Om_nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی رشت رعد و برق جوری میخوره به دکل برق فشار قوی انگار که زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84602" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84601">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84601" target="_blank">📅 18:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84600">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هوا الان یجوریه که همه تو خیابون فکر میکنن شخصیت اصلی داستانن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84600" target="_blank">📅 17:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84599">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حالا من که میگم استقلال یکی زده به تراکتور، ولی ناموسا فوتبال ایران دیدن نداره</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84599" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84597">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/84597" target="_blank">📅 16:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84596">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84596" target="_blank">📅 16:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84595">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmV-rqWjKggMoqmqgwZpr_lV1tRWAQZ54H4OWjcCAbVYjP3NTnNs7LcAmtRYclh4qeoxp2rlcM9rhNZrPGYZPh3CSsFE7ct2vU6aGi-wki_HxuMtXtxURJ_Ki6abMAgFg1Q_a4Lfe5lScvSct6ZstE-OTsPrs5tulYGR0H4tPXeh7hYgffB5XtI9POgJB8yRYXZFi5ZN1nhd6yJRdK1sA41BNOIgQbfKU5__KhRwxHd4caevr1tNUSflO-_t7rHEw3xq2_qU82PxGyElsvTEZDEDkTp9RVR1s771AGpyI-_6xL2MMehaSg1_GgPLHehXCwgN7CdtSSZD0pep9WZskA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر دلو فوت کرده
خدابیامرزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84595" target="_blank">📅 15:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84593">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Us-5DdWeLD8_LwPPiNDRZ8wakpDoTwvfaAcZa4Qdr2Bj9dRP8HJFo6FxcCG0R-JcqsInrBvSC6fJHLPi-RlaUHJYaC0h46YGDhhmeG7pF1pRs5akDMH2MY-egN8vATJuxDZuXIjQNF3wQH3_CId8vu9XfgKZMNuZQz1dJrf8K4JKIT4nMsjiDHt3GzUqcEkXYHJX7RjmqdWpO9KlxOY82M8ZJWiok6Im6pltI0HgX1cFeMKF8LnE-5Y89vV1pOFHgpizoHWg74Q-n6tB7KZTAoeBJZaDLWwQIp-MtsioQjHjMGzbdz2Dhq7dPmaEEXljOPmNti02f-o8tv86bP2yYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1_eneOjXyyPaGBSbgTtotDQhPIHhBeZNNNgSiYQ4EtFYW18F55BpE3aetXr7RailUyxnTp2w9gmTwmM1jzf1nmN2ciC49dCIIXTA31iuZRu2Bl2VnoEIgi1GtcYakfocDfu8hXY7LBYKi9ZVHzboMCg_y_UtrmeDjMKEvR7X5OvVxEn6BOZDtyDmdH9h-pBAWm5fNqWQR2rgoZd7YzZ7kTcifp4TodpZ5J58912o-zSfaVmxHqXSRc9vzay7Ahe8kpkmiH7tLxfJHCiBp7HaOkPVRWvps6hjJNK__DYDnfUq4oyHMGVgKA-TQ4QKK7VkpScMBJQUnoAPAkHUxX8CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشتی ریدی که
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84593" target="_blank">📅 15:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84592">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مجری صداوسیما:
گاو که دلار نمی‌خورد، پس چرا شیر گران می‌شود؟
کارشناس:
اتفاقاً گاوها هم دلار می‌خورند
عالیه پسر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84592" target="_blank">📅 15:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84591">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=Z3vv0SoizIKW4LVKlHrvW_4kKR-_5sHxHGF0rMOFfbjd-6_XWEVraTMNv7jjKc9Wwj71RV2ezaC8mepBvmZiP_y5C3L50tzslvRYf6ZsxgyF6nGfFzoyvNZt-IRh4SapFqL_vlxJEqh82ReG_w-S8WlpgacIDs7IhDYiM4lkxU_SAP8Gj_2Z9dUYCkKgbbvf_mCCvNgnqsQqljRfE9EX7XvXnvXqepAsCrVjBRM-T5bgCT44RVtxMyJoqBIV93DG8Piue_nV5yStpxRuqgUXMAsInRT0kNPAJWwgnTaPc3HERV0jV0PIeS9VGL4wuxLX8oH5rvLhy22eBjl16fGEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=Z3vv0SoizIKW4LVKlHrvW_4kKR-_5sHxHGF0rMOFfbjd-6_XWEVraTMNv7jjKc9Wwj71RV2ezaC8mepBvmZiP_y5C3L50tzslvRYf6ZsxgyF6nGfFzoyvNZt-IRh4SapFqL_vlxJEqh82ReG_w-S8WlpgacIDs7IhDYiM4lkxU_SAP8Gj_2Z9dUYCkKgbbvf_mCCvNgnqsQqljRfE9EX7XvXnvXqepAsCrVjBRM-T5bgCT44RVtxMyJoqBIV93DG8Piue_nV5yStpxRuqgUXMAsInRT0kNPAJWwgnTaPc3HERV0jV0PIeS9VGL4wuxLX8oH5rvLhy22eBjl16fGEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز، ۱۶ مهر؛ روز بزرگداشت داریوش بزرگ، شاهنشاهی که نامش با شکوه و اقتدار ایران هخامنشی گره خورده
👑
داریوش بزرگ در سال ۵۲۲ پیش از میلاد به تخت نشست؛ در حالی که شاهنشاهی هخامنشی درگیر شورش‌های گسترده‌ای از ماد و بابل تا پارس، ایلام و ارمنستان بود. او طبق کتیبه بیستون، طی ۱۹ نبرد مدعیان سلطنت و شورشیان رو شکست داد و دوباره یکپارچگی شاهنشاهی رو برقرار کرد.
در دوران داریوش بزرگ، قلمرو هخامنشی از شرق تا حوالی دره سند و از غرب تا تراکیه و بخش‌هایی از بالکان گسترش پیدا کرد. او همچنین فرمان ساخت تخت‌جمشید رو صادر کرد؛ یکی از ماندگارترین نمادهای تمدن ایران باستان.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84591" target="_blank">📅 14:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84590">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نیویورک تایمز:
پاکستان به کمپین نظامی عربستان سعودی علیه حوثی‌ها در یمن پیوسته است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84590" target="_blank">📅 13:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84589">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خیلی دوس دارم صبحتونو با درو دافایی که تو اینستا دابسمش میگیرن شروع کنم ولی اکسپلورم کلا شده کچالویی که باباش داره مسافرت و بهش پول داده تا ۲ سال دیگه برگرده ببینه با پول چیکار کرده</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84589" target="_blank">📅 12:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84588">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuQ1WIerTQlGJWP1GKUQ8DFEY8viNqfFkzCHVN6hnO6lOavLmR2zJYA7OBKPsT0o3-Ht9NNb1iHCvii5sDj8XhCLLnX8G7W8rXDri4vv9KwJxJdWZer9WbkWZa3IPGwtYuZ_qPH6eiFphMNa65FOK31VyU2Lh9YLhw7R6rt5bG18LGMRma9pOvOqhh-5wpEY3aRGXNwe29gaWLVEYY0H4hFhYKVCG5UN52mcgeotcSNUg_P33po5qA6R-ND97x7O0ZDkLI_zkHnGC-kzpbDlfcl00E9bpg4ZK7d3M-JtbAxnM2IKVrRt3tXakw3Ilxaw0fxkIcIiVVEXMWZ3z9Mrzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84588" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84587">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84587" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84586">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQmZocxghImkt88_vPe6YjrLmRBeM3F606CV3UllSTJRYLJZ2OVyGvxw_Dn1_9qxc-7l2fTYGwIQrM2COAoQddsIJgMbtBz7hhuLL3sxOR2WUGu9KS-xK78WLUlmzGMKKiUrrfCvLtr8rQLfVRuX-ldTLQN4OQPH8p2E5j9vCB99z8c06tyEsb-Ww2APjqSCmFsvpQNgU0QFVoJQLScnjF4XuNCsl6J6Xq1J_KIuZ7vDnHAPxSqw7E2k3B-Ytd24pmQoIYKucgmQ5JwXddU6G5NI9FroU_bSQAtxRV4WMqAaZiQwp4kvBKNNN0LzRQBeQWCjk685eeovB57OTIXeMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
آلومینیوم اراک  - ملوان
🌎
ساعت 16:00
⚽️
گل گهر سیرجان  - استقلال خوزستان
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:r16
🅰
🔗
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84586" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84585">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خیلیا تو بندر صدای انفجار شنیدن حالا معلوم نیست چی ترکیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84585" target="_blank">📅 09:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84584">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وحید جان بیدار شو، زدن</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84584" target="_blank">📅 09:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84583">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4894c49154.mp4?token=U_yUJRzasHfkHdgotApzDxKALXB_dCyPQw6PhGCuknhgL9mr99st_SJwwerpxqHrKutElkvV8wR-Nz6ttRs41YA8R0hfrmM7R4EyPRp0eLHKP7uwQ03-JhrWtcoZDi4kskgOHGPHjTloAalkb9LatnzL2ehkLr-tnIt9XMcnp47Avm7ri6xvA1wILxGKiVD0AvRWQRrmFjDbWFVpt3hIlJiNp96e7PnzVJlY_StE8mGhpMWoeSiZvXRZdgpNuvboGHGKv21Ph8iIDe1v3UYwKmeNZxI-UEMppfqExwA_up-z1ZqE5CUnglDSIPMowrcjYA2demIXIQF2jT9L3ceMbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4894c49154.mp4?token=U_yUJRzasHfkHdgotApzDxKALXB_dCyPQw6PhGCuknhgL9mr99st_SJwwerpxqHrKutElkvV8wR-Nz6ttRs41YA8R0hfrmM7R4EyPRp0eLHKP7uwQ03-JhrWtcoZDi4kskgOHGPHjTloAalkb9LatnzL2ehkLr-tnIt9XMcnp47Avm7ri6xvA1wILxGKiVD0AvRWQRrmFjDbWFVpt3hIlJiNp96e7PnzVJlY_StE8mGhpMWoeSiZvXRZdgpNuvboGHGKv21Ph8iIDe1v3UYwKmeNZxI-UEMppfqExwA_up-z1ZqE5CUnglDSIPMowrcjYA2demIXIQF2jT9L3ceMbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ آقای زنوزی پولاشو از کجا اورده؟
- آذربایجان ستار خان و باقرخان داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/84583" target="_blank">📅 09:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84582">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9Q0qEgbHgcPQhQe0M1817yJ7VJwWD7zG6lpVi31or7rJtf_0_3Io7wH7rCxmgkGDhbPwxVV8eroGeR4M3gQBSYjioxRg_OHc6l2rhBubWUwJ-EwSlkbskFoBNMc1lerJXhnVP1YfrQsKQTBdP5pQwcRW2gb0GtjbJRjWCQeTfOxO055b5Q7PGio2loUpwyzWdZ4kAO_j5GOY9jaGOcoaKyXDJ-ZAfD2Viy6xEBnYcIuG4E4P_EIs-8vfy4UfAq5Eqq31memx2ceMAblPdGfQUf2GWvLHAq1JKUb70LXb8lt4_i7GgTi-Dmz8tK4yCvfoPCA8qFWpUGAN17yTtIxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاوه گویی رسانه‌ی جعلی آکسیوس:
مقامات جنایتکار پنتاگون به سنت‌کام دستور دادن تا آماده بشن برای حمله‌ی مجدد به خاک مقدس جمهوری اسلامی ایران قبل از انتخابات میان‌دوره‌ای آمریکا.
همچنین دو مقام اسرائیلی گفتند که احتمال حمله‌ی پیش‌دستانه‌ی سپاه بسیار بالاست، زیرا آنها دوبار دچار غافلگیری شده‌اند و دوست ندارند این غافلگیر شدن برای بار سوم هم اتفاق بیافتد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84582" target="_blank">📅 03:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84581">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید  Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84581" target="_blank">📅 01:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84580">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84580" target="_blank">📅 00:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84579">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوستان زیاد دنبال موضوع فعالیت این چنل نباشید، هرچیزی جالب باشه یا حتی جالب نباشه رو میزاریم ما
هدف ما راحتی شماست که مجبور نباشید چندتا چنل جوین باشید</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84579" target="_blank">📅 00:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84578">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رسما جنگ زمینیه
افراد مسلح ناشناس با شلیک راکت آرپی‌جی و تیراندازی با سلاح‌های سبک و نیمه‌سنگین، مقر فرماندهی انتظامی جالق در شهرستان گلشن را هدف قرار دادند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/84578" target="_blank">📅 00:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84576">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=Fbkx5Bb6YG7AwchDlY0K-Gkewyicn0vjkuK2OhmhRHj1fuL_49Gtz5beK3YJq4IbAGLLgzXF7rKtm2GRk-mdoVEIjYUgFI6359RxRTQpt0sFw9bbhJcycqf6eeZyxW7VHgOxEqLw0ZWxED6OjymvjR9LFO2GUEKc-836GPOM3sna3o78HeZIR7zbZdKThiEwBph5k0SQc_db60Rge6Z0o8VQs7RePrxusgY9-lLCBLeYv_0DmZboHO303i90Ydz4ZnmLSDWW-MRP_SPKp0z89xQpDN4t83wZUHErnOTOqsKgYwVOQB0ICB0pfI_jQoiZ_gPQVuwGEwvmOQHx6bEYvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=Fbkx5Bb6YG7AwchDlY0K-Gkewyicn0vjkuK2OhmhRHj1fuL_49Gtz5beK3YJq4IbAGLLgzXF7rKtm2GRk-mdoVEIjYUgFI6359RxRTQpt0sFw9bbhJcycqf6eeZyxW7VHgOxEqLw0ZWxED6OjymvjR9LFO2GUEKc-836GPOM3sna3o78HeZIR7zbZdKThiEwBph5k0SQc_db60Rge6Z0o8VQs7RePrxusgY9-lLCBLeYv_0DmZboHO303i90Ydz4ZnmLSDWW-MRP_SPKp0z89xQpDN4t83wZUHErnOTOqsKgYwVOQB0ICB0pfI_jQoiZ_gPQVuwGEwvmOQHx6bEYvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی قیاسی رو با تیر متوقف کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84576" target="_blank">📅 23:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84574">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EIGc2gT-DxQHM-zxUc29XX5wCECzpSPCzC_kbvRNl_y62VBYCEopR6dCUw9f8qD4k93d8G16H32sqUW9StOSORzqxs4tT1IEfzUxUszDx6f0ApI6hxbnnaA-WFSLqO1RrSqQ9KvtvIAR5XmAnrTw_RXj5Jq-QyRdJCnecRKzsnvzZETKAqiArCf-nes3eXC836GThkehjmttgEUuFckXdm_RDw4oqK5AEVo7n4Hn5mPW8HwrT2qzr2P7foNKzEMYoCieASzx4HtI0dkVbssNt-ccDtM0S4K2BdX5-EEIrKj9Hna0AJaYpi-iywjAR-_EhQYwu9Cva-BPSbUsY2naRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhJTzJe3aT6X5waet4ffGmiQpvzvely8KWQfbnScUWjPpdgKkW8qZ3w3IftkKJqJt_lNDpq5n2fEcarkx1S5kJvGkz3cYunwOJfN1SZfKm28eZATBjjrIEtTeYv6_g1s7pIvEypOLwohCwC0vNUMHENew3JyRcc89GvulnntrGRDDVfSfxgP_uiBWhXXV2rS4P08Pvbue-9xJ8T4p9s9ro2ZcyapDm7tXL4Fpr8lEvjo6quDyQdH_NV5NtW1XpS2IyB8wJT_6Gih5zZVH7oquj8nIh4qf_eGIVOhl8UiO8FIWdrIKoP-lk1HQSCgIMZvRjP8qEWmrxVRXMyJ0YoToA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاگان و ادرویت دوباره افتادن به جون هم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84574" target="_blank">📅 23:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84573">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐒𝐡𝐚𝐲𝐚𝐧</strong></div>
<div class="tg-text">بلندگو هاشون خوب نبوده</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84573" target="_blank">📅 23:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84572">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=CSmzH4g2aYp-QNVj7uo8k1Ptoz3j9yO32Ap7pZ2E14OEuRVkfhkuXiWU7Cad2NYvh0E7SLrpqsqX9-7247MU5S91paVZSfWmDMLG8gkjsHBSnm-4ZNUMarwv5hjX3YIGjmgrkS6QOkmeJpOI_hxHAnsmmjbMnqrPBKaqXuHMnj6GWuaIqezF29VnvymNhbIth-P1tstvAKdUQP6mBYVZcRux4nlb08_UzAVaSbtYwarLKgQrHrQo2XA7AU8sAK9SHisvRUBfs47KAlHk3Xcz9x8h1dNqMLB6q8uyxwDd7O3hbdcZgiTl3NgFDo7dMXnkt5uHHzc8hqo4pyBKWdzv6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=CSmzH4g2aYp-QNVj7uo8k1Ptoz3j9yO32Ap7pZ2E14OEuRVkfhkuXiWU7Cad2NYvh0E7SLrpqsqX9-7247MU5S91paVZSfWmDMLG8gkjsHBSnm-4ZNUMarwv5hjX3YIGjmgrkS6QOkmeJpOI_hxHAnsmmjbMnqrPBKaqXuHMnj6GWuaIqezF29VnvymNhbIth-P1tstvAKdUQP6mBYVZcRux4nlb08_UzAVaSbtYwarLKgQrHrQo2XA7AU8sAK9SHisvRUBfs47KAlHk3Xcz9x8h1dNqMLB6q8uyxwDd7O3hbdcZgiTl3NgFDo7dMXnkt5uHHzc8hqo4pyBKWdzv6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میا خانوم انگار تو کنسرتش خراب کاری کرده و خوب نخونده، ولی خب به کسی مربوط نیست ایشون هرکاری کنه درسته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84572" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84571">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a289765.mp4?token=jXKYTmATz_epxssJvgl9gYclzLXye9TDORLBKanqM5X7A6RNLVRcRgRgxXpBKFTTIf8WfuU89qnJBsvl7bNa7R13dNGeLgk-MRYNRCkT7II7kUYyH93Pqvli7WId4qDe0Th0NMirrsPGCyDZ80kACLphROsdY588JWsq2SYee5QSIDawX6iT3anQDCeGHaRn0DNiTUxL0Ixt2RsU_vi5xM0jBK5okDVir55j-eJzCwTkeDZ7kHMPgG3QyUprw4a9bw3iGONczrFQjzpLH1dFUhdESxr69mSphxl9hYVB1KUkDp66-gjBNxkZa3ndCm9lZbUdoEdR829DR1aHTPEcog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a289765.mp4?token=jXKYTmATz_epxssJvgl9gYclzLXye9TDORLBKanqM5X7A6RNLVRcRgRgxXpBKFTTIf8WfuU89qnJBsvl7bNa7R13dNGeLgk-MRYNRCkT7II7kUYyH93Pqvli7WId4qDe0Th0NMirrsPGCyDZ80kACLphROsdY588JWsq2SYee5QSIDawX6iT3anQDCeGHaRn0DNiTUxL0Ixt2RsU_vi5xM0jBK5okDVir55j-eJzCwTkeDZ7kHMPgG3QyUprw4a9bw3iGONczrFQjzpLH1dFUhdESxr69mSphxl9hYVB1KUkDp66-gjBNxkZa3ndCm9lZbUdoEdR829DR1aHTPEcog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلوت کنید آقای سامان ویلسونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84571" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84568">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F61QuHr0GMYF9fohulBoqkJ7jJypWeWvr0Sswg8ivi4Pqu011VaUqhUD2L7XHOQaoKNXwIJ5BTLIqo3h495hJBSwCI4Lm2jSPYVdd101LMRCCxVCmNbtecOX-ugB4yx12BoHp-j9JSXr9wjXPoFHeUKqajDM2mKYQFm53tTVOG-JKp9XOGOSQsRJe80nMVIfpOlK9MdShRTbeDEdOGClRAjnGaXo1_ZZydsmgn38iotAKO6aMnoaU9TMrTdsOOlaqlGI5YQR0vHFHxE7GP_lyP63mAb7dY6FShv45de5UJiYJ_FkS5iHwdd_uGknS-b1FEPUuRSrlBe10dACae9r7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی: لئو، سال‌های زیادی از کشورت دفاع کردی و تاریخی ساختی که برای همیشه ماندگار خواهد بود. بابت تمام چیزهایی که با آرژانتین به دست آوردی، نهایت احترام رو برات قائلم. یه بغل گرم...
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84568" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84567">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کیانا عظیمیان خودش یکی حرومزاده تر از مهدیاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84567" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84566">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaulTSoPJBdBqIh9-M7Z6sy15wdCfH_Pxp-R8JZGKNJaZWnNNPrHz23KiEfk7jFiIUpwXUi1luSJfTRk0a5qrEg-ZcuJ71ADPCIcuWakMetO4DPHN-16wkBSr1xGNqChQIUzYxGd1_F9TogmS59geWjEkvffp_RsfJbk27tYKmCB_D_ZcKzp1HQkhJxT_BHSEfdzz70rNnTu4YcDfQCXnCrloewqusyAxNLTGWmE0qBKrM2VIBon19EcpvulPrGDYWDrAFK6dST4PQvx7_r9Nk74tfenoZVQ7_GCBA3NPbeP8Ax52quyrx-B-HGZZXcOES-7n2wNC8r4n_aoxMcKfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری های صاحب صفحه‌ی ۱۵۰۰ تصویر خطاب به مهدیار و ملتفت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84566" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84565">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مسی کصکش جام جهانی خداحافظی کرده بودی دیگه بازی خداحافظی چی بود پولامونو بگا دادی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84565" target="_blank">📅 20:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84564">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پاییز نیومده ثابت کرد بهترین فصل ساله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84564" target="_blank">📅 20:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84561">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">HEJAB</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84561" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84561" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84560">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7iR7AvqZRhriyqRSL_zElRt9Wbz-MtpzbmYXesJku0JX_yXrSqqUOka4Q_2jHGhnlpJUJxQF_ERPMOaZd8_MJRwzpd57TZL0Nt8pZl02RY4aLxzhoNAWhB3mJF5zaV-Tb6Bhlgx73OXvkFKTb2jLNOOCiXbBxNL3qOA1qHSjWIYQYnyCRTWObJMNvyQilHIu-ndipc0WIq-qiq448HrGfMnPFbRHBeYycPbunUUnkCrZiUHoTM0Xib2ynxnxL60MKYt3AkE8vZHta4-sCaLosTNpc2UTi_CYbKKskS98CvvVFxA6Xcej9hBuAs7jBkemQWEeGeRw5uyJrKP5_qTjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84560" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84559">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=vTlqUY7-WLXd3VjgZiXtt0heTHgdPc6XT7fS1zZ6vUL83M55hf5lDY3IybqhweUSpM5cbWiAfiKRJbaGbDFlJ5WJrkCFqKIa2QDi15nWQIa27thi6qrfWS2g-Euzwto2XjU-kezfgteTbMLocw2pa3ajKOK5kqi6lHef_R_S0_QT5fC_B-YCyUab_uox1ocSrjbGGy8fdfJWW2ez1T2u-DBO0SwnohtrCSqY_nm0e5csCeyv89beGgCC9pDwKuIhT3nhxvIHcPk7IE0hPIkyFXZjIGIliBFw8xhyAAORvrF0dzOM5aTnqbjbK1Ls-UAQ2LDiib4TUUi3ZrEjSmw7fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=vTlqUY7-WLXd3VjgZiXtt0heTHgdPc6XT7fS1zZ6vUL83M55hf5lDY3IybqhweUSpM5cbWiAfiKRJbaGbDFlJ5WJrkCFqKIa2QDi15nWQIa27thi6qrfWS2g-Euzwto2XjU-kezfgteTbMLocw2pa3ajKOK5kqi6lHef_R_S0_QT5fC_B-YCyUab_uox1ocSrjbGGy8fdfJWW2ez1T2u-DBO0SwnohtrCSqY_nm0e5csCeyv89beGgCC9pDwKuIhT3nhxvIHcPk7IE0hPIkyFXZjIGIliBFw8xhyAAORvrF0dzOM5aTnqbjbK1Ls-UAQ2LDiib4TUUi3ZrEjSmw7fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دسسخوش با ۵ تا سرعت پراید چپ شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84559" target="_blank">📅 19:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84558">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qI_5wfay_rbwSqFuJUf-UM77p33fdszUyTntqhhvLLzDKq88DHOu0LLnscmHQ4_4UsYWXQ1KcEvdWdKDDnEDVqjM6Gc1ew39yDJzcakE-mVXNWr59VGYPsBxkSsFnWBzMPjGCxWRsySCs-BPRToe5cnnZmdR3EY3OukR6guGaPQnwzUiJ4NmFsTNsS40gWpoWkFQjzcKJjHMM7Z2qQTj7cUWbu9IOA7QBHyF2aHi5z7DwSbL9uxO-WfisYIfPJO7LGgZFvXCR3mlifDEmctAqMnCd_G5O5UhcH0XAb6YHBuSr0n3rUseZWn8044442Ptf5foWlKQ3-RKIqNqFW7O7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر این کامنت ادمین دومینو بسیجیا دارن دهن شرکت دومینو رو‌ میگان و هر روز جلوش تجمع میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84558" target="_blank">📅 19:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84557">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yhxp2_-PKnujYColhl551CJBiHD2EcCP5FM1LOneRMUj1TqoIzcg5YF_ygJOhfWIZYQ_OgmR0EkVA6iB7W9waouevixZMYVOZniWBxxOmfr-Fhq1G2fOCCa2NVAoX7UQl3dzszGcqbzg30Arg05O5Nz3odXnQqsjBY5GDqpxTcGtwib87KYhumSTh2eNywHXWRM5DO54ewEhgSSUM5dEc7cSAKLtbHxBl1Bv3H6Rfx16m_cITc-JUSZZcWrnGHZDEjyLo8SQblsmUe4nkM0GLlH72G6HNrliBntbdc_4lEqMkdGW8U5_c-TkgGMrBLCIsNUNG4BJa6MUd25cxqs26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیم‌کارت با قابلیت درآمد زایی؟ اونم تو؟ بیا برو مادرج
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84557" target="_blank">📅 18:00 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
