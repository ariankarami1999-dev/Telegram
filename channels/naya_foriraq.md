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
<img src="https://cdn4.telesco.pe/file/aXLDrCXDXLMt8kjygfAojd2LN9q9lfAMvhxzhYmsGKhTXzrPbOcLFEo5eyxUqzVhzCHDHHZTbU_A1JSyZl5D58jgZ2HPnmWJh1UhXgGk_rICgk5eiO_3w3U1pfwhU_SsWIczn4FvvIqWyKGnyNM1eDnsqmtmwDWTKrZ7crv2az3wkH1RFBRpDj8UAOSbEdQPx3Z3fx8LytkqfHvmPPQhixd4hWXRaJNnobn6Uubmm8KJrS-wsoSzNZXB3hiA1IE7DlutvBBLwWX3aeplBY6aDtQUPfhshEVUGI4qLw8DJV8hrvgIwDwfK8JsTlKLNFkuR5zshNVw2_3jIRu5SP1CKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 13:27:39</div>
<hr>

<div class="tg-post" id="msg-89650">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عدوان سعودي على مأرب اليمنية</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/naya_foriraq/89650" target="_blank">📅 13:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89649">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">عدوان سعودي على مأرب اليمنية</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/naya_foriraq/89649" target="_blank">📅 13:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89648">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4qsZ___VZ3Ely-DttKqYVIBH0tWljeLfqj2pA6I0qM0xvtxXdlnBTk7iX-1sXUw-QcjCyoqH0EzgHpwqFAzcW5CM8JgPfAkrFogLxagyW0-Ekiolkq8nspwl9pv5_nzuVKDVH5tABTHXaLt8R-83_bKYHR2Aq6TujC2Z44D5yf-yWN9CdCJ-qQf8HZop_QmfV1iJ_dtZIKYOYrABtrl0kDQ3fZ-Vwjgs_eWBGDY4rmlO-T4RW8rb8oOPtKSUZGDuILbHRD5dQEjhZTfpX1pYTgeUQRmzz93x_Gdk9H0vSGzAvooC0cOFV0r2SlDWzDlnrFv0ZCNIt95JRIjfNse4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحرائق متواصلة في جازان السعودية بعد هجوم القوات المسلحة اليمنية.
توني جاي من جازان ومافي شي
الوضع كويس</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/naya_foriraq/89648" target="_blank">📅 13:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89647">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
🇺🇸
قائد الباسيج في الجمهورية الاسلامية لترامب:
إذا كنت قد قضيت على القوة البحرية الإيرانية، فلماذا ما زلت تقاتل في مضيق هرمز؟ يجب على الحكومة الأمريكية أن تقدم حسابًا لشعبها بسبب إشعال الحرب مع إيران. وفقًا لاستطلاعات الرأي التي أجريت في الولايات المتحدة، يعتقد 60٪ من الناس أن إشعال هذه الحرب لم يكن له قيمة.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/naya_foriraq/89647" target="_blank">📅 13:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89646">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇷🇺
🔻
الخلافات الاوروبية الروسية تتصاعد وهنغاريا تطرد 10 دبلوماسيين روس.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/naya_foriraq/89646" target="_blank">📅 12:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89645">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28761bb29e.mp4?token=GzHHZaI3wzqojwQqyNlOkqQIWyllj2ZIgZkKsZTGsY_2LVMWBCHlmUuYBG_d_snpHcPz0bocamUsYmTNJCQJUg5qMNADCzWFx8J21vKFYWOoA0U1XqV_j_zEoxBC9GLOhJnbnl08K3vb_pA-Cm3gW3XdFD3XkTBbUWx6G8Fy54bJAbWB6tto7MWLzdo1FyIisLSkxHISsmDO93JYGA6lt0vMJtftIcV-jMF94pqtRxgG2X98Mm1SlLk1AnBtD1t6cHswUzCTGB8H4WjN5yAUEwQWR9AguanIirE2GnLpsu7OZxhljQHNtTgOz9fsZaeCgJn21bRzeM6jNrhCZTSmPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28761bb29e.mp4?token=GzHHZaI3wzqojwQqyNlOkqQIWyllj2ZIgZkKsZTGsY_2LVMWBCHlmUuYBG_d_snpHcPz0bocamUsYmTNJCQJUg5qMNADCzWFx8J21vKFYWOoA0U1XqV_j_zEoxBC9GLOhJnbnl08K3vb_pA-Cm3gW3XdFD3XkTBbUWx6G8Fy54bJAbWB6tto7MWLzdo1FyIisLSkxHISsmDO93JYGA6lt0vMJtftIcV-jMF94pqtRxgG2X98Mm1SlLk1AnBtD1t6cHswUzCTGB8H4WjN5yAUEwQWR9AguanIirE2GnLpsu7OZxhljQHNtTgOz9fsZaeCgJn21bRzeM6jNrhCZTSmPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
في العاصمة بغداد... مشاهد لاحد رجال الامن وهو ينهل بالضرب المباشر على احد المتضاهرين الذي يحمل شهادة الدكتوراه.</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/naya_foriraq/89645" target="_blank">📅 12:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89644">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36af9ff10.mp4?token=TOONiM1-GTciu-MegtfmExDTFmY2CJ9z8zS4LdMJs2FGNgyYJk47cqc9HwXcuMvJwZmyy42BkriycWIB7TCN-ZcraMaOsBTMNPJj_qRbT7PGlTDT36pvZfbRKqm_rlLwvqWYKFzUf18PzV53kqNaV7ZP4FknNoaIqNfk06t1prSIYB_6WPvH4ZxcwCslZ-Z667Us2q5FR-p0T9oQcI6NR3Iqkv48mQlQN0KNOm5qPW_fan-sp4wzXGGecKF4eBuh7pD46Lmo3SLk4CHH3S0ZpbYz0rsGXaIfO-1i4FZmYbHcMH81fCt4LrON96ariBSpJ2ktBFzp--Ux0Y4UDw1tpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36af9ff10.mp4?token=TOONiM1-GTciu-MegtfmExDTFmY2CJ9z8zS4LdMJs2FGNgyYJk47cqc9HwXcuMvJwZmyy42BkriycWIB7TCN-ZcraMaOsBTMNPJj_qRbT7PGlTDT36pvZfbRKqm_rlLwvqWYKFzUf18PzV53kqNaV7ZP4FknNoaIqNfk06t1prSIYB_6WPvH4ZxcwCslZ-Z667Us2q5FR-p0T9oQcI6NR3Iqkv48mQlQN0KNOm5qPW_fan-sp4wzXGGecKF4eBuh7pD46Lmo3SLk4CHH3S0ZpbYz0rsGXaIfO-1i4FZmYbHcMH81fCt4LrON96ariBSpJ2ktBFzp--Ux0Y4UDw1tpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
في العاصمة بغداد...
مشاهد لاحد رجال الامن وهو ينهل بالضرب المباشر على احد المتضاهرين الذي يحمل شهادة الدكتوراه.</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/naya_foriraq/89644" target="_blank">📅 12:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89643">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbBRxD-3XnZiEdxOSD1Fw3pVorQaWB4gmsmTlxr9RtlC77j3Ir-sIm9sr7DRccdPwLzL_NW-0ZtNIC-QdJMwyDCFZQbx0HRKUJq8R-IIg8ZFCc5rGZAFV2AJUiwADUZuSVCuzOwyduyaQw2izyXmdqaTAfw7Pq2Cmn_bvEgvUk3ObkcM9yuxs-HH8PzBujxPP4ajLGSf_nCGkSNUL2gDXwkOhaE50eDZn-Spjs304JxWwBjtiMasDJnSDen9OB_OYKpYkKtSlzVWEPiwh043Lcz3p0sTIH98HuIPfZeO_384Dgc0NMqnDm47qAzqAJdc5dZZ_w7ShQgicRIABqP9eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مع تصاعد الدخان من المصافي النفطية في السعودية.. إرتفاع أسعار النفط العالمية حيث سعر البرميل الواحد أصبح يلامس 99 دولار.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/naya_foriraq/89643" target="_blank">📅 12:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89641">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f329323008.mp4?token=PxtSPsEIqsmE1R-uYRha0habh42znGuiUWHZwsl3-hms8NKfanxXoDzqQlQ9mZ3VhWWOv3NbhB6_hitBvgGCIpqkv0dTFGYdmZg65NA8gibyk3YFrxjNzyFvst7qlM27RUTRKYOPYmTAnucFYXsdrZXvQ19PB6vSDAQCuzjLmIcPiZszN33EeOwgxPhEqSdOGCyFuGqJ2nGVDgx3VE1zc2RNpx1QK93u9-6AXLXe4rN-XW1fCevA1l4KHH-q5kxXhLAK_4zfqLQSmvCd4Zlz6xlpiiJzYQ6APw-3btJRAe8yn8xrmakQhi6WlXtsIiZAMDlbHfb6X4yDSnhzOCCshg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f329323008.mp4?token=PxtSPsEIqsmE1R-uYRha0habh42znGuiUWHZwsl3-hms8NKfanxXoDzqQlQ9mZ3VhWWOv3NbhB6_hitBvgGCIpqkv0dTFGYdmZg65NA8gibyk3YFrxjNzyFvst7qlM27RUTRKYOPYmTAnucFYXsdrZXvQ19PB6vSDAQCuzjLmIcPiZszN33EeOwgxPhEqSdOGCyFuGqJ2nGVDgx3VE1zc2RNpx1QK93u9-6AXLXe4rN-XW1fCevA1l4KHH-q5kxXhLAK_4zfqLQSmvCd4Zlz6xlpiiJzYQ6APw-3btJRAe8yn8xrmakQhi6WlXtsIiZAMDlbHfb6X4yDSnhzOCCshg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
حملة اعتقالات تطال متضاهرين من ذوي الشهادات العليا.</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/naya_foriraq/89641" target="_blank">📅 12:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89640">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6ykv1JodtgsAq-vDszFLgv-EHoqRFXllIAg9LNAAHtjl3O4e4u77I3-kMNLMnGvfQPEwY5PFX2edN0bxKzYpNN3-Mg6INfzkCIDm-ygs43KyjeJy0wwPtVPqhwU7N7FbVFmPr-T9w0IoX-I4glBZkTGa3K_c4L-_go55mSkzfkk1FPjzqggw5mNOBWACrFLwom3Ld_iL-cojLMkcLlvhJcYZLM2rlfQkO1rRNXK8VmeOcsgEhznfYmbf93mf6JfU01ISVRbXzhJcaxl5zoX0JyhjZ0y_GdETUS32fQqM-KTZELi4_XxkqIYp9rPKHNeI779ujDSGYqm-VZDyoyZsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇾🇪
🇸🇦
اعمدة الدخان تفرض سيطرتها بسماء جيزان السعودية.</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/naya_foriraq/89640" target="_blank">📅 11:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89639">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d84cecfa.mp4?token=dAWMXEIjm7u6GOjlqtAbkBXqGnxsiMJQ2Bns1iCHfhzxZfJFhX988sC2111XNYHnbNd2tGIr8bAMlmsUtctPPzs3PQ0kab5OLox6CFaDVy-RzW0SCtIrshDHZQKTE1LQisOkf0MUum46HVEwF6bdgwNi_ETRdHlAtk0yY3-OhpdkDkkApex8afHWS2A7tZMaxG_ekomyTRHiN3yLOLD5IlKlrdKs7Wxf6KfbGEH6oixHvgNELPVZd62GktE8kKC3zyfi12FItmyoyfumTjIJuqZ1VjSVMsXUrfbuFxD8E1A9GrDJS4XZxpePN754MV0LDZUvTkcnTlNPDI7SKc4Ijw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d84cecfa.mp4?token=dAWMXEIjm7u6GOjlqtAbkBXqGnxsiMJQ2Bns1iCHfhzxZfJFhX988sC2111XNYHnbNd2tGIr8bAMlmsUtctPPzs3PQ0kab5OLox6CFaDVy-RzW0SCtIrshDHZQKTE1LQisOkf0MUum46HVEwF6bdgwNi_ETRdHlAtk0yY3-OhpdkDkkApex8afHWS2A7tZMaxG_ekomyTRHiN3yLOLD5IlKlrdKs7Wxf6KfbGEH6oixHvgNELPVZd62GktE8kKC3zyfi12FItmyoyfumTjIJuqZ1VjSVMsXUrfbuFxD8E1A9GrDJS4XZxpePN754MV0LDZUvTkcnTlNPDI7SKc4Ijw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇾🇪
🇸🇦
اعمدة الدخان تتوالى بالارتفاع من مصفى جيزان في السعودية.</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/naya_foriraq/89639" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89638">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYOxQyCBgdjVT8uhY5Dmnw2aiyDAC6yJfqR4A3DCvqZ1_aCu_gWNQMrOdVRsEnv_vcvjjqZ86t7aBs1n8aXlRasUNjTNzAjrWR6BKhZ3rA8_RHwMjA8XfnmQyWJydCnA69EfVMquzHbL7ghohy1R1KjgY8rdj2xHPObgHy-nZtYvb-ijYt67MFb04yd89nvY5X7FpR_vRGIdMhi-MvA-2KtoradqHLK4ftn92LjEGShQuG_Rj3Da3HGnCP__t5aLs9ctJSLVD030PC-qY8XmjU4eoPyivOfCT8SlqJ8ZFcN8yEw7o8FZrmBWmb0H7XyZS6bcRZhNPPvwvob5i8tcrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇾🇪
🇸🇦
تضهر ارتفاع مباشر لاعمدة الدخان من وسط مصفى جيزان في السعودية بعد استهدافه من قبل الجيش اليمني.</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/naya_foriraq/89638" target="_blank">📅 11:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89636">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇾🇪
بيان القوات المسلحة اليمنية سيكون في تمام الساعة 10:40صباحاً، بعد قليل.</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/naya_foriraq/89636" target="_blank">📅 11:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89635">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/naya_foriraq/89635" target="_blank">📅 11:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89634">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93d7819112.mp4?token=shx_YaX-MZugJzq-PqjGCWyX8ECMAw72Yqrj7jF_RoffPQPi7SCY3cJxp1BZge_A5vgOGTWoZ7hzTI04aRRAEPd_GNOT09DkYH_mXG38RNUYLWcZDYRXvC2DjQuTXjvbNPvqeWbFYyG-_rbscAi1pjqOkQoIn2Ehx8Ulb1SGF7nKNnajthYa3CadNJDo5DP8cYi51d_mGJ3A_rBhJ1p28_oaKe4pWFpzg3rnkVRoydHXyo_hH92muSjI5eIM60OVX5ernJ_PdoRHqwFwkKengq77impZihxD900vQWgA_vSEymmrpLHKmFUdvKJOJyb9cvA4IsP1aYWZy4nxv-f_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93d7819112.mp4?token=shx_YaX-MZugJzq-PqjGCWyX8ECMAw72Yqrj7jF_RoffPQPi7SCY3cJxp1BZge_A5vgOGTWoZ7hzTI04aRRAEPd_GNOT09DkYH_mXG38RNUYLWcZDYRXvC2DjQuTXjvbNPvqeWbFYyG-_rbscAi1pjqOkQoIn2Ehx8Ulb1SGF7nKNnajthYa3CadNJDo5DP8cYi51d_mGJ3A_rBhJ1p28_oaKe4pWFpzg3rnkVRoydHXyo_hH92muSjI5eIM60OVX5ernJ_PdoRHqwFwkKengq77impZihxD900vQWgA_vSEymmrpLHKmFUdvKJOJyb9cvA4IsP1aYWZy4nxv-f_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇾🇪
🇸🇦
صباح اليوم من سماء جازان في السعودية تضهر سحب الدخان الكثيفة الناتجة عن احتراق مصفى جيزان بعد استهدافه من قبل الجيش اليمني.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/89634" target="_blank">📅 11:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89632">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6OqEgMY7HxlrekYt71zTQkorr2USiQl_dQnPkPGFhAK-c4dvZ351HqNy-aLtMViFdr_T2CZplWYARCLur_-Z1fNyCT78Xhm2ydDxszbrjjrOBU9qm90ovNw-U9m5RsJNRejWzcGvHfcHxDvbqMB6nQ4HIdEx49sD2Wz_U4eEK2AxB_T5IE6otpMX3O7ca4bQZa7DTU7OmhDLvpjyB60hYGTPttECHB0lRF6NK2I0O6luVwmahvaJLi8WlKTJDBAUfazwumcuam-mZYaGGT6zAsdcpbIN8hNiVSy9l3m_E1QfuiR1Vj858uvJtU7rxDd1iyo3kNnQQudkbEywLyQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NggdzwyDEiToUg0Z0PyO_jcAPNVu0zg-MzzEr8ho2o-sxA2jiiQT1VOm1VAILsj9MXY6T-I3qGzVY94td-qkL-vVHnKy4Eso1Cgm3IDGq7udgtmiMB9vTUogeK993UEIKq0oM4wXPhH1YcNP7pHGAhPUNeAzNtSG0IbOItqlhbJyR4UBCvOeI5bKDjcoYu1GHWbkntSz0Zt-_GKKeq5gcuiE_xjCx4iGExYqbMLMEJoImlNWD-aoTRa6XMvh-CLvoRSIJ2whwc9lIrfwYw5UMxoJpNODWLykLa8u6eg1HnMIFS4w-oGDgSSY5RM0co9LvRP-7Q7Py13TXKtT_8ivbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد من الأقمار الصناعية تُظهر سحبًا كثيفة من الدخان تغطي سماء جيزان جراء الحرائق الناجمة عن استهداف مصفاة أرامكو في القصف اليمني الأخير.</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/naya_foriraq/89632" target="_blank">📅 10:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89631">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نايا - NAYA
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/89631" target="_blank">📅 10:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89630">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be6967c380.mp4?token=DlRh5ZWXQaoqImf-t8raAeqwZvMSY30S4QeBJ5lwzwc07yYYOvS91dqhTzEgoNjPhAiib-PbZdu0A7a4XCPwtUh6FwZ4tEY0E1_03mv2jYUYSL4CzIrxySDM4lXO5n05VLoORr_AjpDsEdzYon3LVHcu3JrDfkmRLhjOstFq9Oullni15K1yLMdBv5pbLYmL8EgJlint8Oqfp0l7Mkp9dfh8r1okxM_UndR-1V1G4na97CyiqwnJ8ihC8_HwmoK8OYl3R3wLKw8lC2KOnlRMDzQOeRDlqDfdgbuUWcv-RQCvFENC3Dra1cLra6ZRPUD3vNvLgqgfRslR-DxmX5XlQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be6967c380.mp4?token=DlRh5ZWXQaoqImf-t8raAeqwZvMSY30S4QeBJ5lwzwc07yYYOvS91dqhTzEgoNjPhAiib-PbZdu0A7a4XCPwtUh6FwZ4tEY0E1_03mv2jYUYSL4CzIrxySDM4lXO5n05VLoORr_AjpDsEdzYon3LVHcu3JrDfkmRLhjOstFq9Oullni15K1yLMdBv5pbLYmL8EgJlint8Oqfp0l7Mkp9dfh8r1okxM_UndR-1V1G4na97CyiqwnJ8ihC8_HwmoK8OYl3R3wLKw8lC2KOnlRMDzQOeRDlqDfdgbuUWcv-RQCvFENC3Dra1cLra6ZRPUD3vNvLgqgfRslR-DxmX5XlQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇾🇪
🇸🇦
صباح اليوم من سماء جازان في السعودية تضهر سحب الدخان الكثيفة الناتجة عن احتراق مصفى جيزان بعد استهدافه من قبل الجيش اليمني.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/naya_foriraq/89630" target="_blank">📅 10:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89628">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c1b5f5d8.mp4?token=bNcEKCBL1wkKiqOIcbDNc1ho2NlMpho7C1h-bZrMAByOXpkZ9H6qV859cxwxlEji7n454cEgzgmxs4JDb2i90y5uadGf1tf9ozRDhhjCbn8BLXuL1RYkmq73AUnKMvMrLO6OOuMXWwLLrYVhdq0wldp042I4GUCoop8gaTeb8O-ClNgAUTRI9I5yjHYJrRrmUPDtHh68G2U8R1AGjCVnupSmyyNhLG1k2wl52MBU1jNlW9uwTzSr_tDNM7BUyw7a9nRK9VDgpElrVFkHvrcFaHVb48MuJXVL9Yup-b777Rnxlo9Xr4jF9hnGaPnAhix0EFX2PA7yOC3Ly7mos84QlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c1b5f5d8.mp4?token=bNcEKCBL1wkKiqOIcbDNc1ho2NlMpho7C1h-bZrMAByOXpkZ9H6qV859cxwxlEji7n454cEgzgmxs4JDb2i90y5uadGf1tf9ozRDhhjCbn8BLXuL1RYkmq73AUnKMvMrLO6OOuMXWwLLrYVhdq0wldp042I4GUCoop8gaTeb8O-ClNgAUTRI9I5yjHYJrRrmUPDtHh68G2U8R1AGjCVnupSmyyNhLG1k2wl52MBU1jNlW9uwTzSr_tDNM7BUyw7a9nRK9VDgpElrVFkHvrcFaHVb48MuJXVL9Yup-b777Rnxlo9Xr4jF9hnGaPnAhix0EFX2PA7yOC3Ly7mos84QlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇾🇪
🇸🇦
صباح اليوم من سماء جازان في السعودية تضهر سحب الدخان الكثيفة الناتجة عن احتراق مصفى جيزان بعد استهدافه من قبل الجيش اليمني.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/naya_foriraq/89628" target="_blank">📅 10:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89627">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇾🇪
نائب رئيس الهيئة الإعلامية للجيش اليمني: البيان العسكري في الساعات القادمة، وما تأخر فيه الخير بإذن الله. https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/naya_foriraq/89627" target="_blank">📅 10:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89626">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfc95cc5d.mp4?token=BzS-8dsfvGpfTcfau2Nga_Ll-0rkrAHo1RpF-qkxKDcZZ1rqrkRhcF-Gd6DVEo7h9KFtzzT47hyM5vTuB2CymH7zySAYl0d1GWI5YU3JwXhqi4Us5bnkB3-uN1w0K_ePw0_SispaFfBUMsnjrslpxPGC61VD0ms93uIw_dXepvT9AOVVZcmeHGpjp9-5F4WPAJ0IOFWk9Q0w-33AHDb-OxTbqYn05cgMoL-ppV-lE1RhbZzm3MYO_hkxt-34T59DzfMs3yPNZFmyetde6PqboUJ51svLvEqYDQw9H5C8pHcz5f8nS5_BeBcMbZiZDYn66P3iTPs7T7k-rVR-yjPsFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfc95cc5d.mp4?token=BzS-8dsfvGpfTcfau2Nga_Ll-0rkrAHo1RpF-qkxKDcZZ1rqrkRhcF-Gd6DVEo7h9KFtzzT47hyM5vTuB2CymH7zySAYl0d1GWI5YU3JwXhqi4Us5bnkB3-uN1w0K_ePw0_SispaFfBUMsnjrslpxPGC61VD0ms93uIw_dXepvT9AOVVZcmeHGpjp9-5F4WPAJ0IOFWk9Q0w-33AHDb-OxTbqYn05cgMoL-ppV-lE1RhbZzm3MYO_hkxt-34T59DzfMs3yPNZFmyetde6PqboUJ51svLvEqYDQw9H5C8pHcz5f8nS5_BeBcMbZiZDYn66P3iTPs7T7k-rVR-yjPsFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
أعمدة الدخان تملأ سماء مدينة جيزان جنوبي السعودية عقب دك المنشأت النفطية من قبل القوات اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/89626" target="_blank">📅 10:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89625">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇷🇺
🔻
الجيش البولندي :
‏أنهى سلاح الجو البولندي عمليات الرد على الضربات الروسية على أوكرانيا؛ ولم يتم رصد أي انتهاكات للمجال الجوي
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/89625" target="_blank">📅 10:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89624">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇾🇪
بيان مهم للقوات المسلحة اليمنية للإعلان عن عملية عسكرية واسعة في العمق السعودي، في تمام الساعة 9:30صباحا، بعد قليل.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/naya_foriraq/89624" target="_blank">📅 10:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89623">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔻
لمتابعة الاحتجاجات التي تشهدها البلاد اليوم وتطوراتها أولاً بأول يرجى
الضغط هنا
.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/89623" target="_blank">📅 09:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89622">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvT0SFqhpJQ0murbcWFTMDerLhyAbfRYnVjsIQ45LuFtsnxAKM4HuydU_oiYM0m2SaCc5LrMuO5V_FdZhpRysYdjoCqQjS9lNSBxM2lL0MpMBYe5bOXKI--72c_7tb0-FsYq09AXuAyTgumAivA9SU9NN5TWIDkcwPXQiNP4BlAyh5N-F5k604m9pqCklKc-IFhFtVBf_BGlcad7g7VbSu6yTQrAUTjhm2kJjvmnGVIvsWqqOLm2sC3WOdSgoBtsiTxc0SrpTW_lzqjjj2pTi4z5oY3AcHbtVVYiWriiqCNsfcwy_nw0zP1Y0r9B3LiEDQZh_-vaBml7j6uZ86ss8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
🇾🇪
🇸🇦
تصاعد أعمدة الدخان من مصفاة جيزان النفطي في السعودية نتيجة ضربة صاروخية يمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/89622" target="_blank">📅 09:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89621">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SN7419d_7UfPCkbyhiYwF11-sJ2IOMU57WoYQe8Nqy0dYThTuhk5a7gNMpVHGOJhSlvuwlVe-uIiVvULph3aMwjNAZi7hnIQNlvNVux5AzezmzTzEaF5Z_oXjj6wcD6Q8Zl_5nDNXGmBcxPDTqFvjVU4vydeqXXp3v6hXaUfqNuUV068oIkma7_ZtnPA193qqzHhlRrT5dW6lEU9F0VQfSB0xZoForgXtP582rLH9EMvkZ_UhPnhnHO3SpUckmq6jmol3qanLuhrJeiSdtbKZuw7MYIQBmbPWgTnpXQYTU_lIOxEsGZV3udAqWxDfPUeqQyukScez6G0Eg7_YgJ50A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
‏الطاقة السعودية:  استهداف عدد من منشآت ومرافق قطاع الطاقة في المنطقة الجنوبية من المملكة.  ‏الاستهدافات تسببت بنشوب حرائق ما أدى لتوقف مؤقت لبعض العمليات.  ‏الجهات المختصة تواصل التعامل مع تداعيات الاستهدافات.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/89621" target="_blank">📅 09:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89620">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعترف بتعرضها لضربات يمنية في أبها وخميس مشيط وجازان ونجران وتعلن عن إصابة 73 شخص كحصيلة أولية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/89620" target="_blank">📅 08:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89619">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇾🇪
بيان مهم للقوات المسلحة اليمنية للإعلان عن عملية عسكرية واسعة في العمق السعودي، في تمام الساعة 9:30صباحا، بعد قليل.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/89619" target="_blank">📅 08:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89618">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعترف بتعرضها لضربات يمنية في أبها وخميس مشيط وجازان ونجران وتعلن عن إصابة 73 شخص كحصيلة أولية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/89618" target="_blank">📅 06:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89617">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25f28482b8.mp4?token=a2cbySR--53VmD7Afyl01bdR6GqibCSfZcn838qxG0RJaPiY4ju6D5UBIP2biV0ZkiQ4fSwEqfZXkIfAtoCwQjIHoOy8UBNwrzQ6qdKwfHl2VEGylw_rFx3A9ez9Fg05LA92tPbgDYYz1s7hAxZ8Jtwf7EBcRfNT6aHQ61ORp2WybR_Ib2TxZPwQOkidJGAGjdpOODz-L_Tfi_ZQBFF55OuYL5Y9t5_hu7IlCL7pgUahXrmHm9t-YfYYdBJDprKCr4NMhbkJ2fPtN-3Vu5hp5O6zZ59NAFqjeiirNsztqESrx6Dq-dAuMDu8ZCVi3-OqMZWfGi7NvbqK4ogDR4Db7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25f28482b8.mp4?token=a2cbySR--53VmD7Afyl01bdR6GqibCSfZcn838qxG0RJaPiY4ju6D5UBIP2biV0ZkiQ4fSwEqfZXkIfAtoCwQjIHoOy8UBNwrzQ6qdKwfHl2VEGylw_rFx3A9ez9Fg05LA92tPbgDYYz1s7hAxZ8Jtwf7EBcRfNT6aHQ61ORp2WybR_Ib2TxZPwQOkidJGAGjdpOODz-L_Tfi_ZQBFF55OuYL5Y9t5_hu7IlCL7pgUahXrmHm9t-YfYYdBJDprKCr4NMhbkJ2fPtN-3Vu5hp5O6zZ59NAFqjeiirNsztqESrx6Dq-dAuMDu8ZCVi3-OqMZWfGi7NvbqK4ogDR4Db7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
🇮🇱
إندلاع اشتباكات بين عناصر جيش الاحتلال الصهيوني ومقاومين فلسطينيين في بلدة عقربا جنوب نابلس.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/89617" target="_blank">📅 04:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89616">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
عضو المكتب السياسي لأنصار الله "حزام الأسد":
المناطق النفطية والصناعية والمنشآت الحيوية في مختلف أنحاء المملكة لم تعد آمنة، ومستقبل الاستثمار في السعودية بات على مهبّ الريح.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89616" target="_blank">📅 04:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89615">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇸🇦
إنفجار عنيف يهز خميس مشيط جنوبي السعودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/89615" target="_blank">📅 04:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89614">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇾🇪
🇸🇦
مصدر يمني:
الرد على عدوان وجرائم السعودية مستمر حتى اللحظة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89614" target="_blank">📅 03:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89612">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u1FgiHCHvAV2KKOf7DbRRTWusz6NgxaLs-a0gSzeYqzrDPfP27TfEMafDlFK6K2MLAbw4D4QmWP1IdAzVtIGSTvXTr8NkG6jUaPWWq8N95xdvb_qbPLwfV3sbuLG0wuZT8xkFl-B_MtkqIatu3GN2EcA7aVtc7WEQlhT06Awbmi5kKI43NLNSbi6E7CX7JlhXqrbYjh8T_Ink50MnaQN2FI-egDIu8QrN_GnvYCiDq87jYUTvXHwoyn9UdR4kXl1MQMf4FFaakLyxbyvk3uAkJZXcsYP-YaqxH0jkmb9luCV1h-m5DuL02Ql5gjY8ycCs0gh7MCwx4SlKSNnsXgq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JD-FFDZ6bT10IThuVZPDcUYkMlM16oboDejW59o7Rj6fSuIuAA9WVAqOPgsbq0H1O2AOMMUHAgnN1gENcunSshOBXx8Dcoo0rn4gu5e2Efnl8im0LM8HrUQe2E7gQDZzPM2PLsHta7Eqwdf3PZ5rPeTzQOcmPuXSA_9ibbA91UOA7N0nXg2TxunP6FlZJRioz8Sf-sATJ2_rGmItRBX8UdypvThIOWHw7wWv-ZYhTV0A5sr7lfetfo8nCitcGLYLVhg4R91o0q_JmAMrAXVn1_LeioipBrcI0VVVOmWY_ePN7BpdUaSmpIktAw9WIMKXbTX6b5V6JqrFO6RsHWztvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف منشأة نفطية ثانية تابعة لشركة أرامكو في مدينة أبها السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/89612" target="_blank">📅 03:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89611">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي في هذه الأثناء على محافظة صعدة اليمنية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/89611" target="_blank">📅 03:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89610">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2f5bb5b3.mp4?token=q2Y17_Cehfz0NFUs9Q_lRbsKCDgAWwyPGzufn14Q2fVBpHaOCt2-8N29dRDEcE_mp4Pk7yTo2EhVnPQyqJmg2GVb5zQm6JdGgGONONn1TXTqidqreV6FZrTX1JevC2k1cs1IbHJ7bgk_HJ8M8urumiRYDKiB-YKFjhA5oERrOdPgP2YZaxEQALpS47DSueqr0bvCMpPSf275AqUX_4fDjesj8OHu_k18ms9WlHSQnaNVwTGnLG9wy1UtP4US0lH3iqmeLezJAEFalFt4-tzKxUitXvermThMHgLMk7hySabkkZBHJXDcmouTfXZXOoL3C2yQPa8zTMi4PqRjOexv_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2f5bb5b3.mp4?token=q2Y17_Cehfz0NFUs9Q_lRbsKCDgAWwyPGzufn14Q2fVBpHaOCt2-8N29dRDEcE_mp4Pk7yTo2EhVnPQyqJmg2GVb5zQm6JdGgGONONn1TXTqidqreV6FZrTX1JevC2k1cs1IbHJ7bgk_HJ8M8urumiRYDKiB-YKFjhA5oERrOdPgP2YZaxEQALpS47DSueqr0bvCMpPSf275AqUX_4fDjesj8OHu_k18ms9WlHSQnaNVwTGnLG9wy1UtP4US0lH3iqmeLezJAEFalFt4-tzKxUitXvermThMHgLMk7hySabkkZBHJXDcmouTfXZXOoL3C2yQPa8zTMi4PqRjOexv_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
حبا بالعررررراء
عمي احنه وطنچيه
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89610" target="_blank">📅 03:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89609">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89609" target="_blank">📅 03:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89608">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الله أكبر
🇾🇪
🇸🇦
تصاعد أعمدة الدخان من مصفاة جيزان النفطي في السعودية نتيجة ضربة صاروخية يمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89608" target="_blank">📅 03:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89606">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvSbapMUQnwmYZbigSMcQfsiHx1Q5CHUDRADoZeIYpWZwJXIciRMOu34QoO4QrYPwWLHs-KtOd11_EnnXg_WrwxDtgkoQcKb9AZBHycndr42bHiA3QMHaQauiAPn0HwnHjEKYaYdGXyL5vIUIJlukWnwPH76Jit07AzAXpmGXCcmznvThWXwbbRiE6ULYNXAfqQqu7LOr_6N2KoHXkuuZXhDPNyh7pdxyLuGTKrVrGIu341bn_OdzlimEbX3L5-F-zLxk3bjJGk5CcBJcF3h4I-PzIIMMWJhcP9ANR-b1LSgl_DziaWw-U7ZDFnUs6hCtGi_RQzj46ML3t1UVBD1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
ستنخفض أسعار النفط بشكل حاد عندما ننتصر في الحرب مع إيران ، ستصل إلى ثلاثة دولارات للجالون وكل هذا سيحدث بسرعة ، ولن تمتلك إيران أبدًا سلاحًا نوويًا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/89606" target="_blank">📅 02:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89605">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/89605" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/naya_foriraq/89605" target="_blank">📅 02:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89604">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇾🇪
🇸🇦
سرب جديد من المسيرات الإنقضاضية اليمنية يستهدف مدن جنوب السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/89604" target="_blank">📅 02:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89603">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇾🇪
🇸🇦
إصابات مباشرة في قاعدة الملك خالد الجوية بخميس مشيط جنوب السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89603" target="_blank">📅 02:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89602">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇾🇪
🇸🇦
صاروخ يمني أثناء مروره بسماء المدن السعودية متوجها نحو هدفه.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89602" target="_blank">📅 02:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89601">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f26d82ac8.mp4?token=WWHg8WqraHniIiMsX33-ldG57VNItan8JvPOQ9R9bB5EJ0w1qy1qrHGnGYLBGPkGcpUUjGor_A-TJmZmxZqBuvHnALrX3aCtJ-ihUhKKvsDKmcQElg-pUKsnv3VpbLYfHrwt8bd-jjkVJMl0T7lyPOpt3SCjwINgflflFPB1lvRtigLlTAaZFe_F8fLatInKzuby5XRcl4ceBDc_AGyg1_0WIzPvPoq2bMlgveaVPBZf23dWaiOohZ1lYH8eUbyJslDTB-pxZ2vrqA7lBHwwZs_GmQ8qV4D3sB1aFq3ugU4_uJL7ce_BElQkIUJS43Mnh-d2suNCGuzST9dkx3x-DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f26d82ac8.mp4?token=WWHg8WqraHniIiMsX33-ldG57VNItan8JvPOQ9R9bB5EJ0w1qy1qrHGnGYLBGPkGcpUUjGor_A-TJmZmxZqBuvHnALrX3aCtJ-ihUhKKvsDKmcQElg-pUKsnv3VpbLYfHrwt8bd-jjkVJMl0T7lyPOpt3SCjwINgflflFPB1lvRtigLlTAaZFe_F8fLatInKzuby5XRcl4ceBDc_AGyg1_0WIzPvPoq2bMlgveaVPBZf23dWaiOohZ1lYH8eUbyJslDTB-pxZ2vrqA7lBHwwZs_GmQ8qV4D3sB1aFq3ugU4_uJL7ce_BElQkIUJS43Mnh-d2suNCGuzST9dkx3x-DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقة صاروخية جديدة تنطلق من اليمن نحو أبها ومدن سعودية أخرى.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89601" target="_blank">📅 02:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89600">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇾🇪
🇸🇦
الصواريخ والمسيرات اليمنية تطرب في أبها السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89600" target="_blank">📅 02:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89599">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N36im1lcQP4qZxHHWQhvyM2ZXa5Z36DApYGUIaBZ4h_r86KKV-2Lz1uQJ3kuzzrmqmYbA8e8s-P7rFD0TFl4ydp_tBAanFWEizqsMlx9OtDpMEjkOFykK6Xote7jnl4RcmtBY_oYNpoO-lGSY7D6n5vRQlT48PH46p-a5hFUElu4P-1qB3gf5D83kKNGQPgfyeRv06_jY-SXaFjJGJzrLgGnlZSNiOAW6jumpwH3MuPXjup6wSEFYD3EmP2p6pr3Z760UOGPTH6g_pm-8QSSl4qgHpVPg5zunN6lNzyYYeDVW8-N8dQNTEUZjYfffPGHDnIp3MEam9c7JR5Bh3vIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرب من المسيرات الإنقضاضية اليمنية يدك السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/89599" target="_blank">📅 02:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89598">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/89598" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89597">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">السعودية تفعل منظومة " لا تصور تكفى " بعد فشل منظومة الباترويت   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89597" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89596">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رشقة صاروخية نحو خميس مشيط بالسعودية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/89596" target="_blank">📅 01:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89595">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/89595" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/naya_foriraq/89595" target="_blank">📅 01:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89594">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رشقة صاروخية نحو خميس مشيط بالسعودية
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/89594" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89593">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89593" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89592">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
محسن
رضائي
: ‏في الأيام الأخيرة، تلقت واشنطن تحذيراً واضحاً من الصواريخ الإيرانية الجديدة. سيتم الرد على الحرب الاقتصادية بفرض منطقة حظر بحري عبر الخليج الفارسي وصولاً إلى محيط الحصار. وقد أُعيد تقييم الوضع العملياتي تجاه السفن الحربية والقواعد الأمريكية بشكل جذري.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/89592" target="_blank">📅 01:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89591">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نايا - NAYA
pinned «
🇮🇷
🇮🇶
ماذا حدث في سمنان بايران   تتلخص الحادثة في شجار نشب بالقرب من سكن «نيكان» في شارع كارگر، بعد أن كان أحد الأشخاص الإيرانين في حالة سُكر مع بنت إيرانية سكرانة ايضا ، حيث دخل في خلاف مع عدد من الطلاب العراقيين من دون أي استفزاز أو خطأ من جانبهم ، ثم تطور…
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/89591" target="_blank">📅 00:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89590">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
🇮🇶
ماذا حدث في سمنان بايران
تتلخص الحادثة في شجار نشب بالقرب من سكن «نيكان» في شارع كارگر، بعد أن كان أحد الأشخاص الإيرانين في حالة سُكر مع بنت إيرانية سكرانة ايضا ، حيث دخل في خلاف مع عدد من الطلاب العراقيين من دون أي استفزاز أو خطأ من جانبهم ، ثم تطور الأمر إلى اعتداء على السكن الجامعي الذي يضم طلبة عراقيين . وبعد ذلك تجمع نحو 200 شخص أمام السكن لعدة ساعات، وقام بعضهم برشق النوافذ بالحجارة وترديد شعارات مناهضة للنظام في ايران . ويضم السكن نحو 100 طالب عراقي، وهم ضيوف في إيران، ولم يرتكبوا أي ذنب أو مخالفة. ومع وصول الشرطة ورئيس الجامعة، تم تفريق التجمع، وتبين أن الحادثة لا علاقة لها بالشرف أو بأي قضية أخلاقية حسب ما اعتقد بعض الجمهور الإيراني ، وأن الطلاب العراقيين لم يكونوا طرفًا في المشكلة، فيما ألقت الشرطة القبض على عدد من المعتدين. ومن المؤسف أن البعض حاول استغلال الحادثة لإثارة الفتنة والتوتر بين الشعبين العراقي والإيراني، رغم أن الحقيقة واضحة: الطلاب العراقيون لم يرتكبوا أي ذنب. وان العلاقات العراقية الإيرانية مبنية على أساس الدين والمذهب ووحدة العقيدة والدم حتى اختلطت دمائنا في ساحات القتال وكان يوم المطار بمطار بغداد خير شاهد على ذلك
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/naya_foriraq/89590" target="_blank">📅 00:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89589">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
المقاومة الاسلامية كتائب حزب الله:
بسم الله الرحمن الرحيم
بعد عدوانها الآثم على مقارّ الحشد الشعبي في العراق، تواصل العائلة الحاكمة لأرض الحجاز جرائمها بحق الشعب اليمني، استكمالا لسلسلة الجرائم الصهيوأمريكية ضد الشعوب المناوئة للهيمنة الأمريكية في المنطقة.
إن هذه الأعمال الوحشية لا تزيد الشعبَ اليمني إلا إصراراً على المضي في درب المقاومة، وعزيمة على استعادة حقوقه، وإرادة صلبة لكسر الحصار السعودي الجائر.
إنَّ العدو السعودي المعروف بديدنه الإجرامي، قد ارتكب مجزرة تضاف إلى رصيده الأسود من الجرائم، حين استهدف بقصفه الوحشي الأعيان المدنية في مديرية الحزم بمحافظة الجوف، وهو ما يزال يواصل عدوانه على المستشفيات، والطرقات، وصالات العزاء، وسائر مرافق الحياة الحيوية في يمن العزة والصمود.
وإننا، إذ نجدد تضامننا المطلق مع الشعب اليمني الشقيق في دفاعه المشروع عن أرضه، نشد على سواعد أبنائه المرابطين في جبهات المواجهة والكرامة ضد الكيان السعودي ومرتزقته، الذين أثبتوا للعالم أن إرادة الشعوب أقوى من الطائرات والصواريخ، وأن الحق وإن طال انتظاره آت لا محالة بعونه تعالى.
كتائب حزب الله</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89589" target="_blank">📅 00:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89588">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇦
انفجارات قوية في كييف.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/89588" target="_blank">📅 00:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89587">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇾🇪
رئيس اللجنة الوطنية لشؤون الاسرى في اليمن
: طلائع جيش مرتزقة النظام السعودي الذين شنوا هجوم على أطراف محافظة الجوف تصل إلى صنعاء وقدهم في ضيافتنا ( أسرى).
منتظرين وصول البقية خلال الساعات القادمة.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/89587" target="_blank">📅 00:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89586">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
البعثة الإيرانية إلى مجلس محافظي الوكالة الدولية للطاقة الذرية:
إن تطبيع الأعمال غير القانونية التي تقوم بها الولايات المتحدة وإسرائيل ضد المنشآت النووية السلمية الإيرانية وتلك الخاضعة للضمانات سيكون أقل العواقب السلبية لهذه الهجمات.
‏ اليوم، يتم استهداف إيران؛ غدًا، قد يتم استهداف دولة أخرى.
‏ كن متيقظاً ومستعداً. أهلاً بكم في نظام عالمي جديد يسوده الفوضى العالمية.
‏ فيما يتعلق بالمخاوف التي أثيرت في أحد البيانات حول سلامة محطة بوشهر للطاقة النووية، نؤكد لكم أن هذه المحطة تستوفي جميع معايير السلامة.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89586" target="_blank">📅 23:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89585">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇷
الاعلام الاجنبي:
إيران تحذر من أن أصول الطاقة الأمريكية في الخليج ضعيفة بعد الاشتباكات الاخيرة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/89585" target="_blank">📅 23:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89584">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇱
🔻
انتحار جندي إسرائيلي في كريات جات بسبب الازمات النفسية التي واجهته مع حزب الله.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/89584" target="_blank">📅 22:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89583">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇾🇪
الجيش اليمني يستمر باطلاقة عدة صواريخ باليستية نحو تحشيدات لمليشيات الموالية للسعودية في المخا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/89583" target="_blank">📅 22:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89582">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
اطلاق صاروخي من سيريك نحو مضيق هرمز.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/89582" target="_blank">📅 21:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89581">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
🚀
🔵
إعلام غربي : رصد طائرة مسيرة أخرى في مطار لايبزيغ هاله في المانيا ؛ ويأتي هذا الحادث بعد أسابيع من اكتشاف طائرة مسيرة محملة بالمتفجرات بالقرب من طائرة شحن أوكرانية في المطار نفسه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/89581" target="_blank">📅 21:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89580">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇷🇺
🇺🇦
أنباء اولية عن سقوط طائرتين روسية من طراز Su35 في سماء مدينة كورسك الحدودية مع أوكرانيا
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/89580" target="_blank">📅 21:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89579">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f031a921c.mp4?token=sMHbkMet9NOMLQgODaDS5PxGoDogaPegFZMdCvmyOjJ4c3bh6a4Ljn4gn2RcSulXKn5fHtAsdenDCQKHZGEqw5nWtjc0T9IjTderATVc3WrUc4s-8kiwgiSk6ue2X3SbGuG6pxYbdIe02RZJBjw6XF62rOLH_VmVyqlvPsm-MjJ3b9p3FlmxhE55e6Uhkn9E0GJ5dCtBriZVPj3atbZ1eOAujCwM-Dd9xotPkLym74LjyJJuzia-XA6viwXy4PqQS9O-tZkoqOtWnwqG6XSZ6myNTFaELJkM8kCIM5Q1xBeMWNPCyvpr2iT8X6OX9nUEXSsJnkKhZAbdlEleQSMoTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f031a921c.mp4?token=sMHbkMet9NOMLQgODaDS5PxGoDogaPegFZMdCvmyOjJ4c3bh6a4Ljn4gn2RcSulXKn5fHtAsdenDCQKHZGEqw5nWtjc0T9IjTderATVc3WrUc4s-8kiwgiSk6ue2X3SbGuG6pxYbdIe02RZJBjw6XF62rOLH_VmVyqlvPsm-MjJ3b9p3FlmxhE55e6Uhkn9E0GJ5dCtBriZVPj3atbZ1eOAujCwM-Dd9xotPkLym74LjyJJuzia-XA6viwXy4PqQS9O-tZkoqOtWnwqG6XSZ6myNTFaELJkM8kCIM5Q1xBeMWNPCyvpr2iT8X6OX9nUEXSsJnkKhZAbdlEleQSMoTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مدير الإصلاحية في الجوف: انتشال طفل شهيد وجريحين نتيجة العدوان السعودي ولا يزال 35 نزيلا تحت الأنقاض بالإضافة إلى امرأة كانت زائرة لزوجها.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/89579" target="_blank">📅 20:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89578">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgJlQtY4Camq2CSdsyAbZcfe_9GO7WBz171lNFEsXAVj-BNaHc5G4rH16sfL_h0BeQudVKu2svBv-DRXGZ8hsZhd6QzPB4-xNjkRBNMwoq5yaoszbJQcmas-rfYUYreLvyzJ59QG-aQozitpQTIblsHKz7JZrOtoOip0MHelyBISxUz_UkGPV0upv0tQoAUPTxCUSCGox9KF73XuV_6jIrqmwzxO14EaYVjeUvEJZq4DdqUyrvCk555r2kJvUFaY29kfFgCCBVKQ80vz_yI2fNXST4WPER5lGfn3ERM-GsfHSxbnIGb4laAJ4VLNJIGnQbMGQoTkhvzFGmVM2C5hKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاينانشيال تايمز: اضرار في ارامكو  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/89578" target="_blank">📅 20:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89577">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ee613451.mp4?token=nqRi47XtKKUfCen8mzJ9_CIwqXmdaast6RpeOzoH78pcgZHeqXzO97kMSdAqDedDU-DtJjQfSVi47K1LKjUkXMpTGX2IIBjIhiAOvK6KQGbaDOhiESLpoeivjIlhev5B87q78MSn1BhIIYPYQZePWSxB1oW4RETu6vNxp6HDMTv7ZKjS3fvkhRBgpNJ0SawMKn6M-pdNSfZRFXYNqzYMkTA3eh0B3NQAxjQKJ1IZxDSVZ6EmgTJCxdQlek7h2KkLXHvk5Q7TX3xgQtDRXsmrGgvNXFjyPi9ga337DmHJmLmeX719FUXkZHuDVtyOehwmrjLsq8lEmL3ReOJpO2HAWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ee613451.mp4?token=nqRi47XtKKUfCen8mzJ9_CIwqXmdaast6RpeOzoH78pcgZHeqXzO97kMSdAqDedDU-DtJjQfSVi47K1LKjUkXMpTGX2IIBjIhiAOvK6KQGbaDOhiESLpoeivjIlhev5B87q78MSn1BhIIYPYQZePWSxB1oW4RETu6vNxp6HDMTv7ZKjS3fvkhRBgpNJ0SawMKn6M-pdNSfZRFXYNqzYMkTA3eh0B3NQAxjQKJ1IZxDSVZ6EmgTJCxdQlek7h2KkLXHvk5Q7TX3xgQtDRXsmrGgvNXFjyPi9ga337DmHJmLmeX719FUXkZHuDVtyOehwmrjLsq8lEmL3ReOJpO2HAWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
وزير الاتصالات العراقي: يؤسفني انه تم القبض على قصي شفيق بالجرم المشهود. https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/89577" target="_blank">📅 20:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89576">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_imbDXDFr2zJcAihNXoJYcgi3HTltDZf_idDvWcJu5nmD7AqKrQgjI0Pjf8M6daW5JwFk_zMEbnFCwZPj8BBSEMt04XEiFsnik-13mpAd897BVm1Xk3Q6LhFbfqUdAsuPTC4FzU4DbmHAQoaRVpoV2zZcIkPKYiuRNKVirqb2Dkv1JC8Ao8ZXOGxkCNYkxqpO--3lKfRYDGorEUzhDCIRDVlhIFo5p7ZXS2_xFqI5gDlPcCXidKo4P6_MfiC9NB5ysSpgUDP0D_8gL66bsj3E6KxJjlC7bCTu2MVefOOJfr97ak06jnwiZd0dZ9hbxrfiWIxb6K7p1jmkvz1naFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزير الاتصالات العراقي:
يؤسفني انه تم القبض على قصي شفيق بالجرم المشهود.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89576" target="_blank">📅 19:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89575">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇾🇪
الجيش اليمني:
تمكنت القوات المسلحة اليمنية بفضل من إسقاط طائرة استطلاع مسلح نوع CH4 تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية قبل قليل في أجواء محافظة الجوف، وتعد هذه الطائرة هي الثانية من هذا النوع التي تم إسقاطها خلال ال12 ساعة الماضية، والرابعة خلال ال24 ساعة الماضية، وتم إسقاطها بسلاح مناسب.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89575" target="_blank">📅 19:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89574">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇾🇪
مشاهد مؤلمة من اليمن خلال محاولة انتشال اكثر من 35 شخصا من بينهم اطفال ونساء من اصلاحية الجوف المركزية بعد تعرضها لعدوان سعودي.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/89574" target="_blank">📅 19:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89573">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇾🇪
مشاهد مؤلمة من اليمن خلال محاولة انتشال اكثر من 35 شخصا من بينهم اطفال ونساء من اصلاحية الجوف المركزية بعد تعرضها لعدوان سعودي.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89573" target="_blank">📅 19:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89572">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a93c5e7d85.mp4?token=WRfnKOCZIjw00kZ5VN2z8KvyCqTNL5eYT-EPbmE2XCqysFDvE--R7Y1vhC6QUrIbag_YxLmWoVNTuwgYwwFuD8a6oD3uvjX-eO-N_zKL176Lb9Ujt3hFfiCk_LWJeD3Bb2vNZQdE9k_3kOhC9jeqYRESJ1c4460Bi0cMGb1Cm5wjRvppz-hlF3ww2_6-B3IZH5k-ev5rFbXRvi4i0H86vaUNqkBcSfCyMHRsrqizHFNee7EN8u3dnLfyKqWRrLnEfIi4CRhDvFEGxBLEQv-yigv5vxS0nvoFMkWUgs2Enf8Djmq3pJeeFwgOWqZe2gSU1U8tUFq27FTCTIjwduUSiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a93c5e7d85.mp4?token=WRfnKOCZIjw00kZ5VN2z8KvyCqTNL5eYT-EPbmE2XCqysFDvE--R7Y1vhC6QUrIbag_YxLmWoVNTuwgYwwFuD8a6oD3uvjX-eO-N_zKL176Lb9Ujt3hFfiCk_LWJeD3Bb2vNZQdE9k_3kOhC9jeqYRESJ1c4460Bi0cMGb1Cm5wjRvppz-hlF3ww2_6-B3IZH5k-ev5rFbXRvi4i0H86vaUNqkBcSfCyMHRsrqizHFNee7EN8u3dnLfyKqWRrLnEfIi4CRhDvFEGxBLEQv-yigv5vxS0nvoFMkWUgs2Enf8Djmq3pJeeFwgOWqZe2gSU1U8tUFq27FTCTIjwduUSiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
في مشهد مثير للغضب..
رجل مسن يتعرض للضرب والإهانة لغرض الطشة وجمع اللايكات وسط دعوات لوزارة الداخلية العراقية بمحاسبته قانونيا
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/89572" target="_blank">📅 19:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89571">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇾🇪
مدير الإصلاحية في الجوف: لا يزال تحت الأنقاض 35 نزيلا بالإضافة إلى امرأة كانت زائرة لزوجها إثر العدوان السعودي.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89571" target="_blank">📅 18:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89570">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مشاهد من العدوان السعودي على الإصلاحية المركزية في محافظة الجوف  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/89570" target="_blank">📅 18:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89569">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇾🇪
التلفزيون اليمني: لا تزال جهود انتشال الضحايا مستمرة من تحت أنقاض الإصلاحية المستهدفة في الحزم بغارات العدو السعودي  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/89569" target="_blank">📅 18:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89568">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔻
مصدر أمني مقرب من المقاومة الإسلامية حركة النجباء بالعراق
-النجباء تتابع عن كثب تطور الأحداث بالجبهة اليمنية و الدور الخبيث الذي تمارسه قرن الشيطآن السعودية بحق الشعب المسلم في اليمن .
- المصدر ابلغ نايا بأن النجباء قد يصدر منها موقف ميداني بالتشاور مع باقي فصائل المقاومة بالمنطقة حول الأحداث باليمن .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/89568" target="_blank">📅 18:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89567">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇾🇪
التلفزيون اليمني:
لا تزال جهود انتشال الضحايا مستمرة من تحت أنقاض الإصلاحية المستهدفة في الحزم بغارات العدو السعودي
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/89567" target="_blank">📅 18:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89566">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/89566" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/89566" target="_blank">📅 18:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89565">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇾🇪
🇾🇪
المتحدث باسم القوات المسلحة اليمنية يحيى سريع:
بموازاة حصاره المستمر على اليمن أقدم العدو السعودي على خطوات تصعيدية بشن غارات جوية وارتكاب مجازر والتي كان آخرها مجزرة الجوف وتحليق بطيران التجسس وإمداد مرتزقته بمختلف أنواع الأسلحة.
إن العدوان السعودي المستمر على اليمن لن يبقى دون رد وعقاب، وعلى العدو السعودي أن يتحمل عواقب إجرامه بحق الشعب اليمني.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/89565" target="_blank">📅 18:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89564">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇶
🇮🇷
القضاء الإيراني:
صدور الأوامر القضائية من المدعي العام لمركز المحافظة بحق شخصين من المتورطين بالاعتداء على الطلبة العراقيين واستدعاؤهما إلى الجهة الأمنية المختصة، فيما تتواصل التحريات لتحديد باقي الأشخاص المؤثرين في وقوع الاشتباك.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/89564" target="_blank">📅 18:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89563">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇾🇪
معارك واسعة بين القوات المسلحة اليمنية ومرتزقة السعودية في محافظة الجوف.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/89563" target="_blank">📅 18:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89560">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvPYsXm-FeudJxbZAfE4pm-_9k1t4h_OWkPZ9RFkdiG1soHWNN0bzCy2uBUFBfyWqseYqQmLwltAh_NWSD1S4eHSsYiFDQZZN9WdXG5hG50HHYjHs-oQnGLg9HdGpsQrbZioKJSPepU131BzM7TlaCZhUmWov4FYTSXLM7qEJOumsvVcrWNTBz-U7hyQfYcuIZsAKP8Z8t5NzkhUvKMFS1MwNsQzplK-exH_3-FDt-h5RP7YEUoU9EcjW8xCXSGcs-3-WwGp80ELkkCQ35r2A1BUYTmAilAb7xmtSBncSMun6KEab82PlKoLea_245wxBrEc4c67z7fbR0Im0y-x_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s0L4gTJm5sJqkhdW86XypqiZVVjoCSaqNarMFs_iTrORFaTW34GhyFonySqkTKZK--eJKuMOFiapa3Ez_uhnP_x5Rzd4fXJVxGqr34KTcFIBI0HXK51KdAE4iysaBgrz4zRnb91-bdoQr-Zbi9_49-6RYAsqVQAiiV_cpCTaGJwrax53dsVKNOwVONMmTQdIQij_602VXJT-_09qKhFkmklpLRA2bsGGUA2YpFHMLKRc-wUBao5iR0UuXSokqvGlUHE3NvV6c4GHGQ3t5FJ2HgnKpiiCk7y1DFjBV-dfrStGEgsUY_4xxeqIe15hPjergNslz06FymSmk2niN-9nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t24vfYufjOcuZfo9dN1chQROScR29W_3pJQ6m0x39UIdTD_gkheHgFoicDPfU-LRzZvUecI7sXorrv_9A_259GAG1pNBQT-XppzcR23kNuo1C90CWndjEDVXY6iUWVyHtAJyklzliFkeOuT2zUH8OPqLmv5BQyKG9NKLf2_idm9w-KaKo8JtqWQDtIij_GbGRHRukEZ9yUeBM-pvBQyPmxXAER0jWQzyzSlxnF6PIAw34-g2P5hSRZyCenRbi8bZF4T_j2UyXMq4g-KfQY43tLPJbxQ__0qzZJAzuu0QGcUJGAYMP9Qf2XYWfKGJnxyJS7OoqPUPl2BYbQYDnLCYSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عدوان سعودي يطال سجن الجوف  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/89560" target="_blank">📅 17:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89559">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj2bchhFjOlJlO1boM1DSd7RnPVoF7BTb-X3EPvmoVGjgGDFaN4Tx9GoHn4qRr0jKxcBMmY_LFzUFVXhvFa6wKYYiCSM3Dh8ON5vz04N3ERxcD4UtfM2bx-iTIG2PR2zNz5Scm36l8nR06qn7_gX8ydYJK6jd8r9dzx1csF0C0b9d32AooBYO5p74ERHX4MLVxFCFKU477sCUFPJv5UWk-ffcYZIBFzvF75qf4HUrj9SVSR9IQXdEy5qYAPcAwFvxAVKUFcEHYLvVtiLS3CPyKLrhBpyMNfIM8ikBkW3NYLKSdDu41v7IfcYeBmnJsAwr2br0_TjKRQFsEY3l_q3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انباء اولية عن استهداف العدو السعودي لسجن الجوف وسقوط عدة وفيات من السجناء  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/89559" target="_blank">📅 17:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89558">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انباء اولية عن استهداف العدو السعودي لسجن الجوف وسقوط عدة وفيات من السجناء
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/89558" target="_blank">📅 17:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89557">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇸🇦
🇾🇪
قصف مدفعي سعودي يستهدف منطقة آل الشيخ في مديرية منبه اليمنية الحدودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/89557" target="_blank">📅 17:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89556">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇰🇵
‏
وزير دفاع كوريا الشمالية:
إذا سعت الولايات المتحدة وحلفاؤها إلى مواجهة عسكرية جديدة، فسنتخذ إجراءات مضادة قوية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89556" target="_blank">📅 17:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89555">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇷🇺
وزارة الخارجية الروسية تغلق القنصلية الألمانية في سانت بطرسبرغ.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/89555" target="_blank">📅 17:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89553">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b352d15928.mp4?token=svZg_i4RokcpcHbUCmR8ESyTFkibX-lgog9XRwyYXgCc9w9ROtZobjZBOKc1QOydPRICCGXErBoLzKjr40eRMcRcWW0WBYdEHbFABb1T3NtQsIaO4gNNW6FKlrZTcQwak_QjuL5DBkMcpHKOnWIHr94U2jrzeXVgUcdxMJRuFajXIWKYm8JKus6d1rQSr0XZbFbRBtMsX_gbLDEMlQ-yAjwXD2seQnSkZNfNk0UKaFh5kSekWz8zfBW9lwpQ62FJsoe3R4lQky44oj28mlipVipd-xw59MYz8fYzCyZpbQHGrH7EmQEUJz-RGKpCmU39uyjQ1DHv7LfWaGXfNVeafw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b352d15928.mp4?token=svZg_i4RokcpcHbUCmR8ESyTFkibX-lgog9XRwyYXgCc9w9ROtZobjZBOKc1QOydPRICCGXErBoLzKjr40eRMcRcWW0WBYdEHbFABb1T3NtQsIaO4gNNW6FKlrZTcQwak_QjuL5DBkMcpHKOnWIHr94U2jrzeXVgUcdxMJRuFajXIWKYm8JKus6d1rQSr0XZbFbRBtMsX_gbLDEMlQ-yAjwXD2seQnSkZNfNk0UKaFh5kSekWz8zfBW9lwpQ62FJsoe3R4lQky44oj28mlipVipd-xw59MYz8fYzCyZpbQHGrH7EmQEUJz-RGKpCmU39uyjQ1DHv7LfWaGXfNVeafw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتداء يطال النساء أمام وزارة المالية العراقية</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89553" target="_blank">📅 17:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89552">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇾🇪
🇾🇪
مشاهد من استهداف القوات المسلحة اليمنية لشاحنات محملة بالعتاد العسكري قادمة من الأراضي السعودية
في معسكر
الوديعة بصواريخ باليستية مناسبة محلية الصنع.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/89552" target="_blank">📅 17:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89551">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇸🇦
العدو السعودي يستهدف بغارة محيط مدرسة عثمان بالروض الربيعي في مديرية التعزية اليمنية أثناء تشييع بالمنطقة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/89551" target="_blank">📅 16:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89550">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇶
بلومبرغ:
العراق يواجه صعوبات في بيع النفط من البصرة بعد رفع أسعاره.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/89550" target="_blank">📅 16:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89549">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPiZdQ5wVzeRStT18N5P9DF-HzBf9meQ6bVkdRyfkcczWwR9UOSKlopqR9NDmvJW6Q-RYTxO6K7naNYH0Mb-a3Hob4LtoM9pXy6dnmPw347pPI9wdhEqoHplT0Fs245W52iwboWrkltfw4SMuleQ5xWf0NQ0R88_Z_-ZqlYh1sNH-jOH8idY9y2Y4VCf0XlJR6WslC2cCB0XBUstpK4ghAs6bKw--NL-3ygyzvxbw-nvJx2NFUhrwQWCDEjHL-D4ST5UyTtCPJpIUH8j6x_dtuCLwyF9yNSzMQIyXWqik1iK1M5s5AyJb4vTcOLWOvCs9XLfjAlbVjKS-4sgo5L1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتال مرتزقة السعودية في الوازعية بتعز</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/89549" target="_blank">📅 16:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89548">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgGDoTS6CErLdmmv8MZnJf5W9ke3qrTC427rvivp66txNjQP1W_w6uMZjfQO4kGMwGHvdjdrju3ea29kZCxXEPF-Z7-DeoJP4wCVSEgp4VeBBSIx4Yuj40LjW5-oixCK67qIClR_op5daxCGaKj4doqHNjCXjloXb5ujO-WE2E1UhsCVkcTIAV1qSvf4VQ_seKgpkcoBXjP4YmSVSQF5tAbGdDzYjgJj65isw7D-w1vURykgovnhUxLmUQXFcsot7bC7Jqi_tk3g2q3-D5gdvA0cmyvGBSqUVMeC2uCrBu58U0IixHrVHrsGiINf9yNvBEHz_eQDQx-RTos3rNc1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابادة رتل لمرتزقة السعودية في الوازعية بتعز على يد بواسل انصار الله.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/89548" target="_blank">📅 16:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89547">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/89547" target="_blank">📅 16:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89546">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89546" target="_blank">📅 16:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89545">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇶
وزارة الخارجية العراقية تثمن الإجراءات التي اتخذتها السلطات الإيرانية لتوفير الحماية للطلبة العراقيين في محافظة سمنان.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/89545" target="_blank">📅 16:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89544">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
‏
بلومبيرغ:
أميركا تعتزم تحويل الملف النووي الإيراني لمجلس الأمن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/89544" target="_blank">📅 16:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89543">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مصدر عسكري يمني ينفي لنايا سقوط معسكر اللبنات في محافظة الجوف بيد قوات مرتزقة السعودية المدعومين أمريكيا ...</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89543" target="_blank">📅 15:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89542">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مصدر عسكري يمني ينفي لنايا سقوط معسكر اللبنات في محافظة الجوف بيد قوات مرتزقة السعودية المدعومين أمريكيا ...</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89542" target="_blank">📅 15:56 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
