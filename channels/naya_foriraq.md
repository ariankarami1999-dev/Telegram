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
<img src="https://cdn4.telesco.pe/file/t6sHVkbFB9jMlCFu-QcbGY2jnBNDTaAAZhDzN5BG3BgE9m8ebj8c_BlLsoX6mEHkJHvEmU86Jl5LdEIYWKrj479GeAb2t0u50kojIaYW1P2DhsyWzoo_X-iotj28crtKGg2rvvP2rlfEh-wTb-jt7CaRzQPRnVm2pnEiOm0ynlSdbrAGx70hsRbVQRHAOuxMwU8JRAJ2LNyIJLIV6F2zG0TqbyGODaOqY9hS7zynaYoJNFMyb4mh4Axn0RP0PV1L5UYJclSpIjGcT7HIAhuNncya_IwsSGLStuN8v7tjEG_zGkgZxLgPrNfxKIH-FzQnbbV5LwxC4baauCRzAsm9Ug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 02:55:44</div>
<hr>

<div class="tg-post" id="msg-86697">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvGSC4w5DZxydQlypRb75MxIM-QcYRt0rysoeKWkPk4JlnDIbl3SFv0AUUTr1ZgVcMhWi_hmOONhErE0RwnV4BYYpUPSTnKahHxa6Y7AihSgpOW7wAZ1_tljJ-sqcXIF_t6xvxxBRj35HCNsnKkmXMewbg4JIXtlPoU4PzK41kqcC4vXidRMailwd34J6VngeV1YmI03_DI5wXej0qIEzzFbBzuJDOoIfB2WGuCDreHs1HGhz2PgQouvVgCsLrnOTIJB_wfkhBgQ2Jbh689QONK_gtn-pntcIZzzJrI9g-ZTnLaRxKC7XeJE4LwMNpuCQRK85P2iVE_dQ_RavQdVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب ينشر غلاف النيوزويك بما يتعلق عن فنزويلا علما انها التغريدة رقم ٢٩ خلال ٢٤ ساعة</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/naya_foriraq/86697" target="_blank">📅 02:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86696">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجارات جديدة في أربيل</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/naya_foriraq/86696" target="_blank">📅 02:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86695">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجارات جديدة في أربيل</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/naya_foriraq/86695" target="_blank">📅 02:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86694">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">لحظه اصابت پهپاد انتحاری به مقر تروریست‌های تجزیه طلب در السلیمانیه عراق</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/naya_foriraq/86694" target="_blank">📅 02:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86693">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=TcfOpBAUhbB_9LVNZhv3qac8TjDNkgM3qn8O4lYGIIejmqTcmBUXPrr4wGpe-07rZjDrXGazNnXitUnPXyBIQl8Fv3wDFtPHlUVvSDWmSXiqHc-0p6BN6KfK_h1s-0FHOAcmirSJVm5ZZWGlRUta6jM0tPpLYARABj5Cof1cyKaOv70zDVGLp2jXg34VQn5rcmHfpjMwFpWS_fW5yF50t1by4wDi2f4AregHmZ3sM1jbQHjRX1pHZUnuMTitwFa_VRLIKgykeHqAw53ONdziEkDOaT2Vymaqz_Ku9boFvZYNyPJC5iyHKAzUY2gwu7GDJenX_AFK4GrPIfN5LEnMMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=TcfOpBAUhbB_9LVNZhv3qac8TjDNkgM3qn8O4lYGIIejmqTcmBUXPrr4wGpe-07rZjDrXGazNnXitUnPXyBIQl8Fv3wDFtPHlUVvSDWmSXiqHc-0p6BN6KfK_h1s-0FHOAcmirSJVm5ZZWGlRUta6jM0tPpLYARABj5Cof1cyKaOv70zDVGLp2jXg34VQn5rcmHfpjMwFpWS_fW5yF50t1by4wDi2f4AregHmZ3sM1jbQHjRX1pHZUnuMTitwFa_VRLIKgykeHqAw53ONdziEkDOaT2Vymaqz_Ku9boFvZYNyPJC5iyHKAzUY2gwu7GDJenX_AFK4GrPIfN5LEnMMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احتراق مقرات الإنفصاليين الأكراد في محافظة السليمانية بعد دكها بالطائرات المسيرة الإنتحارية.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/86693" target="_blank">📅 02:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86692">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4fbc9a29.mp4?token=OHC-_9Roo4YopZNLeHTlaZX31WMNn9TtdisjoQI_DB3DKyAjVhyTqi67bT2aKOVqxGJtqaZ-uxmq5BEHFEazJ7RQowt7Ca3ssWm-a86EepyCKlRtD3djQ1U_lkftY3nqIRosYu6U4rF_clsBiYOtcL6d2E5sL1foqslXkZb0GWIL4QwzaPnd3qD4R0nIt01OKnsTTpDt_H9MSCvJoJSXgXzTZT2OrwYCCpkY1Em4DVqJtntrdW-lP_oy3NL-VH1bf-74rBorYW8NDI4TM8HN6ejDEoFg2ZEIonnUPXHssViZeMVw3xQm2qOHGDQ-EssPVFTBxb6RiU5jSzlemcopwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4fbc9a29.mp4?token=OHC-_9Roo4YopZNLeHTlaZX31WMNn9TtdisjoQI_DB3DKyAjVhyTqi67bT2aKOVqxGJtqaZ-uxmq5BEHFEazJ7RQowt7Ca3ssWm-a86EepyCKlRtD3djQ1U_lkftY3nqIRosYu6U4rF_clsBiYOtcL6d2E5sL1foqslXkZb0GWIL4QwzaPnd3qD4R0nIt01OKnsTTpDt_H9MSCvJoJSXgXzTZT2OrwYCCpkY1Em4DVqJtntrdW-lP_oy3NL-VH1bf-74rBorYW8NDI4TM8HN6ejDEoFg2ZEIonnUPXHssViZeMVw3xQm2qOHGDQ-EssPVFTBxb6RiU5jSzlemcopwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي بإرتفاع منخفض يحلق في سماء مدن إقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/86692" target="_blank">📅 02:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86691">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7615a3c5e.mp4?token=OQMcRPVwpx7XY2FKL6jQtQit4d96Ud9BSOfS7CFDg1x3QyXdT95bR-fmbpgNkjbgb6cvgXnhsFDCkJuYLhr-YaIIOM6ZJI5R73xK4jmU-ERyM-4ZSydI5lN8iE2Von_ZtOVQoKRVarIAAz1tOlM-ZoqC8ajuiW9rPS9GkqmZNuIxVqq0y9F35waW9UK-Volhaovpn8POp9vGpG_-3nS5tM-lWgo8pQXkWlXSI73-dF01a5-vo5_NXyn1aqXDXEw16pzrJsgZarOeNolUBwbVNoKyUQ1Lph04T0DGdPvNc3l9TKIybeOIMNkG1B3F4AwIPQcf-z8zvwoTT57GsLMARA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7615a3c5e.mp4?token=OQMcRPVwpx7XY2FKL6jQtQit4d96Ud9BSOfS7CFDg1x3QyXdT95bR-fmbpgNkjbgb6cvgXnhsFDCkJuYLhr-YaIIOM6ZJI5R73xK4jmU-ERyM-4ZSydI5lN8iE2Von_ZtOVQoKRVarIAAz1tOlM-ZoqC8ajuiW9rPS9GkqmZNuIxVqq0y9F35waW9UK-Volhaovpn8POp9vGpG_-3nS5tM-lWgo8pQXkWlXSI73-dF01a5-vo5_NXyn1aqXDXEw16pzrJsgZarOeNolUBwbVNoKyUQ1Lph04T0DGdPvNc3l9TKIybeOIMNkG1B3F4AwIPQcf-z8zvwoTT57GsLMARA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد أخر للهجوم بالطيران المسير الإنتحاري على مقرات ومعاقل الانفصاليين الأكراد بمحافظة السليمانية</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/86691" target="_blank">📅 02:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86690">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
دوي انفجارات في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/86690" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86689">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50695baca0.mp4?token=LIHYhZmLTMZZh3lZlEy5yq2Eudb8-YIuKo9myTbxzJMZekG52wzLtdt9Np17Z8ALvLoaESfSN_vZ4Gb_5H1jLkuEA85vURWsRcJodXa4LrmsAOODo4Q-Jix3LFcQY_lwpVWaBJOEZJA1ZXD9BlJ7fTMFFnZFjTCNgtzV4kCDCG_jnFLbMhd9UCtttSMoUucon4F4HBS2oqFBC8m4oLuLQuphU9-UpqB7ZRDq_ke_XYP4g-p9TJt817leIn5F_FpWog2rXxOtRJ0GY5Wbwh_ImJhUedT1EJDd1jMYmu9wXLRc1V3p4F60_LcVxeT3nRM5goh0Kst8G2dg8LtN9L1P3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50695baca0.mp4?token=LIHYhZmLTMZZh3lZlEy5yq2Eudb8-YIuKo9myTbxzJMZekG52wzLtdt9Np17Z8ALvLoaESfSN_vZ4Gb_5H1jLkuEA85vURWsRcJodXa4LrmsAOODo4Q-Jix3LFcQY_lwpVWaBJOEZJA1ZXD9BlJ7fTMFFnZFjTCNgtzV4kCDCG_jnFLbMhd9UCtttSMoUucon4F4HBS2oqFBC8m4oLuLQuphU9-UpqB7ZRDq_ke_XYP4g-p9TJt817leIn5F_FpWog2rXxOtRJ0GY5Wbwh_ImJhUedT1EJDd1jMYmu9wXLRc1V3p4F60_LcVxeT3nRM5goh0Kst8G2dg8LtN9L1P3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نيران واسعة تشتعل في مقرات الإنفصاليين الأكراد بمحافظة السليمانية</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/86689" target="_blank">📅 01:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86688">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1545bf6dd.mp4?token=BDmAtAbKF4PIhCsFuoHnbtpu_Wq3dtjhflBKPUh-TG2LKOu6OWgU7DBnRuFiVSos5LwpFyM7IsROWX5Sp7RiQt-Xrm2gVwZt-VyYuvpsYL5ka0iuZWU_dS8rIIhpyKhC9sw2OJbHKsslnOzioNls7CTppQ7Gw3JvqbqBEOQFL2e_0ijIaT8zqzwdzGwAyyIqPTwbIIhhBoqzySxSk2li4Y3Pvb-qQtq0EAVE8wDrMrDLh64E7KzvGD-JFEKF72iS2coYjDkL0iHP4njHGEwNYFXuuam3aO1iuUk3sdKSaiwan806aX-aYriGuawXqAeP3MnzKDAEU2QHZXzZKM2rLqfPLa17EtkXE2xdxov8ZDadXmxFtVvJ4E9qzTSztrtOhM6mB4LRaf2s0xUU5ZTKigvKPWtYaAAosDLwhQUuljmOdnZHpCVTMi6POGvX04xydHVMHY07xfLtiG8rOtUWbQv62qrThEoeZhlBDoAb5bcKSuS1-CAFaKlYLfoYukleYJL-6ho7W2AaiRq0LgcgA3aR_dXx5OrIPMwppW-RTX62j3R9-LVdgA6fKgpQNtAJfAVhgQmlafsQG8QuFLDhdUOrA7c97idEyNZ7CtzI6N9R1xdEAK6D89WbOhLGq89Ek-fYwvlg1sKm6V28Njgy385c7Aj-Hv8H9QsIAJEgLvM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1545bf6dd.mp4?token=BDmAtAbKF4PIhCsFuoHnbtpu_Wq3dtjhflBKPUh-TG2LKOu6OWgU7DBnRuFiVSos5LwpFyM7IsROWX5Sp7RiQt-Xrm2gVwZt-VyYuvpsYL5ka0iuZWU_dS8rIIhpyKhC9sw2OJbHKsslnOzioNls7CTppQ7Gw3JvqbqBEOQFL2e_0ijIaT8zqzwdzGwAyyIqPTwbIIhhBoqzySxSk2li4Y3Pvb-qQtq0EAVE8wDrMrDLh64E7KzvGD-JFEKF72iS2coYjDkL0iHP4njHGEwNYFXuuam3aO1iuUk3sdKSaiwan806aX-aYriGuawXqAeP3MnzKDAEU2QHZXzZKM2rLqfPLa17EtkXE2xdxov8ZDadXmxFtVvJ4E9qzTSztrtOhM6mB4LRaf2s0xUU5ZTKigvKPWtYaAAosDLwhQUuljmOdnZHpCVTMi6POGvX04xydHVMHY07xfLtiG8rOtUWbQv62qrThEoeZhlBDoAb5bcKSuS1-CAFaKlYLfoYukleYJL-6ho7W2AaiRq0LgcgA3aR_dXx5OrIPMwppW-RTX62j3R9-LVdgA6fKgpQNtAJfAVhgQmlafsQG8QuFLDhdUOrA7c97idEyNZ7CtzI6N9R1xdEAK6D89WbOhLGq89Ek-fYwvlg1sKm6V28Njgy385c7Aj-Hv8H9QsIAJEgLvM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عنيفة وتصاعد النيران من مقرات المعارضة الكردية في منطقة طاسلوجة بمحافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/86688" target="_blank">📅 01:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86687">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0164d5015.mp4?token=RXo8G3TZW21m4EjoHnKtS7IkMR2qwI-zOTMcK8LUOnBM8_YxdS-EMX1tzPpFto2IbEyMA7rXiuk140frPCDczXGV5PJ6K8HuXLGevn1hS_dn0NFxXKUwVU_UzlKI6KPo4vjZtkBPAY-gz_fcCBoptCh8fZhQSsj2IBLCspgNAVJSYyqQbqbaHluY7Opo-OMeKFxORWDfmeY-IJSuBdIXT7sz1qqLGErcM3572Q5whNbpMIJsVciqx6CcHlW2YeAfmmsADJ3FWz5o-2kY7JL4Vhq-Q1gNQc5dTElj0boIarhH6Oshy514vO25sJfGglWgc3tiuFq6tUifOX9Ym3uVUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0164d5015.mp4?token=RXo8G3TZW21m4EjoHnKtS7IkMR2qwI-zOTMcK8LUOnBM8_YxdS-EMX1tzPpFto2IbEyMA7rXiuk140frPCDczXGV5PJ6K8HuXLGevn1hS_dn0NFxXKUwVU_UzlKI6KPo4vjZtkBPAY-gz_fcCBoptCh8fZhQSsj2IBLCspgNAVJSYyqQbqbaHluY7Opo-OMeKFxORWDfmeY-IJSuBdIXT7sz1qqLGErcM3572Q5whNbpMIJsVciqx6CcHlW2YeAfmmsADJ3FWz5o-2kY7JL4Vhq-Q1gNQc5dTElj0boIarhH6Oshy514vO25sJfGglWgc3tiuFq6tUifOX9Ym3uVUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالطائرات المسيرة الإنتحارية على مقرات المعارضة الكردية في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/86687" target="_blank">📅 01:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86686">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKq3J2jZMHYOki6RjunMJvsNLuIgMjLrhzXzIQoXzkdXStLCDqTz9tSEu7Hdzbe4uS-pshuNit5SgqXhFdIgT9McOG8T8WoLlV34lMxIRegcXrRcy1WcxNeP7ffgSKvjn4t7ZS5igUACS-qDsmIPzi1SmRGvomQfBJNfO7VlDbZWi5gPBBcwpnyDxS_4VAB-S90ZUWgAg_4tZHJDVgQBdHHfYsuvMMjKLfAHlf1Cn3SjT9Kx0J4jNEecgL4ympzgVy7x0TIdpaeNH6SPzie0HiuPeTAs5_4wGtXCaFZMXY2gFBXHvFv3Sp3TG2ev6C2oNn-_PgLk2j-3H5WKrx_CxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران حربي مكثف على الشريط الحدودي العراقي الكويتي الإيراني</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/86686" target="_blank">📅 01:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86685">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هجوم بالطائرات المسيرة الإنتحارية على مقرات المعارضة الكردية في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/86685" target="_blank">📅 01:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86684">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlV9dafseippQhSHJ-eyEpwJuShQfCHCyFcHzJTWhN0JlIknE9rVYZYHNGF_sxvmbQ_dExXPcv8T6SM8q5qpaUVwzQlr8vCk5-6NChC6toLcFroI8QucICy4ZdtvK5sjyqAy1-5MjuSqrkvB2Ya3A_Frm1_wxCMOZxRhkwHByBNLKwYh5hIQKyUpO1vIOxYGk1awXzMJ9mM95G1KLzyprY7vPGTu6tT_TwjXaMLvFbjaSnna7j4eOvPetjLgXvEQaIwlZOMtiboEaUqQRevYzA79rDsLJXa9H2cKvicQyFfsUfQhe0nDXBPVbbX95Cc97btmbT48KuO2TAH-sCwCRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاثنين يوم الأحرار بموكب قادة النصر</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/86684" target="_blank">📅 01:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86683">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe5171ef4.mp4?token=SfMWuTe1WXrFPgxCkfrCVKvFEVyIZGkp5mZHVrCcPsvrAXc3RG2DWbp_nnM7HU7mzHrZpleDH-yb53jKM_70GFrMGzx1SGb8nzWfXmUBq9KFJLrUl7eZ0w4G6QQQMmA2wbPfdSe_ReTBlDuNre07QciQf43JVtJpOWsOSnxxkoKIji_w1r8rE9r8nRG-Zp-GE6TcHjP7TwISQ66_uQYvmGJR4HGm22h0QCptk4mdkS7qDEj1_WV-s02CCsr3ETImDj2J8USLJTG5kcsMqlhaASQ5MmxqST-WFm4bvr_Iw6mdrYgo4EBbo3rtwVrdJKEE74lR-Xg6WPFxOp53474-mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe5171ef4.mp4?token=SfMWuTe1WXrFPgxCkfrCVKvFEVyIZGkp5mZHVrCcPsvrAXc3RG2DWbp_nnM7HU7mzHrZpleDH-yb53jKM_70GFrMGzx1SGb8nzWfXmUBq9KFJLrUl7eZ0w4G6QQQMmA2wbPfdSe_ReTBlDuNre07QciQf43JVtJpOWsOSnxxkoKIji_w1r8rE9r8nRG-Zp-GE6TcHjP7TwISQ66_uQYvmGJR4HGm22h0QCptk4mdkS7qDEj1_WV-s02CCsr3ETImDj2J8USLJTG5kcsMqlhaASQ5MmxqST-WFm4bvr_Iw6mdrYgo4EBbo3rtwVrdJKEE74lR-Xg6WPFxOp53474-mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
إندلاع اشتباكات بين مسلحين وعناصر الأمن الأمريكي في ولاية أيداهو الأمريكية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/86683" target="_blank">📅 01:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86682">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">طيران حربي مكثف على الشريط الحدودي العراقي الكويتي الإيراني</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/86682" target="_blank">📅 01:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86681">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8414b56.mp4?token=mC5XzySRiQl9tNyV5DVi2pLThB3zo4LSl-cNoa3x-RdX8pL4JpTGdRrwwxKcBteXuuWt6EILgeJjiCTQcWMo_uUW3QJEnZ4AhQDx7oxWDl7rlbb9SGQKQe8tO5dtwX_Io1fLiaqPMujIbuBJRSQm7nXfYbSdkMpEV-o-PUeJosqc9RYOSdcxTcvhP6R-d4EB4KbUk7Ig1ht_5WXctpadYdGjnl1Zz2K9W0fj96YWsPRcFEXop5hTgY3DrpR88VTR1ilNTI-8viVoD4K57JhW4YGZF11fJbIeypEIvtgk1N3LRVwPCyui-a965J9l4GQJwpZuQNFxIDg6Y1iq53hxHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8414b56.mp4?token=mC5XzySRiQl9tNyV5DVi2pLThB3zo4LSl-cNoa3x-RdX8pL4JpTGdRrwwxKcBteXuuWt6EILgeJjiCTQcWMo_uUW3QJEnZ4AhQDx7oxWDl7rlbb9SGQKQe8tO5dtwX_Io1fLiaqPMujIbuBJRSQm7nXfYbSdkMpEV-o-PUeJosqc9RYOSdcxTcvhP6R-d4EB4KbUk7Ig1ht_5WXctpadYdGjnl1Zz2K9W0fj96YWsPRcFEXop5hTgY3DrpR88VTR1ilNTI-8viVoD4K57JhW4YGZF11fJbIeypEIvtgk1N3LRVwPCyui-a965J9l4GQJwpZuQNFxIDg6Y1iq53hxHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
إندلاع اشتباكات بين مسلحين وعناصر الأمن الأمريكي في ولاية أيداهو الأمريكية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/86681" target="_blank">📅 01:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86680">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/462eed6d8c.mp4?token=PUYBSKfi_MmspPhYK1i6rcqNuyd-h36fn2IIe4X8iigDNflBBftauQTwE-h4nhF2Xz1GtHS-pE1KRUv9P1kpjrP0RwWO8b6PqSfVFqIHDzxAAn9EUUJ-RjZW1Wu2chGIBvXymH0xJ_ZAUajse9LxNj1_m8Sl03RQkOUmcl7DRFFntpkPpVY5BMru0mcAdxx7l86lGXnkLI3SA-ILDvAgUWRxqDYxAhVRNFttbUWU9vR-RbcDwq2cBQdVO_vH_emQiYXRKBB1jJG3blwIKlFf_0DyFcyNI7xFi17sBodvx4Mh4LNJZp7HnKZaaFYt3-zEmYG9gWByU4WdhUZfvm51_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/462eed6d8c.mp4?token=PUYBSKfi_MmspPhYK1i6rcqNuyd-h36fn2IIe4X8iigDNflBBftauQTwE-h4nhF2Xz1GtHS-pE1KRUv9P1kpjrP0RwWO8b6PqSfVFqIHDzxAAn9EUUJ-RjZW1Wu2chGIBvXymH0xJ_ZAUajse9LxNj1_m8Sl03RQkOUmcl7DRFFntpkPpVY5BMru0mcAdxx7l86lGXnkLI3SA-ILDvAgUWRxqDYxAhVRNFttbUWU9vR-RbcDwq2cBQdVO_vH_emQiYXRKBB1jJG3blwIKlFf_0DyFcyNI7xFi17sBodvx4Mh4LNJZp7HnKZaaFYt3-zEmYG9gWByU4WdhUZfvm51_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قبل قليل بدأت مساجد محافظة كركوك برفع التكبيرات بالتزامن مع استمرار الهزات الأرضية التي تشهدها المحافظة منذ يومين وحتى الآن.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86680" target="_blank">📅 00:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86679">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9b860706.mp4?token=sHcFBb7lzpdTBNF4PhJVIs6OA_S2HEg3jJCGdvyWpboGWlNLIUfxuiXEyAVjmn_sk3Ga-ETMx-OOgMbjS8MV01xhvp-tlmx5SrFnxtiZtcZop8IJxZ00bll5D8n0s-76j-WI_w0SEZWgX3uX_hpu7auMutPYKWI0BU5m56eOMv56yMCJpKwNZYnw0cJyLvmq4ll_Ipq2qGe-hVM7rtxFc-aawerTpR1p8Ey_dTmDd9p0I6rIGeJicdRwD4LFfBtj1wMD6VqeOo_SiptZLUybO-W765OAT-LNdMDXDV2n0bv8x66Nf6aMGJVZB6iJb_F3ytiPmNamhsLNRxOiQSN1iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9b860706.mp4?token=sHcFBb7lzpdTBNF4PhJVIs6OA_S2HEg3jJCGdvyWpboGWlNLIUfxuiXEyAVjmn_sk3Ga-ETMx-OOgMbjS8MV01xhvp-tlmx5SrFnxtiZtcZop8IJxZ00bll5D8n0s-76j-WI_w0SEZWgX3uX_hpu7auMutPYKWI0BU5m56eOMv56yMCJpKwNZYnw0cJyLvmq4ll_Ipq2qGe-hVM7rtxFc-aawerTpR1p8Ey_dTmDd9p0I6rIGeJicdRwD4LFfBtj1wMD6VqeOo_SiptZLUybO-W765OAT-LNdMDXDV2n0bv8x66Nf6aMGJVZB6iJb_F3ytiPmNamhsLNRxOiQSN1iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من أمام مرقد الإمام أبي عبد الله الحسين (ع) وسط توافد ملايين الزائرين لإحياء أربعينية الإمام الحسين (ع).</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86679" target="_blank">📅 00:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86678">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accb6caaa6.mp4?token=TmrZw1KA_jagfKpAXCFNRhvUGI_pUfuLdvs5bZXAT2mYWuaI6ojEcrHY66oKSzCA8g_exYYVLaNTUPDx3yPDEpvBvhipLo07loBj72XlfmUyEwuLDC2ApprqxNNipjWbdQRVO9yNQBitWmtsFYiC-UdwmbLzwEo65SZc_cAvJxNM7OjFnlYar99SdFnVDQ0FKTAxeoO2Z8s7x7WNVdaZiP7vZ2jQAyVA9bUxdvnWZo9uIbqTnO8_tu_zz1M1BC_0ZTq8QZ4AgqQMRQjtuDhFyjHSS4wLoMH4vEfyANQBYlPLmWz19H_ahgG-WEonJQJALO0y6GEX9jHfzdgCQ8jjTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accb6caaa6.mp4?token=TmrZw1KA_jagfKpAXCFNRhvUGI_pUfuLdvs5bZXAT2mYWuaI6ojEcrHY66oKSzCA8g_exYYVLaNTUPDx3yPDEpvBvhipLo07loBj72XlfmUyEwuLDC2ApprqxNNipjWbdQRVO9yNQBitWmtsFYiC-UdwmbLzwEo65SZc_cAvJxNM7OjFnlYar99SdFnVDQ0FKTAxeoO2Z8s7x7WNVdaZiP7vZ2jQAyVA9bUxdvnWZo9uIbqTnO8_tu_zz1M1BC_0ZTq8QZ4AgqQMRQjtuDhFyjHSS4wLoMH4vEfyANQBYlPLmWz19H_ahgG-WEonJQJALO0y6GEX9jHfzdgCQ8jjTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هزة ارضية تضرب محافظة كركوك واجزاء من محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86678" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86677">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
هزة ارضية تضرب محافظة كركوك واجزاء من محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86677" target="_blank">📅 23:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86676">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4Zm3Ae8AU2WgfrWhRRrTvG4mf5Bu6k1RJTyUcRbm7DVCmtEq4Dgq03QV9lhnCT4HBZgj6ZUv0Emi0sznGZDiQe15lmVc_VFFwSouykYkEdi8MYTQeCh3rVVLUPfNG3JOJHvQ7QAdlkAG87Cv7PAn_p-k6G9j5EufW7K_EcNoRaSflRczf0HJMbHkNQkt-nS8b17fuO9pmI4sl0ugxjQoMllOPFtg555sawIx3LckYfXG79lm1EnOkXK0NcgbJq1eCfTiBwBCqie1z3Eh-oxa2qJXq-nRhXHnngCzK0fLuMrREWSA5ch4vWkYFXRb78YLddD3gLiMij6-BpzFtG-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علاسة 3D</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/86676" target="_blank">📅 23:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86675">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇷🇺
انفجار في مقهى بالعاصمة الروسية موسكو</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86675" target="_blank">📅 23:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86674">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sameUNt6gPopDn1GPsmAu0QVL01fNSk267UpUroVHJtHCGHt5EkOAEjBXJtoAL4R5byDyrxJ2cV5D1x8LVQAdJZHwCkJ3S4LP3G0HVQJ8JdodKRC9Kc2y4bDwMY9K8ijSfCF78XbM2VvOmxWs7q31KmwSbO0KesnDkq1F2ZE7E8xyXSW50Fb4P6X7WQo7x7eJY7EvWT4A7wQ_u43fK25o8qn1RnPSrCrWPF1fzhsft8Yr0E7PDlukRJVC-KYYfoZnjX8e8iQ8Onxe5zlS543u_DedDOonFp_SSJ2LOcnK_nig4fs1PMCxO2L9F72e93WsRazz_7Wsgh9Ggf9o4qECg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
لقد كانت الولايات المتحدة واضحة: نحن نُقرّ بسيادة المغرب على الصحراء الغربية، وندعم مقترح المغرب الجاد والموثوق والواقعي للاستقلالية الذاتية باعتباره الأساس الوحيد لحل عادل ودائم.
أي مسار آخر يطيل أمد الوضع الراهن وهو غير مقبول. هذا الحل الذي هو ضرورة ملحة لن يجلب السلام إلى المنطقة فحسب، بل أيضًا الازدهار والتكامل الأكبر لجميع أفريقيا.
يجب أن ينتهي هذا الخلاف الآن، وستواصل الولايات المتحدة المضي قدمًا في تحقيق هذا الهدف.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/86674" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86671">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p5wVxNoN7sFxZ5qmLirAJT5_2aYO1fsybIU8QG3QEg3-_nI3dx8Bn4cSz3bDt391VTptK0bOlwdtUhioivt7tj4o9vmCUwwvVX0k3XHc9rfsDg1rjBdyPDcDsvLz8Dt8xVYvOmk3Q5G0pidGYEemUlrgbnpNJzIFuVKSRInFBtpOc3z9gXfT3CwmqYeUF6Mf8GDpfwatg5rkZ7NOEqY0sUCElsFXOeJRRQN7tyLNC0c-0Sg1g6mi_x_gNeuAN8I9AXIjRueJiQbeYkj2J9nxBI4WiK_TrTFdkLObm-js2aGqfp1ZE4oYBPgJVeiOpLc9ggpcfc7rf6-NnYnouDDXpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CVYBDysVT_9q85DS4Wk5UqLOLDU_LbZZq0lEUzImT3eIolS5nGLfEBuYTBZxVCHTFILRcK4rFC1HSrTB5eeMyWXrmXCs1PdmNVKX_ChRIcg-62AMCF-gg9gLrUVvcPLkknPuHvrIenPQnRPm_dCy2TopqbOf4vyHsD6YtpvCG50DqyRWorUKpPlUs5mVsNkIW0gA7hlJYKyoG0OB5kcZKnh7O5eVYJjoh3l3QSe0avBILLh1kgOJlvWlHShRZyp1bHKP_BMQ6Ebvwlq3L5vBvPZzbB8XEusHAy09P2t64kQjA6Dq8mBx5o9cYetgSkn2MYBrrC5WozIGRk6QfRl6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7xXTZz0TxeK26QcUUUJjeY34PEFD5i52v_VT34xFhKtxbamEnPSretK8sBOHeRkdi-zbFAdl0LNfFIfdT7MoP-jGRkHYOW-_LbINh7tDZbFyD4maSj7UmjRB3itTj7PLVk8a368hbTOJD8if9hEXaXUmU8_5Sve4UeKB_UF4HuphAfQDszzkxCLgitVWTcsMfiyxKVPY71AJzxZS1KtzpxSwdEeTHF--qBXkCgmF6txL5JeFAlOccWbXxCU9vr9J1Cac6JjrSET4hmkxl5pvlh5vXJ_Kq3ZKp7oN5jKKRoH7KGisOpM7zVcyBOmzQAUI3MoTasmWhV9V5ZK0FsAXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية: سنستخدم جميع الأدوات للدفاع المشروع عن حقوقنا وأمننا القومي
في بيان، أشادت وزارة الخارجية بالقوات المسلحة، وأكدت على استمرار الدفاع القوي عن كيان إيران في مواجهة التهديدات والهجمات غير القانونية من قبل الولايات المتحدة.
أعلنت وزارة الخارجية أن إيران، في مواجهة التعديات الأمريكية والإسرائيلية، ستستخدم جميع أدواتها للدفاع المشروع عن حقوقها ومصالحها وأمنها القومي.
اعتبرت الوزارة أن استمرار الحصار البحري، والتهديدات غير القانونية، والهجمات على البنية التحتية المدنية، تمثل "عملًا عدوانيًا" واضحًا وانتهاكًا لميثاق الأمم المتحدة.
أكد البيان أن صمت مجلس الأمن وجمود الأمين العام للأمم المتحدة في مواجهة هذه التعديات يتعارض مع المسؤوليات القانونية لهذه المؤسسات.
أشارت وزارة الخارجية، في إشارة إلى دور الولايات المتحدة في زعزعة استقرار مضيق هرمز وتصعيد التوترات، إلى أن الادعاءات المتعلقة بعبور السفن كانت بمثابة ستار لأعمال عسكرية وضغوط على إيران.
وأضاف البيان أن إيران، في حين تدين التعدي الأمريكي، تؤكد على الحفاظ على علاقات ودية مع جيرانها، ومواصلة الدفاع عن استقلالها وعزتها الوطنية وسيادتها.
﻿</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/86671" target="_blank">📅 22:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86669">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deb2552d63.mp4?token=KTh7aqxXpxS76Z9yaHkoPDvGRqClq5FKL_gvw9rd32F5j9hZAKHdq8E2RXh-H8uI6ziJ0qFnDnJNxFHXvUkf2RFOyPZhu110dpR6P9Y6IC_ur-hoyCYyLTV6wb9-VfcXmcJUrsmYDxlLIkCU13WxFTOK19ICMBR7WHdOyr5UEvz4zrgjK31a_VenSXDdYPmhH0qNgTkSCwcIBpkcZuoDJodNLJ81rtU1D3ukPbRKMdve7xDL-qtoCITKuYyKiQ9WDWAI6LpKqePLBpJZsnY1Wr9brZTPUtRR3KVB5k3kh9QayKc0yfyrt2oJJrsRswbsn7g3_MZkYSW-Eit7JP957Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deb2552d63.mp4?token=KTh7aqxXpxS76Z9yaHkoPDvGRqClq5FKL_gvw9rd32F5j9hZAKHdq8E2RXh-H8uI6ziJ0qFnDnJNxFHXvUkf2RFOyPZhu110dpR6P9Y6IC_ur-hoyCYyLTV6wb9-VfcXmcJUrsmYDxlLIkCU13WxFTOK19ICMBR7WHdOyr5UEvz4zrgjK31a_VenSXDdYPmhH0qNgTkSCwcIBpkcZuoDJodNLJ81rtU1D3ukPbRKMdve7xDL-qtoCITKuYyKiQ9WDWAI6LpKqePLBpJZsnY1Wr9brZTPUtRR3KVB5k3kh9QayKc0yfyrt2oJJrsRswbsn7g3_MZkYSW-Eit7JP957Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ملايين الزائرين يواصلون زحفهم نحو مرقد حبيبهم ابي عبدالله الحسين(ع).</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/86669" target="_blank">📅 22:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86668">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇨🇳
🇺🇸
روبيو
: أي صراع أميركي صيني سيكون كارثيا على العالم أجمع.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/86668" target="_blank">📅 22:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86666">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92e5e813a.mp4?token=Fu1Do9SSd5-FhAVfxoItYDZlPvekWhS-0IS4j0sBDhG40jnOB1VKcY3AAp4d--Ew_JnmzN00FICwLhgHGJhTmsS2lqcDtpnSpxZYDmbuwzK84t1enT9zU_pjg-ddPQ2EFh1RnxAsT9xX6xvP16miDfFPmFvOER76RyLyEV8z3CdcGiKrUcy0T4VgxyID6UU0KC5bkcldgSgvrfd-ll8CP9U3nmW6bgtZ33HQRdXXLdXsnKil86KUJvmMloFTi2gwuw4ghrNXX6hIjzpJUsgidIgMfKbHSJfeFkGBoMzNA4SA6fFM1Xo_i_ctxfhqxERTUYpu0KIMZCxun5sQeaaPrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92e5e813a.mp4?token=Fu1Do9SSd5-FhAVfxoItYDZlPvekWhS-0IS4j0sBDhG40jnOB1VKcY3AAp4d--Ew_JnmzN00FICwLhgHGJhTmsS2lqcDtpnSpxZYDmbuwzK84t1enT9zU_pjg-ddPQ2EFh1RnxAsT9xX6xvP16miDfFPmFvOER76RyLyEV8z3CdcGiKrUcy0T4VgxyID6UU0KC5bkcldgSgvrfd-ll8CP9U3nmW6bgtZ33HQRdXXLdXsnKil86KUJvmMloFTi2gwuw4ghrNXX6hIjzpJUsgidIgMfKbHSJfeFkGBoMzNA4SA6fFM1Xo_i_ctxfhqxERTUYpu0KIMZCxun5sQeaaPrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
نيران لا تتوقف من مقرات الاحزاب المعارضة الايرانية في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/86666" target="_blank">📅 22:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86665">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9fb75e16d.mp4?token=PbbZFO1T2AdoEpPmcBw805DKA2VTIcqmo5gIZ_HhXIBQ81QT6LPZJcL1esDhbEBDkycRTomfdvUbzqjNLw6mc8jHiFiev6zJ2Qft1X5HVNKcb6ERs0nAnlpOH38gw5se4W_yl5NYdbC8aH4P3RaWbl3hkl3rwgmU3Ee0nCK7H5hLsp6Vlf-8ec3hq_O1Z2xAkEwi0zFM8ZAT6DOQu5ses0IGZTpT6fjrUXljK8vnYEkoU9Axmm1dc2tu_Dh_st6WpHqUYl2aQXVPDqJ-xVmGvH0TYkZp9hdk0YgZAIuobLD1I3Hu_AnaDmZ3mFnEf6JB00OqWLBEt0Jj7VuaiAfIag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9fb75e16d.mp4?token=PbbZFO1T2AdoEpPmcBw805DKA2VTIcqmo5gIZ_HhXIBQ81QT6LPZJcL1esDhbEBDkycRTomfdvUbzqjNLw6mc8jHiFiev6zJ2Qft1X5HVNKcb6ERs0nAnlpOH38gw5se4W_yl5NYdbC8aH4P3RaWbl3hkl3rwgmU3Ee0nCK7H5hLsp6Vlf-8ec3hq_O1Z2xAkEwi0zFM8ZAT6DOQu5ses0IGZTpT6fjrUXljK8vnYEkoU9Axmm1dc2tu_Dh_st6WpHqUYl2aQXVPDqJ-xVmGvH0TYkZp9hdk0YgZAIuobLD1I3Hu_AnaDmZ3mFnEf6JB00OqWLBEt0Jj7VuaiAfIag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
انفجار في مقهى بالعاصمة الروسية موسكو</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/86665" target="_blank">📅 21:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86664">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c42d7c0f.mp4?token=A1THh3TA_e0cr9zI6N7zAnwoOOej6eHU19BXzFudEYy4fK1V71bu-8NBP2byflpB20UEf-dw2GBKeu4BkuAoD5Y_tCKr68psXAWcCP2S9xQcHw9pJ8WzZyXzqbSWpm5rRTN9ta8wDNQS596ctkpg8sS5Zu-snwkgf-yBhTBSyx5NHiRpdHmvjerl2Zuwo8wtLZ_bVMRBGnu1v-cjLJ6Fze2VYnKTd-xZQUEBJVPs30QOh6icx7BWwDBV6dSdl8W7QPW9wBdMR-r6xyONwhfxxY9YU47A3kPvUgoj94OrKSzRayIDIhJ1JRXi3Q9kpER_pvNvZAjshvAKO5Slj08CEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c42d7c0f.mp4?token=A1THh3TA_e0cr9zI6N7zAnwoOOej6eHU19BXzFudEYy4fK1V71bu-8NBP2byflpB20UEf-dw2GBKeu4BkuAoD5Y_tCKr68psXAWcCP2S9xQcHw9pJ8WzZyXzqbSWpm5rRTN9ta8wDNQS596ctkpg8sS5Zu-snwkgf-yBhTBSyx5NHiRpdHmvjerl2Zuwo8wtLZ_bVMRBGnu1v-cjLJ6Fze2VYnKTd-xZQUEBJVPs30QOh6icx7BWwDBV6dSdl8W7QPW9wBdMR-r6xyONwhfxxY9YU47A3kPvUgoj94OrKSzRayIDIhJ1JRXi3Q9kpER_pvNvZAjshvAKO5Slj08CEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
انفجار في مقهى بالعاصمة الروسية موسكو</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86664" target="_blank">📅 21:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86663">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG98zkSwr4gljh5Wa3M3uXz73rqPx1jl3odXd68cymtjfCmtLnMDAftCTQRjBsge6vlNSRf4Thr4IhegRdMqNbDmHPqJjX0ht2CVTIXfkYphFiaj3-Wow4k2_rhQ9CpV2rZMNxMezO6ZG7Hv1e-SPaSbGT3mHlvExIg8D-HCBmrRiis9jNaKPi-ZQEVCrla-4K-qm5QwL5INe60GsfK002PZDiSAQhEIqdmfQhLLGCzuRJOfd5TPbqvKUtE7GA_ajQl0UFS7PrzqSGBIfJMLZ-yetugnvKHgCR05bXyv1r9y3RG3hGdbrmgwRXtSH8VlVpCinSrUPLhJim_xpTFVPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب يعيد نشر صورة قد نشرها سابقا مع الفضائيين
😫</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86663" target="_blank">📅 21:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86662">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU9QpWqeT-sVpEwPMFbJmHKGqrR_2tXuslvWHAEECff4cpUdYxkpDOdSQ-H25xpqiTH3qkX5sKsT2nwJkiqvP-y786oFMTxyogLMup2jqej5mX272pkCr_LWQ2cHIVHGyNqWen6r0u79s18VeFCA4krvEdjTTGY5zNLxjxIfFSFyEvrkc4Qx2_ZQ18-PUsnv1b1tUNGHWRBLpQniJzKqQy9Bivm2Wi-QYF7k7YDUpU3jsaWJ6Bia2Hg2ppBNJCxJWwl0Z61XlB32_YAHbwuhY8Dg2EJxIat0MwPCCgpriNLn_U1_6WctuD9eGwLus3OEcU3WzIJL8rXrcBEkRnyHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب يعيد نشر صورة قد نشرها سابقا مع الفضائيين
😫</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/86662" target="_blank">📅 21:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86661">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
Welcome to Karbala</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/86661" target="_blank">📅 21:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86660">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الاعلام السعودي: الأردن أبلغ العراق بمعلومات عن مخططات لميليشيات لاستهداف أراضيه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/86660" target="_blank">📅 20:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86659">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
‏الاعلام الاميركي: ترمب يدرس إصدار أمر فوري بتوجيه ضربة لـ"منشآت طاقة" في إيران.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/86659" target="_blank">📅 20:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86658">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
‏
الاعلام الاميركي:
ترمب يدرس إصدار أمر فوري بتوجيه ضربة لـ"منشآت طاقة" في إيران.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/86658" target="_blank">📅 20:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86657">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/989829c477.mp4?token=vLpgqttP9AnIWbox7OdFfviSuq1IVtmshRB3i0FMNBrTf2PgtgpqRjv1AbTaDsORJL_1tCWTwcxvWJJU0N45Vonxl33oup0ookAwB457lBSuHy0YnckgcjOmmOWo2G5F0uKL7h_9keFkCrvTijWxu_wvbgkTMdGZz6uMUD-veH2O3OQrH0QqloRAxn4LlH8bZUf_HhC6IXYJhKJY-TJUVLgTG8OhvwK0xpFmtB9Ok4lS-bFdC-gBuxv2qViqUME9OvVLib7YVXxf2nGM9Epzxkbo9sX0rgJJBQ-IU72OWqytTrSI21IcvHc76bXwxJSLB0bHm3uGcMGKQMW7WU5zLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/989829c477.mp4?token=vLpgqttP9AnIWbox7OdFfviSuq1IVtmshRB3i0FMNBrTf2PgtgpqRjv1AbTaDsORJL_1tCWTwcxvWJJU0N45Vonxl33oup0ookAwB457lBSuHy0YnckgcjOmmOWo2G5F0uKL7h_9keFkCrvTijWxu_wvbgkTMdGZz6uMUD-veH2O3OQrH0QqloRAxn4LlH8bZUf_HhC6IXYJhKJY-TJUVLgTG8OhvwK0xpFmtB9Ok4lS-bFdC-gBuxv2qViqUME9OvVLib7YVXxf2nGM9Epzxkbo9sX0rgJJBQ-IU72OWqytTrSI21IcvHc76bXwxJSLB0bHm3uGcMGKQMW7WU5zLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران مروحي كثيف في سماء محافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/86657" target="_blank">📅 20:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86656">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الاعلام السعودي: أبلغنا العراق أننا سنضرب الميليشيات الموالية لإيران إذا هاجمت الأردن.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/86656" target="_blank">📅 20:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86655">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الاعلام السعودي:
أبلغنا العراق أننا سنضرب الميليشيات الموالية لإيران إذا هاجمت الأردن.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/86655" target="_blank">📅 20:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86654">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
🇺🇸
‏أفاد مسؤولون أمريكيون لصحيفة نيويورك تايمز بأن هجمات إلكترونية إيرانية مشتبه بها استهدفت شبكات المياه في سبع ولايات على الأقل. ولا توجد أي مؤشرات حتى الآن على تعرض أي من إمدادات المياه للتغيير أو جعلها غير صالحة للشرب.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86654" target="_blank">📅 20:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86653">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119a2ee3a7.mp4?token=HF4JTHc0YGhTKLGnlqcIAjSS_7oazTikQ8gxSvc3D9KcU8blap9zeOoj1s0Egi32FovSO4XMvyqgWHAsEJGt8IKrKuLhSXG0bEqjw6RfXAYc_jxFZ623AKfpTlaPRZHj9fNk-uk99jRIrBKpcJl__UjDZYRZs-bv7Tcr8W4YHyi70g2yZV9fcUMPNwv3R4xsQeOpL8IusUmXC_tybWEw8nNtjUcLHSbCMVdLKiLHZ-7_-A6sU1p_MNwQs1MBvwnxvhevI6Wm-Tch86EDV4eHUGnZo68PIahx7qaHcanGPDPO02k6SQzJOieSu3LGTF18BDKzleGO4VmPc8EJiB3SjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119a2ee3a7.mp4?token=HF4JTHc0YGhTKLGnlqcIAjSS_7oazTikQ8gxSvc3D9KcU8blap9zeOoj1s0Egi32FovSO4XMvyqgWHAsEJGt8IKrKuLhSXG0bEqjw6RfXAYc_jxFZ623AKfpTlaPRZHj9fNk-uk99jRIrBKpcJl__UjDZYRZs-bv7Tcr8W4YHyi70g2yZV9fcUMPNwv3R4xsQeOpL8IusUmXC_tybWEw8nNtjUcLHSbCMVdLKiLHZ-7_-A6sU1p_MNwQs1MBvwnxvhevI6Wm-Tch86EDV4eHUGnZo68PIahx7qaHcanGPDPO02k6SQzJOieSu3LGTF18BDKzleGO4VmPc8EJiB3SjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب يزور القوات الاميركية المتمركزة في ولاية نيوجيرسي، يذكر ان هناك انطباع سائد داخل الجيش الأمريكي إذا زارهم شخصيات سياسية أو صار اهتمام بطعامهم فهذا يعني أنهم سوف يُرسلون إلى القتال
😆</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/86653" target="_blank">📅 19:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86648">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzHVSlKqn0xcqmz5gn8uImf0wU-MC2mlxeNZQA7hjr5Qg5Yj7MO7b-ypTVyJTka3L5-MZbx2a9ClX07Y48WK0Y7ds2ZyLGXLw2bSVbFIGaYQQxGGtCVUTUriPR67YzFLUF4izyFNrvBXKXbwnjboaKLE3-m7YeBn3RPIcM2lja9TrSzycXnD0slBK0kBBcXfcsbqbxwJM96Vh2Ct5mHUKIRKHvkmhn3JT6-QtIDV3RTfKQ181DJ4VNqtVpDPSxkVS9-e3lSUcZXIvyloUR6_8CeZRNa3vHo84A_DQec59igwWsWzW-8saHSsgqguoltySEQHL8VUV85r4LPmr8hocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYem2EzH0N368aJtqo3nZsP8mfb3C_fcuPB30npE2OwyzUkR2BN8ECn6JE9wryDO_X3Mji5oQb9STPmwYaScMp9kDx7ha1T7l73Ys96UfpsMJRjJiuLwU0nxvwlH9QKqdY1XBPJkcBfTtU3VeTmmZ4Ra5cb2M7WyB540j9K3cI5hn3LvTn6XZ5289ICtdmXvuIBWWf0wmHLI2BOJWFOZf54QeqZzfKdt6V-E31MA7HlF0CQdp2cwRPYhONVHw80aHECQFv8jf_O3KaWyMZusufd4UFHubIIWUfJ9JaaGCcJ3uxWT6slrbqtk--4owIYCwDyJr9hJf3mmqN2VA8A6mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rr-sG1zd7BvDMAbv49yNIg1Nbj8024heFOKhjStLjXbDZ4I1YXl6v1_Gufqe-_afaQfCC4BJNwSzf33ku9SiNLY0OSry41JPtigFUUeRDuA_lOsIyCH5dw_PFOmVAbS30rqyDYmYyOYdqlA3EKJntT0Wz6LZvlPsqI5LXsD6OhN03HAEPlYZLtUWWW-wABzCXbRMkW3VlhUbPTQFU-COTVql7D1zSwqdDxL4F1MVMxq97-qH_Y2Bk4AnvZPJfUfM94DEFUhw8XHuIQKUdMdfKoXqzL_F2-tmDwPAhebZ1j1J-urKJGhztESWvV0UV7GFvj0DKiXV1zd6bKp1fqH2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLlT3POrO0pnragPxbyT1J2QewprSbHVUJpxV0DIOAZVYnJYPPkJOTAJChRWYL--Pr_yoy0ebVnmkjTrzD6sPl5aKXdr7eL2k7Ucdy-sVXz8_w2V_e3HQiYmXtu2wILMK3Upaw-ECWPHKsNmNncddjA5pSIXDJurWtm0MQqd9x-9IamcOmgEXHNYQRZTGpVaMzC9fWexOIReCHhBYTWHNXk8nAN6Zw3IhMBP9URh9XKcrIQ0U7ZWOJL5G64OghSk7Jx9Igv95OSL3EV6qCOQfNkMzJ5cwxN-nZzGf0a2PEkHKG9NRR0zcgFT5yXPcykJweqpiYjPzGQgcW8vkq013g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YB9xRgmlg--HLp0bgrQtv4IzqaPeyKQGqctwLcu9DqE1floFLlO8jEv_J5tvcYvNFbJd08KwmyMv2XXKsU-bqL9oGjEpY6A1Lmo_sZ4_yh7qvygrxUWb9YgtWzib5h5a7VvgfxeW2qlPX6mHBScTlonOBEfm-gjzeAuJk3XJpORxVYMuqMkcw6QXVB9qJSTYCWODqK1bvxlgTOVJkuh47scw98OcBC1I4FrVT83lLJXp-YQaGUjdbkaI7xhday2jgrvrvuGEXHTVPHQqp7o9oNRskxeXZCPGSfUZFtiT-f9ddmQUnwwAEGj7x5UsR_SRtrinjTEOvcUrOJM16AEJKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
🔻
القوة الأكثر احترافية في قوات الحشد الشعبي العراقية
نشرت مفارز لواء ٧٢ عاشوراء كلاب بوليسية على طوال طريق الزيارة الذي يمتد من العاصمة بغداد وحتى مدينة كربلاء المقدسة للبحث عن المتفجرات والممنوعات ؛ يذكر ان اللواء يعد ابرز الأولية داخل الحشد من حيث المعدات والتجربة الإعلامية العسكرية ..</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/86648" target="_blank">📅 19:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86647">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏
الصحة العالمية:
تفشي إيبولا في الكونغو الديمقراطية يخرج عن السيطرة.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86647" target="_blank">📅 19:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86646">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1f0463375.mp4?token=MuevMbm17vFZfddzAO0_xzYyBZA-0ZqcexHo3bCGntIPTw4eAXPHmthyU89nx2ubtCqtHq3VQi58jgVPVbtkPIyubu91dBH2KvonoVDvu7cXSYCx6xn8MK4Jac8I7IsairBwoTAheoCZZz--acZLbkjAjdo9sCGs1mVM4G5nGAnJU1NN4NNEAPfV2svmGPcMSmj6acpJytCvigM3mk7QiWycqL8R8W488HICD-sfIszJPr0w0dO0-FkuWQERvS06O9dyx_d7fCU9QY9Cb8GTLt7mTtmNHL0007HGGFyc3VnvtFm1yspRsvph41KAoiyHImnzFGwt16ckoug7BoltqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1f0463375.mp4?token=MuevMbm17vFZfddzAO0_xzYyBZA-0ZqcexHo3bCGntIPTw4eAXPHmthyU89nx2ubtCqtHq3VQi58jgVPVbtkPIyubu91dBH2KvonoVDvu7cXSYCx6xn8MK4Jac8I7IsairBwoTAheoCZZz--acZLbkjAjdo9sCGs1mVM4G5nGAnJU1NN4NNEAPfV2svmGPcMSmj6acpJytCvigM3mk7QiWycqL8R8W488HICD-sfIszJPr0w0dO0-FkuWQERvS06O9dyx_d7fCU9QY9Cb8GTLt7mTtmNHL0007HGGFyc3VnvtFm1yspRsvph41KAoiyHImnzFGwt16ckoug7BoltqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
‏إخلاء القواعد الجوية الاميركية في البحرين خوفا من الهجمة الوقائية الايرانية.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/86646" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86645">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cbf8f15b8.mp4?token=V5xEmydV7xKw3It1tLDoTuUM59WVA5OMGZ5VIKousj_WEkHE5AFOx8pcl76kcIOFJI0-axrorr3HR5ODRqTOS4LC_dbFFFHSkr-isB8Lp6G7cOuGhHdErVQzMIWRtDGBM5mkhpVv8mraznqm7XZb3Q96KbM5Z8QGc20pI_lWCgPdxEmZ4JeJOeb4GgtGowpPT32qrLF8NuI0_C_BJPsHnF9iVvQc7UEzZuii-8aoeYfdA7iHSmt-5jnIFFSzmEtfnZm8Sd0PEIXbw--KoX7ATzIBI2MxhOnt86qwinPQCUhHbHU0jgkEwiATkalWorPnl-WjdcERlcAHFmZA9JT87g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cbf8f15b8.mp4?token=V5xEmydV7xKw3It1tLDoTuUM59WVA5OMGZ5VIKousj_WEkHE5AFOx8pcl76kcIOFJI0-axrorr3HR5ODRqTOS4LC_dbFFFHSkr-isB8Lp6G7cOuGhHdErVQzMIWRtDGBM5mkhpVv8mraznqm7XZb3Q96KbM5Z8QGc20pI_lWCgPdxEmZ4JeJOeb4GgtGowpPT32qrLF8NuI0_C_BJPsHnF9iVvQc7UEzZuii-8aoeYfdA7iHSmt-5jnIFFSzmEtfnZm8Sd0PEIXbw--KoX7ATzIBI2MxhOnt86qwinPQCUhHbHU0jgkEwiATkalWorPnl-WjdcERlcAHFmZA9JT87g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد اخرى لاحتراق مقرات المعارضة الايرانية في محافظة السليمانية شمالي العراق اثر استهدافها بطائرات مسيرة.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86645" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86644">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89cbebf655.mp4?token=JE8_ZIGMH_upYXmM5QB1O8AIpS2mOsGiiC3pq-IdUTLetXHYrvrNO6wXboyK2j21ztoWdHmXg9U9xARN1k-077ghBUXFM8ZUFcs5HbSbuPY7UikEeoeBoDm1AjmcGFLwHQHbH3xrgl7i3IsZOaGauckeNsdtpDjX8x9HLahhTVNPGzcmFhTOO-zNsig0wwZkgLopsriyqk03FNbbVvdko_ppYRBMBqMThG_8a5pA_Dr82ejRd2fHKX8mYFp0eDFm7uVmVQAZtKFhj5ziclpr8rWZur5A56K1RLCmaFar5u09dnVVkiwj5JUAlW37omVzlyLBEbKpNFYs2ht00MUW0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89cbebf655.mp4?token=JE8_ZIGMH_upYXmM5QB1O8AIpS2mOsGiiC3pq-IdUTLetXHYrvrNO6wXboyK2j21ztoWdHmXg9U9xARN1k-077ghBUXFM8ZUFcs5HbSbuPY7UikEeoeBoDm1AjmcGFLwHQHbH3xrgl7i3IsZOaGauckeNsdtpDjX8x9HLahhTVNPGzcmFhTOO-zNsig0wwZkgLopsriyqk03FNbbVvdko_ppYRBMBqMThG_8a5pA_Dr82ejRd2fHKX8mYFp0eDFm7uVmVQAZtKFhj5ziclpr8rWZur5A56K1RLCmaFar5u09dnVVkiwj5JUAlW37omVzlyLBEbKpNFYs2ht00MUW0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من استهداف مقرات المعارضة الايرانية الكردية في محافظة السليمانية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86644" target="_blank">📅 18:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86643">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27ee993f3.mp4?token=TkyvJxfDy6p9oIaeUwU7o1KZbHjFXOP13bE5AtEUw8Y8SA7QpATkc6a29kvbWBTEcaeXNUbtc50v6UHSF4yAFOfl92Ms7zvV0bpVxMCFeC1kIauUSRZAPVLc-r9TtGnMUb4tbhIbUBSUnTGutc_6YxBGkEIQ3d0HwPU5XDH-HFtPSnIZgUgOMgbyob2EVU2LCe8SlfoEt45fyCJHb96Drin2uLTm-uT59w7JaNLS5Ro4UnDMkwPvbIzWRxc0oz3-Y5ft78O3mFsPnkmwLE7uKE3klWa-sh0as6EpBi2VDyFZiZhHB1rh173hWGiPQWL0OKG9K1X0a8j0OnitsoFQ6rIYxYHjTXDkUc-yCe6-FegF-1p_DiY0d4rrdnvku4XR4M-5VNvG-i1zj2d8kRwx18DdS_UaLsiyO9hRHhb7L__yHQvqQWtqw9evCiux6mVdR62smg_tfhmc81PPfPaxPLW_cCxa0F5Lr_dEdM-Dg1cJuXsBGdp6bc6UA-j5oLgvBF50DIYh87tlc_9GH-WJHb9Le60WxhzRneuVx4nyKy7DOj5KhCFDZnOUknGYrYWee7MO1npkONXr0bUjj5SZuIED6MY-Lq98Cf_9Tuq7ntudKBNTzvfpZRfcNcVHdvCWBAVrcY_i4TTLHAUKA_rPpe153ZTWWRBXvgs2WGnH8hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27ee993f3.mp4?token=TkyvJxfDy6p9oIaeUwU7o1KZbHjFXOP13bE5AtEUw8Y8SA7QpATkc6a29kvbWBTEcaeXNUbtc50v6UHSF4yAFOfl92Ms7zvV0bpVxMCFeC1kIauUSRZAPVLc-r9TtGnMUb4tbhIbUBSUnTGutc_6YxBGkEIQ3d0HwPU5XDH-HFtPSnIZgUgOMgbyob2EVU2LCe8SlfoEt45fyCJHb96Drin2uLTm-uT59w7JaNLS5Ro4UnDMkwPvbIzWRxc0oz3-Y5ft78O3mFsPnkmwLE7uKE3klWa-sh0as6EpBi2VDyFZiZhHB1rh173hWGiPQWL0OKG9K1X0a8j0OnitsoFQ6rIYxYHjTXDkUc-yCe6-FegF-1p_DiY0d4rrdnvku4XR4M-5VNvG-i1zj2d8kRwx18DdS_UaLsiyO9hRHhb7L__yHQvqQWtqw9evCiux6mVdR62smg_tfhmc81PPfPaxPLW_cCxa0F5Lr_dEdM-Dg1cJuXsBGdp6bc6UA-j5oLgvBF50DIYh87tlc_9GH-WJHb9Le60WxhzRneuVx4nyKy7DOj5KhCFDZnOUknGYrYWee7MO1npkONXr0bUjj5SZuIED6MY-Lq98Cf_9Tuq7ntudKBNTzvfpZRfcNcVHdvCWBAVrcY_i4TTLHAUKA_rPpe153ZTWWRBXvgs2WGnH8hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">في الموكب نفسه، تجسّد مشهدان متناقضان؛ الأول لمواطن يعبر عن ولائه برفع صورة السيد الشهيد و السيد مقتدى الصدر وسط الحشود بكل سلمية واحترام، والآخر لمندسّ استغل الصورة نفسها غطاءً ليشتم شهداء الحشد الشعبي، سعياً وراء إثارة الفتنة وشق الصف.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86643" target="_blank">📅 18:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86641">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BdlyxkHwOifXUZXq0bLfyPJ7fQq0rdNfdVBA1Pr-KvLGc4Lj197zcKtkcp1MYbI-WW0QfNQCOvbS45ZFKVCPrjrThSwRN9rzf2ojUeAZu3gDEiEAyCkEIzoVjEdD0h7vctlgPu-7lbAweHODSKPWaXaxVlJaU4Gm5qR_URn91yEoYTrjPaOTv1akHD8-EuOoKNEp4JDYpL-5x0ny1PoIR2LDCu3GXUeonxmr8Q8WNxRCqwDjoVomMIPbMgNztQjJ-7WaEfB5qieTVYmMyFetHQehgGFGVRQE4dZ-Prnd4f3fOZ1K0XKmo80yVALG990ZsirPm8y7sg1y1Nh5IACfMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHfXQfCAyjHKALzywLRr-aimac6gVFGi1gbov8s_cj7m5GYLmW7jTiQIcW29LZnUguC_-tP2hc18TxuZp2yKsmGo48zw4yL5A70X9FLeIu0Am4clkgqUR8w-Jg96lT4Tk-OsdsHARJ9pB4ZmZS8NTu26YON1rC6PpnlLPSorv0IDOswJpRS-GxRRibAZ3xXbzqNNDquHdZoQ6BW0FaXcPrPEL-qYikQHapmBkkYn3FTVZEAe2kL5jLzvqxGRa2-JS8dixr7bysO7isNDg0WBtaaoeU84P17ZFpvhgx7rPpIYCIIK79KeN3spqzZ2V20wUy4XY1rdNXVcfaBRHAdR8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد لمنطاد التجسس الامريكي</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86641" target="_blank">📅 18:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86639">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjxB2Rzic_4UxQBr_UhTjWkEm7luPENnkKGUFYFIA4Lu33Vm_ZHmX02CEF0toDCDHSlgM2gnYrDer8tl47BGL5dc_oD5FxH9QXzt_95gZWi3gS6uTxnpid5-k_unPVZSLo5vsQaYKo-otRWUdWnboFOHTQ8ug6wqcLBo9g31eTJq1O2bBlvVxAqzCthSHcpH5twjJ2NuCLJhPl-GsLpI96Rz45jjr1FUBA8QiIg8BX0YDwSz4fctiMasajUG335OJfeSeRBeR5WVFcKKW9TDMdAI2U8IM_DhoxUR1tMy0EClEj1WhevsV7ePtXwVCdmQVq_DGVJCDOMYKkgBDx6wOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZDaU15LMvdnKwr0yN3mrTy-CKoHwb1A-DAoZtWVBeItnr4FkgznjgArILwv0Ma25VnaeJIT2vCqNF0gZTA_AYdJ3cZo_vyoUkaptoRWU7ScGoxGhMfMIuZn55Ab78AbXeC-us2aq6quH6lDWDKHzHgT_jSbtUUloB7UvJZygsQo_dpPgnnCvVhtOKsM8e4kFB78M9Fveq6rjhIl3umBps7lBGSLqAGCcVQiP8eHKjTK4C25f2DpPhR249Xcs6PWP974F6i8V-A8NumCnDBy1AsTM2sSfIJk89mDWteh7HGxfF8laoHHvLA_oB1ciOzWiP8R8ys8mvN6d0Pr6bZ6n9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
جيش العدو الامريكي ينزل منطاد مراقبة مطار أربيل الذي كان بمثابة رادار لنظام باتريوت الأمريكي المضاد للصواريخ والذي تم تركيبه خلال الحرب الأمريكية على ايران.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86639" target="_blank">📅 18:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86638">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2447c36d60.mp4?token=tn7Htfd_UhnzYU4TjWh0bNFrSCCUW8EVR4-yXFqEBDDr385amquoeJyYWMOb5GUveWlP1pq8GGlQeoabhHsUO5VAFiuGNHutKKoRlPHyPwtxMjszr8Izge93flKMh6428sFbnYwnD1L729AGfIaMjoJPa9vBlEWv2DopY94yTNi6H9eoe72m7OblnvUrZE5UE6YyeLk2pzsBr3ivqx_O7kO53ZROKA3d4PwAlcFwoMtI9NMpfIrksnNWhpcbJgxvEwgR652fL2_lTdb3VlgX-yRrwr5l4pfEHTEcSiSdCleI8_FMFGtKRhSr-rU0D_JrUCMZZDuVkXX0eU8nmA3clXECdWt_CGN-eLQ4I580ZkWd5ltgVOw5sgy7jQVMkyQX7DXb5qJe9vYVYLbAJDhB6BDZdOUqPwJKMZJZFXoOOr8IPnyCRXh3f7RtyeegZHjBJVRYP8y_F9VlpV7ar3oSGs6LCFSxHHEmgll5T8HP4z8yi4pIQN_cNHhUChOFF9hFXtizVOBPXxTKzgedQSF1fQ6pFf5mmF6NiJWIHeogSk1o6oVKsvh7CcZg-EBB6NQ6PkTqfcmVctjuBdtMs1-CxlhQqLttNxmKqc5EoyG-CYUfW0hUliCJNJQKXD4dBBCvLGtlRzZTrZEGmuVAAKTiVItMkOr52COZUrrsvYnE030" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2447c36d60.mp4?token=tn7Htfd_UhnzYU4TjWh0bNFrSCCUW8EVR4-yXFqEBDDr385amquoeJyYWMOb5GUveWlP1pq8GGlQeoabhHsUO5VAFiuGNHutKKoRlPHyPwtxMjszr8Izge93flKMh6428sFbnYwnD1L729AGfIaMjoJPa9vBlEWv2DopY94yTNi6H9eoe72m7OblnvUrZE5UE6YyeLk2pzsBr3ivqx_O7kO53ZROKA3d4PwAlcFwoMtI9NMpfIrksnNWhpcbJgxvEwgR652fL2_lTdb3VlgX-yRrwr5l4pfEHTEcSiSdCleI8_FMFGtKRhSr-rU0D_JrUCMZZDuVkXX0eU8nmA3clXECdWt_CGN-eLQ4I580ZkWd5ltgVOw5sgy7jQVMkyQX7DXb5qJe9vYVYLbAJDhB6BDZdOUqPwJKMZJZFXoOOr8IPnyCRXh3f7RtyeegZHjBJVRYP8y_F9VlpV7ar3oSGs6LCFSxHHEmgll5T8HP4z8yi4pIQN_cNHhUChOFF9hFXtizVOBPXxTKzgedQSF1fQ6pFf5mmF6NiJWIHeogSk1o6oVKsvh7CcZg-EBB6NQ6PkTqfcmVctjuBdtMs1-CxlhQqLttNxmKqc5EoyG-CYUfW0hUliCJNJQKXD4dBBCvLGtlRzZTrZEGmuVAAKTiVItMkOr52COZUrrsvYnE030" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من منطقة دوكان في محافظة السليمانية بعد هجوم مسير استهدف مقرات المعارضة الايرانية الكردية</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/86638" target="_blank">📅 18:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86637">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
جيش العدو الامريكي ينزل منطاد مراقبة مطار أربيل الذي كان بمثابة رادار لنظام باتريوت الأمريكي المضاد للصواريخ والذي تم تركيبه خلال الحرب الأمريكية على ايران.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86637" target="_blank">📅 18:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86636">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5826e91067.mp4?token=Z89u8emsWo8QtcXDBsy507Y8eLTUapXE1IovqoMY0ammHiWOhWq1wyfQ1W1grtr99VL41_1jagZU0JKAglMci1rnItgSPZw6YEFZTG01DVbo0fe_732dtpfm4JU7-tR_5jVH5ArM4UJwLsGDaBr6MP10XTxuwT8porZ03qksXIsWVlrf9qpPg-V6EdD5CD-SzvqfHOC8dxKkAl-35MiLqNYxdw2jK6IiAgX99VkIvr2IzLgu6BL0qbhiphCEoKaAJbC_hTPasc1pALc9qZWm6wscLFFBoCp5T08pJeery8Gzhi387Ez-W6cjWhU0RlhZGmSlx1bfY3bkadNeTsyE61D0__4nopxZgWeHELMHehOkxdePu5rKXu9wP0v89C6VuBKTlMaHHNK_IS7FnbpSvha0YfVAveopVCah_OOtsBfwZimcuVpHjwZVCUVqynl7A-dpposxqLq5pkhP53Q7gPlxIDDoEe6QgPlTGzDEkxtmUaSIWxZZb9dBRrNddp9u1W6-qye-hbmtjObgJgVCKiVhd2MUqrigYT-AVdpnFGSRPK9lbxeGrwNuJlBSZAJt2T3OkMXIV4Ot-uCMmHMvQq4Y9xX64T4TRWlyBmQybDc56igV2wQdcsmeUSOxWER9KVrBZwv9FRmklRGTE2fCMVdHLfjqggv_9XahSzgj2DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5826e91067.mp4?token=Z89u8emsWo8QtcXDBsy507Y8eLTUapXE1IovqoMY0ammHiWOhWq1wyfQ1W1grtr99VL41_1jagZU0JKAglMci1rnItgSPZw6YEFZTG01DVbo0fe_732dtpfm4JU7-tR_5jVH5ArM4UJwLsGDaBr6MP10XTxuwT8porZ03qksXIsWVlrf9qpPg-V6EdD5CD-SzvqfHOC8dxKkAl-35MiLqNYxdw2jK6IiAgX99VkIvr2IzLgu6BL0qbhiphCEoKaAJbC_hTPasc1pALc9qZWm6wscLFFBoCp5T08pJeery8Gzhi387Ez-W6cjWhU0RlhZGmSlx1bfY3bkadNeTsyE61D0__4nopxZgWeHELMHehOkxdePu5rKXu9wP0v89C6VuBKTlMaHHNK_IS7FnbpSvha0YfVAveopVCah_OOtsBfwZimcuVpHjwZVCUVqynl7A-dpposxqLq5pkhP53Q7gPlxIDDoEe6QgPlTGzDEkxtmUaSIWxZZb9dBRrNddp9u1W6-qye-hbmtjObgJgVCKiVhd2MUqrigYT-AVdpnFGSRPK9lbxeGrwNuJlBSZAJt2T3OkMXIV4Ot-uCMmHMvQq4Y9xX64T4TRWlyBmQybDc56igV2wQdcsmeUSOxWER9KVrBZwv9FRmklRGTE2fCMVdHLfjqggv_9XahSzgj2DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز السليمانية</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86636" target="_blank">📅 18:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86635">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارات تهز السليمانية</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86635" target="_blank">📅 18:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86634">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">السلاح المنفلت في اقليم كردستان
هجوم مسلح في سوق كلار بمحافظة السليمانية يسفر عن مقتل شخص واصابة اخر والمسلحين يلوذون بالفرار</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/86634" target="_blank">📅 16:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86633">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f9790c4c7.mp4?token=QZ6oN4-eLw6uj7Nzap6ys4v9qNcoKkIDGn9FeVF7dolTPlmqaHLyHtMcS7C3K_P7Jzl0w4IGe4bUAEvHRID73Gv_xZbZI4H713QggYQaQ6GDaxgYIWDdih6zLKIE6KpyR3iZD4yt_msTTQ8GKijDnuVtXP2u-d_GEzsDbWo6dRopWeA350mDaaTqCMH9xVnpvTn6wQg32Q0iGmYQDXLdys-m6mI7jxhvBzXWop-V9pAiAQCA1ncConvEAp-wckF2WPUNVuRu6-WIGAXf_PBHsmP4o2WlO1MHcJ50FfUrXqlYC6PnRZbY3TXf-nLrlB0oq7p9YtRM79IUQekq4hOatQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f9790c4c7.mp4?token=QZ6oN4-eLw6uj7Nzap6ys4v9qNcoKkIDGn9FeVF7dolTPlmqaHLyHtMcS7C3K_P7Jzl0w4IGe4bUAEvHRID73Gv_xZbZI4H713QggYQaQ6GDaxgYIWDdih6zLKIE6KpyR3iZD4yt_msTTQ8GKijDnuVtXP2u-d_GEzsDbWo6dRopWeA350mDaaTqCMH9xVnpvTn6wQg32Q0iGmYQDXLdys-m6mI7jxhvBzXWop-V9pAiAQCA1ncConvEAp-wckF2WPUNVuRu6-WIGAXf_PBHsmP4o2WlO1MHcJ50FfUrXqlYC6PnRZbY3TXf-nLrlB0oq7p9YtRM79IUQekq4hOatQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
خاص لنايا | طيران حربي امريكي يحلق في اجواء شرق الاردن.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86633" target="_blank">📅 16:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86632">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f255af304a.mp4?token=AoJHXpw_NbpyFRBMeVozMdii173_gvkTi9e9Qgvy_nzoMd5t0xtW9Z1AaQRzbierVhtdt8xUkP0pg8K09JCMSPq4L7baLLrhV8IMYYLXGnM4bvpYENl8tVTj6BTEIHUrpWWXHonalIAoD5Fy9rFS_PyAVBRBHlTkibhkFlII-A4JS4jlXRnou7JPmZwh8M31ZY61QbpNSnatW5lYl8WMCvYwuZytwUi9P5PAo2tjuVa3L2jpwMBWNeXRRw4peGjUZ-yf421yGdwc7G9H6hN4S4ISwwNPTn3ZAskFJknHiH5vOFnf8rTXL8vegXtqwCmCvEPzpQcR-iXGi1w3Vh8IDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f255af304a.mp4?token=AoJHXpw_NbpyFRBMeVozMdii173_gvkTi9e9Qgvy_nzoMd5t0xtW9Z1AaQRzbierVhtdt8xUkP0pg8K09JCMSPq4L7baLLrhV8IMYYLXGnM4bvpYENl8tVTj6BTEIHUrpWWXHonalIAoD5Fy9rFS_PyAVBRBHlTkibhkFlII-A4JS4jlXRnou7JPmZwh8M31ZY61QbpNSnatW5lYl8WMCvYwuZytwUi9P5PAo2tjuVa3L2jpwMBWNeXRRw4peGjUZ-yf421yGdwc7G9H6hN4S4ISwwNPTn3ZAskFJknHiH5vOFnf8rTXL8vegXtqwCmCvEPzpQcR-iXGi1w3Vh8IDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
خاص لنايا |
طيران حربي امريكي يحلق في اجواء شرق الاردن.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/86632" target="_blank">📅 16:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86631">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6CvyZwYPdW4Nj1SFdc6nvbkirlYRK5Qvp3tmZh3fRXRHHP9b64ol2yTa0TkvM0bsVo0uAeNx7Y7OGSTFJl0PidaNIp88eyImYZMpdxnwYSV8RXhtIcbl7_KmLJ-mLE1KFXGHRyex31v80FEaQta0Lj_KZSnCejgkehEdCkZ9LvhHE6X522q2jbp2XbHW8KtfTD_aWoXwy1T7vvvL6TXj-PjDNChF46NTFVoMMxdps1qNLYDSnSp2vZol5wpYGIq_0hQa1PLUAlmK2NW-55OW3cp3LRAZfO5TYeyzKGi08BxYhBz9yITQ4qqaQukREJKohz0z38sYoetZuHEOHLAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
السفارات الامريكية في بغداد وعمان والقدس المحتلة والقاهرة وبلدان اخرى تنشر:  يجب على الأمريكيين الموجودين حاليًا في الشرق الأوسط توخي الحذر واليقظة الشديدة، والاستعداد لإلغاء الرحلات الجوية، والإغلاقات الدورية للمجال الجوي، والاضطرابات المحتملة في السفر.…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86631" target="_blank">📅 16:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86630">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb6f4d28c.mp4?token=I-jO02b8EIaoCFkBHjNqnuL3Xfselfj3epMINc3InWRkGaW0Xhb-g9LVA_Qta1wfWFKTMkrTndCuaPGnL2ez7PcrpDYBgitqGAFpsQIpKEHBfgUv3Ic7ta6JfLJH51w51dMJHPQvGmURj_g4CIKpqeCLXzTp0aMhCPu9KIkawMkTDkfwfd1KabEiqW6tJ9Q2ngMU2awpSkH0fKe5E2IPq6CF4bbm72L_6kTGLg1Dl6t4Qp4HybvCXb5SkUWa9DvrUQ-N8zc8cjqEkls4twQksR_7eozZ7sQ3DYlpqt9AtJ35yhlig4IFZ1uqYL3TUBDGcBx9rrTX3sJ0vKBqjhgeXgaw9dtPehZCKqLBOB5hElBxI6nKUq0kHE3s4y7qAlXGnH1_GMXWyrlLTQUaOWxcmvJm10OC39i7bIeh6_EJQe0wqz4yc_8AdO7097zx5VlWuF5JI4R7kioX6hN7PaCOUfBO0l3Ps5GzTZxIv9yqJDoBWOyzfVR9u1UCRQFsRRaNzmH4SS9pFafyiDFdM61WK5OiG6whNqPeuK4_vMT4TrkOkS8tbeQIlBsbatbS8ft3Xi2ITjivd_gfZY56aW30JmmA6jbtM9Q3mxXOK2afsQOVM7C9kwS8mtsCdWEH95cm0YqqoLGbw9bQhuJ8ZUgps_wDhFPFOTs9KMpneCHTeHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb6f4d28c.mp4?token=I-jO02b8EIaoCFkBHjNqnuL3Xfselfj3epMINc3InWRkGaW0Xhb-g9LVA_Qta1wfWFKTMkrTndCuaPGnL2ez7PcrpDYBgitqGAFpsQIpKEHBfgUv3Ic7ta6JfLJH51w51dMJHPQvGmURj_g4CIKpqeCLXzTp0aMhCPu9KIkawMkTDkfwfd1KabEiqW6tJ9Q2ngMU2awpSkH0fKe5E2IPq6CF4bbm72L_6kTGLg1Dl6t4Qp4HybvCXb5SkUWa9DvrUQ-N8zc8cjqEkls4twQksR_7eozZ7sQ3DYlpqt9AtJ35yhlig4IFZ1uqYL3TUBDGcBx9rrTX3sJ0vKBqjhgeXgaw9dtPehZCKqLBOB5hElBxI6nKUq0kHE3s4y7qAlXGnH1_GMXWyrlLTQUaOWxcmvJm10OC39i7bIeh6_EJQe0wqz4yc_8AdO7097zx5VlWuF5JI4R7kioX6hN7PaCOUfBO0l3Ps5GzTZxIv9yqJDoBWOyzfVR9u1UCRQFsRRaNzmH4SS9pFafyiDFdM61WK5OiG6whNqPeuK4_vMT4TrkOkS8tbeQIlBsbatbS8ft3Xi2ITjivd_gfZY56aW30JmmA6jbtM9Q3mxXOK2afsQOVM7C9kwS8mtsCdWEH95cm0YqqoLGbw9bQhuJ8ZUgps_wDhFPFOTs9KMpneCHTeHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طائرات حربية مجهولة تحلق في أجواء مناطق سهل نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86630" target="_blank">📅 16:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86629">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
طائرات حربية مجهولة تحلق في أجواء مناطق سهل نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/86629" target="_blank">📅 16:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86628">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇸
🇮🇷
مسؤول أميركي:
الجهود الدبلوماسية تتقدم ببطء واستئناف المفاوضات المباشرة مع إيران لا يبدو وشيكا.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86628" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86627">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiwYWFEaMJM65osGE7IJEh8CWOBonjBbxIhSDkguvAdvKN_zvzgaQu7ZZkJeitte9AayXqSWOEg3WITjsRiQ94V5N098Q2qWbCqSPOPYzzV6THE7CKRC6_JP8cyyJDlwOqgGlRaLZkm9MSH5QL2M8n-RroA_qcJr8QkCnoKyQ8YU-wDCc5Zx82kdPLXd-fGSq5S-ruQZgO-X86P_DOHb67AJj-tU3kd_6Xat8mwnYuF1S51we09yP8wD4sbg6HVLwEC80dN9uBiDPDwWdmQRHGfPYd3N8WmufaSk1UPvN5yifeYr1wQivlHhFwv1alOb4uLiKQiw6EDuV3Umtx_1Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
واشنطن بوست:
الجنرال أليكسوس غرينكويتش القائد الأعلى للقوات الأمريكية في أوروبا يحذر البنتاغون من عدم كفاية عدد المدمرات البحرية لحماية إسرائيل من الهجمات الصاروخية الباليستية الإيرانية مع تلبية احتياجات الدفاع الأمريكية في الوقت نفسه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86627" target="_blank">📅 15:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86626">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية: اتفاقية ثلاثية لاستئناف التصدير عبر جيهان بطاقة 750 الف برميل يوميا.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86626" target="_blank">📅 15:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86625">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8CAT1CDS8GRRRaldp_pUYNOmwoDwKc3wAdh-qSQiahOmgkKTT1gNsvxt7gHPrM2bSdeX5qc_Vf7DLqCbJbRIMF4NNx8CHlsur0FI98wxXTXnWhwjprgbG3dbLVydzAMMGPav59aBKrdEZRKty6Hw5yyjsjmVqyqkTZL9EXKBL1GCXk7mTdiMKhoc6tMKYmXj_dWEneCTVyARN8y6IRqCSSpPmehXQQ7p-YRGm37909e0EkBxRvUlOzmfWAldHx5cEVgrGr8qC6ZIpfczHGVwbRBUf_v8DeCiIVW_mjlfQ3PKD621BdNFoYvak0df_FgCEdYAI44NEheevcbUqMNgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
في ابهى صور الديمقراطية..
ترامب يهدد السلطات التشريعية باستهداف جو بايدن واوباما سياسيا في حال لم يتم تعيين تود بلانش بمنصب المدعي العام للولايات المتحدة مؤكدا انه سيبقي تود بلانش مدعيا بالوكالة.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86625" target="_blank">📅 15:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86624">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrtHcQahG0knrfBZ1Xe_hnlLZQho9fLR96b5TOkocmyg3QP56DiBYSvb-pUuyPiMfXCgzA9Prj2B-AWtxwaaA7h7TEFuX0KhXH1v5WJTNqICrnULN4CqQpdOshorv9VPTcDlLPAMUbJhhk9YfNIwpvaSXaPK5j8CqX6m3WkspZY5GM5CSZzxvehbtDdZ8BobcQU6LJ0amVdSy9XxUCmUN0cXk5qd3kOpZ7BBBjug_yi-W_1ppsVTZZPXA7dUCGnwq70nUTuFe7AR8x-9kmbtvW3t0gzqKoIp_eY5Lzu36HeGixP9Qv9PGz-3kndvrLLolIrp13cd6CLA9JF1MYLLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
السفارات الامريكية في بغداد وعمان والقدس المحتلة والقاهرة وبلدان اخرى تنشر:
يجب على الأمريكيين الموجودين حاليًا في الشرق الأوسط توخي الحذر واليقظة الشديدة، والاستعداد لإلغاء الرحلات الجوية، والإغلاقات الدورية للمجال الجوي، والاضطرابات المحتملة في السفر. وقد أجلت بعض شركات الطيران في المنطقة استئناف جداول الرحلات السابقة؛ بينما ألغت شركات أخرى بعض الخطوط</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86624" target="_blank">📅 15:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86623">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇱
جيش العدو:
خلال الليلة الماضية أصيب ضابط في الجيش الإسرائيلي إصابة متوسطة خلال عملية عسكرية في جنوب لبنان. تم نقل الجندي إلى المستشفى لتلقي العلاج، وتم إبلاغ عائلته</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/86623" target="_blank">📅 14:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86622">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBjbuHf-wgnv-G8OVYSjUVGT3oZKBv27clLNENCW7qscJk79sgSKXhw-c7m1Pe_VguKmipeM7btuOp7D_aEH7IzYQVzpxtu6bWL5_P8K9Gt3xP-ZwVgopoyR0iUJwL7fbyCT4zIi0jC5-TqW03tmd3cqypjs5uOi_rPUmrPveVpAOJLGb0UgNlwW5TUSKVTltTG_OY4ILgYiPpsvxyaw4CCIo037CF7pKfMP8A7x5U04tg-z3wFdQWFmO1KjFlRfkYj_QzBRSrRawgify5NC5zKIyliMwTcQf917RLG7wPh0UKk8rMdf0_2yRr8nYJiQHLivi1SafO5B4FuH0BsO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظام ال سعود يعلن فتح باب التطوع الى الجيش بسبب النقص في صفوفه لكثرة الانشقاقات ولصعوبة تجنيد مرتزقة بسبب شحة الموارد على خلفية اغلاق مضيق هرمز والحصار في البحر الاحمر.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86622" target="_blank">📅 14:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86621">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
🇮🇷
السفير الايراني في العراق:
موسم الزيارة الأربعينية لهذا العام يسير بأقل قدر من التحديات، هذا العام، بدلًا من الحديث عن المشاكل نتحدث عن الإنجازات التي حققها موسم الأربعين. الزائرين الايرانيين يتمتعون بصحة جيدة وفي ظروف مثالية لأداء الزيارة.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86621" target="_blank">📅 14:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86620">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية:
اتفاقية ثلاثية لاستئناف التصدير عبر جيهان بطاقة 750 الف برميل يوميا.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86620" target="_blank">📅 14:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86619">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">من الحريق في اربيل</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/86619" target="_blank">📅 13:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86618">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34d9c123.mp4?token=aMTJq9f3UjmLU05nGSx2pJOkSSaPTYm2jBSCvoMZ95GXfHTiGufI0rhbExZuUiGA6aLZoT_qRhKpuvkoRs6in314qWduuU_4EQvoHx-V8Hs6aYc9jT4QF4WPtpcIk7pfY_jMO0ACA5tLUtEXFPVAUozHlgOs3pvFetnfNx3MQjHaw0yBCSwWhxbm7nBARWvsx5IIdxo9hKs5-ItOZ1nsoljGuK_4XCgpfSD2gOYa419dxyX0b5oNNoa7lbBFXKveb83_eWHaFfCnwo6A6-8wkSA8AfmEPIVEYURuKTUdQ7WKGqXrl7gAs6vRTBciyc4WsjRTzAP95Zzk1n_uC--gQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34d9c123.mp4?token=aMTJq9f3UjmLU05nGSx2pJOkSSaPTYm2jBSCvoMZ95GXfHTiGufI0rhbExZuUiGA6aLZoT_qRhKpuvkoRs6in314qWduuU_4EQvoHx-V8Hs6aYc9jT4QF4WPtpcIk7pfY_jMO0ACA5tLUtEXFPVAUozHlgOs3pvFetnfNx3MQjHaw0yBCSwWhxbm7nBARWvsx5IIdxo9hKs5-ItOZ1nsoljGuK_4XCgpfSD2gOYa419dxyX0b5oNNoa7lbBFXKveb83_eWHaFfCnwo6A6-8wkSA8AfmEPIVEYURuKTUdQ7WKGqXrl7gAs6vRTBciyc4WsjRTzAP95Zzk1n_uC--gQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيقات اضافية من الحريق الذي التهم احدى مصافي محافظة اربيل</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/86618" target="_blank">📅 13:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86617">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇪🇸
وزارة ‏الداخلية الإسبانية:
وفاة ما لايقل عن 67 مهاجرا خلال عبورهم جيب سبتة.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86617" target="_blank">📅 12:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86616">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e37647a01.mp4?token=efBAe7TJPDwYXUTx6SfVbC9XMqtRilpccBdTZKFCNMKPoQuKGRot8BS213nscgNKSCdfcJ6sRZrSOceG2WKEH4dlNarJH0Ey02L0iJfv8EHVdqCfL6o66OGWv35bl3ANBfPNvXQ5-e5E79DvTf_Pw_uPF9cCcUk8M8tXDDdOXTcQZv-MCDSJfdeH-9yKQXZVmttinpmNtYZstM0V4jMvIc6ftU-I7ySRMtYU9x3qrPadV1qS7zR_pOg3gcmJxjtNaeDc3ECQV7QHg3v-9GI61NwvK3TwArdMPHN4KJwatJnfHeTy8ef_eQi-ZwRh7vtIdOh1IWZEJLkfzxAgLghZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e37647a01.mp4?token=efBAe7TJPDwYXUTx6SfVbC9XMqtRilpccBdTZKFCNMKPoQuKGRot8BS213nscgNKSCdfcJ6sRZrSOceG2WKEH4dlNarJH0Ey02L0iJfv8EHVdqCfL6o66OGWv35bl3ANBfPNvXQ5-e5E79DvTf_Pw_uPF9cCcUk8M8tXDDdOXTcQZv-MCDSJfdeH-9yKQXZVmttinpmNtYZstM0V4jMvIc6ftU-I7ySRMtYU9x3qrPadV1qS7zR_pOg3gcmJxjtNaeDc3ECQV7QHg3v-9GI61NwvK3TwArdMPHN4KJwatJnfHeTy8ef_eQi-ZwRh7vtIdOh1IWZEJLkfzxAgLghZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الحريق في مصفاة للنفط بناحية شمامك بمحافظة أربيل</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86616" target="_blank">📅 12:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86615">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feed9248e1.mp4?token=UfZjMyZNQV_bD5Z_CkEdfKSHx7IeI6zp6paobQ6YzgvtNq9-HjqaG_ROxf2M8FFRndsZoTe1YiYAw6adX-2-d__GLZdOhqZrQjos14gjSzORWFtvRZbvKixNbW3Tf6jdk_YlMJeXPysLvVaFnHoy7QM3GG8MwP_6LGrx1frjKH4VhoY5IAMgekGjUFh-nGWGS5RDF_zFBI8nooT6NMO_FVul9RrNdGbAMKvZmUkJ3wlRRz7lbaUbcoBR-WEJjfw9HXLBwtfMPJUQU441bBsN7uRaL1QDXxDYsss-vNY2yYWcMC8E9Nqz2WpYIc-QLcxELo1st8RSy-5KzWkcBT-AzwCvN5h4c-4kibyW9Av9nCur5ab1IPWFMwYp4kXMarfuTpfRPhbW01TV5kgb2SSDoFTm47d4WVkHv1DtadC2vyonkdAtFzrKfeyczVgNaBc7dH3ArEpVzQ1EFnfW5RlJgJY4feppej5J63ArUEzXQBkQrHWAt2tor02IhF848XrGyigwNBAcTUzO24wI2fhaJ3RGMP9e-bkFD9RXe4VouWTuOKR1J4xqEiJNXzMzKzxkgmKt7_Jw-KmzGY3nhAxkCgeHPD4NIyQqsy771S62TgogblKWmvgZ-1-dH2M-lHrTAawbPEqtZVauj6HVntp6C9b1fJmAVc4uZ_nnvgxqDmE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feed9248e1.mp4?token=UfZjMyZNQV_bD5Z_CkEdfKSHx7IeI6zp6paobQ6YzgvtNq9-HjqaG_ROxf2M8FFRndsZoTe1YiYAw6adX-2-d__GLZdOhqZrQjos14gjSzORWFtvRZbvKixNbW3Tf6jdk_YlMJeXPysLvVaFnHoy7QM3GG8MwP_6LGrx1frjKH4VhoY5IAMgekGjUFh-nGWGS5RDF_zFBI8nooT6NMO_FVul9RrNdGbAMKvZmUkJ3wlRRz7lbaUbcoBR-WEJjfw9HXLBwtfMPJUQU441bBsN7uRaL1QDXxDYsss-vNY2yYWcMC8E9Nqz2WpYIc-QLcxELo1st8RSy-5KzWkcBT-AzwCvN5h4c-4kibyW9Av9nCur5ab1IPWFMwYp4kXMarfuTpfRPhbW01TV5kgb2SSDoFTm47d4WVkHv1DtadC2vyonkdAtFzrKfeyczVgNaBc7dH3ArEpVzQ1EFnfW5RlJgJY4feppej5J63ArUEzXQBkQrHWAt2tor02IhF848XrGyigwNBAcTUzO24wI2fhaJ3RGMP9e-bkFD9RXe4VouWTuOKR1J4xqEiJNXzMzKzxkgmKt7_Jw-KmzGY3nhAxkCgeHPD4NIyQqsy771S62TgogblKWmvgZ-1-dH2M-lHrTAawbPEqtZVauj6HVntp6C9b1fJmAVc4uZ_nnvgxqDmE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق كبير في احدى مصافي محافظة اربيل في اقليم كردستان شمالي العراق</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/86615" target="_blank">📅 12:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86614">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4b26c5b8.mp4?token=Up3xRWGHSU7zH0FeGM_03HhylJ2vPlaDljS0D1RK7XO24UxRh3Rbo_LRY6M_AB_6ulp8VKKYmPEd4OVzGgu3r4gpCyJLXZLbJXSsq98-s9rHsz7Nn7k2llgWzPWo91RO5RxPqr3nPi2hoIC8Nh-GXd3wnNM1pdYASONhxecOwtMayX26TfB981mFooRBpFTmq9uogolkAUW-kk3X9BHkoT95VLN2VKNJDJ1bWkzb2zlWhTuc4F-_X-vgTS0p38XQt67sXvqFaSUCIKZFgbeSZEWxL2SfUrPc3oBylbjQ8h0qNuK59znc49MPhQXgk5-S-dX4j_eys9wYGC5y60NIjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4b26c5b8.mp4?token=Up3xRWGHSU7zH0FeGM_03HhylJ2vPlaDljS0D1RK7XO24UxRh3Rbo_LRY6M_AB_6ulp8VKKYmPEd4OVzGgu3r4gpCyJLXZLbJXSsq98-s9rHsz7Nn7k2llgWzPWo91RO5RxPqr3nPi2hoIC8Nh-GXd3wnNM1pdYASONhxecOwtMayX26TfB981mFooRBpFTmq9uogolkAUW-kk3X9BHkoT95VLN2VKNJDJ1bWkzb2zlWhTuc4F-_X-vgTS0p38XQt67sXvqFaSUCIKZFgbeSZEWxL2SfUrPc3oBylbjQ8h0qNuK59znc49MPhQXgk5-S-dX4j_eys9wYGC5y60NIjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق كبير في احدى مصافي محافظة اربيل في اقليم كردستان شمالي العراق</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86614" target="_blank">📅 12:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86613">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇺🇸
🇯🇴
🇮🇶
السفارات الأمريكية في العراق والأردن يتنافسن بالدعوة للمغادرة..
سفارة أمريكا في الأردن تدعو مواطنيها إلى التفكير في مغادرة منطقة الشرق الأوسط وتجنب القواعد العسكرية، وتحذر من أن النظام الإيراني غير متوقع، وأن هناك احتمالًا لتصعيد مفاجئ واضطرابات في الرحلات الجوية والمجال الجوي</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/86613" target="_blank">📅 11:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86612">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇱
🇺🇸
منصات المستوطنين في الكيان تتحدث عن غضب في الولايات المتحدة .. نتنياهو يريد حرب دون نهاية وقد يقدم على عملية عسكرية قبل الانتخابات</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/86612" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86611">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هجوم مسير إيراني يغزو الكويت</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/86611" target="_blank">📅 11:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86610">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هجوم مسير إيراني يغزو الكويت</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/86610" target="_blank">📅 11:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86609">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/86609" target="_blank">📅 11:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86608">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
قائد مقر خاتم الأنبياء المركزي:
تسعى الولايات المتحدة الأمريكية، بوتيرة متسارعة، إلى إشعال فتيل حرب شاملة في المنطقة.
هذا النهج هو نتاج استراتيجية خطيرة تهدف إلى التوسع والهيمنة غير المشروعة في جميع أنحاء المنطقة.
لقد أثبتت الولايات المتحدة الأمريكية، في الحرب الأخيرة ضد إيران الإسلامية، أنها لا تتردد في ارتكاب أي جريمة أو تدمير ضد مصالح وموارد المسلمين، وذلك في سبيل تحقيق أهدافها وأهدافها الشيطانية.
يجب أن تدرك الدول الإسلامية في المنطقة أن الولايات المتحدة تستغل مواردها وثرواتها وبنيتها التحتية الحيوية ومواردها الاستراتيجية كدرع دفاعي لجيشها المتهالك، وفي الوقت نفسه، لتعزيز آلة الحرب والأمن للنظام الإسرائيلي الإرهابي الذي يقتل الأطفال.
لقد أثبتت الجمهورية الإسلامية الإيرانية وأبناؤها الشجعان والأبطال في القوات المسلحة وجبهة المقاومة أن ميزان القوى في المنطقة لم يعد يتبع المعايير السابقة، وأن عجز الولايات المتحدة عن تحقيق استراتيجياتها العدوانية وغير المشروعة ضد إيران الإسلامية قد دفع الجيش الأمريكي المتدهور والنظام الإسرائيلي المزيف إلى شن الحرب وإراقة الدماء والشر من وراء تحصينات الدول الإسلامية، وإلصاق تكاليف الحرب على حكومات المنطقة.
يُعلن بوضوح: يجب على الدول الإسلامية أن تراقب عن كثب جرائم الولايات المتحدة وأن تعيد النظر في تعاونها معها؛ وإلا، فإن أي دولة تعتبر نفسها درعًا دفاعيًا للولايات المتحدة الأمريكية الإجرامية والمتجاوزة، ستشتعل في نار الحرب.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/naya_foriraq/86608" target="_blank">📅 11:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86607">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
🇺🇸
إعلام العدو عن مسؤول أميركي: بعد الهجوم الصاروخي المفاجئ على قاعدة أميركية في الأردن الأربعاء نفذ الإيرانيون هجمات إضافية
الإيرانيون هاجموا سفناً في مضيق هرمز رغم تهديد ترامب بأن أي هجوم إضافي سيقابل بضربات أميركية</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/86607" target="_blank">📅 11:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86606">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇵🇰
إعلام باكستاني: العثور على جثث 8 من بين 10 متسلقين انقطع اتصالهم بعد انهيار جليدي على جبل "برود بيك" في باكستان</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/86606" target="_blank">📅 11:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86605">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
إعلام أمريكي : ‏دار نقاش حول محاولة إنهاء [الضربات الموسعة] بحلول موعد افتتاح الأسواق المالية يوم الاثنين، وذلك بسبب المخاوف بشأن تأثير التفجيرات على الاقتصاد الأمريكي والعالمي، لكن لم يتم تحديد موعد نهائي</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86605" target="_blank">📅 10:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86604">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇷🇺
🇺🇦
قصف صاروخي روسي كبير على العاصمة الأوكرانية كييف والنيران تشعل السماء وسط انقطاع واسع للكهرباء.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86604" target="_blank">📅 10:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86603">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
إعلام أمريكي :
‏دار نقاش حول محاولة إنهاء [الضربات الموسعة] بحلول موعد افتتاح الأسواق المالية يوم الاثنين، وذلك بسبب المخاوف بشأن تأثير التفجيرات على الاقتصاد الأمريكي والعالمي، لكن لم يتم تحديد موعد نهائي</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/86603" target="_blank">📅 10:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86602">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">هجوم بالمسيرات والصواريخ الإيرانية استهدف القواعد الأمريكية في الكويت</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/86602" target="_blank">📅 09:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86601">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86601" target="_blank">📅 09:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86600">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BC_CCvPlPYo44Vn2gl1IRGLR_a7hHllKGL7c74S60hntSO3sBin3WKV-VojvyBqUuGpLGzXxqgSPmwpS4fF2_cqZ39PcWq6-scw1vljo9OGvwxzKkArlnsGbp-TYkqJwrAaWqVmlDFveiO-fnAjD4bGgpA1bXPTG6tGfSSmRX2zCCNGKpNt_zYWD494pUhDnQDxZa-z61Cnv0KGGbfdtWsbwAL0ftMFYAOiGLVuJU0TvZ89jdgBIad5SXqW_nUxB2suPhUxtjuJglZntWLX6i4LDkL2w1mQxvL1fUHVbxByCxnOKr3P-hc_WDqGXIXXvkYRCN5XywPtILqfhejnxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري قبالة عمان</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/86600" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86599">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حدث بحري قبالة عمان</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/86599" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86598">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86598" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86597">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇾🇪
إعلام يمني: أنباء عن سماع دوي انفجارات شمال شرق تعز في اليمن.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/86597" target="_blank">📅 09:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86596">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WK8fZ-aAvd5smSv8-LoAz_B8WjJwKURqop3Rlz8_iaMXTusN2wLHJqazRbzAq2mKbfXIHEhbfWvHQ6Sjjj0kKGnF1M3MEE5bc4Ka5ifiDg06e21qjjf_evUjUiwF09_xPkYecOTIQQ2-kwhWPC1REbiEG0A1qOh55M52GBYpb6Io5c7cDIsivEebpm1Llgz-TwG3J4fOrEpW4eJ2PGOxMnKHIa0vU7knajEg_V0mrfs9-nndibCoZApL6D1RKTryuz0cqccQ5vgpMgGqcD9WT4gRJEoXC6jq3L5P8v0mqM1z3W0m-DdMUgRiuyqBgQ6ucjO8JBCqQDhfRr2l3rFZhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
الهيئة البحرية البريطانية
: ‏شنت القوات الإيرانية هجوماً على ناقلة نفط أخرى في مضيق هرمز ليلاً أثناء عبورها الممر الذي تحرسه الولايات المتحدة. ‏أصيبت السفينة بقذيفة في غرفة محركاتها ولم تعد تحت القيادة.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/86596" target="_blank">📅 06:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86595">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044c3ed5b4.mp4?token=Fyc1AVs35X__i6RuoZPlLwCGKFX2m1FZ6c7ykL6mk3ika9Oz58FNHZhKje3qrLV7saAlOn0MxI4K9-8QBlvdZ9rZvj0ro7v-0mNoeM07DbxWPLWFLJcpmjShmJj9J9Pxbg5IgTOfXr189FpSeXz8moJQuf4Yk3K8Oz_y9P23RQfTTD7BDEH-MKRtmMrkWKLfoxRouJ99wPbzDEsMo46pF70aupTKPj89UMRA1fsykqsl3za5ljqDeAZN38unl28ep2ncXmcdZcmPY9COKFvPw6aKR1gvzb3JU6B8OCdd-6H3e6xAkKrsFA9je8RN1PIs6ypsnAm6oYSw3pRLKZz6D05xs0TSJzbcQMTzWwk1JdfZXKW63LkQZ0ZOGLj9oaoaCmgVBkJFoaBeRRQYqiRqzDAirMOm6M26rtCk_qNhrU0HGhaVRaqIjsBoISd3-E4KgEPQddpIwmZgEh_SNfm_Z7WF9aEhozpIjUHOx4OF9JcZkUqQVU2-aQMsCp73TWaxxzbqArXg222GH3wNucbtJDsN-IVsPBlF15gdYOgj8rA78WQ2hzG0sirYvyxVXt4evuuHQqugszYxrwD5Ck5en-P9IXa_5__hMX3LGPGuaLFSEI2S2Dwg-VOfT4UvzHwAM9TjtZhBoR59jnSNtuFLKPrWVttv6chKXRpvmjNCobM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044c3ed5b4.mp4?token=Fyc1AVs35X__i6RuoZPlLwCGKFX2m1FZ6c7ykL6mk3ika9Oz58FNHZhKje3qrLV7saAlOn0MxI4K9-8QBlvdZ9rZvj0ro7v-0mNoeM07DbxWPLWFLJcpmjShmJj9J9Pxbg5IgTOfXr189FpSeXz8moJQuf4Yk3K8Oz_y9P23RQfTTD7BDEH-MKRtmMrkWKLfoxRouJ99wPbzDEsMo46pF70aupTKPj89UMRA1fsykqsl3za5ljqDeAZN38unl28ep2ncXmcdZcmPY9COKFvPw6aKR1gvzb3JU6B8OCdd-6H3e6xAkKrsFA9je8RN1PIs6ypsnAm6oYSw3pRLKZz6D05xs0TSJzbcQMTzWwk1JdfZXKW63LkQZ0ZOGLj9oaoaCmgVBkJFoaBeRRQYqiRqzDAirMOm6M26rtCk_qNhrU0HGhaVRaqIjsBoISd3-E4KgEPQddpIwmZgEh_SNfm_Z7WF9aEhozpIjUHOx4OF9JcZkUqQVU2-aQMsCp73TWaxxzbqArXg222GH3wNucbtJDsN-IVsPBlF15gdYOgj8rA78WQ2hzG0sirYvyxVXt4evuuHQqugszYxrwD5Ck5en-P9IXa_5__hMX3LGPGuaLFSEI2S2Dwg-VOfT4UvzHwAM9TjtZhBoR59jnSNtuFLKPrWVttv6chKXRpvmjNCobM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">كلا كلا آل سعود..
تشييع الجثامين الطاهرة لشهداء اللواء 30 الذين ارتقوا نتيجة العدوان السعودي الأمريكي الغادر الغاشم في محافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/naya_foriraq/86595" target="_blank">📅 04:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86594">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇱
إعلام العدو:
حدث أمني في الجيش الإسرائيلي والتفاصيل لاحقًا.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/naya_foriraq/86594" target="_blank">📅 03:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86593">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cffc20c83.mp4?token=pzmL1UOyJfIi6irRdf2m4WyxoZ0QZqN3u71d4PwUplkYTq8Qfm3DiVwE-O7XdGIMYv3b8wdfZ5OO0C3Hf0JUaoAQ6sPPo7H7noro2NfwYyeLnqDBdSVpKCxYQJk0TK9DmLC7sbxMGCG_7t1L_YWtsoPfZDkk_7WELtRtzaCxLxwr1B9CN-glxlu6_IzCMnvt3Lp2aS_1bUdgBuvPFmQPWPKnY-HACtzkfu7Cxns9ImDJWJVGwqEgv5jPOkx5sF2umS-zfFU8ke3ZVXC5qk8MTAaDnweBiDpE2yikd4kcDq0FguWchnYa8-HX8JkGZues8pa-Vz-29O50sRkgE2emUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cffc20c83.mp4?token=pzmL1UOyJfIi6irRdf2m4WyxoZ0QZqN3u71d4PwUplkYTq8Qfm3DiVwE-O7XdGIMYv3b8wdfZ5OO0C3Hf0JUaoAQ6sPPo7H7noro2NfwYyeLnqDBdSVpKCxYQJk0TK9DmLC7sbxMGCG_7t1L_YWtsoPfZDkk_7WELtRtzaCxLxwr1B9CN-glxlu6_IzCMnvt3Lp2aS_1bUdgBuvPFmQPWPKnY-HACtzkfu7Cxns9ImDJWJVGwqEgv5jPOkx5sF2umS-zfFU8ke3ZVXC5qk8MTAaDnweBiDpE2yikd4kcDq0FguWchnYa8-HX8JkGZues8pa-Vz-29O50sRkgE2emUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
إقلاع مستمر للطيران الأمريكي في قاعدة موفق السلطي الجوية بالأردن.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/naya_foriraq/86593" target="_blank">📅 03:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86592">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
إغلاق جزئي في مطار دنفر الدولي بالولايات المتحدة الأمريكية بسبب تهديد أمني محتمل.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/naya_foriraq/86592" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86591">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwVD4XVulCEc3PglvfyP5qh_YyoCfzu5eq4Db3XLx9iHdg7U64XFfj4RFpn2DnN0iKcTU3ZUdDLE5lWJWn7AZkzS-9v9v4y1EaxSLbmeYrg7mrJT5Nt9F9AMmrMuhK5QnNbtNUT8A84uulEXEXQey967X0EhnT0w-HDcpeMx8gOgndsaLfZimFr6nVawJvrvfD8tuZcVZiIuwdfr_9q5tdfMeijj_xhF-FjlioMprjSVnQXb_hOjNaQHTjUe5DomMQBbNrHytaB5F5v0eFJiCkmZCow_1JX4fuRtxjwP2BtmPbdtoHR0ISJXl5alien1bUdkvdmM3dMUeHFWmCQ9sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇺🇦
قصف صاروخي روسي كبير على العاصمة الأوكرانية كييف والنيران تشعل السماء وسط انقطاع واسع للكهرباء.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/naya_foriraq/86591" target="_blank">📅 02:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86590">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
🇮🇷
‏مسؤول أمريكي: ترامب أمر بجولة جديدة من الضربات ضد إيران ستستمر لعدة أيام</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/naya_foriraq/86590" target="_blank">📅 01:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86589">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
البيت الأبيض:
طهران أخلت بمذكرة التفاهم وأطلقت النار على السفن و
قتلت جنودا أمريكيين
.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/naya_foriraq/86589" target="_blank">📅 01:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86588">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAEOVM2dR45GreWiZ4ykViX776OTk5jv0_8NwUl-Z1ywRC0dM9bISWGncq18Vo1G8Ch46JPfBxSdQWaCUjwP9DhCef1CZIN_xEuJJkZ4p4dNTJmLeUhIi7DlbzO29L9hQ_cgOSjmXeBoaeiKYS8wobKIKD0lrsUJm4Z9G7pmgE5ftAuOIbYQDtPF2IOs2oZDNHT5vdQHSepQj0Abyu76dI4ao3dJISTIrowzwwg-vA-z46n5V_BgeMaPlVyonn5gU2RDk4PW2x4C5z7g7fh-stZVIVaK_N99B0eHv5d17e8rg-WDGpBiEWRY737yJ9U1vXgBNhN6H60o_1aLCOyFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الأمين العام للمجلس الأعلى للأمن القومي الإيراني:
إن استمرار الحصار البحري وإشعال الحروب الذي يمارسه النظام الأمريكي سيؤدي إلى تشديد الحصار على مضيق هرمز وإغلاق المضائق والاختناقات الأخرى. وسيدفع الاقتصاد العالمي وسوق الطاقة والناخبون الأمريكيون الثمن.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/naya_foriraq/86588" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
