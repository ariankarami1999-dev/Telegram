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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 22:31:47</div>
<hr>

<div class="tg-post" id="msg-89019">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الله أكبر
تفعيل الدفاعات الجوية في سماء جزيرة قشم</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/naya_foriraq/89019" target="_blank">📅 22:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89018">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تتمكن من إستهداف جسم معادي في سماء البلاد.</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/naya_foriraq/89018" target="_blank">📅 22:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89017">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
مصدر إيراني: حفل زفاف في مدينة سيريك استُهدف بشظايا هجوم وحشي من العدو الأمريكي.</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/naya_foriraq/89017" target="_blank">📅 22:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89016">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔻
مصدر إيراني:
حفل زفاف في مدينة سيريك استُهدف بشظايا هجوم وحشي من العدو الأمريكي.</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/naya_foriraq/89016" target="_blank">📅 22:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89015">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عدوان أمريكي على مطار مدينة جيرفت بمحافظة كرمان الإيرانية.</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/naya_foriraq/89015" target="_blank">📅 22:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89014">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/89014" target="_blank">📅 22:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89013">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تتجدد الانفجارات في جزيرة قشم.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/89013" target="_blank">📅 22:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89012">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99659660c5.mp4?token=Bk2cPHPrdRnwuDhNdJixy7r5v2PR45GzR-MqQiVUefpinBSooQugLV1_E7xAeZ1ET-0v0q7_ia01E70JSfJTCmqxGQPF8RfQ19vhEOpsUeI6JS3Ib1cP7OCwdzBbQ6Z6L8Mok5vMkX4KnICogXNeM5d-nTYCPudkcMlqgKOhS5eUlF24wztxYYl1Tr5Yxdzpu5nARqRmlEJ-0h06WWrQXZjed-FWu9fF8pnV-lwLEqJ7MICGFAml2N-pkywFpca9xGzakkyD_Vgpp9SUkZczrd6OLL73mttg9qb03YDVsPmsmK-YSsS3efAcv9LcrQW874fuV3kZ9Pk0tuToBSLMGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99659660c5.mp4?token=Bk2cPHPrdRnwuDhNdJixy7r5v2PR45GzR-MqQiVUefpinBSooQugLV1_E7xAeZ1ET-0v0q7_ia01E70JSfJTCmqxGQPF8RfQ19vhEOpsUeI6JS3Ib1cP7OCwdzBbQ6Z6L8Mok5vMkX4KnICogXNeM5d-nTYCPudkcMlqgKOhS5eUlF24wztxYYl1Tr5Yxdzpu5nARqRmlEJ-0h06WWrQXZjed-FWu9fF8pnV-lwLEqJ7MICGFAml2N-pkywFpca9xGzakkyD_Vgpp9SUkZczrd6OLL73mttg9qb03YDVsPmsmK-YSsS3efAcv9LcrQW874fuV3kZ9Pk0tuToBSLMGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴
زمان شکار است ..
@Naya_Presd</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/89012" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89011">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4a346104.mp4?token=D3TiKIsMiF1o74Qj-KWoMZ-wKmChHrGoc_D9b4bbK4_SYcEU9iiEEiG8q5z4s5y59XVV5luLA9KEGWS70knibsK0gjrmHm3A9EQEZ6jZKgo60difaxEsmTx2RqUllaHytZdUU_w9FNYuNFGTHt6BfrdKG4ev3zBANDLYSlVRSbZ0DZ7BPldSfnhVfZe-ASpGt4gcpBwVMHmuE2Nd88oqtfOK4lEMh197ObfSacQXSRGrUNBUDmRLJiAdN5y_TmdmjO3UaBLVKxygQPoQfyy70Tf6gCgGhocx1_CHn-ET08rv_0pMY0wzCe_qu4IGExihXwUvOKTyrnPjyS88bAITSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4a346104.mp4?token=D3TiKIsMiF1o74Qj-KWoMZ-wKmChHrGoc_D9b4bbK4_SYcEU9iiEEiG8q5z4s5y59XVV5luLA9KEGWS70knibsK0gjrmHm3A9EQEZ6jZKgo60difaxEsmTx2RqUllaHytZdUU_w9FNYuNFGTHt6BfrdKG4ev3zBANDLYSlVRSbZ0DZ7BPldSfnhVfZe-ASpGt4gcpBwVMHmuE2Nd88oqtfOK4lEMh197ObfSacQXSRGrUNBUDmRLJiAdN5y_TmdmjO3UaBLVKxygQPoQfyy70Tf6gCgGhocx1_CHn-ET08rv_0pMY0wzCe_qu4IGExihXwUvOKTyrnPjyS88bAITSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/89011" target="_blank">📅 22:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89010">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">موجة صاروخية جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/89010" target="_blank">📅 22:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89009">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/89009" target="_blank">📅 22:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89008">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامب:  إيران لن تبقى قائمة إن ردت على الضربات الأمريكية الأخيرة.  إذا ردت إيران سنضربها بقوة أشد بكثير.  ضربة اليوم لإيران كبيرة جدا وإن تكرر الأمر ستمحى كليا.  الاتفاق مع الإيرانيين لا يساوي الورق الذي كتب عليه ومنحناهم فرصا كثيرة.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/89008" target="_blank">📅 21:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89007">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b224f120e8.mp4?token=UcO3MzzQocqEsetQliyRhh-SlWQc96bssZsrAhnusSbvCEJ0b9vJIAT5s-r9BSrRJoFSrIeTf3Lz7F7iib-ZCXE-iV__XHVXwIcYj023Kdp08_Gd4slo-DJhGgi-R0As-egIgx59poG91p6rgkbnwBOuCw7FFBuoazks0qZYh5AXrnCDuQfBICzHGbznxc6nm4sA5wUVlx0Paw3RsXJukUjDC6WF0pZq6HiFInVGU-6l2F0toh0vMtbeNzSEiJdMvWkQpih3nW_2jeE0pxVWyPdiVv1cQvMmtxeXIIESRywS875LE3SrAJRTznv3Ida0TsczperO4iKNBLXU3sN6Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b224f120e8.mp4?token=UcO3MzzQocqEsetQliyRhh-SlWQc96bssZsrAhnusSbvCEJ0b9vJIAT5s-r9BSrRJoFSrIeTf3Lz7F7iib-ZCXE-iV__XHVXwIcYj023Kdp08_Gd4slo-DJhGgi-R0As-egIgx59poG91p6rgkbnwBOuCw7FFBuoazks0qZYh5AXrnCDuQfBICzHGbznxc6nm4sA5wUVlx0Paw3RsXJukUjDC6WF0pZq6HiFInVGU-6l2F0toh0vMtbeNzSEiJdMvWkQpih3nW_2jeE0pxVWyPdiVv1cQvMmtxeXIIESRywS875LE3SrAJRTznv3Ida0TsczperO4iKNBLXU3sN6Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر إيراني: الرد الإيراني بدء</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/89007" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89006">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/89006" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89005">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/89005" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89004">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مصدر إيراني: الرد الإيراني بدء</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/89004" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89003">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/89003" target="_blank">📅 21:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89002">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/89002" target="_blank">📅 21:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89001">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7cc6c894a.mp4?token=ffiBmPiEk1ni4yKQTkeSiS7aMWlEm-yn4x-HzomhNCqG2ohbNLbt9AvBvfhiB2FwsCQuPYyZSoTPAj5yHOpV7y9cn0RKY3A82klpedo7YviXlOVHfopbw223nfIXJbHD3prmtVmP1Rd0PQCKJxtTksXynRrP5nGNFvIzZQCzUWi4FK3H7_hagWU5Z3GHuaqZbjkVafoUE3gGEq1aP9Q2iZddWoNtFP3879NuU09OItMTeWHs7csZLLjaSxavCJzTLW3nhtcqZxvg3V3YSmzq_zI-2cwtiuoz0ai4akTlA-_lGzcOwmdeZ0aM8y-8mwZ83C-7_vuMGmmAoh-AVmE3Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7cc6c894a.mp4?token=ffiBmPiEk1ni4yKQTkeSiS7aMWlEm-yn4x-HzomhNCqG2ohbNLbt9AvBvfhiB2FwsCQuPYyZSoTPAj5yHOpV7y9cn0RKY3A82klpedo7YviXlOVHfopbw223nfIXJbHD3prmtVmP1Rd0PQCKJxtTksXynRrP5nGNFvIzZQCzUWi4FK3H7_hagWU5Z3GHuaqZbjkVafoUE3gGEq1aP9Q2iZddWoNtFP3879NuU09OItMTeWHs7csZLLjaSxavCJzTLW3nhtcqZxvg3V3YSmzq_zI-2cwtiuoz0ai4akTlA-_lGzcOwmdeZ0aM8y-8mwZ83C-7_vuMGmmAoh-AVmE3Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة إستهداف وإسقاط الجسم المعادي في سماء إيران الإسلامية.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/89001" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89000">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/141a08119c.mp4?token=tPyXGG3Zbkfx73ne8ZhztiWl5Jk0OyLUYBCe2QTOsZ92qT_5KiVKSwt-KGpfZQwrw_Fau9amvwikqBhe970ELmxu1eZPJ7n64lb8cCznwuVnmi35TGqXZyBGij71VS0WSHG4exoiBv5PSwAbYvqHUyNyfqe-IkbERwVrCvN-OS76IoHq0i2JX8nwIcW0oYsO8Hs90MKwFocGcCzA1RAHjKKsbrNTqhAc7EAjQyb6uv-ptZzBvWGWiMoazgW5qHD7DeZ595GniKNVHCy2Tuxj2WQt360bzxOwkxeah427-qDv2b3iL0Pzhy3S6qiKwHFWdqWXZjqzk9SQh9JFeN4jZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/141a08119c.mp4?token=tPyXGG3Zbkfx73ne8ZhztiWl5Jk0OyLUYBCe2QTOsZ92qT_5KiVKSwt-KGpfZQwrw_Fau9amvwikqBhe970ELmxu1eZPJ7n64lb8cCznwuVnmi35TGqXZyBGij71VS0WSHG4exoiBv5PSwAbYvqHUyNyfqe-IkbERwVrCvN-OS76IoHq0i2JX8nwIcW0oYsO8Hs90MKwFocGcCzA1RAHjKKsbrNTqhAc7EAjQyb6uv-ptZzBvWGWiMoazgW5qHD7DeZ595GniKNVHCy2Tuxj2WQt360bzxOwkxeah427-qDv2b3iL0Pzhy3S6qiKwHFWdqWXZjqzk9SQh9JFeN4jZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تظهر انفجار جسم معادي في سماء إيران عقب تفعيل الدفاعات الجوية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/89000" target="_blank">📅 21:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88998">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974d1ed34d.mp4?token=VSECbCIWyDpLh7OOwAoOkVmS06npTH3MbJgfuWRvl_V7WBi559H7cIJ-Bf_2RSMy2OZINYNheQdDZFd4fIE-gTK9ALl1NNI0OIZ7V6goppzrwzVOnku7Y3EuIriS1jK-ytmTukkg7sT0-3pltoYm5aB1gFEecBR7uVhM2Bn6JRzq8K_1Kix8B9tb_Z_AOtU3oJzhb8hu9B9ipE9A-GaL5TgZNo3u1GObnbBxxRKBA8u7Co5Y92fP5cMKLVgm6Uwt9b_8-0SSA02RJX3VUErVH8ZjOt1PiNBMreaqdeW7UP0OfAff2DiLTPYoJraJMVD9AYty-3R2JM-M7GQ2L7-1GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974d1ed34d.mp4?token=VSECbCIWyDpLh7OOwAoOkVmS06npTH3MbJgfuWRvl_V7WBi559H7cIJ-Bf_2RSMy2OZINYNheQdDZFd4fIE-gTK9ALl1NNI0OIZ7V6goppzrwzVOnku7Y3EuIriS1jK-ytmTukkg7sT0-3pltoYm5aB1gFEecBR7uVhM2Bn6JRzq8K_1Kix8B9tb_Z_AOtU3oJzhb8hu9B9ipE9A-GaL5TgZNo3u1GObnbBxxRKBA8u7Co5Y92fP5cMKLVgm6Uwt9b_8-0SSA02RJX3VUErVH8ZjOt1PiNBMreaqdeW7UP0OfAff2DiLTPYoJraJMVD9AYty-3R2JM-M7GQ2L7-1GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تتمكن من إستهداف جسم معادي في سماء البلاد.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/88998" target="_blank">📅 21:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88997">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تتمكن من إستهداف جسم معادي في سماء البلاد.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/88997" target="_blank">📅 21:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88995">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عدوان أمريكي على مطار مدينة جيرفت بمحافظة كرمان الإيرانية.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/88995" target="_blank">📅 21:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88994">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامب:
إيران لن تبقى قائمة إن ردت على الضربات الأمريكية الأخيرة.
إذا ردت إيران سنضربها بقوة أشد بكثير.
ضربة اليوم لإيران كبيرة جدا وإن تكرر الأمر ستمحى كليا.
الاتفاق مع الإيرانيين لا يساوي الورق الذي كتب عليه ومنحناهم فرصا كثيرة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/88994" target="_blank">📅 21:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88993">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اطلاق عدة صواريخ من ايران نحو قواعد الاحتلال الاميركي في المنطقة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/88993" target="_blank">📅 21:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88992">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
اصوات انفجارات في جزيرة قشم</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/88992" target="_blank">📅 21:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88991">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏مسؤول أميركي:  عدد غاراتنا الليلة على إيران قد يصل إلى 100.  ‏ كل مرة ستستهدف فيها طهران ناقلة نفط ستقصف أميركا ناقلة نفط إيرانية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/88991" target="_blank">📅 21:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88990">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دوي انفجارات جديدة في بندرعباس</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88990" target="_blank">📅 21:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88989">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
حاكم "مدينة لانغرود" في شمال إيران:
عدم وقوع أي انفجارات أو حوادث في المدينة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88989" target="_blank">📅 21:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88988">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دوي انفجارات جديدة في بندرعباس</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88988" target="_blank">📅 21:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88987">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
🔻
المتحدث باسم الحرس الثوري: "عقوبات قاسية تنتظر المعتدين، وسيشعر الأمريكيون بالندم على هجماتهم الجديدة."</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88987" target="_blank">📅 21:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88986">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
مصدر عسكري إيراني:  القوات المسلحة الإيرانية سترد بالتأكيد على الجريمة التي ارتكبتها الولايات المتحدة الليلة باستهداف مناطق في بلادنا، وأن هذه الردة ستكون مضاعفة للهجمات التي تعرضت لها.  كما حذرنا ووعدنا سابقًا، فإن القوات المسلحة الإيرانية ستتصرف بحزم وبشكل…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88986" target="_blank">📅 21:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88985">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5ca56b7a.mp4?token=XpxzaN9ymTnGeATBw5s_tNITbCKeOCHtC2oM4JInSo9u4ohP6U9f2WkqDded7QKttITG64Oan8e6fPjECyeBPKrY0qiNanRAmuUuk8Ak2a9KXDX8BpZJKwb1H1P4AJYX0_1D8h0d5c09NuL_Mjf_v1ZNvUkYkYQFFzwsHr9ZViX4o0koRf01-I2GhnOTORRUAAL8nUgFwC4BYAhU9vMCC96j3G8DXW4jlW_65jdR71MP-GsNF6jjI1b7GT7lRPstYQyLOTINJub4dccgs45w5louDX34FJyTA1egXBmamj99Dn44k0nKG9u9RzD9LNgSYdDe9hAansPegeLDKW6TVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5ca56b7a.mp4?token=XpxzaN9ymTnGeATBw5s_tNITbCKeOCHtC2oM4JInSo9u4ohP6U9f2WkqDded7QKttITG64Oan8e6fPjECyeBPKrY0qiNanRAmuUuk8Ak2a9KXDX8BpZJKwb1H1P4AJYX0_1D8h0d5c09NuL_Mjf_v1ZNvUkYkYQFFzwsHr9ZViX4o0koRf01-I2GhnOTORRUAAL8nUgFwC4BYAhU9vMCC96j3G8DXW4jlW_65jdR71MP-GsNF6jjI1b7GT7lRPstYQyLOTINJub4dccgs45w5louDX34FJyTA1egXBmamj99Dn44k0nKG9u9RzD9LNgSYdDe9hAansPegeLDKW6TVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر إيراني مطلع: الصوت الذي سمع في مدينة مشهد المقدسة كان نتيجة انفجار وحريق في خط أنابيب الغاز، ولاوجود لحدث أمني.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88985" target="_blank">📅 21:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88984">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
مصدر عسكري إيراني:
القوات المسلحة الإيرانية سترد بالتأكيد على الجريمة التي ارتكبتها الولايات المتحدة الليلة باستهداف مناطق في بلادنا، وأن هذه الردة ستكون مضاعفة للهجمات التي تعرضت لها.
كما حذرنا ووعدنا سابقًا، فإن القوات المسلحة الإيرانية ستتصرف بحزم وبشكل واسع تجاه أي انتهاك لحدودنا أو مصالحنا.
المصالح والقواعد الأمريكية في المنطقة ستتعرض بسرعة لضربات من إيران.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88984" target="_blank">📅 20:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88983">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0HnmIxyzomFJd5X6QihP1mepRd0lAOYJD35WkmTMlkUZ45Vdjq1phgAD7439m5aEuqgPorm-6oghEnLeTIIZzsBvb3PTg7t6xvGmhbCMScfgz-ZIBzybByToTRjkktx9I3LeD9cglDK_53pCC-xZ9AkpKELGX6M7KVE-g3vxim8r_M7AyykLNcl4XQhhysOb5fCmZualg9UzKx-dh-1QXYozjlb6JmkTmab8v0vkLqYu5mtXTjVU0bkbnP9XctYlJj726P9Mmd0IQ9XDhpJuGCBxG7DJE_4XGm-j3qWdwa4VsYF9DBIcxFk7mqZ20CMJYwaadqD2Fnw90wg8ToIig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: ‏
‏"إن الولايات المتحدة، في هذه اللحظة، تشن غارات جوية على أهداف إيرانية قرب مضيق هرمز. هذه الغارات واسعة النطاق وقوية، وتأتي ردًا على محاولة إيران الفاشلة لزرع ألغام بحرية في المضيق، الذي يخلو حاليًا من الألغام (إذ أُزيلت أو فُجِّرت بالكامل!)، وعلى إطلاق الإيرانيين ثمانية صواريخ، تم إسقاطها جميعًا بنجاح، على قاعدتنا العسكرية في الأردن. إذا ردت إيران الفاشلة على هذا الهجوم المبرر، فسوف تُضرب مجددًا بقوة أكبر وعلى مستوى أعلى، لكنها لن تكون أكبر هجوم على الإطلاق، فالهجوم الأكبر ينتظرها، وعندما ينتهي، لن يبقى من الجمهورية الإسلامية الإيرانية إلا القليل جدًا!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88983" target="_blank">📅 20:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88982">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوي انفجارات جديدة في قشم وبندرعباس</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88982" target="_blank">📅 20:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88981">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوي انفجارات جديدة في قشم وبندرعباس</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88981" target="_blank">📅 20:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88980">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مسؤول أمريكي: هجمات القوات الأمريكية ضد أهداف تابعة للحرس الثوري داخل إيران لاتزال مستمرة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88980" target="_blank">📅 20:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88979">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏الوكالة الدولية للطاقة الذرية:
مفتشونا لم يصلوا إلى أي من المنشآت الإيرانية.
‏عدم إتاحة وصول مفتشينا لمنشآت إيران النووية يستدعي معالجة ملحة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88979" target="_blank">📅 20:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88978">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مسؤول أمريكي: هجمات القوات الأمريكية ضد أهداف تابعة للحرس الثوري داخل إيران لاتزال مستمرة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88978" target="_blank">📅 20:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88977">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">السفارات الأمريكية تصدر تنبيهات في الأردن وقطر والبحرين وسلطنة عمان لمواطنيها</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88977" target="_blank">📅 20:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88976">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الجيش لامريكي: بدأت القوات الأمريكية اليوم، الساعة 12 ظهرًا بتوقيت شرق الولايات المتحدة، بضرب أهداف تابعة للحرس الثوري الإسلامي في إيران. وتأتي هذه الضربات في أعقاب محاولات هجمات حديثة شنها الحرس الثوري الإسلامي ضد سفن تجارية في مضيق هرمز وضد أفراد الخدمة الأمريكية المنتشرين في المنطقة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88976" target="_blank">📅 20:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88975">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏السفارة الأميركية بإسرائيل تنذر مواطنيها بالشرق الأوسط لاحتمال التصعيد.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88975" target="_blank">📅 20:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88974">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">السفارات الأمريكية تصدر تنبيهات في الأردن وقطر والبحرين وسلطنة عمان لمواطنيها</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88974" target="_blank">📅 20:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88973">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">السفارات الأمريكية تصدر تنبيهات في الأردن وقطر والبحرين وسلطنة عمان لمواطنيها</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88973" target="_blank">📅 20:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88972">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات جديدة في بندرعباس</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88972" target="_blank">📅 19:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88971">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مسؤول أمريكي: القوات الجوية الأمريكية تشن ضربات على أهداف إيرانية في محيط مضيق هرمز</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88971" target="_blank">📅 19:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88970">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSgWOYVexjGyCLsTncrEz9zQ65EwZjRPLLsGiW_W22ohC_N3Ez_PL-448koucfl4OxY70hHIzJIbSSUCiNm5BIVudyMLTvB31oT9nbW4XcLch9EqFtEm8WVcAlZI15OrsL-LkmnZZpXmrRz8G_KToea3xtG4FpsCXXI2Xlmp5vunsJnUVunDcbwLiGWGV6wmRgjF-j_t97KLGVBhZS8n_yEzjgw0Ck-bGCsCvt9D9zH9Xk9ttQz0QK95A3EMww9PV69ts0_VDRyg8N02dYVtq0FHChh5A0-2sVhIJJ-FTTp3KUATVFOJCx_TXw3cqvVTvdh7iMpi0GGEWR3spN56gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النفط يلامس 93 دولار للبرميل الواحد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88970" target="_blank">📅 19:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88969">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نائب محافظ محافظة هرمزكان: لم يتم حتى الآن تأكيد أي إصابات في محافظة هرمزكان.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88969" target="_blank">📅 19:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88968">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTEB2AB8V8m608tEWZWWtgHZadJ91IV7VneudXjDV7ooPWsr9O-s-jz-ZJk9Qk8QK9D21r9Fipimc8VdpJKZDnfti9EKaENs1_-72QFUagyxXgot-6LE5k8FL4K9Pn5qBf0r_taDr7y7EpDIM7o3aqjZtHaXDb5d3oM9vxFsXpujleaT_C8h-kCkTAeAvPF6grm4sbWklfoawIeIyzOpKfzM9yCzHoa4zs1wRWyEqP1fUxn1y8-6MOZylp10rGwyPzTfB1iToLyGyNUHk4k_LxaddKxkAs-iEKYC4CmjPa2VyCaAUI-iQk5faYB_WAjQgwc7BpVz7pCK89o9N47j4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النفط يلامس 93 دولار للبرميل الواحد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88968" target="_blank">📅 19:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88967">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">أنباء عن سماع دوي انفجارات في قشم وبندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88967" target="_blank">📅 19:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88966">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">أنباء عن سماع دوي انفجارات في قشم وبندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88966" target="_blank">📅 19:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88965">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دوي انفجار في جابهار الإيرانية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88965" target="_blank">📅 19:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88964">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">أنباء عن سماع دوي انفجارات في قشم وبندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88964" target="_blank">📅 19:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88963">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">أنباء عن سماع دوي انفجارات في قشم وبندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88963" target="_blank">📅 19:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88960">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Srk0EJ9a4Sxy3qM8T7aGmr83R05vZpwTaqp8hYlgbHrTBMmp32ZfnEJRGudQbpSK1Q0SWyV3LLOFi1JGvdzOcsVaycFJkhiqWjFXkNPQ0534Z3X-NBQ4zVsUrHwRkX6QRxlD-HwEu-N__ehdKkJas-WX4rm4pB4EfG9zRyiOwqmUy2Qwn5g8iYEGfX7Myi7IeAn-VPtywGiddEfKeqSMc7LaztEwYH-dF8-jHKm2O2nlpY_ekm8R8ADlVyfMp8y7ML4O-Sq-kuOl6lx1vcCVRpwey6JZV1tZT0m4K7zfcLCqO4cHMrinwQzhZiRkSPirIubwIns2mNsIFQrr9SkubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HYkAAvWpWHCuTlpfPljuMV7fJh9VKVrgBCyp6xLtHNgVUsBKHEgzS3bwPWFeRr1QIKl8LWK1CAwRfnvlk1QM4Ouyx5UYZFn4LBOlS7BQNWvQc_i34laD3O4EqzmEHAgIyt9D8mhZuc1sM5AVxd0o_QDV-3hcnKJOFtV_F8TsDkQkGa-Kt7VuFp8gnUjQOOmfN5qnvYocXbCAhyxudQPsbdvlLd-dmXQbYtE__TJACjBI3QV5wNHaM1aEPoCQBN09ug1a3t-8v7heDjQnPKVeGTqFcNd4_OSqvLS0H3EueabJ2HdC8CISz1ASDMurhNMaYlmTdMXvVZPmu4Kz1Mbcmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxFi02amEaBSy9M-8OwDpMAoEHFRwc-11f6DEgRJ8145t49IKwAUO1FcTdhJrxs6cquNRsV0rAHlZZ5axK7eOEW0PNmxakmTMMiYjzmu1KsB4iBrgXtbdrlh0-E2VBtf25Ey7tXjiTMrCm_dfIeA8Y9lGAcoFFLle1eF7wEiKkncPGsNAdmzBPO5_zZTR3B9v4xK45wQF6XSrzZXX87PeQAGquULf4kfOaj7LM89ASwm5OJPFPFh8ulP2lDSGADv2lsURuKKPg8F1rr8Kf3Zuljb-dXBmqadLx9UlVfpf8XhwPV2lDzJ6sjW7sK7tfHK8dZ2wo_DDvD9o61CWEF6oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#ترفيهي
عشر ناقلات نفط على الأقل ترفع العلم السعودي تقوم بتغيير علمها السعودي إلى العلم الليبيري، وقامت جميعها بتغيير اسمها وهم متمركزون الات قبالة سواخب خورفكان في محاولة للعبور باتجاه الخليج.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88960" target="_blank">📅 17:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88959">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وزير الخزانة الأمريكي بيسنت: من المحتمل أن تمتلك إيران ثالث أكبر مورد للطاقة في العالم.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88959" target="_blank">📅 17:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88958">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزير الخزانة الأمريكي بيسنت: من المحتمل أن تمتلك إيران ثالث أكبر مورد للطاقة في العالم.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88958" target="_blank">📅 17:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88957">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">قتيل و5 جرحى كحصيلة اولية للانفجارات في مدينة ادلب السورية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88957" target="_blank">📅 16:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88956">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇵🇸
أمن المقاومة الفلسطينية:
أحبطنا صباح اليوم عملًا عدائيًا كبيرًا كان يستهدف شخصية قيادية مركزية، فيما نجح الاحتلال في اختطاف مسؤول أمني كان متواجدًا في مسرح العملية. نجحنا في كشف القوة المعادية وإيقاع خسائر فيها، واغتنام معدات وأسلحة منها، كما ضبطنا ثلاثة عملاء للاحتلال كانوا في مهام إسناد وجمع معلومات.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88956" target="_blank">📅 16:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88955">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏مقتل المتحدث باسم تنظيم داعش "أبو حذيفة الأنصاري" في حضرموت اليمنية</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88955" target="_blank">📅 16:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88954">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
🇺🇸
وكالة فيتش للتصنيف الائتماني:
قد يؤدي تصاعد الصراع بين الولايات المتحدة وإيران إلى تعريض بعض التصنيفات الائتمانية لدول مجلس التعاون الخليجي للخطر.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88954" target="_blank">📅 15:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88953">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88953" target="_blank">📅 15:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88952">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قتيل و5 جرحى كحصيلة اولية للانفجارات في مدينة ادلب السورية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88952" target="_blank">📅 15:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88951">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
جهاز الأمن الوطني العراقي يعلن عن تفاصيل عملية «ظل العدالة» التي ينفذها الجهاز ويعلن القبض على أكثر من (500) متهم حتى الآن.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88951" target="_blank">📅 14:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88950">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b839ccee98.mp4?token=IrJenBu94c0zIriXAFHmb-AMVo3OjtRrVADqlE3_azCsRDREiJGHmiDT271HTKofmzxxCdCaP3TKKT5tn2k6InJ--uV9TBXyXL9whOBrVwns1a56jhEIYDK6aJkUXw24sGgmdQUlbiDeMKFItpKgOX1Myavzp2VeBvsoNd-TehCtWosC6SQKZCCQubYi09SjVUH2UaD_FaayE5zU2UyVptZHdrAjX6JBRKcyv7VkghczaueGfNL0TysdaTgLURaM1DOBHFusk3s8uZMjIdMnNeZinkzcCVV7Dhio2ML00jWM3qobTG9yfNXlXZpIcv1QkN-I6PSeI82NufbnQfoBMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b839ccee98.mp4?token=IrJenBu94c0zIriXAFHmb-AMVo3OjtRrVADqlE3_azCsRDREiJGHmiDT271HTKofmzxxCdCaP3TKKT5tn2k6InJ--uV9TBXyXL9whOBrVwns1a56jhEIYDK6aJkUXw24sGgmdQUlbiDeMKFItpKgOX1Myavzp2VeBvsoNd-TehCtWosC6SQKZCCQubYi09SjVUH2UaD_FaayE5zU2UyVptZHdrAjX6JBRKcyv7VkghczaueGfNL0TysdaTgLURaM1DOBHFusk3s8uZMjIdMnNeZinkzcCVV7Dhio2ML00jWM3qobTG9yfNXlXZpIcv1QkN-I6PSeI82NufbnQfoBMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من استهداف مجهول طال عدة سيارات في ادلب تحمل كدس عتاد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88950" target="_blank">📅 14:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88949">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني:
لن ننسحب من غزة حتى نزع سلاح من القطاع وتجريد حماس من سلاحها وتدمير جميع الأنفاق.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88949" target="_blank">📅 14:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88948">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2c243aa.mp4?token=v931KNIYDal-z_hcKPd9aanYMkaIEKO-RdtGjSsGg3decVur9O12zKS7zAR53Sx0i4rfN5Vv2VU0kL8McwdgWToYDyo_r3TFg3_ngWTC0YcfoWahhBwqqBZfyjf6pjEOtiRKUAZTiFiuf9ebB_LdKVP5WK0vSNm-SQc1NPyHGjfnjHh3yODR4OmNev7C0Ckkq4AlnWG0Y8WgjohC2zHjIixo2CbnO1ujVTQTccOkGBA7182Tg1LnFE2juXdJ8tRwZ1lub1ubmAi8QOuPed2tNJLb5bvqhXbOz3rLN_rz-HBHdiBSSta_lpGNFUQXdq6ItqLlTTYtsMu_H_UU57NUvgLiztRbBZtUWAhXNP2zhqc9kM899DiTzo7C1qXaobPXQ5utsfO2a2y9aqFgtt5COEYOwshoop06oD2rIDcnXL3dV2lA4_92mCHb1oz9d6yy_OcS2YP3E0nBiqAwxKLBL6dPsENvUHwJV5VGX2BXqjztO0yeVi0WSvFN-N7Tu1y0aXlRKhawSNf6gE9o5r7JTbpc5-mm6W-zljzMJiVUyUQYQdtwbOd3c9iKUDUOA51UiBwE4qQsb6euk3dNUlOQBvqky4Wh58klzYA9lU4pKQcH1xhgJqiN9-cTT2irWrQXEWEs_MRgd3iRilDPkCxKhHznqoJqrGmZC3OzUpKuMH0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2c243aa.mp4?token=v931KNIYDal-z_hcKPd9aanYMkaIEKO-RdtGjSsGg3decVur9O12zKS7zAR53Sx0i4rfN5Vv2VU0kL8McwdgWToYDyo_r3TFg3_ngWTC0YcfoWahhBwqqBZfyjf6pjEOtiRKUAZTiFiuf9ebB_LdKVP5WK0vSNm-SQc1NPyHGjfnjHh3yODR4OmNev7C0Ckkq4AlnWG0Y8WgjohC2zHjIixo2CbnO1ujVTQTccOkGBA7182Tg1LnFE2juXdJ8tRwZ1lub1ubmAi8QOuPed2tNJLb5bvqhXbOz3rLN_rz-HBHdiBSSta_lpGNFUQXdq6ItqLlTTYtsMu_H_UU57NUvgLiztRbBZtUWAhXNP2zhqc9kM899DiTzo7C1qXaobPXQ5utsfO2a2y9aqFgtt5COEYOwshoop06oD2rIDcnXL3dV2lA4_92mCHb1oz9d6yy_OcS2YP3E0nBiqAwxKLBL6dPsENvUHwJV5VGX2BXqjztO0yeVi0WSvFN-N7Tu1y0aXlRKhawSNf6gE9o5r7JTbpc5-mm6W-zljzMJiVUyUQYQdtwbOd3c9iKUDUOA51UiBwE4qQsb6euk3dNUlOQBvqky4Wh58klzYA9lU4pKQcH1xhgJqiN9-cTT2irWrQXEWEs_MRgd3iRilDPkCxKhHznqoJqrGmZC3OzUpKuMH0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادلب بعد الانفجارات</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88948" target="_blank">📅 14:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88947">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6df400dbf.mp4?token=GdHYSl8ViXAXjA9OPCq5PT4cqXGBVM09W5LKf_-eTBTpYsPA05PhPkOPrF0cQKDCYTJLJkUsOoA4vuJM89Bwu1728GtjbNpL992_Oo6lb4_mXDCoro950fu8dlubAP3PuRIdHCGFdAQqctvxQihU1yEnhmemMSRwtxZODFCYybFE1Ov3etMvPf_LVA7dYOwA_6ppNjchvjo3XmKexzdWBdGKDRIo4Nh7IQE8s3IoXAUmQu0_hwnXRMLjTK5miCVWrsTrdENQysbvrHec9QFtbPEOj1zc-lDqNtt7tJAUBLsQIdSsd9a7DED_M6q_C5gMYChde_G9FFsXEi7VFUGW3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6df400dbf.mp4?token=GdHYSl8ViXAXjA9OPCq5PT4cqXGBVM09W5LKf_-eTBTpYsPA05PhPkOPrF0cQKDCYTJLJkUsOoA4vuJM89Bwu1728GtjbNpL992_Oo6lb4_mXDCoro950fu8dlubAP3PuRIdHCGFdAQqctvxQihU1yEnhmemMSRwtxZODFCYybFE1Ov3etMvPf_LVA7dYOwA_6ppNjchvjo3XmKexzdWBdGKDRIo4Nh7IQE8s3IoXAUmQu0_hwnXRMLjTK5miCVWrsTrdENQysbvrHec9QFtbPEOj1zc-lDqNtt7tJAUBLsQIdSsd9a7DED_M6q_C5gMYChde_G9FFsXEi7VFUGW3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من ادلب بعد انفجار كدس عتاد بعد صوت الطيران الذي حلق في اجواء المدينة</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88947" target="_blank">📅 13:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88946">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b327e04c.mp4?token=uUboDclpPqVOR7BIUevLGm4zuPpAIUq2UtgkBmpD-R_PjHKxi-zNqBpiJt1Becw5tIcLLcu0LiAHnlWfdWzP389yjV2xyweYNanQ-XqihjuythN--Q_eKPrk7cXCi1rxZR3XZTUcna2xxpJOBE7d1T8-brL0ymSHzR67B5Hur6ZSL0jlYgPT1KB0j2CnfO9T4foZcOsqKrT4-OA5hr16pgUmYXllr93k7fRs1PXPPJCeGeqDdZmjW83nay0Ndg0esoUsAzWw9ZbE-nEQsSCGDwB3a4m-Maq6dF-UB8giW10PqwKsMhkmk_DXIsEpJqpXt3oNCH1tT-rbIIkfvZBFDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b327e04c.mp4?token=uUboDclpPqVOR7BIUevLGm4zuPpAIUq2UtgkBmpD-R_PjHKxi-zNqBpiJt1Becw5tIcLLcu0LiAHnlWfdWzP389yjV2xyweYNanQ-XqihjuythN--Q_eKPrk7cXCi1rxZR3XZTUcna2xxpJOBE7d1T8-brL0ymSHzR67B5Hur6ZSL0jlYgPT1KB0j2CnfO9T4foZcOsqKrT4-OA5hr16pgUmYXllr93k7fRs1PXPPJCeGeqDdZmjW83nay0Ndg0esoUsAzWw9ZbE-nEQsSCGDwB3a4m-Maq6dF-UB8giW10PqwKsMhkmk_DXIsEpJqpXt3oNCH1tT-rbIIkfvZBFDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسجيل عدة اصابات في ادلب جراء تطاير كدس عتاد بعد استهدافه من قبل طيران وفق شهود عيان</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88946" target="_blank">📅 13:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88945">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5e04eea08.mp4?token=MKT9Wjj-_Y3FgEL3cupc4QGyG7qQqst386gk8YX1bwlCXsjQaw1BEc6C4D4R9yupOq0URGrhNjdyfXmsqJqfYyfFCWaU5MYpOZhQ1FbxzrXds_QGyawM2jRfE8WSYEqpoZ6mdSpTNEBRJIa8DgW4nv-X9FuhS_ZLKJZ0gxOrDu16pxzPUmJs8IXP9QGPJrmTMgCJWgVabEEUQzW6M0Sq7lMWq3jSanY87jPUtfXIhq5YBKKJ633pSg8bC-TJiny4IIP4DXk-6dEHzjWOMHqTbhzOgHgR5CyP7SL4Iql_N7MUGu-CxxwEBSX9UfgRdPAyS65YcGezChXYGXAU0eNhdYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5e04eea08.mp4?token=MKT9Wjj-_Y3FgEL3cupc4QGyG7qQqst386gk8YX1bwlCXsjQaw1BEc6C4D4R9yupOq0URGrhNjdyfXmsqJqfYyfFCWaU5MYpOZhQ1FbxzrXds_QGyawM2jRfE8WSYEqpoZ6mdSpTNEBRJIa8DgW4nv-X9FuhS_ZLKJZ0gxOrDu16pxzPUmJs8IXP9QGPJrmTMgCJWgVabEEUQzW6M0Sq7lMWq3jSanY87jPUtfXIhq5YBKKJ633pSg8bC-TJiny4IIP4DXk-6dEHzjWOMHqTbhzOgHgR5CyP7SL4Iql_N7MUGu-CxxwEBSX9UfgRdPAyS65YcGezChXYGXAU0eNhdYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الانفجارات في ادلب</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/88945" target="_blank">📅 13:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88944">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارات تهز ادلب السورية</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/88944" target="_blank">📅 13:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88943">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجارات تهز ادلب السورية</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/88943" target="_blank">📅 13:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88942">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8auhNaBSydBoLyRhEz6yQePvaWbm3MVD2gbzUoAAdkfHOdDx0vkGChIpFa9MGOlCLeORs4anl6Gobv8K0hlnMeb_TUDyAK35DJkFo4fVzXU9bQuqNEOoadwbYf0B5xBTNBUNDzHaeDnWkvwhYx3JywRMhLjBvldgrFkNUd1K15rkVJmNpoDwKIePdvB8BxBx_SThhH4jhUycdnuqoKelhPIHqo00uQWV15Up8foCmFxvtPRpRw7ze2PkUy4m_HHlyQ6KjDB2MZvsAZDt6Y2QggNgK79Jn6zGEic0HVhvpFO11J3UBxmrQoBko_1xqsT9XOuPr7XiFFXhncJRnjr8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر:
يتعهد بالرد بقوة" بعد أول تبادل لإطلاق النار مع إيران منذ أسابيع.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88942" target="_blank">📅 13:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88941">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
القضاء العراقي:
محكمة تحقيق الكرخ الأولى أعلنت استكمال مرحلة الاستجواب في ملف 5704 متهمين من عناصر عصابات داعش الإرهابية المنقولين من شمال شرق سوريا إلى العراق والانتقال إلى المرحلة القضائية التالية المتمثلة في إحالتهم على محكمة الموضوع، كل وفق الأدلة والوقائع المتحصلة في قضيته،عمليات التدقيق أظهرت أن الملف يضم أشخاصاً من 67 جنسية بينها 16 جنسية عربية و19 جنسية من دول الاتحاد الاوروبي و 32 جنسية أجنبية أخرى، فيما بلغ عدد العراقيين 474 وعدد السوريين 3497، الأمر الذي يعكس الطبيعة الدولية للملف وتشعب الوقائع والأدلة ومسارات الأشخاص المشمولين به، التحقيقات وجمع الأدلة والتحليلات أسفرت عن كشف عدد من العناصر شديدة الخطورة ممن شغلوا مناصب قيادية أو أمنية أو شرعية، أو عسكرية، أو إعلامية، أو ارتبطوا بعمليات نوعية وجرائم ذات بعد دولي وقيادات من الصف الأول في عصابات داعش الإرهابية</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88941" target="_blank">📅 12:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88940">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">▫️
الرئيس التنفيذي لشركة هاباج-لويد المتخصصة بالشحن البحري:
من المنطقي الاعتقاد بأن مضيق هرمز سيظل مغلقاً في المستقبل المنظور.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88940" target="_blank">📅 12:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88939">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88939" target="_blank">📅 12:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88938">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw5HB2dE0PCwWiBfFCBwwce1nQa111qhbO9GkCQMnNmGgFAgv9IA7eax3alJLmx-lWQzDgoKNtFfAXprQynzK1Xk3YeNfF50j7fI4f7-LebHLpy3UgtH_RfVaf05l5n0i3rl7mX0GZdi3ILtIzYzqqXBPNDTOLSFnQ2uSL9gvD-UH6Tn3KlabtdinsZdvuY06e6FZTS6Z7GrhYKRsqVghJ0BaYF63S7kLFAJnbkuBu0LMHiJ7u21XMrs_XOXGAx9-yjYcD8hJ9O6QA7Y-vZj1HM5sYHP1cA18UcAao13EvtKysMVgZ1gPrDs6_UDFn9B3_ifiQ0zSIqAb69No0i5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
الليلة الماضية، حدث شيء غير عادي ومثير للاهتمام للغاية على الساحل الشرقي للولايات المتحدة.
‏تم وضع محطة نورفولك البحرية، وهي المجمع البحري الرئيسي للبحرية الأمريكية وأكبر مجمع بحري في العالم، في حالة تأهب قصوى، لأسباب غير معروفة حالياً.
‏وبحسب متحدث رسمي، "تم تعديل الوصول إلى المنشأة، حيث تم إغلاق بعض البوابات أو تشغيلها بممرات مخفضة" بسبب تهديد غير محدد.
‏الأمر المقلق هو أن إحدى آخر المرات التي صدر فيها مثل هذا التنبيه كانت مباشرة بعد أحداث 11 سبتمبر.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88938" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88937">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
🇮🇷
مصدر امني لنايا
نصب دفاعات جوية اتجاه الجمهورية الإسلامية في ايران من جهة محافظة ميسان ..</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88937" target="_blank">📅 12:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88936">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇷🇺
الخارجية الروسية:
سيكون رد روسيا على أي تحركات محتملة معادية لروسيا في منطقة البلطيق مدمراً، وسنتخذ تدابير مضادة في حال نشر أسلحة أمريكية في اليابان.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88936" target="_blank">📅 10:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88935">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
🇸🇦
منذ فترة ليست بالقريبة،
لم تُرصد عمليات إقلاع لطائرات إنذار مبكر أو طائرات للتزوّد بالوقود من قاعدة الأمير سلطان الجوية في السعودية فهل تعمد السعودية إلى عدم المشاركة في الضربات الأميركية الأخيرة ضد إيران لتجنب فتح جبهة جديدة إلى جانب جبهة أنصار الله في اليمن؟!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88935" target="_blank">📅 10:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88934">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
قيادة الدفاع الجوي الايراني:
تتولى الدفاعات الجوية في جميع أنحاء البلاد أربع مهام رئيسية تشمل الكشف، والتعرف، والتتبع، والمواجهة مع الأهداف الجوية.
المهام الأساسية للدفاعات الجوية هي الكشف عن أي جسم طائر في سماء إيران وحتى ما وراء سماء البلاد. بعد الكشف، تبدأ مرحلة التعرف، وفي حالة الضرورة، يتم التتبع بواسطة الطائرات المقاتلة أو المواجهة باستخدام الصواريخ وأنظمة الدفاع الجوي.
في النهاية، تهدف الدفاعات الجوية إلى منع أي طائرة معادية من تنفيذ مهمتها، وإذا لزم الأمر، تدميرها.
تنتشر قوات الدفاع الجوي في أكثر من 3800 نقطة في أنحاء البلاد، والعديد من هذه النقاط تقع في مناطق وعرة.
إيران دولة ذات تضاريس جغرافية متنوعة، وتنتشر قوات الدفاع الجوية في الصحاري، والشواطئ، والجزر، والارتفاعات.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88934" target="_blank">📅 10:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88933">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇶
مجلس الوزراء يوجه بتجهيز المولدات الأهلية بالوقود بسعر مدعوم لشهر أيلول.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88933" target="_blank">📅 09:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88932">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88932" target="_blank">📅 09:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88931">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOdR6Anv3FWtYfFi_A-sEgqDZad6oLibdYnACk4D-8KXfKSzS393yPKjJe6tJT4qS5KcGoKUSDUjbzxQpcc8gkT7FrEOjxBeNn0VA7aHwI9z7pFlvZ-FEMMHbKfaicLprcgOU15DILw3oJk86PM2yDN6QloPKMsFwIjPd0dY5gSvDQhOV9yW6sOFbDoxToHwWKlaXfWiLhIe-TkTfXF1MBwmEMrzIAS2JV9s7_MFpriEF97O02uD_32REnkKi2ZHglmsezAPuumKRWUjsr1Cu4fMzO2jxfmJf4s6RQn1TniEbYuPrDcGo_dE3nvtWc5Pw85o7yVGKghCd2hUxT6naw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعار النفط تقفز من جديد: ‏خام برنت يرتفع 2.39 دولار ليبلغ عند التسوية 90.49 دولار للبرميل.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88931" target="_blank">📅 09:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88930">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
بزشكيان
:
أدت مفاوضات استمرت حوالي ثلاثة أشهر، بوساطة البلدين الصديقين والشقيقين باكستان وقطر، في النهاية إلى اتفاق في 18 يونيو 1405، والمعروف باسم مذكرة تفاهم إسلام آباد.
لكن التزام أمريكا بالوثيقة التي وقعها رئيسها لم يدم أكثر من أسبوعين، وبدأت تجاوزات ذلك البلد وتراجعه عن التزاماته، والتي لا تزال مستمرة.
من الواضح أن انتهاك الولايات المتحدة لالتزاماتها قوبل برد إيراني متناسب، لكنني أؤكد بوضوح أنه إذا عادت الولايات المتحدة إلى التزاماتها الواردة في مذكرة التفاهم المذكورة آنفاً، فإن الجمهورية الإسلامية الإيرانية سترد بالمثل فوراً. على عكس الولايات المتحدة، يتمتع بلدي بسجل حافل بالوفاء بالتزاماته ومعاهداته الدولية، وقد تصرف دائماً وفقاً لمبادئ القانون الدولي.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88930" target="_blank">📅 08:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88929">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يستهدف العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88929" target="_blank">📅 02:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88927">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433892a9ce.mp4?token=mcmyxwvl563AagXAAx4rZJCBz3bzQgpQnyRwSLB0GCWSkr4KkCieA5Ax-PSFIGPtW2Qd5AYhB3wC3JoxkbwTEdExuulQG1At1QFG8LrWnu5qGUBiGvKwTGN2QUpMikT21F6TU67p6SkojR4PJK2EJskVbgOxzMlhz9Qad7gpgFSsyW-m2WEpsL-pZJvkewZGQzSaVDf6x6rGfCFfSmFNoNnGkGQ_Ar6ysVOrHpVkyn4i7PLHuRlfH0A_02MHXiR1n3L8Pez05mSS6nyXErytuJxu2TmQrY-bd19PNi7pOoQfAeuhzysTpWkjXTV9FIRgSpOk0pxp1JEBNY-HTW4TUqp5R8zCFQRk3amLVKbqVRjbIV6-S8Q1TG2VnZsYUnZmEHcyC6SbwrDYGRLXMr7TfSg6GHi6l9PWn1xi1q4ZZlwP4MnuOlAEjIHcjyP163-4fVwge8AV0xbVyh_p39Ej5J1NBK0L716j7CQ0Q9A6MYX1Oct6zogR1xLxg4Ddxo_RlXHHqJ0MlF2xoptO9dAjB3cF9X5DG2tgVqQdI_COaAG9J8gr39ZowNOKPWV7gBZm8_QzkA9TrdXce03CBX7Hbzj1QBcp-BVpPlJ6zIkDgj-HOIgczg4FAZw4h94hu5MdKSG84aWBn6Pb2oJ0rjqc0h1ujEcEONBhYeFsLv410jE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433892a9ce.mp4?token=mcmyxwvl563AagXAAx4rZJCBz3bzQgpQnyRwSLB0GCWSkr4KkCieA5Ax-PSFIGPtW2Qd5AYhB3wC3JoxkbwTEdExuulQG1At1QFG8LrWnu5qGUBiGvKwTGN2QUpMikT21F6TU67p6SkojR4PJK2EJskVbgOxzMlhz9Qad7gpgFSsyW-m2WEpsL-pZJvkewZGQzSaVDf6x6rGfCFfSmFNoNnGkGQ_Ar6ysVOrHpVkyn4i7PLHuRlfH0A_02MHXiR1n3L8Pez05mSS6nyXErytuJxu2TmQrY-bd19PNi7pOoQfAeuhzysTpWkjXTV9FIRgSpOk0pxp1JEBNY-HTW4TUqp5R8zCFQRk3amLVKbqVRjbIV6-S8Q1TG2VnZsYUnZmEHcyC6SbwrDYGRLXMr7TfSg6GHi6l9PWn1xi1q4ZZlwP4MnuOlAEjIHcjyP163-4fVwge8AV0xbVyh_p39Ej5J1NBK0L716j7CQ0Q9A6MYX1Oct6zogR1xLxg4Ddxo_RlXHHqJ0MlF2xoptO9dAjB3cF9X5DG2tgVqQdI_COaAG9J8gr39ZowNOKPWV7gBZm8_QzkA9TrdXce03CBX7Hbzj1QBcp-BVpPlJ6zIkDgj-HOIgczg4FAZw4h94hu5MdKSG84aWBn6Pb2oJ0rjqc0h1ujEcEONBhYeFsLv410jE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
جانب أخر من الإشتباكات العنيفة على المحور الغربي لمحافظة السويداء السورية بين عصابات الجولاني الإرهابية والفصائل الدرزية.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88927" target="_blank">📅 02:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88926">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الله أكبر  إستهداف ناقلة نفط بثلاثة صواريخ قبالة سواحل عُمان.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88926" target="_blank">📅 02:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88925">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad70a05f98.mp4?token=O6-H5Hf03_J3RD5Q2-gHoV7uwEW9kKeTP_lENfC_nIOSSL3AoLGTZ9uZ0LvrTdQVAqNrwwkXo412uBK9tW9Qt9bv_FLfmmV5FowkY9_k-0hiQCStBCEbI5YcoETjKVtSwtz5yDRvU1NsMhjsRLqAHgdebLr3tdFvjHZnIEjlMdijbBefZaZf2bWNMEdIBid2MkQkH9yYWVyx6fky4zX9PW9ZeNAjumhriUyHqy-nboNn1bKypEhLkT1Ly6_xZJve4zOjG3ECNHjVW_whOChthlYkBYUT5v7yl2ngyoID2at0Ju_vtEHEz7gRKtI8GOJIkw_XWdjqgpQ4XctUgIdBdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad70a05f98.mp4?token=O6-H5Hf03_J3RD5Q2-gHoV7uwEW9kKeTP_lENfC_nIOSSL3AoLGTZ9uZ0LvrTdQVAqNrwwkXo412uBK9tW9Qt9bv_FLfmmV5FowkY9_k-0hiQCStBCEbI5YcoETjKVtSwtz5yDRvU1NsMhjsRLqAHgdebLr3tdFvjHZnIEjlMdijbBefZaZf2bWNMEdIBid2MkQkH9yYWVyx6fky4zX9PW9ZeNAjumhriUyHqy-nboNn1bKypEhLkT1Ly6_xZJve4zOjG3ECNHjVW_whOChthlYkBYUT5v7yl2ngyoID2at0Ju_vtEHEz7gRKtI8GOJIkw_XWdjqgpQ4XctUgIdBdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  إستهداف ناقلة نفط بثلاثة صواريخ قبالة سواحل عُمان.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88925" target="_blank">📅 02:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88924">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVTGCHnDYwWTGU2AfvlQErXAfmzhM4jdYQTypNBgKEZ5h00GrvEW50SET383ZlMxcZNBjdao6NjXkxwo18H0xMrff_S2WH1emb4NpDn5vfCDrhXmyweyzMJrYrqqlPAGM0aU2Idx7tbx7dKvjTOdpMPJKaFlJEu7zJQH4fFBmbGluf6gINCyJFODaPYxH76OGtFkMoD3aKpOkCcDAmLnIiqPLMU7tO4ylHNvYd0haqQeT4SaSae2VrKpCMNChRYpZc59u7qzfw2wWzCOG6_1pbN7N39OTIaCB_G87CvKaabq5AmUytHe41KKqzxpKS_uTBe-3a5OpzUhyHJimx3j4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث امني في مضيق هرمز</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88924" target="_blank">📅 02:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88923">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حدث امني في مضيق هرمز</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88923" target="_blank">📅 02:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88922">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16d4c4b759.mp4?token=P9YqY3ULzRRGos5Gea08D-hq2tkzGO5hofKRn3zc-ge_rkTfCbTDrw7GkOT32WTxQvX7fghPCjSeV4I48jMfZH6zzR0sHzHfGubO0ov7bn9PjyFkaknuu7nuRMVh6_bzNNSm--b-ui6sjWhkngUfoP2x8jPg-YQH5nPQHXGb5ioUGx52ekEiIX9UVxQUNjmQ_2zXjCf1RoOJCfjx9VblPCZQnCY56BNm8K5EMXyuFxQJEw_vRS7KXTCv5EhohuLsAXDFFVstHnMXgt3Ia10Xp1fQF7WzvwEE56Vpi9aW0xuzGbcpEJWUCK7InIQhuf2HYSCeIJN9lSuyyyfKcWNP2DkUH6oOsot4eM7ivGEIBiLAJ20ftOKNw62DtGGczG8X8K8nha7qDyM3Z_C1aEUc6HVGD1jbvY1t_kwzyEJZc7RCgng3i4Vms6W8iMJ1lfwBMLQk8SXTfz6EHHY-S9GrIHNFIHIZgD33HTI6YaM6nUKOnVTpnl38gIgF0OGdgy4Lj9sTXPSbLlmCQnbvK4tXcAAyGFfm8YMU9Cu-1hw8tEVzOpmCeHv_nF1jyWc0zrgMOMUyTHrcDQ96EioBFDIsa-R4HMgggbLIDK0D-8msMfqq6LlgeAWUnpo6b0jnv6vgtfGDaVJhpojIbRdHAEpIQIMlAMh0AVXFf5pbdEgiiwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16d4c4b759.mp4?token=P9YqY3ULzRRGos5Gea08D-hq2tkzGO5hofKRn3zc-ge_rkTfCbTDrw7GkOT32WTxQvX7fghPCjSeV4I48jMfZH6zzR0sHzHfGubO0ov7bn9PjyFkaknuu7nuRMVh6_bzNNSm--b-ui6sjWhkngUfoP2x8jPg-YQH5nPQHXGb5ioUGx52ekEiIX9UVxQUNjmQ_2zXjCf1RoOJCfjx9VblPCZQnCY56BNm8K5EMXyuFxQJEw_vRS7KXTCv5EhohuLsAXDFFVstHnMXgt3Ia10Xp1fQF7WzvwEE56Vpi9aW0xuzGbcpEJWUCK7InIQhuf2HYSCeIJN9lSuyyyfKcWNP2DkUH6oOsot4eM7ivGEIBiLAJ20ftOKNw62DtGGczG8X8K8nha7qDyM3Z_C1aEUc6HVGD1jbvY1t_kwzyEJZc7RCgng3i4Vms6W8iMJ1lfwBMLQk8SXTfz6EHHY-S9GrIHNFIHIZgD33HTI6YaM6nUKOnVTpnl38gIgF0OGdgy4Lj9sTXPSbLlmCQnbvK4tXcAAyGFfm8YMU9Cu-1hw8tEVzOpmCeHv_nF1jyWc0zrgMOMUyTHrcDQ96EioBFDIsa-R4HMgggbLIDK0D-8msMfqq6LlgeAWUnpo6b0jnv6vgtfGDaVJhpojIbRdHAEpIQIMlAMh0AVXFf5pbdEgiiwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
استمرار المعارك بين عصابات الجولاني والفصائل الدرزية في محاور محافظة السويداء السورية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88922" target="_blank">📅 02:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88921">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
🇮🇶
الخارجية الأمريكية:
الموافقة على صفقة محتملة لبيع مروحيات للعراق بقيمة 800 مليون دولار.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88921" target="_blank">📅 02:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88920">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/646c905c1f.mp4?token=Nx6rNInlJHjZArbhl1ap0xf5QnonliDuC78COHzcaTjhfMxIjHS-M5XdS8eDjRl7qCw6Mtwb6QV1wCdyPx_D6sM2xCsOptoc_PLb34RCjXMMBFrcDhUBax6-RgixLnvxiyXIPP3wW5ynILusHohvX0qNy2MSarpR4tXATW_SY48F4Sy-O6jzFAPGVoOkya_9g9MZy_ppeJ9dNlM5khmp5mJ_dFhkBLJTFoEkzTaPB1fNAd29N9IDcf68OFAwu0DMnLemC7PtK3pmg59y6UWcL2j1NC9qLn-qGM2h_cH4tfF0liAZIXzyGVsbGdFTd15jwONhLcp1G4CVCxqf6zvTVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/646c905c1f.mp4?token=Nx6rNInlJHjZArbhl1ap0xf5QnonliDuC78COHzcaTjhfMxIjHS-M5XdS8eDjRl7qCw6Mtwb6QV1wCdyPx_D6sM2xCsOptoc_PLb34RCjXMMBFrcDhUBax6-RgixLnvxiyXIPP3wW5ynILusHohvX0qNy2MSarpR4tXATW_SY48F4Sy-O6jzFAPGVoOkya_9g9MZy_ppeJ9dNlM5khmp5mJ_dFhkBLJTFoEkzTaPB1fNAd29N9IDcf68OFAwu0DMnLemC7PtK3pmg59y6UWcL2j1NC9qLn-qGM2h_cH4tfF0liAZIXzyGVsbGdFTd15jwONhLcp1G4CVCxqf6zvTVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اعتقال عدد من أصحاب المولدات في عدة مناطق من العاصمة بغداد، بعد إعلانهم الإضراب احتجاجاً على حصة الكاز.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88920" target="_blank">📅 01:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88919">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1a03803b.mp4?token=hb2mgLTcHpbFRrzxxJUzATcasZH4VzBZhF2qVmNSb274zai5w1Lfj6f8MZZkVV8U5UL-AgquAkm0Kp_KDIwgzszp5N12dT8TcMMfDXdYV_RlougQl9zlTryM64wOl3EJhDMX_dXAAIbxRnW_qrXqbW6rNykH1-G2l5lNwZeaNq4letZj-20TR8c-hBwX6c3G-S40w_NjB_4Of1BR4V5uVL3GQX6kkW8Vq5l73zJF9bKW4JkieZYSxxYwllSVLnDlpQoJnw-waEzvhhROnWwYoGA5c3hdKy0HFjar-CVpqKG4cNopaQU_jf7Ts_deQYZYIE8WGnstvHBZEiNyqMhTYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1a03803b.mp4?token=hb2mgLTcHpbFRrzxxJUzATcasZH4VzBZhF2qVmNSb274zai5w1Lfj6f8MZZkVV8U5UL-AgquAkm0Kp_KDIwgzszp5N12dT8TcMMfDXdYV_RlougQl9zlTryM64wOl3EJhDMX_dXAAIbxRnW_qrXqbW6rNykH1-G2l5lNwZeaNq4letZj-20TR8c-hBwX6c3G-S40w_NjB_4Of1BR4V5uVL3GQX6kkW8Vq5l73zJF9bKW4JkieZYSxxYwllSVLnDlpQoJnw-waEzvhhROnWwYoGA5c3hdKy0HFjar-CVpqKG4cNopaQU_jf7Ts_deQYZYIE8WGnstvHBZEiNyqMhTYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ظلام دامس يخيّم على عدد من مناطق العاصمة العراقية بغداد بعد إطفاء المولدات الأهلية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88919" target="_blank">📅 01:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88918">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
أمريكا تنهار من الداخل.. وول ستريت جورنال:
‏استقال وزير الجيش الأمريكي دان دريسكول بعد أشهر من الخلاف مع هيغسيث.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88918" target="_blank">📅 01:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88917">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇸🇾
اشتباكات مسلحة بين عصابات الجولاني والفصائل الدرزية عند اطراف محافظة السويداء السورية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88917" target="_blank">📅 01:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88916">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb9c56e9a.mp4?token=p2pm689QmrXPc_5r5Yvapqv-MscxeWHs2XNqMtyxiQqDyoHxQpROf812rWcPatVceLlSiifeWs2yvBeVlz4S4H0h_nS13MGRTp478v8pJNAN9AzQFtKQLijXMVDXN9eYR9d5Mf6ZnnQzXec-aFRfOKIlQAXfzp7blNxJs2nQgEolq7QT9-x26cXEzFboFikzgnhS0YGBQge-s8S8B0oa3f5YfYRQqAVYzy4_X-jnYe8dMYEqAUyxV97aQIcPljcj_aHounxlU46ZgjifVhi25pZwY6e0W9ZRqXTT7xDJlOfFQm6PdG9YO9ljzt2mie5Zgo3RToh3Oa3cyjFc9tlB9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb9c56e9a.mp4?token=p2pm689QmrXPc_5r5Yvapqv-MscxeWHs2XNqMtyxiQqDyoHxQpROf812rWcPatVceLlSiifeWs2yvBeVlz4S4H0h_nS13MGRTp478v8pJNAN9AzQFtKQLijXMVDXN9eYR9d5Mf6ZnnQzXec-aFRfOKIlQAXfzp7blNxJs2nQgEolq7QT9-x26cXEzFboFikzgnhS0YGBQge-s8S8B0oa3f5YfYRQqAVYzy4_X-jnYe8dMYEqAUyxV97aQIcPljcj_aHounxlU46ZgjifVhi25pZwY6e0W9ZRqXTT7xDJlOfFQm6PdG9YO9ljzt2mie5Zgo3RToh3Oa3cyjFc9tlB9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ظلام دامس يخيّم على عدد من مناطق العاصمة العراقية بغداد بعد إطفاء المولدات الأهلية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88916" target="_blank">📅 01:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88915">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حدث بحري لسفينة عند السواحل العمانية بمضيق هرمز اثناء محاولة عبورها المضيق.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88915" target="_blank">📅 01:05 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
