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
<img src="https://cdn4.telesco.pe/file/BKs13liqI2kfBsjh0DZLkukbdaj4F5vxKpe0GBZ3rZOFJkMRe2LCYGGINRUpxSJ4FDQXD14DSvxpQl48y8PCMfahh1i25AOUko3tJV-XcPSm2kqhmqAR5WEkUxEy3YzI3bqMCSL4l8DS-lL85j_ABGp5f4Ayb-sFLuT8pl_eAYGXS-5IbZM2OEdf1cjbEtoFCoHQP4aTgRMF6Czv-gwIeI6j7IUb-_CmSG4MC5wlj-i17GrEwRIwJDyVq2czshuYMG2Jo7LooEfLT5J9Yys7d0WI8GTvYukedz4pip93mPhGzA9Z6CaOzn5yNFlQ4_A_BwZY5hkH_kefziso-l9J8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 269K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 14:44:54</div>
<hr>

<div class="tg-post" id="msg-88724">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
الاعلام الاميركي: تعتزم إدارة ترامب إنهاء المساعدات العسكرية الأمريكية المقدمة لقوات البيشمركة الكردية في العراق، وذلك عند انتهاء الاتفاقية الحالية في 30 سبتمبر.</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/naya_foriraq/88724" target="_blank">📅 14:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88723">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab8369cbea.mp4?token=eeh0RrNqfRSTy86KHsBwdf3n6hpzYN63X2Etb4X2Wwa8CIMJGzkQ_U8Z_v20V6kGgO-PnLZRfy-q8WU5zcUFK12gvg5c5NDqwjb8w2vfGYR2Tjp3wFdIRjNdRxqVYWXOieXQXprtJVB0tWp-Uw3Vu8lOgDaoJ-TbZPFu2eGEnqHS23oU-d6gY4Miyk30hlc-2e5014F_vXr_VP0Ene38I9r2QOrYQFx0QYZ9uFKpNbZSKvltwL_YAWT844r52Bi32-F7eELaYYHqVtGS086Wp28vaBvTDIRIGoN_xpyhtHBaw0wbfio1j1gbQ7_Ny37v5WpluQfJqBr3GrwN1TIcug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab8369cbea.mp4?token=eeh0RrNqfRSTy86KHsBwdf3n6hpzYN63X2Etb4X2Wwa8CIMJGzkQ_U8Z_v20V6kGgO-PnLZRfy-q8WU5zcUFK12gvg5c5NDqwjb8w2vfGYR2Tjp3wFdIRjNdRxqVYWXOieXQXprtJVB0tWp-Uw3Vu8lOgDaoJ-TbZPFu2eGEnqHS23oU-d6gY4Miyk30hlc-2e5014F_vXr_VP0Ene38I9r2QOrYQFx0QYZ9uFKpNbZSKvltwL_YAWT844r52Bi32-F7eELaYYHqVtGS086Wp28vaBvTDIRIGoN_xpyhtHBaw0wbfio1j1gbQ7_Ny37v5WpluQfJqBr3GrwN1TIcug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حريق يلتهم محطة وقود بالكامل في محافظة دهوك ضمن اقليم كردستان العراق</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/naya_foriraq/88723" target="_blank">📅 14:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88721">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇱
إعلام العدو:
محاولة دهس قرب قاعدة عسكرية للتدريب في الأغوار بالضفة والجيش يغلق الموقع.</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/naya_foriraq/88721" target="_blank">📅 13:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88720">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKO39mQgPg5L0ich2ISV-SAY_rg_9N0NtjqJJE40sKBVB_Ogntx1zCqHvAGwMIcJJXPjGtEfauBJSFWnLIyVE4eqlUeSGYRRGj-2UZDjffxrTtSLZaPUv6QotJ6C6Jzeb6-7tuBcbdZs3buDZNHbKCRTrai_3KCiUvErwBUQZYCBJm1JVqDwrzZt5RxPndvbRW3LMUKrjIEbCTtnwo_oV5OhCrXKKAxgf2eqThCAvXZyOkbQERduoBDftgVZ5U_ksvhSM-0B2hFNtQQuoqjTKISfeoJX9Th0SpKzZKrMzm9HLByPm2sExZ0F8y1ayE-aj12WGn_K7DQvtLyHo0i3NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
سفينة تابعة للإمارات حاولت عبور مضيق هرمز من الممر الجنوبي لكنها تخفق في ذلك وتقرر العودة.</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/naya_foriraq/88720" target="_blank">📅 13:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88719">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
الحرس الثوري الايراني: سيطرة كتائب الإسلام على الممر المائي الاستراتيجي لمضيق هرمز حاسمةٌ لا لبس فيها.   في أعقاب التصريحات الكاذبة والمضللة للمسؤولين الأمريكيين بشأن انفتاح مضيق هرمز، أعلنت البحرية التابعة للحرس الثوري الإسلامي ما يلي:   بسم الله الرحمن…</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/naya_foriraq/88719" target="_blank">📅 11:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88718">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
اكتشاف وتوقيف شحنة أسلحة وذخائر حربية على حدود محافظة كردستان الإيرانية عند الحدود العراقية.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/88718" target="_blank">📅 11:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88717">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔻
هزة أرضية بقوة 4.4 ريختر تضرب قضاء كلار بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/88717" target="_blank">📅 10:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88716">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca77794.mp4?token=c_Zm-KzvKiEM43ZePUx2LEDM5S88j5EC9wqQ-o5qpnoFc7UvFcfDZ5mVfXDg5ScR6uWutfsGC9R0DH6InthaV2aU3oFzBNUJdinXqjAo25NsRKwS9iJ9ZmlBOVpgJSwG7cFFpnukCJRJN5h8CsoAkV8olpVe3ERW-3EGzOhhK0GoLgjrOzNGge1bwJGrTo6hzg4Vaw1X_UdorK3AerTQB-oj4_MpFpuTLaXcJfkyrev2GCylA6ekWp5gFH7B9L2qhYJpIIK9MA_eqoItQ4f8utN5Kp0jvvisApQcRtkEqq7OKJ8f42iuNyxgxheSbcaDMe5S3FpgaSjr7FLh1o15kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca77794.mp4?token=c_Zm-KzvKiEM43ZePUx2LEDM5S88j5EC9wqQ-o5qpnoFc7UvFcfDZ5mVfXDg5ScR6uWutfsGC9R0DH6InthaV2aU3oFzBNUJdinXqjAo25NsRKwS9iJ9ZmlBOVpgJSwG7cFFpnukCJRJN5h8CsoAkV8olpVe3ERW-3EGzOhhK0GoLgjrOzNGge1bwJGrTo6hzg4Vaw1X_UdorK3AerTQB-oj4_MpFpuTLaXcJfkyrev2GCylA6ekWp5gFH7B9L2qhYJpIIK9MA_eqoItQ4f8utN5Kp0jvvisApQcRtkEqq7OKJ8f42iuNyxgxheSbcaDMe5S3FpgaSjr7FLh1o15kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يصيب هدفاً في العاصمة الأوكرانية كييف وأعمدة الدخان تتصاعد.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/88716" target="_blank">📅 10:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88715">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇶
🇺🇸
وزارة العدل الأمريكية:
تم رفع الفيزا عن مواطنة عراقية " طيف سامي " كانت تعمل وزيرة حصلت جائرة من إدارة بايدن لدعم المرأة ومحاربة الفساد ؛ حكومة ترامب عازمة بمراجعة ملفات الجوائز الممنوحة في زمن بايدن ، تم وضع الوزيرة ضمن الشخصيات الداعمة للارهاب .</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88715" target="_blank">📅 05:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88714">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
واشنطن سارعت إلى نقل كميات كبيرة من الذخائر للشرق الأوسط لمواجهة إيران، وترامب قرر تعليق الضربات على إيران في يوليو بالتزامن مع تصاعد المخاوف داخل الإدارة بشأن تراجع مخزونات الدفاع الجوي.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88714" target="_blank">📅 04:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88713">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amNNCnOFzZ4_C68X7A6U7_i6ehPU3_elSNT1kGoVXZpqsds4IUjV9I1-t8bs_6WQKaUzGpVhItGjOEtm13L0wT2dUSqvozOXFVnYUG1VwZ1Dr_x7fc3Yx4KHi-oxioKRNk2HTWUHuADfoRKin83Tuaw0C5w_Pg9EdiU-7hXEC3c1j8HsoAktGj24ennQLembZp-nlvaPmIKEGsuxKmRb7WASs2ozOZYZABkRQ6VwigsMmCbo5fe6I0jdO0Ki0F_L7NHX6eqwgnsYDYBcKZKnn9i0r12SP3SV736VI8QQCNS5U0QadgZWDL65rHUA1cwJdnrTBD71i1-zoD7ig4vyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترمب
: أبرمنا للتو صفقة نفطية مع فنزويلا.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88713" target="_blank">📅 02:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88712">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
‏الحرس الثوري يطلق عدة صواريخ باتجاه مضيق هرمز.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88712" target="_blank">📅 00:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88711">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b125233d1.mp4?token=Sth8rvnIzYMjZQmCzJ_hWNmCNxxvy5gfv7loU_HN4NpuvcLfOv26i59t27wQspAmo45sn8TRw_Deagej-r6jyffyD6Qar8UMaADVjBkIpQQ670ln9wo4c9r1dMKTksJcM27e0YGKuQcnJ6RMeP9570mPFwC0htLkohWldav3sUU0n1V--WwOH3vbTCRdxAhiQH8je1dWFpnP5sVvt4phcC5Rpfhurd0-z8_TAa7ml2kXkrOHMwIGGfOgMfaSFDH5QL_DEUScEI6BfcYgIj8yKo-7h0eb51iHu4LYZVVnXQ84GRnHMeuavAI-CDye7yMkjfruHILxOMr41sk_GooOEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b125233d1.mp4?token=Sth8rvnIzYMjZQmCzJ_hWNmCNxxvy5gfv7loU_HN4NpuvcLfOv26i59t27wQspAmo45sn8TRw_Deagej-r6jyffyD6Qar8UMaADVjBkIpQQ670ln9wo4c9r1dMKTksJcM27e0YGKuQcnJ6RMeP9570mPFwC0htLkohWldav3sUU0n1V--WwOH3vbTCRdxAhiQH8je1dWFpnP5sVvt4phcC5Rpfhurd0-z8_TAa7ml2kXkrOHMwIGGfOgMfaSFDH5QL_DEUScEI6BfcYgIj8yKo-7h0eb51iHu4LYZVVnXQ84GRnHMeuavAI-CDye7yMkjfruHILxOMr41sk_GooOEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقجي
: في هذه الحرب، أثبتت صواريخنا كفاءتها بشكل جيد وساهمت في الدفاع عن البلاد بشكل فعال.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88711" target="_blank">📅 00:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88710">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qtp5D_KZSlJ-zsbwsP2RKjkfpwn1KHqc3Y0kfchG6HSZtbY-IR6UphmtVDD4TcstE88VlDqXFfNeaS9zipy5CJC2s1gOun6Ixe6i1wS0J26gmUfk5ccEhPiWv8_DqbOaTcvQFNZlfM7o-6NnPc5cBC8zIGNEQs-ZIseGnyap0PQ2-5ea-llcOAqZNxKGJ4CjfbgtZTKUZ3viBTZaSzZrBfrAWzsMVgvPwohyoR2U_JoelxnDzRMa4p7ELOcwFrfXc4odlbYYLNRSpocPjOEwQng3QiKByQPok-guXCisgsZM8lORXXcC7YzzB037Q14IMH0DvPHGAaWbg1hiurto3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يهاجم صحفية نيويورك تايمز:
اختلقت ماجوت هاجرمان، المراسلة المزيفة من صحيفة نيويورك تايمز الفاشلة، وهي شخصية بغيضة من الداخل والخارج، ولا تعرف عني إلا أقل مما يعرفه معظم المراسلين في هذا المجال (إنها محتالة!)، قصة مفادها أنني في 11 سبتمبر، لن أذهب إلى مركز التجارة العالمي في مدينة نيويورك، لأنهم لن يسمحوا لي بإلقاء خطاب، وسأذهب إلى البنتاغون في واشنطن العاصمة، لأنني متحدث رئيسي. هذه أخبار فاسدة أخرى، لقد زرت نيويورك مرات عديدة على مر السنين، ولم يتحدث أحد قط، إنها "مراسم رسمية!" لم أفكر أبدًا فيما اختلقته ماجوت، وإلى جانب ذلك، أود ألا أتحدث، لأنني أتحدث طوال الوقت، وهذا يوم لتذكر الضحايا وأفراد أسرهم الأعزاء. ماجوت هاجرمان مزيفة، وصحيفة نيويورك تايمز تعرف ذلك! سيتضح كل شيء في الدعوى القضائية المرفوعة ضدهم، ودعوى أخرى ضد المنظمة المانحة لجائزة بوليتزر التي فقدت مصداقيتها، لأن ماغي حصلت عليها عن "تقاريرها" حول "خدعة روسيا، روسيا، روسيا"، والتي تبين أنها عملية احتيال كاملة! إذا أُجبرت على الكشف عن "مصادرها"، ستكتشفون أنها إما غير موجودة، أو أنها لم تذكر ما نشرته. لقد دأبت على الكتابة عني زوراً لسنوات. إنها متطفلة، ويجب إجبارها على تسليم جميع الأموال التي جنتها من خلال تقاريرها الكاذبة عني.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88710" target="_blank">📅 00:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88709">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
الاعلام الاميركي:
تعتزم إدارة ترامب إنهاء المساعدات العسكرية الأمريكية المقدمة لقوات البيشمركة الكردية في العراق، وذلك عند انتهاء الاتفاقية الحالية في 30 سبتمبر.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88709" target="_blank">📅 00:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88708">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEgEHDOtvcbBkzZBvUpemriWKREV-swRhO16m8129nOEdKBBwzgMNLgTxeoiYTok-5Y0_smSw0vIwbjHehh2GPinzZBNcanXnlcQbH3a2hCsYeCc7NdkVkQlNT4qpDx57DFyegY1JuAA2szG3No3dmvjvEvzFUFguJ2FJ1HtOdSXuxjWxTR05ejAmZKFZRu5k1l64naNKv0014RIzuF4e97JaVSh8X38lZdfO9OvZOISxh5F4WeM9LlrTUSP4d6dGAFnW0Kpxo4GNQQIloymMEZ1E4H2kgQLu1ofPLYGdbA6UnD9smFWBZkGzMN8WT4ceOwOvHcrzxYuusZln9qZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الحرس الثوري الايراني:
سيطرة كتائب الإسلام على الممر المائي الاستراتيجي لمضيق هرمز حاسمةٌ لا لبس فيها.
في أعقاب التصريحات الكاذبة والمضللة للمسؤولين الأمريكيين بشأن انفتاح مضيق هرمز، أعلنت البحرية التابعة للحرس الثوري الإسلامي ما يلي:
بسم الله الرحمن الرحيم
إن تصريحات المسؤولين الأمريكيين بشأن انفتاح مضيق هرمز كذبٌ صريح، ولا تهدف إلا إلى التلاعب بأسعار النفط والتغطية على إخفاقاتهم.
إن سيطرة كتائب الإسلام على هذا الممر المائي الاستراتيجي حاسمةٌ لا لبس فيها، وبكل قوة وسلطة، يُغلق مضيق هرمز أمام جميع السفن التي تنوي المرور دون تنسيق مع الجمهورية الإسلامية الإيرانية، ونؤكد للشعب الإيراني الحبيب الشجاع أن هذا الإجراء سيستمر حتى نهاية شرور الجيش الإرهابي الأمريكي ضد بلدنا الحبيب، والوفاء بالالتزامات المنصوص عليها.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88708" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88707">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
🇨🇳
وزارة العدل الأميركية
تعلن أنها تعرضت مع هيئات من بينها مجلس الشيوخ و"الاحتياطي الفيدرالي" ووكالة "ناسا" لاستهداف  من قراصنة معلومات صينيين</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88707" target="_blank">📅 23:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88706">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
إستهداف هدف معادي بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88706" target="_blank">📅 22:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88705">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKYG0JI1zMGtxZPimRi4RlrDA4Kq_0IyDYp1qGLGTA6t3SmOlSMNzs0xEIVUBpAkOYuk-66Ge3urWJm3W9EpflG8VslPaHiDFTgR2WC9RW1mSGceXJmaCg2SyqM29cLlI7GcJKqdE9uzVCOKAcr0ob0KFFlYDOhb0t6BmFJ4mo587dSas2UX16arwAM-qjHfre0o4X4twCUEKvhPYBzLKZuEwHfHO1y_z30WBT79Bz-cInXGK74qVvqS5hTCsoZMf8S-A0-6Khx5yHH0vD-6fQMGXs6G3p1fHdAedvksRtANvTYokLNFzXgs5pfZF2nRP3UXfPlZpyD3nKf1BwwKsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد الثورة الإسلامية سماحة السيد مجتبى الخامنئي:  أعلن بشكل قاطع؛ ارتكاب أي شيء يضر بالوحدة الاجتماعية أمر ممنوع.  أثمن إجراءات حكومتنا التي نفذت رغم قيود ومؤامرات العدو الأمريكي والصهيوني والعقوبات والحصار.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88705" target="_blank">📅 22:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88704">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔻
الشيخ نعيم قاسم:
التضحيات كانت كبيرة جداً في فلسطين ولبنان وإيران واليمن والعراق.
التضحيات الكبيرة التي قدمت في فلسطين ولبنان وإيران واليمن والعراق أوقفت المشروع الصهيو أميركي الذي يستهدف المنطقة.
نحن باقون في الميدان ولن نقبل بالمشاريع التي يتحدثون عنها.
أنجزنا أننا كسرنا مشروع "إسرائيل" الكبرى ومنعناهم أن يصلوا إلى العاصمة بيروت.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88704" target="_blank">📅 22:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88703">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
على أمريكا رفع الحصار والعقوبات والإفراج عن أموالنا وإجبار إسرائيل على وقف اعتداءاتها على لبنان.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88703" target="_blank">📅 22:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88702">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88702" target="_blank">📅 22:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88701">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88701" target="_blank">📅 22:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88698">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BF_EIjUmkCt6Vzxc6-PHbzrGtZvCkpc3UxSLpTbpsKtpyJ5CbCKIj0pPpBEsMF8XTB4BNxYDbfmtCvIP5WQmUMIXA4uNPaPa7V6-1Or2uP-RyjioSFB6ibnoWKjiyAA6TGPyu1BKA90UsrUHO7UxIJhwMHg5BfaYUyrG1BbkvFsYz0B33hKm7zKnclk8CCwWs041OKCPdvh13Cr3Jkt_khJvimsHmJbdbp4wYoU_0dHkHt0jbDGDTfW3AAdpBpNy8lBMYEcnUQgWzTv4L7-cikNHNYiSoxg53_6yObZJdksaoGLJUOz1tmOJQqlkp6M_8J1VpVNSToBhNGfD_gOVOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kIGBc4Ou7epqzWum7tejhrWil6n0j3y-wyqZNBzpYc22y8xEalstGiEGWWQYh7dOFXEwuVfsKW8RlZKHdDyPBDeGAAImmpsJv8YHvFkiU48j9cdpUd6xd80NUY86e6fimqqStXrSqxNSg9IePGI_AA7cU2-fl-q2NVhX_nRpuLJtFLc9H_F5tbFP2PCABxZPWjgxmjwYo9dmGusl89N_SdA9yT84-RYGqDNb8-qj0paEoEIZbEimzq8XkGlYD-uPtRoEeMtU71aFKOKs_9JMlYd-pl8zCsDgCFqFK4OZnrdCaJZB2IKgKSLG9CAmPt4ZYnTjz8aamW6-HR9TaRLguA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8_6G763yEWCGc8Lh5_7j8tRjIZtnTblWVxzOutGAYP1NuVbvwvaf9lggfOCdFOtyAuW80GnbrwPIdPH9lLK7W21DvBwyafWfq2IO0OJTmd6RUc1awZWrIwBY6HOQNmUc377nJfB3X9PE0NG7xgCgQvjGfoPMk3oxMhgGG72dikd4xLFSep_YFc2SC9-4nPZwjzyBIpbFDrdxzE0r0sTfgYM3TI1aAxDzPBBeeEmQnmmCAvydmwEhptTtfpPy7u5tYlyLJrV8kFQBVp1eC2nrqyxD1YV1DW5fuuSIJG8QCxhsKMRB6GDynhGDUs3IBbuqJMbf4LFwOrlg49id4Wg9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تنفرد نايا بنشر وثائق تؤكد قيام البنك المركزي بحجز أموال 12 مسؤول عراقي بتهم الفساد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88698" target="_blank">📅 21:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88697">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63010842fe.mp4?token=my7Dp4OLrHNfI3ST-1XXJiJI33C5VESoF7EiDPHyJIPG6rybQ-L4AzymmhxXt1rI5PzjXtaR9lDHQkhNQrPCA2Rm6JRVGYLbLhKDAu688QfzR4qRKT5vpg0EiJ1H3ZPaevwqFPqUIfTt0YnIK1fLoLq1eN-gJZ_4zOP4mWCiy609je6SwET75QmScNCq-AmVaJU62hk0hsMMHUIKqpktbgV7R4EHbBFJtawnTuQHEcCx8edBuv4tYlq_NCd3DHaP3qVK75HD829sjO1hypHSgeDpP38zzSAG2G4zIAsStxDN3yznZXgHmmAfDKLsOs8B37JjpR2biOeRB9BDvBz6BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63010842fe.mp4?token=my7Dp4OLrHNfI3ST-1XXJiJI33C5VESoF7EiDPHyJIPG6rybQ-L4AzymmhxXt1rI5PzjXtaR9lDHQkhNQrPCA2Rm6JRVGYLbLhKDAu688QfzR4qRKT5vpg0EiJ1H3ZPaevwqFPqUIfTt0YnIK1fLoLq1eN-gJZ_4zOP4mWCiy609je6SwET75QmScNCq-AmVaJU62hk0hsMMHUIKqpktbgV7R4EHbBFJtawnTuQHEcCx8edBuv4tYlq_NCd3DHaP3qVK75HD829sjO1hypHSgeDpP38zzSAG2G4zIAsStxDN3yznZXgHmmAfDKLsOs8B37JjpR2biOeRB9BDvBz6BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
نتيجة هجوم روسي.. إنفجارات كبيرة وتصاعد أعمدة الدخان في العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88697" target="_blank">📅 21:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88696">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سماع دوي إنفجار عنيف في الأردن.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88696" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88695">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
عراقجي:
لن نتهاون في مواجهة انتهاك الهدنة، ولن نسمح للعدو بالتصرف بطريقة تجعل انتهاك الاتفاق عادة. لذلك، قمنا بالرد.
فيما يتعلق بأمننا، لا نتهاون مع أحد. مقاتلونا سيردون على أي هجوم بنيران أكبر.
نحن ندافع بقوة عن مصالح البلاد في ساحة الدبلوماسية، تمامًا كما ندافع عنها في الساحة العسكرية. في ساحة الدبلوماسية وفي طاولة المفاوضات، ندافع عن حقوق الشعب الإيراني.
لا نعول على الانتخابات الأمريكية ونقوم بالاستناد إلى قوتنا وشعبنا.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/88695" target="_blank">📅 21:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88694">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a3331e6d8.mp4?token=LuA_L2rrslwsBcGD5WgXf_JD2mHXG-xZ_a0Dxj9Gd0Y9FPUVu8z_1juZ_XTRD_eRCtdsUKMWNiZhFbrsjZ2WvuJYqDUgEQDctV0Jykp9Z93DdESVOAbGESeK5pmM2FgyyACkPGPg9YXjT4sw9Hp9qwOmRYu9YT3b5EQdIEOv0uuIhK5o-x-M_ETYsKNksW2BWv_HQAozn-SAaE-2GWQxY3Br4B45zk0vkLZZmEDcZaG8CTIg2RltBsnTT5VtAJ_A0FvVe2zkcvZXTT73WY_c38XpFx8dIVthvIjIZbfg87Q8Cte09LmjgiMAMS5-JDZUgzvxfz6pe8XeDemz2txMdzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a3331e6d8.mp4?token=LuA_L2rrslwsBcGD5WgXf_JD2mHXG-xZ_a0Dxj9Gd0Y9FPUVu8z_1juZ_XTRD_eRCtdsUKMWNiZhFbrsjZ2WvuJYqDUgEQDctV0Jykp9Z93DdESVOAbGESeK5pmM2FgyyACkPGPg9YXjT4sw9Hp9qwOmRYu9YT3b5EQdIEOv0uuIhK5o-x-M_ETYsKNksW2BWv_HQAozn-SAaE-2GWQxY3Br4B45zk0vkLZZmEDcZaG8CTIg2RltBsnTT5VtAJ_A0FvVe2zkcvZXTT73WY_c38XpFx8dIVthvIjIZbfg87Q8Cte09LmjgiMAMS5-JDZUgzvxfz6pe8XeDemz2txMdzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
نتيجة هجوم روسي..
إنفجارات كبيرة وتصاعد أعمدة الدخان في العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88694" target="_blank">📅 21:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88692">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8280ed98e.mp4?token=JLYPgkHD5dsOMHvvH8a8x3Wijkk9oU9svRxJtkXqrRe8-YV0ZfKvqA8OXuGVurhLMKJBjhKSDUc8fvdXrQji1iDouv3mvnZx0FmzqQXaEMBbg-sWeuDcrTnCmcSapfAovzIGZgkV_peu8vFlUtFwnLHn1GJ41Nx0xCpM_1jNmAmw7YtWkYrVfjg2plM1opH9gDSTj1jMTKw2z2CBnkcgS6zIy9aC7f8ABDXkq18ndmJQi0XhoJRloLacL1-_KMWK84TtBs0joKGxUImmrNxKDRK0MLLaF241XKQK0MvWriGUDik1e6q29cCUcjDgv2xra6O9KRPaw6K9-mMWQp8KQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8280ed98e.mp4?token=JLYPgkHD5dsOMHvvH8a8x3Wijkk9oU9svRxJtkXqrRe8-YV0ZfKvqA8OXuGVurhLMKJBjhKSDUc8fvdXrQji1iDouv3mvnZx0FmzqQXaEMBbg-sWeuDcrTnCmcSapfAovzIGZgkV_peu8vFlUtFwnLHn1GJ41Nx0xCpM_1jNmAmw7YtWkYrVfjg2plM1opH9gDSTj1jMTKw2z2CBnkcgS6zIy9aC7f8ABDXkq18ndmJQi0XhoJRloLacL1-_KMWK84TtBs0joKGxUImmrNxKDRK0MLLaF241XKQK0MvWriGUDik1e6q29cCUcjDgv2xra6O9KRPaw6K9-mMWQp8KQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
إندلاع معارك مسلحة عنيفة وخروج الوضع الأمني عن السيطرة في بلدة جديدة عرطوز بريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/88692" target="_blank">📅 21:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88691">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmUMT2TPB3sNMobeG6Xleu3-_0xIQ89AVT3QVcHje6wTvlu8yNqwZfqBCaLYoIZ2B5d1ibbym59Uo1hcdxrVhp2TH9mFHeIQ32VPeYoZ4A3HxLQx3xUjoskHwI7QZiH2AksKgWjaBToeWsoz7u3EXedcomzeSopgdoWDrduWsFBHJ6by4WfGlrmjBspokE7YUkLdwKIET0jel8q-AbnpOkkbLjUjJ36uuLUiXFqnJG4J1aAJsGMOYrdyMOk4R8C3nDAgseg5-OXvuCUTgveDQJE3sKgWXgrlU9VmmRnQ_98fEH9piUnVpkEe1ziTO5-w4OuffJW9h744jwWiXn-SSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد الثورة الإسلامية سماحة السيد مجتبى الخامنئي:  أعلن بشكل قاطع؛ ارتكاب أي شيء يضر بالوحدة الاجتماعية أمر ممنوع.  أثمن إجراءات حكومتنا التي نفذت رغم قيود ومؤامرات العدو الأمريكي والصهيوني والعقوبات والحصار.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/88691" target="_blank">📅 20:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88690">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔻
مسؤول في حلف شمال الأطلسي "الناتو":
لم يتم تحديد أي موعد لإنتهاء عمل قواتنا في العراق، وأن مهامنا مرتبطة بـ "الحاجة"؛ تم نقل فريقنا من العراق إلى إيطاليا "بشكل مؤقت"منذ شهر آذار الماضي بسبب الأوضاع الأمنية.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88690" target="_blank">📅 20:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88689">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979455137b.mp4?token=CeHO__7M_xlews2TWT0H-DUvkNUpW_rr0n-0WllhRWUJMS2Z603FlGPckj7m7DQocqmeWJDzreMJY4zCVvdJoyezbNrBdOgcnyvIDcFfxcVQPllMMfkhhMPkHHuGctI_ER3JIJ4-_iwin3whYptc-JesrH7F-FzTyNW0aHasJtjE3N3iEBa7TrZ3-8I5esqmUOYP5qymJVCSzi-GmH6qUceobbc88VERo4LLKQNG_srsC3c3RNi1WjA78QalTBA6WLQsC-rUYVN3dgtZ3VidaQUMBLSl3y7a9HFa_zJ3GTc1zKSbdEvLvtkmMGMoH05QzC6BmAYTRvfrBb34Zx_HXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979455137b.mp4?token=CeHO__7M_xlews2TWT0H-DUvkNUpW_rr0n-0WllhRWUJMS2Z603FlGPckj7m7DQocqmeWJDzreMJY4zCVvdJoyezbNrBdOgcnyvIDcFfxcVQPllMMfkhhMPkHHuGctI_ER3JIJ4-_iwin3whYptc-JesrH7F-FzTyNW0aHasJtjE3N3iEBa7TrZ3-8I5esqmUOYP5qymJVCSzi-GmH6qUceobbc88VERo4LLKQNG_srsC3c3RNi1WjA78QalTBA6WLQsC-rUYVN3dgtZ3VidaQUMBLSl3y7a9HFa_zJ3GTc1zKSbdEvLvtkmMGMoH05QzC6BmAYTRvfrBb34Zx_HXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
إندلاع معارك مسلحة عنيفة وخروج الوضع الأمني عن السيطرة في بلدة جديدة عرطوز بريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/88689" target="_blank">📅 20:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88688">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
قائد الثورة الإسلامية سماحة السيد مجتبى الخامنئي:
أعلن بشكل قاطع؛ ارتكاب أي شيء يضر بالوحدة الاجتماعية أمر ممنوع.
أثمن إجراءات حكومتنا التي نفذت رغم قيود ومؤامرات العدو الأمريكي والصهيوني والعقوبات والحصار.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/88688" target="_blank">📅 20:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88687">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔻
‏
الإعلام الأجنبي:
قال نتنياهو "سننقل المنشآت العسكرية تحت الأرض". ويبدو أن سياسة نقل المنشآت العسكرية إلى تحت الأرض درسٌ استخلصه النظام الإسرائيلي من الحرب مع إيران. فخلال حرب الأيام الاثني عشر وحرب رمضان، استُهدفت العديد من القواعد والمراكز العسكرية الحساسة للنظام بدقة بصواريخ إيرانية، على الرغم من أن جهاز الرقابة في الجيش الإسرائيلي منع بشدة نشر هذه الحالات في وسائل الإعلام.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88687" target="_blank">📅 20:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88686">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
ترامب:
أنتم ترون كم نحن جيدون في القتال. نحن نقاتل بشكل جيد جدًا. انظروا إلى فنزويلا. 48 دقيقة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88686" target="_blank">📅 20:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88685">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0568799d32.mp4?token=IYorV9rgB-IjwGXU0eDituGVgCcEj79XOy0aRcpCCR--ANlZMmf-T1WHoyQULj5W8CzVv4y84u0NVtkq14xmX66xRVg93XOl-dVNR1zdtWHvrp0-QPIqT7O6vaYdf49XS4iYdUI1kUbkV59m89PDpAHFpKvftGj-40C-riIVzsxsHTLpUX-xQ4L7x_Oonx1INkg11jyY43-FqvgkRcS8p8Q-WtuTwO1PSYl97AF8JlPTltPQ-8vZZ09YMdLneD-NkOz5gI1SIVosAAZZPh2tzyFEEdtsDVdxu-EnAoHwMyl0CrUkK-y9Gfi4rTpVZqxz6M49UVkNVyRkb0eEtieS3RN1Hq0RpzF8PZJRe9gnyDI4rdO0AriL_6KKzw34-kyh5Qbhi2GdaRuN42hzmDClD98W0Y7TXQWKGohUSGQBNNwBkeeFIVsQ9Bhs9tof7lJhhyc_bBZMwc1QmVgX-uDsLbANKnK3p3MgTGYvOAKIClv4G9wQ-xPRUn5B6zCdRpoiOoQiv0_sfLejcZCyXFnjEybHwd9zxxnk5mSLzmBcA4gVj9x2-pKmlBe9i8w69sKNlAFPpZGoccPGRNsfUPYFxE7xV4KzPGKnzmmWyltoixtvqhDGo-xOxiuGC_0iBqyT8IZQg_xonD4eLjLlHzDXMwoFTS-owO-S8Rpd_PGkiWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0568799d32.mp4?token=IYorV9rgB-IjwGXU0eDituGVgCcEj79XOy0aRcpCCR--ANlZMmf-T1WHoyQULj5W8CzVv4y84u0NVtkq14xmX66xRVg93XOl-dVNR1zdtWHvrp0-QPIqT7O6vaYdf49XS4iYdUI1kUbkV59m89PDpAHFpKvftGj-40C-riIVzsxsHTLpUX-xQ4L7x_Oonx1INkg11jyY43-FqvgkRcS8p8Q-WtuTwO1PSYl97AF8JlPTltPQ-8vZZ09YMdLneD-NkOz5gI1SIVosAAZZPh2tzyFEEdtsDVdxu-EnAoHwMyl0CrUkK-y9Gfi4rTpVZqxz6M49UVkNVyRkb0eEtieS3RN1Hq0RpzF8PZJRe9gnyDI4rdO0AriL_6KKzw34-kyh5Qbhi2GdaRuN42hzmDClD98W0Y7TXQWKGohUSGQBNNwBkeeFIVsQ9Bhs9tof7lJhhyc_bBZMwc1QmVgX-uDsLbANKnK3p3MgTGYvOAKIClv4G9wQ-xPRUn5B6zCdRpoiOoQiv0_sfLejcZCyXFnjEybHwd9zxxnk5mSLzmBcA4gVj9x2-pKmlBe9i8w69sKNlAFPpZGoccPGRNsfUPYFxE7xV4KzPGKnzmmWyltoixtvqhDGo-xOxiuGC_0iBqyT8IZQg_xonD4eLjLlHzDXMwoFTS-owO-S8Rpd_PGkiWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قوات شعبية إيرانية تنطلق نحو مضيق هرمز ردًا على تصريحات ترامب.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88685" target="_blank">📅 20:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88684">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇾🇪
🇸🇦
هجوم يمني بالطائرات المسيرة الإنقضاضية على معاقل مرتزقة السعودية في مدينة المخا اليمنية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/88684" target="_blank">📅 20:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88683">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfnAqmLuQ09UGDzbIXZTquuDzoDj49ilpLuWxj254Gr813DkJo3sVoe5jg3T2Hk81faZMCa4GpkXwxnlyMZZMQq2bn84UjUo1FmTRfbCe6EsC6MAgcHS0JwGv3DRPNc7epH7NiiFAajQEdjQXdzRcAnB_UN6EbY4gIyDbFb5AdwSwcPBUVihzRpHUdDicJZ4gKksYbPRuzpsX7fjaO45PvAheYmJLv4x8ifgMtNilCZ_pnJ7gbZCafdIxEN4nakGS5TW30FjgtsmrG4FduMQ8_1fDzPy0oOUiVGZ-qNtACldYGtK6LuiF-j9AiMX3ZSTAiq01FLQ-2qziCHuyouJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇷🇺
روسيا تشير إلى ايران
وتفتح النار على القصص الملفقة التي صنعتها الصحافة البريطانية ؛ ماريا زخروفا في عام 2010 بشأن سكينة محمدي أشتياني (ولا يزال بدون تراجع) - كان ملفقًا بالكامل. ساهمت القصة الملفقة في تأجيج الضغط على إيران. ليس هذا بالأمر المفاجئ، بالنظر إلى سجل الغرب في التلاعب بالمعلومات.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88683" target="_blank">📅 19:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88682">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
إشتباكات بين القوات الأمنية الإيرانية وعناصر إرهابية في مدينة سراوان جنوب شرق إيران؛ مقتل إرهابي وإعتقال 6 أخرين.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88682" target="_blank">📅 19:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88681">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔻
‏
برنامج الغذاء العالمي:
نحذر من نقاط الاختناق في هرمز وباب المندب والبحر الأسود.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88681" target="_blank">📅 19:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88680">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇶
🔻
الحاج العامري لشيوخ عموم عشائر العراق:
-سنشرع قانون الحشد الشعبي وتحدثنا مع رئيس الوزراء وهو يؤيد ذلك
-فصائل المقاومة أناس عقلاء دافعوا عن العراق وسيادته وقاتلوا الاحتلال وداعش</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88680" target="_blank">📅 18:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88679">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇾🇪
🇾🇪
الحكومة اليمنية في صنعاء:
امتزجت دماء شهداء اليمن مع شهداء فلسطين ولبنان وإيران والعراق بمواجهة العدو المجرم نفسه الذي يستهدف الأمة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88679" target="_blank">📅 18:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88678">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔻
🇺🇸
أثار حرب أمريكا على المنطقة
ول ستريت جورنال:
‏توقف مشروع نيوم الضخم والمستقبلي في السعودية، حيث اصطدمت التكاليف الباهظة للمدينة المخطط لها بالواقع المالي.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88678" target="_blank">📅 17:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88677">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736924625c.mp4?token=pg37PSzMgnbeW8lyRy8Sa1grbSE9_DI3PkrpQrmtjQ0DmafGM9ulPa42YfUYRNH7bn2Ai7VQGkenMpxcKm2NhAN4DMKdzhnz7OKTE8JQnnvH7sPFNA0Xnb1CiG6WaD3jMxfye5WOTv2LpHfbyZg3z1ep_XGQKNSLE913uPAt9n1IGZP-6PWXQePuI-TnqS8mAr5Z99xnwGd_777pen4A4v2Nit-v9BuBcB_ukwwHCUXzBoaSe36PY0heiXSoRPI5Sw5OcLoKkf5SUAzIqd0QENnBE3iASuqXoYMwjWWecPaUXOHZSlReEC0eqR8Yfm5rBuvq_ymz3PbTLWv6R2l5qAGjjahqR4vgRCWPUlP55y_9Tp15nGVlXD16BLYjSxkpbeYEDbo_BbzJu_jVC02GQlK3c1MalXlt77W-bJkDlxk58jhceC3EtkbyS1dyB9l64gv77-Kxmd24hJFLxekOl37IhrWKffoO_1jwgCKqt8ZRYjVXYnUXWuL7TWXXeVRutozam7Hw8kCJNTJW2IHD22592_0Fmzpqs8JZr37nQZEkYOPV4hR9XunDUA4hD0lvXVTEn4Dnrvm2N5vSwpbBplERhoQiM_egbW9_c1TjeV3pmLrcTlnXsxSHX65lYVQIRrOW-BA7qe7KfVqxSUQ6TuqY9xUrLwRRH0Jfn1JD-HE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736924625c.mp4?token=pg37PSzMgnbeW8lyRy8Sa1grbSE9_DI3PkrpQrmtjQ0DmafGM9ulPa42YfUYRNH7bn2Ai7VQGkenMpxcKm2NhAN4DMKdzhnz7OKTE8JQnnvH7sPFNA0Xnb1CiG6WaD3jMxfye5WOTv2LpHfbyZg3z1ep_XGQKNSLE913uPAt9n1IGZP-6PWXQePuI-TnqS8mAr5Z99xnwGd_777pen4A4v2Nit-v9BuBcB_ukwwHCUXzBoaSe36PY0heiXSoRPI5Sw5OcLoKkf5SUAzIqd0QENnBE3iASuqXoYMwjWWecPaUXOHZSlReEC0eqR8Yfm5rBuvq_ymz3PbTLWv6R2l5qAGjjahqR4vgRCWPUlP55y_9Tp15nGVlXD16BLYjSxkpbeYEDbo_BbzJu_jVC02GQlK3c1MalXlt77W-bJkDlxk58jhceC3EtkbyS1dyB9l64gv77-Kxmd24hJFLxekOl37IhrWKffoO_1jwgCKqt8ZRYjVXYnUXWuL7TWXXeVRutozam7Hw8kCJNTJW2IHD22592_0Fmzpqs8JZr37nQZEkYOPV4hR9XunDUA4hD0lvXVTEn4Dnrvm2N5vSwpbBplERhoQiM_egbW9_c1TjeV3pmLrcTlnXsxSHX65lYVQIRrOW-BA7qe7KfVqxSUQ6TuqY9xUrLwRRH0Jfn1JD-HE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
اندلاع حريق في احد مقرات الحشد الشعبي بقاعدة سبايكر شمال غرب محافظة صلاح الدين العراقية</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88677" target="_blank">📅 17:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88676">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏الخزانة الأميركية تفرض عقوبات جديدة على صلة بإيران</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88676" target="_blank">📅 17:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88675">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏الخزانة الأميركية تفرض عقوبات جديدة على صلة بإيران</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88675" target="_blank">📅 17:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88674">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇱
نتن ياهو يزعم إحباط هجوم وشيك من جنين.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88674" target="_blank">📅 17:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88673">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1275ca3466.mp4?token=aV7_bwSCQhgeLvPbJV9-e1d6AVLEFyJxn-8Scx9X9lggy7usGKy2BlQ3EFmMxYhTOl8IR6gBAP9o3rvU282nUxP9wHVhz4GO65njoG0bnu0R13ZbK1RPG4TieBUwZaM6PWGawZJOviHVh6tgtz4A-NIfUSDdf4eBzd9qFax3tviliDAHqX29jUuVuiTldK6tF_oIrrb3tCgghY4Vzy3HekOHdkiMPL4T0T2RX17dX2oX5nj9FC473Pq9UlydJZaBsmIUblgIEKOyF1b9_R57ZflbsYF0rmrgH9pEuZEbHZlptapFJ1p1r6gL3Sq6aU8FVVmtUlc3UmFAj6I7fbxN-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1275ca3466.mp4?token=aV7_bwSCQhgeLvPbJV9-e1d6AVLEFyJxn-8Scx9X9lggy7usGKy2BlQ3EFmMxYhTOl8IR6gBAP9o3rvU282nUxP9wHVhz4GO65njoG0bnu0R13ZbK1RPG4TieBUwZaM6PWGawZJOviHVh6tgtz4A-NIfUSDdf4eBzd9qFax3tviliDAHqX29jUuVuiTldK6tF_oIrrb3tCgghY4Vzy3HekOHdkiMPL4T0T2RX17dX2oX5nj9FC473Pq9UlydJZaBsmIUblgIEKOyF1b9_R57ZflbsYF0rmrgH9pEuZEbHZlptapFJ1p1r6gL3Sq6aU8FVVmtUlc3UmFAj6I7fbxN-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازمة الوقود متواصلة في محافظة اربيل ضمن اقليم كردستان العراق ولا حلول تلوح بالافق</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88673" target="_blank">📅 17:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88671">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">المنظمة البحرية الدولية التابعة للأمم المتحدة": نحو 6000 بحار على متن 400 سفينة لا يزالون غير قادرين على مغادرة مضيق هرمز</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88671" target="_blank">📅 16:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88670">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇸
🇨🇳
موقع ذا إنفورميشن:
الولايات المتحدة تعمل على وضع قواعد للذكاء الاصطناعي للحد من وصول الصين إلى الرقائق الإلكترونية. الولايات المتحدة تعمل على إيجاد بديل لقاعدة الذكاء الاصطناعي الحالية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88670" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88668">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
🚀
🔵
إعلام غربي :
رصد طائرة مسيرة أخرى في مطار لايبزيغ هاله في المانيا ؛ ويأتي هذا الحادث بعد أسابيع من اكتشاف طائرة مسيرة محملة بالمتفجرات بالقرب من طائرة شحن أوكرانية في المطار نفسه</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88668" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88666">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1vpYn8zqUdjND4EbvNn5kUL8nqN0PXI5XUKbF81QGJfkB0-LOoIWc_aY6XZ61YTahAqbsTHQVM3HETxzaEweV-gshJAMlzPmww3L25mlpe-yfy1yY2t8I0pwxLQn65FuJRA7uxwTuKY6uz-kv65IQ-PhUouCZzrlceawGw0en0IxbsL6F0v3AljYpsIh-ym6fbK-2uEKRcd3sj1ZSkoncY9X91FlIpIUZAJGkeIlv0ZFbSes8hChEo80t-U6RQPJI_iJQS8FbOMXykljPb7aGsRzQlIAlyIZ85lRN4pUwPkHy8-EJIm2lzLlzQXWcJfzqmd7g_AnVvbUw4SXvLN6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKWoqaJtLRQA9UNZhW7G8akqF0MzjGAL3zJObiSQVaq5NM9rgzUwd8QMiMEXOjzLbHA0FKvNKELrOTmRL79QtHfiRJUBu0ka0471f-Lzmo8DuvU3R7ggWWab6kndvEkgwKY1e65_iyuO7R8LvAG4ub8cKvTL_8QhUtgYsg3mmBSVWg69ncZtNIpfjh0QHOIGCt8VT_ifbfsYp-L5WLwQJkPuD4hEVLYWK_ev4rmGmXUdnS0LdkBY-O3C8OD4bWjyUxkIcJsG1Yb5XlwdGTtkVb3bTc4UC7aoJLToZ7DBUKTuZI3iPmhPwsi6fB02itLWBurDZnQ8NNPEZp6rTaH72Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
بيان وزارة الخارجية الايرانية بخصوص العقوبات الاميركية:
بيان صادر عن وزارة الخارجية بشأن الإرهاب الاقتصادي الأمريكي ضد إيران
۱۴۰۵/۰۶/۰۶
في إطار استمرار سياساتها العدائية وغير القانونية ضد إيران، كشفت الحكومة الأمريكية عن موجة جديدة من الإرهاب الاقتصادي يوم الاثنين 2 سبتمبر 1405، تحت عنوان عملية الإقصاء الاقتصادي ضد إيران، وهو ما يرقى إلى مستوى إرهاب الدولة الأمريكية ضد إيران والعالم.
إن إساءة الولايات المتحدة استخدام الدولار كأداة لترهيب الدول الأخرى وإجبارها على اتباع سياساتها التدخلية والمخالفة للقانون الدولي فيما يتعلق بإيران، يُعد انتهاكًا للسيادة الوطنية وحق تقرير المصير لجميع الدول الأعضاء في الأمم المتحدة. وتُمثل العقوبات الأمريكية المفروضة على إيران، بطبيعتها وعواقبها، انتهاكًا صارخًا لميثاق الأمم المتحدة. إذ تنتهك هذه العقوبات مبدأ عدم التدخل في الشؤون الداخلية للدول، ومبدأ عدم عرقلة التعاون بين الدول، وهو مبدأ تم التأكيد عليه، من بين أمور أخرى، في الفقرة (2) من إعلان عدم جواز التدخل في الشؤون الداخلية للدول، القرار 36/103 الصادر في 9 ديسمبر/كانون الأول 1981، و"إعلان" مبادئ القانون الدولي المتعلقة بالعلاقات الودية والتعاون بين الدول، القرار 2625 الصادر عن الجمعية العامة في 24 أكتوبر/تشرين الأول 1970.
إن إعلان الحرب الاقتصادية على إيران هو استمرار للحرب العدوانية التي تشنها الولايات المتحدة والكيان الصهيوني ضد إيران منذ عام ونصف تحت ذرائع كاذبة لا أساس لها، مما يُهدد السلام والأمن الإقليميين والدوليين. جميع هذه الأعمال تُخالف القانون الدولي. وللأسف، فإن لامبالاة وتواطؤ منظومة الأمم المتحدة ودولها الأعضاء تجاه الانتهاكات الجسيمة للقانون الدولي من قِبل الولايات المتحدة والكيان الصهيوني قد أدى إلى تشكيل نمط خطير للغاية من خرق القانون وارتكاب أخطر الجرائم الدولية، مما عرّض الحضارة الإنسانية جمعاء لتهديد غير مسبوق.
تُثبت عملية المقاطعة الاقتصادية بحد ذاتها النية الإجرامية لمصمميها ومنفذيها في إلحاق الألم والمعاناة بالشعب الإيراني وحرمان المواطنين الإيرانيين من حقوقهم الإنسانية الأساسية، ولذا تُعتبر جريمة دولية وجريمة ضد الإنسانية. وتُعد هذه السياسة انتهاكًا صارخًا للقواعد الأساسية لحقوق الإنسان المنصوص عليها في الإعلان العالمي لحقوق الإنسان والعهود والميثاقين الدوليين، وتتعارض مع المادة 1، الفقرة 2، من العهد الدولي الخاص بالحقوق الاقتصادية والاجتماعية والثقافية. كما تُعد العقوبات الأمريكية انتهاكًا مستمرًا لحكم محكمة العدل الدولية الصادر في 3 أكتوبر/تشرين الأول 2018، والذي ألزم الولايات المتحدة بإزالة جميع العقبات والقيود المفروضة على حرية التجارة، بما في ذلك الأغذية والمنتجات الزراعية، والأدوية والمعدات الطبية، ومعدات وخدمات سلامة الطيران المدني الأساسية، والأموال ذات الصلة. وقد خلقت سياسة العقوبات الأمريكية الجديدة وضعًا جديدًا، ومن الضروري أن يتخذ المجتمع الدولي، بما في ذلك أجهزة الأمم المتحدة، التدابير اللازمة لحماية سيادة القانون.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88666" target="_blank">📅 13:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88665">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e23lDHElekfa9qBueOI39VN8JJbsN92k1xaVK_jg7zaTWUqg0eUCEC_k5no8e-8d0AaNMB7j7_-NNnr-JvXgcYD6-Gt7F_1cLvCveF0rCZHRNIfJsBAd9K4zn-wde-SZIktP386flhU79PJDWJ9gjAZCvWAgt4NO3XUYA5hKUwV7MIhEYCu6c0zzX6cI1z-z-W1M7Uzfh9eLvEStkg2WBuykx8xaVRhxIIJfzOehQBw6UmnIoRnHXYyZhYXPe4Aifr_OhCMN0weN5OfVmxE7d42PUD1rgoOfSz_yDMBJ6atgT2h5tKHQCaE3vu7XYU3QcGXpEucERgY9HbbRoGnsWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف يعيد نشر:
معادلة هذه الحرب واضحة: إما الكل أو لا شيء!
في منطقة لا نبيع فيها النفط، لن يبيعه أحد. إذا لم يُضمن أمننا، فلن تكون أي بنية تحتية آمنة، وأمن المضيق مرهون بغياب القوات الأمريكية. لقد أكدنا مرارًا وتكرارًا أن الوضع في المضيق لن يعود إلى ما كان عليه قبل الحرب.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88665" target="_blank">📅 12:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88664">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXFtgDo7V0ni5ON7RSA-d1xIxLV0XjhmUvxko4-4zR0YH5jTYJhkFWAnbHqUt2kdife3sHltc1LwWFBz4eegMKicohB6x904SvMuih7dvA74mlKqfO9kVLoCEWHa9_fGY2nnejADP7uAzOP8ZduWqDrzHgSoNzXKu7wV1x3pPl2A21Up017DTD_Q5wh1-upoedFTqCbRnrEoQwH0HBHyDwBcSRJMr7NGsq4_PHjnqY71Mw4VrVAN5AntQKxA7rEolt6UgJu_aR4E3mnBdlgYY4Keev3MYIcDnypQvxigyJc1M6SCpdWOvBNXFSDd7_s9u-W-fSd-y7MgnO3wV8fziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
نتنياهو يتوسل لبن غفير لكي يعقد اجتماعات مع سموتريتش حتى لا تذهب الانتخابات نحو المنافسيين:
أدعو الوزير إيتامار بن غفير والوزير بتسلال سموتريتش لعقد اجتماعات يوم الأحد. لا يجوز إضاعة أي صوت، يجب أن نتحد لإنقاذ الكتلة اليمينية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88664" target="_blank">📅 12:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88663">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇱
إعلام العدو يدعي :
‏أعلنت الشرطة وجهاز الأمن الإسرائيلي (الشاباك) عن توجيه الاتهام إلى مراهقين عربيين، أحدهما قاصر والآخر بالغ، للاشتباه في ارتباطهما بتنظيم داعش والتخطيط المزعوم لارتكاب هجمات إرهابية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88663" target="_blank">📅 10:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88662">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-PLxS3PkbPH7e3qK0qkVxYpV9m0fxHc48GDmXxr4lgehEIAeJZ4p49WVpw04iRpnxF0MQG0WHKaT4e9cCFr8RzNndJc6VQSPyb5x-qilD4O8TPO4C2ba52n1tByIJfp9a0sIltTQB1k2j0viU5mpA-AlUwGxfR5YaVIrYDme9b1msY75bJJfXf9DbP-VLvHXdEHieMFNRxcHAkVUIVIrq9rpQvqNTtnqSBxFCvAQ2ONzeRxUI-6mfUVsOwxU2uGDPBovQ2TN84s8AxQxBWevPFm-BtshICTqEDGXWXVZkI72TSMvIOwTA_38_vAWY9dA045XjmH_v23C8i34bowAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
أجرينا مناقشات بناءة ومبتكرة مع رئيس الوزراء وزير الخارجية القطري في طهران.
إن إعادة الدبلوماسية إلى مسارها الصحيح ليس مستحيلاً. ويتوقف ذلك على فهم الولايات المتحدة لحقيقة بسيطة واحدة: الضغط لا يجدي نفعاً. يجب على الولايات المتحدة بناء الثقة، والتحدث باحترام، والاعتراف بحقوقنا، والوفاء بالتزاماتنا.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88662" target="_blank">📅 10:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88661">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
🇷🇺
الاعلام الاميركي: سبقت رحلة مدير وكالة المخابرات المركزية جون راتكليف إلى موسكو معلومات استخباراتية أمريكية جديدة تشير إلى أن الكرملين يرى أن الولايات المتحدة قد ضعفت بسبب الحرب الإيرانية، مما يمنح روسيا فرصة لتصعيد العمل ضد المصالح الأمريكية في أوروبا.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88661" target="_blank">📅 02:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88660">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFcSUvjBUh4--Pt3wPZk91QyovNtIknrWnnbxnRNsTbQcaoDBd3g4_WqjHVfg_4MuLgtstsbY_tJCB5NVW4JvB8f-bwMs9kteAjy-bBh2yiaIMZ58u_eFi36mWAnR_xOWbOkqKODPUgGF6B2RJx39izncQ8L0JO34HQ7f2dF_aFC86SB4mHDy4HvtnCtmUVSZYyIMurLoDPmr2G8h0Tqx5egXaH7jq7WwofP3-glngaXj58jzwVr2fRvCc_l9YcXkk9FiDsjHsGL5eIyzDIt0rJdOuoxUb7LC5Kx62MDZ2aA4SHVA6cD8h5UV5hhfYgRP_R5JvAj3FWKWvJ04ZzwRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: قدم جوناثان هانت من فوكس نيوز تقريرا غير دقيق بشكل خاص عن جمهورية إيران الإسلامية الفاشلة. لا أريد أن ألتقي، إنهم يفعلون ذلك. في الواقع، إنهم يتوسلون لإبرام صفقة. يجب على بريت باير تقويم فاشله، من أجل التغيير!.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88660" target="_blank">📅 02:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88659">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzITikI1jjvlQHCYLz56mabIjafW6BKBsU0o1Scos3pTK2UCYnlAT49KwO9ZmTS3n0-HxlFV0mMnxpPkbRJgr4tHF90U80yU1qRyk5vjg_F9FWZcBHrD1j2GjOM-cRnupcN0_NV7MiZ-O8b_EyhDnu3ozui3w6lf2LHg0Rn931xBSpGGQybQzHacMqAcJ22x39O-t0CS7Wd2LdYCm5ztvP2VFb82M_uvNMHFhlFDN1OCH8J3ObqUTmQcZ3nvrWRQ-VoZWISPtoxOtKNEQEA1ek_Th5Tx94qQDTE5Q1JQWCEelKWktqs2B4CgkjKLSrOuR1pLLkddlRtyMnrhdDkMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: قدم جوناثان هانت من فوكس نيوز تقريرا غير دقيق بشكل خاص عن جمهورية إيران الإسلامية الفاشلة. لا أريد أن ألتقي، إنهم يفعلون ذلك. في الواقع، إنهم يتوسلون لإبرام صفقة. يجب على بريت باير تقويم فاشله، من أجل التغيير!.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88659" target="_blank">📅 01:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88658">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇶
اشتباكات عنيفة جراء نزاع عشائري في قضاء الجبايش بمحافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88658" target="_blank">📅 01:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88657">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">المراسل: هل وجه مدير وكالة المخابرات المركزية راتكليف تحذيرًا إلى روسيا بعدم مهاجمة أراضي حلف شمال الأطلسي؟  ترامب: لا أريد التعليق على ذلك، لكنهم لن يهاجموا.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88657" target="_blank">📅 01:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88656">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
ترامب ينشر رسميا تم تغير اسم بحرية أونتاريو الى بحرية اميركا.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88656" target="_blank">📅 01:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88655">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSODNsJhLfvWib4GLukEcOHSQZJ1kL1_uezM9N0B1eJnaDrRz2STYW8MsjA-KMNhZKaQqrX3bIkCAgPWuFRc1GlhIauO2bsxlA0klPZihXGdactb57l99GixyY23PKQn-mMYocpWySBWTpx_PythXlKuZ_3oMC42QzrduqABRlXIfUKhlEz_UT7WlxKvJVLNh7TlcZ0e_u9Ocsf6JEgae3rXOjrx0tsAL6o_WEebfVSsFomr1KJ63WTlzV4NHNwWhC77QYUiTzAYvwfgfN3P6O3vCjUD-cwalR9Xy3iDLwZdEQ2hX5u_Q5uMygmn4ayUX9DxDyN04S8ZCACN--DksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر رسميا تم تغير اسم بحرية أونتاريو الى بحرية اميركا.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88655" target="_blank">📅 00:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88654">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
رئيس لجنة الأمن القومي في البرلمان الايراني عزیزی:
لا توجد أي سفينة تعبر مضيق هرمز دون إذن القوات المسلحة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88654" target="_blank">📅 00:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88653">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏
رويترز
: زلزال بقوة 6.2 درجة شرق خليج عدن.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88653" target="_blank">📅 00:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88652">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745cf92c81.mp4?token=L9OBVhqHv9MNv71IZr0G8M5W-ynSgP2_M0j0TyBIC9muJHwW9fNA6AxiAfIBm3oCrbgX3LuJS-TFe2VZIOVLG8QNAm1NP20GiOxVB1eL_zfnP4WYxKrOOzlsJw99LqC6qqMPSG1ofOd3OKyRhRorZhE0mrYP1kLGwDhf5k3Rhz3A8R8B4zr3OUFzzgDjHMDSb5ko-WZi6E28Ed2Qbjme_2qk7uT-znlF45FkZy13vmfW_8ezKiQC5chDfvh9dfYgCGeZSzTVgbMJ8im9-dlo35NKGfw5Czr0JAaFmy9LQz4CY_17L-5sKWLgRSaYElbriJS8htE_VDOEjaQDF6uQKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745cf92c81.mp4?token=L9OBVhqHv9MNv71IZr0G8M5W-ynSgP2_M0j0TyBIC9muJHwW9fNA6AxiAfIBm3oCrbgX3LuJS-TFe2VZIOVLG8QNAm1NP20GiOxVB1eL_zfnP4WYxKrOOzlsJw99LqC6qqMPSG1ofOd3OKyRhRorZhE0mrYP1kLGwDhf5k3Rhz3A8R8B4zr3OUFzzgDjHMDSb5ko-WZi6E28Ed2Qbjme_2qk7uT-znlF45FkZy13vmfW_8ezKiQC5chDfvh9dfYgCGeZSzTVgbMJ8im9-dlo35NKGfw5Czr0JAaFmy9LQz4CY_17L-5sKWLgRSaYElbriJS8htE_VDOEjaQDF6uQKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اشتباكات عنيفة جراء نزاع عشائري في قضاء الجبايش بمحافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88652" target="_blank">📅 00:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88651">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجارات عنيفة تهز دمشق</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88651" target="_blank">📅 00:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88650">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏
🇬🇧
أفادت التقارير بأن فرقاطة تابعة للبحرية الملكية ستوفر الدفاع الجوي لقمة الاتحاد الأوروبي المقبلة في دبلن بناءً على طلب جمهورية أيرلندا.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88650" target="_blank">📅 00:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88649">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
هيأة الإعلام والاتصالات تتخذ إجراءات بحق قناتي (أي نيوز) و(الرشيد) بسبب مخالفات لقواعد البث الإعلامي شملت توجيه تحذيرات وإلزام قناة الرشيد بإزالة المخالفة وتقديم اعتذار رسمي فيما قررت منع ظهور السيد عماد باجلان إعلامياً لمدة 15 يوماً.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88649" target="_blank">📅 22:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88648">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
إدارة ترمب أبلغت الوسطاء مرارا أنها لا  ترغب في العودة لبنود مذكرة التفاهم مع إيران.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88648" target="_blank">📅 22:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88647">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇶
مستشار رئيس الوزراء للشؤون المالية
: 40 مليون مواطن مستفيدون من رواتب الدولة، فاتورة الرواتب تصل إلى 7.7 ترليونات دينار عراقي شهرياً وتأمينها مسألة إلزامية، سعر برميل النفط في الموازنة سيكون ما بين 50-60 دولاراً، لا توجد أية علاقات مصرفية بين العراق وإيران ولا توجد أية عمليات دفع بالدولار منذ 2011، حجم الغاز الإيراني المستورد حالياً يصل إلى 18 مليون م3 تدعم الشبكة بـ4500 ميغاواط، لا توجد أية تعاملات بالدفع الإلكتروني مع الجانب الإيراني.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/88647" target="_blank">📅 21:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88646">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtqmlUVJ9tNdZkTpY-2kL_POF5bDfft7o9dVftwuK3NOE3R7_Nw4g3wBnsVG836XXV_UmIx-y9bJbTr0uMo8Ae4UPhNrLexRhuepuCeyLNX4IXrJMGE1GIiGcR60eE7yeb2IZkvrbxGbaKLe78FKIcFi5t1DchDh0EBtChrjjbkJMmg1f3y71bGIcrFfVvEHy7CnzSWlqQe5ztsHpNYQ0Ia5olzGrnSHbraxepDmjffFU9WLajZLUZqsDVwa1ELLiFKUAZXJagHQccocdieVaT0pSI1F9N3X-MSurK91A3LBYLyB004P6yJyWPn9ePngbbIceCIub4w295J-Pz5q0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏ناقلة غاز البترول المسال الأخرى، "سيجيت" الخاضعة للعقوبات الأمريكية، تعبر مضيق هرمز عبر الممر الذي حددته إيران.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88646" target="_blank">📅 21:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88645">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2e6046c.mp4?token=Tzd-n9YfJBr6eIvJsxS3Hd51p57vkhCZV1d32a45ScX_5RMp8JNrZRxukWPnYCCCkBN01EBeRfVWUyWr9zf3IpdW8y7-K5e2lofwdtYEuVO9j-7Me-4DhIw1BWH4lu_Ofutd_RaisK27E1zsJpsVCj80Pp5BGtGIeB1xza1ZPwMwwb5qObWhUNg7cBQlm3--12Z5sFZi_pCufm1h-7Mz2UCSe_MJKFPVC_jdwSX_s4EVCC3ggjQR9hQu4sWMQ3t0dNwYteouNNrh0USJBl4H8xLXCWuS6at5__VW4ExTYHhyxUC1zljALrQ72-pWIFSgJllfpz296LkzW9xZVdu25w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2e6046c.mp4?token=Tzd-n9YfJBr6eIvJsxS3Hd51p57vkhCZV1d32a45ScX_5RMp8JNrZRxukWPnYCCCkBN01EBeRfVWUyWr9zf3IpdW8y7-K5e2lofwdtYEuVO9j-7Me-4DhIw1BWH4lu_Ofutd_RaisK27E1zsJpsVCj80Pp5BGtGIeB1xza1ZPwMwwb5qObWhUNg7cBQlm3--12Z5sFZi_pCufm1h-7Mz2UCSe_MJKFPVC_jdwSX_s4EVCC3ggjQR9hQu4sWMQ3t0dNwYteouNNrh0USJBl4H8xLXCWuS6at5__VW4ExTYHhyxUC1zljALrQ72-pWIFSgJllfpz296LkzW9xZVdu25w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
إعلام أمريكي : ‏أفاد مسؤولون أمريكيون أن مدير وكالة الاستخبارات المركزية الأمريكية، جون راتكليف، توجه إلى موسكو، روسيا، في زيارة غير معلنة يوم الثلاثاء، وهي أول زيارة رسمية له إلى العاصمة الروسية. وقد أمضى راتكليف نحو أربع ساعات في موسكو قبل مغادرته.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88645" target="_blank">📅 21:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88644">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/497a3df8c4.mp4?token=GFlyqrkDsOF7Lx6piBSdpss_NaT9Yhvpzj9g0J8-87Ou0Zv4WWaifSzVpc2-1RQ16okp2g7k21Zo891cWccF5VYSkCPC2rUsidxzMInAt9LFTDW6mFfrW4rMl1i3L8GSwYs6pdi5O19Kd6lHxPOtOXE04jB8jkSTxgqeSWmvrndqCYSBAp2dyNB74Ps7vhrxkTRDMEqokaulD4ZXHnw4pjzPWSUWv2kKxZR4x8Gi1ucNQyp2IW5H-SJG6dJCEfUWh4kJqJoZBZgQrZc4zQ04Y6zWQ3IzNB0bx0iJoVwtkoECpLAHlo7SktWgtPotIACFp-bxLbeAV_OKs7A9fF5fEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/497a3df8c4.mp4?token=GFlyqrkDsOF7Lx6piBSdpss_NaT9Yhvpzj9g0J8-87Ou0Zv4WWaifSzVpc2-1RQ16okp2g7k21Zo891cWccF5VYSkCPC2rUsidxzMInAt9LFTDW6mFfrW4rMl1i3L8GSwYs6pdi5O19Kd6lHxPOtOXE04jB8jkSTxgqeSWmvrndqCYSBAp2dyNB74Ps7vhrxkTRDMEqokaulD4ZXHnw4pjzPWSUWv2kKxZR4x8Gi1ucNQyp2IW5H-SJG6dJCEfUWh4kJqJoZBZgQrZc4zQ04Y6zWQ3IzNB0bx0iJoVwtkoECpLAHlo7SktWgtPotIACFp-bxLbeAV_OKs7A9fF5fEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: بوتين لن يهاجم أراضي الناتو، لقد تصرفت روسيا بشكل جيد للغاية فيما يتعلق بمضيق هرمز.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88644" target="_blank">📅 21:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88643">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15ae436795.mp4?token=D1EbdnBnSH807fs2tBoE1F1j7oSx2a4Jf3GsjTfBy9xmuPx6sfl-ciTmHptQ-Jo707Ya9BNkXV7mBX0GeOnUuLD1-g6b0N9f0wp4Qqx1VfsS0x9InrroDdeccBzgGDP8g-NGB-zlCsFp2Zrj4zmmSgP_e12j_l3V5G6Zt7ho1KkQ0OqJj7EiraAipetxgGEz6fKi6xkYvXjCb2nsrKEa6ZUfmd1Z9kDnLzMRBm4Vx2D6k-kW7q0USdl5zlP9OPWAnACNFIlLQOk5_2fKZYP7KPMdNcaAo-whedNcpK6PrHS9_vvno_z-qnZR7YqRptlrzlPlrCTOYPxkX9ehLAmPjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15ae436795.mp4?token=D1EbdnBnSH807fs2tBoE1F1j7oSx2a4Jf3GsjTfBy9xmuPx6sfl-ciTmHptQ-Jo707Ya9BNkXV7mBX0GeOnUuLD1-g6b0N9f0wp4Qqx1VfsS0x9InrroDdeccBzgGDP8g-NGB-zlCsFp2Zrj4zmmSgP_e12j_l3V5G6Zt7ho1KkQ0OqJj7EiraAipetxgGEz6fKi6xkYvXjCb2nsrKEa6ZUfmd1Z9kDnLzMRBm4Vx2D6k-kW7q0USdl5zlP9OPWAnACNFIlLQOk5_2fKZYP7KPMdNcaAo-whedNcpK6PrHS9_vvno_z-qnZR7YqRptlrzlPlrCTOYPxkX9ehLAmPjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: بوتين لن يهاجم أراضي الناتو، لقد تصرفت روسيا بشكل جيد للغاية فيما يتعلق بمضيق هرمز.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88643" target="_blank">📅 21:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88642">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db380e2cda.mp4?token=Iy_yoFmKccRkg8N_enff3nsG5_4rU762sZnFbXLBLbORTfqgc1dgCmaLToitm9F_lAlvvAW_Ix3hMkJjEExTZZwRiXGKYApTkzokW9HpN_roCGA4jhai-AKaWSBGcs004KYnRwq8b-HZ6IN7rP_TSVH727w9cI2ko_RzeG6cNdOJH4_vrDYblKVJL9wHcZj1Ax_aYAgP1NyMgXS9Wqn1xE1Sd-GKaBVDXFTCl3-z9v7vxJmJ56kWNNIM1bcWq4vGIAlF7udcr2mpzzdMEdZK05x1m8iUAeXI5cAiGyCPIRdujug6-O8lLqrga6lIVXgHK1FHC3x0Lbj0yFG5aZupkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db380e2cda.mp4?token=Iy_yoFmKccRkg8N_enff3nsG5_4rU762sZnFbXLBLbORTfqgc1dgCmaLToitm9F_lAlvvAW_Ix3hMkJjEExTZZwRiXGKYApTkzokW9HpN_roCGA4jhai-AKaWSBGcs004KYnRwq8b-HZ6IN7rP_TSVH727w9cI2ko_RzeG6cNdOJH4_vrDYblKVJL9wHcZj1Ax_aYAgP1NyMgXS9Wqn1xE1Sd-GKaBVDXFTCl3-z9v7vxJmJ56kWNNIM1bcWq4vGIAlF7udcr2mpzzdMEdZK05x1m8iUAeXI5cAiGyCPIRdujug6-O8lLqrga6lIVXgHK1FHC3x0Lbj0yFG5aZupkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي عن ترامب: غير قلق على الإطلاق" بشأن احتمال قيام روسيا بمهاجمة حلف شمال الأطلسي (الناتو).</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88642" target="_blank">📅 21:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88641">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c2bbd3a1.mp4?token=l1JZu6foWaQNLWxkSymL_IpWaV1Dcs09HpcqBMZaCpJz0oVMQ9kXwAxgXZLdQ58suZU8YYWUX7lwkFGeKxiBtpVnu1jPdSSRlb8jW0P74JhKhfubn-2BtjR6Q3kM9fsij5mXDg-lf7jOplDMxurjWzGhjAgfueURw4h6E1zpVbN2wfJHGih9JSrJWlBwP-_eZcCeiota_2h_E1-eUh6SZCxpalOlg6CB5Ed2D4wdxAoRvWEULVgZ9LGse_KajDv_wH9jyOhC9FuJBmvXaFLzYk_8If-pDNWpefVlnP4KEbn-sfQOVf3iL2WfRcsqu8vhfJWZuKpa57OrjyyawmIRQhuPh6_m1I_48k6gNCNWIMwdmruBqK7D7zgyx35pqos4fzs_fZAkr4nfYE_xeK08dUzK59gnaQgucSx9Dj4CxZYvpefE_vYlDuuOui7-_tqHpIDVY_Fd2BeHvYfSAWNr2K7ZLqfVD3LqtDUBPimg9tH2xTx2s3Kz9JAQjQVEDHVZJ_ihCAxZ9_W6zxbhc1MZ7zGWPaFQiKz8winzMx7BRgBEMZ2uP59J-B1Ez3hAQWil4envMO5thzTt4FVlR80epLMjipJQ3KKDi7fgF2tEpTWDrrwLduqHijyzyMhgXT-TXFzOfHw92ko2fooSs19gIXCQ3gj42dEaFJzJFKiC8jM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c2bbd3a1.mp4?token=l1JZu6foWaQNLWxkSymL_IpWaV1Dcs09HpcqBMZaCpJz0oVMQ9kXwAxgXZLdQ58suZU8YYWUX7lwkFGeKxiBtpVnu1jPdSSRlb8jW0P74JhKhfubn-2BtjR6Q3kM9fsij5mXDg-lf7jOplDMxurjWzGhjAgfueURw4h6E1zpVbN2wfJHGih9JSrJWlBwP-_eZcCeiota_2h_E1-eUh6SZCxpalOlg6CB5Ed2D4wdxAoRvWEULVgZ9LGse_KajDv_wH9jyOhC9FuJBmvXaFLzYk_8If-pDNWpefVlnP4KEbn-sfQOVf3iL2WfRcsqu8vhfJWZuKpa57OrjyyawmIRQhuPh6_m1I_48k6gNCNWIMwdmruBqK7D7zgyx35pqos4fzs_fZAkr4nfYE_xeK08dUzK59gnaQgucSx9Dj4CxZYvpefE_vYlDuuOui7-_tqHpIDVY_Fd2BeHvYfSAWNr2K7ZLqfVD3LqtDUBPimg9tH2xTx2s3Kz9JAQjQVEDHVZJ_ihCAxZ9_W6zxbhc1MZ7zGWPaFQiKz8winzMx7BRgBEMZ2uP59J-B1Ez3hAQWil4envMO5thzTt4FVlR80epLMjipJQ3KKDi7fgF2tEpTWDrrwLduqHijyzyMhgXT-TXFzOfHw92ko2fooSs19gIXCQ3gj42dEaFJzJFKiC8jM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب يعثر على موضوع غير تدمير القوة البحرية والجوية والبرية الايرانية...
وقع  ترامب أمرًا تنفيذيًا "يغير" اسم بحيرة أونتاريو الكندية إلى "بحيرة أمريكا".</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88641" target="_blank">📅 20:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88640">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي عن ترامب:
غير قلق على الإطلاق" بشأن احتمال قيام روسيا بمهاجمة حلف شمال الأطلسي (الناتو).</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88640" target="_blank">📅 20:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88639">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPkuQxFbMPYnwcj4DlUpr7KIcQUvWM1DjL4-2ZsTL1EMJYQpJy5DpA6RF4v7nZMazGzUvYyiO4XXVrUckyfsvqbdOzJZuMGyIXqadyQu-yMnQuS9-SPQuKT1qqtipsMt1SM68pP1i-WworsUkvElHJxJCjXk9Oe8rIrAeYgcruTE95MsFxnnFTkoR-V8yXjAMOuIM4K7LtnepAEvzfERqhP_-uzMv2CnlG5T9GvHKYL3Fu5YlbgtWekZ3jXMj2CTs9qAoLvStkUkBgFIJTPj8GUjR0ZvqDQPuT_5HHXE3BywvwVwNar9H6XRHek204Y89lbNZR49rHp_P34pwlolBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف
بدلاً من ضخ مليارات الدولارات إلى وكيلها الإرهابي، إسرائيل، و750 قاعدة عسكرية، كان بإمكان هذه الإمبراطورية الفاشلة إنفاق تلك الأموال على شعبها، لكن لا، سيكون ذلك منطقياً للغاية بالنسبة لهذا النظام.
‏يا سكوتي، يا رجل، مصداقيتك على المحك. افعل شيئاً.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88639" target="_blank">📅 20:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88638">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
أمين مجلس الأمن القومي الإيراني رضائي:
إذا بدأت أمريكا أي عمل ضدنا فستحل كارثة على مصالحها العسكرية والاقتصادية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88638" target="_blank">📅 20:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88637">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da9299db7.mp4?token=pAEV-iWmv5-lQgo1YkcslyYPKxkLJL1_VyPHOlfrA7QqIJsPux7R2X6JilCzgFCIfS2gjz9XTJ_0dISbWzWG_vapinpqnGIKK7syCKEoadHtb_yeUCyYIaCoIPBIaeH0QRGZWPg_Lj0ZrIhquC0bx5ieTwMyHvUTkksqZZJo9S2LzYhCLuXu_bfIpZg2G9RllC2fNk_h4eYp03B9R78mxCa2OGfqb0kH3XKUA7txV-nNxcRbjqTzhiERz7MCZNmFqIQQ-DFdGRGh1CJd-6PVDZ7ds95XHMPmG8LMHphO4H11g2zDVFIvPK--uN3PQZaI0IXaPGs6wFpJwLFFCgoSbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da9299db7.mp4?token=pAEV-iWmv5-lQgo1YkcslyYPKxkLJL1_VyPHOlfrA7QqIJsPux7R2X6JilCzgFCIfS2gjz9XTJ_0dISbWzWG_vapinpqnGIKK7syCKEoadHtb_yeUCyYIaCoIPBIaeH0QRGZWPg_Lj0ZrIhquC0bx5ieTwMyHvUTkksqZZJo9S2LzYhCLuXu_bfIpZg2G9RllC2fNk_h4eYp03B9R78mxCa2OGfqb0kH3XKUA7txV-nNxcRbjqTzhiERz7MCZNmFqIQQ-DFdGRGh1CJd-6PVDZ7ds95XHMPmG8LMHphO4H11g2zDVFIvPK--uN3PQZaI0IXaPGs6wFpJwLFFCgoSbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد محزنة لواقع الشعب الكوردي في شمال العراق؛
مواطن يمسح شعاراً سياسياً كورديّاً عن سيارته أثناء محاولته تعبئة البنزين في إحدى محطات محافظة كركوك، بعد مطالبة المصطفين معه بذلك، ليستجيب ويمسحه دون تردد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88637" target="_blank">📅 19:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88636">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇾🇪
🇾🇪
الجيش اليمني يشن هجوما على جزر بالبحر الأحمر بالصواريخ الباليستية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88636" target="_blank">📅 16:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88635">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
وزير النفط الإيراني:
حوالي 40٪ من القدرة الإنتاجية المتضررة في حقل "جنوب بارس" للغاز قد عادت إلى العمل.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88635" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88634">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇸
‏
البيت الأبيض:
لا توجد مفاوضات جارية حاليا مع إيران.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88634" target="_blank">📅 16:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88633">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇶🇦
🇮🇷
وزير الخارجية الايراني عباس عراقجي يستقبل رئيس الوزراء القطري وزير الخارجية في العاصمة طهران.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88633" target="_blank">📅 15:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88632">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a52181c7e.mp4?token=BxkSrDHvD8lxaeYO52PAJ858qIaZAfoVKqN7UR9N_F2BnKnMM3iimt4FoWyXTLgIJmT27lEpqjVd3C13JhCJrkaYal626kloehZi2UJ88j6rcYkRxZKgREJ4xZn0mrjnXUrW1AC_4vZW3AHsktc7oLa_9cEFruOxc_LgQ7cM8VoviqsWA8OLPx0v-r8IF34ciamdhmDIfLgvooMAAmpu8YIYT6Vlc_Ok5qLDhzl_BYrbx6o5JsBDPFfb2VHJobkhdLfZhXJQr0paogt_wp3KNRYXy5nan3e3sEAVf0UWN0299Z77y8VadAA1OPioqEXY817jjxC8n8Wamo2Wkythwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a52181c7e.mp4?token=BxkSrDHvD8lxaeYO52PAJ858qIaZAfoVKqN7UR9N_F2BnKnMM3iimt4FoWyXTLgIJmT27lEpqjVd3C13JhCJrkaYal626kloehZi2UJ88j6rcYkRxZKgREJ4xZn0mrjnXUrW1AC_4vZW3AHsktc7oLa_9cEFruOxc_LgQ7cM8VoviqsWA8OLPx0v-r8IF34ciamdhmDIfLgvooMAAmpu8YIYT6Vlc_Ok5qLDhzl_BYrbx6o5JsBDPFfb2VHJobkhdLfZhXJQr0paogt_wp3KNRYXy5nan3e3sEAVf0UWN0299Z77y8VadAA1OPioqEXY817jjxC8n8Wamo2Wkythwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
صور الأقمار الصناعي تظهر أن هجمات انصار الله استهدفت قاعدة عسكرية تابعة لمرتزقة السعودية في الوديعة على بعد حوالي 23 كم من الحدود السعودية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88632" target="_blank">📅 14:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88631">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ذا أتلانتيك:
يحاول البيت الأبيض إبعاد الحرب الإيرانية عن عناوين الأخبار قبل انتخابات التجديد النصفي. مع استمرار الصراع، وارتفاع أسعار الغاز، وقلق الجمهوريين من خسارة الكونغرس، يتجه ترامب نحو فرض العقوبات والضغوط الاقتصادية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88631" target="_blank">📅 14:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88630">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
المعارضة الايرانية الكردية المسلحة الأرهابية
: الحكومة الإيرانية تواجه عقوبات اقتصادية قاسية.. لن يقتصر دورنا في هذه المرحلة على دور المراقب وسيتم اتخاذ خطوات عسكرية وأمنية وتنظيمية ودبلوماسية. استعدوا ميدانيا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88630" target="_blank">📅 14:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88629">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47828875e.mp4?token=ehNsdcbUZblyMDoONNuqSfzFqA6a5zoCXthRLcBaCBAf-iDuB5nvoysCpGNmLqeMouFb7A288dY8KYfGO7urs2B3zRdbDHFs6YkHj-m7kvwC8yWo8EY7weG_syVMntcrr1gtiCCGB2GzVU86fV0wk8jIX-VgKCz5EPi05TyPDNpSiONj0iEdomqD_7_1N3SmklEzHkrM_ckkH2ufG5TW_ncHOcER0g0e99_XbWKAYKUxFPcsmT8Ysr8QJUkmC3VOYj_5pbrMztydz-KqSoNVE6WVYz_pFfA_uSYnlIYOpUhEPX9_jZMASGnpbidyr-PAKZRizbE5z-lA7-d6aMGE4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47828875e.mp4?token=ehNsdcbUZblyMDoONNuqSfzFqA6a5zoCXthRLcBaCBAf-iDuB5nvoysCpGNmLqeMouFb7A288dY8KYfGO7urs2B3zRdbDHFs6YkHj-m7kvwC8yWo8EY7weG_syVMntcrr1gtiCCGB2GzVU86fV0wk8jIX-VgKCz5EPi05TyPDNpSiONj0iEdomqD_7_1N3SmklEzHkrM_ckkH2ufG5TW_ncHOcER0g0e99_XbWKAYKUxFPcsmT8Ysr8QJUkmC3VOYj_5pbrMztydz-KqSoNVE6WVYz_pFfA_uSYnlIYOpUhEPX9_jZMASGnpbidyr-PAKZRizbE5z-lA7-d6aMGE4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
🇮🇷
وزير الخارجية الايراني عباس عراقجي يستقبل رئيس الوزراء القطري وزير الخارجية في العاصمة طهران.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88629" target="_blank">📅 14:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88628">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4981ae7d7.mp4?token=seG4dNGCBJ0mOsGIihYBiE41erHhYuMezIxQlpU4PIQ1yq3V8v-RWnw49Poq0jolsA1_rjLtipAXngHgtXFvzcwrtHkUMVYIphth56cuyW-A3oZ1-dPwZZxTdqY9R_J6vyBZCUvuBn3turK2KUcF7Bg4VAN3rJT7AKltNocpjQINZvPq0Ve_SbJ3EM0tyUUvwnGmGnd7rI72NzAsprccsXqlvciwYQ3r1Hlqm-LPlKYTXiKgwHi_-sdj363xipkKLdncdShRjF2qJokxkN3F6z2qY0aNDato5hm-kCknPhxvtjuD0kgxal3URfKS3w4oUjbAS_t5jfVwa_0aRPvFOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4981ae7d7.mp4?token=seG4dNGCBJ0mOsGIihYBiE41erHhYuMezIxQlpU4PIQ1yq3V8v-RWnw49Poq0jolsA1_rjLtipAXngHgtXFvzcwrtHkUMVYIphth56cuyW-A3oZ1-dPwZZxTdqY9R_J6vyBZCUvuBn3turK2KUcF7Bg4VAN3rJT7AKltNocpjQINZvPq0Ve_SbJ3EM0tyUUvwnGmGnd7rI72NzAsprccsXqlvciwYQ3r1Hlqm-LPlKYTXiKgwHi_-sdj363xipkKLdncdShRjF2qJokxkN3F6z2qY0aNDato5hm-kCknPhxvtjuD0kgxal3URfKS3w4oUjbAS_t5jfVwa_0aRPvFOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قوات أمنية كبيرة تتوجه نحو منطقة الدورة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88628" target="_blank">📅 13:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88623">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-AIwpgHmICYeHVq1m0swgd4FhXWK7ra2ObdRgD0owmjsxIolWQtwwlqq4SVHAtJl-vhEew5CrIlerjtVOlyJimp4pCSYvbdXN1-2Fv7UDpD9hyRi9D28iJ3KMOVviUGJ10piT-BYZJ5AcGVjnVOC2bKT-wrAU_h1ODb9ArgSVqUWcP4tsHznU-mTFA5m-CzMAQvoXfr_89PhEQUHm9Jyimyetu7k9XEBD37mL3-V5g9MMZ4EnvE55-PRl93d8YxT5Rp7L0aVKb_aGAEIaLUloWQ1TWPLUwNi34K82VFlER4zDs7D4gbeYa8Ufvw3czL06jlxmfiobBp99AeMmRCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WA_6OLgmelZAlKFr4tDgwA4eclz3YqnxSlSHsK2SjT2MCSSZcUR0bspl9PWfA9H3MNw1QbySpwXkiXuhz7kyfk9mQZCuXdj8jbfNlFNeCjYtBXifdfdCr4AgRmbt8VVTb5HcEcr2F8LsOUSkBM7uLmBEdIBYegrycNbmrNYEcEADuF0icB5my9aB5x4Nhaw1v89usQHlkm46CtIe12sAsZiMJk4NWpb51cOnnlh25V4KMlvdk6t5hLR5WJ0Mlg_NSIO3_MCRCyoOT_llEJSkC26fa74yySnXbUSqlCnJOhuzFVn2fdDUqnA_qnufJXZTZPVb9c8MeSfjHZJYRcAVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AIO7ND9o7RiuS601ya0MUvBcU9k1gE4vFaE1XZKUPnebncSqoArspnil5H34cz-KFsavv5-uESqE3u-sFNebyI2MHySGoSW-nGUJ1-ieXti4X_zWXQ4kQ9EgmI9qoZFZ65RUmsTcutyLbXWUFaNszqoY983q4xTCSyDMzYrve4szUnB_lxwBQH1ovU2kFoFoqwqh7nq8zoRCAuFXGd6mVGo1dQra_nKzup9RwEyZh7xOTXQQma_qwVErI2AJb5YTcNKK3_EE7QTMnxAuTO5OsM5AeHiMudC38i5a0THb_HQMy3tcTjaHafnqBqrH6u5HqxscF89DxfFQVnLfpTzglQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmv8b2kjj3KVYtorpGcmwMEcZhH3hA4PEt1mROLEt6mBQTs5eMabn0Onnc03jjP7NzV6nBXvDRiPWTC_somrfSx1JV7JBMO3OzQCnolHIk3xAE9bhkSvgWzt6xW5iprPUlbCyFvalkvLAZkk9SC1UblEArr2z1S4eiGFudzsuIuywfhf__NGMb4iHx3I_sx2dnQdQWMWJetKlUtClBgA_aVvUzbOdnuvl7FTerH2-OUmYfg9pCUfpE27vnxb8fBoYE9guz6ls3G4qBzcpIsz5UGJ2IT2hqGVRyrTHeMuhKiAJXjJmIvWJG5V6v9umYaNwEmHVxjcxQpmYaB10vNvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p2DKlH_YbkT7-u6xeGhjHu74UzrApkjLOu64oqMq8iMUCoDMzHHLBEDhYtTvkbR6VGAoIPrOb5m74_s0OqQnaXvAhQG0LYb3l72btTPY998b_11_b4odeGLlJTXQhOur02J5QxOA24jyCcBS39L1hrhPxg_aLe7jrkTyYmf6V-ubHth258Nvf-CfJNmClQnYlBsU_F0E-IyG2oxV8xogU_G5_ipTc4THAMWiOr7SBOnIkkY427EdeDarEGVafwIpxaLlwXb0A0tjxvRkN3gf9ipzrz0QeKkkjHYocVnSJLqwoBvz5h54kSFw26yx9Nubz0UTOGwpCp8qHBZXsy5l-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88623" target="_blank">📅 12:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88622">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:  استشهاد ضابط برتبة عميد وأحد منتسبي شرطة بغداد الكرخ وإصابة أربعة منتسبين آخرين من الشرطة الاتحادية ومغاوير شرطة بغداد الكرخ أثناء أدائهم واجبهم ضمن حملة إزالة التجاوزات في منطقة الدورة ببغداد.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88622" target="_blank">📅 12:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88621">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88621" target="_blank">📅 12:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88620">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea96c0728.mp4?token=HSoK230r_-wyXeIXJwv2tRg7LBiUHmgG7-n9R7OePgSYGWa41gkErKM-C_Q8gl95af9JWGIfSN3mH499QBkw6vLENY6_cR-DVnfkKgupfkMlheRQ-0VrGVTacgs9__3r1i23V43C4ZGxdOth3V_QX53t1-McyescAvGyw61c5pSDm3Bmuch-a4gNtmwGK8Qhhap4QnZfuwTH5-wCZdemXLIsbUkH0U8Uz7Dn6l4AnSU-WF_frsAV0wg4y8Dh_QMxxe_Jgc1ZOVmvS9eZL5y0-06r5uUucS1NOLsaLZYT2UlIpBgRJUUx8GQPIXr3pNRhjiB-qt_jT7A98ESx86wxMasAXEt8OqDBISJ3UI8s1R1RgAorBRS4PKl5ihRapT1ONMMGqXbyaAr6pdJK_guj-wNxwh53Os3aodIKcJhAmVFNipOoZ9MwarAXVxV2dj6u83Fg9qLSd3qbV_S8kH2fBXFzRJxhqTokZ9wped5Q77TrGmsJ9eDm1KCNc6qCHyZz5j5zkIr-tTa10SovSEF8HnYOE8GQChbm55IA3EN1m9FP_qM0_k9sZCFL012Whn9K91ZSuns6y1m0oubFarHGcSe_niTCxyv78h6uRJ3oPL4n4I-VJuUub9-ZzP-jMHeRRM8OUvfNCMhQ1kFU5kSdAEN719vO2b-Uok2iNgIwS9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea96c0728.mp4?token=HSoK230r_-wyXeIXJwv2tRg7LBiUHmgG7-n9R7OePgSYGWa41gkErKM-C_Q8gl95af9JWGIfSN3mH499QBkw6vLENY6_cR-DVnfkKgupfkMlheRQ-0VrGVTacgs9__3r1i23V43C4ZGxdOth3V_QX53t1-McyescAvGyw61c5pSDm3Bmuch-a4gNtmwGK8Qhhap4QnZfuwTH5-wCZdemXLIsbUkH0U8Uz7Dn6l4AnSU-WF_frsAV0wg4y8Dh_QMxxe_Jgc1ZOVmvS9eZL5y0-06r5uUucS1NOLsaLZYT2UlIpBgRJUUx8GQPIXr3pNRhjiB-qt_jT7A98ESx86wxMasAXEt8OqDBISJ3UI8s1R1RgAorBRS4PKl5ihRapT1ONMMGqXbyaAr6pdJK_guj-wNxwh53Os3aodIKcJhAmVFNipOoZ9MwarAXVxV2dj6u83Fg9qLSd3qbV_S8kH2fBXFzRJxhqTokZ9wped5Q77TrGmsJ9eDm1KCNc6qCHyZz5j5zkIr-tTa10SovSEF8HnYOE8GQChbm55IA3EN1m9FP_qM0_k9sZCFL012Whn9K91ZSuns6y1m0oubFarHGcSe_niTCxyv78h6uRJ3oPL4n4I-VJuUub9-ZzP-jMHeRRM8OUvfNCMhQ1kFU5kSdAEN719vO2b-Uok2iNgIwS9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88620" target="_blank">📅 12:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88619">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djE459D08wFiVhAW79bFNTHPro1F07cu-zIda56NCI-dQJGQDGDu5gZfhRq6V68q0hRpQtpBBU72D3Gpu3U6kiK8h9XRHu7WcUFyh0k_N520KgWOvFvLhAz6qy0fXl9M71z1CpPft6nNITLO84PLfAgwa7NYZlhNFZxpHM2xZWX_RQz_qOb3eLEce6FMShJHnCNy-qeJSM5HYIihQF8xUu6RWBKmdFY--XPswY1vUEcvFS0nZPVdCItnCljTOQ7L_8AXjomb7UnXUqfhxd2CukupAtlWym1uJe0GH6fXG8vPWTdG8Uz2A0KNl_BByJrHCeixjV7jcoGKXZGKG7nEwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88619" target="_blank">📅 12:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88618">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇷🇺
الخارجية الروسية:
قد تتضمن ردود روسيا على الهجمات الأوكرانية باستخدام الأسلحة البريطانية استهداف المنشآت العسكرية البريطانية - سواء داخل أوكرانيا أو خارج حدودها.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88618" target="_blank">📅 12:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88617">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
تحديات عديدة تواجهنا. نحن نطور إجراءات القتال في جميع الجبهات، من إيران إلى لبنان وحتى غزة، ونحن في حالة تأهب عالية في مواجهة التهديدات المتعددة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88617" target="_blank">📅 12:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88616">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73ea710ed1.mp4?token=tIyZBRJSfiFdELsG4chd4mZbwD9QPLIvrpWfmHY_R6Cjf-KNfoVj_IlrYY2MrkBSN9jRYscIqusTqwg9UJjW9N0I63V6VCZx-GYFNe08Kr6AtL4Wlf9qZZR6iZ5pLPbC9p8OsVN3W-PmWMP2kHdtDopBmA8_pbVw9BideW8ATDm64DL9dDDOn_uzNEFA3QxH-B097n-5hOnpRP9drpvZHu2N-FguItXq0J0CRx1X4s21vNMdUtflx4c2ABPScPIjc7z_ALercdUGrssIVwHWDwSY0mCanVQfUlwFMCNYKir21ZhvNimxRbHFcQE-ni7LP-HWwgPrNPbDEy5W0aH_1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73ea710ed1.mp4?token=tIyZBRJSfiFdELsG4chd4mZbwD9QPLIvrpWfmHY_R6Cjf-KNfoVj_IlrYY2MrkBSN9jRYscIqusTqwg9UJjW9N0I63V6VCZx-GYFNe08Kr6AtL4Wlf9qZZR6iZ5pLPbC9p8OsVN3W-PmWMP2kHdtDopBmA8_pbVw9BideW8ATDm64DL9dDDOn_uzNEFA3QxH-B097n-5hOnpRP9drpvZHu2N-FguItXq0J0CRx1X4s21vNMdUtflx4c2ABPScPIjc7z_ALercdUGrssIVwHWDwSY0mCanVQfUlwFMCNYKir21ZhvNimxRbHFcQE-ni7LP-HWwgPrNPbDEy5W0aH_1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
هجمات روسية مستمرة بالطائرات الإنتحارية وإنفجارات كبيرة تهز مناطق في العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88616" target="_blank">📅 11:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88615">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية:
لا حقيقة لانسحاب قطعات الجيش من منطقة الدوز.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88615" target="_blank">📅 11:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88614">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الله اكبر   هجوم على سفينة قبالة سواحل عمان منطقة خصب بطائرة مسيرة …</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88614" target="_blank">📅 11:33 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
