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
<img src="https://cdn5.telesco.pe/file/QiVnFq6pQeUGCSTv6-K8IeAUwFEGF6XFGiU7uwKJ3Z-hjBoNMJ18Ks4020A-NVlDzGXbpni9vCO7PQqcbc6JcWedc-aW2hx2N4LOSUuiJL6a1Cc55f3vBPbJY0b_GC8f-9AE2gIBG4VYY0H57fup8_puLdlA05IOwdstjiNen0UlWVyEXfZUf11sBa1oT2ex_tBfBpTcOiml3fJDb_ti_Df0skIs7LMGsvYkTv4z_-M3vwlnde9JmJHgtL-x-I_HM1aGhGFsjB2pWJxbCrFIYeT0rR71EOtwyEZE6R9R-xUXx9hRTPlhzNij4eqUfIDL1CiQu0Kcdcc-U_4z4ZjnIw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 448K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 19:44:04</div>
<hr>

<div class="tg-post" id="msg-104477">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb3d0d855.mp4?token=jeyax6f_k6XrygaGWNh6RgKSUG-xGZzSgZiaZ_lo37fTkN3Oy-H1EtuVolzL0P_h9w2zcYAvAwj-7VNfy9oUJrTYRLtY17cgD9SCsqTsP0_30k9hq5vMS4D9DJCnpUymov6zRWVanP0rZ4BS0YeAxieb3YcyYORbK1wV3yZsCGac_nFx2QXN6z8dZZuVorSnm8DB2FSEUuFFCxFVzLfJHJw9ksJA9f-1R7jlxQ1CZ0QFud5cboGYmoXdWrf6KFiysWoAybfYwpxqEF6BO2_X8xVrr0kkn1oiztKAbkwbsi-26zktVCvyesDzrQ-o7pnrw6Keh_nWjQQ8Tewnw0er2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb3d0d855.mp4?token=jeyax6f_k6XrygaGWNh6RgKSUG-xGZzSgZiaZ_lo37fTkN3Oy-H1EtuVolzL0P_h9w2zcYAvAwj-7VNfy9oUJrTYRLtY17cgD9SCsqTsP0_30k9hq5vMS4D9DJCnpUymov6zRWVanP0rZ4BS0YeAxieb3YcyYORbK1wV3yZsCGac_nFx2QXN6z8dZZuVorSnm8DB2FSEUuFFCxFVzLfJHJw9ksJA9f-1R7jlxQ1CZ0QFud5cboGYmoXdWrf6KFiysWoAybfYwpxqEF6BO2_X8xVrr0kkn1oiztKAbkwbsi-26zktVCvyesDzrQ-o7pnrw6Keh_nWjQQ8Tewnw0er2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
گل دوم استقلال به سپاهان توسط قلی زاده(10)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/104477" target="_blank">📅 19:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104476">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسماعیل قلی‌زاده</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/104476" target="_blank">📅 19:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104475">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">استقلال دومیووووو زدددد</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/104475" target="_blank">📅 19:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104474">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گلگلگلگگلگل</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/104474" target="_blank">📅 19:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104473">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f589e085ba.mp4?token=pln-Jh7fvP6dsyjD8NXWwIzNfgU62h2pg3MJvLayV7JUR7A2rVg8LnySzX70jebieawN29iSXsy1SrOoEgk3dD7PF1GMtvUZu-YxivU1LXYxLSP9PeZQjZdGU87ZNl94PKzM1v-2Qs6p1SiRXzXOOmw16QBMvJ8E5UnmeFrD3aMmtIzEvpvMKagE-Q7eeO3L1hk0FuFsk6Bn3lmLfr2n9F2hSdwhoOhJjfxoUMnWqdCbW5aKmQtYLUH0mWijyKBl2B4yO1XRFRHfuONaGBF70uv4f-DiK1l31X7Zhy77Uc0LBm3w8SdISIHOuChEIzXOH0poBEjfphucGEbemJzg7YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f589e085ba.mp4?token=pln-Jh7fvP6dsyjD8NXWwIzNfgU62h2pg3MJvLayV7JUR7A2rVg8LnySzX70jebieawN29iSXsy1SrOoEgk3dD7PF1GMtvUZu-YxivU1LXYxLSP9PeZQjZdGU87ZNl94PKzM1v-2Qs6p1SiRXzXOOmw16QBMvJ8E5UnmeFrD3aMmtIzEvpvMKagE-Q7eeO3L1hk0FuFsk6Bn3lmLfr2n9F2hSdwhoOhJjfxoUMnWqdCbW5aKmQtYLUH0mWijyKBl2B4yO1XRFRHfuONaGBF70uv4f-DiK1l31X7Zhy77Uc0LBm3w8SdISIHOuChEIzXOH0poBEjfphucGEbemJzg7YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
سوپررررر گل یاسر‌آسانی مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/104473" target="_blank">📅 19:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104472">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یاسر آسانی</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/104472" target="_blank">📅 19:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104471">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">استقلال زد</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/104471" target="_blank">📅 19:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104470">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گلگلگلگگلگ</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/104470" target="_blank">📅 19:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104469">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCXF-hFnvFQKveRODY2pKWTFlqDnWEPrKx-tOKKEjH65VxNmBDoqpQBsTlt-JAnEKlYP4w1lSvLhAX8AbP4TSY8Y2e4k96gb7sGxQ5Vt_4etbyi1GGN9G9YNhP0-gIoUUkSYkQVQ-zbS2xgc6J-yMNGR2qP2186SoOiid1v7lT-YxxGdOtNGUmIvTO4_JHo-peO0XwcLCtdSV_tMpLCNnrRTtSTaq1qvZy9NdzDCR3h-hN4i_g8MdjlR2ZGvbhoNqegGRi7snI51Rt--Kr0t4VPk8dklkEuJW1GKdf30__ktZKYcNuwLkL-jsc_VJCPC5Fj1Wjhz5635cBqSEGb0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
هو شدن شدید آلوارز در بازی امشب اتلتیکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/104469" target="_blank">📅 19:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104468">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ae17874e.mp4?token=PxTF403O4LTWgzv0BvHCpG-NZQ7WG2zjM-ZY4h5Rf4wwlAgQAnu-nwcOtQjxucA8h1yZ0cM-jDsgfGm5jOcbWKtqv5W1tImYjdtRZetT4H9k6gmAOJSVA3JSKOcBMKMNGDo5DC69LidpZYkwRnJpfTfhzDvqTS9l4duTX6-_mzopLvrNWrKuQ8608t8lRFugSoQisTjgv6V2pHPyt5aM08ROj_rSxf-cvwMl9_5FRH6s4Bj_t1IfPSeLFgobvrXexjyLAxfK5biwvEzLQziivXYafiAyRRHXLoG8bMS5XXBqwoNjVKP0eDurPbM7W_6Ocwoi49-BIWJCy5XIfGOyQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ae17874e.mp4?token=PxTF403O4LTWgzv0BvHCpG-NZQ7WG2zjM-ZY4h5Rf4wwlAgQAnu-nwcOtQjxucA8h1yZ0cM-jDsgfGm5jOcbWKtqv5W1tImYjdtRZetT4H9k6gmAOJSVA3JSKOcBMKMNGDo5DC69LidpZYkwRnJpfTfhzDvqTS9l4duTX6-_mzopLvrNWrKuQ8608t8lRFugSoQisTjgv6V2pHPyt5aM08ROj_rSxf-cvwMl9_5FRH6s4Bj_t1IfPSeLFgobvrXexjyLAxfK5biwvEzLQziivXYafiAyRRHXLoG8bMS5XXBqwoNjVKP0eDurPbM7W_6Ocwoi49-BIWJCy5XIfGOyQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🇮🇷
شعار هواداران استقلال در ورزشگاه: سپاهان دوست داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/104468" target="_blank">📅 19:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104467">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
صحبت‌های هوادار استقلالی که برای تماشای بازی تیم محبوبش، خودش را از آلمان به ایران رسانده: ما مثل بعضی تیم‌ها کاپ پلاستیکی نگرفتیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/104467" target="_blank">📅 19:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104466">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/141a2ee698.mp4?token=hEuIgqs8o78mluXAj1kLN8A27n491g9bYTmAyFSIrrByDpQE10Bzc0MyJZihkqQB7eSuCGShGRXyNhEaUEBa_YPQdXP0tANpL6TQs9vk3vFc-woPDDwWXIhqrt9dctrML47BEWaKU27Q3O5ziUNfiiprCMi5zST9tV-EBx9FBh6Yp_g-1BihUuUPeONEIyFmv9A5EVg-MFIGWvTUxS_b5M9I36rxZgLEpNEF99BzFoSX8mLURqOc7GHEGu2P56tZ3TfSdIAnhGy5eQjvF85E_6J0DB1zrx7UrMbz7KXWD0RJVSeWF37HYvkgTMtM3up8irJgc2M3z8cVi-FuqOOKww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/141a2ee698.mp4?token=hEuIgqs8o78mluXAj1kLN8A27n491g9bYTmAyFSIrrByDpQE10Bzc0MyJZihkqQB7eSuCGShGRXyNhEaUEBa_YPQdXP0tANpL6TQs9vk3vFc-woPDDwWXIhqrt9dctrML47BEWaKU27Q3O5ziUNfiiprCMi5zST9tV-EBx9FBh6Yp_g-1BihUuUPeONEIyFmv9A5EVg-MFIGWvTUxS_b5M9I36rxZgLEpNEF99BzFoSX8mLURqOc7GHEGu2P56tZ3TfSdIAnhGy5eQjvF85E_6J0DB1zrx7UrMbz7KXWD0RJVSeWF37HYvkgTMtM3up8irJgc2M3z8cVi-FuqOOKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول نیوکاسل به لیورپول توسط الانگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/104466" target="_blank">📅 19:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104465">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d702269fdb.mp4?token=pT91E6KNQA2NifnDpyS5uAZ495H0Mk5rgKTV9LVMULRNbsn-GnsRsK67n5qnKthVGHTzECL5mILTktscDo6Qs__2nRr6QvMDjbxM6JlDSGKJNSEzxThW-RuQI7EmT_ZuOyRqFs9cYPNDoNBMsN7u7lqclZzac60hERPpbehWGS_xKANKBtBnokmHknLzOUShdaCnBRTPj2Q8vw0QMxK0Xxz-rrEmjKGdS8kEsazQ7HETAjy8yIX1DnRscH50It4_Di_uFmll93FeVJ1y_LEDGBjy5EhilifYrQA6WVrMgIYqivCxvhHBmMvCVExcfFRoAcR-CMPiCpF94beqz_q63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d702269fdb.mp4?token=pT91E6KNQA2NifnDpyS5uAZ495H0Mk5rgKTV9LVMULRNbsn-GnsRsK67n5qnKthVGHTzECL5mILTktscDo6Qs__2nRr6QvMDjbxM6JlDSGKJNSEzxThW-RuQI7EmT_ZuOyRqFs9cYPNDoNBMsN7u7lqclZzac60hERPpbehWGS_xKANKBtBnokmHknLzOUShdaCnBRTPj2Q8vw0QMxK0Xxz-rrEmjKGdS8kEsazQ7HETAjy8yIX1DnRscH50It4_Di_uFmll93FeVJ1y_LEDGBjy5EhilifYrQA6WVrMgIYqivCxvhHBmMvCVExcfFRoAcR-CMPiCpF94beqz_q63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
هو شدن شدید آلوارز در بازی امشب اتلتیکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/104465" target="_blank">📅 19:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104464">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr0jgVVOmkUeeljHuiJN9fXUmNpxVuGYsBO9MvGV0E0zkTXalNgTDCEtVvoAcnj88VI3qJiisNOlqJfm_qT3I72vonja8eOkqg-zxDcIp9316payKGkz3PomTv9F96q1vq1qvAHd7LWC7moEL6AYjP69yzGOWHgWQPq9TckOc6Dp5u0mA3kh_EgvT1_IP0Tbxh4pi9NafbbVQMZUfUxf8pvFrdKKINaz3Y5jhc_LZ8gmDxkWwmmhddLRPqsMuxytO41gnIoRF33wIayVTAARGoHNEWZksn5o_n3w6sErGtmY8Jvvf3Mdk7Amh67hlyRC-GPpH6A0-mCDt3DdGv4Zgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
شماتیک ترکیب استقلال مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/Futball180TV/104464" target="_blank">📅 18:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104463">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF2ORrMbu6AoLDu7xUCytupC8cTQeOQZ06ltDCSxz4CSaq-KI2cTPgcf8sro279VpchxxvN6kqwkyRlV6kUVxDaao7ZG6r_qdFjsoB3Z1cqCAORRE1-r2-nEQPxHhYcyLor9vltd469bEzsG6maWlksXA-8fU12w8b6gJMbhB79dAVnus5_ts3odb4r_a3Gli7HRtY7rXNISyzHatDhul7b_Ovfgd_b_26Nc6lfl4B5mgNqZ4SaNm4crK6_uYAASBUpfrniUrgklq82QWJn6E-7zU5SFfZtN5UOt1IJyschVO4x2UZyOET6F4HLsQDgwh2paglP_FQBSgM83DPytjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
ترکیییب استقلال مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/Futball180TV/104463" target="_blank">📅 18:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104462">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUOCsuj35VIxdJn8xnqNFiB-AaNIeTu7Dvuk1oWuLlZS9cfHYjXU5bemJrvgfWh7fUBIXZNXfLQyqr968NnPC8Xje0Z7v986rb2SeNXZxuwBFlZJVOH9qKczE8oFmRd7iWVEWK1b5ooaN6uab_n_oK4BTF_XylWXPxdAYzsNIhrCPeh4CRsRoPXZbXTk73Q6IvGDkQt2DzYv5-A6tnW45ruECD5Lxus9otpcpxhxCw1cxyb8_Q6y6lm3oAHV9y2YthcLwKV2Dg2MohX8g_GxxZ6g692JSlcsd5WZxF1dz2lDgZaHvSDsjdslV3h2w8ONttpiaiXyYQT7bD_yd-gwcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
ترکیییب استقلال مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/104462" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104461">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDWpvNglNQvncdL6RBu71hblFSC03e72yQq-yvN5_acVWimhDH6Ru8vZjWgiH0HsegyA5MkMKn-1DvccnTLs3fCCtQFfhnJwIE1fkrKo7BbGf20HcgvHNgQzmTMBDAHGluJhiJMtN9v_Br75qwMMyIsLgrk4XuwURzrJxHoTSCKjC27W7CxUE05k1dLiW433zIB70p35kcIt-CQ1DJPzLdVnOwQb2HBR7DM0HQpbq7EWPOsz6q4qEWtCTTe54s2LEP2L4nAYv1r5k3r9Vr8VZP-2054prYyxF9hH2zi6kueN-PHmxUkiHdCwRXqYNsaVs_VXk5OMkC_b15CbSbZWnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیگ برتر انگلیس| مدافعان کار را برای مارسکا درآوردند؛ کامبک منچسترسیتی برای گرفتن ٣ امتیاز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی دو - بورنموث یک
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/Futball180TV/104461" target="_blank">📅 18:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104460">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dba451e740.mp4?token=Kdtw2YoB67WYNC3DjgmHaQMNXwpe8WPn44Oi6vgRo1h4cjn-m9fiwzUVS_twQ8tLb6oEycjty7l4Sh7pEw0NKSkxYc96jsqHOoQEmtORkL7du1s4_cakYRkM53llH7IDyxusquRvHWuX2v89HQf6RXKQr5OLO2z6yzltDUMDvxIWryaVb8rF-BsYegdO8coTdxMhWnkmht68vwMP6Cp1xioNAMvYgDZv0wN2yTLCOYN5Qe9LQZYcIWta7gM45rsfSYrI_5WQcvyoBWST3STPPLqVJMXHdvdu2EtINZienlR7fPb8np5ctjxBXT9gyXax-ipA4Llq06i7fpe4bsmzIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dba451e740.mp4?token=Kdtw2YoB67WYNC3DjgmHaQMNXwpe8WPn44Oi6vgRo1h4cjn-m9fiwzUVS_twQ8tLb6oEycjty7l4Sh7pEw0NKSkxYc96jsqHOoQEmtORkL7du1s4_cakYRkM53llH7IDyxusquRvHWuX2v89HQf6RXKQr5OLO2z6yzltDUMDvxIWryaVb8rF-BsYegdO8coTdxMhWnkmht68vwMP6Cp1xioNAMvYgDZv0wN2yTLCOYN5Qe9LQZYcIWta7gM45rsfSYrI_5WQcvyoBWST3STPPLqVJMXHdvdu2EtINZienlR7fPb8np5ctjxBXT9gyXax-ipA4Llq06i7fpe4bsmzIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
هوادار استقلال از تصمیم بختیاری‌زاده حمایت کرد
🔵
هوادار استقلال تصمیم سهراب بختیاری‌زاده برای کنار گذاشتن علیرضا کوشکی به‌دلیل مسائل انضباطی را تحسین کرد و آن را نشانه اقتدار سرمربی در مدیریت رختکن دانست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/Futball180TV/104460" target="_blank">📅 18:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104459">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/Futball180TV/104459" target="_blank">📅 18:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104458">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐇𝐚𝐉 | 𝐅𝐢𝐱𝐞𝐝</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1QnVATW19crtdafnArQlqZP7_KzWwvDd9QEQJ_E5Wfg8YmrOv50WoOaibp0EXjK-wE_u__KzCyVMWWbK2vtY3mzg7RtSsvvV14KHLyUCzHQF2zWRfHMjnK85DuX0bk6Irv0TgrLZzkszZDrJ-H85ROVh_iuXw8YmYyeDCJRLLb6_CuqXM6lEfXQZmOOHqyv8po4N14LU6EMYUwZQxKNhE5IthgwsJGpwFFrzxfzhFsZ37czoY1ZI2qxyQW_Oe3gkd7IYVTiz4ALZN3RegZlXzap7LSU_1GpUNhwP4NJ_laFm5ANmBN9gCPHIr0mqY6G6w35DkUylhSQZ7K-I1ixSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/Futball180TV/104458" target="_blank">📅 18:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104456">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUPdIFe_qVaW7Ketds_P0e__Zz8v3wnvVYCtLni_5YgOVtkWj8Eh0fzmXuoLyFsmDVLfACoHmJCSoBHYa1ZJ9kbS4WWrXpycdgXYF31fk12mRHphjQhJghyj6L6L2fgH6DWybbev2F5dFyp_3ark4rvsEjZ6i1G1E91cXFdRJmVvLxnQJ7n7VlsrzPOm7pr518zHHlYjIJF_imFn1lIyJix5_ElzVvR-WJkpx2QW9dHaI6yh1cC_B05BjBvpQ5HeaBtEuMdIHJrwzcap4ZBfndEsMsSsgekwyOkvXXp5Jp7kaOrAtHSqPRUQNXYXxMQaUBeHr-0jK_5jO58ssmhyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhN7pSbWQj7G4WavL0ZDKORyPMfqDVUeO7kgoLvGu0xJ8xZUbFt3aDPwFbKod9zImKtXgGeb7q2NPlVhP5p0S-p6NRAaFevRGyhuatSx-yht6W4oT7tVv3tT_XLsGUTgWZrATJOru8eD6Rezyzf-_cRfnZx_mchhbniQQhB8ClxuOe4qA0mnBQ0CcII8sLXG7AqD4TZD2gzo01mSOR5S2F0i0ekxU5uCn-kzWU-07z7Y7fo6BqhGu2--Nu99TOcvnNqfH_SuLTtrAbRYeVJLas5bMS47MSDL4_HYCOSKYmPfKwfcmHxxJQtzFQ6OuR_fO9EOdE-8QIU_KwO0no_1iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
⚽️
ترکیب تیم‌های نیوکاسل و لیورپول
⚽️
لیگ جزیره/ ساعت ۱۹:۰۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/104456" target="_blank">📅 18:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104455">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🇮🇷
هوادار استقلال در واکنش به برگزاری داربی در اصفهان: امیدوارم آزادی آماده شود تا باخت و گریه پرسپولیسی‌ها را در تهران ببینیم/ ان‌شاءالله سال بعد می‌گوییم سه افتخار در آسیا حسرت پرسپولیسی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/Futball180TV/104455" target="_blank">📅 18:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104454">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7ecc06eb.mp4?token=oAySrLg2qqjs9IYMM6Lov0MYGfPLrxVxQTirmcC4QiODkxu16fPCrbuc9C2MR0YorXOgnzCYSiZezJp72rGgzQqV4zQsjskLhd0xZtx5_wWU3C01fPYlJBjGBfheJHvxcAdAH3Dj_kwBhgab1EMIImjvZyOPn4P49iIiJ1xDK8924YKmJk2cxTiETxRbvUVhbRWyQrxeChTkNMtPsb6N2TpuiCBXngPkqbjSFBd51QXnj4eTLzoaSqwAEIrMRnxIUlpMlR_zjMGB7f5P3oBBSM-7E0Zy9ih6eP77fF8y_EFzoAhijRLrPQ2RQRvW0b1UrLCSG5yUaY1whUVFucW70AqSeFC4E17hsqCiBC04k7Jue_E1CSJUhE3jUfR-0ARbsnGp2RJRYCpOGpJEXxGtYkXefTt-FVdwDMWxBgXUs8ObXml6agyA6FetD6-AhY59tevFSG3TDxFfL5LRpCOH8FXUyxd5BcopUB5EC3LdsFkWsjCNQVouXIlaTon0jAQoZCeo_pPxr1hkj3CgRc2uCJsQpIcDxS_CB7GdiuErhatbLmlAxR60Ck_9eG1UM6FXo0jHe3qitLkYwUH2hrNqOve2Z43U7O355KD2Hz31ITYv6lRPNW0fcjDu_CYP0uAVAZ2WvAq6Gw_v7EL0fEPUaP95cvfXU0YEXSRE-xbHLyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7ecc06eb.mp4?token=oAySrLg2qqjs9IYMM6Lov0MYGfPLrxVxQTirmcC4QiODkxu16fPCrbuc9C2MR0YorXOgnzCYSiZezJp72rGgzQqV4zQsjskLhd0xZtx5_wWU3C01fPYlJBjGBfheJHvxcAdAH3Dj_kwBhgab1EMIImjvZyOPn4P49iIiJ1xDK8924YKmJk2cxTiETxRbvUVhbRWyQrxeChTkNMtPsb6N2TpuiCBXngPkqbjSFBd51QXnj4eTLzoaSqwAEIrMRnxIUlpMlR_zjMGB7f5P3oBBSM-7E0Zy9ih6eP77fF8y_EFzoAhijRLrPQ2RQRvW0b1UrLCSG5yUaY1whUVFucW70AqSeFC4E17hsqCiBC04k7Jue_E1CSJUhE3jUfR-0ARbsnGp2RJRYCpOGpJEXxGtYkXefTt-FVdwDMWxBgXUs8ObXml6agyA6FetD6-AhY59tevFSG3TDxFfL5LRpCOH8FXUyxd5BcopUB5EC3LdsFkWsjCNQVouXIlaTon0jAQoZCeo_pPxr1hkj3CgRc2uCJsQpIcDxS_CB7GdiuErhatbLmlAxR60Ck_9eG1UM6FXo0jHe3qitLkYwUH2hrNqOve2Z43U7O355KD2Hz31ITYv6lRPNW0fcjDu_CYP0uAVAZ2WvAq6Gw_v7EL0fEPUaP95cvfXU0YEXSRE-xbHLyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
شهربانو منصوریان: برای ما دام گذاشته بودند؛ کاری می کنم ووشوکاران ایران به ترکها ببازند
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/Futball180TV/104454" target="_blank">📅 17:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104453">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/836636a573.mp4?token=lToROset1oJ8wukIJ-nk5Zd4zG_06S11ENBRAlBE5H6akmoWRYxdlCsoG839U2MKQp3DoEIK8ZINJrBkaM7M060pYtnS8INuWVdutpgwoTpbuBoJ667B82cU1Y1o6j-Xuare1A7NPOEHZdyC6b755qMwl8domyyZe0xMJZs0UR11gYr-QcWD89rMDlk6rL5mbXkeCjLdT-GPAso8hwete4NzdV_y6wntVQxGj_n-Ai18WdAxsenAaGUNsBob53rOaoGeERs56wU1NevAcLq0I3xGhxF6Oobvw4DhobTQ7_uPhJhBZGU7YAhyF-f5YVIpwYpoXgNSn3qi7ecGELkOFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/836636a573.mp4?token=lToROset1oJ8wukIJ-nk5Zd4zG_06S11ENBRAlBE5H6akmoWRYxdlCsoG839U2MKQp3DoEIK8ZINJrBkaM7M060pYtnS8INuWVdutpgwoTpbuBoJ667B82cU1Y1o6j-Xuare1A7NPOEHZdyC6b755qMwl8domyyZe0xMJZs0UR11gYr-QcWD89rMDlk6rL5mbXkeCjLdT-GPAso8hwete4NzdV_y6wntVQxGj_n-Ai18WdAxsenAaGUNsBob53rOaoGeERs56wU1NevAcLq0I3xGhxF6Oobvw4DhobTQ7_uPhJhBZGU7YAhyF-f5YVIpwYpoXgNSn3qi7ecGELkOFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟢
سوپرگل ترینکائو ستاره جدید الاهلی عربستان در نخستین بازی شب‌گذشته خودش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/104453" target="_blank">📅 17:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104452">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/653b7ca74c.mp4?token=kHUSfULW0cKBEaJWTTgR28SEq-ZR8GUzxZ2Tnpwqycu2CNAoRPSCEU0J8RVTcPBI89ILPQqfNJf5kgG1lbyx5MMuhk4Tlx15ezgXBqOkneVqkvrs-aCbyFIHHtgc1v1S2CSUlnPICh29T3GPZxucAF80VQ36h5Hkv9WMEYGFZqvDzh8CgkFTc2caGGci0whHgr_pQK8ofg41aipzeK11VgQHPyMhPtA5INMgR4g6vmR5xGKNkZ4IWIAmgJ3KrXLlq56p42zKPIrhRg5CuWicOxTw-kLti--3_8Rqc7gwZwD4kKpqaZFcnWrn6bQVLmWjwnJmWYWrH9ELRTX58C80pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/653b7ca74c.mp4?token=kHUSfULW0cKBEaJWTTgR28SEq-ZR8GUzxZ2Tnpwqycu2CNAoRPSCEU0J8RVTcPBI89ILPQqfNJf5kgG1lbyx5MMuhk4Tlx15ezgXBqOkneVqkvrs-aCbyFIHHtgc1v1S2CSUlnPICh29T3GPZxucAF80VQ36h5Hkv9WMEYGFZqvDzh8CgkFTc2caGGci0whHgr_pQK8ofg41aipzeK11VgQHPyMhPtA5INMgR4g6vmR5xGKNkZ4IWIAmgJ3KrXLlq56p42zKPIrhRg5CuWicOxTw-kLti--3_8Rqc7gwZwD4kKpqaZFcnWrn6bQVLmWjwnJmWYWrH9ELRTX58C80pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤯
🐐
یک ربات انسان‌نمای چینی در جریان مسابقات جهانی ربات‌های انسان‌نما در پکن، مسافت ۱۰۰ متر را در ۹.۳۹ ثانیه طی کرد؛ زمانی سریع‌تر از رکورد جهانی دوی ۱۰۰ متر مردان که در اختیار یوسین بولت است
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/104452" target="_blank">📅 16:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104451">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2308ddcaed.mp4?token=DCfyU0pgf-OFWACOi9etNegfXoCYIEUHsu1CJp3zPtv6nlPPVqj1vfsKWKK1yUmqUo037HnHAkKo9VDdvmQAX1wBotaBackNPMylx9fwTicFGwm4yx4PwmzNeoo83PJpXsaU_xBoiCl3NveMQoFr9a7Otv0xOaL1jKd0WXaOeZiOwB-ANc0D7GKZXt1OYg_mWtI_9se7TZNUVgjSSoIzyoNrNIkD8T57mJq6dqlSIFVI4Bzfzt9FEuXDk0eclYsAunZLnRKNUvQLUrdB4c_3uR1QVkiuG82iRTinF4b-sNSBas6q7bzM1wTgrzX0VzBkh_qBgo6RN6UTJ-Eov78h4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2308ddcaed.mp4?token=DCfyU0pgf-OFWACOi9etNegfXoCYIEUHsu1CJp3zPtv6nlPPVqj1vfsKWKK1yUmqUo037HnHAkKo9VDdvmQAX1wBotaBackNPMylx9fwTicFGwm4yx4PwmzNeoo83PJpXsaU_xBoiCl3NveMQoFr9a7Otv0xOaL1jKd0WXaOeZiOwB-ANc0D7GKZXt1OYg_mWtI_9se7TZNUVgjSSoIzyoNrNIkD8T57mJq6dqlSIFVI4Bzfzt9FEuXDk0eclYsAunZLnRKNUvQLUrdB4c_3uR1QVkiuG82iRTinF4b-sNSBas6q7bzM1wTgrzX0VzBkh_qBgo6RN6UTJ-Eov78h4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
هالند نادان با موهای تراشیده در بازی امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/104451" target="_blank">📅 16:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104450">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da4f666bc.mp4?token=i6Z3cCYtZZGLxYpkBTyDCCoEAtQ4NthnNO-R695XLV6PZuRUvy5HLXs0xA2Qb-Jle7foLu7AW6ZP0AntHwb-4wAnsb2mK-bESyasJE2e0469GFwC6uByuMd4SjSyBpcfYSNb7o3baOzgV3lygBUrHDWYfF0Dph7NAj9xEaBDIFgIaKDH9ts5FjP187nnslnbNnzeyqoddHUwizUeg1KbHYbd96xKdo_x-h1G8OJXFNEGz_um4Cx0E8VDPe2PmS91tLDDuz6CWHZkWC27LNHeUsn3GPwv92EFdS600xCjmc2-jz0EpYNBowwNQ0QQS4rbWAVago_82jdHtkI2LLiCeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da4f666bc.mp4?token=i6Z3cCYtZZGLxYpkBTyDCCoEAtQ4NthnNO-R695XLV6PZuRUvy5HLXs0xA2Qb-Jle7foLu7AW6ZP0AntHwb-4wAnsb2mK-bESyasJE2e0469GFwC6uByuMd4SjSyBpcfYSNb7o3baOzgV3lygBUrHDWYfF0Dph7NAj9xEaBDIFgIaKDH9ts5FjP187nnslnbNnzeyqoddHUwizUeg1KbHYbd96xKdo_x-h1G8OJXFNEGz_um4Cx0E8VDPe2PmS91tLDDuz6CWHZkWC27LNHeUsn3GPwv92EFdS600xCjmc2-jz0EpYNBowwNQ0QQS4rbWAVago_82jdHtkI2LLiCeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیخ‌منصور قشنگ سیتی رو خالی کرد
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/104450" target="_blank">📅 16:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104449">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ynlw_FAcM2ydff496f5UX1G4Rqwd6JEbMgz5M1hkS5QIET35caGNWYy8nuo7rBfMuSKLpgtP8_bU0imS4zJkC-E0ZdsDOT4952sHUXJBBHx3V6wowRV3HPCtVKC-QbuMlJKcQJQHgA4IXPAP20ql-VH4pCrHJt8nsa5qor06K1kTAbPnMn7MdPxjwP-SIq0yH133-2vy_0DKrIeHMWmxIwaRvWCVGRso-2r2CJwIprU5XFvis7TrM4uXGLBVDgW90pIhbe-6VC1dP9pENf5TzICp1GyIMFs4-ih__CIEtU_pIE4e71zPYfDIH0DjKqN8WibrZpWvINTo7lNwS_f1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⚽️
بهترین بازیکنان یازده‌فصل اخیر پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/104449" target="_blank">📅 16:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104448">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87c342598b.mp4?token=qBrpY4AKjcqWziTQ7tGqRuNo0E9LXnAbqsgaYdJ4wdmE5hO18hxvZNDcHi-qsrx1-sG6sSwUs3-TnSiKfZf1XxPYzwmbzsomQ1-hUNBqVAwDdUZkErbJDScodqQ4sUcvc9gdz4urVPSnD54cY6CCBiQ1YfUxbXs1UjXRf8DqAG9ROhR8_yBrH1d5pDnhICKcmIHe8Xf_WGZ7FVfJurrCkdDTQJpdcw8QKZuRQmkUGmX7wJufAlP-8p2bgRVRTe1vU6JcWaiUoQKo0okaRMK-jRBPBu-yAxvRdC26aoktB_8qhFY1MjISVCtday1lzgXqtLGrtLIbRw1eREEDxoBYeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87c342598b.mp4?token=qBrpY4AKjcqWziTQ7tGqRuNo0E9LXnAbqsgaYdJ4wdmE5hO18hxvZNDcHi-qsrx1-sG6sSwUs3-TnSiKfZf1XxPYzwmbzsomQ1-hUNBqVAwDdUZkErbJDScodqQ4sUcvc9gdz4urVPSnD54cY6CCBiQ1YfUxbXs1UjXRf8DqAG9ROhR8_yBrH1d5pDnhICKcmIHe8Xf_WGZ7FVfJurrCkdDTQJpdcw8QKZuRQmkUGmX7wJufAlP-8p2bgRVRTe1vU6JcWaiUoQKo0okaRMK-jRBPBu-yAxvRdC26aoktB_8qhFY1MjISVCtday1lzgXqtLGrtLIbRw1eREEDxoBYeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇳🇱
دومین‌نمایش درخشان ترشتگن در تیم‌آژاکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/104448" target="_blank">📅 15:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104447">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd1e841a3.mp4?token=hFcuyBHKgqVfYR4u18TmiS-tJWFGOXqyGM0L3-5_61KANXqqxXXEvz82kTs4crixOCyjibWxGKEDT1OepvQGf6bnxvq2Vn7adbWUBU2FXWsZagfhVPSaaakKJ9gXr8IAyGl8tOp0--PDLwxJCvII8JDcMSqSjA3Kw5Lfn_CLkM360KaNk7_0BNqngVsgC9PpR7X2179v-8zZKLTu_a2i4qKHSJAq_jvmUn2pcBiT-qxUxk52whP0VV-r0Q9msDolF1pdXNq_ZZHZ74N1BFdPL7IHzeHvu0Lbd_EApwg0MsFuHF-oMHUqNOnDkOEu5dL3IIT6xGuO_jsIn47wQeZ1vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd1e841a3.mp4?token=hFcuyBHKgqVfYR4u18TmiS-tJWFGOXqyGM0L3-5_61KANXqqxXXEvz82kTs4crixOCyjibWxGKEDT1OepvQGf6bnxvq2Vn7adbWUBU2FXWsZagfhVPSaaakKJ9gXr8IAyGl8tOp0--PDLwxJCvII8JDcMSqSjA3Kw5Lfn_CLkM360KaNk7_0BNqngVsgC9PpR7X2179v-8zZKLTu_a2i4qKHSJAq_jvmUn2pcBiT-qxUxk52whP0VV-r0Q9msDolF1pdXNq_ZZHZ74N1BFdPL7IHzeHvu0Lbd_EApwg0MsFuHF-oMHUqNOnDkOEu5dL3IIT6xGuO_jsIn47wQeZ1vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
👀
امیرحسین اصلانیان: در رستوران عابدزاده همبرگر خوردیم؛ غذای احمدرضا رو هم من حساب کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/104447" target="_blank">📅 15:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104446">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d764ecc24.mp4?token=j0a2aWS40_anWajTAwEUsl_rK7YbYjsHNMuIDUv7FkQiURRCG8DHhaXyLNlo3r0Rc114LD2gnf5QT0ID_tEhhpk5C47toI5ZWwaMopldnit82YAAXYaGauOvxBhOiCMr9Q0DSHs4f0eNzAcfN8peYYDaZ0myjIdOXpn-b0UiOVCBjvNMViASzwPhbnOyCPxTJzSLMLTlNQhVsKIIjtNHPcae4ZgfcyuDv_bogg341mdMIwMOsKhn2RHB8oqLUpb6BtV4GeZ_gBEEJpoI6-0JhVD6yL7wa-Djfv7P0xN0aCp6_KefTGRW-0htF7pnbonT-EC6g36Ommxwq51VNUcx0mNAYwGZSUTs8TLTyo-A7Tj9EeS2S6ipm_qElAB6gGdomXBYuRY-DxlDxwJ5ACGRM3XWJKVCPah4ir0ydO9gb3hphRzekQcDo4n2BDoq9O4tDCDWLo5QYD9Zb6MpkEyRtMK8uVeJSxIU9mx4Aa_mzvJiZqsJ6ttgaQZoSAMnDkalNZh6m-6wlfQlkUqvY6T1dV1tSCyZE7W7okvhhNXZXFP7Jbmd56k6PbzvmG5K9SJgOOSGaMUyBYncGSjQd9yIDlyq7CnyVLXsCX2kBRXmGkChGJ_e3uvZXHZDKZokoR_jUjweNFYtCZy2OA_smOZwDNDX8-HEW1Y2weeED8wJivM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d764ecc24.mp4?token=j0a2aWS40_anWajTAwEUsl_rK7YbYjsHNMuIDUv7FkQiURRCG8DHhaXyLNlo3r0Rc114LD2gnf5QT0ID_tEhhpk5C47toI5ZWwaMopldnit82YAAXYaGauOvxBhOiCMr9Q0DSHs4f0eNzAcfN8peYYDaZ0myjIdOXpn-b0UiOVCBjvNMViASzwPhbnOyCPxTJzSLMLTlNQhVsKIIjtNHPcae4ZgfcyuDv_bogg341mdMIwMOsKhn2RHB8oqLUpb6BtV4GeZ_gBEEJpoI6-0JhVD6yL7wa-Djfv7P0xN0aCp6_KefTGRW-0htF7pnbonT-EC6g36Ommxwq51VNUcx0mNAYwGZSUTs8TLTyo-A7Tj9EeS2S6ipm_qElAB6gGdomXBYuRY-DxlDxwJ5ACGRM3XWJKVCPah4ir0ydO9gb3hphRzekQcDo4n2BDoq9O4tDCDWLo5QYD9Zb6MpkEyRtMK8uVeJSxIU9mx4Aa_mzvJiZqsJ6ttgaQZoSAMnDkalNZh6m-6wlfQlkUqvY6T1dV1tSCyZE7W7okvhhNXZXFP7Jbmd56k6PbzvmG5K9SJgOOSGaMUyBYncGSjQd9yIDlyq7CnyVLXsCX2kBRXmGkChGJ_e3uvZXHZDKZokoR_jUjweNFYtCZy2OA_smOZwDNDX8-HEW1Y2weeED8wJivM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
صحبت های مهدی توتونچی در مورد شادی شجاع خلیل زاده مقابل سپاهان اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/104446" target="_blank">📅 14:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104445">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b843ddc780.mp4?token=qwMt9XAV7eK96wjosQ8j_9oZlrY2Y_Yme9RgVDyHuU4cy3DdCL4xT4DfELezuD3LjvEmIdyoOmo1vpxVrHV1TryrkSqnCPZ_VsOgFM3c1_GfWpWrZ66nb80wrO_ZpnvGrpddQgqvX5ZgI4hp3dBMuPHkRLxBQEO9ohSHLY3rOEZEfxHN0vw-uEGjgFYmNnRmo98dqMlwSPieO3KxJBXNqu2VKIRfZCV9ECArpC0yoyGMG1v1QRHHMOi-8s5rpXdKqB9SM44VRf5r8tlRsiiFThhadzVMyn5qsOUpb7ix48UqbPyuAwqiQfMjoJNSnSHvFIOznxlD1UkARW7bo6iFoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b843ddc780.mp4?token=qwMt9XAV7eK96wjosQ8j_9oZlrY2Y_Yme9RgVDyHuU4cy3DdCL4xT4DfELezuD3LjvEmIdyoOmo1vpxVrHV1TryrkSqnCPZ_VsOgFM3c1_GfWpWrZ66nb80wrO_ZpnvGrpddQgqvX5ZgI4hp3dBMuPHkRLxBQEO9ohSHLY3rOEZEfxHN0vw-uEGjgFYmNnRmo98dqMlwSPieO3KxJBXNqu2VKIRfZCV9ECArpC0yoyGMG1v1QRHHMOi-8s5rpXdKqB9SM44VRf5r8tlRsiiFThhadzVMyn5qsOUpb7ix48UqbPyuAwqiQfMjoJNSnSHvFIOznxlD1UkARW7bo6iFoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ناراحتی شدید همسایه ورزشگاه وطنی از شعارهای رکیک هواداران در بازی‌های نساجی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104445" target="_blank">📅 14:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104444">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90391f76b.mp4?token=rplt0aoXnyU5bLqrsPjsBqK4McjV8NeM1-w1eEs27S_JdVu1DqyD0vCGvyY2wBA4Lzbo6p7HtVMf0rq6RWPyobm-vzzMZbgsgqKjV4Z5U_fhu8zAhMgZhvs1sYxHDnGlBF_6SiPMONJu_P-aoxjfZTqIL-DkIZDRsnPMOjstW-cDV4rbEYuH2kf8IEkPdl9rfmJDh82kQQp39cCAqx6_98Fb97DwzzClkX55UFfAJg4Bav9jG7O4b6B0HkknsxwOxkybuQF0hgGJAGkjJrttyl73fkGYrCrZbU5M0_vuO-0jo8MqUEuvXi3NzjMLWTG7HplBSwgh7AZHsphIeyyfGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90391f76b.mp4?token=rplt0aoXnyU5bLqrsPjsBqK4McjV8NeM1-w1eEs27S_JdVu1DqyD0vCGvyY2wBA4Lzbo6p7HtVMf0rq6RWPyobm-vzzMZbgsgqKjV4Z5U_fhu8zAhMgZhvs1sYxHDnGlBF_6SiPMONJu_P-aoxjfZTqIL-DkIZDRsnPMOjstW-cDV4rbEYuH2kf8IEkPdl9rfmJDh82kQQp39cCAqx6_98Fb97DwzzClkX55UFfAJg4Bav9jG7O4b6B0HkknsxwOxkybuQF0hgGJAGkjJrttyl73fkGYrCrZbU5M0_vuO-0jo8MqUEuvXi3NzjMLWTG7HplBSwgh7AZHsphIeyyfGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
اسپانیول، اولین قربانیِ رئالِ مورینیو.
🥶
☠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104444" target="_blank">📅 14:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104443">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a456af91c.mp4?token=CVobrvKm4MGN0rG8YuWFo3Ea3SknFlJmOT7e7He3ag_hCwaCHGCLgQdp83GxMkbBjZe-HqoACFs3MwcE7AfRE9S_LZtUlHSG8EbzHFdA6vJQx_NTxqhhUOgYNu38NhroE82p2dMsMRbTgc64cMPKSU1hzJue5zyvcJkTk-voHDF5s53GLfqmxs-mFLQhjGq32jNPU8v2xKEHtSyuArTv3ZL7bmMMiUDaPKt3g1Mo_1N6sA2xE2fJbvTsLWZuXXs3kbJQZ3ig1PbVs9y-DwxFE2aMJbznxciu9v8HPT5i0NqMqT8NjBQG2okGqJtkqrulVjc_8YfPV7HhklaCiWUY7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a456af91c.mp4?token=CVobrvKm4MGN0rG8YuWFo3Ea3SknFlJmOT7e7He3ag_hCwaCHGCLgQdp83GxMkbBjZe-HqoACFs3MwcE7AfRE9S_LZtUlHSG8EbzHFdA6vJQx_NTxqhhUOgYNu38NhroE82p2dMsMRbTgc64cMPKSU1hzJue5zyvcJkTk-voHDF5s53GLfqmxs-mFLQhjGq32jNPU8v2xKEHtSyuArTv3ZL7bmMMiUDaPKt3g1Mo_1N6sA2xE2fJbvTsLWZuXXs3kbJQZ3ig1PbVs9y-DwxFE2aMJbznxciu9v8HPT5i0NqMqT8NjBQG2okGqJtkqrulVjc_8YfPV7HhklaCiWUY7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
جلوه‌هایی از مسابقه دیشب لیگ‌عربستان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104443" target="_blank">📅 13:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104441">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrF3qRuxtLlV_JXrUXjzEz4sRtTrifTPmhh95UJw-NvYs8RTu6MZ20HENUQZoaCN47lJrGMCO5oU09haLe2y9PLQqqQHKQ5jkmqGVwbTsq6bEt5J-rODw1WpJc-Mbwwc8In9N9MzZz2Xs1DZizuckq75KA-T1HDuTyusps9ydNPIOt6Nf1WD133XjdhXmYAuN4v2KkQYbw9WNPfczPDRl5qDe91uZhr3wX8WljaUUC0jHKRkt_Vb5CAUHc9QY87DuU1sNEyH6JwN-3LbZgDWL33cwAyL6nURqLUvptpBTH_PW_XPMtyxDtXpoTT8d_sdDlXNCgO-hbLiCVrW-p2lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfxXKFoqlhqAHjPZeM1g0sLBI1Qd3X39-28W63L2zqENDt6RVQO_o3SBDoZWdugJPgaMep-G0K785TPmzLpGCMDEomy_FpiU1YMXxp9W0BDsmLpdgoKDQ9iXQmNQsnrUiD8FcPl7IjACP0zkLqdiS2g2-lRxJI6qq6Bj6eTtrXHZ7WT-9u-5qFlcIBrO0x8daSX3YiV2lNYQ05iBqT0TcxzdaIgYsV9BOQCwp7bhQWMzYb8S34Kws0L_Dxc_dXaCqx62oDl5xcWpKYb6WeRqyb7WyXfL73fc5ifGYGDyTaYFJnwe7TmFd0fXMRAEXHwd3mAU1qGM1P-IMoGl_tuKFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیوفیس جدید ارلینگ‌هالند
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104441" target="_blank">📅 13:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104440">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5669817976.mp4?token=ThiDaQuJUVJXWMt9auOR13jpe6E_1xVG4wx6-LcHFKr6Sufpy4uxQl8JL0s-LwcNfeNHuA5pkbu8alvOIBjliMBCUmDJKYydDdxVo9DOTc4HzN-SrTEqK4p3rzBlSe_h7OgT8dC-sPYXhORWce7mX4-XeS6og6TcpS2ttIEx6RFzr2KZRalMC7VpEsfE3v60fvzxS6QS6X9q47DIyVkLpEt1ijiuTe6hh-DP810SJ9j8tOsjLfLeaGvtEhjPbHQdCJcmoqLcNf3wYT9lGbFd4QJVm3IAwOQPyKGdcuIab_Iyvdx72akRYJQUYg7QhQETR7PuHYEvtwzQPgElVHxnMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5669817976.mp4?token=ThiDaQuJUVJXWMt9auOR13jpe6E_1xVG4wx6-LcHFKr6Sufpy4uxQl8JL0s-LwcNfeNHuA5pkbu8alvOIBjliMBCUmDJKYydDdxVo9DOTc4HzN-SrTEqK4p3rzBlSe_h7OgT8dC-sPYXhORWce7mX4-XeS6og6TcpS2ttIEx6RFzr2KZRalMC7VpEsfE3v60fvzxS6QS6X9q47DIyVkLpEt1ijiuTe6hh-DP810SJ9j8tOsjLfLeaGvtEhjPbHQdCJcmoqLcNf3wYT9lGbFd4QJVm3IAwOQPyKGdcuIab_Iyvdx72akRYJQUYg7QhQETR7PuHYEvtwzQPgElVHxnMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
ادعای عجیب و قابل تامل هواداران استقلال که مدعى هستند كه كيفيت پخش بازى هاى استقلال پايين تر از پرسپوليس هست و اين موضوع درحالى مطرح مى شود كه بازى هر دو تيم در يك ساعت مشخص و در يك ورزشگاه بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104440" target="_blank">📅 12:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcwhlQ5kqGu9sNo2pm-cofQ-rm7sZ0Efs3RUXpDFrzasf6Z5EBhrX51_BvtWyxuy1zC2viRHIaH8h-LKI7dsADR9vRvPRYdFRbanH2Mph70VT_QNBSVbDN5-oLnxS4P6w8dYrCQiXes1PnYVEkeai4J-0P0ZdFI8sf66lnEd3Eb03K-Jixm7On72zIdzWgoNwm-hU0AbmHMQ63e640ffJzlo4nq_mAgFtzigC6_pf8rYEvQD2JHVcz1t-z8gjIYgpmOgABvvXeLzgRE1puBh0_MeIzN7Ml4ZbXd8wDhpT9Y4_caLU3xGqEl0osFuCkhwWLX1RzU86-zKFB3EKi2xuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست بازیکنان بارسلونا برای دیدار امشب با الچه بدون حضور بالده و رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104439" target="_blank">📅 12:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104438">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e1a23b0e.mp4?token=ZmwSjfgjWWL6yofMpfeJAMsCM5zR1PCUTk5f0EsRed3bVrMCwn6Jy8mXRZGrTCJfxQlEisluXSxX6Tyfed505QJQFKuQ1qxKjN66b1M1pJhCEM59FxBvTihotPoVgNHI51y7TJ0JfaFv2jw7S3xrK1-GsI65CUAJo4AWetjEKqYBigJ0VNsgAYeWK2cibwRaqGpmoTiaus23NsZmwaqfHCWs5FU3HvOtY2MlJN0NQFqncRABnAMZQ3By1yQa__8beMr4cJGc1IlGhqMWOXPCDT7vTv9Xp23ngV3P2XDL1S4HHWenOiE1XYcMVdYbb6moTW68x18ahKLgi2IKe-9DJXJyvU5wq2wLqEuxky20KrywHcLCWVI9C1gADH3DUdg49Qh1RjpdQJYm7IeekzqUx30P1K9xS0ta1W4RvyhfvNHhzJoh6E3AIlCTFM3J_kLXAjbYL3ppzsHcOAEeI8duLkQb_3zbIy50LFngKZNrYPISflRQPKWV8j5BIo8BOJLAcK0ywZ2d72z3MQRvacD2Gm-JM0V4A0sTPULNLBa9xwyMmhzyDPFbtYKvdQPfcx_mx79zTL9S7AUDuYjKKNpObsMxIrKabknYC0g0EV10O4DOuA9qSTBx-xE5XddQxFfDNuge1MXahPARDKfHQzyjDHpLLaxdu_oiCQ64HH7D2Bo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e1a23b0e.mp4?token=ZmwSjfgjWWL6yofMpfeJAMsCM5zR1PCUTk5f0EsRed3bVrMCwn6Jy8mXRZGrTCJfxQlEisluXSxX6Tyfed505QJQFKuQ1qxKjN66b1M1pJhCEM59FxBvTihotPoVgNHI51y7TJ0JfaFv2jw7S3xrK1-GsI65CUAJo4AWetjEKqYBigJ0VNsgAYeWK2cibwRaqGpmoTiaus23NsZmwaqfHCWs5FU3HvOtY2MlJN0NQFqncRABnAMZQ3By1yQa__8beMr4cJGc1IlGhqMWOXPCDT7vTv9Xp23ngV3P2XDL1S4HHWenOiE1XYcMVdYbb6moTW68x18ahKLgi2IKe-9DJXJyvU5wq2wLqEuxky20KrywHcLCWVI9C1gADH3DUdg49Qh1RjpdQJYm7IeekzqUx30P1K9xS0ta1W4RvyhfvNHhzJoh6E3AIlCTFM3J_kLXAjbYL3ppzsHcOAEeI8duLkQb_3zbIy50LFngKZNrYPISflRQPKWV8j5BIo8BOJLAcK0ywZ2d72z3MQRvacD2Gm-JM0V4A0sTPULNLBa9xwyMmhzyDPFbtYKvdQPfcx_mx79zTL9S7AUDuYjKKNpObsMxIrKabknYC0g0EV10O4DOuA9qSTBx-xE5XddQxFfDNuge1MXahPARDKfHQzyjDHpLLaxdu_oiCQ64HH7D2Bo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
🇮🇷
صحبت‌های زیبا و حرفه‌ای بانوی هوادار ملوان درخصوص شرایط این‌فصل تیمش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104438" target="_blank">📅 12:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104437">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWFRwhgg5j6Vk3GpSyufZn2eSobc7SD8hOX6klcU36ynr8O23m5PMDC7gTJoM4EGmsrhWKIjtoOUut3-r2KtFyY3WKN7xPV_y4w20pgT8nZBUTMzVhmorNnWQPIcOZdxVpi-Zp_w-zxcXL9Sf_aa2FxO0PaBDk2VcGMnCHZfGsfXaiyKTNnmSjjtmj8UJGb-519oFFweYgizN3fqjOOOHDjLRXdATzv7Z4_4vNrHVl3KEvt5gfYOCXmUyCnEFD7UGqxC1Q3dylUiKf9ILXHA275OCoDBgrlGjrEGKMsm8RjkqFiluWFJYYkRTgCSnaX0a40MFu3Lz7m-kJ_hhI7aMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
مدیرعامل فجرسپاسی: به سازمان نظام وظیفه برای جذب علیرضا بیرانوند نامه‌زده‌ایم و اگر‌ مورد موافقت قرار بگیرد، از ابتدای مهر در خدمت سنگربان تیم‌ملی خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104437" target="_blank">📅 12:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1928a613f1.mp4?token=FKSOfVCWO5b256h_Xst6JfIQYZalrLXAgBXLsCjnim9kAnfz1fraR_sAZw6nLlMwITGgJXw-cLoFaa1CWlzj5sQBtxxZ3insXjzbfduD_BaoY0DgY_nuMq-V8c_nQPgkP6pI0mbghMMQ_5bedUNtzCwZz5jZsixctFKoG0HdPoLMOZhN8bA9Lq03a723sgRfp4Ox9Nkk8eKON0czqD2EZit6xiytnL0RoBmXqSiD1B-kk3rEQxki-1WT85Ma3jPi64Jk23BzfwnoiVucE5OLEAbF9hKoXLeIh22IG3OpO_jknVOZwvDH-rEtFQ699IP9K5ipgEC6dr-7S6CIU8F8Fayuu7wHRFteASUrmcMJJCUx4D6i5odZ7bQEoC-tLXuIJiZlnY0oM54oXud3lmXyKjRvBK5tOxmBASCLzwopnHMQkEdX0lvDFTlDADBL-KRAwcan-bYiuWZVTCgBElZlVjFUKMm8iqHECO8fSv4WsSZzikzqjpqM78xO-tyDI_YuZ7XZ3SYSe2uPkFYbw1yMKyy-QZoWMgjo_C_XwolwPqi89hdTJQQiehLHIfOBUEi9MvLVBbitC_8Ap0_CgUgkQ4Rn58pphfnn7rHO2hyCGVqjesKMpaT2tdEerVJ_dhwuNNbj52TZ2EEElLx6t2Js51Tizz8YGLhQFUmMN8SIOKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1928a613f1.mp4?token=FKSOfVCWO5b256h_Xst6JfIQYZalrLXAgBXLsCjnim9kAnfz1fraR_sAZw6nLlMwITGgJXw-cLoFaa1CWlzj5sQBtxxZ3insXjzbfduD_BaoY0DgY_nuMq-V8c_nQPgkP6pI0mbghMMQ_5bedUNtzCwZz5jZsixctFKoG0HdPoLMOZhN8bA9Lq03a723sgRfp4Ox9Nkk8eKON0czqD2EZit6xiytnL0RoBmXqSiD1B-kk3rEQxki-1WT85Ma3jPi64Jk23BzfwnoiVucE5OLEAbF9hKoXLeIh22IG3OpO_jknVOZwvDH-rEtFQ699IP9K5ipgEC6dr-7S6CIU8F8Fayuu7wHRFteASUrmcMJJCUx4D6i5odZ7bQEoC-tLXuIJiZlnY0oM54oXud3lmXyKjRvBK5tOxmBASCLzwopnHMQkEdX0lvDFTlDADBL-KRAwcan-bYiuWZVTCgBElZlVjFUKMm8iqHECO8fSv4WsSZzikzqjpqM78xO-tyDI_YuZ7XZ3SYSe2uPkFYbw1yMKyy-QZoWMgjo_C_XwolwPqi89hdTJQQiehLHIfOBUEi9MvLVBbitC_8Ap0_CgUgkQ4Rn58pphfnn7rHO2hyCGVqjesKMpaT2tdEerVJ_dhwuNNbj52TZ2EEElLx6t2Js51Tizz8YGLhQFUmMN8SIOKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
خاطره شنیدنی حسن‌روشن پیشکسوت استقلال از دربی معروف شش‌تایی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104436" target="_blank">📅 11:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d84a4cfcf4.mp4?token=TZBlYY-gn0N8rTuhiBJ-jyfFGdE2PBR0g_kK7CF1OXSV0r9f9rPvllt_iIVt7M7eLVZe9uunrXpDpQAUcVJ3OSBJr20ZMk2DIZTbgDzthsA_fFJ8gK_Ow862aIJzvUCadYhssmy97l3686ygOqbqjMyZTLzc-DDjVxh7qqdLt1Qs6EKn6--_a_wLSeQGdMfufDsQHP5PCayZmWilEKq9-aFDytq39pzvtQJtZm2aiJF8-gNFkUZU804SjmhWgoVm9JH5wWx6ZDcVvs-aiGlTxvQhn87L29JieGj7n9B2uT_w_M_RGVmmgzftRi3KY2VwOjCYtAeZq5pwSpbjRsOPvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d84a4cfcf4.mp4?token=TZBlYY-gn0N8rTuhiBJ-jyfFGdE2PBR0g_kK7CF1OXSV0r9f9rPvllt_iIVt7M7eLVZe9uunrXpDpQAUcVJ3OSBJr20ZMk2DIZTbgDzthsA_fFJ8gK_Ow862aIJzvUCadYhssmy97l3686ygOqbqjMyZTLzc-DDjVxh7qqdLt1Qs6EKn6--_a_wLSeQGdMfufDsQHP5PCayZmWilEKq9-aFDytq39pzvtQJtZm2aiJF8-gNFkUZU804SjmhWgoVm9JH5wWx6ZDcVvs-aiGlTxvQhn87L29JieGj7n9B2uT_w_M_RGVmmgzftRi3KY2VwOjCYtAeZq5pwSpbjRsOPvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
کافه‌های مردم پلمب، بساط لاکچری بابک زنجانی پهن؛ عدالت یعنی
پشم!
در حالی که کافه‌های ساعدی‌نیا به‌طور کامل بسته شده‌اند، بابک زنجانی، مفسد اقتصادی حکومتی، شب گذشته یکی از لاکچری‌ترین کافه‌های تهران را با عنوان «VIP» افتتاح کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104435" target="_blank">📅 11:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ff1QydhtxWKsrEWo8XN3J0l0nfROwQiY6lBaVr_Ubm8s55PQ_EHuI9w-qKDY1ZRYRUtv4is36HrZhRti08Bzk7aHo7XZp2ijYqBivPZLilFqn93unC-qWg3mBh96YiltZfn7kgL81xtwm4XtSYKrDK0J96eFdgKpVvAKRN0b1dEAB2CCp1V6HWe_B0x3ONT187U0Dg3aBb5eAKvFgEzdiCAtjhs9RuWB6eFei2Xny9IdYLcyBjT298EEhxDeg-n-7rvxVthm2MeJ0x1CKHx7ATuQSBK2JmRwIiaAoPrJouVJM7ngNQWsVWvYByrHDErPS9SQnrWkTbbm42XsyuY1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
مصدومیت وحشتناک چادی‌ریاد بازیکن کریستال‌پالاس در بازی دیروز که فصل براش تموم شد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104434" target="_blank">📅 11:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if3pLbPNZHfrS77APPTGE0auNu_K7B1ZLVqgSV_ND9zJ4pmw1nJoJBgHO40LA2I8Up4u19fSLCn_O8LCpyqakboRyml5ML6IjaS4iWP8M9YDCnzbWHJPHZmk7aaDRIHYCmhO4kH3Ncfesea2-Irlyp_IZeH7YtilOoUQQbiJDIUsErhX8CF9chtKIaFRQ28sVAVpFvI6x-Ytpntgdor4dHwWer9zJ1M-wo4aXYsmVDqrnN_8PAfvy9EL-_ug0gF6a7IfZAYnZJHsYhcSQXIIukogcCOJr77Gs0w6yZyD8RSe37GHp1hUa1BImPXKZ46i8-d4Ptv7GBjchvh4hPIIAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
باشگاه استقلال با انتشار پوستری برای بازی با سپاهان نوشت: نبردی از جنس اصالت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104433" target="_blank">📅 11:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104432">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7773a1e510.mp4?token=odzuFcyF_eZ5A1N0k6NNnuefz83LaMOGJElwP3SOsR1hCBYkmcAeaDNKGzvM5eTnWDVMinrM8yS_4QFPCQh9H7ULb-0sN0fmK-GSKkMTPjbJzxFL_k1eH09va1F-1JCzWEvy26M1hOMeYrbLTZwpqVijmDR17WWiBVS3iOQe03JE83j_O0qHYWtQE8fo8rjBOifkLP6frQCv8gwO3Vv1oAhIcTW8HzaX7iVnhDfPwiEzWXoZxxI1dKmIKDJDEMO1sjdhCe1vYfWhhbkOC3QmU9XWC_KO1indMS70qmW4OkL5f7PerOdb09LdawdRQk-TMEmrhb0heVqmiDu8_y25yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7773a1e510.mp4?token=odzuFcyF_eZ5A1N0k6NNnuefz83LaMOGJElwP3SOsR1hCBYkmcAeaDNKGzvM5eTnWDVMinrM8yS_4QFPCQh9H7ULb-0sN0fmK-GSKkMTPjbJzxFL_k1eH09va1F-1JCzWEvy26M1hOMeYrbLTZwpqVijmDR17WWiBVS3iOQe03JE83j_O0qHYWtQE8fo8rjBOifkLP6frQCv8gwO3Vv1oAhIcTW8HzaX7iVnhDfPwiEzWXoZxxI1dKmIKDJDEMO1sjdhCe1vYfWhhbkOC3QmU9XWC_KO1indMS70qmW4OkL5f7PerOdb09LdawdRQk-TMEmrhb0heVqmiDu8_y25yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کریک بعد از شکست 2-0 مقابل هال سیتی:
این فقط یک بازیه، می‌دونید، فقط یک بازیه. اولین بازی فصله. خب به اندازه کافی ناامیدکننده هست و دردناکه، معلومه که هست. ولی فقط یک بازیه، پس یهو مسیر همه‌چی رو عوض نمی‌کنه، کل مسیرِ حرکت تیم یا باشگاه رو تغییر نمیده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104432" target="_blank">📅 11:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104431" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/104431" target="_blank">📅 11:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104430">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HptiEVJ3nRS-2-6FZBrab_3sq91lZem1h7zYGVv73L_TA8mDaLEwocG-U1hODfrGnLQd6ltSV2zQ_9QHXJTux6SZH4USheTQOISotIeWZgaVVWPEdaFiU1CSnO5D2iY7arB4jISmxx-dy2TBoKuxGtfyDDIAwFeuQfUgrgdYDHFb6FwL8S5xrs0uC27PMd8XjenZlMao56B4EJmj_7ueHt2E9xT3j8gCU5loDrGprYXoaGqHM2sLLXKXMXo7EXHlSD7zDM75bDBqNQ1uH5nawz6I9snQ7XO5ZRcuP6jkSQKZiyWgudOGo4Xmvl9EW2MH3ePuUhfn_dmP-LLtIGqJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r1
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/104430" target="_blank">📅 11:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104428">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c490b878e2.mp4?token=hxyncpddpCIXFBNLXzQq37rMN2B7668QtXs0jz18U8pzS69FN-Zc6WZwbDKANtuMcR2P2R4QfVcMP5sC296rFL850ojZdCtfk9DVMxmMW8pUEH9AMi-TCFWlysiddgYgMO035dqiCR0On5--AcoybI0wum337dRMCtJkpwd1dYP8k8yWT5ZaDDNu272aeHFhAcuQx2eI04_b-e3Pl4-1zfYQABjOLC-qRLc__TtNc-kHJbg5YKuvDYpe6xJrrRVzDh3Ma-H56WaS08uewcLrDs0P52XGjg8jZju2h7cYnmmcOuAvE5rqN88S5kUIyidOA28AjMgWtbSxAFlzL4-Htg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c490b878e2.mp4?token=hxyncpddpCIXFBNLXzQq37rMN2B7668QtXs0jz18U8pzS69FN-Zc6WZwbDKANtuMcR2P2R4QfVcMP5sC296rFL850ojZdCtfk9DVMxmMW8pUEH9AMi-TCFWlysiddgYgMO035dqiCR0On5--AcoybI0wum337dRMCtJkpwd1dYP8k8yWT5ZaDDNu272aeHFhAcuQx2eI04_b-e3Pl4-1zfYQABjOLC-qRLc__TtNc-kHJbg5YKuvDYpe6xJrrRVzDh3Ma-H56WaS08uewcLrDs0P52XGjg8jZju2h7cYnmmcOuAvE5rqN88S5kUIyidOA28AjMgWtbSxAFlzL4-Htg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
خبرنگار: رئال مادرید ژوزه مورینیو رو چطور ارزیابی میکنید؟⁣
🇪🇸
هانسی فلیک: امروز با رئال مادرید بازی داریم؟! در مورد الچه سوال کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104428" target="_blank">📅 10:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104427">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c2144e6b.mp4?token=e8icDRuEAKm2TicwqHcsOfpP38ZY6jBP2MKvZbmJrX0uATth2z8h539XWd3jIg8TvszxF9MYLM3UJrjfZ9Q8WlK-31QqaUaf2CXqEhZM2KiNadGfM2pqsxTpab5N2dNHzfKtRRenLCWwJK4wCgbvIm2JHA6JK5IBwOFNbue2AZ_DfpsdTV0k-Q-ik4mRd4-7OUxI0A7Dp1z30zw9uMZh2iWvHki8ZKPKA58xinNYNU9Hfr60t3N9MZwDTIyysHOQ5kKVtfuWX93jIr_x1IicL0armFSz6NmwNAsjBfB8n8ri1M0LHgKNz-KErhSpUpxo0LONH-w8PGZoasVTqrRkqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c2144e6b.mp4?token=e8icDRuEAKm2TicwqHcsOfpP38ZY6jBP2MKvZbmJrX0uATth2z8h539XWd3jIg8TvszxF9MYLM3UJrjfZ9Q8WlK-31QqaUaf2CXqEhZM2KiNadGfM2pqsxTpab5N2dNHzfKtRRenLCWwJK4wCgbvIm2JHA6JK5IBwOFNbue2AZ_DfpsdTV0k-Q-ik4mRd4-7OUxI0A7Dp1z30zw9uMZh2iWvHki8ZKPKA58xinNYNU9Hfr60t3N9MZwDTIyysHOQ5kKVtfuWX93jIr_x1IicL0armFSz6NmwNAsjBfB8n8ri1M0LHgKNz-KErhSpUpxo0LONH-w8PGZoasVTqrRkqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برونو فرناندز بعد از شکست 2-0 مقابل هال سیتی: "همون اشتباهاتی که فصل قبل تو هر بازی بیرون از خانه انجام می‌دادیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104427" target="_blank">📅 10:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104426">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👀
💥
پسر رونالدو هم راه پدر رو خوب ادامه میده و در زدن ضربه‌پنالتی استاد شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104426" target="_blank">📅 09:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104425">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f6325ec27.mp4?token=vrJvFBUwb3YXbC0qUlSgfuEWINSNJ-jtAdZDxDfAmWkMfPbN6iDeNfXgPXEY-a9ANAqjTysoCJZdzmsqJnd37tRudc290eY1Urw9iHM6wHOaebroPu7DuKXYcnxRNYJ6V0DtLu3JD5qbd1ulE2MOVbp2czjITPM0weJDOlqiQm6uN-d4XLzIh5rfqzzfdkET2Ykfdb5bXbizP9-ev18CY7F_M51NvBzpaML8nBnrN4ErTOwxe2OKU5MJ6mfRUZqlRhpVArBeAQ9YwU2hYmsPqD3Q6cH0kBfZOLWcpxAWVJwjYX7Rd1Ll-0O6oa4-mcT1DpVUFOQrexdGauapeVi-1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f6325ec27.mp4?token=vrJvFBUwb3YXbC0qUlSgfuEWINSNJ-jtAdZDxDfAmWkMfPbN6iDeNfXgPXEY-a9ANAqjTysoCJZdzmsqJnd37tRudc290eY1Urw9iHM6wHOaebroPu7DuKXYcnxRNYJ6V0DtLu3JD5qbd1ulE2MOVbp2czjITPM0weJDOlqiQm6uN-d4XLzIh5rfqzzfdkET2Ykfdb5bXbizP9-ev18CY7F_M51NvBzpaML8nBnrN4ErTOwxe2OKU5MJ6mfRUZqlRhpVArBeAQ9YwU2hYmsPqD3Q6cH0kBfZOLWcpxAWVJwjYX7Rd1Ll-0O6oa4-mcT1DpVUFOQrexdGauapeVi-1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی‌ساعاتی‌پیش لیونل‌مسی در شب باخت‌ مجدد تیمش اینترمیامی مقابل تورنتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104425" target="_blank">📅 09:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104424">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995ef211fc.mp4?token=BMFWZjObKZ4u0FzSgFxnThgae7_G2lwNMLepqCVvp9PAAyg9eB8QeCaI3MRmj9UD8z13e9ou8I--mWIsWDTPNf2jJCpTw7efZavn3btoHWGd0-HPPcXI2qME4qJ50iouX22kLKCswNkCFJlywOwGX4AUCKm7ZD0fCXtayuvZhcj4tT9zRE17I7R_MSisMSP7qFG43aEQQ_PlXC7jo9xIid_1LNZm4rh1qfvNSQbFsn_O_wauVeJ_DkFVY2bIkuUaL3cLshhdsVHRGdyGZNZvvFa0Q3hMGBfCCqIdu0_HT6BDN1QTEiZZqoSXeysDHNaG9eNKXbKELm6NuQ1oPocUlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995ef211fc.mp4?token=BMFWZjObKZ4u0FzSgFxnThgae7_G2lwNMLepqCVvp9PAAyg9eB8QeCaI3MRmj9UD8z13e9ou8I--mWIsWDTPNf2jJCpTw7efZavn3btoHWGd0-HPPcXI2qME4qJ50iouX22kLKCswNkCFJlywOwGX4AUCKm7ZD0fCXtayuvZhcj4tT9zRE17I7R_MSisMSP7qFG43aEQQ_PlXC7jo9xIid_1LNZm4rh1qfvNSQbFsn_O_wauVeJ_DkFVY2bIkuUaL3cLshhdsVHRGdyGZNZvvFa0Q3hMGBfCCqIdu0_HT6BDN1QTEiZZqoSXeysDHNaG9eNKXbKELm6NuQ1oPocUlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
جنجال‌علیرضا کوشکی مقابل نساجی که باعث نیمکت‌نشین شدنش جلو سپاهان شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104424" target="_blank">📅 09:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104423">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
‼️
⚠️
رئیس مجلس عراق: قالیباف توی جلسه گفت خلیج فارس منم حرفشو قطع کردم گفتم خلیج عربی درسته، دوباره این کارو تکرار کرد و منم دوباره گفتم خلیج عربی درسته. قالیباف در واکنش بهم گفت مشکلی نیست شما اسم خودتونو دارید ماهم اسم خودمونو!
رئیس جمهور عراق هم گفت چطوره بگیم خلیج اسلامی که مشکلی بینمون پیش نیاد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/104423" target="_blank">📅 02:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104422">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qj8LtqIlxWHTPo4X178LPktTRNEUujg-4QkQmTmWgM4YBKle9wpVtWViuIGHN2chWIFn9tCg4Z_RazwQhxxjs8x4GdSGLPlcmZbaUuPLigTo8i1gbsjALnOy8qQds0mRuPeANCz2lxUzDGCnK0bTr9fg4dD1O67VcGW40d9q-onMCO3e8DiraQC1VxgqjJnEOCCzPuNTF1iIoED8Z0G5_qfQZvnV6ypC7Z62XW9MViu6TRywp8lh9WsJ_1hEJmZ-V0rffB80tViE_pQetW77-rk0fW2xGqbs7_pn3mCPa1pGS0Py-T9PZ-am2rWsazvTpLPFprUwmwwuge_93DyiGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی در ترکیب اینترمیامی مقابل تورنتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/104422" target="_blank">📅 02:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104421">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPTFxZCnNEeAYxCo6sfQg6fMAGxun--VnEXSe6paQcqzgwuIzUoczbxEmY1k2i-wWRHS9S4ufqcn0Q4ikKPbowtWINr3AjiXIhVtKRx_oer_yjhIFBTAmHjLG3y4Yr0tbcNvf4o8jGbxE44v1O3g585fs5LzrBMI7kzQuJ5B9eeyw94_N3c6E_FiyhGHzn4QgoOOBHZtgrxxEu6QQGNOr-tK2x7vTnD3EzG8fHPIIubHSngQl5yQlo40r_aucGmNV1jc7kf7R96uSk33ea5PA0xIkbMac9daSt-CYi_RTt9rLyKEMJxNhkteh22riQ-Ocz83X7evoASjLYLKVSpOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
‼️
🇪🇸
صفحه باشگاه اسپانیول در کنایه به قضاوت داوری بازی با رئال‌مادرید:  ‏" چند بار باید خطا کنید تا یک کارت زرد بگیرید؟ این سوال رو از طرف یه دوست مطرح می‌کنیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/104421" target="_blank">📅 01:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104420">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8znfux4qOm7bBgmi6srqnL6bwDqmLpKpXkQC5UpvqNQLkzKPSepQnMfTIXcbaGh-xwBSTLaZe4kA44ca0sA7TeSuAVTbb-YEJLCYrKWLPUnU37sB-OoR42sFRiHnUC_6SmKBvoQurDJRvSga9Xu_4e3lf7dHP-RaDKs3CrEp2-eyHR3TRSWSEVWKrnSbSRWN2X8n43qZQKwJSt0Wp5Ff2lkIEa3wJusj-ILQvlT33NAhHcxG3nVbViley2Ab5K8EtiB618yBMUv28zjRUTXypmN3B0L8NkMnjUn9CFQiQ45Ae5pbPNrHNflzrAx3DFOUHnmUM16isyejEdf41FfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
‼️
🇪🇸
صفحه باشگاه اسپانیول در کنایه به قضاوت داوری بازی با رئال‌مادرید:
‏" چند بار باید خطا کنید تا یک کارت زرد بگیرید؟ این سوال رو از طرف یه دوست مطرح می‌کنیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/104420" target="_blank">📅 01:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104419">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIte8e1z5aJp9ggRDx24N-NGotkUjn5dbhDWGe95UFO5PZcRctdJRvVRfybSHPMmalinqROwc5MubXArWhj-FhWJfyyhsafADSybMZQzSXVB9IX3LlIc3GdNf4xDPBpnOQV0n1yq2kCz_unvjq0EoveRn7REG8TiVFUqoChrbelJfiI2fDBYboByF1GdCex2JquqA9AFvZcsQLm1lyRsLAd-YGcuXdJG9J8N2UTXF2_v_1twHAw06TZrcoaT-3u5amnT-YhJBRYjMvBL1sKilvTh2xHorfT0ONzGZV1o3tb5_4AHxuPcRA_iEacxKLCp__UysXaYngj1gbs3ZZv7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
👀
نجات‌دهنده ژوزه در قلب بارسلون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/104419" target="_blank">📅 01:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104418">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktxcl9FDkMFyHEfN4PeXsizNa1T1C4Mo3T6WiNIn4k1F59a8l3KFcJlnHcvEkogcI2o_s9D_sywt-Ac3rsibpDShZ1WUL94ah_USnA9B3sJlBFmGGMWR-N930EUKaYMpzlFeKzlN6WXAIV6mnLEknqTDrPy1KLd1G03XcyNKeYO8gXgyiWM0Da9ECR6Xr2l7D_R1gHKNMcjhU-VSlAfhVRql1JYiVIIP1tnzefYNZrskKda1hl87Cb6KQswbPhyBJNHoiks1N82A1VwwnDKN4OLHEs-8D6cuzOBm44S_F8GYoa9fvbEWFST5gnDadAyAv8tQJScl2_LOTxYL0TCvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
⚽️
گل کارلوس اسپی در دقیقه 89 و 54 ثانیه.
🔥
ریال مادرید با به ثمر رساندن گلی پس از دقیقه 90، برای دومین بار در تاریخ خود، در یک بازی افتتاحیه از لیگ اسپانیا به پیروزی رسید.
🗓
پیش از این، این دستاورد در 21 آگوست 1999 در مایورکا، با به ثمر رسیدن گل تعیین‌کننده رائول در دقیقه 90+3، حاصل شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104418" target="_blank">📅 01:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104417">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">💎
میدونستین تو دربی بت
✅
با شارژ بالاتر از ۱۰۰ دلار ۱۲۰٪ بیشتر حسابتون شارژ میشه
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104417" target="_blank">📅 01:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104416">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/104416" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر D
erby Bet
✅
✅
✅
✅
واریز و برداشت ارزی و ریالی
‼️
✅
بونوس 120% اولین واریز
‼️
✅
بونوس برای 4 واریز اول
‼️
🎁
بونوس ورزشی هر شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🎁
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a31
✔
@DerbyBetOfficial</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104416" target="_blank">📅 01:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104415">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cd1_bJKDcz_yvbbUWqjLxiRKm24XC9dU_sBeheeSgTa8GWKkLxF-4XvR38kGRMmHzRj4g2pqETPgrLuOzb5vom6M2wO_s2aTODdfEzkr7TRHG_B9FAG_KhxJXl7ezbRGUny6G4JS5uIJ9Ltnj-qlmJuolGIfYdaO6L9115Tb1GFqpHG4cXXilNGCsMT9mHJyYVt5Nhw9cKYMEET9IdQBytDgedHJrT2TF-I7qUEx-1ICfjEKNgk8p9OXg1YwzFMEDGo8jx7w2gXWvy8LDE-S7KpwbNkN3PW203AFx5z4nH93v0tmDdTOBl46P0mIpUOkfYt60C5QuRDeRqCOo1NI6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104415" target="_blank">📅 01:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104414">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYbrjm5ozjoCd08Lhq3I__dX7WrfuW2EdXGRn4yhVyw78BdDlzbhIbmib7B3qwjUNI1qYV0Mtuo1iGRV9gUq2VgtltwgW1I2nMFn0-oWR9P7wIssTQAZjCaJ21ybmFazo1bLxrST7BMBvbbX-2KI_QxjTSzbf7ESKjx9f5PUW1t1u9zffUTF32wT75aHGOhD_xqp6TBVaGdRscLsgVyZtA7Pe13q22uY8uo54ulLJMReZjZdEVSoqJMsxZl9yIGWZ8yqtEIvAcQka9lUfduXeIUsMKJsq042OUA5Z1rpxuC1_vVOh5MZ1-TKaFDZ3nrbfChiHbsbGdoSTtLklnvTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
هفته‌دوم لالیگا؛ پیروزی سخت و نفس‌گیر کهکشانی‌ها در خارج از خانه؛ مقاومت اسپانیول با گل یک بازیکن کمتر شناخته شده شکست!
🇪🇸
رئال‌مادرید
😀
-
😃
اسپانیول
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104414" target="_blank">📅 00:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104413">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/69ada12902.mp4?token=ZqzQOO1Vt1fVjAqR9N4jJ0Yj-NaaVtUEwx1-jk15y8TY6Q1Dj4SHShza4txsG5LYkdcnggUOsgnkWr0m63IwCJptP20L1hvzJfBXEAPZLJsC13HycPY-4Bw0GuolCPz6Xs01n2e8UnQa27oo0aK9WGTc6yqpzZjmxmuMsg1fybitZUC21GFHIXZMsufboVDWrqzVBxr1tIplB6KX2o737YGfa_RlX4wfchZQMS_zyYVFJ8IJZXktNvtklpZBNyWhCeUBXXOlF9e_7EOAEDy_v7hb4uWqTOpw0dVEAT4hhPowGgWdJOIs49JySZ8KjWJuJaRAOj2E915IbQNwAfqAJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/69ada12902.mp4?token=ZqzQOO1Vt1fVjAqR9N4jJ0Yj-NaaVtUEwx1-jk15y8TY6Q1Dj4SHShza4txsG5LYkdcnggUOsgnkWr0m63IwCJptP20L1hvzJfBXEAPZLJsC13HycPY-4Bw0GuolCPz6Xs01n2e8UnQa27oo0aK9WGTc6yqpzZjmxmuMsg1fybitZUC21GFHIXZMsufboVDWrqzVBxr1tIplB6KX2o737YGfa_RlX4wfchZQMS_zyYVFJ8IJZXktNvtklpZBNyWhCeUBXXOlF9e_7EOAEDy_v7hb4uWqTOpw0dVEAT4hhPowGgWdJOIs49JySZ8KjWJuJaRAOj2E915IbQNwAfqAJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
گلگلگلگلگگلگلگلگلگلل رررررررئاااااال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104413" target="_blank">📅 00:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104412">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اسپیییییییییی زددددددذذ
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104412" target="_blank">📅 00:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104411">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رئاااااالل دومیووووووو زددددددذ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104411" target="_blank">📅 00:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104410">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104410" target="_blank">📅 00:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104409">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">▶️
🇩🇪
🇩🇪
هایلایت دیدار دورتموند 1-2 بایرن مونیخ با گزارش روح الله مدرسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104409" target="_blank">📅 00:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104408">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIQTZS7rvthPg4gAfEirAiTpZvq8Ju0q2vLmVXqbqtLOsyWSKeLhLN3kuiUNg9p549ihFVUkPhJPuhm_H6m5VwJwr1yYw6RJAVVX872Y8W9oPT9Kj4PlZbOec5CUd_t0UU2NLtK27WhkjBELhv8v0N7nkJFSqO55dRfzIfAnuGoB4y-HUEiqvxMWWFFCpljzyBf74Toxl05QCwp_F82xjhOTSHdypsWgZtwTnym9VEjG7WI4OYu6x7W-b4bb_zS2oKxOcDYyYGvB5IPcZZeVv0qzDpco6fCyRAelH4kZvKaoKoYFted-_kf6ox5wPQJTzmPkOdw4JTiKVZLlui2ayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇸🇦
رسمی؛ داروین نونیز مهاجم الهلال با قراردادی قرضی به الدرعیه عربستان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104408" target="_blank">📅 00:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104407">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RP1lzsuv_-IIMTHuL6Q9DpyhjBlmevr7eHftRw84XzSvWnYxk2KyyKgkuoghpkpL9KRqSfos1HJWzfIIlslnpvHYeKnI9sflr_fv49mWLipCYgitzXscQYvAwh0LZlltSp_n1OdEHYDdqUhLhBdsfkuglj6Az4hE0AXU01KMZmQ3xO4ButibkbrrAfbjPypr3i7CKlBnWR7PWgYqGkit8kWwnPfKVl_9Drnc-IWw0JFJy8GETtSjezFd3I_gobdynRwWO_T-M0AjcdN8KlqMpAkbpbA1WBhY7Iv5E39o606foR1b_gMvDC-YlAyH7FKsrIkx-ti05WGTLkDmwclu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇩🇪
سوپرکاپ فوتبال آلمان؛ بایرن کمپانی اولین جام فصل را از رقیب سنتی گرفت؛ دورتمند بازهم مقابل باواریایی‌ها ناکام ماند
🇩🇪
بایرن‌مونیخ
😀
-
😃
دورتمند
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104407" target="_blank">📅 23:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104406">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/06034109f1.mp4?token=X6BzSsVBRaQlL0RhfDVWoVFFssDI2PApsKEyTju084Zv7uU-094GGC48-SwSIvYHppw9f1c2qmKmshMEXneCOMTuOtXjdeQJjQTEby1v5hyZ0jL55gXg5D56jSb76lc-WvLJXw3jv4dlegCpkI1PI7lUTDBl9k4G8D3HOj3lnKycSldHgB1YPZoE8_XmrJ7Mmw9C1p4_bYVE_8zirCyCv0x4n8jbKjlDrEFB3ydMnVv1chToQk6JzeI36jz_xHPutTXYVwnBHKgs9SjnWUOEinxUTRrUBlW2Mby7SY2cyF4ldfu6SbcHpx_Km5MOiwyC-uJQYdWUEgCRU3wG1gANVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/06034109f1.mp4?token=X6BzSsVBRaQlL0RhfDVWoVFFssDI2PApsKEyTju084Zv7uU-094GGC48-SwSIvYHppw9f1c2qmKmshMEXneCOMTuOtXjdeQJjQTEby1v5hyZ0jL55gXg5D56jSb76lc-WvLJXw3jv4dlegCpkI1PI7lUTDBl9k4G8D3HOj3lnKycSldHgB1YPZoE8_XmrJ7Mmw9C1p4_bYVE_8zirCyCv0x4n8jbKjlDrEFB3ydMnVv1chToQk6JzeI36jz_xHPutTXYVwnBHKgs9SjnWUOEinxUTRrUBlW2Mby7SY2cyF4ldfu6SbcHpx_Km5MOiwyC-uJQYdWUEgCRU3wG1gANVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇩🇪
گل‌اول دورتمند به بایرن‌مونیخ توسط سیلوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104406" target="_blank">📅 23:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104405">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1aebcbb396.mp4?token=pnZHBmI3nxrsK3cqwHdvMchzi2zPiqbgmEZ2XZ3P1pvrJX4ArzQKRZ6KX_IDAqIDpN6G3e7qqsyNop5FUewGkCNHqcIgvl6nrvQfHNMcFlqKIaC-Vi45eMdfkb2IjAbXPv5hxqxzENIoiJCrc0kAyJ8FRoDaf9sbK18C99BuHiTBs-6hnw_u7Cjza9AlxkKE3dxWdG064lRWz-ZWaVYizsJFTlJlxnknjoDmGUw5q8gSN7WKsdkGfo0iM0ZmBYJKcTqY7B9VTW75rgq8sB0FydSytIQwCaLvBre0weaYFvfMLZPeg0CHPx7pfF4s-GQ4Oaef2a8afLVcJClArX0Iow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1aebcbb396.mp4?token=pnZHBmI3nxrsK3cqwHdvMchzi2zPiqbgmEZ2XZ3P1pvrJX4ArzQKRZ6KX_IDAqIDpN6G3e7qqsyNop5FUewGkCNHqcIgvl6nrvQfHNMcFlqKIaC-Vi45eMdfkb2IjAbXPv5hxqxzENIoiJCrc0kAyJ8FRoDaf9sbK18C99BuHiTBs-6hnw_u7Cjza9AlxkKE3dxWdG064lRWz-ZWaVYizsJFTlJlxnknjoDmGUw5q8gSN7WKsdkGfo0iM0ZmBYJKcTqY7B9VTW75rgq8sB0FydSytIQwCaLvBre0weaYFvfMLZPeg0CHPx7pfF4s-GQ4Oaef2a8afLVcJClArX0Iow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
گل تساوی اسپانیول به رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104405" target="_blank">📅 23:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104404">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI-n4Vownr_hcsImjDCXScQSdQnLzVWFjiWbN-t3TgTnR8vvNn_c1A79OO4hOfnMkIWm558uOe9CqP720OeyN9BqU9YajMaVpvXkS1vklXRYadW3efdx8TDWz2PV-gsAb10knQzS4JYrJRtYBfzTcG62gEhBb3BUMxnDTx44UZeetrYLU_8fe3t8XZXzp2s0xmDTdNZVlv4Bme1vXZMthrVZx1EUssNzCgk08RaFjSJts8HYl6vqaq1i61kN8GZsn-bDfIii7tLlKqeOk24DKtAUKNANk3d4JRN7u7g9KCisdQC234lO1U5N1EID6dgdDpANFf1XwnTl0cpqbOIZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🚑
هویسن بنده‌خدا اوف شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104404" target="_blank">📅 23:27 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104403">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64261a7aea.mp4?token=rDiKSpxg7R5FFgI-juTUq49EH5itPUVg0in4Q-BY12aSnyMr9W_mzRwVYjOzgEi17wzJa9S5mgD_RLRpu8LYfFl4dS3HBnBxxXf0T1-EUOrn83XkEPMcvwKSx2Xky0UxKYkFG0E0IEbwSPBpPDGyBRz45v2jfQcjg9SkXFG3zL5Shvyt059N4xFCHQqktthsAF_nN86sk9cV0P0NHw047ZQEZZaLIEqb23VtjyzdDToblTy7Z8XMpjQt1rB_B2JhPtcGYw3GXw49D1qdGeXKO3mgJ_Rx1KLY26X_u06Er03Ct65RrOIPS_YLUMgCQpkWZktj-DDGE2y7KZwrX3qrWA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64261a7aea.mp4?token=rDiKSpxg7R5FFgI-juTUq49EH5itPUVg0in4Q-BY12aSnyMr9W_mzRwVYjOzgEi17wzJa9S5mgD_RLRpu8LYfFl4dS3HBnBxxXf0T1-EUOrn83XkEPMcvwKSx2Xky0UxKYkFG0E0IEbwSPBpPDGyBRz45v2jfQcjg9SkXFG3zL5Shvyt059N4xFCHQqktthsAF_nN86sk9cV0P0NHw047ZQEZZaLIEqb23VtjyzdDToblTy7Z8XMpjQt1rB_B2JhPtcGYw3GXw49D1qdGeXKO3mgJ_Rx1KLY26X_u06Er03Ct65RrOIPS_YLUMgCQpkWZktj-DDGE2y7KZwrX3qrWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇪🇸
گل‌اول رئال‌مادرید توسط جود بِلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104403" target="_blank">📅 23:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104402">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96a06aa961.mp4?token=rv-lWjc6f_7mM6bXTsy5k4lHtNN-DbUhsH-q5PNWNolEX9FeKXkIBawAf7-PE4V91fa2LXUGTRk7wxVGv1k1Fpbjs42TnlmnkTmlIxJ8RonI7mq08Am1uKoWPdOWdxlKTImOohQ-udyw77BW08Livkrey-m-ZddNW6KMNar6BxgL3WhwFjywClJltmU994xJ71zaFubxjlzGitwa_v2cZoIl_pqoZ0ktr0fiOUWwbjlbz9rWhdeS6ppxiP-68SaghvRurXcVkrv5WhebJP4s6hpUGkSM9NjuZ3LzKyd_3xkjPauorGbmuIZoD1lMK527QVtFZnttQ_ZlrWqHdKj_nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96a06aa961.mp4?token=rv-lWjc6f_7mM6bXTsy5k4lHtNN-DbUhsH-q5PNWNolEX9FeKXkIBawAf7-PE4V91fa2LXUGTRk7wxVGv1k1Fpbjs42TnlmnkTmlIxJ8RonI7mq08Am1uKoWPdOWdxlKTImOohQ-udyw77BW08Livkrey-m-ZddNW6KMNar6BxgL3WhwFjywClJltmU994xJ71zaFubxjlzGitwa_v2cZoIl_pqoZ0ktr0fiOUWwbjlbz9rWhdeS6ppxiP-68SaghvRurXcVkrv5WhebJP4s6hpUGkSM9NjuZ3LzKyd_3xkjPauorGbmuIZoD1lMK527QVtFZnttQ_ZlrWqHdKj_nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇩🇪
گل‌دوم بایرن‌مونیخ توسط مایکل‌اولیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104402" target="_blank">📅 22:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104401">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2962887cc1.mp4?token=pf6Kx79spGrdk1sNrpmWoO0hH_QVUJWZJk5sUOBqbbT-AY5CKog4Swq1R5M5OC-LK_i96EvauOmex73VAzfKVa922oj8EZkTaJy5Wpo52k-cnH6Yr09EHAPDknwJQojdtC-zu-drNI9Fi12ArXLHZrEfoJzamdk-2uwjHqKaBnUHNf5PgDFz8atZnUBgnWYGS_Ku-DjTbzgeZubZP3C2wDLAQTS6j4AupngyxgHqqVysAp1H7Ovs86uZuCuba6vErwWl3i_L0I0Fjd6CSzaCSjqmk1R7Zgp1NoCjiDmsRrz-w0oqkp7cgUOVqp5H4oa-BREtw5MHHXGUblAL4JmYEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2962887cc1.mp4?token=pf6Kx79spGrdk1sNrpmWoO0hH_QVUJWZJk5sUOBqbbT-AY5CKog4Swq1R5M5OC-LK_i96EvauOmex73VAzfKVa922oj8EZkTaJy5Wpo52k-cnH6Yr09EHAPDknwJQojdtC-zu-drNI9Fi12ArXLHZrEfoJzamdk-2uwjHqKaBnUHNf5PgDFz8atZnUBgnWYGS_Ku-DjTbzgeZubZP3C2wDLAQTS6j4AupngyxgHqqVysAp1H7Ovs86uZuCuba6vErwWl3i_L0I0Fjd6CSzaCSjqmk1R7Zgp1NoCjiDmsRrz-w0oqkp7cgUOVqp5H4oa-BREtw5MHHXGUblAL4JmYEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇩🇪
گل‌اول بایرن‌مونیخ به دورتمند توسط برون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104401" target="_blank">📅 22:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104400">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1145503d.mp4?token=H9fD3xrS9vDsGZEj_YsL5u5JsEQX5h07e0CTxQ7ZCNRoFC6JxZnqR0vdIAFHH8qHEqc2hbXXbOjoa0A7ao2tfI6OMGFXTu8B-WoavLDZq3Hoah_8YlVDjhJZ0WN2VRHCSluuICFfy_-P7B2qZcZV7pHY_sh6tnQ9-e2lZPjqwH60v2owYt8KNfUDAOOza7AFpAN56GenTR_qt5NvVoDD1oj1NRg2lAQCgi2d2I-JuMvs62jl-orDciCG7n2zkIMeu0Lms487GHeI3qzW69MoBTx9d69Ykpvxr_PqqrHdTkJ60mJHnRZ2qOqeZ1KGDRTZRJxhURYLRA_F2V-SFuISUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1145503d.mp4?token=H9fD3xrS9vDsGZEj_YsL5u5JsEQX5h07e0CTxQ7ZCNRoFC6JxZnqR0vdIAFHH8qHEqc2hbXXbOjoa0A7ao2tfI6OMGFXTu8B-WoavLDZq3Hoah_8YlVDjhJZ0WN2VRHCSluuICFfy_-P7B2qZcZV7pHY_sh6tnQ9-e2lZPjqwH60v2owYt8KNfUDAOOza7AFpAN56GenTR_qt5NvVoDD1oj1NRg2lAQCgi2d2I-JuMvs62jl-orDciCG7n2zkIMeu0Lms487GHeI3qzW69MoBTx9d69Ykpvxr_PqqrHdTkJ60mJHnRZ2qOqeZ1KGDRTZRJxhURYLRA_F2V-SFuISUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🔴
علی قلی‌زاده: امیدوارم سال آینده در پرسپولیس باشم
💬
فصل گذشته تمام کارهای انتقال من به پرسپولیس انجام شده بود اما ناگهان ورق برگشت/ باشگاه لخ‌پوزنان امروز یک‌رقم می‌خواست و فردا رقم رضایت‌نامه را افزایش می‌داد/ به هرحال این ماجراها بین باشگاه‌ها طبیعی است/ امیدوارم سال آینده در پرسپولیس حضور داشته باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104400" target="_blank">📅 22:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104399">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8yz5H6oUWZKolgQpvLvSsQsPanMwFFNCx6oFKin0JLY7XqQzGbqtapBWhTmD9r75ag8_NivnQI_tzR8fHyyDhc6ShqEEXp02Tk6SULmdAKnHhnfQ28AUZhWZIYqg_IJ8khmoAerntTLwchoCdZgujXBQFzCtYwYb6LMrv0y_U3kpQC_0tGQkmq6JfFos1zB5ux2ikWEKlA4tSLHVqG4T249SrGIDyKK0LA63ksU6dqgB59ipRWB5LXSIwhq7qwL2kAHLF-C0qQV8extGcxk836DvYoUMv5IG_8xPL65Hf93-iguyXAoyCp61h5lKEHXHgxiUsdgRyCyjSt1-ZQrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
رومانو: فابینیو به ترابوزان‌اسپور
HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104399" target="_blank">📅 22:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104398">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d7144def.mp4?token=B2970oZBbPusszyXiQ4HdRtweb3AIvdCZatCuwfBdDHGOu6XJ6nI0shP0tpWaDHaUICoO9udJmepMwBY_cmAw4w4pNHvBFfOr8r6XDUdq8gA7kYgAD6aCdaXTZS_USh6EGAF81bYTlsT_oYHLdcRdS3BB6bQ7XvtEdD1JsYWvfPT7qhMgudWGKR226J009KhZPhWyhoQzt8iF905NobGvghB_9hfgrwIgbJf_czLPGo4Zguwgvxqdrw9kUWvgKbPnAKJxdyqYQw6bSOUDMI6j5d9eJZA-9aRgLtT52eC-U9qjFbC5HLCylVa92-k_Oc3ufdOGTwVf39mfIFo9E9QDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d7144def.mp4?token=B2970oZBbPusszyXiQ4HdRtweb3AIvdCZatCuwfBdDHGOu6XJ6nI0shP0tpWaDHaUICoO9udJmepMwBY_cmAw4w4pNHvBFfOr8r6XDUdq8gA7kYgAD6aCdaXTZS_USh6EGAF81bYTlsT_oYHLdcRdS3BB6bQ7XvtEdD1JsYWvfPT7qhMgudWGKR226J009KhZPhWyhoQzt8iF905NobGvghB_9hfgrwIgbJf_czLPGo4Zguwgvxqdrw9kUWvgKbPnAKJxdyqYQw6bSOUDMI6j5d9eJZA-9aRgLtT52eC-U9qjFbC5HLCylVa92-k_Oc3ufdOGTwVf39mfIFo9E9QDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤯
🔥
🔥
🔥
سوپرگل تام بالارد بازیکن بریستول سیتی به بیرمنگام
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104398" target="_blank">📅 22:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104397">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nc7vuFu5bRSk9yjEZKTfNVdMESzpk3I2eJCJUmYoXEKVQwt452T4nb__B4GM0qZnm0Lmk5j2hB6nPjyRKDB0JwwrdXYmPNux_QKXduwQDQxEh2fk-WuaC4E08NY0_mR3tGH03GFcmk-ucvslCAitbYbDsM6fPOFhqin2B4WszpdHDfabBG_PNCqWTs1bJjXvPm7aN-9aJe9M34yEHl1uATWPHL4S9Q0jOOJtcyx3s329ox-V6eqIged4dQgI3mKydxHDsuVeAN-wY8un8sALuvQli2Tx6RVHclji_ixpSQ_gFZ0rCMymO5HZvxeFsZ4yRw2eEx5UX5surj2weN4Y1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌دوم لالیگا؛ ترکیب رئال‌مادرید مقابل اسپانیول؛ ساعت ۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104397" target="_blank">📅 21:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104396">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6JkBcYMcETTqyDwFUgS67Mfg9ff-m7RyQDvmqi3aRc7KXNTHYXIUEHyGEJDP6-MdPkfEpx9WA6WqgVvUXnwSjAaqGnWin0Y0xnPAy5c56C3oLmnBRkg0Aj9csGY0zw3kZjCzchUylMLRrf0IWQmmHYpCSIz47P99YqE2kGUF6dXCvmO5_teJ10oFbXCxYrOoj4NOHXn73YoksftD0TtJjKxlWm3zJAcDJDv40Vi7l94o3R7Nbu9W7FceuevKtxksSKuhyBn4WOza2ED9nm6O0bNCGM0inER3ZGFjjyMyGDa631DS0xUoT5TBNbBLxJ6zVwjY87KhR295nOr2JLZKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌دوم لالیگا؛ ترکیب رئال‌مادرید مقابل اسپانیول؛ ساعت ۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104396" target="_blank">📅 21:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104395">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usDS8M-ieiWb6EGifjBzggAo677Cvwhao8Lm1mzfnQJKtyt72tKAZDQjhe2xnlaqhW7xBOh58ZwZSlRK0zFU2bmfvTfdTSMIvPElsfBW-ZkQIOwYbbLayX4zZawtfI1LSI2Mr0_ZAi7yricMV0Jd4657lCKcy82f5Fba--RTZ_NKEXtxHgNmbS7tI4e_pvrhOK7DfCgRbNxDDxwYB8G9FQCq2ZZm3r4s3l5Zi0Q3JUAo5kwjb7-ysJaa8lPzXLwAFfX5TKBn2iazJLiSlfELfiMtK6HXbqS6VK-WuV_M24Wesnkq8whfiG3QlPLPhoeJu08UsKLaoj33nC-1B02-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
خولیان آلوارز در لیست اتلتیکومادرید برای بازی فرداشب مقابل ویارئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104395" target="_blank">📅 21:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104394">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dauRg_y5b7HDAQggnknT_bEvN68lrFhXHQ_Zqor6B5WiA9oxALVV158rmLjgwnqwVR76QQfCDBHz2JW3hcPrmoaw_mMkfLLISwJdmGjhVUDV8CgDd57h8e7igzsnWkKCLouv6OSNkFvJirSV_YcY2dCgQrXZX_U9F7Q7iuWi2TX4MVkVZ_iJ2sopvqG2jKlLiVFqHet4B9fUL6VgOHhJYDjblBIt6C9wI1NNOvW622mfaiZF4zWW12zBq1wau1VK2X1gT3Ap9zucKaTsSBBmsy1CuF7rnu8-XjF7I28qAeWLmxfTh3AIqeh4D4L_hp9jY3lLGrid1etTkStZvRYKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آخر و عاقبت تیمی که مربیش کصشر باشه و با ۳۰۰ میلیون یورو هزینه بازم بگا میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104394" target="_blank">📅 21:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104393">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOSQov7Qdt0SLYZHgyJaNBMLxNAkYE9DfGrIA4jI64uqNgGad1vcl2Ym0pTL1AtCexh38hoSA7p2fOnTAdKOCQdUF96g42iMw7_otiwEs4nypwxH0xFYCuyIizSL7_kMWltpdv46wXll2UFFmzQhA4gXjrdY0bZX3lnuLyfKW1dW4WOnJ9TS-PvT6iAHUX_5LbEisv_IBYBWUG81VHOjGOvvKngIaJteUNN6U3Xs0RHxIL5bz3Vx6l75wJUmHAW4RzxNIb9Y6pdCiHUSxLG8n5xhINJxSnSm-7UjF6wJqeYrvDYWIozleEwEDim_lbpzt28qPlV46FFtzuN1G-WlDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
سوپرجام آلمان؛ ترکیب دورتموند مقابل بایرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104393" target="_blank">📅 21:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104392">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lz9qAKRApH_PfkxtZgbYEz6Pl3IWQLr7XVNaGjoHYNthKLLcrrq2jZ6FtRmL9aUOgCB4LxDrDIRv3CqnTgAdYgsNuiQj_XUwaFXulsB_W-apBcVkr_CiYr1a_GKGn8vMeORKoKfA12GXrI33wEq7zY62SHRIazLvCmXTmAvIU4h31BG7t98Vd5WmAeLyEEcGlmWVntUhWbzlvWzRLVCUPZFTF7aK9-IitV1pI_ercDcBfORlOUDguwon-aU0_CmdYrfQfytXNSyQn7SJMdQk-kDDZqbPlkKtQdNtUHVtX0tkLDHgFEc1Z53drQOOL26FHmCLCAT3UoU0GjTB191Gxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
سوپرجام آلمان؛ ترکیب دورتموند مقابل بایرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104392" target="_blank">📅 20:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104391">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f25fa8009.mp4?token=K0NtIVz-5quC4vXCplkFSIcEIvmhklHvOd-rYTiOHz6sMe0fd0LEBMMAPWT-QnrjvQpe5kdF6pcV261cGGNy3zL28nrxFQnqOznFz-Sk1QjEdKsz3M6Xs_IHTSqVMIABBecHZ626EKo3GYs0ub_SMHEbQOvEL5O4TpbYmzKhLD-D47RQUUI0weYOXJllGy8SmfYGZDW5Y_nkyGZTUqsPkkki5PFhdtM9ee55FyzTFIZ4aDEsByxQ5cnW26vSfDGLkG2vLbDTexScCJ3nOK7zZIAjffMW8ZdLpW33yC5Y01Ufx3QDMNemH58DSP64TJTiDy5U2ZZBA35fFzPBhJN4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f25fa8009.mp4?token=K0NtIVz-5quC4vXCplkFSIcEIvmhklHvOd-rYTiOHz6sMe0fd0LEBMMAPWT-QnrjvQpe5kdF6pcV261cGGNy3zL28nrxFQnqOznFz-Sk1QjEdKsz3M6Xs_IHTSqVMIABBecHZ626EKo3GYs0ub_SMHEbQOvEL5O4TpbYmzKhLD-D47RQUUI0weYOXJllGy8SmfYGZDW5Y_nkyGZTUqsPkkki5PFhdtM9ee55FyzTFIZ4aDEsByxQ5cnW26vSfDGLkG2vLbDTexScCJ3nOK7zZIAjffMW8ZdLpW33yC5Y01Ufx3QDMNemH58DSP64TJTiDy5U2ZZBA35fFzPBhJN4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این حرفای گواردیولا رو گوش بدید و عمل کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104391" target="_blank">📅 20:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104390">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4ecEwD6StIrpt8XbFP8B90Tjl_ICBd715USYqAW3Bgksc8Y4jminaWS3edJ38BGuS6A_NvJgK4oJBEnMS6Z06AWShNRYWGmBhOgrqsocvnoyJ6VXMdinzLuIj5sN2qfm7RY6wj7UQW9DkGaktl-4XDAFpkJ25NmHMBdiEhFk03JVnEMwEJJaqNdfEPiKwAy-kbN_j7hdu8YFT77wv-EDEP958bcXhumhfOvYrT3MT_ZC4RPqnM4JKES28ACQAvNT2B_87S9fYEz3XxOsz5Xe8wfaetWhGMwvqvsdN9SZ7_bPeNzwQzHdbq0PTeGzPM37iXN7JxCPIenCnj5vpI2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇺
لژیونرهای ایرانی حاضر در اروپا:
🇳🇱
علیرضا جهانبخش: اکسلسیور هلند
🇵🇱
الهیار صیادمنش و علی قلی‌زاده: لخ پوزنان لهستان
🇷🇺
محمدجواد حسین‌نژاد: دینامو ماخاچ‌قلعه روسیه
🇧🇾
میلاد محمدی: ویتبسک بلاروس
🇷🇺
نادر محمدی: دسته دو روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104390" target="_blank">📅 20:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104389">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dba53081a0.mp4?token=TF9IDxiP17tmsWHqboxy458IbR5COptOP0VwlAT7Ib4YTM2vA0_Cpne1bREZzdyBx6-dM6j4i-FiDK-9Jksi3RWXmiCdjICa4UegMd7SktoJT3Q_BT3siEXn6_rbSG5n9tq6jU3q4QCm4XhA5VRxZQT-nks7NBy2PEGwEqNaDl6xgXGTQ-cGIMHc3vKEzswQGVcTji4XMZ5DIiTgMkAxE7Sf6ujmDp4p5_HuwNplkB3J_LxEtlh_4WSOOBy5Apgg3JYIPqbQP_Ay7ydRZOZUSnpVqjfGlXKVSopwqhLLIQb4f6ZJ5QihUTwkOZ7G1Hv0evf7K93TChzLrni7Yz-Mng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dba53081a0.mp4?token=TF9IDxiP17tmsWHqboxy458IbR5COptOP0VwlAT7Ib4YTM2vA0_Cpne1bREZzdyBx6-dM6j4i-FiDK-9Jksi3RWXmiCdjICa4UegMd7SktoJT3Q_BT3siEXn6_rbSG5n9tq6jU3q4QCm4XhA5VRxZQT-nks7NBy2PEGwEqNaDl6xgXGTQ-cGIMHc3vKEzswQGVcTji4XMZ5DIiTgMkAxE7Sf6ujmDp4p5_HuwNplkB3J_LxEtlh_4WSOOBy5Apgg3JYIPqbQP_Ay7ydRZOZUSnpVqjfGlXKVSopwqhLLIQb4f6ZJ5QihUTwkOZ7G1Hv0evf7K93TChzLrni7Yz-Mng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🇮🇷
حمایت جانانه بهتاش فریبا عضو کمیته پیشکسوتان استقلال از رامین رضاییان: این‌که چه‌قدر پول بخواهد حق طبیعی اوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104389" target="_blank">📅 19:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104388">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2fde5e301.mp4?token=HsKb2LX7zQqMXMbNk78KmW3TSNjuhXJz4BcARFEJsLczam7jp-tcdosyw4tT8M7t3AjHXpCsSc6KwYME6lA664lxGjJ72gyrWqS6Zm0VnUTDkXaCmTVbWTkJsFujVw-MF3_ogoP5cfh6t0aoPyB5DP8rs3ldXjA3K4hTnppDcqLuujZWRcLCqJpND2wAfDTcOAm-T-WeGbn2xMWMzYZwoyNdYqi0vQ2rqnxjGqFNWCD6s64R6w1j-zRf7iu7HWOjtF5XZIAhu8w80HIvuBqCcPcHOJLjRG1Ka9RgwNITBCc6EDR3UDN24QwLwquef6maEUTFN96crmDB71vAWgLOfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2fde5e301.mp4?token=HsKb2LX7zQqMXMbNk78KmW3TSNjuhXJz4BcARFEJsLczam7jp-tcdosyw4tT8M7t3AjHXpCsSc6KwYME6lA664lxGjJ72gyrWqS6Zm0VnUTDkXaCmTVbWTkJsFujVw-MF3_ogoP5cfh6t0aoPyB5DP8rs3ldXjA3K4hTnppDcqLuujZWRcLCqJpND2wAfDTcOAm-T-WeGbn2xMWMzYZwoyNdYqi0vQ2rqnxjGqFNWCD6s64R6w1j-zRf7iu7HWOjtF5XZIAhu8w80HIvuBqCcPcHOJLjRG1Ka9RgwNITBCc6EDR3UDN24QwLwquef6maEUTFN96crmDB71vAWgLOfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عملکرد ریدمان محمد صلاح در بازی اولش در ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104388" target="_blank">📅 19:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104387">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8Tv2_H2UCTyv0LIpCRFwHdC0vhKed2a3uui8TJQTWQrhRJ6S7r0I4uB-xxz7ZhHhsnlSwGlbUtTWRVNYmEpS7sQKXgE1AuQfBEy7RZ_1DKlEJeynwkPZlf3-9mD4BIymqi4yxys5_rtvToN4ONc6gWy4WpD6LGD8yFq8PvpIu_bZuS0GzHZWrJeyX3f5R_GFUsngcEo51ZZwhINr71S1LPiKwQuA9lLpTeQzCfY-_2qUiMGkzKbDGleX15Ylb3Dz0FfcdsYilhvcrF1aR8r2EGnMAQAJImL6WKKYUBZc10DxuyGmIvPjIcR7tVN7zMMh2QVM4f5MkzaLBomDwB30Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته دوم لالیگا اسپانیا
🇪🇸
اسپانیول
🆚
رئال مادرید
🇪🇸
⏰
ساعت ۲۳:۰۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ ‌‌بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104387" target="_blank">📅 19:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104386">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d02a0a5f.mp4?token=Kyd3UPhllcQ6DZzc66D4N76n1mR_PhXtFphqE7Y3YvUL8_9Azm80xU7t_oGn3T3JuU6FP_WO1D69U_mBdI9CPmRG5PoqNO6eMeiN_5MeltgWs6mXHw0KM5XKKDj_AYge3E-49QmNp7dJD_LxHGJJsIaAmNc_T0AEb2AD1-vaS_rixz6uGjS3lQJdm04xqJEMcdNqsDGGbyN9lF7Z74nqfP-kyYm8O1N2XJh0xKGAAs-0ncy1AJMhOk5KVzxjU0M5MbyDqCZMSLyJ86df3lYuIil_apmmNLGuK-fA5Fbp7G-cAKLslRF9iUFxEafv-QAXr_2QgAOL2B9_1v9EZQGghQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d02a0a5f.mp4?token=Kyd3UPhllcQ6DZzc66D4N76n1mR_PhXtFphqE7Y3YvUL8_9Azm80xU7t_oGn3T3JuU6FP_WO1D69U_mBdI9CPmRG5PoqNO6eMeiN_5MeltgWs6mXHw0KM5XKKDj_AYge3E-49QmNp7dJD_LxHGJJsIaAmNc_T0AEb2AD1-vaS_rixz6uGjS3lQJdm04xqJEMcdNqsDGGbyN9lF7Z74nqfP-kyYm8O1N2XJh0xKGAAs-0ncy1AJMhOk5KVzxjU0M5MbyDqCZMSLyJ86df3lYuIil_apmmNLGuK-fA5Fbp7G-cAKLslRF9iUFxEafv-QAXr_2QgAOL2B9_1v9EZQGghQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اقدام زیبا و تحسین‌برانگیز بازیکنان اولسان کره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104386" target="_blank">📅 19:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104385">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jPhRCUC4XGer8FmoasxreSHQ9JEeIy3WBHBoZd8kpAguvYwRzOHfJUB2IQWGssGgiUTJ8Gnx67jBmbijvN2-q9BDmth57tppOMdZ6y3Z63mdSMejQ7ysGCTWy50I8ksXhg4D0uJbZ3SJOh38D-61Mds4pnj0bOsxB9rFhFAmctf_lQbfAyduQVbhOo6XW6vuerZPh_DIW41U_LYzcF-D69hksgJZdT88nRX_1qGJu-95SQ1bZEpxIdvS4w5ZM-ans214XGUgRKcN9_35qno7EUfwIylhdykNRR_CC1pSIOZBZmerSzd4DIAziBZ5JZjl7tb5QStC3KjlCgXVqiGiow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🇪🇸
#فوووووری
از رئیس باشگاه اینتر: بهتر است بارسلونا خیال جذب لائوتارو را از سرش بیرون کند چون هیچ راهی برای فروش این بازیکن وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104385" target="_blank">📅 19:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104384">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33114edb2.mp4?token=oIKcqvTzumlREsDsGJjpQCYIjZ8Hgepl71GgzCgfNm9EnnSHjEUOQMrDOdpM2QrbGEUhpP_WPu4Q8276XavPVsT0ROHqbK56zISYBJDdDom3oio2hG0awIc3gR8kH-W_ZVEcxIVLImF4kq6gTjsYNFcTxMkm9nTnfeCUjS-TzEj3aDtVwSmBZrBUVi0yK0c81rI5J0dEmbcjbiKiPa4Do0TTJ9IsY8ykVycuRSp8tBBCoAIbqBUCdnJ863JXnqcv5t2P1MTd2m7nmNMeSKRI1hh2MGXeHou0PLiIq4sfEw_YqWsVbq8TsLMRTmPrexv0YfWDUkEYxLsY3dS48aqi7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33114edb2.mp4?token=oIKcqvTzumlREsDsGJjpQCYIjZ8Hgepl71GgzCgfNm9EnnSHjEUOQMrDOdpM2QrbGEUhpP_WPu4Q8276XavPVsT0ROHqbK56zISYBJDdDom3oio2hG0awIc3gR8kH-W_ZVEcxIVLImF4kq6gTjsYNFcTxMkm9nTnfeCUjS-TzEj3aDtVwSmBZrBUVi0yK0c81rI5J0dEmbcjbiKiPa4Do0TTJ9IsY8ykVycuRSp8tBBCoAIbqBUCdnJ863JXnqcv5t2P1MTd2m7nmNMeSKRI1hh2MGXeHou0PLiIq4sfEw_YqWsVbq8TsLMRTmPrexv0YfWDUkEYxLsY3dS48aqi7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل‌تماشایی ساندرلند در مقابل ایپسویچ
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104384" target="_blank">📅 19:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104383">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRK8wjT8-pPjhXexoOU98rtM5QRy633m_eGqJRR3-vcRYuib6GxXNhMii2EwALjpbZZKKC6pYY8vsf5JjAl-k9PINHerRXhX76u5Picf7YZUcIgPMYcMmPc4_9JhkEQBl_Glvt1egc0qcNlfiLyQyx5zREHO1sZ2wmBJ7qd85_vTFgq3xM94fIXiXfJApjbjm4MC7Gffc8O8SABRxyUE8TY-E7swZz_lsCMWaXASXV_Am6BEAopKSA_pm1LtRqTrwMcUnmnCAfYGwsYZy6JKlfbFwAQn8SFxLawQ9vwo5oU4Z67bZ_5lJmhIQephGnDcba4fchwT_8Vw8i2Qh0DvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: دو تیم شهر منچستر به جذب بالده بازیکن بارسلونا علاقه‌مند هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104383" target="_blank">📅 19:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104382">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qa1Ic87UsLqDvNyRdquVZsstkQeiW69Y4nuLnd34vUKzAk_TrhmgMUupu8JsK-Tuzltxs4bChq6WDFQxOMMQ96KsFBW5dg6hlCXPIjZnZ1GDanVDg-mtSXrjVyHNFZvsx7C27fFRLy5yYgi1E6yuN3izL8G0Fp9fpJLLS7DbGOUzd5Pv9j_R0A15PkxNTSR6n6xdn0p8gIh4mlse-JrCRLtmnh8mVzMseWtpt_76NO3wu_vyykj95ydt4WE-LbJbkQDTFTcHzoNaVye7gpS9HrnjztORIjP4f3GYBSoFPCXw7rQXFOKK6dmVE0YSaLshR1b3poB2biDFynC2IK55Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته‌اول سری‌آ؛ ترکیب اینتر مقابل مونزا؛ 20:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104382" target="_blank">📅 19:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104381">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45250f7e28.mp4?token=TwgGsxBhJ5ZPH7Wc0Ic2ASca-buZXtQGkHNofQRpPQWt1w-jEcFaI1A4qhQ25b2L9SultKKlPLk3kdzs-rzSC1QcG1600dW_hrzumQxtkrOSnlGbHBJ-Xxzi66zmGQ9jRPd83h9Q3MtREIDJX728j4mb5g1hcQB7yPhK6JM3cQnOQaaq19cyRlsXBxFXcmfr5OjSV7TVjeI3IZRR-CMXyht0sU_pjMy0S-3vXSI_B3M5AQ763TACImD0ZKI4AI-MnoqyDdK5YgTiI6gnWNU8TiaC5F6nOL-i_m9K9LDiB363J4AYHKD6CHhwmJntwWIk6O5z0giB3AmOLn_smf8Lmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45250f7e28.mp4?token=TwgGsxBhJ5ZPH7Wc0Ic2ASca-buZXtQGkHNofQRpPQWt1w-jEcFaI1A4qhQ25b2L9SultKKlPLk3kdzs-rzSC1QcG1600dW_hrzumQxtkrOSnlGbHBJ-Xxzi66zmGQ9jRPd83h9Q3MtREIDJX728j4mb5g1hcQB7yPhK6JM3cQnOQaaq19cyRlsXBxFXcmfr5OjSV7TVjeI3IZRR-CMXyht0sU_pjMy0S-3vXSI_B3M5AQ763TACImD0ZKI4AI-MnoqyDdK5YgTiI6gnWNU8TiaC5F6nOL-i_m9K9LDiB363J4AYHKD6CHhwmJntwWIk6O5z0giB3AmOLn_smf8Lmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
فوتبال روان سپاهان محرم نویدکیا که با چاشنی بدشانسی همراه است...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104381" target="_blank">📅 19:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104380">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
⚽
@Tipster_Mafiaa
@Tipster_Mafiaa
⚽
@Tipster_Mafiaa
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/104380" target="_blank">📅 19:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104379">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗧𝗶𝗽𝘀𝘁𝗲𝗿 | 𝗠𝗮𝗳𝗶𝗮</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqE5MdOyZDNu-tby-dFZtop_pY1tprfagLgloey5iXHJe88uRPn7RYdz5x2gU0IjGMmOnPHFvmSrdK9Fwo6ixserc5WBKQES2nVGiWYdmowgjpmBM-2jvYYXaywEi25y7XAWUhDlSIAsuXioWVtHD_79quytq8HR1scKYA906DmK1JFFNHooTpBYmp6vh5oEs31Q7o69-ZbcELpgXb1tLi2sEAdI2IKdnemGUxrars-5gaHExMpOef87jI5b3CcMYZliEF7plvG5hQSZxmGCDpM6f5360cePkvdvRKfjkFBYla1jvkKbqMrDVa0QanNyy8m12Kk-rnBWDzLrWSMy6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104379" target="_blank">📅 19:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104378">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b7ad297b.mp4?token=sTyzqR7S8h05cp2Ga5TqKNQpaucIgygxU9Ek8Erg_gAfwSz4IXTjtuBGHng8L06bE6OwTzXpv_OKBkmir6zXbs8tnDR_-cAHgIG-t3UXUDeRC4dDTGiHx5LNcPRfEm4BYAIT_a0-kAqJjXDBi5w-wQarxYpbE7EGqOw146cH2Hw-RgqyYc2RkBt_GPDPhwb6KMFMoeo7mXSpQYkk0mjTuX2Gujzea_bGOVGCMnGiNLEo8taxkh6tbN-9q0fGgLrukiAYVZCKdMm5Xr2RDxPZRPxoloYCYEDcf7TmMLN6GC2cx-jQ4luUWRtKHbGw_TLhkJOk1gKNzFNZx5JW7fdnYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b7ad297b.mp4?token=sTyzqR7S8h05cp2Ga5TqKNQpaucIgygxU9Ek8Erg_gAfwSz4IXTjtuBGHng8L06bE6OwTzXpv_OKBkmir6zXbs8tnDR_-cAHgIG-t3UXUDeRC4dDTGiHx5LNcPRfEm4BYAIT_a0-kAqJjXDBi5w-wQarxYpbE7EGqOw146cH2Hw-RgqyYc2RkBt_GPDPhwb6KMFMoeo7mXSpQYkk0mjTuX2Gujzea_bGOVGCMnGiNLEo8taxkh6tbN-9q0fGgLrukiAYVZCKdMm5Xr2RDxPZRPxoloYCYEDcf7TmMLN6GC2cx-jQ4luUWRtKHbGw_TLhkJOk1gKNzFNZx5JW7fdnYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
هیچوقت این صدای تاریخی استاد مرتضی فنونی‌زاده از ذهن و خاطرات پاک‌نمیشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104378" target="_blank">📅 19:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104377">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVuZ-WmlMIfA47_4pNG3BM9gmWZ30vBEK4x2QuFTv7CKukXmQQ625ONadQgJK5KdVn5mPUbvKqaykdeElQ73vWJHEDQDnmNxapI38cI5OhGyPyblFiLvUH0nxkSvktCmWVsBqHI10Ua5cRsy-kHKY__-wwmdc8mTtkNGZOhKuzT-1OWCR7AxxWkuYFZHQp3fpd6KNy3J6NC1aDRHf_aM7A1Y8nnfjQwK9XtTttczOzfeHZPsfoS3OHETLRY0R78wg1Z4N2lq7zH4bz2YfIwVpIZxJzTBakyZEhbIMqydarEzZ-fL1LayTtmi2eMNZ1i-yg4oQMAHvw1SpJGP7IQbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر کنایه‌آمیز گل‌گهر سیرجان برای دیدار فرداشب مقابل چادرملو اردکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104377" target="_blank">📅 18:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104376">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed1c9346a.mp4?token=VoIR-Wv91Yc3B58o7P-KhuoJ0TLtDPW9tDDc6OXx-CI6tjfR-wexTY45GGJup48Me-mm6rTTk7oMfyCGqrEbdAa0zYeuCnR6GKxzVeVci7TWa69ngToIanG6Ng5N5ZXU2ilOzoU56imRChlX29nrP6baP9V-9sAXOEC4eKsafZV3qPBaW-FnPoMfbbJYXW-VSEm6-3X1GS7xxX2RD7fCHhhVHyRl5MuVW9p1qlo7pO7krYoXHPsRQedZfkwlqVFo_ntvpry9zYLOgKiIwzdzo8Pxlni48LwPZnJeMt69RdaNsK5116OwAY6tlToAr-Mq13l93Z9HLWeWWtgQQv-1aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed1c9346a.mp4?token=VoIR-Wv91Yc3B58o7P-KhuoJ0TLtDPW9tDDc6OXx-CI6tjfR-wexTY45GGJup48Me-mm6rTTk7oMfyCGqrEbdAa0zYeuCnR6GKxzVeVci7TWa69ngToIanG6Ng5N5ZXU2ilOzoU56imRChlX29nrP6baP9V-9sAXOEC4eKsafZV3qPBaW-FnPoMfbbJYXW-VSEm6-3X1GS7xxX2RD7fCHhhVHyRl5MuVW9p1qlo7pO7krYoXHPsRQedZfkwlqVFo_ntvpry9zYLOgKiIwzdzo8Pxlni48LwPZnJeMt69RdaNsK5116OwAY6tlToAr-Mq13l93Z9HLWeWWtgQQv-1aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
از حواشی کمتر دیده شده بازی استقلال و نساجی؛ عصبانیت سهراب بختیاری‌زاده از حبیب فرعباسی بابت انجام حرکات خطرناک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104376" target="_blank">📅 18:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104375">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6820414d13.mp4?token=iPCFDIxmXLZSQI-fn8eTE9rH1Fn7pS1SxojYfyzfk1PJck20UK_9sNg5SkFNPL3c69z9aADyr2zEfe03Y2ewVneWdH3TqfHdxU5OUzl3cIpjo7h7WWNWXFLZq1rzXjKI8ESR0eOf8d_hHw3npK-YL7hwyDeUij0JptPuk7jxfZ6nAhGEPHM9cFN0zcbWqcRtS_K9_cVXkOzZZheo_0CpRNlF9BRjGCo7clKN5pSllHv6USRMWoUAIACBpwjCqoAIPUrs9srrdQoHrUBw-FcO0xK9j-_QiJh_utDM1ucC0T1Sm-K38TTUjQYMweS3F5iEIxrmMCl03U5TIkSKvuxZug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6820414d13.mp4?token=iPCFDIxmXLZSQI-fn8eTE9rH1Fn7pS1SxojYfyzfk1PJck20UK_9sNg5SkFNPL3c69z9aADyr2zEfe03Y2ewVneWdH3TqfHdxU5OUzl3cIpjo7h7WWNWXFLZq1rzXjKI8ESR0eOf8d_hHw3npK-YL7hwyDeUij0JptPuk7jxfZ6nAhGEPHM9cFN0zcbWqcRtS_K9_cVXkOzZZheo_0CpRNlF9BRjGCo7clKN5pSllHv6USRMWoUAIACBpwjCqoAIPUrs9srrdQoHrUBw-FcO0xK9j-_QiJh_utDM1ucC0T1Sm-K38TTUjQYMweS3F5iEIxrmMCl03U5TIkSKvuxZug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آغاز قدرتمند منچستریونایتد در لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104375" target="_blank">📅 17:47 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
