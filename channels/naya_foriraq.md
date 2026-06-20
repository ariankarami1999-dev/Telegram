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
<img src="https://cdn4.telesco.pe/file/s_eoxiJp--qJNHzDngtVVa_VYLSaiLtqTANDTTZTaIf269bt4pxV7aGtUkGLbYu0TOZwtcQ1yuSCvJewufIp9GogdzjABTC1QYUKbdhmSVWkvJbfcddKl5NDzhpK-NeVZBsvxwqnKASvCS1jLeXLuuxoddxiolPwd-090JhKQLm6-l64OvsqqOwQlGfyG0GguuPP_muoHf-xeVVMXnaNjY2Mq8zqrdNkrJHiYBPHKQmGut3qkFXsw6vKHNh7mNGMjcfJwZBRHiZyxBaFRFJsueYYo4kt1c6cSIu14QONwkU8BQizeszEmXeD-NyxyAXGV5S6WS5Uf-22TbdCmXiF4w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 257K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 15:53:56</div>
<hr>

<div class="tg-post" id="msg-79376">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🫡
وزارة الداخلية العراقية توجه بتشكيل لجنة تحقيقية عليا للتحقيق في حادثة وفاة شخص يحمل الجنسية اللبنانية كان قد أُودع التوقيف في العاصمة بغداد إثر مشاجرة مع أحد أقربائه.</div>
<div class="tg-footer">👁️ 504 · <a href="https://t.me/naya_foriraq/79376" target="_blank">📅 15:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79375">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة طير حرفا جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/naya_foriraq/79375" target="_blank">📅 15:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79374">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrOlyOv4VQwb5s7OCxjwqg45HepwC3Swt-G9_kDzs837JE-o3Y0c3ncPd1M3Oi_ak-PwbPEYmbuQHX1CXYAcRytBweAt078_H_bx2kY96nDeRldwxb8Yxuex-X3Lw-_gZ5rEze7W3ww5aEBDm9MNDPNe7-Mo1ReA0lf-bvRh8j00RBSKOFh_3TOFTQTENvdOrRx0If1-mPBOBCC96OwYTTyfwzPN-IC7kG6TE9G7bC-RzihEZzfZUzQScKaipfXVB04opZZtDuHBQKtCoqcB9ir7BIkOu_FhF7Dn_GSBlOVKQqIzG4Fy_w-nfhO1acbF9BMq0SPbijgyBEOB8_TR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
عائلات شهداء مدرسة ميناب ترفع دعوى قضائية رسمية ضد الولايات المتحدة.</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/naya_foriraq/79374" target="_blank">📅 15:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79373">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inh8EctQUZXu77Y1gkLHVa_RWaumdsfEmVpmfcgRyjH72vZzEbYry_C1crQnCApVfUrGf5sH3Zoi9JXO0gcVBxydgKD2s2uZqXzPTdXvHP6oiubPZGQ7U1pF3urZ190ID5bSBNxTNUq1OWp4GZ6z4vQUndnUm5Jlp_IyZeybzaxc4jEaY6s7HFu56mNiLXu9J5juEjwO_Mq1ChvdskIEofAW_VP3hQMI8e-0O6Vco1v95VcRUW7Jb4aEnZgXGNx7NMQxsBxVULXxTcIJNX65oSvpJ0TX9l_hxt0yb9MsNTnbE4dGDo4TTEN0WvWn5od4eLiK555HfWsKe-MLi2GUUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب يصعد تجاه ايطاليا:
طلبت رئيسة الوزراء الإيطالية، جيجيوريا ميلوني، مرارًا وتكرارًا، التقاط صورة معي خلال اجتماع مجموعة السبع في فرنسا. إنها لا تحظى بشعبية كبيرة في إيطاليا، ربما لأنها رفضت الولايات المتحدة الأمريكية، وهي دولة تحب إيطاليا وتحميها حقًا، عندما يتعلق الأمر بمنع إيران من الحصول على سلاح نووي أو تطويره (لكن الناتو فعل ذلك أيضًا!). حتى أنها لم تسمح لنا باستخدام مدارج الطائرات الإيطالية، وهو ما يمثل عائقًا لوجستيًا كبيرًا، وذلك على الرغم من حقيقة أن الولايات المتحدة تساهم بمئات المليارات من الدولارات سنويًا لحماية إيطاليا، وغيرها من حلفاء الناتو "المزعومين".
الآن، بعد أن هزمت الولايات المتحدة إيران عسكريًا، تريد أن تكون صديقة مرة أخرى من أجل رفع "أعدادها". لا شكرًا!!!</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/naya_foriraq/79373" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79372">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇨🇭
اعلام سويسري:
وفود تحضيرية لإيران والولايات المتحدة وباكستان وقطر تعمل منذ أمس بمنتجع "برغنشتوك" تحضيرا للمحادثات ولا أثر بعد لرؤساء وفدي طهران وواشنطن.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/naya_foriraq/79372" target="_blank">📅 15:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79371">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fea425d27.mp4?token=DK_vjedG2yxGln2dUKusK1jH6laC2ZtYKjgqzZeEIu5l4LmnUA6puIMyONvfZcZ960BrepW-Vs0QRycFOFbAbxl3KLMBh1DDFVqqSCZGuWJ3LVTfHuxptSsBhJzwkLlKnM0sskP-4z2cVnWFSHxoNQlVm12tW60jmyP0kaxgJZgmrA84wRmM62iswtvaOJQpgeN1O1hdzbAfxYTX-W_EKfIWQ2vJEfYLiXNiWb4tRT9ZESNNUWS2hrqOl1t9dStW1m0Nt2yIbtgAEYn5HexwIqVxH82V0hE3OHKd9LKhZLizchh6Ll87vlxM1bX-NAkx03F2qjEh4QGQ_wMHpI3Ybw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fea425d27.mp4?token=DK_vjedG2yxGln2dUKusK1jH6laC2ZtYKjgqzZeEIu5l4LmnUA6puIMyONvfZcZ960BrepW-Vs0QRycFOFbAbxl3KLMBh1DDFVqqSCZGuWJ3LVTfHuxptSsBhJzwkLlKnM0sskP-4z2cVnWFSHxoNQlVm12tW60jmyP0kaxgJZgmrA84wRmM62iswtvaOJQpgeN1O1hdzbAfxYTX-W_EKfIWQ2vJEfYLiXNiWb4tRT9ZESNNUWS2hrqOl1t9dStW1m0Nt2yIbtgAEYn5HexwIqVxH82V0hE3OHKd9LKhZLizchh6Ll87vlxM1bX-NAkx03F2qjEh4QGQ_wMHpI3Ybw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
زعيم ما يسمى بـ"المعارضة الاسرائيلية" يائير لابيد:
دفع نتنياهو بالخطة الكردية دون مراعاة رد الفعل التركي المتوقع وتأثير أردوغان في واشنطن. أردوغان أعطاه درسا</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/naya_foriraq/79371" target="_blank">📅 15:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79370">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGaq20Z8PH8RBtiv88bgsNHMHhFAcU_nlQ9f-mRTsPeNRNROOy6uSxRPTSfMWDEshFjFFrvfAvTN1AmusHc1rmFIYpVNkmL7K7BG6bn9MZiTsBsbBFz0fc9fG2VijacNI6yVbWJpGTisaQ3u3DZxvDast-Nax1mhXNBOl3Uj9gdfUcRyC6OxRu2VNjOV_OKvhCeNuBys7TNYMr1FJTLIaq-LwJXmxaYAOJMOEPAT3UjzsWpWkmre_3jSYTaO8W2DEcuEZgLKYqAd0ZHyCu6oj86168Bi1Tf2kwNI970Jwza6ajGINiJsESkWBry7lROgjSF1IvUV56OSMazL3A5TdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
المنشور الأخير لمدير عام كهرباء الوسط علاء الجبوري قبل اعتقاله بتهم فساد والذي سارع أدمنية الصفحة إلى حذفه بعد الاعتقال</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/naya_foriraq/79370" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79369">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e875b0f6c7.mp4?token=ZH2MbOs29kRFf0YcPm5tbDaWLrs45YC5GedKZh3F-E1EoMTm1EH58oWBAA84TYPE3JVY5WzjGO7m3tv1rznWSV1UBZlEiE7afvhEE1twaX1lf7UybCex5O-JvaSzR2aDUzcrDTfA6Mjkz8k4kUwbfERRHQe54t2DsoFU9kNDL52I0DBRg3sv0aPIv8tmAJrYcB9GKxoDw6g0h0n9sjZLelb0ykj6hq4cMPuYDxl8-OicD5R5jDVpcSbk2HaWCJXbLbMq8n2U29ns8Hh49RUhxeegY2h56faXwRpqRy4RCB0cfwN_PYbJa-CPRUAjelgtJWXoIaDODtgtTOpj1cKrgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e875b0f6c7.mp4?token=ZH2MbOs29kRFf0YcPm5tbDaWLrs45YC5GedKZh3F-E1EoMTm1EH58oWBAA84TYPE3JVY5WzjGO7m3tv1rznWSV1UBZlEiE7afvhEE1twaX1lf7UybCex5O-JvaSzR2aDUzcrDTfA6Mjkz8k4kUwbfERRHQe54t2DsoFU9kNDL52I0DBRg3sv0aPIv8tmAJrYcB9GKxoDw6g0h0n9sjZLelb0ykj6hq4cMPuYDxl8-OicD5R5jDVpcSbk2HaWCJXbLbMq8n2U29ns8Hh49RUhxeegY2h56faXwRpqRy4RCB0cfwN_PYbJa-CPRUAjelgtJWXoIaDODtgtTOpj1cKrgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
فوضى واعتداء داخل محكمة كركوك بين احد المواطنين وعناصر امن.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/naya_foriraq/79369" target="_blank">📅 15:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79368">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏴‍☠️
🇺🇸
السفير الامريكي في تل أبيب مايك هاكابي مجددا:
لو لم تكن اليهودية موجودة لما كانت المسيحية موجودة، ولما كانت الحضارة الغربية موجودة ولما كانت أمريكا موجودة.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/naya_foriraq/79368" target="_blank">📅 15:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79367">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏴‍☠️
جيش العدو الصهيوني:
في عدة حوادث مختلفة خلال الليلة الماضية أطلق حزب الله أكثر من 50 عملية إطلاق باتجاه قوات الجيش في جنوب لبنان. سنرد بقوة على أي اعتداء</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/naya_foriraq/79367" target="_blank">📅 15:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79366">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ويتكوف وكوشنر يصلان إلى سويسرا</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/naya_foriraq/79366" target="_blank">📅 14:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79365">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptWYRFsenMRZ0snD_PBdlhwBjS16LUuzdFcmWv3-lR3nfuVaGhpILvyF-6A4ASQ0BXxDA8pOp-6NcJQCWCp9pYm6aOeHQnL1dPoFTBLqPYHzB6EyENp9QYAfDZZCGVJ0fukRJUbujg-xyhgogvgTS3ba0usS8BD-ageY_JS46ySvNQ1zZ6p5VYGWkv225z0_v_uDgmjnYuYSI6OIxnpFlwRSBRMtd1j01pQA2_0OuiCwA5lMa3qLmV3W2uRFE0lTZ84AdZ5-Ykwth_4114nuvAS2LpURBHr7HRVktkxm_4jrowjSQXXs6-nXnyO0tIofQmCndS45e0djljpIOXHJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇱🇧
حزب الله:
ملتزمين بوقف إطلاق النّار، لكن لن نتهاون في التّصدي لأيّ محاولة يُقدم عليها العدوّ لقضم الأراضي وتوسيع احتلاله، وسيكون مجاهدينا بالمرصاد، وبكامل جهوزيّتهم، للدّفاع الكربلائيّ عن أرضهم وشعبهم ووطنهم</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/naya_foriraq/79365" target="_blank">📅 14:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79364">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otIdVlCGdcDC4Kb3TqwS1pzgEm6X9apA0s05qd4VvZZeoEVzZvvnavgRRIFG1BsowY4aUElwzdcAZr0aBRcLjbBXjUR60Pp5zUpKpNqGc72zQa2X1SzWch8YW5M01u9n6bJmLwKblz-NtV18AC0GW_S2J7PssvzbdANvRcQFhZlfyGQAdy-XEdCQPnx_wiCk_oPf4wODNq8FhczgYaXMNoEbyiF9aJHoavD9v0w0tyDMmNi6oQEKnQOutoktvHMl-pLfRekmYmEfzFbkOsI7Jw-4CRNsDh1iq2X5HGOgmziQQ2ZA_ffpWwTGjLf6UT3l9vnwn7b77B37aWunrwBTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب
يدرك الحمقى اليساريون المتطرفون والديمقراطيون مدى نجاحنا في حربنا ضد إيران، حيث هُزمت بلادهم عسكريًا بشكل كامل. استمر أوباما في منحهم مليارات الدولارات نقدًا، ولم يستخدم جيشنا المنهك آنذاك لما كان ينبغي فعله لكبح جماح إيران، الراعي الأول للإرهاب في العالم. لم يكن لديهم أي احترام له. اعتقدوا أنه، مثل جو بايدن النعسان، زعيم ضعيف وغير فعال، وكانوا محقين تمامًا في ذلك. أفلتت إيران من "القتل" لمدة 47 عامًا، حتى جئت. ثم تغير كل شيء. أمريكا عادت!!!</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/naya_foriraq/79364" target="_blank">📅 14:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79363">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK0gcdY4T4oBoDPtS6LsrWluCT_yBWL8BDId4uGRrUZvBrfvwSlxdXVjs5Q09J60t-rf5NtXaejZDb6IoZnJs-3GnCcxZWbKjsi1JFG-0T1_UJ-ArEGxuqxpCMMU3a60fhIJIvqxgLgE3tjd5oIN7qVUzig2ngmMY0hwdp6ZRDfsiVxWeFLbbLV5B2bSRNs0BMjO238B8x-a1ot6P87w-Dp4Ypt3m90Gc5vlJRsuSLy4HPxBhbZtZNWrUJlM5LMh0qF5Cdu6yk-9JnSqfASYXTl9ASejASQ-VB4fnYEx_6XbqNWSCzXlvsN86VgRVJIQ1ri8dyyXR6tx-i_qSemokw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🏴‍☠️
المتحدث باسم وزارة الخارجية الايرانية يشارك تصريحات لسفير النظام الصهيوني في الامم المتحدة ويعلق:
هذا الاستعراض المخزي للتحدي المتغطرس - ضد العقل والقانون والأخلاق والعدالة - هو نتيجة حتمية أخرى للإفلات المطلق من العقاب الذي منحه عوامل التمكين لنظام إرهابي الفصل العنصري. يواصل هذا النظام حملته للإبادة الجماعية ضد الشعب الفلسطيني وفي جميع أنحاء المنطقة بتجاهل تام لجميع المعايير المتحضرة. لقد حان الوقت منذ فترة طويلة لكي ينهض العالم ويواجه هذا التهديد الخطير وغير المسبوق للسلام والإنسانية.</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/naya_foriraq/79363" target="_blank">📅 14:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79361">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-text">من بغداد، من أمام السفارة الإيرانية، اجتمعت جماهير المقاومة الإسلامية احتفاءً بانتصار الجمهورية الإسلامية الإيرانية في مواجهة قوى الاستكبار.
آلاف المشاركين لبّوا دعوة المقاومة الإسلامية كتائب سيد الشهداء، مؤكدين أن خيار المقاومة ما زال حيًّا في وجدان الأمة.
في رسالة واضحة بأن نهج المقاومة باقٍ ومتجذّر، وأن إرادة الشعوب لا تُهزم أمام التحديات.</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/naya_foriraq/79361" target="_blank">📅 13:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79360">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇨🇭
‏سويسرا تقرر تمديد التدابير الأمنية في البلاد حتى 22 يونيو في انتظار موافقة الجانب الايراني على استئناف المفاوضات.</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/naya_foriraq/79360" target="_blank">📅 13:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79359">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">📰
نيويورك تايمز عن مصادر:
مسؤولون غربيون طالبوا نتنياهو بوقف مهاجمة لبنان كي لا تبرر إيران انسحابها من التفاوض.</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/naya_foriraq/79359" target="_blank">📅 13:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79358">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تحليل نايا...تلة علي الطاهر.. لماذا تسعى إسرائيل للسيطرة عليها رغم الخسائر؟  تُعد تلة علي الطاهر من أبرز المرتفعات الاستراتيجية في قضاء النبطية جنوبي لبنان إذ يبلغ ارتفاعها نحو 700 متر فوق سطح البحر ما يمنحها إشرافًا واسعًا على عدد من البلدات أبرزها مدينة…</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/naya_foriraq/79358" target="_blank">📅 13:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79357">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
مقتل جندي إسرائيلي وإصابة 11 آخرين بنيران حزب الله في منطقة علي الطاهر خلال الليل.</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/79357" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79356">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
🇮🇷
وزير الداخلية الباكستاني يصل إلى مشهد تمهيدا للقاء مسؤولين إيرانيين</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79356" target="_blank">📅 12:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79355">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fdcf3568f.mp4?token=MjMZT9M8pI12yPv213eNRc77I7etGHYVH10c8Y0QtknG5UpOKjsc4ysYJi8Ewg0G_xdw0RKMvuVrrraCW9xOS4QfEMd2p337mPFx9PeDOCYimHxpxOK7aVg7O9-x92Sx64OtmCBK9ntXTD93thKMvlCDfyj6EhZc3tl2QWONS63GgzT-tD2XtGDY7AgWqUq59lrFu4MA2Z0HbFNkj0P5MJm0njatTzP20FxU8jh2zu8yEoho2ID_Eh7fO6kxpw9PstRskQiTnKrRmifqKJWg_CCXDURMiDvHrDI1W7hi0qH325UtqRgsgNSfbqcqz92PmrJWsMI9NVAN81vPDn0YRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fdcf3568f.mp4?token=MjMZT9M8pI12yPv213eNRc77I7etGHYVH10c8Y0QtknG5UpOKjsc4ysYJi8Ewg0G_xdw0RKMvuVrrraCW9xOS4QfEMd2p337mPFx9PeDOCYimHxpxOK7aVg7O9-x92Sx64OtmCBK9ntXTD93thKMvlCDfyj6EhZc3tl2QWONS63GgzT-tD2XtGDY7AgWqUq59lrFu4MA2Z0HbFNkj0P5MJm0njatTzP20FxU8jh2zu8yEoho2ID_Eh7fO6kxpw9PstRskQiTnKrRmifqKJWg_CCXDURMiDvHrDI1W7hi0qH325UtqRgsgNSfbqcqz92PmrJWsMI9NVAN81vPDn0YRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
مستشفى رمبام في حيفا تستقبل جنود قتلى ومصابين إثر المعارك الجارية في جنوب لبنان.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79355" target="_blank">📅 12:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79352">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ez-B7DLXz4aezxKpxkjtdoKR0_GnhTngD2fx-KCIE4U9KNLuGp4Fj9u8jOafVPjGLefTnBnZw2EcaKDO1xD4CYRHR44NQn42pX1jepe776ARgGHL7Ep6ggdU_3yjTouby3BOIgh5Q_tKUl9-XbUUiqgz3qOgbrnoe0JzCIIU1tLeeqkN2TT-C3PwjjifDgrxsZRfi2ADY22jdbDbyrzx4f5EZuW9xcay0DBlvp1qfKoACDpgAn2Jdlaw6O8QNiqBCOnYBParlr4kteYS8fbyBFNGr_llO0Y0UYuIl62IggNfsHX4QLaHwp1RSji63mUQkvjX99PHJN_CGm47DZzkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CYF21i0W2YVFKrNNkt7RXbZ5VCZpsta2uALdCiubH6jPhukBMGyp0sHZKP4vklySTKJ9aPmV7nbI8d3OAWDMCC2iLhWENYg3fv_u1dQAhck_G-G-ouyMkEMP297UlBm3cielW-fxPKVR5t7NwzzNdfC4oLy5OJJ6pKRzE0Bp3eeocIkcjaCADQ-AlGym7MLcGIM1wNIAPgnn73L2GujnzCjS5wLd6l_FG3LQeIM9Xq-q0O5DPMX8OvleDkZrw1DMmSokS2Tf3C3QU-Jy2E3oEYH33agpnvv78ArnzjlVPklKEBUn1itDAgTAeZ0fGb6jq_h0E64O6kWXfbCYZXeA2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uAijdpQ_sOC9nCnb3PmKubC2libqAvBeGirJzUF9ddAhgWysLWjAFwuoDg87z-RZ_vB_ko5D7JmhCydOHSTSrh_Ixf1jOacCdCDCIDZR4Z1-BsjFPx19Y0Fga8x5beDNGqxvYBWRbmYpPEKc0OYFMR_Cb55wh8cQbNsOTPthnv5Dji00afkZGqX84nl4D2hhAspiSRpLRGl0Fx0YZHrYRdFrFR_cK5HnbVtILDY_sdtx8gNgDKj5HRtPPa5ynJmXglULu95WRAaOc_2XB4_D_Jcn-hsUUa66pAOLRUvsT94xY52OLd7ZD7Bi9Ghh5gJTZNuDCSFGR_1AwJpebY1xDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇸🇾
ضمن حملة التصفيات بين حكومة الجولاني وعصاباته.. مقتل عدد من إرهابي الجولاني إثر كمين على طريق منبج حلب.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79352" target="_blank">📅 11:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79351">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f9366af54.mp4?token=qWv0RC0n9uBNxFNdYN-Bnmydab5s_0Azf6IdwSYLpjo2i_U2sqcY6rqlAzBHnp2uaq4pgFYDqoazBwx5qFNsar_zTFXat2VwUF1egh3kr9FHJgxmXt1-63WHJiODOzJS9pavdmEcQMFNSSQ7G-Ak2KXIwC4qgL9P-7AwfO-c7qZkPkdlbr1i_0kxDUOOZbZDx21c7d-bzqsh5YZWCvcvBFP3M2QiuKn8CiCjJrbWHQrSgUL5Cvp2gsCUmDNbJOZCYzf0CeJkF3BHtkXM7F8qyc-i4Ezzmhyr8ANv87YPeJca6oo6FEl9w0_WZB3kAgvj2KB9x_uW6cjTQPNyl_bO5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f9366af54.mp4?token=qWv0RC0n9uBNxFNdYN-Bnmydab5s_0Azf6IdwSYLpjo2i_U2sqcY6rqlAzBHnp2uaq4pgFYDqoazBwx5qFNsar_zTFXat2VwUF1egh3kr9FHJgxmXt1-63WHJiODOzJS9pavdmEcQMFNSSQ7G-Ak2KXIwC4qgL9P-7AwfO-c7qZkPkdlbr1i_0kxDUOOZbZDx21c7d-bzqsh5YZWCvcvBFP3M2QiuKn8CiCjJrbWHQrSgUL5Cvp2gsCUmDNbJOZCYzf0CeJkF3BHtkXM7F8qyc-i4Ezzmhyr8ANv87YPeJca6oo6FEl9w0_WZB3kAgvj2KB9x_uW6cjTQPNyl_bO5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
من منفذ مهران الحدودي مع إيران.. بدء توافد الزوار الإيرانيين لإحياء ذكرى عاشوراء في العراق.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79351" target="_blank">📅 11:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79349">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN7KLp6FiefgHtHzXm6tz90eG4oVDenXckKV-jf8Ix1vnBNfjGqPeE09KpdooAZ1wSSVa9-lRk47w0Y6A1TqEeTZ48Yt91PjzZGsM9AC1TaR2A8xzysi11hhNqW2y6k-t61EvXixUs_R0kFEg5p8n209xDztsc9rxZm3Xbfbu0Ijl1K5WAH97a1dqOAbvE-fN-9zrX8tCV0HypAfVC1WSOpJvhuToAvipKhELYZ0CFYmXeRnqac2RCnOyYs7yj9eF-qNPzMD1VJdDf2vj40D-NY-iwmoLNFfKNrVjzReVNpYj5HyEMhPej3kUWQL5ZOoKdqsF6h2Z56XF79iRNXsZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
هيئة البث: مفاوضات ‌لبنان⁩ وإسرائيل القادمة ستحدد مناطق تجريبية جنوبي ‌لبنان⁩ سيتسلمها الجيش اللبناني
من منجزات الجيش اللبناني إغلاق قرى وبلدات الجنوب ومنع وصول سكانها إليها ؛ الصورة أعلاه من إقفال بلدة العامرية في هذه اللحظات.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79349" target="_blank">📅 10:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79348">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇷🇺
ميدفيديف من روسيا: أصبح مضيق هرمز "سلاحًا نوويًا فارسيًا" وسيتم استخدامه على هذا النحو.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79348" target="_blank">📅 10:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79347">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896e6400c7.mp4?token=s_nG69myRS7I0DuhwI44yQoJLdrJLNvGrQ21wrYs9m2NetxkqRZXhMDhHEW5d-YgU3ejgktJFrcyG0YfTu6cjrKQCyeRfLMWnCvp43N4PyN2gTDH_ctjdVKfmv310pk90OXPylRnpsPs8Y1IFbYFFBV0o_X9pHg30Pn5Pj2qensfWfgyzRE1rP3TKCcSEboYgvOba1KpbDqgUQb9Qc5tPNw3Qin5E6goV-23KNz8VZpV2RCbBvAB39Nr1RmW9-SwS8KKRFAiFxiYfKItPz2HZ5BWQ18fRW4ZL69qWB1E26aercDT6eHX8_h5qmvj3naZKX6eSZo71KVz70-iDqdQlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896e6400c7.mp4?token=s_nG69myRS7I0DuhwI44yQoJLdrJLNvGrQ21wrYs9m2NetxkqRZXhMDhHEW5d-YgU3ejgktJFrcyG0YfTu6cjrKQCyeRfLMWnCvp43N4PyN2gTDH_ctjdVKfmv310pk90OXPylRnpsPs8Y1IFbYFFBV0o_X9pHg30Pn5Pj2qensfWfgyzRE1rP3TKCcSEboYgvOba1KpbDqgUQb9Qc5tPNw3Qin5E6goV-23KNz8VZpV2RCbBvAB39Nr1RmW9-SwS8KKRFAiFxiYfKItPz2HZ5BWQ18fRW4ZL69qWB1E26aercDT6eHX8_h5qmvj3naZKX6eSZo71KVz70-iDqdQlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
لليوم الثاني على التوالي لا يزال الكيان الصهيوني يستهدف الجنوب اللبناني بغارات مكثفة وسط اشتباكات عنيفة في مناطق توغل جيش الاحتلال.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79347" target="_blank">📅 10:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79346">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ed7f3d48.mp4?token=Xk7dFah84xZKn_DzzxbOVwnJJ-KPWGxRcwPnRDkTb3Fs_WwcFp_HkEnjeX70QStMjKNWQXRCOHHJIg2CE3LTQrhMr-82ZhiOKtIQJsPXXgEAmNY4Hn24OF2UtAfU-H8uEWcxfF84__UVlQCndUn3YR047V6ZC7d8nh3J-mCVxn1GKt74a_vB77GZVEPuqfSH2tCk55pd0D2O_TQ52dHSN9OpU8XkYk1j31vSZTnI_IDBJAIQvI83A15R1kHRAZcAM5k4VoplTxxhjVLp4mhDXscrnQH6NruWrEM3RkKUBF5KEK0_wZaJVisMuAnj59M0NAFXcn-qDFhufHWzaCzGTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ed7f3d48.mp4?token=Xk7dFah84xZKn_DzzxbOVwnJJ-KPWGxRcwPnRDkTb3Fs_WwcFp_HkEnjeX70QStMjKNWQXRCOHHJIg2CE3LTQrhMr-82ZhiOKtIQJsPXXgEAmNY4Hn24OF2UtAfU-H8uEWcxfF84__UVlQCndUn3YR047V6ZC7d8nh3J-mCVxn1GKt74a_vB77GZVEPuqfSH2tCk55pd0D2O_TQ52dHSN9OpU8XkYk1j31vSZTnI_IDBJAIQvI83A15R1kHRAZcAM5k4VoplTxxhjVLp4mhDXscrnQH6NruWrEM3RkKUBF5KEK0_wZaJVisMuAnj59M0NAFXcn-qDFhufHWzaCzGTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب متحدثاً عن قاسم سليماني: عندما ترى جنودًا يتجولون بدون أرجل، بدون أذرع، مع وجه دمر تمامًا، فإن 96.2٪ منهم جاءوا من إيران.   جاءوا من سليماني. كان هذا سلاحه المفضل.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79346" target="_blank">📅 10:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79345">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bd28a2f5.mp4?token=eGNUY8HvXR_IiG12bwCEBAM4_vm1UNEMNX9FER9bsbc4NqKkF2UJvATCotsiQeIbL99b4bwwGQs-4owyfJ_hCzZ-KTvchEqz99ZLiT7MBW9BwG0K1IC9YV93-hbF73DaTzGeRwAnxopVV48ImTjXINfyNBda2-TPYfEmbrli27dOZSNnZkR4dsWB6oDX8jwhhDFxpZhdSEyqNszt_tApHsTVYN7_Hs78aVaIBeQgry0O1D5BgPgSwvKPzW2h0RR09AftsbaS9Fsj6BZHu1q2tFtfXU8K9rgGYnDsXkJYI4zP9CWsMSWDxpLSaV_URLndww0qNuaZ38wvQgRJMJ7KbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bd28a2f5.mp4?token=eGNUY8HvXR_IiG12bwCEBAM4_vm1UNEMNX9FER9bsbc4NqKkF2UJvATCotsiQeIbL99b4bwwGQs-4owyfJ_hCzZ-KTvchEqz99ZLiT7MBW9BwG0K1IC9YV93-hbF73DaTzGeRwAnxopVV48ImTjXINfyNBda2-TPYfEmbrli27dOZSNnZkR4dsWB6oDX8jwhhDFxpZhdSEyqNszt_tApHsTVYN7_Hs78aVaIBeQgry0O1D5BgPgSwvKPzW2h0RR09AftsbaS9Fsj6BZHu1q2tFtfXU8K9rgGYnDsXkJYI4zP9CWsMSWDxpLSaV_URLndww0qNuaZ38wvQgRJMJ7KbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب متحدثاً عن قاسم سليماني: عندما ترى جنودًا يتجولون بدون أرجل، بدون أذرع، مع وجه دمر تمامًا، فإن 96.2٪ منهم جاءوا من إيران.
جاءوا من سليماني. كان هذا سلاحه المفضل.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79345" target="_blank">📅 10:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79344">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd20de2869.mp4?token=mAWbjBGbrvhDJdSKWagcDTedk-mO_VOadaYrNJdeo3RJz0Ixhagkl96OxDzBlVpmSeqIxf_m6LKruJFFAI9BCOOaC-baNXxQdfTkNQtVEQLNom4JiD7lwJ36ilfLfLab8KjTUHrmuMhDTFVar83F9Fa74vZu4I_bJBO5Si9poidlej1Kiu_FfyVidCze-xadL6WO_NEJ8jR0liKTlQLnxOb88_jKJyejRA1hrBlWd7E7_kVcR_Dnptu07DueIGopAW2Z4vZcsfxrXHjBfDBUN9UEtKIhXbXkQsET180evducrMXHon2X79YIjO9yPegA2k79-EVv70sFtJxV_VFT-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd20de2869.mp4?token=mAWbjBGbrvhDJdSKWagcDTedk-mO_VOadaYrNJdeo3RJz0Ixhagkl96OxDzBlVpmSeqIxf_m6LKruJFFAI9BCOOaC-baNXxQdfTkNQtVEQLNom4JiD7lwJ36ilfLfLab8KjTUHrmuMhDTFVar83F9Fa74vZu4I_bJBO5Si9poidlej1Kiu_FfyVidCze-xadL6WO_NEJ8jR0liKTlQLnxOb88_jKJyejRA1hrBlWd7E7_kVcR_Dnptu07DueIGopAW2Z4vZcsfxrXHjBfDBUN9UEtKIhXbXkQsET180evducrMXHon2X79YIjO9yPegA2k79-EVv70sFtJxV_VFT-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
لليوم الثاني على التوالي لا يزال الكيان الصهيوني يستهدف الجنوب اللبناني بغارات مكثفة وسط اشتباكات عنيفة في مناطق توغل جيش الاحتلال.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79344" target="_blank">📅 09:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79343">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bc3683da.mp4?token=LvCHADY_buJ7zi9DNcTu-f2-NfMHF3GQsqdVq_cU2RtqjD6F2gwC8daE-UzGT7iElyfmNFk0lZJwC-qYDNXUK9vUnxgQ7jdD-eLIpyOeUl7IPhX2pxlj56dMMFw1LXNejmWDCcAbGsd-JCwrbAMvypA2RMi_awr9ko5a2_KQ5Ig8uQhWR90atsWJ0AnuOe_KVp6ttIR6FVlsM_assvoGiBvbVgDdwFwT9Meo9MSDDc5QChGYD-oDWZW4emDXgAnFIzc5NLQZyu9yjOzC6xzylv-G_rtnuSRJBxjO_F3ypOYT6vddwqH6mR6AODYLmamTOrR_qDfVDHMY300k0ZVb3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bc3683da.mp4?token=LvCHADY_buJ7zi9DNcTu-f2-NfMHF3GQsqdVq_cU2RtqjD6F2gwC8daE-UzGT7iElyfmNFk0lZJwC-qYDNXUK9vUnxgQ7jdD-eLIpyOeUl7IPhX2pxlj56dMMFw1LXNejmWDCcAbGsd-JCwrbAMvypA2RMi_awr9ko5a2_KQ5Ig8uQhWR90atsWJ0AnuOe_KVp6ttIR6FVlsM_assvoGiBvbVgDdwFwT9Meo9MSDDc5QChGYD-oDWZW4emDXgAnFIzc5NLQZyu9yjOzC6xzylv-G_rtnuSRJBxjO_F3ypOYT6vddwqH6mR6AODYLmamTOrR_qDfVDHMY300k0ZVb3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
لليوم الثاني على التوالي لا يزال الكيان الصهيوني يستهدف الجنوب اللبناني بغارات مكثفة وسط اشتباكات عنيفة في مناطق توغل جيش الاحتلال.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79343" target="_blank">📅 08:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79342">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqTPXmqlbxYYoydz3CW2xIrmt-pZCo2M7JH8yGnALnEaWe6iJMFpRHmtOMaQcD9FyfLang8wtG0tK11IxBD_gx-IHb1O_P1oDGsrrieEkHWVymk8FSss6ZU6LZTV4H-zFnVENn4eckWLhNSWO65TDN54cR12J6YY4xthsYVAxcPs1Wrl-gUIvADlp5raWBZ6WjPNqPmmXttciAj2SWSHTUJJf_apm-FApAxnQbOFN8csIllOac9K4a3Jqog8I35tTGDowaKyPlR_Niqp4ReBZN7-HVHEc9LPLuwWOo4NRcayrPAbekyZmqzTIfW_dTpoP5ZysujVSV_OmYr1EpcdBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
🇺🇸
انتشر قبل يومين خبر عن وقوع انفجارات في قضاء داقوق التابع لمحافظة كركوك شمالي العراق
وبعد البحث والتدقيق، تبيّن أن الانفجار ناتج عن عملية تفجير مسيطر عليها نفذتها القوات الأمنية العراقية لجسم حربي عُثر عليه في قرية جمبور التابعة للقضاء.
وحصلت نايا على صور حصرية
للجسم قبل تفجيره، ويبدو من المعاينة الأولية أنه من صاروخ كروز، طراز BGM-109 Tomahawk الأمريكي .وتعيد الحادثة طرح تساؤلات بشأن السيادة العراقية وقدرات الدفاع الجوي في مواجهة الاختراقات الجوية المتكررة</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79342" target="_blank">📅 08:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79341">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
🔻
🏴‍☠️
إعلام العدو معاريف :
لسنوات طويلة، كانت إسرائيل القوة التي سعت جميع دول المنطقة إلى استمالتها،واستغلت تقنياتنا ومعارفنا، وسعت إلى التقرب منا، حتى وإن لم يكن ذلك علنًا. لكن مذكرة التفاهم هذه تُحوّل دول المنطقة بعيدًا عنا ونحو الشرق، نحو الجمهورية الإسلامية، باعتبارها القوة المهيمنة في المنطقة، والتي يجب الآن احترامها واسترضاؤها.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79341" target="_blank">📅 08:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79340">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpc3zy7nTV4eOBmRunzoJp1FTL3KMwS7AirYt8YIYUaTLy4-MoXoaJ78guJreMdjOlS0_Ei-Ep9HVuTc4y9biRXXRO8zVdW4nLI60isCJ_yeJMHuZ6hf-GBW1IJAWw6nbo88ad-YO7yTTSKVYSmGuvCuH7SuADtpjO7ojVtkXysgDzIW0Z03KBVnosFySJOImSdky5zLS16OnoGvEBMAsg2lwMZLV0LhWTd5iQgxkPKjtQ6Uua2tgFYjKePzXZSs1-12-_UJOZmwLGQmyfM-Fm48PwJYw9c4ZvXLPtHKhnyVv8u6mkxlvLQal_7RzmVW8tqrogX51UAEvz2oV-wdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
ترامب متأثرا بتجربة حيدر الاكرع
تم تنظيف ٤٥ نصب تذكاري و ٢٢ نافورة ؛ مراسل ABC حاول تخريب النافورة من خلال وضع يده على مطاطة داخل النافورة فتحنا تحقيق بذلك !</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79340" target="_blank">📅 07:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79339">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7567afa506.mp4?token=nApNEx2tU1tPQ79NPd3XtMUayIkruPcD7vL4lT_TnCKUt0mQaDMcvYRKCZH2jp_IObDtr5XwTf86wzlwVMTa2oBSLeiaK6KXxImmVT4Jr2SwTIMOWPeJPMhfy7XpDZHHUteInIw7wZ7WgQBIKJ7eT-K8tJrB6APFP6fjyNRAtxn9ezI9sk7XEqhPtvOckcAk8GxDrljDF7niXfopK56pCWCBBCeyG_C5iul7YYmwn3HP2DQ4WO4lgup4rGL-PqYbTVYocV_4uqZ1EwiPkzVjB--GupIfh_F77f8fghbCA3hMYjaLWOmIOonxWj5p5Ymw72GxnMYYE7oHopPjr62LBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7567afa506.mp4?token=nApNEx2tU1tPQ79NPd3XtMUayIkruPcD7vL4lT_TnCKUt0mQaDMcvYRKCZH2jp_IObDtr5XwTf86wzlwVMTa2oBSLeiaK6KXxImmVT4Jr2SwTIMOWPeJPMhfy7XpDZHHUteInIw7wZ7WgQBIKJ7eT-K8tJrB6APFP6fjyNRAtxn9ezI9sk7XEqhPtvOckcAk8GxDrljDF7niXfopK56pCWCBBCeyG_C5iul7YYmwn3HP2DQ4WO4lgup4rGL-PqYbTVYocV_4uqZ1EwiPkzVjB--GupIfh_F77f8fghbCA3hMYjaLWOmIOonxWj5p5Ymw72GxnMYYE7oHopPjr62LBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
اشتباكات ضارية تدور بين مقاتلي حزب الله وقوات الاحتلال الإسرائيلي التي تحاول التقدم واحتلال تلة علي الطاهر جنوبي لبنان.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/79339" target="_blank">📅 00:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79338">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌟
🌟
اشتباكات ضارية تدور بين مقاتلي حزب الله وقوات الاحتلال الإسرائيلي التي تحاول التقدم واحتلال تلة علي الطاهر جنوبي لبنان.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79338" target="_blank">📅 00:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79335">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HKLSMlqBh5l51FVK7A-z7wW9bcOvrrtFxIB2L_8Gn_MWq6YVha3pcAXNk5HMtAWg2XXImLJHghTTl7AymMRwhETOt-QS_OPwRWkheC0Ij2I1aNmqLwBt_YCQyPFb4JwnLQqvkZ_xscAeuUcyD5G-tn2w7hbFlAxTs2qi7QfkARMqcRWGDtw8J-xnib4iph71rPTwtXxc-A3gqv4Vi7VaC1ruz_YFI5NhHjQ6Mwz4jYYM6dPRsjzq2kvylZZZnHAzUoWKliDSlfcxdGav88kAOZhZZNk44bhPBwK3om4oUVPk4IRemHRS1gvbZbUQtFYTiOlxk5QA4UnVUUFt4_q6aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdX8nBapfLuF3JWyMIbKzqG8lvcQh15cVltvn2Q-H4JArk-PoOZ70m5V3VgpEwWHHl13CidM1TzQXVECans25fTzcwPKoWDDMn2dfnRtd1sXxFYYKn6X8vVPkBB6sWiWN6fqzkYvmOUka1I5QPx09WJ7rPQMaVawaaaBQoXTs9p9RbGubDBCT2SEwbPA1e3bitELKr8H1cImDsmzJf9GWDbfaGPy76j3kDDyJUAlJFf_yW_gZegSNxVGNsdrdVpj1WCsKJ-VrfVjpR1ZRkg3-bh9_l1hYYMVUMxGCZcGSIOWbRCwji8sJx3XIRlRqSTZgRO7fQDRgHSJkShahYF3pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">التحالف الدولي ينفذ عدة ضربات على بلدة دارة عزة في محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/79335" target="_blank">📅 00:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79334">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa1b4e7b2.mp4?token=FM28ItxXmkPEt253kE13QQAt5q3TDx1jfyBFYZDdexcL13LrTqkKS6p_AHBsEcPd7_kaNvm_B06VG0b5TxPx-0j1E0XA9O5QMK1WVivfdsHlJVG48NU2CdRA4gbfmH6ChzjWmveQHZAccd1f5eKG2u2gM8pzSePQXfwNrieDxM1UrRVhzsaGLa_mu6jEV7zB_k4RLK1cmRNVn-L4KaFA_VIcIWWHcogHkRZp_y6jKP8cMmznU6iPi458_lOaMuNgeIwuUYvYi97OAuTPgoK65McPssNaVNEGcFOHW917ypqetIPMy-9A6OMhYSpfoX7pWCNDOmMH_hdbOLXdHaL2-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa1b4e7b2.mp4?token=FM28ItxXmkPEt253kE13QQAt5q3TDx1jfyBFYZDdexcL13LrTqkKS6p_AHBsEcPd7_kaNvm_B06VG0b5TxPx-0j1E0XA9O5QMK1WVivfdsHlJVG48NU2CdRA4gbfmH6ChzjWmveQHZAccd1f5eKG2u2gM8pzSePQXfwNrieDxM1UrRVhzsaGLa_mu6jEV7zB_k4RLK1cmRNVn-L4KaFA_VIcIWWHcogHkRZp_y6jKP8cMmznU6iPi458_lOaMuNgeIwuUYvYi97OAuTPgoK65McPssNaVNEGcFOHW917ypqetIPMy-9A6OMhYSpfoX7pWCNDOmMH_hdbOLXdHaL2-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحليل نايا...تلة علي الطاهر.. لماذا تسعى إسرائيل للسيطرة عليها رغم الخسائر؟  تُعد تلة علي الطاهر من أبرز المرتفعات الاستراتيجية في قضاء النبطية جنوبي لبنان إذ يبلغ ارتفاعها نحو 700 متر فوق سطح البحر ما يمنحها إشرافًا واسعًا على عدد من البلدات أبرزها مدينة…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79334" target="_blank">📅 00:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79333">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d41c5588.mp4?token=p_kIya2iFCHpBgEIJdZrR111QVOljwGQqi34aCvX1C6IY4u11dupsuOuEDAckrrO3GZnPiWa-14fPp_GRZVYDed90G0DPAOl8Lrb48y2jz7Zbp-UmdE8Eg486hDjvtMttdBXafOIvDvpHkRATi067TrryIcTQCCxtsiZv9e9qbClipY9RTL7V2w7VdbGUpUdfWiJOByDxQUuhaUFY3Lpt0dgXJ9RYKEtqxmS_byrGWnSpV2fgb8soZQZqg0MhXb8PwaIdr6O9cTUN_YWNzXGs3F4CTXN5yKBZzA_xYkg-f2QN5nwKqSBfl8L_VGzbojxXKxWPCE5Uw5hlDqanobybQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d41c5588.mp4?token=p_kIya2iFCHpBgEIJdZrR111QVOljwGQqi34aCvX1C6IY4u11dupsuOuEDAckrrO3GZnPiWa-14fPp_GRZVYDed90G0DPAOl8Lrb48y2jz7Zbp-UmdE8Eg486hDjvtMttdBXafOIvDvpHkRATi067TrryIcTQCCxtsiZv9e9qbClipY9RTL7V2w7VdbGUpUdfWiJOByDxQUuhaUFY3Lpt0dgXJ9RYKEtqxmS_byrGWnSpV2fgb8soZQZqg0MhXb8PwaIdr6O9cTUN_YWNzXGs3F4CTXN5yKBZzA_xYkg-f2QN5nwKqSBfl8L_VGzbojxXKxWPCE5Uw5hlDqanobybQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: الطائرة F-47 قيد الإنشاء الآن. لديهم خط التجميع يعمل بالفعل.  يقولون إنها أعظم آلة قتال تم تطويرها على الإطلاق. سنكتشف ذلك.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79333" target="_blank">📅 23:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79332">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYRXgJJvYnf1r1u7NlQcw6BFCnx_V2f8DmKj0mFjS-F-7sX4RVx8piTRR4lJyy_uow33_WbAFDHjViXF848I4uVR78Daz0MZDvfOIZJYm5AsnTNPx5keRqRwiUCg4SMaMb1TBwktSOsaMg-mlVcFJ36QXYx8xF4otzCWGXg6s96m8hAmu3Dsxd63o5q7DsuEoX4bs57Hbi4rmdgjMwCNI9CjjdNsgoEMqe-YMtk16wCQtYIiohzIbybQ3h77TXJrnAtwKxPUv0RWA_XZXE4gh_UIWaJB2xi8BOdOFR4xzmn5pIDtMq2B8rcT-K9hSuk5MJScqJbx_m6X7Dv8sPf4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماع دوي عدة انفجارات في محافظة ادلب السورية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79332" target="_blank">📅 23:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79331">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/642865aff3.mp4?token=qFcUKt2h4fnZoCx8uI3umhm44oH5WgHzZmEo73CJRcrMjzvtLACuB1ElQfvJrVF4pxM9EIYgk2o5HETD5q3XZDaZ8RKHKFqOoelcIxbhLMg1gkueLu4Rp9ecE0hdwSPXbm2_OxgkBfHwUFvJ4uzQ5LDi_uWcIbY4t_HtDn2TanwMbKSOmAV4d7628qPnSWtgrCADqbSIgujotLU04-axp5G090xMzDDOhnkSSVvPnUGT4HG_uA9r-bkqI8xd0EDSictNAA-WW41wPghZZmv9rwwKqWrzVeis1q1LHOLIsI8u3bVSM5sQquyZnAvyq3zr_BCeanyQcjWTWL53V0jI5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/642865aff3.mp4?token=qFcUKt2h4fnZoCx8uI3umhm44oH5WgHzZmEo73CJRcrMjzvtLACuB1ElQfvJrVF4pxM9EIYgk2o5HETD5q3XZDaZ8RKHKFqOoelcIxbhLMg1gkueLu4Rp9ecE0hdwSPXbm2_OxgkBfHwUFvJ4uzQ5LDi_uWcIbY4t_HtDn2TanwMbKSOmAV4d7628qPnSWtgrCADqbSIgujotLU04-axp5G090xMzDDOhnkSSVvPnUGT4HG_uA9r-bkqI8xd0EDSictNAA-WW41wPghZZmv9rwwKqWrzVeis1q1LHOLIsI8u3bVSM5sQquyZnAvyq3zr_BCeanyQcjWTWL53V0jI5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب: إذا كنت سأضربهم الآن، إذا لم نكن سنضع قوات على الأرض، وأنت لا تريد وضع قوات على الأرض، أليس كذلك؟  إذا لم نكن سنضع قوات على الأرض، فمن المحتمل أن نفس الأشخاص سيذهبون إلى أعماق الكهوف. يطلق عليهم اسم "الكهوف الجرانيتية". إنها قوية للغاية.  إنهم يدخلون…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79331" target="_blank">📅 23:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79330">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سماع دوي عدة انفجارات في محافظة ادلب السورية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79330" target="_blank">📅 23:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79329">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌟
🌟
حزب الله يفجر عبوة ناسفة استهدف قوات العدو الإسرائيلي المتوغلة في منطقة علي الطاهر، ما أسفر عن وقوع إصابات في صفوفها، واشتعال النيران بالياتهم.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79329" target="_blank">📅 23:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79328">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYUqMRIgML3lCvVh4RfBgLxhgoRPm52WlmwO81-ALNVGTnNJ3M9weqdxkim6M_Xkv1oCT09vrAy7PReO1-Al9T5EyZjVESoizWM3qoncAM0EJ9fbJd9uxCFpgocXhEGj9JDSKo6z3FcoZT53ME5NJMcYIqKcJv5gG07cKASfvU2NYVHqNO3vdA4JSLBe8IxPd3SEWX-D7NmNht40TElucK1aFCWhdeMCubzyMBQhAH1LYBUS-ww-Cbab0ODTlC1oYewBVEf6KroIN_vIGR600e4E79XWCycyUAiIvhcOclVtrFE15TBa8bVXvRI1ZYfYIAHwF7mBtchkPlEnJLT02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصف بالقنابل الفسفورية يستهدف بلدة النبطية جنوبي لبنان من قبل الاحتلال الاسرائيلي.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79328" target="_blank">📅 22:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79327">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNkCfK1BflVjDL6_wTshtdJDTL37kZb2vR2Uvb0VlsEl1emMTcVNHjhv-ZplLuUW2OFc_Knd52QfWCTrt-vAMsm6nmjNGhiC0Sl9OpOE8zDIGcln7uZlo2eBC4AqIB23BpYoOwZhwhbCeUQR2mvJnZSng1pZArNkq8rrxCQb01p5tZO4hafC71BKajcwpEg0DCp6_9rqY3foW7l0ifLiT1NE384ynkGfcohTxsZnothm7ZMhCcmdn0MYiHw-2__vFIlCvq6HjQSDQd9LXQIoCRR2zmLMJ_Mmdi5xdu0VhCxr3do85dJ21KqiBJ243wUFNvc1IKBjB83orZ6uttddlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصف بالقنابل الفسفورية يستهدف بلدة النبطية جنوبي لبنان من قبل الاحتلال الاسرائيلي.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79327" target="_blank">📅 22:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79326">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/945fd8656b.mp4?token=Vzrzz_Dv7KKHkrLLOyxpLQ_SLMuzy-fNBADc1ZzQdlJ-rHYJqS0s_47JqZxsVHnc2GZ8-JV2oDl1x4dd3NSYnu-quwJPvSoeNKWVLSWDkOZv6w53YHEJWbOiH83UE_bDL61dHT4zZWxB4vyatRgYHxGL7p3rl6vBAZSIadtCoZzU9z_Siwwc4XokI9czPl4m_bcPoo0lU39Pj9F3rMEgtcM3Z5DFpoyvlwx1mP_J60xE97ByuJBR7gZXBGXDCpMEFZNwQWqqCP-Hp3oM8xXg0iprywnPkXsoyP6sqhefeKsVCmoriS6GgwAQqyVnNlohIxSzcR0VFMKOOyT1foeAyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/945fd8656b.mp4?token=Vzrzz_Dv7KKHkrLLOyxpLQ_SLMuzy-fNBADc1ZzQdlJ-rHYJqS0s_47JqZxsVHnc2GZ8-JV2oDl1x4dd3NSYnu-quwJPvSoeNKWVLSWDkOZv6w53YHEJWbOiH83UE_bDL61dHT4zZWxB4vyatRgYHxGL7p3rl6vBAZSIadtCoZzU9z_Siwwc4XokI9czPl4m_bcPoo0lU39Pj9F3rMEgtcM3Z5DFpoyvlwx1mP_J60xE97ByuJBR7gZXBGXDCpMEFZNwQWqqCP-Hp3oM8xXg0iprywnPkXsoyP6sqhefeKsVCmoriS6GgwAQqyVnNlohIxSzcR0VFMKOOyT1foeAyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب: لو لم نضربهم، لكان سيحصلون على سلاح نووي. كانوا سيستخدمونه ضد إسرائيل. كنت ستستخدمه أيضًا في المملكة العربية السعودية.كانت الصواريخ تطير على الفور تقريبًا إلى هذه الدول الخمس الأخرى [قطر، الإمارات العربية المتحدة، الكويت، البحرين].  قلت، لماذا يفعل…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79326" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79325">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🌟
ترامب: الإيرانيون أشخاص أذكياء جدًا. إنهم نوعًا ما من عبقريين بدائيين، لكنهم أذكياء. كانوا سيفجرون إسرائيل. لولاي، لم تكن إسرائيل ستوجد اليوم.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79325" target="_blank">📅 21:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79324">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
ترامب:
الإيرانيون أشخاص أذكياء جدًا. إنهم نوعًا ما من عبقريين بدائيين، لكنهم أذكياء. كانوا سيفجرون إسرائيل. لولاي، لم تكن إسرائيل ستوجد اليوم.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79324" target="_blank">📅 21:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79323">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🌟
🇮🇷
أوباما حول اتفاق ترامب مع إيران: كان هناك اتفاق توافق فيه إيران على عدم تطوير أسلحة نووية.  هذه الإدارة - أو نسخة سابقة من هذه الإدارة - انسحبت منه، مما أدى إلى قيام إيران بتطوير المزيد من القدرات النووية.  لقد خضنا حربًا الآن، وأنفقنا مليارات ومليارات…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79323" target="_blank">📅 21:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79322">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncnZxg5Ce3ZYjC2MdA_FtC_C1v5GRGvGobG_guddtyAO3KtfmKLip9QIqR0V0MV_I4r9kF6NxGtlime5qYHJ3i5uQtLlKUhheAeoGuvXKmAY2IbS437CpdN_LXmjlT7nHrQXxx_CO1Eq4LISj8YXhWt3ewkJqVLkTQyT8kCYbaYkepR7y5dANivNwpmHXVJ6kBghObkKRRsfnV0mwHtUqRfcccDwV5ekLZFZNDyyE06mDa9AuhoEbBKHMSwyPFrtxQRQjuTIWMgkJ2RkPwnsCU68rjqtsGSLSZ7IdKdJzEsnpLhfq8BkqvFRW069HT4HJ6Y_c7CYzaH1q1RbS-iyew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد فيلق القدس التابع للحرس الثوري الإيراني اللواء قاآني:
بسم الله الرحمن الرحيم
عندما قلنا إن حزب الله يمتلك المرصاد، لم تُصغوا، فوقعتم في الفخ؛ من سيُحاسب على المئة قتيل؟  غزة أيضًا لديها طوفان. إذا تحركتم وفقًا لرغبات سياسيكم، فستقعون في العاصفة. كونوا حذرين.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/79322" target="_blank">📅 21:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79321">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌟
🇮🇷
أوباما حول اتفاق ترامب مع إيران:
كان هناك اتفاق توافق فيه إيران على عدم تطوير أسلحة نووية.
هذه الإدارة - أو نسخة سابقة من هذه الإدارة - انسحبت منه، مما أدى إلى قيام إيران بتطوير المزيد من القدرات النووية.
لقد خضنا حربًا الآن، وأنفقنا مليارات ومليارات من الدولارات، وفرضنا ضغطًا هائلاً على جيشنا، ومات الكثير من الناس، ويبدو أننا عدنا إلى المكان الذي كنا فيه قبل بدء الحرب، بل ربما في حالة أسوأ قليلاً.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79321" target="_blank">📅 21:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79320">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال يسمح بنشر إسم أحد الجنود القتلى في جنوب لبنان وهو "دور بن سمحون"قائد كتيبة 52 ونائب قائد الكتيبة ، بينما لم ينشر أسماء الثلاثة الآخرين حتى الآن.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79320" target="_blank">📅 21:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79319">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇸
🏴‍☠️
جي دي فانس حول الكيان الصهيوني:
إسرائيل
شريك جيد بنفس الطريقة التي تكون بها المملكة المتحدة أو فرنسا شريكين جيدين.  هذا لا يعني أنه سيكون لدينا دائمًا مصالح متوافقة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79319" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79318">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534464594.mp4?token=ttosRvvsdPnI2JRvTvz9_gn1wu_orFOU_uUWli1wrztpBz46nQQVQbvqMo0YO1al-lI_XxHeyphFo283JUTEDSBorFv5yLydritYFSOI7ceOtsDuDBcBulZrW-1wCWukM7kqpKhMKuh4laLiQ4XVrsjYssA8sqC_ESrClrD1HNSywE7pVFe5vKCOYSHOPLMXu0iKgM9msmbh3t6M7jxLijuloh72Tu2qei0tDQsTNcdj1aset9cvwIb2RngknThNNWtnWen6B3WA1kRjC2rQLfAMH8Oc0W9LCUizVVlnFOZ6bZOyIBV_IdlXXoXHcYXkKS3R1dZwPdP6LGcK-18FDkZaxsEsfmGWX2cMzwViPeWeRtN-XEzmYn_dYyY4FOFUNzKu7uCtBStGxwSqi-uRvvaeA37LXlestf4UZK0vbQzvb9ZVKPE9Vl2DyOq7GAUNKK96PZM98LY92ZsF9_xSJsbD93vPYRhCvYBZyIN_waqLY7rl_nBLE1J2_x2-hKUOJ3HEgx6G8yentItTbsoz7Dm24eLShXJqvwY5jrHNneoSiiwPIO_HIJguDmXTRQQEzgEtsnsYjz32ZQwp8qPWYEj0ol6mzr4UlYKBXCsJCFXcldt_AtzDnH2pHUX2FfbX3F4WYJ3-RR_uBXWwn7g2mEP_tOZZM7IUYUnZucmHA3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534464594.mp4?token=ttosRvvsdPnI2JRvTvz9_gn1wu_orFOU_uUWli1wrztpBz46nQQVQbvqMo0YO1al-lI_XxHeyphFo283JUTEDSBorFv5yLydritYFSOI7ceOtsDuDBcBulZrW-1wCWukM7kqpKhMKuh4laLiQ4XVrsjYssA8sqC_ESrClrD1HNSywE7pVFe5vKCOYSHOPLMXu0iKgM9msmbh3t6M7jxLijuloh72Tu2qei0tDQsTNcdj1aset9cvwIb2RngknThNNWtnWen6B3WA1kRjC2rQLfAMH8Oc0W9LCUizVVlnFOZ6bZOyIBV_IdlXXoXHcYXkKS3R1dZwPdP6LGcK-18FDkZaxsEsfmGWX2cMzwViPeWeRtN-XEzmYn_dYyY4FOFUNzKu7uCtBStGxwSqi-uRvvaeA37LXlestf4UZK0vbQzvb9ZVKPE9Vl2DyOq7GAUNKK96PZM98LY92ZsF9_xSJsbD93vPYRhCvYBZyIN_waqLY7rl_nBLE1J2_x2-hKUOJ3HEgx6G8yentItTbsoz7Dm24eLShXJqvwY5jrHNneoSiiwPIO_HIJguDmXTRQQEzgEtsnsYjz32ZQwp8qPWYEj0ol6mzr4UlYKBXCsJCFXcldt_AtzDnH2pHUX2FfbX3F4WYJ3-RR_uBXWwn7g2mEP_tOZZM7IUYUnZucmHA3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في الأطراف الشرقية لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79318" target="_blank">📅 20:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79317">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
🏴‍☠️
إن بي سي: ‏تحدث ترامب مع نتنياهو في وقت سابق من يوم الجمعة وطلب منهم الموافقة على وقف إطلاق النار مع حزب الله.
🇺🇸
ترامب: لطالما عاملت نتنياهو بشكل جيد ويتوجب عليه فقط الهدوء أحيانا وإعمال العقل.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79317" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79316">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
🏴‍☠️
إن بي سي:
‏تحدث ترامب مع نتنياهو في وقت سابق من يوم الجمعة وطلب منهم الموافقة على وقف إطلاق النار مع حزب الله.
🇺🇸
ترامب:
لطالما عاملت نتنياهو بشكل جيد ويتوجب عليه فقط الهدوء أحيانا وإعمال العقل.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79316" target="_blank">📅 20:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79315">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">أضافت فرقة العمل المعنية بالإجراءات المالية البوسنة والهرسك والعراق إلى "قائمتها الرمادية" للولايات القضائية التي تتطلب مراقبة متزايدة بسبب أوجه القصور الاستراتيجية في أنظمة مكافحة غسل الأموال وتمويل الإرهاب.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79315" target="_blank">📅 20:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79314">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين:
الاستخبارات الأمريكية حذرت الإدارة من أن نتنياهو قد يقوض جهود اتفاق سلام دائم مع إيران.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79314" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79313">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🌟
الشيخ نعيم قاسم:
عملوا على الضغط على سوريا من أجل أن تتدخل من الشرق لتكون كماشة هي و"اسرائيل" من الشمال.
المخطط يتضمن إقفال كل المعابر لمنع وصول السلاح والتقنيات وكل ما من شأنه أن يقوي المقاومة.
المخطط يتضمن فرض حصار مالي شامل وتحريض الجيش ضد المقاومة.
عملوا على الفتنة السنية الشيعية تحت عنوان حماية موقع رئيس الحكومة بالقرارات التي سيأخذها ضد المقاومة.
سقط مشروع إنهاء حزب الله وتثبيت الاحتلال وستخرج
إسرائيل
من آخر شبر من أرضنا.
لا عودة إلى ما قبل الثاني من مارس وإخراج العدو من أرضنا سيتحقق.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79313" target="_blank">📅 19:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79312">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMarnj5zdZSdOJV-xV1cBQmy51YNKpofnc3o3lVEz4m97IZ-xnOizic-R0dgXyE8khzev6NwrhmUN4iUg_UUXlwB1qoUxUmu1K3LgxO0CsmfsRizxACUniy9qKhSfkwIf_eq8dz1DuuPTyeloSjXgavJCg2j41rDcToo3gd3EYnCp-nSLeWxRkPLrV1aNiuKxLdpdJw7U1uoD4wfSMdGz-R0FpN4deCJBG7OV1-Zpfjrt-TOk49bw_1PKZtWN7zSooaioB86PbP6UvXxVoqY76tAL-sMHSkwxWTZ8MEPz8reshVIHl2qXXT1JaPETlBc5WVWN6-gXYDiQahTPx2TFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇮🇹
توتر العلاقات بين الولايات المتحدة وإيطاليا يتصاعد..  ألغى وزير الخارجية الإيطالي أنطونيو تاجاني زيارته إلى الولايات المتحدة الأمريكية عقب تصريحات الرئيس الأمريكي دونالد ترامب المسيئة لرئيس الوزراء الإيطالي جيورجي ميلوني.   تاجاني: "إن تصريحات الرئيس ترامب…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79312" target="_blank">📅 19:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79311">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">"انا وايطاليا لا نتوسل ابدا".. رئيسة الوزراء الايطالية تنشر فيديو غاضب من ترامب بعد تصريحه ان ميلوني توسلت له من اجل ألتقط صورة معها!  جورجيا ميلوني:  يجب أن يتذكر شيئًا واحدًا: إيطاليا وأنا لا نتوسل أبدًا. تصريحات دونالد ترامب ملفقة تمامًا. أشعر بالصدمة بصراحة.…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79311" target="_blank">📅 18:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79310">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpItC8w2F9WKE1L433c3M8gHpLk3gurD5vq3KbOJ-V3wS8OVxojCz-peq_xAQKkApkgp0ltIAUsi0yKlzR8i4jZzSB84taTDcuwUDyZyUT3eAlBH0UF9WuKkBPKrYmDkXrlo3Hz3DBRAxCSjnuaFnghTtHVoO37gaAcs2rCWrh0zXAxjuiOAd4h1ReymXC18xyjD6xYdfhE8oM4Qf1kVGnKI1xUmKgJZEjam515d0KcnZO1-D7muz1HdQLC0dgvA34enOvOlYx7mja8xCl8RMOCzQOGjkhaCuWB7XdW43MhY_gpFBBJrEQ2JTZ2FjMj7N0AsqiC7_WN7JlO6Y5sbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوة عامّة  يسر المقاومة الإسلامية (كتائب سيد الشهداء) دعوتكم لحضور الحفل الجماهيري الذي يُقام احتفاءً بانتصار الجمهورية الإسلامية الإيرانية في حربها ضد الاستكبار العالمي.  التاريخ: يوم الجمعة 2026/6/19 الوقت: الساعة الخامسة مساءً المكان: بغداد الصالحية -…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79310" target="_blank">📅 18:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79309">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a3ed5b25.mp4?token=v7Dlxo1sr3VLpFZmY5eZZkfDVKiH4VsK4xF7YQwxAjYmDF4ukiGnudnQCllJNVxApw0-4LApKtitQPSn0rBtGb5Ra4HNEsv2FE7Bqb6T1PW7Z3gM4fFhQvZ6rXHbBvv_fCItTgm6juxJxWIQh9oHWmQGOJ3E8iB1zcUu7wZrrU6LPOb1KWhI5GggpHh_MYv1SDQWMHJgsZIBKmyzwtLGvIuzrfKe2bSwE6owdsZdHqLsfhNGzMh3uNHSiIq_lj8FdDNXR2StjC7ahiEXRW40FDT9Z6F6h32M50nVfoey1zt7nChi7wWY5oeMLEBN0hAy7FG_7D_GbwMQoaKeiYNL_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a3ed5b25.mp4?token=v7Dlxo1sr3VLpFZmY5eZZkfDVKiH4VsK4xF7YQwxAjYmDF4ukiGnudnQCllJNVxApw0-4LApKtitQPSn0rBtGb5Ra4HNEsv2FE7Bqb6T1PW7Z3gM4fFhQvZ6rXHbBvv_fCItTgm6juxJxWIQh9oHWmQGOJ3E8iB1zcUu7wZrrU6LPOb1KWhI5GggpHh_MYv1SDQWMHJgsZIBKmyzwtLGvIuzrfKe2bSwE6owdsZdHqLsfhNGzMh3uNHSiIq_lj8FdDNXR2StjC7ahiEXRW40FDT9Z6F6h32M50nVfoey1zt7nChi7wWY5oeMLEBN0hAy7FG_7D_GbwMQoaKeiYNL_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوة عامّة  يسر المقاومة الإسلامية (كتائب سيد الشهداء) دعوتكم لحضور الحفل الجماهيري الذي يُقام احتفاءً بانتصار الجمهورية الإسلامية الإيرانية في حربها ضد الاستكبار العالمي.  التاريخ: يوم الجمعة 2026/6/19 الوقت: الساعة الخامسة مساءً المكان: بغداد الصالحية -…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79309" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79308">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⭐️
نيويورك تايمز:
وفقًا لكتاب "تغيير النظام"، أشار ترامب خلال اجتماع رفيع المستوى في المكتب البيضاوي قائلًا: "أنا لست معجبًا كبيرًا بأوكرانيا. باستثناء نسائهم. فهن يواصلن الفوز بمسابقة ملكة جمال الكون".</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79308" target="_blank">📅 18:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79307">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
ليس لدينا أي خطط لتفتيش الوكالة الدولية للطاقة الذرية للمنشآت النووية الإيرانية. والخبر الذي نشرته بعض وسائل الإعلام بأن الجمهورية الإسلامية الإيرانية قد دعت الوكالة الدولية للطاقة الذرية لتفتيش منشآتها النووية غير صحيح. إن تفتيش المنشآت التي مُنعت الوكالة من الوصول إليها بسبب الهجمات العسكرية الإجرامية التي شنتها الولايات المتحدة والكيان الصهيوني، سيعتمد على سير المفاوضات ونتائجها.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79307" target="_blank">📅 17:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79306">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
أيدينا على الزناد وآذاننا على أوامر القائد الأعلى للقوات المسلحة، نحن على استعداد لحماية أمن الأمة وكرامتها ومصالحها من خلال التضحية بأرواحنا في حالة حدوث أي إخلال بالواجب من جانب العدو.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79306" target="_blank">📅 17:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79305">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6485ab46f4.mp4?token=fVYlztGr6I4kils6LwulOWXiQUsXUNxBgwe5WA4taMgUQPzfm8ZxLkZAm_lmbn_8luawf8yEq4SSzmg7nICepS3T4haLH_ndxjY_cLzvUBSme2u3jpzjSES4ZSmEhHjc73qCSsTpA3ZxdLXW36bpEq2ECnASu7j8Krcgb7PAPMLUapAjVAqyuuifGFiUKETUNy2mudJaly6QaywCTE6PosWDb_UaQW9jVpWJJhYoIr7lacfJjxOZDs9wkYT8a_fioujbOKyml7kCNGzh_Dpg7fZV7VbiBcjrh3VxmD_ONFL1pvVJ0spnXvpK64OKKBoVA87ss5Kh2DkeTjq0rUpWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6485ab46f4.mp4?token=fVYlztGr6I4kils6LwulOWXiQUsXUNxBgwe5WA4taMgUQPzfm8ZxLkZAm_lmbn_8luawf8yEq4SSzmg7nICepS3T4haLH_ndxjY_cLzvUBSme2u3jpzjSES4ZSmEhHjc73qCSsTpA3ZxdLXW36bpEq2ECnASu7j8Krcgb7PAPMLUapAjVAqyuuifGFiUKETUNy2mudJaly6QaywCTE6PosWDb_UaQW9jVpWJJhYoIr7lacfJjxOZDs9wkYT8a_fioujbOKyml7kCNGzh_Dpg7fZV7VbiBcjrh3VxmD_ONFL1pvVJ0spnXvpK64OKKBoVA87ss5Kh2DkeTjq0rUpWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حادث سير عنيف على طريق العمارة - المجر في محافظة ميسان ؛ وفاة وإصابة عدة أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79305" target="_blank">📅 17:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79304">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">طيران مسير يخترق أجواء مستوطنة زرعيت في شمال فلسطين المحتلة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79304" target="_blank">📅 17:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79303">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
🇷🇺
إيران:
المتخصصون الروس سيعودون قريباً لاستكمال بناء محطة بوشهر.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79303" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79302">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏مسؤول أميركي كبير: نتنياهو وافق بنسبة 100% على وقف النار في لبنان</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79302" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79301">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇱🇧
🏴‍☠️
حزب الله ينشر:
لا مناطق آمنة لـ "إسرائيل"... وسَتَرحَل</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79301" target="_blank">📅 17:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79300">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏴‍☠️
جيش العدو: سنهاجم بقدر ما يلزم، تعليمات رئيس الأركان لم تتغير ولا توجد قيود على القوات في الميدان.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79300" target="_blank">📅 16:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79299">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🏴‍☠️
جيش العدو:
سنهاجم بقدر ما يلزم، تعليمات رئيس الأركان لم تتغير ولا توجد قيود على القوات في الميدان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79299" target="_blank">📅 16:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79298">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e0661b1f.mp4?token=bkRJKIMKFN0g-YKSJT3Bs0ikV7p2krb4uKBU3pJwDp6G44S1WAoEcaQrs1FaQxjlEcPy_jOt6ycWoBiNcIj2fFkViC7vRE92320UVaKi4wFBf01Y97XEytC-rMxA4MB6n90KluzWx6HUmmSCEFcamVCrnAipi1hZxg2sg7CuMTtWqcCvVTE9X2eh2EzKflDGAZexWzhkKyE3PqoukQ7gfM2f6NbdkK7g2W7AcKYpJh0ObX7G7PXqGCUf30rXKkskpXVTfNR7H6sHGLuf4kSqx2beIwFin-FAkU1lQuGI-ESeVJIUfbxl5ns9ecP0GrBeF_sYXPfAvjPLE9JfMKfOUZkv5jOsVRAScghlkyTa5w8opKyQyV6pOrEj2rEXtM5qh0aiU_rU5PVy_sQ9d0jnZBNZq16T80u6nBwuLY5Ok1L9RqdGn1xMyNPcnwseNse3Fht4fWJhqOtRF40M0OVwZxeZMaC2QFtUa6d3qI4s_qAj4-5yMWsoJHDdpMC62g5K0LF-rsBbSDTJKukSWE2m4m9x9b-Op57qYAr5GLvlHOAeB9IciE02AXolr3noi2UBlYN-cJCfmlNwCveAUMstgpXnjug_GGZmR_GpL7FFyxJkUjnEYS_53UgcjmyGkPpu9D9lhYLct_8pljGCV6c9zJyq_aKFOS6yC6EGNJdQfEs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e0661b1f.mp4?token=bkRJKIMKFN0g-YKSJT3Bs0ikV7p2krb4uKBU3pJwDp6G44S1WAoEcaQrs1FaQxjlEcPy_jOt6ycWoBiNcIj2fFkViC7vRE92320UVaKi4wFBf01Y97XEytC-rMxA4MB6n90KluzWx6HUmmSCEFcamVCrnAipi1hZxg2sg7CuMTtWqcCvVTE9X2eh2EzKflDGAZexWzhkKyE3PqoukQ7gfM2f6NbdkK7g2W7AcKYpJh0ObX7G7PXqGCUf30rXKkskpXVTfNR7H6sHGLuf4kSqx2beIwFin-FAkU1lQuGI-ESeVJIUfbxl5ns9ecP0GrBeF_sYXPfAvjPLE9JfMKfOUZkv5jOsVRAScghlkyTa5w8opKyQyV6pOrEj2rEXtM5qh0aiU_rU5PVy_sQ9d0jnZBNZq16T80u6nBwuLY5Ok1L9RqdGn1xMyNPcnwseNse3Fht4fWJhqOtRF40M0OVwZxeZMaC2QFtUa6d3qI4s_qAj4-5yMWsoJHDdpMC62g5K0LF-rsBbSDTJKukSWE2m4m9x9b-Op57qYAr5GLvlHOAeB9IciE02AXolr3noi2UBlYN-cJCfmlNwCveAUMstgpXnjug_GGZmR_GpL7FFyxJkUjnEYS_53UgcjmyGkPpu9D9lhYLct_8pljGCV6c9zJyq_aKFOS6yC6EGNJdQfEs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"انا وايطاليا لا نتوسل ابدا"..
رئيسة الوزراء الايطالية تنشر فيديو غاضب من ترامب بعد تصريحه ان ميلوني توسلت له من اجل ألتقط صورة معها!
جورجيا ميلوني:
يجب أن يتذكر شيئًا واحدًا: إيطاليا وأنا لا نتوسل أبدًا. تصريحات دونالد ترامب ملفقة تمامًا. أشعر بالصدمة بصراحة. لا أعرف لماذا يتصرف رئيس الولايات المتحدة بهذه الطريقة تجاه حلفائه! بعد كل شيء، هذه ليست المرة الأولى التي يحدث فيها ذلك. كل ما يمكنني قوله هو أنني آسفة لأنه لا يبدي نفس الحزم والصلابة تجاه أعداء الغرب، وأعداء الولايات المتحدة، ومع تلك القيادات التي يظهر تجاهها، على النقيض من ذلك، قدراً كبيراً من التساهل والمداهنة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79298" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79297">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWTl3QTeTdJHM1BTUeZFUihecewD5LMKaArmU9zJT4l4vmeWRr2_V-hCNtXYK2A_pliFQz97eJt3q8XMijwXd-JPwasbgTKq-PZermWa_IPBXyU45mWbD_Wonno_ihs12H3VEOqOxcCjKGk2uTjHUu7KWrUvG8Zl6NPeTQZAS0hpVh6eDjT1PSY4U_lVzvzuuKOOAH4Jc4QwHWISStGBYJzgZlR3ySKzlamYVtS_S2WTApXkKG_JA2cLzpBHzNNyfnmwUpntpeeKSCNGzVsL_T2vF3fYzn5C7r1WmCL0DphA39s-wyhhhYqw3PFCzmds30sRce6hbMlMH1DEL70t6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
اعلام العدو عن مسؤول إسرائيلي: نحن الآن في وقف لإطلاق النار وإذا لم يهاجمنا حزب الله فإنه ليس وقت حرب من جهتنا.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79297" target="_blank">📅 16:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79296">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">العدو الصهيوني يشن غارات على جنوب لبنان في اول خرق لاتفاق وقف اطلاق النار المزعوم</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79296" target="_blank">📅 16:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79295">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وقف اطلاق النار المزعوم من قبل المسؤول الامريكي يدخل حيز التنفيذ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79295" target="_blank">📅 16:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79294">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏴‍☠️
وزير خارجية النظام الصهيوني جدعون ساعر يناشد الاعلام الغربي بعد العزلة التي يواجهها الكيان الصهيوني:
تصور الكثير من وسائل الإعلام الغربية إسرائيل كنوع من المشروع الاستعماري، كما لو أننا لسنا السكان الأصليين في هذه الأرض - شعب كان هنا منذ أكثر من 3000 عام وحافظ على وجود مستمر هنا عبر التاريخ.
تصورنا دعاية الجانب الآخر كشكل جديد من أشكال الاستعمار.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79294" target="_blank">📅 16:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79293">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مسؤول أميركي: اتفاق وقف النار يدخل حيز التنفيذ عند الساعة الـ4 بتوقيت بيروت.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79293" target="_blank">📅 16:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79292">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏رويترز عن مسؤول أميركي: إسرائيل وحزب الله اتفقا على وقف لإطلاق النار اليوم.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79292" target="_blank">📅 16:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79291">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏
رويترز عن مسؤول أميركي:
إسرائيل وحزب الله اتفقا على وقف لإطلاق النار اليوم.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79291" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79290">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
‏ترامب: لن تحصل إيران على أي أموال ولا حتى 10 سنتات.  والـ300 مليار دولار الي وقعت عليها
😄</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79290" target="_blank">📅 16:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79289">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2xCYrfNv-QY2z7es4AMdqqh5tVeXiPUg_GAoG_ZGHnnEuX7jNXqyAOwjOsyouTnbfEgRfD37er7uQtM4qCFC6U9RpmFazrNQa61nuQ96_x37PsAkIIvb1Cdq-2e8f7ZlljcfGiPM6527h1pskZ4hX8O0F4P04bWzamDuVidgljLckmJknllDecdOl5YZkP_LihhxDbnX7iU-mBqrBQOEkwj7zYW1Qf83_8F6ChzxklGKzXH9JIMR4zfb22ZlKMvMy0Zah6qGc81DmDNf9EZQyPzKTy40px52xVoqXiBcD3VAnlGNd2tGmoYFgncBXl0fhfJGs4lwV4hJvbCD6tjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
لن تحصل إيران على أي أموال ولا حتى 10 سنتات.
والـ300 مليار دولار
الي وقعت عليها
😄</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79289" target="_blank">📅 16:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79288">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏴‍☠️
اعلام العدو عن مسؤول صهيوني:
إيران تقف وراء الهجوم الليلي لحزب الله الذي قُتل خلاله الليلة أربعة من مقاتلي المدرعات. والهدف هو دفع إسرائيل للهجوم في الضاحية وبذلك تعميق الخلاف مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79288" target="_blank">📅 15:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79287">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMiTeFuLhXEFfJ_lcDujx30wpHBRmAVPfRmvvHoGvQdNwS63Cp1pHkwjoedri4c-KBw5cKf1zkIA2fUoh_Jhh72sNalrmXdjt2p_Kxp0ffNL4S8IrfWkCnIDg_des81ayKAdQjHYG1fF-eMxgoM-z6xTgwlbtHdYWZfQ6l45ZtCdEesysIkmGmzLohQMIpnBbV8ozgk6IZcILpo9nZdxcxb2_TMWu468MmyajXRrG5HWto1fcjGIINvn3OjmIfI96suaR5Dsw8orrAK2zqoBfa0ExGkTaoULKncyZpy197nbulZOJCk_2kIsUEJgFiGRKv_9scNGGX1qcqmwUZB-zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🏴‍☠️
وزير الخارجية الايراني عباس عراقجي يشارك تغريدة بن غفير:
هذا ليس هذياناً صادراً عن مجنون إبادة عشوائي. إنه منشور رسمي علني لوزير الأمن القومي في الكيان الإسرائيلي.
منظومة القتل الإبادية المتمركزة في تل أبيب، تشكّل تهديداً للإنسانية جمعاء. إنها تهدد كل البشر. وليس لها من هدف سوى الحرب الدائمة.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79287" target="_blank">📅 15:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79286">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🏴‍☠️
اعلام العدو عن
مسؤول رفيع في الكابينت
: لا يجب الانجرار إلى سياسة رد فعل. يجب فرض ثمن باهظ على دولة لبنان لكي تمارس ضغطًا على حزب الله.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79286" target="_blank">📅 15:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79285">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
هيئة إدارة مضيق هرمز الإيرانية: لن يتم فرض أي رسوم على السفن التي ترغب بعبور المضيق خلال فترة الـ60 يوما، سيتم السماح بمرور السفن التي تتقدم بطلبات العبور وتلتزم بالمتطلبات.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79285" target="_blank">📅 15:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79284">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
هيئة إدارة مضيق هرمز الإيرانية:
لن يتم فرض أي رسوم على السفن التي ترغب بعبور المضيق خلال فترة الـ60 يوما، سيتم السماح بمرور السفن التي تتقدم بطلبات العبور وتلتزم بالمتطلبات.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79284" target="_blank">📅 15:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79283">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇱🇧
حزب الله ينشر:
אם כבר נסוגים, אז למה שתהייה ההרוג האחרון؟</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79283" target="_blank">📅 15:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79282">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
وكالة فارس:
اغلاق مضيق هرمز قرار يمكن طرحه في إطار قرار المجلس الأعلى للأمن القومي كحل رادع لإجبار أمريكا على كبح إسرائيل. وإلا، فإن انتهاك اتفاقية الاستمرار سيستمر وستتحمل الطرف المقابل تكاليفه.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79282" target="_blank">📅 15:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79281">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📰
‏
سي إن إن:
الولايات المتحدة أبلغت إيران أن إسرائيل "وافقت على ترك الأمر عند هذا الحد" عقب الضربات في لبنان.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79281" target="_blank">📅 15:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79280">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اعلام العدو: الحدث قرب مرتفعات علي الطاهر</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79280" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79279">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
🇱🇧
أبو عبيدة:
نحيّي سواعد مجاهدي حزب الله الذين كبّدوا العدو الصهيوني خسائر فادحة ولا يزالون، في إطار التصدي البطولي للعدوان على لبنان وشعبه وسيادته، وهو حقٌ وواجبٌ كفلته كلّ الشرائع</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79279" target="_blank">📅 15:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79278">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🌟
رسو ناقلتين في ميناء البصرة النفطي حمولتهما تتجاوز مليوني برميل
رسو الناقلة Lucia على الرصيف رقم (1) في ميناء البصرة النفطي لتحميل شحنة تبلغ مليون برميل من النفط الخام كما تم إرساء الناقلة Romania على العوامة الثالثة لتحميل شحنة تبلغ مليوناً و300 ألف برميل من النفط الخام.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79278" target="_blank">📅 15:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79277">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اعلام العدو: حدث امني جديد في جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79277" target="_blank">📅 14:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79276">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اعلام العدو:
حدث امني جديد في جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79276" target="_blank">📅 14:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79275">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv-HfXC-x98Fp6E54Hy1gTNNu4xX4-yD8xFyjwOkEej3kR40P5_xlMr8n4gDmhJeHu2x05tkqh8UshUsvwY1ZwieZR6NH-N53g47oYNzSjn4Zb5DsCk7vci8AQE3x46tWVkxVEVC6znvJ3fY_bnXUgxXT_-sXImBgKaBzDgXWFcx1wVAE3cT24ETz6E48iJPqkeAJpbMXY_KZP_b-7YLqVa2JuLoAO363OS_ns7YBQvNyJbd-nne72ZdvezhlCYhOCk4jZ2GHXoHreqbzAJdCMHk2osy9E2i70_7RYodUWGbJX8v-ekAz3YVkBGKmXyOu0aL0cWIYGHn7XHT-hBz0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوة عامّة  يسر المقاومة الإسلامية (كتائب سيد الشهداء) دعوتكم لحضور الحفل الجماهيري الذي يُقام احتفاءً بانتصار الجمهورية الإسلامية الإيرانية في حربها ضد الاستكبار العالمي.  التاريخ: يوم الجمعة 2026/6/19 الوقت: الساعة الخامسة مساءً المكان: بغداد الصالحية -…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79275" target="_blank">📅 14:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79274">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇱🇧
بيان صادر عن غرفة عمليّات المقاومة الإسلاميّة في لبنان - حزب الله:
بِسْمِ اللَّـهِ الرحمن الرَّحِيم
﴿أُذِنَ لِلَّذِينَ يُقَاتَلُونَ بِأَنَّهُمْ ظُلِمُوا وَإِنَّ اللَّهَ عَلَىٰ نَصْرِهِمْ لَقَدِيرٌ﴾‏
صَدَقَ اللهُ العَلِيّ العَظِيم
دحضًا لادّعاءات العدوّ الإسرائيليّ بانتهاك حزب الله لوقف إطلاق النار، تؤكّد المقاومة الإسلاميّة أنّ العدوّ لم يلتزم يومًا بأيّ اتّفاق لوقف إطلاق النار منذ 27-11-2024 مرورًا بـ 16-04-2026 وصولاً إلى مخرجات التفاهم الإيرانيّ الأميريكيّ الأخير الذي أكّد في بنده الأوّل على إنهاء الحرب في جميع الجبهات بما يشمل لبنان.
بل إنّ العدوّ الإسرائيليّ أمعن في خروقاته المتمادية لوقف إطلاق النار مرتكبًا المجازر ومدمّرًا الأبنية السكنيّة والبنى التحتيّة المدنيّة
، واستمر في ممارسة الاعتداءات البرّيّة من خلال محاولات التوغّل والسيطرة على قرى ومناطق لم يتمكّن من الوصول إليها قبل الاتفاق. وبلغ الاستخفاف الإسرائيليّ بوقف إطلاق النار حدًّا صرّح معه رئيس أركان جيش العدوّ، المجرم أيال زامير، قبل أسبوعين بأنّه "لا يوجد وقف إطلاق نار في لبنان"، قبل أن يعاود الناطق باسم جيشه أمس التأكيد على مواصلة نشاط قوّات الاحتلال في جنوب لبنان.
وعلى جري عادته، يلجأ العدوّ، تعويضًا عن عجزه في مواجهة مجاهدي المقاومة، وللتغطية على فشله وخسائره في ميدان القتال، إلى ارتكاب المجازر ضد المدنيّين واستهداف القرى الآمنة، مثلما حصل اليوم في أعقاب تصدّي المجاهدي الباسل لمحاولة تقدّمه باتّجاه تلّة علي الطاهر ليل أمس.
ستبقى المقاومة الإسلاميّة بالمرصاد لأيّ اعتداء، يدافع مجاهدوها بكلّ شجاعة وبروح كربلائيّة حسينيّة عن أرضهم وشعبهم، ويذيقون جيش العدوّ بأسهم، موقعين بين ضبّاطه وجنوده القتلى والجرحى بالعشرات، وفي آليّاته إصابات مدمّرة، وبيننا وبينه الأيّام والليالي والميدان.
﴿وَمَا النَّصْرُ إِلاَّ مِنْ عِندِ اللّهِ الْعَزِيزِ الْحَكِيم﴾‏
الجمعة
19-06-2026
‏
04 محرّم 1448 هـ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79274" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79273">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏴‍☠️
نتن ياهو:
سنجعل حزب الله يدفع ثمنا باهظا للغاية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79273" target="_blank">📅 14:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79272">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني:
لن نسمح بإيذاء جنودنا ومواطنينا وأي خرق لوقف إطلاق النار من جانب حزب الله سيقابل برد قوي للغاية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79272" target="_blank">📅 13:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79271">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامب: لولا تدخلي لكانت إسرائيل قد سحقت</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79271" target="_blank">📅 13:44 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
