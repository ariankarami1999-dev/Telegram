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
<img src="https://cdn5.telesco.pe/file/UFXmewFz6qrOO05Si9vO9AO3mISN0q_I0dmegawcwKTzy9aAvSWmv5q3vjGfA_LLgIC2zWexCbKYs5FuPSTigErLQMe8oRqSulMXqJ_elp58EN-cPU5syjIh2zre6QfLWAwcBSQdyWHddcsOIGJcekg4YKT_LWaWSOGRW87HbuLJJLLUJIKft0Yq0n7uhl0UNIMhcvbvJt2YSYXXFzlWq7lzP_XcChLJfE6ZYz81Eq0la7TI2-0_OLH9r5QPtAoss23lJ2zKyA14MhqnxOD77R1zHi4wNROZ5ATH1Qw583JRGwYZz0-HnBxg5sShLqwg7JWNh_fUJLFyj20wh3jj5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 660K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 13:10:54</div>
<hr>

<div class="tg-post" id="msg-97615">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjdUZEE24Nod2R8H3pI1GDE38MadHzn31SL5uhXarwmq02ZgKPR9Reb5_NdFu5Wg1WFs_Le8v3r0BHY2lYjOLyz9eTyRDIsYEKq4Jf-_bcG1hm5ADMGU1dKQqSGP6JmuHXd8LGYxCZAoknx13OYdAM410JJFJdCx1DZQc3nDfuvbgW1XT3Hlq0hvHoSlpky3dHdWZ4UzA0XU_SSahM8lrpM_2_W0NpdNTMXKl2EHyrBdkF_yQsJA3wUT5F8e-q8xgA4adjijqT3waNFCPgUQZsqD5J1OenWBD4TPeKsOKXX_WtkSrzBoPrPy97VCTgL3DhsXMhz4OmuSEtoX4RTusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
از حواشی بازی مکزیک و اکوادور
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/97615" target="_blank">📅 13:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97614">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6oLOy9QlxQPwhyUOOIikkdfVlKSexav1BgRp8442eykpqq_mRxhkYiW3XkG-hF-T6sIUZ8hx7aNPyRu7PZmxa0UTUn31rAWeSTCdVm0wICDY3zv0uUEgpLOCn4_dM5SgZHZcJ9nrJ2Pr8cLJBTZoNujST6Kd7oDVL61wbOT1txCv7Oerm4OsZfZFJpepAjwlI6xirRxbWE-wOO76XOStFYtRdFkD3fzTD8T1pN27-3XABawnYULtD_TBe8Nwb9zT8TrAjbXBXBVV8eVB0xuYV0jQ6y694fKeaRHyql20gtrNi-pCvs0B85MNbvdCeHn25k6mVs6XQ7cb43-uuXK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فرناندز تو تاتنهام شماره 18 رو میپوشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/97614" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97613">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204ff9d4a4.mp4?token=Ap31tCk2btudSWKfC7Z9JsW0lZpE49nRDX8ApGPnDd4JihdR4JH-iG43Jt6UfN3NFhKKYDrhZWzgavqQ3Sbw7IhrjgLM_jX4ZAHgUFuLJP2PThs9Mhudo0TmkppaeiDbVSsL3LNOmCFCB6UTtK-EsIlKiadyCTvDd4uymodeWHv7x8Ezbw1w_WBGByLZ-3fILhCRmugA9AHSCMX9v6NHegkigGffg5yj0NIVHeRw54mVURWxd7nuVPNOsJJ8SPbJwxJeS70cCsgUyXuv1DmfKQ9JSkLrCAoSzLKzBsGPMLTVGyAw1AN1saXQBGN3I-kyKS256Q1GQjYG_nNICXy9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204ff9d4a4.mp4?token=Ap31tCk2btudSWKfC7Z9JsW0lZpE49nRDX8ApGPnDd4JihdR4JH-iG43Jt6UfN3NFhKKYDrhZWzgavqQ3Sbw7IhrjgLM_jX4ZAHgUFuLJP2PThs9Mhudo0TmkppaeiDbVSsL3LNOmCFCB6UTtK-EsIlKiadyCTvDd4uymodeWHv7x8Ezbw1w_WBGByLZ-3fILhCRmugA9AHSCMX9v6NHegkigGffg5yj0NIVHeRw54mVURWxd7nuVPNOsJJ8SPbJwxJeS70cCsgUyXuv1DmfKQ9JSkLrCAoSzLKzBsGPMLTVGyAw1AN1saXQBGN3I-kyKS256Q1GQjYG_nNICXy9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
خوبه کشور بنگلادش تو جام‌جهانی نیست وگرنه با این هواداراش سوژه رسانه‌ها میشدن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/97613" target="_blank">📅 12:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97612">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAM_RKzIGYyaP4zTCthA06LCZ6QykEeulplMXykw_x-7lAI0Wd3HnItprs6KYuidwwfPAZ00v0PyTdPoidj7JYa3BtMsC1UwBrnUzsNGvDYIRPUq_V717akN6WlGWHBxkM6mLvwj8Z33crhALrbHfhxh3snt_K2lX_uBh_u-1uE_unukMmIya9DIMMaO2xPyg4MD39lNE-dld8Lh1PkAMwFteck_ldbPhlPXVASKS72V6wQ7stB0nRzBMXk_EM8f77TC-mV9JANoPGJlNR7Zn5HAAFEQYQXn0oI0kBl-16veDns8ZTDiu8luIpxeqN4vup7iGPBLBYxisygDLE5Y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی؟
🔴
تریدری ولی همش استرس اینو داری ضرر کنی؟
🔴
یا کلا ترید بلد نیستی ولی میخوای سود دلاری داشته باشی؟
هوش مصنوعی TimeTrade این مشکلاتو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و به صورت live و روزانه درامد دلاری داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/97612" target="_blank">📅 12:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97611">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxhxRzSxeg_-ee65Xy3IhVuktsJFSCMe6psR7Y5Ou81dd4sf5CckOkamb5glRbn-zdYcY226Yl3NQG00EZt0Yn1J7Je8xXBm28tLQORfCSoENzbPQ8Cida929TR0ATskSia0P-2_Xie-pM3tkGYYD5gLzVFolOH2hd-YTpfOjesB-5ag6NWXq2qjohkQ2COyj8g1-Bq8rAxIrNbjt7XYvjkFRU8j2B-0Sva9KSCokXzrBvy7cXwibNwPZZB4uKtJRo2tFy_sJoLma62qz2lbL1dPMiipritDkTMlEQXRVS1MbXlRW1Odm2hZs8MN-RPiWvWwgfLJDNKiiMugs6Ct7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
#فووری فابریزیو رومانو: متئوس فرناندز به تاتنهام؛ !HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/97611" target="_blank">📅 12:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97610">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EERB2GcefyKp6FlC3uZXb1fs50wdGy5MZOm8WvCWu5Rlpp_6Gwx0sLMoh2CcBZQpKdTo2FtFkHbgu_ayOx9Pyxf0_0BK0xgokuBGr6FcPHtD4z-uqFJDcPqNBwnU_GK9eeBbeDyyfC7CN8nQHsU20EqEtzdqssLJyby8mBrCtyh_x3aVgySXGbe3UJ9S7OVbRXAz2h9A88dO81ZPmNQaDpJwtMwCrzZiYuXSs_IodEnW57VQV5m0aKnQvxEBAxPx4CJEOAhdU3tgiLsrEoklHMlFRdMya4jJjb1uCee_f0evJtlLjHngjfNbJwL33jll3q9GJswJKeMCk7l8i1y0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از باخت کنگو جلوی  انگلیس، سباستین دزابره، سرمربی تیم ملی کنگو متوجه شده که پدرش حین بازی با انگلیس فوت کرده و از دنیا رفته
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/97610" target="_blank">📅 12:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97609">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKfuEcfRK_sbemuYNxKsw6em3OHIfN4wTwlVY-UKXpUBDMDLjHLjMguXbOudzwe7HWjA-nprUNrY-BtgiEGAF7tKiumigduVVpBIBI4YhzvlEsu665ViO5X7R8vzJVRgJEk_izauiOtLJgQedUMvAzvi6ZUF4jHUIeqNH-7ROVT90OrRYeiIilbuqcBkuBpjPqGFBoCCNajmKYFZqzwDaGEsak0WThODaK7OQqs6R04oxK7i-CgLTJHo0mBC-R40TMbcz5RYAiK7e_YUIZB3sWM1iK_9AK-nVi9YkDNvwSXtKcDysewUDcakYFvCd_30zCRe1qZkBxs9pwB8Vh4qjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🔥
کار درست مثل گاوی که بین خواهرش و زیدش رفاقت به راه انداخته تا زندگیش بگا نره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/97609" target="_blank">📅 12:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97608">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbba94933c.mp4?token=B4_PDEcp5fyBuE4dTDIBiSB3aDllJxPoYRjIyYNtELNUAptrnq7clsc8gdnk60v8gKNlVGiHC0rVEJjKb-zJaHH_oHEc910LBBs8tJcjZv3SXA-rap4QOjhgGapd-USWHCjmlSEwgbcoj-3iOb-_ceQ3Nsmp63d2jY-4KbN5TfngxHClXp3dgpn4YgM_SbeXg_9LOcOrjcd4jNai4STENYW4o3d81dk3n0cgE9QixHf_fnprJOfQcaF4QDCNZBCMXNPlCaUcQnC57PTzMalBoHRUVMh0cG2GwHuZzL7MEkdGnu0fwDF2BkS3knvA3JZ6yNoxhEbLnP2MsMjQcAaQPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbba94933c.mp4?token=B4_PDEcp5fyBuE4dTDIBiSB3aDllJxPoYRjIyYNtELNUAptrnq7clsc8gdnk60v8gKNlVGiHC0rVEJjKb-zJaHH_oHEc910LBBs8tJcjZv3SXA-rap4QOjhgGapd-USWHCjmlSEwgbcoj-3iOb-_ceQ3Nsmp63d2jY-4KbN5TfngxHClXp3dgpn4YgM_SbeXg_9LOcOrjcd4jNai4STENYW4o3d81dk3n0cgE9QixHf_fnprJOfQcaF4QDCNZBCMXNPlCaUcQnC57PTzMalBoHRUVMh0cG2GwHuZzL7MEkdGnu0fwDF2BkS3knvA3JZ6yNoxhEbLnP2MsMjQcAaQPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✈️
🇺🇸
پرواز جنگنده‌های آمریکایی بر فراز استادیوم دیدار دیشب این‌کشور با بوسنی و هرزگوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/97608" target="_blank">📅 11:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97607">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/97607" target="_blank">📅 11:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97606">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ac3b752e.mp4?token=vgW5PF5V-ch9YaVAl8ZsV7YgGV5cGbgULlcMeOJdAPkPTUDiXIE1m-6TZuG7KEjJ-x2ciVAIKfY5eujHE4CtZ_jCuUc8jveK34jl6wkYQWrIS5MPwsDjBnbuHvn8Ypu9rTwnvQCOX6L-BESfMRAJvs2aX3QX3L0NSyCP6X0pHf9dYZp6E3NUHW4wU9NubKOPDuOBGPjpiztOuOERsKy2YXWJaJPbweTEeBYvfPo7J1fYSAok8oJmOkuMAqmJh280sbRrOB7W_zKhOMvoP_62ZUCE8Er8l5WHWB7o1GZRVI9nJ8f_3IzvRss-lzeno4GALyMZ-cME3ptVM6ZCdPwtFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ac3b752e.mp4?token=vgW5PF5V-ch9YaVAl8ZsV7YgGV5cGbgULlcMeOJdAPkPTUDiXIE1m-6TZuG7KEjJ-x2ciVAIKfY5eujHE4CtZ_jCuUc8jveK34jl6wkYQWrIS5MPwsDjBnbuHvn8Ypu9rTwnvQCOX6L-BESfMRAJvs2aX3QX3L0NSyCP6X0pHf9dYZp6E3NUHW4wU9NubKOPDuOBGPjpiztOuOERsKy2YXWJaJPbweTEeBYvfPo7J1fYSAok8oJmOkuMAqmJh280sbRrOB7W_zKhOMvoP_62ZUCE8Er8l5WHWB7o1GZRVI9nJ8f_3IzvRss-lzeno4GALyMZ-cME3ptVM6ZCdPwtFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
ژاپن، غیرآسیایی‌ترین تیم آسیا...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/97606" target="_blank">📅 11:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97605">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inUskAadUWU2F63VQaod6tIYwET8KnQvxg3v0ynHYfnIWTvPPM_lfSnsWzqQa8joTXfBS7RKK_dvBTZNbgTyZriVbIfLlp6XcGl1PCupUT4rvJmAq_sYja4_pVpd-WviL317_n-nQxtZhn9RFN4gZPfrTGxGcBVXrIuexJlqEiNBsH4XESpJMfKs6ZvH92_hso2HG25bTX_x1MKmUHNcnBan8b-xX2FFBcpONlUbAH7fC46CW13L0DdSUjx5NpdFm8QtZM9A0-HEGbWmN3LzJS2U55PhPXEHNDkD4PjdV494rZ3opLkqnpJcepNiuOK4raUkYU_nf8hiYvGe-nJdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری - فابریتزیو رومانو
📰
|
🇮🇹
— هیچ تماس، مذاکره یا پیشنهاد رسمی بین رئال مادرید و اینتر میلان درباره انتقال باستونی وجود ندارد.
❌
🤩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/97605" target="_blank">📅 11:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97604">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea402ec7ef.mp4?token=mGgE_vFifFYhMUif7WRV5i5_z2aJhDZW_qb8b6RZVnGKWF5mphRSBIq47IhBWAafrMud-FcGLq7_xNj8bNS8QT-sdDNq8FmGoKmJF4o2RGPAw2MfBAqImt9HI_meVoc7CV3KbXYfXsUi26VautPsdKrhoTTIrEG1Cvif6w3pzaxxRVBgU29LRW2sp2TVXEoxX-LjUEkPf1m-PDjzQcg-sugtdR9sBkGstcz4Ti4zd2eDFr9HLgWJFHBy6TWgwWJhoJAw-MiazmihTNgQYHk6EdkR3KZTNYNeF4tbkiJGB3MWvQ5uC29GsVZKEoHect5BMX-RNldZNkScO4cUvPrFEkYLkVKDKsQ4_aYDTkOoKeh37hieVdBAAoDZEjcwygqZLBszife9CUp3KRnhr6G6NKn_Ras5bdkz3nW1Cs6aOuCDqU3QHFDF47VK8DVqh6PdLP5plXb3hX7f8a2gpLA7g_ouz3MI8ik8pecborjoWNtOhBQ1S-rFOd05B4en7Bt5bMhp4UycTNYjc4nSyxZmokidukAl1n8M4M6pi15GDStwNg9iOC3rH1ygtxHafvvZHY0HGhZgVkL295dxWcgW8FgoiAPJqGD6pjJ3FzBpFx4LwAoSRdALRQyrTHbygqDxwsNg-HcXJW5czEDqIytOjV1vuG87ZIOy-Ry4luPzv74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea402ec7ef.mp4?token=mGgE_vFifFYhMUif7WRV5i5_z2aJhDZW_qb8b6RZVnGKWF5mphRSBIq47IhBWAafrMud-FcGLq7_xNj8bNS8QT-sdDNq8FmGoKmJF4o2RGPAw2MfBAqImt9HI_meVoc7CV3KbXYfXsUi26VautPsdKrhoTTIrEG1Cvif6w3pzaxxRVBgU29LRW2sp2TVXEoxX-LjUEkPf1m-PDjzQcg-sugtdR9sBkGstcz4Ti4zd2eDFr9HLgWJFHBy6TWgwWJhoJAw-MiazmihTNgQYHk6EdkR3KZTNYNeF4tbkiJGB3MWvQ5uC29GsVZKEoHect5BMX-RNldZNkScO4cUvPrFEkYLkVKDKsQ4_aYDTkOoKeh37hieVdBAAoDZEjcwygqZLBszife9CUp3KRnhr6G6NKn_Ras5bdkz3nW1Cs6aOuCDqU3QHFDF47VK8DVqh6PdLP5plXb3hX7f8a2gpLA7g_ouz3MI8ik8pecborjoWNtOhBQ1S-rFOd05B4en7Bt5bMhp4UycTNYjc4nSyxZmokidukAl1n8M4M6pi15GDStwNg9iOC3rH1ygtxHafvvZHY0HGhZgVkL295dxWcgW8FgoiAPJqGD6pjJ3FzBpFx4LwAoSRdALRQyrTHbygqDxwsNg-HcXJW5czEDqIytOjV1vuG87ZIOy-Ry4luPzv74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
آموزش رقص‌ توسط ایرانی‌ها به هواداران مصری قبل از بازی این‌تیم با استرالیا در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/97604" target="_blank">📅 11:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97603">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlbi8uLGO4M-G-NRkAxtITofN1qUPZ38vIx_gDaNeKgFL80uteW4nv_nN1sh-Iryn3qtoSVpGO3AaD-dzJzGoDuvGzojWSkFDW3hQDEDbWDOPh_Ho2HnM2Jj58H0yC1KeFeXfCMO0lGiludjQ0S5NmbEv-VHZIfoYOKUukUOZjvsk1bmuOo5jUxy2utveA8K-rlssiiERpxdqG__zxPS9SKSzMcVqWCRiDCD1e82H4vRPfc5BGJY4JjFkOj3iLzqZDOxQD2hldBFH5OcSRPyCPl_JeTgYL2HE78y3Z6fN13LrxbYOKHV0XkrLf719wml5UIyFz3wlQ61MSFgn5bHZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
#فووووری
از آاس:
🇪🇸
سران رئال‌مادرید پس از نمایش درخشان اولیسه مقابل سوئد تصمیم گرفته‌اند که برای این بازیکن تا سقف ۲۵۰ میلیون یورو نیز هزینه کنند و رکورد تاریخ نقل‌وانتقالات فوتبال را عوض کنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/97603" target="_blank">📅 11:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97602">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed83a057c.mp4?token=WbktLwXf0kDZrrlPhViXIjgo1CS7WPffLwJF0C6UQGM6Cra2MNoUQ611a23i1JnUu4p0QvMqAGtywWKDRazeKH65slKRaNniSn0qu23_wckS8d0zNJX3FplK-Hayv9qTTM2_l6QTRAKEMrGh3P4Qx7CTPiM-DC20UrjrzSpR-6RtLT_t2n3xVuPA_VIGdnlMzpVKB3et2f586Aa9eTqIWCewGjp5AvURxsElVFnQ5SvnXElTFmMoSdDUSVH9GRqR6LkPLssXnpBc415ERvpt--Y3LslDb1JNcGQFOjBWA0nTP1u6_tFcL_EjLkfXdNoAvcjQjsDwHD0nL2w3cdQTbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed83a057c.mp4?token=WbktLwXf0kDZrrlPhViXIjgo1CS7WPffLwJF0C6UQGM6Cra2MNoUQ611a23i1JnUu4p0QvMqAGtywWKDRazeKH65slKRaNniSn0qu23_wckS8d0zNJX3FplK-Hayv9qTTM2_l6QTRAKEMrGh3P4Qx7CTPiM-DC20UrjrzSpR-6RtLT_t2n3xVuPA_VIGdnlMzpVKB3et2f586Aa9eTqIWCewGjp5AvURxsElVFnQ5SvnXElTFmMoSdDUSVH9GRqR6LkPLssXnpBc415ERvpt--Y3LslDb1JNcGQFOjBWA0nTP1u6_tFcL_EjLkfXdNoAvcjQjsDwHD0nL2w3cdQTbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇧🇷
🇳🇴
اینبار تقابل دیدنی گابریل و هالند در سطح ملی و بازی حساس برزیل
🆚
نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/97602" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97601">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">لحظه ورود تیم ملی آرژانتین به میامی
تفتیش بدنی مسی و در ادامه خنده هاش
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/97601" target="_blank">📅 11:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97600">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
رومانو: فلورنتینو پرز برای تکمیل معامله اولیسه دست به هرکاری خواهد زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97600" target="_blank">📅 10:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97599">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-ENb7dqBRbeXgIeR9ryCKzNzMoTKFsXp7xGs7zh-oXBzzkKotH7ajI95K9MfTYIu9CXcGKlSnfK-O37c40bg8HCdQhi15BAe_ojws3VGezUqSY0fXUI2LB95088SnfdKOO8t3CRe41NrK-YuQRKNyeGNnZmAZT2mCV2CxHcxzO921QS-esb_JoXQGr-MFIc5kP0kvWMh0wFckuOlQUcvgL20vdEj_yLkMPeq9UbOc7ykPlSJeVUuwBXaSytAOVwU7TG2VEBu0wTkaVtdTQtxxQKASy2naPehAk3TG-mnG6rLb-SXsky8P3GpZb-fVDUddNt4zEqnWBTLmyGZrOaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⁉️
🔥
#فووووری خوزه فلیکس دیاز: رئال‌ مادرید و یک تیم دیگر با نمایندگان مایکل اولیسه درحال مذاکره هستند. کهکشانی‌ها با توافق نزدیک‌ترند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97599" target="_blank">📅 10:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97598">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjoUyVCSskct-WGhgiIbkeqDIlbZTDynXugRC--pkWy2U-sEZ8KFfKNPFLUulxUCeHTBFLtgg69rVDH8JreoUAVPMUUS_Fg1Bn7D8MQwmDksoBZX9krbPRnHQfC16yw5q0yuLqXfYbn-ZOyvKmgWK9N9Wwa9-DQID-JUFiik0Alv_xM-UPnGFI_Hxxlmmc4ItR382n6FX8YLxlImTIlCcSNov8THDm7ygw2KnsDAmFFldjgnz6Oz0jSqliAw7zOf70SbZ2hNkbgpxGc7d-KTfteTdRG1uj64G_GqJsyZKaMIFliRwYsftdXHRtiZzbgovg641SV3KC2wXzQVxw7jyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⁉️
🔥
#فووووری
خوزه فلیکس دیاز: رئال‌ مادرید و یک تیم دیگر با نمایندگان مایکل اولیسه درحال مذاکره هستند. کهکشانی‌ها با توافق نزدیک‌ترند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97598" target="_blank">📅 10:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97597">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6s3lHRyXc18kprgLT1TwLuo7BWFWSIVpqLhG8kQ9RrTRLdil2xBbHhhkXGqmCCalfCiKI50LrMw2Te9SLBycavZeLKzchyhyV87p-X8uNGCarFM2JjCgtoCHfBqmU7ilClbUn-bGm1zZTrNiCd5Uj03sfLLwWJqxJb75R2D7vSdk1XpZpUnaAv108lcG2IXuNubH7PIx6wmdO52T2i5kqCdPpEjDZnKYCPUJa5OgSnAykuhDUWSx5Q4m7eM49fwQRjbLTrkusVp2XPBMNx1hgvaCTpyEodsLwjF0o93wZCN88ro6RpqC5csAKXBInMCPlYrd4fY6wQlP_1jLHJO7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری؛ ساندرو تونالی با رد پیشنهاد هنگفت منچسترسیتی در آستانه عقد قرارداد با تاتنهام قرار دارد و بزودی رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97597" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97596">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aec355d42.mp4?token=dQL23vUMOY4Qru98CiGis6oSPFhMKxX4TYPPiTDIV3Wbh11hrY4MtHNTm7s5lYRX0gfKoesyT8Iom2gf1LajjJmgI_rgTJ9qAvnKA25mEoy1x0pn3HivpJDFZpPvTjt6kqudu8FslelzvkkjDGayciAt5a_StnnpYBeRiNwi3VfqD5PU2mVZfjX7QYsZiPwkTysU7JVVT_htEKLg3WSiJUZI3Uk4GyPwbR-2aQzDxBzx-2dVSe95cuDG7WQxqgb_VjtBoGTTOSUfzdyruIcoSMhC75_lD6Bw26yMFomDLfmqkqS8QQI7K6HXCttd_-1pN8bLG5GrIIZuo4DY5R__6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aec355d42.mp4?token=dQL23vUMOY4Qru98CiGis6oSPFhMKxX4TYPPiTDIV3Wbh11hrY4MtHNTm7s5lYRX0gfKoesyT8Iom2gf1LajjJmgI_rgTJ9qAvnKA25mEoy1x0pn3HivpJDFZpPvTjt6kqudu8FslelzvkkjDGayciAt5a_StnnpYBeRiNwi3VfqD5PU2mVZfjX7QYsZiPwkTysU7JVVT_htEKLg3WSiJUZI3Uk4GyPwbR-2aQzDxBzx-2dVSe95cuDG7WQxqgb_VjtBoGTTOSUfzdyruIcoSMhC75_lD6Bw26yMFomDLfmqkqS8QQI7K6HXCttd_-1pN8bLG5GrIIZuo4DY5R__6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
یه زوج روسی معروف که صخره نورد هستن، بدون داشتن تجهیزات ایمنی و در سکوت کامل دیروز به بالای برج Empire state رفتن و یه پرچم با شعار "وقتی قدرت عشق بر عشق به قدرت غلبه کند، دنیا صلح را می‌شناسد" به اهتزار در آوردن. پلیس آمریکا هم با هزارتا مشکل این زوج رو به پایین آورده و بازداشت کرده. حین انجام این کار، تو بالای برج پسر از دختر خواستگاری میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97596" target="_blank">📅 10:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97595">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a9e27c8f.mp4?token=inNjgZGIbm_IsOMPWlRWgy4PyCcY6cd7CVEX-7KLpg4XcbymiYI3WAEPUn0A8qbxQhoFrOthFuFILyH8y6tYstHuXICc9khdU1DC1byEeKq3mGMePzVtOo_DWoBB5-DzpGBVIGYisZxxpHaMexltswqoHx-LHlz2fbVCjWOLS5UAiRhHg3CdoNkCKZim1H54a3A54sr-T-GzpUAWO-roz6PK9yDg0kBLwtxS4Z9l8LvC920eZ9fHVWd9sSthovQtlchs_HdbESET9bxNMTTRZjqxfrp4DePkp3kKWM88PJh0j1fHwJnD6dqtWwwg3Pqq4w35OA_st6fyzOIQxYkGew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a9e27c8f.mp4?token=inNjgZGIbm_IsOMPWlRWgy4PyCcY6cd7CVEX-7KLpg4XcbymiYI3WAEPUn0A8qbxQhoFrOthFuFILyH8y6tYstHuXICc9khdU1DC1byEeKq3mGMePzVtOo_DWoBB5-DzpGBVIGYisZxxpHaMexltswqoHx-LHlz2fbVCjWOLS5UAiRhHg3CdoNkCKZim1H54a3A54sr-T-GzpUAWO-roz6PK9yDg0kBLwtxS4Z9l8LvC920eZ9fHVWd9sSthovQtlchs_HdbESET9bxNMTTRZjqxfrp4DePkp3kKWM88PJh0j1fHwJnD6dqtWwwg3Pqq4w35OA_st6fyzOIQxYkGew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
اگه قرار بود با مربی ایرانی بریم جام‌جهانی بنظر این قاب برای عموم مردم دیدنی‌تر بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97595" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97594">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97594" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97592">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpAQRu7wIHdTlcIrL0EApDDu46WnBsp3y-dfghUxUdiZfGSqbjJhjhCjZMkvFbFT9EVHhmB1tBYZKV38pnVkKXklAtNNDaakI5l6Sg4FnTL2_x_1T49CRtgAfaoAYoMUdTw_CQasIOAbuxod7CKtjcg2O_BjZlz9HQdSWCpXCRHyPI58f4azwodLk-LbTmwMAuzGiG-wnUWE_sEttsrnVhP5zNwTd32lmcZxP_BJ0SrXWbOiXmiVZAaqWvMs5jXSfstBovKj08wjXdfGjL6LN3lcxJKm7O28EvXZ55PSetGYkOT67teBK-x2lFiJKaBgxOLpL9WADG-aw6Vv4sCz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
فلورنتینو پرز حسابی عاشق بازی مایکل اولیسه است و رئال مادرید هنوز هم دست از فکر کردن به جذبش برنداشته. توی باشگاه، خیلی‌ها اولیسه رو «خرید رؤیایی» می‌دونن. با این حال، فعلا بایرن مونیخ اصرار داره که نگهش داره و قراردادش رو تمدید کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97592" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97589">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQzQ8lK9rEs2lyQJmG3igN8gOuIV1hEpWu3p6ctQEv-gRnRFH3GRRDB1E_O7cxX6iELCpoyD5onLusaS7mxgPiq9eeUduA_Kg9Hd2gceQTb8n7qX1lBsNBQRj_VO1irrIBTmbzgyuoCqz15swxaQjwG7WKJoMSIH2JRmDUbYWg9o0ph03hfoUZFKqEw72DpcUJv9_BvbXGH6jlEVtzcdX9E3WInK0rP9FLJa2incD2_610e6S3OD_XwqNyj3MWdfY3nyr6nhAXjh2xl1T1moknzg-2nWK90hehaTpnC25OlOVfRvLE1h5nSqKao4VTyppP_X29nwbSEANyn5dTaXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRgkBVFYiBlm_tlYknGRMzJXdl8ws_OM9_HPHy0o3Hl273yVAL2S3MwSLpBGpPq5u2XvA2iKwofd6vo99wez8bOVMj8svCZgPgz0dsSo6zEFJ8_T6ljp7_UMlp07C7NzzNZ5yGhznkKf3LJ7fIJzQeR2rOkqjX7AUb6UIPJ0s-XMcUlxlwd2nulTfEAsxDeHqnNt5ieT6_Xiw_9sd3HPxhiq8vN5HEtGlXw1uIIgz5fB-WZIh6v9LviWJnRE6XCcRKv8FH-caLOA7pPBcG0X7wLusJdKa7Ec3MOZW7Rycoh3SvropVq7CuZCtKkf54ovs17LJyiXpaMtKTQced2WMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szjbpVELhqTUHgDyl9aQ_JEmqm3h1-VNG1RocZVyEQyL82ncYEuKQPYMuTmY0NuyDBsuCq-7tyeS8YNUoMkQcam1NMfC9bAgEqWeXdgRZYR69uwD6xxnYd5LFMXB-p6tRQLB8oolnZMej4yQV74yMsmItq3-DAUo2ERL2dIMYEcwoh8icD3UYux0Y1Lsu_V8DIbrHEvYYcoqdYknWp69nM_rlCrwNTyYVUjRuOsVsQgH8XUUy_klgDIXGnmYpg3IjQc1ZxCVnxnbxoaz31HGZBzX4q6DeMm5a6xJ9eet41voHRgC4_oPg_5zNZ_68IUgVGLpgUaoTgin_IrOvJxdKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تفریحات تابستونی خانم آلیشا لمن ستاره تیم‌ملی بانوان فوتبال سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97589" target="_blank">📅 09:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97588">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxuLmJhRY4HrSOEXGe6LMylK_7Vkgpy5SR-WDaoM5_P7HJ5R4wRg1TYzn9faKe2lxICq6zjN0rlhFdtb0CKRb4yNDIUtbrWlxXxhuTmURo7dMdkh78lhqCt6Iezkcubrnhptayr0dmv1tUzhnP5vTjta-wGpBBtHPI-_UhgOLQGpVQXL3BHNj3WcM_yWIkIib_0Ijv1s7PNEy1CYysc8pdenAs-CXCdkj4NB-4BbwX3rDEadHf3EbhaM1F4t5054xie0lqkXf1K8kDzGjljgQVPc6hMb7SMcETyGn1vvULMLqAn11m1ThVWqmOzpZzNsBmjjIZK7giweCRSx6dBjjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
چیزی که وینیسیوس از هالند میبینه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97588" target="_blank">📅 09:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97587">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cfa932c1.mp4?token=Z5Z0Fp8luFd4fVbrqTJCqI2THsBswNMwAzvpviGVIDWDdu76SCboieStPgVmUcXiaehag6MfkPc1QZ2n0Vf6DLgN7PyrunHdV-qGJI39WbZtDkQwJa1EpqMF1sB0-Ep1RHYjaij8-G3iT_5gP1HO6I5agj0i7BTRsZCvxVrtVY8PtlkuDF5hCfS1Yy1-oM-2Spc1XRNblx4KDfKqmrg3w_PSJA51eaV0OzlmpCnuZREPnbIP01NE76rkLtP-QyOCKnUZFsUkMAqUyjr8BYHDsLbqUmorPSa01YW4ek_xQxVXxrAGIhP56nULRKp2Ee-vmNbwNFRAIkRkAazq1by4DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cfa932c1.mp4?token=Z5Z0Fp8luFd4fVbrqTJCqI2THsBswNMwAzvpviGVIDWDdu76SCboieStPgVmUcXiaehag6MfkPc1QZ2n0Vf6DLgN7PyrunHdV-qGJI39WbZtDkQwJa1EpqMF1sB0-Ep1RHYjaij8-G3iT_5gP1HO6I5agj0i7BTRsZCvxVrtVY8PtlkuDF5hCfS1Yy1-oM-2Spc1XRNblx4KDfKqmrg3w_PSJA51eaV0OzlmpCnuZREPnbIP01NE76rkLtP-QyOCKnUZFsUkMAqUyjr8BYHDsLbqUmorPSa01YW4ek_xQxVXxrAGIhP56nULRKp2Ee-vmNbwNFRAIkRkAazq1by4DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
یادی‌کنیم از مصاحبه سمی سوشا مکانی با خبرنگار برنامه نود که فوق‌العاده وایرال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97587" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97582">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUoj_SadaY4JffP05KxIe_Z0j-fk3BagRTPcaAPbnX-40RarU75-taPuGVN5Jn1LEmav2jo0XzgtWJ6HC3SErPglghwwQWWF469jWTYQX8JVpx6XqHOusY4WU6hs9dKFVEL-bM2Xo3uUh5Ews16pXk5XZAg0KnHvJ0vaGWL-E6oY8lm9P9TN-SWJcJqoANlhcAUby4S4tn1YCLWZP1AirX0_GQ3Wzii6BuZSVVxCTTQ1KmxKweHbhztvBZ7_ANujhAiopC_f0GPkdVeszeiRxvjgkV2u-YrZN031wvSqMhQNcGnMjsyQ38RUGG3fQPwa_XCgRTTXYEJSQeDuBt6BKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZgIk-cRKqYIMRLc2so5s_3I4Dg3GAZZXBkk1dW7NMNkqEJD8IZdQbnzvIBPMvz_7wcIzFUAPqaPw2L7yCGTrI4jF9MMy9QY1YzRao5pWEqqNqiKHGkuvBOxIQysnQa3XAGHdmwV4tvZARHBoUEzxrZBqsw71DXqDKyEM3mCvvP415WK_uUr3NYoDonVazY5ZCJREwoK1sv6qjYHyzdy0BS4yK4PTpNpxPQ-3wCHQajlU1PZPokF0zDrFU0BGVrGhNR0hqII7OvsoW2W7ndlSqWsPHmyHZqGUzKNhCPrBnkSzh9I49nqkujcvK9vrUMh-K4hwL0D_BmK1M6ANTdDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leDA68D_HeosmhNIijSTPVztnbDiYPA4cvaNTahLZpQv2HGhaZjPuFP5T9EOViK1emgxAr8jkLJmri5KSmpNWJ75wwxkBke8fgSuQn2niWyl_DYl2Yu_Rv92qecGWIYZEJ1VjPWpWx57Du0TEBwU0OebE0dc2tC0rXlPn9FknDefnPaLEAUfypuuipwkz0ebNRv6BuzafGFdHMA3CMFTogQ_6JP8E1kT9ucK_9kax_Mk2-IEP3crh7-vqlHDSajuJ88JOlSLfcFkMNfn9P6wiVwTt9iAmKjDWnwAjXRRQrNqwC9Dg821zS-p4-78xeIxh33VPQudB6kOe71kvze4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rA_rQ8HqirnhnpgQlFebkfVjHcp8fqtUEJ_t5Ob1ngK6T3TfRWT2EvOuw1F1bgg13bS7pknXy0WltuKgtXo-hGQ4wTujZfA1Ndh71MsLdtdZjqJr054GbiWtqc3TxfjGgg_W3LWwIu-yREyHYR4TydZeVAouetzk74V36kJea3YwG_a9ZqFFejNWI8KXiiFyP6XC7t8naxn3tyksWiKbjRv5b8bUwVTV1OnBEBw3bslNXZAEIMc7LOWMtqfzLJZ6ONWbeLjMXAzCVnXrnCD6uxYaL8uyec33StAchMU_voU4aSs9OBxtqFSk3KLyPLvnJ8erQHh7iM_4gwIE3xZToA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfeNECkkUSduoJjdQh_JbKEHqNAl0wSeHXlE_3wDIfnw158Ex7vTY7oSW0GWDHZpYTJ2K6aK27pVrvH-xTdgCp8kDaoN8amIhXPHGiTxhuv3S7IMJqqL0OlLDoTojV2ICXr8TpK0MMzTMblg4jmewCpUErB-JpKwUhfHPPjctg1lLajy5Ft8h-JykRJV1mOAratZbFSdhqlxs9GuIHCjYWPw5PzvSqzGGPiutXDkXYH65llHFMudPAeo05EwYn9o6I7WVNmV8_L056Or-fD-hTgYHVmC8kM4iAFLvMKoVpQROtECVyIhItxMj502AyENQF3KStVIf-zLNAxTgmC_rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیت‌ بازیکنای انگلیس با زیدیاشون بعد از حذف دکتر کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97582" target="_blank">📅 08:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97581">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6bf8f214.mp4?token=e4qb_ZZP7VsV0SlpvM0ex4MvryOVuWy0funwKmtS8scS3H6pCatfPQlAmMIU8PXzY5aKUtg603nPqqqgccUFmXd_RuRcp6Y-TomDN2999PhN9uDIuj2WjBLMtoqyDxSxsu5GhjtdFK97N-3OodKpdOaf9FRWyeSnqnebymR1sBRQtVYm4XG2djH0hUGQJfnAY7RRPIf1n-KTP6CuILZJbHAUzSv-NHhfdZV-QI22IVIR8h3dvW5NZ6ik2rjtd6n40YvEmIXwg5exKpY0WDQYIZ-ohuck63_PBFTfLgoUeZbSsO4EmPd7-kqm1vke1TfncLGIhG-4AeaVgdpdrPfBqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6bf8f214.mp4?token=e4qb_ZZP7VsV0SlpvM0ex4MvryOVuWy0funwKmtS8scS3H6pCatfPQlAmMIU8PXzY5aKUtg603nPqqqgccUFmXd_RuRcp6Y-TomDN2999PhN9uDIuj2WjBLMtoqyDxSxsu5GhjtdFK97N-3OodKpdOaf9FRWyeSnqnebymR1sBRQtVYm4XG2djH0hUGQJfnAY7RRPIf1n-KTP6CuILZJbHAUzSv-NHhfdZV-QI22IVIR8h3dvW5NZ6ik2rjtd6n40YvEmIXwg5exKpY0WDQYIZ-ohuck63_PBFTfLgoUeZbSsO4EmPd7-kqm1vke1TfncLGIhG-4AeaVgdpdrPfBqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
نعیمه نظام‌دوست: روی عابدزاده کراش داشتم.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97581" target="_blank">📅 08:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97580">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1MHD6PhOPxhTdLwWTMrfOZI4TaVzHy7pO_y1bF-TR8lZpd4zMhsTZjhfAwigPqzgK9vWoJclphcFdMsLwfHYB2LIPI501w91uJXJ1oZI8flH-SK6DeUboCG_NiSm0nTgiuqNbwZhBuGxGz9DPeCRV9hCyvrELtztMMXnHaGMlZEMJvIXV3eX4Jeq27rT0eP1zrM4cUTAErxThOFMQQpULJ-V4iNQgLQyLA1hxWyveqHBOiX5kgm4zxQnZ6Jm91DqZDAlr8b01S2p50ViHfXDvJEs-Dzl_oxeRJEjrEtsOxj5NE3nTXscUcMedI5wWCEFdwIvT5iY9vguWWOqvbVKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
ادینسون کاوانی 39 ساله پس از 3 سال حضور تو بوکاجونیورز به صورت توافقی از این تیم جدا شد.
🔺
کاوانی از اون مدل مهاجم‌هایی که وقتی توی زمین بود، حتی اگه گل هم نمی‌زد، جوری برای توپ می‌جنگید که انگار آخرین بازی زندگیشه. از اونایی که دیگه نسلشون داره منقرض می‌شه؛ با تعصب، جنگنده و تموم‌کننده حرفه‌ای
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97580" target="_blank">📅 07:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97579">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda3b086b1.mp4?token=Flt51R6sxioUxpIXvEDosF7o3QkcjI19kE10ehqH5gNbN4KtLQAD73lDTdP6rIQgPgf8ATu1_pEZMbiF1ASGhdq7SE1-l6-XYW5vHayMYpH9PmsX-Ij4m-GuaoCkeGhpaoKMLSxtM_3BklRC6bj1j5uNdNcBJrN-A2ErLlKjeVjnNMLJad_MJcUPHM8V5Y63e7nP_6bZS-bMKt2eE4aNIz5kCJumq59tPLE_7FzqfrOA-hvn2V-Dx3b5xkjGL7iOFUYDwbxivTbUMHYQaB2U9d7Ot9cck8hnKIexrWkY2t9kXP8-IksHE_l309jdQGj1D9JlZT-FuC3cMbp2zfBWmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda3b086b1.mp4?token=Flt51R6sxioUxpIXvEDosF7o3QkcjI19kE10ehqH5gNbN4KtLQAD73lDTdP6rIQgPgf8ATu1_pEZMbiF1ASGhdq7SE1-l6-XYW5vHayMYpH9PmsX-Ij4m-GuaoCkeGhpaoKMLSxtM_3BklRC6bj1j5uNdNcBJrN-A2ErLlKjeVjnNMLJad_MJcUPHM8V5Y63e7nP_6bZS-bMKt2eE4aNIz5kCJumq59tPLE_7FzqfrOA-hvn2V-Dx3b5xkjGL7iOFUYDwbxivTbUMHYQaB2U9d7Ot9cck8hnKIexrWkY2t9kXP8-IksHE_l309jdQGj1D9JlZT-FuC3cMbp2zfBWmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط فقط بدل رامین رضاییان رو کم داشتیم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97579" target="_blank">📅 07:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97578">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15220e2e5.mp4?token=bCfncHRQFINaqbE6_4ksOSQlOa2317nBld_yYnZRlc1kTMNqMfdlKa29BZr5rh3uGGyS4-cE9mesNgQI0sAJu8tLeBXYbIZdWSbYCmY6G6Cmy_J8qI8zB7gvAbUvlMNkU64PENpBbmRFIStLOvgEB3AXhAQouFDk1yzByFyQ0igla1MrpeLR6JFiFyK09L0khEyHdluKL2DZUt57XSLulBqzCE7FMDiBOu_LJIJKoS4fBXVPpi-b77AsNQFNdJFpKwwhVa4mdcOqdv-ui6q3DQfaJ2MD6smLGu0dwkzB4eLBsIHiB3ObAxNzt_ILIps4pa_CZ79IEFklD9WuT7RhqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15220e2e5.mp4?token=bCfncHRQFINaqbE6_4ksOSQlOa2317nBld_yYnZRlc1kTMNqMfdlKa29BZr5rh3uGGyS4-cE9mesNgQI0sAJu8tLeBXYbIZdWSbYCmY6G6Cmy_J8qI8zB7gvAbUvlMNkU64PENpBbmRFIStLOvgEB3AXhAQouFDk1yzByFyQ0igla1MrpeLR6JFiFyK09L0khEyHdluKL2DZUt57XSLulBqzCE7FMDiBOu_LJIJKoS4fBXVPpi-b77AsNQFNdJFpKwwhVa4mdcOqdv-ui6q3DQfaJ2MD6smLGu0dwkzB4eLBsIHiB3ObAxNzt_ILIps4pa_CZ79IEFklD9WuT7RhqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی میفهمی بعد این بازی باید اشک‌های رونالدو یا مودریچ رو برای خداحافظی از بازی‌های ملی ببینی
♟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97578" target="_blank">📅 06:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97577">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLIk7TXCnJUjOO6xbVMx1wwt7aFJOOlB6h0x9dVss3MzOxCP2WA28CapqpxIRZHZGk8khcPiqslI7wi2xSvxcUyWIgkMMu2rs5TuRICiSo1Rqm7aijdftHPlxyb8-KOs1rgmpT-sHQjIhwPdOsDc9NoPf855z_Us6R4pv-hNCwVwkaM3AQBGkPZJnZlBjDSbsVLPKY828V1xYxV9c-lfffKEU29maPytPqIUTjOB-TJOgXLh0e0oLCHrL9Kfl2P6eIT6bTfMCgWz4PJHAWUA49MVdl7qe7CQijSGqymUH4OHvwtDZS1n-4g2UmxuBMCfK8zdpXBQ4TFhnBgZ5gaV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🌎
تنها ۴ بازیکن در تاریخ جام جهانی در مراحل حذفی هم گل زده‌اند و هم در همان بازی اخراج شده‌اند:
🇺🇸
بالوگان (۲۰۲۶)
🇫🇷
زین‌الدین زیدان (۲۰۰۶)
🇧🇷
رونالدینیو (۲۰۰۲)
🇧🇷
گارینشا (۱۹۶۲)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97577" target="_blank">📅 06:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97575">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWR1ltaSbONXwTr5_JfCcjD-Qr6HSmkUEWbFSVUKbVNPARsg_SxQBIsn-KS4MTcB9008AaUIxmlXpqFmF_OSyedn-s1bx9ETrwv75YDi4yciIpEq1trfwuoBhZbtAlcPx5W7nZKmGN92bZhvo-p11tYq-nLYI1aHg_X8PXCPfYz273MM_5dTF9xj9b7tsmZB8qCaPCAG00_M1HxbDnfM2r9sTShQeTU3xR7PmL5K8KWOvS5_r7_Z32jgmJqDAVX_2dnzRukfrD-7wn7aXC3RDqNJ6B_ucahNPOYFPY3RB2eb1ZL2GL1hiBEogLGesCvjDF8gdR4s86sU5Dy4yHDSMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NdmN-FiYLmcI0pdrsHlnV9MBi6gRI0TwAO97H2M70k8gx-bnpHZCroRkMr8PacQnmVVz3PwtRNgC0O3kju60PtW6FPwxw8096rHBRzYHxIKaPZiGKSYOeOPqMhpuI4vVaQ6UAeD6DTe1D4M5MRdlpdIWzFiNel5ZCmDsc7Exi3MsG-HWqFWV41WNfmtW_hdLfeHMaP15RKc25N3szsCuSm0tEzL_P8FMFtHnfGOrQeuDk6OExt-o90WglTAkN8cPL9JMdPqJ5vQ2ef5w2eAFTLkanel366y_d9Hn-zym-ZwtyA8alj3Zo3u1pDPPVgzxMO8uaay7Qir5iUHCKBLbSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔺
پاپه گی در اینستاگرام:
🟢
بعداً درباره دلایل حذف صحبت خواهم کرد. اما امروز اعلام می‌کنم تا زمانی که این کادر فنی در سنگال باشد دیگر در تیم ملی بازی نمیکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97575" target="_blank">📅 06:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97574">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qa8omcMsFl91UW2XKTMCkXDItAkrXZlHnWpd2E0NvFeJyjNrqnFswNLrFpmNOuBWNYwYnfvt39YPyEBe-Syer0S4azkGBbe7XFgB44Jn8VUElNyhRArYU6sXuOXYcq4LjG6vwbqYDTzVo8f5sux5Q5qbH0UIo_RzdItQzhI0XVdMRwwD46Rr9FCLt8mfnq9D3FmcPjSPQtvGSBFwyyppabyr_IGwh_YnlFQGL2YS0F9wasf0-8nGvTABdtO9Gclrf9xv8wTwsyrQSy_qHyaCcN14bz_A5_BZgK0K_LFRUz9rMA_rY4hSu3gsYrbsJE4eLBO0V6W3guKMBCEJiZX75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار درختی مراحل‌حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97574" target="_blank">📅 05:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97573">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5hvLkH9VaMsuJJmZxJ_wwumvG9Ru9rp19wpLbfJQwmRRj4jMqHwWT1410O26dGGd8Ma1PpNmZI0XDnHMNjDdQdKi_79SuaoG2oW7QxU7GLFQNqvY70N1Xg8GTMsc60xqrYkOiHe12LqfEJo4ib4qj_X-AsRGhb9vY1h8WAGkxviuzNieffmBgzLYZLI3wMx6eYbKudAvC0F_vn_Q504FNNIv4krX6DsUueXNhIjqkg9zcuqfWyJ5sW-w46V3bKQ2cjJLLcaEmJfgP0zbzwF1ePeIP6mCDKqVzL_GAXJAG9trCEw3v3AfPcGsg5oQOPMZA5koUGJ0zw0oSdd6rAwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇧🇪
بلژیک
🆚
آمریکا
🇺🇸
🗓
سه‌شنبه 16 تیر ساعت 03:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97573" target="_blank">📅 05:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97572">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu2j_bvM923M1zyIm-sWo_k9BDJB8L1Zy7O-9oXRHPNY-PpeSM_06OPGxNrPYxHSdRgqNDIuLVjyJouOZh4-dUdq6g8dx-YSZf6rLM-thlZ2KJuUyWr5eC5m-uTJRXCxz-iTwURsVfMw4bC_K7S2NSkK7pDyrRC4D2B49A8Xf47EGWRrgRvWnB73RtjIsHKeC_vnppFffEVurVSwOqZsbCsR5VvAfMUHSSSvkHTtf-5Jl6SGHWgijRbipdVjCDCjXhSCE4hjnEWz3XZw3iX_ueon18XsTTY13OW2IkbGs48rdY-F_MZbmY1ML6SY3EP6KtH_AJBDHveHfxib_DXB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | پوچ بدون بالوگان در یک‌هشتم به بلژیک رسید؛ ژکو و یارانش به خانه برگشتند.
🇺🇸
آمریکا 2 -
🇧🇦
بوسنی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97572" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97571">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNGTHawF7xIs4uJ44wfOskHEKHm8fSembCqRO2F_yndO4gpdI-exjoChThGNPpa0MdwP4ysYv7NY9sfSn90lMXIUcysIEvjNa01JF8kZeK64WYm7IlvjRiW3WDUH1EDqF5Zbe-RZG_hrelo9d6LAt0cEzH3v9dPRvZMzbFKLXjPlVJ-L-B-4Zc7Zn5SPEM26SXGu0pnzw961dVEcr676yLax89UqoU-8MSr1qBS1Kq8vMWH4hhid9vhjKaGYDiVc5qe4OYIwDG9vYNu-xSmsYnLbnKk6xRQqjllyEjbJzCU2mf0ov31TJJLQ6899X0PczFzdV4o4lwdat8WkGpfLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#رسمیییییی
؛ آمریکا راهی مرحله یک‌هشتم نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97571" target="_blank">📅 05:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97570">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ده دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97570" target="_blank">📅 05:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97569">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ea16f99e.mp4?token=SJSrShIE3Fu0seofb1FxCe5ohy4pXSoJVnxVv_Vz9U8Lxp5lsSBTMQ06Rp74kL5O6lRvN6UNE94v3KdpR9mcXxAz-PqZgaRgtPGm_-zCdIGj-3_OvT5Un3I89fOyhnu0u22sESiV27N8UMS748N8ioajWBJlSB7kv0FWu-psQSZPVv2aeu1UvSSUwSe2TzlXCMizriT8K-Qi_dPPfZPxIw1HEs_FD8s5XQMSk7Z3XnBJUvIJVHBGKFBLA-bJQZl-6yss2h6PCqE3kL9aJY_lJ1I_Ny9ZIeCJgd0pWKYgO_3xDzA_WJxNeOEZUh-FOfjlbRl9xM7Mjno3U6y7kumgsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ea16f99e.mp4?token=SJSrShIE3Fu0seofb1FxCe5ohy4pXSoJVnxVv_Vz9U8Lxp5lsSBTMQ06Rp74kL5O6lRvN6UNE94v3KdpR9mcXxAz-PqZgaRgtPGm_-zCdIGj-3_OvT5Un3I89fOyhnu0u22sESiV27N8UMS748N8ioajWBJlSB7kv0FWu-psQSZPVv2aeu1UvSSUwSe2TzlXCMizriT8K-Qi_dPPfZPxIw1HEs_FD8s5XQMSk7Z3XnBJUvIJVHBGKFBLA-bJQZl-6yss2h6PCqE3kL9aJY_lJ1I_Ny9ZIeCJgd0pWKYgO_3xDzA_WJxNeOEZUh-FOfjlbRl9xM7Mjno3U6y7kumgsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل دوم آمریکا به بوسنی توسط تیلمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97569" target="_blank">📅 05:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97568">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">عجب تیمی ساخته پوچ
🔥
🔥</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97568" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97567">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ده نفره زدن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97567" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97566">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دومی آمریکااااااا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97566" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97565">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گلللللللللللللللللللل</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97565" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97564">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNVB3p08IvXAMUtFhV5y-KklUhNAWWige7YdN35aVxUiDNiezQVEYrCqLSAbfuJ7W6957UbMQ42mwLafO7dFfiHKVj2MIefbPqtE7H50gj9Nqu6e49D5pXRAXjcrURqHQWQAU4otLNqRC1zwzwkGAaB_Y5ZtxMKQqsgsu4YLS-uY3tkGrNzyFfqqurU5hA1_gjO2ItKxDuoY5KhLyc2oqFuvXHO5WQ3NkbJNJP0uQ5HFvjOBiEp32Lj658sVJNt7iJzWFj-FUcvXtYoaUdUI3n-_Ex24sfGik2IjMrSS-fTkpSK3O6sAPIRv7Q84uLyGOOi0cg5q2x36pVzkctdlOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97564" target="_blank">📅 05:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97563">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دومییی آمریکا که رد شد
❌</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97563" target="_blank">📅 05:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97562">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAwqIkUhCsGFcGFMA8B7_3N57fkukox4AxeEhV3f9wBaFa3QoUlo-R1t7BDrr4FXSgOQh705qLBNUPxQZw9K3cMTlPodm9guRfGIido0XjWI1m3ed8QE2-tlm-QoYeZHP0MMOFf4DaH5gdrJRFR_rWjFPXIw4k7U5lSQA0kc_ijpgIz99_GLprb0sQcQzEdGLpiobky73ELgCxErxqUiGZdJjC1gpREKtFaCY7D2PGqihnoArYSOEjYyL-vvo-INRJNJc5FOS-1EXULXPbzGrwrfWABdMe2aoe3lnG2neKwPW3kBhm2Pv_zTt-YmjBlSIlibmz3OLIyiCw5QerDxFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالوگان اخراججججججج شد.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97562" target="_blank">📅 05:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97561">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بالوگان اخراججججججج شد.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97561" target="_blank">📅 05:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97560">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دقیقه 62</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97560" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97559">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اوه اوه رفت کارت قرمز برای بازیکن آمریکا چک بشه</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97559" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97556">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VdAj4hzPfn_nbRcJOe_RUL644u3V7pVWMF-PxCNjRsqBspAdLBeOsrHTrv4lKO56zoSFjCBxSC-A0TbGR_1nHcGU_yrFfaz6EHGuiVIIXvz3PN_mx_xMFeo92hG8oh7OHvRxm7jtQ_GmLWk5sU1HkVqa9vCEyF-54nspa4Trh9f9JvRWhmM10fDclezfjSh55S9lUEfa1xeilRY1hIcm_YrTIki_gRjx1XqGzCJf_I-wt_TPC31czL-pK32PfPb6sV-_GGoJVzCGbMLvZlR-avotmqY3MikbakfHR9HA1kafDuafSrRCZs7BejsFKzFz3lE7ObYoR6tXEIvURIrSaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-Ml86sMHx4LXQXFD4uoQSFK4Rj8RO8hKdZ5dRgR3myfo-AKpUMshxJ4RkpEq9x0BbElCaMhIXCtyY2A4WlXvmtfl-i3Usji9juhkFy_GG42HuiMMxhf5TgyPibzg3YMXMZBdl9smdp-Azl-ZaJPfjLKmgTM2RRQfuNY0fg-556C65-q4CUXxsh-_yGnWqepv7FKyr7BEy8Pa0t5tijH41W4XS5T_OJ1yfSsCHoWUmwVrfIsaxkR4NhAiCB9ZK2zsRG5-yTdrFEsF25mc1xU0rDbqUUz6UqAZR4y8X5OunOdWjOPrJOmOd7tCxY3v4xgC9GqWMyA2qBK-KrsQzx8Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqMeWbLVelX_5uE0AdMPtH2egUuQ4GMTYrx3VnLkuUbREzcT0nrKYNkBmP75jXZN5izqgyEzfhMqnoHbmuuCVMah6x-whGCTmuDZM3T28bzt8PCO3r4jYmO0R26-ZCkRQ-WPhcajXnmNw02llL2HebwilsNDGWyXJfdwiLlip5IV4AY4iIqXmkPSrBVd5k1L8o2hC74p6Rw_bzKPGBVYUvyE179-GEgSoWCZUWh6xz9f85Jey3Swe_iO2er_R2mxxSxRtv5UhL0Hni2vN_FV1PkqxZoXnxj5C6IYIbomEM5NwVI8r00d5JP9q8eWUNPm1MKnOg0FB81p8qG8oDQFxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
بانو میروسلاوا مونته‌مایور مجری شبکه TNT اسپورت جام جهانی هستن
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97556" target="_blank">📅 04:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97555">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6nLXZTZc2_Ww8cWJ8Ga7bkCRLPmsQbSqJ3ELgOzwMWYGKs45mVRybsjz-2QeGUmPfYrgAETODkDTIGM2v6bdDVA8CNHXdlwqsg_5za1ad9sYPoW7rJ6FNM8wEPq1ZwfSp9ROpMc1MV0ew_t3ShE3A8Ud792qDJ_s7CyqcbrVlDaAY0d59fUyiEa2ToAbR0UUoa2kQ_BLDr31S-qBkwJaVfGZv4X4aFXpvCLxR7DHuVq1SfCuctcbZVma5JWuj0RbOCChkFZUw_cNirjC7lCtoHeXRzvyTuWS0eD_ze3-5D8sPibjb7KWCNPH3qXEAyn5C1u5zv7ik8dmuccxvvFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تاریخچه دیدارهای تیم‌های اروپایی مقابل آفریقایی در مراحل حذفی جام جهانی:
🗺
اروپا: ۱۴ پیروزی
🤝
دو تساوی (که نتیجه در ضربات پنالتی مشخص شد).
🌍
آفریقا: 4 پیروزی که دو تای آن در ضربات پنالتی بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97555" target="_blank">📅 04:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97554">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am4ngYoFzkRi_iBY9m_sqwBuNGO7-kSOhN3_YYbSQyq-Zf8jTshZW7O7IrnIT3IOOfHZtZ4Xq8rBgKJvUqXvM70n2VLjAv21tTraQZDKJGPu5szjHZekKY6VQKU1_xzFizvx5g_9O1aSYPROnCmGqI2u8bEzwJmZm0DomkiYtL_Da5VIKl6fjU40gfVY84YHRKCEEAI7jasV396Mb9VTs_iqzJsU4VJl6H4ED3Zqd17iOF4aWrdSaGUPgnqTvEWzJe8YYKz829XC9iq9H35VQ36Kg5-HuGIFbpLwqKk5OKtMs99umWYNRGco8HhJ7RLm29ey4p29FmnpxT1v6tNsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخ داد پرز بخرش
😛
🎙
ویتینیا : لوکا مودریچ برای من یه الگوعه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/97554" target="_blank">📅 04:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97553">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/94e4656d07.mp4?token=bH-N1Kd95uF7gpeX9J_EZi8aO2SxCGKD0nIOajTnTtj-6ioxbumDduPLYSEWYsTiA4t2FZ2Rd1NvHj61_d-Q8Co_d78EWaurf_9hFH54JgCgolrQR0DIiGKWTQOBawGelfkGhCU6H84h9aiw8aLqonXCtNGP0WvRhktso1ALRYr3X93-qVwjGSajN_uY_0ttlmvDZHD4uHjGk7FSMpr1yv4Cn17DS4FxjoyWJXqFdl9OLrqzyd4u8rTgqpH4hcrtXu0sEqN4LDAkxm_LmRH8toLw8ZTE5tGHB47wXrJuwFU0PzguA3rM8WyHnESFQ7r0c60l8i2NvpT8seygy8TNuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/94e4656d07.mp4?token=bH-N1Kd95uF7gpeX9J_EZi8aO2SxCGKD0nIOajTnTtj-6ioxbumDduPLYSEWYsTiA4t2FZ2Rd1NvHj61_d-Q8Co_d78EWaurf_9hFH54JgCgolrQR0DIiGKWTQOBawGelfkGhCU6H84h9aiw8aLqonXCtNGP0WvRhktso1ALRYr3X93-qVwjGSajN_uY_0ttlmvDZHD4uHjGk7FSMpr1yv4Cn17DS4FxjoyWJXqFdl9OLrqzyd4u8rTgqpH4hcrtXu0sEqN4LDAkxm_LmRH8toLw8ZTE5tGHB47wXrJuwFU0PzguA3rM8WyHnESFQ7r0c60l8i2NvpT8seygy8TNuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللللللل اول آمریکا به بوسنی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97553" target="_blank">📅 04:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97551">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHQehGFo9jTfyI3lAJXGq0efTxXtvyyoblsTnLAqBek8BLChx91K-UlpkpYQ19P2TE0brbWacw3fDWrPa_L2N-P9SHwjwxYXTWTbBxWBs7ptTWka3fKjvtAuYpzy2au21gzuJFWjotFX_yOBVxcKeiqLOaFsQDIjdQkJKzeYek9v_s1MKS7ug6aSc5REdvEdX17sSbX_RjRv1l_MhF13Ak5KjcVUzXEhp53XwDUDDqm5SgCoXUiwQs44_Dja9EBdv55dEI0P_9fNj_lbMJLBl3-gV2mTc9LTuZZ4_mD3buGvYFDljQ77kfMU5L4JQwUhSvr_ooOtifHLOOAn72iXKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇸🇳
| تیم ملی سنگال اولین تیم در تاریخ شد که پس از پیش افتادن با دو گل در دقیقه ۸۵، از مراحل حذفی جام جهانی حذف می‌شود.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97551" target="_blank">📅 02:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97550">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHuqS12ZF7GXCep0HzjhWsA9QeWvyO8mZlPLq4HYDMM0QclgPYcPIjW4Z8Cuf_tOBYVH6Sv1qtKjaEvExp2NOikU1dOZU3ZDATwYHRwbLta4vQrJAgnffJ9RMuQshxfoZ0D80iXfaT9vB9N3T6lo_ogh35wAHKrgc98cdMUsQmdgscahKoFWmGyCY9vNA9GekwrIqRI6JqaV-QUO-6TL6-w3ySZPsq513R1CGNTn5JNoz7GyPXQFSX8qkdZEKJQWFu1ydXmHmkySxom08AdNVCkC867bfuc9clGI_Dse9S3fohTL-GlJcZfBWRp0QQ3v6mbyRWrHYbx2xf76XURszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇧🇪
بلژیک در ۱۷ بازی آخر خود در تمامی رقابت‌ها شکست نخورده است:
11 پیروزی
✅
6 تساوی
🤝
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97550" target="_blank">📅 02:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97549">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXcagZ5zhkUzlHgSo_dN-cXsAbI8iYQeYVeq8IETqqsZzm0jc8qEACpuz7ACUHAIwgxihYC4lgzWCSJP70Ar9eJcjTizUkhFkh4FxIA6I2wepkvNwG5RBMAGmNbQQMjxM494xS3llDD-8kGubeLLyt4le3V0Zw7YpRHKwksRILLX4PvKjw-k3vh8w7jYdDUrbd6yE7XaSH1BnqLzEnBbx9rIvDMI9BkUdrXJtRXIrcA2Tr4YGQHOmSOkGiy31yOqjFzYO04_Em3SvSSHUHZexKdR6yHOdx-Yq-ziU_5Nfp-18pG13Ve03vmGzbg9EHqKLgNN6xA6tlNsLbKIrPP5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⁉️
🔥
🏆
بهترین بازی جام‌جهانی تاکنون
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97549" target="_blank">📅 02:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97548">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgLc7PxzE3CRkRf1ybBoDKfpKKJyFakoUUCyHbM5jaEoiJMk7ZcfKPSinbNx9zC4gF9Mf2t1Ks0U8B0pRifZQUwtpaAuHVF3C1_Bm6_tGCRwLkfjNNceJOOpH6kcwV_KKPsFXuH90Fv12ZgeB6CBfvgNY7v2ubPTiHlWSeqi2uM8FJix-SlEs3lEkiFoCEHmLboP5pjUGC5JmAwgYIbUqyVSu4YLZU2cmiaQrb2YVH5cqVJ4eehD1EFNP_V59wSW46t5uQ2i21kMdO3o8bnO6jYJaXakDdv58uCiCE-X8liQYC2bOYEP2eedMQHCD7J2Ntrdmwc4NJeObJMMea7UOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇧🇪
| بلژیک برای نهمین بار در تاریخ به مرحله یک‌هشتم نهایی جام جهانی صعود کرد:
‏— دوره ۲۰۲۶
‏— دوره ۲۰۱۸
‏— دوره ۲۰۱۴
‏— دوره ۲۰۰۲
‏— دوره ۱۹۹۴
‏— دوره ۱۹۹۰
‏— دوره ۱۹۸۶
‏— دوره ۱۹۳۸
‏— دوره ۱۹۳۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97548" target="_blank">📅 02:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97547">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6TATxMzFJPjYiFfd76Cd0FXY_0GoqZqUsnwyQq81lX_bUpLSvDOfUgbbFp6GX3tJX0Xa4iP5yOTBNNeoAUK5wMwwxR1Z57iAIm66RbndVrbKRPxAcp13tAZASGek7fztneu7C6FnjLI37EyTojo-eMiSqENAXCmMst4IklCnFpfaeQvF3jTZrwgrGKouByVPSOpRDrLdVinHrSTDRVt1vg6vOnx0vB4KDrX09auRHjc3afONyZqbO_xJcCO7YJOWUpYNlv5y307govsggRq8QWkyY5vuz0MwfwP9Z7sKzQirdykH4FTwwJqp6smT1jOFisAJIy3kgT2OirhH9ckwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
| سنگال چهارمین تیم آفریقایی است که از مرحله یک‌شانزدهم جام جهانی ۲۰۲۶ حذف می‌شود.
‏ــــ سنگال
🇸🇳
❌
‏ــــ ساحل عاج
🇨🇮
❌
‏ــــ کنگو دموکراتیک
🇨🇩
❌
‏ــــ آفریقای جنوبی
🇿🇦
❌
‏• تنها تیمی که صعود کرده، مراکش است!
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97547" target="_blank">📅 02:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97546">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4hB2xe2cWd-555kNR02Ji-3NNHQIv7HtNdypU4G0qqXgFjT99mlBs2yXcJGox3pMqv9SwB5SzxsNlnbySsbO8gyV2gEQVO4FHMoWUEIqVYa05dAZ_xDIizFfDDqrXhBLQSX2Wh8N0qxNJ_XCwqaj_4tf0J6I65CnEWyDVs5L0L-Ali5-0xWDrl3vrJJL0C-PbQhaDoZgcoC8siV7ICfIQ-mJScbwcWZkli37UCxy81nEjoFF9xedYnmzvshLRJ9Gyg6fjI-r_LTzfbJLneNa6sixxgMxHmXZeoplTt7zLh2yy585dFOGVXnDjzGYE2rXGmNRNJB_9w0a0Zy9vW7Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک تیم از بین آمریکا و بلژیک تو یک‌چهارم بازی میکنه. بعد هلند و ژاپن باید حذف شن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97546" target="_blank">📅 02:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97545">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4JSCJRBfjPjPV9irmvaWDB-4XZTf_aYzQRIA6HSGfCc6Yh-8FeljLG24H5h7fxglvrHYTedvy-Dg8wUWaVpwkfkR18Ix3HhYWIgs_ozXnK-hWMojfQfJTb-BDE9i0ueDVcTdrCKRi0Pr3eHEXzM2gwU73Jd_3Z0KLYvN_IrZLa9bCTMsX2sssd9cRqbPoFryBZwdyQkaNta2UYq66gPGhxITpBsWut3vcEw-w3_uWnNsSKWNE7t_hP2Muu3AwGsW4Qwt0BBhRQ2995x_n3zZcLP2rUIK7W4jJ1joY2o8VDmmY0uIZH7PY2wZwnFacIOGwg2M25GS82Aj35u5ZkZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار درختی مراحل‌حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97545" target="_blank">📅 02:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97544">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAoYU1Zo5wajnH3GB8ECj8KCJhCQ3d9tFnhiUVsZP_iN1ixm-VyNEqiS8D-Jg3NJwf_gUoImR6zcsDqoNh30rWIL3jJgSg7GHVVjBtxt3sAn35eDEVsi-Xjil8C_-yrSg0FqfsryCqhZXusSHz0Fr6Ew7uYA2lOpiXJai0WPSHx3sSBX3IsRiDEMRJiFGai3fZiIMxsJ9ImInf_eGQ939tJV7I_b5rS6dnFZGHZkqMj2CwVG8_c5qZmfGVKqZnUyf9jQEaWC_rsZx-9AaKxxPdRP0rG3PPcMydB1_pXynEhJaN8k3XYRBJ1DMggR33oFEjKHKjx2gt_XXGZMDsuIHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
گل‌دقیقه 120+4 یوری تیلمانس دیر هنگام‌ترین گل تاریخ جام‌جهانی فوتبال لقب گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97544" target="_blank">📅 02:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97543">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw0l_acocI-RunxV5dZxK3Vw9r6C88af7PCn-iriLvOSwDHxnT6uGZY054sJkIfHW_ywwDGcZ42TRI4KKqe-GbLydMleAP_KPbm-ZQvnHIpLIxfD19VeyiXkzd44w-JRSLKFezvH1QloDgTuXW50tuNRYHAd5bGivE-9udjkXc19nCC-o8mrvsSn_x4JyZ-yR10pzpscWnITPmiWBObu6sXBKaJ_yQ9PSnlDcnl6bTj_bHA11zSDD0E03rn518cdhBBR42cG9bOMqMYt45j-cIUbJSyN6EQxEsM07WO-rNqO1L8OmTquixhuhNvD-Zi_YcxUTlD_ylTrOJE2-g8Zqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
آرشیو وار:
پنالتی بلژیک درست نبود و به اشتباه گرفته شد، بازیکن بلژیک خودش باعث برخورد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97543" target="_blank">📅 02:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97539">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fmb7ZuBfnApc--OXNq5xRXZgiIL0UK3Zv6wmWb-FIcMT4G0XPuqK8eXXif83No3QUtfX_xKyYQ9yteGOpRpVCbq_zXm5Yoo6FND1M0TXo9_WfIv8t07Jm1ZwBgt6Omd5A71caenk3ZaqhI5YhIgGMcpad6jPC7MKoEUtqwGLPW0TYVfrI-YJ5a_zYMK_Odq95lZwYtG3v82aC8ihKPLiuMdk2Hy0KblVJoyI2z6qHmvBZER_iAi91zTzpciffOA_apBL0AJGAdcFYuBZfGgEHWzdF59WXUueGmx6L0WZZYCiJLaH9fBgi2UnBswThZQF3tk0hByGoT-TywrMwfi9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fgu0x9Wqhlx5PogtI2oqVi46e7vF1GGh0zC9r8csnB45j2TAZj5HnoXod_HYc7pDXTZ-miyTXnLiEi2_U7MOTj3M6hrRl_-sZ6TUAFUXdP2yW40WrnuEINkJ_Ee9quzjjE4vdZWoHVwheSO_CNmfChVwZ4xAQrjwqta9-XdVNYgP3-UEn8j_hbbjAZSy5IDSYv4BcB7dW3Lp_KKhXOWuLZiDTcOsfgOMcXxnkycrc6dQ_aclo2Q8O0pPVnvY3TJGDieeqdJ64_xCc11rtn6kE0MaZb-W7eeGn31-wvJN0NlSown7ep9fme-ZzQiXXEw3-xNHC-QTtMEYn46wY6oPCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
🏆
🇧🇦
ترکیب آمریکا و بوسنی
⏰
ساعت 03:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97539" target="_blank">📅 02:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97538">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nq_0tnFaFPETMJBeShmoSPbwnTahs6YrIFytIO4aLINF2jn-gCSVyPvXbiGiZovxRiFXDgSP3TYbiDMUIRYVgTveIkfzX9TjhTvpbFP1ZKpk3_4-VgvDYHC1mv5SmJv_b9b8XJ3CGvwYbR4lJP8d2N_g6AeY6DXsfiJesC6UqRfSOTLQcRAoHknV3gZm6OQXUC44shHDWyrV3a0MRO4JUDDupGZGwHzcFrEQlCbqJ98RJqdlVNrkRUcXe_DLFAsPsHNWmqe26NATl3quOSP2QkysDgHeCqn9B5PnbcTh640oBOjoTZQ02I8Bb6YRjf3e8XF3c1Eyd9q3xm0rj28o5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇧🇪
برنده دیدار ساعت‌دیگه آمریکا و بوسنی حریف بلژیک در ⅛نهایی خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97538" target="_blank">📅 02:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97537">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgLpWgsyUP5Auuej1n3nHcQX9536lhggb_t4ghUwTQjkmaqI0pDvroa7XLHBR3wndAfkv0kLV9rWGgXgaxTpJgOFgmoQ9omaBQXFFsgBWIF-X3G4_D5Qsc8wu0UbEqUBa0p98235V_4pAg9LnPhKrJUZFky5t7DNGUYxS7xCCPqTILuIW8D9g5PlZ4zLfUUwMv_MOPEK7nRSTmDf5yX05uIqh09kkpDVNX1zS_YLE7YSJ0srKYjcbbYiudsRe0nqZfG3eCBO27ofXNxSGUDNXGPlOwbnYCx8SVaGxOHxliwV5mf3SBIjoxIKUmc7ZPAQcDMvTRbLp-LynW9Wdd2VlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌های فعلی مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97537" target="_blank">📅 02:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97536">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGGqRvDooK-1kQwUrKYU2-ax5sRG2A538H-m1tuajavSJO60W-dJRUhqXPlmGQo9kHshWb2hjBHK0CuBbXok65G6d69MkDmxO2extXDjzt2LVqXtXtix8TksfUedYtRjqAVATZfeORq8xK3BzzAg5v1LkXEA5W6OLdpEWWlgRApkMyc_8CpfkiwZFjXdjEzw_o9jd9xocBWPPdO7x1_cPmUA9yt9A4fUkqs2hkwvCyAjcvPpQawZIT2xrum92ZHSu5i2MZtl4bZMQsX9D-GIsf_6nv34Vbd7TcgdKg1zTAtx7SWmy629CnGIB_7UocBOi3tQJ-bLEZ_wkrP9KZpO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
و تاریخ که باز هم برای بلژیک تکرار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97536" target="_blank">📅 02:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97535">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-n7_t8Y1ioYU3JDqVnw86i8v_9ZiKsYVpvKgrGUmf6pigYtls12YN2-z_ir8zBAKp9l-3pXJslI6irS7yWH7WfIyXGUJaOxBtF8HJY6AlbXgrKxWppxWUOmsKS0-rCqSSrk56DGS8a50Qb3JGN9AniteOaCS0g_uKt1_OPSgy06Fle0qT_IuCTjGoXpdPCJyxE7s1ZRa7MAQlQKQIDXRUmZD06-2fagBz_HSGFEQA0_nC63Al7cJK9WAALBEu4z4owgzuRr6FeryKeV_fFueulObeIt_XB2akkRckNRJZmOaQrRJCJQpjDFjvI7M2cL09npLNoM93cUkxjeKLzQ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | کامبک بلژیکی‌ها با پنالتی دقیقه 120 تکمیل شد؛ بدون دوکو، بدون دی‌بروینه، با تیلمانس!
🇧🇪
بلژیک 3 -
🇸🇳
سنگال 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97535" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97534">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بلژیککککک صعود کردددددد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97534" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97533">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تمامممممممم</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97533" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97532">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تسلیت به هرکی گرفت خوابید
😐
😐</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97532" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97531">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دقیقه 131
😐
😐</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97531" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97530">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">میگن پنالتی شدددددههههههه</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97530" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97529">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چه حساس شددددده</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97529" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97528">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سنگال فشار آوردههههه</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97528" target="_blank">📅 02:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97526">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0db93ce7eb.mp4?token=YKYoMWEb37orcfyE7j5WBTdfzuDSDT3EzjcOTjZf78tly3HRE-pOjeU6xDh4b2Z3_pe49zP60HnkbOBatqCjK5imhhzgSCLZi714ZKeH6h_0y0IbCLJ4lE3i0dAidWvN_oFJhszak129wm_nyEbTmW2Q9HzMtCopnz_X70E6wovQ-ch4W09HhTuhIjW3mEFRvCvMcyTdMaPZkeeffvFh18QH5BpH_8J-PkBABQLY96PuFRwsIB6thQDEOtlHjJRO1jA3dIm9RTdlrUzL76p2opCw73O61IjGqj8BgruXrbq5Ufqhs917Nt12kx1h_YhuqR5ZiVsH8wrIsbOJJMKTBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0db93ce7eb.mp4?token=YKYoMWEb37orcfyE7j5WBTdfzuDSDT3EzjcOTjZf78tly3HRE-pOjeU6xDh4b2Z3_pe49zP60HnkbOBatqCjK5imhhzgSCLZi714ZKeH6h_0y0IbCLJ4lE3i0dAidWvN_oFJhszak129wm_nyEbTmW2Q9HzMtCopnz_X70E6wovQ-ch4W09HhTuhIjW3mEFRvCvMcyTdMaPZkeeffvFh18QH5BpH_8J-PkBABQLY96PuFRwsIB6thQDEOtlHjJRO1jA3dIm9RTdlrUzL76p2opCw73O61IjGqj8BgruXrbq5Ufqhs917Nt12kx1h_YhuqR5ZiVsH8wrIsbOJJMKTBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇧🇪
گل‌سوم بلژیک توسط یوری تیلمانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97526" target="_blank">📅 02:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97525">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak4FYUWRLXIxjmtb5np5j1tzSZfY6g34zgTmy2o5CJtjrecFAdSK0AbTMmHBJ2pZcvGyUU3U9JKIu4afWYVPv-unK_qXnfm490bqrG45B-mEoPj8MWzFHLOArx0jmD2uxBjJ0qXNghauP7PQN-7U5C-gmbhX71xxW525LUHELPOwSFj5vGJB2VLGHSc_9PFRR2Z8gcBdcpgCZROENTl_Mc9fjYr0go3PFLLzr4ASueXsgk6uplretWPMlxAEpr-pEue8rB1ZApd6kG_75hv2ueNzsxZcR2zV13ReE100aaZ0jjr3HUQ8Ru39oqW1315-E90qeGTJWLsU1qxkLfA1EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب کامبکی
عجب دقیقه‌ای
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97525" target="_blank">📅 02:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97524">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عجب کامبک تمیزی زدن
یکی از بازیای قشنگ جام بود واقعا</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97524" target="_blank">📅 02:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97523">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بالاخرههههههه زدننننننننننن کامبکوووووووووو</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97523" target="_blank">📅 02:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97522">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کامبک تکمیل شد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97522" target="_blank">📅 02:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97519">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گلللللللل</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97519" target="_blank">📅 02:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97518">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97518" target="_blank">📅 02:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97517">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">لوکاکو رفته پشت توپ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97517" target="_blank">📅 02:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97516">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW1jEogXAry31OUfCfreAytvErAv6LvRDKrDmqsVYJ1zYeWNV1fUtkoRf6NufkoAEwOyYlZviDTjHR0OHQSJFXEaagHmpl7phDi5w8GxCeS1eBuzMOz2lgHrczOxd02A70atDYSfYFwk2zxNHD4xLJkQC7TlltXdUYK0Gw5rinx8opJnzt0dVS9hnbI3GbbFcy7UCFLuWGkaIVSzswURlV3MPNkpMJ5VFePKDwax3QcAv4i_S7Pp6mnAHY76zHJqSC91YU3goPNYDRCRn0_JNj78seyCm6Bb9XiNzH3vaYHVvl5Nv6wHDoOnGRb580-LRsfZlkRh7jFwi1usNLm8fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کااااریههههه ناموساااا
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97516" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97515">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خوابیده رو نقطه پنالتی بازیکن سنگال
😂
😂
😂</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97515" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97514">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دارن کرم میریزن تمرکز بازیکن بلژیک برینه</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97514" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97513">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دعوا شد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97513" target="_blank">📅 02:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97512">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سنگال دعوا راه انداختتتتتت</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97512" target="_blank">📅 02:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97511">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پنالتی احتمالی برای بلژیک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97511" target="_blank">📅 02:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97510">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سناریو فینال جام ملت‌های آفریقا برای سنگال اما اینبار تخمشو ندارن تیمو بکشن بیرون</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/97510" target="_blank">📅 02:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97508">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چه دقیقه ایهههه</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97508" target="_blank">📅 02:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97506">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia03JEZkqplcaroukoVTpmiBi7LwQkPpII__Nq800d6zqts38QSsi5wfrTYExphBzLtSu_Y7QIMDfMrazwO6QJ7AXVToWK5svNO19khDW3js0VUI4Whb4RLxY0zY_oyJKM4nB4Q7iBFKl3mlO5X6u3GGWKAKNdES4W7FQMsmQN2AEDXs-hwkdeSBPXIy75YUl0xgAEHQJYXtAMWrQ7XiTlFyzU45qZmNJ78Pmdbql8CC1bRhHDjEPs22Ie87sEzJW_EzakImM7GKlvaAkcDb2NbDEBuhzkTb5rZUbJZ4SuZTBGPjNtTyWWO-3EiQ7VdQOBDsNKRZBLbNnsVaxmqybg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
پنالتی احتمالی برای بلژیک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97506" target="_blank">📅 02:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97505">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اوه اوه بلژیک زد تیرک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97505" target="_blank">📅 02:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97503">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JYJxmUQ9PWW7vCwqnwyuPBjf5zGHsNXHFkF8mk4hqDowP6UC1df37vWdZb3dHNOW7IquamU2hDBjIFwTXrYaxXZLmX66_RJk5xsZiXGQdkzDpAZ37ukvFjNRmATRthbmObualoM6db5-dF6pyomp-YI7MUWAMbX6ytLeq8O1EFVfxv5h87pmxq-Quh7b32IxKp8cgxpxcMJdGe5I3LMhZnbEHcwTSTFdGhG7NC-SFFUx-rFadiGoCCE8J2tPmKcmstCJapmYgB_qdt_Ynu6XW278XboHeGB1YXg_EavQRBPq1QtYeStjJ6nJ1uzTbRZjIVRS-oGhyMOQULZTriIICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SeUU6A3v7mWSmdXvs1YIiBnDPnFXJA4HlCozR0iXeihdFDmMOnThP1jvje-wuuJYNbOLPbSJnBejh1-QW-b4nnbYTG3Es3Dh37k2vBua7sq6wnkZcgOGA8ifr3K8IJ40d-PX6ak53txXD6TfsK6pEDC9Y5NK9P7rAi9iMHn7epdqTSA_dkFfAAXh3uurLYLg_k1oM5T_VSLjP_j7zT9O0Jg0oXik6rvWQnQLliTmIslA9BzlHqx5ZzuMzNlogmwYyUVdDxEDh3eweKfjYib1m1YrL22X-Vl58bOtsdkiNtuJykeaY_IfISqcKf-6m3S-xtnTTFabn4hFYNbpSQm1CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اوه اوه اینجارو  تروسارد و تیلمانس نزدیک بود وسط زمین کون هم بذارن که لوکاکو و بقیه جداشون کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/97503" target="_blank">📅 02:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97502">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/digBhNazT0p8eG3UzWMIthWAJ0JbqCVU66owM5NuCx5DBP6l-JR0NYj9o36z4hYKMAyNtci0CxXfvoPS5vFx8WVesspa-n8ZIJ7-YDwcU8pBBw_K7DJgN4vNWa8kul2Fxt5W1CT8GeMjzWppZXlbySMrYWHkE_IJDcZBomGQvBbrWrYX3CjMPFBoa5vlCXtixmU_6r7-heYzPADckyvYoKHn88Bwpa-mq_7y45vzdDnPQLM9xdv-OJorcrcdXq8on1ilFTkxAwfCIMpufjd_UzEVVA7ROyKTIzi9Z6Vig20zEuWwdhgNGJR4Hn_pnRxPINMFMv7Du167ha38zhajWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
لامین‌یامال: به کوکوریا گفتم که اولین الکلاسیکو که جلوم بازی می‌کنی جوری میخورمت که تو بازی‌های بعدیش خودت به مورینیو بگی بذارتم نیمکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97502" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97501">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0badec474.mp4?token=IDZnP_c3f24f3sXcsJm57uMuguVPcxWF1l1RZYmU9JGgxmpDsHujVO5gu37mEo6JDUnl5iOy2AatyjnpgXIE6Mn1o5MTuq0RxIfv70xiY5Kb6Ogxck2CutQeJNav-40fHSFHz92ScVl4v4GArA6GoC2bdip6QNuSxF6i3iNuNglarGVtNjJIcMHPVWPSXnmpiGs8LkMwqjAszQWALFcudvEL7Ij8EzyuF8xWBX8VR_JaLSw--45ns8FkoRWQITqs3rsTOHWiJHp5RyuWmehoH9HEI6DPiK6-SSnAS66JHt4lVc8AZowG0UAEoSjG5kQ9txDE0Upv-5ClM2-ktgofnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0badec474.mp4?token=IDZnP_c3f24f3sXcsJm57uMuguVPcxWF1l1RZYmU9JGgxmpDsHujVO5gu37mEo6JDUnl5iOy2AatyjnpgXIE6Mn1o5MTuq0RxIfv70xiY5Kb6Ogxck2CutQeJNav-40fHSFHz92ScVl4v4GArA6GoC2bdip6QNuSxF6i3iNuNglarGVtNjJIcMHPVWPSXnmpiGs8LkMwqjAszQWALFcudvEL7Ij8EzyuF8xWBX8VR_JaLSw--45ns8FkoRWQITqs3rsTOHWiJHp5RyuWmehoH9HEI6DPiK6-SSnAS66JHt4lVc8AZowG0UAEoSjG5kQ9txDE0Upv-5ClM2-ktgofnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
هوادار پاراگوئه و سگش‌ موقع پنالتی های بازی با آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97501" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97500">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97500" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97499">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QSVRTTl-GPLyJbLJkBXLyU29f5ap-9h5RD2IMaivFdSIhl3b2HQSJS2FN-wvIhEdG2oR00eWVxPHHvF8QfNxDh0hRXktYhEmhFz8Y_kamL6CWbxarkermJHVWZSiUphwe31852frf5cKZk4Pt3GBunTWxcnlXjEVprK-IHsvnBBekD1uzVJ9jZGGjmLQNeznPHTg6dHpEo83ZSaO8CaQ3wzpaeKxOT0nhqEH2CR6J-oHUvbtYWQWdmcWXfC-0UFiYmO3lkVB1rDK5STmet0MA3-ZOs5e2RgraL0OkYNuePddGm-EQloMEZS1pFN1ZFDK5XtCBboQWny-T9cBHhbMAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/97499" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97498">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نیمه‌دوم وقت اضافه آغاز شد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/97498" target="_blank">📅 01:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97497">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2410738935.mp4?token=aOMDjRwHTM_aEpJcMMyEXj-2PQg8JI-brW8fOmXq2QKHpnyMprspfpVY1rRED7vNqr0BIk3559LoRSEEkeh2HXiMgJVDgfqERPHuCDJ4Y4BxtQj8U5OSDZsJSkkID1_F1x_OJ9THnhcL6eTia2dsiMOWhEYsKJOI3nX3t4HImpHSOHnnBZCmekbMzDPm4foPmMBeDoWdckwTMrBWDACO1KVanGE-hlYA-hm-J_5g06tKUUebsEzEa37LPguHbwZFMekfLF0ulghW8Ebr5jfb53zCyUbxjYzWZ0N-qErvz2axflzgSCs-M3MeWtEFnD3CqjqHLcnA6Lay8ik89ARxsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2410738935.mp4?token=aOMDjRwHTM_aEpJcMMyEXj-2PQg8JI-brW8fOmXq2QKHpnyMprspfpVY1rRED7vNqr0BIk3559LoRSEEkeh2HXiMgJVDgfqERPHuCDJ4Y4BxtQj8U5OSDZsJSkkID1_F1x_OJ9THnhcL6eTia2dsiMOWhEYsKJOI3nX3t4HImpHSOHnnBZCmekbMzDPm4foPmMBeDoWdckwTMrBWDACO1KVanGE-hlYA-hm-J_5g06tKUUebsEzEa37LPguHbwZFMekfLF0ulghW8Ebr5jfb53zCyUbxjYzWZ0N-qErvz2axflzgSCs-M3MeWtEFnD3CqjqHLcnA6Lay8ik89ARxsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤪
اشتباه نکنید اینجا اروپا نیست. اینجا یزد خودمونه که ملت از گرما اینجوری رد دادن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97497" target="_blank">📅 01:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97496">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بازی رفت وقت اضافه</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97496" target="_blank">📅 01:30 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
