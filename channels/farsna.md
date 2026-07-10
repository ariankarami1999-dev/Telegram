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
<img src="https://cdn4.telesco.pe/file/l_rNjXhrYZbu5XOE3gIhsPhAWeNltRfwC4ZOsisHc6xyeJchykqrEq0RoMpTEmoizxaDx1CQ-_u3nVtlMssVInApA5HAnWeoK0fQHGtJstIowpZdbbPtGnhfWg3ahC6ISF2045S0ZKvMIqA30qZXXbZLhfkZprxaJCWiV8di6Bi9dBkkEHbg2xFACtbWvJZi_K1L7gGAoj1mtBvvnpHFqVJjvzOuw5gAI6ZyBufZjNo-SJIWsFU2RBeL3v5D4kD1URonARqWARbxy_Kxs1BKM7YHkAIvnHHsyfMGDe2IR6jPZqnvE9lFOA7HB1INXm46HZIg4H2Zfu7WtMieah9l5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 10:29:07</div>
<hr>

<div class="tg-post" id="msg-448922">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRZcUthf58vBCuBEGACdwdyTh72Jazm7XVtQM5EN-V8sii_OB1OwtCOp_-qkba7_HpWBjxD173LLgwL-_ahXYWcS77awWBpnl5qFQPZcbgmP-pcW1ZFn_pjC32ZFUBwp2ehcS4R_MCkRU2DdGcWF89-ahlILqfvENit7bu-9lqU_9otSOLcdZdC3qm-pMS_RfHRA6g6Zot9BJ6Q75Gucn1p6m7M0LKnaVc1vVe5E89GNhKsVVUtlKkUub4V3_cyOjNruE9J1xgwcDkuOyQiS4gLuAShvYadmshzb7MGR4AufgN6YSXXxpUp68lROeZQovB4vDEkCcP28574bzSIrdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر پاکستان: گروه‌های تروریستی از افغانستان وارد پاکستان می‌شوند
🔹
هند به این تروریست‌ها پول و سلاح می‌دهد. برخی دست‌های خارجی دیگر نیز وجود دارد که نمی‌خواهم درباره آن‌ها بیشتر صحبت کنم.
@Farsna
- ‌
Link</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/farsna/448922" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448921">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/574b047b5e.mp4?token=P1dIjEtaRpvXvdkDwlBLY-dznTQAl8hAMV9MbD3qMzQbhIJgqA-W8wq2pz1TmvS1Dnq64Erybs3AyHM3Y61h7qL4n5I5KT2uqB0eab4bgO8ULu9cbz-zcNyg_irLBn9otmdcnE8sb_6DqVIaHBx0hBGZkKm14Qln3DNIEVtWKmt9EKNpa7j-LToSR6vJdUh0RNhw4vFEU21f4fczuv_uJ9lQ9-2iZqoviYvb13NtleDJOTnnClc1B44LB52fnJlquvlCP4nlkFs9vMo6IRLRlOIiC1G3KKKJ6I4foOTiVg90AvGPF7CeKMXoTmSXJDd4mDI3y90f5SnyA9JwWJZq6XIepK7-NaAyAbSAJRlcoB4l2WaAqpHfFlKs4NpfDAelj5Hq-wm5O3IIn6gdZpFJAKANBgO2WfdLJwBoL4wVutRsrcs1NvSoIAXi4VkmB9fxSEtvq5jRDzVrabGOEFAS_Pn_vyoDazt0wSRihaYJ_7yfkGVbEmsEN6fxehorufnBz7Wljp5SWpc0SjWzE6hXquc5_95Olhbrkg7f-xDqEneSEQZugrXRMM1nRIZ7qIPHRB9peAghUWEqZCH-VJzu2giTyMgk5VFN7cQvXE4vAww3S1m7fKf1v33FDzqgFPSOCBXPu47q1QIypF0SvPQjfCRcqONhsBywCDCbcbizGNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/574b047b5e.mp4?token=P1dIjEtaRpvXvdkDwlBLY-dznTQAl8hAMV9MbD3qMzQbhIJgqA-W8wq2pz1TmvS1Dnq64Erybs3AyHM3Y61h7qL4n5I5KT2uqB0eab4bgO8ULu9cbz-zcNyg_irLBn9otmdcnE8sb_6DqVIaHBx0hBGZkKm14Qln3DNIEVtWKmt9EKNpa7j-LToSR6vJdUh0RNhw4vFEU21f4fczuv_uJ9lQ9-2iZqoviYvb13NtleDJOTnnClc1B44LB52fnJlquvlCP4nlkFs9vMo6IRLRlOIiC1G3KKKJ6I4foOTiVg90AvGPF7CeKMXoTmSXJDd4mDI3y90f5SnyA9JwWJZq6XIepK7-NaAyAbSAJRlcoB4l2WaAqpHfFlKs4NpfDAelj5Hq-wm5O3IIn6gdZpFJAKANBgO2WfdLJwBoL4wVutRsrcs1NvSoIAXi4VkmB9fxSEtvq5jRDzVrabGOEFAS_Pn_vyoDazt0wSRihaYJ_7yfkGVbEmsEN6fxehorufnBz7Wljp5SWpc0SjWzE6hXquc5_95Olhbrkg7f-xDqEneSEQZugrXRMM1nRIZ7qIPHRB9peAghUWEqZCH-VJzu2giTyMgk5VFN7cQvXE4vAww3S1m7fKf1v33FDzqgFPSOCBXPu47q1QIypF0SvPQjfCRcqONhsBywCDCbcbizGNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با حمایت نظامیان رژیم اشغالگر، شهرک‌نشینان صهیونیست به زنان در در جنوب الخلیل در کرانه باختری حمله کردند.
@Farsna</div>
<div class="tg-footer">👁️ 697 · <a href="https://t.me/farsna/448921" target="_blank">📅 10:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448920">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dI7dGI2YFdOuyGZLeoH2gdduISs3G4GUS05gMfXszA2vGhU1Il1gXwDPWot_lKIB5kjHZd2ZfLTkXFEoQND5RJtk6LS0zr6ge_1u4V99eqwF-IiCiSIUun-WSOQtIHuW7TMwuFPYB6SAAg25cVr5Xj2zg1NCYKvvcVktjQHMf2VdqHIqNlIWUAvDRrfj87DX7rVsn_250fMkD9fiPzqycsY-cQF-0kUN6rpeDzjvaKlGxVoOiqOXzv4Ns_buuUAF7ntqXwJBhAHkFOnybRJyMRerM_3DkR6BTcFywqYPqe1dK1dVC5fPGcvnRetfJtzldtmVmFMC_pPdOoCnjuBVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختران ملی پوش ایران قهرمان آفریقا را شکست دادند
تیم‌ملی والیبال نشسته بانوان در نخستین روز از رقابت‌های قهرمانی جهان، در اولین دیدار خود به مصاف تیم روآندا قهرمان آفریقا رفت و در ست‌های اول، دوم و سوم با نتیجه ۲۵ بر ۱۱ برابر قهرمان آفریقا پیروز شد.
@Sportfars</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/farsna/448920" target="_blank">📅 10:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448910">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZUVCFibP8mdHUcBpV02XqerJXWlEYXKbQbG-XiJbc5-Bb8N81im76LRqcBiu5GT5gL1Ng9UcyBh0P5Eg9FT7uWG_jDhkn0ZdU2hMDH6qUFKATINA9zKBiERJJQuCFzyi5uXfBxKd3XN60K7EMc0_oz-1Qx9P6eRzpf8gG42vnlSatymLNk4xHU4VWJ7edKwf4-A5QWIhS7x9ojy_9QBxkO02R0AKEuTp9a1YvkIKUesU5CYAowiRTd7_AN6AViSHKCqowsoGPap9awuMSwDtPo7AqIO4OGT3dmth0JRqxZdgHdX_PS4nDGVrnj1wVu0P5NaSB6bUV4-HTHP0lngxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GSTm1y00ACkFyhrxhKuxP-hmDCTqazBe6d5S-tuzapWIA0beHTB8d6BUSckbQx0rlr0-J7a8qLl__oF98lBJGESHicrM8-eadzQQSTjgzPN3szJUDG9rfVVNzDz6BSDgdlN9hQMNpijXlvx5LhfAJI6CGq6w9pe7Ez5wk97v7NFKHAF3T6uMNioQxSMTOEK8ZKwNzfnyeiVPIDt2TclFYk3F-nKgpCgnq7V0kzc0hgalbxplVM29hjcvCE4Gmd_7WVkwG08IDmWFOL13g78JrWsEzOLJGuw9blYTqvbz_2ZbJIkbA-0BgopMmwrYJkCG72eEuYCMQctaSpttuCaBww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_7X4yymGvHwppyP7-sTkaeObh1t3q0BzLhvmDipkwA9YyxNUzneFhX2c22lYR2SZAUJkdhnCn5Mcfp6XF4X0lvdhHeCWgj-sIt3bnzu9dIuSRrZz7OQirNMVJjrOoKyJD0_XKx3tSKaj1ejKxvKObbBnETi82Q6aIxluDPMkzcJ3TbIWNW0kCuz9sv1zi79WvTXQSlNBOlbrfs8ZJbJyL4vbkslU0AbYdbQFwuiWjxkUhYOw8cOZvOs82BMqhK1EkT3pvldsbYa8Sfjng3UuAJNHkSKF5TAr-ei49hLH-fVCkd6boejgqcytwRbycenAedGZXdx6Jo3KMgaqA3KBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7LNrvVr_FHL4hwGDw7a0GSTYF6TdSJNCxGyKhtfAY8SSr3ludfCQh4cCECxJpNtBt-5qqgwIFwBKFuK_R2aOY0tsBTKiouGaa7wNiwARlf4-kW-uDGcPJlLN4XZ2Eks_cvPJwNDztFLphjvB3MoA_eO7rRY0dYvEmDt2TwJmNZcW3agNJXOswK7Q7QAKTUxm7KPAwrW6XbYMLAiac3Gs9iBvwvGp9rDNQNmIP3sD23DBasaP5am10ee9bZrNoUaZgHjR9XqIJ9vKREJ0-uk0wRES5mqJkYnFHBVeO690sTJzdPR09DTmNjDu_BPfziyJiy-A818XVh46roGEnVxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8Zrcgh8eSwxVH8-buQPUHX7z8NJ_fVQ_ULfJNww_NObgrqUoU8J1e6A214hf2W3FP4WaTVZrzjgucfXMI1MRXRdIY-kcxEl4YriwK7K1hHQktWwQtIl2fy1AawWPtRz-qyQzAvTbOx3TiGtBvMTsk-sBRPN0n43TlnUpZX3enyT0_NSEfnIFdNrVxxLAfLZG_FKFJP0oYTIjxUaGs2lj9mEDVq1FQa-TCVc9Xmj7AEGR3HtSTMJrkVGxexerExFLbASiMtaP4fMOnnwZPry7XxxFEpVkzPuotjhqG_f-h6eRpef9j0zH7nfewOY0iC9_vH-kMs4Y2jtK3U04AkOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/paSrHQZpbJZqMMPYhqnHxGx4cLrJKqwyLO_G__lpUfm0zBmiuBmjUgN38LxGUquTNNTUogQaXqHuuokejFU5YGzaltLlb_qVNPgKiHgGoRsIw_j8ycU3Yn8lQr0Vp-KDbEU_7Y8cDnpYKPjYArjfHuF0JJRMLAnfc38L1FTcLeOzBpQe2EsYSSvYI846_J2Ej3VnoS-An6Sav0ZAY-O2xv2vVqAkoSZd9PtjQ9WLJpgR7mP3ndHG2JInz3kPkgtPoW-aoODfsizYI96zwrpwhx5wowWJAgYQtTSmDdin6mcLyUxZ721Ehc049NZ79stdDi80xWmnRx0A2bSmOxOFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ln91VBCHpycL8k07GnIyVCSiwbniP4WFDIvNQQYd9zmrKMJE57EdqrR98caJkI4YOhHV1TuN7Q6ROWQYNYMBQ4OqplvI144sqdqYphmqv2t3iJArY64255oOswbSmvbgYMBAVhFl_vNUsr6obkGqaRWmp1wgq4CtAh0BiF9f0stu-0y5Y_34TZqXwkOjM45rYghgvwNmyk2F9-xeB7jT2HLKHRPAl67Z6NqSu1H65tu6ZxM_L6hewsCMJjVcskHcglUnBwAf0PbeNKgGzc5A4VJ3quFAk074bchMUb72fH0xiBkhX-Uk6JUP17xzLZL5Hw5nIx7iO-2F-rKyVZlujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kHxMaUkeYe9D05dkm8YVAYfXZuhATrtb93k2HeA41lQ3_EAdyKAGEjAko0kStU5kV0KPaKV8HwK9AFedibfkLs7QLd3LapJphF_B90MWWQRv6t2xtv2x_Fst7YVVPNRmN1C3eUnXSXfyWMM8FvRAMkLwH1fS5qgKxrajuljAmRR9O_xQfvv72ikgG_n4KjTTkgyKrg93QYDXITkzIKlJ3gAPmA83uMuwlc4TO0TshmnbMXdnd5ZxZBuf5ndDjvQYeYjumAEuAINDwotpQy64qcBSCZAS8dGiUpHTYaPibW37ygQSEFAytvWiwNWF8rb4fygGSuFO8mVvCfaJIjYF5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLmtbMBJDE_7uMiwi2Rg9zXhFIMlOJjODqt4UkWDihwlzVbxA4OrDgrGcS6kueS-CEfwJiDShTDvgzj2LrNS2W7vEsw7vFV5l7pPOw_NFFMeq6KAku8LshjtGzHXfxUBVo2ZnmEul3lTkiZGwXsMbg2q7ZRxLk4_AnVlzL2dbPFJlRouVc8y4TFR54ycSDvQwzxvrLMLE7jyRUe08_0AY8GcQv3VmxU4l-q7k9bsbzOx5zjtehedCqY8UN5eoRvzRPNHZHQxsXn_5W2DqIzYhPvYaeTpGQQfcjgvEqTNKj4-KMIqrfTbp7IvQWT0WZMGUr4zX4yZcu6FOQdBKLGR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VNxBAttFkHz259NkOTXvMcCzG6xGTW_5m8V-zb7QR6PLRaKqcP_TFxMmQ1jThqQbZSSc9vOBD5d16LOEkW2M-hDfdjlAwWokboW2nyhFotGNhvQavlNYDLnxdPr-eoYH5kf8ze0NRQ8cEr_7D2aVw6sn_Ws3U5dc2Ks4D_U6vDF04SbFXvcq-_3PfYddJVpu8KM1Awqf09oRy_eCy25hfMIVnRnlOd9NVj3DrJ4usGBxEMb8Y30gIs69dp1K25bAPCdjxFiDZEfx28qkyLjBqsVNnO-yZOQJ0BYWfe-lwS0qGIkyA5eTPAjPkFxj-D3L_HQL3OLNA8crFfdGuvtm3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از تشییع تاریخی رهبر شهید انقلاب در مشهد
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/farsna/448910" target="_blank">📅 10:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448909">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آموزش‌وپرورش: زمان‌بندی امتحانات نهایی تغییر نمی‌کند
🔹
رئیس روابط‌عمومی آموزش‌و‌پرورش: هیچ‌گونه تعویق یا تغییری در زمان‌بندی امتحانات نهایی وجود ندارد و آزمون‌ها مطابق برنامه ابلاغی، از ۲۱ تیرماه آغاز خواهد شد.
🔹
تنها امتحان درس «دین و زندگی» پایه یازدهم که قرار بود ۲۰ تیر برگزار شود، به‌دلیل برگزاری آیین تشییع و تدفین امام شهید ایران، به ۵ مرداد موکول شده است.
🔹
دانش‌آموزان می‌توانند کارت ورود به جلسه خود را از طریق سامانه‌های
my.medu.ir
و
my.sanjesh.org
دریافت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/448909" target="_blank">📅 09:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448908">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIhYMwoKaeJ9VgSHSBCFENEmrzwCajKWNtnCCjJ8NWCheOzsFoWizfKcTW7caBxBbFJujdPPhz3-gB84qVU2EhCsOkiJE8jlEqIjUYqbI5BmZTURYMnaNXgXNGpVOCL1TPW0CKFWR4B_GL2vV-PtnCM8a-WnhvWaX83KnCB9v-lhW7vJd6nSqMZVLMdNA5Fg2d4Jwq1w1svcJXeo5RCssnb-4CWcFZijTbDSz5awawIStuPuEEoHS3WpZ2Vd5mIngOk21sXDH80qivdMxCxDk1V0XLOxcCY2f7707ZgDCBePbGRbds-q415WokV2h8_nDLVQ68xP6Fgu1Iz9ZKgNFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادهٔ روزهای داغ باشید
🔹
هواشناسی: از جمعه ۱۹ تیر تا پنجشنبه ۲۵ تیر ۱۴۰۵، با استقرار الگوی تابستانه، افزایش دما و تداوم هوای گرم در بخش‌های گسترده‌ای از کشور پیش‌بینی می‌شود.
کدام استان‌ها تحت تاثیرند؟
🔸
سمنان، تهران، قم، مرکزی، یزد، البرز، قزوین، لرستان، زنجان، همدان، کرمانشاه، فارس، اصفهان
🔸
کردستان، آذربایجان‌شرقی، آذربایجان‌غربی، بوشهر، خوزستان، هرمزگان، خراسان‌شمالی، خراسان‌رضوی، خراسان‌جنوبی، ایلام و سیستان‌وبلوچستان.
این افزایش دما چه خطراتی دارد؟
🔹
افزایش مصرف برق و سایر حامل‌های انرژی
🔹
احتمال گرمازدگی، به‌ویژه برای سالمندان، کودکان و بیماران
🔹
افزایش خطر آتش‌سوزی در مراتع و جنگل‌ها
🔹
احتمال آسیب به محصولات کشاورزی
🔹
تنش دمایی در سالن‌های پرورش دام و طیور
چه باید کرد؟
🔸
در مصرف برق و آب صرفه‌جویی کنید.
🔸
گروه‌های حساس از حضور در فضای باز، به‌ویژه در ساعات گرم روز، خودداری کنند.
🔸
از روشن‌کردن آتش در طبیعت پرهیز شود.
🔸
دما و رطوبت سالن‌های پرورشی به‌طور مستمر کنترل و برق اضطراری آماده بهره‌برداری باشد.
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/448908" target="_blank">📅 09:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448907">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjLmiuLgMn-HvEcOjqxoJMa5cpDDD0hubbzWwuCLw7d8SvM_wJXB5LwwLMx23A9iJF_6rJ_VmDMfZGF7xqxJD0Bg0DbPjcxyG8BMyWtx5RzessbqEbwvFvvzfnFZtW8Vw1J5Frtb2YPocLBHfCvP9PHC0ZuMXZ1FG1t1Kgjg-yVYoPwh_CJyONpQ2sNjlHNe58ogZBlCi2_cCoGQjuPiyVSc_X0S4I-nfU6D-llIq3B8QfLbsc9GvVaRTWtk-glAusGVaU2I2vAWL0kGmCrSC8bWmms279svedTpzlwb0KjYyp6mp-ZoH8ihDo0WHMlHZElIiFY1VS3dyuF5iHRHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باتری هسته‌ای با عمر هزاران سال ساخته شد
🔹
پژوهشگران چینی از نسل جدید یک باتری هسته‌ای رونمایی کردند که به‌دلیل استفاده از ایزوتوپ کربن-۱۴، از نظر تئوری می‌تواند هزاران سال برق تولید کند.
🔹
ابعاد این باتری تنها ۱۶.۸ سانتی‌متر مکعب است و با فناوری «بتاولتائیک» مستقیماً انرژی ذرات بتا را به برق تبدیل می‌کند؛ روشی که عملکردی شبیه پنل خورشیدی دارد، اما به‌جای نور از تابش هسته‌ای استفاده می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/448907" target="_blank">📅 09:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448906">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlVsksP_WMSXz5qwruvWOAmP-4mEUonbHP3sULCfQ2EhKlyp8oW2Eahy6JTSyFylfZ2DXrrbLcL2HP1f_Kr1ZPx3k4met7YFv7LZS-0FYnnzFDfacfA85EKEV3hJ47Z6UFmONWXzXzQk2g1Hfxmyvs7qLPqZmzPr5-IJ_NdgO7ox-iJHeF7s5QFgjvm9z-wrSuEhoitmx7EQQMkb_J4f4SLGvC4tMpiZH4UhDu90k_fUqAIt5U3cHlFUcdgwBF1B590z1ujbT10BzhQ0Ixdu9cMkXeqL4ZTYQYZcI1HmfiWPRsdC7BjEKFyQfJpw8o-C3XLTDU1HahUVjXa24sOCMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست جدید آلمان برای اخراج مهاجران افغان
🔹
دولت آلمان برای نخستین‌بار در حال آماده‌سازی اخراج شماری از پناهجویان افغانستان است که نه پیشینۀ کیفری دارند و نه از نظر امنیتی تهدید به‌شمار می‌روند.
🔹
وزیر کشور آلمان می‌گوید که اخیراً به توافقی با طالبان برای اخراج مهاجران دست یافته، و در مقابل با ورود شمار بیشتری از دیپلمات‌های طالبان به آلمان موافقت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448906" target="_blank">📅 08:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448905">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebQKW8sWtAbuFrt7OT4yb05_8guEYaVr2czLw35VMZUa-jRv7VXiFyarWI1rCchkBZCD3mU6Wyckzl5dnVTv_zL22Ploi9VvTtr8-g0fH8jOF3RWWjqApE6q39Kak8eYUh8BD_Sq-BBnhUV7TJgixjgeJHox-93HgvpqQR1fWrR_ooeOxLzkjN0xIuNXRJudBVI-tBLpilFrbWrp56SI9thF8HODF1pkWLcP1E6msRrjeSAaPQy-rybLpDpajEOv1cKYngRET2aMws0hZaYZOmiWNw_I17bsWitKj2Xe8MvlAJGHcex8vDeVNC6RBji2FNLbJw_VXHInw2BhMYmL8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی گسترده در اسپانیا
🔹
منابع خبری از کشته‌شدن دست‌کم ۱۲ نفر براثر آتش‌سوزی جنگلی در آلمریا در جنوب اسپانیا گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/448905" target="_blank">📅 07:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448904">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0K-tcK9r_x6CXbjFlFvZrW6m5hPvH76NobRvNc4WxlJDxBweyH7FxAus16U4iKg_m4QYtkTJHv8cbY7yw12ecDSJr_wdvsQKQJtOBnG4Fv5vGILw3Jzxy6fSyPiJOpA8nL3N-yD7OzwEKyeEsxrj26iCsW_s6Tn3VSLUb7GOiNmqF3wSILuubpc5MwiKUbG5Na30Wq66BpLTB3j1fi3zzZZJBlaxE4QyUrHGBbkH8ps7Tv0UbWJtr_iLc-MCwG7Fk9AA6FUkjpGxz-6bq2T8SFQp0ruCuaEf7uCjFZA391C9GjT-8ZpFOwIWrRsfRQkdNrfj9XiNKmcvCARIxsdRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردپای عربستان، امارات و قطر در حملات اخیر به زیرساخت‌های ایران
🔹
داده‌های وبسایت‌های اوسینت و مراکز هوانوردی از حمایت‌های متعدد جنگنده‌های آمریکایی توسط پایگاه‌هایی در کشورهای امارات، قطر و عربستان خبر می‌دهند.
🔹
برخی منابع خبری  مدعی شدند سوخت‌رسان‌های اماراتی…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/448904" target="_blank">📅 06:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448903">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLZiqUk_2CSYe3e-YglyC7UWbzxWSEsyO99rx7tQPG3EjveLW2JJt714WpZi4W7VV_k9TZEs8C08NQge4lOi7vLi43iLmlEJwedA20aw0GUc5h_gD4Ib1epmhqbYs-mWO79Y5b8iiS8s2YQW8f4nkxwsHt_pUu2wtaZ4zp75fdwvtxqRWpH1SAhJM629FGyuLSWpl_Nz2jIqd9Au4NQhh77zxV70_5sY9X8NzekTAriqJZVeXlEe6-RfIHguowBuBGYs0ZsiTjeM56urS2KCfv493Jvd7z-DV1-DHeUzE-zHc59Bs2iE2_mL63ulhDyZ4EZ9yJvh3UdrrsM62EyCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور رئیس کرۀشمالی برای تقویت برنامۀ هسته‌ای
🔹
رسانه‌های کره شمالی گزارش دادند که دولت این کشور تصمیم گرفته نیروگاه‌های هسته‌ای خود را از نظر «کمی و کیفی» تقویت کند.
🔹
این تصمیم در پی دستور کیم‌جونگ اون رئیس کرۀ شمالی، برای مدرن‌سازی ارتش این کشور صورت گرفته است.
🔹
کیم‌جونگ اون تاکید کرده است که امنیت کرۀ شمالی و صلح واقعی تنها از طریق ساختن یک ارتش قدرتمند که توانایی مهار و کنترل تمامی تهدیدها را داشته باشد، تضمین خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/448903" target="_blank">📅 05:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448902">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
با آقای شهید وداع نمی‌کنم
@Farspolitics</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/448902" target="_blank">📅 05:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448896">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WI4re2g29qHhsvb7x0-wm5cd6Iv5H7b-uOr3IoX8aY4YSiz-YCWtYYzklmntgs5BXg7SGhYgCQP5Z1mJDsBzEW9X3qU5Dn8W4rPS_3beMqu3EVEEBpunKRPZox_kc-WcmbbJO_Gsioc3Q9BLuKAEUW0uBXpx8TqMwvcpzO6BIJHzSp_BjvxuS9zEbd4qHEteVSc-KwObAO8BpcCSL1NtWV60F6vqoQr2JSoVSaXh5HfWi1_NRF79-IWy1gJGVOho6HgZjBZzaLy85RKaniWFZyKnmkNuDBwzP-kWq8TcLYV9l27zU9Zvh5oQ97NKRqx9ff9Mf1CVybP4otOVQSvCRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjGpzyftTnc-CdR1CwTZLsFXwtx36e63RrUQJ6guxKoV2pgfHnsI33O4vspo5zTZcDDFHOoDL21OiTQIcUGx6PSfXiJo6iNgfsKud0zjCgJuwKtrlx2QDmHC7KwkvpcEuwPpw13XSzmzc_WA3XVEWP4hkGNlvUWpe9iSSv6AXvY1k63Aa_M2S1KNgT-TAbj4IvMGtQjJYfHo7DthGLYkZ3CYbNh9gzaPK6TozYR8_xlmReAgf7Epvhd3o5jq9ENH8kU257b45y_azLO-ZHYuQlujwMQ540K_peJWqnkUhKo2sxxmvbpMroMB0PFvkRUTz4BxQozjnvo73BrurthpjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rO6S-ZcvfOK6g-9znbb7_WtCgaeF2z8Tr0DMfOnbOEuhcwQs04f9X8kY6WlDbVxcp6srUGYmphvXURIsSH0FuDbSxOpfZDuYS4eClclaqC61N7JLpZJraldIh1sNrkfmuteAX0IZOHJtfYopvRccZJkWcIaFv-9VqI7tdL8HBPpGVttIPbmP7KALp8Z7qnKBS8jZWge-IIuaC426MDiLdpd4OU4vRCsv2_HCZ7oNzNUMVYrjPxSQCXqZ1GdbHXXI7PSUfnYW5b9R22QkEdOIQf4UYDKYIeYnMX2YWm_DQ0raW55VGALI6apivmQyI8BK4rV6HIYsqVswheUqC71EGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VOhXdJ1k88qz51-JulRLQ5NPZWEXyElhKOBRLNQjosrS0AHFS0bAP7wo0egphcHKa-9IurzpP1eEsazhrtQi-nxv59JK5H0ExQBe2Um_xZHrF-9IKPDiyJvJ-nHX5Q7UUVJpwQ4tY3OxyAmDVvxRCE439UuAsIkYlxMrCB30_J4ixSs6t2wIcz8_0PmSWE8dklhFx-BQHsMCtEs9a6_-SDkIfDh3o2_DJUGUvzVJ5DhzDoTuPEmLrDoxRZQoTU0HA61Ka9GqLc39h7M-1mLVripDZptu_dE9Rw1qa4kC8vi0n72AwrOTHdfN8lQnVKAq0KgQP45AkvsFXn0c0buwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SshJJGK8o5oDHxnfu1TXe3csxDfbJUbnpDZVYeDqH04Jalu3rWVB7wzpbdTQhqEUdcuCkbl8mnaKh-CTQhpmo7pgtZkkKBQ3YG-ZMHFDynUCPM8Xmz2wwm2az7WxnarD6OBZywsdfYJNbTNL2hm5-3Ozk48ZsN1DLTreUwlxZVFdUxf4iJK5z8bk9UdQmyderMaNeGMNnajWfztphhy3u96H8EX47nYuu17MFwAm_ocZRsQ2MLcT830dmecrz38ybIw5DAo6EsiWc5GnmSAOJvGXUiqM_z8zpcu4MLoO41KTlZxYLIY_ZiQbjuge2QMF-XbJzGn45t78BG1iCrHGgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCL0iGQAQ_vfSyThjS08Ev611t0ptTEXIJ0EA8fiZGwjwjm-qcOSjjlXu2xUqBBAf_mSyilBBf9O5iD1H279C2d0nO2NrjBon4s8o-Vv_3DSN5CVgg5rNZ3VpMfdD_Yw_Azb5glyWytndJBiTTWyMXiKgC_lYcg4i3RMhnso0Wf8ZCZ-pfmQdhLv9zJU1KojHKxrTvdMTZpfaVWdQwReUVIE9MHweHFo1DfiTynXkCgJrByB6iQQWKGHyX9ugyiqPC2SRAWkFnXrGJ51eZ2n2x041B-eWowi5yMiBG0L35wmXrVjawM5q4lmgaANs7BqCOPY65YlCO_7RU1DUiEspg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری عشایر آذربایجان در سوگ آقای شهید ایران
عکاس:
مهدی ایمانی
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/448896" target="_blank">📅 04:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448895">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZfKB48_ubJUeFXi7rR2j48mR_el5aBU23OXCuI7LgllixNTJ4MoQHgMzYdMugrczoCIi4dklBV_sFBZ984O9dpEHEinvvEgSMvE4GzJNZQt4Wt02a4l-EVc6g0oJilMiFHAZFk90-bpB7qO-776RMzKaJYiPmahUNM6V0Owt1u7azwubjgerM91Fw7AH_5Jx0mvSAwoySpMHwzwd4EgCCSj9pSpHnx0zydOL-jZQ61Z7ZJEGVDOBbGI9z-sPG8fLyUYvHLfURFAYCGxtAVv4g7tettTGTheCvRRBn2-IeOkOo1OiqT5wI1A6maFDoVRgSyg-mH2mifxnB4tK80XTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر نتانیاهو نام خانوادگی‌اش را تغییر داد
🔹
یائیر نتانیاهو، پسر ارشد نخست‌وزیر اسرائیل نام خودش را به «یوناتان هان» تغییر داده و اسم او در نهادهای رسمی رژیم با این عنوان ثبت شده است.
🔹
این اقدام پس از موج محکومیت‌های بین‌المللی علیه جنایات و نسل‌کشی خانواده نتانیاهو صورت گرفته است.
🔹
روزنامۀ صهیونیستی هاآرتص گزارش داد که این تغییرنام از طریق اسناد سازمان امور مالیاتی اسرائیل کشف شده است؛ جایی که نام جدید در کنار شمارۀ ملی او ثبت شده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/448895" target="_blank">📅 04:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448890">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dr77jFDr5Td10GQSHZamvuR1Kc1rFy3GvG7nz9PrIFcAKRnzZ8qIV4lT4_sbpPunpa31VSQPpcOuf_iKG0GwFKaBAzd_Qthzm1KpBhxEfghzoucuCNBDzMXbdVpVpTxfvfq_qIwvzWooX5I_YgR6Cb8pTiaIHS7_FNnkJKcedbK-zj4dFeELRsTTcUtrlbSCK9obZmbOuZ1Z8JqAbmtQ2ZsKXHz3IJSV_fTAoB-VicJ7xwq8nfi3yziqS-sahFgVG0fA6lKXWxvD4xVC_CrX-gAQ1gdr4tGZ7gIpHp9nDiqQWdCmLUyUboiknkh10Y4DfBQyhhpqhNuJpDRQxyDdRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLcg7TusQ6H8IUCyGMuRWXjgyEpvQK91JFiUzUu2JSr0K-L6u8aqIH3jCs6qIAI7k1FiCaYSyVIT4IHZP3NgLl62IVcPYIt7vCYfhDdMxhul6Nx3DcNDsUfGMuI79LtJBWbV5ccZw4MdGjn7Nae8jkeeisAbWlgJLPIJVJml3Me24YyPc4XZ3qxD2KoklCTXF7JNlyfdiDqcj0H-emIYNhB0rhQlvngOAWoMV-YEBd7KbgTouyfRmdbix_K0BVv59kqmzIbxdWzV3yK4HWbBL9rOU8h1aW3RBYUYD1mViOBCPVRmhJYOvfrrnBq8i4DXUSIula5LX3IeS-sYR0eWUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPcTRvQ5KXtiOkikaXPjoS2sonsWSGOf0oWN_xm0F0ae8w6MPeXVB1SV2PtGOBaW4hrPp-_vaNgH1E-6L90rzco29dZvV5bBJp5D3RssApELlN60co89URrIcm9ZntjIg-56WGXhrZV1qrrrrw1-lFqgFyGoJIpGPb3ln4Iq-Bc6G1M1Cn3JdUyIkKQREW20w8ctlb0E8QbA7Uwhhcc4ACqCIcBETB-fAjSqckZHDtHj4r6hO-HcH8fYKmL_z-oU81kx7Jw8xF-41HMs_Tu4Xm0CnhgHnEjkMnccJhUicqw_HAe0J21DHWXK8WcbRiJD0tsVTBCgSwBKaOrO1aOP4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H8M1elHglXRtoAub8mKEX4irmX4ZN8mWu3JlHTqcnK9QjcMrlsWa3Afna0GGyryZGoXnVj1jH0QhMSZC00FrerCxrKLLfPeEJX1MvnQajH9tinNA8uSix0TZuM28g-mSOqX0OX_dIxtrbZYwL7Uh-0B2VXsNx9nwRq8HH1M9U9U6-mlipUia4SzJLzn2TKxOvAZA77QTR7_M--QpYT3EII92RTW3neqYeHfCeH9qNIGqN49a8OzJigl78PZpO79nV3tCE4gU9SNwPOg7jJjdUZlNP_9Np2-hU83C1lV60u6Ada_dXgLIYuXkZYYl5k5Td_JmLDIAj2HVw78x0AoKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1lENenM3PO4zb3oN4rlbDO9Z-Hvmmhakwvx1XHsNxQQhK5-UGz1yjU0K5Sk6NcBuyKHMbNyL2zahJGa3G-hg82RnPPbvVB7ex3359JVFJ_bc1A2DSU_tOpjNIJg2WJ_24OrWffhrpMoeSH7HOcg7uj3Bx5US-9bwKwyEEbyTSX5Om6KzGCfNjX8d9N_j4ejcplsaJXZRJr1g0tXyz6hBHt43dIYpceTyb8sHO1SHrttHF7SV-EbGrTsNxTYHHd92bHt9AriQnDgJdLNKV96NW7lOsMA1EiasROcZQcaP4ZXiNt_cbLsoLqPJNMrIsTlP197vhZQpZ7pBsIlGD8aUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دستۀ عزاداری خون‌خواهی امام شهید در زنجان
عکس:
عرفان تقی‌بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/448890" target="_blank">📅 03:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448889">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عبور از کریدور پیشنهادی آمریکا در تنگۀ هرمز به صفر رسید
🔹
بخش انگلیسی‌زبان شبکۀ خبری بی‌بی‌سی گزارش داده پس از تنش‌های اخیر میان ایران و آمریکا عبور کشتی‌ها از مسیر پیشنهادی آمریکا در جنوب تنگۀ هرمز موسوم به کریدور عمانی به صفر رسیده است.
🔹
داده‌های شرکت رصد اطلاعات دریایی «کپلر» نشان می‌دهد که در روز ۲۵ ژوئن حدود ۲۸ فروند از کریدور عمانی برای تردد استفاده کرده بودند اما این رقم از روز چهارشنبه هفتۀ جاری به صفر رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/448889" target="_blank">📅 03:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448881">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2UyVSeq1Lu2cuF0BsdM0p0iDS6yCN5EyJ4PPslcvh_ca5TUCzL0cdqH32KBj3c9wsgoOwa_PrdXV-Ofi5LN6pqsQ8urk2Pdtiiag13nI9RUd6ZlTLJT-Drx-a8dAKQ95pw1t0mI5q0RseWcBMOIGnetKMfLdWlOflOiL9YNuI6wARwaWQsFFiJOBvMddz0DleLXy6sPa4CktIgDBjzWnqdjpgOCU_iv1qJxWVKiAPb6LWpLoXNZobA6Vp0ObA4VJCW6GJQyK3ud50qdoCLofxGYqQmFR-_zoaz3kQt4RKE1ADd5sj9WgzIwAF0tcJ9EA172yQ16Q_CiIBmftjdkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzuuDGs5Ykf03JGBiIYtnfN5VHmmubbhSUQ_YJA0SGhxBnqGF1TBibbepVw_i-MWBriLg68RBPN2_J6Mz7JS0WtPXfXsZbOaSRJ-a0IU9NFJ2f-BlYGSxpW6dwmkQOPectcwvG3-x6mxAh0NkpRwIcUlaBrMAUu34NxNiBdl8eG-dCV_EqEsYvkbX-KgQ9NLcYqKp4ukY-Tzxeg_KQ9uihhbw1atQ-aCHYHEGnufhkAu_hm2lmZiZOZ1dhToPiLDKdvGq96ruRJwzWs_G9kDyJ0o3I83-ulfXrLMizhYfCzU3OYMUUU7bqRVsolLbFkMRdIgBpsJ0irU--i261jgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fLeJd3BjnT5s7_ivt8UnhH8MaeTSJMv_SndRkH6A99jLlP0O7-UVbMg9m2Shsy3hN1rXRMDWdXWY5yCFrCCDLeELWxMXR6JQBNMIngZwa3n3W_DsUcYswGuZNi0hxpsSVwOW8lLqYN0HQJ1jMXUdK8LgEHaDzMxOoyEas0dnJsvB9fmzCkp5-yXj0cAHyGNHGAo_ish-pJXOUXfLaKwkds965AJaRAfB0nFPurIGbiGjtEDhUvfqsfK2TB2fFbbbfo7JB15OoFvrU9sVh83cfAcElHWF2_prAfXXn8qHLhKoSbL_RdRvKlc0wW9pw4TSORxaCWqN8MzjHMkdSNCf1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INIEJXucK3sDAYmcI19X33LBGoHWDyUjcPaM5SDgYmmNLFyYgDQWN40s1YC0JwLjNzAoIgHLNH6lMiX4RdWHVcty0wiDBDLhsbS5lm8sARer8XqEku37NdddXlB8MBeeaK4JcdpjqvOz9kTmP3Nk0XmGyASE3wNdXFpmu-O4vI7S5X3lmGy6YNE5jYwEvjqlmUJEEyOXz4B7LR2OldiUeLMJ-BZpbCgtfC7q06YynVNDSYpWwZ3MKWegC61w-IezTLEKS21CxoaJcUfsuyw9tqbG5J5BT8jNYFisur0JNvM1Rb2mCVye0y7uvd8wvlw-fBK3qJY7TF9nB4sSwI4p5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fd-uvhAGroNv3hi-eQi-3i_m0GV3OIqqTxkD0oVFSJLUxx3-D-UemTIxu1gpeguCB9uWhqNACTDmKegn3ChkXBY96OKu4El67DI65vqjUhVeaAVwmwBdycnXmzHCTjMzXUWUmUJQC2Jkp9YLUpGp90x0-p4RKaTD-zV_F7TR2aybZfBwqTjGTNCRhjf5E9VphMwdaW00q_thAavX37DnhSMQIoX5fh74nW2oA_BSmdTjm_gAGp23vhLbYMaNL096Dgy1VKHq_75X0uml4W_I4pVCHm8p9K6PEF50QjMWqBnBgiOGB1zozHQNVn8wwjPR2LJqPDuhWac4rUrYN4jsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ljj6eVtFJhwskMBB6wLM5RlqjZLsRYxxzwq5gqWYRDVX1XRzBjnz0_4Y6B9Li9J2ySWIE1_ffxbWh1H6gAAGR0SsI38xwESb1E_jpMyE9_L3aib3ebCD7UPfWBaMe8qGn4cdnSqPQNBNGu887c6t2uDAcgudodtKIH0Zj5zC0D7Cb6JBIkopx0UHSWkz1560847GLbKWmRGHKWFO6neFFMI-uABjZXkE-SRk3QX7FihR8PoAoxgqeh_AMxiyTctwYjt0-ni5DsVLWOOybfwLzLfbBbZ303CJyVh_7qtpJy10ZNiqoGT6_GQ6AXOddcLUt6-4a16xjuW0RUfQGoV2Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EDOxXcjck19Y5bv1SY3Hp7XLy4D6L4B1Q1Uzcj9dx9JJ64v-22zD3eLjRQJ-VhLdwkccv0FEWarbYfC_vnbE9Iv7D6LO1tWDv3AcduCVPNNtw_hlF62-_QLSd9fR61gzlHzna64OwRyP9rLUT7gGr77Z4JswmmnAWt4rG_Z6o5JaGNEUDDMBqRWaRkuW2nfgTsb5KbtRQY84-um164bbN6N8ACOkgeFoViYNtIA8xTQITdnQqGQw8rAaZHa0M4fjnkM_SeBMnJMZ4C54_uXGTE4s59R0uqPLRbXOOLyud3dt3xuzLqPwQl4IiFTg3eLzmxGQpObMZuDnyFVYUjRpJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHZyTeowwxa9DT3DojlEMXvllv09kHinHbGX6Hyovg6EMJfy4z4Mp0LTLfBn49zyXkZge8iBeQGbsHMC6q-FRZrSfpP6ywP1iq_sbOyM-c6BWH4bebQPIzDqGmGnze_SZ48dZIGTWld1M6lCauViqlAN0wJwGK75VO-LNko8C0CLG_wCKaGiojVD4TXQGqGduGZn_pO63MhkzBQnCegLA-Jyrm15FWSZqYPFMztDr_9fHp-gJ-S-mjNWoLY1diT7B0jSdYjTv1JxRAQ0-5QkGSsGsm5H9j3phnO4bwtemVJWj3YuO7qnPfPfgPOh-xDixAXK9BQhp2nc3r387pDDug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شام‌غریبان آقای شهید ایران در کرمان
عکس:
مهدی امین زاده
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/448881" target="_blank">📅 03:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448880">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMAv59K5vdnX8MxEH5tG4bDlXfs4vmwx7MLb2zc5UInxqTTCaVJVSjLGsmNPrUoif1yKHzvJ-JJjjnCbew0GhJWVyJ5z8hyc5gvgFVyBxfdMgKrkYfHoOyatgKXKcBbB_3k-pVAxWW5tg197S_9wMXyaufLknIUzOzcWGay7GC1TXidH2nBuQ38O9q30pEBuI4OQ9o9Iz0UiyBrFN9cMm0rKJKkjD_6VZDnKIKgL7TNU65vOlRX37Q4V552GG7KYiQVGs8jxvDBSwLQSo8vsvG3nyjietzCxLFHsDwfdQbXmAauHArU7q6ylpFHJnzBQ0dPY1dk1i4Nll74HLZ-KSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب برای آقای شهیدمان نماز لیلةالدفن بخوانیم
🔹
روش خواندن نماز لیلة‌الدفن به این صورت است که در رکعت اول سوره حمد و آية‌الکرسی و در رکعت دوم سوره حمد و ده مرتبه سوره قدر می‌خواند و بعد از نماز می‌گويد:
🔹
«اَللّهُمَّ صَلِّ عَلی مُحَمَّدٍ وَ آلِ مُحَمَّدٍ وَ ابْعَثْ ثَوابَها إلی قَبرِ فُلانِ بنِ فُلانْ»
🔸
(به‌جای «فلان بن فلان» اسم هر شهید و پدر ایشان گفته شود)
اسامی شهدا به همراه نام پدر:
◾️
حضرت آیت‌الله العظمی شهید سید علی حسینی خامنه‌ای، نام پدر: سید جواد
◾️
شهید مصباح الهدی باقری کنی، نام پدر: محمدباقر
◾️
شهید زهرا حداد عادل، نام پدر: غلامعلی
◾️
شهید سیده بشری حسینی خامنه‌ای، نام پدر: سید علی
◾️
شهید زهرا محمدی گلپایگانی، نام پدر: محمدجواد
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/448880" target="_blank">📅 02:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448879">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d37457a636.mp4?token=nbFGZdXSdHE4XZ5LbEl55K_uXrGljlppZPb8DfBZi8KTRWnyrYPTpq6O00MCxulHupIy7SWx7SxRAjk8-u2dUTWK711_8Va94Sof7wQlPyXl_-HKxXTEIm8F2bM_bBwD0WeZQPmEahJtA42trNPHw4xN2sH7Xq-PeihqHDebb594dvsNBB5XSsR_hfLGSuiF7XWisFQimPkALzH_f_h3fqRed0-9cqpQkEoY9rV2Xle1qX9NfPKY25e3W4HuWGgvbz8NV4McPMAfVNPMlh62VQm-7sbCp3bXv5f-rAnIOyo3wlYl9253sKwqU-0OaQ71YQOWMgP5Eg5aAE37dC9G0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d37457a636.mp4?token=nbFGZdXSdHE4XZ5LbEl55K_uXrGljlppZPb8DfBZi8KTRWnyrYPTpq6O00MCxulHupIy7SWx7SxRAjk8-u2dUTWK711_8Va94Sof7wQlPyXl_-HKxXTEIm8F2bM_bBwD0WeZQPmEahJtA42trNPHw4xN2sH7Xq-PeihqHDebb594dvsNBB5XSsR_hfLGSuiF7XWisFQimPkALzH_f_h3fqRed0-9cqpQkEoY9rV2Xle1qX9NfPKY25e3W4HuWGgvbz8NV4McPMAfVNPMlh62VQm-7sbCp3bXv5f-rAnIOyo3wlYl9253sKwqU-0OaQ71YQOWMgP5Eg5aAE37dC9G0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش صدای خواندن تلقین بر پیکر آقای شهید ایران در حرم مطهر امام رضا علیه‌السلام  @Farsna - Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/448879" target="_blank">📅 02:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448878">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پیکر مطهر رهبر شهید انقلاب اسلامی در دارالذکر حرم امام رضا(ع) به خاک سپرده شد
◾️
پیکر مطهر رهبر شهید انقلاب اسلامی حضرت آیت‌الله العظمی سید علی حسینی خامنه‌ای قدس‌الله‌نفسه‌الزکیه بامداد جمعه ۱۹ تیرماه ۱۴۰۵ در دارالذکر حرم نورانی حضرت ثامن‌الحجج امام رضا علیه‌السلام…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/448878" target="_blank">📅 02:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448877">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaYp7TIUPOuVUS0ohV8lWCLfHjyaLO-ZS8XcpQKuXAWa2UNajRdQNmrVNeUNtaxH_Jb_PV6xEmej-YK7uA2Vf2A9dJPBNPKbP7wj9MCKEHSjTIocYxfqR647NOf7PG4SWJQ39e3J2EEAG8X5ZpSJgnuXM5-8tGrrJ8Ll6_9t3WDj3tX6OSCtk3c4n1lHvKHnyFcTtlIPYPleimGoEm6UxkOodTJS0ZjwHyUoxWwZDVDec8tG0ePqoCx47rNq8lWElP43KHHpqDPNOTWHDsLPxcIpoLfjDU8CZhHqXDaHQnMYdvHX3jBTGL48OSv8xk4LEGH_RTFt-7bDspu_KVcnxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکر مطهر رهبر شهید انقلاب اسلامی در دارالذکر حرم امام رضا(ع) به خاک سپرده شد
◾️
پیکر مطهر رهبر شهید انقلاب اسلامی حضرت آیت‌الله العظمی سید علی حسینی خامنه‌ای قدس‌الله‌نفسه‌الزکیه بامداد جمعه ۱۹ تیرماه ۱۴۰۵ در دارالذکر حرم نورانی حضرت ثامن‌الحجج امام رضا علیه‌السلام به خاک سپرده شد.
@Farsna</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farsna/448877" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448876">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2631b20bf0.mp4?token=bRX9LtokoXkOWKgF5FDOpKHwILRabyOG4EYyb13KEfzc38Zw01fZyH3WfS91tGuD4_OpQVZbeMYCO656avVL2qcCk4shPcWSJnEkeytnI8Ts829fP-GLAQQduZVW1QebQbqSD5mMxyyiSYTFRReNlCzyQ9t9-bBimDvLFF8-mDuG8IWWnYJ8e-8hwnfathnpyUxAASWS3MBbvXTXLPI2ZjcDIMA0YtDuwfXXCzXTAxER_B9BnxYwcCYDTeKP0h4wxdKwgXvdm0U8qWb62XUI4eGDffIJx2N-9rln4z027LzsRh7E2HUpGFVQhj1qynS_lfNRqr22XCTXXCWZD_PqVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2631b20bf0.mp4?token=bRX9LtokoXkOWKgF5FDOpKHwILRabyOG4EYyb13KEfzc38Zw01fZyH3WfS91tGuD4_OpQVZbeMYCO656avVL2qcCk4shPcWSJnEkeytnI8Ts829fP-GLAQQduZVW1QebQbqSD5mMxyyiSYTFRReNlCzyQ9t9-bBimDvLFF8-mDuG8IWWnYJ8e-8hwnfathnpyUxAASWS3MBbvXTXLPI2ZjcDIMA0YtDuwfXXCzXTAxER_B9BnxYwcCYDTeKP0h4wxdKwgXvdm0U8qWb62XUI4eGDffIJx2N-9rln4z027LzsRh7E2HUpGFVQhj1qynS_lfNRqr22XCTXXCWZD_PqVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش صدای خواندن تلقین بر پیکر آقای شهید ایران در حرم مطهر امام رضا علیه‌السلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/448876" target="_blank">📅 02:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448875">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxLJSS1EIPR5pgypuo1XSZHBexYUgWwehA-fuNXazxpDg7Jdd56mevJRV8J2pNGqsVBBUooBpJlocB1vZIEttati625daRHrpahPlVOxmgtNVwo6-r7O3FpcU0bmjZClHFxwRkB3tfmDpHnuQ0FHmHqRTiqJSZ1tbTTPUv6UqDoUqr6nxenCBLoQLSdv8Wid0y7EQRrNH3x9xWV_qnbSEI7XbjQtF63FxGptTtC-PiNizxVlRZRI4hi54Lh5rgowLTK5eH280xRW4a0FJBNiTrjz1JtfOZZ9fGlrMama_Iv1D2UjUx-aMKYgzuiFuMG0PUNGfdDCVJShCIshzGwhCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و امام شهید ما در آغوش امام‌رضا(ع) آرام گرفت...
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/448875" target="_blank">📅 02:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448874">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd9d31545.mp4?token=WCTAIZaccqWpgmF9hdVPEac2KdATfDgAZwGOBiNnf78QfMArcEmfoyyDWtIQkfxCIATaHD9te6mq7HP4nFwfsf5x9ZWyOwGze0xdqbDjxW5JI_UvRjLtnLlAXBEBeeA9xhbjXtIkPdE9BrWrh55Dk0Pe9c3EOu0-EqCxm3P0MRhyi9IjuBvTBpNOhthC9VrlaPi3BmqjMpU6JdFoS5gUUidUi3kLv5VZk8i7cXuyvCv9oaefVRCTpgkc-IP8I1kVVhrAeeIG6UJtm6sDznQMjBCMpE6TbbALP-QxSj-BExHh360lydh0kQqLJukZc6viahzqT5NKx2X0CEYqPrvP-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd9d31545.mp4?token=WCTAIZaccqWpgmF9hdVPEac2KdATfDgAZwGOBiNnf78QfMArcEmfoyyDWtIQkfxCIATaHD9te6mq7HP4nFwfsf5x9ZWyOwGze0xdqbDjxW5JI_UvRjLtnLlAXBEBeeA9xhbjXtIkPdE9BrWrh55Dk0Pe9c3EOu0-EqCxm3P0MRhyi9IjuBvTBpNOhthC9VrlaPi3BmqjMpU6JdFoS5gUUidUi3kLv5VZk8i7cXuyvCv9oaefVRCTpgkc-IP8I1kVVhrAeeIG6UJtm6sDznQMjBCMpE6TbbALP-QxSj-BExHh360lydh0kQqLJukZc6viahzqT5NKx2X0CEYqPrvP-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه خدام حرم امام رضا(ع) بعد از تشییع پیکر آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/448874" target="_blank">📅 02:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448873">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b25ed473b0.mp4?token=XYfEvCFKD4es31qtSG86o9autQMxiD0vwJgvkaOpNlXhcSTvgVGNNGAHWCroVNkDPSapbP8QKd434nCe6L-e_vEFtEua20EZnqrdq3UKplny2b4-CYE3vfxufP55YdxPX4r31ZLA7Gfs2T2c92KCoiT0LnNnwo3SQObbTH3vY12FqBd5KYtMy39nRsY5rY5p3kQer1JTf2IUbSSM-qUmau1ChZ7FjT1Okp_a_Y_pF0d1PDP-pUcmxNWPWTfbkwETpkRenJebhHYZ8Izikghjis-2SX-3xa0DqeHsenWhk5WADYdcXFzRXC0x9SgdpUfAeMOUaxeTe1GrJmisnkSLTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b25ed473b0.mp4?token=XYfEvCFKD4es31qtSG86o9autQMxiD0vwJgvkaOpNlXhcSTvgVGNNGAHWCroVNkDPSapbP8QKd434nCe6L-e_vEFtEua20EZnqrdq3UKplny2b4-CYE3vfxufP55YdxPX4r31ZLA7Gfs2T2c92KCoiT0LnNnwo3SQObbTH3vY12FqBd5KYtMy39nRsY5rY5p3kQer1JTf2IUbSSM-qUmau1ChZ7FjT1Okp_a_Y_pF0d1PDP-pUcmxNWPWTfbkwETpkRenJebhHYZ8Izikghjis-2SX-3xa0DqeHsenWhk5WADYdcXFzRXC0x9SgdpUfAeMOUaxeTe1GrJmisnkSLTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدای گریه بلند است بین خادم‌ها
@Farsna</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/448873" target="_blank">📅 02:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448872">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f739e7fa5.mp4?token=rfAbT9Vies-iGXUkXxb4ADcYNRmg7-KdFKoDbu_aTMjzy021Bv4GuaVnT3SvhLxJUCiGVgNNjM8juodxa5khYFhZx3FZeiPCLO_nxX3LXbRGtwGqvdsveheZAHTXWX9rK60IDTbAoB3kYXRZxIMnN0jTgLwPVXaLCOtVs7NbK3ziWq09jmDh-ZA_500mCkxLK-YBgwDWHbI89M6sOOQHezYX8vjgkArWsGERdyA8ZNxhZbyJ_FwzjxDw-RWNCVvogcVsOV5Z5t1-B_fZTvdOs4chL59CdWcVka6J-rawl8RkPK9kq3SwrvEGGr83nGQqSiHSuiNlQ6t3fnP1hGzokw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f739e7fa5.mp4?token=rfAbT9Vies-iGXUkXxb4ADcYNRmg7-KdFKoDbu_aTMjzy021Bv4GuaVnT3SvhLxJUCiGVgNNjM8juodxa5khYFhZx3FZeiPCLO_nxX3LXbRGtwGqvdsveheZAHTXWX9rK60IDTbAoB3kYXRZxIMnN0jTgLwPVXaLCOtVs7NbK3ziWq09jmDh-ZA_500mCkxLK-YBgwDWHbI89M6sOOQHezYX8vjgkArWsGERdyA8ZNxhZbyJ_FwzjxDw-RWNCVvogcVsOV5Z5t1-B_fZTvdOs4chL59CdWcVka6J-rawl8RkPK9kq3SwrvEGGr83nGQqSiHSuiNlQ6t3fnP1hGzokw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک ایران عزادار آقای شهید بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farsna/448872" target="_blank">📅 01:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448871">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91faf2a0b.mp4?token=MNVsh0cvJ4Ju-8tnawchbtJm_pG7-uoOZRsIC2hK521bdmE-2DrgFeviO7ffipt8pmvg9ennc2bKeYwY_FMcsFkJ1WZ9k65FvO8T82deaSOA8nRAJIfIBfmJr2OM5vZXMJ5zUHloq291gi1hEX-Zb5axbcOb5ODMQSDNkOOSgq95UzHPdLo4ftkZSUOkNNho0zfD8Gh4tvyKxnBL0KZBCe2i9vGgz-8hfFWYBDKXT1pqARrUiQbY22nhxQrBAJeTYWLtFtcSU9CBLQIUcB-JJiZP9OLk6BOt2naZwQOoSI8ZHWmepscGcvRuBImz7kQgd24K1pQzSBrYvY4QyXT_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91faf2a0b.mp4?token=MNVsh0cvJ4Ju-8tnawchbtJm_pG7-uoOZRsIC2hK521bdmE-2DrgFeviO7ffipt8pmvg9ennc2bKeYwY_FMcsFkJ1WZ9k65FvO8T82deaSOA8nRAJIfIBfmJr2OM5vZXMJ5zUHloq291gi1hEX-Zb5axbcOb5ODMQSDNkOOSgq95UzHPdLo4ftkZSUOkNNho0zfD8Gh4tvyKxnBL0KZBCe2i9vGgz-8hfFWYBDKXT1pqARrUiQbY22nhxQrBAJeTYWLtFtcSU9CBLQIUcB-JJiZP9OLk6BOt2naZwQOoSI8ZHWmepscGcvRuBImz7kQgd24K1pQzSBrYvY4QyXT_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در جمع خادمانت، شوری به‌پا بود امشب
@Farsna</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farsna/448871" target="_blank">📅 01:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448870">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vb6aLARmB9NpHGC0h3A4M1UOGAD89W94vltAWB-KTjn6BQwZmf_vEMTPrEKDMiRPrLZBfOC6OeIliF6Q4YSb64cFwdf_Lc72jmIEXxZZcIfgtxQ-4trpV9U7SspEBjGHJoRWEivDCJOj5T0-LzZv5lZOOA1_0zJc0EQyhdgJ25OtTNnoOViZs76Eh4-43E5kTSlKUQy91cI53hV8fyQg0FmhBAyI_Sp3CcZoA-UdEs-4GLnzGgfqg6mHkoInuUGVKBwOeVmtelwBnhhb1KrDXBbPZAKJ4kJt4-qgEoJWM7bYuvyHGngcYi1JqtdLMPTg3E5ibk8UlkgZ1ZTZVgMK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
#عکس
|
ان‌شاءالله خدا کاری کند که در قیامت هم خیلی رفیق باشیم
«در دنیا با هم خیلی خوب بودیم، خیلی رفیق بودیم، خدای متعال کاری کند که در قیامت هم همین جور باشد، خیلی خوب باشیم، خیلی خوب باشد با ما، خیلی رفیق باشد با ما؛ ان‌شاءاللّه.»
امام شهید سید علی خامنه‌ای ۱۴۰۱/۱۰/۱۱
@rahbari_plus</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farsna/448870" target="_blank">📅 01:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448869">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvCGMaxHuXmOSSRQJp8aZnkR2_xVI21C9anDe2GnuS3e_YkDBlDkG-lFX7g3NQDCnMZpU6Z7U3LU6si73tVOZqjxWiQ6UIIvUolvdaeO9LFhiqJownZieJ84R5SNTo6ln2_aH8uMJqQtPLCUyrHDiq5uKhBYmngpf_i_gRDPL8JYXXaTxXPifkwoB7yICfzbqhYpPm1nDIEK0Ml_FZO1yXFGzRAvaRRrCt_Ma55mzeQfNwW-64bWvqVUCgSBF0XQ_8THy4xeHAUrhmXUo5I1v0Aw7RBOHtas7oPlcB_zuxQ__RpMPmq1Z2JoRwX5JCEdhooPqGyttQqkneg-gLQOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه مراکش را حذف کرد
⚽️
فرانسه ۲ - ۰ مراکش
@Farsna</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farsna/448869" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448868">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05a9cb6f9d.mp4?token=XS2Q0vmCrBaRY-zdzTjh_k1qe4gEz6Pi8dkBKebcTLl-HT40QYJZp-YrkirxibJgGnxY3iV1qGRUWNqJv2wZ0w3nmjtVepRjVm9b0upZEd270AN0IWYLyKV9HfQzsVsly6RCLUzzGR8eCGyjXoKxD153vHFnb-3R13Pfgxx9QXIJE0rfr9xVNG64fYKlkYNoiNhyZ1v4AqRpjo7sSQladC07BwnfWVSb62sduWtgO1bRfcGu9BOuerbhQStlalkrOROF1NLgWIDCx-VwOE5vfy5zltYQv2Hir0dqcFdjmU_n3J2-xdqb7WrufOgtzoghqXQUm3UhoBaViqO_1Oh4Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05a9cb6f9d.mp4?token=XS2Q0vmCrBaRY-zdzTjh_k1qe4gEz6Pi8dkBKebcTLl-HT40QYJZp-YrkirxibJgGnxY3iV1qGRUWNqJv2wZ0w3nmjtVepRjVm9b0upZEd270AN0IWYLyKV9HfQzsVsly6RCLUzzGR8eCGyjXoKxD153vHFnb-3R13Pfgxx9QXIJE0rfr9xVNG64fYKlkYNoiNhyZ1v4AqRpjo7sSQladC07BwnfWVSb62sduWtgO1bRfcGu9BOuerbhQStlalkrOROF1NLgWIDCx-VwOE5vfy5zltYQv2Hir0dqcFdjmU_n3J2-xdqb7WrufOgtzoghqXQUm3UhoBaViqO_1Oh4Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
السلام علیک یا اباعبدالله(ع)
◾️
سلام به حضرت امام حسین(ع) توسط رهبر شهید انقلاب اسلامی و شهید حاج قاسم سلیمانی
@Farsna</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farsna/448868" target="_blank">📅 01:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448867">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cfa4c42fe.mp4?token=b1PgIKm8kCP9kpx9USsg3s7nwl0Vprz6zDByQMWLutCNPRhQAom8dMjAAkx56FiScYP_0gh10IFjFqYT6qnQBHKYZvy9JHqyfyzlw-ZZgM3TiZOwkMCrdgkYv9MyzmP_SJHBWZXLRJNFlF2q7ZBxNZF4V0AhYb4oZqb1CDgYYohQLytI9q7WhmHF0IOPYWBCz3JpPQhosH0PYsgdUgolgLxlPME7oar2DgRFYBVa4nhiVaxogML-XIty6wv8f69_xKSNjJAS8MdxAIIzt8xmNaUpzhXymA6Rw9nABocu5_5v84lXc0Z7ynnNpEvZ8FkSlg6qynIURCWwAN89PHJwo13yYDEIkmo5ehMa08O5MB9dfrr3ytO238Ycfq2ODBTsYxhbyLtjMTng13CwbK5p-W0Ilg5zDiXs8dyM7INJJO_IdGb0V90bWu8ZZk0P4e8ozDmPLlRb-Fy2tvgh5VlveUtUREygKrZvY--HT-fkW1uzyiXhk3lzb95XJ-vvWQ46J5c2yMGkel1_ypR1RR4q4qU2fkBkeLigeCgEpoCJiYGHxsv3Lknsf8v4teBjhLite-Pj3M7kb4__gqSXb_IduQcFN4_ovBwYtQWep5nkq81HgkOgIJ_aY7sTbWbeB8Q4zUuT3gweVCCiGwtsqJh55fqgB_dATyRJB02l-IW_Jr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cfa4c42fe.mp4?token=b1PgIKm8kCP9kpx9USsg3s7nwl0Vprz6zDByQMWLutCNPRhQAom8dMjAAkx56FiScYP_0gh10IFjFqYT6qnQBHKYZvy9JHqyfyzlw-ZZgM3TiZOwkMCrdgkYv9MyzmP_SJHBWZXLRJNFlF2q7ZBxNZF4V0AhYb4oZqb1CDgYYohQLytI9q7WhmHF0IOPYWBCz3JpPQhosH0PYsgdUgolgLxlPME7oar2DgRFYBVa4nhiVaxogML-XIty6wv8f69_xKSNjJAS8MdxAIIzt8xmNaUpzhXymA6Rw9nABocu5_5v84lXc0Z7ynnNpEvZ8FkSlg6qynIURCWwAN89PHJwo13yYDEIkmo5ehMa08O5MB9dfrr3ytO238Ycfq2ODBTsYxhbyLtjMTng13CwbK5p-W0Ilg5zDiXs8dyM7INJJO_IdGb0V90bWu8ZZk0P4e8ozDmPLlRb-Fy2tvgh5VlveUtUREygKrZvY--HT-fkW1uzyiXhk3lzb95XJ-vvWQ46J5c2yMGkel1_ypR1RR4q4qU2fkBkeLigeCgEpoCJiYGHxsv3Lknsf8v4teBjhLite-Pj3M7kb4__gqSXb_IduQcFN4_ovBwYtQWep5nkq81HgkOgIJ_aY7sTbWbeB8Q4zUuT3gweVCCiGwtsqJh55fqgB_dATyRJB02l-IW_Jr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین لحظات وداع با رهبر شهید این‌گونه گذشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farsna/448867" target="_blank">📅 01:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448866">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6c21ee90.mp4?token=phEBedhzVmuXRmPHKBecG4pfCycd088UDUf7u-m5TwjnYHG0-63yBneDbOA7mJAAMgkqwCw5StC0xFR3-AWEsdHX1dC1GztnlyrGLbsfbSKEuEzUSB-7BRf20cAP4aw_p80CvUGbnwX1H3jbsT6tCIReIseIOUCO_Fr32GN4nMk7hBoJ9WQmO6vDtIy2jpT7zUyyaPe2sZJppI7rldA4r_Rv5a6KeXWd4yKoaraLOJj3k3O1i4jxgeKhtHzcQgkfih3s9EwoTXb0dOc-ntQo56k__pWaPkVk--6EgfgVJoVgu4KPs5E4bw_1vvSXxoSXcgBQhTohMN6-PJDbhOrBApZNjKme6qMm7cgxF7HJ82qm9zLRJmyp1RtT11VxZj_-lCg8tqIn_GxjPdDEt7bgD3xjey4Xz0bjZ5vG_6OtXhLwviYTMEMd8IEwu-8DYDF2os7F-vwTK3cggrrCYMXJPUIdaYkSiYJYMwU8Qcv6jRHIQvbFHs1FSeIv0LISrhigLMPIourLikdaHQwcZXE-8rKPiPwKRBzLku63U4LqfbEpWgUA_Lz5k5dE4E_FrOVklj-K3ADyxeWqlu6hPhUV34lTsydx1ckmh7oJbjyzB05En1RojsncZEv7FDDkqoflSeEDgMGW0Ic9DP_EM7YWlh5HBqDSDXOcMELogGuA-jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6c21ee90.mp4?token=phEBedhzVmuXRmPHKBecG4pfCycd088UDUf7u-m5TwjnYHG0-63yBneDbOA7mJAAMgkqwCw5StC0xFR3-AWEsdHX1dC1GztnlyrGLbsfbSKEuEzUSB-7BRf20cAP4aw_p80CvUGbnwX1H3jbsT6tCIReIseIOUCO_Fr32GN4nMk7hBoJ9WQmO6vDtIy2jpT7zUyyaPe2sZJppI7rldA4r_Rv5a6KeXWd4yKoaraLOJj3k3O1i4jxgeKhtHzcQgkfih3s9EwoTXb0dOc-ntQo56k__pWaPkVk--6EgfgVJoVgu4KPs5E4bw_1vvSXxoSXcgBQhTohMN6-PJDbhOrBApZNjKme6qMm7cgxF7HJ82qm9zLRJmyp1RtT11VxZj_-lCg8tqIn_GxjPdDEt7bgD3xjey4Xz0bjZ5vG_6OtXhLwviYTMEMd8IEwu-8DYDF2os7F-vwTK3cggrrCYMXJPUIdaYkSiYJYMwU8Qcv6jRHIQvbFHs1FSeIv0LISrhigLMPIourLikdaHQwcZXE-8rKPiPwKRBzLku63U4LqfbEpWgUA_Lz5k5dE4E_FrOVklj-K3ADyxeWqlu6hPhUV34lTsydx1ckmh7oJbjyzB05En1RojsncZEv7FDDkqoflSeEDgMGW0Ic9DP_EM7YWlh5HBqDSDXOcMELogGuA-jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع شهید مدافع وطن در زنجان
🔸
شهید یوسف محمدی از پاسداران زنجانی که در راه مبارزه تروریست‌های اجیر شدهٔ دشمن به شهادت رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farsna/448866" target="_blank">📅 01:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448865">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شایعه‌سازی ضدانقلاب با انتشار خبر کذب تیراندازی در اطراف حرم امام رضا(ع)
🔹
پس از پایان مراسم تشییع پیکر رهبر شهید انقلاب که با حضور میلیونی مردم برگزار شد شایعاتی در خصوص تیراندازی در اطراف حرم امام رضا منتشر شد.
🔹
بررسی‌های خبرنگار فارس در مشهد حاکی است هیچ اتفاق امنیتی در اطراف حرم امام رضا(ع) و مسیر تشییع پیکر شهدا انجام رخ نداده است.
🔹
همزمان اما در یک حادثه تیراندازی در محله سرافرازان مشهد ۲ نفر هدف قرار گرفتند. اخبار اولیه از جانباختن این ۲ نفر حکایت دارد.
🔹
معاون امنیتی استاندار خراسان رضوی نیز وقوع تیراندازی در منطقۀ بلوار سرافرازان مشهد را تایید کرد.
🔹
او با تایید جان باختن ۲ تن در این حادثه گفت: هنوز علت حادثه و هویت کشته‌شدگان مشخص نیست.
🔹
بلوار سرافرازان در غرب مشهد واقع است و بیش از ۱۵ کیلومتر تا حرم مطهر رضوی فاصله دارد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farsna/448865" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448864">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6d305ae3.mp4?token=izLjPZ2diKRCx2j3RvRIJAVcCpC_L7WhZnI4P1jWEsBx5iO77iLTIaO8Qe0NdFuqhrZ7zK7AYp7P78WHz8_cAYd0e4iGnAFtQ8WZT4Fnnt_3boG_hw3ulGe3Opm4-y-KXqGFAOSAvdCrVf0R1Z05T1KEhu9E_Gzo6VtHjpMbpXASrtSw74DTwaqmC1mqkmjGfjTWHg31j-qdfWDNAWFfxlxoe6qB6yociUgOdr2F8KqIPAmN9GOSZmg43-rPTC45KEofab90OCdeLBQlMFYGGEbgvdZTVTB69WhxRn4X54FbzN7HUXGldmapAKmuzVvJwkcPg1PAYm8Q5V0xRCN77g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6d305ae3.mp4?token=izLjPZ2diKRCx2j3RvRIJAVcCpC_L7WhZnI4P1jWEsBx5iO77iLTIaO8Qe0NdFuqhrZ7zK7AYp7P78WHz8_cAYd0e4iGnAFtQ8WZT4Fnnt_3boG_hw3ulGe3Opm4-y-KXqGFAOSAvdCrVf0R1Z05T1KEhu9E_Gzo6VtHjpMbpXASrtSw74DTwaqmC1mqkmjGfjTWHg31j-qdfWDNAWFfxlxoe6qB6yociUgOdr2F8KqIPAmN9GOSZmg43-rPTC45KEofab90OCdeLBQlMFYGGEbgvdZTVTB69WhxRn4X54FbzN7HUXGldmapAKmuzVvJwkcPg1PAYm8Q5V0xRCN77g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین زیارت رهبر شهید هم انجام شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farsna/448864" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448863">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c570b53917.mp4?token=Go1sz0bkIDuZd1BikLizjaCCaOqio_Zk9lm64_rRbMkPSl9Q8vwU4pTKlTM4-91FFqYEfhbrORnnAcGXNdb5rypueHqNYBH15TbnjDNbH7oQPc4nEwa6cFNPbuvRsGVDQF0MEEhtz1bz3o17L0BQV1b8cg0xCWL8KtKY1w7Cd7RpRXSm0r_BeVnxTl2yLURyhlFC8h-0_6Uq_8gFrzeSjtLR8rwTmjbFIYyTjHxicnsXxcxbQHf6gyyC7dV_8RLO-IQIl1KGco0ltd_G6G5YjYn9cTFYM-zzpzmsFwQh4qg_aww5rEgaoMDUZ09oTCAI5V_KPB5C6-UCsrsjIK_QEEkJTLbJUP2amr8Eal2pjUqeQI_JieeFmBLuFv2hOLcAXOTziQhkiiU24H2M7mIuMrPhUqoRVGMHwNZftt8T5SFVQe1_TfyUFJw_Uj25YiTPSWM-BaS3aOX5DnAv7JDHxA_Wz76CjU4fYLInNtmHEOkuJuLZ2u9EICKQzFQhZ0I0kbmcDuqduQXXEC5U_4V8qQGLn80GLCID4K1VnFvguSbx3PZrWnFFDgBvAmLxgTBELEowBVP-vXDTWEPKVqLJN35m-AF6kq14x9OlKm4xn99yZCOJ1I6Xn4-XH52zJ0_SxiaYUVQAVHiztJPUT-5jmq9aA_F1pm100bG_YrLV9TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c570b53917.mp4?token=Go1sz0bkIDuZd1BikLizjaCCaOqio_Zk9lm64_rRbMkPSl9Q8vwU4pTKlTM4-91FFqYEfhbrORnnAcGXNdb5rypueHqNYBH15TbnjDNbH7oQPc4nEwa6cFNPbuvRsGVDQF0MEEhtz1bz3o17L0BQV1b8cg0xCWL8KtKY1w7Cd7RpRXSm0r_BeVnxTl2yLURyhlFC8h-0_6Uq_8gFrzeSjtLR8rwTmjbFIYyTjHxicnsXxcxbQHf6gyyC7dV_8RLO-IQIl1KGco0ltd_G6G5YjYn9cTFYM-zzpzmsFwQh4qg_aww5rEgaoMDUZ09oTCAI5V_KPB5C6-UCsrsjIK_QEEkJTLbJUP2amr8Eal2pjUqeQI_JieeFmBLuFv2hOLcAXOTziQhkiiU24H2M7mIuMrPhUqoRVGMHwNZftt8T5SFVQe1_TfyUFJw_Uj25YiTPSWM-BaS3aOX5DnAv7JDHxA_Wz76CjU4fYLInNtmHEOkuJuLZ2u9EICKQzFQhZ0I0kbmcDuqduQXXEC5U_4V8qQGLn80GLCID4K1VnFvguSbx3PZrWnFFDgBvAmLxgTBELEowBVP-vXDTWEPKVqLJN35m-AF6kq14x9OlKm4xn99yZCOJ1I6Xn4-XH52zJ0_SxiaYUVQAVHiztJPUT-5jmq9aA_F1pm100bG_YrLV9TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار امشب مردم شیراز: باید برخاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farsna/448863" target="_blank">📅 00:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448861">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b62719d5.mp4?token=M7Jw83m8SNqCP_xncc3hN7JRQkjqLVwLMO6yHaYxMKK54wBXsQ4fu9n_tUSmXhfrS5u8ITGEX8D7vZceSergR_9Ty83PX2VJTna_zBqS2s1YcifZZhD99at_GMUuSsyMMZierimgDtAltjfj2PFGRWHMXtFwxPRRvHqTspn8KmAnaR41h3Ay6JLEjnefIZywCnqV_54DJa-qSBCx67oPBQDQ97UJi5h0kU7tqaS2f6o4xbmGBUT4_vA4DQMvPN9t_BTaVVmKspjshYRRV95t0AjkSqyc3EhON81vkByqP85R-rQsNaxEy4rE-89u94pweaKk2FQhP9rWdPrUgEuRUHOP72nTZ8bY0pj5xxuA_QqjIasyisKNfkWLWRj8iCBIzVGuByCDpcgLsyeVCBked70-UPG6e84rSmtLipYNRKaiVwYphE1AlnbMB8H7327NR3O232kIOjtbyaNK1R2OpLB3uB7x9aScTv3t1tfw8PiQta3c1gdbXnmxuv7ME7SbD2mG2z8oLwjDmBM-pTzLudm-2CziaxhcDtYrhC9hW08gyRSxNluSl8zEdPsdAxgF2M6Qg9c94f6NEUTMJ08GARCz7Kvve22FiZY7r_hHBeZAoH4AR30joWYVJUi1q-2FIgqVNMgCDTvBc8Yi6YzZdlx-CMI5Qu9gfXJxg22Rsfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b62719d5.mp4?token=M7Jw83m8SNqCP_xncc3hN7JRQkjqLVwLMO6yHaYxMKK54wBXsQ4fu9n_tUSmXhfrS5u8ITGEX8D7vZceSergR_9Ty83PX2VJTna_zBqS2s1YcifZZhD99at_GMUuSsyMMZierimgDtAltjfj2PFGRWHMXtFwxPRRvHqTspn8KmAnaR41h3Ay6JLEjnefIZywCnqV_54DJa-qSBCx67oPBQDQ97UJi5h0kU7tqaS2f6o4xbmGBUT4_vA4DQMvPN9t_BTaVVmKspjshYRRV95t0AjkSqyc3EhON81vkByqP85R-rQsNaxEy4rE-89u94pweaKk2FQhP9rWdPrUgEuRUHOP72nTZ8bY0pj5xxuA_QqjIasyisKNfkWLWRj8iCBIzVGuByCDpcgLsyeVCBked70-UPG6e84rSmtLipYNRKaiVwYphE1AlnbMB8H7327NR3O232kIOjtbyaNK1R2OpLB3uB7x9aScTv3t1tfw8PiQta3c1gdbXnmxuv7ME7SbD2mG2z8oLwjDmBM-pTzLudm-2CziaxhcDtYrhC9hW08gyRSxNluSl8zEdPsdAxgF2M6Qg9c94f6NEUTMJ08GARCz7Kvve22FiZY7r_hHBeZAoH4AR30joWYVJUi1q-2FIgqVNMgCDTvBc8Yi6YzZdlx-CMI5Qu9gfXJxg22Rsfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاخانه‌ی کرمانشاه در اجتماعات شب ۱۳۱
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farsna/448861" target="_blank">📅 00:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448859">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0JBuh-Dl6VgSkRjSH1GytWaI-w4ppohTW7RdJz3R2oX_l1uPWD39Zms5dr5FLy-c-akzf3D4fOVVHFdbH3wXeFtbByCx5gFun0VHN6x1w7uE1aAfdNfR94wVDFco0INMz7baHNHrxeUIwzf4HddUImgKRAXCJHSJoYbHTNbfqZ8CjoOZT_fwZ87hGxBE-1ouV0DjCwrh12cFyzIlkw_oJ3M0cYm5iCbbemGKHHmqtMrFwYHz6l-En0s5PQ_6_tUPemLL6dMl4fS3rmoNozlQlxz61gvok0KwvW848nf5fpbrx19h9l8_TQmhhdMlFN-6DWQPvDF7-nrnylU0DZfkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توضیحات دفتر آیت‌الله نوری‌همدانی در مورد عدم حضور ایشان در مراسم تشییع رهبر شهید
🔹
«با وجود آنکه مقدمات حضور معظم‌له در این مراسم مورد بررسی قرار گرفته بود، اما با توجه به ملاحظات جسمانی معظم‌له، بُعد مسافت و فراهم نشدن شرایط لازم برای انجام سفر، حضور ایشان میسر نگردید.
🔹
همچنین چند روز پیش از برگزاری مراسم، عدم امکان حضور معظم‌له اطلاع داده شده بود.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farsna/448859" target="_blank">📅 00:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448858">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfbd16b17f.mp4?token=M65h8TGEcZPrHwBsPtn7HBNb0qvjJf6C1Iya2mnEz2fiAzd1b89jM8mRwMgkSS5UYCt6sMTxHtcJJQptTb032FZBMIlycMg9bfeFwl41KhqM1BNAQ5WIm2-EvNPuHD1QYV4IwNMVKCM7r2fQxywD8mdeiesT83dYTooIMaNaM1zO_dqdRJT-g7r71UKrq9rbVU0vYoqltONF4iWbHPr8ArVwTyEZ_Ctk1Y39VenXSD6LkCKt_sgY7Wx89CkLCq8PgIoXuqU7E48s1XHt_bUnytVUuKQcENxHu7Q-Ga4YoSRzD8onmjTRNli4elZgtimC1TIYfofpmbOcUgT-7--S9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfbd16b17f.mp4?token=M65h8TGEcZPrHwBsPtn7HBNb0qvjJf6C1Iya2mnEz2fiAzd1b89jM8mRwMgkSS5UYCt6sMTxHtcJJQptTb032FZBMIlycMg9bfeFwl41KhqM1BNAQ5WIm2-EvNPuHD1QYV4IwNMVKCM7r2fQxywD8mdeiesT83dYTooIMaNaM1zO_dqdRJT-g7r71UKrq9rbVU0vYoqltONF4iWbHPr8ArVwTyEZ_Ctk1Y39VenXSD6LkCKt_sgY7Wx89CkLCq8PgIoXuqU7E48s1XHt_bUnytVUuKQcENxHu7Q-Ga4YoSRzD8onmjTRNli4elZgtimC1TIYfofpmbOcUgT-7--S9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضۀ میثم مطیعی قبل از تدفین پیکر مطهر امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farsna/448858" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448857">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55abc22245.mp4?token=gC4gNUEapVqDNxNcYPBZ5Wb4lxI8FGbhmdn7kj_tWlWq8AJ1vYoBD4g0fUhdrnSXi8lT80k-Oja9CsEBQt34wftL7rhAg9FmNzmiR_Csn9lRGUf5YJTDkbQJxuED6QY1biwY_5P-MaYHsqoA14ukPKRMDW6AGyxJkQP_f5lXJeO585ik0UFChUsCLt5eQ1CcvoBr0Q0wWBAIOaKUTkfnEaossErBxxp7uWNJnHRXlBvhhxtxT_dmFaBLB-LYWvekGBC7GZpM2u-vkSAFSflIJKQVxcgIrFnMe3rNIF95shUldmInhp_h9NrWNDuGTHhttvvC1xYo5VapXsWmqnRe1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55abc22245.mp4?token=gC4gNUEapVqDNxNcYPBZ5Wb4lxI8FGbhmdn7kj_tWlWq8AJ1vYoBD4g0fUhdrnSXi8lT80k-Oja9CsEBQt34wftL7rhAg9FmNzmiR_Csn9lRGUf5YJTDkbQJxuED6QY1biwY_5P-MaYHsqoA14ukPKRMDW6AGyxJkQP_f5lXJeO585ik0UFChUsCLt5eQ1CcvoBr0Q0wWBAIOaKUTkfnEaossErBxxp7uWNJnHRXlBvhhxtxT_dmFaBLB-LYWvekGBC7GZpM2u-vkSAFSflIJKQVxcgIrFnMe3rNIF95shUldmInhp_h9NrWNDuGTHhttvvC1xYo5VapXsWmqnRe1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حلالیت‌طلبی یوسف سلامی، خبرنگار صدا‌وسیما از رهبر شهید انقلاب به‌نیابت از همه کسانی‌که طلب حلالیت داشتند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farsna/448857" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448856">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46229c7a7a.mp4?token=kWbCtoufY2IbXNav5OZFkl1-qckNcKNBZFUzpdhr2OMdHX4DXJdwtEMHrxk0Meb7SwFkaLcJFZ78lLXIUJ0IMRd0keYhcJiCI7Awbhabf0-NKxgsfAPabYng7yQoS4X_m227KK1IeX6Uyd9IL7bJVs09HZr1sgXNGyK9UOTX_1hOvdbaLimIDILAXBPmdk-w1GAElNJe5UDOnwo9BFI_LgwIhcWEmwunmST-s-f1RwE0aCl05qGbceYz5rTZ09zlepFg5q79RWAqm6ZYwF0azVA1mzjn3nzwqPMqwVoFt7Q_ZV-2QZk9l2ROCpUhfvBUJCcTVdfRxCtAqO6dXAmL3pXDnfXQNx1DjrnWZiCVlT5O1gnnNLuwDQSid1zhHPkdupjeOhZPXL50MvbRbociq3RW0qCrLjcAUzDL_V0ti2Ob9DkTvvU0OVzW3Tnhk2O9xFtclciLXMNCng2vRssISRKyhy3dkghnm-OuQeEqqGXUmhKY5NNmVZOFkO5MNrvRCjP7wbcVewisnb0PiNIkixI9-Vik7xnDsUduabgRuskEYrC227TSZ8NharVqgYEzL6l1-VSwAlqj_5c-p-TLwYr95fXyCz3Oj3ZwuswuVNglIjvDVkJIYABc6A1_4stl3zZZOQw-tfD_Yjzfge57QF8ZfBn9JR8HjhxkChcsTTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46229c7a7a.mp4?token=kWbCtoufY2IbXNav5OZFkl1-qckNcKNBZFUzpdhr2OMdHX4DXJdwtEMHrxk0Meb7SwFkaLcJFZ78lLXIUJ0IMRd0keYhcJiCI7Awbhabf0-NKxgsfAPabYng7yQoS4X_m227KK1IeX6Uyd9IL7bJVs09HZr1sgXNGyK9UOTX_1hOvdbaLimIDILAXBPmdk-w1GAElNJe5UDOnwo9BFI_LgwIhcWEmwunmST-s-f1RwE0aCl05qGbceYz5rTZ09zlepFg5q79RWAqm6ZYwF0azVA1mzjn3nzwqPMqwVoFt7Q_ZV-2QZk9l2ROCpUhfvBUJCcTVdfRxCtAqO6dXAmL3pXDnfXQNx1DjrnWZiCVlT5O1gnnNLuwDQSid1zhHPkdupjeOhZPXL50MvbRbociq3RW0qCrLjcAUzDL_V0ti2Ob9DkTvvU0OVzW3Tnhk2O9xFtclciLXMNCng2vRssISRKyhy3dkghnm-OuQeEqqGXUmhKY5NNmVZOFkO5MNrvRCjP7wbcVewisnb0PiNIkixI9-Vik7xnDsUduabgRuskEYrC227TSZ8NharVqgYEzL6l1-VSwAlqj_5c-p-TLwYr95fXyCz3Oj3ZwuswuVNglIjvDVkJIYABc6A1_4stl3zZZOQw-tfD_Yjzfge57QF8ZfBn9JR8HjhxkChcsTTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید روی دستان خادمان حرم امام رضا(ع)  @Farsna</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farsna/448856" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448855">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c4993915.mp4?token=LHMWJ0saj2zRDj3p2X96HI_B0IjK402Cr9DqfquIw5OHD7nWHrdzlLnybRV_r4zGmR4Fa5BCzLDFY-zFzhEjPRbDd8jkQVjt3kPu7YFDYZg7mjbUb4n04iJJVIKXBZmlgYyBOwgRTXHV9aiZbkzo8J8VytSqboT4E8xop9UO18C7DCqIOPRFiHtIKFVEWDtCkDNkKvKaJ4viPzjvqlAeOWpVkFLXOkUadiBfOw0G-LWTXKipTN52ZdgQoUVt6LwrVH2MXv_Dn0HtS1w9C7JqPv9De1EKkQZWDnZDiulAvuSb39xYaSDT6ZotPgqCjU5iQfkdC9k5__EUt11LFPVkxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c4993915.mp4?token=LHMWJ0saj2zRDj3p2X96HI_B0IjK402Cr9DqfquIw5OHD7nWHrdzlLnybRV_r4zGmR4Fa5BCzLDFY-zFzhEjPRbDd8jkQVjt3kPu7YFDYZg7mjbUb4n04iJJVIKXBZmlgYyBOwgRTXHV9aiZbkzo8J8VytSqboT4E8xop9UO18C7DCqIOPRFiHtIKFVEWDtCkDNkKvKaJ4viPzjvqlAeOWpVkFLXOkUadiBfOw0G-LWTXKipTN52ZdgQoUVt6LwrVH2MXv_Dn0HtS1w9C7JqPv9De1EKkQZWDnZDiulAvuSb39xYaSDT6ZotPgqCjU5iQfkdC9k5__EUt11LFPVkxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی محمود کریمی کنار ضریح امام رضا
(ع)
@Farsna</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farsna/448855" target="_blank">📅 00:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448854">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddbc94faed.mp4?token=DtTJQu4zdPjjU_papHtyZ2pemU-LqFpzAEnzStnsfusqRYVM8dy6zvusuUCyLWKZLWEhgzzKSMJr4ifg-UnNuscVSb5HMpZxMW3Ek8OtquZnTSafFOeeScETm5qpTd_iPm9clF8E0dOI2Vp0TFORn1DZ4xXWfrPYONPvGdVlMS4eGgWrodVoaUY5twDfV3ip8nhJcL5oJeK7A_rUS4y4OMPIWsNfjjbNcvOJI4a2ovisXtrJssYYbTPy3VosYPS3CDDKwkek-6TGBnhAzeeMmCeE82MsEvbWh0D0ZpWCwuzzALqFGwgWp2NVlDzlx_1-lrURZUIscliiSSSanj2vdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddbc94faed.mp4?token=DtTJQu4zdPjjU_papHtyZ2pemU-LqFpzAEnzStnsfusqRYVM8dy6zvusuUCyLWKZLWEhgzzKSMJr4ifg-UnNuscVSb5HMpZxMW3Ek8OtquZnTSafFOeeScETm5qpTd_iPm9clF8E0dOI2Vp0TFORn1DZ4xXWfrPYONPvGdVlMS4eGgWrodVoaUY5twDfV3ip8nhJcL5oJeK7A_rUS4y4OMPIWsNfjjbNcvOJI4a2ovisXtrJssYYbTPy3VosYPS3CDDKwkek-6TGBnhAzeeMmCeE82MsEvbWh0D0ZpWCwuzzALqFGwgWp2NVlDzlx_1-lrURZUIscliiSSSanj2vdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوهٔ ۱۴ ماههٔ رهبر شهید به آغوش امام رضا رسید
@Farsna</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farsna/448854" target="_blank">📅 00:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448853">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N64eEfPsPVrs3CkwVwNgxKmDTvj92wfZ8LQyxEGGwS8Hcu3iQHMOowDlRmtrrmcIA4BTiWiURfCP4Q_2-fcwqlIyoHCM4dHVmTQBGfUGUtab0kxYfnh4Ew3HeGB4J1xlQyr0JPZTYtrm6Yovm8BXsY2XGD5noDbkWmQ2pd0puAoUHa6nFxjCQu2cPqux5UyzQV6XI3tuvAsp3_bgE4Xeuaz_hNuB36IQ2RxrbZR6hO62YfVaI6UWe5Wh4DMB9Zmzr54p_DGoZUQgN5J7kNsoilno25_V5DERr3k1TGrpb3jsf-bjyIUVp1IQDZTotR0acPCW_esFn-OuW-xJR9Pstw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پیام رزمندگان پای لانچر به مردم: خدا را شکر که جای خالی ما را در تشییع امام شهید پر کردید
@Farsna</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farsna/448853" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448852">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/361a464c64.mp4?token=EBhMHrZAQIKztoAh0VS5OmxSscDJoW7qAfMAXw6Da1KN5Vnl2WMwzq8OM7oonbJCMhKLsNko9on99Yk5BwHkaUhOmfySRXDCfwz5E8SUdkuOiuR4OkEvjox9yxI2AMW96_APhW0aSQoMawBQfQVYI4Q7cTEmf7rP8jgk46-lFVg3qwId9ZrHxKKdBEcpzNjyjDp-EGaY2PKLOh7WpDXU35afed1Wob7d-KVv7IfixJpY_L-NbRb1iLFK45Mu0_wKJC08Qb2vJvBf85IDWoC893brG5lvgmtv6LoKswsYcsGS_jr9PbGupupmaQ-RJNqC1Oi0Z34tc8PkEtNLR9DiclXEPx91vTyI-75z6GZTJcnW1Aq8KxkqB0xXjo0BR8WM-QOzGCzeFugZpf1ggCDRNrBRHlNKuWeuKAsGkSxoeK7WybhTVRcunZqbWt8-c94Ul8_YDhJRZmpWWNZ1NGEzmhivYpayl2FHK98S_WBzg7QIYUje5di7TUkNxrcvrIun1zBFX5suoJ3iBAlPS7PD7c9e1srP3MLKv8cVWP5AZxaRmO6kML4VOldSRhjJlI2CeEyGg0K4Mxn-3znci4RwS3XtAin5bKKLGrBzELjTgg9ElapZEh72fTmGTurq-7GtjX8r5p7zhzLoAowdWMUpLfZ3BjEDUtGzPhFfeOeuzfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/361a464c64.mp4?token=EBhMHrZAQIKztoAh0VS5OmxSscDJoW7qAfMAXw6Da1KN5Vnl2WMwzq8OM7oonbJCMhKLsNko9on99Yk5BwHkaUhOmfySRXDCfwz5E8SUdkuOiuR4OkEvjox9yxI2AMW96_APhW0aSQoMawBQfQVYI4Q7cTEmf7rP8jgk46-lFVg3qwId9ZrHxKKdBEcpzNjyjDp-EGaY2PKLOh7WpDXU35afed1Wob7d-KVv7IfixJpY_L-NbRb1iLFK45Mu0_wKJC08Qb2vJvBf85IDWoC893brG5lvgmtv6LoKswsYcsGS_jr9PbGupupmaQ-RJNqC1Oi0Z34tc8PkEtNLR9DiclXEPx91vTyI-75z6GZTJcnW1Aq8KxkqB0xXjo0BR8WM-QOzGCzeFugZpf1ggCDRNrBRHlNKuWeuKAsGkSxoeK7WybhTVRcunZqbWt8-c94Ul8_YDhJRZmpWWNZ1NGEzmhivYpayl2FHK98S_WBzg7QIYUje5di7TUkNxrcvrIun1zBFX5suoJ3iBAlPS7PD7c9e1srP3MLKv8cVWP5AZxaRmO6kML4VOldSRhjJlI2CeEyGg0K4Mxn-3znci4RwS3XtAin5bKKLGrBzELjTgg9ElapZEh72fTmGTurq-7GtjX8r5p7zhzLoAowdWMUpLfZ3BjEDUtGzPhFfeOeuzfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید، زائر امام رضا(ع) شد  @Farsna</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farsna/448852" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHsiT_a-qqXUfD3230Bb6ggTj7BQh9xTB34RGqj_JJ8T1AnO3d1UZ71FAXtybjvtJBUiB2oV9XVAwBhSgd9AuBeiyX7MWNKsPTwtz4pk4_QibJvn5RB_bbvW0-VoUURilTVsTC5ap55MdZnq-4opCSNGNO05gyXNZsEGXaniLUrIzLgY1cbW4gg1W8PKHWvgG6ZxULtqoue2Gmr8yK2RvD7kmu-PaNf8xPy1jQsElUgxD78pqo6ZEjwKiLuxeu13F_lOZt-TttKB1W9i2T40fHmjoKOzN0VX0C6i22Wb4nKoH-S61yWDLdOxlSrKi2Je7VDdrC8c8gbWWDIPSR-cFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W2bK7zIY9vbqiuowGbG6KMNfOvnlI7mftuQVYL2LwPfMVMzYnBaSxOKvuPKIEkLgatu7pCuXuv_txcOaLMljQphcr9Go9FtZ8zM1Vsq-wZQi4fi7em30OyW0fhF-ROkQeraliLxu3BYpcVOToYTZxvztSzen2tuS5toAEab3CE8QhVZMRhHdSM95OpXb64ykB6qPzNbGkbFRrCWBYKNECl9SGzUGNCm2AxxUUvdRp0zCV7Ibo_dNEBTlsIH8gLdFFql27Gd2W-nMJBgE8BH7CdaEz16ocxZtbV4bnHaRYfFwzPW_NQc7_2_LyAU0tN8UVwfT43Ak0Q3GDo9IKTxsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VM_8bO-3Pq6PNNJ725EjwXEdo36-i7WK8G_6lEp9KXSUHZG3WPSKGwAsAAHD3-cyKiIj_W70qQ2D1D_CA5LyLNT-g4go3INiUPre_GDZHrXEC5rSEDnkptK8BT8vyCIbrRkEDZyeHMjaDJbGGmaeo3dItjD6G2yxVOJ3PvAqV_xp8Wdt6llpcuMB1uXLvSfYHhnczxp5HLiFYPpxlLtmHzZWSgb9MR4DIu243oag8qD7gAumFO0U4E8rcX9SQCKuiH7gGmT99WM4pqJ16HDlthVcMm8X31ela5VaTAvCygu-SIF9z-qtXttzi0pi8ib34qql7l5MNeeftjakbbGacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRVEAKs_afx3PTibk9X-tDcl6en28_XJSzDkXI_bAPjCWYXYO4VCgPIPJAI4e48So4iYoSmwwHyODix7ik21nDGaGilfGkBRAepFQ97vQCciPjdbJwrDyQNt8DzSCE_TC2tllVg2BfMle2j6RgDQe2NPmFVVItCEZLs0SHm0lRt52cO4FrWuHCDJnG6RC3f1p_twvf8EGQFAdva3ZiqkFAjklQI-SbQENu1Y9SXhgB7QkKZhXAlWrrpkB4FexVISFhEvcPAb2THWAZGLKofbvHHwk95HRx5vhDlVMHwz6udimoMXUQrcwi-IzGf4Glkbi7EFVPswHT549yPPXL2eJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2rOCr_wlcU9MUpihQD9YOUZFYSM-tIhBqgfRMFT-2FA_9e53fi91K0gqiN9w2rjrJBSUNNciK4X8MaGa3S6LuVfKPWBfT-UTKpmw0QrYZBNGyVGoeJcDSIYshxQQ2fMiWN--0Gax_H_8_-LQNniibcq6H7K_bB3X6OUuXqKv-KFeuTcPS3kWJ0OQbRtb2ELXxWZW4h59uwaELb7xCF2l737HWAG_15Bz-NoSMu46E6L_2i2bL2XqeXI7enb3Xw4pMWi4IjCGT45YRNa1FeAgjaZA7iO4zYQHGNAAMN0EKA_2QHlHRhgZwvzop-SacNA77h0icdUD_55ft1Y3Tle1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NC05k7rgWoNg5VE_xXsEuzKCE9GRpf1o-_EXmni-W17frcqOOUVxi-sBbL2yWz2W6sdsI1RUi4RyZG3OzgUPi8epifbTtRrvwd5Y6uuSLOv2ugSUiMdCj6YHImy1kxQx3qUusC2VD0idkA5Pbh2CuYQm-YIGj-L_wGCtfKf2QjaCU_kUGUjGk1-kwrweDc64VVsLNruqVRWEIk0O1YSYIk-tS9uYF6knk2gQIcxrM35aOwI9KyX6Jnmboeqcs56t-_QIuhUBnu2TbVL-MlhUc2LQcsrXebRZAF5GbuKJa9z8N2NDaKoAX66MyIbKDTfJelHeyUqAHgyVqI3vbxZK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOtqEaHUi9BIsobCw7G6VlQWF_43FKwn2IycRLS0DEvC-INZJYcyLVz0R2zrJBpAubnGatoVb2iFJFdztwgTE3J3BqONy5lmRgcTnNvUaZAC4d_2Q3vE6p5G0e2-LRWhJb-tRz8RTjBVB2tvixmgIIO2U8TczfYtgoSkgNjd2xswniP7b4Hgq3bjvBGFevah-1s1cMEndnDEjt6ZoTcVrBbN-yFqbXRJP8pM51St1wRAOPYgjHtScsJ-9H39OAidRUrHYvdySD22EP1XD3oPH3lsdLQ1-uAxxBf4ouuprYsFAqdqaVt5lCTwP7-ZHVhSnHvbON460kmACtfgINZnLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر یار بر دستان عاشقان
عکس:
زینب شعبانپور
@Farsna</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farsna/448845" target="_blank">📅 00:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2684c94630.mp4?token=WFmv7Ii_WlCKoresWsq_gmZQjMBOmYoeas6PZJ8gubcoV8kr4c2sAw5G_GdDq5OsUNlHb5GwU075x6BNNlk34zB4iNlP9Mnk1gmJouP1rWLYErj28TZlPPWKaBwTT5LvmgyCjGYwpUnuj2lU198tRPgYjt3URxhdXBispYgBK7MO1GENtxsb79Moy4WwKMYAaUgW7Kxx09tGS1_b6jyACwHnQIjthbvFmg-qw0CH0AFLDhKRX60Z9SWW3JGAh32iuxmpBroNbNn5QjN3fmHbG8rfpqlPcyuM-Q9JGzIT3avbWCyfZCPMKg35dLHKHcFiE-Ae2REczhWI831i9AX2Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2684c94630.mp4?token=WFmv7Ii_WlCKoresWsq_gmZQjMBOmYoeas6PZJ8gubcoV8kr4c2sAw5G_GdDq5OsUNlHb5GwU075x6BNNlk34zB4iNlP9Mnk1gmJouP1rWLYErj28TZlPPWKaBwTT5LvmgyCjGYwpUnuj2lU198tRPgYjt3URxhdXBispYgBK7MO1GENtxsb79Moy4WwKMYAaUgW7Kxx09tGS1_b6jyACwHnQIjthbvFmg-qw0CH0AFLDhKRX60Z9SWW3JGAh32iuxmpBroNbNn5QjN3fmHbG8rfpqlPcyuM-Q9JGzIT3avbWCyfZCPMKg35dLHKHcFiE-Ae2REczhWI831i9AX2Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ صداوسیما: اقامۀ نماز لیلةالدفن پس از خاکسپاری پیکر شهدا انجام خواهد شد
🔸
به محض خاکسپاری پیکر مطهر رهبر شهید ایران و شهدای خانواده ایشان، اطلاع رسانی می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farsna/448844" target="_blank">📅 00:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448843">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/448843" target="_blank">📅 00:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448842">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
منطقۀ نظامی نیروی دریایی کنارک در ۲ مرحله هدف حملۀ دشمن قرار گرفت
🔹
فرماندار کنارک در جنوب سیستان‌وبلوچستان از وقوع ۲ انفجار در منطقۀ نظامی نیروی دریایی این شهرستان خبر داد و گفت: این منطقه شامگاه پنجشنبه در ۲ مرحله هدف حملۀ جنگنده‌های دشمن قرار گرفت.
🔹
او افزود: دستگاه‌های مسئول، نیروهای امدادی و نیروهای امنیتی بلافاصله در محل حادثه حاضر شدند و بررسی ابعاد و جزئیات این حمله در دستورکار قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/448842" target="_blank">📅 00:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448841">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxzxTC6Cbw8LL1SWU40kVY8Co8Lqw7tHdGvFJvDUkgdECzq84CJeoPTIrl_NE4x5qR08LGP-nC0JqITcPfFwHUA9EYbui_dyJa_O0Z_9P4L6-gWGA7uSUeCNlbGewL_qIDJfbd2ny8SiQ-kv6JKf4xe1PVOOmkXQog60OjxT-iRshzTZvYQsPNy7rxPfiu_gSzYY5tcMXvdBhREU8NfCh3jpzCw52RmryMSbVR6qNinuE9UIMV8-sRO5WKxT6HSVyKnKgxu5MmO7qKkuezo3YD-2ZqreE_B5se3JHAjOkU7aLF6F0x59xNgsW3azWgn6NLsMB61Os4wE6RstWyCODw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سر انجام؛ ۶۹ سال دوری و چشم‌انتظاری، تمام شد...
@Farsna</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farsna/448841" target="_blank">📅 00:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448840">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d641c1bb0.mp4?token=lX1sd16ofE_RIanCXGXoU5PMTvOvIzmP0u0BkdTno1ET_viO7AnzmtEwlxvhqSbaULlzXDNv_AYP15l8xdAOdjweh4aiJ-UeOtSIvKqFMa77jQrRYQGUxKi6V2BMqfS-z9WCF2KUpSqVozLG9fDos63PVqBa07oKp43RlrsyMCaEhtZQvydksgjuyO4_Yi3pD5CHvWVnrkfT2vrWkbg4rflxu5FqXGgi0n6vVcKRYZo3JsBqk1ZzTPTP74EeKydVpqUwTxEdTZFhEnzlWgPWY-OQskUMjZqmeagfuRTOhFOuXzCNK1Qu9WuT9vYkejnKsw0EbsMyU-uJegVc6dYruA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d641c1bb0.mp4?token=lX1sd16ofE_RIanCXGXoU5PMTvOvIzmP0u0BkdTno1ET_viO7AnzmtEwlxvhqSbaULlzXDNv_AYP15l8xdAOdjweh4aiJ-UeOtSIvKqFMa77jQrRYQGUxKi6V2BMqfS-z9WCF2KUpSqVozLG9fDos63PVqBa07oKp43RlrsyMCaEhtZQvydksgjuyO4_Yi3pD5CHvWVnrkfT2vrWkbg4rflxu5FqXGgi0n6vVcKRYZo3JsBqk1ZzTPTP74EeKydVpqUwTxEdTZFhEnzlWgPWY-OQskUMjZqmeagfuRTOhFOuXzCNK1Qu9WuT9vYkejnKsw0EbsMyU-uJegVc6dYruA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری بانوان ملایری در شام غریبان رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/448840" target="_blank">📅 00:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448838">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hin-d6j3GNt1StWJnFGDTIfG6ktux4nTky9ndeedlv7GpRnZCSuaaB0Hupv2k23KnZtFozXN5u6gE3ydmk3hUOU1xsyqF6eGfau4cjMPQnbdjeN9pnDvOl8PAq6GFIrw2qCYoOzjQK8Gi8co-YqXZLkyCZMBM5qlMQ0ZuiB7eqPoVWRpv0j63FAjp_HBi6A3d4Y2b5oIIU-E-uDOp842OtRyRWkHDPdTmKG7HZVQUJ2i_sl1sJP-FTaHlhigUu3F2wHSePAi-atpi050LcEe0ksb6hqyKn0QvMbI7heYLn65a-B-0TIQ8clGIoGb_tHx07pfA5VbykAT8XjMzI4U3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| جمعه ۱۹ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farsna/448838" target="_blank">📅 00:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448837">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1adb3da9e3.mp4?token=uiyAUFIpbzW5B8zUpp1pj2zAeg8M2NKFE9VJ9eQABBcJ74VAtD779HX8__ayRqUxjJZAQ0roSC8iNOZ-Ft10csrTVzRLMi9_gHBJTIpakAP-pEqALz2gFW4nNDNflXT0yz3OMNTymjQBv-qbQ4jXh5WZQhJvT6lTquqdvIX3pyqiZRssEG4RcjWW5A4f2niOj25vU2cdgIBSQdBlk9sTF1vMu96cIWHsqCf_FapHNskP9ieVCHftt07b4UyOx9oX_cVhfZCL4P2TjVIoZ_DdFga0eyHKHKLQc9rMU0FZ4xPaR-8qAoHHExkhE8hoRtu0Zze3TVajth6b-mb7V9dBGUx8Re7nZC6Y-OMS-FlNt_SR3fisTbhIh_qztrFfAA4ryF8DcvTmE04lmLO0rQuDAkzZigdLcJEdu-j0OJ-aGkZt9t5xbLEgupt9vE3Kfa7jR2at1euydSSIoZtoH7oxqdqrxVJSJzdQJuZU7tgd7wksJUcsQFjrPQcBM-2mrD20SK3bvxXfHpyo1nfwztNRPjsTruqDEMd7h2VUsVnoFEL-F8ablIERxXVnXNZM6d6_xMT3C-nkKpvaKRxZsuy6q90aVuySF8osk-nQtSIVwG3TGGKYzqJnFseyN9dthk_4FK0C3seAt_oDjktF35GL4wqINBNY4893NcSDpAFRJek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1adb3da9e3.mp4?token=uiyAUFIpbzW5B8zUpp1pj2zAeg8M2NKFE9VJ9eQABBcJ74VAtD779HX8__ayRqUxjJZAQ0roSC8iNOZ-Ft10csrTVzRLMi9_gHBJTIpakAP-pEqALz2gFW4nNDNflXT0yz3OMNTymjQBv-qbQ4jXh5WZQhJvT6lTquqdvIX3pyqiZRssEG4RcjWW5A4f2niOj25vU2cdgIBSQdBlk9sTF1vMu96cIWHsqCf_FapHNskP9ieVCHftt07b4UyOx9oX_cVhfZCL4P2TjVIoZ_DdFga0eyHKHKLQc9rMU0FZ4xPaR-8qAoHHExkhE8hoRtu0Zze3TVajth6b-mb7V9dBGUx8Re7nZC6Y-OMS-FlNt_SR3fisTbhIh_qztrFfAA4ryF8DcvTmE04lmLO0rQuDAkzZigdLcJEdu-j0OJ-aGkZt9t5xbLEgupt9vE3Kfa7jR2at1euydSSIoZtoH7oxqdqrxVJSJzdQJuZU7tgd7wksJUcsQFjrPQcBM-2mrD20SK3bvxXfHpyo1nfwztNRPjsTruqDEMd7h2VUsVnoFEL-F8ablIERxXVnXNZM6d6_xMT3C-nkKpvaKRxZsuy6q90aVuySF8osk-nQtSIVwG3TGGKYzqJnFseyN9dthk_4FK0C3seAt_oDjktF35GL4wqINBNY4893NcSDpAFRJek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیرزنی که خیابان را به شوق رهبر شهید به هم ریخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farsna/448837" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448836">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3dee3d178.mp4?token=onOp5bCv3CEid5QVk42gH4ZzvvCe1JcqSjhilpyvzOf9ay0VEqNUtFRNE-cvFzaCnZpgHDkOLl_IBAbDW0cty-z7tkgFPkNKT79bP9Puo0TwqjOf445w0X-52MYLUznBz02g64Acvn30FTIFtAlKeNO8y75gj8DY9DvOyJe0fObukjUDcSxE-g6S0Fr7PtmviQZWxegqyBhmaPMnuv6J0zYeLiIVQYR87wee6MCa_HgysB-f-4smCU3G40DkMeFfp8kRGCV3WR16i5AlKe_IESLKo62KuME7yVatPlx9SlBnLEsZSgoSjesG738oymbnVK2GoCQlcpnZyHN4CWKyfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3dee3d178.mp4?token=onOp5bCv3CEid5QVk42gH4ZzvvCe1JcqSjhilpyvzOf9ay0VEqNUtFRNE-cvFzaCnZpgHDkOLl_IBAbDW0cty-z7tkgFPkNKT79bP9Puo0TwqjOf445w0X-52MYLUznBz02g64Acvn30FTIFtAlKeNO8y75gj8DY9DvOyJe0fObukjUDcSxE-g6S0Fr7PtmviQZWxegqyBhmaPMnuv6J0zYeLiIVQYR87wee6MCa_HgysB-f-4smCU3G40DkMeFfp8kRGCV3WR16i5AlKe_IESLKo62KuME7yVatPlx9SlBnLEsZSgoSjesG738oymbnVK2GoCQlcpnZyHN4CWKyfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تا دقایقی دیگر خانواده با آقای شهید ایران وداع می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farsna/448836" target="_blank">📅 23:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448835">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌ صداوسیما: اقامۀ نماز لیلةالدفن پس از خاکسپاری پیکر شهدا انجام خواهد شد
🔸
به محض خاکسپاری پیکر مطهر رهبر شهید ایران و شهدای خانواده ایشان، اطلاع رسانی می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farsna/448835" target="_blank">📅 23:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448834">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f506e92eca.mp4?token=PBRFZfZbm4qp9HA5EXihbs-ag8n6JKJVX0hvvseqAZNBUqrnCMtE8Rr-WdypYeD_nyY_6E4ypnqjIGGNk7N-InkTmBKr4dTUmy0YJjy-cSktNiAPfhXLr-D0aQUU7x_tAB8sbVPt5tl3X4dz907rVXUq0THuaRVUT0yGl2_pk2smpp7RfZvz4WFh2bWg4Pi_Jer3vfVMCWj5pacaqH3Y0zL2ppxekifhgaRmxr0IwVgzbVY_R_zkxxKIEQKf4MXA2h24hWcfnBiHE7m9i8boa7gMyZ6VfxxubkWOcPruwV7HAHAGdaHdjNORBvBIxeITeg82W7mlOoPdIkYJQb0YQ6RmIZlu0CMcAne_lQlSv8q9tNzOPhGhHPrKtCz1q0ztfpqtqNKOhA-BBKiJ9_gqRren_FeYO6LDkPWg2UV4mLuuCjW4A1gRamEInnE-AAYIrYlVyjbGkk9_3OuzRI7_LOAFtNIqTuvr5ZsRZlelvuVbtyQ53KufjSRN9-ovZmwBY7fQ-DYof-G3GhKczh0T8U5kmaW76p2Dtw7r9e4cnOqy6Msdz7rDRs_BMK3w7oubKLse7bGsceAoPCy9YHGfS3_bUDYHDoiExA8fIiooEXKSkBcRnhrHBjrojLJbL_EU1L-_UPRwGlfgaFqJ6aDT8hBEMD5qUPHmiXvYRQwjHJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f506e92eca.mp4?token=PBRFZfZbm4qp9HA5EXihbs-ag8n6JKJVX0hvvseqAZNBUqrnCMtE8Rr-WdypYeD_nyY_6E4ypnqjIGGNk7N-InkTmBKr4dTUmy0YJjy-cSktNiAPfhXLr-D0aQUU7x_tAB8sbVPt5tl3X4dz907rVXUq0THuaRVUT0yGl2_pk2smpp7RfZvz4WFh2bWg4Pi_Jer3vfVMCWj5pacaqH3Y0zL2ppxekifhgaRmxr0IwVgzbVY_R_zkxxKIEQKf4MXA2h24hWcfnBiHE7m9i8boa7gMyZ6VfxxubkWOcPruwV7HAHAGdaHdjNORBvBIxeITeg82W7mlOoPdIkYJQb0YQ6RmIZlu0CMcAne_lQlSv8q9tNzOPhGhHPrKtCz1q0ztfpqtqNKOhA-BBKiJ9_gqRren_FeYO6LDkPWg2UV4mLuuCjW4A1gRamEInnE-AAYIrYlVyjbGkk9_3OuzRI7_LOAFtNIqTuvr5ZsRZlelvuVbtyQ53KufjSRN9-ovZmwBY7fQ-DYof-G3GhKczh0T8U5kmaW76p2Dtw7r9e4cnOqy6Msdz7rDRs_BMK3w7oubKLse7bGsceAoPCy9YHGfS3_bUDYHDoiExA8fIiooEXKSkBcRnhrHBjrojLJbL_EU1L-_UPRwGlfgaFqJ6aDT8hBEMD5qUPHmiXvYRQwjHJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ را بکشید، ۱۰۰ میلیون‌‌دلار جایزه بگیرید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farsna/448834" target="_blank">📅 23:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448833">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ece8888e51.mp4?token=s1rh9khLJFu29-ebR68F-PPMKqSXN9Hv6BSNNhkHaXuiw_6C-T5TbTY0TkZcxM0kEdRuGBvgCE9EQSWNeL_j9BNPVhoV0zOhLntgxQx71UAi7bF64tPxLZmbiLHt4badl4Dvg4fxpJYjZ3yV-FvZ9zev4h6EMJu8h3m5U2trhyql8iJp1bL2S1XiMwlbomoD55YFywAZ6FEA4rVKl8mhThBvIurbep4TuAmlX_XtHJc3GtTPvVPsnrYu3Bs2KL0huiJbvoGEyo2WUnhgA5hLMWSwZAEJaJ2zRf7XjKFcjw2SDQtEksdG_6OU0wRvqIfu7zyV0WF3iZoimoURDG-sUT3BE5OlQ-Nu6wFxqZ8eX5_FP7rYrptKPNWaUGFbkv1Cz9wnbaWwGNV0zNfGw-KquDDGu7oR7O0eFrCmEacaR6r848rZrOTuHKpbzpAXTgDmTxAfTdXppO8nmuTcWHVJzYmAMwQCbtNDnBbJLmL7LzmEJ5QFbSbiXgYLCAbsrXHMD3Mc1Ocrl02ng0m5n9mV82jbDgbVnXpjl0qXMsCtP1d4pqRsWlmeKS4OW3cHJX2H1efTk3nxhPemg7ulRMrSxCEIpBt8kdmBt-ErXzkABWUOMHAHtoKuhCi82RcNUQk7Be5GKPaVVwpDG_ykkXx8lsL1B4dcrEOnMzw2NIt0R4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ece8888e51.mp4?token=s1rh9khLJFu29-ebR68F-PPMKqSXN9Hv6BSNNhkHaXuiw_6C-T5TbTY0TkZcxM0kEdRuGBvgCE9EQSWNeL_j9BNPVhoV0zOhLntgxQx71UAi7bF64tPxLZmbiLHt4badl4Dvg4fxpJYjZ3yV-FvZ9zev4h6EMJu8h3m5U2trhyql8iJp1bL2S1XiMwlbomoD55YFywAZ6FEA4rVKl8mhThBvIurbep4TuAmlX_XtHJc3GtTPvVPsnrYu3Bs2KL0huiJbvoGEyo2WUnhgA5hLMWSwZAEJaJ2zRf7XjKFcjw2SDQtEksdG_6OU0wRvqIfu7zyV0WF3iZoimoURDG-sUT3BE5OlQ-Nu6wFxqZ8eX5_FP7rYrptKPNWaUGFbkv1Cz9wnbaWwGNV0zNfGw-KquDDGu7oR7O0eFrCmEacaR6r848rZrOTuHKpbzpAXTgDmTxAfTdXppO8nmuTcWHVJzYmAMwQCbtNDnBbJLmL7LzmEJ5QFbSbiXgYLCAbsrXHMD3Mc1Ocrl02ng0m5n9mV82jbDgbVnXpjl0qXMsCtP1d4pqRsWlmeKS4OW3cHJX2H1efTk3nxhPemg7ulRMrSxCEIpBt8kdmBt-ErXzkABWUOMHAHtoKuhCi82RcNUQk7Be5GKPaVVwpDG_ykkXx8lsL1B4dcrEOnMzw2NIt0R4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم تشییع شهدای ارتش در بندرعباس
🔸
۳ شهید ارتش در حملهٔ ۲ شب پیش آمریکای کودک کش، بر روی دستان مردم بندرعباس تا گلزار شهدا تشییع شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farsna/448833" target="_blank">📅 23:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448831">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">امشب برای آقای شهیدمان نماز لیلةالدفن بخوانیم
🔹
روش خواندن نماز لیلة‌الدفن به این صورت است که در رکعت اول سوره حمد و آية‌الکرسی و در رکعت دوم سوره حمد و ده مرتبه سوره قدر می‌خواند و بعد از نماز می‌گويد:
🔹
«اَللّهُمَّ صَلِّ عَلی مُحَمَّدٍ وَ آلِ مُحَمَّدٍ وَ…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farsna/448831" target="_blank">📅 23:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448830">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e7cdb87a.mp4?token=Lxwmd5VhAo2JYglQvUim2lUhC5ZSf3Brn52A1f7t1c83aOQjaRrZvyHeSbAdlgX14h8s48xR4HFjR1F8dNGPIdCJJ00m1MIXqImoueoLUyMDD9GpuOCg0x7ncceVGZ1GLYc0s16zue_dgKUEHQDKZCYqD889-86buzaxF91Vw91f3IRGjYfDlHxzthTNhgmptCFMs1NttWhqucLqn61Ie5x0YGT300uiWrfwl6hXps08SNPnoNd8ME85Lwie-isZNJ1EU8f5xAHMcF57cWvKNwb3E-kpLoeS-ObhkH2caQ7UAgVOzN7JU5vPdXHJwJagIir4NFC5Jy8_2HGUP-6eVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e7cdb87a.mp4?token=Lxwmd5VhAo2JYglQvUim2lUhC5ZSf3Brn52A1f7t1c83aOQjaRrZvyHeSbAdlgX14h8s48xR4HFjR1F8dNGPIdCJJ00m1MIXqImoueoLUyMDD9GpuOCg0x7ncceVGZ1GLYc0s16zue_dgKUEHQDKZCYqD889-86buzaxF91Vw91f3IRGjYfDlHxzthTNhgmptCFMs1NttWhqucLqn61Ie5x0YGT300uiWrfwl6hXps08SNPnoNd8ME85Lwie-isZNJ1EU8f5xAHMcF57cWvKNwb3E-kpLoeS-ObhkH2caQ7UAgVOzN7JU5vPdXHJwJagIir4NFC5Jy8_2HGUP-6eVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از انتظار خراسان برای متفاوت‌ترین بدرقه‌ٔ تاریخ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farsna/448830" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448829">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdY5SkkVhgoL-j3MxAvyTIzcanRBm4dRtIGnx4iJLXgLhMv6F4lTLAdKp-BI3EdYOQN07uLrdRP-CFe3WZI6XQ9A3GnCF4x4oUUwTjxTBdNaTv3nTYTxu_L1IGtoqImpMSJ5uNgkT-8wRPN03wBDGhOvDNkJ9XNoKqqsCdqp8_rIWgpnRt4R1-bs2UhBOCgLmMdJqkpyvSPA7hW8wWXojV1Zu7Tdbs92BgczUALzvI3SezIN3ylEVhqWIO81KPELiu5d7E2dHMfOUKoDVjY9zoKVzkobGecZSDt6SAxwzXt6cr1mG_Ipjb2Ic2Nm_I6aJC5IsmmdKGSjxR5e81rLBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
شهید خامنه‌ای در آغوش امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farsna/448829" target="_blank">📅 23:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448828">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-57WriDZim_mvr5T1RCQdmrv20-1DvdXL0_rec7-EZZO1sU8BXfy9hMJ97zRIKqUcsSiAYBgs0rc6SPK1_EaNSHhmMtCm-yPlNR2SbTHhdcz7_ktlvqleWEDKVA4z1o_Y-CP4p8IyH7G3P-OnpGKczndlCbaZzgp0BBuH7pV1VLjvhLQElSAwK5Hfdy7HEHBnxKS_yqr_gWGiJs7vKBD41RE_QnSdK9qBOPO471JMls7wZi5V2XoJDltGXvB8jo44JHcEmZeUY6iGCN0d-2S7J5fK3ni3uJR6J3zRQp_e916t27d_w_8xBMBCQcStPTmYbInh0Dw7uva68xDjb76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین برآوردها از میزان شرکت کنندگان در بزرگترین تشییع تاریخ جهان
🔹
مراسم وداع و تشییع پیکر رهبر شهید انقلاب، در یک بازه ۶ ‌روزه و در ۵ شهر تهران، قم، نجف، کربلا و مشهد برگزار شد که با حضور حماسی و کم‌نظیر مردم، به بزرگترین رویداد تشییعی در تاریخ جهان تبدیل شد. این مراسم در تهران سه روز (دو روز وداع در مصلای بزرگ تهران و یک روز تشییع اصلی) و در قم، نجف_کربلا و مشهد هر کدام یک روز ادامه داشت که با احتساب تکرار حضور افراد در شهرهای مختلف، جمعیتی کم‌سابقه را گرد هم آورد.
🔹
منابع رسمی جمعیت حدود ۴۱ تا ۴۳ میلیون نفر را برای مجموع شرکت‌کنندگان تأیید می‌کنند. این عدد از تلفیق چند منبع میدانی و رسمی به دست آمده است: میزان آمار تردد با وسایل حمل و نقل عمومی به محل مراسم، تعداد گوشی‌های تلفن همراه فعال در مصلی و خیابان محل تشییع، میانگین حضور هر نفر به مدت دو ساعت و نیم در ساعات برگزاری مراسم، محاسبه حجم جمعیت در مسیر راهپیمایی تهران، مساحت فاصله مسجد جمکران تا حرم مطهر در قم و همچنین مسافت مسیر فرودگاه تا حرم رضوی در مشهد که همگی به عنوان پایه‌های پشتیبان آماری در محاسبه لحاظ شده است. علاوه بر این، آمار رسمی مقامات عراقی از طرف دفتر نخست‌وزیری نیز حضور حدود ۱۰ میلیون نفر را در مراسم تشییع در نجف و کربلا تأیید کرده که این داده نیز به عنوان یکی از ارکان مستقل محاسبه، محسوب شده است.
🔹
براساس این داده‌های ترکیبی و میدانی، مراجع ذیربط تأکید کرده اند که حتی با محافظه‌کارانه‌ترین تخمین، این مراسم از تمامی نمونه‌های مشابه در قرن اخیر پیشی گرفته و به‌طور قطع و یقین، بزرگترین مراسم تشییع در طول تاریخ محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farsna/448828" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448821">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jukcKazZ97XnBM6S7_U0XHf3LZ1gd6SPSysWNgjldfbXdLBP999z4k9UpyrXESqiC3wQzk0IDtp17VujXWEVRu8_g7Bp_LK8kvoQqHPGUQk-cKNeMofrBrfE2QzNaSxutiS9A2DNHQ8VN9VrjpB7mkD8JVFx4YcDzSpBO91Y72owmIZdyMmdNLWtwLGyFAFuJG4BKGSECTg-2WAavoCqrBwTMoNtct4fOAUguprvy-dy4a-cqpt57TcHJ2xj1KZtL7tgUpgVE6B3UgmAUn1jCH8zO1jsgGKFVBo1-_GlA93e6luyXVNBH0x21xPZTkQBYsemjWzMnBnJorA77ohKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERWsSNtXUw9OT30K2mMSdAeWgOG9UKo0AQUHZ4FR8Yqc005VoeXgA4uREiIyHRJgIyJEjVtcblpoSMLrJGkOrdzf3Ms6Hhcdvn9Ee4OqXAT1JGs6631LLcSReCdnckPT15JCvqQv5S0gw4iGY6Ua5kcNrY1Cq8mcFdA7TeAU2LIhjCb525c4IWXrPcya3Wq7fw5y5ujc9pzYRJ4Pm3ZPUJ6VdjILc8vc24xdDtnarS18J2zogGk3T2CfCHohuqOX3baDx_1008NeEV8Sz4FkhZmRHNIen80FlzGs95NfenY-i3uW5rKeilSt5lsH89u7mCdceC_X1I8Sncr2QAeYbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SI8Vuf7yLXGY24m1zmOgQiecJRi4l_wRh_wmUTbkiWmqUKay04FdhE4TSSpkL08MoKt2T4_79lhzMXZoeeqGLNM_4CDfP-INEidlukQ8PTVCshQbXse3SVrUCi_0iPmXt1Oq2CP7pqqiG53RdvifAR_VMUqbmMLKGEACpagHJXeJQAqU9FsEUhwkjdqfdoffbWSCnfwX2hp9rYAc0fkeGOFyNDzKBgMa1EvD2a_z6CRjeYOOhp-QYkv7-rzP3sy3ct-am51hBRIHUd2jr9YNn-d3xBk8lZ009FSxpEdA6h9J3ctWGjbKbgEFnXPncSbL15EAF5j0aSEXi2FY7lJHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNZYVtSQXr3PbEASSZqmcwVVUNFFgb7ebJ6RUf5xMDvLEWTRvY-SkSMG1zZTisppFsxfvPjYWUP6VcgVqv7nmexrZfa9BtVEijEfHgyhJiJdMQRY7BSsJHJo2ylHgdE7NUq-BefGnSCrbNCLwlW9nAOCIXWDoNIQ5xCCq47VOMsfSk_iaAq4_btK9ilHDuVyQjSAHAqp32rTYfeog8p-nkzddc66UcEJ-0gxnwIWDS5vqCWR3wt-XyvK1l_ZPr1E43-wgqikAF1aaOnOYR_EwnT_M6NLzELsAdFKoCu9SatqlSFle140j9RpDfJqWDpf61kZCR3g6pzUrNuyTClcdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HY0pLh_sxAsWlZIIVqFqaHqZ997AlKrKsws3MaDrKanhnOPQYOUqzT_WHrIclZ3Y0CI4SD6GTIkuVkrcBjqUB0_ft-GH3VnBNCoS3xeV3Hnsd2cED54OC3_cOw8mhnWHCPXocBH7RFWVtqTiNalLZ_6dKiq8dyVSnVSGxc-aVbDlGWytGcW2HFxN2uCIxK-g2a6_APmz1aTFlfc1LhikqUD_tPrCkRH_bW2zqLjThiyfVSiMZZx1_MQ2uNEusrEb73MwP0AlS5OqQZzY1YnYRwXE9Pqr8sF_GNMPCMd5LFO52WY9R68KSbKpb1ZK8KoyKpAVHTFqs14xQxlk-ce9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWltZzSaSLI--8XEMWg1ujSi2I6T8eanmgutvJG7yETnuCQCmzuL8SHKx-VVmwjaUXVO_hdSU-8f4vQRHHFb__TonDapevQ4WHi3WG9WgX-sPPDFY9wSZx9Qv85Go2qdKc_L51-H7Dj2KJ04m8IJBvdl_GHEw6OIvdzJs72u7PFp-47XJZoGw0CAX0DZbOK57n7aGB58iOwLHT-YEode0mpgdIqBiYyZx_EryO5pViROnJhcY0cErhrm6vcRXs6RwdFro3xjnkre36EIqmsfjHANrDDI5hy9AD0CLD-TsDh0C6bRbztHwnW_UxfQqwT5qbhLl9Cyiujtb8Tia6QLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEzOoHu_qvXFIZXNgzUOo-6KjPSfMM9ChmB52_MJg4mpFkbGe6R3QE1UsoR0DB72ZLEdmONm2GNgP3dCRCkOJoJQ0roDtpCL5ZFnt7FtI8NWtw2BLb1hajnFmc-VQipNly9WB89Lhg9c4BklO5hUlRAFTmLmeYnFVJc0BmbVB6Pecbdgh_Gi4t-daQuOjxSM4s9d-ZJ6XAchgQ38utJjOqt8xdkfExGHoQRhzjgqy70FfzsN8vzXpziMvqJ2AeIICzfNjx7a7lSgGrS9r5IqqXTabSozQTKOlQuuO1xSTgeAuLvH2Rqa66vfukq4LoPjNbXGXd5uAz_7hU3C_HmoSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌های وداع آخر
عکس:
مرتضی مطهری‌نژاد
@Farsna</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farsna/448821" target="_blank">📅 22:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448820">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5371985f25.mp4?token=TvcwzsjMDc9bI9uPCqp8F6hpS9-1Z1KNwaEXgmcDBNge3WcnzBkCIQHFB_gfh6YHFIP7E4LbDkPi_o-KIp5hhQtcMZmFije6xWD8lamm-fsGLDjWhmtkXGMfHygRmRvQoWNqD23C9xv2VVDWZwM2Vx8gJZsfXdpqmz2sSLW7KjFLcbff1LtyPVEtp9HZ91ZBnN92yEBRhjyFJfpkd7atqtJR9EFV-7Z7xl5BWhCrtVnlhDj1C2IHzt6pYcd3gre3Rnp7fot43rWlm0Q1iMLMOXuqCPciNFP0OFycrfliZUlgHeklcIsD7a-oF1rMTi-YIiiMv1Gupj0BFq7T10vx-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5371985f25.mp4?token=TvcwzsjMDc9bI9uPCqp8F6hpS9-1Z1KNwaEXgmcDBNge3WcnzBkCIQHFB_gfh6YHFIP7E4LbDkPi_o-KIp5hhQtcMZmFije6xWD8lamm-fsGLDjWhmtkXGMfHygRmRvQoWNqD23C9xv2VVDWZwM2Vx8gJZsfXdpqmz2sSLW7KjFLcbff1LtyPVEtp9HZ91ZBnN92yEBRhjyFJfpkd7atqtJR9EFV-7Z7xl5BWhCrtVnlhDj1C2IHzt6pYcd3gre3Rnp7fot43rWlm0Q1iMLMOXuqCPciNFP0OFycrfliZUlgHeklcIsD7a-oF1rMTi-YIiiMv1Gupj0BFq7T10vx-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الوعده وفا امام رضا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farsna/448820" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448819">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d23cdb6a64.mp4?token=ZDRDsJUSh_15sx1dJs7K3dMyGVDYRgl3GsYI9nv5BQgE7hk9QRKehn2Nc9xpnZCy6EWmPAaNp5mCiTt49DBaBxKOe8YqPgnysumOYb4waYFMeVyrLpBIsI1msz3FhOsX0cyO8MTQAgz6xIEE8y9-1y0QRj-KlRglSvM4UetIl5Ezsek2yE0koLU0f6lLUb82lI4KiBlTVY_k_jwiWSMBHQGob7W1kJJV7gBy_fdtBH3lD4SkIQ8ua-32m2-7q3uEgBb1t4oCXBBqYwieoJjVQ3Blp7uIsp118NhOWbBModmlmjVgvMzNH5xw-sC3ZKvL3oH0RpFhxRFqenMTa44u-m0L-bhz-vdJnw_R1aXnM9wjCodsoJxsQ6IiXxHYdgmIZFOoqys53QU_3mFRDoXIqj7ArqJsysJ3HGIHJJh0gHwih-YFdVoMJdvigcturCy1vwRUM8QvZ9AAeSPhUVxwafPMu_lYdINGkFU5VwA7w0XikDu9scHnHBboafI4pQEDZcDqo8xBOrF7qP59v1XosY7wKRUCNFgccH1qRR2yCG7yWjeZSv0i6rJq_ZJVOdeyaFFf9mhQJNzOvuPXK7acxpFOin4p7RXi5YfU21EjN4bZfLWFCqVquY26cry_-Rls06ryuZs_APo4R4-iWB3vOzqg68dkQsGgeGRq_7vw_ZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d23cdb6a64.mp4?token=ZDRDsJUSh_15sx1dJs7K3dMyGVDYRgl3GsYI9nv5BQgE7hk9QRKehn2Nc9xpnZCy6EWmPAaNp5mCiTt49DBaBxKOe8YqPgnysumOYb4waYFMeVyrLpBIsI1msz3FhOsX0cyO8MTQAgz6xIEE8y9-1y0QRj-KlRglSvM4UetIl5Ezsek2yE0koLU0f6lLUb82lI4KiBlTVY_k_jwiWSMBHQGob7W1kJJV7gBy_fdtBH3lD4SkIQ8ua-32m2-7q3uEgBb1t4oCXBBqYwieoJjVQ3Blp7uIsp118NhOWbBModmlmjVgvMzNH5xw-sC3ZKvL3oH0RpFhxRFqenMTa44u-m0L-bhz-vdJnw_R1aXnM9wjCodsoJxsQ6IiXxHYdgmIZFOoqys53QU_3mFRDoXIqj7ArqJsysJ3HGIHJJh0gHwih-YFdVoMJdvigcturCy1vwRUM8QvZ9AAeSPhUVxwafPMu_lYdINGkFU5VwA7w0XikDu9scHnHBboafI4pQEDZcDqo8xBOrF7qP59v1XosY7wKRUCNFgccH1qRR2yCG7yWjeZSv0i6rJq_ZJVOdeyaFFf9mhQJNzOvuPXK7acxpFOin4p7RXi5YfU21EjN4bZfLWFCqVquY26cry_-Rls06ryuZs_APo4R4-iWB3vOzqg68dkQsGgeGRq_7vw_ZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب بعد از اقامۀ نماز به‌سوی حرم تشییع شد  @Farsna</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farsna/448819" target="_blank">📅 22:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448818">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e3dd3673.mp4?token=kTsSzK0fi3Wi_MJmQIjdAiPsfKY8_7hoDW-B8PUMCEThiSTylGHJ5K5v1y7T5kc8qQaWqd1rF0v5sxemC8q4XEvZoz_mxc8VyV4U9HGcygmXC88sUmnOKl_loxVtPPId06C7SF0YMfIM0NwwTgB3wVAhrNgCTcXwAMbyd9oDb3yRd_XKIXqPTwNvrXpWEdNJo_8gebzshBIuj8j743p17HQqhdWnF3tHeNOkVZiSvrJz0xIcWTEIFjaY3PxqVWem0bXqD7QEyOd1My3Re6jcND9Prfm86LVr0CLWncRmCNMolG51gjPiAwchGHefYfoJ-0Wd7ihHl5Sxw4cczKr2wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e3dd3673.mp4?token=kTsSzK0fi3Wi_MJmQIjdAiPsfKY8_7hoDW-B8PUMCEThiSTylGHJ5K5v1y7T5kc8qQaWqd1rF0v5sxemC8q4XEvZoz_mxc8VyV4U9HGcygmXC88sUmnOKl_loxVtPPId06C7SF0YMfIM0NwwTgB3wVAhrNgCTcXwAMbyd9oDb3yRd_XKIXqPTwNvrXpWEdNJo_8gebzshBIuj8j743p17HQqhdWnF3tHeNOkVZiSvrJz0xIcWTEIFjaY3PxqVWem0bXqD7QEyOd1My3Re6jcND9Prfm86LVr0CLWncRmCNMolG51gjPiAwchGHefYfoJ-0Wd7ihHl5Sxw4cczKr2wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اللَّهُمَّ إِنَّا لَا نَعْلَمُ مِنْهُ إِلَّا خَیْرا  @Farsna</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farsna/448818" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448817">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0ff55c55.mp4?token=rNp9h0Ko7ChyUmYeGidu_XylPGPIdQ5xew5RSH-ne5oOfyYSk5Cg6s_OwMZJuSCmxKj_h3xDZg5MosyWzG4Af_8MffwWy2dqoA-cibnTnwqaIcCFX9fQqJ8oLnzIxkFWJ8HnKi39MJWO6AjXlv0khzFupJaY3ITUH8I64L5VVOVBGnnwos60GMFsUy2jFfF_mSL56R-RhjqkrpOvdomiXALi3renmNwZauBSOa8jGnT1iuh_qyuLkKYJGkqRMk4eK1GGEw8WMPFx1q3fY_Edo5HOdn-dzEwiZvAZ8m6DIpAtT4lyJq_iC1fFJjj6YM6YKtBj5SBH2ix_o_vRKwmVGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0ff55c55.mp4?token=rNp9h0Ko7ChyUmYeGidu_XylPGPIdQ5xew5RSH-ne5oOfyYSk5Cg6s_OwMZJuSCmxKj_h3xDZg5MosyWzG4Af_8MffwWy2dqoA-cibnTnwqaIcCFX9fQqJ8oLnzIxkFWJ8HnKi39MJWO6AjXlv0khzFupJaY3ITUH8I64L5VVOVBGnnwos60GMFsUy2jFfF_mSL56R-RhjqkrpOvdomiXALi3renmNwZauBSOa8jGnT1iuh_qyuLkKYJGkqRMk4eK1GGEw8WMPFx1q3fY_Edo5HOdn-dzEwiZvAZ8m6DIpAtT4lyJq_iC1fFJjj6YM6YKtBj5SBH2ix_o_vRKwmVGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز اقامۀ نماز بر پیکر رهبر شهید انقلاب توسط آیت‌الله سیدمصطفی خامنه‌ای  @Farsna</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farsna/448817" target="_blank">📅 21:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448816">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f925c851.mp4?token=E8PcV8Ebo5wvmq7OnDIDxgaPtleaopNwSimzY-DDIESWKrX3af6WW16U6gDRKkpqxd_gYs4hoaxLXTzJlKNz0UltAWyVyA1EvSu28dx84DwD0kmtRTE-T1ftfUMMKTdlfUGPrOyQoXuqT7IUUl6xHi5pkv4BqHryM1I496pBk2WzMp0uyQscMWtg13FuH0Ffmprarbed8ipJKTRsxUVD_ONRGowMV_18TOqRXH_U5MmViN1-16huBmQUwhP_LnW4lkqt1RfHsxVbyv1QOMK1hB1RqzxjvkgUGiFL5v5Sdo5j8T8QpOKWHVUUqxJgKMwhYkDpl1T6PYIjwL5EZ9LgPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f925c851.mp4?token=E8PcV8Ebo5wvmq7OnDIDxgaPtleaopNwSimzY-DDIESWKrX3af6WW16U6gDRKkpqxd_gYs4hoaxLXTzJlKNz0UltAWyVyA1EvSu28dx84DwD0kmtRTE-T1ftfUMMKTdlfUGPrOyQoXuqT7IUUl6xHi5pkv4BqHryM1I496pBk2WzMp0uyQscMWtg13FuH0Ffmprarbed8ipJKTRsxUVD_ONRGowMV_18TOqRXH_U5MmViN1-16huBmQUwhP_LnW4lkqt1RfHsxVbyv1QOMK1hB1RqzxjvkgUGiFL5v5Sdo5j8T8QpOKWHVUUqxJgKMwhYkDpl1T6PYIjwL5EZ9LgPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور فرزند ارشد رهبر شهید در حرم امام‌رضا (ع)  @Farsna</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farsna/448816" target="_blank">📅 21:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448815">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS_TyBnPAu7AL-GkIIq6wI5nDjRPc3iymVWMuSha8ypOvGPm2RUDdjyySXIenwNW8C-yOBsBBXkCs5RoxOaitA6qTkqtZY5ba483_3qcU1HgdmpT2U5Vss9kHDSxPx2_YHgK_5XDpAMVmUs76Qrxw21NmvDedqbYYsJ9ruNIsawfDfU7KjbVBVS1LXohOvDfWMtUWPQ1pyAL-Q4Noycy7CLDTP2xI7S6Ew8z5G7nkNf3loy7tVySk9jzRO4X6uRXX86k26VxEe0o0SvwUDIlG90O2xdNWMU7_uwmlIevnj3eIayrqt8E-akdtvfAZpygGqP9zPckSLk5AKEvzZ9J-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
دیری است زآشیانه جدا مانده‌ای «امین»
◾️
غربت بس است رو سوی آن کوی و بام کن
@Farsna</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/448815" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448814">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsA_fw6ZgcJgxA20GKsYseKgN23A7GcER9RbZJfSFxeyYN4XWAzdTeBY5SAqHEXiUG6b-BR50km1gPOuWFpx6EtiObwhqKxPo7VwCMEKKgA4CQBvd61tCGCS7g5XGA6i__rfiNNMfrJhaArXamdfu-jhqlmfSF0XP1eeT4446zh1lzgNrIWtNKjXdMsr0yBRksB0opXvVjSx1iD1n6YDFozRmdhJISTKV8GEAKjET1INJNF1Ox7fLw5C9ihl_A7Vlncxqi7mtSlTDdcMe9bbenaTmDyaQmaa5ZH9_W8ROVvl48IMjo3YdgQYIEevrVPFL-VUqkw9phcgTbJM8p6OMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راغب: هنرمندترین رهبر دنیا را از دست دادیم
🔹
مصطفی راغب، خواننده عرصه موسیقی با حضور در تشییع رهبر شهید انقلاب در مشهد، نوشت:
🔹
«جمعیت عجیبی رو امروز در مشهد دیدم؛ خدا به هر کسی همچین عزتی نمیده
🔸
پاک‌ترین و خالص‌ترین رهبر دنیا و از همه مهم‌تر هنرمندترین روشن‌فکرترین چهره‌ برجسته‌ دنیا رو از دست دادیم
🔹
من از کودکی ایشون رو دوست داشتم و این روزها به عمق دوست داشتنم اضافه خواهد شد
🔸
تاسف برای کسانی که هزینه کردند تا این بزرگوار رو در چشم جهان انسان بدی جلوه بدند. فارغ از اینکه عزت و ذلت دست خداست».
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/448814" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448813">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29151e8f4e.mp4?token=aDZhWZkYXStN922JCXE4IqgP6nG50LgyhLDgYdIRGsevh7Jo8x2rs__ZWg9b6_m2aU3_zni1Vd4DhA7NAW1F0RfBBVZ9e1YMja494Ye5nA_4aRs6G5NVh5Bu953G1diBMOfradK0aEtCAiOAbfE4krxNeCJVXZcvdkidRcxMfyvKyoETAvI04WPvB0ZtmeJNyT1rhSsJ3ZwTW7yiWBGg6sZctaXQP8C1pf0vZBjEaChU-Baj8-pUWuqCdL7Mvs0mlafVQLKUi7j10jHZ8qDzUIj2j2DnlNgXK6wnsVIzqDOkPSDlm7ULEoOuJrW4leBRQfqaVERwS9WwEtl55QLRTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29151e8f4e.mp4?token=aDZhWZkYXStN922JCXE4IqgP6nG50LgyhLDgYdIRGsevh7Jo8x2rs__ZWg9b6_m2aU3_zni1Vd4DhA7NAW1F0RfBBVZ9e1YMja494Ye5nA_4aRs6G5NVh5Bu953G1diBMOfradK0aEtCAiOAbfE4krxNeCJVXZcvdkidRcxMfyvKyoETAvI04WPvB0ZtmeJNyT1rhSsJ3ZwTW7yiWBGg6sZctaXQP8C1pf0vZBjEaChU-Baj8-pUWuqCdL7Mvs0mlafVQLKUi7j10jHZ8qDzUIj2j2DnlNgXK6wnsVIzqDOkPSDlm7ULEoOuJrW4leBRQfqaVERwS9WwEtl55QLRTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور فرزند ارشد رهبر شهید در حرم امام‌رضا (ع)
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/448813" target="_blank">📅 21:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448812">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hldeHULfl18IA8Dzxa-L8ZuCrG920wFPCOMnbIqkGfquSnldbZLBtnwc4fdas-fFw6WZrZKavAIvMBXyH2uDCnGyMIFfGCZ8ole1W_lPUF66UQKfL98RCVGUfS8HK8bYqrRe0-DbHLzQMDACg1rg_EL986xLSyNF62yKWhGJJaPnIHHOXyJLNMfI24dFfAjE5UHb3ZEP9YEi9nDVlw8TsJI2NtV6OFMi4z25tNTmp2XDcmz3xYmo7ZKX7nzpF08ELTZspAP48R6WosRa1qmb-W4Q9JcAOtfrg5GelPQMHBkloYCn_m3tzoelN-rWID-PYGJm92iT8ZJ50sjX-ADWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ با پایان رسمی مراسم تشییع، هم‌اینک عزاداران در حرم مطهر رضوی و خیابان‌های منتهی به آن در انتظار اقامه نماز بر پیکر رهبر شهید و خانواده ایشان هستند
🔹
پس از اقامۀ نماز، مراسم رسمی تدفین پیکر شهدا در رواق دارالذکر آغاز خواهد شد.
🔹
زمان خواندن نماز لیلة‌الدفن…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/448812" target="_blank">📅 21:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448811">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da8747021.mp4?token=uMVHPvXIU8j2VHH-rPcPkg7Kuj5HKD7IpGMo5oLjvmxn6CIRmf2lneRENsiY6bkd8NjhCYrMRvFm6ayDSMkePoISSXXKXmr4cGo4vNj7RfqE7cx27_YnxSwdWvM1vKMTvzpIKRnHPX0S1T-wX9p7hR5XKjuVaYRQE3J9QNmINGe4moX_mTY07KNkQf3APT8fh-dE4ComK4Dpea1moMLRkSSQPq_AQlJgI_y_yYNooBU2vJsJAie4lfK8Gn6AAB3D3i8sC2yO9pFpHfQRFZ55aPfqQdOQIiT60vnGDMmRrdDUWPwNK9JG-5d0VUBrFCWtUQhV0MJ25yJaiJ1qBuki9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da8747021.mp4?token=uMVHPvXIU8j2VHH-rPcPkg7Kuj5HKD7IpGMo5oLjvmxn6CIRmf2lneRENsiY6bkd8NjhCYrMRvFm6ayDSMkePoISSXXKXmr4cGo4vNj7RfqE7cx27_YnxSwdWvM1vKMTvzpIKRnHPX0S1T-wX9p7hR5XKjuVaYRQE3J9QNmINGe4moX_mTY07KNkQf3APT8fh-dE4ComK4Dpea1moMLRkSSQPq_AQlJgI_y_yYNooBU2vJsJAie4lfK8Gn6AAB3D3i8sC2yO9pFpHfQRFZ55aPfqQdOQIiT60vnGDMmRrdDUWPwNK9JG-5d0VUBrFCWtUQhV0MJ25yJaiJ1qBuki9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور قالیباف، اژه‌ای، مخبر، آیت‌الله علم‌الهدی و سیدحسن خمینی در حرم رضوی
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/448811" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448807">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DfilJksrzhqD0fE8WVw0aUYSjhOQ5vFOGUvv4QrQyfZ6KewIfIad_BiwLSZtIoCGi4OayMCghlToeCWo3uWCjJdx7x8Mrp4MwsJBWfmKn-6qxR-VXxTjMcWU9Vw2perJYkROudT9x4FKDB0r94qCr7FQm1AWBPNeeJa8EnwRneY_pboiSTNIRnlBvN7SotHLavfpEcpi6yDvTpUh0tGedWwfPM70H9yNz1WKCDkGQj1HhQFAVCQMvtfB8ROxgo04NZWlGANXs2j2O-iJhO5f4jKWUpGtGUQig2srz4DH3OmAfZ7IJ_rWtnonC29-6rSOOR67BUPwbDad2l6Tdb653A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nd26rj6BX0mo33hyQ8KbwcS6xHwt3UaTZJuoLQbtjiVDZX51o5E98TgAQDPCR5m4D5FD7cIlNfOlbGGFvcv8OlhPVyPF2NCtnSdhGAuEdRXi8NPyBdvBieXBZQ5ipid07k1uI1tHh5bLIeuUn41Py2eTgC-hngRz0-rfQVxTQOV6O3VcONFfqq_OT5YeBxZsk0SBlkjCkABC1PTC49LmeRFrjqcQ1IDPALQuYMDpkVPVINKm3cfuNgJWQabjIPFEe5Op9PLmhR-hYlJWYgFSZFyHhhMeb0LInluGC3XAzg0SNw-bHOKNeARs2Ehp0nrGLcNSs0e8UVv1jxhJRS-4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivbC1adwX6uNcsP1jMhfYjPnmfgabJ2Bv-flQAC9qRPTKjELzeEASqjFoitHUJpD2rLlS6reWKd_sKls7b9Jfl3LzWAaqJ2O6KcCzKfsbfq0_eWcNDJDrnb1qOR47xyuQ8qdSik0A0xLlkH42SJ3tjAuuAxBnncNj5Yh-85cWDJ2eikLlt7VvH0Aumvn-FL2ta6FaWcdRFxFWDlhfOnWxOkA4leWpgIv0n0Z0X7LlrPf1FH0puVxYbRxc5wrDUQL3Wvm0DIAEvGOMhjFyWZpyOtzsU90FUR6JpOPnWIurd68qT1ISRZyBQoOa76_0iBQ806Px6qiR6eb6XdBQaYRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZWMc-2xmspzDWWpC1QofivVuwA66gspdlbrkufCJyugenPJj4N-_EWCugBVnq28pVqlrrjOsf96dvVZEf9uIGZj7LJGLxwD_5wmzzU0QoBUE17XN8nDVapK9wktFd23qruk-98K6KS1k_9qU11aRg8gRIVSWfJkXbY3nWePdkNuM_BNmvvMrW8vm_YKO76gRhzU1h2Z-aDD7dth-Gzzy-CsL4W46SWf0a8Tut-pbWLdZc80WTR3yHzpTtUlSny1xcCsSJrAsFqhojJJEWf5kx8Il-zDjW18WvscMlvVco43SJPxG61fPyLlYLdafRIEbkowL-d33VoI0z61XkEvlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
امروز پرچم خون‌خواهی بالا بود
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/448807" target="_blank">📅 21:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448806">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb9c4c462b.mp4?token=fF9BRnH3pZroHadr62JdiKEKrznRKxfuF6hBnmqLisHfrXCu8zkjpLpob5YmhGwvCW_8D0rRp2gAolNRFve7B6XttH9jYwNw7OnA9C4VGnpmR7lohzaYJih1qKNap9iWBfjXkcdFhOwjtX49AznEbkNt5cCOk0CrxDfn24cBVSjPNJ9lERNZpxtL6FS7ybU9NSsq255BB4pnIKD5UY8og-37AY-3fmspNTEC5jXKe3hzrANQH_chr3brVcFXrG5OrlQMlG2nPM0f5At8_PAj73SfOaFKD7VxB9-oevs8Cww-PcA7G9vO0jWnUIg-2KFyKq1D1O9kIpr8NYIu6vRI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb9c4c462b.mp4?token=fF9BRnH3pZroHadr62JdiKEKrznRKxfuF6hBnmqLisHfrXCu8zkjpLpob5YmhGwvCW_8D0rRp2gAolNRFve7B6XttH9jYwNw7OnA9C4VGnpmR7lohzaYJih1qKNap9iWBfjXkcdFhOwjtX49AznEbkNt5cCOk0CrxDfn24cBVSjPNJ9lERNZpxtL6FS7ybU9NSsq255BB4pnIKD5UY8og-37AY-3fmspNTEC5jXKe3hzrANQH_chr3brVcFXrG5OrlQMlG2nPM0f5At8_PAj73SfOaFKD7VxB9-oevs8Cww-PcA7G9vO0jWnUIg-2KFyKq1D1O9kIpr8NYIu6vRI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیدعلی صبور ما خدانگه‌دار
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/448806" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448805">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcd42908d3.mp4?token=jL4Z5TI15LPRZbjSFV5wBCm8ERkPEY1vPj9QkNm80NQNgOQsVBNWtAc-BfACq2rE_BNo90IXNwajg8S2Epgk1Suf5O82lUBRnjBJsJ7OXMBQGv_oLOjwl_B46SenoJiVLIPdtfJKTMi1EP7hpy40hrHOBVfbgXRG8zVdVenOpiCgziDO9HcwrJ_TZuHDdX2vS4bQz8udNAxhw-_03RxTrhu1qdQtwYFNlI_kQlcZTq9F2BAZ0txAD7fPYYGzr2gv-quXNUZgeM-ehjFOXqUFdtaMdgu9RS1-VyR60QOudQ0sDn-Cl2izwyrN-Kc628wOKGPsz4fT3SfPVq2-srxQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcd42908d3.mp4?token=jL4Z5TI15LPRZbjSFV5wBCm8ERkPEY1vPj9QkNm80NQNgOQsVBNWtAc-BfACq2rE_BNo90IXNwajg8S2Epgk1Suf5O82lUBRnjBJsJ7OXMBQGv_oLOjwl_B46SenoJiVLIPdtfJKTMi1EP7hpy40hrHOBVfbgXRG8zVdVenOpiCgziDO9HcwrJ_TZuHDdX2vS4bQz8udNAxhw-_03RxTrhu1qdQtwYFNlI_kQlcZTq9F2BAZ0txAD7fPYYGzr2gv-quXNUZgeM-ehjFOXqUFdtaMdgu9RS1-VyR60QOudQ0sDn-Cl2izwyrN-Kc628wOKGPsz4fT3SfPVq2-srxQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امام ‌رضا(ع) عاشورایی شد
🔸
مداحی مهدی رسولی در حرم امام رضا (ع)
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/448805" target="_blank">📅 21:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448804">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bee60265af.mp4?token=r1gOsln_ygxrzVGip3hTaYDlvb_vG24Q7Vc36xuaV6AUua-m-daamgqhlOi8_Kk553mLo26mhTlX6XzsBkGetcMHflY8EBvJjdsnIlqGi_5tiEe9uEARKsj4HD-bR1xPdMi02eJdrW3HcIACuD-L81gQ8gpdEURn69az7mXgsVoZiPAGIFECvWQs312HQGxylsmmQAXqwxv7hi-bicess4-BEN8HddzhPuRbyMgwVN9X5BGuxRrXj5LiEBMpQCUODhX_oQrBBGiphZwqdfkntZQhtstHavNdTszv5u157_1AwiNEe7UEiDbaWFwS4TE5xDKmhv-gUY3ns4QCBdIlK57E4vCnv5BVfKvfbOD0CPCI4-ECOuVK3aAwozzIBxyu79P4YkyQQJcAWOdqgT6kosY4DEFiZiYCZOKQXEJRpjLKTzPFnE8h8ftU8tNXzgfByknfDeXbv7QFHCV9wOvDZdklZUklQ5OTkem-WNAggDRakLH7Nxjkq-GNcYPb-AieVdTLr9miMxO8dpgJfUH4tQ9NeH20QOXqf0a01xlunygah8Dz7ohvK5NkDaDAf-xuZscroxOMyNDmFEn9CHjSjjgTJZsOhjjSdlLLmXBTBqhESdqkEC2AWxif7bmj2GNYoA9ChCN7i13kqlWs6-SQ_72utbBYJy2M3Sdu2avqpzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bee60265af.mp4?token=r1gOsln_ygxrzVGip3hTaYDlvb_vG24Q7Vc36xuaV6AUua-m-daamgqhlOi8_Kk553mLo26mhTlX6XzsBkGetcMHflY8EBvJjdsnIlqGi_5tiEe9uEARKsj4HD-bR1xPdMi02eJdrW3HcIACuD-L81gQ8gpdEURn69az7mXgsVoZiPAGIFECvWQs312HQGxylsmmQAXqwxv7hi-bicess4-BEN8HddzhPuRbyMgwVN9X5BGuxRrXj5LiEBMpQCUODhX_oQrBBGiphZwqdfkntZQhtstHavNdTszv5u157_1AwiNEe7UEiDbaWFwS4TE5xDKmhv-gUY3ns4QCBdIlK57E4vCnv5BVfKvfbOD0CPCI4-ECOuVK3aAwozzIBxyu79P4YkyQQJcAWOdqgT6kosY4DEFiZiYCZOKQXEJRpjLKTzPFnE8h8ftU8tNXzgfByknfDeXbv7QFHCV9wOvDZdklZUklQ5OTkem-WNAggDRakLH7Nxjkq-GNcYPb-AieVdTLr9miMxO8dpgJfUH4tQ9NeH20QOXqf0a01xlunygah8Dz7ohvK5NkDaDAf-xuZscroxOMyNDmFEn9CHjSjjgTJZsOhjjSdlLLmXBTBqhESdqkEC2AWxif7bmj2GNYoA9ChCN7i13kqlWs6-SQ_72utbBYJy2M3Sdu2avqpzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقا فدای ایران شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/448804" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448803">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5a63ae6f.mp4?token=IS4yHa2BixyPK5bnwCLAnEzSK9ronxTZ1Z9QgQkqS2dTqGvY4jmAOIyy-jsmreb414akYi6QurBpPlfNwGjr4OX_at4_c2w1Qtr0y8ReUzfZRS_CfreyW9DMv0CvR5Ug6FsAxGo5oKxFLjgxurcCZTlVnwVVrNetsgFXtj60kv67sxhDG6j-szsHzvU0gKzDibwClAnd68CvFN0JdJXXySS03AZk0mSbVnrAGvW1UpBfmrSoXtisTYFYtAHHqsTopW3kq69sH6pZF_puHoBpfAmETrNfr439dCHPeLCl8ZIZN_2iPloYr5dpUN2bKvqa4ViDEJrTLA9MqbjTWhkIcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5a63ae6f.mp4?token=IS4yHa2BixyPK5bnwCLAnEzSK9ronxTZ1Z9QgQkqS2dTqGvY4jmAOIyy-jsmreb414akYi6QurBpPlfNwGjr4OX_at4_c2w1Qtr0y8ReUzfZRS_CfreyW9DMv0CvR5Ug6FsAxGo5oKxFLjgxurcCZTlVnwVVrNetsgFXtj60kv67sxhDG6j-szsHzvU0gKzDibwClAnd68CvFN0JdJXXySS03AZk0mSbVnrAGvW1UpBfmrSoXtisTYFYtAHHqsTopW3kq69sH6pZF_puHoBpfAmETrNfr439dCHPeLCl8ZIZN_2iPloYr5dpUN2bKvqa4ViDEJrTLA9MqbjTWhkIcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یکی بهم بگه دروغه...
🔸
نوحه‌خوانی مهدی رسولی در حرم امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/448803" target="_blank">📅 21:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448802">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6100f7673c.mp4?token=SvicBLLj30fS1T0mQQfiG957BUFCRlMVMsXdrD5DL10vYI_a_Yw9A3B-JQqj37WWtSGox7nySNaQToWDvysXcd7FmJ2YeldQeL3N8fJ873icEPHWlZdT4K3oEaDYrl6dBO8GDNjPfV66_wlk3TUVEr7OQNWY2mr8pgVT3knaV5yKLBgTteEE1fBoGxVxGf1fPjqg5Wwl2eiiK-k7vNvJRIDs-2zpXGN8ocKr2e0DgNUctBS74JreSyoYr0XV-YxKJciIPmdJS0kpv5z2T4H0hS1Fet2pXiTyVB5Mi-jNHLDu5TITY2PQZ4rEphgGN2UZKyRsVQcC4xDgF_5E-9tmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6100f7673c.mp4?token=SvicBLLj30fS1T0mQQfiG957BUFCRlMVMsXdrD5DL10vYI_a_Yw9A3B-JQqj37WWtSGox7nySNaQToWDvysXcd7FmJ2YeldQeL3N8fJ873icEPHWlZdT4K3oEaDYrl6dBO8GDNjPfV66_wlk3TUVEr7OQNWY2mr8pgVT3knaV5yKLBgTteEE1fBoGxVxGf1fPjqg5Wwl2eiiK-k7vNvJRIDs-2zpXGN8ocKr2e0DgNUctBS74JreSyoYr0XV-YxKJciIPmdJS0kpv5z2T4H0hS1Fet2pXiTyVB5Mi-jNHLDu5TITY2PQZ4rEphgGN2UZKyRsVQcC4xDgF_5E-9tmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا رسانه‌های معاند از وحدت ایران وعراق به وحشت افتادند
؟
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/448802" target="_blank">📅 21:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448801">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ae2384a7.mp4?token=qVaM9G8AKbm50BSLOa8G_E4_bKYwFbGjriU1qgDf6FqldQIOAtzdeABP4mX4qIja9cSViYNo3ulf8iVMpdHEPewHL5KKBWE550Y-pc-BNr8RF5X2cc4M7ZkFS80DTnHHMZCPRKx4iVW_exXnL83thlbrS8SibtnU0yjUS4QIvq0IT5c6H5nIp-d2sa3OZN6aHe9R-RWE_pFVeD_XG4gtB-YQRYD-lOekIClt4plWfuJoTbdjMRbQ_diKbsKSxsjp6zvtfl_he4pbey0u1pGVL3Q-xwsJqHIWbO_61OjU35qhhZdxKlJnlqWmTxUKTdGxgV6C7i6invxpebLY_HecVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ae2384a7.mp4?token=qVaM9G8AKbm50BSLOa8G_E4_bKYwFbGjriU1qgDf6FqldQIOAtzdeABP4mX4qIja9cSViYNo3ulf8iVMpdHEPewHL5KKBWE550Y-pc-BNr8RF5X2cc4M7ZkFS80DTnHHMZCPRKx4iVW_exXnL83thlbrS8SibtnU0yjUS4QIvq0IT5c6H5nIp-d2sa3OZN6aHe9R-RWE_pFVeD_XG4gtB-YQRYD-lOekIClt4plWfuJoTbdjMRbQ_diKbsKSxsjp6zvtfl_he4pbey0u1pGVL3Q-xwsJqHIWbO_61OjU35qhhZdxKlJnlqWmTxUKTdGxgV6C7i6invxpebLY_HecVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک فرمان، میلیون‌ها روایت
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/448801" target="_blank">📅 21:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448800">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2575953999.mp4?token=Z4zxCIKKWdbF__UGOgig_B3dxD1liwdnJ0Le1HlHwX16zf8p9qoYYRUISZinioVj9xEjEd3Cuo4ltTeBU0a1atkl-_E9wJCI9ftk9b2AsjEteDu9FHH5iaJCh4OLKT2vB2I-5c3lRKlx9DIw7soL1eI9oIxxTEhkgmFbNfXzyFFdohRbR16eH7BdSzNKkaegbshDsv14gpgxzz4eTx98RAoAo5q3ajBW9_C1v-HYXYtNbpsIY5lTFdrWLxKK-OIpoZps14LQTinsQfjiKAFKn6v5COj6_GxM2ZJByg4JdJO0TrdOfKGWrBLpy1fYLbTFNk3U76M5qJ6KKx5bcAS6GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2575953999.mp4?token=Z4zxCIKKWdbF__UGOgig_B3dxD1liwdnJ0Le1HlHwX16zf8p9qoYYRUISZinioVj9xEjEd3Cuo4ltTeBU0a1atkl-_E9wJCI9ftk9b2AsjEteDu9FHH5iaJCh4OLKT2vB2I-5c3lRKlx9DIw7soL1eI9oIxxTEhkgmFbNfXzyFFdohRbR16eH7BdSzNKkaegbshDsv14gpgxzz4eTx98RAoAo5q3ajBW9_C1v-HYXYtNbpsIY5lTFdrWLxKK-OIpoZps14LQTinsQfjiKAFKn6v5COj6_GxM2ZJByg4JdJO0TrdOfKGWrBLpy1fYLbTFNk3U76M5qJ6KKx5bcAS6GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایش تشییع تاریخی رهبر شهید از زبان رسانه‌های خارجی
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/448800" target="_blank">📅 21:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448799">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944512f8aa.mp4?token=E5hxNUV5767OICSB0WAAra5w4IBJFT7XNsjbRgQf6nB-FchoY7zQysJLrVokSbwTVUQ4VzScVB_VO16Stq5KXTVuDXLc5Dp7AP8-KSCixU9-MxjRDxB69e6iP7keRflPRhFJXWCgQC_BD7bdXOosFyaxQxJlHY0Dw69Idl2UfCPj56GyhqKjsP-b4r4cvo5TvR30TaN116dbai-lOHOg-vxNrbWoqD0PF7IvWRwl8nCX3flgRVPXpuwyUK6LjdNgHVoDxvq45F6CYe_3Q1pyJ7jR3YDMdZ02akVfgU5lBPaduC99BoeZ_UF_ERAklhS6ZzOmAdB5ljCWHf5WnRBRSBLFI8CIPfv9AEMsLqZjbAIHEKJB2_wAg1uhMUWalISSFxVA9pf7ClCZU9nlqkbPjfFlp13-BWJUZvwX5qB3_3grUVIaRLrvNNiAjMH-JiSfZt8cyT_e-s8YoGWy1wqf2cwf5tTTH7NoiHnMfwV2nWJ5XK_EHFf1mnccstGmCy9Ozh5z88zOu6B_WnVelmPZ639w6nOEI1H2N0nTbEhVZohtWQ2Nl8og0rmvi8ldD9Jbwn_0eV8EIPL0RltrJrpWaL3bDSUrRNgfidW6pAOfnr3cHFcT4rA2ymv7o9hodqK8ANOoI-ABu0S7onOP6HjkzJRwVPGirDpXkWYNrNS_6ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944512f8aa.mp4?token=E5hxNUV5767OICSB0WAAra5w4IBJFT7XNsjbRgQf6nB-FchoY7zQysJLrVokSbwTVUQ4VzScVB_VO16Stq5KXTVuDXLc5Dp7AP8-KSCixU9-MxjRDxB69e6iP7keRflPRhFJXWCgQC_BD7bdXOosFyaxQxJlHY0Dw69Idl2UfCPj56GyhqKjsP-b4r4cvo5TvR30TaN116dbai-lOHOg-vxNrbWoqD0PF7IvWRwl8nCX3flgRVPXpuwyUK6LjdNgHVoDxvq45F6CYe_3Q1pyJ7jR3YDMdZ02akVfgU5lBPaduC99BoeZ_UF_ERAklhS6ZzOmAdB5ljCWHf5WnRBRSBLFI8CIPfv9AEMsLqZjbAIHEKJB2_wAg1uhMUWalISSFxVA9pf7ClCZU9nlqkbPjfFlp13-BWJUZvwX5qB3_3grUVIaRLrvNNiAjMH-JiSfZt8cyT_e-s8YoGWy1wqf2cwf5tTTH7NoiHnMfwV2nWJ5XK_EHFf1mnccstGmCy9Ozh5z88zOu6B_WnVelmPZ639w6nOEI1H2N0nTbEhVZohtWQ2Nl8og0rmvi8ldD9Jbwn_0eV8EIPL0RltrJrpWaL3bDSUrRNgfidW6pAOfnr3cHFcT4rA2ymv7o9hodqK8ANOoI-ABu0S7onOP6HjkzJRwVPGirDpXkWYNrNS_6ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسمان دشمن در میانِ شعله‌های موشک‌های بالستیک
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/448799" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448798">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7e483608.mp4?token=ae1Gcul_DEStwaeIfCWEw16dtEDzGuQxEdir2ioMj4DAFFdjaWLSCfo7PqnyFwxliIdCgO6STCfmSQGBOu0xmUdCg9wIVZdENACQOXet_SeVGs8aPsvRSv90S_slIkVM1UxPjNgMxkn4fWzlao6W1OvC7PMp4OBjmMnUj22YsM_-eRdHuEmw9BF9-v19iWULCRSpYdx1PM_NZOcyC0d2cdiUwxhE8gltOv9jtfu8MRoJ0w9jUo0sDJU2v2Dpdz2PHz4MfEx9RLuklouFukZ03_lbpOEw0MzkmYrRxbHE_5RIsyFFvT-0I7KbCxWI1LCYK1C7LHwTg7OhxDcfkk4t_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7e483608.mp4?token=ae1Gcul_DEStwaeIfCWEw16dtEDzGuQxEdir2ioMj4DAFFdjaWLSCfo7PqnyFwxliIdCgO6STCfmSQGBOu0xmUdCg9wIVZdENACQOXet_SeVGs8aPsvRSv90S_slIkVM1UxPjNgMxkn4fWzlao6W1OvC7PMp4OBjmMnUj22YsM_-eRdHuEmw9BF9-v19iWULCRSpYdx1PM_NZOcyC0d2cdiUwxhE8gltOv9jtfu8MRoJ0w9jUo0sDJU2v2Dpdz2PHz4MfEx9RLuklouFukZ03_lbpOEw0MzkmYrRxbHE_5RIsyFFvT-0I7KbCxWI1LCYK1C7LHwTg7OhxDcfkk4t_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» در حرم رضوی طنین‌انداز شد
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/448798" target="_blank">📅 20:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448797">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🎥
خداحافظ مقتدایِ آسمانی
...
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/448797" target="_blank">📅 20:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448796">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8791f99083.mp4?token=gPPpS79PPLPLkzjiodT_UpxhNsTfDHUxvL0D83Fcr3k37Wy4p9Odzf3btJ0QzN-fK-dyTzuhz3cZzBzQwUSFC3FEvEC3b4t5HIposSm87KAo3ALVBLDKBZ-VB-O2eCAUNH7d_rDifSIMJhcMhldfPJGEKZXGquj_e9Ltw7g2NwKMvWgdrPo6qYVT5W8vhJDKVipggH_SPaudStq8I6AsWt3ShBb7CxEfjH2NzXDwMsg3ch8InjGcPEvwH6LAMbGYnWOyKPhSzM0G0EFWIgqWEm2fU8XkAfMBYdkyZd41sWpCLPLHD_8r_HV8XZ2iA6_x5OO5ewlNLO348n9WeI1fNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8791f99083.mp4?token=gPPpS79PPLPLkzjiodT_UpxhNsTfDHUxvL0D83Fcr3k37Wy4p9Odzf3btJ0QzN-fK-dyTzuhz3cZzBzQwUSFC3FEvEC3b4t5HIposSm87KAo3ALVBLDKBZ-VB-O2eCAUNH7d_rDifSIMJhcMhldfPJGEKZXGquj_e9Ltw7g2NwKMvWgdrPo6qYVT5W8vhJDKVipggH_SPaudStq8I6AsWt3ShBb7CxEfjH2NzXDwMsg3ch8InjGcPEvwH6LAMbGYnWOyKPhSzM0G0EFWIgqWEm2fU8XkAfMBYdkyZd41sWpCLPLHD_8r_HV8XZ2iA6_x5OO5ewlNLO348n9WeI1fNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار یک‌صدای مردم در حرم رضوی: حرف ما یک کلام، انتقام انتقام
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/448796" target="_blank">📅 20:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448795">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c208eda68.mp4?token=ecus5Wme0vSZReB7B2Xiq1NycFViFsEAQIITVPgzZDoF3oKfRZepREMaApwAhUt2DxjbNo8eSQ3xbBWfMHvzF8-KgDygKZ1Yspj-HABRPBE8NrBIgX1j2z--cRTYdx1Hs4Iozf3cu7MVS-v-hYDCD8r3j41pgT_d3zi0udW95bzChQzn8cjuocx2v1WElXAP9fNSR__bKnt7PEah2avGw9by6-4C5efNEJZCYfWZUvOaA9R_tMGoGzAtpzSQzRTCnWtS4HDb-hg82VSVkw7HQ6-xO4z-ObsZyhN6rOrS4WMcGcM_bltuQ5SfFDCioaWKUj_aDj6fBQ8RvSyLbXrTUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c208eda68.mp4?token=ecus5Wme0vSZReB7B2Xiq1NycFViFsEAQIITVPgzZDoF3oKfRZepREMaApwAhUt2DxjbNo8eSQ3xbBWfMHvzF8-KgDygKZ1Yspj-HABRPBE8NrBIgX1j2z--cRTYdx1Hs4Iozf3cu7MVS-v-hYDCD8r3j41pgT_d3zi0udW95bzChQzn8cjuocx2v1WElXAP9fNSR__bKnt7PEah2avGw9by6-4C5efNEJZCYfWZUvOaA9R_tMGoGzAtpzSQzRTCnWtS4HDb-hg82VSVkw7HQ6-xO4z-ObsZyhN6rOrS4WMcGcM_bltuQ5SfFDCioaWKUj_aDj6fBQ8RvSyLbXrTUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای پسر فاطمه(س) منتقم تو هستیم
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/448795" target="_blank">📅 20:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448794">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec21531385.mp4?token=MfKasgyMGIwWs4_w6vZ5h12XLf0zSQafxK0QRxrtSwWESpTnO9jAhGoMkUpdcdFFsClJbdMK4une6xA2fYplGcb5ScLAIVB77XUu_nqps9N5kGbFLqNCzOKSDtrzSh4uFi0b9h5aej3iKRtvyEaBdjhJTB-ncTEieYifQJqT7A2ohF-Qu1075rNg2tDymqrN2auLj0DQx2Me1pikFtlS4SGzw-5aQaM1JdtKpZn1d_YP49yoP0xBP6RLHUeYztyO7ahuOp_v72vbbGDdyo4JbcrL-VZISZ9t-IlBPYpproBcEcHIVECM9B8VVSWle8zIZBm7ZWF6BYGFwDdjB0QOeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec21531385.mp4?token=MfKasgyMGIwWs4_w6vZ5h12XLf0zSQafxK0QRxrtSwWESpTnO9jAhGoMkUpdcdFFsClJbdMK4une6xA2fYplGcb5ScLAIVB77XUu_nqps9N5kGbFLqNCzOKSDtrzSh4uFi0b9h5aej3iKRtvyEaBdjhJTB-ncTEieYifQJqT7A2ohF-Qu1075rNg2tDymqrN2auLj0DQx2Me1pikFtlS4SGzw-5aQaM1JdtKpZn1d_YP49yoP0xBP6RLHUeYztyO7ahuOp_v72vbbGDdyo4JbcrL-VZISZ9t-IlBPYpproBcEcHIVECM9B8VVSWle8zIZBm7ZWF6BYGFwDdjB0QOeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید با خانواده خود به بهشت سلام کرد
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/448794" target="_blank">📅 20:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448793">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73925989f.mp4?token=ojmQthLZO8cUMruAUtTFkdSe5I2OZAhB-3cy_LtegAo8zbX9QLT00fhbiUcwdA-I1S3r4IbgyAvmahmzSL84wS9CDI8iZbldZyJPYk3u_HZVBmhz2qL58zPdGsrt4UKxzcnabRAvDy4Dxk7-QbXINBf8BHxt8gGQqhtowvC9j-AneHMsgQlPpjfveq349YWupPdFmnI0p3kbsvhNg2eiH0Wsqo1jvMFgj7wTjHnZtuT8JUsoOQAv6h9iyAPdwdY4rAAzBsEMppbjne2Qw5Pg3qQfIaXwriRQ-N-S_7CnmlO8XQbSqB0xyaRVxjocWHyOq6zZtq4tv4odKIqb5HQFUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73925989f.mp4?token=ojmQthLZO8cUMruAUtTFkdSe5I2OZAhB-3cy_LtegAo8zbX9QLT00fhbiUcwdA-I1S3r4IbgyAvmahmzSL84wS9CDI8iZbldZyJPYk3u_HZVBmhz2qL58zPdGsrt4UKxzcnabRAvDy4Dxk7-QbXINBf8BHxt8gGQqhtowvC9j-AneHMsgQlPpjfveq349YWupPdFmnI0p3kbsvhNg2eiH0Wsqo1jvMFgj7wTjHnZtuT8JUsoOQAv6h9iyAPdwdY4rAAzBsEMppbjne2Qw5Pg3qQfIaXwriRQ-N-S_7CnmlO8XQbSqB0xyaRVxjocWHyOq6zZtq4tv4odKIqb5HQFUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خداحافظ آقاجان
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/448793" target="_blank">📅 20:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448792">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHv7QRe971gWVcJaR6Y8rLKSK_USUVWbKfKB5BwTKSUEUgbe0OFiv_frOUw4KKXIugfU3h4NyOiyVldzcdB65A8kfazNczBahc4FN68wLULh3D-5Axxt_2TprS7j05RA0kNeydCRy3yfgfCAVYsk-hvMWd2mguJh5HV_Bs6Dq5EFHQpKm9WjZerCflwjyWCVDGHE4R7oiKUyHW47u9kf_5qt9H5GgSwCssP67iw7FMMsV6De9-oDyqGZy9Xu1cjKt6cB_hOUP2TEMVtTnIG8NxQw3KkUD_UtOF5XTrYvveT648EM4mHnbz-FtUW5fxm1Nncqh_UYS29ukPgrTIcM7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
خادم حضرت خورشید به آغوش حرم باز آمد…
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/448792" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448791">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8329395b4.mp4?token=MowG9tV_FyOaca9h6T_nxIqf1N5QNwvIOz2VYFodkR5kHbBOuR54MheJI2DXqS9LtEKBHMpGuJXOAGcHO7k_25WTVW1ZOvcN_xkvKdP-Imx-0tPlBLRRSbdBO97dyqzML6P62eQ2XIfyb_kLcA-jNtIUwTb_R_D5obyBTBM-kB2clx86OpezYczTLJqhggJmMh4yIlAYf-JcvBH0aBgTq_i4516hZCiNg0Qf84AaBH1J05J_lOz2-RsOOEsfH23LsvgfAS6u7E_W4iDSq-gVaam3hkXhoRJs5fA51cLikdGkEGZVl-CgoiZmdZlSwPNhd3AzG8wZzs0PTHVb86q5Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8329395b4.mp4?token=MowG9tV_FyOaca9h6T_nxIqf1N5QNwvIOz2VYFodkR5kHbBOuR54MheJI2DXqS9LtEKBHMpGuJXOAGcHO7k_25WTVW1ZOvcN_xkvKdP-Imx-0tPlBLRRSbdBO97dyqzML6P62eQ2XIfyb_kLcA-jNtIUwTb_R_D5obyBTBM-kB2clx86OpezYczTLJqhggJmMh4yIlAYf-JcvBH0aBgTq_i4516hZCiNg0Qf84AaBH1J05J_lOz2-RsOOEsfH23LsvgfAS6u7E_W4iDSq-gVaam3hkXhoRJs5fA51cLikdGkEGZVl-CgoiZmdZlSwPNhd3AzG8wZzs0PTHVb86q5Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای «یا حسین(ع)» در حرم امام رضا(ع) طنین‌انداز شد
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/448791" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448785">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-X8ylgJaaxfO2KWsAzW6dF1H8gm4WT7pd3YQlUEg6LIOWYFCIpUrGG94YKy3G-LkPxn0cwpH70_x5u7LUFz7F1LHw0z9uZXow2rKL4yCwUtMh47aWB1Pan6J-1TQ1YmupRmnB-kq8owyg-V72vv2ZA5QhLmXbH0X9oeljaIhCNFglIgxBobxJeMgm_3raHBg0u2X64WJyJ-K3xgd2UDDWYYXOIibIslMlDREkDFKNqA5JBQBfX2RK4taU3p1zN9NpId0XGgJKjX_glK7TpUxOc1OVPZ34IWwbnhITdVvwGrw2p1k8Kd9uQ51N8TXVY21S9mqDFuWoHOezv8aMvWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYaZ4TPzXcsUBVRmNfSuDB3sxnNHqK2h5-06vyPmsK8nLC8cTB-X5j4V0kzGizXx6E1y0LDcGdXlF81oRFkN0szboz4HdxgCz8aVzNXE4AYjtpaMF3W6AMeTxfIJVO6IEueVdH-pcZ-KTmwGb1lfG2cezm6G8GvRuu3pZvLUzjsHRxK1RkuLgpn2Tc6BeYvl8F-SxzbbMAt2xlK85fzFfbWjkz-BIIbo2MLFRMTa128KUxBrBgoqBHj4wsgnoV33AD6QSzh1LIwfbXRSD6aulgfuSgkx_GaH7LE2Rol0dclVlxzd_GFzeFY3fdMGP2rtG8Z6G1a45Nwf8GZLyg7svg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qf-YQ4V339KCyf9ji8FQmL--SAtQXlipwT5OmZVxUOhEN8joEHb64fdtAiNKPd0mZA2E0008OVJd9acoLmwySupF_edKhoeYxNyPMtPKP7dvVtC6Y9266h-v8Gymt_SYIqihOH295pmaDpC6HWVll6fnyrAgOu9fjn63Mj-q5elrfLLQRm6CL2ymgKwlqLjhSM6ScLeCOAiALiFvZHBB7-pJlF21MUw4LkfXwUI_SrSF83bTlhGUpa4ur8CGNzdPGTrWfraFeFnOv0EEG9l6c_d28PCyXcyVUsu5kOQXsgfLvF078t2AvLW5dczK5f2HVAoF50Onjz65L9-zm91G8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgEaHVvYOFbLb_uRxSi8ZHwW2ezDWMf8VAZhub92j9UxcmeVxrKIwiXX_r-equf-LRs4duU8U9ErmWGAkb-vef9BazggV3O7zaG6jCpqZER5uVMyKmZcFSegKJ9nPKTFcZF_wFQ_E_qhE23bqEnqFBs2472OOqpbHUlGVsQEzD4yLxL5-qSujmUuDsQj7bo3TMx-ySGe9iKpcjSRgMJqW5BYykIGWC-2uaeGkyyhV28nGDzD1lWwWSsqTIue1TNxDSzDTKvEg20aQ7F1lhSVCvOAksmqjwG9Y1iOaZYOS8bQSD4POa8WP55bSlG7HUxjUzTmrWu5S1EYReswmljWnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_jnDpGqiZkUc9aFpVXlQkZ9tcO1w8Wqbg0Ecqw1eoHblGaneJRPu43Q5q8I9EeQkzcUocVSQdVJI-FCs447ks1zvJ7_l6zzaYYwUfhNACN7_njHVyP6jfdurp2RJXjIU7wTzK93zYJmTYZkxupfo4SkUzfFZYOYmn1YGdDsIJSC8OzTjv3QYrE8UHKNhJfK_NthY4Bd23WsMdoTEk6BcKL82tIaJW4Eh6im-IYLNedGv4OJn5diVbwG4QIElzPBNi2i29ZJ5icjepqYANIQIUxHYJXEnbdiot-_c8xJK-kmYJ0IQSNdixqvkmwdc1DzWhC-n08FEWWvWOqVOu7Gew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8anTp9_IQQzXI-HgRCOH1M3M2ADcZvjXPT4GfN5VfGLX8qArfP7qc5b1fd45cUb9-bE9AzCK877ZKe7htHg997wPSh9AvWanSeMAewspoaTFj2y-8VPvTtAW3-Zhr7oi97ZvFq1mJ59oCQClw-gyFOx4AdOB0tCU9dSOTLq56_8KNPkVwHasDwmjOVsPk_PvXJFPgKYEdakuaHCLu9ZiiIKQen_OV2N9tr-5FXooJaFPcz37nN9RsaBr2k_unS87VTuvNftyMkZMk9aR0GELkhHUj4YlYjZuA3u1ciwaBoRhBWl_p6wH3eXmSO0yo_HPUSrX7aX5UfAbNHoPjK8Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر هوایی حوزه هنری انقلاب اسلامی از تشییع باشکوه پیکر مطهر رهبر شهید در مشهد.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/448785" target="_blank">📅 20:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448784">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqjSFpMqyOBsAevkKyD2Zs9wRH_qSDwY4lb_OjYjN9dfvbiGQPBoLhLo9t1EvvVBXemGb33TLZrpWISShlY45S9C-h49HuVEk3IbOW4JiLEH4uLApFhWaGXRtNRbJ6dQgXO30agtrR0bIC-gq8sREP_6UCUmtuaERvfCuGNl58LumJNZ2jlQNzcUFEQIUfmOo4DZ0InJrC1bgd0rx8GjzXtwMkgPnfYadnvuB-W64o9A1Gro8hSMAuHVmQcjcQAaLuuQ765TZhRVrCQwYoxqAoV6l3yb_z8xHzBvakYNBILyEaScwwCFzs06rlh8iuzBP2d7GvQwn1f1fzec7cdJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔖
واریز سود سپرده‌های بلندمدت، فعال‌سازی خدمات چک و امکان مشاهده مانده حساب در بام؛ تداوم بازگشت خدمات بانک ملی ایران
آخرین خدمات فعال‌شده را در ادامه مشاهده کنید
⬇️
✅
واریز سود سپرده‌های بلندمدت
✅
مشاهده مانده حساب در بام
✅
سامانه چکاوک
✅
رفع محدودیت مبلغ استفاده از رمز دوم ثابت
✅
صدور کارت جدید برای حساب‌های واجد شرایط
✅
انتقال وجه از حساب‌های فاقد کارت در بام
✅
مشاهده صورت‌حساب در بام و شعب
(از ۱۱ تیر)
✅
وصول چک‌های صادره بانک ملی ایران
(در صورت وجود موجودی کافی)
روند بازگشت خدمات بانک ملی ایران ادامه دارد
🔹
🔗
مشروح خبر...
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/448784" target="_blank">📅 20:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448783">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448783" target="_blank">📅 20:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448782">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ef055869d.mp4?token=NEruy2NVF3o-Ym9-nctzleapVbOMMAvKieDzAcoGZRVazuCifHg9TveuTZxxFdGv3jWt04aqetshKWbmYuajpEkZWJ73ASwIWDwQJBczN-d3MPbZzX0C1zhq8ju5-bEYr31YGVHHoCUFRh42Lk8EHjKi4UjAijpE-iVZBiD4O_oPxK9c9utLQ-K7BUeM77O_f0_N3_ZKH2JGOC1Ffd1we4MLawNw1mbzL09oShzUFw5BP5gDcBecdcZusVaJCvU-T5vm3ao9lU2RhMSXMR5mNws_x0NQ5GfmPnHFowflxD7SQ9HXxPSKFUm3dGxWUeaT6iEUOv6eiZ5TUhD52Hx9hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ef055869d.mp4?token=NEruy2NVF3o-Ym9-nctzleapVbOMMAvKieDzAcoGZRVazuCifHg9TveuTZxxFdGv3jWt04aqetshKWbmYuajpEkZWJ73ASwIWDwQJBczN-d3MPbZzX0C1zhq8ju5-bEYr31YGVHHoCUFRh42Lk8EHjKi4UjAijpE-iVZBiD4O_oPxK9c9utLQ-K7BUeM77O_f0_N3_ZKH2JGOC1Ffd1we4MLawNw1mbzL09oShzUFw5BP5gDcBecdcZusVaJCvU-T5vm3ao9lU2RhMSXMR5mNws_x0NQ5GfmPnHFowflxD7SQ9HXxPSKFUm3dGxWUeaT6iEUOv6eiZ5TUhD52Hx9hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم در حرم امام رضا(ع): این همه لشکر آمده به عشق رهبر آمده.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/448782" target="_blank">📅 20:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448781">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تردد قطارهای مسیر تهران-مشهد متوقف شد
🔹
راه‌آهن: به‌دنبال حملۀ جنایتکارانه دشمن صهیونیستی آمریکایی بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
🔹
تیم‌های فنی و عملیاتی راه‌آهن بلافاصله به محل اعزام…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/448781" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448780">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">امشب برای آقای شهیدمان نماز لیلةالدفن بخوانیم
🔹
روش خواندن نماز لیلة‌الدفن به این صورت است که در رکعت اول سوره حمد و آية‌الکرسی و در رکعت دوم سوره حمد و ده مرتبه سوره قدر می‌خواند و بعد از نماز می‌گويد:
🔹
«اَللّهُمَّ صَلِّ عَلی مُحَمَّدٍ وَ آلِ مُحَمَّدٍ وَ…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/448780" target="_blank">📅 20:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448779">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3XvhU5LoPzHXsXmcyW4sZqf74a94RJC-Et7dh1eDhxJ2AwNoMj5wFzXkoeKpEYMKAF7Onoaxocp9gkN84o7BjAGz10CgWXqv5kDsKpuy0NuvXDcHJQBhYReDQNInj1J4PnOREuhaaeYZvw5cE8F7K8pY2q7okip7yLXxVoYhtvWs5r3OJRklKlsILcqt0bFByjSIp7TXNH7jMRnoJpWJs6tVRcCAeH2flz6AJE5SYjcXXikdpMgkz_z2RPlYBh5se3Msu5VncQNwgd_hmDabBD9pAUSbRW0Almkd02AERf0oCsm2atOfee0ywdgLSbq26B8AnfWUmBcAflYueaiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رهبر شهید انقلاب اینجا دفن می‌شوند؛ رواق دارالذکر حرم امام رضا(ع)  @Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/448779" target="_blank">📅 20:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448778">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99ff886c9.mp4?token=r_H3Dpt0flV-MRTDLkQ3xiIvtkEotgOZeA0sz8YoPPChNnJ2y82whpZeEjxzdj_3Yo9u2-FUU2SGqtAB7ax61SdAJaPovRAEclYZP7AIxU9nFnMH-WycrV0l8KXNaG_UaQtRI54etjTbr0rmF-e4hOjj18WIQvOiGVcyjHlRpXUABWHhhGdwNOckZafjjcy2mGZVWU0FecqfNXi0O1W03vlinss_qpQk3LxGxwB42pLeueYpdqPueXxu8sPrOgxP70ZXARofHrgtsaivSori-VefxYCgHFfEnfuDXEMiAXw1seFe4DBrpLPR5oswj1SUfFqfF10wR047yMxiP5pHbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99ff886c9.mp4?token=r_H3Dpt0flV-MRTDLkQ3xiIvtkEotgOZeA0sz8YoPPChNnJ2y82whpZeEjxzdj_3Yo9u2-FUU2SGqtAB7ax61SdAJaPovRAEclYZP7AIxU9nFnMH-WycrV0l8KXNaG_UaQtRI54etjTbr0rmF-e4hOjj18WIQvOiGVcyjHlRpXUABWHhhGdwNOckZafjjcy2mGZVWU0FecqfNXi0O1W03vlinss_qpQk3LxGxwB42pLeueYpdqPueXxu8sPrOgxP70ZXARofHrgtsaivSori-VefxYCgHFfEnfuDXEMiAXw1seFe4DBrpLPR5oswj1SUfFqfF10wR047yMxiP5pHbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیارت امین‌الله توسط بنی‌فاطمه قبل از شروع نماز بر پیکر امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448778" target="_blank">📅 20:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448777">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc86d82c8.mp4?token=ZDr-CRa8LxVdqE8jUjNz1GUonIbKlBgfkw1weBdMajJPS5tCIUZ2j0mxebMK6VTgxu47TFZY50B_LxFyGMZj6389bvOKUQ10jewje2l6z4kvce1yHBDBrQZEBt8_iFgZ8xaVfeZByxFkx6C6mlyy_rKCjF2uh4NX-aie5jzIgNeut3BJyBlBFwmIWFRs8kt95MdT_I4-LFVH1p0e2WKGtVMkwVW-NQcNXZW0OqjC-CL36EcCewGq4XhaH9Em2N9l7wkhEdlVEOCJ6ClGed_EhTS1dgDJWb8Djzg6rPTV7I0PTR0ijYUOLxkbH-bYAxKNPdAUZJr9V8ZYgJCUqNNbUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc86d82c8.mp4?token=ZDr-CRa8LxVdqE8jUjNz1GUonIbKlBgfkw1weBdMajJPS5tCIUZ2j0mxebMK6VTgxu47TFZY50B_LxFyGMZj6389bvOKUQ10jewje2l6z4kvce1yHBDBrQZEBt8_iFgZ8xaVfeZByxFkx6C6mlyy_rKCjF2uh4NX-aie5jzIgNeut3BJyBlBFwmIWFRs8kt95MdT_I4-LFVH1p0e2WKGtVMkwVW-NQcNXZW0OqjC-CL36EcCewGq4XhaH9Em2N9l7wkhEdlVEOCJ6ClGed_EhTS1dgDJWb8Djzg6rPTV7I0PTR0ijYUOLxkbH-bYAxKNPdAUZJr9V8ZYgJCUqNNbUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختری که آقا را با بغض تعریف کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/448777" target="_blank">📅 20:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448776">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnLby3c_pG4ysfqZBxZqib__RGsMOC7-LNQijR2zaXrUFfLdg-U0rOJJHS_Cqg8P-GGWT_BqnBog_yWTrNL8JQTdy37jL--pFFbxNSWDwPA8z38mOKlaULYqg_EklRWtEpK-bfA5h1nl23MAUHFYlQfKvE7gnTs6Htp-oSjow1j6GTfEtAgEB9g3tA1NGQKhYt3w36QW6DpsLmtsFge20yDGSETTuMQSVKPp5th9NiR8R-4konVL4_xS0-myAAW5KPj5eEKhRhE56y7PnaZgk2aX6Exa-w_qMK7qSghcggpgoqkC_vpd38J0dJa-L3Oley90mni9c_DMWfI2kPL-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ما همه خون‌خواه توییم خامنه‌ای...
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/448776" target="_blank">📅 19:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448775">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1280170218.mp4?token=r1QK8v2n1QJVNey6e67h9c_ux40Bd2iGdW41pAdEBe9_RhZepJznfVizV_CuPoPJghcfQP4BWuGokC98RfOJI94ZD_bIFaHIaYo1OxvCPHWVsMYeWENE60vuUnnEACaMI0CkyWgTqkS3_yKxryj0tMQXgx6-WkWQ85Tny-ufksfLnhqxUIzTalbOJ-m1vO-8TnnFHHfq8YsnaW1AFE9zSjceKTOiIzAVr5jnm_mT7RIifaIXTei5IO0PRmgOJOKCa0xJk1LgpiMZDYrLyLeUxabZBJo89bE5YAYgHSR2cONecPJJEUK2DBRG70cyFjnORuPek3ddnbesDXQZe7AwVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1280170218.mp4?token=r1QK8v2n1QJVNey6e67h9c_ux40Bd2iGdW41pAdEBe9_RhZepJznfVizV_CuPoPJghcfQP4BWuGokC98RfOJI94ZD_bIFaHIaYo1OxvCPHWVsMYeWENE60vuUnnEACaMI0CkyWgTqkS3_yKxryj0tMQXgx6-WkWQ85Tny-ufksfLnhqxUIzTalbOJ-m1vO-8TnnFHHfq8YsnaW1AFE9zSjceKTOiIzAVr5jnm_mT7RIifaIXTei5IO0PRmgOJOKCa0xJk1LgpiMZDYrLyLeUxabZBJo89bE5YAYgHSR2cONecPJJEUK2DBRG70cyFjnORuPek3ddnbesDXQZe7AwVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب اینجا دفن می‌شوند؛ رواق دارالذکر حرم امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/448775" target="_blank">📅 19:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448774">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe69692a2.mp4?token=hGfpaVPssdSn4wq8cYyI_MDj8I4SiPnfNtiJkRHYr6njy3e5V9XA6bk3Ay3_7j1bb1IAwpB4nyOd_pNsbfDrYEvwEiW8pY4PosTt8lyTBESQq_HoKo1RmBnoIhCmjwia7HHGoR3ct0bY5hvtEJl4bL4w0LlBFrjKzwgoOfn6IzEaTrm9r-iPJsClyoX24NgqeDQ4RmD3D9k9dJYNy78eq0zXSyJvwNrQHkURP1II3Z_l4ocZssVZ-UkvFJ6viLwP0Is5VSK4n_jZoud6PByengBmFMEUoSqEIk91Yr9WJx1PpTiHSfOmjpqW6LL2yRaMJvUoQCYVyNMDVgdVv6qofZGh9YOx35HHLUYhbrJhIIfDAYgNs2aGZtQpVvj9R5xGwjJ_HCh_H9G72TleFU_Ne9L14XOnh09ZMeo81BOaBNq3D4TZY-6XziEbmzzrLx_KzMzjkRuDPU2kYSt7BpmVFtp802ANql0Ku-fPY4Jalj6QkttuAiBDmPMxvdkxaca2QWh-7w8-6t2FmuilDJGuLKfiESFkEFUA-UUYdsWt8pMRDSSjCXxhm1FWLKrUBDCWE-KBjgB27pJOA63LK4JtZ0wkAuTyypOVhKy6JauF2PCVxLNGaGH9w_j-wFh5YsI7enc--W9Jat69L7UNEnsH1OzQFASxyousLE_Bf8URSdY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe69692a2.mp4?token=hGfpaVPssdSn4wq8cYyI_MDj8I4SiPnfNtiJkRHYr6njy3e5V9XA6bk3Ay3_7j1bb1IAwpB4nyOd_pNsbfDrYEvwEiW8pY4PosTt8lyTBESQq_HoKo1RmBnoIhCmjwia7HHGoR3ct0bY5hvtEJl4bL4w0LlBFrjKzwgoOfn6IzEaTrm9r-iPJsClyoX24NgqeDQ4RmD3D9k9dJYNy78eq0zXSyJvwNrQHkURP1II3Z_l4ocZssVZ-UkvFJ6viLwP0Is5VSK4n_jZoud6PByengBmFMEUoSqEIk91Yr9WJx1PpTiHSfOmjpqW6LL2yRaMJvUoQCYVyNMDVgdVv6qofZGh9YOx35HHLUYhbrJhIIfDAYgNs2aGZtQpVvj9R5xGwjJ_HCh_H9G72TleFU_Ne9L14XOnh09ZMeo81BOaBNq3D4TZY-6XziEbmzzrLx_KzMzjkRuDPU2kYSt7BpmVFtp802ANql0Ku-fPY4Jalj6QkttuAiBDmPMxvdkxaca2QWh-7w8-6t2FmuilDJGuLKfiESFkEFUA-UUYdsWt8pMRDSSjCXxhm1FWLKrUBDCWE-KBjgB27pJOA63LK4JtZ0wkAuTyypOVhKy6JauF2PCVxLNGaGH9w_j-wFh5YsI7enc--W9Jat69L7UNEnsH1OzQFASxyousLE_Bf8URSdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این پرچم‌ها نماد خون‌خواهی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448774" target="_blank">📅 19:48 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
