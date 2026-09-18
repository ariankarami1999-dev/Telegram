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
<img src="https://cdn5.telesco.pe/file/AtBtclqpxnk9Jj6d9e8QzZgQw-PQJlCREz1-OwRiiOvCDHa-2LUGGqXei-vdfZex3Vh2cS0-OMDW-zmZUSU50UwFKw7QH4Z3gbmU_Vcd4HlIbRaGgUWUd-LBCBaEb5vws9F0Xb1kaQ5HRM5eTukJI-hXaJLlrsjij6Pting6lTd36gPLQxqjZqVPJgdDSif7LGZFzUKm_-pXZxU9jiVqE4KygDK1Wtz6ObfPk6W5oZOf1HR-eCF-o8Z__gT0aow8t8S1BgSYS40BPh-oc1trTDip2_5-nypjiWjUnPHwlgMEEXytjGkxA6Zh-gOCdzAoKxrZrF0T1Q1vX-kkePxw_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 409K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 03:16:00</div>
<hr>

<div class="tg-post" id="msg-106840">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/106840" target="_blank">📅 00:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106839">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 937 · <a href="https://t.me/Futball180TV/106839" target="_blank">📅 00:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106838">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/106838" target="_blank">📅 00:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106837">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRbEAC5kXoCvqpWB1qCoes0J2rN4e_HuRoDuajVwvbkUDG9AZzMdWyXuj9ond0bUnklITa_9Fyne-Ia61voi5mLDJTpo1obLwfvmXTwTfE9zvLPJRm-_Ruk0OL4bh_-eqiDJiDO1qoLH-aeHbWL5juWmlXybxuiFKnbxZ5ccaNInes5KuqyRPYe6JS4fAvS-uUhl8m2bnnGF2lb-Pj-P4lYSdtTgnfGLkc-Eoyi8sWlFS_7EOuRcYchgwUH-hjgYFRi1qUYOiusQA2vWAqu3lGx5HSnZksdJF5pYgfvI0yRFm65JkSO0Bp9_8_jn1CEddEImjgsp11YSj-PiELW7NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لامین یامال درباره علاقه‌اش به نیمار:
🔻
همیشه سعی کردم بازیکنی باشم که با خوشحالی بازی می‌کند، و نیمار تجسم واقعی شادی در یک فوتبالیست بود.
🔻
نیمار از آن بازیکن‌هایی بود که فقط با دیدن بازی‌اش لذت می‌بردی. نوع بازی‌اش باعث می‌شد تماشایش سرگرم‌کننده باشد.
🔻
تقریباً تمام دوران کودکی‌ام، صبح که بیدار می‌شدم یک کلیپ از دریبل‌های نیمار می‌دیدم، بعد یک کلیپ از گل‌هایش... او واقعاً بازیکن خاصی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/Futball180TV/106837" target="_blank">📅 00:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106836">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofRZ52L_Vq8RJe2opxgdFiUmIhkTQRArZr641rPx58miCQzv8sEoNc5hENwYdI8ITf1H3Zll3FTKxz-dA1J6uEUAPNsNUej7cwaAxrwB7Ce2ZpDILrhfOHVfck6gB_dUOKrPYNYcwtSt0SvGADDpaN6_JiL-QXINA6xlFGd9fySaFgLkejonjkW7w19EyyTXrh_1vFYhwbW2un_n4x-6zWiwtaXLRO8P1RuGirBeCKALmEDde-nxoBqboJftlIySbyBZJ-xEPNNaclYyBiVnHc6Rl5e_1Wt-sz9zMpQ7G_Ty7CTr1SiO1rvDibxl3-ez_d4ljhdNfOrUba9jsEYzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
يحیی‌گل‌محمدی و تیمش دهوک در هفته هشتم لیگ‌عراق مقابل حریفشان به تساوی رسیدند. این ششمین تساوی یحیی و تیمش در لیگ‌عراق بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/Futball180TV/106836" target="_blank">📅 00:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106835">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gl9jAfSQUaWJ_lOthIyZat1gnTqg0W-5ajlbcmHtD-fopakMPrUWaQAo6i16o2BYjs9dlIVEPCTKdAv8o7BKCNab7D15QRWeo8eGNGc2AkG5ANIpNHwzCxXKojzC_F41sebKiPQhSt4zZz1r_c7EYofQ03UOO34D1LWOsYltWWIdjpFNZ2whbLs38EJypP7X0H9cKrDcULdYqP2wDMbBmvKpdk9OrcODzWXdf2FtnUj9SuJHfKb1iBDa7ewY_vbW6x0MDbR2Jr54MnA7Mllw8K5RVJf8pt5xMiw2PRXJKSqqEhtA9HlKLU6nkq8hem7VPWSZMi19rehOYzjIf08W7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
‼️
لامین‌یامال: تا پارسال پاس گل و دریبل زدن را بیشتر دوست داشتم ، اما الان گل زدن از نظرم بهتره ، گل میزنی و تمام، کارت را انجام دادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/Futball180TV/106835" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106834">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1135acc96f.mp4?token=hficH2fe1yynsgjLOhfIiFVT83g9ObvFTy7Cy5lrt0w-bYcdB_q9oyzpTGcCzvn7EERZ3fo8PhDpIm63WtoCj8ShJXPa7RMPNdSEaYtR2X6ksaTzwEBdwjWmMuBhMmqDlhHrpG8SdIorXEZajCa64qrKM1v_2K3A9ikQLHnpPFCVY8RuKg5RWH3uDcd5ujLKuG-K-I-3RF_gJydwxB1IOVx9GDm8-Bg9br0NpuWYGXU_J8khwHQGcV5gPtp0R33_lmW0LKambHvFls_rqyFe3w5dfyBeDQddO6NkrZZ5DjdCTHviG-MpkviR2lVHe9MMbaGvpvyZiksFJqM7KrVs3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1135acc96f.mp4?token=hficH2fe1yynsgjLOhfIiFVT83g9ObvFTy7Cy5lrt0w-bYcdB_q9oyzpTGcCzvn7EERZ3fo8PhDpIm63WtoCj8ShJXPa7RMPNdSEaYtR2X6ksaTzwEBdwjWmMuBhMmqDlhHrpG8SdIorXEZajCa64qrKM1v_2K3A9ikQLHnpPFCVY8RuKg5RWH3uDcd5ujLKuG-K-I-3RF_gJydwxB1IOVx9GDm8-Bg9br0NpuWYGXU_J8khwHQGcV5gPtp0R33_lmW0LKambHvFls_rqyFe3w5dfyBeDQddO6NkrZZ5DjdCTHviG-MpkviR2lVHe9MMbaGvpvyZiksFJqM7KrVs3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
محمد تقوی، در برنامه هت‌تریک درباره پیروزی استقلال در برابر السد در لیگ نخبگان آسیا گفت: «استقلال نمی‌تواند در لیگ برتر مثل لیگ نخبگان بازی کند، چون نوع بازی تیم‌های ایرانی متفاوت است. دفاع منسجم استقلال اجازه نمی‌داد بازیکنان السد، به راحتی بازی کنند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/Futball180TV/106834" target="_blank">📅 00:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106833">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/914fe9902d.mp4?token=k9grUfUNanTxQ60QWbN4xQxkTORrftG57mje8nBjWhGYY1R1oz1G1Lh4ryfuETl-L4sVHuLlKNs3NxH1aiPcXVZsp_bCDPpf0QY0bn8BTDmGDLh2Ug9nca1MYlxH5rfomF0_S7zvP4fac_FhqFE6_Lmv79pc1OBZwGQUiG62D-09RQ9XXkSyHl-IOLKzCMRYghnEnuUPZEO8JT_prEk9QnEqfGZzNHHgarFs5C63wJVwhOI_xZ5tcyHqNDVrzlTOQ81bTsjqKRirxV_Us40grO5fDJ6OLW-Mfhr4o3HnFOa0E5mYpXeaRaQTQE7uWDbQonvVA48EyIiha4uXPqgxog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/914fe9902d.mp4?token=k9grUfUNanTxQ60QWbN4xQxkTORrftG57mje8nBjWhGYY1R1oz1G1Lh4ryfuETl-L4sVHuLlKNs3NxH1aiPcXVZsp_bCDPpf0QY0bn8BTDmGDLh2Ug9nca1MYlxH5rfomF0_S7zvP4fac_FhqFE6_Lmv79pc1OBZwGQUiG62D-09RQ9XXkSyHl-IOLKzCMRYghnEnuUPZEO8JT_prEk9QnEqfGZzNHHgarFs5C63wJVwhOI_xZ5tcyHqNDVrzlTOQ81bTsjqKRirxV_Us40grO5fDJ6OLW-Mfhr4o3HnFOa0E5mYpXeaRaQTQE7uWDbQonvVA48EyIiha4uXPqgxog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
⚽️
گل‌های دیدار بایرن مونیخ - بوینیون برلین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/Futball180TV/106833" target="_blank">📅 00:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106832">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e28dd692.mp4?token=jk-c50J4DRyQ7M6sNDk6R7fpknoDP-h4ROGJedOSyqNl75EidTIevDAIhXiXtlfw1kGC7WIGLErkRTueR0YEoFs_9hCXf137U0YZBL_TbGNYc-jNsnGVBnGXvfy6xXqBs7j6hJzTpDezTCW8WHmvv0Ye9v6MhgPCz5gtxGnP2o2dF7H-Yi6qzat3LXekpJaVk25h9Z3JvgPjIggFmDCWEZgerv29qsKsSZweSj1D60OZALlJsmMGcYOKGBW_9MS5WceqxFZ07tsjzltmhFlHzIv-SEPTM5cY4bRGT6eKMg6-LjWDM8ZzAx6V0rgcPpD54XQfQr1un-22FNod_YbECg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e28dd692.mp4?token=jk-c50J4DRyQ7M6sNDk6R7fpknoDP-h4ROGJedOSyqNl75EidTIevDAIhXiXtlfw1kGC7WIGLErkRTueR0YEoFs_9hCXf137U0YZBL_TbGNYc-jNsnGVBnGXvfy6xXqBs7j6hJzTpDezTCW8WHmvv0Ye9v6MhgPCz5gtxGnP2o2dF7H-Yi6qzat3LXekpJaVk25h9Z3JvgPjIggFmDCWEZgerv29qsKsSZweSj1D60OZALlJsmMGcYOKGBW_9MS5WceqxFZ07tsjzltmhFlHzIv-SEPTM5cY4bRGT6eKMg6-LjWDM8ZzAx6V0rgcPpD54XQfQr1un-22FNod_YbECg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇩🇪
سوپرگل دیدنی اولیسه مقابل یونیون برلین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/106832" target="_blank">📅 22:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106831">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz0U6vJTtl_PxTpZRlGLnDCxwq9kXkOKFDbEaZd_2MDM3rfU4HYHn4tQUGPRZiXmPzune2l_82aK3amz4uKXoYZ-btqWkOO_DGZ7EVQW4KaL19R2KPnghzOZNaFazgcTHed1QGzzZasinpaARgIVpKsh1SMbPJbjAB120rp8CWCDsrg4fC38Ux_ym7h5QDmwCwzEuD-j4lh5MgzTdy_YyPSmJxfWmZgPuNMv8-WYVjc_jToI3RGE8YaJUwNKUW_SqlSI1xY_cGtPMNrafMdcF2hdqgvEKlDbQJlnWfIZXt9n_JiPXk_qbpe0CcgbdCut-u8nxmeDpLoYtVPIEG3L7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
🇪🇸
پس از دو بازی غیبت بدلیل مصدومیت، آلوارز به دیدار یکشنبه مقابل رئال‌مادرید رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/106831" target="_blank">📅 22:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106830">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfXfqBC2VOB4ly3KOyK1tcqboRZUKk_KvUmrf71dpMXVZKNUH3_wVMHGDji_k69_uEtImvKIs77jNCBmR60Pthpb-QSZaK4bk4ZfsDavFJVYCdtdVAmAtUItEfiuYT4MU74gsw4at-eQiynuW732eGPoZnh5SHNZcIxvNKTHddKF8Ih6Pp_34Mk6unUun4HmsfRJz4tVqF1SFdlMQDXLAehQ287VrGm7Ad-gULpYTA3hekBjaWDA6zakkUcCMgThTWrAfMLYIA3NxdTd2BxCN8Gibiegl1zS8nE28M4qnBapZIAKsb-4BuBvTwX5igP_aa36HHPI1ON8FmsUDSq3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
داکنز نازون پس از عدم موفقیت در بازگشت به استقلال، راهی النصر لیبی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106830" target="_blank">📅 22:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106829">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3aa9abbc6.mp4?token=f5Z499pxEHCzIb-VL9PqEW72MFlbCtauo71Gmoe481J7J_6-4C66JxbmDLa27D7QXREtWTzATJw92IbXqjk9iuJDKNTf0yn1A9n9e-YA0YxIT9rVYXc-d5bgQjKpPQodH4asM5AMpz9WfPdwK7lR5E36ZGYjL5ECtPScLICJSN0VuaAPtWtnQ7vlNAsHTru5Z2zYocGWE809dC_9RQng_-1MExxIXhNwLqvKk66r0mnZ2sYUaNbw06EMBh0LGESjgwxiGgCfz0WXkSEacm7rA3-g0_5pGieMcKmOSgCasyW-ZOzj02HY1P9L-GCEuo4U8_YZbG94N_pWlU8d1T85Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3aa9abbc6.mp4?token=f5Z499pxEHCzIb-VL9PqEW72MFlbCtauo71Gmoe481J7J_6-4C66JxbmDLa27D7QXREtWTzATJw92IbXqjk9iuJDKNTf0yn1A9n9e-YA0YxIT9rVYXc-d5bgQjKpPQodH4asM5AMpz9WfPdwK7lR5E36ZGYjL5ECtPScLICJSN0VuaAPtWtnQ7vlNAsHTru5Z2zYocGWE809dC_9RQng_-1MExxIXhNwLqvKk66r0mnZ2sYUaNbw06EMBh0LGESjgwxiGgCfz0WXkSEacm7rA3-g0_5pGieMcKmOSgCasyW-ZOzj02HY1P9L-GCEuo4U8_YZbG94N_pWlU8d1T85Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صف‌فروش آیفون ۱۸ در اولین روز فروش رسمی‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/106829" target="_blank">📅 22:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106827">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdZBu29iEzGAe1jVv0VT7c14cOSSvtlZpFFQQw7JDYoFryNovBTyE50NyxLxVQUW6Bcu8rFg99lC-jcHRDhnemBjgqEHlCcgsn5wWr-ZBmI8CEfplZ6FQse6MLQPNFwPKTI0QwLKQ7UOUMW-DhX67M21AnX4kzLY2YZMqctni23nSQiYEXwwqElu5tZYlwYJ1vpOsKgeaimwY2WosNliIrA71Q4A9QtGjy5uFmf3xcM2jgXEeGVlNlaEN2PdMBNgduXTdOtxjeL5boR503qfDNX2Aej6V23O9t80lJ1LPkf43F2W2Dakn6w5OobUpLAvQP0F2qWB3OKfQClGSl8ufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etq-oAnmSrRsazwCpqD6EjWyCGg3tIcWgXyZYkeNnYguAeNE0AJyrj4Zg4cUEEx4QVPkmOwvlSeXFzK3LvuF6I2FMjoz1DJjN4zNVpPlbOxMgNKIzPZQ9dhjO649GDUco4xxyXttISWteHmGMFUCXRaq_3nygtcqcdPNEFXBNyGDfIIkwwzkBCf_1-bba-G3zgD-hFKQuVKgrIbdXLakW-qx0P-khIMlXNTy6ZqgS6_JIh0XpYc_gj-7cl3ZJpVLpjcx8dDhZK0XdkCubMBONa7oXFp0Ahc1e2HsJd2FBZ6qvPjna0ewiq0njPAmDqnx7QsrDjo51c1otsaG2mWasw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🗓
سه سال پیش در چنین روزی
رونالدو برای اولین و آخرین بار اومد ایران و دوتا بازی بعدی النصر تو ایران رو پیچوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106827" target="_blank">📅 21:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106826">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNpL2an3seBKGgsa8SHASLrvYQcWxtMdqIRrq65DeoVLBsjrnrR05B4lAkkwjFlJyYk-9TuAvhXN2qbit8L8vmR3UUGgdllC3Y3szrVePTd4E8zarmAogGbCx1HrhMKlLrmAFUtCLqrDWDN9fDfSPFOPF91aE6XHT1_8kwIVugOcGc4fxuWqvlpntfPJg4F9ePK3im6fDQWwOrDkGunsL-F9PxJabPMyaTP1wfVsr9UcwQ_EdoTV4BuzQowofhIbXmabjme_zKvM7m2ddaX5zMcpjtNsB93ms72Emn5tWefpjbzdVy8nXJDNxvYryUzvozhIIJfrWQtDGevgH23EDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
ترکیب بایرن‌ مونیخ مقابل یونیون برلین | هفته 4 بوندسلیگا 2026/27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106826" target="_blank">📅 21:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106825">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9ikpv3GROMz4yfNRH5_MM65NSqIAtwJk4HP2bEE4hgX8Ti0zki8RQrFBAddSyQJntQYJ-E3GcPnuR2Nxnb3hSNB0bJ4zgQDPuNLNQmogGgZwcdugTUeXjOy2bjuATnB1Kio20sXN0HTDKUBm1Ele0L3m1JfIQGlEqs6nKFtELEsSqjDLQJOJOck1PL1O1eVi2JPCsAbhak_75ZJ_2tOwYnQ1m9fQ3i2HgqWXIeObAdbXRBVXGSeUt0Lr2VMLaFT5qozOehtbUPfx5JIwI5blbWEecZBQ6UZ5fgROwhUBvjMknmxC760yAV1cxwkph5V2FRMEWh810sTx543vINY7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇹
لیست تیم‌ملی ایتالیا برای فیفادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106825" target="_blank">📅 20:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106824">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa894a6b5.mp4?token=E6u1l4oRfsomWIKClWkLw2SBDRGoC2W-u0MXLkVFdxTvzbnNdAH3WLVmWReF9ZdoOQYkaQxKT-TBXIswn-SWC8gHYRuHWd0Rzd7enJWgQSJMmK__63N_fVyIz0cVLbXXbpXhms0SL6wwtdxTbYnI3iZW5TK8TipOzj7iDO-hctWiXtPyBqtouhWOfgvKCJFvMuim4zgOX-IvuDoCd9e3L944FWqpBXPWNDmZ9Uryh7pl5xc6qIaeR56zYWMOFXFfzIZ-2Pu7Hsg6V_aeqyU0QGSwZ0nud-0gP_tOO-NzkeehecLlZWxEUCqB4csUcJdRiBY_Lao3V2fCudYp65S67Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa894a6b5.mp4?token=E6u1l4oRfsomWIKClWkLw2SBDRGoC2W-u0MXLkVFdxTvzbnNdAH3WLVmWReF9ZdoOQYkaQxKT-TBXIswn-SWC8gHYRuHWd0Rzd7enJWgQSJMmK__63N_fVyIz0cVLbXXbpXhms0SL6wwtdxTbYnI3iZW5TK8TipOzj7iDO-hctWiXtPyBqtouhWOfgvKCJFvMuim4zgOX-IvuDoCd9e3L944FWqpBXPWNDmZ9Uryh7pl5xc6qIaeR56zYWMOFXFfzIZ-2Pu7Hsg6V_aeqyU0QGSwZ0nud-0gP_tOO-NzkeehecLlZWxEUCqB4csUcJdRiBY_Lao3V2fCudYp65S67Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎬
👍
پدرهای عزیز به این‌دیدگاه عقاید جالب علی فروتن حتما گوش بدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106824" target="_blank">📅 20:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106823">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed690df00.mp4?token=oPd6kRKwUQLPDYrfgX-ETSVffpComYCIzgZaQxYarWMo69f7ACeS2z9x1IqhG23cqpY7wW6dJFZ_7-G8hi-eVnwR3-kdyL5D5XP3L_ZpwN9Fg95tIpplXLvslvrrKVoOIWo-ezw7Ze7uRmfpZqvE7dneqwsNjcUjkJ7t7bxhF_Zuwv_fThelEoUandHsGPCh-eL_4uecJUj2QT0FkqAbiipqU49LG4VGYxHOmF3DhQXekdJ9sdR1_G-05DsaohP5iuN9afWAzDPvAizyY8ekynBNQsP_hAZSXoNv6FNeNiAbDj0JgU90ZAhMiyNNZJ_47PNiqCJefQo7EutIvO1gTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed690df00.mp4?token=oPd6kRKwUQLPDYrfgX-ETSVffpComYCIzgZaQxYarWMo69f7ACeS2z9x1IqhG23cqpY7wW6dJFZ_7-G8hi-eVnwR3-kdyL5D5XP3L_ZpwN9Fg95tIpplXLvslvrrKVoOIWo-ezw7Ze7uRmfpZqvE7dneqwsNjcUjkJ7t7bxhF_Zuwv_fThelEoUandHsGPCh-eL_4uecJUj2QT0FkqAbiipqU49LG4VGYxHOmF3DhQXekdJ9sdR1_G-05DsaohP5iuN9afWAzDPvAizyY8ekynBNQsP_hAZSXoNv6FNeNiAbDj0JgU90ZAhMiyNNZJ_47PNiqCJefQo7EutIvO1gTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
مسابقه دوی نیمه ماراتن بانوان که امروز در بوستان ولایت تهران برگزار شد که حجاب شرکت کنندگان بدون محدودیت خاصی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106823" target="_blank">📅 19:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106822">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC320vUAABf0IEFZa6gvCnXZuZwBvima50IbNvTjyrRRtGYve8QBMUHiYPnn-xGN5D7TuxUqpWVTWNls1HcgWMK3ou3zfxnJ0BPcfMIy-W1ahIADbYji6PWh0pupowyr6H5ZjmzUvy9agAqAH8C_1oIwsHS0psDaBM645HHxU9928Uvz1SiSJ8yCRW1DVY4cU5G_tVSRXIU2_gFo9FAUEZPAgTqqdnrBvDn51o_MK1urof-6h8jpRAwVUfUU_SGgehe_bxlRPmINxwWNFK39Nv871lW49XrQQJclsBHyqDZpIjDtjXxv3m3VUigaRBLlWMAvIqV0QSSS8PwxKryHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇫🇷
لیست تیم‌ملی فرانسه برای فیفادی در اولین حضور زیدان روی نیمکت سرمربیگری خروس‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106822" target="_blank">📅 19:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106821">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69347998c.mp4?token=imf3oRM2XKfR3cRGJf1x650hldwlpTgjDz8HCfTtOBLKdKlzDogU4uMBMlKpGnhId_dh_2lde310UVR4epoHmm4WrM0u__LkLzJhftv_Gn6xzsBJ1rqahxQ_apMieoq7OXP9jwWJCXhHubaHZap7qhYDtlasZfD-Bnh4vLL8J72JHyWgbXpX9IHDQeo1pULcX4Smp-xh9d3NE5tdX8hueIjcofMXUIFM9cTIRA4bJFB3XV5llFIDYCunTEnyXQ__TaetUIVOcbxaadF9q2j0lrdkxjaWWMpHVubjymTNFn3h1g3ARtRIb6ygIhf-_wtkZ8X-7PCfGof9MjtqjO06rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69347998c.mp4?token=imf3oRM2XKfR3cRGJf1x650hldwlpTgjDz8HCfTtOBLKdKlzDogU4uMBMlKpGnhId_dh_2lde310UVR4epoHmm4WrM0u__LkLzJhftv_Gn6xzsBJ1rqahxQ_apMieoq7OXP9jwWJCXhHubaHZap7qhYDtlasZfD-Bnh4vLL8J72JHyWgbXpX9IHDQeo1pULcX4Smp-xh9d3NE5tdX8hueIjcofMXUIFM9cTIRA4bJFB3XV5llFIDYCunTEnyXQ__TaetUIVOcbxaadF9q2j0lrdkxjaWWMpHVubjymTNFn3h1g3ARtRIb6ygIhf-_wtkZ8X-7PCfGof9MjtqjO06rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اولین واکنش امید عالیشاه به فحاشی ناموسی خداداد عزیزی: دچار شرم نیابتی شدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106821" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106820">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854ffbdefd.mp4?token=pqhnkZ7D3e_w9buO1G5YzU_hKv80oOCOySma-pRoMT4suA4rfnxoiXN9GVR-1raIbc0bv8_XYxRi-cMTSBs_o-o7p88jF8g7LiYSYBHXBvCGbor2mQdbAElVRdZoNzecEUVukPPbUJZAIHO5252cApeqhzgr-TEYfXhh7knLrE4uOaQeyeydZbGreAqmDoxpZyt6rCa5kMgCiAbOx3dglE7AjUQC9dihRDoBq8zIkFN2b-_uQr4WnSwxooLv-OrIPgcBJz7hTa28gW8olsHxrlswNV4K5lXPcTdsBKoYV56X6lObYjdWltHgLMQdMYwymLnk5mSoaByulfzwkEyO5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854ffbdefd.mp4?token=pqhnkZ7D3e_w9buO1G5YzU_hKv80oOCOySma-pRoMT4suA4rfnxoiXN9GVR-1raIbc0bv8_XYxRi-cMTSBs_o-o7p88jF8g7LiYSYBHXBvCGbor2mQdbAElVRdZoNzecEUVukPPbUJZAIHO5252cApeqhzgr-TEYfXhh7knLrE4uOaQeyeydZbGreAqmDoxpZyt6rCa5kMgCiAbOx3dglE7AjUQC9dihRDoBq8zIkFN2b-_uQr4WnSwxooLv-OrIPgcBJz7hTa28gW8olsHxrlswNV4K5lXPcTdsBKoYV56X6lObYjdWltHgLMQdMYwymLnk5mSoaByulfzwkEyO5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🐐
دیوید بکام: "من هنوزم باورم نمیشه که اونو اینجا تو میامی داریم و داره واسه تیممون بازی می‌کنه. همه ما دلمون می‌خواد لئو تا ابد بازی کنه. هیچ‌کس تو 39 سالگی همچین کاری رو تو این سطح انجام نمیده. پس حقشه که کاندید توپ طلا باشه. به نظر من که باید ببرتش!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106820" target="_blank">📅 19:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106819">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dccf6f34c.mp4?token=MoCf2SmwBiPeQzh6VmpZ4MjyFbMIwPDqP2RROzIjvCjZFCNmtyxgaDzJfvnR7IAO7soYz9x8LFE9mctAu6NYGkhtS8ssj7fgCbKwuQdbJebtlcss0WGBPv-IT70G6f2NulMA1o-6aS8leO82GJerQUyJemIdYS-pIcRrLq7kKfT7rc4ZVlpJF-cNgh_FvPHDdzEofHFM0UjWIQ3TIyxkYbYpT4l6UksEpezFKe-__cL-znZ_DVKJTDJ2QYaqW31a4rUUs26ygG9yhU6wVDo45nQIRxaJYbsSX81AnEUMhzXqgxJ3bP4446m1gw0QkOvu76QLkfGBBtNRJnexR8b9iYNN419cmMaEvzV8_UcOrSBxDvMQRqZlhQbrz3_RpXhgiqGz5VeAAoquGmKnhwCVKFm2RH95Q1QcZGM46EVqDNQlxg9W9xUeWCnDp27f_OKi1YR6Z8wkUXPjY7B-H4grjb6bOnX5OuV2_tR6SaSrGo_TiTUOG2JYAgqYCrkqsOVn2zsOeQWhlOiHx9lLDZ3i2VyLXX8MQYhDt2lcsjgD0tf9ncirhsfj0h_mhm595GV9gyUAj3unHgFOiQQ5ZxWlKlsG_q_DWMbx8F9EbDZIP06JAmfsNqLOe7ky_3L03-BTU2-aI5FoZfunLSYif5MgAhVH1NbN1-eAobmWYLriZ4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dccf6f34c.mp4?token=MoCf2SmwBiPeQzh6VmpZ4MjyFbMIwPDqP2RROzIjvCjZFCNmtyxgaDzJfvnR7IAO7soYz9x8LFE9mctAu6NYGkhtS8ssj7fgCbKwuQdbJebtlcss0WGBPv-IT70G6f2NulMA1o-6aS8leO82GJerQUyJemIdYS-pIcRrLq7kKfT7rc4ZVlpJF-cNgh_FvPHDdzEofHFM0UjWIQ3TIyxkYbYpT4l6UksEpezFKe-__cL-znZ_DVKJTDJ2QYaqW31a4rUUs26ygG9yhU6wVDo45nQIRxaJYbsSX81AnEUMhzXqgxJ3bP4446m1gw0QkOvu76QLkfGBBtNRJnexR8b9iYNN419cmMaEvzV8_UcOrSBxDvMQRqZlhQbrz3_RpXhgiqGz5VeAAoquGmKnhwCVKFm2RH95Q1QcZGM46EVqDNQlxg9W9xUeWCnDp27f_OKi1YR6Z8wkUXPjY7B-H4grjb6bOnX5OuV2_tR6SaSrGo_TiTUOG2JYAgqYCrkqsOVn2zsOeQWhlOiHx9lLDZ3i2VyLXX8MQYhDt2lcsjgD0tf9ncirhsfj0h_mhm595GV9gyUAj3unHgFOiQQ5ZxWlKlsG_q_DWMbx8F9EbDZIP06JAmfsNqLOe7ky_3L03-BTU2-aI5FoZfunLSYif5MgAhVH1NbN1-eAobmWYLriZ4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انزو مارسکا سرمربی سیتیزن‌ها:
🔺
تردید هوادارا پس از رفتن مربیای اسطوره‌ای طبیعیه. این شک و تردیدها برای هوادارای منچستریونایتد و آرسنال هم بعد از رفتن سر الکس و ونگر وجود داشت. برای هوادارای سیتی هم همین مسئله صادقه، چون پپ هم یه مربی معمولی نبود. اونم مثل سر الکس و ونگر، یه اسطوره بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106819" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106818">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106818" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106818" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106817">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPXR_Nme2ou5s9vM2nrxXrngCS_5xqHYozUzOOrM8XlDhUfnepNSMb2mAX2QFoTanEpmWGbuRNfDuiL1PQ73s0ZPo7MSTGsHYV4668Clstj1-DToM_7Rbq0-VMtjJsbFHDuHe-aGWlDHFFOo3RPybETFNsR-cIvAcNfLBc5ggOpNGYGqfRbkGADEuMeaXzrK-V1f8gkrP4Bp3bDQJaXmnVEo_aNM6yvbmOCQHFARwPHhKB8-NXcMITl9U_eNVARakNPtl5i8Tod5fW1n2TX5JPYNu7jvWWliOXjbxLkQM4rYHLFTGChk8Uvr0xwpEge2S394IqH0saPpO8WKjQ3ffA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106817" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106816">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabf7dd06b.mp4?token=QfWpANYdI-S8H8s_lznq9NNy6OCK9BFWm1CMN2_TQZffl9Kt35bypgsjuBGgwXhf8xZ86zw0iaJI-0nKIfJflRpKlkqfLYtedfo5jHurXPgj6fYZgc4t8VKinO90yoXZPOr8voujXJHkrWQ-0JTuouPQ9Cb9UsPEmpUyV-M335oLQB1B9PpHEx88T6ZsQcbg_Mg-e58kr8TXsyR0Vc_QGsge28FL1QGW6yCuBJITkBHPx_FfmgTXw4RwkU7ujdMsS3lUbDpauTUUX8nDCNyLPoSjiNTvk4OKBhP9KDoHSC-smO7UykMt7miL-QAUG2Zxn0rifHt0VhzSbbWoPWXbyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabf7dd06b.mp4?token=QfWpANYdI-S8H8s_lznq9NNy6OCK9BFWm1CMN2_TQZffl9Kt35bypgsjuBGgwXhf8xZ86zw0iaJI-0nKIfJflRpKlkqfLYtedfo5jHurXPgj6fYZgc4t8VKinO90yoXZPOr8voujXJHkrWQ-0JTuouPQ9Cb9UsPEmpUyV-M335oLQB1B9PpHEx88T6ZsQcbg_Mg-e58kr8TXsyR0Vc_QGsge28FL1QGW6yCuBJITkBHPx_FfmgTXw4RwkU7ujdMsS3lUbDpauTUUX8nDCNyLPoSjiNTvk4OKBhP9KDoHSC-smO7UykMt7miL-QAUG2Zxn0rifHt0VhzSbbWoPWXbyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
فرشید اسماعیلی: دلم میخواهد دوباره به استقلال برگردم و دلتنگی شدیدی دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106816" target="_blank">📅 18:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106815">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO78jWhcTNKGNWc3X0DrZdKEBpY6CJOVYY35gZTXk0Nu_C3KZVTF8zoxlUHL730lbepEJTvObQD8IGW-6B6D55FOfFECB-PVyqRu2kyN24CIydDZkdHRISH6nOu-XuL4vfQda_v0BBTYX3AVZebY5poL5yx91XjNEVtKCRqA5z2Djnmcv3_5ZWSzOGfFZO4JhBM9ApibHSo6q8sAVNwCpcpPcQ5LcB6SGYi8OF2udka31p-dMdVNClAV7vo7GlWxU4oHEtA-IMhy6w7fWZyi4FwlW1Y0Wlj4E6OA1HYH-UwD6PihC57ZT_zzNCgSMpZZJ8CuAYilgazYnLg6CHzYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
لامین یامال: من در تمام افتخاراتم از امباپه پیشی گرفته‌ام. به عنوان بهترین بازیکن جهان، شاید فقط دو نفر باشیم. من فکر می‌کنم که امسال شایسته توپ طلا هستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106815" target="_blank">📅 17:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106814">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd6e64a79.mp4?token=N_cTgY_dg04aY-hXHY702Yuw0otXwIJXffSL-JhTe3sryauUQuVjDFwOC47pxs7z9njMbw8jtsCE07ds1XUx45wQYkZy7Ke1o6m5-25n2qas7oXdaqJSXTV7-eE7GW1cFsSwKecLK4Xf_gEmK4W-APUsJoS_OvKqQ9vXYlraMDHWqb9qv3787IZJAuAtpSppjknrbthhzg-AzAGNCG1_6cMhgdSkylYlzU5NczAuJSavVqNnKTQxaqBH1jWZY-FyiUCTuc__28IXzKiFFrPUV-fEiPhLNaZU1_zXgV3y9IQPkWUHZ2l7-5RywTAB4F0GWhU4Faqu5ynoBCW7ArDWxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd6e64a79.mp4?token=N_cTgY_dg04aY-hXHY702Yuw0otXwIJXffSL-JhTe3sryauUQuVjDFwOC47pxs7z9njMbw8jtsCE07ds1XUx45wQYkZy7Ke1o6m5-25n2qas7oXdaqJSXTV7-eE7GW1cFsSwKecLK4Xf_gEmK4W-APUsJoS_OvKqQ9vXYlraMDHWqb9qv3787IZJAuAtpSppjknrbthhzg-AzAGNCG1_6cMhgdSkylYlzU5NczAuJSavVqNnKTQxaqBH1jWZY-FyiUCTuc__28IXzKiFFrPUV-fEiPhLNaZU1_zXgV3y9IQPkWUHZ2l7-5RywTAB4F0GWhU4Faqu5ynoBCW7ArDWxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
نظر ژابی‌آلونسو درباره مالکیت جدید چلسی که به یک فرد ایرانی واگذار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106814" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106813">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-SCdtcTB8tjQlZM0-xeL8Abr0_FaVeWsIc7M20h7kgGdvikTRG9FwT10NBHu8upzOt6mQuY07eQEs6CwIqiAjNAhcd_TqfM_NkAOUXBvUb8_HskDXmkkMoFg5lJhwnxckJL0GBP9bJiBN8LB37jhrb1WtW5jvvq3CqsG_jxlIYtpz6T3vIUm5txDYEh85m2DcgNK8W6gDutvnvAKJ1I7iCI1YiRF3kit0puVec88T09RDfSy-pKJrsuCM3rygJ6hK3NpyhtzojbPQxMruG2bM6aEA9Zi8NxSGDN8lWafUctM_vraY_El94-6sciITwuAD_mx_3hiZdOKppAEb8jBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رافینیا: می‌خواهم قراردادم را تمدید کنم و دوران حرفه‌ای‌ام را در بارسلونا به پایان برسانم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106813" target="_blank">📅 17:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106812">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac9522ee8.mp4?token=N3nSMtb_59dfBgkJy4nBmAu0aWNL2-QdHojq-eOwA9qeVe4HEuCmuQGNdBwwdEFug6LEDHm_nnJDz5zlX-lAjIv4MHqeNa94vFJowl6UTAqQlyY49PxheaALYisNf6BE2JpzEKntX0B_tIWRoOhhYN6ZEzYooXWS5V0hiqUQBZGQ6Rook2C1x8iggt5N_ZrWP1DhGysmUCkbQ5IiFh9r7Jih5DGDmP01XIl8iUVCH5pzUzhjlqswTIrYaJ6g6tuFfCjeRLuIgmq-rNxXZ-Q8VqFTiU3TtkvAAt_gQOH3aEE3DgO7fkqhEYdXUVOZWzNEt0ck6pmCUEqBEJ4D0vXlNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac9522ee8.mp4?token=N3nSMtb_59dfBgkJy4nBmAu0aWNL2-QdHojq-eOwA9qeVe4HEuCmuQGNdBwwdEFug6LEDHm_nnJDz5zlX-lAjIv4MHqeNa94vFJowl6UTAqQlyY49PxheaALYisNf6BE2JpzEKntX0B_tIWRoOhhYN6ZEzYooXWS5V0hiqUQBZGQ6Rook2C1x8iggt5N_ZrWP1DhGysmUCkbQ5IiFh9r7Jih5DGDmP01XIl8iUVCH5pzUzhjlqswTIrYaJ6g6tuFfCjeRLuIgmq-rNxXZ-Q8VqFTiU3TtkvAAt_gQOH3aEE3DgO7fkqhEYdXUVOZWzNEt0ck6pmCUEqBEJ4D0vXlNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
بابک مرادی بازیکن اسبق آبی‌ها: یک کیلو و ۸۰۰ گرم طلا بخشیدم به استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106812" target="_blank">📅 17:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106811">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45512a16b8.mp4?token=ZV5FotvpgSRx_gkr3IEAewFLeIXcvp4Zi1etkpCiU0BxJU-kR8QxJxjs-UAdhI7lIvZROn4gk7ex_OJQ5Nc3HW4s_7E_GXMLlPMt9JLVW3G2gPLhrIXspyXqt-hdlHJamj7GGUTbjiOVxiArL4zZQ47gNd4gEZEMLhh-QbSMEcuCq_QEiWP0T8WGDAuDY_i3Em0UnIu_8v2u1uzrpysvr7Ewp93rK6LgpBQ7_umiqfo7GpYAG8F2Q83oU28GYtVyKiw6HTtJSlZ6gsHb4TA8yAgIp1-XCLW8S7tPk2W0zGbi9GhSsgHNoJ_qZftqE5-yFma0XvxTMqExLZS_AC9UHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45512a16b8.mp4?token=ZV5FotvpgSRx_gkr3IEAewFLeIXcvp4Zi1etkpCiU0BxJU-kR8QxJxjs-UAdhI7lIvZROn4gk7ex_OJQ5Nc3HW4s_7E_GXMLlPMt9JLVW3G2gPLhrIXspyXqt-hdlHJamj7GGUTbjiOVxiArL4zZQ47gNd4gEZEMLhh-QbSMEcuCq_QEiWP0T8WGDAuDY_i3Em0UnIu_8v2u1uzrpysvr7Ewp93rK6LgpBQ7_umiqfo7GpYAG8F2Q83oU28GYtVyKiw6HTtJSlZ6gsHb4TA8yAgIp1-XCLW8S7tPk2W0zGbi9GhSsgHNoJ_qZftqE5-yFma0XvxTMqExLZS_AC9UHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
چرا فیتیله‌ای‌ها دیگه پخش نشد؟! افشاگری عجیب علی فروتن از سکانسی که باعث توقیف برنامه فیتیله‌ای‌ها شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106811" target="_blank">📅 16:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106810">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3_uxCwasajqVzYv3Tw-97AJ-cdO1uaSubLLdqOVui7YXuZcCqnJ4YsJPtFN4Uvd4wVaslVMAmojjqNFaZYiCmmVfDuNPhlWb25AtodCKBbcu7KyQPWnsRY9At-Xfr1kvcBpdluKclodW3VrKn8CbuAjw6CYACr0a9gFMN0v41pIMuGZIbjmCUR0pJVrdQC0L1rRHehKUNc1DlpNMQBYgywx6-2CQY3kHYo-sr6vEdSVWYa01lU4-r4uKLl6vxwK1wNf6VQw1lYTyyXJiKXLy-o_eSl5B2XD2d55gnlG7FlHwOsCaTeEDBVnvKCt_1Api0mq_-aYhSUAeiT7id9BKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
۵ قهرمانی لیونل‌مسی در ۱۱۵ بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106810" target="_blank">📅 16:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106809">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171fd833db.mp4?token=WNSHRWE2kVwW3wUiEoL359junnK2wEQxNeXwgEU37IpyrtED2A83oyvQMe85UcZaRXHuRuwoIA7R1o3FmMOC6B3KTC9WTH5w9xMcO4fkGJjo_Q_vbrSKjuku5LiB9IOXNCVESl3eUNI2Slj_WZS-fMh33ABDi5xemO-elSMIqcJuWkYckcokFgNnPm5wbrI25ae6sMC1C1ngFvGrK9ygw0PU7-N6djXhI5HdH7OqC_uPDYOCAPeP7bpo3w3o2e0RSG665w0gTDbt7d6YtNQ34e565z7_2UzMJIY0Qj8VnNTZwjoI-AT8c_o5ONcyDfAsWb_EYtRuKl4OvchnEmjg8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171fd833db.mp4?token=WNSHRWE2kVwW3wUiEoL359junnK2wEQxNeXwgEU37IpyrtED2A83oyvQMe85UcZaRXHuRuwoIA7R1o3FmMOC6B3KTC9WTH5w9xMcO4fkGJjo_Q_vbrSKjuku5LiB9IOXNCVESl3eUNI2Slj_WZS-fMh33ABDi5xemO-elSMIqcJuWkYckcokFgNnPm5wbrI25ae6sMC1C1ngFvGrK9ygw0PU7-N6djXhI5HdH7OqC_uPDYOCAPeP7bpo3w3o2e0RSG665w0gTDbt7d6YtNQ34e565z7_2UzMJIY0Qj8VnNTZwjoI-AT8c_o5ONcyDfAsWb_EYtRuKl4OvchnEmjg8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی نشون داد پَرش و ضربه سر هم خوب بلده.
😮
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106809" target="_blank">📅 15:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106808">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb5c6a4f7.mp4?token=sYszOFH3iMQ1ErdtbVzJNZ1Rq-3xZcd7PenmBqRPD_X_eQBi31nNiS97snW2cZzH911LITtmgLrk6G-QuPegh9eXAkiSRrcf7lrULklP9m2b3ONgx-DArg1bRIdpvHyPZambWh3JewPF87CddpZ87mz97iffZ2pXNLmOahGjEXRDLXf96gd-swhm26BQbBXT8YhSBvvkAZm_iubJhtNihM9ifdx6Ozjthc-9n9-TpkvLNM0SH7roTYRvDypUJSrJtiYQxKHiAhJv0lYViY-W4QKzm_o_QLQbGJyZhwN5hJ3K_o-WTTOospl4CFkbToY8TGzzUH5aBuDBBIiOPamm4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb5c6a4f7.mp4?token=sYszOFH3iMQ1ErdtbVzJNZ1Rq-3xZcd7PenmBqRPD_X_eQBi31nNiS97snW2cZzH911LITtmgLrk6G-QuPegh9eXAkiSRrcf7lrULklP9m2b3ONgx-DArg1bRIdpvHyPZambWh3JewPF87CddpZ87mz97iffZ2pXNLmOahGjEXRDLXf96gd-swhm26BQbBXT8YhSBvvkAZm_iubJhtNihM9ifdx6Ozjthc-9n9-TpkvLNM0SH7roTYRvDypUJSrJtiYQxKHiAhJv0lYViY-W4QKzm_o_QLQbGJyZhwN5hJ3K_o-WTTOospl4CFkbToY8TGzzUH5aBuDBBIiOPamm4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
اعتراض تند رسول خطیبی به حمید مطهری و تیمش بعد از باخت لحظه‌آخری فجرسپاسی به فولاد در اهواز
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106808" target="_blank">📅 15:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106807">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N98BjJOfPpix7Gm-5fdFCfiariPegrqnfknBwfFRbeYtJKogsFUpjk-AmOrI_fdSICvaswk6RekAkNnea1gsTDC7sDKTuVjym2Fd7oSs-8aZl14_Q8zKDcXjijN6DWbXKkbre5loGlIstOFZhs96TKMuCsBSwtslvMEfCPr-uvzJzEK3IBAJPKqAolUlTT2_96NMTMZBFX84BBFpj0E5_M-YUgYGGm5nzF72zQNrd89_JfXePo151iVoKq-7Lr0Z3tWUD7tMKjNrmerITVxJ-Hw14YjvqkhDrVNUjCtqEv86q0BCNLF_7JK4Zd-R7MYIcbUAine9jbazG6kmA3gUtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌐
گزارش هیئت مستقل حقیقت‌یاب سازمان ملل درباره مدرسه میناب: مدرسه یک مکان غیرنظامی بوده و در عین حال این مدرسه در مجاورت یک مجموعه دریایی وابسته به سپاه پاسداران قرار داشت. اطلاعات مربوط به مدرسه در سامانه‌های هدف‌گیری و بانک اهداف آمریکا آپدیت نشده بود. هیئت این حمله را یک حمله کور/تفکیک‌ناپذیر اعلام کرده که موجب مرگ غیرنظامیان شده. بر همین اساس، هیئت آن را جنایت جنگی تحت حقوق بین‌الملل ارزیابی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106807" target="_blank">📅 15:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106806">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40dc07061.mp4?token=gF4WgVfkvjl6kASi964BUVmWaz469WX8SOITeXWFkt5zbsbvRJJydn8BamlpetOCDfqLG-EErXBggCbuV6ek3Jfa8eG6lGFfwQLNE4ADw7zED8FJ5wfHRg9mIFcIuslsBvPzo6Uwv_FoDmrm-Z8dMDCLMSEUoOJpUsKciJL34x23Rep9237kD1tEOzxaitsgBY5PxksANpu5bgtci6PSwomHVMWjp3Cfw9YPYHhQssmQqHwpLN6RakJKQCVK1UcXHYdAX-H4BnUMy0kZHasHyBjWtg1RA8cl2-CwDvbNApGutEBxeiG6U3S_VUxaAb6QWBfj4b7W8XcSi5NhdjZp-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40dc07061.mp4?token=gF4WgVfkvjl6kASi964BUVmWaz469WX8SOITeXWFkt5zbsbvRJJydn8BamlpetOCDfqLG-EErXBggCbuV6ek3Jfa8eG6lGFfwQLNE4ADw7zED8FJ5wfHRg9mIFcIuslsBvPzo6Uwv_FoDmrm-Z8dMDCLMSEUoOJpUsKciJL34x23Rep9237kD1tEOzxaitsgBY5PxksANpu5bgtci6PSwomHVMWjp3Cfw9YPYHhQssmQqHwpLN6RakJKQCVK1UcXHYdAX-H4BnUMy0kZHasHyBjWtg1RA8cl2-CwDvbNApGutEBxeiG6U3S_VUxaAb6QWBfj4b7W8XcSi5NhdjZp-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
▶️
مهمترین اشتباه در محبوب ترین حرکت بالاسینه؛ به توصیه استاد هانی‌رامبد عزیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106806" target="_blank">📅 14:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106805">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIe1NQNRWMXm6vHDQgm3PF3jbltSCttLTP0odcoPK0uQCy0reKjEcBVaPZNOGo_uuTkDLNVbH616THsBwg-FZzjTsSYAIzqeLFac6myAWBLPUYl4XBaSharC1I_E0jI84jOmllku7A5ySfoKT5LNNzqUhF5Ig759618I13oPcGPNNqTusKuk4y9ihLCQt4BkNPQ8-l4r7LzQ3mbmyJ1wxE_g6C4pZQiRbPvLB9DTMtetF0S3e9z1HjlTO5ZLj-4HIdF2E2js2E3bqUO9eGyFlNoHWWs_5MGfvEJ5TJuyqEYrFYTBMoMkk34-zyYCQVsZtnJXA96P2FCTQ5AAG0YQOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیبو کورتوا درباره برنامه‌هاش برای آینده:
کار من بعد از خداحافظی از فوتبال؟ شاید کار توی بخش مربیگری دروازه‌بانان رئال مادرید و ساخت یک آکادمی درجه‌یک تا به جای خریدن یه تیبو کورتوای دیگه، خودمون یکیو پرورش بدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106805" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106804">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNx3CYJxLMgnXE0fUuW_hHtZaCA6oEgKW0bjKPk8vaDUfG3UF0b49Cn9E7DPa79uKQNsoasRQDYkcdcGS3c_rjssYL3yFU7C1ABEOusTyzsYDf3j4w53Ha9Nahe4A8a2HtcTwchtB3gDlmtBXLTTPkYSSEq7NujOu7a070Kj4DjMRuUncfEQx9s7_iYELfAAvHAjCfLH5cHWy22EvAyg3BnBkfTQwrIhjRss2mVHEZV5GweuGUEGgmDcHu4Al2zFD4RLhkpNy0MXwCHj7mkejn4vFEeQ0uzcOTkKejYe_BwEkmeg8Y9X7XemteTFNyqW-9dgl6VAtbNIFROlNR4WaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هری کین درباره توپ طلایی:
"من دوست ندارم درباره خودم صحبت کنم... 73 گل، خودشون حرف‌های زیادی برای گفتن دارند."
"این بهترین فصل زندگی من بود، و این تفاوت بزرگی ایجاد می‌کند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106804" target="_blank">📅 14:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106803">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325a2dc7b7.mp4?token=WA5igbSCeWCdfVnw-pONZ3qYD46rxRDoWe_blBc2eT9mxGnnwuj4vjd_3WZJCrjdJB3QsMZFgcW35TwHrXkO5M-pmzPhI_FD7EFIel6cRDbBPlPCNW9Lf3UggAcc809QhigI33XFdxiu3deS3eJXyiH1H2_-Y84BFaYNtRhYZF4DpRICE46nPGhXl43EinmpQ_ix42Z5zCnOiYx7_V4khwB_uRCs8UX-ogBQSf8PVF7BKTFJ17B2nwa7SnbGG6W_nLF7kAPHB4fb9p2SibXYlMdC7V1-Cdjnh4HDhfwyHBzJZUkSy5J_rHH7AxWCXTRF7xA6onN2jwLR9YfR7mGligcjy6Cs7TPu1qo0VH6uNeyCtylN7yndV_LiFoF5DyXz8TGKUwntFZN_XJ94yW8j2_Y9MkjtQOjf3fNMO80i0FZXR6lTIRp8kS0THI1jgwQjtkXcqyMhQraHVArTTJ9plitHLtFS6jlogkutYPZLODZ0MLwMOGEUBukjzY-_o1hq8hTd158ic09oHXyTg4n38kTk1Hh1Fh1H2RxdCm8EQsj4E3JYJuM9Cl2NiUeU7LAep9yy2MTAuA9T8jtvA-FW6A2PpqPPTGHuUwdEDj9wWZ5fQLCRsCZ-zvKJmMpDfRvs90zEX0FQGq3-encjmFXQ9BQf_LCieR43PhZhzxzFLTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325a2dc7b7.mp4?token=WA5igbSCeWCdfVnw-pONZ3qYD46rxRDoWe_blBc2eT9mxGnnwuj4vjd_3WZJCrjdJB3QsMZFgcW35TwHrXkO5M-pmzPhI_FD7EFIel6cRDbBPlPCNW9Lf3UggAcc809QhigI33XFdxiu3deS3eJXyiH1H2_-Y84BFaYNtRhYZF4DpRICE46nPGhXl43EinmpQ_ix42Z5zCnOiYx7_V4khwB_uRCs8UX-ogBQSf8PVF7BKTFJ17B2nwa7SnbGG6W_nLF7kAPHB4fb9p2SibXYlMdC7V1-Cdjnh4HDhfwyHBzJZUkSy5J_rHH7AxWCXTRF7xA6onN2jwLR9YfR7mGligcjy6Cs7TPu1qo0VH6uNeyCtylN7yndV_LiFoF5DyXz8TGKUwntFZN_XJ94yW8j2_Y9MkjtQOjf3fNMO80i0FZXR6lTIRp8kS0THI1jgwQjtkXcqyMhQraHVArTTJ9plitHLtFS6jlogkutYPZLODZ0MLwMOGEUBukjzY-_o1hq8hTd158ic09oHXyTg4n38kTk1Hh1Fh1H2RxdCm8EQsj4E3JYJuM9Cl2NiUeU7LAep9yy2MTAuA9T8jtvA-FW6A2PpqPPTGHuUwdEDj9wWZ5fQLCRsCZ-zvKJmMpDfRvs90zEX0FQGq3-encjmFXQ9BQf_LCieR43PhZhzxzFLTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تأثیر غیرمستقیم تحصیلات بر فوتبال، از زبان بهترین بازیکن جام جهانی ۲۰۲۶ و برنده توپ طلای ۲۰۲۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106803" target="_blank">📅 14:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106802">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2929cbe0df.mp4?token=KOlPV3kIk3eeEYLcB_ifvGRfIHk_3FjuCMQXg95DNIqdcHxk7iiwSCJIk6CRifYU0TSwZw-eBsp__I_7K40EN_DgOIh3MZ2VpOY0CsgsBmnt6Zy-IFolGTvj1feMkFz-HqWvxg9fbhWFx5rNdec17rRq0DJl39grnugy489XCDTLETuK9Gxx76aFux0rdjW-ZFesZpHo4AhihmSJHsWPiHq8-Mk-aCpQmsFNf3oyAwPxr-7pmyx_b9lppYcIQSnRIOoLkyWcpOAcJ8J1NF9mXPw73GfwNQklq2whtxQFGp8qTHTkK7gJDCz8Gh-K9f1-WOBGypxDhZofnZArfJ8abg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2929cbe0df.mp4?token=KOlPV3kIk3eeEYLcB_ifvGRfIHk_3FjuCMQXg95DNIqdcHxk7iiwSCJIk6CRifYU0TSwZw-eBsp__I_7K40EN_DgOIh3MZ2VpOY0CsgsBmnt6Zy-IFolGTvj1feMkFz-HqWvxg9fbhWFx5rNdec17rRq0DJl39grnugy489XCDTLETuK9Gxx76aFux0rdjW-ZFesZpHo4AhihmSJHsWPiHq8-Mk-aCpQmsFNf3oyAwPxr-7pmyx_b9lppYcIQSnRIOoLkyWcpOAcJ8J1NF9mXPw73GfwNQklq2whtxQFGp8qTHTkK7gJDCz8Gh-K9f1-WOBGypxDhZofnZArfJ8abg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
زیباترین گل‌های کاندید پوشکاش سال ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106802" target="_blank">📅 13:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106801">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37652c08b0.mp4?token=sxq_lTxraCDzlfQn8hJRgjx-X4eI083Kwt_UFZcR9-a3DXU163T3y7hQcCUWrIFbYn9bo63J5hh55RQSqvCAhcWzICzSaIvtV2kamx3LZ1b3pbOxeschqkSYP_AeP8zcv70q7klXByqFLUKRcejmwTYBRHydNQr7hVlFodVDshRy3D_Ha_DC9Cdblh-XtPVwD3HfOIBzEa2ny3rFm5F073yvEnOYlMzznkfIrWwBUHoTUzYqgY94vT-r2SLZHipn2P6lGulhORth33gEFWVTeQO0tDl_zgsKflBF0xLmVWnrXmnvw_MbgRyycJX5weFlFE1a-2pNfMUCdUEKEUtjPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37652c08b0.mp4?token=sxq_lTxraCDzlfQn8hJRgjx-X4eI083Kwt_UFZcR9-a3DXU163T3y7hQcCUWrIFbYn9bo63J5hh55RQSqvCAhcWzICzSaIvtV2kamx3LZ1b3pbOxeschqkSYP_AeP8zcv70q7klXByqFLUKRcejmwTYBRHydNQr7hVlFodVDshRy3D_Ha_DC9Cdblh-XtPVwD3HfOIBzEa2ny3rFm5F073yvEnOYlMzznkfIrWwBUHoTUzYqgY94vT-r2SLZHipn2P6lGulhORth33gEFWVTeQO0tDl_zgsKflBF0xLmVWnrXmnvw_MbgRyycJX5weFlFE1a-2pNfMUCdUEKEUtjPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✔️
توضیحات مجتبی‌پوربخش مجری اسبق تلویزیون درباره افتخارآفرینی کیمیا علیزاده در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106801" target="_blank">📅 13:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106800">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9960QSC-MFI7AI_I05cpYfuTYElxVdNsny640X54SF8IlwbPyYtS7B1OqN_cSdpTRVX3hzQLpA43EpS_q8U2dpRuVByhT6XiygZ9Eg32sWs1MvJjdquXIiW3TzInMSK9aL67JfRqlfdDMfsoFAC3NX4s36XzgCVm811uDl5m04pxRU_euyo2lnd8yazKrQs6vtUaPU9hgOwZxqbDqLjSnSO_UBpgAq5tMuOEv2q_A33rmAyR6Rp2HHgxQW_K6CIX5g2Z4e6FPClvzL0FDr2mvlMQxeIuyFlWVSegrDXtyitsWOIObjTr4uFtL9qAfxHaZ2C4mNzWR-L2gw6vjonog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
لیست تیم‌ملی انگلیس برای فیفادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106800" target="_blank">📅 13:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106799">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
🎙
صحبت‌های عجیب و‌ دردناک مهدوی‌کیا از دخالت خانواده‌ها در مسیر رشد استعدادها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106799" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106798">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106798" target="_blank">📅 12:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106797">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVxe_er6hiiOI7h8cstlFEFrvML12c2EOsZSoKd-TXPqQWzerHsUEQYihlk5nTza22R36LgSJMM5eUmRkfFv2ZCKMvNgvbw0LNU-1NGVV3elxB-_q8C8sAyerXTPszcb8eivuGKwTCQb5848pjOle_1XXJeAP9EX5aDsAQfdcegnfWQxxKuV-DxJ0FcO13GG0wuSnaLg2d47CSz_U1tByvZtWFy270l6Qw0mVVijmcbqVYUwpsOFdsHMh5S4T_rUlbPFoxC_yutW0h37JKVnzWvihxZheMjJuG_5ap-DEFBMAUvNjxmeCV-UjhmLcerzl7NVOhT2ekpiQxjQuawdNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
چلسی
🆚
برنتفورد
انیون برلین
🆚
بایرن مونیخ
لنس
🆚
موناکو
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106797" target="_blank">📅 12:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106796">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjpbjAdZMgVsgIytVD0puujvDqLgDPNOmMWE2uIw-YUVf8bZrTL32-oCuLFqPbGba2abILYLWiAK-fQpi5gRA3gTjDWMaIPkCAcrviCrlMhiok6EJa9JR4Gbv-q609n3uqXSP3EUp2VDNTzHfzUQv1UlikG7sQNYNq2W271nmju0UuvNlyonIooC9TzGDJ4RxxP6i42V26m2IrHYcECuXEDxCLjwbFM8H2g8YjdsvHKHg3WOlJ3PFE12UuzzBXygmZNHosnpLQ2KiRM5UmrRpksO20BQAT4ClB_YdmJFZw0Oy3FXQba4pymYBPj0kc-73OZPZD33WvanlXtCcVVJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
رافینیا، با هت‌تریک خود مقابل راسینگ، در 7 بازی اول فصل 2026/27، به 14 گل و پاس گل رسید و رکورد بهترین شروع فصل لیونل مسی در باشگاه بارسلونا را شکست. مسی در 11 بازی مشابه، 11 گل و پاس گل به ثمر رسانده بود (فصل 2012/13).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106796" target="_blank">📅 12:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106795">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f364f9a06a.mp4?token=jgg3WnCpqN1Ul7W_1hrtswiz-xb6xaSYF-4robWniChXqL4Fr9ZrmVCOAJUJVMVYSeOdgus7LUZmeFkYJiGR7L1lcLJmQXQpJwzzBixSUgFJuCUa5YG1Fifj2gHtZ5kxqnEkfz0Spjx3MwUe0inD0_NFf2-XhTyO6RXKbAd1VYeOJc_ijj0uB-CGq3-p7Fmr1deBLHU_MkK5bflM4qyb_dLOXXgCBzBOaVBeGDzleklXgoHmw4T9PuqhH9SIlyF76O6a_q2PELYSTD1qBv8YBlyROZ5oqXo8MQBRhAKjWuJqmyS7fDy8HBWCauxs2uESEpaNyjihFYYqGZZ1vokNHHz21CS5lQAyyChIRXlGz0APsHQNizjykpFx_p2T5lsSGZ59gpjXe4BpRXuGR7n2UTrRXSiwA1aCIZ9qKpYP9aVWdrn4q1nKC7gBBq7sG_jdytTkrA_WughVsu0gkAHAIiRdhiRmMrQvxip_rM9cNnTzJzZTOjtaZXeS7wMId5218Z7CQhWIr2DmQ0Y6HQpbkEi5pmlJmKTeMZ6W11kBu9gHbDuHgOTRCvpSxnVPRBk6-ueCKytGIoDgIxwVlD43pAxVjKlz0wJXulx-7H7ocrxrkEg5hZi1s2AwUbAAbyJu2vyHo3PyWUjix6XKLxbG7JsRM_MmeBlcr90BZ3t0yCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f364f9a06a.mp4?token=jgg3WnCpqN1Ul7W_1hrtswiz-xb6xaSYF-4robWniChXqL4Fr9ZrmVCOAJUJVMVYSeOdgus7LUZmeFkYJiGR7L1lcLJmQXQpJwzzBixSUgFJuCUa5YG1Fifj2gHtZ5kxqnEkfz0Spjx3MwUe0inD0_NFf2-XhTyO6RXKbAd1VYeOJc_ijj0uB-CGq3-p7Fmr1deBLHU_MkK5bflM4qyb_dLOXXgCBzBOaVBeGDzleklXgoHmw4T9PuqhH9SIlyF76O6a_q2PELYSTD1qBv8YBlyROZ5oqXo8MQBRhAKjWuJqmyS7fDy8HBWCauxs2uESEpaNyjihFYYqGZZ1vokNHHz21CS5lQAyyChIRXlGz0APsHQNizjykpFx_p2T5lsSGZ59gpjXe4BpRXuGR7n2UTrRXSiwA1aCIZ9qKpYP9aVWdrn4q1nKC7gBBq7sG_jdytTkrA_WughVsu0gkAHAIiRdhiRmMrQvxip_rM9cNnTzJzZTOjtaZXeS7wMId5218Z7CQhWIr2DmQ0Y6HQpbkEi5pmlJmKTeMZ6W11kBu9gHbDuHgOTRCvpSxnVPRBk6-ueCKytGIoDgIxwVlD43pAxVjKlz0wJXulx-7H7ocrxrkEg5hZi1s2AwUbAAbyJu2vyHo3PyWUjix6XKLxbG7JsRM_MmeBlcr90BZ3t0yCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
فرزانه جمامی، سرمربی پیشین بسکتبال زنان استقلال: تمام اعضای خانواده‌ام بجز من طرفدار تیم پرسپولیس بودند و هنگام دربی اذیت میشدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106795" target="_blank">📅 11:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106794">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lktPfLnH9sWPReawaFKaAHg-dzY-1uN6_xI00cYVe4Jray2cP_e0zOlbWSk1NLeBT8LuUdE6SgBRT1hhnhoQDJRfgWVGXmRDDZry01w-Pt3ZRgeVXdnrThhyXsxXYDwg-hx2SQPdyqxSel1mY2DVlHQnwMpicTf24emy6x04nne5oAL4Vm774OcPactlumbH6vNF09wgj99vlAc_oPd37ycZAKvfmh1ZrnxHxW_I45XSCJ0z2mpduDF8f4_2-MUcdxDmrpFCypdMpriEiyDREfhhNu1RsfyM_8ssWOuV0fIGqW5XArDU6EjiRwq0P5a9ldtTc6r6ojq2ALMeyitQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه شروع آموریم و کریک در پریمیرلیگ با منچستریونایتد؛ اخراج بعدی در راهه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106794" target="_blank">📅 11:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106793">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd63d44791.mp4?token=d3qDWTILxWVNRVaakxAQJDX1g02l1Coyhe4Jdlj21uQrlwtN5KVVfpyTns3QmMmZjV5MWWuu3ww8er2-BZ3cdKyKdrWpLFWpHIc2luzI7G5SI6FoFx4H6S6Kt197wBqrNKcE3plx-V5AvQY9NV65qnRrY6onRaHPJvGiJ7SlMKKj6PGgsTvywB9vuvm70S6KwkdxMRPSOgRe63SNW1XEtlFZKg6O_HGcv2_DNv3GwSykRIJXVwK4o4nD94AkA1sBqStIyCnb_161AYZxh0AoyJvt0f6w13E2tWY1o45r_XlyaOIH0fALLvajl5TDYLK-fXVAPQfKSzDCcn8j6Tq3AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd63d44791.mp4?token=d3qDWTILxWVNRVaakxAQJDX1g02l1Coyhe4Jdlj21uQrlwtN5KVVfpyTns3QmMmZjV5MWWuu3ww8er2-BZ3cdKyKdrWpLFWpHIc2luzI7G5SI6FoFx4H6S6Kt197wBqrNKcE3plx-V5AvQY9NV65qnRrY6onRaHPJvGiJ7SlMKKj6PGgsTvywB9vuvm70S6KwkdxMRPSOgRe63SNW1XEtlFZKg6O_HGcv2_DNv3GwSykRIJXVwK4o4nD94AkA1sBqStIyCnb_161AYZxh0AoyJvt0f6w13E2tWY1o45r_XlyaOIH0fALLvajl5TDYLK-fXVAPQfKSzDCcn8j6Tq3AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پاسخ بامزه علی دایی به یک سوال عجیب
طرف انتظار داشت علی دایی چی جواب بده؟ بگه نظرم در مورد خبرنگارهای مثبت، منفیه؟
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106793" target="_blank">📅 11:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106792">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2af4be6.mp4?token=CL_BLFPttlWZiYsMK_GWW8rZrYsry1EoWo6XsiNnZCAqyBOmiXmCaN3IDCF2NbxtY0u5-2dQgljelC1AyE3GhyY7G-t0hPmvzpWjme4mjy0YP7JIRkpsUdrU35FS6Ag9dELSJjn9wJBLgfSKdDgx9ym3pLB95lqYhhfzwP5ofVA1WEd3ViJDzqTUShgR-q1Cl-Q9W3X1TPYs_EHdkz9RYAfrvEyPuAAvXJFaP5Q-7rxa___O6f2y447gkIPbe4Ayy0pkPfth3Yc26mjOOBr5v4TEwFRdMd3nDCIJRkU1PAZRxN6dpDYL5uQbCNNg2-8MVpZuOmDq79JbkboCDO16bIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2af4be6.mp4?token=CL_BLFPttlWZiYsMK_GWW8rZrYsry1EoWo6XsiNnZCAqyBOmiXmCaN3IDCF2NbxtY0u5-2dQgljelC1AyE3GhyY7G-t0hPmvzpWjme4mjy0YP7JIRkpsUdrU35FS6Ag9dELSJjn9wJBLgfSKdDgx9ym3pLB95lqYhhfzwP5ofVA1WEd3ViJDzqTUShgR-q1Cl-Q9W3X1TPYs_EHdkz9RYAfrvEyPuAAvXJFaP5Q-7rxa___O6f2y447gkIPbe4Ayy0pkPfth3Yc26mjOOBr5v4TEwFRdMd3nDCIJRkU1PAZRxN6dpDYL5uQbCNNg2-8MVpZuOmDq79JbkboCDO16bIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دلایل جدایی اسکوچیچ از تراکتور
زنوزی: اسکوچیچ شخصیت ماجراجویی دارد شاید می خواست با تیم دیگری قهرمان لیگ شود اما...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106792" target="_blank">📅 10:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106791">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebaab7dd8.mp4?token=WmqI2TcZgOEuVW1h4CcIyl52Sg5i4hCFVe6RKLy9b91C6hv0WqmbOtfT2DSwSURC7yPqKzyTwGvnyqLzImpdLJRE3hv8iGgJexYy868DFgdqSjqolavVN0F1Czp2xaGZXVhib-_ma6NEABxs6GsmODNQPFlbMvFQxTQzeusWmJNkPSXuE7eD_dLbB1KSXMo9onqgFeZ9MUwtGCG84uRecQWSjXFxJexxoL5fPXQffdUp4XkVsnCDAHhDm5EI1oDkVsU_Ao7Rdc8S81SiOufzrXe_dFZinodV4rqRHHFNPcZcuLVukDRLYv9tcY18MpUNXRTGYvXtw9994TiFkOj6bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebaab7dd8.mp4?token=WmqI2TcZgOEuVW1h4CcIyl52Sg5i4hCFVe6RKLy9b91C6hv0WqmbOtfT2DSwSURC7yPqKzyTwGvnyqLzImpdLJRE3hv8iGgJexYy868DFgdqSjqolavVN0F1Czp2xaGZXVhib-_ma6NEABxs6GsmODNQPFlbMvFQxTQzeusWmJNkPSXuE7eD_dLbB1KSXMo9onqgFeZ9MUwtGCG84uRecQWSjXFxJexxoL5fPXQffdUp4XkVsnCDAHhDm5EI1oDkVsU_Ao7Rdc8S81SiOufzrXe_dFZinodV4rqRHHFNPcZcuLVukDRLYv9tcY18MpUNXRTGYvXtw9994TiFkOj6bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
روزی‌که استقلال تحت هدایت جواد نکونام قهرمانی و اورونوف رو تقدیم پرسپولیس کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106791" target="_blank">📅 10:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106790">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c341c5cc5.mp4?token=ZSxxg0yQa1XyOelCHOV77SaLgrdSMjv8K8YvKvIIDzzq9u3OUZpCOTxHAEA3kJulE47gvNBRQLAh13gQf82papXI5z7oimN6SjbjD-OmZTAkM0h5yIhqZ7GFKpdU1uMA1ihkylQfCzBu_v-bLwQDTUmM-byQGTScMjHmNWb3cutMD_nYvpvfjuPOZ1jlH2fF7g8L90XGLn6Dz1sE-KuegL800UfTQ6-3ZBY4BdZWoz-JBEAFZIzXV6pRN9gUTCGNMP8bFqIBYoEFHfoQwu482Qa2IgpAyIfctdGfRqw03DcsUpmQS3vf_NGoRY2jtmW_v2zLg9GWTLaNU347Tquuv7Mjlq7ywOaYa4qnUpSWwlw8l7Dbl0lA-xckL1bzmhwGDF73v6y07hipnM063UYfLrIEQykb47Pvh87yBnnS1LBafavFIBoBB5ptw7DvV9IJZuT8iYVevcuwJvh5vN7qV0425F3QNCAZ0KVYmZHTeeBjFPPnjfTHgzjZyNSw7_kfMfNRYnwOyyUG2EBssvplWjlX8aAjSvonyyqQXGfa0iQk21001R1DBVNNZk99HugCVwOGCp3_Y-FM-qLeRUiBRURxZFMWXDUmeSVwJ4oSjpxoLH_bx-EA_VfbzzlybkmeBBGqqXV-y988Y8ZeJdrrzC-Royq2HUPghLscCI9KBSE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c341c5cc5.mp4?token=ZSxxg0yQa1XyOelCHOV77SaLgrdSMjv8K8YvKvIIDzzq9u3OUZpCOTxHAEA3kJulE47gvNBRQLAh13gQf82papXI5z7oimN6SjbjD-OmZTAkM0h5yIhqZ7GFKpdU1uMA1ihkylQfCzBu_v-bLwQDTUmM-byQGTScMjHmNWb3cutMD_nYvpvfjuPOZ1jlH2fF7g8L90XGLn6Dz1sE-KuegL800UfTQ6-3ZBY4BdZWoz-JBEAFZIzXV6pRN9gUTCGNMP8bFqIBYoEFHfoQwu482Qa2IgpAyIfctdGfRqw03DcsUpmQS3vf_NGoRY2jtmW_v2zLg9GWTLaNU347Tquuv7Mjlq7ywOaYa4qnUpSWwlw8l7Dbl0lA-xckL1bzmhwGDF73v6y07hipnM063UYfLrIEQykb47Pvh87yBnnS1LBafavFIBoBB5ptw7DvV9IJZuT8iYVevcuwJvh5vN7qV0425F3QNCAZ0KVYmZHTeeBjFPPnjfTHgzjZyNSw7_kfMfNRYnwOyyUG2EBssvplWjlX8aAjSvonyyqQXGfa0iQk21001R1DBVNNZk99HugCVwOGCp3_Y-FM-qLeRUiBRURxZFMWXDUmeSVwJ4oSjpxoLH_bx-EA_VfbzzlybkmeBBGqqXV-y988Y8ZeJdrrzC-Royq2HUPghLscCI9KBSE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
خداحافظی خامس رودریگز از تیم ملی کلمبیا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106790" target="_blank">📅 10:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106789">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0579123b95.mp4?token=TuXTqb-4MfeQsKusYKBliL2Uuw1iYSUXtG1BXHfkrHMG-f2j7hck5dy44uUv5cszZXeyGmQG1J_JOVr9n2SGjouR5EiApBCFP0S9aP9vyiurX_U3qyx8N3q7PUtDwDmWMR0jj4vlFkUdcEpglVpuaLO5ksgsRLju1xanTilGayS1z5rk_I5Kh9m8dn2o8YOsKIe5_MKBx2nGUrLYW5yhxcZMD4n1edQ2gflisasqjcGqsIkeD1FFrp16vaGziQcKxnlR8brc9hLqd7MvkIm3z8nEW6_tMKV8i8_7G0wwHtC3D4bXtcBCJ2LGmnWJzlcaPKg0-N3bjnfA475ajSkU-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0579123b95.mp4?token=TuXTqb-4MfeQsKusYKBliL2Uuw1iYSUXtG1BXHfkrHMG-f2j7hck5dy44uUv5cszZXeyGmQG1J_JOVr9n2SGjouR5EiApBCFP0S9aP9vyiurX_U3qyx8N3q7PUtDwDmWMR0jj4vlFkUdcEpglVpuaLO5ksgsRLju1xanTilGayS1z5rk_I5Kh9m8dn2o8YOsKIe5_MKBx2nGUrLYW5yhxcZMD4n1edQ2gflisasqjcGqsIkeD1FFrp16vaGziQcKxnlR8brc9hLqd7MvkIm3z8nEW6_tMKV8i8_7G0wwHtC3D4bXtcBCJ2LGmnWJzlcaPKg0-N3bjnfA475ajSkU-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حمله تند فرشید اسماعیلی به شفر: قبل از فینال جام حذفی گفت یا قراردادم زیاد می‌شود یا روی نیمکت نمی‌نشینم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106789" target="_blank">📅 09:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106788">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1063b33e5d.mp4?token=T4NCzdNUhyKGoo6QTpAuLsKotsW_uQGCwhtqIttbOpsTSmpFenk4EM0sHdA3WeROf-nZsL6HwHDaV0vQCxjuwZo8TbYoJRHouhIJQoDefJ27alwdHd43p4BT3MQJHmRKPyhQmXiofG9ANvG6t58Ul9ar-rdg6Bl3feJbDVKDS-t0bA_z9eIbervuRsraMdz7BAySxs9SD1U3G3f_NSMApEBD4KtHTiL9eEPtqscheVxzpd5O3kIxOOllwJkd7M8e-Z698Dulple1VzMrVzhX9XVvo9zXVH_wpAGuFJT3u0PFZceB8Csacn2dtA3-qH7ZFuACJVuLriFXvXQ96RYz7ARU0RvLhFdzS5PAUR-cISSCm5ZxdvwulVg3GgGu7yXMRqWJVwZhcMEnWRLcDWriVfXx7Z65cMxSBmScbD1oHOoqgAmV-6RO1rpmUvJdIViuuxl3hNF7qfs9mShLhyzidl4jofICasuavS_wBQn6JTkXx9SPArdO9iV86Y2QANCqmKq8WtoKULwb01hAoqx1ezYoxHd9hnI8BTnAbPVm2-SoltBbe-4Yb2FlAXY5P6zJPnsytXUb_yIfYzm0xMLeOOO9WOIeG_alqFYyhav4ToAmRZKdtrxq3nmquYQqNKe4fnWDA-WtEv0rcG5rl6HZioj59IrULCVmC2h7TeZXzXs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1063b33e5d.mp4?token=T4NCzdNUhyKGoo6QTpAuLsKotsW_uQGCwhtqIttbOpsTSmpFenk4EM0sHdA3WeROf-nZsL6HwHDaV0vQCxjuwZo8TbYoJRHouhIJQoDefJ27alwdHd43p4BT3MQJHmRKPyhQmXiofG9ANvG6t58Ul9ar-rdg6Bl3feJbDVKDS-t0bA_z9eIbervuRsraMdz7BAySxs9SD1U3G3f_NSMApEBD4KtHTiL9eEPtqscheVxzpd5O3kIxOOllwJkd7M8e-Z698Dulple1VzMrVzhX9XVvo9zXVH_wpAGuFJT3u0PFZceB8Csacn2dtA3-qH7ZFuACJVuLriFXvXQ96RYz7ARU0RvLhFdzS5PAUR-cISSCm5ZxdvwulVg3GgGu7yXMRqWJVwZhcMEnWRLcDWriVfXx7Z65cMxSBmScbD1oHOoqgAmV-6RO1rpmUvJdIViuuxl3hNF7qfs9mShLhyzidl4jofICasuavS_wBQn6JTkXx9SPArdO9iV86Y2QANCqmKq8WtoKULwb01hAoqx1ezYoxHd9hnI8BTnAbPVm2-SoltBbe-4Yb2FlAXY5P6zJPnsytXUb_yIfYzm0xMLeOOO9WOIeG_alqFYyhav4ToAmRZKdtrxq3nmquYQqNKe4fnWDA-WtEv0rcG5rl6HZioj59IrULCVmC2h7TeZXzXs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👑
🇮🇷
ینی بهتر از این خانم بنظرم کسی نمیتونست تمدن کهن ایران رو بیان کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106788" target="_blank">📅 09:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106787">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7912d30312.mp4?token=cewg0HA5JEtjAXWKzzpXxtZAlE-55upWAoobL_IkE0P5ZVPfGsZ1zjzcUxBX6O690h3oHP5t8BstKPOAfPFATrYFTZKXOUuhamV-aACOaYFaWsBojsfQUd3uqyomQG2g9zvkFj3YrxTwtJNIHlR9sY6NFoFQjHxsKb4rjfloKeTi8Vw3yDjLdGv_m93gfAtiMcwbO9kkyE3kf6Zjv6irvPlNUvTxqcmFi3L081dPKefcM7MnoL2-6AXEmBlpH7bn4eWUAksvZKc1bWDlS-UyWvcoh4_UCrFilOYZ7EUPzfswAkmhgVYS1kGUZM95YQZvyJCV-MMDqzoljyR7nr51azH_NykgQr474k3eyxSmvwub3ue8zs7CMc3Q50mj4KYJfbfABizO12NIbi1qjVmTc3zPSazWYHdxf833P0UaCJ-S0BCC_4e6wP-ClxKj9WgFPV_K5yatrn3M-CMu7eSJknm4IEzQVQP4lvcBRUEFP9ByPzwsx-wusYjiyerdBc1dKr2A9R276xmxH4ZX-tQoNw20XTTkdJY667VBa_H9ducpy2AF8n7Fz2T9iAau0qur0q_W4JQkta7ZetmxLvQEBODE6CzJBrD4aAo1gxhAy_KnkostVHBbD-zL5Tb9WOBv0DMNr-taTBuWN7G3CVTqrUWQp4AknUXVEECFWrkBJu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7912d30312.mp4?token=cewg0HA5JEtjAXWKzzpXxtZAlE-55upWAoobL_IkE0P5ZVPfGsZ1zjzcUxBX6O690h3oHP5t8BstKPOAfPFATrYFTZKXOUuhamV-aACOaYFaWsBojsfQUd3uqyomQG2g9zvkFj3YrxTwtJNIHlR9sY6NFoFQjHxsKb4rjfloKeTi8Vw3yDjLdGv_m93gfAtiMcwbO9kkyE3kf6Zjv6irvPlNUvTxqcmFi3L081dPKefcM7MnoL2-6AXEmBlpH7bn4eWUAksvZKc1bWDlS-UyWvcoh4_UCrFilOYZ7EUPzfswAkmhgVYS1kGUZM95YQZvyJCV-MMDqzoljyR7nr51azH_NykgQr474k3eyxSmvwub3ue8zs7CMc3Q50mj4KYJfbfABizO12NIbi1qjVmTc3zPSazWYHdxf833P0UaCJ-S0BCC_4e6wP-ClxKj9WgFPV_K5yatrn3M-CMu7eSJknm4IEzQVQP4lvcBRUEFP9ByPzwsx-wusYjiyerdBc1dKr2A9R276xmxH4ZX-tQoNw20XTTkdJY667VBa_H9ducpy2AF8n7Fz2T9iAau0qur0q_W4JQkta7ZetmxLvQEBODE6CzJBrD4aAo1gxhAy_KnkostVHBbD-zL5Tb9WOBv0DMNr-taTBuWN7G3CVTqrUWQp4AknUXVEECFWrkBJu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
صحبت جالب رسول‌مجیدی درباره تواضع رودری ستاره بارسا در دلجویی از والنسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106787" target="_blank">📅 09:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106784">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axUevwwvtTFpKgi5Qyti5Te6BLiggDr_hanRk2oiNaJWi9tuoUpRFq3j2fOJtxCBW6SNmwdF55sk50i3fN7bWhG0BCvdABF7dI0qa9d4yz2ecwL7rNP028DFjgDXEtJwx2RycvCEREweXztsbphLYbaJyWYwmKgtBERI5hkplhyB3SSPhPGkbWUUWStqh8ilapA2f44chzD3M79lv7w6PExtsYmiNq1tTjP_-20i8bZ0VYrDUeFbPKW1gAe5YBqx4Pl-odhZu4MMPpt9J8eqfqJh_uPKxY004qfbl0AIw0N4enSjfNIQRxjqtQNuDhTPVdF9NYVGBHyd2Oqp5lkCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📊
🇪🇺
نتایج هفته اول لیگ اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106784" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106783">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea7884a87d.mp4?token=D_S7uqCNdzh1yEZCuC154cECRxmy5nowClT0eq9I9ExcP-dmP9QcfqZRDtiTuCdf6XelY549KEdiKs8dV0DsM7ukJVP8URwyvRitJA2zfDMKasPETB4rK3ofkLqM_gh2934Bp9HzWwST3lAjlOdlIc2jQTowk_p70vFeMcYMlAkVH6P6FbpK8UNUVNovPUgwVhGhyohjXh5aGXhC86cU2u1iZ6b3ML4dMjduQiTvtwleUfrGsAE3ym-S4Mg4Li07Iks0j76pS1ZFXJQ5QnPNf9NVWfU28n_-aiZUAViWGN3QDtlUB8sjVS5FzcHduPINPgVAC_MgCoE4VtG_Yb-0ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea7884a87d.mp4?token=D_S7uqCNdzh1yEZCuC154cECRxmy5nowClT0eq9I9ExcP-dmP9QcfqZRDtiTuCdf6XelY549KEdiKs8dV0DsM7ukJVP8URwyvRitJA2zfDMKasPETB4rK3ofkLqM_gh2934Bp9HzWwST3lAjlOdlIc2jQTowk_p70vFeMcYMlAkVH6P6FbpK8UNUVNovPUgwVhGhyohjXh5aGXhC86cU2u1iZ6b3ML4dMjduQiTvtwleUfrGsAE3ym-S4Mg4Li07Iks0j76pS1ZFXJQ5QnPNf9NVWfU28n_-aiZUAViWGN3QDtlUB8sjVS5FzcHduPINPgVAC_MgCoE4VtG_Yb-0ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
ادعای هومن افاضلی: ایران در آمریکا از ورزشگاه آزادی هم محبوب تر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106783" target="_blank">📅 00:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106782">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCvd4iFw8Eii8lVqQK3qPh2179_4KftOz_4S5LcvyLRZKDIoxZV5u4-9kzg98lhgAvJ-YoQFpBfPaWuAZKig2umEIgiNpEwaE85jFta_obabk1nbi383QDDl8pGSBdsNdJF_T2COFpc3ubWHhbbO2chgOLOJEek-g7tuUZVc40kZS28Mfhizzz1sTa_hoH0CnI77zgNKFIV8mr1jze0jVZtMJBcD8xH_pbpKXr_BH8Jc2UCH8VJMWlM5CMFqSgpSpqzKCcEFuDMxtHnYQwWxVu3-1V1QIUpjTR7bdkymzivbdGIokI2Zo91mVAvVt8wmyNsefXor6qkTgs-ywNVRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام‌اتحادیه انگلیس؛ سیتیزن‌ها در یک بازی درخشان و با گل‌های بازیکنان ذخیره خود مقابل نوریچ پیروز شدند
منچسترسیتی
😄
-
😏
نوریچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106782" target="_blank">📅 23:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106781">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UASHGEzCGUpAaaYlFe0psOKnCE_fd7wFjuUW4-tuZjIf7xHTe4l7nIl5q3UssffQs71E7ew9himvR0duetsikUSwMbZxyPDYPucsi7ulGTdHRpDWJojA42ah3-3XbZwVluare8s9FSI3JTYekQ_KcFm8GzOuQtg_W8NUp5fFNHJLDozb6mZawWEPA3fscrXPuR3I7qd_e9g0fYAwd1jZVfIbNHDkLfnFd0wwpUrf4Gd1SkcRhB_fC7n6zfXchGlqvaXhdtcjb25YMIjZ5Uh-wWqzrEJxMLh6Vds8rHrS7IujPYfFNXXflJhJLxq8fPAr4h1iuMyWs9lJNzJlal065A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وقتی لیونل مسی در سال ۲۰۲۳ به اینتر میامی پیوست، این تیم در قعر کنفرانس شرق MLS قرار داشت و تا اون لحظه هیچ جام رسمی‌ای در تاریخش نگرفته بود.
✅
مسی پس از ۱۱۵ بازی، به ۱۰۰ گل با پیراهن اینتر میامی رسید و این تیم را به چهارمین جام تاریخش از زمان حضور خودش رساند.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106781" target="_blank">📅 23:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106780">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af53c1869.mp4?token=o7sxpVOJjd4b1dPpdVq8Z3KDS_Gzi2kao0YHnmV5aPwFIsRsCw_jEbk5KN0uFrhzVWpkA4FmOLw7QUIFxAGFjeiiM4ESVL5zNO55jsEjbSPw8Tby5QIFoodyeHV_8ase0rc6eHyqof6fkbNFBsyNWOEWRqAfhQaWheU5ifymLYRfZ7-rB21wkzl11yo5zoMEg0KfMBjVSBom-BEGEqnXtirEwkoFqHOPpz248RE4DvqwSMCn0_orVOzorl03YG50C6EGW04f7sA__L0grjRiCoWitDAKN3PuG7FfXm0Ag1W5L8WCe4557luMIWFyU9jWr3t5o-TOCZAzfBmXRn50-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af53c1869.mp4?token=o7sxpVOJjd4b1dPpdVq8Z3KDS_Gzi2kao0YHnmV5aPwFIsRsCw_jEbk5KN0uFrhzVWpkA4FmOLw7QUIFxAGFjeiiM4ESVL5zNO55jsEjbSPw8Tby5QIFoodyeHV_8ase0rc6eHyqof6fkbNFBsyNWOEWRqAfhQaWheU5ifymLYRfZ7-rB21wkzl11yo5zoMEg0KfMBjVSBom-BEGEqnXtirEwkoFqHOPpz248RE4DvqwSMCn0_orVOzorl03YG50C6EGW04f7sA__L0grjRiCoWitDAKN3PuG7FfXm0Ag1W5L8WCe4557luMIWFyU9jWr3t5o-TOCZAzfBmXRn50-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🟡
دفاع قاطعانه بیگ‌آنز پوستکوگلو از رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106780" target="_blank">📅 22:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106779">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAKxDGPu_Vxt5ACghAvEoDOsDcKPyAjzcV1uWxic9Koz4tTnsFbRZ48ZjFXVvvwjFLP_MFD0LqXUVxrXJKUrTIHjWWjwsRraI9jrNdzur-veoIWcuZUL6RR0PeppXUADyylGVZCZ7th55klNg-0SImeeCXf8Z6B_JMco2fv2aU0EdmdMj-l-IIp4Sp62iSeCbMBFWFkT_SJd0MlvUjVsSNkONst_VQMWtjI_uFBRMjTFh-mHPr1GEJFCCZ7KrfvbgKeSH4sv8EWkIjvzmMxI-6xwiyfH95j1jLjOdQHNYetI-8ou2S5MlXYS9tb3rZmmWg4THF_znsGlio-nkMY1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه اسطوره مسی و رونالدو در سال ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106779" target="_blank">📅 22:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106778">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQNoQ92ispXmUcxw8bW3XvlBWpIOjvAwjtBall-BSO_5MsgpDUDbO5JsTS2c_UvUPNx_rYw6Ga-aeU_Ca73PuFwY4haN2t9_lN9NRIFzg-A6gvt539u6QVY1pHkAfkwtddWf6woxrdxlkSsErsJdcnwVdpsBCL-gP2wU4SUyXOlIpSL0tkLESBPZUj7YZ18HIrPJZrioYSeYlCVXUuBSgQXT9m5rHdj7x0qn8l-XjBaIsqqYKAnPhB89qEAbmkDj3oCR8aARh_sHA1W9WhApjZnKw0X3z5X4G0-kv5pQ7Fk06aOsmFNItrjxbWk6u0lZ-6NgsK6dKLwKxRPJqykvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✅
⚽️
هفته اول لیگ اروپا؛ ترکیب لخ‌پوزنان مقابل کریستال پالاس با حضور الهیار صیادمنش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106778" target="_blank">📅 21:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106777">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
🇮🇷
🎙
صحبت‌های جالب نوید استادرحیمی درباره عملکرد درخشان یاسر‌آسانی در استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106777" target="_blank">📅 21:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106776">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGCFJjbPJ6aQ1Prl2LAyE51dqJTQqihI6uXJTqGCvrD45mYYHliwt1CC2pJG5K6yerkzSzYWVc0jhl3vhzXDJTaN2vw10K_4_yt5eWjIjkd7EXCXpIcl_islerYN0aNR9Wf6huGeAAXHdukEshlqV2BD79Pc70AjPC95MuOj6Afkec5ZxgseFVZnl1aKIjQMdqoupjhbnKtQsp7EzWKXDPWlnYwgtcOsGH85mUu-SptXaJ5iLSk_J0F-y4Z2EVtp2RSXoA2krN9vuPSMGHCI-J-j2ImG7nWRZe_IZE_3bAXzkUQV2zvzXam7rUYj48htwF_cyRV0BjufXGaUHvYsww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام اتحادیه انگلیس؛ ترکیب منچسترسیتی برابر نوریچ؛ ساعت 22:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106776" target="_blank">📅 20:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106775">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8c416616.mp4?token=Wnt6jY1GLSKPMmtVtqhTbPucnLH5gSK1WVP_dlaBT4ts6ZjfjCQxOE84SNKnBv7E_r5hEse_6Zt9d-sxb28L-FEnOY9atHGhOlgQP9l4-c5aPZdv7bHf7ghWubwOeXzAiXVkY7pc6p6xLA0WvYUpq7zStx7a3ZVATkNAZsh04a3foDudzxSu71whMbjbtS1DxhoaJ5uWdLwFqyTAV9bcmps5hfQ9pRQSkp2WHNjKyDGZ2hFxrmB9lYQ0HPa68uaQanMnsdz0UuBsXDUNSMuWaCCS2uYjuf_KXy-4iIVCEe6vYA4DuoLxYtqnQxJ_D_xUe253LVSEl1_ph1tBsF0seG8QTWleXQTvBfad-q635b8uhHBePx63cAEL7iKGOsq5XmNO_BcgAn7Ne_MvRYfE3Srtgj8oCawhCnZH_sJaIMsulJd3wnLkxaipMYsBXtQxO1HTbURtWfK7I8pBiNUgDON8sQE7DOyxMi6ofnPb2GX7W0YqaUDDXearB2j5KWnS99zoWRxfgRUk73rmfOTBXvWzx06H2RnqKhoo0kRTr3_UhCy7p_bTXoM_vO3LSBXwjrDk9BswFLtjJAe3Wbm5l5z-tVR60ooumBLFMHvTFtOMMQ_jjSad7RVOGKMIwcFyguijimmgelfV-Bngsi1QLmW9uD4LCSV09Rf-4nfyA5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8c416616.mp4?token=Wnt6jY1GLSKPMmtVtqhTbPucnLH5gSK1WVP_dlaBT4ts6ZjfjCQxOE84SNKnBv7E_r5hEse_6Zt9d-sxb28L-FEnOY9atHGhOlgQP9l4-c5aPZdv7bHf7ghWubwOeXzAiXVkY7pc6p6xLA0WvYUpq7zStx7a3ZVATkNAZsh04a3foDudzxSu71whMbjbtS1DxhoaJ5uWdLwFqyTAV9bcmps5hfQ9pRQSkp2WHNjKyDGZ2hFxrmB9lYQ0HPa68uaQanMnsdz0UuBsXDUNSMuWaCCS2uYjuf_KXy-4iIVCEe6vYA4DuoLxYtqnQxJ_D_xUe253LVSEl1_ph1tBsF0seG8QTWleXQTvBfad-q635b8uhHBePx63cAEL7iKGOsq5XmNO_BcgAn7Ne_MvRYfE3Srtgj8oCawhCnZH_sJaIMsulJd3wnLkxaipMYsBXtQxO1HTbURtWfK7I8pBiNUgDON8sQE7DOyxMi6ofnPb2GX7W0YqaUDDXearB2j5KWnS99zoWRxfgRUk73rmfOTBXvWzx06H2RnqKhoo0kRTr3_UhCy7p_bTXoM_vO3LSBXwjrDk9BswFLtjJAe3Wbm5l5z-tVR60ooumBLFMHvTFtOMMQ_jjSad7RVOGKMIwcFyguijimmgelfV-Bngsi1QLmW9uD4LCSV09Rf-4nfyA5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
توضیحات فرشید اسماعیلی درباره چیپ معروف در دربی تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106775" target="_blank">📅 20:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106774">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d822ce6be.mp4?token=Z5ffx4CFHilmDOIzfa-9sCwj3fkf9t4dcVMLEh1UShbU42K8vfTAKrNNG_tTJG42ntk7zcZg4NZesN4MOkcb39z1eaQzotAVmTXUJRa1oP7P_Gcbb-hYXYmjp3Hq3Vm7MAv9AJFenf_jgk4FpRZj10qbVhArtycVd0GgNDfV-O_ttApKut2epCs8_s0DMRg2hCNRn074_F6DMVhA1ikpZ4jEWzsA_jMnn8exipdBBZ2BClRIzGIWojw5LzEW-LRT125bidohUG4WnsD4qI0gFniLkgTmGcKLaiQdx7mK-RRajhA_25d8z2hYZKm0-swvH50fviENM-5JI8tGBVmgcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d822ce6be.mp4?token=Z5ffx4CFHilmDOIzfa-9sCwj3fkf9t4dcVMLEh1UShbU42K8vfTAKrNNG_tTJG42ntk7zcZg4NZesN4MOkcb39z1eaQzotAVmTXUJRa1oP7P_Gcbb-hYXYmjp3Hq3Vm7MAv9AJFenf_jgk4FpRZj10qbVhArtycVd0GgNDfV-O_ttApKut2epCs8_s0DMRg2hCNRn074_F6DMVhA1ikpZ4jEWzsA_jMnn8exipdBBZ2BClRIzGIWojw5LzEW-LRT125bidohUG4WnsD4qI0gFniLkgTmGcKLaiQdx7mK-RRajhA_25d8z2hYZKm0-swvH50fviENM-5JI8tGBVmgcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز خوبه قبل گفتن یه ببخشید گفت
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106774" target="_blank">📅 20:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106772">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6b91a252.mp4?token=pevxRj5g7Mtw3RFlpfRs8HDa2XMynv-e9-k28GEy_y_5GNFzs9WFtB2SX2vQpMSBo-34-wmIUf8R7_LLFfZQVYw1Ax1weL3zXlhlLgGcQgRjazcwNLVrnWB2N3UilUCNz5jN8dDun8WxKy-5SQorUOsJtqYAIdP1Y4TF3rhPVC4YHWTjKQkSud_4iVKI_-QEJiaS6O-aE3by6kgqBNVI3IvwQOKc3OMZAgEJEUtoxyNIWofwhBBv0Z3XMGclz81lLKYiYO0FHGoFoJDzbsKOUYqJv7oPzFylKQ5Q93-O1QVUMd3zOOTrekoRuL5b688glriKMCbjRfLywwtgkiLIYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6b91a252.mp4?token=pevxRj5g7Mtw3RFlpfRs8HDa2XMynv-e9-k28GEy_y_5GNFzs9WFtB2SX2vQpMSBo-34-wmIUf8R7_LLFfZQVYw1Ax1weL3zXlhlLgGcQgRjazcwNLVrnWB2N3UilUCNz5jN8dDun8WxKy-5SQorUOsJtqYAIdP1Y4TF3rhPVC4YHWTjKQkSud_4iVKI_-QEJiaS6O-aE3by6kgqBNVI3IvwQOKc3OMZAgEJEUtoxyNIWofwhBBv0Z3XMGclz81lLKYiYO0FHGoFoJDzbsKOUYqJv7oPzFylKQ5Q93-O1QVUMd3zOOTrekoRuL5b688glriKMCbjRfLywwtgkiLIYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
یه خونواده ایرانی عروسی گرفتن، بعد اسنوپ داگ رو به عنوان خواننده آوردن
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106772" target="_blank">📅 19:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106771">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd7aec7c83.mp4?token=HqFPARvlnMNrugE_yNCo2VGCBr67i_z-rDx94EoGM06QIBiDFBkS_K4nsGmx-ulOFW9Pbmte6yOTVWt__gXTz5JwYKUFjowXZ9Sw0PIrMb_jTTERdiFpcaHVu3uBFL0A0aE4GgM2NVKN-esEeqXxPkFwhyvt5vXYjxrvASGbDo4-Ok6_t8PY-ASsw9CesrHV_sbkKOq2wRrtxECgM748vGWjaWLxNX7HgnfRsbO_xfplS3nYPbtIg9fen5Fdk4t5586TE-d_MSRYAPHU7KWsmJG6uhrL4mx_VXY_gyBevjOJy_y7IhmPEOEpyld2CweQaGIg5CrUYvB9L0klKMyrg7a9jq-6M4Ak83e5IyhYcHlEw7J5DvZjFCGCDF1QizudfF-B0HP85ngfTDwfln9lZ0ocYxcFjCKTTMKcoL_b3hyGN1bYOj_EhuO732Rlw9FjuqoVUzhU5r44HdoVvjIecuT6lVCTCwEsNru6Lz1xaezdxUcFTpJrY7zGR5MUhE2shMJ-uuhAVcFRMd_lxWtWg90Rds_YxK85v-367uq0W4uwlj7rpoQC6SDCE2PZDyu9_gHnyGCmDp7s-N-VIacLngKf1S3wUJwrKItMMlTtJGiiouIHcljLlpkmEsrQ694YnxXVkPgrW_K8sU1deOo0Si_PYKTaWDC9CBB-6vrftvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd7aec7c83.mp4?token=HqFPARvlnMNrugE_yNCo2VGCBr67i_z-rDx94EoGM06QIBiDFBkS_K4nsGmx-ulOFW9Pbmte6yOTVWt__gXTz5JwYKUFjowXZ9Sw0PIrMb_jTTERdiFpcaHVu3uBFL0A0aE4GgM2NVKN-esEeqXxPkFwhyvt5vXYjxrvASGbDo4-Ok6_t8PY-ASsw9CesrHV_sbkKOq2wRrtxECgM748vGWjaWLxNX7HgnfRsbO_xfplS3nYPbtIg9fen5Fdk4t5586TE-d_MSRYAPHU7KWsmJG6uhrL4mx_VXY_gyBevjOJy_y7IhmPEOEpyld2CweQaGIg5CrUYvB9L0klKMyrg7a9jq-6M4Ak83e5IyhYcHlEw7J5DvZjFCGCDF1QizudfF-B0HP85ngfTDwfln9lZ0ocYxcFjCKTTMKcoL_b3hyGN1bYOj_EhuO732Rlw9FjuqoVUzhU5r44HdoVvjIecuT6lVCTCwEsNru6Lz1xaezdxUcFTpJrY7zGR5MUhE2shMJ-uuhAVcFRMd_lxWtWg90Rds_YxK85v-367uq0W4uwlj7rpoQC6SDCE2PZDyu9_gHnyGCmDp7s-N-VIacLngKf1S3wUJwrKItMMlTtJGiiouIHcljLlpkmEsrQ694YnxXVkPgrW_K8sU1deOo0Si_PYKTaWDC9CBB-6vrftvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇮🇷
۸ سال پیش در چنین روزی، کامبک پرسپولیس مقابل الدحیل. اون دوران الدحیل تو ۵۱ بازی فقط یک باخت داشت که اونم جلو پرسپولیس برانکو بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106771" target="_blank">📅 19:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106770">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5345b9e16.mp4?token=Q3XM9ne8mq_wV0RcC3qXVeF-7A6AoMOCic1cEHhV8XvSaGaNHgG9AwrkFrQ9xBg5QQSPyN_I0LyZ0o4UabcQ2b4b9psmbLzdImca-Cjazohd0Ur8R4CxHqMcLnGelBGbGlWrGY_LHW3Frla-NId-_olrassX5YoIM6vI0V1HE99W85hwr7xEiLyF2QUU6clLCGk2sEwYTFemFF07ILFDiTJ4HtbfDCWo1Fk7IOt0P8Q1eURnUkOKNhvg5LZ4YUlk_Mtll82Z8DT0u4DKC597fp-YyNGxjG2dYvWZ5FnsK5WfrXcG8hxSkiajLIf9b_lAwRkFs7BYXapo50Jv69W4nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5345b9e16.mp4?token=Q3XM9ne8mq_wV0RcC3qXVeF-7A6AoMOCic1cEHhV8XvSaGaNHgG9AwrkFrQ9xBg5QQSPyN_I0LyZ0o4UabcQ2b4b9psmbLzdImca-Cjazohd0Ur8R4CxHqMcLnGelBGbGlWrGY_LHW3Frla-NId-_olrassX5YoIM6vI0V1HE99W85hwr7xEiLyF2QUU6clLCGk2sEwYTFemFF07ILFDiTJ4HtbfDCWo1Fk7IOt0P8Q1eURnUkOKNhvg5LZ4YUlk_Mtll82Z8DT0u4DKC597fp-YyNGxjG2dYvWZ5FnsK5WfrXcG8hxSkiajLIf9b_lAwRkFs7BYXapo50Jv69W4nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایانِ عصر خامس رودریگز در تیم‌ملی کلمبیا.
💔
🇨🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106770" target="_blank">📅 18:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106769">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9692b0808.mp4?token=lPOiBel2WAHa6LpGHP3h0VHymox0j478ZuVt1EJ1424yXXMZ40YqF2-exGKEIhjOQbxuAkTlPPuDoRuU276h7jqcPLvKIgEDo_Nl1i-bBR0IgB3DbBxMUzLEjUbYxV9J6TGRBDZKHHRPfPZnSTcHJUaD_Sqx4P6c37BH4GrOAyQ4d2y-KIey1aR0DM1xAjHxZd-HD-3olr-x4DbMEp9QlMBN6Jj3oeovAko_hrv8XnQ3BmSlDSY-JpR2Ve-3Qkwsge-_SjWbsPjaPkHk6BEEuPJ2BDdfngV27USnwxdGAj0FyndTteb2VrzRhRkd2fgIMZXSmij9UM3GyBJaesWScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9692b0808.mp4?token=lPOiBel2WAHa6LpGHP3h0VHymox0j478ZuVt1EJ1424yXXMZ40YqF2-exGKEIhjOQbxuAkTlPPuDoRuU276h7jqcPLvKIgEDo_Nl1i-bBR0IgB3DbBxMUzLEjUbYxV9J6TGRBDZKHHRPfPZnSTcHJUaD_Sqx4P6c37BH4GrOAyQ4d2y-KIey1aR0DM1xAjHxZd-HD-3olr-x4DbMEp9QlMBN6Jj3oeovAko_hrv8XnQ3BmSlDSY-JpR2Ve-3Qkwsge-_SjWbsPjaPkHk6BEEuPJ2BDdfngV27USnwxdGAj0FyndTteb2VrzRhRkd2fgIMZXSmij9UM3GyBJaesWScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
بابک‌مرادی بازیکن سابق استقلال: ذهن فرهاد مجیدی را خراب کردند؛ خیلی آدم خوبیه اما یه دستیار مرموز و بی‌شرف در استقلال داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106769" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106768">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTc1m38lIfsxFfTqHs6TKODTM3QZXgaQFrNFj74q3TLVNOEsX3SQIOSrK-eGqR7U3r7EmVDblqrXL5nN4b0sHaRSWEn6wVpQAZ_aKlUkCFTNTgUD1rg6fnqyB3eDm_2Znlew04lUg5DG9bBUGW47bmFN-O-G-FCMZjm9o_UPTq8FPhYHhx14Plb77m_CL9MLSJ5HExXMIaSFI0lOCZPWjX6cshY2pNtAqey2Z0Jm7NJ5_UgcGC4GdwHaAxtbSCExYe_djnsvRcINocms-rn-GtjQLW0HO4DvLFXR6Q0naWxTgjlUoOJi58WQPQoWBoJCBIdn5T9h2h-Ujgpk1orgVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
برنامه سوپرجام اسپانیا 2027 اعلام شد
نیمه‌نهایی اول
🇪🇸
بارسلونا_ اتلتیکومادرید
🇪🇸
⚽️
13 بهمن 1405
⏰
ساعت 23:30 به وقت ایران
نیمه‌نهایی دوم
🇪🇸
رئال سوسیداد _ رئال مادرید
🇪🇸
⚽️
14 بهمن 1405
⏰
ساعت 23:30 به وقت ایران
🇪🇸
فینال سوپرجام اسپانیا
⚽️
17 بهمن 1405
⏰
ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106768" target="_blank">📅 17:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106767">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8b49aaa0.mp4?token=loEBkkfMfcJ7MLVB4cdRdr940cfDAlmWdRZ-cWKwIAlt_kTh366jYhdLJCSCedhiBxm7X3qJ4ddVnRBxFkIRptruQk5XTYN-EK7KOugve6sMoxPRvEvNbuRCyqtdoQTAJF7J0rMbWlL-4AOLemMygs38hQ_inN7rQyuKnoYT7aGmgdzcLq1D3cqYhS3gZxn1Rrun9X0ASaW-j9fR2_EiMzwsDCqI53YcOJgheOMdgQfVW88L38JlqzkGCZiwr7TeAO4IZXikJDsmL_c0lUg3DiiGciOtF0qZPDKItRlPnY9L54K4JREi5uWiLEz2SiDT9WQ5UndrrVX7ZMS_7PrC1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8b49aaa0.mp4?token=loEBkkfMfcJ7MLVB4cdRdr940cfDAlmWdRZ-cWKwIAlt_kTh366jYhdLJCSCedhiBxm7X3qJ4ddVnRBxFkIRptruQk5XTYN-EK7KOugve6sMoxPRvEvNbuRCyqtdoQTAJF7J0rMbWlL-4AOLemMygs38hQ_inN7rQyuKnoYT7aGmgdzcLq1D3cqYhS3gZxn1Rrun9X0ASaW-j9fR2_EiMzwsDCqI53YcOJgheOMdgQfVW88L38JlqzkGCZiwr7TeAO4IZXikJDsmL_c0lUg3DiiGciOtF0qZPDKItRlPnY9L54K4JREi5uWiLEz2SiDT9WQ5UndrrVX7ZMS_7PrC1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
انتقاد جالب میثاقی به زمان‌بندی ارائه‌شده از سوی سازمان‌لیگ‌برای هفته‌های آتی لیگ‌برتر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106767" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106764">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acdc40365b.mp4?token=Wkjmy1uP1N3WP9fHWfqAa_Zr2xyYUT_hJFjwTuNgM5LUxPMyBfHGMeQsfa5tB-rL-nswRbICvO05RP1cFFML0XGP2gBZq9DtXkgA6RY7fBO8mz5BUV5QUqCQQs3EWqIZa5fyG03iIMJ2PG-LKxnYh7wOIhV_yhI_Nb7C_7E95jheRdx8HbjzUdu_UhNxASnAQxeZIY73NQv85gbs5hKNiL-o4Lgu2zLGZVBubCQVZR0apVg98a03uRz5uI1CNxnhfF2tjc6XSQkhAWBw0NER8QTr00_jKqwdslvTHI6b3Xo4aEepzQ5T_lJHlh33utaNmfZYtnyORcLl7PLrIYHnjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acdc40365b.mp4?token=Wkjmy1uP1N3WP9fHWfqAa_Zr2xyYUT_hJFjwTuNgM5LUxPMyBfHGMeQsfa5tB-rL-nswRbICvO05RP1cFFML0XGP2gBZq9DtXkgA6RY7fBO8mz5BUV5QUqCQQs3EWqIZa5fyG03iIMJ2PG-LKxnYh7wOIhV_yhI_Nb7C_7E95jheRdx8HbjzUdu_UhNxASnAQxeZIY73NQv85gbs5hKNiL-o4Lgu2zLGZVBubCQVZR0apVg98a03uRz5uI1CNxnhfF2tjc6XSQkhAWBw0NER8QTr00_jKqwdslvTHI6b3Xo4aEepzQ5T_lJHlh33utaNmfZYtnyORcLl7PLrIYHnjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
واقعا چیشد که به اینجا رسیدیم که یه بازیکن فوتبال برای خودش آرزوی مرگ میکنه!
صحبت‌های تلخ بابک‌مرادی بازیکن سابق استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106764" target="_blank">📅 17:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106763">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFoR5F3fRu4aLSPtqS2DiPHEE0S19VACsCkla8hb7wDvOrn1rIBDzXgrRALOlVS-i3acAFPkzHwyKiDxECO768Cs1ZPq6zDbrg92OFBtw0uqlWV9gZqb5rGZeIdyr0nWT8KY-tSz0nmkQMum_XBlI-SD9CtoBCC8PJQn0Roku8d-hOA_mYuJQA_B56OCB4UYKgmIFvNpdJvc4Mi1WTv4CpLG9_m8RdoYprp8HlSVGnb-i1j6l2iXruxQAG1V5plUPpdOk2xGEBYDUTkl2FmrjHHw_2gOem3nAKAKn-tl0_V4Uo_geDrUjxICANPfrqoQVu9DQ-d1z9bLCMBkBTeJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📊
🥶
کیلیان‌امباپه از زمان حضور در لالیگا به تمامی تیم‌های حاضر در این لیگ گلزنی کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106763" target="_blank">📅 16:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106762">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db11bb42ef.mp4?token=roTeb8lBzZtH7gtbVxmaeST0i4NLE4fKo-NE6eya5fQb4RtdEcgZrIAhvnYKJ_QexLdL_hedGsb8EP6cw1x2LIdoctVtWH4QmOEVEh9KifPR3zSqFVakk_pBePiPGt6IUINfE8y32Ql6DpoOnhKgvoTEirzSGbl7QuLVwkMPOKXrBWlg4hFBL5Y7INHqdwn6Le5eZhi-m8D0s6SZfz5KwnB2ILsTmIyaZ45KNmaehBgvU5aEkVD4vti5K2l16tsWSuHNxKjm1GF3jagku3429PouQmTNTipbn4uGa7O9qvQbDL-N_sSbeIs1TfhLmbca1FCiu6khjwM_FP_Nv8BfGD0BB5_emrcH85Ak10Kmwkklmc5kYk53SpL1-9sEBQsQlakVighnvQ4frMNHOA_TXbKfZO6qBgNXVWsVdoCcBq9mAzUJ_OScp_Ecxs-Q0E5PqD6t0GDWySonaXRE9ZnIPpHSEQsUL_aJ93kzdFO-E64MbZSGSJqp5MfgMDm5Nxxm9fkmf2w9eLto3-m5pENJV6iOLETeImLEVzEgoKJe0XpwDPoS0XNLJ64DJXbzbpb1d2N9xEnmN6Qdse3n8nRxvVUsLjBFbIEI7irexQnHQOJ02oKv-_UNFyOo9nYJirKRwWL-9UZV7px3tPzZSjEnfHdtJE1WyhzrdbZlgHV8Ju8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db11bb42ef.mp4?token=roTeb8lBzZtH7gtbVxmaeST0i4NLE4fKo-NE6eya5fQb4RtdEcgZrIAhvnYKJ_QexLdL_hedGsb8EP6cw1x2LIdoctVtWH4QmOEVEh9KifPR3zSqFVakk_pBePiPGt6IUINfE8y32Ql6DpoOnhKgvoTEirzSGbl7QuLVwkMPOKXrBWlg4hFBL5Y7INHqdwn6Le5eZhi-m8D0s6SZfz5KwnB2ILsTmIyaZ45KNmaehBgvU5aEkVD4vti5K2l16tsWSuHNxKjm1GF3jagku3429PouQmTNTipbn4uGa7O9qvQbDL-N_sSbeIs1TfhLmbca1FCiu6khjwM_FP_Nv8BfGD0BB5_emrcH85Ak10Kmwkklmc5kYk53SpL1-9sEBQsQlakVighnvQ4frMNHOA_TXbKfZO6qBgNXVWsVdoCcBq9mAzUJ_OScp_Ecxs-Q0E5PqD6t0GDWySonaXRE9ZnIPpHSEQsUL_aJ93kzdFO-E64MbZSGSJqp5MfgMDm5Nxxm9fkmf2w9eLto3-m5pENJV6iOLETeImLEVzEgoKJe0XpwDPoS0XNLJ64DJXbzbpb1d2N9xEnmN6Qdse3n8nRxvVUsLjBFbIEI7irexQnHQOJ02oKv-_UNFyOo9nYJirKRwWL-9UZV7px3tPzZSjEnfHdtJE1WyhzrdbZlgHV8Ju8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎙
رست‌دیفنس در فوتبال از زبان رسول‌ مجیدی از معدود مجریان باسواد صداوسیما؛ خیلی جالب و شنیدنی برای عاشقان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106762" target="_blank">📅 16:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106761">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106761" target="_blank">📅 16:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106760">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915324d20d.mp4?token=J9HikILXa3qw4XR43l3PpcpdZ2i99bxffnJHXZ5NIWsRhrPpmTPAoIC7RfRU2r_Png1iC2fUbS82C7VQPqtTHKV9-K-d2CLy6SRrmrBlPL28jwscvA0YqB22xPKy53oxlK8YkJcQXKt4nrsoxodcjGpZwKbso2f1butNHiyG_buq0uoOGyRTIqDRa3x2Vwq8cAH0hzFsU6F8kRaFe4JR8BCWcCuFprxlibCJ6Tda07kxtxevNul4f5jLwugmv55XQOgZfKnyLq4Vz4EX1xlDLeFOvslpMLIpJcb1j-aBQi9VhbC6RVlsD5LQMBKuabPJJOt0JXk3fx670YrhKEG9hbKYj700fPTptbg5PcGoAgnKec7xr3cN47yg8sVB7vWKZZtcRUx9-hNeBy0sxi1hGCtKkJXH0u7OzW-zoENniyQXOmn68TTHCz_s5NksY01e5HsNDIbMTmeW6uX7MpVNze2DQrds2-zJi9sxhbYJWUNDpPQeuj77Q6lbUGTQM_UxXltf-3MGIj-sA-rK-aNKFsw6lU-jpvieL6Sq32y1S-8rQaJITdXgx4p2OhJ6K_7LznS8K6PnLY2a0x_UDL3ipv0cay3qmCX10KhbPR4elhFBP19OZhn7tGvQoV2L9I5LP0Z-Luo3x4LLw_t4EMcO7LINvfsPfDthnjqsreGnoec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915324d20d.mp4?token=J9HikILXa3qw4XR43l3PpcpdZ2i99bxffnJHXZ5NIWsRhrPpmTPAoIC7RfRU2r_Png1iC2fUbS82C7VQPqtTHKV9-K-d2CLy6SRrmrBlPL28jwscvA0YqB22xPKy53oxlK8YkJcQXKt4nrsoxodcjGpZwKbso2f1butNHiyG_buq0uoOGyRTIqDRa3x2Vwq8cAH0hzFsU6F8kRaFe4JR8BCWcCuFprxlibCJ6Tda07kxtxevNul4f5jLwugmv55XQOgZfKnyLq4Vz4EX1xlDLeFOvslpMLIpJcb1j-aBQi9VhbC6RVlsD5LQMBKuabPJJOt0JXk3fx670YrhKEG9hbKYj700fPTptbg5PcGoAgnKec7xr3cN47yg8sVB7vWKZZtcRUx9-hNeBy0sxi1hGCtKkJXH0u7OzW-zoENniyQXOmn68TTHCz_s5NksY01e5HsNDIbMTmeW6uX7MpVNze2DQrds2-zJi9sxhbYJWUNDpPQeuj77Q6lbUGTQM_UxXltf-3MGIj-sA-rK-aNKFsw6lU-jpvieL6Sq32y1S-8rQaJITdXgx4p2OhJ6K_7LznS8K6PnLY2a0x_UDL3ipv0cay3qmCX10KhbPR4elhFBP19OZhn7tGvQoV2L9I5LP0Z-Luo3x4LLw_t4EMcO7LINvfsPfDthnjqsreGnoec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برخی از راکت‌های تماشایی سوبوسلای در لیورپول؛ واقعا عجب گل‌هایی زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106760" target="_blank">📅 16:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106759">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMXiSW8qcz6ymEmkFO9ig7PmYXqzBhK1ge28FOcuEGZjmE5K06sKFs0MyYU6RB3Qq4-fUvWXAmsdeddZlyGEtD3aljKvghukgTJiTDguHQedlx_AMDz9DilhTW54Y_1AKWfoH0pKfbIEs0CGqwMOvEJu0AIOLfMnbNgwry-rISn8qqjJwNU7i4-pQWSZREkXa8Smgz64cMSPCj6weSlWvc_DQ8I6UvMbdbfsJm4JMccmcN0bL53RDIDWM3z2jGvpz6pp7iznUxRaad82zvh2DjliAThtBCA9ap4qh5kL7kzpjh99qU3BuryTS7I1OS4OlH5xvC3KRbmQMOcle7InJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
سال 2018 که فرانسه قهرمان جام جهانی شد، کل مردم فرانسه برای امباپه دعای خیر کردن و نتیجه دعاهاشون شد این بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106759" target="_blank">📅 15:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106758">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab14c70f7.mp4?token=rM61BIihbwVDycwijXK9KCBaaOqAZ8-Y1bfANDy84eCSfQVLsgWHe_JGHjbpjpYsEzo7msG9wiQn0SIPezyzJFUQx0r_E7ELdCjH6SQtg4USh6agBmU1TnSNxz2ZjjJ_DIgF4xqG2FGCxGqugOQDiGQwJF-aa1jadTaxIxKc6MeoTwG3r62WisO6eikoyTkixIEQh4QFBQEcDd1K8vUXCDEc6vk-6pls2OXQqsa6V3TR-_3bphOqTkAag1tL_jUrjsGooZjsK6m3lrQWYFTVw4Sc-Af-AfVeBb7MTSHgulyu7L_eaUbDYj0HNZVh04CUdLRBSOyvfPqux8tw91G6aCWWuFigoDtduz93jUM3CqKPc1o6zHe4WH5aWctJAhFyEPbaaWJ__LVk3bFSnac2GEGUSuZocNVC8Kdykr9bJB63HfTQ46pie90Nc9_cPR70GkQbygrOvib-Oo1fZXAxoGOxtvkGgb3enIhvgeLX9uDpfXrNNRcFVtluwn4caotrtuH3B_KudupUV_YAYhRf3BlWxQWAUfR6rWyxFCe83k2QqMO7BDigz3qLB75IzfcswRNl0wp93cbsOG8POlrcbiM62uy-UfN85gN-XKHv3DhrXhBOza5Flsxghy5sQ91pkTbC4xiybdEOZmLwaJMpnuLG-n94nhWBfKrcylbvE3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab14c70f7.mp4?token=rM61BIihbwVDycwijXK9KCBaaOqAZ8-Y1bfANDy84eCSfQVLsgWHe_JGHjbpjpYsEzo7msG9wiQn0SIPezyzJFUQx0r_E7ELdCjH6SQtg4USh6agBmU1TnSNxz2ZjjJ_DIgF4xqG2FGCxGqugOQDiGQwJF-aa1jadTaxIxKc6MeoTwG3r62WisO6eikoyTkixIEQh4QFBQEcDd1K8vUXCDEc6vk-6pls2OXQqsa6V3TR-_3bphOqTkAag1tL_jUrjsGooZjsK6m3lrQWYFTVw4Sc-Af-AfVeBb7MTSHgulyu7L_eaUbDYj0HNZVh04CUdLRBSOyvfPqux8tw91G6aCWWuFigoDtduz93jUM3CqKPc1o6zHe4WH5aWctJAhFyEPbaaWJ__LVk3bFSnac2GEGUSuZocNVC8Kdykr9bJB63HfTQ46pie90Nc9_cPR70GkQbygrOvib-Oo1fZXAxoGOxtvkGgb3enIhvgeLX9uDpfXrNNRcFVtluwn4caotrtuH3B_KudupUV_YAYhRf3BlWxQWAUfR6rWyxFCe83k2QqMO7BDigz3qLB75IzfcswRNl0wp93cbsOG8POlrcbiM62uy-UfN85gN-XKHv3DhrXhBOza5Flsxghy5sQ91pkTbC4xiybdEOZmLwaJMpnuLG-n94nhWBfKrcylbvE3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🚀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپر گل پریشب سوبوسلای به تاتنهام رو از این زاویه باشگاه لیورپول ببینید
🤌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106758" target="_blank">📅 15:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106757">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbzHElclAzt1PKWGfNJuFla2r-gXpzux8Zuks1K1T1699WtiVIvopSy2OvUI4P1z1IxBtn85L9nB7qOnnRP8jEcB2bQNWhy94p3rPRKJEbzABCLIENky2fzj1CJjJtt8iwOd8auqirwwu02CD7nJ8RduA5KPH5CFQIcPpCc4oltk2JeRPabjSRfzS9mjTv6bIWDGLzoX4wzZbm8nb8z8IVXZRf1kJAyDdSVxkly5SFVYLSUZ14uC29qVAsxq5FwoYAHgV89lLDSpSULVe-56L0MULhqx_OPNEycC9PwXhphlBunV4xtVUtAVQwgMtElw1tPLlyFW0iOYR5hZgrGRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🎙
کیلیان امباپه: "جایزه توپ طلایی؟
به نظر من، امسال زمان مناسبی برای من است تا این جایزه را ببرم.
بهترین کسی که از من دفاع می‌کند، پای من است.
هر چه که بگویم، مهم‌ترین چیز برای من این است که توپ طلایی دوباره به رئال مادرید برگردد. باید به سانتیاگو برنابئو، به هواداران مادرید، بازگردد تا شادی را به قلب همه آنها بازگرداند.
آنها بیشتر از هر کس دیگری، شایسته این هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106757" target="_blank">📅 14:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106756">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/758a2aee2e.mp4?token=bCT3wrfJqC-PM9RnwX-XMBNRREb4NoGWD3pAScrXIYWWZyPL17Wx8ACPnbiqOGfOmYJVza3nXhFaHtqhrVfmbBLn-MDsKkXLTWgv00DuZ99DeE6yBr76CWjVAU_wpSU7DjCa3PmNwE7AjNclid7fgYPCVY0_G-cH7ouYXyZdu9q54ccP4R58kK-QvA8s-fX-yX6Wff51aECcm0snuxEHlqM9LHxKAO0tcrZLnM37UFp1RN6bV69sK-OK_ClrRWHBAod3vh5TI9CDHUq29TyLbgwWUTSqfVd8ekW-bpolpZin1xJiFK7krokOOMdx-RArT6a6m1mB0bCE9MikE555hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/758a2aee2e.mp4?token=bCT3wrfJqC-PM9RnwX-XMBNRREb4NoGWD3pAScrXIYWWZyPL17Wx8ACPnbiqOGfOmYJVza3nXhFaHtqhrVfmbBLn-MDsKkXLTWgv00DuZ99DeE6yBr76CWjVAU_wpSU7DjCa3PmNwE7AjNclid7fgYPCVY0_G-cH7ouYXyZdu9q54ccP4R58kK-QvA8s-fX-yX6Wff51aECcm0snuxEHlqM9LHxKAO0tcrZLnM37UFp1RN6bV69sK-OK_ClrRWHBAod3vh5TI9CDHUq29TyLbgwWUTSqfVd8ekW-bpolpZin1xJiFK7krokOOMdx-RArT6a6m1mB0bCE9MikE555hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇮🇷
🇮🇷
مقایسه فالوورهای ده ستاره سرخابی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106756" target="_blank">📅 14:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106755">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVdDYMAbexFDCDjBpSA6CHIPIlX_NdeQaMp9YnT_JXHzF53AEtn6VL1KeYycRn5vcO_sJdog1TuuPgxA6v6sHAvhvlgP-TwrL32o34oKJkUE09SNF_latS0keuYN3XXvQR3WOK96ew6n9ILJ0SPt1Xl14ZSvby7YzHZ9AdWqZsGSGLuOkfU--cABS2GRDp78twcq9cLMi4shMmCpg1q9QV2XBJb5dskLEVPHPisM-n5zs5213hrc4VtZ58dDU9kwECq-VVwTt6bfsPjhEeX9ic8soT5oXTupMH-uWIKy4S10ulWX-fxtWvWN0mDKxRmOdERSBDxU-NscgIm1suE49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
شبنم‌علیخانی کاپیتان تیم‌ملی والیبال بانوان ایران به تیم استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106755" target="_blank">📅 13:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106754">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=acA3xbrbEKXsqk3NnrI9k_dZeOWKdUZQBbPrXgr4P9uzwBGZYvBR-hCoLFXzAARy2MKuJlNVNWhyCDWytCpnhrOOf83MyN48lk3ORPvRida6EVd1zwoNZLDrYKzsK6ozcbN60GXxAgGImvJoJp_YxUri8SHcZ-sUTIUiqWNWPBkzn5vXsSmImpKGOcM6ZBhUAp9z1Z2yIb6Pm7m5h6BcuUyix24ad6J4223ev90dKUPk6pMjgSlw-GEHwhandPRoS6NpJ6e4WNt-Z5XyZ1q90bEGjwQF1Ob-k2HdPLK5HIGSByMK3w2NnxdcEIr7Cy1ffyBMJeQT9xds6I5j8S7-Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=acA3xbrbEKXsqk3NnrI9k_dZeOWKdUZQBbPrXgr4P9uzwBGZYvBR-hCoLFXzAARy2MKuJlNVNWhyCDWytCpnhrOOf83MyN48lk3ORPvRida6EVd1zwoNZLDrYKzsK6ozcbN60GXxAgGImvJoJp_YxUri8SHcZ-sUTIUiqWNWPBkzn5vXsSmImpKGOcM6ZBhUAp9z1Z2yIb6Pm7m5h6BcuUyix24ad6J4223ev90dKUPk6pMjgSlw-GEHwhandPRoS6NpJ6e4WNt-Z5XyZ1q90bEGjwQF1Ob-k2HdPLK5HIGSByMK3w2NnxdcEIr7Cy1ffyBMJeQT9xds6I5j8S7-Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
حرکات عجیب مجری شبکه‌سه برای توضیح عملی دفع سنگ‌کلیه در برنامه زنده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106754" target="_blank">📅 13:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106753">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2975c02c1e.mp4?token=eiEGzKe0yMNoe8hgDy-1zuuVXND7yaBY8iQ9pCiRTAY4-jnPbo5X4237eOtTVxIINPKBhQ3WZpZKaHGn4sjXqMm48LyVX01TIG_sYnRacqJ4iRRQS0tTnL-XI3Vy4uJbGv8uRC5ClC3j8uyi610GZ8jktfplWu_8Bz_fkjfAFZoHVLWKCBqxy-bwxD1b9JVdZs0fnpYUeM6oOcbxU85j9YfIArbmXBlkkq3d1yiyLfIvB5WQbH9HwzoGrVq9OITCvIcrfMAk5WTqwStpyyokwOh7xC_93YKse3gxz0ozfNN5bUpgyZHb8ct1MiVyKP-786QIlbrKqkqsUmlifTqvBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2975c02c1e.mp4?token=eiEGzKe0yMNoe8hgDy-1zuuVXND7yaBY8iQ9pCiRTAY4-jnPbo5X4237eOtTVxIINPKBhQ3WZpZKaHGn4sjXqMm48LyVX01TIG_sYnRacqJ4iRRQS0tTnL-XI3Vy4uJbGv8uRC5ClC3j8uyi610GZ8jktfplWu_8Bz_fkjfAFZoHVLWKCBqxy-bwxD1b9JVdZs0fnpYUeM6oOcbxU85j9YfIArbmXBlkkq3d1yiyLfIvB5WQbH9HwzoGrVq9OITCvIcrfMAk5WTqwStpyyokwOh7xC_93YKse3gxz0ozfNN5bUpgyZHb8ct1MiVyKP-786QIlbrKqkqsUmlifTqvBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
▶️
✅
بهترین مکمل برای جایگزین کردن قهوه قبل از تمرین چیه؟ به روایت استاد هانی‌رامبد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106753" target="_blank">📅 13:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106752">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPqj8SwNGQ9SUbi40k1TlJJL0UiRNuaxhw63bdmboICQjOVSTzlYV_l_xXQd7DTsRDyPtjVqmtvvzcfGdUnrzKcv89GLyR2XSVslaySQXwfR1fSOTloHXEEAbgUu6EBm2Wh6ormFAJq4ZuscKBZ2PgFn-fnOqxmGGYagqVfh4FB6Zyw84JQHmr4_LAZMRk0sEDrCJzJ8j5CPl-BWRnX6JStSiaaTrCvq3DIkJswMVsUv69La7D4IR3hlbgPHYzBrI_nXBsSBfWtvBSkgbgfYOWdeZ1EdWVmBSWfGuPihs-62kFl5e0u3atgZrqBjAPMfGH5gGSVybt65z7lblJkE3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106752" target="_blank">📅 13:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106751">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpGUqXrKaC_tyCxVrVuVeMAe_sGC3OzLGedbrTKnp5h7CSPQfjyp9j8aAE_6kHDvXYUx3NF1JOCdoDn0f1nLSceMopffqY1XQcLGI2uPejVVQcrhrWb2WG0iRHBlGwUVkY_EiOnhsPrq6Ce3G4x97y4h2fQQeAZpOyY14yaqQ0doD5LdNSGtLimFuWw-sw3p25TI3EIrHIizPIiEK3794P_Fwf0tO-zYe6bulTOprBqwePvYJv52jZr9Un7eqo8U7lUpCPTwAEMEKfsRhnJrojZL6ILkY9bbJJS4W9JGS1zGBOAyAxWYn7n-IAjG5C8SiUzb_fwlAvi8ysF34iZfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106751" target="_blank">📅 12:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106750">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2f37hEL5kgmXXGCv8VV1M4hMeN-aYshBMuGwan3tRcO7V_WtRBfs1QxsRr5M5Z5iuCEli1tFZn38K-EKDashyxcb2DLiwn2VxbAuSN_Phx7q3nS_PITt-alCx9tgz8sLc_E17zNvKLFunLGSRSkFu6YdStLGwxbUqpB_RoJhlbb4gn1N_y1pUqyJyz5bAL75MhrniTkgPWsWXkiiNZv0_5GlLBn77sGLHxeFaF5l7g5txqnKuwCJy-yB3oS10IsQQ010VcHfyuH4iP5R_fc36qUp7kh0qcYIWI2bfXVfipOW6j0Q0SwQ_1f3JF2CJ5d1ZDitMMe33Zn8BYzJWt0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🫣
بالاخره روز پسر شد
😁
👍
‏در تقویم هخامنشی روز ۲۶ شهریور روز تولد کمبوجیه پسر كوروش بزرگ می باشد و این روز را در ایران روز پسر نامیدند. برای پسران عزیز زندگیتون بفرستید که حداقل تو این وضعیت کمی خوشحال بشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106750" target="_blank">📅 12:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106749">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fqd5ELf6FMtdPENv--AVsfuydF6SovRWnOI0Q2JJRJC2_YVRdi6prTuay4W1HWVN2wKFubohWxwuj-8IBMbPHqZ2XHI2kzko8RUeTJ1nC0X0-pTGrRdR3EFeRpM3ujilHrNEhTV2rtJ7R0Z0CEz6mlDJVowT2Hp6Qh5Sgd8N0vZPnt35zRpdguJMJTEjm83-OchcUrQTbtGDaQtOpFYll6lWzE1j-iWBDg_QGfciLpE19GHYIwQoEyVHPniHOyMt6lzUCY89-HEYj3FzaPclZi-Qtlikh1FJDDEEQcZH95l6ttisax_g9qK3T1uDft2bA4qrK6QwFD-LgGHA1wwGrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
💵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بهداد اقبالی میلیاردر ایرانی به طور کامل سهام باشگاه چلسی انگلیس رو خرید و الان تیم کامل برای این آدمه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106749" target="_blank">📅 12:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106748">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🎙
🐐
🟣
دیوید بکام بعد قهرمانی دیشب تیمش:
🔺
هنوز باورم نمی‌شه مسی اینجاست و برای اینتر میامی بازی می‌کنه؛ برای همین هر وقت بتونم می‌رم سر تمرین تا ببینمش. به نظر من، با وجود بازیکنای بزرگی مثل هری کین، کیلیان امباپه، جود بلینگام و سایر نامزدهای توپ طلا، مسی باید این جایزه رو ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106748" target="_blank">📅 12:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106747">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb69509038.mp4?token=f8sWulPv6uwUNYI7aelszwrv-tAt4SSsgtILz4dk36EiMMYBNMF6Q0eAX20rzNN6Y3p1bnvXYhFL-5Sjn5khUYd4ysIIX8-vNFDYmikVusvKeqIKkyczy_nCZpqOTIn0dXTVMxpP26fgaLc0n_MGUw9qHBkxgkWrtkCgxNNTNtx1mnwZ-EBWwhvYkU-GS72dwz4V9S33pCTyKpujoKzTq8WSWudOHd-a3jztNO4GkF7qpiG90E66Qn1g4Az6eykvnXLTcWQae4I4R0LeaCKULVujrB8nA7BUSbCz1UeZJ6JF3d6jBpsvm7e07g0eLf7vK24UZi7PtlaylBJIbq-c-lLgF2AdkZNAnts_UbLtWrbs2EzE_TDsB2LAHGITRfCJAPqRWanSrGVgBrfp27tT053YfHocVRnRysBPc0iwiWLvpn4nwy9kZLbINKuFXnP3fUGzaNhB9M2lhrR-wO4swfKpUhGHrFfIO9jNt0zp5Ik-EQq9K0jfz6F1foYVxW3GhMkh006oilYpL8HRV8ui6DPv8-3rdgDO97ng_XYbPUPNHlHfNNgp6hXatuUNNpiEDyH-7iinaPaVthQv3z4I4Eg-d35LqvZC0X7LmY7aOEESeY0Uoxn_FGBfCFq0vJjXjrrMjA0cdMbb9zhO8TZWElvuJoSnSWKPm0fV0YE0h3o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb69509038.mp4?token=f8sWulPv6uwUNYI7aelszwrv-tAt4SSsgtILz4dk36EiMMYBNMF6Q0eAX20rzNN6Y3p1bnvXYhFL-5Sjn5khUYd4ysIIX8-vNFDYmikVusvKeqIKkyczy_nCZpqOTIn0dXTVMxpP26fgaLc0n_MGUw9qHBkxgkWrtkCgxNNTNtx1mnwZ-EBWwhvYkU-GS72dwz4V9S33pCTyKpujoKzTq8WSWudOHd-a3jztNO4GkF7qpiG90E66Qn1g4Az6eykvnXLTcWQae4I4R0LeaCKULVujrB8nA7BUSbCz1UeZJ6JF3d6jBpsvm7e07g0eLf7vK24UZi7PtlaylBJIbq-c-lLgF2AdkZNAnts_UbLtWrbs2EzE_TDsB2LAHGITRfCJAPqRWanSrGVgBrfp27tT053YfHocVRnRysBPc0iwiWLvpn4nwy9kZLbINKuFXnP3fUGzaNhB9M2lhrR-wO4swfKpUhGHrFfIO9jNt0zp5Ik-EQq9K0jfz6F1foYVxW3GhMkh006oilYpL8HRV8ui6DPv8-3rdgDO97ng_XYbPUPNHlHfNNgp6hXatuUNNpiEDyH-7iinaPaVthQv3z4I4Eg-d35LqvZC0X7LmY7aOEESeY0Uoxn_FGBfCFq0vJjXjrrMjA0cdMbb9zhO8TZWElvuJoSnSWKPm0fV0YE0h3o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت دیشب نیوکمپ که هروقت بارندگی بشه اینجوری استادیوم به گوه‌خوردن میفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106747" target="_blank">📅 11:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106746">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
✔️
اعلام فهرست بازیکنان لیگ برتری تیم ملی
🔵
علیرضا بیرانوند، سیدحسین حسینی، پیام نیازمند، محمد نادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی‌عیدی، امید نورافکن،…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106746" target="_blank">📅 11:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106745">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqHmkBqh-G18n6QDmCv982pAiZErCVuNjvkXDBqd-btZuXQWoBLYGQ7A8-52dCGXLwbVjFLjZKT3TbOhqyZOMGSejssff2HuET8U8KkukAP6EwcXJG3FGJWYO9P-xXtqoUuIrEv18H5amjlb-7JJCe4o-NdKMR7Btg29pHJyU3fh9BA8XzT3UUFBTmoN1RH236lR4hQdaXi9nmbI90skxWen930VW1DikOYzMNn-z9SvEC2xROxHI0u0_zEwp1rRrec2Lr8FcN6SMIeXwkU4qrStGfbE2TDuL-6U9Z-V8sAOvIEdl9T1GMcMRoTFgrl_F7lFpWhgSsLWQCI1JgXD_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
اعلام فهرست بازیکنان لیگ برتری تیم ملی
🔵
علیرضا بیرانوند، سیدحسین حسینی، پیام نیازمند، محمد نادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی‌عیدی، امید نورافکن، مهدی لیموچی، مهدی محبی و امیرحسین محمودی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106745" target="_blank">📅 11:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106744">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b540a014a.mp4?token=hHj64P8EskmeBr-Sy_2qskqPNgvfcQVPQlsyPWooU-N99A0XGzoYv-7pBUuG_srVSrw9oYXHqSQrUDng2dwpZS3y5uhyC7OCvtW_eDgEBKBCgmffEhozgPdTF97MCd7Pxb8cPzEasqWBt0OdREVJLMTy5gR61XZCyBb-8UneuORmO-rZkdEWf8dmFeaqwgg-3HHt0gTODn-ncQeapUjyDXJMmOy5KSPnVP97w7aB4ZNU-7drsWaOwPg8vxOK5H2nr47h_JU55a2n0MTDQ3BfMc6KI2wCAuVp5seQjtqIOikKfJ7h8suI6kg0ifJYDBMbGG-N66hSWOjBHopK1byh5LTKoc5C_0ZGzLyg11_8w4-MpNF_R7T38Vd0s8G_4h81rspPHiBny0FS4UlzNIOiGjxk48nhKjsGkxnKctL69oRysz-J3lOePcZ8VGVNgOC36VLH0-xL0UFOMCv7rUexmhz9M2LfpHNCwpbjv6SfscyQK-oxBzdtmskrnfPVsMLq6RAvNE-0ZO4j8FtftV2Pi_8mMYofg2r1to2We4Pspc-o8EnKGuulJFNJWAoufNvPyJVtaBkKio-_qsjUQ_kaRXLibaG33rhZgGTTqqmG1z9mQsvVqHNbYydR2TfdK2tNhl-4iIX36yRCi7vQ7qpiis6LQ0BYv_dRid_rzIjSuyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b540a014a.mp4?token=hHj64P8EskmeBr-Sy_2qskqPNgvfcQVPQlsyPWooU-N99A0XGzoYv-7pBUuG_srVSrw9oYXHqSQrUDng2dwpZS3y5uhyC7OCvtW_eDgEBKBCgmffEhozgPdTF97MCd7Pxb8cPzEasqWBt0OdREVJLMTy5gR61XZCyBb-8UneuORmO-rZkdEWf8dmFeaqwgg-3HHt0gTODn-ncQeapUjyDXJMmOy5KSPnVP97w7aB4ZNU-7drsWaOwPg8vxOK5H2nr47h_JU55a2n0MTDQ3BfMc6KI2wCAuVp5seQjtqIOikKfJ7h8suI6kg0ifJYDBMbGG-N66hSWOjBHopK1byh5LTKoc5C_0ZGzLyg11_8w4-MpNF_R7T38Vd0s8G_4h81rspPHiBny0FS4UlzNIOiGjxk48nhKjsGkxnKctL69oRysz-J3lOePcZ8VGVNgOC36VLH0-xL0UFOMCv7rUexmhz9M2LfpHNCwpbjv6SfscyQK-oxBzdtmskrnfPVsMLq6RAvNE-0ZO4j8FtftV2Pi_8mMYofg2r1to2We4Pspc-o8EnKGuulJFNJWAoufNvPyJVtaBkKio-_qsjUQ_kaRXLibaG33rhZgGTTqqmG1z9mQsvVqHNbYydR2TfdK2tNhl-4iIX36yRCi7vQ7qpiis6LQ0BYv_dRid_rzIjSuyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
آنچه در بازی دیشب بارسلونا رخ داد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106744" target="_blank">📅 11:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106743">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnYSMcJOuCNuxVYsY6Rc1Tn2lGXpLdiNqhvLRxlznQa1Gc9GcaotWlfG7guZwfI6whFdJri9N2aZZO67mv2Kc-bXCe0PLmzamcBuc1X07X2usUe7o0JqTtMw7lK7d0jN-3z71nViaVM3nAoRkORMqfRxuByBS1VeR6f39OMIsKZ-5CJXQect2nM9J1GYK_Hb1eFMfZH6ZHEzx9cJBWtwzphdDtmj1eNcBIUA0y2tyYZfNaTQ9p9qQvRgn54pgqF3qQmyIKXLCp-tB21k45HN8E0C933FeTx3VDFx_zmSxb2nUJjj6tK-kUszgqPG_dUMMZ-NtvWjd2RaUb1iRahS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📱
علی‌ضیا هم رسما با انتشار این عکس اعلام کرد که زید زده و دیگه سینگل و این‌چیزا نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106743" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106740">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee3ee373ec.mp4?token=d5PFrh866CUlOgO5PnZVWs8vxz7VKYphK8LGLheui-ORclqgkFQ5b4i8xECXy8lmZ0EVHKv0J8w7wIy_7B3TnIlOXEUAg1jY0i5vHBLNwYUS_EoSnKynuM9tOPTX2phhPQ3K8UG8Wn4gADPKWsvWBsklz58rhHBEykcK-bovFW9cifXyTij0Od5iYefMdQWwloxKfF_Q8WwBMfwZjDPCW0-oUXQ8bKdgE37t0y7pFAa-tAdfWqFfUWnOTX-Xzr0XaeYf9q6VVr581lJBjmwAaLC2-ayJtCbxPtBbEvfeburCwORlIqbgZwBO8FpM_KsQBksFgKXYpa0ncCUkdEL_dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee3ee373ec.mp4?token=d5PFrh866CUlOgO5PnZVWs8vxz7VKYphK8LGLheui-ORclqgkFQ5b4i8xECXy8lmZ0EVHKv0J8w7wIy_7B3TnIlOXEUAg1jY0i5vHBLNwYUS_EoSnKynuM9tOPTX2phhPQ3K8UG8Wn4gADPKWsvWBsklz58rhHBEykcK-bovFW9cifXyTij0Od5iYefMdQWwloxKfF_Q8WwBMfwZjDPCW0-oUXQ8bKdgE37t0y7pFAa-tAdfWqFfUWnOTX-Xzr0XaeYf9q6VVr581lJBjmwAaLC2-ayJtCbxPtBbEvfeburCwORlIqbgZwBO8FpM_KsQBksFgKXYpa0ncCUkdEL_dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
از عجایب فوتبال ایران؛ دیروز حین بازی تیم بعثت کرمانشاه و نفت‌وگاز گچساران یه نفر درب اتاق داوران رو شکسته و تمام وسایل قیمتی تیم داوری رو دزدیده
😐
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106740" target="_blank">📅 10:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106739">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebaf856a1.mp4?token=iKgF4p1WmUCpTOZeUIkrIvEnvlFMl_vOFcPjdQ-xge_Cw5PLJ0xRBf3dUrwD5cFDVikL_pax8FjZKymKdTefv3D6BbUsM5nDdjSaHMgSuOLiQSXRH5FcV55Es5V24GV_13anTXncRsqHpr5JBGqg0kofwbWz1mR3V8jjudO9NYGX1QZ9_kRYAetPuJiZI2OY2QAQ4m-e0y4bQGWlGsTMrtGpH4ih6lv3iAVorKAGm5CoJSws_TDrfU9otyIzpYtzHrDY1X1GyNRvm8T28yzukXHTefnUVx2T6bg48-5zZorqjEIskuP61JWbpnnOKTpe_YVggSV-mCUzqp28LyFAsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebaf856a1.mp4?token=iKgF4p1WmUCpTOZeUIkrIvEnvlFMl_vOFcPjdQ-xge_Cw5PLJ0xRBf3dUrwD5cFDVikL_pax8FjZKymKdTefv3D6BbUsM5nDdjSaHMgSuOLiQSXRH5FcV55Es5V24GV_13anTXncRsqHpr5JBGqg0kofwbWz1mR3V8jjudO9NYGX1QZ9_kRYAetPuJiZI2OY2QAQ4m-e0y4bQGWlGsTMrtGpH4ih6lv3iAVorKAGm5CoJSws_TDrfU9otyIzpYtzHrDY1X1GyNRvm8T28yzukXHTefnUVx2T6bg48-5zZorqjEIskuP61JWbpnnOKTpe_YVggSV-mCUzqp28LyFAsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
🙂
آرزوی هوادارای رئال مادرید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106739" target="_blank">📅 10:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106738">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‼️
⚠️
خودکشی سرباز روس با استفاده از نارنجک پس از زخمی شدن توسط کواد اوکراینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106738" target="_blank">📅 09:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106737">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/704ad943ef.mp4?token=Gnr7UiApQriwhfzHDhFQSduR_7bTLcdpD09VdWvW8zBD-1BZ79suznvL7bSM_nO2Hs5eQ92sG2oEzBzWYReszFgev_aatOBehHT0VPqt3O94TBSUWj2wHxqrgUqqoZk2o6TvJbxmWxEU1SOCRS87OQxQNXrsHbAlSVYIrqt5-JLddbJ6lLV4J7S4_sBIO7G8fRU23b-KTy-VDrbDwK1XIOFLAGWJRQhGccAI0wm8dg7-u4-iAmk7QS0q7GjpwXAP9O2iuxwOYneMw87PpE8enl0oyI0OYpWF7FW9buvzRHeWCSLOzxIYahwwbRSWjVxZ5ozbBUnmWTuKgkMjzF4FBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/704ad943ef.mp4?token=Gnr7UiApQriwhfzHDhFQSduR_7bTLcdpD09VdWvW8zBD-1BZ79suznvL7bSM_nO2Hs5eQ92sG2oEzBzWYReszFgev_aatOBehHT0VPqt3O94TBSUWj2wHxqrgUqqoZk2o6TvJbxmWxEU1SOCRS87OQxQNXrsHbAlSVYIrqt5-JLddbJ6lLV4J7S4_sBIO7G8fRU23b-KTy-VDrbDwK1XIOFLAGWJRQhGccAI0wm8dg7-u4-iAmk7QS0q7GjpwXAP9O2iuxwOYneMw87PpE8enl0oyI0OYpWF7FW9buvzRHeWCSLOzxIYahwwbRSWjVxZ5ozbBUnmWTuKgkMjzF4FBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کادو ولنتاین سمی مسعود شصتچی برا زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106737" target="_blank">📅 09:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106736">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546d8bc40e.mp4?token=LRsu3E6L8rmnZ5AoFODqHkRYmwxZtNRvBEOwL4OQ7NWP2GslyOlsVECg6dKNK-eQNifEn2fmlUGQQJFqRSdNRPsAA68bq_ZDf1JVVGgIw7tWZUUzlLDAfodJLWDf7icLSw4yryxYin_NO21HrhPoRSbKXiHpx3DALX50wAEqgRU5pyGABrtKz1Zax8aUp55hnfHM2wYPo5X8ZJSUC_i9jmRXwaVmsugUpCkDQm-PLuw-yzQyCkwTWWicN1d7YmE1cBFG5DFGZAmfATc9NkDL9DI4G1M2uzv-_n21SSI-3wBuVb-F69izXj1H05gwxT1NV2DHMhBjDoEbeWNxqkkmWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546d8bc40e.mp4?token=LRsu3E6L8rmnZ5AoFODqHkRYmwxZtNRvBEOwL4OQ7NWP2GslyOlsVECg6dKNK-eQNifEn2fmlUGQQJFqRSdNRPsAA68bq_ZDf1JVVGgIw7tWZUUzlLDAfodJLWDf7icLSw4yryxYin_NO21HrhPoRSbKXiHpx3DALX50wAEqgRU5pyGABrtKz1Zax8aUp55hnfHM2wYPo5X8ZJSUC_i9jmRXwaVmsugUpCkDQm-PLuw-yzQyCkwTWWicN1d7YmE1cBFG5DFGZAmfATc9NkDL9DI4G1M2uzv-_n21SSI-3wBuVb-F69izXj1H05gwxT1NV2DHMhBjDoEbeWNxqkkmWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
یه زمانی نوکیا به تمام ایده‌های ممکن ساخت مدل جدید، نه نمی‌ گفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/106736" target="_blank">📅 09:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106735">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SL0hLEihZ-9mbrAaVFp8oIkDmtW78XaDpU0yOLPp0RCuBiuMdbeCt_vVYtwQ_DMXEzYoDJWMSgXyOmmfJWhkIrD5-v90vC_2nmqjJm2w6y7mGH_EkgMmXUNRPkiQ9aEk4uDNZAtuKTzxrB4WLQirONRsfFyNuk_7-ETMKpvgpEO5bHO74MqrUdbEs85bqTSDRnLoTunLZH1mE369o5T2qgP4ZYx7atc9fk0g42tXetPbT_q_d8S_oqSPwacbCCpDFv1m-4Re99WS0rLUjT-ZzxGRpRGHTQ4l8nHbrqSswAZ-l9sAgTBup86ReThiE0hz4vcplG6KCDhOMgr9MlDP2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🐐
با قهرمانی بامداد امروز‌ در جام قهرمانان آمریکا، لیونل‌مسی به ۴۹‌مین قهرمان تاریخ فوتبال خودش دست‌یافت و رکورد خود را بهبود بخشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106735" target="_blank">📅 08:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106734">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/106734" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106733">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BnAHWYbiUbbVT-qCFvC6KC0IoF74pd9oCXUDnoKJsd531eQBgsZ3YM64WfOmo4Bhj-Q3YwFBakqth13bgE92A4SIiUsF18I8P-Hcf3hPRG6gfi1_xJOVpalueUGm78QY5Z1FXYNjRtLmD0-0Uc4fMTZzLFc77xYdbIOZVXJwdrBI-TW4RNil2DTkRKhg_k2wmxmhsDYXZHXUEt7ya20xzh947BpqasMfzRo31zrsMSuxQyS-mbDNc8mt8-cUAkis77dEWf5t6gv3L3eKeTVlVfxeyqnXim_WsBqllUZj2t4E2RUf0JH35yxCkhdlYtei9B4D-SC0N3r6iSCaufLViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/106733" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
