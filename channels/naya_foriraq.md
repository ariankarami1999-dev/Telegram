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
<img src="https://cdn4.telesco.pe/file/Nxc5PnsBH-3as0en9R9lWgoNNF4q3ygeTCzYcMOCZ3BDboQVCMVW61nn9gEqrzHj-DgNIyswWW2A4MAKRtYItMU8TmmNzC-UJggTC-vDTSHUBo4Bm1Y3pDjn8T0gSucoNDet4-Bgalvx2fAK3lcqCWeHbYEDVB06aRVP45HTFRw03tXJi_IHWKCFWOGQ3UlDda3aznGdbzsZAJ03J7GpwnP7JDNNf4lJ3d7wVIhyq5fmNeMYaPxwwv7x3XzJnDKlm8W6eNDK2_7AA2lFGQP05CBkl1PVUSEI9GifmL8xz_52eFYB-OnDQpi4cbnHEMZfHrPDCShj4oM9JAW41bjl-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 259K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 12:20:57</div>
<hr>

<div class="tg-post" id="msg-78840">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هجوم على سفينة قبالة اليمن</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/naya_foriraq/78840" target="_blank">📅 12:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78839">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">هجوم على سفينة قبالة اليمن</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/naya_foriraq/78839" target="_blank">📅 12:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78838">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📈
الذهب يستمر بالارتفاع منذ إعلان الاتفاق بين إيران وامريكا حيث ارتفاع 3% منذ ساعات الصباح الأولى ليسجل 4,343 دولارا للأونصة.</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/naya_foriraq/78838" target="_blank">📅 12:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78837">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bd22030f1.mp4?token=oUjnn4pUZctHE42rX4EKmJ7JtJD19C__y2T0chNXjUBDOoYom0ZkWIzuEmRItgqLMnvoSSIXTwBRQ3A1MXDbJsi7H5EqRKfofr7UhY6AKKyQZNhvdFkcqHjys743lnt_mEAfg6WD5fFElR5lCddWrN6gGhnh7TWIcJ2-RH776WBViETwcwaOAJZUP6y_M_8cMnToRnfbovmwsPP3_-9u57ANoVOma1pbppRnGWo0DD8Wv0-ezbkNi49J6xPenn3ueS69MVfdLE7ln8NPs7h3eEKgFzK-OtsadTfzFmCPFSPgWqwCKXZieAWmCCzbOBR-F1_DnIrRwjj7roj718QU8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bd22030f1.mp4?token=oUjnn4pUZctHE42rX4EKmJ7JtJD19C__y2T0chNXjUBDOoYom0ZkWIzuEmRItgqLMnvoSSIXTwBRQ3A1MXDbJsi7H5EqRKfofr7UhY6AKKyQZNhvdFkcqHjys743lnt_mEAfg6WD5fFElR5lCddWrN6gGhnh7TWIcJ2-RH776WBViETwcwaOAJZUP6y_M_8cMnToRnfbovmwsPP3_-9u57ANoVOma1pbppRnGWo0DD8Wv0-ezbkNi49J6xPenn3ueS69MVfdLE7ln8NPs7h3eEKgFzK-OtsadTfzFmCPFSPgWqwCKXZieAWmCCzbOBR-F1_DnIrRwjj7roj718QU8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال يتركون خلفهم دباباتهم وآلياتهم المدمرة على جانبي الطرقات قبل انسحابهم من الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/naya_foriraq/78837" target="_blank">📅 11:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78836">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHTrZYGoJ3rqooaAJhNvrw0bNrzk6L8brw8lL1tA6xI3DDdlSFOsJRmf-56PsbdPG2xTxUMxl5mAsEn01uPo12TGqy5knvcW26rUuq8mC1444OBAoiLHRaQWOt-T06Qi8aHZ7dxxeRiph5LuLDsHB3gMphbItbI-gdhYHUDErHeSTxVdn2yi9vMKIqelzywGb4YqutvkpjksRj2f0pjzJa9o0wdhQf0fjYBd86LXVO12EIt6624EKSNUdtzFuuR6JWSSSVSUoP5xsfkwClAQ64a5I-Ikhj__Hl8W4GR5TcW0uSMjP8D02muSpbuor72xNNmejGkfBtEaqj0_yDrH_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
بعد اتفاقية إيران وامريكا خام برنت يستمر بالهبوط حيث وصل سعر البرميل الواحد إلى مايقارب 82 دولار لأول مرة منذ أكثر من 3 أشهر.</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/naya_foriraq/78836" target="_blank">📅 11:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78835">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رئيس الوزراء البريطاني يعلن حظر استخدام وسائل التواصل الاجتماعي لمن هم دون سن السادسة عشرة</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/naya_foriraq/78835" target="_blank">📅 10:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78834">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7cc2b4e15.mp4?token=gENDs2jicVD7681NCuVrPzZgihTu0kM04yUQiyqMbgU2ph969J5Nya9rE00EYJRA1HbewXs6sj4qgoS1ZywjjXaMaaiI19h40xDLahRZ2AIWJSEk4_kceE32-JJd0nKpYXXFET-UrmwLHcCu7XUeqoEqOn13TN_w-mwC2q4elYKO-Aty662Hlh1tYkLrAGxno06mgRLPxoZhNNPxQunyNCvGQUavZaqHNHFLQgmRbEr8QwIJvfcxbPUYztwFjHTX6YjTY68cmvgFHh7RCJ91WelfbgFeMFEsCkNTwefrdptmDv_uRZ4mNqU0MVeXMhIRXS-7RI_pxrCkz9qC2AZuKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7cc2b4e15.mp4?token=gENDs2jicVD7681NCuVrPzZgihTu0kM04yUQiyqMbgU2ph969J5Nya9rE00EYJRA1HbewXs6sj4qgoS1ZywjjXaMaaiI19h40xDLahRZ2AIWJSEk4_kceE32-JJd0nKpYXXFET-UrmwLHcCu7XUeqoEqOn13TN_w-mwC2q4elYKO-Aty662Hlh1tYkLrAGxno06mgRLPxoZhNNPxQunyNCvGQUavZaqHNHFLQgmRbEr8QwIJvfcxbPUYztwFjHTX6YjTY68cmvgFHh7RCJ91WelfbgFeMFEsCkNTwefrdptmDv_uRZ4mNqU0MVeXMhIRXS-7RI_pxrCkz9qC2AZuKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚢
مشاهد من عبور أول ناقلة غاز ترفع علم مالطا من مضيق هرمز بعد الاتفاقية بين الولايات المتحدة وإيران.</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/naya_foriraq/78834" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78833">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
العراق يعطل الدوام الرسمي يوم غد الثلاثاء بمناسبة رأس السنة الهجرية.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/78833" target="_blank">📅 10:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78832">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏴‍☠️
رغم جهود ترامب وتوسله لسريان الاتفاق مع إيران.. وزير الدفاع الصهيوني يعلن عدم انسحاب الكيان من المناطق المحتلة في لبنان وسوريا وغزة إلى أجل غير مسمى.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/78832" target="_blank">📅 10:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78831">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ba9c4c71.mp4?token=k_waQ6oV3MckeU2xGOCn74EbGPSZ4jRyNX87CCeXoA5NLcAL0xi5kTHXRT3MDukHEcZTqxsKJceJE-AmuudPGTBIbVRPR24MgOxRqj6nF4xKyyzQt_WrndS98yU7DMj6MpUqLg_8di9Oq_eZCOEfmFLh9usTCLOrmgbfqKq5T12clrutmszuOqhjp3v-eTk5CGrA10kS0wldsJvwRElJtVVawjHHsqe7Ux_qDRfXGgGZ5jVRQ_YhUiLNbf6lYkxMtrXuTD-AFYs3W0ROzDGoGQtx32Pv210Y_m0GUkJGcytD4UDJCdaKeNXCXKH0t3GuAL2ev8knEdVUh7H7M5g1Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ba9c4c71.mp4?token=k_waQ6oV3MckeU2xGOCn74EbGPSZ4jRyNX87CCeXoA5NLcAL0xi5kTHXRT3MDukHEcZTqxsKJceJE-AmuudPGTBIbVRPR24MgOxRqj6nF4xKyyzQt_WrndS98yU7DMj6MpUqLg_8di9Oq_eZCOEfmFLh9usTCLOrmgbfqKq5T12clrutmszuOqhjp3v-eTk5CGrA10kS0wldsJvwRElJtVVawjHHsqe7Ux_qDRfXGgGZ5jVRQ_YhUiLNbf6lYkxMtrXuTD-AFYs3W0ROzDGoGQtx32Pv210Y_m0GUkJGcytD4UDJCdaKeNXCXKH0t3GuAL2ev8knEdVUh7H7M5g1Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال يتركون خلفهم دباباتهم وآلياتهم المدمرة على جانبي الطرقات قبل انسحابهم من الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/78831" target="_blank">📅 07:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78830">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf0d0b85af.mp4?token=lemi9Y76SJb0Lau9UnPfloL7-DnH8nNHhhNodmCgNsNEU0xE3_vjwyE_ZYeD0XQT7-NqVUyrB9P4MF03ohy61BU91BvXLF2aaOMLFezBUqq_lmOJkAFfD_QwF_DgM_wEmPztUhomWbHsiNBSqE-pkp-swHZfB40vL6GqjCQ4k_NW6s9lbiZh6ciwxVY95luUkk1GeOviAOjGniL-RVn9fJXZJtLPQuCfI9FjmE7rWMloSe0W9D3DdbhmPdCLjHIEA5HujD4gHuf3YAUkGhO7hSWwjYaS9_Z1g3hyXXmXNRMmJYTHrLNv85-lndQxujK-rASyEdiLvqew09UPKSGOpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf0d0b85af.mp4?token=lemi9Y76SJb0Lau9UnPfloL7-DnH8nNHhhNodmCgNsNEU0xE3_vjwyE_ZYeD0XQT7-NqVUyrB9P4MF03ohy61BU91BvXLF2aaOMLFezBUqq_lmOJkAFfD_QwF_DgM_wEmPztUhomWbHsiNBSqE-pkp-swHZfB40vL6GqjCQ4k_NW6s9lbiZh6ciwxVY95luUkk1GeOviAOjGniL-RVn9fJXZJtLPQuCfI9FjmE7rWMloSe0W9D3DdbhmPdCLjHIEA5HujD4gHuf3YAUkGhO7hSWwjYaS9_Z1g3hyXXmXNRMmJYTHrLNv85-lndQxujK-rASyEdiLvqew09UPKSGOpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
على الرغم من وقف إطلاق النار.. جيش الاحتلال الصهيوني يستهدف بلدة كفرتبنيت جنوب لبنان.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78830" target="_blank">📅 07:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78829">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🌟
الاعلام الاميركي:
قال ترامب إن الولايات المتحدة وإيران لا تزال تتفاوض على التفاصيل الرئيسية لاتفاق نووي نهائي، بما في ذلك ما إذا كانت طهران ستعلق تخصيب اليورانيوم لمدة 15 إلى 20 عامًا.
وقال إنه بموجب أي اتفاق نهائي، سيقتصر استخدام إيران لتخصيب اليورانيوم على المستوى المنخفض، "والذي لا يمكن أن يستخدمه أبدًا الجيش".</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/78829" target="_blank">📅 02:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78828">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M17agmZ-xygmmhxFYdN4HTNRTP7iytU23vNtUw_2C4f3ZaiSFafH20V9y-Ju4OJL96oWwEVXo-4gCcDYqXbtny92Y5_WH0LlZrh0kBM-a8fu7-m0YBtIs3DWxkYbYVmhF3eWo20WO3sx7tHfcZgIDD0PBBRgyhzKF00VSwsIbrVXCqZ31fJDuC77iTRrSGXrIc9xFlE_LESkJFAO3HGE5JC23otyKeLT39JDziSTXq5n4Ns_98sZbtAsl0DcL51dFt0J5BEkiwE3-l1Lv8j-hrWbnymCLMM8fopANBLxFSkDQ-ltgaUaQMMAYm1ahd6ybTfKMuKGgDUoja6yn6ffAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جميع الاطراف اعلنت وقف العمليات العسكرية، ننتضر الكويت
😆</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/78828" target="_blank">📅 02:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78827">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
بيان أمانة المجلس الأعلى للأمن القومي بشأن اتفاق إنهاء الحرب بين إيران والولايات المتحدة بسم الله الرحمن الرحيم  إلى الشعب الإيراني الكريم:   لقد استكملت الجمهورية الإسلامية الإيرانية، بقيادة قائدها الشهيد، تفوقها على العدو الصهيوني الأمريكي، وبتوجيهات المرشد…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/78827" target="_blank">📅 02:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78826">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b0380fc8.mp4?token=Sp330Of_56zeOmuAfaI2H7Za0K5J_3vW3_nAT_NwYDbvJYiykB2k1vwoExeylskGyUgfDTMJvj9lOYbHAg7MEA_NK7rqPecx4byKXtvzgG0enMQdD_lBiBaVQ6zeMj6C7Q1gbIj-SgSggEvchwbiHugEu36noneKfB4cgjlGEH_txbz3Cr679CdqYjpi9K8rLv4WogSqUZzvCPiy2ADLBoELWOcAXRusF-kicsk7LJ5vQn1QTeNqA51qdDNp5-3nRjufKGjn5YeWLq-4O4uVZFIse-sSkzWn0M75kM9w7hLxwU630roXsKGQCdOY_emS-H2mdmL3sVvlI4S7ODlBUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b0380fc8.mp4?token=Sp330Of_56zeOmuAfaI2H7Za0K5J_3vW3_nAT_NwYDbvJYiykB2k1vwoExeylskGyUgfDTMJvj9lOYbHAg7MEA_NK7rqPecx4byKXtvzgG0enMQdD_lBiBaVQ6zeMj6C7Q1gbIj-SgSggEvchwbiHugEu36noneKfB4cgjlGEH_txbz3Cr679CdqYjpi9K8rLv4WogSqUZzvCPiy2ADLBoELWOcAXRusF-kicsk7LJ5vQn1QTeNqA51qdDNp5-3nRjufKGjn5YeWLq-4O4uVZFIse-sSkzWn0M75kM9w7hLxwU630roXsKGQCdOY_emS-H2mdmL3sVvlI4S7ODlBUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
عمدة كييف: انفجارات في العاصمة. قوات الدفاع الجوي في حالة تأهب.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/78826" target="_blank">📅 02:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78825">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
بيان أمانة المجلس الأعلى للأمن القومي بشأن اتفاق إنهاء الحرب بين إيران والولايات المتحدة بسم الله الرحمن الرحيم  إلى الشعب الإيراني الكريم:   لقد استكملت الجمهورية الإسلامية الإيرانية، بقيادة قائدها الشهيد، تفوقها على العدو الصهيوني الأمريكي، وبتوجيهات المرشد…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78825" target="_blank">📅 02:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78824">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇷
"سيصدر البيان الرسمي لأمانة مجلس الامن القومي الايراني بشأن اتفاق وقف إطلاق النار قريباً". ‏  وفقًا لهذا التقرير، بعد الهجوم على منطقة الضاحية في بيروت، ألغت إيران مفاوضاتها وكانت تستعد لمهاجمة الكيان الصهيوني. إلا أنه في نهاية المطاف، وبفضل تنازلات قدمها…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/78824" target="_blank">📅 02:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78822">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e22b6bfdd.mp4?token=anoHzXUNsrV67Vsh8_LKK3MjF0XtnR6mAvX5Mja-ZVZl2bxaUliiI2ku9Myf9ifOZdlTGlSiwC0YH4dCpnGHgvyeFYuC7T3OFE8VjdMzxnkLFAmFECHKdJLewmxZ75znpAZP19WiE0rwiHbU0PYW-sfQihHfgkfLlOnX_U4mfOl8YnZX2-C7j6uP80mxMdQ43XI2EdYjQICaBhtQjU9a58HQwDoPup_lcVBuDxOFHwlm0ywKUysAAVvQKBfB_b0W8MYr_05AmBLq_w6ayI0Eltkl5pNLK0MJBDix-enefRFIOM6Np1XjD9TpHn5cY0v6uYStZEB--LDaDdmrg-xU5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e22b6bfdd.mp4?token=anoHzXUNsrV67Vsh8_LKK3MjF0XtnR6mAvX5Mja-ZVZl2bxaUliiI2ku9Myf9ifOZdlTGlSiwC0YH4dCpnGHgvyeFYuC7T3OFE8VjdMzxnkLFAmFECHKdJLewmxZ75znpAZP19WiE0rwiHbU0PYW-sfQihHfgkfLlOnX_U4mfOl8YnZX2-C7j6uP80mxMdQ43XI2EdYjQICaBhtQjU9a58HQwDoPup_lcVBuDxOFHwlm0ywKUysAAVvQKBfB_b0W8MYr_05AmBLq_w6ayI0Eltkl5pNLK0MJBDix-enefRFIOM6Np1XjD9TpHn5cY0v6uYStZEB--LDaDdmrg-xU5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
افراح تعم شوارع لبنان بعد انتصار ايران وحلفائها على الامبريالية الغربية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/78822" target="_blank">📅 02:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78821">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏
تفاصيل جديدة لمسودة مذكرة التفاهم المكونة من 14 مادة بين إيران والولايات المتحدة الأمريكية"
تفاصيل هذا المشروع هي كالتالي:
‏1- وقف دائم وفوري للحرب على جميع الجبهات، بما في ذلك لبنان
‏2- التزام الولايات المتحدة بعدم التدخل في الشؤون الداخلية لإيران واحترام سيادة الجمهورية الإسلامية الإيرانية.
‏3- رفع الحصار البحري بالكامل في غضون 30 يوماً
‏4- التزام الولايات المتحدة بسحب قواتها من المناطق المحيطة بإيران
‏5- إعادة فتح مضيق هرمز خلال 30 يوماً وفقاً للترتيبات الإيرانية
‏6- تعليق العقوبات المفروضة على بيع النفط والمنتجات البتروكيماوية والمشتقات، ومنح إيران حق الوصول الكامل إلى مواردها المالية.
‏7- ضرورة قيام الولايات المتحدة وحلفائها بتقديم خطط لإعادة إعمار إيران بقيمة لا تقل عن 300 مليار دولار
‏8- 60 يوماً من المفاوضات للتوصل إلى اتفاق نهائي قائم على القضايا النووية والرفع الكامل للعقوبات الأمريكية الأولية والثانوية وقرارات مجلس الأمن التابع للأمم المتحدة ومجلس محافظي الوكالة الدولية للطاقة الذرية.
‏9- إعادة تأكيد التزام إيران بموجب معاهدة عدم انتشار الأسلحة النووية بعدم إنتاج أسلحة نووية
‏10- خلال فترة المفاوضات، التزمت الولايات المتحدة بعدم إضافة قوات في المنطقة وعدم فرض عقوبات جديدة.
‏11- الإفراج عن 24 مليار دولار من الأموال الإيرانية المجمدة خلال فترة المفاوضات النهائية التي تمتد 60 يوماً. ويجب توفير نصف هذا المبلغ لإيران قبل بدء المفاوضات.
‏12- تشكيل آلية إشرافية لتنفيذ الاتفاقية.
‏13- سيتم إقرار الاتفاق النهائي بقرار من مجلس الأمن التابع للأمم المتحدة.
‏14- لن تبدأ المفاوضات النهائية قبل الإفراج عن نصف الأموال الإيرانية المجمدة، وتعليق العقوبات النفطية المفروضة على إيران، ورفع الحصار البحري، وسيقتصر الاتفاق النهائي على مصير المواد المخصبة وتخصيبها، ورفع العقوبات، وخطة إعادة الإعمار الاقتصادي لإيران. وقد تم استبعاد المناقشات المتعلقة ببرنامج الصواريخ الإيراني ودعم جماعات المقاومة بشكل نهائي من جدول الأعمال.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/78821" target="_blank">📅 02:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78819">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQWflgE8mXcGpdxjfBZ7QdmIfKxr4uraJm2W9T313jtZ3bjQautOJj4fNPldjsAa-tvxS08CLsSjI3WtnW4fdxTR_BCAYXcVlmVqMNfYXeBTEyVo5Qsol9xx9qhEFczADOoIayuTQ80r81Kf7c3dfm1a3j3uCxjwCZnRaVSHbC0r3B-3CSKL-P-m1CcVoR9z4UvVQQdEAQBvefagVqiy3zZwjqQSBg5hbMot_3-g5r5EyUt6i9qukYJu470ah0jT1pfGH5m3_R19Mvkll0zoaL7ZIKR-qYjt0m0MmJn-SuawX7xLKNOd7BWJN7cTCTo-Ui9eo3U83knZUNo-gOEvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب
:
"هذه الاتفاقية العظيمة ستجلب السلام والأمن للمنطقة بأسرها. لقد حاول العديد من الرؤساء إحلال السلام مع إيران، وفشلوا جميعًا قبلي. لقد وجد قادة المنطقة، ولأول مرة، رئيسًا قادرًا على مساعدتهم في تحقيق سلام حقيقي. مع فتح المضيق بتوقيع الاتفاقية يوم الجمعة، لأغراض إزالة الألغام، سيتدفق النفط من كلا الجانبين مجددًا إلى المنطقة والعالم! الرئيس دونالد جيه. ترامب"</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/78819" target="_blank">📅 01:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78818">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">المقر المركزي لخاتم الأنبياء:
إن شعب إيران الصامد الفخور، وأبناء الوطن البواسل في القوات المسلحة القوية وجبهة المقاومة، بعون الله تعالى وتحت قيادة القائد الأعلى للقوات المسلحة، حفظهم الله، قد فرضوا إرادتهم الإلهية القوية على الأعداء الأمريكيين والصهاينة، مُثبتين أنه لا خيار أمامهم سوى قبول الهزيمة والاستسلام أمام شعب الله وجنوده.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/78818" target="_blank">📅 01:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78817">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22771bd849.mp4?token=aJjojStJAikcLF1fBuna9n81v3aRA2m3gmBUEh5YPm2WFlfQGljiOuPh1_-cM_KTMM9Cmlg5EX5sxBhZsKNBz5JoGrG8dE2Qq-yPy9rCV09EJzT4iOYzK-rcQOHc1pMxclppAcX9DcwaMkOT2P-1JBbE_WHgT-qS8Fb7TybCWj16KINovJpUWYNhgPDb04uFHc-0b9V2NtHYuk-Azl_yiFmTdQYn8N-ma-4HsV8EqrrKotdz2t3TJZ9MSQfxJUzNhqOytOWXoREXTQeHnilGCxcBc70bwsm5ABxD5HRAqHVvvw0SNFIPCiA1l_8-bJsCrGhGOSlV9CHB3AiDUeRrlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22771bd849.mp4?token=aJjojStJAikcLF1fBuna9n81v3aRA2m3gmBUEh5YPm2WFlfQGljiOuPh1_-cM_KTMM9Cmlg5EX5sxBhZsKNBz5JoGrG8dE2Qq-yPy9rCV09EJzT4iOYzK-rcQOHc1pMxclppAcX9DcwaMkOT2P-1JBbE_WHgT-qS8Fb7TybCWj16KINovJpUWYNhgPDb04uFHc-0b9V2NtHYuk-Azl_yiFmTdQYn8N-ma-4HsV8EqrrKotdz2t3TJZ9MSQfxJUzNhqOytOWXoREXTQeHnilGCxcBc70bwsm5ABxD5HRAqHVvvw0SNFIPCiA1l_8-bJsCrGhGOSlV9CHB3AiDUeRrlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقف العمليات العسكرية بجميع الجبهات بما فيها لبنان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/78817" target="_blank">📅 01:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78816">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وقف العمليات العسكرية بجميع الجبهات بما فيها لبنان</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/78816" target="_blank">📅 01:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78815">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏خام برنت يهبط إلى أدنى مستوى منذ مارس</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/78815" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78814">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">أسعار النفط تتراجع بأكثر من 3% بعد إعلان التوصل إلى اتفاق بين الولايات المتحدة وإيران</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/78814" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78813">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH9kFRpYHm9MslatpbZ2mhW7f5TZnjaLTgDEdBdQpvmBBJl-fB1lWY1jsu_O7kvwYxc_FNNVJG0hnMwFpT4jF1GcbOFbpgDpal_1h8gWFFJC7AABnzsyDyXXYY9cebUebrh0r5-KGbkYhxiMqOzPU50BBH8-oHfiUCrTB3ioxfhLR8mCg6YOxDROkmNbdI71rt6W4esyoX8NCTCqZyYDi16WvcAyZBimT-PJEsm7SLtJhpzT_WrS1f5WD3HWE3g-qi_4UpN8iJaBPiPeRWxn-4vXfViMRhS8FQZYRTJkz-Fefd332UYWLp20z2vsl979nCBm_4a4xwHuamByJYhi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أسعار النفط تتراجع بأكثر من 3% بعد إعلان التوصل إلى اتفاق بين الولايات المتحدة وإيران</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/78813" target="_blank">📅 01:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78812">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇦
عمدة كييف:
انفجارات في العاصمة. قوات الدفاع الجوي في حالة تأهب.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/78812" target="_blank">📅 01:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78811">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الايراني:
كانت تهديدات إيران الليلة فعّالة في دفع بعض بنود نص المفاوضات.
ساهمت بعض الإصلاحات المنصوص عليها في التفاهم، إلى جانب الأحداث التي جرت في لبنان وتصريحات القوات المسلحة، في تقدّم أعمال المفاوضات.
كانت القوات المسلحة على أهبة الاستعداد لردّ حاسم.
كما اتخذ ترامب مواقف وانتقد الكيان الصهيوني. وردّ حزب الله أيضاً بقوة وحزم على العمل الإرهابي الذي ارتكبه الكيان الصهيوني.
ساعدت السلطة العسكرية والتهديدات التي وُجّهت في إتمام صياغة النص ودفع بعض القضايا التي كانت تُعيق إتمامه.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/78811" target="_blank">📅 01:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78810">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🌟
‏
فانس
: سأذهب إلى جنيف للمشاركة في التوقيع على الاتفاق مع إيران</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/78810" target="_blank">📅 01:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78806">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وقف العمليات العسكرية بجميع الجبهات بما فيها لبنان</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/78806" target="_blank">📅 01:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78805">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
"
سيصدر البيان الرسمي لأمانة مجلس الامن القومي الايراني بشأن اتفاق وقف إطلاق النار قريباً".
‏
وفقًا لهذا التقرير، بعد الهجوم على منطقة الضاحية في بيروت، ألغت إيران مفاوضاتها وكانت تستعد لمهاجمة الكيان الصهيوني. إلا أنه في نهاية المطاف، وبفضل تنازلات قدمها الرئيس الأمريكي دونالد ترامب في اللحظات الأخيرة، بما في ذلك الحفاظ على وحدة الأراضي اللبنانية، وانسحاب إسرائيل من الحدود اللبنانية، والرفع الفوري للحصار، اقتنعت إيران بالعدول عن تنفيذ هجومها.
‏ كما تقرر أيضاً أن يتم تنظيم النظام القانوني للملاحة في الخليج الفارسي بالتعاون بين إيران وسلطنة عمان.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78805" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78804">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الله اكبر...طهران الحليف الذي لا يترك حليفه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/78804" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78803">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
‏
تسنيم
: المسؤولون الإيرانيون سيتحدثون عن الاتفاق مع أميركا خلال دقائق.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78803" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78802">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8Ald28Am92ElBq3VbhIAF41z159U1tKk1LPGdp1D6xIYxgnYNoy1UOdvJu8vPNxow6GViOzKxB8ppHBzKs_a37ASv29vy8nyXEi81I6kEFJVo7inMpoOgT_-YUsAN3OtGwvAl30Tz3z4B8j2uJdv71Mvh7Q82PcTlISsrBGKFZTRi9L2bpIEDdRgcnmsnVssPWaZQGki084LAbks7p4rhShwb-wI8WXoAEumOmthfadwFaPdBlQ2ZnLUPmSHEa2iEtzJd6F7kJrAIXFcbM9yO3C8vnjHRQ7vea_-g9-CAfEeP_2Rsn0Ky_0uQK6ogCKzPrJEOBq5y2DqKOMiyuR3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب
: الاتفاق مع جمهورية إيران الإسلامية قد اكتمل الآن. تهانينا للجميع! أفوض بموجب هذا بشكل كامل فتح مضيق هرمز مجانًا، وفي الوقت نفسه، أفوض بإزالة الحصار البحري للولايات المتحدة على الفور. سفن العالم، أشعلوا محركاتكم. دع النفط يتدفق!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/78802" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78801">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نحن جنود الدين والعقيدة...لبنان لن نتركها وحيدة
#شاركها</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/78801" target="_blank">📅 00:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78800">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
🌟
🌟
رئيس وزراء باكستان: ‏يعلن تم توصل الى اتفاق مع واشنطن وطهران بعد مفاوضات مكثفة، يسرنا أن نعلن عن التوصل إلى اتفاق سلام بين الولايات المتحدة الأمريكية والجمهورية الإسلامية الإيرانية. وقد أعلن الجانبان الوقف الفوري والدائم للعمليات العسكرية على جميع الجبهات،…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78800" target="_blank">📅 00:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78799">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وقف العمليات العسكرية بجميع الجبهات بما فيها لبنان</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/78799" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78798">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
🌟
🌟
رئيس وزراء باكستان: ‏يعلن تم توصل الى اتفاق مع واشنطن وطهران بعد مفاوضات مكثفة، يسرنا أن نعلن عن التوصل إلى اتفاق سلام بين الولايات المتحدة الأمريكية والجمهورية الإسلامية الإيرانية. وقد أعلن الجانبان الوقف الفوري والدائم للعمليات العسكرية على جميع الجبهات،…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/78798" target="_blank">📅 00:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78797">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Peerx7D_hApUkkjjkEt2hWZqBQbXep0pMbsg-NbbgN7oeZhbSSALEA4ydeMrGZZyRR1z2UDlrYNJHYIAo39Eqtcc1zWymYN_zj_1bf8O67R1Oij83F1kflcljGzJ4lT8vm4KmUhSn26PyAzIlKUswXuk_ndGsOSxZW22My_1M32Lqsipl-ASwwVAUMYUqlZKOVpA_xJm4T61Cadt3MlW0ASCHYPLhg6tWNuwEuWmZ3Yi4HnSCNlunZ9tLDYvybLBWz1xbuJneNiVy-Id8RqR2j4LKZ2MXrSrXVKf8-np7lBwDPO1iLEx5_D3ZYvohxyU5xy4EnHxURhTWtMmQJvfIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
🌟
رئيس وزراء باكستان: ‏يعلن تم توصل الى اتفاق مع واشنطن وطهران
بعد مفاوضات مكثفة، يسرنا أن نعلن عن التوصل إلى اتفاق سلام بين الولايات المتحدة الأمريكية والجمهورية الإسلامية الإيرانية. وقد أعلن الجانبان الوقف الفوري والدائم للعمليات العسكرية على جميع الجبهات، بما في ذلك في لبنان.
‏سيقام حفل التوقيع الرسمي يوم الجمعة الموافق 19 يونيو في سويسرا.
‏نتقدم بالشكر الجزيل للولايات المتحدة الأمريكية والجمهورية الإسلامية الإيرانية على التزامهما بإيجاد حل دبلوماسي للنزاع. كما نتوجه بجزيل الشكر والتقدير لإخواننا في جهود الوساطة هذه، وللقيادة الرشيدة لدولة قطر، على دعمهم في التوصل إلى هذا الاتفاق. وأخص بالشكر القيادة الرشيدة للمملكة العربية السعودية وجمهورية تركيا على إسهاماتهما الجليلة في هذا الصدد.
‏بعد إبرام الاتفاقية، سيتولى الوسطاء تيسير سلسلة من الاجتماعات هذا الأسبوع. وستضع هذه المناقشات التمهيدية قبل التنفيذ الأساس للمحادثات الفنية وحفل التوقيع الرسمي.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/78797" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78796">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌟
ترمب يتنازل عن ابرز اهدافه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/78796" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78795">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏ترمب: سوف يتم رفع العقوبات عن إيران بموجب الاتفاق</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/78795" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78794">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامب يشير إلى عدم استعجاله في إزالة المواد النووية من إيران، ويؤكد إمكانية حدوث ذلك لاحقاً</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/78794" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78793">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامب: الحصار البحري على إيران أكثر فاعلية من الضربات العسكرية</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/78793" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78792">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامب يشير إلى عدم استعجاله في إزالة المواد النووية من إيران، ويؤكد إمكانية حدوث ذلك لاحقاً</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/78792" target="_blank">📅 00:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78791">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏ترمب بعد ما يأس
😆
: لست مهتما بتغيير النظام في إيران. -‏سأتحدث قريبا عن الاتفاق مع إيران</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/78791" target="_blank">📅 00:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78790">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏
ترمب بعد ما يأس
😆
: لست مهتما بتغيير النظام في إيران.
-‏سأتحدث قريبا عن الاتفاق مع إيران</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/78790" target="_blank">📅 00:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78789">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏴‍☠️
الإعلام العبري:
واشنطن تسعى لتوقيع اتفاق مع إيران يمنعها من الرد على هجوم الضاحية.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/78789" target="_blank">📅 00:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78788">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇸🇾
‏
مستشار الجولاني:
أميركا اقترحت علينا التدخل في لبنان.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/78788" target="_blank">📅 00:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78787">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnJ1wFcirONuuRRxpgZFAmElQUDTrVf3NNHtmcVTFx-ClkibwoJ-M9BALgWLwuvIw6vSql3HXnOYx-IGQzJL0YfvJEmfxGT0bZIIghlo5IWWdDcFwzSBWr92GNVrJjHocVKPM2qsB0I_zZQdePUQPwt378XOdM1aT0_9_WTNOdPbXaPgTvlpJal9wnGY2UVKVcUjHJ1S1sn76YrAP0jZeWz0BNdie_OmdQE34Nu5n8QFuj--nas6kPcSOsAy7RGnXd9VY8ME4WamjQ2KeuUD3jhBaG-pLvsd3PTUS19pi6FaR9Sr0QgTwsLjOrZddbqKOWy_tf8UOStfqd_86deKJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
لن تمتلك إيران أسلحة نووية أبدًا، وسيتم فتح مضيق هرمز للأعمال التجارية قريبًا جدًا!!!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/78787" target="_blank">📅 00:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78786">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be1f8c2a4.mp4?token=U0r7BX4B2J9LjekhQVgpE1GAXC47eMGuhCFoc0kF_UfcH7Le32KxM3x5PHE9n7AiInAkHBCe0plfm_nSaTIjz3eUyNsr3PTY9JpOptLa0Djdmd_xXX-t9GvTFbSczXJzg-fWw19CL8y4Lp7-Uen_hK4u6DeB7Ujtm3H2Oh8F_Jti37pY_GFD1bq3UF6r0l2yRh1k_BF6Fym06re1HsvdvKSCLP7qSPgG89tBZ9ITpRr9jMSrttJylLkGO7Y8I44nGxnuoOeQ26KgT5go-nz0IbWSJtalzDmsLuyhK84t2sYGXqep_pZ-UAEU9VOvJMvPg24NDEBuDYLq6MGqAv9qTwW0qyN8iBayjYPOt5HgrGr87vvmv-sIMGmY7EH2cQRbOoa06zKLYKc01FI6d9D3TPZaZ6UYexyoY8zX1WLmqnMKIvLqvMdt40pgog-tNs2JNGjQK-NmePFu9WIp7dGLo4lxgs-0QAAhhyq3joJmenQNR0yssoQTQFx7LLhrEIIj0geoqbkO-4ujiaaVplQNFtAwW1N3WBL02pDq4D3s9NOZat3lPXNhN82vGR6wLtcVewSoa_vZuWzbl1P4XwDrWX1h6sNj6UPXwTssaHDkmJfsaLBPYG7AieB4GI_VFhE1QSjssBVeqw8w5fux0rSltY3Reij56H_fYhPiQoFM3bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be1f8c2a4.mp4?token=U0r7BX4B2J9LjekhQVgpE1GAXC47eMGuhCFoc0kF_UfcH7Le32KxM3x5PHE9n7AiInAkHBCe0plfm_nSaTIjz3eUyNsr3PTY9JpOptLa0Djdmd_xXX-t9GvTFbSczXJzg-fWw19CL8y4Lp7-Uen_hK4u6DeB7Ujtm3H2Oh8F_Jti37pY_GFD1bq3UF6r0l2yRh1k_BF6Fym06re1HsvdvKSCLP7qSPgG89tBZ9ITpRr9jMSrttJylLkGO7Y8I44nGxnuoOeQ26KgT5go-nz0IbWSJtalzDmsLuyhK84t2sYGXqep_pZ-UAEU9VOvJMvPg24NDEBuDYLq6MGqAv9qTwW0qyN8iBayjYPOt5HgrGr87vvmv-sIMGmY7EH2cQRbOoa06zKLYKc01FI6d9D3TPZaZ6UYexyoY8zX1WLmqnMKIvLqvMdt40pgog-tNs2JNGjQK-NmePFu9WIp7dGLo4lxgs-0QAAhhyq3joJmenQNR0yssoQTQFx7LLhrEIIj0geoqbkO-4ujiaaVplQNFtAwW1N3WBL02pDq4D3s9NOZat3lPXNhN82vGR6wLtcVewSoa_vZuWzbl1P4XwDrWX1h6sNj6UPXwTssaHDkmJfsaLBPYG7AieB4GI_VFhE1QSjssBVeqw8w5fux0rSltY3Reij56H_fYhPiQoFM3bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
عمليات قتل وتصفية لمواطنين سوريين على يد عصابات الجولاني الإرهابية تشهدها منطقة كفرتخاريم بريف محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/78786" target="_blank">📅 23:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78785">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVsYC0Nr5vDltElORvjD3LQwyeXiSU8nRDYCW5BE7Rtdz46iAtWF4NAVRuBfvG9WRc6_RxthSMuUc11OWp1kJmA_1gAa6mhyn57XJSX_KcaF3t4YPvaOy8nDqRGw3R2dDeQnHEz6nFgMi380dIbJ0dabhrNUWBHiHgHby0FZoMIBYUUpLnGq_ZEivcXOHWAJFO_zwigXBgArioW3FZlAvtebRfy7NS9FAt73acO3x1uiwaNaVlI-0B5MjZvq-XfnglHlwUtqiVEzG1oyz3qyDY3ud0GF4WKJOGH4hEP6TmM0xEWnWyGDZjVeGrbkZWBVUbNBp_jqah30Qbj6Y5lrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
كذب السيناتور جاك ريد، الديمقراطي من رود آيلاند، عندما صرّح بأن الاتفاق الذي أبرمناه للتو ليس جيدًا مثل كارثة أوباما المعروفة باسم خطة العمل الشاملة المشتركة. ريد إما محتال صريح، أو غير كفؤ. كان اتفاق أوباما طريقًا لإيران لامتلاك سلاح نووي، بالمال وكل شيء، وهو أحد أسوأ وأغبى (ومن هنا الديمقراطيون!) الصفقات التي أبرمتها الولايات المتحدة على الإطلاق. اتفاقنا هو جدار ضد امتلاك إيران لسلاح نووي، وهو عكس اتفاق أوباما تمامًا. اعزلوا جاك ريد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/78785" target="_blank">📅 23:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78784">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⭐️
الإعلام العبري: تدرس طهران تأجيل ردها المخطط بإطلاق الصواريخ على إسرائيل لإعطاء جهود ترامب للتهدئة فرصة والتوصل إلى اتفاق إطاري محتمل الليلة.  تقوم قطر بوساطة المحادثات، حيث تفيد التقارير أن أحد المقترحات يتضمن إزالة الحصار البحري على إيران فوراً وإعادة…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/78784" target="_blank">📅 23:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78783">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
وزارة الاتصالات العراقية: موافقة الشركات المنفذة لمشاريع الـ(FTTH) على مقترح زيادة سرعة الانترنت للمشتركين بنسبة ‎%‎20 بنفس السعر  -الزيادة ستمكن شركات الـ(FTTH)  من تقديم خدمات ذات مستوى عالي الجودة مما يلبي إحتياجات كافة المواطنين.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/78783" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78782">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭐️
الإعلام العبري:
تدرس طهران تأجيل ردها المخطط بإطلاق الصواريخ على إسرائيل لإعطاء جهود ترامب للتهدئة فرصة والتوصل إلى اتفاق إطاري محتمل الليلة.
تقوم قطر بوساطة المحادثات، حيث تفيد التقارير أن أحد المقترحات يتضمن إزالة الحصار البحري على إيران فوراً وإعادة فتح مضيق هرمز بدلاً من تخفيفه على مراحل.
وقالت مصادر إن إيران خططت لتنفيذ ضربة صاروخية في المساء، ربما توقيتها خلال البث التلفزيوني الرئيسي، لكنها أجلتها عدة مرات بعد تلقي رسائل مباشرة من ترامب.
حذر ترامب من أن أي هجوم يؤدي إلى دورة أوسع من التصعيد قد يعرض المفاوضات للخطر ويترك إيران مسؤولة عن انهيار الجهود الدبلوماسية.
يقال إن الرئيس الأمريكي يدرس تقديم تنازلات إضافية للحفاظ على المحادثات وتأمين اتفاق.
وقال مصدر أمني إسرائيلي إن رئيس الوزراء بنيامين نتنياهو توقع أن يؤدي هجوم بيروت إلى تصعيد وإخراج الدبلوماسية عن مسارها، لكن المفاوضات استمرت على الرغم من الحادث.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/78782" target="_blank">📅 23:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78781">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvXVA8E-C6OBpgoWPbZBBsPYJaSEERQ4xqmaY7STRIAjRjOmhihUUwZczBBxHnGbXJ6_YuuAQC2dYbYMWBmH5KBSanv4HAzp28ifxkxJHL9qeS7Pay9ThEAwPF4hyMVkNT0A58lSSS5wsbmUYcb3no_fKfK5CVnYORJGsB8HuJH7WmTNdzvTqsqfVVBWZsVLkK--hXSRMGIxz34vHn5VCMqqzHX4gl4JGZgjdYB_kUjN4SxW_swSuVUOfibUM1QXzUldQP_nIwKZrtWyfe4Lpq29nOuAZH9LeqXDrGe0aA4rIVxaW4pSIx1M8d8Zkz-x9sV1XE0h8YbTtDomdtHpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
أجسام مضيئة في سماء تل أبيب المحتلة.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/78781" target="_blank">📅 23:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78780">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌟
🏴‍☠️
أستهداف دبابتي ميركافا وآلية بوكلين ومستودع ذخائر دبابات لجيش الإحتلال الصهيوني في بلدة مجدل زون بجنوب لبنان.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/78780" target="_blank">📅 23:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78779">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSMLSPFvd6CiY1HPg6d_YmAAU55TaoUSds8hfcDTnYGzmKXb5CwZbYjQqqGx7uceyN3i-i2TPkqk7OkZRckyfTFbnJexUbYTFMesxVvBzTQ9xBuNls1W6oK2F0XT3ULRQKo2HRK-mg9HNHlw8pDhQGUM4k9aDxrnFylMz9IMwqUdvTcp5rczYxNZZ3Xh1Bg_iGDaM6UiuvG_wXfg3-8B_EoGhHrrqlj7MKYO1iDoY1zhwH3k8bKEiXAnw-s_rzHODVHe3IWnlAMkVtJ_2R5p2xtgWqJvhkNvipwZ5qJMjyi0OcyO6ENeytbF3cdkzTTPUdrVUgfs6nWMwmccyrUiBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏
وزارة الخارجية الإيرانية:
"بيان وزارة الخارجية بشأن استمرار جرائم الكيان الصهيوني في الهجوم على ضاحية بيروت".
‏تدين وزارة خارجية الجمهورية الإسلامية الإيرانية بشدة العمل الإرهابي الذي قام به الكيان الصهيوني بعد ظهر اليوم، الأحد 14 يونيو 2026، في العدوان العسكري على منطقة سكنية في ضاحية بيروت، والذي أسفر عن استشهاد وإصابة العديد من المواطنين اللبنانيين.
‏إن هذه الجريمة الإرهابية ليست مجرد انتهاك صارخ للسيادة الوطنية والسلامة الإقليمية للبنان فحسب، بل هي أيضاً انتهاك جسيم لاتفاق وقف إطلاق النار المؤرخ في 8 أبريل 2026 بين إيران والولايات المتحدة.
‏إن الجمهورية الإسلامية الإيرانية، في الوقت الذي تذكر فيه المسؤولية المباشرة لحكومة الولايات المتحدة عن الجرائم التي ارتكبها النظام الصهيوني والانتهاكات المتكررة لوقف إطلاق النار من قبل ذلك النظام ضد لبنان أو إيران، تؤكد عزمها على اتخاذ جميع التدابير اللازمة لممارسة الحق الأصيل في الدفاع المشروع عن النفس.
‏من الواضح أن مسؤولية العواقب الخطيرة التي يترتب عليها خرق النظام الصهيوني للسلام والأمن الإقليميين ستقع على عاتق الولايات المتحدة والنظام الصهيوني.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/78779" target="_blank">📅 23:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78778">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561b7e384e.mp4?token=t3JkWHXLblChfVoL5TmmQZLzbxNjIGCZtqN9N9pX75j5b8TvItXpNsfFbdQbvrxaw-vB1p-rHOIB-MX1NYexHQ6glOK4bIluBldU9s86_k_zLrLok1XaF1Dc_Qt7UUd8UJBM4vI4-SjMwIguxQZ-9PTiesHkiSCxLOKmGmhmzN1I3FFL9G8O_KaGRg8nihyC1F4E-B7FyQup7k00itHO4ckiZmGFeCLIrZ1P5IVCNy9FeqRtpLndmtLsqSsPUaKUT3RAwOx7_UwUe2vniCVcd00Tq254oKwxzdhK3tXAQfgUyqNDtlG42v_gPB5vHC13UkJ90v_t8T6PA_erebyPZ2haZDDioIZMyv1BUzx1L4892aefyGn_9mzLQ7SnZ98D9Dm8psp-gvckU6h52yymkIJLrmB2gWSAnC9dO78i0SePId5YL3IRDbp-lsDh9RRR5-MRAWcbPD2ehExaxzeELupis1ukiKKtX1gcAKXVlOmVgxniGDDukIKVq2LvQfRHjsjsKcambqNJ7fQtpeoTuAHmL38CXVomoBQ302dgNCa9oJFaoNCPXgleyWcztD6s_SpDbjwIrUncCXQcSPCA01ivAbElFclBDZhdoiceirwnc7v5a39tP49XoDqMtKaQV4ysiRfKIdcbODHJK2dc6fAnjcYrpgDVCT1TADN1s4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561b7e384e.mp4?token=t3JkWHXLblChfVoL5TmmQZLzbxNjIGCZtqN9N9pX75j5b8TvItXpNsfFbdQbvrxaw-vB1p-rHOIB-MX1NYexHQ6glOK4bIluBldU9s86_k_zLrLok1XaF1Dc_Qt7UUd8UJBM4vI4-SjMwIguxQZ-9PTiesHkiSCxLOKmGmhmzN1I3FFL9G8O_KaGRg8nihyC1F4E-B7FyQup7k00itHO4ckiZmGFeCLIrZ1P5IVCNy9FeqRtpLndmtLsqSsPUaKUT3RAwOx7_UwUe2vniCVcd00Tq254oKwxzdhK3tXAQfgUyqNDtlG42v_gPB5vHC13UkJ90v_t8T6PA_erebyPZ2haZDDioIZMyv1BUzx1L4892aefyGn_9mzLQ7SnZ98D9Dm8psp-gvckU6h52yymkIJLrmB2gWSAnC9dO78i0SePId5YL3IRDbp-lsDh9RRR5-MRAWcbPD2ehExaxzeELupis1ukiKKtX1gcAKXVlOmVgxniGDDukIKVq2LvQfRHjsjsKcambqNJ7fQtpeoTuAHmL38CXVomoBQ302dgNCa9oJFaoNCPXgleyWcztD6s_SpDbjwIrUncCXQcSPCA01ivAbElFclBDZhdoiceirwnc7v5a39tP49XoDqMtKaQV4ysiRfKIdcbODHJK2dc6fAnjcYrpgDVCT1TADN1s4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 01-06-2026 تموضع جنود جيش العدو الإسرائيلي على الأطراف الجنوبية لبلدة دبّين جنوبيّ لبنان بصاروخٍ نوعي.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/78778" target="_blank">📅 22:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78777">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvEjaqGUyFQkNwukjXlDFWSSbxfLPLGY2m2GXar6WnnHzBEjmu_KkKuCO76GvHa5qXKrx3l1r37KIg_ZKJ9zfM6qFJ-AWyOKzkr7SRCIcNK6ROLRKLaUorn5yer1CUz5clMxJyecCAKr3DizhR-dQS2AznWh21yErf-GjPH3JTf_Zd0zDukSlpHslROtbs0GM0gme46W4wutA3YScXysCKvbRY8dFLNeWV0agoFtOPj7KbhFBrBWsHD_dFQ6UCN9gGs79qCKnWItFqKOB6bekpOyo1BQVgjJjb_Vq6woUprfUb_DkE8EdtojnjFx5ol7wxvnMd-jZ-pR8TB2BHuEkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
ضمن سياسة بني أمية في اقصاء الشيعة واستهداف مقدساتهم..
عصابات الجولاني الإرهابية تهدم وتزيل جامع وحسينية في قرية الركة بريف محافظة حمص السورية.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/78777" target="_blank">📅 22:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78776">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpKzV2qKJy9c3EzVqLK0h1Ir3Coti5zCFsocF0JTq3x8gmGO90xZrPpLyUwZMvMbEygHDgH0LhTqHAj6FKuNnOXeXN4aHBvMUdtOxcty1LSKnnkck3-LqP7unk3s6oj_XJ_OV3YB6b44Dyu4QkXzDJ0wKDQ2Bnp-umgGWYwzmMRKZAG5zjAB3rEy1wo7vAYtq1vW5PUCBGdY9At8hLNjU3odpkHw0DeHkiNFsVnUgqiMT1UO19sGZfdgnfwNgwsVDWaQNmEO8wIWNAwdfDSeMBdA6HpxhXv5XKqIgnc4jAoE_XLGZLIJFt0915hVVTY8npc6Ce7ePzmz3tbBC6muXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف:
لن يتمكنوا أبدًا من السيطرة على أي جزء من قوات المقاومة بمفردهم؛ فجهود المقاتلين اللبنانيين الشجعان والدبلوماسية القوية للجمهورية الإسلامية الإيرانية ستضمن سيادة لبنان الحبيب ووحدة أراضيه، وستُحبط لعبة النظام الإسرائيلي المجنونة والمُثيرة للحرب.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/78776" target="_blank">📅 22:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78775">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
الغاء جميع الرحلات في مطارات غرب إيران.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/78775" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78774">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
الغاء جميع الرحلات في مطارات غرب إيران.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/78774" target="_blank">📅 22:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78773">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
المطار ملك للشعب العراقي
قرار سيادي عراقي بإبعاد الشركات الأجنبية والاستثماريّة بمطار بغداد والذي يعتبر واجهة البلد …</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/78773" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78772">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN-mlgPzzrtl6kz_J4Un3MObB69lx4bcPhBevh7TyYSkQ58LbnOhn_meWDs2A5xCoWB9JE99GTD0ck2TLGPpTczBtq-HbxrS1KRcYP2wZn_bg4ynRKgtE0hEkPI9ba2U9J3yrwJIixDZ5CyRYQJev9HwSXLW5Gd1ca52ZaPuZi69BzS2WP8qV3UaHPadkwQrDCZG7g-zjl_XQmOdQf7X2z9Gm_GcCnIroSioZqAOq20nOQxx7pW3OrQgJ-wOqb9R_L0nh8FnRASIekPNhiyLGJ6vBZqHGDtTsmAcvESaCf1G4m7s88E5C013blar6-ZroB0P8SJGOErUisTwsA81gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
عدد قليل من الدوموقراطيين ضد FISA، مع أو بدون بيل بولت يذهب إلى DNI، كممثل. أي نوع من الصفقة هذا. إلى جانب ذلك، أنا ضد FISA إذا لم يأت مع قانون إنقاذ أمريكا (النسخة الكاملة!) مرتبط به بقوة. اجعل أمريكا عظيمة مرة أخرى! شكرا لك على اهتمامك بهذه المسألة.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/78772" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78771">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حدث خطير
عملية تجسس لصالح ايران داخل الكنيست الصهيوني</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/78771" target="_blank">📅 21:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78770">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">السلام على شهلائي</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/78770" target="_blank">📅 21:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78769">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Homayoun Shajarian - Iran e Man (همایون شجریان و سهراب پورناظری…</div>
  <div class="tg-doc-extra">Melodifa</div>
