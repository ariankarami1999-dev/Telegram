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
<img src="https://cdn4.telesco.pe/file/fcSczguZhzWkNT4Y0H6_ap6u4sFmKrS9C84Ru6_Lso_TXG7gyxt6_XGD7XLBZTVl_FC_ZL9894jcx1IHrvriYne9fqNC-DatzhoHxXdTG1B_y4JdVNI6Tm-MrL_VgpmidCsX7FuiR1xuRQJjEX_OdABZnhgOkVuD7-g2jyqbKQNu-aCJF5PE2SbD-Pcjf30cKavUo3B-3CnyIpfxKg975R6pBkf2ivYmtN4aF8rJvVHCf5qxVwMmwru2aU8ziYn7DFnDSZM7-9F6Jw4r2CgQN7jfE3Yk-7xnQ3jrYCjUZF3sN5NQj2w4869HMFPyDBbOhKuSLUQ_ryGe6vNGCreN9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 20:56:09</div>
<hr>

<div class="tg-post" id="msg-87719">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee43d192c.mp4?token=aMqWSuGFkD-yiAdPpPclS7nuwAsbvu92rnvZdTb_RIbZPe4Ya0zomOuXGbWecNahvXkNvpikoE-bGAa1GFtQmS0EwaCpOFk9tlirjgIG0Y2MngITRJb0QraZLXXB_vcl5nDLKSKLLdAM30QPVa7EQg8oW3eDpbVpDC4WD3Q_97bzMy-MCFI-AUbyfAtrBBmR2dFtEZp7Elo-nr-SFvBcbTgouTuxXC2uVrM4L3iXufuQpqoU-WDXE6FeDLxj7iB5E_7mkFAHmZSLap4wG0DQ0yD9pcTCpYlq2R3p9PVPzJd5z1Fop9Nz1sTuWxqNHPi1M3_myqX7QS_tHYkST4Mbnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee43d192c.mp4?token=aMqWSuGFkD-yiAdPpPclS7nuwAsbvu92rnvZdTb_RIbZPe4Ya0zomOuXGbWecNahvXkNvpikoE-bGAa1GFtQmS0EwaCpOFk9tlirjgIG0Y2MngITRJb0QraZLXXB_vcl5nDLKSKLLdAM30QPVa7EQg8oW3eDpbVpDC4WD3Q_97bzMy-MCFI-AUbyfAtrBBmR2dFtEZp7Elo-nr-SFvBcbTgouTuxXC2uVrM4L3iXufuQpqoU-WDXE6FeDLxj7iB5E_7mkFAHmZSLap4wG0DQ0yD9pcTCpYlq2R3p9PVPzJd5z1Fop9Nz1sTuWxqNHPi1M3_myqX7QS_tHYkST4Mbnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
السلاح الذي حرر امرلي والجرف وسامراء و بلد وصلاح الدين والأنبار حينما هرب الآخرين هو الحصن المنيع للشعب العراقي بوجه اي مخطط خارجي يستهدف الأمة العراقية ..</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/naya_foriraq/87719" target="_blank">📅 20:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87718">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام صباح النعمان:
رئيس الوزراء العراقي وجه بإنشاء صندوق لتطوير الدفاع الجوي العراقي.</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/naya_foriraq/87718" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87717">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
سنتكوم
: إنشاء أول قوة مهام متعددة المجالات ومتعددة الجنسيات للطائرات المسيّرة الهجومية.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/naya_foriraq/87717" target="_blank">📅 20:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87716">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdJopgIvBvhsD7SAtMMD6TfLlQaVXmgIJ_-AjCGWkOONJkZLe4sg28wksx4qlhQm5Hn-Qsp-0TppmBqe9ctl1Dfsrn-a2BXs6HMyDMhQ23ZxoLcpOBHL81fzc8sh5bjKmQ5cTO51dqcbFuP8XTy8qgc6xAX0Lbly7HGQ-wUMQ6_ibIevLRWssX9BQ9tIpG_nfDZNhA4Su0xe1PmGmK_11pnuod3M47jD3aniyKfB4NMn3NaxmU0hQpIDZ-23_EetYzohddVjiXyQ7Ae8BxNufdwDGPaEonm0l-Lcz-801LQRlhkmaPGH8B80ZKXa-92gcva7vOGRmoY4EBE8OT17WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحضور الإعلامي للمتحدث باسم المقرّ المركزي لخاتم الأنبياء، مع ميدالية تحمل الاسم المبارك للإمام الرضا عليه السلام.</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/naya_foriraq/87716" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87715">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
أعلنَ مكتبُ سماحة السيد السيستاني (دام ظلّه) في النجف الأشرف أن يوم غدٍ الجمعة هو المكمّل لشهر صفر ، ويوم السبت الموافق  (١٥-٨-٢٠٢٦ م) هو الأول من شهر ربيع الاول لعام ١٤٤٨ للهجرة.</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/naya_foriraq/87715" target="_blank">📅 19:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87713">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇸🇦
‏
وزير الدفاع السعودي:
العراق سيبقى جارا عزيزا تربطنا بحكومته وشعبه روابط الأخوة والتضامن.</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/naya_foriraq/87713" target="_blank">📅 19:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87712">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_nHU2AZttpyqcNfdnUK2PM4SSXAJ3SUs951Z1BZkMkrYMPhWWsRAX31Bq1YX9-mTKvyEGWaPyfI7poRKVQkt-Kp3u8DoOA3F86-3EsyA_tDfEKdK4p6VHGU1sbFeDSwtdo1B0rvnuTgNZB8PDtw9dA2vpIkIcbnba9vYQlsCmBkt6WapdjTirE2erC0mZNLb4VvS7Ng8l47QBaBwtr6_LtF4FFeFAGsbRKinRQliiBfqXZ7VZXh5xdgZfG2ZTDGXJfseBMeBaBKZUS9G2TAi4HznGNSAcrUO6_D1VJ10uW6_fFiB-eBLdjTD-VAtkAGswX_ONYWgnRpgM2dZdBCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
الجيش فقد 45 مسيرة إم كيو 9 في الحرب مع إيران ما يعادل نحو 25 % من أسطوله.</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/naya_foriraq/87712" target="_blank">📅 19:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87711">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇾🇪
🇸🇦
نتيجة الهجمات التي تشنها القوات اليمنية.. السعودية تستمر في إغلاق مطارات جيزان ونجران وأبها حتى إشعار أخر.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/87711" target="_blank">📅 18:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87710">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/87710" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87709">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/87709" target="_blank">📅 18:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
‏ كبير الديمقراطيين في مجلس الشيوخ لشؤون القوات المسلحة السيناتور جاك ريد يدعو وزير الحرب بيت هيغسيث للإدلاء بشهادته أمام الكونجرس بشأن حوادث سقوط ضحايا مدنيين جماعيين ناجمة عن الضربات الأمريكية في اليمن وإيران (مدرسة ميناب للبنات).
‏
يلقي ريد باللوم على قيادة هيغسيث في هذه الحوادث، ويتهم وزارة الحرب بتأخير تقرير الشؤون المدنية اليمنية لأشهر ولم تقدم حتى الآن بياناً منفصلاً عن ضرب مدرسة ميناب</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/87708" target="_blank">📅 18:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87707">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVY9i7kgdOzosCPyh2tJ6fghCmgMhlbtuy90IiRNyr_3Jp1S0uVkjVDurfRwc4mYKcjnZPI_9H8Xobc0tL6BSjg2NfVH3yViie62Wepg27cyjnn1voeLsvFJQ31wJaS8J7jVD-4ZUOcGCpSPhky3qmElCe-DH520fRPRuLwOrUlPbCqqrGbWD4B1JASJOho9qERh5FF3gJ6Y1Xz4LPqYX1Ntg5VXr_LksDb5IFcsjCE3hcVt5Zr4nenOUkt5liFKbMweMkJDan3lt6k2Kap80YmHNFkbDvT0UjTBsis5n2Soto3rdmODlNMtMwU8ZoF4laG2gfA-VKsrOb9nGb1zQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قادمة من سوريا.. العراق يحبط محاولة تهريب (45) ألف حبة مخدرة كانت في طريقها للترويج داخل البلاد</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/87707" target="_blank">📅 18:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87706">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">لحظة إنفجار كدس عتاد في كوليفررو جنوب روما الايطالية</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/87706" target="_blank">📅 18:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87705">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqgFeiWJVxIavZGChdfRFgrYbqL7hiHrNwnfrWvryYFdFyiI9PAacXGE8-_dq6tq_sLNTUPkiJk71U4d-FyoGchQFj4upJJuu9hg2sR-6C012go3Jr-RrXD3ps7ZZ67Z7PY9kEGsDugYONAPADnKaXRLYSKiiKYkgKcl1t7k3hpv9LdEQcDiK3WmurXUc-Ctgrek3xqrXEoz-9qc97H5asBWWgqcvIyCPY-1ikAAwI5H1PA6zQ4ESztia7I_l43MK7ekXGfmuJO_OGQHDMQqIBDbFDDam0pZTmjBbJ8xStUQxAoZGJJYn0nkzGC5O7pC-Q2jeMATzA46jFGJuT0OAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملك السعودية المرحوم سلمان بن عبد العزيز يعفي نفسه من رئاسة مجلس الوزراء ويكلف محمد بن سلمان برئاسة المجلس</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/87705" target="_blank">📅 17:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87704">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">السعودية تقرر اغلاق (‏مطار أبها الدولي - مطار جازان الدولي - مطار نجران الدولي)</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/87704" target="_blank">📅 16:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ملك السعودية
المرحوم
سلمان بن عبد العزيز يعفي نفسه من رئاسة مجلس الوزراء ويكلف محمد بن سلمان برئاسة المجلس</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/87703" target="_blank">📅 16:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بيان مرتقب للسيد القائد عبدالملك بدرالدين الحوثي حول الإساءة الأمريكية للقرآن الكريم</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/87702" target="_blank">📅 15:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43381c63c7.mp4?token=ltdSZZzejQBDxPln8IY9he6EOU2ZyAxbIpLixrzRMT1dS0rRP5swm5J5ESeNdWtjOlInTjFpfQTK4c4VqTWXg9XWj67VHjFhLoSnwbyFB5WTzc1zb2AynMvw7AmEjjhY1GMn_lDM3DmLaVJGjkuYPRg9YZBxFp32G_6hlrTl64-es4PvLUO9O8dlVEGZVtXAMVy-srDMgiRdtki5LvKYrRI3u8KlydoDYSIrJIhykXk1HQZNQ8IRNL_aCbKfs7Yh8IT7z8mlywFleenJjBNqcNsFsRBK9Zx88B8NOngc4aFyZnDz-ugqw73uKiDS2Lf5DRnUlfu8klXe2mmLOjgcAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43381c63c7.mp4?token=ltdSZZzejQBDxPln8IY9he6EOU2ZyAxbIpLixrzRMT1dS0rRP5swm5J5ESeNdWtjOlInTjFpfQTK4c4VqTWXg9XWj67VHjFhLoSnwbyFB5WTzc1zb2AynMvw7AmEjjhY1GMn_lDM3DmLaVJGjkuYPRg9YZBxFp32G_6hlrTl64-es4PvLUO9O8dlVEGZVtXAMVy-srDMgiRdtki5LvKYrRI3u8KlydoDYSIrJIhykXk1HQZNQ8IRNL_aCbKfs7Yh8IT7z8mlywFleenJjBNqcNsFsRBK9Zx88B8NOngc4aFyZnDz-ugqw73uKiDS2Lf5DRnUlfu8klXe2mmLOjgcAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الهندي اللي يكضي الفلم يتمرن بالجم حتى يواجه خصومه وتالي ينضرب بمسيرة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/87701" target="_blank">📅 15:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87700">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏هجوم لانصار الله بالمسيّرات على مواقع مرتزقة السعودية بمنطقة العبر في حضرموت</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/87700" target="_blank">📅 15:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87699">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
🔻
هيئة الحشد الشعبي:
تودّ هيئة الحشد الشعبي أن توضح للرأي العام، وللمهتمين، ولمجاهديها الأبطال، أن الجرحى من منتسبي الهيئة قد استوفوا حقوقهم المستحقة ضمن صلاحيات الهيئة، وبنسبة شبه كاملة، سواءً ما يتعلق بالرواتب أو العلاج داخل العراق وخارجه، وذلك من خلال الجهات المختصة في هيئة الحشد الشعبي.
أما الاعتصام القائم هذه الأيام أمام دائرة التقاعد العامة، فإنه يتعلق بملف منفصل عن حقوق الجرحى لدى الهيئة، ويتمثل بالمطالبة بتطبيق أحكام قانون مؤسسة الشهداء رقم (57) المعدل لسنة 2020، ولا سيما الفقرة (ثانيًا)، التي أجازت الجمع بين الراتب التقاعدي وراتب الإصابة، أسوةً بأقرانهم في بعض المؤسسات الأمنية.
وتؤكد الهيئة أن هذا الملف لا يدخل ضمن صلاحياتها القانونية أو الإدارية، وإنما يقع ضمن اختصاص وزارة المالية وهيئة التقاعد الوطنية، باعتبارهما الجهتين المعنيتين بتنفيذ الأحكام القانونية الخاصة بهذا الاستحقاق.
ومع ذلك، وانطلاقًا من مسؤوليتها تجاه مجاهديها، تواصل قيادة هيئة الحشد الشعبي تنسيقها واتصالاتها مع الجهات المختصة، بهدف الإسهام في معالجة هذا الملف، والوصول إلى حل يضمن حقوق الجرحى وفقًا للقانون.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/87699" target="_blank">📅 15:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87698">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء المركزي:
الادعاءات الأمريكية الزائفة حول حركة السفن الاعتيادية عبر مضيق هرمز، والتي تعكس اليأس والعجز للجيش في ذلك البلد، ليست سوى أكاذيب.
نعلن أن مضيق هرمز، كما هو الحال دائمًا، يخضع للإدارة والسيطرة الكاملة للجمهورية الإسلامية الإيرانية، ولا يمكن لأي سفينة تجارية أو ناقلة نفط العبور بأمان عبر هذا المضيق دون إذن ومراقبة القوات المسلحة الإيرانية القوية، ولن يتمكنوا من ذلك.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/87698" target="_blank">📅 15:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87697">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/87697" target="_blank">📅 15:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87696">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/87696" target="_blank">📅 15:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87695">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏رئيس وزراء السلطة اللبنانية نواف سلام يغرد: تم اختراق حسابي وحذف التغريدة</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/87695" target="_blank">📅 15:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87694">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مجلس النواب العراقي يؤجل النظر في الطعون المقدمة بشأن صحة عضوية بعض النواب إلى جلساته المقبلة لعدم تحقق نصاب ثلثي أعضاء البرلمان</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/87694" target="_blank">📅 15:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87693">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رئيس وزراء السلطة اللبنانية يحذف تغريدة له ادان فيها الغارات الصهيونية على لبنان</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/87693" target="_blank">📅 15:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87692">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رئيس وزراء السلطة اللبنانية يحذف تغريدة له ادان فيها الغارات الصهيونية على لبنان</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/87692" target="_blank">📅 15:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87691">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇳🇱
الشرطة الهولندية:
قتيل ومصابون في انفجار بميناء روتردام.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/87691" target="_blank">📅 15:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87690">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
ريبوار رحمن صالح يؤدي اليمين الدستورية نائباً في مجلس النواب العراقي.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/87690" target="_blank">📅 15:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87689">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d0499f575.mp4?token=GGXbT6_fiZdYCs7VlIMTB_L1pY38eg-M75-Ed-95p67G5duVESeiEQZ9dUM8rIwqY0Dj6DC_2DsGWeaqmqC09_uam59RvSglU8bdeGV1LYjL7ky9PsriAry6tmCPFUrIcf-AZGF-uMRuQ-cDYXJj_CVWo3_f4BuozZ7jP8ZVXT-xWqQ5Z2xU2Z2xYhJZVyVxQtaduEoWGqTEDeILGTIE0WNJwxGiy7OX2pGu5gsLEYK-iPmj-RDCsWz1Ubq981KbOOVhSVyVFPG1pMiiNCuQJPxZWYHocPJF4JhtrYZ0qc3E4-bnLBXVZOoMK7qIUn5z7OfCcDqSqiPKdXwwkLmJZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d0499f575.mp4?token=GGXbT6_fiZdYCs7VlIMTB_L1pY38eg-M75-Ed-95p67G5duVESeiEQZ9dUM8rIwqY0Dj6DC_2DsGWeaqmqC09_uam59RvSglU8bdeGV1LYjL7ky9PsriAry6tmCPFUrIcf-AZGF-uMRuQ-cDYXJj_CVWo3_f4BuozZ7jP8ZVXT-xWqQ5Z2xU2Z2xYhJZVyVxQtaduEoWGqTEDeILGTIE0WNJwxGiy7OX2pGu5gsLEYK-iPmj-RDCsWz1Ubq981KbOOVhSVyVFPG1pMiiNCuQJPxZWYHocPJF4JhtrYZ0qc3E4-bnLBXVZOoMK7qIUn5z7OfCcDqSqiPKdXwwkLmJZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الناطق باسم وزارة الدفاع العراقية ينفي انسحاب الجيش العراقي من النقاط العسكرية بين طوزخورماتو وكركوك مؤكدا ان ما جرى هو إعادة انتشار وتبديل ومناورة للقطعات العسكرية إلى جانب تعزيز بعض المواقع بقطعات إضافية ضمن الخطط والإجراءات العسكرية المعتمدة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/87689" target="_blank">📅 15:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87688">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اوكرانيا تزعم استهداف مطار ساكي ومنصات إطلاق المسيرات في شبه جزيرة القرم</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/87688" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87687">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MihCE1mHRCNoqCiC7WJ3X4uwm8_u4s0obVOTsI68mzTNv2ZfHhIbweedLPaeEohCNjnBmA9CSTMmcWHDnIpYd6KGtQVT960BntaQY66_Hm6rgb-sFx9XsjJtGrm6CUxud4NICAxbUZnaina2XKPbIzSxK_dejZRyRgNgwKn5xGpTsx9GDUSXS6MVw3kNvo6cQoRq-AE3sbflJupdOwwjyrQdfMKygeand7zsteWhOLryq1cL1SL6I02OZWRONWcnOyp4CBrQrqKDh5SBC0TsC3QVwBmrVKoByJXbZ6vXDhmb_S4Z8jalPWDf9y9TvP403fPtRPV-lhE5QTE_VySR2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أمين عام كتائب سيد الشهداء في العراق يشارك جرحى الحشد الشعبي مظاهراتهم امام دائرة التقاعد بعد اعتصامهم لمدة ثلاثة ايام دون إصغاء من الجهات ذات العلاقة.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/87687" target="_blank">📅 14:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87686">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hadMPv6dLGSDOl4nKm875P9YvGt9F7q5u2-Z0WzTViQFtm86qKUrfu6ujoAf5gOjR3wkeqOTjtv7t-5kUlecxHJvC3z46exwMcWEctYzRuNg7Sg6-XuKHymlkdf18YV8Y3k0QbmdAMnnl-8-60iukbNAFAG7pzHeqPnUJFfTYFZyHlQZIRrQw56OpWkDvPWAOq514hANq-G7fF45Db-2qmGggq1xlgcPzeuF_C2pwEx7A7U-8NFjIDcmGkHcJJEUC2EZdPHadT9xrIPvjALUypKDQWzY5RiSSViFZkiEdrb8LUHeQax1THQcqYmHmBIbaUHV-e8MK2qqTxdVYsxVLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
رئيس مجلس القضاء الاعلى العراقي القاضي فائق زيدان يلتقي وزير العدل السوري.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/87686" target="_blank">📅 14:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87684">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
الناطق باسم وزارة الدفاع العراقية ينفي انسحاب الجيش العراقي من النقاط العسكرية بين طوزخورماتو وكركوك مؤكدا ان ما جرى هو إعادة انتشار وتبديل ومناورة للقطعات العسكرية إلى جانب تعزيز بعض المواقع بقطعات إضافية ضمن الخطط والإجراءات العسكرية المعتمدة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/87684" target="_blank">📅 14:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87683">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇱
اعلام العدو:
في إطار الجهود لدعم استعداد الجيش الإسرائيلي لمواجهة جميع السيناريوهات: آلاف الأطنان من المعدات العسكرية وصلت إلى "إسرائيل".
أكملت وزارة الحرب استلام وتفريغ سفينة شحن أخرى في ميناء حيفا، كانت تحمل آلاف الأطنان من المعدات العسكرية ووسائل القتال.
تشمل الشحنة، من بين أمور أخرى: جرافات D9 ضرورية، ومركبات هامر، ومركبات مدرعة من طراز JLTV، وشاحنات من طراز أوشكوش، ومعدات أخرى كثيرة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/87683" target="_blank">📅 14:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87682">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇱
نتن ياهو:
يمكنكم أن تسموا بريطانيا بـ "الجمهورية الإسلامية لبريطانيا". قال أحدهم إن أول جمهورية إسلامية تمتلك أسلحة نووية ستكون "الجمهورية الإسلامية لبريطانيا". نحن نتأكد من ألا تحدث أخرى - تعرفون، في إيران.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/87682" target="_blank">📅 14:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87681">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇦
زيلينسكي:
هذا العام، لدينا أقل بنسبة ثلاثة أضعاف ونصف من عدد الصواريخ الاعتراضية التي كانت لدينا في عام 2025. روسيا لديها الآن ضعف عدد الصواريخ الباليستية شهريًا مقارنة بما كانت عليه من قبل. إذا باعت الولايات المتحدة لنا 5٪، فسنتمكن من تجاوز فصل الشتاء وإنقاذ حياة الناس. وإذا تمكنت من بيع لنا 10٪ فسنتمكن من تدمير جميع الصواريخ الباليستية الروسية حاليًا، لدي 1٪.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/87681" target="_blank">📅 13:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87680">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇶
وكالات: الوفد سيترأسه مدير مكتب القائد العام للقوات المسلحة الفريق أول ركن عبد الأمير الشمري ورئيس جهاز المخابرات حميد الشطري.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/87680" target="_blank">📅 13:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87679">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇶
شركة تسويق النفط العراقية:
شركة طاقة رائدة في أبوظبي من بين الجهات التي تشتري النفط الخام العراقي وتنقل شحناته عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/87679" target="_blank">📅 13:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87678">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني كاتس:
نخرّب منازل اللبنانيين في الجنوب ونبني الاستيطان في الضفة</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87678" target="_blank">📅 13:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87677">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
اعلام خليجي:
واشنطن رفعت وتيرة الأرتال المنسحبة من إقليم كردستان العراق تجاه دول الجوار.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87677" target="_blank">📅 13:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87676">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇾🇪
🇸🇦
إعلام سعودي: ‏اشتباك بحري بين زوارق سعودية وزوارق أنصار الله في الساحل الغربي في اليمن.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87676" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87675">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ueq2AcKZKK1Jpkm8qrdFIRpIC7EUTtx_nHF7HpF7sW6TziH1KL1Db12gLLZ5A1jmEO-HMu533-LVylOKbbgtejcfgDeG0OxkqLVOtSyyoqCQNgeREdJMoEn_Ls7rV9I0QL67ad4HRUm9amjqF7GBCTndln5R1YXvie0nucXvh4vRrodFJ7pxQgylmQntHDynUDfkjtAd8QgLg6eDdMy-8HeMRgtZfPeIZWHExcBmPcuYSm4jT26OSVd6vtbEWDVs4Cprmz-9Oo5ViuAJpLMr1_amzt9l-wE1ZiTNTrmAJ_4aQPKVLy4-Fe2i-c5C6maNCGofXYMlXG1D81uK2nYRmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
رئيس مجلس القضاء الاعلى العراقي القاضي فائق زيدان يلتقي وزير العدل السوري.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87675" target="_blank">📅 11:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87674">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFPKO2pBtTQnYOse6Yc5L3nGfF5LTU-LCxEnjx72hkslgG-KtoWxIVTZSteUf2hEfXCLxtKtpqzyanawhMF9viUppocUOmsE7iPQhgksAvZA5NMOX-8nTimIFDblC0oyOD9cfPDdxn0ciLQbk5j-itLI53fw_fjiosIpvpnTbtYjnZi7g6d6L3rWkaTZL9ri13clP3vtjO6tb2NvmVB_yQ5WQVdULpfkl4L_phlPtBz84NpvcKtF6Jeija3HHsHopWwJvUovk4TVbgrEuyhS1l45qXNThqGzMEkfSb5W6rKDphxMRDGGnbpzh62vx3pApJ3zpEhVw0GGFg2X--hQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقجي:
لطالما أخطأت الولايات المتحدة في حساباتها بسبب قصور في الاستخبارات. خير مثال على ذلك: الحرب على إيران. والآن، خطأ أكبر في مضيق هرمز.
‏أسوأ من الأخبار الكاذبة هي المعلومات الاستخباراتية الزائفة. كن حذراً.
‏الله أكبر، أعظم من أي قوة على وجه الأرض. بالله نتوكل.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87674" target="_blank">📅 11:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87672">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">أمبري للأمن البحري:
نشارك في عمليات إنقاذ ناقلة نفط منكوبة قبالة ساحل عمان وسفن الإنقاذ في طريقها إلى الموقع
أفراد متخصصون صعدوا إلى متن ناقلة النفط لتقييم الأوضاع</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87672" target="_blank">📅 09:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87671">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrBhmK7jUJL_a6FQAGjh7LKIw663BbpLjW1R4uEPdJXmO5SlfNy0V-7ChO0UUfHG_lde1kqDDYGKZY4Iao_a85e1pOyF9R9-NjWuvoNUzFqNcMXMm5rqtk3BRNiAIq8LKDO-Ow6xKdxWmU8w14c6MYTnn-dqnBczRK_dhzEp9UIbgcIkakCassuiQAr2HrwHgGBNIvg5GCKBA-XUKNjgN0SbCTYo4JX3EZAmr1GINbC5r6fhvUmlN4RwonI5QKwTt1P-0N0bvStnyYpQ1RO_7LjwNVm5N7VOFybCRfa_eIaCZD0tkasf88QYrwU2YgSXuI1dX0fvFmqd7yELzOHN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
😎
بسبب القصف الإيراني مؤخراً الذي تسبب بهروب وفرار رجال الوطن الإماراتيين ؛ وزارة الدفاع الاماراتية تستعين بفتيات الإمارات وتدعوهن للالتحاق بالكليات العسكرية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87671" target="_blank">📅 09:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87670">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
هزة أرضية بقوة 4,7 على مقياس ريختر تضرب الحدود العراقية السورية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87670" target="_blank">📅 08:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87669">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔻
عصابات الجولاني تطلق قذائف الهاون ورمي بالأسلحة الثقيلة على الحدود السورية اللبنانية بذريعة التدريبات العسكرية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87669" target="_blank">📅 08:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87668">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNX04msXNwmuYbGXqIfZhwpDVhFab83ZicB5ZhQYc5LB92Bli_9T4DBvA87-xrztDLXXJWaqkPYnHk_C3BaTXGkSbp2ZFjWOAhOi1VZST7VG3FtytmS8JrRF49JvUNzCM3HId5SORhkuLq5MhKYgF7iMbGAiKJUqUx7X89Dv1rD-z8NpG9Nynk5eWkVCheyGVaI9pBAwVe2cPY-VK0sEuxZ1QXELN4xIIXJyMyAqB1KKcs6ztit4tnTftJZRiuARoc_Uir3SXENS0hOdVv42VJej6746l05V_Wan0TvKqi5vpTHthOmSFX_6p5Ch0sTtfAwgzWfBekJ7-MvMnzdCaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
دول مثل فرنسا يجب أن تتوقف عن إلقاء المواعظ على العالم بشأن "حقوق الإنسان" والقوانين الدولية. هذا نفاق واضح ومخزي. دعمكم للإبادة الجماعية التي ترتكبها إسرائيل في غزة، والهجمات العدوانية على إيران، قد قضى على أي اعتبار أخلاقي كنتم تتصورون أنكم تتمتعون به.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87668" target="_blank">📅 06:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87667">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZC1kMQEg51Wx_xen3Ab61_pkA0GcYqvUwz-h5B75nBFzG-1RQnlLYD-jxiZjn8kzmANJRTi9sow5-llYkTYbMCzjlx4tZJ-JPHQiLiKKK0JPjiLJaSa8C_jVslcdjiLcJmUlF5sT8ll46sEVopI9hcL0yjJ4lg4si2cNuyOxcayf3nbe5LvmdtbHshodvp4rYj-EgolUnTSCWiGDscMwLKV3_RL_DREHUGP1NojD641kXGo2fGqb2nqmYwq65iPG0n4yF4d5RvW6uUz8wxCskrTaULuyZPNdzTrCCoQxJSW6sQT5-F7MA-F4_AMNIiUJ3MRKJQXt8qPE8-kYtW6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
منصة X تقوم بإغلاق حساب الناطق الرسمي للقوات المسلحة اليمنية العميد يحيى سريع.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87667" target="_blank">📅 05:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87666">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
طيران حربي في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87666" target="_blank">📅 04:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87665">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇶
علي الزيدي:
سماء العراق وسيادته تمثلان رمزاً لن يُسمح باختراق أجوائه أو المساس بأمنه من أي جهة كانت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87665" target="_blank">📅 02:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87664">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
إخراج ترمب سرا من أنقرة جاء بعد معلومات بتسلل خلية إيرانية مع صاروخ يطلق من الكتف.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87664" target="_blank">📅 02:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87663">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrpOQFuRgstk2uf9M-Hgd4VwSwOfpNvh5HfnhOpGyDw2EKVrKbIWYXXQaDPkppC4dfMeCuASmv6akwHKKGdIdgUj-hltd2XMBC91CASscx9ny2NN2epebeCobC9axfVLMg_zZkRk_R-D7zbD8URZcNao70_mRXUpTWBUIqDQwoib6QnNMe3R4_4_jnmlVrQMopDZAPqqxaCe36mu7gKlQuvT_dASpZNX0zrM_7m38RXeYi0lgNPePfUtFiGaNQlUYfoSWpndyLpugo1bl-Y-_aO2YyhZVlxpo5__dzLjKd3WGwsu7N9ghKCQyR6n8vyFUYL5ovpQHxa-JoeHiIXQfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
غارة صهيونية تستهدف بلدة المنصوري في الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87663" target="_blank">📅 02:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87662">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇶
مصدر امني لنايا...
انتشار أمني واسع على طول شارع مطار بغداد بالعاصمة بغداد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/87662" target="_blank">📅 00:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87661">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556bb53c10.mp4?token=A9MORXb0v_cv5MuFfpuZ6UjjTVyBa8b1YikWwjjRQOXY9l-ULJ41OYDew87Zm8JHl3Yd85NWoC4mtnnweMvUBBKkl2xKArVU_DXkQE3Olt_sRy9J8Gm3l5BaJTSvz1iMcYnzSkupUV4s8Y_FQSNyDtTIIRJaJRNIdwE2RTrv1W3f33_g4kMp1puIydEPGEg5eFoPIO9-USQ9Y0ceEfUBOq44Aemrt4aWcZ76i9li1RWa23PrYp_iNpqeqEu0YzZoXWFk2H5tCEbUgkQWxzvlAuPaq70aVeCHhm8Ux-ZG6hUgG7DQjSdQSJqkMztHVb3po0gBQ0Q9vs1qSm2dNjv8-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556bb53c10.mp4?token=A9MORXb0v_cv5MuFfpuZ6UjjTVyBa8b1YikWwjjRQOXY9l-ULJ41OYDew87Zm8JHl3Yd85NWoC4mtnnweMvUBBKkl2xKArVU_DXkQE3Olt_sRy9J8Gm3l5BaJTSvz1iMcYnzSkupUV4s8Y_FQSNyDtTIIRJaJRNIdwE2RTrv1W3f33_g4kMp1puIydEPGEg5eFoPIO9-USQ9Y0ceEfUBOq44Aemrt4aWcZ76i9li1RWa23PrYp_iNpqeqEu0YzZoXWFk2H5tCEbUgkQWxzvlAuPaq70aVeCHhm8Ux-ZG6hUgG7DQjSdQSJqkMztHVb3po0gBQ0Q9vs1qSm2dNjv8-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اندلاع حريق واسع جراء تحطم مروحية عسكرية في تكساس مما اسفر عن مقتل جنديين في الطيران الاميركي.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/87661" target="_blank">📅 23:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87660">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">طائرة من طراز بوينغ 737 تابعة للأسطول الملكي الإماراتي A6-RJA تحلق من أبو ظبي إلى طهران  ‏هل ستتجه المزيد من الجزية الإماراتية إلى إيران، أم أن مسؤولاً إماراتياً رفيع المستوى يقوم بزيارة؟</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/87660" target="_blank">📅 23:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87659">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFHl0brrzXq_saSS8lNqi0vTWnQawZKodLxxj7P3S7Zk7au3RS1u5FCEnrYzx2Bzy2LCDXUUyQOaOYB0LQXlMb3gjqaR6X_yxmdbqzH7xBdX0s2Nz8_YVEu79VHjkZJAg5mLAOCRsQFZjCT9VNq_RAd5qX9hxa7_NmotLqGneHpMciHm2ypNnzMFtHUt-nOBrl1UY0VXyEoi1pfF0-tS-NKIcvrNSxFnUZekVPeSvaMZDf-8JU2N78X9Xwe0n3qxxXPyiILz2jPa43FBqulF9tzX7KRAxH7cEF4YrwWPjJrKQAatwEx0gT5_W4vyweCeZHmZ4wFtq_p9PAtRFfQzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏ترمب: المتحدثة باسم البيت الأبيض كارولين ليفيت ستغادر منصبها نهاية أغسطس.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87659" target="_blank">📅 23:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87658">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbKa2zZqoaqIKpH6_UtZHiXhjHI5l2Yje_PSNuFUDfXf02J9FPd7znZCBVt4p2fJz0OCCKiLyNHxCsJGolaF6CWK7EElSV4Z2CqdoTJXr1i96wI8FY8Lmk0B2dCXRuEsWITGtijy_w19R1iDPaMMXvHlg8C9M8LMErbOai3Orj4_5PlhrqwUdp1gfY3y99U-hbKTmGO7KXHugG931czc6FMwOvqZ3YyLmAXgB8g-VxaDEn9K6v8XDfeuM5TwzK0IBj9DyIwUxLmZfs_L8UlPNiJsd0AOCl-cwMW2QAUTaURKb2OWupOvy71Tf88FEpApZmHNYRScgjzUUQiB5v6Adw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترمب
: المتحدثة باسم البيت الأبيض كارولين ليفيت ستغادر منصبها نهاية أغسطس.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87658" target="_blank">📅 23:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87657">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a260e9217.mp4?token=q6X6LFDLa-8qZLZkeMS-g0ClPZbKrNz0F2n82AbUVD5hfFhBNEpwYEF4_L3ERjypLZCxY4EjVUV9dHL4fEstodyScngNHJBz43zKThycHuxldk-q3YNIEt-BBNtFO_sKkQUT1njxETIMKagCU8y2EM90x5q7KbgOzaCTe6klB4WgEzo0oDVlvWiEntHEKTeYb0u1stVtnZaBsEtP75I34o5ubdYdNa3S5I4Ely5UnF4TnJa_Z4L0EC632WW1KrKYFwnFIAY1IeMW7d04sVAAxB-M0cXHs2hDuLiplTUgeuCLv19UfDLBiPRDE8mV0a9Agt6f9kTvadYMehgM5iK2Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a260e9217.mp4?token=q6X6LFDLa-8qZLZkeMS-g0ClPZbKrNz0F2n82AbUVD5hfFhBNEpwYEF4_L3ERjypLZCxY4EjVUV9dHL4fEstodyScngNHJBz43zKThycHuxldk-q3YNIEt-BBNtFO_sKkQUT1njxETIMKagCU8y2EM90x5q7KbgOzaCTe6klB4WgEzo0oDVlvWiEntHEKTeYb0u1stVtnZaBsEtP75I34o5ubdYdNa3S5I4Ely5UnF4TnJa_Z4L0EC632WW1KrKYFwnFIAY1IeMW7d04sVAAxB-M0cXHs2hDuLiplTUgeuCLv19UfDLBiPRDE8mV0a9Agt6f9kTvadYMehgM5iK2Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
على الرغم من الارتفاع المهول في أسعار البنزين في إقليم كوردستان فإن جودته لا تتناسب حتى مع دينار واحد من سعره، إذ يتم خلط مادة الثنر والماء مع كمية قليلة جداً من البنزين.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87657" target="_blank">📅 22:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87656">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87656" target="_blank">📅 22:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87655">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87655" target="_blank">📅 22:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87654">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKN-Ohq7VCVOzfYmD7BYNvI05Y0Tw5EH8om7fGUPbbx4PQAIC8ADOOqaBojE36XguxZCzcDoF9EyNPtiij6XnRGcvRJmbzcl4aj1EBlCtGma8F02_spN8gm6yODLJOQ1ypiNMWgfKXdDIZEyImyK_GNYQIVmljOGiPh1zSCNFaY4fRnRxc5y6hajDPsNCttYMUZjkKhPHsmOjDk4TvYBnE15BYlJFqfjUyqm0PRq3qOG1wRK-pZEL6T_EtXyeKiuXmIjK3EJY16r5RS8lkwFqttL8nzMjSzjryjmJFOeRKaPGVpYY58KXj8fLXwdnvx3r8dPCeng8oNcFdkDZd44hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هيئة الممرات المائية في الخليج الفارسي:
إن الادعاءات والمنشورات المتكررة من قبل المسؤولين الأمريكيين بأن مضيق هرمز لم يعد مغلقاً لا تغير الواقع: فمضيق هرمز لا يزال مغلقاً ولن يُعاد فتحه حتى يتم قبول شروط إيران.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87654" target="_blank">📅 22:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87653">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec836d6d11.mp4?token=i5U-Id33KO2-pXccv2x97hdaIbvMYdEJlsii8e2-VakopXEfMGt-ayCQeb1uhZGqdUEWHaJONf1R3LUyZ7iiAap_Yxa20mUKCF_nhHHt4C3sQgbxviguNNUSj5y30bLJb22spobGtrjHtZo81jy60M2s465YrarVSdjLqMV3UgHMCDEEHzpv5MEJG14-kTWm87RziI7imLsQdBvIOyB326X1vIR_p2RrIGRXVywYabxt3H73FWVBRSIdwjmwVxRfLw4vpM48qWp6nHDcNGfnpEtK0Ho8XdFBc8hYpplhyRZAidqlAS053gG8YPiEIKl2JGpg46UT4ySmiiJ366HHHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec836d6d11.mp4?token=i5U-Id33KO2-pXccv2x97hdaIbvMYdEJlsii8e2-VakopXEfMGt-ayCQeb1uhZGqdUEWHaJONf1R3LUyZ7iiAap_Yxa20mUKCF_nhHHt4C3sQgbxviguNNUSj5y30bLJb22spobGtrjHtZo81jy60M2s465YrarVSdjLqMV3UgHMCDEEHzpv5MEJG14-kTWm87RziI7imLsQdBvIOyB326X1vIR_p2RrIGRXVywYabxt3H73FWVBRSIdwjmwVxRfLw4vpM48qWp6nHDcNGfnpEtK0Ho8XdFBc8hYpplhyRZAidqlAS053gG8YPiEIKl2JGpg46UT4ySmiiJ366HHHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من حادثة الهركية ومحاربة مدينة كاملة بسبب اختلافها السياسي، إلى حادثة فندق لالازار والرعب الذي عاشته السليمانية جراء الهجمات بالمسيرات ومختلف أنواع الأسلحة، يأتي بارزاني رئيس اقليم كوردستان اليوم ليصرّح بأن فصائل المقاومة ستجعل العراق في عزلة دولية اذا لم تسلم سلاحها.
هل العالم بأسعار النفط الحالية قادر على فقدان أربعة مليون برميل ؟!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87653" target="_blank">📅 21:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87651">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQW5f6CA_QJar43KZQmzo2PSG-yGG5UclMt3gIg2aVcFn47qubAI4sLP2ZSa1vIlqRpr7NNpLSvN7psaVxbY-t3NHz7xidhD2K55H800LaIDSZsA0BIXs-Valp6-tQmlgsco99OZCcSzTFkxnDrK-bVn3gFGFYU1UckJvKIbqRMc6_zmd9R4j3cS50VbeiD6jhymKKxAckc70_5PB4vvcuMqBf79sS0kVMesG98eCJxsSRJutIACbFyd01zfdmg-iyT5NdIklWsaNvxujb6piX-JShmkiMorSE9iy_RfoRKEvL1NYh5LnAsuXLQYke2ZgTEcnOE_RR6FQbORJAdIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6BiIRjitBNQatACNO0AOZWMfaN_QzKEyXbvVpe63rpBtUuR6njZG9YO-GvM1CMslY1ayRDINlXJvDn3dD9xFZ8Kgv4wpj91_IIu9mFcHz-FHpJvX4ePH3zPazQVn80Jss85S6Dp1r9wQ02chu5qr7tMrQeEgekReoQ90V8AYOuSVC_Z63pGjtZxttm5_BfzaJJ3YJifdP4lGRKX794XfKsTy7f0mTWF9GB7kOGIoExuCaT5vN79fUTmFQGKZ0m00bsOIJyKHtP-u-xdwHLVyFX6OwjCPi7MKvdV3821-xAsgsMKXC2F5f9Y1CjkdlOnv_VvjXcvPQLh3E4L9y96yQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇭
سلطات البحرين تستمر في اجرائاتها التعسفية من اعتقالات وغياب قسري في حق الطائفة الشيعية التي تشكل غالبية سكان في البحرين.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87651" target="_blank">📅 19:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87650">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
🌟
‏ترامب:  الولايات المتحدة تسيطر سيطرة كاملة على مضيق هرمز. أعتقد أننا سنحافظ عليه! يُطلق الجميع على حصارنا البحري اسم "جدار من فولاذ"، ولا تستطيع إيران فعل أي شيء حياله. ليس لديهم أسطول بحري، ولا سلاح جو، وجنودهم المتبقون لا يتقاضون رواتبهم، والحرس الثوري…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87650" target="_blank">📅 19:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87649">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
المجلس الوزاري العراقي للأمن الوطني: قرار انتهاء مهمة التحالف الدولي في العراق في 30 أيلول المقبل هو  توقيت نهائي لا عودة عنه.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87649" target="_blank">📅 19:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87648">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇸
‏رفع دعوى قضائية ضد ترامب بسبب بيع حق الوصول إلى منشورات Truth Social.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87648" target="_blank">📅 19:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87647">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZHKj2NH_nZ1eLdk9uv6DKab3IvvZ8JKNaEZIcoIjDeyFo-3M-QeoXwG_74i_bMDT8OhFtn6QyWUr7CxQpATUks3737dUgyQpWUaz2MSx9EECM5Gr9PHjjtM2-aRb7oiebv9BmCFQVaZBSQtzsVzwhMgrGhZShENkVH07Xk8cU1Jwe2BjpToh0Ii8TaorwrxuOwM7yhXAOpKtTPG3NhvhvON44lcERej19qtuhirfLzVWIN80TSYPJRp01VZJG9WD0kqrKqEinCWD_6wEVR3Ld8ONv5_VkVVJ7eXRi3DKju-6Tv1fUcaj4LBojkftYWe0hDSSVKK_oN1ybcyyic-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
‏تتجه ناقلات النفط السعودية حول رأس الرجاء الصالح لتجنب انصار الله في اليمن، فيما تتوقف معظم الناقلات في البحر الأحمر عن العمل، وتتجه أكثر من 12 ناقلة فارغة نحو موانئ عُمان والإمارات.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87647" target="_blank">📅 18:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87646">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تذبذب عدد من خدمات الاتصالات بالمنطقة الغربية في ليبيا بسبب تعرض الغرفة الرئيسية لاستهداف بمسيرات.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87646" target="_blank">📅 18:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87645">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">The bully of the world no longer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87645" target="_blank">📅 18:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87644">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
المجلس الوزاري العراقي للأمن الوطني:
قرار انتهاء مهمة التحالف الدولي في العراق في 30 أيلول المقبل هو  توقيت نهائي لا عودة عنه.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87644" target="_blank">📅 18:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87643">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
وزارة الخارجية الأمريكية تطلب من سفاراتها في منطقة الشرق الأوسط خططا للعمل بعدد محدود من الموظفين.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87643" target="_blank">📅 18:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87642">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmAE4VvGtfcXveYrgVMapKjdm7BhW-xry-1W_WPXs8lw9V0tDHOsDxY1Y2xEe0SFyBYn1cRk6Gaq_4R-NrimnSNUi09YfchQzu-uI-X8W1KbtnIkcledVJ_ImOdbec5q9ShJTrf5ZBgAZNXd1AYjPgq8j3I6OP5mB_Egudxf1Hr2jBaRvQKF1BcsB3dgw3jYNWG2E2nmqBDU0AEEBgea1Yzh2mZUbbZn9UnEYGRAQh-weUo9VhAX0xoG-OG4vdg2CPoDAGSsLCs1UtoIF4gXnPb4nARgZlC2DpRDQQqSPWE1Fxlbvl3_IWTwMaC_C7YVSqep5mbskfgjhAIeuvLVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">The bully of the world no longer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87642" target="_blank">📅 18:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87641">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuvcfbMnhA6XzXD64FDhYBlTJEzctsmsihQddvwGvUUTVEB-TcUtKWPvSzTunTSo0Yy3CYbOXqUryQ1P4lfXIlbHbijbptx1bkUG0ge2fq0gxfVQdpa4aoieBZPVzKmZv-BUAMTaNM-k8ung0AyJeNWKGVMSdPj9MfNbTGStRMNAtWMdXCg0tIxnXKTv5IO-fdlQi_8t6qdIj2M10iATh_L46V5tDJ9e2ssXVD8lmPRZyNuBRWFTmmoi5XPtKTUVNTB1sh0EjRz0TxG6_ebUcbuiduN6OQAgi7OMPqi69djK9gB3ntYXNHJ3JomkBCR03Ax5Fxwec0djYe1XQfn28w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
‏
ترامب:
الولايات المتحدة تسيطر سيطرة كاملة على مضيق هرمز. أعتقد أننا سنحافظ عليه! يُطلق الجميع على حصارنا البحري اسم "جدار من فولاذ"، ولا تستطيع إيران فعل أي شيء حياله. ليس لديهم أسطول بحري، ولا سلاح جو، وجنودهم المتبقون لا يتقاضون رواتبهم، والحرس الثوري الإيراني مُنهك ويهرب، وقيادتهم غير مستقرة، في أحسن الأحوال! ليس لديهم مال - بلادهم في حالة يرثى لها. كل ما لديهم هو أخبار كاذبة وتضخم بنسبة 300%، والوضع يزداد سوءًا! إيران مجرد كلام بلا فعل، لم تعد مُستبدة الشرق الأوسط. الحمد لله!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87641" target="_blank">📅 18:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87640">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
نيويورك تايمز:
يقول صيادون إكوادوريون إن رجالاً غامضين يتحدثون الإنجليزية ويرتدون شارات عليها علم الولايات المتحدة هاجموا قواربهم بطائرات مسيرة مفخخة ما أسفر عن مقتل أو فقدان عدد منهم.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87640" target="_blank">📅 17:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87639">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTP0kf2DpXe9E7bQL-NTXrNHXBv0o5y7Ve9zpkNkIpVqgZQ0h9n0rt2GlNiDQxfvI4KS8VOaqoGpvOFdSlv8G0cWwJ6A_BGUv8SQPd1FFdZCXWV9oJNcozi0mhQ6GhiaudIAqiDFe5k8bg4_NlIkEmSWTFqpC1A5YIa9WLz5Bx6zRgVJJvFauOFj5ui4_YcIjlPLipQFNXPdfOnl0W73acernaMDWwClgB3hXijI0pTL9G-hEbTiZ9N0q6rXKc5MAekzw8oCItQYUJrLFrAGVJUs0xMzWSrezzVWfFZyFJL6eZVDGDDiGu2JnfvXFZjJZPXRmieRJJGSxKeVWAUMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
النائب حيدر المطيري:
يا وزارة الكهرباء العراقية حقيقة أم حلم أم خطأ مطبعي. 801 ضعف بين المبلغ التخميني (900 مليون) وبين مبلغ التعاقد (721 مليار) لشراء 4 آليات، هذا ما كشفته اليوم لدى مراجعة تقرير ديوان الرقابة المالية الاتحادي.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/87639" target="_blank">📅 17:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87638">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇾🇪
🇾🇪
انصار الله:
السعودية تخفي خسائرها لا سيما عدد القتلى وحالياً نستهدف البنى العسكرية فقط. ننصح أبناء اليمن في المعسكرات السعودية بالانسحاب منها للحفاظ على أرواحهم وسنقدّم لهم مكافآت</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/87638" target="_blank">📅 17:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87637">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d416ce65.mp4?token=PyzdFD7rHzG28_Dvy8ujOOb-2U6xVNrWtuvaB6Lh50jCXzUGWvHCumWDTqhCWbTTviCMP4chyeZ1KH24SKeQd91B8JhgifCrJTaJt2h0ifFWWZsDgwCYmgYK7qel36Ffqq180yftZsq7mR1Ai96Q1cdlRflNRWm3jQqKh9eqnZvR0KZcVXh2wuQv2fH5A0lPnbjKqLz1WE8GdAE_cN8dFZ5jgpfhZCTjGsvd_iJDWyZmJwWe8FjIlqevhq6HKUmnCxIcTLXAvMD_0Wu7cErQcztpB7uvEwB1G93ttjoZXFD86RM0kp0RfuIMvFCGaiXuqiDmyS68gmVcAIVtLsBnaqpTyO1TrTjoccU0tAjaWpleQeWf_UDNc6oL1Ucr9fMyH2_ZNIKRg3KagAyz0KSUnGDici6ROLhU4ravn91m8qBD_oZmHyTQ1nM3J2LP-Z3qYMvv9e7w01ZKbP0AzhreOYyyE_JShRCOFSHDDwGSc0iK2g_PdZ4LZhKNStWmTS2xspw4wZJVMHBhjxeQ7ADiAjInQ6uq-a671fxxYRbUZ_SvZ8jhAFGduRddSV03Go9Cs0NDZK-km8IpGprdtk53qzFXmEi00ewURBjbviTRncahAlN-dJOykJWji8GF8g_32U0RrKdmxUQ8FzEUFDueC_KkhzFSQm30eTtaMkql8Kk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d416ce65.mp4?token=PyzdFD7rHzG28_Dvy8ujOOb-2U6xVNrWtuvaB6Lh50jCXzUGWvHCumWDTqhCWbTTviCMP4chyeZ1KH24SKeQd91B8JhgifCrJTaJt2h0ifFWWZsDgwCYmgYK7qel36Ffqq180yftZsq7mR1Ai96Q1cdlRflNRWm3jQqKh9eqnZvR0KZcVXh2wuQv2fH5A0lPnbjKqLz1WE8GdAE_cN8dFZ5jgpfhZCTjGsvd_iJDWyZmJwWe8FjIlqevhq6HKUmnCxIcTLXAvMD_0Wu7cErQcztpB7uvEwB1G93ttjoZXFD86RM0kp0RfuIMvFCGaiXuqiDmyS68gmVcAIVtLsBnaqpTyO1TrTjoccU0tAjaWpleQeWf_UDNc6oL1Ucr9fMyH2_ZNIKRg3KagAyz0KSUnGDici6ROLhU4ravn91m8qBD_oZmHyTQ1nM3J2LP-Z3qYMvv9e7w01ZKbP0AzhreOYyyE_JShRCOFSHDDwGSc0iK2g_PdZ4LZhKNStWmTS2xspw4wZJVMHBhjxeQ7ADiAjInQ6uq-a671fxxYRbUZ_SvZ8jhAFGduRddSV03Go9Cs0NDZK-km8IpGprdtk53qzFXmEi00ewURBjbviTRncahAlN-dJOykJWji8GF8g_32U0RrKdmxUQ8FzEUFDueC_KkhzFSQm30eTtaMkql8Kk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المستشار الأعلى لقائد حرس الثورة اللواء محمد نقدي عن ادارة ترامب: هؤلاء الأشخاص لا يعملون من أجل مصلحة الإنسانية، بل لا يعملون حتى من أجل أمريكا. إنهم يعملون من أجل مصالحهم الخاصة. بمجرد إغلاق سوق الأوراق المالية، يبدأون الأعمال العدائية، وعندما يفتح السوق،…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87637" target="_blank">📅 17:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87636">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔻
المستشار الأعلى لقائد حرس الثورة اللواء محمد نقدي: حتى لو استمرت هذه الحرب لسنوات، وحتى اليوم الأخير، ستُطلق صواريخ إيران. إذا جاء يوم لا يتبقى لدى إيران أي صواريخ، عندها سنكون أكثر خطورة على أمريكا. تمتلك أمريكا آلاف المصالح الاقتصادية في جميع أنحاء العالم،…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/87636" target="_blank">📅 17:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87635">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
المستشار الأعلى لقائد حرس الثورة اللواء محمد نقدي: يجب علينا تحقيق الردع بحيث لا يجرؤ العدو أبدًا على مهاجمتنا، حتى نتمكن من العيش بأمان. إحدى الطرق هي إطالة أمد هذه الحرب حتى نصل إلى الفترة الرئاسية الامريكية القادمة، والتسبب في استنزاف العدو، بحيث إذا أراد…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/87635" target="_blank">📅 17:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87634">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e9534074.mp4?token=m9lHt4OAwTZxc5Nq488n82u6oqJwDSnvW0n2OhXDYpyUIOL8sBol8mOcpHefVOi94l840T6V34XIhS1nmHGJWsywUoUYBhh60viQnV_iHSJ6BkI38qG10bD9c4Yyw2VESI6ahN712AArIijTWZwEApLu1kWQhk-qc7OpWn3eogGFVVb7EqQK2BCmZ5CJUK1kDNnRQ8Ylc6Or8xdt0D4uQ7lly2gVymun6A91R1NWuJT9GqLDVYTUCOTTSLJgEDj26YiWDerxOpUgJoA8NoApOztkyDO6VCV-4FhWNyokz9pLCVHZk9qibJm9NTJfm45H4_LHLPrb9J-29FcsNukqpKt9kDEBjmXvSuIuOei7jldax6X1O-6M8mfGJLMXoTgkQjCOJENaAfsEpYKCj56tPm_jDRxTl5aakLt9UFgq83SCMTmK-VwLNmVPrGdZYUiMo2lIS1pCAwHXGu25lV7hpVDJHp5fwJuQHtdb0I13yHNnm6_NlL1tgSUtCKrZIaadf22pEoaiX4QSZsLsUCkukM0DO8aeS-7T9QHwyKIEpRqrYy2lYm4ncXmrPQJezrnbayDg-W2lrdXIMMV8zhM5L4EOcHE4cVcfjQ5o3XFjj4tT3l6lLTvB6M-0QgXZ9F4e5rFuMsGsK9025vci2vC8Tsutn65YxQre9536KSp404U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e9534074.mp4?token=m9lHt4OAwTZxc5Nq488n82u6oqJwDSnvW0n2OhXDYpyUIOL8sBol8mOcpHefVOi94l840T6V34XIhS1nmHGJWsywUoUYBhh60viQnV_iHSJ6BkI38qG10bD9c4Yyw2VESI6ahN712AArIijTWZwEApLu1kWQhk-qc7OpWn3eogGFVVb7EqQK2BCmZ5CJUK1kDNnRQ8Ylc6Or8xdt0D4uQ7lly2gVymun6A91R1NWuJT9GqLDVYTUCOTTSLJgEDj26YiWDerxOpUgJoA8NoApOztkyDO6VCV-4FhWNyokz9pLCVHZk9qibJm9NTJfm45H4_LHLPrb9J-29FcsNukqpKt9kDEBjmXvSuIuOei7jldax6X1O-6M8mfGJLMXoTgkQjCOJENaAfsEpYKCj56tPm_jDRxTl5aakLt9UFgq83SCMTmK-VwLNmVPrGdZYUiMo2lIS1pCAwHXGu25lV7hpVDJHp5fwJuQHtdb0I13yHNnm6_NlL1tgSUtCKrZIaadf22pEoaiX4QSZsLsUCkukM0DO8aeS-7T9QHwyKIEpRqrYy2lYm4ncXmrPQJezrnbayDg-W2lrdXIMMV8zhM5L4EOcHE4cVcfjQ5o3XFjj4tT3l6lLTvB6M-0QgXZ9F4e5rFuMsGsK9025vci2vC8Tsutn65YxQre9536KSp404U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المستشار الأعلى لقائد حرس الثورة اللواء محمد نقدي:
يجب علينا تحقيق الردع بحيث لا يجرؤ العدو أبدًا على مهاجمتنا، حتى نتمكن من العيش بأمان. إحدى الطرق هي إطالة أمد هذه الحرب حتى نصل إلى الفترة الرئاسية الامريكية القادمة، والتسبب في استنزاف العدو، بحيث إذا أراد أي شخص آخر مهاجمة إيران، فسوف يعرف أن هناك ثمنًا لذلك.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/87634" target="_blank">📅 17:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87632">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزارة ‏الداخلية الكويتية تزعم: الموقوف تلقي تدريبات تتعلق بصناعة المتفجرات والطائرات المسيّرة لاستخدامها في تنفيذ مخططه الإرهابي.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/87632" target="_blank">📅 17:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87631">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‌‏وزارة الداخلية الكويتية تزعم: جهاز أمن الدولة يحبط مخططًا إرهابيًا داعشيا كان يستهدف إحدى المنشآت الحيوية في البلاد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87631" target="_blank">📅 16:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87630">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌‏
وزارة الداخلية الكويتية تزعم:
جهاز أمن الدولة يحبط مخططًا إرهابيًا داعشيا كان يستهدف إحدى المنشآت الحيوية في البلاد</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87630" target="_blank">📅 16:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87629">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
‏
البيت الأبيض:
على إيران التوقيع على الاتفاق وهي تعرف ما سيحدث لها إذا رفضت.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/87629" target="_blank">📅 16:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87628">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57727b7186.mp4?token=c39rbmC169M5zL2jbwLTDx0tbkukE4yC38clXD8lseyEi8TUKbmn3AOjaFI6uE0KOMN32BzChaU3qnGLQ26z0wSNIStNU8mKAA9prv81AYwd6i3SqFpnWbIxj0uOCnPanB0c9Q4yAQ5T8YoO5w7RXqAGLedCwssDivSA-KDczA-vRqfIOsF3npi2L99669Y4iMLvXDW11sqD9FV-ZmrvlHlpVSrrS9j9G_DTqMHKFc0py8KN85EwQmYn429tEZUBwBvPzqPzdvhicinXH-v4owiYOzxFkoCiEKN4FNlKydp1hkVa-B12IHIWwnRVE4nmI0uQCikrfQSgq2FBTfWHew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57727b7186.mp4?token=c39rbmC169M5zL2jbwLTDx0tbkukE4yC38clXD8lseyEi8TUKbmn3AOjaFI6uE0KOMN32BzChaU3qnGLQ26z0wSNIStNU8mKAA9prv81AYwd6i3SqFpnWbIxj0uOCnPanB0c9Q4yAQ5T8YoO5w7RXqAGLedCwssDivSA-KDczA-vRqfIOsF3npi2L99669Y4iMLvXDW11sqD9FV-ZmrvlHlpVSrrS9j9G_DTqMHKFc0py8KN85EwQmYn429tEZUBwBvPzqPzdvhicinXH-v4owiYOzxFkoCiEKN4FNlKydp1hkVa-B12IHIWwnRVE4nmI0uQCikrfQSgq2FBTfWHew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">التقى ببشار الاسد بعد اسبوعين سقط  تحالف وية باكستان، باكستان دخلت بحرب وية الهند وانفجارات الارهاب كل اسبوع  تحالف وية تركيا، مباشرة سقطت طائرة F16 لهم وبدون سبب  الدرس من ذلك: لا تتعاون مع بن سلمان فگر ابن فگر</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87628" target="_blank">📅 16:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87627">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRtHnsDWTiZA4OhHtvl8Tl8j1MPa4dVWREGuvh4NL05zL1Emhf-JKGdiWIfI4C_tJcDop-FMEdAtBVWolum5Y6zHDWYDquCJ25Afs4acIPlYYtv8Ljps5xK_C0cbIM_Yos-Nxctm9335Ky91Bnz6e17vuscnMhP-zt7nRQcMHzjWLZc9o-_4YFGJwtYoqnnJofqVDTLSI7wB86b_Slb7s1n08b4nZDgLFU__fe_Gf-ISLZ2gN95ZElBrn9Nc79C3jPQ9U6FhunfTrJFtnjxLc4hrYZJH6iNna8SYGFvZErvgNXJhmB0I65kN0dolVmiyuln09CwhtVXMEXe4Xs3qHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
تحطم طائرة عسكرية من طراز إف-16 في محافظة يالوفا التركية خلال رحلة تدريبية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87627" target="_blank">📅 16:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87626">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06d02b8565.mp4?token=aXdZhxr9fUVUOA7ZW4cUqLnnFeLESiE_eScmVmjMHmRwR-sEvY2J6BzM03KwXjqHvomwSmahsEGL0T0EYIZd3gF0dQ-gJzUAvPwN8uQk5IApccztm9dEGujQkbIOCCOUxBDVkczl9Z0OWJBiYkQmab2V_mbMoD6filzokJLv4zIlvaWO2MzBVfymSAoODSq4v9ILd4eLvxUwNwh9MwY0ACGiTJEV6i0keyE5QvnD6GPmgnhXHh6SutKlCp1ElOqjcNdOVy9FqkdZRSxG96aYzcFil1jnkmMV17ZQHc5JbVNffJDxuZwzKl1MyEERzcRYcbWIJk3rg6F-bHcpDbQ29g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06d02b8565.mp4?token=aXdZhxr9fUVUOA7ZW4cUqLnnFeLESiE_eScmVmjMHmRwR-sEvY2J6BzM03KwXjqHvomwSmahsEGL0T0EYIZd3gF0dQ-gJzUAvPwN8uQk5IApccztm9dEGujQkbIOCCOUxBDVkczl9Z0OWJBiYkQmab2V_mbMoD6filzokJLv4zIlvaWO2MzBVfymSAoODSq4v9ILd4eLvxUwNwh9MwY0ACGiTJEV6i0keyE5QvnD6GPmgnhXHh6SutKlCp1ElOqjcNdOVy9FqkdZRSxG96aYzcFil1jnkmMV17ZQHc5JbVNffJDxuZwzKl1MyEERzcRYcbWIJk3rg6F-bHcpDbQ29g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تحطم طائرة عسكرية من طراز إف-16 في محافظة يالوفا التركية خلال رحلة تدريبية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87626" target="_blank">📅 16:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87624">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇸🇦
🇮🇶
إعلام سعودي: وفد أمني عراقي رفيع يزور السعودية غدا.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/87624" target="_blank">📅 16:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87623">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بيانات تتبع السفن:
السعودية تقوم بعمليات تحميل النفط في البحر الأحمر مع إيقاف تتبع السفن بسبب هجمات انصار الله في اليمن.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87623" target="_blank">📅 15:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87622">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇲🇦
وزارة ‏الداخلية المغربية:
منشورات عبر مواقع التواصل تحرض على العبور الجماعي نحو سبتة ومليلية يوم 15 أغسطس.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87622" target="_blank">📅 15:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87621">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇱
🇮🇷
اعلام العدو:
بعد اختفاء مواطنتين إسرائيليتين في النمسا يوم الجمعة الماضي، يحقق الموساد في القضية، وسط شكوك باختطافهما من قِبل جهات إيرانية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87621" target="_blank">📅 15:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87620">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">منظمة أوبك تخفض توقعاتها لنمو الطلب العالمي على النفط لعام 2026 إلى 580 ألف برميل يومياً (التوقعات السابقة 780 ألف برميل يومياً) وترفع توقعاتها لنمو الطلب العالمي على النفط لعام 2027 إلى 2.16 مليون برميل يومياً (التوقعات السابقة 1.94 مليون برميل يومياً).</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87620" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87619">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onNIYNpj1Xl6Om1R6COQisUlzwfe2Njt_DDKX0c158G6rcMGyOXH2f2xbWEsZ4M3WKhY2EQ0dsqjyA7X-qIhdO6P1aYhyMNG31dWXRphJ46AoyUFJgoRtRUEIXTDWx9Lh78ViMwKD7aG0TghJcErntTEH5um6Q4dZwtDmoCwB7sdPtMoFJksjS2sTkMMPglh2uy3qcg9k0ZgdEpuEOyj4oKQLtsHOj5vM3wseK1qv1OKEmpHEJmMB48_DR8286hO0ri6XIEkfB3rOxdBb7_XdtqwfsE9ZODKgp5FdJI3YL5Cpc1_8i-BCRDsOUe4uuQM3mwLKrEvFy20Yqe3ixQZAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
كانت داخل شاحنة اردنية..
كمارك طريبيل العراقية تحبط تهريب سحبة أركيلة إلكترونية متكاملة و(390) قطعة كارتج و(310) قطع كارتج إضافة إلى (12) حبة مخدرة فضلاً عن قطعتين من مادة الحشيشة بوزن إجمالي (5) غرامات كانت مخبأة داخل الشاحنة بقصد التهريب.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87619" target="_blank">📅 15:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87618">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">عدوان سعودي مدفعي يستهدف منطقة بني معين غربي محافظة صعدة اليمنية</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87618" target="_blank">📅 15:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87617">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
فايننشال تايمز:
اوكرانيا توقف هجماتها على الناقلات في البحر الأسود عقب طلب مباشر من جي دي فانس نائب ترامب بعد ان اكد أن هذه الغارات ألحقت أضرارًا بمصالح الشركات الأمريكية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87617" target="_blank">📅 15:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87616">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇩
وزير الدفاع الإندونيسي:
لن نسمح بإنشاء قاعدة عسكرية أمريكية في البلاد، التعاون مع واشنطن يقتصر على التدريب العسكري فقط ويجب احترام سيادة إندونيسيا.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87616" target="_blank">📅 15:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87615">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
رويترز عن مصدر إيراني كبير:
لا موعد لوقف إطلاق النار ولا شيء هناك لتمديده.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87615" target="_blank">📅 14:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87614">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇸🇦
🇮🇶
إعلام سعودي:
وفد أمني عراقي رفيع يزور السعودية غدا.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87614" target="_blank">📅 14:11 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
