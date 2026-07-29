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
<img src="https://cdn4.telesco.pe/file/Z3Ch8Y_mxb-anIyJIR8PBMgI8u5-UGKPWkvQCO4lOV6FJjib6ZQRPAHMIcHj3V_iBPdm8-IpO5Iy_wl1WKkOt-qEjJNWPAtX-J1Yu-yz4WsfBDUK7iebyBfDN3KFs1jW8_7mOXGuAM-2Amx_K-aQO2NrZ8B8q5-Dfdjg7QGNsCOvvWF-NltI8nzsTCcUVATD9QYsCPVNlYoX1dtYkXejt75ldGGjW5Bnt-Z62iqvTQhz6ddS8Yc6OBN6NRgUeUe0J5Q_S8kCXKH-qXDOfpqvpHwuwDxKpJfZHfelfVUPxYXB2kibrO62yLtSdFHJmlVpM-aLou-uEkfevvKaeLT1CA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 613K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 23:20:10</div>
<hr>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=Epx85H4WKTggt0l4kDwMlCUfUShoDFOlUCKRNJyttXoBe1IR65kFxAhx19OrdBqEp9NO72DvJtRWH4U-atehfYIdVfIy3EQxJKQPE_vZOCPvOwpXa_X2Otg0kBW7P32rUlem_py2SqGn2em69TLnjUQi9d2NjYUQ568MKDdJBRhZajAfMq4Lwlcd87WZrNaeJLSxX6R4UgKBpe2H8O1pRLAwlSOLMOdqdnB3fw2HQKC9RC_4j79pN-KCEtb5rJDdCrHnH85bn3a2o9b53xi7X6c8tYxO2dwtHu3PdvvnwQ2ALahU4FgEUw2eAafBuhmbPqoG8-cOceo773YYh20cl64ixnjcrg6nMc1H1soPLkLqYSoyNOdJzKP0EkZizXYYCSpRh3zEGEmxV0XsHGxiKa6jjIfIKnJ_slaOEOKiUx63U2jdoD2osAC6tSuiI3kkK8zOMJFz6lDZHlR-iPaoD8siSl1tbSDw23WH2tcdA-Y5c0BtZFuf-MAsYUy887G77XbjpQeDbrIzAAJgi33h4qzO9frIi1WCPUyaHYzI12U15GuOndl5w-VR1V-9o7-4-2O83blhLwS7ZgCgQLdGK7NqmNChCAR3IB0L4hvvPiB42wzxvAf8pXeFBRFwZL5EL_JbwMaPDZBKzprgtMJpDsYd7B1xutoFa-VvFfMxd9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=Epx85H4WKTggt0l4kDwMlCUfUShoDFOlUCKRNJyttXoBe1IR65kFxAhx19OrdBqEp9NO72DvJtRWH4U-atehfYIdVfIy3EQxJKQPE_vZOCPvOwpXa_X2Otg0kBW7P32rUlem_py2SqGn2em69TLnjUQi9d2NjYUQ568MKDdJBRhZajAfMq4Lwlcd87WZrNaeJLSxX6R4UgKBpe2H8O1pRLAwlSOLMOdqdnB3fw2HQKC9RC_4j79pN-KCEtb5rJDdCrHnH85bn3a2o9b53xi7X6c8tYxO2dwtHu3PdvvnwQ2ALahU4FgEUw2eAafBuhmbPqoG8-cOceo773YYh20cl64ixnjcrg6nMc1H1soPLkLqYSoyNOdJzKP0EkZizXYYCSpRh3zEGEmxV0XsHGxiKa6jjIfIKnJ_slaOEOKiUx63U2jdoD2osAC6tSuiI3kkK8zOMJFz6lDZHlR-iPaoD8siSl1tbSDw23WH2tcdA-Y5c0BtZFuf-MAsYUy887G77XbjpQeDbrIzAAJgi33h4qzO9frIi1WCPUyaHYzI12U15GuOndl5w-VR1V-9o7-4-2O83blhLwS7ZgCgQLdGK7NqmNChCAR3IB0L4hvvPiB42wzxvAf8pXeFBRFwZL5EL_JbwMaPDZBKzprgtMJpDsYd7B1xutoFa-VvFfMxd9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOiSCF02LdkNe7XeUEA2OX8-fI_9HdyCUxMvf-adhWYKxDYDzOv4g0s396P_Dxp9k_CRDGIAbG_K_fIuLMx-ps3JxqU6wvEvpyHfFM2WoVOkYvYZ2qRfoU7WN9jz8EslTQHHxzE57sdn0INz9DwNEaa4EfMv2x7sAoD-UVsIJLeO1i8HDl4uE7XquBKi1JwJv0BrNXMLOnDF1zgtrb6rbtLuQnaMxO-Xf5x-WfBGqG5RCdnZgOGBriPBSpgZ_bAjBicY5g7e8roM71C4ymBaQPlNiDmEC-AVeuHF74x5K_tnyoaJR8ZVNAvqIZb5IXDU5vypKsZSQuyuCCOwYr_i0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOxe1LFexCbOHlVa46EMKe3whmsUYawgjtFT2tnZ0H5u_SsCUIIeyZ9DwdSgvwgLwq8ccuDkTwfpeY2igQyRYbTv2kH-zgQrQ-u6QdZEqUnPT0inNnZjBlgmirQACuZ72H2Xk47gOkABq6Ho-Eq1mmuGoNPIi_YCa-q4ZhCzil7fDmSzFx54TMFqLuAN3npiFgMkmGemJwczSKi7JW4dHAVOyt8eZzCsk4WhxhTDuXvuyy0W7l1XjkkliyKr3hkYXu2WINXuHCFeJO4Ax_7pJtH2RnlG6E4mImtbvXjIKdwAHisI9fgDGldCfToDMxtdDoLwcXuXsmuwSQvrrgVIgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbR00GFTRWAt3QXqCJhSjEOMiBNkyuRXHx8Z2Ay1ZnOxvWhgGyU5aZD-GaZRWbOBs0mPSVgcy0Tmo0L2yCRlGPIlmDbpsp6nMQW78gK0FiXMB1uOl7mJeXZk17jidD7YWS8Ipv7gEBt5JL5O0m6qWFZyxFR_h4-aYwfjU5kqj1PiXP83PMo-jDQL5USA02D3mppjKtaiwK138yO_oF-vphHPkO6G2FHuF4885zUGsKu_LEPm83Qghbz0nYi8KrXLtHkKKk-prhuKbLuxndDH9wft9m4ndydh-JhltHEEDdjvBmue-9WSF8CPrzwsjemRWAcR0feVPVPK6K1Cl-RcaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi-4SOOeMmEtmquHY5lqGqFJlbqG1N1rotZbFboVSDgjt6Z5bf2gNPVqGp8RnU3hedYUElT3bmyRMwJi48ZY3rN4usDjUdYKJVW82se5slxSgOp8JcSsbBye8iTjMZuN2ES1rsuOiWmEFRqi1QmDG301W3sFhloiSe2vTbiBwhQgEzG-Dg0e7QiUfCUTo486xMSbDyJReodhhrjtcAmzHzQR0d4oqW2pC3dDTSMjfeGg-YC9UKkZxXuxdSNL_3iTv1OD6PEDf7vc095YYpF2XG-Gp-JJdMjpKX0a44XAyuDYpgkzFl-bmRduz6FR1P4fJCJR7waQXEF4zZbKjSBCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEYuUktl0rcezwmTOJfF0NLqzkxLfKLLd_hSwkb4PjxZTRB8i82cyjbr2svo5rqybgRHaNwJ37svPvTFZgBwPm3nm0EaZIz0Ct7Yi21Q44-yCcqGKqYp1bPi-3wXKyurxihNPNEwRfpXMnodYo_s2_6-yfUDtZh514MXlirbSx3JoA0pVjG-RiPiC-AxuqVgxNh-oSNsKo-mtEVZ22X-tqXd8vzbI9duW-sKltZ8O22K6_b4_2tdRfxSUpngxXznqbGvdTfUS_NdxKMb9x4dFSIqEhjqOD3ATU2qmwS8Sduy3GxeCCYnVc8EJtVtxVHuKwVD3S0wUbeNDiVT19DN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWzOFoFdeadkCYEQBbuiMg2C-4Y2fAMF8BP7SQhpyZ7N7tubH4A3kZ9TqHEer3Yi-evVfK8-6drIARVWAzsCHAtUJSbJK-d3iSqOPSNDhgFGV4-4k9m01bRfqtOZxmWwlxIvP7pbGgXoNM974OnSw-0rXx9bdmIamEI5n63gWc7Dax7YMMau7XH-kZiXE1CqixXbssB_J8OXuZVf9ZLgq_JvRZUxW5BGjfmogLA3xBouuoU9fUoTgHPHXoDlOY-6f26ZnUa1a_DRzAbBWcsV8mnwl0O8nbGBzaWKSXpyiqiENUfhR2VmzZtmPcu6q4F3w-kPoENWU4Wk6w01d9ch5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ANkwv7BWnrIBf0tv-infjyV76zmTEqi01www669_nk76SIu57Ubm4zvwqXczAO3M6tTofnqMmAwJ-EMqwXMigt_rWVzwLPQIn-T4ErtgF_g1mYqTDq9fzLlIJ2aP07lu-20LujymAOLN4PFLTItBf5A_W1CEn7-V_2--IBHCAyagakZ9F3rT7XJClCzMf7a65qC2LvCg3fI9FGIvBMIgnxlWn5qTA3nb9OOmhf__l5BwcThe8jHoNRUPC8hqtDZerRe7sPbGkXnSFcJ_1_v2x2v-ZYmsW9_lPBlaz_yVbkIWMyy4ZXEgFLP-cQZv0sfCQhJA3TWlqu1ox5VYp5hSqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ANkwv7BWnrIBf0tv-infjyV76zmTEqi01www669_nk76SIu57Ubm4zvwqXczAO3M6tTofnqMmAwJ-EMqwXMigt_rWVzwLPQIn-T4ErtgF_g1mYqTDq9fzLlIJ2aP07lu-20LujymAOLN4PFLTItBf5A_W1CEn7-V_2--IBHCAyagakZ9F3rT7XJClCzMf7a65qC2LvCg3fI9FGIvBMIgnxlWn5qTA3nb9OOmhf__l5BwcThe8jHoNRUPC8hqtDZerRe7sPbGkXnSFcJ_1_v2x2v-ZYmsW9_lPBlaz_yVbkIWMyy4ZXEgFLP-cQZv0sfCQhJA3TWlqu1ox5VYp5hSqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=qO-TmDosqF87CAZUdEOrT_cMkRg_A1JWBinvqE1lONoNTP9BErHdMKVtnSpM5XZyIBoHlPHEaXHncBa7IKYpaO0Ro1FaKcHogvossbB4Xou4s0Sn9lAdOgffs5xopfGfxrHRKEVwpVJaMfMJymHBSsbOrt19Sib5BgZsfVK9CO3XVEJMm1hJla0TZhAD-EwKaN3a5Aasjv2ylYUYOnty240GZKENYiiX4pm48k8agW6yvt1N4DNr9wTStyApblqIleZjyloO2-9lJtpq2FvJj0iAL7qT1BJ3PkfIfNQl1P8n8q4xv0Kwcmbp8VZW9Jo4M3nCcepCFkOvSWShWcfSdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=qO-TmDosqF87CAZUdEOrT_cMkRg_A1JWBinvqE1lONoNTP9BErHdMKVtnSpM5XZyIBoHlPHEaXHncBa7IKYpaO0Ro1FaKcHogvossbB4Xou4s0Sn9lAdOgffs5xopfGfxrHRKEVwpVJaMfMJymHBSsbOrt19Sib5BgZsfVK9CO3XVEJMm1hJla0TZhAD-EwKaN3a5Aasjv2ylYUYOnty240GZKENYiiX4pm48k8agW6yvt1N4DNr9wTStyApblqIleZjyloO2-9lJtpq2FvJj0iAL7qT1BJ3PkfIfNQl1P8n8q4xv0Kwcmbp8VZW9Jo4M3nCcepCFkOvSWShWcfSdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhPEm4GfwBGNvOgC-cWcee2XiRZQFIaM2k_VJDa0PUt0PPunEfG0hFY4vpBZj7_7EhUBatX4PlkWCpam4rs_HKtuhrBzlwR5cfVFgOzZVpnWSVgbJ77-SLJ-3iqjlAV2ayKmxz4DssVEtNEia2pICH_zyuNTkqxAqsiz_lHesyKv22u52mAVp0ZdpyQgS-CI9J1YVDtshL2rjKdhBnqHYg8jlwERe51peSj2FdeASlGi0zyyiLFvVFIQXRMvWXk1uAhKnGZQclikKoMiVGmm5SwyD-_kzVzyIX65TG4mat5CA2zUxCFGz-js7G9Bfx58q29yd43ZU17_ppkMbJ-DeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-_yEyu3UHNpDbgVpKGUoQNbTr3QiYDo7rQFYGgf0v8Ni-Gtr2LdEwH8Es9hs6LGMfySuZceKY3L355KeR3KG6dsdX2ixGk1Q9hUm-sUeuP3ttfdFn00U7mwvJCIT5ZnWuuXzEzxcI3btemFFsDFoNXVHewrMLsnHO3q0sC4qn8Nz4aPGN_vXXhGAI9ZZCnXT2wagPwA_ZHtC2T--jWA2xP2v35x60WCBF0iI3t31uWJO3XGiyrTfExVPtxSwc26qkeboB60sd-CS0qXlf2hNpwMEGNwjMIyJLgC_kQEQRBa6G1BA9dS8_TjKCMlc2tRsR52uDqXUrkq14zd_nMRxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=YNIegXpTOhkGOk6_wFaZ_zJxlQdw4djI7kgQM7YF-UcW21vkvxBI_QEw5EPuedFDZ6ZwhpUETgRNFmQeeyJZGZ2ORocCVYDVMjTx15rHolExjgzETjuJ118ii_ZdolRwdvOLvdI52l36GsDEekch7PKET0yyJp1vcosIoWz1AxIJFrZXlJh-TCYfnxaa8EmDOWBaPegCN3j0iBl6OsMAHyrADfyDDVF1GscsPoj3uZ2Dmj3QnYSI09p15Ag6-mZbIxL2hPTERWvFSt3DtFYyqF-w4qVZVNJWlQLiB1RURlJ8MSysUIyPxa8lVBY25yFytWMmfSwQQd7lqt1xphQTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=YNIegXpTOhkGOk6_wFaZ_zJxlQdw4djI7kgQM7YF-UcW21vkvxBI_QEw5EPuedFDZ6ZwhpUETgRNFmQeeyJZGZ2ORocCVYDVMjTx15rHolExjgzETjuJ118ii_ZdolRwdvOLvdI52l36GsDEekch7PKET0yyJp1vcosIoWz1AxIJFrZXlJh-TCYfnxaa8EmDOWBaPegCN3j0iBl6OsMAHyrADfyDDVF1GscsPoj3uZ2Dmj3QnYSI09p15Ag6-mZbIxL2hPTERWvFSt3DtFYyqF-w4qVZVNJWlQLiB1RURlJ8MSysUIyPxa8lVBY25yFytWMmfSwQQd7lqt1xphQTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujiVCUmRHR50pJ5Pz4_-iCo--g_U-Y7zqjcN0V0pTjkM9Mo3Mum_IrqnDDtv0YwMjwHJX6GrY9pB2DVRjcVttnFmO9dlf7Qm_YxgnKLL_Uk3LGdqc2c2D2fpzdl82-tWJYVV1R3q68VEvRfkFVjBTwIZ8mYjCUaV2cfkbUSn6wIkKDxOL-hr_AcvWa-yLGRbpYxw7I77Q6_nfwc8IyyKq-18YUOjDiLz2xPlsKs5k6dfzmJgiby7mrvGzozTHm672xbwfa6obaa5AziOxFzrOIlOL7YjDsM3K31vXbuEuy8GqakFIbN-7-s0ciEsaocJY-5GDHf4nPaoLe6F_rxvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPu0WBbdhEffOdbCexdbnOYSlHhwury2RBeKNjtMiO_-Ix6byhE5iQz9o9yhB--zgKGrGMB3tnIiNCENhpHweJAl9CpyqXliQNNEAXHr_agtNfm_3nbd3YJmFkXHbBhe4nD38JQTSKshCFIZF5Viyq2mJ1ecNZ7GQPuhS85_A3I6byQ7mjnJd2DLA9rzP8Rb3ZshuzKoa-pMUOGdnO4xpF9eSu4lj9FUPt8DqKylKB34oouhmLMgYryZqsj3ZN-uIP5DociTEjCnhPpTSRtTVPCZTkT4_EPa3cFE5mW2WTD0-LPXd2MRdOrKk3mS9LDIWgVdh9f8JEnCT0KBDljzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=c6ZN0vfxEd3sqq5CDMgIrj0pgwZnoQCm3LG2rXaQ4H03ciSeBHQFVDO7CthTLKc0-bU8y53hdmZ9yTxBlhwtN930JMsknfJYmNjfg_TOXjjDSip5BAn8Z7w_o8fdP_4F6GgdsgXKCseDZ3VOc5j0ZcvA46ap_lMQI69YVs3NbMIKvcS1gzT5kFKfPc-hHyqSJ8AlRZjxgiI7LpU4stRmawjvREo9oH3UKRPZ9gMN00k1W2FiMqRJhiK_0kwZBWf7ZIRoKgrl78NGXm5ts5gWy0T72Du_WWRSH71JPZs1Iuyy12x9ipmagQ2ExIbiBqOXGAQdCOXOhDMVtKogkdbkKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=c6ZN0vfxEd3sqq5CDMgIrj0pgwZnoQCm3LG2rXaQ4H03ciSeBHQFVDO7CthTLKc0-bU8y53hdmZ9yTxBlhwtN930JMsknfJYmNjfg_TOXjjDSip5BAn8Z7w_o8fdP_4F6GgdsgXKCseDZ3VOc5j0ZcvA46ap_lMQI69YVs3NbMIKvcS1gzT5kFKfPc-hHyqSJ8AlRZjxgiI7LpU4stRmawjvREo9oH3UKRPZ9gMN00k1W2FiMqRJhiK_0kwZBWf7ZIRoKgrl78NGXm5ts5gWy0T72Du_WWRSH71JPZs1Iuyy12x9ipmagQ2ExIbiBqOXGAQdCOXOhDMVtKogkdbkKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3lB2h8HXbW-gyZvzMR4nJhvaAI8g5kS1alWnvB0pDrgZrqTsA4wvBM_wbI8Cf_vlbtRmL_zgLfhq5eYJbxpSMOFzJkFJvuvsOcYvMxnTl0yP-DzD2ZETzIB_QDo9OCV_UCkfjTDo3VdJlzaCU417mFmoadZ47qTwLPTBRyItx4HcekWJWsVQLskL6WgGaIJ_1C2s_D2SYwmUHkDPfmKTh4wOxAZzsVO2rJLzBVbUkI0nD8yAl_JAF-VtYapq4q0koOaz5cdmewm6G4gje1azzTxHZN8lGFLLqrUzzYAtb1Q0dk9pTw2eVXjtvDbVO177E4_uhfQ-7vcHp0-a5wjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqpiTTot7-N2bcDHdN5ttwKoDvm4KTzNmDKYjQeF0iW2ZsMOjHkhC5ZzrY72bfeXByC88eLhiUdj_zt_DQhgEige8R-XUGA_FUhZ_GSnO_xKSWdXnWt2_Qwx_GuFSI2wBZpwaW09_YbldtLJahT6GbyPQmU69HrYiVBqeAppzzWYvWvQJILSH9mUn24ZJhFoup38ORIdTWhnLLzIfKiA9RwATk7Y7DT_aTC21K2Lx0738aopqh5JR5Kx0DyVYc-XaHap-04NCaZ6hiEX34RP8KYFnUcHdSgt2CNR0fvPNKRK43_az54nOI40PCrOUko2QxWld1GhJeMDOMN_E5-EZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=uWKPxEQq-bjGr4FjW9q23ajGh-Vp1rDp10NXHNCxgR86Y58acY7M6-N7ji-yxKsh_w7yhZsux0A9rbOU2BbA6HTHDRl6QIrCiCIqELltP0QdHqTZbssq7_gFY8H693oJL_Ums4iaO2kjCZA5xmaYVAhTka2djXQ8pidUuwaeRiD_9WLWJ-gdNfBQ2E0DYvkq8YL4cAbFmLbPqeHGiVcdQ-4-HYCr1f7kO0FyRGLO3KAUV-TnhkUBcnMBy2IDdB1E1f4zDODwT9-iljLAHh-8jEgV82_jXhkOXhS3FiJNNjlR-v-5ASjUYGrOim-TY3PQecC4aHZfrbWkzx6sf0zpnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=uWKPxEQq-bjGr4FjW9q23ajGh-Vp1rDp10NXHNCxgR86Y58acY7M6-N7ji-yxKsh_w7yhZsux0A9rbOU2BbA6HTHDRl6QIrCiCIqELltP0QdHqTZbssq7_gFY8H693oJL_Ums4iaO2kjCZA5xmaYVAhTka2djXQ8pidUuwaeRiD_9WLWJ-gdNfBQ2E0DYvkq8YL4cAbFmLbPqeHGiVcdQ-4-HYCr1f7kO0FyRGLO3KAUV-TnhkUBcnMBy2IDdB1E1f4zDODwT9-iljLAHh-8jEgV82_jXhkOXhS3FiJNNjlR-v-5ASjUYGrOim-TY3PQecC4aHZfrbWkzx6sf0zpnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivmS-FwcCJlK4nqwkDJPQoxMhNsgIAxWfvWI2k5lOXVtXdxKYRkTLumpSH7rCKRC6tCX1hdasGVn0igtjjvjy6RBG4WtuVxD67Hoa-0PLeyYd6-qqE2bSlVzjIM1PQHTI213Z42E78uZB33Edu9V7eIyHT7O7RbTlqaB3KFx_vGp3tFO_BBeN3aLCiS7hN_CbSAq1o-ySH-bE-OoGDRo9LoJM8MlK-dUgqFQtv9t-alFRWOqe8LFd5kUpZJidsvHF8LVv06hGQ4hY8_CcdtCoUnM9xSZa7wqwjw5fhA4TuZNI-bldZuZ2D93utOzSeOyr4dWsJP4uThOwNLNngBfvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzfLErNOGS93aEHwdLuh8L37TZF89CGc9X2vczmvaynGlioOhbM9M7LANcFaBnf3Mu_N2MNJzEsFa2GgsChda2-QQdWlQY6rucFc6xzt4nfdzrhe2jW2ocRg89qhxz8Jwz3Z2ij-cV3tjF10t2QqPLFqEmJ2oOxth784asJNHfPaydCPXVx35r4k7_HV8p_LpVxwUYvOgagfuVuWBrtMvk0GEl5tFGMU7Yphh6qe49j5ZByEb6JwW00TMcVNQVHmoHFsd58T6YV-5xdD0iVdbGjI-Em_4v4gmVbh6q3qID-u89KHrQQCw61J76RZ9xRyy5IVomCm5y_uIkHr2H_I5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnb6Gxx3JVum60zVFvTjqiq70crjRrpEsq3Zv6NRn3FB9fi-I7f7Yw3jO_aup56umclhWVzPXXLqRTkoi0TIM0EawQ5131dMMDXfSVNrUwuh7Eq9awIrVamygVPhERnMxcD2l0xgS2loSYmmVTrP7iDPVSX5uCvz1yHn13i5LKRLhbEYZcfuScgZwBzhtQBe_taeL72ItGICfHk754KeDPctyGSfthKFnEQatAJUx6Hp4IPNo52lxSg05pxSkiRT5oH9chLhq0jS0kKRjmhfgqXajnvt1kRsfNpqEMyGixxVwuHYCvTUc5vjr72vzjlx1Pc765hSWqO33rLckVoHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcTZxAP5Xh4wyHQjos2URJARMyfYvyKkIOROyxrSQX1OB5zQwGBsV_wguccngDpXeSKMtigf28a5olXwWRv_eX_dIjK_jvSM-xpDf63sWDfCLojiIUyUoXoc44SdYegq44_wQsT26tkEG_Cu0smLdlYKoakg23i3hqZRWNbmCl55Z6wabDtNeUYbPkZYKUDxlUu57Cto7gaaK6_SlVjnvmEiG44V-_8pphfgQez7XPUxeYnSMn-D1qyoZW9A77XfKg5zhhWbd9iTkwR2ZYaN4p2YIYBkuk17YgNfFZA-SX4U8Irr8QVZmFBwZQbuzKBvgmutI2AkutLzTwKdaHrqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26758">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnxBCZXOK1pnY2omkBJW5vH2ZeidUjsAhHLV8LBrgon3kLWvFhHzpXHdWYqxeKHX6KqJSUAPvOS7uXCNadoo6lO2Nwng6kG_9ui_68aeBLzLB6bw2-z4f1cL0ekkhxL7pwTOlidNsi1OhaDBAilsiNqigxpI7qBLAbNOqnM5bBJRt_9Obb7Kq5VqCImxz_cyO0va19Dd8-XzLunR9IE0cyPn-VInO6bYan1aQ9tMVGMcQ5RQRfq6yYR7UziUHZlWJiZQd4lo7OZWLMZ-7ttnJ9syTf1j9od5JNWySh-BW-56d3l4sMOl9l8A2jESSAb6FudZkDJmreaz0VAByOG-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/26758" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOSmWYz-tLMVaZRiZIPHoVKdzOMPaYpWjhqm0HTbFABpTpT2dPpHieHeWId1blBq8lMUl35x4w0vJ7FvONi0K0ISzyyFN6XmpgouJ03poFpCjfbww_474ocyyNL3LVT9R4xaZxBWwyXMmoKY57MlgxB634TJ_o4rtPJnSQvq90VqM2T7jm7Ba63pgLCgjh_byreEd7CTO9P_MHSy5RBTX0nCqgDUPoYsZTw_5s_ojyQ80imj9Hx20Z3Q_eV-dEQKJvxKi3WB4B9hMS_zqEEuwOAb4ey5Y4M2zWsl2NM0ssmR3BEIAkr07D93B5i3w5ITatp1P8j71u-NlY8HSuzi5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7YMMUfzTu2g5fvskE50DGJKUsnIOBmwpsTXxS0nmcPD7NR1wnTrZOFa5CQPp148I8Q4C-ruV6Dx9DsDso2z5btPmFoDq7rr3v_89AGgmOdHd5tMu55EBtHdNA2GBHBfhR36Da0ePwBzfo4u0NyT9eA8GZ32jgHo63rhYfWI_VsT10LprbEqtxbSZ0Dv0GmFpFueducmcixouerxJfMqdMXlsZNXtrJnyB7yZ_bOaBe5iTB5lIEmS6CcpEnBtDj3ryaJHxKAnbI1WebnYI8_yCpDfuNj-rfVLpl0ZMiYj3mESOszs-YTS6C5U6TbuqHZziwzm3jEpixopOnu9neuZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=IE1kK04tUn2gm9jJKidvaeSWSSxNaCdVMtNOiHxhY8Ct3vaF_kzkHxn8kXCPh13YDf2YoIPI_m0YE9XhNSW2t6ArkSAbWsRymZa5sTUsmJ5uR9ppVMrXPoQIzhaUVWmNdS0h5eC-HGM-W3yrDayRa9XjZE1qBuzvOC0fB7OiHd_2KlYCzMZhYmjRXoPN8H86Datuo_t4zFA2SxNtIcXwYR7A19pGmugUG2QV9hf7gEyrStoEcPiQKCE-ePj7MiyVGq7i5jRmJpfsTnORfHfpp602cY4FvuNvA5LaxKhRkovgUYK_JTJmyVUIT5LyKtA9f5boTr_a1gVGtiHLJl3yEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=IE1kK04tUn2gm9jJKidvaeSWSSxNaCdVMtNOiHxhY8Ct3vaF_kzkHxn8kXCPh13YDf2YoIPI_m0YE9XhNSW2t6ArkSAbWsRymZa5sTUsmJ5uR9ppVMrXPoQIzhaUVWmNdS0h5eC-HGM-W3yrDayRa9XjZE1qBuzvOC0fB7OiHd_2KlYCzMZhYmjRXoPN8H86Datuo_t4zFA2SxNtIcXwYR7A19pGmugUG2QV9hf7gEyrStoEcPiQKCE-ePj7MiyVGq7i5jRmJpfsTnORfHfpp602cY4FvuNvA5LaxKhRkovgUYK_JTJmyVUIT5LyKtA9f5boTr_a1gVGtiHLJl3yEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3WjxLUR8ANyWMrTsGW5sqhcwsbcCJ1veo3yYbk3zCyxcr3FxDOAaZvab1-jmqvW1CQW4iqHZQIbxY68u17pCZw5iSHOusdEmYISOG3qBkfNWDit0tomdkogszFN3bN-GvodSZ3uNZtVJ9K1JDMVBXRayIuvLMzszBQqyZL_N4MbrYo0_0p3iI6sdGMEJ-kbTJKUQG2F8Uo_AIE6hBOVnQo58v3lg11PR1ws45OuQ0_VR54EpnryV_vCQnF4N1tYw1trQNe8kx0JxeG4IrCZfKq3UmchZB9Eiu5wLREGBRC-8e80jv3_tcuRZPq8p1gBOED_N8fxOc7PYHUycst0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BneAuHU406W6H8LXHJ2fEXrO39dP-7yqVcCvr9NUiuSQ4rXIqyh8fpYAiB2YF6f-ndj8KITWKjG-_9tlbl8g2BLn8m-jI5La9YqKAYQwVZ3m2HBMvh_v-gEEO0pjoct30NWusRb69SkyeWLBvKgUMShrTwRfgMAyl373JS7KGcfGHKYoB8rYMxyuXDVA5KHUZjg0L34Rc0Mbnb1b5reGwxWYpKxgd64b6CIxU_nu5yKNbpI_8eHtN_CFhqdM8TM-ZhTCjH5m6osbpiijawifC05xhYlw_2slbhFoK3dXmPK2PUiG46UiqCZYNyFdXULmGgTbCEO42xJZe0vDM-Z07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=e4Nqm2d9hHLsKJRblboK_64MMMGeLMJXGXfBpiJOyZhUpzLioe2Asfkx6ceBqOn9zJ6pauoNvCXbkOep2wD-tAI1hYrO2wj7lwRdRWZwQZvQgzV2P5Wpxoe-BCyPE2ftsrWzOXAq-Zm9ziwmSpfWoKRvQEcOG1_VsYxj_JsxZSn2Vrgfx0pcW06e7ovpNMY36RlrWZ23Ef0AO079d6TDGZDcBKyiMVxiSfhwrzBlQb6_BHgSFC9Xlnj5qn5j2UiopwKPTowh1IYIAXmbrzzNfuwbsSPJTesmCzhf8GNnCY-QDouBrSJGUnqUyZ2-eXl9ZikRlzQola-lQaVuD3bQkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=e4Nqm2d9hHLsKJRblboK_64MMMGeLMJXGXfBpiJOyZhUpzLioe2Asfkx6ceBqOn9zJ6pauoNvCXbkOep2wD-tAI1hYrO2wj7lwRdRWZwQZvQgzV2P5Wpxoe-BCyPE2ftsrWzOXAq-Zm9ziwmSpfWoKRvQEcOG1_VsYxj_JsxZSn2Vrgfx0pcW06e7ovpNMY36RlrWZ23Ef0AO079d6TDGZDcBKyiMVxiSfhwrzBlQb6_BHgSFC9Xlnj5qn5j2UiopwKPTowh1IYIAXmbrzzNfuwbsSPJTesmCzhf8GNnCY-QDouBrSJGUnqUyZ2-eXl9ZikRlzQola-lQaVuD3bQkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Ho4vjv9vB3TjASE8vHv9YHgIXZ0F1yYCnb-mB-zGdW_pFPhfzeV9xrsEXa7X_Fo1nAeog_ErVFTIhr3tVk09J8L9_7yEekUFoWv1fWiKj8_4lNj3kIG-CpUl1U_o3UX8ai84iQqivOQMV1LRwxFTXvfqcRSgX1ePdvxTOdYQqlZWg8RWSrNGOXPTK3ketYIDjRa0j9TE23kjgRBZ1TdMwpw3cUCiQcNJEd1iXqut3vvaxOdqfG_ZywOgZHK8ewbk9Yb-LT5RIkKGXtbJxsOEfgQTkDrQIHfw_CpJjacfrSWEYMyjLNhe3tXNdNTRilhCA4OztcxFxZvvPmaxo6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aknC9ltuYi57cb0QG8CX0uhpd6aP_UTdz5baGB7YK2a7ahVgU2uQaPH0GzS0hxJ0U9zbefq12iu4tzgh1uDa8UfVm33c-Q17LodR4ayuBDkiDrytmeUbmGcdnPuk6__pnKdUQ2JiQ2wmZWHHCC0FnYcm9e_vp8a2SC83iK5lAleXYicUm7XbM-O2tqy4xJTQjFHZg8BVV3RqyqSv3Yac0z5pCbijr-voN75nqxgqPCusRwJwKt70S0x2GuUrnSN8xA6chACFqD4rZ2bHM84Or4hl874fSrN7LzTQXOoJNo8iw96R1k8xxNChBRC7OuxOtXaHTyT86BUg4XP5DpTGmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jx07aEeIkAoCI58EOHj85eZF7h8S8-yIj6rTUldIs0P8fjmI9bbieUryERUkZa5qwfwkLHM6UltnCBQ7cx6LgoUF-k1h1Ur5woSuXPWsOeRulNJpUZJwsjo5O1I-6SKMUj0ZM3wkNyezmOsAtGux3TUu6FM86b9HoNslBLRQKXdAYMKlkIAaEGF8jQfIB0E8ROgzfWeSUID_rW2I5rUOSfvDWzjww7FUYTuGWsOoNj1fK2-QJ50gg53qpMjk_o6tIkimLIWFBeEmHowO9S23d_5kQR3ITNe8rfnKbD4gwbS0_jdh7yAawly1x1izASmDdYyZVT-jO6-9UzrecgohVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BN8F_N73Z4fq0wfB7HlRucDm9MoR_m2ehFczdSUCCGLWW8QNcF3CxyqRdZo9MyeNlWT3GpVXncqa1VK5U4L98XxP5DRZmR_j6XvgdjkqqBgU0By0SyJgoQW_DiQN2X9XuD8SsD36fjNkOADfqrQT2sgA4FzkCdxr5d16Z0WpwRmPZcJFQfy9Mmf2Sv5IKLx2YMaZpqff1QU84mGaVg2HEOBbN-FupxIveWpoXobDSiDEGgBkP_wsRYfrCln1ijsdFikOz5Z89ZyxEG8ufN1pN5JzfLU7lB83qDUkLfL4xtIEQnNa-wz0gLM4j3fdiU5Ga3gfNMX4RLk0Wx5tgAKpqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhCjIDt9twmOcctLL8h_dAM6V2CSRtiKHkiyOqgogge_AUMu2hk7a40bRZjZ0kVovsZJSJwMcYBZKuXNslWuDKg6HCt-jPak7v7Fk2eKB4RcquPYvLMeHr1XfQT4ZVkipR0gfulb-gGu1gmHzTzHHyncXvOJhDqm06-UMZ9d547NWKKtu-gd9IXhTvY2Kg8l-pW0_XYAY4BoFwYaprSPiHS6dCx2k5fc9RI3e4qoELfArJvvadH3xIw-5Q5Sd3WRsmLVnsRRwOmKyH0OyXmM6VG0LrcMhlCsxVaHcouiNhP7yE9q7UH1v7loWnb6BOCZGO6ZcM5lMPes-GCoC-of6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=ll5FOOVFb1ETFkTaIWJk8L2wCvSDLaxuXVXNsYxMdTmCzyf3dG_yhPNvrRj59aqwXlu_fJTw7FdffVf9pdaPQx_Jb5XH_BRLI58wSQV-9etQP1r2m7Tb9IuitdeB1_xLE-He3pFty7zeD-_tj9xdqFHrOP8FVRdt-7ghAbAD1fd1OJ-Cks9RKlayMTrpwN_mYUkQwkMVWzyM2tel4xRRPxuYlcwKQYo51QkLXzjnD6TsywXMIhIbI2jipGTH9iBbLxLDjTO0Xhc1C4GlLEXYyJWssPAZKjTwqd8VeXQsyXQiprDk4X-_5X8qTj8zcDIa3y1yXOE1dji2QVlGKvPurg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=ll5FOOVFb1ETFkTaIWJk8L2wCvSDLaxuXVXNsYxMdTmCzyf3dG_yhPNvrRj59aqwXlu_fJTw7FdffVf9pdaPQx_Jb5XH_BRLI58wSQV-9etQP1r2m7Tb9IuitdeB1_xLE-He3pFty7zeD-_tj9xdqFHrOP8FVRdt-7ghAbAD1fd1OJ-Cks9RKlayMTrpwN_mYUkQwkMVWzyM2tel4xRRPxuYlcwKQYo51QkLXzjnD6TsywXMIhIbI2jipGTH9iBbLxLDjTO0Xhc1C4GlLEXYyJWssPAZKjTwqd8VeXQsyXQiprDk4X-_5X8qTj8zcDIa3y1yXOE1dji2QVlGKvPurg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH3BJGSWqYoutgI9r8-Otc4BI9IMj6rddID-Blw1cb6rj2ygSQJoxII5wxw2byz9mEzlhBwt1JSq8VvgBujvZ4lGi6UA8uQ0PwCx2EukAnL1ZyqJb0qWSoyNeFp-Y37jq2657BZsIP1odv5HjcyLXad67jjAkOMKxmFjiWG3BoZtlUx82Q4UjhQ8kcLQJ_tXXRh04V9RG358aiW5nRu2I3sjHLgogBS6gFh9k5F5LgHFhrmssZZSY8TyeXMNakeQrwmfvl5XTnmmz8nRovMoTgsKDVoGQt-NsNeLuXe3A9osWkTDMPG0JlBKg-0s5up_EZlM44-gmIB4DuQ45YRbnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juPhyuGkucOn07p6S4xROgtIRoHs3_r1DiSgP_UXtPteZTFmT1YVbAYHl5TKSR5HlzlTj5Mwt4OXPKvtoOVWqKPbJJb8lijDiQdhKS5CMx7katpI17GxljxKrpqmWQtuIwpgAHJpUUTjbV0nrfrSilm1zGgnJky2Cl2K9DlN13sWUGya-1jPxeA_H-kpXKy63CKmboauthgCOiiR9muAqIn3wWaYbffgkXytxi6BQkFEvYmlMrIYxd1kxaM3le4dL-uTZG4zI-9s3X8m6maEy6MyBFB2dHZEV6y5sFDPaX-jC-q18HLdCXINyZw-HLo5hvoYCMeLE0ZMYCwqLsL5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=g3DwGNyBM4JRmL5XiwWrLndyWjELxINbJ6t8Y3b4Uy4f7mn8YxOYBO_qxnK-rblrv4bnSdwYT-VFf7KK3WoYduEHg7ZUJF2n7dRxzzhSLOomudOXNbIlZkGeUMsM2CsRozsoI5_U3WC74DNhjINOyC0wnnMY_qrEcztlbBIREF9w9f9EcDFd10ag2GcjyzFL2dhDi2G883ioznVTZuV3ySrnvt5b4zujuDr3tnz0SduWbwN26zf386BwgtOZYHJIE2lNqK-jyj2tbglGgaltmhFcJ351OqjjTJhSAW-mNIbQrWSqulcSfKA6Gvo7eYo4Zz6IVBIYnHMn9ZmjB5tnp6Z7g3la3uadKUXOJDCfGiEkzkGzOINp31W9JtUrle5P9u51HlICjmWAZ1voh1fYE3Cgoo59dzDMDKON0D-y-yufTZrOfWBtXjyDNIJn9CtOOeJeULZqgwNjXwRFvOl6h4a_nWvRIbljfbU7M0sojT6oxUTHktaKvclFU3z-iDf43HNYnh1pUwsn2GMNuwkaysR90sDllKqurNRvzVOsABxe70AwTMl_gBeiA5wPESv4ilpSOst__G63dCP6v4vc7z94vPAByNUsO2EfvKPjYJYv9KIpL7TQllb3QYvf8Jrg625I6ImMGwEmcDekbkczu4Pgperm-Lcnicxv58w7mzE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=g3DwGNyBM4JRmL5XiwWrLndyWjELxINbJ6t8Y3b4Uy4f7mn8YxOYBO_qxnK-rblrv4bnSdwYT-VFf7KK3WoYduEHg7ZUJF2n7dRxzzhSLOomudOXNbIlZkGeUMsM2CsRozsoI5_U3WC74DNhjINOyC0wnnMY_qrEcztlbBIREF9w9f9EcDFd10ag2GcjyzFL2dhDi2G883ioznVTZuV3ySrnvt5b4zujuDr3tnz0SduWbwN26zf386BwgtOZYHJIE2lNqK-jyj2tbglGgaltmhFcJ351OqjjTJhSAW-mNIbQrWSqulcSfKA6Gvo7eYo4Zz6IVBIYnHMn9ZmjB5tnp6Z7g3la3uadKUXOJDCfGiEkzkGzOINp31W9JtUrle5P9u51HlICjmWAZ1voh1fYE3Cgoo59dzDMDKON0D-y-yufTZrOfWBtXjyDNIJn9CtOOeJeULZqgwNjXwRFvOl6h4a_nWvRIbljfbU7M0sojT6oxUTHktaKvclFU3z-iDf43HNYnh1pUwsn2GMNuwkaysR90sDllKqurNRvzVOsABxe70AwTMl_gBeiA5wPESv4ilpSOst__G63dCP6v4vc7z94vPAByNUsO2EfvKPjYJYv9KIpL7TQllb3QYvf8Jrg625I6ImMGwEmcDekbkczu4Pgperm-Lcnicxv58w7mzE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYqlXyBNhFmdq_oJpiHJz-54EWUZE0fSnZMFg-mKoN4iljeIO-eV7oNIia7bNjkAdqakEJxX4KR-8IYodTtWGr-BPYmhgHAkG0PAPXFJcl-G4V6BSJ8zEniORWT4de15shGfuShCKsCfeleWaXHCIgbl-onpfgPBmme9L2Wvb6ebnmHStccZtn1s0wL9DJ9Pnwm-_nhR05XpnTGw7Bq5nqJ8_jMP7vZ27GL1zDU35FerZrgTBIN5yJwQIXDbA42LENGSW3XmxOEeEg3uO5s1k3Qrrh64EAKFz4RcEamoBUlfqnLz3ZmvxHflq9zBpIy7zecUsdDpiJctIvlLsG8-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gICxKefYIbtW0pQYauMQ1TkOhnm1jAP_--iO8r19NzHk1KOtyoXLYAQpmrNVqf03Vp-22p7Kifpy1MHmaawU3oX-DwxQSXpz8waz1bSzCUCjB08whVvZ6lcKWZgist5s_poD5fyI80slDqNaeK4WA5lokjuYQvcWBLF49IMUfk2dwO2LedQpI0q9Fao2SMV7D8tWToeQbBhFqly1QDMBcFsgpJpdRQILLoB7iOgAtzDZw7GPF5Kr2kcwZcdgA6HMko7leC13q6kelXplY4ST-S5D9OJuACFKVrdBovKKYVR9E9oLkhC2ZUh-N282dvkGK9mZiZNCCMDSGO3CnnSvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=blsV_WXyELhwBhwdYKmnsG8cjBbdF9VV4jsY2YZxBC9R3r7Eu5jbTlKF9g0peATt2cOZR7WUa17fcAu_TKyZtdXXdErBK_OTyW16QgEkEUdlAWTpPhjXqmpj7MebhyfsCLz517WRRqgE2QUGrzVcyvaPLc-5vTDwPg9nH1XShxM47heqGTWH3W3NHR508Esn4qE_gcYaX1ZTjLlAmOIG05ze8x2gulDuLdKkxXjMDxXrS4ZH0SpYJzGwL5mYnXm_w3YHDNgyy2DkOpkcAQPvM_pBUKTPHF76r3A8i5gaigY5tvcBpELGD27PFD1IeUca-Wi9yvOvKzoySGEFYcwdkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=blsV_WXyELhwBhwdYKmnsG8cjBbdF9VV4jsY2YZxBC9R3r7Eu5jbTlKF9g0peATt2cOZR7WUa17fcAu_TKyZtdXXdErBK_OTyW16QgEkEUdlAWTpPhjXqmpj7MebhyfsCLz517WRRqgE2QUGrzVcyvaPLc-5vTDwPg9nH1XShxM47heqGTWH3W3NHR508Esn4qE_gcYaX1ZTjLlAmOIG05ze8x2gulDuLdKkxXjMDxXrS4ZH0SpYJzGwL5mYnXm_w3YHDNgyy2DkOpkcAQPvM_pBUKTPHF76r3A8i5gaigY5tvcBpELGD27PFD1IeUca-Wi9yvOvKzoySGEFYcwdkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=tmxiiD4tybqufyVNTrtxZy5jGWp1E78FyJqaDVJiImhlLL1pUewUDHSsDMfJ3WKy3OoumphXWNWwOPqWpHV57ypc8Q7QIM1xF34uNQFplENgJEczY14dsmt69jxe0Dh3HG79tcmPR670oVMcQsJo21Bc49vssJwGgjTzkrmVHkuMT2RJL9HgyPMWCFrjG8FjvkCjpflhjw-YBlRL_wfhKva6FJSpCRu0cQ_GTY1xXjir3HwGTRN_L9MMpI6QlJfHhyxHXfSGLJi_DINWnTE22O7HOKYoMOuNQGNZ5XGm9Hff1Ww7t5Vb1vz7fxMK8JD5jHN84gSEAv8gIxKHWFmZlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=tmxiiD4tybqufyVNTrtxZy5jGWp1E78FyJqaDVJiImhlLL1pUewUDHSsDMfJ3WKy3OoumphXWNWwOPqWpHV57ypc8Q7QIM1xF34uNQFplENgJEczY14dsmt69jxe0Dh3HG79tcmPR670oVMcQsJo21Bc49vssJwGgjTzkrmVHkuMT2RJL9HgyPMWCFrjG8FjvkCjpflhjw-YBlRL_wfhKva6FJSpCRu0cQ_GTY1xXjir3HwGTRN_L9MMpI6QlJfHhyxHXfSGLJi_DINWnTE22O7HOKYoMOuNQGNZ5XGm9Hff1Ww7t5Vb1vz7fxMK8JD5jHN84gSEAv8gIxKHWFmZlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6A-dc0G77Z3YzAIYcFVjhnqAby_RIG-RHw5oRwORuxGNqwPbj_ZMyCVXbcYoaOMZTPGpgi1sTWTjdmYwWhyro7SP3TI1RBby6KqqOftd0NphP6MUAKLwPlkZElREAM56XJ1RVOLZW2FVZYE5wZlgE8r3_tCjmgACR6UgRHm4VRGvkwswJ5j-FeZcdeqEzHJEFS11v-moxwk-V3C8sNLlt_66-1zOw8l1pippMqPaoUdN94CLP3blS37Rzuovk0n3f2pYcnsugHqfuGAIzIeJci_6MfLoUGidUMK3PA7hhhw6EK4S192ax2kePGbv3TEY2IVW7whJkhO3zf5gHYLrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfUmFK64sDuwksQnKD9yq91YOTK1X8Su5JWMSvIdCAFAmh4AXj0Tlj-BjCcoRkjNg3Ht11USFnqfhQrHK_nOouQT-UwOt1W9JqEuM4tVUn8BOPCkIO2Wn5ajrKnly_sMwdmblh-B6Kjdlz8Oj25YSSqSpKPwgHBSkUYM2m3y8udWxViL9Zh9ULf3Mhmqqr9GZUb7fkRO5lPqQpSsDD2KcIkLkWLFxgDBfRsuPBorZP_vD1hYtLZXwAtg77mPoWzazcK1sT2I2DN5W5IjGBku6w7KRCHpavVWimUrDWvXjpZXdYywBqy3Qp7lXpPZzJQTPau4mHF5LsMyMxOQwKmEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26735">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wz_6_ZAldARu42Ax-BjdEl5eVEaHwSI--dEFoTYSguynULgFl44uIYEjfybGsWCpOF74uJLKRc95nUw8mKTf3gn1UxYQOSIRD5dfgjzVOKqcahNApCoZSq-7X75AJBQCL69qRua1HfNEnAZtP_y2TNYOKlbfReYIgNmRSAJDRABWpyVhDKu--8ixjbxsoVP03BP_RBK7gmmQ5g-G4XclAsUNVppm22ZMY6H13mNvU7IGGibud6zwNnitFcjCkoZ2RPlehqydngmrastMLVQSg0zRZK0Mmnj5zL51SWXfD8Zqj5JIPloha-lC_wNBywQxB79_EICCW75hXnBFCP3LGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
🔥
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26735" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oshNibq_rBML009NgHjFa1_9TeABco3rUOJy_doIm2aXx0qj37puZSbLq4z8Z7UGq5N3noQcegCdUt3OC5tH-oQWmtlwvIesNwpyJcn2UGjSmlexi2A5TNwJlxEtsQ9V9GMt6YGwehtxIbBx1TVKy4PBcalyvWdemOQ54iUSuxaASIMeQXrGk8ZTvO9N_zvyyPjW2-2nFso1hK0Eoj-lt6O5iTas2RmVjj4_hAhEhs5KeTh3HXZ4W9ZvxXW0Rf3pPSTAemVdyIRGlBSlOlwZMHKEgzJIE5cQXsKdqRcHdECY3noleiS9jCWxsEiN_Tse58PiuU-Ymz9RiY_X5lF6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=MFxSfbaVfyi_c7_RU3tkvTVUaO_UvuqXSV-iEwSyEqzyb1OwaVE9VGN6WyE4FPhtmLLuNeaG7i8wIlYt-WtWQEQh4rzTMm-VTuVICo3sJq9SBvPMH1sR8qrlHu_J6IgXApxH3rtfhAPWo0Tcono1zWqn9NIXDyO4UooyVpGglg__5Eo4z0Lriu7QGnrpAMR6xrSHLEcnJlcNs7vw68BStKwOXEAwXgUSwq_gRp3CXoOKjrMdREJB2FeMbaa3S0wP4YdQMoXxiMizvK2E9Kog2WkWVuM2IvGjSNbMjU278XVYKvnmwdg0L7zxlDxI2mv7Ly8dM1WeJxcEzStsZt4IIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=MFxSfbaVfyi_c7_RU3tkvTVUaO_UvuqXSV-iEwSyEqzyb1OwaVE9VGN6WyE4FPhtmLLuNeaG7i8wIlYt-WtWQEQh4rzTMm-VTuVICo3sJq9SBvPMH1sR8qrlHu_J6IgXApxH3rtfhAPWo0Tcono1zWqn9NIXDyO4UooyVpGglg__5Eo4z0Lriu7QGnrpAMR6xrSHLEcnJlcNs7vw68BStKwOXEAwXgUSwq_gRp3CXoOKjrMdREJB2FeMbaa3S0wP4YdQMoXxiMizvK2E9Kog2WkWVuM2IvGjSNbMjU278XVYKvnmwdg0L7zxlDxI2mv7Ly8dM1WeJxcEzStsZt4IIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=lXxQWEhV_wLZ5zmQo-KkKnENPa8axR9p0rKis888hOliG70Hd_1KHmlYnY52l7uI8qH78BmajbGkSTm01QeqQ1UIwbdebHbUkd2e6VxvRi-ZwRiLQHqoxa2ke4RnG9ipoJ_DU82L20GTHfbaaFtK51y0FmcNgbQFhQ69sC88-A-nVkBveof_TxEs7GR2iowtsmHZp1_akcQ5VJkm3Wc7Uz57iZr3FKxm6tFN_qDBbI8Hfu5XZptGbY_8-469uyxwYRoHqTPr2KxbhplFosA07a7rr0N_OJ8yOas6O166ZgLBwh4geGNFE9cLwRDI2dxr-YQUD-zWlGBs9fC5kBiapKT4kSHLZfVs0MXFNrLai_YQNtUJH6Y6LYX_JbKOX9_JfVUDORPrT9Z3eXevt0KdVf1u1GMbInwlyaEUkMkNPSVHftFRpxpPo_yq_uwr1hhwQWAHH9pv3xhgFcd-Xj1GOLcCXvld_DeRt397PiO1w1rBN8boSPP4FHI8A0JBchX6lDgrB5VSWZkq9NaplQIN39hW3-75n5yB1_V_A5ydaHiqVWrZtDri1WUgvYlJrTmLGeruH6BlRjO4QWHheOVzexqSISNo6KpwRjr72T4eKmmG3rTiXZkM8m0dxj8LhaYipGf9Oq3L8bhIAZ22oHA5xUkZjI6DAWcE6fzHr5YASRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=lXxQWEhV_wLZ5zmQo-KkKnENPa8axR9p0rKis888hOliG70Hd_1KHmlYnY52l7uI8qH78BmajbGkSTm01QeqQ1UIwbdebHbUkd2e6VxvRi-ZwRiLQHqoxa2ke4RnG9ipoJ_DU82L20GTHfbaaFtK51y0FmcNgbQFhQ69sC88-A-nVkBveof_TxEs7GR2iowtsmHZp1_akcQ5VJkm3Wc7Uz57iZr3FKxm6tFN_qDBbI8Hfu5XZptGbY_8-469uyxwYRoHqTPr2KxbhplFosA07a7rr0N_OJ8yOas6O166ZgLBwh4geGNFE9cLwRDI2dxr-YQUD-zWlGBs9fC5kBiapKT4kSHLZfVs0MXFNrLai_YQNtUJH6Y6LYX_JbKOX9_JfVUDORPrT9Z3eXevt0KdVf1u1GMbInwlyaEUkMkNPSVHftFRpxpPo_yq_uwr1hhwQWAHH9pv3xhgFcd-Xj1GOLcCXvld_DeRt397PiO1w1rBN8boSPP4FHI8A0JBchX6lDgrB5VSWZkq9NaplQIN39hW3-75n5yB1_V_A5ydaHiqVWrZtDri1WUgvYlJrTmLGeruH6BlRjO4QWHheOVzexqSISNo6KpwRjr72T4eKmmG3rTiXZkM8m0dxj8LhaYipGf9Oq3L8bhIAZ22oHA5xUkZjI6DAWcE6fzHr5YASRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1VCF0D89oZH9Z0rOs9aNXj0uSx9RBcWj6E0GiHdkJFyedFSrf3qEOOjT98ft75G9BuAhu0odyobfXKV-Ro17Q7Kh4VeK2hFqh6sh9ZHzSaLxog-PfeKEjkrHZjWTt0PYmRsiNc-sH4wscX-xIC0Ply3YevVEdjckyVXCD8Vq5E0Y2kF0CF3wfaFyeKxVJNjWXS5FNfwsV-U7Br8VVwxcTj5DBMzT6aAkTDuGH8HNWcuhtpOF_GDvgkkZOIQHPIGkz1KcTWOh4Wfj4ttiozt5tc5Zm7Hi_eTi1Io5NON1ckhBlXM7gnO31_Lu9FldBW68NZxIwrMTGEkl6dueMk3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNr20X_69vkukXoKQbYNRIE3gvcPZjmBNq9fWgbiZMTzHmSmphPzIupnx-CYgnMyRgJJfFlKZx-SIAl2QfY3MGoalXiAvGSv9xNX4EbuGFFwp2QbQV2ykS3yen4R_aEBd7E31frRtoimSuPcMVmQJOJYqWfkMxzFfClU-7iz17lc3Iy-AjtJLKMhu6lbAq42zt0L0tcpjtzU5KMga5RE4pCkCJJkeepm9HSjKxLJskVY-ac-KOCjnVtGQIa2klPFxGK_mf8H75RkGAuXdgLtk7Nloe1lAHyvFmJYugNhtuZN4dTaejkhvlcMrL_mFZ4hn--3vsa0E7uCM4mj0C8raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26728">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INqfrlHVSJbIKdn54d1Q_qggDxGIx6x4xC4Va0uRk_ux6sFLUmyRcgtThbde54DvAulXSyutySzthNB4OX9zbpUzBfhnOdRPzdGPznkuGUPejrDLprM9_fryEMlAVX7pLKLsv8hTDxwqZ7kEFj4EL_ycD-QVGqDSo5X5naITSe2ZOaUJA_82G4hXETcHqR-OBLs9zfuqbU60_mWBhgjIUn1t91jGcYR8HPNjy6o82aVtnwpV8R8bxM7O51rZNr8FiFRF-iZ02psTKc31x3dDbo2gU-BezQ-WTYCO4RZUGwi3PYUI30MLKm4esFLJc6R7Vb3zkn5Bq7LHPfOzBTRlqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
برتری شاگردان آلونسو بادرخشش‌ژوائو پدرو و بردآسان سفیدپوشان مادرید مقابل لگانس با ترکیب دوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26728" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kc-HKXwXfiH-Jxjw1yXCe_Hmi4qnYd07dIa6H7mm9VAdBlQpfh5tZj6lGjhwwmC6RD5JxkRVNPOQslAJN6c5fTgsUsqIJaQeFn9R-QFF4bfi77q9OhvYvTpboOdJAzeZ20JL0011D25gi_f9TBh74cLHkathP0WMU4ff_i0qB_z6-rxdMoI6e0FaTkaCHW8INLjR5yktffa8lvx_SjZp-sODkgUyf9bbsoBabegInFZmyCOFMQxpTlHWlTreq2LS4wGLdgo15mqnOmd9Kqfdjget52fuxK-sW4mGV5oS7epqJhoT8_AFID3qSFVcfeT5rEZWKffRC84WIKYdbXVl7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBXPk1sz7Q4PGYd26KPgFBNE48ak7b-_CRZoCVHq1O2ZJkpfUWMN57FQyL0xzNzus0_Zu320aVEn7QDhRksEZLI-48dtQ8PlkceSoiMHXrsiIvAw2cKO4YPj-OmgDDwTNbmb6m01jcUAr11VbbakKs2GXZgXP09NrverKAZbNIGv_Wlqka17q8xzPf3Aw7CmNWYXF5PA79-8FvwKwUfyvn8p7odTN4P_9UbLohoQ6TqiJPDQU74TGiAF9vUl5ktwh-Vb-vx-qXdxbVlGze-JOY6TJh9OV22xTJPcgQJokc5lbur4JlbdLYVX4xuO5aMeuWkHpi096wsNfednzhMysQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqC5LEzitrfPqPbWG-B42YvcUiHOKDUG90pcloxwj76TogCUZpLiwuDylzsDCm3D0J4UnO9jnYXVT1sXy7SLfGAhq1eUTJ7G0ZJBTzScuguyi0JitavjGkD6P4VKk2Em887TMydq6BR58UWMN3lC5niMpYQzxqurRxRb3TY7RCwx3HjSWAGNvB2PzqLGk5uehPArGsAA5UmDmlRDfTX5ptYaL0kd6lu3AdWawmOGcnfy_Z6Tjdegcv-jvQnFiCvhbFC1lkYipcMJwk4NbgVmd2SCGlEChlDV-nVuPk0RjwJgYbdx69aH9nC3hn7cprzKYt9nhxVMlvraRZyyU1vf0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfHlYN1xwX56hP_8vIrUCMz4aSfR9LqitblkCnLdDJz1ZXKYEIOTOQU4nDOMLwHVHEOehyfCMU9B_zwxtGcf_uAnHvvWD_NjD1aKztpJqx5CXMIV-iA55oyLVeYBiycXMrlUc1Owrc-7ILY__q1zDUkOIAzcdz8cZF0v2X7sunH5P4z_kVsbrb1z3SdlN0lCQHs18pXbq3S7Y3S5Qh4Tr_e8XU5l8ABfRAF-PzHNR3QXzEhjA5sxEBppM1oKtb5VyGhyu_BYXOL2R1ebUF17AFt9hyJV7zOfiw2shWUQrHjWhdyG31Pc5vc2465jkShzUUd7CKd2S_AS231laN627Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26723">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=oFlR6Xcbgo2ChhTGVLcgOi2WerQCAjSJr9IILlkzpQn80UCXKyKDWkDHoogR2WoiZCZM_t70xYKS7p1MZOj2ALBLpcA0ZFRV_dM46S5S7ycPDCwSHDoXUPzXACiY317q-pJkFDW-t0tPKRsELKrp2sGIJrcbGB4YIgWmeCn2Df2sWmmqk1DxPZKXvQ6oGFGTAffaIq07nyA0e-ATczHeDIgsYdEwIcaAjBN32Y5j02yh5bpYIKHsdKfLx9j4yUl7-281al1LmHXw7Rubd3M9VfX3Y4KbxN_P9k-ZAL-Or6tmTMqGUYnTnsOGyGM9jTk_DCKhSzP_OT1yuxrjus6DKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=oFlR6Xcbgo2ChhTGVLcgOi2WerQCAjSJr9IILlkzpQn80UCXKyKDWkDHoogR2WoiZCZM_t70xYKS7p1MZOj2ALBLpcA0ZFRV_dM46S5S7ycPDCwSHDoXUPzXACiY317q-pJkFDW-t0tPKRsELKrp2sGIJrcbGB4YIgWmeCn2Df2sWmmqk1DxPZKXvQ6oGFGTAffaIq07nyA0e-ATczHeDIgsYdEwIcaAjBN32Y5j02yh5bpYIKHsdKfLx9j4yUl7-281al1LmHXw7Rubd3M9VfX3Y4KbxN_P9k-ZAL-Or6tmTMqGUYnTnsOGyGM9jTk_DCKhSzP_OT1yuxrjus6DKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
یادی‌ کنیم‌ از شبی که جود بلینگهام بابت پاس تماشایی تونی کروس به وینیسیوس جونیور او رو تشویق کرد. بهداز خداحافظی تونی‌کروس نه تیم ملی آلمان روز خوش دید نه باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26722">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9FWvwtUVAtMxYEqONN97EzDYjIZCxASjwDTTK9BMiuaCntuhJM2rOpRL0TjdWrmjxZRFLt9iNtY9DAdYaXvG33bhLdxN0anwOZD10VHY9vKaBVFV6qaTxGqVcq0xVVUSMZUbH2DfrrM5cG8ZOrRVLQ_Jmod1qtcyZg3NQU86HK_0zJ4Pfuz200jK0Vay1HqRtJbITd9GVplb5zbweOcCTsJ2StbtZ-TyunveVAAg7K0hkvYkw6SzhuXJiOVOafBpLrKmP9HRNr_jFTD9legHOWIfBvUFnY9HKnPRk12x2d2DGjJbjh_Ft9S70TOfhWQFyURYyYylKcLX1ZQuc3-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gauCwK5PyXICQMAF2-Fs91VzpLjghO_ylXuXO5mFkRGpv27_QKeFLWigoDMkMrG9JXmie1iUQ-SA84Lhbsbr-Fk6rjniSGFLR9Rvaw0bB735A7ONElyB7ZAN2NzsTKEmJG4OpgZHVWBiypvEVoC8e8XE_7N_qRt-ExGnr4XTxa2ohTFGr5Uyf5A-_Z3df5xrFqGTR8iWj3T1x5iZh0fZ2DUIy-UT1UPgszDutIG6pDgyHrcjoKubbMCWfNBbTKz3YxMnIIsKKvsGeabcAGMvFBzrWegjIjXhs7WaKHeMF_f-nvs9Ob1BfjfNMw2Qt2graAu8Sq9hy-5WlKgDJzOcHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26720">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCA2aCvGjukC-iWeIpnxVCWVxs-Q8L5b1qrSPj0Aur2vmXw1TbddD3H4iwLdEC4s1atyuyb48xWi0sahBx9nZMn1jWsEZSz-7vzfsG2mWeYhsbYsp6_es8ORsdq_IXJPh1fOfOavMVcmwA-3ePTCjZw9l2IpNjl0pCXBfXECYbnFcHbfMReNu1T_DMOyekbXDHYwidAXxPxl3Y9joxKu_1Wr2m-3-zHSF1-zfECXZglfl5Qfjof8RdSUb4Nc0eNGaYtnW1EF5R0UTOjQrkvoi-WuZ7YcDlDpySFxz9oSd1P-IWzvH7EyPitNaIX9IpU8Ke10aQzgU4RRVw7_Nt67_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26720" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26719">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwJqK0aA4DwLMMAXIjfMoYWsiSBfwFW96n7Ws0aKJMPzvxqGaFUhWG3rDVOaTho7n03DlUuQ-5gWjYk01t9nBUvxeo6jxN-Q_Hlo53kJq-QPeye-qNfUAzQY2jaEKcvNacGkcL9MsSCFSYBEIfU6r_xsnQ1mZBJbDYLcRMCG3MsTypBy1LfOG8r6B_92JcBLGpLnhAkB8rkzGUR11penee9wvjTcuCNbPBVvGD1Q9zYnKFg3K07jav83D1XyGlz535zKRNKvEcO5zNun7eUlkRwHqtHnjq0Q6BOJf4I9GvEmB8xBk7zxbnN6Jf4EikEI0Dn9DifxWNSWlt00HgqT8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکی‌نیکول:
یامال‌ التماس‌‌میکرد باهام باشه‌هفته ای ۲۰ هزار دلار بهم‌میدادکه باهام باشه‌. یه بار بهو ۲۵ هزار تا دادگفت‌نیکو ویلیامز منتظره برو باهاش وان نایت بزن که من‌قبول نکردم.میخوام‌از یامال شکایت کنم و به زودی اطلاعات بیشتری ازش افشا میکنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26719" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26718">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=haaUTxqhOpXPXjGp7JQ4EACMe_Zm34LckH1Pw_JTvGaEf5_cMzgDlQNaEEne_o-i2btlFKoiGzqB_e6isnLsF659AS5kFySA4Q6hxX-TC6WF5Lr4GWBsmUgzcNHdyiwD3tZcQZ1SoQlpfleTOgcXGZtycTapUuRzotp3ergRpkvvY9aChJKUGwf9d0l5bH2y5XtHcFARiQySxcAj4ioUn-6-d_eSRJ2wH75TVHoLn9VaF-ATzVI1eFXOgXO6SaZ9_Ry6MTFFjsYYqzq-DztaPOwC4564hlXxxRWhaDXoG6mkcIhFtBxHaJL4O_Z7b82aw-dTulrTBcjsBiH3QdvbbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=haaUTxqhOpXPXjGp7JQ4EACMe_Zm34LckH1Pw_JTvGaEf5_cMzgDlQNaEEne_o-i2btlFKoiGzqB_e6isnLsF659AS5kFySA4Q6hxX-TC6WF5Lr4GWBsmUgzcNHdyiwD3tZcQZ1SoQlpfleTOgcXGZtycTapUuRzotp3ergRpkvvY9aChJKUGwf9d0l5bH2y5XtHcFARiQySxcAj4ioUn-6-d_eSRJ2wH75TVHoLn9VaF-ATzVI1eFXOgXO6SaZ9_Ry6MTFFjsYYqzq-DztaPOwC4564hlXxxRWhaDXoG6mkcIhFtBxHaJL4O_Z7b82aw-dTulrTBcjsBiH3QdvbbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26718" target="_blank">📅 22:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26717">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFr9xw72lavNP9eVAoceY8abubkqp3q2ggZ5I_xSwqQswwtwzBWqF5Yv8pKdxJn-CxgJCS8mTqXPItupLVqxk-yUWTS1Algq-1pz3F5tOzmqgc9MVhy2QQhXoS4sATkMIWyMxC3EZ-KRfVlhzviUq55MSVU1viJmWTEBQrV-E1cbu--hDtVSMQBSyi5VmCx2c-7qq4a_DTP31CSeLLQbHK7ijZU8CRgsP47tnev9VJDxa-v8jWT_NeVe83eAANFK3fiG8bGbRj7pA-0xDkPy5OjULkqzDzKeilo6N4dDZeLB3gNbIzVanr_fcFOYJESl94nRzPSPmSOxmMs7jX69GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/26717" target="_blank">📅 21:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26716">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8Hp2qmfn0_HkTxQxUNcJeWC-4naHeJSQLZ7949_3Q1_T8g5eDhhB_XE1HrWEuI3tF0S-i-bFjnZ_KjsPN7wvAK34ew2ZTM1UTvGyhKDcGinw9v7M-qq6a9ZqR_rKfANi7vv545LuyRwTMoJhMMFVcB_HsA_TKh46weauxZXnbr629W4BFm1GioPBR_hbfQxlxv9R7URC2nR5FFDQx6G4C5N0wnVoLyz_khwoRfHdkpbtOVhRYHMaqMBuugxbMs_odH_taHiOVDvsHHjAmmwqBL2fgbe5ZjhWfS7cxzBFwZamKhstBWQ982zJJsSNgn8cOnn4S4pwCD3PMa2W4p77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه نساجی مازندران با انتشار این ویدیو از کسری طاهری از خرید جدید رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/persiana_Soccer/26716" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26715">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YurxmnfX5UXQXctjigXFmsTaKfrRNiZqsFDsBFF66qGjxycT4PFzuC7wwGllJpJPp4w9bu2JFuYV6HJcEu4gQm-X6v_PXcl3AaI06XLLDHTf9iP0Eh6Hh0qlPY2yXGBgjfb0CiidL7WGy8praNyJAI2gJ507cRbdNf6DiATFccdEGr-O8xBe-tvy3l0vznjX9wedUVs-8sUy_H-J5hjRO-9pzJJl18IoBE9ITDIkAAkQYbqTw7l5g5sgmzcrGS6TkbX0Ahg_5SmAJFxLZfTkag8Dm6jG_J8f3b454qY3yxdKcB-8q8l6r88UN5DGRd0ff0zKvyqtRh7A3qYf-PS_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟡
👤
#تکمیلی؛ امید عالیشاه کاپیتان سابق و با تجربه پرسپولیس ازطریق‌مدیر برنامه‌های به مدیریت سپاهان اعلام کرده 72 ساعت فرصت بدهند تا پاسخ نهایی‌خودرا به آفرطلایی‌پوشان بدهد. عالیشاه‌ امروز هم با مدیریت فولاد خوزستان جلسه داره درصورتی که‌پیشنهادمالی بهتری‌نسبت…</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26715" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26714">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=Xm0matw-GfOIrPCI6mmuxBn-57KusjRnmZZwoyqwvuR9lrXHkoyrwtkJQANhx1SAgKErBuXhTNCkz0rraCZGy9frUCIeGThqzx4ViZIvXt4uwM9ak8vh7kh6UyMFWcXSD6r5f7RA9OOyBVSGp4LUqUDhHjp35hQaqppj6xL7OdUjLeYrOelnxSDNjosels4_rtchINBbfBcC21Cz-guiBOq4B61i7q64iOxCkxS2oV9H5Vu_oPlL1ApRfzilS9ylY8W6mBs0Jo8NthLh4O1RdbF5HgNzlgNj2gnZ722ZvIRIZsOWqkSKcKEPD0vMH3_c7Y7XhcXPiQ3JQ_VQMUrWhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=Xm0matw-GfOIrPCI6mmuxBn-57KusjRnmZZwoyqwvuR9lrXHkoyrwtkJQANhx1SAgKErBuXhTNCkz0rraCZGy9frUCIeGThqzx4ViZIvXt4uwM9ak8vh7kh6UyMFWcXSD6r5f7RA9OOyBVSGp4LUqUDhHjp35hQaqppj6xL7OdUjLeYrOelnxSDNjosels4_rtchINBbfBcC21Cz-guiBOq4B61i7q64iOxCkxS2oV9H5Vu_oPlL1ApRfzilS9ylY8W6mBs0Jo8NthLh4O1RdbF5HgNzlgNj2gnZ722ZvIRIZsOWqkSKcKEPD0vMH3_c7Y7XhcXPiQ3JQ_VQMUrWhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26714" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26713">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=g-Of-4h6xruxFuzty8zOd_llQCFiKUL4wJqJMax_UwR9F-q9kWuQyGPDDjLr4Woaa2LH470Jjbaqdl2MmAdB53ZGEd3o_Rrf6BW7-LbYF46cyp3pZqb3dAN4N53NHXIpT4sdGUSpAAWhHe7vj6lQ8MYYWAlp6GZKC12UDWg4Vxj35XLshbNva9Dku9rJ_U7DLm6GNV084Sq6uQMxVqgTD1RV8_E0eCeH9R19aKxjFo6wWgk_AzGGzjCFYLD2hU7yWkAn1kjCX4oq8Z7z1h8aXupGHN9AbAQdWHvccOW5r0AmnTPIQ8F6bvRLsHUHkoA3ppvBX9pSrdfpooh8FOYZYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=g-Of-4h6xruxFuzty8zOd_llQCFiKUL4wJqJMax_UwR9F-q9kWuQyGPDDjLr4Woaa2LH470Jjbaqdl2MmAdB53ZGEd3o_Rrf6BW7-LbYF46cyp3pZqb3dAN4N53NHXIpT4sdGUSpAAWhHe7vj6lQ8MYYWAlp6GZKC12UDWg4Vxj35XLshbNva9Dku9rJ_U7DLm6GNV084Sq6uQMxVqgTD1RV8_E0eCeH9R19aKxjFo6wWgk_AzGGzjCFYLD2hU7yWkAn1kjCX4oq8Z7z1h8aXupGHN9AbAQdWHvccOW5r0AmnTPIQ8F6bvRLsHUHkoA3ppvBX9pSrdfpooh8FOYZYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پست‌جالب‌مجتبی و مصطفی بلاحبشی بازیگران نقش‌رحمان‌ورحیم‌پایتخت درصفحه اینساگرام‌شون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26713" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26712">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO831H7nO3zCEqB_e2wU8EvOAZogxKx5mSGsjYX_GKRgDw7FY7TCRJWxxlVQweByg9lCAkB5dZokKVEXIa1XHys6U6q9ng0xnkeexhH4Y5XYafRARyGdj9i3j3pvskMJIQ2zsTR8V8vNNtuS1dj4wq93QzIbqpBZfWo9r4aOr0uLkJnq8lVR2FM89OTsNjVMrgPrFxKRu7k8vEENXoBkcxC0oBfk_s_0rsU9F8cTzFhomI-fP5i_01Agpa_UfeLGepYTg_NvsKVt5iZPiGLSlgzgrOdj7jtobiFcv3GoT5AJx3cmIJX5Nh7Baf64IH6nvzt6av2DnLtC_phw3XrQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26712" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26711">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9jxP7tnpPZLtHo9lRtsm59RLvyM5Xow0s5XgBTvJfK7WU57CgkJ4mMAVn3zul35T3rPJraal99iM1yxU1EY7em_i8i1_Tu8952jKQN5wD_qFlhGRFUvFJTirIUDMxucErCCnqLdtWtCAQL1iUsUZKaBfgeximgUw-AP2ljt-mfr2qUObUK56-IAefOJ7YqY8YmWkP8MNC-P4l_XL-Pd2pIALOe-9iolfwrcZ73xi8_tDGM1Uye9ICbHqFEVcW8Q3hC5ZwIc33ky2P_BNdJvrfVy4OiH5EU15iqKy8tlK_TKVRQdGmTFdNH7z7M6SzabvK1t5aJUTsXBp6POBP5zRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26711" target="_blank">📅 20:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26710">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=JsWyyCrcnSCzPQcozatDXt7u1L39ZLlCp8a29PJqz3qZdeoDBJ7_4XxedTb_T1ks7PNK7KyZQIMKyio_FJf8iCgmmFXwZOn4n8kq90NvuQFZZGQH9ya2tcJOn8pCSLj82PPwcJxv5a0krrXW9Fb5J2tYOpBlSfpxiYcqsLxmxAJ1Dp_w9TBLZr4tP3M2mIPjoqZHVWSiv1qGcNprjPuQ4XekFC0G5PWVpuuvnHdYwKaRs8sMgn07Mq2CzRoFWWen7QxHe1vqUujAyusouIz6dZTkA4PdUREzA6zUP7OceqcCPdDC9p7M6_b2OPIHgsd4gjF3qIyPZKOUbHyW6YH2eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=JsWyyCrcnSCzPQcozatDXt7u1L39ZLlCp8a29PJqz3qZdeoDBJ7_4XxedTb_T1ks7PNK7KyZQIMKyio_FJf8iCgmmFXwZOn4n8kq90NvuQFZZGQH9ya2tcJOn8pCSLj82PPwcJxv5a0krrXW9Fb5J2tYOpBlSfpxiYcqsLxmxAJ1Dp_w9TBLZr4tP3M2mIPjoqZHVWSiv1qGcNprjPuQ4XekFC0G5PWVpuuvnHdYwKaRs8sMgn07Mq2CzRoFWWen7QxHe1vqUujAyusouIz6dZTkA4PdUREzA6zUP7OceqcCPdDC9p7M6_b2OPIHgsd4gjF3qIyPZKOUbHyW6YH2eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26709">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQcQ8iSZMD2rqswW7_fSgE2mnM6pt3XeVVTUoiuWloKyZsW_V8-4XW0ftBkFBLGchOH9UqevB6c4ROZBf_Ca-PyY6lGWjN6PAvEUBcuIMQgPg70VKrL0Pf5L_k-KY5DAnFr7CaHuTn_s2DgFMnMbWADypHSfKIf7J_MHfdZrXppcPrzodJekWgkDUVc2etS1TPF0BmWTnPYJ9zvEO_EZSqCAChFAcyK3i6w8j8y71zuTwtv5r_408DUTPCRGGmC72W6EyumPHvz8H-By9O_wSNcK8Yv3865O651OWENW7a5sHCeOzjt9O39JQaLa32ixbhNVtWaIXU3bnuyl3r1Dqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26709" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26708">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBU8TYhagnjsZHKbww26HpUJhsb-XgemB7ofDMhR06zrNxIzWZl2WFwotCtB4hWH7qDY1TbXNG_X7nFfFm-A_SbY59C5rX3psnczmczpevs2MG2RxQk0GI7cfJ1U7VIFaw1G2iroG79NaZcIEYE_ZSZFLl2Ry6YXhA_UrjNIILDmw7lBZ926EJ3_fgw9HP--CS5npoQWgf7GUOQMk5M7KPexPqq116-I1NjT7wlBzLImBbLxfx7ZW52h1baLJODqJafMmiK5x8R2mOBnOo8KTsxMnLSl1t06oN7ZY7B_28la54mXCs2taeYHviI319r6RcNZU_D4aTAbkBnihFJ64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام سازمان لیگ؛ لیگ برتر رسما از روز سه شنبه 23 مردادماه آغاز خواهدشد و روز 2 مرداد نیز قرعه کشی این رقابت‌ها انجام خواهد شد. البته همه اینا منوط به آروم بودن وضعیت کشوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26708" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhJC1m1P0NgOfm2_p1HJfYE6EJksdurf9bZX3DifBMadXmzLtWjThpJErcYm9ZjwNsHZBq7zRoqiUFnO2uH1NahV1k0E0w1KKt4pIHHBz-ccofG2y7qrEewDyNWCwl8RnM3X7DPM6tBhtGpNxvGK2C9WEex5I5q_jAHMI491HjaKNqifVKCSzZBHXy_cYAxVq6F1zk9MAnBmJ77cvCwGpG1QdfqeywkEJ3HTaFdDBhHjdO2yWVtRNzLWuBqgiQbrL-SfIuLgqmVA165Em44i4lmyfROKvpBZFS0l_oL2puCe0dj5GOXtBz6f2RyF7K7Q-lSIbcxzc1LPzIXirnsMFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26706">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=GYnilr7qWIy1wAuHwr1cgokIPQbDWJNSb2ZoiG02ZujZFjefgBsqQr1CNEfsitGFGzvnCwZXlM4LZL_psmr4Q9iftIYnO6niG1e20aBvgTDGEg9kMP0QAcl1cb2j11y5ewQHzOFHo4-Rg-YAj8CfK5iqXEf8W6jVwNtSentJphbpnmP1AjQyFogpua5u3-5do7H6jnXbyQA7TmIqTYMyV5v9hU49XjNN6VHWW68OfUpmK2HTs2vkxAdCYV7bmffdyyqIZ6Zt1U_8CDkOhu3cVXe5-FHpCaXRRYAkxVsAU4WbBciNp8_ZjAtrgBuzjemST69f31Qqaklwmu28q0qsypLZ1ZUGBmY0eipCFwEceTfievRC1q-tE50WZCiUW36RBX8h-ECXzEriguUyccj2nzYnfKCmO3CL38PxjHadKdR5muIe9iM9DUOvAcv8CXSE_awyAZmtgzmBkU3FdkAVuMp7K_xHpCl2S7MPNFpkJmMSe02Nuy1HYrwSwWRgsaz_srD5MMWdDky7tlZxhVd9XsamirntIX7elQpmxTV8foOT8AwNOscrjFCY833zq9Ud7Jq5EEBHeCvOhRRnk_vDlqqnWhc16GJBt5hOuGHTxmAjcgSaQvUuTHpHZmtYOUJiRG3tjdXPiEwJAsRzzMH4l2aM__2EMTsHVlOQSCf040g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=GYnilr7qWIy1wAuHwr1cgokIPQbDWJNSb2ZoiG02ZujZFjefgBsqQr1CNEfsitGFGzvnCwZXlM4LZL_psmr4Q9iftIYnO6niG1e20aBvgTDGEg9kMP0QAcl1cb2j11y5ewQHzOFHo4-Rg-YAj8CfK5iqXEf8W6jVwNtSentJphbpnmP1AjQyFogpua5u3-5do7H6jnXbyQA7TmIqTYMyV5v9hU49XjNN6VHWW68OfUpmK2HTs2vkxAdCYV7bmffdyyqIZ6Zt1U_8CDkOhu3cVXe5-FHpCaXRRYAkxVsAU4WbBciNp8_ZjAtrgBuzjemST69f31Qqaklwmu28q0qsypLZ1ZUGBmY0eipCFwEceTfievRC1q-tE50WZCiUW36RBX8h-ECXzEriguUyccj2nzYnfKCmO3CL38PxjHadKdR5muIe9iM9DUOvAcv8CXSE_awyAZmtgzmBkU3FdkAVuMp7K_xHpCl2S7MPNFpkJmMSe02Nuy1HYrwSwWRgsaz_srD5MMWdDky7tlZxhVd9XsamirntIX7elQpmxTV8foOT8AwNOscrjFCY833zq9Ud7Jq5EEBHeCvOhRRnk_vDlqqnWhc16GJBt5hOuGHTxmAjcgSaQvUuTHpHZmtYOUJiRG3tjdXPiEwJAsRzzMH4l2aM__2EMTsHVlOQSCf040g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنتونی‌ جاشوآ بوکسور سرشناس‌ بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه چند شب پیش خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی وارد سالن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7-OreobhShCU2yYzxpcH61vC9aHmcOBLW-wtopML3NSaDd4jil6tKXkgegJhBTBuIxE8wf0T3EoRBPpdY-F6jS7k9mHW3C4o2v1x60BFeaa_1tumaWR_aJnsGTy7m0VuIB2yDSY2l5WYh0uiGzUWEoP5GYCrNPddd-PIUW27bzQ9gbQCF5cNBIN9fA2HLkfkJMRtq-tjcwa_2nvyMGwht6rGgx2xQtawMWI2EP7TN1JksQTptjclSHVs7o2_rUT94kUbcHirxhIJ3GWY-TcfsvnFOP1jL6OOVrF1-om1358cskaQadrTa-Ke01mqxg2mRR67ALxAeOSq6MEE73WzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26704">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/persiana_Soccer/26704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
این هم فایل برنامه کامل فصل جدید لیگ برتر؛ ذخیره کنید و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26703">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkdgBFyLV9zQPcvz2whf9IWTpv62dDYHkzCwsbH0RMhaoUNN3D20CV-_ZOIEDVnu28_891_rXl9bCP_CLEaMsmvGBP6zYmTjbTNvW-Qt0dOE1p68stC4hQwnnjSPFSYd-mj9AEWHYq0P_J5AIYNL39KkQA1huGnmgffkU-4Tg8eO3r7E5x03ugm6mED15EsUUHzK720f5NW39hUBE84yiykoDdXoFyf0RZn-2hW2dXktk-Gfv7sSsW4I9aOgCMgwqAJeMl4mNKO2OHLMpIIn5KZy5KuJ-ba8uFFFw8DLj40aCMQx5AKEXmD-N2R_qsf7NFPSf-Xh4OZ5xm5xLZbWCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دوئل‌های جذاب 4 تیم مدعی لیگ‌ برتر
🗓
هفته دوم:
سپاهان اصفهان
🆚
تراکتور تبریز
🗓
هفته‌سوم:
استقلال تهران
🆚
سپاهان اصفهان
🗓
هفته‌سوم:
تراکتور تبریز
🆚
پرسپولیس تهران
🗓
هفته پنجم:
استقلال
🆚
پرسپولیس؛ شهرآورد
🗓
هفته هشتم:
تراکتور تبریز
🆚
استقلال تهران
🗓
هفته‌پانزدهم:
پرسپولیس
🆚
سپاهان اصفهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26703" target="_blank">📅 17:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26698">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMvE8PN5To1CC3DBt6Fy2bRdxPcBnDu1QgmCwSfZSJfGTHRF1q3Ze6wNB2wNrSJGIw9xHn-Nb3_tYHUNpxne_5dT_3KNe3PHPlhAiW4gThGRXeijvgDLbKyo9c0qdx6zMK_0q21uKVh-IoZpznMbV0E37pa3bzCcQhzvjvx0JTcC3gsgUtxr-_liivDwXHx5CuxcFm6ihLsC9wEi7Dt8us1qyPD7C7o1IJ36HelZDXeeUYcmTm51Tsqx8qswLniGGfaS_6np4UiN3pSFX_o0YCWTW4okKNDGkyrb7F0EmO0EdQG-1fCx231S439VHjI6Lq1TQqJbwwZlpBwACiQOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kpf8e0qlKommAem8jzdC5CFQ-v8Ques_q2t_blHcNT9fEgT4ugAzJL7XWMaUj2C1mkfBeWO5iXfcV44WLX9VJMpH-L9CMYutqS3F56jVloEKmlZF2Iifd1GhFQXcfxGKZxVpNeT5prvH8IvWG8lOp-TO9FD_hnuAGDQ6wCBDkgPRU0-1QhOuQTWbuMfgRRQkFE-DAojNjkJRP5HSoKa3KlVgbxT6RPxD0qeO6qKvtdbkzFCQA8_JSNSOLJ40g0ldDAxzLREYobew6wJkkNM5lmNi-P6WPijrNKYR2qos0CSBDaOu1wEbfvKpwbDnkHYdp8toE7A86VZSpow7a6Yh0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26698" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26697">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l34Ggrn5Fsw8MMMaXPVxtmVG_3fhkh5r-P_KscOkGEDld3HIU6fucR1N9wVYyhm-n2t9B6T-Y9hfLuoNX_VzcXCi3RpbI7TJaWoz1CV5r0EZ6I1578xxpaMavmwJLHlcfBkx3qVcm326s_yvR6vCPPNqLkBIA3aNlVEzlJ4MIcEiKvDk7f0lB2Sw_PYmNHRGTmSV5JecxYIunaSC559GEHJKfeKBRzV_CMeq_Nr-AjybKRJojAlJjX66uFaPhQKSoEFu8FjCnkrM-QXPXBcoN2wM2xqNFfVE-kpE-XNTYDLT5E_UNtxj9sMAOBNcFxf6J34Dj6H8mEv2O1gb_Aq7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26697" target="_blank">📅 17:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26696">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPhY9oozWF95Z-2Ub0TAZEmvfFd2IkLhp9m-IShiZaUJ5eZEWKeQ_Ts1IqhqPCSJ3aE8BGUtGOLoeCvG8PjdMn_MhATULcVCdglde_mGhoZXeM7oiqvTKbRQzBkcotXoOqsp8qgJdKC3DKwwB182ROVLcYAhi1IUtzgIi9qFJ9dtSH1D6yv7x5mj5x_mevZp8v1nQ8hcGuGPLZcoi8hA3fNygLBWXwxSpsm0UCLIJSqHnBuM7nqSK3A4ipfCViS95sBOeirCqVmKQZ035zGdhHrh7Zvr4wORLNIB9PW3UmVM3qPPj8RiX1LQrsfHjJzFjnJtZXdoyj22C6Z5RkeB1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26696" target="_blank">📅 17:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26695">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crhqf8zEbAE7r90ii5UwIX9hnYms19l3HcO2EaVBh0Ba1v9K4ifYmY3_0zlfgY42vilw-E0smT77XHAd09LLjPSpFIMCF2m7vmEfHbhPGwHkwSecBq4ls-couNW-HxXqlDxWRkAKtn2lSFuqDTq0i4YBMrUN-QHRtndEvuRjeQ9ckrrfGOClSPfZ4bKVHfb8aszbW3zyru0zORE_2ncac3jXhWhLFSzlPv9M7uL0EC3pDb0N03-SIAsGMuNzGCXsPohh7zE0i9-EzvrxwcJhhkuy_F44M9hdFeNZ9twEFMOXd_UDvTYbJkqkZuhi7KusRlZ_9Wty6wmjQYcOHwu57w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26695" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26694">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31211ab420.mp4?token=aF1KGrUuDyrT_jQS32jf7dU0gjwUwtwLZAO_UP8yADs7o5DwkZLZvhRvvBaYxZWztTWLALD4UBBeKYq3OaG_V7yk73Log72tpZNyl24jZfmSUpF4ym4Tif4e5Cpl3d_BDmnurMSVnAoW1taVE0ILFnaQgBUxbncw7MFCE0pXzbRdRX9NDciIXkvxmkmFFExF4HZ_5FjNn941qSumklchFwRKM4mdwwN5_95Emiqv_tP5x1quKazameG_kyMTa83kNh4jh3O1oUwdgg9QDfWMlyNn4uUNNbhZ4lJZraxkkorgNoWP8_jOgiWgYMVbWctbna_iTg6amk51crQ51MAA8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31211ab420.mp4?token=aF1KGrUuDyrT_jQS32jf7dU0gjwUwtwLZAO_UP8yADs7o5DwkZLZvhRvvBaYxZWztTWLALD4UBBeKYq3OaG_V7yk73Log72tpZNyl24jZfmSUpF4ym4Tif4e5Cpl3d_BDmnurMSVnAoW1taVE0ILFnaQgBUxbncw7MFCE0pXzbRdRX9NDciIXkvxmkmFFExF4HZ_5FjNn941qSumklchFwRKM4mdwwN5_95Emiqv_tP5x1quKazameG_kyMTa83kNh4jh3O1oUwdgg9QDfWMlyNn4uUNNbhZ4lJZraxkkorgNoWP8_jOgiWgYMVbWctbna_iTg6amk51crQ51MAA8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26694" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26693">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRO1tZMMevDelP6mLZjEaSKEL6Lk-TuABMZTHRoW3AKRw0Uqndb2iiLWBVt9tHspLNQk4GjdIQXcMPDrnhoYSNv7juVcy7w4YZT6am_apEVRrXM-o-Xzwbe8bsQRWUXc3G19Ie4YAObulPjwvYTU98HC6FDnmEgFlgxiUUXK7DMbJiNeCHH9txKJZt3WFWGu0x_WajOBwuJ3kzrmHqDW-Tk249CmsZTyoWPnv54ZTsxv085LZmBAc9Zu66jxGuywqVYPFZeRroiVFhHEPat2sD04BB7XF5Xr--ULw3_DUnyFQBPIMTjpxt2ICC-Q4ulTIHw2BebR2Hhpxlak9vD4oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26693" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26691">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0SLO1ZqcM0WvvMYKYCDUu2O0TtXPBGKtJJOsUtMAqDh1LENBZEPXIBJ6N0y_oNf_ZeDHYiTjnrr8HUsd-Tr2Az85KBxE6GVrQgCamSo96TH8Yp8QQh-c7OQmbKI3vs9nVDcif_-W1bOA_pDV4k8FDvjO7-eCAQS5NB_8rhP-X-X1G-An97MgZXBp-K8sR0ljg-D_4h3c3dF-I14vHHLbgNMgTXkrIg1yYYeFTBp8so7brN0_iHQdh3aGqIhbbSMvwR6raBfJRQjVmnpgBt0AMdQ79Ws4p3c7iZsNJPAmvOP7PVgQpkDsYvp2OeWXPQqwdJhbjUDbyqnYtcu5v5z0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ محمد مهدی‌ محبی دقایقی قبل بالاخره قرار داد خود را به مدت سه فصل با‌ پرسپولیس امضا کرد. ممکن است باشگاه امشب یا فردا پوستر محبی رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26691" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26690">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNEpgVlkobMJY7HrTBIytouQh8oipVv7KWLAKQCJ1889e-YF6hYyUf--2DYWZuBkUaKtLjxOQbm_LS4oCLtRigtBAer7toUSfmgJY4dpNFytlRTbYhAGPJ2UEteipdxvDYZk_p0ubdEirqO38lQR-ggjbdj4kbDLBh_eLojUCZ1paFsmeQQdd1mJNVkFuALqsPd7CRlzwH4HuHqwUVUWHMGbcKs13mitPKqsABV8JIhRWKbStK0avDrIMYmmuEa0igu4nDvifOI8j95NdECaiTwt39GEP-0WCUfuZ27gruYu-rHGbjXKI_Dp3A28n6Bf4k-mY6XcCwhMn2DU_r46Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌عمو کسری‌طاهری ستاره تیم نساجی: مهدی تارتار به بانک‌شهر اعلام‌کرده با وجود علیپور، سرگیف و شهر آبادی نیازی به جذب طاهری ندارم. تارتار سر انتقال 150 میلیارد تومانی شهر آبادی به باشگاه پرسپولیس 35 میلیارد تومان به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26690" target="_blank">📅 16:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26689">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=pBwQ4DRluY-3-0p0PdVWhxdGwVmxBDG1fLtxKSqhW0yf0K99PrdnBd7iIg5RW-_3YwOIr9EEtWTGVfKDYaXQrWMV2pjwSFiQC-g1E_eQmgOB7dduqXMWZuZInxpouHtm4Btj0nnfbZRi4YuQtQ1y7GztIhlssJkCz1c5GewGEARtYV2DIEc1tbqWieoCsfjSPfJuDBz_fN3PINimmgp9cV3kY3zk3QWkvkn4U9ew73uEXa5jb6u2jFso6iKC21vNHvpPZJAiyXKXk_Yqr66Hz8rBZ9s69CWNPk_jOgPYhEGpxiy686EGXWX4jQ4XztCt_IJPtmsSGS9W8z_j3CmDTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=pBwQ4DRluY-3-0p0PdVWhxdGwVmxBDG1fLtxKSqhW0yf0K99PrdnBd7iIg5RW-_3YwOIr9EEtWTGVfKDYaXQrWMV2pjwSFiQC-g1E_eQmgOB7dduqXMWZuZInxpouHtm4Btj0nnfbZRi4YuQtQ1y7GztIhlssJkCz1c5GewGEARtYV2DIEc1tbqWieoCsfjSPfJuDBz_fN3PINimmgp9cV3kY3zk3QWkvkn4U9ew73uEXa5jb6u2jFso6iKC21vNHvpPZJAiyXKXk_Yqr66Hz8rBZ9s69CWNPk_jOgPYhEGpxiy686EGXWX4jQ4XztCt_IJPtmsSGS9W8z_j3CmDTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هر اثری هنری دیدنی یک کپی بی ارزش داره؛ در نقاط سخت زندگی فردی به دادت خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26689" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26688">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbFlmwaAAa30gvaxJZTQ4jMSVFXYcx4YrFHRXMSxVcJD-mDXJO1j3s0TOJBQGcfYYUi-tESPbu-K0REfrQZcH1mxQqA9g9W8099o3Qh6g1CEbC7hChEiFHH6-HgMp7zjTONrj6CwTVO_V8wtQzRxX7zzwsfVlH5PinyfA-eSBJzh84huQoTspwkqs20golfqSy3XJ6yDiwYdVYEKqrUynggtP2OEepo5tqPKlAtoy0JrpBgIknAL0LAbVy_hV8Q86B2hcIAz8wtU7QuPUsGZZZ5o_L_26ZmdstX_Im8NOjYMU17kveW5uIA3ahMvASSzySQw2RL8k4SVokq54DImEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
مارک‌کوکوریا مدافع‌تیم‌اسپانیا: اگه قهرمان جام‌ جهانی شویم و همسرم‌هم مشکلی نداشته باشه میخوام که عکس دلافوئنته رو روی قلبم تتو کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26688" target="_blank">📅 16:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26687">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd927FMvJXOuhR2MSTYHr-pI0MutrGwGiJYN8Bhc80mOTgrqSQVzOr4-UblCNcHn55_7CVQH_YgrX-shVh0EgciR8HVv2PNxC05kPKAhISqPhCKBfdr5QLdla2h4MZdQo8jCAnQdqYTsF9mdXcE5sD74lCrX7d4Kk3qwnwYdb8wEfK3auhPKB3DxlSJoWGs893SDNEhSheCryFz8Mtd1BioVwvb1uzvJLpBFL5ZP7ERRtL9T6_x5LYXPrIQsyRv7-ynIBfGXIjopfwCOUWNma2CdcG_Eim2hE5vaYyeOumvsi_fCi27YIZ-3p2_GHzLM-HPXVOAJVPTRKUFAjyNbiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26687" target="_blank">📅 15:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26686">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJxEtzzbhirnHHrYpw7bOf92ATUOFPW3hAfjpCmYWdFqKA4CGVEYgE9nM48tNlRMsM8_O-b17nsC7yYDLuzaGcg3Npms8oNX-VqIQALFyWpgBC-QmViyQv7hIb3qNmWXOPVRNYqxNBXd829DNSgXYnm75FqXQHRqbYqyKDQwI0E0dznSYTaWwYDQoI5-e7GZOw7NliF9WO6JVDAl0RY1Ch4EEu0T6O35SzkU4CTpKhW3naR6tzARATg8fYkHSWcL1HaiKQMrPtLEFWjQ0RMK_HWqRmRv8Ib2LZ12QxM4d9Sdi28EP7VhwQizr27WzGUHo6pzpsT1_Osw9Oh-J_5phg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛فیفا درروزهای‌اخیر رسما اعلام کرد که ازنظرحقوقی‌هیچ‌مشکلی‌برای پیوستن کسری طاهری از نساجی به تیم جدیدش نداره. هر باشگاهی پول رضایت نامه طاهری رو به نساجی پرداخت کنه باخیال راحت میتونه باهاش قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/persiana_Soccer/26686" target="_blank">📅 15:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26685">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDorOPgmCLL6mGmuelvzpcPyY4cz3mvERio8KqYMYx9J-pql9AZ7KG0Kd0dByaHUFqanM6Nx4QnCvtu16Byz1h3Qi50chIRHnxu5ex3WuRGRjrQOm3oUjo1s1cLgbL_Avs4J2ix8nbWw6djAJeJkyYvinsLn3lzzI52Kz8JSIUVWggp36dYT9q_AEX-0tiHMTyqQVUAPN0__w4dYA7m5oLx_u-_ZftJ4szfnvUuMPMP_nuTyhDIE4vwWoJXLCNh2bTroPEpTQHJq5m8Yf5oqkuJOfGdeJbfr8it4qm9z7sVq4dvFQsELpWXd2fz3XbzvBP3z1yMg9qgvJoPYhXvcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس:
برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/26685" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26684">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkFRNNOBOvQD40P23OFsdElAjlzBf5WNVWG7Wgt4Ga2bs5HmeU5ZYNCLw7nWpELcMoB8cOrjldcrpPKpzenzgLRZnIEZ1xFI8bqc608GHqnU5YIFfSAad67VQkYUYgcgnaIamE6lH0ZaKy8fwoNNnEGGc3vYBMBHvquYOmk95JYcTEuc3WQbcyi9GgabqlNgnoU_eQez_vijZuoXiHgihagfGMoGOgOregFd9H3kQxr_bZF6BEgE2TMtTecivA5LjQKOPP-xsxbbGPgLjB1e3m9lXp2k0r7WocpWOx6Cz212n9JPDKyGv-QluKWgyF6-GZk6LIim8vlUq6DxeFJUSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگاروگزارشگر معروف ایتالیایی: فدراسیون فوتبال ایتالیا به زودی روبرتو مانچینی رو بعنوان سر مربی جدید آتزوری در یورو 2028 انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/persiana_Soccer/26684" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26683">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X82eiGYH5kSHErxaamW7f9IYgEB6zMyuuPuX6kP4XDvGZCHsbNMhFrDovNBULcHjY2lX9T6NcUhUaWIO22mGKVArzzfpl9mreix8Klg24AvwEVIOfaOfKEHH5kXQAEjUTZC1Q1G2IO8E4Z9G7J2FkoLOnr0Ue_avcbwxJqGR4y_Z6fhLv0kPjTEsJjaQz_1z76CzQfczSc2GFYaokmvZbaVwRvncJb_rlCBnzSYelt3zIPXU4nEJyyaNJH9641kd8UDNjSHneRn8b-hrxdD1Gji0ItWHBkpnmjI9ZlrmkrzDoH9aI4Mzn1OEjDspfi7RyJf4pbnmq2d8BiNPuWTZww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/persiana_Soccer/26683" target="_blank">📅 14:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26682">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERtdEEGbGHNGA0d60N8NR5qk60Kf0tGxhNeb9P4fqleQMaMzPlFSVK-ikYTQNyybQvZErNdJe2xFUoTa5_NMl5Wnx58hAIV7ZEg_xGSbt3NM51Jac6Pc_x2QmPAaZ5sg-MOzqAuu125v6dsQkby3ZVGNeIM9SAwaBIsrrMxPnp1LMRk5YvDTA6WIlTATOlXB4w0UpBgY99W9qS10VRjGC5lnvIE7k4ZtKFOuRLlf0YoOayLPY-XfDdbqjlQSbSxSIRqSFfEli1VaNbXLygKPjShjpsXLW2g2io6dd3vYF_eaNuE1-OxTgmsDRBrPzVtJLyKgaJPLn7J4czGE6poTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ ایجنت رضا غندی پور به مدیریت پرسپولیس گفته درصورتیکه درجذب این مهاجم 20 ساله شباب الاهلی مصمم باشند با 1.2 میلیون دلار حاضر است رضایت نامه رو از اماراتی‌ها بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/persiana_Soccer/26682" target="_blank">📅 14:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26681">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH3MQM3Ss_VAxZg7D0EXHm1uHbsQSuC-X2A3yrVg-wfdO_X0m0f-K94z9DOEyA7jD3hPFTWxSeQxpkW8JoIUmvhklpChM4hhly80fAKQW8LuxbIHPWfCWpXZlAEAPFoY8SjQoGbAIUViDs4XEv9UUTXHPhe27jyY9-eWL4Xg6RIHiLtFkQ61BEUnJWMOvuoicfMr28-eYmpQS0ERjIUueuggzPQsX4OCcilhVSRPenVHR3uQzVw3VFF5WxQ10D5wU-E_lIgXeB3zBUokm_KYrg_tIS8qOE3KVSV1mMl1Q0AsjSVrd5qONcuUhaS3JEtz019Rq6MoFSL4mti9_KtOCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/persiana_Soccer/26681" target="_blank">📅 14:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26680">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJyccrHMoETdk389jDeX2OCyNiPYw7uaTUNvV6wKghUT3YHp7EfhxPPdqtagDYVWmjTt8Hdehi8-ZvH8G1d3avwmdy3PUnNpvg9PKWS5D9dw6prOm5FvBLZvbJxOsh3RJp06WjC4ycOB1MPVtofU4vdQPcQ-UErWPq5Lt66HHrbBsnBZJEqNuYA75hlP2H89HRE82bD353D4tjn0j6oWhVIXaehSqchFL9bEckkcg_LKS53eRluA_GQ-DrRl_HSVNU77VYdHMScn3LLbjGCEWVn8l_WCDt1ZgZLHiw4MOMwhCIYR8t0z_pcDuxCxI3uEkXPoqYS5Tf4U2_TJMuv0vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوریا شهر آبادی، ابوالفضل جلالی و مهدی زارع سه‌خرید جدید پرسپولیس که سابق بازی در تیم‌های امید و بزرگسالان استقلال رو در کارنامه‌ داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/persiana_Soccer/26680" target="_blank">📅 13:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26679">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTROHqfXNLAY4i-XNmemaLPKroTehfuTZZ-UPP0GuqmMRNCE6e2YFnbC1BDa1O8NdNO2ZhEoreCX7m1cvcAoh3jdf9wHNoJwtBi8WXzSZkjGf2qANBUbWcg7mPXoKT89arFpLpUHj44D6skpHCQGmEMU0QuXXidx1XJZSNC2IxqCR2SwUhU-4ipiacoGdn6WdVkiFABoSjr8vo5vcx_4tUJJyTuPBd-AUrrHnAqQ1rEcUSJtydgl4xjTeJwzuYlxxZJspnNZXBHcuzJnSqISkhKDFe4lbRqqBOo_vGJZy8wdH5wtv_PaVhpDSWCAnzJgCQ15R3yrUEvOz71URRVldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/26679" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26678">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaSCe2-vPZMGpUyQxcm3XdqLxrkP-JJDQAAMue03Z3RTJ7T_i03CY9S5AkJ1Mt51eekdoHIZPz3CiKZxr79qKdNe7pLwraSrRd3LFgjYGi53emlXlcSA3e6bfPo7wotrSj6eM9qMpN_0Nxzf1SzOkqBRBGCefZKYSX2PCiXhBU9Bv3QCd1fQNLxIMxzjd5iu2nlEFbaVaKB8ss2AjZAvTkAj_UOgGR0H4cN1oNq3X4X_2Gl8cVyi5j30akhBOzJPs35eZAFKdqfT1_hXL29zAWmc8ShltYcei1Afx9if4m192M-iEEX6zgIPrdKFossXQF3fRyBmxyAdo1mehSLz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26678" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26677">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJjSs7jIR6wnOgYPlncOWRY1VuzKmpRMVM_2VLAX-jdudyyu1LQQ60jmHCy5-B1XGX7UQf7hD_LfueSmEeDAuSKvYAkcotmCvBivZvPzvUy7PXeaouepXzxt_8YTuG9im28Mw4dWvPOPVx0OcZtoIeCbRuRfCa3BYHYtiXgdVS0Ugxqg-7MyxAQD_M8qGTpMByYLOgTbkYwBW6EQTIIXLZ0zGI_HZs3-w2aXL7GEZNjJcFrNsFjZhlyyzRPJxEDCVL7pKsmAvE78JRDgkHfHpvADH_tk2kJj3QvMDK8KnNMAMMDZDGFBY9nSDpdO_dLCwH6SjR7abTztWpo0ru_iCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اینستا یه آپدیت جدید داده؛ میتونین تو قسمت «یادبود» اینستا یک نفرو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه و توی بیوی پیجتون هم میزنه صفحه یادبود و یا کلا اکانتتون حذف بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26677" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26676">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkdMlkOKd3Go1_lqCqRuO9yGbdaiD-UbJB04amORyq5VkH-m7C2XKtdvZpzkfP72rXp4WziGCwvwDc7kiikUXrJuVr5JtWQ5QsxYrxIMNi5VuXmbS-S96TthelwNaXTtJ2O0GJ5cgXDtzrUee2gFXIDZaPuAGo-gVl4uQwfwmOOuMQa2tU4Pm__7ysxzn7WEL2_yzGSg_dleZwKdq24LSYjDRqmMYcmoribVYrBfdA5BTBwuj3jDiLErCacxefYdACOfJtog1mxNIFFLxsQqUyqF_skCgnngF5PxCOkX4Lptur-2qEHLMy4TUh_bWAmebea-pblAJokLVZzGITIElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌بورسیادورتموند درطول‌سالای‌اخیر عثمان دمبله، جود بلینگهام، جیدون سانچو و ارلینگ هالند با ارقام پایین خریده و با رقم‌‌های نجومی به بارسا، رئال مادرید، منچستریونایتد و منچستر سیتی فروخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26676" target="_blank">📅 13:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26675">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7vjigEwV0rXbv5CjDYz0upw_2wZY8caHK1JX-_W98dH2Mf5H3qAGoxc4qgOHj_UsUiryrEwNnFWvYim5KXyvQjNrFU2H_xE3lGym907ojBaXQELGbJy4QuXe_TFYhv3byK13KwWvLPeqp6X686D688gIWd8FzfyowSb1IKy9xfVlWGM-3HZXj5e4U32CcLUkqfcm72FS34_AL6byY2DBmbbg7RWv86nWBZ_U54kph6uZbbElSN_HL59n1AkN4GSAx10PwyFl1V5udy7Poe44kjDm8QmwXMlw7NHYGyCeNSB7KMx1yu2dRvNEz4QluGk2z0RZFtUdrfRBGPZMY4uXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو، توافق زیدان بافرانسه‌نهایی شد و این سرمربی جانشین دشان روی نیمکت فرانسه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26675" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26674">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxEEpo2Szr0FANV4PYwDSgqKWbXHb7Qjqq2nZXANZe1aIxkulSHhwwEPh1qeJhY-qtxRRVRkjovxEwi-jiYre5uOz3zZlLxqQc68cIqM7vnibLgT-xRyODWgpcLjFixWdO6ugqunSn0HNvEeh82bdonA4qPpBsIk-N3F00lH_AtRZFqAnKgzz2nKyQCc9QQNLOu9uYE5eXifEXqS3oRiQWU76G7QSdUt7verGbpPuaV03Sqb6kgxGdaq1ocyiDojsuk5RScvTL_cZjdBc--kIHvjacVS6mq5Lz4awI0qF9R9YbQ6eehF7ND4O1GmymPFjhE0VX-hZO1mxEADH3JjTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عجیـب‌ترین‌تولد ۵/۵/۵؛ یک‌اتفاق باورنکردنی!
‼️
صبح دیروز یک نوزاد دختر در تاریخی خاص، ۵/۵/۵، چشم‌به‌جهان‌گشود؛شگفتی‌ماجرا فقط تاریخ‌ تولدش‌نبود! مادرنوزادمتولد ۱۳۸۸ و مادر بزرگش که برای مراقبت‌از دختر و نوه‌اش در بیمارستان حضور داشت، متولد ۱۳۷۰ و فقط و فقط…</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/26674" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26673">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZJXGfyJNqfujrHqS8Pzv_4K1G0QKZK4RSXXhPz7NpRLP4eq-5AAmicCChLH4emzQRx7npwW_07BaykwxJcM6w5-3EhGGhF6S8GbXf9T2yK8QlF-im_z_wLliK94trtux20ACObnpSUevL5r2TSwXSh4RYC-Lh744ZaQNs04rTQwAiZLAIGM4amvNQfdcldTzQLlQdbVKeX0MsOYu6Kno3M177leU_XOTCBV3eHGSFv7ait0mfkB5hR_uyU3iir3k44FnCAZ711IbRdJyk6jCj0BVjeuAI3sXJ6e5aTOAaB2Cvvi5OEhKf1wPo5MM_T1J2G2iD2KasZFjv9N9Y57XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
«گونزالوتورس»پارتنرسابق«اینس گارسیا» یه استوری گذاشته و خطاب به لامین یامال گفته: او عاشقت نیست؛ فقط میخواهد از تو باردار شود و با گرفتن نفقه یا حمایت مالیِ فرزند، تو را گیر بیندازد. امیدوارم قبل از اینکه دیر شود، خودت متوجه این موضوع بشوی. گارسیا فقط بخاطر…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26673" target="_blank">📅 11:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26672">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zkysy3_wEFyn9jZjJPt9-5jTtk-Yrv4bT6_XBlGWF-84UQu19XewqoHKUqv-VU4hXMQ8azyJH61Ai7TC7LxQli9-fo3zRBu8C0jleEL1Jwxu2S-QOmS30Hp_GYB2ZddVnkzq1CR8CUc78OYsppZ7UjnLXhql4Ocy8exbBHyRJs1XuY6NnQx5Wtf43TQvw3fd-Rgkms6XQi4QhcoEHH3WcCC2FZ8pTacnPJnKLUvuO7YbImMpyxQuXxB10KryDeeXfnyQIfbbOQXzXjfm_n6eylx8W2Lu9W_NiUsm9QN4AllOKhbnbMn2BFaC-nSIfKL3n92WMGOeAFO9FAVM1m1C9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26672" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26671">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=JkCoXNjgz3l5vDtWluCG-ekIJ-GPa5KbgCdlGGwVIpjqXkKcMoj95VfumHq_3ZIeDQxg-cnnJo4cXF07yIgn2PnwtnldKN5vS_f6swk6WbZeffpuLwuUk49t7S1p_ht9guV3HGZFnBUjFTkHbFVdkXAjNs0DMHThK7soPqeZlXFoIcmp1QvIiOUf7bUd88NcFduV_nhUV3tcJfVk0Keh-2Qz1r0pBgEADH8fyKhQjZAy2Gie4JOMu1x8adUZ1gGSkEzSaA_DH73VdEtp84ILLthrRd_QFI4ZfvyIsAXCmAyEbFLYOy4IgPLl1oZmEekwYuwA3T0_dzniNy6v7xGuqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=JkCoXNjgz3l5vDtWluCG-ekIJ-GPa5KbgCdlGGwVIpjqXkKcMoj95VfumHq_3ZIeDQxg-cnnJo4cXF07yIgn2PnwtnldKN5vS_f6swk6WbZeffpuLwuUk49t7S1p_ht9guV3HGZFnBUjFTkHbFVdkXAjNs0DMHThK7soPqeZlXFoIcmp1QvIiOUf7bUd88NcFduV_nhUV3tcJfVk0Keh-2Qz1r0pBgEADH8fyKhQjZAy2Gie4JOMu1x8adUZ1gGSkEzSaA_DH73VdEtp84ILLthrRd_QFI4ZfvyIsAXCmAyEbFLYOy4IgPLl1oZmEekwYuwA3T0_dzniNy6v7xGuqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇦🇷
پائولو دیبالا ستاره آرژانتینی آاس رم قرارداد خود را به مدت دو فصل با این باشگاه تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26671" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26669">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak77PxOp9mwBUTL6bauv4jOk4bpzA1W8_7zb5NNzUrfu44_9xa6x66Ju1d8OBhp2TVVfbpusY1eMAFcStsq0lHXp2qFSf4vd_5SAhWQGK8J1mm6nd-gxmkgFS_0_fQf6XyMttycle5Jnc9PAJHiyHFuf3r-E53hYQlitvBLSZ6BvK-fze02-mcOcWj-t21f0W5PLD34uU3BzH4sJJtF9FVBla1SXy7FmNHb5n59ttEYlutMoBmnOXhuUyV3bV34a_Bb0uthuMwyAlaRE7dWRgKDtSRnxjEVztuH8NHbVkjEUE2nkx7D7HYxSjWG8wA49Wz2zADoJmssJ6J9-jb3FNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وندا اکس مائورو ایکاردی: علت‌جدایی ما این بود که ایکاردی با شغل من مشکل داشت و شکاک بود که باعث میشد هرشب که برمیگشتم باهم دعوا کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26669" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
