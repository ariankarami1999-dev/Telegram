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
<img src="https://cdn4.telesco.pe/file/AEtT6i2ibv15nY7YHNL6PJh8l4bOzoqNPlS510C03Hb2pKJ4WsTkbwGEO3o5E8KbzZ90NQKuHnxlxZZUS4cohKGoHhD8JXa1JyF9sRT8rXkMaA07KH8rlyHDmzC-MpVqA5i7BRmwYyTzRBYH9sUyzWpqPqCrvz5XUqzP_LxYRqoAF08CXHBYyQwnWo1Uz-7JtwoZxVeFLOZnSCYGUqzZ9SivXBF_4VBb_iDr6F8P3gL5c5gdh0SGJt0L32rb_t_8Unignp7Vr2ixmjW5Fyaoz1T0PgPD4h_satXK7jArkZ4hJUKcPiSsbckBBWqAQcK3CRouOi_dqHK1z0TGs9bouw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 260K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 22:41:20</div>
<hr>

<div class="tg-post" id="msg-78776">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpKzV2qKJy9c3EzVqLK0h1Ir3Coti5zCFsocF0JTq3x8gmGO90xZrPpLyUwZMvMbEygHDgH0LhTqHAj6FKuNnOXeXN4aHBvMUdtOxcty1LSKnnkck3-LqP7unk3s6oj_XJ_OV3YB6b44Dyu4QkXzDJ0wKDQ2Bnp-umgGWYwzmMRKZAG5zjAB3rEy1wo7vAYtq1vW5PUCBGdY9At8hLNjU3odpkHw0DeHkiNFsVnUgqiMT1UO19sGZfdgnfwNgwsVDWaQNmEO8wIWNAwdfDSeMBdA6HpxhXv5XKqIgnc4jAoE_XLGZLIJFt0915hVVTY8npc6Ce7ePzmz3tbBC6muXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف:
لن يتمكنوا أبدًا من السيطرة على أي جزء من قوات المقاومة بمفردهم؛ فجهود المقاتلين اللبنانيين الشجعان والدبلوماسية القوية للجمهورية الإسلامية الإيرانية ستضمن سيادة لبنان الحبيب ووحدة أراضيه، وستُحبط لعبة النظام الإسرائيلي المجنونة والمُثيرة للحرب.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/naya_foriraq/78776" target="_blank">📅 22:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78775">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
الغاء جميع الرحلات في مطارات غرب إيران.</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/naya_foriraq/78775" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78774">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
الغاء جميع الرحلات في مطارات غرب إيران.</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/naya_foriraq/78774" target="_blank">📅 22:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78773">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇶
المطار ملك للشعب العراقي
قرار سيادي عراقي بإبعاد الشركات الأجنبية والاستثماريّة بمطار بغداد والذي يعتبر واجهة البلد …</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/78773" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78772">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_NMdd4yqWTJeyG9dFMK4FbuVAvD4GCv4l3t-wegJoz7JkEEHOk2EfVOA6pHPyF2qkV_78T-0hRu09iBKhOZKi4h3wp9849B2TAr51nr8VfF8BNxKMpD5PvmGV6QMA5FHo08AR2c5e7-Eq2mZPkYWZwZCjKSWBKtDQXxwA7vFENvLjgzUPukh4sv-i92kYMgatD81zlf2eecW8TsBrkUuLGMbiEROx_T7t_v9npi4TnXI2ipeUMTOXTvbMVIEtOyfJyqkcYkRkshJCPOAhbObwui-Yvg4m2wkBhVT2tKmix16jYAi8NgzUA1bOxniZog5qEJkldRtugS_rmCA7g5Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
عدد قليل من الدوموقراطيين ضد FISA، مع أو بدون بيل بولت يذهب إلى DNI، كممثل. أي نوع من الصفقة هذا. إلى جانب ذلك، أنا ضد FISA إذا لم يأت مع قانون إنقاذ أمريكا (النسخة الكاملة!) مرتبط به بقوة. اجعل أمريكا عظيمة مرة أخرى! شكرا لك على اهتمامك بهذه المسألة.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/78772" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78771">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حدث خطير
عملية تجسس لصالح ايران داخل الكنيست الصهيوني</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78771" target="_blank">📅 21:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78770">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">السلام على شهلائي</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78770" target="_blank">📅 21:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78769">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78769" target="_blank">📅 21:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78768">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwEXE9fxla3R4S_ZPrKdt4l6gc8YTa7VO1VEIhfL0LRgATejr_NrwMQE79G4ppMFAO-WYpXkrGp3zOz8gbWeYl7O-cHq0FzoSk3Isn1-l1mo86WPuxdWkDMYuOKagXNBUL-UYP-rp8LnOVX07VKnNlVn4rzkPa7AArgBbHoYwg44GHQnKzrUvyrV_BMqpWdGgx02PfWXuiKE2z81EVUnIIup-8S3qTc1HfrX3h1-0v88-_awZOqG01nThFdMDAe-pVjfGPVKDmfP_z1r0N332lf8tXADgTMNFRSwvIsiKjrrX-W-xIP0XYW5YWVdw-X3rmHnTzYs-CDcvqP7oFnetA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/78768" target="_blank">📅 21:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78767">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P59O7TKbMLQJi3smsTlXx8TPWaJaNyiQXRLFLLaHetMGYImha3Jc3RzCTqgmI11hSghR4Cm5XyGrt5Oz5N4oDduSbovfuxNrM5QvGgN14jpY7iUUcwU-MAzIoJJcmn5q4uTF3ha8LPtEnMHnTnkIZfFtC-PeFllmEfy3nVytE-ghyf0AeC_hJmwQqL50kK7LhWKskU6AHstoKiSqr15XyAZfQ5of9xzlkhpNEveYANTxQdkRFYKCtVBwbsYaqQ-sCmujUl5DATTHV1dM1zi1OhDsaon6tpZ9Yzn647foeqgJgFO0rGKapgPWCzcMzdtXZXbRGOl-e-rxlywABoGiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
أمين المجلس الأعلى للأمن القومي الإيراني:
ردّ جند الإسلام قادم. ‏لقد شكّلت وحدة الصفوف سلسلةً أمنيةً لحماية المنطقة. ‏لبنان هو روحنا، ولن يُتسامح مع انتهاك الخطوط الحمراء للجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/78767" target="_blank">📅 21:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78766">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31ab1b676a.mp4?token=aWKVX32uElD10AOmblVOs9w7Nuk36PGQPwj966U9lSqMI75sy5eJMombeej6kq9rQT2e_iOGJeGRLXdqnYBaKXE6B-ezlR4mlrM0VC42SXmWUNuZLsTyC_roYu3xvyl3JplYzhGQgODcGmt_qXHkA1JqsZ_9Wi93ZQr7ybFVw4uanz49urrqS3Ho-xNFyslmM5YlJBp4Uvn2Rvkbft5B4fsY1Ar0htgOy-oBjh1XXv7S_26U7g-jrM_6fZritU7dSZRO-_vVB_8QVAvtQWxCzY9Y2YwpWfkmJg9GqpG8dN9JfOxOBiul1I2bNOrEq0I-pBckJ9yl6p_YzZvbjirzPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31ab1b676a.mp4?token=aWKVX32uElD10AOmblVOs9w7Nuk36PGQPwj966U9lSqMI75sy5eJMombeej6kq9rQT2e_iOGJeGRLXdqnYBaKXE6B-ezlR4mlrM0VC42SXmWUNuZLsTyC_roYu3xvyl3JplYzhGQgODcGmt_qXHkA1JqsZ_9Wi93ZQr7ybFVw4uanz49urrqS3Ho-xNFyslmM5YlJBp4Uvn2Rvkbft5B4fsY1Ar0htgOy-oBjh1XXv7S_26U7g-jrM_6fZritU7dSZRO-_vVB_8QVAvtQWxCzY9Y2YwpWfkmJg9GqpG8dN9JfOxOBiul1I2bNOrEq0I-pBckJ9yl6p_YzZvbjirzPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
عمليات قتل وتصفية لمواطنين سوريين على يد عصابات الجولاني الإرهابية تشهدها منطقة كفرتخاريم بريف محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/78766" target="_blank">📅 20:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78764">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee3f06f50.mp4?token=iJuPD7dWTHZPwo7IvOuFgp_734d8bY9H2ajlZl4qfz2wAo1XF7DFE9c0QM6EzkCoXGI3RoanFXyjl4hnjqYPZHULrFTxUApU7rEfYPLXkPQt85d1F_-wR5n2LU8PW0eBiCjRwYZIyVoeSv2KzGevcn0eZdJCevgVpKpI5QGYgOxI8sxBmh_jG49UOEXuixnt5JA8GLw6H7Os5y42qV_CDneZ6O03HDK8d3zbb1HfBGoLp3oPnIjR7JmAR_ukMGUnN4oIMSuB0wwOPo9vdRc33XQe-mKcutBV0KXM5ezcWP1nPdtNZ9U4NlgurfZNbVILvUg0PtXkxpE9BDEm8sTcBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee3f06f50.mp4?token=iJuPD7dWTHZPwo7IvOuFgp_734d8bY9H2ajlZl4qfz2wAo1XF7DFE9c0QM6EzkCoXGI3RoanFXyjl4hnjqYPZHULrFTxUApU7rEfYPLXkPQt85d1F_-wR5n2LU8PW0eBiCjRwYZIyVoeSv2KzGevcn0eZdJCevgVpKpI5QGYgOxI8sxBmh_jG49UOEXuixnt5JA8GLw6H7Os5y42qV_CDneZ6O03HDK8d3zbb1HfBGoLp3oPnIjR7JmAR_ukMGUnN4oIMSuB0wwOPo9vdRc33XQe-mKcutBV0KXM5ezcWP1nPdtNZ9U4NlgurfZNbVILvUg0PtXkxpE9BDEm8sTcBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
عصابات الجولاني الإرهابية تقدم على تعذيب وقتل مواطن سوري بتهمة الإنتماء إلى النظام السابق في منطقة كفرتخاريم ضمن ريف محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78764" target="_blank">📅 20:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78763">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh1h2PIpm_KeqUcEZ4eRmXMgWTXyoUhOaEPtdksA1yX1lqpz3LYfqQersumAw_ybgvvK2Fwug7lc3ZvIFDG20Uyi6-o4n9-ZMNwGHWeB7hGfDy6s3_Tu96so7OnlUsVpmJ2Z2kge_0CGlDUxZaF7_OADl0QAMIXYR9NN-h5y8T8IUntICgC7MnNq8n39wyuyVKyPFgS_KLLL6vhzUG3iif-qZRM1yoBiQKglOHK52gI1c8inndDQZulVbELj9_jOitfeE6Fymz9ywtkN0H4Xy7a0_PR-ojqdMQqh7kZB5SfZ8f9GY4mkjwe4DMlxKr32OQW9NAuOUS4t3pgyP9d-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف آلية لجيش الإحتلال الصهيوني في بلدة الطيبة بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78763" target="_blank">📅 20:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78762">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78762" target="_blank">📅 20:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78761">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
وزير الاتصالات مصطفى سند يعقد اجتماعاً مع الشركات المنفذة لمشاريع الـ(FTTH) ويطرح مشروع زيادة سرعة الانترنت للمشتركين بنسبة ‎%‎20 وبنفس السعر.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/78761" target="_blank">📅 20:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78760">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الإسرائيلي:
في أعقاب الإنذارات التي تم تفعيلها قبل وقت قصير في عدة مناطق في شمال البلاد، تم رصد سقوط إطلاق صاروخ عبر من لبنان في منطقة نواعت مردخاي، وسقوطات أخرى متعددة في المنطقة التي تعمل فيها قوات جيش الدفاع الإسرائيلي في جنوب لبنان.
بالإضافة إلى ذلك، قبل وقت قصير، تم رصد عدة سقوطات أخرى لأهداف جوية مشبوهة في أراضي دولة إسرائيل، بالقرب من الحدود مع لبنان.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78760" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78759">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In0xPgVM3hP-a5W6bjA3QJuqUUGw1cCz7AGQdI7qYNsQxNQgzNZQZwpdidtOxDsNlBahp_lmMM50qdOEHOtPe114cXacPpQCGhUbTroCZVrR4daAkqy2r5FVFllujw5vykLB2DSwscbvARW44uS9htPSPEkcipnAoOT02yr28YbW02zh2IADj59WmiKuxAzK63SYrhtrmziqg2szWKrJLqXsc25y4pAJaDYTep5iq9Mkt9QfoBg6r5qHQ4pxnSz5Y9S9nvCByEsooSNn1bHKZ1wgqwwyOV70njFI-L_DAQopK0epF3b9zNtI_LU0SPTxqBHUVrjNd5PEN6zZxvuxdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇺🇸
إيتمار بن غفير يتحدى ترامب ويطالب نتنياهو الإستمرار:
السيد رئيس الوزراء، كن قوياً وشجاعاً، ولا تخف أو تيأس.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78759" target="_blank">📅 20:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78758">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
وزير الاتصالات مصطفى سند يعقد اجتماعاً مع الشركات المنفذة لمشاريع الـ(FTTH) ويطرح مشروع زيادة سرعة الانترنت للمشتركين بنسبة ‎%‎20 وبنفس السعر.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78758" target="_blank">📅 20:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78757">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🌟
🇷🇺
ترامب أبلغ بوتين بأن الاتفاق مع إيران بات قريبا وبوتين أعرب عن ارتياحه لقرب انتهاء النزاع.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/78757" target="_blank">📅 19:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78756">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏ترامب: توقيع الاتفاق اليوم سيكون إلكترونيا وبعد أسبوع حضوريا في أوروبا.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/78756" target="_blank">📅 19:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78755">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامب: لا يوجد لدى بيبي أي تقدير أو حكمة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78755" target="_blank">📅 19:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78754">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b5cad09f.mp4?token=e8sVvN0jZuMDxDksQn9f3ogbwn4655GMgbAyr9wIw-78Z0AIefuhIM7C0tH_wz-u2APgDpZ4aKp_kU9I6ienYr-qsMRuLA9Okp4Wnfkg-H9FMm9j5nLFdZ4kcOSotbTAyt9ClAuZVa9FLKbWDcib1Qzyc3uDKAsXSJmq2VRmN2HcV7W_d_1Dlk5HGeyQZ1fmsfrp2okWDK3Lg0cRKZO3KG4Zwc7uaocqzw0wfcXWNR9sXNOCWHSUdUHz04XjjlLMDxZD91QQV0BcycBagx6XPVxF_vcxAfuyVhhg5XP4JJm2YQ67wSAnurAkqR5ceH1QziIzYNIgYcKHuw5LXfJNwpO1UNUzEr0amX0d-1ILvT3nerlXKlhtGRQ1wJK1F3VfwEa6JQ9sypFBwYnzcTTnXr2n5vh-df55GAss3cBVi8EF75d4oUkCpg8lt6WykVSm7IiZsq3QfPoL5rfLy7vm6Bmse5_XT0COLAw94hx_NWk7OJlbbNIf6AvbGKicYWGuu1Pvt9CHDhzjknMnv23zNvJsBqP5kDxasyj5i0zBzgX5uXU6_ongmRyiPH42Zbco2LOb26a6XkwCwzEMTC5-ud19Vd3GdhtbtqgZi7bjOnXyzncoKx5_SfdsCCH8gXEBi2AKTSF1hxISQil9iOFywGbb0khOWjlh9imj5P0AeOE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b5cad09f.mp4?token=e8sVvN0jZuMDxDksQn9f3ogbwn4655GMgbAyr9wIw-78Z0AIefuhIM7C0tH_wz-u2APgDpZ4aKp_kU9I6ienYr-qsMRuLA9Okp4Wnfkg-H9FMm9j5nLFdZ4kcOSotbTAyt9ClAuZVa9FLKbWDcib1Qzyc3uDKAsXSJmq2VRmN2HcV7W_d_1Dlk5HGeyQZ1fmsfrp2okWDK3Lg0cRKZO3KG4Zwc7uaocqzw0wfcXWNR9sXNOCWHSUdUHz04XjjlLMDxZD91QQV0BcycBagx6XPVxF_vcxAfuyVhhg5XP4JJm2YQ67wSAnurAkqR5ceH1QziIzYNIgYcKHuw5LXfJNwpO1UNUzEr0amX0d-1ILvT3nerlXKlhtGRQ1wJK1F3VfwEa6JQ9sypFBwYnzcTTnXr2n5vh-df55GAss3cBVi8EF75d4oUkCpg8lt6WykVSm7IiZsq3QfPoL5rfLy7vm6Bmse5_XT0COLAw94hx_NWk7OJlbbNIf6AvbGKicYWGuu1Pvt9CHDhzjknMnv23zNvJsBqP5kDxasyj5i0zBzgX5uXU6_ongmRyiPH42Zbco2LOb26a6XkwCwzEMTC5-ud19Vd3GdhtbtqgZi7bjOnXyzncoKx5_SfdsCCH8gXEBi2AKTSF1hxISQil9iOFywGbb0khOWjlh9imj5P0AeOE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 02-06-2026 جنود لجيش العدو الإسرائيلي عند الأطراف الشرقيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78754" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78753">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
🏴‍☠️
حزب الله يعلن عن استهداف دبابة ميركافا في محيط بلدة يحمر الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/78753" target="_blank">📅 19:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78752">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOCXRWqFAJ9AMORC6VyNfZDEDdyeqWv9-9mN9FkYRYgqn3kZGGNbGSBz-gaRV3aCtTdF4O-wNNdaiqxkdXgpG4IglQ1mZDcfyI9juK1wnn5tv8eNny31rYLNX7SfM1dHGAIYQzkQBbLaMDKj0SZ4NYKmIEIeGbC7olMaUARctAA0poYUb6nWEf_zDkv3WpIBVIxM3d0Tu9WMgUIf8O7gtzM65b7tRudgCqRU1EPwpelHUgOnelPmbwjw-VGg1SAEeVIVha5708iucilHAvoIv2jy1fpSy4BDlwsiiiC9jpkQ7JE1dIE-7pRUj9iiCXI5SWPm7vUjXKs28zxzY-BFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
إبراهيم عزيزي:
إن جريمة اليوم التي ارتكبها النظام الصهيوني في الضاحية تثبت مرة أخرى أن أمريكا ضعيفة وغير جديرة بالثقة، وأنها لا تملك حتى القدرة على السيطرة على هذا الكيان الزائف.
الجواب مؤكد، وقد قدمته جبهة المقاومة المتحدة.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/78752" target="_blank">📅 19:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78751">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامب: "اتصلوا بي وقالوا لي - سيدي إسرائيل تهاجم في بيروت - قبل ساعة من موعد توقيع الاتفاق. لم أصدق أن هذا يحدث. هذا سيء جدًا".</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/78751" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78750">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامب: أطلب من إيران عدم إطلاق النار تجاه إسرائيل</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/78750" target="_blank">📅 19:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78749">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامب: "اتصلوا بي وقالوا لي - سيدي إسرائيل تهاجم في بيروت - قبل ساعة من موعد توقيع الاتفاق. لم أصدق أن هذا يحدث. هذا سيء جدًا".</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/78749" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78748">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامب: لماذا قام بيبي بهذا الهجوم؟ حزب الله أطلقوا وأصابوا في وسط اللا مكان. لم يصب أحد. ثم عليه أن يقوم بهذا الهجوم اللعين وأيضًا في بيروت. هذا أغضبني جدًا".</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/78748" target="_blank">📅 19:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78747">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇺🇸
ترامب: تحدثت مع رئيس الوزراء الإسرائيلي نتنياهو، قلت له "ماذا تفعل بحق الجحيم".</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/78747" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78746">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/78746" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78745">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇸
ترامب:
تحدثت مع رئيس الوزراء الإسرائيلي نتنياهو، قلت له "ماذا تفعل بحق الجحيم".</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/78745" target="_blank">📅 19:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78744">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59874abc6.mp4?token=n2lgfPsr_-NXWjRGSOKfEw5plRy7MXQEG6lWJFdyctKUQyRTR23p68eQ0XKQ1EQCbl7qKn5qpc8xNKQ9dyfrI_RduRt5dxKbGaz9balJ5ZL9eGHs0XMP5-P7rU875M7tUsgSiuZEOnvuiL4S7kA_IToIVNcR2UD5V1vKphgeGj6vAHEh8bsJDuo2GhrgWX_76bDkVcvg0XfwoY_JgGQmwHeONfK5M2KcPFQlfT_oD0oUHrWj8-nZlvE5cDVHNE5Yn0z6DXD5hSayBCQn4u2SqPZLZstTpgb3PG_-GAXeRuUlut-RIU5MFLcOEXW_D5C0mZ-4HwAI03HNiHJKrenedw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59874abc6.mp4?token=n2lgfPsr_-NXWjRGSOKfEw5plRy7MXQEG6lWJFdyctKUQyRTR23p68eQ0XKQ1EQCbl7qKn5qpc8xNKQ9dyfrI_RduRt5dxKbGaz9balJ5ZL9eGHs0XMP5-P7rU875M7tUsgSiuZEOnvuiL4S7kA_IToIVNcR2UD5V1vKphgeGj6vAHEh8bsJDuo2GhrgWX_76bDkVcvg0XfwoY_JgGQmwHeONfK5M2KcPFQlfT_oD0oUHrWj8-nZlvE5cDVHNE5Yn0z6DXD5hSayBCQn4u2SqPZLZstTpgb3PG_-GAXeRuUlut-RIU5MFLcOEXW_D5C0mZ-4HwAI03HNiHJKrenedw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إطلاق رشقة صاروخية من حزب الله تدك كريات شمونة ومحيطها في الشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78744" target="_blank">📅 19:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78743">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
التفاوض لا يعني التنازل عن المبادئ، ولن تخضع الجمهورية الإسلامية الإيرانية لأي نوع من الترهيب أو الضغط غير القانوني. المفاوضات ليست سوى إحدى الوسائل لضمان المصالح الوطنية. وتسعى الحكومة في الوقت نفسه إلى اتباع مسارات متعددة لتعزيز الاقتصاد وتحسين مكانة البلاد.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/78743" target="_blank">📅 19:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78742">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: الارتباك في الولايات المتحدة:  ترامب ينتقد إسرائيل التي هاجمت الضاحية  وزير حربه يثني على الرد باعتباره متزناً  وزارة الخارجية تضغط على إيران لعدم الرد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/78742" target="_blank">📅 19:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
الارتباك في الولايات المتحدة:
ترامب ينتقد إسرائيل التي هاجمت الضاحية
وزير حربه يثني على الرد باعتباره متزناً
وزارة الخارجية تضغط على إيران لعدم الرد</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/78741" target="_blank">📅 19:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
مدير شركة سومو النفطية:
لم تستهدف أي ناقلة تحمل النفط العراقي خلال أيام التصعيد الأمريكي الإيراني.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/78740" target="_blank">📅 19:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ae956065.mp4?token=iOnz1jj5R2gZlu0-nD_IoBBCsrH8EbPeJbc9W6DXhMt_eV29dgULmNj0QXBR66caO24-gn1RhhEc1u9azmlfg4XKq-0dvVxMdaxsuHeG9s1Wg1zOHY1w2X3Lys1qJLCrrH27ILTxAGbhtDkpw1nh8_7iujIfnkQULXEfIphDUqTX1PuTBUuS1ewjEOWiKurkmX-K69j51ys0S3BQDdhItmX3elEcrn3VKjWYyrQGNA8vVJtBneaDOudURAyOSB343Ah2NPjsokRipT8ARoGtd_90rtwYWs-rF06AUQ1V7MPaBZHDLhz8ARPoRK4bi4GICLr7cCskolBq5v2sXtq4-iWWy3U4M5ixBLMl7pAF6_IdqJUXEVFJ5UxqP0mdtA6tkUbSsIh4Trs19QiP0rCqVlWbbeeyyTtqdK8v0NeCUvpxaaHPdndmazQHc9th6pF0akET8t99JYfYRkoMGwnrPns99Y6I8ZKNvBpcSKkQ7UCJbLjC6hC10LxHSy3ybSoB3cgD3BLiFdfElcA6NnLsvGZTcoV9-7FN3HVRxXTyKvH_OpE7HM-GcZFzBgtWNDe1GBm1OzdeKaqsZiozrx1CDDrCkwAVpWFEdC3iQYyVO6VTzWJqfSLogfq4RkwyxTg2In1M9ix8sDyjWPaPvo1EW5wG4_YHFS0JSmcLQtjKnCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ae956065.mp4?token=iOnz1jj5R2gZlu0-nD_IoBBCsrH8EbPeJbc9W6DXhMt_eV29dgULmNj0QXBR66caO24-gn1RhhEc1u9azmlfg4XKq-0dvVxMdaxsuHeG9s1Wg1zOHY1w2X3Lys1qJLCrrH27ILTxAGbhtDkpw1nh8_7iujIfnkQULXEfIphDUqTX1PuTBUuS1ewjEOWiKurkmX-K69j51ys0S3BQDdhItmX3elEcrn3VKjWYyrQGNA8vVJtBneaDOudURAyOSB343Ah2NPjsokRipT8ARoGtd_90rtwYWs-rF06AUQ1V7MPaBZHDLhz8ARPoRK4bi4GICLr7cCskolBq5v2sXtq4-iWWy3U4M5ixBLMl7pAF6_IdqJUXEVFJ5UxqP0mdtA6tkUbSsIh4Trs19QiP0rCqVlWbbeeyyTtqdK8v0NeCUvpxaaHPdndmazQHc9th6pF0akET8t99JYfYRkoMGwnrPns99Y6I8ZKNvBpcSKkQ7UCJbLjC6hC10LxHSy3ybSoB3cgD3BLiFdfElcA6NnLsvGZTcoV9-7FN3HVRxXTyKvH_OpE7HM-GcZFzBgtWNDe1GBm1OzdeKaqsZiozrx1CDDrCkwAVpWFEdC3iQYyVO6VTzWJqfSLogfq4RkwyxTg2In1M9ix8sDyjWPaPvo1EW5wG4_YHFS0JSmcLQtjKnCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
من يصرّ على العدوان والعبث بالأمن، فلن يجد إلا ردًّا يردعه. وإن لم ينسحب واستمرّ في غيّه، فسنمضي في تأديبه حتى يصبح خائفًا يترقّب، ويحسب لكل خطوة ألف حساب.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/78739" target="_blank">📅 19:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUWzaiJ1mmIGsCkvEROBxPRT6MWFbdQJ8pEQtKkWznNpDhvffT5CwPVmb2T3gcvCIGx8V1HoyXoI_bBmmeLMD2dsxeTvNlzVLpEnQmUSAGjMFInnMMt3YbIrww7w1_QLxAjNyBGsM_qBlQhPkjgl1tHpIJqQEWOt6f1uMTe6YiS4yZSwlrBP5ujLVCKj-iSJpRRP1wdzRth4xqpwX_1I01y63Bvqe55YDNECGo2o_wIP0xLJuGIDbxOD7UogiOEbxlvupKoBAg1NVS_m2uPsU_UWawA_b73iEo3EcZo4mNMs_LN7RlfOTzzi0qzxOTium4Nx8Dfi_m3a11r1RAgf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد قوة الجوفضائية في الحرس الثوري السيد مجيد الموسوي:
بسم الله الرحمن الرحيم
يا أيها الشعب الحكيم الغيور، الذي أُرسلتم لطلب دماء الإمام الشهيد، وعقدتم عهداً جديداً مع الإمام الحاضر في سبيل تحقيق المثل العليا للثورة الإسلامية، واستعادة كرامة إيران الحبيبة، تذكروا أن الطاعة ركنٌ من أركان الالتزام. فلا تتقدموا خطوةً ولا تتراجعوا خطوةً، كونوا مع وليّكم. وكما قال الإمام الخميني الجليل، رحمه الله: كونوا نصرةً لولاية الفقيه، فلا يمس وطنكم مكروه. استمعوا لأمر الولاية، وتجنبوا كل كلمةٍ تُهدد وحدتكم المقدسة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/78738" target="_blank">📅 19:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇸
‏مسؤول أميركي: استهداف إسرائيل في الضاحية محاولة واضحة لتخريب الاتفاق.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/78737" target="_blank">📅 18:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: بمساعدة قطر وباكستان ،يحاول الأمريكيون في هذه اللحظة منع إطلاق النار من إيران إلى أراضي البلاد.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/78736" target="_blank">📅 18:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78735">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: بلديات إيلات وتل ابيب الكبرى ونتانيا وحيفا تفتح الملاجئ العامة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/78735" target="_blank">📅 18:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78734">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
بلديات إيلات وتل ابيب الكبرى ونتانيا وحيفا تفتح الملاجئ العامة.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/78734" target="_blank">📅 18:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78733">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⭐️
طيران مسير من لبنان يهاجم مستوطنة عرب العرامشة بالشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78733" target="_blank">📅 18:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78732">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الإسرائيلي:
قبل وقت قصير، تم رصد عدة سقوط لأهداف جوية مشبوهة في أراضي دولة إسرائيل، بالقرب من الحدود مع لبنان. الحدث قيد التحقيق.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/78732" target="_blank">📅 18:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78731">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وزير الحرب الامريكي يتعرض للاحراج مجددا.. وزير الحرب: الرئيس ترامب هو من أجبر إيران على إبرام هذه الصفقة.  الصحفية ‏مارغريت برينان: لم نصل حتى إلى مرحلة مذكرة تفاهم!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/78731" target="_blank">📅 18:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78730">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97f97793b.mp4?token=BG5sJK3uxngoLyIH-2vQe8U4qtzJFdL9_-ZLXw8g-8Zb4HeaUo2dinuILVnuLa4nd1_-rY4Oup8T8_H8RqRAyoV548rdhWbG0jB-RfbbAfZtVR8jAGHZCSfCUek0RaO9r7O2Ogdm8o7e8FYvZZ_KFmY08RrwvHmrVEvCwPcokhKLSkw9SvCIX97RRZY5MpIDS61pN_KGsRReTSA82xSvNgGzwfv9v1Pc1Xbdt6kDzn6a01MXA_yS1QLoasD4d830ZwhLi2cnaBR_Ny_SvQl0HBiP9Sx5Bw-qEnMvGk53jXjWCzd3rsM9q-IB4aNH9UBwjwAzsdFM1CwBabzJ2NYX7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97f97793b.mp4?token=BG5sJK3uxngoLyIH-2vQe8U4qtzJFdL9_-ZLXw8g-8Zb4HeaUo2dinuILVnuLa4nd1_-rY4Oup8T8_H8RqRAyoV548rdhWbG0jB-RfbbAfZtVR8jAGHZCSfCUek0RaO9r7O2Ogdm8o7e8FYvZZ_KFmY08RrwvHmrVEvCwPcokhKLSkw9SvCIX97RRZY5MpIDS61pN_KGsRReTSA82xSvNgGzwfv9v1Pc1Xbdt6kDzn6a01MXA_yS1QLoasD4d830ZwhLi2cnaBR_Ny_SvQl0HBiP9Sx5Bw-qEnMvGk53jXjWCzd3rsM9q-IB4aNH9UBwjwAzsdFM1CwBabzJ2NYX7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحفية تحرج وزير الحرب الامريكي.. وزير الحرب: لقد سيطرنا على مضيق هرمز طوال هذا الوقت  ‏الصحفية: أنت تتفاوض معهم لإعادة فتحه!</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/78730" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏴‍☠️
‏
الجيش الإسرائيلي:
بعد تقييم الوضع، تقرر تغيير سياسة الدفاع لقيادة الجبهة الداخلية ابتداءً من اليوم (الأحد)، 14 يونيو 2026، الساعة 18:00 وحتى يوم الاثنين (الاثنين)، 15 يونيو 2026، الساعة 20:00.
‏وكجزء من التغييرات، تقرر السماح بالنشاط الكامل مع حد أقصى للتجمعات يصل إلى 5000 شخص في جميع مناطق البلاد باستثناء خط المواجهة.
‏في منطقة خط المواجهة - نشاط جزئي، دون تغيير في التعليمات.
‏تواصل قيادة الجبهة الداخلية إجراء تقييمات مستمرة للوضع. وفي حال حدوث أي تغييرات في السياسة الدفاعية، سيتم إطلاع الجمهور على آخر المستجدات عبر المنصات الرسمية لقيادة الجبهة الداخلية والمتحدث الرسمي باسم الجيش الإسرائيلي.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/78729" target="_blank">📅 18:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78728">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qN1ixfUiPy8za-EI4cYWj7cMphU224QbKcYaizzD4jlmasIoUB0zuck_h7aTxXJtouL7CRWjWa4U5FvXeakTXssL26kG0HlYjHkq8UYmazok21Igl16Za7uE7i7v4HhQUgjMtt1Ry00EzFnhsrP_S9sJv679E-vBQBdTC29yc8BcrcvZyrJEtB2UeMltl0SbFVAvgKsbLCA-mKuAtq7DYnhw0dFJWP0OqmTcqO02_B1HwgYHdsO5mKbIyXJLuJGPL1g0uE9whTB1Azwx59pOh5nUCpJDysk60Vwme_mvkIAbTi_UMYIFPocXmPI32OVcMYEfvqPv7CbLYXPcqi5WnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب:
كان ينبغي ألا يقع هجوم بيروت هذا الصباح، لا سيما في يوم مميز ونحن على وشك التوصل إلى اتفاق سلام مع إيران. لإسرائيل الحق في الدفاع عن نفسها ضد التهديدات، لكن الهجوم الذي ردت عليه كان محدودًا للغاية وغير ذي أهمية، ولم يُصب أحد بأذى أو جرح أو قتلى، ولا ينبغي أن يعرقل هذه العملية المهمة. نحن على وشك التوصل إلى اتفاق من شأنه أن يحقق السلام في المنطقة، بما في ذلك لبنان، وعلى جميع الأطراف أن تقف down. يجب ألا تكون هناك هجمات أخرى من جانب إسرائيل في أي مكان في لبنان، كما يجب ألا تكون هناك هجمات أخرى من جانب أي طرف آخر، بما في ذلك حزب الله، ضد إسرائيل. قد تكون هذه بداية سلام طويل وجميل - فلنحافظ عليه! شكرًا لاهتمامكم بهذا الأمر. الرئيس دونالد جيه. ترامب"</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/78728" target="_blank">📅 18:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78727">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a1ae25e1.mp4?token=TA9QM0mM-j_P3nOf6m-WsOxNslWdNe_U63GTfDKJrGMIEE6m8voJTCCReCiDTLxV8bg3xcMwq9ymGFw0NwAIJN-U9KR2jlbY7Itb7gHs31dq2aI0awFaF9Ddg9KqR30u7IMro4edaq2vOH9oqGpUO0G8cbBKjIvHD3FJBAO9h0ES9HbMUa4gUIB4WUgRngYK3NOAh_vaO1lsdnSjjgcpv8ypBwpd1Q-prYqz6qK-HKV5y6Q1jQE0Bzg87rQ2K2VluDXA-ZwjCyxtMVHdlIyLGSGVbFBSJGHX9XaVCk4nB3FKTuLDEhoGdwXgw9IqJUqAXe1Ik8GZB8oknKi0cJpRCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a1ae25e1.mp4?token=TA9QM0mM-j_P3nOf6m-WsOxNslWdNe_U63GTfDKJrGMIEE6m8voJTCCReCiDTLxV8bg3xcMwq9ymGFw0NwAIJN-U9KR2jlbY7Itb7gHs31dq2aI0awFaF9Ddg9KqR30u7IMro4edaq2vOH9oqGpUO0G8cbBKjIvHD3FJBAO9h0ES9HbMUa4gUIB4WUgRngYK3NOAh_vaO1lsdnSjjgcpv8ypBwpd1Q-prYqz6qK-HKV5y6Q1jQE0Bzg87rQ2K2VluDXA-ZwjCyxtMVHdlIyLGSGVbFBSJGHX9XaVCk4nB3FKTuLDEhoGdwXgw9IqJUqAXe1Ik8GZB8oknKi0cJpRCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي  وزير الحرب الأمريكي: رد إسرائيل على حزب الله اتسم بضبط نفس كبير إدراكا بأننا على وشك التوصل لاتفاق.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/78727" target="_blank">📅 18:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78726">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الأمريكي: لا أتوقع أن تعرقل ضربات إسرائيل على الضاحية الجنوبية لبيروت الاتفاق مع إيران، إذا أرادت إيران لهذا الأمر أن يصمد فعليها كبح جماح حزب الله</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/78726" target="_blank">📅 18:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78725">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الأمريكي:
لا أتوقع أن تعرقل ضربات إسرائيل على الضاحية الجنوبية لبيروت الاتفاق مع إيران، إذا أرادت إيران لهذا الأمر أن يصمد فعليها كبح جماح حزب الله</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/78725" target="_blank">📅 18:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78724">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اعلام العدو: حدث امني في جنوب لبنان</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/78724" target="_blank">📅 17:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78723">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اعلام العدو يقول ان
اسرائيل
تتجهز لضربات صاروخية ايرانية بدءا من بعد الساعة 6:00 مساء وربما من اليمن أيضا</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/78723" target="_blank">📅 17:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78722">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اعلام العدو:
حدث امني في جنوب لبنان</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/78722" target="_blank">📅 17:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78721">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دويلة الكويت تسحب الجنسية من 2193 شخصاً وعن كل من أكتسبها بالتبعية من هؤلاء الأشخاص</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/78721" target="_blank">📅 17:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78720">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اعلام العدو:
تعليمات داخلية لمعظم التجمعات في شمال ووسط البلاد تجهيزات لتلقي صواريخ من إيران بالوقت القريب.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/78720" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78719">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇷
وكالة فارس عن مصادر:
- يتواجد فريق قطري حاليًا في طهران، وتقوم إيران عبر هذا الفريق بنقل بنودها المطلوبة، بالإضافة إلى التفاصيل الدقيقة التي تنوي تضمينها، إلى الطرف الآخر.
- لم يتم التوصل إلى اتفاق نهائي بعد، أن مسار المفاوضات يتسم بالتقلبات، حتى لو شهدنا جولات متضاربة في عملية التفاوض، فإن الشرط الأساسي لإيران هو أن تُؤخذ جميع بنودها بعين الاعتبار بشكل كامل في نهاية المطاف".
- حتى لو تم تنفيذ جميع آراء إيران، فلن يتم توقيع أي اتفاق بشكل قاطع عند إعلان ترامب
- تجدر الإشارة إلى أن هذه التصريحات صدرت قبل الهجمات الأخيرة التي شنها الكيان الصهيوني على الضاحية الجنوبية</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78719" target="_blank">📅 17:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78718">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🏴‍☠️
المتحدث باسم جيش العدو:
في أعقاب الهجوم في بيروت، يجري رئيس الأركان تقييمات مستمرة مع جميع القادة المعنيين. وفقًا لتقييمات الوضع، نستعد لاحتمال إطلاق نار باتجاه أراضي
دولة إسرائيل
في الساعات القادمة. نواصل الحفاظ على الجاهزية واليقظة لمجموعة متنوعة من السيناريوهات في الدفاع والهجوم ولن نتسامح مع إطلاق النار باتجاه أراضي
دولة إسرائيل
.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78718" target="_blank">📅 17:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78717">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
رفع حالة التأهب في إسرائيل خشية إطلاق صواريخ من إيران.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78717" target="_blank">📅 17:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78716">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 05-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة
أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78716" target="_blank">📅 17:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78715">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🏴‍☠️
وزارة الخارجية الصهيونية:
النظام الايراني الذي يهددنا يكذب. حزب الله هو من هاجم إسرائيل. لن نتحمل إطلاق النار على أراضينا.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78715" target="_blank">📅 17:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78714">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اعلام العدو عن
تقييم أمني اسرائيلي
: إيران ستطلق صواريخ من أرضها تجاه إسرائيل.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/78714" target="_blank">📅 17:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78713">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
‏
أوباما عن الحرب الامريكية على ايران:
إنه تذكير بأنه في العديد من مشاكل السياسة الخارجية المختلفة، قد تبدو فكرة أنه يمكننا ببساطة استخدام الترهيب أو القصف للوصول إلى حل جذابة في بعض الأحيان.. قد تعتقد أننا تعلمنا هذا الدرس الآن، ولكن يبدو أننا نضطر إلى تعلم هذا الدرس مرة أخرى بين الحين والآخر</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78713" target="_blank">📅 17:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78712">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رئيس الأركان الصهيوني:
نتابع من كثب ما يجري مع الحفاظ على أعلى درجات اليقظة والاستعداد في جميع الساحات، لبنان هو مركز الثقل الرئيسي لكننا نستعد لاحتمال تطورات في ساحات أخرى.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/78712" target="_blank">📅 17:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78711">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">طيران مسير من لبنان يهاجم الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78711" target="_blank">📅 16:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78710">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏴‍☠️
نتن ياهو:
هاجمنا أهدافا تابعة لحزب الله في الضاحية الجنوبية لبيروت ولن نتسامح مع إطلاق النار علينا</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78710" target="_blank">📅 16:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78709">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🏴‍☠️
نتن ياهو يلغي مشاركته في مراسم ما يسمى بـ"اتفاق السقف" في مستوطنة كرني شمرون بمشاركة سموتريتش بسبب التطورات الامنية وخشية رد ايراني.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78709" target="_blank">📅 16:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78708">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQF24MUODfzFwvzCiCQ_FQHB8nf5e3C-PUkxXrTQxumQOq92o6YNrGQ-N48ylcMKv0v6GqAlS7WjKlljJg6LXmk-O08cCCUAFqQxIbf0k1nl2g0i8yi1Q_dSQ0tJW9whpViDlxJ_KVJfJ5R50o-bTl8F9ddbyNG9RKc2BH6F0M6Ph-komKyCxFnaH2KIO0Bl27k0u_QihiFdvM7SxXKq2u9DbM7YdXfF2VROFY_yGvxBCA2tmSbcX-j_q4LP4i_l8b2gqt3s98nXYoEg9QiyDd09QPPPRw-YP3fRD5z_vJVc-vKITMZouLMc2pG11d8_jhqSguhhuIHd0k3WT5_Eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توجيهات حكومية بإيقاف كافة المشاريع الاستثمارية الخاصة بالسكن في العراق وايقاف منح اجازات الاستثمار للمجمعات السكنية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/78708" target="_blank">📅 16:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78707">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">طيران مسير من لبنان يهاجم الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78707" target="_blank">📅 16:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78706">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📰
فوكس نيوز عن دبلوماسي مشارك في المفاوضات:
هجمات بيروت اليوم تُعرقل إتمام الاتفاق. هذه محاولة إسرائيلية واضحة لتخريب اتفاق الرئيس وجر الولايات المتحدة إلى الحرب مجدداً.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78706" target="_blank">📅 16:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78705">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIsXSwPjKMDKfAL6s0t_p2_nhIhdgSV62zhXiKdFRXmjPzFtxEjSrgAAdMCleNMCwn3YVGfi1ZQU_wQPDWH_dKvZ7BK04IA-pNV5CkN_mkmJOOR0x82HDZMZiOICTRDoMHt79vqym-qQZ5RxEYGn6YuyM3c0reWWSNl1yuXnN_5xb3XdliRF40CWwgQX-3p-gyGK10ozpRPy5NUx194zNRsSmH7R04Khsskftr46unsa9DcLH-gaVCwLCMPP-3Ti_dQNKQEIq6e21tv3qgbhIrofnw5ijlXo0_hXt71PZqpj8JwmPu5macTfiDwIkbCazbwn_ktL4P5nyIl0-xinpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف:
أظهر العدوان الصهيوني على الضاحية مجدداً أن أمريكا إما تفتقر إلى الإرادة للوفاء بالتزاماتها أو تفتقر إلى القدرة على ذلك. لا يمكن كسب أي نقاط بمنح الكيان الضوء الأخضر.
لعبة الشرطي الطيب ضد الشرطي السيئ أصبحت قديمة.
إذا لم تكن لديك الإرادة والقدرة على الوفاء بالتزاماتك، فلا يمكن الحديث عن الاستمرار في هذا المسار.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78705" target="_blank">📅 16:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78704">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 10-06-2026 تجمع جنود وآليات جيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78704" target="_blank">📅 16:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78703">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6veotxl7dB3RyP7DQgOQ9sO5g61-hf9D5Pt8zNM5eTBV46Xh-NH6Ufa6SfvbvdxHsa_PynqygysJ2XXMb5XTz8qeGfItFM5zOrg6_bhm_LHs4tMUQm-bunUcWtflrokWwmgoLl1XH7RMwBSaipe98I1YkZZSas8IQxJuO3JPOwWfUvA2G0NRduZoVNwdFOz9KO-jId-QBisEkSET-WSfl9XmB7Cm0ldUEU7NwZLx3UrCNvUJFDbmRdjzTMN0EvZ6ANW8LxTZzHbQWEummIHHGjDVlAjtZOtNBLp-HbQOiBYv6TW0shQu0eBznvgcoE6hfdaGTh0zPoIrO0rrgysLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میشه یه آمریکایی با شرف باشی،
‏میشه یه ایرانی بیشرف باشی!
‏شرافت ملیت نمیشناسه...</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/78703" target="_blank">📅 15:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78702">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏴‍☠️
🇺🇸
‏
مسؤولون إسرائيليون:
أبلغنا أميركا قبل تنفيذ ضربات الضاحية الجنوبية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/78702" target="_blank">📅 15:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78701">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdY6-EF4YRAKozLJlZAtxZsF0ofOW0IaX7FL3KJ_sJ8dtX_b3YA-WVVbYyyrnjQxiaQsZEkxQDG7K9PngatSI91SI49XNxq4Z1Fol49oQBltjv-p5m8a9QfS2bo7Le2OssyYMBSXO6u7jcKaSbGDDv434O7AcczipL8XJ56K9RMz1SEkekZjVTDWsEUdzDupkN68kvofhXepY_92fDAWJMZcrmMGZb0tf7VaK1nr69hWkWfL5WE15cPpMnfhZHr1L5WRTcFRCE9i7M4DZfrAN1giSd-oQPy7PG5dVnndBVqBCFGGfJl1HOE9fQdMH0sXrqkXG3eiL8dKe8rR8HymJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لا يمكن المرور على موسى الدقدوق او نعيه كمقاتل او قيادي عادي او ذكر جيفارا او اي مقاتل اممي آخر دون تذكار فارس العبوات الارتجالية ومهندس المجاميع الخاصة و كاسر هيبة الجيش البريطاني بالبصرة وتلميذ عماد مغنية وفيلسوف نظام حرب الشوارع بأزقة شوارع الداخل والگيارة وسوگ العورة ورفيق سجون الاحتلال هاشم الحاج ابو الاء و قيس الشيخ الخزعلي و عدنان الشيخ الحميداوي وموسى الدقدوق ؛ نحن ننعى باختصار فترة الزمن الجميل ولابأس ان نسير قليلا نحو دور اكرم الشيخ الكعبي بإخراج الدقدوق من اقبية بوكا نحو حادثة النادي التركماني و تحديدا بناية الحاسبة المالية في شارع فلسطين يوم خلعها اكرم كما يخلع الأسد الصغير من لبوتها .. وداعا يا دقدوق ولك منا سلاما حيدري بطعم لبيك يا ثار الله وإنا لله وإنا إليه راجعون</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/78701" target="_blank">📅 15:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78700">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حزب الله يشن هجوم صاروخي على كريات شمونه شمالي الكيان</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/78700" target="_blank">📅 15:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78699">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏴‍☠️
الجبهة الداخلية الصهيونية:
رفع مستوى التأهّب إلى أعلى درجة من دون أي تغيير في التعليمات الموجّهة للجمهور حتى الآن.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/78699" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78698">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سوالف الگهوة
وزير الداخلية الباكستاني يتصل بالحكومة العراقية !!!!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/78698" target="_blank">📅 14:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78697">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اعلام العدو:
بعد قصف الضاحية الجنوبية لبيروت ضغوط مكثفة من قطر وباكستان لوقف جولة أخرى من القتال والتي من شأنها أن تُفشل المفاوضات</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/78697" target="_blank">📅 14:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78696">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 13-06-2026
نقطة لوجستيّة تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/78696" target="_blank">📅 14:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78695">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b7b68c3b.mp4?token=Z8JxFv7La7xwOfEjqKC-eRogPRJIOYTWDtskdBgcgUheEzW6zLpaL4XaVEH47QhRDiQ-yfSapMVTxY2SCqnejnZqCQDtWiZnyhEqLLLbqoCd2Qr7LDkFlRdOR6AhDn-atWLT-rtT2Om8q17Zf_LgFYJkH2U-GxZK9Kk0JpNSWyM8_GxzojAeb1_xPflmQsnmQCFl7lPd-kqM_QKN7oGYwbwUkmX9vv6K1Y7cc2josWgqB3gto6s_jwPcUSoL5wwp4DkJRA35Al6aKKFqhYMA5TvNyIIUEtWOFqkWVk9783MsKW5Z-9WCt-k2NauTPevNzY1_MGF97wXVxWmFzKMiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b7b68c3b.mp4?token=Z8JxFv7La7xwOfEjqKC-eRogPRJIOYTWDtskdBgcgUheEzW6zLpaL4XaVEH47QhRDiQ-yfSapMVTxY2SCqnejnZqCQDtWiZnyhEqLLLbqoCd2Qr7LDkFlRdOR6AhDn-atWLT-rtT2Om8q17Zf_LgFYJkH2U-GxZK9Kk0JpNSWyM8_GxzojAeb1_xPflmQsnmQCFl7lPd-kqM_QKN7oGYwbwUkmX9vv6K1Y7cc2josWgqB3gto6s_jwPcUSoL5wwp4DkJRA35Al6aKKFqhYMA5TvNyIIUEtWOFqkWVk9783MsKW5Z-9WCt-k2NauTPevNzY1_MGF97wXVxWmFzKMiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء عن غارات على الضاحية الجنوبية لبيروت</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78695" target="_blank">📅 14:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
في أعقاب هجوم بيروت: يستعد الجيش الإسرائيلي للتصدي لأي تهديدات من إيران</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/78694" target="_blank">📅 14:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78693">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
بالنظر إلى آخر بيان صادر عن مقرّ خاتم الأنبياء المركزي بشأن اعتبار استهداف الضاحية الجنوبية لبيروت خطاً أحمر بالنسبة لإيران، يُتوقّع أن تشنّ إيران هجومًا على إسرائيل في وقت قريب.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/78693" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اعلام العدو:
أهمية الحدث في لبنان، أن إيران هددت سابقا بالرد على أي هجوم إسرائيلي على بيروت.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/78692" target="_blank">📅 14:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78691">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الشقة المستهدفة في الضاحية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78691" target="_blank">📅 14:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXENSf1Vf09qxd-YEeXm6c-kLlPtA0m9hHlj79i79R5cYocxvJLZDGpqYhVTLe2fnZzZWS8N9LdQb12u51McIVF7kTKNgC6yFVKY7Sj5xD2w9UkzwEDxyVeB1tDKvPkzivmIy6n_yoB8CwcYYmOdQrrNdKAH-FKnHF2yoq0_FPC7lauTfOlicwlLpNKfCbItOJzz79UgQUFzxuMFXghqGYEp37u_PZCVTy1rDDizN0rjL3O9pXncn2e3feV2mV92kAJpQArJXvzNwQtBUwkiils27slrytZUDWyUKpWS6BqzSnToNotNdqBmnc95JlNOlCvk1rz0rHhDGxORtrQ4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مكان الغارة في الضاحية</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/78690" target="_blank">📅 14:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78689">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f57c16e8.mp4?token=U3GeaKV3A6Z7HbncT8GhXr-EmH0ck85-KKltlv9b12XiDjAw5AzNlA74di6j4tyaiANqwp76mNplLpj6K1nLcOWsu2LXOdtToxWvzzh4OsHA14JO_gh_ioS8IB6NDu-4R2-F4DnGmasrJXrEUBzD1UoR1CtJwvpOEw9xgP42WUcOnI4Yf67v86u3A9QYEwwX6KZnju7mGl0JRqkyJI18q2KavQPRz8Po3fYLNQsi2Z1Ds8TP_4Fe0YQW_b7PwPVhW-I4ziimdlmebsOWmsKAPztxSe09GbvuDy8duWtrESr2JgkPV0osLSolNPc1B-ANGhxZB-OkldC68ZKbIx4RVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f57c16e8.mp4?token=U3GeaKV3A6Z7HbncT8GhXr-EmH0ck85-KKltlv9b12XiDjAw5AzNlA74di6j4tyaiANqwp76mNplLpj6K1nLcOWsu2LXOdtToxWvzzh4OsHA14JO_gh_ioS8IB6NDu-4R2-F4DnGmasrJXrEUBzD1UoR1CtJwvpOEw9xgP42WUcOnI4Yf67v86u3A9QYEwwX6KZnju7mGl0JRqkyJI18q2KavQPRz8Po3fYLNQsi2Z1Ds8TP_4Fe0YQW_b7PwPVhW-I4ziimdlmebsOWmsKAPztxSe09GbvuDy8duWtrESr2JgkPV0osLSolNPc1B-ANGhxZB-OkldC68ZKbIx4RVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من مكان الغارة في الضاحية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78689" target="_blank">📅 14:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78687">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JPsbSnNbijHZ4DLscxIlyILF5UlizexIYJuL3EXaOVm1n-ubdiggFSd5c2xYR6YmfMJK5GxveTM9IpHzpO3zxc-gURpDBMkIF4sHuG-PYlOzMQ3zFkYxW3x0Q4E9BSeI-yuBdkimjgF1qcGm7nQxAZfB13vHiLEvujC4Y1x9YqmiWKpgp8TuepaNHpl4aOidTGLHWSEVKJjJgGuRnpusQ3YInl71zXSgfIlDYuCwV6M2CblrRGm7F5-Lw0gKEnM5xcIMt4LIrtKgnBXOfMUctmKh1aQJcLBhAQ1MCcjUd1vCEJ9suXYXrv91q9uG75cx-orYbWdl9CtC5vws1Zw2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZy1ybmEI6lg0JCS5F8L8sOfXpFGIobiEELDDNNbVJ_-StZdRAbbQ-Mgvf6MtkSZic69xK0Bf-mwLsYB1marSSyI7hX7IQ2t7fgxPTD2UP4ikXLnY_bMzDNcdeYB7jPKo6ZUWBRVK0Erb8hFSVj-A1J79FkyuRjX88WIrsoSfwi5td08bpb5tPHTIb3mrM3dj16QY8-iBXHZr7MggzvNYOcwQ1EiW6HXPCFCpmaGGD15KEuVOzlRmgwsRDqi7m7z7BqOf_03V74v4ptNKIv36IpN_xUhFKq1UaKqpO3F2B8rz3kjGxwmped3swb9iw9cLS09Lf4F-y2RtCHqVDJTVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴‍☠️
بيان مشترك للنتن ياهو وكاتس: يهاجم الجيش الإسرائيلي الآن أهدافا لمنظمة حزب الله في بيروت ردا على إطلاق حزب الله النار على الأراضي الإسرائيلية. لن تتسامح إسرائيل مع إطلاق النار على أراضيها</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78687" target="_blank">📅 14:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78686">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جيش العدو يهاجم الضاحية الجنوبية</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78686" target="_blank">📅 14:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78685">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgQsef7EarlkDfl4aDRJz1xWo1xivIOTxRAQtQ8lmawj7TwRLTsNhiYhaoO8qFZf0LOJqY43lETtaFjJMshvGxtKtAxLdfnOCY7qTd0ZmPX0azPe0kH9lNummsLMXf_RSQYUPMBK0sZCUAn7VLVHJJM78yU1TwFh2VKyylG3mVs_SqYVTrWikXlsQNH8awySCCpbfgd8xCRmkqkodjr4ecZrJWMZPMR0qyPABMC8j_DZ4YyjGiquB39cOM7PUxGGELI1zvYw57kSEVp0oiIYoQXye5EhZktssFleEDsGRAJHIWQZkYhLJ3kN_HLqopuRxQeONbCcCNBGyKUX8wqkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انباء عن غارات على الضاحية الجنوبية لبيروت</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78685" target="_blank">📅 14:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انباء عن غارات على الضاحية الجنوبية لبيروت</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78684" target="_blank">📅 14:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78683">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">📰
مسؤول إيراني كبير لوكالة رويترز:
في إطار مسودة مذكرة التفاهم، توافق الولايات المتحدة على الإفراج عن 25 مليار دولار من الأصول الإيرانية المجمدة، من بين أمور أخرى من خلال تحويلات مالية مباشرة، وتعاون بين دول المنطقة، وخطوط ائتمان مالية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78683" target="_blank">📅 13:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صافرات الإنذار تدوي في غلاف غزة</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/78681" target="_blank">📅 13:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78680">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزارة الخارجية اللبنانية:
تقدمنا بشكوى إلى مجلس الأمن ضد إسرائيل لاستهدافها آلية عسكرية للجيش واستشهاد عسكريين ولرشها مبيدات الغليفوسات فوق قرى جنوبية حدودية.
تقدمنا بشكوى وسنواصل التفاوض المباشر معهم
😄</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78680" target="_blank">📅 13:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78679">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
مهدي محمدي، المستشار الاستراتيجي لرئيس فريق التفاوض يكشف عن تفاصيل مذكرة التفاهم الإيرانية الأمريكية
- في الخطوة الأولى، يتضمن جدول الأعمال وقفًا تامًا للعمليات العسكرية ضد إيران ولبنان، ومنع أي عمل عسكري جديد. كما يتعين على الجانب الأمريكي تقديم الضمانات اللازمة لمنع تجدد التوترات
- بناءً على الإطار الذي نوقش، سيتم الإفراج عن جزء من الأصول الإيرانية المجمدة مع بداية تنفيذ الاتفاق، وفي الوقت نفسه، ستبدأ عملية تعليق بعض القيود والعقوبات الاقتصادية للسماح بزيادة التبادلات الاقتصادية ومبيعات النفط.
- يُعدّ تسهيل حركة السفن التجارية الإيرانية وتخفيف القيود البحرية أحد المحاور الرئيسية للاتفاق. ويهدف هذا البند إلى إعادة التجارة البحرية الإيرانية إلى وضعها الطبيعي وإزالة العقبات أمام النقل الدولي.
- لا تتضمن المرحلة الأولى من الاتفاق، في النص قيد التفاوض، القضايا النووية. ووفقًا لهذا الإطار، يجب أولًا تنفيذ الالتزامات الأولية للطرف الآخر والتحقق منها، ثم تنتقل المحادثات بشأن القضايا النووية إلى المراحل التالية.
- في المرحلة النهائية، تمّ النظر في رفع العقوبات الأمريكية الأولية والثانوية، فضلًا عن توفير آليات للتعويض عن الأضرار الناجمة عن الحرب والضغوط الاقتصادية وإعادة إعمارها. ويُعتبر هذا البند من أهم مطالب إيران في عملية التفاوض.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78679" target="_blank">📅 13:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78678">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60e8157bf.mp4?token=oMnvqfcdNoKI9sbEofijDr68vCmDrHGgD_LwkD0knhPqa_mUgHzycErkEEDEK-zEi8XRWlwMOlM6dCn4G3zsmIVUe1hlnQeo1m8F8CKuphDttz0E7ni2SNq2Apu7FI50zKLWsBukJafuQRLB9MF1Q9IiOg9lQyRBN5BFvlVCc8QxrMq40Vf5JM5yUjH6oMzT41AqyhdBJkITOTOmOErhx62w-w6qvtjFikcFD3T3oeoPf3HIN1X0I7b5j74NbPZ4UH5STWBtwhiQCXNLk27qA-8GV1NoZlcsfKTQIllt-5t-JGcQOAr7qO0kCKEWkmrmIoNCyfRZBXhUgEetOMrxjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60e8157bf.mp4?token=oMnvqfcdNoKI9sbEofijDr68vCmDrHGgD_LwkD0knhPqa_mUgHzycErkEEDEK-zEi8XRWlwMOlM6dCn4G3zsmIVUe1hlnQeo1m8F8CKuphDttz0E7ni2SNq2Apu7FI50zKLWsBukJafuQRLB9MF1Q9IiOg9lQyRBN5BFvlVCc8QxrMq40Vf5JM5yUjH6oMzT41AqyhdBJkITOTOmOErhx62w-w6qvtjFikcFD3T3oeoPf3HIN1X0I7b5j74NbPZ4UH5STWBtwhiQCXNLk27qA-8GV1NoZlcsfKTQIllt-5t-JGcQOAr7qO0kCKEWkmrmIoNCyfRZBXhUgEetOMrxjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
وزارة الدفاع البريطانية:
هذا الصباح صعدت القوات البريطانية على متن ناقلة نفط روسية في القناة الإنجليزية كانت تساعد سرًا في تمويل حرب بوتين في أوكرانيا.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78678" target="_blank">📅 13:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 08-06-2026 تجمّع لجنود جيش العدو الإسرائيلي في بلدة الناقورة جنوبيّ لبنان بمسيّرات انقضاضيّة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78677" target="_blank">📅 13:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78676">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏴‍☠️
‏مسؤول صهيوني: لانتوقع نجاح المفاوضات لكن لا نتوقع عودة الحرب
طلبنا من واشنطن عدم تقييد عملنا العسكري في لبنان</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78676" target="_blank">📅 12:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78675">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">إعلام العدو: للمرة الثالثة هذا الصباح مسيرة إصابة هدف عسكري شمال البلاد خط المواجهة</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/78675" target="_blank">📅 12:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">📰
وكالة فارس عن مصدر مقرب من فريق التفاوض: قرار طهران النهائي بشأن مذكرة التفاهم لا زال قيد المراجعة القانونية والسياسية والتقنية
إيران لم تعلن بعد قرارها النهائي بشأن مذكرة التفاهم المقترحة</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78674" target="_blank">📅 12:20 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
