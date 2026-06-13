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
<img src="https://cdn5.telesco.pe/file/Cma3ZbAAk513kQ8tQvaGzZrD5R_o1snNfZmEamQr3sXUGZ2vLuDMoE8xUp7II6gDfjdlvOp5k5nJkKImFx_vOR8OcEsxKYL1Pe4x123V3KKawuueCwfwLBJ3yicHXLqQLpn7Yv5mZvxL4coOTxBnzX1SBzNVMmKujf7Wcoud4Iqwbbo_Dh0p7CaJUnrMhBMrAuL1_4aAKUVvTExF_YEgjhcbN_n_GAj73bM751lMxTifE6mf0lITj9BjM2gjzpQ8aURY3SS-WY46UNRACeM8OqK9Fgoeqr1HgpI1XPBFji3mZnn1EzcPM0qIhMw6MjXpqDR3SCndDVbsFHSWhOZ2Aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 474K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 08:27:04</div>
<hr>

<div class="tg-post" id="msg-92535">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX-EEMZRzfHvGTnNtdUiTjMguSkuYHg97-WkxV15g1a2iBBfxqp5X9P3kHqoavKlUJleg9eCWYFJNThLzOBnP-GMUdFpuc2u2nIA8xJ8r4gx5BAEgesTAy8S5eRG1dW6YlQAdfju-g45r49QgsiNg3lTBQ7UqDlLnAHuSCeTHraPEENV2JY4wwMYE7KwQye8XUy4UbG9qOtDkOLC5QvjwHFNJ0xdExgaW6-KzrMFyGlLCkwrF3aWrhCqKztKIzVxqtNNfhC9UyzB2jSajqPgZW4BlkMu_HnYQsOaMxTL3q6ixTJDyYq6VcyK5YSvqbTZRL31L5PmXkgLncx4Kh76hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا قطعا لایق برد بود
😅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/92535" target="_blank">📅 08:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92534">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBU6bRezDAALOtxPFaUq-iCCpPXoWSkO0sQ3SZmzNklvRuCx4OdgazD7oYp1BmbUlfO9bdm0_El0CsxR4cm0U0iUDvD5udMJMVnYwMAGjJ57y6ZjD5j7GbtWqxFYD1PTdq2nJH6eJ0xxQQwWO7mYHblqeVWkGWMEoulu0QpO3a7-_IEaFWK4yU_1tzfxTkAskFguB9c-JZ1a2aGXVx2e9vgwCt0UfBHXyu26jctjZq1uj3hUoKfbKLSEuC4M42mp3XyBdB3ve-d5g3SZT9HygSDwVFf7sRuDZZR4_ZM4HBJ9O7q6Hcj3xWV-yBKz_i-M45WEG76-wYYMD05D_Q_8fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇺🇸
عملکرد تیم‌ملی فوتبال آمریکا به سرمربیگری مائوریتسیو پوچتینو
✅
16 برد
🧮
یک مساوی
❌
10 شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/Futball180TV/92534" target="_blank">📅 07:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92533">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzWyvVsBaIQOkWViEP5iYod5bYJQ0rO1dou0CGNI1wakUDFPlHk3SupGxvSpAbFhWKofM4WoFdvSLKA3YNbtRC5PiMsENJ7SOV9tJfiwi_cu-V-4CbH8mvZAtIKXY00X82Ygux9TPS-3jQ22PbRnAL2pieGA3Nbm9ODTlsGqlMKVlw1bGTQboLJPvNZ82Yu5e4ugOPr3c2XMi9HjZyDvmyBTAR1Pdp1hC4R-7Tz8Gug-BBbtoRAC02o5mk6bD0k4uFurH0c7sw-v3sufyo-7KHlUkXN-UrIiRr0ac3nS6I6QHBbG8kavVtskOe9ZcPT7S7Y3PRuyFNPGcElzxowSgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
| تیم‌های آمریکای شمالی با بیشترین پیروزی در جام‌جهانی
18 برد —
🇲🇽
مکزیک
10 برد —
🇺🇸
امريكا
6 برد —
🇨🇷
کاستاریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/Futball180TV/92533" target="_blank">📅 07:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92532">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMTqGJkiVYwYI1KjOWw6639YJkeMzw65iWmcXlWXCononnHX43go8UHsaH-5MBVhNDVjTnGqzCjqS16h9-7Sp32XGHx8DZknLJ3vxGG6-myCaHL9mjPzcjNV0UXH9lYHbG9_6bxZddbSw-8DDv6_jcv6izedvxGnyxQwwuHQk0XfPmMp_F2eCh18yAlc6B5pMielydqg4oFWhjI_pszn73YVMYtybXnirb3NWlGTccsoqBk4uJ53DsqjigWWwsvwIhPoHGh88vpJKbO-rB3kmSe7GuDR8odjvigau9ddtSWp0m7MQCg81cd_chT3RC615urpWi47q3XYqfONM-s-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: بارسلونا همچنان به جولیان آلوارز فکر می کند و این بازیکن نیز به ایده بارسلونا علاقه مند است اما باید منتظر باشیم تا ببینیم چه اتفاقی می افتد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/92532" target="_blank">📅 07:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92531">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBsO0rtCTEvGdcGVIPKvCVKgk98q2d4GWllHtAAJluNMsCOYzrgjr-nif80T4nC3S5IX9phrtxCjPe_sEHB_5G4ZA1Bh6Su6LxeQAiOboeojOcxfCXkv9E7-4xz1hgprD5_cDCm_e8kKeYJ0F-RDho0gBfVpRbFm-nXRlGjAmc3BZghlMM0x5RJWeBZh0gFfxB4aI9bk6PZVPw_0i-xbFD1921MUdusoC44EahmtvU5sSMGNvajRSc6llGv1fhR9Cm0dwnnwiao3Nvulxa2vjrSDu7ZZjI0Qb4cgZLWgjvXRnJi-TDfKtN8BEzYjWeSoeaeL8kUTCH9X4AiEJao7fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شکست‌ناپذیری میزبان‌های جام جهانی 2026 در خط استارت
✔️
مکزیک
2 _ 0 آفریقای جنوبی
✔️
کانادا
1 _ 1 بوسنی و هرزگوین
✔️
آمریکا
4 _ 1 پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/Futball180TV/92531" target="_blank">📅 07:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92530">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTqH9rDuTnG2oAeJFsosj0R1Qg-BbKaA90GZadmIKUUuGEWg0F2Mk50xV5pB-tOth-NSbzPqI7UncuthynzI1bJUq45retyjafP-3IBwDe2Lnxh_NGbemTqGzA8Mh4QHTKHAq3Hou-yClTsx8JMahp83A6hSO3rzIAVL-cdo7B3hi1spr3XIqO6UFguHlldvYMzePSn014em7wtiVfFxfnT6Mvle_t-5KF6iyMt46l-eYdDfF7hF-EJNDfTKlHbmjUhlKWD-WPejiTNf8ilIOOJY7-xcYV_rRCgXYlDil-a876eu1QZX3z-6MSdLvwsl5jf01_22rcJRJwIfjg__yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
بالوگان بهترین بازیکن دیدار آمریکا - پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/92530" target="_blank">📅 07:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92528">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wx4oqSitHLAlsAgRahwUz5n48qolUAsu2ABFu0HLog5VV9tBeLBRu8kQ5NHDasHRIvEAoiKDHkG8KFdCJDL_ixEiRQtLVL9Ma1nJEHwD3KfhJThz-rJPbjOOWaVi9VuxGrQt0PCmptHKsqM4R5eHPaMWjw49QhXC-Yk3H3_KLiEDbX46NPOOOBPutdUcu7y7yTbS7patTzWychK6S1mvPhgn-ntFW6Hp_aExWsc-1EYCSlUO6exZUQEKnKDY9s9AgmHk8nbS4gGejdxxc6bmGGeCWjrqo3zQsLeIESqo7VpmWbp_mDfRnWjmhtJ3NRbMyihsmr7Rmk7PKxBFVEnVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_V9yMmX2861qtiEbTR6PPi0108LRfigOLFv1KFDCf2sDRjogcSd_hLgwBBM65mXmRjpYlTjiYwOX16b9lALFi-jbDKTiEHJFvsRloRRZv20hU2z62t0CeJUr7JMR74o2iXD0A7Agwf_aN_JQs60-_A2kj1oY6-_uH1fh2ChsP8_zlcuZnY6p3m1ZmRRN5l5m8HoI-En1JCie6M5ohceYUCeRgSXAQjLm-5s8KyNPXVE27O98pRbyszEJDLqOwICiwofT8jv1gs9U6dKtjOtNlp6Mzo-0K4cC5p9T5EteeK27bc6Bm9sy5sLksB-jssDBTYNlZ8UXm3WdADy7rJreA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/Futball180TV/92528" target="_blank">📅 06:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92527">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F79uXakMUnXECWoL3qw-RnRpA9niST5OfqTJYHaqaoEdKz6UtyEtZLGWXiaFJ5cKmLNJzAAqKO2lRXVrhf2LIzqQX5SWwv4piUPES2U6-ZG76ZQ5sYeD6-ZRPaoKJUJnk6kpFMwliQsDdL2dbVYHuC6p_2MJhvIXKF9V7LOLSdXo585qybpzOEGTRgYHzN5RHQVbjXWAj1hpMK_4gDT_zDBwwDOh3Epep29yR6CXIAmATtrfxi4Qndw2jV-N-HE3W7Iq4ZtSIuCgSql03tLcwtxbqwRP7kI8x7DvJQ_4k7WcFkLovNtRfsMryni3CqOyG80AMYitZob7RB0hcmzm1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
آمریکا برای اولین بار در تاریخ خود، در یک بازی در جام جهانی ۴ گل به ثمر رساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/92527" target="_blank">📅 06:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92526">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwW3p1sWk59ZN4klPfUpKdCqER5z-PwaKkfWSypjPE-HRrXT1TJfKHC4lBGcJZqCXtZJjXxCm5GOaGYm_oHva6_ocufdeyCIal7VqL0P6BmNiX3uh7cb41iI0vp9T1et5T8iUnkujgl3koPBtQSWE4Tf3ylsPKHIX4Ofx76wbRoNl4PKG72YhnkDvMgD-Qf_qzocJ8VyjqBD8pQ4s328q2IB9KUHYaFqEG5PGUO-fmtbjKMxuCPnbmP8FpJQRJ4ssG8Zotrq03MK0jWnb1M4UQFmgWPpEyIzviFzAj05SLtYcQUZEU2MSbkvm0oIaTNiCaPWtkjLRgmiiYG4hEsh9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
✔️
پایان بازی |  نمایش درخشان شاگردان پوچتینو در خانه
🔺
آمریکا
4️⃣
-
1️⃣
پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/92526" target="_blank">📅 06:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92525">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4aSjp-w-m8tJ1En4auwDpponE2zdkrPFMFb2GLHdh9T6zQmPQD3Qr0D-nm4QPTfCY5VR6G5fzUbeaXG17Kw7YfGNdvhpCmWGN_QB5HhEaeHZLi79Sh4IYk15w8vBcC9k4VHs1SbkkxQ0n2gdsIjds3mbBVb-axxsbAyIJyh7j2RMUaeV6Ipvk8hhjgbz7Oc1NjleEVAasiyi6OLPJXc5q98iYkKU_r0R4ddDkA6T5yMvPqbGVhZhErjV9JxpBB1qgLr1ECIpsxHLX74exurzkwhZvgSeHJc9nfGQsYmQV5jGq2C14qe9uZXVtMfFWctVDpibPgzb_XRkv5H9XV5hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
✔️
پایان بازی |  نمایش درخشان شاگردان پوچتینو در خانه
🔺
آمریکا
4️⃣
-
1️⃣
پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/92525" target="_blank">📅 06:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92524">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e217c2352a.mp4?token=px7jnXbMaw_PiwpSk0j4EbR1GdL-MAEl1jfN8Ykxvn0TAdV8joUm22NYLTMzPCWY-mizvFG8PumCAKxoWjI6ql67uBm8J_Al-IDTurGa6vhunThTuTPIn_ZGxREXzE3skQaPUf9Jfzqifegd3BTk2JoJMxJlkam578zR5M45Ujyzp3Rr_BJlp5b96YcH_84rdUko1jRDcHpQB_zt_7jytKYI5Jd_kNCiXA9XgogTX0dGP6L3DWJN_RnuGaqo7_qxFuJJ9lEhaaVjF1KGOYg34BywZxFFqC-tBKEyOKbptqZoV5p2vrv1OPb8bxU1T6NZ6oLyMXfo_L9CaTuYZS0Y_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e217c2352a.mp4?token=px7jnXbMaw_PiwpSk0j4EbR1GdL-MAEl1jfN8Ykxvn0TAdV8joUm22NYLTMzPCWY-mizvFG8PumCAKxoWjI6ql67uBm8J_Al-IDTurGa6vhunThTuTPIn_ZGxREXzE3skQaPUf9Jfzqifegd3BTk2JoJMxJlkam578zR5M45Ujyzp3Rr_BJlp5b96YcH_84rdUko1jRDcHpQB_zt_7jytKYI5Jd_kNCiXA9XgogTX0dGP6L3DWJN_RnuGaqo7_qxFuJJ9lEhaaVjF1KGOYg34BywZxFFqC-tBKEyOKbptqZoV5p2vrv1OPb8bxU1T6NZ6oLyMXfo_L9CaTuYZS0Y_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیرون پای سکسی رینا به پاراگوئه رو ببینید و لذت ببرید
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/92524" target="_blank">📅 06:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92522">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عجب سوپر گلی زد رینا</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/92522" target="_blank">📅 06:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92521">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گللللل چهارم آمریکا
🔥
🔥</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/92521" target="_blank">📅 06:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92520">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY7K7p1SfX7fJtT3VKN6Q8vgoS2oq2Aix6eR0gG7_oTX2oK2DF0cfJn0T4R45DBn1vk1jsjooXjQLOPiRq6GHnTroD7E1A-rm0fQiAjWVzZg8oUj8AADdnaflRYWSF65-hT5CyIl4sWbqyNcG8l2HSkxKYTJOGS2P6giBlNa03sWhM0cK4M5LRiLAlhy0Tspt4iw4KuIvqRGx6Gqe_cel_zsELumt30n_kubwrsoQv-KCfM71cvPrqMZdB4jq_JgSKrAEcbNCB_CakTrWMlWsz2x3ugTzFdoUQxmf8HCFwzNDHfgu6LSYkYDImG7BoTwZlf50st5dp99M4ldv7-RIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇵🇾
70492 نفر از نزدیک بازی آمریکا و پاراگوئه رو تماشا کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92520" target="_blank">📅 06:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92519">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_2YzvhaqYVkMzJkxUl3SoWEmMb3lSjV7XhFA1lslVzL0FlWqkyjm2K4bD6ckSm1GtCWHQ-nVqJUGdEedGtJ2d3_qEN7jUJhaxlnkFikJJn8cx_HQ3AI4E575hJVOBYZGHYJvKHEc9vcYqKtArfQOjzNDcCWw3i7piPvmJG3pgubn5XRFuhMMJaIF9uxtyp0GPi7mKlXO10Ax4L4rfI3rV29t33frig-1zfuiiEBQ8vjrkivU4bMjWzx1OKUs1jkP9RXocUevdL9IM_KmSPHBykU9tdvKcHlIo_H3jPbUz84b9ZTbNpz-vEQo-GsU8fY0F0PCMdseF2s6KU-aWsENA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
#فکت
نامحبوب:
🔺
پاس‌گل های پولیشیچ در جام‌جهانی: 3 پاس گل
🔹
پاس‌گل رونالدو در جام‌جهانی: 2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/92519" target="_blank">📅 06:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92518">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQH8naEJ6HRgxHlatdbcvu01Z-UqoVGp8tgBr-I-5L0TqqMSe_L8Sk6aQIK9xjEZTeKWFnKL2m6wwe2a5kUQKdCxeMZg3WUQzV18pj8y9_xD00cyg8NVtSdBTq2DZaywq8d2SI3VkQ7R2fxB8IGqg0xviqNxs3OylWGoCe11cgSJLZ6AHNQjQeAtAub5WwqRniBrSM6C5ApZQ_GC3I19DgW978HEg7IUNVsDQRyRywrRQBQonr_lwKFRXx0EjYKk1Ug3gCB31LlPSx5YRSYXHBJWJ0Cpgo3nb7gQs8UuhAAWXbvOZhcHZBGqQtpJ29ZtFyWgNZDdIwf8n-JXM1LDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔺
اسپید به زلاتان: تو فیفا خیلی کُندی
🔻
زلاتان: شاید تو سرعتت زیادتر از من باشه ولی مهم اینه که من سریع‌تر فکر میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/92518" target="_blank">📅 06:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92516">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iaehdFShpwWKMsYXQ3jObxVGYP87HeAR-m5dVnZ7QxhlRSxf8KhoxFICgpso2pzOqZkZ8Pj5fGvmqoZnjGMaPCZQFlV9ln3j9ITy8mGqadB1bP7VzKoNXrx4ycs-Y2cd-9eHTCDIznwjY_n2RVqXqBDARdOGMppWf2bw6PGHGM05Yf4DYhT-ZwhBLdRVdp1MUBkLflEF8KA0MhoN9bdFpUSfKSKSi5hXCIcM2bMLMPKSh9aq5Sk_k52ZYB4FK7WArEk3I99t7AQovUFWPRt2aHeZ3pdIvDyPDBkbt5a9yIaqISs-7BKaJlqjHDcaUsP18gZXUiNjyPCpD7aEJ2OMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOu6ZbPUbJzpYEiwuPb7p0eu4D1BxgZKu8o102TNdaqq49TSGhzUy_nRy5NAK05IaMXKpKGRU2H1gYGv9xucGE_8Vye3hFrzjThMBU5wrgItUsNK8GgedNrh8A443AYG9vyYtV8WmhZqubqkaaYr9OI_kvP2kxoyrB9ATBi1bJMs8w18LbY9qMgE32ZwMr2OmQJ5dib4Npqsuq02JJR7hRtWfBkJxENbXKqBilzDkzjoU-PeqrYvTE2WPSUtx5Ekx4IRN6Ui0Us2Uuu_JFROWE5w3kNTUDVL6qoPeF1rkIiTsO0kj3P9_kKrEf_hC47jJNXW2ly1nwonkng6QPeHgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کن چقدر باید سوپر باشی که تو اولین بازیت تو جام‌جهانی همچین شاهکاری رو خلق کنی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/92516" target="_blank">📅 06:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92515">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d2169a1a.mp4?token=VAqSdqc8YCr-u0i3-eFkhBTFbVdJeghE08JJuCLZTwBT4h_DlYAjFvEGu4TkYgueAc1ZdsdDNFlKjE4tTIRty4AdTQc2_JQ6t7IpP1SXlwEhI-JnIfn3TRH_iefbytGzWFCeyYglgwi1HZ8RuZYzBlFbaJc7wA-G_7ZJNsRyVtRkL1tvByW-RHQqAfDPQgLgvgLWovu56BdQMqigCqDes_Jl7geH3gR0RBvWe2wp1APGhsV0OPER8sgD2a_ld90PzyazRJf5Kr9uMicx3y6R68sbSx5Y-8Ld2tg9v8u6-Fp5VpxzPH84KClDJn93op37_FsGDS4BAIcQIYyJSqshQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d2169a1a.mp4?token=VAqSdqc8YCr-u0i3-eFkhBTFbVdJeghE08JJuCLZTwBT4h_DlYAjFvEGu4TkYgueAc1ZdsdDNFlKjE4tTIRty4AdTQc2_JQ6t7IpP1SXlwEhI-JnIfn3TRH_iefbytGzWFCeyYglgwi1HZ8RuZYzBlFbaJc7wA-G_7ZJNsRyVtRkL1tvByW-RHQqAfDPQgLgvgLWovu56BdQMqigCqDes_Jl7geH3gR0RBvWe2wp1APGhsV0OPER8sgD2a_ld90PzyazRJf5Kr9uMicx3y6R68sbSx5Y-8Ld2tg9v8u6-Fp5VpxzPH84KClDJn93op37_FsGDS4BAIcQIYyJSqshQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇾
گل اول پاراگوئه به آمریکا توسط مائوریسیو در دقیقه 73
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/92515" target="_blank">📅 06:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92514">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گللللل
پاراگوئه اولیو به آمریکا زد.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/92514" target="_blank">📅 06:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92513">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927bbb478c.mp4?token=AkpA_z8vmU3EBrV-nHzDRb_2M0kko2vhK-pq6SXF6UqVgj9Ime6nVU4Mh3P3T3RNRAvqLtGRzyi1MLms6s7VDC5FTjak_i3AHoQPs0iHvDdGEq0N8Nfu5GtD7jnxt4g3mP8OjJXMEkU5xHctlyzkGZDxokbEG9pQWmz54sYtMbq6vJCunuraOq751YTizxW1caysSOrOzEsK_5khBM0Ue9yFo1sKMMxrcA1zEWqE-xi7duDIYSU-vYFtMghw-VgxBdrk6eNxaPMZzjP2HRT5odexYU7mDvMvAahL50Pivf1RcT9lmkm4a3NBCmPhoWjNsAPZJ4BMHGiZHFCoSCEXtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927bbb478c.mp4?token=AkpA_z8vmU3EBrV-nHzDRb_2M0kko2vhK-pq6SXF6UqVgj9Ime6nVU4Mh3P3T3RNRAvqLtGRzyi1MLms6s7VDC5FTjak_i3AHoQPs0iHvDdGEq0N8Nfu5GtD7jnxt4g3mP8OjJXMEkU5xHctlyzkGZDxokbEG9pQWmz54sYtMbq6vJCunuraOq751YTizxW1caysSOrOzEsK_5khBM0Ue9yFo1sKMMxrcA1zEWqE-xi7duDIYSU-vYFtMghw-VgxBdrk6eNxaPMZzjP2HRT5odexYU7mDvMvAahL50Pivf1RcT9lmkm4a3NBCmPhoWjNsAPZJ4BMHGiZHFCoSCEXtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
رونمایی از قانون جدید تشخیص هویت در جام جهانی:
🔻
در حالیکه داور با اعلام ضربه ایستگاهی به نفع پاراگوئه به بازیکن آمریکا کارت زرد داده بود با دخالت VAR، داور به دلیل شبیه‌سازی کارت زرد رام کنسل و به آلمیرون بازیکن پاراگوئه کارت زرد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/92513" target="_blank">📅 05:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92512">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f73fbe3dd.mp4?token=AClaGiwcnOkUvMJBOTAMvLUQ1G92nzgaY-KBCyRgDsKxl3TRLyPz9Zs-MwQ4JgXkO4lGKj8elm9x7l0wsqtAyCEXD_L7yQ7G2TsiE1rrd4F7UOATLMGC_4oOCJdGgrhKLWJva4F8Vi-gEh4oOGPqcH2Aj2u7lS1VYNvPOKRvPTXXCO-y-WyDe4sP_E4DcZe3Ru2qFUlVvyWGmhp5yr1X99KFc6GyW_BnX4D5_rRkBlhPo90BAEdzNn6qT-8QlxuYjsxuJ8an9yo8EzGGiNp9AbSmQhtATMOvjrSOXbb6SjvH-ijBt2_Jp5Q-BAupmQ90fJNrbflVp93S4D24zVEvrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f73fbe3dd.mp4?token=AClaGiwcnOkUvMJBOTAMvLUQ1G92nzgaY-KBCyRgDsKxl3TRLyPz9Zs-MwQ4JgXkO4lGKj8elm9x7l0wsqtAyCEXD_L7yQ7G2TsiE1rrd4F7UOATLMGC_4oOCJdGgrhKLWJva4F8Vi-gEh4oOGPqcH2Aj2u7lS1VYNvPOKRvPTXXCO-y-WyDe4sP_E4DcZe3Ru2qFUlVvyWGmhp5yr1X99KFc6GyW_BnX4D5_rRkBlhPo90BAEdzNn6qT-8QlxuYjsxuJ8an9yo8EzGGiNp9AbSmQhtATMOvjrSOXbb6SjvH-ijBt2_Jp5Q-BAupmQ90fJNrbflVp93S4D24zVEvrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازیکنای آمریکا تو بازی امشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/92512" target="_blank">📅 05:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92511">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ef7c3eda2.mp4?token=msdYGsO3MMIGEy4WmqUWy4M_XIV4Ms4bj_bKDG207DFHsHtqxLKuSW3PS6_bicgya03z5swh7cuAdPJQJCecHQToRqiTaIXuOcULLAdoQolnohAYGVFcTZjqUS2bypQ8lv3dvBLhvka_yTaCA_nVXOigDijNPSWwSD6-hiyGbvLgSlNv24Rgy4SevC9NHjgVtKNWLShqUdVn7zerhGl4MiB5NHZmJ67338TOHQGidaiyW1MnO-zxWtCvv_WrL5ETJTBMrvlYnr8VA8hIOvUSEU5ViKdt_l5ZZz3iTrfJEQ5AEsGu0iaAwmQpb7Ynkd0HorMKAiaOSc-qAvPk2rtz2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ef7c3eda2.mp4?token=msdYGsO3MMIGEy4WmqUWy4M_XIV4Ms4bj_bKDG207DFHsHtqxLKuSW3PS6_bicgya03z5swh7cuAdPJQJCecHQToRqiTaIXuOcULLAdoQolnohAYGVFcTZjqUS2bypQ8lv3dvBLhvka_yTaCA_nVXOigDijNPSWwSD6-hiyGbvLgSlNv24Rgy4SevC9NHjgVtKNWLShqUdVn7zerhGl4MiB5NHZmJ67338TOHQGidaiyW1MnO-zxWtCvv_WrL5ETJTBMrvlYnr8VA8hIOvUSEU5ViKdt_l5ZZz3iTrfJEQ5AEsGu0iaAwmQpb7Ynkd0HorMKAiaOSc-qAvPk2rtz2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
جاذبه گردشگری استادیوم های آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/92511" target="_blank">📅 05:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92510">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پولیشیچ تعویض شد تا برای بازی بعدی استراحت کنه.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/92510" target="_blank">📅 05:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92509">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8xD7nimupwuAKpCIJMgWkdBRnc7Wr4oHcFZ2uQJZ-rQfb0ygWayDJNkHM7E0ruth8GMTXSCS2MV1MUJV3nsKdMuKLGhYzvRXv7_KhoCIAdT0_s-fTAcgT0_PctoitC1aUGHPuXv6sJeetZCETbiktOi_vF5N4KIA4AsCAIcbrURcPLSXMoDH5RJOHahpCdyNsHCqeDnxc1c6ux5LjNtpiB8bhwwN3AuCeRWAiw6knLX8n2yWT6ciN5X7YIqvK_JI_hHoizi9c8We0PBZFePJV7NHZT7Tx4A6j2c5pw4l3pa4cdRGQMFNXdYt9-0_cJEJMPSJdXNNKlpzPYU3OBe5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار پولیشیچ در جام جهانی با آمریکا:
✅
5 بازی
🔝
4 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/92509" target="_blank">📅 05:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92508">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTs8K-O2RU3TLiEcfcx4RSpN6xYOPFPmWY-e5LrMfS7k1E0HERcIasCdU8wbPt3CqPnVbV5dD87e8wqRMVDit9B1MctbleRRtate1UqTf5fEVIAjBrKxi3TL-NBvhJNOXv7rwnUYtS970EV4uh5-rtjzwVgSFk4WS-iMns4-Tt9V-AfEv3KRCyoZQSbeJT1nMA2FAAMJsmLWtplK9Kb1c_IWRGKoRPpbGewmQ9YiyhOlpsZvRKshwg5jPI5JsKsKUwMsrvNpZRo-J9nHR88c6PkWpl9iBeobsnElMmqPWf0hDrXFMyJUN2lVL_Lhm2ZS3MBaHY20pMxGWXkD7e9AQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الان حال این طرف که روی باخت آمریکا 1 میلیون و 800 هزار دلار شرط بسته بود دیدنیه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92508" target="_blank">📅 05:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92507">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پایان نیمه اول بازی
با اختلاف زیبا ترین بازی جام‌جهانی تا اینجا بوده.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/92507" target="_blank">📅 05:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92506">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1368a8262a.mp4?token=noAwFLUJDm_AurxdCdA4VUc-asOPMqC50pHmKTbMOJfnjcChL8L7EBm4WWTv5KhvaZf-DMY22QLTGH-ImgY_1pgEBUOuBE-SgBDkbY_5aMHL7PyNPCsInvAdFli19W2pvdXFHFQ1uoXrDUXivKHsxgTTPjwgcNKAHJnhUgZS89X89SBh3yd3Y4zxzTKglotl-ZIWG5TvplR6HQVemyBc-iUizqExUAJ2Lfb-uOkdpYdRc6qAQYoNTUW07T--zDfovf0RdT3LXNKcLGdSolrOOO7VjnwJP4oUvi3nczxM1-vZU6Tr82QbiN-Xu-3xmyevHxIcx2slmWnELizxn5Fdeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1368a8262a.mp4?token=noAwFLUJDm_AurxdCdA4VUc-asOPMqC50pHmKTbMOJfnjcChL8L7EBm4WWTv5KhvaZf-DMY22QLTGH-ImgY_1pgEBUOuBE-SgBDkbY_5aMHL7PyNPCsInvAdFli19W2pvdXFHFQ1uoXrDUXivKHsxgTTPjwgcNKAHJnhUgZS89X89SBh3yd3Y4zxzTKglotl-ZIWG5TvplR6HQVemyBc-iUizqExUAJ2Lfb-uOkdpYdRc6qAQYoNTUW07T--zDfovf0RdT3LXNKcLGdSolrOOO7VjnwJP4oUvi3nczxM1-vZU6Tr82QbiN-Xu-3xmyevHxIcx2slmWnELizxn5Fdeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
دبل بالوگان مقابل پاراگوئه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/92506" target="_blank">📅 05:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92505">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بالوگانننن
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/92505" target="_blank">📅 05:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92504">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پشمامممم آمریکااااا سومیو زد.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92504" target="_blank">📅 05:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92503">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enJLF4W1y1eqbVWLiNuxryyedBEvS6eIBfQTbBSM44MOCn0NbwXvOpCZQT7-L0WOV-ZgN80536AxFhgs6BVJQVzrz1duJ9Dq3MVDHWg8SVfDymQvO0PylsUzj_S_jNhNPj51YJois51gsInvwvsS1Ox73ZZp58fIeokeSGcbxJ6hCdJrhjpopAlczKv19Im7dgIlMCt2dn_aKRzpBs5sj-KpqQOY3mUjfYjEFV-PojwdLZnOCbIBAbrn01nnntkMOG9JypTshkN0yyT5LOGAvuC_5K-cZmhjsUKXJn_Ljz88VKf-PLx91SdlsGqljIXHwYDJbHkTSjf-Ws-ZUh6Q9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویو رو ببین
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/92503" target="_blank">📅 05:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92502">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGP8DfiQnCHfHq3yaT7e2fUgMWYdYJmyEVnc4GLbufnsE21XRaJ_qWI5E9QNw9d_lB5NA-OCsADPfe0KlB4ju9VBXix7_c7kM3sB8RI7TR58wvxd1-nkD20bh365kuQVGiWp9r50O5xPEZLhvr36kG3ie6RBVkyjjqgXeFtgRxvefCRF6b8Zntf5VvRYgZ5pdf9scWm69XWe7qcsEqsaEj5cUn9utDPRUBUOwelyqySIIGOkhCe6RGIQ7HZ1KZf-mXllIo1yMv6vD9ownBS-kdmm_b8GElnpTcVhxPz5JFJ6gpNvY8hkEs8OnzsmGGsSEtWHj64EXNhkrpEKRv84lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو هم تو ورزشگاهه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/92502" target="_blank">📅 05:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92499">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oj-FeHV9cGQZ4GQV3yGCM9USBKreW1zOCg796VP62HH1Gnwl2WEzZwzp1hng3IasUMS_uFZ0WyqWvRJpQxrC16pHo8yDwhucJOlZrKci8OdoyPNjgkxlul4AFjV9lM1lAl50WV9gsTM3YkWm8_L_lAa6FXYuCOThCKDS0Taxhra5b5-cEUKHfmlkK7WKbwuKlugyVEQEFCkJm2dx6SWL_UKWFah2Ec3flHkLeZP2iv5j4zxOssG20ylilFZWxtkMAWR_yc9-Yyje3bnzc_Ly8LzF7ttM7EB1PS4KV97bHBvDiCF192U1uXWm9NSldo2j0pqu81oBqygc9Xfx4YChLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cddPzhUng9kZ5DsaQQ7JxJdT-Knxg4iHOZ61AMrCwjaPP5eIpCFZaZtxrRPJ_jUJmrUte5sfKg866UXeTQDSRWoTw0r9pdjog5SAsNBlaLt4pH23ly3XXWdzgxbDl8d2U-4k1tNVI9aWE6b5JYjXd2KiStd2bTp6N9UO0FevGx4MPmQf79AomvfEnWq2SzD7F-e2pxVY4dFVwKU8jNsa_BEvRBX8VfWpVpJ_KpBOeaKarIeA6r73H1A9fiDafOzilZBzLBN2ktErRNv3CCR7d8ZCxkdtYQtYhA7bOpo6s0CEpYrWd9QQGoPK47PCU-ImPVRxswcO98kbZPmUwQy5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iN1enZFm7bOfxbYn1sAdto9CxJusFCN5W0zs3vovpvX92ymZUJoQTqAEBT16NipqQCRpA02ct-tZlBcIKcQu4agJcjGYsRNvuJPWbXooVYnxInSe5-iuhoDn_KAU5xtriCelO0T70uEfbT7txAJrE0UZQ-rf72xX5btG4cnChSMTUMdySK33XSsnvFsI74KO1U22zH8Gh_pKnemXg5NpiEcEgvXO7xyReglxnoW9FcZ4tMYNzFMrxKvtxADWlElzOxOP0_2YrEBSxGJ6P3UjtXw9DI_BJKw1BmuVZXZM3bu0HJo3dergF8vq52rg4rUtbnStUMOKmDT-Xe9jm8RC9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وینیسیوس لاشی چجوری دلت اومد به این بانو خیانت کنی اصن؟
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92499" target="_blank">📅 05:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92498">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پولیشیچ دفاع پاراگوئه رو اتوبان کرده.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/92498" target="_blank">📅 05:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92497">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cceeec25f1.mp4?token=U1muvQmtNP7_mYh9i966JLln7Y_hk4Y3A3O8P_SI-Dg5qVagX3ZCuHJtd3PAThh7vDML9Mctf9a6amOKTjlRVGBaKFpT24su0FLKGhQLJkHgy5h89XSTNN8goLBnxDDjujh_U4bZkQU-K64x7mcxndCMqRMEiRgKRFR4wdPRJZyD9GG0qu7qBBYF_oyfTa1uWF15k1dcp9BxzYFGjvYwi3EtDBhDhXL4lJaKZJ2VVgkgYN-6mt5kWxRkFM0MjUZIeOSew2z00mqbgBkXGVe4NgJY_rvWIgjyuryhJGPpLfsIEwglepihNg2PzVwJcYlZSJ1oOCnu5OGKDfVi6C4Isg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cceeec25f1.mp4?token=U1muvQmtNP7_mYh9i966JLln7Y_hk4Y3A3O8P_SI-Dg5qVagX3ZCuHJtd3PAThh7vDML9Mctf9a6amOKTjlRVGBaKFpT24su0FLKGhQLJkHgy5h89XSTNN8goLBnxDDjujh_U4bZkQU-K64x7mcxndCMqRMEiRgKRFR4wdPRJZyD9GG0qu7qBBYF_oyfTa1uWF15k1dcp9BxzYFGjvYwi3EtDBhDhXL4lJaKZJ2VVgkgYN-6mt5kWxRkFM0MjUZIeOSew2z00mqbgBkXGVe4NgJY_rvWIgjyuryhJGPpLfsIEwglepihNg2PzVwJcYlZSJ1oOCnu5OGKDfVi6C4Isg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
گل دوم آمریکا به پاراگوئه توسط فلوریان بالوگان در دقیقه 31
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/92497" target="_blank">📅 05:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92496">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">و بلههههه گل دوم
این بار تاییده
🔥
🔥</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/92496" target="_blank">📅 05:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92495">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گللللل اول آمریکاااااا
⬛️
⬛️
⬛️
🇺🇸</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/92495" target="_blank">📅 05:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92493">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i5qVPea5HAmU_FuPe7NSRilC9cvEt2hapTqSuKquL8FzvDidXyfdAVS0gwkEKdzKbkE6mHr3hg-IcRrDswa-gejBs-FuO3k6fMyQPDAfyFL8fhcdJNA2yPAMMiFH5x0Zn-XQzH-4sRiZz_PTH5SIio6xlGoaBUWfP5WDWFBBlinZSG4__uVqXP4U9kWeiUAFBsWl0pEw8bkS5_Bd52-Nvd3rojaqucLBiRTUGBTcxCUAZ70LXIDqh03E-DvuOtHxaWarS4kBfXgHziq3j_CIxu4Qi7wCnl-XRlwWmgbgixcTXxVPAfTV9o1vRQxk5taQ93AaQKam7ZAPibuvIdlBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKCnb9WTl9N_8mWBQT_9ilLgz2lCeSmSUY8cXMtI4lQswWFKauEXRnCGLXdM5QotKyJ03dVMp6244yuR0CVBZhFST_diMuo4TgKomiAP-maTYuqAi-o34UTpCvxHFyRkP_9IQCHdNoztnBYHwkeKVQNdk8D6152UvyjjVhG3Hdbu233yzX5M4JnyjD-vqQHtxdXM9aasQFIk-ssm1k_EfEIS7pQw1m4HeDvos9gwvmRhDrzR0Kqf1EgkbraH0kYVHnQznfEM7WSmkxFaQzUXEAoUVXihfNkfFxaWEchoyLmVrVysNuq0S5jv0figag749CDkDkJx7phGwMLUMNPHLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
‼️
این وسط وینیسیوس هم یه دسته گل برا ویرجینیا فرستاده و دوباره با هم وارد رابطه شدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/92493" target="_blank">📅 04:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92492">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2fae2f7a.mp4?token=NJMu6FkUdptpO1fdYAwxPFdnELKpcXJBCleAgsdRxY9OrsOfbfd4lKH-B9cnhZ0LGRGnv18jqyyc0UT1B7wSwTtk1iWz2aRdfrESX2k62K3hJWKj7sIVHbdJDWib0oNVA4TYcXqHbxLkIOJecGWhSO6fxxxkKZAxrWlq6pCHFJECwDWmY9qsU9TiRSLr3CCHbwm6-kkVg-KVVjLqX-A2JG0jQNTHFhfgVzYtE3qutrLDrpaw-UGZ6IlhvWr9QLwf7jE4SgPYk8Yv61VXmh8oYAj96UYy__DQA1-AdTSBlVIxVbjbnsIcMbpqdpVqqo1Ngd825UjoHApwlLV4bw6Z5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2fae2f7a.mp4?token=NJMu6FkUdptpO1fdYAwxPFdnELKpcXJBCleAgsdRxY9OrsOfbfd4lKH-B9cnhZ0LGRGnv18jqyyc0UT1B7wSwTtk1iWz2aRdfrESX2k62K3hJWKj7sIVHbdJDWib0oNVA4TYcXqHbxLkIOJecGWhSO6fxxxkKZAxrWlq6pCHFJECwDWmY9qsU9TiRSLr3CCHbwm6-kkVg-KVVjLqX-A2JG0jQNTHFhfgVzYtE3qutrLDrpaw-UGZ6IlhvWr9QLwf7jE4SgPYk8Yv61VXmh8oYAj96UYy__DQA1-AdTSBlVIxVbjbnsIcMbpqdpVqqo1Ngd825UjoHApwlLV4bw6Z5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش اسپید به گل آمریکا خداست
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/92492" target="_blank">📅 04:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92491">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آمریکا ول کن پاراگوئه نیست و داره فشار میاره.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/92491" target="_blank">📅 04:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92490">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a08dc037d6.mp4?token=UQZScxMgAMAHC78bfcgi_xUZQK-lS1NU0bfbXXjelYdYnChXGQHZcSBSpOC9ZskgnqQE_AGo21CdoNM08jf86JK3AKc4eN3lMTGKqHO61UmaRcniIs16K6yu7q3NUu6xpGdOHts0ZP2CRlm5dKynycj2a023fO5dU-rzYTdsIKIZzMH49rjlVF6uw6kXENGKpw6wRCrraCk9jJjwgW-RHxW4tY8D8FLrnoDl16LvRiEQ-WMv_Q-_mbH-8_z2UZ-r4zuoorVOibyzvHDWStuKns2EnBBHEeK3l2IC7krhvRF9QN7iamAqXF-Y5xxNr0AbvzGMFa5mwnZeKePZ6cLpuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a08dc037d6.mp4?token=UQZScxMgAMAHC78bfcgi_xUZQK-lS1NU0bfbXXjelYdYnChXGQHZcSBSpOC9ZskgnqQE_AGo21CdoNM08jf86JK3AKc4eN3lMTGKqHO61UmaRcniIs16K6yu7q3NUu6xpGdOHts0ZP2CRlm5dKynycj2a023fO5dU-rzYTdsIKIZzMH49rjlVF6uw6kXENGKpw6wRCrraCk9jJjwgW-RHxW4tY8D8FLrnoDl16LvRiEQ-WMv_Q-_mbH-8_z2UZ-r4zuoorVOibyzvHDWStuKns2EnBBHEeK3l2IC7krhvRF9QN7iamAqXF-Y5xxNr0AbvzGMFa5mwnZeKePZ6cLpuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
گل اول آمریکا به پاراگوئه در دقیقه 7
حرکت سکسی پولیشیچ
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/92490" target="_blank">📅 04:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92489">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گل بخودی زدن
😂
😂</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/92489" target="_blank">📅 04:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92488">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گللللل اول آمریکاااااا
⬛️
⬛️
⬛️
🇺🇸</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/92488" target="_blank">📅 04:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92487">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خب بریم برا شروع بازی آمریکا - پاراگوئه
🔥</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/92487" target="_blank">📅 04:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92486">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Y9z2DiQR6zr4UN0o4d0Xgl0TnALDpHkII-v11Laba6s92cmZaoygpaC0Y89h5EHRX37b8LnfNKDn12E8jX_jgF06cR6Y_dOv68Fg49Y6xJygKf9Iks1rwy-yKCf4TAgnLAqoBeZX_Tv2nk6hZkaF_DHpuB2z4Ra3ohyyHrwO9rkGlyuCEQHsKG4FZgc5uC6AOSkSBBT-PpoQW2udLi2noDZRGk2WPY1C3L2pyzf3oz1iNAdeU-5bIzPzfbK6NBQuznHd06A06-jX1idx-iAlkjIFfuGfvXg2nObZbGmkP4suWzQ5rBzyOFo3QhARma8LCYwsTsufmSO7W1momiio9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏆
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🏆
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/92486" target="_blank">📅 04:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92485">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amLg2UNIq3_KZ9btdr0WYS1xu_ok8hC_f5KjZbPWIWbYSy4NhcfaxuLMFynvPOcbVwhVGJOVEfN06UiP43ullVE3CehvVz73rmtC0Tn1oAyk_XlIZwkGRPtC9Nt0tcjSZS4K7v83y5Dqx9sWaprPfKGqUANOThn1A-n8ntpKGvlUdK6-EiTJQ2g-egmGTxtI9DgwvFZQRexZHItCfUCVNatOL11L7ErEHO2VUhBM7QzI13b_DNwKoR-V47sw2PgLkXF-h3n8RfXVfTKxkbUMgbpKaYSmE22TSkciKwR19bVjo8dF5lQ_MAsbk6cZtwAjOH1lX8oMwWVkPN509IQxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بکهام و تام‌کروز هم اومدن
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/92485" target="_blank">📅 04:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92484">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcwyF_cf4NPVOEPXrTgbCgrn_u580uf8MGpwHIzmqsJ-7Dw48ghnGZOHFQ4no-BadGc1tUpxZKGGBoC1qr_-79338Yge9Nzwk9YqdW8lIM8D2MAUuSZxJw8yscLJj4tAq2f5y5X_KpPG-5jtI3K5I7STNiwvN4nBd3V03Tv8tLDfTqhiXimLcVTAui22NilQZOAE5VXiWuTVbGTGHQL3ylqbnd9qBe477uQ_RQiWHrYukZf3yHqkk3VAkQ-w_mSsw-t6zVKTzrBJ0mewHuz_y44sZQisjd8fxoVnJS6O8ZQAOoMW5LFKPCOlErvITiMgvQXTYoUU-Veqmo8iByKEBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇮🇷
حمل پرچم جمهوری‌اسلامی حین مراسم افتتاحیه امشب در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92484" target="_blank">📅 04:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92483">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری؛ فدراسیون فوتبال انگلیس به فیفا هشدار داده که اگر تا ۲۴ ساعت آینده اقلام دزدیده شده پیدا نشه، از حضور‌ در جام‌جهانی انصراف میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/92483" target="_blank">📅 04:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92482">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oad0He4HyrySDY3GDx1CxshQHAVm1aWFnAd7pnzUebILFl515AyGgodoQwtGqyIFXNkAyG_lk3rPTi-4mSS3xLozYpIuHIgVp3JEgLO4rufonVUJPHTVOvAJwF5g2MhCuMp3_9O0qkGf1C1H3jSf2t3Edu9IztM6s7OuNvNv2jfT8jnuYNF6Va5G0MpmaCcp8nVB_8zwb_T3hNl5LDtfv9pOq2Alpb4ynX40LD5viLOwjCuHBtZLD6oxdc3keoGtcLfNUAIgE8kuTS9BI6MuXStKp-nL9R8goBcMNo5CECyGQEqqzt__xrqskZm10Y0aJSfQB3vXt2EeTm2Z4_BaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیگ ملت‌های والیبال/ پایان ست دوم به سود ایران  ایران ۲ - ۰ آرژانتین
🇮🇷
۲۵ | ۲۵
🇦🇷
۲۳ | ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/92482" target="_blank">📅 04:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92481">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری؛ تجهیزات ضروری اعضای تیم‌ملی انگلیس شامل کفش و دارو و ... در محل‌ کمپ این تیم در آمریکا دزدیده شده
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92481" target="_blank">📅 04:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92480">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری
؛ تجهیزات ضروری اعضای تیم‌ملی انگلیس شامل کفش و دارو و ... در محل‌ کمپ این تیم در آمریکا دزدیده شده
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/92480" target="_blank">📅 04:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92479">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlWsmc3ECUyJ15ndSKheZ8aQNr1BVcFQno9DHxT8cvfzhFTKDAT8HVUsvjwjBLmOiZ6E1dc3DGxPtMwAa471HI0IQioMyxSxgx-itKgS2wVGuzRhAbzLeDrWeq7d5qWvVWa9e3HtLjIeEwVYcXgki4vDe_w1Mm_jZ0jsT22A5xerwIiff2HanG3KK3YXcmhcu__sttNrRwVOko-Fod6xwployLgZ114XE-4Z7-ZJsTjPHLgsOvHCWLytZdUtInfTWnrq_GgMQ7ihnSzZGWSCZxzvG14OjtQ1eLcfATrD1YdMJcXJz9dD9xb-GJwnYhVm3CiLXekvxEUWLvKUiMMSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
🇩🇪
مجریان تلویزیون آلمان در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/92479" target="_blank">📅 04:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92478">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kb1qy9uJa01yq-2muKitHgxTbtDNxGy0ACcQcbDyod-Mf4AW8WEJ6eMd7jQmRDI363D0aFcCXNHnNKkPa0e8_fP8okhqpjCIB6OrvRERvrGM41Jx4dwIoxcqhTd3FDVnbgMfqzdhCT53napXuyK_-XLaUXSWLqaQrAnK3X29Dk-drPazlnxduWSGqt-4GqKrnEKxZzlHCyGfZ6faE4_zT8nrlOfEkM3IUzIxf6S1OeFX2KsTME4drFCCFLhdx3m1VvaZzYYoBTqCTz9G-4sLnmNCos3got6oqu6gSn8v5gbmUv4OwZRRJ8YmCAZRuNE40_JvnJS4bBmJvSedMvdfMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
اسطوره کارلوس پویول در ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/92478" target="_blank">📅 03:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92477">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfjabuJHuUEGK6bLHbTGg1bLxBhPFaYUgh0URO_5WAHznXWAW_1Au18Y8p9x-mNYgLSpZPbddiIe5xApYT88W0T0hS5d0MXUJGmVBEd2aHJBcoSyJXQbNw75XV7yi91_BsWlbbzbhcpxHX8F2P4sHqS-t_pkmxGs9XKbVLi4EmqhAFd3l3q4icEcpZtcF8VZcORXKDprqmHXqY2TwlqGLsz_0HCDf-GkN4IxJruhMLVsRbWigG3CTvfSrhS5_ICsGhzD6aH_M5N4s9bE3RPTo4hpYDFF0aHG08axXJONopvf5K07H6ZGuYKtUjMzDct-KJXGLjYCflWnpCY4baEkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان‌آمریکا هم به استادیوم اومده
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/92477" target="_blank">📅 03:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92476">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b291ed502d.mp4?token=aRa91YivnjVMoj52l9cff8BipepbxTDbt-YJEc56cTE11XSJf9KpkBV1cAgh0DzyvpsndAGA1Y33JjYxEKVVff04MhMbd_kgP_Nkd5PSOAE_bPUkPXLZ3yv_XBuO8ewuzQzjTtCWRt5E_gOJ8aDAPgTSFz_d6JrSvLZwTvaFrTmk8JYHw3WcOzl69fHLYKGYC7hQ4UztwQGzzWudaVJAaKo9Ku5KW7fO_KPknbtQn0GKDAxIAQQxU1Or5RR0Qzl67CjlPrhW8tT_dm2G_LdAqVjZvFpbA0mC5kEPj3lGEpw9LdGRKpg20B9jvanWd5MqmkozaRrsMBapwFWA7m0Zxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b291ed502d.mp4?token=aRa91YivnjVMoj52l9cff8BipepbxTDbt-YJEc56cTE11XSJf9KpkBV1cAgh0DzyvpsndAGA1Y33JjYxEKVVff04MhMbd_kgP_Nkd5PSOAE_bPUkPXLZ3yv_XBuO8ewuzQzjTtCWRt5E_gOJ8aDAPgTSFz_d6JrSvLZwTvaFrTmk8JYHw3WcOzl69fHLYKGYC7hQ4UztwQGzzWudaVJAaKo9Ku5KW7fO_KPknbtQn0GKDAxIAQQxU1Or5RR0Qzl67CjlPrhW8tT_dm2G_LdAqVjZvFpbA0mC5kEPj3lGEpw9LdGRKpg20B9jvanWd5MqmkozaRrsMBapwFWA7m0Zxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
اجرای دو نفره بانو لیسا با آنیتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/92476" target="_blank">📅 03:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92473">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QeUqCd7QgnNNqyaTCd8zblq9GnIKZ6PhyrUTG1Cq6A0rajTZj7Y_j5BG_488mH2BNlbcEgNiqLh9cEkWgQI1_7pyPR7Anej6wMvRDoDSNCdxrcajtiLXwJxYFU74NxssSLAi3dYTZv7RyPmYQy0bQh-2Bjrdzfjb3aZ2xl__s-F2k_sXT_FkyHvem_tWy8mjZV7zoFbi1zkCLZtpU0rwGQup0B8B2q2Qt9fUpyYRhawDDu6vPfBtJtHTu1KvKyVnMrJQaaTH0I9TIfAEPAWDSds62ErmGk9e0_y5QS7SA7ROkQEhKTMPKOwkcQh_ZJWQR4pHbZRudV9MBGBD3QExhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SG35i8W8xroG71TNLiLEFH0OQ4mqhdAVf_XRE4eT_m3jifdF-4qlY7ycFBB8XrWphl604e1VawrNsUWMTW-WIa8u8N-Tz8s3kfJFQs6tFG6A5PyUSOsZldgAFnV98IwbLnOq1cXVauUXmAGCnboBwlLR99unT_ODU04neyRUH7dFY-FbgCRfFPE3JwgpSXU77qXVABpiTXK1UWpX8oYiLKRm990B6Lz5cq9XLb8goIsG8sHY5gskRrcaJFOyoP0tpARp8LdaTea3b-jQCOFjbtIlxrRIdK3Xg7QiwhfNuEz3gs7dK9f21jyjdoqWRxev9aSUJbkaVpz_zrTFTIYjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QU0wCaYBC_GeF5_gWadgEkVwFQybvtk6WJdY9gj4eRc-nbVQeJvFwp7Stmbba1v6b7xF17QlUhy9I5H279rMx4-BGriTiOtfLVyhbO9VwEYJVAFNWdmERFXIDadJgj6TRU2y2S4AuEWnbb6OWCl9k-86RwwHT89XKYcFbzr-7r_eWy0GpIOKHnHfGir6R-Yr_yJwsHz6hiF_7Jc9G2E7oyNaR9qZDnk6OC2voNN0PNvMHbCXoyBvW-sKDBz_URtHFPa_ej_bslJU7lIU1qflzGWbwRFn9GUF2ihc_C8yRqh_n8StJKbhHkvrYz9Q5_Ht0r5VEN1EA7ql8USe5ey8gA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
تصاويري ‌زیبا از مراسم افتتاحیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/92473" target="_blank">📅 03:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92472">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">لیگ ملت‌های والیبال/ پایان ست اول به سود ایران  ایران ۱ - ۰ آرژانتین
🇮🇷
۲۵
🇦🇷
۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/92472" target="_blank">📅 03:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92471">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🔥
🏆
🇺🇸
اجرای کامل بانو لیسا برای افتتاحیه جام‌ جهانی 2026 آمریکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/92471" target="_blank">📅 03:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92470">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بخشی از اجرای بانو لیزا تو مراسم افتتاحیه امشب
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92470" target="_blank">📅 03:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92469">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0252ecab75.mp4?token=BOk9rw1OhP5N3pdPz_hSfOig8hDmMjYz5GtQww-fU7ILk8ibdOzqc40Sqpu7Pp7fxH3NWnMXw7O9OxbR9mdANJtv1SW15XJybf13AyLEI5B-9QSLTMZZSAW2p1UbmYIGjMQKu_1J3rpIKP6_7V4M0w-dBAhvghdERCzS8aEA0n65JHrZw0u78XdhsIuHp36pXlhOWxgIsoxeXopMIwqRGh1V3Lr0pxK_ihKBCKVpZXXC1u1fqitYADLLJQfqojSzUHEmXhiw6bTtlwfn_C7sC_hYTpcBnjWlWMKkP2TCJoLMBf7RLnjh6ImepaqR_b6_Zqrw8uhBpftFS5zmuG-QoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0252ecab75.mp4?token=BOk9rw1OhP5N3pdPz_hSfOig8hDmMjYz5GtQww-fU7ILk8ibdOzqc40Sqpu7Pp7fxH3NWnMXw7O9OxbR9mdANJtv1SW15XJybf13AyLEI5B-9QSLTMZZSAW2p1UbmYIGjMQKu_1J3rpIKP6_7V4M0w-dBAhvghdERCzS8aEA0n65JHrZw0u78XdhsIuHp36pXlhOWxgIsoxeXopMIwqRGh1V3Lr0pxK_ihKBCKVpZXXC1u1fqitYADLLJQfqojSzUHEmXhiw6bTtlwfn_C7sC_hYTpcBnjWlWMKkP2TCJoLMBf7RLnjh6ImepaqR_b6_Zqrw8uhBpftFS5zmuG-QoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخشی از اجرای بانو لیزا تو مراسم افتتاحیه امشب
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/92469" target="_blank">📅 03:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92468">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNbET_IcJvxi_Y-AzAKoeBuBAqZ9X3_F0XJWK3RuX4nw8JDh8hh9DBjyYzkKjAW1dapPCyv7ec1J0u3LDF-N-sia1FxqFvkc3Hkjqx4E7_E2FTJv2t-Bgb0AS3fTIJlGhTaDA-qC3cvcCbG1btAmu0yVMPqF7VvOxYIRdso5BeiQWegGyUfYsd0oN15i5wHTJY8VTSKpW5l2EBNjG95bWj1CDWXkVQfg0n5WnxJiUZRpI44qJm43T6ebxCLw4Sf-betJIU5PFrAtFJTE6C6VfqWY1D7rg1zfdFCnEPnI36I69LwXV_wHR7eSkAOy94SD-_Fbl0v6CQRVDV3LQHTPgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه کیپ‌کیپههههههه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/92468" target="_blank">📅 03:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92466">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WY_NRgkVhnOW95_6jAKN9aAuQH3_TyjiO2OWNUiF_VaYUMg499s4tH4o5dhgqvs-1MAhByo6cQbrSY5jS1riywo_cjDQiFZNtL7OgvzzRrRzFGrcvLX_QErC39j861iJj0WSdHF26DCPXq1x4j43bCwViWwqG6-0Jq9rZcrCv3y3YPbhRM80psrDrRsNNZGP5rupnlrFhcj-JPl1-GEKFJ_5Gu6cz_rwEtXvXRh6AzKRn6jmPE5VPShzUODLb_eNATKjKoohbMxAw9NgRtQUiZ92qaFggfuFF2ss8ykijNbqbj_w7HvukXGGpniSeN69a2Z9s5qz9G1cpEKTR-uTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
بانو لیزا درحال اجرا در مراسم امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92466" target="_blank">📅 03:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92465">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLHG4UnDCDyi5onoIdlR_8rzAhs9nRDkvgfOT7EOS7Y7doTFbL75ZvJQAFEdBnGyfEh3qZBjTA-LdaE15H-gw-vPypNpMRvqoiG-xfD24XTfCVVJrKjT2qeiEWA73zE0Tcvggn31CElzFzTVcYXs-6wvejj4VoE8DyLCvgnwrKcBiuztQZ4TN6dRhZ9bbNJ-JPJp8HIi_oLt0ce6i5NBUWcaS6bXpGhVutRnGOQky5l7O6s2sJHzBopwb10t7qnssS4zNfmeJTF_lvVmynXLdIOhPgArd0pzn-HsN8sp0KhxwPP04f_Nn_L1zTp0Cz-glkvIOjETawTPbzhuLFmdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇺🇸
ترکیب آمریکا مقابل پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/92465" target="_blank">📅 03:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92464">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a643a87a13.mp4?token=Lm85vI7LbGDUwxLnIE_3-a7tWbqlnf1TRihVYGUIO8qmbl5tzhXQ27dEIl0A7p1PIn1IJz9o6TA0VYg6skmskaN8ZRbZEryjGmS49CRovixpwIp6AxvZ4kb_lndaXjsbXoj1Ui9CEJWGN8lvJfNIXkfNN0ZhVoOD5lblazPK27Tv-KeloKAJJKyd0QvhbGoIECA0UKZjAMkkokBRgZHUBVh_ABPTjSWUzo8aHjekX6tvsfufCx-ld0LVMiOep3yA9a99zqITZRO2Cs99Yha4Pdp4iFsaLEXXy6WpuM_oKLPkLICp0Fj0ESfSMPkz8n9f8_HDB8zXT9tjkOjkZ6qUA26Mj9B-_cPeNAEGhAycOegCzA7VOUc5rw7IkkSzbZZi_JDAmdHl7oHA2sPQH-O2-gifzqtdUftdWkjzL98KFAMroXJ_Q8xau34CBPbuPs0IICUywx-FbYqr1AW6B5b8YcZH6XIUocXjm5wTPbjP-liqHxGP-U6Xf2wAuQSbh-RXng3lRQ0rVVL1Hh58cDqSqXr46GwcTTzF7Rbnbb0RIWJBFLPsnkbzS3KosmBiNckPntRzygqPteuvZqf2Bmwo90xJnC298Jw9h7qqtm7Sm-EvlnQlPD5SCQe5CynyKM8gbwqAzYx5coIgP7gznISSo-4d4QaU-9ZTZGjxhGNucJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a643a87a13.mp4?token=Lm85vI7LbGDUwxLnIE_3-a7tWbqlnf1TRihVYGUIO8qmbl5tzhXQ27dEIl0A7p1PIn1IJz9o6TA0VYg6skmskaN8ZRbZEryjGmS49CRovixpwIp6AxvZ4kb_lndaXjsbXoj1Ui9CEJWGN8lvJfNIXkfNN0ZhVoOD5lblazPK27Tv-KeloKAJJKyd0QvhbGoIECA0UKZjAMkkokBRgZHUBVh_ABPTjSWUzo8aHjekX6tvsfufCx-ld0LVMiOep3yA9a99zqITZRO2Cs99Yha4Pdp4iFsaLEXXy6WpuM_oKLPkLICp0Fj0ESfSMPkz8n9f8_HDB8zXT9tjkOjkZ6qUA26Mj9B-_cPeNAEGhAycOegCzA7VOUc5rw7IkkSzbZZi_JDAmdHl7oHA2sPQH-O2-gifzqtdUftdWkjzL98KFAMroXJ_Q8xau34CBPbuPs0IICUywx-FbYqr1AW6B5b8YcZH6XIUocXjm5wTPbjP-liqHxGP-U6Xf2wAuQSbh-RXng3lRQ0rVVL1Hh58cDqSqXr46GwcTTzF7Rbnbb0RIWJBFLPsnkbzS3KosmBiNckPntRzygqPteuvZqf2Bmwo90xJnC298Jw9h7qqtm7Sm-EvlnQlPD5SCQe5CynyKM8gbwqAzYx5coIgP7gznISSo-4d4QaU-9ZTZGjxhGNucJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
جو هالیوودی اطراف استادیوم محل‌برگزاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/92464" target="_blank">📅 03:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92463">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfDQU5MKKVbgfQU7GZml0tIQeJ4u_672q93aXgSqvNzJV8ZDI_eQTMOvtsAOvJ3sZUGQFSyOw-fr14JpQhX_jqOqBLbdbxGCk9rizgTqSxfn5BDhHVPgdWawXrsuDCNCg_SVCmHk9d8diIovd0KcufFs2BADkMkSAGEgs7jXJmh_y0DoJsxjv0HGV52CH81QW-Msxq7wJZZT6bp5ZH51LXvHXnfhPdjgm1npqs3_MgPkJzVfQo2yuqsPqorQPnCdDmCbxs6aDoPAdsv7HZR8uhpXM4-SsFLnTDsPD0i1Oh_RghMnmQQra_TtB9eBP4LOrE5ctvjrKx3lJyVYJwfC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇺🇸
ترکیب آمریکا مقابل پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92463" target="_blank">📅 03:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92462">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd835b923e.mp4?token=U70XpIWVhlTFj7ohtuL0zsumfgEOmGiEwl4iT2J7XZHThl0kt-XYo9HWrXyS_PwJv_Lfbqc9m0rnYO66hK5yPCw3uptdgitwtRWcjeuAQXgQMkmVP8af51HoPaP4eAp8tG0_N5iRwOhB81usvl0z4oEryHxq06z-s9wagQeUs2zmB4eM71FAVfuAs4rzEoAiXxcsrqLE9SDY-1dctQHFuG5_Crbz2zMJRXy3yT7kTGfmCN8wodPt59tkbU640MGLl1Ns-wEy9PrIpEgzMZOz_GjZiId-YftOMHlJoyGe4lTezcoM2h1HTqLm_RBBjZl657M6YtlMn98wfYjAj-cQebWFvX3kWyi7SP2hcNc7rAyNg7UOTGd8LPjXgum5_xATwIFWVbPtyabCTeKcGxMdoJHH4P_uV43oJb74UdKS9zj8S2tn1F3ye2hG_s2VXBPNKYdejFLq4OdVQ-BKUCQYJ6Q3lLB-CxchfVnQGbsFnyvbss_ThxlKgc53P6zqE5abmxkvLE5PiAojvUOLKVbULalenwG2osOz8ptUxeysXT5X_oNhwfWr4GFB1qpv3deoK2RU7cGCX8Y8Cao6Dw85AkHBjkwKP81P3XgF9Wrk2J1KXefFHAJXZdQA7KJ2kb4WSjE6QTl41r1VVrIMXciNzl4SG65uKKukXR1B5hLlurM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd835b923e.mp4?token=U70XpIWVhlTFj7ohtuL0zsumfgEOmGiEwl4iT2J7XZHThl0kt-XYo9HWrXyS_PwJv_Lfbqc9m0rnYO66hK5yPCw3uptdgitwtRWcjeuAQXgQMkmVP8af51HoPaP4eAp8tG0_N5iRwOhB81usvl0z4oEryHxq06z-s9wagQeUs2zmB4eM71FAVfuAs4rzEoAiXxcsrqLE9SDY-1dctQHFuG5_Crbz2zMJRXy3yT7kTGfmCN8wodPt59tkbU640MGLl1Ns-wEy9PrIpEgzMZOz_GjZiId-YftOMHlJoyGe4lTezcoM2h1HTqLm_RBBjZl657M6YtlMn98wfYjAj-cQebWFvX3kWyi7SP2hcNc7rAyNg7UOTGd8LPjXgum5_xATwIFWVbPtyabCTeKcGxMdoJHH4P_uV43oJb74UdKS9zj8S2tn1F3ye2hG_s2VXBPNKYdejFLq4OdVQ-BKUCQYJ6Q3lLB-CxchfVnQGbsFnyvbss_ThxlKgc53P6zqE5abmxkvLE5PiAojvUOLKVbULalenwG2osOz8ptUxeysXT5X_oNhwfWr4GFB1qpv3deoK2RU7cGCX8Y8Cao6Dw85AkHBjkwKP81P3XgF9Wrk2J1KXefFHAJXZdQA7KJ2kb4WSjE6QTl41r1VVrIMXciNzl4SG65uKKukXR1B5hLlurM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
هم‌اکنون از اطراف استادیوم دیدار امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/92462" target="_blank">📅 03:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92461">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEeDb3CJQqFJt2RtxyRQCRkLhw4gQ2kQMc-qDb4yB5wk6nre76bwuli2L-1bCu5PpbV5aB0bNZnOJzNE6b2iodUHlU_9YJvhsL6ZL8ilElR8oqVbQ2HtoYr509msmpZyEHZma8va8N8R4hm9mtKh7VaOaSlWCqPRBzBzyl8bHRPSad9su-Z8Fp6cjF_pak-wWokFzSEv7ZHoRHVQZgVSbQKE14EHfxjJUDfeFPVAgSBp3ZW8T4seN-_xDjBwZnt9_XQzHeDYgidI-PowJAx3Jn8bnS2ouumChnWINICTFFaWyvLBPAjjX9Mw2_fnJdJg08Isrd4Re5xDTN8M0gedrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هم‌اکنون استادیوم محل دیدار آمریکا و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/92461" target="_blank">📅 03:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92459">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">لیگ ملت‌های والیبال/ پایان ست اول به سود ایران
ایران ۱ - ۰ آرژانتین
🇮🇷
۲۵
🇦🇷
۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/92459" target="_blank">📅 03:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92458">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmN-ELYKWuxaaooqYwugfk-aFE9pRhdz2hTmkTIZQaBgkWTcD0HQ67C8Uge55n09oia_fVwqhDNK1HKOxWonuLciJjPTMmgQt44Ywck-5FnrTdg3kg_sck2yq1DsNPACE5S9EjT00gK-rAB4amOTXGyOSjk2UUe-aNLyDRUiJk5XMKMjj6ufsD0RYvkFn1_imVYnRSKC7v8PvWDPnakR7mQT22pCSG7VzLLGOAL6lFLdgu7wDRELTOC4towhGg4Dos4aTb68D_IgE2svChv1Of0NtC9zxxfZ95EIex-XbsXsdplbRUmszIJyA9hkWZrx-3UMX1QeyS7vaWiZ1SES_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
ترکیب احتمالی برزیل مقابل مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/92458" target="_blank">📅 02:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92457">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0PVIz8ONTyiGUfkhbCUkqZmrA7qb1CzRtKzfPgayoOWYmrf-WbWUshvo_D66-kZxIoAxR4XzvQKiSbvxhsGtFJcCbafgJy3KRCE8N4xZDRN0-IxwD_-ovBgMyplufM8cCp5E9LCWrhBKY8Fjwb43ZRzbdwvEi7hlOr6Y3p5G_a5TbabIdbn6XxQ1xnX6u5XNbSlBShn7QPCDtYSZI4OP4Roccsx0IcP8x4M6oXz9WvmfumeTgWUN6BCXZ_RLsI0-fJf0bvS8sfQKUeXk3Jy0RIikhPaGoWt7qzw2ZKmIWdhaGX1xPjeiOJ0O2sBDDCNE69pV_77j6lSXJaID4bKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
رسانه‌های خارجی از قلعه‌نویی چی ساختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92457" target="_blank">📅 02:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92456">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea6577b63.mp4?token=f_D4BnhT8mI6eRShz8tZ3FJTAeJBu9xOdRQZUPTfgqlCGljUVS6FoAbZnvy4kHEH8-Q0IsDJ3g0I8nWDiYa4nrKV7SjUv9iDfYVC1yIgK_fS--hUb_4rwrom-9qarwAKvX59NP1e_5vuRzepnTgeoUI6pSXDOT8cc9Ak2ePqZb2KmQllZKQOucRzPKzz_7QVwVxwkz6kFCpAmXyA4kOAth9Ijtu6kVxMSRLnL7Aww_h7qDMawc1gAUl7BOzOG7WJZd70vXPcLFFcxUNtFo27VZ_9J6ku-KtrA3sSPZ_I-udVA4vMTFy1gB-WEJUr4e7BUHJSkC2OJVSHUEou0CI8xDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea6577b63.mp4?token=f_D4BnhT8mI6eRShz8tZ3FJTAeJBu9xOdRQZUPTfgqlCGljUVS6FoAbZnvy4kHEH8-Q0IsDJ3g0I8nWDiYa4nrKV7SjUv9iDfYVC1yIgK_fS--hUb_4rwrom-9qarwAKvX59NP1e_5vuRzepnTgeoUI6pSXDOT8cc9Ak2ePqZb2KmQllZKQOucRzPKzz_7QVwVxwkz6kFCpAmXyA4kOAth9Ijtu6kVxMSRLnL7Aww_h7qDMawc1gAUl7BOzOG7WJZd70vXPcLFFcxUNtFo27VZ_9J6ku-KtrA3sSPZ_I-udVA4vMTFy1gB-WEJUr4e7BUHJSkC2OJVSHUEou0CI8xDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🏆
#فووووووری
؛ خبرگزاری‌های مکزیک: امروز نزدیک محل کمپ تیم‌ فوتبال جمهوری اسلامی یه جسد پیدا شده و پلیس درحال تحقیق درباره دلایل این قتل هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/92456" target="_blank">📅 02:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92455">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
#فوریییی از رومانو:  نیمار بازی اول برزیل مقابل مراکش رو از دست داد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/92455" target="_blank">📅 02:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92454">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khLCDxI_5tIeUiG_WXGmStLiPZUGh-ixzCojKZ8SXGKM7jIiakzyrwBAFskCpq6MSHx39EKTssZFL8FbRdqWRLgcmh5rd01_qDpcqGJlctObv24aOspoD6bi1TCxvUj5XSkyKwGSgAkmuKKKZVVoBNfXLh37FuImOjEGcrhEpqHJiDrcQk-Du8sX1LnDQC3zFhGv1ASRCEHhuZoI-igWHSzW_i5m2btOxmFN80t8ozigWvcPBpEZOffyWlz_gDuZb9A7sELYwcImlIypr0ZgNmgtUEMq1ndZe8lDVuV4EBL4_0LS1_od_eyHGe1rnZyFNtB1Eb_zJA2oKAGbhfXLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مادر دختر پاراگوئه‌ای آماده بازی افتتاحیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/92454" target="_blank">📅 02:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92453">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
از طرف اتحادیه پسرا به دختران مملکت:
دخترخانومای ناز و کیوت
🎀
ما نوکر شما هم هستیم ولی باتوجه به فرا رسیدن جام جهانی و لیگ ملت‌های والیبال، از شما عزیزان تقاضا میشه در راستای حفظ آرامش روانی، حفظ تمرکز این حقیر و جلوگیری از هرگونه دعوا و قطع‌رابطه نهایت همکاری رو به‌ عمل آورید و از انجام موارد زیر خودداری نمایید:
🙏🏻
🙏🏻
❗️
پرسیدن سوالِ «من یا فوتبال؟»
❗️
شروعِ غیبت با پیامِ «اون خرابه رو
یادته؟؟»
❗️
ارسال پیام «بهم زنگ بزن» از دقیقه 60 به بعد بازی
❗️
قهرهای ناگهانی همزمان با ضربات پنالتی
❗️
درخواست بیرون رفتن دقیقا ۲ دقیقه قبل از شروع بازی
❗️
بلاک کردن به‌دلیل« دیر سین زدن» در وسط بازی
❗️
ارسال هرگونه عکس« مدل‌مو،مدل ناخن» و انتظار ذوق در وسط بازی
بدیهی است پس از پایان تورنمنت، تمامی ما مجدداً به چرخه عاطفی عادی کشور و بوجی‌موجی کردن شما بازخواهیم گشت.
#کپی
شما هم میتونید به همسران و دوستانتون این متنو کپی کنید بفرستید یا فوروارد کنید من که کردم تموم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/92453" target="_blank">📅 02:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92452">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxPYP_4qGYvSfNMX_ovmwPTEzS_Gp5M3fB_20-625fv_kDh5Qaih_TfSqZVx3DVODxUucZPk4Ix8mOwiOH2PwR2R0NFKNmNTW6fW7exuWGz4YTKDnouZFdBCfGSWCu-X8iwYoiz98JAg8oZ_ybbRehXpihFC3lpZBALF0IaBqcyjOMjGiWSmCet-ipeh_tm4i-TsU92zNPe_TlXmQzrZvMKr2TSenBBp5g5MYbntzyaPE8f8qImuYE6z0c0s8njCUEak4cDQbV2w2BrS35gRetmkXiguF-qVPrCj__wao4EcgBRRJgbeEWCr83qFHTClanjyzEPtIweIiGd30jK6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
پست‌جدید نیمار درحال عشق‌بازی با زنش تو آمریکا با کپشن: خیلی دوست‌دارم بیب
😊
😍
همینکارو میکنه که نصف سال مصدومه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/92452" target="_blank">📅 02:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92451">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCe3tidXanle4QQT0aNYRoNBpP0oWQiEN_N9wnnLZoq3tKzKFrQLFTdJTM53t5QzXYUzI6TdMsgUsMZxwWNXmqCJmmlR74v9XPiGG2846FgA8F4WAUtXK7MHRvu6f1IpZOgxoRRYdV8go2XJzP3EXbCoemOb1JHU5pYtPNQgkhX2KeJH4Q8uaWhhgQtdflfQdteqmeqOC1w4lASZumkpUEsTvKZpbfYFlMNKrNDfCy857muNGnoYPYrsnYpkaGXvM5m-BczJSfYW4C8PQqcVq_y_-iF2EHxTM45lL-E6ACubAT9LPBs2GgWNtk__-G3LXD8p0w8yg93TCkF-Azw0JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوریییی
از رومانو:
نیمار بازی اول برزیل مقابل مراکش رو از دست داد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/92451" target="_blank">📅 01:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92450">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGS4nu1FhZoWKGrMZCKkvQbv416I8iUu750BVCI6E9GXiwaMY_Km9xrZKMKTIv4rmF5dqZJmIcF5BUh28NSE3vjp2ZdScSWqIiJ4GhURZBgNZuO5mw1PH1ekaBxKlDtUWPntbw3PiTWME44mBE11k0ccWtHfyD0ArgZLsC0T_sRQCNaktcTHhmM-epRD2panChsvIB_pxYbvDg8zDfU_DioQg4rM24BiGJD-_FAHsr-VTEjTbEIS-rsYCKUP-OWaGucaTJ6WGtN0bQULuShXrsDG2kBN9H2tRfZl6rzgf4Z4PONBrXsUqW6apdPVemB6G9iar6Wykfdnx1NJQUYGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زنده از ورزشگاه بازی آمریکا و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/92450" target="_blank">📅 01:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92449">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMIvXTm_CHCFUpEmA_PkB5Rzv3gU4o43X4wg9guKGLa9ScR4E5gBwsfIhGyOpElX_HGjEEB9sXAKekFtSV8lblzi9_1Se1jGfWQPwwDB5ib0kUggNLDUzgcadC6b8VY_mNPFQ85ZRAd1R21Xxft1s28ycQ6lcn8QCEDIDLvD1CC5sMcghZhafx_-HAPdYyJDijMczjNYoQ7FWp13LaQ8NlsLlEp6tg3QEDErJCx813wpiOv8nQQaOIzwSfX9WkvdD9aRnQIAcjF9FzWITnVDE3-r3uLuFIzGFdNLpI9KsIpLJ08tQdH6HIkbIyZ1377ZCGhPGXEANXMkGdj4RH260w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ترکیب تیم‌ملی والیبال مقابل آرژانتین؛ ساعت ۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/92449" target="_blank">📅 01:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92448">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCLzQ08rv8UzaG_K6fmGIQ-Tz8D9KZCrjUXxGNgABQQmpTkBpYr_8Tb6qIA-wNnGXYa4czbUf9ucDoNtKtxfFGfh9uUfn_UNFelVewGn-qrJvV709IO_ZSTNYHAmXKAhpFTI91ypy5UZU_hkdtfqqUsxHJCDTqgxxxDuc3cr7XoSTRqG2srwqzWwA2fgVOSKCL0hAImeRV-KUJG9lpTs1iGA9dPNCxGd3ZI0S-A0y37wG5x__hXcc13l71_lZnB-w39eSn4Xn36cYyIesW4LkBoOnZTGqiehdTQKh5BPbkRsYYJdqjz5Zv_SMLJwZ4I10WtEd0Gakn883MyGfz3jhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇷🇺
🇷🇺
#فووووووری
؛ رسانه‌های روسیه گزارش دادند که پوتین به مسئولان فوتبالی کشورش دستور داده که تورنمت جدیدی با حضور برخی از تیم‌های حذف شده از جام‌جهانی و تیم‌هایی که شرایط سیاسی خوبی در جهان ندارن طراحی کنه تا به نوعی تحریم فیفا و اروپا علیه روسیه در بخش ورزش به نوعی خنثی بشه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92448" target="_blank">📅 01:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92447">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujad1yP1ipKyaBNCnRxBERyY2BBq7Yvj7svrJqp0bLjkpTrwU8nSqlA8Lkv5CttCUwRMUiE38xUxyCYjPcryVwcwmLYZ06TudCyzTLr1_YKcRDCSnGRfQg_RyUVyUUO5WXHfxfQoEt-I7bZB6T54Te97WWiZApItpcmytcpCcHXWjgx03d-X2sM8S9TZlstrSPjJNMbyCJcvV24o-ZmhS0MYYcg_EU1Xu-aPXedx_cIabwX8GX4Y-ZKhSgEQsvOWNAdHglkd02i8wWe3Sk1A8bJ-eHUuWAbSHktHfC0Q92gBy3Rw92A-2XTgzLeAz0RbR21kSXeIc2qcVUjYTtNWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
هواداران پاراگوئه در آستانه بازی با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/92447" target="_blank">📅 01:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92446">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXlIIL_lwygwPxEIuGv7vH7JTdHZoE1axz4teucVOUmN4d8SaGPWRwWIVkGxHe-htQilbdcpjOCviTN6J21lJtt_3toQamWiJSTk0J0O552vrbjHa8ocHBfQ7ZdTAAki_FjCfmKqu3OFXxiferX1nyUnYBPHOShFfDk080Nnc89zQULPbwarlbElrLilbzgBrdXGHKsN5iqmOonMYkEIEbrDyifYNUbpzTGIE5Uj_Iz3JijY29mCYQFp_1VK-MJt1nBrmetO5d0PjCvkzR-S9L8q4J3uAGhe7ISyRIzAhkuz4kPBNniJeLzLQdsh_JcMnd-c4hcOSk0NZ90SKyfagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
#فوووووری
؛ دیمارزیو خبرنگار ایتالیایی: پاری‌سن‌ژرمن قصد داره در صورت درخشش فران‌تورس در جام‌جهانی، برای جذبش اقدام کنه. ظاهرا انریکه از سبک بازی هموطنش شدیدا راضیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/92446" target="_blank">📅 01:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92445">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kD7teyNhJrvdcegBouUCQtl4gB8KZIDBjuselEJm1bljT1ZbowuawFcnXaAsOYWiJ2dJDCPF75yDJNQbuEkBv2Vcj4VV2Ir5oNZ-QurxGiy6wEAE_Y6kneC1FvcUr4m3I6lR7up6w5jx3ILSWHHvpW6zIExhNpBa4Zq6SNT9mkfLwSIat83WwR1hJ_l6c12HzDpJo4RZjmQtZPnyQYr9FdQUQEJPZjLJ_PJimGerwXy2FYaZdmnZgKWAaLSvvvrnh8XUpnpaVJBZd-jOUHNEkuBYJ0pYEuPZnDnziHeS_-efhr_YVMEhmct8nkO91MRcwv5S3F03ZjFaPLFQz5Angg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کونی خان بهترین بازیکن بازی افتتاحیه کانادا شد
این چه اسمیه تو داری مرد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/92445" target="_blank">📅 01:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92444">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9dd472ef5.mp4?token=rfBX9_9Zbz1tCwaZeVqFGXmQXbMbzYu1kp38xM1lLPf7faikhBb1HFYsgCmIKWPm8v5gx3jRKsdCvJ9E6RfuBaF_z17dThnaSXy2ha9pBNsXtZJ7c0Rsxspq4wFtQ2oFpi3XyCn9vzYz8iCSYwE4hiwQbshswTlLxctX1mpp83OwzCOXPdo44DBPQl24e9voFGc0EXNlSLkb-NBFG1_-gSdpn2yBkpPwrG2F_NEzhB9xvEHs7ok5QAc85fbAZRntcuQlEdzeabgzEKfBeErcToA-XQ8KxPLb9sZCu-aMuTeg3dtZ19yvKDITKCSwvY6HIErOhNJIY2iAdxDL8IZ99Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9dd472ef5.mp4?token=rfBX9_9Zbz1tCwaZeVqFGXmQXbMbzYu1kp38xM1lLPf7faikhBb1HFYsgCmIKWPm8v5gx3jRKsdCvJ9E6RfuBaF_z17dThnaSXy2ha9pBNsXtZJ7c0Rsxspq4wFtQ2oFpi3XyCn9vzYz8iCSYwE4hiwQbshswTlLxctX1mpp83OwzCOXPdo44DBPQl24e9voFGc0EXNlSLkb-NBFG1_-gSdpn2yBkpPwrG2F_NEzhB9xvEHs7ok5QAc85fbAZRntcuQlEdzeabgzEKfBeErcToA-XQ8KxPLb9sZCu-aMuTeg3dtZ19yvKDITKCSwvY6HIErOhNJIY2iAdxDL8IZ99Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرکی : شب اول تو امریکا یه دهه برام طول کشید تا صبح شه
ساعت 6، 6:20، 6:30، 6:40، 7، 8 و 9 از خواب بیدار شدم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/92444" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92443">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa48a9b18.mp4?token=JxIx7RfFTBxPd7WShJyXSmMCugK_SlnM9dwa3_YhKSE0Rfvo3LbA7w8n-p4S-IMn1XuNh6X66NH8J-SCbvL8JPtL1TYTRbmZL8dwdjt2Nsa0mqkU19z_Y4SP0F_oXJosCtAzKWyjp_jGXOgU3uEptwS8Pbm2pIrOL9KAGFoKfzgtifHcOb_ISJUaCIHqOSkBo50IBVKg_SRNldbuFW5s_8WgwhkeXUkKw90DgGH2ISmh3HByDHVMkHlD5wpK_P_4x9bewVzyHCfN_jd3WZl1OnjTU2NyrjzU67SnxMwdpf6Fr45e4IqAmZb1-LELZySObvoGxFreMA7RF3G6QZ00iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa48a9b18.mp4?token=JxIx7RfFTBxPd7WShJyXSmMCugK_SlnM9dwa3_YhKSE0Rfvo3LbA7w8n-p4S-IMn1XuNh6X66NH8J-SCbvL8JPtL1TYTRbmZL8dwdjt2Nsa0mqkU19z_Y4SP0F_oXJosCtAzKWyjp_jGXOgU3uEptwS8Pbm2pIrOL9KAGFoKfzgtifHcOb_ISJUaCIHqOSkBo50IBVKg_SRNldbuFW5s_8WgwhkeXUkKw90DgGH2ISmh3HByDHVMkHlD5wpK_P_4x9bewVzyHCfN_jd3WZl1OnjTU2NyrjzU67SnxMwdpf6Fr45e4IqAmZb1-LELZySObvoGxFreMA7RF3G6QZ00iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
زندان هم زندانای قدیم؛ یکی از اعضای تیم تتلو یه ویدیو منتشر کرده و گفته که آقا امیر(
😂
) از پشت میله‌های زندان باهام تماس میگرفته تا موزیکشو براش تنظیم کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/92443" target="_blank">📅 01:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92442">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=vsdMcZQ8DaFkjNL71uVxJEdMkQ2TYI9_BLGuu-bo3GNfO7oJxpUrQzb5VtecXc2B7pbvYHFlNgfyL73cCQSpvSE4_Qi8_HFpKSbLewLp_4s1iAF3G5OWAAwHyfSAu_yqMDyoq5WCcCfrnEoW58uKcP6mEXsV-qBb3VkJb-uy9ofYQUEMOml9h7hNnEfuShgzTY19fS7qJjgym2fE-GZqKmsDJt7qUnPgFv4SflRl6WRpqmE5StM4PmAWCht16Fyt06g0YryaGfQFLMrCDXSl1XrxinDXNb_wbB_O-a3LePy3h1V1QUzaihrWwqdjU5zsPmVE966XMIhFFjKg2kdH6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=vsdMcZQ8DaFkjNL71uVxJEdMkQ2TYI9_BLGuu-bo3GNfO7oJxpUrQzb5VtecXc2B7pbvYHFlNgfyL73cCQSpvSE4_Qi8_HFpKSbLewLp_4s1iAF3G5OWAAwHyfSAu_yqMDyoq5WCcCfrnEoW58uKcP6mEXsV-qBb3VkJb-uy9ofYQUEMOml9h7hNnEfuShgzTY19fS7qJjgym2fE-GZqKmsDJt7qUnPgFv4SflRl6WRpqmE5StM4PmAWCht16Fyt06g0YryaGfQFLMrCDXSl1XrxinDXNb_wbB_O-a3LePy3h1V1QUzaihrWwqdjU5zsPmVE966XMIhFFjKg2kdH6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
دیدار رونالدو با یک اینفلوئنسر که طرفدارشه
دختره زده زیر گریه رونالدو بهش میگه اشکاتو پاک کن تو خیلی خوشگلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/92442" target="_blank">📅 01:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92441">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92441" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/92441" target="_blank">📅 01:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92440">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvDK_6-LufwXvHx6VaH9KAi32kApA4XnzE298-kJc2YujpU0EEMnborNWtDlkK7BduHduc-dQXFtUwscy8Z7bQ4_d3pVS1LQ7BrGFoAD6cTLato0m0yaXaL0qZ9yJ746XBuXMoRwH4-u3c_Ry6CCXGsz-GUcdUQ8deKWRTHyYNf5qj4hBqLY8V7CUC8u801pG8zcpyyBqThYiu0PkjwxUOR8VDQjFU3jKMZRqWvTl7vw3phvYJeREYqw7bhI1LG918AQFCP-Nd6o8BTo2Qjv3TElQuGbAsr_clJwW2erXcAFcgNAtcVV85ar-lyWodazVJQYMrrUIf3WeEdkNSsoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/92440" target="_blank">📅 01:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92439">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a47e4dd2a8.mp4?token=lxOfw9e4nwcsjXXMvQkGk0_NWtaWSDt39MhL3z6tV5xhuPCUOLn3a2Dkr00MSHS2oGa5Te6t6TVKirwzcFCgPbA2EkZ1fVPa0KBf4aZq9z_2vkkd1C7UX3bBCgxi3QIqKWEPglMVK077KAsunB03JpN5ePb8jDhNU0GGfZ5I0p1ZN6GoTQlXWus-1FnxHnXMwiJayHa4EPIcRSH1p7s5l2fhZSRTl33-lKJONgM9Yr3ZJNnRBq-bZPVAwiVgJfsC4JRE3r91kZYUfhyzi_kHv3b6vVRsK63YK4TXb3-jiTJGvI_uNGWFx5jZUgPhR-49JjIBySGE7XgSiAcT6vYhBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a47e4dd2a8.mp4?token=lxOfw9e4nwcsjXXMvQkGk0_NWtaWSDt39MhL3z6tV5xhuPCUOLn3a2Dkr00MSHS2oGa5Te6t6TVKirwzcFCgPbA2EkZ1fVPa0KBf4aZq9z_2vkkd1C7UX3bBCgxi3QIqKWEPglMVK077KAsunB03JpN5ePb8jDhNU0GGfZ5I0p1ZN6GoTQlXWus-1FnxHnXMwiJayHa4EPIcRSH1p7s5l2fhZSRTl33-lKJONgM9Yr3ZJNnRBq-bZPVAwiVgJfsC4JRE3r91kZYUfhyzi_kHv3b6vVRsK63YK4TXb3-jiTJGvI_uNGWFx5jZUgPhR-49JjIBySGE7XgSiAcT6vYhBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ با اعضای تیم ملی آمریکا تلفنی حرف زد و بهشون روحیه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/92439" target="_blank">📅 00:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92438">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuQdHI2YGIzQltIlN1qXrWjW56dXtWWuH0kOHBBO34pXf-wziBx3C0104uCoCNLTiU1SKzoN5XRETAr9jx_TBTpLXWcOcKA48xs-ftuYtlp-euibJ-lM8aZ-TeO9_i9n8baN2G6KNNQ6YqA2qIepzmQD5mXLR0GM_ZK4RSjnrgX-dl_41vrLmPYuDHat3SR-TlGnh6644BKjFZiuizRDu2IpWfFOW3mTW6ruklrPxtkNQHDwHKzD7QH4_sGI3AXXTNGikD3sD0F6DHdcKQ7YgFqYIsFAsEmfiUFWl04Fy1cHOupSLYIgl0ncZQZIr4cPJA0vUFXTUKL6aXe5RjEtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇷
طبق گفته رسانه‌های آرژانتنی، خط‌ هافبک‌ اصلی این کشور در جام‌جهانی متشکل از این چهار دوست عزیز هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/92438" target="_blank">📅 00:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92437">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2gUqqWQZYdEMATq5bgnFjyoCd4LplCRTp-vXxGyffhg9p9Uck2z3dUR4W1iPoe0_uDakKD4FpD1GVfclm42L9xCZtYMix8E8MjOXHKWeU2hvzUZ1dw_sTsiNfz38HtXi_0umu4PMwZgH3xBjmkwenXja8Iyvj1neL4kgdzE4vzUSirodCIxZaAzeZb6e4Yvx8hKOviWPT2No7hoVsp1RICOdIN5PIRecJuROAD0Ujht5ye71bHWo6LFEdXxYEDy9V8aUkZd74oJDN3OWfZFzawmUb_R3wTxxieVcG3mZNxMaRu3-Ev-MCDJKi5Ua3qV1xHDG5rQttVnRYmraIHfkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
کمتر از ۴ ساعت تا افتتاحیه سوم جام‌جهانی ۲۰۲۶ به میزبانی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/92437" target="_blank">📅 00:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92436">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjTcdL2N9gPuj_3H3Y0yWtdcKd3nLlQhHPG8sHfyxIJL6enF_rFLsQyKC-6z7DBBT1HP8CVmiUGOSri1kg927M89Ndz8ZpzawM303dWQMGNpuLL7qsxquJb3t7f1ckYkAfimd8oHaYcPBvcDlXUuZ8lFGhOQXuh8NG4By3171z72CDOYB_th3lqmB0SP_mCiOw-JHsWTTUGHfnXqBtWT4QuaE1mChf7LQ2ADr9w-hZMO2zZjJ17UB9I71ao2Na_fDKGdJWW8bU3Yg_xAJ-fbGWzUAetVuSEX1uhp9CBNm0EzV1ZmoiHMPPlgqIU2nUzwx8MfGrNPSetSk7UMHc9VDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی بازی امشب بوسنی و کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/92436" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92435">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZF953ukFrXePehMcTPZA2oK2BM0xQ3VKLLSENg_O_vZhyuNlhEI4Mq_OoKmm4YghPeY2rIAYTQDSgWqPHESlhcsY-r4AIVnhSeEuwol0TcwsMMflPiHUbp_Nwq-0Ku7csJE77L0kIOsNG7g8kmMNO3vAj2GgZm18zD5Hu_--3t7AEJMt4QmPS3N0eO6ep2js5CULKaXdQ4za0aiyTCWv6f2IQF2rzWzU7axkXfBpjatxdKk3t3q8BlQzB2zZnxrhvkeDtYtB1KKk9HRUkEXYHsZyKM4PHbgFomxGkwmbVvoRno3uoQKrYWUjX0k7sKjjUa9l1a8khwMBOEbzPwXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|کانادا بالاخره در جام‌جهانی نباخت!؛ میزبان مسابقات در بازی افتتاحیه دوم مقابل تماشاگرانش به تساوی رضایت داد!
🇨🇦
کانادا
😃
-
😃
بوسنی‌وهرزگووین
🇧🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/92435" target="_blank">📅 00:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92434">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">#فکت
🇨🇦
کانادا اولین مساوی تاریخش رو تو جام جهانی گرفت همرو باخته بود تو بازیای قبلی
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92434" target="_blank">📅 00:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92433">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHW99lf3Cwf-oU1La-QJYl85tIcUzaOvfi966GmCCwgJQ1VCRfT4M-pP3ZoTyMH4a7kha6KEy6FgkBUuFRtrgQoEuli6G9kr2A16IDXrb05gktDuOWAAu3nSxyK5FLWXzu0IibqF79BdoYHdfLTGxAlsODfzW8q1IqoaAx1PSFyfSWjBdI84OUWRYukYEYi-3FcCWtwqCTSpq2SEUZsDTpSN020N0TncibPZsG-V_lFFZlwYmehtxurom0HKFFLJ8BHkJJopmrxQ_sU7cErBZTftkqEKvvB4XK1ZfWLA2EKBYRekxAt9pc753_6yUNxbxtrao-b36UxjnedgQC1IBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|کانادا بالاخره در جام‌جهانی نباخت!؛ میزبان مسابقات در بازی افتتاحیه دوم مقابل تماشاگرانش به تساوی رضایت داد!
🇨🇦
کانادا
😃
-
😃
بوسنی‌وهرزگووین
🇧🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/92433" target="_blank">📅 00:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92432">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrreH3y8uFTw-TN594KBO5u27CS1TrWdZ99xdYBixQrS-w3eFCjsDdc_fdWcWlJJwfUOBzpG4ZxgZQk1vhDsANtL-pRYNa0wMnrNYDIBEc5OlKsSTT_T0PQL9Vfp1N7Jb0C30Y1QXq9q6OfFV6YBFObBefS-7nqT1rzyRSwRyEl4NxnTJbZhGr5dnlpS-xR7PITDFyJ5LxM5C5eqXb4skCClWpbejTzB7E_cGmy8U2EVGLU-l6Ju29eFOl4wckagIpkGQ4tCUC5Gw2t_4zmG2pevV8qnNc5WjAReyy_8WyYOa2JECY24bzZ8uKCSQeFd-oXQoVPxgBBxDxhBbYI6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇲🇦
مراکش
🏆
جام جهانی ۲۰۲۶ - گروه C
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه متلایف
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
- برزیل پرافتخارترین تیم جام جهانی با
۵
قهرمانی است و در همه ادوار جام حضور داشته است.
- برزیل در جام جهانی ۲۰۲۲ از گروه خود صعود کرد و در مرحله
یک‌چهارم‌نهایی
در مقابل کرواسی شکست خورد.
- مراکش در شش دوره جام جهانی حضور داشته و بهترین عملکرد این تیم کسب مقام
چهارمی
در ۲۰۲۲ می‌باشد.
- مراکش در جام جهانی ۲۰۲۲ با حذف اسپانیا و پرتغال به
نیمه‌نهایی
رسید و یک شگفتی بزرگ خلق کرد.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92432" target="_blank">📅 00:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92431">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMfDkF-Ix4wlnFpofIBO5YLtYVK06ufll0PbV7K_yeapAQgzvPJMdR-A7KjWY7t1E3FTbIFlS6zG8d5QpP1Wb1kzJs-rh5ucpUan2-cOTKl3UT91CnfXKqZLPDf6mjnouhKiSc7VKaR7-PnC7KtysyTDgUTVCVVhPYRNW7hgj1o1Rum6c5kPYY4AH0UOTq08sG3w0nnVeydBI6qh64oAOucIHiuyRyrwclt9bbAHZZ-pHK-8aP19Q4LRhV7tMdSyqPrT8xVOww_y0GXWInaF6_vATmpceS6M78U_BkbewQ8rPI9H47241iqnlYLpuk5SMTnrhuIj6rPaKHxDNq4iaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
‼️
توهین‌ناموسی محمدحسین میثاقی نسبت به منتقدان تیم دوست‌نداشتنی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/92431" target="_blank">📅 00:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92430">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blhG6c5DOKF24JUD8K1Pjgs6EB9uI3Qlx_N_a7eSrdxmDPDHWAeYrlPqBU3CoUwDTOpxz_QF9kbKm8nFgLPSXNlPu6ZDA9RkNkfd2bgqYf191uRsmmGDgSAo7t2Aw_T8K_WG3VHzA6OeDnDoDeS6WWIsCCfHrEOHnkuSyW5U1OKJ1RiK5wBIHtC7FThMum7dH6LUBq3lGDF4v1iQ79l_SeNhrpoxtFCeg9u6bxWYvmRUyReslA1DtpRvgDirCmcRBap3WaUzGBBijBE1jXji6dH13F_ptAaNEsTLDX6GQe5fA_I4y7Q8w4MwrwU0ID8VnCKTcO5oGkd6abSdrHa3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
گل‌تساوی کانادا به بوسنی دقیقه ۷۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/92430" target="_blank">📅 00:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92429">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇨🇦
گل‌تساوی کانادا به بوسنی دقیقه ۷۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/92429" target="_blank">📅 00:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92427">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گللگلگگلگللگل تساوی کانادااا
⬛️
⬛️
⬛️
🇨🇦</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/92427" target="_blank">📅 00:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92426">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
‼️
‼️
توهین‌ناموسی محمدحسین میثاقی نسبت به منتقدان تیم دوست‌نداشتنی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/92426" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92425">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c23cc9050.mp4?token=l_z88YQ1ZUES4ah_KiQx46SRCnkmd4kApfvLTAR6mQb_4EW-KWjOOhIAnIoakXR8jpPEKGZdU3ShK_JEj67IruYYqBBR2-v3i-JGyr2YDeQJKzCaK2Jkd_QtshP73FLYMJvWXtxx49PqQJsQJ5skHY_ljExZ5CHu-z076dc1qmrR4EXBQlJH5h0XXsDNnf7BzU9_y-86_U_INa8AI1Fnb_DRwvi_KyUW4YOEmedx4i7P-CXDq8v25YLwi5P_7zDq4R_L8iouqj6ieUd0eNgo6Igj4faypEskXjg0dnnOOM3AxQOv-7ksheTRYvKWJjoSnyJtuO5b6_EO2kBei4PM1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c23cc9050.mp4?token=l_z88YQ1ZUES4ah_KiQx46SRCnkmd4kApfvLTAR6mQb_4EW-KWjOOhIAnIoakXR8jpPEKGZdU3ShK_JEj67IruYYqBBR2-v3i-JGyr2YDeQJKzCaK2Jkd_QtshP73FLYMJvWXtxx49PqQJsQJ5skHY_ljExZ5CHu-z076dc1qmrR4EXBQlJH5h0XXsDNnf7BzU9_y-86_U_INa8AI1Fnb_DRwvi_KyUW4YOEmedx4i7P-CXDq8v25YLwi5P_7zDq4R_L8iouqj6ieUd0eNgo6Igj4faypEskXjg0dnnOOM3AxQOv-7ksheTRYvKWJjoSnyJtuO5b6_EO2kBei4PM1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
‼️
توهین‌ناموسی محمدحسین میثاقی نسبت به منتقدان تیم دوست‌نداشتنی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/92425" target="_blank">📅 00:05 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
