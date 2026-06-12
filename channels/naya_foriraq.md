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
<img src="https://cdn4.telesco.pe/file/hp1D4-5FQEEJ4vY-1-jVRnPNpQwRMvtarPgPeFIhlVotFQ0FGNZPFoYeBPjkCrxHPDBsEmJ2AmwRTQl5vsCfFMn5ja--C_khFhq9jgsxO8jQmL5h4fPAfmKwI3_4fpwNJ0c7FmrbMJ2bUsS-PNAxRI65OWqfn4oEpT7rcnpWoipUAvELm5sddhKhcWrvwZSZHChJTrglDeOFxeoBrDkYNxsNtvtarkuK8s4k5gP3deYEnLuuMo7dNNb_bE9zzHGDwr0OIxq00003sPe9xzeG_UvmKW-uo4stA9Xa-LUR7t-5UpfrWUzQdsAosNxEu84GBxCAJh5qdw7U_aGY9W5pww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 260K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 22:28:47</div>
<hr>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابتي ميركافا لجيش الإحتلال الإسرائيلي في محيط بلدة يحمر الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/naya_foriraq/78549" target="_blank">📅 22:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🌟
حسين الحاج حسن النائب في كتلة حزب الله البرلمانية:
ما تبلغناه بشكل واضح من إيران أن لبنان مشمول بوقف إطلاق النار.
تم إبلاغنا من مسؤولين إيرانيين أن إسرائيل ستنسحب من الأراضي اللبنانية وفق الاتفاق.
لن نقبل بالعودة إلى ما قبل 2 آذار 2026 على الإطلاق وليس لإسرائيل حق في البقاء بأراضينا.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/naya_foriraq/78548" target="_blank">📅 22:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78547">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭐️
هنتر بايدن إبن الرئيس الأمريكي السابق جو بايدن:
لدى دونالد ترامب الجرأة ليقول إنه طوله 6'3 ووزنه 224 رطل، بينما نعلم كلانا أنه طوله 5'11 ووزنه 300 رطل. لدى دونالد ترامب الجرأة ليقول إن هناك أشخاصًا رائعين جدًا على كلا الجانبين.
لدى دونالد ترامب الجرأة ليقول إنه سيُنهي الحرب في العراق في يوم واحد. لدى دونالد ترامب الجرأة أن يكذب في وجهك ويضربك بالبول ويخبرك أن الأمطار تهطل. هذا ليس أصالةً.</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/naya_foriraq/78547" target="_blank">📅 21:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭐️
رويترز:
الإمارات ستفرج عن مليارات الدولارات لإيران.
سيتم إطلاق ما لا يقل عن 10 مليارات دولار أمريكي، مع تسليم أول 3 مليارات دولار أمريكي بالفعل، وقد يصل المجموع إلى 20 مليار دولار أمريكي مقابل وقف الهجمات وتجديد التعاون الاقتصادي والاستخباراتي.</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/naya_foriraq/78546" target="_blank">📅 21:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
09/08-06-2026
تجمّعات آليات وجنود جيش العدو الإسرائيلي في بلدات البيّاضة، رشاف، وفي محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بصليةٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/naya_foriraq/78545" target="_blank">📅 21:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭐️
مصدر إيراني مطلع:
وزير الخارجية الباكستاني سيتوجه إلى جنيف.</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/78544" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78543">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الإيرانية:
ليس من الجديد أن يُقال لنا إننا قريبون جدًا من التوصل إلى تفاهم.
المشكلة التي واجهناها خلال هذه الفترة هي التصريحات المتناقضة من الطرف الآخر.
بخصوص نص التفاهم، نحن بصدد وضع الصيغة النهائية له داخلياً.
يُعقد حالياً اجتماع للمؤسسات المعنية.
لا أستطيع تأكيد أيٍّ من التكهنات حول نص التفاهمات.
إن عدم قدرتنا على الحديث عن تفاصيل العملية الدبلوماسية لا يعني أن الناس ليسوا محل ثقة.
نأخذ تجاربنا السابقة مع الولايات المتحدة بعين الاعتبار دوما.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/78543" target="_blank">📅 20:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بناء على مناشدة عبر نايا
استجابة الحاج حسين قانونية للمناشدة وصرف راتب عدد من الاخوة  بالحشد الشعبي الذين لم يستلموا منذ اشهر بسبب تبديل البطاقات الائتمانية
#شكرا_قانونية</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/78542" target="_blank">📅 20:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي يزعم: واشنطن ستحصل على مواد مخصبة بموجب الاتفاق مع إيران.  مسودة الاتفاق ترفع الحصار الأمريكي وتؤدي إلى تفكيك البرنامج النووي الإيراني.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/78541" target="_blank">📅 20:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي يزعم: واشنطن ستحصل على مواد مخصبة بموجب الاتفاق مع إيران.  مسودة الاتفاق ترفع الحصار الأمريكي وتؤدي إلى تفكيك البرنامج النووي الإيراني.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/78540" target="_blank">📅 20:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⭐️
‏أكسيوس: ترامب أبلغ نتنياهو أن الوقت حان لإنهاء الحرب مع إيران.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/78539" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇸
ترامب: ما زلت أعتقد أن الاتفاق قد يوقع خلال نهاية الأسبوع أو يوم الاثنين.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/78538" target="_blank">📅 20:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78537">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95d839e0a.mp4?token=uOQZ-ywTe0zcNgsYXfzAWxCPS1T0HMDPqaZHtbabBS0O2mA6LAUndrtw6OLZGOk3G4XPGHjltYYEO1k0e958ReoZiba6tNKaDOpo1ZFd_kOPIg9h-Y4j0ISp93JWiHKshjdj4TOP7ETqzZCbe1L57hycLay44_MZj7GYLPbaj5gYO33ppflp3zrTmqu-TglTY8b54096Qps9pwPOPm-wQXe7rGTmYk8I5GoXRsm7d8bcrxYaclaKHz-xsji5GYQbWe695CeK-xweP6Zv4DRVagQB7PwaymfxPmkEmOa33vSgIc95Nm-mlypFT8Jp9X9jj_O17Iq9Z53xXVAYqr28l0c8wegHnQgcD_7E20pJTbctMRyBwdt-T1QLc6PqJ_bNEmhwxyNQTpgaTWs1jJOloiYRA7hPy2Qtsdm8bCLEgOgQ70AQFPIA3xtJojOZ1qcsERPfYpadFrd2gugZh6kgp0SHPUX05oWxX5rwilZZspS3L-tx38qYTI-hrqpTUronKYRx4T15CWM1WPTV8pBllAF3X23zacoTeXAGw4l9sK1WgPWC-F9N0fSLnGGKz36UqwzuRwL-7YPaFtC6KFgmyYdz0v7tzzYQ4GHrq1Atn1PynP1-C7Rf8roPajzhfOt4yzTFwHiux6nZL3HrIiWoLDLgGFKZeclDldh0yeAEVok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95d839e0a.mp4?token=uOQZ-ywTe0zcNgsYXfzAWxCPS1T0HMDPqaZHtbabBS0O2mA6LAUndrtw6OLZGOk3G4XPGHjltYYEO1k0e958ReoZiba6tNKaDOpo1ZFd_kOPIg9h-Y4j0ISp93JWiHKshjdj4TOP7ETqzZCbe1L57hycLay44_MZj7GYLPbaj5gYO33ppflp3zrTmqu-TglTY8b54096Qps9pwPOPm-wQXe7rGTmYk8I5GoXRsm7d8bcrxYaclaKHz-xsji5GYQbWe695CeK-xweP6Zv4DRVagQB7PwaymfxPmkEmOa33vSgIc95Nm-mlypFT8Jp9X9jj_O17Iq9Z53xXVAYqr28l0c8wegHnQgcD_7E20pJTbctMRyBwdt-T1QLc6PqJ_bNEmhwxyNQTpgaTWs1jJOloiYRA7hPy2Qtsdm8bCLEgOgQ70AQFPIA3xtJojOZ1qcsERPfYpadFrd2gugZh6kgp0SHPUX05oWxX5rwilZZspS3L-tx38qYTI-hrqpTUronKYRx4T15CWM1WPTV8pBllAF3X23zacoTeXAGw4l9sK1WgPWC-F9N0fSLnGGKz36UqwzuRwL-7YPaFtC6KFgmyYdz0v7tzzYQ4GHrq1Atn1PynP1-C7Rf8roPajzhfOt4yzTFwHiux6nZL3HrIiWoLDLgGFKZeclDldh0yeAEVok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 07-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/78537" target="_blank">📅 20:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
ترامب: اعتبرت منشور وزير الخارجية الإيراني عراقجي بشأن الاتفاق إيجابيا جدا.  إيران اعتذرت سرا عن تقديم معلومات كاذبة بشأن الاتفاق.  طالبت بتوضيح علني بشأن تقارير إعلامية رسمية إيرانية عن تلقي طهران مليارات من الأصول المجمدة فور توقيع الاتفاق.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/78536" target="_blank">📅 20:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
رئيس وزراء باكستان:  وسط جهود الوساطة المكثفة المستمرة من جانب باكستان، نحن على دراية تامة بحملة التضليل المستمرة التي يشنها أولئك الذين يرغبون في تخريب اتفاق السلام.  بغض النظر عن الضجة، يمكننا أن نؤكد أنه تم التوصل إلى نص نهائي متفق عليه لاتفاق السلام،…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/78535" target="_blank">📅 20:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🐦
سي إن إن:
كادت الولايات المتحدة أن تفكر في عملية برية كبيرة لاستيلاء على اليورانيوم عالي التخصيب في إيران، حيث قام رئيس هيئة الأركان المشتركة دان كين بزيارة سرية عاجلة إلى مقر القيادة المركزية للقوات الأمريكية في فلوريدا في شهر مايو لمراجعة الخطط قبل إطلاع الرئيس ترامب عليها.
تم تعليق العملية في نهاية الأمر بسبب مخاوف من أنها قد تؤدي إلى رد فعل إيراني شديد، وإطالة أمد الحرب، وإلحاق أضرار بالاقتصاد العالمي، وتؤدي إلى خسائر كبيرة في الأرواح الأمريكية.
قام المخططون العسكريون بتقييم المهمة على أنها تنطوي على مخاطر "عالية إلى شديدة"، وقد تتطلب إرسال مئات من قوات العمليات الخاصة لدخول المواقع النووية الجوفية المحصنة بشدة.
في حين تعتقد المخابرات الأمريكية أنها تعرف مواقع المواد (فوردو، ونطنز، وأصفهان)، إلا أن خبراء النووي يشككون فيما إذا كان يمكن تحديد موقعها وإزالتها بأمان خلال عملية قتالية.
كما قيّم المسؤولون الأمريكيون أيضًا أن إيران قد ترد بالوسائل الاقتصادية من خلال تشجيع الحوثيين على تعطيل مضيق باب المندب، مما يهدد شحنات النفط والطاقة العالمية.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/78534" target="_blank">📅 20:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78533">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭐️
المدير العام للوكالة الدولية للطاقة الذرية:
سنجعل التحقق من النطاق الكامل لقدرات إيران النووية أولويتنا القصوى.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/78533" target="_blank">📅 20:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNnkfuq7xWrIo8dGbn0NFlKCQIUAc5nKvTC8rppBtbXG8CxfRi9REA_4njBMi91pV3h7Aedn4JHa--MuyKbx97WQUInyRp_mZLa5m4Tl5wuCrrFMA2wlDAfATfRV0kqCZgPxjzrJRHtONSuQ0YmcAw0X8gJm5aMJVzCmmyQ8W_V-2cMXiwHXtKQtIiKuVpwW-xz1YfmeFgSUh1_S_n3AzWRpXldm-aI7Rm6JsqoldBqEdK1YJ2P8o5kHQ2oR751LawbwjjmewpFftAPY7TJ0hkWKuqvz2N6Otir4yTdFJtyQ7BAv7gGlRWa_qGV3Ww_IENMDcxyqTm9noQkKzvQLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
رئيس وزراء باكستان:
وسط جهود الوساطة المكثفة المستمرة من جانب باكستان، نحن على دراية تامة بحملة التضليل المستمرة التي يشنها أولئك الذين يرغبون في تخريب اتفاق السلام.
بغض النظر عن الضجة، يمكننا أن نؤكد أنه تم التوصل إلى نص نهائي متفق عليه لاتفاق السلام، وتعمل باكستان الآن بشكل وثيق مع كلا الجانبين لوضع اللمسات الأخيرة على الخطوات التالية.
لم يكن السلام أبدًا قريبًا كما هو الحال الآن.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/78532" target="_blank">📅 19:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d31c79e4.mp4?token=gJIr5iz0d3uwGalxn8YY6f1KymAnPNNukTHoaQhpOXsHtcL_hQf6HLiNSqT2_oDpykmuhrSIjAT4tNB1EcV_2OS3eVYVWbpUQPhMXGAIwcsaww6y14Cn8OEu1kRwJE4UUqIrtIo2i2VkSWcCghjOhritNihZoFbjamxDmLdw9SD9clADr-uZC4KVNzalhbjWKK1ggibbRaYNUXGYrOQn9XQNHyGmNvGReA9Mu6tbOJvmoEqM14amebkd0iA8HHi9kPeTr5rCAMwYYTxzarx_5DIax1fQNe9Z1TmaN4dWVxABxEb5ZpJzQ6Yuu8tat8fX8WQBeoSFkS406pvXL8vpKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d31c79e4.mp4?token=gJIr5iz0d3uwGalxn8YY6f1KymAnPNNukTHoaQhpOXsHtcL_hQf6HLiNSqT2_oDpykmuhrSIjAT4tNB1EcV_2OS3eVYVWbpUQPhMXGAIwcsaww6y14Cn8OEu1kRwJE4UUqIrtIo2i2VkSWcCghjOhritNihZoFbjamxDmLdw9SD9clADr-uZC4KVNzalhbjWKK1ggibbRaYNUXGYrOQn9XQNHyGmNvGReA9Mu6tbOJvmoEqM14amebkd0iA8HHi9kPeTr5rCAMwYYTxzarx_5DIax1fQNe9Z1TmaN4dWVxABxEb5ZpJzQ6Yuu8tat8fX8WQBeoSFkS406pvXL8vpKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
لحظة تنفيذ غارة صهيونية على بلدة تفاحتا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/78531" target="_blank">📅 19:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78530">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭐️
طيران مسير من لبنان يهاجم مستوطنات الشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/78530" target="_blank">📅 19:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYdWqaHQ1gR65JSUuWHrnFUnvT4ecPYWL8UNZEj7gDoiPoqkzLRtao_K6uhPYDKddsxxcu-nzgyqAlEqSW6xX4-SEsjP82krOKEC9d1y0l6fwxEd2aYe86IiWE8VSI8vT9eNowu2ffzCiF0fNlfIm6wN78Uoj5ike4xAuz-dex59SYdqp0w37rEO3KBcKH_mrHojRm6AITILrSF_3tQ4-SRRsUgQNfDOztu2khA1ESGcXDCoxtO3PCXhwpAP8nSfmDQr36uaN_iZi6eMfUtAZRfdcrJeny4t-81xnVoxX02LkAK6qTHCSDp9JVSRlTYJIyb-HREF85ASUuul920NFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي: لم تكن مذكرة التفاهم في إسلام آباد أقرب من أي وقت مضى. في انتظار إتمامها، يجب على وسائل الإعلام الامتناع عن التكهن بمحتواها. تماشياً مع نهجنا المسؤول والشفاف، سيتم مشاركة جميع التفاصيل مع الجمهور في الوقت المناسب</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78529" target="_blank">📅 19:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nw5son4Syg9AqYsba82wotIvAc2JebD1ooZ-2vmkuxKMETRn62kuNzelz3TxuAOavDTsUOfO-OAxYN3BGRpBs_SDIZ2gOOoe1gNlVybYYQrlEMGCldLo2hXlQRrfqTtnd4xXoPlcxxVLR8NzC0aPVVhVlO0gTR5P-HzvcWtEthG-NGOrNVseiWUQ2EDv-Kse-NvxR4jGfuh57mUrGKd5PoCbEkZrDcU7LeQOeKFCtjPnAg8V8SgbBr9OQNzPTNMBScYiZrj4lVJ4va6TQzqH6WXrMopl3SKGvMrm7WQYAO96B7GTLhle8sNtPdp4r1ur7p-Lsbnk4hKl4wzHf-AkIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
نائب الرئيس الأمريكي "جي دي فانس":
أولاً، لا يحصل الإيرانيون على أي أموال نقدية، ولا يتم إطلاق أي أموال مقابل مجرد توقيع اتفاق أو حضور اجتماع.
الاتفاق مُصمم لضمان إعطاء الأولوية لمخاوف الولايات المتحدة وحلفائها، وإذا امتثلت جمهورية إيران الإسلامية لالتزاماتها، فستتدفق المنافع الاقتصادية عليها وعلى المنطقة بأكملها. هذا الاتفاق لديه القدرة على إعادة صياغة المنطقة وإدخال سلام دائم.
لقد لاحظت بضعة أشياء غريبة في التقارير خلال الساعات الأخيرة. أولاً، الأشخاص الذين (بشكل صحيح) قالوا إن دونالد ترامب كان رئيسًا تاريخيًا قبل شهر، يقومون الآن بانتقاد اتفاق بناءً على تقارير إعلامية غير مؤكدة. ثانياً، الأشخاص الذين يقولون إنه لا يمكنك الوثوق بأي كلمة يقولها الحرس الثوري الإيراني والذين يبدو أنهم يؤمنون بمشاركات وسائل التواصل الاجتماعي من مصادر مجهولة.
الرئيس سيحصل لنا على نتيجة جيدة، بطريقة أو بأخرى.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/78528" target="_blank">📅 18:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
وزير الطاقة الأمريكي:
يمكن أن يكون هناك رفع جزئي للعقوبات عن إيران ضمن التنازلات التي نقدمها.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/78527" target="_blank">📅 18:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jF9bBtbAGWYgype1HcYIikAsqEY2m9GQ35tClDpYOiUXd9YltLx0nWhV7wwf3Tq6Jcm2zOv7i92VNzatKo2Q1nWTqo1U2_5m5NlAupFCH8mAD6cvNElKA_1RvvqGQMwU7MQYlIOVzo6TrgS8WdUCKhLzQbTxJ30dijXv7tobiSE9tjPGELSBNO46gwM38gR56XvWWqRKWyJ__S1TLB4znD_P7QQJfA-vy8nnFVfCg2xA1CDAW1nrE3J1jENV74yOjt4lNqVNcsmLDLnePmmUVdASKFV-Swbd2lIAAw2BtGuyefi8zgQdRa5D5em6ZcCbDbDMKDYQKGdZmZDLjZge8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:
لم تكن مذكرة التفاهم في إسلام آباد أقرب من أي وقت مضى. في انتظار إتمامها، يجب على وسائل الإعلام الامتناع عن التكهن بمحتواها. تماشياً مع نهجنا المسؤول والشفاف، سيتم مشاركة جميع التفاصيل مع الجمهور في الوقت المناسب</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78526" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني: رئيس الولايات المتحدة يقود هذه الأيام نحو اتفاق مع إيران من منطلق رؤية المصالح الأمريكية ونحن نتوقع أن يلتزم بمبدأ منع ايران من الحصول على النووي ومبادئ أخرى في مجال الصواريخ ووكلاء الإرهاب ويجب على إسرائيل التأكد من أنه في المستقبل…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78525" target="_blank">📅 18:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني:
رئيس الولايات المتحدة يقود هذه الأيام نحو اتفاق مع إيران من منطلق رؤية المصالح الأمريكية ونحن نتوقع أن يلتزم بمبدأ منع ايران من الحصول على النووي ومبادئ أخرى في مجال الصواريخ ووكلاء الإرهاب ويجب على إسرائيل التأكد من أنه في المستقبل سيكون لدينا القدرة على العمل بشكل مستقل لمنع إيران من الحصول على سلاح نووي.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/78524" target="_blank">📅 17:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اعلام العدو: محاولة اغتيال في ام الفحم.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78523" target="_blank">📅 17:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🏴‍☠️
انفجار سيارة في ام الفحم شمالي الكيان وتسجيل اصابتين كحصيلة اولية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78522" target="_blank">📅 17:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🏴‍☠️
انفجار سيارة في ام الفحم شمالي الكيان وتسجيل اصابتين كحصيلة اولية.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/78521" target="_blank">📅 17:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">📱
خلل يضرب تطبيق الفيسبوك في العراق وعدد من دول العالم يتسبب بتوقفه.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/78520" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr80r-pP-DWepUdXveK0aqbitxQfQ8TsyduOeUY3gnM8jNhiSbza0-dhcMsegClZEA4HCjNpWUGLtyhXVZvqnqLpitztzOqBTcpV23f2BGP11c4qm1WRuOZaRYGuDERsHNVoLCIF_zi5DmzYWbxgHv3-S-h_HxZxWZUKW46SECkcaFxJGGr35esqU5D8a_wdXxQb_9E23g2SHDqdFmWrityOEfU4z9lK-9XPu5YzZaCefk4sMO-b3b98gY1R63GWPF4ckB_AcgYgFTvqtfbyElfwXoqyxHnBwXH4N8HhxDrOx7fpE8y54afWdb14V4O9BcKRdILnQtL7DGYnSn1EPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب مغردا:
الشروط التي سربتها إيران إلى وسائل الإعلام الكاذبة لا علاقة لها بالشروط المتفق عليها كتابيًا. ما قالوه، بما في ذلك بيانهم الضعيف والمثير للشفقة بشأن وجود اتفاق، لا يمت للحقيقة بصلة. أشخاص غير شرفاء للغاية في التعامل معهم. لا يوجد معهم شيء اسمه التعامل بحسن نية. أمر مذهل! كما أن هجومهم الذي تم رفضه تمامًا بطائرات بدون طيار الليلة الماضية على السفن الهندية المغادرة لمضيق هرمز غير مقبول على الإطلاق. من الأفضل لهم أن يضبطوا أوضاعهم، وبسرعة!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78519" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78518">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية جرّافة (D9) تابعة لجيش العدو الإسرائيلي عند الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/78518" target="_blank">📅 17:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
جهاز الامن الوطني العراقي يعلن إحباط مخطط لاغتيال رئيس جهاز الأمن الوطني وعدد من الضباط كانت تقف وراءه خلية مرتبطة بما يسمى "التجمع الوطني العراقي للتحرير والتغيير" إحدى واجهات حزب البعث المحظور بعد جهد استخباري شمل الرصد والمتابعة والاختراق.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/78517" target="_blank">📅 16:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78516">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
اخلاء 3 جنود من جنوب لبنان.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78516" target="_blank">📅 16:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78515">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📰
‏مصدر غربي لرويترز: من المرجح أن تستضيف جنيف مفاوضات الاتفاق بين واشنطن وطهران.. إيران تتمسك بموقفها المطالب بإنهاء القتال في لبنان</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/78515" target="_blank">📅 16:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
وكالة فارس عن مصدر مُقرّب من الفريق الإيراني المُفاوض:
إنّ الادعاءات التي أطلقها ترامب وبعض وسائل الإعلام الأجنبية بأنّ "الاتفاق قد تمّت صياغته النهائية ومن المُقرّر توقيعه في جنيف يوم الأحد" عارية تمامًا عن الصحة، في الأساس، لم تُستكمل بعد عملية المراجعة واتخاذ القرار في إيران، وبالتالي فإنّ الإعلان عن يوم الأحد ومكان جنيف يُنفى تمامًا.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78514" target="_blank">📅 16:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78513">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">📰
‏
مصدر غربي لرويترز:
من المرجح أن تستضيف جنيف مفاوضات الاتفاق بين واشنطن وطهران.. إيران تتمسك بموقفها المطالب بإنهاء القتال في لبنان</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78513" target="_blank">📅 16:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78512">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇱🇧
كتلة «الوفاء للمقاومة» التابعة لحزب الله:
المفاوضات المباشرة التي انزلقت فيها السلطة لردم هوة العداء للكيان الصهيوني أدت إلى مزيد من الانقسام الداخلي بين اللبنانيين، الإصرار على المضي في هذا الخيار يشكل مكابرةً غبيةً تصبح معها المفاوضات انتحاراً سياسياً مجانياً لن يحقق شيئاً، الحل يقتضي عودة السلطة عن خياراتها العدمية هذه والابتعاد عن خطاب التحريض والكراهية وعن استعداء غالبية الشعب</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78512" target="_blank">📅 15:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78511">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBEmiylFhxph2RrFQVlAREJWPFu65KlSn3aG-ZItU4qnxN81mJURG0jYMe4AT5LG2RL_4Vn9eh3AthhmcbejDPJRVhi6cAoYrWKcD7i5r79yV35zWfPsTk7fUIVC9ulI3XzcCJbbU4MUk9fMvY4Fk1I9U5-xfeIr9c6xYSYBLAxHL9cZCnwbAFf12ztvXJIXMaCPvdtyFgqwDx3sJOPdtOLXq_Pq1r8cPZEIFCoYKF2l_fjqWG31jy-tZQWpBxvRdLcvyXOBwImWqQXJco4-oXzAhnZR4gfTAGxqypzWvQWtjEC_gsuF8nHUGjEzB7GuxJt1INdQVkqq6VbIUgG7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
اكثر من 100 الف مشارك الان في مسيرة الفروخ (المثليين) وسط تل ابيب.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/78511" target="_blank">📅 15:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">📰
شبكة CNN:
مصدر إسرائيلي مطلع يقول إن إسرائيل تضغط على الولايات المتحدة بعدم الإفراج عن أصول إيرانية مجمدة كجزء من مذكرة التفاهم</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78509" target="_blank">📅 15:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية تصدّي المقاومة الإسلامية بتاريخ 05/06-06-2026 مربض المدفعيّة المُستَحدث التابع لجيش العدو الإسرائيلي في بلدة العديسة جنوبيّ لبنان بصاروخٍ نوعي ومسيّرات انقضاضية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/78508" target="_blank">📅 15:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏴‍☠️
‏نتن ياهو:
إيران تسعى لتدمير دولة اليهود وأنا أكرس حياتي لمنعهم من القيام بذلك ولن تمتلك إيران سلاحا نوويا في عهدي</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78507" target="_blank">📅 15:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78506">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وكالة إرنا: النص الحالي لا يشمل عبارة "تمديد وقف إطلاق النار" بل إنهاء الحرب تماما بكل الجبهات.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78506" target="_blank">📅 14:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وكالة إرنا: على عكس ما يتداول إعلاميا فإن إيران لن تلتزم بإعادة أوضاع مضيق هرمز لما كانت عليه.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78505" target="_blank">📅 14:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78504">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
وكالة إرنا حول تفاصيل الاتفاق المحتمل بين إيران والولايات المتحدة: تم إعداد نص اتفاق إنهاء الحرب بعناية فائقة ودقة متناهية ولا مجال لأي تفسير تعسفي أو تهرب من الالتزامات من جانب أي من الطرفين في هذا الاتفاق، لن يتم التوصل إلى أي اتفاق بشأن الملف النووي في…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/78504" target="_blank">📅 14:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78503">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
وكالة إرنا حول تفاصيل الاتفاق المحتمل بين إيران والولايات المتحدة:
تم إعداد نص اتفاق إنهاء الحرب بعناية فائقة ودقة متناهية ولا مجال لأي تفسير تعسفي أو تهرب من الالتزامات من جانب أي من الطرفين في هذا الاتفاق، لن يتم التوصل إلى أي اتفاق بشأن الملف النووي في مذكرة التفاهم الحالية ولن تقدم إيران أي التزامات جديدة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78503" target="_blank">📅 14:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78502">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اعلام العدو الصهيوني:
تنازل امريكي جديد لايران.. الولايات المتحدة تمنح شبكة beIN Sports إعفاءً من حقوق بث مباريات كأس العالم في إيران.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/78502" target="_blank">📅 14:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78501">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">📰
فاينانشال تايمز:
تقييمات المخابرات والدبلوماسيين الغربيين تعتقد أن طهران احتفظت بجزء كبير من ترسانتها من الصواريخ ومنصات إطلاقها وبنيتها التحتية السرية. ويُقال إن العديد من المنشآت أُعيد فتحها أو إصلاحها في غضون ساعات أو أيام.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/78501" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78500">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
وكالة مهر الايرانية للأنباء تنشر بنود الاتفاقية التي سيتم توقيعها
:
1- وقف فوري ودائم لإطلاق النار على جميع الجبهات، بما فيها لبنان
2- التزام الولايات المتحدة بعدم التدخل في الشؤون الداخلية لإيران واحترام سيادة الجمهورية الإسلامية الإيرانية
3- رفع الحصار البحري بالكامل
4- التزام الولايات المتحدة بسحب قواتها من محيط إيران
5- إعادة فتح مضيق هرمز خلال 30 يومًا بالتنسيق مع إيران
6- تعليق العقوبات المفروضة على بيع النفط والمنتجات البتروكيماوية، ومنح إيران حق الوصول الكامل إلى مواردها المالية
7- تقديم الولايات المتحدة وحلفائها خطة لإعادة إعمار إيران بقيمة لا تقل عن 300 مليار دولار
8- 60 يومًا من المفاوضات للتوصل إلى اتفاق نهائي قائم على الملف النووي والرفع الكامل للعقوبات الأولية والثانوية، وقرارات مجلس الأمن الدولي. مجلس محافظي الوكالة الدولية للطاقة الذرية
9- إعادة تأكيد التزام إيران بموجب معاهدة عدم انتشار الأسلحة النووية بعدم إنتاج أسلحة نووية
10- خلال المفاوضات، تعهدت الولايات المتحدة بعدم زيادة قواتها في المنطقة وعدم فرض عقوبات جديدة على إيران.
11- الإفراج عن 24 مليار دولار من الأموال الإيرانية المجمدة خلال فترة الستين يومًا للمفاوضات النهائية، على أن يُتاح نصفها لإيران قبل بدء المفاوضات.
12- إنشاء آلية مراقبة لتنفيذ الاتفاق.
13- سيتم إقرار الاتفاق النهائي بقرار من مجلس الأمن الدولي.
14- لن تبدأ المفاوضات النهائية قبل الإفراج عن نصف الأموال الإيرانية المجمدة، وتعليق العقوبات المفروضة على النفط الإيراني، ورفع الحصار البحري. وسيقتصر الاتفاق النهائي على مصير المواد المخصبة وتخصيبها، ورفع العقوبات، وخطة إعادة إعمار الاقتصاد الإيراني، مع استبعاد مناقشة برنامج الصواريخ الإيراني ودعم جماعات المقاومة نهائيًا من جدول الأعمال.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/78500" target="_blank">📅 13:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78499">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
وكالة تسنيم عن مصادر:
لم يتم بعد اعتماد نص الاتفاق حتى الآن من قبل الجهات المختصة في إيران. حاول ترامب خلال الأيام الأخيرة بدء الضغط والتهديد والإجراء العسكري، ومن خلال وسيط قطري الضغط من جهتين لتغيير مواقف إيران، لكن في النهاية لم تقبل إيران التغييرات الجديدة</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/78499" target="_blank">📅 13:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
مشاهد من المحفل التأبيني السنوي لذكرى مجزرة سبايكر في محافظة صلاح الدين شمال العراق.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/78498" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📰
بلومبرغ تقول انه قد يتم توقيع الاتفاق بين طهران وواشنطن في جنيف يوم الأحد المقبل.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/78497" target="_blank">📅 13:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وسائل اعلام خليجية عن مصادر:
إيران هي من طلبت توقيع الاتفاق مع أميركا في دولة أوروبية لمنحه طابعا دوليا.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/78496" target="_blank">📅 12:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78495">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇩🇪
إلغاء رحلات من مطار هامبورغ في ألمانيا وإخلاء المنطقة الأمنية حوله بعد على العثور على طرد مشبوه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/78495" target="_blank">📅 12:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78494">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYkAlDP6gwmv4Gi38zi-8vS2JZ3MFuWRzvnNSmgVytghfymRnQbAZH2sKajOsOJgjWT-DVGFbik6QOxIodFmZNbggnJX6Ao4I2YveJF9etylH-2hjwrLeJaaHcO0mV-njcn4_dIMQrY0czbHyKkFR3MwKksTfjHEcBKdnVOqmvKilDWaeABDERMd5pgvIhSvdpT2wRRe-OD8WchwAun3zEYciwcZNli-9xdL5aXlzmgh5hhfbpRk22PRijVv374LecB2zrAk7VOd14w8VL-325wFf7O8CWLM3_BuSe-uA2hE8KunlrOhJr85xOk6yok071nzscALR2u5CsCDPDEN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ اعتراضية في كريات شمونة دون تفعيل صافرات الإنذار</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/78494" target="_blank">📅 12:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/631780cade.mp4?token=YDATppCAR_1JVLa6zs4zvMG53ogNCVI35GndxRUC1RS5zlFTquIrEzuwqgmIm948LEhbDgFvDNxMdc_BYYQV2AJ1ZvIgm7SxV9oErHq6oQ5jbkln7DGx3o5DcCEbgwmsv-wB82g1gAlRveYzUgnDTHVB8FJHdcwaes3z0Obj5v2JcBQ-z4Lzl2ceuZk-TH4tlTVQy65pb8O4P1ey8szdYxkNd_Wu_yhCmOjdIsR9xDuVK4txb2Jf_T3BSIgQScf3emzZzyWfwXf6oWfSWncZGvUn3ewz1G2p7sD2NVFLdsz9WnSl96cudcIEax4bBRxjklCyoqOIiOTRlyePgsFJyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/631780cade.mp4?token=YDATppCAR_1JVLa6zs4zvMG53ogNCVI35GndxRUC1RS5zlFTquIrEzuwqgmIm948LEhbDgFvDNxMdc_BYYQV2AJ1ZvIgm7SxV9oErHq6oQ5jbkln7DGx3o5DcCEbgwmsv-wB82g1gAlRveYzUgnDTHVB8FJHdcwaes3z0Obj5v2JcBQ-z4Lzl2ceuZk-TH4tlTVQy65pb8O4P1ey8szdYxkNd_Wu_yhCmOjdIsR9xDuVK4txb2Jf_T3BSIgQScf3emzZzyWfwXf6oWfSWncZGvUn3ewz1G2p7sD2NVFLdsz9WnSl96cudcIEax4bBRxjklCyoqOIiOTRlyePgsFJyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ اعتراضية في كريات شمونة دون تفعيل صافرات الإنذار</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/78493" target="_blank">📅 12:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">صفارات الانذار تدوي في غلاف غزة</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/78492" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صفارات الانذار تدوي في غلاف غزة</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/78491" target="_blank">📅 12:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxhNr7LrlyzGFA20TXwzWW-OD8GTYZ-tgoML6s0a31ck329rdeYjlacJegxZzOCVqYaXsu8V2HBe3BbjRqw92M4KNlYpSNrlXfUm62swOFOOrzh1BVZ-UL-tp2E1rH1R9lbUWLUMaxK5WgAVHkeOZeGJPzEN5wbAtrA-h0hxQullr2Q0kR6t3bHA8nfL4KuvFxdSvyP8f9l_ezGCt97aYgC_MAyY1G5YWwGR9ZeoVf1mPIGHQvYcCBQqzhzVHuxHyN6uXo5xBUY4RMWrkKrcxx2_seYi4wFYbZoQIen07kkUrG0KmKfvWf9ou7JPG3r3qezi-NsqNhoYQjN8A_fM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇱🇧
🏴‍☠️
سلسلة من الغارات الصهيونية استهدفت بلدة البياض في قضاء صور جنوب لبنان.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/78490" target="_blank">📅 11:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇹🇷
🇸🇾
مصادر إعلامية تابعة لحكومة الجولاني: ازدياد الخلافات بين الجولاني وداعميه.. أردوغان يطالب الجولاني بعدم الرد على ترامب والدخول في معركة لبنان دفاعاً عن إسرائيل.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/78489" target="_blank">📅 11:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPVV2R60NHzAKLN59xix09vFOJFMQ6pU_B5vVWGbnQoJ0NJur2IHPpwur3DNPxS3UsE_SiLKPwIWETeSOZCowRbTey2KrWgtTUl6avBALEEM3NDeVxLmHCzucsIyUJJkhCPzZqMi0xc5VPayxA-MZkV-n9C08iW9s92MJG4IYgJTDfYqJtBK3sWeDpCiCb_tTIBWSR87kJmGzXu0ahY5CSPhufcKTjLJoX1f3SadRoCo_Lyi4QvtIVIRNKhYPHdsisdAzQWAGwNepxp9isUR2HWMS1Gsor68fZZQmL_AqLmvEXS2_hVVh57h1ulu78Hf18apZSxjHzjGNxuOUhjSkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الخارجية الأمريكية لمواطنيها : لا تسافرون للعراق الوضعية داچه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/78488" target="_blank">📅 11:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇹🇷
🇸🇾
مصادر إعلامية تابعة لحكومة الجولاني: ازدياد الخلافات بين الجولاني وداعميه.. أردوغان يطالب الجولاني بعدم الرد على ترامب والدخول في معركة لبنان دفاعاً عن إسرائيل.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/78487" target="_blank">📅 10:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏴‍☠️
إعلام العدو عن مصادر: نتنياهو قال إنه أكد لترمب تفهمه لسعيه لاتفاق مع إيران لكن يجب ألا تكون إسرائيل الضحية</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/78486" target="_blank">📅 10:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78485">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64e8806f6a.mp4?token=gk2wtEcetPkbGjKf1QuqvDlxM4AQmqb5WBGVM3VDrar7IeeOGJ0jeRBktxWgZoERH0e5BO2culfITO4zy1Mxi2WIiKHgEKujmAX0jKphypqLpTbk_MqbYNt4wOQzG6UVNdLm71asTesISXilOCHm89bCsOAjbgts0vaHCfSgrCKosg3odAoDlU1kzLvAI1zn3ONp2dLwr_QKYZPfqGw28a6dyAMtV12-d-7IRIsg1aL1xtjk4y-NKnTcz8hbVWohMoIcanVOibG_0QDzIPIRcsubtzaEFx85ZgPW60awSgeb8HnfxA-0Mp3illbXkZuBYxLUEFmBx6tD8V0oCehRTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64e8806f6a.mp4?token=gk2wtEcetPkbGjKf1QuqvDlxM4AQmqb5WBGVM3VDrar7IeeOGJ0jeRBktxWgZoERH0e5BO2culfITO4zy1Mxi2WIiKHgEKujmAX0jKphypqLpTbk_MqbYNt4wOQzG6UVNdLm71asTesISXilOCHm89bCsOAjbgts0vaHCfSgrCKosg3odAoDlU1kzLvAI1zn3ONp2dLwr_QKYZPfqGw28a6dyAMtV12-d-7IRIsg1aL1xtjk4y-NKnTcz8hbVWohMoIcanVOibG_0QDzIPIRcsubtzaEFx85ZgPW60awSgeb8HnfxA-0Mp3illbXkZuBYxLUEFmBx6tD8V0oCehRTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد من المحفل التأبيني السنوي لذكرى مجزرة سبايكر في محافظة صلاح الدين شمال العراق.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/78485" target="_blank">📅 09:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78484">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: الجيش ليس قريباً من حسم المعركة مع حزب الله</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/78484" target="_blank">📅 07:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78483">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">📰
أكسيوس عن مصدر: مذكرة التفاهم بين واشنطن وطهران ستمدد وقف إطلاق النار لمدة 60 يوما بما في ذلك بلبنان
مذكرة التفاهم بين واشنطن وطهران تتضمن إطارا للتعامل مع مخزون إيران من اليورانيوم المخصب
ستجرى مفاوضات نووية بين واشنطن وطهران خلال فترة وقف إطلاق النار.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/78483" target="_blank">📅 07:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78482">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">صفارات الانذار تدوي في مطلة شمال اسرائيل بعد اطلاق رشقة صاروخية من حزب الله.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/78482" target="_blank">📅 05:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78480">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9CqOTwmt7Xi58fKvEKsAKFiFq2UHDg0XKBzlJLmB7GrwvTN45gY9QfSnmLs6J1vUvCw_wS5ANCS95YL8P3i4gXG_L5Vqs-tWFzmv9vtQm5HLX9QANHzi5grXryM4kd6Wa2rHOeX2obs2XLwabL8LA8LzGeOtW4iebuvpI_0Ng5to5qbvqQoR01PMPyzG-T8WPvJ74ckjNARn7mmAHKgIxlCQLqeB81DeECYyfdbkZSgZmCGCnUDwItLufEGL0iByIeS0Ksf6aqqRZmpMmDR1t53SYaaWFGWOQSJSrnD739FIfR-1Nw5X9QRCA_jKNNV6D5WCzKIv0X8n7syK6tWEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SE9GaSpb96rTEdG46UUHoYhqmylxhfCV0mqxJsA_2sLDfmvPz0rStpOCWwnlRNT5taZW7OnGrhlYxxF2Q6MQ_CRHH0wq6vpxoRAy53J_TEskCVXeXb-LwT8eQ6yiTzidqQ-aFMdWEKdM3721Eb-tvIVkSLxk_HB8UskJV2R6ZV4-D8BVtByvhoa_zsSWu8tV3nQWQuro-sLNLMSXKrrlJHP3dxypEctiaXJJNrEqzMI4nTothD2zcKHrRm0-S4Uawrk7EkUzf8daxL3YzmYoYvjh-QAh99zj-1f5xvpaOis6S3PPf1UVloLbRU5F1LewT7GYnZUVDbdlKciLTChlmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇳
الخارجية الهندية: 3 سفن هندية تعرضت لهجمات نفذتها البحرية الأمريكية.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/78480" target="_blank">📅 04:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78479">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
زلزال يضرب مدينة كهنوج الايرانية بدرجة ٤.١.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/78479" target="_blank">📅 02:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78478">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
الحرس الثوري الايراني يمنع مرور سفينة من مضيق هرمز كونها لا تمتلك تصريح مسبق.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/naya_foriraq/78478" target="_blank">📅 01:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الاصوات المسموعة في سيريك سببها اعتراض سفن في مضيق هرمز.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/naya_foriraq/78477" target="_blank">📅 01:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdS4fQA6WKaIwKKA5CBetfgdmWXXHchGdTsBA_OYJxFiaQppqe0tkS49zjgsOonreJmjm5m6e2xSa8e-mpIZNhHxs-NxabJVmAn6XnmGURjFeWoWR-fWRj9D6Aj-SZV48SlUI94YFIgRhF-SqeXpU0_KeJ74I5g2PWaeIvTIz-cEgQIZSl9CpTRKz86NFcKivf5GBaXRXFCanuLEZm8HZgmw6WPDeMdhyRdmfKwRBsRa6r7HEsB_lieLq4o9s4_-g73x0WuH4J3-Cct48TSlA_IuTYwCpN2Hw7M8l93KH6fbRgHjjPo6zbm5Gm1D9l9OWJ_wXqOjb8euDfRTKNPBDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرئيس الأمريكي ترامب:
هذه هي الأسلحة التي نستولي عليها من الكارتيلات المكسيكية. إنهم يقتلون آلاف الأمريكيين كل عام! الرئيس دونالد ج. ترامب.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/naya_foriraq/78476" target="_blank">📅 01:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3yCNITkP3b8ysO6QZPxK1aOXFhI67fwSBJARkASAxtrfp0L7HaLuaqeTyv8UUmnliYxMC02U-ZXx71juExCH0rU4yhSRWGBLSJSElDlUmdT98XCcTvg_LOmqyi7mkkMo72HNxhwc0JQBuLhl6EJr2xUXfb7L1TF56z-PWKbi34XFpQfyndwbQcr2XicSdYcuCEZ69LGkUQbKgWGExNwVffAzFDf0SqyEqhweZ8F4UAac75-qUYYxgqEEyAhp1n0hu37KdYRCM-D9jseV02ceYoI45K0FEcN7EZSvoTs74P51FWkQWebQvnxzjNnS_FR1ctsEhDSvXxTjTjMZKe8og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة حربية من نوع F-35 تطلق نداء استغاثة فوق ابو ظبي لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/78475" target="_blank">📅 01:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78474">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجارات مستمرة في سيريك من الممكن تصدي لسفن لم تلتزم بقوانين الحرس الثوري.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/78474" target="_blank">📅 01:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78473">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
انباء عن انفجار في سيريك الايرانية.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/naya_foriraq/78473" target="_blank">📅 01:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78472">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
انباء عن انفجار في سيريك الايرانية.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/naya_foriraq/78472" target="_blank">📅 00:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78471">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLv_E-4NeWiXiWDud8MXnK4T0WFqMapUObWfPzdjgPwMxmXR4izyupBYkns1bWWYQAHVXfx4_tclvtN3zrjsSTU1zKg7IMKA10y_LUqOCk0Po1FsU8ymKghaXjU-p-oDWeP69G3oocjdAZj5-DotGcD0i5vOtQnIwErh4xvzcyPmXk0TFcogz6hYomd8w47Q-nvPWJALxEzA01t3_jIojuxvuOlIq-Geq6fz5P1v08_lwDaCL8OPV7__rmBD6nMSKUImsfAcxTNJfF37W7UBFGndf1fcC7gmKxbcJZM80SYVqTWvl5SjLzTKVziKqsjswjAIp5eahdVKlvyw0kfZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
إسماعيل بقائي:
إن الهجمات الأمريكية الوحشية على السفن التجارية الهندية، والتي أسفرت عن مقتل ثلاثة مواطنين هنود على الأقل، تُعد دليلاً واضحاً على سياسة أمريكا المستمرة المتمثلة في السطو المسلح والقرصنة الحكومية.
‏نتقدم بأحر التعازي إلى عائلات وأصدقاء البحارة الهنود الذين سقطوا، ونقدم خالص تعازينا للشعب والحكومة الهندية.
‏يجب على المجتمع الدولي محاسبة الولايات المتحدة على سلوكها الخارج عن القانون، والذي لا يزال يهدد السلام والأمن العالميين ويعرض حرية الملاحة للخطر.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/naya_foriraq/78471" target="_blank">📅 00:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78470">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⭐️
أكسيوس عن مصدر:
نتنياهو لم يكن لديه أي إشعار مسبق وفوجئ عندما أصدر ترمب بيانه الأولي بشأن الاتفاق مع إيران.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/78470" target="_blank">📅 00:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78469">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: الاتفاق مع واشنطن لم يصبح نهائيا بعد.  روايات الجانب الأمريكي هي لإظهار أن إيران تراجعت عن مواقفها تحت الضغط والتهديد.  نص التفاهم جاهز تقريبا.  الوسطاء ناشطون الآن وباكستان وقطر فاعلتان في الوساطة.  إيران أثبتت أنها لا تتهاون في ما حددته…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/78469" target="_blank">📅 00:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78468">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: قلنا سابقا إن أكثر نصوص الاتفاق كانت محسومة لكن الجانب الأمريكي كان يريد إضافة مطالب جديدة.  المراجع العليا ستقوم ببحث جميع بنود أي تفاهم محتمل وسنعلن موقفنا في وقته.  ما يجري الحديث عنه بشأن زمان ومكان توقيع الاتفاق تكهنات إعلامية.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/78468" target="_blank">📅 23:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78467">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
قلنا سابقا إن أكثر نصوص الاتفاق كانت محسومة لكن الجانب الأمريكي كان يريد إضافة مطالب جديدة.
المراجع العليا ستقوم ببحث جميع بنود أي تفاهم محتمل وسنعلن موقفنا في وقته.
ما يجري الحديث عنه بشأن زمان ومكان توقيع الاتفاق تكهنات إعلامية.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/78467" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78466">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🏴‍☠️
‏
نتنياهو:
على الرغم من أن إسرائيل ليست طرفاً في المذكرة، فقد أعربت عن تقديري لالتزام ترامب بأن أي اتفاق نهائي سيشمل إزالة المواد المخصبة، وتفكيك البنية التحتية للتخصيب، والحد من إنتاج الصواريخ، وإنهاء دعم إيران لوكلائها الإقليميين.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/78466" target="_blank">📅 23:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78465">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/994003fdaa.mp4?token=ixmGwJppmgmPHLhvvbKyQzUDiiULVT79s3RHbQs1qpOzHjC5UdOE8IEnsFntsV8pd2RaVaBsiVNTbQKE6NGXvWIM7MgH9TYKMQeCihtQ4U29XnshPHL1HqJbCOLyPdbK57c5fT0L3P3BVTB1K1P9umK1fCEpvfDZifDXs-zhB2FlPGmeTSkdL14a9_Zl60cJNP-raAxuTBJIK19Rhl14MVJcMXg_XaUvI_r8lSINO-41xB4EKYV2tfbJrHDhcZuiGPeCzL8X1w7pmlq6Jvsi54WUwpq4kVqWAFgSAga-VoahpkXUI8aI7Xxty3L-VcWMy_ejbsfFNoybCym9NOVk2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/994003fdaa.mp4?token=ixmGwJppmgmPHLhvvbKyQzUDiiULVT79s3RHbQs1qpOzHjC5UdOE8IEnsFntsV8pd2RaVaBsiVNTbQKE6NGXvWIM7MgH9TYKMQeCihtQ4U29XnshPHL1HqJbCOLyPdbK57c5fT0L3P3BVTB1K1P9umK1fCEpvfDZifDXs-zhB2FlPGmeTSkdL14a9_Zl60cJNP-raAxuTBJIK19Rhl14MVJcMXg_XaUvI_r8lSINO-41xB4EKYV2tfbJrHDhcZuiGPeCzL8X1w7pmlq6Jvsi54WUwpq4kVqWAFgSAga-VoahpkXUI8aI7Xxty3L-VcWMy_ejbsfFNoybCym9NOVk2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لا أريد تحديد مهلة للتوصل إلى صفقة مع إيران.
😆</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/78465" target="_blank">📅 23:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78464">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf0cf36cd.mp4?token=b6Fhg5i1jtmyr6EaeQq9zYBrlhhriD9xv3E0Rqa_Osfjl8Erd-opngELOSRGz8yjaC5BPQ4MX2jq9dZ4-zP_djoqjAo7vuQB8wofmHRoV-vMAzA1IZBK0T4dGhvZiZ72UFzi5KrXK5o5RYBl8gxxHimSv8sMGElqDlAYsqJ15cCYhkRABsUULSNr1wA9p0YjBEK80Vk5fFszSpdjKt4yPb_U6JmUu4b9ByJaePkgyeIwgV4ukpFB6DJTmTpLvHcVCYdeMAOwY6NwInbTXXOsHLO_vRVKN8Sbpdey_xiEN6jIwqbdo7dWw3ILUkVaKHZANO1tImJam2CRQGxgl-OmBabj4SOgOH18fBVnla48lVTI2Z883MPVkFXKBnm3Exfh4TBsrfG8ilQtLqJAWVTd35KbyX38KJaa8Zb41DWrVS5EgmgHXP61t2cKh_R8_h3jBuk0csvNmbdty3mC_bi9qmjmnOuA1ByS9cO1PtZmI5-9rkn3mZKQqVw28vzopyvmDm8oQeByNSweB8adYQALWtYpvaC_DQWvCHL53-rzJchQkNiN7TefEzrazHQh0sEV0ye8fACp9bUdhGeiyfeTg_eBoxsNPn3WQ_kfFXRTSWlrDYa4lCbw-dixJDjaDnfJlWsR4IqtEJIOa32RH5ARYeC1ZmaEKx-Lkly6uMzk_Lk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf0cf36cd.mp4?token=b6Fhg5i1jtmyr6EaeQq9zYBrlhhriD9xv3E0Rqa_Osfjl8Erd-opngELOSRGz8yjaC5BPQ4MX2jq9dZ4-zP_djoqjAo7vuQB8wofmHRoV-vMAzA1IZBK0T4dGhvZiZ72UFzi5KrXK5o5RYBl8gxxHimSv8sMGElqDlAYsqJ15cCYhkRABsUULSNr1wA9p0YjBEK80Vk5fFszSpdjKt4yPb_U6JmUu4b9ByJaePkgyeIwgV4ukpFB6DJTmTpLvHcVCYdeMAOwY6NwInbTXXOsHLO_vRVKN8Sbpdey_xiEN6jIwqbdo7dWw3ILUkVaKHZANO1tImJam2CRQGxgl-OmBabj4SOgOH18fBVnla48lVTI2Z883MPVkFXKBnm3Exfh4TBsrfG8ilQtLqJAWVTd35KbyX38KJaa8Zb41DWrVS5EgmgHXP61t2cKh_R8_h3jBuk0csvNmbdty3mC_bi9qmjmnOuA1ByS9cO1PtZmI5-9rkn3mZKQqVw28vzopyvmDm8oQeByNSweB8adYQALWtYpvaC_DQWvCHL53-rzJchQkNiN7TefEzrazHQh0sEV0ye8fACp9bUdhGeiyfeTg_eBoxsNPn3WQ_kfFXRTSWlrDYa4lCbw-dixJDjaDnfJlWsR4IqtEJIOa32RH5ARYeC1ZmaEKx-Lkly6uMzk_Lk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: عملية جزيرة خارك لم تعد مطروحة الآن.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/78464" target="_blank">📅 23:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78463">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db4faddc2.mp4?token=VnSK0hWBoHO5c-0bKs6VwnFAVl08Soqzvlnr5pm7AmJv67HTwZpBVst8cMsQ8-_RDIUPLj1nnl8F9eMix3njfRJvhiWFPEOzJpRXpLEPQGvQay6c3WPCTUx56icS8b5HsL3eMQTcY3mlBE8-pTYre9AEo7DtlwrkjPQG7SR6zefc51bXUQ5f17nTiu5dNViu4PfV52K0NbCsBCeuJG401pBLPhDhl9_JsHpw8e0JbFs7AUhbNmfqRaY6lT3_MOiEfPZeBDHrg2OPjgWISSr1qLQmaBDaD-1ILr4CvJt5dkh7IQjpAGjp3wJ5RO2J8E2NXvMF1gRnCqHKlegeTMhQRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db4faddc2.mp4?token=VnSK0hWBoHO5c-0bKs6VwnFAVl08Soqzvlnr5pm7AmJv67HTwZpBVst8cMsQ8-_RDIUPLj1nnl8F9eMix3njfRJvhiWFPEOzJpRXpLEPQGvQay6c3WPCTUx56icS8b5HsL3eMQTcY3mlBE8-pTYre9AEo7DtlwrkjPQG7SR6zefc51bXUQ5f17nTiu5dNViu4PfV52K0NbCsBCeuJG401pBLPhDhl9_JsHpw8e0JbFs7AUhbNmfqRaY6lT3_MOiEfPZeBDHrg2OPjgWISSr1qLQmaBDaD-1ILr4CvJt5dkh7IQjpAGjp3wJ5RO2J8E2NXvMF1gRnCqHKlegeTMhQRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: وجدنا إيران عقلانية، وستتوصل إلى اتفاق.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/78463" target="_blank">📅 23:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78462">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">المراسل: ما مدى ثقتك في أن هناك توقيعًا سيحدث في نهاية هذا الأسبوع مع إيران؟  ترامب: سيكون ذلك قريبًا — ربما في نهاية هذا الأسبوع.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/78462" target="_blank">📅 23:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78461">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3173a00b9.mp4?token=b5jHaSvG9tFxyemkHHY6aGdCbvu2D9hN834SHNnOpdcRCMuCE-SSYsVLp6YBAAUZ05YNQAQlS8xT-ZsPJ-LSMuhWbwg2LJrIE2BosApwCPzE_gJUGoPFnq51K8xVbc8JdiT7oXbgqhU9_XoWBeIjgjBTgtZEp6jDHo0Da_wo2_GWgho69o7_oXf4SqRPPsP0pI6yvj0PQSQtUmV4Kwu5-IuXp2w4YiHaOoA6sLk53u43ptZSy3DoVzaMfULL1GAFXt6AmIlBZMLiZtkAnhTCbBWfgp6h2HemEJe3DHzwrmpLHtJCNbhp70WxmdIsbcpD36lHmaiMCPU0C9JZJXpPNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3173a00b9.mp4?token=b5jHaSvG9tFxyemkHHY6aGdCbvu2D9hN834SHNnOpdcRCMuCE-SSYsVLp6YBAAUZ05YNQAQlS8xT-ZsPJ-LSMuhWbwg2LJrIE2BosApwCPzE_gJUGoPFnq51K8xVbc8JdiT7oXbgqhU9_XoWBeIjgjBTgtZEp6jDHo0Da_wo2_GWgho69o7_oXf4SqRPPsP0pI6yvj0PQSQtUmV4Kwu5-IuXp2w4YiHaOoA6sLk53u43ptZSy3DoVzaMfULL1GAFXt6AmIlBZMLiZtkAnhTCbBWfgp6h2HemEJe3DHzwrmpLHtJCNbhp70WxmdIsbcpD36lHmaiMCPU0C9JZJXpPNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: الولايات المتحدة سترفع الحظر عن إيران بمجرد توقيع الاتفاق.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/78461" target="_blank">📅 23:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78460">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
‏ترامب: تم إبلاغي أن مرشد إيران وافق على الاتفاق.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/78460" target="_blank">📅 23:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78459">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8be63313a.mp4?token=eQ4Jx50ykYPE6r8E_9xihPrTh_J4hZv9p_R1NIT_KYVqNPeIYi9wAh3QTYT67wEuuQ47iKF4yEgfsZWeyM7RvloQgCgzCva11T3w9roYDhUfH36pCkC1BWmiVUE4jEekTk8OOXAp9DSkKCJvBbyMLzN_UrTvHpAm5uR9TAwJFTjPPbFIn9gLlwINBR5RDsoNWDN-U1B6QKqhvxByGR_sxnqbHqDyFC7tvpw3_gIfR8KfBcaqTeVBcQme35UbfQ66YL6UUE9NSMMm-WAgo4EqEqS0JwRU6L8BkwJ-R1w2vfDieib7cxbZGpL0WEqRkF3BmpSW-sqTOlMSvUKD5mRBfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8be63313a.mp4?token=eQ4Jx50ykYPE6r8E_9xihPrTh_J4hZv9p_R1NIT_KYVqNPeIYi9wAh3QTYT67wEuuQ47iKF4yEgfsZWeyM7RvloQgCgzCva11T3w9roYDhUfH36pCkC1BWmiVUE4jEekTk8OOXAp9DSkKCJvBbyMLzN_UrTvHpAm5uR9TAwJFTjPPbFIn9gLlwINBR5RDsoNWDN-U1B6QKqhvxByGR_sxnqbHqDyFC7tvpw3_gIfR8KfBcaqTeVBcQme35UbfQ66YL6UUE9NSMMm-WAgo4EqEqS0JwRU6L8BkwJ-R1w2vfDieib7cxbZGpL0WEqRkF3BmpSW-sqTOlMSvUKD5mRBfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: تم إبلاغي أن مرشد إيران وافق على الاتفاق.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/78459" target="_blank">📅 23:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78458">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابة ميركافا تابعة للجيش الإسرائيلي في محيط بلدة طير حرفا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/78458" target="_blank">📅 23:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78457">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⭐️
وزارة التربية العراقية تنفي تأجيل موعد امتحانات السادس الإعدادي أو تسريب الأسئلة.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/78457" target="_blank">📅 23:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78456">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامب: لن أتمكن من حضور مراسم التوقيع، وفانس سيكون حاضراً في توقيع اتفاق إيران.  توقيع الاتفاق مع إيران قد يتم قريباً، ربما خلال عطلة نهاية الأسبوع.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/78456" target="_blank">📅 23:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78455">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcb7b99701.mp4?token=DYtTJaob-j5hj1YRZAfWnrRbq2iy46mHLb6HktlKAkU6sKdhJyx2UgFMAEI48oR05dHk5G3PxoWgr5ELVTTHA34KLbTO8B4dg1GCaehlZhpN_FNQjQo5ydvf8yvZD4gpr_NEGrbjFDhebl26HwsW7jeH1R11r3Xyqu8-tiB6QX1jnJiC4TeZTrs77T3QjTb9mDHzXjL10P2l92lY90FoaEFzLr-YY5iAEge0C458zEDBw2A-rPOLWkiN_wRzHIqiDLFFYkbX-GdRs9qu1OyMHIUty90Ds5Y4i2y4RGMorKvNcxQkSWMujHmcJOxhdSaHPlMph6mjpSVxNjOrItS87g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcb7b99701.mp4?token=DYtTJaob-j5hj1YRZAfWnrRbq2iy46mHLb6HktlKAkU6sKdhJyx2UgFMAEI48oR05dHk5G3PxoWgr5ELVTTHA34KLbTO8B4dg1GCaehlZhpN_FNQjQo5ydvf8yvZD4gpr_NEGrbjFDhebl26HwsW7jeH1R11r3Xyqu8-tiB6QX1jnJiC4TeZTrs77T3QjTb9mDHzXjL10P2l92lY90FoaEFzLr-YY5iAEge0C458zEDBw2A-rPOLWkiN_wRzHIqiDLFFYkbX-GdRs9qu1OyMHIUty90Ds5Y4i2y4RGMorKvNcxQkSWMujHmcJOxhdSaHPlMph6mjpSVxNjOrItS87g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بعد أن زعم جيشه أن المضيق مفتوح.. ترامب: سيفتح المضيق فور توقيع الاتفاق.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78455" target="_blank">📅 23:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامب: توصلنا إلى اتفاق يمنع إيران من امتلاك سلاح نووي.  تحدثت للتو مع نتنياهو.  وثائق إيران في مرحلة نهائية تقريباً.   تحدثت للتو مع قادة قطر والإمارات والسعودية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/78454" target="_blank">📅 23:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3470ffac2.mp4?token=u6zm3v63yeYGw4f_GisBt8Q0YOtHXxfUA0gU6yuq8AGIqeoB65ovSiqI0_S_bOqIKJW1K8Q-_WDSFN0i5MwkcT97b0YTga1pID1Z3ydgGhXIw68yF3p97V0-1N01-72p-HLFOF67V4x8GOzwSGneczx_F1Dq96HEQr5ERmTrPus3_L098JQEDBor57Px9nDiDgJAKVlUoQVjDXV_Wdt1KHCPN_w1i0XZ1dSNWMrrNuRqAuSDg-3RcYG5wCTi7GA730Cg0G2ob4AsqMgbR4_xARdy7Trwpl9_LbV3BRSDeTheeAmFlzU5Si15IUhbKyAqsea6vODPEdkq-GpyHSd2_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3470ffac2.mp4?token=u6zm3v63yeYGw4f_GisBt8Q0YOtHXxfUA0gU6yuq8AGIqeoB65ovSiqI0_S_bOqIKJW1K8Q-_WDSFN0i5MwkcT97b0YTga1pID1Z3ydgGhXIw68yF3p97V0-1N01-72p-HLFOF67V4x8GOzwSGneczx_F1Dq96HEQr5ERmTrPus3_L098JQEDBor57Px9nDiDgJAKVlUoQVjDXV_Wdt1KHCPN_w1i0XZ1dSNWMrrNuRqAuSDg-3RcYG5wCTi7GA730Cg0G2ob4AsqMgbR4_xARdy7Trwpl9_LbV3BRSDeTheeAmFlzU5Si15IUhbKyAqsea6vODPEdkq-GpyHSd2_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: قريباً توقيع اتفاق مع إيران.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78453" target="_blank">📅 23:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامب: التسوية مرهونة بالتوصل إلى اتفاق خلال الأيام المقبلة، وتوقيع اتفاق إيران قد يتم في أوروبا.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/78452" target="_blank">📅 23:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامب: توصلنا إلى تسوية عظيمة للصراع مع إيران.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/78451" target="_blank">📅 23:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b447a8a70.mp4?token=a1lWuUHXtiTIByeuA72t6KK235hqgNJv0ysZzvX4VoTe3jROWysMrJWuhB-qG5-APL5ow3TjhHT7sMtd6U8QYdip1946WLc--DiA9JTGSaUsuiWK5CSCsBLjxjs71CnIhTRbJ8FJyAgkGFQg9H1qw5hsUAs7NS-V7_4RKIriHWzhyLDNnIU7QVb7G8EKWwXTjgFGNA9s9H41kxWXO0deogX2AwGcWMOu4ZUXMHp9SYtMLd7hqW6xIRBwPMZOVIe1WQbqggsM3yRtB93vg7lPGzIDzs7n8-YMvdNOkk43k0voLAKaU7_Mn5vlTdSmfqjpPyGRdoGkUfOuMc1Wi1-Xow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b447a8a70.mp4?token=a1lWuUHXtiTIByeuA72t6KK235hqgNJv0ysZzvX4VoTe3jROWysMrJWuhB-qG5-APL5ow3TjhHT7sMtd6U8QYdip1946WLc--DiA9JTGSaUsuiWK5CSCsBLjxjs71CnIhTRbJ8FJyAgkGFQg9H1qw5hsUAs7NS-V7_4RKIriHWzhyLDNnIU7QVb7G8EKWwXTjgFGNA9s9H41kxWXO0deogX2AwGcWMOu4ZUXMHp9SYtMLd7hqW6xIRBwPMZOVIe1WQbqggsM3yRtB93vg7lPGzIDzs7n8-YMvdNOkk43k0voLAKaU7_Mn5vlTdSmfqjpPyGRdoGkUfOuMc1Wi1-Xow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: توصلنا إلى تسوية عظيمة للصراع مع إيران.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/78450" target="_blank">📅 23:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6PGS_jlOCxIEwHNVCsy_nHGuzNdvUtI2LPdqQYzE5cKY8_P8Nvin6Gdc1Ikv9yS6ySQ0LNXvYMOHijtRZ_Y-JcgDxmrb8MQb8gFuBhhpfFK37f5kjtobAlFpxhTjAyv2qHpRS3BcOMwhrzNGStGL0MrvxZu5hQm2bblTstM-Vmbnf3TZ34gxoGa0Lm2EJgPtfIpIDLJBwl-4irqKx39-kC0Gv2NHtckS_GAqC0seZQsFmMd2uuCaCb0KUWXDVmg8AVW59o5Z4Fp7YIuhp4pcGMGg-NQNKyq4rITkareUx0ah4Y9A9-yL6aTrtJYy05MomttE7uXJgzE9Lal6dbIYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية "إسماعيل بقائي":
‏لقد تحطم جيشه في ليلة الأحداث. ‏من كان صالحاً في موقف السلام، فإنه يقرع طبول الحرب.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/78449" target="_blank">📅 22:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⭐️
نيويورك تايمز: قبل إلغاء الضربات المخططة على إيران يوم الخميس، تحدث ترامب إلى الوسطاء الباكستانيين، الذين أخبروه أن لديهم "اتفاقًا" مع إيران.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/78448" target="_blank">📅 22:42 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
