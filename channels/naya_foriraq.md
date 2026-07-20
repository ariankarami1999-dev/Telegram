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
<img src="https://cdn4.telesco.pe/file/hHN-KtnS6JNJw2NUUrZ-gGJkC4e1i0Lmz9pRJ2gFWdOLek1_ZHF0fb2dBgzcs0tbm0pynx0KA8eua1W_7LmRQFSN1NIHwWzCqkdaCh2f16ryn-3BoNfbuS9gxK6B74zY9-yPDjTh4YWARBm0VqE8bkGiJvLjO3mPmz0a4Cg63Ys8gA-FdZP5KHi01Uk2q08J4kR4gOSKa7OTB4TZ9Eq3ZyQUNK-3OZpsOs9BfZDtx1Wk-70hU9pQoYVRvuoZdTcWYmoW7z9_HAJulV49y0HiRzzSjv36EDf84S2fQP8NG_xF0u3pUraZwG4k96RpLGjz3lC9ReFI2HhbmioUCc_WXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 08:29:30</div>
<hr>

<div class="tg-post" id="msg-84361">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انفجارات عنيفة تهز المنامة</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/naya_foriraq/84361" target="_blank">📅 08:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0727eab181.mp4?token=TBvlc8mXpeyNcPLNuMAUdv4LPOrR6IxHaDLdyMxUBmBXmaLbXX5WLWIM2yI_1s_kfbZ_pb4UsWelQkGG8IXPZ053iRlmA0ugS41TzAEMx6-VK1FZqSkFCMgmY_6fn4KQtmPEmrWGWo1yKZKMj-oN96mvxoHKkKi4x2o3du4kXZkzzj6wUiblFgllUWh0qyixY6NpiRnYC5_97WWgkaF9pf56Cuz12fNZfX6jfuGrhmLmC1TVO28GWB-ZB1MNmrcoXlPHjkBR9P0q75qauLirPnHNP__j3_2NptZUNOfhKbNuk5jFA0b_rEsAejgtbMFGK2W-hTv_61NABtHGhGEnrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0727eab181.mp4?token=TBvlc8mXpeyNcPLNuMAUdv4LPOrR6IxHaDLdyMxUBmBXmaLbXX5WLWIM2yI_1s_kfbZ_pb4UsWelQkGG8IXPZ053iRlmA0ugS41TzAEMx6-VK1FZqSkFCMgmY_6fn4KQtmPEmrWGWo1yKZKMj-oN96mvxoHKkKi4x2o3du4kXZkzzj6wUiblFgllUWh0qyixY6NpiRnYC5_97WWgkaF9pf56Cuz12fNZfX6jfuGrhmLmC1TVO28GWB-ZB1MNmrcoXlPHjkBR9P0q75qauLirPnHNP__j3_2NptZUNOfhKbNuk5jFA0b_rEsAejgtbMFGK2W-hTv_61NABtHGhGEnrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
🇰🇼
لاول مرة
الكويت بدأت باستخدام المولدات الكهربائية المتنقلة للمناطق السكنية بسبب العجز التام لمنظومة الكهرباء على خلفية القصف الإيراني المستمر .</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/naya_foriraq/84360" target="_blank">📅 08:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84359">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">منظومة الباتريوت تفشل بالتصدي للصواريخ الإيرانية في سماء المنامة عاصمة البحرين</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/naya_foriraq/84359" target="_blank">📅 08:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84358">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/naya_foriraq/84358" target="_blank">📅 08:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84357">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/naya_foriraq/84357" target="_blank">📅 08:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84356">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">إصابة مباشرة في مقر دعم البحرين</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/naya_foriraq/84356" target="_blank">📅 08:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84355">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجارات قرب مقر دعم البحرية في البحرين.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/naya_foriraq/84355" target="_blank">📅 08:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84354">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/naya_foriraq/84354" target="_blank">📅 08:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84353">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/naya_foriraq/84353" target="_blank">📅 08:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84352">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/naya_foriraq/84352" target="_blank">📅 08:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84351">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a0ec0dd3.mp4?token=azQGlNhDo6QxYCoPZZE0s-amOMatZKtlI0Ea1d25m9sswCLbY5MaZAVLEAC_KD8u67KFK9m0cLFx12hB9oWPnhQ0DXbymrKsh10ndQE5W0twQfd8fxsRyj1epxN_hJ-Hj2Hea2CVlxaGafU6UHLmNcIJ4bnyawSUtQZdujRakXsi3B6bzpowku9SZe-8lgZ7HgYgzNVtaswy0dc8dYaJWIIeigl0TegFhV8fjT0ocPHnr7eTC4kxvpydH5vFnvW78kZr9rklgPq0A_4tbIPF0Cz9pJOXUdjABramzd4PH99k49fa1ySVGolf0uHHNo7jY9JnGzxwZHjM9QqJUOJHFWSVCLa77BAmVOft7_9lsaWO5kzfHt2TFaB_3ogKm9_pqoaE4gPqK7enqix6LWNd_gDdTStLGipZz0aW5T8eyIQPx6wzi2Ep3LJ1ZE-Fhtk5aqCsI3cRzxdrDiYSxVQsyLYQ96V3DSCo1gArl8hw1XOn7krO6IMZstRadq87oBAcx_nsqGkJN8Kky1p1t45-MdgzXVJMOzyjCVpw88ByUE3B0GBZEhSFlnhnSOMHZUB-NPW11eRSrMywJTemLVJiQmlbcDrDHhHbkRqIAPMFLXlz2egmZ3BltEw4M-CymbkIcyPlV56p92iVGiE1QYdp9S0arPLXBfoxpWLK_oiAke4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a0ec0dd3.mp4?token=azQGlNhDo6QxYCoPZZE0s-amOMatZKtlI0Ea1d25m9sswCLbY5MaZAVLEAC_KD8u67KFK9m0cLFx12hB9oWPnhQ0DXbymrKsh10ndQE5W0twQfd8fxsRyj1epxN_hJ-Hj2Hea2CVlxaGafU6UHLmNcIJ4bnyawSUtQZdujRakXsi3B6bzpowku9SZe-8lgZ7HgYgzNVtaswy0dc8dYaJWIIeigl0TegFhV8fjT0ocPHnr7eTC4kxvpydH5vFnvW78kZr9rklgPq0A_4tbIPF0Cz9pJOXUdjABramzd4PH99k49fa1ySVGolf0uHHNo7jY9JnGzxwZHjM9QqJUOJHFWSVCLa77BAmVOft7_9lsaWO5kzfHt2TFaB_3ogKm9_pqoaE4gPqK7enqix6LWNd_gDdTStLGipZz0aW5T8eyIQPx6wzi2Ep3LJ1ZE-Fhtk5aqCsI3cRzxdrDiYSxVQsyLYQ96V3DSCo1gArl8hw1XOn7krO6IMZstRadq87oBAcx_nsqGkJN8Kky1p1t45-MdgzXVJMOzyjCVpw88ByUE3B0GBZEhSFlnhnSOMHZUB-NPW11eRSrMywJTemLVJiQmlbcDrDHhHbkRqIAPMFLXlz2egmZ3BltEw4M-CymbkIcyPlV56p92iVGiE1QYdp9S0arPLXBfoxpWLK_oiAke4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇨🇳
قادة أمريكيون:
سلاح فرط الصوتي بعيد المدى "دارك إيجل" انطلاقًا من غوام قادر على تهديد أهداف بالغة الأهمية في البر الرئيسي للصين.
ربما يكون الجيش الأمريكي نشر هذا السلاح خلال مناورات "فاليانت شيلد" خلال تدريبات على استخدام "دارك إيجل". حيث لم يكشف عن الموقع أثناء هذه المناورات، لكن الصور وتحركات الأدميرال صموئيل بابارو في يونيو ومنطقة التدريب تشير بقوة إلى غوام.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/naya_foriraq/84351" target="_blank">📅 07:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84350">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔻
مركز رصد الزلازل الأورومتوسطي: زلزال بقوة 5.5 درجة يهز غرب إيران</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/naya_foriraq/84350" target="_blank">📅 07:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84349">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔻
مركز رصد الزلازل الأورومتوسطي: زلزال بقوة 5.5 درجة يهز غرب إيران</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/naya_foriraq/84349" target="_blank">📅 07:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84348">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇶
هزة أرضية قوية شعر بها معظم سكان العاصمة العراقية بغداد في هذه الأثناء.</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/naya_foriraq/84348" target="_blank">📅 07:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84347">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هجوم جوي جديد على البحرين</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/naya_foriraq/84347" target="_blank">📅 07:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84346">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eadd25eee.mp4?token=rufIShhm1P4j28vwfaPd9OEy6YgcPUssGeqlTfMuXPVyIryA32wcPRH_0AN7wcLYwRl9f3ISAQ0WsrGpPsiL_2_dUdCiPeYpc2yIbkk47bsSdVir_CB8G5vWW4qERZVc-CJXC2SZbRJwB91JUWSQf_Hz2iZ_dQy7DTLkrUq8H-HA0XzKBMvFLRj9b0YVD3IgICwQbIrx6_BpTiSnLIj82qkNUM9BWd6M-rXGvJ-X4lauzC9lCZmg-40yn_d32F5wjZyMzD0SwR2E1-mV_lGfCL_pZ-8GmDqh-3-mJgVN8HJhcHzJ8YI7MJwSe1RngrQdIaJFCJ38dQbU5HI-LSLGKJ0OZQudGyua-gVjZqOmcKpMy0uC7aMWCh4wagTtRbW3MlaWhbTTji2U2TEFWlUtJHd1RIsr2w-M69HXibcOb6gcCUucdOS3y9SKQkgqD9GcVWl9oSGbv8wNcsFd3I1Dlirm55cg6hzIxIdVgBZW98RKWR-9fQ_iO7A40beFyCqHrOo8bzPYn0J5mJ06eTsiSC0kuhkJmIpkZZ8j2F3v46G14foxK0Zkjnrw0N_EMQ54OcnqHYrsLTjdLBep_bl1ADHrYbToFOdZYF7UQ7ooLIhuQANiocO_yfZJHBcCTyqWBQ3sgJe9uhvhNpu3C4uNWn619iIb_SPyBa49cU5ly1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eadd25eee.mp4?token=rufIShhm1P4j28vwfaPd9OEy6YgcPUssGeqlTfMuXPVyIryA32wcPRH_0AN7wcLYwRl9f3ISAQ0WsrGpPsiL_2_dUdCiPeYpc2yIbkk47bsSdVir_CB8G5vWW4qERZVc-CJXC2SZbRJwB91JUWSQf_Hz2iZ_dQy7DTLkrUq8H-HA0XzKBMvFLRj9b0YVD3IgICwQbIrx6_BpTiSnLIj82qkNUM9BWd6M-rXGvJ-X4lauzC9lCZmg-40yn_d32F5wjZyMzD0SwR2E1-mV_lGfCL_pZ-8GmDqh-3-mJgVN8HJhcHzJ8YI7MJwSe1RngrQdIaJFCJ38dQbU5HI-LSLGKJ0OZQudGyua-gVjZqOmcKpMy0uC7aMWCh4wagTtRbW3MlaWhbTTji2U2TEFWlUtJHd1RIsr2w-M69HXibcOb6gcCUucdOS3y9SKQkgqD9GcVWl9oSGbv8wNcsFd3I1Dlirm55cg6hzIxIdVgBZW98RKWR-9fQ_iO7A40beFyCqHrOo8bzPYn0J5mJ06eTsiSC0kuhkJmIpkZZ8j2F3v46G14foxK0Zkjnrw0N_EMQ54OcnqHYrsLTjdLBep_bl1ADHrYbToFOdZYF7UQ7ooLIhuQANiocO_yfZJHBcCTyqWBQ3sgJe9uhvhNpu3C4uNWn619iIb_SPyBa49cU5ly1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇴
لقطات من الأقمار الصناعية تظهر ضربة مباشرة على مبنى في قاعدة موفق السلطي الجوية بالأردن حيث وقد دُمر المبنى إضافة إلى تضرر عدة مركبات مجاورة.</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/84346" target="_blank">📅 07:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84345">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/naya_foriraq/84345" target="_blank">📅 06:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84344">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/naya_foriraq/84344" target="_blank">📅 06:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84343">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/naya_foriraq/84343" target="_blank">📅 06:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84342">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني: استُهدفت منظومة رادار الإنذار المبكر الأمريكية، ومبنى لتجهيزات وقطع غيار جوية، ومنصة لطائرات مسيرة من طراز MQ9 أمريكية.
أهل الكويت الكرام؛ منذ سنوات، تشغل قوات عسكرية كافرة أمريكية أجزاء من أرضكم الإسلامية، وتستخدمها كقاعدة لقتل المسلمين في إيران والعراق وأفغانستان وفلسطين.
قبل 140 يومًا، بدأت جيوش الأطفال الأمريكية، مستخدمة هذه القواعد، حربًا ضدنا، بدأت بقتل 168 طفلًا في مدرسة ميناب، واستشهاد العلامة الدينية البارز في العصر الحاضر، الإمام الخامنئي (رحمه الله).
يجب ألا تكون أرض الكويت مكانًا آمنًا للجيش الإرهابي الذي هاجم على الأقل عشر دول إسلامية خلال العقود الأخيرة، وقتل ملايين المسلمين. هذا الجيش، بحكم فتاوى علماء جميع المذاهب والفرق الإسلامية، متجاوز لحدود المسلمين، ودمه مباح، وواجب على كل مسلم أن يبيده بكل الوسائل الممكنة، وأن يطهر أراضي المسلمين من وجوده. نتوقع منكم أن تنهضوا بواجبكم الديني، وأن تعيدوا العزة لأراضي المسلمين.
قواتنا الشجاعة في الموج الثاني والعشرين من عملية "نصر 2"، تحت شعار "يارقية (عليها السلام)"، ردًا على التعديات المتكررة الأمريكية على أرض إيران، قامت بهجوم بطائرة مسيرة، ودمرت بالكامل منظومة رادار الإنذار المبكر الأمريكية. كما في هجوم آخر، استهدفت مبنى لتجهيزات وقطع غيار جوية، ومنصة لطائرات مسيرة من طراز MQ9 أمريكية في قاعدة "علي السالم"، وأشعلت فيها عدة طائرات مسيرة.
نتوقع منكم، يا أهل الكويت الكرام والأصيلين، أن تنهضوا بواجبكم الإلهي، وأن لا تسمحوا بأن تكون أرض الكويت منطلقًا للشر والقتل للمسلمين.
"إن تنصروا الله ينصركم ويثبت أقدامكم</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/84342" target="_blank">📅 06:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84341">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الخارجية الأمريكي: الولايات المتحدة لا تزال منفتحة على الحل الدبلوماسي في إيران.</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/naya_foriraq/84341" target="_blank">📅 06:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84340">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عدوان أمريكي غاشم على مدينة تشابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/84340" target="_blank">📅 05:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84339">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd21cb7cb7.mp4?token=g2ah1606z1nVm6tXdDQTP9SLQ7NnWB9fEBYH4X3a6Y3JO53QMOFQcNA3c-w7WBdLjijsi42Myf2ubbIWFQk9ECc3VIrzuvbxQq-0HBuW2QfrbYT9VnQELcC3wDAc-UNP_NVjA4NCl9Q5Iq-Uufr9zytzjhtYapPgjd3tGd69KyE6Hxln3MkLi39gQ4GRxS4In89St6gXGvnH2W85N7cUZ_BonUrOS0NxfVebbicD0uvKptft8YraAn-_ALxSHGmiLSgTMjvMw-nwfueVAhNa_w_E0R2xt2af0gmd0_WRaHT1ZUe31BEv9CM4SDncqWWGSlkjAP1XgDTBDR2RwJR58g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd21cb7cb7.mp4?token=g2ah1606z1nVm6tXdDQTP9SLQ7NnWB9fEBYH4X3a6Y3JO53QMOFQcNA3c-w7WBdLjijsi42Myf2ubbIWFQk9ECc3VIrzuvbxQq-0HBuW2QfrbYT9VnQELcC3wDAc-UNP_NVjA4NCl9Q5Iq-Uufr9zytzjhtYapPgjd3tGd69KyE6Hxln3MkLi39gQ4GRxS4In89St6gXGvnH2W85N7cUZ_BonUrOS0NxfVebbicD0uvKptft8YraAn-_ALxSHGmiLSgTMjvMw-nwfueVAhNa_w_E0R2xt2af0gmd0_WRaHT1ZUe31BEv9CM4SDncqWWGSlkjAP1XgDTBDR2RwJR58g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الأمريكي:
تامبا، فلوريدا - أنهت القيادة المركزية الأمريكية (سنتكوم) بنجاح، مساء التاسع عشر من يوليو/تموز، الساعة العاشرة مساءً بتوقيت شرق الولايات المتحدة، الضربات الجوية التاسعة على التوالي ضد إيران.
استهدفت أصول سنتكوم مراكز القيادة العسكرية الإيرانية، ومواقع الدفاع الجوي والمراقبة الساحلية، والقدرات البحرية، ومواقع إطلاق الصواريخ والطائرات المسيّرة، وشبكات الاتصالات، وذلك بهدف تقويض قدرة إيران على مهاجمة السفن التجارية والبحارة المدنيين العابرين لمضيق هرمز.
يُحاسب الجيش الأمريكي إيران بتوجيهات من القائد الأعلى للقوات المسلحة. وتبقى قوات سنتكوم في حالة تأهب قصوى، ومركزة، وقادرة على القتال، وجاهزة للعمليات.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/84339" target="_blank">📅 05:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84338">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الخارجية الأمريكي:
الولايات المتحدة لا تزال منفتحة على الحل الدبلوماسي في إيران.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/84338" target="_blank">📅 05:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84337">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔻
الحرس الثوري:
أيها الشعب الأردني الكريم والجنود الأردنيون المخلصون،
نشكركم على تعاونكم الصادق والمعلومات الدقيقة التي ساهمت في استهداف مقاتلي الإسلام وتدمير 20 مبنى تستخدم كمواقع لتمركز قوات الجيش الأمريكي "قاتل الأطفال"، وأدت إلى مقتل العشرات من عناصر الإرهابيين الأمريكيين في منطقة الأزرق.
🔹
مقاتلو قوة الجوفضاء التابعة للحرس الثوري، في الموجة الثانية والعشرين من عملية "النصر 2"، تحت شعار مبارك "يا رقية (س)"، وإهداءً لفتيات الشهيدات في حرب الدفاع عن الوطن الثالثة، وبمساعدتكم، استهدفوا طائرات النقل العسكرية الكبيرة من طراز C17 وطائرات القيادة والتحكم من طراز P8 التابعة للجيش الأمريكي المعتدي في مطار العقبة، وألحقوا أضرارًا جسيمة بعدد منها.
🔹
الجنود الأمريكيون المعتدون، الذين هاجموا أكثر من عشر دول إسلامية على مدى العقود الأخيرة، وقتلوا ملايين المسلمين، وهم الداعم الرئيسي للنظام الصهيوني الدموي في قتل جماعي لشعب غزة وتدمير الضفة الغربية، يعتبرون شرعًا دمًا، وكل مسلم، أينما أمكنه، يجب أن يقتل هؤلاء القتلة الوحشية.
🔹
نشكركم مرة أخرى على جهودكم وتعاونكم الذي يمهد الطريق لتحرير القدس الشريف من خلال أداء واجبكم الشرعي.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/84337" target="_blank">📅 05:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84336">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الله أكبر
الدفاعات الجوية الإيرانية تتمكن من إستهداف واسقاط مسيرة MQ9 أمريكية في سماء مدينة "إسلام آباد غرب" بمحافظة كرمانشاه الإيرانية.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/84336" target="_blank">📅 05:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84335">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔻
الحرس الثوري:
في وقت متأخر من الليلة الماضية، انفجرت سفينتان نفطيتان مخالفتا تعليمات، كانتا تحت تأثير وتحريض من قبل الجيش الأمريكي، وكانتا تنويان الدخول والخروج من ممر غير آمن وخطير في جنوب مضيق هرمز. وقد أدت الانفجارات إلى توقفهما عن الحركة.
على الجيش الأمريكي الاستعداد لعمليتنا العقابية بسبب أعماله غير القانونية.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/84335" target="_blank">📅 04:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84334">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">عدوان أمريكي جديد على ميناء تشابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/84334" target="_blank">📅 03:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84333">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a3ed7e945.mp4?token=BTL4rCQ43PPzDdFZGaO_SMjYN-bjC4BAYJGuvTiiKL0uJAVO22DuCxRyd4iN4nvx-bEA9g6jZ6fTHCN6a_cxXv4I55ybJCWSBZ6G6pnKhqOgT5KFdlY01Df0SC_sXHKIA7eIfSkoh598zbcT6F7hVDt25H9rdaS7Vd47HE50aJqc30LvN3tFSo3QmqDkJMm4KMzEthnCIHYfjlaA9Ue-0RvRoCx9u168GYbWEr8dDrgfgbwfTSUOyq1ZJbFiK3yIoZ33VOwl5X9pE-7mzfXIFpPKLhbvPMAq7pM_d5X7o2lk0Xhqo2Zom030qr2YSX9V7SqEeWxKIGxXtHOH1DSewYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a3ed7e945.mp4?token=BTL4rCQ43PPzDdFZGaO_SMjYN-bjC4BAYJGuvTiiKL0uJAVO22DuCxRyd4iN4nvx-bEA9g6jZ6fTHCN6a_cxXv4I55ybJCWSBZ6G6pnKhqOgT5KFdlY01Df0SC_sXHKIA7eIfSkoh598zbcT6F7hVDt25H9rdaS7Vd47HE50aJqc30LvN3tFSo3QmqDkJMm4KMzEthnCIHYfjlaA9Ue-0RvRoCx9u168GYbWEr8dDrgfgbwfTSUOyq1ZJbFiK3yIoZ33VOwl5X9pE-7mzfXIFpPKLhbvPMAq7pM_d5X7o2lk0Xhqo2Zom030qr2YSX9V7SqEeWxKIGxXtHOH1DSewYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب:
سنضرب إيران بقوة هذه الليلة.
إيران ربما لديها بعض الصوايخ والطائرات المسيرة لكنها ليست كثيرة.
لم نعد نكتفي بمنع الإيرانيين من حيازة قدرات معينة بل نقوم الآن بإنهاء هذا الأمر تماما.
نوجه الضربات لإيران وسنرى ما سيحدث.
كنا نعتقد أن شخصين [من القوات العسكرية الأمريكية] قُتلا في الهجمات الإيرانية، لكن كان هناك ثلاثة أشخاص.
نُسيطر على مضيق هرمز وإيران لا تسيطر على أي شيء.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/84333" target="_blank">📅 03:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84332">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d18382358.mp4?token=c05jYzlzsEICa5Se0ySQh8atTruxCbFc0xmn23E18dnbO2oqtVSIbTc6-w03e_v10Yl5cUKfFr1IbCLTqAYblAP8SP7A3s9hC2PtOlLKByNZehotQAYhg3j6i-_lEiirrqdKfIcxJstZIJQnvqnwuSjCe9WFmvZt6wVQPSwuxC5Z7rHWujsoNEMIyj6S1yf-dG3VAoCQjcJMszXJx4tZjF-PQ9DzidAIeJeyCmUFIzzHks9rMGUxOQTOoSH2dzTMsKrn9Wh0oXFpxssHs5Vdq1bIvCdOmquUkRP4tNJuFbQvMn3RlWMOjEkpOt5SI4Se6pZmfnklwOa-atw8ccV9xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d18382358.mp4?token=c05jYzlzsEICa5Se0ySQh8atTruxCbFc0xmn23E18dnbO2oqtVSIbTc6-w03e_v10Yl5cUKfFr1IbCLTqAYblAP8SP7A3s9hC2PtOlLKByNZehotQAYhg3j6i-_lEiirrqdKfIcxJstZIJQnvqnwuSjCe9WFmvZt6wVQPSwuxC5Z7rHWujsoNEMIyj6S1yf-dG3VAoCQjcJMszXJx4tZjF-PQ9DzidAIeJeyCmUFIzzHks9rMGUxOQTOoSH2dzTMsKrn9Wh0oXFpxssHs5Vdq1bIvCdOmquUkRP4tNJuFbQvMn3RlWMOjEkpOt5SI4Se6pZmfnklwOa-atw8ccV9xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي على مدينة ماهشهر</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/84332" target="_blank">📅 03:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84331">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الله أكبر
🇬🇧
الجيش البريطاني:
اندلاع حريق على متن سفينة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/84331" target="_blank">📅 03:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84330">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عدوان على مدينة خورموج وميناء سيريك جنوبي إيران.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/84330" target="_blank">📅 03:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84329">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇱
دوي صافرات الانذار في مستوطنات غلاف غزة والعدو يزعم أنها بسبب تشخيص خاطئ.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84329" target="_blank">📅 03:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84328">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1682925309.mp4?token=tO3S1SONWcQYYP11Yw5ReoiDnEVkmTTzJUyn-dp5q6luWyXP3oYlip7KfbuCP_0V4y5sSzWnFSiv75JK-8wrBw1gdx6_1daf58yb_sfxAQdowbczIkg5OPjIpeoHkM2wYSFsWXlNk41ErtIJZ6nAHS9kEFy3J6a8z8fU5__CLaJqzNsh_SZpSeZssXXd5BCjn49OCzq2khf4YH2fee4kSdDV727rSuBFmzTWlcYkQ6Q8vb6ObtP5YwaCkdVZKiVMBNarHpxMAuOalzNUL_cIa2pE-2aQToL4_AYs8YObo1VyI40b_U6t7_meirrFwisxnmnHYEq0CDIGWCJd2Wzinw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1682925309.mp4?token=tO3S1SONWcQYYP11Yw5ReoiDnEVkmTTzJUyn-dp5q6luWyXP3oYlip7KfbuCP_0V4y5sSzWnFSiv75JK-8wrBw1gdx6_1daf58yb_sfxAQdowbczIkg5OPjIpeoHkM2wYSFsWXlNk41ErtIJZ6nAHS9kEFy3J6a8z8fU5__CLaJqzNsh_SZpSeZssXXd5BCjn49OCzq2khf4YH2fee4kSdDV727rSuBFmzTWlcYkQ6Q8vb6ObtP5YwaCkdVZKiVMBNarHpxMAuOalzNUL_cIa2pE-2aQToL4_AYs8YObo1VyI40b_U6t7_meirrFwisxnmnHYEq0CDIGWCJd2Wzinw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في غرب وجنوب شرق إيران.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84328" target="_blank">📅 03:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84327">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عدوان على مدينة خورموج وميناء سيريك جنوبي إيران.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/84327" target="_blank">📅 03:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84326">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/84326" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84325">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84325" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84324">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0ckfWy4W7PALiRJfqMeINdgSA8RfiijImXJdQoxYvtYxqskGVfqv0rULO2N3eQU0oGZWih8tKlyuClUg7j23_8SA3rVkNqHgrZYLQYRUYUQwd7d5Ra3A3aXA30IFkGAl5f7YS88hSQcheKfmgaybgUmIihFAHibXebMarrR7Gb7C6fnkQqBkr_Y3se6GcJdUnDWoQoSYJPf87nscuDEBg1IPfN-JTZ-eVpoKNxwYbQIuFoYjpq0q4QGGgdHl2V-Oo3NooialADBBaPcgQpEyPi321LdctFb4vFCfTnRcjm-8_op8rKZG6YZHzgOXSj7ue5JwvJTA_p01KqC7UX0Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث أمني قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/84324" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84323">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حدث أمني قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84323" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84322">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETX8uGJS6np3pHoMgSlTTk2IBndIq4iLkhuZ3tI36nBO8oze05eKH4Jq9PiS84fdN4SzwM5kTZ0TCFrd9_phDzKo-cBDTpQQWY0fO_JlJF9V-uVVLWivIGUkkEztEOsosiI051SdXHESKUxMH0hkoscYg18v1Dpn6Y2hUTsKQQIMIPiQEHyrYDZBVgwelsbQuR8Cs1tYyqk1eFoWEvra3waSnBIT9JRvW2wsCNcjhQ8-vfnjh1MAvvxEtAaLn2ykOilmsb_OuIvqJKgOQ-OESC0D5ayTg-JCu83JuP7TQ-w1k3fLV1ifbkEcVJHXXrhxwr5_wFVZikTAmPaK1faaVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من العدوان الأمريكي الغاشم على مدينتي ماهشهر وسربندر (ميناء الإمام خميني) جنوبي إيران.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/84322" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84321">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
🇧🇭
‏
السفارة الأمريكية في المنامة بالبحرين:
لدى السفارة معلومات تشير إلى أن إيران قد تسعى لاستهداف مواقع غير محددة في وسط المنامة.
نحث جميع الأمريكيين على توخي الحذر، واتباع تعليمات السلطات المحلية، ومراجعة أحدث التوجيهات.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/84321" target="_blank">📅 03:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84320">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الله أكبر
إنفجارات عنيفة في رأس الخيمة الإرماراتية</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/84320" target="_blank">📅 03:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84318">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c5b8b6ad4.mp4?token=bl27hH9l7fPRczPCgC7znm29neKM7XC2XVDoNzBpYgAwijHmVNEAb8kXYIJhRrdDVoMBR-Vxjz46a71vzKyACQS6yF_AfKvwS56Hx9yBpbjtHB_CGg5ClCKPafiOr8KyJ6E0ei6BkthQYxLIPrPbmO8hRrnl1oCrQV45SWz1Ou7r6B7NZnJPWI0n_DI5Yh48BR6bxsClYJD6GORcjzWFaOAyCERcxXEhHKhz1XrQqe5LJL-7k5yvJ1lXv9-lrdjenMzHx0UXpFgod93R_OEs9hAGT17YbSWKtHHylXmJdjdVUZKm3olwW4Mty_RLpUT4jeo98xS1lyHkBI4ZF8_Xow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c5b8b6ad4.mp4?token=bl27hH9l7fPRczPCgC7znm29neKM7XC2XVDoNzBpYgAwijHmVNEAb8kXYIJhRrdDVoMBR-Vxjz46a71vzKyACQS6yF_AfKvwS56Hx9yBpbjtHB_CGg5ClCKPafiOr8KyJ6E0ei6BkthQYxLIPrPbmO8hRrnl1oCrQV45SWz1Ou7r6B7NZnJPWI0n_DI5Yh48BR6bxsClYJD6GORcjzWFaOAyCERcxXEhHKhz1XrQqe5LJL-7k5yvJ1lXv9-lrdjenMzHx0UXpFgod93R_OEs9hAGT17YbSWKtHHylXmJdjdVUZKm3olwW4Mty_RLpUT4jeo98xS1lyHkBI4ZF8_Xow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان أمريكي جديد على مدينة ماهشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84318" target="_blank">📅 03:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84317">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عدوان أمريكي جديد على مدينة ماهشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/84317" target="_blank">📅 03:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4322d49914.mp4?token=PM5T7SGQuz0rZnoBKHobbRcA5HZOQQh1Vzkw5sWZsdJ28j9P4ujuqC9_uSzL21UGlKPRScgfu1-eslxnWbAvVnlZoQR6XaRn0eDl6AAg3snKcrhVMJYLWcS4WrTkSbMQPRzaRiG38ir67Gaifl0D7IYw_1dV3XKGyiwyel_H3pYA7q0Fm3fCfrXwRcSuDaVQcOlmQFp2bTmLoyyU1FrbIBSeMCgsJwW14PeQe4dJY3YaqP1YY2CnjTAKZ9SgUllNgA2LDnVb2BihoukX3vJG1Lx-tK1aocceVQSEw1kwvhf7zfYZCQP959JT5QeY-V-ryT6Rjzb7qkV693cM9NuTPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4322d49914.mp4?token=PM5T7SGQuz0rZnoBKHobbRcA5HZOQQh1Vzkw5sWZsdJ28j9P4ujuqC9_uSzL21UGlKPRScgfu1-eslxnWbAvVnlZoQR6XaRn0eDl6AAg3snKcrhVMJYLWcS4WrTkSbMQPRzaRiG38ir67Gaifl0D7IYw_1dV3XKGyiwyel_H3pYA7q0Fm3fCfrXwRcSuDaVQcOlmQFp2bTmLoyyU1FrbIBSeMCgsJwW14PeQe4dJY3YaqP1YY2CnjTAKZ9SgUllNgA2LDnVb2BihoukX3vJG1Lx-tK1aocceVQSEw1kwvhf7zfYZCQP959JT5QeY-V-ryT6Rjzb7qkV693cM9NuTPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي على تبريز شمال غرب إيران.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/84316" target="_blank">📅 03:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84315">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=n0wJAhcyqA_ehB_yr4A1KyiL0__CwznByECrfQWYvVL1fZfEsgNAl5US2xG-vnT-y23Bn8nIr9cHyMuG9n0vXIqiPbuULIBkaqUhQZQsk5_q1hqegZw94GngXCwOr-ifHWMC9_H30pu0xBxBI0dNS_P9YyleNnFuNTW90jkg4x5dJA2sVDvy08q3RtdGb2ipI1drsxEgJ07kJGUxSdgrxLiOJvH-yxCtgLHwOW9fdwbbf97Ns7QvVDEn1XHoFXx9pIWZseeS32SEqk0cTFmFL1dmce51JpY2ah85qfCCgybnRDu85KBG67q8EyxF9B8Bm-ECgbDg1qNgA6ekr8h6lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=n0wJAhcyqA_ehB_yr4A1KyiL0__CwznByECrfQWYvVL1fZfEsgNAl5US2xG-vnT-y23Bn8nIr9cHyMuG9n0vXIqiPbuULIBkaqUhQZQsk5_q1hqegZw94GngXCwOr-ifHWMC9_H30pu0xBxBI0dNS_P9YyleNnFuNTW90jkg4x5dJA2sVDvy08q3RtdGb2ipI1drsxEgJ07kJGUxSdgrxLiOJvH-yxCtgLHwOW9fdwbbf97Ns7QvVDEn1XHoFXx9pIWZseeS32SEqk0cTFmFL1dmce51JpY2ah85qfCCgybnRDu85KBG67q8EyxF9B8Bm-ECgbDg1qNgA6ekr8h6lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صواريخ من الكويت تجاه إيران الإسلامية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84315" target="_blank">📅 03:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84314">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الله أكبر
🇮🇷
الدفاعات الجوية الإيرانية تتمكن من إستهداف وإسقاط مسيرة أمريكية جنوبي إيران.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/84314" target="_blank">📅 02:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84313">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9cfa9c17.mp4?token=bad6KLFIWH3Mt_oiv97X7MvoHeSGLqHYKaKH0j0uQccLvuWqYUATR0eDdSya9qjPbgr5M_Sbz9snzI2AvS6GsjewA-X5h5OfbmsysKh7Rg6DY-aw13XJlogfV3IaIji4ERAvrb5j5JsEPnxDK509fXcCwm6tWsKRxmfw7dv7xLRbjqZ2fsxp0QVdPnFJ9QFh8VtzQdzd2h3_0QYs_UldtbEZ7W3oJLSieLIHklVQwS8L6nN-Ge3hPaBzDAiRQ-X7ELCjMcGhNaM20ISC-unGCgGLqYpwMMP-pBHd7bLWNk4TaXYGAfXnJtT49ElGQhnZ94_dk5DkOzzSY-FLNbNYAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9cfa9c17.mp4?token=bad6KLFIWH3Mt_oiv97X7MvoHeSGLqHYKaKH0j0uQccLvuWqYUATR0eDdSya9qjPbgr5M_Sbz9snzI2AvS6GsjewA-X5h5OfbmsysKh7Rg6DY-aw13XJlogfV3IaIji4ERAvrb5j5JsEPnxDK509fXcCwm6tWsKRxmfw7dv7xLRbjqZ2fsxp0QVdPnFJ9QFh8VtzQdzd2h3_0QYs_UldtbEZ7W3oJLSieLIHklVQwS8L6nN-Ge3hPaBzDAiRQ-X7ELCjMcGhNaM20ISC-unGCgGLqYpwMMP-pBHd7bLWNk4TaXYGAfXnJtT49ElGQhnZ94_dk5DkOzzSY-FLNbNYAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجار في مدينة تبريز الإيرانية</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/84313" target="_blank">📅 02:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84312">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e07ac69b1.mp4?token=X2QaI7n5A9E28ykOG61r1v5o59iClB1azO8aj01nTLaGBXa1vYplON2aoO4bX0WdagknVjIjYhUl8Cea-TsqP3Pvac5Gm-SP4x-u0_5P7ajMu8suVM12-BmIWjF_5QAYYyPjZ8hZZeMK_ivC4Lt-NfCqokWeI2FuojsjKhosEsgDc3u4x56tE2tf1a1Oc78uLU3FgZspGnQydib3PnKfcC7-cZcIu82QT4qihyk_SJfWW3NIE0dn5NqDDAOH2IND1LSC6c9c-ILy7bnicAWyHHyiu0H4kW-lbWybGOFQQsYMC7cnOJz3_mwiWNiOXy6df3m15BlgPVe3soC_Mz6q7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e07ac69b1.mp4?token=X2QaI7n5A9E28ykOG61r1v5o59iClB1azO8aj01nTLaGBXa1vYplON2aoO4bX0WdagknVjIjYhUl8Cea-TsqP3Pvac5Gm-SP4x-u0_5P7ajMu8suVM12-BmIWjF_5QAYYyPjZ8hZZeMK_ivC4Lt-NfCqokWeI2FuojsjKhosEsgDc3u4x56tE2tf1a1Oc78uLU3FgZspGnQydib3PnKfcC7-cZcIu82QT4qihyk_SJfWW3NIE0dn5NqDDAOH2IND1LSC6c9c-ILy7bnicAWyHHyiu0H4kW-lbWybGOFQQsYMC7cnOJz3_mwiWNiOXy6df3m15BlgPVe3soC_Mz6q7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم عنيف يدك مقرات المعارضة الكردية الإرهابية في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84312" target="_blank">📅 02:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84311">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجارات في غرب وجنوب شرق إيران.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/84311" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84310">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجارات تهز الكويت مجددا</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84310" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84309">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجارات في غرب وجنوب شرق إيران.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84309" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84308">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الجيش الأمريكي: ‏
بدأت القيادة المركزية الأمريكية (سنتكوم) اليوم، في تمام الساعة السابعة مساءً بتوقيت شرق الولايات المتحدة، موجة جديدة من الضربات الجوية ضد إيران، وذلك لليلة التاسعة على التوالي. وستواصل هذه الضربات تقويض القدرات العسكرية الإيرانية التي تستخدمها إيران لمهاجمة السفن التجارية والبحارة المدنيين العابرين لمضيق هرمز.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/84308" target="_blank">📅 02:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84307">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عدوان أمريكي على مدينتي ماهشهر وميناء إمام خميني جنوبي إيران</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84307" target="_blank">📅 02:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84306">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b4cafb2c.mp4?token=Ca0FECqLPLuCKvfMRM3Yny8npgebTwXHk7KVCNqr2DpFqDArNgxdQXVDVEQxJNM9ZxhII3_esX5mRiEjkpBgqoq7nrVi_Il8fYqqFVyaas5Jf240W3zBqn2HFKSllJKGo0y5doeJ8W2_f9EbQxpxqS5QLmBDtebEpbusLeTwV_1uFNMUzaKmDdRInZhDABEOPgqHKFkLVMu47r513_oYXUkk3EYJUKKpiYW-yf6b5NOshx3kZs9kYrDJfp9SioAICuunqi7UPRs9okn1mW1PxqwbxEh1TasEHx8FHS29rVoHGUeyBKuBungsAbj4_TrMn17rOlzjeK-IDtRVfqm0fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b4cafb2c.mp4?token=Ca0FECqLPLuCKvfMRM3Yny8npgebTwXHk7KVCNqr2DpFqDArNgxdQXVDVEQxJNM9ZxhII3_esX5mRiEjkpBgqoq7nrVi_Il8fYqqFVyaas5Jf240W3zBqn2HFKSllJKGo0y5doeJ8W2_f9EbQxpxqS5QLmBDtebEpbusLeTwV_1uFNMUzaKmDdRInZhDABEOPgqHKFkLVMu47r513_oYXUkk3EYJUKKpiYW-yf6b5NOshx3kZs9kYrDJfp9SioAICuunqi7UPRs9okn1mW1PxqwbxEh1TasEHx8FHS29rVoHGUeyBKuBungsAbj4_TrMn17rOlzjeK-IDtRVfqm0fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم عنيف يدك مقرات المعارضة الكردية الإرهابية في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84306" target="_blank">📅 02:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84305">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07d9dc9b9.mp4?token=cMwyKcVEtM_-RorQXi1anniFNpBMNL87r00kAbi92ay-aLmPF3UqfAK8BLbDZFaMy2a2N1iT7xaJmhe0kiHWSOJb3Uv1pWVmDZ9bx_iEP5S5QFcF-iyIGoRhwsz-yXBrh09-a201arWIsILCfArpYSQEKbOFoLFORa4h3xdFzDevzKxJQkU3bsfboeP0CU9GBnXvj4mnmMoRic1Aj1dkRDxFidMs4lGATx7CYmzJeGWB3AjTcdKj8F79dTMTLj_1eX2o3wpW2f1arn-TMfgSdzX_CLewMETfYAA6LDC05ZyvzLI-2oSaCxhGtH1QvQJL1mugDW9UyMhCJWnOxuUZAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07d9dc9b9.mp4?token=cMwyKcVEtM_-RorQXi1anniFNpBMNL87r00kAbi92ay-aLmPF3UqfAK8BLbDZFaMy2a2N1iT7xaJmhe0kiHWSOJb3Uv1pWVmDZ9bx_iEP5S5QFcF-iyIGoRhwsz-yXBrh09-a201arWIsILCfArpYSQEKbOFoLFORa4h3xdFzDevzKxJQkU3bsfboeP0CU9GBnXvj4mnmMoRic1Aj1dkRDxFidMs4lGATx7CYmzJeGWB3AjTcdKj8F79dTMTLj_1eX2o3wpW2f1arn-TMfgSdzX_CLewMETfYAA6LDC05ZyvzLI-2oSaCxhGtH1QvQJL1mugDW9UyMhCJWnOxuUZAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجار في مدينة تبريز الإيرانية</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/84305" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84304">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4Su2avF8Lio5AcFBeofBe2DcMGvSyu6ErVCJeT2giUWF-QBi-EA3_QwUTA1ox06D5WPXeuZaPDVtHmKFLx8xjCjmJUCS0BBLDs7nG57GTvM7wwzNwMCKgON5eun5xsKvqIhx0sO611H1NMzBUPE0m4uB9Emrjd8gt5nRFGhppw6g82xtgo8T3ch_9Nh9YQScxJ9cGWys09V1jSWUTcf79TqGXL2wpZpIWE7ZUprNAVX7IS7UrQ7so5W_a1CiegRBzL8G0-AO3IbVACL6sKimsT0orehnFas5eobm92pxDIYeYlBVdodpC-kJ2j-i_9GVHc9bGcD-XOuDrwPLlSAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لا عزاء لنتنياهو و ترامب... إسبانيا تتغلب على الأرجنتين</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/84304" target="_blank">📅 02:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84303">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/84303" target="_blank">📅 02:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84302">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دوي انفجارات قوية في الكويت</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/84302" target="_blank">📅 01:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84301">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دوي انفجارات قوية في الكويت</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/84301" target="_blank">📅 01:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84300">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc48fae07a.mp4?token=ggKR5jz6562Kvr3mCX2FRgqOPQsVJOtgIn34plK9NDu8HIOE3UgROk7bhNyYO1tW4mc7HKxVg8Wnc4l4U8VGdS4_-68qVQYXY963aMeYDAZAxkk_XIv2vOxJhDVhkwXstvXRxIRr3t7kQeZeX8kXxOvk5bHKmTJeg6WIiihA54BnVmmbPokZGIxQiDj7BEsyhMSJkBMgVazDGjul0WhN45xLtc2bRw7dFc6tSt5TbGLkR1tMwQt9q5vnjEFSAMhYQXD5fZHd7FSmclpaFSJ1uHa4OgQzmdDGAsrdD2Do6CxmSDzZ-F8OMvn4ml4VhoyzlqBnGnxkt49XtkOsY8MQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc48fae07a.mp4?token=ggKR5jz6562Kvr3mCX2FRgqOPQsVJOtgIn34plK9NDu8HIOE3UgROk7bhNyYO1tW4mc7HKxVg8Wnc4l4U8VGdS4_-68qVQYXY963aMeYDAZAxkk_XIv2vOxJhDVhkwXstvXRxIRr3t7kQeZeX8kXxOvk5bHKmTJeg6WIiihA54BnVmmbPokZGIxQiDj7BEsyhMSJkBMgVazDGjul0WhN45xLtc2bRw7dFc6tSt5TbGLkR1tMwQt9q5vnjEFSAMhYQXD5fZHd7FSmclpaFSJ1uHa4OgQzmdDGAsrdD2Do6CxmSDzZ-F8OMvn4ml4VhoyzlqBnGnxkt49XtkOsY8MQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لا عزاء لنتنياهو و ترامب... إسبانيا تتغلب على الأرجنتين</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/84300" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84299">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_cX3eylwSaIviHwC7oaJO1UEaAK_Pp1ofCwJDe2Vz-RKaeCc9twBVAkRNZNK67Gi0bkienU3pGOwVe_a7Lnd5N5aMWjPlk2Fco-2JxVt4lFI-kqOQlh9hQ-VowpETuYChbKZgMEnBSzFeRZrIKyWzbkUnTlV3uwg9xzr149VvwKSgjASbJ5vsabKxzCC-EfxbInFfQ2Kcndlkuorovm9sDfnyH41PUWkNYdrvgl4fE7vL68876_kwmoA-GtA9T80pVNan2k40ajK7Adlavl-rl59xR_EapFAI1SQVXB2fAUu8mWnyL79xRKkmEy_iNNrEhavR-i6_Ic4ecjwG8Ecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
نتيجة إستمرار التوتر والإشتباكات في المنطقة..
أسعار النفط تتجاوز 90 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/84299" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84298">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1f0fpy8PfbOzFN7kcSmBxDtv2qjJZqUScBbk60DURUrLQ_afRx2zzOyex7bIDxfwTRCQb1Uiquf6IrtxtgPhfiUCK2hJg6jMPF2J6n-Q2J9kHuhZizF7LG0Ndd3MHintSqqn8XqaVNejIxFgthgcMmTI_VqzrIXALlV_dLR04Mi7d0_1KTBSZxiSLREE5P_EQz5_lhcSYLtUJoCCsxpNiBWRU9eQu6km7HCNAB1OkgTwOQhySF5adYRCPPwJGt8aALsTQdaHJQGQDHUPHPHUUq_8uK94NgfSU8P-pNODHVN3CYp4rQWxBL7JjNz8PrBZjBtRXvMtpYBbDNo6wZJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوارع طهران حاليا</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/84298" target="_blank">📅 01:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84297">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ka-aQoCzb6-Cqq7EMyzqFi4Q-sxqz2oSjnTl1gCKAeUXgGqPMXJhw3ql4Kogp1zGJ2Qz8pBKHpIoOJpUl6OyjXSARj0zP3JqC9GnVA6Eh82Q_6Eui0_fdB8RT667JKApgAA6hgcBkdaKgwuYva2NuqSVT3sArlIlMVXSE5k5eYV11YDdtU5_w-Jw6Twn23FBCc5qE2J3w8b669w3ZMQCzLqKpZknuw5K2_CFuVUypRDsQnzkXgUqN7BK78Ap94pV1-mOTvgn6Zn0b4HoEjBygu5j2-NoigHP-h76vPENfHyVzL2u54Np9AFFdT_R98_mun0BBCay78txEuxs-f9L4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
نحسی و شومی اگه عکس بود
..
@Naya_Press</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/84297" target="_blank">📅 01:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84296">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQmUR0FtB2I3SiwzXE_h7Jd83jq9kD0YZcdcgbneFamNJrFQsXtHzWPfPJxn9OzivA6QCLZ7ohU3foHEwlw8SxPeQytYqSMF2UX5lt2po6VxwpMtzoVWYez3ToaLUPqpkLsmrTkCXM7FMKPEfxPVJ8JwT8-SLpQ_70rFwRiyJBrWuysQnWJ465DNw6LvHEH4W5_6tcU_51gGN37xrD3dw_1MjMBtQJj3ktnlDoXFTyWfnGJmoc8X8GQvGHsv-R-PcyLjq2qXyangtVfRtX7moUQu_hFJwS6ySpq2yIIK3S2IPTry_sUKRq_NlGCqxfMTBZhgMCW32YlkJecPFa7EqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لا عزاء لنتنياهو و ترامب... إسبانيا تتغلب على الأرجنتين</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/84296" target="_blank">📅 01:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84295">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انطلاق نهائي كأس العالم بين اسبانيا والارجنتين.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/84295" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84294">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6w3xirKuVJtCHGdyYUkq3sC0CyjmN6HN6TY9mJ-adndxjgAjhppF5MyUljtxIwb_UZWANaUhBYdCJzQbP7J94x8KMlme4GaXkp_p6vO76IyWSCdC33wdRqoD_ghfK1l-03QPhcjQ3HteuVw7FceTioMZKAKWTgPK5ZeGJ-ZytjvYPJbBa2JGEaP1j1aU--a1hs9mkSDn-cCDNp3rkOMYfGOGcO2n04zI0CNznkBnhfNRbgdA6Z6ITmqpiVMMMx6ONl9hb2ptdhhATOMu3QJkviGf1or2WXkM42mXgMvw1YeFkiTlb72i7eAWo2lNOVdm23yOtsQtI6ACR8buoqzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحزن يعم أرجنتين حليفة ترامب والصهيونية</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/84294" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84293">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اسبانيا تدك حليف الصهاينة</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/84293" target="_blank">📅 01:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84292">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">كووووول</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/84292" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84291">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">كووووول</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/84291" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84290">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
المعارضة الكردية الإرهابية في كردستان العراق:
تعرضت مقراتنا إلى هجوم من قبل إيران بعدد من الصواريخ والمسيرات الإنتحارية.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/84290" target="_blank">📅 01:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84289">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مهزلة تحكمية كبرى !
الحكم يلغي هدف لإسبانيا مستحق على الأرجنتين !</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/84289" target="_blank">📅 01:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84288">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxXo6y_cdzKPgV7OJ-8PlWFpP-5AdVRnD3itCiN4Vf5MOu2UXFfFgyo41Vr-HNeDJondHkGREIJMsip7E_ZnWIKeHzcuEXVQX4wUSTobwLcwlQwm_QyqPrwXCkABV-7l_eSRiCVInn6TgxrAfLGWn6jrMt0bmnneJsIQWsGdA4ddltJj9q9RP_QUqa4fLpCmNx9Nm0QtLP12ByiaJHa7VcpDfNbteD3bwBcyp1sg6Ag8mI5wkei35lYr6882T87af0PROz_ifiM5MMwF0EUcgdArSgTX5LlaSkGAi9MkNWccbH6p7MHSXuge9Svd-oXKsqJLwsIBMvMlTiR44BXDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
المقاومة الإسلامية في العراق:
بسم الله الرحمن الرحيم
​تُجدّد المقاومة الإسلامية تأكيدها بالانخراط المباشر في المعركة ضد العدو الأمريكي إذا ما تمادى في توسيع عدوانه على الجمهورية الإسلامية، وأنها ستستهدف بكل قوة وحزم كافة المصالح والقواعد الأمريكية في البلاد والمنطقة.
​وفي هذا السياق، نلفت إلى أن المقاومة الإسلامية في العراق لم تُنفّذ أي استهداف عسكري ضد القواعد الأمريكية في العراق والمنطقة خلال الأيام الماضية.
​(وَمَا النَّصْرُ إِلَّا مِنْ عِندِ اللَّهِ الْعَزِيزِ الْحَكِيم)
المقاومة الإسلامية في العراق
20-7-2026</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/84288" target="_blank">📅 00:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84287">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OENxKnjTlcNogACUoaR2pkzc3eP1-X0jtXiBYlkQ2edQoiExP10g6XFvYjV_IaXQzNzrjs12eYL7F8kc8in1qn5gPt-VBhtbDeMJb6YS_F6DVfhOflAXkzMw7TepBgU5w6By90l1L5s9QcwqmezeJPoZf-jUUjD9GzVNeHvkHoNkwKSA9BPVplI7rGrf3WGILAI4E_j7ZHFZv9sR5suZwK70Y2kCViWcS8Qd9KXf-g-6hIEEiqF_o4-ZSmpT18dLmpshWackNQQJnQJ0aTtGhlsPEL1RvMiG0GaSFNjq0KETAa1-GHOX-TiBf3iMfziDLzcKv6SQGSzsa6htUJis4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
واشنطن بوست :
مسؤول أمريكي حذّر من أن توسيع العمليات الأمريكية سيظل محدودًا بسبب تناقص مخزونات أنظمة الدفاع الجوي والذخائر بعيدة المدى، إضافةً إلى القيود التي تعوق إرسال المزيد من القوات والطائرات إلى المنطقة نتيجة الأضرار التي لحقت بها بسبب المعارك. لا نملك ما يكفي لمواصلة العمليات بأمان، ولا أعتقد أن البيت الأبيض يدرك ذلك”، على حد قول المسؤول</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/84287" target="_blank">📅 00:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84286">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجارات عنيفة تهز البحرين جراء هجوم إيراني</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/84286" target="_blank">📅 00:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84285">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات عنيفة تهز البحرين جراء هجوم إيراني</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/84285" target="_blank">📅 00:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84284">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سماع دوي انفجار بقضاء كويا في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/naya_foriraq/84284" target="_blank">📅 00:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84283">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/84283" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/naya_foriraq/84283" target="_blank">📅 00:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84282">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">يا فاطمة الزهراء</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/84282" target="_blank">📅 00:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84280">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/84280" target="_blank">📅 00:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84279">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLUfisRos7iczuBobbczsrS4lXdzbYDIcBmgvSbfSyZjw0hvrqovio6UUX20uWs3ZSwUXGyl10gyOoq9Dyxaey4IS72Vx6vWRnzQ45LHgiO64kxCw8-8K5D_XmInRenRcmgADFG0gn9a1R69Yd1ELZ9MIs7loST9XWB-5pWZOVsKHZL24K-EycsxoVM6H9d8COccI_28Bfyjg3sSaVtahWvVsGaupmguLG29FQHfXPy3VZeQNIuyeregYJZJnXJrwdMb5pB-cJ7vTNCg_MzEXIbPzkHLKD4lQioavZ3JODy8EEf9_f66nI4i8jIj9zDDFUPXAzhXel39cyZigzexeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسقاط طائرة تجسس معادية في منطقة كهكيلويه بجنوب ايران من قبل الحرس الثوري الايراني.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/naya_foriraq/84279" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84278">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الله اكبر... اصابات في صفوف الجيش الاميركي في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/84278" target="_blank">📅 23:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84277">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02dfa7de95.mp4?token=n5QyRa1eq4dyGKZArdHhEb2qvJThXG2vh2FOloOZliO5w2oAXum2LHtcnsguONKqf8bkM-ygX9vPckYPdIOcBbQbRp_X9qdtOL6iICIEXZ1gipYnyj8Cl2K0oZPQS4Ufv9EMlfTilOF1GrUwi2Om-Ti_EFh9psR7sqrmZaOV13XengloNPmrCxuTBLiKIUwZmg7wtS4QcZRu0hp2a1U-ikCa_0isW-3Qts4psFvYq8XhKHoFO-IOTBBowgv_RG-MzSIF1didZR9zfbJf-CuyXJMSW6dou5Nhxb_AS5AV7xomlVz318mzS-0s7Lre-CkNjxXZstt2rJiFlKVvBPgAew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02dfa7de95.mp4?token=n5QyRa1eq4dyGKZArdHhEb2qvJThXG2vh2FOloOZliO5w2oAXum2LHtcnsguONKqf8bkM-ygX9vPckYPdIOcBbQbRp_X9qdtOL6iICIEXZ1gipYnyj8Cl2K0oZPQS4Ufv9EMlfTilOF1GrUwi2Om-Ti_EFh9psR7sqrmZaOV13XengloNPmrCxuTBLiKIUwZmg7wtS4QcZRu0hp2a1U-ikCa_0isW-3Qts4psFvYq8XhKHoFO-IOTBBowgv_RG-MzSIF1didZR9zfbJf-CuyXJMSW6dou5Nhxb_AS5AV7xomlVz318mzS-0s7Lre-CkNjxXZstt2rJiFlKVvBPgAew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Parents of U.S. troops, get your children out of the Persian Gulf region. Your president does not care about their lives.
We miss you man
#مرد_ميدان
🇮🇷
سرباز سردار قاسم سليماني</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/84277" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84276">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxObvp5OA5pL9e2B8ISC25h-rmPoePmMLWmJRC2b9ITda9oc2N1WNP5h8ewWIDRVRp0YKu1pSMbee5Ygh36edYgYk9Zfv9Aq58NhPhjDem-eSab6zb4WxKn-m0YEGbWBNNQ0JGcIVbqy-zMyzgWQ6S3IPMB15njrjBrYg2TMedRC6Azv_UhqkFxmmp9SP64suj85WrAZ5h1oM-vAv_EFT3toEJbnkYckbiru-iBwMcLTwEBcnm0mWubr-DCoCOwu9UZHvJXeic3C-drUUmuhDoDaCKwQlqwGlpcw0nsgM3CJa8tvAQY7IkVXjaJkB02D2Q7rK4hwXS2Qlccpg_Gwlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
Just imagine, study a lot of time in air dynamic , IT , Mechanical Engineering then The Lurs are taking this technology to reverse engineer and use donkey to cary the best US equipment MQ9</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/84276" target="_blank">📅 22:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84275">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الاعلام الاميركي: 16 عسكريا أمريكيا قتلوا وأصيب أكثر من 430 آخرين منذ اندلاع الحرب مع إيران في فبراير الماضي.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/84275" target="_blank">📅 22:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84273">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مقتل جندي امريكي بشمال العراق</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/84273" target="_blank">📅 22:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84272">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/84272" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/naya_foriraq/84272" target="_blank">📅 22:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84271">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مقتل جندي امريكي بشمال العراق</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/84271" target="_blank">📅 22:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84270">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/84270" target="_blank">📅 22:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84269">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/84269" target="_blank">📅 22:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84268">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مقتل جندي امريكي بشمال العراق</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/84268" target="_blank">📅 22:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84267">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انطلاق نهائي كأس العالم بين اسبانيا والارجنتين.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/84267" target="_blank">📅 22:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84266">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇺🇸
دفاعًا عن مقتل اثنين من أفراد الخدمة الأمريكية، رفض ترامب الانتقادات من خلال مقارنة الصراع بالحروب السابقة، وسأل:
"هل سألتم يومًا كم عدد الأشخاص الذين لقوا حتفهم في فيتنام؟ هل سألتم يومًا كم عدد الأشخاص الذين لقوا حتفهم في أفغانستان في يوم واحد؟"</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/naya_foriraq/84266" target="_blank">📅 22:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84265">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ace39da0.mp4?token=cE-rOYyV8NyY7Pa97UIVxDqlXbzaQb1PvI6iQ3RDFRXhZRWjbQHSfP2RRB9P3yp7AQ-Fq4A0g6uxYi24ucKZuauhvjs0BhS8S5AU0X5pPmuqWhBKI3WF1eKa5ZeTN8qX2AJkpKKDJEjW2iHL04469cS7gQS49zZtCketoRtuKe9WzfmsfMZhvPia6zFlmmdXYsvuprJsm5cAg4ujt8YuXAdVAcZZTyz_lRPdrFFSwhu8bmGSfpkvUcUdbYST54mIR-04xt9N58T8X6h5XXtm9c5I9aX7HUTxoLV9Aqwj6EPhv-QfS-qxo2iuReNrQZgUHmuw6WXfOVLHphN6msgsgVLZRxTAo89A6sV5cA_V7OT6K_zhqsvDXBPlDgdX8xdTvp-cyLC0AmPXjlqDBH-I_q83FWUXkWURjyAtYznPqRdIhOqGMNL0wyG-1V-lFC6qg6ZuLMsK4W5SQs3Tu-Ay5vUCXlkZ_JPihsOgV8pvcnhKxwe9QdSRsscZNg1frvxE_gcqD9ojRdIBBODhau8kkMdv00BYIgP9cKeOsc1uOVXwb0nqItrMZnodepgNeduQPbK6LhRlDMA8TNc07HFk_4fJx0UNzY8tgbvNQG0lvexqQSLpTC9lx6EDLoOKQ29GZmsml2QiGaC6HIYsHwq1UoJy19k0Y5Jarsg9kvDbBeE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ace39da0.mp4?token=cE-rOYyV8NyY7Pa97UIVxDqlXbzaQb1PvI6iQ3RDFRXhZRWjbQHSfP2RRB9P3yp7AQ-Fq4A0g6uxYi24ucKZuauhvjs0BhS8S5AU0X5pPmuqWhBKI3WF1eKa5ZeTN8qX2AJkpKKDJEjW2iHL04469cS7gQS49zZtCketoRtuKe9WzfmsfMZhvPia6zFlmmdXYsvuprJsm5cAg4ujt8YuXAdVAcZZTyz_lRPdrFFSwhu8bmGSfpkvUcUdbYST54mIR-04xt9N58T8X6h5XXtm9c5I9aX7HUTxoLV9Aqwj6EPhv-QfS-qxo2iuReNrQZgUHmuw6WXfOVLHphN6msgsgVLZRxTAo89A6sV5cA_V7OT6K_zhqsvDXBPlDgdX8xdTvp-cyLC0AmPXjlqDBH-I_q83FWUXkWURjyAtYznPqRdIhOqGMNL0wyG-1V-lFC6qg6ZuLMsK4W5SQs3Tu-Ay5vUCXlkZ_JPihsOgV8pvcnhKxwe9QdSRsscZNg1frvxE_gcqD9ojRdIBBODhau8kkMdv00BYIgP9cKeOsc1uOVXwb0nqItrMZnodepgNeduQPbK6LhRlDMA8TNc07HFk_4fJx0UNzY8tgbvNQG0lvexqQSLpTC9lx6EDLoOKQ29GZmsml2QiGaC6HIYsHwq1UoJy19k0Y5Jarsg9kvDbBeE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحمدالله كادر القناة يشجع رونالدو
😆
سييييييييييي</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/naya_foriraq/84265" target="_blank">📅 22:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84264">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏
رئيس مجلس الأعيان الأردني:
إيران تشكل خطرا على جميع دول الإقليم</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/84264" target="_blank">📅 21:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84263">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجارات في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/84263" target="_blank">📅 21:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84262">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الكويت تعترف بتعرض المصالح الأمريكية على أراضيها لاستهداف بالصواريخ الإيرانية.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/84262" target="_blank">📅 21:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84261">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇾🇪
بيان للقوات المسلحة اليمنية يوم غد إن شاء الله للإعلان عن موقف مهم</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/84261" target="_blank">📅 21:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84260">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
🇮🇷
انفجار في منطقة عبادان المجاورة للحدود العراقية.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/84260" target="_blank">📅 21:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84259">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">م/ توضيح
🔻
جمهورنا العزيز...
نؤكد لكم أن الفيديو الذي نُشر على أنه يوثق قصف محطة كهرباء الصبية في الكويت هو فيديو قديم ولا يعود إلى الأحداث الحالية.
ومن باب الأمانة والمصداقية الإعلامية نتقدم إليكم بخالص الاعتذار عن هذا الخطأ غير المقصود ونؤكد التزامنا بالتحقق من صحة المواد المنشورة قبل نشرها حرصًا على نقل المعلومات بدقة والحفاظ على ثقة متابعينا.
شكرًا لتفهمكم وثقتكم المستمرة.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/84259" target="_blank">📅 20:36 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
