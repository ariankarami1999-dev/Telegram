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
<img src="https://cdn5.telesco.pe/file/llK7IPcic6konEPbVGFxlEjg5XxBRTDtANNjc6nAKnpw1qBD3rJLmwSkSzBL2Fimt7EzXMHkFsnJXfZ1HBDDHHTT_vo6S8de0DXo0RpXETArp5Viz_5_Sbjmn41zy4rUV5-BdG73iXAjDIOI8paJvoEyvbqtGbjNVOZ4KiqKGsz_RGS0XZCuTyjTG-2oyiGkoBtApPEygPkYLwDfEzNhtHDxKbzyktig0B8iE8Xd-JbxkKcscWo4U9Ueua8d0-fZhzW65gIBxZ9vLu7w30nf6YeaWXAuechbYkDyqPwU1Itk-NdvvBLuhBhBsVrwp8QXgzrVbg21dIu4Cw7K0PqPYw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 286K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 03:12:55</div>
<hr>

<div class="tg-post" id="msg-91630">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGZHgjvLEzsjqWOseNdtApL8PpHjlywiOuLMobG3BVnB3VW0lguQe28xyevD9lSSglcWYUPeU_ejP5CBrMd30ZzAiPQKu-aS_uo_gVV91QgHwkCTPY4NTcjvGVDDxVlR2cMVY-5_uPDCOT-Ir1gLFGQ-gIWSQKq3c6Xdn_VjxHXsGNpt3JrQORFH44mT4oM9iAr7duqJRAN3p8TQYDy07DBkvHNxai3dsHtwn39mKr3pKQ0F1kKlXhftDDuIG_lssf82BvZPZvC5LmNXpDXtGAXA1dSvbcK6LUaSfe2MssQFwRW_GjuMj__Dd9frvQHs0Tlx-oYIf2CcX4DI_HpN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فورییییی
از موندو:
🟡
🔵
الهلال و النصر پیشنهادی به ارزش ۸۰ میلیون یورو برای جذب رافینیا ارائه داده‌اند؛
با حقوقی چهار برابر حقوق فعلی‌اش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/91630" target="_blank">📅 01:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91629">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axnusDTOn-2RnTCPSJI8jPrt1yg1X5k-_kDWNEmX3AcyzkwF_CUCDNjFwgKzfWldBRhwOtToKWJamJsyBb6t7wGBKXdlcGdkxO019SG9qO3rSVevQ3jUUZom-gqYvI-rV6WzIYeky4ZgMvHO0GEerMlJKEA7dTQ3g3Lrd8NUI65FWYm8W01QoFEkZoa8pONHF7rhHQQLIWjn1gfcfgm5mrDlBfxAk-k8VO1Tn51PI1Zn88tNmYEaGRPeC1LBoOk0f3KDd-yywxT8PPj-CddG_Jkkul-zf3BWzjWG5yQkM4YeKcs6FG9UcYaKnE00HKfucX8WaTaxnVWpXfJwC4Ojvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
رامون آلوارز: بنظرم بازیکنی که پرز قراره براش 150 میلیون دلار هزینه کنه خولیان آلوارزه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/91629" target="_blank">📅 01:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91628">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-owQfa3GqvnfAU_EPZpuHMUaW6zzIphoRPBoGlRZYASH9r04Nt45XycuCnlK2NByNYSFNvP96t6ZTlbIvHJhyYYqFojwRZo0dr_JhU26FDBh26uGgNNUvR6hZ7lBVzf07oDRwwufbSzqgCGwzFSmcVp4ht0Ct9dhy9YrtyqS3DGcJz4Xb0JPiQ37JN92BbArFltIpi1kd-NCv99fZ9X44kBhGxKxAOKzKBP2UEvfR-HeLQKONoF1WiIHAywQ0ybCpuluRyG5UJycJpwk6LLiOyfIHvjMss3MVBNarIKfc8hfzrhvJ5sXffpwf_D_bpy58hK4sCTjG3r_wQilC3hnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو در کنار رئیس جمهور پرتغال قبل از سفر به آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/91628" target="_blank">📅 01:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91627">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عمر آرتان، داور سومالیایی منتخب فیفا، از ورود به آمریکا منع شد.  او قرار بود اولین داور کشورش در جام جهانی باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/91627" target="_blank">📅 00:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91626">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce3S86d4NHoMhtXY984QG7-uBWQbQA2ACEtaLndL0MG9Q77aboZCcHO6Kf9L97ExtS1UtevmPGnvz0sN1W3HT4MDjf4gAEVC0FqwxPFshXozQPw3OFHGuINWdbEpdGpXDe5koUNfJ6Orwb0dsfGpEGIRNshQdFI9s4z8LsO_pOvrCS_nPmA8Gz-Pkq7zNp8dbgcAnkSgd06Jy-Y6-3lBAgxfCKFe5UFzpTaB238tKkQH-PIJEMsMwL7U86e7GOgIb5pDrKN7XspibJ7qKfq3RWAFs-hBoGpTzmGgqSgoT7EAOgRQ4HKfhRzOanaWuhKVnugRI4VGy8lIUGY4srpOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📣
🏆
ویلتون سامبایو برزیلی داور بازی افتتاحیه جام‌جهانی میان مکزیک و آفریقای جنوبی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/91626" target="_blank">📅 00:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91625">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElsghVIuqVHEHeZnfYcV4mvMg849JMCX9svP9QTDYmPxckSpxwJQXG94bJcj4vjw88JgCdp8inBqE1DWn47l4iGYIxm0YKRsO-3tQyKuIKmltpIxUhCtK4oC24Loh6_DnK2MV-vKbtauPrxogTV2bHnugeOxXvgtks0zUqFK956P845C5EeEk8qHGuLjYwrKFy696IR60twN1uDm0T6-Nyje0kLq3sLjnhfmj8mbQnZkE26EsMDxvBw0eFhBvvfpaJwFj77R5rbOU9AiDpmpu9L9Uo0c3LMebW46Gjgf6Dx3x_OlwrTYcCq1zC8gqD_XxsAJ6lQjdKECrhBBl-gJlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">POV: Bitcoin in 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91625" target="_blank">📅 00:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91624">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj_F9GxFarOoGj3PXhz1t6U3nmA_DTAQ8WLJtio2Ptb5LgryRDD7toQI4_l1mWS5vUZJS_nflhsUMiP2yhZPp19xrsNtqhZ-mrh0eLSUOBooL3MzmC_oafI1EXwsMctkgR-hTbrfHAhoCc-a1S97PpPoETjw__qzTOg80TmwHMMFr1gc8QieZa9ey0CrcribAxa3RKuyRugRq0EZzjMPfFX6z5jq0qj_L1o78EDUfaLwtg3bjN7wazJh0UUEKEoF3xIMg09NnMy7lcYROfhwoqPP3IL-itJa3wP5wZGmZ3tV8ssjtxbw_a5MoAL6uh0rmCdACmSVFBEDUunvmwnalA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آمار پشم ریزون  مایکل اولیسه تو بازی امشب: 3 گل 3 دریبل موفق  4 شوت تو چارچوب  4 لمس توپ تو محوطه جریمه 5 شوت   نمره 10 از سوفااسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91624" target="_blank">📅 00:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91623">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YNWxawSfCZzna0AhwbL7MllvMv8TScNc5NcjoSzhujwqn96Z5GpEmLRxxD_b6SO9M_eSQXkujFzmZprWaWYuRQktBwkynWZUB0cvqVniWwvCr404V3VZUw4VsFc40TVk8XTwlbEdz8Wsed2Xwfby3GUt9HMu--XfJXUV8rP-nawVJpc9lipLISr33Vx7qgnvmr3B0synrBTshe4q2zpWQZ2eCeW8ZssvMHX8MWSVfwT3vW7pRZFrIzUIkC97T1cow1ilUBgqnf9rSoW1GuwJTGm2ky166XQCpwhLhP1Fj8deI1kd9gpEBCAGr1FYVkqGBEvYW2N9xkra3yCJEBfBGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آمار پشم ریزون  مایکل اولیسه تو بازی امشب:
3 گل
3 دریبل موفق
4 شوت تو چارچوب
4 لمس توپ تو محوطه جریمه
5 شوت
نمره 10 از سوفااسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/91623" target="_blank">📅 00:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91622">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaea310c51.mp4?token=eadkRBGdRwom3KS7SfFkkgsornFjYU0wlxTFAzetx7eFQyTAJXspSkeIlh-EO7d4KITTmrCgAYeda3liZy41EZL7GJx1pmYTyNczSm0OFiDISZQsdKPg3dj1hPVpOcx_WV7xsUzS-ROF5HnIVfYyUdzn7glyZmsIVGicFdHzafqlo0rUvsXmexK1kgUD-8jK8mJsAms71YB6hmEkCK_96YEaekdxiLJJq0qPzUKAtfv0NmuClq6seuxUQl_UgjYHKVJqNVUny8_9lBaXSazMuYU82Rm6eQ9lYqRlAQtZXtPnPzC54tG-71KKlLJ3xRlvTGsijB-T_uz1WgSpKnnZQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaea310c51.mp4?token=eadkRBGdRwom3KS7SfFkkgsornFjYU0wlxTFAzetx7eFQyTAJXspSkeIlh-EO7d4KITTmrCgAYeda3liZy41EZL7GJx1pmYTyNczSm0OFiDISZQsdKPg3dj1hPVpOcx_WV7xsUzS-ROF5HnIVfYyUdzn7glyZmsIVGicFdHzafqlo0rUvsXmexK1kgUD-8jK8mJsAms71YB6hmEkCK_96YEaekdxiLJJq0qPzUKAtfv0NmuClq6seuxUQl_UgjYHKVJqNVUny8_9lBaXSazMuYU82Rm6eQ9lYqRlAQtZXtPnPzC54tG-71KKlLJ3xRlvTGsijB-T_uz1WgSpKnnZQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپر گل اولیسه و هتریکش تو بازی امشب
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91622" target="_blank">📅 00:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91621">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fw5ZSjKqu0cD3vR4wZjI70_cBpX4kmVGlU-fIyhHZOmAeONFbPadRz06QLf2UsbiyFS7U89QlC7bo1YoeyaEljgUOtT73Buk3OFxpA52rOsOb4VliSt8WyBlnF4YteMI7TuKy0Qe6ucG7i0juCltBySK_XDX_JOXXQXgi8pWuBLrtVBwWgi5Yryf-Oh2IVQDjKabe5kXzr-QRYHjRtA091bohnIch-Je388U9s88M5vK4SDtq2x-YaxLN0kHvuKZmhplEB5Lx0XpVDQEpnuYjyKN6UdlsoLmo1PAW-nG_wp8WQVXOitV8rHLkLbqXg7jCAswfmfxgJEGDdtKU5xtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه توی ۱۷ بازی اولش برای تیم ملی فرانسه ۶ گل زده و اولین بازیکنیه که بعد از داوید ترزگه این آمار رو ثبت کرده. ترزگه آخرین بار تو سال ۲۰۰۰ تونسته بود تو ۱۷ بازی اول ملیش ۶ گل بزنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91621" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91620">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پشماممممم اولیسسسسسه چقد خوبببببه
🔥
🔥
🔥
🔥
حیف این پسر بره زیر سایه امباپه تو رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/91620" target="_blank">📅 00:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91619">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb905f6488.mp4?token=LX_gfc-VNMirIZMKhV7R9kyXrko8eunbIFSJSqgfKP2DWQZ_mWm_Rt8HFuOjnoLWb6ioiMhCX_BLPJKJb9fGVi61TMBRzuZGPufSVYSDDobTowcZwISyrCKY3uEw3to0hDM4kCiB_uir9t_UeInBKFYjbNWhhyORT3v111RJBSbRTkAfMRnyRwpRR9zETdbSeQxh8MopkuLnZRra9u6q_c-ZXXGrs1eNvDinM8avBQ0e84YLwf_Myxj52OGWbzE9opVg1DhzddKGutTn4hNcFGPUWtZJF56w_7OxkGAvfllnaKt0CVRRjdSFGviWowqxdsWec9bK4bIIDkDmRmqdMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb905f6488.mp4?token=LX_gfc-VNMirIZMKhV7R9kyXrko8eunbIFSJSqgfKP2DWQZ_mWm_Rt8HFuOjnoLWb6ioiMhCX_BLPJKJb9fGVi61TMBRzuZGPufSVYSDDobTowcZwISyrCKY3uEw3to0hDM4kCiB_uir9t_UeInBKFYjbNWhhyORT3v111RJBSbRTkAfMRnyRwpRR9zETdbSeQxh8MopkuLnZRra9u6q_c-ZXXGrs1eNvDinM8avBQ0e84YLwf_Myxj52OGWbzE9opVg1DhzddKGutTn4hNcFGPUWtZJF56w_7OxkGAvfllnaKt0CVRRjdSFGviWowqxdsWec9bK4bIIDkDmRmqdMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل سرگیِف بازیکن پرسپولیس به تیم ملی هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/91619" target="_blank">📅 00:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91618">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پشماممممم اولیسسسسسه چقد خوبببببه
🔥
🔥
🔥
🔥
حیف این پسر بره زیر سایه امباپه تو رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91618" target="_blank">📅 00:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91617">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ck9E0ynpUWXSRXvCM7Z3H-lIw-gDRhF9xFaaqXNl9XchEO9WwOdPVPZQhfluIQTI8qMPzvUt7pvsRvCB3B_5yKfgpIjsILq9oRw13nsqlQdbKiKXYWUyA72NTh3RAvFQdSGmxItt2j4PtsVABDJkuHYUqSO9x2rJWtDF4S0yktJrVV--o6Vkq9c5G6ZMcoYhp-AsgFHYNwMroYmQvTJJ0ZKrwNCua4MI7Nn9hDCz0tPjwCDerqVlK2OdZEoPGN6U9zUHMxrmloCGpHWEKy5SFJkL3KTRLtfra8J5WzF4R1-j9XXBmsQHR3gfKe4s0TJsEfR0n69SNOnN3PRNjEc28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر آرتان، داور سومالیایی منتخب فیفا، از ورود به آمریکا منع شد.
او قرار بود اولین داور کشورش در جام جهانی باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/91617" target="_blank">📅 00:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91616">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzfwOOpleA0hJzAX7_rE3TWYIeuNkMNDXmIdZVVkuN0OLulIoy0eM-8yMQPCFU5-Pjw6mQ7Y_Y95JfPM8fjt4zst-GsYYYFGhRM2peqHfQKinDLZd4KECe-dLhg6xIX2skaV2rWA6Xwb5HKZvjotHErI6pnwawt7HRx8NTeuq8W_CGs8BTKWnqL0d0ZrJwcyq4cHrff5ndGRX2xhD3ecsG0UvLnotNmPss00HUoVQ-ULwouIzpajrBMEm-sBFZTRNH6wo0v5GpP13dpxNGWl8scS1vePP1bKk8Eb9UhrFmlZN-2HNmMwM_hI4WWfepjLWsA0eHuqYZtVw3_lMq4CEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری؛ یونایتد، psg، آرسنال و لیورپول بدنبال جذب ماتئوس فرناندز ستاره وستهام. تیم لندنی خواستار دریافت ۸۰ میلیون یورو برای فروش این بازیکن شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/91616" target="_blank">📅 00:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91615">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REJ-XEr7NPp09pFxyreKqe3xIBYy9wnXxA8p_MBk1psqfD2dXs7cvPnOdUUj9LatXon4BT8WCndnWHWsO6zEcj8qFcU9e9Lec6c-i4PhGI_y0pv95lJiStm2u7Fx7yJ0RA4nCq_PHl-DbsRiDc0Nx-Y3plUNl2KlHus0XqrRCWC5o3qloDCtFp59f_PMplGdXgUmcz6MB2B7LAAMj_ikJAI6d8wYpFVV-_SuhjTTKbXaYq8EBub6JwfddxKK4fYUiox6qW7j3GoLMknEt2eDAuqr5lSA2vqYy519eDIeu8s8jiVrSr7MvPi6XCGhYcmJXR_2GqCNadNSOU425cBpcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
؛ گستون آیدول خبرنگار مطرح آرژانتینی: منچستریونایتد درحال آماده سازی اولین پیشنهاد برای جذب رومرو ستاره خط دفاعی آرژانتین و تاتنهامه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/91615" target="_blank">📅 23:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91614">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c9b54af6.mp4?token=L4pNR8DeXV3RB8jJBeJAXobNdJrb5q3dvZc0BCr2xQDXmxafzknnlkHmyDeXx8wI-XF4TfRB_wQPQd4rcxFb8JO0_Npgn8laBwLi8_bAOCr-GDgzLKsHzR41mW_J6CT9Oj_fLO0-E1QZtxeOttGxbl9j0lRJBH_zX-iCGLBvFVpfuZ8o0kzFSu8RL-disYwZjRcHvXtt0E_tbZr3EcquqDLYyp27FGJZaD3D4fvaWRzO9BiiE8SUbQBR5jsXhv4tJQygBosx3ySSw7-s1asuRTl_dad6Yv1RmA6_8H5UZgckje5JltOhuszimolVWyRiM-0iB_DnqJkir0iFhLJvRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c9b54af6.mp4?token=L4pNR8DeXV3RB8jJBeJAXobNdJrb5q3dvZc0BCr2xQDXmxafzknnlkHmyDeXx8wI-XF4TfRB_wQPQd4rcxFb8JO0_Npgn8laBwLi8_bAOCr-GDgzLKsHzR41mW_J6CT9Oj_fLO0-E1QZtxeOttGxbl9j0lRJBH_zX-iCGLBvFVpfuZ8o0kzFSu8RL-disYwZjRcHvXtt0E_tbZr3EcquqDLYyp27FGJZaD3D4fvaWRzO9BiiE8SUbQBR5jsXhv4tJQygBosx3ySSw7-s1asuRTl_dad6Yv1RmA6_8H5UZgckje5JltOhuszimolVWyRiM-0iB_DnqJkir0iFhLJvRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چی زد اولیسه
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/91614" target="_blank">📅 23:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91613">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔥
چالش جذاب و ترسناک‌نیمار در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91613" target="_blank">📅 23:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91612">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4-Zz99jOCwq6m4SHY1uHigB08pwOUcPtZlbYU-F8L10bOmz9Z_lUrXMdfzttHH6H-wd0Xnv6gi6lFTD0SAZXnSBQpv1FWupHiilDHYT3Y-4LIXMBJkRcvXxhn_8mirwek0Pv4ar2USdpPS7dp_8WJxBIPcSRs8IGJ0M8qaCueW-u1reGn8HPysxoVzHdVQ4S-PmBlrPU2oOY2rHGSNGj--v0x1VQqnGOUzZvYWFUsWNsCI9hOvIZsrFJNVeNFohg7DXDdQVPLZZoqg7vlxvrHN184JG_wjpUw5Iaq5B7bO3CehyEyp1XfDHkPzFgrpT58mEEyAylk1Pud_qW2pavA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
دی یونگ: میخواهیم همه را در جام‌جهانی شگفت زده کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/91612" target="_blank">📅 23:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91611">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUWcSme6V_lQrYaAuLx11P01XAO1XWyWhM3k6MMOxlwBtax0mJfGF9-Jd982wRiCl8PKcSIplXUubgvFjD9p51i5rwJ-ak4DkBojmzChF8vIvTprGqpZnan90uHL2V7IRr90CPq1tWXfQrhlE_T4ZFguJNJltTGlfqw0Cn-0riZSLpf2oc3vuCMXYf245ErsK18X_lAa-9lqBs7wUerp5UxIUl3VSCAT4wJqrhBN9ZqNFUCbMcmzeYq7ZqCYq3bCMBJjfQ6Ws55uP957SC_3LHLSZNMnGpaxnIbRotEfD3UqCStkQKlvLpiBlSspmP9pc1USXS8mUSEIZInrKqzQoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
دی یونگ: میخواهیم همه را در جام‌جهانی شگفت زده کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/91611" target="_blank">📅 23:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91610">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-u6drWgG___NA6L4vXR93Lfy64EdagUnH1wRR5figihyyepMSBvXQMNIIFefV97T7zOEwpqtvde_aHxNfj3Mb-T6xk351QaeWymLPFiNRsWFLpTKBwTDa5pA1A49JBP362BlZmjQlBxcCbPtIjxRX-5mhl6wygz0bwD-OiKzBPE3OIjl3Onm5NRZZfjN2Bt1CD6nPZA9aQ8_dd8s1apNHT7nxXQmKyZRNCN2BKewhnbzFjXmDtdj1e-FnM8io9JPLZZWBw_C8Ao9lPbqQz2t6VCiFKXszz4ZyRlQVXuxJljN4JszW5B5t_uJFwn_6MpWTPH3ss2KRdZqtx6ao-nrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اولین خاطره‌ای که از جام جهانی داری ؟
🎙
یامال : بازی آلمان و برزیل و فینال 2014
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/91610" target="_blank">📅 23:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91609">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT-dgQwUjmOTyBLP8ZwFgWfK4InpZrxzlKnoF5C8r31SilmiX7K6dpP87V4IykmItrhiyf7UGElKOX2HlK9IUc9bEexQqMrWsAbLBRgpUkFBD_hHL8sobchKd_FCc8LgRukgLB_o1JJxzYQE557FimB6GakFbeHcyhx9GWMcIEAVC-AD_gSGwC9yW6iXfnVuXJNIlJq-j3GpS11zmU6S49RozIwKsu1hkUSQT7sIfoQPDahiD6xmiklE9xJ1u7CfjuNx4NJyHylQaFl6QJkHqxW32IPwpjGzn0ALdR2GP0sHnvUlr70piG8lkF4niV7ZR6ZIgav3_-e8bvAgD8Wt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
| کیلیان امباپه دهمین بازیکن با بیشترین بازی برای تیم ملی فرانسه با ۹۸ بازی ملی شد و از لوران بلان، وینسنتی لیزارازو و کریم بنزما پیشی گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91609" target="_blank">📅 23:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91608">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43547db82.mp4?token=FoLiowOkxpTS3PuZ-ELkZr-nJMMISgwa7TvRd3zb7Ml0RCJbbgfz23PjyCmrR-WNHgMa3Dne-loaU7gG1zc6yI-RgStgR9WkaTd8wNEKwXbC-wDF4EB_M7HhV7oM13p4Ev2u1KgU_BEJpolvyPWfBsARoDzwexMZG9yVtC83H1u_UMmr5sLRVKKIrdU64MweMC6ISaU3jJ5_Ia_Xr6_7_pj3jAzgDMDTbFsESpFwPw_wnc3JRZ7p_UKspQhA0AD-ateDJ5_GL6twuMhjSvXWY9tdqVTcNS7EMV8kwrLGQQqMMTxWt8cnzZr0E3q5tLLPFMpTQFIoWA4DFiA6S7fJ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43547db82.mp4?token=FoLiowOkxpTS3PuZ-ELkZr-nJMMISgwa7TvRd3zb7Ml0RCJbbgfz23PjyCmrR-WNHgMa3Dne-loaU7gG1zc6yI-RgStgR9WkaTd8wNEKwXbC-wDF4EB_M7HhV7oM13p4Ev2u1KgU_BEJpolvyPWfBsARoDzwexMZG9yVtC83H1u_UMmr5sLRVKKIrdU64MweMC6ISaU3jJ5_Ia_Xr6_7_pj3jAzgDMDTbFsESpFwPw_wnc3JRZ7p_UKspQhA0AD-ateDJ5_GL6twuMhjSvXWY9tdqVTcNS7EMV8kwrLGQQqMMTxWt8cnzZr0E3q5tLLPFMpTQFIoWA4DFiA6S7fJ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم اینترنتا وصل شد گیر این فن پیجا افتادیم.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91608" target="_blank">📅 23:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91607">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21c49fb96.mp4?token=CwyZJSjMEgqjtAtv9WmZ4UTz4RRy5yg8AP2b-uJQoiGMuy9dWKD9uqj3Br0XfOHJ0Xe9ELwZee1HVWEVXLj2TjPh5di2anWbVspkV_itJgtfIWp8EY8EzYICTAWxuvk4voYTr68aHdia6zw9L0b3TbPoLPl44QNzvdTFpQ5uLY9ng-XimQG_2N2nWYxwlNkjXQ3ezDVmHRcaGj9gnLCcj6xpzGYVjckDW3kbBa0hwVjf--C326YMpVdjPoAIQAV4acbPeT_WhveUHUvpvSSikOQ5EOeftCkp8RoNWFxSWUlsZDPPuAv6izS7KUN4D0Pzw9J_oQsSqk8GFoM28km8Yyo0AnNU2pOVj9W5f_oNnE21hsp0nZTLIhPEqU0ZEp_nLaA51CsY-5mdTUGU-pZkRACAyFBj3ih0ESKQa2uBlcQ1xY6VAW0p8p99avmCHBqR4W8_5fKawLW5G015G7O5yAIYbp2fQUQZOesNqy0QEne1m1ozqPHrWIrEbBB9f3GtxY5RrxiJBqe6PRLRfU1_vB3yy8Dyi8f-vQZ0g-CNE_4qqRokuLdxUIKrdtvAyVw3OgRUskHQisCmMJIOUIrkRTS_Ot41p72QV2PFaY6oVHpZvoaKJO7qIjJ4rwda2xocsyKSeKTRhRV_hmUk3sOllg-Lq8mpG-qm-YPWjNCbyYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21c49fb96.mp4?token=CwyZJSjMEgqjtAtv9WmZ4UTz4RRy5yg8AP2b-uJQoiGMuy9dWKD9uqj3Br0XfOHJ0Xe9ELwZee1HVWEVXLj2TjPh5di2anWbVspkV_itJgtfIWp8EY8EzYICTAWxuvk4voYTr68aHdia6zw9L0b3TbPoLPl44QNzvdTFpQ5uLY9ng-XimQG_2N2nWYxwlNkjXQ3ezDVmHRcaGj9gnLCcj6xpzGYVjckDW3kbBa0hwVjf--C326YMpVdjPoAIQAV4acbPeT_WhveUHUvpvSSikOQ5EOeftCkp8RoNWFxSWUlsZDPPuAv6izS7KUN4D0Pzw9J_oQsSqk8GFoM28km8Yyo0AnNU2pOVj9W5f_oNnE21hsp0nZTLIhPEqU0ZEp_nLaA51CsY-5mdTUGU-pZkRACAyFBj3ih0ESKQa2uBlcQ1xY6VAW0p8p99avmCHBqR4W8_5fKawLW5G015G7O5yAIYbp2fQUQZOesNqy0QEne1m1ozqPHrWIrEbBB9f3GtxY5RrxiJBqe6PRLRfU1_vB3yy8Dyi8f-vQZ0g-CNE_4qqRokuLdxUIKrdtvAyVw3OgRUskHQisCmMJIOUIrkRTS_Ot41p72QV2PFaY6oVHpZvoaKJO7qIjJ4rwda2xocsyKSeKTRhRV_hmUk3sOllg-Lq8mpG-qm-YPWjNCbyYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این طرف تو جام جهانیم ول کن گورتزکا نیست
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/91607" target="_blank">📅 23:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91606">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d1d72e16.mp4?token=AJjV-Ie_sP4W9iT8H9yhksR03l6tNnmrZunUpw-nJy_CfcSlb9v7wnbUD_iBEkUUYAUFb4OiUqKDlVmphV9lIGVpk0U7whZY__Lf0-xK1mx1DDFiQObsd6CoL8cdYdQnQGw_5P-Ki3Em27BZmlK4dwU97-K9CzbuKHl0R9NIZ89adFxzLlBPHgUfJJqikuPe7f5k75v4K7b895tFhHiwemNS9L0QxmU-dURikBSE5nR4Af1aYS5Di4bK8pCGSh0GdK9Wu-ieIorhUUF4XrC_-qcDCnVKDAbZKyMTsLeZKtxDYwYww81DoyoWljOXh2xtPJomAEqAvB83yJ2C76TDwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d1d72e16.mp4?token=AJjV-Ie_sP4W9iT8H9yhksR03l6tNnmrZunUpw-nJy_CfcSlb9v7wnbUD_iBEkUUYAUFb4OiUqKDlVmphV9lIGVpk0U7whZY__Lf0-xK1mx1DDFiQObsd6CoL8cdYdQnQGw_5P-Ki3Em27BZmlK4dwU97-K9CzbuKHl0R9NIZ89adFxzLlBPHgUfJJqikuPe7f5k75v4K7b895tFhHiwemNS9L0QxmU-dURikBSE5nR4Af1aYS5Di4bK8pCGSh0GdK9Wu-ieIorhUUF4XrC_-qcDCnVKDAbZKyMTsLeZKtxDYwYww81DoyoWljOXh2xtPJomAEqAvB83yJ2C76TDwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار ریدمانی امشب امباپه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/91606" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91605">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUoUt_SJj8C3eOn08m7cHXCjki7V3DCbvs-FPe3lw3p_IUd21L2S_PqIc85zAamD26na7meJI4n5udXTZVBLpJxcSw0NUlAFtF_umKf5LJRKZLxmQV6uC2Nvj-DegNU5g_oIGakInYzNWiCwi7b3tm76kvGwVplKvVB6pgKafFg-TczhmlJJ0qF8uNVSbrGK_7OO84kvwcA-y1sL5gC8YepFdOFMEbQQPWyihGpastIl_l7gdYX3VNdKkcHQR4tjY4U-xO0dpU7TYfrjH-HTFF9hH9v4PwncIrS8FiM-3Sso30d7TEaFG1ciJOgP5-yjG67nlcVrrpkGdj9jpdMFXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فورییییی
؛ در نزدیکی کمپ تمرینی تیم ملی سوئیس در سن دیگو آتش‌سوزی رخ داده
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/91605" target="_blank">📅 23:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91604">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37db48d9f1.mp4?token=WkmMhO-obXCIy5i7xJAiXSEn3aBAeszoPJwNlEECx1_V5oiyWdkdijveQnk-ZK10turLSTVKXNNOX6cH5ibv-uuB5EcEnw-OwVteHHhsbTlHpzw9FaUtrceBm9B65z_QeKLpsWtOCQxnpUESWM9-ioXh_4lMuUYNI7FKGmvZQvwNx74l0WdwLUS_qjJv-0NrgmJtB2moFSvWYFjLLTn53pAM_hH0BMHG4FHvVV1V8qTCyNsMU_EneHTMzdF9vDEi8vRqaX5-01JYx_kanwOcH58FG1AJgnFHFa8EiGFcr6Gh2gTijHxLv0Z_VT-32jdQxsjpT3WKc0dbgyVVqkt6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37db48d9f1.mp4?token=WkmMhO-obXCIy5i7xJAiXSEn3aBAeszoPJwNlEECx1_V5oiyWdkdijveQnk-ZK10turLSTVKXNNOX6cH5ibv-uuB5EcEnw-OwVteHHhsbTlHpzw9FaUtrceBm9B65z_QeKLpsWtOCQxnpUESWM9-ioXh_4lMuUYNI7FKGmvZQvwNx74l0WdwLUS_qjJv-0NrgmJtB2moFSvWYFjLLTn53pAM_hH0BMHG4FHvVV1V8qTCyNsMU_EneHTMzdF9vDEi8vRqaX5-01JYx_kanwOcH58FG1AJgnFHFa8EiGFcr6Gh2gTijHxLv0Z_VT-32jdQxsjpT3WKc0dbgyVVqkt6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
زلزله 7/8 ریشتری‌ فیلیپین اینجوری باعث شد این 3 ساختمان متصل به هم از هم جدا شن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91604" target="_blank">📅 23:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91603">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f87b14f6.mp4?token=c8wOahAZJpwLOSu2UNXhW7akuqVhjnOs9bL2a1ta6brCGj9AenWfPKduod9oHeC0LgquMFMNO_rM0eHAFSiZEVey2eFufG2CcTjppNcy3Wu8UgqpmxCWrjX8QmfqYz86aMMK_a2ec3L5CIUPl07e8PacAXBP7KMzKmGBFBlxmynsbcWsHvrFTa5CWi8s0RFHecvFUnTUJ11c79mNvfQkVG8gM3DHOhaVg3DVRqaa0qmRaY8O8LedBUopsgA3MszMr3eJm49KBiLI_8eRDCXWiqTfC6ABoSVeXmLsIHrSrdSV615UfuiXFsg-dnfu-0MiwQYpI5Ib4HcdJOv2PdEbWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f87b14f6.mp4?token=c8wOahAZJpwLOSu2UNXhW7akuqVhjnOs9bL2a1ta6brCGj9AenWfPKduod9oHeC0LgquMFMNO_rM0eHAFSiZEVey2eFufG2CcTjppNcy3Wu8UgqpmxCWrjX8QmfqYz86aMMK_a2ec3L5CIUPl07e8PacAXBP7KMzKmGBFBlxmynsbcWsHvrFTa5CWi8s0RFHecvFUnTUJ11c79mNvfQkVG8gM3DHOhaVg3DVRqaa0qmRaY8O8LedBUopsgA3MszMr3eJm49KBiLI_8eRDCXWiqTfC6ABoSVeXmLsIHrSrdSV615UfuiXFsg-dnfu-0MiwQYpI5Ib4HcdJOv2PdEbWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
ایکر کاسیاس در مصاحبه با روماریو: «مسی خواب و خوراک رو ازم گرفته بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91603" target="_blank">📅 22:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91602">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIeEBP_-ql9LrejKB4ljS6WBwD4cNC6eHiyhLgPyvc2v72c5kMgudypCNhMdWhKoQk-nOT6lt9L_Lr45J2rCBCpNaG1bMRUGNHCeK-BJRPHtr48zzKYI_0bDJqqjXyTGU-_NSE2i2LaxUoPypJavEwgmGEqZ102yqNnh_oEQu91ZWYiGVD7g7CAcg36bFpZGQAlyADtjSqjJtZjHIsGx0Pfjbw6UNVRkeJUDWwQ4OcSgrVYqq190Zk5nsN4ZjRCGp2U5n--ELhudmAXY_G93T_w_7Q6Co691VGfbNyFjU29U3dZeHMHMEEVcEQgkvN8efrQlHuqJ4pjZbeZ_z-w5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برونو گیمارش:
«برزیل هر تورنمنتی بره مدعی قهرمانیه. پنج‌تا قهرمانی جام جهانی داریم و این اتفاقی نیست. فقط باید تمرکزمون رو روی هر بازی بذاریم؛ اگه همه‌چی خوب پیش بره، دوباره قهرمان جهان میشیم.»
🇧🇷
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/91602" target="_blank">📅 22:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91600">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzMbeR5mUo5KQA5ye6xLpaowNTsPbJZyp10j-KUpeRug0TkObMmOJE0u8HFT6aTW94e3KXiQ8XMtTOAvtmjP9-xqHYVRFDcEjKPZKTCKK2pMpuSN8N5uwG021J8EvR5sRkfcQT_qddGqm9jzw7Z0O_UPgE1eJvA2EeC1Y3ZE0-rLrstKkXZ_sJ6JjjSRrKavsT0ZAApx-_d5at3humsRHWrX8gX6Si_nUr9jEul_BPGvxtY7oJcrJ2Qlk4gYAR8Yndz3FTsTtRn3jSY7sKP6JIJGZTtC8J-LtCSKi-8BEOo0oUNUpYeJc0FuFsbvhV8izuHzINFFvUdmMJP5Q13UZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDhdnTG4K8xUXaEpeT7D6KCFMXYAOtQWkyo1Rj3cBbUWWUkztBKgWnLQ0G-P3ua43zRaii_GngtSXW1ilN-jPf0eDJBcneyLix_bD47XlySRDwCim7EXviF9tIW0GfsIjIe7OuG6WMAbjU30wwgh5IM5hiIMiqGDjpSEPe-_BJYJ-Gpe8npf-mCUjsWS2pSijXqvyOkLOqzD1SZvnwiuZzw0GN10lJXDd3VJldOCFf8uKb9n0q5lvhNjI77fpG4k08L5IFRTwJnBQNywLcUuQprWk9MSR7JSvJGj4NhRx63kXJ-mbfFG6gQO00HO-dGC1UEgbC5LMDJM8Wui_ZFwtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
خوزه فلیکس دیاز :
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گواردیول میخواد به رئال مادرید بپیونده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/91600" target="_blank">📅 22:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91599">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYO8_vrVA5qOnImAiDC_F6Jv0Ia285JxDhyUxsSk3YX3fwX8vQANUWXay61F4oVvosiKpCUO3OXfAgFDuXUUaIEA5TJPzvljsYSdHOr6rStrWM_HuUY4KHlFBJ0T5zty_91TeuyNXnNHq0zU2cLKO2NimwaDm2Hyb4DRNr0EaONiyzXo_JQt1l8RP1SFeOQruylcfBt8uwe11x-NEMPOxZHesYbB9WVPYAE4Kq6B0eALgtZ-rcvfFqEt_gylO8J-qdxNkg7Hb3KqGoVexVkSLudPx56QnA9kIzDWhpg4pVg9kO4-puJjnWFxibScjpQWSrjn1TxJjZmzQay3sYK7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خوزه فلیکس دیاز :
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گواردیول میخواد به رئال مادرید بپیونده
!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91599" target="_blank">📅 22:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91598">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q61Ovr9EXDIlncjpghHPTI5QN563ApXdoetAeIIVCZ4Qp04RrtGI1CnHSFrhPPIyTi3qRGH4VhWHWrq6yBHSJT3AyGZ0cGin5vRcnZDHatPDqDNAr745GOIH-3AfefgAw6cSdW4hB1faIX25KBB-yRJ6bp1ZFJrHsADyZaBWie_CxifjSbqcTsYpd-Q3D4gDCiBKJfRw5gASGK7IVVpu4_pvrpFpYKVwz2XfQbjhn5bl5mYM3yQsCf2rE4L8C0PtTvs6Xz1ZFJYG82tEZZ_8VAT33IJzzmJBn4STFIY7ZWeU7mVdfMMW_FPuOM6ktys6msZ9-EsnVZuE9IztlVoPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل: نیمار روز دوشنبه MRI انجام داده و آزمایش‌ها نشان داد که درمان او به خوبی پیش رفته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91598" target="_blank">📅 22:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91597">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkXjQHc67SSBEygb77z9tN-2gAkHxawtDmHnLH90DPMQWlJkafFScfTdi6goWOisy5jkaTOZQftjsMgi_H9GrEA70CX7bQP1A3lmHfvFiZGmCO999cu-BnG0ddDfJ4GJzeEpe09fDImudeD0lbvQ32HtY1yR0009PPb_lGT-rlqOCq22lC75ljLNwtuNTOtNMeALSakdV3MHXGlCFPbJJyGv_A2s1kxEGLhrxSHXXLUpKGHsenI2zU6E4EgXsG_3X4Pga5kJeBPmhmoI3UPwJZTaylqiJq72DNKkcDonB1WEaq-SmBgXmG51Ay9hbLunkzkveqHbGOrvZp26QMohoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رومانو: برناردو سیلوا تصمیم گرفته مقصدشو بعد جام جهانی مشخص کنه
❗️
بارسلونا و اتلتیکو مدت هاست که با ژرژ مندس، مدیر برنامه‌های برناردو سیلوا در ارتباطن ولی خوب هنوز با هیچ تیمی به توافق نرسیده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/91597" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91596">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVPwXO6f_bx7EVKFL45ZlOdIYyOQxbNj4TakspW-ej8S4BJCXfM60OHUNb0qiYGYScNbRF9YKs_mOhMYpKIIjFXtbPFeNVH9laQaN9blHQlrDdWw28g7q7vNrx7__ih4n7_HsLYgvnsmEndf1FWhLwwB2L3TpENsGMuVkChyi41ZCyHSfkXBibejrby2cqhEat3KV2XZ3528ocwm73CbNRDEptpLDfXUQW3z5B-M1dN0RzIqKrnArDfITcImtJLOxdaSWkJ_veSxLJ9G4x9DStfvGbfdjfZH3Ny--4-9W6ILdSmN4jwR6UPSLJ0px1TW5A_eqkkMvKmp8EpLjRnEOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
#فکت
؛ مسی زیر نظر اسکالونی داخل تیم ملی آرژانتین در 7 سال اخیر جام های بیشتری نسبت به تعداد شکست‌هایش داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91596" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91595">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f1d33e7b.mp4?token=QC-3F7pvBk4if0lKo0SjUFBbJsoFoavHnmY_Jel79CA8BueYHukhQrE5hbIzyHkJhIpMPbUp514kybyul3aYrQMdqR3rQy4-hMAjXS77IaoB8muMnCaPGMWWUafjI4tHq6soMEKNpSXZPuJRVpXBQVH8-yFepf6SkGdrpJQtpu9PzIES52x20jNLwufdjPuopcZHeC6Wt2OpHpHk1GexB0gh1_gVCjLhLzCg8BCM579CTAlgjYY2R8xcR7-cLLtK0u31WODb2m0BytZkAzR6ANS8Kxgceue3Z1S7pLDIFpaXlf1PYTTJBJHyNpFamrtfuiouIpCyNt5cPLKAupDKNx2mecFKwgl5Y7sENS0VBuSy-FZKEC7c5fYAi8aP9ZloFpahy697P0F5c2F00YJ3X__uj-chMpVrCFw0rCvltA2N3psvVdBDved9hBf5TxxPaNtibIlqNaMkCjKknsm2smsjdBP_juBvehAeljqrFYNXd7-GQWlCN_1-WuKD5e7eH2ZBzXX2JC3uuFiD_uzUO6g2uhUtqW3p5nF82easWX_Mu1IrDuMoMJtzt_0LskuYh1GcNwvY2dZo6EbP4Wl71DwiOMfZs_B5FiPWaSzq5kyBzNewYv8NvyKCGRjZmfDb7EUnpkGelNsKbi7J9lG5vbLvTEiCE9uySXvDMC-O9DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f1d33e7b.mp4?token=QC-3F7pvBk4if0lKo0SjUFBbJsoFoavHnmY_Jel79CA8BueYHukhQrE5hbIzyHkJhIpMPbUp514kybyul3aYrQMdqR3rQy4-hMAjXS77IaoB8muMnCaPGMWWUafjI4tHq6soMEKNpSXZPuJRVpXBQVH8-yFepf6SkGdrpJQtpu9PzIES52x20jNLwufdjPuopcZHeC6Wt2OpHpHk1GexB0gh1_gVCjLhLzCg8BCM579CTAlgjYY2R8xcR7-cLLtK0u31WODb2m0BytZkAzR6ANS8Kxgceue3Z1S7pLDIFpaXlf1PYTTJBJHyNpFamrtfuiouIpCyNt5cPLKAupDKNx2mecFKwgl5Y7sENS0VBuSy-FZKEC7c5fYAi8aP9ZloFpahy697P0F5c2F00YJ3X__uj-chMpVrCFw0rCvltA2N3psvVdBDved9hBf5TxxPaNtibIlqNaMkCjKknsm2smsjdBP_juBvehAeljqrFYNXd7-GQWlCN_1-WuKD5e7eH2ZBzXX2JC3uuFiD_uzUO6g2uhUtqW3p5nF82easWX_Mu1IrDuMoMJtzt_0LskuYh1GcNwvY2dZo6EbP4Wl71DwiOMfZs_B5FiPWaSzq5kyBzNewYv8NvyKCGRjZmfDb7EUnpkGelNsKbi7J9lG5vbLvTEiCE9uySXvDMC-O9DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یورگن کلینزمن: در فینال جام یوفای سال ۱۹۸۹ اشتوتگارت در برابر ناپولی، با دیدن گرم کردن معروف مارادونا قبل از بازی، شکست خوردیم. همواره او را به چشم هنرمندی میدیدم که با ذهن خود درگیر بود. این ویژگی در داخل زمین برای او یک مزیت بود اما در خارج از زمین او را گرفتار مواد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/91595" target="_blank">📅 22:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91594">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqgoU6GylIxWN587D5RqvgY2YwjSFYj1UhwdDG-lfyQr0W0DuNwlKop-YsZFWrvdqyviSEz-Sjjtiy8abx6N93Q7t3GufhmXtIoglvCab5ZYhrplfnHHAXkEvu5JPVJcHNwg6X1PQbc_VnGfhyPViP-AFix6yKf4_r6gCmxjqpzwouPDNq1C5K23nG06neElG8w0XIUQYOjwYl-1ONTBxZDCbpCv6tiSaHXn7RaSiQX1c2cdqF-9zl8PEv6R-UdCm9U-0h-qCOR8kgAkerigycdbgIBiz2YfKgzAXqV2dCBMHs_U3P5xVtNpPdjYHoaeJS47eWOFeqZIUrZ5O4_1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرژانتین
🇦🇷
-
🇮🇸
ایسلند
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
ورزشگاه جردن-هیر
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آرژانتین در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایسلند در
۱۰
دیدار اخیر خود،
دو
برد و
سه
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرژانتین
۲
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایسلند
۳
.
۵
گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91594" target="_blank">📅 22:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91593">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxN4rUHtrkna6dO64o5FP4tBqsmt6ZhJEDZX_iIMq2W5EDPhmj4qyOfZGOvOwbDIQMJdxL36sbjXzCUBIXjXvmnXeP5Ajf-VRH6Nwaky4rEnoawpCLit598lKvxQfcVt2eyD5mwPaOqt9E7HWMHYdSqSnNQnbfrAVBVeHVr3aGNqb6d6cz_PIxia0WVmiA6SBgHM1wFyrdbStdJ6hT6Wq5dxu8AF_wTHU8lY6aofGN_5uBA0ZiJLDMkIXVtOHf4rEsKeWfWlTl68L3s8znHJYeDqjjO3-uyZktD9Yk2QIe2C2NHXrPXownmCQickzq4E-EDBdbkW-kUvGICFLrLF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شیا رائل ویتست، بازیکن آمریکایی تیم بسکتبال بانوان استقلال، با یه فرد ایرانی ازدواج کرد!!
چرا اونا میان اینور ازدواج میکنن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91593" target="_blank">📅 21:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91592">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxJwFLu6PWpLDDQ1lciEOLFapHQLOf63FDLVF7uLk-dyo1JkzF_AJRYPc7z7oQZ6cXajmts_HOlgY4N9Quf1SihFUlYJ0PCnTWrovFU7SN_9M8mT1YzAcfI-fSY772xxsnSU05Y_AAolO-jnBQe0op8bylxkwhgOWQnuhvvNxDXTtJKcFIjS-miyUScU2Zk7Gtxl_bzYdblw8RL231ArOtkwJsZfR6de6rLV9tuHE6KWK8F-MZ3-Ziw-aqjKn0sI_gRKIMvIaeIx4Gc-5PMXF8Hxynjc4lXiqdpgXUZ1pr2MvIJ69W187t3DWWA3vSim07CK4dm55R265etW9wLu0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشرف حکیمی: به مردان میگم دوستانتان و همسرانتان ممکن است به شما خیانت کنند، اما عشق مادر بالاتر از همه چیز است
❤️‍🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91592" target="_blank">📅 21:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91591">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0l4Xv2pLhNwLRyJtWCnmT_3pZNe0t_Q6wy89U5pMUELEMfWPM_GSu_JYtws6kPhL4sOMFoblPkqKATVrqjSJVWSs_tHBwdbv9-7ownf8dgxDziClAj5C8YbzsfzAPfFCg-Ry4d6AeJSXbXQhygB4PX1O2_Yn6UDo4dlh4sU2TMvapUlTs4XkoIV5Inb8qLs5kPC3ZmYrI9iojBWPzJx0bFveuhVsQ51Hn1LPFkWC7NOt2z88XeAbsoB_XKx8CTaFquJ8EYW-nqs1PrHQGg97zFOfItwubLIQ9lfR33EfQ8LvOVUgWoOOiUNoNdeAK3D7jT-eulJsqH1AQFGPZ154Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تیم ملی ایران در جام جهانی 1978، آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91591" target="_blank">📅 21:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91590">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFjYCKYCa3GBL_1o0d_JyitawBDB2uGBluXckUzNb9xP1lKdFDfxpHAXcFRQ6f_zQROefVBWWp27VXmL2Zw9qy6fQgTbz5158vbf-3_I79r76aAxFCBMeJkvnyykM3p__WkbsAjnG78yS-v9qtcQB5nvvIBQIwuiQCCyIAtiS8pnguUTSpnB1W4k_9kwhEJ2TfU1Vk4uGOU15zxV_ht8jBQtwhX-p6CuLFAFiBJQBcXxnojrQHRScryStRpa5qVQ-Y2nQ6Td157PbCdg35lWUt50TCA2bS0A_DQUUUDcDzILoVaDBVoXPFPjnjfHkvxNcDARBuX86mgahzJAup1SOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمان ⁧ جام جهانی⁩ ۲۰۲۶ کیه؟
‏اگر جواب رو می‌دونید، وقتشه که در لیگ پیش‌بینی جام جهانی «همراه من» ثبتش کنید!
‏پیش‌بینی‌ها از امروز، ۱۹ خرداد شروع می‌شه. رقابتی که فقط به شانس نیست، به تحلیل و شناخت فوتبال هم بستگی داره
‏اولین پیش‌بینی شما چیه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91590" target="_blank">📅 21:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91589">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICCP7iw8v2PHp-1ZjYAA_ej8OPL2Q0_86H2tHKixzHhbOUOjNpWE9N7jWOOPQhmJFjVhwi6gBR2-jAwuLWZMXJ7NJC8RvJh2oEAmR-7zkLPT2YXcEvMW4R7EQ8ovVly7EDePiLaE5d-iAEJbTjRDg6s5WFLjzt2uIp1U7HqxlrPsTT1_iYWu8PRmS_SQmYNaBGl9NPGOtJKBtCk_wC-03M20UR4BfdKwALoEW9wave7CJweLMYCI0PY-cmwG-OhNMdOuwlo76ABTZI57EMSO1Df8s1xzpjMx-tJBlqL-SMszeueADrjMrDQVgJUOasuVrX_q8642I2glVmOcfEEr8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
اسکای آلمان:
بایرن مونیخ در صورت داشتن پیشنهاد 200 میلیون یورویی با فروش مایکل اولیسه موافقت خواهد کرد
!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91589" target="_blank">📅 21:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91588">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYQMxBzbQhchUlubgl7TyeZGHpHgs1t-O5pcDVEIuzbJ1uP0ti6iQvX2HprcTztTNaarvkq836rfRhASB0TS-ZMViKUBtYs8y-16uRj15bKHeSIAZwCXYwX9Q4zgD82v19a0khzgZ1WdoGaVi5lI4iOL86FxM7ubEwCDs6nTNyTEOHOlRbEBTTwNeg2ZUPH_6TYqsg4TD4XbxmmUsVOWEhT_1C89l3Kj1J2fHdxoVTu2Ql9f2E0cFD_o1a6BHn7VYkWAarJVZjmRffdbR0fWphTAHf9bSBqoC2vwBlbl_PMdqkWd6t_JBSN4OVDKpHBqHHnzbHi4pP7EwRymt-l4xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
تیمبر به دلیل مصدومیت از لیست تیم ملی هلند برای حضور در جام جهانی خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91588" target="_blank">📅 21:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91587">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🏅
تاجرنیا و جویباری بزودی برای کسری طاهری و محمد جواد حسین نژاد اقدام میکنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91587" target="_blank">📅 21:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91586">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQAzSAoqKyxJYwKwrhR_D9jDEH8reY1z7mlRsw7b5fYyjn3HcVsMHJAn2xKVoyNmNIea2mLyF4z7a7fC6OXMd6Qv650G1IaLHbUmL3ZzrvqneK8wgCPZwJH_D6SX9PIM9CO4tVjjPR-4LZXdreg9NVZyilas-w8vmWKHOpg4PvGikJLcjxGL5p4542PjAwT5gHgg8gWRno7PW6xAthVa8PRpt_ZKY-5zmZYiELUFJ4SeocRYqaSXBsWCQBjKYaYTNC1zE-y0TJFqsAI43EHRTt-ivo4EW-_4K_Gh9nIlXqSDcjzhi5Q6XgiE9iKHXEPL-vw_dIpX8_rqcZY9lrqX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب ازبکستان مقابل هلند با حضور فیکس آشورماتوف و اورونوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91586" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91585">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2mM-Y22TbCMpG_sWrKYdoE_8nB9dRAWSthMPg6u-PRtjoQWfedUzgSOVx2VK3uq0uthCIph2XAR479O60g0oa1tv9Q7vGvvGpW8YsRuvLgH-Lc-j9e3o8QjMmBX-EXF8j7lag0anpB4_6GuWKlHVPgYap7csRwop_M7NXw9oUyG1gf6emOYSGPtuP7c_1pn-RlutcB_XU_Slr5tC7-XGIrJhdFqpEPxmbc4E3xVcuEomosFS6c-7OVxWn0YjUHvI04eugUa9asVgsug5RBuVIOfkdUatNpAnqwwp_CVUgx7niVMB7TmJIeBK_imb62CucfGihLwe4EDSndA-ShIzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
کارلو آنچلوتی انتظار داره نیمار این هفته به تمرینات گروهی برزیل اضافه بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91585" target="_blank">📅 21:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91584">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlnJrrhLIgfDAE3vxRxn_iPBa2SY0QC0KpQmV7llyLo92AHEIPQ58QcBlBocNraCfWu_BdYeviBDNG590LTpOmfaHh05R8se1glRT8sdDZWUlRePMW1f6Z_wRohIA1RwPKVjFMrHoE-nre4HRfYehU2vrXxS7HUQ8vscqnINQsFEE_JqpovDW63eplHYR12C6UOTxVQdY-eCxq53sgqhyf2YOcFuBir7-0yMP1RHLKHrCEC-02HCDVHacuAqgrP8MDB5L4gJ_bKVrBbTmw1IAj0Zg-9e708wouT-5K8e68GtKFFQiVCdEnTYO3sscYZ-Hqj58nIw6VEM-iCkEq6yJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنایی که بیشترین دقایق بازی رو در جام جهانی داشتن؛
لیونل مسی قلب‌ها در صدر
🫶
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91584" target="_blank">📅 20:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91583">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jos7uu4iLiL1ZCVPpb0w5OhzM23JG8NvrYMhOIlRU5UB6Zdua7V67Y-KZD9Gtfs_PnQs1zopE7EAayL9qANBmpDIwPbOU3ZGvVmAAVWT9j7sb6VedzU9pAIcRT_SqIX-1uAMVybdlNhX9XUf0ErgYTR-kUqt0NURDuILlMl7cVZA9vAcocgsnXKJbmP9bIWTzSGtM27GCasWRzns_lMwnDPqZT7p8EEU_XNy6LPspipjTLWe539LDSY52g8NuJk3xZriHSvAorJb9sdxIjXw4ENOU9z0dh_IQ9NCfOl0rLv3Pu7B2ogDAlhFqOVFX6ko5RSkUHkoqdImdFvN9TaarQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر سپهر حیدری هم پرقدرت فعالیتشو شروع کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91583" target="_blank">📅 20:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91581">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdfWRQdrlofPTGrjxNy55POFcNEi1hQ-O3hRhqpkBuCKkkOp-KqxRwUlvAuH2OEAnD093CVrNA4j9FLIVBDsu_1xOZxWzkHPsSINLLqxumhPkcsaICZtgz6OkNk6HDhPV0HwQp4mMLm7qu0uBbdcGyrYsPOtQWjXQ7eWaw-mzpk6cd035l1sFp1DqllUa-MZzP1VctBi9oRikezV77wX6Tm8Y0Uz_gP08dP0bVDDLkLYmtcqioZFC-MvWQ0Nt63J8HvTHv4zJPatqaUNsV8JF2DPeLjyHX0I-mSZ-SN3RU7irNb2yN4sM35OtwhWZoMA_XinQgL0T9oAZhizlQmzUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M9iOJkTzZGgyZlF_qKMCVeiDsTdv7jNP7lm6I8uCEBizKq3Q4QvbiaRrtuoYYfLfkqTV6laTNTjWDoF9gZgBRwdf8DVIMtI8yYoMA0cgd1P4WCOYsbHLPJ3ktVvYGl8VUecM6-yxoxX3aamsm0c_ySM-3YFI-W3sVt3Wasfds7SuSMmIuubjQ0GMNKM-XpjykxvKZHtVW6Rz3rfT0rpuObbu19f8J1hV08YV0z3D_LYn7AipZQiPYcE0YpFOh7CkFHQaD9kLVNAzVhPLyzi41IoQymLrabty2GrD00eHdd_0pUE54jrgO55LxUBQLyHEGKE0OcPJcTKXfEwCAePDuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خدایا یا من پولدار بشم یا دنیا جهانبخت تو روبیکا و بله چنل بزنه. واکنش خدا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91581" target="_blank">📅 19:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91580">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab5cab715c.mp4?token=cXw1wcMSbF0zswJ44ctDh_Mx5dfciKQ9GyNsYCR3aKYU0FiSMphf0jXMJnAUAvO-V1_An1rzUWosBvpqVAWyvaNmYcJWOKHxSRok7xUixfAd4lC0RIJkJKX1fsA2wCLP9KJ87j31ABc6RLZ7oIjYigYlNRR5HiRDCc70GCi-qISSZzn1UxbEPYU6ObEMIHGp2Pt4aBc4h6l6-Dq3akuG_DCrPywRSDj0P9IvSfwT5x1RDAgZULb6N6qscca0riffjK2TZgtP2scjZZST0g7i6cCtGzW4b6nut_Dh5aMj98lALQtonRew1tNzEg2X5K0t4bBlNPrwM0JrLeaLvxdX2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab5cab715c.mp4?token=cXw1wcMSbF0zswJ44ctDh_Mx5dfciKQ9GyNsYCR3aKYU0FiSMphf0jXMJnAUAvO-V1_An1rzUWosBvpqVAWyvaNmYcJWOKHxSRok7xUixfAd4lC0RIJkJKX1fsA2wCLP9KJ87j31ABc6RLZ7oIjYigYlNRR5HiRDCc70GCi-qISSZzn1UxbEPYU6ObEMIHGp2Pt4aBc4h6l6-Dq3akuG_DCrPywRSDj0P9IvSfwT5x1RDAgZULb6N6qscca0riffjK2TZgtP2scjZZST0g7i6cCtGzW4b6nut_Dh5aMj98lALQtonRew1tNzEg2X5K0t4bBlNPrwM0JrLeaLvxdX2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد مقامات آمریکایی با بازیکنان تیم ملی سنگال
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/91580" target="_blank">📅 19:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91579">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odm_lFGkwkjYIFmnsvfnM6UmjBU1Qt8lRMTTQSLA6L5XHSqAyvhJFq70QapzfX7lQ59upvzY7moVWGJRriwnfFaUBZGjPhypiH7uP0sj5VTrV781p9H8Xv6ZdaOr6oOr6WjLL5aa1WOnFA-Y-k8XLOPsSAujmfRdrnxanNBHn_1gtK2VgLWTfdP6NRKK3ZzszZqyvFNdsoLVJ6vlGeURjJATJk8LIuVxVSv9bsfiUf70sq4tcdz3nSSN1CwqeOIbGl2_tJcIKLgrx05hnui29gYRTut6BowGyGIbYeSqE-RIS3cxLQNsXmtVqT5puCXU6UwEfCKQ5I0okGa8R8vwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
کادنا سر:
رئال مادرید پرقدرت وارد رقابت برای جذب برناردو سیلوا شد. مورینیو این بازیکن رو میخواد و اکنون این احتمال واقعی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91579" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91576">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpWk1ljyd9PlDeBoCm7eVu6iB14_eZJBbaATyG3oDrLO1qPWXmMCGCZsP0Z93W495saqKiB-oRVBBuODDhG1jw0YoOv9JfOrsiE1LEyFdTHJSIZYRmn6jVz4WyYbBkKKASDw0_w6x9-hxBmPa_fLXTYqGkOgfh77SkUuk47AlLQHF6R68VFXs_aoYp5by2g9aVo6w4bzl7KNEVnHt-fnwX2ya8YnQ4vGbBU2CWvWqQL4Ubf_dM9GfYjFZKPINxfPRF1g8_AwIQtLjzg3phMiUeIp5hQ1Y2DFWLWpJIdsgfIixnN4GUQRY5fCmqs-i-KltAaRxvyElsULImiU4ieSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vJf1VKvLw9lN04SX5i6RN6UbE-yWeKTG2wWJdo5HGugadpdMKqMab_Uu68CjeBU2in0wU7nQhykdSpFduLh_KIhL_D3vuxM2tSronBoyQ4ImsEk9BOEVqtWtJwJ_2uSbIwK2aa-FGe8zxi_9KC4Os8WdYqh17giyGZtoIp7-OHczT5njAqZg7gKLBkFrpOA8st1pNKcv2dgJbNxpOso-h2Vk05GONB3Pz9U2NWex594jTVlGzc_8C_xC5pd_YCVDYzfJt4RrvYd21Ga76bmusvm-VoapR8MmI6_UG1sODd_FAt7eQRp-xjElGyViJuZKFAyCH7cKltnes-BWFpN9VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twT5i5pPNljtWtFNVc_m9H8kz40KNf0qyZQ7Nrl5IwSWLus9xWG93TMZHKx_Lthoq8InX48AoNmB6nATpTn85NP5QCMW8uM39PANjPHcqYQaSeVJdu9oP7n2vS0PbduyWa6aAcOVmZ5bkGZ4-CvQBeQ8CSVI8B6XP3U7Toh-CdxxR6LVF9zm57AebIuHfWVGP6KtYPwfH3oPtQ56xkWV-Sqc-1T8V4V5xApzyRWnKH9JByDOmtQ3xANtuxpspSFqSPw0j24fPbyoO4JkgF0LN0PXgkJpheu-SEcK_t5t3HXQV3KvK3x5MA6qs_U7WBOGOeEagyFeGbct7-j0EuQm9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خاله دلیتای عزیز هم که معرف حضورتون هست تو جام جهانی مجری خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91576" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91575">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfe52300bf.mp4?token=Yyj3sAROEfn7XlJHSz7HWVvpBC7Wb0LNCXmk2pmL25gNV3JLJOt9_3TgS84XNYTAaEOxRvDIr8mm8RTdGT46G0tQnx43O20BWpvR-ZUISo6QyyqeZAZlDWkA8xvkksY3UqSvrducKLWqbHKOu5Fd1BxnPgCiLtZ_7rNrq6gfI-3rwNg86lFRVlloPbdpjAkNz57b_ijNAihcsDycA1jig7ULxpuBpdDDNjnShNK4yL2_vWeLz8m7rngfDT67SeOciR2K3S_i_iX1yeUcbZYgU6VWLhCE2bN0Xmzr9gQaCQrONVN8qbjVC52j81sV6W60S7KoWPZqZsNqMeXZGZ0BuIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfe52300bf.mp4?token=Yyj3sAROEfn7XlJHSz7HWVvpBC7Wb0LNCXmk2pmL25gNV3JLJOt9_3TgS84XNYTAaEOxRvDIr8mm8RTdGT46G0tQnx43O20BWpvR-ZUISo6QyyqeZAZlDWkA8xvkksY3UqSvrducKLWqbHKOu5Fd1BxnPgCiLtZ_7rNrq6gfI-3rwNg86lFRVlloPbdpjAkNz57b_ijNAihcsDycA1jig7ULxpuBpdDDNjnShNK4yL2_vWeLz8m7rngfDT67SeOciR2K3S_i_iX1yeUcbZYgU6VWLhCE2bN0Xmzr9gQaCQrONVN8qbjVC52j81sV6W60S7KoWPZqZsNqMeXZGZ0BuIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیمار؛
بزرگترین «چی میشد اگه..» در دنیای فوتبال..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91575" target="_blank">📅 19:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91574">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde175f21b.mp4?token=JD6BHoI-L9fa7zgkCSPfP9Y0DH761Ls-pe2R3QiNE2aUAuAQAg9R0VJ4p4li6jWKZ1OXPE2H2GXgRF4kacLRA9aTyQgXM9alXb1d66XttaFUSJm4O6WIy4fEXkoRgePwtsufpBlmncVNtDWBanEx-2pY8OoVVfGKoWjsKLP7DHlL8C20KrRhmTUI0VwMXHxKgHTVsw_EOlmigdpzBE0qGyjHup4Jt1R1tI8isxSmKN4Q9yGrhf1dU7lEULjUZ6NfMoFwgfpjeNfWbCL8EvsgGQGkxgGrk97xyvaqkSU88UVc88Dy7et874Z0NRMI3GD3h3cQyhUAJUiacuxcvvbRJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde175f21b.mp4?token=JD6BHoI-L9fa7zgkCSPfP9Y0DH761Ls-pe2R3QiNE2aUAuAQAg9R0VJ4p4li6jWKZ1OXPE2H2GXgRF4kacLRA9aTyQgXM9alXb1d66XttaFUSJm4O6WIy4fEXkoRgePwtsufpBlmncVNtDWBanEx-2pY8OoVVfGKoWjsKLP7DHlL8C20KrRhmTUI0VwMXHxKgHTVsw_EOlmigdpzBE0qGyjHup4Jt1R1tI8isxSmKN4Q9yGrhf1dU7lEULjUZ6NfMoFwgfpjeNfWbCL8EvsgGQGkxgGrk97xyvaqkSU88UVc88Dy7et874Z0NRMI3GD3h3cQyhUAJUiacuxcvvbRJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوریگی عشق بارساییا از دنیای فوتبال خدافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91574" target="_blank">📅 19:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91572">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJaLo1QqaaB0BOlZ20JfVVcvoF8GSf2Kvo-zclHJprEvkmx8A76zJQgB1jIAh2qzV9RgCcS-34YmRe0_lakCusfwzRtX9gXQSRZq8O1TYYDXXA8ezaEhsGBQJfRjrhMVRNcPq3Z_MJEcNnSUOQh471jDHB79tX5a9ZKuasEL7FEdt8H8zyTR1w7NfdzrjtIihfXVlJ8JeoB2SmunTngsiCUMLbdmRn6YzDvqRZl9S7VlUi3mInGRLf3sxyU3KxAvQda-8Vn_SAruTE9qGEoFc_iDHye5mDN7EeKzS63bbgEi6-N9V1e1Z52s7cIMxYqg4QhXkw3QcLioYapdXDEAvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PbwBFv1kfH_5KFfEhlsEw-tzhlDzXQIiyOweMUtb_216HfctYRIaQOqslXiNmFhXDCYCQW57RV71smpiekhV5mx_CsUddpySHtsWCRNw0Zm0u5Vwn-SPytFo7Qmyn3IugdvMuUvVjimJKZBivzTdyYIdYyCQJWtnwdpncSBAiSGaDT6QoTZC0HgoRUpDyXtGv5cRJRgSYe5S856uS7keezrrJUVdL1p7VouiZPwJmSvMCICyp9Svk7XPTTanvT9PPs5IChVoYG10fzoqyh07aR3-Qu-984skI9qVulWM98axHZ7JiBKtlmDMUjidsbv5Bc5smeh6NkfMHpa93BaTXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اوریگی عشق بارساییا از دنیای فوتبال خدافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91572" target="_blank">📅 18:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91571">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/My-DJG2rNW3OXfHDcLWNGTW0pAqUeEwaYeJkJp5DkV6gfKXLxMPFMiQVx18aeplorh3nKKP6Mo3L1CytE94zR8DRl-6vR8oeCkGxdF52jkGPetzQ00plJ_s34sSkvqpROjE7ydgIaAsHo-1LEz1SqARJiP6yJgGMbHlQf7L-GfftNHWfW46oNm5GjE_3o7fZbJZKNoYWrEQ50KbDKGdxco30Y8FiStUz4neFbr4ZbbS15TCRp4qzMLt-khdtWdM72qi8J83C3KD445yH7J4FsiODbNpZewMUcP87ZcDufw_g9MhixLGe59sVIVlTqbsxD8cmxrO3bfETnPnkI5bLBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کروس : بهترین بازیکنی که در دوران حرفه‌ایم باهاش بازی کردم بدون شک کریستیانو رونالدوی افسانه‌ای بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91571" target="_blank">📅 18:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91570">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7s_oU5uTNtnWQOdd6bXTbNaSKcBRs-TxfEQnQHqfeWM23ia-nCq4E_YUDrYwZn04uecChv7M6_QjZpN3TJA1nV7tL8UnNk3l_87KVB7NiKQbsHBqSq4ZjYWF4oo1kp9iA-7N6bhA0Y1R6735CYMbtmRcen_YdMYlybSpsZ8nFlqrmG0TSAg8uc_BV07N8VdN98uzTP-HFVhp0NASNM6JE7j3nLlq4uIBx8BRkeEIwQchXzVb4LSqcsOGuohd9ojzy22i_E5Ogfq3xs1oYeN1U6_YL3COb_bPiNRvWRGQF2wJjJSvIP0L7Pvq8ugF-YrE72CMcAJGtbUuEJjRxb9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
دیلی میل: چلسی ۱۳۹ میلیون یورو برای انزو فرناندز میخواد
🔵
مسئولان چلسی
میدونن که رئال مادرید به این بازیکن علاقه‌مند است.
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91570" target="_blank">📅 18:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91568">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0de371fc06.mp4?token=lc2-sF8vPLkWWGerzWRyYwlfi4EB_7O7yMTOwiOjLHwIQgkNuych3DmCxz8Dhz9RF2T8_VS02Kxbk4WlpUoqQv67re8KfNN_0NN29d0AOZHRHNnEWpIBXX-ZGLSaAD079APJOM3ea9hbsKc1Ti7IBqkBc2Up3CH4l-H7HPE_yjmsoPW9ksbC_SS_Wyldi6tAMmncO7Mo_Zj2c37kgrIRkbPJAPSbtkB3ikTR7GaYUNanLEjntODWYqvsguQS0hGMJzQIuRCHn1uq1xTrdeW9vnpjnSf1TDPN5yNHIm96nPdPSsraodrVtgYK77t-RuvgW9v0y4hcpi2ObRUVJmdSrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0de371fc06.mp4?token=lc2-sF8vPLkWWGerzWRyYwlfi4EB_7O7yMTOwiOjLHwIQgkNuych3DmCxz8Dhz9RF2T8_VS02Kxbk4WlpUoqQv67re8KfNN_0NN29d0AOZHRHNnEWpIBXX-ZGLSaAD079APJOM3ea9hbsKc1Ti7IBqkBc2Up3CH4l-H7HPE_yjmsoPW9ksbC_SS_Wyldi6tAMmncO7Mo_Zj2c37kgrIRkbPJAPSbtkB3ikTR7GaYUNanLEjntODWYqvsguQS0hGMJzQIuRCHn1uq1xTrdeW9vnpjnSf1TDPN5yNHIm96nPdPSsraodrVtgYK77t-RuvgW9v0y4hcpi2ObRUVJmdSrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
هیچوقت این‌صحنه تاریخی از لیگ‌رومانی فراموش نمیشه که وسط صحبت سرمربی یه توله شیر میارن رو گردن مربی و همه خایه‌چسپون میشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91568" target="_blank">📅 18:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91567">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Liro9BE52t_kLXDZpMXJSiKdpeZOtqtNpeL8guKHMxFmFOH3eByitfzo-x1s5lH45x4U9wjMB3zH111XNsQGnvonrZZ093CbBOmIiLN4mU6PRlt_kX7t2i60k83Sz9cw5-bqQgQk3RuEdpBBjAS8DOjNjJCz70pgiBMxkVtCxMqHj7WFnZGtWY2VE6ZqZ1amG84hA_outIL3E7OSnLXNngV9QQF9bN6LnP_SIWCRr36uxwjnxCERsOtLN3NvwEffHOqeBS3jVpI7brNU-UGLWDFK_OdiYbufOFMC0YtJgudk874uL1yfe4KPD-ELao5tgFKGmVpZqE1jvbKLgvGkLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه قاب تر و تمیزی حاجی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91567" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91566">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/585ec3a1b4.mp4?token=PXP1_JkGHXP5EDsHpNcf1OX5xvJzveIAjMhNHuCz0zbC84HlldY7igQt9k4fpXFv2EhrytYVn1YrmKWXGCC-ZmioCN8EXfWl0_suNtTHpJuMnjcSXBdG3OcZxcLL_QvoUzHzqpZuH6Z3qfTzPiW8aQOIEDfVBYxBqCkNpTf8woj6VrhgRr4Qf-L_ug1Qwh_gZVk-GvR_H927Khh-zi1B2icVWrKwvdn7M17KfisaBF-bDilLDWvYyRE4sZO0qQFJuhJunr38yLFWO78XWI2Z6w-9gb4gu7fEtJUYqVNBhXLWgRMCN1qZBR3aXFOfl83UkLqym7Bho_z0xJrKGOTaog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/585ec3a1b4.mp4?token=PXP1_JkGHXP5EDsHpNcf1OX5xvJzveIAjMhNHuCz0zbC84HlldY7igQt9k4fpXFv2EhrytYVn1YrmKWXGCC-ZmioCN8EXfWl0_suNtTHpJuMnjcSXBdG3OcZxcLL_QvoUzHzqpZuH6Z3qfTzPiW8aQOIEDfVBYxBqCkNpTf8woj6VrhgRr4Qf-L_ug1Qwh_gZVk-GvR_H927Khh-zi1B2icVWrKwvdn7M17KfisaBF-bDilLDWvYyRE4sZO0qQFJuhJunr38yLFWO78XWI2Z6w-9gb4gu7fEtJUYqVNBhXLWgRMCN1qZBR3aXFOfl83UkLqym7Bho_z0xJrKGOTaog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
نیمار جونیور ورژن برزیل در کوپا آمریکا 2021
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91566" target="_blank">📅 18:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91565">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a249a370c.mp4?token=E_dO2Ogn2twg-U9bLfgX5kVJOgbzVfKkfF42IBeYeGxTF-3CwRH46VEs9Ne6UFY9WjvLIen8LBFwic0otscuUo6s5puKyKPNAOQ679KndymBQuxHLZ8vRwpJEA_LKSo4rJ5ZmajDeXX8EVaWKkURElRA3AmInY3jvQq1bE3ACYyHgoeEQfFuVzZ6ukrzBQ6wTS-9UtQyvmWKnUJ0zGJAmfy92pFs8t53pjfPrgWHjSk_w1a5WbWWqMv7_LtwsqVeLQa9aC_PMQHBP1NpjVPPudnffL73RwGwetvAlr1_WkUsNYz-xw61w_Lq-OHlze-LLdmR3y-6snCI7asb7jFtjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a249a370c.mp4?token=E_dO2Ogn2twg-U9bLfgX5kVJOgbzVfKkfF42IBeYeGxTF-3CwRH46VEs9Ne6UFY9WjvLIen8LBFwic0otscuUo6s5puKyKPNAOQ679KndymBQuxHLZ8vRwpJEA_LKSo4rJ5ZmajDeXX8EVaWKkURElRA3AmInY3jvQq1bE3ACYyHgoeEQfFuVzZ6ukrzBQ6wTS-9UtQyvmWKnUJ0zGJAmfy92pFs8t53pjfPrgWHjSk_w1a5WbWWqMv7_LtwsqVeLQa9aC_PMQHBP1NpjVPPudnffL73RwGwetvAlr1_WkUsNYz-xw61w_Lq-OHlze-LLdmR3y-6snCI7asb7jFtjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۱۶ سال از این ویدیو سمی بازیکنان تیم فوتبال منچستریونایتد گذشت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91565" target="_blank">📅 17:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91564">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX89DumnurZk8mDE9eUF9gGzjW5kRX3o5hUG1X4EY6h1jUnFLFuKXg4TM_BWvv6OvjQc_qo2oR8S5wwxls5UDiLaxRM65dRyIU38_iY6zvRWtB36F_-jW-gNsmGsWW2bUKVFdHE5kmPsGFKt6zyRdkSeaSB3GhNpkqEiOpw4qI3GbQ8ctB3Cocd2khrbCU46kyU8Xi6u0_fb7eDqZjmwG2g__qrDombi-XSvkqqd_RNiry1PdIkJlKwPBqo0mi4pg6AZNnDzr4yumNvoLgc7fLZJeQLVzG2odfKseuq0EXYYYQOOc9QGqia6IjfhIxtFHJRxzv1q6n9tTmRLpAcEpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
متئو مورتو:
روبرتو مانچینی در آستانه کامبک به نیمکت تیم ملی ایتالیا قرار داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91564" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91563">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89d3e3015.mp4?token=NeytpdKkfKid_U1QNn--o8HWth5n2kmqMYkpqRIfMD3u6JHQ1lXvvrHeog_nNeLEdh9FsVDdtn9x_Y0gChTupqCRz37phiD_RATi28DB2lXi9QZkd1Hv5AEj2x6NddZlAZ4MH_zN54BbnOvo7yW5sOIf7FTav8DrP0IhLJwOUjyWlLOR124dU6K1AVlnEi-zq8LVgqCBNd5vX6bzwnHSE1ckrMWhBa8FlSt4wFzz2SAJflkHcvLVT0Bwc38DOB9vQpw2qIEPlVhWQuW4XrINvn4S5X2D2MZxtnRhgUQQOc6LUqMxPeGiAlczbCV4lNiqYXKQi2owfHqW0VpWW_NBUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89d3e3015.mp4?token=NeytpdKkfKid_U1QNn--o8HWth5n2kmqMYkpqRIfMD3u6JHQ1lXvvrHeog_nNeLEdh9FsVDdtn9x_Y0gChTupqCRz37phiD_RATi28DB2lXi9QZkd1Hv5AEj2x6NddZlAZ4MH_zN54BbnOvo7yW5sOIf7FTav8DrP0IhLJwOUjyWlLOR124dU6K1AVlnEi-zq8LVgqCBNd5vX6bzwnHSE1ckrMWhBa8FlSt4wFzz2SAJflkHcvLVT0Bwc38DOB9vQpw2qIEPlVhWQuW4XrINvn4S5X2D2MZxtnRhgUQQOc6LUqMxPeGiAlczbCV4lNiqYXKQi2owfHqW0VpWW_NBUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اتحاد و همدلی بازیکنان اوکراین و دانمارک در صحنه بازی دیشب و سکته اریکسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91563" target="_blank">📅 17:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91562">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEwh2G5FL25iOcgSDxkaI-gZpq5bauTNMe9QByRfBJGDBNO1ObfxEVI4eL_S6QrC13TOaC011FVJl-ewYfAdNbAkjmhNIninOf5u1sPGPO-oB8q3cJYwQolj9hS3oxfp1Ts9lLEpzufeWRDNuI3twR27nMfy6C4TuFSfjKrNHProovKShwfpRwVO7TrEGFnx8vTpX3dV6ur41QCzgn6i4vVu676pwF1r-IqTFH2HXOKZ22zm07N5maFvNgWxJmOQEnALJDvorH-QQ1cbT9k8dfEE8AUiuGS21bbLbx51rgLPUuabENKsK75crIO2rJi0maCItVSrkdxkY1fGcV1mNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام ۱۰۰ میلیونی، از اینجا ارزون‌تر درمیاد!
😎
💸
وام بانکی از اسنپ‌پی
با ۲۰% تخفیف
خرید اشتراک
📱
💙
✅
تا ۲۴ماه
مهلت پرداخت اقساط
✅
بدون ضامن!
ارزون‌تر از همه‌جا، آنلاین وام بگیر
👇
https://l.snpy.ir/aqijh
https://l.snpy.ir/aqijh
https://l.snpy.ir/aqijh</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91562" target="_blank">📅 17:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91561">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7cfe2ee7b.mp4?token=u0ir42FENlUDpLQnFQzZ9wxPJdssEfSweeGm6LCm8C6sTlRWk1yGoI7mTngEq5fFq3i7rInFnetKq-5suy46-ha6M2boitadE6rc4xKm2jHhBtp-Soq5vgf5ttFZ83X_XEzvDI11u9BA-cxZ_kZ0AcArjhkW6eLbeFQJ7lMMydE-MZ5VdDiEr2QBymk3vdJEf4fGHeEhSRwjQfsN-E2Bi0eLQ9D929IzICa0KaauvB1sGmbybfHQgz5byqLOntjd02EXNoN_J191b4i3VBebBNIkL0u8SIBiSCYzpN_7WvH5c3YSyYtv9mtU73DiPg-A5Y8SkENxyauRLysaTGtdzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7cfe2ee7b.mp4?token=u0ir42FENlUDpLQnFQzZ9wxPJdssEfSweeGm6LCm8C6sTlRWk1yGoI7mTngEq5fFq3i7rInFnetKq-5suy46-ha6M2boitadE6rc4xKm2jHhBtp-Soq5vgf5ttFZ83X_XEzvDI11u9BA-cxZ_kZ0AcArjhkW6eLbeFQJ7lMMydE-MZ5VdDiEr2QBymk3vdJEf4fGHeEhSRwjQfsN-E2Bi0eLQ9D929IzICa0KaauvB1sGmbybfHQgz5byqLOntjd02EXNoN_J191b4i3VBebBNIkL0u8SIBiSCYzpN_7WvH5c3YSyYtv9mtU73DiPg-A5Y8SkENxyauRLysaTGtdzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ناصر الخلیفی در شبکه الکاس قطر : لوئیس انریکه به مدت ۸ ماه پیاپی از مرکز تمرینات باشگاه خارج نشد او هر روز از ساعت ۸ صبح تا ۹ شب کار می‌کرد؛ تا جایی که نگران شده بودیم مبادا از شدت فشار کار دچار مشکل روحی شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91561" target="_blank">📅 17:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91559">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uyqW0oZJjnX3k4Yt-vt1iy_pxiYEZ_DVkDUNWmV4VSylnQjeBDIhu3Z0eE5mmxUaNkDdwVVpecGiFIBA2CFBD4GGgOY5oQWMkjIWGpzrNGxvyE2XdzF1tnIFMHbPsXCSgZZ_u3ki5ZZhTS1D6o2uyZ7-R9qujdLD1kG22MkmJZ7gXzJeBHx18LlfevTZXqBfC9QTWqhvTukW-AlQ7KiG1CROIxFElmEyzSoQCywFnUa4B7RiIDiUUvI21GnmL0Y0JxONs2wWhWKBIvAPCPURFbudO-LUciNhQrronPleheIOr8Dhxg_PPPAJXZljO2zmopsQSdENxy2nMg56Y2-xmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ci1N9d8aE5HFE9IZHcD95HkT9VMduKyMopnUB-faWqoWbCvvuvQDf_pGhaQaw0pmyCXQjZMmZ-SeONlWmbqw6n_sQeqVyu8VGwunq0qdEpHOJWTD-0eB00ahfA6kfMEnew-_agC1J55-B0UFSQSnqAHOvCwoloYJCUbVQ1jipGLu02JAz2e7hcMf3yygdIp6eugo0kiPlEcwkdcvEE-jjlBV6lWcTyeQXAA97YKsMHEIRG0afAuDhllbG0UcQf6Kt1TmaykzIIz3ooMA3pfHx22DbcVEaJqaTw50jYHKSih9l1Mi1wqGzQ5EBTmhNT_94NUUwns_LzzCp0Bot47-Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خاله وندا بهتون سلام میرسونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/91559" target="_blank">📅 17:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91558">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgjThKg-cwryqER31MTc6R4s87D1cf5yfSHbUSY37aDJe4zYFjmls5zV0hyDh9zGHIqf6rMwsNhXb2pnvpiYjkvXyZg8YQGb9JGpsekIpkWurmQ7rDOYD763Snl6QO9tA3bpOth3lAKb2OwTcMRGnG9_Fe4c_4DHW69haP0ac5mH05Llp1S2GqqYvHxfnXm4jDSKodlkNVQuSoEDZ57rgn-VPB9lx-RVh6IqlFOc_pMdWdmYzRp0O0-QlY7xgyKlpwuPSCF47WIuct1jL-lDQYwNploxEvz7w4U_xhPljlPEtvYdzGcygZ8_5TT30C2V0T1MQbi7AAtN_mJkwtMgIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
سانتی اونا:
⚠️
اولیسه در بایرن مونیخ موندگاره و به هیچ وجه راهی برای خروج از بایرن نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/91558" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91557">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2681453adb.mp4?token=dEjr89wtTeX6A6UNbmq6zhc4K2oIz_9AlboPFXEed0iQPdwAMjbucAaJvjqGR_qjTlK-X2fu5tbKR8jrlnSKj6jZ9iUzuZLn2kziwq2iFDxsYjnxl6tdshS39PzCHqs1Loel54mp8WP1ve7TsMaHB6DmYWMDtoJxHbFpyasJ58_IEc9Ef0P1yaT6dYO2xDa2-NCq3XYq5E4M2rv-6oOYSoCtz9IXDoyo9cVZQHpuV6XfEthGeQHGCOBd_eHLqjoMr_pcgRwHpwS2tHqGXwjdrDuuHYMO0571t-flugl92u3R2x3KBDiQiUBF99up3RTiLuVy7iLBvMz3E7NRkUeUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2681453adb.mp4?token=dEjr89wtTeX6A6UNbmq6zhc4K2oIz_9AlboPFXEed0iQPdwAMjbucAaJvjqGR_qjTlK-X2fu5tbKR8jrlnSKj6jZ9iUzuZLn2kziwq2iFDxsYjnxl6tdshS39PzCHqs1Loel54mp8WP1ve7TsMaHB6DmYWMDtoJxHbFpyasJ58_IEc9Ef0P1yaT6dYO2xDa2-NCq3XYq5E4M2rv-6oOYSoCtz9IXDoyo9cVZQHpuV6XfEthGeQHGCOBd_eHLqjoMr_pcgRwHpwS2tHqGXwjdrDuuHYMO0571t-flugl92u3R2x3KBDiQiUBF99up3RTiLuVy7iLBvMz3E7NRkUeUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧑‍🎨
اثر هنری جدید حمید سحری: تاریخ دوباره برای اسپانیا تکرار میشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91557" target="_blank">📅 16:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91556">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj-M12RtLJL9Pzmvx3fTPlh2IMrHETo6l2d7U4dFSt0Dijcq7mBmWrUIvEXBIIQ84qC5DrMlBUoMp0aCXU0-t1xKFYPr34KVJsHImvKuVT85LP_pjRFKkthpR4e-F_1IkaDNbD2HDQbYxviKvMwlvOso_CohaY77YGcxcLpeUk4CIonzavMupXias7nRsPC7OkTRb81BMpKn4Tb3cgLPETyYJUEmLphFbzrptifr8SBpBYuVqf7EJCXaO-NjzVRdWwglJqAHmv0P4_tNoBKHt60HM-VsVDN2OSq52hbxfVd2CH3FuE_mA40oWO3MA486GFdUOTxV9g3B6xV7Qp9l3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زین‌الدین زیدان:
🔸
قبلاً بازیکنان آزاد شماره ده بازیکنان باهوشی بودند که بازی را به شکل دیگری درک می‌کردند. حالا همه چیز فیزیکی‌تر، منظم‌تر و کنترل‌شده‌تر شده است اما فوتبال بدون شماره ده شعر و شاعری‌اش را از دست می‌دهد. فوتبال بیش از حد فیزیکی و تاکتیکی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91556" target="_blank">📅 16:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91555">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
اسرائیل دقایقی پیش جنوب لبنان رو زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/91555" target="_blank">📅 15:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91554">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚪️
اونورم سانتی آیونا گفته که رئال مادرید به شدت روی مک آلیستر هافبک لیورپول کراش زده.  امروز عجب روز نقل و انتقالاتی جذابی شده
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/91554" target="_blank">📅 15:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91553">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6zoNTsf9VluKWFTipxQRBpmfD4zFe8qqODYsf125r-o1SCwMQaHFGeaUOSgEntgQfP8NZVAtPizaPW4GcyRapssKj40jGsFUSLJYNKmmcFgszeYLC5KfhGWZbwK9ii23L8iOZzec6ZRr9th_WYKUf5lFnUhsuc_szw4jZbT8ugrdKv-6SJU8TKO1-OZFVzLy_sbA9V_hF7uysIrtJ5ueuS4yygKLjzcgfGymwxi5GUj2jSyztrTKlGeEh5ogFiY2_yGBkCjpP0s9b0gsIG-w568STPIZ7nHZCfrZA9cFlyXCjutQCBttC7cgbaoqBoyMkknk9khRCiCfnQ3aXdyQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‼️
دونالد ترامپ : یک جنگ دیگر را پایان دادم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/91553" target="_blank">📅 15:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91552">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJgWsfwXpNCq0LAfsygJ_ChhYD1aJLHANE5Zo-glJbu9IQXxIr6K_wfcZLKk7_kCXkp3BfhxvbFIhTKcUgty_JJx4nTIlh7SGkaessWH4gV4JBf80z9Z_u3F9DFEs7wht5lKo8SZefGZ4GmXI8XoEmPMijiC8eQGZQpFCgICmtSJTHWo27SCfiVsGyqe_Ra5DU0GMqHyJGNb0wHC4epOUpnPIFZiwyK1mlPjfH1_THAE5aUiX02SuiLTMn_wHJ_wodtX_V9MaOlW7Rit24gLscfH8MYtmdI8QrF6L9n7EJFE1NdNtWDAcMHH9gCDK8pniqp943yZpfqoUSuwX0NT4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اونورم سانتی آیونا گفته که رئال مادرید به شدت روی مک آلیستر هافبک لیورپول کراش زده.
امروز عجب روز نقل و انتقالاتی جذابی شده
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/91552" target="_blank">📅 15:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91551">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOFpSfj9g1PnzzIjuQJaOCZONZgpLTxYE2SoSbUctlKCkFOMo4uQYE1AOi2QjqDZar1GvAt0LPG-GG3aPngNQgM6anrxsEmrqmwFJnKyVYEDHU3cf_QhB14zeNvBzOtgb3dfimCnSbhjajUSa0WbIMHuI3q7V7v8bb6ipry7AX1n5CZTUVO4xwNgdo15WS6IG16G3HM0psVUWcr5VNfQLdkw4t5pWqMXcN3GrSouLs0p9UoZF9a97xqGZLBiDH7NyW-Pfi7cpp8GEoK9pQMJw0cUbxwU-WDfnhJi8cJb_Wgq31EiVWaePEg0SGUNnrCZDqMItvD0Wn5aUFV3z0F8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خوزه لوئیز سانچز:
به شما می‌گویم بازیکنی که ارزشش ۱۵۰ میلیون یورو است و پرز زیر نظر دارد بمب است بمب
‼️
کاملاً باور نکردنیه و وقتی اسمش رو شنیدم بدنم یخ زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91551" target="_blank">📅 15:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91550">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPcZSddCWenWi7DZ1PCnaiFCqWug9mcKe9M74usGw6w8TQtcQJt46EWqCq-Z_jdmc3pExAEdMJVHobOID7cIT2U1rFe0kvW6SHd8lT6AVhZfEy_QGt6LHO9QWFpSlg5uh0EJfyyJScyDCo2kiZpKETJv92REgH3x1agWEQ9Ix17Nn5VWylri8TFopOVeIPOPcmrQc9-tnTlaUxxmhlAchAIVwA4x4aEK-iWXvU5jyNhy6zPVJDAiSmIyL0u3xUZGk44_9BE9gt7Th3P-O9f154qy5Jl3RQn_va-VFAf73Vw1yV4jHa7pr-Ucx44PhPs-x6sedEN_QWnHgs2WnEJBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
سانتی اونا
:
⚠️
اولیسه در بایرن مونیخ موندگاره و به هیچ وجه راهی برای خروج از بایرن نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91550" target="_blank">📅 15:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91549">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/as73fMedWbyXdo2Gzw17_9ewT5HNAz6e6mRA56JAW26f_qQSFwCqSp8VLJeS2ENuEISrcHUBAINi4HDqrlhEze5yIt9BMxln5WN-Kq4Zm5BAa1qaSCPxFPha-WCGdXVmGkQWelF890rVoMWHig4bzfz-1GoN3EklbWYDR9YVEBkUjiOv6ufZ1rlBzU154FbA9RfXrqabhQnkxYt4Th88YrjtmYjmgFsjoJUh9LWsaTrM0m46PGPQO5XEAi9aaWb1WeE8fhDbvQA_Ys91H1FBF8RdKkKGu_aGCjusTLWdAxDSw2wOa0EAWhGP_lOFy3o7AR_WbOqUveRRE3352YGlqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
جرارد رومرو:
🔺
پیشنهاد آخر لاپورتا برای جذب آلوارز: 120 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91549" target="_blank">📅 15:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91548">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
‼️
دونالد ترامپ : یک جنگ دیگر را پایان دادم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91548" target="_blank">📅 15:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91546">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knAR_dkzmH5-DqafQS539I5eBT8lGSyg4UrcaSH5YiYz7ah4Wqs3U0GZWAR2SDjNGqjeHdP8Td3B2RDF-vfXl8l3O-o_YgNksiM0ODYOZjow4c9ap_5ud089izBz8AqCOaG3piACQBQbEtK9tjrxZwooP3o-RmSoyWfCXZsSxjymlI5z-Dver46qLJYK1psN0fAJh4ZWr5i03j48VgYXgeKIdGlLpLbT_82_xVGoxu9c6K8sZeNzAcKad4g3BoUmfZy8X5-Un_YoIc7CFcdPBonmY10J7XqsbIS6nPcJgBg3L7m91zQdN8472FOkBtFr63SGdxdpc9sGaKrfp5fz0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qejDbSoB85Zwu0ZsSSr5BehJ7zOcn7QOirLFQWbl_lNp9wUVzys_GogRM7PTFaGuEIsYOQ0yLWp12RqjEKtosa6LHmONIbULn5h78_cpVZRIDghj7nGbwuewsKf89kbVC6V1aOuTdGpWS2A-Hj9jcDfqhwYO3pbCgKB4nEtVFu5A9bCxkrNGwUri8hp1jL3GX71qJZmf1FJ5CZqMkuWcqiD6oqSQCADXq3Joc3ehFwVt3s5-QAjEdn7fAuzsWkauGsTeGqYt9AQ0PzYuOIECr34EF1wOJxPGXFbQ1N7hkts0kSI-KDA1_Uf4Y9wUi80q89_GHNneheRsZ_YdlBSxIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
#فورییییی از اسکای آلمان:
⚪️
رئال مادرید آلوارز رو بازیکن ارزشمندی میدونه.
🔴
اتلتیکو در صورت دریافت پیشنهاد 150 میلیون یورویی آلوارز رو خواهد فروخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91546" target="_blank">📅 15:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91545">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfpiTm4IX6mJ5IMG7JPeuQdjwkvIdazFne_EO5DxpyMFPCLy7yLP8kpBO1WgbSFHIwJWnS4N9e7m1P8fP-EYpo7lNSIGiauxg3O2x-vCbho97eivtBGKPK4a5_OxlHSU22MVEk9SK1dxLx8FuKllRUNjJ-ny9rYddZOL7ZJvj9Sln8E9IPv8BGWQoCUDDHJT6ezigbbJ499BAcKRkMFgLoLZ4N0uBhiNGkkRDSjVftln5En0TS6Fe2jFEbYaD7j-SN39nuFiIVJaek1BqmxzAOWPY5REszocCHATzGvQQqydM7tvEqkHyv5sU5Fon5Tbigu3uVLII-K198AtoOqZNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فورییییی
از اسکای آلمان:
⚪️
رئال مادرید آلوارز رو بازیکن ارزشمندی میدونه.
🔴
اتلتیکو در صورت دریافت پیشنهاد 150 میلیون یورویی آلوارز رو خواهد فروخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91545" target="_blank">📅 15:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91544">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh5ZhizS6Kxylpm4SNruMElI2rTH3ZcL_jRFCLBO3o2x6ySQJhApVZs1u9LYwVyisaQIOQUk1odyx0dDN9AWLsNyVCq5mPoLWpHO5QhBPjN1mgaOtgNQcJPfVTx325kIzjqHJQfSJOA3-_APjmBQiuG-ot_wCgxHspnQ93xQGInmIA6YHv5KpgxhPmNkFU3sZy2spiG8hX_L_XB5lBXRwe7Z25YMQ9Y80CW7NrtNQJMcpozcbIgDmR-afUElcVBv-L1jbyYbC3UEKIEcyeasHf9Jz-WXZAM3_HvGwJrDRvbsB7gHNCB51i_2zZGF_OL28OE5apoZcQFre7n0XeoCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
رومانو:
🔹
من درباره شایعاتی که آلوارز را به باشگاه رئال مادرید لینک میکنند پرس‌وجو کردم.
پاسخ رئال مادرید: هیچ نظری نداریم.
نزدیکان خولیان آلوارز: هیچ نظری نداریم.
باید صبور باشیم و ببینیم چه اتفاقی خواهد افتاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91544" target="_blank">📅 15:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91543">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U3jNG8-nCbGtEbnoPrwVVVOeV0003jFsVXfXQTQWga7IfRGMcVQsC5xHqq85gTQ30Ju03K7m8WXud_wj4Uzpbk8WIq6g5h9IS4jzcUKXSL2GlI4dFmF6g2dyF_14gua4S63CkYoWYCu_qozCN6XRc9CqnN57qEVwbwi-fqQJ9I5yvUl3qN5rxp3p8eko_Wr7iOLO0RPh5-TLS41Q8b-jVADISd7p0cYwyOjjbCAvm-YeNhSgANgUrHmqpDe7EXi_Lk9SZbH2dIk_f1jAKGtuvCM5mB23V8Yc0V-c53GWRp5vs8E7BHg1M-YA3cYxo89r00Tiz4DB7wy9Mpt3kdTNfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
رومانو:
🔵
منچستر سیتی آماده ارائه پیشنهاد جدیدی برای الیوت اندرسون است. باشگاه به نهایی شدن این قرارداد اطمینان دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91543" target="_blank">📅 15:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91541">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaiPiANX1iK8KyhoMH8lCL9w4B8lwdhyU4Tq3TX1CtIlOHq5HFsq7_Fm9Zd67565MDlmojyBzgHWYjJMSYZf7-p0YS8ErlGBECkRIFxO3J_awa4s6zJjtUCqr52SHICUBTfzrysM_v3oMk4QzwYb6G3D__ay-ywi66rrcgZXedDI62hNMDWSC_PYDbx9YAHUXHGt7klcfBnB4ohwI9O3l-RDAYSfwqQJFCKLSsjhD3Nai3l2Cj1HdlqfktLF-eEmzmZcC7RLbGeMmAvQgs6pW6iLIzEOgO58M7OPx9BUfyzORNWR7yGIaWGoQUpkbk_717iHOohg4F6HWDXgz2yEKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgcpKM-Frwswa2S0vj65arVXsZV_idIH93-vLCF3tV6ZcgEhfpU4iriUyenVw5vJteN9tGYfYU-WamCsSOFDsAndclOOnBxW0_aXX4cJWmIRAkXaM5wreBy1qqFXNgrIeLvkLH6x3Opgmt8SKChMHoAGjmC8S5fNCgb9YwCJnWH_y5Q4oQpGKJNqlcDm8NCzIuObe1B8R7xeVgiClzbH5u_SBNS3aofM9nfna5phYYk2ZCO3QmKLcT_39-5AdppdbHMu0usnKB5AV8pjR4ov3OuPgjGLeVN1wKIuxwah6orFPIgQ8yhTPsm3CQ8P3tpLthkGfu4wag4C5EsWqHtNnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇷
#فوری
؛ قرارگاه خاتم‌الانبیا: پاسخ دردناک داده شد و پایان عملیات اعلام می‌شود
.
🚨
🇮🇱
#مهم
؛ اسرائیل هیوم: اگر ایران حمله نکند، اسرائیل هم حمله دیگری نخواهد کرد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91541" target="_blank">📅 14:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91539">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
فوری | قرارگاه خاتم الانبیاء:
ما توقف عملیات نظامی را اعلام می‌کنیم و تأکید می‌کنیم که اگر حملات، به ویژه در جنوب لبنان، ادامه یابد، پاسخ ما بسیار قوی‌تر خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91539" target="_blank">📅 14:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91538">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVinOZNLTxGVzh0sSpYU3GwPdMdRmehqV9-ls6iidin5ydqg7NbifNCRNmcDkVItiHEVhhuoVLDq7bOQDnjfe55CEIF_e_dJWPP2I8kXUtS1-4YgMTDjrLUMLybpY83i9IR1XIfhKeKA-r7kYECAneR4hr4pS4-cA6GDkd60czwKZzjqnVZgK2XDiyHAa2rkR0XhuJY6i7F4SnkvP0ulNxtoH87aN5ubba4Q2otwnNolmjbE9PWkz5S0AH19OPbPTHS8eJy827zioDUYDkOiNJ9qsDCx7aA2WX9CUEIYIttvmE1dB-AouzxG1eQ1mbUh6nUvl-QMjn66u77wOjOFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حریف تو من هستم نتانیاهوی قمارباز
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/91538" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91537">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrZmKb7kZtF02Hixmg5CXF9UoGPMuMGY8ur4fV9zuVH4XPI9SEm8J6Ge_J6oE7h8GOm6SNwt0pQht-vMvFLjJJCSrpuTFpWFWa3vTfxPq16KEvaA9JGDjO2NkjozhcpOPy4mGLASKbnFPx6eKTugBQBV9yL7pfcpsRCmFFZ5ofr0iSbZjeMTmFP1uhu6OkAiWnWNnJ3DVvn3r811G0UOUkdsKruiN4CjtyrwYkOGoPD1zTc5pZ-UK1IrQ8XoOTaUqvdBB1zrqZnav5qOYF7BPSv0BfM7ehGXz6JeDFGTVQ14i6ONqSte7VeStAc5esPR0p_ZZBe4_8SpqrpGFdFTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
‼️
🇪🇸
هفده‌سال پیش در چنین‌روزی کاکا با رقم 68 میلیون یورو به رئال‌مادرید اومد و‌ در 129 بازی با ثبت 29 گل، 39 پاس گل و 2 جام این تیم‌رو‌ ترک کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91537" target="_blank">📅 14:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91536">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662d05e7ae.mp4?token=clvTwjI7pQXLNPwIlq8VTgb4NJGON5vv50FDPqOjxaKfYkVq7WsK0-SzBS1cksofwGeCKZ4ptv2h1NhC1VfdWGJEQIxK-SA-WEou8NrducBbWikMNVF4OV700F09kGonfoZUDrzPo1ZPD7Kw03kJ776mYBOLFTVPwVNV8V5jjEnImqxKeHy3LQ7bqEnrEP7du84no5IrUg02o6QfJK98riWScT_b28fIkxQnTg-ECBwd08xc2fYMYmZ3UZ5j6LC7x2N7VnSjt5nXBUdFPrGS8uEc2ECcpIzl8vfFki4w53jAbbbQ7CwExgDabX4HNb-kxa7z7qWmc7amj7TdoQ99NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662d05e7ae.mp4?token=clvTwjI7pQXLNPwIlq8VTgb4NJGON5vv50FDPqOjxaKfYkVq7WsK0-SzBS1cksofwGeCKZ4ptv2h1NhC1VfdWGJEQIxK-SA-WEou8NrducBbWikMNVF4OV700F09kGonfoZUDrzPo1ZPD7Kw03kJ776mYBOLFTVPwVNV8V5jjEnImqxKeHy3LQ7bqEnrEP7du84no5IrUg02o6QfJK98riWScT_b28fIkxQnTg-ECBwd08xc2fYMYmZ3UZ5j6LC7x2N7VnSjt5nXBUdFPrGS8uEc2ECcpIzl8vfFki4w53jAbbbQ7CwExgDabX4HNb-kxa7z7qWmc7amj7TdoQ99NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد باقری هم سایدشو برای جام جهانی مشخص کرد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/91536" target="_blank">📅 14:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91534">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QljdxE8E-YacRA9yIQYFJ_s0SZERhy3ggoCnoQg5fbhbRmo7yAHzXdtJIcJwFZaGGJge_vCh8Bg6i5mVCDPdkvAgmlKNAjnKuH5__61V45vMnkudNEKYgYY99IMHEJfw6TL6YaSx5cxIVz4JWpzjKPp5P22EjCTzmrdyqG-z7GcqRCGjqn6NaZYhWyBN-iYMV9anC5YXqhmvO0G1ZQ6gJcYxhR95P_Lb2ODb8sUYkwJ_XTQ4jN11Tn4l2HYxGMdOspvEraURRxEnf6Di3_kR7Pt5YEQPCUw8zi83sMqi8Dx2oHrjLULHFhTi3aZ1dYqV7wn0e1c_-r2rgYqscbDVfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا یا من پولدار بشم یا دنیا جهانبخت تو روبیکا و بله چنل بزنه.
واکنش خدا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/91534" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91532">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEwwA6OtEv54a0EaDsNLlHFZtqRG3xTvFdkPdfH36liLIXA6LLdO3dRkdxx8G-vSb7L509Lw9T6aINMPWXZA0t-xnet7gDpSyHmpMBQS1NuGA2o2IvzCL-oFf12CjZ529ZNeILyc2Y_CkIBvQoIZi8MVpV61M1bsoFaPf1SccfCEArMBAl9uNO91KDm5vVBOdSzj_q8S4daJZD5Cezu4_uGZOoP1EegaAOfXInR_3MdVHdyda2DCe8TeLckvDjFRT5ZH49i_9zIdZGE7WIPkrI78_50W0fSroUT39wpyj1yzRJN_T6NcjJoz3zU1jQHCWVAJMMcYmTay0HVt05Bqhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⭕️
🚨
تنها 3 روز تا شروع جام جهانی
تلویزیون دولتی ترکیه مسابقات جام جهانی فوتبال را به صورت زنده و با کیفیت 4K و Super HD در ماهواره ترکست پخش خواهد کرد.
TRT 4K
TURKSAT 42°E
11767 V 15000
TRT SPOR HD
TRT 1 HD
TURKSAT 42°E
11054 V 30000
11794 V 30000
تلویزیون دولتی ترکیه با بهره‌گیری از تجهیزات مدرن پخش، استانداردهای فنی بالا و جلوگیری از فشرده‌سازی‌های مکرر به‌واسطه دسترسی به پهنای باند مناسب، تصاویری با کیفیت بسیار بالا ارائه می‌دهد. به همین دلیل، حتی در مواردی که بیت‌ریت برخی شبکه‌ها تقریباً برابر است، کیفیت تصویر TRT بالاتر به نظر می‌رسد. برای نمونه، شبکه TRT 1 HD با وجود بیت‌ریت نسبتاً مشابه با بین اسپورت، در بسیاری از برنامه‌ها تصویری شفاف‌تر، رنگ‌هایی طبیعی‌تر و جزئیات بیشتری را به بیننده ارائه می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91532" target="_blank">📅 13:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91529">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ملی شکن⚡🔥.npvt</div>
  <div class="tg-doc-extra">2.3 KB</div>
