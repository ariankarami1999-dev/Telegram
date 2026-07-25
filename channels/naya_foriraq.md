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
<img src="https://cdn4.telesco.pe/file/cMcLCylQfKn3wVhgZKWTT3O_6Y5dbccK-QbJcHGKrx8XzDJlotY_IPzgvuyHLKG-ibIqktn7BtkLStd9ycuYfJX5J4SSoWfTh-oGL9eZUkeEwznD3YFu5lQ_u8Bl8jLa3Lt7zOsnv86xJa_LuR83k2G1gkWOaGZRTY6X_EqR8pafM9ogkTlqnq56m-HQUXdVkvS674kptBsOp4sfJnG294_EOZS6KDaYmp47ycXTC5C5JnLmcyqwtGRYuEOESXkIlCOmh0ii7chepaToYevTFK4XBUymk3NmiggLLBF_g5WSvPuTC_vNnEnbezaAxHeyEBHaSiJQNpK3CDtrZjvqcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 11:01:25</div>
<hr>

<div class="tg-post" id="msg-85510">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
🇺🇸
لاول مرة منذ 13 ليلة   لم تهاجم قيادة العمليات الأمريكية الوسطى ايران ولم تنشر اي بيان !</div>
<div class="tg-footer">👁️ 709 · <a href="https://t.me/naya_foriraq/85510" target="_blank">📅 10:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85509">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">📰
بلومبرج: السعودية تحاول ايجاد حل بديل إذا اغلق أنصار الله باب المندب
سيكون تصميم طريق بديل جديد يتجنب مضيق باب المندب في الطرف الجنوبي من البحر الأحمر مهمة شاقة. سيتطلب ذلك استخدام خط أنابيب إضافي واحد، وربما اثنين، وعدد كبير من ناقلات النفط، وجرعة جيدة من دبلوماسية الشرق الأوسط السرية للحفاظ على سير كل شيء على الرغم من تهديد الصواريخ والطائرات بدون طيار. لن يكون الأمر سهلاً - أو رخيصًا</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/naya_foriraq/85509" target="_blank">📅 10:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85508">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇬🇷
القوات المسلحة اليونانية تدعي: بطارية دفاع جوي يونانية من طراز "باتريوت" تم نشرها في المملكة العربية السعودية اعترضت ودمرت صاروخين باليستيين أُطلقا من اليمن واستهدفا مصفاة نفطية رئيسية في منطقة ينبع</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/naya_foriraq/85508" target="_blank">📅 10:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85507">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇾🇪
بيان مهم للقوات المسلحة اليمنية في تمام الساعة الثالثة عصراً، للإعلان عن عمليات عسكرية نوعية وواسعة.</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/naya_foriraq/85507" target="_blank">📅 10:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85505">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PipGTHeJWNjQfNM0mkhGif0Rz1zhTmP6NmZ7EsDSS372zYDA6IfK2MwYjmGa_lXSVzQdg7XtFvMrhzdrKdPtpMVXbuZQabUMpKxH-5ECS9Tc5T0frOyuSUjzPcKWexKhTz_tICDz5JR02SOX9HUjiWqcPM7fSuMHl3rkw91J7wBlUlqRHFTOb-77IEE49tklWw2sE3LrWiO5Cd9tHDH0Wsb6-KodL6fRHdHNfcIT3LdysZLsQGMtFFBTuAxyLBAc6kUYt0EhWZFI_gF_3Mb6afG1iKNOzjQcc9VVpKb7M-wFBRmmEEYuI9ebjtUE7KbltUltHnwAjdUO-mi8WdOR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBNrvUipUKHjrdsc6mJs8KlwCRmA0lT9MbykDdmaxjG7D8Lyyi8wepHwcz1h1AdtZE9u0q2rQsLBWcv_ouZIy8i3q7P9Cuk9252BqxxFQgAGqcZBKQIc0GAgRsSbtMBYJnlixSmoWQcA_bIYCf4EBEspUdRu9fMDlzUXhhSfYrzWncnghnLUduCVICURvjaH139OXn823bJzdMoQ7mqReoxhIqjLxhNZ1u0ciUmNG2ucwZIf-XgmmT63kZmNeBRnpCvkh5PXfBGjJ_KjsrELVLVM4JUNiHHKOF0161LRjjanNla1ZHzNAn-eGYZ6FhQhLXOZyfvRpJDJHsvjnAzLvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صور الأقمار الصناعية من ناسا تؤكد اندلاع حريق في مصافي مدينة جيزان السعودية نتيجة هجمات أنصار الله في اليمن</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/naya_foriraq/85505" target="_blank">📅 10:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85504">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFVQtQHSafITCjpaz4QVwoqNWWzLAarbDkEOcXIf609i_1xu98sh0HthwYgl1mIHDDogod3OKxzZsYJWG_4fV6jtULt4RTjYsZTuyGGnzu1sAdEKgTCBp_vORNoD4261XBNpjlXF0UwypK21KYE4DRo6n8JZZjTU44EmJ6oAJdgztcXoCuhBS6jNi2msvckAxaJluq6gj-vPbI0vHNlRcaL7T8JkOflXIkBMUBaJTSaAwIVVCUB5O2xR1KdH9qmSV6hTo5TjG-k08mnIazxxQ6J8OyJkmYvEJCvsJTjtPjrH2nZGCmh_buaBTjzbPwOigWL2roFSRTnIQr6VLA4b0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأقمار الصناعية توضح اشتعال النيران في خليج فارس وعلى مايبدو استهداف سفينة مخالفة من قبل الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85504" target="_blank">📅 08:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85503">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86224dabce.mp4?token=JM91oOZ1c2_ygHOZLvt5_oNk-EcvPC2kexLvbX_KoSEwA2Gz42bVLnEfftJ18upSRMV5aKRSKymL966q8VwMcUuPGDIOLKKLGp57c3v13QVLWDyEexf3byBg-8nE54jrLxy6j1QiNeeAiaBZeDlygEyO0LdsbNvsQ2nWTUVGrPD5rBwh1hKWbd5k51C2kkCKoXGZslZHwCKag76fXbEZIAps6dF-k2eBuoSXZhSZinF2vNvz8PIfTtx8mfoga7uDOfqRzFTfhNKFdQInnd9r6Pgud8xb3nnA6bcAu4u7xv-IsQ1o-O2QwkHxpyR0wevCTk0tK5GRO0neO-waQY1BZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86224dabce.mp4?token=JM91oOZ1c2_ygHOZLvt5_oNk-EcvPC2kexLvbX_KoSEwA2Gz42bVLnEfftJ18upSRMV5aKRSKymL966q8VwMcUuPGDIOLKKLGp57c3v13QVLWDyEexf3byBg-8nE54jrLxy6j1QiNeeAiaBZeDlygEyO0LdsbNvsQ2nWTUVGrPD5rBwh1hKWbd5k51C2kkCKoXGZslZHwCKag76fXbEZIAps6dF-k2eBuoSXZhSZinF2vNvz8PIfTtx8mfoga7uDOfqRzFTfhNKFdQInnd9r6Pgud8xb3nnA6bcAu4u7xv-IsQ1o-O2QwkHxpyR0wevCTk0tK5GRO0neO-waQY1BZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏لا تزال أعمدة النيران تتصاعد بكثافة من المواقع المستهدفة في جازان السعودية</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/85503" target="_blank">📅 08:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85502">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoyksrCzUPGZLnENRIah3wdQUgBwqrj1Ik2oiOLAUS31AylUXK4LsRubS7vsGg6j6QG8pOE1hjn5XhQYM6rZXPP0gFI8DM6Opi3oBROjP7fto5LIgbrF6QmHFmFRC7DrXw7Zb2D7xa73jtK9fuaZNlFITSeqmnpOl_b-RAW5XzOYu9ZnjDtsiouBkuWlLLUSaU_jOoyEW9PcHZ-VFqSGUJpPSRMLVskrzL2TAbnygyA1Ufx2VZiSvnFB7e-rdfKb3wQ_HtVk2fo7jvk0lDPUAyCFrDTno3rVTxJMSbS7l4fOGg7bg8X2yS26MTsM_4x96smR3xlTNSgL_8_3ZsIxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السعوديون يتسببون بازدحام خانق يشل الحركة على محطات الوقود بعد القصف اليمني الأخير على السعودية خشيةً من تفاقم الأوضاع واستمرار القصف.
عبي عبي يا طويل العمر
😂</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/85502" target="_blank">📅 08:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85501">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e9e30099f.mp4?token=uhsy1ys-UM0KwO5vqellOFgUUlZhyhNtSxl_jjn9p6VjiMGLX3JtT4kBo-v7JflYpvZuszFmk1UWZ2USApXX2jEy59iE_DRNkHVUs4jVdwMJTEUZxaOmDG-0mvSPxGwlITad1XLRF-1zaKVhkMRxGCgMvlGqgoFeTfTSBfX-XXgYaHiPDzUhIMSbawvriG_VUW0i021BDccg6zCFOm2IL6sp4eLpFhsPHr2CQeramMceFsWH2-ql8VAEKtpE10WkaBtC0BTuBSuuFyt6C4ZsgwdOCYp3EXvZhEYGuIPZyyfzysJp0I-zFzENk35-YAfTK0762gaiOhI_YORAHeVFlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e9e30099f.mp4?token=uhsy1ys-UM0KwO5vqellOFgUUlZhyhNtSxl_jjn9p6VjiMGLX3JtT4kBo-v7JflYpvZuszFmk1UWZ2USApXX2jEy59iE_DRNkHVUs4jVdwMJTEUZxaOmDG-0mvSPxGwlITad1XLRF-1zaKVhkMRxGCgMvlGqgoFeTfTSBfX-XXgYaHiPDzUhIMSbawvriG_VUW0i021BDccg6zCFOm2IL6sp4eLpFhsPHr2CQeramMceFsWH2-ql8VAEKtpE10WkaBtC0BTuBSuuFyt6C4ZsgwdOCYp3EXvZhEYGuIPZyyfzysJp0I-zFzENk35-YAfTK0762gaiOhI_YORAHeVFlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من انطلاق الصواريخ اليمنية باتجاه السعودية</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/85501" target="_blank">📅 08:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85500">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مطاري الأمير عبد المحسن عبد العزيز  و مطار عبد الله بن عبد العزيز في جازان وينبع يتوقف عن العمل موقتا نتيجة الهجمات اليمنية</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85500" target="_blank">📅 07:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85499">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">Guys in CENTCOM  Where is U.S. Concludes 14th Night of Strikes on Iranian , it’s to late ,
😆
don’t forget to write we destroyed the Iranian navy that we  already destroyed them 2 months ago</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/85499" target="_blank">📅 07:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85498">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghn7Wpm3WL3KCbr17TLKEnloZSd4Izf1tHD-KRHo78neA9fKWDh-dS9erd5je6K35kYC2GLXS8PinYwAZAA_DfmcBxLx9Bq03dT9zPEUypckobcB-hOQLAohgkjZo3nCiGKllL8_iu1aBgtwNuCTrGNxbL3Gcb--V7prcA_kaImxBQlc0_HCadin6XiKD28NwAqfAQZhDdlw0qS1tTF4f8e2hfPMPTXD0eOb2YvJi-GaqDIGgEV3zqN8EhfAIlJKgetfuSrvcYK0X-Keq40TDa3KFgJSK097ePXonhu9PFL6CbrjdTuwZC0xK9JQ7_YKZr5B2kwEkGIUO2IVf4J6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من مدينة جيزان السعودية</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/85498" target="_blank">📅 07:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85497">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هجوم على ينبع بالسعودية</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/85497" target="_blank">📅 07:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85496">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/85496" target="_blank">📅 07:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85495">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e105faa0e.mp4?token=N0L-YfhgoXmeZfQrWEiqUTysR6XSoJwhadsHBfxw0twXo6_WLY_KRIXqdPSysHS-IZDlr85T9jtOmrZSo3IEq3N1tqCioAoRJlKToI0g257qOQkFLqHqNmbdSz907CqFwejZ6SfY1ewUGED97JZSDON3IBu7m25VaBp6lvPINggNZIeTN-LdkbsDHNvaEDmrqk9UhHBDMSgK7GTvDqWV6yO6vYFIiWrH0cfNFJIRbhL8SYTQf3Q4UDQ4H3YHtoWmOm3hBgDA5KquhKeVSr3cIpqCwiQdGQsKvH9DUjjgxzrH6E1y0oKuK7oNG6Gjfi8kRfgrOWcKpgpISI6A0HNXDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e105faa0e.mp4?token=N0L-YfhgoXmeZfQrWEiqUTysR6XSoJwhadsHBfxw0twXo6_WLY_KRIXqdPSysHS-IZDlr85T9jtOmrZSo3IEq3N1tqCioAoRJlKToI0g257qOQkFLqHqNmbdSz907CqFwejZ6SfY1ewUGED97JZSDON3IBu7m25VaBp6lvPINggNZIeTN-LdkbsDHNvaEDmrqk9UhHBDMSgK7GTvDqWV6yO6vYFIiWrH0cfNFJIRbhL8SYTQf3Q4UDQ4H3YHtoWmOm3hBgDA5KquhKeVSr3cIpqCwiQdGQsKvH9DUjjgxzrH6E1y0oKuK7oNG6Gjfi8kRfgrOWcKpgpISI6A0HNXDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جازان السعودية تحترق نتيجة هجمات أنصار الله في اليمن</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/85495" target="_blank">📅 07:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85493">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b3d6745d.mp4?token=TYJX_Zj1vOW1iRoMTZrX1B210co-9XUQmvfJ39VEvYFOWaOk0lVe_MiupctMnRj7EOeLoT0QRxodekl3MbAf941iIXEueQhALATMG71fBt0j47k19uAuHO6pm2Ou7gnnAZeN70V0-6OumzujcMpIwKQXuclvNG9rT6vHIu575aHQ2zGq1_buejkKfi7DeryqwPkC-xKEdlWwALUPob6eQzQTBgXVKueNQ-6tvFLNZ5dVMOYX5gOUyxGNYE07ea9IX16z0aLsoVdtAK3CF_qjwlIcEPhg82NZX9zy7DB39QybVtmqhTWGYRoltNnMeN0nvy07j_5awFulofr-8VBNGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b3d6745d.mp4?token=TYJX_Zj1vOW1iRoMTZrX1B210co-9XUQmvfJ39VEvYFOWaOk0lVe_MiupctMnRj7EOeLoT0QRxodekl3MbAf941iIXEueQhALATMG71fBt0j47k19uAuHO6pm2Ou7gnnAZeN70V0-6OumzujcMpIwKQXuclvNG9rT6vHIu575aHQ2zGq1_buejkKfi7DeryqwPkC-xKEdlWwALUPob6eQzQTBgXVKueNQ-6tvFLNZ5dVMOYX5gOUyxGNYE07ea9IX16z0aLsoVdtAK3CF_qjwlIcEPhg82NZX9zy7DB39QybVtmqhTWGYRoltNnMeN0nvy07j_5awFulofr-8VBNGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جازان السعودية تحترق نتيجة هجمات أنصار الله في اليمن</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/85493" target="_blank">📅 07:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85490">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lu1_OSVWRy6e53KDlPWYbaV_GeCHKf_B886GCG2jhTWjZOovNmlLUEkiI5rAroQU9vc9fc9lFH2v6R21JLwikdKD6g16eRVE4SXFyilcMHXOYC5yeqPwBAMdMEuOJ3SlzzDVvVutr7hKeyrMsNmACCBKRhRGhr4Hsdap5Y82xJyWc1uApTShwB0-nt0vIpU1QtbrbPy2GcM1x8bE6jbltMayV9EJNDGotOAQw7QBgkkPrDIkUUV-VqBktAkDZP1STm5voe0vcO0sfOdSNAYyZAoxxjHve6Ha5vXb7uKdvcKcPOVy1eXnh9-VGbdxvWFenM_6axUu1sKvpsJ48AkFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من مدينة جيزان السعودية</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/85490" target="_blank">📅 07:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85489">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq3obwWYv3JXW9RKuLErwM0yShDBWRQpl1UCe6kGNCaPcbOOXZ8QGn4tCYoxAT-zzyPOh6ElrPR_R0Hr4gZxZMhJKF9m6MBaxNQ4UtIapLiC_mNfStqkb5tChF4zGtPyMZu4zqHi4hy8MNKWqRDqlel43jTIqVw9nkWKEgNGADC0u2j1UTBOxug5dzIeQ7_GuIfiRE5XMesM5E74oShcg5-DjAf8CeZIlxQVuBq1aBuGmn3YwMzK9wq-m1NRDzBta36Yby5bV-eia4pfSPV5GLXY4YY6WzLfQF58cohJTh9cZS5C7UCk-eaLMtckGzlL10U-6UKea2pXKzJ1xnT6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد فشل المنظومات الدفاعية في السعودية تركي ال الشيخ يلتجئ إلى الدعاء.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/85489" target="_blank">📅 07:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85488">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etp-B7Ox-YahCaPViXnU2LgXpepb-sd4XUf9kGifZILbNT_6A3JzF41QwCvSqCrPxmBUDRbWHLGcqOYsgUSDanWtzLKEFrK0kTiH7pPBEsFW0VpAAuEoP67CFuCtaNDkAFyrNeRqSK22lEfxfl_ka5Ot6BcAwc8m3UppLbUsKhyF2dSnT23rHHSCoFz8rdbLLu8sr1lfQjQOW1NGiUjEG5A50i64AHpBCzSDL-KZLINmpEviibVX-2J9beQJpVNrU_81LLLer-_BvKaB3ALIqbZysPTzdceYvbsQ10ffHmoKUc2oUzkbwXK9UfytDhQVKdlPMy6WrGLY68TrD9SwBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الموجة الصاروخية الأخيرة التي استهدفت محافظة ينبع السعودية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/85488" target="_blank">📅 07:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85487">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktlrhgi0v4k_ocsb0YSFGiLj5XKSAm2jW_GWQhCl0eiKNAN1CZ1R3X4MeZwH14zv6PBjHKYugOz6ng2r5T5mVvdrdc5gyPqAPXJpck-mPbsFJStmRNH1GSjAIj1qdqVyThf3u_-IoIiprKEagx_g5LGsjPfDKWpbcxBJDB2wIaluh5_xoSqv9WImzwu29vVWwbpdaoU569QiBl071LkjVT7U-tOTfJDGsfiN3UmzeDlUJRDb6b4HcIt_qTUeNXqTUQCTYo3niAFShX_4z-zU_D6IYFSbiUPh9IcyUA83OcEhdt75m88GzzKdItIz2dapSwfL2TVykZe_fBoyykZp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ اليمنية تصل إلى ينبع</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/85487" target="_blank">📅 06:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85486">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWPlk4QD64N9S7OKy30qM-9L5BIq3_4Cmd_yIfKp3ZihRTsZ5Cn5sUb9foT1j-IBGIOoETFqhNMCUtnSHIQ_P7TkqdYP5CQZ12YgOzjiTO6iyxkSZ1R_46SWQLorHcFlfbwbzUE-fJkh5geGZMwgYpBjst_SsSeQR0qmbFWZ5r6cx-eUQjX-6eAcdmJ2KGgQMqIo20XkydwKZah3m96smhdENRZZTdUtsLoV9p0iH8Kq9Y8pI8e1Gv840mDmQ4qMDBB1rPBIBi8CERINSRmfYPk5hfY1e5RwiM2dPgh1nrzA4nEbq1Sy2S5TLDJJCLz9pFodlNEBacMXHs_5D4SjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطاري جدة والرياض يعلقان رحلاتهم الجوية بعد الهجوم اليمني على السعودية</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85486" target="_blank">📅 06:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85485">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انفجارات تهز خميس مشيط بالسعودية</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/85485" target="_blank">📅 06:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85484">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات تهز جازان السعودية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/85484" target="_blank">📅 06:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85483">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b79c69b57.mp4?token=lHzd_UX45TSwdCom94FkDae5SwQUnT6yV0sTcyzSty_ZvKoC2w3D1SKRYR4iQE9R7hbZM00Oq_6ZTnIsxPhUAY7Qtl-KTRpE8K2tWhh95uEmO8ooJ3BoE2vbvmYp71hDUJldtzyd2CjgqptJCkIhOaOIB-qUdZS6kbvygiVnjg8dDcE6PKPE0CJByfd4xCRiFwAnF4FZtA2JLIESZfDR-Bvhd8pZJsltg8zyBmQVM1yKQL1qKvVj1l6qctzNIyfGlXR_tcNQdS_HALsTRiOE2Ycrt3TCe72Q7hQLSf009PiqVW2M0lFG90E1lTHLOlVei7NI-YUb9whz3IstpAQ5eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b79c69b57.mp4?token=lHzd_UX45TSwdCom94FkDae5SwQUnT6yV0sTcyzSty_ZvKoC2w3D1SKRYR4iQE9R7hbZM00Oq_6ZTnIsxPhUAY7Qtl-KTRpE8K2tWhh95uEmO8ooJ3BoE2vbvmYp71hDUJldtzyd2CjgqptJCkIhOaOIB-qUdZS6kbvygiVnjg8dDcE6PKPE0CJByfd4xCRiFwAnF4FZtA2JLIESZfDR-Bvhd8pZJsltg8zyBmQVM1yKQL1qKvVj1l6qctzNIyfGlXR_tcNQdS_HALsTRiOE2Ycrt3TCe72Q7hQLSf009PiqVW2M0lFG90E1lTHLOlVei7NI-YUb9whz3IstpAQ5eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من مدينة جيزان السعودية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/85483" target="_blank">📅 06:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85482">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجارات عنيفة تهز السعودية مجددا</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/85482" target="_blank">📅 06:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85481">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات عنيفة تهز السعودية مجددا</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/85481" target="_blank">📅 06:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85480">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/593dc6491b.mp4?token=W4o5RiOe1Z87VuFPAvPSK8diYhRvMY8IJhDIbRzt-G25V6iNnfKqn15_0SSTbB0tZzcQJCepmu92SBEk23VdlpfmraSvHdpwJNYsIt_2gPuCBiqXe5a7ZOlFIjit9Qu6j9LKnhAWvcpfM_yx-kbUIgDvUwr-LnCEV9ZgZoZFZwtIiEgTxYgq9HH85OQpTuMToK7zisZ9sJvCm-xcpTAYs0LopEFlC-FqSpLaRrkH7pnDHeApIgX84S_umS5tuysU7EZifeKQO90NG9b4aPVAQbts7SJYaUzY5frNxgIMF7WEttqstrOX17JcvE4x3_UJ5N_jH4P8vwg0jCYhD1v9KgDq17V31hQQMWAqdzEzhKUBddIDeVqLwwVApGiStOXr84oLyCF-Ir6BwMXLseYWTc8wUZ9o298CF3WD2vaLm5KORs3lc_JU0XM_VEvdk8CnDvS8Iz2qpB5qERzrw7Ezn9xyVQ7cF8dkGPFcidZ7NL8XURTiiEl_QbLqdco_2hjZRBKmJAQV2Fi2T8bRGjKNPh63l256yl8digYD8t9wceqHuPijlZxwlcC_Fi1ihCOl42rQ1_Bh12JNT6NSBXahk1zlC1Vk_bTCYBtgjaUOyfgpONf4DjSQ4IKjUoAsTWUV5N-Ig2cMLcECWky9cRihlx7Lido8Jhj97Smg5BD6lmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/593dc6491b.mp4?token=W4o5RiOe1Z87VuFPAvPSK8diYhRvMY8IJhDIbRzt-G25V6iNnfKqn15_0SSTbB0tZzcQJCepmu92SBEk23VdlpfmraSvHdpwJNYsIt_2gPuCBiqXe5a7ZOlFIjit9Qu6j9LKnhAWvcpfM_yx-kbUIgDvUwr-LnCEV9ZgZoZFZwtIiEgTxYgq9HH85OQpTuMToK7zisZ9sJvCm-xcpTAYs0LopEFlC-FqSpLaRrkH7pnDHeApIgX84S_umS5tuysU7EZifeKQO90NG9b4aPVAQbts7SJYaUzY5frNxgIMF7WEttqstrOX17JcvE4x3_UJ5N_jH4P8vwg0jCYhD1v9KgDq17V31hQQMWAqdzEzhKUBddIDeVqLwwVApGiStOXr84oLyCF-Ir6BwMXLseYWTc8wUZ9o298CF3WD2vaLm5KORs3lc_JU0XM_VEvdk8CnDvS8Iz2qpB5qERzrw7Ezn9xyVQ7cF8dkGPFcidZ7NL8XURTiiEl_QbLqdco_2hjZRBKmJAQV2Fi2T8bRGjKNPh63l256yl8digYD8t9wceqHuPijlZxwlcC_Fi1ihCOl42rQ1_Bh12JNT6NSBXahk1zlC1Vk_bTCYBtgjaUOyfgpONf4DjSQ4IKjUoAsTWUV5N-Ig2cMLcECWky9cRihlx7Lido8Jhj97Smg5BD6lmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب للصحفيين: عندما أرحل، ستصبحون جميعًا مفلسين.نموذج عملكم سينتهي.لن يكون هناك أحد لتغطية الأخبار.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/85480" target="_blank">📅 06:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85479">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامب: الأمور تسير على نحو ممتاز في إيران.لا تصدقوا الأخبار الكاذبة.  إيران تتحدث إلينا ويريدون اتفاقا ولكن لا أعتقد انهم مستعدون الآن.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/85479" target="_blank">📅 06:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85478">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇸🇦
🇾🇪
متداول.. انفجارات ونيران واسعة في مدينة جيزان السعودية جراء القصف الصاروخي اليمني.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/85478" target="_blank">📅 06:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85477">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9fd9e3a4.mp4?token=V_B6TGwGoLOR_6OnbFB6iC5tGQYcL2vjm2ao1oyzWAIsZG7X9lAGNapW2FcpXEYHT5mW_r-UjiVj5PSYaJL10aj57JqEPb7ffMTbHwKqmxColSU-goSVIxbKSssR4P3CM78ZN6Dv1TUneSI7Ohy7AUBSNlfBixxlO20zoxyE7mnFNwVnhdSj7mQPuqdOIsNj7C6YJZ26A9Ea5E3cnSivLqNWTSZOZ_anp9iOvqS5Ah7FYTiUNBziIrm1XWK7vUvfEL8Pz3_duZaxsrfBhD4Iju5q7aY3aCSN5oQr_5LRMfBOHoarapyl3JbnWOGVvECABuXrugDH6CH2FXlJ0KV3ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9fd9e3a4.mp4?token=V_B6TGwGoLOR_6OnbFB6iC5tGQYcL2vjm2ao1oyzWAIsZG7X9lAGNapW2FcpXEYHT5mW_r-UjiVj5PSYaJL10aj57JqEPb7ffMTbHwKqmxColSU-goSVIxbKSssR4P3CM78ZN6Dv1TUneSI7Ohy7AUBSNlfBixxlO20zoxyE7mnFNwVnhdSj7mQPuqdOIsNj7C6YJZ26A9Ea5E3cnSivLqNWTSZOZ_anp9iOvqS5Ah7FYTiUNBziIrm1XWK7vUvfEL8Pz3_duZaxsrfBhD4Iju5q7aY3aCSN5oQr_5LRMfBOHoarapyl3JbnWOGVvECABuXrugDH6CH2FXlJ0KV3ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية من النيران المشتعلة في جيزان عقب الهجوم الصاروخي اليمني</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85477" target="_blank">📅 05:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85476">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b34ad181aa.mp4?token=DLuD51Anivzi6mqwCnjOS5bB_ZkH-lu8XAxTKTCMVYtbxhDYeEvyYl-gO55MGeqYre8XIoo13Dl_I2sAK9D7cVBv-NDAe7aKe0lDUWbw8hJMjeolrF9ofBaY1O-c6qLCAKCo7ndrgXGwGWmjh8jJD6KXt5TQgxBRWWo6tHuUle5NErmlYTdSduZ9O3nZPTC0Uz1w2W9SQNKcZMIw927ehwE_9X8NLh9DdGKDkisvvvafECcDnezHw6vni5VO3lltKu6n55hN9llNWd76lF6IPrPXsfJL43xuSufNbjpHR3f5H0TTnjES7zWUcCh-sa72hJUwnHy7i0PLAQS3DB7DAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b34ad181aa.mp4?token=DLuD51Anivzi6mqwCnjOS5bB_ZkH-lu8XAxTKTCMVYtbxhDYeEvyYl-gO55MGeqYre8XIoo13Dl_I2sAK9D7cVBv-NDAe7aKe0lDUWbw8hJMjeolrF9ofBaY1O-c6qLCAKCo7ndrgXGwGWmjh8jJD6KXt5TQgxBRWWo6tHuUle5NErmlYTdSduZ9O3nZPTC0Uz1w2W9SQNKcZMIw927ehwE_9X8NLh9DdGKDkisvvvafECcDnezHw6vni5VO3lltKu6n55hN9llNWd76lF6IPrPXsfJL43xuSufNbjpHR3f5H0TTnjES7zWUcCh-sa72hJUwnHy7i0PLAQS3DB7DAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
مشاهد متداولة لم يتسنى التأكد منها لإنفجارات عنيفة في مدينة ضمد السعودية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85476" target="_blank">📅 05:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85475">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامب: الأمور تسير على نحو ممتاز في إيران.لا تصدقوا الأخبار الكاذبة.  إيران تتحدث إلينا ويريدون اتفاقا ولكن لا أعتقد انهم مستعدون الآن.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/85475" target="_blank">📅 05:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85474">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ae533044.mp4?token=FW6f5Z-R4S9gwKflu3QIDq-HUF7zynCLjXWaKLDwQZMIzQ4hx35MV77xKWesLLoOrlSJKF07mpTERX8eeqx-RAMzIsFLg4NMzkn8GELm5goAlEYFD0g0CYJSGrVOVKZEcso9Z400uhLPFkV5fhFIP5VntJP98st2qneuNJSrM1p2lxjzQYcFRnVQZ4RQIwkDYDQIgGRrhXzMlHGd5sElIdp2fPEBJKwf11UP-goqDG36UE935aGltJ3LEChmV325LfM-LW4okCDynIfNBnkHztL9cbknaRfF_zoRh9VGcf5tjucIoKnIbMFZMTbXv8dU0oykuVJqW9A4nb33-4ryRQEKmPM-kdhfbxjgWmixLmNUkGmBhjsRiXvoDZNnFVIqLHREPw7OHW1m7Az50i87R19_Dvp7i_4M90AzkBkblMaykrafC4jzkYeTlo_tGEGhnEJglzUJxtVFdgtAsUvgxBAN6SJhsOR1SD4EKzkLtsAQJ0hoVUCIZ-NBgqw4FA8p-MGJnZSwKi_3vh5FHlbbW5b0dyqI-61euJOPhEGfhu8AlzLRkHOKa0z3s8O0GmBA9vrDUEa_KGfZAidNQJ16hJgRum6E-v9baqdi5qhpH7JF2YdTxRQrynyIqjfWpbr2YHdDvyM9PgMctV5i8HdvleFp8tqyztrRegxNELSD7ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ae533044.mp4?token=FW6f5Z-R4S9gwKflu3QIDq-HUF7zynCLjXWaKLDwQZMIzQ4hx35MV77xKWesLLoOrlSJKF07mpTERX8eeqx-RAMzIsFLg4NMzkn8GELm5goAlEYFD0g0CYJSGrVOVKZEcso9Z400uhLPFkV5fhFIP5VntJP98st2qneuNJSrM1p2lxjzQYcFRnVQZ4RQIwkDYDQIgGRrhXzMlHGd5sElIdp2fPEBJKwf11UP-goqDG36UE935aGltJ3LEChmV325LfM-LW4okCDynIfNBnkHztL9cbknaRfF_zoRh9VGcf5tjucIoKnIbMFZMTbXv8dU0oykuVJqW9A4nb33-4ryRQEKmPM-kdhfbxjgWmixLmNUkGmBhjsRiXvoDZNnFVIqLHREPw7OHW1m7Az50i87R19_Dvp7i_4M90AzkBkblMaykrafC4jzkYeTlo_tGEGhnEJglzUJxtVFdgtAsUvgxBAN6SJhsOR1SD4EKzkLtsAQJ0hoVUCIZ-NBgqw4FA8p-MGJnZSwKi_3vh5FHlbbW5b0dyqI-61euJOPhEGfhu8AlzLRkHOKa0z3s8O0GmBA9vrDUEa_KGfZAidNQJ16hJgRum6E-v9baqdi5qhpH7JF2YdTxRQrynyIqjfWpbr2YHdDvyM9PgMctV5i8HdvleFp8tqyztrRegxNELSD7ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: الأمور تسير على نحو ممتاز في إيران.لا تصدقوا الأخبار الكاذبة.
إيران تتحدث إلينا ويريدون اتفاقا ولكن لا أعتقد انهم مستعدون الآن.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85474" target="_blank">📅 05:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85473">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4bb7ba831.mp4?token=oXPpqEBq2mlwepfkT38b5lO3z8UPYus0nb65MJCLpEtTvNeeSj__X_zD6q3NE0SZcwgUGgZsQhK-vZo6DdT1SY69zA6kfY6PDvbMbjfmd9xRUxDwFxBf7YpjmqiaDLrNQMDA70leQQlo8f0qplcoid5NT_iU-P4dQu5vipUQhE-7Hqy_ao4EClpb4UhOpkCi2JEg1bwalcT59sryAdIENRLNBMjvp_ED66eQmcfNkDcRlB7bywc0t6Fbcb6ZhhDRn8BO2CexMYeqPxnm8LMXG_zrTbPLHw3RJQJ8b25czj07tLJjPwK69uAW4rtJbOleP4hRWnMjRmsTXAuurW_pkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4bb7ba831.mp4?token=oXPpqEBq2mlwepfkT38b5lO3z8UPYus0nb65MJCLpEtTvNeeSj__X_zD6q3NE0SZcwgUGgZsQhK-vZo6DdT1SY69zA6kfY6PDvbMbjfmd9xRUxDwFxBf7YpjmqiaDLrNQMDA70leQQlo8f0qplcoid5NT_iU-P4dQu5vipUQhE-7Hqy_ao4EClpb4UhOpkCi2JEg1bwalcT59sryAdIENRLNBMjvp_ED66eQmcfNkDcRlB7bywc0t6Fbcb6ZhhDRn8BO2CexMYeqPxnm8LMXG_zrTbPLHw3RJQJ8b25czj07tLJjPwK69uAW4rtJbOleP4hRWnMjRmsTXAuurW_pkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عملية تأديب آل سعود مستمرة</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85473" target="_blank">📅 05:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85472">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQzhIp-kkwhpnUmGRlIsKxxbLnjfA8kypq6BbxHkmCRU35Jju6-6AlOlNEMuwxGWCO-LkvcMajGyxPCrZHKhmU4NzSTmcqlXXBMyNDavmE_oxno808SIyoDd89rlqaRDu9QkX5fu8bJFcr8ZrS06H6G0exCvHfdxgCiVwtZZjbslGHYtF1TwC6oiPERiFGVz4aWPMPOSwifmQB3Yv8JpUnaDVFJ3GbP8RKkjqPfHsklpwTEuzHSicKw1NPzI0AXK8E5IyR4qHCLoiFODejqRgjil1_fa9P0aaowNsRoT-_gpvVJNa5p1B8NTUeYKm4CNn11GtusXDJ_JWcZ5-rRSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏تحلق عدة رحلات جوية قبل الوصول إلى مدينة أبها الواقعة جنوب غرب السعودية، حيث تتعرض المنطقة لهجوم صاروخي يمني.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/85472" target="_blank">📅 05:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85471">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">موجة صاروخية جديدة تنطلق نحو السعودية</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85471" target="_blank">📅 05:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85470">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/85470" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/85470" target="_blank">📅 05:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85469">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85469" target="_blank">📅 05:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85468">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/85468" target="_blank">📅 05:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85467">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رجال أبوجبريل يستهدف جيزان السعودية بموجة صاروخية والنيران تشتعل فيها</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85467" target="_blank">📅 05:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85466">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارات ضخمة تهز ينبع</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/85466" target="_blank">📅 05:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85465">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nD2tG_Qp0jjfVQsAkC2EN2Js9FTX5A4wlGWIuYwHQJvKKIaTDd9HhqjO2iom0pJpuT56v_aVA2eKVHmFdRLB34dTPAVTmvHpVkV47wOeLecgZjYtsXH5LqbY2xzKlD5_mtV3omAUTwEy09xJo941WaSRZQajOcdM16kEd6l9HW2lsk04aR8JjhFBKpOFdrWDIWcBWwd3d3Jr-t8xqyGdhA2-V8ZVE1P8p5mJ5XRRY7rSkRI6tNLWs_CHzIYHzcTV_47TRL21FScDLQMEaXTIcqyzVMg6X8eWFwTw31HLffoQ0pN6h2x3NFAy2LeS0X4sVoYQ6yLRdiHrKfUIVZKYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رجال أبوجبريل يستهدف جيزان السعودية بموجة صاروخية والنيران تشتعل فيها</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85465" target="_blank">📅 05:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85462">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O9JpLwhtnpfY9XnO1ngi37eqteUhjM07vYo1pXI876Kh1jQCt2Zmz6_JZKFlHFzSncH8GZZFZ6SA0Ya1sw4k6KMbg40cewZKpa_sroGu1zG4IPSWVkRA_QMouMVq7D-WxAKUZQrJe44CINrCihIc8y-e74v5w0ggbN1vWqRpC9mD87tV8TY2_lpjvcypf5PbgapkTTsx2hgntqmrmxKIOe0ruojnkQ4jf-YK7KbYE5wJq5T93fEQzyn-oysiKEYIMJev8Mu15A_B-ISRmXstnKAVU2JI3TTo1Ct-lDOmUvRShvSR67YkrSoEdI6ar1uctfeyblKZoCpTuXDPlt-GOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlkXil88kn1T_u6qZrlBN76p_25YGgHQiiXZFHzy0OclIH5Nj7XXP-HaC-WkETXxneI5NQFDyJQ9YvMoBhZmUn0YCSCkTT3R6JZP7RJxYTp1p_k5XC-O0ID6rlQGtrohGoRZ9P6c_Zc_d5f_S4g4sP1ueG0xizUN7Q4a30ZO22Ouvc05nMlaE35aHLoE2Om-Fp83v_BOGVdDFnAEUN75gXWNdEd0X3GMdbSN8lDsuVL6ZgeRFQOjgnNqY6F-54N9r-6LTkYbdcpN0Uk_kTb9huxOz9v194CbdG63P4BdnY-t7LlkwNWQr75D_va6gDyd1Jd3BCxOcNPeoxCNRnXrfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8b45dbe9.mp4?token=owkcjYvaFeCEnZ6R9I-IFdkdYkXEO_D1PCZpqRD99igayQoUbfv139OY62AlHgpDsbMpTvZ0XYyexj32wRoWTa1mX3i6jwm1rpqDgkvs4_5oAP05dx0XCaCrL25YBfpStOYCIb7QITCRSqdJhkqQ7fsmFP7H_S_ev1bWUZigVxJX-kqm6d771hJe4OT83tB1v1Fnz2PuAgR1aSLzIsHY8XlEGGpFfJe2VsjSwftIzgUU0LtMi0YG5f-71UUwhB6ef2Fu9j5ipaKl6z7bud8-JzGhbtMQP4h8e01965-AnIX5phV8cYvc5Amb1Zh4TytzuiFzguH0Hdu6pubM62NDug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8b45dbe9.mp4?token=owkcjYvaFeCEnZ6R9I-IFdkdYkXEO_D1PCZpqRD99igayQoUbfv139OY62AlHgpDsbMpTvZ0XYyexj32wRoWTa1mX3i6jwm1rpqDgkvs4_5oAP05dx0XCaCrL25YBfpStOYCIb7QITCRSqdJhkqQ7fsmFP7H_S_ev1bWUZigVxJX-kqm6d771hJe4OT83tB1v1Fnz2PuAgR1aSLzIsHY8XlEGGpFfJe2VsjSwftIzgUU0LtMi0YG5f-71UUwhB6ef2Fu9j5ipaKl6z7bud8-JzGhbtMQP4h8e01965-AnIX5phV8cYvc5Amb1Zh4TytzuiFzguH0Hdu6pubM62NDug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النيران تشتعل في جيزان جراء هجوم صاروخي يمني</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/85462" target="_blank">📅 05:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85461">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/85461" target="_blank">📅 05:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85460">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هجوم صاروخي يدك مدينة ينبع السعودية</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/85460" target="_blank">📅 05:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85459">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/85459" target="_blank">📅 05:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85458">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/85458" target="_blank">📅 05:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85457">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">النيران تشتعل في جيزان جراء هجوم صاروخي يمني</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/85457" target="_blank">📅 05:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85456">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uhs3IcNo1e9g_HS2xpxtEqzfonom03qnJ__q3xVU40S37-of6pUeXFZkhOVPNPRofXce6lfNv-JA-Dl3qdUDWe2yqLE_TpIHjmNCHxU0vWt17ZwtsNfp0DdWleCl7EIy_bVp1TIUqWN-MOx3JqlVaFb0ck57GnqiRwcMBLC44W7vci8Q5rAmFI-fyOLRxESN3ZVXDwaVTzxxSh2JckVtG6gHLgw43qZHO9aq2ZvrQK7qIvohj-87n3RjExrLvCsCVYp32p0k4J8mGAric0dDT5nGp6XDd3trfgudhBW9RLBkp8yegAkergbGXrOhzHlbPcTHVHjtPScXKDTuGU7GXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد متداولة تظهر إشتعال نيران كبيرة في مدينة جيزان السعودية عقب هجوم صاروخي من اليمن</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/85456" target="_blank">📅 05:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85455">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee48f24b8c.mp4?token=owccPEpAtCY7nBU-1mzDu49KkdKkUAlwQpTBH0wZhpb4L8FMbmQBQ6BXc2PyX7y8ZSz-TIFLqnCYXuUOtb0tkaDxWEjvprTMOgBVwxfos2h1XEt96dlnqmsg_kmt2GPt62ZOR-mCqFCQaw6b5UqzyCf4dKb8JFjnnLC2eOP7opdUXm_47jOhn315YJJntzdnalp9ukPP4j7bGVrainNP4Lm17sFWaenUdIfYYhp8WFGAVixexDdreecKmcUXZfRnPej9ayeEGO9-dNzbxuzaiBpPUK92YadXaDZ4GqJufxkgKlzKzadjInzQlwK6SB4-eKIIJbiGFbxqyCFdEWfZkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee48f24b8c.mp4?token=owccPEpAtCY7nBU-1mzDu49KkdKkUAlwQpTBH0wZhpb4L8FMbmQBQ6BXc2PyX7y8ZSz-TIFLqnCYXuUOtb0tkaDxWEjvprTMOgBVwxfos2h1XEt96dlnqmsg_kmt2GPt62ZOR-mCqFCQaw6b5UqzyCf4dKb8JFjnnLC2eOP7opdUXm_47jOhn315YJJntzdnalp9ukPP4j7bGVrainNP4Lm17sFWaenUdIfYYhp8WFGAVixexDdreecKmcUXZfRnPej9ayeEGO9-dNzbxuzaiBpPUK92YadXaDZ4GqJufxkgKlzKzadjInzQlwK6SB4-eKIIJbiGFbxqyCFdEWfZkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قصف صاروخي وتصاعد اعمدة الدخان في مدينة جيزان السعودية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/85455" target="_blank">📅 05:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85454">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">أكثر من 5 إنفجارات هزت مدينة جيزان السعودية</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85454" target="_blank">📅 05:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85453">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هجوم صاروخي يستهدف مدينة جازان السعودية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/85453" target="_blank">📅 05:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85452">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انباء عن انفجارات في مدينة جازان السعودية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/85452" target="_blank">📅 05:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85451">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انباء عن انفجارات في مدينة جازان السعودية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/85451" target="_blank">📅 05:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85450">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تحليق طيران حربي في سماء الكويت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/85450" target="_blank">📅 02:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85449">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lToL7zS7dhHk_GBKIW619g9qWhKQgGqV7M-dZPm-eNKTDuE0cbeKCA60aj-5XyjpfSlKugQM8M0i2e6G3HXFxbF51eDi53J_SDMgJEj9HdZMI1YjmJTZvyyYjERjitb6sVyVpvniaEiwcsbmf-u2ZRdUFhR0jqTg-LN16ujJ2wdMLGJ-Hyz02zyDwxXGaLGqB_KfUHQqsxDX65BYiRCPyAWJppuzwWZFXZalRt7Z9eaO96r7b97REoUzAUhr3VAQP_ElmzZy4l3YrZ5sxU0A-b1G0fG0K37BCAUcIIsWtidvHknXgWtF4sqStIrccUS1Nj-13zX79o2m4HaYDJRneQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Guys in CENTCOM
Where is U.S. Concludes 14th Night of Strikes on Iranian , it’s to late ,
😆
don’t forget to write we destroyed the Iranian navy that we  already destroyed them 2 months ago</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/85449" target="_blank">📅 02:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85447">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
🇮🇷
ول ستريت جورنال ‏:
اشتكى ترامب لمستشاريه من صعوبة معرفة من يتحدث باسم القيادة العليا، وفي كل مرة تعتقد فيها الولايات المتحدة أنها أحرزت تقدماً على طاولة المفاوضات، تواصل إيران هجومها</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/85447" target="_blank">📅 02:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85446">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
إعلام أمريكي :
‏بينما تعود الولايات المتحدة وإيران إلى وتيرة يومية من الهجمات في جميع أنحاء الشرق الأوسط، يعيش مئات الدبلوماسيين الأمريكيين وعائلاتهم في حالة من عدم اليقين، غير متأكدين متى - أو حتى ما إذا كانوا - سيعودون إلى منازلهم ومدارسهم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/85446" target="_blank">📅 02:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85445">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/85445" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
عاشت المقاومة العراقية البطلة وسلاحها الموجه نحو الاحتلال</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/85445" target="_blank">📅 01:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85444">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dfa6493e.mp4?token=qOxZaCeOT2cFWXQU5XkB_Tk9nuabpqEGIw_B4lWQ0aCKOIqG63WG_vEph8wD3y2WdB4QPE0fGbr5oCjkaAu2E_yLL6rP38BIz8UsaXsZS5p22sr8mX4jOgIfa3Na3VI9FOUYm5YsADGQpVVAoIyC-lmXCDSSGEwYKOMi22buuYwUAwcGKNOo-f9tu0wOzPnYhaMrWbDDn7fCXrbMpzGGb9DZ0pxL_4l-Z_OkiaR-RTgC9QkVnzByjshadhg7hpLhbIN2-scRXKmDUptTlWtplSNaN61izX19E8m56nI0dur-n71SyqveaXduZ2levpcY1x3QwDXgDGQ_i4UdGEklCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dfa6493e.mp4?token=qOxZaCeOT2cFWXQU5XkB_Tk9nuabpqEGIw_B4lWQ0aCKOIqG63WG_vEph8wD3y2WdB4QPE0fGbr5oCjkaAu2E_yLL6rP38BIz8UsaXsZS5p22sr8mX4jOgIfa3Na3VI9FOUYm5YsADGQpVVAoIyC-lmXCDSSGEwYKOMi22buuYwUAwcGKNOo-f9tu0wOzPnYhaMrWbDDn7fCXrbMpzGGb9DZ0pxL_4l-Z_OkiaR-RTgC9QkVnzByjshadhg7hpLhbIN2-scRXKmDUptTlWtplSNaN61izX19E8m56nI0dur-n71SyqveaXduZ2levpcY1x3QwDXgDGQ_i4UdGEklCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
رتل عسكري كبير يجوب شوارع العاصمة العراقية بغداد.تحديدا مدينة الصدر مناطق جميلة الطالبية المدينة تتحول لثكنة عسكرية</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/85444" target="_blank">📅 01:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85443">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8wMoxnle0lTvXWWSS5dUdNhXHffm2K-hJJ40FYJ6_zWna2kWYvhqbGJR94c_7Tbubhiu5I6Ga_5JvoKtYNSO5u9Kd1Ky3dGv0D16cyTDu4QEExBiFJH97NzWtYQ_3e0F0_hOhKyIz9mojRmj3KwXiz80vCYjsQotmcXR8tFkTFsitEJAioAj0-dhxSZAA1X0p0ePKoCSArxSyxp7TR7UPS-TjTYjqnP5uDn5zD_RGVh8nE229UdOP5uRMUmU2oY91dIYdkJwzpSspWoV5mrzxdmeJbSu7hJ9gcLlwlFCAPSbqxXAtGNPlCcgKXz1mTHgQKT3msPCrl6jlAlrWQgwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار عنيف جراء سقوط صاروخ دفاعي من منظومة الباتريوت على نقطة الإطلاق داخل القاعدة الأمريكية في البحرين.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/85443" target="_blank">📅 01:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85442">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd41fe1d33.mp4?token=h7ndS6adXmo0N3Hpeg_21CKRdgKrYnjV_a6FohWrRrmv2BfP6cyZp0pNSgG2D_3nH_tMKT_9xhz9BI8vL_T0QXz5ejezhOfZpfm-6zKqG6Qeq2Sh9hEWMkOBYSyChCwF6cqgoDlgYDgs7aVCXMpjPllD_oN9IYEMBP40JloryenaWmNh5ZqOCFAaEETxiLQ0WCR_jCNexnBkCKuy6sF90WJvvxV-RGw93w-bNvss7o5foj9Je3prgp3cnBzcfRqpTGyiZyM_gL3Pv0oZwC8m3DrOgofyXp58b7e6JW_HQEk5xlIFqLh0dzhJenZshWCyvGkm-XVf3nxdFHW-ez-rNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd41fe1d33.mp4?token=h7ndS6adXmo0N3Hpeg_21CKRdgKrYnjV_a6FohWrRrmv2BfP6cyZp0pNSgG2D_3nH_tMKT_9xhz9BI8vL_T0QXz5ejezhOfZpfm-6zKqG6Qeq2Sh9hEWMkOBYSyChCwF6cqgoDlgYDgs7aVCXMpjPllD_oN9IYEMBP40JloryenaWmNh5ZqOCFAaEETxiLQ0WCR_jCNexnBkCKuy6sF90WJvvxV-RGw93w-bNvss7o5foj9Je3prgp3cnBzcfRqpTGyiZyM_gL3Pv0oZwC8m3DrOgofyXp58b7e6JW_HQEk5xlIFqLh0dzhJenZshWCyvGkm-XVf3nxdFHW-ez-rNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  خلل في منظومة الباتريوت الامريكية بالبحرين يؤدي الى اصابة صاروخ دفاعي في نقطة الإطلاق</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/85442" target="_blank">📅 01:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85441">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الله أكبر
خلل في منظومة الباتريوت الامريكية بالبحرين يؤدي الى اصابة صاروخ دفاعي في نقطة الإطلاق</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/85441" target="_blank">📅 01:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85440">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اصابة مباشرة لصاروخ إيراني على قاعدة تضم مقر الأسطول الخامس  في البحرين واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/85440" target="_blank">📅 01:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85438">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/85438" target="_blank">📅 01:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85437">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
‏
أسوشيتد برس:
الجيش الأميركي يعترض سفينة تجارية في خليج عمان.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/85437" target="_blank">📅 01:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85436">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇸🇦
🇦🇪
‏التحالف العربي الارهابي: لم يتم استهداف ميناء الحديدة وجميع موانئ الحديدة مفتوحة أمام الملاحة البحرية، والأهداف التي تم تدميرها مرتبطة بالتهديد على السفن التجارية بالبحر الأحمر.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/85436" target="_blank">📅 01:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85435">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هزة أرضية شعر بها سكان محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/85435" target="_blank">📅 01:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85434">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/85434" target="_blank">📅 01:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85432">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YwNK9bIc5rKpe4TPHsSWydrqIODfTxkBXCbc2oRa3XmNNJ2j1P-YmLrSAFwDkQ28XZH9v24trAfWN7CSG6Y_gABIN2V17Fs7WQ0jjhoBANaIOi-0vzvAKZ0vJUiSmkT3wfVDYwpoqttUX4VMTCnRaOZl6IfRoygRCqiUWo3Dgxc_b-lXeHz_KyAi6LdT_OlrFSbwtlEqUm3af6fUrQT8EcYOM-RFfAa5Kb63pw1glfYhKqOOQsq5r6YcuS633RUohDetk5lxvIfGupBhvDYO2d5LOg8DpBV5Wbjt7kpgNGbH9O7LN-P8cuYXgpEAZlWFLsgQYCUCsQzGRYb_mGCZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPE_NSFZ-zgrEPOjZLNyrzYbCfqrC4W9d8HRP5AUAgiJPE9CSzfVUEDK6htIDtFRiJXKHH_3E_0DyaFff2c2vgwkG-NtLIpAFPg0d3sAmrQaIMM2aiAbxspg-hzmlhSdErUzryvEEutEuil5Q8V4qL2i75AttX2-IzS4-o2XzU8ERjI-CJ-IW_mh9AHzlaO0ir8H_duADi_bmv9hSEUJG0p37lEgZ5bsp2H-75qWZnoBuCQ8euUPoQXerabGlh5ANBeQ7v-U10OEEY75IOkzJpYdjyKorCxDUye1sxWB_36ohh0Wv7AXkHKyfbWyE1u8L0IKQYwemXuQgmR7JkRXMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تفعيل منظومة الباترويت في سماء المنامة</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/85432" target="_blank">📅 01:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85431">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c750476a91.mp4?token=F0qO7d5KUAqROyjdC4ekUrRB_KHCluqyYEJiRKmK_HrTcmVGDMyO3_lA5vpjhSql37KUBCmC9kL20KbynUGM4IFu_WL1Zwq0TQYVyQgjgtMjeP00E8heySvbb9j-TjdPL14s0_9RFg0qDoEQNv-DUZYQMeTiYKYIxNhg_7yD2ds0vr3LRhEQmJh6yHoo3kumFY9WDPyW64c18Flqn6Aitx8q3NN7aPJqZTDwsCoNpZOYs_G8dKnifh0LOaIHBl2X2Cajd-NyGTlcjDJIUeUvJZs5Aq_SQa8k7CX5eAM17-IsF4ytvMCCwycifnvmClCYWJUrIDwj1wPQq5X0sJFlVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c750476a91.mp4?token=F0qO7d5KUAqROyjdC4ekUrRB_KHCluqyYEJiRKmK_HrTcmVGDMyO3_lA5vpjhSql37KUBCmC9kL20KbynUGM4IFu_WL1Zwq0TQYVyQgjgtMjeP00E8heySvbb9j-TjdPL14s0_9RFg0qDoEQNv-DUZYQMeTiYKYIxNhg_7yD2ds0vr3LRhEQmJh6yHoo3kumFY9WDPyW64c18Flqn6Aitx8q3NN7aPJqZTDwsCoNpZOYs_G8dKnifh0LOaIHBl2X2Cajd-NyGTlcjDJIUeUvJZs5Aq_SQa8k7CX5eAM17-IsF4ytvMCCwycifnvmClCYWJUrIDwj1wPQq5X0sJFlVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/85431" target="_blank">📅 00:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85430">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d30c5e9eb4.mp4?token=kuFkIEaFBAvDqMrmlb_ftOizt7NU8Z2YyUj7UOw1WGl96fd-wAKWXVl5jNLSJ6r9Nat-FcR6S7YDisHYbB_n2IqW6wpyfT7JaL9aak1c-M3H9Sf5Xa40ypYXO91Eu25hQngZ3rzpQXmoymYdUekQQcTrcuBg2NwbH5O-5CI7zcEfHjEU-WKZry46moWB4uHNgSU3J3brjes2lC57YRGA0rqLcHrOJqb8N6ua4RRpmtf9gNfZYQF_KcVQiWJPEiNkNzg0mpp4wa_ZWJKJcKvT9rH-MSIHz88VmEbvLX8u3sEaR1gc9Ea5irYyEsXARVSQ2RSQF6gEJKtlv1RIqTEgUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d30c5e9eb4.mp4?token=kuFkIEaFBAvDqMrmlb_ftOizt7NU8Z2YyUj7UOw1WGl96fd-wAKWXVl5jNLSJ6r9Nat-FcR6S7YDisHYbB_n2IqW6wpyfT7JaL9aak1c-M3H9Sf5Xa40ypYXO91Eu25hQngZ3rzpQXmoymYdUekQQcTrcuBg2NwbH5O-5CI7zcEfHjEU-WKZry46moWB4uHNgSU3J3brjes2lC57YRGA0rqLcHrOJqb8N6ua4RRpmtf9gNfZYQF_KcVQiWJPEiNkNzg0mpp4wa_ZWJKJcKvT9rH-MSIHz88VmEbvLX8u3sEaR1gc9Ea5irYyEsXARVSQ2RSQF6gEJKtlv1RIqTEgUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/85430" target="_blank">📅 00:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85429">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏
🇮🇱
ألغت الخطوط الجوية النمساوية وشركة النقل الإسرائيلية رحلاتهما إلى إسرائيل في نهاية هذا الأسبوع خشية تصعيد سريع للحرب مع إيران</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/85429" target="_blank">📅 00:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85428">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اصابات في صفوف المدنيين جراء العدوان السعودي على مبنى الاتصالات بمدينة الحديدة اليمنية.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/85428" target="_blank">📅 00:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85427">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/85427" target="_blank">📅 00:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85426">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/85426" target="_blank">📅 00:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85425">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇸🇦
🇦🇪
‏التحالف العربي الارهابي: لم يتم استهداف ميناء الحديدة وجميع موانئ الحديدة مفتوحة أمام الملاحة البحرية، والأهداف التي تم تدميرها مرتبطة بالتهديد على السفن التجارية بالبحر الأحمر.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/85425" target="_blank">📅 00:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85424">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇸🇦
🇦🇪
‏التحالف العربي الارهابي: استهداف مواقع عسكرية يمنية في محافظة الحديدة.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/85424" target="_blank">📅 00:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85423">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇸🇦
‏الاعلام السعودي: ميناء الحديدة لم يُستهدف ولم تلحق به أي أضرار.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/85423" target="_blank">📅 00:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85422">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0af83149f.mp4?token=h47Rij3-llhbd7p3XL6ncfVpNNaAq2JyrcOvjLJb0L0yZaGOCRAW8D-NmPrZENOOos6zVfgXqQL9lsvs6J8jHJSX5XMccjGjrpeYjaS6Ao0R0vAIzWTqR_EO10Of_3TZ3uoxwr7XZZle7NXajKrX_pVK2AAe098Li3pGWCJnNkefMqZAuc3mcxxjpjtQiaK5H7uW02BHiIpSsMwGXsUreMlNOk7NNOFVfrS2gvI-UeiWNzaVhNRVIJkVCPWwCE-hd6yGWbFyYCKe95vTdZjA_nAN8XdCcgTA3Si0CGkAu208zcDsVkOJD0Q7XF2LWrI2sL9rlkDKJjtXxMiTFsGP9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0af83149f.mp4?token=h47Rij3-llhbd7p3XL6ncfVpNNaAq2JyrcOvjLJb0L0yZaGOCRAW8D-NmPrZENOOos6zVfgXqQL9lsvs6J8jHJSX5XMccjGjrpeYjaS6Ao0R0vAIzWTqR_EO10Of_3TZ3uoxwr7XZZle7NXajKrX_pVK2AAe098Li3pGWCJnNkefMqZAuc3mcxxjpjtQiaK5H7uW02BHiIpSsMwGXsUreMlNOk7NNOFVfrS2gvI-UeiWNzaVhNRVIJkVCPWwCE-hd6yGWbFyYCKe95vTdZjA_nAN8XdCcgTA3Si0CGkAu208zcDsVkOJD0Q7XF2LWrI2sL9rlkDKJjtXxMiTFsGP9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد من سماء اليمن عقب إطلاق صواريخ اعتراضية يمنية باتجاه طائرات سعودية.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/85422" target="_blank">📅 00:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85421">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رويترز تدعي هجوم على ميناء الحديدة اليمني</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/85421" target="_blank">📅 00:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85420">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇸🇦
🇾🇪
استمرار العدوان السعودي باستهداف جزيرة كمران في الحديدة باليمن.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/85420" target="_blank">📅 23:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85419">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ99Z_AkApdqIfLlS-6qfcWC5Zp3UQ4eDxwIHEAEVTlXZK0Rf82FZT2GODyiOgWiWBHyJTq9Mg0jdC9lphSNfmzDT6fvhFY-zv-Qg9hLTEtjZl5nQhunutp_cDeJrIaCa9pFv0CPdDhTP0BKvQDlBSMWWjX7MlVlAhieZWOsjOeLiMdCWxtKyQh7Snmc5_5hRrLITbn_301ClojQ99WnpXVTTt3u0irSA8xi_QuF_qmvxo9x6V6NavDANGTYR53xkHYNXIOQqo8bqqN0c13X8im0d4TzN_JZwqeSX2obEa_e85DICaJAO0Ifrn4uSmQChsOyBZYCKPFeLf9QlB5E_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
اول تعليق يمني
الميناء بالميناء</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/85419" target="_blank">📅 23:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85418">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
هجوم بالطائرات المسيرة يستهدف مقرات الاحزاب الاثنية الايرانية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/85418" target="_blank">📅 23:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85416">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jJCRai_134XeMWGUPcP1vdFsR3NeDsWaz0JZfdIbBfIhREO4HEN_uU7q4cxzsLS2Hz69ZEkd1Ao899mobdN-pnPFpIitB2-3t0ApKGdpUl1Lq93-EGFRIXAoas6CCJiQYCfCx2HWdbJmgtGD1DXKOjkCr1ttETDjQ7b47q60RnzMrIuCo378xs4dQAnlftCjTPyRPoXWxHR1oKa7GWT_nlyFla9RC5W3nVBwlHrjrIsKDTc3kBxLre4aLT2sFsclkcTioMvwWytEyHgxz4X8e0vamUNsVRkpX8o887FLt0O9SqPu4RPlFWXT3l_cB_f3lh6DKoAv2VBnnzhmIjYnvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2suauiisL_eZ5D-59UKodYC-LanGk4Kslf7t7C-gtoiCEA2SbJZkzLYSPbDRbgWyDqoPzaJSHAD9O3ZwIHARc_JsiAWKkUdmH9nv4Wm5DY2MAKZHaUWV3cozYSd0mzEuDUlTgqLYaTVo-ROHlG4PAsHgvN46LKdFXAo_OPUuUx1gDE9qAJi3vQxIxHPExm0GJNe2b0mXBXWJ6O8-QbGREWxcuJgBmEYEPpiHZOyneami9j_7MuWXY3SYpLp24V9hUTLhcR2TEWqQ8mjoIGHDYVYNnNnUT5JGwPvN4b0emliWDxMofyXkHzhc7Oj4piiphkG95Pzbin10cLzaHFg9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد اخرى لارتفاع اعمدة الدخان من ميناء حديدة في اليمن</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/85416" target="_blank">📅 23:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85414">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA-zRm9kzmY1FznvzWlPvxOk4PJIXxbyW8CuDpt716epzpolStStlrHdQzUhT2ahBVEpFbY1CdrjN2Xytxg53T-B0dVmJjRBc3jHW6PJJ7_yvuAZbgjb4tyCuWrsFqchQZXf699iLGLnpGIed7Gw5QwaUzIKQ9kVDjdVHlFsJSpw0K7KSbBl3oQjdrTVr5diwFDqNKIQClIQ12p4YMCGWksF0g-h2-UmEJx3yGFCAPjrtAfmP3vDIVjfVjnKXv-VUPzUxhPj3DBBe7N0_fQtUduIrtjcfEnxAbI_T1aZvTvW0xBXw8rLCr3-UklKxT8b0dSkVH03_vKjLbQOS9nxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رويترز تدعي هجوم على ميناء الحديدة اليمني</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/85414" target="_blank">📅 23:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85413">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رويترز تدعي هجوم على ميناء الحديدة اليمني</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/85413" target="_blank">📅 23:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85412">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏
🔻
حظرت فرنسا استخدام الأطفال دون سن 15 عامًا لوسائل التواصل الاجتماعي، لتصبح بذلك أول دولة في الاتحاد الأوروبي تُقر حظرًا شاملًا على هذه المنصات، في ظل تزايد المخاوف في جميع أنحاء العالم بشأن الآثار الضارة للمحتوى الرقمي على الأطفال.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/85412" target="_blank">📅 23:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85411">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4e996641e.mp4?token=M1igGPrTxlOFScUnxJb4oH50xa_4EdWuJVWuhyyx5rMNRFS31SvE1kjkU_9SznLandzHlb_y0amsVPBj2teS_n541gh64xviohnLWemY9PEIWQtHJXBui88H9g4WbH6fgJCcd5nRekpepXaGpOQkrod9gbinHoW8gyC2cSOPbbHbgYqMdDRQkfr9e7FsGlqBLdPg9omkckbNs4mdgAs8XJK16mR2-Z45PLNdwDU-YHiBZl5tu-oAp2UuuuCa3sza_lVZDeaudwFjC8-mgsFP5WfK0H0ehITQ4V7-dbow3fdujsspNmewVPu78rILpc6F4QpbxZrCvbEicpPOpPEfjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4e996641e.mp4?token=M1igGPrTxlOFScUnxJb4oH50xa_4EdWuJVWuhyyx5rMNRFS31SvE1kjkU_9SznLandzHlb_y0amsVPBj2teS_n541gh64xviohnLWemY9PEIWQtHJXBui88H9g4WbH6fgJCcd5nRekpepXaGpOQkrod9gbinHoW8gyC2cSOPbbHbgYqMdDRQkfr9e7FsGlqBLdPg9omkckbNs4mdgAs8XJK16mR2-Z45PLNdwDU-YHiBZl5tu-oAp2UuuuCa3sza_lVZDeaudwFjC8-mgsFP5WfK0H0ehITQ4V7-dbow3fdujsspNmewVPu78rILpc6F4QpbxZrCvbEicpPOpPEfjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
ترامب حول الاتفاق النووي السعودي:  إذا لم تنضم المملكة العربية السعودية إلى اتفاقيات أبراهام، فلن أقم بهذا الاتفاق.  كان هذا الأمر مفهومًا دائمًا. كانت المملكة العربية السعودية على علم بذلك.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/85411" target="_blank">📅 23:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85410">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521af5d459.mp4?token=A25p86P6bqAADewm30JBGd_vIXUOJCQuyWgtKBqrzngk_s50xblUoCr02N6EcCoQmhIYmBc6XWITIGe369xIbSsE2ebLTgaq1bWidf3cTr-MXt1Xz216rcw-qmWwRuCkIIXOMrw7D-3VlwNDDn0ZoDM0SWYtviMG9RRY0X9q1YRAWBY9TjNdrKuymlzCOeLVAqsLL6S9YBy1TAIsax01rXi4yyv01vdijaEPLL6IWUARXdHYOL0F7UwhEvqKiXkQhddaMOoIV8pqarn7U9FbSHFDScEr4KLhcX5xnaDt5C9p0iCOj-FfaIgs_5eAKEyN_v0vDeBiT9Gn6TQ_onIMBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521af5d459.mp4?token=A25p86P6bqAADewm30JBGd_vIXUOJCQuyWgtKBqrzngk_s50xblUoCr02N6EcCoQmhIYmBc6XWITIGe369xIbSsE2ebLTgaq1bWidf3cTr-MXt1Xz216rcw-qmWwRuCkIIXOMrw7D-3VlwNDDn0ZoDM0SWYtviMG9RRY0X9q1YRAWBY9TjNdrKuymlzCOeLVAqsLL6S9YBy1TAIsax01rXi4yyv01vdijaEPLL6IWUARXdHYOL0F7UwhEvqKiXkQhddaMOoIV8pqarn7U9FbSHFDScEr4KLhcX5xnaDt5C9p0iCOj-FfaIgs_5eAKEyN_v0vDeBiT9Gn6TQ_onIMBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
ترامب حول الاتفاق النووي السعودي:  يجب أن تكون السعودية جزءًا من اتفاقيات أبراهام.  حان الوقت الآن. لم ينضموا هم والآخرون بسبب إيران، ولكن إيران لم تعد تمثل مشكلة.  إيران لم تعد قوة عظمى.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/85410" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85409">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/85409" target="_blank">📅 23:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85408">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/85408" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85407">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD8KTPzRgFhVsOnIOtSVyBrdHb5lYmB1zG6_yPFBfny4tY7ACHe4zvHYMbMdHmspdsTo-pH5WGUiK5c6ndp-qCd4X4-RbTZ2cYT8BVliDP7fPAOFswn4_9j26O3GMeScQqmQ8t2xqANCbE6l8d8UUJbOgKMFI558OsxqxsLHNgGEwMhuhJUyZYVKulg93Vz-b1MgRw5moCa0X4KRFRWniT-t9KMHrllTxpocXXx44dsB91d8pv4lsibRL1VFbs2RsxKsZqC1hAew38ftNfq1kk87e3zds_qUbLXbhXn6DHrE1texz4GHLvXuAtf4YrFGKUINIOj8-OmBTWcuVSJ_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏ترمب: الذخائر جاهزة للضربة الكبرى ضد إيران</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/85407" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85406">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇸🇦
‏
هيئة النقل السعودية:
السفينة المستهدفة في البحر الأحمر تعرضت لإصابات طفيفة في بدنها.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/85406" target="_blank">📅 23:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85405">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏ترامب: يمكننا التفاوض ونحن نجري محادثات مع إيران</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/85405" target="_blank">📅 23:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85404">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0368971c8.mp4?token=MC4sDIoxWpHcN0b_RgZJmGAp2DdHfEg6bxRFBuiK2MyAJKJzs9kNFgC6QdhP4IX4OBQ8ACsH51z9MYV6dJirK6aBWZQwIbCcIGc1JTFodY1WprEzWj5JKfFB5ZGbD_q-RMD3eW6Km_YFjceZNdLraKOgcA12cznTXR7QXFIdAupNAyd4yS6eG6V-1zRled7qaSmJ2kC2aghudnyv2xL0PYbIP-8ALbqaMeIumfsed7LhyeBKdBFHNQju3TELd2IUakVCo-vNRktqW0jqA_8Rrx7fsNLJOJx6wWIlxlCYaat3DItqBR1iB0dz0L_UxFAu1F4DUiubU-KlewGMTKrUDIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0368971c8.mp4?token=MC4sDIoxWpHcN0b_RgZJmGAp2DdHfEg6bxRFBuiK2MyAJKJzs9kNFgC6QdhP4IX4OBQ8ACsH51z9MYV6dJirK6aBWZQwIbCcIGc1JTFodY1WprEzWj5JKfFB5ZGbD_q-RMD3eW6Km_YFjceZNdLraKOgcA12cznTXR7QXFIdAupNAyd4yS6eG6V-1zRled7qaSmJ2kC2aghudnyv2xL0PYbIP-8ALbqaMeIumfsed7LhyeBKdBFHNQju3TELd2IUakVCo-vNRktqW0jqA_8Rrx7fsNLJOJx6wWIlxlCYaat3DItqBR1iB0dz0L_UxFAu1F4DUiubU-KlewGMTKrUDIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
ترامب حول الاتفاق النووي السعودي:  يجب أن تكون السعودية جزءًا من اتفاقيات أبراهام.  حان الوقت الآن. لم ينضموا هم والآخرون بسبب إيران، ولكن إيران لم تعد تمثل مشكلة.  إيران لم تعد قوة عظمى.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/85404" target="_blank">📅 23:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85403">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3a1afad1.mp4?token=YWViuqgeKTZD_7GZC5b96RL5qzOlV-3Y0CbRRUV9UKVjDLdge2_5lUjqbC8J8m3GluW20kq3cHd6EPo9HKjLPSqm5ed9o2BBj2SVv5CWoLBqxG_Ib_sLIu15VQXGXM6O65H0GVks-SftK8Hh7sf6Ea84zEPfnpY2eA69_ScaNL3nwWTHURHAIZmgUBCH4GVD62IO9SjJoRHOE6E7WIz88ZOzzgmqb1BoOKM_flaJU1YT3XdqJkAdPVQZ833bKNoL2ptR8kCk1fRRwqjRJVzMvU17g2nFzNSdVJ2ovBONHKVU4wRuFLUQ2N3FuhRxreGmjqnXQHQEWh2IUU6Qcjd3Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3a1afad1.mp4?token=YWViuqgeKTZD_7GZC5b96RL5qzOlV-3Y0CbRRUV9UKVjDLdge2_5lUjqbC8J8m3GluW20kq3cHd6EPo9HKjLPSqm5ed9o2BBj2SVv5CWoLBqxG_Ib_sLIu15VQXGXM6O65H0GVks-SftK8Hh7sf6Ea84zEPfnpY2eA69_ScaNL3nwWTHURHAIZmgUBCH4GVD62IO9SjJoRHOE6E7WIz88ZOzzgmqb1BoOKM_flaJU1YT3XdqJkAdPVQZ833bKNoL2ptR8kCk1fRRwqjRJVzMvU17g2nFzNSdVJ2ovBONHKVU4wRuFLUQ2N3FuhRxreGmjqnXQHQEWh2IUU6Qcjd3Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
ترامب حول الاتفاق النووي السعودي:  يجب أن تكون السعودية جزءًا من اتفاقيات أبراهام.  حان الوقت الآن. لم ينضموا هم والآخرون بسبب إيران، ولكن إيران لم تعد تمثل مشكلة.  إيران لم تعد قوة عظمى.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/85403" target="_blank">📅 23:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85402">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38cc825320.mp4?token=eiZ3LteBDGeVYlpugQ6lf0Pf5Im5GqlIgZI8YDKW2sUZgwwa2qZ3AU3Rk9LAiRADNfG-5GvSFVnLCRMzMXTQ0CFOS8gu8MU0iRj6CXg72dn1EUKq_Gvr3ePGszLWH4ZOQ72zC7OkKphS3qAyRGN-3uxVSr5zDnNGh8e6AtOdjQj8aWyHokuBtglgPayDC520eEfAOFVSDfzTHG1TmtH3wx6qxUuAOZo5k4azeozfRSmURc6qHYpxiEgJcefzRCFFjU8TTEFCR6vLRAqOR3TX7R9U-nH1NNs28PC088lc49k974QRVaVhWwdKeohwD1YvMTiZJ1zmKUtAPcCdiRY0WEpmRK1UW1juwff46exVOkqyg4X36kbUAY6W-xCIYh_iHZkdSDDkEVUo0cA3Ngk3v2mpV7rOwGN4i-vaLIft8VrI9V51V3r3CYOc_f-XcFX9qYDlV--12i3It3LrHWbMcoRrdK996kj4oEADNLtMCKGQTDNr3ESsIjmMyT5eJpnBBrb77hmQu_StvGhpl8DrjxqUHwqY-iawZkvvxUIqYl-LToSLCqHd_7GbkSlZk-P-ro9mXU0iC51JMK63EQ4TZL_r75Q83eyClH5UiX6pZmM9kE0hLpNnOPskKhfPVZ20Wr0cL_xGSpIO1mNDZCxnqNVnAThOhhL-A-5lAxCx4q0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38cc825320.mp4?token=eiZ3LteBDGeVYlpugQ6lf0Pf5Im5GqlIgZI8YDKW2sUZgwwa2qZ3AU3Rk9LAiRADNfG-5GvSFVnLCRMzMXTQ0CFOS8gu8MU0iRj6CXg72dn1EUKq_Gvr3ePGszLWH4ZOQ72zC7OkKphS3qAyRGN-3uxVSr5zDnNGh8e6AtOdjQj8aWyHokuBtglgPayDC520eEfAOFVSDfzTHG1TmtH3wx6qxUuAOZo5k4azeozfRSmURc6qHYpxiEgJcefzRCFFjU8TTEFCR6vLRAqOR3TX7R9U-nH1NNs28PC088lc49k974QRVaVhWwdKeohwD1YvMTiZJ1zmKUtAPcCdiRY0WEpmRK1UW1juwff46exVOkqyg4X36kbUAY6W-xCIYh_iHZkdSDDkEVUo0cA3Ngk3v2mpV7rOwGN4i-vaLIft8VrI9V51V3r3CYOc_f-XcFX9qYDlV--12i3It3LrHWbMcoRrdK996kj4oEADNLtMCKGQTDNr3ESsIjmMyT5eJpnBBrb77hmQu_StvGhpl8DrjxqUHwqY-iawZkvvxUIqYl-LToSLCqHd_7GbkSlZk-P-ro9mXU0iC51JMK63EQ4TZL_r75Q83eyClH5UiX6pZmM9kE0hLpNnOPskKhfPVZ20Wr0cL_xGSpIO1mNDZCxnqNVnAThOhhL-A-5lAxCx4q0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
ترامب حول الاتفاق النووي السعودي:
يجب أن تكون السعودية جزءًا من اتفاقيات أبراهام.
حان الوقت الآن. لم ينضموا هم والآخرون بسبب إيران، ولكن إيران لم تعد تمثل مشكلة.
إيران لم تعد قوة عظمى.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/85402" target="_blank">📅 23:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85401">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
‏
ترمب
: لن نسمح لإيران بأن تكون بلطجي المنطقة</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85401" target="_blank">📅 23:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85400">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔻
🏴‍☠️
زلينسكي : ‏
نعلم من معلوماتنا الاستخباراتية وشركائنا أن الروس قد جهزوا صواريخ لشن هجوم واسع النطاق جديد على أوكرانيا. قد يقع الهجوم اليوم، ولدينا معلومات أولية تشير إلى أنه قد يحدث خلال الـ 48 ساعة القادمة. لذا، نرجو منكم توخي الحذر والانتباه إلى تنبيهات الغارات الجوية. ونتوقع تفهمًا من شركائنا، فالدفاع الجوي هو أولويتنا القصوى، ويمكن للشركاء تقديم الدعم اللازم لنا.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/85400" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
