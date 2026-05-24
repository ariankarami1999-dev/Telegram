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
<img src="https://cdn4.telesco.pe/file/od7rhwn4pb3imgYzHwz97_ZwLjesEqXRjYM_6Hd4r0w6g6MN92a9UqZWtkGZwamyyylAOA2VGTZriR-sliCZ7lJN8ITVi3m25pbUb9Xmbl200Mzohxyzp6Vz9d3uj-c5rIchLklorfQS-8Th9v6_NELuRAUX_If0MLczspCI2hwKg6pBCxih3hW4XyUkCbptPl1Vop3H35GRHRVDLpk0MSB4FTOWAgIe9bXLmq9Rcg8Nvw-JUfFu77ZcI4Ue9jvv8CVlA2of6XyNDc9EKtkTlpCn6oxEEGsrJ-uzhLFhWxSP2nDOX2uywl0vAD_TYy0yv8DUw0XuRAU6gzeE0J0PTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 15:16:57</div>
<hr>

<div class="tg-post" id="msg-75991">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff86c83697.mp4?token=TyxD8b1UkRxToMl1DKuVAZZc31MNYja0-k9OGdINjKO1WkG-U7-gCXz5Nx8gJfyRg12IW-lTpxiVFRrii7DVIdjs4ZtazCHNPR3y0no41LsxI9Enxelpk69rKDxPKbtfHCsRjsDqz9e3PWZrq8ixGpdYyZowIrbsEoODyttGXJF91XBC4y5Z1qc_qPQA0gma8jBJX7WDZkKVLJu28TvkXr5K-xPf4CqEHG2hskoC3aBGdkm8mCTg3ZqjTbAtGIMaZGaFb6ZFDAy2Jp36npkl7xmT097Y46KADJYJgjgZKx6Ij0zunjPQEMjgFyS7pslwqIQhYwnl9QgM0jL1-DJIhz_O7T6sA9o0JhzRdHI5OdS4HmNe4yfikuDupvnLua5E22Fg4_ZKOWqIB6Mqnw8g43NYYhWiQzJhYhAsVP0DkH2JqXJga2escIf-jkx9RJO-i-zjRRMkkO28Kn8bDPUox_SaOuJv-aO0LaRe_6yDik2fQm7SY-CLdWu0eDIInHRJkUjWdKpZljfMrYuZOholAa8ONR2yT8_E175AX4uJwZEoGnbKO9MncPe6hoamnKXbt-MnFxy8fNcLfkQoUpYMUARXjAJgNrm9fGgPcIK-x7aHscn-nIyaGcQSWpuv60lsS1O1RQ2Mdu2_bUoRPM0cnRV2TeKr-4J9EISSa9H1TOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff86c83697.mp4?token=TyxD8b1UkRxToMl1DKuVAZZc31MNYja0-k9OGdINjKO1WkG-U7-gCXz5Nx8gJfyRg12IW-lTpxiVFRrii7DVIdjs4ZtazCHNPR3y0no41LsxI9Enxelpk69rKDxPKbtfHCsRjsDqz9e3PWZrq8ixGpdYyZowIrbsEoODyttGXJF91XBC4y5Z1qc_qPQA0gma8jBJX7WDZkKVLJu28TvkXr5K-xPf4CqEHG2hskoC3aBGdkm8mCTg3ZqjTbAtGIMaZGaFb6ZFDAy2Jp36npkl7xmT097Y46KADJYJgjgZKx6Ij0zunjPQEMjgFyS7pslwqIQhYwnl9QgM0jL1-DJIhz_O7T6sA9o0JhzRdHI5OdS4HmNe4yfikuDupvnLua5E22Fg4_ZKOWqIB6Mqnw8g43NYYhWiQzJhYhAsVP0DkH2JqXJga2escIf-jkx9RJO-i-zjRRMkkO28Kn8bDPUox_SaOuJv-aO0LaRe_6yDik2fQm7SY-CLdWu0eDIInHRJkUjWdKpZljfMrYuZOholAa8ONR2yT8_E175AX4uJwZEoGnbKO9MncPe6hoamnKXbt-MnFxy8fNcLfkQoUpYMUARXjAJgNrm9fGgPcIK-x7aHscn-nIyaGcQSWpuv60lsS1O1RQ2Mdu2_bUoRPM0cnRV2TeKr-4J9EISSa9H1TOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026 آلية اتصالات تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/naya_foriraq/75991" target="_blank">📅 14:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75988">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrCIu7ms_8qawOYneBvzTbI8Uhry19-6gto4vGrnuf_2E4cs5KKrqIo90XmBsm5f-4I9jZiLTuVT8yzelSsmbWp-7-nl46xiKnWwxNe6uZvsBtiXcSFF0EJt31nViHuph5C9QkNAWXWUYPAAsLDN2nWjwUO0lotxb1vahj5j8dPt4K1wcZ8tz6L2Su5E2lsyQ4sfEKWF8VZmonEgqJWQs2Cf10dqdvVCjlSBDN_zzpqxVG3RKIAacyEUKSUnPHnfSvKZgAlgEMMDYQ62aB4IjYMky9T21GySg-EK3LJmyaBDUyoZzifUwk410uda_aimx1mxhTIEBZNEwouspMtXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETk_7x1mY_MXscqADRSxgKc8MoSFY5twshkJ_K0gmQkPxXkwVwNW13sb6TBQv_vgVTGVJRzF0f5mItAgpficb7xuu8EVQFBNDTZwM0qfZyhLHawj0QSkj9WP-r152tJUAcqXYNwsMRzB4gwjVD7rUNC6fdaaKHL3hJF59wgclY7sgM5AtqMM_KdmmOqRhUhnL4MrotF5LEtxn_kwoRdrqILiGRN8H75HKiK0uEHizVXt_7f4RWGLm3Jq9EUYT0aZiqbwWgsAC7lN6TIc_iSlwu4x-8eHoNau2NXBvkNgERH3qMIv28VTxJwf0ciwtQoK8xQlmU6Wd5KK7EVrqQlZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVs0RYmIJwRXao0Y9LhkbW_ahO5VRGE0-VNW5jc9yjhj-B-iSasJB5sZhQWnqar8VlAn5Lk3QfMDeGafGHUd8bbjju1SUUYUtxxWk3l42DwMCU19t-MHZrKfchWdDIn6lP_HO8z38Wx4O0PXgeKWlO-8s0yEt6k38P3G0ZwO3MyzMP0HTZHWHRoVvVdqUifrqTk2Q6UIVDymVsSSJblHeTzmXnUCaNWgGksYBS9NZOrRZ1OIqIsrFKunYPapED7RHaBGbuNhdIUl2LJXSFhjPjpPcyNajVjnG_-IPr43EZv2otP31n73Xp7lVz6su6hP3hsl1FCZ_bgAQagHfGMsDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
ابطال الحشد الشعبي يسعفون اخوتهم في جهاز مكافحة الارهاب بعد ان انفجرت عبوة ناسفة عليهم.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/naya_foriraq/75988" target="_blank">📅 14:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75987">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎤
فوكس نيوز:
الاتفاق المتوقع ينص على بقاء القوات الأمريكية بالقرب من إيران لمدة 30 يومًا.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/naya_foriraq/75987" target="_blank">📅 14:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75986">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
حكومة البحرين الجائرة تصدر الحكم المؤبد لتسع افراد مدعية تخابرهم مع الحرس الثوري الايراني.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/naya_foriraq/75986" target="_blank">📅 14:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75985">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8621a769e.mp4?token=axe9SE69SiYBBUKuZ6YakPzYWNnh8rgMT1KorSd_SGEP3TNQ5VIWShDwPWWyRNskzVpvH-ZTIiWdjJ_am-ROq4T0NQ2mZcYafbBk66DD7CG7By53ya0xwWbaoJ6Lw_l9N_s4z6HFn8b_F6H443kEUiPE9dp7xOECKCdKY9t95sQ6w-r143hSsbFLhLrtDKolFwMvtUR4cA-0gooN0TidB5e-4P285kSY_w0Qas_Sj-eZqrtruXP2QvjY-LzGokoR9eaXua_-SfDGHKb75lwakF3c-_P1FU5B_qkJbJMiQlux2EAJCBgRM7DcJ768ViTPQf-2AlrWOZHDB6RMzV6W6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8621a769e.mp4?token=axe9SE69SiYBBUKuZ6YakPzYWNnh8rgMT1KorSd_SGEP3TNQ5VIWShDwPWWyRNskzVpvH-ZTIiWdjJ_am-ROq4T0NQ2mZcYafbBk66DD7CG7By53ya0xwWbaoJ6Lw_l9N_s4z6HFn8b_F6H443kEUiPE9dp7xOECKCdKY9t95sQ6w-r143hSsbFLhLrtDKolFwMvtUR4cA-0gooN0TidB5e-4P285kSY_w0Qas_Sj-eZqrtruXP2QvjY-LzGokoR9eaXua_-SfDGHKb75lwakF3c-_P1FU5B_qkJbJMiQlux2EAJCBgRM7DcJ768ViTPQf-2AlrWOZHDB6RMzV6W6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
أحذية شهداء الجيش اللبناني أمام مبنى مجلس النواب في العاصمة اللبنانية بيروت، احتجاجاً على مشروع قانون العفو العام.</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/naya_foriraq/75985" target="_blank">📅 14:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75984">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🌟
🇮🇶
جهاز مكافحة الارهاب:
يعلن استشهاد 3 مقاتلين وإصابة 4 آخرين بانفجار عبوة من مخلفات داعش في صحراء الحضر جنوب غرب نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/naya_foriraq/75984" target="_blank">📅 13:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75983">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 18-05-2026 آلية نميرا تابعة لجيش العدو الإسرائيلي عند خلة الراج في بلدة دير سريان جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/naya_foriraq/75983" target="_blank">📅 13:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75982">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94daa968c2.mp4?token=TGp11dbD_hpBkpU9xkdsOB0HKNKOR7EbrjfV1Ep7_YmfLnBi-P6vhTI8Y0_xQIWTCZP7hB50c1pHAbAXmOghRDdbd3BjoNRckOtH6N5y28J3ez9FHKG-51YcYG6ROlKr9KvaqopdSFrSj3rlzL00Z5Y7FvvdLJi3c0bQdKLQsjttWPZsEiAq-HcyMcy1r_VixPXTdmlHUgq5mUvEvns_qhS_KSIhKdBhh-HkV7P0H6Y5ZxrXAMdZST-wFvfSkvRji42zVHXPycOpLIWuNLyPfrGQhoLNhjvENQvUqeVX2udxhbyqhEYkdblQtJwBNEkV_ZdNnhedvNiZ278A7mMYMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94daa968c2.mp4?token=TGp11dbD_hpBkpU9xkdsOB0HKNKOR7EbrjfV1Ep7_YmfLnBi-P6vhTI8Y0_xQIWTCZP7hB50c1pHAbAXmOghRDdbd3BjoNRckOtH6N5y28J3ez9FHKG-51YcYG6ROlKr9KvaqopdSFrSj3rlzL00Z5Y7FvvdLJi3c0bQdKLQsjttWPZsEiAq-HcyMcy1r_VixPXTdmlHUgq5mUvEvns_qhS_KSIhKdBhh-HkV7P0H6Y5ZxrXAMdZST-wFvfSkvRji42zVHXPycOpLIWuNLyPfrGQhoLNhjvENQvUqeVX2udxhbyqhEYkdblQtJwBNEkV_ZdNnhedvNiZ278A7mMYMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 20-05-2026 آلية نميرا تابعة لجيش العدو الإسرائيلي في بلدة حداثا جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/naya_foriraq/75982" target="_blank">📅 12:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75981">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🌟
إعلام خليجي عن ‏مصادر رفيعة: الاتفاق المبدئي المحتمل بين إيران وأميركا سيحمل اسم إعلان إسلام آباد</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/75981" target="_blank">📅 11:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75980">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
انفجار لغم أرضي في منطقة الطيب بمحافظة ميسان جنوب العراق ؛ مقتل شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/75980" target="_blank">📅 11:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75979">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📰
رويترز عن مصدر إيراني: طهران لم توافق على تسليم مخزونها من اليورانيوم عالي التخصيب</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/75979" target="_blank">📅 11:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75978">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">📰
إعلام إيراني: في حال الاتفاق على المذكرة سيتم إعلان انتهاء الحرب بين الولايات المتحدة وحلفائها ضد إيران وحلفائها على جميع الجبهات</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75978" target="_blank">📅 10:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75977">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇶
أنباء عن سماع دوي انفجار في محافظة السماوة جنوب العراق دون معرفة التفاصيل.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75977" target="_blank">📅 10:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75976">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔹
في هذه الأثناء تزور صواريخ كنجال الفرط صوتية الروسية مدينة كييف   الهجوم الروسي يندرج ضمن رد موسكو على الهجوم على بناية سكنية للطلاب في جمهورية لوغانسك التابعة لروسيا.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75976" target="_blank">📅 10:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75975">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc1dc9836.mp4?token=IeCstnH0GABNJgbejwp4rOVbe41KUNC_4kHmo_qGM19CcE2bNBNktbImSffOjX-sWyTAICw3S66Gd2TJpOqNqwMwXQsRjyCSwRTrL93Fkh3wB39DYSXXrEv6Opk8tkjGTsmgNMOCT9FwjcSQe6F_xOLh-03ubPSO4qk5zDdoGWbEkVv1XuRvvJGRue7Qw1kkgx5JFktBiXRZqCrxkEg1GDd-MYCimVDgH3UL1Rrr0J2s0AXIXmplFYItxW7KOmtmVDoUb9W1FPiYWvF9e46UKXIDz6icnaJNI-62PRhuQPjGsjIegEhvngEEAosJyCF4Wz6gofpSt29H8-51f78tBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc1dc9836.mp4?token=IeCstnH0GABNJgbejwp4rOVbe41KUNC_4kHmo_qGM19CcE2bNBNktbImSffOjX-sWyTAICw3S66Gd2TJpOqNqwMwXQsRjyCSwRTrL93Fkh3wB39DYSXXrEv6Opk8tkjGTsmgNMOCT9FwjcSQe6F_xOLh-03ubPSO4qk5zDdoGWbEkVv1XuRvvJGRue7Qw1kkgx5JFktBiXRZqCrxkEg1GDd-MYCimVDgH3UL1Rrr0J2s0AXIXmplFYItxW7KOmtmVDoUb9W1FPiYWvF9e46UKXIDz6icnaJNI-62PRhuQPjGsjIegEhvngEEAosJyCF4Wz6gofpSt29H8-51f78tBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
في هذه الأثناء تزور صواريخ كنجال الفرط صوتية الروسية مدينة كييف   الهجوم الروسي يندرج ضمن رد موسكو على الهجوم على بناية سكنية للطلاب في جمهورية لوغانسك التابعة لروسيا.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75975" target="_blank">📅 09:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75974">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏴‍☠️
إعلام العدو عن مصدر إسرائيلي: الاتفاق المحتمل مع إيران سيء</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75974" target="_blank">📅 09:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75973">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bdaad755f.mp4?token=aKWDi9Kg_Qsor5PZ3dLO7-PxU50nJBz_nh-T_JKkpsNS0VOsAJUvdoku7kONNUIOlDA7wlZongZWafB7Jz8MpkYbAXH0QzJfB8ssxLrvnVjQQy9Xuld9XxfmN4du8a4TwooNVNz5SUK2j53tClDUpBTFzACWjximz6zbkPXluWpIcASKf172Qv6CJo-jB4npuZkbHvvCKGWISJLYOReQt3GrgE7FjL6w_-yFO-PS8eaY1TQlw7sHIiSGhP8gkLy5Kd-GeN6l97Y8JZsGigLHf_rSiZmtBS1S5m4yjTMuWn2BOvC4DLM3iRWII2ckZSWhec2M0ZhGCqXomHSxszdjXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bdaad755f.mp4?token=aKWDi9Kg_Qsor5PZ3dLO7-PxU50nJBz_nh-T_JKkpsNS0VOsAJUvdoku7kONNUIOlDA7wlZongZWafB7Jz8MpkYbAXH0QzJfB8ssxLrvnVjQQy9Xuld9XxfmN4du8a4TwooNVNz5SUK2j53tClDUpBTFzACWjximz6zbkPXluWpIcASKf172Qv6CJo-jB4npuZkbHvvCKGWISJLYOReQt3GrgE7FjL6w_-yFO-PS8eaY1TQlw7sHIiSGhP8gkLy5Kd-GeN6l97Y8JZsGigLHf_rSiZmtBS1S5m4yjTMuWn2BOvC4DLM3iRWII2ckZSWhec2M0ZhGCqXomHSxszdjXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇰
مقتل ما لا يقل عن 20 جنديًا باكستانيًا بعد أن استهدف قطارًا يحمل أفرادًا من الجيش الباكستاني وقوات حرس الحدود في كويتا، جمهورية بلوشستان الباكستانية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75973" target="_blank">📅 08:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75972">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏴‍☠️
إعلام العدو :
تتضمن مسودة مذكرة التفاهم بين الولايات المتحدة وإيران إنهاء القتال بين "إسرائيل" وحزب الله في لبنان. ووفقًا لمسؤول أمريكي رفيع، أعرب نتنياهو عن قلقه خلال محادثة مع ترامب، لكنه تقبّل موقف الإدارة الأمريكية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75972" target="_blank">📅 08:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75971">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IG7wYmrMFak378IYKXFrHdD8thaONaHP9M_zjT1teUj5khXyd6tCE7EX56CXr6smJ-40fPjjhAlT91OqNx20rHsb1liNQUBo-WehMisWxNLGPguxKTvF7XpbEWuvnTt3hFJ6cerbOmXIXEw58N6jR4rC-Q43I6jTzVHCtAH_1xcZT6lHRI4tOISsJZW1Tv0TY50fZgSR4gTIA6L1O-W4UPplrkuqOOSb8eB9yE4g2s9s5U1bzBudeC4N3dhIz3YIK06BhBMnhslXOepbhpDrjkw8BlIwQIMAFhbwSHHwBFh14379ytlalD3u2wOfFh2s4BTUSkjpt4W5EiGerdYPtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يشكر الخدمة السرية بعد إطلاق نار واشتباكات قرب البيت الأبيض</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75971" target="_blank">📅 08:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75970">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇺🇸
🇷🇺
على غرار التحذير من العراق   السفارة الأمريكية في أوكرانيا تنشر معلوماتٍ بشأن هجوم جوي محتمل كبير وتوصي السفارة، كعادتها، المواطنين الأمريكيين بالاستعداد للاحتماء فورًا في حال صدور إنذار جوي.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/75970" target="_blank">📅 01:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75969">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bq_KEqdPEqj2i0bYHrgaE8_1AKmdTc579b-nPOQZzyw3cisuVJkwK7rg9P1QaTn6R1P1YHz2li_WsjLeVkGgj_-x0r0Yz-0QWocjyej2eZCMY1_ov15kxiq4ZKaFJ9xzFmjhLUNkAmyKKy9-Ea6Y_pWmGYjFxr-8U7CZ_ozasuUFyGjPYxFba-yI1aCKCafqzRzAfZqRlSTm8h-v5bLI1OjuQW-5IiwoaMOvPXZOjNheQA7qlpDmmRQC_zn2dHYIEqO0xAXpmlN6nsjZ-AcSC5bsnRA--n8l3RjDbss3GH4EtRGLNv4y4dmIkrG90I6J-qpDOqPZ_AKlWan4uThgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام العدو : ترامب يعلن الاستسلام أمام ايران .</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/75969" target="_blank">📅 00:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75968">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
🇷🇺
على غرار التحذير من العراق
السفارة الأمريكية في أوكرانيا تنشر معلوماتٍ بشأن هجوم جوي محتمل كبير وتوصي السفارة، كعادتها، المواطنين الأمريكيين بالاستعداد للاحتماء فورًا في حال صدور إنذار جوي.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/75968" target="_blank">📅 00:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75967">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b8d79693.mp4?token=gPfLamc29uWbNhI9GeXkHp6ie_xoVti6XLCrvRKDgujWJ2-PMn3RbnXp1l-Oa8fVcbIQ7-SG_xKFmXW7uICH9_O3_c_xPdmBHqu2yFKDmmsM5H1IH4aYZZmVR_VL28IkYGcnkVJR48HJyGme4fjpe-CZ3Sdd4UdxsNvXQa6LufwSF9i8rCMYsfZQVIUonqY5aErbEAdAN4fnZaNbMWCkExdZpGSODg3Dggf9D-LZ7933aj8d_3bq42hK3lUVIEeJsPaewOkzQGDcCk3OQWXO9kJYOVRgZV9xOoQV-qdIrrdl_9GPWCGhIUqik_eLFFx3kSCO80FA4sBs_eA44r1IxKLbj1yini6CL1i6_MtkbCOegWgc9Gu8iiPYHjQ9J1s9VXWxLh_FXp5qeFiNHR3ycIAFbF-QBAFB3QBVUb5R6lpa9t42AnWSgb_rAegyqHW6b7exkWzs9CHmcsBXTga4ZJc4eAlnQ1YgmPGUR8LGb9plIGdP1XYORULKoqVpKzY4Tl2yNE9RvFgXqKaa1spwx_OKeVuDgrPqKJl2VYrBHNGhgL4qloqVu3lukzv1Wg38wpaZnb3gJv3ERZIC9YkOIgtfu-ptcQWDstp4efSbN2EGnBn4_HIFh-SaCFk9SnHj3NV-82d88yRhAXcrSb35wBNc6ltfxw-LFx8Y_-c90ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b8d79693.mp4?token=gPfLamc29uWbNhI9GeXkHp6ie_xoVti6XLCrvRKDgujWJ2-PMn3RbnXp1l-Oa8fVcbIQ7-SG_xKFmXW7uICH9_O3_c_xPdmBHqu2yFKDmmsM5H1IH4aYZZmVR_VL28IkYGcnkVJR48HJyGme4fjpe-CZ3Sdd4UdxsNvXQa6LufwSF9i8rCMYsfZQVIUonqY5aErbEAdAN4fnZaNbMWCkExdZpGSODg3Dggf9D-LZ7933aj8d_3bq42hK3lUVIEeJsPaewOkzQGDcCk3OQWXO9kJYOVRgZV9xOoQV-qdIrrdl_9GPWCGhIUqik_eLFFx3kSCO80FA4sBs_eA44r1IxKLbj1yini6CL1i6_MtkbCOegWgc9Gu8iiPYHjQ9J1s9VXWxLh_FXp5qeFiNHR3ycIAFbF-QBAFB3QBVUb5R6lpa9t42AnWSgb_rAegyqHW6b7exkWzs9CHmcsBXTga4ZJc4eAlnQ1YgmPGUR8LGb9plIGdP1XYORULKoqVpKzY4Tl2yNE9RvFgXqKaa1spwx_OKeVuDgrPqKJl2VYrBHNGhgL4qloqVu3lukzv1Wg38wpaZnb3gJv3ERZIC9YkOIgtfu-ptcQWDstp4efSbN2EGnBn4_HIFh-SaCFk9SnHj3NV-82d88yRhAXcrSb35wBNc6ltfxw-LFx8Y_-c90ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">على الرغم من تنفيذ حكومة البحرين حملة اعتقالات كبيرة للشيعة ومنعهم من مواكب العزاء.. شيعة البحرين يكسرون القرار الجائر في ليلة استشهاد الإمام محمد الباقر (عليه السّلام).</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/75967" target="_blank">📅 00:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75966">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامب:  «أنا في المكتب البيضاوي في البيت الأبيض حيث أجرينا للتو اتصالًا جيدًا جدًا مع الرئيس محمد بن سلمان آل سعود، رئيس المملكة العربية السعودية، ومحمد بن زايد آل نهيان، رئيس دولة الإمارات العربية المتحدة، والأمير تميم بن حمد بن خليفة آل ثاني، ورئيس الوزراء…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/75966" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75965">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsznsu3DNi9FL2OLTe6McPGHTxpVLlWr8tC0QRHX8CAk7FhosZ0AT2NI2Lg7R9OEBn8a-ET_fZ6-_MGe-lOi2uhVTZ3e--ghjmRxcXEcoJMQbFooMKjUtLJ1SN1P3gtQbLtHLncSahW0xDB4OcjBAZr8H7xUd5T9muwuBN6I9DhqJWrVYLlfWTgVmUCUoDLnyl7n-JaWH1YwUUhjg0WmZ-egdrNY3wZleCk5UCKrwWRTMJzxY2Jo20Xsjvrcz0LVOIVGIsHFlG-QswvmvCGUQqC8tPuaTq4fTua7aq0OtH_AFNHEGvFl_Kn5z888szrf6NZUr3k9JOuE3aMoR7jjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إسماعيل بقائي: ‏
في
الفكر الروماني، كانت روما مركز العالم بلا منازع. إلا أن الإيرانيين حطموا هذا الوهم؛ فعندما زحف ماركوس يوليوس فيليبوس (فيليب العربي) شرقًا ضد بلاد فارس، لم تسفر الحملة عن انتصار روماني، بل انتهت بسلام قائم على شروط ساسانية: كان على الإمبراطور أن يرضخ!
﻿</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/75965" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75964">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات تهز الجانب الشمالي من العاصمة بغداد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75964" target="_blank">📅 00:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75963">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2SzCVICWswoh4Fjvc2S5oMu8RfwwFmzofnC9209C5sMn9mE1-dSriLn3oDwuAizo8zzP_xSz43YIxEwpD4stgptR39dC5R_LlXv8HcZbkDkKOKCS-Y9PtFIgT5IBWD9gXKGhxB5MzSLhjPtqJsNlMd8Vq_2mdrkh8xqmDL2N1TrA0G8H5PPM1jECLjDt6DEHKfKyK7PdbSJzSwi3qg-5CRdQQgOfpwufmgvodchxNDDzJYpLiu2KhNWpuaKZ7fajkrWnmkzOXYk5ym6smtWCb974LDQIQhy6aKkISOkdGFxmxKrYBXJD2eDJN0ZMgO6ZOQvXeXsykTtAf9YaJn5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب
:
«أنا في المكتب البيضاوي في البيت الأبيض حيث أجرينا للتو اتصالًا جيدًا جدًا مع الرئيس محمد بن سلمان آل سعود، رئيس المملكة العربية السعودية، ومحمد بن زايد آل نهيان، رئيس دولة الإمارات العربية المتحدة، والأمير تميم بن حمد بن خليفة آل ثاني، ورئيس الوزراء محمد بن عبد الرحمن بن جاسم بن جبر آل ثاني، والوزير علي الثوادي من قطر، والمشير سيد عاصم منير أحمد شاه من باكستان، والرئيس رجب طيب أردوغان من تركيا، والرئيس عبد الفتاح السيسي من مصر، والملك عبد الله الثاني من الأردن، والملك حمد بن عيسى آل خليفة من البحرين، وذلك بشأن الجمهورية الإسلامية الإيرانية وكل ما يتعلق بمذكرة تفاهم تتعلق بالسلام.
تم التفاوض إلى حد كبير على اتفاق، وهو بانتظار الصياغة النهائية بين الولايات المتحدة الأمريكية والجمهورية الإسلامية الإيرانية والدول المختلفة المذكورة أعلاه.
وبشكل منفصل، أجريت اتصالًا مع رئيس الوزراء بيبي نتنياهو من إسرائيل، والذي سار أيضًا بشكل جيد جدًا.
تجري حاليًا مناقشة الجوانب والتفاصيل النهائية للاتفاق، وسيتم الإعلان عنها قريبًا.
وبالإضافة إلى العديد من العناصر الأخرى في الاتفاق، سيتم فتح مضيق هرمز</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75963" target="_blank">📅 00:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75962">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEozyhzzis_yx6cd2xq1NrFQCLFCmBO57PRv76pkNbM_FQecyoy20K0KCYDC8XVGRBAvF8P1TjtrrHCsxVE1R-QMzdL_p8qG3qlu-DUYYs1UiSXfYK5no6wLcojDsurmGln9EA2hxYQQ5b3cP5E4H3yQeJu8jB_l0mQ2CFdo-kqJ_b0h79ZDy36OQIgAFlkU7rOVATSAEOAsl9xeTTlIjomACK7NBw69oQWHNZB4Yy3wzL3XVMqq_Nx38NDoHU-PH8d0qVTo5iljDLynHGsRoFVLFZcjr2wu0dSsXQbj49xP6Nk_jbQ4XsMCR5NhObmJXYMyM9jN-8JjRZrmL6W6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة تزود أمريكية تطلب نداء استغاثة في سماء الأردن بعد ان انطلقت من مطار الملك حسين ..</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75962" target="_blank">📅 00:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75961">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجارات تهز الجانب الشمالي من العاصمة بغداد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75961" target="_blank">📅 00:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75960">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجارات تهز الجانب الشمالي من العاصمة بغداد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75960" target="_blank">📅 23:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75959">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات تهز الجانب الشمالي من العاصمة بغداد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75959" target="_blank">📅 23:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75958">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
استهداف مقر حزب الحرية المعارض في قضاء خليفان بمحافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75958" target="_blank">📅 23:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75957">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">على الرغم من تنفيذ حكومة البحرين حملة اعتقالات كبيرة للشيعة ومنعهم من مواكب العزاء.. شيعة البحرين يكسرون القرار الجائر في ليلة استشهاد الإمام محمد الباقر (عليه السّلام).</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75957" target="_blank">📅 23:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75956">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrXV_V8R4eIIccstoevbdQhw0kPBEO857t64mUuHTX98wQ28JG_L4tcsxuIlTIG3GWYgkKIQgac0D27e8nlQyoJ0YJRWj0ilEuf4IQx9ogzvFU5nuTEmwGLFWxqz4qB_YjTl080iIfA5Kbk0RQNJ2TCJIt1nBJtPm7cwAj9WSL1_F1bmZQzvrEkcKak3wngKZ_2Vc2sr-gyJLDvyCiL9QICLmeZGcABaJswUDJcayj5bYScMmxdmLS601ykSYEEqdAzPgZ95gW-zHTntOFgsOhRiUsZbWftw6JQCuHl9GeDFCG7vCdGYbPFRweOuvRH2B4nsH6rXNtekEcOiYpagMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: أليكس ميلر (23 عاماً) جندي اسرائيلي يقتل نفسه بعد إصابته بصدمة نفسية حادة، وسط تصاعد الحديث داخل إسرائيل عن التأثيرات النفسية المتزايدة للحرب والخوف من هجمات المسيّرات التابعة لحزب الله.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75956" target="_blank">📅 23:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75955">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4228c26c11.mp4?token=BSt2j6XXW-XOvDGhcy9wrpdfgcaTgsfblJ8b97R_jgLHCF1bEUj5oHLB_QXmphfGE6OTR4OQEPEIfaAnPzIj8-QV1Hq4T2txWcokvUdiN2PZb1Ba_ngylDvjsU2tiGZjdGP7TzbE8h-cvt7YXVNRjAqLwTOStBYywWfPUYjAd1mip9oitYDYKOOwnf86LIfXlXugMK2lzwcgHttdlBXFm1d-2isb3GZNjksWjxzPNIrV7A-PG4sc6nfz2TbTGzFepIZzPFyk020ylyTwca0hRT1mXsn38UjILzhNPYStMSoBUH6TtyxLJnWgyrYX2cEWz_zytXbjgCXjXzAYoeHsFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4228c26c11.mp4?token=BSt2j6XXW-XOvDGhcy9wrpdfgcaTgsfblJ8b97R_jgLHCF1bEUj5oHLB_QXmphfGE6OTR4OQEPEIfaAnPzIj8-QV1Hq4T2txWcokvUdiN2PZb1Ba_ngylDvjsU2tiGZjdGP7TzbE8h-cvt7YXVNRjAqLwTOStBYywWfPUYjAd1mip9oitYDYKOOwnf86LIfXlXugMK2lzwcgHttdlBXFm1d-2isb3GZNjksWjxzPNIrV7A-PG4sc6nfz2TbTGzFepIZzPFyk020ylyTwca0hRT1mXsn38UjILzhNPYStMSoBUH6TtyxLJnWgyrYX2cEWz_zytXbjgCXjXzAYoeHsFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 16-05-2026 آلية "نميرا" تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75955" target="_blank">📅 23:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75954">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🌟
🏴‍☠️
حدث أمني صعب يتعرض له جنود الاحتلال جنوب لبنان وطيران الإنقاذ يجلون جنود مصابين.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75954" target="_blank">📅 22:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75953">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">📰
‏FOX NEWS: محادثة ترمب مع قادة الدول العربية كانت "إيجابية جدا"</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75953" target="_blank">📅 22:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75952">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70dd906bcd.mp4?token=hPl4fhR7e7Q_oXZlN04MiM5E_dpt1tZnrqtGiMlZJMvnd3ufdtcAep1NE9uV9yKbHWRdtJaR16wAjq8UwvrXWbAVJhoXBlT28QV2ivvlhLDkGfO1GFMbkQHeF0OHeB_QuWTzDjAykn7_vb-KKjQ8zcdMYG8DeTWzmPMnLEZSXcw54Qm2HWWuPVlLkW0IpyUF_J5NVz2BSX2aaETxOVjK2YpDRs_-8ZnXsyvSABni1pw1BbKPuHgCtK3ymkyAMdibdiiht4WNV7Gn89pQfn7aWBpVb6YcHJKtjLqUAQIoF9dmH4To1GKyMcY_OFUvYrHMVDcnLvmwE5vldCr8yH_0lmK-aYRfDIAynwvuLJew_noetbiArxammpCV5_LcNYb-KUITtRwsZ6meMfJHptYRblVG6XAhSa8zGzdDVFOXe4mEFUWJHBJZ4vWQdTxs2DkTynzIGE3vWz4JQs73xoR7qufbO_EFYzBnCaIvFY0ok-seCOcY0qqa77HPy6Aj7AKncJ_wyZW6MTnbKRw9rMDuAS866abgTmAZTWVFeUrNB9Ijead6vqjK7w1JFxlu_pH9FrWsB8pUojY2Yz7eG7HNPh-ego99r3yEJlmnsoPvsjljGvJrM6lNZAoWJxg-QmAJzRAQrlQwjl1zFQDsxJtwaY_EcfP6EQSzec30mycD4QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70dd906bcd.mp4?token=hPl4fhR7e7Q_oXZlN04MiM5E_dpt1tZnrqtGiMlZJMvnd3ufdtcAep1NE9uV9yKbHWRdtJaR16wAjq8UwvrXWbAVJhoXBlT28QV2ivvlhLDkGfO1GFMbkQHeF0OHeB_QuWTzDjAykn7_vb-KKjQ8zcdMYG8DeTWzmPMnLEZSXcw54Qm2HWWuPVlLkW0IpyUF_J5NVz2BSX2aaETxOVjK2YpDRs_-8ZnXsyvSABni1pw1BbKPuHgCtK3ymkyAMdibdiiht4WNV7Gn89pQfn7aWBpVb6YcHJKtjLqUAQIoF9dmH4To1GKyMcY_OFUvYrHMVDcnLvmwE5vldCr8yH_0lmK-aYRfDIAynwvuLJew_noetbiArxammpCV5_LcNYb-KUITtRwsZ6meMfJHptYRblVG6XAhSa8zGzdDVFOXe4mEFUWJHBJZ4vWQdTxs2DkTynzIGE3vWz4JQs73xoR7qufbO_EFYzBnCaIvFY0ok-seCOcY0qqa77HPy6Aj7AKncJ_wyZW6MTnbKRw9rMDuAS866abgTmAZTWVFeUrNB9Ijead6vqjK7w1JFxlu_pH9FrWsB8pUojY2Yz7eG7HNPh-ego99r3yEJlmnsoPvsjljGvJrM6lNZAoWJxg-QmAJzRAQrlQwjl1zFQDsxJtwaY_EcfP6EQSzec30mycD4QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 04-05-2026 آلية لوجستية "هيمت" تابعة لجيش العدو الإسرائيلي في موقع المنارة على الحدود اللبنانية الجنوبية بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75952" target="_blank">📅 22:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75951">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d0057e37b.mp4?token=X2f4wdrbNbMWI115CawVf4tiHgmA2q0W_sjoNVrQ9S9Kz6oLFi3SckPPNRjxl5HMrWHjGcZboUa55MDfMbVhbEZ95prBvg9DIjCQ_Ki3PwGrvyIWs-5vAqmV1eO3VTbTG5cKyZFqAQXv5PRz8KPohw3HKBV7jeb60Ee_FYGICeCRW2g3OD-ZyC6W8gpU5OE9zBt08KV5mjz-fZfCLJQ6i2xygU1L2DbMGef1piIMHAbKKZ4DwS1H8JJZZHVof_znSoAlGGOwpvPuMRuZ6jCiyzRrnYey_ATVqb2NmzJrP3eUCro0cmFp_7MYJf0MOL9EFMe12kSNQHBZ9nlJvE5ezQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d0057e37b.mp4?token=X2f4wdrbNbMWI115CawVf4tiHgmA2q0W_sjoNVrQ9S9Kz6oLFi3SckPPNRjxl5HMrWHjGcZboUa55MDfMbVhbEZ95prBvg9DIjCQ_Ki3PwGrvyIWs-5vAqmV1eO3VTbTG5cKyZFqAQXv5PRz8KPohw3HKBV7jeb60Ee_FYGICeCRW2g3OD-ZyC6W8gpU5OE9zBt08KV5mjz-fZfCLJQ6i2xygU1L2DbMGef1piIMHAbKKZ4DwS1H8JJZZHVof_znSoAlGGOwpvPuMRuZ6jCiyzRrnYey_ATVqb2NmzJrP3eUCro0cmFp_7MYJf0MOL9EFMe12kSNQHBZ9nlJvE5ezQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استهداف مقر حزب الحرية المعارض في قضاء خليفان بمحافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75951" target="_blank">📅 22:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75950">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5151e44404.mp4?token=KSoOZ88eoXGMTaBlXtkPiWVsmT9iDw8LX1_JrPAOwsBRQ41GIgmzwTT7EYnCyePbXHNuhZEbRKP7sjIO007RK_R2Xt3ou-yRbvkro5goWSvKucPQxGadYhIRCKvfmdltl5NZ_lJvrj-BgT8_MwuM9uF0Qj48KF_QebiOkpmErPkl9-Gvl_-qnjcjOaQYyE4yImiWZSPNv0X3FFASC3WUpFeNE5I-JczkDqxuQ_wE64GzurRZAX1JhbZIaLHGSZz3m1gjimwG0H9uDFMjNQJaICovDjWonnbasvkJMdKFTLmz_Uv8-sxuRISvWIEEXP5g0R4DZ03kXp8vR0hGx6fWrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5151e44404.mp4?token=KSoOZ88eoXGMTaBlXtkPiWVsmT9iDw8LX1_JrPAOwsBRQ41GIgmzwTT7EYnCyePbXHNuhZEbRKP7sjIO007RK_R2Xt3ou-yRbvkro5goWSvKucPQxGadYhIRCKvfmdltl5NZ_lJvrj-BgT8_MwuM9uF0Qj48KF_QebiOkpmErPkl9-Gvl_-qnjcjOaQYyE4yImiWZSPNv0X3FFASC3WUpFeNE5I-JczkDqxuQ_wE64GzurRZAX1JhbZIaLHGSZz3m1gjimwG0H9uDFMjNQJaICovDjWonnbasvkJMdKFTLmz_Uv8-sxuRISvWIEEXP5g0R4DZ03kXp8vR0hGx6fWrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استهداف مقر حزب الحرية المعارض في قضاء خليفان بمحافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75950" target="_blank">📅 22:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75949">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f4151d37.mp4?token=u8OsVJ3ETZpWTEgtz2k3HkTCqLvbqxKHgQU48Sxuzi9YXLKmeZfPEDwDry-cNrxqft2bc1wzq053zGnpffOfkK4Jk04SdP8JJmJJbARKgj3u5zYDSkuSq1nh3IeK9gTh9ySGS9Ds-iORJgO-IN5_cv9b5oxdtTYxYLqdky1rHvOgDneQ1VDmVXUV95RhQMYeIY68pCUIDMVHcg2nMGzZVtMeoa513mZN_Frxb8ZXOj0Z8CHuHYjvRxrUmDFhRtpI-brEUOjv9ksejZX2lswbHRUazBPkVhZGa0ptKLB5Ivt3o1p69ZSbTL6JOu8uXd02kqHInPaAmMa5jgyZTLg3ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f4151d37.mp4?token=u8OsVJ3ETZpWTEgtz2k3HkTCqLvbqxKHgQU48Sxuzi9YXLKmeZfPEDwDry-cNrxqft2bc1wzq053zGnpffOfkK4Jk04SdP8JJmJJbARKgj3u5zYDSkuSq1nh3IeK9gTh9ySGS9Ds-iORJgO-IN5_cv9b5oxdtTYxYLqdky1rHvOgDneQ1VDmVXUV95RhQMYeIY68pCUIDMVHcg2nMGzZVtMeoa513mZN_Frxb8ZXOj0Z8CHuHYjvRxrUmDFhRtpI-brEUOjv9ksejZX2lswbHRUazBPkVhZGa0ptKLB5Ivt3o1p69ZSbTL6JOu8uXd02kqHInPaAmMa5jgyZTLg3ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تحليق طيران حربي أمريكي فوق سماء قضاء خليفان بمحافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75949" target="_blank">📅 21:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75948">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">واشنطن تايمز": الولايات المتحدة وإيران ستعلنان عن اتفاق سلام خلال 24 ساعة</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75948" target="_blank">📅 21:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75947">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFCD3LWVVkJ8OuofRhzXLOfKsyfDdFeiCYtpwIWeQqiMjg2NfkqNbnZ2ZojX6e8-_DZmJHfliAvj9N3aG9840e4ozQY-3KV_oZ-qlWVoz3Dd7VJN4pnH2CaAU_s1FdIE_nbGol4xG1ilqn7bS8i4Xdw6iGESS3AGU2Jwp5an97k8P3WMIhsK0Q16JP7e2cJC3faQqxA0ejBAwdUVIY3i0rF2Yo2iQErbpfwzZPDygac0d-Ai4vAdE59IY-dgvF-8l5iAMWM4CDbEi7kXvgPMrTxJxQMIi06OJ2o_0kDQUz-zxU3jmVvKXZyKX8DjXV2jg0c_RbTc0MhoLpUN0YlAqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: نوام هامبورغر، 23 عامًا، من عتليت، مقاتل في تكنولوجيا وصيانة في الكتيبة 9، قُتل جراء انفجار طائرة بدون طيار في قاعدة شمال البلاد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75947" target="_blank">📅 21:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75946">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOkqmc_CTTQq-7ZRE-zeW8vxns-jzlKWeX68qZ0TbH08TgLke8D5xFRjAiD6l3pa1qHQX_-BQ8A7R4zgCOl2mHKSv-tqNRmQF3kBIfG9L81LCBNGd7y902b_lYoCKH7Jrs40EXR7j_KEmxMqb-qfMhoKl8f6qg1-FRz1-thp4undvvRqNHBaODRoyy0hOqLb2wGRbfTFkBu2ozEcKkjXO4Pf_70O2DlAa9gmaxhZOBHTl3Teh2J17KxRjWn-uXYIMPlp3qTf2WzsdZpMPvgb1FQTlgF015C--LEBdh-w_l0jSGCyKUEc3ctEr2sM9r1czo2EkM4NvGEiWFozkMibtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
شكرًا لك أيها الرئيس أردوغان!
«الرئيس ترامب هو الزعيم الذي انتظره العالم لقرون - إنه لا يتحدث عن القوة فحسب، بل يجسدها.»</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75946" target="_blank">📅 20:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75945">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📰
رويترز عن مسؤول أمني باكستاني: يجري وضع اللمسات الأخيرة على مذكرة تفاهم لإنهاء الحرب بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75945" target="_blank">📅 20:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75944">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">📰
‏مسؤولون إسرائيليون لـ أكسيوس: نتنياهو حث ترمب على استئناف الهجمات ضد إيران</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75944" target="_blank">📅 20:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75943">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBQqnFF2P-6QAgZz3vg2ymu5UV_yKFqlDzn9FwNJEjQDiz0zP4J-0VzBs19RZ_Ep6bJrE-6zsUasl69dXOcyaXqVVJnAUHLmK_C0p50-jnNbEYSxDoLYjtYBpjDHKExfkMcTLV5cw10nVLcE_dycpO8lHYF1vhEBZiT6GJh0PT2lT0_rmLozFLdgtXTWWRBgNd21E7ajlPIK7W_gVEW8GmYpiHFB9B7WXuOamJ5KqAiJGNR8IgeJtQ07F4G6AO-sV1e3R1-8BY_2nNASQr_k0GdhIzweDNVbOUNgE7cgONpLqPtZ3GYfvsnKZf_CvK5kvkh_EMdxbRxD4VnJSV89WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات وتصاعد أعمدة الدخان في محافظة السليمانية شمال العراق</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75943" target="_blank">📅 20:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75942">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
وكالة فارس عن مصدر مقرب من فريق إيران المفاوض: 3 نقاط خلافية رئيسية قائمة وإذا لم تحل فلن تجرى المفاوضات
إيران تقول إنها ستحدد السفن المسموح لها بالعبور وفق آليتها</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75942" target="_blank">📅 19:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75941">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fcd1734e4.mp4?token=DmkPQSp357Oc3GQt44hFd3pyZBP48nYIzn9cQBZLG3lYDoTCGMk4MkyuwFKJ61JwubOyILa-xMTTYJwjTaIdTpyPKZgkB3TIVPgSV7liPuLdBAEB3irUYSAGLpjxGy-nCyFeFPrBA2ORrjB5GxjkkcQiUCR5akHCNQQiyDI8qx7YnrAsUtLhHy2jNnNV9TgQ3KGAj3wIGmgPG0DDJWXrM1kZwbuJn5y7Z0oMNbOrLhlAm_Oxwb5XI5fqDFre7aFnfqMVp8SsgU3KGq6G1DXqIjWL6m3P0gCyK42AJGgZ31Sr1rvZKJuWmI0MvIqcg7mIamd4bESfvWehbvu1zDhE7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fcd1734e4.mp4?token=DmkPQSp357Oc3GQt44hFd3pyZBP48nYIzn9cQBZLG3lYDoTCGMk4MkyuwFKJ61JwubOyILa-xMTTYJwjTaIdTpyPKZgkB3TIVPgSV7liPuLdBAEB3irUYSAGLpjxGy-nCyFeFPrBA2ORrjB5GxjkkcQiUCR5akHCNQQiyDI8qx7YnrAsUtLhHy2jNnNV9TgQ3KGAj3wIGmgPG0DDJWXrM1kZwbuJn5y7Z0oMNbOrLhlAm_Oxwb5XI5fqDFre7aFnfqMVp8SsgU3KGq6G1DXqIjWL6m3P0gCyK42AJGgZ31Sr1rvZKJuWmI0MvIqcg7mIamd4bESfvWehbvu1zDhE7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
العمليات المشتركة العراقية: نفذ صقور الجو الأبطال بواسطة طائرات F-16 ضربتين جويتين ناجحتين استهدفتا مضافة بداخلها مفرزة تابعة لعصابات داعش الإرهابية في وادي الشاي ضمن قاطع عمليات كركوك وقتل 4 إرهابيين وتدمير مضافة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75941" target="_blank">📅 19:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75940">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/625c4fea23.mp4?token=Fv2puMn-_lNNs03A5CdUjgWuXH9Y-PIi_xa2AFTLs7SVca-Z4h8S_pd3BFYobx4Alji1XTqRmrYtEZrL0VJJ_Eyhy-Fi2KHClq5X1H3qJCv9dL-rrExaHrPdEBvaAFLRRrPap5F-jSMv_rhnGExIyY7gV1eT4146Th_xqWD3r5IHEv9WDBVDG1xb5qbj_He5zy6o_uZgrE99sngkE89wdiAjTlLVvLj-747YBeRt2PHF-ARo3ItHXx-_AtN5P1Rh7J2JpI7s0a8IR8Fpw7GLun_loPbs7CkoFH_gZMvNKq9KwtRaDVkN0grsX0FMUKnp2lp44LaTiZpGDyufEygRmTa9sM1KV_I4SYbP218FG_e5lacgwC83pCXEvrVhGe1wL5BoEqjertkb3kKXT56by_TADnXYt42jt0EevZviW6yjK1aWsPbuVKKs7yccFk1W89ZnHRjELeZWn_aaML6RCyDbCVogaASc3nVAahPhxgYSMlgcPb1boZe2QOxlJjRwJ95HweyXt38xEVnr6cEk_8LIhaeMZ4kp5CIiYMRJ-p5GHnnZ6JdFedvAUQshNsNWHFA2ERXBq6xZz9R9Egpkzl3LeTsNJoouPr0Gt8Lp_T4zpmmMtChxeCRxGIHlH0TdRtFHO5MSL7WC4E_iFkRyEdevdX2J_9jN-8qAnDXuhgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/625c4fea23.mp4?token=Fv2puMn-_lNNs03A5CdUjgWuXH9Y-PIi_xa2AFTLs7SVca-Z4h8S_pd3BFYobx4Alji1XTqRmrYtEZrL0VJJ_Eyhy-Fi2KHClq5X1H3qJCv9dL-rrExaHrPdEBvaAFLRRrPap5F-jSMv_rhnGExIyY7gV1eT4146Th_xqWD3r5IHEv9WDBVDG1xb5qbj_He5zy6o_uZgrE99sngkE89wdiAjTlLVvLj-747YBeRt2PHF-ARo3ItHXx-_AtN5P1Rh7J2JpI7s0a8IR8Fpw7GLun_loPbs7CkoFH_gZMvNKq9KwtRaDVkN0grsX0FMUKnp2lp44LaTiZpGDyufEygRmTa9sM1KV_I4SYbP218FG_e5lacgwC83pCXEvrVhGe1wL5BoEqjertkb3kKXT56by_TADnXYt42jt0EevZviW6yjK1aWsPbuVKKs7yccFk1W89ZnHRjELeZWn_aaML6RCyDbCVogaASc3nVAahPhxgYSMlgcPb1boZe2QOxlJjRwJ95HweyXt38xEVnr6cEk_8LIhaeMZ4kp5CIiYMRJ-p5GHnnZ6JdFedvAUQshNsNWHFA2ERXBq6xZz9R9Egpkzl3LeTsNJoouPr0Gt8Lp_T4zpmmMtChxeCRxGIHlH0TdRtFHO5MSL7WC4E_iFkRyEdevdX2J_9jN-8qAnDXuhgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 18-05-2026 آلية قائد اللواء 300 التابع لجيش العدو الإسرائيلي داخل ثكنة شوميرا في مستوطنة شوميرا شمال فلسطين المحتلة بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75940" target="_blank">📅 19:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75939">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📰
أكسيوس: ترامب يقول إنه متردد بنسبة 50/50 بشأن الاتفاق النووي مع إيران أو القنابل، وسيلتقي بالمبعوثين لاتخاذ القرار ؛ وقد يتخذ يوم الأحد
ترمب لأكسيوس: إما أن نوقع اتفاقا أو أضربهم بقوة</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75939" target="_blank">📅 19:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75938">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📰
إعلام إيراني: الأخبار المتداولة حول مقترح إيراني لتجميد تخصيب اليورانيوم فوق نسبة 3.6% لمدة 10 سنوات عار عن الصحة</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75938" target="_blank">📅 18:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75937">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bG1r1zJllHEOfB7adGkrFRVaG4p_jBXwdvsDBMI0I8FhCarcMdrVz4qdVGk2UBQgYOhWEUld6rKwIZCXn9-vrHrgHORSypKk0N8d7Usoa1bLqdSz33MmhnjFBM1T5G2FdTwlrZoALhoTllIg3Q20yze1Vso5ysUCD6JUJN7o1YJCLrd02uxwV9J8Kt34lRMkoVCIYbYEScUFG2YZ-3C8p9r3KP92_8ugV4jJPazCgHdmkXeuJ6JDp1VZBId3Xtg90v0jTd6SjS2s1eGiiAzpBUderkjHklz5m_9jIxyi4b-ejZEENTj2roajAcITuZBMUJSk3rqdfE-u8EnVmGp7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إصابة موقع عسكري في الجليل الغربي شمال الكيان بمسيرات حزب الله</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75937" target="_blank">📅 18:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75936">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🌟
وزير الحرب الأمريكي:
طلبنا من قواتنا الانتشار في الشرق الأوسط لتحمي الأمريكيين وقواعدنا من وكلاء إيران.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75936" target="_blank">📅 18:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75935">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🌟
حزب الله:
أبابيل المقاومة الإسلامية فوق مستوطنة شوميرا شمال فلسطين المحتلة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75935" target="_blank">📅 18:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75934">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hskeScI4k6s9DKR0nmw9-nmD05oAiaTwFt7SN8Rs9ECfHcoBKT8lmXta5LSI5Qf2I3WLkpGrGliVVqwj2c0V99kWdNK6r4ecAKdJyWzAIn0zKrjan9tGro63Nw-a2m8rWH5o6AVHwDDDwAbfIw5WlMfOvwLAoR2CzgmA6aJDU_UHz0j19_MR-kUwBJmxkpA4fu5a2MWgMShsCUkfUpjfSTI07jXUMq6tavjqtPFHA4vhTvucW7wVAO1FfzYhNV2KUZ3AOVFtfdmfLlN7ETv28L7HGyhLkR0tqmow8_GmfBZTzoyuXh4lHzoY8Qmg9c9vJYxG2k0I7rvrRikh3JBOCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب ينشر
: الولايات المتحدة في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75934" target="_blank">📅 16:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75933">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
‏
وزير خارجية فرنسا:
منع بن غفير من دخول أراضينا اعتبارا من اليوم.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75933" target="_blank">📅 15:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75932">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSLt_EhjKHkVBm6nx8eNmeEIyCkMFywZKLPn2HvQUMtnVFIWYrvMvRueiZSreL64dAndqCwPZkmt7TNpqVVPTGvxXGU1iCds4vCpStrGhzNoCUaU4Kh_oksJ1o54ofAU_M5Eyh6kOeTfkOg0r07p2aAY84d7advao8Tr3nDp8mKXbQpepQLG4FHkWsZZE8AxM9Cy8MEOlavFY0B9AYYcqqZcqEKmYz5_8ALjrntE0wbMTL1mB5Ygj5ZK8eaGKtvhtraWI4XzeMY32H_4ZjYXx5EkRb3Wl7XZzG8y76mtfZhcv_XkSW77yoSXDhmQAwSXScII4VDA4hC2uPK6pQcDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النتيجة الاولية  يونس محمود ٢٥ صوت عدنان درجال ١٠ صوت</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75932" target="_blank">📅 15:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75931">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315a28e845.mp4?token=ZGgVropUpUkuBsKB8sBxwtZ0jiDn4a4vMYixz_LB3UmqKBEBYr45VOdH-Ws4Nn_qqi-sOYeEdFYLBypoYh7RHV_eu1g5M7zsuItfcsBSak2_MdIvYvzctmbxFd08wriq_aPS-4jb9tNkeIb6v2vWRG2ciOAIexZvbbupryvrDmzqBLGOuqW-cRlfJE60e_L0RS1vyY0QD6fZzShNXvlr3bfae4Dcs1pet4GXoNCxFI2SSN_G6Al55cVftGno04TfenX4qcMcsRJVnNGf2Us2xvDW8yVYbXyIf2B74IOtDVNs9xFJwr-DFW0pwco35YmMbfp6I7TsKV5qnUywzFB55yiayzJwtcMb7lyBEL2RwAWM3vHA1eEdjA6R-QS7Fm9Xdy2HeBP_MIe-iKcxvZ_JnodPtWzsrzAg3_D-zuZyTEs0yJK3ixf71ZIY2APa5Ni9h1r0sswjkTXzxvbrVfZeJr4dtC4pq-2wUiYaQIgW8pI0AL2SEKqLSTgj1LhIcOZcmqYnHewj95ObU54lXMGjpGWR0v6u_nPDN_wEZibUQ_KSvqVvIvwWGGQm1MkQxyOAeWQMG6bwjLcOg9JAibh02ChTpzuH6gvC-BRG10yIucFylyA4jKUE95XuL0d0ItRCI2Va86_UgEo_qYu-5-hVag2Utj62pNCr2oLn3lwOtS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315a28e845.mp4?token=ZGgVropUpUkuBsKB8sBxwtZ0jiDn4a4vMYixz_LB3UmqKBEBYr45VOdH-Ws4Nn_qqi-sOYeEdFYLBypoYh7RHV_eu1g5M7zsuItfcsBSak2_MdIvYvzctmbxFd08wriq_aPS-4jb9tNkeIb6v2vWRG2ciOAIexZvbbupryvrDmzqBLGOuqW-cRlfJE60e_L0RS1vyY0QD6fZzShNXvlr3bfae4Dcs1pet4GXoNCxFI2SSN_G6Al55cVftGno04TfenX4qcMcsRJVnNGf2Us2xvDW8yVYbXyIf2B74IOtDVNs9xFJwr-DFW0pwco35YmMbfp6I7TsKV5qnUywzFB55yiayzJwtcMb7lyBEL2RwAWM3vHA1eEdjA6R-QS7Fm9Xdy2HeBP_MIe-iKcxvZ_JnodPtWzsrzAg3_D-zuZyTEs0yJK3ixf71ZIY2APa5Ni9h1r0sswjkTXzxvbrVfZeJr4dtC4pq-2wUiYaQIgW8pI0AL2SEKqLSTgj1LhIcOZcmqYnHewj95ObU54lXMGjpGWR0v6u_nPDN_wEZibUQ_KSvqVvIvwWGGQm1MkQxyOAeWQMG6bwjLcOg9JAibh02ChTpzuH6gvC-BRG10yIucFylyA4jKUE95XuL0d0ItRCI2Va86_UgEo_qYu-5-hVag2Utj62pNCr2oLn3lwOtS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 21-05-2026 آلية هندسيّة تابعة لجيش العدو الإسرائيلي في خلّة الراج عند أطراف بلدة دير سريان جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75931" target="_blank">📅 15:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75930">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d509ff84fd.mp4?token=Dnhnnkfv-LdS7G8-ZHLdkGpmDIozixP1IXXJqW90K8tAL_l_YGIpnz_l2j0NGUoFFm8KzMmTt2zaiAmP-UQ8i1tPoc5Y-iwEA6WfmHaKV68Azvss8f-6Ct7_6r4bO53qpOAwKMArWh_KYiERsbY-0FqMpAjDeuYc4eEmyiOFLehEF3fHp3xs3OSJRg1HfTCnJ81W-EThvqr9U47FdKBzSKBC4JuRQhqGeChbB2RIcuQucYYKZUI6DITiex28OAhuG-pVjMO-ktPEqTK_h4vq4P98YvIVoPTkfQrlW54xvYbdOmPMRRf3sSnhjEuZCBsRCbmXC-SySKUZID3zfUFYtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d509ff84fd.mp4?token=Dnhnnkfv-LdS7G8-ZHLdkGpmDIozixP1IXXJqW90K8tAL_l_YGIpnz_l2j0NGUoFFm8KzMmTt2zaiAmP-UQ8i1tPoc5Y-iwEA6WfmHaKV68Azvss8f-6Ct7_6r4bO53qpOAwKMArWh_KYiERsbY-0FqMpAjDeuYc4eEmyiOFLehEF3fHp3xs3OSJRg1HfTCnJ81W-EThvqr9U47FdKBzSKBC4JuRQhqGeChbB2RIcuQucYYKZUI6DITiex28OAhuG-pVjMO-ktPEqTK_h4vq4P98YvIVoPTkfQrlW54xvYbdOmPMRRf3sSnhjEuZCBsRCbmXC-SySKUZID3zfUFYtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
طيران مروحي كثيف فوق العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75930" target="_blank">📅 15:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75929">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
قائد الجيش الباكستاني يلتقي في طهران مع قالبياف.  انا نايا...</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75929" target="_blank">📅 14:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75928">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrl4Z3dT-IMtrFiXpTwHv4xUjeBsqmC_5sHty12llyZ8nL__4LSCnXBpHzJxti1B_q9IpF4cGrHZ6_J3FKwHDWnLrFaA1_HMVhhBFjRq1JTomXPjlHHu5mB_Ho5f4yXxwLetHadzs4Ynvlds_8wn5G-1KJ58zp3pwoSkIuWwyCDosJdrw0nRiXADntWbISJNRhCxt9_O17OjjlRb8s49y2x3OFazDoViJrjmSWY3iZyxgywMWAiPMVjIKeEJ1ubyIRkxk8vM25jrBcD3La7N7wRhR3azxPDGtC8HFNOovJ7IQCLmC3XNJfAeffxsGIY1bAHXE2vtKqEIwTNQvblAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
مجاميع مسلحة تابعة لليكتي و الكادحين المعارض لايران(كومله) تفرض طوقاً عسكرياً حول جبال سورين في السليمانية شمالي العراق، تتحدث الانباء عن محاولة لاعتقال محمد حاجي محمود.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75928" target="_blank">📅 14:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75927">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok2nhHSYPOw7U5Jwlb4F9szPFftHS8V0OnlOEdaQNo_G45BpaUgHGtC1xPH5WMYGb-qOatiEgDo5sDwej1NSL5h_F43fx2ArIwLWfYdFTSISL2ykKRjJTMx7HTCcjVX2fVyCXRk4LMK-aFS70KNz8FENpV6VB_6kabzQYy9Tg7kMm1ZFgbacdC-EaFnaHpjanRzORlGUXxd8DGtJCMGkrhCyLMBsdUL-QthR1TF4D6qmAZSoOJ6Uiy1otxzqJ2ISyM3USg_2YlYr_S3dWXqI7-1jYJK8J2nt3gRwTn51yh1EMEOG2vAsROPV6bo8WFg7F6nJLmrQo-jbk7WgBOPpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لم يغادر الوفد الباكستاني ايران كما يبث إعلام العدو ؛ حاليا تنشر كمية هائلة من الأشاعات لجس نبض حركة الدفاع الجوي الإيراني و القوة الصاروخية .. حركة شبه طبيعية للطيران المدني في سماء العراق</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75927" target="_blank">📅 13:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75926">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026 موقع هضبة العجل وثكنات أفيفيم، راميم (هونين)، راموت نفتالي ومعاليه غولاني بسربٍ من المسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75926" target="_blank">📅 13:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75925">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBnG0Dat4suEwpAtbtd5jxcw6MXGtpuK41qZEmeU5NEq3h2iYMvd6o3NXP2LUzbEBc8iUNS2Hf7ZiM8jQ-BI707mDE_-9lhvWfcgL01mpQHsQRooaP5HiE_nSaY-kPC7BvpaayGIDSwWGzXDwihO3-0CJVeTaJ_dGs4KkwnnOXGCW3NRoaQfhz5-3C3zXJ_rpO9keYYYTB-MAeg66-i9rSj-PxcrIUUd0T4-E6FNAolLNpz-5CexS8sU2HyCB9X48GZ_peF5J2X7ULInSFNU2ZnoK4aVpD4K3pt0Shy67VifBgMbFKbbOWV4oEqsVqo_i46csxLD0BiBXt4q-KM-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇧
البحرية البريطانية:
وردت تقارير متعددة عن اقتراب زوارق صغيرة من سفن، كما شوهد زورق صغير كبير مزود بمحركين خارجيين يحمل سلالم وأسلحة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75925" target="_blank">📅 13:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75924">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⭐️
‏
تايوان:
الصين نشرت أكثر من 100 سفينة حربية بالمياه الإقليمية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75924" target="_blank">📅 12:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75923">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⭐️
طيران مسير من لبنان يهاجم مستوطنات الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75923" target="_blank">📅 12:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75922">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ed39e6b3.mp4?token=YYtOcL_hzuRsbf64SPKsYMSZiBJXZfsTTB5BaVoE_7PjI5K4gFw8WQV8fwqMYJUU-Zlno3Db5qIfJHSBmeBAsxst0HZLqc1_EdaHQHdykqKrx0AFICC1-zzy0hjTYtHD9aYyF8T6t5qpjoMK8zFqwbmApFiDdarxWHh8GlxL8eghoYL_3u-mZaWVEUVk74iF6TE63qXIEmle4ktfLQ6arp2LcyUXDvbCNiKf6RvstVoNEmXoSU07c2bJe1oN5WNDKrFHISCh7KL6hG8hz6CXXhQk98E0vVdEGzCsp6XN2afP-t6_VHvk4ham3MrisvO5KQPzaYUzW_Ld1BhL6SHs6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ed39e6b3.mp4?token=YYtOcL_hzuRsbf64SPKsYMSZiBJXZfsTTB5BaVoE_7PjI5K4gFw8WQV8fwqMYJUU-Zlno3Db5qIfJHSBmeBAsxst0HZLqc1_EdaHQHdykqKrx0AFICC1-zzy0hjTYtHD9aYyF8T6t5qpjoMK8zFqwbmApFiDdarxWHh8GlxL8eghoYL_3u-mZaWVEUVk74iF6TE63qXIEmle4ktfLQ6arp2LcyUXDvbCNiKf6RvstVoNEmXoSU07c2bJe1oN5WNDKrFHISCh7KL6hG8hz6CXXhQk98E0vVdEGzCsp6XN2afP-t6_VHvk4ham3MrisvO5KQPzaYUzW_Ld1BhL6SHs6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
ضمن الممارسات الوحشية الصهيونية..
قوات جيش الإحتلال الإسرائيلي تقدم على إعتقال عدد من الأطفال الفلسطينيين في رام الله.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/75922" target="_blank">📅 12:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75921">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
المتحدث باسم هيئة الطيران المدني الإيراني:
لم تصدر هيئة الطيران المدني أي إشعار جديد (NOTAM). ننفي ماجاء في الإشعار الذي نُشر مؤخرًا على وسائل التواصل الإجتماعي. لازال وضع الطيران في البلاد كما هو، وتُسيّر الرحلات الجوية وفقًا للخطة الموضوعة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75921" target="_blank">📅 11:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75920">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⭐️
رويترز:
بعد ثلاثة أشهر من حرب كان من المفترض أن تنتهي في ستة أسابيع بانتصار حاسم، أصبح ترامب عالقًا في المستنقع الإيراني، غير قادر على إيجاد مخرج يحفظ ماء وجهه أو توسيع نطاق الضربات.
على الرغم من الضربات العسكرية الأمريكية، لم تنهار إيران؛ ولا يزال سيطرتها المستمرة على مضيق هرمز - الذي يمر عبره خمس إمدادات النفط في العالم - تشكل أهم أداة ضغط لديها.
يقول المحللون إن الرئيس الذي يتباهى بالانتصارات يواجه الآن تحديًا قد يقوض مكانة أمريكا العالمية أكثر من أي صراع في العقود الأخيرة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75920" target="_blank">📅 11:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75919">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAZhMiOk6KmT1pQLwGcsNyue-PVbz1-SUOG5Lv5PkGJk8VoPVu60CL8pulsetm_VU-mpFdCKF7mX9J-oO-i3g2nbqN4z1Fga_Ku0BpDTs8lh2jBjOmJUGBF-n2oMLXtjF43VZCx_Dge3sCAtnWvAcGVdjNw1l18dZXrGTwlvR6Q56faS-myiXRy2BBMeygop9velR6dl17gUHML8Q8EGv-nGZr-h3Bux15acAnragx-5aTDW_W0sFy_hD89TkFFRGmbiABpppl0r4ZLHdzVtSGSaWjdjCoWl-Dur46qvpe61d2M4dULCIbKjDdyzEz4cr8kMtmk_XXYV1IupoH6fYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوالف الگهوة   مسرور وارين بارزاني وسومو والزيدي في بغداد ..</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75919" target="_blank">📅 11:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75916">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZbkPxinrp9Smb3ikuAlRMudrYGgdOXCl6lNaBzZUZx16TpjBUbSAuAVgBFDlJW0aBJVS_s5JlZ0WXGvAO667owQinc9dHRlGj3muWpakqKulFwZdaERrdsbSoq8kEJYFcWGq8MifSGcXFq98bX0hlAzUyUex8MCTXI062POPsEp8btOF6Cq77lqG8QeWoIFQu9yMCoLDNda2i0U366RUJC2N2Med3bNhQGweTGisc9nlHb8ACezPGISX1BGad4rcRwbiE8VUaZiT6WZzOIRhld9hQN2blZonSUShZc5OZ2xyoOBIqfJuMcSIHueOANium_UTw8ZOv-gSt_al3WqXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHmXEdfw0VDe6Z-YJ7pevztcc7oWqPAD13SM1NtMZIAC8D3HknkkcNUX9EmhJ0iaTXx13UeCxAPvvzzx47T2EiLQ7J054JHK5hnPaU36rv8OA_bq6ctTGRXQhaJXa-bNJjqpM3nwPB66L3vT4icgXsYP7gzbQf7W-wF7-qlIuVjYvOF-OLOB3R4Nvp1J6C-QduIWtUyLesR216csoPmD0pftHwzZ61boR96yfVMkyTn_XUJ6qPbB-jmKj8Tp1uSgU0fWANEbk5nTrHax9-CJsbpqz2fxYM21MetTI2YPKCvTwkZ7sNJ0OFcQvSz64z1TNb27GmqwyzZsN2JUqq4l0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dRDvo9RZcfd4tk1vKuxgNbULQe4vt4Noq2VLTmGc8sD6d4fDEXZwCCSrXrbZNqW0du0VbaNzM_03IKUvf-MCi3UqSG7zH9jzXm4TycfnZkBLA0JDsNtxTVtrCOZXTj2r2ksPH7oCP8IO94yljlgUHxdMzK-2ABkBH1OdJOwbEKE9sB2NF3kmr7bqT-QmMBSDTjZk61X3DQquri7jTfLVD1kK1pEW90RVDGItqed6BJWAYhVeofsCEhXyErpMHlBtekqO7CAb0vjpt42mVtz7VO0Inzv2Vvql_HUdomOZc33Q3edoJBTQpZbjgnjVaottV4LiJZL3cR9Y_i1LNVgbgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
تم رصد طائرة هليكوبتر من طراز MH-60S تابعة للبحرية الأمريكية تحمل نداء RESCU11 فوق خليج عمان. ‏قد تكون مهمة إنقاذ. (هذه المروحية تابعة لإحدى السفن الحربية المنتشرة في بحر العرب).</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75916" target="_blank">📅 09:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75915">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzqbcubgpOgHAkOM-FgT-7hTQ2sQS1ohgF-_uJSlnYlvmTaNUTZTUHNi7jNfu-sXAtr-5yaaHpUpmALfqB7H9ktlibQbZt4MuTxXX06jFyNndZewroRfVqLlAL02XXOn0a_UB9-qe3Oz7gSFgjb_tY-kzWXDlbboVMR3gNrbNWI4VkIm1jjhZ8fjYOGWDHJUM7ixu09RP4n1CWcRbi5UeCLmPcoOOBvHKmx3Jqatimld6ZADO35ilPsUWGbWGQeNBCBvsjr4g0v3lEvqB2Yao-THWWtszf-4Fgq7mqk4Oe9VV3I9nKr3sMU2sYU_wKS312oeyOdHURq5nqFCn4fyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
الإحتلال الصهيوني يزعم إحباط محاولة إدخال سلاح وذخيرة إلى الأراضي الفلسطينية المحتلة من الحدود الشرقية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/75915" target="_blank">📅 09:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75914">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⭐️
نيويورك بوست:
يُزعم أن محمد باقر السعدي، وهو مشتبه به عراقي مرتبط بـ "الحرس الثوري الإيراني"، خطط لاغتيال إيفانكا ترامب انتقامًا لمقتل قاسم سليماني في عام 2020. وتقول السلطات إنه كان لديه خرائط لمنزلها في فلوريدا وهدد عائلة ترامب عبر الإنترنت.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75914" target="_blank">📅 09:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75913">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⭐️
طيران مسير من لبنان يهاجم كريات شمونة في الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/75913" target="_blank">📅 09:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75912">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الدفاع الإيرانية:
عدم احترام حقوق إيران سيؤدي إلى مزيد من الهزائم لترامب. ليس أمام ترامب خيار سوى قبول مطالب الشعب الإيراني واحترام حقوق بلادنا.في ساحة المعركة والدبلوماسية على حد سواء، يُعدّ تلبية مطالب الشعب الإيراني السبيل الوحيد للخروج من الحرب الثالثة المفروضة على العدو الأمريكي الصهيوني. كما يجب على ترامب، مع قبوله للمقترح الإيراني، أن يحرص على منع المزيد من الخسائر والتكاليف المترتبة على استمرار الحرب، سواء للشعب الأمريكي أو للمجتمع الدولي.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/75912" target="_blank">📅 09:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75911">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrfUJS3-sUzAgQjJBmlAfT4ATvzEngh2IhIaciL04kYJFdrbJgpP7V155jr-klTRxcELIeUIJRLaFk-Ot4VUCWb_CW90ENjRxutIS7NT035FhlGhKdCfhMfib_QZiD4BkIW7IAF_jUVtWCg_lji4JLdMGaUn5JP3LuXS_BT6P8s8ElIPVIC6BO8Ie5gyz9eCE9BvqeNlX6vWEFULqw0EMGv7fRdE-1mucZSBjdr2v2sLn4h27DA-62q5cv0OX-CLi10T86zjopQYWrP9PbFoQIV0YE5nAXW3k6aHJjthMfoIa9JxKOpHK8ucyGKy-6QLMIxulILJ8IUO7enxtxCePQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لم يغادر الوفد الباكستاني ايران كما يبث إعلام العدو ؛ حاليا تنشر كمية هائلة من الأشاعات لجس نبض حركة الدفاع الجوي الإيراني و القوة الصاروخية .. حركة شبه طبيعية للطيران المدني في سماء العراق</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/75911" target="_blank">📅 02:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75910">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">لم يغادر الوفد الباكستاني ايران كما يبث إعلام العدو ؛ حاليا تنشر كمية هائلة من الأشاعات لجس نبض حركة الدفاع الجوي الإيراني و القوة الصاروخية .. حركة شبه طبيعية للطيران المدني في سماء العراق</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/75910" target="_blank">📅 02:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75909">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3WXbVtdi0PadLMWUG3fLzBwh0fq04BD-OLTB_CZjsK0Yx-7O2pHw4BhLyjlC4WF7l2TpxoRedOniGDzLDmB6cdAyrgS81Ks81SXm664_vEhNZInekj31mDHVtW9hX_ztT5S2lU6T6c6zv4I3-WvTJpuhItQH4BqGD7ijFlXpQPpjANofD53T6zqOwZmgfDRoJ3UVxDaSPDKq_s2iaHnvjt9U0x31283Et6ulpIZLPBCftu2okvl-VOfIG5GLHWjvrGrcbmDMzHWI9YSSJ782-9s_OMt_E-1qPV4gu69U4AIHRQ_imazs14df9_HkvgVCweuUgzoDTK3npoqUP7m7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنشط القوات الأميركية في سماء بادية السماوة جنوبي العراق بنشر طائرات إرضاع جوي الأمر الذي يشير الى وجود طيران حربي آخر في سماء العراق ..</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/75909" target="_blank">📅 02:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75908">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نقابة البحريين العراقيين تطالب بتحرك حكومي عاجل لكشف مصير البحارة العراقيين المفقودين قرب المياه الكويتية</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/75908" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75907">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">📰
وول ستريت جورنال:
أوقفت الولايات المتحدة مؤخرًا إصدار تأشيرات الدخول للمسافرين من جنوب السودان أو الكونغو أو أوغندا بعد تفشي فيروس إيبولا بسرعة كبيرة في وسط أفريقيا.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/75907" target="_blank">📅 00:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75906">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1153e5630a.mp4?token=G9h6JYAGUV-nSjhYQGmozSME6GNTDEqzEplYqrNkxZxEZheY8JqYGLVtKU7BlWuL7K_wskcDOhkxnF4Ghv81Xyue82h4cOG8SKdXfyPk0FaOORNI0hYxlbWMPemsmkEgURrECJyGdvUUEJV-MJ1WPHA56Wae6iyzhI8Zd31LWS5DLClFS0dhVqotVmkjr-MQP9osSFeXYGpehUlB9VjjhnhXTsNgSil5cMPBBjcUiexSe_qdO0xrB05pugAa2usqldoonY3JjIlGThGDjWos-1Uj_H5yDy02tAWeLvXN0htNR8Uafgbg-Habg6B_2ZD675X25ApXkZEJsvjYmrnPDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1153e5630a.mp4?token=G9h6JYAGUV-nSjhYQGmozSME6GNTDEqzEplYqrNkxZxEZheY8JqYGLVtKU7BlWuL7K_wskcDOhkxnF4Ghv81Xyue82h4cOG8SKdXfyPk0FaOORNI0hYxlbWMPemsmkEgURrECJyGdvUUEJV-MJ1WPHA56Wae6iyzhI8Zd31LWS5DLClFS0dhVqotVmkjr-MQP9osSFeXYGpehUlB9VjjhnhXTsNgSil5cMPBBjcUiexSe_qdO0xrB05pugAa2usqldoonY3JjIlGThGDjWos-1Uj_H5yDy02tAWeLvXN0htNR8Uafgbg-Habg6B_2ZD675X25ApXkZEJsvjYmrnPDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ترامب
: "قال ملك السعودية إننا الدولة الأكثر حرارة"،ولقد استخرجنا الكثير من النفط من فنزويلا، وقد دفعنا تكلفة الحرب أكثر من 25 مرة.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/75906" target="_blank">📅 23:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75905">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
🇮🇷
وول ستريت جورنال:
يسعى الوسطاء جاهدين للتوصل إلى اتفاق مؤقت بين إيران والولايات المتحدة لمنع شن ضربات أمريكية-إسرائيلية جديدة، يحذر المسؤولون من أنها قد تحدث في غضون أيام.
تحاول باكستان وقطر وغيرهما من اللاعبين الإقليميين سد الثغرات بشأن البرنامج النووي الإيراني، وتخفيف العقوبات، والأمن الإقليمي.
الهدف ليس اتفاقًا كاملًا، بل إطارًا مؤقتًا يمدد وقف إطلاق النار ويسمح باستمرار مفاوضات أوسع.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/75905" target="_blank">📅 23:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75903">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f688b7274.mp4?token=BVj5XXb49zcKfiAzYs2qO_BxrRb4vdDbxK3wdhORtPpD5hfGaD13KD9U7OHCKIMZbyfR30wqZchplJ925CPZAdH9ovnShGP9_OiLfgtyZ84dthRnKvh-KMHrvjNW4Y6v84fcQfk965tjmpqEiSBkngWxDks2cOmcj1nQ8tT9KH0zuMgGcBXB95NSnHKHgSv0bvHnnsrefbxvIxvcAvtOAlDEEs9mVEgsMoDwI_97USHEPb5btmK-bLcNFxwe7xhDu-5QlP7KHbpSjjGzBPOhN75Vhm96H4Fk2jQ04cMjKwQ0YuTkM4Fr6OGVzzjRz4ywByfNt4mOzDJj0EZZ1t5lGpGmv5uUyhDPWZJcnTupfCEhDLpNizQCHqAHfwAPQLFUtr0hc-aNeUaePnlKcNPdP2KBIzKg0uwetBgMfHTWgTfOPtyCJflDuNlxCwhcQTQl3mY6GC3gSH-ZeWP4ca53SoqhSE_7hnfpwMelYR5jy9qEZP7Vw1emhSKgg8wTqJMAXNTwcNx6MI-_4Js8cQEEOuhGJoPwDEmjlSzFLs1b71IbspMYW4T-ulrYhadsidsrRTOga6JZ04tZPohUvvVc6bdYPeCw5s31230l86i4kUGfd6XmLASWikJm74IJnVT26HX15aB6QC8QFwZjv1__lAhE4-000MElAxS4wsHv5XE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f688b7274.mp4?token=BVj5XXb49zcKfiAzYs2qO_BxrRb4vdDbxK3wdhORtPpD5hfGaD13KD9U7OHCKIMZbyfR30wqZchplJ925CPZAdH9ovnShGP9_OiLfgtyZ84dthRnKvh-KMHrvjNW4Y6v84fcQfk965tjmpqEiSBkngWxDks2cOmcj1nQ8tT9KH0zuMgGcBXB95NSnHKHgSv0bvHnnsrefbxvIxvcAvtOAlDEEs9mVEgsMoDwI_97USHEPb5btmK-bLcNFxwe7xhDu-5QlP7KHbpSjjGzBPOhN75Vhm96H4Fk2jQ04cMjKwQ0YuTkM4Fr6OGVzzjRz4ywByfNt4mOzDJj0EZZ1t5lGpGmv5uUyhDPWZJcnTupfCEhDLpNizQCHqAHfwAPQLFUtr0hc-aNeUaePnlKcNPdP2KBIzKg0uwetBgMfHTWgTfOPtyCJflDuNlxCwhcQTQl3mY6GC3gSH-ZeWP4ca53SoqhSE_7hnfpwMelYR5jy9qEZP7Vw1emhSKgg8wTqJMAXNTwcNx6MI-_4Js8cQEEOuhGJoPwDEmjlSzFLs1b71IbspMYW4T-ulrYhadsidsrRTOga6JZ04tZPohUvvVc6bdYPeCw5s31230l86i4kUGfd6XmLASWikJm74IJnVT26HX15aB6QC8QFwZjv1__lAhE4-000MElAxS4wsHv5XE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
14-05-2026
دبابة ميركافا تابعة لجيش العدو الإسرائيلي في مدينة بنت جبيل جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/75903" target="_blank">📅 22:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75902">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي حول إيران: المفاوضات مرهقة للغاية والمسودات تنتقل ذهابا وإيابا يوميا دون إحراز تقدم كبير.  الرئيس الأمريكي شعر بإحباط متزايد خلال الأيام القليلة الماضية.  الرئيس طرح احتمال تنفيذ عملية عسكرية كبرى أخيرة وإعلان النصر وإنهاء الحرب.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/75902" target="_blank">📅 22:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75901">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🏴‍☠️
حدث أمني جديد يتعرض له جيش الإحتلال الصهيوني في بلدة الناقورة بجنوب لبنان.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/75901" target="_blank">📅 22:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75900">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي حول إيران:
المفاوضات مرهقة للغاية والمسودات تنتقل ذهابا وإيابا يوميا دون إحراز تقدم كبير.
الرئيس الأمريكي شعر بإحباط متزايد خلال الأيام القليلة الماضية.
الرئيس طرح احتمال تنفيذ عملية عسكرية كبرى أخيرة وإعلان النصر وإنهاء الحرب.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/75900" target="_blank">📅 22:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75899">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
حدث أمني في قاعدة بينساكولا الجوية البحرية بولاية فلوريدا الأمريكية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/75899" target="_blank">📅 21:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75896">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCnVenIscgS8fzHYsYM81BixTUvrc3dJujuY_T72onvfM2NnIG5_VnqKAMB5vz6mcnUzkLkzSIt5XjgoUUVWRigQNZ2TXsmq1IsY4x4zy1hA6DxluciopMW3yllV4b1RKBQouFLqX2bpsWvzRBQB7_FMaW-cC-8O_21iid3i0xvS2NICqBBWuIQkkfgne3kEgBAcyPp8ND6N9RrgVuFnzM5DHEjxCSmTOmBZAWquzw-c7CkP0Deeh2u3zRgdvaiSydDOQJPtVqDmoTxs1krZVtnX0b9ZsBUCkXsMimkZ8KAz6kzEpr2SmBdQS3b2OaDZx9D9_zb0Uy3tMZK8torPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYVHicUoRraviKW2kMONGl9pXGVRsHqcBiaEHL8nMe7lyJ0xLsFlWgKb_H4lTBI58izUgwcC8mU5E0y97xXQldmKVdQG9g7wiISvDVcJxyoFWpZ6zpAAI4qr1A8RjZsX5vx53dPwILBlU-pXI9sF9vNf6ePv_jj8e8s6GL1KfpcH_0qmcJUpHY1FQ5yDWwA7ikrHzj75e1MA54YdGYYWsEr-j-9Tc61xXn31wSfNxrK-uUSM133l564IMAIOZ2gvO9Q9BXOAtS20WUfikmBiEv0A1_UdNgrqiVOnqIopYIEbPfIRjTIQOnIR5Wj77mC_vvV-eQ0rvjg5z3pSmQ7pmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
سيتم اغتيال ترامب يوم الأحد المقبل، بالتزامن مع عيد الأضحى المبارك. وقد تم اختيار ثور يُدعى دونالد ترامب في بنغلاديش للاحتفال بهذا العيد الإسلامي. واشتهر هذا الجاموس الأبيض الأمهق بشبهه الكبير بالرئيس الأمريكي.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/75896" target="_blank">📅 20:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75895">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يتمكنون من إحراق دبابة ميركافا تابعة للجيش الصهيوني في بلدة مركبا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75895" target="_blank">📅 20:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75894">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇸
أمريكا تنهار من الداخل..
استقالة تولسي غابارد مديرة الاستخبارات الوطنية الأمريكية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75894" target="_blank">📅 20:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75893">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: سقوط 6 إصابات في صفوف الجيش الإسرائيلي جراء استهدافهم بمسيرة انقضاضية في مرتفعات راميم بالقرب من الحدود مع لبنان.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/75893" target="_blank">📅 19:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75892">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية الإغارة النارية التي نفذتها المقاومة الإسلامية بتاريخ
17-05-2026
على تموضعات جنود وآليات جيش العدو الإسرائيلي في بلدات الخيام، الطيبة، العديسة، دير سريان ودير ميماس جنوبيّ لبنان بالأسلحة الصاروخية وقذائف المدفعية.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75892" target="_blank">📅 19:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75891">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
‏
ترامب:
لقد ضربنا إيران بشدة وهم يريدون بشدة التوصل لاتفاق.
لدينا أعظم جيش في العالم ونريد الحصول على ميزانية دفاع تصل إلى 1.5 تريليون دولار.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75891" target="_blank">📅 19:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75890">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏴‍☠️
نقل عدد من جنود الاحتلال المصابين بانفجار مسيرات حزب الله في المواقع العسكرية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75890" target="_blank">📅 19:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75889">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
إصابة جندي إسرائيلي بجروح في البطن جراء انفجار مُحلّقة مفخخة استهدفت مستوطنة مسكافعام ضمن إصبع الجليل.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75889" target="_blank">📅 19:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75888">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
حزب الله: استهدف مجاهدو المقاومة الإسلاميّة ناقلة جند تابعة لجيش العدو الإسرائيلي في موقع الرّاهب بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75888" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75887">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇷🇺
بوتين: أوكرانيا قصفت سكنًا طلابيًا و15 شخصاً في عداد المفقودين ومقتل ستة أشخاص وإصابة 39 آخرين</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75887" target="_blank">📅 17:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75886">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجارات عنيفة تهز مستوطنة مرجليوت شمال الكيان جراء هجوم حزب الله</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75886" target="_blank">📅 17:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75885">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c738e132a0.mp4?token=Y2IiAs-rHC6TWY0wPl6Gpcr7EEGdu5vbrhqq7fgnxWW7hPLksHuKTz-Y3HOcHKBxGd365-6yWg10lJNBDy3R26Na3sAlbEcEzF7o-Uz0Y_nuKtee_qvZTPb6Fqpi7nVI_U91c8fYjIHqJfkugiaQuwlRw0wpSlByscOyfqcNDkuNplZTR_sAXJAp7ydbalB9EAlY4PpIS37Rvdli3wMoj651vMCj30N3kPhbk0eKUtSdvyE1ugp3WbBeh8ULd2DTksIcZTOcNqiI0G370ie5OPkdhD5saSnCXwR-0tAI9cuDgce4IsmrdTLplaU_0kvvNhUIf-VWqnsDRdLzfCVtLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c738e132a0.mp4?token=Y2IiAs-rHC6TWY0wPl6Gpcr7EEGdu5vbrhqq7fgnxWW7hPLksHuKTz-Y3HOcHKBxGd365-6yWg10lJNBDy3R26Na3sAlbEcEzF7o-Uz0Y_nuKtee_qvZTPb6Fqpi7nVI_U91c8fYjIHqJfkugiaQuwlRw0wpSlByscOyfqcNDkuNplZTR_sAXJAp7ydbalB9EAlY4PpIS37Rvdli3wMoj651vMCj30N3kPhbk0eKUtSdvyE1ugp3WbBeh8ULd2DTksIcZTOcNqiI0G370ie5OPkdhD5saSnCXwR-0tAI9cuDgce4IsmrdTLplaU_0kvvNhUIf-VWqnsDRdLzfCVtLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">البيت الأبيض ينشر: من المرجح أن يكون "تشكيل 4 أجسام طائرة مجهولة، إيران، 26 أغسطس 2022 فوق الماء [رمز النداء]" مستمدًا من مستشعر الأشعة تحت الحمراء على متن منصة عسكرية أمريكية تعمل ضمن منطقة مسؤولية القيادة المركزية الأمريكية في عام 2022.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/75885" target="_blank">📅 17:20 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
