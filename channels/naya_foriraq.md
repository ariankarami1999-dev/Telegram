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
<img src="https://cdn4.telesco.pe/file/VuNRm182_SE3FqdtRzN6ovJEHenxsEzhBvG6ryBiL9b1V5RvPTAxBdkY3IbJ9rfJduOsGUCHaizIbYZwEZIk7wU3w9_K8p9dZ6ihW6CyLP_Eet5PkSjQdeAG3mOzudE3kL2rgLhGbsASd0TawVloRrAT5VS_EezVKOi4M2GOI6ZzgNkzD15RqQMPsPqMbGIPOqgFxXmgASO00A_4akgNZc5Kh2bC1edMhbnUmzo7XioQRnmRXpg1qunsaaVbbeSN1FRa4AgJM2o6bL2aPPJRXu5Vdr2ug9XYe53NLUDeOW6uEuU5-XrUsNRYtZ8O37LK2e-0pkmALC1PGA7nlJmmQw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 03:10:30</div>
<hr>

<div class="tg-post" id="msg-93482">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏أعلنت الخطوط الجوية القطرية تعليق رحلاتها من وإلى مطاري الرياض والدمام في السعودية</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/naya_foriraq/93482" target="_blank">📅 02:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93481">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انباء عن اصوات طائرات مسيرة تحلق في اربيل شمال العراق</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/naya_foriraq/93481" target="_blank">📅 01:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93480">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏ترامب عن إيران: ليس لديهم أسطول بحري؛ وليس لديهم سلاح جو. التضخم مرتفع للغاية.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/93480" target="_blank">📅 00:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93479">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">كوريا الشمالية: الأعلان عن تجربة إطلاق صاروخ باليستي تكتيكي</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/93479" target="_blank">📅 00:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93478">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9bdc6dbff.mp4?token=fVFZ2r17KVkpgFdM-Y_uupRao5Y14V7nC-6wn1PqI7CT0jBLXiidcvZdR5gQEJDFf9zSV-LKXN-5FlLy72wp-h8e50rJHQfo5EwZj9FvlJYznYfdhiVgvHXb7569jMo6t7t1D8YX7hGp-McatgkGv2Eiibwjn2HRY_uXFDFX9Q-PYHqK4x--LnydFl_CnI854HJ__udEOkIKTyto6VFhG0el_0_B0kMb4xPLaGTVvdpbrslvyrKi1sypC1HECU7xHuoZ07e_WfHbiT9P1BTrvtFw-fg32dIfJOoxygFzKizsz-jf3l6vQ6exfEV0NVcZ9jtzGiXo10ADq1BFYOL6bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9bdc6dbff.mp4?token=fVFZ2r17KVkpgFdM-Y_uupRao5Y14V7nC-6wn1PqI7CT0jBLXiidcvZdR5gQEJDFf9zSV-LKXN-5FlLy72wp-h8e50rJHQfo5EwZj9FvlJYznYfdhiVgvHXb7569jMo6t7t1D8YX7hGp-McatgkGv2Eiibwjn2HRY_uXFDFX9Q-PYHqK4x--LnydFl_CnI854HJ__udEOkIKTyto6VFhG0el_0_B0kMb4xPLaGTVvdpbrslvyrKi1sypC1HECU7xHuoZ07e_WfHbiT9P1BTrvtFw-fg32dIfJOoxygFzKizsz-jf3l6vQ6exfEV0NVcZ9jtzGiXo10ADq1BFYOL6bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: الحوثيون يتصرفون بشكل سيء للغاية</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/93478" target="_blank">📅 00:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93477">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEmzvzquqdkJBjxNQy_gNjkCUWmmMs3vmEPLZhiwefYVG0Ll735QcUlqjLm1cT9GJYN8UxDzD9o5IWUh3qtyMCBPtTcNBLabsu2QuD7H-dmwIzfS8Np_Q3GAGRuA6T7IowPyxzZ3u7e3DpgyYZHysztLZfDDFCBwxC31fjskXCuimG78X5px16p44th5wqRye92rryRLPYIjWizANj0Cv38p5_5y7T6mSyD8b65S3URFvgNs4QiPQVPs4_SGNWtZvwbdTK4xc7NqCjbAP4f5wILgD_i7_8GP9y09AUZRbUufByweAdwD0k7CJvUTmM7F-LJ5EGsQeaABVhOWuu0TKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏طالبة محجبة وصديقاتها في أذربيجان حُرمت من حقها في التعليم بسبب ارتدائها الحجاب بعد ان اصدر الرئيس الاذربيجاني إلهام علييف الموالي للصهاينة قرارا بمنع الحجاب في التعليم بسبب ما اسماه بـ"الحجاب ثقافة عربية وفارسية".</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/93477" target="_blank">📅 00:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93476">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجارات تهز خميس مشيط</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/93476" target="_blank">📅 00:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93475">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارات تهز أطراف الرياض الان</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/93475" target="_blank">📅 00:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93474">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سماع دوي انفجار في الدمام</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93474" target="_blank">📅 00:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93473">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سماع دوي انفجار في الدمام</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93473" target="_blank">📅 00:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93472">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇾🇪
انباء عن عدوان يستهدف العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/93472" target="_blank">📅 23:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93471">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mS_GwLCa0CB7J9iR8JdGwIztWDxT29fD92eSvYaY9A2JJHe_NIANG7a6sHnmGY3_frVkMyxioYW2rsUjaiCLF2tFMYnc_pvbCW6_ajjRf3OVr267Y2PNZlu0DnhUH3eUFrhZaV6utkylf0I6JY5qzNGx-4Va_-9OPckQZZtGtJeWJxKTReOujAosPW6EC2VUKJSEO1wzUGIEeGMjLh5bDCnVgcJfqcIE2ccwZ55ZAiWehocNFQm5hZD2j57WJ6pmrRFMRQrF4Nha7KJhse9-QkNmEj8Crlbuhg-rG4d3KxINBGLErCEIAd3r71Em0Tt9FDutCNAhta7c3IFQ2h0Qhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🇸🇦
🇾🇪
جروك يرد على موظفي مركز اعتدال السعودي
🔻
حتى الذكاء الصناعي لدى إيلون ماسك بدأ يعاني من إفهام الذباب الإلكتروني السعودي</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/93471" target="_blank">📅 23:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93470">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجارات تهز خميس مشيط</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/93470" target="_blank">📅 23:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93469">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نايا - NAYA
pinned «
🔻
لمتابعة المشاهد الحصرية التي تحصل عليها نايا من داخل السعودية يُرجى متابعة حسابنا على منصة «إكس». اضغط هنا
🔻
To follow the exclusive footage NAYA obtains from inside Saudi Arabia, please follow our account on X. Click here
🔻
برای دنبال کردن تصاویر اختصاصی…
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/93469" target="_blank">📅 23:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93468">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOOr9ahKLE6bcfau55_d-b_lBPJ9ZqPcZ1e_JswN8eLq_dJ0MYw78AmIUwQc8_xhlKeS1Z6ec5mfA_n5BbueXDoOyB0JWEnjoJZ0ih5n6WAB90409qQVvt-c_6uEZtKdM_aVpenUzlSnkizLKcuOXfS6Xw031fqQU_VAi39qGJG1mEHdmLkz0HcjusiOFzeWbAdOOEOgZgZ-5zHY-WN16CixyFtesnZpLo-W129b_cNxo0o87RRrkaGXmBYMhUDAj6HHqS5jfnvNQUVqgftwWEVWssQoNvdIqZc1_N1XorKBSXX50ZDnIVEH859LQo9SxWA27agahR8i9O3BUhytrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
السعودية مجددا تتوسل بالمواطنين للإبلاغ عن وصول المسيرات والصواريخ
😭
.
رابط التغريدة
ليلة هادئة جدا في الرياض
😆
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93468" target="_blank">📅 23:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93467">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔻
لمتابعة المشاهد الحصرية التي تحصل عليها نايا من داخل السعودية يُرجى متابعة حسابنا على منصة «إكس».
اضغط هنا
🔻
To follow the exclusive footage NAYA obtains from inside Saudi Arabia, please follow our account on X.
Click here
🔻
برای دنبال کردن تصاویر اختصاصی که نایا از داخل عربستان سعودی دریافت می‌کند، لطفاً حساب ما را در پلتفرم ایکس دنبال کنید.
اینجا کلیک کنید</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93467" target="_blank">📅 23:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93465">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZvrlk5hwxvfD4OBghhpgL6-Plq1ttZNHyacbYpQiH60175tMczO_I7D4LelmuPdsEBDSrJzKj1H9DmNHJQ5XGCTexHidkbjiq92zk1H1hFkZQlIwmCC-J7mBxPeVD8TjCUWH1HSIz2YWdwJqS-3GM5LnTPWlIKT624l6-GIthWVVnUBf1sUj1CRplB9uLtIZ3puKF5cX6-zHRcY9oQr0WfUiXNa8UBsekpl_gVq_-Rk9YRO00sP9JX2D4_oIveChZNlw32jxhwG8jGcWWlKvtT-swjjyEkELwtdzBUiG2hdOF9FQNK9wswuIHlFuZnTvnfw2sUoqDizP6UBmkRbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرياض فارغة بانتظار صواريخ انصار الله
رابط التغريدة</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/93465" target="_blank">📅 23:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad0902f6a.mp4?token=M91QXFuWX5qPlz2XGTmHSoSXw7KfUgiZxz9KZIMU7DrvfZE-qWbMlAE0A5mO_eHvvJMIGkd96xR_8i6bEHVBCOaJzj3SGvKYG817uwg14tKYwcnaRQRx3ZU1sjC_qos2qnggNZ3kxL5w6IcULEI_QXd8VoOqOezl8BKuCrNLMwRC9aiegjSJNicL8a8KufAmOHujE0xxDCspgP8CsIrR2GtC863w4zUvxvZeniGaPcj8Pvdfp4eaC8xygRnEMeikNc_a1LOUy_rkQlXr1xQ7y_KVK5QPTlyXO9XZ2aIwgqtLO3IiVKHDl7I8AJOzThUnE3xDUMQXKW9J8eSA8JqGvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad0902f6a.mp4?token=M91QXFuWX5qPlz2XGTmHSoSXw7KfUgiZxz9KZIMU7DrvfZE-qWbMlAE0A5mO_eHvvJMIGkd96xR_8i6bEHVBCOaJzj3SGvKYG817uwg14tKYwcnaRQRx3ZU1sjC_qos2qnggNZ3kxL5w6IcULEI_QXd8VoOqOezl8BKuCrNLMwRC9aiegjSJNicL8a8KufAmOHujE0xxDCspgP8CsIrR2GtC863w4zUvxvZeniGaPcj8Pvdfp4eaC8xygRnEMeikNc_a1LOUy_rkQlXr1xQ7y_KVK5QPTlyXO9XZ2aIwgqtLO3IiVKHDl7I8AJOzThUnE3xDUMQXKW9J8eSA8JqGvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇸🇦
مشاهد غير محدودة لنايا
😎
من الهجمات التي طالت الرياض قبل قليل.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93464" target="_blank">📅 23:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f2d20cb2.mp4?token=O-jyuGDrqPdbSqSy2FYznKeppzwxCeWgLxBnRBOVo52CtJ_XJc929Du-xzpydWRUP2DG5QShmRBuuuybkNVtIJD82LWpzJuUZEw-2M4CXXtdjRiLXqQAN4wyFXI_PsKcFSeLR7QYNXao2rhv7ezdzDnbTxQA8Ylks4N8e2QqUmo6PuLR-nLHTdQ27fUwpYQPtKlrORw3MYOv_MLZTD-d5HTl-XvKrNnxf-dRMy4IZIwPmkUD-8t0LtgCkYofsvdoRzH6oFQB07KVRKfatUnmmSmMeHM-FXQHbR08AVPd2hh4yvU219A7sT9TURRsAQQY5g08AkMIGtCcxZnzAENVrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f2d20cb2.mp4?token=O-jyuGDrqPdbSqSy2FYznKeppzwxCeWgLxBnRBOVo52CtJ_XJc929Du-xzpydWRUP2DG5QShmRBuuuybkNVtIJD82LWpzJuUZEw-2M4CXXtdjRiLXqQAN4wyFXI_PsKcFSeLR7QYNXao2rhv7ezdzDnbTxQA8Ylks4N8e2QqUmo6PuLR-nLHTdQ27fUwpYQPtKlrORw3MYOv_MLZTD-d5HTl-XvKrNnxf-dRMy4IZIwPmkUD-8t0LtgCkYofsvdoRzH6oFQB07KVRKfatUnmmSmMeHM-FXQHbR08AVPd2hh4yvU219A7sT9TURRsAQQY5g08AkMIGtCcxZnzAENVrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد حديثة قبل قليل لانطلاق الدفاعات الجوية من وسط الرياض.  الشكر لمراسلينا
😎
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/93463" target="_blank">📅 22:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇷🇺
بالتزامن مع الهجوم على الرياض
موسكو تهاجم كييف الان بالصواريخ البالستية .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/93462" target="_blank">📅 22:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نايا - NAYA
pinned «
فجر ساخن جدا   https://t.me/naya_foriraq
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/93461" target="_blank">📅 22:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
الاعلام الاوروبي:
تبحث المملكة العربية السعودية عن أسباب فشل أنظمة الدفاع الجوي في إيقاف هجمات الطائرات المسيرة والصواريخ التي شنها الحوثيون على مطار الرياض، والتي أسفرت عن مقتل ما لا يقل عن 13 شخصًا وإصابة أكثر من 300 آخرين.
أظهرت التحقيقات الأولية أن الحوثيين استخدموا الطائرات المسيرة لتسهيل مهمة صواريخ كروز والصواريخ الباليستية.
تسعى الرياض إلى زيادة مشاركة الولايات المتحدة العسكرية ضد الحوثيين، بينما يدرس الرئيس ترامب إمكانية شن ضربات.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93460" target="_blank">📅 22:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇸🇦
🇾🇪
لاول مرة منذ اندلاع المواجهة مع الشعب اليمني
وزارة الدفاع السعودية تنشر تنويه بسبعة لغات تضمنت " الهندية ؛ الفلبينية ؛ الاوردو ، البنجابي ، البنغلاديش ، الإنكليزية " تدعو بها المقيمين عدم نشر الفديوهات اثناء القصف التي تظهر فشل منظومات الدفاع الجوي الحديثة لدى السعودية و فشلها بالتصدي لهجمات القوات المسلحة اليمنية .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93459" target="_blank">📅 22:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93458">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇬🇧
🇺🇸
‏
وزيرا خارجية أميركا وبريطانيا:
يجب محاسبة إيران على أفعالها.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/93458" target="_blank">📅 22:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93457">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
يسعى نتنياهو إلى وساطة أمريكية لإقناع المملكة العربية السعودية بالسماح بمشاركة عسكرية إسرائيلية ضد الحوثيين في اليمن، على أمل تعزيز العلاقات وتهيئة الطريق نحو تطبيع العلاقات.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93457" target="_blank">📅 22:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93456">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
بفضل الله وعونه تمكنت قواتنا المسلحة من استهداف مطار خالد الدولي في عاصمة العدو السعودي الرياض مساء اليوم بصاروخ باليستي وكانت الإصابة دقيقة.
نجدد تحذيرنا لكافة شركات الطيران العالمية وجميعِ الخبراء والموظفين والعاملين والمسافرينَ من كلِّ دولِ العالمِ من مغبةِ تسييرِ الرحلاتِ باتجاهِ المطاراتِ السعوديةِ فإنها غيرُ آمنةٍ باستثناءِ مطاراتِ وأجواءِ المناطقِ المقدسةِ في مكةَ المكرمةِ والمدينةِ المنورةِ.
وفي سياق متصل نفذت القوات المسلحة عملية استهداف لقاعدة خميس مشيط الجوية بطائرة مسيرة وكانت الإصابة مباشرة بفضل الله.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93456" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93455">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔻
If you want to see our Video inside KSA join us in “ twitter “
🔻
https://x.com/nayaixa3/status/2109720131270275359?s=46</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/93455" target="_blank">📅 22:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93454">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80ec7f71a.mp4?token=wBLOSdGTkxEto3oCK-IBSuI8HdzgxlccJCot2jdwPk8kZJdPo8F0HLvnWjepEHujENPF5OhMXELQhA4TC-Z32MVr0JwKQtJBCPHVqz9FA9f0g8BtZmAWx4ze-iqowJGGIAiHvB1LHzltXrViEN_LhnhYTsrRMam4k_zNnDwiAetvuVlPOJc-QrjBCr7PfDnJjPNCfIGFiWgToBXmo41dXGgT0InK50MG_UvEkyUnuEZ2MyGsHMiUw6D3ek_kyWYUyfOQYrz4wS2_SQOoruYdxzDVSUTaGNckH6V0wUlDKmaMylzuWiLl44uvc3H24RDloM77XnnPktJYtx7eQjWVzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80ec7f71a.mp4?token=wBLOSdGTkxEto3oCK-IBSuI8HdzgxlccJCot2jdwPk8kZJdPo8F0HLvnWjepEHujENPF5OhMXELQhA4TC-Z32MVr0JwKQtJBCPHVqz9FA9f0g8BtZmAWx4ze-iqowJGGIAiHvB1LHzltXrViEN_LhnhYTsrRMam4k_zNnDwiAetvuVlPOJc-QrjBCr7PfDnJjPNCfIGFiWgToBXmo41dXGgT0InK50MG_UvEkyUnuEZ2MyGsHMiUw6D3ek_kyWYUyfOQYrz4wS2_SQOoruYdxzDVSUTaGNckH6V0wUlDKmaMylzuWiLl44uvc3H24RDloM77XnnPktJYtx7eQjWVzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السعودية تفقد السيطرة على الهنود
😆
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/93454" target="_blank">📅 22:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93451">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06004d882c.mp4?token=MWH_qVlExeQEVcPMPIbfxNLVOUXrPBaluE40QYhpUA6pVbAVJP9QBFLrVeyQoYGcSE7JjvoSu8XXI5UJAva2frwqMlEqsBLEAVRLOVB3l_-1QqeEYcyD8ZGkV07VJ1sIT09N7b-vWaM8zqt9AdD95jS2icdrqvOBHr9E0gWexaq15sYKMDJV1qFSj68wvWdELhDM5FarW-OUa_J5TSIkSS8KmtSSul-FFVWVGg4F9RE8JW97jZmrldDaU07d9jxJM44mUszdCnzqxtKaqUYfj-jRs2Gvw-xoWjb73XaSR06o2HLdaHeIi85Jccg5ZIT7rm1YJB55CIjyfKcDv6_uLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06004d882c.mp4?token=MWH_qVlExeQEVcPMPIbfxNLVOUXrPBaluE40QYhpUA6pVbAVJP9QBFLrVeyQoYGcSE7JjvoSu8XXI5UJAva2frwqMlEqsBLEAVRLOVB3l_-1QqeEYcyD8ZGkV07VJ1sIT09N7b-vWaM8zqt9AdD95jS2icdrqvOBHr9E0gWexaq15sYKMDJV1qFSj68wvWdELhDM5FarW-OUa_J5TSIkSS8KmtSSul-FFVWVGg4F9RE8JW97jZmrldDaU07d9jxJM44mUszdCnzqxtKaqUYfj-jRs2Gvw-xoWjb73XaSR06o2HLdaHeIi85Jccg5ZIT7rm1YJB55CIjyfKcDv6_uLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد جديدة غير متداولة من استهدافات التي طالت الرياض ظهر اليوم.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/93451" target="_blank">📅 22:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93450">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">استهداف سفينة اخرى في مضيق هرمز  الله اكبر  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/93450" target="_blank">📅 22:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93449">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الله اكبر
▫️
استهداف سفينة ثانية في مضيق هرمز واندلاع حريق كبير فيها.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93449" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93448">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇾🇪
جولة ميدانية من مركز مديرية المسراخ لمراسل الإعلام الحربي - 12 أكتوبر 2026م
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/93448" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93447">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b0c970cd.mp4?token=T6SyQZ7_b9xHj4UOtj10_VRMWZ4FnqLkiZ-wXXfxMitXRISDou0PUu5Wx5-9zsSiT5YRsIjHrJp83OKsVjx4uel1EwgdCuQF0Ak1MLapznJIanY_mqTne_fIg5kyX2-gpHo7SOcgQdxNv0FeyHvAXf_MgxUGB4GK-z9c2DVCZX1GiSoxU50TFtNwEQs2xUSTsvJES9KFHFywwdvxA56bh-7-ZR0wZMlq4SM5S02YITt6m0CiSLSZRKDLT-EGfAS3X0JPKHLP5NBsLhZ0AbN_Z7YX-7pcABdAcOG9_KGzDXlr2HlqJAofeMIOqpNLTf8WN73zpp2fB7P5fZLB-tAGEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b0c970cd.mp4?token=T6SyQZ7_b9xHj4UOtj10_VRMWZ4FnqLkiZ-wXXfxMitXRISDou0PUu5Wx5-9zsSiT5YRsIjHrJp83OKsVjx4uel1EwgdCuQF0Ak1MLapznJIanY_mqTne_fIg5kyX2-gpHo7SOcgQdxNv0FeyHvAXf_MgxUGB4GK-z9c2DVCZX1GiSoxU50TFtNwEQs2xUSTsvJES9KFHFywwdvxA56bh-7-ZR0wZMlq4SM5S02YITt6m0CiSLSZRKDLT-EGfAS3X0JPKHLP5NBsLhZ0AbN_Z7YX-7pcABdAcOG9_KGzDXlr2HlqJAofeMIOqpNLTf8WN73zpp2fB7P5fZLB-tAGEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد اخرى من توثق لحظات اطلاق الدفاعات الجوية السعودية لمحاولة اعتراض الصواريخ اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/93447" target="_blank">📅 22:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93446">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd4c20bdb.mp4?token=LCo-tI_BhsnBR6WNmpcCNpT6PVzeL9ouO22HZqD5DWmE6nHRxyE5A2f8eTzqFRpNvmQolZIwLJHxlqwW2mD8Q4vH0dTSPcWGqoL97FYmpFpjkRMH5U7N63-3ztRBx9dJdx4WbWEUZxg79J-0YsnP0ZB_GbVfZbFe9wxJPGgVnAe6yrBPdNDW0cYYes7YcJtL4Lam1srb5OO7R0CKJfFKvj6WZvW3kFVsJgQzhrxei1jb1dPU3rd5nQKZVUJ03PFm55INEmImFAVJjn00oZP7Ef9KNlUWhVOY8_wnUgWsqpPfdNh9unhYXy23zFIqJ95Z1FlHIKeB8OngCtpXMInKCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd4c20bdb.mp4?token=LCo-tI_BhsnBR6WNmpcCNpT6PVzeL9ouO22HZqD5DWmE6nHRxyE5A2f8eTzqFRpNvmQolZIwLJHxlqwW2mD8Q4vH0dTSPcWGqoL97FYmpFpjkRMH5U7N63-3ztRBx9dJdx4WbWEUZxg79J-0YsnP0ZB_GbVfZbFe9wxJPGgVnAe6yrBPdNDW0cYYes7YcJtL4Lam1srb5OO7R0CKJfFKvj6WZvW3kFVsJgQzhrxei1jb1dPU3rd5nQKZVUJ03PFm55INEmImFAVJjn00oZP7Ef9KNlUWhVOY8_wnUgWsqpPfdNh9unhYXy23zFIqJ95Z1FlHIKeB8OngCtpXMInKCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تم اعتراض جميع الصواريخ:  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/93446" target="_blank">📅 22:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93445">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d642d2db.mp4?token=qqhLTUaFNR9twO_BOfSc0aCbwb-8bpYkow-wA4f_7bU4h2BmNuPIyxKnDodb1VDv1-SqVWvocTz0zXrQtpkE6_430L2mSkzwG-7f9U9DrasjBwhtk2GRpNFfV_CH09y0CsGa4dlxdkMYjywn__mE8DlnTCy0WGkkUv0j_YH2Wv25_-F9D3ZtBLtFpKLIyLr9vBkOK71Bv-KIR_LAJbJMEeQnP1M0h-i9CjJqYWEBw8FdBPQZXpRsvWD5nUq4j_kR8KA1_vCQa0ao_X3knxyFW2SJ3LDm5fKprMRnRPN6fcOGP-9r2mQ2ShmFTxW5RgGhPNg__dGNz0eBaGGKY4e8aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d642d2db.mp4?token=qqhLTUaFNR9twO_BOfSc0aCbwb-8bpYkow-wA4f_7bU4h2BmNuPIyxKnDodb1VDv1-SqVWvocTz0zXrQtpkE6_430L2mSkzwG-7f9U9DrasjBwhtk2GRpNFfV_CH09y0CsGa4dlxdkMYjywn__mE8DlnTCy0WGkkUv0j_YH2Wv25_-F9D3ZtBLtFpKLIyLr9vBkOK71Bv-KIR_LAJbJMEeQnP1M0h-i9CjJqYWEBw8FdBPQZXpRsvWD5nUq4j_kR8KA1_vCQa0ao_X3knxyFW2SJ3LDm5fKprMRnRPN6fcOGP-9r2mQ2ShmFTxW5RgGhPNg__dGNz0eBaGGKY4e8aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد حصرية لنايا توثق سماء العاصمة السعودية الرياض قبل قليل.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/93445" target="_blank">📅 22:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93444">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee472b449.mp4?token=g5snT434LLDVLvE_21mecT5CZmtQQ1ZTa6ip64CcAKXDbfX9EY4e0cabVYtSQn8hasxWk0k9k2SQgBzNk-2Krnnlv-SszqUXuEyjCCHs6DlD1VrGt5fuCXWC81tCkhw8zWBDHh_h3gPWx0X3dcXyvAq3L7OkGJYendcEJiVtQ3v7oaAY9Voxv0cvfa1cE7KwkuOc62t_CfquWvJD4d3-F1KDLZ10XZTeRzcsjGhWOKIVMaGkgB8-2rXgBjv-mopZ42Yuezs2apCJtCXxIQkPNoQHmTk3W2gb1SkBqk-K9RnfKJJREH4pLAScc9hzJq7SggcDosJASCUe-OQ3tvYqhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee472b449.mp4?token=g5snT434LLDVLvE_21mecT5CZmtQQ1ZTa6ip64CcAKXDbfX9EY4e0cabVYtSQn8hasxWk0k9k2SQgBzNk-2Krnnlv-SszqUXuEyjCCHs6DlD1VrGt5fuCXWC81tCkhw8zWBDHh_h3gPWx0X3dcXyvAq3L7OkGJYendcEJiVtQ3v7oaAY9Voxv0cvfa1cE7KwkuOc62t_CfquWvJD4d3-F1KDLZ10XZTeRzcsjGhWOKIVMaGkgB8-2rXgBjv-mopZ42Yuezs2apCJtCXxIQkPNoQHmTk3W2gb1SkBqk-K9RnfKJJREH4pLAScc9hzJq7SggcDosJASCUe-OQ3tvYqhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
الصواريخ تصول في سماء الرياض متجه نحو هدفها  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/93444" target="_blank">📅 22:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93443">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230d30c017.mp4?token=u_bSRLvGpOsoyHyBxFEvKKq3m4rpZWjRuAtsg52ndvtovLU5qhfayoa8obgFOOefoE_oAi2Y_va0B7kZK3xIHmIT-HzUoSqMEuP91zT7ZWP_2EQ46F1Lo5-WzTBeDExEcTVDy3nxDgIFLQt5L8lquK0aoudvSmi_7kjRNFqgvM2VohCFgm7jJP_bqXWL11CRG08UkAS0sl-6D64h9mB08dGYWpe5bNAmxNO9wuRxQ662LhYiZ7_nwChtELkwZhGAWKiT6jkcoeiEQL9KDR-dMvmBElgIQRmMuolYbXvNL9GmdYjQZVFDRARq_kLOksDrKBJmI1uSG7iWXvVNdaPu5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230d30c017.mp4?token=u_bSRLvGpOsoyHyBxFEvKKq3m4rpZWjRuAtsg52ndvtovLU5qhfayoa8obgFOOefoE_oAi2Y_va0B7kZK3xIHmIT-HzUoSqMEuP91zT7ZWP_2EQ46F1Lo5-WzTBeDExEcTVDy3nxDgIFLQt5L8lquK0aoudvSmi_7kjRNFqgvM2VohCFgm7jJP_bqXWL11CRG08UkAS0sl-6D64h9mB08dGYWpe5bNAmxNO9wuRxQ662LhYiZ7_nwChtELkwZhGAWKiT6jkcoeiEQL9KDR-dMvmBElgIQRmMuolYbXvNL9GmdYjQZVFDRARq_kLOksDrKBJmI1uSG7iWXvVNdaPu5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد حصرية لنايا توثق انطلاق الدفاعات الجوية السعودية قبل قليل في محاولة منها لاعتراض الصواريخ اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/93443" target="_blank">📅 22:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93442">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/93442" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/93442" target="_blank">📅 22:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93441">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfbac31622.mp4?token=p9wOU4V8reOD0HHKouP_4whLz7YhCS4OIOyta8CxjKG0EV4MXIlScos6cjyN7-PugQynqTVxb1K42SulJqmX4mCS1RuyIMj4vtNcxW1wHPSLElMS4idhFTFIJn3I4Xh0cXsLH7K6VtUSfDCQ1QcSumfUCJWC6c5bo-7aZRWKMsAmRAt_GFUQR32dOsIkGDQF85NliCgLCcW-72ZyeQDjlq0ins6gFK65yPjOuRl_j9chsh8K-toF5fNipwaVaimSVFFBoOolrx-C_CJ-ZahffQdxj_m_F-ToN1477llCt6mlaM4ak5mT6yQ6iba6DInl6UV9BEwPCd3QOXMy9sMavQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfbac31622.mp4?token=p9wOU4V8reOD0HHKouP_4whLz7YhCS4OIOyta8CxjKG0EV4MXIlScos6cjyN7-PugQynqTVxb1K42SulJqmX4mCS1RuyIMj4vtNcxW1wHPSLElMS4idhFTFIJn3I4Xh0cXsLH7K6VtUSfDCQ1QcSumfUCJWC6c5bo-7aZRWKMsAmRAt_GFUQR32dOsIkGDQF85NliCgLCcW-72ZyeQDjlq0ins6gFK65yPjOuRl_j9chsh8K-toF5fNipwaVaimSVFFBoOolrx-C_CJ-ZahffQdxj_m_F-ToN1477llCt6mlaM4ak5mT6yQ6iba6DInl6UV9BEwPCd3QOXMy9sMavQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد حديثة من سماء العاصمة السعودية الرياض بالتزامن مع انطلاق الدفاعات الجوية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/93441" target="_blank">📅 22:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93440">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbd8766f2.mp4?token=R5xu1pDCY13auRPb3UYoeDdqLlMqgmATGxlW8rLZ1asT9dbW8HYxLovIvVx0d7kpVyudSdILRJ2wHV5rf-Qpge-yAJVMbfPE5glU5fqc1_JOlI9R9bE621kZsTG6_g0cxVI4cBNUXEvBZg3_zH6oy2_L6Idx2Qb2xZJLEhhMajHZGYsiwC_CNVScPnKEmH4RxXnrFqehTeUQxp6R37r3lMqEUf2D9RnliRjuI7RX4h_JIqLW4QqW7sZ4bktLXlPbt5g_bm8HFR5w80QDhl_aHft_0p8oq2g7F0zjNTxj2TwcxYVB2pqglg__ojeCEahtVOT7gsRw-5RRGmektF8VUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbd8766f2.mp4?token=R5xu1pDCY13auRPb3UYoeDdqLlMqgmATGxlW8rLZ1asT9dbW8HYxLovIvVx0d7kpVyudSdILRJ2wHV5rf-Qpge-yAJVMbfPE5glU5fqc1_JOlI9R9bE621kZsTG6_g0cxVI4cBNUXEvBZg3_zH6oy2_L6Idx2Qb2xZJLEhhMajHZGYsiwC_CNVScPnKEmH4RxXnrFqehTeUQxp6R37r3lMqEUf2D9RnliRjuI7RX4h_JIqLW4QqW7sZ4bktLXlPbt5g_bm8HFR5w80QDhl_aHft_0p8oq2g7F0zjNTxj2TwcxYVB2pqglg__ojeCEahtVOT7gsRw-5RRGmektF8VUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
صاروخ باليستي يمني يطلق نحو الرياض</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/93440" target="_blank">📅 22:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93439">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21384b098a.mp4?token=ssi-zfzRH9CPLX0lVSbgKH_mpV3RL8P-JV-J_KbCQlTJLBPTZY2jT9FyG350S7XE25eTqYW7Z2Zfk1Ju7UpZZq-sJsSrAhz0YfdF-wJQocLkQkcXwUyukwGHIrvTvHRAIyBNjJ8w9I3czXUALdJsOhUwKIuPi2COwerrx5SiBm3HHYT5k-YguKxt75hKPwfl6aCm3XEX0Ew9e_AFQS28-aR6ir76tB-xwD_yeMu7gCIYCmEPfB-IoHJfNSOoRs3ImVh41CCVqQ5r_2TmNmFHgOIo5sgaoS-X8FesyvaodL5B0WD63Sqn6orSZ71qobHMmja1827BwqHH87mnm2IKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21384b098a.mp4?token=ssi-zfzRH9CPLX0lVSbgKH_mpV3RL8P-JV-J_KbCQlTJLBPTZY2jT9FyG350S7XE25eTqYW7Z2Zfk1Ju7UpZZq-sJsSrAhz0YfdF-wJQocLkQkcXwUyukwGHIrvTvHRAIyBNjJ8w9I3czXUALdJsOhUwKIuPi2COwerrx5SiBm3HHYT5k-YguKxt75hKPwfl6aCm3XEX0Ew9e_AFQS28-aR6ir76tB-xwD_yeMu7gCIYCmEPfB-IoHJfNSOoRs3ImVh41CCVqQ5r_2TmNmFHgOIo5sgaoS-X8FesyvaodL5B0WD63Sqn6orSZ71qobHMmja1827BwqHH87mnm2IKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
تأجيل مباراة النصر أمام نيفتشي في الرياض إثر القصف الصاروخي اليمني.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/93439" target="_blank">📅 21:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93437">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد من التدمير الذي لحق بالمباني المدنية في العاصمة رياض اثر سقوط صواريخ الدفاع الجوي التابع للسعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/93437" target="_blank">📅 21:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93436">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEhA1PFamsWhlFpvRfaPJT0XHTp3N64cn7-pBMEl57drOgU0ctispYiLfa_HpZO3Ac51AzjEPbBgDV5kK7I-yJZRtQhAe6WctAELr-heJce9fwG_sjZN7yBWRkDu25fUghO4NGo70-C-9cL8hlz9eGRr0pB_BC_tH6i9fUtkdffeiNQ4N6_G3lMGIm6QXe-xixS3K1Rs2nL01yro2n8fzyvZlO-qL6Ysu3hlBpwsafT0kkmE0Nb1dYiuGaTVnSRYsMFCr2n2aCKIAC2VoSaXSbknjso-IK0a1lhPDujWm-dZE92kPtLU0d9K44pItrgpjel8fPG_QsR81LeLLJD5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
انفجار سفينة في مضيق هرمز اثر تعرضها لصاروخ مجهول.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/93436" target="_blank">📅 21:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93435">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2S140rf7Zq4FUpNII5RXb8kEUvSB7P52EkFhIEAPXGk77CmTIPYAKAEk4Z5xyDi7E_9VIIhrklcNExaBmW7Rin6oP0bNJnfn6ZCX1q5I3HV0m0cmmici_ybF32F_lHiTsCQQQmfmidnW9CBU_WiLojFZYDCEvCB4Tz6eGC60SxKkNwW7S8XXXZslN-2kPPLqKWnuzV8x7crjU9e8uJ36SSS5YO7clVCl6129F8SooO6uFWcKBu-qDq_VgiRqbdV6p1uKpnY_6mXTGQPWZJektrjkAyJZKyeGP9eZeWQ8TgT9qIMmkzcADzUwGSbHawPjzMJwoz6RgJ5lqQPp3qhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
انفجار سفينة في مضيق هرمز اثر تعرضها لصاروخ مجهول.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/93435" target="_blank">📅 21:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93434">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASfxHSXgPBvqpNWJ2NwNAT3sMRKtkEpEUcxUouCF5fhEMN57AR56StinjKabHt6xapCrCCXmtl7ZOu_nzZFFvxiwVAzU_E_VNj7wcEJ2Px9-A2A42fzvxCTM4Fs9EGiTityQQoua50SI4wkKNZzqlulo0Di-qsyMIhIWYvpI4CARRZ7CKurtq2oepw0IWGp7Mw8DN9jNe1sFHeZBZ5iezNLB7_INXK62I_s_MfVjKtZCVFrHCDl0TdJGyTg5haivFTFTIE3rlF2ylUzBMELSKKpQUjjwdPoRXF60QaPtFXeRdu6kD67uDe4bEeOXfGUiURgm0UyNV7f71e5Vh-AB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
قفزة في أسعار النفط لتقترب من 107 دولارات للبرميل الواحد.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/93434" target="_blank">📅 21:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93433">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇸🇦
تفعيل الدفاعات الجوية في العاصمة السعودية رياض.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93433" target="_blank">📅 21:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93432">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8575d2165e.mp4?token=LCMfntOjK6Fn-GZQDhWnHO2dMyRjOg2immH2V6YYadDdG8DXVM9No73Q7Qcd8L5LlYJy9kcMvItvZ-KIqPBHBF93pqyQdhpLkXuVAs8yXXPF7ZnfW5Uf1wkIbCVD6fFrbxtGSIdLAp8srNFSW4dVokn_Nij4yrKN8QQTDntF2kuzF2Ls7sZA9chojpW1ofWIJuxMCZi9YuUjhyZo078pHXrMJBEoKLlsECLRyQsxjbRekgCz3anuR-orxLCTLvLmb8_An6NZBz7pV70EfePcJx2-Jgp9QzFt8eXHms_Kf5NB1aYocLNP4AzgSHatmPbmHEg-ej9cGsmnCLMI3PmJww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8575d2165e.mp4?token=LCMfntOjK6Fn-GZQDhWnHO2dMyRjOg2immH2V6YYadDdG8DXVM9No73Q7Qcd8L5LlYJy9kcMvItvZ-KIqPBHBF93pqyQdhpLkXuVAs8yXXPF7ZnfW5Uf1wkIbCVD6fFrbxtGSIdLAp8srNFSW4dVokn_Nij4yrKN8QQTDntF2kuzF2Ls7sZA9chojpW1ofWIJuxMCZi9YuUjhyZo078pHXrMJBEoKLlsECLRyQsxjbRekgCz3anuR-orxLCTLvLmb8_An6NZBz7pV70EfePcJx2-Jgp9QzFt8eXHms_Kf5NB1aYocLNP4AzgSHatmPbmHEg-ej9cGsmnCLMI3PmJww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد من التدمير الذي لحق بالمباني المدنية في العاصمة رياض اثر سقوط صواريخ الدفاع الجوي التابع للسعودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93432" target="_blank">📅 21:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93431">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇸🇦
تفعيل الدفاعات الجوية في العاصمة السعودية رياض.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/93431" target="_blank">📅 21:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93430">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eiz0mZ52Ap8zi8cYxoAKVBEVZvTQsTZO5ea5-e7dtLNJx0L7ixumz7556cyiIhoj7-lXuTOZr3u0yqlnN43zZgHE8EyOhKOHkSAOge6cGLxIq_zuFyiC-8sjQSlB7mbFo5Kwq0xAoRKXRnyVoR4qGFqjQbOWcBZt0Hz0etag2UwEWZweANgO639DBw92PNOpqmG8qbMMxnd1bjMyNrZOO5-W3TGunckqRthljBIn8l0WaQEI5XozaduBxgPAuydht29dGnnFdqDYCErRgABdvL_OEf8DK6tXr-q643jHXuGZnp_44plI8sgWUmLOhKqNKzuio0zgQUFeBgymkSwAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
يستمر العدو في انتهاكه الصارخ لسيادتنا الجوية، انطلاقا من قواعدهم في الأردن والاراضي المحتلة.
- طائرات (KC-135) عدد
2
.
- طائرة (F35) عدد
1
.
- طائرة (E-11) عدد 1.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93430" target="_blank">📅 21:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93429">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجارات تهز الرياض</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/93429" target="_blank">📅 21:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93428">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مشاهد تطهير وتأمين مديرية جبل حبشي ومثلث البيرين ومفرق يفرس بمحافظة تعز وطرد تحشيدات العدو السعودي منها - 12 أكتوبر 2026م</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93428" target="_blank">📅 21:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93427">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجارات تهز الرياض</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/93427" target="_blank">📅 21:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93425">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a503742f5c.mp4?token=nSA3xqHlZymA8JOBb20fU6Vha0xcCaP3C9N75XOyLp8Uq2cmr6H4eeHu5Eg4S3ag5nv1qSXdsTTHcLKsdGYa-eiYRaiJAJBYRWTj-7KZl0_szbk4_VlojzcGPzNMf4m_cMpXuAajGI54CqpaItTCeVUo_zSGAZF7DN01hKjf15K7zXUenQa4jrqFGDwAi5_Jq1QiVz56vcjYAUg9svg3zCFr24dqeRgmdsyZI3Fgay5jzPqZEtKF-u-uJCA1VVd-6gCWqoaATAyMty_vli9GCznus7aBaelS5p38ffQmperyvNMWuTz7wd8q5HdGRfuXLiDorOGbd5mFiwBMgIsJFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a503742f5c.mp4?token=nSA3xqHlZymA8JOBb20fU6Vha0xcCaP3C9N75XOyLp8Uq2cmr6H4eeHu5Eg4S3ag5nv1qSXdsTTHcLKsdGYa-eiYRaiJAJBYRWTj-7KZl0_szbk4_VlojzcGPzNMf4m_cMpXuAajGI54CqpaItTCeVUo_zSGAZF7DN01hKjf15K7zXUenQa4jrqFGDwAi5_Jq1QiVz56vcjYAUg9svg3zCFr24dqeRgmdsyZI3Fgay5jzPqZEtKF-u-uJCA1VVd-6gCWqoaATAyMty_vli9GCznus7aBaelS5p38ffQmperyvNMWuTz7wd8q5HdGRfuXLiDorOGbd5mFiwBMgIsJFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
مشاهد من الهجمة الصاروخية الأخيرة للقوات المسلحة اليمنية التي استهدفت مدينة أبها في السعودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93425" target="_blank">📅 21:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93424">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇸🇦
تجدد اضطرابات الرحلات الجوية فوق جدة والدمام ومكة المكرمة والمنطقة الشرقية في المملكة العربية السعودية.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93424" target="_blank">📅 21:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93423">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏وزراء أوبك
: أدى الانقطاع الحالي في تدفقات الطاقة إلى وصول تكاليف الشحن والتأمين إلى مستويات غير مسبوقة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/93423" target="_blank">📅 20:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93422">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac48e4e35b.mp4?token=J7TPOehVpcj6JZrC1LQ661Bh4vhhEdBwz8IfDQTLJ7Ne3HeSakyPugsAj1nSdnuHcI_YmE11BtirmBJBoD8eaBc4P5ks_fNG3wH0XlEHEmQ3h4xTWrG7iK_hfKAtm7vuKoCixa6C1ofS7n832f6-1JMmXZUHBsGlXG7v2YZ53Ho-36qM8s5DSd3dOEert16w1Kc6GPLWC8lhYZmQzfRNUlWWGsYDuO33LbP17XaEU3mPqY4hIpfDkbXARWTOs0-1zjd2YKu55415soVW0ykQh82wy_P-iV-VLw5CzN1qqa5-4gdU38ul8Ej9cAgFS9z5waNl6pX7QaQnM2ZBu714wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac48e4e35b.mp4?token=J7TPOehVpcj6JZrC1LQ661Bh4vhhEdBwz8IfDQTLJ7Ne3HeSakyPugsAj1nSdnuHcI_YmE11BtirmBJBoD8eaBc4P5ks_fNG3wH0XlEHEmQ3h4xTWrG7iK_hfKAtm7vuKoCixa6C1ofS7n832f6-1JMmXZUHBsGlXG7v2YZ53Ho-36qM8s5DSd3dOEert16w1Kc6GPLWC8lhYZmQzfRNUlWWGsYDuO33LbP17XaEU3mPqY4hIpfDkbXARWTOs0-1zjd2YKu55415soVW0ykQh82wy_P-iV-VLw5CzN1qqa5-4gdU38ul8Ej9cAgFS9z5waNl6pX7QaQnM2ZBu714wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
‏رئيس إقليم كردستان العراق: أبلغت حكومة إقليم كردستان أحزاب المعارضة للجمهورية الإسلامية الإيرانية أنها لن تسمح بأي هجمات مسلحة ضد إيران.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93422" target="_blank">📅 20:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93421">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
‏رئيس إقليم كردستان العراق:
أبلغت حكومة إقليم كردستان أحزاب المعارضة للجمهورية الإسلامية الإيرانية أنها لن تسمح بأي هجمات مسلحة ضد إيران.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/93421" target="_blank">📅 20:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93420">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
🇸🇦
السفارة الأميركية في الرياض: توقيف أميركيين في السعودية بسبب "التقاط صور لأحداث وقعت مؤخراً" شملت تعرض مطار الرياض لهجمات.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/93420" target="_blank">📅 20:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93419">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
🇸🇦
السفارة الأميركية في الرياض:
توقيف أميركيين في السعودية بسبب "التقاط صور لأحداث وقعت مؤخراً" شملت تعرض مطار الرياض لهجمات.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93419" target="_blank">📅 20:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93418">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 119 غارةً جويةً وصاروخاً استهدف بها الأعيان المدنية في العاصمة صنعاء ومحافظات الجوف وتعز وصعدة ومأرب ولحج والبيضاء وإب من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران وجيزان وخلفت شهداء وجرحى من المدنيين بينهم نساء وأطفال.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا 2177 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93418" target="_blank">📅 20:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93417">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
🇾🇪
عضو المكتب السياسي لـ"أنصار الله"البخيتي:
إذا تورطت أميركا في العدوان على اليمن ردنا سيستهدف مصالحها في المنطقة وأينما طالتها أيدينا.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93417" target="_blank">📅 20:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93416">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇸🇦
🇾🇪
‏
مفتي السعودية:
‏نسأل الله تعالى أن يقطع دابر هؤلاء المجرمين، وأن يحفظ بلادنا وبلاد المسلمين.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/93416" target="_blank">📅 20:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93415">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇬🇧
🇸🇦
‏
رئيس وزراء بريطانيا:
نؤكد إرسال أنظمة دفاع جوي وطائرة "فوياجر" للسعودية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/93415" target="_blank">📅 19:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93414">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQrCvYdTtkBfDwAwAvO_Ehapsf3cgD5tJGo_BcTDAvJRmDU0uWhFzVjThB2r0rtYd1qR2YBlSrp7lrsfpwVUNSmY7kTAadNHYKk0Fnuk-nMeeYmlt7-wzdSmrMcyTvV4hqqg-5zsjIWLyOq5hfqL6-e79ZoYba5cH7wHrBDR7dyTHgI9tz8O5DLcNftEuyC0SecyESvqocVUDXpu27T21lqfD-CUe7crz8FrZn4IGaTCKJtxPD3J8XQbT71c4JKyt2aTV3wpBd-AstM9d5MIrXCU1UkFwyfnLuldAofRRrkid27IND4WFjAjpBXCIsri2VDXxiENz5NjqKdCFWrjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
انفجار سفينة في مضيق هرمز واشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/93414" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93413">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔻
شركات الطيران التابعة لمجموعة لوفتهانزا الألمانية:
إلغاء جميع الرحلات إلى الرياض حتى 16 أكتوبر.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93413" target="_blank">📅 19:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93412">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8565a278e.mp4?token=qF3u05u7-6XzNdNUuXcbkltMruD7tT8_T0-DjjTEFL1ZuqqEMLLNWtMCTNwkITGPPCZQJ6lZiHOnjYcQI5O4FYGWjq-D_UjYQxF8JqCDg6Ku3iqA8ez1zIMm34AaKu18bJjU_K7jBXbEw3MiosGA1oM_Cx8HqBNU2iqA7Ox7UhMF78DcJMsd8q8xeNWjgo5_GKzykKsquL0Oaa-KqNAES-uaAwg8vmZnK9hMMMUCmnNylxaQJ0NiOBA1SZK_mWTnXbQwj5VSDOr3KYfZhwdRrCAoMJyM5Zb4fpHlXGZCYuxCcEG-xq04JeuHV75GJ-LzEVIUPdIJIJolJlod46OtNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8565a278e.mp4?token=qF3u05u7-6XzNdNUuXcbkltMruD7tT8_T0-DjjTEFL1ZuqqEMLLNWtMCTNwkITGPPCZQJ6lZiHOnjYcQI5O4FYGWjq-D_UjYQxF8JqCDg6Ku3iqA8ez1zIMm34AaKu18bJjU_K7jBXbEw3MiosGA1oM_Cx8HqBNU2iqA7Ox7UhMF78DcJMsd8q8xeNWjgo5_GKzykKsquL0Oaa-KqNAES-uaAwg8vmZnK9hMMMUCmnNylxaQJ0NiOBA1SZK_mWTnXbQwj5VSDOr3KYfZhwdRrCAoMJyM5Zb4fpHlXGZCYuxCcEG-xq04JeuHV75GJ-LzEVIUPdIJIJolJlod46OtNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
زيلينسكي
: إذا كان ترامب يريد تغيير القائد في أوكرانيا، فعليه أن يعلم أن شعبنا فقط هو الذي يمكنه تغيير القائد.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/93412" target="_blank">📅 19:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93410">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇬🇧
🇮🇷
بريطانيا تستدعي السفير الايراني على خلفية محاولة الهجوم على قاعدة فيرفورد مؤكدة ان العملية كانت منسقة في إيران وبشكل مباشر من الحرس الثوري.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/93410" target="_blank">📅 18:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93409">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8qC1DUkIfmoZfj3vMp1bOqNky9ImOn75rE3mcl6yDAU0ZyPMo9XI57cFw4mnoki1hcMW5ohyQCp5FYqRh7fccvvunSayMPcRPi4LAXJmG_hUZyXuEmeZvDqANvhrMoxIBtXHMKdyJCCtXTqLJeOIYjXrJMy3moRZrkcZJWWnaF6-TkLgCeP6kIXF-XfNcEjTUOsAfjH4LSepOlE81t5OALwslaKHTLWHXdaid4FW4PVx3A_fKUeC2-37rjcJVPtR0SfQrmOfqylMu1kd7JspL9QmAJUEM_rEmtqEu8rF4WrUfNRjebx8eJwheOtY0d09upXnDmIG1mNVeSXViiKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران جيش العدو يستنفر لنقل اشلاء القتلى والجرحى</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/93409" target="_blank">📅 18:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93408">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4XepYAkIHvsVFbFuWijK_9aUqIN5RFE_Gb5XJ4ENCNtfJsLFpmuS7lrSn-E4RqZ4k7ztkVRrwdubAYnVEcws42dIRWgLB9I7J7YSzhpHO0wKP3UWBT9mjVq3xLvRSSCx9gunil1PtphuJXQIdjeF7JseMXB-lIrbarmieBb8ee_kWaLffyziAPXkV6930SNNymdeOpQrR6C_DumB6bvLajiZYUoXU92eqQBzms6R3UvNNcE5TzlVor3QfO9wRb1tvPI0pnQCus55sM5cwQqbFzq_DwHxy7GsfdJhyw9A9knSxGO_GK8TPnrGlY0Ee3VgZvFwWTcVhABJbz_C1ALFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية تسيطر على كامل جبل صبر وقرى الصراري وتتقدم نحو قمة جبل العروس الاستراتيجي المطل على مدينة تعز.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93408" target="_blank">📅 17:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93407">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhhif6HCCVd2l5HXHxJT-nEfu6UayOujCU404jmPWstdc9zgqZaDrr10cmhO7rrKt3kOGhE3hWgxJmw9SP5UZJ72tjAcY7lJ4Gescu9jPjaJAShNhgUcntvoarUNqSEyjgnMT3MCvE1fh2ss9iyC2ZrOa7-8XpPu3LQWM_VtkpkUEUBue1oyrKo3HIHJkPne5KXqkY-l5MsI44tSZIK8nTgdtii0kAxpY0jsmjej7x9NFNgbEqjmsDh-d8JR8KR90T6VAcoOVZ_ESUBLpiBgVhF8Z6Mm7ho-d-XPYHtQbAqrDXnrKFmgiC_bFi_6qlPxHrzRnfK388cdt6qRsXZVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط تتجاوز حاجز الـ107 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93407" target="_blank">📅 17:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93406">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خطوط دلتا الجوية الامريكية تلغي رحلاتها إلى الرياض حتى مارس 2027</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93406" target="_blank">📅 17:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93405">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خطوط دلتا الجوية الامريكية تلغي رحلاتها إلى الرياض حتى مارس 2027</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/93405" target="_blank">📅 17:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93404">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية تسيطر على كامل جبل صبر وقرى الصراري وتتقدم نحو قمة جبل العروس الاستراتيجي المطل على مدينة تعز.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/93404" target="_blank">📅 17:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93403">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
القوات البحرية لحرس الثورة الاسلامية:
صباح اليوم، تعرّضت ثالث ناقلة نفط مخالفة من فئة الناقلات العملاقة (سوبر تانكر) للإصابة في مضيق هرمز، ما أدى إلى اندلاع حريق فيها.
وكانت الناقلة قد أطفأت نظام الملاحة الخاص بها، وتجاهلت تحذيرات القوات البحرية للحرس الثوري، وحاولت، على غرار الناقلات المخالفة السابقة، مغادرة مضيق هرمز والإخلال بالنظام والأمن فيه، الأمر الذي أدى إلى استهدافها.
وتعلن القوات البحرية للحرس الثوري أن أي تعاون من جانب السفن التجارية وناقلات النفط مع الجيش الأمريكي، الذي وصفته في بيانها بـ«الإرهابي والمهرب والمعتدي والناهب»، في مضيق هرمز ومنطقة الخليج الفارسي، سيواجه برد حازم من جانبها»</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/93403" target="_blank">📅 17:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93402">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFDuepUwUX-msBACUSwTqlC6bcqz5Zrs698PYhhCMe0G0jTEZBVFnq1PslwcDAHImt9Qsp3Dff6AJYHX6PxTIfmsOmhu4R8D1nZnGC8Obj_9Ipt27huW4Yg38cTnAq8ShqmfMWpm_LT7XhdKEza7huiD70X3kFh8Qh6iOzh_tCAOGKhA8kEDOnhAuBmgSdaaIVHIwyMSxI4sUUgwfGT0kUsDqbq7ZdltoL7o9lMfLS0esyukd7Enakk0j8lfXCQwDJvSKBajdWqzKGI9KFEZ5OTM_eVL6M0ZOrglVSD3mMgLTNnAbucPzaEPzH1wk4hf1qfNlxM__1fbPEyUO7E_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناورات صاروخية ينفذها حرس الثورة في الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93402" target="_blank">📅 17:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93400">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tw2JMfAEV7GTXJZdgKo5_JvOt6p0epLQcZy2HhIkWSW-cD5q27kApMW0_mEr-dnYdnU6UHLp87Gk8X-t6RpkdYdkFE4YDPXaofLOCpP4ZiysXvUIjrra1ChJLxkqjGOM7rUaxyH0UYqDAeocWFLfMWeW4gDuhv4iqcefvok9V3XTB5zah30xuzQuz5jS7GXORuC6shaeHcWtmaL-mQi0LFKvH_albzefEIlecCHGcXpaX9w6hX0Pqo1tKQWOLV5RpF155f3oAgZspfMODF2xza2HJUw5IISGGtxlli5HT4ic9MWjV8wfbh4st5o4SgFP965VfEHIVVQCeUosETEieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qAgbFAoBeW12VOFaN6sZ8I3y5U2y_K85l3r0gVztc7Kk0xl4ebZcWURWeRy7Fy2o9x4i1QEdEmQtLiTQ2pXCg1Wl-QeYD1Cjbu96-d8euRyp_79JJmQakqnCNYJNDLmMATbOHK8aVvxc-K66k8WWwwZhj9B5AxIoxHVatd-5-xPRp_PJpcFcAgIMsW2x4aqkph_v6nybFYpshoGVTid1Fku8bEETGxUSQWuGUHQnZgDK7k-G6A5hvM91pqlc0oCySUHIkn-YCAs4iyinS6StxJ0KlcPm5oguZJKzmJ8T2PxkBQZDz5oPpmHpvZ_CCpGEfjgWIK03tKiVUQd3mXg45g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حرس الثورة يبدأ باجراء تجارب صاروخية</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/93400" target="_blank">📅 17:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93399">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حرس الثورة يبدأ باجراء تجارب صاروخية</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93399" target="_blank">📅 17:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93398">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020de12a7b.mp4?token=Kok64z2gzyNzT4z_uETiuH1g2jZ8fRPjbhYampvx4S-q-rVDDDlqP1I-KisMNmihjzeb83wHK7pDo7-SRgw8oPQmOlduECxlTvGIGZj02-9fbF8e4ocOZ1LsS8OjziD3sgFjr2h5jmjvdPWGnEAqLOt0ibRTkh6hSuOIReYp48bZwaSCCnXG-T4aJYQE2b31rcMsEjSxvA6kbO5No-O8YpiAmb7XBUja-08YmLUb0j44P8qKqu6eB6BKPyw_q4TXuzBwjWzJym7CqdNwpP5UulViypWN0tA0GhcrCh6HtI3kmdi9cl-xHT5KBtAUWO3mD2IKx_BW3i_iQhnYSDYxhgvaSWg8s8JeJAu3I10oY4C9niH_1d5d00Q62J8KD0xF44N1EQz3CwRpsT8UUHh8MU78SY83zF5OwR3X3C9i6zEo9M_pHmG2FvjPdOIV63O-jzRuGEN_PA7xSKCy9Zm1ZhRKfsf40pgA0gmcUC5z_H0vkKEQneoM7y8jEPF51Sde-9meoCE2uIuYGQApULex3zzJyTPXiSmCUblMyTeZvLoc-sBm7Wf5qKj31f4MpmuTlGYi80z10WQAj4x4LqJ7HZOyYT8CJ8-YDu7lWtTMAEDGwBzkA5CzqdcPLczQ0XaG2U7QpVm2YZkbHavSy0hwAH7iKdYivR5sbnCaGB58nCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020de12a7b.mp4?token=Kok64z2gzyNzT4z_uETiuH1g2jZ8fRPjbhYampvx4S-q-rVDDDlqP1I-KisMNmihjzeb83wHK7pDo7-SRgw8oPQmOlduECxlTvGIGZj02-9fbF8e4ocOZ1LsS8OjziD3sgFjr2h5jmjvdPWGnEAqLOt0ibRTkh6hSuOIReYp48bZwaSCCnXG-T4aJYQE2b31rcMsEjSxvA6kbO5No-O8YpiAmb7XBUja-08YmLUb0j44P8qKqu6eB6BKPyw_q4TXuzBwjWzJym7CqdNwpP5UulViypWN0tA0GhcrCh6HtI3kmdi9cl-xHT5KBtAUWO3mD2IKx_BW3i_iQhnYSDYxhgvaSWg8s8JeJAu3I10oY4C9niH_1d5d00Q62J8KD0xF44N1EQz3CwRpsT8UUHh8MU78SY83zF5OwR3X3C9i6zEo9M_pHmG2FvjPdOIV63O-jzRuGEN_PA7xSKCy9Zm1ZhRKfsf40pgA0gmcUC5z_H0vkKEQneoM7y8jEPF51Sde-9meoCE2uIuYGQApULex3zzJyTPXiSmCUblMyTeZvLoc-sBm7Wf5qKj31f4MpmuTlGYi80z10WQAj4x4LqJ7HZOyYT8CJ8-YDu7lWtTMAEDGwBzkA5CzqdcPLczQ0XaG2U7QpVm2YZkbHavSy0hwAH7iKdYivR5sbnCaGB58nCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جيش العدو: نحن بصدد التحقيق في الحادث. كان هناك انفجار ناتج عن سقوط قذيفة، ونحن نحاول فهم ما تسبب في ذلك - لا نعرف ما إذا كانت القذيفة قديمة أم حديثة. تم نقل جميع المصابين من موقع الحادث إلى المستشفيات</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/93398" target="_blank">📅 17:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93397">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اعلام العدو: أحد الطلاب عثر على الجسم المتفجر، وتجمهر طلاب آخرون حوله، ثم وقع الانفجار.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93397" target="_blank">📅 16:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93396">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اعلام العدو: أحد الطلاب وضع الجسم المتفجر من مخلفات الحرب داخل حقيبته وانفجر</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/93396" target="_blank">📅 16:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93395">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اعلام العدو: تشير التحقيقات الأولية التي أجرتها جهات الأمن في الموقع إلى أن أحد الطلاب أدخل قطعة سلاح إلى حقيبته، والتي انفجرت لاحقًا عندما كان الطلاب متواجدين بالقرب من الطريق.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93395" target="_blank">📅 16:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93394">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اعلام العدو: تشير التحقيقات الأولية التي أجرتها جهات الأمن في الموقع إلى أن أحد الطلاب أدخل قطعة سلاح إلى حقيبته، والتي انفجرت لاحقًا عندما كان الطلاب متواجدين بالقرب من الطريق.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/93394" target="_blank">📅 16:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93393">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الاعلان عن مصرع صهيوني ثاني</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/93393" target="_blank">📅 16:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93392">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اعلام العدو: لحظة ايقاف نتن ياهو البث المباشر بسبب الكارثة التي وقعت في الشمال.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/93392" target="_blank">📅 16:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93391">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a4f25f760.mp4?token=HgImRWWJdJwWMeKjnpo-d3ccIlbQHLW70lyWP-CkVAhtVY6fbcfJizc3FKPxaEYSMxYJDN40WHQuZBFvNpkbon6Jf7CaOVIP91rFIpEHcgyzbBN-5ZQgq7_OY_4YDNOxQSd_3JnzKeCOQd_hvgeg8A1-ACVHz0eMyyvGeEvoodhj_QhhX_6g0M54tYwkuBlONlQDHuqy09GOSy8jw4FBARvr9a-Y4KlrvSHM2nRUk6fNq9SFpqj5d8fhMOEPiVMRzubj-Xr-DLovd_H0npFXpRZOBr_J_nphY742jAC4Xngnuilv-0byHa4cDnniAZ6YXWHoDeHdwWQ9G0mkuFBBAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a4f25f760.mp4?token=HgImRWWJdJwWMeKjnpo-d3ccIlbQHLW70lyWP-CkVAhtVY6fbcfJizc3FKPxaEYSMxYJDN40WHQuZBFvNpkbon6Jf7CaOVIP91rFIpEHcgyzbBN-5ZQgq7_OY_4YDNOxQSd_3JnzKeCOQd_hvgeg8A1-ACVHz0eMyyvGeEvoodhj_QhhX_6g0M54tYwkuBlONlQDHuqy09GOSy8jw4FBARvr9a-Y4KlrvSHM2nRUk6fNq9SFpqj5d8fhMOEPiVMRzubj-Xr-DLovd_H0npFXpRZOBr_J_nphY742jAC4Xngnuilv-0byHa4cDnniAZ6YXWHoDeHdwWQ9G0mkuFBBAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضلت بس جنطهم</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93391" target="_blank">📅 16:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93390">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد ضرب تحشيدات العدو السعودي وتدمير وإحراق آلياته في جبهة الفليحة جنوب محافظة مأرب</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93390" target="_blank">📅 16:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93389">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اعلام العدو: الجيش الإسرائيلي يفحص احتمال أن يكون الانفجار ناجمًا عن صاروخ لحزب الله أُطلق خلال الحرب ولم يُكتشف حتى اليوم.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/93389" target="_blank">📅 16:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇸🇦
السعودية تعلن عن خط ساخن لتقديم استشارات نفسية للمواطنين بسبب الاحداث الجارية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/93388" target="_blank">📅 16:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بلدية القدس تفتح ملاجئ في حي رومما.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/93387" target="_blank">📅 16:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بلدية القدس تفتح ملاجئ في حي رومما.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93386" target="_blank">📅 16:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jz0woaFUAJ6vw7kbyD8QT4Y41h0a05PqrUptgk7eCEmzx1-c6K9xMnjdoN78i9ZosB8PeExQ0tu7ZDtr1xl6e4fdVJoRfcUbUZcirXgzju1id2EWYQfDltCxEmdXKO0redlhU_6vQb-sCiBE3g_Rmlg3TxtkIBGTLDjxVm5OAKJ2fmZnX3pVmpzEAkPL2EN-tQX8KJ6PmhT77WSq4fUMqwrWv1RA7Cgjhl6TjfHKeZRhJh4d-W8VuDPEykoKrM6QVJkYxDH_fPrA33DfupFQ3G7NDet6gnWgVMi1_wI2E-QMgdudpOkn_exJXZSdIYCYmskZqlGHfMSNEgRU8cthUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام العدو يعلن عن مصرع أحد المصابين في الانفجار الذي وقع في سلسلة جبال راميم.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/93385" target="_blank">📅 16:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الاسعاف الصهيوني يستنفرا جوا وبرا لاجلاء القتلى واعداد كبيرة من الجرحى</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/93384" target="_blank">📅 16:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdfMYBMNME3Q67iv01q4G8M6Hb4dQ4jRo_a1f2FjCwp5iDo53978XIioGQ8QgCnzgC1MXakCknVIYgGlqEasPghm9D3IYVbF3imidn23ztXQVQfwPWKPdVmY8l_O3pndQdfprlMgHrbyd7Yk-hrlxeOdvhBCFFKa4j8M-u8kpPntir-Bw_y-88xZ7DBeT4EbjoTyNj2IUw_8WBe8piecEeuIHU9jY2R0O-V9J6Rp66aEw-8hW080J7_S8djkXniXctG2LJKGAxth-4pL6YfhNDmmuQeTLzXUn-3Gh8BWiWgIWvh8YD7MeDHIAcaqOYJ_dY7lVPXnX2fg-r5b-OXH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالة من الذعر في صفوف جيش العدو الصهيوني بموقع الحدث</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93383" target="_blank">📅 16:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d9c431a9.mp4?token=cYA7BtAhDQ1pRhEpi-XbSIbSKo0W7D_6lOfkhPOpHcvJ2ttpA95YsVIiFG6SQnGA6l6AB__HsY9RW4jmxEK0vPnUb0bfmx6gE0Uams-0KGblsJ_HepwyCzBosTz1vfhK5C8Nx_cyy9a4aSasqXJpLbBF3kTEgWjxInwCOBlVxGs-FxEYdsUHyYfrNJEzve3HyTSxJGOPe_AvljfeBn4Rk8Yp2hkkfevUuEuYNyg6uZopnkoPB4D3BXK6KkDUw8QU-QTUnxYEQOTlUN3nXgoq1KR2pk3z0i7O9Ss3_PsFEFK7MqkBaJXcSMrhXPLit1dttfHIYAyJK-Yph3Pol1crjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d9c431a9.mp4?token=cYA7BtAhDQ1pRhEpi-XbSIbSKo0W7D_6lOfkhPOpHcvJ2ttpA95YsVIiFG6SQnGA6l6AB__HsY9RW4jmxEK0vPnUb0bfmx6gE0Uams-0KGblsJ_HepwyCzBosTz1vfhK5C8Nx_cyy9a4aSasqXJpLbBF3kTEgWjxInwCOBlVxGs-FxEYdsUHyYfrNJEzve3HyTSxJGOPe_AvljfeBn4Rk8Yp2hkkfevUuEuYNyg6uZopnkoPB4D3BXK6KkDUw8QU-QTUnxYEQOTlUN3nXgoq1KR2pk3z0i7O9Ss3_PsFEFK7MqkBaJXcSMrhXPLit1dttfHIYAyJK-Yph3Pol1crjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالة من الذعر في صفوف جيش العدو الصهيوني بموقع الحدث</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/93382" target="_blank">📅 16:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93380">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5Z3mxtn0218rqHzxOy_xSXB18nevOPmQtp7w_aS0Yeaivnb0naw_jwSBZsdWGUeemtI_sr7JpNrzV7gmzao7g6vgpz-0tgfO7Gh7uDNasLesRr_Pl2YKWOlDE3FUaJucXB_8SwYJI9sRuGtiHOI5VgFjBSHm-0qUi3D-3dF--p1v7F5_XMFbcC69i87PL3Hihj8FP47Gf9ACWZJUMuG2qqwBktQ2P0QggM9GuvjO_NZvXhSepL_Gq7pTZHTes-kXSeR-qWEQbKiBz-aL_MmdxlwFEg_5ktQmcca6XkMx3gdaY7e9pCeqFy6c0j9mlpS6K1OWw94Z5MLByTOWdDHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXSuYrvoNxt0bk6ej0eO0dKqNWjKZfTHtfKTVhqY0Xp2dK0zcWClrSAquNfdFoHtL7G74i5qd6oRnwahv02srPoFW4QtVUu_UkaYpFDecRQ-oTZUL7LKU2R7s0KCQkWCShbt2XTYEt_m321J3ZeTmErdyVODZvxCdKZ-Eztx3k1LYbIf8EYUMY0zq3S2Jy9YOyZxlY_S5Ym5sta07Dw4pjK5V697VYvi3wxWGAdxTVHyvS7DqOdff4ZwPOglWx-qY4YsBjKBIiEzzDzxiU11YRiRohlbl9GmQOhAsaMS40GXfkXiSpKmbczHyB31cT3V-OpLMFHyYdZQpvj3EdQuIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طيران جيش العدو يتجه لموقع الحدث</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/93380" target="_blank">📅 16:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93379">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90fc74ebc8.mp4?token=onlpmMEDkzB-uzgSZaknu8n47_T2qaoRRgdUYCNTHj-1ScEP-vkYiRH9OoBCGDzGlAl7SA1xK4bIK0N632HTvKrJ38dPSWmHm10J9kouAFO7yFTJS9dYDTfhV7bvJrGI50w1p-70T7Sb86V492RpWUERijZCbmtWKQF9RCPSLdvS0rZitc_5cIWH5rS4G74xDMc1FXmJytJ2vHSElUw55B9NTm089wQIvSQ1ljlpxVIAltM79drgFDe-mG3JNK-bt8CGePV0Bi9mi2deu8-upVVVA3v4JCdyuoOtrCnuGx5-Sij9pQRjSOhaAdkSGGoh5J2rKjaDLh9g75iNf-pRIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90fc74ebc8.mp4?token=onlpmMEDkzB-uzgSZaknu8n47_T2qaoRRgdUYCNTHj-1ScEP-vkYiRH9OoBCGDzGlAl7SA1xK4bIK0N632HTvKrJ38dPSWmHm10J9kouAFO7yFTJS9dYDTfhV7bvJrGI50w1p-70T7Sb86V492RpWUERijZCbmtWKQF9RCPSLdvS0rZitc_5cIWH5rS4G74xDMc1FXmJytJ2vHSElUw55B9NTm089wQIvSQ1ljlpxVIAltM79drgFDe-mG3JNK-bt8CGePV0Bi9mi2deu8-upVVVA3v4JCdyuoOtrCnuGx5-Sij9pQRjSOhaAdkSGGoh5J2rKjaDLh9g75iNf-pRIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاسعاف الصهيوني يستنفر</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93379" target="_blank">📅 16:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93378">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6073e9d6.mp4?token=XKKISMWZEGlkGavxe_OzZKG3iejCNVZioaFVIMHHudVo7AkNBtUAWoU0i3Pq_uA2iIJUV18DQZtGYN60bZXlaZbBw3ZctnKBwPkjt5W_rDJelHBmqk8jCx-jCQ9rtonnfAGTe3Izig5jSW5hL9dimZuRpInMr3S92DDnA2zI7lk0mnJyyeEwbWavjWhVxnKYHPLIgdUxihaQsIMyaAhCEiKQjXdCpkId--93fM21oaBNrJAGkMYGaMe836UqCbaZeXYw4DK2HWB9jA9oxL5Vbd1RgsIVo9EVtnHBf_O-BOQ_TqcBmafHQHHFRXKyLxaN2zAp-lrHcVblWzCzgxGp1YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6073e9d6.mp4?token=XKKISMWZEGlkGavxe_OzZKG3iejCNVZioaFVIMHHudVo7AkNBtUAWoU0i3Pq_uA2iIJUV18DQZtGYN60bZXlaZbBw3ZctnKBwPkjt5W_rDJelHBmqk8jCx-jCQ9rtonnfAGTe3Izig5jSW5hL9dimZuRpInMr3S92DDnA2zI7lk0mnJyyeEwbWavjWhVxnKYHPLIgdUxihaQsIMyaAhCEiKQjXdCpkId--93fM21oaBNrJAGkMYGaMe836UqCbaZeXYw4DK2HWB9jA9oxL5Vbd1RgsIVo9EVtnHBf_O-BOQ_TqcBmafHQHHFRXKyLxaN2zAp-lrHcVblWzCzgxGp1YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاسعاف الصهيوني يواصل الاتجاه لموقع الانفجار لنقل القتلى والجرحى</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93378" target="_blank">📅 16:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93377">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7431866df.mp4?token=R4NFyjbURqFV3e5Si7ZgEQOsmAB-xcBy-RW3dL5EfLTS_Kki_eXQh5EcNDpD4AaRenkeEcYi2H8L89iLR8aOfOxhmND0qQw_Stoez48jYOtYEoTWG0DOHI-RwyclSo7SUwX3u6UHAVz5s4IC-ha-ICMfAqhpeJed7vftWy629FiTJGZoARXs1TejmS8PEVTW6HlwzbPBDU9LvHT6XZDhLTr5LU95rEEnW_hgZWCMT_OOoKZucmC6pOh905eBRQgt5Iu7nJxVVtxamOWF9qQ0YFhUoWG9-KfxgNd17euLRCegGRUtkvi6Zlx-C_0Fxs-nNEdLIxdwR5JV-SxiAzbV-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7431866df.mp4?token=R4NFyjbURqFV3e5Si7ZgEQOsmAB-xcBy-RW3dL5EfLTS_Kki_eXQh5EcNDpD4AaRenkeEcYi2H8L89iLR8aOfOxhmND0qQw_Stoez48jYOtYEoTWG0DOHI-RwyclSo7SUwX3u6UHAVz5s4IC-ha-ICMfAqhpeJed7vftWy629FiTJGZoARXs1TejmS8PEVTW6HlwzbPBDU9LvHT6XZDhLTr5LU95rEEnW_hgZWCMT_OOoKZucmC6pOh905eBRQgt5Iu7nJxVVtxamOWF9qQ0YFhUoWG9-KfxgNd17euLRCegGRUtkvi6Zlx-C_0Fxs-nNEdLIxdwR5JV-SxiAzbV-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاسعاف الصهيوني يهرع لنقل القتلى والجرحى ومستشفى صفد يعلن حالة الطوارئ</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/93377" target="_blank">📅 16:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93376">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHRauXxV4d_pmL2zqrrg_B_4I2u6r5Kr0r5RNF7ZqETkd7w8YlH3CHJN4eAjMAIymfJHBojwxVB1mm6JCUi5XxAeHOL-zFAtV0C5wsPhfH1vpkHqibBVRUDVi4YLOeZZ0rUSJ7Z5qs1Onn0JWnA1yc7TYT1KJM0txO_Ohl1I9QHaTCFit0WkHJWi_XcDB2n6v2FpDroV6s6pzwwwDEbmbEFDEdjZZfQfH1_11UH77S_qGh8K6JbLIY4RxDXXUJMR5ziKQMmVSrsJtBuia-269IJV3Y-bGrF1GvjdPRM-PjyVYZUDeNIextFZj_6CgFkR88e8Sm03V5O_dS82ABNMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاسعاف الصهيوني يستنفر بعد الانفجار</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/93376" target="_blank">📅 16:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93375">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riWzgXFXvp3uISTHYi5NOQukx_94UgJWGPvZ4oNtKfqQEeCtqyErO-RWEEs1eZW6dZ7EGkVKo2TJDmcExLJY8pRKHJQO_AddPByIIu6nIlozeimZJCWdooFj1InMM5thk0CrxaYAVs9X7Rci24bcDzWkZA17nl8lBWfA-3ZTeU44X1UR6vIvjeDhdUB0LM62duYTEzI7PVw9tDuh32KlmBnkqNXriMRA-xugwwj0Pzsv1maNxHF0Ccm54Bb-NCzMrgV66vDJ8RwNPrIQtVG5YUFQHiGo2tJ6vE9FU25jIo7eBXp3Jgn5vMzIc9e_dxUMC9mxpclZpER18GZMEDiwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارة التعليم الصهيونية: إنها حادثة مؤلمة للغاية، وقلوبنا مع الضحايا وعائلاتهم.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/93375" target="_blank">📅 16:02 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
