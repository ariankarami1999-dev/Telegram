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
<img src="https://cdn4.telesco.pe/file/TDm8nRhYSf-VQkdZdpu25tigChcSMyTLswhXzFeABSaKzQzn-O7O9qoR5H1c1sHudFuo1ZKCD1_tqtJTa_PqGgKrfHOF5HeoPkxTua-mb3suoskAhSF0yK8wKcTrw6AmKo75E7MnR2-ZSeX4uNHsA3MXEw2A-CbYgd7MxLYlTfEz-n1lDk9gmQDSALfTZbidu8shJIYI_Cf5Xp2rwt9HMkno75QliH4Vmff15Mj2MuLeNvDJ9viX710iaN3w5n_0HgiIw10JxHBag9-EDLg7UKbfKLe0F3UwML4QmpnhKE2PbWXvt81SL90lC5AzlpfRwcgH7zyp1r-W50vLXIde9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 19:17:59</div>
<hr>

<div class="tg-post" id="msg-88960">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Srk0EJ9a4Sxy3qM8T7aGmr83R05vZpwTaqp8hYlgbHrTBMmp32ZfnEJRGudQbpSK1Q0SWyV3LLOFi1JGvdzOcsVaycFJkhiqWjFXkNPQ0534Z3X-NBQ4zVsUrHwRkX6QRxlD-HwEu-N__ehdKkJas-WX4rm4pB4EfG9zRyiOwqmUy2Qwn5g8iYEGfX7Myi7IeAn-VPtywGiddEfKeqSMc7LaztEwYH-dF8-jHKm2O2nlpY_ekm8R8ADlVyfMp8y7ML4O-Sq-kuOl6lx1vcCVRpwey6JZV1tZT0m4K7zfcLCqO4cHMrinwQzhZiRkSPirIubwIns2mNsIFQrr9SkubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HYkAAvWpWHCuTlpfPljuMV7fJh9VKVrgBCyp6xLtHNgVUsBKHEgzS3bwPWFeRr1QIKl8LWK1CAwRfnvlk1QM4Ouyx5UYZFn4LBOlS7BQNWvQc_i34laD3O4EqzmEHAgIyt9D8mhZuc1sM5AVxd0o_QDV-3hcnKJOFtV_F8TsDkQkGa-Kt7VuFp8gnUjQOOmfN5qnvYocXbCAhyxudQPsbdvlLd-dmXQbYtE__TJACjBI3QV5wNHaM1aEPoCQBN09ug1a3t-8v7heDjQnPKVeGTqFcNd4_OSqvLS0H3EueabJ2HdC8CISz1ASDMurhNMaYlmTdMXvVZPmu4Kz1Mbcmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxFi02amEaBSy9M-8OwDpMAoEHFRwc-11f6DEgRJ8145t49IKwAUO1FcTdhJrxs6cquNRsV0rAHlZZ5axK7eOEW0PNmxakmTMMiYjzmu1KsB4iBrgXtbdrlh0-E2VBtf25Ey7tXjiTMrCm_dfIeA8Y9lGAcoFFLle1eF7wEiKkncPGsNAdmzBPO5_zZTR3B9v4xK45wQF6XSrzZXX87PeQAGquULf4kfOaj7LM89ASwm5OJPFPFh8ulP2lDSGADv2lsURuKKPg8F1rr8Kf3Zuljb-dXBmqadLx9UlVfpf8XhwPV2lDzJ6sjW7sK7tfHK8dZ2wo_DDvD9o61CWEF6oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#ترفيهي
عشر ناقلات نفط على الأقل ترفع العلم السعودي تقوم بتغيير علمها السعودي إلى العلم الليبيري، وقامت جميعها بتغيير اسمها وهم متمركزون الات قبالة سواخب خورفكان في محاولة للعبور باتجاه الخليج.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/naya_foriraq/88960" target="_blank">📅 17:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88959">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزير الخزانة الأمريكي بيسنت: من المحتمل أن تمتلك إيران ثالث أكبر مورد للطاقة في العالم.</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/naya_foriraq/88959" target="_blank">📅 17:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88958">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزير الخزانة الأمريكي بيسنت: من المحتمل أن تمتلك إيران ثالث أكبر مورد للطاقة في العالم.</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/naya_foriraq/88958" target="_blank">📅 17:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88957">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">قتيل و5 جرحى كحصيلة اولية للانفجارات في مدينة ادلب السورية</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/88957" target="_blank">📅 16:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88956">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇵🇸
أمن المقاومة الفلسطينية:
أحبطنا صباح اليوم عملًا عدائيًا كبيرًا كان يستهدف شخصية قيادية مركزية، فيما نجح الاحتلال في اختطاف مسؤول أمني كان متواجدًا في مسرح العملية. نجحنا في كشف القوة المعادية وإيقاع خسائر فيها، واغتنام معدات وأسلحة منها، كما ضبطنا ثلاثة عملاء للاحتلال كانوا في مهام إسناد وجمع معلومات.</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/naya_foriraq/88956" target="_blank">📅 16:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88955">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏مقتل المتحدث باسم تنظيم داعش "أبو حذيفة الأنصاري" في حضرموت اليمنية</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/88955" target="_blank">📅 16:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88954">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
🇺🇸
وكالة فيتش للتصنيف الائتماني:
قد يؤدي تصاعد الصراع بين الولايات المتحدة وإيران إلى تعريض بعض التصنيفات الائتمانية لدول مجلس التعاون الخليجي للخطر.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/88954" target="_blank">📅 15:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88953">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1adcf2ddab.mp4?token=TPj1Iz7qUt9CFEG3cemav7N4tbpmymebGdLPXrUB7BTGu95t40z1_7DTzeYV7fPrj_P4RDfFVxd_N1ErnRFRYCeZID48dltLnsuVvCR0AZS3zU19rfhksgu86eNnb7ezOV-GOXMoikt5n0vaJM8mjFIZoBa1nzgAyBhKJ4ztsNRO_t2pHHumTFhSLoZwYkkPhGJKJXswbxJRN62JpvTLsy4BG9O3SNbXQKDZ_6DNqi4xqnR9Pj-TSEVO1cHlKZY0YVTmwdPOR46ffjeJSfrFgquzyGeY0XIaQ4B2yxQr39BQLTkjlIUVIIQDJeXS0MmfzUlc5gWyKydOzCMfxOOVzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1adcf2ddab.mp4?token=TPj1Iz7qUt9CFEG3cemav7N4tbpmymebGdLPXrUB7BTGu95t40z1_7DTzeYV7fPrj_P4RDfFVxd_N1ErnRFRYCeZID48dltLnsuVvCR0AZS3zU19rfhksgu86eNnb7ezOV-GOXMoikt5n0vaJM8mjFIZoBa1nzgAyBhKJ4ztsNRO_t2pHHumTFhSLoZwYkkPhGJKJXswbxJRN62JpvTLsy4BG9O3SNbXQKDZ_6DNqi4xqnR9Pj-TSEVO1cHlKZY0YVTmwdPOR46ffjeJSfrFgquzyGeY0XIaQ4B2yxQr39BQLTkjlIUVIIQDJeXS0MmfzUlc5gWyKydOzCMfxOOVzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇷🇺
بوتين للرئيس الإيراني:
الشعب الروسي يقف بتضامن مع الشعب الإيراني في سعيه للدفاع عن مصالحه. روسيا وإيران تحافظان على علاقاتهما الاقتصادية والتجارية على الرغم من الوضع العسكري والسياسي الحالي.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/88953" target="_blank">📅 15:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88952">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قتيل و5 جرحى كحصيلة اولية للانفجارات في مدينة ادلب السورية</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/88952" target="_blank">📅 15:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88951">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
جهاز الأمن الوطني العراقي يعلن عن تفاصيل عملية «ظل العدالة» التي ينفذها الجهاز ويعلن القبض على أكثر من (500) متهم حتى الآن.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/88951" target="_blank">📅 14:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88950">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b839ccee98.mp4?token=IrJenBu94c0zIriXAFHmb-AMVo3OjtRrVADqlE3_azCsRDREiJGHmiDT271HTKofmzxxCdCaP3TKKT5tn2k6InJ--uV9TBXyXL9whOBrVwns1a56jhEIYDK6aJkUXw24sGgmdQUlbiDeMKFItpKgOX1Myavzp2VeBvsoNd-TehCtWosC6SQKZCCQubYi09SjVUH2UaD_FaayE5zU2UyVptZHdrAjX6JBRKcyv7VkghczaueGfNL0TysdaTgLURaM1DOBHFusk3s8uZMjIdMnNeZinkzcCVV7Dhio2ML00jWM3qobTG9yfNXlXZpIcv1QkN-I6PSeI82NufbnQfoBMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b839ccee98.mp4?token=IrJenBu94c0zIriXAFHmb-AMVo3OjtRrVADqlE3_azCsRDREiJGHmiDT271HTKofmzxxCdCaP3TKKT5tn2k6InJ--uV9TBXyXL9whOBrVwns1a56jhEIYDK6aJkUXw24sGgmdQUlbiDeMKFItpKgOX1Myavzp2VeBvsoNd-TehCtWosC6SQKZCCQubYi09SjVUH2UaD_FaayE5zU2UyVptZHdrAjX6JBRKcyv7VkghczaueGfNL0TysdaTgLURaM1DOBHFusk3s8uZMjIdMnNeZinkzcCVV7Dhio2ML00jWM3qobTG9yfNXlXZpIcv1QkN-I6PSeI82NufbnQfoBMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من استهداف مجهول طال عدة سيارات في ادلب تحمل كدس عتاد</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88950" target="_blank">📅 14:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88949">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني:
لن ننسحب من غزة حتى نزع سلاح من القطاع وتجريد حماس من سلاحها وتدمير جميع الأنفاق.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/88949" target="_blank">📅 14:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88948">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2c243aa.mp4?token=v931KNIYDal-z_hcKPd9aanYMkaIEKO-RdtGjSsGg3decVur9O12zKS7zAR53Sx0i4rfN5Vv2VU0kL8McwdgWToYDyo_r3TFg3_ngWTC0YcfoWahhBwqqBZfyjf6pjEOtiRKUAZTiFiuf9ebB_LdKVP5WK0vSNm-SQc1NPyHGjfnjHh3yODR4OmNev7C0Ckkq4AlnWG0Y8WgjohC2zHjIixo2CbnO1ujVTQTccOkGBA7182Tg1LnFE2juXdJ8tRwZ1lub1ubmAi8QOuPed2tNJLb5bvqhXbOz3rLN_rz-HBHdiBSSta_lpGNFUQXdq6ItqLlTTYtsMu_H_UU57NUvgLiztRbBZtUWAhXNP2zhqc9kM899DiTzo7C1qXaobPXQ5utsfO2a2y9aqFgtt5COEYOwshoop06oD2rIDcnXL3dV2lA4_92mCHb1oz9d6yy_OcS2YP3E0nBiqAwxKLBL6dPsENvUHwJV5VGX2BXqjztO0yeVi0WSvFN-N7Tu1y0aXlRKhawSNf6gE9o5r7JTbpc5-mm6W-zljzMJiVUyUQYQdtwbOd3c9iKUDUOA51UiBwE4qQsb6euk3dNUlOQBvqky4Wh58klzYA9lU4pKQcH1xhgJqiN9-cTT2irWrQXEWEs_MRgd3iRilDPkCxKhHznqoJqrGmZC3OzUpKuMH0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2c243aa.mp4?token=v931KNIYDal-z_hcKPd9aanYMkaIEKO-RdtGjSsGg3decVur9O12zKS7zAR53Sx0i4rfN5Vv2VU0kL8McwdgWToYDyo_r3TFg3_ngWTC0YcfoWahhBwqqBZfyjf6pjEOtiRKUAZTiFiuf9ebB_LdKVP5WK0vSNm-SQc1NPyHGjfnjHh3yODR4OmNev7C0Ckkq4AlnWG0Y8WgjohC2zHjIixo2CbnO1ujVTQTccOkGBA7182Tg1LnFE2juXdJ8tRwZ1lub1ubmAi8QOuPed2tNJLb5bvqhXbOz3rLN_rz-HBHdiBSSta_lpGNFUQXdq6ItqLlTTYtsMu_H_UU57NUvgLiztRbBZtUWAhXNP2zhqc9kM899DiTzo7C1qXaobPXQ5utsfO2a2y9aqFgtt5COEYOwshoop06oD2rIDcnXL3dV2lA4_92mCHb1oz9d6yy_OcS2YP3E0nBiqAwxKLBL6dPsENvUHwJV5VGX2BXqjztO0yeVi0WSvFN-N7Tu1y0aXlRKhawSNf6gE9o5r7JTbpc5-mm6W-zljzMJiVUyUQYQdtwbOd3c9iKUDUOA51UiBwE4qQsb6euk3dNUlOQBvqky4Wh58klzYA9lU4pKQcH1xhgJqiN9-cTT2irWrQXEWEs_MRgd3iRilDPkCxKhHznqoJqrGmZC3OzUpKuMH0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادلب بعد الانفجارات</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/88948" target="_blank">📅 14:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88947">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6df400dbf.mp4?token=GdHYSl8ViXAXjA9OPCq5PT4cqXGBVM09W5LKf_-eTBTpYsPA05PhPkOPrF0cQKDCYTJLJkUsOoA4vuJM89Bwu1728GtjbNpL992_Oo6lb4_mXDCoro950fu8dlubAP3PuRIdHCGFdAQqctvxQihU1yEnhmemMSRwtxZODFCYybFE1Ov3etMvPf_LVA7dYOwA_6ppNjchvjo3XmKexzdWBdGKDRIo4Nh7IQE8s3IoXAUmQu0_hwnXRMLjTK5miCVWrsTrdENQysbvrHec9QFtbPEOj1zc-lDqNtt7tJAUBLsQIdSsd9a7DED_M6q_C5gMYChde_G9FFsXEi7VFUGW3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6df400dbf.mp4?token=GdHYSl8ViXAXjA9OPCq5PT4cqXGBVM09W5LKf_-eTBTpYsPA05PhPkOPrF0cQKDCYTJLJkUsOoA4vuJM89Bwu1728GtjbNpL992_Oo6lb4_mXDCoro950fu8dlubAP3PuRIdHCGFdAQqctvxQihU1yEnhmemMSRwtxZODFCYybFE1Ov3etMvPf_LVA7dYOwA_6ppNjchvjo3XmKexzdWBdGKDRIo4Nh7IQE8s3IoXAUmQu0_hwnXRMLjTK5miCVWrsTrdENQysbvrHec9QFtbPEOj1zc-lDqNtt7tJAUBLsQIdSsd9a7DED_M6q_C5gMYChde_G9FFsXEi7VFUGW3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من ادلب بعد انفجار كدس عتاد بعد صوت الطيران الذي حلق في اجواء المدينة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/88947" target="_blank">📅 13:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88946">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b327e04c.mp4?token=uUboDclpPqVOR7BIUevLGm4zuPpAIUq2UtgkBmpD-R_PjHKxi-zNqBpiJt1Becw5tIcLLcu0LiAHnlWfdWzP389yjV2xyweYNanQ-XqihjuythN--Q_eKPrk7cXCi1rxZR3XZTUcna2xxpJOBE7d1T8-brL0ymSHzR67B5Hur6ZSL0jlYgPT1KB0j2CnfO9T4foZcOsqKrT4-OA5hr16pgUmYXllr93k7fRs1PXPPJCeGeqDdZmjW83nay0Ndg0esoUsAzWw9ZbE-nEQsSCGDwB3a4m-Maq6dF-UB8giW10PqwKsMhkmk_DXIsEpJqpXt3oNCH1tT-rbIIkfvZBFDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b327e04c.mp4?token=uUboDclpPqVOR7BIUevLGm4zuPpAIUq2UtgkBmpD-R_PjHKxi-zNqBpiJt1Becw5tIcLLcu0LiAHnlWfdWzP389yjV2xyweYNanQ-XqihjuythN--Q_eKPrk7cXCi1rxZR3XZTUcna2xxpJOBE7d1T8-brL0ymSHzR67B5Hur6ZSL0jlYgPT1KB0j2CnfO9T4foZcOsqKrT4-OA5hr16pgUmYXllr93k7fRs1PXPPJCeGeqDdZmjW83nay0Ndg0esoUsAzWw9ZbE-nEQsSCGDwB3a4m-Maq6dF-UB8giW10PqwKsMhkmk_DXIsEpJqpXt3oNCH1tT-rbIIkfvZBFDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسجيل عدة اصابات في ادلب جراء تطاير كدس عتاد بعد استهدافه من قبل طيران وفق شهود عيان</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/88946" target="_blank">📅 13:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88945">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5e04eea08.mp4?token=MKT9Wjj-_Y3FgEL3cupc4QGyG7qQqst386gk8YX1bwlCXsjQaw1BEc6C4D4R9yupOq0URGrhNjdyfXmsqJqfYyfFCWaU5MYpOZhQ1FbxzrXds_QGyawM2jRfE8WSYEqpoZ6mdSpTNEBRJIa8DgW4nv-X9FuhS_ZLKJZ0gxOrDu16pxzPUmJs8IXP9QGPJrmTMgCJWgVabEEUQzW6M0Sq7lMWq3jSanY87jPUtfXIhq5YBKKJ633pSg8bC-TJiny4IIP4DXk-6dEHzjWOMHqTbhzOgHgR5CyP7SL4Iql_N7MUGu-CxxwEBSX9UfgRdPAyS65YcGezChXYGXAU0eNhdYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5e04eea08.mp4?token=MKT9Wjj-_Y3FgEL3cupc4QGyG7qQqst386gk8YX1bwlCXsjQaw1BEc6C4D4R9yupOq0URGrhNjdyfXmsqJqfYyfFCWaU5MYpOZhQ1FbxzrXds_QGyawM2jRfE8WSYEqpoZ6mdSpTNEBRJIa8DgW4nv-X9FuhS_ZLKJZ0gxOrDu16pxzPUmJs8IXP9QGPJrmTMgCJWgVabEEUQzW6M0Sq7lMWq3jSanY87jPUtfXIhq5YBKKJ633pSg8bC-TJiny4IIP4DXk-6dEHzjWOMHqTbhzOgHgR5CyP7SL4Iql_N7MUGu-CxxwEBSX9UfgRdPAyS65YcGezChXYGXAU0eNhdYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الانفجارات في ادلب</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/88945" target="_blank">📅 13:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88944">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجارات تهز ادلب السورية</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/88944" target="_blank">📅 13:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88943">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارات تهز ادلب السورية</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/88943" target="_blank">📅 13:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88942">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8auhNaBSydBoLyRhEz6yQePvaWbm3MVD2gbzUoAAdkfHOdDx0vkGChIpFa9MGOlCLeORs4anl6Gobv8K0hlnMeb_TUDyAK35DJkFo4fVzXU9bQuqNEOoadwbYf0B5xBTNBUNDzHaeDnWkvwhYx3JywRMhLjBvldgrFkNUd1K15rkVJmNpoDwKIePdvB8BxBx_SThhH4jhUycdnuqoKelhPIHqo00uQWV15Up8foCmFxvtPRpRw7ze2PkUy4m_HHlyQ6KjDB2MZvsAZDt6Y2QggNgK79Jn6zGEic0HVhvpFO11J3UBxmrQoBko_1xqsT9XOuPr7XiFFXhncJRnjr8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر:
يتعهد بالرد بقوة" بعد أول تبادل لإطلاق النار مع إيران منذ أسابيع.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88942" target="_blank">📅 13:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88941">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
القضاء العراقي:
محكمة تحقيق الكرخ الأولى أعلنت استكمال مرحلة الاستجواب في ملف 5704 متهمين من عناصر عصابات داعش الإرهابية المنقولين من شمال شرق سوريا إلى العراق والانتقال إلى المرحلة القضائية التالية المتمثلة في إحالتهم على محكمة الموضوع، كل وفق الأدلة والوقائع المتحصلة في قضيته،عمليات التدقيق أظهرت أن الملف يضم أشخاصاً من 67 جنسية بينها 16 جنسية عربية و19 جنسية من دول الاتحاد الاوروبي و 32 جنسية أجنبية أخرى، فيما بلغ عدد العراقيين 474 وعدد السوريين 3497، الأمر الذي يعكس الطبيعة الدولية للملف وتشعب الوقائع والأدلة ومسارات الأشخاص المشمولين به، التحقيقات وجمع الأدلة والتحليلات أسفرت عن كشف عدد من العناصر شديدة الخطورة ممن شغلوا مناصب قيادية أو أمنية أو شرعية، أو عسكرية، أو إعلامية، أو ارتبطوا بعمليات نوعية وجرائم ذات بعد دولي وقيادات من الصف الأول في عصابات داعش الإرهابية</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/88941" target="_blank">📅 12:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88940">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">▫️
الرئيس التنفيذي لشركة هاباج-لويد المتخصصة بالشحن البحري:
من المنطقي الاعتقاد بأن مضيق هرمز سيظل مغلقاً في المستقبل المنظور.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/88940" target="_blank">📅 12:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88939">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7940f24a22.mp4?token=XZ2Y-_6EvCEbkNGWpQQ6WxEZI-Xqw6teCbb29GVSHuLRF65dhQPalHcu4_KHJ2EPCgpmPYRI5Hf35jxTwl4bvdtBfdNd6HkOw9thVDdhKBbOutO9wCI8KhudCnB-auGkeA_ndl_RyZIcGCuY2MR5BF94Qs9njbfqnLBdqhQpH8VosWTYboQD6QetbXLpjgDtZCeNzPdEkEOLfI8I94kFc9oTne3bR42kVUCQ-fM_8YlVgTooIOUEZGPoe1GE2CzhqtVzMVRRxvq7ghNI-t8VsbpSomtrFiZMfcAktbVzoNxILSur_Q5kjaZo0A8oQ2jwib-FhMGSRMfPy3JidLFhlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7940f24a22.mp4?token=XZ2Y-_6EvCEbkNGWpQQ6WxEZI-Xqw6teCbb29GVSHuLRF65dhQPalHcu4_KHJ2EPCgpmPYRI5Hf35jxTwl4bvdtBfdNd6HkOw9thVDdhKBbOutO9wCI8KhudCnB-auGkeA_ndl_RyZIcGCuY2MR5BF94Qs9njbfqnLBdqhQpH8VosWTYboQD6QetbXLpjgDtZCeNzPdEkEOLfI8I94kFc9oTne3bR42kVUCQ-fM_8YlVgTooIOUEZGPoe1GE2CzhqtVzMVRRxvq7ghNI-t8VsbpSomtrFiZMfcAktbVzoNxILSur_Q5kjaZo0A8oQ2jwib-FhMGSRMfPy3JidLFhlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
مصدر امني لنايا   نصب دفاعات جوية اتجاه الجمهورية الإسلامية في ايران من جهة محافظة ميسان ..</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88939" target="_blank">📅 12:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88938">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw5HB2dE0PCwWiBfFCBwwce1nQa111qhbO9GkCQMnNmGgFAgv9IA7eax3alJLmx-lWQzDgoKNtFfAXprQynzK1Xk3YeNfF50j7fI4f7-LebHLpy3UgtH_RfVaf05l5n0i3rl7mX0GZdi3ILtIzYzqqXBPNDTOLSFnQ2uSL9gvD-UH6Tn3KlabtdinsZdvuY06e6FZTS6Z7GrhYKRsqVghJ0BaYF63S7kLFAJnbkuBu0LMHiJ7u21XMrs_XOXGAx9-yjYcD8hJ9O6QA7Y-vZj1HM5sYHP1cA18UcAao13EvtKysMVgZ1gPrDs6_UDFn9B3_ifiQ0zSIqAb69No0i5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
الليلة الماضية، حدث شيء غير عادي ومثير للاهتمام للغاية على الساحل الشرقي للولايات المتحدة.
‏تم وضع محطة نورفولك البحرية، وهي المجمع البحري الرئيسي للبحرية الأمريكية وأكبر مجمع بحري في العالم، في حالة تأهب قصوى، لأسباب غير معروفة حالياً.
‏وبحسب متحدث رسمي، "تم تعديل الوصول إلى المنشأة، حيث تم إغلاق بعض البوابات أو تشغيلها بممرات مخفضة" بسبب تهديد غير محدد.
‏الأمر المقلق هو أن إحدى آخر المرات التي صدر فيها مثل هذا التنبيه كانت مباشرة بعد أحداث 11 سبتمبر.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/88938" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88937">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇶
🇮🇷
مصدر امني لنايا
نصب دفاعات جوية اتجاه الجمهورية الإسلامية في ايران من جهة محافظة ميسان ..</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/88937" target="_blank">📅 12:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88936">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇷🇺
الخارجية الروسية:
سيكون رد روسيا على أي تحركات محتملة معادية لروسيا في منطقة البلطيق مدمراً، وسنتخذ تدابير مضادة في حال نشر أسلحة أمريكية في اليابان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88936" target="_blank">📅 10:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88935">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
🇸🇦
منذ فترة ليست بالقريبة،
لم تُرصد عمليات إقلاع لطائرات إنذار مبكر أو طائرات للتزوّد بالوقود من قاعدة الأمير سلطان الجوية في السعودية فهل تعمد السعودية إلى عدم المشاركة في الضربات الأميركية الأخيرة ضد إيران لتجنب فتح جبهة جديدة إلى جانب جبهة أنصار الله في اليمن؟!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88935" target="_blank">📅 10:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88934">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
قيادة الدفاع الجوي الايراني:
تتولى الدفاعات الجوية في جميع أنحاء البلاد أربع مهام رئيسية تشمل الكشف، والتعرف، والتتبع، والمواجهة مع الأهداف الجوية.
المهام الأساسية للدفاعات الجوية هي الكشف عن أي جسم طائر في سماء إيران وحتى ما وراء سماء البلاد. بعد الكشف، تبدأ مرحلة التعرف، وفي حالة الضرورة، يتم التتبع بواسطة الطائرات المقاتلة أو المواجهة باستخدام الصواريخ وأنظمة الدفاع الجوي.
في النهاية، تهدف الدفاعات الجوية إلى منع أي طائرة معادية من تنفيذ مهمتها، وإذا لزم الأمر، تدميرها.
تنتشر قوات الدفاع الجوي في أكثر من 3800 نقطة في أنحاء البلاد، والعديد من هذه النقاط تقع في مناطق وعرة.
إيران دولة ذات تضاريس جغرافية متنوعة، وتنتشر قوات الدفاع الجوية في الصحاري، والشواطئ، والجزر، والارتفاعات.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88934" target="_blank">📅 10:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88933">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
مجلس الوزراء يوجه بتجهيز المولدات الأهلية بالوقود بسعر مدعوم لشهر أيلول.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88933" target="_blank">📅 09:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88932">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d8498082.mp4?token=nz3VdeIU-15y3rSXVe4mReX8gdvmCCOhizl6feT2mC9zE5ttA6_Uz18LLszhzdQqfRz0Y09GV6WtGK_6aer9jUaBrsY4iR_9wzX0nAjI99N1yN-l3nSLnc4KlbOM7yz63fnVS9R_pJKazCN-G45NRmXVY7bA35EMhfbpGuKF0dvHeEa0ktmdJptFpNnQ_l2cnNbu0wdclkLjhWiJICnajH_Hdkmg-8OD8wLzHYU31oIUBNOxREIwIA1BvMi4F-5aqZmQSxeSB-tQANIN7eaxnVqQhInlchHh4BjcXbGWKv1GA8oqNcGimyTQA3on7-mNS6NPy2Ii-LEPyvnuew9TQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d8498082.mp4?token=nz3VdeIU-15y3rSXVe4mReX8gdvmCCOhizl6feT2mC9zE5ttA6_Uz18LLszhzdQqfRz0Y09GV6WtGK_6aer9jUaBrsY4iR_9wzX0nAjI99N1yN-l3nSLnc4KlbOM7yz63fnVS9R_pJKazCN-G45NRmXVY7bA35EMhfbpGuKF0dvHeEa0ktmdJptFpNnQ_l2cnNbu0wdclkLjhWiJICnajH_Hdkmg-8OD8wLzHYU31oIUBNOxREIwIA1BvMi4F-5aqZmQSxeSB-tQANIN7eaxnVqQhInlchHh4BjcXbGWKv1GA8oqNcGimyTQA3on7-mNS6NPy2Ii-LEPyvnuew9TQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
فانس
:إن قيادة إيران مجنونة حقًا، حقًا. وهم على استعداد لفعل أي شيء، وأعتقد أنه ليس ذلك بدافع حكمة استراتيجية كبيرة، من أجل تحقيق أقل قدر ممكن من تدفق النفط والغاز.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88932" target="_blank">📅 09:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88931">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOdR6Anv3FWtYfFi_A-sEgqDZad6oLibdYnACk4D-8KXfKSzS393yPKjJe6tJT4qS5KcGoKUSDUjbzxQpcc8gkT7FrEOjxBeNn0VA7aHwI9z7pFlvZ-FEMMHbKfaicLprcgOU15DILw3oJk86PM2yDN6QloPKMsFwIjPd0dY5gSvDQhOV9yW6sOFbDoxToHwWKlaXfWiLhIe-TkTfXF1MBwmEMrzIAS2JV9s7_MFpriEF97O02uD_32REnkKi2ZHglmsezAPuumKRWUjsr1Cu4fMzO2jxfmJf4s6RQn1TniEbYuPrDcGo_dE3nvtWc5Pw85o7yVGKghCd2hUxT6naw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعار النفط تقفز من جديد: ‏خام برنت يرتفع 2.39 دولار ليبلغ عند التسوية 90.49 دولار للبرميل.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88931" target="_blank">📅 09:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88930">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
بزشكيان
:
أدت مفاوضات استمرت حوالي ثلاثة أشهر، بوساطة البلدين الصديقين والشقيقين باكستان وقطر، في النهاية إلى اتفاق في 18 يونيو 1405، والمعروف باسم مذكرة تفاهم إسلام آباد.
لكن التزام أمريكا بالوثيقة التي وقعها رئيسها لم يدم أكثر من أسبوعين، وبدأت تجاوزات ذلك البلد وتراجعه عن التزاماته، والتي لا تزال مستمرة.
من الواضح أن انتهاك الولايات المتحدة لالتزاماتها قوبل برد إيراني متناسب، لكنني أؤكد بوضوح أنه إذا عادت الولايات المتحدة إلى التزاماتها الواردة في مذكرة التفاهم المذكورة آنفاً، فإن الجمهورية الإسلامية الإيرانية سترد بالمثل فوراً. على عكس الولايات المتحدة، يتمتع بلدي بسجل حافل بالوفاء بالتزاماته ومعاهداته الدولية، وقد تصرف دائماً وفقاً لمبادئ القانون الدولي.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88930" target="_blank">📅 08:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88929">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يستهدف العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88929" target="_blank">📅 02:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88927">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433892a9ce.mp4?token=mcmyxwvl563AagXAAx4rZJCBz3bzQgpQnyRwSLB0GCWSkr4KkCieA5Ax-PSFIGPtW2Qd5AYhB3wC3JoxkbwTEdExuulQG1At1QFG8LrWnu5qGUBiGvKwTGN2QUpMikT21F6TU67p6SkojR4PJK2EJskVbgOxzMlhz9Qad7gpgFSsyW-m2WEpsL-pZJvkewZGQzSaVDf6x6rGfCFfSmFNoNnGkGQ_Ar6ysVOrHpVkyn4i7PLHuRlfH0A_02MHXiR1n3L8Pez05mSS6nyXErytuJxu2TmQrY-bd19PNi7pOoQfAeuhzysTpWkjXTV9FIRgSpOk0pxp1JEBNY-HTW4TUqp5R8zCFQRk3amLVKbqVRjbIV6-S8Q1TG2VnZsYUnZmEHcyC6SbwrDYGRLXMr7TfSg6GHi6l9PWn1xi1q4ZZlwP4MnuOlAEjIHcjyP163-4fVwge8AV0xbVyh_p39Ej5J1NBK0L716j7CQ0Q9A6MYX1Oct6zogR1xLxg4Ddxo_RlXHHqJ0MlF2xoptO9dAjB3cF9X5DG2tgVqQdI_COaAG9J8gr39ZowNOKPWV7gBZm8_QzkA9TrdXce03CBX7Hbzj1QBcp-BVpPlJ6zIkDgj-HOIgczg4FAZw4h94hu5MdKSG84aWBn6Pb2oJ0rjqc0h1ujEcEONBhYeFsLv410jE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433892a9ce.mp4?token=mcmyxwvl563AagXAAx4rZJCBz3bzQgpQnyRwSLB0GCWSkr4KkCieA5Ax-PSFIGPtW2Qd5AYhB3wC3JoxkbwTEdExuulQG1At1QFG8LrWnu5qGUBiGvKwTGN2QUpMikT21F6TU67p6SkojR4PJK2EJskVbgOxzMlhz9Qad7gpgFSsyW-m2WEpsL-pZJvkewZGQzSaVDf6x6rGfCFfSmFNoNnGkGQ_Ar6ysVOrHpVkyn4i7PLHuRlfH0A_02MHXiR1n3L8Pez05mSS6nyXErytuJxu2TmQrY-bd19PNi7pOoQfAeuhzysTpWkjXTV9FIRgSpOk0pxp1JEBNY-HTW4TUqp5R8zCFQRk3amLVKbqVRjbIV6-S8Q1TG2VnZsYUnZmEHcyC6SbwrDYGRLXMr7TfSg6GHi6l9PWn1xi1q4ZZlwP4MnuOlAEjIHcjyP163-4fVwge8AV0xbVyh_p39Ej5J1NBK0L716j7CQ0Q9A6MYX1Oct6zogR1xLxg4Ddxo_RlXHHqJ0MlF2xoptO9dAjB3cF9X5DG2tgVqQdI_COaAG9J8gr39ZowNOKPWV7gBZm8_QzkA9TrdXce03CBX7Hbzj1QBcp-BVpPlJ6zIkDgj-HOIgczg4FAZw4h94hu5MdKSG84aWBn6Pb2oJ0rjqc0h1ujEcEONBhYeFsLv410jE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
جانب أخر من الإشتباكات العنيفة على المحور الغربي لمحافظة السويداء السورية بين عصابات الجولاني الإرهابية والفصائل الدرزية.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88927" target="_blank">📅 02:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88926">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله أكبر  إستهداف ناقلة نفط بثلاثة صواريخ قبالة سواحل عُمان.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88926" target="_blank">📅 02:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88925">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad70a05f98.mp4?token=O6-H5Hf03_J3RD5Q2-gHoV7uwEW9kKeTP_lENfC_nIOSSL3AoLGTZ9uZ0LvrTdQVAqNrwwkXo412uBK9tW9Qt9bv_FLfmmV5FowkY9_k-0hiQCStBCEbI5YcoETjKVtSwtz5yDRvU1NsMhjsRLqAHgdebLr3tdFvjHZnIEjlMdijbBefZaZf2bWNMEdIBid2MkQkH9yYWVyx6fky4zX9PW9ZeNAjumhriUyHqy-nboNn1bKypEhLkT1Ly6_xZJve4zOjG3ECNHjVW_whOChthlYkBYUT5v7yl2ngyoID2at0Ju_vtEHEz7gRKtI8GOJIkw_XWdjqgpQ4XctUgIdBdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad70a05f98.mp4?token=O6-H5Hf03_J3RD5Q2-gHoV7uwEW9kKeTP_lENfC_nIOSSL3AoLGTZ9uZ0LvrTdQVAqNrwwkXo412uBK9tW9Qt9bv_FLfmmV5FowkY9_k-0hiQCStBCEbI5YcoETjKVtSwtz5yDRvU1NsMhjsRLqAHgdebLr3tdFvjHZnIEjlMdijbBefZaZf2bWNMEdIBid2MkQkH9yYWVyx6fky4zX9PW9ZeNAjumhriUyHqy-nboNn1bKypEhLkT1Ly6_xZJve4zOjG3ECNHjVW_whOChthlYkBYUT5v7yl2ngyoID2at0Ju_vtEHEz7gRKtI8GOJIkw_XWdjqgpQ4XctUgIdBdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  إستهداف ناقلة نفط بثلاثة صواريخ قبالة سواحل عُمان.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88925" target="_blank">📅 02:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88924">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVTGCHnDYwWTGU2AfvlQErXAfmzhM4jdYQTypNBgKEZ5h00GrvEW50SET383ZlMxcZNBjdao6NjXkxwo18H0xMrff_S2WH1emb4NpDn5vfCDrhXmyweyzMJrYrqqlPAGM0aU2Idx7tbx7dKvjTOdpMPJKaFlJEu7zJQH4fFBmbGluf6gINCyJFODaPYxH76OGtFkMoD3aKpOkCcDAmLnIiqPLMU7tO4ylHNvYd0haqQeT4SaSae2VrKpCMNChRYpZc59u7qzfw2wWzCOG6_1pbN7N39OTIaCB_G87CvKaabq5AmUytHe41KKqzxpKS_uTBe-3a5OpzUhyHJimx3j4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث امني في مضيق هرمز</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88924" target="_blank">📅 02:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88923">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حدث امني في مضيق هرمز</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88923" target="_blank">📅 02:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88922">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16d4c4b759.mp4?token=P9YqY3ULzRRGos5Gea08D-hq2tkzGO5hofKRn3zc-ge_rkTfCbTDrw7GkOT32WTxQvX7fghPCjSeV4I48jMfZH6zzR0sHzHfGubO0ov7bn9PjyFkaknuu7nuRMVh6_bzNNSm--b-ui6sjWhkngUfoP2x8jPg-YQH5nPQHXGb5ioUGx52ekEiIX9UVxQUNjmQ_2zXjCf1RoOJCfjx9VblPCZQnCY56BNm8K5EMXyuFxQJEw_vRS7KXTCv5EhohuLsAXDFFVstHnMXgt3Ia10Xp1fQF7WzvwEE56Vpi9aW0xuzGbcpEJWUCK7InIQhuf2HYSCeIJN9lSuyyyfKcWNP2DkUH6oOsot4eM7ivGEIBiLAJ20ftOKNw62DtGGczG8X8K8nha7qDyM3Z_C1aEUc6HVGD1jbvY1t_kwzyEJZc7RCgng3i4Vms6W8iMJ1lfwBMLQk8SXTfz6EHHY-S9GrIHNFIHIZgD33HTI6YaM6nUKOnVTpnl38gIgF0OGdgy4Lj9sTXPSbLlmCQnbvK4tXcAAyGFfm8YMU9Cu-1hw8tEVzOpmCeHv_nF1jyWc0zrgMOMUyTHrcDQ96EioBFDIsa-R4HMgggbLIDK0D-8msMfqq6LlgeAWUnpo6b0jnv6vgtfGDaVJhpojIbRdHAEpIQIMlAMh0AVXFf5pbdEgiiwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16d4c4b759.mp4?token=P9YqY3ULzRRGos5Gea08D-hq2tkzGO5hofKRn3zc-ge_rkTfCbTDrw7GkOT32WTxQvX7fghPCjSeV4I48jMfZH6zzR0sHzHfGubO0ov7bn9PjyFkaknuu7nuRMVh6_bzNNSm--b-ui6sjWhkngUfoP2x8jPg-YQH5nPQHXGb5ioUGx52ekEiIX9UVxQUNjmQ_2zXjCf1RoOJCfjx9VblPCZQnCY56BNm8K5EMXyuFxQJEw_vRS7KXTCv5EhohuLsAXDFFVstHnMXgt3Ia10Xp1fQF7WzvwEE56Vpi9aW0xuzGbcpEJWUCK7InIQhuf2HYSCeIJN9lSuyyyfKcWNP2DkUH6oOsot4eM7ivGEIBiLAJ20ftOKNw62DtGGczG8X8K8nha7qDyM3Z_C1aEUc6HVGD1jbvY1t_kwzyEJZc7RCgng3i4Vms6W8iMJ1lfwBMLQk8SXTfz6EHHY-S9GrIHNFIHIZgD33HTI6YaM6nUKOnVTpnl38gIgF0OGdgy4Lj9sTXPSbLlmCQnbvK4tXcAAyGFfm8YMU9Cu-1hw8tEVzOpmCeHv_nF1jyWc0zrgMOMUyTHrcDQ96EioBFDIsa-R4HMgggbLIDK0D-8msMfqq6LlgeAWUnpo6b0jnv6vgtfGDaVJhpojIbRdHAEpIQIMlAMh0AVXFf5pbdEgiiwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
استمرار المعارك بين عصابات الجولاني والفصائل الدرزية في محاور محافظة السويداء السورية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88922" target="_blank">📅 02:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88921">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇸
🇮🇶
الخارجية الأمريكية:
الموافقة على صفقة محتملة لبيع مروحيات للعراق بقيمة 800 مليون دولار.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88921" target="_blank">📅 02:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88920">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/646c905c1f.mp4?token=Nx6rNInlJHjZArbhl1ap0xf5QnonliDuC78COHzcaTjhfMxIjHS-M5XdS8eDjRl7qCw6Mtwb6QV1wCdyPx_D6sM2xCsOptoc_PLb34RCjXMMBFrcDhUBax6-RgixLnvxiyXIPP3wW5ynILusHohvX0qNy2MSarpR4tXATW_SY48F4Sy-O6jzFAPGVoOkya_9g9MZy_ppeJ9dNlM5khmp5mJ_dFhkBLJTFoEkzTaPB1fNAd29N9IDcf68OFAwu0DMnLemC7PtK3pmg59y6UWcL2j1NC9qLn-qGM2h_cH4tfF0liAZIXzyGVsbGdFTd15jwONhLcp1G4CVCxqf6zvTVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/646c905c1f.mp4?token=Nx6rNInlJHjZArbhl1ap0xf5QnonliDuC78COHzcaTjhfMxIjHS-M5XdS8eDjRl7qCw6Mtwb6QV1wCdyPx_D6sM2xCsOptoc_PLb34RCjXMMBFrcDhUBax6-RgixLnvxiyXIPP3wW5ynILusHohvX0qNy2MSarpR4tXATW_SY48F4Sy-O6jzFAPGVoOkya_9g9MZy_ppeJ9dNlM5khmp5mJ_dFhkBLJTFoEkzTaPB1fNAd29N9IDcf68OFAwu0DMnLemC7PtK3pmg59y6UWcL2j1NC9qLn-qGM2h_cH4tfF0liAZIXzyGVsbGdFTd15jwONhLcp1G4CVCxqf6zvTVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اعتقال عدد من أصحاب المولدات في عدة مناطق من العاصمة بغداد، بعد إعلانهم الإضراب احتجاجاً على حصة الكاز.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88920" target="_blank">📅 01:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88919">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1a03803b.mp4?token=hb2mgLTcHpbFRrzxxJUzATcasZH4VzBZhF2qVmNSb274zai5w1Lfj6f8MZZkVV8U5UL-AgquAkm0Kp_KDIwgzszp5N12dT8TcMMfDXdYV_RlougQl9zlTryM64wOl3EJhDMX_dXAAIbxRnW_qrXqbW6rNykH1-G2l5lNwZeaNq4letZj-20TR8c-hBwX6c3G-S40w_NjB_4Of1BR4V5uVL3GQX6kkW8Vq5l73zJF9bKW4JkieZYSxxYwllSVLnDlpQoJnw-waEzvhhROnWwYoGA5c3hdKy0HFjar-CVpqKG4cNopaQU_jf7Ts_deQYZYIE8WGnstvHBZEiNyqMhTYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1a03803b.mp4?token=hb2mgLTcHpbFRrzxxJUzATcasZH4VzBZhF2qVmNSb274zai5w1Lfj6f8MZZkVV8U5UL-AgquAkm0Kp_KDIwgzszp5N12dT8TcMMfDXdYV_RlougQl9zlTryM64wOl3EJhDMX_dXAAIbxRnW_qrXqbW6rNykH1-G2l5lNwZeaNq4letZj-20TR8c-hBwX6c3G-S40w_NjB_4Of1BR4V5uVL3GQX6kkW8Vq5l73zJF9bKW4JkieZYSxxYwllSVLnDlpQoJnw-waEzvhhROnWwYoGA5c3hdKy0HFjar-CVpqKG4cNopaQU_jf7Ts_deQYZYIE8WGnstvHBZEiNyqMhTYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ظلام دامس يخيّم على عدد من مناطق العاصمة العراقية بغداد بعد إطفاء المولدات الأهلية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88919" target="_blank">📅 01:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88918">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
أمريكا تنهار من الداخل.. وول ستريت جورنال:
‏استقال وزير الجيش الأمريكي دان دريسكول بعد أشهر من الخلاف مع هيغسيث.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88918" target="_blank">📅 01:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88917">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇸🇾
اشتباكات مسلحة بين عصابات الجولاني والفصائل الدرزية عند اطراف محافظة السويداء السورية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88917" target="_blank">📅 01:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88916">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb9c56e9a.mp4?token=p2pm689QmrXPc_5r5Yvapqv-MscxeWHs2XNqMtyxiQqDyoHxQpROf812rWcPatVceLlSiifeWs2yvBeVlz4S4H0h_nS13MGRTp478v8pJNAN9AzQFtKQLijXMVDXN9eYR9d5Mf6ZnnQzXec-aFRfOKIlQAXfzp7blNxJs2nQgEolq7QT9-x26cXEzFboFikzgnhS0YGBQge-s8S8B0oa3f5YfYRQqAVYzy4_X-jnYe8dMYEqAUyxV97aQIcPljcj_aHounxlU46ZgjifVhi25pZwY6e0W9ZRqXTT7xDJlOfFQm6PdG9YO9ljzt2mie5Zgo3RToh3Oa3cyjFc9tlB9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb9c56e9a.mp4?token=p2pm689QmrXPc_5r5Yvapqv-MscxeWHs2XNqMtyxiQqDyoHxQpROf812rWcPatVceLlSiifeWs2yvBeVlz4S4H0h_nS13MGRTp478v8pJNAN9AzQFtKQLijXMVDXN9eYR9d5Mf6ZnnQzXec-aFRfOKIlQAXfzp7blNxJs2nQgEolq7QT9-x26cXEzFboFikzgnhS0YGBQge-s8S8B0oa3f5YfYRQqAVYzy4_X-jnYe8dMYEqAUyxV97aQIcPljcj_aHounxlU46ZgjifVhi25pZwY6e0W9ZRqXTT7xDJlOfFQm6PdG9YO9ljzt2mie5Zgo3RToh3Oa3cyjFc9tlB9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ظلام دامس يخيّم على عدد من مناطق العاصمة العراقية بغداد بعد إطفاء المولدات الأهلية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88916" target="_blank">📅 01:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88915">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حدث بحري لسفينة عند السواحل العمانية بمضيق هرمز اثناء محاولة عبورها المضيق.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88915" target="_blank">📅 01:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88914">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ ايرانية نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88914" target="_blank">📅 00:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88913">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇾🇪
اطلاق عدة صواريخ من اليمن نحو تحشيدات المليشيات الموالية للسعودية في المخا.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88913" target="_blank">📅 00:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88912">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇾🇪
اطلاق عدة صواريخ من اليمن نحو تحشيدات المليشيات الموالية للسعودية في المخا.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/88912" target="_blank">📅 00:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88911">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
‏ترامب: لقد استبعدت استخدام سلاح نووي ضد إيران.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/88911" target="_blank">📅 23:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88910">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F19idNbGZ6MDPf1CHNIw7mJrPIIa90XC4ORhx5EInAy-nK6HKzYIXTGjDIsM_J3vBLBBs4r0KqKo3Md3XzUFJcAtEOtBNqxYyqzTqCoKVI4QrhdzT8buurAE_X34lY6JfIQDrBRQ2u-3M-lkq2S1lQEokFNQlw1UKTw-XNJuUva7n5dMkEzEDVvUA-LXHU29EqdNwb3UbjpJ8Ff3s938maZk2ZMwUN-vw9aXGNjKZed0DHDvypp0eJg_PQvI-_T8xPI7sJZXANEHFzqjxDB95Qn8ppgrgXRDDmy0gIRRmNlSp2ODZqLxzjuCjkaWDpPDDPAMeENbDZyUHND9Mu7ElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري لسفينة عند السواحل العمانية بمضيق هرمز اثناء محاولة عبورها المضيق.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88910" target="_blank">📅 23:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88909">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">المراسل: هل استئناف الهجمات على إيران هو حملة محدودة أم حرب شاملة؟  ترامب: إنهم دولة فاشلة... هذا لا يعني أننا لن نضربهم. سنرى ما سيحدث.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88909" target="_blank">📅 23:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88908">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇸
‏ترامب:  ‏   إن شي جين بينغ كان غير نشط نسبياً تجاه إيران. قد نضرب إيران، وسنرى ما سيحدث.  ‏الضربات الإيرانية ستكون محدودة.  ‏مضيق هرمز في حالة جيدة للغاية.  لن تحصل إيران على السلاح النووي أبدا.  إن حصلت إيران على السلاح النووي فلن يكون هناك وجود لإسرائيل…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/88908" target="_blank">📅 23:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88907">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
‏ترامب: إيران دولة فاشلة
😫</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88907" target="_blank">📅 23:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88906">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
ترامب: لا أحد سيهاجمنا. هل تعرفون السبب؟ لأنهم أذكياء.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88906" target="_blank">📅 23:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88905">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c216c7655e.mp4?token=aUps_EQy9pFnlTpXWHcejf7LSMWLfDir92vCaBXB_5FAYqGXVtA5iZgcz9H2VOOgbiAwYiT2hs7T5Rnw2G4v8hd2-5FO6BliHpnIjBHP6IZbhEJxAb20K98RfKFC_q6YaB_l-6Ruk68n_9-2RBCs8NbDZed1yz7EENOGITo491kkhhEQBaER70tZe26A1MbrxJXi_1QZ72X8-Nzdm1_lKRxmgqnMvkaqr_nNla7CM28GtXAREw1PRnqsRSSFLbB5xl5mPA6PJOpsou_X74QsjTJ7e25spM-JoiMbRsPndU8nF0ix4Kkw8s3N36qP6TbDpy6YhxRetT0cyJg9FSu-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c216c7655e.mp4?token=aUps_EQy9pFnlTpXWHcejf7LSMWLfDir92vCaBXB_5FAYqGXVtA5iZgcz9H2VOOgbiAwYiT2hs7T5Rnw2G4v8hd2-5FO6BliHpnIjBHP6IZbhEJxAb20K98RfKFC_q6YaB_l-6Ruk68n_9-2RBCs8NbDZed1yz7EENOGITo491kkhhEQBaER70tZe26A1MbrxJXi_1QZ72X8-Nzdm1_lKRxmgqnMvkaqr_nNla7CM28GtXAREw1PRnqsRSSFLbB5xl5mPA6PJOpsou_X74QsjTJ7e25spM-JoiMbRsPndU8nF0ix4Kkw8s3N36qP6TbDpy6YhxRetT0cyJg9FSu-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب
: لا أحد سيهاجمنا. هل تعرفون السبب؟ لأنهم أذكياء.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88905" target="_blank">📅 22:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88904">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/envBa7KUeY3wFEiGPbdlu5OgZ9suGc_3DlADq5kTqUGyzZncSQ-e2ezW6uTB9Cq97LmKJZxaw9Vqd9F6Jxvq-iRWwIxE2jHogLhrvBO2tw9vONZpt4nkCI1mGQpPwMBWk8gtI4Dq9CldVS6WQ3xRaoh2_pbT4LNdtL5C2Ga2AEHD68aS_7QOLHJvBvlmlpVyZ92cqYxKHSJ4VFE6O2DHzadzidE1wrPG3kehpu_1N4LhzhQ0RMvbyuoFUQtcjK4L3-KE-wGgGgxvsoUSqksIv0AQrcTHh9zDFP50kWpWsilRlI-94yzXlgabLzp2n4zxWNx5MZPjr0kk_ULiWucGcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعار النفط تقفز من جديد:
‏خام برنت يرتفع 2.39 دولار ليبلغ عند التسوية 90.49 دولار للبرميل.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88904" target="_blank">📅 22:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88903">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الله اكبر
🇺🇸
الاعلام الاميركي:
تم إطلاق صاروخ أرض-جو إيراني على مقاتلة أمريكية متعددة المهام من طراز إف-35 كانت توفر غطاءً جوياً للسفن في مضيق هرمز.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/88903" target="_blank">📅 22:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88902">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
‏
عراقجي
: على الولايات المتحدة العودة إلى التزاماتها وتنفيذ بنود مذكرة التفاهم</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88902" target="_blank">📅 21:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88901">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
مسؤول أمريكي إن الخطة تهدف إلى تقليل خطر الهجمات الإيرانية على ناقلات النفط وسفن البحرية الأمريكية وطائرات القوات الجوية، واصفاً النهج بأنه "جز العشب.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88901" target="_blank">📅 21:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88900">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYyI4Sc4rmZyd156LqEw90hSXsiyVN59L5nOoPDnl4UqpQAFVQzgB30dMBmwirGEB_0ewe5Kp_zry9LSTip5o4JO3llZru86KTLxzyPVQ8kZRzINH6zKALDcS0GpbUlUaiVIc7kNe3ySUP1iscRvCZPyRr05K_Z01ktNJg1XOC6LisWLzF9qgIX1OMXMxPV8YUGRAe0FyxeX3lY-oEwZjM39o_Eq2xDpPsqGcFLgmGOzsOrUbE_RE10wzyvFGbnjbBeusd4n94-zBDKN7OVpQ9js2KgRjjj65STSlsDN6n-CcuMf5HlGMHL1GbiLLpzL0Rhaow3xCmB72IpH62c1CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ويد تكبل وهي كما يفتدى  ويد تقبل وهي مما يقطع   الشيخ المرحوم احمد الوائلي   تسقط الوصاية الأمريكية على العراق</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/88900" target="_blank">📅 21:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88899">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ۗ وَسَيَعْلَمُ الَّذِينَ ظَلَمُوا أَيَّ مُنْقَلَبٍ يَنْقَلِبُونَ﴾.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/88899" target="_blank">📅 21:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88898">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
هيئة الأركان العامة للقوات المسلحة والمقر المركزي للنبي محمد (صلى الله عليه وسلم):
لن نتسامح مع أي انتهاك لأي مبدأ
هيئة الأركان العامة للقوات المسلحة والمقر المركزي للنبي محمد (صلى الله عليه وسلم):
على الرغم من الإعلان الرسمي من بعض دول المنطقة بأنها لن تسمح أبدًا للجيش الأمريكي المعتدي باستخدام أراضيها وسماءها وسواحلها ضد إيران الإسلامية، ورغم التحذيرات السابقة، لا يزال الجيش الأمريكي الإرهابي يستغل أراضي وسماء ومجال تلك الدول ضد بلادنا وبعض المواقع العسكرية الإيرانية، ويشن هجمات.
كما أظهرنا حتى الآن على أرض الواقع، مع احترامنا للسيادة الوطنية لجيراننا، لن نتسامح أبدًا مع أي انتهاك، وسيكون ردنا أشدّ وطأة، وقد برهنا على ذلك الليلة الماضية ببسالة جنود الحرس الثوري الإسلامي وجيش الجمهورية الإسلامية.
لا خيار أمام الجيش الأمريكي المعتدي سوى مغادرة المنطقة، وعلى من يدعمون العدوان الأمريكي على إيران الإسلامية أن يعلموا أن قواتنا المسلحة الجبارة، بما فيها الحرس الثوري والجيش، ستعمل جنباً إلى جنب لسحق مصدر أي عدوان واستهدافه.
نحذركم أنكم اختبرتم إرادة قواتنا المسلحة وشعبنا الشجاع الصامد مرات عديدة. لا تدعوا ذلك يتكرر.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/88898" target="_blank">📅 21:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88897">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb97f9367b.mp4?token=anfAKgL7wPPvc4A0a_eRKiJAtWLSWXl7XfLKDdmR9Uln21RsW2W9OW7NyZgWG-vkre9kruzCz-ehz6dBQs88DkGDcHxiZRUNnLsovPX7U2rYr5n5mdBgEYW6CY7kGB2VNDq871EsC10-BlJoqEp-dDPRpARkDNxGB126-y4FsLn1ycJu5pOXO24OUle2HQuez7wgp51uwqZl8H0DC5wOBjTa4DPmovuN2WRBWftqbEyyrCUYuD-oU8zULWyoA4yAywNbpL4842u4F8D5N2JB52BX3a2ywDZbma_rd4n7yC2lBt4yXESwuPFTHXrhw7r9eiFVTUTlZZ3aPWsj5Tk0Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb97f9367b.mp4?token=anfAKgL7wPPvc4A0a_eRKiJAtWLSWXl7XfLKDdmR9Uln21RsW2W9OW7NyZgWG-vkre9kruzCz-ehz6dBQs88DkGDcHxiZRUNnLsovPX7U2rYr5n5mdBgEYW6CY7kGB2VNDq871EsC10-BlJoqEp-dDPRpARkDNxGB126-y4FsLn1ycJu5pOXO24OUle2HQuez7wgp51uwqZl8H0DC5wOBjTa4DPmovuN2WRBWftqbEyyrCUYuD-oU8zULWyoA4yAywNbpL4842u4F8D5N2JB52BX3a2ywDZbma_rd4n7yC2lBt4yXESwuPFTHXrhw7r9eiFVTUTlZZ3aPWsj5Tk0Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
لحظات اطلاق طائرات مسيرة نحو السفن المخالفة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88897" target="_blank">📅 20:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88896">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
ترمب فحص خطة لهجمات محدودة ضد إيران في محيط مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88896" target="_blank">📅 20:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88894">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇸🇾
اشتباكات مسلحة بين عصابات الجولاني والفصائل الدرزية عند اطراف محافظة السويداء السورية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88894" target="_blank">📅 20:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88893">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ca3414a6.mp4?token=qrJ2TDRXZ6kVzdkIERtJr8bTDSsSW8O6gMtPT6x1ZUaH4siYPwimoPse-6BfahlfI-VbOBZKpq1kYyHTKd0dZTuBthu9ZPavow5yrSIM2q3zGfKNQ8fPlF0-tCG7U86XQ-rfm_xKeigve0hxuGX4pb5IIBt-GtgxphUjYfACTWhI-qY6GPRldSYrvxykQ8-_2__R3G7niu-FNcLSwyccuD8bC50R1WZLEhLQu2Ek1jUkc0aNfKcAujLLr7LHSA46A6r2PCTMmoJ8GfwHVweqDi0QiNlMS3m7Q9jkaQjWSOgfwNwOagFffuAm6f_SWDWWSUbn6XjV6P7VkjVa8aZbRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ca3414a6.mp4?token=qrJ2TDRXZ6kVzdkIERtJr8bTDSsSW8O6gMtPT6x1ZUaH4siYPwimoPse-6BfahlfI-VbOBZKpq1kYyHTKd0dZTuBthu9ZPavow5yrSIM2q3zGfKNQ8fPlF0-tCG7U86XQ-rfm_xKeigve0hxuGX4pb5IIBt-GtgxphUjYfACTWhI-qY6GPRldSYrvxykQ8-_2__R3G7niu-FNcLSwyccuD8bC50R1WZLEhLQu2Ek1jUkc0aNfKcAujLLr7LHSA46A6r2PCTMmoJ8GfwHVweqDi0QiNlMS3m7Q9jkaQjWSOgfwNwOagFffuAm6f_SWDWWSUbn6XjV6P7VkjVa8aZbRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاقمار الصناعية تظهر ‏تمكن صاروخ إيراني من اختراق الدفاعات الجوية الأمريكية في قاعدة موفق السلطي الجوية بالاردن، وأصابة حظيرة طائرات.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88893" target="_blank">📅 20:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88892">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الله أكبر
🇮🇷
🔻
الدفاعات الجوية التابعة للحرس الثوري تتمكن من إسقاط وتدمير طائرة مسيرة أمريكية من طراز  MQ9 فوق مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88892" target="_blank">📅 19:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88891">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇸
نائب الرئيس الأمريكي جيه دي فانس حول منشور ترامب لتدمير مركز الطاقة الإيرانية في جزيرة خارك:
يحب الرئيس تغيير أسلوبه قليلًا على وسائل التواصل الاجتماعي. سيكون أول من يقول إنه لا يعلن عن عمليات عسكرية على وسائل التواصل الاجتماعي، لكنني أعتقد أنه يوجه رسالة إلى الإيرانيين.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88891" target="_blank">📅 19:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88890">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ae530ed8.mp4?token=MbMctOdbRc5Ia1lr400OD64WBNkkwbU2rdiQX_iImPzjLuhVYWXRZADBtjwwCOqo3fkFwXMoIB4GCgsuxSEl8xeQE1Eb_IkuWcmIWYEa_sPAG_zULzKAsfzQrkR-fUYkGDHFkhstnswPD-muhDSSEC8jUpv2DA1vuwA0Os2Cvjtpe9W4krkfqAggMGvmG7ybPQQ1R-3Wan1CkJkR3SENOEUF4zvMF1sYVFDfBKg7QQcBbUEbwGUN_g7jbhddxqh40bP3WIRQrRgNaQE1T_YWbnWedmsV4f5D0ANKdyfVdWSjLmO64_Olosw23SS-ZOxM3dG7FWwIn0y-wdHDxWHoVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ae530ed8.mp4?token=MbMctOdbRc5Ia1lr400OD64WBNkkwbU2rdiQX_iImPzjLuhVYWXRZADBtjwwCOqo3fkFwXMoIB4GCgsuxSEl8xeQE1Eb_IkuWcmIWYEa_sPAG_zULzKAsfzQrkR-fUYkGDHFkhstnswPD-muhDSSEC8jUpv2DA1vuwA0Os2Cvjtpe9W4krkfqAggMGvmG7ybPQQ1R-3Wan1CkJkR3SENOEUF4zvMF1sYVFDfBKg7QQcBbUEbwGUN_g7jbhddxqh40bP3WIRQrRgNaQE1T_YWbnWedmsV4f5D0ANKdyfVdWSjLmO64_Olosw23SS-ZOxM3dG7FWwIn0y-wdHDxWHoVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/88890" target="_blank">📅 19:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88889">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88889" target="_blank">📅 19:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88888">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية:
إذا كان الغرض من العقوبات هو تغيير سياسات الدولة أو ممارسة الضغط إلى الحد الذي تتخلى فيه الجمهورية الإسلامية الإيرانية عن سياساتها القائمة على القوانين وإرادة الشعب، فإن مثل هذا الأمر لن يحدث.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88888" target="_blank">📅 18:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88887">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حريق كبير داخل مطار الملكة علياء الدولي جنوب العاصمة الاردنية عمان لاسباب مجهولة</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/88887" target="_blank">📅 17:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88886">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd74b90fbc.mp4?token=vbSPWG3EAgUEznGV7plA3jip9m9GYzQXDFuYEQoE2EoB20RZ9cOl3GPicPJzQKylUyi5uovrzvetuOcZ30WfSIG0pk7X95dOP0N2rODUCtd6_8HjaVh6kPpfi4vA_u7aQKcQqePu116irSUzdSL29_DHgGY5VOGeeWZavgv-YmB5fXfh6hKr41aPPRhNEW-PeljfAq_On72P-QwJvIelm7WFoWT0LXErspPCrK94HS-yYRAxpZbvBhfnu6ecEB3LrYwhdzOVA7P_vosJH4RxOv84V7vn3-OpQsI9ZrX4yhXc0_ldDZbYx-u4hJ5XKHiUs-dG9xWvGdYIYJgQCILq1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd74b90fbc.mp4?token=vbSPWG3EAgUEznGV7plA3jip9m9GYzQXDFuYEQoE2EoB20RZ9cOl3GPicPJzQKylUyi5uovrzvetuOcZ30WfSIG0pk7X95dOP0N2rODUCtd6_8HjaVh6kPpfi4vA_u7aQKcQqePu116irSUzdSL29_DHgGY5VOGeeWZavgv-YmB5fXfh6hKr41aPPRhNEW-PeljfAq_On72P-QwJvIelm7WFoWT0LXErspPCrK94HS-yYRAxpZbvBhfnu6ecEB3LrYwhdzOVA7P_vosJH4RxOv84V7vn3-OpQsI9ZrX4yhXc0_ldDZbYx-u4hJ5XKHiUs-dG9xWvGdYIYJgQCILq1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول قوات عسكرية سعودية وأمريكية إلى محافظة المهرة اليمنية وعدد من المواقع في حضرموت على متن طائرات شحن عسكرية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88886" target="_blank">📅 17:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88885">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJurUIueMWcmjs6Roh8YReCwNUm9ixEnFhd4XZebkgALj3PunjjmplVG5pN24CT2qsFpppUwnPr1VyaIWvleLc0r4X6_60TKkzIJoZdufkqccG1KC6l6zxw0LI_9oKqfX-SdMJd28vndfHqXimNd9lV4DBO9SswPuVeVYHOYbq2yspx9Z6nsc0t5xaFZ06URDHiXyGPt4jhzUo2c1HQjqjCdgGbHmxcaKvIYuJJ-lcggZGzpY8bGntEcBWlK7fxlK0QZS1RgGZUKZ7zX6IeQHpQJVF45Itj9q7NubLKn6oNz5Sc8yB73gSs7eViNeP9B1mGFpIH0sPKgU7nieLAuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحي الله اخوة بدر وحي الله حزب الله
اليوم الذكرى السنوية لدخول كتائب حزب الله قوة ابو إسراء وباسم مع تشكيلات القوة الحيدرية " العصائب ، سرايا السلام "  لفتح حصار مدينة امرلي ستالينغراد العراقية باكورة انتصار العراق على عصابات داعش الأمريكية المدعومة من الولايات المتحدة الأمريكية..
#المقاومة_حياة</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88885" target="_blank">📅 17:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88884">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اشتباكات في البحر الاحمر بين انصار الله ومرتزقة السعودية في اليمن</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88884" target="_blank">📅 16:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88883">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
وزير الخزانة الامريكي:
قد يستغرق انهيار الاقتصاد الإيراني شهوراً.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/88883" target="_blank">📅 16:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88882">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏ترامب: سنوجه للإيرانيين ضربة قوية</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/88882" target="_blank">📅 16:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88881">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
🇺🇸
ترامب: الولايات المتحدة سترد على الهجوم الذي شنته إيران على القوات الأمريكية.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/88881" target="_blank">📅 16:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88880">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
🇺🇸
ترامب: الولايات المتحدة سترد على الهجوم الذي شنته إيران على القوات الأمريكية.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/88880" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88879">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🌟
🇺🇸
ترامب:
الولايات المتحدة سترد على الهجوم الذي شنته إيران على القوات الأمريكية.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/88879" target="_blank">📅 16:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88878">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇹🇷
‏وزير الخارجية التركي: اتفقنا على تسمية رسمية لحلفنا "حلف مكة الدفاعي" ومنفتحين على توسعة الحلف.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/88878" target="_blank">📅 15:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88877">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇹🇷
‏
وزير الخارجية التركي:
اتفقنا على تسمية رسمية لحلفنا "حلف مكة الدفاعي" ومنفتحين على توسعة الحلف.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/88877" target="_blank">📅 15:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88876">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مسؤول امريكي:
لم نستهدف جزيرة خرج في الضربات التي وقعت الليلة الماضية.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/88876" target="_blank">📅 15:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88875">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:
هناك تيارات داخل الولايات المتحدة ترى مصالحها في استمرار الحرب وترغب في استمرار الصراعات.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/88875" target="_blank">📅 14:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88874">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
القضاء العراقي:
ضبط 7 مليارات دينار و5 ملايين ونصف المليون دولار و35 عقاراً تخص المتهم الموقوف علاء محسن خلف مدير مكتب المتهم الموقوف عدنان الجميلي، وذلك إثر التحقيقات الجارية معه.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/88874" target="_blank">📅 14:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88873">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">▫️
الحكومة العراقية:
- رئيس الوزراء سيجري جولة أوروبية لزيارة باريس وبرلين خلال النصف الأول من أيلول تلبية لدعوة رسمية.
- ‏نصدر 2,000,000 برميل نفط عراقي والصادرات العراقية النفطية تمر بانتظام.
- تم تخويل وزارة النفط بمنح 35 لتر لكل (كي في) ويكون سعر الوقود للمولدات مدعوما</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/88873" target="_blank">📅 13:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88872">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIvxRVLhGuv1FOk9bvbPgeIyFbr8I85ysqqhFITdzmSFQjUtLWr5mW0q6njMvo8z5KPpGrEdX-JA-yk7pa-Sto1sLYelce5teA4YZT_HZ9-nWtpxF81qMPlFqjOkxypzVMcLBNN9BEif_vFkdhRmBmPCuRXVh-tly0nOE3btCid9glnt93KKq_IZJBZlLpCXLAt4r-uUCcOeI2N864zh26d75xZRpqCmdDaxL6Qna3g60Ob9TlhFn75wau9e3D7hVss1oHKfq6WMEunWDpPZ0uKnE78Qoffj-SGbLwvoSPAYZeK4FGsXa9La_Q4Q8AMUvU7IgY-x4-QeikMvg4smxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتل عمران زراري أبن شقيق النائب في البرلمان العراقي عن الحزب الديمقراطي الكردستاني بايز زراري خلال اشتباكات مسلحة في ناحية دارشكران ضمن محافظة اربيل</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/88872" target="_blank">📅 13:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88871">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">#ترفيهي
🇦🇪
الامارات تقر بالهجوم الايراني رسميا وتقول انها تحتفظ بحق الرد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/88871" target="_blank">📅 12:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88870">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترفيهي
🇦🇪
بعد أن أعلن الجيش الإيراني استهدافها بالمسيرات.. وزارة الدفاع الإماراتية تنفي استهداف قاعدة المنهاد الجوية بالصواريخ.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/88870" target="_blank">📅 12:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88869">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
متحدث الحكومة العراقية:
موعد 30 أيلول المقبل سيشهد الانتهاء التام لتواجد بعثة التحالف الدولي على الأراضي العراقية.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/88869" target="_blank">📅 11:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88868">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇸
‏
مسؤولون أميركيون:
نراقب هرمز وسنهاجم من يهدد الملاحة هناك.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/88868" target="_blank">📅 10:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88867">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇶
الشيخ حيدر الغراوي اعزه الله:
الوفاء الحقيقي لرسول الله (ص) لا يكون بالشعارات وحدها، وإنما بالثبات على الحق ونصرة المظلوم والوقوف في وجه الاحتلال والعدوان.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/88867" target="_blank">📅 10:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88866">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترفيهي
🇦🇪
بعد أن أعلن الجيش الإيراني استهدافها بالمسيرات..
وزارة الدفاع الإماراتية تنفي استهداف قاعدة المنهاد الجوية بالصواريخ.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/88866" target="_blank">📅 10:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88864">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa1a420d2d.mp4?token=o_bdW8S9VYU5Dt-KSnqmVttHuYFR1-yk5ySum7EeG_Yh9AJtHDyI25LslYEJmQMUvFSgEHuzyEuufFHx8yofQYOyHl83wjmi_kn-8YBtXDffeQ0vY6KXr1ooGmnlsAt1gMVMxeUJ0Au4zZmT0c0ob8IfWuvixvLRTdvV8JmgprJth9F1SdCsmV4End_wbOOPyrW1W1T0yDPgtIxvN22J8GhWPTuWAUKQAxHr6CnpHBkm0GI42bjodXj_Ez2mBF-UviDNaNkIZ4UYu-q0aewXzwp5EiDqMVLA5O6A-IzKMiMx5eDTsJjeejmOPDoMJKzTiwC2p6YVkzR3jora0YgGSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa1a420d2d.mp4?token=o_bdW8S9VYU5Dt-KSnqmVttHuYFR1-yk5ySum7EeG_Yh9AJtHDyI25LslYEJmQMUvFSgEHuzyEuufFHx8yofQYOyHl83wjmi_kn-8YBtXDffeQ0vY6KXr1ooGmnlsAt1gMVMxeUJ0Au4zZmT0c0ob8IfWuvixvLRTdvV8JmgprJth9F1SdCsmV4End_wbOOPyrW1W1T0yDPgtIxvN22J8GhWPTuWAUKQAxHr6CnpHBkm0GI42bjodXj_Ez2mBF-UviDNaNkIZ4UYu-q0aewXzwp5EiDqMVLA5O6A-IzKMiMx5eDTsJjeejmOPDoMJKzTiwC2p6YVkzR3jora0YgGSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
😆
ترمب: جزيرة "خرج" الإيرانية تتعرض للتدمير</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/naya_foriraq/88864" target="_blank">📅 06:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88863">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏
😆
ترمب: جزيرة "خرج" الإيرانية تتعرض للتدمير</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/88863" target="_blank">📅 05:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88862">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c79390d1f.mp4?token=Fx2U6vhKijwSb9cneo_H3zkxlPd02Ye0bZBRjiULh9lMtAATrCKeuAieY-1yvDUOb5gLqrMS9ZSh6q90et32myiIGl-gQPFfdiS1GeTH7JY7jvvgfqRlLDof-EablHoDRBONxS9fbl779v0lBXPqrEJlhEI0oDJQxbSEvGbYDsO92jTXjvtVv0fD4YHDPohwWW75rImuMXpeLXZCiUFWJh0z4lkZu1J811NAgUtO8zpS_uVOoylw4XyU9T4SFhfA-mb2XtnPG3jMpYJW5zx4OQkpeSpDLlERuVNtgS5btyGAm_R4hVSOWbZCA8g4RBGHZcGDO93SoeKpL-ELZnBH_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c79390d1f.mp4?token=Fx2U6vhKijwSb9cneo_H3zkxlPd02Ye0bZBRjiULh9lMtAATrCKeuAieY-1yvDUOb5gLqrMS9ZSh6q90et32myiIGl-gQPFfdiS1GeTH7JY7jvvgfqRlLDof-EablHoDRBONxS9fbl779v0lBXPqrEJlhEI0oDJQxbSEvGbYDsO92jTXjvtVv0fD4YHDPohwWW75rImuMXpeLXZCiUFWJh0z4lkZu1J811NAgUtO8zpS_uVOoylw4XyU9T4SFhfA-mb2XtnPG3jMpYJW5zx4OQkpeSpDLlERuVNtgS5btyGAm_R4hVSOWbZCA8g4RBGHZcGDO93SoeKpL-ELZnBH_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ارتفاع أعمدة الدخان من مصفى الدورة جنوبي العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/naya_foriraq/88862" target="_blank">📅 05:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88861">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e138b9204f.mp4?token=kBYwiPOxLOj7OPESiBa_1_oshWd_W7HYG_KVaFji3P9D0fI3H_Nxwi55GyLSq7gjas3C_Cd6ov4U8SXE2Esb8O991eN0NGtOidigFBSUZzNcvJMnNN-xkoEna_e_YgTJRBOAZrcd5wQDgwAYpa8FOS3aeLc2y2C4GN-Ov42IUQHeNQm1VvhoFx-0RH4f3hR4BVZOOqOrfEGa3EuoLtHqeuJxwC2c6iVBiQb3Mlm3ezQNvR0GI_ox0Y3NgOOeFi9KEuxEBFiU4P1eWnlKOgqjdfIDP9iJ4shxG-Qttzs_yD5W6kyoeu4yS5czKuVPsWtTPOJ6PpYWkFr4cvXv5n2URg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e138b9204f.mp4?token=kBYwiPOxLOj7OPESiBa_1_oshWd_W7HYG_KVaFji3P9D0fI3H_Nxwi55GyLSq7gjas3C_Cd6ov4U8SXE2Esb8O991eN0NGtOidigFBSUZzNcvJMnNN-xkoEna_e_YgTJRBOAZrcd5wQDgwAYpa8FOS3aeLc2y2C4GN-Ov42IUQHeNQm1VvhoFx-0RH4f3hR4BVZOOqOrfEGa3EuoLtHqeuJxwC2c6iVBiQb3Mlm3ezQNvR0GI_ox0Y3NgOOeFi9KEuxEBFiU4P1eWnlKOgqjdfIDP9iJ4shxG-Qttzs_yD5W6kyoeu4yS5czKuVPsWtTPOJ6PpYWkFr4cvXv5n2URg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ارتفاع أعمدة الدخان من مصفى الدورة جنوبي العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/naya_foriraq/88861" target="_blank">📅 05:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88860">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
ما تسمى القيادة المركزية الاميركية:
زعم الحرس الثوري الإيراني في بيان صدر مؤخراً أن الضربات التي شنتها القوات الأمريكية لمنع الحرس الثوري من زرع ألغام في مضيق هرمز كانت "عملاً عدوانياً". هذا الادعاء باطل تماماً.
اتخذت القوات الأمريكية إجراءً محدودًا ودقيقًا ضد قوات زرع الألغام التابعة للحرس الثوري الإيراني التي كانت تشكل تهديدًا وشيكًا في مضيق هرمز. في جوهر الأمر، إيران هي من خلقت هذا التهديد، وقام الجيش الأمريكي بإزالته لحماية البحارة المدنيين، والشحن التجاري، وحرية حركة التجارة العالمية.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/naya_foriraq/88860" target="_blank">📅 04:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88859">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
🔻
الحرس الثوري:  لحظة إطلاق الصواريخ في عملية "محمد بن عبد الله (ص)" المشتركة بين الطائرات المسيرة والصواريخ، والتي استهدفت البنية التحتية والمرافق الفنية ومواقع تمركز طائرات العدو في قاعدتين جويتين أمريكيتين في الأردن، وهما قاعدة "الملك حسين" و"الأزرق"،…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/naya_foriraq/88859" target="_blank">📅 03:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88858">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترفيهي
🔻
الجيش الأردني:
اعتراض 8 صواريخ اخترقت المجال الجوي للمملكة.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/naya_foriraq/88858" target="_blank">📅 02:57 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