</div>
<a href="https://t.me/Futball180TV/91529" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
✅
به اشتراک بذارید دوستاتون وصل‌شن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/91529" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91528">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtlPgi1RBGpL-YvRe1W_XKXQVlghn5sPwzAwSbn6NHUxqmUAO2A_TPj-a5jcsLrMC0N3KyxFrlJlEAbkDKYph1dPq6jKv5PrnCpnnsNmVC6vQzcYNRKV9ZULpvVU41LMuPGBygeBdmDZXMveiceT28M--ixwZLqfEToEp5HA4WjbRx29g2kgMPl6TLU-Pr-v8jN-bNgeuVU9y_gsIH084D2iDX7KlHoZd-foSQvbm65AMA0uPpKJsUSor692j_GyySDPxkkTVLNZyUUw3ox3u9XYmTjxgc30pkmneMEGXccsz4je8utFNLAyCx8bCab1q1L-IcTIrAEBwakftIfMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سر صبحی خواهران منصوریان اینجوری به شکل عجیبی به دفتر رئیس فدراسیون ووشو حمله ور شدن و خیلی وضع بگایی رقم خورده
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/91528" target="_blank">📅 13:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91527">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
فورییییی ترامپ:   اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91527" target="_blank">📅 13:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91525">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
فورییییی ترامپ:
اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/91525" target="_blank">📅 13:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91524">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سازمان ملل باز هم ابراز نگرانی کرد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/91524" target="_blank">📅 12:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91523">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/91523" target="_blank">📅 12:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91522">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR7dGCgEdlvGBFaWAQgX50IwdLRWXcpIDAj9zKuoIEArMQ8phSGG3rRm_U00JfowyU90JpJfz4Uf5HSB4K0lyb9naV4g6DEurEmFr4K9p_MZGm4kNNhoNUV0qpk5Iok1J6ZKY4ydaukvXcl0Y2nHitRLEoeEf-4-mgyC0SAj2iBXjBE58o4_6gk4QED4g-lxshCJ8kn-N5ZaZZA_ruskDWmU9XQchMSAjVMTqVNzno19vY1u0x4Z6ASUyDOpKg1wCDJLAm_DZA0swM2IU1QrihxAaNiO9NM_EvgxGERerSrz4pTvBts4bQQIBIxs9bV8n5j7K4lYgAeFs7SFwoOzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عموی ترامپ الانا زیر پتو کنار یا روی زنش خوابیده. تا بیدار بشه یه حرکتی بزنه یکی دو ساعت دیگه زمان میبره. احتمالا این سری علاوه بر ایران، کیرشو سفت حواله نتانیاهو هم بکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/Futball180TV/91522" target="_blank">📅 12:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91521">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/Futball180TV/91521" target="_blank">📅 12:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91518">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc4CGeIgzkFFXYW1pSPJwvit6u67fBWRxvSzs63q2sMsfNpvwDbOfLyZ9AbZKborwJ3vHyVtGevB_-L7U5LL_qod0D5UivtmSBuAzJX-HBTWcmi2ssx5_5lYtTYkvXeTTSZzSDS3Gp5WHzM9As7VGOwNb5rfbsLDq2HJf3U8M5qp-Rlf6LeIF00pz9B2rALvrpXgEJq6GjlREp4UaSylbxcR5bXx4kNhbUxyEBKnI1NbSr_kxYLhSd71dImFiGdTbWvFFI0TFH4iqELjBAApcdQKvutzIgoVUBg8OwLoXf-erM9lZe00ZLCyL7hmYwgQf154fxq4Eok4lo5p8YKkhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
#فووووری
؛ عبدالصمد الزلزولی ستاره مراکش بدلیل مصدومیت از ناحیه رباط جانبی جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/Futball180TV/91518" target="_blank">📅 12:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91517">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3302fb4017.mp4?token=AL2ptsRIO8v6qwnQZlpyd1EBzAQ3Rq4SvL1KcQRpdzGVs1ScJajaD2Lhhd37Ib8QqKRBVeTIGM8LON1Qwi_9y_Vbs4ei9ZVOK-KTJtopKGzvyZJhAO7OC2Ukulr4puKHBo1iOtGjJO-Gb0ksXWMqF8XBLCUezmlEkZriRRKZhHgUCy9_eFifJ53cG9ATLjEcTCoarZxQlNkKPLgjniHtaxUWj7PYddiAGRVvX8U9oNp05Cd-bTL1NmAtSysUBNltxv-hvhF3fhLvb3BZqq_T5Hx_Y3JxYcVl0qhSMqWykF3_oLHdowtoBFCmtNyBLHsixzK68cjb02StPmzLyXjbhH6sMS-PjGJsvBGSrPk9593Kw5JXkRQynDq5SDH3FgYxHw2mGhuZezEP0YCrx98BU-DjrUW-zrH1n-UL3I3yC01KIuYCGGti6Uy-TXvMlhqPhQ7uUOollFSWelzs8jLiBJ52SpGuKRqI2DYznj3I1VquZ4xrIe0BabyFvmwwsmMlH8OWFfI-jZ4fAX8QaP-OVxLjnrWBggK5wmypLc9tFid4EMKqKnm3zLbGOIqZrT3dTekxsOa9lmWnHwWEh_f_PrZq4uA1815IUY4he27QJct3KrZR83ccRi1CEqwC3F3B0d5pmLmLvqP9yM8vBSgd0jVDPXRcy2i0z-cmAcWtCPc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3302fb4017.mp4?token=AL2ptsRIO8v6qwnQZlpyd1EBzAQ3Rq4SvL1KcQRpdzGVs1ScJajaD2Lhhd37Ib8QqKRBVeTIGM8LON1Qwi_9y_Vbs4ei9ZVOK-KTJtopKGzvyZJhAO7OC2Ukulr4puKHBo1iOtGjJO-Gb0ksXWMqF8XBLCUezmlEkZriRRKZhHgUCy9_eFifJ53cG9ATLjEcTCoarZxQlNkKPLgjniHtaxUWj7PYddiAGRVvX8U9oNp05Cd-bTL1NmAtSysUBNltxv-hvhF3fhLvb3BZqq_T5Hx_Y3JxYcVl0qhSMqWykF3_oLHdowtoBFCmtNyBLHsixzK68cjb02StPmzLyXjbhH6sMS-PjGJsvBGSrPk9593Kw5JXkRQynDq5SDH3FgYxHw2mGhuZezEP0YCrx98BU-DjrUW-zrH1n-UL3I3yC01KIuYCGGti6Uy-TXvMlhqPhQ7uUOollFSWelzs8jLiBJ52SpGuKRqI2DYznj3I1VquZ4xrIe0BabyFvmwwsmMlH8OWFfI-jZ4fAX8QaP-OVxLjnrWBggK5wmypLc9tFid4EMKqKnm3zLbGOIqZrT3dTekxsOa9lmWnHwWEh_f_PrZq4uA1815IUY4he27QJct3KrZR83ccRi1CEqwC3F3B0d5pmLmLvqP9yM8vBSgd0jVDPXRcy2i0z-cmAcWtCPc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
سر صبحی خواهران منصوریان اینجوری به شکل عجیبی به دفتر رئیس فدراسیون ووشو حمله ور شدن و خیلی وضع بگایی رقم خورده
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/Futball180TV/91517" target="_blank">📅 12:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91516">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/Futball180TV/91516" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91515">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کاش یکی به این کصمشنگا بگه اگه با قطع اینترنت فکر می‌کنید اسرائیل حمله نمیکنه و فیلمی منتشر نمیشه از خر، خرترید  اونی که بخواد فیلم بفرسته نیاز به نت کسشر بین‌المللی که به خرد مردم میدید نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/Futball180TV/91515" target="_blank">📅 12:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91514">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
حمید رسایی: از آن فرد بی‌خردی که اینترنت را وصل کرد در مراجع قانونی شکایت می‌کنیم. در شرایط جنگی و حتی پساجنگ بازگشت اینترنت یعنی خیانت به جمهوری اسلامی!!  +منظورش مسعود پزشکیان هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/91514" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
