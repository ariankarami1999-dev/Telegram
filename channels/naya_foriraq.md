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
<img src="https://cdn4.telesco.pe/file/TqI87NaW7jnZsESUqDsR7eKyGCOYPOgXmq8uoY-VlsQZHRsE2cpdEJj6qNiiDGyO9nUDchbsS-Q5BaUAdKHxyXFYGaYYLE4Jitna0xGLjrieCQxDPzFSdCXIqyrx1JRFzA_cWOnft8J_-O4I0S8shjIgIE0tTJNHfRFzztzHRAEhVV3P_rZmMmfXh_zeglAzb3hbIenkeUz-WXB5H5TST2UFmEsEAQBhKpYSNwMe_D6sL8rzNFmSCeOB9KAS7UldBn94xJqa8x3MRbczXEBI1SsYL-M_Y1j6pDRwhhd71sbAIvpUQFDkle_DRrlDJDIdsWnZ83fqk3I5ETsUa7dDJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 05:29:24</div>
<hr>

<div class="tg-post" id="msg-86595">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044c3ed5b4.mp4?token=Fyc1AVs35X__i6RuoZPlLwCGKFX2m1FZ6c7ykL6mk3ika9Oz58FNHZhKje3qrLV7saAlOn0MxI4K9-8QBlvdZ9rZvj0ro7v-0mNoeM07DbxWPLWFLJcpmjShmJj9J9Pxbg5IgTOfXr189FpSeXz8moJQuf4Yk3K8Oz_y9P23RQfTTD7BDEH-MKRtmMrkWKLfoxRouJ99wPbzDEsMo46pF70aupTKPj89UMRA1fsykqsl3za5ljqDeAZN38unl28ep2ncXmcdZcmPY9COKFvPw6aKR1gvzb3JU6B8OCdd-6H3e6xAkKrsFA9je8RN1PIs6ypsnAm6oYSw3pRLKZz6D05xs0TSJzbcQMTzWwk1JdfZXKW63LkQZ0ZOGLj9oaoaCmgVBkJFoaBeRRQYqiRqzDAirMOm6M26rtCk_qNhrU0HGhaVRaqIjsBoISd3-E4KgEPQddpIwmZgEh_SNfm_Z7WF9aEhozpIjUHOx4OF9JcZkUqQVU2-aQMsCp73TWaxxzbqArXg222GH3wNucbtJDsN-IVsPBlF15gdYOgj8rA78WQ2hzG0sirYvyxVXt4evuuHQqugszYxrwD5Ck5en-P9IXa_5__hMX3LGPGuaLFSEI2S2Dwg-VOfT4UvzHwAM9TjtZhBoR59jnSNtuFLKPrWVttv6chKXRpvmjNCobM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044c3ed5b4.mp4?token=Fyc1AVs35X__i6RuoZPlLwCGKFX2m1FZ6c7ykL6mk3ika9Oz58FNHZhKje3qrLV7saAlOn0MxI4K9-8QBlvdZ9rZvj0ro7v-0mNoeM07DbxWPLWFLJcpmjShmJj9J9Pxbg5IgTOfXr189FpSeXz8moJQuf4Yk3K8Oz_y9P23RQfTTD7BDEH-MKRtmMrkWKLfoxRouJ99wPbzDEsMo46pF70aupTKPj89UMRA1fsykqsl3za5ljqDeAZN38unl28ep2ncXmcdZcmPY9COKFvPw6aKR1gvzb3JU6B8OCdd-6H3e6xAkKrsFA9je8RN1PIs6ypsnAm6oYSw3pRLKZz6D05xs0TSJzbcQMTzWwk1JdfZXKW63LkQZ0ZOGLj9oaoaCmgVBkJFoaBeRRQYqiRqzDAirMOm6M26rtCk_qNhrU0HGhaVRaqIjsBoISd3-E4KgEPQddpIwmZgEh_SNfm_Z7WF9aEhozpIjUHOx4OF9JcZkUqQVU2-aQMsCp73TWaxxzbqArXg222GH3wNucbtJDsN-IVsPBlF15gdYOgj8rA78WQ2hzG0sirYvyxVXt4evuuHQqugszYxrwD5Ck5en-P9IXa_5__hMX3LGPGuaLFSEI2S2Dwg-VOfT4UvzHwAM9TjtZhBoR59jnSNtuFLKPrWVttv6chKXRpvmjNCobM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">كلا كلا آل سعود..
تشييع الجثامين الطاهرة لشهداء اللواء 30 الذين ارتقوا نتيجة العدوان السعودي الأمريكي الغادر الغاشم في محافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/naya_foriraq/86595" target="_blank">📅 04:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86594">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇱
إعلام العدو:
حدث أمني في الجيش الإسرائيلي والتفاصيل لاحقًا.</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/naya_foriraq/86594" target="_blank">📅 03:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86593">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cffc20c83.mp4?token=pzmL1UOyJfIi6irRdf2m4WyxoZ0QZqN3u71d4PwUplkYTq8Qfm3DiVwE-O7XdGIMYv3b8wdfZ5OO0C3Hf0JUaoAQ6sPPo7H7noro2NfwYyeLnqDBdSVpKCxYQJk0TK9DmLC7sbxMGCG_7t1L_YWtsoPfZDkk_7WELtRtzaCxLxwr1B9CN-glxlu6_IzCMnvt3Lp2aS_1bUdgBuvPFmQPWPKnY-HACtzkfu7Cxns9ImDJWJVGwqEgv5jPOkx5sF2umS-zfFU8ke3ZVXC5qk8MTAaDnweBiDpE2yikd4kcDq0FguWchnYa8-HX8JkGZues8pa-Vz-29O50sRkgE2emUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cffc20c83.mp4?token=pzmL1UOyJfIi6irRdf2m4WyxoZ0QZqN3u71d4PwUplkYTq8Qfm3DiVwE-O7XdGIMYv3b8wdfZ5OO0C3Hf0JUaoAQ6sPPo7H7noro2NfwYyeLnqDBdSVpKCxYQJk0TK9DmLC7sbxMGCG_7t1L_YWtsoPfZDkk_7WELtRtzaCxLxwr1B9CN-glxlu6_IzCMnvt3Lp2aS_1bUdgBuvPFmQPWPKnY-HACtzkfu7Cxns9ImDJWJVGwqEgv5jPOkx5sF2umS-zfFU8ke3ZVXC5qk8MTAaDnweBiDpE2yikd4kcDq0FguWchnYa8-HX8JkGZues8pa-Vz-29O50sRkgE2emUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
إقلاع مستمر للطيران الأمريكي في قاعدة موفق السلطي الجوية بالأردن.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/86593" target="_blank">📅 03:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86592">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇸
إغلاق جزئي في مطار دنفر الدولي بالولايات المتحدة الأمريكية بسبب تهديد أمني محتمل.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/86592" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86591">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7OE8neXgogf8ckM9FlB_Y8Ex1BQ3rmT1K8UMhs88C4JwRRo9EbMhCTFzCup0KjO3uMc5KbbTEd939OskFHjo1QafGkrfEwfBXIoWdpSQMqxlkgHqPWDJ64woBDzTIce0dPr081112rx8klnEO_MpgtCWK5KtsC4fQJEnJ_Lnbs9t1nTwKdvSP1H9dEwlqhU_eIY3sCGm8kTjcG5G_wDG00E-8V5Rys1X5LCOjB_yXxISV5Xh0rRw3XWy9nFREsvwN96WAtcl-05wrDN8mKyjE82j6xRS4Ll2BVBuG4h2BrlvNw4nCE80GgAtLwp-EgII3iLIm8lavQ5vHwD1PvyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇺🇦
قصف صاروخي روسي كبير على العاصمة الأوكرانية كييف والنيران تشعل السماء وسط انقطاع واسع للكهرباء.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/86591" target="_blank">📅 02:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86590">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇸
🇮🇷
‏مسؤول أمريكي: ترامب أمر بجولة جديدة من الضربات ضد إيران ستستمر لعدة أيام</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86590" target="_blank">📅 01:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86589">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
البيت الأبيض:
طهران أخلت بمذكرة التفاهم وأطلقت النار على السفن و
قتلت جنودا أمريكيين
.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86589" target="_blank">📅 01:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86588">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu9fGDNEs-NbzdVh_tb4hQ2k7ucgQ25sRmixv4e7ZNm_qOzZ2I0fqPLYcQnupDaUD2CoglJ_C8Ltsdj588hNGx8mJET0AXMZJiTnO-awkBmT8AhIFtpf4Nm9qFI_vASklua9ntPCvBf26ey9BJxOFReNLHAamgAPw_MqZxYOtbmy-GF3QS0bpBOx9TB9Z4lEsAFpGfryQtnWYLKH0ojNIniKfrJIfK6-fN3qHnr5rjkfd_SosX8O8QlQqMLgTvUIS3iMW4qPnFNEs_lYieO6ZlDkArASb_kq_fRpXR3rdiPUGEOmW5LrGsl5VM19uoxnuFm_9ZIC5rRN445_oYpf9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الأمين العام للمجلس الأعلى للأمن القومي الإيراني:
إن استمرار الحصار البحري وإشعال الحروب الذي يمارسه النظام الأمريكي سيؤدي إلى تشديد الحصار على مضيق هرمز وإغلاق المضائق والاختناقات الأخرى. وسيدفع الاقتصاد العالمي وسوق الطاقة والناخبون الأمريكيون الثمن.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86588" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86587">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔹
مسؤولين أمريكيين وأوروبيين:
روسيا تزود إيران بمراقبة الأقمار الصناعية والاستخبارات الإلكترونية التي قد تساعد طهران في تحديد مواقع القوات الأمريكية، وتحسين دفاعاتها الجوية، وتشويش الأسلحة الأمريكية الصنع.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/86587" target="_blank">📅 00:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86586">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔻
تسجيل لمحادثة تحذيرية من قبل القوة البحرية التابعة لحرس الثورة الإيرانية، وعودة سفن النفط من مسار غير قانوني وغير مصرح به.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86586" target="_blank">📅 00:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86585">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
🇮🇷
‏
مسؤول أمريكي:
ترامب أمر بجولة جديدة من الضربات ضد إيران ستستمر لعدة أيام</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86585" target="_blank">📅 00:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86584">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇸
🇮🇶
وسائل إعلام خليجية:
القوات الأميركية تبدأ الانسحاب التدريجي من إقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86584" target="_blank">📅 00:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86583">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الاعلام الغربي:
‏تستعد الولايات المتحدة وإسرائيل لقصف أهداف متعلقة بالطاقة في إيران في أقرب وقت ممكن نهاية هذا الأسبوع.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86583" target="_blank">📅 00:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86582">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇾🇪
العميد يحيى سريع:
في إطار تثبيت معادلة "الحصار بالحصار" ونتيجة لإحكام قواتنا المسلحة للحظر البحرى على سفن العدو السعودي النفطية تم إجبار ثمان سفن نفطية سعودية على تغيير مسارها باتجاه الرجاء الصالح.
تؤكد القوات المسلحة أنها مستمرة في عملية الحصار للعدو السعودي وأن يد القوات المسلحة ستطال سفنه بإذن الله حيث ما تمكنت من ذلك.
تحيي القوات المسلحة بإعزاز وتقدير شعبنا اليمني العظيم المؤمن المجاهد على خروجه المليوني في الساحات والميادين رغم غزارة الأمطار ونؤكد له أننا لن نألو جهدا في إنهاء الحصار عنه واسترداد كل حقوقه بإذن الله وقوته.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86582" target="_blank">📅 23:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86581">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
ترامب: لو لم يكن لي، لما كانت إسرائيل موجودة اليوم. لمَا كانت موجودة، وكانت إيران على بعد أسبوعين فقط من امتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86581" target="_blank">📅 23:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86580">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇧🇭
إدارة مطار البحرين الدولي تُصدر تنبيهات احترازية للمسافرين والعاملين في المطار.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86580" target="_blank">📅 23:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86579">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
ترامب: أنا أقوم بعمل أكبر بكثير مما كنت قد أعلنت أنني سأفعله. كنت سأتدخل وأدمر قواتهم العسكرية، وأدخل، وأخرج.  ثم أدركت أنه إذا فعلنا ذلك، فعلينا أن نحافظ على هذا الوضع بطريقة ما. وإلا، فسوف يعيدون بناء ما دمرناه.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86579" target="_blank">📅 23:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86578">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
🇺🇸
‏ترامب: ‏مع إيران، وبحسب التعريفات، فقدنا ما بين 16 و18 شخصاً، و‏نفس الأشخاص الذين أبقونا في فيتنام لمدة 21 عاماً يشتكون الآن من إيران.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86578" target="_blank">📅 23:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86577">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇸
ترامب: "هل تريدون أن تنتهي الأمور بسرعة؟ أعطوا الأشخاص المضطربين أسلحة نووية. ستنتهي الأمور بسرعة كبيرة."</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/86577" target="_blank">📅 23:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86576">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90150a3aec.mp4?token=IU1fx1jfLsn27_i0DhsxwvcGyv4OYuKAEni55SnXdq3qgP3s9NeRA03MdM4BYBzKfqLZt9SI7ItriDNPCh3kFRdaFt7kB1qvc_jteDCTrmm74bNsLOyAO10k6UCDEn6EpycvIIux2LbycqRv2sVAa9Y7_T680BoLLlBdqGSvoxX2ruOKEzhWWPX3jdyyTv2NPC-f0vXQNG7YvWVsI3dMAUDFw6bquheOXFo4Kxbjl0vrU_hoDkdvPsjE8N8HyqneYU2qCjWsDCb647DMpadUzaPIb_r4-CeConQKTogcKkq07L8p6Kgax2qcUN7Mws9mON_DM0rBzkUQhSD8l1uo8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90150a3aec.mp4?token=IU1fx1jfLsn27_i0DhsxwvcGyv4OYuKAEni55SnXdq3qgP3s9NeRA03MdM4BYBzKfqLZt9SI7ItriDNPCh3kFRdaFt7kB1qvc_jteDCTrmm74bNsLOyAO10k6UCDEn6EpycvIIux2LbycqRv2sVAa9Y7_T680BoLLlBdqGSvoxX2ruOKEzhWWPX3jdyyTv2NPC-f0vXQNG7YvWVsI3dMAUDFw6bquheOXFo4Kxbjl0vrU_hoDkdvPsjE8N8HyqneYU2qCjWsDCb647DMpadUzaPIb_r4-CeConQKTogcKkq07L8p6Kgax2qcUN7Mws9mON_DM0rBzkUQhSD8l1uo8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار عسكري كبير في حي جميلة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/86576" target="_blank">📅 23:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86575">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ce236252.mp4?token=nbpjqwVinx-e-iQNxmREUrl1RDOLDxZ6h6wKJMG0Jsx4r-PMU_bZrLAEf4Kd0SNKUqFpv93YZSWbO7QcZ53hxmewQHgIYfJz797OtNBpTplXrqFV0aOecseO2o1EmC7-ZtrLG9j2VT1xOYyOfU5M81c4c3edL9QKhF1W3caueLoBKm3tkz8-mvgm5wNe_sJ1xQxrkfGFroqj20VMjumoAPHJzt9gXAOJbziwqM21rhW-o3cZ5eE9vivVEXzHbXW9v6N0MTHN-4a6uzX4f9wh0Dwi_oJsXPH0zJP1uJifw2B4FtDEKdr_D9hDnXjit6Vp9gmwlmAx8210RzqKl5TGhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ce236252.mp4?token=nbpjqwVinx-e-iQNxmREUrl1RDOLDxZ6h6wKJMG0Jsx4r-PMU_bZrLAEf4Kd0SNKUqFpv93YZSWbO7QcZ53hxmewQHgIYfJz797OtNBpTplXrqFV0aOecseO2o1EmC7-ZtrLG9j2VT1xOYyOfU5M81c4c3edL9QKhF1W3caueLoBKm3tkz8-mvgm5wNe_sJ1xQxrkfGFroqj20VMjumoAPHJzt9gXAOJbziwqM21rhW-o3cZ5eE9vivVEXzHbXW9v6N0MTHN-4a6uzX4f9wh0Dwi_oJsXPH0zJP1uJifw2B4FtDEKdr_D9hDnXjit6Vp9gmwlmAx8210RzqKl5TGhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب
: "هل تريدون أن تنتهي الأمور بسرعة؟ أعطوا الأشخاص المضطربين أسلحة نووية. ستنتهي الأمور بسرعة كبيرة."</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/86575" target="_blank">📅 23:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86574">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اندلاع حريق حريق مجهول قرب القاعدة العسكرية في مطار بغداد " مطار دبلن "</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86574" target="_blank">📅 23:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86572">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
استنفار بين البعثية للبحث عن الشخص الذي ظهر في مقطع الفيديو بعد مطالبته بمكافأة قدرها 33 مليون دولار زاعمًا أنه أبلغ عن مكان اختباء صدام حسين(
الحفرة
).
كفمي كفمي شوكلاطة
😆</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86572" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86571">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
‏تعرضت 67 سفينة على الأقل للهجوم أو الاقتحام، وقُتل 17 بحاراً، منذ بداية الحرب مع إيران.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86571" target="_blank">📅 22:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86570">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5605707ff5.mp4?token=TLMQ_ZnBd--qsBkJtOoz8bDKsLduy4rJxa9xYCSqz1WCvU-6vTrzbqV6fsxBVDHMyrUqtQRYBGnKu6rgP85yo6xKN_HBb4UZklAs3TOS7baS-NgKX-jox8rIHtZfL4Y4XKl3j4sd50eWSno-ahiBMEgB-4CNvV03xBiDKd0zIA2mM3Gjrlsibm6f5J0x1G4RadwIsViX9c2vNANM8LYzkbSiCamQROWP0V2lUk74xZ96va77vZxIsAn9eBIeWafo0OSsrBYXDYgW8_73Ejif6Vy3MkZphp6bewGRgJQfjXbBxbAbRui7WjlM2uobswHdB04XlmOscp6uG1iEu5taDZNJ2-teutl50TRveo6ceUv7MKpYfNKHJUFwzTHHBEkHw5yIMHkcAgC7xYnP-shqQ3dQqh8eKNnmEx9qO4oLrd_CnqnFT5dAFw4-zdyn9C2MQ47ZbrzG8o3cxViFn3NDIUd7BIuVCkb7ErBy_DTJCyR91uq-pDfd7_x3SOdzjdPw_05oEBR9VIGzHiNZVP2H2sfTp_kQCIPUpvudQz8UZJq0lagHCtyIDkLH4gy6pANun1VVMdWqHk15v61GfjuLJt0JS2eQct25XUjqp0KsloSsUqlBhxu12qIOrgmrszu3t-NimUO5kNvK3XyYiUT-AYqycuKjjgFb7cqo0SuQcNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5605707ff5.mp4?token=TLMQ_ZnBd--qsBkJtOoz8bDKsLduy4rJxa9xYCSqz1WCvU-6vTrzbqV6fsxBVDHMyrUqtQRYBGnKu6rgP85yo6xKN_HBb4UZklAs3TOS7baS-NgKX-jox8rIHtZfL4Y4XKl3j4sd50eWSno-ahiBMEgB-4CNvV03xBiDKd0zIA2mM3Gjrlsibm6f5J0x1G4RadwIsViX9c2vNANM8LYzkbSiCamQROWP0V2lUk74xZ96va77vZxIsAn9eBIeWafo0OSsrBYXDYgW8_73Ejif6Vy3MkZphp6bewGRgJQfjXbBxbAbRui7WjlM2uobswHdB04XlmOscp6uG1iEu5taDZNJ2-teutl50TRveo6ceUv7MKpYfNKHJUFwzTHHBEkHw5yIMHkcAgC7xYnP-shqQ3dQqh8eKNnmEx9qO4oLrd_CnqnFT5dAFw4-zdyn9C2MQ47ZbrzG8o3cxViFn3NDIUd7BIuVCkb7ErBy_DTJCyR91uq-pDfd7_x3SOdzjdPw_05oEBR9VIGzHiNZVP2H2sfTp_kQCIPUpvudQz8UZJq0lagHCtyIDkLH4gy6pANun1VVMdWqHk15v61GfjuLJt0JS2eQct25XUjqp0KsloSsUqlBhxu12qIOrgmrszu3t-NimUO5kNvK3XyYiUT-AYqycuKjjgFb7cqo0SuQcNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستمرين بالمواجهة لن نخضع ولا نركع إلا الله .. والسلاح هو ملك وخزينة للدفاع عن الشعب العراقي والمستضعفين
المقاومة الإسلامية كتائب سيد الشهداء</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86570" target="_blank">📅 22:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86569">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
يواجه البنتاغون حقيقة متنامية بعد أشهر من القتال في إيران.
يتقلص مخزون أمريكا من صواريخ الاعتراض الدفاعية لدرجة أن المخططين العسكريين يدرسون ما إذا كان بإمكانهم مواصلة الدورة الحالية من الضربات الانتقامية المحدودة.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86569" target="_blank">📅 22:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86568">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
العقود الآجلة للخام الأمريكي ترتفع 1.29% لتبلغ عند التسوية 84.67 دولار للبرميل.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/86568" target="_blank">📅 22:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86565">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fG43g8zOAmay9RtgbzqdtGYiXmdAcaf6RZGPUG_wrxfj39xHI0kVit1LpFK1iRzyK9j-RDUPIuOL934LV8qhIXiMI0eUeqn_z7W_rQR0kHov4oddn1U0NtF-h37hcujzjq46l-xC48lj8pnUrw44HXOXd3vV45pIE0Kg6Rw_qVUEhmddsY1eE2P_zhlAr3adT0QtLqBuMm_Fhr3EoT5sPgZykezUwbGSxaOF36d2zNsEK6Xro0AR_yQQ4nqIPport6NT1Y3e9dAUknz5daj1EheWOCpww28-5opJzshNkStr-NkjhpwtBtR18vB8EFVG3m600c6FXfnRBwD540JkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLCh3DDhdycR1JGxvy151wyGqLgDExisK1QSUeXJu8tN9to_ZTFRnCrLpTrtOd_BN57kYQb_8uyK62XwVG8IphoMNgs-WZwNZ_NqJ-qY95vjut0s-x8BI7qgrTUDK9PZNMfDnBW1oOcZcSWEZ8QyEGxbEEkh4gLWBxRcciBDlniFg-NK0R0eiiSQOzr7Q8tyO5ACtpsaYoR2fZ0RFMR4vr-ieAguDlN7bNmO0I8Wxcf5ZrhuWdkFYTx10UlAZ_Kr746efqZj4u82RE79G3E-VFGhu0PhQAAQMgF_ue3mMVVdcytcz9xJoNwtvB1wwe1gqevwTMyS9dNArDdRB9DVyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXZY6OzITKJZVnssCg5wFL6oypOa2qgKgUBJEc21goSeD0mFv3UT3uomkGrjh13kaN6Ds1M0xgRrsSQXDilwzZ-9diANxNRN3i7wopI_oRrYJRq03N9ErRic6nsgMVVk5hHHb8jgmv8sRYVqVUqXl8FByXpgqhKAXzSu8rpGljJXGjsmuZNT3PkAILctF__SZYz3zm0yqjz54rWSDmPJNxODbA5SF9EiMJjPjoRvyiujqsdGh5rf4Y0qSPA87G8ldS7fXKZZDmUTCaBx_rOmhyKbbOzCM1fcaflXxtPmjSQDufbRQpPqObMhfvtPqPl26HiELVoBDB6qzgJ-KnGoBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤡
🏴‍☠️
🇮🇶
خلايا اوكرانية تنفذ هجمات في العراق وتُنسب للفصائل.. مستشار الأمني القومي يكشف سراً "لم يسمعه العراقيون" من قبل</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86565" target="_blank">📅 21:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86564">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e0d6ec59a.mp4?token=ePzGWfHt4Rj6W0NH2UcPniOcnB0LFcjmrJVFu9lcMh-1Uyes7hST-7H3a71jb6pNQQyj0htXaOA-y-YoIDuWEfPTfTzOCdlQlpMmCtxNgQAb1TutB1PQ_rw2RHWibgWM9FE1pKIbSNsAL9x7NsbkLFolz25AZd__D6WEjy6hf-JUfFoom3oJ2sUY2X0qCfkAgV2kBw29yfBmQiFM1IB8v2x3bOWlSKulYF8fuwZ79UrI507NH9dUmc7PjFYynj5Vx2eJlal7ZTl91VaG9QPzBIWSVP_k_vlgwyCP6oyxwviUzIPRLt9a6uND8AS2UtWD4IBk4T0NbuJcAVGhuU0h8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e0d6ec59a.mp4?token=ePzGWfHt4Rj6W0NH2UcPniOcnB0LFcjmrJVFu9lcMh-1Uyes7hST-7H3a71jb6pNQQyj0htXaOA-y-YoIDuWEfPTfTzOCdlQlpMmCtxNgQAb1TutB1PQ_rw2RHWibgWM9FE1pKIbSNsAL9x7NsbkLFolz25AZd__D6WEjy6hf-JUfFoom3oJ2sUY2X0qCfkAgV2kBw29yfBmQiFM1IB8v2x3bOWlSKulYF8fuwZ79UrI507NH9dUmc7PjFYynj5Vx2eJlal7ZTl91VaG9QPzBIWSVP_k_vlgwyCP6oyxwviUzIPRLt9a6uND8AS2UtWD4IBk4T0NbuJcAVGhuU0h8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ارتفاع اعمدة الدخان من وسط القاعدة الاميركية في ولاية كاليفورنيا. وتدمير طائرة F35</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86564" target="_blank">📅 21:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86563">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67da2ed6f7.mp4?token=evRh-32yGc328owZK_eOHlB2NeNlGoEiy084JoKU4GLh09-JyCjsReeMuMsOXFy3CQ70L6QnAsCU9Bv6cnoZvo0-F2OgddIvqQQ6hNrornqo3pADYHZRdUBE3SJyu7FQbwi0TDJIVWHzce1EYZFOOqOP81347i5Rgj7jdT7cq_wunoa1115Ia5ggInVa0hqElbPqNMYbQ7qTEUSmtdgGkomcMhGAXVEiW-U2y-hh6La5vthC3E8K9pRSff9fg9pPP_VTJSRsfsiMfHpUVgSeOlQ53YVR6LIbvXAeX7cETFidteuebWW80nGG4UgKcbaPS5EzSXbpyxd9PinvckP26g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67da2ed6f7.mp4?token=evRh-32yGc328owZK_eOHlB2NeNlGoEiy084JoKU4GLh09-JyCjsReeMuMsOXFy3CQ70L6QnAsCU9Bv6cnoZvo0-F2OgddIvqQQ6hNrornqo3pADYHZRdUBE3SJyu7FQbwi0TDJIVWHzce1EYZFOOqOP81347i5Rgj7jdT7cq_wunoa1115Ia5ggInVa0hqElbPqNMYbQ7qTEUSmtdgGkomcMhGAXVEiW-U2y-hh6La5vthC3E8K9pRSff9fg9pPP_VTJSRsfsiMfHpUVgSeOlQ53YVR6LIbvXAeX7cETFidteuebWW80nGG4UgKcbaPS5EzSXbpyxd9PinvckP26g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات داخل قاعدة عسكرية أمريكية في كاليفورنيا</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86563" target="_blank">📅 21:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86562">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات داخل قاعدة عسكرية أمريكية في كاليفورنيا</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86562" target="_blank">📅 21:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86560">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlnFTEHyag_86UGniRf_SdiaJW5lzuqMkofFi3RtbAsAcxkngRjf_lBriTmgiiPT_n0s2Gx-wugv56sl8LZPaCMpDuzoPSnNYLbA7LMJ3iHUUK4uSsqr4GoARl4VLIPTn4nkmn25tN2n90dcxiuHyu9kI3oSyTUHFTsWff2ZD52fDa0L4PO0cMMk36zqXBwCOUmIMWm2HNXoEbxKM-Xm393fn938CZwiGCv7Xhm47i5hTFJDtl_WwbeIe4DKxsOfUPWE0BdXacIfdlTEr3y08xhxIFUc7h811dwa7lJ2FAE45Aeq1sC_bpWBluqN5Vk9yX4ah6gCqdYaC9ZalgqQeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصرنا
😆</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86560" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86559">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4999db8b.mp4?token=dftjh-MNby1ecaPWecaT8yRxToOUGRAk7KjI2LnlcmxHGFD6807VJ-e8l704oj9dw13WP581GFrrPhJMxWcslyRf5DbWzPEk3Pz813TMnQOBmyCfwyfIijIdeQsvS1JuM4sxKrTYBFETq4Vof2Xu4plFLf7fMKCqffp9RNH8SO1d3puBqJ8XWEWOxpVhvcm4Lh-3xd4qe2YiUZkYxPGpEYP7DhN-Rp7PZydvwlQm7pY3ipC8MB4zAcWw2kffQ3FvJKh1OArZaVyJzT6m4FpggnZ3AHWETHFuE06XmFjjhDmpo31gVE9aBb69JX5rnrms5a6oAC_Xv9YfIsL4PSJEbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4999db8b.mp4?token=dftjh-MNby1ecaPWecaT8yRxToOUGRAk7KjI2LnlcmxHGFD6807VJ-e8l704oj9dw13WP581GFrrPhJMxWcslyRf5DbWzPEk3Pz813TMnQOBmyCfwyfIijIdeQsvS1JuM4sxKrTYBFETq4Vof2Xu4plFLf7fMKCqffp9RNH8SO1d3puBqJ8XWEWOxpVhvcm4Lh-3xd4qe2YiUZkYxPGpEYP7DhN-Rp7PZydvwlQm7pY3ipC8MB4zAcWw2kffQ3FvJKh1OArZaVyJzT6m4FpggnZ3AHWETHFuE06XmFjjhDmpo31gVE9aBb69JX5rnrms5a6oAC_Xv9YfIsL4PSJEbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إنهم يتحدثون عن البرنامج النووي لمدة سبع ساعات. وأقول: "لماذا سبع ساعات؟ يمكنكم إنجاز الأمر في خمس إلى عشر دقائق."</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86559" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86558">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇸
ترامب: إنهم يتحدثون عن البرنامج النووي لمدة سبع ساعات. وأقول: "لماذا سبع ساعات؟ يمكنكم إنجاز الأمر في خمس إلى عشر دقائق."</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/86558" target="_blank">📅 20:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86557">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7828268882.mp4?token=PiueIPBB4x9fMvglSjl9XNR5LGp53gkIVBdEf0ilqwwUYq9upZDLrfb7HXyTWSKZJuXrEHKHB3DU8I3hTqOGNXpg5VGGeL7F9NUartK4q0JHfuo0m_Wh2rmS5VYGBVCdlA5RPKvMqf7tdqdE96AXaaKwJshUHd8OjOw_rpMDfpEs12RnqOGnnlxBmk_MS9oK7Y7rCH0ulNfRA1Iibhb2YR66lm90rKb5RMXcuYNMcAEPuM9ZtBEZ8cRZa8thOfQxKFVIed5tr5ghquXHql_dkIXawbtw_toBTQqtRdaC4FsG3VHt5zhFYbw770cPs1lddxSQsXOL3CgqsRnneyATUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7828268882.mp4?token=PiueIPBB4x9fMvglSjl9XNR5LGp53gkIVBdEf0ilqwwUYq9upZDLrfb7HXyTWSKZJuXrEHKHB3DU8I3hTqOGNXpg5VGGeL7F9NUartK4q0JHfuo0m_Wh2rmS5VYGBVCdlA5RPKvMqf7tdqdE96AXaaKwJshUHd8OjOw_rpMDfpEs12RnqOGnnlxBmk_MS9oK7Y7rCH0ulNfRA1Iibhb2YR66lm90rKb5RMXcuYNMcAEPuM9ZtBEZ8cRZa8thOfQxKFVIed5tr5ghquXHql_dkIXawbtw_toBTQqtRdaC4FsG3VHt5zhFYbw770cPs1lddxSQsXOL3CgqsRnneyATUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: الدبابات الروسية كانت متجهة إلى كييف، لكنها علقت في الوحل، قرر أحد الجنرالات السير في الوحل بدلاً من السير على الطريق السريع، حيث كانوا يتقدمون بسرعة.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86557" target="_blank">📅 20:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86556">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf2738436a.mp4?token=N7-Own6IxIYzlpx0xmO_INPUzyziO4u36YeBvF4KwOsxcLCBEWkktTWhJmf5NusZZTby8EXG5aSldAIvxFIKrc52fCcjPv059PEk2iQRqfAGGtXAIeovRq6HxzyVLm7yTII87Y88m2pX51RWbk63YsuO99S6sRapQN4-qJxgsOmhIQghJk_ENoUrmpgPJQqZC7Iz40c9y8XgKFKOFynfeNSgFxgTdSi1PWg5OFyYsK_PAC-dqCJm73wQQQv10igctHtGoXNRg9_xtOkmbj9QuSb1yaL0Fvz2kx5g5dm-K4HNYNfgIracgx7DMvIoLBvOh-Ai3ffl7J1EOzgPKdCw1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf2738436a.mp4?token=N7-Own6IxIYzlpx0xmO_INPUzyziO4u36YeBvF4KwOsxcLCBEWkktTWhJmf5NusZZTby8EXG5aSldAIvxFIKrc52fCcjPv059PEk2iQRqfAGGtXAIeovRq6HxzyVLm7yTII87Y88m2pX51RWbk63YsuO99S6sRapQN4-qJxgsOmhIQghJk_ENoUrmpgPJQqZC7Iz40c9y8XgKFKOFynfeNSgFxgTdSi1PWg5OFyYsK_PAC-dqCJm73wQQQv10igctHtGoXNRg9_xtOkmbj9QuSb1yaL0Fvz2kx5g5dm-K4HNYNfgIracgx7DMvIoLBvOh-Ai3ffl7J1EOzgPKdCw1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
المراسل: ذكرت أن إيران لا تزال لديها بعض القدرات. هل يجب على الأمريكيين الاستعداد لمواصلة هذه الهجمات المتبادلة حتى تصبح إيران غير قادرة ببساطة على الرد؟ ترامب: ستزداد قوتهم قليلًا، ربما الآن، ولكنهم سيصبحون أضعف. نعم، بالطبع. يجب دائمًا أن تكون حذرًا.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86556" target="_blank">📅 20:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86555">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb7c06f17.mp4?token=ctxmor6Bctwiw1SGkDeAeRHWLgOm-cnd8ofunSY_Gval5HyWZDow7R_fX5-BdJoL5vNn49gc0cvLZnh_eJ1vdnsoCbW_MiIPe3QPiYKROFBLX3hl64gPlgtjX3AcUPs_uPd-p6HhzZ2hfvKU8OAKGyeeEtuVl05SofVVeg0IOXY4dDxqiFqQYHI-wkObfAha003SYDQSEmiPMk-0cKqX-RBIA4VR5tDBMkFHnHToXq1j_ziSSZoLhyPM6gLjVcs_4F_MLzWPX-_OYlbA5sjk1eNcmMpgogcYLCGM-2MsBy7xQ5z3nEpwkpIp02dVmkNjUR36jOhwSDto_YkuJNLNMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb7c06f17.mp4?token=ctxmor6Bctwiw1SGkDeAeRHWLgOm-cnd8ofunSY_Gval5HyWZDow7R_fX5-BdJoL5vNn49gc0cvLZnh_eJ1vdnsoCbW_MiIPe3QPiYKROFBLX3hl64gPlgtjX3AcUPs_uPd-p6HhzZ2hfvKU8OAKGyeeEtuVl05SofVVeg0IOXY4dDxqiFqQYHI-wkObfAha003SYDQSEmiPMk-0cKqX-RBIA4VR5tDBMkFHnHToXq1j_ziSSZoLhyPM6gLjVcs_4F_MLzWPX-_OYlbA5sjk1eNcmMpgogcYLCGM-2MsBy7xQ5z3nEpwkpIp02dVmkNjUR36jOhwSDto_YkuJNLNMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترمب: إيران تريد دائما التفاوض وتريد التوصل إلى اتفاق معنا، ويمكن التوصل لاتفاق مع إيران،ويتكوف وكوشنر وفانس وروبيو يشاركون في محادثات متعلقة بإيران.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/86555" target="_blank">📅 20:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86554">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a25f78e699.mp4?token=dp6mUpZK9U2DmNRKAxzgXHmeKEgOtgfrSy7oub5In8AiLiFz5XCJnpDXh1qoK69QpnjE2RjwVkH4LBE9bA9FONqeef5eCQz7ccgkYv0oZW9wSPjToc-eYkRyTBPyP99ZKj0exQIwsGnmf-WgvxBgZ9JLTuZUfLHduf0wNaYV-2i3MxpWaGdIJDJZzQo_0VjWGdsmhDS7hIlmB-DWDBY5L_n9pdXx3SFNVhd9ASCPEL8kbwYG90dQVRahIdhlUIJSbb91RLtlM9xfN339I94YXZagWBYZeQdmg_PUi81V9qKCjdJsd_sFjMaNmmYV8obMd6ptHRsRtwOZSPQ8E2DNqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a25f78e699.mp4?token=dp6mUpZK9U2DmNRKAxzgXHmeKEgOtgfrSy7oub5In8AiLiFz5XCJnpDXh1qoK69QpnjE2RjwVkH4LBE9bA9FONqeef5eCQz7ccgkYv0oZW9wSPjToc-eYkRyTBPyP99ZKj0exQIwsGnmf-WgvxBgZ9JLTuZUfLHduf0wNaYV-2i3MxpWaGdIJDJZzQo_0VjWGdsmhDS7hIlmB-DWDBY5L_n9pdXx3SFNVhd9ASCPEL8kbwYG90dQVRahIdhlUIJSbb91RLtlM9xfN339I94YXZagWBYZeQdmg_PUi81V9qKCjdJsd_sFjMaNmmYV8obMd6ptHRsRtwOZSPQ8E2DNqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب بينغ بينغ بينغ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/86554" target="_blank">📅 19:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86553">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇸
ترامب : "إيران كانت تمتلك أسلحة دفاع جوي متطورة جدًا، ولكنها لم تكن فعالة."</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/86553" target="_blank">📅 19:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86552">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377310bac7.mp4?token=aqZGWag7WLUfEtkbanj8g6CIUf9qwJYVGoDUZHKLOpztcwd2Zmcl928fQwJ7ipL3k_MRUV-iEa6RxAhzedg69vWXC9eytHXmtQ0ALGge5qUBF6LAuvXFhXynn0AAVXlp5AR6eAqkaiWshYnWc0aq0q5F1mreA1yAuu0FzY685c2YevXOaSEY59zoLqZxfrioZJFoipjaG4S_brRwM2nXjB4VmoZtV4MJozZD68R2-6wZpaDvnPv-BCf6UA91jiHXdK-YQpdm4pf7DWkc7dN1fVHVfO_18Ee9gxRpQ_g_NMIgJGmUJbwNZq_Tza68h7bILWHX0cgXyD4cvQLw2FsWNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377310bac7.mp4?token=aqZGWag7WLUfEtkbanj8g6CIUf9qwJYVGoDUZHKLOpztcwd2Zmcl928fQwJ7ipL3k_MRUV-iEa6RxAhzedg69vWXC9eytHXmtQ0ALGge5qUBF6LAuvXFhXynn0AAVXlp5AR6eAqkaiWshYnWc0aq0q5F1mreA1yAuu0FzY685c2YevXOaSEY59zoLqZxfrioZJFoipjaG4S_brRwM2nXjB4VmoZtV4MJozZD68R2-6wZpaDvnPv-BCf6UA91jiHXdK-YQpdm4pf7DWkc7dN1fVHVfO_18Ee9gxRpQ_g_NMIgJGmUJbwNZq_Tza68h7bILWHX0cgXyD4cvQLw2FsWNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب حول إيران: "نحن نريد فقط الفوز.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/86552" target="_blank">📅 19:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86551">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=vcvnfnVwp0jkixqaMFc84hJY71EjbLQJcuASWOlqWs_xSTH5FxI9a55_Kar6E8yGKItF1Gx48qAqUzYS8GPn6MesHmH-gVPo9TuLq64COBKKsZ_RS6AbwEdrjSVTzrLa-OMTsYzKtJPmm71JV7yztWRxT4_dHHo5VHNwwIDaMWTDwcNlHwI2rnWP-9KiVod8zP0Y7PsfKQk3b2_zxF_f1AT1cVMusZh49tJ9XGh3GyGkq0Xx0NfRzhXoC-Jz81FZ-nsPZTopZP8WIud3Hu4xl3D2wzwN7GkwzsQV9-d97uXZiPlDHXlSGqZUZBLi1ySGcilqAv65WN4Ql0zjDWnGGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=vcvnfnVwp0jkixqaMFc84hJY71EjbLQJcuASWOlqWs_xSTH5FxI9a55_Kar6E8yGKItF1Gx48qAqUzYS8GPn6MesHmH-gVPo9TuLq64COBKKsZ_RS6AbwEdrjSVTzrLa-OMTsYzKtJPmm71JV7yztWRxT4_dHHo5VHNwwIDaMWTDwcNlHwI2rnWP-9KiVod8zP0Y7PsfKQk3b2_zxF_f1AT1cVMusZh49tJ9XGh3GyGkq0Xx0NfRzhXoC-Jz81FZ-nsPZTopZP8WIud3Hu4xl3D2wzwN7GkwzsQV9-d97uXZiPlDHXlSGqZUZBLi1ySGcilqAv65WN4Ql0zjDWnGGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب حول إيران: "نحن نريد فقط الفوز.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/86551" target="_blank">📅 19:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86550">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1facef9bcc.mp4?token=aEaN7g73KdOTr4yPq2pFMmyWH5oRlLDo3Jeo1cDFarAH4UrllgKjjt5k8GTw024OEWgnfHNguO3PkgDMtb3VU4PAHQY5gYeqo1zp_kQN1Ez3mhr1vPgR7gFdUrksrHT0klEQotyqGEhZXwVcIVr8z9GZ-vDazFzRBeeejd-i5sbZqN9S4h7ynqq-pSCIuGylQ4cUr_5g2orTc8uw2pwb2uOX-7L63DA6mdI2X5GNJ7x-EsW8mF1WNBu3smw6C7n2zbwRwk524VGnEf2KUGWpNqKgkJOVyu8Goc9uk39X7O41xw_2Hf5mO-45VGQ4NhDP0Jc8M2N1qF-quAD_cBG9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1facef9bcc.mp4?token=aEaN7g73KdOTr4yPq2pFMmyWH5oRlLDo3Jeo1cDFarAH4UrllgKjjt5k8GTw024OEWgnfHNguO3PkgDMtb3VU4PAHQY5gYeqo1zp_kQN1Ez3mhr1vPgR7gFdUrksrHT0klEQotyqGEhZXwVcIVr8z9GZ-vDazFzRBeeejd-i5sbZqN9S4h7ynqq-pSCIuGylQ4cUr_5g2orTc8uw2pwb2uOX-7L63DA6mdI2X5GNJ7x-EsW8mF1WNBu3smw6C7n2zbwRwk524VGnEf2KUGWpNqKgkJOVyu8Goc9uk39X7O41xw_2Hf5mO-45VGQ4NhDP0Jc8M2N1qF-quAD_cBG9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
اقلاعات متتالية من قاعدة الاحتلال الاميركي موفق السلطي في الاردن.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/86550" target="_blank">📅 19:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86549">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
وزير الحرب الاميركي بيت هيغسيث: هل تتساءلون عن سبب عدم مشاركة الحوثيين في هذا الصراع، على الرغم من أنهم عملاء لإيران؟ ذلك لأنهم شعروا بوزن القوة الأمريكية لمدة 45 يومًا.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/86549" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86548">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية:
القائد العام وجه برفع مستوى الإنذار والجاهزية في جميع المعسكرات والقواعد
القائد العام وجه بالخطط الاستخبارية الوقائية لإحباط أي استهدافات أو محاولات اختراق
توجه لتسريع خطة التجهيز والتسليح الخاصة بمنظومات الرادار والكشف المبكر والدفاع الجوي
حماية الأمن الداخلي مسؤولية حصرية لمؤسسات الدولة العسكرية والأمنية
بعض الأطراف الخارجية تحاول إقحام الأراضي والأجواء العراقية في حسابات الصراع
منظوماتنا العسكرية والأمنية تتصرف بأعلى درجات الانضباط والجاهزية</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/86548" target="_blank">📅 19:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86547">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488504489f.mp4?token=bAyVldTjki_0m4UbbcXzerHeojwIm5YgrkuaP8cxf3pKOMcvKxvILmZRteGcBT5bx-QGOTQivKksn-vtaIwjrD4AuHnLmVCjKeQXb-5Pgr1Ad1sicozbF1x1zpasCIOTT8tjlz1zX_r9xxfJEZ6mp4OiscnzZBJE6TEQ3C99k19gKyz4eT7aA_rxvVyTHuDq8P_Yd0HrOucKXppryyDY4u6aB-2o--6R6jNXh3unpLJEW0vARjJOS5n43pdnBL_0FgqHqs9XcFlT2cFj59DT05zI0KLGU5JScWozefD2yio8iwV0lb9Xf2Dl6NiF_8NrJ7W0h5zSod9A8DMox9XQQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488504489f.mp4?token=bAyVldTjki_0m4UbbcXzerHeojwIm5YgrkuaP8cxf3pKOMcvKxvILmZRteGcBT5bx-QGOTQivKksn-vtaIwjrD4AuHnLmVCjKeQXb-5Pgr1Ad1sicozbF1x1zpasCIOTT8tjlz1zX_r9xxfJEZ6mp4OiscnzZBJE6TEQ3C99k19gKyz4eT7aA_rxvVyTHuDq8P_Yd0HrOucKXppryyDY4u6aB-2o--6R6jNXh3unpLJEW0vARjJOS5n43pdnBL_0FgqHqs9XcFlT2cFj59DT05zI0KLGU5JScWozefD2yio8iwV0lb9Xf2Dl6NiF_8NrJ7W0h5zSod9A8DMox9XQQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب :لديهم بعض الصواريخ المتبقية، ولكن لديهم عدد أقل بكثير مما كان لديهم قبل أربعة أو خمسة أشهر، قدرتهم الإنتاجية قد تضاءلت إلى حد كبير. قدراتهم في مجال الطائرات بدون طيار قد تضاءلت إلى حد كبير، ولكن لا يزال لديهم بعض القدرات.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/86547" target="_blank">📅 19:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86546">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/728d2b7bc8.mp4?token=WCq3qC4TGzgV_o2nxFlVi34k2CCpUM8Pvct_oCVa70kFBsVod2eAD6R8hr4I3anClzBg1iX_z7KHMK_T7fhfwkWkfZN3sHulWtFATkNqcnCZhthHB2ih_R932jwIZKkA_Wnd81OUYFZQNQD4VjQHKs9Pp2X9sgBtemNPsv7L5bxNweqNkdd3xlsOOQTWgWXU30mb0R0u__tYPJz9U-PFQx5XaLdzdzFywpLjkAziXcv5ggAg_16aXxEiho_FtDst-yA88YySLGG2DqKdPhoryR7FL5IiQ2Vk5uUhTfeWZgRDVTcqzRHrN7IadjEMYHi7Tjg4GoI6ko056PDMbQ-JyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/728d2b7bc8.mp4?token=WCq3qC4TGzgV_o2nxFlVi34k2CCpUM8Pvct_oCVa70kFBsVod2eAD6R8hr4I3anClzBg1iX_z7KHMK_T7fhfwkWkfZN3sHulWtFATkNqcnCZhthHB2ih_R932jwIZKkA_Wnd81OUYFZQNQD4VjQHKs9Pp2X9sgBtemNPsv7L5bxNweqNkdd3xlsOOQTWgWXU30mb0R0u__tYPJz9U-PFQx5XaLdzdzFywpLjkAziXcv5ggAg_16aXxEiho_FtDst-yA88YySLGG2DqKdPhoryR7FL5IiQ2Vk5uUhTfeWZgRDVTcqzRHrN7IadjEMYHi7Tjg4GoI6ko056PDMbQ-JyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب عن إيران: "نحن موجودون هناك منذ 5 أشهر، وإذا نظرتم إلى فيتنام، ستجدون أنهم كانوا هناك لمدة 20 عاماً، ما نقوم به ضد إيران عملية عسكرية لا حربا.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86546" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86545">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ca7dfea1f.mp4?token=CIjgrbdTGzGIhp1HX9LlRZdcvmu-bc6p2OlU6zMrEtnCk5MVPlM1opSuAL5AE1SpeUZSi-2wwdpHpdZWevReRhFpplArk-FDBoHvw1i2TTf8Mzi9RyqRuzzKKdGxfBiHsx0KudvYDWT8ACi4MGrSN5LREct8Jqh6teE0jXea4itk0W3bx2vfsLfIi7noCp5eHH3QScAmfAu-o5W3c7u2K68Ldew1dmXmKU7HaLNLjuBq2i9CAGxmVUfrzP8xAJ4g_CgWM-YwcKZcfsphDseBTBioxCDEw9yusaHfBsg6HFci5e5y1xM67EJ4N42Re93KV02a2KycKjs93VABDIVN-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ca7dfea1f.mp4?token=CIjgrbdTGzGIhp1HX9LlRZdcvmu-bc6p2OlU6zMrEtnCk5MVPlM1opSuAL5AE1SpeUZSi-2wwdpHpdZWevReRhFpplArk-FDBoHvw1i2TTf8Mzi9RyqRuzzKKdGxfBiHsx0KudvYDWT8ACi4MGrSN5LREct8Jqh6teE0jXea4itk0W3bx2vfsLfIi7noCp5eHH3QScAmfAu-o5W3c7u2K68Ldew1dmXmKU7HaLNLjuBq2i9CAGxmVUfrzP8xAJ4g_CgWM-YwcKZcfsphDseBTBioxCDEw9yusaHfBsg6HFci5e5y1xM67EJ4N42Re93KV02a2KycKjs93VABDIVN-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب عن إيران: "نحن موجودون هناك منذ 5 أشهر، وإذا نظرتم إلى فيتنام، ستجدون أنهم كانوا هناك لمدة 20 عاماً، ما نقوم به ضد إيران عملية عسكرية لا حربا.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/86545" target="_blank">📅 19:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86544">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الله أكبر  مسؤولين أمريكيين: استخباراتنا ترجح أن إيران تقف وراء هجوم سيبراني على نظام المياه في مينيسوتا.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86544" target="_blank">📅 19:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86543">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇱
السفير الصهيوني لدى الأمم المتحدة:
خيار إقامة دولة فلسطينية ليس مطروحا بعد 7 أكتوبر.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86543" target="_blank">📅 18:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86542">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86542" target="_blank">📅 18:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86541">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86541" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86540">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86540" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86539">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a759ef21a.mp4?token=l-y8oOHTv6ca3Ol65tBAteg5NdoxZNwd9Pp844e4UuBxot_J-FQau8JCjgBVfF4cPelkERSiqu9GFzG_NJi0rDV3pgLSENetKLbWS7M74C6XSo_fk5T83dLV6dTaGYSQV_b2AnQFb5YgqmnzETdPp3bT1VSEs3yCoK0xDnqQhH4OyieUwFqCR4eD62OsFmsZzBEezjwRp2G8cI3GtdSRe6claGCsWhI-vv5vLUBRJMAj6jkrJK-nHOk5E7KQR7AAQ9aPqbngDFv8w2rMktm2tru9YxzpxuGYMGXPbBsZurqpMlVBb5CNa3fShRd3-hPEJfWwPpepmQDynYZ6Ylpsnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a759ef21a.mp4?token=l-y8oOHTv6ca3Ol65tBAteg5NdoxZNwd9Pp844e4UuBxot_J-FQau8JCjgBVfF4cPelkERSiqu9GFzG_NJi0rDV3pgLSENetKLbWS7M74C6XSo_fk5T83dLV6dTaGYSQV_b2AnQFb5YgqmnzETdPp3bT1VSEs3yCoK0xDnqQhH4OyieUwFqCR4eD62OsFmsZzBEezjwRp2G8cI3GtdSRe6claGCsWhI-vv5vLUBRJMAj6jkrJK-nHOk5E7KQR7AAQ9aPqbngDFv8w2rMktm2tru9YxzpxuGYMGXPbBsZurqpMlVBb5CNa3fShRd3-hPEJfWwPpepmQDynYZ6Ylpsnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
من بوت نايا
:
"هذا والدي مدمن على اخباركم".
شهادة نعتز بها، ونسأل الله أن يديم عليه الصحة والعافية، شكرًا لثقتكم ومتابعتكم الدائمة.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86539" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86538">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNKumMyBMFlAcy7FwDwtnLoR1PReWZjLSGGpjlhgaxwEh16xsTFylMv-IjTN7h3HFKHzpzo4kx4meLvPC8fIn0g4R_-FMTrtgdGGYDyF8dtUxEZkG2THUEE1xZDoNn3tcZ0kSmjyJtzq6Hf2k-zz7o9zO90iesQbdCNrWPXKLXcD5ObvTuWl9VKY67fxrM2uoGMlB9TSgKg87VMS9MTzg8XzLkQsJQYunw_x-PWapYk3lFEoawLAs5MxOtUuYcseFrGZxn6bjeGzGphwg3CjH9nhPQS6o8CRqkItMhxnqVk7vpdHY6hKr4Qoc0ptPWWVAxBSqRw1Rz-37izGf5-3NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لن نشكر العامري لان زار جرحى الحشد
نتيجة مجزرة ال سعود فهذا واجبه
نحن نشكر موقفه باجتماع الإطار التنسيقي قبل ثلاثة أيام ؛ ستجدني اول واحد يحمل السلاح بوجهكم إذا تم المساس بالعناوين الأربعة ..</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86538" target="_blank">📅 17:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86537">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترمب: شيء ما سيحدث بشأن إيران</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86537" target="_blank">📅 17:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86536">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇱
بن غفير:
مسودة الاتفاق التي نشرها "مجلس السلام" غير مقبولة لدى إسرائيل. بعد السابع من أكتوبر، فإن دم كل عنصر في حماس مهدور، ولذلك فإن التعهد بوقف عمليات اغتيال عناصر المنظمة القتلة يعادل الموافقة على أن تعيد حماس تنظيم نفسها استعدادا للمجزرة المقبلة. يجب أن تستمر عمليات الاغتيال في غزة، ويجب تشجيع الهجرة، وعلى إسرائيل أن تنتصر.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86536" target="_blank">📅 17:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86535">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇸🇾
عصابات الجولاني تعترض الصهاريج العراقية وتمنعها من المرور في مدينة في ريف دير الزور الشرقي.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86535" target="_blank">📅 17:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86534">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffae7e8ee.mp4?token=LovPnkyfmr5ajxNl4-zhfMZ4A6946HjVHDISD-9MHunGHf8a_bQWilnDNQZ2UI9Yygi261ewVEpq_8WJ1hBmTuh_4ESJaJOT1e82Lka6uG7TXxyCltJsXLTffxsxZ9FP4zVrGZvu64p2CccoPnjhjtovWPqt5jHKMbQKa4fCChEb7Npg2wqzatjKAJovwuRrVNZZCmURbYyoYtQMgYFHYsWjgqiY5F7Ya9tSNMKRF6h-zFvG7x7sUT2sWDP8OqL-5GeTw4Qs_ugPdCOUcqpAJB6qIw8cMaWKDCbCQ2FyCfTOzLrrylDW5cwCL-llEKTJHWkAuaH0_ZVgjjPMmHszt7-Y3FWzwyD0_kk0SoMdEwgbUzAjD5M3IQXjpeGoP997Hjus4AxDjGjKhMTg1QLZTRfZMwLkvny9ttE62zPPeXi4tnMuPJjdQu7hycg3HOtk4qGci_phoOXwj3onED7dtyDvGhIoUS8u589m4d8w1ZumJIsz5Ri6R_fGNBKX7yo0SKF0ez0SKZsKaUwids8tuVapQ1u5rIYuAyfxLNFrjpsbV8IYgY2DvCtwAA8jinZ--tP2XuRCSXjsJmTtZsUfrbkqRqI-tZCvSIC5Kaiq3eu7hwy0ES52PBvGC8nYHJGuXKRgv6qDmbs-d4JJ9SxW4boU0UVUhIoAmb69LUp_DKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffae7e8ee.mp4?token=LovPnkyfmr5ajxNl4-zhfMZ4A6946HjVHDISD-9MHunGHf8a_bQWilnDNQZ2UI9Yygi261ewVEpq_8WJ1hBmTuh_4ESJaJOT1e82Lka6uG7TXxyCltJsXLTffxsxZ9FP4zVrGZvu64p2CccoPnjhjtovWPqt5jHKMbQKa4fCChEb7Npg2wqzatjKAJovwuRrVNZZCmURbYyoYtQMgYFHYsWjgqiY5F7Ya9tSNMKRF6h-zFvG7x7sUT2sWDP8OqL-5GeTw4Qs_ugPdCOUcqpAJB6qIw8cMaWKDCbCQ2FyCfTOzLrrylDW5cwCL-llEKTJHWkAuaH0_ZVgjjPMmHszt7-Y3FWzwyD0_kk0SoMdEwgbUzAjD5M3IQXjpeGoP997Hjus4AxDjGjKhMTg1QLZTRfZMwLkvny9ttE62zPPeXi4tnMuPJjdQu7hycg3HOtk4qGci_phoOXwj3onED7dtyDvGhIoUS8u589m4d8w1ZumJIsz5Ri6R_fGNBKX7yo0SKF0ez0SKZsKaUwids8tuVapQ1u5rIYuAyfxLNFrjpsbV8IYgY2DvCtwAA8jinZ--tP2XuRCSXjsJmTtZsUfrbkqRqI-tZCvSIC5Kaiq3eu7hwy0ES52PBvGC8nYHJGuXKRgv6qDmbs-d4JJ9SxW4boU0UVUhIoAmb69LUp_DKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلحين مجهولين يقتلون الشاب "ريگر خيلاني" أثناء فتحه بث مباشر على التيك توك في حي باداوا وسط محافظة أربيل باقليم كردستان العراق ضمن الانهيار الامني الذي يشهده الاقليم.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86534" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86533">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
ترامب: الحرب مع إيران تسير على ما يرام</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86533" target="_blank">📅 16:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86532">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇱
اعلام العدو عن مسؤول كبير:
لن نتراجع بأي شكل من الأشكال عن الخط الأصفر الحالي الذي يفصلنا عن قطاع غزة ما لم يتم تفكيك حركة حماس بشكل كامل من أسلحتها.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86532" target="_blank">📅 16:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86531">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
ترامب:
الحرب مع إيران تسير على ما يرام</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/86531" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86530">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7m7udJ4bYGry3nMVYkQ6nxrE-sVvmIT_a5aO9ddTesmVIRdmt80xCdSN59E2yWehocL41jy52PFD9BW8vt8tyY_QxzDkJ6I7-7GOlJfRWNRsh9n47pJCVM-jfvpSjvbO4wFIpxa-8xby9lKsPJQinIJjlGambvw3SfOzb8lnjYr33KBoM8mgXIDNCxBnxtTZ5D_5hTWM5_x-T41uQd1P2p4u_e17v8ZicTballdWig3iEq7lqY-IsPkBY1_slYyZJ7mfaOPfZnIXhXHe9o5Y-LfnmkRtMi5rlKuN58fLxJjXv6vPs-fSKCG7ejz2L7ax1VAMeaX5vINOc1hs3rH4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇮🇶
بيان مسيرات صنعاء:
ندين العدوان السعودي الأمريكي الإجرامي على الشعب العراقي الشقيق ومؤسسته الأمنية ومجاهديه الأعزاء.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86530" target="_blank">📅 16:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86527">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2ocpRUKrkIpJIkX_BvuDSxeLcawoR1rka9ZI8fGfBocoQwfsj9KmodkW5NySmbCtjoMuxuyTY9eHxOMa0WZpmYycwJK-Ej_47_kbcK-AXE-sHg0CrFHY0mB2raMTNYz9-4Obxrf0jiU_xw7gcJh5ibpaCRk99c3l-kBQPyj2TOrHV_-GzF0W_QYiCgH4upWjpz0KIB_66zbhJiP9upm7CuxzAwnQeWrjnXKATYd7u91xmjE-63W21Bc-nEJGakRgcaDPlw4rzHYxRFs239wS8FxgnqN4qbwTHRZcY3T8xShKMIHfQy9sazGUagEI5zAqAxCvobH3Kp312DlpEzwuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dd236AyeV6pWFGxxcPGghthiH_cPjAqsczqY6Ep7-1ZKbnXpOnaiYzenSXmeb2_uVSRdZGLhOM0xgBy1eH4Bdr2_Qcz68PJlWw34UI0DiEsarbpsT0e_UivZXidyO2YduEyKJoOezcybwJuDlzd_ZCUAV3KxOvYBRX18Ka2fyCMjunIE7IzFwYBpU5cwBIW860IJuyNnql6mCOeJrqNqP7nu5Jw5AbNood-vTiawaPlgS85mPmFF7r71-aFVbgYwCZFIURFxm0RnC9PIvRevGA0sFBF_nDxtzGdLboWaTFMPAbSbgu3lN3HkfaxrWEGhvc6UB7V9RIJWUOUCTgxRcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RuevKKogYbrjwhae1cTgYzFFTIKIItUH99YZXDKSKLUXJkaGJbxMhGvf-o_dzwn-UCVy-XGW6nk7ifmgoL5tkHPbggywEI6mkQHOolTxROXGjz64ZtqDJKkKjaDQ4_a0_qRTazNJ2emL4FJV5BUNJ-bi8OdVRuEmsqZownEuosrNb_gvthKDGFIbjZie17OKf6sgFzeKhmT25mcTbITJG-1dvBpgtC_Oxzfktdl8hj_qk9oYxt-0qJgfk8B_6K2rH0po87CKbGIpuCe9fBJkVDA1g68gQTXWWFJyV-chKX98J7FCYfmSM46YgY6X5uyyBuJN0AIyhCD0vgpAkbm8EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇾🇪
مشاهد من العاصمة اليمنية صنعاء..
العلم العراقي حاضرا في مشهد يجسد عمق التضامن ويؤكد وحدة المواقف بين الشعبين.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86527" target="_blank">📅 16:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86526">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
🔻
بيان صادر عن حزب الله حول العدوان الأميركي على العراق:
يدين حزب الله العدوان الأميركي الغاشم على العراق الشقيق وشعبه الأبي، والذي أدى إلى ارتقاء عدد من الشهداء الأبرار وإصابة عدد من الجرحى، في انتهاك صارخ وفاضح للقانون الدولي ولسيادة العراق واستقلاله.
إن هذا العدوان السافر والخطير على جهة رسمية عراقية، وبمشاركة دولة عربية، يفتح الباب أمام تداعيات بالغة الخطورة على المنطقة بأسرها، ولا يصب إلا في مصلحة المشروع الأميركي - الإسرائيلي الرامي إلى زعزعة استقرار المنطقة، وتفتيت الأمة، وإدخالها في دوامة من التوترات والخلافات والاقتتال.
ووفق مقتضيات حسن الجوار والعلاقة الأخوية والتاريخية التي تجمع السعودية بالعراق وشعبه، كان الأجدر بالسعودية أن تلجأ إلى الحوار وفتح قنوات التواصل الدبلوماسية مع الحكومة العراقية لمعالجة أي توتر أو أزمة، بدلًا أن تنجر وراء سياسات العدو الأميركي والإسرائيلي والغرق في وحول مشاريعهما لزعزعة استقرار المنطقة وتفتيت وحدتها.
إن إيغال العدو الأميركي في سفك الدم العراقي يكشف مجددًا عن نواياه العدوانية تجاه العراق وشعبه، وسعيه الدائم إلى منع استقراره وتعافيه وإضعاف دوره الوطني والإقليمي في هذه المرحلة الدقيقة التي تمر بها المنطقة، ويؤكد استمرار أطماعه في خيراته وثرواته.
يعلن حزب الله وقوفه إلى جانب العراق وشعبه العزيز، ويؤكد أن هذا العدوان يستوجب موقفًا عربيًا وإسلاميًا ودوليًا عاجلًا وحازمًا ومسؤولًا لوضع حدّ للسياسات الأميركية العدوانية، وصون سيادة الدول واحترام القانون الدولي، ويؤكد أن الصمت إزاء هذه الاعتداءات، والاستمرار في التغاضي عن هذا النهج الخطير والمدمر، لن يؤديا إلا إلى جر المنطقة إلى عواقب خطيرة لا تحمد عقباها.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86526" target="_blank">📅 16:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86525">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌟
حركة حماس:
الموافقة على إدراج ملف السلاح الثقيل في إطار الاتفاق قد رُبطت واشترطت بوقف جميع أشكال العدوان، والانسحاب من قطاع غزة، وتحقيق التعافي المبكر، ودخول اللجنة الإدارية، وانتشار قوات الحماية الدولية، وحل العصابات المسلحة والميليشيات التي شكّلها الاحتلال، وإعادة الإعمار، وضمان حق تقرير المصير، وإقامة الدولة الفلسطينية المستقلة، وحماية حقوق المواطنين.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86525" target="_blank">📅 15:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86522">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-MAKFAo7Wm4NgBeL4maziOtj1bI37oxieMJpNhNy9XV5N7L4mptYYKiS2Vkx1rS7rAko6hKtiy6166-gGNj65LBKPXEjm3PWHDjF3TcHQblOkrq1CzdrDGoF41-2nouDwVOtrVzymKITAZ-sQv6968k8KOB0ztTXi9A7jG9xVh0-bXQZc1hzn8di3KUyTKupJVwclmq78AcUj6fvvOdUFgIsJm5_wT7Wu4Z9jB5Y3Vpk1liwYTkAER2ofjUVMFuw9eeZTLkjTk5bpR15LS8M4lxvT1IATM95Ft4P2xfC4uCAR3dfTx6beKYd7VlX5_BaR8AtN3dwnVQAJ1GR6g4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvE4NKevraTe2TAvo1FRqe1l85H-ZpF-I579S9NvtPYtn5wnVIdUxPGih0NwuwKu5TC_5m8kdNVaCO07Im07wKupeAV1ARN45wutDyhJM9_qDvJ3w7GeMZCU7kvLW-b6twgT2ODv2rMQkakglkBdvLZutg7s9lkQBp2I5Y234EUe7Njxd3AKWL8weUN7OZsz57gyfau79ihOv-4kweMbZ2Lc9pkv-EL6Alm-tYrYLVq9SJjR6WyBvREkWJV2D35Apt84xqI3PPsJIy7skUVsKQpmCUuW4Mj3xJpezJ3hTpIQsHIzs97Fh-_ZQiDFj5JNtWRKe6EhnxHoTHGs75SwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ds5FAyIy_05AaMJBGWzJAUtjCDlVHj750-DOOAQex6DJK9-1pkLNWmZgVHPbBf758zm2QM1gNoDf2glf7IiK4TG5DZJXeq2xAzMev2QMRJgS6JcOTEWoUGytMC8veSPK_eSM8B2ji4xhGtIrHpgRhAtC81chMDyKlf9Gj-_6F6t2zL51AGXW0UtJ7xAitw1SmyjydhEjVSePpq7UPzdBMAakbu3PWKmN_XwgrMSPZcF8XNJ3LbmUwBSJX6lB0EfO6yUhh8rWVbOtanKJnwyVY7JV8VACPsWz3Bd2b50N6zThc3dpwYIMMkkORPbNtRzqbgWI0glojYLqEWlWDPeoTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
إعلام حقل الأحدب في واسط: اندلاع حريق في أحواض النفط الخام وفرق الإطفاء تواصل عمليات الإخماد دون خسائر بشرية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86522" target="_blank">📅 15:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86521">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏إسبانيا: نحو 60 ألفا عبروا إلى سبتة حتى الآن</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86521" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86520">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f06fd1d40a.mp4?token=fqGxG1PiZBnHQTHiciDDrpJ7EG_05Z87OajAN59qLqD99tbkZD-8O1x0zfbAGeCDRUZ3khVN1DtuSfBal_Tgxsrm2dsFrLnWCnDvV2ODrKTcpIShunj6KeeyjOWForc2F01hqnmeSMlNgPBStjpuL0-x2rjNZIQm4pU6hA1E9RYb-C4yevifJhiY8p7L8EqGNwiULHVyYFGmLsU4-0-KQG0EnZYZQgr47z7oqppBeQBv3ajlcDtCBG2ZMxMPAK1xtPw_q9aeldk1wsqGZVVYKqsO68bQu_XODOFm7on5k7vaXdc6rh4s_Gq3vLjJpR6y1Euz5KFxFoBZZtUANKU3gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f06fd1d40a.mp4?token=fqGxG1PiZBnHQTHiciDDrpJ7EG_05Z87OajAN59qLqD99tbkZD-8O1x0zfbAGeCDRUZ3khVN1DtuSfBal_Tgxsrm2dsFrLnWCnDvV2ODrKTcpIShunj6KeeyjOWForc2F01hqnmeSMlNgPBStjpuL0-x2rjNZIQm4pU6hA1E9RYb-C4yevifJhiY8p7L8EqGNwiULHVyYFGmLsU4-0-KQG0EnZYZQgr47z7oqppBeQBv3ajlcDtCBG2ZMxMPAK1xtPw_q9aeldk1wsqGZVVYKqsO68bQu_XODOFm7on5k7vaXdc6rh4s_Gq3vLjJpR6y1Euz5KFxFoBZZtUANKU3gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من حقل الاحدب النفطي في محافظة واسط لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86520" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86519">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الكويت تعرضنا لهجمات من مسيرات  إيرانية منذ فجر اليوم</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86519" target="_blank">📅 14:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86518">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الكويت تعرضنا لهجمات من مسيرات  إيرانية منذ فجر اليوم</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86518" target="_blank">📅 14:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86517">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇱
خطف سلاح جندي وإطلاق النار على جنود في جيش الاحتلال الصهيوني</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86517" target="_blank">📅 13:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86516">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
🇮🇱
وزير الحرب الصهيوني كاتس:
إذا طلب ترامب منا فسننضم إلى هجوم على إيران.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86516" target="_blank">📅 13:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86515">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2a14531c6.mp4?token=bjSfog7m-LTLvxFZDh-CvI0iCRq6Hz5TGrldbMF0YjftRRHYXD7J22Me3XSwu1KsxKTcpU4zHmdm_UvH9-2b-FSNGl6_YHtSFO3ryshrAaGRnDcQM3Ecq26hbIpU7r3misBXv7k26nIsq7OE0dGBHnJTj9FmHMUetQsJ2hFGmGa_ImHUiEjwByhdFXHFfV1-awxg9QREP7yaX8d3ZiRsJ6TKo7XixvsW8CGNNkvXEdET93WKFeT0geTVbVnvq5wiSrmtCzj6kZU4g_8iwDo12kVeG_9greNFfjjk5mnE6zGyYcp1OeEAk54YbE_ScCI8BCsas1K9RT8W-mODYZzfhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2a14531c6.mp4?token=bjSfog7m-LTLvxFZDh-CvI0iCRq6Hz5TGrldbMF0YjftRRHYXD7J22Me3XSwu1KsxKTcpU4zHmdm_UvH9-2b-FSNGl6_YHtSFO3ryshrAaGRnDcQM3Ecq26hbIpU7r3misBXv7k26nIsq7OE0dGBHnJTj9FmHMUetQsJ2hFGmGa_ImHUiEjwByhdFXHFfV1-awxg9QREP7yaX8d3ZiRsJ6TKo7XixvsW8CGNNkvXEdET93WKFeT0geTVbVnvq5wiSrmtCzj6kZU4g_8iwDo12kVeG_9greNFfjjk5mnE6zGyYcp1OeEAk54YbE_ScCI8BCsas1K9RT8W-mODYZzfhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دخان حريق حقل الأحدب يغطي أجواء المناطق السكنية في محافظة واسط وسط دعوات للأجهزة المختصة بالتدخل العاجل لإخماده بأسرع وقت ممكن لما يشكله من مخاطر صحية على السكان</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86515" target="_blank">📅 13:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86513">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWjalXZzFPln8-3AMW0-44jpzc26y8v57SoiVcVgqzyTus4Qg70i72dCOp7cH1AsPi-IBDOXcpwSutp-TkxOy5h9TmE5CmFew9Z76qticGBuvPcDXMItakOb1kGQLrithvfpoXwz5h3EeljuJ1oN8Rbs2Ghsk51kEsUDRghDwg8ExH5zI7-CDe_WuTH7Z-OWxiT6CcKTp4zemJqugmF9LX4cbwHiuiPdgbEpCkoXg_VWorHBPHp2VBkr7oh2hQ3tnIUtrLAhMRZSdpsDJyeqsAOsT5ek-CM4_oUAKn9w2MB0mBc2lmifRlYck3cq-dL5K7IGSsGXkmCwbm0RVxJZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa393aaca.mp4?token=X8Djohpvp5D1X7mj0f-B5lVTq3aOiwu3cxMB2kNXEcKvbMK14oxlt8RXnYmNmh-bxb0uD1znaEhjr3AFiwk2TvP02iHMpDN1WhY8yztrMHNVgMbAJJwqNX_GmQfGFRHa5t8kCR4gVONLKuphxoBo916lAp4xacFPV3eZwrU1mtKunN2UrAD8nEi6csk7un-zYq8CHyox3FWnsrEvhS0NwjGasDrLmS6-8Ivcelz6cdNBojw5c7xTzArAPMb4L3cFT77CnTPLSlxBWlt49HsaMALL8oP4JcRdZlf_LIVdv2m_6CLkv3MefvZOunJXBLwx2fOfnzcg4_fCz8oncvdH6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa393aaca.mp4?token=X8Djohpvp5D1X7mj0f-B5lVTq3aOiwu3cxMB2kNXEcKvbMK14oxlt8RXnYmNmh-bxb0uD1znaEhjr3AFiwk2TvP02iHMpDN1WhY8yztrMHNVgMbAJJwqNX_GmQfGFRHa5t8kCR4gVONLKuphxoBo916lAp4xacFPV3eZwrU1mtKunN2UrAD8nEi6csk7un-zYq8CHyox3FWnsrEvhS0NwjGasDrLmS6-8Ivcelz6cdNBojw5c7xTzArAPMb4L3cFT77CnTPLSlxBWlt49HsaMALL8oP4JcRdZlf_LIVdv2m_6CLkv3MefvZOunJXBLwx2fOfnzcg4_fCz8oncvdH6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استنفار في محافظة واسط للسيطرة على حريق حقل الاحدب الضخم</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86513" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86512">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6401944253.mp4?token=YDocxVji8Wifs5DQMq43aDXZMmQv1aaCIJyU8B2Zd4KQfidGtXpp6DxkfRQd7MAB6ui6WLCiKsaniIsL8jV4i2hPEK6bPnWZ26fOjOdV95Q56NS4Nlx9Nxxicgxmj2hoTb2MhByT1JWbinE9fxkqsDP1b0wR7h1DBXX_v6RfAiCYLyia56MvkrVIYwlF61PQqbj0YPZe7gnPsLL_wo1GRDholKYhEBaHxUJC076h6f7z5r3CgtQ-Z13rfes4Y7YGlxxdlZ66z3OuP2ExqPn04NOBJlSkPb4ibViL0jm6bQNS5Jhxxc7lp3hnct7cretFpStkNmXm4SGNV5kuVJ5AoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6401944253.mp4?token=YDocxVji8Wifs5DQMq43aDXZMmQv1aaCIJyU8B2Zd4KQfidGtXpp6DxkfRQd7MAB6ui6WLCiKsaniIsL8jV4i2hPEK6bPnWZ26fOjOdV95Q56NS4Nlx9Nxxicgxmj2hoTb2MhByT1JWbinE9fxkqsDP1b0wR7h1DBXX_v6RfAiCYLyia56MvkrVIYwlF61PQqbj0YPZe7gnPsLL_wo1GRDholKYhEBaHxUJC076h6f7z5r3CgtQ-Z13rfes4Y7YGlxxdlZ66z3OuP2ExqPn04NOBJlSkPb4ibViL0jm6bQNS5Jhxxc7lp3hnct7cretFpStkNmXm4SGNV5kuVJ5AoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تواصل تصاعد اعمدة الدخان من حقل الاحدب النفطي في محافظة واسط العراقية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/86512" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86511">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b061325f8d.mp4?token=JHFrcMMuA-RUAVsB0qWJYtc5B04PNeBYkSKQyzjtGjKw6hr4hVQfTW8gljZtzW6pLX518S0fwXP8rIpBiosdaUZbHhj21VYlozEKKdE_5Y_LdDsUuQKkOCqNY7x2hfVAv2_55IOTjJqffcJPcpEuLmWpQZBoW6yHDCAXiccFqUEoZ2qSrfZTUMTU7kBq_3WJ5-mxCOhVhctuitWBpBqCQkL8YhnRUCnZfDSBrKdk4M3UBqKvQdNqbBsDgS-E8Bt98i8LJL2xn7nUn3ZnmiVbWKm3WOoVKAyyEN2pXL3xfZ1Y6mDw2DnrZQV3mQzMCK2sX5c-hBN2A82cxPpV-ncnOYpX5AkidfvmkCU_xXh8u_DumD65WVEcaYeQY7X76dDA-I34y2NFKDcUiqrBrqlexf8hP999skd2famoCvWdLLGBagKrg8KMoFuQdrdmRrwP1k57g4NbeHH4QEaNtqy0zJWQSJZvwxqNbihFW32ApUMyTRTLlDSWKznpSCUokurbF5OYtzS-KL0Ggn7qlvxvIS7EiVEHwQHC0MNtuCoDEqcpVfrhYSi3dTZswNMJHFtf5P0SVWIOKy-LmgC1dGUTOqOi4Tkiv7stQt-VBPKWek-U98-8xJ1J4340n4jA0PWX580LW94f4sl6wHij3DZexiiv1ugjO7fN588omjxhDro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b061325f8d.mp4?token=JHFrcMMuA-RUAVsB0qWJYtc5B04PNeBYkSKQyzjtGjKw6hr4hVQfTW8gljZtzW6pLX518S0fwXP8rIpBiosdaUZbHhj21VYlozEKKdE_5Y_LdDsUuQKkOCqNY7x2hfVAv2_55IOTjJqffcJPcpEuLmWpQZBoW6yHDCAXiccFqUEoZ2qSrfZTUMTU7kBq_3WJ5-mxCOhVhctuitWBpBqCQkL8YhnRUCnZfDSBrKdk4M3UBqKvQdNqbBsDgS-E8Bt98i8LJL2xn7nUn3ZnmiVbWKm3WOoVKAyyEN2pXL3xfZ1Y6mDw2DnrZQV3mQzMCK2sX5c-hBN2A82cxPpV-ncnOYpX5AkidfvmkCU_xXh8u_DumD65WVEcaYeQY7X76dDA-I34y2NFKDcUiqrBrqlexf8hP999skd2famoCvWdLLGBagKrg8KMoFuQdrdmRrwP1k57g4NbeHH4QEaNtqy0zJWQSJZvwxqNbihFW32ApUMyTRTLlDSWKznpSCUokurbF5OYtzS-KL0Ggn7qlvxvIS7EiVEHwQHC0MNtuCoDEqcpVfrhYSi3dTZswNMJHFtf5P0SVWIOKy-LmgC1dGUTOqOi4Tkiv7stQt-VBPKWek-U98-8xJ1J4340n4jA0PWX580LW94f4sl6wHij3DZexiiv1ugjO7fN588omjxhDro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من حقل الاحدب في محافظة واسط</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/86511" target="_blank">📅 13:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86510">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حريق كبير في حقل الاحدب النفطي العراقي لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/86510" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86509">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa78545065.mp4?token=e_olnc0y0dYuYlBvITgMpnGvxNisSi1s1ooKqk_I9kwjg3RwIU15VimaBnG74ZIj3mWhjhD797k8fmTposl9T0sruQhLMT5O0lifaStFH9OIfuV8Tm6Da9pua7K6CCiZTU2c6gEl9grftIoo0oGcA4yeRsVv3bHYRL04ZGvKeK64MbhZsIqKihI9rMBIXyFUqqdvAuDUTtfZIwLNgD5ptFMBZqXAMNX2Q0j45aQC2JARHV9i1DKPw1c5qriMxznpHg_Prkzt23dVelx2t_LABo6gVQtJR8Qwhtwnrr8en-8sXjq3HWbreS-G6JmFkGZ5BEhagtuLeBCGM6RzndEivw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa78545065.mp4?token=e_olnc0y0dYuYlBvITgMpnGvxNisSi1s1ooKqk_I9kwjg3RwIU15VimaBnG74ZIj3mWhjhD797k8fmTposl9T0sruQhLMT5O0lifaStFH9OIfuV8Tm6Da9pua7K6CCiZTU2c6gEl9grftIoo0oGcA4yeRsVv3bHYRL04ZGvKeK64MbhZsIqKihI9rMBIXyFUqqdvAuDUTtfZIwLNgD5ptFMBZqXAMNX2Q0j45aQC2JARHV9i1DKPw1c5qriMxznpHg_Prkzt23dVelx2t_LABo6gVQtJR8Qwhtwnrr8en-8sXjq3HWbreS-G6JmFkGZ5BEhagtuLeBCGM6RzndEivw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من حقل الاحدب النفطي</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86509" target="_blank">📅 13:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86508">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbdadf0ac1.mp4?token=Gy3JJIrNxB4jBmZRCoX16WCqZlcyHQxoSGEQThfjf3chWM8rdksofwJuMAWxQQtwK_FyhS-B5NdH7Cci5ga0DUTBMYPfE8CA2PcXyosb1H570KGz5pqlJnG2DE2tQtyZeK_yVGQqY01xXKfaCVCtVJoGHciJhCw0jUP5y_uWNrSOJvD_FaTHDxTcaOgwgbD3qiKS9o1TQi71EeipQwxxGZvxJA8flAeTtyASStHSaIAIGaEGvcRQFOnz2MD4bdcWVJqBXAHK1mCj8iYq9_9OEq-AYHOR0jAd354Hzuau-_W0FJvMSnQOsr1HOjDq_zObS6HvqUeyFHmynBb-MLJUBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbdadf0ac1.mp4?token=Gy3JJIrNxB4jBmZRCoX16WCqZlcyHQxoSGEQThfjf3chWM8rdksofwJuMAWxQQtwK_FyhS-B5NdH7Cci5ga0DUTBMYPfE8CA2PcXyosb1H570KGz5pqlJnG2DE2tQtyZeK_yVGQqY01xXKfaCVCtVJoGHciJhCw0jUP5y_uWNrSOJvD_FaTHDxTcaOgwgbD3qiKS9o1TQi71EeipQwxxGZvxJA8flAeTtyASStHSaIAIGaEGvcRQFOnz2MD4bdcWVJqBXAHK1mCj8iYq9_9OEq-AYHOR0jAd354Hzuau-_W0FJvMSnQOsr1HOjDq_zObS6HvqUeyFHmynBb-MLJUBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من تصاعد اعمدة الدخان من حقل الاحدب النفطي في محافظة واسط.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/86508" target="_blank">📅 13:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86507">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5549b21f6.mp4?token=O7SpnSdTuE7LFhqAEa9Z9zE1mmlUUZLZ6OxI3rwYwknek2Kk6XDu69Y9oGUDzwyQkm80Yspcvsn9CFUbbhlVCEh07vvC2VirhnoU-EO-F7nNpGPs_hI1Dia73Ua1wvQDaeVjS5TLfJLIG5sFQTXiEtC9mQJ9i9TJznmRdM22iD4XLHX8ODejndSV0NLrRfRhYRbdGtGadPNm-7_yIPaoXLZ6CUZLQqW_lZXIQlqOGXOAOdAG6nb2NkjViD7ta11AP7otWNxIGbfUNjmxwU2LK1S-jkJBj0r2vRFpQCo05NnmIsIaNpO4aFmJh83nVVpjOrDilUUiHzKCnJq7v7dj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5549b21f6.mp4?token=O7SpnSdTuE7LFhqAEa9Z9zE1mmlUUZLZ6OxI3rwYwknek2Kk6XDu69Y9oGUDzwyQkm80Yspcvsn9CFUbbhlVCEh07vvC2VirhnoU-EO-F7nNpGPs_hI1Dia73Ua1wvQDaeVjS5TLfJLIG5sFQTXiEtC9mQJ9i9TJznmRdM22iD4XLHX8ODejndSV0NLrRfRhYRbdGtGadPNm-7_yIPaoXLZ6CUZLQqW_lZXIQlqOGXOAOdAG6nb2NkjViD7ta11AP7otWNxIGbfUNjmxwU2LK1S-jkJBj0r2vRFpQCo05NnmIsIaNpO4aFmJh83nVVpjOrDilUUiHzKCnJq7v7dj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
خاص لنايا | تصاعد اعمدة الدخان من حقل الاحدب النفطي العراقي في محافظة واسط لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/86507" target="_blank">📅 13:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86506">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IV2r7gdDXrUxTGDiWEFnXajT49imo4wytVl-QMBqpzfyyo1AOGG5ux-SllpkSiiEF-IMGlU1FExhUd9sB3g2m8uHux5E5R2dGxxuWU31oMMlKeaPvYZj6gO5dJyqrraNl7D7-A2iCqBWgB7Zaenno-we6KCedTAyzNWLMCK5EthcA8sicHFBN2vhKRDVcwNc0VxLb61Jbr2keDH5g10jKCnN3nnCrow9ualCCtt2g4j6aE9CAFEAA5c4zOP1o0mNQFeE9fEJJjPGuQFjxjaWoIBn5DO0uRxmPpBbb0JTu4N_uxyhFBnD2X-wfFC3ejlwi3A4XH00hVSMDTL5Bs0dOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من حقل الاحدب النفطي في محافظة واسط لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/86506" target="_blank">📅 12:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86505">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMr-7H7wD3-gtZy27fshU6udtv1qggYlDiRkesRg-I8KTqpN3GKgG-mtJ_E2BqlY6-tdop9aim1pEL3OpqHnh_nfZOXBLt9ey2lRJ_TV1FKDhYONA8zsRTLHEfKCbP_wKwQfP1gc8YU4XpzSlUjAOo-6Il4x3E69r03fXbF9CsBxLnpdhXHsFPAyIHlXnPTQA-6GZ0-NXvDSDH6opmXv7RTGB-bSzZRX4QzS5-EK9kzsh0hqFypLzJBpY4QAzbTUrIeqkyN1DcshFhDG7-AusiI3rAYr5o_ipTa-dXbb20ljh878rd2rjw6Vo72z3km9ZDlki0v06lgjdQ29n_92iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من حقل الاحدب النفطي في محافظة واسط لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/86505" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86504">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e9b717dc1.mp4?token=BgS6nJhY4AFDEH1jXamjeS3cPLU_gJnmYKahiBZo459LlIJ6p8yEIL2kXHyvUkirFHIMIxAg5OzrSKSRmfAfR2sHl_i2pud5HQqxT4Xs4fiBOIkdd677jO87dPFHzJswBM7IHvSR6QfBljoAzGvel-x-6gLiqFGQv6lyt2fTqx-_GNR46XGOi16AjdHjZ2ONYT2FyrgzXoYYrbZsIfl_1CNuNFfJF6rqTIp7iqRDeqTslyj-K29NH8YikzBNnHjAN4Hzv5jDPALWS39MUagVUeVDUPf5q4z9GvVVgiFLkI_NanSxJi-NZx5m1IhFlu6VjXD955wSYDl0qyJdpCEpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e9b717dc1.mp4?token=BgS6nJhY4AFDEH1jXamjeS3cPLU_gJnmYKahiBZo459LlIJ6p8yEIL2kXHyvUkirFHIMIxAg5OzrSKSRmfAfR2sHl_i2pud5HQqxT4Xs4fiBOIkdd677jO87dPFHzJswBM7IHvSR6QfBljoAzGvel-x-6gLiqFGQv6lyt2fTqx-_GNR46XGOi16AjdHjZ2ONYT2FyrgzXoYYrbZsIfl_1CNuNFfJF6rqTIp7iqRDeqTslyj-K29NH8YikzBNnHjAN4Hzv5jDPALWS39MUagVUeVDUPf5q4z9GvVVgiFLkI_NanSxJi-NZx5m1IhFlu6VjXD955wSYDl0qyJdpCEpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حرس الثورة الاسلامية
:
في الساعات الأولى من اليوم، تعرضت سفينتان نفطيتان متورطتان، وتحت تأثير التضليل الذي تمارسه القيادة المركزية الأمريكية، ظنًا منهما أنهما يمكن أن تتحركا في مسار غير معلن تحت حراسة جوية للجيش الأمريكي "الطفل القاتل" والإرهابي، دون الانتباه إلى تحذيراتنا، وتعرضتا للقصف وتوقفتا، بينما غيرت 4 سفن نفطية أخرى مسارها بسرعة وعادت إلى مواقعها.
في الليلة الماضية، ردًا على بيان القيادة المركزية الأمريكية الزائف، أبلغنا جميع مالكي شركات الشحن والتأمين بألا ينتبهوا إلى إعلانات القيادة المركزية الأمريكية، وأن يسألوا أولئك الذين وقعوا ضحية التضليل وتعرضوا لحوادث.
تكرر القوات البحرية التابعة للحرس تحذيرها: أي تدخلات وأوامر ونواهي غير قانونية من قبل الجيش الأمريكي "الطفل القاتل" لن تمر دون رد على السفن في المنطقة.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86504" target="_blank">📅 12:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86503">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇱
حدث أمني قرب مستوطنة ميتساد يهودا في الكيان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86503" target="_blank">📅 12:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86502">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇱
حدث أمني قرب مستوطنة ميتساد يهودا في الكيان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86502" target="_blank">📅 12:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86501">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">أنباء عن سماع دوي انفجارات في مضيق هرمز</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86501" target="_blank">📅 12:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86500">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مشاهد من إطلاق صواريخ إيرانية باتجاه معاقل الاحتلال الأمريكي في المنطقة</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86500" target="_blank">📅 10:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86499">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKnOBopLSzYyRpZYBThqI2ytMxFg8_NZnGscxmeRU-tRbjm-wQvT4xFoZjWkarUBFDh9C4btELwH5PCYca4wsVc7o61_qFaD5ZO4eTsYdnbgarVkzk_dnAKpxsnCiPgJ3_mrNQ7OrPZXrg1DTtlrSHIeQtL4EnLF3-puGFKoJiGZj19AHGK7VqIAcwxn9Hp9nw_f1S2Mrt1dcdzCtrusL98JfzQul1C3G54bHHUxgEo8dv11m3nJUB4XqcV-SazBBbEdNrCGTqWiprht9XYTRwkEqSSFL_8PBkPwzTtmDeu6uXfeX1LXk6DhPKaqCdLCyzVZ6hhAI1wuT-c8ghpBUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إطلاق من ايران</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86499" target="_blank">📅 10:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86498">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688082acb0.mp4?token=WfezBglCYDRzQVXqn2vsv1esT3npphBI72iCvJalw9JfUN9jtKSNiJCbUeHVw-SKe0_YbpOjqqxWV7Oo4Mu8aIQiKdd9mWToqBrq_oHjcVToDAcyW-tVcW9eTYnyH_HspYsJJ60UW3JydZu6izR3ajrVZjzQDsun3x_RVw1KqFqQ1mB-KTU_mCxCfO8zw3R_-TGdV_JDblrPXa1ocJfangfRf72YTpTf5grT7EdHxfQ6reYC2QtbYv1UvVYJbX_ZduM0Y9O3ypV2GppkR0YT1iDVtyHkG9XtMUpNheEk5V3OUBe4zp2Dyhw5IOrBNYLO77BnMFQvq3E7jO2EJD4abg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688082acb0.mp4?token=WfezBglCYDRzQVXqn2vsv1esT3npphBI72iCvJalw9JfUN9jtKSNiJCbUeHVw-SKe0_YbpOjqqxWV7Oo4Mu8aIQiKdd9mWToqBrq_oHjcVToDAcyW-tVcW9eTYnyH_HspYsJJ60UW3JydZu6izR3ajrVZjzQDsun3x_RVw1KqFqQ1mB-KTU_mCxCfO8zw3R_-TGdV_JDblrPXa1ocJfangfRf72YTpTf5grT7EdHxfQ6reYC2QtbYv1UvVYJbX_ZduM0Y9O3ypV2GppkR0YT1iDVtyHkG9XtMUpNheEk5V3OUBe4zp2Dyhw5IOrBNYLO77BnMFQvq3E7jO2EJD4abg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق من ايران</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86498" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86497">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
رويترز: طائرة مسيرة تستهدف معسكراً لحزب المعارضة الإيراني الإرهابي شرقي أربيل.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86497" target="_blank">📅 10:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86496">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b76d3d31.mp4?token=QwYB15uXrErbLXv_N2_bq0GhyUDCGCIpvHYPxW0S9U50_TXQLf01AwXGXrwpQumcbCN6iYMxDvfj3wndzfrXhSvn1cmzRWhS2MTe37wVrDkdbXRXDGqotyE59XI9p8DCIZqiv6Pty4TeFX0T3GtR3luA_yoqiDboZLyXS39oQs3ExWSSbRrLaU9SL0kL-_BrYtfyrA0h93TUIuHH0PRBjTcKX9_RWqAJQCXS3sN6cnLvGKMyzJK0QcT_AcArwTz1BpdmZQuQfKw2E4T4XSGlmI4CMP8brYneg7Tm7RnuQr3vt7RqUgJcRFFiWsm5-KNFI7VORMX6tr3815AUvHUgsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b76d3d31.mp4?token=QwYB15uXrErbLXv_N2_bq0GhyUDCGCIpvHYPxW0S9U50_TXQLf01AwXGXrwpQumcbCN6iYMxDvfj3wndzfrXhSvn1cmzRWhS2MTe37wVrDkdbXRXDGqotyE59XI9p8DCIZqiv6Pty4TeFX0T3GtR3luA_yoqiDboZLyXS39oQs3ExWSSbRrLaU9SL0kL-_BrYtfyrA0h93TUIuHH0PRBjTcKX9_RWqAJQCXS3sN6cnLvGKMyzJK0QcT_AcArwTz1BpdmZQuQfKw2E4T4XSGlmI4CMP8brYneg7Tm7RnuQr3vt7RqUgJcRFFiWsm5-KNFI7VORMX6tr3815AUvHUgsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
تشييع المستشارين الإيرانيين من منفذ زرباطية الحدودي ؛ المستشارين ارتقوا نتيجة الضربة الجوية الأمريكية على العراق في وقت سابق</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86496" target="_blank">📅 10:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86493">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vc2C_pAPgr4Ikr5YaWmai3l602OyKvDy-6TeuaKcHwVuZZENVY41zfNN8ToZxyLH5An2NSj8x9sQyprylGGnxkgf6Z6jpYOWeyTq03ufkW5jhqsZjyZKb7VLbbWDe_vz6P-nBNXFU2-xo0ErQNTXs20QTxkSW1rMWMpFhmgTfizjUTMX6pTi1F9-avh0XdZZU3VkuC9qGgIHGazAhlJrT6gD6IL-55xno0BcknDLa6OGvFlc-f2KUTJge-ldQiVzui3aL3vJrEzKUrd5H7eqVtY1YfzfjiFockNHRFgET2SesG4lqzHoqm_mVBO-TiKkljPEcOt7gi_DLDtys6golw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWwllgSMPyhodVV10UvQTkiLnYGeU7aMv8puARLIrDafnqnzQ6hhmAzeEd8oC4aFtFp0sA3XP1qEKceQRxiRN6azLbX6LjAP7koAxNLoYX7Cexlcqxq0LbQuEzmSODhAVUMPxBgkZaf9OzakjL4SN9X0nWW5FuI2LIebSvBP49iUf8qu9gIyySmUouOiBDE5v_uSpGVQd-dQGjn5k-G8zZKMSmVtJidUCSaG_Cauw63kx3hwEmSkyxYxsUU8H02piRzH2VIGuDXdMWtFq9u6qC_P5HFibv5gYJhr2nBIhefgoabfiqlX0JMSpuNBbFyHY1xw19FXDYQPSkrq5qd5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJTPEac7BroiZLOkE_OZjnSgdebjGIZx3ZK4Je0cSHJM7oD_MPfVibhJrtfv0fp55ialprntcdY25w-7GiL0eUywYNdBU3T7LmHPJvGS7AHMAkIWiJRZb174dSqInhuXxUgQI_s2YBoPLYX50hJSNAZ9I4PfVr94dZL8-nKyALEF_lpTAv61N47jNQaDDKODKvPSpGn1SwXSbuC0E7Gj2_KSGT48kvEwC9pz3Ga-9PVjuJ0LZ8Ipevm6hSSZOzlDNrcgO0UOVslxVVsumX27aKtAUlFjadN4zTfSJ6LKOM86EYpALUBbgrc6926XT91Dd31zfIN7_VpM6ENKSA9hVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇶
تشييع المستشارين الإيرانيين من منفذ زرباطية الحدودي ؛ المستشارين ارتقوا نتيجة الضربة الجوية الأمريكية على العراق في وقت سابق</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86493" target="_blank">📅 10:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86492">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔻
🇮🇶
هزة أرضية جديدة الآن شعر بها أهالي محافظة كركوك شمال العراق ؛ حيث تعد الهزة الثالثة التي تضرب المحافظة منذ ساعات الصباح الأولى.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86492" target="_blank">📅 09:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86491">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81cba719d5.mp4?token=KMTt0FIBlnrwWgg3qulApoZpvkHsSXGW9ilx676sqVGWtzevN7mPLiedTZTYekjGkdfdwXUd_YmlRGpF5CSeb3-z75tHZEu8PA8vqJSK23lB57zlQ1C1Vg7lYKRlcZEymgNENtOxNtwv_pciH969bVyYl0qtq5vm8FW26GehFmJDLPGTKAwTqU5qfB3JRPw1h-cVQfAnIMUDi5iByivQUHp19tGXrBe_pn8XYIx2kJ9XJGWO7nRFxfmdr_yeoxEWOHljmQZA4kMMp9IfP-tDnjb9mFeAuvxxIfHc1JmRJYWMu0PfJArfrxNEqC-6fEAiSpr8cyVt-fF401JQ1MKIAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81cba719d5.mp4?token=KMTt0FIBlnrwWgg3qulApoZpvkHsSXGW9ilx676sqVGWtzevN7mPLiedTZTYekjGkdfdwXUd_YmlRGpF5CSeb3-z75tHZEu8PA8vqJSK23lB57zlQ1C1Vg7lYKRlcZEymgNENtOxNtwv_pciH969bVyYl0qtq5vm8FW26GehFmJDLPGTKAwTqU5qfB3JRPw1h-cVQfAnIMUDi5iByivQUHp19tGXrBe_pn8XYIx2kJ9XJGWO7nRFxfmdr_yeoxEWOHljmQZA4kMMp9IfP-tDnjb9mFeAuvxxIfHc1JmRJYWMu0PfJArfrxNEqC-6fEAiSpr8cyVt-fF401JQ1MKIAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
في المرحلة السابعة والعشرين من عملية "صاعقة"، وردًا على التعديات الأخيرة التي ارتكبها الجيش الأمريكي الإرهابي ضد بلدنا، والهجوم الوحشي على منزل سكني في جزيرة قشم، استهدفت، قبل ساعات، "مواقع طائرات مقاتلة"، و"أنظمة اتصالات الأقمار الصناعية"، و"مخازن المعدات" لهذا الجيش القاتل، في قاعدة أحمد الجابر في الكويت، بواسطة طائرات مسيرة تابعة للجيش.
تلعب قاعدة أحمد الجابر في الكويت دورًا رئيسيًا في العمليات الجوية والمراقبة الأمريكية، وتعتبر، بالإضافة إلى دورها العملياتي، مركزًا حيويًا للدعم الجوي للجيش الأمريكي الإرهابي.
الجرائم والعقوبات والتهديدات تجعل إيران أكثر تماسكًا وتوحدًا في دفاعها المقدس.
الهجمات الحاسمة والواسعة والنادرة التي يشنها الجيش والحرس الثوري الإيراني تجعل اعتراض طائرات مسيرة وصواريخ إيران مكلفًا وصعبًا للغاية بالنسبة للعدو، على الرغم من استخدام أحدث أنظمة الدفاع وتطويرها، ويضطر العدو الخبيث إلى استخدام الرقابة الشديدة لمنع نشر أخبار الأضرار والقتلى والجرحى.
﻿</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86491" target="_blank">📅 07:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86490">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f829242f02.mp4?token=Qyo7GhCJ8sFYElBG-1xspgRlA2sm2DTfOy38hyRvR79cKy24TxHI1Qfyfm6eohpm2SRXdgSu5cJbza8KZ10N6dTPKQjVeFtyT6qgxD60WLovtQf8zMP5F8KGrGY-Zos5qYaetQGHHfnrI6OlUc7ujW6smCU5iLlEj8VXMGlxcdWkULyWar75PkLw5e_Lx67I-dbJSvzpYy2AgUQYndJR7VfyxUO21_K1_RhklFG1hZayYYCkNEaub4tSAqzNxEo3kj5wk0vt8ex2R3sghNBjBAXqZP-5SCzjf3tnwzGFTiXVzVMTWIR-fGubzXT2MgXAJAieZeATnnmvFTcn46AB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f829242f02.mp4?token=Qyo7GhCJ8sFYElBG-1xspgRlA2sm2DTfOy38hyRvR79cKy24TxHI1Qfyfm6eohpm2SRXdgSu5cJbza8KZ10N6dTPKQjVeFtyT6qgxD60WLovtQf8zMP5F8KGrGY-Zos5qYaetQGHHfnrI6OlUc7ujW6smCU5iLlEj8VXMGlxcdWkULyWar75PkLw5e_Lx67I-dbJSvzpYy2AgUQYndJR7VfyxUO21_K1_RhklFG1hZayYYCkNEaub4tSAqzNxEo3kj5wk0vt8ex2R3sghNBjBAXqZP-5SCzjf3tnwzGFTiXVzVMTWIR-fGubzXT2MgXAJAieZeATnnmvFTcn46AB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مسير انتحاري يدك مقرات الانفصاليين في محافظة دهوك شمالي العراق.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86490" target="_blank">📅 05:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86489">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933e01f5b0.mp4?token=TAoaNwIlOTQM-3VGuYHAaluQSszWY22xeloTyRORnFePp3UsbmCDOKZvsG4Y-PXkp5Sn2w2Xjejn01NCwYGqDUf44h0TH-d1HFzcrrH5KjyXbQ7saN0dF5mR0r_IBTdPFnX9tmgMrFIYszVk3ZB6vY2GM9PyO0uFN1ne91S9s2u6wTDPTiTRu-xUPqz22sMoqnXnx2wlZcv33LbUpSnwB0UM-OvcBBmFxuhXXMVXjbyVB0Z9AKRDcOKGhv9kyA8chgxFST8g8qPPx9nHcMi4Nmyt-O_VZDIlcVYakysCUMbjrethKpbZO_moo83ojz8Xhn4sVJ-oSfnjee9FIq5d3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933e01f5b0.mp4?token=TAoaNwIlOTQM-3VGuYHAaluQSszWY22xeloTyRORnFePp3UsbmCDOKZvsG4Y-PXkp5Sn2w2Xjejn01NCwYGqDUf44h0TH-d1HFzcrrH5KjyXbQ7saN0dF5mR0r_IBTdPFnX9tmgMrFIYszVk3ZB6vY2GM9PyO0uFN1ne91S9s2u6wTDPTiTRu-xUPqz22sMoqnXnx2wlZcv33LbUpSnwB0UM-OvcBBmFxuhXXMVXjbyVB0Z9AKRDcOKGhv9kyA8chgxFST8g8qPPx9nHcMi4Nmyt-O_VZDIlcVYakysCUMbjrethKpbZO_moo83ojz8Xhn4sVJ-oSfnjee9FIq5d3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز محافظة دهوك</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86489" target="_blank">📅 05:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86488">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات تهز محافظة دهوك</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86488" target="_blank">📅 05:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86487">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbe150fb6.mp4?token=fa6LtstF19yPPXyb6Q88YPPSMbcZwWev3FtFhX9HM88aOsNTZ8YBxLKF1RF7TmWvMi8OAyCBu08l26c4rww8o-yaUH13HJc4br3N33hdujcn4lvZO3iG5AmFFpHidQaawDR5rpS-ZVJIwvimSH5UZGAOEdgRLANDLdohg4ZDEgPLc9McIy8fejM_poQDrG5mkAlqDsqUpZeHY85TS3D1Abe7hy0LOOTUpYRATUWdSuNfGmM2Woy0LNyVcl4GXI827YTVEixiaXDoZxJIGBJciTydzwIz4rG9azMON6mHSzIO302ouAOEkhjKkzTx2LdRJz5tXNtQevSLL0dOG37hiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbe150fb6.mp4?token=fa6LtstF19yPPXyb6Q88YPPSMbcZwWev3FtFhX9HM88aOsNTZ8YBxLKF1RF7TmWvMi8OAyCBu08l26c4rww8o-yaUH13HJc4br3N33hdujcn4lvZO3iG5AmFFpHidQaawDR5rpS-ZVJIwvimSH5UZGAOEdgRLANDLdohg4ZDEgPLc9McIy8fejM_poQDrG5mkAlqDsqUpZeHY85TS3D1Abe7hy0LOOTUpYRATUWdSuNfGmM2Woy0LNyVcl4GXI827YTVEixiaXDoZxJIGBJciTydzwIz4rG9azMON6mHSzIO302ouAOEkhjKkzTx2LdRJz5tXNtQevSLL0dOG37hiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق أخر للهجوم الواسع بواسطة المسيرات الإنقضاضية على مقرات الإنفصاليين في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86487" target="_blank">📅 04:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86486">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c6755af0.mp4?token=tzKpVpL6DRnBXDr8JJURW5qUPjuK6QTVcpVzs2xT1hccbG8s30BeZ2zQLU6xcGYDwWpbUsP9t8jxRl-ezaIsgfOwToWlnmP2-RpUwyGpCfROQKh_1y1D0eaylhN7Yk35fOzzc2tC2dfCxQB9hZGuFELxh8PnD18vq_EFC4Fu1-4FFpxchcPKn0Kf0WpEnt_5F-5-UaQqfxn8dcLej5vyQ5sd7inm5Hm-n_6UwiIdOxUbRQLMHIO_wd6N2-ZxSlUnqMYO0PI7WEL2RjBmh3PNDrOjCULQd2WL8uB66Wlzc6WatDUZsJS824lQSo-lEbe6Aj1zmmn7sGutWbS37OatkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c6755af0.mp4?token=tzKpVpL6DRnBXDr8JJURW5qUPjuK6QTVcpVzs2xT1hccbG8s30BeZ2zQLU6xcGYDwWpbUsP9t8jxRl-ezaIsgfOwToWlnmP2-RpUwyGpCfROQKh_1y1D0eaylhN7Yk35fOzzc2tC2dfCxQB9hZGuFELxh8PnD18vq_EFC4Fu1-4FFpxchcPKn0Kf0WpEnt_5F-5-UaQqfxn8dcLej5vyQ5sd7inm5Hm-n_6UwiIdOxUbRQLMHIO_wd6N2-ZxSlUnqMYO0PI7WEL2RjBmh3PNDrOjCULQd2WL8uB66Wlzc6WatDUZsJS824lQSo-lEbe6Aj1zmmn7sGutWbS37OatkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين: البنتاغون قلص وجوده بالكويت ردا على هجمات إيران على قواعد أمريكية للحد من المخاطر.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86486" target="_blank">📅 04:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86485">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين: البنتاغون قلص وجوده بالكويت ردا على هجمات إيران على قواعد أمريكية للحد من المخاطر.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86485" target="_blank">📅 04:25 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
