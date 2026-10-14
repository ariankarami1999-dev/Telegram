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
<img src="https://cdn4.telesco.pe/file/XNQpF321Brf93FP0JcU_1DT4XP7IK7axkkFH_cnIrEH5YdpwOsGl83GdPVpTytNV4dnHwfC9POJUbkA5ANVMPZeSOJqo4vu5Nss98kljK9K-KjFm8Kgj05o1PUZAVbczvusd95IAqd8yq8ioL7quZ2daTT8su9XPpAn4ibYArA7jbUae7bapydSiwIHfVTV9_TEgeielgG6ZAx_PWScqjn9uPM7JJMuz2utu01Huk-AkjFndtwA9WSKObWbsh2UgIWX2UBsU7idJdKGvDL697yTDEMwjKri7orB4uv7XgUFKgN0afqPhKin7lntqm4BJd1lnTwsUQTto75Oeu2v17Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-23 01:19:55</div>
<hr>

<div class="tg-post" id="msg-93719">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">القوات اليمنية المسلحة:تمكنت قواتنا المسلحة بفضل الله قبل قليل من استهداف طائرة حربية سعودية نوع "تايفون" أقلعت من قاعدة الطائف وتم استهدافها في أجواء محافظة صعدة بصاروخ أرض جو وتمت إصابتها إصابة مباشرة وهي معرضة للسقوط.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/naya_foriraq/93719" target="_blank">📅 00:45 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93718">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38dce1b295.mp4?token=uvtBDTueKcdxf1dJF1jd-6gr0hrpUncMfYzVrfWyqFE_La5bgcb79lfRIqGPQSxnIvr4rNWbUcU10XisxdK4Lc0zkKQTQYERNpO-U3OJp9m1DYJO0OVzQ_LtaVJDpN3ZtODlh0grC7YR7OCXTCV97LXhEyNc9-uN2okw1XSz8i5HDs4GZ_c_7jMIpZNvwlGCB1IkXMng4LmqHq1pWdmNNDk8irrw1vQvcOvi5r96giZExUzXPMdp2V_9B3Y-KksJLUOMI9EDSFnYBToW3AtlKSzWykr2pcBPL78EkqOIWbFz91siIo9w-Iq-lDA0QskrqomrTR_BE5yWRC9ax4AFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38dce1b295.mp4?token=uvtBDTueKcdxf1dJF1jd-6gr0hrpUncMfYzVrfWyqFE_La5bgcb79lfRIqGPQSxnIvr4rNWbUcU10XisxdK4Lc0zkKQTQYERNpO-U3OJp9m1DYJO0OVzQ_LtaVJDpN3ZtODlh0grC7YR7OCXTCV97LXhEyNc9-uN2okw1XSz8i5HDs4GZ_c_7jMIpZNvwlGCB1IkXMng4LmqHq1pWdmNNDk8irrw1vQvcOvi5r96giZExUzXPMdp2V_9B3Y-KksJLUOMI9EDSFnYBToW3AtlKSzWykr2pcBPL78EkqOIWbFz91siIo9w-Iq-lDA0QskrqomrTR_BE5yWRC9ax4AFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: إيران ستضرب الساحل الغربي للولايات المتحدة بسلاح نووي لو كانت تمتلكه، لأن قادتها "مجانين".</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/naya_foriraq/93718" target="_blank">📅 00:42 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93717">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8bcfa291.mp4?token=FLKnQ1EnwvdfAtAdcnxeKw7BXczgaetZ88DAOk4MqxpsLSLiVMBnVL3SgLpVlpRVI-X3ujX6D6OeDH7P-Qxj7rjhmId_lcBONJn0H3vvImIRnXWs_YMaXyc6Dl2tGiwUiiCdu8cE-YJJwmLM9tg6mSHsuDS6dYZ3xz52nTJzNoJjYkFcl0tOdDsJ8TRj1T2Lzeq3eMELfUc1Bo56JfmRMPyAXZh6mwuNqygKdVgsSTA2J-HIJiGtzoAmhhYcorK9l380Tn2rkXFI4eq7-p7rs92s40OjpD6ycK3J3d-NlGkMjiMbmTfAud8LbKAoHaKMddf-n6NlwVDgRrzRyV1brQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8bcfa291.mp4?token=FLKnQ1EnwvdfAtAdcnxeKw7BXczgaetZ88DAOk4MqxpsLSLiVMBnVL3SgLpVlpRVI-X3ujX6D6OeDH7P-Qxj7rjhmId_lcBONJn0H3vvImIRnXWs_YMaXyc6Dl2tGiwUiiCdu8cE-YJJwmLM9tg6mSHsuDS6dYZ3xz52nTJzNoJjYkFcl0tOdDsJ8TRj1T2Lzeq3eMELfUc1Bo56JfmRMPyAXZh6mwuNqygKdVgsSTA2J-HIJiGtzoAmhhYcorK9l380Tn2rkXFI4eq7-p7rs92s40OjpD6ycK3J3d-NlGkMjiMbmTfAud8LbKAoHaKMddf-n6NlwVDgRrzRyV1brQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: إيران ستضرب الساحل الغربي للولايات المتحدة بسلاح نووي لو كانت تمتلكه، لأن قادتها "مجانين".</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/naya_foriraq/93717" target="_blank">📅 00:36 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93716">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50e1597ca.mp4?token=qRw4qzFfXe-kGWmAoAPJvZfAmspKO19cCMpInYBp8dNsx9Q2zwLzW-RqdnDuH3usn2I1ubmKQINww0NvfUtLjVZEjNG83zsDXZQQBLZzxxQouqwj5bLij68ksfynrcacUKFwTTsKz6BVjRa6L7IRluxHxvAJlua-RYRSz8RQLUcg45z5YtRIx8o2WCvDu38xE8V0jxRPP4POQQJEQB_kBvs-UsJuRuKniS5dbGdxppai8Xo7hT-04bOxJNVVohoO-TFWf7lesReIWuT5wvWSQ3R3qAppUSjHVlb5mP1HlgXGwryS0_mV859tRgFO1QQIv_RX3cx0UBVXnA3fwhIt4CWaFMxd4KBTqOHD_T1DUjlOSfjIFHXjjRdBFzFWvFJIJPrtDtgruDDzFfIoF_mewLNLc8e-cMTzZlL4C7SEnrpb7q_tv2Yrmhavq5O5mJevvln4B3jyne8i2jLMlo-p4cmJ5kE6qL06URRkZvBahPOk-WM8pfbVqTAKIlX0PjMgNI7aMHC1NZrESZtkRshTiX4CyNrIwv8qA3Xq5cM_jAHzfVN2jNUscw1NP59UwH0-PGghALvUVepzgflkJQnTkS-YAgap0D2ZxMBYddbeniK3_i3v0490i6vRkcpdwOvJsMlFGGoCxma8Z-kFGzqP2YacLVNAxntWrBNemWSLWNY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50e1597ca.mp4?token=qRw4qzFfXe-kGWmAoAPJvZfAmspKO19cCMpInYBp8dNsx9Q2zwLzW-RqdnDuH3usn2I1ubmKQINww0NvfUtLjVZEjNG83zsDXZQQBLZzxxQouqwj5bLij68ksfynrcacUKFwTTsKz6BVjRa6L7IRluxHxvAJlua-RYRSz8RQLUcg45z5YtRIx8o2WCvDu38xE8V0jxRPP4POQQJEQB_kBvs-UsJuRuKniS5dbGdxppai8Xo7hT-04bOxJNVVohoO-TFWf7lesReIWuT5wvWSQ3R3qAppUSjHVlb5mP1HlgXGwryS0_mV859tRgFO1QQIv_RX3cx0UBVXnA3fwhIt4CWaFMxd4KBTqOHD_T1DUjlOSfjIFHXjjRdBFzFWvFJIJPrtDtgruDDzFfIoF_mewLNLc8e-cMTzZlL4C7SEnrpb7q_tv2Yrmhavq5O5mJevvln4B3jyne8i2jLMlo-p4cmJ5kE6qL06URRkZvBahPOk-WM8pfbVqTAKIlX0PjMgNI7aMHC1NZrESZtkRshTiX4CyNrIwv8qA3Xq5cM_jAHzfVN2jNUscw1NP59UwH0-PGghALvUVepzgflkJQnTkS-YAgap0D2ZxMBYddbeniK3_i3v0490i6vRkcpdwOvJsMlFGGoCxma8Z-kFGzqP2YacLVNAxntWrBNemWSLWNY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: "لقد سرب أحدهم المعلومات. شخص وضيع. يجب أن يُسجن أو يُقتل رمياً بالرصاص."</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/naya_foriraq/93716" target="_blank">📅 00:32 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93715">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
🇸🇦
السفارة الامريكية في السعودية:
يتعين على موظفي الحكومة الأمريكية العاملين في المملكة الحصول على إذن خاص من رئيس البعثة لاستخدام أي مطار داخل المملكة، وذلك في أعقاب الهجمات الأخيرة التي استهدفت مطارات المملكة باستخدام الصواريخ والطائرات المسيرة (بدون طيار). مددت الهيئة العامة للطيران المدني في المملكة العربية السعودية تعليق العمليات في مطار الملك خالد الدولي بالرياض حتى 17 أكتوبر/تشرين الأول.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/93715" target="_blank">📅 23:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93714">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇸🇦
‏الكويت تخصص خطبة يوم الجمعة القادمة في كافة الجوامع والمساجد لإدانة الاعتداءات الحوثية على السعودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/93714" target="_blank">📅 23:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93713">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Flgpbh4PshOI5CxGw10I-VkZA68tvvhk10xAIJXJJezgua_9pkV3t0p-AhLFADlw2101C1S_yH0mSXq4iwrh25jFCoNDyudB8sREoZ_fXNnV4W2Zq9G6bFeUix41YQ5WoMnUYVtzbsOuMYwcEMt8fcG6ndsLA9ZeKwohEGiQGn0fHT2vvTISnA0sN_pwmRmof4Lx0e_-aKNClku8MheVpwj9atLIbPXiAfjfJygrvtTirESFj4mTOVbpWUZpqlM7UNSgouHa_9Mc52Fgws0wrwYc_byALdApNI3DWj4jyhzayXKdyj7dKiD8HphuRgia68CSHOOZqbuyrV0Ni_TaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇮🇶
بوتين يرسل للعراق تيمور بيتشاتكين
الأخير سيكون سفير روسيا في العراق كبديل عن البروس الذي غادر العراق قبل ايام ؛ تيمور يجيد اللغة العربية والإنكليزية والفرنسية. بالوقت الذي تطمح روسيا بدور اكبر بالعراق خصوصا وسط التغيرات السياسية في المنطقة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/93713" target="_blank">📅 23:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93712">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سماع دوي انفجار في جدة  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93712" target="_blank">📅 22:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93711">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سماع دوي انفجار في جدة
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/93711" target="_blank">📅 22:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93710">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇾🇪
ما يسمى ‏وزيرة خارجية المليشيات الموالية للسعودية في اليمن:
ناقشنا مع الصين استخدام الحوثيين لتكنولوجيا صينية لصنع أسلحة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/93710" target="_blank">📅 21:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93709">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9399d36df9.mp4?token=vcGvU_rtzxAo8DuXYevKOhjWyrx1KQPHaj9J7gqPY1IyUrBD6BQL9Iwwk27ycfRs6VBtJHOcezpXhdoVMuZL9e7rLUf_uiYfu6tdODaWJ2OQTKY9pKll8XZe79ql4X5TBVJKppLzcsBO5fFHiEtamefWV2H1vtD02hBHhO58yufotNr3Ieno9s8kDtRKxe0bXKreVEzu37Wm0tTsTdKxOFTZmiJlYLWblyoLED_cA0biptPW0ComfNXT7QXTs-5RfLXaLNTpdMmY9f81P2rUIdYwqK7a1A9XgptxnbrDzLUAPwtDFXL7qZOw3beNiT0-P32z0XwR58Em5s8StBL20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9399d36df9.mp4?token=vcGvU_rtzxAo8DuXYevKOhjWyrx1KQPHaj9J7gqPY1IyUrBD6BQL9Iwwk27ycfRs6VBtJHOcezpXhdoVMuZL9e7rLUf_uiYfu6tdODaWJ2OQTKY9pKll8XZe79ql4X5TBVJKppLzcsBO5fFHiEtamefWV2H1vtD02hBHhO58yufotNr3Ieno9s8kDtRKxe0bXKreVEzu37Wm0tTsTdKxOFTZmiJlYLWblyoLED_cA0biptPW0ComfNXT7QXTs-5RfLXaLNTpdMmY9f81P2rUIdYwqK7a1A9XgptxnbrDzLUAPwtDFXL7qZOw3beNiT0-P32z0XwR58Em5s8StBL20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
يمن اليوم ليس بيمن الأمس
.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/93709" target="_blank">📅 21:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93708">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
تمكنت قواتنا المسلحة بفضل الله وعونه من استهداف مطار خالد الدولي في عاصمة العدو السعودي الرياض بصاروخ باليستي وكانت الإصابة دقيقة ومباشرة.
وفي سياق آخر نفذت قواتنا المسلحة عملية استهداف لعدد من تحشيدات العدو السعودي في منطقة رأس العارة والمضاربة بثلاثة صواريخ بالستية وكانت الإصابات دقيقة بفضل الله وخلفت عددا كبيرا من القتلى والجرحى وإعطاب عدد من الآليات.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/93708" target="_blank">📅 21:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93707">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFFWSHAcXwMAUcpp2HRLBWgi17NeRgH6W1P3WiPzWGM2Ryz_jrj2-OtEBj5R6n0ImXON50dO8PhME9XGkJHF2rT4r3lTRCvXljz5hCZgagSrquJlYm2gi5zo8iDHzkhnIdJImaOaNNElMnXWr8yG4W-m_z3fSsojmcdkbXAf0JdY5OUh0YIyvA_dOH3OB3typVybnLJAP_SSXbbM28IN6TYwJYHxAT59P_j7ejJAOS0jXxcMAOWuNTokMpmSN9bVYDI8hX6Tq1s07EErOs_3lFWjXQqq81XGhyAI9u8i0nOfDKRyIMEVh2EDWts6tum3ghiSXvp9VrkLUX1ewodQDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
: بالمناسبة، "ليس لديهم شيء في غضون أسبوعين"، "تنفجر الآبار في غضون 3 أيام"، "يوم النصر الاقتصادي" كلها مرت.
الوقت نسبي؛ اتضح أنه قد يكون غير ذي صلة. جائزة نوبل في الفيزياء التطبيقية لوزارة الخزانة؟
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/93707" target="_blank">📅 21:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93705">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J1U824PolO6uehlaEMaWxthad9KDufqOiTTxDrLOK3T4QsksMDSo27PB8RC_zr_LIZ4IyYVzGPIJBMIqKTa1YFCJiDLXQItUtoRMoPTtE365PSlQevTSuVewnLq-LynE3-muHl9QVJi_QF33_44iHEBI3a1e6K8SJkzd30HbnI2Q7i-vUfSPa6jLjZOo9DbjHt9sYwt-GCvcwb3ZuG-ezpGbmsZt3b1jb4TqeeYPhBWvgEbwRmp39w43zQ8RbXuBb-K-vlm-g7n_IyWdFs_z4wBzDVotL3hxT1gMf6VofyCj0LBpqVUkp-ZL9vmoRZ1-Xx2gR43qgbuZ-E6UtHclkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvyBvBaIvwbQMjlp8oVYsHJK4fRy2wRRHJtrsQh2YjMHz4vhzD4FBTJxBxOCD5kdhVMGk21yIw_Ji_QzRlPf8C8K_tkffhi3qkqbtoC65BcmhsHrcxLn8ToTeKRTEB52rOM0q92N1WJJpgBXv_jDCoEAaw_j234qc5vVdYum2ORNLqAMf88oxVmlUWzaDnHTTcntoq6CxuXKyhJxbSOdXoG4uQ69lm0yblXk_fpGyo1RBk1fg5G1QVZN8dnF-YoG_Q1jZqCW3CwMKpfIZmwJ_IZlF05_By_q5EweIHieB6AtzjubJAZ1pZe52Jn6JNX6sqlmElGrlbxcaw4fZRjfww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🔻
المسؤول الامني لكتائب حزب الله الحاج ابو مجاهد العساف:
لم تتسلم المقاومة الإسلامية لغاية اليوم جواباً رسمياً من السيد رئيس الوزراء بشأن وثيقة تنظيم السلاح التي اتفق عليها عبر لجنة التفاوض الإطارية، وهذا يشير إلى أنها لا تزال في المربع الصفر.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93705" target="_blank">📅 20:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93704">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 42 غارة جوية وصاروخا استهدف بها الأعيان المدنية في العاصمة صنعاء ومحافظات تعز ولحج ومأرب وعمران وجزيرة ميون من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا 2323 غارة جوية وصاروخاً.
إن استهداف جزيرة ميون بالقصف الجوي والصاروخي من قبل العدو السعودي يهدد خطوط الملاحة البحرية بشكل مباشر ونحمل المعتدي السعودي أي تبعات جراء ذلك وما سينتج عنه من تهديد لسلامة الملاحة البحرية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93704" target="_blank">📅 20:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">المنظمة البحرية الدولية:
‏سفينة شحن البضائع الجافة هي ثاني سفينة تجارية تغرق بالقرب من هرمز خلال الـ 24 ساعة الماضية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/93703" target="_blank">📅 19:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
🇮🇷
قُطعت كلمة "هيغسيث" في أحد المؤتمرات أربع مرات متتالية على يد محتجين مناهضين للحرب على إيران.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/93702" target="_blank">📅 18:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
🇸🇦
‏أدان رئيس الوزراء العراقي خلال لقائه ولي العهد السعودي استهداف مطار الرياض والبنية التحتية المدنية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/93701" target="_blank">📅 18:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93700">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇸
🇸🇦
قضية الجاسوس السعودي تتوسع في داخل امريكا   ‏الرجل السعودي الذي تم اعتقاله بتهمة زرع جهاز تسجيل سري في مقر شركة OpenAI هو شريك استثماري في شركة رأس مال مخاطر إلى جانب ابن مسؤول استخباراتي سعودي رفيع المستوى. يظهر هنا في صورة إلى جانب محمد بن سلمان في…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/93700" target="_blank">📅 18:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93698">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184ab84906.mp4?token=sqvHxA0yI-1bIsit3NTG2CJN0hRe1yphobIq3HIEGMGzHhu_OEalE5RkYABJEP6Af7ZnfZw0jL_AcucvicU20CYoKCNJpTxg1IS6AE9gMVRl5M0SX9dEnsmrW0IOxNcrA-P3V7waMMAjf5Y7hWiNJoevFImCJ062_KwVD2lYOmtW6RJZ8K4ttGKEW12Ov0Rgirn9j0Wm6A3iUTXgFlQqteyGhm-brw9acIZ1bOARktwYdO4K7xjts5CaUEwoyuz8SOp_q6_-ePS1h02mOscAGL_UC4CMA2Pq6o0ti6trGxnoOqourdWNlpxP4nNEo0Aox7ZzL9tkw8crezNlfU5VIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184ab84906.mp4?token=sqvHxA0yI-1bIsit3NTG2CJN0hRe1yphobIq3HIEGMGzHhu_OEalE5RkYABJEP6Af7ZnfZw0jL_AcucvicU20CYoKCNJpTxg1IS6AE9gMVRl5M0SX9dEnsmrW0IOxNcrA-P3V7waMMAjf5Y7hWiNJoevFImCJ062_KwVD2lYOmtW6RJZ8K4ttGKEW12Ov0Rgirn9j0Wm6A3iUTXgFlQqteyGhm-brw9acIZ1bOARktwYdO4K7xjts5CaUEwoyuz8SOp_q6_-ePS1h02mOscAGL_UC4CMA2Pq6o0ti6trGxnoOqourdWNlpxP4nNEo0Aox7ZzL9tkw8crezNlfU5VIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا لاستهداف ناقلات النفط في مضيق هرمز بالقرب من سواحل عمان.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/93698" target="_blank">📅 18:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93697">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تؤجل بطولة للتنس عقب هجمات المتتالية للقوات المسلحة اليمنية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93697" target="_blank">📅 18:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93696">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عدة انفجارات جديدة تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/93696" target="_blank">📅 18:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93695">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/93695" target="_blank">📅 17:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93694">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/93694" target="_blank">📅 16:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93693">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">التلفزيون اليمني عن مصدر عسكري:
ننصح المساهمين في شركة أرامكو التخلص من أسهمهم فيها حتى لا يتعرضوا لخسائر في الأيام القادمة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/93693" target="_blank">📅 16:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93691">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">القوات المسلحة اليمنية: مشاهد نوعية لطرد تحشيدات تابعة للعدو السعودي في مطار ذوباب وإحراق واغتنام عدد من آلياته وأسر عدد منهم</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/93691" target="_blank">📅 16:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93688">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxyLNzyxBd_SatBMgy_lVAeNBk5GSivR6pCb-9IyKKwwdI1h6Olv4UJ_106sS3oEpYwBBUdyhfJ7PPT-7SJvJzfieKYDNVMdDvZzuaHLx84jibphrRv35a3XWHTj4wrjBOjaTv012_RrsL8Lz3tFLzQxFZ-YE-QqHbJ_CBKtlDhxi5iv7q_cR3LKOGHktv7Zk14JD2ojMQfmDU7acExDtKucFxwwPYanU9DrcBPh5aiVOiGwn9nQBAHqoIN2ejLbnkC3Xj-ryISxfMJtjKTl0RvGms8Hk_Yh5Jd46VevedGHDCUJCq9HCWuQPPKBThQLKBWl2i3KhdeClDC7wBn2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YE5yCaaEwn4nNXq5V0f0TT1aFe_bBkk-ThxJ4MZKIFyPf4yyd4w-GnvVVyVoLprrAzAgdN9V7i_4j2WDn6_GoXuCCigZkouivOSK_vB7nUz6KoYBagtbu5iAkQRsvuDnQp3yOvzBqIBsVEFSYSA0w3q0Xw9IaorzpkLmUmBXgyK3aw3M1KU3AM9ESL6J0QMfib-WREgOHzCbUU1UGWsMycACShXEtGI6RuK693Dqgm3oas_Z_UM32MGE5ePyG1HqTWi6YExPIW8N3aBmKuerbCKHD_B7cNq1B6VrdE1kCbeloBylAG8NnJay2SB68kKHtmVXVFoe6lTj8yfWEs1m7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HvkwOinwJk0-GyhTCwmcnIK43cpjF7Vwwg2Unpj-h1ooBcRxV1smFCWflv5fnbX9Wv3bWCnJ_Vlnx_fZWJ8Uz3WdZkU2XFVy6vg09kzD04ue7P6RaSim9QExyhyNKRLkbSRcqW2_nel3qdZ-a8KyVwq6D5wLKi6gd4U0r_R3CndQsf3u7GKIktzwUEsEe4GgdqtFuQ_eYZn3-iIr-UhadQgyM7jXZs2fsutm-Ym4xR7-E88J6xthgbTuz2RuzSnTo6ytAJ_fEkimYbVyWUt8no5YFx74FTZJyU2sTpWhR-qoHVb09NszaHmvrF2xPFZInKDhmuebFuod6gCvvIbOcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارات تهز الرياض</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/93688" target="_blank">📅 16:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93687">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجارات تهز الرياض</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/93687" target="_blank">📅 16:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93686">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c2f3d4d17.mp4?token=Y15nnTscOxO5Skni4qZu3egH09ZmC2sYGzBiW-Vl7C7KwUxhqshyN_er3VZvwjlO9C8kQAt8YQ3CHkTkvTQH9-lIqrp32Kik_IbcJd6XCNCxCHh6lXBMWEP9HMW3mosjRcUrY3gfjSRtHxqHpQ89mc8mJuEByXqpovsn9Z5DAZelO_YXNTr8qjVKR-2k4FGbK08-Cw-JPcdQpSoluPPUnqQrizM7RgwN6_gOCZgPN0pYV05oxEU12S_7kowB1r-ZU8fK6doctt4aI56F-StKYjVqRL0ZtBRKKTqGqiK3R_2kpsiYQSBttjMUDc5cIptrY4JPO9FaSCXt1xz0KSf0KzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c2f3d4d17.mp4?token=Y15nnTscOxO5Skni4qZu3egH09ZmC2sYGzBiW-Vl7C7KwUxhqshyN_er3VZvwjlO9C8kQAt8YQ3CHkTkvTQH9-lIqrp32Kik_IbcJd6XCNCxCHh6lXBMWEP9HMW3mosjRcUrY3gfjSRtHxqHpQ89mc8mJuEByXqpovsn9Z5DAZelO_YXNTr8qjVKR-2k4FGbK08-Cw-JPcdQpSoluPPUnqQrizM7RgwN6_gOCZgPN0pYV05oxEU12S_7kowB1r-ZU8fK6doctt4aI56F-StKYjVqRL0ZtBRKKTqGqiK3R_2kpsiYQSBttjMUDc5cIptrY4JPO9FaSCXt1xz0KSf0KzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء السعودية قبل قليل بعد الهجوم اليمني</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/93686" target="_blank">📅 15:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93685">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srWYITM6V3onAYBOYWEFIEEAa-8lAuJeIhj877H42tEV5tq2LUAlNNgYjQHoo06Jx-5tpg2MMj26q1_BRMYAdd4q5EjLST0EedZVxJzyPXqC8stmZfGabgfjFYM6YXKUG0Md2aIN4b6GsL27sViV-YBQ_XXcyGm08a3CkHQV4SnOafRhG3x8yUgTIyTBsUm87fTkRbUv--BbNxYLP0GV0DXGpyYxqjb7KF4sRwMlBj0eJ46nYPuI9gnoKejCFnbHDQ2Kk-6KQtCyty-bNIjvc4fVRbwxQ68mT1Cc0BILD9mSiqeHLMx9NJSeXVGLkAd7qoNXRKTUqlyfDXp-zaGQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئيس الوزراء العراقي يلتقي محمد بن سلمان في الرياض في اول ظهور لبن سلمان منذ اختبائه في غرفة محصنة اسفل احدى القصور وفقا للصحافة الامريكية</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93685" target="_blank">📅 15:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93684">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07668509af.mp4?token=U7ibB4AEpwtbMaDV4qMGAP1F1U6rtzHBA96BiwmBQAkQuUJ-ZfBh2CHoBBTwnn3l8AQ5CJInOILWHSrMOKjfYysItSGtviVlyG1nHPwfOChrl_85-ftPEzGBIKB5zxcH8hCKifzbKYxV_L6lxydO0pMdqZTX5awA6X_Z2N5hQcI__MTwZu9ryTXaUW3aiDm0icHiZOb64ZATOU6r4ijpObWj72yn0AmIdGmGwlIsb_XTuaBQEAzXISg9jrGBHrtx41xRR-z9BhIyHSo0z_RwZYdsilz7wjuOFCgmeEl9Pqb4tCS4ZckXeuzgCKh6WFbltGjavEDMCTp3Xfi49JV0UmilCrI57Tw2t5A28RcdeMhZ0824nC4FFE329Qu581-qtqTI2tJ-DvDsES_TsQaM_UbuX2MAvhbICL0NvPijoZPH-3SmWGzF1uw03pIvAFi1kkrUs8Q2YwfVxBy2iHm4YhZV1SQDBpS8lg74W_7E-NoKljAH6SNGPhJGVALdMWQ-7K8sXyAXu83C9IKLnTLv5XaniypzuYPc5BIq6zJ7rtqwM_uHCBhjsbQONIeB5Jjs8NaP96UdY4h2zKcM8FLsmczYNO5v4oU3JzMsa7uzZpq26_tXCKvPOmvyblQ6HxgeqWaO3uypfK5ZMu5btyv4-3Pq2gTXhAVMVyso7onKsBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07668509af.mp4?token=U7ibB4AEpwtbMaDV4qMGAP1F1U6rtzHBA96BiwmBQAkQuUJ-ZfBh2CHoBBTwnn3l8AQ5CJInOILWHSrMOKjfYysItSGtviVlyG1nHPwfOChrl_85-ftPEzGBIKB5zxcH8hCKifzbKYxV_L6lxydO0pMdqZTX5awA6X_Z2N5hQcI__MTwZu9ryTXaUW3aiDm0icHiZOb64ZATOU6r4ijpObWj72yn0AmIdGmGwlIsb_XTuaBQEAzXISg9jrGBHrtx41xRR-z9BhIyHSo0z_RwZYdsilz7wjuOFCgmeEl9Pqb4tCS4ZckXeuzgCKh6WFbltGjavEDMCTp3Xfi49JV0UmilCrI57Tw2t5A28RcdeMhZ0824nC4FFE329Qu581-qtqTI2tJ-DvDsES_TsQaM_UbuX2MAvhbICL0NvPijoZPH-3SmWGzF1uw03pIvAFi1kkrUs8Q2YwfVxBy2iHm4YhZV1SQDBpS8lg74W_7E-NoKljAH6SNGPhJGVALdMWQ-7K8sXyAXu83C9IKLnTLv5XaniypzuYPc5BIq6zJ7rtqwM_uHCBhjsbQONIeB5Jjs8NaP96UdY4h2zKcM8FLsmczYNO5v4oU3JzMsa7uzZpq26_tXCKvPOmvyblQ6HxgeqWaO3uypfK5ZMu5btyv4-3Pq2gTXhAVMVyso7onKsBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ اليمنية تشق طريقها في سماء الرياض لشق نظام ال سعود</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/93684" target="_blank">📅 15:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93683">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d3e76b11.mp4?token=FtP6aQuHGqLPC23up4hvG5IZl64r9Urmkk4b0BTjtifPVn12DhXAogE-xhFmdR-9lAaDWr6toTT1xrkKvlMmoQkem17zQ9-yaM8RoirMERbXyK8I7lkkCdj_EyoKEmJ4z9W8py_kJGYVvuTgaa0vDS4shmAc7eLuD92pHkVLZ0YlvxCKYebA66UKs4bKYxW0Bok_olaEQIx4FdjzCp2BJTF8LgxVKO6SJIcnyMDCACNJnzubVgG8db0ivYT7hgJXjMzzXsfZ7-rpZCvOty2yawAuHCNFRxgpxBGrc8p3ztJyVghB8LfCsGTtnSyj5DenjBfR-igA5FVg5zj4Wv2JT4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d3e76b11.mp4?token=FtP6aQuHGqLPC23up4hvG5IZl64r9Urmkk4b0BTjtifPVn12DhXAogE-xhFmdR-9lAaDWr6toTT1xrkKvlMmoQkem17zQ9-yaM8RoirMERbXyK8I7lkkCdj_EyoKEmJ4z9W8py_kJGYVvuTgaa0vDS4shmAc7eLuD92pHkVLZ0YlvxCKYebA66UKs4bKYxW0Bok_olaEQIx4FdjzCp2BJTF8LgxVKO6SJIcnyMDCACNJnzubVgG8db0ivYT7hgJXjMzzXsfZ7-rpZCvOty2yawAuHCNFRxgpxBGrc8p3ztJyVghB8LfCsGTtnSyj5DenjBfR-igA5FVg5zj4Wv2JT4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء السعودية قبل قليل</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/93683" target="_blank">📅 15:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93682">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6741f41417.mp4?token=qFMDWjZJg7p49Ec-6fFioFR1pdc8GKgXV2nmrStDV8H7opjeE88BCpdb29DDH72oxzmsrWAVasGgJ7TePnoSxC5KeHDdTeXFypUjgCEWct5R5cBcWQtzOlRVhS-fmB8B60W3cxk9eUCljstgZA8o7sMuTfHDWnS-wecwQfPbUOb8Y2mAnPPTb8GHnGkxaO6Z22rlcgkPERB8NCnOLe_paD9NhHGDgc3YTbSPzHg00TR8S33k4nr1tvTXJ2WyGN0LbAu7IPPB64gBZQfcLoXny13PHVDCMnNfENw7Vk8gTl3Nyvk7it5dCDm2WZoFxWZqPje70DLzZwKw7XD0btFqroWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6741f41417.mp4?token=qFMDWjZJg7p49Ec-6fFioFR1pdc8GKgXV2nmrStDV8H7opjeE88BCpdb29DDH72oxzmsrWAVasGgJ7TePnoSxC5KeHDdTeXFypUjgCEWct5R5cBcWQtzOlRVhS-fmB8B60W3cxk9eUCljstgZA8o7sMuTfHDWnS-wecwQfPbUOb8Y2mAnPPTb8GHnGkxaO6Z22rlcgkPERB8NCnOLe_paD9NhHGDgc3YTbSPzHg00TR8S33k4nr1tvTXJ2WyGN0LbAu7IPPB64gBZQfcLoXny13PHVDCMnNfENw7Vk8gTl3Nyvk7it5dCDm2WZoFxWZqPje70DLzZwKw7XD0btFqroWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من سماء السعودية قبل قليل عشرات الصواريخ اليمنية والصواريخ الاعراضية تملئ سماء السعودية</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93682" target="_blank">📅 15:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93681">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9555bbe18f.mp4?token=WxBz5U27UEsz_-xf3AiBDIuaWGCV1VDc-Pix5LEOaCcQqHiE4T49ZXc1OhDvbif2aSfAve84NzBoxKyOxqOMyhOUSpf8cOZhWwKM-xm53t-Rr5ViYkEuyLNlNOhBWDTEiuIrJPbe6O2ItX9RE7sB98ikcgEogOVkutwV2cIvgchhGQlrDqASHkZqMHTgwHj1JSAAfsjwkgWiGYmpHoxXSqVpFL7kvwgwH4GjOnOpFGEnoxYCdHJJLEb2mG7QeYaAN2jFmdsINHHet_rVofyq2p7DX9Zy_MiBoNGwFHk5JWciRVCoH2o0V2lf8obsMQpLw04dVeZw8eWM35NJq_ih_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9555bbe18f.mp4?token=WxBz5U27UEsz_-xf3AiBDIuaWGCV1VDc-Pix5LEOaCcQqHiE4T49ZXc1OhDvbif2aSfAve84NzBoxKyOxqOMyhOUSpf8cOZhWwKM-xm53t-Rr5ViYkEuyLNlNOhBWDTEiuIrJPbe6O2ItX9RE7sB98ikcgEogOVkutwV2cIvgchhGQlrDqASHkZqMHTgwHj1JSAAfsjwkgWiGYmpHoxXSqVpFL7kvwgwH4GjOnOpFGEnoxYCdHJJLEb2mG7QeYaAN2jFmdsINHHet_rVofyq2p7DX9Zy_MiBoNGwFHk5JWciRVCoH2o0V2lf8obsMQpLw04dVeZw8eWM35NJq_ih_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من سماء السعودية قبل قليل
عشرات الصواريخ اليمنية والصواريخ الاعراضية تملئ سماء السعودية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/93681" target="_blank">📅 15:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93680">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e09852f6.mp4?token=V7YasLL2Kydz9yVtrQWMLjAc0TTB_FiKIyZRbZt3rMcdg7zCGDz-mnCfHdF-UoxntdKQIILu2Z4HrAJnVaUdgh52IBuadotYISaY9uPavTRy_mDu0F7ypDofJpfZ5DQeW-HrwGk2ASzceE3Ly9jkvxFXJMAPYEjOEW-Q0d8KVlYWezAmulJSJhwnXaOWUe71315q-z1cZ8FgR2_swykZhsvEWH98lFFRteq0_Nd26k07Ko6Wf657SwcLEjvv5YYLu_obCwpOPPoo_cpBqizMSRH3EWkIvJkjmCzlAOKmuTNE-ymebGjOhnXCCP235GWYMVbKivfhQ80pKfI1nZGlZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e09852f6.mp4?token=V7YasLL2Kydz9yVtrQWMLjAc0TTB_FiKIyZRbZt3rMcdg7zCGDz-mnCfHdF-UoxntdKQIILu2Z4HrAJnVaUdgh52IBuadotYISaY9uPavTRy_mDu0F7ypDofJpfZ5DQeW-HrwGk2ASzceE3Ly9jkvxFXJMAPYEjOEW-Q0d8KVlYWezAmulJSJhwnXaOWUe71315q-z1cZ8FgR2_swykZhsvEWH98lFFRteq0_Nd26k07Ko6Wf657SwcLEjvv5YYLu_obCwpOPPoo_cpBqizMSRH3EWkIvJkjmCzlAOKmuTNE-ymebGjOhnXCCP235GWYMVbKivfhQ80pKfI1nZGlZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرس الثورة الإسلامية ينشر مشاهد لناقلة الحاويات المخالفة التي غرقت وعلى متنها 2500 حاوية في جنوب مضيق هرمز</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/93680" target="_blank">📅 15:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93679">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D42HOmU995P-A8CUmGL1FrxqHfy2CRjffnBso2BJS13ivenTW42nllYM9zMQiJ048tb1gpAwmuryHv2-Qs8ff-tzaFTFeG8y-mI1PrBIIDNDoDJrncOZp-nLIgXfEbTDEXW7yw7kGN1xY-LiFk4cetk0ZO8AfDHcKFnHFQY6bUJpQCjh_Otfu-qnXRWsvna3BqIzdcBNHkjefEqzPRNIA6iSZ5oxPychy_yybA8Eh2Rus_68JqlMqTiYcjE-5JOiTXoP1HHid6QNiySrjNVzOioBofzYsHIfTBzuQzZWIThLsVwP6aiYrwarNyPpp1p6rCzovrMeUoBHVRrglB49Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
مصرع ضابط في الجيش التركي باقليم كردستان العراق اثر حادث إطلاق نار.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/93679" target="_blank">📅 14:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93678">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇶
الجيش العراقي يعلن رفع الجاهزية الى أعلى الدرجات والاستعداد.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/93678" target="_blank">📅 14:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93677">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا الساعة الرابعة عصرا.. مشاهد نوعية لطرد تحشيدات تابعة للعدو السعودي في باب المندب و مطار ذوباب وإحراق واغتنام عدد من آلياته وأسر عدد منهم.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/93677" target="_blank">📅 14:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93676">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رويترز: مقر أرامكو في الظهران تعرض لأضرار جسيمة جراء هجوم أمس والنيران امتدت لعدة طوابق</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93676" target="_blank">📅 14:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93675">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">أرامكو تأمر موظفيها بالعمل من المنزل بعد استهداف الشركة من قبل القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93675" target="_blank">📅 14:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93674">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">أرامكو تأمر موظفيها بالعمل من المنزل بعد استهداف الشركة من قبل القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/93674" target="_blank">📅 14:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93673">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9e12b2415.mp4?token=OQLvpaqL-fOCPGlcEZuKcx_D5y30jjkafkuubIfWwCrx2j2dpfmffnO8dy4jrr4-8eadzDgghP5aHHd2REMGPcR0Ctu7oGIivefZXRRqD2CsmbjoEzo7H80PIEzDdG2hYGI2EwHL5dZ11cy_znmsc3VeUjAlsNPTJCZxy4yIqiKHOqByRAj8x-TNVztjZYPUSiNLjl3XMmpLct6D9d85s5rCNBaqtrfprKoN6zxFJ8buClFAjgGsQS6Lf1t_PC4GAhwb5M4ClbI7qiO-OGBgzmPrpOtJNJzwuiWJsUBXa1yDNmCMv5DVZ3HB6cyAnR-Wj-Z322m-4fn_G_DgoeWLjhitrbJb3WyR-iiOkHqco7eTVVdAqNqJ-tghRJJ6ywxThmprJ2TvB1H-kGdtAxxqCDeOqliijsWlwz_1dPf_DYtuyTuQfE4p5IX_3f6uFWLS4sMIQd9DAdkzf4yAlNNI-kcs4gXYL-MOIImFE63mN_OLfWiR7ZcJWmysLgFMufigTERhS-hsK-guzPc1TJjqiacXx_HDsiiJ2Z09K3AL7NrCgj5IFD3aQMHPeRM8cVcheHOzXLoFrApzU-5Ejf2hlY-1S3iiwsjbXld40En_k_l4rWuosrjm8KztYtC92Ca5DFkaDEelb1uqUJxC9qH3z_gOU_W01Ga44jTZCNDs0Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9e12b2415.mp4?token=OQLvpaqL-fOCPGlcEZuKcx_D5y30jjkafkuubIfWwCrx2j2dpfmffnO8dy4jrr4-8eadzDgghP5aHHd2REMGPcR0Ctu7oGIivefZXRRqD2CsmbjoEzo7H80PIEzDdG2hYGI2EwHL5dZ11cy_znmsc3VeUjAlsNPTJCZxy4yIqiKHOqByRAj8x-TNVztjZYPUSiNLjl3XMmpLct6D9d85s5rCNBaqtrfprKoN6zxFJ8buClFAjgGsQS6Lf1t_PC4GAhwb5M4ClbI7qiO-OGBgzmPrpOtJNJzwuiWJsUBXa1yDNmCMv5DVZ3HB6cyAnR-Wj-Z322m-4fn_G_DgoeWLjhitrbJb3WyR-iiOkHqco7eTVVdAqNqJ-tghRJJ6ywxThmprJ2TvB1H-kGdtAxxqCDeOqliijsWlwz_1dPf_DYtuyTuQfE4p5IX_3f6uFWLS4sMIQd9DAdkzf4yAlNNI-kcs4gXYL-MOIImFE63mN_OLfWiR7ZcJWmysLgFMufigTERhS-hsK-guzPc1TJjqiacXx_HDsiiJ2Z09K3AL7NrCgj5IFD3aQMHPeRM8cVcheHOzXLoFrApzU-5Ejf2hlY-1S3iiwsjbXld40En_k_l4rWuosrjm8KztYtC92Ca5DFkaDEelb1uqUJxC9qH3z_gOU_W01Ga44jTZCNDs0Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#متابعات  ارتفاع ضغط مواطنة سعودية "بشكل مجنون" بعد رؤيتها شخص رافع جواله للسماء وقت الانذار وكان يضحك ومستانس</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93673" target="_blank">📅 14:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93672">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني
كاتس:
إذا انضم حزب الله إلى إيران في شن هجوم على إسرائيل، فسيتلقى ضربة قاسية وسيفقد المزيد من الأراضي في جنوب لبنان، في منطقتي النبطية والليطاني، اللتين ستصبحان جزءا من المنطقة الأمنية الدائمة لإسرائيل. وقد صدرت تعليمات للجيش الإسرائيلي بالاستعداد لتنفيذ عملية برية. كما سيجري إخلاء حي الضاحية في بيروت وتدمير البنى التحتية فيه، وسيتحول أكثر من مليون شيعي إلى نازحين داخل لبنان.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93672" target="_blank">📅 14:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93671">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Je8fPhFt0spPrC0iM9nsV8PGOkj1149YkBuiLIOqw5ZU9mVuqw7ZTUvwPMhCqrFrZ6CLHZRjFzqQxmnznIqihklt9cJiqgPs9Wx0cxMELYxBXla-1tQoa-ewIEyfce1k0HY8uvw5o6thrQ8sr-ljpoobKGfkjYGz2g2nPYz4kZvBjLUsUQR7hLPmIJN8NJXaCFvjT36AN6I-VF_QBh9-FaYXNiZ8Bg9876eeYs4SR7gbl6G_d4sioouDaZlUwbqUBo9nx5z9OdX25jRPSCsKdGJAEsXW-U2gc74HWT2H-JPo1FgSVA5jTOiMg9OjTQbbgMnTBiGMn7bWFGPE83PzrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#متابعات
ارتفاع ضغط مواطنة سعودية "بشكل مجنون" بعد رؤيتها شخص رافع جواله للسماء وقت الانذار وكان يضحك ومستانس</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/93671" target="_blank">📅 14:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93670">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba7c3b915.mp4?token=UwlcYzpZ21AhsNmjZSK797NdzV5fmj3X8OVraIgb0yD8fE0NVTA9puGXZn9lwmg98_Ewzb0kuVEHK3Ma6_e2j_GhiaG-EIUPiJt6OcTFW9-qi8INahbfpfJWQCfhJQrczZuTzB5P6ezAnujvjeV0NFpgvj8fuZcve2e97ByFBobabrYOwlwcCCUSZBTzoyq7QxJi_MUIFf5TXYKQ_OF60yYnMC8qbu9AVNQJP0DnXVgRTKywm3KxP4Vfu5Vf5lVGz7FnB-J5FsRvUOOW1lQpeiDK4O_bAhpPu-bKhreXBAdiUSw1fAXp2Cn4l4kwNie-h42puNKvkX6sUCjssdSOPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba7c3b915.mp4?token=UwlcYzpZ21AhsNmjZSK797NdzV5fmj3X8OVraIgb0yD8fE0NVTA9puGXZn9lwmg98_Ewzb0kuVEHK3Ma6_e2j_GhiaG-EIUPiJt6OcTFW9-qi8INahbfpfJWQCfhJQrczZuTzB5P6ezAnujvjeV0NFpgvj8fuZcve2e97ByFBobabrYOwlwcCCUSZBTzoyq7QxJi_MUIFf5TXYKQ_OF60yYnMC8qbu9AVNQJP0DnXVgRTKywm3KxP4Vfu5Vf5lVGz7FnB-J5FsRvUOOW1lQpeiDK4O_bAhpPu-bKhreXBAdiUSw1fAXp2Cn4l4kwNie-h42puNKvkX6sUCjssdSOPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من منطقة عسير جنوبي السعودية بعد هجوم للقوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/93670" target="_blank">📅 13:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93669">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇱
نتن ياهو عن الإخفاق في 7 أكتوبر:
كان هناك عمى استخباراتي، لكن كان هناك عمى أيضا في الحادي عشر من سبتمبر 2001، ولم يطالب أحد الرئيس بوش بالرحيل.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/93669" target="_blank">📅 13:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93668">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e467f943b9.mp4?token=T6INRIhSIUr3vLiMMtd9odsAU8_i3VaUYJkHO-ELUYzEVttrBjEPbEevN5QIHoCC5852VhcCmllv-10gpZWH7uevowCmsuR2ERD0gnNuzQ1MfshormsIDzVGWaAh4d9X6bSMb9zEZF990GwWGXGpLe1TjAjKvn1sMovwjnytAQPtUbebDu5aN2gFkj-d3qhjWWj-7r20rfKef-ZS2u4OSwYw538x3Zr0SK30OBIhi1w3mmlhXYX4BGnp1ImaPx4YbFNsznCtlfufv06JhEpqgGh3Hu6zlCZiW4xOVMOO3L59zckLR1qSqK53wmGJWJLxVFCIoXS7-ZVWxx1vlHPX8X7wm3o5viQ_ZCkze3PBXqJWquaMXANTPqTHahaCMpor6TFszimnTzofhgYwJTAxfXB5J5Ykqt97tuldGTDdM7yQsfj88t9dW_qqBtV_b95303SDEz6o9ccn2xvdQvTRIBRe3jgOykTJSsL1C1bEXhgd8rBIxNvdtEPy0O7prFD_Zuhqz8rJCplk8J0ww_5dvZLquT69Fk33o9TYD378CvCvJVVm3Ni4Dv7sqyf8mTRlStqD53xNGS_0U03e_zyLExURnr1bCA8pr6177Y_721fDSF4mYger4G1FJJcesimABshpyhGqnkwF42RG1-sK04dqzzPx-pHDE3F7sdovFBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e467f943b9.mp4?token=T6INRIhSIUr3vLiMMtd9odsAU8_i3VaUYJkHO-ELUYzEVttrBjEPbEevN5QIHoCC5852VhcCmllv-10gpZWH7uevowCmsuR2ERD0gnNuzQ1MfshormsIDzVGWaAh4d9X6bSMb9zEZF990GwWGXGpLe1TjAjKvn1sMovwjnytAQPtUbebDu5aN2gFkj-d3qhjWWj-7r20rfKef-ZS2u4OSwYw538x3Zr0SK30OBIhi1w3mmlhXYX4BGnp1ImaPx4YbFNsznCtlfufv06JhEpqgGh3Hu6zlCZiW4xOVMOO3L59zckLR1qSqK53wmGJWJLxVFCIoXS7-ZVWxx1vlHPX8X7wm3o5viQ_ZCkze3PBXqJWquaMXANTPqTHahaCMpor6TFszimnTzofhgYwJTAxfXB5J5Ykqt97tuldGTDdM7yQsfj88t9dW_qqBtV_b95303SDEz6o9ccn2xvdQvTRIBRe3jgOykTJSsL1C1bEXhgd8rBIxNvdtEPy0O7prFD_Zuhqz8rJCplk8J0ww_5dvZLquT69Fk33o9TYD378CvCvJVVm3Ni4Dv7sqyf8mTRlStqD53xNGS_0U03e_zyLExURnr1bCA8pr6177Y_721fDSF4mYger4G1FJJcesimABshpyhGqnkwF42RG1-sK04dqzzPx-pHDE3F7sdovFBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العاصمة السعودية الرياض صباح اليوم خلال هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/93668" target="_blank">📅 13:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93667">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da3dde5505.mp4?token=pX2XYLWLGXK_AF1EcUJcycte4r2jtZu-eyg0q8DkxHHh8jdkfrH1oOYA-IgEyQCBLLsI-Myp-GxWvCnUzqDE6Jj5q8gWEpc5mK9II5nfXWj1XvLjJvQjjhT0ofRd2c1R-7l8DsXKEPSW5XjecvGR_gv-M3r-eZPVaz6xb1yGpxr4O40q0o23ibEeEwszkPsoWoKFXt5BQPv6QvyLkv1lW2rI2ylUEEDxZn81Dj1u2qVz_dNsIGfkX_SUEMYxZGb7aLrrWFO-_UR1BYoWCfQ18h2HbvO6VGTGFusH73BQfs7SkWnqThs_Vc9-812Hiu4p5I3Ncym72t3uWaGbemqgdjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da3dde5505.mp4?token=pX2XYLWLGXK_AF1EcUJcycte4r2jtZu-eyg0q8DkxHHh8jdkfrH1oOYA-IgEyQCBLLsI-Myp-GxWvCnUzqDE6Jj5q8gWEpc5mK9II5nfXWj1XvLjJvQjjhT0ofRd2c1R-7l8DsXKEPSW5XjecvGR_gv-M3r-eZPVaz6xb1yGpxr4O40q0o23ibEeEwszkPsoWoKFXt5BQPv6QvyLkv1lW2rI2ylUEEDxZn81Dj1u2qVz_dNsIGfkX_SUEMYxZGb7aLrrWFO-_UR1BYoWCfQ18h2HbvO6VGTGFusH73BQfs7SkWnqThs_Vc9-812Hiu4p5I3Ncym72t3uWaGbemqgdjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
سماع دوي إنفجار مجهول في قضاء سيد صادق بمحافظة السليمانية شمالي العراق.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/93667" target="_blank">📅 13:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93666">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇶
سماع دوي إنفجار مجهول في قضاء سيد صادق بمحافظة السليمانية شمالي العراق.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/93666" target="_blank">📅 13:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93665">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
🔻
الحرس الثوري:
إيران مستعدة للرد على أي انتهاك جديد، بقوة أكبر من أي وقت مضى، وستكون تداعيات ذلك هذه المرة أكثر إيلامًا للولايات المتحدة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/93665" target="_blank">📅 13:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93664">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6639629a5.mp4?token=vNU7MSnr1ylq3q7W_m-GjmHHoYbkwbGGGeGmz1VIrI609OplSufLvCPTgAB-qqU9OfRrhtYGxbAyDT5iJN8r_P-GvlUMw1SGhpozdYn6xjFqBWBmgT7mHgTQ1kUT3--m0vSsorPfcOQXQKf3eRrt4gJ6DKUtGaYHX9uVhgByqbRwBrdk7FBhRmtGmxIaILprDx8gUaS2MxOBXgkllJ9IBMDyObB58NiTLo3AnUrhNopxvKxROfsGqXPq38KMzwAgKGNQtvRObhdtGhzUK6AW3TTfxdJuVBwPrOUO02SZMI5I9d1e_zA0zqRFf766bDKQ9uu5iXUF8QUoTBeQ315jkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6639629a5.mp4?token=vNU7MSnr1ylq3q7W_m-GjmHHoYbkwbGGGeGmz1VIrI609OplSufLvCPTgAB-qqU9OfRrhtYGxbAyDT5iJN8r_P-GvlUMw1SGhpozdYn6xjFqBWBmgT7mHgTQ1kUT3--m0vSsorPfcOQXQKf3eRrt4gJ6DKUtGaYHX9uVhgByqbRwBrdk7FBhRmtGmxIaILprDx8gUaS2MxOBXgkllJ9IBMDyObB58NiTLo3AnUrhNopxvKxROfsGqXPq38KMzwAgKGNQtvRObhdtGhzUK6AW3TTfxdJuVBwPrOUO02SZMI5I9d1e_zA0zqRFf766bDKQ9uu5iXUF8QUoTBeQ315jkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔻
بحرية الحرس الثوري:  اصطدمت سفينة حاويات مخالفة -كانت تحاول عبور مسار غير مصرح به وخطير في مضيق هرمز- بلغم بحري، مما أدى إلى وقوع انفجار واندلاع حريق هائل فيها.  غرقت السفينة -التي كانت تحمل شحنة تتجاوز 2500 حاوية- صباح اليوم في المياه الواقعة جنوب مضيق…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/93664" target="_blank">📅 13:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93663">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
🔻
بحرية الحرس الثوري:
اصطدمت سفينة حاويات مخالفة -كانت تحاول عبور مسار غير مصرح به وخطير في مضيق هرمز- بلغم بحري، مما أدى إلى وقوع انفجار واندلاع حريق هائل فيها.
غرقت السفينة -التي كانت تحمل شحنة تتجاوز 2500 حاوية- صباح اليوم في المياه الواقعة جنوب مضيق هرمز؛ وذلك بسبب شدة الحريق.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93663" target="_blank">📅 12:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93662">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQ0VmKNjXy95Qs8Ey_vowlhzJJXN8n5kKdEI6hApnGfGO3KST79mamDRs_EDqzDOn1UL5ay_plyTXxODIYK6H_kp5BVZ0jmq5B6v-dvPX1Lc2liAUYXHMTgcoT3-M1Oh1DrbmJbUk1izGbEGnRszMsl5Rbu9vcLv47aXzNMWVM_9T1SAhxw7t-7J070CTOx3opLXX8jpGloFU0ehIXgixyrxGGu28olbFafJ8SyQXHcZ4ZjV337JV_eP9ZpS23HSKpMZIxYDCJdvLuG7yIcPC7T7x3nq-Y4YkjI1jFjtIkK8-NmXgdIVryKdWNRblGZQ896Ls2LIpYQgGTxrnva_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
إستشهاد عنصر من الشرطة الإيرانية وإصابة 3 أخرين في هجوم إرهابي بمحافظة بلوشستان جنوب شرق إيران.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/93662" target="_blank">📅 12:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93661">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aom69BGqFGNxrI1Q5Lu9Gfieur5XklKvmfIoetYar1jVQ7RQdpBU8GF3fs_tJ0-ojJIiyZLno-KqMkEfwfHkV_bEdyr0iD2P4iF48COUxPF2vXfveYtPidYS0VBZoliKtBgjFdJj54Bzq0Rjs-nsEpcY_7y7xrBwr-3molJSIRpwl718rkcvfIwScIMAyNgKEy2LoWctS9RaJSVxX_b45t637Pc1tU8Mv08awQLU3KpGAYwJETs8pqwODGp_RFPkOsdpGLWM0clZU6XdwFB8Kp4wTNntF8Kb3eGxtakebVyKsC6rOjXQPIROk4xXVszN3f9Jt1-CRHpN-bV5S9ie9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
إستشهاد عنصر من الشرطة الإيرانية وإصابة 3 أخرين في هجوم إرهابي بمحافظة بلوشستان جنوب شرق إيران.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/93661" target="_blank">📅 12:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93660">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇾🇪
القواتِ المسلحةِ اليمنية:
ردًّا على العدوانِ السعوديِّ الغاشمِ على العاصمةِ صنعاءَ والمحافظاتِ الحرةِ وفي إطارِ عملياتِ الردعِ تجاهَ المعتدي السعوديِّ الذي استهدفَ بلدَنا وشعبَنا خلالَ فترةِ التصعيدِ بـ 2281 غارةً جويةً وصاروخًا ارتكبَ من خلالِها عشراتِ الجرائمِ.
وتنفيذًا لما التزمتْ بهِ القواتُ المسلحةُ في تحذيراتِها للعدوِّ السعوديِّ المجرمِ
نفذتِ القواتُ المسلحةُ اليمنيةُ عمليةً عسكريةً نوعيةً استهدفت شركةَ أرامكو في الظهرانِ بالمنطقةِ الشرقيةِ ومطارَ خالدٍ الدوليَّ ومصفاةَ أرامكو في الرياضِ
وذلك بعددٍ كبيرٍ من الصواريخِ الباليستيةِ والمجنحةِ والطائراتِ المسيرةِ وكانتِ الإصابةُ دقيقةً بفضلِ اللهِ وتسببت بدمارٍ وبنشوبِ حرائقَ في المواقعِ المستهدفةِ.
تؤكدُ القواتُ المسلحةُ اليمنيةُ أنَّ عملياتِها باتجاهِ العمقِ السعوديِّ ستستمرُّ خلالَ الأيامِ المقبلةِ باستهدافِ مطاراتِ العدوِّ السعوديِّ ومنشآتِهِ النفطيةِ وستكونُ عواقبُها عليهِ وخيمةً بإذنِ اللهِ وقوتِهِ.
وبهذا تحذرُ القواتُ المسلحةُ اليمنيةُ كافةَ شركاتِ الملاحةِ العالميةِ والمواطنينَ والعاملينَ في تلكَ المطاراتِ والشركاتِ بالابتعادِ عنها والإخلاءِ الفوريِّ لها كونَها أصبحت أهدافًا مشروعةً لقواتِنا المسلحةِ.
مستمرونَ في فرضِ معادلةِ الحصارِ بالحصارِ والتصعيدِ بالتصعيدِ واستهدافِ التحشيداتِ التابعةِ للعدوِّ السعوديِّ حتى وقفِ العدوانِ وإنهاءِ الحصارِ عن بلدِنا العزيزِ.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/93660" target="_blank">📅 12:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93659">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇱
🔻
إعلام العدو:
خطر تعرض إسرائيل لهجوم صاروخي من حزب الله؛ تم نشر المزيد من بطاريات الدفاع الجوي في الشمال.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93659" target="_blank">📅 12:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93658">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔻
وكالة الطاقة الدولية:
تصاعد الهجمات مؤخرا يهدد تعافي صادرات النفط في الشرق الأوسط المسجل في سبتمبر.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/93658" target="_blank">📅 12:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93657">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuWcxqGiut6tOgLWBVCqjvkIn8yYj1qVvZKZxXzGzcgs1qtEkX-FoNopCeKwV_9l_iQMbO0ldXzIwQZkyPVrLA-jU25pVa-rVkmmjtaWBHGPx5fJkFBrTzhhmxw-1-jFVxrWTFbSC1Fc0IFZP2s9AjKu0YaR5-W4R50WzhEMz9mTALtEvmuo4obX_d9QSdWDPFb3wdIUKfwgIRLUV1LOV3vTibDHvcFMB6XfzXkduXlwpBfvrvj1QRhUAzA_audwOfG5FiUYIYaXI2oh1BU9Hwwy9v9_M03m0vsxg0XvFPbZMWErBHel2UsNgZFca5fvwi6urV9oG5Ja3A1BP84akQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
إنفجارات عنيفة تهز مدينة جدة في السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/93657" target="_blank">📅 11:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93656">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇦
🇷🇺
🇺🇸
‏
مسؤول أوكراني كبير:
أميركا تساعد روسيا في حربها على أوكرانيا.
😆
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/93656" target="_blank">📅 11:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93655">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBz8KLUNdFBfd30KTl1Mlpi2i3uS0AAhxrMAsTBBz-4Wp4hubrh_n2GlIdAUBGNf3xTsnNNQ8QmlEIBnaz0pX22rOIi5KGVN9m8ljtFhA2mK-mZV8CfEO2Ts6b14mNy8yZjY9pkRTQKxs7J6ENrj0u8RRYNyTxxyNol8yEJCcm2UVn25taLLfqF3BN_2BQIjejcoDzIsHefgEo4lu6BgynLW49bXkd6GKpWq4mKCS-htGLC8Z-Q0mzCNmZVfD0rXtgBiX0028-0zNeV46lWofftpzLSkxBNjcmhp8oyeIWVmLycxCrjp0H-k3PzDW51b85afcQI9f7nZCD1ms8TjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
إنفجار عبوة ناسفة في كركوك ؛ إستشهاد عميد كحصيلة اولية .  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93655" target="_blank">📅 11:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93654">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇸🇦
انفجارات تهز الرياض.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/93654" target="_blank">📅 11:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93653">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
🇮🇷
عدوان أمريكي على صيادة إيرانيين بالقرب من سيريك جنوبي إيران.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93653" target="_blank">📅 10:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93652">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/701e388461.mp4?token=KKO6fU2OqyqQbOX45QNxKhYbMEuIeJOpMWdOHCoNzxh3JeqZUU_aciqLHyREd5JQmZwj_aWCqAuwPhNo48r8z_LlvEBM8FCpRgd8UQMCZBN4_uUifjAJ00D2A8lKbST2Kp7MAWpJzzGCJLTYhkwbHm7WlgocgBmkfEbUndJuyrc0A_evrrOVaZOhM55QaXGjtWiUfsvm3KwbsjCcP-YP92_yhF2elMOMpC53cJ6yxY6scGoOA9O_swcsVU6S5d9Q7ZzF2fRXV77P_sY3VRpOFQ1tgZn5Dz_IP6mijIHG93rkSePJUY2JmGqcRpTv4cfc_zZvNZRwqZV7ctqCkHTrKx8_jDiPZBZnI00gKZaVXoGLYNnTexKClYKAz7p9WvnSMYqqLUFla05WmV8Tk5-FA_tTPIe5Ua8IALR-w40ZelYz8R7BZmADjagtwoiTrvnGo_4mt6l7zLAgCPTzf61D1-dyACEB3IwloIn9253RrYJIz7-SQPYiHLoHWRdgV1k0XOkbplkLlWV89KuQJM1jd7t2Dg2ce1_dx9n5TdjIl2AEDkNF9kWgYXT_pl-ibXCdAgUWOrfQq3ysStCiEgT77AuSRRGeLdLbjUhLVr3Swy3sFUdz2p9yCRHjnwqUG2Z4V2XTeoZrcpVO2nM_t6bnzF5mR-4T3lk0Gdv6_xtHV6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/701e388461.mp4?token=KKO6fU2OqyqQbOX45QNxKhYbMEuIeJOpMWdOHCoNzxh3JeqZUU_aciqLHyREd5JQmZwj_aWCqAuwPhNo48r8z_LlvEBM8FCpRgd8UQMCZBN4_uUifjAJ00D2A8lKbST2Kp7MAWpJzzGCJLTYhkwbHm7WlgocgBmkfEbUndJuyrc0A_evrrOVaZOhM55QaXGjtWiUfsvm3KwbsjCcP-YP92_yhF2elMOMpC53cJ6yxY6scGoOA9O_swcsVU6S5d9Q7ZzF2fRXV77P_sY3VRpOFQ1tgZn5Dz_IP6mijIHG93rkSePJUY2JmGqcRpTv4cfc_zZvNZRwqZV7ctqCkHTrKx8_jDiPZBZnI00gKZaVXoGLYNnTexKClYKAz7p9WvnSMYqqLUFla05WmV8Tk5-FA_tTPIe5Ua8IALR-w40ZelYz8R7BZmADjagtwoiTrvnGo_4mt6l7zLAgCPTzf61D1-dyACEB3IwloIn9253RrYJIz7-SQPYiHLoHWRdgV1k0XOkbplkLlWV89KuQJM1jd7t2Dg2ce1_dx9n5TdjIl2AEDkNF9kWgYXT_pl-ibXCdAgUWOrfQq3ysStCiEgT77AuSRRGeLdLbjUhLVr3Swy3sFUdz2p9yCRHjnwqUG2Z4V2XTeoZrcpVO2nM_t6bnzF5mR-4T3lk0Gdv6_xtHV6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
عدوان أمريكي على صيادة إيرانيين بالقرب من سيريك جنوبي إيران.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/93652" target="_blank">📅 10:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هجوم صاروخي يمني يدك الرياض.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/93651" target="_blank">📅 10:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93650">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الله أكبر  انفجارات في محافظة الخرج السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/93650" target="_blank">📅 10:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/93649" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/93649" target="_blank">📅 10:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الله أكبر
انفجارات في محافظة الخرج السعودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93648" target="_blank">📅 10:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93647">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇸🇦
انفجارات تهز الرياض.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93647" target="_blank">📅 10:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇸🇦
انفجارات تهز الرياض.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/93646" target="_blank">📅 10:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYR7Ch9IMj25-Maz0dVFsZNUZnBE6HtXHjbhI7AopOeYopWPnc6D2hJdTAdptmMviwIGu45u8F0oEbUkc-CF_7_fXQ1OhfoAWJEXeTxGsU59XLRfE_XJn0-uuW6Sp_mKpLtfEzQBfmdFaYclJfhNvPgM8IVLxnvGe4fj-KXd3vurGlepvx_cQ31MmTxWVwPrSKavKQKEBkdft_l7_q1O0Fq2oY1m8Dudw97lyihjPScoVaagDu-3BR61rkLrZSOQiIIvH9LWIJzoWYUsUIIh8pmHzFZuFdc-pQ9SmxirhJByxRTEWDzCfwlwt49gbRYO8jdZir4eZ7nGB_9vbCSxAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
إنهيار مبنى من عدة طوابق في تل أبيب؛ سقوط إصابات بصفوف الصهاينة كحصيلة أولية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/93645" target="_blank">📅 10:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇶
إنفجار عبوة ناسفة في كركوك ؛ إستشهاد عميد كحصيلة اولية .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/93644" target="_blank">📅 10:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇦
زيلينسكي:
السبب الرئيسي لارتفاع أسعار الطاقة هو الحرب في الشرق الأوسط وحصار مضيق هرمز.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/93643" target="_blank">📅 09:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93642">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇸🇦
إنفجارات عنيفة تهز مدينة جدة في السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/93642" target="_blank">📅 09:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93641">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇸🇦
إنفجارات عنيفة تهز مدينة جدة في السعودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/93641" target="_blank">📅 09:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93640">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Alj37Hs8_V0hNXMEg2bW2U-EbPro0jJLHj3Hpvd7C0pFD4cpYAvw7T-d4Rky4BGe2brtck3WAW7MPEODY7ojwPgJaLzP5eb8nBVgODJEOpqyg5WHs0PlnETQ8XxempymShsmOsKOWenlGT-uk_IVEMgWVPSGp92iu5Hbh4-zpnRK8xv6Tv7uhVxIWNkkNkuwZPZ9MJixiTJYsynTxrTVR_EF4evH8jE51R6xN2FO-l-88STG24N5Oa9tUE1S8J3UBTqMVGZqPA8W8ZLfOzwrlr0Ww_-3NKZGN6YJ5WBWMaz_fUO4ISgTcfVe-1sfUgC3-ycQjm5L5Q8QxX31ABP9lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
التحقيقات الفدرالية الأمريكية تعتقل مواطن سعودي كان يتجسس مع زوجته على شركة بمجال الذكاء الصناعي في امريكا والتحقيقات الاولية تشير ان محمد بن سلمان قد كلفه بذلك !</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/93640" target="_blank">📅 09:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93639">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDMXsplul5K4OFaA4VtOrz3DdB4GQNSEeRNMZMyktE_G6h9uYqFB34myrI-jaTEDKtYdIDjfQuHuBYyaIbmgvwRhZBaO6AvxAMinwxOTiiM25OXzqOaqTuVuhsGmy5wujBOsUAnkph1Yi02Hp_MOpe3_EjZBQFk2Rsdp2XDNt_U-BTKAFfFk0jyLAkbfnIJYWEFX2YF-PPq-dRCEXrsNAB9FVYuydHIXDsHGw7U8enGz3rHwR-BTNyk1bSGVkKsiZO_doXwwvvqMRcXu50tPEff_4FxBdl9bOT-vUYhp5GGhXci48i6034fdfAeR5GkoHppUadTF1VVsTxPi1fYzbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
التحقيقات الفدرالية الأمريكية تعتقل مواطن سعودي كان يتجسس مع زوجته على شركة بمجال الذكاء الصناعي في امريكا والتحقيقات الاولية تشير ان محمد بن سلمان قد كلفه بذلك !</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/93639" target="_blank">📅 08:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93636">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b42f603e9.mp4?token=VpD1CsGzAtSZGyamJDfEAVeWRjtNGebSqOYXatAO4rHr1eTnq5l8n-HEmFBdrtCp-tl1m8-AqS2DDSGlhdw3PcICaMb4e3Vgnx9S-f4kDdohIsI1Ttla6g5E036DbyLl1ed1wvx2s0j448XL5XhlBKTj24_5ND3RVU6SJCCJrvfPJthScdvxmtQkPimdEhTsvRHZK-GtjX7I4OG4s5yVAIi_S5B-idrvjAbuOaFCQ7bWrE-wDx4tEVa4YGDcBgHDYs3C0LmINVeMmKcIANk2FucblDu-QQtdd3nPvobEMncljqyFRW1lvRL1DvkK9zmC_wdEaNozmW0u4kVNFa-4Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b42f603e9.mp4?token=VpD1CsGzAtSZGyamJDfEAVeWRjtNGebSqOYXatAO4rHr1eTnq5l8n-HEmFBdrtCp-tl1m8-AqS2DDSGlhdw3PcICaMb4e3Vgnx9S-f4kDdohIsI1Ttla6g5E036DbyLl1ed1wvx2s0j448XL5XhlBKTj24_5ND3RVU6SJCCJrvfPJthScdvxmtQkPimdEhTsvRHZK-GtjX7I4OG4s5yVAIi_S5B-idrvjAbuOaFCQ7bWrE-wDx4tEVa4YGDcBgHDYs3C0LmINVeMmKcIANk2FucblDu-QQtdd3nPvobEMncljqyFRW1lvRL1DvkK9zmC_wdEaNozmW0u4kVNFa-4Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة إصابة صواريخ القوات اليمنية المسلحة اهدافها في الرياض وسط السعودية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/93636" target="_blank">📅 03:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93633">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">لحظة إصابة صواريخ القوات اليمنية المسلحة اهدافها في الرياض وسط السعودية
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/93633" target="_blank">📅 02:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93632">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSQ8njANFx-KWb7gwkSe3kIZLVBdFnZN3WjTcnB7tCt7jybS1SgmDzOv0r3sjR4O90A3gpDixojuoLjNOIYd9BkfjnezsEdDgFrpGD-2w9PUUvgsdRcprkx493GJK9t1SDxvYOzTnmR7Eb7e2LARSYJCIsxUNjO6bptV2v6zQc049on0ic_8ckbFZaX9Wgomju_AtOKDoFLNGlLoVhmVQGpsFqz5tut66Hhrcu7MpmLc8KBeoVwj3OFOqFERd1TWaCr3mJGj1MncSTVuHOqgsRGjXgvvYIKD80z_zrJKcElLzjdl0Dia2GoiVpuvszskbNCdSKGBTG5scqe_rsDx1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
التحقيقات الفدرالية الأمريكية تعتقل مواطن سعودي كان يتجسس مع زوجته على شركة بمجال الذكاء الصناعي في امريكا والتحقيقات الاولية تشير ان محمد بن سلمان قد كلفه بذلك !</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/93632" target="_blank">📅 02:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93631">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجارات تهز مدينة الخرج في السعودية،صاروخ كروز مجنح يصيب هدفه بشكل مباشر
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/93631" target="_blank">📅 01:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93630">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fd1b9c49.mp4?token=Gf12aaKKxxG1q21nQZDzXQDYg82x5fnKXWBHZHnGGOKUZwYzAnTrj7WEsaP4kxqEyKJmx94Xh6lPd9fzq1v2fAeHooOf3iV8Y_IvdxjOXgIyhhyBne7mG2GxvLwWUBQy3pWIaeUuIbG7oRtVLNypIxFZS8XDF2d_ulUniTID1Du43xevoF5W0-te2Y8ulZevaxRR86CjbgawpJxLvXfbWKTQ9E5fhmixiQUzOtQFVh93YmasgH9X-jbHt7RrmUFB2uJ0ctQH36_T_UPY8LKQizCaBlvkfuzOKfGcQcipl5uy4Rw5CE7xRHD_2WBAUZuLe7YB6wx00V6zdOD_RvtQoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fd1b9c49.mp4?token=Gf12aaKKxxG1q21nQZDzXQDYg82x5fnKXWBHZHnGGOKUZwYzAnTrj7WEsaP4kxqEyKJmx94Xh6lPd9fzq1v2fAeHooOf3iV8Y_IvdxjOXgIyhhyBne7mG2GxvLwWUBQy3pWIaeUuIbG7oRtVLNypIxFZS8XDF2d_ulUniTID1Du43xevoF5W0-te2Y8ulZevaxRR86CjbgawpJxLvXfbWKTQ9E5fhmixiQUzOtQFVh93YmasgH9X-jbHt7RrmUFB2uJ0ctQH36_T_UPY8LKQizCaBlvkfuzOKfGcQcipl5uy4Rw5CE7xRHD_2WBAUZuLe7YB6wx00V6zdOD_RvtQoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر
🇸🇦
وزارة الطاقة السعودية: استهداف مبنى إداري تابع لشركة أرامكو السعودية في الظهران.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/93630" target="_blank">📅 01:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93628">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed9d03570d.mp4?token=tsISL9yINGhT5R2BvRHfgreZwv78A3tFxOci54vXSWkE8ziMyW1qs9qfV1L9g-lYExBvNbPf9sg1hsKcgrHgIVtRmNvaf09aR53o6Ex4igE6dpf_Kb7ETCEHCIl1soEeYBiYyjg5biz0CcR1K4Xt-GUbiCsDCstVEB9Te5t30eZdFsOCO803KD8CkjAJFcd9DE_GiCf86wqoJ-pf7iNBM3tXmV7sDQHNYGYlhq7LDjIVS-6LvV8Mjr7xF_u8enJ_hqXNM9_ILEeH7myHomtCeR6NhB7RQ6LISiKnGIM_fCMV2FkC7aTzky0GjCergvi0ZgJo9AJKfba6y3Ln1yYdVj6_iiNmYXPcFMJ9HPPKx_359C469rjHAq7aDClCPZ18bMDqLhCW1z7ePoVUqbgflgfKKoC8XHOTYJlpxbU7Mx8eja5MTB__K1wcLPom6g34pIAECd2y14nPIjPmC3EdSXB_LMsacmjnW8lnoMwlXKT_SPbClE9YvXLnD835Ne62tSEcdIZs8Mzdp-17LpK1Z9-HAN02DIPeu9mchcQ98-8PE1seq1pRv2vaUSVGxDLntXGHFgEMP2VC5Jn04x0P6JZQ1o598-KQNvwfSi-gol2_iIfhomviybOyAU7Y7X_H0KF_wqguqcPa1Rcg2oHM3ecALrdwQDg08hMAK7q6Ljk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed9d03570d.mp4?token=tsISL9yINGhT5R2BvRHfgreZwv78A3tFxOci54vXSWkE8ziMyW1qs9qfV1L9g-lYExBvNbPf9sg1hsKcgrHgIVtRmNvaf09aR53o6Ex4igE6dpf_Kb7ETCEHCIl1soEeYBiYyjg5biz0CcR1K4Xt-GUbiCsDCstVEB9Te5t30eZdFsOCO803KD8CkjAJFcd9DE_GiCf86wqoJ-pf7iNBM3tXmV7sDQHNYGYlhq7LDjIVS-6LvV8Mjr7xF_u8enJ_hqXNM9_ILEeH7myHomtCeR6NhB7RQ6LISiKnGIM_fCMV2FkC7aTzky0GjCergvi0ZgJo9AJKfba6y3Ln1yYdVj6_iiNmYXPcFMJ9HPPKx_359C469rjHAq7aDClCPZ18bMDqLhCW1z7ePoVUqbgflgfKKoC8XHOTYJlpxbU7Mx8eja5MTB__K1wcLPom6g34pIAECd2y14nPIjPmC3EdSXB_LMsacmjnW8lnoMwlXKT_SPbClE9YvXLnD835Ne62tSEcdIZs8Mzdp-17LpK1Z9-HAN02DIPeu9mchcQ98-8PE1seq1pRv2vaUSVGxDLntXGHFgEMP2VC5Jn04x0P6JZQ1o598-KQNvwfSi-gol2_iIfhomviybOyAU7Y7X_H0KF_wqguqcPa1Rcg2oHM3ecALrdwQDg08hMAK7q6Ljk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حديثة من سماء الرياض أثناء الهجوم الصاروخي اليمني.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/93628" target="_blank">📅 01:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93627">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇸🇦
الدفاع المدني السعودي يعلن عن إصابات مباشرة للصواريخ اليمنية في العاصمة الرياض وسقوط عدة إصابات.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/93627" target="_blank">📅 01:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93626">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بمن نصدق؟!
التحالف يقول تم التصدي
ووزارة الطاقة تقول تعرضنا لاعتداء!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/93626" target="_blank">📅 01:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93625">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مقرات شركة ارامكو في الظهران تتعرض للقصف  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/93625" target="_blank">📅 01:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93624">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الله أكبر
🇸🇦
وزارة الطاقة السعودية:
استهداف مبنى إداري تابع لشركة أرامكو السعودية في الظهران.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/93624" target="_blank">📅 01:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93620">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/010a765bc9.mp4?token=FqUNArvYgua6sjMjUpnYQEhlPIp41s9k1lwEo_xOZQJoaia8EsqnOz7D6paz8Ve5RSv_XVgGajZ_0X1AyZhIlXzd8po9NZCawPl4DSmG_2rSx0CYVIngaE-3iRtvO-hVn5j358erYBhd7XL36TfyXuacptA9_ksR0vaSdv3EFujFq7kCvV_VknUDjh9t7V8ntZyi5CB2-D9_sVe6QdM7nGamn82Qra_pHtc0E1bDPqnZGRFhCZlH7lMon3wI-6XGO_Nrtv4gObHmSxok_G4-y3zkqUTGoRJ9fioIcYcZFLXnru1oMl4aUf9f3XiCsdva5naZaRwI9Gbt1JgAb26Fpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/010a765bc9.mp4?token=FqUNArvYgua6sjMjUpnYQEhlPIp41s9k1lwEo_xOZQJoaia8EsqnOz7D6paz8Ve5RSv_XVgGajZ_0X1AyZhIlXzd8po9NZCawPl4DSmG_2rSx0CYVIngaE-3iRtvO-hVn5j358erYBhd7XL36TfyXuacptA9_ksR0vaSdv3EFujFq7kCvV_VknUDjh9t7V8ntZyi5CB2-D9_sVe6QdM7nGamn82Qra_pHtc0E1bDPqnZGRFhCZlH7lMon3wI-6XGO_Nrtv4gObHmSxok_G4-y3zkqUTGoRJ9fioIcYcZFLXnru1oMl4aUf9f3XiCsdva5naZaRwI9Gbt1JgAb26Fpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد مناشدات عديدة من السلطات السعودية لحجب التوثيقات،مجموعة جديدة من المشاهد لنايا من مراسليها في الرياض والدمام
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/93620" target="_blank">📅 00:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93619">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">أعلن الفاتيكان عن تشخيص إصابة البابا ليو الرابع عشر، البالغ من العمر 71 عامًا، بسرطان الرئة. وأكدت الفحوصات التي أجريت أثناء الجراحة إصابته بسرطان غدي رئوي. وقد استأصل الجراحون الفص السفلي من رئته اليمنى في مستشفى جيميللي بروما. تكللت العملية بالنجاح، ولم تُسجّل أي مضاعفات.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/93619" target="_blank">📅 00:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93618">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صافرات الانذار تدوي في وادي الدواسر  والسليل في السعودية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/93618" target="_blank">📅 00:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93617">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/93617" target="_blank">📅 23:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93616">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/93616" target="_blank">📅 23:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93615">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0611040fa2.mp4?token=gbnV5SWJZcMaKLHRAnUX8gI5fH4mXT9eLc2o5PgXSYyaosO-1YoO5Sgb2bGkUNkM-ePemo0P0Z5jBUZTR3o9kn6wVpDSLulVMTUTxDjJP_uO_BFtR4hyVQMh50Fa-d0cIOBhNHDOAdyrhl0UmwNrMz3xv6E4QlTroQfXiUvJOJS9Gxgz4EclvxLM_gOAydVtSY1qroFFOP4GNSYBnA7CKr3MgPH9VH_jkzBZ_QQX9A5iCJW-PjOKCk8YhnMXoanfNXnwmX6Wyp9czUEWR42H8gpskxuWyCNCO2ZJ37axT5AH8RmJSd72dssjURfQEipKdjXQOnssZm8CFc1QlkstGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0611040fa2.mp4?token=gbnV5SWJZcMaKLHRAnUX8gI5fH4mXT9eLc2o5PgXSYyaosO-1YoO5Sgb2bGkUNkM-ePemo0P0Z5jBUZTR3o9kn6wVpDSLulVMTUTxDjJP_uO_BFtR4hyVQMh50Fa-d0cIOBhNHDOAdyrhl0UmwNrMz3xv6E4QlTroQfXiUvJOJS9Gxgz4EclvxLM_gOAydVtSY1qroFFOP4GNSYBnA7CKr3MgPH9VH_jkzBZ_QQX9A5iCJW-PjOKCk8YhnMXoanfNXnwmX6Wyp9czUEWR42H8gpskxuWyCNCO2ZJ37axT5AH8RmJSd72dssjURfQEipKdjXQOnssZm8CFc1QlkstGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ اليمنية تصيب اهدافها،اصوات انفجارات هائلة تُسمع في الرياض وسط السعودية
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/93615" target="_blank">📅 23:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93614">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اعتقال موظف بمستوى رفيع بوزارة التربية العراقية وسط العاصمة العراقية بغداد اثناء استلامه الرشوى .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/93614" target="_blank">📅 23:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93612">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227ecb5731.mp4?token=VbSmI6T2_K9vq1oU_79O4UWSUHc9Nw-i_6aMdskkHdyfeywC65W5HPO8XDmoY2TruY3_JJ9BAY3XGsSe2R6qy7vo8fhfVMsz5V86txDzcsNbCVcNt5xKTFT3axBpX94zGdTss4ugBMQS_duyp3dhaVqEgC3ID25biSoVRUHkebuZbXP0O_4VD2ik3mvJDC0hgx8CRGvnDRGVkKMO8p2fjtQyxZbohZFEp4uE2JxjyX1XdrxYy9sQoi4UosZgbtsWu_UGwUrDm-DD6IIpqbfWiDM2r-NjPVTJAVst9njSI3Hy6ZNLeklFnsUT2Y5of2EI7WrdH8JRfQ7XZRJVYJEu5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227ecb5731.mp4?token=VbSmI6T2_K9vq1oU_79O4UWSUHc9Nw-i_6aMdskkHdyfeywC65W5HPO8XDmoY2TruY3_JJ9BAY3XGsSe2R6qy7vo8fhfVMsz5V86txDzcsNbCVcNt5xKTFT3axBpX94zGdTss4ugBMQS_duyp3dhaVqEgC3ID25biSoVRUHkebuZbXP0O_4VD2ik3mvJDC0hgx8CRGvnDRGVkKMO8p2fjtQyxZbohZFEp4uE2JxjyX1XdrxYy9sQoi4UosZgbtsWu_UGwUrDm-DD6IIpqbfWiDM2r-NjPVTJAVst9njSI3Hy6ZNLeklFnsUT2Y5of2EI7WrdH8JRfQ7XZRJVYJEu5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد من انطلاق الدفاعات الجوية السعودية في العاصمة رياض.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/93612" target="_blank">📅 23:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93611">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇸🇦
🇬🇧
🔻
🇺🇸
إعلام أمريكي :
فشل ذريع آخر لقوات الدفاع الجوي السعودية الليلة! من المرجح أن يلقي باللوم على الولايات المتحدة وبريطانيا وفرنسا في ذلك!
‏وبحسب التقارير، فشلت أنظمة الدفاع الجوي السعودية باتريوت باك-3 وثاد في منع الصواريخ الباليستية الحوثية من ضرب أهدافها المقصودة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/93611" target="_blank">📅 23:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93610">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ee8793ee.mp4?token=sUfTP_MRmcH-VTJa-LphhfspkFSjo9JNob3CXce7GRiebIdKtQq523NNgQ8LH6254zcoIp2ysUVI3V6uacJ4B7lNWqo8ZSHWJ74oE3SEWoZMxueEK61SyhnVpi6rpv_1eI9l772dkeE93832e1uorEpAGqcKQwGk3mYAOlGnEQhQnfn2dFk0GUPzg6tKlB_EiaYkR0mVISj7huOqsk7X57ZO252BVhvXeA8ljniOBnpYoX3PS4yRuX0yZVEZiAaHvdzCimxGEVbEHNvW4GP7n4LYXce6CST6nbCTKNxle9vYnRXsEhldSx97Hi6ec0GXokUM8sCBF60Szz5D2ZyDRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ee8793ee.mp4?token=sUfTP_MRmcH-VTJa-LphhfspkFSjo9JNob3CXce7GRiebIdKtQq523NNgQ8LH6254zcoIp2ysUVI3V6uacJ4B7lNWqo8ZSHWJ74oE3SEWoZMxueEK61SyhnVpi6rpv_1eI9l772dkeE93832e1uorEpAGqcKQwGk3mYAOlGnEQhQnfn2dFk0GUPzg6tKlB_EiaYkR0mVISj7huOqsk7X57ZO252BVhvXeA8ljniOBnpYoX3PS4yRuX0yZVEZiAaHvdzCimxGEVbEHNvW4GP7n4LYXce6CST6nbCTKNxle9vYnRXsEhldSx97Hi6ec0GXokUM8sCBF60Szz5D2ZyDRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
صاروخ كروز رابع يستهدف الرياض.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/93610" target="_blank">📅 23:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93609">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇾🇪
ثلاثة صواريخ مجنحة تستهدف العاصمة السعودية الرياض.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/93609" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93608">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇸🇦
رويترز: تصاعد اعمدة الدخان من مقر شركة ارامكو في الظهران.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/93608" target="_blank">📅 23:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93607">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇸🇦
رويترز:
تصاعد اعمدة الدخان من مقر شركة ارامكو في الظهران.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/93607" target="_blank">📅 23:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93606">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇾🇪
مصدر لنايا يمني   الضربة الأخيرة تم استخدام سلاح جديد نوعي دخل للخدمة موخراً في ترسانة القوات المسلحة اليمنية .   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/93606" target="_blank">📅 22:56 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