</div>
<a href="https://t.me/naya_foriraq/78769" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">السلام على ايران وشعب ايران المقاوم
#شاركها</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/78769" target="_blank">📅 21:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78768">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-DUzhnMGuW0Kkmwao-Y33FjDiqkuo5htjwW0NvRR-HZsWVY4veCX_7W8-tVZwH8Gp-rrrH6kivN7rhhJA2ItbCQmzVyWJtHcFAXDsoIF1D1DYadbRVeWIRbEBOvr49Vd4E62U9IKeXut9AoiyG99M2d31QA0wOeFnLqx8onFG152fBPeV2ZGDyIls0E9MJth0YxglGmEJQgw0Wq6uyVz_PD6a2SLFOVNbiDBu20zd1T-WHY_EsSfSPYxwrctiarhUDq39yFBvM4CXjcLEDJEX1uxYCUovFvwEvZaDWgwvmYytaB7GnOlVBM2WlM5YphiiNbgTX_OFSQwYXuCBFO8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/78768" target="_blank">📅 21:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78767">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAexB5PlIq1QnoRYYAOBt5ixO3ud8nz0hZ4U6BS8aPTeTgN2uAKccFd10qdy1DGNhQjoGUzyMqKPjUe96CJnNIx4w_ZmIVMJe9EQ005xLBJPA5ZT8JdHKwmOZjHob9mzOx9XiejS6ySsvdME1dbVuGLzVxz4OJB6udzJ1Nk1_JDwlF21WXN40JFhzgr5F5EmAGt6au2jBTvaGmZPEwkY4oifvkIJ1K7tb8PnImzZwJJ24-t1hdDOFCWYlhCnj6QB_GWwmccJNSCwfrVnq-mXn3XhVO_a_4fbxVCrmdfF4I3XTbySBI37BS__nMWl5iwjuPOKphBi6_HgWOiyv-cTpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
أمين المجلس الأعلى للأمن القومي الإيراني:
ردّ جند الإسلام قادم. ‏لقد شكّلت وحدة الصفوف سلسلةً أمنيةً لحماية المنطقة. ‏لبنان هو روحنا، ولن يُتسامح مع انتهاك الخطوط الحمراء للجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/78767" target="_blank">📅 21:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78766">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31ab1b676a.mp4?token=bdGlOY7_YXgYjdcRR9C-Zob3j3uvQfMo4Ka01596bD8vYXM54LqENfV0h-8B8fD2DWydoG-SbSyuArDkL4wNrnS5FwCBiSjjo0U4nRAmdcagQFf5be4bIP8WPkDH4qr-rx8I2jbghr055jtGbE5gOtc82NqBM_yRQWdyWJRcUfY90Z7Ou6AfWldUCgeyrW2mGCB5YOd7U2hU1SjdcMQMd6xlsEN6I-gnJmpv_1JWoppUl6RsClft5myrWJnkz6kjnSRLJm1yEra4qm3cT90eKj6dH-wfTOgxMGFvOAWGEM_juu6a4Z4o3Mbx24Sp8tLT85WHGY7ZaJZIzpkPJnHmow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31ab1b676a.mp4?token=bdGlOY7_YXgYjdcRR9C-Zob3j3uvQfMo4Ka01596bD8vYXM54LqENfV0h-8B8fD2DWydoG-SbSyuArDkL4wNrnS5FwCBiSjjo0U4nRAmdcagQFf5be4bIP8WPkDH4qr-rx8I2jbghr055jtGbE5gOtc82NqBM_yRQWdyWJRcUfY90Z7Ou6AfWldUCgeyrW2mGCB5YOd7U2hU1SjdcMQMd6xlsEN6I-gnJmpv_1JWoppUl6RsClft5myrWJnkz6kjnSRLJm1yEra4qm3cT90eKj6dH-wfTOgxMGFvOAWGEM_juu6a4Z4o3Mbx24Sp8tLT85WHGY7ZaJZIzpkPJnHmow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
عمليات قتل وتصفية لمواطنين سوريين على يد عصابات الجولاني الإرهابية تشهدها منطقة كفرتخاريم بريف محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/78766" target="_blank">📅 20:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78764">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee3f06f50.mp4?token=PqjRe98bELT1p9EEF9_q8nS4YSkNRCHRKdvT3rjVPeTwPhIg2HxG8jS9jPBwRhLv2gbMYfhGXN8UCTbSbn3--gd8xOirpk9JW29NLo6webjHhih84zLLFSZGP-lYYKJ8J3BXmqQa58lU4tDdEh21YbvIMLO2-fGFyo35zb07vKCIcdBOCEyaQWodl0kzBeydT2ke0JIw0dz_xHhdb_wqF6-WHfQPLZWt5LcRz2WMYEchc0CJXd0n_NKOZnvE5alt3DGRXljXeJLjOvzswqXnUcZSwOzbJoO_auIXRXwWNYbpM2532FQzuW8Sp5vZlL1tnPIZoxUkPrVmgcg8DsBePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee3f06f50.mp4?token=PqjRe98bELT1p9EEF9_q8nS4YSkNRCHRKdvT3rjVPeTwPhIg2HxG8jS9jPBwRhLv2gbMYfhGXN8UCTbSbn3--gd8xOirpk9JW29NLo6webjHhih84zLLFSZGP-lYYKJ8J3BXmqQa58lU4tDdEh21YbvIMLO2-fGFyo35zb07vKCIcdBOCEyaQWodl0kzBeydT2ke0JIw0dz_xHhdb_wqF6-WHfQPLZWt5LcRz2WMYEchc0CJXd0n_NKOZnvE5alt3DGRXljXeJLjOvzswqXnUcZSwOzbJoO_auIXRXwWNYbpM2532FQzuW8Sp5vZlL1tnPIZoxUkPrVmgcg8DsBePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
عصابات الجولاني الإرهابية تقدم على تعذيب وقتل مواطن سوري بتهمة الإنتماء إلى النظام السابق في منطقة كفرتخاريم ضمن ريف محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/78764" target="_blank">📅 20:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78763">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIuNzSwZ8S7RK2vpKyZdhyIhmuM5qsb-7LRUvi__32S6gHvcTbmYw0qX95w3cwdfM8ZP6ticyJj7c6O-puDYvpDREbMx889rJFqgF0Pv-AYQtj_BgDYu307ewvY4qe3InB12wLoA9BM-kXK8jqUhe5JRGJa8sMndoKWT8_xbIUrjG6UhCopgWPUG6a2ZY5P_wTvc_X9ivzh6bYh5SVv-vzGF1SsweQX0HFXd_PBzH7v2nyF8PJMM4httwRp_MRmdxQLqY3WHMkIqHic95XuHWsUKOcbwUwtA3MVl9-QdMyELXLQS-T3bd_0ephBe_rDVUO8TIEUCt6AfT78aq7noiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف آلية لجيش الإحتلال الصهيوني في بلدة الطيبة بجنوب لبنان.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/78763" target="_blank">📅 20:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78762">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
قائد المقر المركزي لخاتم الأنبياء:
أبناء الوطن في القوات المسلحة على أهبة الاستعداد لاستهداف قلب العدو وأيديهم على الزناد.
لقد شكّلت مقاومتكم ونهضتكم فصلاً جديداً في التطورات الدولية، وأرست دعائم الجمهورية الإسلامية الإيرانية كقوة عالمية مؤثرة. أبناؤكم في القوات المسلحة، ولا سيما القادة الشهداء الذين تخرجوا من مدرسة الإمام الخميني (رضي الله عنه) والإمام خامنئي الشهيد، اعتبروا ولا يزالون يعتبرون الكراهية والعداء مع الكبرياء والصهيونية جزءاً لا يتجزأ من طبيعة الثورة الإسلامية منذ اليوم الأول للحركة.
🔹
إن أحداث العام الماضي، من حرب الأيام الاثني عشر إلى حرب رمضان، ورغم الخسائر الفادحة والمفجعة التي خلّفها استشهاد الإمام، قد أتاحت للقادة الأبرياء وللشعب فرصة عظيمة لتصفية حساباتهم مع المجرمين. لقد أنزلت القوات المسلحة بهم، بدعم من الشعب وبتوفيق من الله، ما يستحقونه.
والآن نعلن بكل جدية:
🔹
إن قدراتنا القتالية والدفاعية والصاروخية والبحرية والمسيرة والجوية أقوى من أي وقت مضى، وقد تم تعزيزها بأوامر القائد الأعلى للقوات المسلحة، سماحة آية الله السيد مجتبى الحسيني الخامنئي، وأبناء الوطن في القوات المسلحة على أهبة الاستعداد لإطلاق النار على قلب العدو.
🔹
لن يُنسى أبدًا هدف فتح القدس والثأر لدم الإمام الشهيد؛ فنحن ننتظر أدنى هفوة من العدو المعتدي لنلقنه درسًا لا يُنسى.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/78762" target="_blank">📅 20:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78761">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
وزير الاتصالات مصطفى سند يعقد اجتماعاً مع الشركات المنفذة لمشاريع الـ(FTTH) ويطرح مشروع زيادة سرعة الانترنت للمشتركين بنسبة ‎%‎20 وبنفس السعر.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/78761" target="_blank">📅 20:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78760">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الإسرائيلي:
في أعقاب الإنذارات التي تم تفعيلها قبل وقت قصير في عدة مناطق في شمال البلاد، تم رصد سقوط إطلاق صاروخ عبر من لبنان في منطقة نواعت مردخاي، وسقوطات أخرى متعددة في المنطقة التي تعمل فيها قوات جيش الدفاع الإسرائيلي في جنوب لبنان.
بالإضافة إلى ذلك، قبل وقت قصير، تم رصد عدة سقوطات أخرى لأهداف جوية مشبوهة في أراضي دولة إسرائيل، بالقرب من الحدود مع لبنان.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/78760" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78759">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRJCQ52kGKLY5Ijw4_de-hv8uAMLibLBckj9F5inOKkM677pXmi6Ly51CFS0Ng7oSaLeV1g6JVrontcOhdg3vAH4c_YjbXFlEcyEh6wY_C8O0KC49qWCe2NCI4c_SpPcuDKULLFwswX1o3SoaH_h6DWFxu6gRGVQNqOruFPSAhHBfRhnsL2eFA5HB0sYzujq2EKNKjQt8DfNuaFBxKcvWLfxWdx8XiK4EbS7nQHKmF_imcUnP5XJxKqSmr-eoO16Z9AMzrvydVEaJ5lexffd4jCT81VdJGvMjLxLAo1ur99u0Q-96hoJQw8VEJRPX8soCimDQkQtLGSehYMC7V6mTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇺🇸
إيتمار بن غفير يتحدى ترامب ويطالب نتنياهو الإستمرار:
السيد رئيس الوزراء، كن قوياً وشجاعاً، ولا تخف أو تيأس.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/78759" target="_blank">📅 20:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78758">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇶
وزير الاتصالات مصطفى سند يعقد اجتماعاً مع الشركات المنفذة لمشاريع الـ(FTTH) ويطرح مشروع زيادة سرعة الانترنت للمشتركين بنسبة ‎%‎20 وبنفس السعر.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/78758" target="_blank">📅 20:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78757">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
🇷🇺
ترامب أبلغ بوتين بأن الاتفاق مع إيران بات قريبا وبوتين أعرب عن ارتياحه لقرب انتهاء النزاع.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/78757" target="_blank">📅 19:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78756">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏ترامب: توقيع الاتفاق اليوم سيكون إلكترونيا وبعد أسبوع حضوريا في أوروبا.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/78756" target="_blank">📅 19:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78755">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامب: لا يوجد لدى بيبي أي تقدير أو حكمة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/78755" target="_blank">📅 19:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78754">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b5cad09f.mp4?token=FHaqpS_IJZQZInVk6bbS50TsO03jpkVcgddxnogsgBCmBIyUg-o5c4bewbIenJ7ahfF_rHtNPdLKPrj3EuCtoH2HFvvxAV6dJPQ7Y3mvhb11m9Xo68x-IPssRVrS8N8V5MYxujMksBDN7g4PUwnIbnhtFgK4QtYYwMhDWCTHWQ2fd6EhNkqDcDLLvpz7_tqvQnxPh31H0t1KtIfXNNt8v2t2w7xN-prGSXjZeNE9i9vk23VKT5hOB1tuGLeQDtv0hXDssYRku-p2yYN1919-mh9lC7Bdbfcweerf6VN12P8sV-unCJdC4jzj0gajoqCueHMHKK5BTl9tvZ7loVeR_X72y8xOw1Pct94ZelXiBV7pbI0JFMFgVRFO79NCurtvSHeEqy9G3nLvdYvY8BqK0QNKZ9owZHaRqsf-bhTmlCVjWttchXBS5_OJm_sxXSwrjpr4xQSzPbK3DJbZKLJzxpMImdO_FV35TDm9Zumaw23GWhe2GscqIbe8sVKENiA02Dw7KFXSInirUeQvPKMl469Y8t9JAGImNMIPc0GhFiBiinIhCwQhnOG4dU3sPQ7O7tReU8lyY2qaaHQbHZK-6MmLYMJN97YyyKvqncL07vMN8jCKLyIYhnRNO5fp54UGiK1Y42-SqtxwyJ0N3I_5QJ_buHGZu5MmuYfgJbayQfY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b5cad09f.mp4?token=FHaqpS_IJZQZInVk6bbS50TsO03jpkVcgddxnogsgBCmBIyUg-o5c4bewbIenJ7ahfF_rHtNPdLKPrj3EuCtoH2HFvvxAV6dJPQ7Y3mvhb11m9Xo68x-IPssRVrS8N8V5MYxujMksBDN7g4PUwnIbnhtFgK4QtYYwMhDWCTHWQ2fd6EhNkqDcDLLvpz7_tqvQnxPh31H0t1KtIfXNNt8v2t2w7xN-prGSXjZeNE9i9vk23VKT5hOB1tuGLeQDtv0hXDssYRku-p2yYN1919-mh9lC7Bdbfcweerf6VN12P8sV-unCJdC4jzj0gajoqCueHMHKK5BTl9tvZ7loVeR_X72y8xOw1Pct94ZelXiBV7pbI0JFMFgVRFO79NCurtvSHeEqy9G3nLvdYvY8BqK0QNKZ9owZHaRqsf-bhTmlCVjWttchXBS5_OJm_sxXSwrjpr4xQSzPbK3DJbZKLJzxpMImdO_FV35TDm9Zumaw23GWhe2GscqIbe8sVKENiA02Dw7KFXSInirUeQvPKMl469Y8t9JAGImNMIPc0GhFiBiinIhCwQhnOG4dU3sPQ7O7tReU8lyY2qaaHQbHZK-6MmLYMJN97YyyKvqncL07vMN8jCKLyIYhnRNO5fp54UGiK1Y42-SqtxwyJ0N3I_5QJ_buHGZu5MmuYfgJbayQfY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 02-06-2026 جنود لجيش العدو الإسرائيلي عند الأطراف الشرقيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78754" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78753">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🌟
🏴‍☠️
حزب الله يعلن عن استهداف دبابة ميركافا في محيط بلدة يحمر الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/78753" target="_blank">📅 19:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78752">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p66DY2b2ZdOEzvirAzTmSTHNSb23YnX42gOcky_iIzoN9oiex6cK16W7pD6XR8ZS0yt2ASClIcRrr8mkMu9ODbEIvobfok59JMgJrN9Q9ABSrz9RIy4zG3uFRqd6bNkPZUfk_snI7bJk2Gm6hBJuN_zh6mjgGWlH-nigkyBn27rwyBQuy0CT36f0OQEtCvQdCf6dgUJHu94y3qEMy8UjCMjXZeMTbE27S4YvnOA5NwWz23y3u-hFhd1utwDYAUcJRCO-VBbaz4mWeLsUPzIoN0FUCUPjYoud7rzaBbdTCADYuy1vtgtpM_-zGLlO2-xbpEQYG_2kvw8OddjZORPPKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
إبراهيم عزيزي:
إن جريمة اليوم التي ارتكبها النظام الصهيوني في الضاحية تثبت مرة أخرى أن أمريكا ضعيفة وغير جديرة بالثقة، وأنها لا تملك حتى القدرة على السيطرة على هذا الكيان الزائف.
الجواب مؤكد، وقد قدمته جبهة المقاومة المتحدة.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/78752" target="_blank">📅 19:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78751">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامب: "اتصلوا بي وقالوا لي - سيدي إسرائيل تهاجم في بيروت - قبل ساعة من موعد توقيع الاتفاق. لم أصدق أن هذا يحدث. هذا سيء جدًا".</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78751" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78750">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامب: أطلب من إيران عدم إطلاق النار تجاه إسرائيل</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78750" target="_blank">📅 19:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78749">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامب: "اتصلوا بي وقالوا لي - سيدي إسرائيل تهاجم في بيروت - قبل ساعة من موعد توقيع الاتفاق. لم أصدق أن هذا يحدث. هذا سيء جدًا".</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78749" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78748">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامب: لماذا قام بيبي بهذا الهجوم؟ حزب الله أطلقوا وأصابوا في وسط اللا مكان. لم يصب أحد. ثم عليه أن يقوم بهذا الهجوم اللعين وأيضًا في بيروت. هذا أغضبني جدًا".</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78748" target="_blank">📅 19:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78747">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
ترامب: تحدثت مع رئيس الوزراء الإسرائيلي نتنياهو، قلت له "ماذا تفعل بحق الجحيم".</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78747" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78746">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الإطار التنسيقي:
بيان صحفي
بسم الله الرحمن الرحيم
في الذكرى المباركة لفتوى الجهاد الكفائي، نستحضر بكل فخر واعتزاز الموقف التاريخي للشعب العراقي الذي شكّل نقطة تحول مفصلية في تاريخ العراق المعاصر، حين هبّ أبناء الوطن لتلبية نداء المرجعية الدينية العليا دفاعاً عن العراق وشعبه ومقدساته، ولحماية المنطقة والعالم من خطر الإرهاب والتطرف الذي لم يكن يستهدف العراق وحده، بل كان يهدد الأمن والاستقرار الإقليمي والدولي بأسره.
وإذ نستذكر هذه المناسبة الوطنية العظيمة، فإننا نؤكد أن الوفاء لتضحيات الشهداء يقتضي مواصلة العمل على بناء الدولة العراقية القوية ومؤسساتها الدستورية الراسخة، وترسيخ سيادة القانون، وتعزيز الأمن والاستقرار، وحصر السلاح بيد الدولة باعتباره الركيزة الأساسية لحماية الوطن وصيانة منجزاته وضمان مستقبل أبنائه.
كما نؤكد اعتزازنا بالدور الوطني الذي اداه الحشد الشعبي باعتباره مؤسسة أمنية رسمية تعمل ضمن منظومة الدولة العراقية وقوانينها النافذة، في الدفاع عن العراق ومواجهة التحديات التي تهدد أمنه واستقراره.
وفي الذكرى الثانية عشر لتأسيس الحشد الشعبي نؤكد على دعمه  وتقويته وتنظيمه وصون حقوق شهدائه وجرحاه ومجاهديه ويبقى الحشد مورد الفخر ومرتكز أساس من مرتكزات الامن القومي العراقي مع باقي صنوف قواتنا المسلحة البطلة .
الإطار التنسيقي
الدائرة الاعلامية
١٤/٠٦/٢٠٢٦</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78746" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78745">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
ترامب:
تحدثت مع رئيس الوزراء الإسرائيلي نتنياهو، قلت له "ماذا تفعل بحق الجحيم".</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/78745" target="_blank">📅 19:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78744">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59874abc6.mp4?token=m2Iyqw13lKovRsifhT4XlrAgoGQsLBVY_0uY7nmBog0dEha417gMwKdg_HQ3SIuRqjJWxvnBVov6A_qDDTlGpBvy4r8PDyL86weifjGJQgdSREwjQ-qhijfZta03N_EGQN4G1uN5x7-M0R-K9UTASek4t0BBLpzgPGEA9_uOf2x62olsGoK6KE6euQkG5DbthMF_7zN1ksB-OZjwJhUdCcbc57v7LODHYZe14Qr3_oFPa_yQxSVou2unRc9AxQAUb4dKZShVqg-v-kCSEn06fIOcaJI9TnjPhXB14PI2rkBVJqy0H3d8wo9VVNDyl6aZAF2-yPZ9BdXTO2hwBjou8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59874abc6.mp4?token=m2Iyqw13lKovRsifhT4XlrAgoGQsLBVY_0uY7nmBog0dEha417gMwKdg_HQ3SIuRqjJWxvnBVov6A_qDDTlGpBvy4r8PDyL86weifjGJQgdSREwjQ-qhijfZta03N_EGQN4G1uN5x7-M0R-K9UTASek4t0BBLpzgPGEA9_uOf2x62olsGoK6KE6euQkG5DbthMF_7zN1ksB-OZjwJhUdCcbc57v7LODHYZe14Qr3_oFPa_yQxSVou2unRc9AxQAUb4dKZShVqg-v-kCSEn06fIOcaJI9TnjPhXB14PI2rkBVJqy0H3d8wo9VVNDyl6aZAF2-yPZ9BdXTO2hwBjou8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إطلاق رشقة صاروخية من حزب الله تدك كريات شمونة ومحيطها في الشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/78744" target="_blank">📅 19:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78743">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
التفاوض لا يعني التنازل عن المبادئ، ولن تخضع الجمهورية الإسلامية الإيرانية لأي نوع من الترهيب أو الضغط غير القانوني. المفاوضات ليست سوى إحدى الوسائل لضمان المصالح الوطنية. وتسعى الحكومة في الوقت نفسه إلى اتباع مسارات متعددة لتعزيز الاقتصاد وتحسين مكانة البلاد.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78743" target="_blank">📅 19:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78742">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: الارتباك في الولايات المتحدة:  ترامب ينتقد إسرائيل التي هاجمت الضاحية  وزير حربه يثني على الرد باعتباره متزناً  وزارة الخارجية تضغط على إيران لعدم الرد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78742" target="_blank">📅 19:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78741">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
الارتباك في الولايات المتحدة:
ترامب ينتقد إسرائيل التي هاجمت الضاحية
وزير حربه يثني على الرد باعتباره متزناً
وزارة الخارجية تضغط على إيران لعدم الرد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78741" target="_blank">📅 19:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78740">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇶
مدير شركة سومو النفطية:
لم تستهدف أي ناقلة تحمل النفط العراقي خلال أيام التصعيد الأمريكي الإيراني.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/78740" target="_blank">📅 19:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78739">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ae956065.mp4?token=OboCjgWDLJy6Q3ngA7L8pFIGffm6TwwCax84lDSBVAIUv7HDio4bERGRL6rMQaMpJp1nNRpoXsSffjd6d0zUds-ARGkHpqWW0Av-2KFM-JWfiBo398hTAwhHQgpEegiLc3weynDYK4SCIhYg7Ah27k37r2_Egmzj02_x6cfwnIGT_s3kBJ-cnM3oJFgzuNl0cSPcTcjceBcmgdfKw7Q66fJ_QQlftg18NsVKVEcs2WUcaSN03vbRq21tu0AhUgEhucd0t2rMbbM92_IijfYzunmlkTNdIGkwlx7TDUn9HPy_d83uh3OYhN3RaiY9rMpP1dzwyoqbF631_dD8O2TF5lhnvBAmxVtQLIwPzL_j93Ecywngt85009dxPh5UBxNtd87WhoNpDpclitJV0ouaMaqu3lQtTAraRSgScOGCzsU6NCg5K4iG0D4rJV2g_NXSrNXscCKghXsvgRK9aAu4c6cfaAV56mHU8jH_hy6NCYkclmwLGLsF6nsV0lObvIXzwZ7cPVH8Ra_NApVe3gLy9bPZSyyfYtJBVqtYFs1TcBb2bbjotLKhLqLiPU3WZoRIYqCcX7fIjdV-hfhoUs1G1lbFqY2zJ8fDRspDoTruhF8YwVcr-Jk_o4htky2urRkECr2lsXbMIb1Hi7NxXUMWjnSDeLc32AxUbJPkf9YM-po" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ae956065.mp4?token=OboCjgWDLJy6Q3ngA7L8pFIGffm6TwwCax84lDSBVAIUv7HDio4bERGRL6rMQaMpJp1nNRpoXsSffjd6d0zUds-ARGkHpqWW0Av-2KFM-JWfiBo398hTAwhHQgpEegiLc3weynDYK4SCIhYg7Ah27k37r2_Egmzj02_x6cfwnIGT_s3kBJ-cnM3oJFgzuNl0cSPcTcjceBcmgdfKw7Q66fJ_QQlftg18NsVKVEcs2WUcaSN03vbRq21tu0AhUgEhucd0t2rMbbM92_IijfYzunmlkTNdIGkwlx7TDUn9HPy_d83uh3OYhN3RaiY9rMpP1dzwyoqbF631_dD8O2TF5lhnvBAmxVtQLIwPzL_j93Ecywngt85009dxPh5UBxNtd87WhoNpDpclitJV0ouaMaqu3lQtTAraRSgScOGCzsU6NCg5K4iG0D4rJV2g_NXSrNXscCKghXsvgRK9aAu4c6cfaAV56mHU8jH_hy6NCYkclmwLGLsF6nsV0lObvIXzwZ7cPVH8Ra_NApVe3gLy9bPZSyyfYtJBVqtYFs1TcBb2bbjotLKhLqLiPU3WZoRIYqCcX7fIjdV-hfhoUs1G1lbFqY2zJ8fDRspDoTruhF8YwVcr-Jk_o4htky2urRkECr2lsXbMIb1Hi7NxXUMWjnSDeLc32AxUbJPkf9YM-po" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
من يصرّ على العدوان والعبث بالأمن، فلن يجد إلا ردًّا يردعه. وإن لم ينسحب واستمرّ في غيّه، فسنمضي في تأديبه حتى يصبح خائفًا يترقّب، ويحسب لكل خطوة ألف حساب.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78739" target="_blank">📅 19:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78738">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta8gCMiq1Za-0ixtcaXe3Fil_SnKpWRldaqPN-QcZ2SyNeqn_1t_U4nMXXzDoZSbkXn4oBp7E4q_btFVSTlguRXJyCy0oaDoenOGV_pehjhmXmH9pRKINOGeG08B7_OIaInOyXQJBDVIMedUV0Jo0aoiSSTQyyn39DjrYoA-v-2Q0Mti2JLzTo-lCeuQ3NA44FHGPWv7jotGIG5mk_97AggDumJXqOD0L9Mfq_ibERaWVolTbK8Nj9IiRFGhlBn7DhXWPPxt8oISkktYAPH0tuyowG3NgkBol1z6HFP3DdRK4r7B4V14fx3pOCTak3sp0OsP8fpfhRsDqy3-ESvv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد قوة الجوفضائية في الحرس الثوري السيد مجيد الموسوي:
بسم الله الرحمن الرحيم
يا أيها الشعب الحكيم الغيور، الذي أُرسلتم لطلب دماء الإمام الشهيد، وعقدتم عهداً جديداً مع الإمام الحاضر في سبيل تحقيق المثل العليا للثورة الإسلامية، واستعادة كرامة إيران الحبيبة، تذكروا أن الطاعة ركنٌ من أركان الالتزام. فلا تتقدموا خطوةً ولا تتراجعوا خطوةً، كونوا مع وليّكم. وكما قال الإمام الخميني الجليل، رحمه الله: كونوا نصرةً لولاية الفقيه، فلا يمس وطنكم مكروه. استمعوا لأمر الولاية، وتجنبوا كل كلمةٍ تُهدد وحدتكم المقدسة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78738" target="_blank">📅 19:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78737">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
‏مسؤول أميركي: استهداف إسرائيل في الضاحية محاولة واضحة لتخريب الاتفاق.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78737" target="_blank">📅 18:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78736">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: بمساعدة قطر وباكستان ،يحاول الأمريكيون في هذه اللحظة منع إطلاق النار من إيران إلى أراضي البلاد.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78736" target="_blank">📅 18:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78735">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: بلديات إيلات وتل ابيب الكبرى ونتانيا وحيفا تفتح الملاجئ العامة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78735" target="_blank">📅 18:54 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
