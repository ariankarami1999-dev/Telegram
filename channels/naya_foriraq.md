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
<img src="https://cdn4.telesco.pe/file/cQFBfWzxi_twoemKTIE28fsIA2wlv5jDAbKq0NRGE7_mtpJrHCu2NuczNbSxN3NF57D539HIPWLzjJrDQQv5NHDgq44p2MipeLLiZfOUd5ruQP-t-HpytOZ1VQaHXeDpcPsuAZc7uDIF4LPM6W06m7-tCbL1ReqGQVGmb0tmhj9Nsw6B7eTjm34b5CuN2zF66l9cHWo_NB-7e2aVFI2ep8pAt_sta4_82FNr-tLlj7IP8Ea0r4K9ghSGtMbmiCe829MUJVXBt5LizRVmVM0CZkdKSHo8CNH3-_-k7bnyrzJROKg9oi5adtiOf4wF2WlxJ7QsBa9SDRs_htNwy_gnFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 16:08:11</div>
<hr>

<div class="tg-post" id="msg-92493">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
تمكنت قواتنا المسلحة _بفضل الله تعالى_ من طرد واستهداف تحشيدات العدو السعودي من شرقي الجوف إثر محاولات فاشلة للتقدم باتجاه مواقع قواتنا المسلحة ونتج عن عملية الاستهداف والطرد ما يلي:
-إحراق عدد كبير من الآليات التابعة لتحشيدات العدو السعودي.
-مصرع وإصابة العشرات من تلك التحشيدات.
-ملاحقة ومطاردة من تبقى منهم في صحراء الجوف.
-استهداف تجمعات تلك التحشيدات بعدد من الصواريخ الباليستية والطائرات المسيّرة.
​التحية لأبناء الجوف ومأرب وهم يقفون موقف الحق مع شعبهم وبلدهم، يقفون إلى جانب قواتهم المسلحة في التصدي الفعال والمؤثر للعدو فأفشلوا _بعون الله_ تحركاته وكسروا بفضل الله زحوفاته فهزموا أدواته ونكلوا بعملائه وأسقطوا خططه وأهدافه ودفنوا في الصحارى والأودية أحلامه وطموحاته وأمانيه .. وهذا هو اليمن الحر العزيز.</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/naya_foriraq/92493" target="_blank">📅 15:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92492">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">في خبر غير مهم
رئيس مرتزقة السعودية:
أعلن بدء العمليات العسكرية لاستعادة ما تبقى من أراضي الجمهورية وبسط سلطة الدولة</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/naya_foriraq/92492" target="_blank">📅 15:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92491">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏مصادر يمنية: الحوثيون سيطروا على منزل رئيس البرلمان اليمني سلطان البركاني جنوبي تعز بعد اشتباكات مع القوات الحكومية</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/naya_foriraq/92491" target="_blank">📅 15:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92490">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇱
اعلام العدو:
جبهة اليمن على جدول أعمال الكابينت اليوم
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/naya_foriraq/92490" target="_blank">📅 15:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92489">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇾🇪
وكالة الانباء الفرنسية: عناصر أنصار الله يقطعون طريقاً رئيساً لمدينة تعز ويحاصرونها  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/naya_foriraq/92489" target="_blank">📅 15:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92488">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇾🇪
وكالة الانباء الفرنسية:
عناصر أنصار الله يقطعون طريقاً رئيساً لمدينة تعز ويحاصرونها
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/naya_foriraq/92488" target="_blank">📅 15:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92487">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي يأمر بتشكيل لجنة تحقيقية بشأن التجاوز على علم الولايات المتحدة خلال يوم السيادة
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/naya_foriraq/92487" target="_blank">📅 14:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92486">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انصار الله يسيطرون على سوق المركز ويستمرون في التقدم باتجاة التربة في تعز</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/naya_foriraq/92486" target="_blank">📅 14:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92485">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNsgZ5zFTc7vybnHstNPX_m3ZIqET8Pj0KfJUBiteL0Omwpkco_qDCetQzywlV4sD_toSnu7bZUF2pLbQugFcekVJLBIb8t-NMmRdtYMJIystTMOTwQ7jmRlQwUdEMYTXSWSsE-OXtVyyqOWQlPX9zASg4FTopJFVPNmq4AYC5z7mrZdzMj5AkPaOM15BsnEMkSN0ME0kZUgJ8ancn2V5FmPiD7AbdghSpbQCvQlBqnrn-vF5JRKpbGX2v6bg4lYOU7Gm9Dg21yHl7zw5r4o19yHVsY4V9k1Wu9nWWW5Ky6EpHB4WN5IIw6A_bCfj4Ilz1BtjDZNzK4herbys2aEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇱
غصب في الشارع العراقي بسبب غزو المنتجات الصهيونية للاسواق العراقية عن طريق الاردن.
العراق كان قد اعفى الاردن من ادخال نحو 399 منتج من الكمارك وهو رقم هائل اكبر مما تستطيع الاردن انتاجه الامر الذي سمح للكيان الصهيوني بادخال منتجاته الى العراق عن طريق الاردن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/naya_foriraq/92485" target="_blank">📅 14:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92484">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b3fa96286.mp4?token=RNsh9wuU7oPWVF7AY12lfV2Vp_R5-JUSJOCEvGdSWIRMRsSdsR6DSf1wGnZMQvntoVxb0NY_NI19wRZem2uMIVApP0ubC8cuy2dQhktrihVIPF_ujQIoHXzviA-OqVhCEN-WM0nWuQbmPiLqy24UZojvBtRGN1c3481RwxQYbBpgJJWh8RDMLXH7l0MHYbRCYXSkaMuJn54K1JwZfFQoKRucIwd349uDRqUBAk4FUgfrIahNmSjd2mJM1AFVCMdd3ZPAYhkFoAdRzWNQevEPNY8bR5foYzANsiEfvo8NgUca-1zQIK2VPejjShe2V-QCtCYusoK3MXB69gZHFHuUIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b3fa96286.mp4?token=RNsh9wuU7oPWVF7AY12lfV2Vp_R5-JUSJOCEvGdSWIRMRsSdsR6DSf1wGnZMQvntoVxb0NY_NI19wRZem2uMIVApP0ubC8cuy2dQhktrihVIPF_ujQIoHXzviA-OqVhCEN-WM0nWuQbmPiLqy24UZojvBtRGN1c3481RwxQYbBpgJJWh8RDMLXH7l0MHYbRCYXSkaMuJn54K1JwZfFQoKRucIwd349uDRqUBAk4FUgfrIahNmSjd2mJM1AFVCMdd3ZPAYhkFoAdRzWNQevEPNY8bR5foYzANsiEfvo8NgUca-1zQIK2VPejjShe2V-QCtCYusoK3MXB69gZHFHuUIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مصادر يمنية: الحوثيون سيطروا على منزل رئيس البرلمان اليمني سلطان البركاني جنوبي تعز بعد اشتباكات مع القوات الحكومية</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/naya_foriraq/92484" target="_blank">📅 13:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92482">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏مصادر يمنية: الحوثيون سيطروا على منزل رئيس البرلمان اليمني سلطان البركاني جنوبي تعز بعد اشتباكات مع القوات الحكومية</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/naya_foriraq/92482" target="_blank">📅 13:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92481">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKShszTQRss8m0Ab-7CVCngr2PMzpNNLO-s8UHzOhBn_9JN6plegcxGIslycqv_43AO0iOCKQ1KClDJk2VnoJlW1HA8GrDYzIzvlyWjhwV1kUDlb65NjVWwuOPFYOd6LwKOctQ8NWy5F9HIAfZzNJhrdKtPFJNfJFE7YJvNQ0lDTa2xKlk4ul1sn6PdaRehb2db0hjO8T0Mauzb8Dm38JMgfhuejp6iJhWwNi6VUA_8TZVNFmsOre6_WlcrIR_eLmVbMn3uI1L3RW9YAtrIqerac8FF6KH49BTLF36lXHgt-NiuqeBdlb0KFV6e5OANqsCd1n8AyK8NtWpqO2WbiZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد أن أغلقت نتيجة الإقتحام..
القائم بالأعمال السويدي يعلن توجه حكومة بلاده نحو إعادة فتح سفارتها في بغداد.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/92481" target="_blank">📅 13:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92478">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDBDTh1o-HLIWWoBuQuOvk7jRXKdyiHBNCBFeqNNlvAwEYO2mdrZ-zIudKRhq2IVHhWt_4vAxYGREvEKSdtCPgearkvxtF56xWmyRnl9_2b5m2G15Q0hpba9h_E7pyJcODUjAu1geOkIMh3yMM-9EBM0ZbUpk-IesSxO9Nca8FO-CsOWztwL7xvabyI3q2gMACwif_PFdjEqeohr5ibOrRL6J8jUzPEimFAUYb2C8i9y3El9et2cJH8e-Qwu_MtIGRHp8RehqI0I27ddfShE35hjJz-lYAay7E2Vq0g0BLO9bt7eYGdwu2yDGyjOLoki5AoXFnybnsDq39DCaPYqEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvuE0rqzGCb6Q5duoeOcRXNnEv8IjQgiqNBTTAGxo-ovsy6eKn7w1S6eqW9trY_KQ1vAtatmc_qX0JNC259YeBiBpyslFL3r-YHic3VzR2Wtv3G3MvJfcFWOr1bWc8UC9QXDD0LZieYxntNE4nZVUKZ88XBeTfr6JgEH9i6HO0snaSth_Mw7wTrUW4no2xUxvLo0mcV0y2IVYv0QK8QukGOMdX61jzFdi9rzroWMjFR3vMtBDRp_i19LUzzuiKwx3yVCB-zE4vUynFnDcr9cDlB7DCps_E3nFq6jAV35zio3azuCFm9UlQRuiSdrsP23LMfk_jdsbt7jMK1dZGR5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GoGbDKtRCHRBUPw-gl_DzIUUZ4zLwSLjBVMWcFDdfbejP46mrQ1z5A_5FBGAct5-iRoS_Y0NXKbnkO1I4qr2vgA5ipmQmo4DyJTC3p6AfH3LDcYEj-epzNO3Hu8w1tz8THJ77IwZvBxbdjZPySijMlOOgdmq7s_RSKaUgdju0K4TUxT0qsUCvZxqHehWl9_U-30jStxzXMcRB4ob8kwO8vD47gk7losADmcsUiK_p9EIqTHwvuhlLYHmKvfV4JijxuzDelDVdLBzbewe4mCjrwgGHVTlr_Yty_9DgHpbDMcA1QbuExvXLV-0WkgXTzQamsABmYCbZOPUjywoymrXmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
من إنفجار العبوة الناسفة التي طالت عجلة تابعة للجيش العراقي في صحراء راوة جنوبي محافظة الموصل؛ حيث أدى ذلك لإستشهاد وإصابة 4 منتسبين من الجيش العراقي.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/92478" target="_blank">📅 13:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92477">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الطائف الدولي بالسعودية.</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/naya_foriraq/92477" target="_blank">📅 13:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92476">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇱
عملية دهس في القدس المحتلة؛ مقتل مستوطنة كحصيلة أولية.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/92476" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92475">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
🇮🇷
مطار النجف الأشرف يعلن استئناف عدد من الرحلات الإيرانية.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/92475" target="_blank">📅 11:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92474">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0012925a86.mp4?token=af1LBbNnAaG02Hx9d6hn2GxqP2khRJ7FMZGsA2hwZBYvo3KNDtn0IWIfsJ5nw0Le9FS7v1E2QHSqkKw20onSG4tifmTi6w3YDaSarigsNCRdN__TXd2nH1KRX1mJqZv0czwVIM9j5CPemsRwaAy-X_xM5q24S58jiFW47eURy0RvHciQ3GyP0hf5LV6aAAeSltahQpBVQpOpcdXrrncK1QhNuxf-7lnArGZ5Bye5wmXYq9K40qSHCQZRyOoealA1uVDnP2Aa0bpqH8r9b4I_I1kIQ0aF08yHNYQS1TxWcc35vUk9qx_xd8cbcZ0tz9AJi1pIEHPJkqYi-swXyN5ZaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0012925a86.mp4?token=af1LBbNnAaG02Hx9d6hn2GxqP2khRJ7FMZGsA2hwZBYvo3KNDtn0IWIfsJ5nw0Le9FS7v1E2QHSqkKw20onSG4tifmTi6w3YDaSarigsNCRdN__TXd2nH1KRX1mJqZv0czwVIM9j5CPemsRwaAy-X_xM5q24S58jiFW47eURy0RvHciQ3GyP0hf5LV6aAAeSltahQpBVQpOpcdXrrncK1QhNuxf-7lnArGZ5Bye5wmXYq9K40qSHCQZRyOoealA1uVDnP2Aa0bpqH8r9b4I_I1kIQ0aF08yHNYQS1TxWcc35vUk9qx_xd8cbcZ0tz9AJi1pIEHPJkqYi-swXyN5ZaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
إنفجارات وتصاعد أعمدة الدخان في العاصمة الأوكرانية كييف عقب هجوم روسي.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/92474" target="_blank">📅 11:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92473">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYEduEDLuTV4eHAMx_vMeowMzAvvKC1oMr_wtdBhAC4tPSLwViJ6DFPtajig5m1G3-eiGzNx1ehbnJeBBhDUsL-YxgAZ52NdOnzCS79JhX7PkpaWP5ZSlp0zIKTCivAOBl-4JZUKVg8puZJHklnFdkS4a1MXf-NKUMGceMI_y8oQEb7lLfByQWveHtnTP2aIKg-LIwHBpI-CpgCrX1PwDqhqfZFBaNFDJMw5lCSwsOUABW2jOliq73SDkRQ4OzB9g2Xlo27aYwJKb--fdatYE36Xw4Eh7jOmD6WqWPxOk3GcnSO0iR6sTtosvLSdEKJNBEvfOwaBq6DEzHnb7LUDhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الهيئة البحرية البريطانية:
ناقلة نفط أبلغت عن تعرضها لمقذوف مجهول بمضيق هرمز ألحق أضرارا بغرفة المحركات.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/92473" target="_blank">📅 11:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92472">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqoTBbctfAJrs22_nEPvBKMMsE4wF2IJL69AIHGBopXArfgsqyfE4BKPqt6X83asDdhk1-56q86tmpJtaEwrA5iBa5xzv6VWV8qno2akhL7LB0CaOJhDq-jz1UAdNqohkkcB-5z1GA-f3etkJfNnIyxcYZPbzzpqxtnMNfHOe8bDlcOLuJTUcrOtjETyNNzdBHOYa-cFRxzVgzFzUVCOlxx5ABU2lu9euBoKAz6tM1_D0ln3Tk2uhx2_xe4ExqtcrMnwG-eS8c1r86uj9kYdKIPmmiFaNya4Brx-IC2-0GMJyaZlgQ5___d5IMMBIrm8VFGPGrHTrkp1XArae0uQwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
‏الكويت تقرر سحب الجنسية الكويتية من 415 شخصاً وممن اكتسبها معهم عن طريق التبعية  عيل منو بقى بالكويت</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/92472" target="_blank">📅 11:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92471">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇸🇦
🇾🇪
توثيق من نقطة قريبة لمخازن النفط المشتعلة داخل مصفاة أرامكو بالعاصمة السعودية الرياض جراء دكها بالصواريخ والمسيرات الإنقضاضية اليمنية.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/92471" target="_blank">📅 10:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92470">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">النظام السعودي يواصل عملية اخماد الحرائق</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/92470" target="_blank">📅 10:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92469">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
أوبك بلاس تتوصل إلى اتفاق مبدئي للإبقاء على أهداف إنتاج النفط دون تغيير في نوفمبر المقبل.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/92469" target="_blank">📅 10:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92468">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIVsZS-pIkVKWnb08RwWN6A8VzwDItfOIVmhHIouqkOAumKss-U0IkAhXuFdBqAwGUU7xvsCEkdHM9Z-gmE3g-J-dpDIqhBqUsfKNQhOMuqrpqfjWDYg3_hJsPZ5ORVSdq7H09j7o3VuxT8fesje-NQD6QZSdaJs5gRepjVN0nh9aQT4P4YA63SQ5nVeIQrnW_CJDYPm6b8NwaSX_J0JctiMrDii2G7zFuQ9j8DjlUJC2S0hzUMVwz9hpCwdlrPFkBShko7n_ktCuB7TfUAMyOlMaPm5wzJZDUngqm_9PxUZg4bG-eNA0aW7qw0gwz1YsnsLnzcLGDTVIByu0WPoKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇺🇦
إنفجارات وتصاعد أعمدة الدخان في العاصمة الأوكرانية كييف عقب هجوم روسي.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/92468" target="_blank">📅 09:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92467">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa57f09733.mp4?token=rTm7fSzXQm6IaJ-w1poKkDKIflQmcrmPh_ZJYjepmSWcpim7FoyFv7LiuKiCuX_v5ejop_kuI-qgrB-NTffN6eXy9ak4AUa4K_5tkWQmJJLQpTzAAFv11VmFrNICM4FnetjUGwEt7s6INodv1Pt9Gd1a9NcLZHZ6qNn4EyCua-UXR_kzfx3g3VsZ1gaVuavE1uMHk2C1vFx6KlHAbOyHdJ1SZUl6DfOoK8jC-RpVLc0cGi8kKgVhpOiYZbKH2s5qbk3b8SN0gsiZJ2d4rU1xGhf_kzI3yuniVwiFUzBrqQ1qvIMciJowpw_sFjmXzcb63iTnEv6i8ijvK9ro5g0p5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa57f09733.mp4?token=rTm7fSzXQm6IaJ-w1poKkDKIflQmcrmPh_ZJYjepmSWcpim7FoyFv7LiuKiCuX_v5ejop_kuI-qgrB-NTffN6eXy9ak4AUa4K_5tkWQmJJLQpTzAAFv11VmFrNICM4FnetjUGwEt7s6INodv1Pt9Gd1a9NcLZHZ6qNn4EyCua-UXR_kzfx3g3VsZ1gaVuavE1uMHk2C1vFx6KlHAbOyHdJ1SZUl6DfOoK8jC-RpVLc0cGi8kKgVhpOiYZbKH2s5qbk3b8SN0gsiZJ2d4rU1xGhf_kzI3yuniVwiFUzBrqQ1qvIMciJowpw_sFjmXzcb63iTnEv6i8ijvK9ro5g0p5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قاليباف:
الأمريكيون، الذين يتحدثون شيئًا مختلفًا في وسائل الإعلام، قد طرحوا مؤخرًا مقترحات من خلال وسيط. ولكن يجب أن يدركوا أن عصر إضاعة الوقت وإملاء المطالب من جانب واحد قد انتهى. وموقف الجمهورية الإسلامية الإيرانية واضح وثابت تمامًا. ولن يتم فتح مضيق هرمز إلا عندما يتم تحقيق الشروط السبعة التي وضعناها استنادًا إلى اتفاقية إسلام آباد.
بناءً على استراتيجية القوة والعقلانية، نحن لا ننفعِل ولا نُرهَب. نحن نقاتل ونتفاوض في الوقت نفسه. نحن موجودون بكل قوتنا في ساحة المعركة العسكرية وسنواجههم بمفاجآت جديدة، وفي الوقت نفسه، نستخدم أدوات الدبلوماسية لترسيخ تفوقنا في الساحة العسكرية وفرض حقوق الشعب الإيراني. لقد ذكرت مرارًا وتكرارًا أن الفائز في ساحة التفاوض هو من أعد نفسه للحرب.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92467" target="_blank">📅 09:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92466">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
🇮🇷
هزة أرضية بقوة 3.6 ريختر تضرب الحدود الشمالية بين العراق وإيران.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92466" target="_blank">📅 09:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92465">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zy2oJdp_xa36MD4yjLbdSKiM8CS34PAZd_PoFBNHCu8-2LjjTwfabb2U96k-lApsUZ-kJLTO0o2upINflh-bKjXSG1T-vxUiD2bheS2-Z4PN05MrjwZZR5pJPE1pfZ4ytdIiqWmuuaQJU_FnFsjxG2MIQmM563iooLJ1TYr0q_186Z0KfaqHW56nMqYVu_DY_fyJbg9irZnMEOn1j0cwiWWW4sDsSwPbDSAcaTab2oh-GGFPIGsm-qebmo_RFztIlnId2HmATIsZH4VbSUxoLPrDtB8dmBwwDy_8DY6cV9DBOZma6SnGpadYSuZr8D75KZycHkWL7Vcf5VOrJfVl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
النائب الامريكي جو ويلسون ينتفض
😆
:
شوهدت قوات الحشد الشعبي، وهي قسم رسمي من الأجهزة الأمنية للحكومة العراقية، وهي تدنس العلم الأمريكي بدافع عدم الاحترام وتمجيد النظام القاتل في إيران.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/92465" target="_blank">📅 03:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92463">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">▫️
‏الكويت تقرر سحب الجنسية الكويتية من 415 شخصاً وممن اكتسبها معهم عن طريق التبعية
عيل منو بقى بالكويت</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/92463" target="_blank">📅 01:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92462">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQwDGbdw7UAyZVx6DkfU2zTO9bWw9GG1Ow9XOOxP2mfjDPqSDH2z7EybJwkOhygvSJIRvUWq-3qEeUGytk2SciEMgn7nBTfPSI0nE3HahCs471uT0o7XdAWQkIKTEI6P_nTppmmiRSjqrIZy_u-FzeeSBzOF2hUNMmSeDET6ULyzeLdKenWCv4pD4kPrUgqkGsKE5I2fckBgBD747gN8WfZyiiUghgDl222OBSTxoRJfsODWB2GJYsEfPAsn_RSBm1z1_OQmLKrn51p6O7j8iqSLTtr_dCs8Bp3AvSDenqfZ4oVuV8krpJRrVQuekQZ9jgmVt3h2enaOONcpeHkAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرد اليمني وصل،هجوم صاروخي عكسي من اليمن يستهدف السعودية في ينبع واصابة عدد من  المواقع النفطية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/92462" target="_blank">📅 01:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92461">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnKAoEklZ2PyXaFXxNUwv7PEwIU96oNa8VOJLQnBAo1wopxoAJ2fRYTe-McwLciaGHxcPPAraXFKMkRb5Wn9vSX1JTUKDo3f8Fi0dwC-uHM-yIqePcxGKvD8Xf2QT7aWGGmfe8bU3qpy3UfNpBC9h-JO9EGLT2jDYtXFhMaZEFlwJbnSpe5hxYxaJXIX9LyXE9EBg3CM-Il8Kw9M0_BJwyqTMqY1RVZO8giX3KHwQCx2dRCQpREVSv8zQmuZpQnwBEd4WoWNJqZ3kgziP2PkqagDZLbw-dwnGlVNno-QdKJ3dtmwQvcksS0S3LZS0404wJckA93mI0wMuLja6vTttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات اليمنية المسلحة تستهدف الدمام شرق السعودية</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/92461" target="_blank">📅 01:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92460">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">القوات اليمنية المسلحة تستهدف الدمام شرق السعودية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92460" target="_blank">📅 01:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92459">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP9-7RMjFgiQS18uJRlVFZ72ZwDMcC7FatSrTnVBqQ4j0XltGgcpoYXjATzvjz_vQ-oplAFSYSJE4eJY3Q4GLwlSaDDaAU2LxDlso8WzTH_7wQN8HjNsV_ZgJbwj4QbNoTRlDi15PhcytLoAVvjUBD3XzmewApTcJmX0rDt4pw6nUYL31QR48uJectWyOpmDam8J5sf63zHDh7dgWzxoRxUf2Dj3hsfecvaLDx-Xaoxmu8Xj-mcTFnG6NmRxiJbT6CGWvo6-uovM6KuLrvgPLcYDtVBaUCMhYcarupXjtSu23D4yRtyYze-jjLjR2pgQt3rmt-VpUJAYpvd4n5skyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تداول ناشطون على مواقع التواصل الاجتماعي وثيقة تشير بمؤشرات امنية خطرة تخص والد مرشح حقيبة وزارة التخطيط و تؤكد انتماء الأخير لعصابات داعش الارهابية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92459" target="_blank">📅 00:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92458">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇸🇦
🇾🇪
غارات سعودية تستهدف محافظة عمران والعاصمة صنعاء</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92458" target="_blank">📅 00:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92457">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab78e7a2b6.mp4?token=lDNanNd18TVyHx_cccRYzEqU_V4jjuOjWfjs9YNOuiBkRIps-YAMhNN0mqswig79Qi94hm-1aSTASjyRaPz2trOrTFwbBBdZVVNwYRkDzvpHnxrrsyQzJLN-K5sfi-3CgzSrz1Xj7io3l1GG2pewej1xJyyv82phZQDHI3PtwAtXWoRDKqxfEQ5npaBlQT7AmhBEUrwPxb_74V4dzvK2B4Ynl5Ar3wbqj3_e5Q2cpvl-FlJg0ER3KYQp9bU3_-zHiq8_FqQQxWmPAV6ag4RZYTFEEUxLg5gHzLEch-2jlA2o_OjzJkbtQQmobTqb-muUk6NN_6KtUcRR6zRrljn-yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab78e7a2b6.mp4?token=lDNanNd18TVyHx_cccRYzEqU_V4jjuOjWfjs9YNOuiBkRIps-YAMhNN0mqswig79Qi94hm-1aSTASjyRaPz2trOrTFwbBBdZVVNwYRkDzvpHnxrrsyQzJLN-K5sfi-3CgzSrz1Xj7io3l1GG2pewej1xJyyv82phZQDHI3PtwAtXWoRDKqxfEQ5npaBlQT7AmhBEUrwPxb_74V4dzvK2B4Ynl5Ar3wbqj3_e5Q2cpvl-FlJg0ER3KYQp9bU3_-zHiq8_FqQQxWmPAV6ag4RZYTFEEUxLg5gHzLEch-2jlA2o_OjzJkbtQQmobTqb-muUk6NN_6KtUcRR6zRrljn-yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: لدي قرار سأتخذه بشأن إيران. وسنتخذه بالطريقة السهلة أو الصعبة.
‏-لا يمكن لإيران أن تمتلك سلاحاً نووياً. بالمناسبة، كما تعلمون، تخلت إيران فعلياً عن أي خطط لامتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/92457" target="_blank">📅 00:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92456">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇷🇺
🔻
خوفا من مسيرات روسيا
‏تقوم ولاية مكلنبورغ-فوربومرن الألمانية ببناء شبكة للكشف عن الطائرات بدون طيار على طول ساحل بحر البلطيق بأكمله، حيث من المقرر أن توفر مئات أجهزة الاستشعار السلبية بيانات في الوقت الفعلي للسلطات بحلول الربيع</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92456" target="_blank">📅 00:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92455">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92455" target="_blank">📅 23:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92454">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇾🇪
بيان القوات المسلحة اليمنية بشأن تنفيذ عملية عسكرية نوعية استهدفت شركة أرامكو في عاصمة العدو السعودي الرياض وأدت إلى اشتعال النيران في المواقع المستهدفة   بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنيةِ  بسمِ اللهِ الرحمنِ الرحيمِ قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/92454" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92453">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇸🇦
تعليق الدراسة غداً الأحد في جيزان خوفا من هجمات القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92453" target="_blank">📅 23:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92452">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
🇮🇷
الاعلام الاميركي:
طرد دبلوماسيين إيرانيين من الولايات المتحدة بعد تجاهلهما أمر المغادرة.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/92452" target="_blank">📅 23:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92451">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjfoaLyUpULWISLPElz4N1kErVkR4q2YVmqhczat46cUpxnakOycvhO37g8OBDBpnWivvL9oGZ7g93eetME3xoA--rsEb67_DcKPHbf6XohcBtWD70ZWIX1_LcMsfg_pCoRPjBufhKKavBLWWIrKtRv_BGaZWimEUFiCfewdt_qdT3SlgynysTG6l2dunUXcax-VRu_0jr04izHBwJjvi_uCIzz4UyFWtrxPii3UcRPHF3V-GyybtKvQ1tFV_LcFjU1AKF69TiE7jNenbXfQY_Ar30_7o11ImbTUCE5ghVhj4R8JR74F9oOdRC6RWNjFsYU-QERqT8S7-h8cbeduKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني: ‏
اتخذت الحكومة نهجاً جديداً في إدارة هذه الظروف الاستثنائية. تمثلت خطة العدو في الأشهر الأخيرة في قطع شرايين البلاد الحيوية بهدف الضغط على الشعب الإيراني الكريم. وقد ازداد الضغط الاقتصادي، ولكن بفضل الله، وبدعم من الشعب، وبجهود زملائنا في الحكومة، لم نسمح للعدو بتحقيق أهدافه في الحرب الاقتصادية.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/92451" target="_blank">📅 22:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92449">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇾🇪
بيان القوات المسلحة اليمنية بشأن تنفيذ عملية عسكرية نوعية استهدفت شركة أرامكو في عاصمة العدو السعودي الرياض وأدت إلى اشتعال النيران في المواقع المستهدفة
بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنيةِ
بسمِ اللهِ الرحمنِ الرحيمِ
قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ} صدقَ اللهُ العظيم
في إطارِ الردِّ على العدوانِ السعوديِّ على العاصمةِ صنعاءَ والمحافظاتِ الحرةِ والتي بلغت خلال 24 ساعة الماضية 60 غارة جوية وصاروخ ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا 1410 غارة وصاروخ
نفذتِ القواتُ المسلحةُ اليمنيةُ عمليةً عسكريةً نوعيةً وذلك بعددٍ من الصواريخِ الباليستيةِ والطائراتِ المسيرةِ استهدفت شركةَ أرامكو في عاصمةِ العدوِّ السعوديِّ الرياضِ.
​وحققتِ العمليةُ هدفَها بنجاحٍ بفضلِ اللهِ
وكانتِ الإصاباتُ دقيقةً ومباشرةً وأدت إلى اشتعالِ النيرانِ في المواقعِ المستهدفةِ.
​إنَّ سفكَ دماءِ اليمنيينَ بهذا الإجرامِ وبهذه الوحشيةِ يُحَتِّمُ على القواتِ المسلحةِ ومعها كلُّ أحرارِ شعبِنا ضرورةَ اتخاذِ ما يلزمُ من خطواتٍ تصعيديةٍ وإجراءاتٍ رادعةٍ تؤكدُ للجميعِ أنَّ ثمنَ الاستهتارِ بدماءِ شعبِنا المؤمنِ سيكونُ كبيرًا وباهظًا وليدركَ العدوُّ المجرمُ أنَّ الاستمرارَ في سفكِ دماءِ شعبِنا سيكلفُه الكثيرَ.
مستمرونَ في فرضِ معادلةِ الحصارِ بالحصارِ والتصعيدِ بالتصعيدِ واستهدافِ التحشيداتِ التابعةِ للعدوِّ السعوديِّ حتى وقفِ العدوانِ وإنهاءِ الحصارِ عن بلدِنا العزيزِ
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 22 ربيع الثاني 1448هـ
الموافقُ 3 أكتوبر 2026م.
صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/92449" target="_blank">📅 22:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92448">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇶
شركة ناقلات النفط العراقية:
تنفيذ عملية نقل مليوني برميل من النفط الخام العراقي بواسطة ناقلة عملاقة من نوع (VLCC) إلى خارج مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/92448" target="_blank">📅 22:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92447">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">🇮🇶
🇬🇧
العثور على جثة موظف هندي يعمل في شركة النفط البريطانية BP داخل أحد الفنادق في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/92447" target="_blank">📅 21:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92446">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e7e6594e.mp4?token=ct1fUcd3j8in0q-p5vkhKu-frKysX95n6g3Ct4-1hU7B4t-zU2-imV_PQVOS_GSZ73On7ySgTYfAciy3z2z1DcftOTfXEcrh38kXJ9FARsBXuoOQQ8Or33zJX6JXf0BmYAgn9_68BcuBuoyRdqWwMMYFG8XTMvh2V58ETc8IUlmJGJrxgD_MzYGmKx0FFUlEjH6Y27HgMNUeV4FkYtWpIScq0H-6z1XwAtswOjO1P25PCMXOoNj-_tcXMoyY5HRj7QNDMLX_Iwg6BMEDebmeSXdHIbbmuLUmXbzHGkUOvp0FWp_r553u0Fu5RigxXW_SUOSygersYaL8IEIVhcpMAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e7e6594e.mp4?token=ct1fUcd3j8in0q-p5vkhKu-frKysX95n6g3Ct4-1hU7B4t-zU2-imV_PQVOS_GSZ73On7ySgTYfAciy3z2z1DcftOTfXEcrh38kXJ9FARsBXuoOQQ8Or33zJX6JXf0BmYAgn9_68BcuBuoyRdqWwMMYFG8XTMvh2V58ETc8IUlmJGJrxgD_MzYGmKx0FFUlEjH6Y27HgMNUeV4FkYtWpIScq0H-6z1XwAtswOjO1P25PCMXOoNj-_tcXMoyY5HRj7QNDMLX_Iwg6BMEDebmeSXdHIbbmuLUmXbzHGkUOvp0FWp_r553u0Fu5RigxXW_SUOSygersYaL8IEIVhcpMAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
حريق كبير مجهول في حيفا المحتلة بالكيان الصهيوني.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/92446" target="_blank">📅 21:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92445">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1luZTxZT_jVU-hwUuYrlyS-t73PlEUlY01-vexN2H02BmzLDfUME7TVhggeq0HEPaPb7U2jad0sP4TpdFSzpYCWIxEu_b5LhYpVu9j0uvtMOlME8hKnzpIoGnGlCPfMxEsRfamJhDIrYJKTC0XACeqkFTXCfzZFpvpwK8y0TLbrCaPrpxO6r8vPtTXZZiUH3sWbkHkPx0NgSb5TpdPRv6L6ZJmXBvi9XaAbx4IIv_60d6cJi_tmw8PVtFoNBw9Rwb-_IpVPSexDzNxcV-Avi7jjGiL2E4WcF9Mkcr0A2TFcrUHpiROf5oyOUfmZ3PZaL_eCO048hfA_Si8p3A9H4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس منظمة الطيران المدني الايراني: ستأنف رحلات الطيران بين إيران والعراق اعتبارًا من الغد، وذلك من خلال شركات الطيران الإيرانية والعراقية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92445" target="_blank">📅 20:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92444">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
رئيس منظمة الطيران المدني الايراني:
ستأنف رحلات الطيران بين إيران والعراق اعتبارًا من الغد، وذلك من خلال شركات الطيران الإيرانية والعراقية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92444" target="_blank">📅 20:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92443">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 60 غارةً جويةً وصاروخاً استهدف بها الأعيان المدنية في محافظات صنعاء وصعدة وتعز وحجة ومأرب وذلك من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1410 غارات جوية وصواريخ.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/92443" target="_blank">📅 20:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92442">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇬🇧
وزير دفاع بريطانيا:
سندرس الرد المناسب بعد التوصل لاستنتاجات مؤكدة في ما يتعلق بقاعدة فيرفورد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92442" target="_blank">📅 19:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92441">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
انفجار ناقلة نفط ثانية في مضيق هرمز بعد استهدافها بصاروخ من قبل بحرية الحرس ااثوري.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/92441" target="_blank">📅 19:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92440">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇱
مسؤول أمريكي:
إسرائيل حذرت ألمانيا من مخاطر على قواعد أمريكية خاصة قاعدتي سبانغدالم ورامشتاين.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/92440" target="_blank">📅 19:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92439">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇶
رسائل تصل للمواطنين في العراق:
مشتركينا الاعزّاء، نظراً لتوجيهات وزارة الإتصالات، غداَ سيتم قطع خدمة الإنترنت من المصدر مؤقتاً خلال أوقات الإمتحانات الوزارية من الساعة 6:30 صباحاً إلى 7:05 صباحاً، علماً بأن التوجيهات تشمل جميع الشركات المزودة لخدمات الإنترنت.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/92439" target="_blank">📅 18:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92438">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
اشتباکات مسلحة في قضاء كلار ضمن محافظة السليمانية شمالي العراق وإصابة عدة اشخاص كحصيلة اولية</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/92438" target="_blank">📅 18:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92437">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9b9a634d.mp4?token=WFXQ4GStjsWPYAzU_WSYK1bH7QUB4hjXeTIajFpp22JEmQwDfAX-vX86JGQvdilcssUlTn5_fvxwTfm85m9m4PaBLRatxNUzToHyXpXQbXv6YEsa1sVu-3TVPUnKKITF7Z5JDjT4JpOa_YmZf2G7UlvdH2OT3WPb5QKWAQatQtYg9qYTgEewIRWoLGx_H2hht-qvJCuGDsy8nPMFwwq5gGTn8Kr_TRLpVLDrkGDsQBIomjkGx1rdHSGrD_ghSHBoIob2Ke09_3CPqxR57gQB316EL1QXYcCh5GgD0gamlI488G2VPuIHeoQ_e7h1NgTf5cUapT9dDM3rZKE_va2TlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9b9a634d.mp4?token=WFXQ4GStjsWPYAzU_WSYK1bH7QUB4hjXeTIajFpp22JEmQwDfAX-vX86JGQvdilcssUlTn5_fvxwTfm85m9m4PaBLRatxNUzToHyXpXQbXv6YEsa1sVu-3TVPUnKKITF7Z5JDjT4JpOa_YmZf2G7UlvdH2OT3WPb5QKWAQatQtYg9qYTgEewIRWoLGx_H2hht-qvJCuGDsy8nPMFwwq5gGTn8Kr_TRLpVLDrkGDsQBIomjkGx1rdHSGrD_ghSHBoIob2Ke09_3CPqxR57gQB316EL1QXYcCh5GgD0gamlI488G2VPuIHeoQ_e7h1NgTf5cUapT9dDM3rZKE_va2TlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النظام السعودي يبدأ باخماد الحرائق في الرياض الناجمة عن ضربات القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/92437" target="_blank">📅 18:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92436">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce85fd1ad6.mp4?token=JzYVim7GbmwZ94FjsGFLhKs2MvsqZDU8K8bjd1RkF-YNW0-8VeMVMcz_Og3YigdOwoFnCxS00JTWBAEB-h8YqgLYrF30JJqaCNQw53cbrq76b1hlC-hCqxuFy49Egn9Gh1BmojKIEngpH4XBlGT1RDDYxZTi6atjRUw-kgwNqc_fYxDTBzn-8Y4YX9bKGBPK16kUeos4HLBtic0n-AIkiJ8IgLc2HmBf7GcNZj0DcDSJ05uHwRarI5zfznJIl14LwjwcJ3ez4eFpYLlu_tMDQfXaSM-hAT73YvCzhE_GilrO_nxCpvslMVs46vTlm7Wk5ExJgp3iVIVH4IuR3TyRKWRjsE13XCwVVfJxHBUi3jYzSbTeF0b2lqFXo6EPPXuatWa-Qqyo83LUNyb4W0eluqwqAdewmZZAND4t0EQI7cR9fCFvaC33UWp9ZnJ0J_Sw8YTKIt3HL_oHHNGFG2eHNFdjajqHPBSqih2lmR4j0bEk0j49khKIBNeMYMn4quBNVMmtmrSLTISivPaAi88IqB3Pxp4H82e-r08o7NDstO0hL4w61ajqq4-cD_ddWISd8ftU7Y5yhxtF9A4l8sr7w4DUu4dQU5-j3oKFc8h2WTbh6IN10BVrKtWdqhGmktmcA4L4TQIcQpjRwou1lkLTtBAcKmg7rwpKoPjNnbBknGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce85fd1ad6.mp4?token=JzYVim7GbmwZ94FjsGFLhKs2MvsqZDU8K8bjd1RkF-YNW0-8VeMVMcz_Og3YigdOwoFnCxS00JTWBAEB-h8YqgLYrF30JJqaCNQw53cbrq76b1hlC-hCqxuFy49Egn9Gh1BmojKIEngpH4XBlGT1RDDYxZTi6atjRUw-kgwNqc_fYxDTBzn-8Y4YX9bKGBPK16kUeos4HLBtic0n-AIkiJ8IgLc2HmBf7GcNZj0DcDSJ05uHwRarI5zfznJIl14LwjwcJ3ez4eFpYLlu_tMDQfXaSM-hAT73YvCzhE_GilrO_nxCpvslMVs46vTlm7Wk5ExJgp3iVIVH4IuR3TyRKWRjsE13XCwVVfJxHBUi3jYzSbTeF0b2lqFXo6EPPXuatWa-Qqyo83LUNyb4W0eluqwqAdewmZZAND4t0EQI7cR9fCFvaC33UWp9ZnJ0J_Sw8YTKIt3HL_oHHNGFG2eHNFdjajqHPBSqih2lmR4j0bEk0j49khKIBNeMYMn4quBNVMmtmrSLTISivPaAi88IqB3Pxp4H82e-r08o7NDstO0hL4w61ajqq4-cD_ddWISd8ftU7Y5yhxtF9A4l8sr7w4DUu4dQU5-j3oKFc8h2WTbh6IN10BVrKtWdqhGmktmcA4L4TQIcQpjRwou1lkLTtBAcKmg7rwpKoPjNnbBknGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السحب السوداء تغطي العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92436" target="_blank">📅 18:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92435">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/564139a66e.mp4?token=srEXxv_KzMmxLrwwrHloLifvm3lEk2V6xdxstGTVeGA9Q3euvoiqzV6qSwAwu-n4mTqnAzCPi-x-yClZ93fs_q0Eepjd7XuuQpaZ6fBeB0TPYBIGT9Jmzu6ldeokG4_lFpIKZylVjPIiayevedTcjGO-YZ4DOJKjAKCZ8Y8TiD9lxjFIrAhY3kaOixJGRdAddVjZcq5U4Z3NmE8vi3g-R4wkR-KZSrZpxjwuR036BvHutxaxg_2crzHAS34XAddB7-GIuOs3Mzp99a_sn0XIarFpzY121naGFYJ7uuTJS38IrVMvrFq7qwLI1GtxLT59bYQtlXnW9qeihGPmyLoEyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/564139a66e.mp4?token=srEXxv_KzMmxLrwwrHloLifvm3lEk2V6xdxstGTVeGA9Q3euvoiqzV6qSwAwu-n4mTqnAzCPi-x-yClZ93fs_q0Eepjd7XuuQpaZ6fBeB0TPYBIGT9Jmzu6ldeokG4_lFpIKZylVjPIiayevedTcjGO-YZ4DOJKjAKCZ8Y8TiD9lxjFIrAhY3kaOixJGRdAddVjZcq5U4Z3NmE8vi3g-R4wkR-KZSrZpxjwuR036BvHutxaxg_2crzHAS34XAddB7-GIuOs3Mzp99a_sn0XIarFpzY121naGFYJ7uuTJS38IrVMvrFq7qwLI1GtxLT59bYQtlXnW9qeihGPmyLoEyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عودة الاحتجاجات في سوريا بسبب سوء الوضع المعيشي والمتظاهرين يقطعون الطرق لمنع صهاريج النفط من الخروج من دير الزور</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92435" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92434">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7164999ac.mp4?token=WnMiYh4-nutZz12MzMqHtzLr29x-OKH1gSA7ew0b8aYZSx7RMywEFk-aQytDxkByZjX5XOIiLrl7fWxMv4pBmMpMKROVJS19wgrTfaUQMCl12R-foTyarNCAAxx4FueKEjqSbdLpggGrPGTxdE24A8ni8KKrSTXkYfPvl1nQvGRXVcE2NrVim6gSyG5Uk0nOQHsSLx7QS-QBklLSR1jnnwHcOyy7Ry5WW3zOMdJC2Les8sJDemX_PYFxxFxKqXsHFwFVh8I3pmpD_X7a7cillsxaXxbMEkImhkZKcrdt-Zwa8M6vnV_PUsNegi7XONZIpd_KEEWSbAE5aZV2qcTfpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7164999ac.mp4?token=WnMiYh4-nutZz12MzMqHtzLr29x-OKH1gSA7ew0b8aYZSx7RMywEFk-aQytDxkByZjX5XOIiLrl7fWxMv4pBmMpMKROVJS19wgrTfaUQMCl12R-foTyarNCAAxx4FueKEjqSbdLpggGrPGTxdE24A8ni8KKrSTXkYfPvl1nQvGRXVcE2NrVim6gSyG5Uk0nOQHsSLx7QS-QBklLSR1jnnwHcOyy7Ry5WW3zOMdJC2Les8sJDemX_PYFxxFxKqXsHFwFVh8I3pmpD_X7a7cillsxaXxbMEkImhkZKcrdt-Zwa8M6vnV_PUsNegi7XONZIpd_KEEWSbAE5aZV2qcTfpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تدخل منطقة المساحين في مديرية الشمايتين بمحافظة تعز</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92434" target="_blank">📅 17:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92433">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">إصابة شخصين نتيجة عدوان سعودي استهدف قسم الشرطة في مدينة صعدة اليمنية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92433" target="_blank">📅 17:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92432">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzv02zAAXhIOhGjHMgVSUgb4hIv2P-mu8nN2T46VCplLmZmmd6s6-Z4ZJPkuyMbMiPpklAaIe4_lLJ_ptdRfGABlbHYTNJmMOR2ptvlQHCz7gmuQRnWaAds3izAE4NeaRya5uFYthBhW8z1Fp82KZJnK9NXdfh4TBxpEOrmAvCEO7DYBrpHnifJWDCIIn-CFWC0I9VKrfiK2puKsBt8boSHNj1p1TqtbTvShDQqHw5wEMg2OI4uNxM2kivbJYI4vX5GpB_xOpQrtjOdrAH-UqJqvWYKR9PSk0hX746uySuupa5qyx71C4htx44nlwtI9c6cTFmxHkvUBz1hCCV_U_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العاصمة السعودية الرياض تحترق</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92432" target="_blank">📅 16:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567da1e998.mp4?token=AKDf1nfybtGQek9w3ZlSxOoOKV-qa8qcMHPv6sXgqucEheLVcFZ9y3mqEMwpT5FdHjRw0TGzWFmyIV6e1vpXQS75cjckCcvqsIIOSCLwEIEC-NyoIf65D8e98-3PVPe9-lxR_wRdLeke5kx13FFsp-7P7fvom_9RN-rQAGcPUE72nBLgamus_pq_pY9-hSEx0Ul7VFW_H5zAq17LfzwACtaAw-3j8LKlsZ3bF5J9ReHNNO9emHYYhEaH69vBt0tnwkYUEmCJL6_-BZTtOUiHoybrYADJu1XQgVkVCJWUCShlqJDmj26jwl1a8_MGzcR1U2GQAA-43SvN_qlZ5JwWcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567da1e998.mp4?token=AKDf1nfybtGQek9w3ZlSxOoOKV-qa8qcMHPv6sXgqucEheLVcFZ9y3mqEMwpT5FdHjRw0TGzWFmyIV6e1vpXQS75cjckCcvqsIIOSCLwEIEC-NyoIf65D8e98-3PVPe9-lxR_wRdLeke5kx13FFsp-7P7fvom_9RN-rQAGcPUE72nBLgamus_pq_pY9-hSEx0Ul7VFW_H5zAq17LfzwACtaAw-3j8LKlsZ3bF5J9ReHNNO9emHYYhEaH69vBt0tnwkYUEmCJL6_-BZTtOUiHoybrYADJu1XQgVkVCJWUCShlqJDmj26jwl1a8_MGzcR1U2GQAA-43SvN_qlZ5JwWcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منشأت ارامكو تحترق</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92431" target="_blank">📅 16:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92430">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52d0e3bdb.mp4?token=bEW4JcaLMOwk_VTT95cSe0qSdwTShdYAFT1WpqJNVrtxB5gEtQPFjdJbdccSvIKYJ4Fy6-VxArcw5xQ5JEWhL5jDBcZK5lhveKwCxgLb6LKU3R_FpBHDWu7buIjnoLL82gv0AzDD2FzbgcAhBIr1Oc7UtoOPn_8nK-HiwMc6KV0bNgTnm5glPNkOEX-SX7goUDs3rva_koLdaYv1rpX2Rgzf_zItr49szx5K0RpcK9_S0VDmgU3vesBivrcsw-JVLtaFL_OPFzjr7DF6YYJ4S7V-Bu-McB80hgqbZ9GJNOnYQR9ob6Y0wkYCeoG08lx93X9jWgp0gCRMoQRer5YemQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52d0e3bdb.mp4?token=bEW4JcaLMOwk_VTT95cSe0qSdwTShdYAFT1WpqJNVrtxB5gEtQPFjdJbdccSvIKYJ4Fy6-VxArcw5xQ5JEWhL5jDBcZK5lhveKwCxgLb6LKU3R_FpBHDWu7buIjnoLL82gv0AzDD2FzbgcAhBIr1Oc7UtoOPn_8nK-HiwMc6KV0bNgTnm5glPNkOEX-SX7goUDs3rva_koLdaYv1rpX2Rgzf_zItr49szx5K0RpcK9_S0VDmgU3vesBivrcsw-JVLtaFL_OPFzjr7DF6YYJ4S7V-Bu-McB80hgqbZ9GJNOnYQR9ob6Y0wkYCeoG08lx93X9jWgp0gCRMoQRer5YemQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منشأت ارامكو بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92430" target="_blank">📅 16:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92429">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f30f9744.mp4?token=JtnjvVWcVf6B11C9CO4_YNkQzNUoKsk005GGSK4gIo7aVpswilrgZuVkivNJhEEk3Ip6jteCU6XLnI_8ijVeMfPa6k9AXhlJkbFY0Qg3QUKfMDJ_BEoOTh9dpoGZWW48frFSkAs7YhPXlFRfFUg2-nSKkrFtJuO06Xhr9GnMjadb5MpNa2nQD_AFNuKQYlc0hZpVW7etYf9f0UAMaacUa7ikBkKvcv2WnZeUHbPh2xgc_TKSUFKpgZ-8AdQge2Hg1uSvKlUQ2-cy8kkpSZfiiLXXsIwaqC3bPpDfpCtLYSBAjHp1Q6CqqfURQtTKT47MhMDS71LgNO5Fhx0HYi-bzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f30f9744.mp4?token=JtnjvVWcVf6B11C9CO4_YNkQzNUoKsk005GGSK4gIo7aVpswilrgZuVkivNJhEEk3Ip6jteCU6XLnI_8ijVeMfPa6k9AXhlJkbFY0Qg3QUKfMDJ_BEoOTh9dpoGZWW48frFSkAs7YhPXlFRfFUg2-nSKkrFtJuO06Xhr9GnMjadb5MpNa2nQD_AFNuKQYlc0hZpVW7etYf9f0UAMaacUa7ikBkKvcv2WnZeUHbPh2xgc_TKSUFKpgZ-8AdQge2Hg1uSvKlUQ2-cy8kkpSZfiiLXXsIwaqC3bPpDfpCtLYSBAjHp1Q6CqqfURQtTKT47MhMDS71LgNO5Fhx0HYi-bzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من العاصمة السعودية الرياض بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92429" target="_blank">📅 16:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92428">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd6222851.mp4?token=ZY0rz38eA2f4LItL-6V9CHFBAMZw7XpG5UfIde60E-vlvXxB7AAb8T2GlfX0gur2EiK-CVGXuvtTYA2LHzDncnnqMhOsslf_hRZzThLlE1Ir8JkhmNpclvpuUHoGzhJiFEMFp0smMzfAK4ovm2jyehCXGUNU9MTrNAHglBCJxvcEZ1CSx7gTedcEAy7XxJZUes1DaB0aCxaLiN5d23oL0BWqr3U_nij2rvgWB8uU_1q0cDt0Uy9IDY4uOdD1MDsWggPyJIxGD1gTTrTktE2oHvo9bqibgjIbwrmS5uG5FjA8smOaBYOPIoPnluvOzyVLMY5jhDDZtF4--APkQzwSig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd6222851.mp4?token=ZY0rz38eA2f4LItL-6V9CHFBAMZw7XpG5UfIde60E-vlvXxB7AAb8T2GlfX0gur2EiK-CVGXuvtTYA2LHzDncnnqMhOsslf_hRZzThLlE1Ir8JkhmNpclvpuUHoGzhJiFEMFp0smMzfAK4ovm2jyehCXGUNU9MTrNAHglBCJxvcEZ1CSx7gTedcEAy7XxJZUes1DaB0aCxaLiN5d23oL0BWqr3U_nij2rvgWB8uU_1q0cDt0Uy9IDY4uOdD1MDsWggPyJIxGD1gTTrTktE2oHvo9bqibgjIbwrmS5uG5FjA8smOaBYOPIoPnluvOzyVLMY5jhDDZtF4--APkQzwSig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من العاصمة السعودية الرياض بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92428" target="_blank">📅 16:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92426">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3lttzcG0hPtqa0_H_t9wy0lBvNO58xof9UFCK9L-LjDOv8yrdK7U1Q0r7ZCLzECtRVhMpA1VEI9QLAlWex8mWgJcAuFdLE6i4b-CwlTpwJLx9ATjQ2Wb-34uqAkObQlHUEgPJgwHMIUmUEMVqroUDVw6TQJcj5dNQqC27GFz-Jc6PH5ynu9J5CcPNtbeyL5qyYkqrAshq2bCpnlH5wGJ2-gAYqF3QFksJgQ1XJnZ6B-SNy6PEheuXHLPrO6hcV9iJkhor84cbvakcWaoDPBF55f11ukgCd8Woj9Yy0QOefcF-lsN1iLaNAXrKu7oUkEyKODwcB9e5IAG1So7SZong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtPjaKZHrixrae5V54WT9LleLITGn4vSmMQvEwSjBkPvixNyBGCbOaFoQBLRhWUI8xdFRpYhJ6LbQfmE98jjqsTUiZ_E_c9TKUSAxeItwr29k2bI8wngVf8AW3O10cx3-MW1MHVWLkWcpjwp6Sk-63HwPBTv2hMyBizULrJwysbmd0mIhxm2Hk-j42NKDUhP_b1muu9z8w-BuJrVNhdS0JrJ7IMs7560bi_iLkaIiMeSYqdl_LMMgauJLZKBujm1KG2aTu-ntJjWUKicE4LVke1iuuUR3oJ8ZF2FGlp5qzYViog-nAGERXPqtKzZ9ex5i_fQYFbc1z3GHcVHTDZ9kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صور أقمار صناعية جديدة تُظهر اشتعال صهاريج الوقود وخزانات الضغط في مصفاة أرامكو في الرياض عقب ضربات القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92426" target="_blank">📅 16:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92425">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انفجارات جديدة تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92425" target="_blank">📅 16:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92424">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جيش الاحتلال يعلن اصابة 8 جنود امس من لواء المدرعات السابع، بجروح نتيجة حادث سير عملياتي في جنوب لبنان حيث اصطدمت مركبتان ببعضهما بالقرب من بلدة رب ثلاثين ما ادى إلى نقل 6 من الجنود لتلقي العلاج الطبي في أحد المستشفيات وتم إبلاغ عائلاتهم.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92424" target="_blank">📅 16:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92423">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">عضو المكتب السياسي لأنصار الله حزام الأسد: العاصمة بالعاصمة ومن كانت عاصمته من بترول لا يُشعل النار في عواصم الآخرين</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92423" target="_blank">📅 16:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92422">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وزارة الصحة اليمنية: اضرار بمستشفى السبعين للأمومة جراء العدوان السعودي على العاصمة صنعاء</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92422" target="_blank">📅 15:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92421">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIur-6bj819jB_RBOWIWzo3H9LHd4ZwMOy7FsA4vWFHvqh08iXaQ4a_f_Cga1t8rPQyjzoJWCOOtt1sbTkN0x4B0Li6w3G7zcvaV0dmrDNYJVxFLPlECPt0trW6IPrahVbbWyWyFmWttnr-NzdyAJ-36NQvalaH5IocRYsHNiyevWNyDHlO1nOiDS4BAwNArLgmgMAldimaYiHXUpxzw5iwHmWqG2Z7_lDQ6BNZgkeOu95NtisLhQAFvNZjk-vP5fVz2QcFVSt0uMTjBZNNQ_g7qc2ag-FdgeiX9R2K_qY3VdEWgVjFVuGNr9W6SNEOWjInsjYZj7pG9FqTEGgKSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خفر السواحل الأمريكي: اختفاء طائرة إسعاف جوية كانت تقل 6 أشخاص قبالة سواحل مدينة "نانتاكيت" بولاية ماساتشوستس. وعمليات البحث جارية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92421" target="_blank">📅 15:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92420">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">القوات المسلحة اليمنية تتقدم في عدة مديريات في مدينة تعز</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92420" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92419">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اطلاقات صاروخية من العاصمة صنعاء باتجاه الاصول العسكرية والاقتصادية للعدو السعودي</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92419" target="_blank">📅 15:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92418">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇶
🔻
الحشد الشعبي يطيح بعدد من كبار تجار المخدرات الدوليين في منفذ ربيعة الحدودي مع سوريا و
التفاصيل لاحقاً.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92418" target="_blank">📅 15:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92417">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tsgx0p9eRsBLVz1OoTabHdR8M6i2VFZ0HHJ5C9u-CFvTSj3UtbdyMRhD1lULTZGE8LJ-B8mkTQGwddOOO_7TvPYyrSDgHI4g36GUDuacG969VUSik3ONdx5TyF9rOzDlCVuSnlW7Tp-hqOWJ5ogEatSYCZsuK8olIfkebNtQroEroqHbjc04cvEOIzwcuIs7VQpF5cw97L4HFvOZwekRSTVHmrE85E8ZsaHqUdUuf-BRlIoWywBMdwQvC6b8g7BqhZvJPY06UBZMPkgCHGQUc1kErysVUNzM4MVvOWIGXHTDld3tgiNC8yPHplHdVxorBjx8VJno1xucb3h2_qihQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وكالة رويترز: شوهد عمود دخان كبير وألسنة نار بالقرب من منشأة تابعة لشركة أرامكو في الرياض</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/92417" target="_blank">📅 15:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92416">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92416" target="_blank">📅 15:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92415">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ممثل المرجعية الدينية العليا الشيخ عبد المهدي الكربلائي يعلن استعداد العتبة الحسينية المقدسة لتقديم العلاج المجاني للمرضى القادمين من فلسطين وتحمل تكاليف علاجهم ونقلهم</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92415" target="_blank">📅 15:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92414">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وكالة رويترز: شوهد عمود دخان كبير وألسنة نار بالقرب من منشأة تابعة لشركة أرامكو في الرياض</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92414" target="_blank">📅 15:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92413">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a5b43795.mp4?token=SzuT5rjNqTLPqGJQ3Qexn14472gr9mEiZbq-iusjcAt23QtvTYZB-dBO0Cf81n2S4yk9ieWVQ26vJ4Vg6DkkldfQpIBbYfeciPU5-EUsri8T-mT9azgSzu3Cjg38fgILk6HZSdL1ASiDQehhu-MkTalCyKve-DASO_Ozgri49fhGzZoXAQeu0FFczbf6LFj-3wGW2XhIl7xSdXb6JPqOtwjcboMDxjdpQ1UZDqwoE79WalnJxjn4biGkNgRudnmgctgcsZkE1zUjLnLkZgDjG0M88opKSaCpQyAN41c9YdvyQpilzhqg6uJSuWcfK4KQC48SIIVZLKMCksUYJuFieg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a5b43795.mp4?token=SzuT5rjNqTLPqGJQ3Qexn14472gr9mEiZbq-iusjcAt23QtvTYZB-dBO0Cf81n2S4yk9ieWVQ26vJ4Vg6DkkldfQpIBbYfeciPU5-EUsri8T-mT9azgSzu3Cjg38fgILk6HZSdL1ASiDQehhu-MkTalCyKve-DASO_Ozgri49fhGzZoXAQeu0FFczbf6LFj-3wGW2XhIl7xSdXb6JPqOtwjcboMDxjdpQ1UZDqwoE79WalnJxjn4biGkNgRudnmgctgcsZkE1zUjLnLkZgDjG0M88opKSaCpQyAN41c9YdvyQpilzhqg6uJSuWcfK4KQC48SIIVZLKMCksUYJuFieg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
توثيق يظهر إشتعال النيران في موقع نفطي أخر بالعاصمة السعودية الرياض بعد قصف صاروخي عنيف من قبل القوات المسلحة اليمنية صباح اليوم.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92413" target="_blank">📅 14:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92412">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">القوات المسلحة اليمنية تتقدم في عدة مديريات في مدينة تعز</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92412" target="_blank">📅 14:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92411">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f77d1d4ff.mp4?token=da_E1rt1kp9vxxPOD3R8mwJpqPeNWYIkTZqz-8W1n6PgHXpgBnMxJOaZ7tCrZ1XVUyaJHmqX87v-F0cBlCBuROKhHyy1e2IuDjdCkYm4i5_APoGCV_PgDjNXWp3-lVzO4-HWjPGWK2XLqdovWvmM2Ssdfjfus3x3ReHekYIL3wYfYK9Eq2b6QnsocvGj9Zo6hnWiaoCs0haRNot3YqkbZ2N1uzuPCgFTYo_ayoeMRdSfs2U-NS5BRXMymzytogZ3-MDlLNy0fmflpf8OnWNlsIxNktgY7lzs1UOqajaUYjY79s3yU99ZIRvGV6-A4aFbSBZ46UYFYfCCpf8rwulk_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f77d1d4ff.mp4?token=da_E1rt1kp9vxxPOD3R8mwJpqPeNWYIkTZqz-8W1n6PgHXpgBnMxJOaZ7tCrZ1XVUyaJHmqX87v-F0cBlCBuROKhHyy1e2IuDjdCkYm4i5_APoGCV_PgDjNXWp3-lVzO4-HWjPGWK2XLqdovWvmM2Ssdfjfus3x3ReHekYIL3wYfYK9Eq2b6QnsocvGj9Zo6hnWiaoCs0haRNot3YqkbZ2N1uzuPCgFTYo_ayoeMRdSfs2U-NS5BRXMymzytogZ3-MDlLNy0fmflpf8OnWNlsIxNktgY7lzs1UOqajaUYjY79s3yU99ZIRvGV6-A4aFbSBZ46UYFYfCCpf8rwulk_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان السعودي الاجرامي على العاصمة اليمنية الابية صنعاء</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92411" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92410">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba88927483.mp4?token=fOuR_efsi0RFeKYSLi7hn8ISN6PgDlW7fjdrK9-MCxQ-TA9GY8IbcA839wVG-wNS5CxdH9Owc_m6yiMejejIqSG8NIFImqQQ6nTtsHFvVmgOMA7xQJzL_RWnYIWb4EWsNrq1h3lfs_pkVzt3-WUGP3oj4eE2b2NgLtMdS73sy73g3FWV9SBXjTqnG_dE3CEVgxzHXeUhJU33UghAO45x5iN885kj_2pRNY5r6bGTdWfDVGHUyBC82osL3wtG29oFeR2qzL57x3B21nHzsmC57hTPdcmqkfjpzffnDg8Gp9EvOSzFP3EsKI6705d1KsL6vf3n1yLbb45DDL3vTg9VJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba88927483.mp4?token=fOuR_efsi0RFeKYSLi7hn8ISN6PgDlW7fjdrK9-MCxQ-TA9GY8IbcA839wVG-wNS5CxdH9Owc_m6yiMejejIqSG8NIFImqQQ6nTtsHFvVmgOMA7xQJzL_RWnYIWb4EWsNrq1h3lfs_pkVzt3-WUGP3oj4eE2b2NgLtMdS73sy73g3FWV9SBXjTqnG_dE3CEVgxzHXeUhJU33UghAO45x5iN885kj_2pRNY5r6bGTdWfDVGHUyBC82osL3wtG29oFeR2qzL57x3B21nHzsmC57hTPdcmqkfjpzffnDg8Gp9EvOSzFP3EsKI6705d1KsL6vf3n1yLbb45DDL3vTg9VJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان السعودي الاجرامي على العاصمة اليمنية الابية صنعاء</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92410" target="_blank">📅 14:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92408">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wB79sWsSaCp-mFudTxZB6rfFF5x13V2tNTcawSHP15C5VcIhUnOhf4js2toSqe-4E7zJUbKnXzsX2vYe2n0LpRgm0mND6vjA4UeaOvp47Wi2FjjoqyGkH6VYvAFzMMgMF-NHQ3w5yGFQxl3TcEWt5WJpRa524KEDP2KP4Ic__2lg65r6vtv_F-0SogHBat6PdRFBWPKY8b9AvuK4Sly9cdkHmv6bjyQIRbRSgE3dtRjuKPwQPBsev6-O5e6wPFDw1Qn3KVaK7AkgJ1ioOh9G5lifV7uhwf0w4uMlsyTq0XDWlIlTEZA6GKHCppe8kW95nTZGT7gaMgum9MsTnzXPJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0OoEJwE2JIAvDAM0ypm93FT7gqFAocrnwzEr1rEw6soGELnwnbLFq-szJhm5cACqFnoqrR_Mg5QZfPdbTnwoO0A-EiPPdp9j77Er2a1Wv_eqttkPH1RKbGw8_VunJXneLdDr53F9bAaxM2ciIPev0X9CWS7W2K4rCqyPsT7GQc68gmOO2Ntu9mRynovfbbY23sGlPJ2VAGQDMH5r5wVZvghcxCmgE8_dB2qJ-riR8U9ykPaYmtr8DTCCgMDbe_lacAB28DKma0Wwc-opgH4blpgggx-_ohYio_w-0H7dmRPWlQBGGMpC3yC36l7WIQaQ7hejnm-3T44u65WigOQ_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">غارات جديدة على صنعاء</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92408" target="_blank">📅 13:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92407">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">من العدوان على صنعاء</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/92407" target="_blank">📅 13:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92406">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c05eae18.mp4?token=tWyuMDWM5TbPTM5jEEeETfOHarIuNl-VjMcg1dXvQSA7fehdaoyEajpr5ZJzlCXi9kSsoGFtE_MGUE0DYPza5oZO5ZonoK4ceATyfah7SwtY3I7vOUSKQbAmUXy-vMapnnBnCNoGHHKzrDWE88LYg3LbBClMpB5A1qsUJkOhnZMliLxdIualC0A71FLidk96THrHnsxN2NeleJdl8cTUWOWk9vIPp25MAtu6uOemAxNrR34LEXpL9YNihvbbDKXMqaEDd3l1Cw3lrRN0WHBc4En58c2G3Wm3BFY7UUg2inToxojPfc2PlhY_mTZnHEn-KY0QJTVtbWnykoMDSVnNOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c05eae18.mp4?token=tWyuMDWM5TbPTM5jEEeETfOHarIuNl-VjMcg1dXvQSA7fehdaoyEajpr5ZJzlCXi9kSsoGFtE_MGUE0DYPza5oZO5ZonoK4ceATyfah7SwtY3I7vOUSKQbAmUXy-vMapnnBnCNoGHHKzrDWE88LYg3LbBClMpB5A1qsUJkOhnZMliLxdIualC0A71FLidk96THrHnsxN2NeleJdl8cTUWOWk9vIPp25MAtu6uOemAxNrR34LEXpL9YNihvbbDKXMqaEDd3l1Cw3lrRN0WHBc4En58c2G3Wm3BFY7UUg2inToxojPfc2PlhY_mTZnHEn-KY0QJTVtbWnykoMDSVnNOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اكثر من غارة على صنعاء وسط دعوات للهنود في الرياض لشحن هواتفهم والاستعداد</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92406" target="_blank">📅 13:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92405">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaFQMRMjJfg1BE4-ewxILKsNeSrAZL0v7M5FJyMWS-iNWUMFpoVHDQdqo7GV6Duwzi5kxPFz_QGNLCM--XONFqAtqShdWGW38CQvHHQxFxSoCid9Yb-4IZ8iilplsMECsGmpNdiWJVuguK53Ghi7-xlNDjy3gktLEqtkr-fqstNHxLr95qyRV606SRspO7KIoxZS8s_jcWONcWj_9g3yQu2dzp5JgLdD43bPkgR5s314hUqVDf_yDKFkrwy641HCJ4Z4jyD10FXzHqkK-bgC27tL6bkQRHABSkvsvLUKCHqM44LsE5HNk2eo3nhK6KCAJ-i28Q8WP6nU4vwtHmrxYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من صنعاء بعد العدوان السعودي</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/92405" target="_blank">📅 13:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92403">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YeYIsunLJcHNyofWzIm9YABcNCVzDwNr9W4s8wGXXqEgvWsP-q5T83atAHEIJnf3-0k_vfc_dOEJXNRhk6_UpvsBHXFp0TNXjR0DufGZLwwI5awJCHNgmD8Gn6kZ8gXIywGtySbtjsx9o3jXwUnLrQLNEa_ri1NoaTv4SynRPp5QBMhFu1rpedyhuT2pGUW6gi2au5GChbH-SOGXCynxD2tzL48eFyGQJErmiF3v-tvzMzGSv83XhVnT-glsRxbLSwym1on9GxCaaKp3PIDQhLP4N63RXrZq5yolnMvhM2vg_9gPy_63WSUVWcXdEhlnx2EKiFR4l82TrrpEMYjmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RgbLG1b33H-EnknF1CQJ4ln5AIeuc59fC7JFqXViSH8MS83yc3dzdatrClQndAPHbPu1Vikbm-TSxk0f1Eur9lAUcdwtxhDTrxFhoEGVqS1MNB-i6fsZgYwo1drJMkTKkMEe983vBQb6l4X8pQd7-3PiDYgLckt8IbCj3iGgXwk9hyJTQPXsOoqvZH_-ip4bxVzEB7S2o3Dtfityym79WCCPQYp2SjzKLwmgZ1zoD2G0DvtxpqdU64dneWiqNzCIVjWhm9WhgP3KtrgxSzuTK3hMTW0S7KBHNJGRSu0L68_Hle5ReB5MZKlkJbUm9pTk5tZq4NPozX2v26mQgf2B2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من العدوان السعودي على العاصمة صنعاء</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/92403" target="_blank">📅 13:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92402">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_bczVHQ52eVcj5cM-ijsn-2B0ZwEDYQBVP0SNHjsB8_AA_kZYYLXwewPbJtUvUMrEZfLiyaF35YwtDSMs7iEvQQRKqY1l0knxmmNouhPNZfgS5mgk2J_pupgd2feVARrNH_kWn8kT7hNltPyefRWDod2jFboQzEvUOvf8bA6bOv8adN9ady8scJzIHI88h1roynxBpsoss1Rz5q4njJMbnAP0RghTFoqvY3JBHecocOqOrNq7n4BGOi_sf2g3JrGE0OpPw_kEQrEL5JOkos075ZG9D_adNGFmiGF4oavBI5GV5CfklX2TUGQ3BNxr9crDzrf2J0-RFFMpn4ZTTL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/92402" target="_blank">📅 13:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92401">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92401" target="_blank">📅 13:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92400">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تتمكن من أسر عدد من مرتزقة السعودية في جبهات محافظة تعز.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92400" target="_blank">📅 13:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92399">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
وزارة الإستخبارات الإيرانية:
تم تحديد واعتقال أعضاء 4 شبكات منظمة، تتكون من 31 عنصراً من عملاء العدو الأمريكي والصهيوني في مدينة سيرجان بمحافظة كرمان.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/92399" target="_blank">📅 13:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92398">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇸🇦
🇾🇪
انظروا إليها تحترق.. من الحرائق الواسعة وتصاعد أعمدة الدخان في مصفى آرامكو النفطي بالعاصمة السعودية الرياض بعد أن طاله الإستهداف الصاروخي على يد رجال أبوجبريل.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92398" target="_blank">📅 12:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92397">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cad71f6a8.mp4?token=ZNN_4AwatwT73TQNYkpgdBEbP3oTjJXXtcOFdvAqOyrSD-d7DyRHVSglAw7zg0V1Ecuy8IzbeT7NUyYUuYeRvA-RmjbUtsTLKg2l8wMd7nqRngFZg2iKk3D2J826eQL85aEEBzMxyGVbkbx2MEzV_a2v_P9Ya_LUX4ZFDHG-02igKajI8b1wXaFubWQ__MLx8t2yentZCaQ_pk2HFmqIunK_pm--wNCYZRZsTXZ8F0dA8RlT5zUvR8IBElCFK3VTe0445V6B6o6ob3hG-0vVET6-SAA64ZZ6xikFp7haIBKBqZQxfqAVBkJDqyWsJO4MIQQn1X__L-u4wiRKRjAj3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cad71f6a8.mp4?token=ZNN_4AwatwT73TQNYkpgdBEbP3oTjJXXtcOFdvAqOyrSD-d7DyRHVSglAw7zg0V1Ecuy8IzbeT7NUyYUuYeRvA-RmjbUtsTLKg2l8wMd7nqRngFZg2iKk3D2J826eQL85aEEBzMxyGVbkbx2MEzV_a2v_P9Ya_LUX4ZFDHG-02igKajI8b1wXaFubWQ__MLx8t2yentZCaQ_pk2HFmqIunK_pm--wNCYZRZsTXZ8F0dA8RlT5zUvR8IBElCFK3VTe0445V6B6o6ob3hG-0vVET6-SAA64ZZ6xikFp7haIBKBqZQxfqAVBkJDqyWsJO4MIQQn1X__L-u4wiRKRjAj3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
من القصف الصاروخي للقوات المسلحة اليمنية على المصافي والمنشأت النفطية بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92397" target="_blank">📅 12:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92396">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/251473a77d.mp4?token=kU-KYgEAcDGBAusC-Unos6tWEQPUWiNzHWm1U7B3L5shpC_UJH1sLRFBDxQm0sa-rU2ZnSrbX50cZ1Wp-p-tBP4CbExE6RUjV11LmNUWvw_NanShs-eba2pVrO2ueFJqsG_fROpYZwqa_qMM4qIVck7ZlqHc9wZfLBGJXPfZtmxI36DhZRTtHIuTD8kZVDfovaBJ-DVI4Gg2I6AHuJfr7aB7PXc1cBaRmJF3TDfdGD7wzbTDfp4ISyisyUAS8k_Rh2mGOBX0X2AGL0xO2TlyQAhedOEg2IY2sXPLDJIfaMKhhdM17Df9474ablMbGI5ISrvT5VGLc2M0ASf1NkuFrrEcM8WLLRIsr94fjw8cH5lu8bJ2zDvArxvinJo2CxBTHjh_kAhcqCBiPkY1lM6l91562PohahR4E1_ewF83FUrFpsNFaVm8lylXLT9Scrwzaw6XIWQNAo0ImicvDgE83eBia_JnkkOZdOFIp95FWP2qZwKhhwYX51hFaHP_UGLZ2g0h46kJo-BOnp4ObfdTolGLLHwqd2xKDFMt9Ab8NVQOCDacVmZ0lW0chZL8kBhy0i1RnWK7LdUSfdZ6ASjTh4D55OYNizs6QuGwg_6CccdN0ZTtGZYsqIkFYgmpRqK_7Fyp7cq1L5mESOGMY3QvNhR938mX4RJLS_hFjnOy4HE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/251473a77d.mp4?token=kU-KYgEAcDGBAusC-Unos6tWEQPUWiNzHWm1U7B3L5shpC_UJH1sLRFBDxQm0sa-rU2ZnSrbX50cZ1Wp-p-tBP4CbExE6RUjV11LmNUWvw_NanShs-eba2pVrO2ueFJqsG_fROpYZwqa_qMM4qIVck7ZlqHc9wZfLBGJXPfZtmxI36DhZRTtHIuTD8kZVDfovaBJ-DVI4Gg2I6AHuJfr7aB7PXc1cBaRmJF3TDfdGD7wzbTDfp4ISyisyUAS8k_Rh2mGOBX0X2AGL0xO2TlyQAhedOEg2IY2sXPLDJIfaMKhhdM17Df9474ablMbGI5ISrvT5VGLc2M0ASf1NkuFrrEcM8WLLRIsr94fjw8cH5lu8bJ2zDvArxvinJo2CxBTHjh_kAhcqCBiPkY1lM6l91562PohahR4E1_ewF83FUrFpsNFaVm8lylXLT9Scrwzaw6XIWQNAo0ImicvDgE83eBia_JnkkOZdOFIp95FWP2qZwKhhwYX51hFaHP_UGLZ2g0h46kJo-BOnp4ObfdTolGLLHwqd2xKDFMt9Ab8NVQOCDacVmZ0lW0chZL8kBhy0i1RnWK7LdUSfdZ6ASjTh4D55OYNizs6QuGwg_6CccdN0ZTtGZYsqIkFYgmpRqK_7Fyp7cq1L5mESOGMY3QvNhR938mX4RJLS_hFjnOy4HE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
من القصف الصاروخي للقوات المسلحة اليمنية على المصافي والمنشأت النفطية بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92396" target="_blank">📅 12:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92394">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965605401f.mp4?token=agOkTB2qiq5reMC32zMefOnESodNMeEd9-qROIr_Dn443MqQcanJSWlKQlR8VAWC4RyY7oSIXBkTtR_OCHR5gxz5PuwwupfmMmcIxJe3UlN4O9DNjCBYn4kv5mxrrE6Dd6kYejxvC_RyTLXylzATEim04-XpFW2cM4u80MCb_IJSllVim-wLrTByROt42Cd67rldQUR27T2XQWjTBcg8f-7wjQUTHN2p2cOUfiK3prz03iFrrgWH0C2rTFKsoKbCaIj6Bb55J8WrSNBmk_-DaMenXA0J5ElYNs-nf5BBmslVT0ZryFwAWbd3Sa5BuKfR2C0GxKchmCWGPZ7kc00YPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965605401f.mp4?token=agOkTB2qiq5reMC32zMefOnESodNMeEd9-qROIr_Dn443MqQcanJSWlKQlR8VAWC4RyY7oSIXBkTtR_OCHR5gxz5PuwwupfmMmcIxJe3UlN4O9DNjCBYn4kv5mxrrE6Dd6kYejxvC_RyTLXylzATEim04-XpFW2cM4u80MCb_IJSllVim-wLrTByROt42Cd67rldQUR27T2XQWjTBcg8f-7wjQUTHN2p2cOUfiK3prz03iFrrgWH0C2rTFKsoKbCaIj6Bb55J8WrSNBmk_-DaMenXA0J5ElYNs-nf5BBmslVT0ZryFwAWbd3Sa5BuKfR2C0GxKchmCWGPZ7kc00YPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مصفاة النفط التابعة لشركة آرامكو بالعاصمة السعودية الرياض تحترق بنيران صواريخ أبناء اليمن.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92394" target="_blank">📅 12:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92393">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇱
إعلام العدو:
فشل محاولة اغتيال علي العامودي خليفة السنوار المحتمل في غزة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92393" target="_blank">📅 12:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92392">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a76c3a62fc.mp4?token=pbSfbS4gRR0XQ_7jyPtSRnwNbjhODO3QOhtrL8McAQm44snqH1rLKn1xQSkqZIAANJ8WiFK3ocglKiufO1yuPOAUEE5u30SDRxcFscIvpcrUSY0YMUpGFdbrzGY-hQW3bUcaOFRFwatyDKD8byo0L2etopN1nU2Aw3E1FFQlFXe9Oo_UIyfVzI2E_Pd1sVz1t1m-5c__HemDxd3QqblSeJfh2-pSmelpwxmPbjFCcBZPubL_YVVkdawdAoKEDT0G_MppW2heeGRSgM42iKqyUahpMBaM8JH4ZSHB-GU1HMLSUzfLtkynyG25HtT7r8SKpkq0mDTcw1cef1iZag90aDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a76c3a62fc.mp4?token=pbSfbS4gRR0XQ_7jyPtSRnwNbjhODO3QOhtrL8McAQm44snqH1rLKn1xQSkqZIAANJ8WiFK3ocglKiufO1yuPOAUEE5u30SDRxcFscIvpcrUSY0YMUpGFdbrzGY-hQW3bUcaOFRFwatyDKD8byo0L2etopN1nU2Aw3E1FFQlFXe9Oo_UIyfVzI2E_Pd1sVz1t1m-5c__HemDxd3QqblSeJfh2-pSmelpwxmPbjFCcBZPubL_YVVkdawdAoKEDT0G_MppW2heeGRSgM42iKqyUahpMBaM8JH4ZSHB-GU1HMLSUzfLtkynyG25HtT7r8SKpkq0mDTcw1cef1iZag90aDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مصافي النفط في العاصمة السعودية الرياض تشهد تصاعد كثيف للدخان جراء الهجمات الصاروخية والطيران الإنقضاضي اليمني.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92392" target="_blank">📅 11:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92391">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcb6959801.mp4?token=t5VDkVWrfQp0ORQgb74h0KJqLp2Ps6eBtmwu6wwvNaPQ8SARONonRvTWobVoJVBeTh4Ga60jglbiYHt-cr5XueXiCXR_F66MbR-7cLPN-vDU_B4DfaJ25QTGOyhBPBw4XWiJ5lbAFvke9qQOubbTEWqwPuj5iYjYhAXBcqHZ4YScEVDaG6SA9SSrYa3IfhbZg-C-EUUbM-BRN6ymv7wq7vuoXx-m3JHZQuUYTXTm5tPSTzebaW_Tv3dPCUiowo7Kk0wUXUqerIUidMVSHEYYCwahBR8bsdk4hOUQ8T753dH2SXfwma85rEUPOCyrxbPCVWr9yWXcXhGuKKer5a6hdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcb6959801.mp4?token=t5VDkVWrfQp0ORQgb74h0KJqLp2Ps6eBtmwu6wwvNaPQ8SARONonRvTWobVoJVBeTh4Ga60jglbiYHt-cr5XueXiCXR_F66MbR-7cLPN-vDU_B4DfaJ25QTGOyhBPBw4XWiJ5lbAFvke9qQOubbTEWqwPuj5iYjYhAXBcqHZ4YScEVDaG6SA9SSrYa3IfhbZg-C-EUUbM-BRN6ymv7wq7vuoXx-m3JHZQuUYTXTm5tPSTzebaW_Tv3dPCUiowo7Kk0wUXUqerIUidMVSHEYYCwahBR8bsdk4hOUQ8T753dH2SXfwma85rEUPOCyrxbPCVWr9yWXcXhGuKKer5a6hdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد تظهر دك مصافي النفط التابعة لشركة آرامكو في العاصمة السعودية الرياض من قبل رجال أبوجبريل، واعمدة الدخان تتصاعد من عدة نقاط.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92391" target="_blank">📅 11:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92389">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwmYs6ShKTQVHLm09Or1DJaXeBVvLLQbyyVf37_9i3zOIQNDQbByifenyA2_lHnpwJGr8NaN_KIm5e2lTkYvg85gXoD0Aux5QQ33u-hvc9ETYsNUn_-Dae5O2vhI14PnD298ljNyknzyIzxuNKj6w_8ubcO8mNc_PyUrhTjJTbrW3GepQ637eG7RRw64dEZeGceaL4IHawtPFHlr5_VHSYsSD_LZDnqceFiHRgGuc4YPsmKi3oVCtFnyjImQYelH4Cdn67aC7qWE06uj7leoVJ9HISDdCUwb5b-bp6tkh73QWbWTek5QCXiBsYxx28X_43IRa6YwkYSPtCSVzi7wdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VA7fRYlVMg6EOwisCZecclS6HhAOA1l-w4P4UYouj0qGveYppVEaabUX9tNZXTRMaEXe1Vm4scKGh6MPjdcM7D_WSYqNWb4tVDNHzuV9dbGEozVhYKQ2MwCDcWxlORBNt6dwBibxJ22dk5QHWfabhN89uYdhT_YRP3ox3warxcteTaLmR0ljRwDMT-s-Ew7SRhnWrwGgk4xB8wYlFg6YOFVyxcHCTVu68LtywWD8TLPz0ax4Az-eGEXw89wSLMvSMoUGQh91xuYx-ybpCWcW8OI64D-oqpEcQQROPSnFP5UB8taPR40P7tL6SKxaxt2XVTiVbDaIwX89x8jjeNdOkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
سقوط طائرة استطلاع مسيرة من طراز "MQ-4C Triton" تابعة للبحرية الأمريكية على ضفة النهر في قاعدة "مايبورت" البحرية بولاية فلوريدا.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92389" target="_blank">📅 11:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92388">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔻
السلطات الليتوانية: إغلاق مطار فيلنيوس وإقلاع طائرات للنيتو بعد رصد مسيرة قادمة من بيلاروسيا.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92388" target="_blank">📅 11:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92387">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي في الرياض.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92387" target="_blank">📅 11:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92386">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiKcMkKmh748Xk9IuMpZDl8oKnaLZyMTZ1-JNg4LwZAVxOTD7k01Rd1Yf2tvaRNdQFiDvoQLUUNIidqEu_1qIf-gwZi2mnvh3wwvn_k1Nz6PN00zbzamzFJC09MzM543zokhjM0_wFDgyFX0ZUHcx8Ud77fYpaxy44Wik7inrJsNtGB9eRcuSRzyGrFIcUPVY037FgPV6tpwCTEubJWLhM-RYl61VpNbJmg3OloCMWotdfHC8ui_spe4t9itEI6x3JjazWn-2qtzf-WSmqGvSok4VmUte9OhieXTkgrhZgu6YmmvpdxjzEKbpyFH3-ZIQe_t6UvXpiqpqHJQnmasBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صواريخ تنطلق من صنعاء نحو المواقع السعودية</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92386" target="_blank">📅 11:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92385">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTTTHdRl4Orc7T1n12VTX6ybTZAP74yUGK-VB9ZIs98XQOXbwRBLqXVcpwzpBqVdb_kfIkymjDDWTjsu3k1JJDAju2VezzdQpHh-m2y70U5elCTCNHfyKYvuGaAicFqNmGTOW7Vx1RJdGu_RnQC6nXuIgOftWmNGR8j21PVuxutUjlG94jO7kFBVZPPqtMOfqgT-EmFLypC2p8fizOcTXIENAXCn0EJWKojUWf59QkgNZLpjsEb-JPOrZzQ-_Ug4a0m_V8B3Cm5OjcFf0qnXxsywoLKvX72HYErzsVEIylPECnXskuibX7AZyJ84SzmasN-q2i2pxwJL97HrxxOmBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية بمطار الملك فهد في الدمام.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92385" target="_blank">📅 10:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92384">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔻
السلطات الليتوانية:
إغلاق مطار فيلنيوس وإقلاع طائرات للنيتو بعد رصد مسيرة قادمة من بيلاروسيا.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/92384" target="_blank">📅 10:37 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
