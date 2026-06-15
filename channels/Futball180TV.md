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
<img src="https://cdn5.telesco.pe/file/nsTl0sBdmqKtcYk2XxsvZzO3MDGr_0MmKNM2vPW6cUdNGivhTgOpC3D2O9WdMpTfXkxdy_X_3YHCtxsg9MGjBc_AITRIpG0fpJeWJ7mJa80CHfXAosuk4tpgCaSW7YKyE2NIkkcL-37f-ZrqH_ROAk3NZfOmFsd-8ZR9MiVuRYefRGDilIMXPobAyyzMr7v_s4K9Kee1rYPETDpAyThQnwZwL1tr3HwJky8Ha9xBUCaCRkSux18tdJ5eD-sgN8wDLjdy913hrksyJkDjR3PoHvJ-fy1cy65iog5x31JFVW67Udi9RmYhYdAGnOB6Ga3IiNbPV0NyLyF4p0XI5j3AVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 580K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 03:17:21</div>
<hr>

<div class="tg-post" id="msg-93425">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بالاخره عربستان خوردددد</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/93425" target="_blank">📅 03:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93424">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
‼️
#فووووووری
؛ صداوسیما دستور داده که موقع‌ پخش بازی امشب، صدای استادیوم قطع بشه و ممکنه سرود ملی هم از قاب تلویزیون پخش نشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/93424" target="_blank">📅 03:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93423">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xc8jIbP_Tld41vQY-e577ZlWrIM1m54lpiv7Q4hHBgfPfugDezvbUpwOwC-sWeOgmrERY53HJXTXyIlnj5A3KD2XkGLJXK1B5_zL1-Qin99STjv8hsWcNy4cc9cks-nnFLNKDR49pdJy64LQMUhCmow9lF1oZOjpkQ465d_YwVOKK5S12ZrTc9vWHGs0munD-73W2A6_iIjd99Vc7nHepdEKu8JVqg4APgJhGFgTTAkRscEAabtt4o5Qp5ldbXnqY2q1eNI84RP2BgQp-iABHfriFXpC7Jo8Ve5tfDOBl3GokrQc2QtnOafAaBmHo8tWRy0sV6z6n13TDiMQa3-Ymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب‌رسمی قلعه‌نویی برای بازی نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/93423" target="_blank">📅 03:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93422">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گلللل اروگوئه بازیو مساوی کرد</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/93422" target="_blank">📅 03:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93421">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpCh0vvFLXaT0EWwmIz2QE8ZelHsOHh-sGk9hZjpVYC9FbojqthcSXbfVl9E34Vc_k_JR_qfIktXRAiIJKGLQJXoMBQv8NjsR3yqE5_MkD7TdpM4O3zkhgMjOV1ysu9MwwMuwt7CneP4sXNTR1WZLz35QsPU5y7IVK0Gev0OBycshz5Vjxkm0n58RVPevRhM33m_THmRd9-dqN7v4_73SZiCIC4a8MPt3DL1EU5Cgup5KOLxPW2bb7sDi86k4h3GJz_k_0rrCldSEIv-z-pbY782Bm1xzpBTXcqT38mf9tO9YqjFsDCEzGdAqdMf1bvZqQzJC8OqBZItUcHeaqwZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری دیگر از هواداران در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/93421" target="_blank">📅 03:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93416">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ay6IPdjn7wOe7XxuSnudovWIPE7a_yEb3ngZgHGOp0WEm-_FBg5dLhezeM7bVRXYZ0dDoxhhLA36762k54okhKh4XAB3RTgjgbLKZASBP8O6jY9KKBaD82bvI0mwqWLYqXvWp4w3fvDyWfId9A9bjUkGoRacf1-vUJYqWHmPu4f_-CkzTP0gZHCFx94nGfLHiMBZI28zpDHr87KVjA9L7LnWFOZZfKo4k85ne4na7BtkfC4D_XkwWEaXVu7dhlx6I3FIPHZXMiRHhUQmDqx2XcT-8C0jvJFPpn_1rc9YWMxgiSkioqDJjdawHoGbPM_C3R0g29pWHiP82VHFpvK7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4R2QK5jlTPumxpuyKmFaWE8zsNiP-oxWV7No3iYU96pyWxQtn-B6APIGpnOCaDCus2Mj0PORofGg4TCeoRGcvRs9tSek-Z50xHz1xKZREEtNIhp869rjLr-Er0ZE-4_PviTdzXrgMYGhcLA2CfX3kZ3rUVHUx3gYtzCOdhvXXozEZfBDRCE1Ev9rqKtOjYG1z74QrgwbBXgtA-zIGuTbtV5d7PYntd8pSpxr4cj_xz8CyjCm1A6DMrBGU0wSsw27TI6o_iXzxRZdQMzN5a1QMtPRTcnVQ-J8EwkMDUJa8f2ZaN2G_O4Tj-wWGjSAGWbJbwQpKCUlHHnKUkKvhJ6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMjFGoEPEBMBWg4cUTKWegLkq2kkmO_j77Ya27xUGTYxljL1NWlvzAr8V5E0wngVYTiOXVWeiMeiK46Jf5LTC6UK1QTIXEXwsLu8ahzbsVbKGyg8v_g0LD1ePrlCkL1k-dk69TLVVQA13cvVGbdrHI86ZjEuFPsz9FqDPjk_d_BZpUmC1Kdti7F232dHTgp2lCG_g__PWkfjlpI4qehqiwa5nrqvsvqtnhnFMkr-thqJqzkFYNhxeK-8Iw52tNh3wn6iPeuVZy54Q0DEeDFMsvHlpycJqYpmG7KHnDIODFcIy8D7ksY9IS52ExxiPILaZlH_BnAxTW_sJwDj0-KTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHfnarVCApJCFLqfOplMPpndaH1e-MRAw65kGJ2BhxbaEZkg9aXE2RLs0zNkqwmj9CCmvaAB9J2CPT3a9379wF9jW80Km-lN4Kc7t1g_UUD-MiKEVRX6PhmPp0nwxp2ea0nsaftMBDJwxH9KUmTCSqHuNgKNUTNMSsxoegOv8YPQrxgD8bEsZZrmVUOhm7tSHFspcPT4QPqFE10aQziax6EbqJ8zSVnrpSQLvsKlsqkLwl3_II0OZzpmTiINQpgcZcgOVzl8GanPlY7-alq6Iva6QQIyyg-bODDEOMfYbN5_57lPkwaxmx7eoIiaJA9HC14rDTq1I-d1K80Rs8bivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fG0yYRVoFa6aA0lBb1lRw8oGWQWAJRtUuNk8ZalxVEZhPEoqOgMUwQozL1Na-yKlZCPSptDVLyEhmHan7jU1ZImVXqeSgUKnDPiqcYzc3nb1e0WiDISjL_JdjjKtZ5eex-FCV71KSHjKpGiCWlUDzwkM78ViCrDwarEEaJFh5pWMJjbg_-Zml7bngSDpeXY-npuhYaz0KBwDA4F5aaYvvfPpaSCqWTQL4_1p0594Uw7fM_4VIAhOT3Z2YL1e3fj9NUaQ3KCQhsgnf03OI4qotSW0TKm2hR2W0a8Ioy4z8M-vHuIbgGJR--eJV3eeQFy-05vs99ePnSvfOmZHjNi4tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جو عجیب و دو دستگی بیرون از ورزشگاه
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/93416" target="_blank">📅 03:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93415">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS046LsbPT6HbVP5XzWJIUdbL-jDsCkD9FWPCCDQdBAUcGiNmX_2w4G7YqSL_8HpEK8Lf0d9Vgqo4iC927OA2sKT0krgk3BKSwCSiyCYUmylbVO2pZjrvbwmtulO4bdH_O0uhMwdIuDDJmrOR8n2cMcrXOyvsFBxKEcRgZLTxdr6z_zHq-PWoRBUCH0cNsM-fWJAYhYiIIV11uR1Ntzh2gzjAyae-df6DvTFZyNWhX1OIabBw2cTAIiWstviyveIXu_bkUQz3ulmKj5342RIwmkoKRQDhX7fUsjmn_v1Bf9YCx_dQZeUOK0_X3XsyIZIZinhBC_qXY-ScBNAOUDiZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👀
اونوریا هم کم نیاوردن و با عکس علی خامنه‌ای در خاک کشوری که رئیس جمهورش دستور ترور داد، حاضر شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/93415" target="_blank">📅 03:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93414">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hJzfTMb8D2gfM5bKinJw5Vu_CHgBl_3kPYR3vIaIUQ2YnVgbvnW7xYYKA0ikndlwnlyc6UchkY6IvP9ma-lL6C_2wX6urcLBtcXm8KhYwwKxElDsLJ2G9WokrnKDKQWp7WaCRGQV3XbLQqgZQm8A5fLDWaGZdChOGeBRrUQoFS1dOu-0_4fk9lOXzO0-vESjytlA0VpoCKlFBieGfs_GUhDSpThA6d7k1GA9RDnaUUcVh7HHH5AstdcSmc6k_Pr2SPWKcMrdVlykq4dJgKCDfACmt9_UQ-m4ncvIt1qKeoXflJ3bgJhASRDZS7wE_DwJCq6jR4CrAhOmdyi4BzVkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحث وطنه وگرنه تا الان واس بازی شاگردای قلعه نویی بیدار نمیموندم🫩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/93414" target="_blank">📅 03:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93413">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
مصاحبه ایرانیان در مقابل استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/93413" target="_blank">📅 03:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93412">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa41d0c57.mp4?token=V4eCar1sHyeW9brPyJcUAtlDpBxmMYBDs67msUWWp57Dl0FNrI7bnfqzj67hvNEUWESMxNkjFxTKJFTd5djJsikACW4cVqZeP9UAzsYuAWzstatPT1l60cSMFyq3MphjtjxMRy7cTWwVZINwc0KVKim8OxFr0sKXOT74X4aAmEqD-f8SUaJFlQYAqqlBlBb8wSzmh1HRD1auj6x6LY2ITR3ZUz7fi85IzFsJf0AqZsgNqvxXdcEAGbjsf9FDjmtkkOd_qkTunBQwsr57nICBZVRznNnTe2c5t2TiTLUwxaAHWw8IHEULqXVdhdRf0SMIBy74tNSQEP-A12YeGfhQV7Fr-ZQ89LNFgfOCgmLqPgzA1dMz-r_Xb-OdY-l7Gw7brXQ6zecQfxNwqFuVEhgmSLUIUCiFG-8ouSuQ7I6p2mTq8xDHPzTz11e2HpDDPdTUcpnPrJTHKi6j7DmR0ZGqF2QiZKOqGTvYRxEKNJsnSnELwUZ2cPG6cZTgTqhDajebTR31mBKbNT_FHB3PuMZvLHR7ocIxcxdR_RIZbLGY38zQqtIQkmfuCnjR4gP8K7rp6egI9SLsZQLJK3JJQ5gEE1iKugtyMgeeDz5L6AugARPT2MEbto3EZ2uoEMW3sjnUUevD0ylI1GxOs07bY4zNLK95KkLCJh8tcJpC2i-2o60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa41d0c57.mp4?token=V4eCar1sHyeW9brPyJcUAtlDpBxmMYBDs67msUWWp57Dl0FNrI7bnfqzj67hvNEUWESMxNkjFxTKJFTd5djJsikACW4cVqZeP9UAzsYuAWzstatPT1l60cSMFyq3MphjtjxMRy7cTWwVZINwc0KVKim8OxFr0sKXOT74X4aAmEqD-f8SUaJFlQYAqqlBlBb8wSzmh1HRD1auj6x6LY2ITR3ZUz7fi85IzFsJf0AqZsgNqvxXdcEAGbjsf9FDjmtkkOd_qkTunBQwsr57nICBZVRznNnTe2c5t2TiTLUwxaAHWw8IHEULqXVdhdRf0SMIBy74tNSQEP-A12YeGfhQV7Fr-ZQ89LNFgfOCgmLqPgzA1dMz-r_Xb-OdY-l7Gw7brXQ6zecQfxNwqFuVEhgmSLUIUCiFG-8ouSuQ7I6p2mTq8xDHPzTz11e2HpDDPdTUcpnPrJTHKi6j7DmR0ZGqF2QiZKOqGTvYRxEKNJsnSnELwUZ2cPG6cZTgTqhDajebTR31mBKbNT_FHB3PuMZvLHR7ocIxcxdR_RIZbLGY38zQqtIQkmfuCnjR4gP8K7rp6egI9SLsZQLJK3JJQ5gEE1iKugtyMgeeDz5L6AugARPT2MEbto3EZ2uoEMW3sjnUUevD0ylI1GxOs07bY4zNLK95KkLCJh8tcJpC2i-2o60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ایرانیان بیرون از ورزشگاه با در دست گرفتن پرچم شیر و خورشید و آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/93412" target="_blank">📅 03:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93411">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HndUuVZRfCAJ_26Rdv7dTdXgVC4asMXle19QtVbiHF5cXAjfsXsNlq8t0b25WIagvk6nq2aNw5NJnTFGTARNaJ6jxshMOJRB3AT83UbYSRmEx2lUayzQs9sY6aUT2Gcyf0D-zY3ZRbzX0qNGyY-J3cu02Fk_VHyctot_EGE0jPGBNwinESS0JF3uJS83DE6h3oyeM9_WiD704vJGtSx3LANMo7eRa7HuXWvWcKviEh19I_GOD5d83zoAzliay8xxAUTZRJnODgrWM1UL_8tEShhSg07JZpRyrTZo5SqscgMa3IgIqr6UZy3vG4HnnBrRmV018o2zeMdLB_c_k1XplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب‌رسمی قلعه‌نویی برای بازی نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/93411" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93410">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/889a5aef9a.mp4?token=e2t0k9tgUgELfeScDOiNP4yt8XnyHJOzXSybiQ9vOYPmQgqsO0KxZcygjCgxRbmclPH-hA_5lh4BtvktbQTxTZaJviDGLZbCLG18yXeSFJTNR0D0jVsiyAx3ZcyUQL8TKf-RParI32s3Sn2CDZO7i8Hzs7UecVx-Dw8SpAVbNZW_i7ySWCi6Bz6v5QSALXC_lYrR7UywAoy-oCor9kyblsifTb6OX1TozER9Mmvpa8_TyDrF4GAbMZG_1zIBfy6sT5nJlt00g4VvkroGkERtp0TFIgOvSimoLqpXD3aOBTFMPJ8Ol2SyYF0G24zjHK1WH_QtL2Pzw9gz97jjR-LrYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/889a5aef9a.mp4?token=e2t0k9tgUgELfeScDOiNP4yt8XnyHJOzXSybiQ9vOYPmQgqsO0KxZcygjCgxRbmclPH-hA_5lh4BtvktbQTxTZaJviDGLZbCLG18yXeSFJTNR0D0jVsiyAx3ZcyUQL8TKf-RParI32s3Sn2CDZO7i8Hzs7UecVx-Dw8SpAVbNZW_i7ySWCi6Bz6v5QSALXC_lYrR7UywAoy-oCor9kyblsifTb6OX1TozER9Mmvpa8_TyDrF4GAbMZG_1zIBfy6sT5nJlt00g4VvkroGkERtp0TFIgOvSimoLqpXD3aOBTFMPJ8Ol2SyYF0G24zjHK1WH_QtL2Pzw9gz97jjR-LrYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
بساط عشق و حال سوئدیا بعد از بردشون مقابل تونس
فقط آخرش
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/93410" target="_blank">📅 02:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93409">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5182e9afbd.mp4?token=YBvbqqUBqKX2-GAavw8TA71LUR6-pZo7_yFl6v_PovPMvz30VUu6LjlD6HFrtLFjV8OmUplbEORhRYovpJN9YVIh2EOV_wNnagRavsfwlEhdZIaOk629QZGbM7Ob0OT8gTrkVOkEqT2MZoZCv0x8E0wukGxwm8rBydYcr5Fu1EBkdr7PMhP48sqxaZNgpcjErWxpJ78fJhNdZ0sgU9z-MoC8xgF2j6aLxv1jsSciu1pu6JwrQALh7GTu53lqP9UjxfKAeZTdgQLy-GQnHecgHiXrZkcu0ej0jwOfR8XAwW_mikERstDeI5YvYn_mCSf9QOocnYg02PT3b7bIVHiECA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5182e9afbd.mp4?token=YBvbqqUBqKX2-GAavw8TA71LUR6-pZo7_yFl6v_PovPMvz30VUu6LjlD6HFrtLFjV8OmUplbEORhRYovpJN9YVIh2EOV_wNnagRavsfwlEhdZIaOk629QZGbM7Ob0OT8gTrkVOkEqT2MZoZCv0x8E0wukGxwm8rBydYcr5Fu1EBkdr7PMhP48sqxaZNgpcjErWxpJ78fJhNdZ0sgU9z-MoC8xgF2j6aLxv1jsSciu1pu6JwrQALh7GTu53lqP9UjxfKAeZTdgQLy-GQnHecgHiXrZkcu0ej0jwOfR8XAwW_mikERstDeI5YvYn_mCSf9QOocnYg02PT3b7bIVHiECA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
امشب ورزشگاه قیامتههههههههه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/93409" target="_blank">📅 02:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93408">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10adb291f.mp4?token=OKlhRoH-VJ3vdcMmkc8HqzX3qgMYsd62HqG00fZZN83AgzSim7iDQEFrSkbgorfbHmcBITrht0uwgS9rI3R-UxH0d5tExFMpMW-TNOjbpZXpND9rk3OOhzDzP2aPFmYm6OqXvxcyLjt1jSbp0fNbI7ogflTYfHiah06XP9L4fbq1Chav8w2Sx0bDDhuPqGFlFVhh5IB06t_zi56QMT9G2mnhShJh3W3JAyUcXPwxyu-8C2mnOfK4LrYtxR-lA1pxm9jqWTX-lhtSPdSDNnXIB_t7yBE0uR84ROrltCdV_rtv3V7EujlIYmQmts8svmvqnyc2cgxDwz5em05YLk_Cqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10adb291f.mp4?token=OKlhRoH-VJ3vdcMmkc8HqzX3qgMYsd62HqG00fZZN83AgzSim7iDQEFrSkbgorfbHmcBITrht0uwgS9rI3R-UxH0d5tExFMpMW-TNOjbpZXpND9rk3OOhzDzP2aPFmYm6OqXvxcyLjt1jSbp0fNbI7ogflTYfHiah06XP9L4fbq1Chav8w2Sx0bDDhuPqGFlFVhh5IB06t_zi56QMT9G2mnhShJh3W3JAyUcXPwxyu-8C2mnOfK4LrYtxR-lA1pxm9jqWTX-lhtSPdSDNnXIB_t7yBE0uR84ROrltCdV_rtv3V7EujlIYmQmts8svmvqnyc2cgxDwz5em05YLk_Cqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه اوه پشماممم
تیشرت‌هایی که بیرون از ورزشگاه بین هوادارا داره پخش میشه
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93408" target="_blank">📅 02:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93407">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d900fe663.mp4?token=WPhpTbF9E-tEmmrXAY1lms6NZHoiEzpSE3hjMVP4PBCVQGCFdNCzgCQ0BmkwDKfbqu-fQQ4ejTblzbGSadWLSFQvKQVdK1h9DRa9wkVsH1lVIFkl5YAQT7GyWWwMihIDUMBkuWUu4vfAdnNhID991wz3ct7Ob7MWIi75kM_ehY_s8ikiC6FkATuMXsYq_-L93oYwe5-xDW6k7Hirch5nfA8dLaFr0UJJ_TURk6Kmle3Hf7hzFyNVT9xTHQRVr6vYMFaz1RyfxrOYDIAxwrprV6J7gRlfoi0yb03FpYy0EokBdqsl5m3A52_BwKwHoIpS_vHmNBPjqFWyorgB1sekzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d900fe663.mp4?token=WPhpTbF9E-tEmmrXAY1lms6NZHoiEzpSE3hjMVP4PBCVQGCFdNCzgCQ0BmkwDKfbqu-fQQ4ejTblzbGSadWLSFQvKQVdK1h9DRa9wkVsH1lVIFkl5YAQT7GyWWwMihIDUMBkuWUu4vfAdnNhID991wz3ct7Ob7MWIi75kM_ehY_s8ikiC6FkATuMXsYq_-L93oYwe5-xDW6k7Hirch5nfA8dLaFr0UJJ_TURk6Kmle3Hf7hzFyNVT9xTHQRVr6vYMFaz1RyfxrOYDIAxwrprV6J7gRlfoi0yb03FpYy0EokBdqsl5m3A52_BwKwHoIpS_vHmNBPjqFWyorgB1sekzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏆
یه طیف کمی از مجاهدین خلق هم برای حضور  در استادیوم امروز حضور دارن. ماشالا فوتبال نیست که جنگ سیاسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/93407" target="_blank">📅 02:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93406">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آغاز نیمه دوم بازی عربستان و اروگوئه</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/93406" target="_blank">📅 02:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93405">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5J4EoI3VWs_vN-X5ugfc0ACs6GZyEpyO2Ws4vRLg_eTQYv3CyzdXeOau1XlRrm1AvClvj1ISRhekDOae84NhSHO10AxyXZRd-c0UsV_XT9tJksZvLaynZK050mXRWY43wKou25u7vNXZbUEdBVw9y2eO8iRm2yWF3s53TKFgnkSqUUWnnxLxe2UjgxMOPUSUiceZoWLKnGdwQgXMOIZvYW5ONXKIDpKsAjrfMw-aE9bipJ-LbFoM42FqkeW9hlW3F441JuJp2UnsUNvc4FX-_Sd-hFGckylVO-DgU_La1w4eiwAjnTlvGx3sJ2oijkKP5NM4U2rfO_QEc5Da-Kg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
#
فوریییی
از رومانو
:
🔹
تاتنهام وارد رقابت برای جذب ساندرو تونالی شد! دی زیربی می‌خواهد تونالی را به عنوان ستاره خط میانی جذب کند.
🔹
تاتنهام آماده رقابت با منچستر سیتی و آرسنال در  جذب تونالی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93405" target="_blank">📅 02:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93404">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NldnnH8UUXbQZF2I9yMJ9pL0XfRduYp3fZDdHzULKGy3E9gWzWSR7AExzeAB3wYQG22NyH-MXcoPa6BYDq4h81AayUNdbDocl_06c9LkQvGxEr9v6xazpz_ooYffMDtOXnAQPLWl_-gYlAgVqM2qE9akSqXf-XtoLY89rGG60Pndzq5kvaeqYo9izQZbhxXjvvXFTUxyx4PM5cCmbcQkuIioxXUqSBaHVOFZBXTRDrJfhyAaOt4kmJQsBWIlMPWU16fuVA_I5arRMkMwtfcFgQqBQKKYnztqXWFuEjio0qOJv81fnZsCF-oCIe-HEG_qzt6sQfX5j3_cc_c8cxjeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظرتون؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93404" target="_blank">📅 02:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93403">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8e47cdb41.mp4?token=euKmFMQqYAsGq-5yadIWJkAsBO9Gzxe8Mj4rGmed1bmgJsBTbGHJeoUp_hzejxm3RsdeQicmh-l6iCLgvDwtzOdAr1E33B72pF1qX7QGaYcsUxX0kEtzsf9K-NfyrptbTp-9eCdQsm4BPwg7COFfi0teJdr8NUvRW2XWfiK1v-kNhsayN-I0dmJzboJOgpOR8QxU7eyld47fMzYTmDgz3M4uW6JxCi_iixWrHTCT4C3gFl3A-zyQLRRmLAFQ8NBirxzjbnV1zwvLxQStBpVxoknTzZTtCGbP28KS6wUHNrkfrI1OZFV_HeL5CQlhk8p3C7AgHQy1F4LTxJ4tlDjcog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8e47cdb41.mp4?token=euKmFMQqYAsGq-5yadIWJkAsBO9Gzxe8Mj4rGmed1bmgJsBTbGHJeoUp_hzejxm3RsdeQicmh-l6iCLgvDwtzOdAr1E33B72pF1qX7QGaYcsUxX0kEtzsf9K-NfyrptbTp-9eCdQsm4BPwg7COFfi0teJdr8NUvRW2XWfiK1v-kNhsayN-I0dmJzboJOgpOR8QxU7eyld47fMzYTmDgz3M4uW6JxCi_iixWrHTCT4C3gFl3A-zyQLRRmLAFQ8NBirxzjbnV1zwvLxQStBpVxoknTzZTtCGbP28KS6wUHNrkfrI1OZFV_HeL5CQlhk8p3C7AgHQy1F4LTxJ4tlDjcog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
نرمال‌ترین هوادار عاشق قلعه‌نویی که میخواد امروز به ورزشگاه بره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93403" target="_blank">📅 02:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93402">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ee74904b5.mp4?token=sGTh9FLfVmZaeYAsKZApMiICipC2PGUK6rp7uuh4PNfHbpmGrJyz23eTKIpxgEzM47vRqkWxaL8SSHvVEmvb4gUEBNEDYaIuD2TCLZ5nUxD_vZbFGB48HL-99jQGKzSRgDWXpAdd7lUcyAS7hpfKcjC3OFGIZLHnH_ZIlQDaRGtpHDecFG2H0toXVIX-NaYQlsMx9D0h9U-ztvvk8G8scgS5WGjombNzNDhc4LccB4ffyUttKq4edBQnHGbc2mrBqsXk-JO6JKzWkOID7Y4trbfCDvqiNOhTxje56flsUW27BiZ1sFvS2KsQo4cHD4FZaEjqdvTaxuvV6adx5EBGgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ee74904b5.mp4?token=sGTh9FLfVmZaeYAsKZApMiICipC2PGUK6rp7uuh4PNfHbpmGrJyz23eTKIpxgEzM47vRqkWxaL8SSHvVEmvb4gUEBNEDYaIuD2TCLZ5nUxD_vZbFGB48HL-99jQGKzSRgDWXpAdd7lUcyAS7hpfKcjC3OFGIZLHnH_ZIlQDaRGtpHDecFG2H0toXVIX-NaYQlsMx9D0h9U-ztvvk8G8scgS5WGjombNzNDhc4LccB4ffyUttKq4edBQnHGbc2mrBqsXk-JO6JKzWkOID7Y4trbfCDvqiNOhTxje56flsUW27BiZ1sFvS2KsQo4cHD4FZaEjqdvTaxuvV6adx5EBGgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
#فووووری
؛ یکی از مفاد توافق اخیر ایران و ایالات متحده آمریکا انجام شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93402" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93401">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwfmndJVNrl0qoryQqLNw66OaTg2g_eKjrlHGfjZXcE1wuKG4k-EDCYE8mmEjQSNGZ7kxghLYsQ5hZEsFsn1FQ1CngMUYUgJttxxAfNeQX5Xn1fAvjY3Xof9tRCPgPAaGJVTn-Fu9g55SSVjRoP5ff4g-HUzqViuhhMTGnqAoH4-frBJdR37TFmiCPV4fng6FEl6jLGovtKgE3hiJPvUA_C0JANWBopNqrHmeISdeL85kq4e1qSIEPKVoPMKIkl4qt0LnC5X4xyuAULS4L_BRfp-6CxZe0zm7mVU-EPbWQ3eHSevdNv4cGcF-6R_XHcx6SvaE8LRoRy5qmwdqPSMQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدوم آدم نحسی امشب بت زده؟
بگاااا دادین تیما رو
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93401" target="_blank">📅 02:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93400">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4210e30181.mp4?token=CuT3aNPEI-300K89qb8XYib210EQysYai64wvb-CWQ1YDkNXaxb3j4ei8n2cXc0gBUtor0rt2ZyM1b09j9aCvqbuiwla_u_ZY1oaq0A-yFGJdWDzoXEUD8FdboyEtuKogd8zMApLWnJ2M4NBuNSjnj1him7e4HCMBeeeGEbmu502iejch8FSzY5X6t9MH_3-5shMlWB0lOYd1B4wWdJcNECiJ9yI1gvrjtHbzvrOs47frbVV2rDVpWuKD-iSEFDzNJQx7O-NKu-b5wkuK0I9sSIyJEChYTyGQOiz66_JCpzJmk20aGyHjqVvlL2nCyqC8Zvh4CXAv8WUwposI0TCRCSKMw3aRLnf5ElqAwPW1mYvzAML4hfGKiRvvIpKzzWEhQr-ArISd2h4ti2qehR1lrIxhIUfe9MGMHuiLGtEh9oyw5bUfOj4zcAwQ4gSYgTwo3Ri1mvPVSChbTPm4YaenR2p9XKEF15BJfR5fayEF7C4F6MY8dHShO9ldHL3cz9wDhrmf59Vlb2kayNX6vBNj6DXx7zOM4oga4S4j7VajsK2uIeGTKIF6KT5z0Filqlw-ulzmWs8nxxXJg0pXGRTPE2cK8vhYDZIPk_pApFOrzfjyWVQv28L2hGrw6L4SviwsegyL0j4-UgUxZrYimQcVE6F8fMXBnU3bT_9Mab8Rz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4210e30181.mp4?token=CuT3aNPEI-300K89qb8XYib210EQysYai64wvb-CWQ1YDkNXaxb3j4ei8n2cXc0gBUtor0rt2ZyM1b09j9aCvqbuiwla_u_ZY1oaq0A-yFGJdWDzoXEUD8FdboyEtuKogd8zMApLWnJ2M4NBuNSjnj1him7e4HCMBeeeGEbmu502iejch8FSzY5X6t9MH_3-5shMlWB0lOYd1B4wWdJcNECiJ9yI1gvrjtHbzvrOs47frbVV2rDVpWuKD-iSEFDzNJQx7O-NKu-b5wkuK0I9sSIyJEChYTyGQOiz66_JCpzJmk20aGyHjqVvlL2nCyqC8Zvh4CXAv8WUwposI0TCRCSKMw3aRLnf5ElqAwPW1mYvzAML4hfGKiRvvIpKzzWEhQr-ArISd2h4ti2qehR1lrIxhIUfe9MGMHuiLGtEh9oyw5bUfOj4zcAwQ4gSYgTwo3Ri1mvPVSChbTPm4YaenR2p9XKEF15BJfR5fayEF7C4F6MY8dHShO9ldHL3cz9wDhrmf59Vlb2kayNX6vBNj6DXx7zOM4oga4S4j7VajsK2uIeGTKIF6KT5z0Filqlw-ulzmWs8nxxXJg0pXGRTPE2cK8vhYDZIPk_pApFOrzfjyWVQv28L2hGrw6L4SviwsegyL0j4-UgUxZrYimQcVE6F8fMXBnU3bT_9Mab8Rz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
پیام ویدیویی یکی از هواداران ایرانی حاضر در محل استادیوم بازی با نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/93400" target="_blank">📅 02:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93399">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏆
پایان نیمه‌اول؛ عربستان
😃
-
😏
اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93399" target="_blank">📅 02:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93398">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08da328c5f.mp4?token=mNpSuZ5eAn9dolDpoWSdnG2Y_TTiJIfvRKevf9GmJo7XvQx-Avuy34j50qODqiHeuaJpbMaSoVTBWZY-pjHBYqpkCfYy0FaBKVkl3TWvL4sx_0cJgj1Ko7pI0NZ5u4h7qCLA5j4tXCXDWHXCwqjU0T0qlQDBBdCNzLdnv7XMdQ2s6Y4mlgwL68Cjh0y5q00zd5hTBdRqpAC3Ko04Js9W31qbdlZx7sYAlxVe1dWZogwMllhE9PoU2i48j9fGJMt9PbxVGmmQdgLIfVG-MpIx1Q2puZZyRZmghVbdQNxu5fZPGHV8tCod9S-b4mjnr3Ai-xhCnyNGgc7tYz3LnvGI_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08da328c5f.mp4?token=mNpSuZ5eAn9dolDpoWSdnG2Y_TTiJIfvRKevf9GmJo7XvQx-Avuy34j50qODqiHeuaJpbMaSoVTBWZY-pjHBYqpkCfYy0FaBKVkl3TWvL4sx_0cJgj1Ko7pI0NZ5u4h7qCLA5j4tXCXDWHXCwqjU0T0qlQDBBdCNzLdnv7XMdQ2s6Y4mlgwL68Cjh0y5q00zd5hTBdRqpAC3Ko04Js9W31qbdlZx7sYAlxVe1dWZogwMllhE9PoU2i48j9fGJMt9PbxVGmmQdgLIfVG-MpIx1Q2puZZyRZmghVbdQNxu5fZPGHV8tCod9S-b4mjnr3Ai-xhCnyNGgc7tYz3LnvGI_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇸🇦
گل‌اول عربستان به اروگوئه توسط الامری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93398" target="_blank">📅 02:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93397">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AswQNCzSi8iCvrz17E9xCKRo6gTz0QdSpIc5OxpedfBYmarQ8Tjfv4RQZvvKmJrCh2lQe7IcMQw9l4_qvi6VkVpbHh7sswqVJ5rkHzKWqH2aBSGEggNO1gGVkqQ2i8jqnU5kSAhVJ6qQDDoBjfTaZgdiheX1PoZVo-9RcqjtoCfigLQzsTQuNE16-nG6QWqNlqTwmnXjbdKfhnjFAKCfEqYfPcDj8-B94L4cLIjqDgpxRQEK_Qh4LS1JB7SdpF_DQwa2VR3vosvWZ0GzM2J_mhRZ-f1OiDCV9pqHg9q8Ye36vF8qJ1_2G45l3Iggtu3mEg8dBezBCm6aELUCwRRePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونایی که جام جهانی ۲۰۱۰ بازیای اروگوئه رو میدیدن یادشونه فورلان تو نسخه پرایمش یه تنه کون همه تیما گذاشته بود، آخرم جایزه بهترین بازیکن اون جام جهانی رو گرفت
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93397" target="_blank">📅 02:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93396">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آقای قلعه‌نویی امشب برینی علاوه بر ایران یه آسیا سوژه خنده دارن
😐</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93396" target="_blank">📅 02:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93395">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پشماممممممم</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93395" target="_blank">📅 02:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93394">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حقشون بود واقعا
ترکوندن چند دقیقست</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93394" target="_blank">📅 02:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93393">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عربستانننننننن
😐
😐
😐</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93393" target="_blank">📅 02:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93392">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گلگلگلللگل</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93392" target="_blank">📅 02:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93391">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پشمام عربستان گل زددد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93391" target="_blank">📅 02:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93390">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9RXatcX4okzA_YRzJUo-buu7DaVYhuSFJ4OS_r4guzNdkCQdtM03bMzJJNe0lrLPS-J6IOPKxu6R5Ha9_BdhVBhNmSZKk4g483asjg6i_6S6K7WKf9xHaFC9zvFhu3hUGAb6E27PfZydIIaw7Ty0JPXyu0r-gpZxXalUktEufp_E5cv83kDcdDqRU81ZOTKsHRQG8lO1iT2jddCBLkP78rxwwvkb5kaQcNJsPs5o3uZK7TWxoLh_4RtIg82-6X1vsbbypKBDn7wWyf0q7QHmtPUMVKLZF3x-L7Cd1ExtCeRnqavqUCXeRFmPwKcR9nke3Lj2hIunnosJg1tKunHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🏆
زید آقای لامین‌یامال که در استادیوم امشب حضور داشته و شاهد ریدمان دوس‌پسرش بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/93390" target="_blank">📅 02:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93389">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC_Z_Kg1XHBpvBqx6Cpfoj7GtTpJJRZR-08fqc2v0hjpSs9Sz5MoZFLEKUc6_3Z1X0-3Wa_hDTjRqjTt8AQ7_7F9IlCGidEj6ZD8C2A_ZdurdVUqZiDv8fzbEOSfxo66wI_YvxHDtO826-HLV_NyKMR2uPbawzMvL6J8LK1h3_519egquTS-50W8cGRlY8NMrQLfhsqZYlmfviOHZRApVQzwwnoe3jGDTbMv2LL6sxpkEbFPAPcEYVsjFF59MiwzItJo9eR3OCGJQDOMPZfufAfb5AfJWgQCmZvc0ytQqfHzgjeI0v8yp92S1ADuDPf6TeTOQhHfnj5-lTF72oozLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجریای شبکه DAZN در جام جهانی هستن
💗
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93389" target="_blank">📅 02:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93388">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تیم‌های آسیایی عجیب امسال سگ شدن. به راحتی وا نمیدن. عربستان هم حسابی اروگوئه رو فعلا تو دردسر انداخته</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93388" target="_blank">📅 02:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93387">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8e3f17e9.mp4?token=kd3QF0IPbCuPex51XKddQylMAq-McI3MQKaJL1-GjQJbqEVZ2Dz--d-fmYa8-arZkREOnB2SeCCzdQTOalQw87aOb-IbPCibCyUg5vshZw3Ec1qromcknTiwFJ-wiCmIRleW_zEQgBC0eoq_gkOHN9Am--mCHmM9RSZio91-c1sup2PSSlVIVkC1_2vqSQxejdblBDGAQXwDJDFXoKE8KsaNyNQTxci0P1aZVLlrwfhxuYnfMHgH4ols9z079_a-jZGq3oVfKLT5DaJwDA4PdfG_FXk47iWSMMitquNnhZEWplfRLy2fNmXCcrIRu6RrFr5UwG_Vs6-VRqGAdg9Rig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8e3f17e9.mp4?token=kd3QF0IPbCuPex51XKddQylMAq-McI3MQKaJL1-GjQJbqEVZ2Dz--d-fmYa8-arZkREOnB2SeCCzdQTOalQw87aOb-IbPCibCyUg5vshZw3Ec1qromcknTiwFJ-wiCmIRleW_zEQgBC0eoq_gkOHN9Am--mCHmM9RSZio91-c1sup2PSSlVIVkC1_2vqSQxejdblBDGAQXwDJDFXoKE8KsaNyNQTxci0P1aZVLlrwfhxuYnfMHgH4ols9z079_a-jZGq3oVfKLT5DaJwDA4PdfG_FXk47iWSMMitquNnhZEWplfRLy2fNmXCcrIRu6RrFr5UwG_Vs6-VRqGAdg9Rig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
شعارهای مخالفان جمهوری اسلامی در اطراف استادیوم محل برگزاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93387" target="_blank">📅 02:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93386">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/986e63cda4.mp4?token=jZrOuzBM9Q8GMivAUi07UjETHwGampI7z6uaSiwKOcjYkQ05PivKJF5xzzfuVlgTWNmTwqxjyHFIQdIORXVEfUWos3FZo9DmIRI9ZPU019g3tcTencP8wlm0b_AMTDvOun1ahD8KgTMi3J3lSPEPcKSOUujEmXjXkskUqBY0vofuWF3GQ9Mhed8eLejkjljFx7IXCIHmn-mARUqcQNkjNzufoVlL-fgspj1mJq6Jl5YTh4OEHf5DAc9uyBJQOsT-dkuyMDwaMuHrUysW3JYS0qAFZ5rxVbrMAbG8BMj7JJhXBI7si81aQK3mHCo9BPTZJCw3z7cBVYUIaqUrLj6hjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/986e63cda4.mp4?token=jZrOuzBM9Q8GMivAUi07UjETHwGampI7z6uaSiwKOcjYkQ05PivKJF5xzzfuVlgTWNmTwqxjyHFIQdIORXVEfUWos3FZo9DmIRI9ZPU019g3tcTencP8wlm0b_AMTDvOun1ahD8KgTMi3J3lSPEPcKSOUujEmXjXkskUqBY0vofuWF3GQ9Mhed8eLejkjljFx7IXCIHmn-mARUqcQNkjNzufoVlL-fgspj1mJq6Jl5YTh4OEHf5DAc9uyBJQOsT-dkuyMDwaMuHrUysW3JYS0qAFZ5rxVbrMAbG8BMj7JJhXBI7si81aQK3mHCo9BPTZJCw3z7cBVYUIaqUrLj6hjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
طرفداران تیم‌ملی در اطراف استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93386" target="_blank">📅 02:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93385">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/092eca3636.mp4?token=l8HNw082r1fEzm3kCunYHkX6XjYvruBr42AckavQzXTJJrkMoTBA5KzNFxUq231YCXQq7BqBE2dAyxivi1K5k4JemhmC2GHoZZVRmfNBB-VlnfarR1FPrVNj926xlmEmCJH_Hn9OoAyAGj00e-Yw0lYjRnCZ2oGSK-ZfPiIHCD_JaKMkJllDi6U2q6WTCWF7zS4SKD10ekI6l09NuvLaQM8W_19eQq_6EKh9Wp3WyEZ1vVgzEkOtSt65vnHsBRdG2JInRrdGjC-uYm1T4HQKDkZrHFM_rg0ssa61rNJAPqO1wqcxdkKKq7URA85oykTmanLj-bzAcAaefffHRKQW1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/092eca3636.mp4?token=l8HNw082r1fEzm3kCunYHkX6XjYvruBr42AckavQzXTJJrkMoTBA5KzNFxUq231YCXQq7BqBE2dAyxivi1K5k4JemhmC2GHoZZVRmfNBB-VlnfarR1FPrVNj926xlmEmCJH_Hn9OoAyAGj00e-Yw0lYjRnCZ2oGSK-ZfPiIHCD_JaKMkJllDi6U2q6WTCWF7zS4SKD10ekI6l09NuvLaQM8W_19eQq_6EKh9Wp3WyEZ1vVgzEkOtSt65vnHsBRdG2JInRrdGjC-uYm1T4HQKDkZrHFM_rg0ssa61rNJAPqO1wqcxdkKKq7URA85oykTmanLj-bzAcAaefffHRKQW1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
پیام ویدیویی ترامپ در آستانه بازی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/93385" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93383">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MUji3b7r5b9b9sMXc5Mz86tn0sgDGU4Wr45VKN24cU5Wtmkesnpm84dbGGwaYgoEiKjKQinBkMDmFf-AYDLouQi7FqN_8XpbpwqypwfgZldhrVHq6_Uv8lVW7pEC8E1E4yrQ8owfWm9srhhmu58YsD6QVQkPNVM-854qw9cKIMnVk7kBxENgc7X-Yl9icgeKpyXCE6Zqf8qJ2GPshrK52yo0hCoseVk31_aq09qblTc8x5fmz4YfvkGe2_1jrqjIs8lt3cCd3AkaMDAEjaqQXqJWsJaPFgTR6dxO6psbPzJrkQc-tnx2nAWDfQG_7D7D9GLWf7FkFzvu9mD-TAf-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dej2x3t_LbTq_CcKakBQc6PEa5bD60anLrToD5xrGHw3fIWaHowi9KkL1FzYDRf0wNzbN5ieB1YWXujJD9g-aNX395hWH5Ixp3RL7xGKBsPXMQaB5VgKXjbL3A6smnrp9DM0luG2WnkOf2TKvm4tHyaIKUi5yO4PLsxpaei-UAHzEPsAwJtHpphGdBYjYq9W4VfJ8b0bfh2PaFAqWyna-tYNZ9kfscANBxnqNknI9xLcaAfckVD2yzS-fnKQVVXqZRoo8DgtfTbiez-V0CcjSlI__U-6qrUpjYZflpCYf1SAZ1_VJJH37KKA42AOBdkxpcnaZKTGGmIsN07_BBsTsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔙
درست مثل روزهای قدیم
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/93383" target="_blank">📅 01:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93382">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بازی فرداشب فرانسه و سنگال رو عادل فردوسی‌پور قراره گزارش کنه</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/93382" target="_blank">📅 01:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93380">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کم کم بریممممممم سراغ نبرد اروگوئه و عربستان</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/93380" target="_blank">📅 01:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93379">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCnk6WmH13yH-hIHX1X0RMuk7Ydxsi6nfpqYlamKT49Qvm8uBYx0b3mQ7QIdXY96cMreBvhx6CmHAT9Z0bVa7VKYvvCbMnz369dN2gds7fMsAWtMjWcebB7IGrpkVwLcvqTGnRCqMvpuTTEKk7UZ11UJzYwAHdCp1026_ZqQAOd-lLVqkkanOtD2ux3NsGqwrGnQkqdNErCQAK2vhay0p3bJwgcqlWCN4fLIVKyJNgEsb2WOWCpA4cr0EEzN1fvt409yCfMHnavT534wIeWWTXMwUwcW4MkZ1yR92Kx0i5uNRW8ozJV0VgNP4HyFFqPPytneRVV-qQQEnJq8ZTBjzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
رونالدو حسابی بدنو ساخته برا دشت جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93379" target="_blank">📅 01:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93377">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEsecEBeITIR6DzmKj88ZXeF0sRpurzUf0dtugCY-r-XHyZy_qOmM9cEiRGPEWxf0uwzaS9k9wjbvIaLB_Bh0Wkeen5Fxvw2EJh_e1mgk858gAIO_fJ-d7U7Qob2R_9_lgxrrqytPm0cY9yP3MiegDLajoFtR1tK-qH3Kfz9kO5hzVeaOEgf8VZJGVfar9Xt2Er0NteH7Gt6VqlVf9f9otUL4xVa6WdttVJ9MVfputej9jKmFV8j03PyWwuf3D_bWOZyEx-MPKFh8wU-FGkjjdC2CD_O_V84yqxrSBnDXGy76deQdAOLll10uxj5AFZx73HbwElOxwL1kExKcVdGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLJ_oo8upVlnMD1yrZ6cTsi_8ow8aQzFERzvpd1YmY-uuKWxFlQh1BszuE3jLz2SC6eGTDR7OgR27DX2i-jEG3jdXVSEM74gA4kIgLDZoXNSDRbrmtJpmmaC-CtfIrgi2Efi1UZjfr9xWTUmguZ87tLiTPTKLIHEOeaaOePaojnRFPCU9CXgC-BX37NLSnZq0cS0lM7gLHlM7VnthvSyfWmarL21mS9HeRB_U-lnQGs2UVS3s5teNVzdozCzqtVQLT-9Bb7hzjKuVqcobsI_TEBxR0IrsE3s7yH2P7WCfUdMY-aKSWpboHR8u-3sYCIYZjLLiQdEuwaHTCylclbQhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسپانیا بر خلاف بازیاش بیرون از زمین حسابی ترکونده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/93377" target="_blank">📅 01:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93376">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lgfj-9x2_RDEnTFm8rxElEBM7bcZ3oTMBHrfeT6W4cy0hGVMvEzKGd-UeYFL0OH92aPy4SN05p83Lt3z2b0AUX9CAIm8vzkG97LkhwnfAy8foVdcp-0ig51Fnh8rHRaxRISmPd7Y1ng1l4klVUcJ17RNj4cvxEMMjiUBd61U5blDUU-OiSi7xfi2JMjfyZ5AnHCIhcxRtMHmfgfe-P2ESg4M6B6RTWKHwJGUL0PeG83IGzMuW8-hrtdtLQccT82vCLZaEhZBQaTKCxPIdnUfdTMpPEF-Y25736cXJQliqRdxd-nzN-zviVt4-BdZbVhsenMAwIYbQsl8uD1jDzUp1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
بنر یکی از هواداران اسپانیا: پدری بیا با مادر زنم بخواب ولی کیت‌ خودتو بهم بده
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/93376" target="_blank">📅 00:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93375">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhOlCQyu32vdClAljFX3ZoYVuAq_kpXDvROS-BUCedN0vl44hdYH9ucTLj9ytNrvwGi8C8VOOWlGvRCoQr0mBcDm6L-4QWUMvPh7EG-A4OI8aHm3VIUgZnnCjvCfJnEfDEhOQ_gARgsUEdDORfh4MDCP1a3mIiO0TRYg1oCiQIWjlaAF3OQGSP9qhYvwJTnmpL7qpwWbjgAHEmORiVskO2qz7wHqHw5XtwlooIMv-a2-n4adk5LK5kqjJ3LkO7BfOeHV1EAetUwmenZvVFClQYnzszpsCF9LzKONH1cUXxKIndb3j6HDwM2hOp8Y7DuhuPljdSlvLQAsXxLbNh4T_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
تیم‌های اروپایی در ۱۰ بازی در جام جهانی ۲۰۲۶ تا کنون:
✅
• [۳] پیروزی.
🤝
•
[۵] تساوی‌
❌
• [۲] شکست‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/93375" target="_blank">📅 00:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93374">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVWECt0M4XN3-Nn3K08jxqRZvzLJgeBVAfCXFJFBSdrUbwKDP7Ko9NPlVy91-jAD0ZLxSL6qYkrmzMc87SP5wHGzzVdEPjkQ4kjYL3nwX6XiG-ZXdMdPfIvjh21rakZfMJndLunY39hvAZ1AKg_VnWGKTyzzqghmKsUBpJuP3dux4EIqtezBcBzD0qvgSxylP--BXuEsIfnP5WBvUQP0700HZmcCiT0xOj_GILBpFe5RvDhdohVdNeT7PTaP066QxSFa2dHkUTqZaLA5p6IffEPPHl6YayzweBaDE90MpxxIzEp2Pc6uSZt_VZTNoHvdJV6GXeY_4PiCEONmcoAxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
تیم‌های آفریقایی پس از ۶ بازی اول خود در جام جهانی ۲۰۲۶، ۶ امتیاز کسب کردن.
🔥
🌍
◀️
‏
این بهترین شروع اونا در یک دوره از مسابقات از سال ۲۰۰۲ است (که در اون هم پس از ۶ بازی اول، ۶ امتیاز کسب کرده بودند).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/93374" target="_blank">📅 00:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93373">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/93373" target="_blank">📅 00:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93372">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromProxy MTProto | پروکسی(|•𝓗𝓸𝓼𝓼𝓮𝓲𝓷🥀•|)</strong></div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/93372" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93371">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtRiKRn5V_SOVex1XktKvJxwZtOQmvP-e0N-Ts1yPiFt5oo6cyXyHMktIQT_gbigm11A5Ec26rBKD6iAY9oiLghVPkg4FrCquRpfOmuq2PHOOVbZeVDgjnaIXnFv5G2LscLoWLLGvFj_UGg_imrkrQlImDceTimZDPb4LeCHwDwot1UnK3FhMkY2B-VmGIww08Cdm-fOIpzG97MclogT5zCvBH5aldldUeJDNgQngzeidbJ-K2F7G9OjAGeeAPVVhVNHzsU4M7hlxczcAqHdyl4BN0XLch9agH4PdjruxaRDtMERfymEMa6YmZ3DeilFeksiZd19qeqSxoK8_ROxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببینید امشب تصویربردارا چی شکار کردن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93371" target="_blank">📅 00:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93370">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYT3ENSS5qETKDQBV7Htv7ykWwU3qbLriHD3rYBFgKPa6MeDRpUvFMpBJHaT3xl9iekVbLg2NCctYUIzfS1ip0UejpvHIytsOKagKij8hSp84ER_Z9EIi34QnznuccY_sSQF8oyhv0UZZjuWnVSxSR-nkjSkwq3J6xPe70SQ38lTrtYfqiNYATd6uTIYjagSf3Ku_Y-McVnoriELE2rdLq5Oa4EwDTPE8CVpbmC7Gzn45eMBSQBqQIVEsj-G1K-frZC4kQnIUEWGV8ZfPIDkHni7B3k5KFCIZCVgoh-etpg1Cv2C7x6G24wiXJ4WfPvlsxPZx1ZNE0eeFJZ-5P5MtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
تیم ملی مصر برای اولین بار از جام جهانی ۱۹۹۰، در جام جهانی امتیاز کسب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/93370" target="_blank">📅 00:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93368">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivUkShdmYBz6JEkRzAgRnzAepgBlQtm5WF9BhRzlskkECmFN5J50GVM9vnA0WXVOECGTdpgf_0THV0ic8bDP5peBRuE3IDS1oNAOdle8gX8miFdl-XWorWmkGOqIUe0x9twT1bws4WQMICFwynXWQOus00-2E0FVBv6Wrk6wwvbcmaqGfQaD6VfKuvaGrBIueIkKKdh-gHK2Xi_uQe4AKb-qj3polBZWHCvT1dAlVD7E76aqeznzoN1kF0gna4D8NzVPls5TVXaZqXHbkhHVxH38CR8GFpF9jTl8ChCPYYI8wwhPVGaDXXGJYPcqEs4Uqjqkldpf17Id3q4qd3bqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم برای دلت مَرد، ضربه ای که تو با شرط بستن روی اسپانیا خوردی هیچکس نخورد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/93368" target="_blank">📅 00:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93367">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY2i9_iKML8d-KtZDdQlnxuh_64DgdO4X9jzO26fR1Y1r5oLBHueJvQiS2dljZGrvCLpp36LDoH1uu5BOJQnpI_9VTxptLGQFSm5uK7JF-q3YxrqgQ4E41EST9G1UDNBFSALjFNzKEY2z0RI3WzBRy4y1SHc5iPRtpJf-cV9rgKVbTh6r8zO1OyLRdYnvRoMNW55-u6Pt2gfnmg_Z5iVPmIaeUJf8r5PF4HyF2i8a1ZArVRoRhEjRHQXJOEACX763MUZRl9WlSmnsZB4zfSfnTDvwRCui9TJihcSshIihHa9XE-re0yPP-AK8d-HGuMLeTwTAge5CuQcincRSmQdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امام عاشور به عنوان بهترین بازیکن دیدار بلژیک و مصر انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93367" target="_blank">📅 00:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93366">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNvUO0jvAfg2rRi-WZ_NpWMwY9AnIgeitIRJ0qLQl1O9d9tGhzvvoOgpkKzdRH_0mqYzeq8e4KbvJxRf6Jpsj0pQ98NncLL-hp9CWDWiNkkjn7-BM5k6x4klDjeB-aAvxrV9GRljEXIfnGRI4PS-OFYfx618yL6g6axE5VCeuYsQuXNCvxf6M_5Y6qGt3sX2wpQw74H17bGDWjiCFVQhlILDFIfY4OR0OM_aC6TeXC1KMBYNi5OjV1Vxhwnn3IHYDGFk2lSOHerFZ2B1nM_BnlSoy4LMxIJW7Omt-zk9aeI-p4np92Zry1BypbIMHoIqY9dSE9jNbOsa77rgLGJYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
🇪🇬
🇧🇪
آمار بازی امشب دو تیم بلژیک و مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/93366" target="_blank">📅 00:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93365">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYJEipZZUArWxpbslsL4yV6T5aH7oF4sfS1RgIuJlCOf8nAwsOvO2JwhfXXHTBG9GsydkthYmHoqIOy2VjpFUa2TvPJpQDXtZqF71rCqJX8RZXdhK7Gvmq8awXOCDM6Neg8h-TfcdgdF9Era2PCVfaMK-bPlyuvIpgm5gxFxcM3iT7PkR1xV5YMfeEHP0AU4mbmbF2rn1zbmi6WbSiXH3L9BOwxvns5Lf5JC2y5oZua9KAo_sBzCZy2HqsrSHFbzEE-B7m1TaUXeXB_u0zUSplX2wmEaR-gRyD7ZLvNvFsabFIG0aYJ_XFTbc6rdVVZdhl957EXjKZOr6s-FUME7lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
پایان بازی | حریفان ایران به یک امتیاز بسنده کردند
🇧🇪
بلژیک 1 -
🇪🇬
مصر 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/93365" target="_blank">📅 00:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93364">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ch-w7U9F3IpTUDcNPoZAK0ZZ1qqOrPt3gotFBE8HVBFqFz9OBsVQCQixHGWJ-Yb0VldzK245SytmQel_lJZM2hO3VSqrwQWnPzyui-ItcKQnUqHLa5tdV5B-BR6jXE6G-SlGUzqE0VAbD0ES0gEtE3zQT3DrIdK84kVGDx6gy82lwmhmWocA2OeBLqlgd06HkQe7l9ubpIL3DK8Pmb_ZhNqKqLjhP0v84xRzVe4KIwyGchdv8lErTw8icve0UyN1cHO-bqByXL9lOQvEW_73TgiCUD_hgy-bI0CV-GNb3z_8Fb9Z3U8v73YmwqBqjGsiGHpK9rdCmI4aLEWWqmYzww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
تعداد تماشاگران بازی بلژیک و مصر اعلام شد : 66775
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/93364" target="_blank">📅 00:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93363">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">واااااااای چیووووو دراورد گلررر مصر</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/93363" target="_blank">📅 00:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93362">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گلللللللللل بلژییییییک لوکاکو</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/93362" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93361">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a05a2beef1.mp4?token=QNi41FKduY8KYmywtIJsv4ZqibOw1j11O0r19tzLbe9NV3fu-xmL8CHkc-cEKKYd9CGP9yH_7wwnimDVL7YHgATY33hcSpjjyerv5szC_UXp1mUpccB5Py2aF0x7HPd_k3HVYvV3dCY27p4CZMNSVqW3fdYal-SyilHJCTl0a_nYW4P2GRSnoEBDSkVCfisza554Zkbr7lkBbk5WGQdn_h5sKwzmnvJWRgRE2nIuduUT88S41OeIBJWC6Hl2CoymA3ZiRHIrms7phO8fUjI5nb8URHFCKOMfHQRHhamnBeTpjh-V7KS3tRAo6-saOCvxEHob0llNOmVW1kUC4QVKpgZms_jm25eBKzHSbMQ-aYOWfGBFJ4LcbtGH-ncPHfneQcDEGt7VdJi8tJRXTGDS_XNhpBZxtsypkjrkVQ3tznBvxqpgAXzn2PSwv6aYjaeYPxPcLHX3WE72nQOf22PXXfxj_1ddsDf9fJvxXsnkt0DgIVJuX7B-hTFrCPkrsVkjmhYZdItqs4ifcRPLjUREvUkr_9cchnNNCK1-8xFpN1OlwbVuJgoQwF6BueQsxyIZH-1gR7S2FFUvmFiHwF8jx3B7GecNr_pV8QCeX4cVJnTjCBKvigQIIWWJfYTfNSWh2k7nZGkTaJTdSvKWPLZ8-SppSxgO18uBAkNXrRwxlNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a05a2beef1.mp4?token=QNi41FKduY8KYmywtIJsv4ZqibOw1j11O0r19tzLbe9NV3fu-xmL8CHkc-cEKKYd9CGP9yH_7wwnimDVL7YHgATY33hcSpjjyerv5szC_UXp1mUpccB5Py2aF0x7HPd_k3HVYvV3dCY27p4CZMNSVqW3fdYal-SyilHJCTl0a_nYW4P2GRSnoEBDSkVCfisza554Zkbr7lkBbk5WGQdn_h5sKwzmnvJWRgRE2nIuduUT88S41OeIBJWC6Hl2CoymA3ZiRHIrms7phO8fUjI5nb8URHFCKOMfHQRHhamnBeTpjh-V7KS3tRAo6-saOCvxEHob0llNOmVW1kUC4QVKpgZms_jm25eBKzHSbMQ-aYOWfGBFJ4LcbtGH-ncPHfneQcDEGt7VdJi8tJRXTGDS_XNhpBZxtsypkjrkVQ3tznBvxqpgAXzn2PSwv6aYjaeYPxPcLHX3WE72nQOf22PXXfxj_1ddsDf9fJvxXsnkt0DgIVJuX7B-hTFrCPkrsVkjmhYZdItqs4ifcRPLjUREvUkr_9cchnNNCK1-8xFpN1OlwbVuJgoQwF6BueQsxyIZH-1gR7S2FFUvmFiHwF8jx3B7GecNr_pV8QCeX4cVJnTjCBKvigQIIWWJfYTfNSWh2k7nZGkTaJTdSvKWPLZ8-SppSxgO18uBAkNXrRwxlNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل اول بلژیک به مصر توسط هانی ( گل بخودی )
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/93361" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93360">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گلللللللللل بلژییییییک لوکاکو</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/93360" target="_blank">📅 23:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93359">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIXD71rRyfqWL-gfIUPLxd_x046xQuwmoK6ZUoy8qSoC2xsJFKpGjdQ1NzFmDujv9UVaOvBSd6T1hQsP_gfVasmeNKsKNSabb_sGbW7uqacKKsbfBBadGUu1Lj4E1IMnb9Jf3CLTBx_1g6X9ka8F7A3ZEhPCZ5OBYyKgZfqCfcS6e1CT3B15k1wXvMDx52g7MRrj9Ss2XN-mFdv9fPSpb2qaRtnacoFtmOb0SJOqi9k6RME68XSMgl-nOXOpKcJ9H1c_PJa_7IH04Pkd80zPwlubRRPUe7k1j6csfnjhmsh7HgBJFUXfk1Asf2_Hd93DCum0Wrc4tJKyPhFEAPzO4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇸🇦
ترکیب عربستان مقابل اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93359" target="_blank">📅 23:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93358">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وای مصر نزدیک بود دومی بزنه</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93358" target="_blank">📅 23:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93357">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">لوکاکو داره میاد تا کارو واسه بلژیک در بیاره</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/93357" target="_blank">📅 23:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93356">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مرموش هم توپو زد به کص گاو</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93356" target="_blank">📅 23:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93355">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smUlmQQyz_pxWUiJzSGqwx8wqbD28KrLSLYPUunfN4HhhSTyoc05kcACbXER8LXPSBZjSQpS2wsN5PYAK6dkBIWH-T2PFeVJRpgEQS5axCM1gd3kICnUnqbL5LRafyM0w94Z1g9YovxYxPJa2pjvN2srCaJ0b3xPUs9DdOU6P-9NpLiAo9DJXme5QI6r4SYNvtafcPLAb4wNh09wqKRUlh5yqjAau_kiALLsLUHLdYlv-xI0L0ZfepwRBLMeycLLBzjTwni8odUzkMMROIE-btuOws5zyQQoFkuhrn8--EvZXfBsv-oaqmX7I_8dMv1DYhpwVYDkpQioZ5XesvZfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکن مصر این توپو به اوت زد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/93355" target="_blank">📅 23:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93354">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs_ajTOVslEOwxr-_AvpwZnA-i5zf8pe2ritM9ydYIFOvaQ_TsqTj7VhQ3UUcBR9hWGjJmTLQO6Ht04BXeoyL53wLKchXvxmkPp6TNvauBPd95RQ1CuEiWMLCwlvK_N6jC1ppZXZ9Ey5fhCUe6LqoD1UY_AMaM-ihVjxJrd7KiCloW43Yg5qkpXI_LHOf-xB8vd01ad70-JVsQJ0TTw8-HxafdSaYTnc5KsA2GCQHIuyTswFIMpKhvCXDW27efe6UZHC4ILiG2-fOf_ISjQxfirdJRkdX5nAPMbyoqsFvQQ7-d5oPE4OXyqeyrjL4cMlbi-WxE_RFhtYomOEvB-j7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
لامین‌یامال: به هواداران اسپانیا قول می‌دهم به آن‌چیزی که در ذهنشان است با قاطعیت دست پیدا خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/93354" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93353">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پشمام مصر چجوری این توپو گل نکرد
😐</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/93353" target="_blank">📅 23:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93352">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e1c9a760.mp4?token=BZs5uOOGaeLurEoUolAEAAcMRIiebmdzL8oFAuiVBWowRGGhd3AbbpUD0zk4JW-AeVBhgpBXVgnmuIBtEq0o4eTpY60l1_7bZQZ47ScR9VwPsku45O8JDls-PAxOyJ3WkKPZgYB2phFiF7MpFIYmujJe05DKfaFua455pqcpckcfO6D9s0IFGOPz-DSWJ_kB7tMc5GxTlU_ChqdhmTnqWBn3ZXKZCSrREyHm8LcLkavdfKe2aHIM6kM-q6hwK-q16IPOpnIQHPjM5_kkOfVqlcMuIKm2uYjynpfglypC9udiHXfGgxn6XqhAX_hoGHbU5ncS1xFxm0NrVp04mEmETw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e1c9a760.mp4?token=BZs5uOOGaeLurEoUolAEAAcMRIiebmdzL8oFAuiVBWowRGGhd3AbbpUD0zk4JW-AeVBhgpBXVgnmuIBtEq0o4eTpY60l1_7bZQZ47ScR9VwPsku45O8JDls-PAxOyJ3WkKPZgYB2phFiF7MpFIYmujJe05DKfaFua455pqcpckcfO6D9s0IFGOPz-DSWJ_kB7tMc5GxTlU_ChqdhmTnqWBn3ZXKZCSrREyHm8LcLkavdfKe2aHIM6kM-q6hwK-q16IPOpnIQHPjM5_kkOfVqlcMuIKm2uYjynpfglypC9udiHXfGgxn6XqhAX_hoGHbU5ncS1xFxm0NrVp04mEmETw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دروازه بان کیپ ورد بعد بازی وقتی میبینه فالوورهاش 2 میلیون شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/93352" target="_blank">📅 23:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93351">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇪🇸
#فووووووری
؛ فدراسیون فوتبال ایران با پرداخت مبلغی به فدراسیون اسپانیا خواستار حضور هواداران این کشور با پرچم رسمی ایران در بازی امشب شده است تا در مقابل ایرانیان با پرچم شیر و خورشید قرار بگیرند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/93351" target="_blank">📅 23:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93350">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fabd41212.mp4?token=ZdRhXeZieFbk4OHjJ8WLSrHsemvhP5f7YQ8YzYzz671dP9Y_yN6MgGT0WX4mPBt8POb44cGfDrXwvnUi3UcPbvghm0m9XsatNgZp2HDxaesF3Sxtxt1TmFG148klRzbBe_KBhQk-Rwir_pyIwJhQv3-i351nv-2115NEM-z_h_70xNxwUcr73Fj8ejBJNXRUizoGj-YsOxGYQlsySrbweV2hEceyILKE8JsOd9CdMU_tfEU9Sb92ZfW_j9reMcx8trZSMeLkvHgmNpeGxriFH_GKQOOD4LisvEK4nV5AiOkKEgcbh-LHL3DNpLxnLgp1upH78ecnbt743-iZEwc0mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fabd41212.mp4?token=ZdRhXeZieFbk4OHjJ8WLSrHsemvhP5f7YQ8YzYzz671dP9Y_yN6MgGT0WX4mPBt8POb44cGfDrXwvnUi3UcPbvghm0m9XsatNgZp2HDxaesF3Sxtxt1TmFG148klRzbBe_KBhQk-Rwir_pyIwJhQv3-i351nv-2115NEM-z_h_70xNxwUcr73Fj8ejBJNXRUizoGj-YsOxGYQlsySrbweV2hEceyILKE8JsOd9CdMU_tfEU9Sb92ZfW_j9reMcx8trZSMeLkvHgmNpeGxriFH_GKQOOD4LisvEK4nV5AiOkKEgcbh-LHL3DNpLxnLgp1upH78ecnbt743-iZEwc0mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
من بعد اینکه 10 فوتبال رو توی 4 روز دیدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/93350" target="_blank">📅 23:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93349">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !  هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/93349" target="_blank">📅 23:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93348">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddjn_pP2ONHvmtPa6DxHVYD0IRP7YUnia9GbWlWlzkRzp3Pq0__wkJppQxE3k4HuHQHBUke-7fvsw9E3VqsvGoOyS5oJxxkhDyD6Yi0aJPy8QvhZXjyGPMM4RYO2kxs6CCKJS7ojVFzB7MB29Ovk0hAlxPEd2AFpaA9YaISnp99MpPWFhHQbjByBdlIGG3QFfU9TXH2eHckAJDbaQTkOhh6AUB9cjbjXpquJ8U3PqbaOmTWaKbEadjemGodLKM-nXYuPlAyhsf40VjMyTJUhqjJ5f_njRhjwOorzPiq-CC7vLj-6aqxBMBUuVwBLVeqv0vWyXbXtEFybh30Zrmc8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !
هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/93348" target="_blank">📅 23:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93347">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شروع نیمه دوم</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/93347" target="_blank">📅 23:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93346">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhnRuhLSl6f-MTseUKmKc_9wHczmTaQvKAGO9NC396KBSMAXVq9TkLAGhswXJNJIKoI9RGDO0U87HsLuhkzgUGWJ7tBtHYhXaD0WCrc6LFrP8XwHlSQ6oKww348dSe9DWxwr7JNPLOSOWSwvNI1i1O6bQmYZ10eSNhp7bCwkXjWku-3JJfa-xneZP4kT3Rql2MHcB1xXj8tBV9n320PVP8K4o51jX8hUOun2XQ8v14DVuE74pAyiQc9jqP1NxclOo748mPyseRuoo9cpZhUrKubYKpbNZgTyncuRlnF-riGy6PD5c9CUCT7SLmrMl9ve4LpWvEHATZQ6Vt4c19modQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
مانوئل نویر یک بازی دیگه تا تبدیل شدن به دروازه‌بانی با بیشترین حضور در تاریخ جام جهانی فاصله داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/93346" target="_blank">📅 23:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93345">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRtMTMQjSmXJpdAx1ZzylQZ3lY3AYFrvca84-ZGZXLg5uTcO9-F7itQhZI5Xg-Ow-ipBIuy_nhlsIVNDtmgxTcfSAhOOR8HxrVi_WIh7akis5j1_fReJxd5RYcB42LS2c9-lbPTsRFBE2yfmqlwK40DA0ag5brbVvNYutVGQYtfN3VugKbpGUujB_lT8OO0ze3DP3a1ZPlDGMvgrm6znZg0WRMqR3IR3xANAY5XfFoesnEInBskZUeOVgci8_jq6ffFui3YV-pPYos4UWB6ySIq0g03XK1H4CooE0P3-OxQ3NtXzS5-7gSCTGJg_3Kn_fzkUzAEWF3UFKs2YpBqZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیکلاس اوتامندی:
ما تیمی هستیم که همه به دنبال شکست دادن ما هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/93345" target="_blank">📅 23:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93344">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fym56uA5IIZP54Ag8NgoikmETrm1upLv-A7FoGaq13W5stJ5ex7Wb06srLw3h-TTYoNykDqus-4gJn0kc2x_cL7Vhzz-jKvhTirRjEu5jQKR-jHdXwzLnTGE9R1MkXJRaiBqpyJVX662yIBY5ujvAs__MgAJa6nV0pCraNkPXFTa92uK27hkcGjyToD2TvJ9Sj2NlCbV6YOtnLYzMoCJrpDXFWGXxy8zpP1iQEVcseNzH10T6CyyKGrxYvGjkBCg5Nx014PZYQFlQmDXLE6tSithLMGUcx3FKOK3oz4DR8J6QXHV4FxP925iLjo4SWICAOu5qaH1D6N23tOMgeQvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرعت شوت امام عاشور بازیکن مصر به 123 کیلومتر در ساعت رسید.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93344" target="_blank">📅 23:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93343">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پایان نیمه اول
🇪🇬
مصر 1 -
🇧🇪
بلژیک 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/93343" target="_blank">📅 23:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93342">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPAmw0UQQUuifIkmgKBX74aznFOMScSGljr15WCUWdCzuVEiDoNdj18AkGxHsi8-BGkn8Io_ClSMT3jC84qdj3bhhD00YX2kx03i_ttSbld8RQYR0tYESMGnE22k4fBk2foTnKi6WSmdbDK2-vC85ji3ddtIMRip3MX93CjdmJg9KiRhGAYOcUL0Aqlz_-4a5SrL_3W2ZXJnWfrPg-KNcFNCiR6BT5JPP0DXSLtXL7GtgEVbRGuiojb5UVvboX-D0k5v9BOjP2KIAkI9y1N1OTjkdB6T9XT2C9_4H03xue678snC02tg7xzPQMpCVJ0tbFSSgwCxTujQxkrhLwQgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
شات بازیکن های تیم ملی فرانسه با کیت اولین باشگاهشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/93342" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93341">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df284ec986.mp4?token=GtCmj-azJvCfKlkacVdebmEwHllYoK8aGkj3k2RyhyFOfn0moMTOGdlRndisdgUH0BhobG9_OnhjPbDwd4Sf6O2tuHR70q0tdrTKgT6D3_X4bV7q4iSdCiV_Jx0tGufmTAMykqZXeQmvA0O7CtiK07yIGrwyrkxK4loS5GDi5WdNQiar0zluf3sCs30W0rNSxjoBk7GgQ2XVVvc1_uuD3K1kxRaAhWVl12bi7OUUvlJyF9gJCz3Ierxa-oXdhtualKo6DXrIO5uMRaKfSaAURvkUdaIOXXqBEwbTzNVUJoXCliT5OKn0LvHViammMxJ1mlA2Vgl9hwxIlem5EsIyGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df284ec986.mp4?token=GtCmj-azJvCfKlkacVdebmEwHllYoK8aGkj3k2RyhyFOfn0moMTOGdlRndisdgUH0BhobG9_OnhjPbDwd4Sf6O2tuHR70q0tdrTKgT6D3_X4bV7q4iSdCiV_Jx0tGufmTAMykqZXeQmvA0O7CtiK07yIGrwyrkxK4loS5GDi5WdNQiar0zluf3sCs30W0rNSxjoBk7GgQ2XVVvc1_uuD3K1kxRaAhWVl12bi7OUUvlJyF9gJCz3Ierxa-oXdhtualKo6DXrIO5uMRaKfSaAURvkUdaIOXXqBEwbTzNVUJoXCliT5OKn0LvHViammMxJ1mlA2Vgl9hwxIlem5EsIyGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
😂
شکم امیرحسین قیاسی از خنده درد گرفت؛ خاطره خنده دار بیگ زاده از حج
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/93341" target="_blank">📅 23:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93340">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMain Online پشتیبانی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5nu1O8jxgY-BXAel441duUo-vuNVP-5DtAZcMRpEpm3dwtTJLC_G-o5CapG1UYF-DeSPXkzZE3mprr36xrV4_Rxlc3OlZ0TM1kwyxL_4UmCS7MUgQFXK8In3oPfzUtMsfjpYGbnX1KTMZJdcg5gDaEWMOZ9IawlS5vFtJcFf49ot9DCaemDHiPge5hmdfiZupVm0Czh-lSY3M0r1Z1zdxbwmQj0Vahny1E8bwnGgMxpu6RxckyBj6BPDE9bIq2g0afpNZNGlwA2aAFfGqEU8Do7JmNQyC-3H8pEREvh3rTVWWPyvr7I9RvKY27ZIFNJCjoarXxd_6MV9aDg2hE2CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فیلترشکن فقط گیگی ۵ هزار تومان
✅
👥
| بدون محدودیت کاربر 999+ نفر
🔥
| بالاترین کیفیت یعنی تانل شده
🎁
| کد تخفیف : 50
▫️
5 گیگ 25 هزار تومان
▫️
10 گیگ 50 هزار تومان
▫️
15 گیگ 75 هزار تومان
▫️
20 گیگ 100 هزار تومان
▫️
30 گیگ 150 هزار تومان
▫️
40 گیگ 200 هزار تومان
▫️
50 گیگ 250 هزار تومان
⚠️
| تنها راه خرید مراجعه به ربات
🤖
| ربات :
@YOUPINGROBOT
⚡️
| ارزون ترین قیمت بالاترین کیفیت</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93340" target="_blank">📅 23:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93339">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سوپر سیو کورتوا</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/93339" target="_blank">📅 23:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93338">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOtfUhW147QUHadSm4lxQSWy19qQv_lYXI80H84xonB2R1CoqzoawLEkvul6iSbfpVqQR2big3gF7Q2-aB9_5W8SHUf2jCjtmi3-qtpyQGQsvdtJDhRKJkcqttao5-cImRbFdM186C95kWyoRGguXrpIlS-CwwkAIKH6M-BM2PpR1IYQRB2t-U-nmF_8r3PcUqa-KMHeEQ6i69ydUm4Hg00OzVJxj6fhNavsCqknua3whx-pEew2wDh6-l8CNMVx4xH43WD8aPMNo2pfNmjfad1RDX4XORSIQsBQ_mUqBz7UsOAzZORlqaOp7x4v6jTR1kngK7IjCqTdjP1OPz_4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه ای که کورتوا هرچقدر به خودش کش داد نتونست توپو مهار کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/93338" target="_blank">📅 23:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93337">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tn_EEbS658q4R8M3cd-Ta6tX9iT6nlneT2dO1KSLkfgBiv7qQfT3OHfcE6IznX7ZhxJkljMLF5wTaZOJh5P09bw8VEfRUhOE_dvK_iXfi4Sq7_C4HeFc3ixKBVMlk1Nl3dhT4FUy66lmpbnfWFsaf8D7-CWZ8rBx9CIkFlflDhYHvkt3inGiSK_d8nacGIVDR1W3DzjCZy34_g078cDj9M7OIZHAqUGrvMzh2B_z2pPi59Lv0e9jb7rc5ymB3EEbM9nxN5wDJNB4H8pusd-VU6tG8yHtxF2jXKArB-X0XrIEW59r7nZ8azsmop_M2Cx6Xv6wSjZWclrde3G_ho5xgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک بمب‌افکن استراتژیک B-52 نیروی هوایی آمریکا بلافاصله پس از برخاستن در پایگاه نیروی هوایی ادواردز سقوط کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/93337" target="_blank">📅 23:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93336">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99491ee01b.mp4?token=PsFW2wPfd6e776eL_snkcEfXlykVp0Na30_jbc1QzMN2nnvbuHixYmTHdQDy53xVrEmLHIZ4cr9Poz6Z9REHVp3OjDfScqTvl0y-TyoL3FoKPfjLXOqA7Umf3aQtBkvbysH4vyrdcA-bBcnJFAHVWoe1PLZZMvDcc8ZpSw8EPlln3M3ncuqRu3JMe5ZUrr1OHOyuf5aaZPQ748ui5ZOf58gJjTnqNtCnM6i0l1UMqexXn97ygZPnbbQC7GJ-lLaFM__5_mn-6YCJNx3RSq0HI2Z7dc27JYJt1eENpxiJGkyOBSW6f2GPiwjTPt4f6-yaSKxl41v0tz1Mo4RU_UnceA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99491ee01b.mp4?token=PsFW2wPfd6e776eL_snkcEfXlykVp0Na30_jbc1QzMN2nnvbuHixYmTHdQDy53xVrEmLHIZ4cr9Poz6Z9REHVp3OjDfScqTvl0y-TyoL3FoKPfjLXOqA7Umf3aQtBkvbysH4vyrdcA-bBcnJFAHVWoe1PLZZMvDcc8ZpSw8EPlln3M3ncuqRu3JMe5ZUrr1OHOyuf5aaZPQ748ui5ZOf58gJjTnqNtCnM6i0l1UMqexXn97ygZPnbbQC7GJ-lLaFM__5_mn-6YCJNx3RSq0HI2Z7dc27JYJt1eENpxiJGkyOBSW6f2GPiwjTPt4f6-yaSKxl41v0tz1Mo4RU_UnceA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی: به خاطر خط خوردن برخی بازیکنان از تیم ملی، شب‌ها خوابم نمی‌برد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/93336" target="_blank">📅 23:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93335">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/883c9456a5.mp4?token=aQmNAKAVXJqv2QOKXUsOpnMbOKLGpdzxw2G-9xZOA3Q5f87hWxpv77qUUc6eBKI0SPw5bomTRK8Difi2WNzd--DilQat3MaZNChsxx2AymRfpaHuMcdAU2FsVgBhHlni7d4b70u_l2wKseaIOoSwsWiRXuBiFhc-Vc4yKNkesssjDcnWxzCRmSwDOvFu6Kzcn10fN2KK3ka68VeKTdE3ou6FoJ5eUV5PNdj-73mh4m_SP2Gmkb8TBHZPpn7EArb0q93zmeCI4OZkqGb91oBfadjBqn5sO1dpZipSQdxFI4TXAN-pzqj6nNyv-4IWiFu9nxNykXmokBOVTjr7hm2EU2Hu1p5_zAEV_sVGLfGBqeZPc5hZeVJUfq806lNd_KbU7m6vkykw2SrxQ5HbHkkhsxNQQlnC4vmT3dA5CBTSnYoJM1GC13enDI9O5xqEC28NmBQCDYNp42D-BGqrq9MevWVHjOlR4MqlRQIXM5f8_ZK-xPYbpK2Eo7d3d2-x4W3DdXesRCk7eL6YQh79zsvQpR5_JU3ARo3rj1jOlUSSzDp9pkh13pngYbHD1ZGXOCakWvKnW2jLA93TFAHgkje-35BhcRJ7-yb1pNlW6-EolHfMzjnGgAZN0EY0vBzlNQZr7y5QGZZ8vx1muWSF0sJLC48u2rDNuSoY1LsEBQumufE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/883c9456a5.mp4?token=aQmNAKAVXJqv2QOKXUsOpnMbOKLGpdzxw2G-9xZOA3Q5f87hWxpv77qUUc6eBKI0SPw5bomTRK8Difi2WNzd--DilQat3MaZNChsxx2AymRfpaHuMcdAU2FsVgBhHlni7d4b70u_l2wKseaIOoSwsWiRXuBiFhc-Vc4yKNkesssjDcnWxzCRmSwDOvFu6Kzcn10fN2KK3ka68VeKTdE3ou6FoJ5eUV5PNdj-73mh4m_SP2Gmkb8TBHZPpn7EArb0q93zmeCI4OZkqGb91oBfadjBqn5sO1dpZipSQdxFI4TXAN-pzqj6nNyv-4IWiFu9nxNykXmokBOVTjr7hm2EU2Hu1p5_zAEV_sVGLfGBqeZPc5hZeVJUfq806lNd_KbU7m6vkykw2SrxQ5HbHkkhsxNQQlnC4vmT3dA5CBTSnYoJM1GC13enDI9O5xqEC28NmBQCDYNp42D-BGqrq9MevWVHjOlR4MqlRQIXM5f8_ZK-xPYbpK2Eo7d3d2-x4W3DdXesRCk7eL6YQh79zsvQpR5_JU3ARo3rj1jOlUSSzDp9pkh13pngYbHD1ZGXOCakWvKnW2jLA93TFAHgkje-35BhcRJ7-yb1pNlW6-EolHfMzjnGgAZN0EY0vBzlNQZr7y5QGZZ8vx1muWSF0sJLC48u2rDNuSoY1LsEBQumufE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇬
گل اول مصر به بلژیک توسط امام عاشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/93335" target="_blank">📅 22:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93332">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مصر اولی رو زد</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/93332" target="_blank">📅 22:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93331">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/93331" target="_blank">📅 22:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93330">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔥
🏆
🇦🇷
پست جدید لیونل‌مسی: بیایید یکبار دیگر در جام‌جهانی کنار یکدیگر باشیم
این پست مسی با بیش از ۲ میلیون لایک در فضای مجازی حسابی وایرال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/93330" target="_blank">📅 22:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93329">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10e04857a.mp4?token=gSBDb5YXDoDXcx_iKMrSLGzb7tDKuXUYKUxCQmDzWCVhqFryG7Xc2-PvnxIL40ffw5ayWpyGKaKiAImu91g6VwlqZis4dfb8jUlq8C-Ku0SBqmMz2uoEEOuaivruG1tjXcV-kiES88vkKf4VpEfPi8tRuU65ZWHJ_yPVaP6cYz-yF2zm4QrGrpvpVmovMf3U4xu0ilqO3CVS_dd41RbNx2Cr6Epw1SS-wkRTPuHQW-7KZyFIegxzzO99PBeKLWryeYxzOfFs50xnXo2NbxoX32Qsa1nrZaBSI476KQfRDltFlz8DPMbhBzLnXahtxM00ViNegKqiYOEKEXYMG4LwhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10e04857a.mp4?token=gSBDb5YXDoDXcx_iKMrSLGzb7tDKuXUYKUxCQmDzWCVhqFryG7Xc2-PvnxIL40ffw5ayWpyGKaKiAImu91g6VwlqZis4dfb8jUlq8C-Ku0SBqmMz2uoEEOuaivruG1tjXcV-kiES88vkKf4VpEfPi8tRuU65ZWHJ_yPVaP6cYz-yF2zm4QrGrpvpVmovMf3U4xu0ilqO3CVS_dd41RbNx2Cr6Epw1SS-wkRTPuHQW-7KZyFIegxzzO99PBeKLWryeYxzOfFs50xnXo2NbxoX32Qsa1nrZaBSI476KQfRDltFlz8DPMbhBzLnXahtxM00ViNegKqiYOEKEXYMG4LwhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدل پدری هم پیدا شد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/93329" target="_blank">📅 22:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93328">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvgfmpZZSDlxsRuczPlKn8xY9KAjA_tEIKUadHMzjtn-WBNlEyt0bss7lbRkCFJFSoeY1pGc3MnnDqGqq30OQxIKnCXyqPczdw_fn67gfyyoP8r1hqoxPrh3GxQM-tYMGK3wCiXXVy9hu1Kc6Dg-9bNEgQnX-d6eFyjxModfKgQ7ahORfCU7g6WJRFAokatVFUVn2TfM8Uh7rT41C6208r54EkvE_GfH7kxouP93oy5RkuLk2Me2gTF1b0uYYQb4_M6JXh5rTv4Noy7Jrb2cyx-B8-D_t83zyZ-fCYvOMxlnVL7aGrrYFJ4utpsKrRiyNMbf0suhsJd5Ih1aYvx1aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
ووزینیا، بهترین بازیکن کیپ‌ورد و اسپانیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93328" target="_blank">📅 22:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93327">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeUlp5RmhCvOH8d5diRX9HQccO4cSCi_lyFffue7J5oMR-4Z52osnDk1Vc1BJ-nTsq1PkZfd-JVMqq91d2D1bgs2uFmI4g8T7ApeCXQUKG6HwagWyTK8PdJi1Le0JjYV1hDp1EJiA3zPXnoIr7WPs4RcnkdCwkjjGl_YBrobVMbTLSJ6nRxDBAiZF85dOWdeASWJ8LIW5jdO9DR689RCuSyfw2CR7uncb07dD1qlN2jisSbxlKte1lFqF3qv-nrCesqYRyAsK9PQgQDriT7VKE8wNO6W-M2GgCKBDFtMQvoJ-1fH7jqfPvq1hqkwH2v8gsuIdjlR3pfKH37MlEFHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادارای مصر تو استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/93327" target="_blank">📅 22:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93326">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmEcizo3FRykZMlKQUwcrdInG2ou3htWoj3hQtB3M2jvkLGYiVNCzw0f7RmfwJCxBvmUS98yBNNN1sSPAPR5Jb0CVbd-Sh11O4QQMUfsUMEO3F-tNZYCo_sx4xNYm-Fi8sfTJ85Scv_Y45h0GSGys06iVa0-Vqh0PvnMxUO65KBUSezrv1VUDpPYwYzqFVkQCXig4r-ZNMLLdeNu_SI_dnTczQ9UGDYoLcpxrFleduWoFizt0J-CRlQGbqZJc5vqjEwtVnuiuxOMQjxKJ2phjWJde24OFAwBBXZ5Hxa8z-mpI-UFO9CwDvhGIngKSwcyRE6A5qWMPOQIXTLpS6ZU0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
⚽️
۳۵۹ نفر فقط با یک پیش‌بینی دقیق، ۷۰۰ هزار تومان جایزه گرفتند!
🔹
در بازی سوئد و تونس، ۳۵۹ نفر نتیجه مسابقه و تعداد گل‌های دو تیم را درست حدس زدند و از جایزه ۲۵۰ میلیون تومانی این بازی سهم بردند.
🔹
سهم هر نفر حدود ۷۰۰ هزار تومان بود که مستقیم به کیف پول همراه من واریز شد.
🔹
در این کمپین ۳۴ میلیارد تومانی، قرعه‌کشی در کار نیست؛ هر روز ۱ میلیارد تومان به ازای تمامی مسابقات همان روز، جایزه نقدی بین پیش‌بینی‌کنندگان دقیق تقسیم می‌شود.
🔹
شما هم با پیش‌بینی دقیق نتایج هر بازی، می‌توانید جایزه نقدی‌تان را مستقیم در کیف پول
همراه من
دریافت کنید.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/93326" target="_blank">📅 22:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93325">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بازی فعلا درگیرانه دنبال میشه و تا دقیقه 15 دو تا کارت زرد ثبت شده</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93325" target="_blank">📅 22:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93324">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjhUKudnQ-uiwq43cf2yQbURvWMtYDa2CKaQcRA-n8kEyYX-_Oq4kiglEVE_WZIrx6ThM4hLdNaXnN7XE7j-6zNpmk9973pntK2OHs_LHvaYhocEMFih9AGWzjdty-s6xWM4w3ey6sTaBdTqQXtLvdkFXsSODVcWEjLQMx_CJ4-aGgFC6kzwmp72z5z_YNUXi3nuUjo0OowabWo468P9N2kICWpVc6BZnavF9gSqdOMontfHbz2JBmwbUofvjCsGqdZZp1gQyvHaaSp6tMsIkOGd_gx3lhLmgHOzAqwPQFJvpT4buT39TR47mJWSAuI0OJNIHWXQ0EF7axhfmTcPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
اسپانیا در اولین دیدار از پنج جام جهانی اخیر تنها یک بازی را برده است.
‼️
❌
۲۰۱۰: شکست ۱-۰ مقابل سوئیس
❌
۲۰۱۴: شکست ۵-۱ مقابل هلند
➖
۲۰۱۸: تساوی ۳-۳ مقابل پرتغال
✅
۲۰۲۲: پیروزی ۷-۰ مقابل کاستاریکا
➖
۲۰۲۶: تساوی ۰-۰ مقابل کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93324" target="_blank">📅 22:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93323">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بریم سراغ بازی مصر و بلژیک
🔥</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/93323" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93322">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9bSQRBpXCXwS1D--MWimaetKlaCgHQrGwNMpcSoHQw8oKSfNWKCWqmcazplAVVCSmlLnUNp6T_pmMSv2XcS-eO10P_3lD8wQn8nZoZQf-ezunrq62vAnZoxvTVKvizmNwbz80JlskMJn5BSSz0nLqZtzDX428N4QaYYFB1f5KjCyceJZGr_9d4EQ7TzjxdeS5l1y6apoqDnbzpHXErsPu-ST2d67IKdDr3BSE-y1WJZlvlvMG6LL7KXTbhEdUfVt8Ny3Sl89C5B0Jhr-baxlegPKU6otV-E3jX48y0Wj4JCjtdWmfK3asOEUDHz_J-ClY62-4C96lhVsrQL9pnBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
پشماتون بریزه ووزینیا بعد از درخشش امشبش جلوی اسپانیا تعداد فالووراش از 50 هزار تا به 1.6 میلیون نفر رسیده و همینجور داره میره بالا.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/93322" target="_blank">📅 22:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93321">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6DziTL09Hy31QykbtMdWwVcRxU0CDcAV34wVxrZsezyS1xG6L3NWWI9ZqVmOU3Vbj3ZXs827eOHWTJg11VAPOT59kdLis7Z7EITqW6k5Y69To_RLmrtDhPL0UGf76yJxmwujyYUZFX1GDOQorck8Viaf-e5aK3x8mOgBSSNoe7yWPS6EBJZC4NV6ERgOyMPq_5Utphqy99ZrzvAtW-2JnpeE_mZuFY7U5Y2mHUM-XKxpLNPm9hiQBNlk89Nsybv-Wp1M_UBd9HmMzcT4c5mf48_n6kaCWHI25KtEEoVfJAUVRliBKWwQb8nkmJjDEzyfb_lNa-CGtg6PcjKUa_DTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا بدون وینگر تفاوتی با یه تیم معمولی نداره.
۷۰ دقیقه بدون یامال، کل پلن این بود که توپ بدید پدری یه کاری کنه!
با یامال و ویلیامز اسپانیا میرسه به ورژن یورو ۲۰۲۴، ولی بدون اونا حتی توان بردن کیپ ورد هم نداشتن…
البته گلر کیپ ورد هم کار بزرگی کرد و یه امتیاز برای تیمش گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/93321" target="_blank">📅 22:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93320">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZhQSsnugrByJYgyrZeE5DNisQMlB8hbDdVWtUeRLRaeZOGVVRJnM3zGJ37eyc1LGaUUZ73VuW9fvcNJgJWssGq04OLVDuP_uESDNfSe-y9kSOxz0SELlMYQ41sAraCITHzMAgDwhCuqZuFXqy2UA4SHkWZtlTPUAZidODmJqn7TKRqOYYSC8qXlor_HdRkN8UMTkjOLmZo4HRKOSX3i56gSmWonUzh7Pr4fZvwcmAinjrRcfQFldevpJHTGRipnBML8D7wXGadSu8oJDhosm1D1f76jFWr9qhke-rkEaejKo9X-vbHrOnnpmOJaJtYb974WT2sXwM_zrD9HwEqk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم برای دلت مَرد، ضربه ای که تو با شرط بستن روی اسپانیا خوردی هیچکس نخورد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93320" target="_blank">📅 22:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93319">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b27f7be0b.mp4?token=roqwQsAN6aRS0iN6crT3LHx5dekpnMVrR2AB4vXjij94VlMWtR2Ku1NnoKzCJyIX5KV2L5kyb8ZOJpKnamx38gViBZF_rptxBi3kwF5XnS2Hmg97oBHysV96Dk8sMokM4jAU_jHYEAquuXj6M2TorRhFI5IN7sIgFeE-4zrsyXxG3YPpBUxjWH2oUeZdH06bBzMH5f_tdQAxe3Lr5pw87icLJMu8V2N-EC0WCTodDAr-hxE8Ntz_HdBZf7VEmIppgSe59PaJRO-XoR2cuqz_vXOuOZhhqRM8Yn-DATlIM_VqbloKeL-Ce3yYbW2JNp1Ep60qUXaiYZK_UxkYjvXkKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b27f7be0b.mp4?token=roqwQsAN6aRS0iN6crT3LHx5dekpnMVrR2AB4vXjij94VlMWtR2Ku1NnoKzCJyIX5KV2L5kyb8ZOJpKnamx38gViBZF_rptxBi3kwF5XnS2Hmg97oBHysV96Dk8sMokM4jAU_jHYEAquuXj6M2TorRhFI5IN7sIgFeE-4zrsyXxG3YPpBUxjWH2oUeZdH06bBzMH5f_tdQAxe3Lr5pw87icLJMu8V2N-EC0WCTodDAr-hxE8Ntz_HdBZf7VEmIppgSe59PaJRO-XoR2cuqz_vXOuOZhhqRM8Yn-DATlIM_VqbloKeL-Ce3yYbW2JNp1Ep60qUXaiYZK_UxkYjvXkKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
ایرانیا لس‌آنجلس سازشون کوکه انگار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/93319" target="_blank">📅 21:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93318">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/678ca94f4f.mp4?token=QLWi_yayUgN8OM5NQs_KbD_pcpGMuF0HTpEcE-iI9Xtgh0rGLV002G7sXaSdK8UbyWUs7z_1lusJ_b4rWFCPcwy5ZBBUw9cBcPGpGy1t5eEcltF6mukIbJgSTBji-I3o6ubLeyql3xDvJqx_vpYs-JaoLFG6BrWpEG-EAQfU6_Hs6uvnzzWItfYsgSCoeqM6ZTaIv5X1YKWyzHxHUrhYt7-r16ykmef0difeJlucUjvOd2HYwtzBP7bE0Z0_SrLCWHFIJzku0xWOZ04bPi5RGhID-P4wUvkJpYml8gnHLCqg4Tfx-xSy3IO35oaqSW0QfE4bxdklp7codU8vH2M8kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/678ca94f4f.mp4?token=QLWi_yayUgN8OM5NQs_KbD_pcpGMuF0HTpEcE-iI9Xtgh0rGLV002G7sXaSdK8UbyWUs7z_1lusJ_b4rWFCPcwy5ZBBUw9cBcPGpGy1t5eEcltF6mukIbJgSTBji-I3o6ubLeyql3xDvJqx_vpYs-JaoLFG6BrWpEG-EAQfU6_Hs6uvnzzWItfYsgSCoeqM6ZTaIv5X1YKWyzHxHUrhYt7-r16ykmef0difeJlucUjvOd2HYwtzBP7bE0Z0_SrLCWHFIJzku0xWOZ04bPi5RGhID-P4wUvkJpYml8gnHLCqg4Tfx-xSy3IO35oaqSW0QfE4bxdklp7codU8vH2M8kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🏆
انتقاد ویرجیل فن‌دایک کاپیتان هلند از هایدریشن بریک در بازی های جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/93318" target="_blank">📅 21:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93317">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffi3Y6t6mUG3N_mk_5Y9ChOe4a_4JMunvq6QIF-Xye6ElN8k0SepHmqOWF_e6lx1PcUTe3BR9AoEuyRVcIb-GadFGH3pZ5gRZ6CuEKmDIQ7R5T3UpwPMntDfKcISyWycKxyRt-h3obcLW6w68C2mPf6446X9hyVo2WsgEHXDOea_3LPNjqQ1v7pIXaempoYfGqT09aLNWo7uGb62zuN3q4BdD4LCOz-anENFDgGsYs2XnUDwPJUolViUgoWffk-dx5w94S7qTdNybCmqz3NLOhJX-lPS0xHoKN4WtLZT5UMH_-eweYG7exPVLbgacLzZsDi7bL6VC_O43SqZpUa2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🆚
🇳🇿
ایران
🆚
نیوزلند
🔥
نبردی که برای ایران فقط یک بازی نیست؛
شروع مسیر اثبات قدرت در جام جهانی 2026 است.
تیم ملی ایران با میلیون‌ها هوادار پرشور،
با انگیزه‌ای بزرگ وارد میدان می‌شود تا اولین قدم را محکم بردارد
⚽️
🇮🇷
اما نیوزلند…
تیمی جنگنده، منظم و خطرناک در ضدحمله‌ها که آمده تا معادلات را به‌هم بزند
👀
⚡️
🏆
آیا ایران می‌تواند با یک شروع قدرتمند، پیامش را به تمام مدعیان جام ارسال کند؟
یا نیوزلند یکی از غافلگیری‌های بزرگ تورنمنت را رقم خواهد زد؟
🕟
ساعت ۴:۳۰ صبح
📅
سه‌شنبه ۲۶ خرداد
📺
پخش آنلاین بازی منتخب داخل کانال زنده
🎁
شرط رایگان ورزشی ویژه کاربران جدید
⚡️
هیجان لحظه‌به‌لحظه جام جهانی 2026
🚀
امشب فقط تماشا نکن… هیجان را زندگی کن
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/93317" target="_blank">📅 21:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93316">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
#فوووری
؛ نتانیاهو: بلایی که سر غزه آمد را بر سر جنوب لبنان خواهیم آورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/93316" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
