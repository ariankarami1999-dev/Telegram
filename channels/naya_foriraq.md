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
<img src="https://cdn4.telesco.pe/file/MS3n1NHI-GyQR_WsTYIofikPRDEjahVNQL48pqvUZnZu25x7c7c__fzAPm9TNRLclQoyvHaejbTjMd_ZNfm8g4xnf3iiR-eckZm33Ig5rYZP0L2UVjw4BWBhNxUWD5vD135BpIfk5v8pzYNU8EZkp6gjzn9tJ5azYHNN5C84DiiKGvfM_TEI_mBFYoSCx2JRpM5nOhtpZJv8Fh_yVBLolIVqq2-cAMbee7uVlY2QaFMyMjornQ3Z2jPGWJC8K8NZryaJ9TkxWOK55B_DTUrQ8acK9ruQxvAiY5XNfBx2YYYkIiLjvGP2u9cjH_vWwk5iTrtDfQsVZd0Da8Jul86J5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 251K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 17:23:55</div>
<hr>

<div class="tg-post" id="msg-76367">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
‏
وزير الخارجية الإيراني عراقجي:
ناقشنا هرمز وإدارتها المستقبلية بما يتماشى مع مسؤولياتنا السيادية والقانون الدولي.</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/76367" target="_blank">📅 17:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76366">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfLvPNZDJvTyEhim-z_sEdhBFolLGLO8Awlmxkj_8bS3HV4o4aD5XiQ6QG7tBKhtuHQu13BgwNFmuRfINxxOGCH7DeGv61XZwS25SqRw3lXfMn_VIzdKPuLVf8194uA2vP3U4O2VlqoWt-LHK6kqBxLP0gmpiaNnyKrj-GluJStYpJrnIIOVt8i1e-ciWS0luiU_ccmzV60ZusW94N8Ogr9YfEJzaypV8AiUnFE5KNnPg0hxs6ErET2Uya5zeswaKMcr5sZKRx1XM0cPRvr6b_Jgt_uqHDAnFVmtjQu6HY3fETwrEqUPfaLLKtINT9Lgydo89kLbRDjuLYzFYM8LvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
حزب الله:
بعد قليل...</div>
<div class="tg-footer">👁️ 862 · <a href="https://t.me/naya_foriraq/76366" target="_blank">📅 17:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76365">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6933bc2db8.mp4?token=bNiy5f-9UdhAiQ6m8v_v0AgDMHptWfmRS3geLOPoi-YtShVvWZzK4wO_s1ZN_FYsXpwsQBWl__06oKhllS4u4S-jKVLDSWLUISUHskbb8yX7JJ5qvS04JF4COn1XrcmoXI_keuik-RDa_jTsmlT2lEfVyoGqr5w4Dg65UT2VWxp8GGZ3fRwjqakIpITuz7VL4pSlnBnsglOjrCd65Y2SwzlVC2LF7tbV83w_T54096w5bydeJrSPeN--eztXGc69Ck9zKxcsGKqiYBTEHKKSvYRyYt4F3PBMF0L67buMdGeeLliGAjZicAwUzI7u88lN8eKtDOo-5hYEHOUGic0LSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6933bc2db8.mp4?token=bNiy5f-9UdhAiQ6m8v_v0AgDMHptWfmRS3geLOPoi-YtShVvWZzK4wO_s1ZN_FYsXpwsQBWl__06oKhllS4u4S-jKVLDSWLUISUHskbb8yX7JJ5qvS04JF4COn1XrcmoXI_keuik-RDa_jTsmlT2lEfVyoGqr5w4Dg65UT2VWxp8GGZ3fRwjqakIpITuz7VL4pSlnBnsglOjrCd65Y2SwzlVC2LF7tbV83w_T54096w5bydeJrSPeN--eztXGc69Ck9zKxcsGKqiYBTEHKKSvYRyYt4F3PBMF0L67buMdGeeLliGAjZicAwUzI7u88lN8eKtDOo-5hYEHOUGic0LSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
طيران العدو الصهيوني يغير على بلدة البيسارية جنوب لبنان.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/naya_foriraq/76365" target="_blank">📅 16:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76364">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌟
‏
شركة شيفرون الاميركية:
لدينا 6 سفن في مضيق هرمز ولن ندفع رسوم عبور.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/naya_foriraq/76364" target="_blank">📅 16:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76363">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7bX3r-zeU6L1gvZAcNSaaGQ5Q3-jRAEps3g9R4te08XVtEBgFYHaPb55DAP7xdVZjuOyfQzcyweRfGrerWVXmJ3KLydqdW6AzaOKpNGNEd4quA1Iphls9ql9-IM1nYpDnGh8fSKeB87WHjdZHVQvD0NXDtsa9Sh4fZRE4XflVKsBUc4TTLywkad0C5hXE-JvQYVNRrar_Z8AMTiFRYcoDmnQ5pjfIfzJsV_m6A0CV5bBUMh_UQlzxWYUtAci04LLgpzvx4cxK1GAb1prrobHquFw_T_JTvedkZHDhHqYNxVOllavuVMo4VnOSOuIu4q4I68-etCvIuAI5HRg1m4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
دمیتري میدفيديف: التزموا الصمت. هذه مجرد البداية تستخدم الطائرات المسيرة الأوروبية، وقطع غيارها، وأسلحتها الأخرى، فضلاً عن المعلومات الاستخباراتية، في هجمات على روسيا يومياً. وتؤدي عملياتها إلى إلحاق أضرار بالمباني السكنية، ومقتل مدنيين.  جميع أنواع الحثالة،…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/naya_foriraq/76363" target="_blank">📅 16:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76362">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PL1ReQSaPBQJ3EJ2FCW7V6d7nEmif4qncf-tqGYfeoljV4m8IGIK0uz3FZhn86WF4oAxyGAOa0_RDIBzv7fRDtaoY9mssjmRbi4gscke1UTP5aBTQA9sG_WPuddSisZk74frgoRzSfA_13c-NoyrfVp9npRSAawuFUmuZ2wGUD1UMAPbsq-4E88uInnn0jnFzlrGQxqhMjABxSh4SIy0bMHXIs11YFDJ80aD6P71S2GEVo3x7UDCDOM9-tJ6wntfVwj6Hgzjqx8U853BySBbO79zgY5eK7rUxuHeDZUU6aOY6V03jSssiBu2kxZZfsRObhdTQDemOTDylQVknAlgMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
جيل بايدن تعترف الآن أخيرًا بأنها لم تكن تعلم ما الخطأ الذي حدث مع "سليبي جو" خلال مناظرتنا الرئاسية المذهلة ذات التقييم المرتفع لعام 2024، حيث لم يكن جو يقدم أداءً على أعلى مستوى من معايير المناظرة.
قالت إنها كانت تعتقد أنه كان يعاني من "سكتة دماغية"، وأشياء أخرى سيئة حقًا، ومع ذلك لم تهرع أبدًا إلى المسرح لمساعدة زوجها المضطرب، كما ستفعل أي زوجة جيدة. والشيء الوحيد الذي فشلت في ذكره هو مدى أدائي القوي قبل انهياره شبه التام.
بمعنى آخر، كما سأل الكثيرون، هل تسبب أدائي القوي في تلك المناظرة في أنه "اختنق" ببساطة، مما أدى إلى هزيمته المخزية، أم أن هناك أسبابًا أخرى؟ لا أحد غيري يعرف الإجابة على ذلك، لكنني أعرف ذلك!!!</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/naya_foriraq/76362" target="_blank">📅 16:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76361">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkKgxPJhfWUnjAJQqrKKIskLIHSP3GorDwkhfFOUiNUIbitBEHm3h8pT7ayfESKOOJ0KITpzjFoL7G4GPYFyWi60b4njQvT14HUMfINyXQKdyVUL_2VPn421haGCw-4UtUHEcEvU4NaMDq0qCv0mdDmGjb6aMdzbX2PVm-635zMVWpKtz5S0XvKNrH9jsBa-YixQa4LRZGyA_WRmNVixzZiBX4dV_IZsVtwNzOmnBaSKHNLm90friLws222hMLrho3i3Xz97XX8dW4qgjifA_4lJITnGFVaR0-e5jBEf0wiTrDdfuyH5e1AlFERl8WXinCjM8U628dxwF3tKHR4s-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف
:
- لا نحصل على تنازلات من خلال الحوار، بل من خلال الصواريخ. في المفاوضات، نكتفي بشرحها.
2- لا نثق بالضمانات والأقوال، فالمعيار الوحيد هو السلوك. ولن نتخذ أي إجراء قبل أن يتخذ الطرف الآخر إجراءً.
- الفائز في أي اتفاق هو من يكون أكثر استعداداً للحرب في اليوم التالي.</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/naya_foriraq/76361" target="_blank">📅 16:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76360">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bf1f46f4.mp4?token=AeTf4msicDi3oIHaW1Hq_S3q2mYnFYvGGbSZItdS4WNQKDQY9CKRhax19YxPoPxUyIA6y2SzQdWsJUjX7kuts5KtCiGFN4pwJvKwG5TftlzzDZVpeLRdu7tddnl-MjlarOccnH4Uur468j1WwqH4F0PePcOVaS1lsFMiwbUf4U3yZR258AvXmPG6uBVSVFVFCJjk3GX8a3Dk0V09Vu8hYxH69Pj8l0uu0F-lHNISwCUJuASgY7dXsfIX8oKu8SNSULiWtFVXSiXebn_28U8FUsBb1zzwlKCafb77DGNtR0CDv92WumQHyLaz9yWDvZ6a6jghQRD0oUGKMzVfcJ6mMlw5JMriVNt_y2DTQXWbFERKx0G7Ow5Pqy5Rqh-t-fq2WSy3fe6N8yZ0K6FJGow9RpVfeh77v4c1d7oQ0cNAl2uk1rBFQxQagPCywOezqaEndMDupwZsJS8LIEZvfyq9_hXtgWdiiQRGwNEgNO9xVB7U0SGmz0hoig-grm-L2lamOA6DAq3KQitxKY090AeRFMNix9-t13n3F3i7G1tlvb5w1lGUv1knqPg7xhht_fXrTmSbz65-TxfOQ-XmvDZXKMz4J4oHVqQD6ZDvLfvp-3udSBnFsFA6eycoMJi4SMdF0plH-f4mGMvQjxtuikAvtseQ6ow2IHR1_dcubm8bTTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bf1f46f4.mp4?token=AeTf4msicDi3oIHaW1Hq_S3q2mYnFYvGGbSZItdS4WNQKDQY9CKRhax19YxPoPxUyIA6y2SzQdWsJUjX7kuts5KtCiGFN4pwJvKwG5TftlzzDZVpeLRdu7tddnl-MjlarOccnH4Uur468j1WwqH4F0PePcOVaS1lsFMiwbUf4U3yZR258AvXmPG6uBVSVFVFCJjk3GX8a3Dk0V09Vu8hYxH69Pj8l0uu0F-lHNISwCUJuASgY7dXsfIX8oKu8SNSULiWtFVXSiXebn_28U8FUsBb1zzwlKCafb77DGNtR0CDv92WumQHyLaz9yWDvZ6a6jghQRD0oUGKMzVfcJ6mMlw5JMriVNt_y2DTQXWbFERKx0G7Ow5Pqy5Rqh-t-fq2WSy3fe6N8yZ0K6FJGow9RpVfeh77v4c1d7oQ0cNAl2uk1rBFQxQagPCywOezqaEndMDupwZsJS8LIEZvfyq9_hXtgWdiiQRGwNEgNO9xVB7U0SGmz0hoig-grm-L2lamOA6DAq3KQitxKY090AeRFMNix9-t13n3F3i7G1tlvb5w1lGUv1knqPg7xhht_fXrTmSbz65-TxfOQ-XmvDZXKMz4J4oHVqQD6ZDvLfvp-3udSBnFsFA6eycoMJi4SMdF0plH-f4mGMvQjxtuikAvtseQ6ow2IHR1_dcubm8bTTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 27-05-2026 تجمّعات لآليات وجنود جيش العدو الإسرائيلي في جنوب لبنان بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/naya_foriraq/76360" target="_blank">📅 16:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76359">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇷🇺
‏الخارجية الروسية: سنرد قريبا على قرار رومانيا إغلاق قنصليتنا.</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/naya_foriraq/76359" target="_blank">📅 15:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76358">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇷🇺
‏
الخارجية الروسية:
سنرد قريبا على قرار رومانيا إغلاق قنصليتنا.</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/naya_foriraq/76358" target="_blank">📅 15:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76356">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326e188e45.mp4?token=EJ5hwnCpJQGEFi298Bw7G5CF4eIodFuaxkH0rmwlMJaKes060Sel4MSou9qhqIaYBqAltS9nEdsStZESFp85bcSemuzJFYeR9oku8aXBHSwxzMrMuwACQ623KSj-8ubAHpZs0OfSFeIny6udnlYAn3JlBWd-ZhkfFuNN3WK9bDTELUVTC9LyJhUb3alnR2xdFXg-wGXdet2OwiSODt4y4twWH9iWJwuO-NVnSr4ZgSkldb6Gc3GRFdD2HiK2q1taAY6_oEn4ene-ptYgfyCUxbyZewKqLmTe-R1nxA8KOyKqFLLgpNnV6V8ma3Ld6nOFlBh3dvzKZJWGl0EzqLE0Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326e188e45.mp4?token=EJ5hwnCpJQGEFi298Bw7G5CF4eIodFuaxkH0rmwlMJaKes060Sel4MSou9qhqIaYBqAltS9nEdsStZESFp85bcSemuzJFYeR9oku8aXBHSwxzMrMuwACQ623KSj-8ubAHpZs0OfSFeIny6udnlYAn3JlBWd-ZhkfFuNN3WK9bDTELUVTC9LyJhUb3alnR2xdFXg-wGXdet2OwiSODt4y4twWH9iWJwuO-NVnSr4ZgSkldb6Gc3GRFdD2HiK2q1taAY6_oEn4ene-ptYgfyCUxbyZewKqLmTe-R1nxA8KOyKqFLLgpNnV6V8ma3Ld6nOFlBh3dvzKZJWGl0EzqLE0Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اعتراض طائرة مسيرة اميركية من قبل انصار الله في اليمن.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/76356" target="_blank">📅 14:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76355">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مضحك
‏
زيلينسكي
: مستعدون لدعم رومانيا في مواجهة مسيّرات روسيا.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/76355" target="_blank">📅 14:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76354">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7483fa8b.mp4?token=ofzHbOK6fOR38gSsH-2WfXQqHf6tpUYGSNDGqwTbie6NSBvrtCtSE_Q7aQyTJMWTUYYGx2nGBM1bQHFvtOSrxw17ylgj1zXRsWRGru-R5Wmg75W8eJNXLocxC5chPi200a5u7HhVC6D7RBvHwnUR1Vl73H8Nv2cLPdeRi_KjDbcxFIzY0roB4ZfmcSFPZ_T2unZXWeNnuWH5devHR2A_r8hrtl4ieAHqmtMs9I22GWFOsQnrbEqhGCyp7HIne_ppP2339lWimVapm9mbCS2sX3-hRUThAhY-U16rEXiz5TgmeVqHR7iuij8ZP9wXQtr7s7vPsjrulKphJ11-c7ufLrWSVTb6l2xjVKrUIjzmquV25BBCCVlRlHEisavXxmAEcf3uWusUCL8wUj79WBbqDv0gRRB0cIFWA3s21Yd0CmIWRFd-YomoASn90Jo05J2ijmK59l39pBiEmGozciKUydBe78V5daQ8Rq2mbcRtpwlplLGmAPuLIomNoP34nncCuyvKkExfF0Au1StFn4F4TolV94vRnRYie1ohx6NoTygmP4tRg4QXieSQfEgLCgyPYECKedSn_InWjZk6EsPA0vf84omCE1EeynVVrS0d7cwQ3HSLhqIM1y1Veo1OF2_P2SLaT_nfwOu3-ywQfZARek_hMsXhUOEYOrYWo2qsSq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7483fa8b.mp4?token=ofzHbOK6fOR38gSsH-2WfXQqHf6tpUYGSNDGqwTbie6NSBvrtCtSE_Q7aQyTJMWTUYYGx2nGBM1bQHFvtOSrxw17ylgj1zXRsWRGru-R5Wmg75W8eJNXLocxC5chPi200a5u7HhVC6D7RBvHwnUR1Vl73H8Nv2cLPdeRi_KjDbcxFIzY0roB4ZfmcSFPZ_T2unZXWeNnuWH5devHR2A_r8hrtl4ieAHqmtMs9I22GWFOsQnrbEqhGCyp7HIne_ppP2339lWimVapm9mbCS2sX3-hRUThAhY-U16rEXiz5TgmeVqHR7iuij8ZP9wXQtr7s7vPsjrulKphJ11-c7ufLrWSVTb6l2xjVKrUIjzmquV25BBCCVlRlHEisavXxmAEcf3uWusUCL8wUj79WBbqDv0gRRB0cIFWA3s21Yd0CmIWRFd-YomoASn90Jo05J2ijmK59l39pBiEmGozciKUydBe78V5daQ8Rq2mbcRtpwlplLGmAPuLIomNoP34nncCuyvKkExfF0Au1StFn4F4TolV94vRnRYie1ohx6NoTygmP4tRg4QXieSQfEgLCgyPYECKedSn_InWjZk6EsPA0vf84omCE1EeynVVrS0d7cwQ3HSLhqIM1y1Veo1OF2_P2SLaT_nfwOu3-ywQfZARek_hMsXhUOEYOrYWo2qsSq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 24-05-2026
آلية نميرا تابعة لجيش العدو الإسرائيلي في بلدة الطيبة جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/76354" target="_blank">📅 13:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76353">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🐦
نيويورك تايمز:
أحد أحدث العناصر الأكثر إثارة للدهشة في اتفاق مشروع السلام الإيراني هو صندوق استثمار مقترح لإيران - يبلغ حجمه حسب التقارير 300 مليار دولار أمريكي.
قامت إيران في الأصل بتصنيف ذلك على أنه تعويضات عن أضرار الحرب (التي تقدرها بـ 300 مليار إلى 1 تريليون دولار أمريكي). الجانب الأمريكي يعيد تسميته على أنه "صندوق استثمار" دولي سيساعد في تسهيله - وهو إطار أكثر ليونة يتجنب كلمة التعويضات.
يبدو أن الفكرة نشأت مع ستيف ويتكوف وجاريد كوشنر، اللذين اقترحا تعزيز مشاريع العقارات في طهران وآلية استثمار أوسع كحوافز للصفقة.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/76353" target="_blank">📅 13:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76352">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏الصحة العالمية: نتحقق من 223 حالة وفاة مرتبطة بإيبولا في الكونغو الديمقراطية
ارتفاع عدد الإصابات بـ"إيبولا" في الكونغو الديمقراطية لـ 906</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/76352" target="_blank">📅 12:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76351">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0fc8b717.mp4?token=Xd8WK9O7ioiLeB2OnwOwVK3EV73HEXOjoYgoO3DP-L9u2QmslhVirUQCvKuJiCjcIqEHLP3QBXDnRC_OfW0oKZIzLVMiC-jg04Bqn8M2RYQO_HVJT3k9HHTSXwrDJEodL9kFRcE5S0rAl9mLx1JtQN8UUgV1I1en13kBqosfkwVlnYj2E6UqSpP4tg0Qby1qNTBSVpBinN0a2UyS_b__UuAO86GiuxfJ6mlKTpkzV5etvgXArvLkDvVEOjpuVOxetshHY9MwYfxT7h5g7z8g9r7jmqBeEtkkjb47ATowV1uG8lnfq3paguuqcBCo_X3rk7hAoLfGyekLAtT1R3nZmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0fc8b717.mp4?token=Xd8WK9O7ioiLeB2OnwOwVK3EV73HEXOjoYgoO3DP-L9u2QmslhVirUQCvKuJiCjcIqEHLP3QBXDnRC_OfW0oKZIzLVMiC-jg04Bqn8M2RYQO_HVJT3k9HHTSXwrDJEodL9kFRcE5S0rAl9mLx1JtQN8UUgV1I1en13kBqosfkwVlnYj2E6UqSpP4tg0Qby1qNTBSVpBinN0a2UyS_b__UuAO86GiuxfJ6mlKTpkzV5etvgXArvLkDvVEOjpuVOxetshHY9MwYfxT7h5g7z8g9r7jmqBeEtkkjb47ATowV1uG8lnfq3paguuqcBCo_X3rk7hAoLfGyekLAtT1R3nZmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
دوي انفجارات تهز محافظة حمص السورية</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76351" target="_blank">📅 12:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76350">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">🇮🇶
وزارة الموارد المائية العراقية: جاهزون لاستيعاب الموجة المائية القادمة من سوريا ولا توجد أي مخاوف على السكان القاطنين على ضفاف نهر الفرات</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/76350" target="_blank">📅 12:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76349">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDzuAQ93SkMUmn8i0Ze8qPoVRE4KC2ZEWs8YxYM10ULWEdqz3R2BCZNDbwvcU5l8LnKEZkbSa74QrV-J7-8FYdFJcNjhkxyqg5SAz5RfPmh1wYy3YjgVqagBqb-YvB_b_Lo8CvD5DJdvIsm7FvBXyELVhUoGwpLPw3u3s2NrWwtrlT-oBLESZrRAEFqAtefbKneNJNBjP_n0HJtFLizfbOw-ys3NIyLSSIn9cM35WtDlKCbzPuPzwU29hWj4P4jZenFrVJj0xK-OG-8Qkr1WwE187SWCKobbAvFlAlIjuJFgmPS1nw3WGCCY-O-BJURE_29r8b1k0591q6PD_PT4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ اعتراضية الآن فوق الجليل الأعلى دون تفعيل صفارات الإنذار</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76349" target="_blank">📅 11:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76348">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 26-05-2026 دبابتي ميركافا تابعتين لجيش العدو الإسرائيلي في بلدة رشاف جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76348" target="_blank">📅 11:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76347">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏الأمين العام للناتو: خرق مسيّرة روسية أجواء رومانيا يؤكد أننا جميعا في خطر</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76347" target="_blank">📅 11:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76346">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">إعلام إيراني: حركة الملاحة البحرية في مضيق هرمز الآن</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76346" target="_blank">📅 11:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76345">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حدث أمني يتعرض له جنود الاحتلال جنوب لبنان</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76345" target="_blank">📅 10:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76344">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📰
سي إن إن: تراجع مخزونات الولايات المتحدة من النفط الخام والبنزين والديزل بسرعة مع استمرار الحرب مع إيران</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76344" target="_blank">📅 10:16 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76343">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ول ستريت جورنال:
مقتل
7 من أصل 11 جندياً إسرائيلياً سقطوا منذ بدء وقف إطلاق النار في أبريل بسبب مسيرات الـ FPV
مع كل رحلة بالمسيرات يكتسب مقاتلو حزب الله خبرات اكثر</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76343" target="_blank">📅 08:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76342">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">في خبر غير مهم
🌟
وزارة الخارجية العراقية تدين قصف قواعد الاحتلال الاميركي في الكويت التي انطلقت منها الصواريخ لضرب ايران.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/76342" target="_blank">📅 02:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76341">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌟
فانس
: نقترب من نقطة تسمح لنا بالجلوس وحسم القضايا العالقة مع إيران لكن الأمر يتطلب إحراز تقدم إضافي.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/76341" target="_blank">📅 01:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76340">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f662ae4b77.mp4?token=Rp4pl5q-QifUhLwrGktmwSXDlE3sd3FjSyEnnwAFezlXzbXKTuIqhdViy2fJvNrZK0_11VI3OboFjbM_vgdD8cNVq1ENf88vZKa9g45h4zgQpicKmzRvFhjYGOn0kRYPBqu_W_t-TgqbqmcG00smyxs-g7cMGCovc19B-FDZDrKaEnKhQhUEWZzNumcn2qNPJRocoUrmYUaRjNLSvY7TpufymAMtLyckKdnFuo55AoRYv07TKRu-iub04bp-zUj_7dbtlLPHxrmisz_DMIDobGMQN1eLmKzLQFRtMlt17DUYJx9kHa4JOmxBaCqZ3ooNdf0Q3JDSTQLAY9oQNrSSpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f662ae4b77.mp4?token=Rp4pl5q-QifUhLwrGktmwSXDlE3sd3FjSyEnnwAFezlXzbXKTuIqhdViy2fJvNrZK0_11VI3OboFjbM_vgdD8cNVq1ENf88vZKa9g45h4zgQpicKmzRvFhjYGOn0kRYPBqu_W_t-TgqbqmcG00smyxs-g7cMGCovc19B-FDZDrKaEnKhQhUEWZzNumcn2qNPJRocoUrmYUaRjNLSvY7TpufymAMtLyckKdnFuo55AoRYv07TKRu-iub04bp-zUj_7dbtlLPHxrmisz_DMIDobGMQN1eLmKzLQFRtMlt17DUYJx9kHa4JOmxBaCqZ3ooNdf0Q3JDSTQLAY9oQNrSSpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
البيت الأبيض ينشر فيديو مع عبارة "هل أنت تستمع؟".</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/76340" target="_blank">📅 01:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76339">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌟
وزارة العدل الأمريكية:
توجيه 8 تهم للعراقي محمد باقر السعدي بسبب أنشطته مع كتائب حزب_الله والحرس الثوري، السعدي ضالع في 20 هجوما ومخططا ضد مصالح أمريكية وإسرائيلية بعضها على الأراضي الأمريكية.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/76339" target="_blank">📅 00:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76338">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجار داخل مسبح يهز مدينة الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/76338" target="_blank">📅 00:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76337">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARNOklx14RfnVu_4Em2tbnUmYgEKVIHqDtfbkOpPEkmXftMWQuE7dac61ydcD6VMx6QfUjQrzNKDC6E_BPemei7MNXctYZxxQKZlKbBLaqeOmRbm0w6aO3pPp8OvuGO2R9LCjwUHdei18TD7nNIAjX651KINlbqjpLiusANzNyg09cVH7dRB_gTaj9y0qaAJo_XjMpRLE1IILP0Ikh19OiCNaKDxMJNiHFdhxCH8GkYJaCR59hDpf9Z4b6k-HfX6-uQZf1782adi5s7Hmhozs5il6BDLXaq8OFHqFPWTeQ_Ui5rMCqFxarICFwFhJTasNVuKpQq0qZYjPmtyqjipAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار داخل مسبح يهز مدينة الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/76337" target="_blank">📅 00:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76336">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجار داخل مسبح يهز مدينة الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/76336" target="_blank">📅 00:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76335">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKikjtojkkMl9Rf0mmlYXrUIOLFt5iJNIkXATcVF8ivw-yAJGTSOAXrY0aCfeAPmsSfJQMsx2JXRU-HjFwx4v30nXRamuWab3k4iOky87Qipx4AXLXOex_1z2Gao8IYdjyP8lI54cYyG2iOtkoZSYg23T8-WEdLuHquI-YquKfJR_Bh4IXjBE3YmAYPN3B_irZF17tEsmiNIjZnUlHDVADnycbxcEybG7Jef-AcNDEe5l9IZ2dzaIPkOMjMVwDyUii2Lb5YGjg7ptbyqRMbtSq2VHCwmxEMYYnqHH2CjLlzdVrYewDTL0jJ6WYelkFV5pU7oUi_lOaZNFnZV5KM1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇬🇧
رصد نايا
تمارس القوات الجوية البريطانية نشاط لوجستي في سماء العراق حيث تم رصد طائرة شحن عملاقة " A400 “ بالتزامن مع وجود طائرة إرضاع جوي اخرى تؤمن الوقود للطيران الحربي ؛ يذكر ان السفير البريطاني في بغداد قد صرح لقناة عراقية ان العراق يتمتع بالسيادة ولا يوجد هناك احتلال</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/76335" target="_blank">📅 00:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76334">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
‏وكالة مهر: الدفاعات الجوية حاولت التصدي لطائرات معادية في بوشهر.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/76334" target="_blank">📅 00:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76333">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
وكالة مهر: القوات المسلحة الإيرانية أطلقت نيراناً تحذيرية باتجاه 4 سفن مخالفة قرب مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/76333" target="_blank">📅 00:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76332">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صواريخ كروز من طراز ابو مهدي المهندس باتجاه سفن أمريكية في هرمز</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/76332" target="_blank">📅 23:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76331">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🌟
🇷🇺
‏الخزانة الأميركية تصدر ترخيصا يسمح ببعض الصفقات مع شركة "لوك أويل" النفطية الروسية.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/76331" target="_blank">📅 23:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76330">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🌟
🇷🇺
‏الخزانة الأميركية تصدر ترخيصا يسمح ببعض الصفقات مع شركة "لوك أويل" النفطية الروسية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/76330" target="_blank">📅 23:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76329">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">أنباء عن انفجارات في هرمز</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/76329" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76328">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639d01573a.mp4?token=PaDvLingfH_xCi5wMs3bXINK5tdv_0DXkylyJD2_rKctjzkm1wO6TJZ7Nt1MzjfkSEt_DYjeC7z0K3jQIiCpU8vATNCJMQt7F-6cJSiZbCh0wmWNbYew7o51GjgTLd_Yx5J-r1E4EVuiOsMUFLtdesV9PAvaQiKEkrjYItPXAVnmHthHCf1BkBNVQ_MLop8xxoKbHUbiBw9C1XUIskmV-gbNU8nUpDG0SzuUh16jpI1kXdvu8T_Qwji0d7sdfhSLDZQ1X2STOIRrT1ho95uqUyadD5AiCY2IdxRqZPhfros61RZVKsHWEvnHYB6l9f8FHRLVkKenWSpUFs2DVUWAu73cFiGzE5t9QelamQ2CzbMYjOFz12t404wjRiYhP7FNw_riEvoax64UxjpTKEPH0rzMtXyryLIJ90ryXGNg5V69rEXSPjnfeUInLld7uwkNm48iW5AKDO15t9jUiAnzR3uQ0MU76-RuyJ5fj0DNpUYN99c0j1JUGXa7lX6Bd7VFxiAhK9NLHnvBbOWYdEvLGJ9HG5MzvmQ1Ivpfum2DU5acQJZCOPcPBJE4d5z5YdxHKAc51anerfMXUMM8xN_m1yW7BgysmcfT1cMHVKXxpP5bW8MMMxWbNJFgiEiDWQFwoyBA1B8nYaW42_US2mJI4jFvomrcjCz6HzQLd9zFT-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639d01573a.mp4?token=PaDvLingfH_xCi5wMs3bXINK5tdv_0DXkylyJD2_rKctjzkm1wO6TJZ7Nt1MzjfkSEt_DYjeC7z0K3jQIiCpU8vATNCJMQt7F-6cJSiZbCh0wmWNbYew7o51GjgTLd_Yx5J-r1E4EVuiOsMUFLtdesV9PAvaQiKEkrjYItPXAVnmHthHCf1BkBNVQ_MLop8xxoKbHUbiBw9C1XUIskmV-gbNU8nUpDG0SzuUh16jpI1kXdvu8T_Qwji0d7sdfhSLDZQ1X2STOIRrT1ho95uqUyadD5AiCY2IdxRqZPhfros61RZVKsHWEvnHYB6l9f8FHRLVkKenWSpUFs2DVUWAu73cFiGzE5t9QelamQ2CzbMYjOFz12t404wjRiYhP7FNw_riEvoax64UxjpTKEPH0rzMtXyryLIJ90ryXGNg5V69rEXSPjnfeUInLld7uwkNm48iW5AKDO15t9jUiAnzR3uQ0MU76-RuyJ5fj0DNpUYN99c0j1JUGXa7lX6Bd7VFxiAhK9NLHnvBbOWYdEvLGJ9HG5MzvmQ1Ivpfum2DU5acQJZCOPcPBJE4d5z5YdxHKAc51anerfMXUMM8xN_m1yW7BgysmcfT1cMHVKXxpP5bW8MMMxWbNJFgiEiDWQFwoyBA1B8nYaW42_US2mJI4jFvomrcjCz6HzQLd9zFT-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية تصدي المقاومة الإسلامية بتاريخ 26-05-2026 أجهزة اتصالات تابعة لجيش العدو الإسرائيلي في موقع العاصي على الحدود اللبنانيّة الجنوبيّة بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/76328" target="_blank">📅 23:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76327">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">أنباء عن انفجارات في هرمز</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/76327" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76326">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محرم 1 00_٠٦٤٢٥١</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/76326" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">شبه لهم يا حسين
#شاركها</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/76326" target="_blank">📅 22:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76325">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وَاللهِ لاَ أُعْطِيكُمْ بِيَدِي إِعْطَاءَ الذَّلِيلِ، وَلاَ أُقِرُّ إِقْرَارَ الْعَبِيدِ
وإنّ الدّعيّ بن الدّعيّ قد ركز بين اثنتَين؛ بين السّلة (والذّلّة، وهيهات منّا الذّلّة؛ يأبى الله لنا ذلك ورسوله والمؤمنون، وحجورٌ طابت وطهرت، وأُنوفٌ حميّة، ونفوسٌ أبيّة، من أن نؤثر طاعة اللئام على مصارع الكرام ..</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76325" target="_blank">📅 22:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76324">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9IhF_6AwK5Zwesgo4FhVFwsKFbL1xhi_33LDhqHfYpfpxJR_Yg-L5IwFAl3BNVcTufGrbaTb88vAC8Tn0v0cE7MCG4-voVYQbQgBEFeNAeky4MmtEIT_In1feA8_JWucDTnq0TQJXW2ENwzzpxU_hjyUekfLNAGc4njECj4e5bfEtHgGZxFHX-2d-BlMX9UcpW1r-DiW-7zlxxZBHDeB1JdcJ7BaokC5PuadluoLG8iouWFSPgG2pyajG491ZCEiI81J6FKmoXWE2w7mq8Vh0swftfAyY7aZ-v9L2wu-VhRCGeEnOk08tR8-Co6DhLb7N7YE-SccGXHflRunPmhmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المتحدث باسم "سرايا أولياء الدم" أبو مهدي الجعفري: لا تسليم للسلاح ولا حديث عن الطمأنينة قبل أن يرفع الظلم وينتهي الاحتلال عن العراق</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76324" target="_blank">📅 22:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76323">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZzVAlX97Td40-ypgTFsJNS_PjasRP69jy7Gm15Mn1Ix_-t052u-W-NUzZqperxu4tG0Y8vzCDD-Nc8Y8Zh-uHhbJHB2zE6_M341FDP9jN7SEtlmGpq9Y5dKVvI_SXH1DcBeKMojKOReNBotttFeFdHqt5mdUwx50-lNvDTKf1duIUoYgMvOvnUJo7oR8KjvErjLreKV7olPiicP6yrDTgTELh2CvUo1s8E5yYZKIT1saN9fdSO3WAyBJtYhjeQDhZntTwaCms02IcgDKn2qL2lktyb2MbHtEcOxq-F4HdIKwfQ_zuJHymWhlBtU3xNotNJkk5CwZM1XdxCo3WX9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">كلُّ عامٍ والوطنُ بخير، ما دام فيه حُرّاسٌ ودماءُ شهداء ورجالٌ مستعدّون للتضحية.
لا تسليمَ للسلاح، ولا حديثَ عن الطمأنينة، قبل أن يُرفع الظلم وينتهي الاحتلال عن العراق.
في الحرب ينادوننا أبناءَ الأطايب، وفي السِّلم يتناسون أسماءَ الذين حموا الأرض.
فالأوطان لا يحرسها العابرون، وللمقاومة رجالٌ أوفياء يحمون العراق في كل ِّ المحن.
#موقفنا_ثايت
#قرارنا_مقاومة</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76323" target="_blank">📅 22:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76322">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 23-05-2026
منصتيّ قبّة حديديّة تابعتين لجيش العدو الإسرائيلي في ثكنة راميم (هونين) بمحلّقتي
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76322" target="_blank">📅 22:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76321">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🌟
بيان صادر عن حزب الله ردًا على مزاعم العدو الإسرائيلي الكاذبة حول سدّ القرعون:
يواصل العدو الإسرائيلي سياسة الأكاذيب والتضليل لتبرير اعتداءاته المستمرة على لبنان وجرائمه بحق المدنيين والأطفال والمسعفين والإعلاميين، في انتهاك صارخ لكل القوانين والأعراف الدولية. واليوم يخرج علينا بمزاعم كاذبة واتهامات سخيفة لتبرير اعتدائه الخطير في محيط سدّ القرعون، الذي يُعد من أهم المنشآت والبنى التحتية المائية الحيوية والاستراتيجية في لبنان، ويشكّل مصدرًا أساسيًا للمياه والريّ والطاقة الكهربائية لعشرات المناطق اللبنانية، بما يمس مباشرة بأمن اللبنانيين.
إن ادعاء العدو حرصه على البنى التحتية اللبنانية وخيرات لبنان المائية والزراعية والكهربائية، وخوفه على الاقتصاد اللبناني، لن ينطلي على أحد. وإن سعيه لتحميل المقاومة مسؤولية الأزمات التي تسبب بها الاحتلال نفسه وعدوانه المستمر بدعم أميركي مفتوح ومباشر، ومحاولة تصوير المقاومة كأنها تعمل ضد المصلحة الوطنية اللبنانية، يندرجان في سياق التحريض الداخلي وإثارة الفتنة وبث الانقسامات بين اللبنانيين.
إن العدو الإسرائيلي، الذي دمّر خلال حروبه واعتداءاته المتكررة على لبنان الجسور والطرقات ومحطات الكهرباء والمياه والمرافئ والمنازل والمنشآت المدنية، ولا يزال يمارس يوميًا اعتداءاته بحق اللبنانيين وسيادة لبنان ومقدراته الوطنية، لا يمكن أن يدّعي حرصه عليها أو أن يكون حاميًا لها، بل يبقى التهديد الحقيقي والدائم لأمن لبنان واستقراره وبناه التحتية واقتصاده.
وإننا إذ نحذر من أن تكون هذه الادعاءات والذرائع المفبركة تمهيدًا لاعتداء إسرائيلي جديد يستهدف سد القرعون أو محيطه، أو يستهدف المنشآت المدنية والحيوية في لبنان، فإننا نضع هذه التهديدات برسم المجتمع الدولي والمؤسسات الحقوقية والإنسانية، التي باتت مطالبة بكسر صمتها إزاء الاعتداءات الإسرائيلية المتكررة على لبنان وبناه التحتية.
كما ندعو الدولة اللبنانية، بكل مؤسساتها، إلى دق جرس الإنذار وعدم الاكتفاء بالمشاهدة، والتحرك الفوري على المستويات الدبلوماسية والقانونية والإعلامية كافة، وتقديم شكوى عاجلة إلى الجهات الدولية المختصة، بما يضع المجتمع الدولي أمام مسؤوليته في لجم هذا العدو عن عدوانه وإجرامه بحق لبنان وشعبه.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76321" target="_blank">📅 21:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76320">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
مصدر إيراني مُقرّب من فريق التفاوض: خلافًا لما تزعمه بعض المصادر الغربية من أن نص ما يُسمى "مذكرة التفاهم" بين إيران والولايات المتحدة قد تم الانتهاء منه، وأنه ينتظر فقط إعلان الطرفين، فهذا غير صحيح، ولم يتم الانتهاء من صياغة النص بعد. لم تُعلن إيران بعدُ…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76320" target="_blank">📅 21:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76319">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTyTvMetv0c7O3MbvLP0jIktyOQJLBiFfEbifChOjzZdlkAxlHCEvotfmw0cxIAZwrP-pdDa36QuNp7zWQx55HmM7Hr4jmk7tc6GkQbGy0K0ppqhakGzK-4EP41gNIiUsvxpc3N3AOl-GQbdj6tYsVlh1yXiBXct0BR3NlxUhhti-iQLx0sTNh2zG6rXJdDz2IIClpwHqB5SefIjdVOBQxNaFk54u7-XB57yc_x40t3ZokFdfDZVlNA-ZGLKfyDQvNMegkpN8a_xyaGCV4ySLgi4LpwITKtEzon1WUKQ6D4zQA4faNkExIpzBxY_Hodgn7-226jjQalsfJpVhRMFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
🇮🇶
🇮🇶
اهتمام روسي إعلامي كبير بزيارة الحاج فالح الفياض رئيس هيئة الحشد الشعبي و السيد قاسم الاعرجي للعاصمة موسكو ..</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76319" target="_blank">📅 21:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76318">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
سي إن إن: ترامب يسعى للحصول على المشورة قبل الموافقة على الاتفاق مع إيران.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76318" target="_blank">📅 21:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76317">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/76317" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرايا أولياء الدم بالميدان
#شاركها</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76317" target="_blank">📅 21:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76316">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بيان هام بعد قليل لا ابو مهدي الجعفري الناطق العسكري لسرايا اولياء الدم … لذلك نسترعي الانتباه</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76316" target="_blank">📅 21:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76315">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⭐️
ذي أتلانتيك:
بدأ ترامب الحرب لأسباب شخصية، وليس استراتيجية واضحة، وهو الآن في طريقه للخسارة لتلك الأسباب الشخصية نفسها، حيث خدع نفسه فقط.
الرئيس الذي كان دائمًا ما يصف أسلافه بـ "الأغبياء" ويصف نفسه بـ "الذكي" تجاهل أن كل شخص من كارتر وريغان إلى بايدن كان حكيمًا بما يكفي لعدم بدء حرب كبيرة مع إيران.
ترامب طالب بـ "الاستسلام غير المشروط" لإيران، لكنه يتفاوض الآن على صفقة تلبي طلبات طهران أكثر من طلبات واشنطن.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76315" target="_blank">📅 21:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76314">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR0woLxSJ99URNS6-_A1s6H6SvIZDGqCg_NgC6SUuPySret4GgzZ8L7_0Ew8s1x18WGP3yWEJQqXk0YsL1boRXj7KtWXK_z4BYLoZtNCHM9rcTF_MYKG6XwjI7zkF2kGZiYVwrO9CZLn34H3B7_UV6QSN-K7G1yRfejDnpepMgMDEovkMGsWDayTwqq7uICVHVcOi5jVuF_l6LRpZ_ZT23FkuQMc_rNEFmlSH9hQcT4kX1nilqfP8TCSRJ-cKleXZgfogxdCR_ghayeNO4IYUSQJVQtZvrYxjPdpaKLf8hMOsZaU8tl8u3a4tqirsrrzaW46sRY3W_E2UFu1vxVhtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاول مرة بدر تخرج عن المألوف
🌟
المكتب السياسي لفيلق بدر ينشر عن تحديات التي تعرقل مضي العراق في مشروع التنمية بتفاصيل اكثر
اضغط هنا</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76314" target="_blank">📅 21:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76313">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
مصادر أمريكية: نؤكد توصل الولايات المتحدة وإيران إلى مذكرة تفاهم بشأن مضيق هرمز والمفاوضات النووية.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76313" target="_blank">📅 20:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76312">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
25-05-2026
آليتين تابعتين لجيش العدو الإسرائيلي عند موقع رأس الناقورة البحري على الحدود اللبنانية الجنوبية بمحلّقتي أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76312" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76311">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
تظاهر نحو 30 رئيس بلدية إسرائيلي أمام مبنى الأمم المتحدة احتجاجًا على القرار المشين بإدراج "إسرائيل" على القائمة السوداء بتهمة العنف الجنسي إلى جانب حركة حماس. وأوضح وفد من مركز بيريز الأكاديمي أن "هذا قرار معادٍ للسامية، ومنفصل عن الواقع، وغير أخلاقي.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76311" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76310">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: بعد تقييم الوضع، تبقى سياسة الدفاع لقيادة الجبهة الداخلية دون تغيير، وستظل سارية المفعول حتى الساعة الثامنة مساءً من يوم الأحد الموافق 31 مايو 2026.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76310" target="_blank">📅 20:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76309">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🏴‍☠️
‏إذاعة جيش العدو: شكوك بشأن نجاح عملية اغتيال علي الحسيني قائد وحدة الصواريخ في حزب الله</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76309" target="_blank">📅 20:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76308">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
بعد تقييم الوضع، تبقى سياسة الدفاع لقيادة الجبهة الداخلية دون تغيير، وستظل سارية المفعول حتى الساعة الثامنة مساءً من يوم الأحد الموافق 31 مايو 2026.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76308" target="_blank">📅 20:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76307">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
نحن لا نسعى لامتلاك أسلحة نووية، ولا نمارس الدبلوماسية بالإذلال؛ إن الاضطرابات في المنطقة سببها
إسرائيل
.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76307" target="_blank">📅 20:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76306">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed657d94fe.mp4?token=vZAhQ0p320DXs7Z-ukCTrDcWkeUOqOqPcdBYHkDb0e-9m_5y84P1so03pug9--y4sIfBdxmitV9n7Ywja2nLe_TxBebiAJO4bmDsauhq8QT8iFachd12rEAjK-cB4HoCckq3NJxlElrIMlHJtb5VyAg5g919GUcMxpwxZdHCxSelYTAWztXmN8Tnb_CkxFA8ERXPlrBc4hQ2ZljtAVNoCvjwIR5lgnTVy_OkcL6xHt32PGEfP3POavXMklJDCxgV1uvAghXIG-vHB0XSmYuZbRW5dmEO5d-BxFM1yJE7wframa24H8Np91Uqb6_0tRdBYp2HZEp8chyV_Dd_RwGZ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed657d94fe.mp4?token=vZAhQ0p320DXs7Z-ukCTrDcWkeUOqOqPcdBYHkDb0e-9m_5y84P1so03pug9--y4sIfBdxmitV9n7Ywja2nLe_TxBebiAJO4bmDsauhq8QT8iFachd12rEAjK-cB4HoCckq3NJxlElrIMlHJtb5VyAg5g919GUcMxpwxZdHCxSelYTAWztXmN8Tnb_CkxFA8ERXPlrBc4hQ2ZljtAVNoCvjwIR5lgnTVy_OkcL6xHt32PGEfP3POavXMklJDCxgV1uvAghXIG-vHB0XSmYuZbRW5dmEO5d-BxFM1yJE7wframa24H8Np91Uqb6_0tRdBYp2HZEp8chyV_Dd_RwGZ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إعلام العدو:
انقطاع التيار الكهربائي في المطلة بعد إطلاق صواريخ من قبل حزب الله.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76306" target="_blank">📅 20:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76305">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الإيراني: لن نوقع على أي تفاهم لا ينسجم مع مصالحنا وسنرد على أي انتهاك لوقف إطلاق النار.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76305" target="_blank">📅 19:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76304">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⭐️
‏أكسيوس عن مسؤولين: اتفقت الولايات المتحدة وإيران على تمديد وقف إطلاق النار لمدة 60 يومًا وإطار المحادثات النووية، لكن ترامب يؤجل التوقيع شخصيًا. لقد طلب من الوسطاء بضعة أيام للتفكير في الأمر قبل اتخاذ قرار نهائي.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76304" target="_blank">📅 19:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76303">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
25-05-2026
خيمة تموضع لجنود جيش العدو الإسرائيلي في موقع حدب البستان على الحدود اللبنانية الجنوبية بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76303" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76302">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83ccef82c.mp4?token=Hgm_MdYwSY_IWA0oQ4aNh1qem9Ehw2EEad_zEUXS7PTmpd0qOeYp3VnEyacFpGyhwBigy6xEgta8zcg61b5mCu1zXtr0N2sa-wncf0TNjAJ9IoKkTeEDeI06tSEasIiFOAGM3SDyqI88Rm_2C3NU5DjzVx3bTt_h2lO8Bl1z2eJ917MUH5m3w9yxUVpFvTdAXY5g34maIjwrtgzh972Ks4NJ2_Hpm5GUIFRzxPNpFbsFq3xwd31qELCsUcS6diMUjIEGXp07Qt2OAzUdn_2gWqrfFb6tRHX6b0152rvIVemIs2Xds6BLorJMwbVhrbTeEAz44ijBVIg6oRL76i50xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83ccef82c.mp4?token=Hgm_MdYwSY_IWA0oQ4aNh1qem9Ehw2EEad_zEUXS7PTmpd0qOeYp3VnEyacFpGyhwBigy6xEgta8zcg61b5mCu1zXtr0N2sa-wncf0TNjAJ9IoKkTeEDeI06tSEasIiFOAGM3SDyqI88Rm_2C3NU5DjzVx3bTt_h2lO8Bl1z2eJ917MUH5m3w9yxUVpFvTdAXY5g34maIjwrtgzh972Ks4NJ2_Hpm5GUIFRzxPNpFbsFq3xwd31qELCsUcS6diMUjIEGXp07Qt2OAzUdn_2gWqrfFb6tRHX6b0152rvIVemIs2Xds6BLorJMwbVhrbTeEAz44ijBVIg6oRL76i50xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
متظاهر حريدي في محاولة إنتحار رفضاً للإنضمام إلى الخدمة العسكرية ومن تحت عجلة يهتف "نموت ولن ننضم للخدمة".
😭</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76302" target="_blank">📅 19:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76301">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9421e16253.mp4?token=iBvfmaD_cHTHjOOkf_9s4giwdS9fM-TMFBT3VATHIGRGSvMxArmbEY5eVaF7sjvjybndrZMMd72U2Iik-ZWzZ4KuihvMIf84_fzko0htfwdWB8JeTI4T--vJcgwOYoNFv1Yhjg5VsC-TrjpGAVedm3-KNBWmqYUTaRSPY6S57xQCaPHFBiL6CVUfYIc-kdCBVywB7HBHKwnUXCGE4OoSFO_1gRPs6hDK5yonw8RStWvJjKz3KGNivIy3uNDwI_2x14poELbkVyEEqjWU6vRtYZH9G7dyukf0csBAY8o2OTfZSsQvXGtY4ktXskXGHr01jKAEGZg2V88Xd0wVKMxXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9421e16253.mp4?token=iBvfmaD_cHTHjOOkf_9s4giwdS9fM-TMFBT3VATHIGRGSvMxArmbEY5eVaF7sjvjybndrZMMd72U2Iik-ZWzZ4KuihvMIf84_fzko0htfwdWB8JeTI4T--vJcgwOYoNFv1Yhjg5VsC-TrjpGAVedm3-KNBWmqYUTaRSPY6S57xQCaPHFBiL6CVUfYIc-kdCBVywB7HBHKwnUXCGE4OoSFO_1gRPs6hDK5yonw8RStWvJjKz3KGNivIy3uNDwI_2x14poELbkVyEEqjWU6vRtYZH9G7dyukf0csBAY8o2OTfZSsQvXGtY4ktXskXGHr01jKAEGZg2V88Xd0wVKMxXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
🇮🇶
🇮🇶
اهتمام روسي إعلامي كبير بزيارة الحاج فالح الفياض رئيس هيئة الحشد الشعبي و السيد قاسم الاعرجي للعاصمة موسكو ..</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76301" target="_blank">📅 19:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76300">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47e2cac299.mp4?token=Cb2OThkGiGTRYDLMqQf1lSQ456T33JIzB0vMrNjABicJM6-Tq8fU-VHmfvCTVIzxLQ_JDG7dEfJyD0MQUBYa614PqGV8wP5B1JYT3aPDIaXad_Zq-7GeSFVJzsSDOSnQwKVQz1hW4Fs2eI4Gc2ZyUTHKXQLXjT7ShF0hNEIj5Z1dWxaJdY_emjzzxjZr7aFLb9swLaR0enArGlCzanuMR6CmKDo993sxFNCoP2L8BRiJ4E-tqdKS8RIpx49-YjHHT6iXoXk8KxX3yQ7ovCpdddvx7da-m37NgIevakJle0B5mUEu2PyxnaXjKohxWIEFHD0f5-F21LnHp1VP_5lP9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47e2cac299.mp4?token=Cb2OThkGiGTRYDLMqQf1lSQ456T33JIzB0vMrNjABicJM6-Tq8fU-VHmfvCTVIzxLQ_JDG7dEfJyD0MQUBYa614PqGV8wP5B1JYT3aPDIaXad_Zq-7GeSFVJzsSDOSnQwKVQz1hW4Fs2eI4Gc2ZyUTHKXQLXjT7ShF0hNEIj5Z1dWxaJdY_emjzzxjZr7aFLb9swLaR0enArGlCzanuMR6CmKDo993sxFNCoP2L8BRiJ4E-tqdKS8RIpx49-YjHHT6iXoXk8KxX3yQ7ovCpdddvx7da-m37NgIevakJle0B5mUEu2PyxnaXjKohxWIEFHD0f5-F21LnHp1VP_5lP9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
البيت الأبيض ينشر فيديو مع عبارة "هل أنت تستمع؟".</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76300" target="_blank">📅 18:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76299">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭐️
إعلام العدو:
التقديرات هي أن المعركة القادمة مع إيران ستبدأ بمفاجأة تامة دون أي إنذار مسبق.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76299" target="_blank">📅 18:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76298">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🌟
حزب الله ينشر:
لِتَعلَم كلّ أمٍ عِبريّة...
תדע כל אם עברייה...</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76298" target="_blank">📅 18:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76297">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
وزارة الخزانة الأمريكية تهدد سلطنة عُمان:
‏لن تتسامح حكومة الولايات المتحدة مع أي محاولة لفرض رسوم عبور في مضيق هرمز. وعلى سلطنة عُمان، على وجه الخصوص، أن تعلم أن وزارة الخزانة الأمريكية ستستهدف بقوة أي جهة متورطة - بشكل مباشر أو غير مباشر - في تسهيل فرض رسوم العبور، وسيتم معاقبة أي شريك متواطئ. يجب على جميع الدول رفض أي محاولات من جانب إيران لعرقلة حرية التجارة رفضًا قاطعًا.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76297" target="_blank">📅 18:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76296">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a977370897.mp4?token=oNr6uChliYwpoddlIVaRKuCBJgmNqVKw2Tox33NRF8Jmcpz4Pt6X1FsayekgZ1MeIRhNrd_L24pId4qfsU88rpzik4_OQh3jecIVOObomuXYlOkiuUt1z1RaL1ZSWwWhoMRHSkg8a91yeb3_2Sa28go5wW_RyWM6MhDMAGbuza_UkIgOPxnPEGlJrAejN81js8i87NdV-lN4vep5xoQZAY14h-r3BkakFa7sxX-QXa0Nph5h5VJTKach-TY889YqpCUJHKdsGRirGRpOz9Ol46leBTIfxajWeXeR3fcfdCo9JYbrw69nW85tSqZXHx-J2O35HYZKE2BUFKkkp6e_EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a977370897.mp4?token=oNr6uChliYwpoddlIVaRKuCBJgmNqVKw2Tox33NRF8Jmcpz4Pt6X1FsayekgZ1MeIRhNrd_L24pId4qfsU88rpzik4_OQh3jecIVOObomuXYlOkiuUt1z1RaL1ZSWwWhoMRHSkg8a91yeb3_2Sa28go5wW_RyWM6MhDMAGbuza_UkIgOPxnPEGlJrAejN81js8i87NdV-lN4vep5xoQZAY14h-r3BkakFa7sxX-QXa0Nph5h5VJTKach-TY889YqpCUJHKdsGRirGRpOz9Ol46leBTIfxajWeXeR3fcfdCo9JYbrw69nW85tSqZXHx-J2O35HYZKE2BUFKkkp6e_EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إطلاق صواريخ إعتراضية شمال فلسطين المحتلة دون تفعيل صافرات الإنذار.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76296" target="_blank">📅 18:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76295">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭐️
‏
أكسيوس عن مسؤولين:
اتفقت الولايات المتحدة وإيران على تمديد وقف إطلاق النار لمدة 60 يومًا وإطار المحادثات النووية، لكن ترامب يؤجل التوقيع شخصيًا. لقد طلب من الوسطاء بضعة أيام للتفكير في الأمر قبل اتخاذ قرار نهائي.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76295" target="_blank">📅 17:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76294">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🏴‍☠️
🇺🇳
‏الكيان الصهيوني يعلن تعليق علاقاته مع الأمين العام للأمم المتحدة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76294" target="_blank">📅 17:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76293">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏴‍☠️
نتن ياهو يوجه الجيش الاسرائيلي برفع نسبة السيطرة في قطاع غزة من 60% الى 70%</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76293" target="_blank">📅 17:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76292">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏴‍☠️
نتن ياهو يوجه
الجيش الاسرائيلي
برفع نسبة السيطرة في قطاع غزة من 60% الى 70%</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76292" target="_blank">📅 17:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76291">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇶
أنصار الله الأوفياء الفصيل العراقي ؛ يعلن عن استهداف قيادي بالحركة على الأيادي الصهيو أمريكية في محافظة ميسان جنوبي العراق .</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76291" target="_blank">📅 17:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76290">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تنظيم داعش الارهابي يتبنى الانفجار الذي طال جهاز مكافحة الارهاب العراقي</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76290" target="_blank">📅 17:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76289">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
‏
التلفزيون الايراني:
بينما انتهكت أمريكا وقف إطلاق النار مرارًا وتكرارًا بمهاجمة الأراضي الايرانية خلال المفاوضات وفترة وقف إطلاق النار، يسعى جيش هذا البلد إلى إيجاد ذريعة لبدء حرب من خلال بناء رواية زائفة! سيكون رد إيران من خارج المنطقة. المفاوضات ما هي إلا خداع أمريكي جديد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76289" target="_blank">📅 16:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76288">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026
آلية هندسيّة تابعة لجيش العدو الإسرائيلي في مدينة الخيام جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76288" target="_blank">📅 16:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76287">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0mDWe4CGvMGEgB2flxidmA7u1sxMr-0NZiRzDJkcY9NPAqHbucrhdBweE3raEwW20a-AjbKYB7TjM1o119UTQ1V9CciAGjLQMuF-Srdt7YOUNDIQnBiLpfsSa6WjzjRfRX3hDeos9-9iWDmSUmAbvNIoRnDBWQS3UgVOUgqUSerxAo0cEkT2upMBtZaP9cQFdEMmtYEO-iK_i_80UkRF22C6c0ZnB87K1GvyjGpi956ak51pAuv3CfZO6Jg3v8j-o0fnUADCx-EqZ8Nz4eH2rAXh2ZRue5H49lhw59Fiw2PZxCWnWxfZ8Bu8rFMwRygnUcRLKLiKGKNvwucgdf8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير الخزانة الأمريكي:
سنمنع الطائرات الإيرانية من الهبوط في المطارات والتزود بالوقود وبيع التذاكر.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76287" target="_blank">📅 16:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76286">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وسائل اعلام تزعم:
إسلام أباد ستعرض يوم غد على واشنطن نقل اليورانيوم الإيراني إلى بكين تحت رقابة دولية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76286" target="_blank">📅 16:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76285">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MS0f9XH6xjH2Dp4pdPN2atZA3TiU9dvAaLGI-dlfBPYFB7Bfd3eExb79oZ-p3Yxu9pzeGK5QdYBaMTgoGxpVFJ6AsJuQCE7nxUV8CST18J5_ZFQIMGadfqsgNLqJEyPHs2fuZ3EFiB1SAUAt_5jgDv-dJxsn7Lf1guaLglTs2lE8plGsPg58wyHe_PCdizxk7eBxEnU5RmKwL1yLhcJqSgZe5_3JjRuv7wXBvKE2AbSUv5fhnh00_fqJAEXo6MdPDVoRsg79Tb3ZCdhMEA2Nu1fKVEnz3ZDtVU8EN1TXeCqxF6N5plv6UJw0qDYavoA9A_NDCrJyW-KLpKWlkiR0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قيادي في حزب تقدم يدعو لمقاطعة منتوجات المدعو بـ(ابو جنة) بسبب حلفه بـ"الامام علي"!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76285" target="_blank">📅 15:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76284">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26db9455a5.mp4?token=BbwF15pAIY9cqn6sD3NpuWMwlaAsWy7I-p_ZBRf3zYSYEdWKDA54Oalf5e9V381Rwx3YkvX97l0avr_8o3ECl7sUijjhzH91x5nowN1oR0CTe7w8V_bU37BblnJ_oo1UfDDpmvYI9c_XhmVFC3TuZjAAm5degdZ08wJp1Bxd4PjRHWVlxamCjoAM9M7AvMix5tFqjlYacOvrujNRM_GZHhtt6ZyiqXrtey68Oy6hTCIZ1ES-CK732S6FqE40uVnw053SyyofkDglRCIydMXD-4UPa5w0L92eqMDMYR2oysw0Osm1CDkFVmEFYgzxiAjgHXDRjTHXsQkWCbCofgFEOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26db9455a5.mp4?token=BbwF15pAIY9cqn6sD3NpuWMwlaAsWy7I-p_ZBRf3zYSYEdWKDA54Oalf5e9V381Rwx3YkvX97l0avr_8o3ECl7sUijjhzH91x5nowN1oR0CTe7w8V_bU37BblnJ_oo1UfDDpmvYI9c_XhmVFC3TuZjAAm5degdZ08wJp1Bxd4PjRHWVlxamCjoAM9M7AvMix5tFqjlYacOvrujNRM_GZHhtt6ZyiqXrtey68Oy6hTCIZ1ES-CK732S6FqE40uVnw053SyyofkDglRCIydMXD-4UPa5w0L92eqMDMYR2oysw0Osm1CDkFVmEFYgzxiAjgHXDRjTHXsQkWCbCofgFEOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
‏إذاعة جيش العدو: شكوك بشأن نجاح عملية اغتيال علي الحسيني قائد وحدة الصواريخ في حزب الله</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/76284" target="_blank">📅 14:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76283">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">إعلام العدو يدعي : اغتيال علي الحسيني مسؤول الصواريخ في فرقة الإمام الحسين</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76283" target="_blank">📅 14:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76282">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/704b0794ee.mp4?token=BHvCZhgZ0wMm1L4hAwfEjLun91GtipEy98O7hvi2ISefprkaGqW7pJCovt5HSGmES3tgZHlZkRKtzu-vq0gFzUcXayAxPEou3nM_n94iu-c8cnym6Q_4u_3MI9ugA2Xa16F1Ql37XioPQjimyO0xojPFVK-1grsMuDeN5tx9a-esMVGegQdYB8pbDlGrP6vSKO1PfGYKjnnBw1NA7yMQvmwvBmBcghQcUF2lYGWOkHH856pruvkdDoi2SQNvw-KqiPB11mjvdtGqpfmV1GfOw1xrautSQ0r-y-55jSp7KZH7qu9TEm70MIabe7Ez8ElvGJLpoeN2gSe9lypn5dHnZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/704b0794ee.mp4?token=BHvCZhgZ0wMm1L4hAwfEjLun91GtipEy98O7hvi2ISefprkaGqW7pJCovt5HSGmES3tgZHlZkRKtzu-vq0gFzUcXayAxPEou3nM_n94iu-c8cnym6Q_4u_3MI9ugA2Xa16F1Ql37XioPQjimyO0xojPFVK-1grsMuDeN5tx9a-esMVGegQdYB8pbDlGrP6vSKO1PfGYKjnnBw1NA7yMQvmwvBmBcghQcUF2lYGWOkHH856pruvkdDoi2SQNvw-KqiPB11mjvdtGqpfmV1GfOw1xrautSQ0r-y-55jSp7KZH7qu9TEm70MIabe7Ez8ElvGJLpoeN2gSe9lypn5dHnZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
أنصار الله الأوفياء الفصيل العراقي ؛ يعلن عن استهداف قيادي بالحركة على الأيادي الصهيو أمريكية في محافظة ميسان جنوبي العراق .</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76282" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76281">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ضربة جوية قرب مطار بيروت</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76281" target="_blank">📅 14:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76280">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/406121fc42.mp4?token=Yd9urpKGJOG71VlqyA_3wkGbFtfN0rolfrF91UM4-zMydn1vsAWb_F07TMWj3dX3v2JOYI3fCXD79VGndPr4HxvQhGHBTWld0EhZ61nyOhsPJqLaTgDSGoWxGqwqn5sTjPGWq3_wMZEYGP-VwMVqPZyj-VcPgCLMW87eXbahE38gYbhh3PxK6Ou_Es6KNYY5xf9q_Yqufbz9-F5ESGwK0_k2_sKA0poo3I3X4tETC3uzyl1XWwdqaqj7U9ZaOnevbd5Oo4qkY4jFT9EU2MiZa5L6XAszZ0gJHvTJyWA9UAkjEUwTFqpTisq6Mx3Yd2SWxqJtUiSYUoTx1ftgvixxHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/406121fc42.mp4?token=Yd9urpKGJOG71VlqyA_3wkGbFtfN0rolfrF91UM4-zMydn1vsAWb_F07TMWj3dX3v2JOYI3fCXD79VGndPr4HxvQhGHBTWld0EhZ61nyOhsPJqLaTgDSGoWxGqwqn5sTjPGWq3_wMZEYGP-VwMVqPZyj-VcPgCLMW87eXbahE38gYbhh3PxK6Ou_Es6KNYY5xf9q_Yqufbz9-F5ESGwK0_k2_sKA0poo3I3X4tETC3uzyl1XWwdqaqj7U9ZaOnevbd5Oo4qkY4jFT9EU2MiZa5L6XAszZ0gJHvTJyWA9UAkjEUwTFqpTisq6Mx3Yd2SWxqJtUiSYUoTx1ftgvixxHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربة جوية قرب مطار بيروت</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76280" target="_blank">📅 14:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76279">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ضربة جوية قرب مطار بيروت</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76279" target="_blank">📅 14:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76277">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
جيش العدو الامريكي:
في الساعة 10:17 مساء بالتوقيت الشرقي يوم 27 مايو، أطلقت إيران صاروخا باليستيا باتجاه الكويت حدث هذا الانتهاك الصارخ لوقف إطلاق النار من قبل النظام الإيراني بعد ساعات من إطلاق القوات الإيرانية خمس طائرات بدون طيار هجومية أحادية الاتجاه تشكل تهديدا واضحا في مضيق هرمز وبالقرب منه</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76277" target="_blank">📅 14:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76276">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیام_حضرت_آیت‌الله_سیّدمجتبیٰ_خامنه‌ای_رهبر_معظّم_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">131.9 KB</div>
</div>
<a href="https://t.me/naya_foriraq/76276" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📖
متن کامل پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم | ۷ خرداد ۱۴۰۵
🔗
https://farsi.khamenei.ir/news-content?id=62984
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76276" target="_blank">📅 14:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76275">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">#ترفيهي
الأمين العام لمجلس التعاون الخليجي: ندين بأشد العبارات استمرار الهجمات الإيرانية الغادرة على دولة الكويت
جا وتهديدات ترامب لعمان؟
😄</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76275" target="_blank">📅 13:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76274">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇳
الأمم المتحدة:
معلومات تشير لأن غارات إسرائيلية بما فيها على صور والنبطية أدت لمقتل مدنيين بينهم نساء وأطفال.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76274" target="_blank">📅 13:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76273">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af565a9037.mp4?token=JcIzXsJ6paAFYi2RANVfTAmmmvY7hRD1iWVSiqd3t2f9o7yAvndTI8u3TcdRC0kdAZNeK-FiZkNQV2y-O00tPh47qw71zrv3ueFbhqo3HerfEpALufTiuVk1vEl1Sod5VXxmacE6FZd4wSrRmCbd91OPyvDvqsWXi9aCDs6sjLGJsLNGtxc1rX0pbjtE0c5myAro8KFRa7PcPQyXmtebFnM9zI2_CZx2LW-HUXOL4F55CkqFaZ28SYVaRpAX-XIVAy4Xb2NebMIsNw3uXQM9kMMk8_ghOqhlwwTgVXMtN-QjFJ7v1pymNs5rV7PgRj4-xbnxShdbD5Ndfi7WES4Tlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af565a9037.mp4?token=JcIzXsJ6paAFYi2RANVfTAmmmvY7hRD1iWVSiqd3t2f9o7yAvndTI8u3TcdRC0kdAZNeK-FiZkNQV2y-O00tPh47qw71zrv3ueFbhqo3HerfEpALufTiuVk1vEl1Sod5VXxmacE6FZd4wSrRmCbd91OPyvDvqsWXi9aCDs6sjLGJsLNGtxc1rX0pbjtE0c5myAro8KFRa7PcPQyXmtebFnM9zI2_CZx2LW-HUXOL4F55CkqFaZ28SYVaRpAX-XIVAy4Xb2NebMIsNw3uXQM9kMMk8_ghOqhlwwTgVXMtN-QjFJ7v1pymNs5rV7PgRj4-xbnxShdbD5Ndfi7WES4Tlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
‏
الشرطة السويسرية:
3 جرحى جراء هجوم بسكين في محطة قطارات بمدينة فينترتور.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76273" target="_blank">📅 13:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76272">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷
كلمة لقائد الثورة بعد قليل.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76272" target="_blank">📅 13:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76271">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">📰
‏
رويترز:
تقارير للبنتاغون كشفت عن استهداف قوات أميركية عبر بيانات تحديد المواقع</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/76271" target="_blank">📅 13:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76270">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">📰
اكسيوس:
إدارة ترامب تعقد تدريبات عسكرية لاستعدادات محتملة في حالة حدوث فوضى في كوبا</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/76270" target="_blank">📅 13:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76269">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58cd922a9d.mp4?token=ECnieslKewjut72RHSEEpScOF5C5DKgzrEctpMoAKV0B0Rt0UubIBRl_9FZBXjF6Vajk7h3zRZYL5kAlggCwHsq9Yg0LlFd6BpRg2lW8x6XNQcyCrzTamGNWCw8dNbz51lqCOCX_ON8qkfGsO0Dv8sQ3uxyXYpPuHboPeMY5EstlCQ-Fi8w483MRqK4hgSFj7MM2xk8oncb8TTT5F6Zhdc1a8iwHrewi9q6pb0UMLG3UeWowjA6U2sAC8RniLJNzq1VKrbaXJO_fp0svKMHDudH7u4rHI5LA7GmQ5B8Jbqn041eXZiUa3rBwvbtDjT69TDQ5hzDYeCj-BhunNqFdWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58cd922a9d.mp4?token=ECnieslKewjut72RHSEEpScOF5C5DKgzrEctpMoAKV0B0Rt0UubIBRl_9FZBXjF6Vajk7h3zRZYL5kAlggCwHsq9Yg0LlFd6BpRg2lW8x6XNQcyCrzTamGNWCw8dNbz51lqCOCX_ON8qkfGsO0Dv8sQ3uxyXYpPuHboPeMY5EstlCQ-Fi8w483MRqK4hgSFj7MM2xk8oncb8TTT5F6Zhdc1a8iwHrewi9q6pb0UMLG3UeWowjA6U2sAC8RniLJNzq1VKrbaXJO_fp0svKMHDudH7u4rHI5LA7GmQ5B8Jbqn041eXZiUa3rBwvbtDjT69TDQ5hzDYeCj-BhunNqFdWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇸🇾
توغل اسرائيلي قرب تل الجلع بريف القنيطرة جنوب سوريا.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/76269" target="_blank">📅 12:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76268">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏴‍☠️
دبابة ميركافا صهيونية تحترق بصواريخ حزب الله جنوب لبنان</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/76268" target="_blank">📅 12:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76267">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZryxdDBXLk5B2OuX3B9IyeNuxEjMsfm_dJw8u5_FWn74UiNycUFQ99P-IbFMuOSI4iZqJbwF556Eitcvl6jxSew1cSYvsbjVKiAvpfUdWyc1aZewzje7ORbT0ynmCYzHeAJ5knLqKm7_ZUgQOLdG0RkUBLGPQ5Ws8B4sSyL0GXK-Th1fNczmTySO9JLbZ8v2bBlJRVoPX0F-OWGIBcXwZg0as1FvhgibmglV2hykqJVjj-Dyt4pkELplpuUvTlioxbDoaWzAES1f4Psj5F25ACZbzEon0XqHO_Mb3t8mIm0tKcv0flyS4jNK3fPzGXXibCgHTu3cSrNjk2dkOwuypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
قناة العالم الفضائية تنعى مراسلها السوري "حسام زيدان"  شهيداً في غارة اسرائيلية على صيدا جنوب لبنان.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/76267" target="_blank">📅 12:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76266">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDJKYV5u561xOcyqL9znWgysTC9sMaYcTnmsgecYZqR72qmZcmWIYdT2_bsl-0EKk-J08r6jIuDGFpQRIV1g2j_-71BVKT2HvNyGtOoTjfJeDgXqD92rdbsadGi6FcWEN-NX7WoeVeGqRHeFDlZG5yiNF7u4l6uqBjslKqUAxVCrC16S4uAP197ef1NX_sg-T4sa4wfMgaB1-id4W9t9b8q6JoTUU2XJfybE65yEvDHNLUC_DItaxtINq-peRGzyRDr9cT0iVB_e3WcEvtQ2JrSI1zrmTSpB5W0bTO-MLQJW4yClUUTknqLskF7l3TT6Z9UT2EImqrh9w5yG4NlwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يعلن انفكاك سرايا السلام عن التيار الشيعي الوطني والحاقها التحاقا تاما بالدولة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/76266" target="_blank">📅 12:10 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
