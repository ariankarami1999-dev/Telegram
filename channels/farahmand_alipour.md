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
<img src="https://cdn4.telesco.pe/file/h5YAyUuFU2gx8IEElS0qQZl0qEaMdMFt6_mUa9vv7GGhLHHLqRLcWjT5sfMT2hHxIEWYmGFCmPLOul3M8dPn1rmR4kT0UPNVvx7nuvpP4gQ0vnmLLhIscnLiNQm2gjAHeV1Ys0lnpjQS2SBHsKxW_74pj9PP6AO605ePml__bJOKxJV8E45XtAkRfOB65Y1jTL7sM4B_Pyf0mC4CV4NHc8guXpdVXbLXsiUZdrQQd-JYNNP937I76RoMlJmnAFv-RHX6_VyU6GZSXj0FuJaYQXfj1uMcnMGf467Cm5W9RdPlgqHzAEkvPAYLs-YJuxxRkcj1Sq8cMetnuNh3whq-og.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 22:51:11</div>
<hr>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=ikV5mJC_Lw2eeSiVZwr-Bgr2dr4LY0Jv9O1hPG4jXnbSVs4NjO-0hHsJ6sqbXh6IEi-tZhJ8LQDKeUloCAiIbzmbVr1SqsrMKXeP6RMvqcX5bSYfPjl3ERQ9X-tVKyiTXbAPbIC9OO2dvBKbjkVXW08D20RjDwURnDcL47e6OvKHwlLAxoazfK4np2-bTmwEmTOJ7dzhjnBcDfGRVS05p3IXKUTaV6HYTPvLK0CODVK_aLe3mr7wKEVp2SpbIJ6UY5M_Szzu8WW9H63Kmg3DrGkOLilbiDLb1Ox-23TnYwUkRTRswv0jhl0qbJq0XuH9TzAyAKypDZdCTiQdJFZV-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=ikV5mJC_Lw2eeSiVZwr-Bgr2dr4LY0Jv9O1hPG4jXnbSVs4NjO-0hHsJ6sqbXh6IEi-tZhJ8LQDKeUloCAiIbzmbVr1SqsrMKXeP6RMvqcX5bSYfPjl3ERQ9X-tVKyiTXbAPbIC9OO2dvBKbjkVXW08D20RjDwURnDcL47e6OvKHwlLAxoazfK4np2-bTmwEmTOJ7dzhjnBcDfGRVS05p3IXKUTaV6HYTPvLK0CODVK_aLe3mr7wKEVp2SpbIJ6UY5M_Szzu8WW9H63Kmg3DrGkOLilbiDLb1Ox-23TnYwUkRTRswv0jhl0qbJq0XuH9TzAyAKypDZdCTiQdJFZV-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=vgzk22LsggUDmZnLuPT2s08bPum_1MfE3BjuTaZzEGppBvYIeV6faedWDyneNIlIMUDemibVFcoq9S7mrWip9b0LfhAK4-pN2_qkuQzC0TNtIoVOSzJ7IAiZRlCVkSM6r8_KJM-tBCs_tNCIQqiTVQ-VdF5kvT_cPi2JYCzhtVKxh8GSkZPfBdsb-O3xUyn8kKkNEh27Xd2-AG4ncNgqXiJFVNHjQcHqFD9dPCDN4QA5KBs2eWIc0Q3hoSKSJCoPtdxzXTuslDgYIJvBAsIGDj5Vk30zo5xf8H3aqaReuOnEM_PuHcxVfdHHJ9rgqF5ixdgNVnYfPUFYtolNkhRAZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=vgzk22LsggUDmZnLuPT2s08bPum_1MfE3BjuTaZzEGppBvYIeV6faedWDyneNIlIMUDemibVFcoq9S7mrWip9b0LfhAK4-pN2_qkuQzC0TNtIoVOSzJ7IAiZRlCVkSM6r8_KJM-tBCs_tNCIQqiTVQ-VdF5kvT_cPi2JYCzhtVKxh8GSkZPfBdsb-O3xUyn8kKkNEh27Xd2-AG4ncNgqXiJFVNHjQcHqFD9dPCDN4QA5KBs2eWIc0Q3hoSKSJCoPtdxzXTuslDgYIJvBAsIGDj5Vk30zo5xf8H3aqaReuOnEM_PuHcxVfdHHJ9rgqF5ixdgNVnYfPUFYtolNkhRAZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2jXUzua6hqCme7db5HWAsnQpa4fSpg6wrDhaMKcv0NSw4IfhepNxyKTR0VKuswg2bQm6dqIjVuWN9vNMt0tgWoPIa25z3eVX6rx2F3xzLI7YBDjS0ptFM-mAAh0BpkiJpKMZbV61VDsyz92q8qIC6B0UO_5t8MCXWIqH1DYyIsTDXJOLPHRjxQ3t0_qiYmeKCsCn042cC5BM8gBNyDkY1fI9-m1wRB5jeeHkW5p_UyX-OZoRn_nJCNYDrU9ipt_p0JJU8YQy4f3-nH3fXsDN1TNa7RAx8m8XwTzMaqfcLyiSkCEwIgTc9013Shnsp8H96M3EeWlGfE6pzyBze7HHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=cGcq508OQsu3q24pjLGWWVsFUn130EycN0gSx7k12EHMyu3khCgz9MDekURo6mDdsIGom5paHbEE7Z3wikdMgscKf13eRRGXIX3gNq6IhwlidvgjsuDM05WzzKjSeyvZDUvJHs1g6ZeUxh9WqoD1lXHGGVCubIIQNa_WS33ajhwkGhKsf8euMbyAw6FR0zN1-Ln9Qx3MQAcFzzKdfd-cokW9WXnhr-3Cxn_fVBAjcBs_rddSatgScyMGfacmwb5KjA6mdff6CZTWDw2aRZgiX2Thj63dc5Y061V391fFTjsEsOytMdmpAbJas89bvP1pTiORRuDsaLfXqx26c3ri-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=cGcq508OQsu3q24pjLGWWVsFUn130EycN0gSx7k12EHMyu3khCgz9MDekURo6mDdsIGom5paHbEE7Z3wikdMgscKf13eRRGXIX3gNq6IhwlidvgjsuDM05WzzKjSeyvZDUvJHs1g6ZeUxh9WqoD1lXHGGVCubIIQNa_WS33ajhwkGhKsf8euMbyAw6FR0zN1-Ln9Qx3MQAcFzzKdfd-cokW9WXnhr-3Cxn_fVBAjcBs_rddSatgScyMGfacmwb5KjA6mdff6CZTWDw2aRZgiX2Thj63dc5Y061V391fFTjsEsOytMdmpAbJas89bvP1pTiORRuDsaLfXqx26c3ri-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS5S9d764T9zFk6An4H5s1vCscROBLJiiwGNHZ3PKoNqthjA7EcQ0OEiwVRGC45CrT-B9nfORTMt-zTaBzRuhnwOSAi0N573j2jYXeYHfJjSPJ5MurKlKB607h538uhofhuzsdPrUsKIlOTR0h4fj-UV8LHj-AeaqFVtOq_ia2nYNQcxCdd28v3yIazw3z2Ih453pO2vA11hfz3ufIZ5FU6CWS0lJ0KH_i4U9toPEpr0xUMzz277_Mxdqcxk98bl4rlWjbku7LR-QPbnDZS5NoNMqnOKmnzjRLZ_pskoTfEzF_YClS8gjtIL2KssvvaMGtx2l3EZqqsPISxlkzr3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ti8Uz9ARcybXL0HKjBVxmxbf7kS8YOBH18zWqzQl7OOmnOhajooddGtQiqH5K8rmIy_W97Svteux9Rgheqgg7hEYWTVtNyK-aP2yiQ8MbPIvIBcbuMSgDtO5RjsKzznju3mQOAMDeu6lJ-q11twyKlwsSla6sd7d0g37yzLmiXQsLvvJLJHRQbyyY7uw17pNKrSLA0yXcDi7YaUQf5kk-pOD0ZMHSFFcqCpvN0ag4_TPhyaukyIzoS-Xs3Bc9GjKl6Uilf-1C20uhnyx3gXxUEQXXSIkN7RVTOpb4fWwBgTgf99yCp-8LCuhRwHj0aPDT8xSiL5GSZAZmUtBYUsi6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=vbxhInx35vFu0JMUt4IUIzodAnxhF2MWmPAajg0GqW42xgmayS-ES3ciwQciSScDKBPeZFrztt3UDKqLS4G5ogCQCgrogz7aiCa_bUfFRUQWTmozTXpJAkJQt9rxTQI1UcZFS5thU5vH3jfOU31hsLugPfoiQurzgD6tO6NceMChq2UXNE2gXjaFs5z3yyC3u9m88Sb7ArSjM4qsAobICnkdei4nyLRon7vT_ArqseVTk5joxKLOPxtu4XZ0E908EerRYowcMjguzhWOFq_BxKoo6C3e8D3HX4WLx4hfHygV0--Qmk4_gcAsxL5DfuqtVVVWHnV5_gD2t6fRHmNo1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=vbxhInx35vFu0JMUt4IUIzodAnxhF2MWmPAajg0GqW42xgmayS-ES3ciwQciSScDKBPeZFrztt3UDKqLS4G5ogCQCgrogz7aiCa_bUfFRUQWTmozTXpJAkJQt9rxTQI1UcZFS5thU5vH3jfOU31hsLugPfoiQurzgD6tO6NceMChq2UXNE2gXjaFs5z3yyC3u9m88Sb7ArSjM4qsAobICnkdei4nyLRon7vT_ArqseVTk5joxKLOPxtu4XZ0E908EerRYowcMjguzhWOFq_BxKoo6C3e8D3HX4WLx4hfHygV0--Qmk4_gcAsxL5DfuqtVVVWHnV5_gD2t6fRHmNo1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9TahEAJjyzkLcwG_A_tgJ_nSwAK0ogmhz3o9DzS74uyJDrht38vN9GU_I5wKvhtsC40k-B0xio9OiadKyIbtP_hqkpsRf1qAbJ3Fw9vAZlWrHnRqGmXy-2ypZ12THdwfQmHSgg7MeFDYZXwYyZUBvf_0xAzx0trY_6H_6uMUpD0fc2FE-stvKNQzHzbF6GgkGcZ4rgq9gGABscl_9jH-QDsLGeNoTLhcH-ldhbsof49sFIdldqw3IiHGIqeMHIqx3b0t6dnpxCJxow5VxovrFfnbUOgQx2rTOJNDs4gVnBc6mgTxygOM6RnjA9YbjMyDJUcmhnCN_LNHnJFCDSd5Qg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9TahEAJjyzkLcwG_A_tgJ_nSwAK0ogmhz3o9DzS74uyJDrht38vN9GU_I5wKvhtsC40k-B0xio9OiadKyIbtP_hqkpsRf1qAbJ3Fw9vAZlWrHnRqGmXy-2ypZ12THdwfQmHSgg7MeFDYZXwYyZUBvf_0xAzx0trY_6H_6uMUpD0fc2FE-stvKNQzHzbF6GgkGcZ4rgq9gGABscl_9jH-QDsLGeNoTLhcH-ldhbsof49sFIdldqw3IiHGIqeMHIqx3b0t6dnpxCJxow5VxovrFfnbUOgQx2rTOJNDs4gVnBc6mgTxygOM6RnjA9YbjMyDJUcmhnCN_LNHnJFCDSd5Qg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=Xk1xG0W3VSl_CvtsYN6tJLms2G4rzzsRy36LImw-cnHt1tjqt5TaSnia__qx26Fi-IrzFov9EcRgUFeQkGf1LjZAyaxa_0FAUU55roHLtbVdvuWl4bY7af016h-SM69HQ-NMj8ws_Ehb7dA-c_TheefnbaPQIvukVYR12QL2rYfjY3_3ZhJmw_JT_0bxhgZDRyvGButzfqTLoiofUVj1Ih8Tab0shSDVbNVFxcPhYfVViKYSvMTy0YMwC1Wrq1IC8YXM8zJGJU-8RTdGJmQsdwSOLJL09gTyS691qEm37SIYOKpKfu25Gd71ZDFto3uFqxnL_rNs60OBQrexrV2aeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=Xk1xG0W3VSl_CvtsYN6tJLms2G4rzzsRy36LImw-cnHt1tjqt5TaSnia__qx26Fi-IrzFov9EcRgUFeQkGf1LjZAyaxa_0FAUU55roHLtbVdvuWl4bY7af016h-SM69HQ-NMj8ws_Ehb7dA-c_TheefnbaPQIvukVYR12QL2rYfjY3_3ZhJmw_JT_0bxhgZDRyvGButzfqTLoiofUVj1Ih8Tab0shSDVbNVFxcPhYfVViKYSvMTy0YMwC1Wrq1IC8YXM8zJGJU-8RTdGJmQsdwSOLJL09gTyS691qEm37SIYOKpKfu25Gd71ZDFto3uFqxnL_rNs60OBQrexrV2aeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvztdfVtj9TfByy9vnraHfetouPFFNNQ7M1mSDFN9PsWO9nZmlU-_SU8KSxxzWOvPJHFb9l3sbbzS1vOSYIS3ERYaR0gD4S8VlFBsU5z9VWH5YogCVTsFkKTLwDMXex_hVBP94EaZS5S8t_BkPSsIBS2CuSeRjk6voR6QnHTVTUe7JJ1tMvzQA_5dQqFWLNmo56zzFTsip_AS_jJ9RjDKnC9quVXkR5i-O1-k4lk6-ygBaaN91OuFicUO3JTAWIGPEFKGYKcs0vP-xKBYgkD6PWK1S87hPAUgTzbNRRV0tAwOoDFadfm3ZGhVBKrTMOnUaBvbdap64KhpVAPcxwlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=akq5WJp14bhlbIiyUSA1FdCVD6vLGnKvXUQtfdXoKKLSJ0ORsOyG-WUHMzi_d6STDOaTVEYxGGPHUx7jplmxKv8oz2APedwqgKaDxqd5w-pV0Kiv9fm80VT9q-rjklPYzii_nEJwhLIusJj70JLQHTEgUPfHakT7ZeTE04ShNDq8pM4LwT8gWOKTtOhcHMr7mGxphV3dutlKCp9ZayrFrQyOW7gCWmZOk2cSZ7D2n3Z9kskpsyHjOmxxtixWE4R1pPio4kDkfdggw5_3pXRemzK-ZaiSJDf0mWAohyLHOWK-6eLpp4uYE3SdU-SUhNZ34mpWIeljHCA49kc3iyNaSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=akq5WJp14bhlbIiyUSA1FdCVD6vLGnKvXUQtfdXoKKLSJ0ORsOyG-WUHMzi_d6STDOaTVEYxGGPHUx7jplmxKv8oz2APedwqgKaDxqd5w-pV0Kiv9fm80VT9q-rjklPYzii_nEJwhLIusJj70JLQHTEgUPfHakT7ZeTE04ShNDq8pM4LwT8gWOKTtOhcHMr7mGxphV3dutlKCp9ZayrFrQyOW7gCWmZOk2cSZ7D2n3Z9kskpsyHjOmxxtixWE4R1pPio4kDkfdggw5_3pXRemzK-ZaiSJDf0mWAohyLHOWK-6eLpp4uYE3SdU-SUhNZ34mpWIeljHCA49kc3iyNaSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qDIoFiL5DR8OV0FJLUDttEVA81pgYbLyE5zz61AG9sa-fAuGXTvXKxMaHPv62F1HP-uOhqwqqbZ91dLsQ3zw5tmPzJbTHccNcLg4JPROZ3mtBaHyVO66oWKjSjiQ4tTklGOjLprq1f72VCw0n90FJNGJAd6PoSVuL6cV2goDHkj4yETKD5cZ0rhYHWhfMs7VaOuTBKqL3B4bjVzEYq6Te_qWazU3SdvMqnnQhPwWYiGXcyEQKw33mZF4IDuj8Hj1gI0STka32kOYr9FIi-N3WfDatdjYWH4i2ps5OuxH4CulE7QVIs0KHF_W8lyw7wfVWuEVJxEEHbKgeZEPjOY2cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qDIoFiL5DR8OV0FJLUDttEVA81pgYbLyE5zz61AG9sa-fAuGXTvXKxMaHPv62F1HP-uOhqwqqbZ91dLsQ3zw5tmPzJbTHccNcLg4JPROZ3mtBaHyVO66oWKjSjiQ4tTklGOjLprq1f72VCw0n90FJNGJAd6PoSVuL6cV2goDHkj4yETKD5cZ0rhYHWhfMs7VaOuTBKqL3B4bjVzEYq6Te_qWazU3SdvMqnnQhPwWYiGXcyEQKw33mZF4IDuj8Hj1gI0STka32kOYr9FIi-N3WfDatdjYWH4i2ps5OuxH4CulE7QVIs0KHF_W8lyw7wfVWuEVJxEEHbKgeZEPjOY2cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vahz6obxbAoqstAxuTMkuWWiqxQHz-JwHM_5z8clcUXiqSVtD6C6FiezdR1gNBW0oq6deW8Azso50a_EYoR40OLQc5Nr-rrdxI7Y2ybs7eAuN-CNv9niVoVnMX_NXPZTUjqNoFrrnHkyEJHsrLPIPk7XlCc0M6G2iOH2KSeFCoU1Eaj077qWUhxGMkMEz4snMMX9ho82p6ORb7bg87x2pkF-gkjlgZTpLDSoK4GOapAOR9r9qjAx-9ylVlATUIedWRp8UqOkIJVsl0uSttLi25l1wk4bTWDOiPkw80GZytXD57SR0rD9Tq1yy0T3bg-wckGv5_ZTW5sRwYculMIQJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vahz6obxbAoqstAxuTMkuWWiqxQHz-JwHM_5z8clcUXiqSVtD6C6FiezdR1gNBW0oq6deW8Azso50a_EYoR40OLQc5Nr-rrdxI7Y2ybs7eAuN-CNv9niVoVnMX_NXPZTUjqNoFrrnHkyEJHsrLPIPk7XlCc0M6G2iOH2KSeFCoU1Eaj077qWUhxGMkMEz4snMMX9ho82p6ORb7bg87x2pkF-gkjlgZTpLDSoK4GOapAOR9r9qjAx-9ylVlATUIedWRp8UqOkIJVsl0uSttLi25l1wk4bTWDOiPkw80GZytXD57SR0rD9Tq1yy0T3bg-wckGv5_ZTW5sRwYculMIQJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YoA_jkol-01mjn0tXCS0NIBGUESMY858Ks4TjKmXysUaNUQ4NY5DoYZq89DW4Ju4XckW5d-eSPIHckGSlLZvok47mpkbmz03rBF23VulaysoRIC7LYgpg9O8U-Eb7Vo_wU1sp4NENVO81MHPx7dMUMcDNsziWpRy600htyci2PbNbyTNU_jAVw0ortEm6I5iLLgwKKfomdbGnYYrl4nZAbpIwlyqMbAajxGYKEpCfLvM-JzF2r71TEYo4B-a_Pbq01xeSvh991Qg9zzhvkf-lTMseZM4KV_4CAuvrxdTuu1u-CYnVoTOWcCySjJ_JqLW5uFI3fvOQkA-O992h6UXDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YoA_jkol-01mjn0tXCS0NIBGUESMY858Ks4TjKmXysUaNUQ4NY5DoYZq89DW4Ju4XckW5d-eSPIHckGSlLZvok47mpkbmz03rBF23VulaysoRIC7LYgpg9O8U-Eb7Vo_wU1sp4NENVO81MHPx7dMUMcDNsziWpRy600htyci2PbNbyTNU_jAVw0ortEm6I5iLLgwKKfomdbGnYYrl4nZAbpIwlyqMbAajxGYKEpCfLvM-JzF2r71TEYo4B-a_Pbq01xeSvh991Qg9zzhvkf-lTMseZM4KV_4CAuvrxdTuu1u-CYnVoTOWcCySjJ_JqLW5uFI3fvOQkA-O992h6UXDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LndJz2xo-eldmWGJk3dOkz9uOpTn1b6vjxJ6LW1mpZqHGcRwPDi_4OevapX855JLg5aCyPdqBcQA2Dt7ZvHwR3CGBV1ek4YkN24pOQgDft0Jn6ubCtAAelrzqQiJnEb6bzNwIWqYz2Uzxaqa_U1vsyhyAInHpGKbFdzaBSu805kmPWyr1St6dYWU-QHcdGT3oIau-ts55w6kO3tMsGkpkXs8bNc_NoozG-vAg2oaALDag1EKPrlTZSEpEnS6tGNKc_OB2sUtPoniTsBH7QjDMKNWAkedZ6Cg6rWTzAOJotOhBqZ2QCOToKUE2C60D4xOqiyr9109ui8HTCK4qLAaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=tTZzMplzaWAoi6Dbiifgg9cv5SryPq3XiuVsjrPVdxWZ0cfxb2vVu4pfqUmfJelmgV8b6-t484nCwJtA8w6rjMVauABA4Xar52lID1jQrSAnzBKbgo04RlJxKRDRbtWQDBMCICCV6SSBk3IR_O1RpIlussrMn7ggyCzEYhrdPGJMTzuNxjzdRhkTQqi5E3HiHgvpQkVHQshT4eSLhEPL5pnofhh54GtMDBLIlX_1IGLIGThnvj7PQ0yvsGo8ImwmUGzdOozUmv5L3hAJWJjc9xjamogbnPBqHscfMKfHAzFN4b22JiOGHIya2zzMvsudSu1wIVEBUPmJpAG-YoaTZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=tTZzMplzaWAoi6Dbiifgg9cv5SryPq3XiuVsjrPVdxWZ0cfxb2vVu4pfqUmfJelmgV8b6-t484nCwJtA8w6rjMVauABA4Xar52lID1jQrSAnzBKbgo04RlJxKRDRbtWQDBMCICCV6SSBk3IR_O1RpIlussrMn7ggyCzEYhrdPGJMTzuNxjzdRhkTQqi5E3HiHgvpQkVHQshT4eSLhEPL5pnofhh54GtMDBLIlX_1IGLIGThnvj7PQ0yvsGo8ImwmUGzdOozUmv5L3hAJWJjc9xjamogbnPBqHscfMKfHAzFN4b22JiOGHIya2zzMvsudSu1wIVEBUPmJpAG-YoaTZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=iER6FA9e7nxY9M8TSdTlwo6h89qYM33Pu2lej9RROyZFpcfKBQaJid322sv359nmrQk2kTS3aKgUbOl9bZ5Jl2o3g29F26nBaFK64A4iwOU9yU7zItl1yEDyttjcpQdjrjMPy0e8n1sI1XHS63ok_XgKQXn0c2AUXbziOQsnAx-6X8Cl_SPoTrRGEPFnxwrOaxMn4JI8_LvvZ2aohf72RqZQ59WThVorvEo0dbWl2M13g5WUDyODI9cEZ9n6wRF3u3yZ4X4lDcU8remAu08Biy6lfvoGTdni_JhnH_UifP_lOCq36ngnuUlF7KnhPx9kxaL93qtb7owDnhSYMYYrZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=iER6FA9e7nxY9M8TSdTlwo6h89qYM33Pu2lej9RROyZFpcfKBQaJid322sv359nmrQk2kTS3aKgUbOl9bZ5Jl2o3g29F26nBaFK64A4iwOU9yU7zItl1yEDyttjcpQdjrjMPy0e8n1sI1XHS63ok_XgKQXn0c2AUXbziOQsnAx-6X8Cl_SPoTrRGEPFnxwrOaxMn4JI8_LvvZ2aohf72RqZQ59WThVorvEo0dbWl2M13g5WUDyODI9cEZ9n6wRF3u3yZ4X4lDcU8remAu08Biy6lfvoGTdni_JhnH_UifP_lOCq36ngnuUlF7KnhPx9kxaL93qtb7owDnhSYMYYrZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHKMJQ7ia77KGjP9CnlycjbkdieJ-mWyNjnoXx9NvlEu0G1Xmo18kaBOdb7o39qK5Or3_RlruSlFagtYsk9FOiRQ_3OP2YfcdApG5R65nDsXso2Vy5WFmf9jhE5jlwc278VivvP5EVDH0UsEkoSldCURYNiKQmDrs-4x1Wpy_gRWR6ksgFan-ze6hPXcSbXxD8k8HuxuqR1qFBbiz5brlq1g24gzflFNxUQZy6LBWQqHI7KK_L9WvB8c4UMlLKe9VSHWbVs1NdjKVyzqWlZ1f0fFSj1qJCeQQgM77zFTdBcbvHFbK0QitJvlp1Qtx16Hizwe8ZQ7QKW3TxkA12IrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=khqSO6f50SF3AyhNLYcGXfoluIS8ieYPwMrEV1u0Bot7dfcf2l_ooNiSGoFbfbm-YT0gJ1G5vrOQbjcp6xYfNALX6Vgu9_5P1l9O2FrI97kpwIeMzJoa1QqcdZlLas9sD3s3_e6y99MdZtYzGL1lKnSOV5sO2fWf6SZ0zHr2MhWrLAsBLu1S524w7-qZkJxhSfbxhxcdwxH3v5iAgfPozxOFMxwLtOpHIhN1mn_TM5AGL0AHe1d4PJus9inkB0C-XyeqYRK6CQTQBdnOsQ6F21nTjonMifgStzBuEtEoTttJc1E5Uh5IMrkommT5bW9YRInmUmFMYsrprPqJsXuong" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=khqSO6f50SF3AyhNLYcGXfoluIS8ieYPwMrEV1u0Bot7dfcf2l_ooNiSGoFbfbm-YT0gJ1G5vrOQbjcp6xYfNALX6Vgu9_5P1l9O2FrI97kpwIeMzJoa1QqcdZlLas9sD3s3_e6y99MdZtYzGL1lKnSOV5sO2fWf6SZ0zHr2MhWrLAsBLu1S524w7-qZkJxhSfbxhxcdwxH3v5iAgfPozxOFMxwLtOpHIhN1mn_TM5AGL0AHe1d4PJus9inkB0C-XyeqYRK6CQTQBdnOsQ6F21nTjonMifgStzBuEtEoTttJc1E5Uh5IMrkommT5bW9YRInmUmFMYsrprPqJsXuong" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=YIR5OL8U8oBjcgBHENdP5Py-ciOwhtz0WH3dqHD0izaNCr-6PtrVmG5V0qcAQbfOLDtaw0oCFhDVM8kQ5nj4hS2s3E_PY0PJoBQGpXG1IjAbtsGWfAgJOhLOk9pcVepb4kwOVJ0q7hc6MK8pYNiuLSKn4909qxwEp3otuufVphgbovhAYZqLpJgZcPegJICk0S3tIB-ovetyjk0TIWPekEiNn8rfKcIDQwVwoepjUtE7fihGL61yMV_IExFYWOXP5nGepj7ggNG3LITbKpRnF077dV9zQ-EmnsLxfhxDfsDJLQR1-wO9_QIsF5a8oN80JdSP8jC_GcB8vTjIKjrtqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=YIR5OL8U8oBjcgBHENdP5Py-ciOwhtz0WH3dqHD0izaNCr-6PtrVmG5V0qcAQbfOLDtaw0oCFhDVM8kQ5nj4hS2s3E_PY0PJoBQGpXG1IjAbtsGWfAgJOhLOk9pcVepb4kwOVJ0q7hc6MK8pYNiuLSKn4909qxwEp3otuufVphgbovhAYZqLpJgZcPegJICk0S3tIB-ovetyjk0TIWPekEiNn8rfKcIDQwVwoepjUtE7fihGL61yMV_IExFYWOXP5nGepj7ggNG3LITbKpRnF077dV9zQ-EmnsLxfhxDfsDJLQR1-wO9_QIsF5a8oN80JdSP8jC_GcB8vTjIKjrtqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=E6vXOWihJwRxN82F8Hur-cnqqQDql2jnpM6HTw-x2IBS1pYUNc8V7JBCfIdvKtFZ4MennSKPEDmJNSarfoPt4XMw2HskzVAlQ2i3oual1hsO1sukTMC_PiuCCTj5plW82Yx8oaGk3Xc5-64W9ge2V7avHH0JQ6zgcnQfUUJqBlOjGmx-bwcwiahE904IpJ7Q_rajM2et1PUSFPrjuqk594DBb-vRvKAwXD8EECbiQBz53OKbSzOhxNbLQEzESN7__GSsUdX92onAU6kmrmopgeBqqGi-zw1rDxap6H3F8eFuRT4aCdTyUYiB9gJQc_SIF5U0GXG3APsO0bbnSDWPLTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=E6vXOWihJwRxN82F8Hur-cnqqQDql2jnpM6HTw-x2IBS1pYUNc8V7JBCfIdvKtFZ4MennSKPEDmJNSarfoPt4XMw2HskzVAlQ2i3oual1hsO1sukTMC_PiuCCTj5plW82Yx8oaGk3Xc5-64W9ge2V7avHH0JQ6zgcnQfUUJqBlOjGmx-bwcwiahE904IpJ7Q_rajM2et1PUSFPrjuqk594DBb-vRvKAwXD8EECbiQBz53OKbSzOhxNbLQEzESN7__GSsUdX92onAU6kmrmopgeBqqGi-zw1rDxap6H3F8eFuRT4aCdTyUYiB9gJQc_SIF5U0GXG3APsO0bbnSDWPLTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cdgAh88dtsZXx7Ph4F0ffY6I4Pk1YsT_UpU0SNNZNaDzHHD8RdGuqzbr3rnrhYLbWNBA1RJvXqxFXTaFOragiIVBz3MZWHSrDtnoN482TvrPpR01hm-a-QLPMud-TsaC1dNs0edsv6IrZhEYpDuO2LIDcGdkxA9HsuQ_S240zqhgM-jGdjmnYjgaUqxteNYKAG0hjELCWxpUOUNIDUaBeQfIaq0C7E0v2L4YfKmOuj_vdmhn2q6Y0Z7LhG-QpB78GL4hzkWelB9EqwLINzE34DhfTQAI6-gkOwnzInOp8pjHAqqi4cB6EFq3YKsk-2NkvIPlH5ekJFGNf7o_jDabJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCeMrC6O2JlizpTbRgYi8PlrPXavkk0pujAIytIaPlWXjKIHeFfwp8DKYQT4fWofZvn8jmfQMQx-vAt4E4WGMw2b0eF9gdj_7A5_ffRMcrVaX5NIjY9e8wPpYRnOri_ade7dAjl1fhKhaDzztd1iDCshrjyCo0aWyv-5w4XNwBQxZlU9bBkYDvqAY7v2Six7e11QSBfylCBpzpFlaA4W1INKLewcSfUY5cbD0Mt7hixYheGV8Raps5SWPe4bA-rVvcjL9dluRhGa6c2S5Wtjbu8uGtwPi0hGnGpxsUuQC4WliH4FRYLEwM3O_5Fxr8h3yGDUzzVJ4-ZTsCt2wjHv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmVgibiuWmv1DWhn_7M_4lo5gsVfm_b7KudHcQS-76mr6oNzeAUNb4IAD41JO6ESMNAzPxsi6_9X-oadJ7cKiWJ5qQOzXHp5H6DBlgvWQJUkEs8Siea6msqr3g9Qb3VD9mQmt9qs-PghNPPJXpmpEsBjxhzNhq7HsUseEMIxlULaAoS-7OGxb1FatRzXjcY9zS3IzVdwncKoyB5xphR0S7HsRWeVmBC0ZQMsYL9psAYYDlJkJPxyWzfLmj6rYYKQv_tPvkKxibITPJ_jx5kelym-oRPjdz1LYnCB4ZPhxrXteicR68BloZjzmf9ixmjPSiutN3k0e3n8J2ViUH-siA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=vBWpEYj5c1KNAKqENe7tMZ6-rXkfO8B26arn3DkxBgApW4ypdY_ggzWHnu8Soq_jVBkQf52MP7lcpajhqICC7g5gDBLH6dwHoFY41Vb6iTbIa7pp8jfNBGdJKEcvZx9BjJ7vmYrSPTJPNlYp-8O33XUtNJIEIYyln4m32nbPSMyEB8FzCdfuIpXdeII4DH3lVRaofsRr42pxWOjU5jVPnbhP1w2ankWXwzh2mXBciEMSUbs7lIJsJ6N6V_6cK-g7yyrph-aC3ED9SrLTuomrmIn2H6jiHMqy7rlv6oR_qiNEWiDvIB88-TXEbuDTYYb0Ktj-7ZVa-8vSvLPH6uvWRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=vBWpEYj5c1KNAKqENe7tMZ6-rXkfO8B26arn3DkxBgApW4ypdY_ggzWHnu8Soq_jVBkQf52MP7lcpajhqICC7g5gDBLH6dwHoFY41Vb6iTbIa7pp8jfNBGdJKEcvZx9BjJ7vmYrSPTJPNlYp-8O33XUtNJIEIYyln4m32nbPSMyEB8FzCdfuIpXdeII4DH3lVRaofsRr42pxWOjU5jVPnbhP1w2ankWXwzh2mXBciEMSUbs7lIJsJ6N6V_6cK-g7yyrph-aC3ED9SrLTuomrmIn2H6jiHMqy7rlv6oR_qiNEWiDvIB88-TXEbuDTYYb0Ktj-7ZVa-8vSvLPH6uvWRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaUSsjr3XZOV95oVsrGyWwHJOi5Ch7L9BiQ5joE-x0_kP8bLW09b6GxHUhr_QTGu-O3xqyzNMxU0shQGFV4YZ_9zyI51Udcz6pDaYu0PRxAoN_NzGFadFGh-GJ_37SmnugGVtVGtZ5s6u-yDdiT18kp9toKmf2pkw8KlueXAflMmGoUPu55Xdsjsj4801AIX5lNyMEwXkztzM2R4-hTuZUythr86-R3pSBUJ5VCKfbHcwNnnOwx7tQADrAgmIpuMAfnMhcXKB8VEFrIUxbMsdkMH3PyNA-A-ygQ-aepLWX30agFSPC8FKk28Tcat7yazQoinOWbWD9CV2LmI1TTj1lYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaUSsjr3XZOV95oVsrGyWwHJOi5Ch7L9BiQ5joE-x0_kP8bLW09b6GxHUhr_QTGu-O3xqyzNMxU0shQGFV4YZ_9zyI51Udcz6pDaYu0PRxAoN_NzGFadFGh-GJ_37SmnugGVtVGtZ5s6u-yDdiT18kp9toKmf2pkw8KlueXAflMmGoUPu55Xdsjsj4801AIX5lNyMEwXkztzM2R4-hTuZUythr86-R3pSBUJ5VCKfbHcwNnnOwx7tQADrAgmIpuMAfnMhcXKB8VEFrIUxbMsdkMH3PyNA-A-ygQ-aepLWX30agFSPC8FKk28Tcat7yazQoinOWbWD9CV2LmI1TTj1lYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=Eo-7--1kgeCRL_zZCqSM_7Aq-uF2F3QoRm7UBx7Lwxko9AzpVv89f7kjiSi3kBW8ZJpBq9GQPhEmuTRLHaPOWb2I2wEStmKrPhQsm05peyK15cz9p2glLa1YsyqwxJDNbK6ygyyAZzuCSw8Bq3rof3HMaB777MAFnQO2cqxuTNhYnAweUklZWDyM4TRigPF3Z1Ap-azfgDlxGji_MIKy1koIw9-wF9eIMIkWYcT6EZStoXibYGyusEbIOwQLfMYMnq08suNJspbXk5mGr9Xa6ZYvCtLluocbTgd-W56FLDA7i95ZO9oyZb0C7PTbUYCnxKnACj72nmSqRCC_ft7UCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=Eo-7--1kgeCRL_zZCqSM_7Aq-uF2F3QoRm7UBx7Lwxko9AzpVv89f7kjiSi3kBW8ZJpBq9GQPhEmuTRLHaPOWb2I2wEStmKrPhQsm05peyK15cz9p2glLa1YsyqwxJDNbK6ygyyAZzuCSw8Bq3rof3HMaB777MAFnQO2cqxuTNhYnAweUklZWDyM4TRigPF3Z1Ap-azfgDlxGji_MIKy1koIw9-wF9eIMIkWYcT6EZStoXibYGyusEbIOwQLfMYMnq08suNJspbXk5mGr9Xa6ZYvCtLluocbTgd-W56FLDA7i95ZO9oyZb0C7PTbUYCnxKnACj72nmSqRCC_ft7UCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdafRjjIxGRt1irmnY4ysf8M9RrFYZ3EUa65rGUVoMZD_odR2lsOdj08euUw4cp2TNNCqPOLjsJFyXtMah802axQmgAEQVGvpxKYiSJ7OeGDAOEi3kpakh3uFJa7dinrtxlJ9wtzOcsVWn8iy2nx2Ge9jdr1U73TUysv91jzPwYWWdIyVAVgPNdeYJIa13ISfiKRllN6s1fgXXt8oSPj8DBkei33DSw4_sFMGDPdqVrGeUVsrXFlkuaJtv5-i3ORVq1m74zUoPls0dejykUk3VrZ0K0unb3FgpaCb4f_9Dl6ThTj3w2Ky_msYCjU7o2W8W8WC5arHNWBHu5eBa1rCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTig42DsbUP_gEbji9ZJz_DjejOn54sklHQrvdOq3qJtRJPdE8paJrjcwWeg2rIki3KAN5U2w89XZTJT1w8A78oS00H5PYlJxK-FfQP29vot093GJkKWkoCeJ42NjGECL96Er40gKH8BTb-fun5Kps_iYkHd3raj0lwZzobOWJf9CLorWmnKJmoK2BmM5NfdkLNxWdpswogPatLvaHNJuvg33sj-ebCpqP_qrUSgkO_T8e1tUYFL2qTmKzrDpYO5BOv7-8se-86T_agXfcLnRu5jcyX9oJsEvMGDI8l2ixZA0-c6ce0v2rm1tz0RSBue12VwgkXo7izqxmUGknGTLFI4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTig42DsbUP_gEbji9ZJz_DjejOn54sklHQrvdOq3qJtRJPdE8paJrjcwWeg2rIki3KAN5U2w89XZTJT1w8A78oS00H5PYlJxK-FfQP29vot093GJkKWkoCeJ42NjGECL96Er40gKH8BTb-fun5Kps_iYkHd3raj0lwZzobOWJf9CLorWmnKJmoK2BmM5NfdkLNxWdpswogPatLvaHNJuvg33sj-ebCpqP_qrUSgkO_T8e1tUYFL2qTmKzrDpYO5BOv7-8se-86T_agXfcLnRu5jcyX9oJsEvMGDI8l2ixZA0-c6ce0v2rm1tz0RSBue12VwgkXo7izqxmUGknGTLFI4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUfD2Yrk71iR0TOUkEcXnHasZG-vmC_wnewwKXF4urxKRHnqvGURVhxksTOS9F0i6YqEYjRKSGxygfw0-Y4ptnhicV0eCqcWf1EJrsyBgOPD8M9fylYu0lIeBPu5KWKyy8PG3Rzi6DdV17IC-GNcbK4fwEj9_TmlJOKXBwf7BzkYj7WD_NljxLVQ9tdyMkgvs9O9sTAd_41M_CxioenwfUIlZB7iUA5wcN4jXfp34K_Nj3vQEro9T5qFJCmhJfeP7aT6CFl3_OXhY7OhqCcycSyZsdplAvnk4bEyg4RlSB_S1kI6SS_uiasSd_cXaMwJQ9opBKNSP66jkZsDRQapOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=D2t7CqRUXqAJ4aEoY4UET9yyjJXuyQhBJ0d8Rq5I5-dlTIEf06AjO4iw9Y0gkiQrLVXMBcdW70k51pn6GT1_BbyWp8-6rFp1zR8k8lOjOv7ZWCJh2ZZxEz0mOCgFkNu6lnwswl6iLgJjiJfQWQXglE1mBnKr_vwMD-QlVjNGqU62HNzfuVoYWZx8ETNYd_SKlIcJmtwit4DVHGDLz9WORPEHyaIAELucq1XVF47bPHOZXIBVTyK998na3zI91t4pCFjSoy1yTKfQcQfbB2kb0vhNg7PbekJSRNRC8ikk9Q-lJ19WxkkiuXwSFxazYeldASgHV0NE5KMIoXEfYBSJdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=D2t7CqRUXqAJ4aEoY4UET9yyjJXuyQhBJ0d8Rq5I5-dlTIEf06AjO4iw9Y0gkiQrLVXMBcdW70k51pn6GT1_BbyWp8-6rFp1zR8k8lOjOv7ZWCJh2ZZxEz0mOCgFkNu6lnwswl6iLgJjiJfQWQXglE1mBnKr_vwMD-QlVjNGqU62HNzfuVoYWZx8ETNYd_SKlIcJmtwit4DVHGDLz9WORPEHyaIAELucq1XVF47bPHOZXIBVTyK998na3zI91t4pCFjSoy1yTKfQcQfbB2kb0vhNg7PbekJSRNRC8ikk9Q-lJ19WxkkiuXwSFxazYeldASgHV0NE5KMIoXEfYBSJdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=RS9pBC2E1EdVXfhdM0yDnMxWEL-ppWsyosjnXqqLk6vkgPmgDN99zJ34XTaOZqGiSPGcfE0U9lt5epud96YN0RQggL5XagF-RQZmidrhukqwBn1K8Zj3LPvKAeITbQ4USDGrRSgaPiww5gogPofrZSBXcc_GCSI6kMkkbV2RLk08KykxyIMiXzXOXzHW8yiCDg1E-Fqb6Xf1YT4NvPhPBBy4SG09neSZaokisP0CNTJX4ONMn-u-Rgtl-4YVutcADn8-_lyRcyTbu3IVTusOfG6ref3PSpFGQrKm8gracTTi3M2vqAzsQzJotfr0qnE62FIwdnfUi9BrFUsLXLh9Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=RS9pBC2E1EdVXfhdM0yDnMxWEL-ppWsyosjnXqqLk6vkgPmgDN99zJ34XTaOZqGiSPGcfE0U9lt5epud96YN0RQggL5XagF-RQZmidrhukqwBn1K8Zj3LPvKAeITbQ4USDGrRSgaPiww5gogPofrZSBXcc_GCSI6kMkkbV2RLk08KykxyIMiXzXOXzHW8yiCDg1E-Fqb6Xf1YT4NvPhPBBy4SG09neSZaokisP0CNTJX4ONMn-u-Rgtl-4YVutcADn8-_lyRcyTbu3IVTusOfG6ref3PSpFGQrKm8gracTTi3M2vqAzsQzJotfr0qnE62FIwdnfUi9BrFUsLXLh9Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=tKPQ0i79jiUOd7yjaLP2gf-S8HQXN3trIFDGquZKmZwzi9yJJYGN_fhbaqqnQ5ljBPRthUQGGiALqIT9vDeLOaaRECpl20YzPiBGISITkmrUVhU1YI83W0xete4MdLE-TVVGOSavgOu_fBEsueLzp8eamP0d9itxQtRNDz7bDRi-oEMbfQl0JTEgOJhPjC2aDmzyesaXu4WMslGgySmh6PfKdoa2BSIYWsjapP3yl8mdVEUqC1O8FgV_adoaJ5fie5xGB27SAraDhxlwpGzoLb1WIyfXb1AyxOxAn_yjnbDtM12kp8bwemZIt6UIZAluo5iojjkMItrmaNLiMhs-TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=tKPQ0i79jiUOd7yjaLP2gf-S8HQXN3trIFDGquZKmZwzi9yJJYGN_fhbaqqnQ5ljBPRthUQGGiALqIT9vDeLOaaRECpl20YzPiBGISITkmrUVhU1YI83W0xete4MdLE-TVVGOSavgOu_fBEsueLzp8eamP0d9itxQtRNDz7bDRi-oEMbfQl0JTEgOJhPjC2aDmzyesaXu4WMslGgySmh6PfKdoa2BSIYWsjapP3yl8mdVEUqC1O8FgV_adoaJ5fie5xGB27SAraDhxlwpGzoLb1WIyfXb1AyxOxAn_yjnbDtM12kp8bwemZIt6UIZAluo5iojjkMItrmaNLiMhs-TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb7kIe6kVT4w-CXrurZChpWWEnZ_-EyFsCu8B1mtsRBREe1wzpVQbuUgwiihrbkmtQo2mtFr2VzTPo8P7hnkQHiEND_AiC4D8PC8W_1wkA8MTtVDD5iZme9hXPELhesgcwrAYkPmNXVYh9EPOje2VeaVkscYJKGJlD0aDcB7XNv-Ui7oCV6qCbfEbDZtNNj66GrJ_FRkdb71lBWGtuGfI6exZHdkvax5m-nSQUJTuMFlFgINqgrlcsEChwDQWD3zYuOrWDFz0YBfNo8RHOlpRdDjW6GhGEoi8xgWLycgt9OTz70l7OM7xvVG-OPp-5AB2rvjTFc9OWyooLB9aAYd8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3a9yIljb_-1kyaMoeVkC0AXsqNk1kRlvSuun_5-CfkFNT87dqfCi7ge2PxVeSgOvn5zMrRoNDQjd0ZjSr3t1vlbiG1rrX-2eu4hHbI9yJSjuejkWIvaiBLbhgANZ7B4SbmzMoSQ3VJumHHGpW7359jo5_dUVhwiDD_ms5IeN6RELj0clMhnA-yA5suArGxosMU9xrZjyFOnKN2wWZHk361pGOLGtbLg49PksoaIZc9DstUsUSBJT9PFIrdJ2e7135ImgBEIIAuy8G-0NRw8QvdLpEkg-9lDmJldYZFRcvlafX3XSOIXTZ_mQnDoR2dScwVVWru8CeIi-3SUrXJzTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=dAOJ_MizM4uMFi8dBDljjZU7f2xBipvZMD9NvleIcbN2lSF9ekhrHBaaKi3TUiP5E04AjZN7bxTs8j4i4yIbk-nooB8lPddPk7EsGQFlCsOidDU0WYywfAEUOaXQ8PbA-D3cgkeRgJ8XHFHDU0iFIlAd5YsQUILKA6zuxLQOCPF7hK90SAGAcnrFrQqm-QS0zY8grm5YA9OqBnOC-Ml7Xn_WqDsSNsZYO0oAm8i-TLU45NxfY8mxrAKiwOt4OP2QItGWAg8aR86d7ADIzDoL6j_HnJmZAEEw19le-9eoEFn4P30BE6HrmPOFMFBdRWlqkKk95Lc8b77tPDL6NSestA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=dAOJ_MizM4uMFi8dBDljjZU7f2xBipvZMD9NvleIcbN2lSF9ekhrHBaaKi3TUiP5E04AjZN7bxTs8j4i4yIbk-nooB8lPddPk7EsGQFlCsOidDU0WYywfAEUOaXQ8PbA-D3cgkeRgJ8XHFHDU0iFIlAd5YsQUILKA6zuxLQOCPF7hK90SAGAcnrFrQqm-QS0zY8grm5YA9OqBnOC-Ml7Xn_WqDsSNsZYO0oAm8i-TLU45NxfY8mxrAKiwOt4OP2QItGWAg8aR86d7ADIzDoL6j_HnJmZAEEw19le-9eoEFn4P30BE6HrmPOFMFBdRWlqkKk95Lc8b77tPDL6NSestA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGRvu-AAo-vKKwZpz6Gku58-RQR9tdiVyr39zljdlSw5PL5NrOwioakCFeESNGkNgkWObiojMQim_ONzq2gBVLFti8upd9ZiZmBltCOak9WqZMqId9AFT2TlpzazCF_WhnpAADR-AvEnHGG1JcGv8ZjTFGZYAE8rZy_q41F7ONspdgHtuoRkaLTXGRjKAm-zMHl8AhZXl1tZgfuYExuds45IAhsC3gaPPNM_tx2E9vwsvTC9f39c9I65KNTv_dKVcPlKk3HvOg9eSrOhxMMmyKmXmMADNqCYHd8guWNnjD0XNVkF1fMXgpY1jfvx3nM77U1yYRZazd_BxXa14OLPmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoVRWVinqaTBNCamCQ6aIKqM_OnsZpdMf2LFEgi2O30kyG3Afijd6zWr9uDcQj-YTnlgZF3U3IE9cW5SyRe_fmWSwoB2BuRKfdGpDa6lZFGOivz_a-arW4B7XYxssU5p1yOvRsGRCDsJbKUj2YGbAoKlGISWSVs8EwmJkFXjp9y6o9nv2cARdvqpBOpB0ecmImRW8aU6KnghOvDcz4KOdtNfhbo9xNwQ2ee3omPFG0TkgqzJzAcu6vl4eyroanwseuFhQWfgV81rYLXEetECrGUNeabn2_4s97IXpZmhP2P5MaAZbCyrbLPvxZai2Ts_OpyUgWfsmAubx7PD_UaSxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=mLH9_xizFMApOzsrqkE-RHXCjRrU3Q8jAK4dxaiFsalzvtbZFcCCreodBMIiMLkh1taSKQDtNt14I-3Vo2nowMs8BeY3u5jyFK8Wzf7jYFhNAZ7sc6jI0UaNKEsCBaYJJNYBrau161dw4VKFU3fbYnoSscFwlTO4aSc8i60H9Q73bZ06R_h_U49tZYC0dalHgXsM69eYn-lfnicUrjTmQORECg_-UrjHlVppL04MAGGQhdsWnCWnr1EyWx-yt1lWAbySB0QjdmqzTcCRzqBc030Ckj9lbFq-WaLz7vJr8tzzLTI2QTFv5p-udD8k9Mct1JI9xFfNLR6kRiWvDqpUZ1ETt8NEGhuwksnV264SfHX-vnMZQyxWnaSk4qliJXeIiiXaDAIlUUvvACQzNCvO66u_P-k0NIXCDA9-dvLs9Lgd7tmxfxDe87EPRA8pdPImyLarxC5OYnogBY_u8cyIOGZWvAm7XaczvgEvOzEYvV4uhlUAMU64ZrzFzNmxzXj92gFjo_2YFpBsPmGJIThE5tg4hCZ7oqfYv7EZM_N8xkpiPIQDhZku6J4gvFAQOAPSiQ-0IbH1ZOHxkhtkEglbKUh6IquW3Bfp8Bx8WT21HqbYLU_uWHDSITOUx2cbfn08RelejzHhypXN-RoIMmt1fDVW600mIfHYA599ebkVAJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=mLH9_xizFMApOzsrqkE-RHXCjRrU3Q8jAK4dxaiFsalzvtbZFcCCreodBMIiMLkh1taSKQDtNt14I-3Vo2nowMs8BeY3u5jyFK8Wzf7jYFhNAZ7sc6jI0UaNKEsCBaYJJNYBrau161dw4VKFU3fbYnoSscFwlTO4aSc8i60H9Q73bZ06R_h_U49tZYC0dalHgXsM69eYn-lfnicUrjTmQORECg_-UrjHlVppL04MAGGQhdsWnCWnr1EyWx-yt1lWAbySB0QjdmqzTcCRzqBc030Ckj9lbFq-WaLz7vJr8tzzLTI2QTFv5p-udD8k9Mct1JI9xFfNLR6kRiWvDqpUZ1ETt8NEGhuwksnV264SfHX-vnMZQyxWnaSk4qliJXeIiiXaDAIlUUvvACQzNCvO66u_P-k0NIXCDA9-dvLs9Lgd7tmxfxDe87EPRA8pdPImyLarxC5OYnogBY_u8cyIOGZWvAm7XaczvgEvOzEYvV4uhlUAMU64ZrzFzNmxzXj92gFjo_2YFpBsPmGJIThE5tg4hCZ7oqfYv7EZM_N8xkpiPIQDhZku6J4gvFAQOAPSiQ-0IbH1ZOHxkhtkEglbKUh6IquW3Bfp8Bx8WT21HqbYLU_uWHDSITOUx2cbfn08RelejzHhypXN-RoIMmt1fDVW600mIfHYA599ebkVAJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETiGopSAlNlPlazJBisbRFZR2ENNB8CzweMWuEjaS-kAxESZZOhxvg2bNtXpftO8zHrTUo79Tq5Q1qmcp7dt6XCcXSsNT-mXFyXALL_6SHFK5EJl8Tw_9DlZNx65ybNdV8UrplzC93pC4LXGvgwRbFRlbd960V59jEV1wG0qthsGFHOK6qzl7Sg-TRz6zBXGrBjrJVpCeu8J2Dub3dfg-sE1qFFK_DCj5cpRu8sqd6tCSH8ecv2aIjnPOMMLrAjkIn9T97Na_jOivs0tcQXYwPFUfgWe5s0RD9RZSOvoZ96vb4GQlWZ0_d8Ji3h-qcm-lqqK0Kjfgf9eqX9ccj5z9cYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETiGopSAlNlPlazJBisbRFZR2ENNB8CzweMWuEjaS-kAxESZZOhxvg2bNtXpftO8zHrTUo79Tq5Q1qmcp7dt6XCcXSsNT-mXFyXALL_6SHFK5EJl8Tw_9DlZNx65ybNdV8UrplzC93pC4LXGvgwRbFRlbd960V59jEV1wG0qthsGFHOK6qzl7Sg-TRz6zBXGrBjrJVpCeu8J2Dub3dfg-sE1qFFK_DCj5cpRu8sqd6tCSH8ecv2aIjnPOMMLrAjkIn9T97Na_jOivs0tcQXYwPFUfgWe5s0RD9RZSOvoZ96vb4GQlWZ0_d8Ji3h-qcm-lqqK0Kjfgf9eqX9ccj5z9cYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=oyn3lbCxFyRI_-qhJTY_zV-n-EA7-vAGUCz09O093E91_zKREjhWJ-nUPbI1Kjkr8EQLWGLYSRUi_mocLRlnSr54YuF1k6bUK-LLIHWRYB-CfnxrwQLQEC-L-pfyCOlKuwhLi-r8d2M0EIuCMiZq_7phGfaJ4-0vOgzzPAeHiKDSu-BpSUbHCq8k1BYEiRLvZZcMZfywvf3IqvtDClF9raszulXKD0HgqnplFsNboxqNKO_4QGrF1ORItfmi_Jsu6Ysg8NiO_sqRiMWVDg9aBrBQN43tbSbGR-FpMb_HuVk3QOdSVA_z21RK6FNmJM-kBtV4PecHmlfQ0jUOf1Tvtoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=oyn3lbCxFyRI_-qhJTY_zV-n-EA7-vAGUCz09O093E91_zKREjhWJ-nUPbI1Kjkr8EQLWGLYSRUi_mocLRlnSr54YuF1k6bUK-LLIHWRYB-CfnxrwQLQEC-L-pfyCOlKuwhLi-r8d2M0EIuCMiZq_7phGfaJ4-0vOgzzPAeHiKDSu-BpSUbHCq8k1BYEiRLvZZcMZfywvf3IqvtDClF9raszulXKD0HgqnplFsNboxqNKO_4QGrF1ORItfmi_Jsu6Ysg8NiO_sqRiMWVDg9aBrBQN43tbSbGR-FpMb_HuVk3QOdSVA_z21RK6FNmJM-kBtV4PecHmlfQ0jUOf1Tvtoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=XDu2KGnyl28tL6YSwObr-rGeK8e-vOmRCaoCKW4ir00naBz2hPtwoqXLLmnyAjGs4sZMvVMJ9HneEUgUgbsdCSqjhnNyzxDcCm4fvAbI6NQeGjWwCJYEinkZ3ePzuT6AHCIuSOHH2c14s4jcOs25b_7_zMAF82iGlw5lsuuOgKJB8PysoWLn_zYFUF4-cEITz0BlJ0mykHtohVHbuWB7cNrxuQtavH5Eva1K3b2nAz3foKoUn4A_y0jaPQXLjKpbDs6--wydY4lR5CM7WC3wghBphNL_sxkPYY1f2mMIZBEnvK2z_nUheHQNR29jCR_rpLQyICdcZRtSiCcnhGvdvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=XDu2KGnyl28tL6YSwObr-rGeK8e-vOmRCaoCKW4ir00naBz2hPtwoqXLLmnyAjGs4sZMvVMJ9HneEUgUgbsdCSqjhnNyzxDcCm4fvAbI6NQeGjWwCJYEinkZ3ePzuT6AHCIuSOHH2c14s4jcOs25b_7_zMAF82iGlw5lsuuOgKJB8PysoWLn_zYFUF4-cEITz0BlJ0mykHtohVHbuWB7cNrxuQtavH5Eva1K3b2nAz3foKoUn4A_y0jaPQXLjKpbDs6--wydY4lR5CM7WC3wghBphNL_sxkPYY1f2mMIZBEnvK2z_nUheHQNR29jCR_rpLQyICdcZRtSiCcnhGvdvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEHhBGmkHrWuKkMlLgSOczuvY1eSzjFfvO5weyDM3T-3dvaGyDG1oxtcroCso8Hn5zxIHX2HfXVaJPq2seHm0yM9gPFvxFgqp-VsdoRpWp9WV0AeAgdUvvc3O5fidSzaPl3x6N5Ka_htBLJQ8knfsRNIKEGRNBvVqahEF_nwfQSSL_P1VPqOt1xsdoC1lKGDdWs0x-emtVkiW0mViiH8qb2yAqdj8yUitou3j8h264RwwtDIx9T0VmMiKLY36hScCDYglVPGnqDrXHmBgUZdxjL1ICMwPxfo8W5cq9RzagoT6lld1YftQwFvUjxMWgaYpAv_AVXfuAcahF3KPCOQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBcT0YPRM3GlFESKZblWLVO3zllVpPws3JsOIu_sA-RiIvO-MRd6UvF6m6cOlxdclpoIO0JMjwCYsFwrRExjLoCHWVp6-lTTrZtwuVp_B7DUO2M0N2HjAaRQZINUQBcw_n5VN5IgidbnD0WbAmzKMM4bxvxbZiVLyB9fHErw7RKU8dgTZIDOXM4RVgmsrXTmEiivDOAc0t4JLB8mP___PjKNpq2yZGvwNHUuHZSzbK5TkogiLMGx5wJw-jxXxUQhkaiH8dShKZERaG4-XTTagu4jQkPwyDXcQeVpSGkztG4QVY-0JscPtY7SUxi_P5Hd7uvX4bHtmrmKhDnQVXzyvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlIRF4DgAqoKkVnGVJmAqyR3H8cAUJ4nRY8GbXNdZvKS1FDXi7fa1GYsOt7FeURgEkvHGLVb30t_gLo4GGlyPzrSCH4PxoCsB68QlzxLgCFNAMyRbOXNiKSZGYtp4uAvrPQOUKERtsjL5zypETog-D1-Ft4tBR2FjpF0oEEa1oO7wmcvRgadogeWjTU8AuVj7NyfmqTVbY4r9rQj24vts4_-0IMKn6lo5lsMjM6T2JWIKId0_eQYZu9HknwuVuYGLXHK7yBWWU9nlsUlINsYRhIVVvT3MDCfuIOFZ-57_kGiR0DoWMoWhLG82dfYlaUToRlX2NY_g0BhYSVKItB_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVFzuYnhnL4sYEecpGrJ17QJgR8z619BdgTkd7bGaf42s0T2dP5aKneKiBT-Z0btMwy9XC426ZATMXKpFpx9Eth6TQtseVPBAOQfavs4NTIKYD35q0Q-1Ul-wBjtHq643o3W5CiJZD8hSVVaRua0jZTS9uZdgJZ6mZjVuRY1ZzXa5NerP2yQuSXm1F8ihZFrHUgoDMg4CaKgg0xNzjc0hF9tKoZLrbYxmcYHPvJmyRJGmtiEfry7z4mGeX7ypZZxPKaHP7arjlAwa1HZ6wkLHtihoAn28fwYJApn07VxdJrUKIDA_1_kdm7oFAklm0tBbhbH06RfUSe4bpC8ULN8WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUuQh4-tcA2CP1Jb_aKrZJGe2W4wW8uxR2iCeDnXZXbA40wEwz80JPE8WampNnHOYVDHD4Dli2QeCNw1mx_8pZZaBvt5C1uXIbzJnKROZzBZo14QzYG-D48V65iLeZd8M9KoJrz8164xrDiVpFD8gnD5fr-dxHxrNTPDIktW1Y1zc7hrd08v1Iuc869uxBig1ptPmJikg_ZpuVkJv2ecR1apLJDPsaAQ4mqS85pQ6NuKgwreCJc8Xf140Ek_qXg5fc1PdDB8m3IxP4fuy0IIfWRW1VQAMI2ymxAiMqrq3L_zj2pgVw0Ge5SmBj2c2ewkJLBefkJcl54clq965XtTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=SULtsDT9tvbqxbC1t28CiED96LtZYKD-KHx_-YXlcVQF3bxYf7hJ_8nglxMW47hm4_IxC8oQUlzhiii1jxAMBRVUHop-z8lMyyRSe-Sil_w47AE6AxqtIHL-MI-jVTWLdQUoXnQabPdYbblgQSsqzjZHccVXvRzTybW8RpESYbJJFCA15Mz0-gvc7bNDhHHdb-j6pKNsMaWJzUnfEkzjnKrqFZclxOYVfDSL1LdH9nGddnslTZmOdhKsvO8dt-OmB_qakFGoE6vbLr9u4LSLETE6BxFMbPKueEVoeZJRfXlgPaq8LyVPRNUHHPJ-POyRTkAEPFjazZ7SHDBAsSUjTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=SULtsDT9tvbqxbC1t28CiED96LtZYKD-KHx_-YXlcVQF3bxYf7hJ_8nglxMW47hm4_IxC8oQUlzhiii1jxAMBRVUHop-z8lMyyRSe-Sil_w47AE6AxqtIHL-MI-jVTWLdQUoXnQabPdYbblgQSsqzjZHccVXvRzTybW8RpESYbJJFCA15Mz0-gvc7bNDhHHdb-j6pKNsMaWJzUnfEkzjnKrqFZclxOYVfDSL1LdH9nGddnslTZmOdhKsvO8dt-OmB_qakFGoE6vbLr9u4LSLETE6BxFMbPKueEVoeZJRfXlgPaq8LyVPRNUHHPJ-POyRTkAEPFjazZ7SHDBAsSUjTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=EsyO8jEJKh_R-MEnpdchV530FaVHgmV0Med9fr4TqCuiZ1ZZIg_3J6qIc3Arjbj4dK70HTpZqMWV_BO_uT-tadKDh1nsY2Pe1sxJr_L8WGR0N1roQKmGcW20qanNfq3TUzUUnTiqO77uiIN8w2NMchCAwF_iX2DSVrgD-2wPd9VGXUNIcXXKgkfhcE20IKlJ5o9wfp2snaeuA6g2N0N_1lDIis46KPek4MFEwAidmzonHhHN_gQu4zdjpz4LZBA5OyyXiyi1hHQVNeVbVLQcoI5bHLx8_Rde2uwKQBErahxFc8CNfiK-JSH8wE3twUKaWywVGRZdXmy-eLCFWPciSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=EsyO8jEJKh_R-MEnpdchV530FaVHgmV0Med9fr4TqCuiZ1ZZIg_3J6qIc3Arjbj4dK70HTpZqMWV_BO_uT-tadKDh1nsY2Pe1sxJr_L8WGR0N1roQKmGcW20qanNfq3TUzUUnTiqO77uiIN8w2NMchCAwF_iX2DSVrgD-2wPd9VGXUNIcXXKgkfhcE20IKlJ5o9wfp2snaeuA6g2N0N_1lDIis46KPek4MFEwAidmzonHhHN_gQu4zdjpz4LZBA5OyyXiyi1hHQVNeVbVLQcoI5bHLx8_Rde2uwKQBErahxFc8CNfiK-JSH8wE3twUKaWywVGRZdXmy-eLCFWPciSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeOETwCQqJ7aQDzziUXyG49Bp1Sh2Xq5etf7J-R23VLiJNqzvxCjgkA8idIoOZS47yjmSVKminPvPLmtJKfb5IC09-PA1vRJq67mvTA58N1fd33qJaxcRok2HEAiblzfL9-_7cOhLY3KXOIAP9-4cIsZrC2AhrdqMhlS-ZBsGb0q6FKM1PuxS6bnu3bOwTW9a9_7Pmz10I9nZ_QS51ydZWsN_QXVeefkSHOO2PI4Uyy1MoB87yiiosLklDblLcn9sSqaD7xUsKlStNagEXFtok-PQPT_9z6b-40SRWq9cyHb5Uch9ga8-wE0Ko824XEK3B1inSI_Uy4P9yeTq1fkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPxZ9qhORo7t2D9wW8Tfwcgp8x9P7aJVZXSLoG0eZDa1sfWBfwacyLtXkEZR8poIg6zY4-wF2H6RXuQ4ea9YDM3bFfhu3wYszFCd--lOPdOIcKRzMc8NO7dJBlnJM9vOnEswDjAPj_-eLS5aZMyHLNxyFegeB8mlngJa4sbyU_wJcG89lyMfjRLfImLSjTdDaw3Np8LV3srzvwgj3Dv6hlS3zwYYasbBKSW9QpSPC7Mz85w8ekV2QaNJpTRzv4B9-XjKjkO_Y6vUjWvr2Ean1mjfJ-kywkAG9lAkEd-qSp7L2W2cHUwMaLuGUxZN3iMrMOhJeiDNzq9uIKd0AL7ixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=YKqOhsY6tnxRC9kQ2vQ2srkUBRCj692Z7DVsfDv4ZpYeNipl2WY5vC1HuJRapq_0g9HhcSjFnx4EwajFd6yU8ErdGRfQ7SA_dNWTI2eCYJvpcSHZtDu_7Pp9gjVo7_WlwZiMA-PrpiYCldLlluLt7_xO1xWUqi_Cs2Y-3FqbRfUHxtdMeXsIKV9WT44-UbaiR-_dQauGAVpHEXL0wcPdRb46RPQgVgoimtcal9JI4gOWDAfASB5LKfEbp5JTH3s4by3AcrutqL7hrMDcmHCm-qLBdB-lSCqd2dQvpHJ77woHw3xO44L96NYsoku0xEDNaOGc5aAamVYGQg2tWj0FVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=YKqOhsY6tnxRC9kQ2vQ2srkUBRCj692Z7DVsfDv4ZpYeNipl2WY5vC1HuJRapq_0g9HhcSjFnx4EwajFd6yU8ErdGRfQ7SA_dNWTI2eCYJvpcSHZtDu_7Pp9gjVo7_WlwZiMA-PrpiYCldLlluLt7_xO1xWUqi_Cs2Y-3FqbRfUHxtdMeXsIKV9WT44-UbaiR-_dQauGAVpHEXL0wcPdRb46RPQgVgoimtcal9JI4gOWDAfASB5LKfEbp5JTH3s4by3AcrutqL7hrMDcmHCm-qLBdB-lSCqd2dQvpHJ77woHw3xO44L96NYsoku0xEDNaOGc5aAamVYGQg2tWj0FVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ao6x6JDUOYrN5x9-KhyxYKFAzb6XsqntgMH3oYkBG7uADSUrHfE2pDv-U9tFWNlJDF-M180MxuJQ7lF3d4dQZPKAUlgDbdcsaiE3SLcG9bLMCFrUV_uvk4DC4jgHvW_srNLn0NzCo7Xy6zLUFo7al79NlTGaQbHKhlFPMhlxnPFAfcZzDDCjCzrq9glYw76EfB7JTbmF_EPdXRd_gV9FDOLkALi94qES30uh6gS2etJ1MsiH0FsIhRVwbDi8tOyZAgboGRpBLLBg2SN6mnCh2DGDPaNw30ym5IDCwgwwhPlecynRZoIW-E_WCL4smXHmxcG1UfIsg4KnYe4f6X0Ing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ao6x6JDUOYrN5x9-KhyxYKFAzb6XsqntgMH3oYkBG7uADSUrHfE2pDv-U9tFWNlJDF-M180MxuJQ7lF3d4dQZPKAUlgDbdcsaiE3SLcG9bLMCFrUV_uvk4DC4jgHvW_srNLn0NzCo7Xy6zLUFo7al79NlTGaQbHKhlFPMhlxnPFAfcZzDDCjCzrq9glYw76EfB7JTbmF_EPdXRd_gV9FDOLkALi94qES30uh6gS2etJ1MsiH0FsIhRVwbDi8tOyZAgboGRpBLLBg2SN6mnCh2DGDPaNw30ym5IDCwgwwhPlecynRZoIW-E_WCL4smXHmxcG1UfIsg4KnYe4f6X0Ing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HForCjavVAOIX-GcnpbHHpe2Avdc-Qadx-5ij9Y_fhE1KRPapuwoQAr74ZGFzWSIAoR-V796iZTdGiDt6yF5VGvSX1Apftxpeda8Fd9E45TApx024gE4z039NwxkxkK-JxPrXrAUL8s2TyQV1Bm2o6QrnbGp-8dYPnyjtZ5IU8ZazxG2UX2yndGKCrRnfoogh-L8EuhqZOvTe4yBbeq7MPrYUsXtYWIXy0OWSYuR2NscIUvdqBtN8NVA0rFH8cCL9amrAwCDT8H9yIl__fpkQPOs0AFoxgp0nlKC17Duky4SGVL3Bmw0dCMHIPCoS1EVuPJB30vcIxWqmND-KlQFhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGJxTtkU-IgM2tLCmWZIyoDP8j_5AmA9WKE6HHfFXjjHsE1kvtE1m3NB-bAoStOUVEC9N7E67eSr7IEtjrpmo41BwxNpCH2mfZG53ymcgHQeCJOBzbGmCxM2DUGVUtgegO4WJ8c6sHaKlKTcuF02Hf0e0BSpDt8YyUktVY9UMKsO9Xvf5WTNAF66velu9Tbu9siUfJ22HpCkz37E5-Bt4F0De0AkgNkrn0kr2klt50Fj6llGRMI181T9kHiqvybWTRYIWljfhWdEo3d5oivnZmmQY2XnMY-M6k988Ytgnsxsbxgh8ga3XMyjeo6kdew25hRKxfaLUHrb4cj0RFVF7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYB3paIfSPUqXqIXG8586yg9wOosEdY92fwPB9EDp05QnTSGRv3Hg-QJI_yOE32RqEeu6rtQ6LCV0MHOejDpdtNTERqgipuGPNwGYSyEFV3NAYi7DUgg9kZcBYId3Xe2T5M-T4s9yeooFKvuCcFgCawgfrYHN_B4eZGWM1LOpmLDPgddJtogMsmng2KqCRBkmYgC_xBrnKhdKjsJegnLZHAONlDtb9ov8GDPDbglb5Zw65z3EuB41DQKbrVybFCJSUTbVlhfAOw3GJNyJ5x1JYczJFf1aaIfFlhLdH392Z_u-VcqhldGBSAUyVhne1qGa4gqI9zR9CeO6caVY25O3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=vBVLyiv-itrN5ZxU4oVOd6aSySTg7ks1JBQRbPeNtLh0lsAfpHRTXp0MTYB4jWaKzEcdqagFxfRr7EGN_zamNeLqi4lvvRwOjjhbYx7NfnboIMpIsnmTo8EkpCgkojeuR1-hCuU1HzAbUDlKmT3abd_puQiPBxMVLDDlxUDbNRZF8Mws48Jd0asBEExtrSuuT3_fpHJFjwbI8AG7BnpKYYFokPDKjwnaca8_XTwTPO8esGqvTXT864STLkoofKiNsf7Vt8N1NuJzkByJwZi6XgDocOk7JtZZ5-0rSsQgF20siErb2fo_P_XV9nAe1-bq4C7DUSeG60S1y4N-FWXFPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=vBVLyiv-itrN5ZxU4oVOd6aSySTg7ks1JBQRbPeNtLh0lsAfpHRTXp0MTYB4jWaKzEcdqagFxfRr7EGN_zamNeLqi4lvvRwOjjhbYx7NfnboIMpIsnmTo8EkpCgkojeuR1-hCuU1HzAbUDlKmT3abd_puQiPBxMVLDDlxUDbNRZF8Mws48Jd0asBEExtrSuuT3_fpHJFjwbI8AG7BnpKYYFokPDKjwnaca8_XTwTPO8esGqvTXT864STLkoofKiNsf7Vt8N1NuJzkByJwZi6XgDocOk7JtZZ5-0rSsQgF20siErb2fo_P_XV9nAe1-bq4C7DUSeG60S1y4N-FWXFPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCQlbBk466yvHxmTJu3_K8IJUl84cY0DRH8PnX99Eda6ipXnQvdbqiWjB48QhhoXJII6z_qazwzeONdfBJSDKettQXGrVvIhSsJDEXtJToj8Ew0PaFmVB2TI0ZjvAajSkslLWvE3yYZhAny0u_baumoioETTOdjCNkGIMfk6Pz9NpwYEsYwfcBXQN3TtnfqlhCD0lMWBDRLAnTfray69yhaFQAJtXnzfPJ2m8eIVtSWet9Z2AtymVgePpkqiDoACv1ImcJ-E5L2mn_yB3e7LD-0PpfGKo2diMhtVnOy4GK263CHdAPywvSe8t44SZDXgBGADoDEI5lkC3YH5vo2ThA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtdxjBgw3EIP65dcuPqa9ZCIj2HUUykGZd1QODcjtjgLMWRb3TWr2uYs_4e2XsJwTC-1nUUDkuZBMn1lsuMcfRjTZkpEYmLxWfZ5o3JjFpIWWE5epB3_vkRb5pG1i0hkHo8NmnOI8ENHaoP6MgBrMsew7QsCLgiH8uslUBLQ-nxkDbsGUD_kMVqC20hYEkOf_IX_ecewBi9QWMq1DzYPckBL5N3OJTKzwHhQq_2s_FH8d9VB5nHhLPGKSbiuh8owlZ3xyZqT3I1HZRKKEthyEGXJa58C-5e3rq5JkDcXxf90fb8g7w6S_FJfo6hkMPBETBRM45DJM0osKvEcNdls7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0_m5bJ5UYk2p578Jrn_BV5c8hMhAIxgiuv-Gvmv1wyntVmLT_ealfVu0PBXYfe6ivclXzNP6t4e1aLpH3nOPz61lyAEznowWBMT9DvFaMSYAYRpQ-b8IX5tgE3l3Z4Pb3cBV5zADg5e0COXAXuuQg4DNHdrpOBeDRrUEQ7Y0ciQ30Z5WTFjvFJe7yndoXRhBvvExVS72CgMwwWfdmSyO2D486CF68XBIT9yKG8Y-6QILppt6EUSl5yRvqDhOSPIa9rqr_o8H5def-pyEhX1V_b2t-695WSig6p1fEclVQB9ZGlQbN0UBfCLfhyTBdi0zXBrlVKDIIdV2fUGAFvn5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYSjcLoRkysJbFKSCCJK9JGNiORAm4jFMa2ZQUQHTc9FVi6Ny0mbfgVnunTOsHRzmBLJbmIiAvuuVrnjVzgLotLDJHNEjQNs7oqxLX_ghq114qcPVg79Lbc1-SfPIPjRMsKhMY-7K5arEgJD0q7tt5MXRmJo2CxXNd2qrXbMO9VktL27sGp5frdhaFcsukDt1kvY5zM5a03pwYheIK5W5Y4U5WpDYN30ZvlcUYbhFukHxfYytXOK4EMa4XFtsM123hmLwXK4eZJ8MyV4PXFjMC02c_T56vsByQZ2SiM64GSA2PZJy9gDbyc3B8VQESXHcyxEIvoGZCSVi6LB3GKTzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=kxzyEYCyW5srUdvB5brTtIDvd4LhY6ojcgM2ZgLN92B73zPormJN7MPMg96oBvd7O6rjHccKQhxo1jjGqBnHZkFyQQ967i1HZWwYWBhBnGoRhp6zr7m1yvVOwNOMvAMEz1bz4Acu3HYF3whFxhdez6eRJzIYX6mETHHhRz8ZtuuPCGgrjSb3-VY5URaLsHiU51kbBpDvF2Bf6Gk40jItilqSInfRFgjfn5znboYWnoRW2nY9hprhjHEnDiBnAuIUuUK38ZxyXnung2z--yDH_eymWvbE5Vyi76H64ClhnEGIOjZZzMFZcODfMCslFycvAjT0L5Wk3AqJxfp-p0U1dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=kxzyEYCyW5srUdvB5brTtIDvd4LhY6ojcgM2ZgLN92B73zPormJN7MPMg96oBvd7O6rjHccKQhxo1jjGqBnHZkFyQQ967i1HZWwYWBhBnGoRhp6zr7m1yvVOwNOMvAMEz1bz4Acu3HYF3whFxhdez6eRJzIYX6mETHHhRz8ZtuuPCGgrjSb3-VY5URaLsHiU51kbBpDvF2Bf6Gk40jItilqSInfRFgjfn5znboYWnoRW2nY9hprhjHEnDiBnAuIUuUK38ZxyXnung2z--yDH_eymWvbE5Vyi76H64ClhnEGIOjZZzMFZcODfMCslFycvAjT0L5Wk3AqJxfp-p0U1dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QX55CQUibHNmFhAFOC_wUPbzfvCzt8tsKbmqISerB1EyrYJ4bmLF_N3Nr7IczW5zO2AB3S7YcA3UuqLsiQCYhxeHY6tO_JTC0eOviM6UDPHZ7T9hnvaoDO3zA3cUs280enbhaUTgtQyuYryA9b4z_d2KszVkGaAkJAZLeA_3L2MVOPqNqAueoWvZRFLHIL1vKDoTqUUWi0vKYNPbsJvoQcX-J7A4JtLerX6CxrdkeYw10lqrl1Y3uhF2vk2XxGRpFuOmpZVctWjJFo7GBxKqA8_OIolU4mWbIztHbZ5DZLjE2rK8H6OnO4u7757Kx9g3khsrz60dE5nfxwTTWi32Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oW55PJn5gn-k6qqRWVer8sYJXWYzKuTu1XAuQjwrPSPrRWq4qjXc6XOKiOVupFY5Qwe8EOGzCskZdujZ688lMmFKntYCHs9nYBxsP7kVoCD6x44tnRbEb39bjlruBojjg8pozF7lrPEqnOKsUphPLQvUY3aTnHatrlQDqZYO9E6LQDSx-ziknCOW3qRCswzyX_b8lcEStWnc7W46ofrZycoWegKDUpS29SI-5vClkVzSrV9RtxjnzJjvSgA6YiGK-oNe9MGyGIr1YJRIhBv79PvDrPjzdGv3LxJYeIaMFkNhZ0WMJg261jn5xo90YLfgp5V5If_tojbtuVf8PxCqyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Shqnd6dpTSlNTaExP1hcNSrEF9p5LrGDLu6Fbp-Vm6X_oMZJh0oH1aV3q9qvKiuwKMM9XAAsLwl_qdrmL9MnAWuxzBXbNWRMKMPhDxUsqrhrg0AZR-MZo3i1Q-8zejKjN1TlGYsnj3ByqLc-W_95_utLv6rJNKLQlH16nZV9ihdyxI8ft2kJxJP1t5Ua2h_H-VDSltknfiir3cbj4dd1C9JhEHR4cAmD6lKUnUjA7U_1DUwlkv9MXHvXhlks5ZY7UgJpCstjugyr1PrU4QaI_bbO6DKEpGlfSrenhGq70u4nc1bKY_63hdrh4JzjTFX__SW7T0DLnyPyTA0AJR-4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=UzPeC_Nfm_I3KTBN0hIwDtt9-DOLi85SmMa7U-EvTOmOOs1WUiBgC4IDPWElP_cO7DMoL_ceRKav7Cr_aWfLOZSveX6XHIkFNyIglHQvSr49_t3fQ6XYziOCKtBtMzCQ6IIlhG1PmV4NHtRNN5I7zyFGqglAlzVKNEgzC6gwnC6DrQUtS_ELkuKUVny-FwNwEcIlhPKAScWZsozqshysNlc4GQ3oX2GBfYeWaOQxJpq4sEDunEJMRiGWI3KgmzQBDV_AY7eJNBuzGWY69pOWwGJHVCFOQZR-51tFUyUECB5bsytuie9BvdRHiDg9n-aFEdYg89kPTHLACYrIm6hVIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=UzPeC_Nfm_I3KTBN0hIwDtt9-DOLi85SmMa7U-EvTOmOOs1WUiBgC4IDPWElP_cO7DMoL_ceRKav7Cr_aWfLOZSveX6XHIkFNyIglHQvSr49_t3fQ6XYziOCKtBtMzCQ6IIlhG1PmV4NHtRNN5I7zyFGqglAlzVKNEgzC6gwnC6DrQUtS_ELkuKUVny-FwNwEcIlhPKAScWZsozqshysNlc4GQ3oX2GBfYeWaOQxJpq4sEDunEJMRiGWI3KgmzQBDV_AY7eJNBuzGWY69pOWwGJHVCFOQZR-51tFUyUECB5bsytuie9BvdRHiDg9n-aFEdYg89kPTHLACYrIm6hVIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=vp6b68nTCUes8Q-5Z-6G5egA_GYByv0q3elEIyeb4_C223OHRnClgm-yJ0j6uHIYg5k5GQKrzLQM-OKWvxfp7nvi9LiCTyjQVBhQr9EgEPCb5OKBiKpt9p03MR7wBO0m-HqmdHf6VMi9X-3NEmAmARAx_COAlJFP1FnQ0wRJlRWYwcLlSNzv6DzaZ8jYPOyS33vtI0PqjMeX2-Qg23melXPH6tXHdvzVQSa1HvrELxM3cOjoAr0Fg2oVKVsHJNM-JthU1ng4fX90Z6c3Vtx5ImE8uh54hT7FTU4kjC2279sF5_erMZGUIXR0d_cbcTAA8cbCphZDVBOvEn4Uj_IHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=vp6b68nTCUes8Q-5Z-6G5egA_GYByv0q3elEIyeb4_C223OHRnClgm-yJ0j6uHIYg5k5GQKrzLQM-OKWvxfp7nvi9LiCTyjQVBhQr9EgEPCb5OKBiKpt9p03MR7wBO0m-HqmdHf6VMi9X-3NEmAmARAx_COAlJFP1FnQ0wRJlRWYwcLlSNzv6DzaZ8jYPOyS33vtI0PqjMeX2-Qg23melXPH6tXHdvzVQSa1HvrELxM3cOjoAr0Fg2oVKVsHJNM-JthU1ng4fX90Z6c3Vtx5ImE8uh54hT7FTU4kjC2279sF5_erMZGUIXR0d_cbcTAA8cbCphZDVBOvEn4Uj_IHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=F7CKWvfs-ci7wqNXIirJxkOvtzbumyYXAHOt2o6C13CvUiY_3DSDygv5EMtcIntkRUio96psGlcMGtGvgoYSJqjypwDTha4MpBz0Znf558XxX_cHb8ZvB242PeT2ZYH5pYXzFvPjqZB4d4GU3sjv_x7tBdIF9XSuPKxa10NEX8U4yuIRkC0RtVFBf-FsKoDonhO5louJ7rpvU7tX_4DlHKY3dRX52I-NKteprJC3ul4VAROg7IDUw5rf8D6rvBpwdqK0NYpLIRoVSCeHu_dnMqSSKorQNmaArp-6PK_EjC2TKV2aUa-rvwk8d4x6GLoh0aLjlEkOcueUDtpnNRYllQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=F7CKWvfs-ci7wqNXIirJxkOvtzbumyYXAHOt2o6C13CvUiY_3DSDygv5EMtcIntkRUio96psGlcMGtGvgoYSJqjypwDTha4MpBz0Znf558XxX_cHb8ZvB242PeT2ZYH5pYXzFvPjqZB4d4GU3sjv_x7tBdIF9XSuPKxa10NEX8U4yuIRkC0RtVFBf-FsKoDonhO5louJ7rpvU7tX_4DlHKY3dRX52I-NKteprJC3ul4VAROg7IDUw5rf8D6rvBpwdqK0NYpLIRoVSCeHu_dnMqSSKorQNmaArp-6PK_EjC2TKV2aUa-rvwk8d4x6GLoh0aLjlEkOcueUDtpnNRYllQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b17wJbymSh0nSxntQ34kywpMNANqGtor4EgHSn6dNyLWNHdYyYKjjZlV7_FbEZ_0uIvHAwspN1LVrp2GNwv66PkznvLB2ir0WjkQgQpeP9CR_JPi80A3nA9QkJy3fLXZR4EQVMV85S1-tbNcZE3AsI1ZcAF135pmindps0TQ6xShEAtbL1EuanI0EcPjbA_LApDIe4mC9_gLU2GrXBsOuyJreLCFb1CL-jERYaCE8fLCfKXcVTPTy2ckNWmaScWK_2tP5HSvu82Zqlz3ZiLapqhjnp4_tYoN-EycmShHcw413wy3NunjrTHrrVPvYRcmiY5mUZeLnwiBLQsHJ198bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnIHAhhuYLMOwGpIFGacLuanjAuA8k0WlcqVpnlXfPf1Pn0GI9u-F1BofpHl0peKAA9fEAHFii_KsC2-R2PkkW_NryBA20EYWgg6sOapZ_712-01UBNrgP57SWvCi5fDQSCbcW_JQT1woa4PppeP1tH-zlLXkDaCMzd-P1I8wcaIT0L-P3lmrFyBfiN2TW_yUiAmltVGZ3G_aBv4cG0ElqcyExfdfW-VmTFD4qi8_U_o_IYjcWA0UNxmgAxNz8IcVgj6AFGu7WyRfUDeLYDOY-Oy_XdTJlejMfze8c-kHd7VXSuUtJ5z3L54Zv_324MghKD73hfbh9n_-9K-cp-XwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2Omm-H5pnhKx00bhAzbhb3Mfn1quGojX1OepQyEmNtvZmwkvfTld5OjGrqNI87KRIoEEZFsH5kUNEg93tBSjxWxRqugEdEb_g74UArWLRI7B9K_6dSTxHmSWhy9Zy1AHZ5fLo0NBvDWTCC7J_7F-rRj5WySKo0notA900ijIoWua8sjqxM2011l89Wwp6ovOyNrUUe9iC-3gB0mfyTHGlUfFCFu9lWe8M13tgamumRNdHKWUZbGF2CkECO9FucCtqQWaERHHeYc-dz6sOPmgOnG6dg7dqtILTq3qqX9Om-Yxzdg8LKpk4SEoLA20FFAYqpYZraNWEl737WVbfTOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYc58BNAP9BHOaK0Wy9xax_iCFEPXBUNoQt-WYPNMiVxElftZv_f7AnlLBNqIvS_b405bMAGJ8odNGCfKecsTeYnubFK8ApIorAP0RnjUzi3PgBB1z8qY4qVKYzC6NFvvmxykTMFPgWir1acTjI-Hch5uYGL1j2hkaZH5nHvTLLEM_cdrstw9GtuEtiHMWgTnjb5rYCGv70yp2sYeVe61PK5W95No6k1bIL83dEqfCyCLDQcZpc4hh1onmDd4i0csls5YT2gpzh6xRk3s5CPd6AqPaZ1Z2k36FaiN5nLg7gkjeGnQeIJs8Xa3Dxlk9Rg4KpiGQuLbB_gIyM5mqRYUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jzWnQHSL9VwBCvIZIufZXlqxPtCRQZfFvO-secrXQVgx4pmfByllNVyArACIlSZNryasUoYdl2_Tbnbly6tc7zD1iD-iI634A3Ksr3bpYS2qzA0ZmqLMM7BtCVbvaGVS7nPqF5FSRcWMHre4SdC7DwAg9Jo0rL_oxWUc9j_-wWtTHGzgDdT0VWX1j3tLjYGFonl5F9WxYlnHvMeEYGwuxHMJLgs9xvH0dNaPljpXOHoqsCth6dZSixKLDAjXZbb4lXUb0BKxxNyvlrqL7y29trcu1-tx_DiPs5TQNtzwtXu3pVjSHVkCaXPs1eykj5YY0FpgfdQZQYCQWiCZ4EJz6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BhXz8wT2yFbPQA_X3FHvdQRDiduLeDSo7kOlGYN83zO9vT2WlWOAg9oKXemaoxcOAJtGcMIvvuInthzNDFQArfEGV1j-envRUlqK4HrWqhGqkcgP--7WUJleeRh7cSTFzPRnOhzJs4jyvIKAs7kYThB1rHTExIdqKUo13s8-PKXZ9M0t7Led4nsd6h72PnMZ0G4YB0r646qfcg2-dre04_piIiwqwcUjFi33C1J8T6bBDUMbhJHrj7MBopuXSc36hEkbysayoNPVK1seDACDXffqEyH1V_C_0-5VioKgAXbsh2oikfG9o7aKn6bYO2r5dBUahfb8GMAZ4t6cg5Z51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sBm_WN5UTgKdOmSMlTbI-JVGWVdp8-vP3NIm9brJAW5aVTW9OkqCnB5KCKtDIfOmunJGZvUfhcmgb1vBPYtrV7ff27rU7VowzFfzwfsOnSObGFwTwnzc1c0lagylJka7kUS-CtqXcTO03qOonu7CwUdCDW70aQIpn_Og0mfOrdTEdYTXZZ6DAWHS_DtxZaxScmUpt-SfzNt83RzcnmVNc8Utv_L2sx7jJsOAnDawfJM7T862bCSuMPN07zfEkgrJ1WuHYEweNDuECG67djEZPcUW_fF6JWmBNFIlJz4YtVFicteNUyseUYAg-Fadsil62Kl2TZ0h5MAgV6MMhuspeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqD4OiFe15v9IMVJ_SIEzjWUejoIv_dnm5ikY7MGewU0zUIdBjlfmDquDQ2VQYpQpUc3yBbjK2rBfK6p_Di8tWwKyCj2iQ1EzQwqasUqBQMGf0XykHz6Ef59w3Wh0MTT_8dfBczfw2SZycszbkj9gmutxS8O_q8VXaf9yq8_HxzvnJfI1h5ACs-J1LusUwcNiKQ8pr8XleiCRPa9fcsvoyjNAr9LKURYum1RUJ4YrNyctvFsb4A7HCoiuBQzfqdXZ0K3ZuAwawEcgnDWToopTGLybQBc9RDeVvFvTvjFg2v6Y95luoi_uJPO35OrNqlbVRdMqXr_rRgATzuQEHCJDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnc8MCvrUlX1lZOOSM2m4uri93in0ItijkaaPnxco_0hfM-5gXGgQvy0HxtU7RHtMq97i1OIBm5lZH7QWB824C4gp5rml_hhGN34ALozwm_ZWJEN_51cYAic0WMfaroIkqfNXoxyJ4X4qn1Sn62PzuItwx-Oz8USApIezuUZCAjWqa_vbwd3gIxp-vQ9sIqkPKUHXpi9RtF_3KNyrV2kQVa0tB0GuUyC-piKEIholdjnf_oh-DJzVuo3E-wWhapj44ibyfPI1BuNMKh6gLwHCWiczRxXCGLUYHsUW9JX0N6cDOMS6GSxS-YPBY0JcDi08tXPNrKnj6JlulUykdCnFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0NxzbmcwqKtUCF2JAbNOHZVrFEloSdDN82d3KlOwq3JbpgtSjxOZoRqV7kmr7o1OnZ3Yw_mpOANs2sWO5Fp_3Z5Ccov_99soo4hlWjShicjzavGoePyAyronr9zcs4PYWgaUzHPBKFOWw-m-db87BQDJIw3s8LaL9hF18lreQefOXTDg0LRfBpeuuip9lQ0IZXscDA-Ng2kueVc3f_Sh6FADSYgdk30-3_IeclUwaZVqzlxM4FCDQTvyONdIrexbty9q6lOtzDL-Dej0GlN1XlRMYJmUCC8Py9t0NC4AuVT67z6n7qnfMXSN_OZwLHjEP5FN5lkRx3uZVXW-1YB8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q38ublhtkgeKt5Xt47new5faZ0OGuM98lmX-CuboyLbSq1hPbee7J2aeyzC08wDvSNw2XcUXL9OoazQc0sIbG1DSXSG-H6qrnoOqnSHK1P8lXSIgdwaZljzIWDBp5lUG8hN9tjZvCihrMFi3mjP-524EpkFnwXOrPGqNshKPLZRCkQ0qP3bkgco0acePVqziOJ1zvhHtsvxrjUDmw-53jn_jZ6jdLwyFrNwjsgWS-ti888qaMoypJjPCD0kv7DuqCo8K__E1T3bup92yM2LNy6DQONmzynslblBzPCovYRQUPHTpKp-XPFSZLvUoIo8pmuY1ETzR-oiMr4QqnvLTtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACMcu8-lIi-NSwoiWdpkBDUn2gytA8hdkLsruQFhTyDUdghoY_dRVDgWEcV-YgEMDRoqCJZbjm2iOTY2ulj3cvuKoB5JOuWtTn07PlAAXFrZhVgVzIfVHIyX1eTradCzsngGY_MvIsiLyl2uNHiYCX7Jj-Blbu2-YQmTxvSAScRDq3TulfM0nTW01uyDzFu12i1av4z5f1GlhEe_p4uRwr4rvrdBp0kjxNuhS1PHcnyPhJ_Ev36r2ZA5KqNr8ur3SdDsBpsnV411k8yvPzw4YMUr54FowoShQRb-YZkmvw_qF1Hz3YN-sCYKV9dkBlj1Ww-UI4-3NE8Ijh6KLjWPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SktAfupzYCQJVYP02s0by5V_e70tu_txHB7U-cH1otguiExOu9x9tAZWRqXKT8XdAHoZd6Q9TNTJ5ihFIqQWTR6C55NGmxV-pZeW0YE0OZhOPuoDsgkmsNY9I4KQ9-ZIUKPfyZZ9hgXwZRj4jwMY3946cQyuMXGXT93qfcSGDz07C1_G2jFj2GK-ja8AXPClUh7mtAKkUNuNHPPjC21_1EfhJT30Oxez91rPBQvJIi3w0ePUhckhXr63T8-1jhJs_QbwRPG4mRmBeQK5nf28hnPhDrjtC3bqOZh1l7xC0e89TEHNC18XX-VtbtlggI2Vsm0Ys-df7kc7oaxoaCcpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4PtHZzthMUnUco6tigIWNqNHdA_8wqdIUeYpqFB7mrd0bz9vt5qQliJUEjL-rk3QiasdyCEiLr6wL-igsjc0F9XjI3m-qlyue5zhTe2aVACDI6K3fccMY0WsA6cTQhgiCGbuZufJkNueHVF0O8mRIQ0INU5t0p4oL9iinbCQ5aibexgRgcGMc6pyljuJwZTeZQ7N4x7yTj7FiH0s6MBBraU0pBwQNxSg27Pbpb-JMzxMaAkzjnlsk0t57Fxz_Mx5Cmp33c-Nn1qxvMSBy654Cu7NqGGVs1nqaETt3-Jv7419_f4IvabpixqlaRxv6C2nhLGTwyo3dNZN5wGgroxVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
