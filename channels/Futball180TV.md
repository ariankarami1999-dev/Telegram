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
<img src="https://cdn5.telesco.pe/file/hUEp8XfCtW9Z6zlJulYiyVgtsTiHF-ATVrStROt45Au4lncQBrxpxkxE7MvsHaoE6Zzypv5CecIUaIn9aYTa55D7qhKNd2Vngcow0IOj6Umwcwd4b-edKrosf-w1w425pidIkYSQV3Qdb7y4ZL2MrwEUyVKmuPjcVKW111328VUdbsaei5kQxiNrTjUSLn4JeCOXsUqvsKrI9lzosuOI6nBw6JBlGS3gM_Sz6SXo0_e2SKkn-e25XQe4MakN7q-C4pq7pVTW1eKe_F5Az6keGmkQ58VWRcVod2aEOO1fLVT-udjXUOk75JkbwNwi3UguNq6Que5AjQA_57XW3YpmiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 646K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 02:32:45</div>
<hr>

<div class="tg-post" id="msg-98001">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZDC23mFJPQAxLDIhcUlJSRWtQJ0UVgUVEpp_wl8OVPnDR_b_qM8SufejNf2ILfeDwERL6r_hAf6p_eHkv95qOq2_wdAbXNJNM2QQloHjKgTsNb_cgJTcT915JgPQMiBE3a8M8mY0lCQ_BPgkiQapHQvxjNQlw_3ODsy1G7q5cDL_ixQMCUxhrPc38M2pQSuRRBorgVJ31X-jYv32oTTDLAnqPC-etFLiuRb_E22wZivneOf3vzn6PZJBUrr153oMW2GbDwr-KEtNGYGLnHKF8qcDmvhdB2dFlIZzcO0Kz7sefs33veFMh4mghFdVaZ0uc0uh1669RK89heG6vnHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا جناب مسی آرایشگر حلال خوری داره
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/98001" target="_blank">📅 02:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98000">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSI3J2Vrn76J2xFGht_CmU1cye7Og8tzJIQc0YgiAh-z7Ck4sNVH8bFjegAVN7KnHSEt-GPtgbMpzCh88r316byq7EohfcOq0Qtc2byx3snye0CMW5rTXo4L69_cM3plOqWPOZ3pEh2VHObSVKgI1D7rG09ntuNtPIzG7Mx11BWuuFh7r5_yN95Hz8PlKppELS1Gg4VdIL3giNxGNrOf7Kh4haeuY_k5JKrYe7c_y6-uDCUtvcYJOFjdM2B-7eUDmaiTFdoQmU1ndq6wtAjmLYLmVwqyn8GoFZbg5pO1V0kRc8se-kv3Wb2oWdDp2Tw4NUn4v_OCdn7IeWgSq9q5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🏆
| بیشترین مشارکت در گلزنی در تاریخ جام‌جهانی:
‏
🔴
لیونل مسی: 28 گل و پاس گل
🔴
کیلیان امباپه: 22 مشارکت در گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/98000" target="_blank">📅 02:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97999">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پایان نیمه اول بازی</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/97999" target="_blank">📅 02:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97998">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IbZoYfi0z_CYZOOb0el2jqdH9PHyRPk840XmgYleKuRCtep6w3eCl0mclqRslTjOiTBDogPvsMCJj_ePpdSZmvFTYYcQWQIegtd3lE-W57CKmGrnclY5DSttFFavfm1R7Z9NxfXDcSsSU56BHHnQrko63KVXqqs1yXdLI-ZFOPNpNvu2RIqL3UAS505l9tn1QvrzSShi_SftvQvEQOdXzGLT3l70KXyUR6LcZ9MBk_cvuszxF8H4kKLyOwqEalNyKXq7nJRWZJAN1UTE2MJGW_YKnEjKXQOrr2tvxndo3vyfgX-vA-0gFNHGqv_-I9LvtMSg4L6g0g3V55k87TrxSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/97998" target="_blank">📅 02:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97997">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4FsY2IC-B9SLtsRjglE6gYDq7o38tuu4eDAgUQpzd_anR8gmolOQqJhX8Ax2hxEguEgjn9L05DFDcxeMe8XfqdOesQjmIoHtlY-9pYAr_LSpqyUoaksdEqFI8x3kHCfpF_iEq64gdNMzsY_Sv3jqcy8eCeLZbI4F-UmugJGx-uC2pZttttG5Yf3r1d3II3g22VKqG5J7Jmrwfv_zyX51zHb7HeqgsKNAvEYWAU7qVnGl3tCFF_fgoO3T_PBFeip7bGo1Vtyrhy1Rj2Yc7lNte-4fuB2JNj5V1SISABvd4CUZYnqHw8V_Dno02G_CqlWg4TgfgCq5fQKXxH4pByVhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
آرژانتین تا به حال 9 گل در جام جهانی 2026 به ثمر رسانده است..
🔥
7 گل از این 9 گل، توسط لیونل مسی به ثمر رسیده است.
✅
🤩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/97997" target="_blank">📅 02:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97996">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBvBWVV446I1c7pdmSHpPUo9zpPEJQoz9F4XgsMbVMJMmbURLLTz23Rqp5FhIAXfCt6Fc5X-xhAzTKDyREAZ-NUaOpsDSqmbiusxCNIen5r-d-ZwHozpQndXL0LNth66cBwpTz_37PR-IPtN1ItM0PkK_Hm4TQrufwhjPSRXJNJJYi1SrLfewNFLQVWDB5OA-TUZCnnH1qQ-ZeNJ6duvMLdVTdjOuPxkfQDt3gGcE3XoJLaeSqeMoHdTi_8NJVt6ltwbOqeQGExDqAo5X3DLiN998NLuqw40jitDvrNfW0aO4r5zErTe94dBE2yKcYYbepXDEb9VQMzEatjdQazDSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بانو شکیرا هم تو استادیوم حضور داره
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/97996" target="_blank">📅 02:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97995">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN9FbKg9yPXBeD2nEZJBMF2fP5mVdytmG_BlYNCadWT3Oa30s9Nk_bvj8KtvfDqD3RYmlXUJiuJq6wKLyCfK13AKM_Dstj0PKGw1Obu9zLqQxocIEJiatoPgx4MWYsV0KB8aJOVkx4SHuWbggdFV4G11PCmhC7jLnnqjwgKr0xJrgwAvCJd7b82LcWNRpCuG1bkP2GhW3zkeZPp12NW00ldqhet4tqvvDNql4P7Ae1pqZOtXcfDKvfcyAaktuhncPF64QUP7wZN9dvzHNuO-NbOoR-5d3ilidbyTJVc2QL6P70g5zeKbrVWnl5cJ_HFoFSKzfviEgsUFPIC-76UnxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
لئو مسی اسطوره فوتبال جهان در ۸ بازی متوالی در جام جهانی گلزنی کرده است.
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/97995" target="_blank">📅 02:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97994">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBz7YI9m-5baQyGxfS2Tm6UOXkd9YZX4IfOjA1q78lNiqDnGnv72BXj3bAWQ3N9iq7SeYE5CeY-iumEcjO6y3hmgqFCGx2S1tv4cZE8ZeTGgvjs9P142CLlUojBDLnofxanScWVLle3Yi5ODVTrtGMUTU3S33uwt-6RICU3d5YEuIt5tGgd8CF9qZvF_zu8-tJHUAWBVT-3a7cYFHIO-00eyB9VqKcvBh16oeoGJWKCzX6qIdcqpW9jUltMjKjvJj_wL5ksMHdlEFjjVFd-c-Uf0dijO0kWecrXQY6r20X75fYe8dkYKCW-INQu-YlQReJXPYba2N4RzjuQB3pqOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاگرد اول امیر خان قلعه نویی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/97994" target="_blank">📅 02:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97993">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c431ba96db.mp4?token=WxEGOIN2s1xLeCZqrt-CgFXQunVgJOSfe8Ropy8MsUbWqUivv00vGQVhvBW7KfmdMW2861fUDgkhzvk9d3rFxF1fmM2LkN3HYUgCu3iiQLKrJI83PRZGPgLg5Eejq2L0y-8DAy4D2ivJXMMsw9pp75sojJMprz2hynbeZ3aHJZMxzOaphfIWj7gj1sRjUpjoTzHf_v01s-IMtYVW17lk4lC0KTyZURdguHKQO-nLdwT2XqZUBRsC9X8foYhNGZ4D8vgKYgU489IoJS4CftE-va2fcYooUbZYaJ5ubm7gysOdZ3Vg3eDANHKaqKyD-yAKX4ohghrpmgD58BnwRzC2yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c431ba96db.mp4?token=WxEGOIN2s1xLeCZqrt-CgFXQunVgJOSfe8Ropy8MsUbWqUivv00vGQVhvBW7KfmdMW2861fUDgkhzvk9d3rFxF1fmM2LkN3HYUgCu3iiQLKrJI83PRZGPgLg5Eejq2L0y-8DAy4D2ivJXMMsw9pp75sojJMprz2hynbeZ3aHJZMxzOaphfIWj7gj1sRjUpjoTzHf_v01s-IMtYVW17lk4lC0KTyZURdguHKQO-nLdwT2XqZUBRsC9X8foYhNGZ4D8vgKYgU489IoJS4CftE-va2fcYooUbZYaJ5ubm7gysOdZ3Vg3eDANHKaqKyD-yAKX4ohghrpmgD58BnwRzC2yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللللللل مسی تموم نشدنی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/Futball180TV/97993" target="_blank">📅 02:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97992">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بنازممممممم پسر تموم نمیشه این بشرررررر</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/Futball180TV/97992" target="_blank">📅 01:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97991">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">استاد گلزدن در جام جهانیییییییی</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/Futball180TV/97991" target="_blank">📅 01:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97990">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">لیوووووووووووووووووووووووووووو مسییییییییییی پادشاه فوتبال جهان</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/Futball180TV/97990" target="_blank">📅 01:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97989">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مسییییییییییی</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/97989" target="_blank">📅 01:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97988">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گگللگلگلگلگلگلگلگلگگلگلگلگللگلگللللللللل</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/Futball180TV/97988" target="_blank">📅 01:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97987">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گلللللللللللللللل</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/97987" target="_blank">📅 01:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97986">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js2xO9Vm7XjjJLSjf0Dpq7ceUb9_YuYgFVa027IMT3sdJ8oNJENep3cRdy_QV9Ic0XCqlhoMQwTfnB2qpIuR4mNOO3e5CN0FyTv8oWG7ass-8b9NpBOxQFw7jX9lSBJqVMGVuW2KoKkw1A7k15hLfkrIyEhFTxtSPeR41N51L2YJDPh2AfU0xg4y8VxXgfKnu8-vcULqDynIDrmhCcDbLGzcaF7ki--pcrFIgyJvK5_oqGBK-f2NetN5Lo7Pgss-duLFR6HMcsUjywHOH-q7kE8rAgGRYjGEN9iGUvdbcFywX1jLNg-Itql2-X1kEWmBN_o1CI8m_xf98fsc-Fwh2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این زن و بچه و زندگی نداره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/Futball180TV/97986" target="_blank">📅 01:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97985">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jz5tD296GjFW9FrLU83EP52otuTb_TjNkgIthQkQmyy-vqIichXiOIMXRZkBhi4g7AiRSfVpXDbpwAgzFQXCruFdE11-ZXce-wqmGu1UGY0CUh8NsnD6IWhXgc1UcEB9SHjHFtrFZfVqMOimHk__GOO7f2rhALyxWIFkXYs_5MP2UPq-XgcAAdauGdbNk7lWM9HGLzSoyzJGoGX9Vvuk1akJZ_RLljfMZMr7pBlrUZ7LzaT6Bqr_FpgwDfg41GikBpYaW7IG5FC6ywuKe30ockaLEXzPTS7DygZQ0mZzq7YVI_M8jhqK9S4i_uD7mNBPAQzdnYj9cpdmapM0rrF-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون سوال باشه که چرا جایزه های بهترین بازیکن زمین باهم فرق میکنه
اسپانسر جایزه های بهترین بازیکن زمین یه شرکت آبجو سازیه (Michelob ULTRA)، زمانی که بازیکن مسلمان باشه فقط یک جایزه فلزی تحویل میگیره بدون نوشته نام شرکت آبجو سازی، اما زمانی که بازیکن مسیحی باشه جایزه اش فرق میکنه و یک قوطی آبجو هم داخلش وجود داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/97985" target="_blank">📅 01:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97984">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/Futball180TV/97984" target="_blank">📅 01:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97983">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uR-G63i5-dPTAjAuViOkjLZAER0Tze4Csdc0fVgeCbvUHqGJjJkP19AoAp-936kkYJ8UFENcjEDt0GprQxP2sIIa5xUiqmqzk-cCntaDMYuVZDh-hwzOXgo1DTUoQ7HGzo_l1xgV-WN2crNsvJI-DiIs9SQqElhEUPxIWKqrQ4IwmsVgLy5FDmN3AHTFf54sj0zYhTQ8MCANCm1bRnjxPflNB4IDhs0sqYS3bKZIXf5DaoTBNZrhua_j-TRQHEycaBIqfCBAYOSDbo9bd7BDpthvBTjyDl73zidGUFEOAefbm_5mmAtYF9baABN71ZwKeMk-ip4KHcUjd04iyZmimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/Futball180TV/97983" target="_blank">📅 01:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97982">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بریم برا بازی
🔥</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/Futball180TV/97982" target="_blank">📅 01:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97981">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بازیکنان وارد زمین شدند</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/97981" target="_blank">📅 01:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97980">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d41a557420.mp4?token=UPY5ViA5TbPSLhLxU5DNZImUFbh2o0vwXA2LjqT0pnKcqw8Co5RiLCBpupD3JZmg4yHUru2QVwRwUreKkBNEvkgn5-lEj_E6qWr5eesYuk7ot1bfZjk1uL-hdIjhEPNsDjI7Cr50NHxawMFLuyPYdif03FpaTKhitUI4w1DnZkcz0RlzMNr2c2vnlBvwU494IEYs_c-9E-LgJq-uW-q4U5v2pwGO0We16uKu4ReRMizbFBNkW_bBFd6CjDLk60s3kJkg4aLB6fyhqWQWuq2o_QLN50blsPkzIGSB-CBxV2WT3xxFpnZJPOaJZtDutk1FXQcgWqOC2Isade0RdgSF3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d41a557420.mp4?token=UPY5ViA5TbPSLhLxU5DNZImUFbh2o0vwXA2LjqT0pnKcqw8Co5RiLCBpupD3JZmg4yHUru2QVwRwUreKkBNEvkgn5-lEj_E6qWr5eesYuk7ot1bfZjk1uL-hdIjhEPNsDjI7Cr50NHxawMFLuyPYdif03FpaTKhitUI4w1DnZkcz0RlzMNr2c2vnlBvwU494IEYs_c-9E-LgJq-uW-q4U5v2pwGO0We16uKu4ReRMizbFBNkW_bBFd6CjDLk60s3kJkg4aLB6fyhqWQWuq2o_QLN50blsPkzIGSB-CBxV2WT3xxFpnZJPOaJZtDutk1FXQcgWqOC2Isade0RdgSF3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇦🇷
🇨🇻
⚠️
اطراف استادیوم محل بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/97980" target="_blank">📅 01:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97979">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
‼️
متن خبر: خداداد عزیزی دقایقی‌پیش مدعی منتفی شدن حضور اسکوچیچ در پرسپولیس شد
✔️
❗️
🤩
واقعیت در پرسپولیس: جنگ قدرت شدیدا در باشگاه شدت گرفته و چند نفر اصلی بدنبال فرو کردن گزینه‌های خودشون به نیمکت سرخپوشان هستند. صحبت‌های خداداد عزیزی هم با دستور زنوزی رخ…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97979" target="_blank">📅 01:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97978">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSJrjPrKUvpd-AoMFfqEFy739wxA_AFk96dELEKHy2HIZnQqyT2QVa03u6IavBu060jGh8BTkInXTJR5d7KYjovcF2nTPQaqdT2fz7rLZpzH8oYCh2O65FIo9ycE0yEAhb48HUzxGEfQ0gMMSJ7tXK5nXse1hylTrhahroVRrpC78Hk6iNfRKPkfC_tlH4VpO-rqA0gd93n9nBKmbhtl_TmeWIo7wTmnJwuejpbnlVAazQJ0teQJlqT1SxVfZN9BoIzn3Dv2rNZT0imIcTH1rj1lXFeuxgZlmdQTHL46Q8pZAcXBUUzXt4Sp97cuBenOFOZaoEhd6a_zJ85LcrmprQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👀
🇪🇬
دلیل انتشار این تصویر از امباپه که قبل از ضربات پنالتی بین مصر و استرالیا در حال شادی است، این است که بازیکنان مصری در حال بررسی حرکات رایان، دروازه‌بان استرالیا، بودند. او دروازه‌بان باشگاه لوانته در اسپانیا است. آن‌ها یک ضربه پنالتی از امباپه را به عنوان مثال نشان دادند تا بازیکنان مصری بتوانند او را بهتر بشناسند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/97978" target="_blank">📅 01:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97977">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUsnkE4kko3inRHpCJxQSV4WT19VNQjrv3vo2q49fiUGl9rn6XQxvSMm5g-VOyfEsSYPqtN-DdUpGT3xnuHbFSAReaA5xqpuyfyslIPo_uDW9EFW9fGAWqTvnbk1Gpaj_uY-ytg0LbnYoZyfJHKcy8_V_OgeVNBwQcfT5XKfHTT7dtmDC8CK_7czkVMZcKxu2RhQHxFyWwG7_G-6CFcG_dUXPh41Qd1gNHMOO5Ed_t9OX2XtdRH2YaJAG0lSoCVhLSrKh4jPGdQ8pu5HotgwQ_jxwfxhayWglKyxv9-edIku7jIQOt0dwgb0oMLMZHnQhY8l4VX5Cd5tJHv76a6hPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
🇵🇸
🇪🇬
حسام‌حسن سرمربی مصر: این پیروزی رو به مردم فلسطین که در بازی با ایران از ما حمایت کردن،‌ تقدیم میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/97977" target="_blank">📅 01:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97976">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVlwbuGsDvHkUAZZw4kJ-Ccwfe94uEH8ioEZaHmG20VUhimR7g2BbBQFseuygz2XTrLz9B01MBzPM87YwiEFLVS0Dwr541u-IfoSXpa9TZOk7zYM_0EDP6_-glZfwJ5yPvoUIIAuBN7RmHkZtSB3MaKp7b_zwoXhXfKa-sYtgSk_38KNzYbxSCOtnVlo81T24FoEMY1mcBVhZmUH0oUt4C968Il22T0RMDQ3MIHFfLE3XNR7cwo2mzdnW1aC2fho-F87pTATVYW6QCr10fdnLV9RQkdH8s9X00tB5wUEmEZd7n0IUB4kNrft5MZw5JeAk5ubOCtWBD2wCYUIs-6dPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
از آسمون میامی بوووو میاد
🌩
🌩
🌩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/97976" target="_blank">📅 01:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97975">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWLQkQz5yNulzpTTC4Vlr-4_M_dSW-huZ9SPe7xhbqGvos6nE61qmZXxu4ruKlz5LJYTBkCtBOOhXZagImC72k6v7LEMHCELyK_n9t9mogCAKZsu5vwokyzeWhC1IyPxxILMYDOlCazIladkGoxXX0wNJZLlOklpwKmpr7CdsVeOTGjDZRz-YGJ2wxxm9wtjZIJIAg_4hRBgscf2mP7KV77BiQZEU-FxwslSdX59wkrBWJELAxHjkd8qD8htuLR0p_L538Gly-r7gNEnXB4qT2t7mWc69RGUAMsI_80SxaRrn39VLXc8_OripWTI7G86zU89xLxlInWceOSvhTRcdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🎙
🇩🇪
یورگن‌کلوپ: سرمربیگری تیم‌ملی آلمان رویا همیشگی من بوده و‌ مطمئنم بزودی نام کشورم رو در فوتبال اروپا دوباره در اوج قرار میدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/97975" target="_blank">📅 01:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97973">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FD_0v8wcnXxcdxyMoIj-GHxpCLquar8WMrPvzHhwiJ9Tqcj1pZ4F8mw284jQHyU9uF6zJZ-agG7BE5vLdg-eKqqzhf-_2fGgQd-DZEjVmxn7g3Lk-jKcM7V-AZ2bNNa_4QDOrb6YLwHmJLgsOn-Uzso_eMkKhE26FMsppFWvT64y2MyjLTqfi8V5QVVeapLFElAAyeRw3KLkTRgXA6YiyZWFIducwxMbyrqzJ7XmKsuUjMGytDVesfYjjp7wulvCTaSrKqdfomCDTVOzu6NC8LkTQ0nRP8mcaegQCIpuNGwx2ifNIxunliwG2LK2gzYtWONDCoyrAF_h_lJvkoJlsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVv6boP4LEl2TgT47t7QHSmBf3fJtnWGBVrrTlIyGd3w_LDZTaQhZM4iETMGW8HnSE8rW6wiz1W6kqFdMvADeS7zrS4i1uXOL6__sojpc1_pFgksyGsG6uHjI9b8tYv4HxhuGlAJ9QfzVMtKcKpDx9BeYOGRH5K02Gj0TlNvSOPTEdP8bIrDZsK3f9YTBoLOghuTNPuEq0KIxa6sNRo_Jpl1E3kAGTDmK0HKVxT52AlU9_J1Wv90tZOPMryqf7Xr3un-_WPmA6LB_qB0XOHopAPkO0blDcrG40YoOJyukpdRD7uMUqPdFdZ_4Yy5s7MjAgCH91gvvkAMmv0D5RXU0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
👍
🇦🇷
حال‌خوب اسطوره پیش از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/97973" target="_blank">📅 01:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97970">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HgXzzGJgtgRvnAUjqzyFnpaIUcH3N0xFKH0pnxKC14a9EcRM3DygMdJpsfy75TPehvkViVjYLEvp9uKO3_xERiay0H6YAS03bTaf4VO_-wrYLbSuxERmXZ0qFXKgQCLf_CAiLOuN2nCp4FUsP2W2tt8rAVbRR05NcknJUHataMtuLnrHW6SkFkKL87l5z8hyD7yr5DuYY3w9tO-n3cm4MMkEsvJfCXhD6cSMZLSi5jqG9P_hEZ5PLmFRb_SipMvv96fz_ApsnoNm0wSSCEWLxxciZsxXgxe8Sjk2dKh1Fm2iZAmsjzwqN6SQb_9J3WvhpQ14U0WANJI71Nf4mDte7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErF1ZyHJWMhGkN1p-PS-u7eC_OqvzxTaPBx2_xzrDmDB6rV_1BVM0hUbKw2G96Nfl-_jhEL2-dY16s6VA0oWYRKg7VcKOXUQdE9fpm5fRsV89dvtJE2yuInwyVbKoHLoPkHa52f8YXx38kQcYgltF_RY2t_BRj62kP1FWBEso_V1igOh_kK7qd-PoJjqI-QQJi4ObnVCiPq0X0r3N6r18YfUoRP6rxl78mfRF_ebTDqz8SJh3hV4tEcjV8bpX0AyqC-kdZqcRfzmApCAl0Kc-ya4xhHjhHZ5TfNH3wrjmGbCs03Z9Im50Tn3TPVfDV1LxO0JMb4i9TD1QsLwbujU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QTgzfW9eA-rpcNH3HRS31ne09SP5-FOBX7QFwSIZajBrCX7D19GUEfT1r7dv3Y5CI_j4SYyBeNoGcaheD-Q50t4mU0JPZLJO7nk8pR9sCBs0blTRIDTxpvSU0IkH9PHu-DT_VX0yCDHyeF_cVvIwCgHtnB56rVrw4XI77rwJKY7KL5224hJXX1ln_ilyk5h9fDJjim3yWGNHAnc5vbbmQab0q_IQuacbIyiEMgegnaXJOkSiUiD_fM2AHEQZDwPYU-PrjTem3FS7Gln7OQ8paYBoIJzeyVb2hUODZRfXvKV9X0Fp_inqo0ndgZjB4Ch0wcp9xBrhVfkNXPhCWo52zQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
🇵🇸
🇪🇬
حسام‌حسن سرمربی مصر: این پیروزی رو به مردم فلسطین که در بازی با ایران از ما حمایت کردن،‌ تقدیم میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/97970" target="_blank">📅 01:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97969">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S19X15O6Snm9vSKBXuPWccw39MI3lhP5XzmzX4m-VHjmwXZSGa-WpqAZK1uWFzsEm9sMfNr-mDFd7QNWgqz7VjwNWd91pn4WgPATp_uYsXxpnIYSycTDHmoq9t9VXBk5gytUzAda82gfzJysSKVyLWLLwQ0CwJD09_B-3WIdEzQq-qmWldmQP6i8FjB8ZM2rnvEvui8_a68TmACPb1RhMObiXqdz9FF6jatG4TtbZ5lRH6hPcmTJ8olIJ1ZwYCoiPVOfpqnurUbJA1VAiNBwbzuq25KFGSI5onVaD-GlnMyO7TmHAQbTU_s_-7n5XMVIewglxLRKU12JRhAAkvRBNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/97969" target="_blank">📅 00:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97968">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4TWNCEKkG_V90QCYALNLPiLfepsIQbtsGLW3ljxN7SNNknf1wobG0eozsoihON08SGpPh8Tc7hNI9u5VL0g9pVSM8ECfv6eLzXhGqpqovqXDCqHNcaSROx7fOqthBRHIo5iTb0WLmXAOqD1IyiIg0QGSRX0VS3FMKaCIFXnmIfoLhavbb-xRr2nnz1lbfeS-3l6wJ4nfFGWUkebqER6J8CuG5vlCp5G3PquLvzCANbaGhzq1Te7AtdJJ2yesxCWGhKmtF8RAlUOAOE2iWhlQNf29Ol__mtEvF2RMp9QCglNiprjJvJsyY5J_oiv4_2QCAXRPesB_-e40G1jKonM1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
🇵🇸
🇪🇬
حسام‌حسن سرمربی مصر: این پیروزی رو به مردم فلسطین که در بازی با ایران از ما حمایت کردن،‌ تقدیم میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97968" target="_blank">📅 00:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97967">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c4UcqxgQ69Pek8t0T2s8BliB0e40jH-W6aJi4xGEvL5OYf2rEqZSN8OTawzNOJHrfGMxLnzQMecawQlmf2XDoCVx7TOlfPubxovrRp2BKUUxf6x1rWTYAjGE6TXlt2WhEhEwdOIsvVmAV7lcjmcJj-y3FxcHkh9gg9KrUN2bivXbZlDiWUf1YGSJkrGwzvgRh7IPJRirIgUWvBmfGld04nxk5ZpxwLR8v_jbLO_bU4d1VOuWsgrZoQGE5lKQnfucq_1yyZl_ENOvsSZhqhoH7hjmSXLcVt8hvoKa89Y3g5iCBPQYz6iOe4bz9guZSalyZV7G6iA_NN0va7u-9yJ9Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇬
سرمربی تیم‌ملی مصر: از شخصیت گلر تیم‌ملی کیپ‌ورد خوشم میاد و دوس‌دارم باهاش در مرحله بعدی روبه‌رو بشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/97967" target="_blank">📅 00:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97966">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووووری؛ در صورت تایید احتمال رعد و برق، بازی حداقل نیم ساعت با تاخیر آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/97966" target="_blank">📅 00:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97965">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇷
🇨🇻
#فوووووری  فیفا اعلام کرد که بدلیل شرایط نامساعد جوی در میامی احتمال داره بازی آرژانتین و کیپ‌ورد با تاخیر آغاز بشه. اطلاعات تکمیلی تا ۱۵ دقیقه آینده اعلام میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97965" target="_blank">📅 00:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97964">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇷
🇨🇻
#فوووووری
فیفا اعلام کرد که بدلیل شرایط نامساعد جوی در میامی احتمال داره بازی آرژانتین و کیپ‌ورد با تاخیر آغاز بشه. اطلاعات تکمیلی تا ۱۵ دقیقه آینده اعلام میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97964" target="_blank">📅 00:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97963">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pq_DkJrpsRhDOyAQmtATK3-bYvtI2ErzllSbezQaLfJXy5K2wUk6NXI5wYS-jX7xnaAUv8whJzM76sMLE_ea2ioR5LRnBk9sS0M9ps6KRVdSg8ofkMW-jm48_Gv8JuARdXdTHqQrLSZdl1ux6279UOGGxet75UhyrokMxPeRgiEb-5ur_3VqN8Y5hCUX2ku66uIQXGYmdivd0ZtPItQhxcw3NsKHfrz94lebUR3cV5k3xF8AbQbhUqLo1Mljt0t7-sD9wCg6mfmf1maG9ICqHJhVP3E2QfEJ0uyfs_rQssbiNOtHYURF-XQMsTz9NGsp9jUgD30sZumiQUw9nI9xgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏
بازی بعدی مقابل لیونل مسی خواهد بود. نظر شما چیست؟
🚨
🚨
🎙️
محمد صلاح
:
"نه، خیر. بازی با آرژانتین به زودی آغاز می‌شود. ما باید به حریف خود نیز احترام بگذاریم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97963" target="_blank">📅 00:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97962">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🎙
خداداد عزیزی: از کادرفنی تیم‌ملی خواهش میکنم از فردا نیان کسشر بگن که صعود نکردن ما بخاطر حضور تیمای قدرتمند مصر ‌و بلژیک بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97962" target="_blank">📅 00:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97961">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPfwu-rcf7aitD-6VBJkZ8vijm-bqjMTDuulQWhEDCIN5AZienaNkzo0oXEuE-lymzHFxIWSx87DU1mOcBPVokFpWaX5pw-XKg2fbnf5DpJWYjCoWvjR9Dz4s6OCzglIZErqFZxexJlRJxZ-8gCeQdrO5bPmYp_6Im2oyOaa4T4ufBMC9V5GkOYXNsL_tGczAo-E60lwrfvxCuBrtzK2xtucv0v2Rw0ALB69Be0eNwO9NftKnM06uFdCY6tDk3gD-RzpdeAZdwLD4ZzJccs8cs-8XWv3TYVutWqHsk1Hdjhb7QCe_vPsAJrcBNFnIi-WQGenwhTJ8P5xFJVFe_XPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇨🇻
ترکیب کیپ‌ورد مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97961" target="_blank">📅 00:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97960">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8RVUJumE5BKU-TfpTXRNLhAfyu72VT4q0xSar_FdLBfdcqWNIpXsydQmxAys7AheKUSyAb8QlNMp8jN3i7G0WrnSwbePmoO2h26H-de9_lTrR40GMF4ZQtRU6UCPFIVEKSE8YYYSzzK2UCgKKVqMqYuB-FkVT7dWCsqiE15QgKgsWgxxXR9S9lrg3-5-rQX5_G-kQqu43DPnFc1yafz1VhH5w9P55RbaPijavsXmsFav94jJi54a5JKOaO9TReor5IIJNbrnokQTe4YRHPb8_mFV08DodDfgOEOkwRNwpjoysrpZURO0B1TQM7xGTT_Jm6wfz-6i2fLBADORAwNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
فرعون مصریا درحال گریه کردن بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97960" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97959">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sciDKGLZrtfzTE4VODTIVyinD-fcCSNdHKyDNaEHcOvGX6rYHbGCvAzO-0llQePMaEqzS-BwFH0MvexCF-wn6BmE6Et_SEuVOcg7ZMHqiV-9txHECE2HZAv1Rxdd1NwfLOsGYka1PhWm6ps-dqdsBgCmuc0tgYmbtyuKqRYQXuXt_Sdu_Hy-zbwyfODM75du7wMCRmj_D8Rtwt9t-wQai7ihoR7ru87JHPe7Ew-aiy_L7IDkKwuhH4ivNSvRPKJDwI5c_4mIhoySYGJrGL6hXORcM85XDNfHd5VIsLF-gatSYK5UOIflC3JDlCvcD14Eb3hpsFRWEDou-eIdcpX_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚠️
بهترین تعویض تاریخ جام‌جهانی؛ متئو رایان وارد دروازه استرالیا شد و همه پنالتیا مصر رو سیو نکرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97959" target="_blank">📅 00:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97957">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NVbaXHVrsrgXC_JLRa626tZuit3paV5xbEURgxGw92kOI9JSnN32LAQAvvNRK2RJcMUMrNIb6HWiPl7iwfCAwQvuqWeEvqeEOCfSP_UvaufdH2qENS7H7OpYkXzKYvtKAOBK_nlKOvR6etoUj3V0to-4VBGS-_vIDM-u9Rs2Tnz9cUA8kz9FbvWY45HpZtgucTydhudXT9y3P3wiwpBeQObmLH6lXRH7l59TjJvfolMlqac4GtxpM77nM2qQw_Rmd_zUmnwHRYkpDrm46Cb0ixnX6OSJDz4PYuQgkgvUrF3XqEOzWujuX6mwgc1ydQg5EjENgVfypc34LC9qvdK_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lc2QBvbMlXVmpWXKBlmlS7U9dUL47QuhB5fWNl24Cwrz5JQv5UTrJMo_DqSNwewEOAhzikVK-_6lAyPlj1DBhGgA5CTs6j3XlBT6F5RL34aXwiTxyB-wp8PLfpTdMOoMiLeL5XGgONbSssTQ5XhQxlvYvy_pUVJW4BpF-T9kGbg4r5tIRzbFdklUZpxpDVN-obromdFHqdq_nBVaDoclkP0Se2RSLoboYiWrmcjgjS6YyBkTPIwnz1lahrAGFqAsURdvvF89KVXJit-wT-MLvuBdncaLfUiaBgvRagghbPnuTgBRw80TeObU7q9IZZTVVsC4XG2bCcmODEDxCfwqJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
اسطوره مصمم و آماده وارد ورزشگاه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97957" target="_blank">📅 00:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97956">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔥
ضربه چیپ‌دیدنی محمد صلاح مقابل استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97956" target="_blank">📅 00:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97953">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PuIrIloncGfNWvjhShTYwej4JE0fwsVpsLwNKd2vpoc4fi98bUlQCUJpmsAEajJExeYnWLGT9FKaH4cAZsSVYqf09YQG9FM17nhPt9RHUxB-Cczkh_u8lSHbR1lhMbDcZHp0WEqbxmwE9FETtzq2-W3lMaCzPDkdhJfgRPZ4YR8cnTpECj8iV0jkGCZjoDjb-LI0jKdY4wLoWp1CwuP-aV3WqBIK_VbaUHaQFRke-GlB1Bgt4Ew2GJHurGqcAoxdNr5UkOqCsDLhyN7mdXTfbRRhQzUBnzodCz4B-5tx6NKrn9tEHSoj84wUL-y84QkVZrxYuw8k7-LcZ_gnfUNyqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZ-XN7nR-0XnVuJzNe9yXRA1AYatVrPgQZanu2qY1RSME5S2cogVdypQG7znGGCIKp63vbbVY0oEBvGNpC-8aeof5yd0QMyN-fCicV5mDLffWMpPsPvZOgw4x9-3B7cNDLApeMDE6hUO3W9guDVcUpHPC0_UsHivam5oWr2gSW7uj3jQsmgRguH9p--pIQ6EF7En9QLhdvAiHLPzzcdPaEszmXCw5s9V_9VGbxiu3kZzfmEO0550vlBHRBI8INKRTytXIciQ2wO2ElzTepXi8IY5Rde4F1CKsU8nOeaiQHH1DJEm-Rz3LvgTVFy8H2g1oSCJusyQhcEbnYB8SljKuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
برنده دیدار آرژانتین و کیپ‌ورد رقیب مصر در مرحله ⅛نهایی جام‌جهانی خواهد بود
🫡
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97953" target="_blank">📅 00:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97952">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6765dad0c0.mp4?token=WhJAmCeou2wzQVeIf0Dr82fV2YR4YLGnGNB-gG9n5S-vX5IHPco3-lN_kq8IJZ7ALt-gy5dDvSHBw5yAXqu1_lREgJYYavOjOBVwhd_FngSu65EjBwcXRtgl7p-50gkQzTuyTr3fyvvEmbtT2CFDsK4bG6EJb5h9iDYcwy8QXvukd-QaUcz7k-eJKpgwQ0bGQpSf2LfVasLC1_FyFI9vrgtGU2hx9nKJZW12QzaA6y4s5e14yYkYbw3sgw9ocKf0m5EHnSq2yxp6SFvkqXUd3b-31TpMq7pWjtvOrluPyEkzxhG_defUoO5tZ9_4oVMfkE6211lC_KeSZVXKxU6ZmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6765dad0c0.mp4?token=WhJAmCeou2wzQVeIf0Dr82fV2YR4YLGnGNB-gG9n5S-vX5IHPco3-lN_kq8IJZ7ALt-gy5dDvSHBw5yAXqu1_lREgJYYavOjOBVwhd_FngSu65EjBwcXRtgl7p-50gkQzTuyTr3fyvvEmbtT2CFDsK4bG6EJb5h9iDYcwy8QXvukd-QaUcz7k-eJKpgwQ0bGQpSf2LfVasLC1_FyFI9vrgtGU2hx9nKJZW12QzaA6y4s5e14yYkYbw3sgw9ocKf0m5EHnSq2yxp6SFvkqXUd3b-31TpMq7pWjtvOrluPyEkzxhG_defUoO5tZ9_4oVMfkE6211lC_KeSZVXKxU6ZmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
ضربه چیپ‌دیدنی محمد صلاح مقابل استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97952" target="_blank">📅 00:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97951">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇪🇬
تیم ملی مصر به مرحله یک‌شانزدهم نهایی جام جهانی 2026 صعود کرد، و این برای اولین بار در تاریخ این تیم است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97951" target="_blank">📅 00:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97950">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE8cMnaDTQ6iQBNmypDLAdibYzz_oZ42J7aGIw9M4tX6e6Y5vsPB03BbUmpN5pKDsz34ozZwCBsQ6aoxwkHNQ1LhJXlGy1QmgT4JA_KGa5kG_X3opAA0okG6MWPweCfgJxd-_fdFdKiWW_keE72gw_8iAXshq84jhnI3_YkORYOBj_6NVT8bvcGnWAhyFAE74xLJnKyfTENS4fkxJJK87PtnoPMEtKJSSqFssOEaHaqqnWsjuiJ8gGih4666o7ojF8BJrT4qm_SbaG1-LT9tfASTrnjzOEAI8y0VFWSWXElBbeot6qx93JsmXVRcXggAlN2mad1_skHK_X_LI3Re2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
تیم ملی مصر به مرحله یک‌شانزدهم نهایی جام جهانی 2026 صعود کرد، و این برای اولین بار در تاریخ این تیم است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97950" target="_blank">📅 00:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97949">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بازیکن مصر هم زد و تمااام</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97949" target="_blank">📅 00:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97948">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این قیافش بو ریدن میده</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97948" target="_blank">📅 00:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97947">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این قیافش بو ریدن میده</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97947" target="_blank">📅 00:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97946">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چه خوشگل زد</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97946" target="_blank">📅 00:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97945">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گللللل مصر صلاح</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97945" target="_blank">📅 00:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97944">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">صلاح پشت توپ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97944" target="_blank">📅 00:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97943">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گلللل سومی استرالیا ااازد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97943" target="_blank">📅 00:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97942">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلل مصر زد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/97942" target="_blank">📅 00:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97941">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇦🇺
❌
✅
✅
❌
🇪🇬
✅
✅
✅</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/97941" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97940">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گلللللل استرالیا زد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97940" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97939">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلل مصر زد</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/97939" target="_blank">📅 00:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97938">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پنالتی اولو استرالیا میزنه</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/97938" target="_blank">📅 00:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97937">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پنالتی اولو استرالیا میزنه</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/97937" target="_blank">📅 00:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97936">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بازی به ضربات پنالتی کشیده شد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97936" target="_blank">📅 00:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97935">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMbKz1VZ-h1ORY6FtQrm0NE543OJB2UVgQSWPBVuqCAEHLTR_CjHWlg4sVM90-LTMAB5edXr4t8GX8Y47dfytIULhCWWySQx9AyUIsEEjLvulRLaeqdmWojiO1Ceo-WmHukokSaT0gO5ssOdkuIBuMewvXt7SnfceYKhRDNShXce00lsQMnWBr6yuR8GDj1PgneA8uA8Vo_ivDTooT0sTDwW_avwB_KoXcRV9aAYh6aIx0KXNC8X-oWQVvQmF5onaJiLdPEhXq_a5XcBo3HNO7ei_b2fX4Yyq_5b6Tp-cthwNjz2z0iSVjBhSlO7mRn6vFCxnD7Hoe04JiB9vZLC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
ژائو‌نوس و دوس‌دخترش بعد بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97935" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97934">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شروع نیمه دوم وقت اضافه</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97934" target="_blank">📅 23:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97933">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS8-qb00XVTPxTukDiZRn60WlmRRa-5a6U9u19NVOliGTfuA3ZN_6UA_vuam976qilN6j1IkZQoYQRF-Jtk4KXn6_gr_mLoSJuFc5HWNzVdtZfYFTh8o3fhiH1n-ap23e_dI20WCVOGeg24qWs26u0yIdhk4gVh0Zlw8OraSII2Ruoy0GU0qfRYWgXl6GoAO2XWY8TFlzacVdDWM3ZdNLGMQUzBH6RNjp7bmYauSNnDEqNskZAWj6BaMyESroHMpTx7QEe747SAbFVh-NvMBBl_U41EP1xtEj9l_CepH2A27EJsNG-OGKTO6JR2KmrhGmPHtdGsiZTQxxeaKmnaR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیب رسمی آرژانتین مقابل کیپ ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97933" target="_blank">📅 23:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97931">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بریم سراغ ۱۵ دقیقه اول</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97931" target="_blank">📅 23:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97930">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بریم سراغ ۱۵ دقیقه اول</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97930" target="_blank">📅 23:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97929">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9537d57a20.mp4?token=Uf8wG7vLJLNTM_1vZ2w-XhicbD8hdviGAITeJ9QYW_jBA0D3PVDJwYmk32LwywXbAz52uwwtz2w_mq3XOYK-QNK9dtp3JR-kwX-1FRV1j3fejMOdn0gEWNqr5qWW6G3GlC-lgCgw7S6Tp4LHJ9D2FI5iYhvqOX2MRo1DJInaxpJlJC_0vF2V0a8gm5DqAdu0LXU8npZRMOMQn6qQxtLceGhH-mqLzgYJIl95X0j7XplvHbkSnnixd6-mLL-BwmgxrKh8jWpDjqaCXeQEZ2zvQORDaiSS5bSSeSi1oj9S-5jOtw0qLeMzdFfilj_VQLC3hkDFpfXTJGg0K2GSkXxsYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9537d57a20.mp4?token=Uf8wG7vLJLNTM_1vZ2w-XhicbD8hdviGAITeJ9QYW_jBA0D3PVDJwYmk32LwywXbAz52uwwtz2w_mq3XOYK-QNK9dtp3JR-kwX-1FRV1j3fejMOdn0gEWNqr5qWW6G3GlC-lgCgw7S6Tp4LHJ9D2FI5iYhvqOX2MRo1DJInaxpJlJC_0vF2V0a8gm5DqAdu0LXU8npZRMOMQn6qQxtLceGhH-mqLzgYJIl95X0j7XplvHbkSnnixd6-mLL-BwmgxrKh8jWpDjqaCXeQEZ2zvQORDaiSS5bSSeSi1oj9S-5jOtw0qLeMzdFfilj_VQLC3hkDFpfXTJGg0K2GSkXxsYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
میثاقی امشب به سیم آخر زد و شماره موبایل اصلی خودش رو به صورت کامل روی آنتن زنده اعلام کرد تا مردم بهش پیامک بزنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97929" target="_blank">📅 23:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97928">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🏆
پایان بازی | پایان بازی در 90 دقیقه با تساوی؛ وقت‌ اضافه تکلیف را مشخص خواهد کرد.
🇪🇬
مصر
😃
-
😃
استرالیا
🇦🇺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97928" target="_blank">📅 23:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97927">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWn-opKC9bfpDks_LZW8g52aWGmxpBjNfO1EdtBMF4sLXrAbuVwjYQ3DyV5GJOXn0dgTpr_N87PMZIOa0bcRDeivH3kATabVe89ylIZzMiKZSjAbypM0C2KlbG5D0_-SPoMU9vTvYA29OM9ki7KgbjzWS62Oa0elV2NixPF75A70F9FoZtVxiYziQ10CBbxvVN310RHiA1ONMdo36AXkZL2cL9gRTDrOb6EvsjNlaE6YHxQUGqLUyqIrg6t4OEFb5jZOT6jbf9IiAd5ML4vqOpGZmdV7PtubN2-8UOg0pVtA6YyIr3s1ZdR9REnBPCSTrfFxDW4dWUfLwpOoE98clw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇳🇱
❌
تیم ملی هلند تنها تیمی از بین 10 تیم برتر جهان است که از مرحله یک‌شانزدهم نهایی حذف شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97927" target="_blank">📅 23:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97926">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B07qjCPnt-GX66Jy6ZOaLp79bAB-zO0U0euDZ2Ym63lC74CUEdAuUyL3a4F1gXNCO13R4loLQRmns5C8NGcexeqL5UZP2BdBuxShXwuG8ENjXCk6IVwdL29scHIkrW7buDdacXk5txKllhlQxyNPoMuxwxqHUaeCT0PrA13vxx2oSTj3CX-qXiBVsSdWaA9r2-H9n-e1Gml8uNyCtkQSszEbBEJziZieLmPZ344zD-G9zVngI-EH9YpOrYei2lkX1467c_QphtyeqCeB6huWlG_B1aJLNL4tc9ocB8rysceZvD-LQ2hDTVx7SWqcd6CJP51hM1m31kfExbB61RQGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
محمد هانی، اولین بازیکنی از سال 1966 است که در یک دوره از جام جهانی، دو گل بخودی میزند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97926" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97925">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d324a1031.mp4?token=T26qRO9IhS2neVDuIQ8xudlFuzN5oApSC_syuZ6TbwuudtEEJHxa1TDycDfrU3xE9ruE6E-BBlInvmugcpb_QFQfSnJ6MddN5OxavI12RCg1SPI-0Fnh12PZtVMHCgecP9pZQBL2yafH3kDuA1z6XdHY58eW1pk4CZY9RBZpcc8-xcULpEArqTJe7cbt5ROEoerjo4xx43HoROFGPza9pcxfCuzffjJtz5gfAgpvzfWl0YsoBVEXms5RLzhG7pNIaa_7a5Tkwsuux7HEm347huCbHRKtPSNCBSzWktlKE9ui5UYZCYhOdnB9aQPz16PUCKctpbLarYRuUcYSnGjqtncqtGrN-n_4hWt6ExNjPr9w64Dgsqu6KJytvRyuRvy_l-8S305Ci07oBkSWVz0qYYX3Kfxxy0UwoDa8BmHqTuTV27xyBhpYY6b7NSkkvney6ZrQusIDHxohK64Dp1XS5Y9tIlQMG4ASo6mQIoCrViemiGpBwshFdj8LFOQjnFJWJwWsUGpTPHVMGk9Xtw74cMyoYova12tP1T3hrxXwakr2qmrm1mezWCjahRkI70D4o8inzbJbRh9cvnFNoCVcgImOrgNt0z2qrEAQ210T5B8LABa_GQemlzZJ240tGm5mg3oyazKIH8OSm1Z8seaWuhEPDE8rlddKYbijKXlcdXc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d324a1031.mp4?token=T26qRO9IhS2neVDuIQ8xudlFuzN5oApSC_syuZ6TbwuudtEEJHxa1TDycDfrU3xE9ruE6E-BBlInvmugcpb_QFQfSnJ6MddN5OxavI12RCg1SPI-0Fnh12PZtVMHCgecP9pZQBL2yafH3kDuA1z6XdHY58eW1pk4CZY9RBZpcc8-xcULpEArqTJe7cbt5ROEoerjo4xx43HoROFGPza9pcxfCuzffjJtz5gfAgpvzfWl0YsoBVEXms5RLzhG7pNIaa_7a5Tkwsuux7HEm347huCbHRKtPSNCBSzWktlKE9ui5UYZCYhOdnB9aQPz16PUCKctpbLarYRuUcYSnGjqtncqtGrN-n_4hWt6ExNjPr9w64Dgsqu6KJytvRyuRvy_l-8S305Ci07oBkSWVz0qYYX3Kfxxy0UwoDa8BmHqTuTV27xyBhpYY6b7NSkkvney6ZrQusIDHxohK64Dp1XS5Y9tIlQMG4ASo6mQIoCrViemiGpBwshFdj8LFOQjnFJWJwWsUGpTPHVMGk9Xtw74cMyoYova12tP1T3hrxXwakr2qmrm1mezWCjahRkI70D4o8inzbJbRh9cvnFNoCVcgImOrgNt0z2qrEAQ210T5B8LABa_GQemlzZJ240tGm5mg3oyazKIH8OSm1Z8seaWuhEPDE8rlddKYbijKXlcdXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇺
گل مساوی استرالیا ( گل بخودی محمد هانی )
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97925" target="_blank">📅 22:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97924">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گلللللللللللل مساوی استرالیا زد</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97924" target="_blank">📅 22:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97921">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گلللللللللللل مساوی استرالیا زد</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97921" target="_blank">📅 22:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97920">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJt-FWGp9Yc6FHaDuTot8JVsHcuGVaC9J3cxHvJatHN-S0yrJqAngOcxJQkIZA4o5RiaCpGhc0ZRdUFf2QVUb7yaNgHqKKpkKWLaaIG1lsIItUatEqnJAFTeZoCfbyCowmVdsWhkxZ2aj3NIu9KDVbCuzCq9IeeG702MN1_W2IDrYaJ54YhZ5aON-ag2XM8k3Ypy34HZMMFQzfCccU-EyXw6Iyazz7-VsxRv3P9vypzJxw6nJ6emUXTplsvG2gxLQqKxVapYsSMpRVtnnknj27n2KbzE5PwHS1bGvEZttT3AACVNZj6IZiAzHV5zSANGFf2g3vC86hAG67h3WxZ1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرموش اینو نزد.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97920" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97919">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFNAiZteR8ZhYNkQ4YZfxafDZDIm8KS3DMJ_juFsZCcW-pbckJBaVtzx5e3QoFpQRS3UluX-7Uv-_2R4S0H_RIpGzOWoZo7T1lF0KD2MSsbUcjUhOHyyq2JS2qR5Jrbd10S0DJmQScCBU9tWJt86R10JzwQ9lBJjSKWWn85mfjljYzVKK80vah7mmfdvA5iwXPUDKNvnOO142SViNeXHw2Ec5UAn1YAp0CKNLX_VAmwwmNgNv-9DsyYyTywxs7lD4Mch5D35Ukuutt2cF2qEz8PFhoYPRdqMPDb-VU1xM7LeiMuVhWnEzJUvtPhGx5YWnsbUEWHwOs8p0QWrvqCO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هالند تو اینستاگرام این کلیپو لایک کرده و برای وینیسیوس کامنت گذاشته:
🇳🇴
هالند: وینی باید این صحنه رو بازسازی کنیم.
🇧🇷
وینیسیوس: خخخخخخخخخ
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97919" target="_blank">📅 22:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97918">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxREkjHfDh2gdEeGFLbKMZEV4fhsUFfxoCSccH9_aKi2lDvrMZvULtsclIblPKd83tRmJs9TvMd0YoiU4sefL4cO2m2DOlTuSxR2QXz_zp5-tJ7Sg5XAjsvBKsQymxpizxYmElx1Y_VMtcSQlETaZQtbU-ap-aDqI7B2cYhOQbXZZLyrrL_lEn5ea7Y317YjOoHLX1PLSgK6scsHMnsfi-XqQMqiFFEuzx8E2s_doyDEwTGrcMUyA7rQI1dAYLvKYVoSgcGEPFltoXGUGosz_YLn3NSnXxqzNjQe9zx9AMiXhlR-FolpPwb4e6DpTDroSxwQCz5kyvf4hk6JdmQkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زمان برگزاری مسابقه بین مکزیک و انگلیس در مرحله یک‌هشتم نهایی به دلیل خطر وقوع طوفان با رعد و برق تغییر خواهد کرد.
این مسابقه که قرار بود روز دوشنبه ساعت 3:30 صبح برگزار شود، اکنون روز یکشنبه ساعت 21:30 برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97918" target="_blank">📅 22:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97917">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRs6kMBEPMEHj5MnDLQ8ZVoU5BUoapWV5IB9dYgqIrweOPxXqPs8YjeuvCeUlSVcf2UrLitZHsQI7kSQjAud0fD8M2OzfhVutQNkHWGvviZ7_5sMqCuuRISeiiJg3jdSTcm2b3t9xaJbk5LhDgiRPm6s844uUS2dO0qrg4ztA5Su_OyB7iV1FR4BXEApZy78W4KeJwPaK-uHBP1HC2u3Lvz2mkD_TL9o9w9lnttlo3PDnQrGmJFaQvDSugLhv9Z1ettKB6zvFEBZq7Gfv1WdJR_bdKte9nWkNMH3MuJtC51fKFrkVej_u4sl5d18GiyprjszrwZX1z-nsRh58ZO5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
امام عاشور پس از محمد صلاح (3) و عبدالرحمن فوزی (2) سومین بازیکنی است که برای تیم ملی مصر در جام جهانی دو گل به ثمر رسانده است.
🔹
او پس از محمد صلاح دومین بازیکنی است که در دو بازی مختلف در جام جهانی گلزنی می کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97917" target="_blank">📅 22:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97916">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پایان نیمه اول
🇪🇬
مصر 1 -
🇳🇿
استرالیا 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97916" target="_blank">📅 22:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97915">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYKzugFDGalxJBSILInjWsoJYVQoa9tCIUUXhyAqRHZnvQduyraCdpp-f47KIiKTbA_QR6CNeSa6nj8FWXUBnWnMg3YBghFWuyB-8SZuz3j1n0eps_AX3qrmgDjstoj01d5vdO-cRq0PhnUpo5PkTXUVXDod81wOptKxb2Pn-BDrMbcB_TsKjsHCU_f6E09dvnmVclYVJnnxxtSDf2pUZpoR9qZBbMn8U5MiYaSkupUYE7oO9MMe32l3Du129TCJBK-vlHW4uYYrcWMZTgiepPLiQ_DCjuAMfXJ_0M_7wUQfMKpG4E8LHcu8iQBy-r6sE_l9Z4Nux9BuC-fa-O7gCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی اسپانیا برای بازی با پرتغال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97915" target="_blank">📅 22:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97914">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lbfbd3G2qmlgplhQQGr7dljO2EBwD4DgiX73h5g-1EP5cH02s1zKAVWig5UBUJboYmYH-ri76brH8Ps-MmP4bjmSNuGimltuznu91L_36eSa5t1rTwz6o42sppFJdx1y3A1Jd-0xIC22LiX6dyo-p7ALmcMD9TTvLJGhzM2C4zOLJ7XkQucaa28oN1iujNTa7-TEi3sN-iYIe8khkCk1RxknYQypq_U4BggXgmcyYgCEktWKXeyQwOUY8nu-nBFErjD2vvX8q18tQ6pomkCbT0efsky4pa0iB1wvkNJ9cbKR-A_QnGM7AlLKOmUysoOqf_rALxY1Isr8VRiMmZPQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سرمربی کره جنوبی به دلیل تهدید شدن به مرگ از کره فرار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97914" target="_blank">📅 21:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97912">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zd0iHZcZWWt4wMzSFJVyW7ZkZzZgP-VmbcW2y10uuf9WL5vsuaCfykeTFG4cOPyjwWverRD9eoq3qB0hLMWiNp6pupgKJr7faWcjZz1eZT5Qtb3zaX9lFCrMrOdYiyCZIpiS7j6NxJ_7f2P0COQPfvEtqZrBu-TEAS92xpAT5F_iVT8Y9o6nIJ7pdgYL7IMNN_jD88dOrAT3MN08Kptl9QViO23VyT6GwkxNexwU2K6HvUspSOIrao_6fMxfYbxMd-9b33NE5qix9VrwMHoZd1F7BBqCdA0hfMpIXsh2lF4d_GPOQKSbZptAoppkE4kWx_DRQc5S-yfB_OvsnmKJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4c7wigYxVOjgxIPfquli-YOsc_qF6fcorT53dqCtKrjvWLmj2v30sR5bBx8ZMsUgyB5CszqTExHv5y7uStMBg6Na0YMBjAYsdIRGCEQzRCCuaunBCLLTiyXtWaY78Y5MtrZh5qixJY1UGCGxdwxXZ6SBsnK_oYds-m75nL2NBzV3CZaaYoL4ZLcjucP76z-cpE6yPUaKEgm_6SUR-Tzlj7bCENdSryMizaaer8UdZlmliBFddLdFHkte8WxGeE_30Arqu4WWKBLJXhwvk7GIvmO1D0wqkKOmLOJqsVg8KR9hDKJmp684vT1dL_52pKFunU9SugLdVdzOETLPIGr-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🆚
🇨🇻
🗓️
۱۳ تیر
⏰
۰۱:۳۰
آرژانتین
🆚
کیپ‌ورد
📌
آرژانتین یا شگفتی تاریخی کیپ‌ورد؟
⚽
🔥
مدافع عنوان قهرمانی برای ادامه مسیر به میدان می‌آید، اما کیپ‌وردِ شگفتی‌ساز بدون هیچ ترسی به دنبال رقم زدن یکی از بزرگ‌ترین غافلگیری‌های جام است.
👀
⚡️
آیا مسی و یارانش صعود می‌کنند یا تاریخ دوباره نوشته می‌شود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97912" target="_blank">📅 21:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97911">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2fa6b65337.mp4?token=nOWqkQOnzmLpx0lOrpHev6mPo-rzauDB8NORPQxX7nutEL_DCcgheCHW12Lk-sL8e6KYYJmajC3us-21ROKvOsF-51RYZwDxuYL-UFnPj8M2nWtq3ic4R77r-Q23vV5-12n6AH9rOW3NNJNKRnGruzFD-uROQ0TO3oQYfqO3N0EpdkZa5OwFOuP5hxz6DSQ0WAzYQUKA6dH5x7yjr8GpFrfsXkjqGzfJIbdO9Xa89hTn1rizLaUr6apY7KX8VEZYFF3lBM7p23AjJ4JcrFys-zjPt7KayL0vYHX1vamSf065c42O_ALkXm1wTlTonzSBnyPkHypOUhmUPFtJ9HIl367uYOjW6HJMDBXVtQYwitspowIw2tYwzTvadkl-R71NYlimylWEj6xEXa9ouqblCAA_1u9NZxmzjNmU_xqmbbZRZJRHWkUk5aCymV9_MkFEkj4kTyD2LRZOfeSpEZxRA1TUhKmrW7g_AbO_-lZbcrA6IHqUbfzlOYwEwGURJnaZAU8KhVtp5KsxoL6LQawZTlNZv5vEpj5Zz8KXFQhsCdFZBgMC5LXGOYw5NLHkefZyAki1ou0OvF9_hQCn-eSHxaSv2EZ9pMlFeWOFGGhmQOoo3n_WyVJDUgueRW2q2uq9gHKNif8F4X5XcrcBEiyKfcAn3OiY5UHRqLn-VKW2BCY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2fa6b65337.mp4?token=nOWqkQOnzmLpx0lOrpHev6mPo-rzauDB8NORPQxX7nutEL_DCcgheCHW12Lk-sL8e6KYYJmajC3us-21ROKvOsF-51RYZwDxuYL-UFnPj8M2nWtq3ic4R77r-Q23vV5-12n6AH9rOW3NNJNKRnGruzFD-uROQ0TO3oQYfqO3N0EpdkZa5OwFOuP5hxz6DSQ0WAzYQUKA6dH5x7yjr8GpFrfsXkjqGzfJIbdO9Xa89hTn1rizLaUr6apY7KX8VEZYFF3lBM7p23AjJ4JcrFys-zjPt7KayL0vYHX1vamSf065c42O_ALkXm1wTlTonzSBnyPkHypOUhmUPFtJ9HIl367uYOjW6HJMDBXVtQYwitspowIw2tYwzTvadkl-R71NYlimylWEj6xEXa9ouqblCAA_1u9NZxmzjNmU_xqmbbZRZJRHWkUk5aCymV9_MkFEkj4kTyD2LRZOfeSpEZxRA1TUhKmrW7g_AbO_-lZbcrA6IHqUbfzlOYwEwGURJnaZAU8KhVtp5KsxoL6LQawZTlNZv5vEpj5Zz8KXFQhsCdFZBgMC5LXGOYw5NLHkefZyAki1ou0OvF9_hQCn-eSHxaSv2EZ9pMlFeWOFGGhmQOoo3n_WyVJDUgueRW2q2uq9gHKNif8F4X5XcrcBEiyKfcAn3OiY5UHRqLn-VKW2BCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مصر به استرالیا توسط امام عاشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97911" target="_blank">📅 21:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97910">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مصر اولی رو زددد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97910" target="_blank">📅 21:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97909">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97909" target="_blank">📅 21:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97907">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGRJnivT6ZPouTYkEfdxUvtmMoPJm7SLblfAgFyjYbRRJwLGF7yF2WmHxCUK2hcx_9jxpPdUaj5vHR1vFblaNhlP4zcL0lFIcCcUolc-su2lVynfe5cN5wFUdAOQoItsCq-hJ4PXXEMi0BahZ15vSEVx4VcebAlhDlS9cb3PEvfOexcvFz8uRo4vGI8eXs6Bl-a_nH_6jWcU9mg8KkxXyRI4fQR6dKQ1ovd_efrask03h1nFnpXa_JQy0xg7mtyaOQDOTZgkjI8-cXxu1oG1c1ZTwR4QiqaGiWGnlzbH5toWY7VKJKDgeelAWprVKZuut6vCw-9jRp9h7TZlViN7ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVnWL_K_pENGHqYk9_6AeatSrzLGh9zxAGRamvpla16mmXlz3unzC3JAHNsUEQAK2X-9PUVhhVbvZuitDxl6LZryfhXauVOBmh2q605S6SqIgjL4gD5e_bUG3lJ2oPtt0__V52cKP5OhA0Lm8Ah-F9ZhzWz9WfVFzrzy5IRJL9gg4oaMioy7Wm-0iSq8L9qHJWjgJKbnG5SR3c2TzbEYW-v9C4hyNTsdaH8kyeDAntYtI_1yG87405AXZbRZB_lsB7IxyaIWBzV6sJwuWKT9-w49X0sCeVpnjuFJ_0bNQqaVMl-1oDQSXTcG-xb7TGC06oVHbNzyigTE0HEerA_Jmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری - روزنامه "ذا صن" بریتانیایی:
به بازیکنان تیم ملی انگلیس اجازه داده شده تا از داروی "ویاگرا" برای کمک به مقابله با اثرات ارتفاع زیاد در شهر مکزیکو استفاده کنند. این دارو توسط آژانس جهانی مبارزه با دوپینگ ممنوع نشده است و به بهبود جریان خون در ریه‌ها کمک می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97907" target="_blank">📅 21:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97906">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQE30nwc3RseaQrbzde1aXupSNbcygbjGgMmvcwe1GVDC6x3Pqj7wsI6y7hNQBTCCofMZIm6dvnWXLbf0e05BitsOpWVDnPpPFSteAhE0-S9D8IM0hnRVfoNT7nv6cVY_HgG7kpW5uwvU1UzMwzQL2U5rJvxCgG7Xk1bp3ZDYfuN17j8K12DdCzmmI5dknKMg7BiAi4kO887dIY9Jvhq0CTmroDA7Lhb5bNX_M7__7KK76gPouniUDgyhYUTdNEJCdkgGYEQv8opdtMy5AXjJfuYul9rPFO1NPUecBtkBP5DEB7ZtoMt0emZQXCdQ5spMUJCQp5zSk21O08NHgv1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇧🇷
بازگشت رافینیا به تمرینات برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97906" target="_blank">📅 20:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97905">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3dfc9e63.mp4?token=pH_eQ7-srJxAsl2bYwWfmfUbudYrNdb7dDF_C16IEckkaEQmiW39fox3ROI196ZRPTvGM2TDswILhf_qTIm13h5f__DghY-MMNBDlNI876ZQTORqi1erChexNiNpII2pF1HzNYyPY2WgCkkHfZsoveI_vYlj7lZdfQs8pH9thYybRLoOlxb1IslIupN6h-RT_STb8dgcci6tH3FxeHWZZ_3SVj9xNhkSdUNVmyMB6kFrH6j13F21FIRsh9UUsITbzlCsSBwpXx03cZjsdXT2RBVFUtUDZhNac1QVua64aHuZ6sITKU-TJMwIPgE8xKDS2tYpy8_OwBO9FimtGko_Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3dfc9e63.mp4?token=pH_eQ7-srJxAsl2bYwWfmfUbudYrNdb7dDF_C16IEckkaEQmiW39fox3ROI196ZRPTvGM2TDswILhf_qTIm13h5f__DghY-MMNBDlNI876ZQTORqi1erChexNiNpII2pF1HzNYyPY2WgCkkHfZsoveI_vYlj7lZdfQs8pH9thYybRLoOlxb1IslIupN6h-RT_STb8dgcci6tH3FxeHWZZ_3SVj9xNhkSdUNVmyMB6kFrH6j13F21FIRsh9UUsITbzlCsSBwpXx03cZjsdXT2RBVFUtUDZhNac1QVua64aHuZ6sITKU-TJMwIPgE8xKDS2tYpy8_OwBO9FimtGko_Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
تتوی " کایزن " اولیسه که راجبش گفته: «این موضوع از یک صحبت در زمین تمرین در کریستال پالاس شروع شد. یکی از مربیان درباره مفهوم کایزن صحبت می‌کرد. بعد از آن خودم درباره‌ اش تحقیق کردم. ایده‌ی بهتر شدن هر روز حتی به‌صورت کوچک تا زمانی که به سطح مشخصی برسی. من با این فلسفه ارتباط می‌گیرم.»
😒
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97905" target="_blank">📅 20:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97904">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdDcjBvlqDdZ7fqT_VhluQKyFyeOnuuZmB2elxHEut-0h84lbcX-DCVh9uQQogOvobX3LfWlkqdRNbS_LdKYyaJgUmSTTkJ1Zq6xXub50jQMiBR2eJ59o4oBO9y3h-bRGKmMkfmjNJ3cPhNPSsGLkjmJurDp2q8-i8Bw1h5y2VP8VWz9zan_blyjHv05j7rUMrvQ9ZWinhb1Dp_dHRdSn9UnG066dfjibfGsb2pSCl2Bdw2aRSSnYmtOyM69KGaPw31S-agy8op2sp_auUzDyC2i3yB2jT01p1KKtOwXAv5vQxsaPBw8M5Ye5mT_KGT4HU5o2kxf3a7Sf7yx7lQDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
علیرضا فغانی داور بازی انگلیس و مکزیک در مرحله ⅛نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97904" target="_blank">📅 20:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97903">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOqKMac-LY1aSJlxQ3yWH5iKS3tR_QPdZllbysh5OhyPZq3YbpImsjk9vlck1VSeLyiMu-v6aKQWviAKFXNd5NhRVGi3tQjOeRfKILwhorg1LoNtZODUGE1-widwRtO9DQXcHFBtA4EAesropfke9ciaRAiHkxhokCDO9O8AjBMy65WyABvrhPBdv9MWOdZM_JSQrLiZ-qjJ_vP3iLktm800F9XrxLhB4s-8YX-rihN-WTSr8dCfn9QCLwvqZwdYsSYqQCBb-OsDZsdBzTKb9artOE3yyD6g5ouSn5_oNFS3eW0fMJGjH6ks7jrfd2NaAJB3HLDcjIkQP7IAaqzRHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#رسمیییییی؛ آنژ پوستکوغلو سرمربی سابق تاتنهام هدایت النصر عربستان را برعهده گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97903" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97902">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-EqB2ud86gfw-3-abbxel5zjM6Y681ZrKMUXrUtkVuyGuOOeaTHqJ0isZawEsEQxUHuNV63ApwARVG96gpAeZc37pRsFys30BCZEHYAV7SPswC6LkFHIQROtOb3i53OiztNh74xM9dOcmfTytEteljeWvJ5yYkG_Rrc6X6PE5WASD8gSMVE5M526apl41dGYfsIBYoS9wr615qLAUl6q7G4r0fSiHuVIa7lTiaP8HpR_TJbL8I21GOCS5DhsNvi6XKBOl8RgjhHHo4G0aSQ1aDfTQ2PsVpsy5baSQP5yV0Vo0iCJgzCJThV6qCq11MyD_b5yTb6ebwdfPWoVJ_Ypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها افتخار الجزایر تو جام‌جهانی حذف تیم قلعه نویی و حضور ویژه ایشون بوده.
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97902" target="_blank">📅 20:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97900">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCsTzhBqcek5zqvjwPytxYoTS227ONOF1vphuMwwGeTz-49-o86QdvzpANrlmzGrHhI89-Lti76O4PDjVKoUQzPL31oNh8reB_YqUkZppTz31KkW77MmstziUIdRiwR9KEu-Vs4jsnyUplwVkci54jJkCOMRZn-eTELM2bX-yfvDdiJy9gVQJLuY43TcYyr3RHoBq0mvV8YAhKtuUDK_mQRgTtg1YMtrYsLU9vRRXkRHcs6YrQ5cftZflknivGZG6ANl4lvSIwLXmaPdBLWT9K6I0LvbEdIylea7FrTWOTnINRFFANZESvZC_OpEswf7WcmWo7h7F6AkgaIBRCMpVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bads9rPF5Pivujqw_MedzK-B6GG_K4QYPMSYwD_c81_zoMGnjEugf5N_cVW6M2hboJ1auZgeKY_FtbFFrX5qN_dHka8Cnwe5_b8oWpaxphCdB5FWAMSTAgr17ADi2li4Y3W25aJgYbaPyyygVgD91NA26ollOU60jVwpuJqiXHX5UwiQjcJBwDGiuZy_LkGFBUrHkunxuKLZ3LA-rIxF2q1PJLWhtOQlofdXvgNQW77SPs52V1ZOpCH7MktFP85EtSsgBQlNzSzcTY_QzUvAsYBICVo4c9E1xRd3cDm1wZjkLp2rAXEsT-hRZ9Tv3eJnmbAE7JzOxRP5pZhF9XsCYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇬
🇦🇺
ترکیب رسمی مصر
⚽️
استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97900" target="_blank">📅 20:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97899">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97899" target="_blank">📅 20:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97898">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gqR-rQ4Td6345M9ZA3ld7EuC4v6NH7tCdgs8xnCFq4w0ygNr63MwzpQoQb5DrmvFyiZcd49QCZh73QNLWJDCCoHyjRI5e9WS4eHBx26Fo9L3wgKut07umX32tTgh6zAdBec2rWLZuC-Ai0bRa2ptiGJ_2NqXfQPSQYOtsy8_tNJD--yudjaCF6Plp3o16IaiQx03234JOeRZIR8pAZk_ol3W-i_kT4mlEV8EB1Iz6_7QkC7sZ4W-UKC56J191j0kot6ib4KlxcWEIXDmJACqHYo-uah99qcouOhLr0NUEggOq_NS1u-GvqX1lYZbxu7DNqAg7lBVmyuDouZ1UQbw_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97898" target="_blank">📅 20:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97897">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZ2jqOOpepdZlir7xiKge0ecUA1mIt1goWFR4L_So22RKfLdBPt6X1xvpQx2JbtYOrW8nDXWBVw5n_3eOp7-7y9qUNVf2d8Qc1AvgJ639PQTncWsmeu5kbtG6W0ylCLWRggmWmInnSrM6JC2BLaJ7ocrAE6V2WaTFfNlcHjUzjo_AtidOOcmBpv7h0KF6LoFelg6gsYc9pJSiNVtTWFBSGf4KAAsyUdHFxaHGGGVxCS3EYwGbupVaEwGFBCGUZJdSxlO3KgPt5dDnOW1Y-jI4IR0P85A4dwTPEHHRFChDJ9AbQWTUoFRd3m8_aEODauccITV89gO9CaDeTVH9tBuxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#رسمیییییی
؛ آنژ پوستکوغلو سرمربی سابق تاتنهام هدایت النصر عربستان را برعهده گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97897" target="_blank">📅 20:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97896">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUvO39HpiYU5mZMKeYBPJ0_1gj2nGFhxAXjOZMZoTOuKY_HMqToKdPSbrn-MOHw2j1-ZysMHDeUcgcEDLIpIuRP1WAaQrHcB6cCnACMEIa4R7opQk4WSSfIUFSAm3j1vaa7aaPl0-Zd_YPemJEeAx6HA0raOq6Q3lno6MF1tbCtVLxPvpujPa1SwkcSEolToOlWtWm5hEXBZhyq7sc8aBBqkhU3m0s3gR6fdivsOrRyMh-xcDZ4h6XR8hdn67KDoE_UYMLGxBUifJ8JAPavNeOmCW5VVPetb4C4H8_S5lmjUgn7jwSB5831p5gSw_F1VaNWX3hqIEVNvcn6dyLn7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با انتقال تونالی به تاتنهام، نیوکاسل که ۱۷۵ میلیون پوند حدوداً برای این سه بازیکن خرج کرده بود موفق شد حدود ۳۰۰ میلیون پوند بفروشتشون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97896" target="_blank">📅 19:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97895">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOYko7SWrRejLrBMVoAWllfyzisjbOoJOZmx5HpPSZyFLKpBkgtwQWYUyiMBtAtlT0PJeF2pJ0iTpYI_K6GrRl_RUBWrYYj8Bm50lJwKD4cTSLQSqCNLWweEUxhw_fyFvDQbnFKjsog0O1Pe2HKcoqU03XauBtYZWDymvyiiKoAf9HnHqAHt3SYtHRjOlFs17-q4uAw7fMRQPpLiRLqWHcWkomwSRvu1OrL9es2l-1g1QoiIzOPM1JBfddAKhGMhtDFxQEf86v0N0OHMILsMGSs74P4hiqkKulBoFofahB3H4zUud2RfnJFGHFZMLMDxvmcbJq_X2xV7oscva8_R6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇩🇪
فوری از بن‌جیکوبز:
یورگن کلوپ تمایلشو به مربیگری تیم ملی آلمان اعلام کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/97895" target="_blank">📅 19:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97894">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61eb94b3b4.mp4?token=bM3_AUZqb9oJLiVoHUT-7HqV9ggMZslf7MA8_PbXPb7b5bpJ24A83vom26u8mBi7540DmNMTz_YmRdaHpuVVaMYWCJIZlcCy3GfLoBiIIVSDg1zm3iXGEodPy8PV81sdchn2WWPH6yn6W0RImpVj-XEmPiskR46AraPCpmuaMyZTKFDzMvO9zrqegqIswh1Z9VSWxBqF6ms7jN9kckiGHgHZICaJgatw_Lf8OH1w1yxexSUjmIUHPO36NKHGsfdlSraMz6i1yHPE88rPc9kCqjLytDLOdaVi1NfyoVW0-24dhbN-k-l9SyVvvO8BDr5h-KH2ogDUNlsB3yYqgCQhfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61eb94b3b4.mp4?token=bM3_AUZqb9oJLiVoHUT-7HqV9ggMZslf7MA8_PbXPb7b5bpJ24A83vom26u8mBi7540DmNMTz_YmRdaHpuVVaMYWCJIZlcCy3GfLoBiIIVSDg1zm3iXGEodPy8PV81sdchn2WWPH6yn6W0RImpVj-XEmPiskR46AraPCpmuaMyZTKFDzMvO9zrqegqIswh1Z9VSWxBqF6ms7jN9kckiGHgHZICaJgatw_Lf8OH1w1yxexSUjmIUHPO36NKHGsfdlSraMz6i1yHPE88rPc9kCqjLytDLOdaVi1NfyoVW0-24dhbN-k-l9SyVvvO8BDr5h-KH2ogDUNlsB3yYqgCQhfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند تو ملیت های مختلف
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97894" target="_blank">📅 19:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97893">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecbf79b99b.mp4?token=q9Ar2rpY6cM6nIAEDrIzpizsNk87rw1o17D1sxb-bRvRHOZras82RrGn2SgCmglQXOYkLGyNLqF-MGLzIUJo8f7b0b2BfpPnUAW8HqqycxFTcljFAKwqQX45npBVaULMxMxbCYNVM3iQ0f2p69HSv4Nx0c_uY2UpTfdNn4u9VxNhUFcQAu6bUJPp4gxMj42QF-Zh5Ozy61ycsJMCLg-u3RUAN7GvME9TGJDWDOnQDKFCBQeC2rZ9krvQnK4-YJLLN3bECXuY8Xbur03ntdafjTxaN4NHC3pQLj8ADTHnVPtsvh-tpXFcJ3-r65Lnh9Vn2lChVsu2H6s96hb3N_jV1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecbf79b99b.mp4?token=q9Ar2rpY6cM6nIAEDrIzpizsNk87rw1o17D1sxb-bRvRHOZras82RrGn2SgCmglQXOYkLGyNLqF-MGLzIUJo8f7b0b2BfpPnUAW8HqqycxFTcljFAKwqQX45npBVaULMxMxbCYNVM3iQ0f2p69HSv4Nx0c_uY2UpTfdNn4u9VxNhUFcQAu6bUJPp4gxMj42QF-Zh5Ozy61ycsJMCLg-u3RUAN7GvME9TGJDWDOnQDKFCBQeC2rZ9krvQnK4-YJLLN3bECXuY8Xbur03ntdafjTxaN4NHC3pQLj8ADTHnVPtsvh-tpXFcJ3-r65Lnh9Vn2lChVsu2H6s96hb3N_jV1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازیای نصف شب جام‌جهانی هم دردسری شده
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97893" target="_blank">📅 19:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97891">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">😏
😏
😏
انتظاری که مردم از بازی امشب آرژانتین و کیپ ورد دارن بعد پیش‌بینی جادوگر غنایی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97891" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97890">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5205517f12.mp4?token=aZT2OpatCPYTNas4h9fa5-vizrJv95NMo3t39LB6ozYvrqlmMWxp6c-cZCOkyFLOR3-AsjQ4ocY1K1HQ7g4rcceLLpgFsyxd0xwOH8jLjUWP0BamYenaLYjLKm63LNpA-mTtdisPreTISkGBPXEJfHBlTPfiV_WFVp7NKpy8RlZ76D4NoPFG0eQJmwE3wz2XPFk2RA5MD5q6A50mCTZiwlsPUUsOAvf9YhnLNjmjqIZSyX63Orv7w2rbTbOhukJ2e2dJJQAMEBvVPwM0RVenvZiiSqf8wu-lzev2LcABR6tIiS2oG4bZVMdxADCmmkdZoZ41xQwTuQtdEmDnsJRniw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5205517f12.mp4?token=aZT2OpatCPYTNas4h9fa5-vizrJv95NMo3t39LB6ozYvrqlmMWxp6c-cZCOkyFLOR3-AsjQ4ocY1K1HQ7g4rcceLLpgFsyxd0xwOH8jLjUWP0BamYenaLYjLKm63LNpA-mTtdisPreTISkGBPXEJfHBlTPfiV_WFVp7NKpy8RlZ76D4NoPFG0eQJmwE3wz2XPFk2RA5MD5q6A50mCTZiwlsPUUsOAvf9YhnLNjmjqIZSyX63Orv7w2rbTbOhukJ2e2dJJQAMEBvVPwM0RVenvZiiSqf8wu-lzev2LcABR6tIiS2oG4bZVMdxADCmmkdZoZ41xQwTuQtdEmDnsJRniw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
اتفاقات امشب بازی آرژانتین
🆚
کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97890" target="_blank">📅 18:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97889">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwrAN8EhZbtjHFRD51mbtTw1z4RB4D-W4JmVqPvUtNgQzB9kT8lzkaD3MerS6h5IZlpWO77RzfBNvDvC-hXCU4CB3TYm9Ogg4Enug1O0J9KW5tT09zIbAn4KpUrYQd6OYhhqKrr9K1ks0R6-966oF3-DdbXSY8BQ5Td9cJdS7fm9jgtDypZweHoLSrfeQf2mhBCnoDzzZQV8lNclNrOC8v36m8hCs3ZzDWrb0vkokr5ahWRbzPfg1k0lYBDdEyhHO4YExtI_qn4gBBd7AD-CAPjyVrAMZbI1XnZL1sUWPHaVkOEGTc4moscMgBl8o9k4LIEylKfZZUKSw4AS6cphiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#رسمیییییی
؛ ناتان آکه مدافع هلندی تیم فوتبال منچسترسیتی به فنرباغچه ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/97889" target="_blank">📅 18:17 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
